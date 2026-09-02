<!-- COMPACT_REPORT_HEADER_START -->
> **Vista compatta:** Decisione operativa, Global Confluence e cambiamenti giornalieri restano aperti. Tocca il titolo di una sezione per mostrare o nascondere i dettagli.  
> Tutte le tabelle e tutti i dati restano nel file: copiando il Markdown raw viene copiato tutto.
<!-- COMPACT_REPORT_HEADER_END -->

<!-- COMPACT_SECTION_START:decision -->
<details open>
<summary><strong>🧭 Decisione operativa — da leggere per prima</strong></summary>

<!-- DECISION_REPORT_START -->

# Decisione operativa sintetica

Generato: 2026-09-02 05:32 UTC

Report separato completo: [decision_report.md](decision_report.md)

Sintesi automatica dello scanner: l'azione spot viene copiata direttamente dal Global Confluence; long, short e rischio restano filtri separati e più prudenti.

| Asset | Global | Direzione | Spot | Long leva | Short leva | Max long | Max short | Rischio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +8 | BULLISH | ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA | LONG PRUDENTE | NO SHORT | max 2x isolated | nessuna | MEDIO |
| SOL | +7 | BULLISH | HOLD / ACCUMULO A TRANCHE, NO LEVA AGGRESSIVA | NO LONG A LEVA | NO SHORT | nessuna | nessuna | MOLTO ALTO |
| DOGE | -1 | LEGGERMENTE BEARISH | EVITA LONG / SOLO RIMBALZI VELOCI | NO LONG A LEVA | SHORT SOLO DOPO SPIKE | nessuna | max 1x-2x isolated | MOLTO ALTO |

## Lettura immediata

- **BTC**: Global = **+8**, spot = **ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA**, long = **LONG PRUDENTE**, short = **NO SHORT**, rischio = **MEDIO**.
- **SOL**: Global = **+7**, spot = **HOLD / ACCUMULO A TRANCHE, NO LEVA AGGRESSIVA**, long = **NO LONG A LEVA**, short = **NO SHORT**, rischio = **MOLTO ALTO**.
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

- Global Confluence: **+7**
- Confluenza: **POSITIVA FORTE**
- Bias Global: **Rialzista**
- Direzione decisionale: **BULLISH**
- Azione spot dal Global: **HOLD / ACCUMULO A TRANCHE, NO LEVA AGGRESSIVA**
- Long leva: **NO LONG A LEVA**
- Short leva: **NO SHORT**
- Rischio: **MOLTO ALTO**
- Conferme: Doppio minimo target raggiunto finché mantiene 78,73; nuova conferma tecnica sopra 110,04; milestone analogiche 105,25 / 124,40, valide soltanto se rientra anche il gap frattale.
- Invalidazioni: Allarmi sotto 82,37 / 74,20 / 62,19.

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
- **Lifecycle EMA200** = per SOL resta solo contesto, peso Global 0; score interno 2; EMA200 circa 111,28 $; upside verso EMA200 +11,03%. Non autorizza leva e non aggiunge punti automatici.
- **NO LONG** non significa automaticamente **SHORT**. Lo short ha senso solo se il quadro è bearish o se lo spike viene spesso scaricato.
- Per SOL, se il Global è da **+3 in su**, la decisione non deve diventare bearish solo perché lo scanner grezzo a 30 giorni è incerto.

<!-- DECISION_REPORT_END -->

<!-- PAPER_TRADING_START -->
# Paper trading automatico KuCoin

Generato: 2026-09-02T05:33:04+00:00


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [paper_trading_report.md](paper_trading_report.md)

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-09-02T05:05:30+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-09-02T05:05:30+00:00 | 2026-09-02T05:05:30+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-09-02T04:45:00+00:00 | 2026-09-02T04:45:00+00:00 | 5,8 min | 25,0 min | OK |
| 60m | 12 | 2026-09-02T04:00:00+00:00 | 2026-09-02T04:00:00+00:00 | 5,8 min | 45,0 min | OK |
| 240m | 12 | 2026-09-02T00:00:00+00:00 | 2026-09-02T00:00:00+00:00 | 1,10 h | 1,00 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Combo Adaptive Side Regime Guard V1 | UNI | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Master Adaptive No Alt V1 | USELESS | 60m | LONG | 7,75 | 0,00 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top20 Long | USELESS | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top15 Long | USELESS | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Forza relativa 1H V2 | USELESS | 60m | LONG | 7,75 | 5,50 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Forza relativa 1H V1 | USELESS | 60m | LONG | 7,75 | 4,00 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Principale 4H | DOGE | 240m | SHORT | -5,58 | 6,00 | 0,42 | STALE_CANDLE | 1,10 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.8 minuti; tolleranza 60 minuti. |
| Principale 4H | ZEC | 240m | LONG | 5,50 | 6,00 | 0,50 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.8 minuti; tolleranza 60 minuti. |
| Principale 4H | SUI | 240m | SHORT | -4,74 | 6,00 | 1,26 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.8 minuti; tolleranza 60 minuti. |
| Principale 4H | HYPE | 240m | LONG | 4,46 | 6,00 | 1,54 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.8 minuti; tolleranza 60 minuti. |
| Principale 4H | XRP | 240m | SHORT | -2,33 | 6,00 | 3,67 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.8 minuti; tolleranza 60 minuti. |
| Principale 4H | PEPE | 240m | SHORT | -2,31 | 6,00 | 3,69 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.8 minuti; tolleranza 60 minuti. |
| Principale 4H | BTR | 240m | SHORT | -1,06 | 6,00 | 4,94 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.8 minuti; tolleranza 60 minuti. |
| Principale 4H | BTC | 240m | SHORT | -1,00 | 6,00 | 5,00 | STALE_CANDLE | 1,10 h | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.8 minuti; tolleranza 60 minuti. |
| Principale 4H | SOL | 240m | SHORT | -0,87 | 6,00 | 5,13 | STALE_CANDLE | 1,10 h | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.8 minuti; tolleranza 60 minuti. |
| Principale 4H | ETH | 240m | SHORT | -0,19 | 6,00 | 5,81 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.8 minuti; tolleranza 60 minuti. |
| Bilanciata 1H V1 | UNI | 60m | LONG | 7,75 | 5,00 | 0,00 | READY | 5,8 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Balanced Long No Rhv V1 | UNI | 60m | LONG | 7,75 | 5,00 | 0,00 | READY | 5,8 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Fast No Pepe V1 | UNI | 60m | LONG | 7,75 | 4,50 | 0,00 | READY | 5,8 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Fast Tp2 V1 | UNI | 60m | LONG | 7,75 | 4,50 | 0,00 | READY | 5,8 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Rapida 1H V3 Filtered | UNI | 60m | LONG | 7,75 | 4,50 | 0,00 | READY | 5,8 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Fast V3 Nohigh V1 | UNI | 60m | LONG | 7,75 | 4,50 | 0,00 | READY | 5,8 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Fast V3 No Esports V1 | UNI | 60m | LONG | 7,75 | 4,50 | 0,00 | READY | 5,8 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Fast V3 No Esports Mfe Lock V1 | UNI | 60m | LONG | 7,75 | 4,50 | 0,00 | READY | 5,8 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Benchmark Donchian breakout 1H | UNI | 60m | LONG | 7,75 | 5,00 | 0,00 | READY | 5,8 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Donchian 1H Gb20 120R V1 | UNI | 60m | LONG | 7,75 | 5,00 | 0,00 | READY | 5,8 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.811,21 | -1,89% | €2,65 | €3.000,00 | 0,09% | 6 | 56 | 41,07% | 0,87 | 6,86% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 56 | 2690 | PRIME INDICAZIONI | 100 (mancano 44) |

