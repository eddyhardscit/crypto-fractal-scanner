<!-- COMPACT_REPORT_HEADER_START -->
> **Vista compatta:** Decisione operativa, Global Confluence e cambiamenti giornalieri restano aperti. Tocca il titolo di una sezione per mostrare o nascondere i dettagli.  
> Tutte le tabelle e tutti i dati restano nel file: copiando il Markdown raw viene copiato tutto.
<!-- COMPACT_REPORT_HEADER_END -->

<!-- COMPACT_SECTION_START:decision -->
<details open>
<summary><strong>🧭 Decisione operativa — da leggere per prima</strong></summary>

<!-- DECISION_REPORT_START -->

# Decisione operativa sintetica

Generato: 2026-09-09 05:33 UTC

Report separato completo: [decision_report.md](decision_report.md)

Sintesi automatica dello scanner: l'azione spot viene copiata direttamente dal Global Confluence; long, short e rischio restano filtri separati e più prudenti.

| Asset | Global | Direzione | Spot | Long leva | Short leva | Max long | Max short | Rischio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +6 | BULLISH | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE | LONG PRUDENTE | NO SHORT | max 2x isolated | nessuna | MEDIO |
| SOL | +5 | NEUTRALE / COSTRUTTIVO | HOLD / TRANCHE PICCOLE, NO LEVA | NO LONG A LEVA | NO SHORT | nessuna | nessuna | MOLTO ALTO |
| DOGE | +3 | NEUTRALE / COSTRUTTIVO | SOLO TRANCHE PICCOLE / NO LEVA | NO LONG A LEVA | NO SHORT | nessuna | nessuna | MOLTO ALTO |

## Lettura immediata

- **BTC**: Global = **+6**, spot = **ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE**, long = **LONG PRUDENTE**, short = **NO SHORT**, rischio = **MEDIO**.
- **SOL**: Global = **+5**, spot = **HOLD / TRANCHE PICCOLE, NO LEVA**, long = **NO LONG A LEVA**, short = **NO SHORT**, rischio = **MOLTO ALTO**.
- **DOGE**: Global = **+3**, spot = **SOLO TRANCHE PICCOLE / NO LEVA**, long = **NO LONG A LEVA**, short = **NO SHORT**, rischio = **MOLTO ALTO**.

## Dettaglio logica

### BTC

- Global Confluence: **+6**
- Confluenza: **MODERATAMENTE POSITIVA**
- Bias Global: **Costruttivo prudente**
- Direzione decisionale: **BULLISH**
- Azione spot dal Global: **ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE**
- Long leva: **LONG PRUDENTE**
- Short leva: **NO SHORT**
- Rischio: **MEDIO**
- Conferme: Prima resistenza sopra 82.262; conferma del doppio minimo sopra 65.402.
- Invalidazioni: Sotto 76.248 il quadro tecnico peggiora.

### SOL

- Global Confluence: **+5**
- Confluenza: **MODERATAMENTE POSITIVA**
- Bias Global: **Costruttivo prudente**
- Direzione decisionale: **NEUTRALE / COSTRUTTIVO**
- Azione spot dal Global: **HOLD / TRANCHE PICCOLE, NO LEVA**
- Long leva: **NO LONG A LEVA**
- Short leva: **NO SHORT**
- Rischio: **MOLTO ALTO**
- Conferme: Doppio minimo target raggiunto finché mantiene 78,73; nuova conferma tecnica sopra 110,04; milestone analogiche 109,65 / 137,24, valide soltanto se rientra anche il gap frattale.
- Invalidazioni: Allarmi sotto 90,88 / 97,45 / 62,19.

### DOGE

- Global Confluence: **+3**
- Confluenza: **MODERATAMENTE POSITIVA**
- Bias Global: **Costruttivo prudente**
- Direzione decisionale: **NEUTRALE / COSTRUTTIVO**
- Azione spot dal Global: **SOLO TRANCHE PICCOLE / NO LEVA**
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
- **Lifecycle EMA200** = per SOL resta solo contesto, peso Global 0; score interno 2; EMA200 circa 111,27 $; upside verso EMA200 +6,76%. Non autorizza leva e non aggiunge punti automatici.
- **NO LONG** non significa automaticamente **SHORT**. Lo short ha senso solo se il quadro è bearish o se lo spike viene spesso scaricato.
- Per SOL, se il Global è da **+3 in su**, la decisione non deve diventare bearish solo perché lo scanner grezzo a 30 giorni è incerto.

<!-- DECISION_REPORT_END -->

<!-- PAPER_TRADING_START -->
# Paper trading automatico KuCoin

Generato: 2026-09-09T05:33:19+00:00


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [paper_trading_report.md](paper_trading_report.md)

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-09-09T05:05:32+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-09-09T05:05:32+00:00 | 2026-09-09T05:05:32+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-09-09T04:45:00+00:00 | 2026-09-09T04:45:00+00:00 | 5,8 min | 25,0 min | OK |
| 60m | 12 | 2026-09-09T04:00:00+00:00 | 2026-09-09T04:00:00+00:00 | 5,8 min | 45,0 min | OK |
| 240m | 12 | 2026-09-09T00:00:00+00:00 | 2026-09-09T00:00:00+00:00 | 1,10 h | 1,00 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1H Fast V3 Nohigh Regime Guard V1 | ETH | 60m | LONG | 6,65 | 4,50 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 Nohigh Range Only V1 | ETH | 60m | LONG | 6,65 | 4,50 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Master Adaptive Gb20 Loss Cap V1 | USELESS | 60m | LONG | 7,75 | 0,00 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Combo Mean Reversion | ZEC | 60m | LONG | 8,99 | 5,00 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top10 Long | XRP | 60m | LONG | 6,23 | 5,00 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Benchmark Bollinger mean reversion 1H | ZEC | 60m | LONG | 8,99 | 5,00 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | ETH | 60m | LONG | 6,65 | 4,50 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 No Esports Stress Guard V1 | ETH | 60m | LONG | 6,65 | 4,50 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 No Esports Long Only V1 | ETH | 60m | LONG | 6,65 | 4,50 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 Long Nohigh Cap75 V1 | ETH | 60m | LONG | 6,65 | 4,50 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 Long Only V1 | ETH | 60m | LONG | 6,65 | 4,50 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 Nohigh V1 | ETH | 60m | LONG | 6,65 | 4,50 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 Cap75 V1 | ETH | 60m | LONG | 6,65 | 4,50 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Score 6 75 Range Only V1 | ETH | 60m | LONG | 6,65 | 6,00 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Score 6 75 No Trend Up V1 | ETH | 60m | LONG | 6,65 | 6,00 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Score 6 75 V1 | ETH | 60m | LONG | 6,65 | 6,00 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Principale 4H | PEPE | 240m | LONG | 4,13 | 6,00 | 1,87 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.8 minuti; tolleranza 60 minuti. |
| Principale 4H | SUI | 240m | LONG | 4,10 | 6,00 | 1,90 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.8 minuti; tolleranza 60 minuti. |
| Principale 4H | HYPE | 240m | LONG | 4,09 | 6,00 | 1,91 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.8 minuti; tolleranza 60 minuti. |
| Principale 4H | ETH | 240m | LONG | 3,95 | 6,00 | 2,05 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.8 minuti; tolleranza 60 minuti. |
| Principale 4H | XRP | 240m | LONG | 3,87 | 6,00 | 2,13 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.8 minuti; tolleranza 60 minuti. |
| Principale 4H | DOGE | 240m | LONG | 1,92 | 6,00 | 4,08 | STALE_CANDLE | 1,10 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.8 minuti; tolleranza 60 minuti. |
| Principale 4H | ADA | 240m | LONG | 1,60 | 6,00 | 4,39 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.8 minuti; tolleranza 60 minuti. |
| Principale 4H | BTC | 240m | SHORT | -1,00 | 6,00 | 5,00 | STALE_CANDLE | 1,10 h | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.8 minuti; tolleranza 60 minuti. |
| Principale 4H | SOPH | 240m | LONG | 0,75 | 6,00 | 5,25 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.8 minuti; tolleranza 60 minuti. |
| Principale 4H | SOL | 240m | LONG | 0,71 | 6,00 | 5,29 | STALE_CANDLE | 1,10 h | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.8 minuti; tolleranza 60 minuti. |
| 1H Balanced Long No Rhv V1 | ZEC | 60m | LONG | 8,99 | 5,00 | 0,00 | READY | 5,8 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Fast No Pepe V1 | ZEC | 60m | LONG | 8,99 | 4,50 | 0,00 | READY | 5,8 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Fast Tp2 V1 | ZEC | 60m | LONG | 8,99 | 4,50 | 0,00 | READY | 5,8 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Rapida 1H V2 | ZEC | 60m | LONG | 8,99 | 5,00 | 0,00 | OPENED | 5,8 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida 1H V3 Filtered | ZEC | 60m | LONG | 8,99 | 4,50 | 0,00 | READY | 5,8 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Fast V3 No Esports V1 | ZEC | 60m | LONG | 8,99 | 4,50 | 0,00 | READY | 5,8 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Fast V3 No Esports Mfe Lock V1 | ZEC | 60m | LONG | 8,99 | 4,50 | 0,00 | READY | 5,8 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Forza relativa 1H V1 | ZEC | 60m | LONG | 8,99 | 4,00 | 0,00 | READY | 5,8 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Forza relativa 1H V2 | ZEC | 60m | LONG | 8,99 | 5,50 | 0,00 | READY | 5,8 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Benchmark Donchian breakout 1H | ZEC | 60m | LONG | 8,99 | 5,00 | 0,00 | READY | 5,8 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.816,14 | -1,84% | €7,58 | €3.000,00 | 0,25% | 5 | 60 | 41,67% | 0,88 | 6,86% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 60 | 3290 | PRIME INDICAZIONI | 100 (mancano 40) |