- Trade del Principale 4H chiusi: **56**; win rate **41,07%**; profit factor **0,87**.
- Expectancy: **€-3,30** per trade; P&L netto: **€-184,95**; max drawdown: **6,86%**.
- Valutazione: **Si può osservare la direzione, ma il risultato resta fragile.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 6 | €9.811,21 | €701,54 | €2.104,63 | €196,25 | €-2,72 |
| TEST | Benchmark Donchian breakout 1H | 6 | €11.231,18 | €4.071,45 | €8.142,91 | €225,68 | €5,43 |
| TEST | Donchian 1H Gb20 120R V1 | 6 | €10.966,75 | €3.975,60 | €7.951,19 | €220,37 | €5,30 |
| TEST | Main Side Regime Guard V1 | 6 | €10.964,56 | €751,96 | €2.255,89 | €218,34 | €-21,17 |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | 6 | €10.914,47 | €1.083,77 | €3.251,31 | €218,28 | €5,76 |
| TEST | Scanner Top 5 Long 1H | 6 | €10.852,64 | €1.133,45 | €2.266,91 | €217,07 | €0,00 |
| TEST | Combo Trend Side Regime Guard V1 | 6 | €10.788,53 | €2.851,37 | €5.702,75 | €111,46 | €40,76 |
| TEST | 1H Fast No Pepe V1 | 7 | €10.575,84 | €1.337,57 | €4.012,72 | €211,52 | €0,00 |
| TEST | Combo Adaptive Long Only V1 | 5 | €10.455,92 | €2.279,33 | €4.558,66 | €207,30 | €0,00 |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | 3 | €10.374,80 | €2.424,70 | €7.274,09 | €154,26 | €-3,20 |
| TEST | Rapida 1H V2 | 1 | €10.363,82 | €749,31 | €2.247,94 | €51,80 | €0,00 |
| TEST | Sol Donchian 1H | 1 | €10.331,04 | €1.019,77 | €3.059,30 | €51,67 | €-0,43 |
| TEST | Ampia 4H | 8 | €10.307,55 | €1.071,19 | €2.142,37 | €207,40 | €27,62 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 0 | €10.300,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | 5 | €10.282,66 | €2.160,68 | €6.482,05 | €205,36 | €-13,91 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 0 | €10.271,73 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | 5 | €10.246,90 | €1.220,23 | €3.660,70 | €204,95 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 0 | €10.239,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 0 | €10.235,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive | 7 | €10.226,17 | €945,51 | €1.891,02 | €155,75 | €4,59 |
| TEST | Btc Bollinger 1H | 0 | €10.209,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Nohigh Range Only V1 | 3 | €10.204,53 | €1.564,63 | €4.693,88 | €153,18 | €0,00 |
| TEST | Scanner Top5 Btc Tp3 V1 | 5 | €10.198,94 | €1.803,17 | €3.606,35 | €201,46 | €4,88 |
| TEST | Scanner Top5 Btc Runner25 V1 | 5 | €10.192,97 | €1.802,12 | €3.604,24 | €201,34 | €4,88 |
| TEST | Sol Adaptive 4H | 0 | €10.191,22 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 0 | €10.185,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V3 Filtered | 5 | €10.181,06 | €1.212,39 | €3.637,18 | €203,63 | €0,00 |
| TEST | Sol Donchian 4H | 1 | €10.159,24 | €449,62 | €899,24 | €50,98 | €-37,14 |
| TEST | Scanner Top 5 + forza BTC 1H | 6 | €10.154,80 | €1.063,56 | €2.127,11 | €203,11 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 0 | €10.145,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 1H | 1 | €10.121,32 | €888,04 | €2.664,11 | €50,62 | €-0,37 |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 0 | €10.099,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top10 Long | 5 | €10.087,45 | €2.258,24 | €4.516,48 | €200,07 | €0,00 |
| TEST | 1H Fast Score 6 75 Range Only V1 | 4 | €10.087,09 | €1.750,21 | €5.250,64 | €201,76 | €0,00 |
| TEST | Btc Bollinger 4H | 1 | €10.085,97 | €775,58 | €1.551,16 | €0,00 | €55,60 |
| TEST | Combo Adaptive Partial 1R V1 | 5 | €10.062,88 | €1.942,68 | €3.885,36 | €151,43 | €-1,87 |
| TEST | Doge Bollinger 1H | 1 | €10.058,84 | €1.204,04 | €3.612,13 | €0,00 | €39,96 |
| TEST | Main Dynamic Asset Selector V1 | 1 | €10.057,70 | €140,98 | €422,93 | €50,75 | €0,00 |
| TEST | Sol Ema 4H | 0 | €10.057,68 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Ema 1H | 0 | €10.057,57 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 0 | €10.048,77 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €10.045,08 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V1 | 0 | €10.043,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Balanced Short Trend Down Strict V1 | 0 | €10.035,46 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · prudente · 5x | 0 | €10.032,32 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Donchian 1H | 0 | €10.025,86 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €50 · 15x | 0 | €10.017,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 4H | 0 | €10.017,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €50 · 15x | 0 | €10.009,44 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 0 | €10.009,02 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 0 | €10.008,92 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €10 · 15x | 0 | €10.003,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 0 | €10.003,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €10 · 15x | 0 | €10.001,89 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 1H | 1 | €10.001,13 | €877,49 | €2.632,47 | €50,02 | €-0,37 |
| TEST | Scanner Bottom5 Short Continuation V1 | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €10 · 15x | 0 | €9.998,68 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €10 · 15x | 0 | €9.997,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 4H | 1 | €9.996,52 | €478,97 | €957,94 | €0,00 | €66,93 |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 0 | €9.995,23 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 No Esports Long Only V1 | 6 | €9.993,99 | €533,18 | €1.599,53 | €151,13 | €0,00 |
| TEST | Scalp RSI Long 20 · €50 · 15x | 0 | €9.993,42 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · prudente · 5x | 0 | €9.991,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €10 · 15x | 0 | €9.989,27 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €50 · 15x | 0 | €9.988,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top15 Long | 8 | €9.982,95 | €1.807,23 | €3.614,46 | €198,57 | €-0,11 |
| TEST | Scanner Top20 Long | 8 | €9.982,95 | €1.807,23 | €3.614,46 | €198,57 | €-0,11 |
| TEST | Scalp RSI Long 15 · prudente · 5x | 0 | €9.980,94 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 0 | €9.974,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Tp2 V1 | 5 | €9.968,62 | €720,81 | €2.162,44 | €149,09 | €0,00 |
| TEST | Btc Adaptive 1H | 0 | €9.968,58 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Side Regime Guard V1 | 5 | €9.967,91 | €1.319,98 | €2.639,95 | €147,39 | €3,54 |
| TEST | Btc Ema 4H | 0 | €9.966,88 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €50 · 15x | 0 | €9.946,36 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.939,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · prudente · 5x | 0 | €9.939,55 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 4H | 0 | €9.913,56 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Nohigh Cap75 V1 | 4 | €9.902,55 | €1.338,71 | €4.016,13 | €198,07 | €0,00 |
| TEST | Forza relativa 1H V2 | 7 | €9.893,74 | €925,48 | €1.850,95 | €149,79 | €-0,11 |
| TEST | Btc Donchian 1H | 1 | €9.888,28 | €1.289,36 | €3.868,07 | €49,51 | €-11,89 |
| TEST | Eth Ema 4H | 0 | €9.887,30 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Nohigh V1 | 6 | €9.862,15 | €1.217,21 | €3.651,63 | €197,24 | €0,00 |
| TEST | Eth Adaptive 1H | 0 | €9.857,66 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 1H | 1 | €9.857,56 | €1.037,93 | €3.113,80 | €49,30 | €-0,81 |
| TEST | Combo Scanner | 6 | €9.851,19 | €1.484,97 | €2.969,93 | €195,27 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 0 | €9.837,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 0 | €9.817,34 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Long Only V1 | 5 | €9.779,77 | €880,89 | €2.642,66 | €147,40 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 0 | €9.762,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Global Confluence puro 1H | 1 | €9.758,55 | €1.363,98 | €2.727,96 | €48,77 | €6,71 |
| TEST | Eth Donchian 1H | 0 | €9.747,26 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Ema 1H | 1 | €9.734,61 | €1.098,91 | €3.296,73 | €48,65 | €5,80 |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | 0 | €9.726,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 0 | €9.723,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | 4 | €9.656,13 | €1.305,40 | €3.916,19 | €193,14 | €0,00 |
| TEST | 1H Balanced Long No Rhv V1 | 5 | €9.653,19 | €1.124,13 | €3.372,38 | €193,06 | €0,00 |
| TEST | Eth Bollinger 1H | 0 | €9.649,49 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Quality7 Regime V1 | 0 | €9.603,78 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 0 | €9.579,83 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | 2 | €9.561,10 | €791,57 | €2.374,70 | €95,73 | €0,00 |
| TEST | Btc Ema 1H | 1 | €9.559,39 | €1.107,32 | €3.321,96 | €47,84 | €-6,05 |
| TEST | Bilanciata 1H V3 Filtered | 4 | €9.544,80 | €2.270,08 | €6.810,24 | €191,30 | €-42,85 |
| TEST | Combo Adaptive Regime V1 | 1 | €9.541,28 | €987,06 | €1.974,12 | €49,09 | €0,00 |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | 4 | €9.532,59 | €886,36 | €2.659,08 | €190,86 | €-15,23 |
| TEST | Scanner Top5 Btc Mfe V1 | 6 | €9.519,63 | €997,03 | €1.994,07 | €190,41 | €0,00 |
| TEST | Combo Adaptive Quality7 V1 | 4 | €9.514,37 | €1.438,51 | €2.877,02 | €190,29 | €0,00 |
| TEST | Scanner Top5 Btc Guard V1 | 5 | €9.491,50 | €1.103,75 | €2.207,51 | €189,83 | €0,00 |
| TEST | 1H Fast V3 No Esports V1 | 5 | €9.412,84 | €734,78 | €2.204,35 | €188,27 | €0,00 |
| TEST | Master Adaptive Gb20 Be V1 | 5 | €9.375,37 | €1.356,06 | €2.712,12 | €187,71 | €0,00 |
| TEST | Master Adaptive Expanded V1 | 4 | €9.370,06 | €1.563,30 | €3.126,60 | €186,75 | €0,00 |
| TEST | Master Adaptive Gb20 Partial V1 | 5 | €9.365,40 | €1.354,62 | €2.709,24 | €187,51 | €0,00 |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | 4 | €9.337,78 | €868,43 | €2.605,28 | €186,96 | €-14,99 |
| TEST | Master Adaptive V1 | 5 | €9.329,18 | €1.349,38 | €2.698,76 | €186,79 | €0,00 |
| TEST | Scanner Bottom10 Short | 4 | €9.320,74 | €1.261,36 | €2.522,73 | €140,86 | €0,00 |
| TEST | Scanner Bottom15 Short | 4 | €9.320,74 | €1.261,36 | €2.522,73 | €140,86 | €0,00 |
| TEST | Scanner Bottom20 Short | 4 | €9.320,74 | €1.261,36 | €2.522,73 | €140,86 | €0,00 |
| TEST | Scanner Top5 Btc Guard Mfe V1 | 5 | €9.270,76 | €1.078,08 | €2.156,17 | €185,42 | €0,00 |
| TEST | 1H Fast Score 6 75 V1 | 4 | €9.258,29 | €1.466,40 | €4.399,21 | €138,42 | €10,17 |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | 4 | €9.256,15 | €1.252,64 | €2.505,29 | €139,88 | €0,00 |
| TEST | Scanner Bottom5 Short Profit Lock V1 | 4 | €9.242,07 | €1.250,74 | €2.501,48 | €139,67 | €0,00 |
| TEST | Master Adaptive Runner25 V1 | 6 | €9.223,03 | €1.288,13 | €2.576,26 | €184,63 | €0,00 |
| TEST | Bilanciata 1H V2 | 5 | €9.206,59 | €955,13 | €2.865,38 | €140,57 | €-0,50 |
| TEST | Master Adaptive Gb20 V1 | 5 | €9.206,07 | €1.331,51 | €2.663,01 | €184,32 | €0,00 |
| TEST | Benchmark trend following EMA 1H | 6 | €9.176,14 | €616,44 | €1.232,88 | €96,72 | €-1,41 |
| TEST | Scanner Bottom 5 Short 1H | 4 | €9.170,95 | €1.241,11 | €2.482,23 | €138,60 | €0,00 |
| TEST | Master Adaptive Gb20 Loss Cap V1 | 6 | €9.157,30 | €1.263,51 | €2.527,01 | €183,20 | €0,00 |
| TEST | Master Adaptive No Alt V1 | 6 | €9.145,75 | €1.384,13 | €2.768,25 | €182,92 | €-0,10 |
| TEST | Combo Trend | 6 | €9.102,45 | €1.651,93 | €3.303,86 | €90,54 | €-17,36 |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | 5 | €9.102,17 | €1.091,72 | €2.183,43 | €182,04 | €0,00 |
| TEST | Combo Adaptive Mfe Trail | 7 | €9.072,43 | €804,70 | €1.609,39 | €137,16 | €-15,48 |
| TEST | 1H Balanced V3 Long Only V1 | 4 | €9.027,63 | €2.147,08 | €6.441,23 | €180,94 | €-40,53 |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | 4 | €9.012,14 | €1.427,41 | €4.282,24 | €134,74 | €9,90 |
| TEST | Bilanciata 1H V1 | 6 | €8.999,99 | €2.087,42 | €6.262,25 | €180,67 | €-8,07 |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | 2 | €8.959,01 | €1.370,15 | €2.740,30 | €91,08 | €0,00 |
| TEST | Combo Adaptive Runner25 V1 | 6 | €8.949,59 | €1.335,52 | €2.671,05 | €134,20 | €96,55 |
| TEST | 1H Fast V3 Cap75 V1 | 4 | €8.947,73 | €1.417,34 | €4.252,03 | €133,89 | €9,79 |
| TEST | Combo Mean Reversion | 4 | €8.804,50 | €5.439,63 | €10.879,27 | €131,04 | €34,43 |
| TEST | Combo Adaptive Tp3 V1 | 6 | €8.782,40 | €1.310,57 | €2.621,15 | €131,70 | €94,74 |
| TEST | Benchmark Bollinger mean reversion 1H | 2 | €8.735,32 | €2.952,41 | €5.904,81 | €43,73 | €34,05 |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | 5 | €8.728,44 | €754,09 | €1.508,19 | €131,28 | €2,68 |
| TEST | Master Adaptive Strict3 V1 | 4 | €8.704,25 | €1.184,13 | €2.368,27 | €173,50 | €0,00 |
| TEST | Scanner Top5 Btc Btc Le3 V1 | 4 | €8.612,89 | €1.990,67 | €3.981,33 | €172,29 | €0,00 |
| TEST | Forza relativa 1H V1 | 6 | €8.397,21 | €1.959,17 | €3.918,34 | €167,95 | €4,19 |

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
| PRINCIPALE | Principale 4H | Confluenza trend | €9.811,21 | €-184,95 | 56 | 56 | 41,07% | 0,87 | €-3,30 | 6,86% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €11.231,18 | €1.229,80 | 121 | 121 | 45,45% | 1,45 | €10,16 | 6,75% |
| TEST | Donchian 1H Gb20 120R V1 | Donchian breakout 20 barre | €10.966,75 | €965,41 | 89 | 89 | 43,82% | 1,53 | €10,85 | 6,75% |
| TEST | Main Side Regime Guard V1 | Confluenza trend | €10.964,56 | €987,59 | 42 | 42 | 57,14% | 2,39 | €23,51 | 3,82% |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | Momentum / breakout | €10.914,47 | €910,79 | 172 | 172 | 50,00% | 1,25 | €5,30 | 6,72% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.852,64 | €854,12 | 158 | 158 | 46,84% | 1,28 | €5,41 | 8,85% |
| TEST | Combo Trend Side Regime Guard V1 | Combo Trend | €10.788,53 | €749,20 | 133 | 133 | 51,13% | 1,29 | €5,63 | 8,10% |
| TEST | 1H Fast No Pepe V1 | Momentum / breakout | €10.575,84 | €578,07 | 258 | 258 | 44,57% | 1,13 | €2,24 | 7,89% |
| TEST | Combo Adaptive Long Only V1 | Combo Adaptive | €10.455,92 | €458,74 | 141 | 141 | 46,81% | 1,16 | €3,25 | 7,78% |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | Momentum / breakout V3 Filtered | €10.374,80 | €382,18 | 83 | 83 | 50,60% | 1,22 | €4,60 | 4,50% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €10.363,82 | €364,97 | 58 | 52 | 48,28% | 1,27 | €6,29 | 3,89% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €10.331,04 | €333,40 | 16 | 16 | 62,50% | 2,35 | €20,84 | 2,77% |
| TEST | Ampia 4H | Confluenza trend | €10.307,55 | €280,43 | 52 | 52 | 34,62% | 1,24 | €5,39 | 4,45% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | Momentum / breakout V3 Filtered | €10.300,05 | €300,05 | 33 | 33 | 48,48% | 2,04 | €9,09 | 2,01% |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | Momentum / breakout V3 Filtered | €10.282,66 | €300,29 | 95 | 95 | 46,32% | 1,16 | €3,16 | 5,24% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | Momentum / breakout V3 Filtered | €10.271,73 | €271,73 | 22 | 22 | 50,00% | 1,74 | €12,35 | 1,72% |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | Momentum / breakout V3 Filtered | €10.246,90 | €249,29 | 208 | 208 | 49,04% | 1,07 | €1,20 | 9,50% |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | Momentum / breakout V3 Filtered | €10.239,20 | €239,20 | 17 | 17 | 52,94% | 4,50 | €14,07 | 1,01% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | Momentum / breakout V3 Filtered | €10.235,18 | €235,18 | 20 | 20 | 50,00% | 1,90 | €11,76 | 2,73% |
| TEST | Combo Adaptive | Combo Adaptive | €10.226,17 | €222,72 | 180 | 180 | 44,44% | 1,07 | €1,24 | 7,91% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.209,20 | €209,20 | 6 | 6 | 83,33% | 4,66 | €34,87 | 0,85% |
| TEST | 1H Fast V3 Nohigh Range Only V1 | Momentum / breakout V3 Filtered | €10.204,53 | €207,25 | 62 | 62 | 46,77% | 1,14 | €3,34 | 4,19% |
| TEST | Scanner Top5 Btc Tp3 V1 | Scanner Top 5 + forza BTC | €10.198,94 | €196,31 | 123 | 123 | 40,65% | 1,07 | €1,60 | 11,78% |
| TEST | Scanner Top5 Btc Runner25 V1 | Scanner Top 5 + forza BTC | €10.192,97 | €190,34 | 127 | 127 | 40,94% | 1,07 | €1,50 | 12,06% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €10.191,22 | €191,22 | 9 | 9 | 55,56% | 2,16 | €21,25 | 1,01% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | Momentum / breakout V3 Filtered | €10.185,37 | €185,37 | 22 | 22 | 40,91% | 1,57 | €8,43 | 2,27% |
| TEST | Rapida 1H V3 Filtered | Momentum / breakout V3 Filtered | €10.181,06 | €183,45 | 252 | 252 | 44,05% | 1,04 | €0,73 | 9,48% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €10.159,24 | €196,46 | 6 | 6 | 50,00% | 2,73 | €32,74 | 1,18% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €10.154,80 | €156,19 | 141 | 141 | 43,97% | 1,05 | €1,11 | 11,27% |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | Momentum / breakout V3 Filtered | €10.145,12 | €145,12 | 44 | 44 | 45,45% | 1,20 | €3,30 | 2,91% |
| TEST | Sol Ema 1H | Trend following EMA | €10.121,32 | €123,38 | 18 | 18 | 44,44% | 1,25 | €6,85 | 3,33% |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | Momentum / breakout V3 Filtered | €10.099,04 | €99,04 | 55 | 55 | 54,55% | 1,12 | €1,80 | 3,59% |
| TEST | Scanner Top10 Long | Scanner Top10 Long | €10.087,45 | €90,24 | 153 | 153 | 47,06% | 1,03 | €0,59 | 10,31% |
| TEST | 1H Fast Score 6 75 Range Only V1 | Momentum / breakout | €10.087,09 | €90,14 | 47 | 47 | 42,55% | 1,07 | €1,92 | 4,60% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.085,97 | €29,45 | 2 | 2 | 50,00% | 1,54 | €14,72 | 0,91% |
| TEST | Combo Adaptive Partial 1R V1 | Combo Adaptive | €10.062,88 | €67,05 | 166 | 166 | 45,18% | 1,03 | €0,40 | 8,69% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €10.058,84 | €21,05 | 12 | 12 | 58,33% | 1,07 | €1,75 | 1,89% |
| TEST | Main Dynamic Asset Selector V1 | Confluenza trend | €10.057,70 | €58,16 | 15 | 15 | 33,33% | 1,13 | €3,88 | 3,39% |
| TEST | Sol Ema 4H | Trend following EMA | €10.057,68 | €57,68 | 10 | 10 | 40,00% | 1,22 | €5,77 | 2,27% |
| TEST | Doge Ema 1H | Trend following EMA | €10.057,57 | €57,57 | 21 | 21 | 61,90% | 1,13 | €2,74 | 2,77% |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | Momentum / breakout V3 Filtered | €10.048,77 | €48,77 | 23 | 23 | 43,48% | 1,12 | €2,12 | 3,05% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €10.045,08 | €45,08 | 28 | 28 | 46,43% | 1,40 | €1,61 | 0,33% |
| TEST | Rapida 1H V1 | Momentum / breakout | €10.043,28 | €43,28 | 78 | 78 | 34,62% | 1,02 | €0,55 | 6,76% |
| TEST | 1H Balanced Short Trend Down Strict V1 | Confluenza trend | €10.035,46 | €35,46 | 13 | 13 | 38,46% | 1,13 | €2,73 | 1,80% |
| TEST | Scalp RSI Long 20 · prudente · 5x | Inversione RSI estrema 15m | €10.032,32 | €32,32 | 11 | 11 | 54,55% | 1,85 | €2,94 | 0,36% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €10.025,86 | €25,86 | 15 | 15 | 60,00% | 1,07 | €1,72 | 3,08% |
| TEST | Scalp RSI Short 85 · €50 · 15x | Inversione RSI estrema 15m | €10.017,98 | €17,98 | 5 | 5 | 60,00% | 1,69 | €3,60 | 0,31% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €10.017,60 | €17,60 | 3 | 3 | 33,33% | 1,17 | €5,87 | 0,96% |
| TEST | Scalp RSI Short 80 · €50 · 15x | Inversione RSI estrema 15m | €10.009,44 | €9,44 | 17 | 17 | 41,18% | 1,17 | €0,56 | 0,53% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €10.009,02 | €9,02 | 28 | 28 | 46,43% | 1,40 | €0,32 | 0,07% |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | Momentum / breakout V3 Filtered | €10.008,92 | €8,92 | 30 | 30 | 36,67% | 1,02 | €0,30 | 4,84% |
| TEST | Scalp RSI Short 85 · €10 · 15x | Inversione RSI estrema 15m | €10.003,60 | €3,60 | 5 | 5 | 60,00% | 1,69 | €0,72 | 0,06% |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | Momentum / breakout V3 Filtered | €10.003,37 | €3,37 | 8 | 8 | 37,50% | 1,02 | €0,42 | 2,15% |
| TEST | Scalp RSI Short 80 · €10 · 15x | Inversione RSI estrema 15m | €10.001,89 | €1,89 | 17 | 17 | 41,18% | 1,17 | €0,11 | 0,11% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €10.001,13 | €3,16 | 20 | 20 | 45,00% | 1,01 | €0,16 | 4,59% |
| TEST | Scanner Bottom5 Short Continuation V1 | Scanner Bottom5 Short Continuation | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 20 · €10 · 15x | Inversione RSI estrema 15m | €9.998,68 | €-1,32 | 11 | 11 | 36,36% | 0,74 | €-0,12 | 0,04% |
| TEST | Scalp RSI Long 15 · €10 · 15x | Inversione RSI estrema 15m | €9.997,60 | €-2,40 | 3 | 3 | 33,33% | 0,13 | €-0,80 | 0,02% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €9.996,52 | €-69,33 | 4 | 4 | 25,00% | 0,56 | €-17,33 | 1,96% |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | Momentum / breakout V3 Filtered | €9.995,23 | €-4,77 | 15 | 15 | 46,67% | 0,99 | €-0,32 | 2,70% |
| TEST | 1H Fast V3 No Esports Long Only V1 | Momentum / breakout V3 Filtered | €9.993,99 | €-5,05 | 195 | 195 | 42,05% | 1,00 | €-0,03 | 10,60% |
| TEST | Scalp RSI Long 20 · €50 · 15x | Inversione RSI estrema 15m | €9.993,42 | €-6,58 | 11 | 11 | 36,36% | 0,74 | €-0,60 | 0,21% |
| TEST | Scalp RSI Short 85 · prudente · 5x | Inversione RSI estrema 15m | €9.991,38 | €-8,62 | 5 | 5 | 60,00% | 0,61 | €-1,72 | 0,30% |
| TEST | Scalp RSI Long 25 · €10 · 15x | Inversione RSI estrema 15m | €9.989,27 | €-10,73 | 17 | 17 | 35,29% | 0,33 | €-0,63 | 0,14% |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | €9.988,00 | €-12,00 | 3 | 3 | 33,33% | 0,13 | €-4,00 | 0,12% |
| TEST | Scanner Top15 Long | Scanner Top15 Long | €9.982,95 | €-14,66 | 152 | 152 | 46,71% | 0,99 | €-0,10 | 10,31% |
| TEST | Scanner Top20 Long | Scanner Top20 Long | €9.982,95 | €-14,66 | 152 | 152 | 46,71% | 0,99 | €-0,10 | 10,31% |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | €9.980,94 | €-19,06 | 3 | 3 | 33,33% | 0,19 | €-6,35 | 0,20% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €9.974,38 | €-25,62 | 17 | 17 | 35,29% | 0,71 | €-1,51 | 0,71% |
| TEST | 1H Fast Tp2 V1 | Momentum / breakout | €9.968,62 | €-30,00 | 247 | 247 | 38,87% | 0,99 | €-0,12 | 6,56% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €9.968,58 | €-31,42 | 9 | 9 | 44,44% | 0,86 | €-3,49 | 1,23% |
| TEST | Combo Adaptive Side Regime Guard V1 | Combo Adaptive | €9.967,91 | €-34,09 | 137 | 137 | 45,26% | 0,99 | €-0,25 | 10,02% |
| TEST | Btc Ema 4H | Trend following EMA | €9.966,88 | €-33,12 | 4 | 4 | 25,00% | 0,78 | €-8,28 | 1,76% |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | €9.946,36 | €-53,64 | 17 | 17 | 35,29% | 0,33 | €-3,16 | 0,72% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.939,62 | €-60,38 | 28 | 28 | 46,43% | 0,60 | €-2,16 | 0,84% |
| TEST | Scalp RSI Short 80 · prudente · 5x | Inversione RSI estrema 15m | €9.939,55 | €-60,45 | 17 | 17 | 35,29% | 0,39 | €-3,56 | 0,89% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €9.913,56 | €-86,44 | 5 | 5 | 20,00% | 0,61 | €-17,29 | 2,43% |
| TEST | 1H Fast Nohigh Cap75 V1 | Momentum / breakout | €9.902,55 | €-95,04 | 180 | 180 | 40,00% | 0,97 | €-0,53 | 8,83% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €9.893,74 | €-105,04 | 130 | 123 | 41,54% | 0,97 | €-0,81 | 10,88% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €9.888,28 | €-97,74 | 11 | 11 | 45,45% | 0,71 | €-8,89 | 1,82% |
| TEST | Eth Ema 4H | Trend following EMA | €9.887,30 | €-112,70 | 7 | 7 | 28,57% | 0,57 | €-16,10 | 1,83% |
| TEST | 1H Fast V3 Nohigh V1 | Momentum / breakout V3 Filtered | €9.862,15 | €-135,93 | 152 | 152 | 43,42% | 0,95 | €-0,89 | 7,10% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.857,66 | €-142,34 | 16 | 16 | 43,75% | 0,72 | €-8,90 | 3,14% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.857,56 | €-139,86 | 14 | 14 | 42,86% | 0,72 | €-9,99 | 2,91% |
| TEST | Combo Scanner | Combo Scanner | €9.851,19 | €-146,92 | 152 | 152 | 44,08% | 0,96 | €-0,97 | 11,38% |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | Momentum / breakout V3 Filtered | €9.837,38 | €-162,62 | 37 | 37 | 40,54% | 0,76 | €-4,40 | 3,08% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | Momentum / breakout V3 Filtered | €9.817,34 | €-182,66 | 24 | 24 | 41,67% | 0,64 | €-7,61 | 3,23% |
| TEST | 1H Fast V3 Long Only V1 | Momentum / breakout V3 Filtered | €9.779,77 | €-218,65 | 196 | 196 | 41,33% | 0,95 | €-1,12 | 12,52% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | Momentum / breakout V3 Filtered | €9.762,18 | €-237,82 | 7 | 7 | 14,29% | 0,02 | €-33,97 | 2,82% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.758,55 | €-246,75 | 19 | 19 | 36,84% | 0,55 | €-12,99 | 3,93% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.747,26 | €-252,74 | 16 | 16 | 31,25% | 0,58 | €-15,80 | 3,74% |
| TEST | Eth Ema 1H | Trend following EMA | €9.734,61 | €-269,38 | 23 | 23 | 39,13% | 0,66 | €-11,71 | 4,80% |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | Combo Adaptive | €9.726,12 | €-273,88 | 46 | 46 | 43,48% | 0,79 | €-5,95 | 4,21% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | Momentum / breakout V3 Filtered | €9.723,72 | €-276,28 | 31 | 31 | 32,26% | 0,62 | €-8,91 | 4,83% |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | Momentum / breakout | €9.656,13 | €-341,52 | 144 | 144 | 38,19% | 0,88 | €-2,37 | 8,83% |
| TEST | 1H Balanced Long No Rhv V1 | Confluenza trend | €9.653,19 | €-344,72 | 115 | 115 | 44,35% | 0,84 | €-3,00 | 9,26% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €9.649,49 | €-350,51 | 8 | 8 | 25,00% | 0,19 | €-43,81 | 4,16% |
| TEST | Combo Adaptive Quality7 Regime V1 | Combo Adaptive | €9.603,78 | €-396,22 | 46 | 46 | 39,13% | 0,69 | €-8,61 | 5,41% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | Momentum / breakout V3 Filtered | €9.579,83 | €-420,17 | 11 | 11 | 0,00% | 0,00 | €-38,20 | 4,20% |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | Momentum / breakout | €9.561,10 | €-437,48 | 99 | 99 | 38,38% | 0,82 | €-4,42 | 7,99% |
| TEST | Btc Ema 1H | Trend following EMA | €9.559,39 | €-432,76 | 18 | 18 | 22,22% | 0,38 | €-24,04 | 4,52% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €9.544,80 | €-408,45 | 176 | 176 | 40,34% | 0,89 | €-2,32 | 10,69% |
| TEST | Combo Adaptive Regime V1 | Combo Adaptive | €9.541,28 | €-457,54 | 77 | 77 | 45,45% | 0,76 | €-5,94 | 5,38% |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | Momentum / breakout V3 Filtered | €9.532,59 | €-450,49 | 115 | 115 | 40,87% | 0,85 | €-3,92 | 6,64% |
| TEST | Scanner Top5 Btc Mfe V1 | Scanner Top 5 + forza BTC | €9.519,63 | €-479,07 | 133 | 133 | 42,86% | 0,82 | €-3,60 | 12,28% |
| TEST | Combo Adaptive Quality7 V1 | Combo Adaptive | €9.514,37 | €-484,42 | 98 | 98 | 38,78% | 0,80 | €-4,94 | 8,88% |
| TEST | Scanner Top5 Btc Guard V1 | Scanner Top 5 + forza BTC | €9.491,50 | €-507,47 | 126 | 126 | 37,30% | 0,84 | €-4,03 | 7,34% |
| TEST | 1H Fast V3 No Esports V1 | Momentum / breakout V3 Filtered | €9.412,84 | €-585,64 | 220 | 220 | 41,82% | 0,87 | €-2,66 | 10,92% |
| TEST | Master Adaptive Gb20 Be V1 | Master Adaptive Consensus | €9.375,37 | €-623,94 | 83 | 83 | 28,92% | 0,74 | €-7,52 | 8,39% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €9.370,06 | €-629,27 | 82 | 82 | 34,15% | 0,73 | €-7,67 | 7,96% |
| TEST | Master Adaptive Gb20 Partial V1 | Master Adaptive Consensus | €9.365,40 | €-633,91 | 78 | 78 | 32,05% | 0,73 | €-8,13 | 7,98% |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | Momentum / breakout V3 Filtered | €9.337,78 | €-645,58 | 118 | 118 | 43,22% | 0,81 | €-5,47 | 8,24% |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | €9.329,18 | €-670,13 | 80 | 80 | 31,25% | 0,73 | €-8,38 | 7,80% |
| TEST | Scanner Bottom10 Short | Scanner Bottom10 Short | €9.320,74 | €-677,79 | 70 | 70 | 31,43% | 0,65 | €-9,68 | 9,06% |
| TEST | Scanner Bottom15 Short | Scanner Bottom15 Short | €9.320,74 | €-677,79 | 70 | 70 | 31,43% | 0,65 | €-9,68 | 9,06% |
| TEST | Scanner Bottom20 Short | Scanner Bottom20 Short | €9.320,74 | €-677,79 | 70 | 70 | 31,43% | 0,65 | €-9,68 | 9,06% |
| TEST | Scanner Top5 Btc Guard Mfe V1 | Scanner Top 5 + forza BTC | €9.270,76 | €-728,23 | 143 | 143 | 38,46% | 0,79 | €-5,09 | 8,78% |
| TEST | 1H Fast Score 6 75 V1 | Momentum / breakout | €9.258,29 | €-749,14 | 143 | 143 | 39,16% | 0,81 | €-5,24 | 14,70% |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | Scanner Bottom 5 Short | €9.256,15 | €-742,38 | 61 | 61 | 31,15% | 0,58 | €-12,17 | 9,08% |
| TEST | Scanner Bottom5 Short Profit Lock V1 | Scanner Bottom 5 Short | €9.242,07 | €-756,47 | 62 | 62 | 30,65% | 0,56 | €-12,20 | 9,08% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €9.223,03 | €-776,38 | 70 | 70 | 30,00% | 0,67 | €-11,09 | 8,25% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €9.206,59 | €-790,90 | 129 | 117 | 41,86% | 0,72 | €-6,13 | 11,21% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €9.206,07 | €-793,24 | 114 | 114 | 43,86% | 0,71 | €-6,96 | 9,02% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.176,14 | €-821,73 | 138 | 138 | 37,68% | 0,70 | €-5,95 | 12,31% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.170,95 | €-827,60 | 89 | 89 | 31,46% | 0,64 | €-9,30 | 10,17% |
| TEST | Master Adaptive Gb20 Loss Cap V1 | Master Adaptive Consensus | €9.157,30 | €-842,66 | 72 | 72 | 22,22% | 0,64 | €-11,70 | 11,41% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €9.145,75 | €-852,30 | 82 | 82 | 31,71% | 0,68 | €-10,39 | 9,97% |
| TEST | Combo Trend | Combo Trend | €9.102,45 | €-878,19 | 174 | 174 | 37,93% | 0,78 | €-5,05 | 11,90% |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | Scanner Top 5 + forza BTC | €9.102,17 | €-896,81 | 88 | 88 | 35,23% | 0,66 | €-10,19 | 11,79% |
| TEST | Combo Adaptive Mfe Trail | Combo Adaptive | €9.072,43 | €-911,13 | 189 | 189 | 40,74% | 0,75 | €-4,82 | 15,45% |
| TEST | 1H Balanced V3 Long Only V1 | Confluenza trend V3 Filtered | €9.027,63 | €-928,15 | 130 | 130 | 40,00% | 0,66 | €-7,14 | 10,43% |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | Momentum / breakout | €9.012,14 | €-995,10 | 101 | 101 | 39,60% | 0,69 | €-9,85 | 15,00% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €8.999,99 | €-988,63 | 127 | 127 | 35,43% | 0,65 | €-7,78 | 15,68% |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | Scanner Top 5 + forza BTC | €8.959,01 | €-1.039,15 | 41 | 41 | 19,51% | 0,28 | €-25,35 | 11,76% |
| TEST | Combo Adaptive Runner25 V1 | Combo Adaptive | €8.949,59 | €-1.145,20 | 99 | 99 | 30,30% | 0,51 | €-11,57 | 14,10% |
| TEST | 1H Fast V3 Cap75 V1 | Momentum / breakout V3 Filtered | €8.947,73 | €-1.059,41 | 146 | 146 | 34,93% | 0,72 | €-7,26 | 16,28% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €8.804,50 | €-1.223,12 | 51 | 51 | 33,33% | 0,43 | €-23,98 | 14,46% |
| TEST | Combo Adaptive Tp3 V1 | Combo Adaptive | €8.782,40 | €-1.310,62 | 80 | 80 | 28,75% | 0,36 | €-16,38 | 14,10% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €8.735,32 | €-1.295,27 | 85 | 85 | 38,82% | 0,55 | €-15,24 | 15,18% |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | Scanner Top 5 + forza BTC | €8.728,44 | €-1.273,76 | 104 | 104 | 33,65% | 0,59 | €-12,25 | 13,91% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €8.704,25 | €-1.294,33 | 71 | 71 | 25,35% | 0,56 | €-18,23 | 13,50% |
| TEST | Scanner Top5 Btc Btc Le3 V1 | Scanner Top 5 + forza BTC | €8.612,89 | €-1.384,66 | 84 | 84 | 29,76% | 0,46 | €-16,48 | 16,16% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €8.397,21 | €-1.604,88 | 109 | 109 | 27,52% | 0,48 | €-14,72 | 19,11% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | SPCX | LONG | Confluenza trend | 240m | 3,0x | 136,56189 | 136,56189 | 128,79610 | 91,72407 | 152,09346 | €285,50 | €856,50 | €48,71 | €0,00 |
| Principale 4H | VELVET | LONG | Confluenza trend | 240m | 3,0x | 0,55987 | 0,55987 | 0,49269 | 0,37605 | 0,69424 | €131,08 | €393,24 | €47,19 | €0,00 |
| Principale 4H | EDEN | LONG | Confluenza trend | 240m | 3,0x | 0,06195 | 0,06195 | 0,05451 | 0,04161 | 0,07681 | €130,34 | €391,02 | €46,92 | €0,00 |
| Principale 4H | TRUMP | LONG | Confluenza trend | 240m | 3,0x | 2,46049 | 2,46049 | 2,16523 | 1,65263 | 3,05101 | €134,98 | €404,95 | €48,59 | €0,00 |
| Principale 4H | XRP | LONG | Confluenza trend | 240m | 3,0x | 1,46057 | 1,34421 | 1,30460 | 0,98102 | 1,77252 | €8,58 | €25,73 | €2,75 | €-2,05 |
| Principale 4H | ZEC | LONG | Confluenza trend | 240m | 3,0x | 852,88054 | 835,72000 | 799,15184 | 572,85143 | 960,33794 | €11,06 | €33,19 | €2,09 | €-0,67 |
| Bilanciata 1H V1 | PEPE | SHORT | Confluenza trend | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €634,36 | €1.903,09 | €44,20 | €4,66 |
| Bilanciata 1H V1 | ARB | LONG | Confluenza trend | 60m | 3,0x | 0,10991 | 0,10991 | 0,10273 | 0,07382 | 0,12428 | €230,61 | €691,82 | €45,23 | €0,00 |
| Bilanciata 1H V1 | BTC | SHORT | Confluenza trend | 60m | 3,0x | 77204,03610 | 77443,87000 | 78315,77422 | 102552,69462 | 74980,55986 | €8,80 | €26,39 | €0,38 | €-0,08 |
| Bilanciata 1H V1 | USELESS | LONG | Confluenza trend | 60m | 3,0x | 0,11591 | 0,11096 | 0,10466 | 0,07786 | 0,13843 | €154,36 | €463,09 | €44,98 | €-19,79 |
| Bilanciata 1H V1 | ETH | SHORT | Confluenza trend | 60m | 3,0x | 2417,02650 | 2410,98000 | 2451,83168 | 3210,61686 | 2347,41613 | €1.041,05 | €3.123,14 | €44,97 | €7,81 |
| Bilanciata 1H V1 | DOGE | SHORT | Confluenza trend | 60m | 3,0x | 0,08051 | 0,08150 | 0,08185 | 0,10695 | 0,07783 | €18,24 | €54,72 | €0,91 | €-0,67 |
| 1H Balanced Long No Rhv V1 | SKHYNIX | LONG | Confluenza trend | 60m | 3,0x | 1214,11277 | 1214,11277 | 1170,18211 | 815,47908 | 1301,97411 | €413,43 | €1.240,28 | €44,88 | €0,00 |
| 1H Balanced Long No Rhv V1 | BOME | LONG | Confluenza trend | 60m | 3,0x | 0,00129 | 0,00129 | 0,00114 | 0,00087 | 0,00160 | €134,98 | €404,95 | €48,59 | €0,00 |
| 1H Balanced Long No Rhv V1 | TAO | LONG | Confluenza trend | 60m | 3,0x | 247,38947 | 247,38947 | 237,94346 | 166,16326 | 266,28148 | €428,20 | €1.284,61 | €49,05 | €0,00 |
| 1H Balanced Long No Rhv V1 | HEMI | LONG | Confluenza trend | 60m | 3,0x | 0,01177 | 0,01177 | 0,01036 | 0,00790 | 0,01459 | €131,93 | €395,78 | €47,49 | €0,00 |
| 1H Balanced Long No Rhv V1 | ARB | LONG | Confluenza trend | 60m | 3,0x | 0,11110 | 0,11110 | 0,10386 | 0,07462 | 0,12560 | €15,59 | €46,76 | €3,05 | €0,00 |
| Bilanciata 1H V2 | SKHYNIX | LONG | Confluenza trend V2 | 60m | 3,0x | 1214,11277 | 1214,11277 | 1170,18211 | 815,47908 | 1301,97411 | €422,38 | €1.267,15 | €45,85 | €0,00 |
| Bilanciata 1H V2 | XMR | LONG | Confluenza trend V2 | 60m | 3,0x | 520,62410 | 520,62410 | 498,16818 | 349,68586 | 565,53596 | €358,56 | €1.075,68 | €46,40 | €0,00 |
| Bilanciata 1H V2 | PEPE | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €9,49 | €28,46 | €0,69 | €0,34 |
| Bilanciata 1H V2 | USELESS | LONG | Confluenza trend V2 | 60m | 3,0x | 0,11116 | 0,11096 | 0,09999 | 0,07466 | 0,13351 | €152,70 | €458,10 | €46,04 | €-0,83 |
| Bilanciata 1H V2 | ENA | LONG | Confluenza trend V2 | 60m | 3,0x | 0,16057 | 0,16057 | 0,15346 | 0,10785 | 0,17479 | €12,00 | €35,99 | €1,59 | €0,00 |
| Bilanciata 1H V3 Filtered | SKHYNIX | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1220,85412 | 1220,85412 | 1177,63561 | 820,00702 | 1307,29117 | €460,42 | €1.381,27 | €48,90 | €0,00 |
| Bilanciata 1H V3 Filtered | ADA | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,20138 | 0,20138 | 0,20719 | 0,26750 | 0,18976 | €559,88 | €1.679,63 | €48,45 | €-0,00 |
| Bilanciata 1H V3 Filtered | USELESS | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,11591 | 0,11096 | 0,10466 | 0,07786 | 0,13843 | €161,07 | €483,22 | €46,93 | €-20,65 |
| Bilanciata 1H V3 Filtered | BTC | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 76920,91274 | 77443,87000 | 78028,57388 | 102176,61242 | 74705,59045 | €1.088,71 | €3.266,12 | €47,03 | €-22,21 |
| 1H Fast Score 6 75 V1 | ARB | LONG | Momentum / breakout | 60m | 3,0x | 0,10878 | 0,10878 | 0,10318 | 0,07307 | 0,11718 | €300,38 | €901,14 | €46,37 | €0,00 |
| 1H Fast Score 6 75 V1 | USELESS | LONG | Momentum / breakout | 60m | 3,0x | 0,11367 | 0,11096 | 0,10544 | 0,07635 | 0,12603 | €211,09 | €633,27 | €45,88 | €-15,11 |
| 1H Fast Score 6 75 V1 | ENA | LONG | Momentum / breakout | 60m | 3,0x | 0,16057 | 0,16057 | 0,15504 | 0,10785 | 0,16887 | €446,88 | €1.340,64 | €46,17 | €0,00 |
| 1H Fast Score 6 75 V1 | UNI | LONG | Momentum / breakout | 60m | 3,0x | 6,13623 | 6,23800 | 6,13623 | 4,12150 | 6,41501 | €508,05 | €1.524,15 | €0,00 | €25,28 |
| 1H Fast Score 6 75 No Trend Up V1 | ARB | LONG | Momentum / breakout | 60m | 3,0x | 0,10878 | 0,10878 | 0,10318 | 0,07307 | 0,11718 | €292,39 | €877,18 | €45,14 | €0,00 |
| 1H Fast Score 6 75 No Trend Up V1 | USELESS | LONG | Momentum / breakout | 60m | 3,0x | 0,11367 | 0,11096 | 0,10544 | 0,07635 | 0,12603 | €205,48 | €616,43 | €44,66 | €-14,71 |
| 1H Fast Score 6 75 No Trend Up V1 | ENA | LONG | Momentum / breakout | 60m | 3,0x | 0,16057 | 0,16057 | 0,15504 | 0,10785 | 0,16887 | €435,00 | €1.305,00 | €44,94 | €0,00 |
| 1H Fast Score 6 75 No Trend Up V1 | UNI | LONG | Momentum / breakout | 60m | 3,0x | 6,13623 | 6,23800 | 6,13623 | 4,12150 | 6,41501 | €494,54 | €1.483,63 | €0,00 | €24,61 |
| 1H Fast Score 6 75 Range Only V1 | ADA | SHORT | Momentum / breakout | 60m | 3,0x | 0,20260 | 0,20260 | 0,20707 | 0,26912 | 0,19589 | €765,21 | €2.295,64 | €50,71 | €-0,00 |
| 1H Fast Score 6 75 Range Only V1 | HEMI | LONG | Momentum / breakout | 60m | 3,0x | 0,01177 | 0,01177 | 0,01065 | 0,00790 | 0,01345 | €178,53 | €535,59 | €51,05 | €0,00 |
| 1H Fast Score 6 75 Range Only V1 | ARB | LONG | Momentum / breakout | 60m | 3,0x | 0,10878 | 0,10878 | 0,10318 | 0,07307 | 0,11718 | €326,57 | €979,72 | €50,41 | €0,00 |
| 1H Fast Score 6 75 Range Only V1 | ENA | LONG | Momentum / breakout | 60m | 3,0x | 0,16057 | 0,16057 | 0,15504 | 0,10785 | 0,16887 | €479,90 | €1.439,69 | €49,58 | €0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | BTW | LONG | Momentum / breakout | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €8,91 | €26,72 | €3,13 | €0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00086 | 0,00146 | €215,92 | €647,76 | €57,03 | €0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | NEAR | LONG | Momentum / breakout | 60m | 3,0x | 2,08142 | 2,08142 | 2,02315 | 1,39802 | 2,16882 | €42,86 | €128,59 | €3,60 | €0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €157,13 | €471,39 | €56,57 | €-0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | USELESS | LONG | Momentum / breakout | 60m | 3,0x | 0,11008 | 0,11096 | 0,10173 | 0,07394 | 0,12260 | €240,53 | €721,59 | €54,72 | €5,76 |
| 1H Fast Score 6 75 Cost Aware V1 | ENA | LONG | Momentum / breakout | 60m | 3,0x | 0,16057 | 0,16057 | 0,15504 | 0,10785 | 0,16887 | €418,42 | €1.255,26 | €43,23 | €0,00 |
| 1H Fast Nohigh Cap75 V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €139,29 | €417,86 | €50,14 | €-0,00 |
| 1H Fast Nohigh Cap75 V1 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €141,57 | €424,71 | €50,14 | €-0,00 |
| 1H Fast Nohigh Cap75 V1 | XMR | LONG | Momentum / breakout | 60m | 3,0x | 527,13541 | 527,13541 | 512,43358 | 354,05928 | 549,18814 | €585,79 | €1.757,38 | €49,01 | €0,00 |
| 1H Fast Nohigh Cap75 V1 | ENA | LONG | Momentum / breakout | 60m | 3,0x | 0,16057 | 0,16057 | 0,15504 | 0,10785 | 0,16887 | €472,06 | €1.416,18 | €48,77 | €0,00 |
| 1H Fast Long Btc 1 3 Cap75 V1 | PROM | LONG | Momentum / breakout | 60m | 3,0x | 6,93686 | 6,93686 | 6,39299 | 4,65926 | 7,75266 | €205,67 | €617,01 | €48,38 | €0,00 |
| 1H Fast Long Btc 1 3 Cap75 V1 | XMR | LONG | Momentum / breakout | 60m | 3,0x | 527,17541 | 527,17541 | 512,97206 | 354,08615 | 548,48045 | €585,90 | €1.757,69 | €47,36 | €0,00 |
| 1H Fast No Pepe V1 | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €172,22 | €516,67 | €49,86 | €0,00 |
| 1H Fast No Pepe V1 | TAO | LONG | Momentum / breakout | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €47,93 | €143,78 | €4,27 | €0,00 |
| 1H Fast No Pepe V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €136,27 | €408,80 | €49,06 | €-0,00 |
| 1H Fast No Pepe V1 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €9,48 | €28,43 | €3,41 | €-0,00 |
| 1H Fast No Pepe V1 | ADA | SHORT | Momentum / breakout | 60m | 3,0x | 0,20138 | 0,20138 | 0,20590 | 0,26750 | 0,19460 | €739,08 | €2.217,23 | €49,74 | €-0,00 |
| 1H Fast No Pepe V1 | 0G | LONG | Momentum / breakout | 60m | 3,0x | 0,23904 | 0,23904 | 0,21901 | 0,16056 | 0,26909 | €210,41 | €631,23 | €52,89 | €0,00 |
| 1H Fast No Pepe V1 | ENA | LONG | Momentum / breakout | 60m | 3,0x | 0,16057 | 0,16057 | 0,15504 | 0,10785 | 0,16887 | €22,20 | €66,59 | €2,29 | €0,00 |
| 1H Fast Tp2 V1 | BTW | LONG | Momentum / breakout | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,56752 | €142,85 | €428,56 | €50,25 | €0,00 |
| 1H Fast Tp2 V1 | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00132 | 0,00132 | 0,00119 | 0,00088 | 0,00158 | €18,87 | €56,62 | €5,59 | €0,00 |
| 1H Fast Tp2 V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,17246 | 0,17246 | 0,17246 | 0,22908 | 0,13107 | €139,71 | €419,14 | €0,00 | €-0,00 |
| 1H Fast Tp2 V1 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03379 | €141,13 | €423,40 | €50,81 | €-0,00 |
| 1H Fast Tp2 V1 | ARB | LONG | Momentum / breakout | 60m | 3,0x | 0,10991 | 0,10991 | 0,10432 | 0,07382 | 0,12109 | €278,24 | €834,72 | €42,44 | €0,00 |
| Rapida 1H V2 | ADA | SHORT | Momentum / breakout V2 | 60m | 3,0x | 0,20283 | 0,20283 | 0,20750 | 0,26943 | 0,19582 | €749,31 | €2.247,94 | €51,80 | €-0,00 |
| Rapida 1H V3 Filtered | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €172,00 | €515,99 | €49,79 | €0,00 |
| Rapida 1H V3 Filtered | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €589,98 | €1.769,95 | €52,56 | €0,00 |
| Rapida 1H V3 Filtered | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €140,02 | €420,06 | €50,41 | €-0,00 |
| Rapida 1H V3 Filtered | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €16,99 | €50,96 | €6,11 | €-0,00 |
| Rapida 1H V3 Filtered | ARB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,10991 | 0,10991 | 0,10432 | 0,07382 | 0,11829 | €293,41 | €880,24 | €44,76 | €0,00 |
| 1H Fast V3 Cap75 V1 | ARB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,10878 | 0,10878 | 0,10318 | 0,07307 | 0,11718 | €290,81 | €872,44 | €44,89 | €0,00 |
| 1H Fast V3 Cap75 V1 | USELESS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,11367 | 0,11096 | 0,10544 | 0,07635 | 0,12603 | €204,16 | €612,48 | €44,38 | €-14,62 |
| 1H Fast V3 Cap75 V1 | ENA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16057 | 0,16057 | 0,15504 | 0,10785 | 0,16887 | €431,89 | €1.295,68 | €44,62 | €0,00 |
| 1H Fast V3 Cap75 V1 | UNI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 6,13623 | 6,23800 | 6,13623 | 4,12150 | 6,41501 | €490,48 | €1.471,44 | €0,00 | €24,40 |
| 1H Fast V3 Nohigh V1 | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €131,05 | €393,14 | €47,18 | €-0,00 |
| 1H Fast V3 Nohigh V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €133,20 | €399,59 | €47,18 | €-0,00 |
| 1H Fast V3 Nohigh V1 | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,20138 | 0,20138 | 0,20590 | 0,26750 | 0,19460 | €719,57 | €2.158,72 | €48,43 | €-0,00 |
| 1H Fast V3 Nohigh V1 | 0G | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,23904 | 0,23904 | 0,21901 | 0,16056 | 0,26909 | €196,32 | €588,95 | €49,35 | €0,00 |
| 1H Fast V3 Nohigh V1 | ARB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,10991 | 0,10991 | 0,10432 | 0,07382 | 0,11829 | €26,13 | €78,40 | €3,99 | €0,00 |
| 1H Fast V3 Nohigh V1 | ENA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16057 | 0,16057 | 0,15504 | 0,10785 | 0,16887 | €10,94 | €32,83 | €1,13 | €0,00 |
| 1H Fast V3 Long Only V1 | BTW | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €126,57 | €379,72 | €44,52 | €0,00 |
| 1H Fast V3 Long Only V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00147 | €9,56 | €28,69 | €2,66 | €0,00 |
| 1H Fast V3 Long Only V1 | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €554,42 | €1.663,26 | €49,39 | €0,00 |
| 1H Fast V3 Long Only V1 | HEMI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01177 | 0,01177 | 0,01065 | 0,00790 | 0,01345 | €170,60 | €511,79 | €48,79 | €0,00 |
| 1H Fast V3 Long Only V1 | ENA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16057 | 0,16057 | 0,15504 | 0,10785 | 0,16887 | €19,73 | €59,20 | €2,04 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 V1 | HEMI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01177 | 0,01177 | 0,01065 | 0,00790 | 0,01345 | €166,97 | €500,92 | €47,75 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 V1 | PROM | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 6,92735 | 6,92735 | 6,35093 | 4,65287 | 7,79198 | €195,87 | €587,60 | €48,89 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 V1 | ARB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,10878 | 0,10878 | 0,10318 | 0,07307 | 0,11718 | €310,83 | €932,49 | €47,98 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 V1 | USELESS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,11367 | 0,11096 | 0,10544 | 0,07635 | 0,12603 | €212,69 | €638,08 | €46,23 | €-15,23 |
| 1H Fast V3 No Esports V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €169,36 | €508,09 | €49,03 | €0,00 |
| 1H Fast V3 No Esports V1 | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €27,04 | €81,13 | €2,41 | €0,00 |
| 1H Fast V3 No Esports V1 | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €133,96 | €401,88 | €48,23 | €-0,00 |
| 1H Fast V3 No Esports V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €129,73 | €389,20 | €46,70 | €-0,00 |
| 1H Fast V3 No Esports V1 | ARB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,10991 | 0,10991 | 0,10432 | 0,07382 | 0,11829 | €274,69 | €824,06 | €41,90 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | BTW | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €132,94 | €398,81 | €46,76 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00147 | €10,06 | €30,18 | €2,80 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | HEMI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01177 | 0,01177 | 0,01065 | 0,00790 | 0,01345 | €175,30 | €525,91 | €50,13 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | PROM | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 6,92735 | 6,92735 | 6,35093 | 4,65287 | 7,79198 | €9,71 | €29,12 | €2,42 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | 0G | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,23904 | 0,23904 | 0,21901 | 0,16056 | 0,26909 | €187,89 | €563,68 | €47,23 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | ENA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16057 | 0,16057 | 0,15504 | 0,10785 | 0,16887 | €17,27 | €51,82 | €1,78 | €0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €173,11 | €519,32 | €50,11 | €0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €593,79 | €1.781,38 | €52,90 | €0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €140,93 | €422,78 | €50,73 | €-0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €17,09 | €51,28 | €6,15 | €-0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | ARB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,10991 | 0,10991 | 0,10432 | 0,07382 | 0,11829 | €295,31 | €885,93 | €45,05 | €0,00 |
| 1H Fast V3 No Esports Stress Guard V1 | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,20283 | 0,20283 | 0,20750 | 0,26943 | 0,19582 | €739,04 | €2.217,11 | €51,09 | €-0,00 |
| 1H Fast V3 No Esports Stress Guard V1 | SOL | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 99,69706 | 99,78700 | 101,13696 | 132,43092 | 97,53720 | €1.183,21 | €3.549,63 | €51,27 | €-3,20 |
| 1H Fast V3 No Esports Stress Guard V1 | ENA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16057 | 0,16057 | 0,15504 | 0,10785 | 0,16887 | €502,45 | €1.507,35 | €51,91 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | HEMI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01177 | 0,01177 | 0,01065 | 0,00790 | 0,01345 | €163,25 | €489,75 | €46,69 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | PROM | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 6,92735 | 6,92735 | 6,35093 | 4,65287 | 7,79198 | €191,37 | €574,11 | €47,77 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | ARB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,10878 | 0,10878 | 0,10318 | 0,07307 | 0,11718 | €304,49 | €913,46 | €47,00 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | USELESS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,11367 | 0,11096 | 0,10544 | 0,07635 | 0,12603 | €209,32 | €627,96 | €45,50 | €-14,99 |
| Ampia 4H | SPCX | LONG | Confluenza trend | 240m | 2,0x | 136,56189 | 136,56189 | 126,46637 | 68,96375 | 164,82935 | €323,86 | €647,73 | €47,88 | €0,00 |
| Ampia 4H | VELVET | LONG | Confluenza trend | 240m | 2,0x | 0,55987 | 0,55987 | 0,49269 | 0,28274 | 0,74799 | €201,63 | €403,26 | €48,39 | €0,00 |
| Ampia 4H | LINK | LONG | Confluenza trend | 240m | 2,0x | 11,96839 | 11,96839 | 11,08055 | 6,04404 | 14,45436 | €14,07 | €28,15 | €2,09 | €0,00 |
| Ampia 4H | ETH | LONG | Confluenza trend | 240m | 2,0x | 2430,03591 | 2410,98000 | 2267,54364 | 1227,16813 | 2885,01426 | €18,82 | €37,65 | €2,52 | €-0,30 |
| Ampia 4H | HYPE | LONG | Confluenza trend | 240m | 2,0x | 79,31286 | 82,88000 | 70,73982 | 40,05299 | 103,31737 | €13,82 | €27,64 | €2,99 | €1,24 |
| Ampia 4H | TRUMP | LONG | Confluenza trend | 240m | 2,0x | 2,37347 | 2,37347 | 2,08866 | 1,19860 | 3,17096 | €210,83 | €421,66 | €50,60 | €0,00 |
| Ampia 4H | DOGE | SHORT | Confluenza trend | 240m | 2,0x | 0,08583 | 0,08150 | 0,09382 | 0,12832 | 0,06346 | €274,53 | €549,07 | €51,10 | €27,72 |
| Ampia 4H | SOL | LONG | Confluenza trend | 240m | 2,0x | 103,77875 | 99,78700 | 96,79200 | 52,40827 | 123,34165 | €13,62 | €27,23 | €1,83 | €-1,05 |
| Forza relativa 1H V1 | XMR | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 522,67451 | 522,67451 | 500,84717 | 263,95063 | 570,69467 | €505,06 | €1.010,12 | €42,18 | €0,00 |
| Forza relativa 1H V1 | PEPE | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00001 | 0,00000 | €869,59 | €1.739,17 | €40,40 | €4,26 |
| Forza relativa 1H V1 | ARB | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,10812 | 0,10812 | 0,10113 | 0,05460 | 0,12350 | €321,13 | €642,27 | €41,51 | €0,00 |
| Forza relativa 1H V1 | SOL | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 99,89102 | 99,78700 | 101,70108 | 149,33707 | 95,90889 | €13,28 | €26,56 | €0,48 | €0,03 |
| Forza relativa 1H V1 | ENA | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,16057 | 0,16057 | 0,15346 | 0,08109 | 0,17621 | €16,43 | €32,85 | €1,45 | €0,00 |
| Forza relativa 1H V1 | USELESS | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,11098 | 0,11096 | 0,10103 | 0,05605 | 0,13289 | €233,68 | €467,36 | €41,93 | €-0,09 |
| Forza relativa 1H V2 | BEAT | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,25984 | 0,25984 | 0,25657 | 0,38847 | 0,19125 | €200,38 | €400,75 | €0,00 | €-0,00 |
| Forza relativa 1H V2 | TUT | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,04452 | 0,04452 | 0,04986 | 0,06656 | 0,03277 | €204,64 | €409,28 | €49,11 | €-0,00 |
| Forza relativa 1H V2 | ADA | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,20283 | 0,20283 | 0,20884 | 0,30323 | 0,18961 | €17,52 | €35,04 | €1,04 | €-0,00 |
| Forza relativa 1H V2 | HEMI | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €200,86 | €401,72 | €48,21 | €0,00 |
| Forza relativa 1H V2 | XMR | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 520,62410 | 520,62410 | 498,16818 | 262,91517 | 570,02714 | €13,24 | €26,48 | €1,14 | €0,00 |
| Forza relativa 1H V2 | ENA | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,16057 | 0,16057 | 0,15346 | 0,08109 | 0,17621 | €16,83 | €33,66 | €1,49 | €0,00 |
| Forza relativa 1H V2 | USELESS | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,11098 | 0,11096 | 0,10103 | 0,05605 | 0,13289 | €272,01 | €544,03 | €48,80 | €-0,11 |
| Benchmark Donchian breakout 1H | SKHYNIX | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1174,33482 | 1174,33482 | 1128,44989 | 593,03908 | 1289,04713 | €641,25 | €1.282,50 | €50,11 | €0,00 |
| Benchmark Donchian breakout 1H | VELVET | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,14787 | 0,14787 | 0,16561 | 0,22107 | 0,10351 | €237,23 | €474,47 | €56,94 | €-0,00 |
| Benchmark Donchian breakout 1H | ADA | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,20283 | 0,20283 | 0,20951 | 0,30323 | 0,18614 | €72,87 | €145,74 | €4,80 | €-0,00 |
| Benchmark Donchian breakout 1H | ETH | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 2415,46681 | 2410,98000 | 2454,11428 | 3611,12288 | 2318,84814 | €1.754,61 | €3.509,21 | €56,15 | €6,52 |
| Benchmark Donchian breakout 1H | SOL | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 99,77304 | 99,78700 | 101,87931 | 149,16070 | 94,50736 | €1.329,55 | €2.659,09 | €56,14 | €-0,37 |
| Benchmark Donchian breakout 1H | XRP | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 1,33090 | 1,34421 | 1,35970 | 1,98970 | 1,25890 | €35,95 | €71,89 | €1,56 | €-0,72 |
| Donchian 1H Gb20 120R V1 | SKHYNIX | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1174,33482 | 1174,33482 | 1128,44989 | 593,03908 | 1289,04713 | €626,15 | €1.252,30 | €48,93 | €0,00 |
| Donchian 1H Gb20 120R V1 | VELVET | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,14787 | 0,14787 | 0,16561 | 0,22107 | 0,10351 | €231,65 | €463,30 | €55,60 | €-0,00 |
| Donchian 1H Gb20 120R V1 | ADA | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,20283 | 0,20283 | 0,20951 | 0,30323 | 0,18614 | €71,16 | €142,31 | €4,68 | €-0,00 |
| Donchian 1H Gb20 120R V1 | ETH | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 2415,46681 | 2410,98000 | 2454,11428 | 3611,12288 | 2318,84814 | €1.713,30 | €3.426,59 | €54,83 | €6,37 |
| Donchian 1H Gb20 120R V1 | SOL | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 99,77304 | 99,78700 | 101,87931 | 149,16070 | 94,50736 | €1.298,24 | €2.596,49 | €54,81 | €-0,36 |
| Donchian 1H Gb20 120R V1 | XRP | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 1,33090 | 1,34421 | 1,35970 | 1,98970 | 1,25890 | €35,10 | €70,20 | €1,52 | €-0,70 |
| Benchmark Bollinger mean reversion 1H | SOL | LONG | Bollinger mean reversion | 60m | 2,0x | 99,81296 | 99,78700 | 98,23262 | 50,40554 | 102,18346 | €1.381,04 | €2.762,08 | €43,73 | €-0,72 |
| Benchmark Bollinger mean reversion 1H | DOGE | LONG | Bollinger mean reversion | 60m | 2,0x | 0,08061 | 0,08150 | 0,08085 | 0,04071 | 0,08229 | €1.571,36 | €3.142,73 | €0,00 | €34,76 |
| Benchmark trend following EMA 1H | BEAT | SHORT | Trend following EMA | 60m | 2,0x | 0,28257 | 0,28257 | 0,25706 | 0,42244 | 0,20797 | €186,11 | €372,23 | €0,00 | €-0,00 |
| Benchmark trend following EMA 1H | TUT | SHORT | Trend following EMA | 60m | 2,0x | 0,04446 | 0,04446 | 0,04980 | 0,06647 | 0,03272 | €194,70 | €389,39 | €46,73 | €-0,00 |
| Benchmark trend following EMA 1H | VELVET | SHORT | Trend following EMA | 60m | 2,0x | 0,14786 | 0,14786 | 0,16560 | 0,22105 | 0,10883 | €187,91 | €375,83 | €45,10 | €-0,00 |
| Benchmark trend following EMA 1H | USELESS | LONG | Trend following EMA | 60m | 2,0x | 0,11591 | 0,11096 | 0,10340 | 0,05854 | 0,14343 | €17,31 | €34,63 | €3,74 | €-1,48 |
| Benchmark trend following EMA 1H | SOL | SHORT | Trend following EMA | 60m | 2,0x | 100,01299 | 99,78700 | 101,99785 | 149,51943 | 95,64631 | €16,08 | €32,17 | €0,64 | €0,07 |
| Benchmark trend following EMA 1H | DOGE | SHORT | Trend following EMA | 60m | 2,0x | 0,08148 | 0,08150 | 0,08296 | 0,12181 | 0,07823 | €14,32 | €28,63 | €0,52 | €-0,01 |
| Scanner Top 5 Long 1H | BOME | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00160 | €218,24 | €436,47 | €52,38 | €0,00 |
| Scanner Top 5 Long 1H | TRUMP | LONG | Scanner Top 5 Long | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,08367 | €238,89 | €477,78 | €55,13 | €0,00 |
| Scanner Top 5 Long 1H | SKHYNIX | LONG | Scanner Top 5 Long | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1331,36020 | €17,74 | €35,49 | €0,91 | €0,00 |
| Scanner Top 5 Long 1H | HEMI | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €228,24 | €456,48 | €54,78 | €0,00 |
| Scanner Top 5 Long 1H | XMR | LONG | Scanner Top 5 Long | 60m | 2,0x | 519,56389 | 519,56389 | 495,28598 | 262,37977 | 568,11972 | €14,50 | €28,99 | €1,35 | €0,00 |
| Scanner Top 5 Long 1H | ARB | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,10968 | 0,10968 | 0,10275 | 0,05539 | 0,12353 | €415,84 | €831,69 | €52,53 | €0,00 |
| Scanner Bottom 5 Short 1H | SOXL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €378,86 | €757,72 | €48,07 | €-0,00 |
| Scanner Bottom 5 Short 1H | SNDK | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €492,80 | €985,60 | €47,71 | €-0,00 |
| Scanner Bottom 5 Short 1H | VELVET | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €191,07 | €382,14 | €0,00 | €-0,00 |
| Scanner Bottom 5 Short 1H | TUT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €178,38 | €356,76 | €42,81 | €-0,00 |
| Scanner Top10 Long | TAO | LONG | Scanner Top10 Long | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €678,43 | €1.356,86 | €51,81 | €0,00 |
| Scanner Top10 Long | SKHYNIX | LONG | Scanner Top10 Long | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €972,86 | €1.945,72 | €48,38 | €0,00 |
| Scanner Top10 Long | HEMI | LONG | Scanner Top10 Long | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €207,88 | €415,77 | €49,89 | €0,00 |
| Scanner Top10 Long | XMR | LONG | Scanner Top10 Long | 60m | 2,0x | 519,56389 | 519,56389 | 495,28598 | 262,37977 | 568,11972 | €12,79 | €25,57 | €1,20 | €0,00 |
| Scanner Top10 Long | ARB | LONG | Scanner Top10 Long | 60m | 2,0x | 0,10968 | 0,10968 | 0,10275 | 0,05539 | 0,12353 | €386,28 | €772,56 | €48,79 | €0,00 |
| Scanner Bottom10 Short | SOXL | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom10 Short | SNDK | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Bottom10 Short | VELVET | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €194,19 | €388,38 | €0,00 | €-0,00 |
| Scanner Bottom10 Short | TUT | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €181,31 | €362,61 | €43,51 | €-0,00 |
| Scanner Top15 Long | NEAR | LONG | Scanner Top15 Long | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €16,79 | €33,59 | €1,21 | €0,00 |
| Scanner Top15 Long | TAO | LONG | Scanner Top15 Long | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €88,53 | €177,07 | €6,76 | €0,00 |
| Scanner Top15 Long | TRUMP | LONG | Scanner Top15 Long | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,08367 | €215,87 | €431,75 | €49,81 | €0,00 |
| Scanner Top15 Long | SKHYNIX | LONG | Scanner Top15 Long | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €787,36 | €1.574,72 | €39,16 | €0,00 |
| Scanner Top15 Long | XMR | LONG | Scanner Top15 Long | 60m | 2,0x | 522,24443 | 522,24443 | 497,48743 | 263,73344 | 571,75843 | €19,54 | €39,08 | €1,85 | €0,00 |
| Scanner Top15 Long | ARB | LONG | Scanner Top15 Long | 60m | 2,0x | 0,10968 | 0,10968 | 0,10275 | 0,05539 | 0,12353 | €379,03 | €758,05 | €47,87 | €0,00 |
| Scanner Top15 Long | ENA | LONG | Scanner Top15 Long | 60m | 2,0x | 0,15596 | 0,15596 | 0,14889 | 0,07876 | 0,17010 | €21,88 | €43,77 | €1,98 | €0,00 |
| Scanner Top15 Long | USELESS | LONG | Scanner Top15 Long | 60m | 2,0x | 0,11098 | 0,11096 | 0,10103 | 0,05605 | 0,13089 | €278,22 | €556,44 | €49,92 | €-0,11 |
| Scanner Bottom15 Short | SOXL | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom15 Short | SNDK | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Bottom15 Short | VELVET | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €194,19 | €388,38 | €0,00 | €-0,00 |
| Scanner Bottom15 Short | TUT | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €181,31 | €362,61 | €43,51 | €-0,00 |
| Scanner Top20 Long | NEAR | LONG | Scanner Top20 Long | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €16,79 | €33,59 | €1,21 | €0,00 |
| Scanner Top20 Long | TAO | LONG | Scanner Top20 Long | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €88,53 | €177,07 | €6,76 | €0,00 |
| Scanner Top20 Long | TRUMP | LONG | Scanner Top20 Long | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,08367 | €215,87 | €431,75 | €49,81 | €0,00 |
| Scanner Top20 Long | SKHYNIX | LONG | Scanner Top20 Long | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €787,36 | €1.574,72 | €39,16 | €0,00 |
| Scanner Top20 Long | XMR | LONG | Scanner Top20 Long | 60m | 2,0x | 522,24443 | 522,24443 | 497,48743 | 263,73344 | 571,75843 | €19,54 | €39,08 | €1,85 | €0,00 |
| Scanner Top20 Long | ARB | LONG | Scanner Top20 Long | 60m | 2,0x | 0,10968 | 0,10968 | 0,10275 | 0,05539 | 0,12353 | €379,03 | €758,05 | €47,87 | €0,00 |
| Scanner Top20 Long | ENA | LONG | Scanner Top20 Long | 60m | 2,0x | 0,15596 | 0,15596 | 0,14889 | 0,07876 | 0,17010 | €21,88 | €43,77 | €1,98 | €0,00 |
| Scanner Top20 Long | USELESS | LONG | Scanner Top20 Long | 60m | 2,0x | 0,11098 | 0,11096 | 0,10103 | 0,05605 | 0,13089 | €278,22 | €556,44 | €49,92 | €-0,11 |
| Scanner Bottom20 Short | SOXL | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom20 Short | SNDK | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Bottom20 Short | VELVET | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €194,19 | €388,38 | €0,00 | €-0,00 |
| Scanner Bottom20 Short | TUT | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €181,31 | €362,61 | €43,51 | €-0,00 |
| Scanner Top 5 + forza BTC 1H | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €203,45 | €406,91 | €48,83 | €0,00 |
| Scanner Top 5 + forza BTC 1H | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,14149 | €223,03 | €446,06 | €51,47 | €0,00 |
| Scanner Top 5 + forza BTC 1H | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €18,23 | €36,45 | €0,93 | €0,00 |
| Scanner Top 5 + forza BTC 1H | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €213,35 | €426,70 | €51,20 | €0,00 |
| Scanner Top 5 + forza BTC 1H | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 519,56389 | 519,56389 | 495,28598 | 262,37977 | 572,97530 | €16,38 | €32,76 | €1,53 | €0,00 |
| Scanner Top 5 + forza BTC 1H | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,10968 | 0,10968 | 0,10275 | 0,05539 | 0,12491 | €389,11 | €778,23 | €49,15 | €0,00 |
| Scanner Top5 Btc Mfe V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €190,73 | €381,46 | €45,77 | €0,00 |
| Scanner Top5 Btc Mfe V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,14149 | €209,08 | €418,16 | €48,25 | €0,00 |
| Scanner Top5 Btc Mfe V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €17,09 | €34,17 | €0,88 | €0,00 |
| Scanner Top5 Btc Mfe V1 | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €200,01 | €400,01 | €48,00 | €0,00 |
| Scanner Top5 Btc Mfe V1 | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 519,56389 | 519,56389 | 495,28598 | 262,37977 | 572,97530 | €15,36 | €30,72 | €1,44 | €0,00 |
| Scanner Top5 Btc Mfe V1 | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,10968 | 0,10968 | 0,10275 | 0,05539 | 0,12491 | €364,77 | €729,55 | €46,07 | €0,00 |
| Scanner Top5 Btc Guard V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €197,27 | €394,55 | €47,35 | €0,00 |
| Scanner Top5 Btc Guard V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,55551 | 2,55551 | 2,29388 | 1,29053 | 3,13109 | €13,03 | €26,06 | €2,67 | €0,00 |
| Scanner Top5 Btc Guard V1 | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €195,03 | €390,06 | €46,81 | €0,00 |
| Scanner Top5 Btc Guard V1 | ZORA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00942 | 0,00942 | 0,00829 | 0,00476 | 0,01191 | €192,06 | €384,12 | €46,09 | €0,00 |
| Scanner Top5 Btc Guard V1 | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 525,28504 | 525,28504 | 500,95080 | 265,26894 | 578,82035 | €506,36 | €1.012,72 | €46,92 | €0,00 |
| Scanner Top5 Btc Btc Le3 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €847,75 | €1.695,49 | €43,45 | €0,00 |
| Scanner Top5 Btc Btc Le3 V1 | 0G | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,24373 | 0,24373 | 0,21916 | 0,12308 | 0,29778 | €215,80 | €431,60 | €43,51 | €0,00 |
| Scanner Top5 Btc Btc Le3 V1 | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 524,45487 | 524,45487 | 505,31170 | 264,84971 | 566,56985 | €595,92 | €1.191,84 | €43,50 | €0,00 |
| Scanner Top5 Btc Btc Le3 V1 | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,10968 | 0,10968 | 0,10275 | 0,05539 | 0,12491 | €331,20 | €662,40 | €41,83 | €0,00 |
| Scanner Top5 Btc Btc 2 3 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €891,28 | €1.782,56 | €45,68 | €0,00 |
| Scanner Top5 Btc Btc 2 3 V1 | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 522,24443 | 522,24443 | 497,48743 | 263,73344 | 576,70983 | €478,87 | €957,73 | €45,40 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €192,69 | €385,37 | €46,24 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,55551 | 2,55551 | 2,29388 | 1,29053 | 3,13109 | €12,72 | €25,45 | €2,61 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €190,49 | €380,99 | €45,72 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | ZORA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00942 | 0,00942 | 0,00829 | 0,00476 | 0,01191 | €187,59 | €375,19 | €45,02 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 525,28504 | 525,28504 | 500,95080 | 265,26894 | 578,82035 | €494,59 | €989,17 | €45,82 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,55551 | 2,55551 | 2,29388 | 1,29053 | 3,13109 | €12,70 | €25,40 | €2,60 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €191,20 | €382,39 | €45,89 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | PROM | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 7,01991 | 7,01991 | 6,30832 | 3,54505 | 8,58541 | €213,89 | €427,78 | €43,36 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | ZORA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00942 | 0,00942 | 0,00829 | 0,00476 | 0,01191 | €188,34 | €376,68 | €45,20 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 525,28504 | 525,28504 | 500,95080 | 265,26894 | 578,82035 | €485,59 | €971,18 | €44,99 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | ZORA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00942 | 0,00942 | 0,00829 | 0,00476 | 0,01191 | €185,37 | €370,74 | €44,49 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,10968 | 0,10968 | 0,10275 | 0,05539 | 0,12491 | €325,70 | €651,40 | €41,14 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 525,90516 | 525,90516 | 508,26113 | 265,58211 | 564,72203 | €17,51 | €35,02 | €1,17 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | USELESS | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,11026 | 0,11096 | 0,09902 | 0,05568 | 0,13500 | €212,03 | €424,06 | €43,25 | €2,68 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | ENA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15596 | 0,15596 | 0,14889 | 0,07876 | 0,17152 | €13,48 | €26,97 | €1,22 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00176 | €210,95 | €421,90 | €50,63 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1363,81560 | €965,52 | €1.931,04 | €49,49 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01601 | €209,51 | €419,03 | €50,28 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,11110 | 0,11110 | 0,10386 | 0,05611 | 0,13284 | €390,51 | €781,02 | €50,94 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | UNI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 5,69614 | 6,23800 | 6,03348 | 2,87655 | 6,44709 | €25,63 | €51,25 | €0,00 | €4,88 |
| Scanner Top5 Btc Tp3 V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00176 | €211,07 | €422,14 | €50,66 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1363,81560 | €966,09 | €1.932,17 | €49,52 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01601 | €209,64 | €419,27 | €50,31 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,11110 | 0,11110 | 0,10386 | 0,05611 | 0,13284 | €390,74 | €781,47 | €50,97 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | UNI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 5,69614 | 6,23800 | 6,03348 | 2,87655 | 6,44709 | €25,64 | €51,28 | €0,00 | €4,88 |
| Global Confluence puro 1H | DOGE | SHORT | Global Confluence puro | 60m | 2,0x | 0,08170 | 0,08150 | 0,08316 | 0,12214 | 0,07805 | €1.363,98 | €2.727,96 | €48,77 | €6,71 |
| Combo Trend | BEAT | SHORT | Combo Trend | 60m | 2,0x | 0,25984 | 0,25984 | 0,25657 | 0,38847 | 0,19125 | €193,71 | €387,42 | €0,00 | €-0,00 |
| Combo Trend | ADA | SHORT | Combo Trend | 60m | 2,0x | 0,19986 | 0,19986 | 0,20356 | 0,29879 | 0,19173 | €1.205,82 | €2.411,64 | €44,61 | €-0,00 |
| Combo Trend | ETH | SHORT | Combo Trend | 60m | 2,0x | 2415,22686 | 2410,98000 | 2454,83114 | 3610,76415 | 2328,09740 | €14,37 | €28,74 | €0,47 | €0,05 |
| Combo Trend | USELESS | LONG | Combo Trend | 60m | 2,0x | 0,11591 | 0,11096 | 0,10340 | 0,05854 | 0,14343 | €204,72 | €409,44 | €44,18 | €-17,50 |
| Combo Trend | SOL | SHORT | Combo Trend | 60m | 2,0x | 100,01299 | 99,78700 | 101,99785 | 149,51943 | 95,64631 | €20,08 | €40,16 | €0,80 | €0,09 |
| Combo Trend | DOGE | SHORT | Combo Trend | 60m | 2,0x | 0,08148 | 0,08150 | 0,08296 | 0,12181 | 0,07823 | €13,24 | €26,47 | €0,48 | €-0,01 |
| Combo Mean Reversion | ADA | LONG | Combo Mean Reversion | 60m | 2,0x | 0,20284 | 0,20284 | 0,19804 | 0,10244 | 0,21052 | €942,00 | €1.883,99 | €44,59 | €0,00 |
| Combo Mean Reversion | SOL | LONG | Combo Mean Reversion | 60m | 2,0x | 99,81296 | 99,78700 | 98,23262 | 50,40554 | 102,34150 | €1.393,28 | €2.786,55 | €44,12 | €-0,72 |
| Combo Mean Reversion | BTC | LONG | Combo Mean Reversion | 60m | 2,0x | 77237,45440 | 77443,87000 | 76310,60495 | 39004,91447 | 78720,41353 | €1.763,77 | €3.527,53 | €42,33 | €9,43 |
| Combo Mean Reversion | XRP | LONG | Combo Mean Reversion | 60m | 2,0x | 1,33144 | 1,34421 | 1,33864 | 0,67238 | 1,36601 | €1.340,59 | €2.681,19 | €0,00 | €25,72 |
| Combo Scanner | BOME | LONG | Combo Scanner | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €195,20 | €390,40 | €46,85 | €0,00 |
| Combo Scanner | TRUMP | LONG | Combo Scanner | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,14149 | €213,98 | €427,96 | €49,38 | €0,00 |
| Combo Scanner | SKHYNIX | LONG | Combo Scanner | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €24,78 | €49,55 | €1,27 | €0,00 |
| Combo Scanner | XMR | LONG | Combo Scanner | 60m | 2,0x | 527,13541 | 527,13541 | 508,23306 | 266,20338 | 568,72055 | €660,18 | €1.320,37 | €47,35 | €0,00 |
| Combo Scanner | ARB | LONG | Combo Scanner | 60m | 2,0x | 0,11110 | 0,11110 | 0,10386 | 0,05611 | 0,12705 | €377,46 | €754,92 | €49,24 | €0,00 |
| Combo Scanner | ENA | LONG | Combo Scanner | 60m | 2,0x | 0,16057 | 0,16057 | 0,15346 | 0,08109 | 0,17621 | €13,38 | €26,75 | €1,18 | €0,00 |
| Combo Adaptive | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,01735 | 121,01735 | 128,90956 | 180,92093 | 105,23292 | €367,30 | €734,61 | €47,91 | €-0,00 |
| Combo Adaptive | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €40,89 | €81,77 | €3,12 | €0,00 |
| Combo Adaptive | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,52450 | 2,33981 | 1,27487 | 2,89389 | €18,69 | €37,37 | €2,73 | €0,00 |
| Combo Adaptive | 0G | LONG | Combo Adaptive | 60m | 2,0x | 0,23904 | 0,23904 | 0,21329 | 0,12072 | 0,29055 | €230,13 | €460,26 | €49,58 | €0,00 |
| Combo Adaptive | SOL | SHORT | Combo Adaptive | 60m | 2,0x | 99,77304 | 99,78700 | 101,66869 | 149,16070 | 95,98175 | €14,76 | €29,52 | €0,56 | €-0,00 |
| Combo Adaptive | USELESS | LONG | Combo Adaptive | 60m | 2,0x | 0,11008 | 0,11096 | 0,09935 | 0,05559 | 0,13155 | €260,60 | €521,20 | €50,82 | €4,16 |
| Combo Adaptive | UNI | LONG | Combo Adaptive | 60m | 2,0x | 6,13623 | 6,23800 | 5,89727 | 3,09879 | 6,61413 | €13,14 | €26,28 | €1,02 | €0,44 |
| Combo Adaptive Mfe Trail | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €54,29 | €108,58 | €4,15 | €0,00 |
| Combo Adaptive Mfe Trail | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,52450 | 2,33981 | 1,27487 | 2,89389 | €315,75 | €631,50 | €46,20 | €0,00 |
| Combo Adaptive Mfe Trail | TUT | SHORT | Combo Adaptive | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €190,04 | €380,09 | €45,61 | €-0,00 |
| Combo Adaptive Mfe Trail | PROM | LONG | Combo Adaptive | 60m | 2,0x | 7,01991 | 7,01991 | 6,30832 | 3,54505 | 8,44309 | €21,72 | €43,45 | €4,40 | €0,00 |
| Combo Adaptive Mfe Trail | USELESS | LONG | Combo Adaptive | 60m | 2,0x | 0,11591 | 0,11096 | 0,10466 | 0,05854 | 0,13843 | €182,25 | €364,50 | €35,40 | €-15,58 |
| Combo Adaptive Mfe Trail | SOL | SHORT | Combo Adaptive | 60m | 2,0x | 100,01299 | 99,78700 | 101,79936 | 149,51943 | 96,44025 | €23,91 | €47,81 | €0,85 | €0,11 |
| Combo Adaptive Mfe Trail | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,08148 | 0,08150 | 0,08281 | 0,12181 | 0,07882 | €16,73 | €33,46 | €0,55 | €-0,01 |
| Combo Adaptive Quality7 V1 | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €371,68 | €743,36 | €47,16 | €-0,00 |
| Combo Adaptive Quality7 V1 | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €646,78 | €1.293,57 | €49,39 | €0,00 |
| Combo Adaptive Quality7 V1 | ZORA | LONG | Combo Adaptive | 60m | 2,0x | 0,00942 | 0,00942 | 0,00829 | 0,00476 | 0,01169 | €199,23 | €398,46 | €47,81 | €0,00 |
| Combo Adaptive Quality7 V1 | 0G | LONG | Combo Adaptive | 60m | 2,0x | 0,24605 | 0,24605 | 0,22046 | 0,12425 | 0,29722 | €220,81 | €441,63 | €45,92 | €0,00 |
| Combo Adaptive Regime V1 | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €987,06 | €1.974,12 | €49,09 | €0,00 |
| Combo Adaptive Long Only V1 | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €645,48 | €1.290,95 | €46,47 | €0,00 |
| Combo Adaptive Long Only V1 | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,52450 | 2,33981 | 1,27487 | 2,89389 | €48,12 | €96,24 | €7,04 | €0,00 |
| Combo Adaptive Long Only V1 | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1331,36020 | €968,99 | €1.937,97 | €49,66 | €0,00 |
| Combo Adaptive Long Only V1 | HEMI | LONG | Combo Adaptive | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €216,09 | €432,18 | €51,86 | €0,00 |
| Combo Adaptive Long Only V1 | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,11110 | 0,11110 | 0,10386 | 0,05611 | 0,12560 | €400,65 | €801,31 | €52,27 | €0,00 |
| Combo Adaptive Partial 1R V1 | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,01735 | 121,01735 | 128,90956 | 180,92093 | 105,23292 | €352,70 | €705,40 | €46,00 | €-0,00 |
| Combo Adaptive Partial 1R V1 | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,52450 | 2,33981 | 1,27487 | 2,89389 | €347,19 | €694,38 | €50,80 | €0,00 |
| Combo Adaptive Partial 1R V1 | VELVET | SHORT | Combo Adaptive | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €207,76 | €415,52 | €0,00 | €-0,00 |
| Combo Adaptive Partial 1R V1 | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €1.013,20 | €2.026,40 | €50,39 | €0,00 |
| Combo Adaptive Partial 1R V1 | USELESS | LONG | Combo Adaptive | 60m | 2,0x | 0,11591 | 0,11096 | 0,10466 | 0,05854 | 0,13843 | €21,83 | €43,65 | €4,24 | €-1,87 |
| Combo Adaptive Runner25 V1 | 0G | LONG | Combo Adaptive | 60m | 2,0x | 0,23904 | 0,23904 | 0,21329 | 0,12072 | 0,31630 | €204,19 | €408,39 | €43,99 | €0,00 |
| Combo Adaptive Runner25 V1 | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,10968 | 0,10968 | 0,10275 | 0,05539 | 0,13046 | €350,40 | €700,80 | €44,26 | €0,00 |
| Combo Adaptive Runner25 V1 | UNI | LONG | Combo Adaptive | 60m | 2,0x | 5,69614 | 6,23800 | 6,04873 | 2,87655 | 6,44709 | €505,26 | €1.010,52 | €0,00 | €96,13 |
| Combo Adaptive Runner25 V1 | SOL | SHORT | Combo Adaptive | 60m | 2,0x | 99,61607 | 99,78700 | 101,40716 | 148,92603 | 94,24282 | €20,98 | €41,95 | €0,75 | €-0,07 |
| Combo Adaptive Runner25 V1 | PEPE | SHORT | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00001 | 0,00000 | €14,42 | €28,84 | €0,64 | €-0,24 |
| Combo Adaptive Runner25 V1 | USELESS | LONG | Combo Adaptive | 60m | 2,0x | 0,11079 | 0,11096 | 0,10052 | 0,05595 | 0,14161 | €240,28 | €480,55 | €44,56 | €0,73 |
| Combo Adaptive Tp3 V1 | 0G | LONG | Combo Adaptive | 60m | 2,0x | 0,23904 | 0,23904 | 0,21329 | 0,12072 | 0,31630 | €200,38 | €400,76 | €43,17 | €0,00 |
| Combo Adaptive Tp3 V1 | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,10968 | 0,10968 | 0,10275 | 0,05539 | 0,13046 | €343,85 | €687,70 | €43,43 | €0,00 |
| Combo Adaptive Tp3 V1 | UNI | LONG | Combo Adaptive | 60m | 2,0x | 5,69614 | 6,23800 | 6,04873 | 2,87655 | 6,44709 | €495,82 | €991,64 | €0,00 | €94,33 |
| Combo Adaptive Tp3 V1 | SOL | SHORT | Combo Adaptive | 60m | 2,0x | 99,61607 | 99,78700 | 101,40716 | 148,92603 | 94,24282 | €20,58 | €41,17 | €0,74 | €-0,07 |
| Combo Adaptive Tp3 V1 | PEPE | SHORT | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00001 | 0,00000 | €14,15 | €28,30 | €0,63 | €-0,23 |
| Combo Adaptive Tp3 V1 | USELESS | LONG | Combo Adaptive | 60m | 2,0x | 0,11079 | 0,11096 | 0,10052 | 0,05595 | 0,14161 | €235,79 | €471,58 | €43,73 | €0,71 |
| Btc Ema 1H | BTC | SHORT | Trend following EMA | 60m | 3,0x | 77303,06629 | 77443,87000 | 78416,23045 | 102684,23973 | 75076,73798 | €1.107,32 | €3.321,96 | €47,84 | €-6,05 |
| Btc Donchian 1H | BTC | SHORT | Donchian breakout 20 barre | 60m | 3,0x | 77206,56560 | 77443,87000 | 78194,80964 | 102556,05464 | 75230,07752 | €1.289,36 | €3.868,07 | €49,51 | €-11,89 |
| Btc Bollinger 4H | BTC | SHORT | Bollinger mean reversion | 240m | 2,0x | 80323,10217 | 77443,87000 | 78401,16314 | 120083,03774 | 75648,94663 | €775,58 | €1.551,16 | €0,00 | €55,60 |
| Sol Ema 1H | SOL | SHORT | Trend following EMA | 60m | 3,0x | 99,77304 | 99,78700 | 101,66869 | 132,53186 | 95,98175 | €888,04 | €2.664,11 | €50,62 | €-0,37 |
| Sol Donchian 1H | SOL | SHORT | Donchian breakout 20 barre | 60m | 3,0x | 99,77304 | 99,78700 | 101,45806 | 132,53186 | 96,40301 | €1.019,77 | €3.059,30 | €51,67 | €-0,43 |
| Sol Donchian 4H | SOL | LONG | Donchian breakout 20 barre | 240m | 2,0x | 104,08581 | 99,78700 | 98,18471 | 52,56334 | 120,60890 | €449,62 | €899,24 | €50,98 | €-37,14 |
| Sol Bollinger 1H | SOL | LONG | Bollinger mean reversion | 60m | 3,0x | 99,81296 | 99,78700 | 98,23262 | 67,04104 | 102,18346 | €1.037,93 | €3.113,80 | €49,30 | €-0,81 |
| Sol Bollinger 4H | SOL | SHORT | Bollinger mean reversion | 240m | 2,0x | 107,28254 | 99,78700 | 102,35930 | 160,38740 | 97,27311 | €478,97 | €957,94 | €0,00 | €66,93 |
| Sol Adaptive 1H | SOL | SHORT | Combo Adaptive | 60m | 3,0x | 99,77304 | 99,78700 | 101,66869 | 132,53186 | 95,98175 | €877,49 | €2.632,47 | €50,02 | €-0,37 |
| Eth Ema 1H | ETH | SHORT | Trend following EMA | 60m | 3,0x | 2415,22686 | 2410,98000 | 2450,87073 | 3208,22634 | 2343,93912 | €1.098,91 | €3.296,73 | €48,65 | €5,80 |
| Doge Bollinger 1H | DOGE | LONG | Bollinger mean reversion | 60m | 3,0x | 0,08061 | 0,08150 | 0,08077 | 0,05414 | 0,08229 | €1.204,04 | €3.612,13 | €0,00 | €39,96 |
| Master Adaptive V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99403 | 639,55695 | 1331,36019 | €22,75 | €45,50 | €1,17 | €0,00 |
| Master Adaptive V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €195,57 | €391,15 | €46,94 | €0,00 |
| Master Adaptive V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,20498 | 0,11491 | 0,27267 | €236,54 | €473,08 | €46,91 | €0,00 |
| Master Adaptive V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 520,62410 | 520,62410 | 498,16818 | 262,91517 | 565,53595 | €529,71 | €1.059,43 | €45,70 | €0,00 |
| Master Adaptive V1 | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,10968 | 0,10968 | 0,10275 | 0,05539 | 0,12353 | €364,80 | €729,60 | €46,08 | €0,00 |
| Master Adaptive No Alt V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1255,10261 | 1255,10261 | 1225,12158 | 633,82682 | 1315,06467 | €19,09 | €38,19 | €0,91 | €0,00 |
| Master Adaptive No Alt V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €183,81 | €367,62 | €44,11 | €0,00 |
| Master Adaptive No Alt V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 514,40286 | 514,40286 | 493,14790 | 259,77344 | 556,91277 | €554,63 | €1.109,27 | €45,83 | €0,00 |
| Master Adaptive No Alt V1 | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,10968 | 0,10968 | 0,10275 | 0,05539 | 0,12353 | €359,36 | €718,72 | €45,39 | €0,00 |
| Master Adaptive No Alt V1 | ENA | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,16077 | 0,16077 | 0,15357 | 0,08119 | 0,17517 | €14,18 | €28,36 | €1,27 | €0,00 |
| Master Adaptive No Alt V1 | USELESS | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,11098 | 0,11096 | 0,10103 | 0,05605 | 0,13089 | €253,05 | €506,09 | €45,40 | €-0,10 |
| Master Adaptive Strict3 V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €178,16 | €356,31 | €42,76 | €0,00 |
| Master Adaptive Strict3 V1 | PROM | LONG | Master Adaptive Consensus | 60m | 2,0x | 7,01991 | 7,01991 | 6,30832 | 3,54505 | 8,44309 | €215,49 | €430,99 | €43,69 | €0,00 |
| Master Adaptive Strict3 V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,24076 | 0,24076 | 0,21579 | 0,12159 | 0,29071 | €209,83 | €419,66 | €43,53 | €0,00 |
| Master Adaptive Strict3 V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 524,22482 | 524,22482 | 504,57786 | 264,73354 | 563,51875 | €580,65 | €1.161,30 | €43,52 | €0,00 |
| Master Adaptive Expanded V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03814 | 0,02188 | 0,05374 | €197,50 | €395,01 | €47,40 | €0,00 |
| Master Adaptive Expanded V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1261,89668 | 1261,89668 | 1231,08309 | 637,25783 | 1323,52387 | €934,21 | €1.868,43 | €45,62 | €0,00 |
| Master Adaptive Expanded V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01194 | 0,01194 | 0,01050 | 0,00603 | 0,01480 | €195,34 | €390,67 | €46,88 | €0,00 |
| Master Adaptive Expanded V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,20498 | 0,11491 | 0,27267 | €236,25 | €472,49 | €46,85 | €0,00 |
| Master Adaptive Gb20 V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99403 | 639,55695 | 1331,36019 | €22,45 | €44,90 | €1,15 | €0,00 |
| Master Adaptive Gb20 V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €193,03 | €386,06 | €46,33 | €0,00 |
| Master Adaptive Gb20 V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,20498 | 0,11491 | 0,27267 | €233,42 | €466,83 | €46,29 | €0,00 |
| Master Adaptive Gb20 V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 520,62410 | 520,62410 | 498,16818 | 262,91517 | 565,53595 | €522,62 | €1.045,25 | €45,08 | €0,00 |
| Master Adaptive Gb20 V1 | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,10968 | 0,10968 | 0,10275 | 0,05539 | 0,12353 | €359,99 | €719,98 | €45,47 | €0,00 |
| Master Adaptive Runner25 V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03814 | 0,02188 | 0,05894 | €34,77 | €69,54 | €8,34 | €0,00 |
| Master Adaptive Runner25 V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1255,10261 | 1255,10261 | 1225,12158 | 633,82682 | 1345,04570 | €27,05 | €54,10 | €1,29 | €0,00 |
| Master Adaptive Runner25 V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01601 | €185,86 | €371,72 | €44,61 | €0,00 |
| Master Adaptive Runner25 V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,20498 | 0,11491 | 0,29523 | €233,84 | €467,69 | €46,37 | €0,00 |
| Master Adaptive Runner25 V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 520,62410 | 520,62410 | 498,16818 | 262,91517 | 587,99187 | €446,15 | €892,30 | €38,49 | €0,00 |
| Master Adaptive Runner25 V1 | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,10968 | 0,10968 | 0,10275 | 0,05539 | 0,13046 | €360,46 | €720,91 | €45,53 | €0,00 |
| Combo Adaptive Side Regime Guard V1 | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €77,52 | €155,04 | €5,58 | €0,00 |
| Combo Adaptive Side Regime Guard V1 | VELVET | SHORT | Combo Adaptive | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €216,61 | €433,23 | €0,00 | €-0,00 |
| Combo Adaptive Side Regime Guard V1 | TUT | SHORT | Combo Adaptive | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €192,40 | €384,79 | €46,18 | €-0,00 |
| Combo Adaptive Side Regime Guard V1 | USELESS | LONG | Combo Adaptive | 60m | 2,0x | 0,11008 | 0,11096 | 0,09935 | 0,05559 | 0,13155 | €237,09 | €474,18 | €46,23 | €3,78 |
| Combo Adaptive Side Regime Guard V1 | UNI | LONG | Combo Adaptive | 60m | 2,0x | 6,23925 | 6,23800 | 5,98083 | 3,15082 | 6,75608 | €596,36 | €1.192,72 | €49,40 | €-0,24 |
| Master Adaptive Gb20 Be V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99403 | 639,55695 | 1331,36019 | €22,86 | €45,73 | €1,17 | €0,00 |
| Master Adaptive Gb20 Be V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €196,54 | €393,08 | €47,17 | €0,00 |
| Master Adaptive Gb20 Be V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,20498 | 0,11491 | 0,27267 | €237,71 | €475,42 | €47,14 | €0,00 |
| Master Adaptive Gb20 Be V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 520,62410 | 520,62410 | 498,16818 | 262,91517 | 565,53595 | €532,34 | €1.064,67 | €45,92 | €0,00 |
| Master Adaptive Gb20 Be V1 | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,10968 | 0,10968 | 0,10275 | 0,05539 | 0,12353 | €366,61 | €733,22 | €46,31 | €0,00 |
| Master Adaptive Gb20 Partial V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99403 | 639,55695 | 1331,36019 | €22,84 | €45,68 | €1,17 | €0,00 |
| Master Adaptive Gb20 Partial V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €196,33 | €392,67 | €47,12 | €0,00 |
| Master Adaptive Gb20 Partial V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,20498 | 0,11491 | 0,27267 | €237,46 | €474,91 | €47,09 | €0,00 |
| Master Adaptive Gb20 Partial V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 520,62410 | 520,62410 | 498,16818 | 262,91517 | 565,53595 | €531,77 | €1.063,54 | €45,87 | €0,00 |
| Master Adaptive Gb20 Partial V1 | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,10968 | 0,10968 | 0,10275 | 0,05539 | 0,12353 | €366,22 | €732,44 | €46,26 | €0,00 |
| Master Adaptive Gb20 Loss Cap V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03828 | 0,02188 | 0,05682 | €195,70 | €391,41 | €45,67 | €0,00 |
| Master Adaptive Gb20 Loss Cap V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01069 | 0,00594 | 0,01465 | €210,34 | €420,68 | €38,67 | €0,00 |
| Master Adaptive Gb20 Loss Cap V1 | PROM | LONG | Master Adaptive Consensus | 60m | 2,0x | 7,01991 | 7,01991 | 6,48622 | 3,54505 | 8,44309 | €34,75 | €69,51 | €5,28 | €0,00 |
| Master Adaptive Gb20 Loss Cap V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,21062 | 0,11491 | 0,27267 | €309,65 | €619,30 | €46,05 | €0,00 |
| Master Adaptive Gb20 Loss Cap V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 514,40286 | 514,40286 | 498,46164 | 259,77344 | 556,91277 | €32,91 | €65,81 | €2,04 | €0,00 |
| Master Adaptive Gb20 Loss Cap V1 | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,10968 | 0,10968 | 0,10448 | 0,05539 | 0,12353 | €480,15 | €960,31 | €45,49 | €0,00 |
| 1H Fast V3 Nohigh Range Only V1 | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,20283 | 0,20283 | 0,20750 | 0,26943 | 0,19582 | €740,69 | €2.222,07 | €51,20 | €-0,00 |
| 1H Fast V3 Nohigh Range Only V1 | ARB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,10878 | 0,10878 | 0,10318 | 0,07307 | 0,11718 | €330,06 | €990,17 | €50,95 | €0,00 |
| 1H Fast V3 Nohigh Range Only V1 | ENA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16057 | 0,16057 | 0,15504 | 0,10785 | 0,16887 | €493,88 | €1.481,64 | €51,02 | €0,00 |
| 1H Fast V3 Nohigh Regime Guard V1 | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €140,84 | €422,53 | €50,70 | €-0,00 |
| 1H Fast V3 Nohigh Regime Guard V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €143,15 | €429,46 | €50,70 | €-0,00 |
| 1H Fast V3 Nohigh Regime Guard V1 | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,20283 | 0,20283 | 0,20750 | 0,26943 | 0,19582 | €34,57 | €103,71 | €2,39 | €-0,00 |
| 1H Fast V3 Nohigh Regime Guard V1 | ARB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,10991 | 0,10991 | 0,10432 | 0,07382 | 0,11829 | €333,52 | €1.000,56 | €50,87 | €0,00 |
| 1H Fast V3 Nohigh Regime Guard V1 | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 77206,56560 | 77443,87000 | 78071,27913 | 102556,05464 | 75909,49530 | €1.508,59 | €4.525,78 | €50,69 | €-13,91 |
| Main Side Regime Guard V1 | VELVET | LONG | Confluenza trend | 240m | 3,0x | 0,55987 | 0,55987 | 0,49269 | 0,37605 | 0,69424 | €142,25 | €426,74 | €51,21 | €0,00 |
| Main Side Regime Guard V1 | AKE | LONG | Confluenza trend | 240m | 3,0x | 0,01021 | 0,01021 | 0,00899 | 0,00686 | 0,01266 | €145,97 | €437,90 | €52,55 | €0,00 |
| Main Side Regime Guard V1 | XRP | LONG | Confluenza trend | 240m | 3,0x | 1,47102 | 1,34421 | 1,31178 | 0,98804 | 1,78951 | €12,77 | €38,31 | €4,15 | €-3,30 |
| Main Side Regime Guard V1 | ETH | LONG | Confluenza trend | 240m | 3,0x | 2437,91749 | 2410,98000 | 2326,72117 | 1637,46791 | 2660,31012 | €9,94 | €29,83 | €1,36 | €-0,33 |
| Main Side Regime Guard V1 | ENA | LONG | Confluenza trend | 240m | 3,0x | 0,16108 | 0,16108 | 0,14175 | 0,10819 | 0,19974 | €150,44 | €451,33 | €54,16 | €0,00 |
| Main Side Regime Guard V1 | ZEC | LONG | Confluenza trend | 240m | 3,0x | 852,88054 | 835,72000 | 799,15184 | 572,85143 | 960,33794 | €290,60 | €871,79 | €54,92 | €-17,54 |
| Main Dynamic Asset Selector V1 | ENA | LONG | Confluenza trend | 240m | 3,0x | 0,16108 | 0,16108 | 0,14175 | 0,10819 | 0,19974 | €140,98 | €422,93 | €50,75 | €0,00 |
| Combo Trend Side Regime Guard V1 | VELVET | SHORT | Combo Trend | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,12693 | €217,86 | €435,73 | €0,00 | €-0,00 |
| Combo Trend Side Regime Guard V1 | TUT | SHORT | Combo Trend | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03364 | €12,81 | €25,62 | €3,07 | €-0,00 |
| Combo Trend Side Regime Guard V1 | SUI | SHORT | Combo Trend | 60m | 2,0x | 0,71926 | 0,72140 | 0,73823 | 1,07529 | 0,67752 | €1.029,16 | €2.058,32 | €54,29 | €-6,14 |
| Combo Trend Side Regime Guard V1 | DOGE | SHORT | Combo Trend | 60m | 2,0x | 0,08277 | 0,08150 | 0,08184 | 0,12375 | 0,07926 | €1.329,20 | €2.658,40 | €0,00 | €40,90 |
| Combo Trend Side Regime Guard V1 | UNI | LONG | Combo Trend | 60m | 2,0x | 5,77916 | 6,23800 | 6,03540 | 2,91847 | 6,35335 | €12,69 | €25,39 | €0,00 | €2,02 |
| Combo Trend Side Regime Guard V1 | USELESS | LONG | Combo Trend | 60m | 2,0x | 0,11008 | 0,11096 | 0,09816 | 0,05559 | 0,13632 | €249,64 | €499,29 | €54,09 | €3,98 |
| 1H Fast Nohigh Cap75 Short Only V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €135,82 | €407,46 | €48,90 | €-0,00 |
| 1H Fast Nohigh Cap75 Short Only V1 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €138,05 | €414,14 | €48,89 | €-0,00 |
| 1H Fast Nohigh Cap75 Short Only V1 | XMR | LONG | Momentum / breakout | 60m | 3,0x | 527,13541 | 527,13541 | 512,43358 | 354,05928 | 549,18814 | €571,22 | €1.713,65 | €47,79 | €0,00 |
| 1H Fast Nohigh Cap75 Short Only V1 | ENA | LONG | Momentum / breakout | 60m | 3,0x | 0,16057 | 0,16057 | 0,15504 | 0,10785 | 0,16887 | €460,31 | €1.380,94 | €47,56 | €0,00 |
| 1H Balanced V3 Long Only V1 | SKHYNIX | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1220,85412 | 1220,85412 | 1177,63561 | 820,00702 | 1307,29117 | €435,49 | €1.306,46 | €46,25 | €0,00 |
| 1H Balanced V3 Long Only V1 | ADA | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,20138 | 0,20138 | 0,20719 | 0,26750 | 0,18976 | €529,53 | €1.588,58 | €45,82 | €-0,00 |
| 1H Balanced V3 Long Only V1 | USELESS | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,11591 | 0,11096 | 0,10466 | 0,07786 | 0,13843 | €152,34 | €457,03 | €44,39 | €-19,53 |
| 1H Balanced V3 Long Only V1 | BTC | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 76920,91274 | 77443,87000 | 78028,57388 | 102176,61242 | 74705,59045 | €1.029,72 | €3.089,16 | €44,48 | €-21,00 |
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
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | UNI | LONG | 2026-09-02T04:45:00+00:00 | 6,22173 | €90,39 | 2,16 | TARGET |
| Forza relativa 1H V2 | UNI | LONG | 2026-09-02T04:45:00+00:00 | 6,27314 | €104,19 | 2,16 | TARGET |
| Forza relativa 1H V1 | UNI | LONG | 2026-09-02T04:45:00+00:00 | 6,22173 | €89,83 | 2,16 | TARGET |
| Benchmark trend following EMA 1H | UNI | LONG | 2026-09-02T04:45:00+00:00 | 6,32649 | €89,82 | 2,16 | TARGET |
| Combo Trend | UNI | LONG | 2026-09-02T04:45:00+00:00 | 6,32649 | €95,94 | 2,16 | TARGET |
| Combo Scanner | UNI | LONG | 2026-09-02T04:45:00+00:00 | 6,24559 | €3,77 | 2,16 | TARGET |
| Combo Adaptive Mfe Trail | UNI | LONG | 2026-09-02T04:45:00+00:00 | 6,22949 | €86,11 | 1,96 | TARGET |
| 1H Fast V3 Nohigh Range Only V1 | UNI | LONG | 2026-09-02T04:45:00+00:00 | 6,25777 | €1,43 | 1,45 | TARGET |
| Rapida 1H V2 | UNI | LONG | 2026-09-02T04:45:00+00:00 | 6,25777 | €74,22 | 1,45 | TARGET |
| Bilanciata 1H V2 | BTR | SHORT | 2026-09-02T04:45:00+00:00 | 0,09089 | €-0,21 | -0,00 | STOP_STRESS_SLIPPAGE |
| Scanner Top20 Long | UNI | LONG | 2026-09-02T04:15:00+00:00 | 6,19554 | €97,13 | 1,96 | TARGET |
| Scanner Top15 Long | UNI | LONG | 2026-09-02T04:15:00+00:00 | 6,19554 | €97,13 | 1,96 | TARGET |

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

Generato: 2026-09-02 05:32 UTC


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

Segnali totali salvati: **162**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-09-02 | BTC | 77.662,37 | +8 | +3 | +3 | 0 | +3 | +1 | 0 | ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA |
| 2026-09-02 | DOGE | 0.08189 | -1 | -2 | -2 | 0 | +2 | 0 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-09-02 | SOL | 100,25 | +7 | +3 | +3 | 0 | +3 | +1 | 0 | HOLD / ACCUMULO A TRANCHE, NO LEVA AGGRESSIVA |
| 2026-09-01 | BTC | 79.026,52 | +7 | +3 | +3 | 0 | +3 | +1 | 0 | ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA |
| 2026-09-01 | DOGE | 0.08350 | -1 | -2 | -2 | 0 | +2 | 0 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-09-01 | SOL | 104,07 | +7 | +3 | +3 | 0 | +3 | +1 | 0 | HOLD / ACCUMULO A TRANCHE, NO LEVA AGGRESSIVA |
| 2026-08-31 | BTC | 78.005,28 | +7 | +3 | +3 | 0 | +3 | +1 | 0 | ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA |
| 2026-08-31 | DOGE | 0.08279 | 0 | -1 | -1 | 0 | +2 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-08-31 | SOL | 102,56 | +6 | +3 | +3 | 0 | +3 | +1 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-08-30 | BTC | 78.145,28 | +7 | +3 | +3 | 0 | +3 | +1 | 0 | ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA |
| 2026-08-30 | DOGE | 0.08501 | +1 | -1 | -1 | 0 | +2 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-08-30 | SOL | 105,04 | +7 | +3 | +3 | 0 | +3 | +1 | 0 | HOLD / ACCUMULO A TRANCHE, NO LEVA AGGRESSIVA |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 54 | 53 | 52 | 51 | 49 | 47 | 44 | 40 | 34 | 26 | 11 | 0 |
| SOL | 54 | 53 | 52 | 51 | 49 | 47 | 44 | 40 | 34 | 26 | 11 | 0 |
| DOGE | 54 | 53 | 52 | 51 | 49 | 47 | 44 | 40 | 34 | 26 | 11 | 0 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-07-20 | 45g | 2026-09-03 | domani |
| SOL | 2026-07-20 | 45g | 2026-09-03 | domani |
| DOGE | 2026-07-20 | 45g | 2026-09-03 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 50 | 52,00% | +0,43% | +0,41% | PRIMA CALIBRAZIONE |
| BTC | 2g | 49 | 53,06% | +0,79% | +0,69% | PRIMA CALIBRAZIONE |
| BTC | 3g | 48 | 47,92% | +1,00% | +0,85% | PRIMA CALIBRAZIONE |
| BTC | 5g | 46 | 43,48% | +2,01% | +1,73% | PRIMA CALIBRAZIONE |
| BTC | 7g | 44 | 52,27% | +2,88% | +2,63% | PRIMA CALIBRAZIONE |
| BTC | 10g | 41 | 56,10% | +4,18% | +3,96% | PRIMA CALIBRAZIONE |
| BTC | 14g | 37 | 62,16% | +6,06% | +5,96% | PRIMA CALIBRAZIONE |
| BTC | 21g | 32 | 56,25% | +8,12% | +7,91% | PRIMA CALIBRAZIONE |
| BTC | 30g | 24 | 87,50% | +11,24% | +9,45% | FEEDBACK RAPIDO |
| BTC | 45g | 10 | 80,00% | +22,88% | +13,96% | FEEDBACK RAPIDO |
| BTC | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 1g | 46 | 56,52% | +0,66% | +0,53% | PRIMA CALIBRAZIONE |
| SOL | 2g | 45 | 51,11% | +1,42% | +1,27% | PRIMA CALIBRAZIONE |
| SOL | 3g | 44 | 59,09% | +2,28% | +2,08% | PRIMA CALIBRAZIONE |
| SOL | 5g | 42 | 64,29% | +3,99% | +3,86% | PRIMA CALIBRAZIONE |
| SOL | 7g | 40 | 70,00% | +5,68% | +5,81% | PRIMA CALIBRAZIONE |
| SOL | 10g | 37 | 70,27% | +7,71% | +7,92% | PRIMA CALIBRAZIONE |
| SOL | 14g | 33 | 75,76% | +10,42% | +11,52% | PRIMA CALIBRAZIONE |
| SOL | 21g | 27 | 70,37% | +12,82% | +11,51% | FEEDBACK RAPIDO |
| SOL | 30g | 20 | 50,00% | +13,83% | +3,94% | FEEDBACK RAPIDO |
| SOL | 45g | 10 | 30,00% | +33,14% | -16,16% | FEEDBACK RAPIDO |
| SOL | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 1g | 49 | 46,94% | +0,38% | +0,38% | PRIMA CALIBRAZIONE |
| DOGE | 2g | 48 | 50,00% | +0,79% | +0,84% | PRIMA CALIBRAZIONE |
| DOGE | 3g | 48 | 45,83% | +1,12% | +1,42% | PRIMA CALIBRAZIONE |
| DOGE | 5g | 46 | 54,35% | +2,07% | +2,75% | PRIMA CALIBRAZIONE |
| DOGE | 7g | 45 | 60,00% | +2,74% | +3,72% | PRIMA CALIBRAZIONE |
| DOGE | 10g | 42 | 61,90% | +3,41% | +4,89% | PRIMA CALIBRAZIONE |
| DOGE | 14g | 38 | 71,05% | +5,79% | +8,23% | PRIMA CALIBRAZIONE |
| DOGE | 21g | 32 | 75,00% | +6,66% | +5,42% | PRIMA CALIBRAZIONE |
| DOGE | 30g | 25 | 68,00% | +9,07% | +0,14% | FEEDBACK RAPIDO |
| DOGE | 45g | 11 | 0,00% | +18,98% | -18,98% | FEEDBACK RAPIDO |
| DOGE | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 50 | 52,00% | +0,43% | +0,41% | -0,03% | +0,99% | PRIMA CALIBRAZIONE |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 53 | 54,72% | +0,40% | +0,40% | -0,05% | +0,95% | PRIMA CALIBRAZIONE |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 53 | 54,72% | +0,40% | +0,40% | -0,05% | +0,95% | PRIMA CALIBRAZIONE |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,25% | +0,25% | -0,10% | +0,70% | PRIMA CALIBRAZIONE |
| BTC | 1g | Tecnico | CALIBRABILE | 48 | 39,58% | +0,55% | +0,12% | +0,07% | +1,09% | PRIMA CALIBRAZIONE |
| BTC | 1g | Classic technical | CALIBRABILE | 21 | 38,10% | +0,80% | +0,30% | +0,07% | +1,33% | FEEDBACK RAPIDO |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +0,27% | +0,27% | -0,26% | +0,74% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 49 | 53,06% | +0,79% | +0,69% | +0,19% | +1,47% | PRIMA CALIBRAZIONE |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 52 | 55,77% | +0,89% | +0,89% | +0,30% | +1,56% | PRIMA CALIBRAZIONE |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 52 | 55,77% | +0,89% | +0,89% | +0,30% | +1,56% | PRIMA CALIBRAZIONE |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,52% | +0,52% | -0,02% | +1,18% | PRIMA CALIBRAZIONE |
| BTC | 2g | Tecnico | CALIBRABILE | 47 | 44,68% | +1,10% | +0,22% | +0,50% | +1,77% | PRIMA CALIBRAZIONE |
| BTC | 2g | Classic technical | CALIBRABILE | 20 | 40,00% | +1,23% | +0,47% | +0,63% | +1,88% | FEEDBACK RAPIDO |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +2,14% | +2,14% | +1,22% | +2,65% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 48 | 47,92% | +1,00% | +0,85% | -0,90% | +2,65% | PRIMA CALIBRAZIONE |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 51 | 56,86% | +1,32% | +1,32% | -0,89% | +2,90% | PRIMA CALIBRAZIONE |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 51 | 56,86% | +1,32% | +1,32% | -0,89% | +2,90% | PRIMA CALIBRAZIONE |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 35 | 57,14% | +0,91% | +0,91% | -1,00% | +2,36% | PRIMA CALIBRAZIONE |
| BTC | 3g | Tecnico | CALIBRABILE | 46 | 36,96% | +1,68% | -0,15% | -0,68% | +3,22% | PRIMA CALIBRAZIONE |
| BTC | 3g | Classic technical | CALIBRABILE | 19 | 36,84% | +1,96% | -0,06% | -0,39% | +3,39% | FEEDBACK RAPIDO |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +1,42% | +1,42% | -0,64% | +3,18% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 46 | 43,48% | +2,01% | +1,73% | -1,48% | +4,20% | PRIMA CALIBRAZIONE |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 49 | 51,02% | +2,28% | +2,28% | -1,45% | +4,53% | PRIMA CALIBRAZIONE |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 49 | 51,02% | +2,28% | +2,28% | -1,45% | +4,53% | PRIMA CALIBRAZIONE |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 35 | 48,57% | +2,08% | +2,08% | -1,57% | +4,07% | PRIMA CALIBRAZIONE |
| BTC | 5g | Tecnico | CALIBRABILE | 44 | 40,91% | +2,66% | -1,19% | -1,23% | +4,97% | PRIMA CALIBRAZIONE |
| BTC | 5g | Classic technical | CALIBRABILE | 17 | 41,18% | +4,72% | -2,12% | -0,74% | +6,82% | FEEDBACK RAPIDO |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 33,33% | +0,36% | +0,36% | -1,24% | +3,59% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 44 | 52,27% | +2,88% | +2,63% | -1,65% | +5,51% | PRIMA CALIBRAZIONE |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 47 | 59,57% | +3,22% | +3,22% | -1,63% | +5,83% | PRIMA CALIBRAZIONE |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 47 | 59,57% | +3,22% | +3,22% | -1,63% | +5,83% | PRIMA CALIBRAZIONE |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 35 | 60,00% | +3,17% | +3,17% | -1,80% | +5,49% | PRIMA CALIBRAZIONE |
| BTC | 7g | Tecnico | CALIBRABILE | 42 | 38,10% | +3,87% | -2,20% | -1,38% | +6,39% | PRIMA CALIBRAZIONE |
| BTC | 7g | Classic technical | CALIBRABILE | 15 | 33,33% | +7,45% | -4,83% | -0,59% | +10,35% | FEEDBACK RAPIDO |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +0,68% | +0,68% | -1,68% | +3,81% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 41 | 56,10% | +4,18% | +3,96% | -1,81% | +6,89% | PRIMA CALIBRAZIONE |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 44 | 61,36% | +4,34% | +4,34% | -1,82% | +7,15% | PRIMA CALIBRAZIONE |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 44 | 61,36% | +4,34% | +4,34% | -1,82% | +7,15% | PRIMA CALIBRAZIONE |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 35 | 62,86% | +4,42% | +4,42% | -2,02% | +6,89% | PRIMA CALIBRAZIONE |
| BTC | 10g | Tecnico | CALIBRABILE | 39 | 38,46% | +5,05% | -1,77% | -1,52% | +7,91% | PRIMA CALIBRAZIONE |
| BTC | 10g | Classic technical | CALIBRABILE | 12 | 33,33% | +10,50% | -7,08% | -0,15% | +13,38% | FEEDBACK RAPIDO |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 50,00% | +0,69% | +0,69% | -0,88% | +5,44% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 37 | 62,16% | +6,06% | +5,96% | -2,31% | +9,37% | PRIMA CALIBRAZIONE |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 40 | 62,50% | +6,11% | +6,11% | -2,31% | +9,47% | PRIMA CALIBRAZIONE |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 40 | 62,50% | +6,11% | +6,11% | -2,31% | +9,47% | PRIMA CALIBRAZIONE |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 35 | 68,57% | +6,60% | +6,60% | -2,13% | +9,78% | PRIMA CALIBRAZIONE |
| BTC | 14g | Tecnico | CALIBRABILE | 35 | 57,14% | +7,16% | +0,24% | -2,00% | +10,58% | PRIMA CALIBRAZIONE |
| BTC | 14g | Classic technical | CALIBRABILE | 8 | 25,00% | +12,28% | -12,28% | -0,83% | +16,12% | FEEDBACK RAPIDO |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -2,25% | -2,25% | -3,05% | +4,24% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 32 | 56,25% | +8,12% | +7,91% | -2,96% | +11,77% | PRIMA CALIBRAZIONE |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 34 | 64,71% | +7,57% | +7,57% | -3,00% | +11,24% | PRIMA CALIBRAZIONE |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 34 | 64,71% | +7,57% | +7,57% | -3,00% | +11,24% | PRIMA CALIBRAZIONE |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 30 | 70,00% | +8,77% | +8,77% | -2,80% | +12,42% | PRIMA CALIBRAZIONE |
| BTC | 21g | Tecnico | CALIBRABILE | 29 | 37,93% | +8,61% | +1,92% | -2,74% | +12,34% | FEEDBACK RAPIDO |
| BTC | 21g | Classic technical | CALIBRABILE | 4 | 0,00% | +11,68% | -11,68% | -1,55% | +14,27% | FEEDBACK RAPIDO |
| BTC | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,21% | +1,21% | -3,06% | +4,24% | FEEDBACK RAPIDO |
| BTC | 30g | Global confluence | BENCHMARK | 24 | 87,50% | +11,24% | +9,45% | -2,93% | +15,13% | FEEDBACK RAPIDO |
| BTC | 30g | Famiglia statistica | CALIBRABILE | 26 | 80,77% | +11,00% | +11,00% | -2,98% | +14,99% | FEEDBACK RAPIDO |
| BTC | 30g | Scanner grezzo | DIAGNOSTICO | 26 | 80,77% | +11,00% | +11,00% | -2,98% | +14,99% | FEEDBACK RAPIDO |
| BTC | 30g | Market regime grezzo | DIAGNOSTICO | 22 | 81,82% | +12,14% | +12,14% | -2,71% | +16,43% | FEEDBACK RAPIDO |
| BTC | 30g | Tecnico | CALIBRABILE | 21 | 28,57% | +10,59% | -8,42% | -2,63% | +15,03% | FEEDBACK RAPIDO |
| BTC | 30g | Classic technical | CALIBRABILE | 4 | 0,00% | +24,06% | -24,06% | -1,55% | +28,48% | FEEDBACK RAPIDO |
| BTC | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +0,16% | +0,16% | -3,06% | +4,24% | FEEDBACK RAPIDO |
| BTC | 45g | Global confluence | BENCHMARK | 10 | 80,00% | +22,88% | +13,96% | -2,63% | +26,74% | FEEDBACK RAPIDO |
| BTC | 45g | Famiglia statistica | CALIBRABILE | 11 | 100,00% | +22,96% | +22,96% | -2,62% | +26,80% | FEEDBACK RAPIDO |
| BTC | 45g | Scanner grezzo | DIAGNOSTICO | 11 | 100,00% | +22,96% | +22,96% | -2,62% | +26,80% | FEEDBACK RAPIDO |
| BTC | 45g | Market regime grezzo | DIAGNOSTICO | 10 | 100,00% | +23,26% | +23,26% | -2,50% | +26,92% | FEEDBACK RAPIDO |
| BTC | 45g | Tecnico | CALIBRABILE | 10 | 40,00% | +23,20% | -5,30% | -2,56% | +27,04% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 49 | 46,94% | +0,38% | +0,38% | -0,25% | +1,40% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 52 | 59,62% | +0,25% | +0,68% | -0,39% | +1,20% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 52 | 59,62% | +0,25% | +0,68% | -0,39% | +1,20% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,15% | +0,26% | -0,32% | +0,87% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Tecnico | CALIBRABILE | 46 | 52,17% | +0,14% | +0,32% | -0,52% | +1,07% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Classic technical | CALIBRABILE | 31 | 41,94% | +0,27% | -0,51% | -0,38% | +0,97% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 62,50% | +2,48% | +2,09% | +0,94% | +3,13% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 48 | 50,00% | +0,79% | +0,84% | +0,03% | +2,10% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 51 | 56,86% | +0,56% | +1,13% | -0,19% | +1,76% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 51 | 56,86% | +0,56% | +1,13% | -0,19% | +1,76% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 38 | 50,00% | +0,36% | +0,74% | -0,26% | +1,41% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Tecnico | CALIBRABILE | 45 | 55,56% | +0,09% | +0,50% | -0,64% | +1,27% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Classic technical | CALIBRABILE | 31 | 45,16% | +0,67% | -1,20% | -0,10% | +1,65% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 50,00% | +3,38% | +3,05% | +2,44% | +5,44% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 48 | 45,83% | +1,12% | +1,42% | -1,61% | +4,03% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 50 | 56,00% | +0,92% | +1,67% | -1,78% | +3,65% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 50 | 56,00% | +0,92% | +1,67% | -1,78% | +3,65% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,84% | +1,55% | -1,48% | +3,36% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Tecnico | CALIBRABILE | 44 | 43,18% | -0,08% | +0,30% | -2,11% | +2,52% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Classic technical | CALIBRABILE | 31 | 32,26% | +1,30% | -2,13% | -1,89% | +4,20% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 50,00% | +2,90% | +2,64% | -0,79% | +6,76% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 46 | 54,35% | +2,07% | +2,75% | -2,42% | +6,44% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 48 | 54,17% | +1,85% | +2,79% | -2,52% | +6,07% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 48 | 54,17% | +1,85% | +2,79% | -2,52% | +6,07% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +2,45% | +3,08% | -2,17% | +5,74% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Tecnico | CALIBRABILE | 42 | 54,76% | +0,56% | +0,25% | -3,05% | +4,79% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Classic technical | CALIBRABILE | 31 | 38,71% | +2,48% | -3,99% | -2,71% | +6,71% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 42,86% | +2,23% | +2,00% | -1,09% | +8,98% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 45 | 60,00% | +2,74% | +3,72% | -2,85% | +8,36% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 46 | 58,70% | +2,70% | +3,63% | -2,83% | +8,13% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 46 | 58,70% | +2,70% | +3,63% | -2,83% | +8,13% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,59% | +4,60% | -2,54% | +8,00% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Tecnico | CALIBRABILE | 40 | 57,50% | +1,06% | +1,09% | -3,46% | +6,40% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Classic technical | CALIBRABILE | 31 | 38,71% | +2,76% | -4,80% | -3,30% | +8,15% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 42,86% | +0,39% | +0,24% | -1,74% | +8,98% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 42 | 61,90% | +3,41% | +4,89% | -2,93% | +10,34% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 44 | 61,36% | +3,17% | +4,61% | -3,00% | +9,92% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 44 | 61,36% | +3,17% | +4,61% | -3,00% | +9,92% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,79% | +5,36% | -2,91% | +9,59% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Tecnico | CALIBRABILE | 37 | 64,86% | +0,95% | +1,99% | -3,59% | +7,32% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Classic technical | CALIBRABILE | 29 | 44,83% | +2,95% | -4,12% | -3,35% | +9,95% | FEEDBACK RAPIDO |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 6 | 66,67% | +1,71% | +1,21% | -1,24% | +10,26% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 38 | 71,05% | +5,79% | +8,23% | -3,29% | +13,88% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 40 | 75,00% | +5,39% | +7,73% | -3,35% | +13,24% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 40 | 75,00% | +5,39% | +7,73% | -3,35% | +13,24% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 38 | 76,32% | +5,76% | +8,06% | -3,33% | +13,70% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Tecnico | CALIBRABILE | 33 | 66,67% | +1,58% | +1,05% | -4,09% | +8,18% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Classic technical | CALIBRABILE | 27 | 51,85% | +4,09% | -4,09% | -3,41% | +12,32% | FEEDBACK RAPIDO |
| DOGE | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 75,00% | +12,47% | +2,65% | -1,31% | +16,91% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 32 | 75,00% | +6,66% | +5,42% | -4,30% | +15,73% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 34 | 85,29% | +6,86% | +10,34% | -4,31% | +16,06% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 34 | 85,29% | +6,86% | +10,34% | -4,31% | +16,06% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 32 | 87,50% | +7,37% | +10,91% | -4,34% | +16,79% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Tecnico | CALIBRABILE | 30 | 63,33% | +5,01% | -5,01% | -4,70% | +12,46% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Classic technical | CALIBRABILE | 22 | 68,18% | +2,23% | -2,23% | -4,78% | +9,45% | FEEDBACK RAPIDO |
| DOGE | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 75,00% | +12,49% | -0,95% | -1,31% | +25,23% | FEEDBACK RAPIDO |
| DOGE | 30g | Global confluence | BENCHMARK | 25 | 68,00% | +9,07% | +0,14% | -5,18% | +20,02% | FEEDBACK RAPIDO |
| DOGE | 30g | Famiglia statistica | CALIBRABILE | 26 | 84,62% | +9,45% | +7,69% | -5,24% | +20,68% | FEEDBACK RAPIDO |
| DOGE | 30g | Scanner grezzo | DIAGNOSTICO | 26 | 84,62% | +9,45% | +7,69% | -5,24% | +20,68% | FEEDBACK RAPIDO |
| DOGE | 30g | Market regime grezzo | DIAGNOSTICO | 24 | 91,67% | +7,91% | +10,66% | -5,36% | +19,30% | FEEDBACK RAPIDO |
| DOGE | 30g | Tecnico | CALIBRABILE | 26 | 46,15% | +9,45% | -9,45% | -5,24% | +20,68% | FEEDBACK RAPIDO |
| DOGE | 30g | Classic technical | CALIBRABILE | 20 | 55,00% | +7,30% | -7,30% | -5,27% | +16,83% | FEEDBACK RAPIDO |
| DOGE | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +31,53% | +31,53% | -1,85% | +40,20% | FEEDBACK RAPIDO |
| DOGE | 45g | Global confluence | BENCHMARK | 11 | 0,00% | +18,98% | -18,98% | -6,73% | +36,47% | FEEDBACK RAPIDO |
| DOGE | 45g | Famiglia statistica | CALIBRABILE | 11 | 0,00% | +18,98% | -18,98% | -6,73% | +36,47% | FEEDBACK RAPIDO |
| DOGE | 45g | Scanner grezzo | DIAGNOSTICO | 11 | 0,00% | +18,98% | -18,98% | -6,73% | +36,47% | FEEDBACK RAPIDO |
| DOGE | 45g | Market regime grezzo | DIAGNOSTICO | 11 | 0,00% | +18,98% | -18,98% | -6,73% | +36,47% | FEEDBACK RAPIDO |
| DOGE | 45g | Tecnico | CALIBRABILE | 11 | 0,00% | +18,98% | -18,98% | -6,73% | +36,47% | FEEDBACK RAPIDO |
| DOGE | 45g | Classic technical | CALIBRABILE | 10 | 0,00% | +19,37% | -19,37% | -6,60% | +36,59% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 46 | 56,52% | +0,66% | +0,53% | -0,02% | +1,59% | PRIMA CALIBRAZIONE |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 48 | 58,33% | +0,33% | +0,32% | -0,28% | +1,23% | PRIMA CALIBRAZIONE |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 51 | 56,86% | +0,38% | +0,23% | -0,24% | +1,27% | PRIMA CALIBRAZIONE |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +0,27% | +0,39% | -0,30% | +0,87% | PRIMA CALIBRAZIONE |
| SOL | 1g | Tecnico | CALIBRABILE | 50 | 52,00% | +0,33% | +0,31% | -0,32% | +1,19% | PRIMA CALIBRAZIONE |
| SOL | 1g | Classic technical | CALIBRABILE | 34 | 52,94% | +0,55% | +0,50% | -0,24% | +1,51% | PRIMA CALIBRAZIONE |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 45 | 51,11% | +1,42% | +1,27% | +0,49% | +2,52% | PRIMA CALIBRAZIONE |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 47 | 46,81% | +0,99% | +0,47% | +0,05% | +1,80% | PRIMA CALIBRAZIONE |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 50 | 46,00% | +0,95% | +0,42% | +0,04% | +1,85% | PRIMA CALIBRAZIONE |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +0,76% | +0,78% | -0,00% | +1,60% | PRIMA CALIBRAZIONE |
| SOL | 2g | Tecnico | CALIBRABILE | 49 | 42,86% | +0,87% | +0,25% | +0,01% | +1,97% | PRIMA CALIBRAZIONE |
| SOL | 2g | Classic technical | CALIBRABILE | 33 | 51,52% | +1,02% | +0,99% | +0,13% | +2,00% | PRIMA CALIBRAZIONE |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 44 | 59,09% | +2,28% | +2,08% | -1,17% | +4,53% | PRIMA CALIBRAZIONE |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 46 | 50,00% | +1,70% | +1,06% | -1,52% | +3,95% | PRIMA CALIBRAZIONE |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 49 | 48,98% | +1,62% | +0,98% | -1,50% | +3,91% | PRIMA CALIBRAZIONE |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +1,43% | +1,38% | -1,48% | +3,53% | PRIMA CALIBRAZIONE |
| SOL | 3g | Tecnico | CALIBRABILE | 48 | 50,00% | +1,45% | +0,09% | -1,58% | +3,62% | PRIMA CALIBRAZIONE |
| SOL | 3g | Classic technical | CALIBRABILE | 32 | 56,25% | +1,43% | +1,26% | -1,49% | +3,61% | PRIMA CALIBRAZIONE |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 42 | 64,29% | +3,99% | +3,86% | -1,65% | +7,39% | PRIMA CALIBRAZIONE |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 44 | 56,82% | +3,18% | +1,94% | -2,02% | +6,57% | PRIMA CALIBRAZIONE |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 47 | 55,32% | +3,02% | +1,77% | -2,02% | +6,40% | PRIMA CALIBRAZIONE |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +2,66% | +2,88% | -2,09% | +5,82% | PRIMA CALIBRAZIONE |
| SOL | 5g | Tecnico | CALIBRABILE | 46 | 50,00% | +3,03% | -0,44% | -2,20% | +6,28% | PRIMA CALIBRAZIONE |
| SOL | 5g | Classic technical | CALIBRABILE | 30 | 63,33% | +2,35% | +2,16% | -2,00% | +5,51% | PRIMA CALIBRAZIONE |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 40 | 70,00% | +5,68% | +5,81% | -1,90% | +9,57% | PRIMA CALIBRAZIONE |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 42 | 64,29% | +4,71% | +3,20% | -2,30% | +8,65% | PRIMA CALIBRAZIONE |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 45 | 64,44% | +4,39% | +2,99% | -2,33% | +8,34% | PRIMA CALIBRAZIONE |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 34 | 61,76% | +4,35% | +4,41% | -2,45% | +7,76% | PRIMA CALIBRAZIONE |
| SOL | 7g | Tecnico | CALIBRABILE | 44 | 43,18% | +4,35% | -1,35% | -2,51% | +8,28% | PRIMA CALIBRAZIONE |
| SOL | 7g | Classic technical | CALIBRABILE | 28 | 57,14% | +2,69% | +2,76% | -2,36% | +6,58% | FEEDBACK RAPIDO |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 37 | 70,27% | +7,71% | +7,92% | -2,24% | +11,86% | PRIMA CALIBRAZIONE |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 39 | 64,10% | +6,62% | +5,45% | -2,74% | +10,53% | PRIMA CALIBRAZIONE |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 42 | 61,90% | +6,13% | +5,07% | -2,79% | +10,06% | PRIMA CALIBRAZIONE |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 34 | 64,71% | +6,91% | +6,75% | -2,80% | +10,27% | PRIMA CALIBRAZIONE |
| SOL | 10g | Tecnico | CALIBRABILE | 41 | 46,34% | +5,44% | -2,76% | -3,02% | +9,57% | PRIMA CALIBRAZIONE |
| SOL | 10g | Classic technical | CALIBRABILE | 25 | 60,00% | +2,22% | +2,37% | -2,99% | +6,63% | FEEDBACK RAPIDO |
| SOL | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +3,45% | +3,45% | -2,62% | +8,30% | FEEDBACK RAPIDO |
| SOL | 10g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 14g | Global confluence | BENCHMARK | 33 | 75,76% | +10,42% | +11,52% | -3,05% | +15,81% | PRIMA CALIBRAZIONE |
| SOL | 14g | Famiglia statistica | CALIBRABILE | 36 | 86,11% | +9,94% | +10,98% | -3,28% | +14,70% | PRIMA CALIBRAZIONE |
| SOL | 14g | Scanner grezzo | DIAGNOSTICO | 39 | 87,18% | +8,93% | +10,37% | -3,32% | +13,87% | PRIMA CALIBRAZIONE |
| SOL | 14g | Market regime grezzo | DIAGNOSTICO | 34 | 73,53% | +10,71% | +10,82% | -2,97% | +15,49% | PRIMA CALIBRAZIONE |
| SOL | 14g | Tecnico | CALIBRABILE | 37 | 29,73% | +6,92% | -7,47% | -3,83% | +11,87% | PRIMA CALIBRAZIONE |
| SOL | 14g | Classic technical | CALIBRABILE | 21 | 38,10% | +1,19% | -1,19% | -4,25% | +5,07% | FEEDBACK RAPIDO |
| SOL | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 50,00% | +8,38% | +8,38% | -5,94% | +13,89% | FEEDBACK RAPIDO |
| SOL | 14g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 21g | Global confluence | BENCHMARK | 27 | 70,37% | +12,82% | +11,51% | -4,78% | +18,61% | FEEDBACK RAPIDO |
| SOL | 21g | Famiglia statistica | CALIBRABILE | 30 | 83,33% | +13,10% | +14,96% | -4,70% | +18,17% | PRIMA CALIBRAZIONE |
| SOL | 21g | Scanner grezzo | DIAGNOSTICO | 33 | 84,85% | +11,66% | +13,85% | -4,82% | +16,87% | PRIMA CALIBRAZIONE |
| SOL | 21g | Market regime grezzo | DIAGNOSTICO | 28 | 67,86% | +14,22% | +14,83% | -4,40% | +19,38% | FEEDBACK RAPIDO |
| SOL | 21g | Tecnico | CALIBRABILE | 32 | 37,50% | +9,67% | -10,96% | -5,06% | +14,69% | PRIMA CALIBRAZIONE |
| SOL | 21g | Classic technical | CALIBRABILE | 21 | 38,10% | +11,18% | -11,18% | -4,64% | +15,32% | FEEDBACK RAPIDO |
| SOL | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 50,00% | +17,59% | +17,59% | -5,94% | +22,78% | FEEDBACK RAPIDO |

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