- Trade del Principale 4H chiusi: **60**; win rate **41,67%**; profit factor **0,88**.
- Expectancy: **€-3,05** per trade; P&L netto: **€-182,77**; max drawdown: **6,86%**.
- Valutazione: **Si può osservare la direzione, ma il risultato resta fragile.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 5 | €9.816,14 | €700,63 | €2.101,90 | €196,32 | €0,00 |
| TEST | Benchmark Donchian breakout 1H | 6 | €11.341,25 | €3.389,12 | €6.778,25 | €226,77 | €-70,28 |
| TEST | Main Side Regime Guard V1 | 6 | €11.175,45 | €628,60 | €1.885,81 | €223,51 | €0,00 |
| TEST | Donchian 1H Gb20 120R V1 | 6 | €11.074,23 | €3.309,33 | €6.618,66 | €221,43 | €-68,63 |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | 7 | €10.979,98 | €753,45 | €2.260,35 | €120,75 | €28,16 |
| TEST | Scanner Top 5 Long 1H | 6 | €10.950,06 | €1.236,30 | €2.472,61 | €223,50 | €0,61 |
| TEST | Combo Trend Side Regime Guard V1 | 6 | €10.790,32 | €1.449,24 | €2.898,47 | €167,65 | €0,00 |
| TEST | Combo Adaptive Long Only V1 | 6 | €10.531,71 | €2.330,81 | €4.661,61 | €208,87 | €0,00 |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | 7 | €10.457,68 | €2.037,11 | €6.111,33 | €156,61 | €-7,97 |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | 2 | €10.401,95 | €2.287,50 | €6.862,50 | €103,11 | €-191,24 |
| TEST | Main Dynamic Asset Selector V1 | 3 | €10.383,82 | €487,35 | €1.462,04 | €101,76 | €81,87 |
| TEST | 1H Fast No Pepe V1 | 6 | €10.364,13 | €1.315,38 | €3.946,13 | €209,22 | €-207,66 |
| TEST | Combo Adaptive | 8 | €10.363,63 | €1.341,55 | €2.683,10 | €156,26 | €0,35 |
| TEST | Rapida 1H V2 | 3 | €10.356,85 | €1.895,85 | €5.687,56 | €156,34 | €-193,35 |
| TEST | Scanner Top15 Long | 8 | €10.352,60 | €1.939,61 | €3.879,23 | €206,92 | €6,60 |
| TEST | Scanner Top20 Long | 8 | €10.352,60 | €1.939,61 | €3.879,23 | €206,92 | €6,60 |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | 5 | €10.306,08 | €1.562,50 | €4.687,49 | €207,96 | €-89,88 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 0 | €10.300,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Tp3 V1 | 6 | €10.275,45 | €1.981,44 | €3.962,88 | €205,93 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 0 | €10.271,73 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Scanner | 7 | €10.271,00 | €1.562,67 | €3.125,34 | €209,73 | €0,00 |
| TEST | Scanner Top5 Btc Runner25 V1 | 6 | €10.269,44 | €1.980,28 | €3.960,56 | €205,81 | €0,00 |
| TEST | Scanner Top 5 + forza BTC 1H | 7 | €10.264,72 | €1.170,86 | €2.341,73 | €211,83 | €0,00 |
| TEST | Rapida 1H V3 Filtered | 5 | €10.239,87 | €1.552,46 | €4.657,37 | €206,63 | €-89,30 |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 0 | €10.239,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Donchian 1H | 0 | €10.236,75 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 0 | €10.235,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 No Esports Long Only V1 | 8 | €10.216,59 | €2.061,99 | €6.185,98 | €200,94 | €1,47 |
| TEST | Btc Bollinger 1H | 0 | €10.209,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top10 Long | 6 | €10.201,69 | €2.352,63 | €4.705,26 | €204,04 | €-0,02 |
| TEST | Ampia 4H | 9 | €10.197,35 | €1.023,36 | €2.046,73 | €203,96 | €3,79 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 0 | €10.185,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 4H | 1 | €10.176,68 | €613,63 | €1.227,27 | €50,96 | €-13,85 |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 0 | €10.145,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Donchian 4H | 1 | €10.143,30 | €574,98 | €1.149,96 | €50,72 | €-0,57 |
| TEST | Btc Bollinger 4H | 1 | €10.108,51 | €985,68 | €1.971,36 | €0,00 | €40,60 |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 0 | €10.099,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | 5 | €10.090,54 | €2.166,79 | €6.500,37 | €151,28 | €32,00 |
| TEST | Doge Donchian 1H | 0 | €10.066,52 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Partial 1R V1 | 5 | €10.049,05 | €1.969,94 | €3.939,88 | €151,12 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 0 | €10.048,77 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V1 | 0 | €10.043,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Tp2 V1 | 6 | €10.041,24 | €593,76 | €1.781,29 | €150,51 | €1,16 |
| TEST | 1H Balanced Short Trend Down Strict V1 | 0 | €10.035,46 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · prudente · 5x | 0 | €10.032,32 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €50 · 15x | 0 | €10.022,70 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €10.014,08 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €50 · 15x | 0 | €10.009,44 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 0 | €10.008,92 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 4H | 0 | €10.005,51 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €10 · 15x | 0 | €10.004,54 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 0 | €10.003,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 0 | €10.002,82 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €10 · 15x | 0 | €10.001,89 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Continuation V1 | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €10 · 15x | 0 | €9.998,68 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · prudente · 5x | 0 | €9.996,83 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 0 | €9.995,23 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €10 · 15x | 0 | €9.994,07 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €50 · 15x | 0 | €9.993,42 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Ema 1H | 0 | €9.989,46 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €10 · 15x | 0 | €9.988,90 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 4H | 0 | €9.980,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Bollinger 1H | 0 | €9.979,42 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €50 · 15x | 0 | €9.970,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · prudente · 5x | 0 | €9.970,34 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 0 | €9.966,58 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 4H | 0 | €9.964,84 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 1H | 0 | €9.962,68 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | 0 | €9.959,32 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | 5 | €9.955,32 | €1.948,53 | €5.845,58 | €199,11 | €38,90 |
| TEST | Sol Adaptive 1H | 0 | €9.953,87 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Nohigh Range Only V1 | 5 | €9.945,30 | €2.505,93 | €7.517,80 | €100,00 | €-157,20 |
| TEST | Scalp RSI Long 25 · €50 · 15x | 0 | €9.944,51 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · prudente · 5x | 0 | €9.939,55 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 1H | 1 | €9.937,98 | €1.153,77 | €3.461,31 | €49,84 | €-28,93 |
| TEST | 1H Fast Score 6 75 Range Only V1 | 5 | €9.932,52 | €1.281,06 | €3.843,19 | €102,57 | €-169,42 |
| TEST | Btc Donchian 1H | 0 | €9.922,88 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.917,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 4H | 0 | €9.914,14 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Side Regime Guard V1 | 7 | €9.895,17 | €1.112,87 | €2.225,74 | €101,44 | €0,25 |
| TEST | Eth Ema 4H | 1 | €9.887,95 | €690,19 | €1.380,39 | €49,44 | €2,49 |
| TEST | Btc Donchian 4H | 0 | €9.861,10 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Long Only V1 | 7 | €9.853,15 | €1.121,16 | €3.363,48 | €147,97 | €30,91 |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 0 | €9.837,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Forza relativa 1H V2 | 6 | €9.835,51 | €844,71 | €1.689,41 | €99,47 | €-2,88 |
| TEST | Combo Adaptive Quality7 Regime V1 | 0 | €9.834,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 0 | €9.817,34 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Adaptive 1H | 0 | €9.771,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 1H | 0 | €9.765,13 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 0 | €9.762,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Bollinger 1H | 0 | €9.731,13 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 0 | €9.723,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Donchian 1H | 0 | €9.711,11 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Guard V1 | 6 | €9.689,08 | €1.051,56 | €2.103,13 | €195,06 | €0,41 |
| TEST | 1H Fast Score 6 75 V1 | 5 | €9.673,09 | €3.074,96 | €9.224,87 | €98,69 | €46,86 |
| TEST | Eth Ema 1H | 0 | €9.667,53 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Nohigh V1 | 5 | €9.665,75 | €1.215,56 | €3.646,68 | €193,32 | €-202,20 |
| TEST | 1H Balanced Long No Rhv V1 | 5 | €9.654,26 | €1.152,76 | €3.458,29 | €194,56 | €0,51 |
| TEST | Global Confluence puro 1H | 0 | €9.647,46 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | 5 | €9.646,94 | €3.081,56 | €9.244,68 | €99,01 | €46,98 |
| TEST | 1H Fast Nohigh Cap75 V1 | 4 | €9.631,96 | €1.004,71 | €3.014,12 | €145,58 | €-87,05 |
| TEST | Scanner Top5 Btc Mfe V1 | 7 | €9.622,67 | €1.097,63 | €2.195,25 | €198,58 | €0,00 |
| TEST | Master Adaptive Gb20 Be V1 | 5 | €9.622,60 | €1.120,46 | €2.240,92 | €192,25 | €6,16 |
| TEST | Master Adaptive Gb20 Partial V1 | 5 | €9.612,36 | €1.119,27 | €2.238,53 | €192,04 | €6,16 |
| TEST | Combo Adaptive Regime V1 | 1 | €9.587,02 | €987,06 | €1.974,12 | €49,09 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 0 | €9.579,83 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive V1 | 5 | €9.575,18 | €1.114,94 | €2.229,88 | €191,30 | €6,13 |
| TEST | Master Adaptive Runner25 V1 | 7 | €9.545,31 | €1.377,51 | €2.755,02 | €191,36 | €3,32 |
| TEST | Combo Adaptive Quality7 V1 | 4 | €9.512,30 | €1.438,51 | €2.877,02 | €190,29 | €0,00 |
| TEST | 1H Fast V3 No Esports V1 | 5 | €9.468,91 | €1.053,15 | €3.159,44 | €191,07 | €-83,60 |
| TEST | Scanner Top5 Btc Guard Mfe V1 | 6 | €9.463,75 | €1.027,11 | €2.054,22 | €190,52 | €0,40 |
| TEST | Btc Ema 1H | 1 | €9.457,61 | €1.097,82 | €3.293,47 | €47,43 | €-25,76 |
| TEST | Master Adaptive Gb20 V1 | 5 | €9.448,83 | €1.100,26 | €2.200,52 | €188,78 | €6,05 |
| TEST | Master Adaptive Gb20 Loss Cap V1 | 8 | €9.401,46 | €1.188,08 | €2.376,15 | €188,04 | €0,25 |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | 4 | €9.392,07 | €979,65 | €2.938,95 | €141,95 | €-84,88 |
| TEST | Master Adaptive Expanded V1 | 5 | €9.370,92 | €1.584,98 | €3.169,96 | €187,41 | €0,57 |
| TEST | Bilanciata 1H V2 | 6 | €9.328,07 | €1.122,19 | €3.366,57 | €93,13 | €89,25 |
| TEST | Scanner Bottom10 Short | 4 | €9.320,74 | €1.261,36 | €2.522,73 | €140,86 | €0,00 |
| TEST | Scanner Bottom15 Short | 4 | €9.320,74 | €1.261,36 | €2.522,73 | €140,86 | €0,00 |
| TEST | Scanner Bottom20 Short | 4 | €9.320,74 | €1.261,36 | €2.522,73 | €140,86 | €0,00 |
| TEST | Bilanciata 1H V3 Filtered | 5 | €9.286,43 | €1.676,21 | €5.028,62 | €146,05 | €-96,65 |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | 4 | €9.256,15 | €1.252,64 | €2.505,29 | €139,88 | €0,00 |
| TEST | Scanner Bottom5 Short Profit Lock V1 | 4 | €9.242,07 | €1.250,74 | €2.501,48 | €139,67 | €0,00 |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | 7 | €9.219,67 | €842,57 | €1.685,14 | €184,07 | €16,10 |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | 1 | €9.214,28 | €205,67 | €617,01 | €48,38 | €0,00 |
| TEST | Master Adaptive No Alt V1 | 7 | €9.209,65 | €1.531,15 | €3.062,30 | €184,52 | €47,55 |
| TEST | Benchmark trend following EMA 1H | 5 | €9.187,13 | €981,82 | €1.963,65 | €144,18 | €0,00 |
| TEST | Scanner Bottom 5 Short 1H | 4 | €9.170,95 | €1.241,11 | €2.482,23 | €138,60 | €0,00 |
| TEST | Bilanciata 1H V1 | 3 | €9.130,02 | €400,34 | €1.201,03 | €48,28 | €-2,73 |
| TEST | Combo Adaptive Runner25 V1 | 6 | €9.109,08 | €1.341,56 | €2.683,11 | €138,29 | €0,61 |
| TEST | Combo Adaptive Mfe Trail | 7 | €9.032,52 | €1.144,17 | €2.288,34 | €146,41 | €0,47 |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | 3 | €9.031,85 | €1.382,30 | €2.764,59 | €90,81 | €0,00 |
| TEST | Master Adaptive Strict3 V1 | 6 | €8.949,97 | €1.098,44 | €2.196,88 | €178,97 | €1,33 |
| TEST | Combo Adaptive Tp3 V1 | 6 | €8.938,67 | €1.316,46 | €2.632,92 | €135,71 | €0,60 |
| TEST | 1H Fast V3 Cap75 V1 | 4 | €8.905,71 | €2.836,76 | €8.510,29 | €88,77 | €43,41 |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | 4 | €8.856,60 | €1.515,93 | €3.031,86 | €176,80 | €16,43 |
| TEST | Combo Trend | 5 | €8.829,71 | €1.983,96 | €3.967,91 | €94,84 | €-245,92 |
| TEST | 1H Balanced V3 Long Only V1 | 5 | €8.783,27 | €1.585,38 | €4.756,15 | €138,14 | €-91,41 |
| TEST | Combo Mean Reversion | 2 | €8.781,83 | €1.716,82 | €3.433,64 | €88,50 | €161,29 |
| TEST | Scanner Top5 Btc Btc Le3 V1 | 6 | €8.700,64 | €2.022,17 | €4.044,33 | €174,02 | €-0,09 |
| TEST | Forza relativa 1H V1 | 6 | €8.532,23 | €1.719,48 | €3.438,97 | €132,41 | €-62,44 |
| TEST | Benchmark Bollinger mean reversion 1H | 1 | €8.328,62 | €734,84 | €1.469,68 | €41,65 | €-0,29 |

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
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €11.341,25 | €1.414,74 | 143 | 143 | 44,06% | 1,45 | €9,89 | 6,75% |
| TEST | Main Side Regime Guard V1 | Confluenza trend | €11.175,45 | €1.177,18 | 51 | 51 | 60,78% | 2,53 | €23,08 | 3,82% |
| TEST | Donchian 1H Gb20 120R V1 | Donchian breakout 20 barre | €11.074,23 | €1.145,99 | 111 | 111 | 42,34% | 1,51 | €10,32 | 6,75% |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | Momentum / breakout | €10.979,98 | €953,32 | 197 | 197 | 49,24% | 1,23 | €4,84 | 7,95% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.950,06 | €951,03 | 176 | 176 | 47,16% | 1,31 | €5,40 | 8,85% |
| TEST | Combo Trend Side Regime Guard V1 | Combo Trend | €10.790,32 | €792,30 | 155 | 155 | 50,32% | 1,27 | €5,11 | 10,10% |
| TEST | Combo Adaptive Long Only V1 | Combo Adaptive | €10.531,71 | €534,51 | 165 | 165 | 47,27% | 1,18 | €3,24 | 7,78% |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | Momentum / breakout V3 Filtered | €10.457,68 | €469,44 | 143 | 143 | 48,25% | 1,20 | €3,28 | 5,24% |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | Momentum / breakout V3 Filtered | €10.401,95 | €597,12 | 135 | 135 | 48,15% | 1,21 | €4,42 | 5,29% |
| TEST | Main Dynamic Asset Selector V1 | Confluenza trend | €10.383,82 | €303,23 | 19 | 19 | 42,11% | 1,61 | €15,96 | 3,39% |
| TEST | 1H Fast No Pepe V1 | Momentum / breakout | €10.364,13 | €573,98 | 274 | 274 | 44,16% | 1,13 | €2,09 | 9,28% |
| TEST | Combo Adaptive | Combo Adaptive | €10.363,63 | €365,07 | 207 | 207 | 46,38% | 1,11 | €1,76 | 8,17% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €10.356,85 | €553,13 | 80 | 71 | 48,75% | 1,29 | €6,91 | 3,89% |
| TEST | Scanner Top15 Long | Scanner Top15 Long | €10.352,60 | €348,42 | 197 | 197 | 47,21% | 1,11 | €1,77 | 10,31% |
| TEST | Scanner Top20 Long | Scanner Top20 Long | €10.352,60 | €348,42 | 197 | 197 | 47,21% | 1,11 | €1,77 | 10,31% |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | Momentum / breakout V3 Filtered | €10.306,08 | €398,88 | 217 | 217 | 49,31% | 1,11 | €1,84 | 9,50% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | Momentum / breakout V3 Filtered | €10.300,05 | €300,05 | 33 | 33 | 48,48% | 2,04 | €9,09 | 2,01% |
| TEST | Scanner Top5 Btc Tp3 V1 | Scanner Top 5 + forza BTC | €10.275,45 | €278,05 | 150 | 150 | 44,00% | 1,09 | €1,85 | 11,78% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | Momentum / breakout V3 Filtered | €10.271,73 | €271,73 | 22 | 22 | 50,00% | 1,74 | €12,35 | 1,72% |
| TEST | Combo Scanner | Combo Scanner | €10.271,00 | €273,01 | 187 | 187 | 43,85% | 1,08 | €1,46 | 11,38% |
| TEST | Scanner Top5 Btc Runner25 V1 | Scanner Top 5 + forza BTC | €10.269,44 | €272,04 | 154 | 154 | 44,16% | 1,09 | €1,77 | 12,06% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €10.264,72 | €266,19 | 155 | 155 | 45,16% | 1,09 | €1,72 | 11,27% |
| TEST | Rapida 1H V3 Filtered | Momentum / breakout V3 Filtered | €10.239,87 | €332,07 | 261 | 261 | 44,44% | 1,07 | €1,27 | 9,48% |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | Momentum / breakout V3 Filtered | €10.239,20 | €239,20 | 17 | 17 | 52,94% | 4,50 | €14,07 | 1,01% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €10.236,75 | €236,75 | 20 | 20 | 55,00% | 1,65 | €11,84 | 2,77% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | Momentum / breakout V3 Filtered | €10.235,18 | €235,18 | 20 | 20 | 50,00% | 1,90 | €11,76 | 2,73% |
| TEST | 1H Fast V3 No Esports Long Only V1 | Momentum / breakout V3 Filtered | €10.216,59 | €218,83 | 245 | 245 | 42,86% | 1,04 | €0,89 | 10,60% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.209,20 | €209,20 | 6 | 6 | 83,33% | 4,66 | €34,87 | 0,85% |
| TEST | Scanner Top10 Long | Scanner Top10 Long | €10.201,69 | €204,54 | 181 | 181 | 47,51% | 1,07 | €1,13 | 10,31% |
| TEST | Ampia 4H | Confluenza trend | €10.197,35 | €194,83 | 55 | 55 | 34,55% | 1,15 | €3,54 | 4,45% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | Momentum / breakout V3 Filtered | €10.185,37 | €185,37 | 22 | 22 | 40,91% | 1,57 | €8,43 | 2,27% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €10.176,68 | €191,22 | 9 | 9 | 55,56% | 2,16 | €21,25 | 1,18% |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | Momentum / breakout V3 Filtered | €10.145,12 | €145,12 | 44 | 44 | 45,45% | 1,20 | €3,30 | 2,91% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €10.143,30 | €144,72 | 7 | 7 | 42,86% | 1,87 | €20,67 | 1,61% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.108,51 | €68,27 | 3 | 3 | 66,67% | 2,25 | €22,76 | 0,91% |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | Momentum / breakout V3 Filtered | €10.099,04 | €99,04 | 55 | 55 | 54,55% | 1,12 | €1,80 | 3,59% |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | Momentum / breakout V3 Filtered | €10.090,54 | €62,48 | 165 | 165 | 44,24% | 1,02 | €0,38 | 6,64% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €10.066,52 | €66,52 | 17 | 17 | 58,82% | 1,16 | €3,91 | 3,08% |
| TEST | Combo Adaptive Partial 1R V1 | Combo Adaptive | €10.049,05 | €51,39 | 178 | 178 | 44,38% | 1,02 | €0,29 | 8,69% |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | Momentum / breakout V3 Filtered | €10.048,77 | €48,77 | 23 | 23 | 43,48% | 1,12 | €2,12 | 3,05% |
| TEST | Rapida 1H V1 | Momentum / breakout | €10.043,28 | €43,28 | 78 | 78 | 34,62% | 1,02 | €0,55 | 6,76% |
| TEST | 1H Fast Tp2 V1 | Momentum / breakout | €10.041,24 | €41,13 | 273 | 273 | 39,19% | 1,01 | €0,15 | 6,56% |
| TEST | 1H Balanced Short Trend Down Strict V1 | Confluenza trend | €10.035,46 | €35,46 | 13 | 13 | 38,46% | 1,13 | €2,73 | 1,80% |
| TEST | Scalp RSI Long 20 · prudente · 5x | Inversione RSI estrema 15m | €10.032,32 | €32,32 | 11 | 11 | 54,55% | 1,85 | €2,94 | 0,36% |
| TEST | Scalp RSI Short 85 · €50 · 15x | Inversione RSI estrema 15m | €10.022,70 | €22,70 | 6 | 6 | 66,67% | 1,87 | €3,78 | 0,31% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €10.014,08 | €14,08 | 30 | 30 | 43,33% | 1,10 | €0,47 | 0,33% |
| TEST | Scalp RSI Short 80 · €50 · 15x | Inversione RSI estrema 15m | €10.009,44 | €9,44 | 17 | 17 | 41,18% | 1,17 | €0,56 | 0,53% |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | Momentum / breakout V3 Filtered | €10.008,92 | €8,92 | 30 | 30 | 36,67% | 1,02 | €0,30 | 4,84% |
| TEST | Sol Ema 4H | Trend following EMA | €10.005,51 | €5,51 | 11 | 11 | 36,36% | 1,02 | €0,50 | 2,27% |
| TEST | Scalp RSI Short 85 · €10 · 15x | Inversione RSI estrema 15m | €10.004,54 | €4,54 | 6 | 6 | 66,67% | 1,87 | €0,76 | 0,06% |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | Momentum / breakout V3 Filtered | €10.003,37 | €3,37 | 8 | 8 | 37,50% | 1,02 | €0,42 | 2,15% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €10.002,82 | €2,82 | 30 | 30 | 43,33% | 1,10 | €0,09 | 0,07% |
| TEST | Scalp RSI Short 80 · €10 · 15x | Inversione RSI estrema 15m | €10.001,89 | €1,89 | 17 | 17 | 41,18% | 1,17 | €0,11 | 0,11% |
| TEST | Scanner Bottom5 Short Continuation V1 | Scanner Bottom5 Short Continuation | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 20 · €10 · 15x | Inversione RSI estrema 15m | €9.998,68 | €-1,32 | 11 | 11 | 36,36% | 0,74 | €-0,12 | 0,04% |
| TEST | Scalp RSI Short 85 · prudente · 5x | Inversione RSI estrema 15m | €9.996,83 | €-3,17 | 6 | 6 | 66,67% | 0,86 | €-0,53 | 0,30% |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | Momentum / breakout V3 Filtered | €9.995,23 | €-4,77 | 15 | 15 | 46,67% | 0,99 | €-0,32 | 2,70% |
| TEST | Scalp RSI Long 15 · €10 · 15x | Inversione RSI estrema 15m | €9.994,07 | €-5,93 | 4 | 4 | 25,00% | 0,06 | €-1,48 | 0,06% |
| TEST | Scalp RSI Long 20 · €50 · 15x | Inversione RSI estrema 15m | €9.993,42 | €-6,58 | 11 | 11 | 36,36% | 0,74 | €-0,60 | 0,21% |
| TEST | Doge Ema 1H | Trend following EMA | €9.989,46 | €-10,54 | 26 | 26 | 57,69% | 0,98 | €-0,41 | 2,77% |
| TEST | Scalp RSI Long 25 · €10 · 15x | Inversione RSI estrema 15m | €9.988,90 | €-11,10 | 19 | 19 | 36,84% | 0,37 | €-0,58 | 0,15% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €9.980,98 | €-19,02 | 5 | 5 | 40,00% | 0,88 | €-3,80 | 1,96% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €9.979,42 | €-20,58 | 15 | 15 | 60,00% | 0,94 | €-1,37 | 1,89% |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | €9.970,37 | €-29,63 | 4 | 4 | 25,00% | 0,06 | €-7,41 | 0,30% |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | €9.970,34 | €-29,66 | 4 | 4 | 25,00% | 0,13 | €-7,42 | 0,30% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €9.966,58 | €-33,42 | 19 | 19 | 36,84% | 0,66 | €-1,76 | 0,71% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €9.964,84 | €-35,16 | 4 | 4 | 25,00% | 0,77 | €-8,79 | 1,10% |
| TEST | Sol Ema 1H | Trend following EMA | €9.962,68 | €-37,32 | 25 | 25 | 40,00% | 0,95 | €-1,49 | 3,33% |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | Combo Adaptive | €9.959,32 | €-40,68 | 55 | 55 | 49,09% | 0,97 | €-0,74 | 4,27% |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | Momentum / breakout V3 Filtered | €9.955,32 | €-79,77 | 166 | 166 | 47,59% | 0,98 | €-0,48 | 8,44% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €9.953,87 | €-46,13 | 25 | 25 | 44,00% | 0,94 | €-1,85 | 4,59% |
| TEST | 1H Fast V3 Nohigh Range Only V1 | Momentum / breakout V3 Filtered | €9.945,30 | €106,84 | 89 | 89 | 42,70% | 1,05 | €1,20 | 7,07% |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | €9.944,51 | €-55,49 | 19 | 19 | 36,84% | 0,37 | €-2,92 | 0,77% |
| TEST | Scalp RSI Short 80 · prudente · 5x | Inversione RSI estrema 15m | €9.939,55 | €-60,45 | 17 | 17 | 35,29% | 0,39 | €-3,56 | 0,89% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €9.937,98 | €-31,42 | 9 | 9 | 44,44% | 0,86 | €-3,49 | 1,54% |
| TEST | 1H Fast Score 6 75 Range Only V1 | Momentum / breakout | €9.932,52 | €104,07 | 58 | 58 | 43,10% | 1,07 | €1,79 | 6,49% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €9.922,88 | €-77,12 | 13 | 13 | 46,15% | 0,77 | €-5,93 | 1,98% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.917,05 | €-82,95 | 30 | 30 | 43,33% | 0,52 | €-2,77 | 0,84% |
| TEST | Btc Ema 4H | Trend following EMA | €9.914,14 | €-85,86 | 5 | 5 | 20,00% | 0,58 | €-17,17 | 1,76% |
| TEST | Combo Adaptive Side Regime Guard V1 | Combo Adaptive | €9.895,17 | €-103,48 | 164 | 164 | 43,29% | 0,97 | €-0,63 | 11,68% |
| TEST | Eth Ema 4H | Trend following EMA | €9.887,95 | €-112,70 | 7 | 7 | 28,57% | 0,57 | €-16,10 | 1,83% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €9.861,10 | €-138,90 | 6 | 6 | 16,67% | 0,49 | €-23,15 | 2,43% |
| TEST | 1H Fast V3 Long Only V1 | Momentum / breakout V3 Filtered | €9.853,15 | €-175,71 | 245 | 245 | 42,45% | 0,96 | €-0,72 | 12,52% |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | Momentum / breakout V3 Filtered | €9.837,38 | €-162,62 | 37 | 37 | 40,54% | 0,76 | €-4,40 | 3,08% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €9.835,51 | €-160,30 | 140 | 133 | 40,71% | 0,95 | €-1,15 | 10,88% |
| TEST | Combo Adaptive Quality7 Regime V1 | Combo Adaptive | €9.834,05 | €-165,95 | 55 | 55 | 45,45% | 0,88 | €-3,02 | 5,41% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | Momentum / breakout V3 Filtered | €9.817,34 | €-182,66 | 24 | 24 | 41,67% | 0,64 | €-7,61 | 3,23% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.771,60 | €-228,40 | 19 | 19 | 42,11% | 0,63 | €-12,02 | 3,14% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.765,13 | €-234,87 | 17 | 17 | 41,18% | 0,62 | €-13,82 | 2,91% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | Momentum / breakout V3 Filtered | €9.762,18 | €-237,82 | 7 | 7 | 14,29% | 0,02 | €-33,97 | 2,82% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €9.731,13 | €-268,87 | 10 | 10 | 40,00% | 0,38 | €-26,89 | 4,16% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | Momentum / breakout V3 Filtered | €9.723,72 | €-276,28 | 31 | 31 | 32,26% | 0,62 | €-8,91 | 4,83% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.711,11 | €-288,89 | 18 | 18 | 33,33% | 0,56 | €-16,05 | 3,74% |
| TEST | Scanner Top5 Btc Guard V1 | Scanner Top 5 + forza BTC | €9.689,08 | €-310,52 | 145 | 145 | 38,62% | 0,90 | €-2,14 | 7,34% |
| TEST | 1H Fast Score 6 75 V1 | Momentum / breakout | €9.673,09 | €-368,21 | 197 | 197 | 41,62% | 0,93 | €-1,87 | 15,64% |
| TEST | Eth Ema 1H | Trend following EMA | €9.667,53 | €-332,47 | 28 | 28 | 39,29% | 0,63 | €-11,87 | 4,80% |
| TEST | 1H Fast V3 Nohigh V1 | Momentum / breakout V3 Filtered | €9.665,75 | €-130,13 | 176 | 176 | 44,89% | 0,96 | €-0,74 | 7,10% |
| TEST | 1H Balanced Long No Rhv V1 | Confluenza trend | €9.654,26 | €-344,06 | 125 | 125 | 44,80% | 0,85 | €-2,75 | 9,26% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.647,46 | €-352,54 | 21 | 21 | 33,33% | 0,46 | €-16,79 | 3,93% |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | Momentum / breakout | €9.646,94 | €-394,47 | 156 | 156 | 42,95% | 0,91 | €-2,53 | 15,94% |
| TEST | 1H Fast Nohigh Cap75 V1 | Momentum / breakout | €9.631,96 | €-279,18 | 199 | 199 | 40,20% | 0,93 | €-1,40 | 10,76% |
| TEST | Scanner Top5 Btc Mfe V1 | Scanner Top 5 + forza BTC | €9.622,67 | €-375,95 | 147 | 147 | 44,22% | 0,86 | €-2,56 | 12,28% |
| TEST | Master Adaptive Gb20 Be V1 | Master Adaptive Consensus | €9.622,60 | €-383,44 | 108 | 108 | 31,48% | 0,86 | €-3,55 | 8,39% |
| TEST | Master Adaptive Gb20 Partial V1 | Master Adaptive Consensus | €9.612,36 | €-393,66 | 103 | 103 | 33,98% | 0,85 | €-3,82 | 7,98% |
| TEST | Combo Adaptive Regime V1 | Combo Adaptive | €9.587,02 | €-411,80 | 84 | 84 | 46,43% | 0,80 | €-4,90 | 6,28% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | Momentum / breakout V3 Filtered | €9.579,83 | €-420,17 | 11 | 11 | 0,00% | 0,00 | €-38,20 | 4,20% |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | €9.575,18 | €-430,82 | 105 | 105 | 33,33% | 0,85 | €-4,10 | 7,80% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €9.545,31 | €-456,96 | 87 | 87 | 31,03% | 0,82 | €-5,25 | 8,44% |
| TEST | Combo Adaptive Quality7 V1 | Combo Adaptive | €9.512,30 | €-486,49 | 99 | 99 | 38,38% | 0,80 | €-4,91 | 8,88% |
| TEST | 1H Fast V3 No Esports V1 | Momentum / breakout V3 Filtered | €9.468,91 | €-445,48 | 225 | 225 | 42,22% | 0,91 | €-1,98 | 10,92% |
| TEST | Scanner Top5 Btc Guard Mfe V1 | Scanner Top 5 + forza BTC | €9.463,75 | €-535,85 | 162 | 162 | 39,51% | 0,85 | €-3,31 | 8,78% |
| TEST | Btc Ema 1H | Trend following EMA | €9.457,61 | €-514,81 | 21 | 21 | 23,81% | 0,36 | €-24,51 | 5,69% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €9.448,83 | €-557,09 | 139 | 139 | 43,17% | 0,82 | €-4,01 | 9,02% |
| TEST | Master Adaptive Gb20 Loss Cap V1 | Master Adaptive Consensus | €9.401,46 | €-598,95 | 97 | 97 | 25,77% | 0,78 | €-6,17 | 11,41% |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | Momentum / breakout | €9.392,07 | €-521,29 | 162 | 162 | 38,27% | 0,84 | €-3,22 | 10,76% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €9.370,92 | €-628,95 | 87 | 87 | 34,48% | 0,73 | €-7,23 | 7,96% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €9.328,07 | €-758,31 | 168 | 154 | 42,26% | 0,79 | €-4,51 | 11,82% |
| TEST | Scanner Bottom10 Short | Scanner Bottom10 Short | €9.320,74 | €-677,79 | 70 | 70 | 31,43% | 0,65 | €-9,68 | 9,06% |
| TEST | Scanner Bottom15 Short | Scanner Bottom15 Short | €9.320,74 | €-677,79 | 70 | 70 | 31,43% | 0,65 | €-9,68 | 9,06% |
| TEST | Scanner Bottom20 Short | Scanner Bottom20 Short | €9.320,74 | €-677,79 | 70 | 70 | 31,43% | 0,65 | €-9,68 | 9,06% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €9.286,43 | €-614,11 | 206 | 206 | 41,26% | 0,85 | €-2,98 | 14,04% |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | Scanner Bottom 5 Short | €9.256,15 | €-742,38 | 61 | 61 | 31,15% | 0,58 | €-12,17 | 9,08% |
| TEST | Scanner Bottom5 Short Profit Lock V1 | Scanner Bottom 5 Short | €9.242,07 | €-756,47 | 62 | 62 | 30,65% | 0,56 | €-12,20 | 9,08% |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | Scanner Top 5 + forza BTC | €9.219,67 | €-795,87 | 108 | 108 | 37,96% | 0,73 | €-7,37 | 11,79% |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | Momentum / breakout | €9.214,28 | €-785,35 | 146 | 146 | 38,36% | 0,78 | €-5,38 | 9,99% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €9.209,65 | €-836,01 | 101 | 101 | 33,66% | 0,73 | €-8,28 | 10,13% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.187,13 | €-811,71 | 158 | 158 | 39,24% | 0,71 | €-5,14 | 12,31% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.170,95 | €-827,60 | 89 | 89 | 31,46% | 0,64 | €-9,30 | 10,17% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €9.130,02 | €-866,26 | 181 | 181 | 38,12% | 0,75 | €-4,79 | 15,68% |
| TEST | Combo Adaptive Runner25 V1 | Combo Adaptive | €9.109,08 | €-889,87 | 146 | 146 | 35,62% | 0,69 | €-6,09 | 14,10% |
| TEST | Combo Adaptive Mfe Trail | Combo Adaptive | €9.032,52 | €-966,60 | 222 | 222 | 40,54% | 0,75 | €-4,35 | 15,45% |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | Scanner Top 5 + forza BTC | €9.031,85 | €-966,29 | 53 | 53 | 26,42% | 0,43 | €-18,23 | 12,23% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €8.949,97 | €-1.050,04 | 82 | 82 | 28,05% | 0,65 | €-12,81 | 13,60% |
| TEST | Combo Adaptive Tp3 V1 | Combo Adaptive | €8.938,67 | €-1.060,29 | 126 | 126 | 34,92% | 0,59 | €-8,42 | 14,10% |
| TEST | 1H Fast V3 Cap75 V1 | Momentum / breakout V3 Filtered | €8.905,71 | €-1.132,57 | 206 | 206 | 38,35% | 0,77 | €-5,50 | 17,41% |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | Scanner Top 5 + forza BTC | €8.856,60 | €-1.158,48 | 137 | 137 | 37,23% | 0,68 | €-8,46 | 13,91% |
| TEST | Combo Trend | Combo Trend | €8.829,71 | €-921,72 | 192 | 192 | 39,58% | 0,78 | €-4,80 | 14,08% |
| TEST | 1H Balanced V3 Long Only V1 | Confluenza trend V3 Filtered | €8.783,27 | €-1.122,66 | 160 | 160 | 41,25% | 0,64 | €-7,02 | 13,79% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €8.781,83 | €-1.377,24 | 62 | 62 | 33,87% | 0,44 | €-22,21 | 16,00% |
| TEST | Scanner Top5 Btc Btc Le3 V1 | Scanner Top 5 + forza BTC | €8.700,64 | €-1.296,65 | 111 | 111 | 36,04% | 0,56 | €-11,68 | 16,19% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €8.532,23 | €-1.402,84 | 152 | 152 | 32,89% | 0,59 | €-9,23 | 19,11% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €8.328,62 | €-1.670,21 | 113 | 113 | 39,82% | 0,54 | €-14,78 | 19,96% |

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
| Bilanciata 1H V1 | ARB | LONG | Confluenza trend | 60m | 3,0x | 0,13283 | 0,13283 | 0,12480 | 0,08922 | 0,14889 | €256,10 | €768,31 | €46,46 | €0,00 |
| Bilanciata 1H V1 | PEPE | SHORT | Confluenza trend | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €18,46 | €55,39 | €1,83 | €-2,73 |
| 1H Balanced Long No Rhv V1 | SKHYNIX | LONG | Confluenza trend | 60m | 3,0x | 1214,11277 | 1214,11277 | 1170,18211 | 815,47908 | 1301,97411 | €413,43 | €1.240,28 | €44,88 | €0,00 |
| 1H Balanced Long No Rhv V1 | BOME | LONG | Confluenza trend | 60m | 3,0x | 0,00129 | 0,00129 | 0,00114 | 0,00087 | 0,00160 | €134,98 | €404,95 | €48,59 | €0,00 |
| 1H Balanced Long No Rhv V1 | TAO | LONG | Confluenza trend | 60m | 3,0x | 247,38947 | 247,38947 | 237,94346 | 166,16326 | 266,28148 | €428,20 | €1.284,61 | €49,05 | €0,00 |
| 1H Balanced Long No Rhv V1 | HEMI | LONG | Confluenza trend | 60m | 3,0x | 0,01177 | 0,01177 | 0,01036 | 0,00790 | 0,01459 | €131,93 | €395,78 | €47,49 | €0,00 |
| 1H Balanced Long No Rhv V1 | SUI | LONG | Confluenza trend | 60m | 3,0x | 0,81626 | 0,81940 | 0,78829 | 0,54826 | 0,87220 | €44,22 | €132,67 | €4,55 | €0,51 |
| Bilanciata 1H V2 | SKHYNIX | LONG | Confluenza trend V2 | 60m | 3,0x | 1214,11277 | 1214,11277 | 1170,18211 | 815,47908 | 1301,97411 | €422,38 | €1.267,15 | €45,85 | €0,00 |
| Bilanciata 1H V2 | BTR | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,05545 | 0,05545 | 0,05545 | 0,07365 | 0,04214 | €126,95 | €380,86 | €0,00 | €-0,00 |
| Bilanciata 1H V2 | ARB | LONG | Confluenza trend V2 | 60m | 3,0x | 0,13495 | 0,13495 | 0,12685 | 0,09064 | 0,15116 | €19,71 | €59,12 | €3,55 | €0,00 |
| Bilanciata 1H V2 | SUI | LONG | Confluenza trend V2 | 60m | 3,0x | 0,81626 | 0,81940 | 0,78829 | 0,54826 | 0,87220 | €13,32 | €39,96 | €1,37 | €0,15 |
| Bilanciata 1H V2 | ZEC | LONG | Confluenza trend V2 | 60m | 3,0x | 1183,25660 | 1245,61000 | 1207,46714 | 794,75402 | 1268,83160 | €422,16 | €1.266,48 | €0,00 | €66,74 |
| Bilanciata 1H V2 | USELESS | LONG | Confluenza trend V2 | 60m | 3,0x | 0,27548 | 0,29292 | 0,24242 | 0,18503 | 0,34159 | €117,67 | €353,00 | €42,36 | €22,35 |
| Bilanciata 1H V3 Filtered | SKHYNIX | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1220,85412 | 1220,85412 | 1177,63561 | 820,00702 | 1307,29117 | €460,42 | €1.381,27 | €48,90 | €0,00 |
| Bilanciata 1H V3 Filtered | ADA | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,20138 | 0,22024 | 0,20719 | 0,26750 | 0,18976 | €559,88 | €1.679,63 | €48,45 | €-157,31 |
| Bilanciata 1H V3 Filtered | ARB | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,13283 | 0,13283 | 0,12480 | 0,08922 | 0,14889 | €262,61 | €787,82 | €47,64 | €0,00 |
| Bilanciata 1H V3 Filtered | UNI | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 7,14143 | 7,14143 | 6,87560 | 4,79666 | 7,67309 | €9,58 | €28,74 | €1,07 | €0,00 |
| Bilanciata 1H V3 Filtered | ZEC | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1183,25660 | 1245,61000 | 1207,46714 | 794,75402 | 1268,83160 | €383,72 | €1.151,16 | €0,00 | €60,66 |
| 1H Fast Score 6 75 V1 | BTR | SHORT | Momentum / breakout | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €126,75 | €380,26 | €0,00 | €-0,00 |
| 1H Fast Score 6 75 V1 | ARB | LONG | Momentum / breakout | 60m | 3,0x | 0,13189 | 0,13189 | 0,12574 | 0,08858 | 0,14110 | €21,85 | €65,56 | €3,05 | €0,00 |
| 1H Fast Score 6 75 V1 | USELESS | LONG | Momentum / breakout | 60m | 3,0x | 0,27739 | 0,29292 | 0,27739 | 0,18631 | 0,31453 | €178,54 | €535,61 | €0,00 | €30,00 |
| 1H Fast Score 6 75 V1 | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 85,62612 | 86,01300 | 84,59501 | 57,51221 | 87,17280 | €1.307,85 | €3.923,56 | €47,25 | €17,73 |
| 1H Fast Score 6 75 V1 | ETH | LONG | Momentum / breakout | 60m | 3,0x | 2504,34077 | 2503,84000 | 2476,29215 | 1682,08222 | 2546,41369 | €1.439,96 | €4.319,89 | €48,38 | €-0,86 |
| 1H Fast Score 6 75 No Trend Up V1 | BTR | SHORT | Momentum / breakout | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €123,38 | €370,15 | €0,00 | €-0,00 |
| 1H Fast Score 6 75 No Trend Up V1 | ARB | LONG | Momentum / breakout | 60m | 3,0x | 0,13189 | 0,13189 | 0,12574 | 0,08858 | 0,14110 | €21,27 | €63,82 | €2,97 | €0,00 |
| 1H Fast Score 6 75 No Trend Up V1 | USELESS | LONG | Momentum / breakout | 60m | 3,0x | 0,27739 | 0,29292 | 0,27739 | 0,18631 | 0,31453 | €178,05 | €534,15 | €0,00 | €29,91 |
| 1H Fast Score 6 75 No Trend Up V1 | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 85,62612 | 86,01300 | 84,59501 | 57,51221 | 87,17280 | €1.322,78 | €3.968,35 | €47,79 | €17,93 |
| 1H Fast Score 6 75 No Trend Up V1 | ETH | LONG | Momentum / breakout | 60m | 3,0x | 2504,34077 | 2503,84000 | 2476,29215 | 1682,08222 | 2546,41369 | €1.436,07 | €4.308,21 | €48,25 | €-0,86 |
| 1H Fast Score 6 75 Range Only V1 | ADA | SHORT | Momentum / breakout | 60m | 3,0x | 0,20260 | 0,22024 | 0,20707 | 0,26912 | 0,19589 | €765,21 | €2.295,64 | €50,71 | €-199,90 |
| 1H Fast Score 6 75 Range Only V1 | HEMI | LONG | Momentum / breakout | 60m | 3,0x | 0,01177 | 0,01177 | 0,01065 | 0,00790 | 0,01345 | €178,53 | €535,59 | €51,05 | €0,00 |
| 1H Fast Score 6 75 Range Only V1 | BTR | SHORT | Momentum / breakout | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €131,87 | €395,61 | €0,00 | €-0,00 |
| 1H Fast Score 6 75 Range Only V1 | USELESS | LONG | Momentum / breakout | 60m | 3,0x | 0,27739 | 0,29292 | 0,27739 | 0,18631 | 0,31453 | €181,51 | €544,53 | €0,00 | €30,50 |
| 1H Fast Score 6 75 Range Only V1 | ETH | LONG | Momentum / breakout | 60m | 3,0x | 2504,34077 | 2503,84000 | 2476,29215 | 1682,08222 | 2546,41369 | €23,94 | €71,81 | €0,80 | €-0,01 |
| 1H Fast Score 6 75 Cost Aware V1 | BTW | LONG | Momentum / breakout | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €8,91 | €26,72 | €3,13 | €0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00086 | 0,00146 | €215,92 | €647,76 | €57,03 | €0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | NEAR | LONG | Momentum / breakout | 60m | 3,0x | 2,08142 | 2,08142 | 2,02315 | 1,39802 | 2,16882 | €42,86 | €128,59 | €3,60 | €0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €157,13 | €471,39 | €56,57 | €-0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | BTR | SHORT | Momentum / breakout | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €150,22 | €450,66 | €0,00 | €-0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | USELESS | LONG | Momentum / breakout | 60m | 3,0x | 0,27739 | 0,29292 | 0,27739 | 0,18631 | 0,31453 | €166,68 | €500,03 | €0,00 | €28,00 |
| 1H Fast Score 6 75 Cost Aware V1 | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 85,62612 | 86,01300 | 84,59501 | 57,51221 | 87,17280 | €11,73 | €35,20 | €0,42 | €0,16 |
| 1H Fast Nohigh Cap75 V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €139,29 | €417,86 | €50,14 | €-0,00 |
| 1H Fast Nohigh Cap75 V1 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €141,57 | €424,71 | €50,14 | €-0,00 |
| 1H Fast Nohigh Cap75 V1 | BTR | SHORT | Momentum / breakout | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €135,62 | €406,85 | €0,00 | €-0,00 |
| 1H Fast Nohigh Cap75 V1 | PEPE | SHORT | Momentum / breakout | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €588,23 | €1.764,70 | €45,30 | €-87,05 |
| 1H Fast Long Btc 1 3 Cap75 V1 | PROM | LONG | Momentum / breakout | 60m | 3,0x | 6,93686 | 6,93686 | 6,39299 | 4,65926 | 7,75266 | €205,67 | €617,01 | €48,38 | €0,00 |
| 1H Fast No Pepe V1 | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €172,22 | €516,67 | €49,86 | €0,00 |
| 1H Fast No Pepe V1 | TAO | LONG | Momentum / breakout | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €47,93 | €143,78 | €4,27 | €0,00 |
| 1H Fast No Pepe V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €136,27 | €408,80 | €49,06 | €-0,00 |
| 1H Fast No Pepe V1 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €9,48 | €28,43 | €3,41 | €-0,00 |
| 1H Fast No Pepe V1 | ADA | SHORT | Momentum / breakout | 60m | 3,0x | 0,20138 | 0,22024 | 0,20590 | 0,26750 | 0,19460 | €739,08 | €2.217,23 | €49,74 | €-207,66 |
| 1H Fast No Pepe V1 | 0G | LONG | Momentum / breakout | 60m | 3,0x | 0,23904 | 0,23904 | 0,21901 | 0,16056 | 0,26909 | €210,41 | €631,23 | €52,89 | €0,00 |
| 1H Fast Tp2 V1 | BTW | LONG | Momentum / breakout | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,56752 | €142,85 | €428,56 | €50,25 | €0,00 |
| 1H Fast Tp2 V1 | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00132 | 0,00132 | 0,00119 | 0,00088 | 0,00158 | €18,87 | €56,62 | €5,59 | €0,00 |
| 1H Fast Tp2 V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,17246 | 0,17246 | 0,17246 | 0,22908 | 0,13107 | €139,71 | €419,14 | €0,00 | €-0,00 |
| 1H Fast Tp2 V1 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03379 | €141,13 | €423,40 | €50,81 | €-0,00 |
| 1H Fast Tp2 V1 | 4 | LONG | Momentum / breakout | 60m | 3,0x | 0,03351 | 0,03351 | 0,03024 | 0,02251 | 0,04003 | €142,67 | €428,01 | €41,68 | €0,00 |
| 1H Fast Tp2 V1 | USELESS | LONG | Momentum / breakout | 60m | 3,0x | 0,28018 | 0,29292 | 0,25625 | 0,18818 | 0,32802 | €8,52 | €25,56 | €2,18 | €1,16 |
| Rapida 1H V2 | ADA | SHORT | Momentum / breakout V2 | 60m | 3,0x | 0,20283 | 0,22024 | 0,20750 | 0,26943 | 0,19582 | €749,31 | €2.247,94 | €51,80 | €-192,96 |
| Rapida 1H V2 | DASH | SHORT | Momentum / breakout V2 | 60m | 3,0x | 63,23735 | 63,23735 | 65,48922 | 84,00028 | 59,85955 | €493,82 | €1.481,47 | €52,75 | €-0,00 |
| Rapida 1H V2 | ZEC | LONG | Momentum / breakout V2 | 60m | 3,0x | 1245,85912 | 1245,61000 | 1212,90668 | 836,80204 | 1295,28779 | €652,71 | €1.958,14 | €51,79 | €-0,39 |
| Rapida 1H V3 Filtered | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €172,00 | €515,99 | €49,79 | €0,00 |
| Rapida 1H V3 Filtered | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €589,98 | €1.769,95 | €52,56 | €0,00 |
| Rapida 1H V3 Filtered | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €140,02 | €420,06 | €50,41 | €-0,00 |
| Rapida 1H V3 Filtered | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €16,99 | €50,96 | €6,11 | €-0,00 |
| Rapida 1H V3 Filtered | PEPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €633,48 | €1.900,43 | €47,75 | €-89,30 |
| 1H Fast V3 Cap75 V1 | BTR | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €122,50 | €367,49 | €0,00 | €-0,00 |
| 1H Fast V3 Cap75 V1 | USELESS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,27739 | 0,29292 | 0,27739 | 0,18631 | 0,31453 | €164,37 | €493,10 | €0,00 | €27,62 |
| 1H Fast V3 Cap75 V1 | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 85,62612 | 86,01300 | 84,59501 | 57,51221 | 87,17280 | €1.224,17 | €3.672,52 | €44,22 | €16,59 |
| 1H Fast V3 Cap75 V1 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2504,34077 | 2503,84000 | 2476,29215 | 1682,08222 | 2546,41369 | €1.325,73 | €3.977,18 | €44,54 | €-0,80 |
| 1H Fast V3 Nohigh V1 | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €131,05 | €393,14 | €47,18 | €-0,00 |
| 1H Fast V3 Nohigh V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €133,20 | €399,59 | €47,18 | €-0,00 |
| 1H Fast V3 Nohigh V1 | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,20138 | 0,22024 | 0,20590 | 0,26750 | 0,19460 | €719,57 | €2.158,72 | €48,43 | €-202,18 |
| 1H Fast V3 Nohigh V1 | 0G | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,23904 | 0,23904 | 0,21901 | 0,16056 | 0,26909 | €196,32 | €588,95 | €49,35 | €0,00 |
| 1H Fast V3 Nohigh V1 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2504,34077 | 2503,84000 | 2476,29215 | 1682,08222 | 2546,41369 | €35,43 | €106,28 | €1,19 | €-0,02 |
| 1H Fast V3 Long Only V1 | BTW | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €126,57 | €379,72 | €44,52 | €0,00 |
| 1H Fast V3 Long Only V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00147 | €9,56 | €28,69 | €2,66 | €0,00 |
| 1H Fast V3 Long Only V1 | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €554,42 | €1.663,26 | €49,39 | €0,00 |
| 1H Fast V3 Long Only V1 | HEMI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01177 | 0,01177 | 0,01065 | 0,00790 | 0,01345 | €170,60 | €511,79 | €48,79 | €0,00 |
| 1H Fast V3 Long Only V1 | USELESS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,27739 | 0,29292 | 0,27739 | 0,18631 | 0,31453 | €183,34 | €550,03 | €0,00 | €30,80 |
| 1H Fast V3 Long Only V1 | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 85,62612 | 86,01300 | 84,59501 | 57,51221 | 87,17280 | €10,62 | €31,85 | €0,38 | €0,14 |
| 1H Fast V3 Long Only V1 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2504,34077 | 2503,84000 | 2476,29215 | 1682,08222 | 2546,41369 | €66,05 | €198,15 | €2,22 | €-0,04 |
| 1H Fast V3 Long Nohigh Cap75 V1 | HEMI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01177 | 0,01177 | 0,01065 | 0,00790 | 0,01345 | €166,97 | €500,92 | €47,75 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 V1 | PROM | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 6,92735 | 6,92735 | 6,35093 | 4,65287 | 7,79198 | €195,87 | €587,60 | €48,89 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 V1 | USELESS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,27739 | 0,29292 | 0,27739 | 0,18631 | 0,31453 | €186,51 | €559,53 | €0,00 | €31,34 |
| 1H Fast V3 Long Nohigh Cap75 V1 | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 85,62612 | 86,01300 | 84,59501 | 57,51221 | 87,17280 | €115,33 | €346,00 | €4,17 | €1,56 |
| 1H Fast V3 Long Nohigh Cap75 V1 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2504,34077 | 2503,84000 | 2476,29215 | 1682,08222 | 2546,41369 | €1.502,11 | €4.506,32 | €50,47 | €-0,90 |
| 1H Fast V3 No Esports V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €169,36 | €508,09 | €49,03 | €0,00 |
| 1H Fast V3 No Esports V1 | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €27,04 | €81,13 | €2,41 | €0,00 |
| 1H Fast V3 No Esports V1 | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €133,96 | €401,88 | €48,23 | €-0,00 |
| 1H Fast V3 No Esports V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €129,73 | €389,20 | €46,70 | €-0,00 |
| 1H Fast V3 No Esports V1 | PEPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €593,05 | €1.779,15 | €44,70 | €-83,60 |
| 1H Fast V3 No Esports Long Only V1 | BTW | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €132,94 | €398,81 | €46,76 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00147 | €10,06 | €30,18 | €2,80 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | HEMI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01177 | 0,01177 | 0,01065 | 0,00790 | 0,01345 | €175,30 | €525,91 | €50,13 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | PROM | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 6,92735 | 6,92735 | 6,35093 | 4,65287 | 7,79198 | €9,71 | €29,12 | €2,42 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | 0G | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,23904 | 0,23904 | 0,21901 | 0,16056 | 0,26909 | €187,89 | €563,68 | €47,23 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | USELESS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,27548 | 0,29292 | 0,27548 | 0,18503 | 0,31405 | €11,54 | €34,63 | €0,00 | €2,19 |
| 1H Fast V3 No Esports Long Only V1 | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 85,62612 | 86,01300 | 84,59501 | 57,51221 | 87,17280 | €13,68 | €41,03 | €0,49 | €0,19 |
| 1H Fast V3 No Esports Long Only V1 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2504,34077 | 2503,84000 | 2476,29215 | 1682,08222 | 2546,41369 | €1.520,87 | €4.562,61 | €51,10 | €-0,91 |
| 1H Fast V3 No Esports Mfe Lock V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €173,11 | €519,32 | €50,11 | €0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €593,79 | €1.781,38 | €52,90 | €0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €140,93 | €422,78 | €50,73 | €-0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €17,09 | €51,28 | €6,15 | €-0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | PEPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €637,57 | €1.912,72 | €48,06 | €-89,88 |
| 1H Fast V3 No Esports Stress Guard V1 | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,20283 | 0,22024 | 0,20750 | 0,26943 | 0,19582 | €739,04 | €2.217,11 | €51,09 | €-190,31 |
| 1H Fast V3 No Esports Stress Guard V1 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2504,34077 | 2503,84000 | 2476,29215 | 1682,08222 | 2546,41369 | €1.548,46 | €4.645,39 | €52,03 | €-0,93 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | HEMI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01177 | 0,01177 | 0,01065 | 0,00790 | 0,01345 | €163,25 | €489,75 | €46,69 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | PROM | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 6,92735 | 6,92735 | 6,35093 | 4,65287 | 7,79198 | €191,37 | €574,11 | €47,77 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | XRP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,42851 | 1,43158 | 1,40948 | 0,95948 | 1,45705 | €1.240,21 | €3.720,62 | €49,57 | €8,01 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | USELESS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,27739 | 0,29292 | 0,25262 | 0,18631 | 0,31453 | €184,49 | €553,48 | €49,41 | €31,00 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2504,34077 | 2503,84000 | 2476,29215 | 1682,08222 | 2546,41369 | €169,21 | €507,62 | €5,69 | €-0,10 |
| Ampia 4H | SPCX | LONG | Confluenza trend | 240m | 2,0x | 136,56189 | 136,56189 | 126,46637 | 68,96375 | 164,82935 | €323,86 | €647,73 | €47,88 | €0,00 |
| Ampia 4H | VELVET | LONG | Confluenza trend | 240m | 2,0x | 0,55987 | 0,55987 | 0,49269 | 0,28274 | 0,74799 | €201,63 | €403,26 | €48,39 | €0,00 |
| Ampia 4H | LINK | LONG | Confluenza trend | 240m | 2,0x | 11,96839 | 11,96839 | 11,08055 | 6,04404 | 14,45436 | €14,07 | €28,15 | €2,09 | €0,00 |
| Ampia 4H | ETH | LONG | Confluenza trend | 240m | 2,0x | 2430,03591 | 2503,84000 | 2267,54364 | 1227,16813 | 2885,01426 | €18,82 | €37,65 | €2,52 | €1,14 |
| Ampia 4H | HYPE | LONG | Confluenza trend | 240m | 2,0x | 79,31286 | 86,01300 | 70,73982 | 40,05299 | 103,31737 | €13,82 | €27,64 | €2,99 | €2,33 |
| Ampia 4H | TRUMP | LONG | Confluenza trend | 240m | 2,0x | 2,37347 | 2,37347 | 2,08866 | 1,19860 | 3,17096 | €210,83 | €421,66 | €50,60 | €0,00 |
| Ampia 4H | SOL | LONG | Confluenza trend | 240m | 2,0x | 103,77875 | 104,18000 | 96,79200 | 52,40827 | 123,34165 | €13,62 | €27,23 | €1,83 | €0,11 |
| Ampia 4H | XRP | LONG | Confluenza trend | 240m | 2,0x | 1,42001 | 1,43158 | 1,35851 | 0,71711 | 1,59222 | €12,52 | €25,04 | €1,08 | €0,20 |
| Ampia 4H | UNI | LONG | Confluenza trend | 240m | 2,0x | 6,98040 | 6,98040 | 6,22147 | 3,52510 | 9,10539 | €214,19 | €428,38 | €46,57 | €0,00 |
| Forza relativa 1H V1 | BTR | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,05109 | 0,05109 | 0,05109 | 0,07638 | 0,03760 | €174,72 | €349,43 | €0,00 | €-0,00 |
| Forza relativa 1H V1 | ARB | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,15050 | €352,71 | €705,43 | €42,65 | €0,00 |
| Forza relativa 1H V1 | PEPE | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00001 | 0,00000 | €661,53 | €1.323,06 | €41,35 | €-62,44 |
| Forza relativa 1H V1 | NEAR | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 2,37648 | 2,37648 | 2,26708 | 1,20012 | 2,61715 | €474,73 | €949,47 | €43,71 | €0,00 |
| Forza relativa 1H V1 | UNI | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 7,16543 | 7,16543 | 6,92567 | 3,61854 | 7,69291 | €13,42 | €26,84 | €0,90 | €0,00 |
| Forza relativa 1H V1 | DASH | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 63,17736 | 63,17736 | 66,00780 | 94,45016 | 56,95039 | €42,37 | €84,74 | €3,80 | €-0,00 |
| Forza relativa 1H V2 | BEAT | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,25984 | 0,25984 | 0,25657 | 0,38847 | 0,19125 | €200,38 | €400,75 | €0,00 | €-0,00 |
| Forza relativa 1H V2 | TUT | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,04452 | 0,04452 | 0,04986 | 0,06656 | 0,03277 | €204,64 | €409,28 | €49,11 | €-0,00 |
| Forza relativa 1H V2 | ADA | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,20283 | 0,22024 | 0,20884 | 0,30323 | 0,18961 | €17,52 | €35,04 | €1,04 | €-3,01 |
| Forza relativa 1H V2 | HEMI | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €200,86 | €401,72 | €48,21 | €0,00 |
| Forza relativa 1H V2 | BTR | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,05109 | 0,05109 | 0,05109 | 0,07638 | 0,03760 | €205,02 | €410,03 | €0,00 | €-0,00 |
| Forza relativa 1H V2 | SUI | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,81626 | 0,81940 | 0,78829 | 0,41221 | 0,87780 | €16,29 | €32,59 | €1,12 | €0,13 |
| Benchmark Donchian breakout 1H | SKHYNIX | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1174,33482 | 1174,33482 | 1128,44989 | 593,03908 | 1289,04713 | €641,25 | €1.282,50 | €50,11 | €0,00 |
| Benchmark Donchian breakout 1H | VELVET | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,14787 | 0,14787 | 0,16561 | 0,22107 | 0,10351 | €237,23 | €474,47 | €56,94 | €-0,00 |
| Benchmark Donchian breakout 1H | ADA | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,20283 | 0,22024 | 0,20951 | 0,30323 | 0,18614 | €72,87 | €145,74 | €4,80 | €-12,51 |
| Benchmark Donchian breakout 1H | PEPE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00001 | 0,00000 | €794,09 | €1.588,18 | €58,23 | €-78,34 |
| Benchmark Donchian breakout 1H | BTC | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 78821,06263 | 79104,63000 | 80082,19964 | 117837,48864 | 75668,22013 | €123,54 | €247,07 | €3,95 | €-0,89 |
| Benchmark Donchian breakout 1H | HYPE | LONG | Donchian breakout 20 barre | 60m | 2,0x | 85,41008 | 86,01300 | 83,92864 | 43,13209 | 89,11368 | €1.520,14 | €3.040,29 | €52,73 | €21,46 |
| Donchian 1H Gb20 120R V1 | SKHYNIX | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1174,33482 | 1174,33482 | 1128,44989 | 593,03908 | 1289,04713 | €626,15 | €1.252,30 | €48,93 | €0,00 |
| Donchian 1H Gb20 120R V1 | VELVET | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,14787 | 0,14787 | 0,16561 | 0,22107 | 0,10351 | €231,65 | €463,30 | €55,60 | €-0,00 |
| Donchian 1H Gb20 120R V1 | ADA | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,20283 | 0,22024 | 0,20951 | 0,30323 | 0,18614 | €71,16 | €142,31 | €4,68 | €-12,22 |
| Donchian 1H Gb20 120R V1 | PEPE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00001 | 0,00000 | €775,40 | €1.550,79 | €56,86 | €-76,50 |
| Donchian 1H Gb20 120R V1 | BTC | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 78821,06263 | 79104,63000 | 80082,19964 | 117837,48864 | 75668,22013 | €120,63 | €241,25 | €3,86 | €-0,87 |
| Donchian 1H Gb20 120R V1 | HYPE | LONG | Donchian breakout 20 barre | 60m | 2,0x | 85,41008 | 86,01300 | 83,92864 | 43,13209 | 89,11368 | €1.484,35 | €2.968,70 | €51,49 | €20,96 |
| Benchmark Bollinger mean reversion 1H | ZEC | SHORT | Bollinger mean reversion | 60m | 2,0x | 1245,36088 | 1245,61000 | 1280,65295 | 1861,81451 | 1192,42278 | €734,84 | €1.469,68 | €41,65 | €-0,29 |
| Benchmark trend following EMA 1H | BEAT | SHORT | Trend following EMA | 60m | 2,0x | 0,28257 | 0,28257 | 0,25706 | 0,42244 | 0,20797 | €186,11 | €372,23 | €0,00 | €-0,00 |
| Benchmark trend following EMA 1H | TUT | SHORT | Trend following EMA | 60m | 2,0x | 0,04446 | 0,04446 | 0,04980 | 0,06647 | 0,03272 | €194,70 | €389,39 | €46,73 | €-0,00 |
| Benchmark trend following EMA 1H | VELVET | SHORT | Trend following EMA | 60m | 2,0x | 0,14786 | 0,14786 | 0,16560 | 0,22105 | 0,10883 | €187,91 | €375,83 | €45,10 | €-0,00 |
| Benchmark trend following EMA 1H | ARB | LONG | Trend following EMA | 60m | 2,0x | 0,13283 | 0,13283 | 0,12390 | 0,06708 | 0,15246 | €341,57 | €683,14 | €45,90 | €0,00 |
| Benchmark trend following EMA 1H | UNI | LONG | Trend following EMA | 60m | 2,0x | 7,07742 | 7,07742 | 6,75804 | 3,57409 | 7,78005 | €71,53 | €143,05 | €6,46 | €0,00 |
| Scanner Top 5 Long 1H | BOME | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00160 | €218,24 | €436,47 | €52,38 | €0,00 |
| Scanner Top 5 Long 1H | TRUMP | LONG | Scanner Top 5 Long | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,08367 | €238,89 | €477,78 | €55,13 | €0,00 |
| Scanner Top 5 Long 1H | SKHYNIX | LONG | Scanner Top 5 Long | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1331,36020 | €17,74 | €35,49 | €0,91 | €0,00 |
| Scanner Top 5 Long 1H | HEMI | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €228,24 | €456,48 | €54,78 | €0,00 |
| Scanner Top 5 Long 1H | ARB | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,14889 | €453,65 | €907,29 | €54,86 | €0,00 |
| Scanner Top 5 Long 1H | SUI | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,81626 | 0,81940 | 0,78829 | 0,41221 | 0,87220 | €79,54 | €159,09 | €5,45 | €0,61 |
| Scanner Bottom 5 Short 1H | SOXL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €378,86 | €757,72 | €48,07 | €-0,00 |
| Scanner Bottom 5 Short 1H | SNDK | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €492,80 | €985,60 | €47,71 | €-0,00 |
| Scanner Bottom 5 Short 1H | VELVET | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €191,07 | €382,14 | €0,00 | €-0,00 |
| Scanner Bottom 5 Short 1H | TUT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €178,38 | €356,76 | €42,81 | €-0,00 |
| Scanner Top10 Long | TAO | LONG | Scanner Top10 Long | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €678,43 | €1.356,86 | €51,81 | €0,00 |
| Scanner Top10 Long | SKHYNIX | LONG | Scanner Top10 Long | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €972,86 | €1.945,72 | €48,38 | €0,00 |
| Scanner Top10 Long | HEMI | LONG | Scanner Top10 Long | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €207,88 | €415,77 | €49,89 | €0,00 |
| Scanner Top10 Long | ARB | LONG | Scanner Top10 Long | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,14889 | €422,09 | €844,19 | €51,04 | €0,00 |
| Scanner Top10 Long | UNI | LONG | Scanner Top10 Long | 60m | 2,0x | 7,14143 | 7,14143 | 6,87560 | 3,60642 | 7,67309 | €15,10 | €30,20 | €1,12 | €0,00 |
| Scanner Top10 Long | XRP | LONG | Scanner Top10 Long | 60m | 2,0x | 1,43187 | 1,43158 | 1,40917 | 0,72309 | 1,47725 | €56,26 | €112,52 | €1,78 | €-0,02 |
| Scanner Bottom10 Short | SOXL | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom10 Short | SNDK | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Bottom10 Short | VELVET | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €194,19 | €388,38 | €0,00 | €-0,00 |
| Scanner Bottom10 Short | TUT | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €181,31 | €362,61 | €43,51 | €-0,00 |
| Scanner Top15 Long | NEAR | LONG | Scanner Top15 Long | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €16,79 | €33,59 | €1,21 | €0,00 |
| Scanner Top15 Long | TAO | LONG | Scanner Top15 Long | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €88,53 | €177,07 | €6,76 | €0,00 |
| Scanner Top15 Long | TRUMP | LONG | Scanner Top15 Long | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,08367 | €215,87 | €431,75 | €49,81 | €0,00 |
| Scanner Top15 Long | SKHYNIX | LONG | Scanner Top15 Long | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €787,36 | €1.574,72 | €39,16 | €0,00 |
| Scanner Top15 Long | ARB | LONG | Scanner Top15 Long | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,14889 | €426,02 | €852,04 | €51,52 | €0,00 |
| Scanner Top15 Long | UNI | LONG | Scanner Top15 Long | 60m | 2,0x | 7,12843 | 7,12843 | 6,87194 | 3,59985 | 7,64140 | €88,01 | €176,02 | €6,33 | €0,00 |
| Scanner Top15 Long | SUI | LONG | Scanner Top15 Long | 60m | 2,0x | 0,81626 | 0,81940 | 0,78829 | 0,41221 | 0,87220 | €69,90 | €139,81 | €4,79 | €0,54 |
| Scanner Top15 Long | USELESS | LONG | Scanner Top15 Long | 60m | 2,0x | 0,28937 | 0,29292 | 0,26165 | 0,14613 | 0,34480 | €247,12 | €494,24 | €47,34 | €6,07 |
| Scanner Bottom15 Short | SOXL | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom15 Short | SNDK | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Bottom15 Short | VELVET | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €194,19 | €388,38 | €0,00 | €-0,00 |
| Scanner Bottom15 Short | TUT | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €181,31 | €362,61 | €43,51 | €-0,00 |
| Scanner Top20 Long | NEAR | LONG | Scanner Top20 Long | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €16,79 | €33,59 | €1,21 | €0,00 |
| Scanner Top20 Long | TAO | LONG | Scanner Top20 Long | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €88,53 | €177,07 | €6,76 | €0,00 |
| Scanner Top20 Long | TRUMP | LONG | Scanner Top20 Long | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,08367 | €215,87 | €431,75 | €49,81 | €0,00 |
| Scanner Top20 Long | SKHYNIX | LONG | Scanner Top20 Long | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €787,36 | €1.574,72 | €39,16 | €0,00 |
| Scanner Top20 Long | ARB | LONG | Scanner Top20 Long | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,14889 | €426,02 | €852,04 | €51,52 | €0,00 |
| Scanner Top20 Long | UNI | LONG | Scanner Top20 Long | 60m | 2,0x | 7,12843 | 7,12843 | 6,87194 | 3,59985 | 7,64140 | €88,01 | €176,02 | €6,33 | €0,00 |
| Scanner Top20 Long | SUI | LONG | Scanner Top20 Long | 60m | 2,0x | 0,81626 | 0,81940 | 0,78829 | 0,41221 | 0,87220 | €69,90 | €139,81 | €4,79 | €0,54 |
| Scanner Top20 Long | USELESS | LONG | Scanner Top20 Long | 60m | 2,0x | 0,28937 | 0,29292 | 0,26165 | 0,14613 | 0,34480 | €247,12 | €494,24 | €47,34 | €6,07 |
| Scanner Bottom20 Short | SOXL | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom20 Short | SNDK | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Bottom20 Short | VELVET | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €194,19 | €388,38 | €0,00 | €-0,00 |
| Scanner Bottom20 Short | TUT | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €181,31 | €362,61 | €43,51 | €-0,00 |
| Scanner Top 5 + forza BTC 1H | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €203,45 | €406,91 | €48,83 | €0,00 |
| Scanner Top 5 + forza BTC 1H | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,14149 | €223,03 | €446,06 | €51,47 | €0,00 |
| Scanner Top 5 + forza BTC 1H | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €18,23 | €36,45 | €0,93 | €0,00 |
| Scanner Top 5 + forza BTC 1H | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €213,35 | €426,70 | €51,20 | €0,00 |
| Scanner Top 5 + forza BTC 1H | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,15050 | €424,88 | €849,77 | €51,38 | €0,00 |
| Scanner Top 5 + forza BTC 1H | UNI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 7,09542 | 7,09542 | 6,78408 | 3,58319 | 7,78036 | €17,99 | €35,98 | €1,58 | €0,00 |
| Scanner Top 5 + forza BTC 1H | NEAR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,37648 | 2,37648 | 2,26708 | 1,20012 | 2,61715 | €69,93 | €139,86 | €6,44 | €0,00 |
| Scanner Top5 Btc Mfe V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €190,73 | €381,46 | €45,77 | €0,00 |
| Scanner Top5 Btc Mfe V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,14149 | €209,08 | €418,16 | €48,25 | €0,00 |
| Scanner Top5 Btc Mfe V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €17,09 | €34,17 | €0,88 | €0,00 |
| Scanner Top5 Btc Mfe V1 | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €200,01 | €400,01 | €48,00 | €0,00 |
| Scanner Top5 Btc Mfe V1 | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,15050 | €398,31 | €796,61 | €48,17 | €0,00 |
| Scanner Top5 Btc Mfe V1 | UNI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 7,09542 | 7,09542 | 6,78408 | 3,58319 | 7,78036 | €16,86 | €33,73 | €1,48 | €0,00 |
| Scanner Top5 Btc Mfe V1 | NEAR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,37648 | 2,37648 | 2,26708 | 1,20012 | 2,61715 | €65,55 | €131,11 | €6,04 | €0,00 |
| Scanner Top5 Btc Guard V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €197,27 | €394,55 | €47,35 | €0,00 |
| Scanner Top5 Btc Guard V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,55551 | 2,55551 | 2,29388 | 1,29053 | 3,13109 | €13,03 | €26,06 | €2,67 | €0,00 |
| Scanner Top5 Btc Guard V1 | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €195,03 | €390,06 | €46,81 | €0,00 |
| Scanner Top5 Btc Guard V1 | ZORA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00942 | 0,00942 | 0,00829 | 0,00476 | 0,01191 | €192,06 | €384,12 | €46,09 | €0,00 |
| Scanner Top5 Btc Guard V1 | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,15050 | €401,05 | €802,11 | €48,50 | €0,00 |
| Scanner Top5 Btc Guard V1 | SUI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,81626 | 0,81940 | 0,78829 | 0,41221 | 0,87780 | €53,12 | €106,24 | €3,64 | €0,41 |
| Scanner Top5 Btc Btc Le3 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €847,75 | €1.695,49 | €43,45 | €0,00 |
| Scanner Top5 Btc Btc Le3 V1 | 0G | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,24373 | 0,24373 | 0,21916 | 0,12308 | 0,29778 | €215,80 | €431,60 | €43,51 | €0,00 |
| Scanner Top5 Btc Btc Le3 V1 | NEAR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,37648 | 2,37648 | 2,26708 | 1,20012 | 2,61715 | €466,33 | €932,66 | €42,93 | €0,00 |
| Scanner Top5 Btc Btc Le3 V1 | UNI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 7,16543 | 7,16543 | 6,92567 | 3,61854 | 7,69291 | €17,38 | €34,75 | €1,16 | €0,00 |
| Scanner Top5 Btc Btc Le3 V1 | WLD | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,46919 | 0,46919 | 0,44675 | 0,23694 | 0,51857 | €433,72 | €867,43 | €41,49 | €0,00 |
| Scanner Top5 Btc Btc Le3 V1 | XRP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,43312 | 1,43158 | 1,40753 | 0,72372 | 1,48940 | €41,20 | €82,39 | €1,47 | €-0,09 |
| Scanner Top5 Btc Btc 2 3 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €891,28 | €1.782,56 | €45,68 | €0,00 |
| Scanner Top5 Btc Btc 2 3 V1 | UNI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 7,09542 | 7,09542 | 6,78408 | 3,58319 | 7,78036 | €17,98 | €35,96 | €1,58 | €0,00 |
| Scanner Top5 Btc Btc 2 3 V1 | NEAR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,37648 | 2,37648 | 2,26708 | 1,20012 | 2,61715 | €473,04 | €946,07 | €43,55 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €192,69 | €385,37 | €46,24 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,55551 | 2,55551 | 2,29388 | 1,29053 | 3,13109 | €12,72 | €25,45 | €2,61 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €190,49 | €380,99 | €45,72 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | ZORA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00942 | 0,00942 | 0,00829 | 0,00476 | 0,01191 | €187,59 | €375,19 | €45,02 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,15050 | €391,73 | €783,45 | €47,37 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | SUI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,81626 | 0,81940 | 0,78829 | 0,41221 | 0,87780 | €51,89 | €103,77 | €3,56 | €0,40 |
| Scanner Top5 Btc Guard Btc Le3 V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,55551 | 2,55551 | 2,29388 | 1,29053 | 3,13109 | €12,70 | €25,40 | €2,60 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €191,20 | €382,39 | €45,89 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | PROM | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 7,01991 | 7,01991 | 6,30832 | 3,54505 | 8,58541 | €213,89 | €427,78 | €43,36 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | ZORA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00942 | 0,00942 | 0,00829 | 0,00476 | 0,01191 | €188,34 | €376,68 | €45,20 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | NEAR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,37648 | 2,37648 | 2,26708 | 1,20012 | 2,61715 | €32,15 | €64,31 | €2,96 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | UNI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 7,14143 | 7,14143 | 6,87560 | 3,60642 | 7,72626 | €12,97 | €25,94 | €0,97 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | USELESS | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,28110 | 0,29292 | 0,24944 | 0,14195 | 0,35074 | €191,32 | €382,64 | €43,09 | €16,10 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | ZORA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00942 | 0,00942 | 0,00829 | 0,00476 | 0,01191 | €185,37 | €370,74 | €44,49 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | LINK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 13,22564 | 13,22564 | 12,79229 | 6,67895 | 14,17903 | €673,21 | €1.346,41 | €44,12 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | WLD | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,46919 | 0,46919 | 0,44675 | 0,23694 | 0,51857 | €462,02 | €924,05 | €44,20 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | USELESS | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,28110 | 0,29292 | 0,24944 | 0,14195 | 0,35074 | €195,33 | €390,66 | €44,00 | €16,43 |
| Scanner Top5 Btc Runner25 V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00176 | €210,95 | €421,90 | €50,63 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1363,81560 | €965,52 | €1.931,04 | €49,49 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01601 | €209,51 | €419,03 | €50,28 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,15692 | €27,23 | €54,45 | €3,29 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | UNI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 7,09542 | 7,09542 | 6,78408 | 3,58319 | 8,02944 | €21,18 | €42,36 | €1,86 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | NEAR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,37648 | 2,37648 | 2,26708 | 1,20012 | 2,70466 | €545,89 | €1.091,78 | €50,26 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00176 | €211,07 | €422,14 | €50,66 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1363,81560 | €966,09 | €1.932,17 | €49,52 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01601 | €209,64 | €419,27 | €50,31 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,15692 | €27,24 | €54,49 | €3,29 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | UNI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 7,09542 | 7,09542 | 6,78408 | 3,58319 | 8,02944 | €21,19 | €42,39 | €1,86 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | NEAR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,37648 | 2,37648 | 2,26708 | 1,20012 | 2,70466 | €546,21 | €1.092,42 | €50,29 | €0,00 |
| Combo Trend | BEAT | SHORT | Combo Trend | 60m | 2,0x | 0,25984 | 0,25984 | 0,25657 | 0,38847 | 0,19125 | €193,71 | €387,42 | €0,00 | €-0,00 |
| Combo Trend | ADA | SHORT | Combo Trend | 60m | 2,0x | 0,19986 | 0,22024 | 0,20356 | 0,29879 | 0,19173 | €1.205,82 | €2.411,64 | €44,61 | €-245,92 |
| Combo Trend | BTR | SHORT | Combo Trend | 60m | 2,0x | 0,05109 | 0,05109 | 0,05109 | 0,07638 | 0,03760 | €188,04 | €376,08 | €0,00 | €-0,00 |
| Combo Trend | ARB | LONG | Combo Trend | 60m | 2,0x | 0,13283 | 0,13283 | 0,12390 | 0,06708 | 0,15246 | €327,77 | €655,53 | €44,04 | €0,00 |
| Combo Trend | UNI | LONG | Combo Trend | 60m | 2,0x | 7,07742 | 7,07742 | 6,75804 | 3,57409 | 7,78005 | €68,62 | €137,24 | €6,19 | €0,00 |
| Combo Mean Reversion | ADA | LONG | Combo Mean Reversion | 60m | 2,0x | 0,20284 | 0,22024 | 0,19804 | 0,10244 | 0,21052 | €942,00 | €1.883,99 | €44,59 | €161,60 |
| Combo Mean Reversion | ZEC | SHORT | Combo Mean Reversion | 60m | 2,0x | 1245,36088 | 1245,61000 | 1280,65295 | 1861,81451 | 1188,89356 | €774,83 | €1.549,65 | €43,92 | €-0,31 |
| Combo Scanner | BOME | LONG | Combo Scanner | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €195,20 | €390,40 | €46,85 | €0,00 |
| Combo Scanner | TRUMP | LONG | Combo Scanner | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,14149 | €213,98 | €427,96 | €49,38 | €0,00 |
| Combo Scanner | SKHYNIX | LONG | Combo Scanner | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €24,78 | €49,55 | €1,27 | €0,00 |
| Combo Scanner | ARB | LONG | Combo Scanner | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,15050 | €419,07 | €838,14 | €50,68 | €0,00 |
| Combo Scanner | UNI | LONG | Combo Scanner | 60m | 2,0x | 7,09542 | 7,09542 | 6,78408 | 3,58319 | 7,78036 | €583,31 | €1.166,62 | €51,19 | €0,00 |
| Combo Scanner | NEAR | LONG | Combo Scanner | 60m | 2,0x | 2,37648 | 2,37648 | 2,26708 | 1,20012 | 2,61715 | €21,23 | €42,45 | €1,95 | €0,00 |
| Combo Scanner | TAO | LONG | Combo Scanner | 60m | 2,0x | 264,91297 | 264,91297 | 254,31765 | 133,78105 | 288,22268 | €105,11 | €210,22 | €8,41 | €0,00 |
| Combo Adaptive | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,01735 | 121,01735 | 128,90956 | 180,92093 | 105,23292 | €367,30 | €734,61 | €47,91 | €-0,00 |
| Combo Adaptive | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €40,89 | €81,77 | €3,12 | €0,00 |
| Combo Adaptive | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,52450 | 2,33981 | 1,27487 | 2,89389 | €18,69 | €37,37 | €2,73 | €0,00 |
| Combo Adaptive | 0G | LONG | Combo Adaptive | 60m | 2,0x | 0,23904 | 0,23904 | 0,21329 | 0,12072 | 0,29055 | €230,13 | €460,26 | €49,58 | €0,00 |
| Combo Adaptive | BTR | SHORT | Combo Adaptive | 60m | 2,0x | 0,04853 | 0,04853 | 0,04853 | 0,07255 | 0,03688 | €212,51 | €425,02 | €0,00 | €-0,00 |
| Combo Adaptive | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,14889 | €420,61 | €841,21 | €50,86 | €0,00 |
| Combo Adaptive | UNI | LONG | Combo Adaptive | 60m | 2,0x | 7,16543 | 7,16543 | 6,92567 | 3,61854 | 7,64496 | €12,79 | €25,58 | €0,86 | €0,00 |
| Combo Adaptive | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 85,62612 | 86,01300 | 84,30040 | 43,24119 | 88,27757 | €38,63 | €77,27 | €1,20 | €0,35 |
| Combo Adaptive Mfe Trail | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €54,29 | €108,58 | €4,15 | €0,00 |
| Combo Adaptive Mfe Trail | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,52450 | 2,33981 | 1,27487 | 2,89389 | €315,75 | €631,50 | €46,20 | €0,00 |
| Combo Adaptive Mfe Trail | TUT | SHORT | Combo Adaptive | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €190,04 | €380,09 | €45,61 | €-0,00 |
| Combo Adaptive Mfe Trail | PROM | LONG | Combo Adaptive | 60m | 2,0x | 7,01991 | 7,01991 | 6,30832 | 3,54505 | 8,44309 | €21,72 | €43,45 | €4,40 | €0,00 |
| Combo Adaptive Mfe Trail | BTR | SHORT | Combo Adaptive | 60m | 2,0x | 0,04991 | 0,04991 | 0,04841 | 0,07462 | 0,03793 | €142,63 | €285,27 | €0,00 | €-0,00 |
| Combo Adaptive Mfe Trail | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,14889 | €367,37 | €734,74 | €44,43 | €0,00 |
| Combo Adaptive Mfe Trail | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 85,62612 | 86,01300 | 84,30040 | 43,24119 | 88,27757 | €52,35 | €104,71 | €1,62 | €0,47 |
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
| Combo Adaptive Long Only V1 | UNI | LONG | Combo Adaptive | 60m | 2,0x | 7,16543 | 7,16543 | 6,92567 | 3,61854 | 7,64496 | €15,48 | €30,96 | €1,04 | €0,00 |
| Combo Adaptive Partial 1R V1 | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,01735 | 121,01735 | 128,90956 | 180,92093 | 105,23292 | €352,70 | €705,40 | €46,00 | €-0,00 |
| Combo Adaptive Partial 1R V1 | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,52450 | 2,33981 | 1,27487 | 2,89389 | €347,19 | €694,38 | €50,80 | €0,00 |
| Combo Adaptive Partial 1R V1 | VELVET | SHORT | Combo Adaptive | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €207,76 | €415,52 | €0,00 | €-0,00 |
| Combo Adaptive Partial 1R V1 | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €1.013,20 | €2.026,40 | €50,39 | €0,00 |
| Combo Adaptive Partial 1R V1 | TAO | LONG | Combo Adaptive | 60m | 2,0x | 264,91297 | 264,91297 | 254,31765 | 133,78105 | 286,10361 | €49,09 | €98,18 | €3,93 | €0,00 |
| Combo Adaptive Runner25 V1 | 0G | LONG | Combo Adaptive | 60m | 2,0x | 0,23904 | 0,23904 | 0,21329 | 0,12072 | 0,31630 | €204,19 | €408,39 | €43,99 | €0,00 |
| Combo Adaptive Runner25 V1 | BTR | SHORT | Combo Adaptive | 60m | 2,0x | 0,04991 | 0,04991 | 0,04991 | 0,07462 | 0,03194 | €182,83 | €365,66 | €0,00 | €-0,00 |
| Combo Adaptive Runner25 V1 | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,15692 | €376,21 | €752,41 | €45,50 | €0,00 |
| Combo Adaptive Runner25 V1 | UNI | LONG | Combo Adaptive | 60m | 2,0x | 7,16543 | 7,16543 | 6,92567 | 3,61854 | 7,88472 | €17,00 | €34,01 | €1,14 | €0,00 |
| Combo Adaptive Runner25 V1 | TAO | LONG | Combo Adaptive | 60m | 2,0x | 264,91297 | 264,91297 | 254,31765 | 133,78105 | 296,69893 | €536,57 | €1.073,13 | €42,92 | €0,00 |
| Combo Adaptive Runner25 V1 | USELESS | LONG | Combo Adaptive | 60m | 2,0x | 0,28937 | 0,29292 | 0,26165 | 0,14613 | 0,37252 | €24,75 | €49,51 | €4,74 | €0,61 |
| Combo Adaptive Tp3 V1 | 0G | LONG | Combo Adaptive | 60m | 2,0x | 0,23904 | 0,23904 | 0,21329 | 0,12072 | 0,31630 | €200,38 | €400,76 | €43,17 | €0,00 |
| Combo Adaptive Tp3 V1 | BTR | SHORT | Combo Adaptive | 60m | 2,0x | 0,04991 | 0,04991 | 0,04991 | 0,07462 | 0,03194 | €179,40 | €358,80 | €0,00 | €-0,00 |
| Combo Adaptive Tp3 V1 | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,15692 | €369,17 | €738,34 | €44,64 | €0,00 |
| Combo Adaptive Tp3 V1 | UNI | LONG | Combo Adaptive | 60m | 2,0x | 7,16543 | 7,16543 | 6,92567 | 3,61854 | 7,88472 | €16,69 | €33,37 | €1,12 | €0,00 |
| Combo Adaptive Tp3 V1 | TAO | LONG | Combo Adaptive | 60m | 2,0x | 264,91297 | 264,91297 | 254,31765 | 133,78105 | 296,69893 | €526,53 | €1.053,06 | €42,12 | €0,00 |
| Combo Adaptive Tp3 V1 | USELESS | LONG | Combo Adaptive | 60m | 2,0x | 0,28937 | 0,29292 | 0,26165 | 0,14613 | 0,37252 | €24,30 | €48,60 | €4,65 | €0,60 |
| Btc Ema 1H | BTC | SHORT | Trend following EMA | 60m | 3,0x | 78490,59874 | 79104,63000 | 79620,86336 | 104261,67866 | 76230,06950 | €1.097,82 | €3.293,47 | €47,43 | €-25,76 |
| Btc Bollinger 4H | BTC | SHORT | Bollinger mean reversion | 240m | 2,0x | 80768,04316 | 79104,63000 | 79312,77020 | 120748,22452 | 77055,51340 | €985,68 | €1.971,36 | €0,00 | €40,60 |
| Btc Adaptive 1H | BTC | SHORT | Combo Adaptive | 60m | 3,0x | 78449,01706 | 79104,63000 | 79578,68290 | 104206,44433 | 76189,68537 | €1.153,77 | €3.461,31 | €49,84 | €-28,93 |
| Sol Donchian 4H | SOL | LONG | Donchian breakout 20 barre | 240m | 2,0x | 104,23184 | 104,18000 | 99,63427 | 52,63708 | 117,10505 | €574,98 | €1.149,96 | €50,72 | €-0,57 |
| Sol Adaptive 4H | SOL | LONG | Combo Adaptive | 240m | 2,0x | 105,36907 | 104,18000 | 100,99415 | 53,21138 | 116,30636 | €613,63 | €1.227,27 | €50,96 | €-13,85 |
| Eth Ema 4H | ETH | LONG | Trend following EMA | 240m | 2,0x | 2499,33977 | 2503,84000 | 2409,82951 | 1262,16658 | 2723,11538 | €690,19 | €1.380,39 | €49,44 | €2,49 |
| Master Adaptive V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99403 | 639,55695 | 1331,36019 | €22,75 | €45,50 | €1,17 | €0,00 |
| Master Adaptive V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €195,57 | €391,15 | €46,94 | €0,00 |
| Master Adaptive V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,20498 | 0,11491 | 0,27267 | €236,54 | €473,08 | €46,91 | €0,00 |
| Master Adaptive V1 | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,13517 | 0,13517 | 0,12719 | 0,06826 | 0,15112 | €410,30 | €820,61 | €48,44 | €0,00 |
| Master Adaptive V1 | USELESS | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,28937 | 0,29292 | 0,26165 | 0,14613 | 0,34480 | €249,77 | €499,54 | €47,85 | €6,13 |
| Master Adaptive No Alt V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1255,10261 | 1255,10261 | 1225,12158 | 633,82682 | 1315,06467 | €19,09 | €38,19 | €0,91 | €0,00 |
| Master Adaptive No Alt V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €183,81 | €367,62 | €44,11 | €0,00 |
| Master Adaptive No Alt V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 530,08600 | 530,08600 | 509,10047 | 267,69343 | 572,05705 | €589,91 | €1.179,82 | €46,71 | €0,00 |
| Master Adaptive No Alt V1 | SUI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,81626 | 0,81940 | 0,78829 | 0,41221 | 0,87220 | €28,88 | €57,76 | €1,98 | €0,22 |
| Master Adaptive No Alt V1 | WLD | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,46919 | 0,46919 | 0,44675 | 0,23694 | 0,51408 | €481,98 | €963,96 | €46,11 | €0,00 |
| Master Adaptive No Alt V1 | USELESS | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,26037 | 0,29292 | 0,22980 | 0,13149 | 0,32152 | €184,85 | €369,71 | €43,41 | €46,22 |
| Master Adaptive No Alt V1 | XRP | LONG | Master Adaptive Consensus | 60m | 2,0x | 1,41308 | 1,43158 | 1,39180 | 0,71361 | 1,45565 | €42,62 | €85,24 | €1,28 | €1,12 |
| Master Adaptive Strict3 V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €178,16 | €356,31 | €42,76 | €0,00 |
| Master Adaptive Strict3 V1 | PROM | LONG | Master Adaptive Consensus | 60m | 2,0x | 7,01991 | 7,01991 | 6,30832 | 3,54505 | 8,44309 | €215,49 | €430,99 | €43,69 | €0,00 |
| Master Adaptive Strict3 V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,24076 | 0,24076 | 0,21579 | 0,12159 | 0,29071 | €209,83 | €419,66 | €43,53 | €0,00 |
| Master Adaptive Strict3 V1 | LINK | LONG | Master Adaptive Consensus | 60m | 2,0x | 13,22564 | 13,22564 | 12,79229 | 6,67895 | 14,09236 | €13,27 | €26,55 | €0,87 | €0,00 |
| Master Adaptive Strict3 V1 | WLD | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,46919 | 0,46919 | 0,44675 | 0,23694 | 0,51408 | €465,87 | €931,73 | €44,57 | €0,00 |
| Master Adaptive Strict3 V1 | USELESS | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,28110 | 0,29292 | 0,24944 | 0,14195 | 0,34441 | €15,82 | €31,64 | €3,56 | €1,33 |
| Master Adaptive Expanded V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03814 | 0,02188 | 0,05374 | €197,50 | €395,01 | €47,40 | €0,00 |
| Master Adaptive Expanded V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1261,89668 | 1261,89668 | 1231,08309 | 637,25783 | 1323,52387 | €934,21 | €1.868,43 | €45,62 | €0,00 |
| Master Adaptive Expanded V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01194 | 0,01194 | 0,01050 | 0,00603 | 0,01480 | €195,34 | €390,67 | €46,88 | €0,00 |
| Master Adaptive Expanded V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,20498 | 0,11491 | 0,27267 | €236,25 | €472,49 | €46,85 | €0,00 |
| Master Adaptive Expanded V1 | XRP | LONG | Master Adaptive Consensus | 60m | 2,0x | 1,41308 | 1,43158 | 1,39180 | 0,71361 | 1,45565 | €21,68 | €43,37 | €0,65 | €0,57 |
| Master Adaptive Gb20 V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99403 | 639,55695 | 1331,36019 | €22,45 | €44,90 | €1,15 | €0,00 |
| Master Adaptive Gb20 V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €193,03 | €386,06 | €46,33 | €0,00 |
| Master Adaptive Gb20 V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,20498 | 0,11491 | 0,27267 | €233,42 | €466,83 | €46,29 | €0,00 |
| Master Adaptive Gb20 V1 | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,13517 | 0,13517 | 0,12719 | 0,06826 | 0,15112 | €404,89 | €809,78 | €47,80 | €0,00 |
| Master Adaptive Gb20 V1 | USELESS | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,28937 | 0,29292 | 0,26165 | 0,14613 | 0,34480 | €246,48 | €492,95 | €47,22 | €6,05 |
| Master Adaptive Runner25 V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03814 | 0,02188 | 0,05894 | €34,77 | €69,54 | €8,34 | €0,00 |
| Master Adaptive Runner25 V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1255,10261 | 1255,10261 | 1225,12158 | 633,82682 | 1345,04570 | €27,05 | €54,10 | €1,29 | €0,00 |
| Master Adaptive Runner25 V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01601 | €185,86 | €371,72 | €44,61 | €0,00 |
| Master Adaptive Runner25 V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,20498 | 0,11491 | 0,29523 | €233,84 | €467,69 | €46,37 | €0,00 |
| Master Adaptive Runner25 V1 | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,13517 | 0,13517 | 0,12719 | 0,06826 | 0,15910 | €399,89 | €799,78 | €47,21 | €0,00 |
| Master Adaptive Runner25 V1 | NEAR | LONG | Master Adaptive Consensus | 60m | 2,0x | 2,22144 | 2,22144 | 2,12346 | 1,12183 | 2,51541 | €477,69 | €955,38 | €42,14 | €0,00 |
| Master Adaptive Runner25 V1 | ZEC | LONG | Master Adaptive Consensus | 60m | 2,0x | 1142,68849 | 1245,61000 | 1099,52971 | 577,05769 | 1272,16483 | €18,41 | €36,81 | €1,39 | €3,32 |
| Combo Adaptive Side Regime Guard V1 | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €77,52 | €155,04 | €5,58 | €0,00 |
| Combo Adaptive Side Regime Guard V1 | VELVET | SHORT | Combo Adaptive | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €216,61 | €433,23 | €0,00 | €-0,00 |
| Combo Adaptive Side Regime Guard V1 | TUT | SHORT | Combo Adaptive | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €192,40 | €384,79 | €46,18 | €-0,00 |
| Combo Adaptive Side Regime Guard V1 | BTR | SHORT | Combo Adaptive | 60m | 2,0x | 0,05109 | 0,05109 | 0,05109 | 0,07638 | 0,03883 | €195,57 | €391,13 | €0,00 | €-0,00 |
| Combo Adaptive Side Regime Guard V1 | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,14889 | €385,18 | €770,35 | €46,58 | €0,00 |
| Combo Adaptive Side Regime Guard V1 | UNI | LONG | Combo Adaptive | 60m | 2,0x | 7,16543 | 7,16543 | 6,92567 | 3,61854 | 7,64496 | €12,54 | €25,08 | €0,84 | €0,00 |
| Combo Adaptive Side Regime Guard V1 | SUI | LONG | Combo Adaptive | 60m | 2,0x | 0,81626 | 0,81940 | 0,78829 | 0,41221 | 0,87220 | €33,06 | €66,11 | €2,27 | €0,25 |
| Master Adaptive Gb20 Be V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99403 | 639,55695 | 1331,36019 | €22,86 | €45,73 | €1,17 | €0,00 |
| Master Adaptive Gb20 Be V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €196,54 | €393,08 | €47,17 | €0,00 |
| Master Adaptive Gb20 Be V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,20498 | 0,11491 | 0,27267 | €237,71 | €475,42 | €47,14 | €0,00 |
| Master Adaptive Gb20 Be V1 | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,13517 | 0,13517 | 0,12719 | 0,06826 | 0,15112 | €412,34 | €824,67 | €48,68 | €0,00 |
| Master Adaptive Gb20 Be V1 | USELESS | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,28937 | 0,29292 | 0,26165 | 0,14613 | 0,34480 | €251,01 | €502,02 | €48,08 | €6,16 |
| Master Adaptive Gb20 Partial V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99403 | 639,55695 | 1331,36019 | €22,84 | €45,68 | €1,17 | €0,00 |
| Master Adaptive Gb20 Partial V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €196,33 | €392,67 | €47,12 | €0,00 |
| Master Adaptive Gb20 Partial V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,20498 | 0,11491 | 0,27267 | €237,46 | €474,91 | €47,09 | €0,00 |
| Master Adaptive Gb20 Partial V1 | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,13517 | 0,13517 | 0,12719 | 0,06826 | 0,15112 | €411,90 | €823,79 | €48,63 | €0,00 |
| Master Adaptive Gb20 Partial V1 | USELESS | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,28937 | 0,29292 | 0,26165 | 0,14613 | 0,34480 | €250,74 | €501,48 | €48,03 | €6,16 |
| Master Adaptive Gb20 Loss Cap V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03828 | 0,02188 | 0,05682 | €195,70 | €391,41 | €45,67 | €0,00 |
| Master Adaptive Gb20 Loss Cap V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01069 | 0,00594 | 0,01465 | €210,34 | €420,68 | €38,67 | €0,00 |
| Master Adaptive Gb20 Loss Cap V1 | PROM | LONG | Master Adaptive Consensus | 60m | 2,0x | 7,01991 | 7,01991 | 6,48622 | 3,54505 | 8,44309 | €34,75 | €69,51 | €5,28 | €0,00 |
| Master Adaptive Gb20 Loss Cap V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,21062 | 0,11491 | 0,27267 | €309,65 | €619,30 | €46,05 | €0,00 |
| Master Adaptive Gb20 Loss Cap V1 | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,13517 | 0,13517 | 0,12918 | 0,06826 | 0,15112 | €19,32 | €38,65 | €1,71 | €0,00 |
| Master Adaptive Gb20 Loss Cap V1 | WLD | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,46919 | 0,46919 | 0,45236 | 0,23694 | 0,51408 | €80,25 | €160,51 | €5,76 | €0,00 |
| Master Adaptive Gb20 Loss Cap V1 | XRP | LONG | Master Adaptive Consensus | 60m | 2,0x | 1,41806 | 1,43158 | 1,39982 | 0,71612 | 1,46671 | €19,97 | €39,95 | €0,51 | €0,38 |
| Master Adaptive Gb20 Loss Cap V1 | USELESS | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,29298 | 0,29292 | 0,27254 | 0,14795 | 0,34749 | €318,08 | €636,15 | €44,38 | €-0,13 |
| 1H Fast V3 Nohigh Range Only V1 | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,20283 | 0,22024 | 0,20750 | 0,26943 | 0,19582 | €740,69 | €2.222,07 | €51,20 | €-190,74 |
| 1H Fast V3 Nohigh Range Only V1 | BTR | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €135,43 | €406,30 | €0,00 | €-0,00 |
| 1H Fast V3 Nohigh Range Only V1 | USELESS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,27548 | 0,29292 | 0,27548 | 0,18503 | 0,31405 | €179,30 | €537,91 | €0,00 | €34,06 |
| 1H Fast V3 Nohigh Range Only V1 | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 85,62612 | 86,01300 | 84,59501 | 57,51221 | 87,17280 | €24,31 | €72,94 | €0,88 | €0,33 |
| 1H Fast V3 Nohigh Range Only V1 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2504,34077 | 2503,84000 | 2476,29215 | 1682,08222 | 2546,41369 | €1.426,20 | €4.278,59 | €47,92 | €-0,86 |
| 1H Fast V3 Nohigh Regime Guard V1 | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €140,84 | €422,53 | €50,70 | €-0,00 |
| 1H Fast V3 Nohigh Regime Guard V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €143,15 | €429,46 | €50,70 | €-0,00 |
| 1H Fast V3 Nohigh Regime Guard V1 | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,20283 | 0,22024 | 0,20750 | 0,26943 | 0,19582 | €34,57 | €103,71 | €2,39 | €-8,90 |
| 1H Fast V3 Nohigh Regime Guard V1 | BTR | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,05154 | 0,05154 | 0,05154 | 0,06846 | 0,04226 | €139,06 | €417,17 | €0,00 | €-0,00 |
| 1H Fast V3 Nohigh Regime Guard V1 | USELESS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,27548 | 0,29292 | 0,27548 | 0,18503 | 0,31405 | €8,82 | €26,45 | €0,00 | €1,67 |
| 1H Fast V3 Nohigh Regime Guard V1 | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 85,62612 | 86,01300 | 84,59501 | 57,51221 | 87,17280 | €13,91 | €41,73 | €0,50 | €0,19 |
| 1H Fast V3 Nohigh Regime Guard V1 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2504,34077 | 2503,84000 | 2476,29215 | 1682,08222 | 2546,41369 | €1.556,76 | €4.670,27 | €52,31 | €-0,93 |
| Main Side Regime Guard V1 | VELVET | LONG | Confluenza trend | 240m | 3,0x | 0,55987 | 0,55987 | 0,49269 | 0,37605 | 0,69424 | €142,25 | €426,74 | €51,21 | €0,00 |
| Main Side Regime Guard V1 | AKE | LONG | Confluenza trend | 240m | 3,0x | 0,01021 | 0,01021 | 0,00899 | 0,00686 | 0,01266 | €145,97 | €437,90 | €52,55 | €0,00 |
| Main Side Regime Guard V1 | ENA | LONG | Confluenza trend | 240m | 3,0x | 0,16108 | 0,16108 | 0,14175 | 0,10819 | 0,19974 | €150,44 | €451,33 | €54,16 | €0,00 |
| Main Side Regime Guard V1 | BTR | SHORT | Confluenza trend | 240m | 3,0x | 0,04853 | 0,04853 | 0,05435 | 0,06446 | 0,03688 | €12,76 | €38,29 | €4,59 | €-0,00 |
| Main Side Regime Guard V1 | DASH | LONG | Confluenza trend | 240m | 3,0x | 69,69394 | 69,69394 | 61,33066 | 46,81109 | 86,42048 | €155,22 | €465,66 | €55,88 | €0,00 |
| Main Side Regime Guard V1 | NEAR | LONG | Confluenza trend | 240m | 3,0x | 2,38548 | 2,38548 | 2,20016 | 1,60225 | 2,75612 | €21,97 | €65,90 | €5,12 | €0,00 |
| Main Dynamic Asset Selector V1 | ENA | LONG | Confluenza trend | 240m | 3,0x | 0,16108 | 0,16108 | 0,14175 | 0,10819 | 0,19974 | €140,98 | €422,93 | €50,75 | €0,00 |
| Main Dynamic Asset Selector V1 | ZEC | LONG | Confluenza trend | 240m | 3,0x | 1190,40803 | 1245,61000 | 1090,98250 | 799,55740 | 1389,25911 | €203,57 | €610,70 | €51,01 | €28,32 |
| Main Dynamic Asset Selector V1 | USELESS | LONG | Confluenza trend | 240m | 3,0x | 0,26037 | 0,29292 | 0,26037 | 0,17488 | 0,32286 | €142,80 | €428,41 | €0,00 | €53,55 |
| Combo Trend Side Regime Guard V1 | VELVET | SHORT | Combo Trend | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,12693 | €217,86 | €435,73 | €0,00 | €-0,00 |
| Combo Trend Side Regime Guard V1 | TUT | SHORT | Combo Trend | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03364 | €12,81 | €25,62 | €3,07 | €-0,00 |
| Combo Trend Side Regime Guard V1 | BTR | SHORT | Combo Trend | 60m | 2,0x | 0,04853 | 0,04853 | 0,05435 | 0,07255 | 0,03572 | €222,18 | €444,37 | €53,32 | €-0,00 |
| Combo Trend Side Regime Guard V1 | ARB | LONG | Combo Trend | 60m | 2,0x | 0,13283 | 0,13283 | 0,12390 | 0,06708 | 0,15246 | €399,57 | €799,13 | €53,69 | €0,00 |
| Combo Trend Side Regime Guard V1 | UNI | LONG | Combo Trend | 60m | 2,0x | 7,09542 | 7,09542 | 6,74949 | 3,58319 | 7,85647 | €523,05 | €1.046,10 | €51,00 | €0,00 |
| Combo Trend Side Regime Guard V1 | TAO | LONG | Combo Trend | 60m | 2,0x | 264,91297 | 264,91297 | 253,14039 | 133,78105 | 290,81264 | €73,76 | €147,52 | €6,56 | €0,00 |
| 1H Fast Nohigh Cap75 Short Only V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €135,82 | €407,46 | €48,90 | €-0,00 |
| 1H Fast Nohigh Cap75 Short Only V1 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €138,05 | €414,14 | €48,89 | €-0,00 |
| 1H Fast Nohigh Cap75 Short Only V1 | BTR | SHORT | Momentum / breakout | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €132,24 | €396,72 | €0,00 | €-0,00 |
| 1H Fast Nohigh Cap75 Short Only V1 | PEPE | SHORT | Momentum / breakout | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €573,54 | €1.720,62 | €44,16 | €-84,88 |
| 1H Balanced V3 Long Only V1 | SKHYNIX | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1220,85412 | 1220,85412 | 1177,63561 | 820,00702 | 1307,29117 | €435,49 | €1.306,46 | €46,25 | €0,00 |
| 1H Balanced V3 Long Only V1 | ADA | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,20138 | 0,22024 | 0,20719 | 0,26750 | 0,18976 | €529,53 | €1.588,58 | €45,82 | €-148,78 |
| 1H Balanced V3 Long Only V1 | ARB | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,13283 | 0,13283 | 0,12480 | 0,08922 | 0,14889 | €248,38 | €745,13 | €45,06 | €0,00 |
| 1H Balanced V3 Long Only V1 | UNI | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 7,14143 | 7,14143 | 6,87560 | 4,79666 | 7,67309 | €9,06 | €27,18 | €1,01 | €0,00 |
| 1H Balanced V3 Long Only V1 | ZEC | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1183,25660 | 1245,61000 | 1207,46714 | 794,75402 | 1268,83160 | €362,93 | €1.088,78 | €0,00 | €57,37 |
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
| Scanner Top10 Long | ZEC | LONG | 2026-09-09T05:00:00+00:00 | 1262,43184 | €3,35 | 1,95 | TARGET |
| Master Adaptive Gb20 Loss Cap V1 | ZEC | LONG | 2026-09-09T05:00:00+00:00 | 1246,85627 | €111,60 | 2,62 | TARGET |
| 1H Fast V3 No Esports Stress Guard V1 | ZEC | LONG | 2026-09-09T04:45:00+00:00 | 1224,82010 | €74,53 | 1,44 | TARGET |
| 1H Fast V3 No Esports Long Only V1 | ZEC | LONG | 2026-09-09T04:45:00+00:00 | 1219,18847 | €72,88 | 1,45 | TARGET |
| 1H Fast V3 Nohigh V1 | ZEC | LONG | 2026-09-09T04:45:00+00:00 | 1230,94355 | €1,74 | 1,44 | TARGET |
| 1H Fast V3 Nohigh Regime Guard V1 | ZEC | LONG | 2026-09-09T04:45:00+00:00 | 1219,18847 | €74,40 | 1,45 | TARGET |
| 1H Fast V3 Nohigh Range Only V1 | ZEC | LONG | 2026-09-09T04:45:00+00:00 | 1219,18847 | €67,15 | 1,45 | TARGET |
| 1H Fast V3 Nohigh Range Only V1 | BTC | SHORT | 2026-09-09T04:45:00+00:00 | 79162,44611 | €-0,61 | -1,12 | STOP |
| 1H Fast V3 Long Only V1 | ZEC | LONG | 2026-09-09T04:45:00+00:00 | 1219,18847 | €2,95 | 1,45 | TARGET |
| 1H Fast V3 Long Nohigh Cap75 V1 | ZEC | LONG | 2026-09-09T04:45:00+00:00 | 1219,18847 | €72,36 | 1,45 | TARGET |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | ZEC | LONG | 2026-09-09T04:45:00+00:00 | 1219,18847 | €6,55 | 1,45 | TARGET |
| 1H Fast V3 Cap75 V1 | ZEC | LONG | 2026-09-09T04:45:00+00:00 | 1219,18847 | €63,77 | 1,45 | TARGET |

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