Generato: 2026-09-02 05:32 UTC

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
| BTC | 54 | PRIMA CALIBRAZIONE | 53 | 15 | 0 | 0 | Famiglia statistica | 1g | 54,72% | +0,40% | prima calibrazione possibile, solo modifiche leggere |
| SOL | 54 | PRIMA CALIBRAZIONE | 50 | 20 | 0 | 0 | Tecnico | 1g | 52,00% | +0,31% | prima calibrazione possibile, solo modifiche leggere |
| DOGE | 54 | PRIMA CALIBRAZIONE | 52 | 21 | 0 | 0 | Famiglia statistica | 1g | 59,62% | +0,68% | prima calibrazione possibile, solo modifiche leggere |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Classic technical | 21 | 38,10% | +0,30% | +0,80% | +0,07% | +1,33% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Famiglia statistica | 53 | 54,72% | +0,40% | +0,40% | -0,05% | +0,95% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 1g | BREVE | Microstruttura exchange | 3 | 66,67% | +0,27% | +0,27% | -0,26% | +0,74% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 48 | 39,58% | +0,12% | +0,55% | +0,07% | +1,09% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 2g | BREVE | Classic technical | 20 | 40,00% | +0,47% | +1,23% | +0,63% | +1,88% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Famiglia statistica | 52 | 55,77% | +0,89% | +0,89% | +0,30% | +1,56% | PESO OK | 0,0 | MEDIA |
| BTC | 2g | BREVE | Microstruttura exchange | 3 | 66,67% | +2,14% | +2,14% | +1,22% | +2,65% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 47 | 44,68% | +0,22% | +1,10% | +0,50% | +1,77% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 3g | BREVE | Classic technical | 19 | 36,84% | -0,06% | +1,96% | -0,39% | +3,39% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Famiglia statistica | 51 | 56,86% | +1,32% | +1,32% | -0,89% | +2,90% | PESO OK | 0,0 | MEDIA |
| BTC | 3g | BREVE | Microstruttura exchange | 3 | 66,67% | +1,42% | +1,42% | -0,64% | +3,18% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 46 | 36,96% | -0,15% | +1,68% | -0,68% | +3,22% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 5g | SETTIMANALE | Classic technical | 17 | 41,18% | -2,12% | +4,72% | -0,74% | +6,82% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 49 | 51,02% | +2,28% | +2,28% | -1,45% | +4,53% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 5g | SETTIMANALE | Microstruttura exchange | 3 | 33,33% | +0,36% | +0,36% | -1,24% | +3,59% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 44 | 40,91% | -1,19% | +2,66% | -1,23% | +4,97% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 7g | SETTIMANALE | Classic technical | 15 | 33,33% | -4,83% | +7,45% | -0,59% | +10,35% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 47 | 59,57% | +3,22% | +3,22% | -1,63% | +5,83% | PESO OK | 0,0 | MEDIA |
| BTC | 7g | SETTIMANALE | Microstruttura exchange | 3 | 66,67% | +0,68% | +0,68% | -1,68% | +3,81% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 42 | 38,10% | -2,20% | +3,87% | -1,38% | +6,39% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 10g | SETTIMANALE | Classic technical | 12 | 33,33% | -7,08% | +10,50% | -0,15% | +13,38% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 44 | 61,36% | +4,34% | +4,34% | -1,82% | +7,15% | PESO OK | 0,0 | MEDIA |
| BTC | 10g | SETTIMANALE | Microstruttura exchange | 2 | 50,00% | +0,69% | +0,69% | -0,88% | +5,44% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 39 | 38,46% | -1,77% | +5,05% | -1,52% | +7,91% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 14g | SWING | Classic technical | 8 | 25,00% | -12,28% | +12,28% | -0,83% | +16,12% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Famiglia statistica | 40 | 62,50% | +6,11% | +6,11% | -2,31% | +9,47% | PESO OK | 0,0 | MEDIA |
| BTC | 14g | SWING | Microstruttura exchange | 1 | 0,00% | -2,25% | -2,25% | -3,05% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 35 | 57,14% | +0,24% | +7,16% | -2,00% | +10,58% | PESO OK | 0,0 | MEDIA |
| BTC | 21g | SWING | Classic technical | 4 | 0,00% | -11,68% | +11,68% | -1,55% | +14,27% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Famiglia statistica | 34 | 64,71% | +7,57% | +7,57% | -3,00% | +11,24% | PESO OK | 0,0 | MEDIA |
| BTC | 21g | SWING | Microstruttura exchange | 1 | 100,00% | +1,21% | +1,21% | -3,06% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Tecnico | 29 | 37,93% | +1,92% | +8,61% | -2,74% | +12,34% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Classic technical | 4 | 0,00% | -24,06% | +24,06% | -1,55% | +28,48% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Famiglia statistica | 26 | 80,77% | +11,00% | +11,00% | -2,98% | +14,99% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Microstruttura exchange | 1 | 100,00% | +0,16% | +0,16% | -3,06% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Tecnico | 21 | 28,57% | -8,42% | +10,59% | -2,63% | +15,03% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Famiglia statistica | 11 | 100,00% | +22,96% | +22,96% | -2,62% | +26,80% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Tecnico | 10 | 40,00% | -5,30% | +23,20% | -2,56% | +27,04% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 31 | 41,94% | -0,51% | +0,27% | -0,38% | +0,97% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 1g | BREVE | Famiglia statistica | 52 | 59,62% | +0,68% | +0,25% | -0,39% | +1,20% | PESO OK | 0,0 | MEDIA |
| DOGE | 1g | BREVE | Microstruttura exchange | 8 | 62,50% | +2,09% | +2,48% | +0,94% | +3,13% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 46 | 52,17% | +0,32% | +0,14% | -0,52% | +1,07% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Classic technical | 31 | 45,16% | -1,20% | +0,67% | -0,10% | +1,65% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Famiglia statistica | 51 | 56,86% | +1,13% | +0,56% | -0,19% | +1,76% | PESO OK | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Microstruttura exchange | 8 | 50,00% | +3,05% | +3,38% | +2,44% | +5,44% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 45 | 55,56% | +0,50% | +0,09% | -0,64% | +1,27% | PESO OK | 0,0 | MEDIA |
| DOGE | 3g | BREVE | Classic technical | 31 | 32,26% | -2,13% | +1,30% | -1,89% | +4,20% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 3g | BREVE | Famiglia statistica | 50 | 56,00% | +1,67% | +0,92% | -1,78% | +3,65% | PESO OK | 0,0 | MEDIA |
| DOGE | 3g | BREVE | Microstruttura exchange | 8 | 50,00% | +2,64% | +2,90% | -0,79% | +6,76% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 44 | 43,18% | +0,30% | -0,08% | -2,11% | +2,52% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 5g | SETTIMANALE | Classic technical | 31 | 38,71% | -3,99% | +2,48% | -2,71% | +6,71% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 48 | 54,17% | +2,79% | +1,85% | -2,52% | +6,07% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 5g | SETTIMANALE | Microstruttura exchange | 7 | 42,86% | +2,00% | +2,23% | -1,09% | +8,98% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 42 | 54,76% | +0,25% | +0,56% | -3,05% | +4,79% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 7g | SETTIMANALE | Classic technical | 31 | 38,71% | -4,80% | +2,76% | -3,30% | +8,15% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 46 | 58,70% | +3,63% | +2,70% | -2,83% | +8,13% | PESO OK | 0,0 | MEDIA |
| DOGE | 7g | SETTIMANALE | Microstruttura exchange | 7 | 42,86% | +0,24% | +0,39% | -1,74% | +8,98% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 40 | 57,50% | +1,09% | +1,06% | -3,46% | +6,40% | PESO OK | 0,0 | MEDIA |
| DOGE | 10g | SETTIMANALE | Classic technical | 29 | 44,83% | -4,12% | +2,95% | -3,35% | +9,95% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 44 | 61,36% | +4,61% | +3,17% | -3,00% | +9,92% | PESO OK | 0,0 | MEDIA |
| DOGE | 10g | SETTIMANALE | Microstruttura exchange | 6 | 66,67% | +1,21% | +1,71% | -1,24% | +10,26% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 37 | 64,86% | +1,99% | +0,95% | -3,59% | +7,32% | PESO OK | 0,0 | MEDIA |
| DOGE | 14g | SWING | Classic technical | 27 | 51,85% | -4,09% | +4,09% | -3,41% | +12,32% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Famiglia statistica | 40 | 75,00% | +7,73% | +5,39% | -3,35% | +13,24% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 14g | SWING | Microstruttura exchange | 4 | 75,00% | +2,65% | +12,47% | -1,31% | +16,91% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 33 | 66,67% | +1,05% | +1,58% | -4,09% | +8,18% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 21g | SWING | Classic technical | 22 | 68,18% | -2,23% | +2,23% | -4,78% | +9,45% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Famiglia statistica | 34 | 85,29% | +10,34% | +6,86% | -4,31% | +16,06% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 21g | SWING | Microstruttura exchange | 4 | 75,00% | -0,95% | +12,49% | -1,31% | +25,23% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Tecnico | 30 | 63,33% | -5,01% | +5,01% | -4,70% | +12,46% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 30g | MEDIO | Classic technical | 20 | 55,00% | -7,30% | +7,30% | -5,27% | +16,83% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Famiglia statistica | 26 | 84,62% | +7,69% | +9,45% | -5,24% | +20,68% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Microstruttura exchange | 2 | 100,00% | +31,53% | +31,53% | -1,85% | +40,20% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Tecnico | 26 | 46,15% | -9,45% | +9,45% | -5,24% | +20,68% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Classic technical | 10 | 0,00% | -19,37% | +19,37% | -6,60% | +36,59% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Famiglia statistica | 11 | 0,00% | -18,98% | +18,98% | -6,73% | +36,47% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Tecnico | 11 | 0,00% | -18,98% | +18,98% | -6,73% | +36,47% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Classic technical | 34 | 52,94% | +0,50% | +0,55% | -0,24% | +1,51% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 1g | BREVE | Famiglia statistica | 48 | 58,33% | +0,32% | +0,33% | -0,28% | +1,23% | PESO OK | 0,0 | MEDIA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 50 | 52,00% | +0,31% | +0,33% | -0,32% | +1,19% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Classic technical | 33 | 51,52% | +0,99% | +1,02% | +0,13% | +2,00% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Famiglia statistica | 47 | 46,81% | +0,47% | +0,99% | +0,05% | +1,80% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Microstruttura exchange | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 49 | 42,86% | +0,25% | +0,87% | +0,01% | +1,97% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Classic technical | 32 | 56,25% | +1,26% | +1,43% | -1,49% | +3,61% | PESO OK | 0,0 | MEDIA |
| SOL | 3g | BREVE | Famiglia statistica | 46 | 50,00% | +1,06% | +1,70% | -1,52% | +3,95% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Microstruttura exchange | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 48 | 50,00% | +0,09% | +1,45% | -1,58% | +3,62% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Classic technical | 30 | 63,33% | +2,16% | +2,35% | -2,00% | +5,51% | PESO OK | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 44 | 56,82% | +1,94% | +3,18% | -2,02% | +6,57% | PESO OK | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 46 | 50,00% | -0,44% | +3,03% | -2,20% | +6,28% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Classic technical | 28 | 57,14% | +2,76% | +2,69% | -2,36% | +6,58% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 42 | 64,29% | +3,20% | +4,71% | -2,30% | +8,65% | PESO OK | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 44 | 43,18% | -1,35% | +4,35% | -2,51% | +8,28% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 10g | SETTIMANALE | Classic technical | 25 | 60,00% | +2,37% | +2,22% | -2,99% | +6,63% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 39 | 64,10% | +5,45% | +6,62% | -2,74% | +10,53% | PESO OK | 0,0 | MEDIA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Microstruttura exchange | 3 | 66,67% | +3,45% | +3,45% | -2,62% | +8,30% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 41 | 46,34% | -2,76% | +5,44% | -3,02% | +9,57% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 14g | SWING | Classic technical | 21 | 38,10% | -1,19% | +1,19% | -4,25% | +5,07% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Famiglia statistica | 36 | 86,11% | +10,98% | +9,94% | -3,28% | +14,70% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 14g | SWING | Frattale SOL | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Microstruttura exchange | 2 | 50,00% | +8,38% | +8,38% | -5,94% | +13,89% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Tecnico | 37 | 29,73% | -7,47% | +6,92% | -3,83% | +11,87% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 21g | SWING | Classic technical | 21 | 38,10% | -11,18% | +11,18% | -4,64% | +15,32% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Famiglia statistica | 30 | 83,33% | +14,96% | +13,10% | -4,70% | +18,17% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 21g | SWING | Frattale SOL | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Microstruttura exchange | 2 | 50,00% | +17,59% | +17,59% | -5,94% | +22,78% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Tecnico | 32 | 37,50% | -10,96% | +9,67% | -5,06% | +14,69% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 30g | MEDIO | Classic technical | 18 | 11,11% | -24,17% | +24,17% | -5,27% | +30,07% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Famiglia statistica | 22 | 86,36% | +19,08% | +19,56% | -6,09% | +25,16% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Frattale SOL | 1 | 0,00% | -4,50% | -4,50% | -9,39% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Microstruttura exchange | 1 | 100,00% | +8,54% | +8,54% | -9,62% | +9,47% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Tecnico | 26 | 15,38% | -17,34% | +16,62% | -6,21% | +21,88% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Classic technical | 4 | 0,00% | -36,37% | +36,37% | -6,39% | +45,71% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Famiglia statistica | 8 | 12,50% | -21,42% | +29,92% | -7,77% | +37,49% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Frattale SOL | 1 | 100,00% | +19,26% | +19,26% | -9,39% | +23,73% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Tecnico | 11 | 36,36% | -14,12% | +32,02% | -7,51% | +38,64% | OSSERVA | 0,0 | BASSA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 50 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 38 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 53 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Classic technical | 60 | 38,33% | +0,24% |
| BTC | BREVE | Famiglia statistica | 156 | 55,77% | +0,87% |
| BTC | BREVE | Microstruttura exchange | 9 | 66,67% | +1,28% |
| BTC | BREVE | Tecnico | 141 | 40,43% | +0,06% |
| BTC | SETTIMANALE | Classic technical | 44 | 36,36% | -4,39% |
| BTC | SETTIMANALE | Famiglia statistica | 140 | 57,14% | +3,24% |
| BTC | SETTIMANALE | Microstruttura exchange | 8 | 50,00% | +0,56% |
| BTC | SETTIMANALE | Tecnico | 125 | 39,20% | -1,71% |
| BTC | SWING | Classic technical | 12 | 16,67% | -12,08% |
| BTC | SWING | Famiglia statistica | 74 | 63,51% | +6,78% |
| BTC | SWING | Microstruttura exchange | 2 | 50,00% | -0,52% |
| BTC | SWING | Tecnico | 64 | 48,44% | +1,00% |
| BTC | MEDIO | Classic technical | 4 | 0,00% | -24,06% |
| BTC | MEDIO | Famiglia statistica | 37 | 86,49% | +14,55% |
| BTC | MEDIO | Microstruttura exchange | 1 | 100,00% | +0,16% |
| BTC | MEDIO | Tecnico | 31 | 32,26% | -7,42% |
| DOGE | BREVE | Classic technical | 93 | 39,78% | -1,28% |
| DOGE | BREVE | Famiglia statistica | 153 | 57,52% | +1,16% |
| DOGE | BREVE | Microstruttura exchange | 24 | 54,17% | +2,59% |
| DOGE | BREVE | Tecnico | 135 | 50,37% | +0,38% |
| DOGE | SETTIMANALE | Classic technical | 91 | 40,66% | -4,31% |
| DOGE | SETTIMANALE | Famiglia statistica | 138 | 57,97% | +3,65% |
| DOGE | SETTIMANALE | Microstruttura exchange | 20 | 50,00% | +1,15% |
| DOGE | SETTIMANALE | Tecnico | 119 | 58,82% | +1,07% |
| DOGE | SWING | Classic technical | 49 | 59,18% | -3,25% |
| DOGE | SWING | Famiglia statistica | 74 | 79,73% | +8,93% |
| DOGE | SWING | Microstruttura exchange | 8 | 75,00% | +0,85% |
| DOGE | SWING | Tecnico | 63 | 65,08% | -1,84% |
| DOGE | MEDIO | Classic technical | 30 | 36,67% | -11,32% |
| DOGE | MEDIO | Famiglia statistica | 37 | 59,46% | -0,24% |
| DOGE | MEDIO | Microstruttura exchange | 2 | 100,00% | +31,53% |
| DOGE | MEDIO | Tecnico | 37 | 32,43% | -12,29% |
| SOL | BREVE | Classic technical | 99 | 53,54% | +0,91% |
| SOL | BREVE | Famiglia statistica | 141 | 51,77% | +0,61% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 15 | 53,33% | +1,74% |
| SOL | BREVE | Tecnico | 147 | 48,30% | +0,22% |
| SOL | SETTIMANALE | Classic technical | 83 | 60,24% | +2,42% |
| SOL | SETTIMANALE | Famiglia statistica | 125 | 61,60% | +3,46% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Microstruttura exchange | 13 | 61,54% | +3,01% |
| SOL | SETTIMANALE | Tecnico | 131 | 46,56% | -1,47% |
| SOL | SWING | Classic technical | 42 | 38,10% | -6,19% |
| SOL | SWING | Famiglia statistica | 66 | 84,85% | +12,79% |
| SOL | SWING | Frattale SOL | 2 | 0,00% | -3,49% |
| SOL | SWING | Microstruttura exchange | 4 | 50,00% | +12,98% |
| SOL | SWING | Tecnico | 69 | 33,33% | -9,09% |
| SOL | MEDIO | Classic technical | 22 | 9,09% | -26,39% |
| SOL | MEDIO | Famiglia statistica | 30 | 66,67% | +8,28% |
| SOL | MEDIO | Frattale SOL | 2 | 50,00% | +7,38% |
| SOL | MEDIO | Microstruttura exchange | 1 | 100,00% | +8,54% |
| SOL | MEDIO | Tecnico | 37 | 21,62% | -16,38% |

## Aree ancora in attesa

| Asset | Famiglia | Righe senza controlli | Stato |
| --- | --- | --- | --- |
| BTC | BREVE | 3 | in attesa di controlli maturati |
| BTC | SETTIMANALE | 3 | in attesa di controlli maturati |
| BTC | SWING | 2 | in attesa di controlli maturati |
| BTC | MEDIO | 9 | in attesa di controlli maturati |
| SOL | MEDIO | 6 | in attesa di controlli maturati |
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
| BTC     |         54 |              26 |          28 | RACCOLTA DATI | 0,00%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| SOL     |         54 |              26 |          28 | RACCOLTA DATI | 3,85%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| DOGE    |         54 |              26 |          28 | RACCOLTA DATI | 7,69%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |

Regola: sotto 60 controlli osserva soltanto; da 100+ controlli può diventare utile per correggere rischio spot/leva nel Decision Report.

## Ultima lettura rapida

| Asset   | Rischio spot   | Rischio leva   | Nota leva                                                               |
|:--------|:---------------|:---------------|:------------------------------------------------------------------------|
| BTC     | ALTO           | MOLTO ALTO     | spot preferibile; leva molto pericolosa anche 2x/3x senza margine largo |
| SOL     | ALTO           | MOLTO ALTO     | spot preferibile; leva molto pericolosa anche 2x/3x senza margine largo |
| DOGE    | ALTO           | MOLTO ALTO     | spot/tranche; se proprio leva, massimo 2x con margine molto largo       |
<!-- RISK_CALIBRATION_END -->

</details>
<!-- COMPACT_SECTION_END:risk_calibration -->

<!-- COMPACT_SECTION_START:global_confluence -->
<details open>
<summary><strong>🌐 Global Confluence — quadro finale</strong></summary>

<!-- GLOBAL_CONFLUENCE_START -->
# Sintesi finale di confluenza

Generato: 2026-09-02 05:32 UTC


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
| SOL | +7 | POSITIVA FORTE | Rialzista | MEDIA / ALTA | HOLD / ACCUMULO A TRANCHE, NO LEVA AGGRESSIVA | Doppio minimo target raggiunto finché mantiene 78,73; nuova conferma tecnica sopra 110,04; milestone analogiche 105,25 / 124,40, valide soltanto se rientra anche il gap frattale. | Allarmi sotto 82,37 / 74,20 / 62,19. |
| DOGE | -1 | DEBOLE / FRAGILE | Fragile | BASSA / RACCOLTA DATI | EVITA LONG / SOLO RIMBALZI VELOCI | Sopra 0.09998 migliora; sopra 0.06933 viene invalidato il pattern ribassista dominante. | Sotto 0.06895 il rischio ribassista aumenta. |

## Punteggi per modulo

| Asset | Scanner grezzo | Market grezzo | Famiglia statistica | Scanner path | Tecnico | Classic tech | Frattale SOL | Fractal path | RSI top-cycle | Lifecycle EMA | Exchange flow | Futures | Daily change | Totale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +3 | 0 | +3 | 0 | +3 | +1 | 0 | 0 | 0 | 0 | 0 | 0 | +1 | +8 |
| SOL | +3 | 0 | +3 | 0 | +3 | +1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | +7 |
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