Generato: 2026-09-09 05:33 UTC


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

Segnali totali salvati: **183**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-09-09 | BTC | 78.978,35 | +6 | +3 | +3 | 0 | +3 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-09-09 | DOGE | 0.09017 | +3 | -1 | -1 | 0 | +3 | 0 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-09-09 | SOL | 104,26 | +5 | +2 | +2 | 0 | +3 | +1 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-09-08 | BTC | 78.724,26 | +6 | +3 | +3 | 0 | +3 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-09-08 | DOGE | 0.09002 | +3 | -2 | -2 | 0 | +3 | +1 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-09-08 | SOL | 103,26 | +8 | +3 | +3 | 0 | +3 | +1 | 0 | HOLD / ACCUMULO A TRANCHE, NO LEVA AGGRESSIVA |
| 2026-09-07 | BTC | 79.828,11 | +7 | +3 | +3 | 0 | +3 | 0 | 0 | ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA |
| 2026-09-07 | DOGE | 0.09027 | +1 | -2 | -2 | 0 | +3 | +1 | 0 | STAI ALLA FINESTRA |
| 2026-09-07 | SOL | 105,55 | +8 | +3 | +3 | 0 | +3 | +1 | 0 | HOLD / ACCUMULO A TRANCHE, NO LEVA AGGRESSIVA |
| 2026-09-06 | BTC | 79.879,48 | +6 | +3 | +3 | 0 | +3 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-09-06 | DOGE | 0.09088 | +3 | -2 | -2 | 0 | +3 | +1 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-09-06 | SOL | 105,95 | +7 | +3 | +3 | 0 | +3 | +1 | 0 | HOLD / ACCUMULO A TRANCHE, NO LEVA AGGRESSIVA |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 61 | 60 | 59 | 58 | 56 | 54 | 51 | 47 | 40 | 33 | 18 | 3 |
| SOL | 61 | 60 | 59 | 58 | 56 | 54 | 51 | 47 | 40 | 33 | 18 | 3 |
| DOGE | 61 | 60 | 59 | 58 | 56 | 54 | 51 | 47 | 40 | 33 | 18 | 3 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-07-12 | 60g | 2026-09-10 | domani |
| SOL | 2026-07-12 | 60g | 2026-09-10 | domani |
| DOGE | 2026-07-12 | 60g | 2026-09-10 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 57 | 50,88% | +0,41% | +0,39% | PRIMA CALIBRAZIONE |
| BTC | 2g | 56 | 51,79% | +0,72% | +0,63% | PRIMA CALIBRAZIONE |
| BTC | 3g | 55 | 47,27% | +0,94% | +0,81% | PRIMA CALIBRAZIONE |
| BTC | 5g | 53 | 47,17% | +1,91% | +1,67% | PRIMA CALIBRAZIONE |
| BTC | 7g | 51 | 54,90% | +2,65% | +2,43% | PRIMA CALIBRAZIONE |
| BTC | 10g | 48 | 62,50% | +3,69% | +3,50% | PRIMA CALIBRAZIONE |
| BTC | 14g | 44 | 63,64% | +5,73% | +5,65% | PRIMA CALIBRAZIONE |
| BTC | 21g | 37 | 62,16% | +10,56% | +10,38% | PRIMA CALIBRAZIONE |
| BTC | 30g | 31 | 90,32% | +13,88% | +12,49% | PRIMA CALIBRAZIONE |
| BTC | 45g | 16 | 87,50% | +22,54% | +16,97% | FEEDBACK RAPIDO |
| BTC | 60g | 3 | 100,00% | +24,28% | +24,28% | FEEDBACK RAPIDO |
| SOL | 1g | 53 | 54,72% | +0,65% | +0,53% | PRIMA CALIBRAZIONE |
| SOL | 2g | 52 | 51,92% | +1,30% | +1,16% | PRIMA CALIBRAZIONE |
| SOL | 3g | 51 | 58,82% | +2,09% | +1,91% | PRIMA CALIBRAZIONE |
| SOL | 5g | 49 | 63,27% | +3,53% | +3,42% | PRIMA CALIBRAZIONE |
| SOL | 7g | 47 | 65,96% | +4,87% | +4,99% | PRIMA CALIBRAZIONE |
| SOL | 10g | 44 | 68,18% | +6,85% | +7,02% | PRIMA CALIBRAZIONE |
| SOL | 14g | 40 | 80,00% | +10,54% | +11,45% | PRIMA CALIBRAZIONE |
| SOL | 21g | 33 | 75,76% | +17,34% | +16,26% | PRIMA CALIBRAZIONE |
| SOL | 30g | 26 | 61,54% | +19,79% | +12,19% | FEEDBACK RAPIDO |
| SOL | 45g | 14 | 35,71% | +33,18% | -11,07% | FEEDBACK RAPIDO |
| SOL | 60g | 2 | 100,00% | +34,65% | +34,65% | FEEDBACK RAPIDO |
| DOGE | 1g | 56 | 44,64% | +0,51% | +0,12% | PRIMA CALIBRAZIONE |
| DOGE | 2g | 55 | 45,45% | +1,01% | +0,38% | PRIMA CALIBRAZIONE |
| DOGE | 3g | 54 | 40,74% | +1,50% | +0,73% | PRIMA CALIBRAZIONE |
| DOGE | 5g | 52 | 50,00% | +2,43% | +1,80% | PRIMA CALIBRAZIONE |
| DOGE | 7g | 50 | 60,00% | +2,88% | +3,23% | PRIMA CALIBRAZIONE |
| DOGE | 10g | 48 | 58,33% | +2,96% | +4,04% | PRIMA CALIBRAZIONE |
| DOGE | 14g | 45 | 68,89% | +5,11% | +7,18% | PRIMA CALIBRAZIONE |
| DOGE | 21g | 38 | 78,95% | +9,94% | +8,90% | PRIMA CALIBRAZIONE |
| DOGE | 30g | 31 | 74,19% | +12,41% | +5,21% | PRIMA CALIBRAZIONE |
| DOGE | 45g | 18 | 5,56% | +20,48% | -17,95% | FEEDBACK RAPIDO |
| DOGE | 60g | 3 | 0,00% | +22,53% | -22,53% | FEEDBACK RAPIDO |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 57 | 50,88% | +0,41% | +0,39% | -0,03% | +0,97% | PRIMA CALIBRAZIONE |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 60 | 53,33% | +0,39% | +0,39% | -0,05% | +0,93% | UTILE |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 60 | 53,33% | +0,39% | +0,39% | -0,05% | +0,93% | UTILE |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,25% | +0,25% | -0,10% | +0,70% | PRIMA CALIBRAZIONE |
| BTC | 1g | Tecnico | CALIBRABILE | 55 | 40,00% | +0,51% | +0,14% | +0,06% | +1,05% | PRIMA CALIBRAZIONE |
| BTC | 1g | Classic technical | CALIBRABILE | 24 | 37,50% | +0,81% | +0,37% | +0,13% | +1,33% | FEEDBACK RAPIDO |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | -0,17% | -0,17% | -0,60% | +0,27% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 56 | 51,79% | +0,72% | +0,63% | +0,14% | +1,41% | PRIMA CALIBRAZIONE |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 59 | 54,24% | +0,81% | +0,81% | +0,24% | +1,50% | PRIMA CALIBRAZIONE |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 59 | 54,24% | +0,81% | +0,81% | +0,24% | +1,50% | PRIMA CALIBRAZIONE |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,52% | +0,52% | -0,02% | +1,18% | PRIMA CALIBRAZIONE |
| BTC | 2g | Tecnico | CALIBRABILE | 54 | 44,44% | +0,98% | +0,22% | +0,41% | +1,67% | PRIMA CALIBRAZIONE |
| BTC | 2g | Classic technical | CALIBRABILE | 24 | 41,67% | +1,18% | +0,55% | +0,59% | +1,89% | FEEDBACK RAPIDO |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +0,73% | +0,73% | +0,13% | +1,27% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 55 | 47,27% | +0,94% | +0,81% | -0,96% | +2,62% | PRIMA CALIBRAZIONE |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 58 | 55,17% | +1,23% | +1,23% | -0,95% | +2,84% | PRIMA CALIBRAZIONE |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 58 | 55,17% | +1,23% | +1,23% | -0,95% | +2,84% | PRIMA CALIBRAZIONE |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 35 | 57,14% | +0,91% | +0,91% | -1,00% | +2,36% | PRIMA CALIBRAZIONE |
| BTC | 3g | Tecnico | CALIBRABILE | 53 | 37,74% | +1,53% | -0,06% | -0,77% | +3,11% | PRIMA CALIBRAZIONE |
| BTC | 3g | Classic technical | CALIBRABILE | 24 | 41,67% | +1,81% | +0,20% | -0,58% | +3,31% | FEEDBACK RAPIDO |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +0,35% | +0,35% | -1,11% | +1,90% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 53 | 47,17% | +1,91% | +1,67% | -1,52% | +4,15% | PRIMA CALIBRAZIONE |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 56 | 53,57% | +2,15% | +2,15% | -1,49% | +4,44% | PRIMA CALIBRAZIONE |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 56 | 53,57% | +2,15% | +2,15% | -1,49% | +4,44% | PRIMA CALIBRAZIONE |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 35 | 48,57% | +2,08% | +2,08% | -1,57% | +4,07% | PRIMA CALIBRAZIONE |
| BTC | 5g | Tecnico | CALIBRABILE | 51 | 45,10% | +2,46% | -0,86% | -1,30% | +4,81% | PRIMA CALIBRAZIONE |
| BTC | 5g | Classic technical | CALIBRABILE | 24 | 50,00% | +3,70% | -1,14% | -1,03% | +5,94% | FEEDBACK RAPIDO |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 25,00% | -0,34% | -0,34% | -1,71% | +2,56% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 51 | 54,90% | +2,65% | +2,43% | -1,78% | +5,39% | PRIMA CALIBRAZIONE |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 54 | 61,11% | +2,96% | +2,96% | -1,76% | +5,67% | PRIMA CALIBRAZIONE |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 54 | 61,11% | +2,96% | +2,96% | -1,76% | +5,67% | PRIMA CALIBRAZIONE |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 35 | 60,00% | +3,17% | +3,17% | -1,80% | +5,49% | PRIMA CALIBRAZIONE |
| BTC | 7g | Tecnico | CALIBRABILE | 49 | 42,86% | +3,49% | -1,72% | -1,55% | +6,14% | PRIMA CALIBRAZIONE |
| BTC | 7g | Classic technical | CALIBRABILE | 22 | 45,45% | +5,46% | -2,91% | -1,23% | +8,53% | FEEDBACK RAPIDO |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +0,68% | +0,68% | -1,68% | +3,81% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 48 | 62,50% | +3,69% | +3,50% | -2,00% | +6,50% | PRIMA CALIBRAZIONE |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 51 | 66,67% | +3,86% | +3,86% | -2,00% | +6,75% | PRIMA CALIBRAZIONE |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 51 | 66,67% | +3,86% | +3,86% | -2,00% | +6,75% | PRIMA CALIBRAZIONE |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 35 | 62,86% | +4,42% | +4,42% | -2,02% | +6,89% | PRIMA CALIBRAZIONE |
| BTC | 10g | Tecnico | CALIBRABILE | 46 | 47,83% | +4,40% | -1,38% | -1,76% | +7,35% | PRIMA CALIBRAZIONE |
| BTC | 10g | Classic technical | CALIBRABILE | 19 | 57,89% | +6,93% | -4,18% | -1,23% | +10,01% | FEEDBACK RAPIDO |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +0,54% | +0,54% | -2,46% | +3,88% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 44 | 63,64% | +5,73% | +5,65% | -2,09% | +9,07% | PRIMA CALIBRAZIONE |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 47 | 63,83% | +5,79% | +5,79% | -2,10% | +9,18% | PRIMA CALIBRAZIONE |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 47 | 63,83% | +5,79% | +5,79% | -2,10% | +9,18% | PRIMA CALIBRAZIONE |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 35 | 68,57% | +6,60% | +6,60% | -2,13% | +9,78% | PRIMA CALIBRAZIONE |
| BTC | 14g | Tecnico | CALIBRABILE | 42 | 59,52% | +6,63% | +0,86% | -1,82% | +10,07% | PRIMA CALIBRAZIONE |
| BTC | 14g | Classic technical | CALIBRABILE | 15 | 46,67% | +8,42% | -4,69% | -0,87% | +12,10% | FEEDBACK RAPIDO |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 33,33% | -0,03% | -0,03% | -2,90% | +4,64% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 37 | 62,16% | +10,56% | +10,38% | -2,38% | +14,19% | PRIMA CALIBRAZIONE |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 40 | 70,00% | +10,28% | +10,28% | -2,38% | +13,97% | PRIMA CALIBRAZIONE |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 40 | 70,00% | +10,28% | +10,28% | -2,38% | +13,97% | PRIMA CALIBRAZIONE |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 35 | 74,29% | +11,25% | +11,25% | -2,21% | +14,88% | PRIMA CALIBRAZIONE |
| BTC | 21g | Tecnico | CALIBRABILE | 35 | 34,29% | +11,52% | -1,49% | -2,08% | +15,27% | PRIMA CALIBRAZIONE |
| BTC | 21g | Classic technical | CALIBRABILE | 8 | 0,00% | +19,34% | -19,34% | -0,83% | +22,19% | FEEDBACK RAPIDO |
| BTC | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,21% | +1,21% | -3,06% | +4,24% | FEEDBACK RAPIDO |
| BTC | 30g | Global confluence | BENCHMARK | 31 | 90,32% | +13,88% | +12,49% | -2,98% | +17,83% | PRIMA CALIBRAZIONE |
| BTC | 30g | Famiglia statistica | CALIBRABILE | 33 | 84,85% | +13,53% | +13,53% | -3,02% | +17,55% | PRIMA CALIBRAZIONE |
| BTC | 30g | Scanner grezzo | DIAGNOSTICO | 33 | 84,85% | +13,53% | +13,53% | -3,02% | +17,55% | PRIMA CALIBRAZIONE |
| BTC | 30g | Market regime grezzo | DIAGNOSTICO | 29 | 86,21% | +14,75% | +14,75% | -2,82% | +19,00% | FEEDBACK RAPIDO |
| BTC | 30g | Tecnico | CALIBRABILE | 28 | 42,86% | +13,68% | -2,44% | -2,76% | +18,04% | FEEDBACK RAPIDO |
| BTC | 30g | Classic technical | CALIBRABILE | 4 | 0,00% | +24,06% | -24,06% | -1,55% | +28,48% | FEEDBACK RAPIDO |
| BTC | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +0,16% | +0,16% | -3,06% | +4,24% | FEEDBACK RAPIDO |
| BTC | 45g | Global confluence | BENCHMARK | 16 | 87,50% | +22,54% | +16,97% | -3,22% | +26,53% | FEEDBACK RAPIDO |
| BTC | 45g | Famiglia statistica | CALIBRABILE | 18 | 100,00% | +22,59% | +22,59% | -3,27% | +26,54% | FEEDBACK RAPIDO |
| BTC | 45g | Scanner grezzo | DIAGNOSTICO | 18 | 100,00% | +22,59% | +22,59% | -3,27% | +26,54% | FEEDBACK RAPIDO |
| BTC | 45g | Market regime grezzo | DIAGNOSTICO | 14 | 100,00% | +23,03% | +23,03% | -2,92% | +26,92% | FEEDBACK RAPIDO |
| BTC | 45g | Tecnico | CALIBRABILE | 15 | 33,33% | +22,81% | -7,88% | -2,97% | +26,99% | FEEDBACK RAPIDO |
| BTC | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +20,42% | +20,42% | -3,06% | +26,73% | FEEDBACK RAPIDO |
| BTC | 60g | Global confluence | BENCHMARK | 3 | 100,00% | +24,28% | +24,28% | -3,05% | +29,12% | FEEDBACK RAPIDO |
| BTC | 60g | Famiglia statistica | CALIBRABILE | 3 | 100,00% | +24,28% | +24,28% | -3,05% | +29,12% | FEEDBACK RAPIDO |
| BTC | 60g | Scanner grezzo | DIAGNOSTICO | 3 | 100,00% | +24,28% | +24,28% | -3,05% | +29,12% | FEEDBACK RAPIDO |
| BTC | 60g | Market regime grezzo | DIAGNOSTICO | 3 | 100,00% | +24,28% | +24,28% | -3,05% | +29,12% | FEEDBACK RAPIDO |
| BTC | 60g | Tecnico | CALIBRABILE | 2 | 0,00% | +24,78% | -24,78% | -2,93% | +29,27% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 56 | 44,64% | +0,51% | +0,12% | -0,15% | +1,52% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 59 | 57,63% | +0,39% | +0,43% | -0,28% | +1,34% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 59 | 57,63% | +0,39% | +0,43% | -0,28% | +1,34% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,15% | +0,26% | -0,32% | +0,87% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Tecnico | CALIBRABILE | 53 | 52,83% | +0,31% | +0,47% | -0,39% | +1,24% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Classic technical | CALIBRABILE | 34 | 41,18% | +0,22% | -0,49% | -0,44% | +0,96% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 55,56% | +2,13% | +1,78% | +0,65% | +2,81% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 55 | 45,45% | +1,01% | +0,38% | +0,21% | +2,32% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 58 | 55,17% | +0,80% | +0,69% | +0,01% | +2,01% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 58 | 55,17% | +0,80% | +0,69% | +0,01% | +2,01% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 38 | 50,00% | +0,36% | +0,74% | -0,26% | +1,41% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Tecnico | CALIBRABILE | 52 | 55,77% | +0,42% | +0,78% | -0,35% | +1,62% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Classic technical | CALIBRABILE | 33 | 42,42% | +0,60% | -1,16% | -0,16% | +1,59% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 44,44% | +2,90% | +2,61% | +2,02% | +4,90% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 54 | 40,74% | +1,50% | +0,73% | -1,52% | +4,37% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 57 | 52,63% | +1,28% | +1,00% | -1,68% | +3,98% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 57 | 52,63% | +1,28% | +1,00% | -1,68% | +3,98% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,84% | +1,55% | -1,48% | +3,36% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Tecnico | CALIBRABILE | 51 | 47,06% | +0,46% | +0,78% | -1,95% | +3,04% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Classic technical | CALIBRABILE | 32 | 31,25% | +1,23% | -2,09% | -1,90% | +4,10% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 44,44% | +2,49% | +2,26% | -0,95% | +6,11% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 52 | 50,00% | +2,43% | +1,80% | -2,45% | +6,71% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 55 | 49,09% | +2,25% | +1,81% | -2,55% | +6,40% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 55 | 49,09% | +2,25% | +1,81% | -2,55% | +6,40% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +2,45% | +3,08% | -2,17% | +5,74% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Tecnico | CALIBRABILE | 49 | 59,18% | +1,18% | +0,92% | -3,00% | +5,35% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Classic technical | CALIBRABILE | 31 | 38,71% | +2,48% | -3,99% | -2,71% | +6,71% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 37,50% | +1,54% | +1,34% | -1,56% | +8,05% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 50 | 60,00% | +2,88% | +3,23% | -3,01% | +8,43% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 53 | 54,72% | +2,90% | +2,60% | -3,09% | +8,19% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 53 | 54,72% | +2,90% | +2,60% | -3,09% | +8,19% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,59% | +4,60% | -2,54% | +8,00% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Tecnico | CALIBRABILE | 47 | 59,57% | +1,52% | +1,55% | -3,65% | +6,72% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Classic technical | CALIBRABILE | 31 | 38,71% | +2,76% | -4,80% | -3,30% | +8,15% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 50,00% | +0,41% | +0,28% | -2,23% | +8,54% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 48 | 58,33% | +2,96% | +4,04% | -3,63% | +9,67% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 50 | 54,00% | +2,86% | +3,32% | -3,68% | +9,40% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 50 | 54,00% | +2,86% | +3,32% | -3,68% | +9,40% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,79% | +5,36% | -2,91% | +9,59% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Tecnico | CALIBRABILE | 44 | 63,64% | +0,85% | +1,72% | -4,37% | +7,00% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Classic technical | CALIBRABILE | 31 | 41,94% | +2,22% | -4,39% | -3,95% | +9,25% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 62,50% | +0,72% | +0,35% | -3,12% | +9,19% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 45 | 68,89% | +5,11% | +7,18% | -3,91% | +13,41% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 46 | 71,74% | +4,82% | +6,86% | -3,86% | +12,97% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 46 | 71,74% | +4,82% | +6,86% | -3,86% | +12,97% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 38 | 76,32% | +5,76% | +8,06% | -3,33% | +13,70% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Tecnico | CALIBRABILE | 40 | 65,00% | +1,56% | +1,12% | -4,65% | +8,64% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Classic technical | CALIBRABILE | 31 | 48,39% | +3,26% | -3,87% | -4,53% | +11,11% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 57,14% | +7,65% | +2,04% | -2,99% | +15,57% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 38 | 78,95% | +9,94% | +8,90% | -3,51% | +20,06% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 40 | 87,50% | +9,95% | +12,91% | -3,56% | +20,13% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 40 | 87,50% | +9,95% | +12,91% | -3,56% | +20,13% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 38 | 89,47% | +10,54% | +13,52% | -3,55% | +20,95% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Tecnico | CALIBRABILE | 33 | 63,64% | +7,02% | -3,84% | -4,34% | +15,23% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Classic technical | CALIBRABILE | 27 | 55,56% | +7,10% | -7,10% | -3,69% | +15,72% | FEEDBACK RAPIDO |
| DOGE | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 75,00% | +12,49% | -0,95% | -1,31% | +25,23% | FEEDBACK RAPIDO |
| DOGE | 30g | Global confluence | BENCHMARK | 31 | 74,19% | +12,41% | +5,21% | -4,45% | +24,50% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Famiglia statistica | CALIBRABILE | 33 | 87,88% | +12,97% | +11,59% | -4,45% | +25,44% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Scanner grezzo | DIAGNOSTICO | 33 | 87,88% | +12,97% | +11,59% | -4,45% | +25,44% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Market regime grezzo | DIAGNOSTICO | 31 | 93,55% | +12,01% | +14,14% | -4,50% | +24,68% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Tecnico | CALIBRABILE | 30 | 40,00% | +11,60% | -11,60% | -4,76% | +23,68% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Classic technical | CALIBRABILE | 22 | 50,00% | +9,38% | -9,38% | -4,86% | +19,29% | FEEDBACK RAPIDO |
| DOGE | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 75,00% | +30,85% | +15,03% | -1,31% | +42,05% | FEEDBACK RAPIDO |
| DOGE | 45g | Global confluence | BENCHMARK | 18 | 5,56% | +20,48% | -17,95% | -6,13% | +37,64% | FEEDBACK RAPIDO |
| DOGE | 45g | Famiglia statistica | CALIBRABILE | 18 | 11,11% | +20,48% | -14,67% | -6,13% | +37,64% | FEEDBACK RAPIDO |
| DOGE | 45g | Scanner grezzo | DIAGNOSTICO | 18 | 11,11% | +20,48% | -14,67% | -6,13% | +37,64% | FEEDBACK RAPIDO |
| DOGE | 45g | Market regime grezzo | DIAGNOSTICO | 16 | 12,50% | +19,51% | -12,97% | -6,42% | +37,15% | FEEDBACK RAPIDO |
| DOGE | 45g | Tecnico | CALIBRABILE | 18 | 0,00% | +20,48% | -20,48% | -6,13% | +37,64% | FEEDBACK RAPIDO |
| DOGE | 45g | Classic technical | CALIBRABILE | 16 | 0,00% | +20,67% | -20,67% | -5,92% | +37,88% | FEEDBACK RAPIDO |
| DOGE | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +30,17% | +30,17% | -1,85% | +44,37% | FEEDBACK RAPIDO |
| DOGE | 60g | Global confluence | BENCHMARK | 3 | 0,00% | +22,53% | -22,53% | -7,62% | +35,88% | FEEDBACK RAPIDO |
| DOGE | 60g | Famiglia statistica | CALIBRABILE | 3 | 0,00% | +22,53% | -22,53% | -7,62% | +35,88% | FEEDBACK RAPIDO |
| DOGE | 60g | Scanner grezzo | DIAGNOSTICO | 3 | 0,00% | +22,53% | -22,53% | -7,62% | +35,88% | FEEDBACK RAPIDO |
| DOGE | 60g | Market regime grezzo | DIAGNOSTICO | 3 | 0,00% | +22,53% | -22,53% | -7,62% | +35,88% | FEEDBACK RAPIDO |
| DOGE | 60g | Tecnico | CALIBRABILE | 3 | 0,00% | +22,53% | -22,53% | -7,62% | +35,88% | FEEDBACK RAPIDO |
| DOGE | 60g | Classic technical | CALIBRABILE | 3 | 0,00% | +22,53% | -22,53% | -7,62% | +35,88% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 53 | 54,72% | +0,65% | +0,53% | -0,06% | +1,56% | PRIMA CALIBRAZIONE |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 55 | 56,36% | +0,36% | +0,35% | -0,28% | +1,24% | PRIMA CALIBRAZIONE |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 58 | 55,17% | +0,40% | +0,28% | -0,25% | +1,27% | PRIMA CALIBRAZIONE |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +0,27% | +0,39% | -0,30% | +0,87% | PRIMA CALIBRAZIONE |
| SOL | 1g | Tecnico | CALIBRABILE | 57 | 50,88% | +0,36% | +0,34% | -0,32% | +1,20% | PRIMA CALIBRAZIONE |
| SOL | 1g | Classic technical | CALIBRABILE | 41 | 51,22% | +0,55% | +0,51% | -0,25% | +1,48% | PRIMA CALIBRAZIONE |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 52 | 51,92% | +1,30% | +1,16% | +0,35% | +2,39% | PRIMA CALIBRAZIONE |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 54 | 48,15% | +0,92% | +0,48% | -0,03% | +1,76% | PRIMA CALIBRAZIONE |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 57 | 47,37% | +0,89% | +0,43% | -0,03% | +1,81% | PRIMA CALIBRAZIONE |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +0,76% | +0,78% | -0,00% | +1,60% | PRIMA CALIBRAZIONE |
| SOL | 2g | Tecnico | CALIBRABILE | 56 | 44,64% | +0,83% | +0,28% | -0,06% | +1,92% | PRIMA CALIBRAZIONE |
| SOL | 2g | Classic technical | CALIBRABILE | 40 | 52,50% | +0,93% | +0,90% | +0,01% | +1,91% | PRIMA CALIBRAZIONE |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 51 | 58,82% | +2,09% | +1,91% | -1,30% | +4,35% | PRIMA CALIBRAZIONE |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 53 | 50,94% | +1,59% | +1,04% | -1,60% | +3,85% | PRIMA CALIBRAZIONE |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 56 | 50,00% | +1,53% | +0,97% | -1,58% | +3,82% | PRIMA CALIBRAZIONE |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +1,43% | +1,38% | -1,48% | +3,53% | PRIMA CALIBRAZIONE |
| SOL | 3g | Tecnico | CALIBRABILE | 55 | 50,91% | +1,38% | +0,19% | -1,65% | +3,57% | PRIMA CALIBRAZIONE |
| SOL | 3g | Classic technical | CALIBRABILE | 39 | 56,41% | +1,33% | +1,19% | -1,60% | +3,53% | PRIMA CALIBRAZIONE |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 49 | 63,27% | +3,53% | +3,42% | -1,95% | +6,85% | PRIMA CALIBRAZIONE |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 51 | 56,86% | +2,85% | +1,78% | -2,26% | +6,16% | PRIMA CALIBRAZIONE |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 54 | 55,56% | +2,73% | +1,64% | -2,24% | +6,04% | PRIMA CALIBRAZIONE |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +2,66% | +2,88% | -2,09% | +5,82% | PRIMA CALIBRAZIONE |
| SOL | 5g | Tecnico | CALIBRABILE | 53 | 50,94% | +2,73% | -0,28% | -2,40% | +5,93% | PRIMA CALIBRAZIONE |
| SOL | 5g | Classic technical | CALIBRABILE | 37 | 62,16% | +2,06% | +1,90% | -2,33% | +5,15% | PRIMA CALIBRAZIONE |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 47 | 65,96% | +4,87% | +4,99% | -2,40% | +8,75% | PRIMA CALIBRAZIONE |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 49 | 61,22% | +4,08% | +2,78% | -2,72% | +8,00% | PRIMA CALIBRAZIONE |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 52 | 61,54% | +3,84% | +2,63% | -2,72% | +7,76% | PRIMA CALIBRAZIONE |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 34 | 61,76% | +4,35% | +4,41% | -2,45% | +7,76% | PRIMA CALIBRAZIONE |
| SOL | 7g | Tecnico | CALIBRABILE | 51 | 43,14% | +3,79% | -1,12% | -2,89% | +7,70% | PRIMA CALIBRAZIONE |
| SOL | 7g | Classic technical | CALIBRABILE | 35 | 54,29% | +2,21% | +2,26% | -2,93% | +6,07% | PRIMA CALIBRAZIONE |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 44 | 68,18% | +6,85% | +7,02% | -2,57% | +11,18% | PRIMA CALIBRAZIONE |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 46 | 63,04% | +5,96% | +4,97% | -2,98% | +10,08% | PRIMA CALIBRAZIONE |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 49 | 61,22% | +5,59% | +4,68% | -3,01% | +9,70% | PRIMA CALIBRAZIONE |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 34 | 64,71% | +6,91% | +6,75% | -2,80% | +10,27% | PRIMA CALIBRAZIONE |
| SOL | 10g | Tecnico | CALIBRABILE | 48 | 47,92% | +4,98% | -2,02% | -3,21% | +9,28% | PRIMA CALIBRAZIONE |
| SOL | 10g | Classic technical | CALIBRABILE | 32 | 59,38% | +2,24% | +2,35% | -3,29% | +6,84% | PRIMA CALIBRAZIONE |
| SOL | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 80,00% | +3,41% | +3,41% | -2,87% | +9,17% | FEEDBACK RAPIDO |
| SOL | 10g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 14g | Global confluence | BENCHMARK | 40 | 80,00% | +10,54% | +11,45% | -2,55% | +16,22% | PRIMA CALIBRAZIONE |
| SOL | 14g | Famiglia statistica | CALIBRABILE | 42 | 80,95% | +9,94% | +8,98% | -2,92% | +14,91% | PRIMA CALIBRAZIONE |

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