- Famiglia statistica: **+3** — Scanner grezzo +3, Market Regime grezzo 0, match regime 1. Regime ignorato: meno di 5 match utili. Punteggio contato nel Global: +3.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **+3** — Casi positivi 72,50%, return centrale 30g +7,19%. Direzione scanner: SALITA. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **0** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 1, positivi 30g 100,00%, return p50 +29,98%.
- Scanner path: **0** — Controlli disponibili 51. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **+3** — Score tecnico 10/12, verdetto rialzista tecnico, trend rialzista, struttura rialzista con massimi e minimi crescenti, divergenza rialzista nascosta rsi, Wyckoff markup / fase rialzista, pattern score 0 (rialzista Doppio minimo / TARGET RAGGIUNTO; ribassista Doppio massimo / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **+1** — Score classico 8/12, verdetto COSTRUTTIVO / CONFERMA PARZIALE, stage STAGE 3 / DISTRIBUZIONE O PAUSA, struttura MASSIMI E MINIMI CRESCENTI, Wyckoff SIGN OF STRENGTH POSSIBILE, volatilità locale MEDIO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Non applicabile a questo asset.
- Fractal path: **0** — Non applicabile a questo asset.
- RSI top-cycle: **0** — Non applicabile a questo asset.
- Lifecycle EMA: **0** — Non applicabile a questo asset.
- Exchange flow: **0** — Flow +0.75, derivati -1.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +0.00; exchange 3/3, copertura 100%, consenso bull 0, bear 1, divergenze 0, campioni 4h 9 su 4.00h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias MISTA / NEUTRALE; confidenza BASSA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Misto, forza 1/5.
- Daily change: **+1** — BTC: cambiamento medio in miglioramento rispetto a ieri.

Conferme: Prima resistenza sopra 81.347; conferma del doppio minimo sopra 66.910.

Invalidazioni: Sotto 62.488 il quadro tecnico peggiora.

### SOL

- Confluenza: **POSITIVA FORTE**
- Bias: **Rialzista**
- Punteggio finale: **+7**
- Affidabilità: **MEDIA / ALTA**
- Azione coerente: **HOLD / ACCUMULO A TRANCHE, NO LEVA AGGRESSIVA**

SOL ha una confluenza molto interessante, ma resta più rischiosa di BTC. Le conferme tecniche e frattali devono comunque reggere prima di usare leva.

Dettaglio moduli:

- Famiglia statistica: **+3** — Scanner grezzo +3, Market Regime grezzo 0, match regime 1. Regime ignorato: meno di 5 match utili. Punteggio contato nel Global: +3.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **+3** — Casi positivi 67,50%, return centrale 30g +6,71%. Direzione scanner: SALITA. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **0** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 1, positivi 30g 100,00%, return p50 +34,95%.
- Scanner path: **0** — Controlli disponibili 51. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **+3** — Score tecnico 9/12, verdetto rialzista tecnico, trend rialzista, struttura rialzista con massimi e minimi crescenti, divergenza nessuna, Wyckoff markup / fase rialzista, pattern score 0 (rialzista Doppio minimo / TARGET RAGGIUNTO; ribassista Doppio massimo / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **+1** — Score classico 7/12, verdetto COSTRUTTIVO / CONFERMA PARZIALE, stage STAGE 3 / DISTRIBUZIONE O PAUSA, struttura MASSIMI E MINIMI CRESCENTI, Wyckoff SIGN OF STRENGTH POSSIBILE, volatilità locale MEDIO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Verdetto ANALOGIA DEBOLE / SCENARIO SECONDARIO, somiglianza strutturale +65,97%, aderenza live +70,75%, errore live +14,63%, gap corrente +3,59%, peso operativo 0, tracking STRUTTURA STABILE, fase FRATTALE SOLO DI CONTESTO, rischio ALTO.
- Fractal path: **0** — Controlli disponibili 48, ma percorso ancorato non aderente: gap +3,59%, errore live +14,63%. Peso 0.
- RSI top-cycle: **0** — Rischio top-cycle RSI: BASSO.
- Lifecycle EMA: **0** — Contesto non pesato nel Global. Lifecycle score 2, bias CONTESTO DA OSSERVARE, EMA200 111,28 $, upside EMA200 +11,03%, gap EMA50/EMA200 -5,88%, hit EMA200 12w +73,33%, trend STABILE / DA CONFERMARE. Peso Global forzato a 0.
- Exchange flow: **0** — Flow +1.75, derivati +0.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +0.50; exchange 3/3, copertura 100%, consenso bull 0, bear 1, divergenze 1, campioni 4h 9 su 4.00h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias LEGGERMENTE POSITIVA / NON PESATA; confidenza BASSA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Misto, forza 1/5.
- Daily change: **0** — SOL: cambiamento medio in misto rispetto a ieri.

Conferme: Doppio minimo target raggiunto finché mantiene 78,73; nuova conferma tecnica sopra 110,04; milestone analogiche 105,25 / 124,40, valide soltanto se rientra anche il gap frattale.

Invalidazioni: Allarmi sotto 82,37 / 74,20 / 62,19.

### DOGE

- Confluenza: **DEBOLE / FRAGILE**
- Bias: **Fragile**
- Punteggio finale: **-1**
- Affidabilità: **BASSA / RACCOLTA DATI**
- Azione coerente: **EVITA LONG / SOLO RIMBALZI VELOCI**

DOGE non ha ancora una confluenza pulita. Serve conferma tecnica prima di trattarlo come asset forte.

Dettaglio moduli:

- Famiglia statistica: **-2** — Scanner grezzo -2, Market Regime grezzo 0, match regime 1. Regime ignorato: meno di 5 match utili. Punteggio contato nel Global: -2.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **-2** — Casi positivi 27,50%, return centrale 30g -7,54%. Direzione scanner: DISCESA. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **0** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 1, positivi 30g 0,00%, return p50 -16,46%.
- Scanner path: **0** — Controlli disponibili 51. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **+2** — Score tecnico 4/12, verdetto costruttivo ma non confermato, trend misto, struttura rialzista con massimi e minimi crescenti, divergenza nessuna, Wyckoff possibile accumulazione, pattern score 0 (rialzista Triplo minimo / TARGET RAGGIUNTO; ribassista Doppio massimo / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **0** — Score classico 1/12, verdetto NEUTRALE / MISTO, stage STAGE 4 / MARKDOWN, struttura MASSIMI E MINIMI CRESCENTI, Wyckoff ACCUMULO POSSIBILE / RANGE BASSO, volatilità locale MEDIO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Non applicabile a questo asset.
- Fractal path: **0** — Non applicabile a questo asset.
- RSI top-cycle: **0** — Non applicabile a questo asset.
- Lifecycle EMA: **0** — Non applicabile a questo asset.
- Exchange flow: **0** — Flow +0.75, derivati +0.50, affollamento +0.00, liquidazioni +0.00, conferme tecniche +0.50; exchange 3/3, copertura 100%, consenso bull 0, bear 2, divergenze 1, campioni 4h 9 su 4.00h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias LEGGERMENTE POSITIVA / NON PESATA; confidenza BASSA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Rischio sotto, forza 2/5.
- Daily change: **-1** — DOGE: cambiamento medio in peggioramento rispetto a ieri.

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

Generato: 2026-09-02 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [btc_macro_cycle_report.md](btc_macro_cycle_report.md)

Questo modulo descrive il contesto macro di Bitcoin. Non genera entrate tattiche, non autorizza leva e pesa **0** nel Global Confluence.

## Sintesi

| Voce | Valore | Lettura |
| --- | --- | --- |
| Prezzo BTC | 77.708 $ | prezzo corrente |
| Power Law centrale | 124.461 $ | deviazione -37,56% |
| Banda p10-p90 | 77.325 $ / 314.441 $ | BASSA NEL CORRIDOIO |
| Percentile residuo | 10,67% | posizione storica nel corridoio |
| Esponente β | 5,8079 | R² log-log 91,93% |
| Stabilità β | BASSA | range 1,3165 cambiando finestra |
| Ultimo halving | 2024-04-19 | 866 giorni fa |
| Fase ciclo | 59,28% | percentuale indicativa del ciclo quadriennale |
| Peso Global | 0 | CONTESTO MACRO / DIAGNOSTICO |

La Power Law viene trattata come regressione empirica, non come legge fisica. Il report mostra quanto cambia l'esponente usando finestre iniziali diverse e la confronta con il benchmark ingenuo 'prezzo invariato'.

## Bitcoin Power Law

- Campione: 2014-09-17 → 2026-09-02 (4368 osservazioni)
- Formula stimata: prezzo ≈ exp(-39.0924) × giorni^5.8079
- Prezzo centrale oggi: **124.461 $**
- Posizione corrente: **BASSA NEL CORRIDOIO**, percentile 10,67%
- Scarto dal centro: **-37,56%**

![Bitcoin Power Law](btc_power_law_chart.png)

![Bitcoin Power Law log-log](btc_power_law_loglog_chart.png)

### Stabilità dell'esponente

| Inizio campione | β | R² log-log |
| --- | --- | --- |
| 2014 | 5,8079 | 91,93% |
| 2015 | 5,8906 | 91,48% |
| 2016 | 5,5750 | 87,73% |
| 2017 | 4,8466 | 82,89% |
| 2018 | 4,5740 | 78,38% |

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
| 2012-11-28 → 2016-07-09 | 2015-01-19 | +9,99% | +3,60% | +27,94% | +76,93% |
| 2016-07-09 → 2020-05-11 | 2018-10-18 | -14,24% | -43,57% | -19,16% | +23,11% |
| 2020-05-11 → 2024-04-19 | 2022-09-11 | -12,48% | -21,32% | -7,27% | +15,59% |

Campione molto piccolo: questi rendimenti sono contesto di ciclo, non probabilità affidabili.

## SOL/BTC e DOGE/BTC dentro il tempo Bitcoin

![Altcoin nel ciclo BTC](alt_btc_cycle_spirals.png)

| Asset | Coppia | Forza vs BTC | Score raw | Candidato | 30g | Peso Global |
| --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | SOVRAPERFORMA BTC | 5 | 1 | 11.45203819388616 | 0 |
| DOGE | DOGE/BTC | SOTTOPERFORMA BTC | -7 | -1 | -5.349331496508536 | 0 |

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

Generato: 2026-09-02 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [relative_strength_btc_report.md](relative_strength_btc_report.md)

Questo modulo controlla se SOL e DOGE stanno davvero battendo Bitcoin. Una salita in USD accompagnata da una coppia ALT/BTC ribassista è spesso soltanto trascinamento di BTC.

**Protezione iniziale:** il candidato relativo è limitato a -1/0/+1, ma il peso nel Global resta **0**. La coppia BTC conferma o indebolisce il tecnico USD; non viene sommata come secondo modulo indipendente.

## Sintesi

| Asset | Coppia | Prezzo | Score raw | Candidato | Peso Global | Forza vs BTC | Confidenza | 30g | Tecnico USD | Lettura combinata |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | 0.00128950 | +5 | +1 | 0 | SOVRAPERFORMA BTC | MEDIA | +11,45% | RIALZISTA | CONFERMA FORTE: sale in USD e batte BTC |
| DOGE | DOGE/BTC | 0.00000105 | -7 | -1 | 0 | SOTTOPERFORMA BTC | MEDIA | -5,35% | RIALZISTA | SALE SOLO IN USD: BTC resta più forte |

## Matrice di lettura

| ALT/USD | ALT/BTC | Interpretazione |
| --- | --- | --- |
| Rialzista | Rialzista | Conferma migliore: sale e batte BTC |
| Rialzista | Ribassista | Sale soprattutto perché BTC trascina il mercato |
| Ribassista | Rialzista | Forza relativa nascosta / possibile rotazione futura |
| Ribassista | Ribassista | Debolezza completa |

## SOL/BTC

- **Verdetto relativo:** SOVRAPERFORMA BTC (+5)
- **Candidato futuro:** +1; **peso attuale Global: 0**
- **Lettura combinata USD/BTC:** CONFERMA FORTE: sale in USD e batte BTC
- **Struttura:** MASSIMI E MINIMI CRESCENTI
- **Rendimenti relativi:** 7g +4,84%; 30g +11,45%; 90g +15,34%; 180g +3,08%
- **Daily:** RSI 58.13; MA50 0.00119919; MA200 0.00118082
- **Weekly:** MA30 0.00118525; RSI 55.43
- **Livelli:** supporto 0.00122200; resistenza 0.00129400; breakout 60g 0.00136900; breakdown 60g 0.00112700
- **Pattern:** DOPPIO MINIMO / TARGET RAGGIUNTO; neckline 0.00120200; target 0.00125350
- **Fibonacci:** VICINO — 23.6% a 0.00128404
- **Fonte:** Yahoo Finance SOL-BTC (coppia diretta)
- **Motivi score:** prezzo sopra MA50 daily; prezzo sopra MA200 daily; prezzo sopra MA30 weekly; MA30 weekly in discesa; struttura con massimi/minimi crescenti; RSI relativo forte; MACD relativo positivo

![Grafico SOL/BTC](relative_strength_SOLBTC.png)

## DOGE/BTC

- **Verdetto relativo:** SOTTOPERFORMA BTC (-7)
- **Candidato futuro:** -1; **peso attuale Global: 0**
- **Lettura combinata USD/BTC:** SALE SOLO IN USD: BTC resta più forte
- **Struttura:** VOLATILITÀ IN ESPANSIONE
- **Rendimenti relativi:** 7g -3,41%; 30g -5,35%; 90g -26,16%; 180g -20,19%
- **Daily:** RSI 38.89; MA50 0.00000111; MA200 0.00000128
- **Weekly:** MA30 0.00000127; RSI 34.56
- **Livelli:** supporto 0.00000105; resistenza 0.00000114; breakout 60g 0.00000131; breakdown 60g 0.00000100
- **Pattern:** DOPPIO MINIMO / TARGET RAGGIUNTO; neckline 0.00000115; target 0.00000128
- **Fibonacci:** NON ATTIVO — 23.6% a 0.00000112
- **Fonte:** Rapporto sintetico DOGE-USD / BTC-USD (sintetica)
- **Motivi score:** prezzo sotto MA50 daily; prezzo sotto MA200 daily; MA50 daily in discesa; prezzo sotto MA30 weekly; MA30 weekly in discesa; RSI relativo debole; MACD relativo negativo

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
| SOL | 1g | 29 | 62,07% | +0,26% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 3g | 27 | 55,56% | +0,67% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 7g | 23 | 56,52% | +1,28% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 14g | 17 | 17,65% | -1,84% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 30g | 10 | 0,00% | -12,10% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 1g | 42 | 71,43% | +0,19% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 3g | 40 | 65,00% | +0,57% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 7g | 36 | 63,89% | +0,50% | ELIGIBILE FUTURO ±1 | 0 |
| DOGE | 14g | 34 | 70,59% | +0,23% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 30g | 24 | 75,00% | +1,12% | LOCKED / RACCOLTA LIVE | 0 |

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

Ultima candela SOL usata: **2 settembre 2026**

## SOL PRICE CONTEXT

| Voce | Valore | Provenienza / significato |
| --- | --- | --- |
| Anchor computazionale | 100,24 $ | 2026-09-02T05:30:22Z \| Yahoo Finance daily shared snapshot \| Close 1d |
| Candela anchor completata | NO | Stato esplicito; il valore non viene sostituito dal prezzo pubblico. |
| Riferimento pubblico corrente | 100,21 $ | 2026-09-02T05:31:00Z \| Yahoo Finance \| solo display |
| Età anchor alla generazione | 0h 1m | WITHIN_DAILY_REPORT_CADENCE |
| Gap corrente vs anchor | -0,03000 $ | -0,03% |
| Validità input modello | REPRODUCIBLE_SHARED_SNAPSHOT | Non è una dichiarazione di validità del segnale/trading. |

```text
COMPUTATIONAL_ANCHOR_PRICE=100.23999786376953
COMPUTATIONAL_ANCHOR_FIELD=Close
COMPUTATIONAL_ANCHOR_TIMESTAMP=2026-09-02T05:30:22Z
COMPUTATIONAL_ANCHOR_SYMBOL=SOL-USD
COMPUTATIONAL_ANCHOR_PROVIDER=Yahoo Finance daily shared snapshot
COMPUTATIONAL_ANCHOR_TIMEFRAME=1d
COMPUTATIONAL_ANCHOR_COMPLETED=NO
CURRENT_PUBLIC_REFERENCE_PRICE=100.20999908447266
CURRENT_PUBLIC_REFERENCE_TIMESTAMP=2026-09-02T05:31:00Z
CURRENT_PUBLIC_REFERENCE_ACQUIRED_AT=2026-09-02T05:32:04Z
CURRENT_PUBLIC_REFERENCE_SYMBOL=SOL-USD
CURRENT_PUBLIC_REFERENCE_PROVIDER=Yahoo Finance
CURRENT_PUBLIC_REFERENCE_FIELD=Close
CURRENT_PUBLIC_REFERENCE_TIMEFRAME=1m
CURRENT_PUBLIC_REFERENCE_STATUS=AVAILABLE
ANCHOR_AGE_SECONDS=102.356909
ANCHOR_AGE_HOURS=0.028432474722222222
CURRENT_VS_ANCHOR_GAP_USD=-0.029998779296875
CURRENT_VS_ANCHOR_GAP_PCT=-0.029926955243597675
```

## Verdetto: ANALOGIA DEBOLE / SCENARIO SECONDARIO

- **Fase attuale:** FRATTALE SOLO DI CONTESTO
- **Somiglianza totale:** +65,97%
- **Somiglianza strutturale:** +65,97%
- **Aderenza prezzo live:** +70,75%
- **Errore medio live:** +14,63%
- **Gap prezzo corrente:** +3,59%
- **Peso operativo suggerito:** 0
- **Affidabilita:** BASSA
- **Rischio fase:** ALTO
- **Trend tracking:** STRUTTURA STABILE
- **Sintesi:** Esistono alcuni elementi comuni, ma non abbastanza per una conferma.
- **SOL è al giorno:** 88 dal bottom usato.
- **Giorno BTC equivalente:** 2023-02-17
- **Prossimo step:** Proiezione condizionale, non conferma operativa: **Fase negativa / rischio discesa.** Zona bassa **91,25 $** intorno al **16 settembre 2026**; zona alta **101,32 $** intorno al **5 settembre 2026**; fine step circa **91,25 $** entro il **16 settembre 2026**.

### Metadata aderenza prezzo

```text
OPERATIONAL_VERDICT_REASON=ANALOGIA DEBOLE / SCENARIO SECONDARIO
PRICE_ADHERENCE_FAILED=NO
PRICE_ADHERENCE_LIVE_AVG_GAP_FAILED=NO
PRICE_ADHERENCE_LAST_GAP_FAILED=NO
PRICE_ADHERENCE_LIVE_AVG_GAP_THRESHOLD_PCT=15.0
PRICE_ADHERENCE_LAST_GAP_THRESHOLD_PCT=18.0
PRICE_ADHERENCE_OBSERVED_LIVE_AVG_GAP_PCT=14.626563430856939
PRICE_ADHERENCE_OBSERVED_LAST_GAP_PCT=3.586195603591702
```

## Somiglianza prima e dopo inizio programma

Questa sezione separa la somiglianza della forma dall'aderenza reale del prezzo.

- **Inizio programma/scanner:** 3 luglio 2026
- **Prima del programma** = backtest retroattivo.
- **Da inizio programma** = verifica live: è la parte più importante per l'uso operativo.

| Periodo | Date | Giorni | Aderenza prezzo | Errore medio | Gap ultimo | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| Prima del programma | 6 giugno 2026 -> 2 luglio 2026 | 27 | +87,95% | +6,02% | +21,89% | ABBASTANZA ALLINEATO |
| Da inizio programma | 3 luglio 2026 -> 2 settembre 2026 | 62 | +70,75% | +14,63% | +3,59% | DEVIAZIONE MODERATA |
| Totale dal bottom | 6 giugno 2026 -> 2 settembre 2026 | 89 | +75,97% | +12,02% | +3,59% | DEVIAZIONE MODERATA |

Nota: un frattale può avere una forma simile ma un prezzo distante. In quel caso non è operativo finché il gap non rientra.

## Lettura operativa veloce

Il frattale resta non operativo. Motivo effettivo: ANALOGIA DEBOLE / SCENARIO SECONDARIO.

| Voce | Risposta | Perché |
| --- | --- | --- |
| Uso operativo | NO | Peso 0 per il verdetto: ANALOGIA DEBOLE / SCENARIO SECONDARIO. |
| Aderenza live | +70,75% | Errore medio live +14,63%. |
| Gap corrente | +3,59% | Metrica separata dal motivo del verdetto. |
| Prima conferma prezzo | 105,25 $ | Serve anche miglioramento del gap, non solo una candela sopra il livello. |
| Seconda conferma | 124,40 $ | Rende più credibile il percorso, ma non sostituisce l'aderenza. |
| Invalidazione soft | 82,37 $ | Sotto questa zona il quadro peggiora. |
| Invalidazione forte | 62,19 $ | Sotto il bottom il paragone è quasi rotto. |

## Target ciclo fino al top BTC 2025

| Voce | Valore |
| --- | --- |
| Stato | CONTESTO / NON OPERATIVO |
| Top BTC 2025 | 6 ottobre 2025 - 124.753 $ |
| Data SOL equivalente | 21 aprile 2029 |
| Target ciclo base dall'anchor modello | 509,05 $ |
| Massimo percorso base | 509,05 $ (21 aprile 2029) |

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
| Prima conferma | 105,25 $ | Deve accompagnarsi al rientro del gap. |
| Seconda conferma | 124,40 $ | Scenario più credibile. |
| Invalidazione soft | 82,37 $ | Il frattale si indebolisce. |
| Invalidazione forte | 62,19 $ | Il paragone si rompe. |

## Proiezione veloce con date SOL

| Orizzonte | Data SOL | BTC fece | SOL base | Min percorso | Max percorso |
| --- | --- | --- | --- | --- | --- |
| 7 giorni | 9 settembre 2026 | -5,57% | 94,66 $ | 94,66 $ | 101,32 $ |
| 14 giorni | 16 settembre 2026 | -8,97% | 91,25 $ | 91,25 $ | 101,32 $ |
| 30 giorni | 2 ottobre 2026 | +14,14% | 114,41 $ | 82,37 $ | 114,41 $ |
| 60 giorni | 1 novembre 2026 | +23,74% | 124,04 $ | 82,37 $ | 124,40 $ |
| 90 giorni | 1 dicembre 2026 | +9,23% | 109,49 $ | 82,37 $ | 124,40 $ |
| 120 giorni | 31 dicembre 2026 | +7,92% | 108,18 $ | 82,37 $ | 124,40 $ |

## Prossimi step se SOL segue BTC 2022

| Step | Date SOL | BTC fine | SOL zona bassa | SOL zona alta | SOL fine base | Lettura |
| --- | --- | --- | --- | --- | --- | --- |
| Step 1 - prossime 2 settimane | 2 settembre 2026 -> 16 settembre 2026 | -8,97% | 91,25 $ (16 settembre 2026) | 101,32 $ (5 settembre 2026) | 91,25 $ | Fase negativa / rischio discesa. |
| Step 2 - primo mese | 17 settembre 2026 -> 2 ottobre 2026 | +14,14% | 82,37 $ (23 settembre 2026) | 114,41 $ (2 ottobre 2026) | 114,41 $ | Prima retest / debolezza, poi recupero. |
| Step 3 - secondo mese | 3 ottobre 2026 -> 1 novembre 2026 | +23,74% | 110,74 $ (10 ottobre 2026) | 124,40 $ (28 ottobre 2026) | 124,04 $ | Spinta rialzista abbastanza pulita. |
| Step 4 - terzo mese | 2 novembre 2026 -> 1 dicembre 2026 | +9,23% | 109,29 $ (26 novembre 2026) | 120,52 $ (18 novembre 2026) | 109,49 $ | Spinta rialzista abbastanza pulita. |

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
| Prezzo SOL | 100,24 $ |  |
| Weekly RSI | 56,78 / linea grezza 52,47 | LINEA NON AFFIDABILE / RISCHIO NON ATTIVO — IRREALISTICA / NON OPERATIVA |
| Monthly RSI | 46,47 / linea grezza 55,48 | RSI TROPPO BASSO PER RISCHIO TOP — VALIDA / USO PRUDENTE |
| Target ciclo base | 509,05 $ | Avanzamento +19,69% |
| Rischio top-cycle RSI | BASSO | Nessun segnale top-cycle macro attivo. Prezzo ancora lontano dal target ciclo; il filtro RSI resta solo di monitoraggio. |

## Lettura semplice

- Weekly: La top-line weekly non supera i controlli di qualità. Non viene usata per generare rischio top-cycle.
- Monthly: RSI monthly è 46,5, sotto la soglia prudente 55. Anche se fosse vicino alla linea, non è una vera zona di esaurimento ciclo.
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
| Prezzo SOL | 100,24 $ |
| TVL Solana | 5,69 mld $ |
| TVL 7g | +1,54% |
| DEX volume 24h | 2,25 mld $ |
| Fees 24h | 12,27 mln $ |
| Stablecoin su Solana | 15,79 mld $ |
| Stake ratio | 69,20% |
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
| Prezzo SOL | 100,24 $ |
| EMA200 weekly target | 111,28 $ |
| Upside verso EMA200 | +11,03% |
| Distanza prezzo da EMA200 | -9,94% |
| Gap EMA50/EMA200 | -5,88% |
| Stato cross | EMA50 SOTTO EMA200 |
| RSI weekly | 56,77 |
| Età SOL | 6,4 anni |
| Analoghi storici usati | 30 |
| Max analoghi per asset | 3 |
| Hit EMA200 12w analoghi | +73,33% |
| Max gain mediano 12w | +31,94% |
| Drawdown mediano 12w | -29,41% |

Lettura semplice:

**SOLO OSSERVAZIONE**

Autocontrollo: **STABILE / DA CONFERMARE**.

Questo modulo confronta SOL con altre crypto in fasi simili di età, distanza da EMA200, EMA50/EMA200 e RSI. Non usa stock market.

Nota importante: **questo modulo ora NON pesa più nel Global Confluence**. Resta solo come contesto di ciclo e come mappa verso EMA200 weekly. Il punteggio Global resta guidato da prezzo, scanner, regime, struttura tecnica, frattale, RSI e conferme reali.

Nota: se EMA50/EMA200 sono dentro ±2%, il modulo parla di medie sovrapposte / incrocio in corso, perché exchange diversi possono mostrare il cross leggermente prima o dopo.

<!-- Generato: 2026-09-02 05:32 UTC -->
<!-- MAJOR_ALT_LIFECYCLE_SQUEEZE_END -->

</details>
<!-- COMPACT_SECTION_END:major_alt_lifecycle -->

# Report giornaliero BTC / SOL / DOGE

Aggiornato il: **2026-09-02 05:30:23 UTC**

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
- SOL: cambiamento importante, ma lettura mista.
- DOGE: cambiamento importante in peggioramento rispetto a ieri.

| Asset | Cambio | Tono | Verdetto oggi | Casi positivi oggi | Δ casi positivi |
| --- | --- | --- | --- | --- | --- |
| BTC | CAMBIAMENTO MEDIO | miglioramento | RIALZISTA | +72.50% | +5.00 punti |
| SOL | CAMBIAMENTO MEDIO | misto | RIALZISTA | +67.50% | 0.00 punti |
| DOGE | CAMBIAMENTO MEDIO | peggioramento | NEUTRALE / INCERTO | +27.50% | -7.50 punti |

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
| BTC | 73.784 $ | 85.434 $ | +62,86% | +15,79% | rimbalzo possibile | 85.434 $ | 73.784 $ | +7,14% | -13,64% | spike storicamente più resistente |
| SOL | 95,23 $ | 110,26 $ | +55,88% | +15,79% | rimbalzo possibile | 110,26 $ | 95,23 $ | +30,00% | -13,64% | spike storicamente più resistente |
| DOGE | 0,07779 $ | 0,09007 $ | +24,14% | +15,79% | rimbalzo poco frequente | 0,09007 $ | 0,07779 $ | +44,00% | -13,64% | scarico possibile |

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

- **BTC: su 40 casi simili, 35 prima sono scesi a -5,00%. Tra quei 35, 22 poi sono rimbalzati fino a +10,00%. Percentuale: +62,86% (22/35). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo possibile.**
- **BTC: su 40 casi simili, 28 prima sono saliti a +10,00%. Tra quei 28, 2 poi sono scaricati a -5,00%. Percentuale: +7,14% (2/28). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.**
- **SOL: su 40 casi simili, 34 prima sono scesi a -5,00%. Tra quei 34, 19 poi sono rimbalzati fino a +10,00%. Percentuale: +55,88% (19/34). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo possibile.**
- **SOL: su 40 casi simili, 30 prima sono saliti a +10,00%. Tra quei 30, 9 poi sono scaricati a -5,00%. Percentuale: +30,00% (9/30). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.**
- **DOGE: su 40 casi simili, 29 prima sono scesi a -5,00%. Tra quei 29, 7 poi sono rimbalzati fino a +10,00%. Percentuale: +24,14% (7/29). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.**
- **DOGE: su 40 casi simili, 25 prima sono saliti a +10,00%. Tra quei 25, 11 poi sono scaricati a -5,00%. Percentuale: +44,00% (11/25). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: scarico possibile.**

<!-- BOUNCE_AFTER_DRAWDOWN_END -->

</details>
<!-- COMPACT_SECTION_END:bounce_after_drawdown -->

<!-- COMPACT_SECTION_START:scanner_forecast -->
<details>
<summary><strong>🔭 Cono probabilistico dello scanner</strong></summary>

<!-- SCANNER_FORECAST_TRACKER_START -->
# Scanner forecast path / cono probabilistico

Generato: 2026-09-02 05:31:53 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [scanner_forecast_tracker_report.md](scanner_forecast_tracker_report.md)

## Snapshot effettivamente usato

| Asset   | Snapshot prezzo   | Generazione snapshot prezzo   | Snapshot match scanner   |
|:--------|:------------------|:------------------------------|:-------------------------|
| BTC | 2026-09-02 | 2026-09-02T05:30:22Z | 2026-09-02 05:30:23 |
| SOL | 2026-09-02 | 2026-09-02T05:30:22Z | 2026-09-02 05:30:23 |
| DOGE | 2026-09-02 | 2026-09-02T05:30:22Z | 2026-09-02 05:30:23 |

La data di generazione del report non sostituisce la data degli input: se gli snapshot locali sono più vecchi, i valori restano riferiti agli snapshot indicati in tabella.

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
| BTC | 2026-09-02 | 77.667 $ | SALITA | 72,50% | 52.437,95 $ | 73.497,02 $ | 83.250,64 $ | 93.419,12 $ | 108.183,33 $ |
| SOL | 2026-09-02 | 100,24 $ | SALITA | 67,50% | 69,77 $ | 92,76 $ | 106,97 $ | 141,75 $ | 202,68 $ |
| DOGE | 2026-09-02 | 0.08188 $ | DISCESA | 27,50% | 0.05992 $ | 0.06673 $ | 0.07570 $ | 0.08374 $ | 0.11694 $ |

## Confronto raw / regime-adjusted

Il cono raw continua a usare i 40 casi dello scanner. Il cono regime-adjusted sceglie una sola coorte nella gerarchia SAME_BTC_AND_ASSET_REGIME → SAME_ASSET_REGIME → SAME_BTC_REGIME. Ogni livello richiede almeno 5 match; le coorti non vengono mai combinate e ogni fallback è dichiarato.

| Asset   | Stato adjusted              | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level        | selection_reason              | Raw p50 30g   | Adjusted p50 30g   | Raw p90 30g   | Adjusted p90 30g   |
|:--------|:----------------------------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:----------------------|:------------------------------|:--------------|:-------------------|:--------------|:-------------------|
| BTC | INSUFFICIENT_REGIME_MATCHES | NONE | 1 | 2 | 4 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES | 83.250,64 $ | n/a | 108.183,33 $ | n/a |
| SOL | INSUFFICIENT_REGIME_MATCHES | NONE | 1 | 2 | 3 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES | 106,97 $ | n/a | 202,68 $ | n/a |
| DOGE | AVAILABLE | SAME_ASSET_REGIME | 1 | 13 | 1 | 13 | 5 | 1_SAME_ASSET_FALLBACK | FALLBACK_TO_SAME_ASSET_REGIME | 0.07570 $ | 0.07381 $ | 0.11694 $ | 0.10348 $ |

## Grafici

### BTC

![Scanner forecast BTC](scanner_forecast_BTC.png)

#### Verifica storica e discrepanza

![Verifica storica cono BTC](scanner_forecast_history_BTC.png)

- Cono congelato il **2026-08-03**; verificato fino al **2026-09-02**; stato **COMPLETO 30/30g**.
- Reale **77.657,02 $**; p50 previsto **68.882,65 $**; scarto **12,74%**.
- Errore medio assoluto **7,91%**; massimo **17,47%**; DENTRO p10-p90; DENTRO p25-p75.

#### Cono regime-adjusted

Gruppo selezionato: **NONE**; fallback: **NONE**; motivo: **INSUFFICIENT_REGIME_MATCHES**.

Non disponibile: INSUFFICIENT_REGIME_MATCHES (campione selezionato 0/5 match).

### SOL

![Scanner forecast SOL](scanner_forecast_SOL.png)

#### Verifica storica e discrepanza

![Verifica storica cono SOL](scanner_forecast_history_SOL.png)

- Cono congelato il **2026-08-03**; verificato fino al **2026-09-02**; stato **COMPLETO 30/30g**.
- Reale **100,21 $**; p50 previsto **81,90 $**; scarto **22,36%**.
- Errore medio assoluto **11,99%**; massimo **35,69%**; DENTRO p10-p90; FUORI p25-p75.

#### Cono regime-adjusted

Gruppo selezionato: **NONE**; fallback: **NONE**; motivo: **INSUFFICIENT_REGIME_MATCHES**.

Non disponibile: INSUFFICIENT_REGIME_MATCHES (campione selezionato 0/5 match).

### DOGE

![Scanner forecast DOGE](scanner_forecast_DOGE.png)

#### Verifica storica e discrepanza

![Verifica storica cono DOGE](scanner_forecast_history_DOGE.png)

- Cono congelato il **2026-08-03**; verificato fino al **2026-09-02**; stato **COMPLETO 30/30g**.
- Reale **0.08189 $**; p50 previsto **0.07225 $**; scarto **13,34%**.
- Errore medio assoluto **12,93%**; massimo **39,38%**; DENTRO p10-p90; DENTRO p25-p75.

#### Cono regime-adjusted

Gruppo selezionato: **SAME_ASSET_REGIME**; fallback: **1_SAME_ASSET_FALLBACK**; motivo: **FALLBACK_TO_SAME_ASSET_REGIME**.

**WARNING:** coorte fallback meno stringente rispetto a SAME_BTC_AND_ASSET_REGIME.

![Scanner forecast regime-adjusted DOGE](scanner_forecast_DOGE_regime_adjusted.png)

## Accuratezza percorso scanner

| Asset   | Giorno   |   Controlli | Dentro p10-p90   | Dentro p25-p75   | Errore medio abs vs p50   | Errore medio vs p50   |
|:--------|:---------|------------:|:-----------------|:-----------------|:--------------------------|:----------------------|
| BTC | 1g | 51 | 94,12% | 62,75% | 2,17% | 0,60% |
| BTC | 3g | 48 | 89,58% | 72,92% | 3,34% | 0,93% |
| BTC | 7g | 44 | 90,91% | 72,73% | 5,43% | 2,51% |
| BTC | 14g | 37 | 97,30% | 64,86% | 6,56% | 3,96% |
| BTC | 30g | 23 | 100,00% | 91,30% | 8,90% | 3,16% |
| SOL | 1g | 51 | 76,47% | 56,86% | 2,99% | 1,09% |
| SOL | 3g | 48 | 87,50% | 68,75% | 4,25% | 1,94% |
| SOL | 7g | 44 | 86,36% | 68,18% | 5,92% | 4,22% |
| SOL | 14g | 37 | 81,08% | 64,86% | 8,61% | 7,61% |
| SOL | 30g | 23 | 91,30% | 47,83% | 15,48% | 14,92% |
| DOGE | 1g | 51 | 84,31% | 56,86% | 3,43% | 0,73% |
| DOGE | 3g | 48 | 87,50% | 66,67% | 4,75% | 1,99% |
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
| BTC | 3g | 8 | 30 | RACCOLTA (22 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 7g | 8 | 30 | RACCOLTA (22 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 14g | 7 | 30 | RACCOLTA (23 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 30g | 5 | 30 | RACCOLTA (25 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 1g | 9 | 30 | RACCOLTA (21 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 3g | 8 | 30 | RACCOLTA (22 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 7g | 8 | 30 | RACCOLTA (22 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 14g | 7 | 30 | RACCOLTA (23 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 30g | 5 | 30 | RACCOLTA (25 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 1g | 9 | 30 | RACCOLTA (21 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 3g | 8 | 30 | RACCOLTA (22 mancanti) | 0,0% | 0,00% | 1,000 |
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

Righe salvate nello storico: **150**.

Questa sezione tiene un diario delle previsioni giornaliere a 30 giorni, senza appesantire il report principale.

| Data | Asset | Prezzo | Direzione | Casi positivi | Return p50 | Drawdown p50 | Max gain p50 | Controllo 30g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-09-02 | BTC | 77.667 $ | SALITA | 72,50% | 83.251 $ | 67.636 $ | 89.690 $ | 2026-10-02 |
| 2026-09-02 | DOGE | 0,08000 $ | DISCESA | 27,50% | 0,08000 $ | 0,07000 $ | 0,10000 $ | 2026-10-02 |
| 2026-09-02 | SOL | 100,24 $ | SALITA | 67,50% | 106,97 $ | 87,62 $ | 126,04 $ | 2026-10-02 |

<!-- FORECAST_30D_HISTORY_END -->

</details>
<!-- COMPACT_SECTION_END:scanner_forecast -->

<!-- COMPACT_SECTION_START:extreme_cases -->
<details>
<summary><strong>⚠️ Percorso dei casi estremi</strong></summary>

<!-- EXTREME_CASES_PATH_START -->
# Extreme cases path report

Generato: 2026-09-02 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [extreme_cases_path_report.md](extreme_cases_path_report.md)

Questo report si attiva quando i casi positivi o negativi sono almeno **80%**.

Ora misura anche il **rialzo massimo prima della discesa principale**, quindi distingue uno spike iniziale da una discesa quasi immediata.

## Trigger estremi

| Asset   | Direzione   | Trigger   | Percentuale   | Motivo                           |   Match disponibili |
|:--------|:------------|:----------|:--------------|:---------------------------------|--------------------:|
| BTC     | NESSUNO     | NO        | +72,50%       | Nessun lato sopra soglia estrema |                  40 |
| SOL     | NESSUNO     | NO        | +67,50%       | Nessun lato sopra soglia estrema |                  40 |
| DOGE    | NESSUNO     | NO        | +72,50%       | Nessun lato sopra soglia estrema |                  40 |

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
- Casi positivi / salita storica: **72,50%**
- Casi negativi / discesa storica: **27,50%**
- Quanto è netto il segnale: **forte**
- Prezzo attuale: **77.666,99 $**
- Return normale fra 30 giorni: **83.250,64 $** (7,19%)
- Drawdown normale durante il mese: **67.636,28 $** (-12,92%)
- Drawdown brutto da rispettare: **62.694,50 $** (-19,28%)
- Max gain normale durante il mese: **89.689,52 $** (15,48%)
- Max gain buono / take profit ottimistico: **97.954,82 $** (26,12%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Solana
- Direzione più probabile a 30 giorni: **SALITA**
- Casi positivi / salita storica: **67,50%**
- Casi negativi / discesa storica: **32,50%**
- Quanto è netto il segnale: **medio**
- Prezzo attuale: **100,24 $**
- Return normale fra 30 giorni: **106,97 $** (6,71%)
- Drawdown normale durante il mese: **87,62 $** (-12,59%)
- Drawdown brutto da rispettare: **79,37 $** (-20,82%)
- Max gain normale durante il mese: **126,04 $** (25,74%)
- Max gain buono / take profit ottimistico: **152,44 $** (52,07%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Dogecoin
- Direzione più probabile a 30 giorni: **DISCESA**
- Casi positivi / salita storica: **27,50%**
- Casi negativi / discesa storica: **72,50%**
- Quanto è netto il segnale: **forte**
- Prezzo attuale: **0,08 $**
- Return normale fra 30 giorni: **0,08 $** (-7,54%)
- Drawdown normale durante il mese: **0,07 $** (-10,59%)
- Drawdown brutto da rispettare: **0,06 $** (-23,00%)
- Max gain normale durante il mese: **0,10 $** (17,43%)
- Max gain buono / take profit ottimistico: **0,11 $** (33,17%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Messaggio del giorno

Il quadro generale oggi è più favorevole. Lo scanner vede più possibilità di salita su più asset.

---

# Mappa semplice asset per asset

# Bitcoin — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟢 VERDE / Favorevole
**Prezzo attuale:** 77.666,99 $

**Direzione più probabile a 30 giorni:** **SALITA**
- Probabilità storica di salita: **72,50%**
- Probabilità storica di discesa: **27,50%**
- Quanto è netto il segnale: **forte**

## Come leggere questa parte

- **Probabilità storica di salita** = su 40 casi simili, quanti hanno chiuso sopra dopo 30 giorni.
- **Probabilità storica di discesa** = su 40 casi simili, quanti hanno chiuso sotto dopo 30 giorni.
- **Quanto è netto il segnale** = quanto è grande la differenza tra salita e discesa. Non vuol dire certezza, vuol dire solo che il risultato storico non è vicino al 50/50.

La lettura principale è rialzista, con segnale forte. Nei casi storici simili, il prezzo ha chiuso sopra dopo 30 giorni più spesso di quanto abbia chiuso sotto.

## 1. Return 30d — prezzo fra 30 giorni

**Return** significa rendimento finale. Qui guardiamo dove potrebbe stare il prezzo **alla fine dei 30 giorni**, non durante il percorso.

- Se va molto male: **52.437,95 $** (-32,48%)
- Se va male: **73.497,02 $** (-5,37%)
- Scenario normale: **83.250,64 $** (7,19%)
- Se va bene: **93.419,12 $** (20,28%)
- Se va molto bene: **108.183,33 $** (39,29%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **67.636,28 $** (-12,92%)
- Discesa brutta: **62.694,50 $** (-19,28%)
- Discesa molto brutta: **51.482,01 $** (-33,71%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **89.689,52 $** (15,48%)
- Rialzo buono: **97.954,82 $** (26,12%)
- Rialzo molto forte: **118.498,18 $** (52,57%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Bitcoin tendeva a muoversi tra una zona bassa intorno a **67.636,28 $** e uno spike normale intorno a **89.689,52 $**.

La chiusura a 30 giorni era più spesso positiva: salita 72,50%, discesa 27,50%. Quindi la lettura principale è favorevole.

Nota leva BTC: se la liquidazione è vicina a 51.000 $, guarda soprattutto la discesa brutta e molto brutta. Il prezzo può recuperare dopo, ma la leva può saltare prima.

---

# Solana — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟢 VERDE / Favorevole
**Prezzo attuale:** 100,24 $

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

- Se va molto male: **69,77 $** (-30,40%)
- Se va male: **92,76 $** (-7,46%)
- Scenario normale: **106,97 $** (6,71%)
- Se va bene: **141,75 $** (41,41%)
- Se va molto bene: **202,68 $** (102,20%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **87,62 $** (-12,59%)
- Discesa brutta: **79,37 $** (-20,82%)
- Discesa molto brutta: **61,88 $** (-38,27%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **126,04 $** (25,74%)
- Rialzo buono: **152,44 $** (52,07%)
- Rialzo molto forte: **214,30 $** (113,79%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Solana tendeva a muoversi tra una zona bassa intorno a **87,62 $** e uno spike normale intorno a **126,04 $**.

La chiusura a 30 giorni era più spesso positiva: salita 67,50%, discesa 32,50%. Quindi la lettura principale è favorevole.

---

# Dogecoin — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟡 GIALLO / Incerto
**Prezzo attuale:** 0,08 $

**Direzione più probabile a 30 giorni:** **DISCESA**
- Probabilità storica di salita: **27,50%**
- Probabilità storica di discesa: **72,50%**
- Quanto è netto il segnale: **forte**

## Come leggere questa parte

- **Probabilità storica di salita** = su 40 casi simili, quanti hanno chiuso sopra dopo 30 giorni.
- **Probabilità storica di discesa** = su 40 casi simili, quanti hanno chiuso sotto dopo 30 giorni.
- **Quanto è netto il segnale** = quanto è grande la differenza tra salita e discesa. Non vuol dire certezza, vuol dire solo che il risultato storico non è vicino al 50/50.

La lettura principale è ribassista, con segnale forte. Nei casi storici simili, il prezzo ha chiuso sotto dopo 30 giorni più spesso di quanto abbia chiuso sopra.

## 1. Return 30d — prezzo fra 30 giorni

**Return** significa rendimento finale. Qui guardiamo dove potrebbe stare il prezzo **alla fine dei 30 giorni**, non durante il percorso.

- Se va molto male: **0,06 $** (-26,82%)
- Se va male: **0,07 $** (-18,51%)
- Scenario normale: **0,08 $** (-7,54%)
- Se va bene: **0,08 $** (2,27%)
- Se va molto bene: **0,12 $** (42,82%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **0,07 $** (-10,59%)
- Discesa brutta: **0,06 $** (-23,00%)
- Discesa molto brutta: **0,06 $** (-29,86%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **0,10 $** (17,43%)
- Rialzo buono: **0,11 $** (33,17%)
- Rialzo molto forte: **0,13 $** (58,40%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Dogecoin tendeva a muoversi tra una zona bassa intorno a **0,07 $** e uno spike normale intorno a **0,10 $**.

La chiusura a 30 giorni era più spesso negativa: salita 27,50%, discesa 72,50%. Quindi la lettura principale è prudente/debole.

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

- Grezzo: **7,19%** → **83.250,64 $**
- Correzione imparata dagli errori: **2,01%**
- Calibrato: **9,20%** → **84.810,13 $**
- Lettura: Lo scanner è stato troppo pessimista sul prezzo finale.

### Drawdown 30d — rischio di discesa durante il mese

- Grezzo: **-12,92%** → **67.636,28 $**
- Correzione imparata dagli errori: **4,72%**
- Calibrato: **-8,19%** → **71.304,73 $**
- Lettura: Lo scanner è stato troppo prudente: nella realtà il prezzo è sceso meno del previsto.

### Max gain 30d — rialzo/spike durante il mese

- Grezzo: **15,48%** → **89.689,52 $**
- Correzione imparata dagli errori: **-2,82%**
- Calibrato: **12,65%** → **87.495,49 $**
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

- Grezzo: **6,71%** → **106,97 $**
- Correzione imparata dagli errori: **8,80%**
- Calibrato: **15,51%** → **115,79 $**
- Lettura: Lo scanner è stato troppo pessimista sul prezzo finale.

### Drawdown 30d — rischio di discesa durante il mese

- Grezzo: **-12,59%** → **87,62 $**
- Correzione imparata dagli errori: **2,99%**
- Calibrato: **-9,60%** → **90,61 $**
- Lettura: Lo scanner è stato troppo prudente: nella realtà il prezzo è sceso meno del previsto.

### Max gain 30d — rialzo/spike durante il mese

- Grezzo: **25,74%** → **126,04 $**
- Correzione imparata dagli errori: **4,02%**
- Calibrato: **29,76%** → **130,07 $**
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

- Grezzo: **-7,54%** → **0,08 $**
- Correzione imparata dagli errori: **15,19%**
- Calibrato: **7,64%** → **0,09 $**
- Lettura: Lo scanner è stato troppo pessimista sul prezzo finale.

### Drawdown 30d — rischio di discesa durante il mese

- Grezzo: **-10,59%** → **0,07 $**
- Correzione imparata dagli errori: **15,34%**
- Calibrato: **4,75%** → **0,09 $**
- Lettura: Lo scanner è stato troppo prudente: nella realtà il prezzo è sceso meno del previsto.

### Max gain 30d — rialzo/spike durante il mese

- Grezzo: **17,43%** → **0,10 $**
- Correzione imparata dagli errori: **2,52%**
- Calibrato: **19,95%** → **0,10 $**
- Lettura: Lo scanner ha sottostimato gli spike: nella realtà il prezzo è salito più del previsto.

### Come leggerlo

La parte grezza ti dice cosa mostrano i vecchi pattern storici. La parte calibrata ti dice come cambia quella lettura dopo aver visto se lo scanner, nel mercato reale, è stato troppo ottimista o troppo pessimista.

---

# Approfondimento tecnico — Bitcoin (BTC-USD)

## Semaforo: 🟢 VERDE / Favorevole

**Prezzo attuale:** 77.666,99 $

Bitcoin ha un segnale favorevole. La statistica dei casi simili indica più possibilità di salita che di discesa, ma resta comunque una probabilità, non una certezza.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **72,50%**
- Casi negativi dopo 30 giorni: **27,50%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **82,74%**
- Rendimento medio dopo 30 giorni: **7,42%**
- Rendimento centrale dopo 30 giorni: **7,19%**
- Discesa media durante i 30 giorni: **-16,62%**
- Massimo rialzo medio durante i 30 giorni: **23,90%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **83.430,67 $**
- Scenario centrale a 30 giorni: **83.250,64 $**
- Zona di rischio media: **64.759,73 $**
- Zona di rialzo media: **96.227,64 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -32,48% → **52.437,95 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -5,37% → **73.497,02 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: 7,19% → **83.250,64 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 20,28% → **93.419,12 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 39,29% → **108.183,33 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -33,71% → **51.482,01 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -19,28% → **62.694,50 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -12,92% → **67.636,28 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -7,91% → **71.522,87 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: -3,53% → **74.926,49 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 1,71% → **78.991,42 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 8,33% → **84.138,62 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 15,48% → **89.689,52 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 26,12% → **97.954,82 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 52,57% → **118.498,18 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| XRP-USD         | 2023-08-09   | 2023-11-16 |        86.55 |         1.25 |          -5.18 |           9.96 |
| THETA-USD       | 2023-08-08   | 2023-11-15 |        86.1  |         8.57 |         -10.03 |          20.88 |
| 1INCH-USD       | 2023-08-06   | 2023-11-13 |        85.77 |         4.53 |          -9.19 |          14.73 |
| THETA-USD       | 2018-11-12   | 2019-02-19 |        85.4  |        29.98 |          -3.49 |         102.52 |
| BNB-USD         | 2018-11-13   | 2019-02-20 |        85.02 |        39.22 |         -13.17 |          46.99 |
| MATIC-USD       | 2023-08-09   | 2023-11-16 |        84.69 |         0.4  |         -13.46 |           8.92 |
| XTZ-USD         | 2023-08-09   | 2023-11-16 |        84.57 |        12.21 |          -8.26 |          16.47 |
| FIL-USD         | 2023-08-08   | 2023-11-15 |        84.5  |        -8.23 |         -19.2  |           0    |
| SAND-USD        | 2023-08-08   | 2023-11-15 |        84.47 |        12.26 |         -16.7  |          25.52 |
| ZIL-USD         | 2023-08-06   | 2023-11-13 |        84.42 |         9.27 |         -10.04 |          13.63 |

---

# Approfondimento tecnico — Solana (SOL-USD)

## Semaforo: 🟢 VERDE / Favorevole

**Prezzo attuale:** 100,24 $

Solana ha un segnale favorevole. La statistica dei casi simili indica più possibilità di salita che di discesa, ma resta comunque una probabilità, non una certezza.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **67,50%**
- Casi negativi dopo 30 giorni: **32,50%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **80,33%**
- Rendimento medio dopo 30 giorni: **46,78%**
- Rendimento centrale dopo 30 giorni: **6,71%**
- Discesa media durante i 30 giorni: **-16,68%**
- Massimo rialzo medio durante i 30 giorni: **67,92%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **147,13 $**
- Scenario centrale a 30 giorni: **106,97 $**
- Zona di rischio media: **83,52 $**
- Zona di rialzo media: **168,32 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -30,40% → **69,77 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -7,46% → **92,76 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: 6,71% → **106,97 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 41,41% → **141,75 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 102,20% → **202,68 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -38,27% → **61,88 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -20,82% → **79,37 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -12,59% → **87,62 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -6,83% → **93,39 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: -0,52% → **99,72 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 0,61% → **100,85 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 10,47% → **110,73 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 25,74% → **126,04 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 52,07% → **152,44 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 113,79% → **214,30 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| ZIL-USD         | 2020-08-26   | 2020-12-03 |        86.44 |       116.9  |         -11.64 |         166.95 |
| VET-USD         | 2020-03-04   | 2020-06-11 |        85.38 |       109.07 |          -6.61 |         125.67 |
| VET-USD         | 2023-08-06   | 2023-11-13 |        85.38 |        45.73 |          -9.21 |          45.73 |
| BNB-USD         | 2018-11-13   | 2019-02-20 |        83.43 |        39.22 |         -13.17 |          46.99 |
| THETA-USD       | 2023-08-08   | 2023-11-15 |        82.95 |         8.57 |         -10.03 |          20.88 |
| NEO-USD         | 2023-08-04   | 2023-11-11 |        82.17 |        -8.87 |         -21.33 |           0.65 |
| RUNE-USD        | 2026-01-31   | 2026-05-10 |        81.7  |       -36.07 |         -47.56 |           2.93 |
| 1INCH-USD       | 2023-08-06   | 2023-11-13 |        81.68 |         4.53 |          -9.19 |          14.73 |
| XRP-USD         | 2020-08-24   | 2020-12-01 |        81.61 |       -64.13 |         -65.44 |           3.03 |
| HBAR-USD        | 2024-08-20   | 2024-11-27 |        81.57 |        94.37 |           0    |         158.91 |

---

# Approfondimento tecnico — Dogecoin (DOGE-USD)

## Semaforo: 🟡 GIALLO / Incerto

**Prezzo attuale:** 0,08 $

Dogecoin è in una situazione incerta. Lo scanner non vede un vantaggio chiaro né per la salita né per la discesa. In questi casi è meglio non forzare la previsione.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **27,50%**
- Casi negativi dopo 30 giorni: **72,50%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **82,30%**
- Rendimento medio dopo 30 giorni: **5,06%**
- Rendimento centrale dopo 30 giorni: **-7,54%**
- Discesa media durante i 30 giorni: **-14,02%**
- Massimo rialzo medio durante i 30 giorni: **31,23%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **0,09 $**
- Scenario centrale a 30 giorni: **0,08 $**
- Zona di rischio media: **0,07 $**
- Zona di rialzo media: **0,11 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -26,82% → **0,06 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -18,51% → **0,07 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: -7,54% → **0,08 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 2,27% → **0,08 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 42,82% → **0,12 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -29,86% → **0,06 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -23,00% → **0,06 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -10,59% → **0,07 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -4,75% → **0,08 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: 0,00% → **0,08 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 0,23% → **0,08 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 4,80% → **0,09 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 17,43% → **0,10 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 33,17% → **0,11 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 58,40% → **0,13 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| MANA-USD        | 2025-01-25   | 2025-05-04 |        86.51 |        -2.82 |          -6.91 |          32.03 |
| FIL-USD         | 2022-05-05   | 2022-08-12 |        85.28 |       -26.85 |         -35.95 |           0    |
| YFI-USD         | 2022-04-30   | 2022-08-07 |        84.49 |       -24.38 |         -25.9  |           0.85 |
| QTUM-USD        | 2021-05-11   | 2021-08-18 |        84.23 |        -3.67 |          -8.92 |          24.24 |
| INJ-USD         | 2021-05-13   | 2021-08-20 |        83.83 |         1.61 |          -0.81 |          44.17 |
| IOTA-USD        | 2025-01-26   | 2025-05-05 |        83.63 |       -10.71 |         -12.59 |          25.96 |
| SAND-USD        | 2025-01-24   | 2025-05-03 |        83.6  |        -0.55 |          -4.85 |          30.08 |
| BAT-USD         | 2021-05-11   | 2021-08-18 |        83.25 |         4.22 |           0    |          36.57 |
| QTUM-USD        | 2019-07-31   | 2019-11-07 |        83.25 |       -20.6  |         -26.68 |           4.86 |
| BTC-USD         | 2025-01-27   | 2025-05-06 |        83.01 |         4.93 |           0    |          15.36 |

</details>
<!-- COMPACT_SECTION_END:scanner_full_detail -->

<!-- COMPACT_SECTION_START:market_regime -->
<details>
<summary><strong>🌦️ Market Regime Match</strong></summary>

<!-- MARKET_REGIME_MATCH_START -->
# Market Regime Match Report


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [market_regime_match_report.md](market_regime_match_report.md)

Generated: 2026-09-02 05:31 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | snapshot_date   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | 2026-09-02 | RECOVERY | 77.667 $ | True | 21.73% | -7.16% | RECOVERY | 21.73% | -7.16% |
| DOGE-USD | 2026-09-02 | BEAR | 0.08188 $ | False | -7.35% | -13.93% | RECOVERY | 21.73% | -7.16% |
| SOL-USD | 2026-09-02 | RECOVERY | 100,24 $ | True | 45.87% | -12.35% | RECOVERY | 21.73% | -7.16% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 72.50% | 7.19% | 20.28% | 39.29% | -12.92% | -33.71% | 15.48% | 26.12% | 52.57% | 67.50% | 11.04% | 36.38% | 90.22% |
| BTC-USD | SAME_BTC_REGIME | 4 | 75.00% | 33.98% | 38.29% | 38.85% | -8.33% | -27.50% | 43.89% | 60.87% | 85.86% | 75.00% | 60.81% | 95.28% | 110.49% |
| BTC-USD | SAME_ASSET_REGIME | 2 | 100.00% | 16.58% | 23.28% | 27.30% | -9.13% | -13.64% | 56.76% | 79.64% | 93.37% | 100.00% | 21.63% | 28.21% | 32.15% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 1 | 100.00% | 29.98% | 29.98% | 29.98% | -3.49% | -3.49% | 102.52% | 102.52% | 102.52% | 100.00% | 34.79% | 34.79% | 34.79% |
| DOGE-USD | ALL_MATCHES | 40 | 27.50% | -7.54% | 2.27% | 42.82% | -10.59% | -29.86% | 17.43% | 33.17% | 58.40% | 32.50% | -8.75% | 21.50% | 84.06% |
| DOGE-USD | SAME_BTC_REGIME | 1 | 0.00% | -16.46% | -16.46% | -16.46% | -18.64% | -18.64% | 9.17% | 9.17% | 9.17% | 0.00% | -21.13% | -21.13% | -21.13% |
| DOGE-USD | SAME_ASSET_REGIME | 13 | 15.38% | -9.86% | -1.50% | 26.38% | -14.09% | -28.03% | 9.17% | 16.98% | 41.55% | 23.08% | -23.01% | -10.39% | 36.91% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 1 | 0.00% | -16.46% | -16.46% | -16.46% | -18.64% | -18.64% | 9.17% | 9.17% | 9.17% | 0.00% | -21.13% | -21.13% | -21.13% |
| SOL-USD | ALL_MATCHES | 40 | 67.50% | 6.71% | 41.41% | 102.20% | -12.59% | -38.27% | 25.74% | 52.07% | 113.79% | 67.50% | 23.69% | 74.76% | 133.42% |
| SOL-USD | SAME_BTC_REGIME | 3 | 100.00% | 39.22% | 74.14% | 95.10% | -13.17% | -19.16% | 46.99% | 86.33% | 109.93% | 100.00% | 120.62% | 131.30% | 137.70% |
| SOL-USD | SAME_ASSET_REGIME | 2 | 100.00% | 19.06% | 27.01% | 31.77% | -17.71% | -20.06% | 22.97% | 28.96% | 32.55% | 100.00% | 39.88% | 55.58% | 65.01% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 1 | 100.00% | 34.95% | 34.95% | 34.95% | -20.65% | -20.65% | 34.95% | 34.95% | 34.95% | 100.00% | 71.29% | 71.29% | 71.29% |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 5 | 20.00% | -24.87% | -33.21% | 27.42% | 40.00% | -22.48% | 29.58% |
| BTC-USD | HISTORICAL_BTC_BULL | 30 | 80.00% | 7.19% | -12.62% | 22.72% | 70.00% | 10.73% | 51.59% |
| BTC-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 100.00% | 18.48% | -2.96% | 24.83% | 100.00% | 151.30% | 193.70% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 4 | 75.00% | 33.98% | -8.33% | 60.87% | 75.00% | 60.81% | 115.06% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 11 | 18.18% | -9.86% | -14.09% | 17.88% | 18.18% | -28.14% | 24.76% |
| DOGE-USD | HISTORICAL_BTC_BULL | 26 | 34.62% | -3.87% | -8.30% | 41.13% | 42.31% | -3.88% | 43.99% |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION | 2 | 0.00% | -25.91% | -33.22% | 8.86% | 0.00% | -12.46% | 8.86% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 1 | 0.00% | -16.46% | -18.64% | 9.17% | 0.00% | -21.13% | 9.17% |
| SOL-USD | HISTORICAL_BTC_BEAR | 15 | 53.33% | 0.86% | -12.94% | 43.25% | 60.00% | 5.36% | 69.65% |
| SOL-USD | HISTORICAL_BTC_BULL | 20 | 80.00% | 9.75% | -10.83% | 61.29% | 75.00% | 31.38% | 120.23% |
| SOL-USD | HISTORICAL_BTC_DISTRIBUTION | 2 | 0.00% | -27.96% | -32.00% | 18.27% | 0.00% | -31.96% | 18.27% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 3 | 100.00% | 39.22% | -13.17% | 86.33% | 100.00% | 120.62% | 137.23% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 28 | 75.00% | 7.19% | -13.19% | 30.76% | 64.29% | 10.73% | 54.93% |
| BTC-USD | HISTORICAL_ASSET_BULL | 7 | 71.43% | 10.93% | -12.56% | 21.74% | 71.43% | 28.07% | 119.17% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 100.00% | 18.48% | -2.96% | 24.83% | 100.00% | 151.30% | 193.70% |
| BTC-USD | HISTORICAL_ASSET_MIXED | 2 | 0.00% | -20.22% | -25.68% | 4.94% | 50.00% | 5.98% | 33.05% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 2 | 100.00% | 16.58% | -9.13% | 79.64% | 100.00% | 21.63% | 85.12% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 13 | 15.38% | -9.86% | -14.09% | 16.98% | 23.08% | -23.01% | 30.74% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 25 | 32.00% | -5.12% | -8.92% | 36.57% | 36.00% | -3.99% | 43.45% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 100.00% | 125.28% | 0.00% | 128.29% | 100.00% | 81.09% | 149.46% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 1 | 0.00% | -8.06% | -15.42% | 6.21% | 0.00% | -5.35% | 14.02% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 29 | 62.07% | 2.91% | -12.19% | 46.99% | 62.07% | 11.31% | 68.64% |
| SOL-USD | HISTORICAL_ASSET_BULL | 7 | 71.43% | 16.29% | -12.56% | 139.71% | 71.43% | 85.18% | 155.24% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 100.00% | 105.25% | -12.68% | 119.61% | 100.00% | 130.65% | 217.10% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 2 | 100.00% | 19.06% | -17.71% | 28.96% | 100.00% | 39.88% | 61.69% |

## Top regime-adjusted matches

A single cohort is selected deterministically: SAME_BTC_AND_ASSET_REGIME, otherwise SAME_ASSET_REGIME, otherwise SAME_BTC_REGIME. Each level must have at least 5 matches; cohorts are never combined.

| target   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level        | selection_reason              |
|:---------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:----------------------|:------------------------------|
| BTC-USD | NONE | 1 | 2 | 4 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES |
| DOGE-USD | SAME_ASSET_REGIME | 1 | 13 | 1 | 13 | 5 | 1_SAME_ASSET_FALLBACK | FALLBACK_TO_SAME_ASSET_REGIME |
| SOL-USD | NONE | 1 | 2 | 3 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES |

- WARNING DOGE-USD: SAME_ASSET_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| DOGE-USD | FIL-USD | 2022-05-05 | 85.28% | BEAR | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -26.85% | -35.95% | 0.00% | -41.41% | -41.41% | 0.00% |
| DOGE-USD | YFI-USD | 2022-04-30 | 84.49% | BEAR | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -24.38% | -25.90% | 0.85% | -28.14% | -30.98% | 0.85% |
| DOGE-USD | QTUM-USD | 2022-05-01 | 82.69% | BEAR | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -25.68% | -28.31% | 2.87% | -32.52% | -33.72% | 2.87% |
| DOGE-USD | MATIC-USD | 2022-04-21 | 82.26% | RECOVERY | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -16.46% | -18.64% | 9.17% | -21.13% | -24.98% | 9.17% |
| DOGE-USD | THETA-USD | 2026-01-19 | 82.20% | BEAR | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -11.37% | -11.37% | 18.77% | -37.22% | -37.22% | 18.77% |
| DOGE-USD | ETH-USD | 2025-02-09 | 82.12% | BULL | BEAR | SAME_ASSET_ONLY | MIXED | -0.19% | -4.46% | 11.24% | 40.32% | -11.90% | 40.32% |
| DOGE-USD | EGLD-USD | 2023-07-25 | 82.04% | BULL | BEAR | SAME_ASSET_ONLY | EXPLOSIVE_60D | 40.51% | 0.00% | 48.58% | 110.79% | 0.00% | 126.47% |
| DOGE-USD | INJ-USD | 2022-05-13 | 81.80% | BEAR | BEAR | SAME_ASSET_ONLY | MIXED | -1.50% | -9.36% | 16.40% | 23.27% | -9.36% | 30.74% |
| DOGE-USD | EOS-USD | 2022-05-01 | 81.34% | BEAR | BEAR | SAME_ASSET_ONLY | BULLISH_30D | 33.02% | -5.84% | 47.24% | -10.39% | -10.39% | 47.24% |
| DOGE-USD | MANA-USD | 2022-10-18 | 81.05% | BEAR | BEAR | SAME_ASSET_ONLY | MIXED | -3.09% | -6.46% | 16.98% | -14.29% | -24.97% | 16.98% |

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

Generato: 2026-09-02 05:32 UTC


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
| BTC | 77.667 $ | +8 | COSTRUTTIVO / CONFERMA PARZIALE | STAGE 3 / DISTRIBUZIONE O PAUSA | MASSIMI E MINIMI CRESCENTI | SIGN OF STRENGTH POSSIBILE | MEDIO | SPOT OK / LONG SOLO PRUDENTE SU CONFERMA |
| SOL | 100,24 $ | +7 | COSTRUTTIVO / CONFERMA PARZIALE | STAGE 3 / DISTRIBUZIONE O PAUSA | MASSIMI E MINIMI CRESCENTI | SIGN OF STRENGTH POSSIBILE | MEDIO | TRANCHE PICCOLE / NO LEVA FINCHÉ NON ROMPE CONFERME |
| DOGE | 0.08188 $ | +1 | NEUTRALE / MISTO | STAGE 4 / MARKDOWN | MASSIMI E MINIMI CRESCENTI | ACCUMULO POSSIBILE / RANGE BASSO | MEDIO | STAI ALLA FINESTRA |

## Punteggi per area

| Asset | Trend | Struttura | Momentum | Volume | Prezzo | Candela | Wyckoff | Totale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +1 | +2 | 0 | +2 | 0 | +1 | +2 | +8 |
| SOL | +1 | +2 | 0 | +2 | 0 | 0 | +2 | +7 |
| DOGE | -2 | +2 | -2 | +2 | 0 | +1 | 0 | +1 |

## Livelli tecnici

| Asset | Supporto | Resistenza | Breakout 60g | Breakdown 60g | ATR14 | Rendimento 30g | Rendimento 90g |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 76.909 $ | 77.991 $ | 81.347 $ | 57.748 $ | 3,99% | 22,33% | 21,31% |
| SOL | 83,52 $ | 110,04 $ | 110,04 $ | 70,51 $ | 6,38% | 36,44% | 39,93% |
| DOGE | 0.07809 $ | 0.08494 $ | 0.09998 $ | 0.06797 $ | 7,30% | 15,85% | -10,37% |

## Lettura dettagliata

### BTC

- Prezzo: **77.667 $**
- Score classico: **+8 / 12**
- Verdetto: **COSTRUTTIVO / CONFERMA PARZIALE**
- Azione coerente: **SPOT OK / LONG SOLO PRUDENTE SU CONFERMA**
- Volatilità tecnica locale: **MEDIO** — ATR14 3,99%; distanza supporto 0,97%; distanza resistenza 0,43%

Dettaglio:

- Trend: **+1** — prezzo sopra MA200 daily; breve termine sopra MA20/MA50; MA50 daily in salita; MA200 daily in discesa; STAGE 3 / DISTRIBUZIONE O PAUSA
- Stage weekly: **STAGE 3 / DISTRIBUZIONE O PAUSA** — Prezzo sopra MA30 weekly ma pendenza debole o piatta.
- Struttura: **+2** — MASSIMI E MINIMI CRESCENTI
- Momentum: **0** — RSI sano 66.7; RSI in peggioramento; MACD sopra signal; istogramma MACD in peggioramento
- Volume: **+2** — OBV sopra media; CMF positivo 0.32; volume ratio 0.95
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **+1** — Hammer / rejection basso
- Wyckoff: **+2** — SIGN OF STRENGTH POSSIBILE. Prezzo nella parte alta del range con flusso volume positivo.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 66.74 |
| MACD histogram | 103.19209 |
| CMF20 | 0.318 |
| Volume ratio 20 | 0.95 |
| MA20 | 73.182 $ |
| MA50 | 67.886 $ |
| MA100 | 66.233 $ |
| MA200 | 69.469 $ |
| Pendenza MA50 20g | +7,18% |
| Pendenza MA200 60g | -7,31% |
| Bollinger width | 35,43% |
| Bollinger position | 0.66 |

### SOL

- Prezzo: **100,24 $**
- Score classico: **+7 / 12**
- Verdetto: **COSTRUTTIVO / CONFERMA PARZIALE**
- Azione coerente: **TRANCHE PICCOLE / NO LEVA FINCHÉ NON ROMPE CONFERME**
- Volatilità tecnica locale: **MEDIO** — ATR14 6,38%; distanza supporto 19,99%; distanza resistenza 9,81%

Dettaglio:

- Trend: **+1** — prezzo sopra MA200 daily; breve termine sopra MA20/MA50; MA50 daily in salita; MA200 daily in discesa; STAGE 3 / DISTRIBUZIONE O PAUSA
- Stage weekly: **STAGE 3 / DISTRIBUZIONE O PAUSA** — Prezzo sopra MA30 weekly ma pendenza debole o piatta.
- Struttura: **+2** — MASSIMI E MINIMI CRESCENTI
- Momentum: **0** — RSI sano 63.8; RSI in peggioramento; MACD sopra signal; istogramma MACD in peggioramento
- Volume: **+2** — OBV sopra media; CMF positivo 0.27; volume ratio 0.88
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **+2** — SIGN OF STRENGTH POSSIBILE. Prezzo nella parte alta del range con flusso volume positivo.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 63.75 |
| MACD histogram | 0.60658 |
| CMF20 | 0.268 |
| Volume ratio 20 | 0.88 |
| MA20 | 91,59 $ |
| MA50 | 81,69 $ |
| MA100 | 77,92 $ |
| MA200 | 82,00 $ |
| Pendenza MA50 20g | +8,09% |
| Pendenza MA200 60g | -12,57% |
| Bollinger width | 48,07% |
| Bollinger position | 0.68 |

### DOGE

- Prezzo: **0.08188 $**
- Score classico: **+1 / 12**
- Verdetto: **NEUTRALE / MISTO**
- Azione coerente: **STAI ALLA FINESTRA**
- Volatilità tecnica locale: **MEDIO** — ATR14 7,30%; distanza supporto 4,85%; distanza resistenza 3,74%

Dettaglio:

- Trend: **-2** — prezzo sotto MA200 daily; breve termine sopra MA20/MA50; MA50 daily in salita; MA200 daily in discesa; STAGE 4 / MARKDOWN
- Stage weekly: **STAGE 4 / MARKDOWN** — Prezzo sotto MA30 weekly con MA30 in discesa.
- Struttura: **+2** — MASSIMI E MINIMI CRESCENTI
- Momentum: **-2** — RSI sano 53.0; RSI in peggioramento; MACD sotto signal; istogramma MACD in peggioramento
- Volume: **+2** — OBV sopra media; CMF positivo 0.11; volume ratio 0.75
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **+1** — Hammer / rejection basso
- Wyckoff: **0** — ACCUMULO POSSIBILE / RANGE BASSO. Prezzo nella metà bassa del range, ma senza spring confermato.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 52.98 |
| MACD histogram | -0.00055 |
| CMF20 | 0.110 |
| Volume ratio 20 | 0.75 |
| MA20 | 0.08109 $ |
| MA50 | 0.07505 $ |
| MA100 | 0.07922 $ |
| MA200 | 0.08883 $ |
| Pendenza MA50 20g | +3,75% |
| Pendenza MA200 60g | -14,15% |
| Bollinger width | 42,11% |
| Bollinger position | 0.52 |

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

Generato: 2026-09-02 05:32 UTC


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
| BTC | 77.667 $ | Doppio massimo | CANDIDATO | ribassista | n/a | 49.952 $ | n/a | 34,49% | Fib 23,6% TENUTO (0) @ 75.778 $ | NEL RANGE | 74.959 $ |
| SOL | 100,24 $ | Doppio massimo | CANDIDATO | ribassista | n/a | 62,51 $ | n/a | 41,79% | Fib 23,6% TENUTO (0) @ 98,33 $ | NEL RANGE | 83,52 $ |
| DOGE | 0.08188 $ | Doppio massimo | CANDIDATO | ribassista | n/a | 0.06214 $ | n/a | 20,46% | Fib 61,8% TENUTO (+1) @ 0.08020 $ | NEL RANGE | 0.08157 $ |

## BTC

![Classic visual BTC](classic_visual_BTC.png)

- Pattern principale: **Doppio massimo**
- Stato pattern: **CANDIDATO** (0)
- Famiglia: **ribassista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-06-22 -> 2026-08-09**
- Età formazione: **24 giorni**
- Breakout pattern: **n/a**
- Età breakout: **n/a**
- Neckline: **57.748 $**
- Target teorico: **49.952 $**
- Progresso verso target: **n/a**
- Distanza dalla neckline: **34,49%**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 23,6% TENUTO (0) @ 75.778 $** — Swing UP 2026-07-01 57.748 -> 2026-08-28 81.347; livello più vicino 23.6% a 75.778; stato TENUTO; confluenza: nessuna confluenza indipendente.
- Invalidazione: **58.903 $**
- Relazione prezzo/neckline: **sopra neckline**
- Dettaglio: Due massimi simili vicino a 65.544 tra 2026-06-22 e 2026-08-09. Neckline ribassista stimata: 57.748. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 24 giorni. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Hammer / rejection basso**
- Stato prezzo: **NEL RANGE**
- Supporto: **74.959 $**
- Resistenza: **77.991 $**
- Breakout 60g: **81.347 $**
- Breakdown 60g: **57.748 $**
- RSI14: **66.78**
- ATR14: **3,98%**
- Volume ratio 20g: **0.95**
- Rendimento 30g: **+22,34%**
- Rendimento 90g: **+21,33%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Doppio massimo | CANDIDATO | 0 | ribassista | 57.748 $ | n/a | n/a | 32.703 $ | n/a | 34,49% | 58.903 $ | Due massimi simili a 82.792 $ e 81.347 $. Neckline circa 57.748 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 5 giorni. |
| Doppio minimo | TARGET RAGGIUNTO | 0 | rialzista | 65.402 $ | 2026-08-19 | 14g | 68.577 $ | 386,29% | n/a | 64.094 $ | Due minimi simili a 62.227 $ e 62.488 $. Neckline circa 65.402 $. Breakout neckline: 2026-08-19 (14 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 68.577 $; progresso: 386,29%; prezzo sopra neckline. |

## SOL

![Classic visual SOL](classic_visual_SOL.png)

- Pattern principale: **Doppio massimo**
- Stato pattern: **CANDIDATO** (0)
- Famiglia: **ribassista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-07-15 -> 2026-08-09**
- Età formazione: **24 giorni**
- Breakout pattern: **n/a**
- Età breakout: **n/a**
- Neckline: **70,69 $**
- Target teorico: **62,51 $**
- Progresso verso target: **n/a**
- Distanza dalla neckline: **41,79%**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 23,6% TENUTO (0) @ 98,33 $** — Swing UP 2026-06-06 60,41 -> 2026-08-27 110,04; livello più vicino 23.6% a 98,33; stato TENUTO; confluenza: nessuna confluenza indipendente.
- Invalidazione: **72,11 $**
- Relazione prezzo/neckline: **sopra neckline**
- Dettaglio: Due massimi simili vicino a 78,88 tra 2026-07-15 e 2026-08-09. Neckline ribassista stimata: 70,69. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 24 giorni. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **NEL RANGE**
- Supporto: **83,52 $**
- Resistenza: **110,04 $**
- Breakout 60g: **110,04 $**
- Breakdown 60g: **70,51 $**
- RSI14: **63.81**
- ATR14: **6,37%**
- Volume ratio 20g: **0.88**
- Rendimento 30g: **+36,48%**
- Rendimento 90g: **+39,98%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Doppio massimo | CANDIDATO | 0 | ribassista | 70,69 $ | n/a | n/a | 62,66 $ | n/a | 41,79% | 72,11 $ | Due massimi simili a 78,73 $ e 77,62 $. Neckline circa 70,69 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 24 giorni. |
| Testa e spalle inverso | TARGET RAGGIUNTO | 0 | rialzista | 78,17 $ | 2026-08-19 | 14g | 85,65 $ | 295,14% | n/a | 76,61 $ | Spalla sinistra 73,40 $, testa 70,69 $, spalla destra 74,20 $. Neckline circa 78,17 $. Breakout neckline: 2026-08-19 (14 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 85,65 $; progresso: 295,14%; prezzo sopra neckline. |
| Doppio minimo | TARGET RAGGIUNTO | 0 | rialzista | 78,73 $ | 2026-08-19 | 14g | 84,05 $ | 404,08% | n/a | 77,15 $ | Due minimi simili a 73,40 $ e 74,20 $. Neckline circa 78,73 $. Breakout neckline: 2026-08-19 (14 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 84,05 $; progresso: 404,08%; prezzo sopra neckline. |

## DOGE

![Classic visual DOGE](classic_visual_DOGE.png)

- Pattern principale: **Doppio massimo**
- Stato pattern: **CANDIDATO** (0)
- Famiglia: **ribassista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-07-26 -> 2026-08-11**
- Età formazione: **22 giorni**
- Breakout pattern: **n/a**
- Età breakout: **n/a**
- Neckline: **0.06797 $**
- Target teorico: **0.06214 $**
- Progresso verso target: **n/a**
- Distanza dalla neckline: **20,46%**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 61,8% TENUTO (+1) @ 0.08020 $** — Swing UP 2026-08-01 0.06797 -> 2026-08-22 0.09998; livello più vicino 61.8% a 0.08020; stato TENUTO; confluenza: neckline rialzista, invalidazione rialzista.
- Invalidazione: **0.06933 $**
- Relazione prezzo/neckline: **sopra neckline**
- Dettaglio: Due massimi simili vicino a 0.07380 tra 2026-07-26 e 2026-08-11. Neckline ribassista stimata: 0.06797. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 22 giorni. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Hammer / rejection basso**
- Stato prezzo: **NEL RANGE**
- Supporto: **0.08157 $**
- Resistenza: **0.09169 $**
- Breakout 60g: **0.09998 $**
- Breakdown 60g: **0.06797 $**
- RSI14: **52.98**
- ATR14: **7,30%**
- Volume ratio 20g: **0.75**
- Rendimento 30g: **+15,85%**
- Rendimento 90g: **-10,37%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Doppio massimo | CANDIDATO | 0 | ribassista | 0.06797 $ | n/a | n/a | 0.06214 $ | n/a | 20,46% | 0.06933 $ | Due massimi simili a 0.07380 $ e 0.07286 $. Neckline circa 0.06797 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 22 giorni. |
| Doppio minimo | TARGET RAGGIUNTO | 0 | rialzista | 0.07923 $ | 2026-08-20 | 13g | 0.08952 $ | 25,73% | n/a | 0.07765 $ | Due minimi simili a 0.06961 $ e 0.06895 $. Neckline circa 0.07923 $. Breakout neckline: 2026-08-20 (13 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 0.08952 $; progresso: 25,73%; prezzo sopra neckline. |

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

Generato: 2026-09-02 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [fractal_path_tracker.md](fractal_path_tracker.md)

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-09-02**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-02-17**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **100,24 $**
- Verdetto principale: **ANALOGIA DEBOLE / SCENARIO SECONDARIO**
- Somiglianza strutturale: **+65,97%**
- Aderenza live principale: **+70,75%**
- Errore medio live principale: **14,63%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE SOLO DI CONTESTO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **88**
- Osservazioni inclusive dal bottom: **89**
- Osservazioni da inizio programma/scanner: **62**
- Errore assoluto medio dal bottom: **12,02%**
- Errore assoluto medio da inizio programma: **14,63%**
- Gap firmato medio ultimi 7 giorni: **+15,61%**
- Errore assoluto medio ultimi 7 giorni: **15,61%**
- Gap ultimo giorno: **+3,59%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **+3,59%**
- Gap firmato medio 7g: **+15,61%**
- Errore assoluto medio 7g: **15,61%**
- Variazione recente gap: **-12,80%**
- Stato gap: **VICINO AL FRATTALE**
- Trend gap: **SOL resta sopra il percorso ancorato, ma sta riducendo il distacco**

Soglie operative del grafico:

- entro **±5%**: percorso vicino;
- tra **±5% e ±12%**: deviazione gestibile;
- oltre **±12%**: frattale non abbastanza aderente per conferma operativa;
- oltre **±18%**: disallineamento marcato.

## Ultimi giorni del confronto ancorato

|   Giorno | Data SOL   | Data BTC eq.   | SOL reale   | Percorso ancorato   | Gap firmato   | Fase                |
|---------:|:-----------|:---------------|:------------|:--------------------|:--------------|:--------------------|
| 79 | 2026-08-24 | 2023-02-08 | 98,56 $ | 90,36 $ | +9,07% | da inizio programma |
| 80 | 2026-08-25 | 2023-02-09 | 96,60 $ | 85,95 $ | +12,39% | da inizio programma |
| 81 | 2026-08-26 | 2023-02-10 | 102,17 $ | 85,29 $ | +19,79% | da inizio programma |
| 82 | 2026-08-27 | 2023-02-11 | 109,21 $ | 86,15 $ | +26,76% | da inizio programma |
| 83 | 2026-08-28 | 2023-02-12 | 104,13 $ | 85,83 $ | +21,32% | da inizio programma |
| 84 | 2026-08-29 | 2023-02-13 | 105,65 $ | 85,91 $ | +22,98% | da inizio programma |
| 85 | 2026-08-30 | 2023-02-14 | 101,88 $ | 87,53 $ | +16,39% | da inizio programma |
| 86 | 2026-08-31 | 2023-02-15 | 103,00 $ | 95,75 $ | +7,56% | da inizio programma |
| 87 | 2026-09-01 | 2023-02-16 | 103,00 $ | 93,06 $ | +10,68% | da inizio programma |
| 88 | 2026-09-02 | 2023-02-17 | 100,24 $ | 96,77 $ | +3,59% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-09-09 | 91,38 $ | 94,66 $ | 94,66 $ / 101,32 $ | no | n/a | n/a | n/a |
| 14g | 2026-09-16 | 88,09 $ | 91,25 $ | 91,25 $ / 101,32 $ | no | n/a | n/a | n/a |
| 21g | 2026-09-23 | 79,52 $ | 82,37 $ | 82,37 $ / 101,32 $ | no | n/a | n/a | n/a |
| 28g | 2026-09-30 | 108,03 $ | 111,90 $ | 82,37 $ / 111,90 $ | no | n/a | n/a | n/a |
| 35g | 2026-10-07 | 108,30 $ | 112,19 $ | 82,37 $ / 115,62 $ | no | n/a | n/a | n/a |
| 42g | 2026-10-14 | 112,18 $ | 116,21 $ | 82,37 $ / 116,21 $ | no | n/a | n/a | n/a |
| 49g | 2026-10-21 | 110,01 $ | 113,95 $ | 82,37 $ / 116,21 $ | no | n/a | n/a | n/a |
| 56g | 2026-10-28 | 120,09 $ | 124,40 $ | 82,37 $ / 124,40 $ | no | n/a | n/a | n/a |
| 63g | 2026-11-04 | 107,45 $ | 111,30 $ | 82,37 $ / 124,40 $ | no | n/a | n/a | n/a |
| 70g | 2026-11-11 | 115,58 $ | 119,72 $ | 82,37 $ / 124,40 $ | no | n/a | n/a | n/a |
| 77g | 2026-11-18 | 116,34 $ | 120,52 $ | 82,37 $ / 124,40 $ | no | n/a | n/a | n/a |
| 84g | 2026-11-25 | 105,59 $ | 109,38 $ | 82,37 $ / 124,40 $ | no | n/a | n/a | n/a |
| 91g | 2026-12-02 | 105,93 $ | 109,73 $ | 82,37 $ / 124,40 $ | no | n/a | n/a | n/a |
| 98g | 2026-12-09 | 105,25 $ | 109,03 $ | 82,37 $ / 124,40 $ | no | n/a | n/a | n/a |
| 105g | 2026-12-16 | 107,34 $ | 111,19 $ | 82,37 $ / 124,40 $ | no | n/a | n/a | n/a |
| 112g | 2026-12-23 | 104,31 $ | 108,05 $ | 82,37 $ / 124,40 $ | no | n/a | n/a | n/a |
| 119g | 2026-12-30 | 103,71 $ | 107,43 $ | 82,37 $ / 124,40 $ | no | n/a | n/a | n/a |
| 126g | 2027-01-06 | 120,92 $ | 125,25 $ | 82,37 $ / 125,25 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 48 | 37,50% | 11,40% | 13,58% |
| 14g | 41 | 26,83% | 20,24% | 12,29% |
| 21g | 35 | 17,14% | 26,91% | 14,23% |
| 28g | 29 | 37,93% | 24,91% | 14,02% |
| 35g | 22 | 59,09% | 15,66% | 13,24% |
| 42g | 15 | 100,00% | 8,49% | 12,54% |
| 49g | 8 | 100,00% | 6,18% | 13,75% |
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

Ultima lettura salvata: **2026-09-02** — SOL 100,24 $, gap +3,59%, somiglianza +65,97%.

Nel report principale lascio solo il link, così non diventa troppo lungo.

<!-- SOL_BTC_FRACTAL_HISTORY_END -->

</details>
<!-- COMPACT_SECTION_END:fractal_path -->

<!-- COMPACT_SECTION_START:exchange_microstructure -->
<details>
<summary><strong>🏦 Dati exchange, liquidità e leva</strong></summary>

<!-- EXCHANGE_MICROSTRUCTURE_START -->
# Dati exchange, liquidità e leva

Generato: 2026-09-02 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [exchange_microstructure_report.md](exchange_microstructure_report.md)

Questo modulo legge Kraken Futures, Bitget Futures e KuCoin Futures come nucleo derivati. OKX e Coinbase vengono raccolti come fonti ausiliarie non pesate.
Non modifica la formula matematica di RSI, Fibonacci o Wyckoff: controlla se quei segnali sono sostenuti da acquisti, vendite, OI, funding e liquidità.

**Limite importante:** questo nucleo non assume disponibile un feed pubblico completo delle liquidazioni. La componente liquidazioni resta neutrale; le zone future restano stime di pressione, non dati certi delle singole posizioni.

Diagnostica completa: [exchange_source_diagnostics.md](exchange_source_diagnostics.md)

## Sintesi

| Asset | Prezzo | Exchange | Segnale candidato | Peso Global | Bias exchange | Confidenza | Copertura | Funding 8h eq. | OI 24h | Taker flow (campione/4h) | Book 0,5% | Liq long campione | Liq short campione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 77.400 $ | 3 | 0 | 0 | MISTA / NEUTRALE | BASSA | 100% | +0,0085% | +2,54% | 0,94 | -1,43% | 0 $ | 0 $ |
| SOL | 99,75 $ | 3 | 0 | 0 | LEGGERMENTE POSITIVA / NON PESATA | BASSA | 100% | -0,0011% | -2,41% | 1,31 | +3,33% | 0 $ | 0 $ |
| DOGE | 0.08150 $ | 3 | 0 | 0 | LEGGERMENTE POSITIVA / NON PESATA | BASSA | 100% | +0,0092% | -4,77% | 1,07 | -1,60% | 0 $ | 0 $ |

Il segnale candidato è limitato a **±1**, ma il peso nel Global resta **0** finché il tracker a 7 giorni non raggiunge 30 controlli, almeno 55% di accuratezza e return corretto direzione positivo. Un singolo muro o funding non basta.

La colonna taker usa un campione recente nel primo run. Dopo almeno 3 fotografie distribuite su almeno 45 minuti viene sostituita automaticamente dalla media intraday 4h.

## Dati separati per exchange

| Asset | Exchange | Stato | Funding 8h eq. | Open interest | Taker flow | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | Kraken | OK | +0,0082% | 154,37 mln $ | 0,24 | -4,61% |
| BTC | Bitget | OK | +0,0099% | 2,70 mld $ | 0,00 | +7,17% |
| BTC | Kucoin | OK | +0,0063% | 1,54 mld $ | 1,33 | -1,44% |
| SOL | Kraken | OK | -0,0013% | 29,42 mln $ | 0,08 | +1,26% |
| SOL | Bitget | OK | +0,0039% | 441,70 mln $ | 0,08 | +76,72% |
| SOL | Kucoin | OK | -0,0027% | 245,76 mln $ | 0,67 | -18,70% |
| DOGE | Kraken | OK | +0,0183% | 4,27 mln $ | 0,86 | +4,98% |
| DOGE | Bitget | OK | +0,0100% | 103,72 mln $ | 0,01 | -8,93% |
| DOGE | Kucoin | OK | +0,0084% | 104,94 mln $ | 0,34 | +24,92% |

Kraken, Bitget e KuCoin contribuiscono a funding normalizzato, open interest, trade aggressivi e order book. Non viene inventato un long/short ratio pubblico né un feed completo delle liquidazioni.

## Conferme per indicatori tecnici

### BTC

- Score grezzo exchange: **-0,25**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 3, accuratezza +66,67%.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 0, bear 1, divergenze 0.
- Flusso taker/order book: **+0,75**.
- OI/funding/basis: **-1,00**.
- Affollamento long/short: **+0,00**.
- Liquidazioni: **NON PESATE / FEED COMPLETO NON ASSUNTO DISPONIBILE**.
- **Wyckoff:** Fase Wyckoff non abbastanza chiara per una conferma exchange.
- **Fibonacci:** Fibonacci tenuto; nessuna conferma exchange netta.
- **RSI:** RSI in zona non estrema o flusso exchange non abbastanza netto.
- **Pattern:** I pattern candidati restano non operativi: i dati exchange possono solo preparare la conferma.
- **Breakout/breakdown:** Prezzo non abbastanza vicino a un livello chiave o flusso non netto.
- **Mappa liquidità attuale:** muro bid: n/a; muro ask: n/a

![Microstruttura exchange BTC](exchange_microstructure_BTC.png)

### SOL

- Score grezzo exchange: **+2,00**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 5, accuratezza +60,00%.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 0, bear 1, divergenze 1.
- Flusso taker/order book: **+1,75**.
- OI/funding/basis: **+0,00**.
- Affollamento long/short: **+0,00**.
- Liquidazioni: **NON PESATE / FEED COMPLETO NON ASSUNTO DISPONIBILE**.
- **Wyckoff:** Fase Wyckoff non abbastanza chiara per una conferma exchange.
- **Fibonacci:** Fibonacci tenuto con acquisti/assorbimento coerenti: conferma positiva.
- **RSI:** RSI in zona non estrema o flusso exchange non abbastanza netto.
- **Pattern:** I pattern candidati restano non operativi: i dati exchange possono solo preparare la conferma.
- **Breakout/breakdown:** Prezzo non abbastanza vicino a un livello chiave o flusso non netto.
- **Mappa liquidità attuale:** muro bid: n/a; muro ask: n/a

![Microstruttura exchange SOL](exchange_microstructure_SOL.png)

### DOGE

- Score grezzo exchange: **+1,50**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 7, accuratezza +42,86%.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 0, bear 2, divergenze 1.
- Flusso taker/order book: **+0,75**.
- OI/funding/basis: **+0,50**.
- Affollamento long/short: **+0,00**.
- Liquidazioni: **NON PESATE / FEED COMPLETO NON ASSUNTO DISPONIBILE**.
- **Wyckoff:** Possibile accumulazione ancora neutrale nei dati exchange.
- **Fibonacci:** Fibonacci tenuto con acquisti/assorbimento coerenti: conferma positiva. Confluenza tecnica dichiarata: neckline rialzista, invalidazione rialzista.
- **RSI:** RSI in zona non estrema o flusso exchange non abbastanza netto.
- **Pattern:** I pattern candidati restano non operativi: i dati exchange possono solo preparare la conferma.
- **Breakout/breakdown:** Prezzo non abbastanza vicino a un livello chiave o flusso non netto.
- **Mappa liquidità attuale:** muro bid: n/a; muro ask: n/a

![Microstruttura exchange DOGE](exchange_microstructure_DOGE.png)

## Overlay sulle previsioni a 30 giorni

La previsione storica grezza dello scanner resta intatta. L'overlay exchange può correggerla solo dopo almeno 30 controlli maturati a 30 giorni e solo se il modulo dimostra accuratezza direzionale almeno del 55%.

| Asset | Prob. grezza salita | Return p50 grezzo | Controlli 30g | Accuratezza exchange | Stato overlay | Peso | Prob. corretta | Return corretto |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +72,50% | +7,19% | 1 | +0,00% | RACCOLTA DATI | 0,00 | +72,50% | +7,19% |
| SOL | +67,50% | +6,71% | 1 | +100,00% | RACCOLTA DATI | 0,00 | +67,50% | +6,71% |
| DOGE | +27,50% | -7,54% | 2 | +100,00% | RACCOLTA DATI | 0,00 | +27,50% | -7,54% |

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

Generato: 2026-09-02 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [exchange_signal_tracker_report.md](exchange_signal_tracker_report.md)

Questo tracker verifica se il segnale candidato exchange ±1 anticipa correttamente la direzione del prezzo a 1/3/7/14/30 giorni.
Il peso Global resta 0 finché l'orizzonte 7g non ha almeno 30 controlli, accuratezza almeno 55% e return corretto direzione positivo. L'overlay a 30g ha un gate separato.

Controlli maturati completati in questa esecuzione: **15**.

## Ultime fotografie giornaliere

| Data | Asset | Prezzo | Versione | Calibrazione | Candidato | Peso Global | Score raw | Confidenza | Taker 4h | OI 24h | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-09-02 | BTC | 77.400,00 | V2.1.3 | OK | 0 | 0 | -0,25 | BASSA | 0,94 | +2,54% | -1,43% |
| 2026-09-02 | DOGE | 0.08150 | V2.1.3 | OK | 0 | 0 | 1,50 | BASSA | 1,07 | -4,77% | -1,60% |
| 2026-09-02 | SOL | 99,75 | V2.1.3 | OK | 0 | 0 | 2,00 | BASSA | 1,31 | -2,41% | +3,33% |
| 2026-09-01 | BTC | 78.881,00 | V2.1.3 | OK | 0 | 0 | 2,00 | BASSA | 1,53 | +1,73% | -2,60% |
| 2026-09-01 | DOGE | 0.08336 | V2.1.3 | OK | 0 | 0 | 1,75 | BASSA | 1,12 | +0,30% | -0,88% |
| 2026-09-01 | SOL | 103,94 | V2.1.3 | OK | 0 | 0 | 3,25 | MEDIA | 1,77 | +2,67% | -2,00% |
| 2026-08-31 | BTC | 77.627,40 | V2.1.3 | OK | 0 | 0 | 2,00 | BASSA | 2,70 | -5,61% | -4,10% |
| 2026-08-31 | DOGE | 0.08216 | V2.1.3 | OK | 0 | 0 | 2,50 | BASSA | 1,51 | -6,45% | -4,98% |
| 2026-08-31 | SOL | 101,54 | V2.1.3 | OK | 0 | 0 | 1,75 | MEDIA | 1,62 | -9,59% | -10,08% |

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
| SOL | 14g | 2 | +50,00% | +8,38% | -5,94% | +13,89% | FEEDBACK RAPIDO |
| SOL | 30g | 1 | +100,00% | +8,60% | -9,55% | +9,55% | FEEDBACK RAPIDO |
| DOGE | 1g | 8 | +50,00% | +0,90% | -0,21% | +1,91% | FEEDBACK RAPIDO |
| DOGE | 3g | 8 | +37,50% | +1,43% | -3,31% | +6,31% | FEEDBACK RAPIDO |
| DOGE | 7g | 7 | +42,86% | -1,02% | -4,29% | +8,47% | FEEDBACK RAPIDO |
| DOGE | 14g | 4 | +50,00% | +2,59% | -1,41% | +16,82% | FEEDBACK RAPIDO |
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
| BTC | 77.667 $ | +0.0086% | -11.54% | 1.94 | Misto | 1/5 |
| SOL | 100,24 $ | -0.0009% | -33.39% | 2.70 | Misto | 1/5 |
| DOGE | 0.08188 $ | +0.0100% | -0.55% | 4.78 | Rischio sotto | 2/5 |

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

Generato: 2026-09-02 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [rsi_multitimeframe_divergence_report.md](rsi_multitimeframe_divergence_report.md)

Il modulo confronta prezzo e RSI 14 sui pivot confermati **daily e weekly**. Riconosce divergenze regolari e nascoste, segnali in formazione, invalidazioni e semplice conferma del momentum.

**Peso operativo: 0.** Non modifica il Global Confluence, non cambia le soglie del Paper Trading e non apre né blocca operazioni. I risultati vengono misurati prima di qualsiasi futura decisione sul peso.

## Sintesi corrente

| Asset   | Daily              | Stato D    | Weekly             | Stato W    | Lettura weekly                                                                                                              |   Peso |
|:--------|:-------------------|:-----------|:-------------------|:-----------|:----------------------------------------------------------------------------------------------------------------------------|-------:|
| BTC     | Hidden bullish     | CONFERMATA | Conferma rialzista | CONTESTO   | Prezzo e RSI stanno salendo insieme: momentum rialzista confermato.                                                         |      0 |
| SOL     | Conferma rialzista | CONTESTO   | Hidden bearish     | CONFERMATA | Hidden bearish confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto. |      0 |
| DOGE    | Conferma rialzista | CONTESTO   | Hidden bearish     | CONFERMATA | Hidden bearish confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto. |      0 |

## Dettaglio dei pivot

| Asset   | TF   | Tipo               | Stato      | Prezzo / RSI      | Pivot confrontati                                                   | Δ prezzo contesto   | Δ RSI contesto   |   Peso |
|:--------|:-----|:-------------------|:-----------|:------------------|:--------------------------------------------------------------------|:--------------------|:-----------------|-------:|
| BTC     | 1D   | Hidden bullish     | CONFERMATA | 77.663 $ / 66,76  | 2026-08-03 62.227 $ / RSI 47,40 → 2026-08-14 62.488 $ / RSI 42,71   | n/a                 | n/a              |      0 |
| BTC     | 1W   | Conferma rialzista | CONTESTO   | 77.663 $ / 56,54  | n/a                                                                 | +18,86%             | 15,88            |      0 |
| SOL     | 1D   | Conferma rialzista | CONTESTO   | 100,22 $ / 63,77  | n/a                                                                 | +30,10%             | 6,27             |      0 |
| SOL     | 1W   | Hidden bearish     | CONFERMATA | 100,22 $ / 56,77  | 2026-05-17 98,27 $ / RSI 38,29 → 2026-07-05 83,81 $ / RSI 42,25     | n/a                 | n/a              |      0 |
| DOGE    | 1D   | Conferma rialzista | CONTESTO   | 0.08188 $ / 52,98 | n/a                                                                 | +16,62%             | 5,43             |      0 |
| DOGE    | 1W   | Hidden bearish     | CONFERMATA | 0.08188 $ / 43,92 | 2026-05-17 0.11825 $ / RSI 44,25 → 2026-08-23 0.09998 $ / RSI 49,72 | n/a                 | n/a              |      0 |

### BTC

- **1D — Hidden bullish / CONFERMATA**: Hidden bullish confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto.
- **1W — Conferma rialzista / CONTESTO**: Prezzo e RSI stanno salendo insieme: momentum rialzista confermato.

### SOL

- **1D — Conferma rialzista / CONTESTO**: Prezzo e RSI stanno salendo insieme: momentum rialzista confermato.
- **1W — Hidden bearish / CONFERMATA**: Hidden bearish confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto.

### DOGE

- **1D — Conferma rialzista / CONTESTO**: Prezzo e RSI stanno salendo insieme: momentum rialzista confermato.
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

Generato: 2026-09-02 05:32 UTC


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

| Asset   | Prezzo   |   Punteggio | Verdetto                      | Trend           | Momentum        | Struttura                                          |   Pattern score | Fibonacci   | Pattern rialzista                | Pattern ribassista         | Supporto   | Resistenza   |
|:--------|:---------|------------:|:------------------------------|:----------------|:----------------|:---------------------------------------------------|----------------:|:------------|:---------------------------------|:---------------------------|:-----------|:-------------|
| BTC | 77.667 $ | 10 | RIALZISTA TECNICO | Trend rialzista | Momentum misto | Struttura rialzista con massimi e minimi crescenti | 0 | 0 / TENUTO | Doppio minimo / TARGET RAGGIUNTO | Doppio massimo / CANDIDATO | 62.488 | 81.347 |
| SOL | 100,24 $ | 9 | RIALZISTA TECNICO | Trend rialzista | Momentum misto | Struttura rialzista con massimi e minimi crescenti | 0 | 0 / TENUTO | Doppio minimo / TARGET RAGGIUNTO | Doppio massimo / CANDIDATO | 74,20 | 110,04 |
| DOGE | 0.08188 $ | 4 | COSTRUTTIVO MA NON CONFERMATO | Trend misto | Momentum debole | Struttura rialzista con massimi e minimi crescenti | 0 | +1 / TENUTO | Triplo minimo / TARGET RAGGIUNTO | Doppio massimo / CANDIDATO | 0.06895 | 0.09998 |

## Riepilogo ciclo di vita pattern

| Asset   | Doppio minimo    | Triplo minimo    | Adam/Eve Bottom                        | Doppio massimo   | Triplo massimo   | Adam/Eve Top                 |   Punteggio pattern |
|:--------|:-----------------|:-----------------|:---------------------------------------|:-----------------|:-----------------|:-----------------------------|--------------------:|
| BTC | TARGET RAGGIUNTO | TARGET RAGGIUNTO | Adam and Eve Bottom — TARGET RAGGIUNTO | CANDIDATO | CANDIDATO | Adam and Eve Top — CANDIDATO | 0 |
| SOL | TARGET RAGGIUNTO | TARGET RAGGIUNTO | Adam and Eve Bottom — TARGET RAGGIUNTO | CANDIDATO | CANDIDATO | Adam and Eve Top — CANDIDATO | 0 |
| DOGE | TARGET RAGGIUNTO | TARGET RAGGIUNTO | Adam and Eve Bottom — TARGET RAGGIUNTO | CANDIDATO | CANDIDATO | Adam and Eve Top — CANDIDATO | 0 |

## Indicatori tecnici

| Asset   |   RSI 14 |   Istogramma MACD | MA20    | MA50    | MA200   | Pendenza MA50 20g   | Pendenza MA200 60g   | Rendimento 30g   | Rendimento 90g   |
|:--------|---------:|------------------:|:--------|:--------|:--------|:--------------------|:---------------------|:-----------------|:-----------------|
| BTC | 66.78 | 103.828 | 73.183 | 67.886 | 69.469 | 7,10% | -7,16% | 22,39% | 21,73% |
| SOL | 63.81 | 0.60849 | 91,59 | 81,69 | 82,00 | 7,86% | -12,35% | 36,43% | 45,87% |
| DOGE | 52.98 | -0.00055 | 0.08109 | 0.07505 | 0.08883 | 3,92% | -13,93% | 16,73% | -7,35% |

## Dettaglio asset

### BTC

- Prezzo: **77.667 $**
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
  - Due minimi simili vicino a 62.201 tra 2026-06-18 e 2026-08-14. Neckline stimata: 66.910. Breakout neckline: 2026-08-19 (14 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 71.619; progresso corrente: 228,44%. Relazione prezzo/neckline: sopra neckline.
  - neckline 66.910; target 71.619; breakout 2026-08-19 (14g); progresso 228,44%; prezzo sopra neckline.
- Triplo minimo: **TARGET RAGGIUNTO** (0)
  - Tre minimi simili vicino a 62.201 dal 2026-06-18 al 2026-08-14. Neckline stimata: 66.910. Breakout neckline: 2026-08-19 (14 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 71.619; progresso corrente: 228,44%. Relazione prezzo/neckline: sopra neckline.
  - neckline 66.910; target 71.619; breakout 2026-08-19 (14g); progresso 228,44%; prezzo sopra neckline.
- Adam and Eve Bottom: **TARGET RAGGIUNTO** (0)
  - Pattern Adam and Eve Bottom vicino a 59.109 dal 2026-06-05 al 2026-08-14. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 67.248. Breakout neckline: 2026-08-19 (14 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 75.387; progresso corrente: 128,01%. Relazione prezzo/neckline: sopra neckline.
  - neckline 67.248; target 75.387; breakout 2026-08-19 (14g); progresso 128,01%; prezzo sopra neckline.
- Doppio massimo: **CANDIDATO** (0)
  - Due massimi simili vicino a 65.544 tra 2026-06-22 e 2026-08-09. Neckline ribassista stimata: 57.748. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 24 giorni.
  - neckline 57.748; target 49.952; distanza dalla neckline 34,49%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 65.544 dal 2026-06-22 al 2026-08-09. Neckline ribassista stimata: 57.748. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 24 giorni.
  - neckline 57.748; target 49.952; distanza dalla neckline 34,49%; prezzo sopra neckline.
- Adam and Eve Top: **CANDIDATO** (0)
  - Pattern Adam and Eve Top vicino a 67.248 dal 2026-06-15 al 2026-07-21. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 57.748. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 43 giorni.
  - neckline 57.748; target 48.247; distanza dalla neckline 34,49%; prezzo sopra neckline.

### SOL

- Prezzo: **100,24 $**
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
  - Due minimi simili vicino a 73,40 tra 2026-07-17 e 2026-08-16. Neckline stimata: 78,73. Breakout neckline: 2026-08-19 (14 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 84,05; progresso corrente: 404,08%. Relazione prezzo/neckline: sopra neckline.
  - neckline 78,73; target 84,05; breakout 2026-08-19 (14g); progresso 404,08%; prezzo sopra neckline.
- Triplo minimo: **TARGET RAGGIUNTO** (0)
  - Tre minimi simili vicino a 70,69 dal 2026-07-17 al 2026-08-16. Neckline stimata: 78,73. Breakout neckline: 2026-08-19 (14 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 86,76; progresso corrente: 267,86%. Relazione prezzo/neckline: sopra neckline.
  - neckline 78,73; target 86,76; breakout 2026-08-19 (14g); progresso 267,86%; prezzo sopra neckline.
- Adam and Eve Bottom: **TARGET RAGGIUNTO** (0)
  - Pattern Adam and Eve Bottom vicino a 67,92 dal 2026-06-19 al 2026-08-01. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 83,81. Breakout neckline: 2026-08-19 (14 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 99,70; progresso corrente: 103,40%. Relazione prezzo/neckline: sopra neckline.
  - neckline 83,81; target 99,70; breakout 2026-08-19 (14g); progresso 103,40%; prezzo sopra neckline.
- Doppio massimo: **CANDIDATO** (0)
  - Due massimi simili vicino a 78,88 tra 2026-07-15 e 2026-08-09. Neckline ribassista stimata: 70,69. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 24 giorni.
  - neckline 70,69; target 62,51; distanza dalla neckline 41,79%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 78,88 dal 2026-07-15 al 2026-08-09. Neckline ribassista stimata: 70,69. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 24 giorni.
  - neckline 70,69; target 62,51; distanza dalla neckline 41,79%; prezzo sopra neckline.
- Adam and Eve Top: **CANDIDATO** (0)
  - Pattern Adam and Eve Top vicino a 77,62 dal 2026-06-22 al 2026-08-09. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 64,42. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 24 giorni.
  - neckline 64,42; target 51,22; distanza dalla neckline 55,61%; prezzo sopra neckline.

### DOGE

- Prezzo: **0.08188 $**
- Punteggio tecnico: **4 / 12**
- Verdetto: **COSTRUTTIVO MA NON CONFERMATO**
- Trend: **Trend misto** (1)
- Momentum: **Momentum debole** (-3)
- Volume: **Volume da accumulazione** (2)
- Struttura: **Struttura rialzista con massimi e minimi crescenti** (2)
  - Dettaglio struttura: Ultimi minimi: 0.06835 -> 0.06895. Ultimi massimi: 0.07286 -> 0.09998.
- Divergenza: **Nessuna** (0)
- Fase Wyckoff candidata: **Possibile accumulazione** (1)
  - Dettaglio Wyckoff: Prezzo sotto MA200, vicino alla parte bassa del range a 120 giorni, RSI 53.0.
- Fibonacci automatico: **TENUTO** (+1)
  - Swing UP 2026-08-01 0.06797 -> 2026-08-22 0.09998; livello più vicino 61.8% a 0.08020; stato TENUTO; confluenza: neckline rialzista, invalidazione rialzista.
- Punteggio pattern: **0**
  - rialzista dominante: Triplo minimo (TARGET RAGGIUNTO, 0); ribassista dominante: Doppio massimo (CANDIDATO, 0).
- Supporto più vicino: **0.06895**
- Resistenza più vicina: **0.09998**

Pattern classici e ciclo di vita:

- Doppio minimo: **TARGET RAGGIUNTO** (0)
  - Due minimi simili vicino a 0.06829 tra 2026-07-24 e 2026-08-12. Neckline stimata: 0.07380. Breakout neckline: 2026-08-19 (14 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 0.07931; progresso corrente: 146,54%. Relazione prezzo/neckline: sopra neckline.
  - neckline 0.07380; target 0.07931; breakout 2026-08-19 (14g); progresso 146,54%; prezzo sopra neckline.
- Triplo minimo: **TARGET RAGGIUNTO** (0)
  - Tre minimi simili vicino a 0.06835 dal 2026-06-30 al 2026-08-12. Neckline stimata: 0.07923. Breakout neckline: 2026-08-20 (13 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 0.09012; progresso corrente: 24,31%. Relazione prezzo/neckline: sopra neckline.
  - neckline 0.07923; target 0.09012; breakout 2026-08-20 (13g); progresso 24,31%; prezzo sopra neckline.
- Adam and Eve Bottom: **TARGET RAGGIUNTO** (0)
  - Pattern Adam and Eve Bottom vicino a 0.06829 dal 2026-07-24 al 2026-08-06. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 0.07380. Breakout neckline: 2026-08-19 (14 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 0.07931; progresso corrente: 146,54%. Relazione prezzo/neckline: sopra neckline.
  - neckline 0.07380; target 0.07931; breakout 2026-08-19 (14g); progresso 146,54%; prezzo sopra neckline.
- Doppio massimo: **CANDIDATO** (0)
  - Due massimi simili vicino a 0.07380 tra 2026-07-26 e 2026-08-11. Neckline ribassista stimata: 0.06797. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 22 giorni.
  - neckline 0.06797; target 0.06214; distanza dalla neckline 20,46%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 0.07923 dal 2026-07-04 al 2026-08-11. Neckline ribassista stimata: 0.06797. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 22 giorni.
  - neckline 0.06797; target 0.05671; distanza dalla neckline 20,46%; prezzo sopra neckline.
- Adam and Eve Top: **CANDIDATO** (0)
  - Pattern Adam and Eve Top vicino a 0.07923 dal 2026-07-04 al 2026-08-11. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 0.06797. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 22 giorni.
  - neckline 0.06797; target 0.05671; distanza dalla neckline 20,46%; prezzo sopra neckline.

## Fibonacci automatico

Il modulo seleziona uno swing recente tramite pivot confermati. Un semplice tocco vale 0: Fibonacci pesa al massimo ±1 soltanto quando il livello è tenuto, perso, recuperato o respinto e coincide con almeno un livello tecnico indipendente.

| Asset   | Swing                       | 23,6%   | 38,2%   | 50,0%   | 61,8%   | 78,6%   | Livello vicino   | Stato   | Confluenza                                  |   Score |
|:--------|:----------------------------|:--------|:--------|:--------|:--------|:--------|:-----------------|:--------|:--------------------------------------------|--------:|
| BTC | UP 2026-07-01 -> 2026-08-28 | 75.778 | 72.332 | 69.547 | 66.763 | 62.798 | 23.6% / 75.778 | TENUTO | nessuna confluenza indipendente | 0 |
| SOL | UP 2026-06-06 -> 2026-08-27 | 98,33 | 91,08 | 85,23 | 79,37 | 71,03 | 23.6% / 98,33 | TENUTO | nessuna confluenza indipendente | 0 |
| DOGE | UP 2026-08-01 -> 2026-08-22 | 0.09243 | 0.08775 | 0.08398 | 0.08020 | 0.07482 | 61.8% / 0.08020 | TENUTO | neckline rialzista, invalidazione rialzista | +1 |

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

- **BTC**: 30/30 previsioni controllate su 60 fatte. Stato: **ATTIVA**.
- **SOL**: 30/30 previsioni controllate su 60 fatte. Stato: **ATTIVA**.
- **DOGE**: 30/30 previsioni controllate su 60 fatte. Stato: **ATTIVA**.

| Asset | Previsioni fatte | Controllate | Progresso | In attesa | Stato | Prossimo controllo |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 60 | 30 | 30/30 [██████████] | 30 | ATTIVA | 2026-09-03 / tra 1 giorno |
| SOL | 60 | 30 | 30/30 [██████████] | 30 | ATTIVA | 2026-09-03 / tra 1 giorno |
| DOGE | 60 | 30 | 30/30 [██████████] | 30 | ATTIVA | 2026-09-03 / tra 1 giorno |

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

Generato: 2026-09-02 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [data_quality_coherence_report.md](data_quality_coherence_report.md)

Questo controllo non modifica punteggi o decisioni. Verifica che tutti i moduli usino lo stesso prezzo corrente e che le nuove regole Technical/Classic Visual siano integre.

## Stato finale: **WARN**

## Avvisi

- 3 campi prezzo superano la tolleranza specifica del modulo.

## Prezzo unico per modulo

| Modulo                  | Asset   | Campo             | Stato   | Prezzo snapshot   | Prezzo modulo   | Differenza   |
|:------------------------|:--------|:------------------|:--------|:------------------|:----------------|:-------------|
| Scanner                 | BTC     | current_price     | OK      | 77.667 $          | 77.667 $        | +0,0000%     |
| Scanner                 | DOGE    | current_price     | OK      | 0.08188 $         | 0.08188 $       | -0,0000%     |
| Scanner                 | SOL     | current_price     | OK      | 100,24 $          | 100,24 $        | -0,0000%     |
| Scanner Forecast        | BTC     | current_price     | OK      | 77.667 $          | 77.667 $        | +0,0000%     |
| Scanner Forecast        | SOL     | current_price     | OK      | 100,24 $          | 100,24 $        | -0,0000%     |
| Scanner Forecast        | DOGE    | current_price     | OK      | 0.08188 $         | 0.08188 $       | -0,0000%     |
| Technical Structure     | BTC     | price             | OK      | 77.667 $          | 77.667 $        | +0,0000%     |
| Technical Structure     | SOL     | price             | OK      | 100,24 $          | 100,24 $        | -0,0000%     |
| Technical Structure     | DOGE    | price             | OK      | 0.08188 $         | 0.08188 $       | -0,0000%     |
| Classic Technical       | BTC     | price             | OK      | 77.667 $          | 77.667 $        | +0,0000%     |
| Classic Technical       | SOL     | price             | OK      | 100,24 $          | 100,24 $        | -0,0000%     |
| Classic Technical       | DOGE    | price             | OK      | 0.08188 $         | 0.08188 $       | -0,0000%     |
| Classic Visual          | BTC     | price             | OK      | 77.667 $          | 77.667 $        | +0,0000%     |
| Classic Visual          | SOL     | price             | OK      | 100,24 $          | 100,24 $        | -0,0000%     |
| Classic Visual          | DOGE    | price             | OK      | 0.08188 $         | 0.08188 $       | -0,0000%     |
| Exchange Microstructure | BTC     | price             | WARN    | 77.667 $          | 77.400 $        | -0,3438%     |
| Exchange Microstructure | SOL     | price             | WARN    | 100,24 $          | 99,75 $         | -0,4882%     |
| Exchange Microstructure | DOGE    | price             | WARN    | 0.08188 $         | 0.08150 $       | -0,4641%     |
| RSI top-cycle           | SOL     | current_price     | OK      | 100,24 $          | 100,24 $        | -0,0000%     |
| RSI top-cycle           | SOL     | current_price     | OK      | 100,24 $          | 100,24 $        | -0,0000%     |
| Frattale BTC/SOL        | SOL     | sol_current_price | OK      | 100,24 $          | 100,24 $        | -0,0000%     |
| Fractal path            | SOL     | current_price     | OK      | 100,24 $          | 100,24 $        | -0,0000%     |

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

Generato: 2026-09-02T08:30:34+00:00

- Modalità: **SOLO PAPER TRADING**
- Asset: **SOL spot**
- Leva: **nessuna (1x)**
- Capitale iniziale separato: **€40.000,00**
- Fonte mercato: **KUCOIN_PUBLIC_API**; nuove entrate: **CONSENTITE**

| Equity | Cash | SOL | Prezzo | Rendimento | Realizzato | Commissioni | Max DD | Operazioni |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €43.406,07 | €23.906,86 | 195.414205 | 99.7840 | +8.52% | €3.453,09 | €94,99 | 6.48% | 59 |

**Ultima decisione:** BUY_TRANCHE — SOL sotto la prima banda adattiva.

Bande 4H: L2 96.8900 · L1 99.7853 · media 103.4045 · U1 107.0236 · U2 109.9189.

> Questo portafoglio non condivide capitale, posizioni o statistiche con il paper trading da €10.000.
<!-- SOL_SPOT_ADAPTIVE_END -->