Generato: 2026-09-09 05:33 UTC

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
| BTC | 61 | UTILE | 60 | 17 | 1 | 0 | Famiglia statistica | 1g | 53,33% | +0,39% | campione utile, valutare con prudenza |
| SOL | 61 | PRIMA CALIBRAZIONE | 57 | 23 | 0 | 0 | Tecnico | 1g | 50,88% | +0,34% | prima calibrazione possibile, solo modifiche leggere |
| DOGE | 61 | PRIMA CALIBRAZIONE | 59 | 25 | 0 | 0 | Famiglia statistica | 1g | 57,63% | +0,43% | prima calibrazione possibile, solo modifiche leggere |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Classic technical | 24 | 37,50% | +0,37% | +0,81% | +0,13% | +1,33% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Famiglia statistica | 60 | 53,33% | +0,39% | +0,39% | -0,05% | +0,93% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 1g | BREVE | Microstruttura exchange | 5 | 40,00% | -0,17% | -0,17% | -0,60% | +0,27% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 55 | 40,00% | +0,14% | +0,51% | +0,06% | +1,05% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 2g | BREVE | Classic technical | 24 | 41,67% | +0,55% | +1,18% | +0,59% | +1,89% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Famiglia statistica | 59 | 54,24% | +0,81% | +0,81% | +0,24% | +1,50% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 2g | BREVE | Microstruttura exchange | 5 | 40,00% | +0,73% | +0,73% | +0,13% | +1,27% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 54 | 44,44% | +0,22% | +0,98% | +0,41% | +1,67% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 3g | BREVE | Classic technical | 24 | 41,67% | +0,20% | +1,81% | -0,58% | +3,31% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Famiglia statistica | 58 | 55,17% | +1,23% | +1,23% | -0,95% | +2,84% | PESO OK | 0,0 | MEDIA |
| BTC | 3g | BREVE | Microstruttura exchange | 5 | 40,00% | +0,35% | +0,35% | -1,11% | +1,90% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 53 | 37,74% | -0,06% | +1,53% | -0,77% | +3,11% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 5g | SETTIMANALE | Classic technical | 24 | 50,00% | -1,14% | +3,70% | -1,03% | +5,94% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 56 | 53,57% | +2,15% | +2,15% | -1,49% | +4,44% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 5g | SETTIMANALE | Microstruttura exchange | 4 | 25,00% | -0,34% | -0,34% | -1,71% | +2,56% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 51 | 45,10% | -0,86% | +2,46% | -1,30% | +4,81% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 7g | SETTIMANALE | Classic technical | 22 | 45,45% | -2,91% | +5,46% | -1,23% | +8,53% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 54 | 61,11% | +2,96% | +2,96% | -1,76% | +5,67% | PESO OK | 0,0 | MEDIA |
| BTC | 7g | SETTIMANALE | Microstruttura exchange | 3 | 66,67% | +0,68% | +0,68% | -1,68% | +3,81% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 49 | 42,86% | -1,72% | +3,49% | -1,55% | +6,14% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 10g | SETTIMANALE | Classic technical | 19 | 57,89% | -4,18% | +6,93% | -1,23% | +10,01% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 51 | 66,67% | +3,86% | +3,86% | -2,00% | +6,75% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| BTC | 10g | SETTIMANALE | Microstruttura exchange | 3 | 66,67% | +0,54% | +0,54% | -2,46% | +3,88% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 46 | 47,83% | -1,38% | +4,40% | -1,76% | +7,35% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 14g | SWING | Classic technical | 15 | 46,67% | -4,69% | +8,42% | -0,87% | +12,10% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Famiglia statistica | 47 | 63,83% | +5,79% | +5,79% | -2,10% | +9,18% | PESO OK | 0,0 | MEDIA |
| BTC | 14g | SWING | Microstruttura exchange | 3 | 33,33% | -0,03% | -0,03% | -2,90% | +4,64% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 42 | 59,52% | +0,86% | +6,63% | -1,82% | +10,07% | PESO OK | 0,0 | MEDIA |
| BTC | 21g | SWING | Classic technical | 8 | 0,00% | -19,34% | +19,34% | -0,83% | +22,19% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Famiglia statistica | 40 | 70,00% | +10,28% | +10,28% | -2,38% | +13,97% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| BTC | 21g | SWING | Microstruttura exchange | 1 | 100,00% | +1,21% | +1,21% | -3,06% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Tecnico | 35 | 34,29% | -1,49% | +11,52% | -2,08% | +15,27% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 30g | MEDIO | Classic technical | 4 | 0,00% | -24,06% | +24,06% | -1,55% | +28,48% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Famiglia statistica | 33 | 84,85% | +13,53% | +13,53% | -3,02% | +17,55% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| BTC | 30g | MEDIO | Microstruttura exchange | 1 | 100,00% | +0,16% | +0,16% | -3,06% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Tecnico | 28 | 42,86% | -2,44% | +13,68% | -2,76% | +18,04% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Famiglia statistica | 18 | 100,00% | +22,59% | +22,59% | -3,27% | +26,54% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Microstruttura exchange | 1 | 100,00% | +20,42% | +20,42% | -3,06% | +26,73% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Tecnico | 15 | 33,33% | -7,88% | +22,81% | -2,97% | +26,99% | OSSERVA | 0,0 | BASSA |
| BTC | 60g | MEDIO | Famiglia statistica | 3 | 100,00% | +24,28% | +24,28% | -3,05% | +29,12% | OSSERVA | 0,0 | BASSA |
| BTC | 60g | MEDIO | Tecnico | 2 | 0,00% | -24,78% | +24,78% | -2,93% | +29,27% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 34 | 41,18% | -0,49% | +0,22% | -0,44% | +0,96% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 1g | BREVE | Famiglia statistica | 59 | 57,63% | +0,43% | +0,39% | -0,28% | +1,34% | PESO OK | 0,0 | MEDIA |
| DOGE | 1g | BREVE | Microstruttura exchange | 9 | 55,56% | +1,78% | +2,13% | +0,65% | +2,81% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 53 | 52,83% | +0,47% | +0,31% | -0,39% | +1,24% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Classic technical | 33 | 42,42% | -1,16% | +0,60% | -0,16% | +1,59% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Famiglia statistica | 58 | 55,17% | +0,69% | +0,80% | +0,01% | +2,01% | PESO OK | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Microstruttura exchange | 9 | 44,44% | +2,61% | +2,90% | +2,02% | +4,90% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 52 | 55,77% | +0,78% | +0,42% | -0,35% | +1,62% | PESO OK | 0,0 | MEDIA |
| DOGE | 3g | BREVE | Classic technical | 32 | 31,25% | -2,09% | +1,23% | -1,90% | +4,10% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 3g | BREVE | Famiglia statistica | 57 | 52,63% | +1,00% | +1,28% | -1,68% | +3,98% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 3g | BREVE | Microstruttura exchange | 9 | 44,44% | +2,26% | +2,49% | -0,95% | +6,11% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 51 | 47,06% | +0,78% | +0,46% | -1,95% | +3,04% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 5g | SETTIMANALE | Classic technical | 31 | 38,71% | -3,99% | +2,48% | -2,71% | +6,71% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 55 | 49,09% | +1,81% | +2,25% | -2,55% | +6,40% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 5g | SETTIMANALE | Microstruttura exchange | 8 | 37,50% | +1,34% | +1,54% | -1,56% | +8,05% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 49 | 59,18% | +0,92% | +1,18% | -3,00% | +5,35% | PESO OK | 0,0 | MEDIA |
| DOGE | 7g | SETTIMANALE | Classic technical | 31 | 38,71% | -4,80% | +2,76% | -3,30% | +8,15% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 53 | 54,72% | +2,60% | +2,90% | -3,09% | +8,19% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 7g | SETTIMANALE | Microstruttura exchange | 8 | 50,00% | +0,28% | +0,41% | -2,23% | +8,54% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 47 | 59,57% | +1,55% | +1,52% | -3,65% | +6,72% | PESO OK | 0,0 | MEDIA |
| DOGE | 10g | SETTIMANALE | Classic technical | 31 | 41,94% | -4,39% | +2,22% | -3,95% | +9,25% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 50 | 54,00% | +3,32% | +2,86% | -3,68% | +9,40% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 10g | SETTIMANALE | Microstruttura exchange | 8 | 62,50% | +0,35% | +0,72% | -3,12% | +9,19% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 44 | 63,64% | +1,72% | +0,85% | -4,37% | +7,00% | PESO OK | 0,0 | MEDIA |
| DOGE | 14g | SWING | Classic technical | 31 | 48,39% | -3,87% | +3,26% | -4,53% | +11,11% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 14g | SWING | Famiglia statistica | 46 | 71,74% | +6,86% | +4,82% | -3,86% | +12,97% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 14g | SWING | Microstruttura exchange | 7 | 57,14% | +2,04% | +7,65% | -2,99% | +15,57% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 40 | 65,00% | +1,12% | +1,56% | -4,65% | +8,64% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 21g | SWING | Classic technical | 27 | 55,56% | -7,10% | +7,10% | -3,69% | +15,72% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Famiglia statistica | 40 | 87,50% | +12,91% | +9,95% | -3,56% | +20,13% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 21g | SWING | Microstruttura exchange | 4 | 75,00% | -0,95% | +12,49% | -1,31% | +25,23% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Tecnico | 33 | 63,64% | -3,84% | +7,02% | -4,34% | +15,23% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 30g | MEDIO | Classic technical | 22 | 50,00% | -9,38% | +9,38% | -4,86% | +19,29% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Famiglia statistica | 33 | 87,88% | +11,59% | +12,97% | -4,45% | +25,44% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 30g | MEDIO | Microstruttura exchange | 4 | 75,00% | +15,03% | +30,85% | -1,31% | +42,05% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Tecnico | 30 | 40,00% | -11,60% | +11,60% | -4,76% | +23,68% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 45g | MEDIO | Classic technical | 16 | 0,00% | -20,67% | +20,67% | -5,92% | +37,88% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Famiglia statistica | 18 | 11,11% | -14,67% | +20,48% | -6,13% | +37,64% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Microstruttura exchange | 2 | 100,00% | +30,17% | +30,17% | -1,85% | +44,37% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Tecnico | 18 | 0,00% | -20,48% | +20,48% | -6,13% | +37,64% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Classic technical | 3 | 0,00% | -22,53% | +22,53% | -7,62% | +35,88% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Famiglia statistica | 3 | 0,00% | -22,53% | +22,53% | -7,62% | +35,88% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Tecnico | 3 | 0,00% | -22,53% | +22,53% | -7,62% | +35,88% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Classic technical | 41 | 51,22% | +0,51% | +0,55% | -0,25% | +1,48% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 1g | BREVE | Famiglia statistica | 55 | 56,36% | +0,35% | +0,36% | -0,28% | +1,24% | PESO OK | 0,0 | MEDIA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 57 | 50,88% | +0,34% | +0,36% | -0,32% | +1,20% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Classic technical | 40 | 52,50% | +0,90% | +0,93% | +0,01% | +1,91% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Famiglia statistica | 54 | 48,15% | +0,48% | +0,92% | -0,03% | +1,76% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Microstruttura exchange | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 56 | 44,64% | +0,28% | +0,83% | -0,06% | +1,92% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Classic technical | 39 | 56,41% | +1,19% | +1,33% | -1,60% | +3,53% | PESO OK | 0,0 | MEDIA |
| SOL | 3g | BREVE | Famiglia statistica | 53 | 50,94% | +1,04% | +1,59% | -1,60% | +3,85% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Microstruttura exchange | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 55 | 50,91% | +0,19% | +1,38% | -1,65% | +3,57% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Classic technical | 37 | 62,16% | +1,90% | +2,06% | -2,33% | +5,15% | PESO OK | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 51 | 56,86% | +1,78% | +2,85% | -2,26% | +6,16% | PESO OK | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 53 | 50,94% | -0,28% | +2,73% | -2,40% | +5,93% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Classic technical | 35 | 54,29% | +2,26% | +2,21% | -2,93% | +6,07% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 49 | 61,22% | +2,78% | +4,08% | -2,72% | +8,00% | PESO OK | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 51 | 43,14% | -1,12% | +3,79% | -2,89% | +7,70% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 10g | SETTIMANALE | Classic technical | 32 | 59,38% | +2,35% | +2,24% | -3,29% | +6,84% | PESO OK | 0,0 | MEDIA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 46 | 63,04% | +4,97% | +5,96% | -2,98% | +10,08% | PESO OK | 0,0 | MEDIA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Microstruttura exchange | 5 | 80,00% | +3,41% | +3,41% | -2,87% | +9,17% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 48 | 47,92% | -2,02% | +4,98% | -3,21% | +9,28% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 14g | SWING | Classic technical | 28 | 53,57% | +1,89% | +3,67% | -3,23% | +8,33% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Famiglia statistica | 42 | 80,95% | +8,98% | +9,94% | -2,92% | +14,91% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 14g | SWING | Frattale SOL | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Microstruttura exchange | 5 | 80,00% | +8,16% | +8,16% | -3,30% | +14,31% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Tecnico | 44 | 40,91% | -4,51% | +7,59% | -3,25% | +12,86% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 21g | SWING | Classic technical | 21 | 38,10% | -11,18% | +11,18% | -4,64% | +15,32% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Famiglia statistica | 36 | 86,11% | +18,74% | +17,19% | -3,75% | +22,71% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 21g | SWING | Frattale SOL | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Microstruttura exchange | 2 | 50,00% | +17,59% | +17,59% | -5,94% | +22,78% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Tecnico | 37 | 32,43% | -14,62% | +13,51% | -4,47% | +18,90% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 30g | MEDIO | Classic technical | 21 | 9,52% | -26,53% | +26,53% | -4,64% | +32,91% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Famiglia statistica | 29 | 89,66% | +23,92% | +24,28% | -4,99% | +30,62% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Frattale SOL | 1 | 0,00% | -4,50% | -4,50% | -9,39% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Microstruttura exchange | 2 | 100,00% | +22,28% | +22,28% | -5,94% | +27,20% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Tecnico | 32 | 12,50% | -21,52% | +20,94% | -5,31% | +26,83% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 45g | MEDIO | Classic technical | 10 | 0,00% | -36,35% | +36,35% | -6,72% | +45,19% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Famiglia statistica | 14 | 42,86% | -1,10% | +32,72% | -7,61% | +40,35% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Frattale SOL | 1 | 100,00% | +19,26% | +19,26% | -9,39% | +23,73% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Microstruttura exchange | 1 | 100,00% | +32,54% | +32,54% | -9,62% | +40,68% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Tecnico | 18 | 22,22% | -22,55% | +33,48% | -7,44% | +40,82% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Famiglia statistica | 2 | 0,00% | -34,09% | +34,09% | -9,20% | +41,33% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Frattale SOL | 1 | 100,00% | +35,29% | +35,29% | -9,39% | +41,04% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Tecnico | 3 | 100,00% | +34,06% | +34,06% | -9,18% | +41,37% | OSSERVA | 0,0 | BASSA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 57 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 38 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 60 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Classic technical | 72 | 40,28% | +0,37% |
| BTC | BREVE | Famiglia statistica | 177 | 54,24% | +0,80% |
| BTC | BREVE | Microstruttura exchange | 15 | 40,00% | +0,30% |
| BTC | BREVE | Tecnico | 162 | 40,74% | +0,10% |
| BTC | SETTIMANALE | Classic technical | 65 | 50,77% | -2,63% |
| BTC | SETTIMANALE | Famiglia statistica | 161 | 60,25% | +2,96% |
| BTC | SETTIMANALE | Microstruttura exchange | 10 | 50,00% | +0,23% |
| BTC | SETTIMANALE | Tecnico | 146 | 45,21% | -1,31% |
| BTC | SWING | Classic technical | 23 | 30,43% | -9,78% |
| BTC | SWING | Famiglia statistica | 87 | 66,67% | +7,86% |
| BTC | SWING | Microstruttura exchange | 4 | 50,00% | +0,28% |
| BTC | SWING | Tecnico | 77 | 48,05% | -0,21% |
| BTC | MEDIO | Classic technical | 4 | 0,00% | -24,06% |
| BTC | MEDIO | Famiglia statistica | 54 | 90,74% | +17,15% |
| BTC | MEDIO | Microstruttura exchange | 2 | 100,00% | +10,29% |
| BTC | MEDIO | Tecnico | 45 | 37,78% | -5,25% |
| DOGE | BREVE | Classic technical | 99 | 38,38% | -1,23% |
| DOGE | BREVE | Famiglia statistica | 174 | 55,17% | +0,70% |
| DOGE | BREVE | Microstruttura exchange | 27 | 48,15% | +2,22% |
| DOGE | BREVE | Tecnico | 156 | 51,92% | +0,67% |
| DOGE | SETTIMANALE | Classic technical | 93 | 39,78% | -4,39% |
| DOGE | SETTIMANALE | Famiglia statistica | 158 | 52,53% | +2,55% |
| DOGE | SETTIMANALE | Microstruttura exchange | 24 | 50,00% | +0,65% |
| DOGE | SETTIMANALE | Tecnico | 140 | 60,71% | +1,38% |
| DOGE | SWING | Classic technical | 58 | 51,72% | -5,37% |
| DOGE | SWING | Famiglia statistica | 86 | 79,07% | +9,67% |
| DOGE | SWING | Microstruttura exchange | 11 | 63,64% | +0,95% |
| DOGE | SWING | Tecnico | 73 | 64,38% | -1,12% |
| DOGE | MEDIO | Classic technical | 41 | 26,83% | -14,75% |
| DOGE | MEDIO | Famiglia statistica | 54 | 57,41% | +0,94% |
| DOGE | MEDIO | Microstruttura exchange | 6 | 83,33% | +20,07% |
| DOGE | MEDIO | Tecnico | 51 | 23,53% | -15,38% |
| SOL | BREVE | Classic technical | 120 | 53,33% | +0,86% |
| SOL | BREVE | Famiglia statistica | 162 | 51,85% | +0,62% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 15 | 53,33% | +1,74% |
| SOL | BREVE | Tecnico | 168 | 48,81% | +0,27% |
| SOL | SETTIMANALE | Classic technical | 104 | 58,65% | +2,16% |
| SOL | SETTIMANALE | Famiglia statistica | 146 | 60,27% | +3,12% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Microstruttura exchange | 15 | 66,67% | +3,06% |
| SOL | SETTIMANALE | Tecnico | 152 | 47,37% | -1,11% |
| SOL | SWING | Classic technical | 49 | 46,94% | -3,71% |
| SOL | SWING | Famiglia statistica | 78 | 83,33% | +13,48% |
| SOL | SWING | Frattale SOL | 2 | 0,00% | -3,49% |
| SOL | SWING | Microstruttura exchange | 7 | 71,43% | +10,86% |
| SOL | SWING | Tecnico | 81 | 37,04% | -9,13% |
| SOL | MEDIO | Classic technical | 31 | 6,45% | -29,70% |
| SOL | MEDIO | Famiglia statistica | 45 | 71,11% | +13,55% |
| SOL | MEDIO | Frattale SOL | 3 | 66,67% | +16,68% |
| SOL | MEDIO | Microstruttura exchange | 3 | 100,00% | +25,70% |
| SOL | MEDIO | Tecnico | 53 | 20,75% | -18,72% |

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
| BTC     |         61 |              33 |          28 | OSSERVAZIONE 30+ | 0,00%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| SOL     |         61 |              33 |          28 | OSSERVAZIONE 30+ | 3,03%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| DOGE    |         61 |              33 |          28 | OSSERVAZIONE 30+ | 6,06%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |

Regola: sotto 60 controlli osserva soltanto; da 100+ controlli può diventare utile per correggere rischio spot/leva nel Decision Report.

## Ultima lettura rapida

| Asset   | Rischio spot   | Rischio leva   | Nota leva                                                               |
|:--------|:---------------|:---------------|:------------------------------------------------------------------------|
| BTC     | MEDIO          | MOLTO ALTO     | spot preferibile; leva molto pericolosa anche 2x/3x senza margine largo |
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

Generato: 2026-09-09 05:33 UTC


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
| BTC | +6 | MODERATAMENTE POSITIVA | Costruttivo prudente | MEDIA | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE | Prima resistenza sopra 82.262; conferma del doppio minimo sopra 65.402. | Sotto 76.248 il quadro tecnico peggiora. |
| SOL | +5 | MODERATAMENTE POSITIVA | Costruttivo prudente | MEDIA | HOLD / TRANCHE PICCOLE, NO LEVA | Doppio minimo target raggiunto finché mantiene 78,73; nuova conferma tecnica sopra 110,04; milestone analogiche 109,65 / 137,24, valide soltanto se rientra anche il gap frattale. | Allarmi sotto 90,88 / 97,45 / 62,19. |
| DOGE | +3 | MODERATAMENTE POSITIVA | Costruttivo prudente | MEDIA | SOLO TRANCHE PICCOLE / NO LEVA | Sopra 0.09998 migliora; sopra 0.06933 viene invalidato il pattern ribassista dominante. | Sotto 0.08028 il rischio ribassista aumenta. |

## Punteggi per modulo

| Asset | Scanner grezzo | Market grezzo | Famiglia statistica | Scanner path | Tecnico | Classic tech | Frattale SOL | Fractal path | RSI top-cycle | Lifecycle EMA | Exchange flow | Futures | Daily change | Totale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +3 | 0 | +3 | 0 | +3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | +6 |
| SOL | +2 | 0 | +2 | 0 | +3 | +1 | 0 | 0 | 0 | 0 | 0 | 0 | -1 | +5 |
| DOGE | -1 | 0 | -1 | 0 | +3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | +1 | +3 |

Le colonne **Scanner grezzo** e **Market grezzo** sono diagnostiche: nel totale entra soltanto la colonna **Famiglia statistica**.

## Lettura asset per asset

### BTC

- Confluenza: **MODERATAMENTE POSITIVA**
- Bias: **Costruttivo prudente**
- Punteggio finale: **+6**
- Affidabilità: **MEDIA**
- Azione coerente: **ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE**

BTC è l'asset messo meglio nel breve, ma lo score statistico ora conta Scanner e Market Regime una sola volta. La struttura macro resta debole: ha più senso accumulare a tranche sui pullback che inseguire il prezzo vicino alle resistenze.

Dettaglio moduli:

- Famiglia statistica: **+3** — Scanner grezzo +3, Market Regime grezzo 0, match regime 0. Regime ignorato: meno di 5 match utili. Punteggio contato nel Global: +3.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **+3** — Casi positivi 80,00%, return centrale 30g +20,27%. Direzione scanner: SALITA. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **0** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 0, positivi 30g n/a, return p50 n/a.
- Scanner path: **0** — Controlli disponibili 58. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **+3** — Score tecnico 7/12, verdetto rialzista tecnico, trend rialzista, struttura rialzista con massimi e minimi crescenti, divergenza nessuna, Wyckoff markup / fase rialzista, pattern score 0 (rialzista Doppio minimo / TARGET RAGGIUNTO; ribassista Doppio massimo / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **0** — Score classico 1/12, verdetto NEUTRALE / MISTO, stage STAGE 3 / DISTRIBUZIONE O PAUSA, struttura VOLATILITÀ IN ESPANSIONE, Wyckoff SIGN OF STRENGTH POSSIBILE, volatilità locale BASSO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Non applicabile a questo asset.
- Fractal path: **0** — Non applicabile a questo asset.
- RSI top-cycle: **0** — Non applicabile a questo asset.
- Lifecycle EMA: **0** — Non applicabile a questo asset.
- Exchange flow: **0** — Flow +1.75, derivati +0.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +0.00; exchange 3/3, copertura 100%, consenso bull 1, bear 0, divergenze 1, campioni 4h 9 su 4.00h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias LEGGERMENTE POSITIVA / NON PESATA; confidenza BASSA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Misto, forza 1/5.
- Daily change: **0** — BTC: nessun cambiamento forte in peggioramento rispetto a ieri.

Conferme: Prima resistenza sopra 82.262; conferma del doppio minimo sopra 65.402.

Invalidazioni: Sotto 76.248 il quadro tecnico peggiora.

### SOL

- Confluenza: **MODERATAMENTE POSITIVA**
- Bias: **Costruttivo prudente**
- Punteggio finale: **+5**
- Affidabilità: **MEDIA**
- Azione coerente: **HOLD / TRANCHE PICCOLE, NO LEVA**

SOL ha una confluenza costruttiva, ma va ancora trattato come setup anticipato. La conferma vera arriva solo sopra le resistenze tecniche e con rientro del gap frattale. Il modulo lifecycle/EMA200 resta utile come contesto, ma non aumenta il punteggio Global.

Dettaglio moduli:

- Famiglia statistica: **+2** — Scanner grezzo +2, Market Regime grezzo 0, match regime 0. Regime ignorato: meno di 5 match utili. Punteggio contato nel Global: +2.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **+2** — Casi positivi 62,50%, return centrale 30g +17,40%. Direzione scanner: SALITA. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **0** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 0, positivi 30g n/a, return p50 n/a.
- Scanner path: **0** — Controlli disponibili 58. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **+3** — Score tecnico 7/12, verdetto rialzista tecnico, trend rialzista, struttura rialzista con massimi e minimi crescenti, divergenza nessuna, Wyckoff markup / fase rialzista, pattern score 0 (rialzista Doppio minimo / TARGET RAGGIUNTO; ribassista Doppio massimo / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **+1** — Score classico 5/12, verdetto COSTRUTTIVO / CONFERMA PARZIALE, stage STAGE 3 / DISTRIBUZIONE O PAUSA, struttura MASSIMI E MINIMI CRESCENTI, Wyckoff SIGN OF STRENGTH POSSIBILE, volatilità locale MEDIO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Verdetto ANALOGIA DEBOLE / SCENARIO SECONDARIO, somiglianza strutturale +69,05%, aderenza live +71,98%, errore live +14,01%, gap corrente +14,28%, peso operativo 0, tracking STRUTTURA STABILE, fase FRATTALE SOLO DI CONTESTO, rischio ALTO.
- Fractal path: **0** — Controlli disponibili 55, ma percorso ancorato non aderente: gap +14,28%, errore live +14,01%. Peso 0.
- RSI top-cycle: **0** — Rischio top-cycle RSI: BASSO.
- Lifecycle EMA: **0** — Contesto non pesato nel Global. Lifecycle score 2, bias CONTESTO DA OSSERVARE, EMA200 111,27 $, upside EMA200 +6,76%, gap EMA50/EMA200 -5,68%, hit EMA200 12w +83,33%, trend STABILE / DA CONFERMARE. Peso Global forzato a 0.
- Exchange flow: **0** — Flow +1.75, derivati +0.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +0.00; exchange 3/3, copertura 100%, consenso bull 0, bear 1, divergenze 1, campioni 4h 9 su 4.00h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias LEGGERMENTE POSITIVA / NON PESATA; confidenza BASSA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Misto, forza 1/5.
- Daily change: **-1** — SOL: cambiamento medio in peggioramento rispetto a ieri.

Conferme: Doppio minimo target raggiunto finché mantiene 78,73; nuova conferma tecnica sopra 110,04; milestone analogiche 109,65 / 137,24, valide soltanto se rientra anche il gap frattale.

Invalidazioni: Allarmi sotto 90,88 / 97,45 / 62,19.

### DOGE

- Confluenza: **MODERATAMENTE POSITIVA**
- Bias: **Costruttivo prudente**
- Punteggio finale: **+3**
- Affidabilità: **MEDIA**
- Azione coerente: **SOLO TRANCHE PICCOLE / NO LEVA**

DOGE non ha ancora una confluenza pulita. Serve conferma tecnica prima di trattarlo come asset forte.

Dettaglio moduli:

- Famiglia statistica: **-1** — Scanner grezzo -1, Market Regime grezzo 0, match regime 0. Regime ignorato: meno di 5 match utili. Punteggio contato nel Global: -1.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **-1** — Casi positivi 37,50%, return centrale 30g -8,47%. Direzione scanner: DISCESA. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **0** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 0, positivi 30g n/a, return p50 n/a.
- Scanner path: **0** — Controlli disponibili 58. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **+3** — Score tecnico 10/12, verdetto rialzista tecnico, trend rialzista, struttura rialzista con massimi e minimi crescenti, divergenza nessuna, Wyckoff markup / fase rialzista, pattern score 0 (rialzista Doppio minimo / TARGET RAGGIUNTO; ribassista Doppio massimo / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **0** — Score classico 4/12, verdetto ANTICIPATO / COSTRUTTIVO MA NON CONFERMATO, stage STAGE 3 / DISTRIBUZIONE O PAUSA, struttura COMPRESSIONE / TRIANGOLO POSSIBILE, Wyckoff ACCUMULO POSSIBILE / RANGE BASSO, volatilità locale MEDIO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Non applicabile a questo asset.
- Fractal path: **0** — Non applicabile a questo asset.
- RSI top-cycle: **0** — Non applicabile a questo asset.
- Lifecycle EMA: **0** — Non applicabile a questo asset.
- Exchange flow: **0** — Flow +1.75, derivati +0.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +0.00; exchange 3/3, copertura 100%, consenso bull 1, bear 1, divergenze 0, campioni 4h 9 su 4.00h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias LEGGERMENTE POSITIVA / NON PESATA; confidenza BASSA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Rischio sotto, forza 2/5.
- Daily change: **+1** — DOGE: cambiamento medio in miglioramento rispetto a ieri.

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

Generato: 2026-09-09 05:33 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [btc_macro_cycle_report.md](btc_macro_cycle_report.md)

Questo modulo descrive il contesto macro di Bitcoin. Non genera entrate tattiche, non autorizza leva e pesa **0** nel Global Confluence.

## Sintesi

| Voce | Valore | Lettura |
| --- | --- | --- |
| Prezzo BTC | 78.978 $ | prezzo corrente |
| Power Law centrale | 124.966 $ | deviazione -36,80% |
| Banda p10-p90 | 77.598 $ / 315.224 $ | BASSA NEL CORRIDOIO |
| Percentile residuo | 11,68% | posizione storica nel corridoio |
| Esponente β | 5,8037 | R² log-log 91,93% |
| Stabilità β | BASSA | range 1,3166 cambiando finestra |
| Ultimo halving | 2024-04-19 | 873 giorni fa |
| Fase ciclo | 59,75% | percentuale indicativa del ciclo quadriennale |
| Peso Global | 0 | CONTESTO MACRO / DIAGNOSTICO |

La Power Law viene trattata come regressione empirica, non come legge fisica. Il report mostra quanto cambia l'esponente usando finestre iniziali diverse e la confronta con il benchmark ingenuo 'prezzo invariato'.

## Bitcoin Power Law

- Campione: 2014-09-17 → 2026-09-09 (4375 osservazioni)
- Formula stimata: prezzo ≈ exp(-39.0582) × giorni^5.8037
- Prezzo centrale oggi: **124.966 $**
- Posizione corrente: **BASSA NEL CORRIDOIO**, percentile 11,68%
- Scarto dal centro: **-36,80%**

![Bitcoin Power Law](btc_power_law_chart.png)

![Bitcoin Power Law log-log](btc_power_law_loglog_chart.png)

### Stabilità dell'esponente

| Inizio campione | β | R² log-log |
| --- | --- | --- |
| 2014 | 5,8037 | 91,93% |
| 2015 | 5,8858 | 91,48% |
| 2016 | 5,5698 | 87,73% |
| 2017 | 4,8421 | 82,92% |
| 2018 | 4,5693 | 78,43% |

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
| 2012-11-28 → 2016-07-09 | 2015-01-25 | -5,91% | -10,77% | +13,62% | +54,39% |
| 2016-07-09 → 2020-05-11 | 2018-10-25 | -40,08% | -44,64% | -13,96% | +33,73% |
| 2020-05-11 → 2024-04-19 | 2022-09-18 | -0,44% | -13,51% | +41,22% | +37,77% |

Campione molto piccolo: questi rendimenti sono contesto di ciclo, non probabilità affidabili.

## SOL/BTC e DOGE/BTC dentro il tempo Bitcoin

![Altcoin nel ciclo BTC](alt_btc_cycle_spirals.png)

| Asset | Coppia | Forza vs BTC | Score raw | Candidato | 30g | Peso Global |
| --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | SOVRAPERFORMA BTC | 4 | 1 | 12.33191980361379 | 0 |
| DOGE | DOGE/BTC | RELATIVA MISTA / NON CONFERMATA | -1 | 0 | 6.911327661015609 | 0 |

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

Generato: 2026-09-09 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [relative_strength_btc_report.md](relative_strength_btc_report.md)

Questo modulo controlla se SOL e DOGE stanno davvero battendo Bitcoin. Una salita in USD accompagnata da una coppia ALT/BTC ribassista è spesso soltanto trascinamento di BTC.

**Protezione iniziale:** il candidato relativo è limitato a -1/0/+1, ma il peso nel Global resta **0**. La coppia BTC conferma o indebolisce il tecnico USD; non viene sommata come secondo modulo indipendente.

## Sintesi

| Asset | Coppia | Prezzo | Score raw | Candidato | Peso Global | Forza vs BTC | Confidenza | 30g | Tecnico USD | Lettura combinata |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | 0.00131990 | +4 | +1 | 0 | SOVRAPERFORMA BTC | BASSA | +12,33% | RIALZISTA | CONFERMA FORTE: sale in USD e batte BTC |
| DOGE | DOGE/BTC | 0.00000114 | -1 | 0 | 0 | RELATIVA MISTA / NON CONFERMATA | BASSA | +6,91% | RIALZISTA | QUADRO MISTO / NESSUNA CONFERMA RELATIVA |

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
- **Rendimenti relativi:** 7g +2,16%; 30g +12,33%; 90g +28,39%; 180g +7,13%
- **Daily:** RSI 61.22; MA50 0.00121572; MA200 0.00118269
- **Weekly:** MA30 0.00118876; RSI 57.98
- **Livelli:** supporto 0.00127500; resistenza 0.00134900; breakout 60g 0.00136900; breakdown 60g 0.00112700
- **Pattern:** DOPPIO MINIMO / TARGET RAGGIUNTO; neckline 0.00120200; target 0.00125350
- **Fibonacci:** NON ATTIVO — 23.6% a 0.00128404
- **Fonte:** Yahoo Finance SOL-BTC (coppia diretta)
- **Motivi score:** prezzo sopra MA50 daily; prezzo sopra MA200 daily; MA50 daily in salita; prezzo sopra MA30 weekly; MA30 weekly in discesa; struttura con massimi/minimi crescenti; RSI relativo forte; MACD relativo negativo

![Grafico SOL/BTC](relative_strength_SOLBTC.png)

## DOGE/BTC

- **Verdetto relativo:** RELATIVA MISTA / NON CONFERMATA (-1)
- **Candidato futuro:** 0; **peso attuale Global: 0**
- **Lettura combinata USD/BTC:** QUADRO MISTO / NESSUNA CONFERMA RELATIVA
- **Struttura:** VOLATILITÀ IN ESPANSIONE
- **Rendimenti relativi:** 7g +8,25%; 30g +6,91%; 90g -15,42%; 180g -15,04%
- **Daily:** RSI 57.87; MA50 0.00000110; MA200 0.00000126
- **Weekly:** MA30 0.00000126; RSI 41.83
- **Livelli:** supporto 0.00000112; resistenza 0.00000115; breakout 60g 0.00000131; breakdown 60g 0.00000099
- **Pattern:** DOPPIO MINIMO / TARGET RAGGIUNTO; neckline 0.00000115; target 0.00000128
- **Fibonacci:** NON ATTIVO — 23.6% a 0.00000112
- **Fonte:** Rapporto sintetico DOGE-USD / BTC-USD (sintetica)
- **Motivi score:** prezzo sopra MA50 daily; prezzo sotto MA200 daily; MA50 daily in discesa; prezzo sotto MA30 weekly; MA30 weekly in discesa; RSI relativo forte; MACD relativo positivo

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
| SOL | 1g | 34 | 58,82% | +0,23% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 3g | 32 | 56,25% | +0,57% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 7g | 30 | 50,00% | +0,77% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 14g | 23 | 39,13% | +0,35% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 30g | 15 | 0,00% | -12,60% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 1g | 46 | 67,39% | -0,10% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 3g | 46 | 56,52% | -0,13% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 7g | 43 | 58,14% | -0,19% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 14g | 36 | 66,67% | +0,08% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 30g | 31 | 64,52% | +0,10% | LOCKED / RACCOLTA LIVE | 0 |

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

Ultima candela SOL usata: **9 settembre 2026**

## SOL PRICE CONTEXT

| Voce | Valore | Provenienza / significato |
| --- | --- | --- |
| Anchor computazionale | 104,43 $ | 2026-09-09T05:30:23Z \| Yahoo Finance daily shared snapshot \| Close 1d |
| Candela anchor completata | NO | Stato esplicito; il valore non viene sostituito dal prezzo pubblico. |
| Riferimento pubblico corrente | 104,23 $ | 2026-09-09T05:32:00Z \| Yahoo Finance \| solo display |
| Età anchor alla generazione | 0h 1m | WITHIN_DAILY_REPORT_CADENCE |
| Gap corrente vs anchor | -0,20000 $ | -0,19% |
| Validità input modello | REPRODUCIBLE_SHARED_SNAPSHOT | Non è una dichiarazione di validità del segnale/trading. |

```text
COMPUTATIONAL_ANCHOR_PRICE=104.43000030517578
COMPUTATIONAL_ANCHOR_FIELD=Close
COMPUTATIONAL_ANCHOR_TIMESTAMP=2026-09-09T05:30:23Z
COMPUTATIONAL_ANCHOR_SYMBOL=SOL-USD
COMPUTATIONAL_ANCHOR_PROVIDER=Yahoo Finance daily shared snapshot
COMPUTATIONAL_ANCHOR_TIMEFRAME=1d
COMPUTATIONAL_ANCHOR_COMPLETED=NO
CURRENT_PUBLIC_REFERENCE_PRICE=104.2300033569336
CURRENT_PUBLIC_REFERENCE_TIMESTAMP=2026-09-09T05:32:00Z
CURRENT_PUBLIC_REFERENCE_ACQUIRED_AT=2026-09-09T05:32:14Z
CURRENT_PUBLIC_REFERENCE_SYMBOL=SOL-USD
CURRENT_PUBLIC_REFERENCE_PROVIDER=Yahoo Finance
CURRENT_PUBLIC_REFERENCE_FIELD=Close
CURRENT_PUBLIC_REFERENCE_TIMEFRAME=1m
CURRENT_PUBLIC_REFERENCE_STATUS=AVAILABLE
ANCHOR_AGE_SECONDS=111.471256
ANCHOR_AGE_HOURS=0.03096423777777778
CURRENT_VS_ANCHOR_GAP_USD=-0.1999969482421875
CURRENT_VS_ANCHOR_GAP_PCT=-0.19151292507683104
```

## Verdetto: ANALOGIA DEBOLE / SCENARIO SECONDARIO

- **Fase attuale:** FRATTALE SOLO DI CONTESTO
- **Somiglianza totale:** +69,05%
- **Somiglianza strutturale:** +69,05%
- **Aderenza prezzo live:** +71,98%
- **Errore medio live:** +14,01%
- **Gap prezzo corrente:** +14,28%
- **Peso operativo suggerito:** 0
- **Affidabilita:** BASSA
- **Rischio fase:** ALTO
- **Trend tracking:** STRUTTURA STABILE
- **Sintesi:** Esistono alcuni elementi comuni, ma non abbastanza per una conferma.
- **SOL è al giorno:** 95 dal bottom usato.
- **Giorno BTC equivalente:** 2023-02-24
- **Prossimo step:** Proiezione condizionale, non conferma operativa: **Fase negativa / rischio discesa.** Zona bassa **90,88 $** intorno al **23 settembre 2026**; zona alta **106,45 $** intorno al **14 settembre 2026**; fine step circa **90,88 $** entro il **23 settembre 2026**.

### Metadata aderenza prezzo

```text
OPERATIONAL_VERDICT_REASON=ANALOGIA DEBOLE / SCENARIO SECONDARIO
PRICE_ADHERENCE_FAILED=NO
PRICE_ADHERENCE_LIVE_AVG_GAP_FAILED=NO
PRICE_ADHERENCE_LAST_GAP_FAILED=NO
PRICE_ADHERENCE_LIVE_AVG_GAP_THRESHOLD_PCT=15.0
PRICE_ADHERENCE_LAST_GAP_THRESHOLD_PCT=18.0
PRICE_ADHERENCE_OBSERVED_LIVE_AVG_GAP_PCT=14.010656962867284
PRICE_ADHERENCE_OBSERVED_LAST_GAP_PCT=14.277464605263157
```

## Somiglianza prima e dopo inizio programma

Questa sezione separa la somiglianza della forma dall'aderenza reale del prezzo.

- **Inizio programma/scanner:** 3 luglio 2026
- **Prima del programma** = backtest retroattivo.
- **Da inizio programma** = verifica live: è la parte più importante per l'uso operativo.

| Periodo | Date | Giorni | Aderenza prezzo | Errore medio | Gap ultimo | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| Prima del programma | 6 giugno 2026 -> 2 luglio 2026 | 27 | +87,95% | +6,02% | +21,89% | ABBASTANZA ALLINEATO |
| Da inizio programma | 3 luglio 2026 -> 9 settembre 2026 | 69 | +71,98% | +14,01% | +14,28% | DEVIAZIONE MODERATA |
| Totale dal bottom | 6 giugno 2026 -> 9 settembre 2026 | 96 | +76,47% | +11,76% | +14,28% | DEVIAZIONE MODERATA |

Nota: un frattale può avere una forma simile ma un prezzo distante. In quel caso non è operativo finché il gap non rientra.

## Lettura operativa veloce

Il frattale resta non operativo. Motivo effettivo: ANALOGIA DEBOLE / SCENARIO SECONDARIO.

| Voce | Risposta | Perché |
| --- | --- | --- |
| Uso operativo | NO | Peso 0 per il verdetto: ANALOGIA DEBOLE / SCENARIO SECONDARIO. |
| Aderenza live | +71,98% | Errore medio live +14,01%. |
| Gap corrente | +14,28% | Metrica separata dal motivo del verdetto. |
| Prima conferma prezzo | 109,65 $ | Serve anche miglioramento del gap, non solo una candela sopra il livello. |
| Seconda conferma | 137,24 $ | Rende più credibile il percorso, ma non sostituisce l'aderenza. |
| Invalidazione soft | 90,88 $ | Sotto questa zona il quadro peggiora. |
| Invalidazione forte | 62,19 $ | Sotto il bottom il paragone è quasi rotto. |

## Target ciclo fino al top BTC 2025

| Voce | Valore |
| --- | --- |
| Stato | CONTESTO / NON OPERATIVO |
| Top BTC 2025 | 6 ottobre 2025 - 124.753 $ |
| Data SOL equivalente | 21 aprile 2029 |
| Target ciclo base dall'anchor modello | 561,59 $ |
| Massimo percorso base | 561,59 $ (21 aprile 2029) |

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
| Prima conferma | 109,65 $ | Deve accompagnarsi al rientro del gap. |
| Seconda conferma | 137,24 $ | Scenario più credibile. |
| Invalidazione soft | 90,88 $ | Il frattale si indebolisce. |
| Invalidazione forte | 62,19 $ | Il paragone si rompe. |

## Proiezione veloce con date SOL

| Orizzonte | Data SOL | BTC fece | SOL base | Min percorso | Max percorso |
| --- | --- | --- | --- | --- | --- |
| 7 giorni | 16 settembre 2026 | -3,60% | 100,67 $ | 100,67 $ | 106,45 $ |
| 14 giorni | 23 settembre 2026 | -12,98% | 90,88 $ | 90,88 $ | 106,45 $ |
| 30 giorni | 9 ottobre 2026 | +20,67% | 126,02 $ | 90,88 $ | 127,55 $ |
| 60 giorni | 8 novembre 2026 | +22,03% | 127,43 $ | 90,88 $ | 137,24 $ |
| 90 giorni | 8 dicembre 2026 | +14,13% | 119,19 $ | 90,88 $ | 137,24 $ |
| 120 giorni | 7 gennaio 2027 | +31,69% | 137,52 $ | 90,88 $ | 138,18 $ |

## Prossimi step se SOL segue BTC 2022

| Step | Date SOL | BTC fine | SOL zona bassa | SOL zona alta | SOL fine base | Lettura |
| --- | --- | --- | --- | --- | --- | --- |
| Step 1 - prossime 2 settimane | 9 settembre 2026 -> 23 settembre 2026 | -12,98% | 90,88 $ (23 settembre 2026) | 106,45 $ (14 settembre 2026) | 90,88 $ | Fase negativa / rischio discesa. |
| Step 2 - primo mese | 24 settembre 2026 -> 9 ottobre 2026 | +20,67% | 92,88 $ (24 settembre 2026) | 127,55 $ (6 ottobre 2026) | 126,02 $ | Prima retest / debolezza, poi recupero. |
| Step 3 - secondo mese | 10 ottobre 2026 -> 8 novembre 2026 | +22,03% | 122,17 $ (10 ottobre 2026) | 137,24 $ (28 ottobre 2026) | 127,43 $ | Spinta rialzista abbastanza pulita. |
| Step 4 - terzo mese | 9 novembre 2026 -> 8 dicembre 2026 | +14,13% | 118,55 $ (7 dicembre 2026) | 132,95 $ (18 novembre 2026) | 119,19 $ | Spinta rialzista abbastanza pulita. |

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
| Prezzo SOL | 104,43 $ |  |
| Weekly RSI | 58,72 / linea grezza 52,24 | LINEA NON AFFIDABILE / RISCHIO NON ATTIVO — IRREALISTICA / NON OPERATIVA |
| Monthly RSI | 47,28 / linea grezza 55,48 | RSI TROPPO BASSO PER RISCHIO TOP — VALIDA / USO PRUDENTE |
| Target ciclo base | 561,59 $ | Avanzamento +18,60% |
| Rischio top-cycle RSI | BASSO | Nessun segnale top-cycle macro attivo. Prezzo ancora lontano dal target ciclo; il filtro RSI resta solo di monitoraggio. |

## Lettura semplice

- Weekly: La top-line weekly non supera i controlli di qualità. Non viene usata per generare rischio top-cycle.
- Monthly: RSI monthly è 47,3, sotto la soglia prudente 55. Anche se fosse vicino alla linea, non è una vera zona di esaurimento ciclo.
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
| Score on-chain | 5 |
| Bias | POSITIVA FORTE |
| Azione coerente | ON-CHAIN SANO / RAFFORZA IL FRATTALE |
| Prezzo SOL | 104,43 $ |
| TVL Solana | 5,94 mld $ |
| TVL 7g | +5,28% |
| DEX volume 24h | 2,58 mld $ |
| Fees 24h | 16,44 mln $ |
| Stablecoin su Solana | 16,56 mld $ |
| Stake ratio | 69,22% |
| Metriche mancanti | sol_realized_price_usd, sol_mvrv, sol_holder_profit_pct, sol_exchange_netflow_24h_usd |

Lettura semplice:

**ON-CHAIN SANO / RAFFORZA IL FRATTALE**

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
| Confronto precedente | 2026-09-07 |
| Fonte prezzi | Yahoo Finance SOL-USD weekly |
| Prezzo SOL | 104,43 $ |
| EMA200 weekly target | 111,27 $ |
| Upside verso EMA200 | +6,76% |
| Distanza prezzo da EMA200 | -6,33% |
| Gap EMA50/EMA200 | -5,68% |
| Stato cross | EMA50 SOTTO EMA200 |
| RSI weekly | 58,57 |
| Età SOL | 6,4 anni |
| Analoghi storici usati | 30 |
| Max analoghi per asset | 3 |
| Hit EMA200 12w analoghi | +83,33% |
| Max gain mediano 12w | +20,65% |
| Drawdown mediano 12w | -37,49% |

Lettura semplice:

**SOLO OSSERVAZIONE**

Autocontrollo: **STABILE / DA CONFERMARE**.

Questo modulo confronta SOL con altre crypto in fasi simili di età, distanza da EMA200, EMA50/EMA200 e RSI. Non usa stock market.

Nota importante: **questo modulo ora NON pesa più nel Global Confluence**. Resta solo come contesto di ciclo e come mappa verso EMA200 weekly. Il punteggio Global resta guidato da prezzo, scanner, regime, struttura tecnica, frattale, RSI e conferme reali.

Nota: se EMA50/EMA200 sono dentro ±2%, il modulo parla di medie sovrapposte / incrocio in corso, perché exchange diversi possono mostrare il cross leggermente prima o dopo.

<!-- Generato: 2026-09-09 05:32 UTC -->
<!-- MAJOR_ALT_LIFECYCLE_SQUEEZE_END -->

</details>
<!-- COMPACT_SECTION_END:major_alt_lifecycle -->

# Report giornaliero BTC / SOL / DOGE

Aggiornato il: **2026-09-09 05:30:23 UTC**

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
- DOGE: cambiamento importante in miglioramento rispetto a ieri.

| Asset | Cambio | Tono | Verdetto oggi | Casi positivi oggi | Δ casi positivi |
| --- | --- | --- | --- | --- | --- |
| BTC | NESSUN CAMBIAMENTO FORTE | peggioramento | RIALZISTA | +80.00% | -2.50 punti |
| SOL | CAMBIAMENTO MEDIO | peggioramento | RIALZISTA | +62.50% | -2.50 punti |
| DOGE | CAMBIAMENTO MEDIO | miglioramento | RIBASSISTA | +37.50% | +5.00 punti |

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
| BTC | 75.167 $ | 87.035 $ | +68,18% | +15,79% | buona zona storica di rimbalzo | 87.035 $ | 75.167 $ | +8,82% | -13,64% | spike storicamente più resistente |
| SOL | 99,21 $ | 114,87 $ | +56,00% | +15,79% | rimbalzo possibile | 114,87 $ | 99,21 $ | +24,14% | -13,64% | spike storicamente più resistente |
| DOGE | 0,08591 $ | 0,09947 $ | +37,50% | +15,79% | rimbalzo debole | 0,09947 $ | 0,08591 $ | +54,55% | -13,64% | attenzione a prendere profitto |

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

- **BTC: su 40 casi simili, 22 prima sono scesi a -5,00%. Tra quei 22, 15 poi sono rimbalzati fino a +10,00%. Percentuale: +68,18% (15/22). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: buona zona storica di rimbalzo.**
- **BTC: su 40 casi simili, 34 prima sono saliti a +10,00%. Tra quei 34, 3 poi sono scaricati a -5,00%. Percentuale: +8,82% (3/34). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.**
- **SOL: su 40 casi simili, 25 prima sono scesi a -5,00%. Tra quei 25, 14 poi sono rimbalzati fino a +10,00%. Percentuale: +56,00% (14/25). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo possibile.**
- **SOL: su 40 casi simili, 29 prima sono saliti a +10,00%. Tra quei 29, 7 poi sono scaricati a -5,00%. Percentuale: +24,14% (7/29). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.**
- **DOGE: su 40 casi simili, 32 prima sono scesi a -5,00%. Tra quei 32, 12 poi sono rimbalzati fino a +10,00%. Percentuale: +37,50% (12/32). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.**
- **DOGE: su 40 casi simili, 22 prima sono saliti a +10,00%. Tra quei 22, 12 poi sono scaricati a -5,00%. Percentuale: +54,55% (12/22). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: attenzione a prendere profitto.**

<!-- BOUNCE_AFTER_DRAWDOWN_END -->

</details>
<!-- COMPACT_SECTION_END:bounce_after_drawdown -->

<!-- COMPACT_SECTION_START:scanner_forecast -->
<details>
<summary><strong>🔭 Cono probabilistico dello scanner</strong></summary>

<!-- SCANNER_FORECAST_TRACKER_START -->
# Scanner forecast path / cono probabilistico

Generato: 2026-09-09 05:31:55 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [scanner_forecast_tracker_report.md](scanner_forecast_tracker_report.md)

## Snapshot effettivamente usato

| Asset   | Snapshot prezzo   | Generazione snapshot prezzo   | Snapshot match scanner   |
|:--------|:------------------|:------------------------------|:-------------------------|
| BTC | 2026-09-09 | 2026-09-09T05:30:23Z | 2026-09-09 05:30:23 |
| SOL | 2026-09-09 | 2026-09-09T05:30:23Z | 2026-09-09 05:30:23 |
| DOGE | 2026-09-09 | 2026-09-09T05:30:23Z | 2026-09-09 05:30:23 |

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
| BTC | 2026-09-09 | 79.123 $ | SALITA | 80,00% | 52.020,74 $ | 86.202,26 $ | 95.158,40 $ | 113.067,81 $ | 141.373,53 $ |
| SOL | 2026-09-09 | 104,43 $ | SALITA | 62,50% | 70,96 $ | 89,26 $ | 122,60 $ | 165,33 $ | 222,92 $ |
| DOGE | 2026-09-09 | 0.09043 $ | DISCESA | 37,50% | 0.06706 $ | 0.07016 $ | 0.08277 $ | 0.09937 $ | 0.12020 $ |

## Confronto raw / regime-adjusted

Il cono raw continua a usare i 40 casi dello scanner. Il cono regime-adjusted sceglie una sola coorte nella gerarchia SAME_BTC_AND_ASSET_REGIME → SAME_ASSET_REGIME → SAME_BTC_REGIME. Ogni livello richiede almeno 5 match; le coorti non vengono mai combinate e ogni fallback è dichiarato.

| Asset   | Stato adjusted              | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level        | selection_reason              | Raw p50 30g   | Adjusted p50 30g   | Raw p90 30g   | Adjusted p90 30g   |
|:--------|:----------------------------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:----------------------|:------------------------------|:--------------|:-------------------|:--------------|:-------------------|
| BTC | AVAILABLE | SAME_ASSET_REGIME | 0 | 5 | 0 | 5 | 5 | 1_SAME_ASSET_FALLBACK | FALLBACK_TO_SAME_ASSET_REGIME | 95.158,40 $ | 81.563,96 $ | 141.373,53 $ | 110.970,49 $ |
| SOL | INSUFFICIENT_REGIME_MATCHES | NONE | 0 | 4 | 1 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES | 122,60 $ | n/a | 222,92 $ | n/a |
| DOGE | INSUFFICIENT_REGIME_MATCHES | NONE | 0 | 0 | 1 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES | 0.08277 $ | n/a | 0.12020 $ | n/a |

## Grafici

### BTC

![Scanner forecast BTC](scanner_forecast_BTC.png)

#### Verifica storica e discrepanza

![Verifica storica cono BTC](scanner_forecast_history_BTC.png)

- Cono congelato il **2026-08-10**; verificato fino al **2026-09-09**; stato **COMPLETO 30/30g**.
- Reale **78.975,22 $**; p50 previsto **71.929,11 $**; scarto **9,80%**.
- Errore medio assoluto **9,75%**; massimo **16,42%**; DENTRO p10-p90; FUORI p25-p75.

#### Cono regime-adjusted

Gruppo selezionato: **SAME_ASSET_REGIME**; fallback: **1_SAME_ASSET_FALLBACK**; motivo: **FALLBACK_TO_SAME_ASSET_REGIME**.

**WARNING:** coorte fallback meno stringente rispetto a SAME_BTC_AND_ASSET_REGIME.

![Scanner forecast regime-adjusted BTC](scanner_forecast_BTC_regime_adjusted.png)

### SOL

![Scanner forecast SOL](scanner_forecast_SOL.png)

#### Verifica storica e discrepanza

![Verifica storica cono SOL](scanner_forecast_history_SOL.png)

- Cono congelato il **2026-08-10**; verificato fino al **2026-09-09**; stato **COMPLETO 30/30g**.
- Reale **104,23 $**; p50 previsto **85,81 $**; scarto **21,46%**.
- Errore medio assoluto **16,91%**; massimo **32,96%**; DENTRO p10-p90; FUORI p25-p75.

#### Cono regime-adjusted

Gruppo selezionato: **NONE**; fallback: **NONE**; motivo: **INSUFFICIENT_REGIME_MATCHES**.

Non disponibile: INSUFFICIENT_REGIME_MATCHES (campione selezionato 0/5 match).

### DOGE

![Scanner forecast DOGE](scanner_forecast_DOGE.png)

#### Verifica storica e discrepanza

![Verifica storica cono DOGE](scanner_forecast_history_DOGE.png)

- Cono congelato il **2026-08-10**; verificato fino al **2026-09-09**; stato **COMPLETO 30/30g**.
- Reale **0.09015 $**; p50 previsto **0.08290 $**; scarto **8,74%**.
- Errore medio assoluto **12,83%**; massimo **39,44%**; DENTRO p10-p90; DENTRO p25-p75.

#### Cono regime-adjusted

Gruppo selezionato: **NONE**; fallback: **NONE**; motivo: **INSUFFICIENT_REGIME_MATCHES**.

Non disponibile: INSUFFICIENT_REGIME_MATCHES (campione selezionato 0/5 match).

## Accuratezza percorso scanner

| Asset   | Giorno   |   Controlli | Dentro p10-p90   | Dentro p25-p75   | Errore medio abs vs p50   | Errore medio vs p50   |
|:--------|:---------|------------:|:-----------------|:-----------------|:--------------------------|:----------------------|
| BTC | 1g | 58 | 93,10% | 65,52% | 2,10% | 0,60% |
| BTC | 3g | 54 | 90,74% | 70,37% | 3,25% | 1,11% |
| BTC | 7g | 46 | 91,30% | 71,74% | 5,42% | 2,62% |
| BTC | 14g | 37 | 97,30% | 64,86% | 6,56% | 3,96% |
| BTC | 30g | 23 | 100,00% | 91,30% | 8,90% | 3,16% |
| SOL | 1g | 58 | 79,31% | 58,62% | 2,86% | 1,14% |
| SOL | 3g | 54 | 88,89% | 72,22% | 4,13% | 2,08% |
| SOL | 7g | 46 | 86,96% | 69,57% | 5,84% | 4,21% |
| SOL | 14g | 37 | 81,08% | 64,86% | 8,61% | 7,61% |
| SOL | 30g | 23 | 91,30% | 47,83% | 15,48% | 14,92% |
| DOGE | 1g | 58 | 86,21% | 58,62% | 3,32% | 0,92% |
| DOGE | 3g | 54 | 88,89% | 66,67% | 4,79% | 2,34% |
| DOGE | 7g | 46 | 73,91% | 71,74% | 9,20% | 6,67% |
| DOGE | 14g | 37 | 81,08% | 51,35% | 11,12% | 10,02% |
| DOGE | 30g | 23 | 91,30% | 34,78% | 17,34% | 17,34% |

## Tail / outlier audit

I casi di coda restano nel calcolo. L'audit leave-one-out quantifica la sensibilità dei percentili senza trasformare l'analisi in un filtro discrezionale.

Dettaglio completo: [scanner_forecast_tail_outlier_audit.md](scanner_forecast_tail_outlier_audit.md).

## Calibratore shadow

Il cono ufficiale resta grezzo e invariato. Il calibratore usa soltanto previsioni passate già mature, campionate una volta a settimana per ridurre la falsa indipendenza. Ogni orizzonte si attiva a 30 controlli indipendenti: parte al 25% della correzione stimata e cresce gradualmente fino al 100% a 100 controlli.

| Asset   | Orizzonte   |   Controlli indipendenti |   Soglia | Stato                  | Forza correzione   | Shift p50   |   Scala p10-p90 |
|:--------|:------------|-------------------------:|---------:|:-----------------------|:-------------------|:------------|----------------:|
| BTC | 1g | 10 | 30 | RACCOLTA (20 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 3g | 9 | 30 | RACCOLTA (21 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 7g | 9 | 30 | RACCOLTA (21 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 14g | 8 | 30 | RACCOLTA (22 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 30g | 6 | 30 | RACCOLTA (24 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 1g | 10 | 30 | RACCOLTA (20 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 3g | 9 | 30 | RACCOLTA (21 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 7g | 9 | 30 | RACCOLTA (21 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 14g | 8 | 30 | RACCOLTA (22 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 30g | 6 | 30 | RACCOLTA (24 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 1g | 10 | 30 | RACCOLTA (20 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 3g | 9 | 30 | RACCOLTA (21 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 7g | 9 | 30 | RACCOLTA (21 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 14g | 8 | 30 | RACCOLTA (22 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 30g | 6 | 30 | RACCOLTA (24 mancanti) | 0,0% | 0,00% | 1,000 |

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

Righe salvate nello storico: **171**.

Questa sezione tiene un diario delle previsioni giornaliere a 30 giorni, senza appesantire il report principale.

| Data | Asset | Prezzo | Direzione | Casi positivi | Return p50 | Drawdown p50 | Max gain p50 | Controllo 30g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-09-09 | BTC | 79.123 $ | SALITA | 80,00% | 95.158 $ | 72.636 $ | 102.292 $ | 2026-10-09 |
| 2026-09-09 | DOGE | 0,09000 $ | DISCESA | 37,50% | 0,08000 $ | 0,07000 $ | 0,10000 $ | 2026-10-09 |
| 2026-09-09 | SOL | 104,43 $ | SALITA | 62,50% | 122,60 $ | 94,78 $ | 143,04 $ | 2026-10-09 |

<!-- FORECAST_30D_HISTORY_END -->

</details>
<!-- COMPACT_SECTION_END:scanner_forecast -->

<!-- COMPACT_SECTION_START:extreme_cases -->
<details>
<summary><strong>⚠️ Percorso dei casi estremi</strong></summary>

<!-- EXTREME_CASES_PATH_START -->
# Extreme cases path report

Generato: 2026-09-09 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [extreme_cases_path_report.md](extreme_cases_path_report.md)

Questo report si attiva quando i casi positivi o negativi sono almeno **80%**.

Ora misura anche il **rialzo massimo prima della discesa principale**, quindi distingue uno spike iniziale da una discesa quasi immediata.

## Trigger estremi

| Asset   | Direzione            | Trigger   | Percentuale   | Motivo                           |   Match disponibili |
|:--------|:---------------------|:----------|:--------------|:---------------------------------|--------------------:|
| BTC     | POSITIVO / RIALZISTA | SI        | +80,00%       | Casi positivi 80.00% >= 80%      |                  40 |
| SOL     | NESSUNO              | NO        | +62,50%       | Nessun lato sopra soglia estrema |                  40 |
| DOGE    | NESSUNO              | NO        | +62,50%       | Nessun lato sopra soglia estrema |                  40 |

## BTC — casi rialzisti

- Trigger: **Casi positivi 80.00% >= 80%**
- Casi usati nei grafici: **32**
- Return mediano 7g: **+3,17%**
- Return mediano 14g: **+10,14%**
- Return mediano 30g: **+31,31%**
- Drawdown mediano: **-2,82%**
- Max gain mediano: **+37,56%**

### Quanto salivano prima di scendere

- Spike massimo mediano prima del minimo: **+0,00%**
- Spike massimo medio prima del minimo: **+2,37%**
- Spike p75 prima del minimo: **+1,16%**
- Giorno mediano dello spike: **giorno 0**
- Giorno mediano del minimo: **giorno 1**
- Scarico mediano dal picco al minimo: **-7,27%**
- Casi con almeno +5% prima del minimo: **+9,38%**
- Casi con almeno +10% prima del minimo: **+6,25%**
- Casi con almeno +15% prima del minimo: **+6,25%**
- Discesa quasi immediata: **+65,62%**

Un segnale ribassista a 30 giorni non significa necessariamente discesa immediata: alcuni casi fanno prima uno spike e poi scaricano.

### Distribuzione 30 giorni

| P10    | P25     | P50     | P75     | P90     |
|:-------|:--------|:--------|:--------|:--------|
| +9,83% | +13,71% | +31,31% | +49,52% | +88,02% |

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
| XLM-USD         | 2020-12-11 | +90,70%      | +26,60%                  |              5 | -16,34%      |              12 | -33,92%          | +91,00%      | SPIKE PRIMA DEL DUMP          |
| ADA-USD         | 2020-12-11 | +84,64%      | +20,18%                  |              5 | -2,19%       |              12 | -18,61%          | +118,64%     | ECCEZIONE POSITIVA            |
| INJ-USD         | 2023-11-13 | +88,46%      | +9,93%                   |              2 | -7,66%       |               8 | -16,00%          | +89,19%      | ECCEZIONE POSITIVA            |
| AVAX-USD        | 2021-09-03 | +83,83%      | +4,94%                   |              2 | -19,30%      |               5 | -23,10%          | +49,67%      | RIALZO MODESTO PRIMA DEL DUMP |
| BTC-USD         | 2019-04-20 | +85,70%      | +4,39%                   |              3 | -2,39%       |               5 | -6,49%           | +49,47%      | ECCEZIONE POSITIVA            |
| QTUM-USD        | 2023-11-16 | +84,64%      | +3,34%                   |              4 | -5,87%       |               5 | -8,91%           | +3,09%       | ECCEZIONE POSITIVA            |
| 1INCH-USD       | 2023-11-23 | +85,90%      | +3,34%                   |              2 | -4,97%       |               7 | -8,04%           | +17,36%      | ECCEZIONE POSITIVA            |
| DOGE-USD        | 2019-04-21 | +83,62%      | +1,38%                   |              1 | -10,65%      |               8 | -11,87%          | +11,81%      | ECCEZIONE POSITIVA            |
| ZEC-USD         | 2019-04-21 | +83,49%      | +1,09%                   |              1 | -17,25%      |              18 | -18,15%          | +9,64%       | ECCEZIONE POSITIVA            |
| BCH-USD         | 2019-04-21 | +85,88%      | +0,80%                   |              1 | -18,54%      |               8 | -19,19%          | +43,74%      | ECCEZIONE POSITIVA            |
| BNB-USD         | 2019-02-25 | +89,55%      | +0,00%                   |              0 | -3,26%       |               1 | -3,26%           | +70,51%      | DISCESA QUASI IMMEDIATA       |
| THETA-USD       | 2023-11-20 | +88,07%      | +0,00%                   |              0 | -10,09%      |               1 | -10,09%          | +12,61%      | DISCESA QUASI IMMEDIATA       |
| ADA-USD         | 2023-11-21 | +87,40%      | +0,00%                   |              0 | +0,00%       |               0 | +0,00%           | +77,51%      | DISCESA QUASI IMMEDIATA       |
| ETC-USD         | 2023-11-21 | +86,97%      | +0,00%                   |              0 | +0,00%       |               0 | +0,00%           | +13,76%      | DISCESA QUASI IMMEDIATA       |
| EGLD-USD        | 2023-11-21 | +86,89%      | +0,00%                   |              0 | +0,00%       |               0 | +0,00%           | +55,32%      | DISCESA QUASI IMMEDIATA       |
| THETA-USD       | 2019-02-24 | +86,85%      | +0,00%                   |              0 | +0,00%       |               0 | +0,00%           | +25,99%      | DISCESA QUASI IMMEDIATA       |
| XRP-USD         | 2023-11-21 | +86,35%      | +0,00%                   |              0 | +0,00%       |               0 | +0,00%           | +7,49%       | DISCESA QUASI IMMEDIATA       |
| ALGO-USD        | 2023-11-20 | +86,15%      | +0,00%                   |              0 | -12,15%      |               1 | -12,15%          | +39,80%      | DISCESA QUASI IMMEDIATA       |
| XTZ-USD         | 2023-11-21 | +86,05%      | +0,00%                   |              0 | +0,00%       |               0 | +0,00%           | +20,77%      | DISCESA QUASI IMMEDIATA       |
| EOS-USD         | 2023-11-21 | +85,62%      | +0,00%                   |              0 | +0,00%       |               0 | +0,00%           | +29,79%      | DISCESA QUASI IMMEDIATA       |

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
- Casi positivi / salita storica: **80,00%**
- Casi negativi / discesa storica: **20,00%**
- Quanto è netto il segnale: **forte**
- Prezzo attuale: **79.122,84 $**
- Return normale fra 30 giorni: **95.158,40 $** (20,27%)
- Drawdown normale durante il mese: **72.636,27 $** (-8,20%)
- Drawdown brutto da rispettare: **65.215,46 $** (-17,58%)
- Max gain normale durante il mese: **102.292,09 $** (29,28%)
- Max gain buono / take profit ottimistico: **123.183,32 $** (55,69%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Solana
- Direzione più probabile a 30 giorni: **SALITA**
- Casi positivi / salita storica: **62,50%**
- Casi negativi / discesa storica: **37,50%**
- Quanto è netto il segnale: **medio**
- Prezzo attuale: **104,43 $**
- Return normale fra 30 giorni: **122,60 $** (17,40%)
- Drawdown normale durante il mese: **94,78 $** (-9,25%)
- Drawdown brutto da rispettare: **73,91 $** (-29,22%)
- Max gain normale durante il mese: **143,04 $** (36,97%)
- Max gain buono / take profit ottimistico: **179,39 $** (71,78%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Dogecoin
- Direzione più probabile a 30 giorni: **DISCESA**
- Casi positivi / salita storica: **37,50%**
- Casi negativi / discesa storica: **62,50%**
- Quanto è netto il segnale: **medio**
- Prezzo attuale: **0,09 $**
- Return normale fra 30 giorni: **0,08 $** (-8,47%)
- Drawdown normale durante il mese: **0,07 $** (-17,22%)
- Drawdown brutto da rispettare: **0,06 $** (-30,59%)
- Max gain normale durante il mese: **0,10 $** (14,67%)
- Max gain buono / take profit ottimistico: **0,11 $** (25,06%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Messaggio del giorno

Il quadro generale oggi è più favorevole. Lo scanner vede più possibilità di salita su più asset.

---

# Mappa semplice asset per asset

# Bitcoin — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟢 VERDE / Favorevole
**Prezzo attuale:** 79.122,84 $

**Direzione più probabile a 30 giorni:** **SALITA**
- Probabilità storica di salita: **80,00%**
- Probabilità storica di discesa: **20,00%**
- Quanto è netto il segnale: **forte**

## Come leggere questa parte

- **Probabilità storica di salita** = su 40 casi simili, quanti hanno chiuso sopra dopo 30 giorni.
- **Probabilità storica di discesa** = su 40 casi simili, quanti hanno chiuso sotto dopo 30 giorni.
- **Quanto è netto il segnale** = quanto è grande la differenza tra salita e discesa. Non vuol dire certezza, vuol dire solo che il risultato storico non è vicino al 50/50.

La lettura principale è rialzista, con segnale forte. Nei casi storici simili, il prezzo ha chiuso sopra dopo 30 giorni più spesso di quanto abbia chiuso sotto.

## 1. Return 30d — prezzo fra 30 giorni

**Return** significa rendimento finale. Qui guardiamo dove potrebbe stare il prezzo **alla fine dei 30 giorni**, non durante il percorso.

- Se va molto male: **52.020,74 $** (-34,25%)
- Se va male: **86.202,26 $** (8,95%)
- Scenario normale: **95.158,40 $** (20,27%)
- Se va bene: **113.067,81 $** (42,90%)
- Se va molto bene: **141.373,53 $** (78,68%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **72.636,27 $** (-8,20%)
- Discesa brutta: **65.215,46 $** (-17,58%)
- Discesa molto brutta: **48.232,63 $** (-39,04%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **102.292,09 $** (29,28%)
- Rialzo buono: **123.183,32 $** (55,69%)
- Rialzo molto forte: **167.264,43 $** (111,40%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Bitcoin tendeva a muoversi tra una zona bassa intorno a **72.636,27 $** e uno spike normale intorno a **102.292,09 $**.

La chiusura a 30 giorni era più spesso positiva: salita 80,00%, discesa 20,00%. Quindi la lettura principale è favorevole.

Nota leva BTC: se la liquidazione è vicina a 51.000 $, guarda soprattutto la discesa brutta e molto brutta. Il prezzo può recuperare dopo, ma la leva può saltare prima.

---

# Solana — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟢 VERDE / Favorevole
**Prezzo attuale:** 104,43 $

**Direzione più probabile a 30 giorni:** **SALITA**
- Probabilità storica di salita: **62,50%**
- Probabilità storica di discesa: **37,50%**
- Quanto è netto il segnale: **medio**

## Come leggere questa parte

- **Probabilità storica di salita** = su 40 casi simili, quanti hanno chiuso sopra dopo 30 giorni.
- **Probabilità storica di discesa** = su 40 casi simili, quanti hanno chiuso sotto dopo 30 giorni.
- **Quanto è netto il segnale** = quanto è grande la differenza tra salita e discesa. Non vuol dire certezza, vuol dire solo che il risultato storico non è vicino al 50/50.

La lettura principale è rialzista, con segnale medio. Nei casi storici simili, il prezzo ha chiuso sopra dopo 30 giorni più spesso di quanto abbia chiuso sotto.

## 1. Return 30d — prezzo fra 30 giorni

**Return** significa rendimento finale. Qui guardiamo dove potrebbe stare il prezzo **alla fine dei 30 giorni**, non durante il percorso.

- Se va molto male: **70,96 $** (-32,05%)
- Se va male: **89,26 $** (-14,52%)
- Scenario normale: **122,60 $** (17,40%)
- Se va bene: **165,33 $** (58,32%)
- Se va molto bene: **222,92 $** (113,47%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **94,78 $** (-9,25%)
- Discesa brutta: **73,91 $** (-29,22%)
- Discesa molto brutta: **60,28 $** (-42,28%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **143,04 $** (36,97%)
- Rialzo buono: **179,39 $** (71,78%)
- Rialzo molto forte: **260,44 $** (149,39%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Solana tendeva a muoversi tra una zona bassa intorno a **94,78 $** e uno spike normale intorno a **143,04 $**.

La chiusura a 30 giorni era più spesso positiva: salita 62,50%, discesa 37,50%. Quindi la lettura principale è favorevole.

---

# Dogecoin — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🔴 ROSSO / Prudenza
**Prezzo attuale:** 0,09 $

**Direzione più probabile a 30 giorni:** **DISCESA**
- Probabilità storica di salita: **37,50%**
- Probabilità storica di discesa: **62,50%**
- Quanto è netto il segnale: **medio**

## Come leggere questa parte

- **Probabilità storica di salita** = su 40 casi simili, quanti hanno chiuso sopra dopo 30 giorni.
- **Probabilità storica di discesa** = su 40 casi simili, quanti hanno chiuso sotto dopo 30 giorni.
- **Quanto è netto il segnale** = quanto è grande la differenza tra salita e discesa. Non vuol dire certezza, vuol dire solo che il risultato storico non è vicino al 50/50.

La lettura principale è ribassista, con segnale medio. Nei casi storici simili, il prezzo ha chiuso sotto dopo 30 giorni più spesso di quanto abbia chiuso sopra.

## 1. Return 30d — prezzo fra 30 giorni

**Return** significa rendimento finale. Qui guardiamo dove potrebbe stare il prezzo **alla fine dei 30 giorni**, non durante il percorso.

- Se va molto male: **0,07 $** (-25,84%)
- Se va male: **0,07 $** (-22,41%)
- Scenario normale: **0,08 $** (-8,47%)
- Se va bene: **0,10 $** (9,89%)
- Se va molto bene: **0,12 $** (32,92%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **0,07 $** (-17,22%)
- Discesa brutta: **0,06 $** (-30,59%)
- Discesa molto brutta: **0,06 $** (-33,55%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **0,10 $** (14,67%)
- Rialzo buono: **0,11 $** (25,06%)
- Rialzo molto forte: **0,13 $** (41,67%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Dogecoin tendeva a muoversi tra una zona bassa intorno a **0,07 $** e uno spike normale intorno a **0,10 $**.

La chiusura a 30 giorni era più spesso negativa: salita 37,50%, discesa 62,50%. Quindi la lettura principale è prudente/debole.

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

- Grezzo: **20,27%** → **95.158,40 $**
- Correzione imparata dagli errori: **2,01%**
- Calibrato: **22,27%** → **96.747,12 $**
- Lettura: Lo scanner è stato troppo pessimista sul prezzo finale.

### Drawdown 30d — rischio di discesa durante il mese

- Grezzo: **-8,20%** → **72.636,27 $**
- Correzione imparata dagli errori: **4,72%**
- Calibrato: **-3,47%** → **76.373,49 $**
- Lettura: Lo scanner è stato troppo prudente: nella realtà il prezzo è sceso meno del previsto.

### Max gain 30d — rialzo/spike durante il mese

- Grezzo: **29,28%** → **102.292,09 $**
- Correzione imparata dagli errori: **-2,82%**
- Calibrato: **26,46%** → **100.056,93 $**
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

- Grezzo: **17,40%** → **122,60 $**
- Correzione imparata dagli errori: **8,80%**
- Calibrato: **26,20%** → **131,79 $**
- Lettura: Lo scanner è stato troppo pessimista sul prezzo finale.

### Drawdown 30d — rischio di discesa durante il mese

- Grezzo: **-9,25%** → **94,78 $**
- Correzione imparata dagli errori: **2,99%**
- Calibrato: **-6,25%** → **97,90 $**
- Lettura: Lo scanner è stato troppo prudente: nella realtà il prezzo è sceso meno del previsto.

### Max gain 30d — rialzo/spike durante il mese

- Grezzo: **36,97%** → **143,04 $**
- Correzione imparata dagli errori: **4,02%**
- Calibrato: **40,99%** → **147,24 $**
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

- Grezzo: **-8,47%** → **0,08 $**
- Correzione imparata dagli errori: **15,19%**
- Calibrato: **6,71%** → **0,10 $**
- Lettura: Lo scanner è stato troppo pessimista sul prezzo finale.

### Drawdown 30d — rischio di discesa durante il mese

- Grezzo: **-17,22%** → **0,07 $**
- Correzione imparata dagli errori: **15,34%**
- Calibrato: **-1,88%** → **0,09 $**
- Lettura: Lo scanner è stato troppo prudente: nella realtà il prezzo è sceso meno del previsto.

### Max gain 30d — rialzo/spike durante il mese

- Grezzo: **14,67%** → **0,10 $**
- Correzione imparata dagli errori: **2,52%**
- Calibrato: **17,20%** → **0,11 $**
- Lettura: Lo scanner ha sottostimato gli spike: nella realtà il prezzo è salito più del previsto.

### Come leggerlo

La parte grezza ti dice cosa mostrano i vecchi pattern storici. La parte calibrata ti dice come cambia quella lettura dopo aver visto se lo scanner, nel mercato reale, è stato troppo ottimista o troppo pessimista.

---

# Approfondimento tecnico — Bitcoin (BTC-USD)

## Semaforo: 🟢 VERDE / Favorevole

**Prezzo attuale:** 79.122,84 $

Bitcoin ha un segnale favorevole. La statistica dei casi simili indica più possibilità di salita che di discesa, ma resta comunque una probabilità, non una certezza.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **80,00%**
- Casi negativi dopo 30 giorni: **20,00%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **85,66%**
- Rendimento medio dopo 30 giorni: **23,89%**
- Rendimento centrale dopo 30 giorni: **20,27%**
- Discesa media durante i 30 giorni: **-12,70%**
- Massimo rialzo medio durante i 30 giorni: **48,16%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **98.027,25 $**
- Scenario centrale a 30 giorni: **95.158,40 $**
- Zona di rischio media: **69.073,85 $**
- Zona di rialzo media: **117.224,82 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -34,25% → **52.020,74 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: 8,95% → **86.202,26 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: 20,27% → **95.158,40 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 42,90% → **113.067,81 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 78,68% → **141.373,53 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -39,04% → **48.232,63 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -17,58% → **65.215,46 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -8,20% → **72.636,27 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: 0,00% → **79.122,84 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: 0,00% → **79.122,84 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 6,88% → **84.562,76 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 17,01% → **92.584,31 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 29,28% → **102.292,09 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 55,69% → **123.183,32 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 111,40% → **167.264,43 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| XLM-USD         | 2020-09-03   | 2020-12-11 |        90.7  |        91    |         -16.34 |         125.42 |
| BNB-USD         | 2018-11-18   | 2019-02-25 |        89.55 |        70.51 |          -3.26 |          75.63 |
| INJ-USD         | 2023-08-06   | 2023-11-13 |        88.46 |        89.19 |          -7.66 |          89.19 |
| THETA-USD       | 2023-08-13   | 2023-11-20 |        88.07 |        12.61 |         -10.09 |          20.8  |
| UNI-USD         | 2023-04-07   | 2023-07-15 |        88    |       -47.87 |         -48.23 |         315.96 |
| LRC-USD         | 2019-11-18   | 2020-02-25 |        87.58 |       -31.73 |         -38.57 |          19.06 |
| ADA-USD         | 2023-08-14   | 2023-11-21 |        87.4  |        77.51 |           0    |          85.5  |
| ETC-USD         | 2023-08-14   | 2023-11-21 |        86.97 |        13.76 |           0    |          22.61 |
| EGLD-USD        | 2023-08-14   | 2023-11-21 |        86.89 |        55.32 |           0    |          61.6  |
| THETA-USD       | 2018-11-17   | 2019-02-24 |        86.85 |        25.99 |           0    |         109.84 |

---

# Approfondimento tecnico — Solana (SOL-USD)

## Semaforo: 🟢 VERDE / Favorevole

**Prezzo attuale:** 104,43 $

Solana ha un segnale favorevole. La statistica dei casi simili indica più possibilità di salita che di discesa, ma resta comunque una probabilità, non una certezza.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **62,50%**
- Casi negativi dopo 30 giorni: **37,50%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **84,27%**
- Rendimento medio dopo 30 giorni: **32,94%**
- Rendimento centrale dopo 30 giorni: **17,40%**
- Discesa media durante i 30 giorni: **-16,47%**
- Massimo rialzo medio durante i 30 giorni: **63,51%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **138,83 $**
- Scenario centrale a 30 giorni: **122,60 $**
- Zona di rischio media: **87,23 $**
- Zona di rialzo media: **170,75 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -32,05% → **70,96 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -14,52% → **89,26 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: 17,40% → **122,60 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 58,32% → **165,33 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 113,47% → **222,92 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -42,28% → **60,28 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -29,22% → **73,91 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -9,25% → **94,78 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -2,34% → **101,99 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: 0,00% → **104,43 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 3,59% → **108,18 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 7,67% → **112,44 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 36,97% → **143,04 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 71,78% → **179,39 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 149,39% → **260,44 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| RUNE-USD        | 2020-03-18   | 2020-06-25 |        87.37 |        36.51 |         -13.77 |          57.1  |
| ZIL-USD         | 2020-08-31   | 2020-12-08 |        87.04 |       143.04 |          -5.35 |         185.86 |
| VET-USD         | 2020-03-09   | 2020-06-16 |        86.83 |        99.18 |          -8.4  |         121.32 |
| HBAR-USD        | 2020-10-25   | 2021-02-01 |        86.63 |        46.2  |           0    |          73.81 |
| BNB-USD         | 2023-10-03   | 2024-01-10 |        86.42 |         6.14 |          -4.32 |           6.14 |
| ENJ-USD         | 2020-10-28   | 2021-02-04 |        86.18 |       221.5  |           0    |         261.65 |
| BNB-USD         | 2018-11-18   | 2019-02-25 |        85.73 |        70.51 |          -3.26 |          75.63 |
| RUNE-USD        | 2026-02-05   | 2026-05-15 |        85.52 |       -20.87 |         -35.52 |           0    |
| WAVES-USD       | 2023-08-14   | 2023-11-21 |        85.09 |        36.7  |           0    |          36.7  |
| 1INCH-USD       | 2023-08-16   | 2023-11-23 |        85.05 |        17.36 |          -4.97 |          17.36 |

---

# Approfondimento tecnico — Dogecoin (DOGE-USD)

## Semaforo: 🔴 ROSSO / Prudenza

**Prezzo attuale:** 0,09 $

Dogecoin richiede prudenza. La statistica dei casi simili indica più possibilità di discesa che di salita. Con leva, il rischio principale è il drawdown durante il percorso.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **37,50%**
- Casi negativi dopo 30 giorni: **62,50%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **79,70%**
- Rendimento medio dopo 30 giorni: **-2,28%**
- Rendimento centrale dopo 30 giorni: **-8,47%**
- Discesa media durante i 30 giorni: **-18,79%**
- Massimo rialzo medio durante i 30 giorni: **21,18%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **0,09 $**
- Scenario centrale a 30 giorni: **0,08 $**
- Zona di rischio media: **0,07 $**
- Zona di rialzo media: **0,11 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -25,84% → **0,07 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -22,41% → **0,07 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: -8,47% → **0,08 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 9,89% → **0,10 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 32,92% → **0,12 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -33,55% → **0,06 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -30,59% → **0,06 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -17,22% → **0,07 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -7,87% → **0,08 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: -1,82% → **0,09 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 0,00% → **0,09 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 6,72% → **0,10 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 14,67% → **0,10 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 25,06% → **0,11 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 41,67% → **0,13 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| FIL-USD         | 2022-05-10   | 2022-08-17 |        84.8  |       -28.78 |         -31.42 |           0    |
| MANA-USD        | 2022-10-23   | 2023-01-30 |        83.63 |       -12.23 |         -16.35 |           7.7  |
| BTC-USD         | 2025-02-03   | 2025-05-13 |        83    |         1.69 |          -2.49 |           7.2  |
| SAND-USD        | 2021-04-20   | 2021-07-28 |        82.87 |         4.11 |         -14.27 |           8.86 |
| MATIC-USD       | 2022-04-26   | 2022-08-03 |        81.91 |        -1.77 |         -13.97 |          15.45 |
| INJ-USD         | 2021-05-18   | 2021-08-25 |        81.81 |       -24.85 |         -35.16 |          25.62 |
| NEAR-USD        | 2022-10-23   | 2023-01-30 |        81.53 |         0.56 |          -5.2  |          16.82 |
| MANA-USD        | 2025-01-30   | 2025-05-09 |        81.44 |       -20.93 |         -26.57 |           8.86 |
| QTUM-USD        | 2021-05-16   | 2021-08-23 |        81.37 |       -22.03 |         -32.66 |          16.48 |
| YFI-USD         | 2022-05-10   | 2022-08-17 |        80.76 |       -22.15 |         -23.92 |           0    |

</details>
<!-- COMPACT_SECTION_END:scanner_full_detail -->

<!-- COMPACT_SECTION_START:market_regime -->
<details>
<summary><strong>🌦️ Market Regime Match</strong></summary>

<!-- MARKET_REGIME_MATCH_START -->
# Market Regime Match Report


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [market_regime_match_report.md](market_regime_match_report.md)

Generated: 2026-09-09 05:31 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | snapshot_date   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | 2026-09-09 | RECOVERY | 79.123 $ | True | 24.48% | -5.56% | RECOVERY | 24.48% | -5.56% |
| DOGE-USD | 2026-09-09 | MIXED | 0.09043 $ | True | 5.18% | -12.77% | RECOVERY | 24.48% | -5.56% |
| SOL-USD | 2026-09-09 | RECOVERY | 104,43 $ | True | 56.28% | -10.14% | RECOVERY | 24.48% | -5.56% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 80.00% | 20.27% | 42.90% | 78.68% | -8.20% | -39.04% | 29.28% | 55.69% | 111.40% | 80.00% | 18.79% | 44.50% | 93.74% |
| BTC-USD | SAME_BTC_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| BTC-USD | SAME_ASSET_REGIME | 5 | 60.00% | 3.09% | 36.70% | 40.25% | -14.89% | -36.96% | 36.70% | 45.11% | 207.62% | 80.00% | 8.85% | 25.17% | 63.73% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| DOGE-USD | ALL_MATCHES | 40 | 37.50% | -8.47% | 9.89% | 32.92% | -17.22% | -33.55% | 14.67% | 25.06% | 41.67% | 37.50% | -7.01% | 11.42% | 43.96% |
| DOGE-USD | SAME_BTC_REGIME | 1 | 0.00% | -1.77% | -1.77% | -1.77% | -13.97% | -13.97% | 15.45% | 15.45% | 15.45% | 0.00% | -13.91% | -13.91% | -13.91% |
| DOGE-USD | SAME_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL-USD | ALL_MATCHES | 40 | 62.50% | 17.40% | 58.32% | 113.47% | -9.25% | -42.28% | 36.97% | 71.78% | 149.39% | 62.50% | 19.45% | 96.24% | 207.38% |
| SOL-USD | SAME_BTC_REGIME | 1 | 100.00% | 99.18% | 99.18% | 99.18% | -8.40% | -8.40% | 121.32% | 121.32% | 121.32% | 100.00% | 116.63% | 116.63% | 116.63% |
| SOL-USD | SAME_ASSET_REGIME | 4 | 75.00% | 39.66% | 81.40% | 151.20% | -13.26% | -39.78% | 180.53% | 321.36% | 331.09% | 75.00% | 57.31% | 116.05% | 163.93% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 14 | 71.43% | 29.40% | -17.90% | 63.27% | 71.43% | 44.79% | 106.16% |
| BTC-USD | HISTORICAL_BTC_BULL | 26 | 84.62% | 18.56% | -5.42% | 50.90% | 84.62% | 18.22% | 67.83% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 19 | 21.05% | -19.36% | -23.58% | 20.43% | 15.79% | -13.10% | 21.32% |
| DOGE-USD | HISTORICAL_BTC_BULL | 12 | 66.67% | 7.11% | -8.95% | 42.88% | 66.67% | 10.60% | 86.74% |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION | 8 | 37.50% | -10.82% | -20.15% | 27.82% | 50.00% | -1.15% | 41.17% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 1 | 0.00% | -1.77% | -13.97% | 15.45% | 0.00% | -13.91% | 15.45% |
| SOL-USD | HISTORICAL_BTC_BEAR | 20 | 50.00% | 0.63% | -19.30% | 47.26% | 50.00% | 0.39% | 73.78% |
| SOL-USD | HISTORICAL_BTC_BULL | 17 | 82.35% | 46.20% | -2.19% | 145.34% | 82.35% | 31.36% | 315.96% |
| SOL-USD | HISTORICAL_BTC_DISTRIBUTION | 2 | 0.00% | -7.27% | -19.74% | 17.02% | 0.00% | -5.17% | 18.93% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 1 | 100.00% | 99.18% | -8.40% | 121.32% | 100.00% | 116.63% | 141.68% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 29 | 86.21% | 20.77% | -4.97% | 52.49% | 86.21% | 19.19% | 69.58% |
| BTC-USD | HISTORICAL_ASSET_BULL | 5 | 60.00% | 7.49% | -7.66% | 89.19% | 40.00% | -4.71% | 179.49% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 100.00% | 91.00% | -16.34% | 125.42% | 100.00% | 162.43% | 162.43% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 5 | 60.00% | 3.09% | -14.89% | 45.11% | 80.00% | 8.85% | 103.03% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 19 | 36.84% | -7.43% | -15.36% | 19.09% | 31.58% | -13.69% | 36.99% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 18 | 38.89% | -15.95% | -24.22% | 29.76% | 44.44% | -3.05% | 44.61% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 50.00% | -6.73% | -12.50% | 36.07% | 50.00% | 8.14% | 36.07% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 1 | 0.00% | -16.58% | -20.55% | 0.00% | 0.00% | -11.78% | 0.00% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 30 | 63.33% | 15.56% | -7.49% | 61.05% | 63.33% | 16.10% | 81.74% |
| SOL-USD | HISTORICAL_ASSET_BULL | 4 | 50.00% | 50.13% | -17.28% | 150.55% | 50.00% | 68.33% | 240.52% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 50.00% | 40.65% | -19.07% | 96.88% | 50.00% | 76.43% | 124.64% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 4 | 75.00% | 39.66% | -13.26% | 321.36% | 75.00% | 57.31% | 321.36% |

## Top regime-adjusted matches

A single cohort is selected deterministically: SAME_BTC_AND_ASSET_REGIME, otherwise SAME_ASSET_REGIME, otherwise SAME_BTC_REGIME. Each level must have at least 5 matches; cohorts are never combined.

| target   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level        | selection_reason              |
|:---------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:----------------------|:------------------------------|
| BTC-USD | SAME_ASSET_REGIME | 0 | 5 | 0 | 5 | 5 | 1_SAME_ASSET_FALLBACK | FALLBACK_TO_SAME_ASSET_REGIME |
| DOGE-USD | NONE | 0 | 0 | 1 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES |
| SOL-USD | NONE | 0 | 4 | 1 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES |

- WARNING BTC-USD: SAME_ASSET_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | UNI-USD | 2023-04-07 | 88.00% | BULL | RECOVERY | SAME_ASSET_ONLY | HIGH_SPIKE_60D | -47.87% | -48.23% | 315.96% | -44.33% | -53.90% | 315.96% |
| BTC-USD | LRC-USD | 2020-03-12 | 85.00% | BEAR | RECOVERY | SAME_ASSET_ONLY | EXPLOSIVE_60D | 42.62% | -20.06% | 45.11% | 89.45% | -20.06% | 103.03% |
| BTC-USD | QTUM-USD | 2023-08-09 | 84.64% | BULL | RECOVERY | SAME_ASSET_ONLY | MIXED | 3.09% | -5.87% | 12.60% | 0.39% | -5.87% | 20.46% |
| BTC-USD | WAVES-USD | 2023-08-14 | 84.26% | BULL | RECOVERY | SAME_ASSET_ONLY | BULLISH_30D | 36.70% | 0.00% | 36.70% | 25.17% | 0.00% | 55.93% |
| BTC-USD | DASH-USD | 2020-08-29 | 83.61% | BULL | RECOVERY | SAME_ASSET_ONLY | BEARISH_30D | -12.81% | -14.89% | 7.15% | 8.85% | -14.89% | 45.20% |

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

Generato: 2026-09-09 05:32 UTC


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
| BTC | 79.123 $ | +1 | NEUTRALE / MISTO | STAGE 3 / DISTRIBUZIONE O PAUSA | VOLATILITÀ IN ESPANSIONE | SIGN OF STRENGTH POSSIBILE | BASSO | HOLD / ASPETTA ROTTURA RESISTENZA |
| SOL | 104,43 $ | +5 | COSTRUTTIVO / CONFERMA PARZIALE | STAGE 3 / DISTRIBUZIONE O PAUSA | MASSIMI E MINIMI CRESCENTI | SIGN OF STRENGTH POSSIBILE | MEDIO | TRANCHE PICCOLE / NO LEVA FINCHÉ NON ROMPE CONFERME |
| DOGE | 0.09043 $ | +4 | ANTICIPATO / COSTRUTTIVO MA NON CONFERMATO | STAGE 3 / DISTRIBUZIONE O PAUSA | COMPRESSIONE / TRIANGOLO POSSIBILE | ACCUMULO POSSIBILE / RANGE BASSO | MEDIO | STAI ALLA FINESTRA |

## Punteggi per area

| Asset | Trend | Struttura | Momentum | Volume | Prezzo | Candela | Wyckoff | Totale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +1 | 0 | -2 | 0 | 0 | 0 | +2 | +1 |
| SOL | +1 | +2 | -2 | +2 | 0 | 0 | +2 | +5 |
| DOGE | +1 | 0 | +3 | 0 | 0 | 0 | 0 | +4 |

## Livelli tecnici

| Asset | Supporto | Resistenza | Breakout 60g | Breakdown 60g | ATR14 | Rendimento 30g | Rendimento 90g |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 76.909 $ | 79.468 $ | 82.262 $ | 61.276 $ | 2,74% | 21,77% | 28,49% |
| SOL | 97,45 $ | 110,04 $ | 110,04 $ | 70,69 $ | 4,63% | 36,76% | 65,02% |
| DOGE | 0.08189 $ | 0.09169 $ | 0.09998 $ | 0.06797 $ | 4,52% | 30,16% | 8,66% |

## Lettura dettagliata

### BTC

- Prezzo: **79.123 $**
- Score classico: **+1 / 12**
- Verdetto: **NEUTRALE / MISTO**
- Azione coerente: **HOLD / ASPETTA ROTTURA RESISTENZA**
- Volatilità tecnica locale: **BASSO** — ATR14 2,74%; distanza supporto 2,66%; distanza resistenza 0,65%

Dettaglio:

- Trend: **+1** — prezzo sopra MA200 daily; breve termine sopra MA20/MA50; MA50 daily in salita; MA200 daily in discesa; STAGE 3 / DISTRIBUZIONE O PAUSA
- Stage weekly: **STAGE 3 / DISTRIBUZIONE O PAUSA** — Prezzo sopra MA30 weekly ma pendenza debole o piatta.
- Struttura: **0** — VOLATILITÀ IN ESPANSIONE
- Momentum: **-2** — RSI sano 62.1; RSI in peggioramento; MACD sotto signal; istogramma MACD in peggioramento
- Volume: **0** — OBV sotto media; CMF positivo 0.21; volume ratio 0.95
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **+2** — SIGN OF STRENGTH POSSIBILE. Prezzo nella parte alta del range con flusso volume positivo.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 62.13 |
| MACD histogram | -363.08079 |
| CMF20 | 0.205 |
| Volume ratio 20 | 0.95 |
| MA20 | 78.460 $ |
| MA50 | 69.969 $ |
| MA100 | 66.579 $ |
| MA200 | 69.869 $ |
| Pendenza MA50 20g | +9,37% |
| Pendenza MA200 60g | -5,71% |
| Bollinger width | 8,60% |
| Bollinger position | 0.57 |

### SOL

- Prezzo: **104,43 $**
- Score classico: **+5 / 12**
- Verdetto: **COSTRUTTIVO / CONFERMA PARZIALE**
- Azione coerente: **TRANCHE PICCOLE / NO LEVA FINCHÉ NON ROMPE CONFERME**
- Volatilità tecnica locale: **MEDIO** — ATR14 4,63%; distanza supporto 6,96%; distanza resistenza 5,57%

Dettaglio:

- Trend: **+1** — prezzo sopra MA200 daily; breve termine sopra MA20/MA50; MA50 daily in salita; MA200 daily in discesa; STAGE 3 / DISTRIBUZIONE O PAUSA
- Stage weekly: **STAGE 3 / DISTRIBUZIONE O PAUSA** — Prezzo sopra MA30 weekly ma pendenza debole o piatta.
- Struttura: **+2** — MASSIMI E MINIMI CRESCENTI
- Momentum: **-2** — RSI sano 63.5; RSI in peggioramento; MACD sotto signal; istogramma MACD in peggioramento
- Volume: **+2** — OBV sopra media; CMF positivo 0.20; volume ratio 0.63
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **+2** — SIGN OF STRENGTH POSSIBILE. Prezzo nella parte alta del range con flusso volume positivo.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 63.53 |
| MACD histogram | -0.51885 |
| CMF20 | 0.199 |
| Volume ratio 20 | 0.63 |
| MA20 | 100,79 $ |
| MA50 | 85,47 $ |
| MA100 | 79,36 $ |
| MA200 | 82,64 $ |
| Pendenza MA50 20g | +11,84% |
| Pendenza MA200 60g | -10,37% |
| Bollinger width | 19,83% |
| Bollinger position | 0.67 |

### DOGE

- Prezzo: **0.09043 $**
- Score classico: **+4 / 12**
- Verdetto: **ANTICIPATO / COSTRUTTIVO MA NON CONFERMATO**
- Azione coerente: **STAI ALLA FINESTRA**
- Volatilità tecnica locale: **MEDIO** — ATR14 4,52%; distanza supporto 10,07%; distanza resistenza 1,72%

Dettaglio:

- Trend: **+1** — prezzo sopra MA200 daily; breve termine sopra MA20/MA50; MA50 daily in salita; MA200 daily in discesa; STAGE 3 / DISTRIBUZIONE O PAUSA
- Stage weekly: **STAGE 3 / DISTRIBUZIONE O PAUSA** — Prezzo sopra MA30 weekly ma pendenza debole o piatta.
- Struttura: **0** — COMPRESSIONE / TRIANGOLO POSSIBILE
- Momentum: **+3** — RSI sano 62.3; MACD sopra signal; istogramma MACD in miglioramento
- Volume: **0** — OBV sotto media; CMF positivo 0.06; volume ratio 0.84
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **0** — Doji / indecisione
- Wyckoff: **0** — ACCUMULO POSSIBILE / RANGE BASSO. Prezzo nella metà bassa del range, ma senza spring confermato.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 62.32 |
| MACD histogram | 0.00015 |
| CMF20 | 0.065 |
| Volume ratio 20 | 0.84 |
| MA20 | 0.08712 $ |
| MA50 | 0.07715 $ |
| MA100 | 0.07834 $ |
| MA200 | 0.08834 $ |
| Pendenza MA50 20g | +7,39% |
| Pendenza MA200 60g | -13,02% |
| Bollinger width | 17,65% |
| Bollinger position | 0.69 |

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

Generato: 2026-09-09 05:32 UTC


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
| BTC | 79.123 $ | Doppio massimo | CANDIDATO | ribassista | n/a | 58.946 $ | n/a | 27,15% | Fib 23,6% NON ATTIVO (0) @ 76.477 $ | NEL RANGE | 76.248 $ |
| SOL | 104,43 $ | Doppio massimo | CANDIDATO | ribassista | n/a | 62,51 $ | n/a | 47,72% | Fib 23,6% NON ATTIVO (0) @ 98,33 $ | NEL RANGE | 97,45 $ |
| DOGE | 0.09043 $ | Doppio massimo | CANDIDATO | ribassista | n/a | 0.06214 $ | n/a | 33,04% | Fib 23,6% TESTATO (0) @ 0.08924 $ | NEL RANGE | 0.08930 $ |

## BTC

![Classic visual BTC](classic_visual_BTC.png)

- Pattern principale: **Doppio massimo**
- Stato pattern: **CANDIDATO** (0)
- Famiglia: **ribassista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-07-15 -> 2026-08-09**
- Età formazione: **31 giorni**
- Breakout pattern: **n/a**
- Età breakout: **n/a**
- Neckline: **62.227 $**
- Target teorico: **58.946 $**
- Progresso verso target: **n/a**
- Distanza dalla neckline: **27,15%**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 23,6% NON ATTIVO (0) @ 76.477 $** — Swing UP 2026-07-01 57.748 -> 2026-09-03 82.262; livello più vicino 23.6% a 76.477; stato NON ATTIVO; confluenza: supporto tecnico.
- Invalidazione: **63.471 $**
- Relazione prezzo/neckline: **sopra neckline**
- Dettaglio: Due massimi simili vicino a 65.508 tra 2026-07-15 e 2026-08-09. Neckline ribassista stimata: 62.227. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 31 giorni. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **NEL RANGE**
- Supporto: **76.248 $**
- Resistenza: **79.468 $**
- Breakout 60g: **82.262 $**
- Breakdown 60g: **61.276 $**
- RSI14: **62.79**
- ATR14: **2,74%**
- Volume ratio 20g: **0.95**
- Rendimento 30g: **+22,02%**
- Rendimento 90g: **+28,76%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Triangolo ascendente possibile | CANDIDATO | 0 | rialzista | n/a | n/a | n/a | n/a | n/a | n/a | n/a | Resistenza quasi piatta e minimi crescenti. Stato: CANDIDATO; il pattern non ha una neckline univoca da usare per il lifecycle. |
| Doppio minimo | CANDIDATO | 0 | rialzista | 82.792 $ | n/a | n/a | 90.626 $ | n/a | 4,64% | 81.136 $ | Due minimi simili a 74.959 $ e 76.248 $. Neckline circa 82.792 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 7 giorni. |
| Doppio massimo | CANDIDATO | 0 | ribassista | 62.227 $ | n/a | n/a | 58.946 $ | n/a | 27,15% | 63.471 $ | Due massimi simili a 65.508 $ e 65.402 $. Neckline circa 62.227 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 31 giorni. |

## SOL

![Classic visual SOL](classic_visual_SOL.png)

- Pattern principale: **Doppio massimo**
- Stato pattern: **CANDIDATO** (0)
- Famiglia: **ribassista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-07-15 -> 2026-08-09**
- Età formazione: **31 giorni**
- Breakout pattern: **n/a**
- Età breakout: **n/a**
- Neckline: **70,69 $**
- Target teorico: **62,51 $**
- Progresso verso target: **n/a**
- Distanza dalla neckline: **47,72%**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 23,6% NON ATTIVO (0) @ 98,33 $** — Swing UP 2026-06-06 60,41 -> 2026-08-27 110,04; livello più vicino 23.6% a 98,33; stato NON ATTIVO; confluenza: supporto tecnico.
- Invalidazione: **72,11 $**
- Relazione prezzo/neckline: **sopra neckline**
- Dettaglio: Due massimi simili vicino a 78,88 tra 2026-07-15 e 2026-08-09. Neckline ribassista stimata: 70,69. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 31 giorni. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **NEL RANGE**
- Supporto: **97,45 $**
- Resistenza: **110,04 $**
- Breakout 60g: **110,04 $**
- Breakdown 60g: **70,69 $**
- RSI14: **63.75**
- ATR14: **4,63%**
- Volume ratio 20g: **0.63**
- Rendimento 30g: **+37,03%**
- Rendimento 90g: **+65,34%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Doppio massimo | CANDIDATO | 0 | ribassista | 70,69 $ | n/a | n/a | 62,66 $ | n/a | 47,72% | 72,11 $ | Due massimi simili a 78,73 $ e 77,62 $. Neckline circa 70,69 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 31 giorni. |
| Testa e spalle inverso | TARGET RAGGIUNTO | 0 | rialzista | 78,17 $ | 2026-08-19 | 21g | 85,65 $ | 351,18% | n/a | 76,61 $ | Spalla sinistra 73,40 $, testa 70,69 $, spalla destra 74,20 $. Neckline circa 78,17 $. Breakout neckline: 2026-08-19 (21 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 85,65 $; progresso: 351,18%; prezzo sopra neckline. |
| Doppio minimo | TARGET RAGGIUNTO | 0 | rialzista | 78,73 $ | 2026-08-19 | 21g | 84,05 $ | 482,77% | n/a | 77,15 $ | Due minimi simili a 73,40 $ e 74,20 $. Neckline circa 78,73 $. Breakout neckline: 2026-08-19 (21 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 84,05 $; progresso: 482,77%; prezzo sopra neckline. |

## DOGE

![Classic visual DOGE](classic_visual_DOGE.png)

- Pattern principale: **Doppio massimo**
- Stato pattern: **CANDIDATO** (0)
- Famiglia: **ribassista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-07-26 -> 2026-08-11**
- Età formazione: **29 giorni**
- Breakout pattern: **n/a**
- Età breakout: **n/a**
- Neckline: **0.06797 $**
- Target teorico: **0.06214 $**
- Progresso verso target: **n/a**
- Distanza dalla neckline: **33,04%**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 23,6% TESTATO (0) @ 0.08924 $** — Swing DOWN 2026-05-14 0.11825 -> 2026-09-02 0.08028; livello più vicino 23.6% a 0.08924; stato TESTATO; confluenza: nessuna confluenza indipendente.
- Invalidazione: **0.06933 $**
- Relazione prezzo/neckline: **sopra neckline**
- Dettaglio: Due massimi simili vicino a 0.07380 tra 2026-07-26 e 2026-08-11. Neckline ribassista stimata: 0.06797. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 29 giorni. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **NEL RANGE**
- Supporto: **0.08930 $**
- Resistenza: **0.09169 $**
- Breakout 60g: **0.09998 $**
- Breakdown 60g: **0.06797 $**
- RSI14: **62.95**
- ATR14: **4,50%**
- Volume ratio 20g: **0.84**
- Rendimento 30g: **+30,58%**
- Rendimento 90g: **+9,01%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Doppio massimo | CANDIDATO | 0 | ribassista | 0.06797 $ | n/a | n/a | 0.06214 $ | n/a | 33,04% | 0.06933 $ | Due massimi simili a 0.07380 $ e 0.07286 $. Neckline circa 0.06797 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 29 giorni. |
| Doppio minimo | TARGET RAGGIUNTO | 0 | rialzista | 0.07923 $ | 2026-08-20 | 20g | 0.08952 $ | 108,88% | n/a | 0.07765 $ | Due minimi simili a 0.06961 $ e 0.06895 $. Neckline circa 0.07923 $. Breakout neckline: 2026-08-20 (20 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 0.08952 $; progresso: 108,88%; prezzo sopra neckline. |

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

Generato: 2026-09-09 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [fractal_path_tracker.md](fractal_path_tracker.md)

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-09-09**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-02-24**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **104,43 $**
- Verdetto principale: **ANALOGIA DEBOLE / SCENARIO SECONDARIO**
- Somiglianza strutturale: **+69,05%**
- Aderenza live principale: **+71,98%**
- Errore medio live principale: **14,01%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE SOLO DI CONTESTO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **95**
- Osservazioni inclusive dal bottom: **96**
- Osservazioni da inizio programma/scanner: **69**
- Errore assoluto medio dal bottom: **11,76%**
- Errore assoluto medio da inizio programma: **14,01%**
- Gap firmato medio ultimi 7 giorni: **+9,00%**
- Errore assoluto medio ultimi 7 giorni: **9,00%**
- Gap ultimo giorno: **+14,28%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **+14,28%**
- Gap firmato medio 7g: **+9,00%**
- Errore assoluto medio 7g: **9,00%**
- Variazione recente gap: **+3,69%**
- Stato gap: **IN DEVIAZIONE SOPRA IL FRATTALE**
- Trend gap: **SOL sta aumentando il distacco sopra il percorso ancorato**

Soglie operative del grafico:

- entro **±5%**: percorso vicino;
- tra **±5% e ±12%**: deviazione gestibile;
- oltre **±12%**: frattale non abbastanza aderente per conferma operativa;
- oltre **±18%**: disallineamento marcato.

## Ultimi giorni del confronto ancorato

|   Giorno | Data SOL   | Data BTC eq.   | SOL reale   | Percorso ancorato   | Gap firmato   | Fase                |
|---------:|:-----------|:---------------|:------------|:--------------------|:--------------|:--------------------|
| 86 | 2026-08-31 | 2023-02-15 | 103,00 $ | 95,75 $ | +7,56% | da inizio programma |
| 87 | 2026-09-01 | 2023-02-16 | 99,99 $ | 93,06 $ | +7,45% | da inizio programma |
| 88 | 2026-09-02 | 2023-02-17 | 100,39 $ | 96,77 $ | +3,74% | da inizio programma |
| 89 | 2026-09-03 | 2023-02-18 | 103,98 $ | 97,07 $ | +7,12% | da inizio programma |
| 90 | 2026-09-04 | 2023-02-19 | 101,95 $ | 95,83 $ | +6,38% | da inizio programma |
| 91 | 2026-09-05 | 2023-02-20 | 103,19 $ | 97,81 $ | +5,50% | da inizio programma |
| 92 | 2026-09-06 | 2023-02-21 | 106,45 $ | 96,26 $ | +10,58% | da inizio programma |
| 93 | 2026-09-07 | 2023-02-22 | 103,87 $ | 95,29 $ | +9,01% | da inizio programma |
| 94 | 2026-09-08 | 2023-02-23 | 103,87 $ | 94,33 $ | +10,10% | da inizio programma |
| 95 | 2026-09-09 | 2023-02-24 | 104,43 $ | 91,38 $ | +14,28% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-09-16 | 88,09 $ | 100,67 $ | 100,67 $ / 106,45 $ | no | n/a | n/a | n/a |
| 14g | 2026-09-23 | 79,52 $ | 90,88 $ | 90,88 $ / 106,45 $ | no | n/a | n/a | n/a |
| 21g | 2026-09-30 | 108,03 $ | 123,45 $ | 90,88 $ / 123,45 $ | no | n/a | n/a | n/a |
| 28g | 2026-10-07 | 108,30 $ | 123,77 $ | 90,88 $ / 127,55 $ | no | n/a | n/a | n/a |
| 35g | 2026-10-14 | 112,18 $ | 128,20 $ | 90,88 $ / 128,20 $ | no | n/a | n/a | n/a |
| 42g | 2026-10-21 | 110,01 $ | 125,71 $ | 90,88 $ / 128,20 $ | no | n/a | n/a | n/a |
| 49g | 2026-10-28 | 120,09 $ | 137,24 $ | 90,88 $ / 137,24 $ | no | n/a | n/a | n/a |
| 56g | 2026-11-04 | 107,45 $ | 122,79 $ | 90,88 $ / 137,24 $ | no | n/a | n/a | n/a |
| 63g | 2026-11-11 | 115,58 $ | 132,08 $ | 90,88 $ / 137,24 $ | no | n/a | n/a | n/a |
| 70g | 2026-11-18 | 116,34 $ | 132,95 $ | 90,88 $ / 137,24 $ | no | n/a | n/a | n/a |
| 77g | 2026-11-25 | 105,59 $ | 120,67 $ | 90,88 $ / 137,24 $ | no | n/a | n/a | n/a |
| 84g | 2026-12-02 | 105,93 $ | 121,05 $ | 90,88 $ / 137,24 $ | no | n/a | n/a | n/a |
| 91g | 2026-12-09 | 105,25 $ | 120,28 $ | 90,88 $ / 137,24 $ | no | n/a | n/a | n/a |
| 98g | 2026-12-16 | 107,34 $ | 122,67 $ | 90,88 $ / 137,24 $ | no | n/a | n/a | n/a |
| 105g | 2026-12-23 | 104,31 $ | 119,21 $ | 90,88 $ / 137,24 $ | no | n/a | n/a | n/a |
| 112g | 2026-12-30 | 103,71 $ | 118,52 $ | 90,88 $ / 137,24 $ | no | n/a | n/a | n/a |
| 119g | 2027-01-06 | 120,92 $ | 138,18 $ | 90,88 $ / 138,18 $ | no | n/a | n/a | n/a |
| 126g | 2027-01-13 | 120,06 $ | 137,20 $ | 90,88 $ / 138,18 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 55 | 36,36% | 11,03% | 12,91% |
| 14g | 48 | 27,08% | 18,17% | 11,73% |
| 21g | 41 | 14,63% | 27,72% | 13,39% |
| 28g | 35 | 31,43% | 25,67% | 12,85% |
| 35g | 29 | 44,83% | 17,59% | 12,02% |
| 42g | 22 | 90,91% | 8,28% | 11,14% |
| 49g | 15 | 100,00% | 6,13% | 10,95% |
| 56g | 8 | 100,00% | 7,13% | 9,31% |
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

Ultima lettura salvata: **2026-09-09** — SOL 104,43 $, gap +14,28%, somiglianza +69,05%.

Nel report principale lascio solo il link, così non diventa troppo lungo.

<!-- SOL_BTC_FRACTAL_HISTORY_END -->

</details>
<!-- COMPACT_SECTION_END:fractal_path -->

<!-- COMPACT_SECTION_START:exchange_microstructure -->
<details>
<summary><strong>🏦 Dati exchange, liquidità e leva</strong></summary>

<!-- EXCHANGE_MICROSTRUCTURE_START -->
# Dati exchange, liquidità e leva

Generato: 2026-09-09 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [exchange_microstructure_report.md](exchange_microstructure_report.md)

Questo modulo legge Kraken Futures, Bitget Futures e KuCoin Futures come nucleo derivati. OKX e Coinbase vengono raccolti come fonti ausiliarie non pesate.
Non modifica la formula matematica di RSI, Fibonacci o Wyckoff: controlla se quei segnali sono sostenuti da acquisti, vendite, OI, funding e liquidità.

**Limite importante:** questo nucleo non assume disponibile un feed pubblico completo delle liquidazioni. La componente liquidazioni resta neutrale; le zone future restano stime di pressione, non dati certi delle singole posizioni.

Diagnostica completa: [exchange_source_diagnostics.md](exchange_source_diagnostics.md)

## Sintesi

| Asset | Prezzo | Exchange | Segnale candidato | Peso Global | Bias exchange | Confidenza | Copertura | Funding 8h eq. | OI 24h | Taker flow (campione/4h) | Book 0,5% | Liq long campione | Liq short campione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 79.100 $ | 3 | 0 | 0 | LEGGERMENTE POSITIVA / NON PESATA | BASSA | 100% | +0,0074% | +1,21% | 9,11 | -1,05% | 0 $ | 0 $ |
| SOL | 104,15 $ | 3 | 0 | 0 | LEGGERMENTE POSITIVA / NON PESATA | BASSA | 100% | +0,0017% | -0,20% | 2,40 | +1,45% | 0 $ | 0 $ |
| DOGE | 0.09035 $ | 3 | 0 | 0 | LEGGERMENTE POSITIVA / NON PESATA | BASSA | 100% | +0,0076% | -1,20% | 2,82 | -0,63% | 0 $ | 0 $ |

Il segnale candidato è limitato a **±1**, ma il peso nel Global resta **0** finché il tracker a 7 giorni non raggiunge 30 controlli, almeno 55% di accuratezza e return corretto direzione positivo. Un singolo muro o funding non basta.

La colonna taker usa un campione recente nel primo run. Dopo almeno 3 fotografie distribuite su almeno 45 minuti viene sostituita automaticamente dalla media intraday 4h.

## Dati separati per exchange

| Asset | Exchange | Stato | Funding 8h eq. | Open interest | Taker flow | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | Kraken | OK | +0,0188% | 167,95 mln $ | 58,89 | -0,22% |
| BTC | Bitget | OK | +0,0075% | 2,76 mld $ | 152,52 | -15,36% |
| BTC | Kucoin | OK | +0,0055% | 1,14 mld $ | 0,42 | +6,37% |
| SOL | Kraken | OK | +0,0226% | 30,04 mln $ | 0,42 | -14,90% |
| SOL | Bitget | OK | +0,0010% | 469,78 mln $ | 163,81 | +23,99% |
| SOL | Kucoin | OK | +0,0000% | 195,83 mln $ | 0,39 | +0,87% |
| DOGE | Kraken | OK | +0,0192% | 4,61 mln $ | 0,67 | -2,38% |
| DOGE | Bitget | OK | +0,0082% | 113,38 mln $ | 18,08 | -1,30% |
| DOGE | Kucoin | OK | +0,0100% | 77,16 mln $ | 1,13 | -4,73% |

Kraken, Bitget e KuCoin contribuiscono a funding normalizzato, open interest, trade aggressivi e order book. Non viene inventato un long/short ratio pubblico né un feed completo delle liquidazioni.

## Conferme per indicatori tecnici

### BTC

- Score grezzo exchange: **+1,75**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 3, accuratezza +66,67%.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 1, bear 0, divergenze 1.
- Flusso taker/order book: **+1,75**.
- OI/funding/basis: **+0,00**.
- Affollamento long/short: **+0,00**.
- Liquidazioni: **NON PESATE / FEED COMPLETO NON ASSUNTO DISPONIBILE**.
- **Wyckoff:** Fase Wyckoff non abbastanza chiara per una conferma exchange.
- **Fibonacci:** Fibonacci non_attivo; nessuna conferma exchange netta. Confluenza tecnica dichiarata: supporto tecnico.
- **RSI:** RSI in zona non estrema o flusso exchange non abbastanza netto.
- **Pattern:** I pattern candidati restano non operativi: i dati exchange possono solo preparare la conferma.
- **Breakout/breakdown:** Prezzo non abbastanza vicino a un livello chiave o flusso non netto.
- **Mappa liquidità attuale:** muro bid: n/a; muro ask: n/a

![Microstruttura exchange BTC](exchange_microstructure_BTC.png)

### SOL

- Score grezzo exchange: **+1,75**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 5, accuratezza +60,00%.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 0, bear 1, divergenze 1.
- Flusso taker/order book: **+1,75**.
- OI/funding/basis: **+0,00**.
- Affollamento long/short: **+0,00**.
- Liquidazioni: **NON PESATE / FEED COMPLETO NON ASSUNTO DISPONIBILE**.
- **Wyckoff:** Fase Wyckoff non abbastanza chiara per una conferma exchange.
- **Fibonacci:** Fibonacci non_attivo; nessuna conferma exchange netta. Confluenza tecnica dichiarata: supporto tecnico.
- **RSI:** RSI in zona non estrema o flusso exchange non abbastanza netto.
- **Pattern:** I pattern candidati restano non operativi: i dati exchange possono solo preparare la conferma.
- **Breakout/breakdown:** Prezzo non abbastanza vicino a un livello chiave o flusso non netto.
- **Mappa liquidità attuale:** muro bid: n/a; muro ask: n/a

![Microstruttura exchange SOL](exchange_microstructure_SOL.png)

### DOGE

- Score grezzo exchange: **+1,75**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 8, accuratezza +50,00%.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 1, bear 1, divergenze 0.
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

![Microstruttura exchange DOGE](exchange_microstructure_DOGE.png)

## Overlay sulle previsioni a 30 giorni

La previsione storica grezza dello scanner resta intatta. L'overlay exchange può correggerla solo dopo almeno 30 controlli maturati a 30 giorni e solo se il modulo dimostra accuratezza direzionale almeno del 55%.

| Asset | Prob. grezza salita | Return p50 grezzo | Controlli 30g | Accuratezza exchange | Stato overlay | Peso | Prob. corretta | Return corretto |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +80,00% | +20,27% | 1 | +0,00% | RACCOLTA DATI | 0,00 | +80,00% | +20,27% |
| SOL | +62,50% | +17,40% | 2 | +100,00% | RACCOLTA DATI | 0,00 | +62,50% | +17,40% |
| DOGE | +37,50% | -8,47% | 4 | +75,00% | RACCOLTA DATI | 0,00 | +37,50% | -8,47% |

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

Generato: 2026-09-09 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [exchange_signal_tracker_report.md](exchange_signal_tracker_report.md)

Questo tracker verifica se il segnale candidato exchange ±1 anticipa correttamente la direzione del prezzo a 1/3/7/14/30 giorni.
Il peso Global resta 0 finché l'orizzonte 7g non ha almeno 30 controlli, accuratezza almeno 55% e return corretto direzione positivo. L'overlay a 30g ha un gate separato.

Controlli maturati completati in questa esecuzione: **15**.

## Ultime fotografie giornaliere

| Data | Asset | Prezzo | Versione | Calibrazione | Candidato | Peso Global | Score raw | Confidenza | Taker 4h | OI 24h | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-09-09 | BTC | 79.100,00 | V2.1.3 | OK | 0 | 0 | 1,75 | BASSA | 9,11 | +1,21% | -1,05% |
| 2026-09-09 | DOGE | 0.09035 | V2.1.3 | OK | 0 | 0 | 1,75 | BASSA | 2,82 | -1,20% | -0,63% |
| 2026-09-09 | SOL | 104,15 | V2.1.3 | OK | 0 | 0 | 1,75 | BASSA | 2,40 | -0,20% | +1,45% |
| 2026-09-08 | BTC | 78.728,60 | V2.1.3 | OK | 0 | 0 | 1,75 | BASSA | 1,33 | +0,59% | -1,63% |
| 2026-09-08 | DOGE | 0.08985 | V2.1.3 | OK | 0 | 0 | 1,75 | BASSA | 1,16 | -2,94% | +1,74% |
| 2026-09-08 | SOL | 103,18 | V2.1.3 | OK | 0 | 0 | 1,75 | BASSA | 1,63 | -2,35% | -2,79% |
| 2026-09-07 | BTC | 79.707,00 | V2.1.3 | OK | 0 | 0 | 2,00 | BASSA | 1,26 | -1,97% | +0,37% |
| 2026-09-07 | DOGE | 0.08993 | V2.1.3 | OK | 0 | 0 | -0,25 | BASSA | 0,78 | -5,60% | +5,30% |
| 2026-09-07 | SOL | 105,30 | V2.1.3 | OK | 0 | 0 | -0,25 | BASSA | 0,80 | -0,56% | +4,43% |

## Accuratezza direzionale

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 5 | +40,00% | -0,26% | -0,89% | +0,60% | FEEDBACK RAPIDO |
| BTC | 3g | 5 | +40,00% | +0,25% | -2,11% | +2,12% | FEEDBACK RAPIDO |
| BTC | 7g | 3 | +66,67% | +0,53% | -2,29% | +3,66% | FEEDBACK RAPIDO |
| BTC | 14g | 3 | +33,33% | -0,17% | -3,31% | +4,48% | FEEDBACK RAPIDO |
| BTC | 30g | 1 | +0,00% | -0,24% | -3,45% | +3,82% | FEEDBACK RAPIDO |
| SOL | 1g | 5 | +60,00% | +0,93% | +0,43% | +3,39% | FEEDBACK RAPIDO |
| SOL | 3g | 5 | +60,00% | +2,75% | -3,02% | +7,77% | FEEDBACK RAPIDO |
| SOL | 7g | 5 | +60,00% | +3,63% | -3,62% | +9,63% | FEEDBACK RAPIDO |
| SOL | 14g | 5 | +80,00% | +8,45% | -4,32% | +14,61% | FEEDBACK RAPIDO |
| SOL | 30g | 2 | +100,00% | +22,28% | -5,94% | +27,20% | FEEDBACK RAPIDO |
| DOGE | 1g | 9 | +44,44% | +0,77% | -0,33% | +1,78% | FEEDBACK RAPIDO |
| DOGE | 3g | 9 | +33,33% | +1,22% | -3,22% | +5,78% | FEEDBACK RAPIDO |
| DOGE | 7g | 8 | +50,00% | -0,83% | -4,47% | +8,09% | FEEDBACK RAPIDO |
| DOGE | 14g | 7 | +42,86% | +0,79% | -5,33% | +14,98% | FEEDBACK RAPIDO |
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

**DOGE** — DOGE: i futures sembrano più vulnerabili verso una discesa improvvisa. Non significa che deve scendere, ma se rompe sotto può accelerare. Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale.

| Asset | Prezzo | Funding | OI 24h | Long/Short | Lettura futures | Forza |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 79.123 $ | +0.0043% | -5.32% | 1.24 | Misto | 1/5 |
| SOL | 104,43 $ | -0.0046% | -17.50% | 1.87 | Misto | 1/5 |
| DOGE | 0.09043 $ | +0.0100% | -9.55% | 5.38 | Rischio sotto | 2/5 |

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

Generato: 2026-09-09 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [rsi_multitimeframe_divergence_report.md](rsi_multitimeframe_divergence_report.md)

Il modulo confronta prezzo e RSI 14 sui pivot confermati **daily e weekly**. Riconosce divergenze regolari e nascoste, segnali in formazione, invalidazioni e semplice conferma del momentum.

**Peso operativo: 0.** Non modifica il Global Confluence, non cambia le soglie del Paper Trading e non apre né blocca operazioni. I risultati vengono misurati prima di qualsiasi futura decisione sul peso.

## Sintesi corrente

| Asset   | Daily                                                | Stato D       | Weekly             | Stato W       | Lettura weekly                                                                                                              |   Peso |
|:--------|:-----------------------------------------------------|:--------------|:-------------------|:--------------|:----------------------------------------------------------------------------------------------------------------------------|-------:|
| BTC     | Hidden bullish                                       | IN_FORMAZIONE | Conferma rialzista | CONTESTO      | Prezzo e RSI stanno salendo insieme: momentum rialzista confermato.                                                         |      0 |
| SOL     | Momentum in indebolimento, divergenza non confermata | CONTESTO      | Hidden bearish     | IN_FORMAZIONE | Hidden bearish in formazione: il secondo estremo non è ancora un pivot confermato. Peso operativo sempre 0.                 |      0 |
| DOGE    | Misto / nessuna divergenza                           | CONTESTO      | Hidden bearish     | CONFERMATA    | Hidden bearish confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto. |      0 |

## Dettaglio dei pivot

| Asset   | TF   | Tipo                                                 | Stato         | Prezzo / RSI      | Pivot confrontati                                                   | Δ prezzo contesto   | Δ RSI contesto   |   Peso |
|:--------|:-----|:-----------------------------------------------------|:--------------|:------------------|:--------------------------------------------------------------------|:--------------------|:-----------------|-------:|
| BTC     | 1D   | Hidden bullish                                       | IN_FORMAZIONE | 78.952 $ / 62,10  | 2026-09-02 76.248 $ / RSI 65,21 → 2026-09-09 78.446 $ / RSI 62,10   | n/a                 | n/a              |      0 |
| BTC     | 1W   | Conferma rialzista                                   | CONTESTO      | 78.952 $ / 57,19  | n/a                                                                 | +24,37%             | 18,35            |      0 |
| SOL     | 1D   | Momentum in indebolimento, divergenza non confermata | CONTESTO      | 104,24 $ / 63,54  | n/a                                                                 | +7,90%              | -16,05           |      0 |
| SOL     | 1W   | Hidden bearish                                       | IN_FORMAZIONE | 104,24 $ / 58,59  | 2026-08-30 110,04 $ / RSI 57,95 → 2026-09-06 107,12 $ / RSI 60,25   | n/a                 | n/a              |      0 |
| DOGE    | 1D   | Misto / nessuna divergenza                           | CONTESTO      | 0.09015 $ / 62,34 | n/a                                                                 | +5,17%              | -2,00            |      0 |
| DOGE    | 1W   | Hidden bearish                                       | CONFERMATA    | 0.09015 $ / 48,53 | 2026-05-17 0.11825 $ / RSI 44,25 → 2026-08-23 0.09998 $ / RSI 49,72 | n/a                 | n/a              |      0 |

### BTC

- **1D — Hidden bullish / IN_FORMAZIONE**: Hidden bullish in formazione: il secondo estremo non è ancora un pivot confermato. Peso operativo sempre 0.
- **1W — Conferma rialzista / CONTESTO**: Prezzo e RSI stanno salendo insieme: momentum rialzista confermato.

### SOL

- **1D — Momentum in indebolimento, divergenza non confermata / CONTESTO**: Momentum in indebolimento, divergenza non confermata. Non esiste una divergenza confermata sugli ultimi pivot.
- **1W — Hidden bearish / IN_FORMAZIONE**: Hidden bearish in formazione: il secondo estremo non è ancora un pivot confermato. Peso operativo sempre 0.

### DOGE

- **1D — Misto / nessuna divergenza / CONTESTO**: Misto / nessuna divergenza. Non esiste una divergenza confermata sugli ultimi pivot.
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

Generato: 2026-09-09 05:32 UTC


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
| BTC | 79.123 $ | 7 | RIALZISTA TECNICO | Trend rialzista | Momentum debole | Struttura rialzista con massimi e minimi crescenti | 0 | 0 / NON ATTIVO | Doppio minimo / TARGET RAGGIUNTO | Doppio massimo / CANDIDATO | 76.248 | 82.262 |
| SOL | 104,43 $ | 7 | RIALZISTA TECNICO | Trend rialzista | Momentum debole | Struttura rialzista con massimi e minimi crescenti | 0 | 0 / NON ATTIVO | Doppio minimo / TARGET RAGGIUNTO | Doppio massimo / CANDIDATO | 97,45 | 110,04 |
| DOGE | 0.09043 $ | 10 | RIALZISTA TECNICO | Trend rialzista | Momentum in miglioramento | Struttura rialzista con massimi e minimi crescenti | 0 | 0 / TESTATO | Doppio minimo / TARGET RAGGIUNTO | Doppio massimo / CANDIDATO | 0.08028 | 0.09998 |

## Riepilogo ciclo di vita pattern

| Asset   | Doppio minimo    | Triplo minimo    | Adam/Eve Bottom                        | Doppio massimo   | Triplo massimo   | Adam/Eve Top                 |   Punteggio pattern |
|:--------|:-----------------|:-----------------|:---------------------------------------|:-----------------|:-----------------|:-----------------------------|--------------------:|
| BTC | TARGET RAGGIUNTO | TARGET RAGGIUNTO | Adam and Eve Bottom — TARGET RAGGIUNTO | CANDIDATO | CANDIDATO | ASSENTE | 0 |
| SOL | TARGET RAGGIUNTO | TARGET RAGGIUNTO | Adam and Eve Bottom — TARGET RAGGIUNTO | CANDIDATO | CANDIDATO | Adam and Eve Top — CANDIDATO | 0 |
| DOGE | TARGET RAGGIUNTO | TARGET RAGGIUNTO | Adam and Eve Bottom — TARGET RAGGIUNTO | CANDIDATO | CANDIDATO | Adam and Eve Top — CANDIDATO | 0 |

## Indicatori tecnici

| Asset   |   RSI 14 |   Istogramma MACD | MA20    | MA50    | MA200   | Pendenza MA50 20g   | Pendenza MA200 60g   | Rendimento 30g   | Rendimento 90g   |
|:--------|---------:|------------------:|:--------|:--------|:--------|:--------------------|:---------------------|:-----------------|:-----------------|
| BTC | 62.79 | -352.586 | 78.469 | 69.972 | 69.870 | 8,93% | -5,56% | 23,80% | 24,48% |
| SOL | 63.75 | -0.50609 | 100,80 | 85,48 | 82,64 | 11,55% | -10,14% | 37,51% | 56,28% |
| DOGE | 62.95 | 0.00017 | 0.08714 | 0.07716 | 0.08835 | 7,15% | -12,77% | 29,76% | 5,18% |

## Dettaglio asset

### BTC

- Prezzo: **79.123 $**
- Punteggio tecnico: **7 / 12**
- Verdetto: **RIALZISTA TECNICO**
- Trend: **Trend rialzista** (3)
- Momentum: **Momentum debole** (-2)
- Volume: **Volume da accumulazione** (2)
- Struttura: **Struttura rialzista con massimi e minimi crescenti** (2)
  - Dettaglio struttura: Ultimi minimi: 6.249e+04 -> 7.625e+04. Ultimi massimi: 8.135e+04 -> 8.226e+04.
- Divergenza: **Nessuna** (0)
- Fase Wyckoff candidata: **Markup / fase rialzista** (2)
  - Dettaglio Wyckoff: Prezzo sopra MA200, MA50 in salita e trend a 30 giorni positivo.
- Fibonacci automatico: **NON ATTIVO** (0)
  - Swing UP 2026-07-01 57.748 -> 2026-09-03 82.262; livello più vicino 23.6% a 76.477; stato NON ATTIVO; confluenza: supporto tecnico.
- Punteggio pattern: **0**
  - rialzista dominante: Doppio minimo (TARGET RAGGIUNTO, 0); ribassista dominante: Doppio massimo (CANDIDATO, 0).
- Supporto più vicino: **76.248**
- Resistenza più vicina: **82.262**

Pattern classici e ciclo di vita:

- Doppio minimo: **TARGET RAGGIUNTO** (0)
  - Due minimi simili vicino a 62.227 tra 2026-08-03 e 2026-08-14. Neckline stimata: 65.402. Breakout neckline: 2026-08-19 (21 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 68.577; progresso corrente: 432,15%. Relazione prezzo/neckline: sopra neckline.
  - neckline 65.402; target 68.577; breakout 2026-08-19 (21g); progresso 432,15%; prezzo sopra neckline.
- Triplo minimo: **TARGET RAGGIUNTO** (0)
  - Tre minimi simili vicino a 62.201 dal 2026-06-18 al 2026-08-14. Neckline stimata: 66.910. Breakout neckline: 2026-08-19 (21 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 71.619; progresso corrente: 259,35%. Relazione prezzo/neckline: sopra neckline.
  - neckline 66.910; target 71.619; breakout 2026-08-19 (21g); progresso 259,35%; prezzo sopra neckline.
- Adam and Eve Bottom: **TARGET RAGGIUNTO** (0)
  - Pattern Adam and Eve Bottom vicino a 58.076 dal 2026-06-25 al 2026-08-14. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 66.910. Breakout neckline: 2026-08-19 (21 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 75.744; progresso corrente: 138,25%. Relazione prezzo/neckline: sopra neckline.
  - neckline 66.910; target 75.744; breakout 2026-08-19 (21g); progresso 138,25%; prezzo sopra neckline.
- Doppio massimo: **CANDIDATO** (0)
  - Due massimi simili vicino a 65.508 tra 2026-07-15 e 2026-08-09. Neckline ribassista stimata: 62.227. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 31 giorni.
  - neckline 62.227; target 58.946; distanza dalla neckline 27,15%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 65.544 dal 2026-06-22 al 2026-08-09. Neckline ribassista stimata: 57.748. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 31 giorni.
  - neckline 57.748; target 49.952; distanza dalla neckline 37,01%; prezzo sopra neckline.
- Adam/Eve Top: **ASSENTE** (0)

### SOL

- Prezzo: **104,43 $**
- Punteggio tecnico: **7 / 12**
- Verdetto: **RIALZISTA TECNICO**
- Trend: **Trend rialzista** (3)
- Momentum: **Momentum debole** (-2)
- Volume: **Volume da accumulazione** (2)
- Struttura: **Struttura rialzista con massimi e minimi crescenti** (2)
  - Dettaglio struttura: Ultimi minimi: 74.2 -> 97.45. Ultimi massimi: 77.62 -> 110.
- Divergenza: **Nessuna** (0)
- Fase Wyckoff candidata: **Markup / fase rialzista** (2)
  - Dettaglio Wyckoff: Prezzo sopra MA200, MA50 in salita e trend a 30 giorni positivo.
- Fibonacci automatico: **NON ATTIVO** (0)
  - Swing UP 2026-06-06 60,41 -> 2026-08-27 110,04; livello più vicino 23.6% a 98,33; stato NON ATTIVO; confluenza: supporto tecnico.
- Punteggio pattern: **0**
  - rialzista dominante: Doppio minimo (TARGET RAGGIUNTO, 0); ribassista dominante: Doppio massimo (CANDIDATO, 0).
- Supporto più vicino: **97,45**
- Resistenza più vicina: **110,04**

Pattern classici e ciclo di vita:

- Doppio minimo: **TARGET RAGGIUNTO** (0)
  - Due minimi simili vicino a 73,40 tra 2026-07-17 e 2026-08-16. Neckline stimata: 78,73. Breakout neckline: 2026-08-19 (21 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 84,05; progresso corrente: 482,77%. Relazione prezzo/neckline: sopra neckline.
  - neckline 78,73; target 84,05; breakout 2026-08-19 (21g); progresso 482,77%; prezzo sopra neckline.
- Triplo minimo: **TARGET RAGGIUNTO** (0)
  - Tre minimi simili vicino a 70,69 dal 2026-07-17 al 2026-08-16. Neckline stimata: 78,73. Breakout neckline: 2026-08-19 (21 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 86,76; progresso corrente: 320,03%. Relazione prezzo/neckline: sopra neckline.
  - neckline 78,73; target 86,76; breakout 2026-08-19 (21g); progresso 320,03%; prezzo sopra neckline.
- Adam and Eve Bottom: **TARGET RAGGIUNTO** (0)
  - Pattern Adam and Eve Bottom vicino a 67,92 dal 2026-06-19 al 2026-08-01. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 83,81. Breakout neckline: 2026-08-19 (21 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 99,70; progresso corrente: 129,77%. Relazione prezzo/neckline: sopra neckline.
  - neckline 83,81; target 99,70; breakout 2026-08-19 (21g); progresso 129,77%; prezzo sopra neckline.
- Doppio massimo: **CANDIDATO** (0)
  - Due massimi simili vicino a 78,88 tra 2026-07-15 e 2026-08-09. Neckline ribassista stimata: 70,69. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 31 giorni.
  - neckline 70,69; target 62,51; distanza dalla neckline 47,72%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 78,88 dal 2026-07-15 al 2026-08-09. Neckline ribassista stimata: 70,69. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 31 giorni.
  - neckline 70,69; target 62,51; distanza dalla neckline 47,72%; prezzo sopra neckline.
- Adam and Eve Top: **CANDIDATO** (0)
  - Pattern Adam and Eve Top vicino a 77,62 dal 2026-06-22 al 2026-08-09. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 64,42. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 31 giorni.
  - neckline 64,42; target 51,22; distanza dalla neckline 62,11%; prezzo sopra neckline.

### DOGE

- Prezzo: **0.09043 $**
- Punteggio tecnico: **10 / 12**
- Verdetto: **RIALZISTA TECNICO**
- Trend: **Trend rialzista** (3)
- Momentum: **Momentum in miglioramento** (3)
- Volume: **Volume neutrale** (0)
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
  - Due minimi simili vicino a 0.06829 tra 2026-07-24 e 2026-08-12. Neckline stimata: 0.07380. Breakout neckline: 2026-08-19 (21 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 0.07931; progresso corrente: 301,69%. Relazione prezzo/neckline: sopra neckline.
  - neckline 0.07380; target 0.07931; breakout 2026-08-19 (21g); progresso 301,69%; prezzo sopra neckline.
- Triplo minimo: **TARGET RAGGIUNTO** (0)
  - Tre minimi simili vicino a 0.06895 dal 2026-07-08 al 2026-08-12. Neckline stimata: 0.07380. Breakout neckline: 2026-08-19 (21 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 0.07866; progresso corrente: 342,59%. Relazione prezzo/neckline: sopra neckline.
  - neckline 0.07380; target 0.07866; breakout 2026-08-19 (21g); progresso 342,59%; prezzo sopra neckline.
- Adam and Eve Bottom: **TARGET RAGGIUNTO** (0)
  - Pattern Adam and Eve Bottom vicino a 0.06829 dal 2026-07-24 al 2026-08-06. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 0.07380. Breakout neckline: 2026-08-19 (21 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 0.07931; progresso corrente: 301,69%. Relazione prezzo/neckline: sopra neckline.
  - neckline 0.07380; target 0.07931; breakout 2026-08-19 (21g); progresso 301,69%; prezzo sopra neckline.
- Doppio massimo: **CANDIDATO** (0)
  - Due massimi simili vicino a 0.07380 tra 2026-07-26 e 2026-08-11. Neckline ribassista stimata: 0.06797. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 29 giorni.
  - neckline 0.06797; target 0.06214; distanza dalla neckline 33,04%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 0.07923 dal 2026-07-04 al 2026-08-11. Neckline ribassista stimata: 0.06797. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 29 giorni.
  - neckline 0.06797; target 0.05671; distanza dalla neckline 33,04%; prezzo sopra neckline.
- Adam and Eve Top: **CANDIDATO** (0)
  - Pattern Adam and Eve Top vicino a 0.07923 dal 2026-07-04 al 2026-08-11. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 0.06797. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 29 giorni.
  - neckline 0.06797; target 0.05671; distanza dalla neckline 33,04%; prezzo sopra neckline.

## Fibonacci automatico

Il modulo seleziona uno swing recente tramite pivot confermati. Un semplice tocco vale 0: Fibonacci pesa al massimo ±1 soltanto quando il livello è tenuto, perso, recuperato o respinto e coincide con almeno un livello tecnico indipendente.

| Asset   | Swing                         | 23,6%   | 38,2%   | 50,0%   | 61,8%   | 78,6%   | Livello vicino   | Stato      | Confluenza                      |   Score |
|:--------|:------------------------------|:--------|:--------|:--------|:--------|:--------|:-----------------|:-----------|:--------------------------------|--------:|
| BTC | UP 2026-07-01 -> 2026-09-03 | 76.477 | 72.898 | 70.005 | 67.112 | 62.994 | 23.6% / 76.477 | NON ATTIVO | supporto tecnico | 0 |
| SOL | UP 2026-06-06 -> 2026-08-27 | 98,33 | 91,08 | 85,23 | 79,37 | 71,03 | 23.6% / 98,33 | NON ATTIVO | supporto tecnico | 0 |
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

- **BTC**: 30/30 previsioni controllate su 67 fatte. Stato: **ATTIVA**.
- **SOL**: 30/30 previsioni controllate su 67 fatte. Stato: **ATTIVA**.
- **DOGE**: 30/30 previsioni controllate su 67 fatte. Stato: **ATTIVA**.

| Asset | Previsioni fatte | Controllate | Progresso | In attesa | Stato | Prossimo controllo |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 67 | 30 | 30/30 [██████████] | 37 | ATTIVA | 2026-09-10 / tra 1 giorno |
| SOL | 67 | 30 | 30/30 [██████████] | 37 | ATTIVA | 2026-09-10 / tra 1 giorno |
| DOGE | 67 | 30 | 30/30 [██████████] | 37 | ATTIVA | 2026-09-10 / tra 1 giorno |

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

Generato: 2026-09-09 05:33 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [data_quality_coherence_report.md](data_quality_coherence_report.md)

Questo controllo non modifica punteggi o decisioni. Verifica che tutti i moduli usino lo stesso prezzo corrente e che le nuove regole Technical/Classic Visual siano integre.

## Stato finale: **WARN**

## Avvisi

- 1 campi prezzo superano la tolleranza specifica del modulo.

## Prezzo unico per modulo

| Modulo                  | Asset   | Campo             | Stato   | Prezzo snapshot   | Prezzo modulo   | Differenza   |
|:------------------------|:--------|:------------------|:--------|:------------------|:----------------|:-------------|
| Scanner                 | BTC     | current_price     | OK      | 79.123 $          | 79.123 $        | +0,0000%     |
| Scanner                 | DOGE    | current_price     | OK      | 0.09043 $         | 0.09043 $       | -0,0000%     |
| Scanner                 | SOL     | current_price     | OK      | 104,43 $          | 104,43 $        | +0,0000%     |
| Scanner Forecast        | BTC     | current_price     | OK      | 79.123 $          | 79.123 $        | +0,0000%     |
| Scanner Forecast        | SOL     | current_price     | OK      | 104,43 $          | 104,43 $        | +0,0000%     |
| Scanner Forecast        | DOGE    | current_price     | OK      | 0.09043 $         | 0.09043 $       | -0,0000%     |
| Technical Structure     | BTC     | price             | OK      | 79.123 $          | 79.123 $        | +0,0000%     |
| Technical Structure     | SOL     | price             | OK      | 104,43 $          | 104,43 $        | +0,0000%     |
| Technical Structure     | DOGE    | price             | OK      | 0.09043 $         | 0.09043 $       | -0,0000%     |
| Classic Technical       | BTC     | price             | OK      | 79.123 $          | 79.123 $        | +0,0000%     |
| Classic Technical       | SOL     | price             | OK      | 104,43 $          | 104,43 $        | +0,0000%     |
| Classic Technical       | DOGE    | price             | OK      | 0.09043 $         | 0.09043 $       | -0,0000%     |
| Classic Visual          | BTC     | price             | OK      | 79.123 $          | 79.123 $        | +0,0000%     |
| Classic Visual          | SOL     | price             | OK      | 104,43 $          | 104,43 $        | +0,0000%     |
| Classic Visual          | DOGE    | price             | OK      | 0.09043 $         | 0.09043 $       | -0,0000%     |
| Exchange Microstructure | BTC     | price             | OK      | 79.123 $          | 79.100 $        | -0,0289%     |
| Exchange Microstructure | SOL     | price             | WARN    | 104,43 $          | 104,15 $        | -0,2643%     |
| Exchange Microstructure | DOGE    | price             | OK      | 0.09043 $         | 0.09035 $       | -0,0885%     |
| RSI top-cycle           | SOL     | current_price     | OK      | 104,43 $          | 104,43 $        | +0,0000%     |
| RSI top-cycle           | SOL     | current_price     | OK      | 104,43 $          | 104,43 $        | +0,0000%     |
| Frattale BTC/SOL        | SOL     | sol_current_price | OK      | 104,43 $          | 104,43 $        | +0,0000%     |
| Fractal path            | SOL     | current_price     | OK      | 104,43 $          | 104,43 $        | +0,0000%     |

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

Generato: 2026-09-09T08:30:34+00:00

- Modalità: **SOLO PAPER TRADING**
- Asset: **SOL spot**
- Leva: **nessuna (1x)**
- Capitale iniziale separato: **€40.000,00**
- Fonte mercato: **KUCOIN_PUBLIC_API**; nuove entrate: **CONSENTITE**

| Equity | Cash | SOL | Prezzo | Rendimento | Realizzato | Commissioni | Max DD | Operazioni |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €45.340,96 | €27.858,61 | 167.274366 | 104.5130 | +13.35% | €4.505,48 | €124,89 | 6.48% | 64 |

**Ultima decisione:** HOLD — Prezzo dentro la fascia neutrale.

Bande 4H: L2 97.2176 · L1 100.1227 · media 103.7541 · U1 107.3855 · U2 110.2906.

> Questo portafoglio non condivide capitale, posizioni o statistiche con il paper trading da €10.000.
<!-- SOL_SPOT_ADAPTIVE_END -->
