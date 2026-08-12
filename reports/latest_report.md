<!-- COMPACT_REPORT_HEADER_START -->
> **Vista compatta:** Decisione operativa, Global Confluence e cambiamenti giornalieri restano aperti. Tocca il titolo di una sezione per mostrare o nascondere i dettagli.  
> Tutte le tabelle e tutti i dati restano nel file: copiando il Markdown raw viene copiato tutto.
<!-- COMPACT_REPORT_HEADER_END -->

<!-- COMPACT_SECTION_START:decision -->
<details open>
<summary><strong>🧭 Decisione operativa — da leggere per prima</strong></summary>

<!-- DECISION_REPORT_START -->

# Decisione operativa sintetica

Generato: 2026-08-11 05:23 UTC

Report separato completo: [decision_report.md](decision_report.md)

Sintesi automatica dello scanner: l'azione spot viene copiata direttamente dal Global Confluence; long, short e rischio restano filtri separati e più prudenti.

| Asset | Global | Direzione | Spot | Long leva | Short leva | Max long | Max short | Rischio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +6 | BULLISH | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE | NO LONG A LEVA / ATTENDI SOPRA 67.248 $ | NO SHORT | nessuna | nessuna | MEDIO |
| SOL | +4 | NEUTRALE / COSTRUTTIVO | HOLD / TRANCHE PICCOLE, NO LEVA | NO LONG A LEVA | NO SHORT | nessuna | nessuna | MOLTO ALTO |
| DOGE | +4 | NEUTRALE / COSTRUTTIVO | SOLO TRANCHE PICCOLE / NO LEVA | NO LONG A LEVA | NO SHORT | nessuna | nessuna | MOLTO ALTO |

## Lettura immediata

- **BTC**: Global = **+6**, spot = **ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE**, long = **NO LONG A LEVA / ATTENDI SOPRA 67.248 $**, short = **NO SHORT**, rischio = **MEDIO**.
- **SOL**: Global = **+4**, spot = **HOLD / TRANCHE PICCOLE, NO LEVA**, long = **NO LONG A LEVA**, short = **NO SHORT**, rischio = **MOLTO ALTO**.
- **DOGE**: Global = **+4**, spot = **SOLO TRANCHE PICCOLE / NO LEVA**, long = **NO LONG A LEVA**, short = **NO SHORT**, rischio = **MOLTO ALTO**.

## Dettaglio logica

### BTC

- Global Confluence: **+6**
- Confluenza: **MODERATAMENTE POSITIVA**
- Bias Global: **Costruttivo prudente**
- Direzione decisionale: **BULLISH**
- Azione spot dal Global: **ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE**
- Long leva: **NO LONG A LEVA / ATTENDI SOPRA 67.248 $**
- Short leva: **NO SHORT**
- Rischio: **MEDIO**
- Conferme: Prima resistenza sopra 66.910; conferma del doppio minimo sopra 66.910.
- Invalidazioni: Sotto 62.227 il quadro tecnico peggiora.

### SOL

- Global Confluence: **+4**
- Confluenza: **MODERATAMENTE POSITIVA**
- Bias Global: **Costruttivo prudente**
- Direzione decisionale: **NEUTRALE / COSTRUTTIVO**
- Azione spot dal Global: **HOLD / TRANCHE PICCOLE, NO LEVA**
- Long leva: **NO LONG A LEVA**
- Short leva: **NO SHORT**
- Rischio: **MOLTO ALTO**
- Conferme: conferma del doppio minimo sopra 83,81; nuova conferma tecnica sopra 78,73; milestone analogiche 79,78 / 93,47, valide soltanto se rientra anche il gap frattale.
- Invalidazioni: Allarmi sotto 71,42 / 70,69 / 62,19.

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
- **Lifecycle EMA200** = per SOL resta solo contesto, peso Global 0; score interno 4; EMA200 circa 111,66 $; upside verso EMA200 +47,36%. Non autorizza leva e non aggiunge punti automatici.
- **NO LONG** non significa automaticamente **SHORT**. Lo short ha senso solo se il quadro è bearish o se lo spike viene spesso scaricato.
- Per SOL, se il Global è da **+3 in su**, la decisione non deve diventare bearish solo perché lo scanner grezzo a 30 giorni è incerto.

<!-- DECISION_REPORT_END -->

<!-- PAPER_TRADING_START -->
# Paper trading automatico KuCoin

Generato: 2026-08-11T05:23:09+00:00


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [paper_trading_report.md](paper_trading_report.md)

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-08-11T05:08:36+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-08-11T05:08:36+00:00 | 2026-08-11T05:08:36+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-08-11T04:45:00+00:00 | 2026-08-11T04:45:00+00:00 | 8,9 min | 25,0 min | OK |
| 60m | 12 | 2026-08-11T04:00:00+00:00 | 2026-08-11T04:00:00+00:00 | 8,9 min | 45,0 min | OK |
| 240m | 12 | 2026-08-11T00:00:00+00:00 | 2026-08-11T00:00:00+00:00 | 1,15 h | 1,00 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Master Adaptive Strict3 V1 | SPCX | 60m | LONG | 5,89 | 0,00 | 0,00 | OPENED | 8,9 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Forza relativa 1H V2 | SPCX | 60m | LONG | 5,89 | 5,50 | 0,00 | OPENED | 8,9 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Bilanciata 1H V2 | SPCX | 60m | LONG | 5,89 | 5,50 | 0,00 | OPENED | 8,9 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Balanced Long No Rhv V1 | SPCX | 60m | LONG | 5,89 | 5,00 | 0,00 | OPENED | 8,9 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Principale 4H | BEAT | 240m | SHORT | -9,75 | 6,00 | 0,00 | STALE_CANDLE | 1,15 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.9 minuti; tolleranza 60 minuti. |
| Principale 4H | SPCX | 240m | LONG | 7,75 | 6,00 | 0,00 | STALE_CANDLE | 1,15 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.9 minuti; tolleranza 60 minuti. |
| Principale 4H | CYS | 240m | LONG | 6,25 | 6,00 | 0,00 | STALE_CANDLE | 1,15 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.9 minuti; tolleranza 60 minuti. |
| Principale 4H | XRP | 240m | SHORT | -6,20 | 6,00 | 0,00 | STALE_CANDLE | 1,15 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.9 minuti; tolleranza 60 minuti. |
| Principale 4H | DOGE | 240m | SHORT | -3,28 | 6,00 | 2,72 | STALE_CANDLE | 1,15 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.9 minuti; tolleranza 60 minuti. |
| Principale 4H | TUT | 240m | LONG | 2,75 | 6,00 | 3,25 | STALE_CANDLE | 1,15 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.9 minuti; tolleranza 60 minuti. |
| Principale 4H | BTC | 240m | SHORT | -1,75 | 6,00 | 4,25 | STALE_CANDLE | 1,15 h | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.9 minuti; tolleranza 60 minuti. |
| Principale 4H | ZEC | 240m | SHORT | -1,41 | 6,00 | 4,59 | STALE_CANDLE | 1,15 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.9 minuti; tolleranza 60 minuti. |
| Principale 4H | SOL | 240m | LONG | 1,12 | 6,00 | 4,88 | STALE_CANDLE | 1,15 h | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.9 minuti; tolleranza 60 minuti. |
| Principale 4H | ETH | 240m | SHORT | -0,94 | 6,00 | 5,06 | STALE_CANDLE | 1,15 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.9 minuti; tolleranza 60 minuti. |
| Principale 4H | HYPE | 240m | SHORT | -0,85 | 6,00 | 5,15 | STALE_CANDLE | 1,15 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.9 minuti; tolleranza 60 minuti. |
| Principale 4H | SOXL | 240m | SHORT | -0,25 | 6,00 | 5,75 | STALE_CANDLE | 1,15 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.9 minuti; tolleranza 60 minuti. |
| Benchmark trend following EMA 1H | HYPE | 60m | LONG | 6,61 | 5,00 | 0,00 | READY | 8,9 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Combo Trend | HYPE | 60m | LONG | 6,61 | 5,00 | 0,00 | READY | 8,9 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Combo Adaptive Side Regime Guard V1 | HYPE | 60m | LONG | 6,61 | 5,00 | 0,00 | READY | 8,9 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Bilanciata 1H V1 | BEAT | 60m | SHORT | -6,25 | 5,00 | 0,00 | READY | 8,9 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Bilanciata 1H V3 Filtered | BEAT | 60m | SHORT | -6,25 | 6,00 | 0,00 | READY | 8,9 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Rapida 1H V3 Filtered | BEAT | 60m | SHORT | -6,25 | 4,50 | 0,00 | READY | 8,9 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Fast V3 Cap75 V1 | BEAT | 60m | SHORT | -6,25 | 4,50 | 0,00 | READY | 8,9 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Fast V3 No Esports V1 | BEAT | 60m | SHORT | -6,25 | 4,50 | 0,00 | READY | 8,9 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.802,53 | -1,97% | €54,18 | €3.000,00 | 1,81% | 4 | 33 | 36,36% | 0,83 | 6,36% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 33 | 1041 | PRIME INDICAZIONI | 100 (mancano 67) |

- Trade del Principale 4H chiusi: **33**; win rate **36,36%**; profit factor **0,83**.
- Expectancy: **€-5,31** per trade; P&L netto: **€-175,07**; max drawdown: **6,36%**.
- Valutazione: **Si può osservare la direzione, ma il risultato resta fragile.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 4 | €9.802,53 | €1.619,55 | €4.858,66 | €194,15 | €-24,49 |
| TEST | Benchmark Donchian breakout 1H | 3 | €10.510,79 | €3.285,77 | €6.571,55 | €158,30 | €-48,02 |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | 3 | €10.461,10 | €2.794,65 | €8.383,96 | €157,41 | €-40,00 |
| TEST | 1H Fast Nohigh Cap75 V1 | 2 | €10.453,42 | €328,49 | €985,47 | €104,92 | €-38,09 |
| TEST | 1H Fast Score 6 75 V1 | 4 | €10.435,20 | €2.962,76 | €8.888,29 | €209,08 | €-45,02 |
| TEST | Bilanciata 1H V3 Filtered | 4 | €10.419,03 | €2.884,53 | €8.653,58 | €207,84 | €-15,81 |
| TEST | Scanner Top 5 Long 1H | 3 | €10.373,00 | €2.499,17 | €4.998,35 | €155,32 | €20,48 |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | 1 | €10.365,76 | €144,44 | €433,33 | €52,00 | €-33,87 |
| TEST | Bilanciata 1H V1 | 5 | €10.347,75 | €2.867,82 | €8.603,45 | €155,23 | €47,86 |
| TEST | Main Side Regime Guard V1 | 1 | €10.310,14 | €747,08 | €2.241,25 | €51,13 | €-5,84 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 0 | €10.300,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 0 | €10.271,73 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H V2 | 4 | €10.271,29 | €3.242,25 | €9.726,76 | €205,48 | €-1,67 |
| TEST | Donchian 1H Gb20 120R V1 | 3 | €10.263,33 | €3.208,41 | €6.416,83 | €154,57 | €-46,89 |
| TEST | 1H Fast V3 Nohigh Range Only V1 | 1 | €10.261,93 | €143,00 | €428,99 | €51,48 | €-33,53 |
| TEST | Combo Adaptive Side Regime Guard V1 | 4 | €10.257,93 | €5.318,44 | €10.636,89 | €205,70 | €-55,25 |
| TEST | Scanner Top 5 + forza BTC 1H | 3 | €10.241,48 | €2.467,49 | €4.934,97 | €153,35 | €20,23 |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 0 | €10.239,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 0 | €10.235,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Main Dynamic Asset Selector V1 | 0 | €10.230,30 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Cap75 V1 | 4 | €10.205,79 | €3.428,49 | €10.285,47 | €203,89 | €-5,25 |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | 2 | €10.193,29 | €320,32 | €960,95 | €102,31 | €-37,14 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 0 | €10.185,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Score 6 75 Range Only V1 | 1 | €10.184,54 | €141,92 | €425,75 | €51,09 | €-33,28 |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | 4 | €10.157,75 | €2.883,99 | €8.651,97 | €203,52 | €-43,82 |
| TEST | Combo Adaptive | 4 | €10.154,76 | €3.979,00 | €7.958,01 | €202,39 | €14,73 |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 0 | €10.145,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Donchian 1H | 0 | €10.113,92 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 1H | 0 | €10.110,96 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast No Pepe V1 | 4 | €10.107,15 | €2.240,68 | €6.722,04 | €202,31 | €-8,82 |
| TEST | Combo Adaptive Runner25 V1 | 5 | €10.103,12 | €2.735,23 | €5.470,46 | €153,63 | €98,53 |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 0 | €10.099,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 4H | 0 | €10.086,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 4H | 0 | €10.084,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | 0 | €10.075,90 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Ema 1H | 1 | €10.074,30 | €1.168,55 | €3.505,64 | €50,48 | €-19,83 |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 0 | €10.048,77 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V1 | 0 | €10.043,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Donchian 1H | 0 | €10.038,53 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Trend Side Regime Guard V1 | 4 | €10.035,65 | €6.026,02 | €12.052,04 | €200,51 | €-29,88 |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | 4 | €10.027,42 | €3.588,75 | €10.766,24 | €199,78 | €2,11 |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | 4 | €10.020,66 | €6.699,40 | €13.398,80 | €150,09 | €9,23 |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 0 | €10.008,92 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Profit Lock V1 | 4 | €10.005,42 | €6.689,21 | €13.378,42 | €149,86 | €9,21 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €10.003,85 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 0 | €10.003,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €50 · 15x | 0 | €10.001,42 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 0 | €10.000,77 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €10 · 15x | 0 | €10.000,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Continuation V1 | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · prudente · 5x | 0 | €9.999,47 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · prudente · 5x | 0 | €9.997,70 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €10 · 15x | 0 | €9.997,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 1H | 0 | €9.996,84 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €10 · 15x | 0 | €9.996,69 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | 0 | €9.996,45 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 0 | €9.995,23 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €10 · 15x | 0 | €9.994,44 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €10 · 15x | 0 | €9.989,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €50 · 15x | 0 | €9.988,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Donchian 4H | 0 | €9.985,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom10 Short | 4 | €9.983,90 | €6.681,70 | €13.363,40 | €149,69 | €0,20 |
| TEST | Scanner Bottom15 Short | 4 | €9.983,90 | €6.681,70 | €13.363,40 | €149,69 | €0,20 |
| TEST | Scanner Bottom20 Short | 4 | €9.983,90 | €6.681,70 | €13.363,40 | €149,69 | €0,20 |
| TEST | Scalp RSI Long 20 · €50 · 15x | 0 | €9.983,45 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 4H | 0 | €9.982,09 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · prudente · 5x | 0 | €9.980,94 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V2 | 0 | €9.974,21 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €50 · 15x | 0 | €9.972,22 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 1H | 0 | €9.970,30 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | 0 | €9.968,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V3 Filtered | 4 | €9.961,90 | €3.565,30 | €10.695,89 | €198,48 | €2,09 |
| TEST | Btc Adaptive 1H | 0 | €9.959,54 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Bollinger 1H | 0 | €9.959,49 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 0 | €9.953,21 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Long Only V1 | 3 | €9.952,78 | €2.422,29 | €4.844,57 | €148,96 | €23,83 |
| TEST | Btc Ema 4H | 0 | €9.950,68 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 4H | 0 | €9.949,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €50 · 15x | 0 | €9.945,22 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Balanced Short Trend Down Strict V1 | 0 | €9.943,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Ampia 4H | 5 | €9.936,50 | €1.922,32 | €3.844,65 | €98,60 | €74,60 |
| TEST | Scanner Bottom 5 Short 1H | 4 | €9.928,42 | €6.637,73 | €13.275,47 | €148,71 | €9,14 |
| TEST | 1H Fast V3 No Esports Long Only V1 | 3 | €9.927,94 | €2.066,85 | €6.200,54 | €148,63 | €6,84 |
| TEST | Forza relativa 1H V2 | 3 | €9.926,23 | €2.976,40 | €5.952,81 | €148,95 | €-4,43 |
| TEST | Scalp RSI Short 80 · prudente · 5x | 0 | €9.925,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | 0 | €9.923,70 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | 0 | €9.922,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.921,51 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Quality7 V1 | 1 | €9.914,48 | €207,25 | €414,51 | €49,74 | €-33,39 |
| TEST | Combo Adaptive Tp3 V1 | 5 | €9.914,38 | €2.684,13 | €5.368,26 | €150,76 | €96,69 |
| TEST | Combo Adaptive Regime V1 | 0 | €9.903,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Bollinger 1H | 0 | €9.902,02 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 4H | 0 | €9.898,26 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Tp2 V1 | 4 | €9.897,68 | €2.194,24 | €6.582,72 | €198,12 | €-8,64 |
| TEST | Eth Ema 4H | 0 | €9.894,27 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Donchian 1H | 0 | €9.871,99 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 1H | 0 | €9.867,86 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Tp3 V1 | 3 | €9.859,98 | €2.375,57 | €4.751,14 | €147,64 | €19,47 |
| TEST | Btc Ema 1H | 1 | €9.858,94 | €1.141,05 | €3.423,15 | €49,29 | €2,32 |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | 0 | €9.857,49 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Balanced V3 Long Only V1 | 4 | €9.854,74 | €2.728,30 | €8.184,91 | €196,58 | €-14,96 |
| TEST | Scanner Top5 Btc Runner25 V1 | 3 | €9.854,21 | €2.374,18 | €4.748,36 | €147,55 | €19,46 |
| TEST | Sol Ema 4H | 0 | €9.845,78 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Mean Reversion | 1 | €9.840,12 | €1.759,32 | €3.518,64 | €49,16 | €9,67 |
| TEST | 1H Fast V3 Nohigh V1 | 1 | €9.838,04 | €137,09 | €411,27 | €49,35 | €-32,15 |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 0 | €9.837,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | 3 | €9.824,22 | €2.366,96 | €4.733,91 | €147,10 | €19,40 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 0 | €9.817,34 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Gb20 Be V1 | 3 | €9.810,16 | €2.775,65 | €5.551,31 | €147,03 | €10,32 |
| TEST | Master Adaptive Expanded V1 | 3 | €9.806,06 | €2.774,49 | €5.548,99 | €146,97 | €10,31 |
| TEST | Master Adaptive Gb20 Partial V1 | 3 | €9.799,73 | €2.772,70 | €5.545,40 | €146,87 | €10,31 |
| TEST | Eth Adaptive 1H | 0 | €9.799,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Quality7 Regime V1 | 0 | €9.797,24 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Btc Le3 V1 | 3 | €9.786,76 | €2.357,93 | €4.715,86 | €146,54 | €19,33 |
| TEST | Sol Adaptive 1H | 0 | €9.781,19 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Runner25 V1 | 3 | €9.778,65 | €2.766,74 | €5.533,48 | €146,56 | €10,28 |
| TEST | Master Adaptive No Alt V1 | 3 | €9.765,85 | €2.763,12 | €5.526,23 | €146,37 | €10,27 |
| TEST | Global Confluence puro 1H | 1 | €9.765,36 | €1.528,83 | €3.057,65 | €48,92 | €-17,30 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 0 | €9.762,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Benchmark Bollinger mean reversion 1H | 1 | €9.761,96 | €1.952,30 | €3.904,60 | €46,86 | €2,81 |
| TEST | Master Adaptive V1 | 3 | €9.761,82 | €2.761,98 | €5.523,95 | €146,31 | €10,27 |
| TEST | 1H Fast V3 No Esports V1 | 4 | €9.759,12 | €3.492,72 | €10.478,17 | €194,44 | €2,05 |
| TEST | Combo Adaptive Partial 1R V1 | 4 | €9.751,06 | €3.820,82 | €7.641,64 | €194,35 | €14,15 |
| TEST | Eth Ema 1H | 0 | €9.727,87 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 0 | €9.723,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Benchmark trend following EMA 1H | 4 | €9.713,67 | €5.214,25 | €10.428,49 | €194,31 | €11,47 |
| TEST | Scanner Top5 Btc Guard V1 | 3 | €9.705,00 | €2.338,23 | €4.676,46 | €145,32 | €19,17 |
| TEST | Combo Scanner | 4 | €9.697,14 | €4.007,41 | €8.014,82 | €193,43 | €8,95 |
| TEST | Master Adaptive Gb20 Loss Cap V1 | 3 | €9.687,71 | €3.456,41 | €6.912,81 | €140,82 | €12,79 |
| TEST | Forza relativa 1H V1 | 4 | €9.663,22 | €2.526,29 | €5.052,59 | €192,86 | €-6,55 |
| TEST | 1H Balanced Long No Rhv V1 | 3 | €9.656,65 | €1.886,59 | €5.659,76 | €144,85 | €3,30 |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | 3 | €9.655,66 | €2.326,35 | €4.652,69 | €144,58 | €19,07 |
| TEST | Master Adaptive Gb20 V1 | 3 | €9.632,12 | €2.725,28 | €5.450,56 | €144,36 | €10,13 |
| TEST | Scanner Top5 Btc Mfe V1 | 3 | €9.599,91 | €2.312,91 | €4.625,82 | €143,74 | €18,96 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 0 | €9.579,83 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top10 Long | 3 | €9.554,34 | €2.301,93 | €4.603,87 | €143,06 | €18,87 |
| TEST | Scanner Top15 Long | 3 | €9.554,34 | €2.301,93 | €4.603,87 | €143,06 | €18,87 |
| TEST | Scanner Top20 Long | 3 | €9.554,34 | €2.301,93 | €4.603,87 | €143,06 | €18,87 |
| TEST | Combo Trend | 5 | €9.524,56 | €3.845,62 | €7.691,23 | €190,81 | €-42,15 |
| TEST | Scanner Top5 Btc Guard Mfe V1 | 3 | €9.479,29 | €2.283,85 | €4.567,70 | €141,94 | €18,72 |
| TEST | 1H Fast V3 Long Only V1 | 3 | €9.452,48 | €1.967,86 | €5.903,59 | €141,51 | €6,51 |
| TEST | Master Adaptive Strict3 V1 | 3 | €9.397,49 | €2.817,86 | €5.635,72 | €141,02 | €-4,19 |
| TEST | Combo Adaptive Mfe Trail | 4 | €9.371,26 | €3.672,00 | €7.344,00 | €186,78 | €13,59 |

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
| PRINCIPALE | Principale 4H | Confluenza trend | €9.802,53 | €-175,07 | 33 | 33 | 36,36% | 0,83 | €-5,31 | 6,36% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €10.510,79 | €562,76 | 40 | 40 | 52,50% | 1,62 | €14,07 | 3,09% |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | Momentum / breakout | €10.461,10 | €506,14 | 36 | 36 | 52,78% | 1,93 | €14,06 | 1,96% |
| TEST | 1H Fast Nohigh Cap75 V1 | Momentum / breakout | €10.453,42 | €492,11 | 64 | 64 | 46,88% | 1,41 | €7,69 | 2,83% |
| TEST | 1H Fast Score 6 75 V1 | Momentum / breakout | €10.435,20 | €485,55 | 75 | 75 | 44,00% | 1,37 | €6,47 | 2,49% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €10.419,03 | €440,04 | 66 | 66 | 39,39% | 1,33 | €6,67 | 2,82% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.373,00 | €355,52 | 50 | 50 | 44,00% | 1,30 | €7,11 | 5,09% |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | Momentum / breakout V3 Filtered | €10.365,76 | €399,89 | 20 | 20 | 65,00% | 3,42 | €19,99 | 1,39% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €10.347,75 | €305,06 | 75 | 75 | 45,33% | 1,24 | €4,07 | 3,56% |
| TEST | Main Side Regime Guard V1 | Confluenza trend | €10.310,14 | €317,32 | 18 | 18 | 50,00% | 1,84 | €17,63 | 2,40% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | Momentum / breakout V3 Filtered | €10.300,05 | €300,05 | 33 | 33 | 48,48% | 2,04 | €9,09 | 2,01% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | Momentum / breakout V3 Filtered | €10.271,73 | €271,73 | 22 | 22 | 50,00% | 1,74 | €12,35 | 1,72% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €10.271,29 | €278,80 | 41 | 39 | 51,22% | 1,36 | €6,80 | 2,75% |
| TEST | Donchian 1H Gb20 120R V1 | Donchian breakout 20 barre | €10.263,33 | €314,07 | 8 | 8 | 62,50% | 6,29 | €39,26 | 1,61% |
| TEST | 1H Fast V3 Nohigh Range Only V1 | Momentum / breakout V3 Filtered | €10.261,93 | €295,72 | 12 | 12 | 58,33% | 2,80 | €24,64 | 1,78% |
| TEST | Combo Adaptive Side Regime Guard V1 | Combo Adaptive | €10.257,93 | €319,56 | 35 | 35 | 54,29% | 1,76 | €9,13 | 1,58% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €10.241,48 | €224,22 | 41 | 41 | 39,02% | 1,25 | €5,47 | 4,25% |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | Momentum / breakout V3 Filtered | €10.239,20 | €239,20 | 17 | 17 | 52,94% | 4,50 | €14,07 | 1,01% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | Momentum / breakout V3 Filtered | €10.235,18 | €235,18 | 20 | 20 | 50,00% | 1,90 | €11,76 | 2,73% |
| TEST | Main Dynamic Asset Selector V1 | Confluenza trend | €10.230,30 | €230,30 | 11 | 11 | 45,45% | 1,85 | €20,94 | 1,50% |
| TEST | 1H Fast V3 Cap75 V1 | Momentum / breakout V3 Filtered | €10.205,79 | €217,21 | 68 | 68 | 44,12% | 1,16 | €3,19 | 4,04% |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | Momentum / breakout | €10.193,29 | €231,01 | 28 | 28 | 46,43% | 1,69 | €8,25 | 1,76% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | Momentum / breakout V3 Filtered | €10.185,37 | €185,37 | 22 | 22 | 40,91% | 1,57 | €8,43 | 2,27% |
| TEST | 1H Fast Score 6 75 Range Only V1 | Momentum / breakout | €10.184,54 | €218,07 | 13 | 13 | 53,85% | 1,74 | €16,77 | 2,28% |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | Momentum / breakout | €10.157,75 | €206,76 | 33 | 33 | 51,52% | 1,32 | €6,27 | 3,20% |
| TEST | Combo Adaptive | Combo Adaptive | €10.154,76 | €144,81 | 42 | 42 | 42,86% | 1,24 | €3,45 | 3,05% |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | Momentum / breakout V3 Filtered | €10.145,12 | €145,12 | 44 | 44 | 45,45% | 1,20 | €3,30 | 2,91% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €10.113,92 | €113,92 | 4 | 4 | 75,00% | 26,39 | €28,48 | 0,79% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.110,96 | €110,96 | 4 | 4 | 75,00% | 2,94 | €27,74 | 0,70% |
| TEST | 1H Fast No Pepe V1 | Momentum / breakout | €10.107,15 | €120,01 | 73 | 73 | 43,84% | 1,09 | €1,64 | 2,79% |
| TEST | Combo Adaptive Runner25 V1 | Combo Adaptive | €10.103,12 | €7,88 | 44 | 44 | 36,36% | 1,01 | €0,18 | 2,31% |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | Momentum / breakout V3 Filtered | €10.099,04 | €99,04 | 55 | 55 | 54,55% | 1,12 | €1,80 | 3,59% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €10.086,98 | €86,98 | 1 | 1 | 100,00% | ∞ | €86,98 | 0,40% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.084,12 | €84,12 | 1 | 1 | 100,00% | ∞ | €84,12 | 0,30% |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | Momentum / breakout V3 Filtered | €10.075,90 | €75,90 | 20 | 20 | 45,00% | 1,17 | €3,80 | 2,17% |
| TEST | Doge Ema 1H | Trend following EMA | €10.074,30 | €96,23 | 10 | 10 | 70,00% | 1,57 | €9,62 | 1,36% |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | Momentum / breakout V3 Filtered | €10.048,77 | €48,77 | 23 | 23 | 43,48% | 1,12 | €2,12 | 3,05% |
| TEST | Rapida 1H V1 | Momentum / breakout | €10.043,28 | €43,28 | 78 | 78 | 34,62% | 1,02 | €0,55 | 6,76% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €10.038,53 | €38,53 | 6 | 6 | 66,67% | 1,34 | €6,42 | 1,08% |
| TEST | Combo Trend Side Regime Guard V1 | Combo Trend | €10.035,65 | €72,76 | 32 | 32 | 50,00% | 1,14 | €2,27 | 2,89% |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | Momentum / breakout V3 Filtered | €10.027,42 | €31,78 | 60 | 60 | 50,00% | 1,03 | €0,53 | 4,01% |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | Scanner Bottom 5 Short | €10.020,66 | €19,47 | 21 | 21 | 42,86% | 1,06 | €0,93 | 1,38% |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | Momentum / breakout V3 Filtered | €10.008,92 | €8,92 | 30 | 30 | 36,67% | 1,02 | €0,30 | 4,84% |
| TEST | Scanner Bottom5 Short Profit Lock V1 | Scanner Bottom 5 Short | €10.005,42 | €4,23 | 22 | 22 | 40,91% | 1,01 | €0,19 | 1,53% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €10.003,85 | €3,85 | 23 | 23 | 43,48% | 1,04 | €0,17 | 0,33% |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | Momentum / breakout V3 Filtered | €10.003,37 | €3,37 | 8 | 8 | 37,50% | 1,02 | €0,42 | 2,15% |
| TEST | Scalp RSI Short 85 · €50 · 15x | Inversione RSI estrema 15m | €10.001,42 | €1,42 | 3 | 3 | 66,67% | 2,74 | €0,47 | 0,08% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €10.000,77 | €0,77 | 23 | 23 | 43,48% | 1,04 | €0,03 | 0,07% |
| TEST | Scalp RSI Short 85 · €10 · 15x | Inversione RSI estrema 15m | €10.000,28 | €0,28 | 3 | 3 | 66,67% | 2,74 | €0,09 | 0,02% |
| TEST | Scanner Bottom5 Short Continuation V1 | Scanner Bottom5 Short Continuation | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 85 · prudente · 5x | Inversione RSI estrema 15m | €9.999,47 | €-0,53 | 3 | 3 | 66,67% | 0,77 | €-0,18 | 0,16% |
| TEST | Scalp RSI Long 20 · prudente · 5x | Inversione RSI estrema 15m | €9.997,70 | €-2,30 | 7 | 7 | 42,86% | 0,94 | €-0,33 | 0,36% |
| TEST | Scalp RSI Long 15 · €10 · 15x | Inversione RSI estrema 15m | €9.997,60 | €-2,40 | 3 | 3 | 33,33% | 0,13 | €-0,80 | 0,02% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €9.996,84 | €-3,16 | 5 | 5 | 60,00% | 0,97 | €-0,63 | 1,49% |
| TEST | Scalp RSI Long 20 · €10 · 15x | Inversione RSI estrema 15m | €9.996,69 | €-3,31 | 7 | 7 | 28,57% | 0,24 | €-0,47 | 0,04% |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | Momentum / breakout | €9.996,45 | €-3,55 | 25 | 25 | 36,00% | 0,99 | €-0,14 | 2,27% |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | Momentum / breakout V3 Filtered | €9.995,23 | €-4,77 | 15 | 15 | 46,67% | 0,99 | €-0,32 | 2,70% |
| TEST | Scalp RSI Short 80 · €10 · 15x | Inversione RSI estrema 15m | €9.994,44 | €-5,56 | 11 | 11 | 27,27% | 0,38 | €-0,51 | 0,11% |
| TEST | Scalp RSI Long 25 · €10 · 15x | Inversione RSI estrema 15m | €9.989,04 | €-10,96 | 13 | 13 | 30,77% | 0,26 | €-0,84 | 0,14% |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | €9.988,00 | €-12,00 | 3 | 3 | 33,33% | 0,13 | €-4,00 | 0,12% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €9.985,00 | €-15,00 | 2 | 2 | 50,00% | 0,71 | €-7,50 | 0,79% |
| TEST | Scanner Bottom10 Short | Scanner Bottom10 Short | €9.983,90 | €-8,28 | 27 | 27 | 40,74% | 0,98 | €-0,31 | 2,72% |
| TEST | Scanner Bottom15 Short | Scanner Bottom15 Short | €9.983,90 | €-8,28 | 27 | 27 | 40,74% | 0,98 | €-0,31 | 2,72% |
| TEST | Scanner Bottom20 Short | Scanner Bottom20 Short | €9.983,90 | €-8,28 | 27 | 27 | 40,74% | 0,98 | €-0,31 | 2,72% |
| TEST | Scalp RSI Long 20 · €50 · 15x | Inversione RSI estrema 15m | €9.983,45 | €-16,55 | 7 | 7 | 28,57% | 0,24 | €-2,36 | 0,19% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €9.982,09 | €-17,91 | 2 | 2 | 50,00% | 0,65 | €-8,96 | 0,77% |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | €9.980,94 | €-19,06 | 3 | 3 | 33,33% | 0,19 | €-6,35 | 0,20% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €9.974,21 | €-25,79 | 17 | 15 | 41,18% | 0,93 | €-1,52 | 1,69% |
| TEST | Scalp RSI Short 80 · €50 · 15x | Inversione RSI estrema 15m | €9.972,22 | €-27,78 | 11 | 11 | 27,27% | 0,38 | €-2,53 | 0,53% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.970,30 | €-29,70 | 5 | 5 | 40,00% | 0,82 | €-5,94 | 1,89% |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | Scanner Top 5 + forza BTC | €9.968,72 | €-31,28 | 10 | 10 | 30,00% | 0,87 | €-3,13 | 2,84% |
| TEST | Rapida 1H V3 Filtered | Momentum / breakout V3 Filtered | €9.961,90 | €-33,78 | 104 | 104 | 37,50% | 0,98 | €-0,32 | 3,98% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €9.959,54 | €-40,46 | 4 | 4 | 50,00% | 0,63 | €-10,11 | 0,89% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €9.959,49 | €-40,51 | 2 | 2 | 50,00% | 0,28 | €-20,26 | 0,91% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €9.953,21 | €-46,79 | 13 | 13 | 30,77% | 0,37 | €-3,60 | 0,71% |
| TEST | Combo Adaptive Long Only V1 | Combo Adaptive | €9.952,78 | €-68,14 | 20 | 20 | 25,00% | 0,81 | €-3,41 | 2,34% |
| TEST | Btc Ema 4H | Trend following EMA | €9.950,68 | €-49,32 | 1 | 1 | 0,00% | 0,00 | €-49,32 | 0,96% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €9.949,62 | €-50,38 | 1 | 1 | 0,00% | 0,00 | €-50,38 | 0,74% |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | €9.945,22 | €-54,78 | 13 | 13 | 30,77% | 0,26 | €-4,21 | 0,72% |
| TEST | 1H Balanced Short Trend Down Strict V1 | Confluenza trend | €9.943,38 | €-56,62 | 2 | 2 | 0,00% | 0,00 | €-28,31 | 1,11% |
| TEST | Ampia 4H | Confluenza trend | €9.936,50 | €-135,92 | 27 | 27 | 25,93% | 0,82 | €-5,03 | 4,21% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.928,42 | €-72,76 | 49 | 49 | 36,73% | 0,92 | €-1,48 | 5,48% |
| TEST | 1H Fast V3 No Esports Long Only V1 | Momentum / breakout V3 Filtered | €9.927,94 | €-75,18 | 36 | 36 | 38,89% | 0,90 | €-2,09 | 4,81% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €9.926,23 | €-65,77 | 55 | 54 | 38,18% | 0,96 | €-1,20 | 5,53% |
| TEST | Scalp RSI Short 80 · prudente · 5x | Inversione RSI estrema 15m | €9.925,12 | €-74,88 | 11 | 11 | 27,27% | 0,10 | €-6,81 | 0,89% |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | Momentum / breakout V3 Filtered | €9.923,70 | €-76,30 | 49 | 49 | 46,94% | 0,93 | €-1,56 | 3,21% |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | Combo Adaptive | €9.922,04 | €-77,96 | 11 | 11 | 45,45% | 0,71 | €-7,09 | 1,95% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.921,51 | €-78,49 | 23 | 23 | 43,48% | 0,39 | €-3,41 | 0,84% |
| TEST | Combo Adaptive Quality7 V1 | Combo Adaptive | €9.914,48 | €-51,88 | 27 | 27 | 33,33% | 0,88 | €-1,92 | 2,73% |
| TEST | Combo Adaptive Tp3 V1 | Combo Adaptive | €9.914,38 | €-179,09 | 25 | 25 | 36,00% | 0,61 | €-7,16 | 2,55% |
| TEST | Combo Adaptive Regime V1 | Combo Adaptive | €9.903,28 | €-96,72 | 22 | 22 | 45,45% | 0,79 | €-4,40 | 2,18% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €9.902,02 | €-97,98 | 4 | 4 | 25,00% | 0,41 | €-24,49 | 1,89% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €9.898,26 | €-101,74 | 2 | 2 | 0,00% | 0,00 | €-50,87 | 1,48% |
| TEST | 1H Fast Tp2 V1 | Momentum / breakout | €9.897,68 | €-89,74 | 80 | 80 | 35,00% | 0,94 | €-1,12 | 2,94% |
| TEST | Eth Ema 4H | Trend following EMA | €9.894,27 | €-105,73 | 2 | 2 | 0,00% | 0,00 | €-52,87 | 1,21% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.871,99 | €-128,01 | 5 | 5 | 20,00% | 0,42 | €-25,60 | 1,62% |
| TEST | Sol Ema 1H | Trend following EMA | €9.867,86 | €-132,14 | 7 | 7 | 28,57% | 0,52 | €-18,88 | 2,09% |
| TEST | Scanner Top5 Btc Tp3 V1 | Scanner Top 5 + forza BTC | €9.859,98 | €-156,64 | 26 | 26 | 30,77% | 0,80 | €-6,02 | 4,98% |
| TEST | Btc Ema 1H | Trend following EMA | €9.858,94 | €-141,33 | 7 | 7 | 28,57% | 0,48 | €-20,19 | 1,57% |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | Momentum / breakout V3 Filtered | €9.857,49 | €-142,51 | 44 | 44 | 40,91% | 0,86 | €-3,24 | 2,86% |
| TEST | 1H Balanced V3 Long Only V1 | Confluenza trend V3 Filtered | €9.854,74 | €-125,39 | 22 | 22 | 31,82% | 0,72 | €-5,70 | 2,51% |
| TEST | Scanner Top5 Btc Runner25 V1 | Scanner Top 5 + forza BTC | €9.854,21 | €-162,40 | 30 | 30 | 33,33% | 0,79 | €-5,41 | 5,29% |
| TEST | Sol Ema 4H | Trend following EMA | €9.845,78 | €-154,22 | 3 | 3 | 0,00% | 0,00 | €-51,41 | 1,57% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €9.840,12 | €-167,45 | 20 | 20 | 35,00% | 0,76 | €-8,37 | 3,63% |
| TEST | 1H Fast V3 Nohigh V1 | Momentum / breakout V3 Filtered | €9.838,04 | €-129,57 | 62 | 62 | 38,71% | 0,90 | €-2,09 | 2,96% |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | Momentum / breakout V3 Filtered | €9.837,38 | €-162,62 | 37 | 37 | 40,54% | 0,76 | €-4,40 | 3,08% |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | Scanner Top 5 + forza BTC | €9.824,22 | €-192,34 | 19 | 19 | 31,58% | 0,70 | €-10,12 | 4,66% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | Momentum / breakout V3 Filtered | €9.817,34 | €-182,66 | 24 | 24 | 41,67% | 0,64 | €-7,61 | 3,23% |
| TEST | Master Adaptive Gb20 Be V1 | Master Adaptive Consensus | €9.810,16 | €-196,83 | 22 | 22 | 18,18% | 0,66 | €-8,95 | 3,42% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €9.806,06 | €-200,92 | 22 | 22 | 31,82% | 0,74 | €-9,13 | 3,64% |
| TEST | Master Adaptive Gb20 Partial V1 | Master Adaptive Consensus | €9.799,73 | €-207,25 | 17 | 17 | 29,41% | 0,62 | €-12,19 | 2,99% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.799,60 | €-200,40 | 6 | 6 | 33,33% | 0,08 | €-33,40 | 2,09% |
| TEST | Combo Adaptive Quality7 Regime V1 | Combo Adaptive | €9.797,24 | €-202,76 | 11 | 11 | 27,27% | 0,31 | €-18,43 | 2,32% |
| TEST | Scanner Top5 Btc Btc Le3 V1 | Scanner Top 5 + forza BTC | €9.786,76 | €-229,74 | 22 | 22 | 31,82% | 0,64 | €-10,44 | 4,73% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €9.781,19 | €-218,81 | 7 | 7 | 28,57% | 0,24 | €-31,26 | 2,92% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €9.778,65 | €-228,32 | 21 | 21 | 28,57% | 0,68 | €-10,87 | 3,98% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €9.765,85 | €-241,11 | 19 | 19 | 26,32% | 0,66 | €-12,69 | 4,03% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.765,36 | €-215,51 | 13 | 13 | 30,77% | 0,44 | €-16,58 | 2,92% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | Momentum / breakout V3 Filtered | €9.762,18 | €-237,82 | 7 | 7 | 14,29% | 0,02 | €-33,97 | 2,82% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €9.761,96 | €-238,51 | 50 | 50 | 40,00% | 0,82 | €-4,77 | 5,70% |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | €9.761,82 | €-245,13 | 19 | 19 | 26,32% | 0,66 | €-12,90 | 4,07% |
| TEST | 1H Fast V3 No Esports V1 | Momentum / breakout V3 Filtered | €9.759,12 | €-236,64 | 78 | 78 | 37,18% | 0,85 | €-3,03 | 3,95% |
| TEST | Combo Adaptive Partial 1R V1 | Combo Adaptive | €9.751,06 | €-258,50 | 43 | 43 | 39,53% | 0,67 | €-6,01 | 3,97% |
| TEST | Eth Ema 1H | Trend following EMA | €9.727,87 | €-272,13 | 8 | 8 | 25,00% | 0,16 | €-34,02 | 2,76% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | Momentum / breakout V3 Filtered | €9.723,72 | €-276,28 | 31 | 31 | 32,26% | 0,62 | €-8,91 | 4,83% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.713,67 | €-291,54 | 46 | 46 | 30,43% | 0,71 | €-6,34 | 3,97% |
| TEST | Scanner Top5 Btc Guard V1 | Scanner Top 5 + forza BTC | €9.705,00 | €-311,36 | 24 | 24 | 25,00% | 0,59 | €-12,97 | 4,25% |
| TEST | Combo Scanner | Combo Scanner | €9.697,14 | €-307,00 | 50 | 50 | 36,00% | 0,77 | €-6,14 | 5,37% |
| TEST | Master Adaptive Gb20 Loss Cap V1 | Master Adaptive Consensus | €9.687,71 | €-320,93 | 19 | 19 | 21,05% | 0,55 | €-16,89 | 4,72% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €9.663,22 | €-327,20 | 54 | 54 | 27,78% | 0,75 | €-6,06 | 7,55% |
| TEST | 1H Balanced Long No Rhv V1 | Confluenza trend | €9.656,65 | €-343,26 | 20 | 20 | 25,00% | 0,47 | €-17,16 | 4,33% |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | Scanner Top 5 + forza BTC | €9.655,66 | €-360,61 | 34 | 34 | 35,29% | 0,61 | €-10,61 | 3,93% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €9.632,12 | €-374,74 | 54 | 54 | 55,56% | 0,59 | €-6,94 | 4,27% |
| TEST | Scanner Top5 Btc Mfe V1 | Scanner Top 5 + forza BTC | €9.599,91 | €-416,27 | 34 | 34 | 32,35% | 0,46 | €-12,24 | 5,33% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | Momentum / breakout V3 Filtered | €9.579,83 | €-420,17 | 11 | 11 | 0,00% | 0,00 | €-38,20 | 4,20% |
| TEST | Scanner Top10 Long | Scanner Top10 Long | €9.554,34 | €-461,76 | 22 | 22 | 27,27% | 0,34 | €-20,99 | 6,61% |
| TEST | Scanner Top15 Long | Scanner Top15 Long | €9.554,34 | €-461,76 | 22 | 22 | 27,27% | 0,34 | €-20,99 | 6,61% |
| TEST | Scanner Top20 Long | Scanner Top20 Long | €9.554,34 | €-461,76 | 22 | 22 | 27,27% | 0,34 | €-20,99 | 6,61% |
| TEST | Combo Trend | Combo Trend | €9.524,56 | €-428,67 | 64 | 64 | 31,25% | 0,77 | €-6,70 | 7,64% |
| TEST | Scanner Top5 Btc Guard Mfe V1 | Scanner Top 5 + forza BTC | €9.479,29 | €-536,69 | 41 | 41 | 34,15% | 0,53 | €-13,09 | 5,73% |
| TEST | 1H Fast V3 Long Only V1 | Momentum / breakout V3 Filtered | €9.452,48 | €-550,49 | 56 | 56 | 28,57% | 0,62 | €-9,83 | 6,86% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €9.397,49 | €-594,93 | 27 | 27 | 22,22% | 0,49 | €-22,03 | 6,23% |
| TEST | Combo Adaptive Mfe Trail | Combo Adaptive | €9.371,26 | €-637,93 | 52 | 52 | 28,85% | 0,48 | €-12,27 | 7,57% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | DOGE | SHORT | Confluenza trend | 240m | 3,0x | 0,07019 | 0,07003 | 0,07248 | 0,09323 | 0,06560 | €485,79 | €1.457,36 | €47,61 | €3,24 |
| Principale 4H | XRP | SHORT | Confluenza trend | 240m | 3,0x | 1,01047 | 1,01310 | 1,03352 | 1,34224 | 0,96437 | €711,84 | €2.135,52 | €48,72 | €-5,56 |
| Principale 4H | SPCX | LONG | Confluenza trend | 240m | 3,0x | 136,56189 | 137,17000 | 128,79610 | 91,72407 | 152,09346 | €285,50 | €856,50 | €48,71 | €3,81 |
| Principale 4H | BEAT | SHORT | Confluenza trend | 240m | 3,0x | 1,31391 | 1,39730 | 1,47158 | 1,74531 | 0,99857 | €136,42 | €409,27 | €49,11 | €-25,98 |
| Bilanciata 1H V1 | SPCX | LONG | Confluenza trend | 60m | 3,0x | 136,85206 | 137,17000 | 132,31345 | 91,91897 | 145,92928 | €517,88 | €1.553,64 | €51,53 | €3,61 |
| Bilanciata 1H V1 | HYPE | LONG | Confluenza trend | 60m | 3,0x | 55,32406 | 55,42000 | 54,37122 | 37,15933 | 57,22974 | €997,04 | €2.991,13 | €51,52 | €5,19 |
| Bilanciata 1H V1 | XRP | SHORT | Confluenza trend | 60m | 3,0x | 1,02104 | 1,01310 | 1,01832 | 1,35628 | 0,99163 | €1.192,22 | €3.576,67 | €0,00 | €27,80 |
| Bilanciata 1H V1 | CYS | LONG | Confluenza trend | 60m | 3,0x | 1,28356 | 1,31820 | 1,12953 | 0,86212 | 1,59161 | €142,82 | €428,45 | €51,41 | €11,56 |
| Bilanciata 1H V1 | DOGE | SHORT | Confluenza trend | 60m | 3,0x | 0,06964 | 0,07003 | 0,07064 | 0,09250 | 0,06763 | €17,86 | €53,57 | €0,77 | €-0,30 |
| 1H Balanced Long No Rhv V1 | HYPE | LONG | Confluenza trend | 60m | 3,0x | 55,29106 | 55,42000 | 54,45225 | 37,13716 | 56,96867 | €1.060,90 | €3.182,69 | €48,28 | €7,42 |
| 1H Balanced Long No Rhv V1 | CYS | LONG | Confluenza trend | 60m | 3,0x | 1,32770 | 1,31820 | 1,16837 | 0,89177 | 1,64634 | €134,09 | €402,26 | €48,27 | €-2,88 |
| 1H Balanced Long No Rhv V1 | SPCX | LONG | Confluenza trend | 60m | 3,0x | 137,25230 | 137,17000 | 134,05746 | 92,18780 | 143,64199 | €691,60 | €2.074,81 | €48,30 | €-1,24 |
| Bilanciata 1H V2 | XRP | SHORT | Confluenza trend V2 | 60m | 3,0x | 1,01393 | 1,01310 | 1,02853 | 1,34683 | 0,98473 | €1.189,68 | €3.569,03 | €51,39 | €2,91 |
| Bilanciata 1H V2 | CYS | LONG | Confluenza trend V2 | 60m | 3,0x | 1,32770 | 1,31820 | 1,16837 | 0,89177 | 1,64634 | €142,72 | €428,16 | €51,38 | €-3,06 |
| Bilanciata 1H V2 | HYPE | LONG | Confluenza trend V2 | 60m | 3,0x | 55,42308 | 55,42000 | 54,61538 | 37,22584 | 57,03848 | €1.174,31 | €3.522,93 | €51,34 | €-0,20 |
| Bilanciata 1H V2 | SPCX | LONG | Confluenza trend V2 | 60m | 3,0x | 137,25230 | 137,17000 | 134,05746 | 92,18780 | 143,64199 | €735,55 | €2.206,64 | €51,36 | €-1,32 |
| Bilanciata 1H V3 Filtered | SPCX | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 136,85206 | 137,17000 | 132,31345 | 91,91897 | 145,92928 | €524,66 | €1.573,99 | €52,20 | €3,66 |
| Bilanciata 1H V3 Filtered | HYPE | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 55,32406 | 55,42000 | 54,37122 | 37,15933 | 57,22974 | €1.010,10 | €3.030,31 | €52,19 | €5,25 |
| Bilanciata 1H V3 Filtered | DOGE | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,06964 | 0,07003 | 0,07064 | 0,09250 | 0,06763 | €1.207,28 | €3.621,85 | €52,15 | €-20,49 |
| Bilanciata 1H V3 Filtered | CYS | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1,33140 | 1,31820 | 1,17163 | 0,89426 | 1,65093 | €142,48 | €427,43 | €51,29 | €-4,24 |
| 1H Fast Score 6 75 V1 | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 55,32406 | 55,42000 | 54,58296 | 37,15933 | 56,43571 | €1.304,60 | €3.913,81 | €52,43 | €6,79 |
| 1H Fast Score 6 75 V1 | CYS | LONG | Momentum / breakout | 60m | 3,0x | 1,33140 | 1,31820 | 1,19968 | 0,89426 | 1,52898 | €175,99 | €527,96 | €52,23 | €-5,23 |
| 1H Fast Score 6 75 V1 | ZEC | SHORT | Momentum / breakout | 60m | 3,0x | 491,45169 | 493,00000 | 497,86052 | 652,81166 | 481,83845 | €1.337,47 | €4.012,40 | €52,32 | €-12,64 |
| 1H Fast Score 6 75 V1 | BEAT | SHORT | Momentum / breakout | 60m | 3,0x | 1,29600 | 1,39730 | 1,45152 | 1,72152 | 1,06272 | €144,71 | €434,12 | €52,09 | €-33,93 |
| 1H Fast Score 6 75 No Trend Up V1 | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 55,32406 | 55,42000 | 54,58296 | 37,15933 | 56,43571 | €1.269,92 | €3.809,75 | €51,03 | €6,61 |
| 1H Fast Score 6 75 No Trend Up V1 | CYS | LONG | Momentum / breakout | 60m | 3,0x | 1,33140 | 1,31820 | 1,19968 | 0,89426 | 1,52898 | €171,31 | €513,92 | €50,84 | €-5,09 |
| 1H Fast Score 6 75 No Trend Up V1 | ZEC | SHORT | Momentum / breakout | 60m | 3,0x | 491,45169 | 493,00000 | 497,86052 | 652,81166 | 481,83845 | €1.301,91 | €3.905,72 | €50,93 | €-12,30 |
| 1H Fast Score 6 75 No Trend Up V1 | BEAT | SHORT | Momentum / breakout | 60m | 3,0x | 1,29600 | 1,39730 | 1,45152 | 1,72152 | 1,06272 | €140,86 | €422,58 | €50,71 | €-33,03 |
| 1H Fast Score 6 75 Range Only V1 | BEAT | SHORT | Momentum / breakout | 60m | 3,0x | 1,29600 | 1,39730 | 1,45152 | 1,72152 | 1,06272 | €141,92 | €425,75 | €51,09 | €-33,28 |
| 1H Fast Score 6 75 Cost Aware V1 | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 55,32406 | 55,42000 | 54,58296 | 37,15933 | 56,43571 | €1.307,16 | €3.921,49 | €52,53 | €6,80 |
| 1H Fast Score 6 75 Cost Aware V1 | ZEC | SHORT | Momentum / breakout | 60m | 3,0x | 491,45169 | 493,00000 | 497,86052 | 652,81166 | 481,83845 | €1.341,98 | €4.025,95 | €52,50 | €-12,68 |
| 1H Fast Score 6 75 Cost Aware V1 | BEAT | SHORT | Momentum / breakout | 60m | 3,0x | 1,29600 | 1,39730 | 1,45152 | 1,72152 | 1,06272 | €145,51 | €436,52 | €52,38 | €-34,12 |
| 1H Fast Nohigh Cap75 V1 | BEAT | SHORT | Momentum / breakout | 60m | 3,0x | 1,29600 | 1,39730 | 1,45152 | 1,72152 | 1,06272 | €145,72 | €437,17 | €52,46 | €-34,17 |
| 1H Fast Nohigh Cap75 V1 | CYS | LONG | Momentum / breakout | 60m | 3,0x | 1,32770 | 1,31820 | 1,20067 | 0,89177 | 1,51824 | €182,77 | €548,30 | €52,46 | €-3,92 |
| 1H Fast No Pepe V1 | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 55,32406 | 55,42000 | 54,58296 | 37,15933 | 56,43571 | €1.267,13 | €3.801,40 | €50,92 | €6,59 |
| 1H Fast No Pepe V1 | CYS | LONG | Momentum / breakout | 60m | 3,0x | 1,28356 | 1,31820 | 1,14107 | 0,86212 | 1,49729 | €152,86 | €458,58 | €50,91 | €12,38 |
| 1H Fast No Pepe V1 | SPCX | LONG | Momentum / breakout | 60m | 3,0x | 136,80203 | 137,17000 | 133,40452 | 91,88536 | 141,89830 | €682,89 | €2.048,66 | €50,88 | €5,51 |
| 1H Fast No Pepe V1 | BEAT | SHORT | Momentum / breakout | 60m | 3,0x | 1,29313 | 1,39730 | 1,44831 | 1,71771 | 1,06037 | €137,80 | €413,39 | €49,61 | €-33,30 |
| 1H Fast Tp2 V1 | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 55,32406 | 55,42000 | 54,58296 | 37,15933 | 56,80626 | €1.240,87 | €3.722,61 | €49,87 | €6,46 |
| 1H Fast Tp2 V1 | CYS | LONG | Momentum / breakout | 60m | 3,0x | 1,28356 | 1,31820 | 1,14107 | 0,86212 | 1,56853 | €149,69 | €449,08 | €49,85 | €12,12 |
| 1H Fast Tp2 V1 | SPCX | LONG | Momentum / breakout | 60m | 3,0x | 136,80203 | 137,17000 | 133,40452 | 91,88536 | 143,59705 | €668,73 | €2.006,20 | €49,82 | €5,40 |
| 1H Fast Tp2 V1 | BEAT | SHORT | Momentum / breakout | 60m | 3,0x | 1,29313 | 1,39730 | 1,44831 | 1,71771 | 0,98278 | €134,94 | €404,82 | €48,58 | €-32,61 |
| Rapida 1H V3 Filtered | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 55,32406 | 55,42000 | 54,58296 | 37,15933 | 56,43571 | €1.247,94 | €3.743,81 | €50,15 | €6,49 |
| Rapida 1H V3 Filtered | SPCX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 136,80203 | 137,17000 | 133,40452 | 91,88536 | 141,89830 | €672,56 | €2.017,68 | €50,11 | €5,43 |
| Rapida 1H V3 Filtered | XRP | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,01197 | 1,01310 | 1,02330 | 1,34423 | 0,99497 | €1.481,61 | €4.444,83 | €49,78 | €-4,97 |
| Rapida 1H V3 Filtered | CYS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,33140 | 1,31820 | 1,19968 | 0,89426 | 1,52898 | €163,19 | €489,56 | €48,43 | €-4,85 |
| 1H Fast V3 Cap75 V1 | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 55,32406 | 55,42000 | 54,58296 | 37,15933 | 56,43571 | €1.271,22 | €3.813,65 | €51,09 | €6,61 |
| 1H Fast V3 Cap75 V1 | SPCX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 136,80203 | 137,17000 | 133,40452 | 91,88536 | 141,89830 | €685,11 | €2.055,32 | €51,04 | €5,53 |
| 1H Fast V3 Cap75 V1 | CYS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,33140 | 1,31820 | 1,19968 | 0,89426 | 1,52898 | €171,42 | €514,25 | €50,88 | €-5,10 |
| 1H Fast V3 Cap75 V1 | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 491,45169 | 493,00000 | 497,86052 | 652,81166 | 481,83845 | €1.300,75 | €3.902,26 | €50,89 | €-12,29 |
| 1H Fast V3 Nohigh V1 | BEAT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,29600 | 1,39730 | 1,45152 | 1,72152 | 1,06272 | €137,09 | €411,27 | €49,35 | €-32,15 |
| 1H Fast V3 Long Only V1 | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 55,32406 | 55,42000 | 54,58296 | 37,15933 | 56,43571 | €1.175,70 | €3.527,10 | €47,25 | €6,12 |
| 1H Fast V3 Long Only V1 | SPCX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 136,80203 | 137,17000 | 133,40452 | 91,88536 | 141,89830 | €633,63 | €1.900,88 | €47,21 | €5,11 |
| 1H Fast V3 Long Only V1 | CYS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,33140 | 1,31820 | 1,19968 | 0,89426 | 1,52898 | €158,54 | €475,61 | €47,05 | €-4,71 |
| 1H Fast V3 No Esports V1 | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 55,32406 | 55,42000 | 54,58296 | 37,15933 | 56,43571 | €1.222,54 | €3.667,61 | €49,13 | €6,36 |
| 1H Fast V3 No Esports V1 | SPCX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 136,80203 | 137,17000 | 133,40452 | 91,88536 | 141,89830 | €658,87 | €1.976,61 | €49,09 | €5,32 |
| 1H Fast V3 No Esports V1 | XRP | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,01197 | 1,01310 | 1,02330 | 1,34423 | 0,99497 | €1.451,45 | €4.354,36 | €48,77 | €-4,87 |
| 1H Fast V3 No Esports V1 | CYS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,33140 | 1,31820 | 1,19968 | 0,89426 | 1,52898 | €159,86 | €479,59 | €47,45 | €-4,75 |
| 1H Fast V3 No Esports Long Only V1 | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 55,32406 | 55,42000 | 54,58296 | 37,15933 | 56,43571 | €1.234,84 | €3.704,51 | €49,62 | €6,42 |
| 1H Fast V3 No Esports Long Only V1 | SPCX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 136,80203 | 137,17000 | 133,40452 | 91,88536 | 141,89830 | €665,50 | €1.996,50 | €49,58 | €5,37 |
| 1H Fast V3 No Esports Long Only V1 | CYS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,33140 | 1,31820 | 1,19968 | 0,89426 | 1,52898 | €166,51 | €499,53 | €49,42 | €-4,95 |
| 1H Fast V3 No Esports Mfe Lock V1 | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 55,32406 | 55,42000 | 54,58296 | 37,15933 | 56,43571 | €1.256,15 | €3.768,44 | €50,48 | €6,53 |
| 1H Fast V3 No Esports Mfe Lock V1 | SPCX | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 136,80203 | 137,17000 | 133,40452 | 91,88536 | 141,89830 | €676,98 | €2.030,95 | €50,44 | €5,46 |
| 1H Fast V3 No Esports Mfe Lock V1 | XRP | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,01197 | 1,01310 | 1,02330 | 1,34423 | 0,99497 | €1.491,36 | €4.474,07 | €50,11 | €-5,01 |
| 1H Fast V3 No Esports Mfe Lock V1 | CYS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,33140 | 1,31820 | 1,19968 | 0,89426 | 1,52898 | €164,26 | €492,78 | €48,75 | €-4,88 |
| Ampia 4H | XMR | LONG | Confluenza trend | 240m | 2,0x | 364,45854 | 364,45854 | 386,58243 | 184,05156 | 410,69083 | €544,42 | €1.088,84 | €0,00 | €0,00 |
| Ampia 4H | DOGE | SHORT | Confluenza trend | 240m | 2,0x | 0,07002 | 0,07003 | 0,07288 | 0,10467 | 0,06199 | €17,06 | €34,13 | €1,40 | €-0,01 |
| Ampia 4H | XRP | SHORT | Confluenza trend | 240m | 2,0x | 1,01047 | 1,01310 | 1,04043 | 1,51065 | 0,92656 | €831,51 | €1.663,02 | €49,32 | €-4,33 |
| Ampia 4H | BEAT | SHORT | Confluenza trend | 240m | 2,0x | 1,71466 | 1,39730 | 1,71466 | 2,56341 | 1,13853 | €205,47 | €410,93 | €0,00 | €76,06 |
| Ampia 4H | SPCX | LONG | Confluenza trend | 240m | 2,0x | 136,56189 | 137,17000 | 126,46637 | 68,96375 | 164,82935 | €323,86 | €647,73 | €47,88 | €2,88 |
| Forza relativa 1H V1 | SPCX | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 136,85206 | 137,17000 | 132,31345 | 69,11029 | 146,83700 | €726,10 | €1.452,21 | €48,16 | €3,37 |
| Forza relativa 1H V1 | HYPE | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 55,32406 | 55,42000 | 54,37122 | 27,93865 | 57,42031 | €1.397,93 | €2.795,86 | €48,15 | €4,85 |
| Forza relativa 1H V1 | CYS | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 1,28356 | 1,31820 | 1,12953 | 0,64820 | 1,62242 | €200,59 | €401,18 | €48,14 | €10,83 |
| Forza relativa 1H V1 | BEAT | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 1,31391 | 1,39730 | 1,47158 | 1,96429 | 0,96704 | €201,67 | €403,34 | €48,40 | €-25,60 |
| Forza relativa 1H V2 | CYS | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 1,32770 | 1,31820 | 1,16837 | 0,67049 | 1,67821 | €206,96 | €413,93 | €49,67 | €-2,96 |
| Forza relativa 1H V2 | HYPE | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 55,42308 | 55,42000 | 54,61538 | 27,98866 | 57,20002 | €1.703,07 | €3.406,15 | €49,64 | €-0,19 |
| Forza relativa 1H V2 | SPCX | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 137,25230 | 137,17000 | 134,05746 | 69,31241 | 144,28095 | €1.066,37 | €2.132,73 | €49,64 | €-1,28 |
| Benchmark Donchian breakout 1H | XRP | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 1,01197 | 1,01310 | 1,02816 | 1,51289 | 0,97149 | €1.650,43 | €3.300,86 | €52,81 | €-3,69 |
| Benchmark Donchian breakout 1H | BEAT | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 1,29313 | 1,39730 | 1,44831 | 1,93323 | 0,90519 | €219,77 | €439,54 | €52,74 | €-35,41 |
| Benchmark Donchian breakout 1H | ZEC | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 491,45169 | 493,00000 | 500,60716 | 734,72028 | 468,56302 | €1.415,57 | €2.831,15 | €52,74 | €-8,92 |
| Donchian 1H Gb20 120R V1 | XRP | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 1,01197 | 1,01310 | 1,02816 | 1,51289 | 0,97149 | €1.611,57 | €3.223,15 | €51,57 | €-3,61 |
| Donchian 1H Gb20 120R V1 | BEAT | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 1,29313 | 1,39730 | 1,44831 | 1,93323 | 0,90519 | €214,59 | €429,19 | €51,50 | €-34,57 |
| Donchian 1H Gb20 120R V1 | ZEC | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 491,45169 | 493,00000 | 500,60716 | 734,72028 | 468,56302 | €1.382,25 | €2.764,49 | €51,50 | €-8,71 |
| Benchmark Bollinger mean reversion 1H | XRP | LONG | Bollinger mean reversion | 60m | 2,0x | 1,01237 | 1,01310 | 1,00022 | 0,51125 | 1,03060 | €1.952,30 | €3.904,60 | €46,86 | €2,81 |
| Benchmark trend following EMA 1H | BTC | SHORT | Trend following EMA | 60m | 2,0x | 64070,44335 | 64026,93000 | 65095,57044 | 95785,31281 | 61815,16374 | €1.516,95 | €3.033,89 | €48,54 | €2,06 |
| Benchmark trend following EMA 1H | SPCX | LONG | Trend following EMA | 60m | 2,0x | 136,85206 | 137,17000 | 131,80916 | 69,11029 | 147,94644 | €658,50 | €1.316,99 | €48,53 | €3,06 |
| Benchmark trend following EMA 1H | XRP | SHORT | Trend following EMA | 60m | 2,0x | 1,02104 | 1,01310 | 1,03737 | 1,52645 | 0,98510 | €1.516,32 | €3.032,64 | €48,52 | €23,57 |
| Benchmark trend following EMA 1H | DOGE | SHORT | Trend following EMA | 60m | 2,0x | 0,06964 | 0,07003 | 0,07075 | 0,10411 | 0,06718 | €1.522,48 | €3.044,96 | €48,72 | €-17,23 |
| Scanner Top 5 Long 1H | CYS | LONG | Scanner Top 5 Long | 60m | 2,0x | 1,28356 | 1,31820 | 1,12953 | 0,64820 | 1,59161 | €215,74 | €431,48 | €51,78 | €11,65 |
| Scanner Top 5 Long 1H | SPCX | LONG | Scanner Top 5 Long | 60m | 2,0x | 136,85206 | 137,17000 | 132,31345 | 69,11029 | 145,92928 | €780,60 | €1.561,19 | €51,78 | €3,63 |
| Scanner Top 5 Long 1H | HYPE | LONG | Scanner Top 5 Long | 60m | 2,0x | 55,32406 | 55,42000 | 54,37122 | 27,93865 | 57,22974 | €1.502,84 | €3.005,68 | €51,77 | €5,21 |
| Scanner Bottom 5 Short 1H | XRP | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1,02104 | 1,01310 | 1,01832 | 1,52645 | 0,99163 | €1.717,56 | €3.435,12 | €0,00 | €26,70 |
| Scanner Bottom 5 Short 1H | BTC | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 64070,44335 | 64026,93000 | 64993,05773 | 95785,31281 | 62225,21458 | €1.717,08 | €3.434,17 | €49,45 | €2,33 |
| Scanner Bottom 5 Short 1H | DOGE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,06982 | 0,07003 | 0,07082 | 0,10437 | 0,06781 | €1.722,95 | €3.445,90 | €49,62 | €-10,56 |
| Scanner Bottom 5 Short 1H | ZEC | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 491,45169 | 493,00000 | 499,69161 | 734,72028 | 474,97185 | €1.480,14 | €2.960,29 | €49,63 | €-9,33 |
| Scanner Top10 Long | CYS | LONG | Scanner Top10 Long | 60m | 2,0x | 1,28356 | 1,31820 | 1,12953 | 0,64820 | 1,59161 | €198,71 | €397,43 | €47,69 | €10,73 |
| Scanner Top10 Long | SPCX | LONG | Scanner Top10 Long | 60m | 2,0x | 136,85206 | 137,17000 | 132,31345 | 69,11029 | 145,92928 | €718,99 | €1.437,98 | €47,69 | €3,34 |
| Scanner Top10 Long | HYPE | LONG | Scanner Top10 Long | 60m | 2,0x | 55,32406 | 55,42000 | 54,37122 | 27,93865 | 57,22974 | €1.384,23 | €2.768,46 | €47,68 | €4,80 |
| Scanner Bottom10 Short | XRP | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 1,02104 | 1,01310 | 1,01832 | 1,52645 | 0,99163 | €1.728,78 | €3.457,57 | €0,00 | €26,87 |
| Scanner Bottom10 Short | BTC | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 64070,44335 | 64026,93000 | 64993,05773 | 95785,31281 | 62225,21458 | €1.728,30 | €3.456,61 | €49,78 | €2,35 |
| Scanner Bottom10 Short | DOGE | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,06964 | 0,07003 | 0,07064 | 0,10411 | 0,06763 | €1.736,20 | €3.472,41 | €50,00 | €-19,64 |
| Scanner Bottom10 Short | ZEC | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 491,45169 | 493,00000 | 499,69161 | 734,72028 | 474,97185 | €1.488,41 | €2.976,82 | €49,91 | €-9,38 |
| Scanner Top15 Long | CYS | LONG | Scanner Top15 Long | 60m | 2,0x | 1,28356 | 1,31820 | 1,12953 | 0,64820 | 1,59161 | €198,71 | €397,43 | €47,69 | €10,73 |
| Scanner Top15 Long | SPCX | LONG | Scanner Top15 Long | 60m | 2,0x | 136,85206 | 137,17000 | 132,31345 | 69,11029 | 145,92928 | €718,99 | €1.437,98 | €47,69 | €3,34 |
| Scanner Top15 Long | HYPE | LONG | Scanner Top15 Long | 60m | 2,0x | 55,32406 | 55,42000 | 54,37122 | 27,93865 | 57,22974 | €1.384,23 | €2.768,46 | €47,68 | €4,80 |
| Scanner Bottom15 Short | XRP | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 1,02104 | 1,01310 | 1,01832 | 1,52645 | 0,99163 | €1.728,78 | €3.457,57 | €0,00 | €26,87 |
| Scanner Bottom15 Short | BTC | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 64070,44335 | 64026,93000 | 64993,05773 | 95785,31281 | 62225,21458 | €1.728,30 | €3.456,61 | €49,78 | €2,35 |
| Scanner Bottom15 Short | DOGE | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,06964 | 0,07003 | 0,07064 | 0,10411 | 0,06763 | €1.736,20 | €3.472,41 | €50,00 | €-19,64 |
| Scanner Bottom15 Short | ZEC | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 491,45169 | 493,00000 | 499,69161 | 734,72028 | 474,97185 | €1.488,41 | €2.976,82 | €49,91 | €-9,38 |
| Scanner Top20 Long | CYS | LONG | Scanner Top20 Long | 60m | 2,0x | 1,28356 | 1,31820 | 1,12953 | 0,64820 | 1,59161 | €198,71 | €397,43 | €47,69 | €10,73 |
| Scanner Top20 Long | SPCX | LONG | Scanner Top20 Long | 60m | 2,0x | 136,85206 | 137,17000 | 132,31345 | 69,11029 | 145,92928 | €718,99 | €1.437,98 | €47,69 | €3,34 |
| Scanner Top20 Long | HYPE | LONG | Scanner Top20 Long | 60m | 2,0x | 55,32406 | 55,42000 | 54,37122 | 27,93865 | 57,22974 | €1.384,23 | €2.768,46 | €47,68 | €4,80 |
| Scanner Bottom20 Short | XRP | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 1,02104 | 1,01310 | 1,01832 | 1,52645 | 0,99163 | €1.728,78 | €3.457,57 | €0,00 | €26,87 |
| Scanner Bottom20 Short | BTC | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 64070,44335 | 64026,93000 | 64993,05773 | 95785,31281 | 62225,21458 | €1.728,30 | €3.456,61 | €49,78 | €2,35 |
| Scanner Bottom20 Short | DOGE | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,06964 | 0,07003 | 0,07064 | 0,10411 | 0,06763 | €1.736,20 | €3.472,41 | €50,00 | €-19,64 |
| Scanner Bottom20 Short | ZEC | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 491,45169 | 493,00000 | 499,69161 | 734,72028 | 474,97185 | €1.488,41 | €2.976,82 | €49,91 | €-9,38 |
| Scanner Top 5 + forza BTC 1H | CYS | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,28356 | 1,31820 | 1,12953 | 0,64820 | 1,62242 | €213,00 | €426,01 | €51,12 | €11,50 |
| Scanner Top 5 + forza BTC 1H | SPCX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 136,85206 | 137,17000 | 132,31345 | 69,11029 | 146,83700 | €770,70 | €1.541,40 | €51,12 | €3,58 |
| Scanner Top 5 + forza BTC 1H | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 55,32406 | 55,42000 | 54,37122 | 27,93865 | 57,42031 | €1.483,78 | €2.967,57 | €51,11 | €5,15 |
| Scanner Top5 Btc Mfe V1 | CYS | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,28356 | 1,31820 | 1,12953 | 0,64820 | 1,62242 | €199,66 | €399,32 | €47,92 | €10,78 |
| Scanner Top5 Btc Mfe V1 | SPCX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 136,85206 | 137,17000 | 132,31345 | 69,11029 | 146,83700 | €722,42 | €1.444,84 | €47,92 | €3,36 |
| Scanner Top5 Btc Mfe V1 | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 55,32406 | 55,42000 | 54,37122 | 27,93865 | 57,42031 | €1.390,83 | €2.781,67 | €47,91 | €4,82 |
| Scanner Top5 Btc Guard V1 | CYS | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,28356 | 1,31820 | 1,12953 | 0,64820 | 1,62242 | €201,85 | €403,69 | €48,44 | €10,90 |
| Scanner Top5 Btc Guard V1 | SPCX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 136,85206 | 137,17000 | 132,31345 | 69,11029 | 146,83700 | €730,33 | €1.460,65 | €48,44 | €3,39 |
| Scanner Top5 Btc Guard V1 | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 55,32406 | 55,42000 | 54,37122 | 27,93865 | 57,42031 | €1.406,06 | €2.812,12 | €48,43 | €4,88 |
| Scanner Top5 Btc Btc Le3 V1 | CYS | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,28356 | 1,31820 | 1,12953 | 0,64820 | 1,62242 | €203,55 | €407,09 | €48,85 | €10,99 |
| Scanner Top5 Btc Btc Le3 V1 | SPCX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 136,85206 | 137,17000 | 132,31345 | 69,11029 | 146,83700 | €736,48 | €1.472,96 | €48,85 | €3,42 |
| Scanner Top5 Btc Btc Le3 V1 | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 55,32406 | 55,42000 | 54,37122 | 27,93865 | 57,42031 | €1.417,90 | €2.835,81 | €48,84 | €4,92 |
| Scanner Top5 Btc Guard Mfe V1 | CYS | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,28356 | 1,31820 | 1,12953 | 0,64820 | 1,62242 | €197,15 | €394,30 | €47,32 | €10,64 |
| Scanner Top5 Btc Guard Mfe V1 | SPCX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 136,85206 | 137,17000 | 132,31345 | 69,11029 | 146,83700 | €713,34 | €1.426,68 | €47,31 | €3,31 |
| Scanner Top5 Btc Guard Mfe V1 | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 55,32406 | 55,42000 | 54,37122 | 27,93865 | 57,42031 | €1.373,36 | €2.746,72 | €47,31 | €4,76 |
| Scanner Top5 Btc Guard Btc Le3 V1 | CYS | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,28356 | 1,31820 | 1,12953 | 0,64820 | 1,62242 | €204,33 | €408,65 | €49,04 | €11,03 |
| Scanner Top5 Btc Guard Btc Le3 V1 | SPCX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 136,85206 | 137,17000 | 132,31345 | 69,11029 | 146,83700 | €739,30 | €1.478,60 | €49,04 | €3,44 |
| Scanner Top5 Btc Guard Btc Le3 V1 | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 55,32406 | 55,42000 | 54,37122 | 27,93865 | 57,42031 | €1.423,33 | €2.846,66 | €49,03 | €4,94 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | CYS | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,28356 | 1,31820 | 1,12953 | 0,64820 | 1,62242 | €200,82 | €401,64 | €48,20 | €10,84 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | SPCX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 136,85206 | 137,17000 | 132,31345 | 69,11029 | 146,83700 | €726,61 | €1.453,23 | €48,20 | €3,38 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 55,32406 | 55,42000 | 54,37122 | 27,93865 | 57,42031 | €1.398,91 | €2.797,82 | €48,19 | €4,85 |
| Scanner Top5 Btc Runner25 V1 | CYS | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,28356 | 1,31820 | 1,12953 | 0,64820 | 1,74564 | €204,95 | €409,90 | €49,19 | €11,06 |
| Scanner Top5 Btc Runner25 V1 | SPCX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 136,85206 | 137,17000 | 132,31345 | 69,11029 | 150,46789 | €741,55 | €1.483,11 | €49,19 | €3,45 |
| Scanner Top5 Btc Runner25 V1 | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 55,32406 | 55,42000 | 54,37122 | 27,93865 | 58,18259 | €1.427,68 | €2.855,35 | €49,18 | €4,95 |
| Scanner Top5 Btc Tp3 V1 | CYS | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,28356 | 1,31820 | 1,12953 | 0,64820 | 1,74564 | €205,07 | €410,14 | €49,22 | €11,07 |
| Scanner Top5 Btc Tp3 V1 | SPCX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 136,85206 | 137,17000 | 132,31345 | 69,11029 | 150,46789 | €741,99 | €1.483,98 | €49,22 | €3,45 |
| Scanner Top5 Btc Tp3 V1 | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 55,32406 | 55,42000 | 54,37122 | 27,93865 | 58,18259 | €1.428,51 | €2.857,02 | €49,21 | €4,95 |
| Global Confluence puro 1H | DOGE | SHORT | Global Confluence puro | 60m | 2,0x | 0,06964 | 0,07003 | 0,07075 | 0,10411 | 0,06685 | €1.528,83 | €3.057,65 | €48,92 | €-17,30 |
| Combo Trend | SPCX | LONG | Combo Trend | 60m | 2,0x | 136,85206 | 137,17000 | 131,80916 | 69,11029 | 147,94644 | €646,55 | €1.293,10 | €47,65 | €3,00 |
| Combo Trend | DOGE | SHORT | Combo Trend | 60m | 2,0x | 0,06964 | 0,07003 | 0,07075 | 0,10411 | 0,06718 | €1.488,74 | €2.977,49 | €47,64 | €-16,84 |
| Combo Trend | XRP | SHORT | Combo Trend | 60m | 2,0x | 1,01197 | 1,01310 | 1,02816 | 1,51289 | 0,97635 | €1.480,58 | €2.961,16 | €47,38 | €-3,31 |
| Combo Trend | ZEC | SHORT | Combo Trend | 60m | 2,0x | 491,45169 | 493,00000 | 500,60716 | 734,72028 | 471,30966 | €34,52 | €69,05 | €1,29 | €-0,22 |
| Combo Trend | BEAT | SHORT | Combo Trend | 60m | 2,0x | 1,31391 | 1,39730 | 1,47158 | 1,96429 | 0,96704 | €195,22 | €390,44 | €46,85 | €-24,78 |
| Combo Mean Reversion | ZEC | LONG | Combo Mean Reversion | 60m | 2,0x | 491,64831 | 493,00000 | 484,77896 | 248,28240 | 502,63927 | €1.759,32 | €3.518,64 | €49,16 | €9,67 |
| Combo Scanner | CYS | LONG | Combo Scanner | 60m | 2,0x | 1,28356 | 1,31820 | 1,12953 | 0,64820 | 1,62242 | €201,94 | €403,87 | €48,46 | €10,90 |
| Combo Scanner | SPCX | LONG | Combo Scanner | 60m | 2,0x | 136,85206 | 137,17000 | 132,31345 | 69,11029 | 146,83700 | €730,65 | €1.461,31 | €48,46 | €3,39 |
| Combo Scanner | HYPE | LONG | Combo Scanner | 60m | 2,0x | 55,32406 | 55,42000 | 54,37122 | 27,93865 | 57,42031 | €1.406,69 | €2.813,38 | €48,45 | €4,88 |
| Combo Scanner | DOGE | SHORT | Combo Scanner | 60m | 2,0x | 0,06982 | 0,07003 | 0,07082 | 0,10437 | 0,06760 | €1.668,13 | €3.336,26 | €48,04 | €-10,22 |
| Combo Adaptive | CYS | LONG | Combo Adaptive | 60m | 2,0x | 1,28356 | 1,31820 | 1,12953 | 0,64820 | 1,59161 | €210,67 | €421,33 | €50,56 | €11,37 |
| Combo Adaptive | SPCX | LONG | Combo Adaptive | 60m | 2,0x | 136,85206 | 137,17000 | 132,31345 | 69,11029 | 145,92928 | €762,24 | €1.524,48 | €50,56 | €3,54 |
| Combo Adaptive | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 55,24705 | 55,42000 | 54,31202 | 27,89976 | 57,11709 | €1.493,31 | €2.986,63 | €50,55 | €9,35 |
| Combo Adaptive | ZEC | SHORT | Combo Adaptive | 60m | 2,0x | 491,45169 | 493,00000 | 499,69161 | 734,72028 | 474,97185 | €1.512,79 | €3.025,57 | €50,73 | €-9,53 |
| Combo Adaptive Mfe Trail | CYS | LONG | Combo Adaptive | 60m | 2,0x | 1,28356 | 1,31820 | 1,12953 | 0,64820 | 1,59161 | €194,41 | €388,82 | €46,66 | €10,49 |
| Combo Adaptive Mfe Trail | SPCX | LONG | Combo Adaptive | 60m | 2,0x | 136,85206 | 137,17000 | 132,31345 | 69,11029 | 145,92928 | €703,43 | €1.406,85 | €46,66 | €3,27 |
| Combo Adaptive Mfe Trail | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 55,24705 | 55,42000 | 54,31202 | 27,89976 | 57,11709 | €1.378,10 | €2.756,19 | €46,65 | €8,63 |
| Combo Adaptive Mfe Trail | ZEC | SHORT | Combo Adaptive | 60m | 2,0x | 491,45169 | 493,00000 | 499,69161 | 734,72028 | 474,97185 | €1.396,07 | €2.792,13 | €46,81 | €-8,80 |
| Combo Adaptive Quality7 V1 | BEAT | SHORT | Combo Adaptive | 60m | 2,0x | 1,29313 | 1,39730 | 1,44831 | 1,93323 | 0,98278 | €207,25 | €414,51 | €49,74 | €-33,39 |
| Combo Adaptive Long Only V1 | CYS | LONG | Combo Adaptive | 60m | 2,0x | 1,28356 | 1,31820 | 1,12953 | 0,64820 | 1,59161 | €206,91 | €413,83 | €49,66 | €11,17 |
| Combo Adaptive Long Only V1 | SPCX | LONG | Combo Adaptive | 60m | 2,0x | 136,85206 | 137,17000 | 132,31345 | 69,11029 | 145,92928 | €748,66 | €1.497,32 | €49,66 | €3,48 |
| Combo Adaptive Long Only V1 | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 55,24705 | 55,42000 | 54,31202 | 27,89976 | 57,11709 | €1.466,71 | €2.933,42 | €49,65 | €9,18 |
| Combo Adaptive Partial 1R V1 | CYS | LONG | Combo Adaptive | 60m | 2,0x | 1,28356 | 1,31820 | 1,12953 | 0,64820 | 1,59161 | €202,29 | €404,58 | €48,55 | €10,92 |
| Combo Adaptive Partial 1R V1 | SPCX | LONG | Combo Adaptive | 60m | 2,0x | 136,85206 | 137,17000 | 132,31345 | 69,11029 | 145,92928 | €731,94 | €1.463,87 | €48,55 | €3,40 |
| Combo Adaptive Partial 1R V1 | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 55,24705 | 55,42000 | 54,31202 | 27,89976 | 57,11709 | €1.433,95 | €2.867,89 | €48,54 | €8,98 |
| Combo Adaptive Partial 1R V1 | ZEC | SHORT | Combo Adaptive | 60m | 2,0x | 491,45169 | 493,00000 | 499,69161 | 734,72028 | 474,97185 | €1.452,65 | €2.905,29 | €48,71 | €-9,15 |
| Combo Adaptive Runner25 V1 | CYS | LONG | Combo Adaptive | 60m | 2,0x | 1,28356 | 1,31820 | 1,12953 | 0,64820 | 1,74564 | €209,83 | €419,66 | €50,36 | €11,33 |
| Combo Adaptive Runner25 V1 | SPCX | LONG | Combo Adaptive | 60m | 2,0x | 136,85206 | 137,17000 | 132,31345 | 69,11029 | 150,46789 | €759,21 | €1.518,41 | €50,36 | €3,53 |
| Combo Adaptive Runner25 V1 | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 55,24705 | 55,42000 | 54,31202 | 27,89976 | 58,05212 | €1.487,37 | €2.974,74 | €50,35 | €9,31 |
| Combo Adaptive Runner25 V1 | BEAT | SHORT | Combo Adaptive | 60m | 2,0x | 1,71466 | 1,39730 | 1,50962 | 2,56341 | 1,09738 | €202,19 | €404,38 | €0,00 | €74,84 |
| Combo Adaptive Runner25 V1 | ZEC | SHORT | Combo Adaptive | 60m | 2,0x | 491,45169 | 493,00000 | 499,69161 | 734,72028 | 466,73193 | €76,64 | €153,27 | €2,57 | €-0,48 |
| Combo Adaptive Tp3 V1 | CYS | LONG | Combo Adaptive | 60m | 2,0x | 1,28356 | 1,31820 | 1,12953 | 0,64820 | 1,74564 | €205,91 | €411,82 | €49,42 | €11,11 |
| Combo Adaptive Tp3 V1 | SPCX | LONG | Combo Adaptive | 60m | 2,0x | 136,85206 | 137,17000 | 132,31345 | 69,11029 | 150,46789 | €745,02 | €1.490,04 | €49,42 | €3,46 |
| Combo Adaptive Tp3 V1 | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 55,24705 | 55,42000 | 54,31202 | 27,89976 | 58,05212 | €1.459,58 | €2.919,17 | €49,41 | €9,14 |
| Combo Adaptive Tp3 V1 | BEAT | SHORT | Combo Adaptive | 60m | 2,0x | 1,71466 | 1,39730 | 1,50962 | 2,56341 | 1,09738 | €198,41 | €396,82 | €0,00 | €73,45 |
| Combo Adaptive Tp3 V1 | ZEC | SHORT | Combo Adaptive | 60m | 2,0x | 491,45169 | 493,00000 | 499,69161 | 734,72028 | 466,73193 | €75,20 | €150,41 | €2,52 | €-0,47 |
| Btc Ema 1H | BTC | SHORT | Trend following EMA | 60m | 3,0x | 64070,44335 | 64026,93000 | 64993,05773 | 85106,90558 | 62225,21458 | €1.141,05 | €3.423,15 | €49,29 | €2,32 |
| Doge Ema 1H | DOGE | SHORT | Trend following EMA | 60m | 3,0x | 0,06964 | 0,07003 | 0,07064 | 0,09250 | 0,06763 | €1.168,55 | €3.505,64 | €50,48 | €-19,83 |
| Master Adaptive V1 | CYS | LONG | Master Adaptive Consensus | 60m | 2,0x | 1,32770 | 1,31820 | 1,16837 | 0,67049 | 1,64634 | €203,23 | €406,45 | €48,77 | €-2,91 |
| Master Adaptive V1 | SPCX | LONG | Master Adaptive Consensus | 60m | 2,0x | 136,76201 | 137,17000 | 133,25764 | 69,06481 | 143,77074 | €951,69 | €1.903,38 | €48,77 | €5,68 |
| Master Adaptive V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 55,29106 | 55,42000 | 54,45225 | 27,92198 | 56,96866 | €1.607,06 | €3.214,12 | €48,76 | €7,50 |
| Master Adaptive No Alt V1 | CYS | LONG | Master Adaptive Consensus | 60m | 2,0x | 1,32770 | 1,31820 | 1,16837 | 0,67049 | 1,64634 | €203,31 | €406,62 | €48,79 | €-2,91 |
| Master Adaptive No Alt V1 | SPCX | LONG | Master Adaptive Consensus | 60m | 2,0x | 136,76201 | 137,17000 | 133,25764 | 69,06481 | 143,77074 | €952,08 | €1.904,17 | €48,79 | €5,68 |
| Master Adaptive No Alt V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 55,29106 | 55,42000 | 54,45225 | 27,92198 | 56,96866 | €1.607,72 | €3.215,45 | €48,78 | €7,50 |
| Master Adaptive Strict3 V1 | CYS | LONG | Master Adaptive Consensus | 60m | 2,0x | 1,32770 | 1,31820 | 1,16837 | 0,67049 | 1,64634 | €195,94 | €391,88 | €47,03 | €-2,80 |
| Master Adaptive Strict3 V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 55,42308 | 55,42000 | 54,61538 | 27,98866 | 57,03848 | €1.612,35 | €3.224,71 | €46,99 | €-0,18 |
| Master Adaptive Strict3 V1 | SPCX | LONG | Master Adaptive Consensus | 60m | 2,0x | 137,25230 | 137,17000 | 134,05746 | 69,31241 | 143,64199 | €1.009,56 | €2.019,13 | €47,00 | €-1,21 |
| Master Adaptive Expanded V1 | CYS | LONG | Master Adaptive Consensus | 60m | 2,0x | 1,32770 | 1,31820 | 1,16837 | 0,67049 | 1,64634 | €204,15 | €408,29 | €49,00 | €-2,92 |
| Master Adaptive Expanded V1 | SPCX | LONG | Master Adaptive Consensus | 60m | 2,0x | 136,76201 | 137,17000 | 133,25764 | 69,06481 | 143,77074 | €956,00 | €1.912,01 | €48,99 | €5,70 |
| Master Adaptive Expanded V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 55,29106 | 55,42000 | 54,45225 | 27,92198 | 56,96866 | €1.614,34 | €3.228,69 | €48,98 | €7,53 |
| Master Adaptive Gb20 V1 | CYS | LONG | Master Adaptive Consensus | 60m | 2,0x | 1,32770 | 1,31820 | 1,16837 | 0,67049 | 1,64634 | €200,53 | €401,05 | €48,13 | €-2,87 |
| Master Adaptive Gb20 V1 | SPCX | LONG | Master Adaptive Consensus | 60m | 2,0x | 136,76201 | 137,17000 | 133,25764 | 69,06481 | 143,77074 | €939,05 | €1.878,09 | €48,12 | €5,60 |
| Master Adaptive Gb20 V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 55,29106 | 55,42000 | 54,45225 | 27,92198 | 56,96866 | €1.585,71 | €3.171,42 | €48,11 | €7,40 |
| Master Adaptive Runner25 V1 | CYS | LONG | Master Adaptive Consensus | 60m | 2,0x | 1,32770 | 1,31820 | 1,16837 | 0,67049 | 1,80567 | €203,58 | €407,15 | €48,86 | €-2,91 |
| Master Adaptive Runner25 V1 | SPCX | LONG | Master Adaptive Consensus | 60m | 2,0x | 136,76201 | 137,17000 | 133,25764 | 69,06481 | 147,27511 | €953,33 | €1.906,66 | €48,86 | €5,69 |
| Master Adaptive Runner25 V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 55,29106 | 55,42000 | 54,45225 | 27,92198 | 57,80747 | €1.609,83 | €3.219,66 | €48,84 | €7,51 |
| Combo Adaptive Side Regime Guard V1 | XRP | SHORT | Combo Adaptive | 60m | 2,0x | 1,01197 | 1,01310 | 1,02654 | 1,51289 | 0,98282 | €1.785,27 | €3.570,54 | €51,42 | €-4,00 |
| Combo Adaptive Side Regime Guard V1 | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,06982 | 0,07003 | 0,07082 | 0,10437 | 0,06781 | €1.784,78 | €3.569,55 | €51,40 | €-10,94 |
| Combo Adaptive Side Regime Guard V1 | ZEC | SHORT | Combo Adaptive | 60m | 2,0x | 491,45169 | 493,00000 | 499,69161 | 734,72028 | 474,97185 | €1.534,08 | €3.068,15 | €51,44 | €-9,67 |
| Combo Adaptive Side Regime Guard V1 | BEAT | SHORT | Combo Adaptive | 60m | 2,0x | 1,30406 | 1,39730 | 1,46055 | 1,94957 | 0,99108 | €214,32 | €428,65 | €51,44 | €-30,65 |
| Master Adaptive Gb20 Be V1 | CYS | LONG | Master Adaptive Consensus | 60m | 2,0x | 1,32770 | 1,31820 | 1,16837 | 0,67049 | 1,64634 | €204,23 | €408,47 | €49,02 | €-2,92 |
| Master Adaptive Gb20 Be V1 | SPCX | LONG | Master Adaptive Consensus | 60m | 2,0x | 136,76201 | 137,17000 | 133,25764 | 69,06481 | 143,77074 | €956,40 | €1.912,81 | €49,01 | €5,71 |
| Master Adaptive Gb20 Be V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 55,29106 | 55,42000 | 54,45225 | 27,92198 | 56,96866 | €1.615,02 | €3.230,04 | €49,00 | €7,53 |
| Master Adaptive Gb20 Partial V1 | CYS | LONG | Master Adaptive Consensus | 60m | 2,0x | 1,32770 | 1,31820 | 1,16837 | 0,67049 | 1,64634 | €204,02 | €408,03 | €48,96 | €-2,92 |
| Master Adaptive Gb20 Partial V1 | SPCX | LONG | Master Adaptive Consensus | 60m | 2,0x | 136,76201 | 137,17000 | 133,25764 | 69,06481 | 143,77074 | €955,39 | €1.910,77 | €48,96 | €5,70 |
| Master Adaptive Gb20 Partial V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 55,29106 | 55,42000 | 54,45225 | 27,92198 | 56,96866 | €1.613,30 | €3.226,60 | €48,95 | €7,52 |
| Master Adaptive Gb20 Loss Cap V1 | CYS | LONG | Master Adaptive Consensus | 60m | 2,0x | 1,32770 | 1,31820 | 1,20521 | 0,67049 | 1,65434 | €262,28 | €524,56 | €48,40 | €-3,75 |
| Master Adaptive Gb20 Loss Cap V1 | SPCX | LONG | Master Adaptive Consensus | 60m | 2,0x | 136,76201 | 137,17000 | 134,13373 | 69,06481 | 143,77074 | €1.259,04 | €2.518,08 | €48,39 | €7,51 |
| Master Adaptive Gb20 Loss Cap V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 55,29106 | 55,42000 | 54,66195 | 27,92198 | 56,96866 | €1.935,08 | €3.870,17 | €44,03 | €9,03 |
| 1H Fast V3 Nohigh Range Only V1 | BEAT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,29600 | 1,39730 | 1,45152 | 1,72152 | 1,06272 | €143,00 | €428,99 | €51,48 | €-33,53 |
| 1H Fast V3 Nohigh Regime Guard V1 | BEAT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,29600 | 1,39730 | 1,45152 | 1,72152 | 1,06272 | €144,44 | €433,33 | €52,00 | €-33,87 |
| Main Side Regime Guard V1 | XRP | SHORT | Confluenza trend | 240m | 3,0x | 1,01047 | 1,01310 | 1,03352 | 1,34224 | 0,96437 | €747,08 | €2.241,25 | €51,13 | €-5,84 |
| Combo Trend Side Regime Guard V1 | DOGE | SHORT | Combo Trend | 60m | 2,0x | 0,06964 | 0,07003 | 0,07075 | 0,10411 | 0,06718 | €1.566,82 | €3.133,64 | €50,14 | €-17,73 |
| Combo Trend Side Regime Guard V1 | XRP | SHORT | Combo Trend | 60m | 2,0x | 1,01197 | 1,01310 | 1,02816 | 1,51289 | 0,97635 | €1.565,11 | €3.130,22 | €50,08 | €-3,50 |
| Combo Trend Side Regime Guard V1 | ZEC | SHORT | Combo Trend | 60m | 2,0x | 491,45169 | 493,00000 | 500,60716 | 734,72028 | 471,30966 | €1.345,98 | €2.691,96 | €50,15 | €-8,48 |
| Combo Trend Side Regime Guard V1 | HYPE | LONG | Combo Trend | 60m | 2,0x | 55,42308 | 55,42000 | 54,52564 | 27,98866 | 57,39746 | €1.548,11 | €3.096,22 | €50,14 | €-0,17 |
| 1H Fast Nohigh Cap75 Short Only V1 | BEAT | SHORT | Momentum / breakout | 60m | 3,0x | 1,29600 | 1,39730 | 1,45152 | 1,72152 | 1,06272 | €142,10 | €426,29 | €51,16 | €-33,32 |
| 1H Fast Nohigh Cap75 Short Only V1 | CYS | LONG | Momentum / breakout | 60m | 3,0x | 1,32770 | 1,31820 | 1,20067 | 0,89177 | 1,51824 | €178,22 | €534,66 | €51,15 | €-3,82 |
| 1H Balanced V3 Long Only V1 | SPCX | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 136,85206 | 137,17000 | 132,31345 | 91,91897 | 145,92928 | €496,25 | €1.488,74 | €49,37 | €3,46 |
| 1H Balanced V3 Long Only V1 | HYPE | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 55,32406 | 55,42000 | 54,37122 | 37,15933 | 57,22974 | €955,40 | €2.866,19 | €49,36 | €4,97 |
| 1H Balanced V3 Long Only V1 | DOGE | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,06964 | 0,07003 | 0,07064 | 0,09250 | 0,06763 | €1.141,90 | €3.425,69 | €49,33 | €-19,38 |
| 1H Balanced V3 Long Only V1 | CYS | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1,33140 | 1,31820 | 1,17163 | 0,89426 | 1,65093 | €134,76 | €404,29 | €48,51 | €-4,01 |
| Scanner Bottom5 Short Profit Lock V1 | XRP | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1,02104 | 1,01310 | 1,01832 | 1,52645 | 0,99163 | €1.730,88 | €3.461,76 | €0,00 | €26,91 |
| Scanner Bottom5 Short Profit Lock V1 | BTC | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 64070,44335 | 64026,93000 | 64993,05773 | 95785,31281 | 62225,21458 | €1.730,40 | €3.460,80 | €49,84 | €2,35 |
| Scanner Bottom5 Short Profit Lock V1 | DOGE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,06982 | 0,07003 | 0,07082 | 0,10437 | 0,06781 | €1.736,31 | €3.472,62 | €50,01 | €-10,64 |
| Scanner Bottom5 Short Profit Lock V1 | ZEC | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 491,45169 | 493,00000 | 499,69161 | 734,72028 | 474,97185 | €1.491,62 | €2.983,24 | €50,02 | €-9,40 |
| Scanner Bottom5 Short Mfe Trail V1 | XRP | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1,02104 | 1,01310 | 1,01832 | 1,52645 | 0,99163 | €1.733,52 | €3.467,03 | €0,00 | €26,95 |
| Scanner Bottom5 Short Mfe Trail V1 | BTC | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 64070,44335 | 64026,93000 | 64993,05773 | 95785,31281 | 62225,21458 | €1.733,03 | €3.466,07 | €49,91 | €2,35 |
| Scanner Bottom5 Short Mfe Trail V1 | DOGE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,06982 | 0,07003 | 0,07082 | 0,10437 | 0,06781 | €1.738,95 | €3.477,91 | €50,08 | €-10,66 |
| Scanner Bottom5 Short Mfe Trail V1 | ZEC | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 491,45169 | 493,00000 | 499,69161 | 734,72028 | 474,97185 | €1.493,89 | €2.987,79 | €50,09 | €-9,41 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Main Side Regime Guard V1 | DOGE | SHORT | 2026-08-11T04:10:31+00:00 | 0,07008 | €5,48 | 0,11 | TIME_EXIT |
| Forza relativa 1H V1 | BEAT | SHORT | 2026-08-11T03:24:37+00:00 | 1,26224 | €101,52 | 2,19 | TARGET |
| Combo Trend Side Regime Guard V1 | BEAT | SHORT | 2026-08-11T03:24:37+00:00 | 1,26224 | €109,10 | 2,19 | TARGET |
| Combo Trend | BEAT | SHORT | 2026-08-11T03:24:37+00:00 | 1,26224 | €102,11 | 2,19 | TARGET |
| Scanner Bottom5 Short Profit Lock V1 | BEAT | SHORT | 2026-08-11T02:09:22+00:00 | 1,30340 | €98,25 | 1,99 | TARGET |
| Scanner Bottom5 Short Mfe Trail V1 | BEAT | SHORT | 2026-08-11T02:09:22+00:00 | 1,30340 | €98,40 | 1,99 | TARGET |
| Scanner Bottom 5 Short 1H | BEAT | SHORT | 2026-08-11T02:09:22+00:00 | 1,30340 | €97,49 | 1,99 | TARGET |
| Scanner Bottom20 Short | BEAT | SHORT | 2026-08-11T02:09:22+00:00 | 1,30340 | €97,66 | 1,99 | TARGET |
| Scanner Bottom15 Short | BEAT | SHORT | 2026-08-11T02:09:22+00:00 | 1,30340 | €97,66 | 1,99 | TARGET |
| Scanner Bottom10 Short | BEAT | SHORT | 2026-08-11T02:09:22+00:00 | 1,30340 | €97,66 | 1,99 | TARGET |
| Combo Adaptive Side Regime Guard V1 | BEAT | SHORT | 2026-08-11T02:09:22+00:00 | 1,30340 | €101,75 | 1,99 | TARGET |
| Combo Adaptive Partial 1R V1 | BEAT | SHORT | 2026-08-11T02:09:22+00:00 | 1,30340 | €93,09 | 1,99 | TARGET |

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

Generato: 2026-08-11 05:23 UTC


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

Segnali totali salvati: **102**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08-11 | BTC | 63.889,59 | +6 | +4 | +3 | +3 | +2 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-08-11 | DOGE | 0.06985 | +4 | +4 | +3 | +3 | 0 | 0 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-08-11 | SOL | 75,73 | +4 | +4 | +3 | +3 | 0 | 0 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-08-10 | BTC | 64.966,07 | +6 | +4 | +3 | +3 | +3 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-08-10 | DOGE | 0.06975 | +5 | +4 | +3 | +3 | 0 | 0 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-08-10 | SOL | 76,57 | +3 | +4 | +3 | +3 | -1 | 0 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-08-09 | BTC | 64.733,97 | +7 | +4 | +3 | +3 | +3 | 0 | 0 | ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA |
| 2026-08-09 | DOGE | 0.06994 | +4 | +4 | +3 | +3 | 0 | -1 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-08-09 | SOL | 75,92 | +4 | +4 | +3 | +3 | 0 | 0 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-08-08 | BTC | 64.965,57 | +8 | +4 | +3 | +3 | +3 | 0 | 0 | ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA |
| 2026-08-08 | DOGE | 0.07012 | +3 | +3 | +2 | +3 | -1 | 0 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-08-08 | SOL | 74,51 | +3 | +4 | +3 | +3 | -2 | 0 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 34 | 33 | 32 | 31 | 29 | 27 | 24 | 20 | 13 | 4 | 0 | 0 |
| SOL | 34 | 33 | 32 | 31 | 29 | 27 | 24 | 20 | 13 | 4 | 0 | 0 |
| DOGE | 34 | 33 | 32 | 31 | 29 | 27 | 24 | 20 | 13 | 4 | 0 | 0 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-07-13 | 30g | 2026-08-12 | domani |
| SOL | 2026-07-13 | 30g | 2026-08-12 | domani |
| DOGE | 2026-07-13 | 30g | 2026-08-12 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 31 | 48,39% | +0,02% | -0,02% | PRIMA CALIBRAZIONE |
| BTC | 2g | 30 | 46,67% | +0,13% | -0,03% | PRIMA CALIBRAZIONE |
| BTC | 3g | 29 | 41,38% | +0,06% | -0,18% | FEEDBACK RAPIDO |
| BTC | 5g | 27 | 33,33% | +0,30% | -0,17% | FEEDBACK RAPIDO |
| BTC | 7g | 25 | 48,00% | +0,51% | +0,08% | FEEDBACK RAPIDO |
| BTC | 10g | 22 | 45,45% | +0,63% | +0,21% | FEEDBACK RAPIDO |
| BTC | 14g | 18 | 50,00% | +0,19% | +0,00% | FEEDBACK RAPIDO |
| BTC | 21g | 12 | 33,33% | +0,17% | -0,18% | FEEDBACK RAPIDO |
| BTC | 30g | 4 | 100,00% | +1,41% | +1,41% | FEEDBACK RAPIDO |
| BTC | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 1g | 26 | 53,85% | +0,02% | -0,22% | FEEDBACK RAPIDO |
| SOL | 2g | 25 | 44,00% | +0,02% | -0,26% | FEEDBACK RAPIDO |
| SOL | 3g | 24 | 50,00% | +0,16% | -0,21% | FEEDBACK RAPIDO |
| SOL | 5g | 22 | 50,00% | -0,28% | -0,52% | FEEDBACK RAPIDO |
| SOL | 7g | 20 | 55,00% | -0,44% | -0,18% | FEEDBACK RAPIDO |
| SOL | 10g | 18 | 38,89% | -0,98% | -0,56% | FEEDBACK RAPIDO |
| SOL | 14g | 15 | 60,00% | -2,74% | +0,42% | FEEDBACK RAPIDO |
| SOL | 21g | 12 | 58,33% | -2,97% | -0,32% | FEEDBACK RAPIDO |
| SOL | 30g | 3 | 33,33% | -2,35% | -1,70% | FEEDBACK RAPIDO |
| SOL | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 1g | 31 | 41,94% | -0,04% | -0,06% | PRIMA CALIBRAZIONE |
| DOGE | 2g | 30 | 43,33% | -0,16% | -0,16% | PRIMA CALIBRAZIONE |
| DOGE | 3g | 29 | 41,38% | -0,37% | +0,02% | FEEDBACK RAPIDO |
| DOGE | 5g | 27 | 51,85% | -0,71% | +0,22% | FEEDBACK RAPIDO |
| DOGE | 7g | 26 | 57,69% | -1,06% | +0,64% | FEEDBACK RAPIDO |
| DOGE | 10g | 23 | 60,87% | -1,64% | +1,09% | FEEDBACK RAPIDO |
| DOGE | 14g | 19 | 68,42% | -2,68% | +2,16% | FEEDBACK RAPIDO |
| DOGE | 21g | 13 | 100,00% | -3,98% | +3,98% | FEEDBACK RAPIDO |
| DOGE | 30g | 4 | 100,00% | -4,73% | +4,73% | FEEDBACK RAPIDO |
| DOGE | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 31 | 48,39% | +0,02% | -0,02% | -0,30% | +0,54% | PRIMA CALIBRAZIONE |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 33 | 51,52% | +0,00% | +0,00% | -0,31% | +0,50% | PRIMA CALIBRAZIONE |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 33 | 51,52% | +0,00% | +0,00% | -0,31% | +0,50% | PRIMA CALIBRAZIONE |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 29 | 51,72% | -0,04% | -0,04% | -0,36% | +0,42% | FEEDBACK RAPIDO |
| BTC | 1g | Tecnico | CALIBRABILE | 28 | 35,71% | +0,17% | -0,39% | -0,16% | +0,67% | FEEDBACK RAPIDO |
| BTC | 1g | Classic technical | CALIBRABILE | 4 | 0,00% | +0,76% | -0,76% | +0,03% | +1,12% | FEEDBACK RAPIDO |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +2,00% | +2,00% | +1,48% | +2,25% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 30 | 46,67% | +0,13% | -0,03% | -0,34% | +0,79% | PRIMA CALIBRAZIONE |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 32 | 50,00% | +0,10% | +0,10% | -0,36% | +0,75% | PRIMA CALIBRAZIONE |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 32 | 50,00% | +0,10% | +0,10% | -0,36% | +0,75% | PRIMA CALIBRAZIONE |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 28 | 50,00% | +0,01% | +0,01% | -0,45% | +0,65% | FEEDBACK RAPIDO |
| BTC | 2g | Tecnico | CALIBRABILE | 27 | 48,15% | +0,31% | -0,29% | -0,13% | +0,96% | FEEDBACK RAPIDO |
| BTC | 2g | Classic technical | CALIBRABILE | 4 | 25,00% | +0,86% | -0,86% | +0,50% | +1,73% | FEEDBACK RAPIDO |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +3,18% | +3,18% | +3,05% | +3,89% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 29 | 41,38% | +0,06% | -0,18% | -1,28% | +1,70% | FEEDBACK RAPIDO |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 31 | 54,84% | +0,14% | +0,14% | -1,26% | +1,68% | PRIMA CALIBRAZIONE |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 31 | 54,84% | +0,14% | +0,14% | -1,26% | +1,68% | PRIMA CALIBRAZIONE |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 27 | 55,56% | +0,13% | +0,13% | -1,27% | +1,59% | FEEDBACK RAPIDO |
| BTC | 3g | Tecnico | CALIBRABILE | 26 | 38,46% | +0,54% | -0,27% | -0,97% | +2,01% | FEEDBACK RAPIDO |
| BTC | 3g | Classic technical | CALIBRABILE | 4 | 25,00% | +1,18% | -1,18% | -0,41% | +2,46% | FEEDBACK RAPIDO |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,88% | +1,88% | +1,44% | +4,24% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 27 | 33,33% | +0,30% | -0,17% | -1,99% | +2,29% | FEEDBACK RAPIDO |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 29 | 44,83% | +0,29% | +0,29% | -1,96% | +2,31% | FEEDBACK RAPIDO |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 29 | 44,83% | +0,29% | +0,29% | -1,96% | +2,31% | FEEDBACK RAPIDO |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 25 | 48,00% | +0,42% | +0,42% | -1,93% | +2,30% | FEEDBACK RAPIDO |
| BTC | 5g | Tecnico | CALIBRABILE | 24 | 45,83% | +0,58% | -0,44% | -1,65% | +2,64% | FEEDBACK RAPIDO |
| BTC | 5g | Classic technical | CALIBRABILE | 4 | 25,00% | +1,14% | -1,14% | -1,16% | +2,94% | FEEDBACK RAPIDO |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,16% | -0,16% | -0,37% | +4,24% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 25 | 48,00% | +0,51% | +0,08% | -2,23% | +2,76% | FEEDBACK RAPIDO |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 27 | 59,26% | +0,43% | +0,43% | -2,22% | +2,75% | FEEDBACK RAPIDO |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 27 | 59,26% | +0,43% | +0,43% | -2,22% | +2,75% | FEEDBACK RAPIDO |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 23 | 65,22% | +0,74% | +0,74% | -2,17% | +2,82% | FEEDBACK RAPIDO |
| BTC | 7g | Tecnico | CALIBRABILE | 22 | 36,36% | +1,04% | -0,64% | -1,86% | +3,13% | FEEDBACK RAPIDO |
| BTC | 7g | Classic technical | CALIBRABILE | 4 | 0,00% | +1,94% | -1,94% | -1,23% | +3,13% | FEEDBACK RAPIDO |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,77% | +1,77% | -0,79% | +4,24% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 22 | 45,45% | +0,63% | +0,21% | -2,72% | +3,05% | FEEDBACK RAPIDO |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 24 | 54,17% | +0,38% | +0,38% | -2,74% | +3,02% | FEEDBACK RAPIDO |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 24 | 54,17% | +0,38% | +0,38% | -2,74% | +3,02% | FEEDBACK RAPIDO |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 20 | 65,00% | +0,87% | +0,87% | -2,61% | +3,15% | FEEDBACK RAPIDO |
| BTC | 10g | Tecnico | CALIBRABILE | 19 | 36,84% | +0,78% | -0,18% | -2,37% | +3,50% | FEEDBACK RAPIDO |
| BTC | 10g | Classic technical | CALIBRABILE | 3 | 0,00% | +1,40% | -1,40% | -1,93% | +3,00% | FEEDBACK RAPIDO |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,43% | -0,43% | -2,30% | +4,24% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 18 | 50,00% | +0,19% | +0,00% | -3,10% | +3,58% | FEEDBACK RAPIDO |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 20 | 50,00% | +0,02% | +0,02% | -3,12% | +3,48% | FEEDBACK RAPIDO |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 20 | 50,00% | +0,02% | +0,02% | -3,12% | +3,48% | FEEDBACK RAPIDO |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 16 | 62,50% | +0,65% | +0,65% | -2,79% | +3,76% | FEEDBACK RAPIDO |
| BTC | 14g | Tecnico | CALIBRABILE | 16 | 50,00% | +0,27% | +0,04% | -2,71% | +3,94% | FEEDBACK RAPIDO |
| BTC | 14g | Classic technical | CALIBRABILE | 1 | 0,00% | +0,80% | -0,80% | -1,82% | +3,19% | FEEDBACK RAPIDO |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -2,25% | -2,25% | -3,05% | +4,24% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 12 | 33,33% | +0,17% | -0,18% | -2,86% | +4,69% | FEEDBACK RAPIDO |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 13 | 53,85% | +0,29% | +0,29% | -2,84% | +4,69% | FEEDBACK RAPIDO |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 13 | 53,85% | +0,29% | +0,29% | -2,84% | +4,69% | FEEDBACK RAPIDO |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 10 | 60,00% | +0,50% | +0,50% | -2,49% | +5,16% | FEEDBACK RAPIDO |
| BTC | 21g | Tecnico | CALIBRABILE | 11 | 9,09% | +0,49% | -0,70% | -2,60% | +4,94% | FEEDBACK RAPIDO |
| BTC | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,21% | +1,21% | -3,06% | +4,24% | FEEDBACK RAPIDO |
| BTC | 30g | Global confluence | BENCHMARK | 4 | 100,00% | +1,41% | +1,41% | -3,09% | +4,98% | FEEDBACK RAPIDO |
| BTC | 30g | Famiglia statistica | CALIBRABILE | 4 | 100,00% | +1,41% | +1,41% | -3,09% | +4,98% | FEEDBACK RAPIDO |
| BTC | 30g | Scanner grezzo | DIAGNOSTICO | 4 | 100,00% | +1,41% | +1,41% | -3,09% | +4,98% | FEEDBACK RAPIDO |
| BTC | 30g | Market regime grezzo | DIAGNOSTICO | 4 | 100,00% | +1,41% | +1,41% | -3,09% | +4,98% | FEEDBACK RAPIDO |
| BTC | 30g | Tecnico | CALIBRABILE | 3 | 33,33% | +1,43% | -1,36% | -3,03% | +5,05% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 31 | 41,94% | -0,04% | -0,06% | -0,50% | +0,60% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 33 | 54,55% | -0,16% | +0,21% | -0,63% | +0,46% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 33 | 54,55% | -0,16% | +0,21% | -0,63% | +0,46% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 31 | 54,84% | -0,05% | +0,10% | -0,54% | +0,59% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Tecnico | CALIBRABILE | 30 | 50,00% | -0,12% | +0,12% | -0,60% | +0,51% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Classic technical | CALIBRABILE | 22 | 40,91% | +0,18% | -0,18% | -0,35% | +0,74% | FEEDBACK RAPIDO |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 50,00% | +1,92% | +1,13% | +0,84% | +2,11% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 30 | 43,33% | -0,16% | -0,16% | -0,77% | +0,75% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 32 | 46,88% | -0,28% | +0,01% | -0,89% | +0,60% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 32 | 46,88% | -0,28% | +0,01% | -0,89% | +0,60% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 30 | 46,67% | -0,39% | +0,10% | -0,94% | +0,55% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Tecnico | CALIBRABILE | 30 | 60,00% | -0,30% | +0,30% | -0,91% | +0,61% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Classic technical | CALIBRABILE | 22 | 50,00% | +0,17% | -0,17% | -0,49% | +1,24% | FEEDBACK RAPIDO |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 50,00% | +3,12% | +2,46% | +2,21% | +3,52% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 29 | 41,38% | -0,37% | +0,02% | -1,90% | +1,81% | FEEDBACK RAPIDO |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 31 | 48,39% | -0,48% | -0,07% | -2,00% | +1,64% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 31 | 48,39% | -0,48% | -0,07% | -2,00% | +1,64% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 29 | 51,72% | -0,76% | +0,17% | -1,96% | +1,48% | FEEDBACK RAPIDO |
| DOGE | 3g | Tecnico | CALIBRABILE | 30 | 50,00% | -0,49% | +0,49% | -2,02% | +1,67% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Classic technical | CALIBRABILE | 21 | 38,10% | -0,08% | +0,08% | -1,88% | +2,28% | FEEDBACK RAPIDO |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +2,43% | +1,74% | +0,13% | +5,37% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 27 | 51,85% | -0,71% | +0,22% | -2,93% | +2,09% | FEEDBACK RAPIDO |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 29 | 48,28% | -0,81% | +0,08% | -2,98% | +1,94% | FEEDBACK RAPIDO |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 29 | 48,28% | -0,81% | +0,08% | -2,98% | +1,94% | FEEDBACK RAPIDO |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 27 | 48,15% | -0,83% | +0,05% | -3,01% | +1,75% | FEEDBACK RAPIDO |
| DOGE | 5g | Tecnico | CALIBRABILE | 28 | 64,29% | -0,83% | +0,83% | -3,03% | +1,94% | FEEDBACK RAPIDO |
| DOGE | 5g | Classic technical | CALIBRABILE | 20 | 55,00% | -0,45% | +0,45% | -2,87% | +2,58% | FEEDBACK RAPIDO |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +1,26% | +1,26% | +0,02% | +6,57% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 26 | 57,69% | -1,06% | +0,64% | -3,46% | +2,29% | FEEDBACK RAPIDO |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 27 | 55,56% | -1,17% | +0,41% | -3,58% | +2,12% | FEEDBACK RAPIDO |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 27 | 55,56% | -1,17% | +0,41% | -3,58% | +2,12% | FEEDBACK RAPIDO |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 25 | 56,00% | -1,18% | +0,36% | -3,65% | +1,93% | FEEDBACK RAPIDO |
| DOGE | 7g | Tecnico | CALIBRABILE | 27 | 66,67% | -1,17% | +1,17% | -3,58% | +2,12% | FEEDBACK RAPIDO |
| DOGE | 7g | Classic technical | CALIBRABILE | 20 | 55,00% | -1,01% | +1,01% | -3,42% | +2,68% | FEEDBACK RAPIDO |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +1,19% | +1,19% | -0,23% | +6,57% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 23 | 60,87% | -1,64% | +1,09% | -4,27% | +2,41% | FEEDBACK RAPIDO |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 24 | 54,17% | -1,74% | +0,90% | -4,37% | +2,22% | FEEDBACK RAPIDO |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 24 | 54,17% | -1,74% | +0,90% | -4,37% | +2,22% | FEEDBACK RAPIDO |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 22 | 54,55% | -1,82% | +0,90% | -4,45% | +2,01% | FEEDBACK RAPIDO |
| DOGE | 10g | Tecnico | CALIBRABILE | 24 | 70,83% | -1,74% | +1,74% | -4,37% | +2,22% | FEEDBACK RAPIDO |
| DOGE | 10g | Classic technical | CALIBRABILE | 20 | 65,00% | -1,32% | +1,32% | -4,00% | +2,72% | FEEDBACK RAPIDO |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +1,09% | +1,09% | -1,85% | +6,57% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 19 | 68,42% | -2,68% | +2,16% | -5,43% | +2,59% | FEEDBACK RAPIDO |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 20 | 70,00% | -2,76% | +1,93% | -5,50% | +2,36% | FEEDBACK RAPIDO |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 20 | 70,00% | -2,76% | +1,93% | -5,50% | +2,36% | FEEDBACK RAPIDO |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 18 | 72,22% | -2,89% | +1,97% | -5,69% | +2,12% | FEEDBACK RAPIDO |
| DOGE | 14g | Tecnico | CALIBRABILE | 20 | 80,00% | -2,76% | +2,76% | -5,50% | +2,36% | FEEDBACK RAPIDO |
| DOGE | 14g | Classic technical | CALIBRABILE | 17 | 76,47% | -2,45% | +2,45% | -5,18% | +2,87% | FEEDBACK RAPIDO |
| DOGE | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +0,46% | +0,46% | -1,85% | +6,57% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 13 | 100,00% | -3,98% | +3,98% | -6,48% | +2,40% | FEEDBACK RAPIDO |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 13 | 100,00% | -3,98% | +3,98% | -6,48% | +2,40% | FEEDBACK RAPIDO |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 13 | 100,00% | -3,98% | +3,98% | -6,48% | +2,40% | FEEDBACK RAPIDO |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 13 | 100,00% | -3,98% | +3,98% | -6,48% | +2,40% | FEEDBACK RAPIDO |
| DOGE | 21g | Tecnico | CALIBRABILE | 13 | 100,00% | -3,98% | +3,98% | -6,48% | +2,40% | FEEDBACK RAPIDO |
| DOGE | 21g | Classic technical | CALIBRABILE | 12 | 100,00% | -3,86% | +3,86% | -6,35% | +2,55% | FEEDBACK RAPIDO |
| DOGE | 30g | Global confluence | BENCHMARK | 4 | 100,00% | -4,73% | +4,73% | -7,38% | +2,68% | FEEDBACK RAPIDO |
| DOGE | 30g | Famiglia statistica | CALIBRABILE | 4 | 100,00% | -4,73% | +4,73% | -7,38% | +2,68% | FEEDBACK RAPIDO |
| DOGE | 30g | Scanner grezzo | DIAGNOSTICO | 4 | 100,00% | -4,73% | +4,73% | -7,38% | +2,68% | FEEDBACK RAPIDO |
| DOGE | 30g | Market regime grezzo | DIAGNOSTICO | 4 | 100,00% | -4,73% | +4,73% | -7,38% | +2,68% | FEEDBACK RAPIDO |
| DOGE | 30g | Tecnico | CALIBRABILE | 4 | 100,00% | -4,73% | +4,73% | -7,38% | +2,68% | FEEDBACK RAPIDO |
| DOGE | 30g | Classic technical | CALIBRABILE | 4 | 100,00% | -4,73% | +4,73% | -7,38% | +2,68% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 26 | 53,85% | +0,02% | -0,22% | -0,48% | +0,68% | FEEDBACK RAPIDO |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 29 | 62,07% | -0,29% | +0,01% | -0,75% | +0,33% | FEEDBACK RAPIDO |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 32 | 59,38% | -0,16% | -0,10% | -0,65% | +0,47% | PRIMA CALIBRAZIONE |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 27 | 55,56% | -0,11% | +0,04% | -0,69% | +0,49% | FEEDBACK RAPIDO |
| SOL | 1g | Tecnico | CALIBRABILE | 32 | 50,00% | -0,10% | -0,02% | -0,59% | +0,53% | PRIMA CALIBRAZIONE |
| SOL | 1g | Classic technical | CALIBRABILE | 21 | 47,62% | +0,04% | -0,04% | -0,54% | +0,59% | FEEDBACK RAPIDO |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 50,00% | +0,17% | +0,17% | -0,04% | +0,81% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 25 | 44,00% | +0,02% | -0,26% | -0,60% | +0,90% | FEEDBACK RAPIDO |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 28 | 50,00% | -0,26% | -0,09% | -0,93% | +0,47% | FEEDBACK RAPIDO |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 31 | 48,39% | -0,20% | -0,12% | -0,85% | +0,69% | PRIMA CALIBRAZIONE |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 26 | 46,15% | -0,18% | -0,14% | -0,85% | +0,71% | FEEDBACK RAPIDO |
| SOL | 2g | Tecnico | CALIBRABILE | 31 | 38,71% | -0,11% | -0,26% | -0,76% | +0,78% | PRIMA CALIBRAZIONE |
| SOL | 2g | Classic technical | CALIBRABILE | 21 | 47,62% | +0,02% | -0,02% | -0,52% | +0,51% | FEEDBACK RAPIDO |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 0,00% | -0,82% | -0,82% | -0,93% | +0,46% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 24 | 50,00% | +0,16% | -0,21% | -1,88% | +2,10% | FEEDBACK RAPIDO |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 27 | 48,15% | -0,31% | -0,03% | -2,24% | +1,72% | FEEDBACK RAPIDO |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 30 | 46,67% | -0,25% | -0,06% | -2,14% | +1,89% | PRIMA CALIBRAZIONE |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 25 | 48,00% | -0,19% | -0,26% | -2,07% | +1,93% | FEEDBACK RAPIDO |
| SOL | 3g | Tecnico | CALIBRABILE | 31 | 41,94% | -0,19% | -0,19% | -2,03% | +1,94% | PRIMA CALIBRAZIONE |
| SOL | 3g | Classic technical | CALIBRABILE | 21 | 42,86% | +0,13% | -0,13% | -1,91% | +1,82% | FEEDBACK RAPIDO |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -3,20% | -3,20% | -3,71% | +0,62% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 22 | 50,00% | -0,28% | -0,52% | -3,00% | +2,53% | FEEDBACK RAPIDO |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 25 | 52,00% | -0,53% | -0,25% | -3,29% | +2,19% | FEEDBACK RAPIDO |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 28 | 50,00% | -0,40% | -0,30% | -3,16% | +2,37% | FEEDBACK RAPIDO |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 23 | 47,83% | -0,66% | -0,35% | -3,18% | +2,31% | FEEDBACK RAPIDO |
| SOL | 5g | Tecnico | CALIBRABILE | 29 | 48,28% | -0,47% | -0,10% | -3,14% | +2,41% | FEEDBACK RAPIDO |
| SOL | 5g | Classic technical | CALIBRABILE | 20 | 55,00% | -0,06% | +0,06% | -2,79% | +2,42% | FEEDBACK RAPIDO |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -3,99% | -3,99% | -6,07% | +0,62% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 20 | 55,00% | -0,44% | -0,18% | -3,64% | +2,78% | FEEDBACK RAPIDO |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 23 | 60,87% | -0,85% | +0,15% | -3,92% | +2,49% | FEEDBACK RAPIDO |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 26 | 61,54% | -0,76% | +0,15% | -3,78% | +2,65% | FEEDBACK RAPIDO |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 21 | 52,38% | -0,57% | -0,47% | -3,80% | +2,60% | FEEDBACK RAPIDO |
| SOL | 7g | Tecnico | CALIBRABILE | 27 | 40,74% | -0,71% | -0,04% | -3,76% | +2,69% | FEEDBACK RAPIDO |
| SOL | 7g | Classic technical | CALIBRABILE | 19 | 47,37% | -0,37% | +0,37% | -3,44% | +2,85% | FEEDBACK RAPIDO |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -6,33% | -6,33% | -6,71% | +0,62% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 18 | 38,89% | -0,98% | -0,56% | -4,38% | +3,05% | FEEDBACK RAPIDO |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 20 | 45,00% | -1,17% | -0,09% | -4,89% | +2,56% | FEEDBACK RAPIDO |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 23 | 43,48% | -1,04% | -0,05% | -4,70% | +2,74% | FEEDBACK RAPIDO |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 18 | 33,33% | -0,72% | -1,03% | -4,76% | +2,70% | FEEDBACK RAPIDO |
| SOL | 10g | Tecnico | CALIBRABILE | 24 | 62,50% | -1,14% | +0,94% | -4,70% | +2,77% | FEEDBACK RAPIDO |
| SOL | 10g | Classic technical | CALIBRABILE | 16 | 68,75% | -1,08% | +1,08% | -4,56% | +2,99% | FEEDBACK RAPIDO |
| SOL | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -5,36% | -5,36% | -7,47% | +0,62% | FEEDBACK RAPIDO |
| SOL | 10g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 14g | Global confluence | BENCHMARK | 15 | 60,00% | -2,74% | +0,42% | -5,54% | +2,99% | FEEDBACK RAPIDO |
| SOL | 14g | Famiglia statistica | CALIBRABILE | 16 | 68,75% | -2,04% | +0,30% | -5,91% | +2,57% | FEEDBACK RAPIDO |
| SOL | 14g | Scanner grezzo | DIAGNOSTICO | 19 | 73,68% | -2,21% | +0,74% | -5,59% | +2,79% | FEEDBACK RAPIDO |
| SOL | 14g | Market regime grezzo | DIAGNOSTICO | 14 | 35,71% | -1,86% | -1,61% | -5,55% | +2,76% | FEEDBACK RAPIDO |
| SOL | 14g | Tecnico | CALIBRABILE | 20 | 55,00% | -2,30% | +1,28% | -5,66% | +2,82% | FEEDBACK RAPIDO |
| SOL | 14g | Classic technical | CALIBRABILE | 12 | 66,67% | -1,88% | +1,88% | -5,83% | +3,15% | FEEDBACK RAPIDO |
| SOL | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -5,80% | -5,80% | -9,62% | +0,62% | FEEDBACK RAPIDO |
| SOL | 14g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 21g | Global confluence | BENCHMARK | 12 | 58,33% | -2,97% | -0,32% | -7,03% | +3,14% | FEEDBACK RAPIDO |
| SOL | 21g | Famiglia statistica | CALIBRABILE | 9 | 77,78% | -3,66% | +1,90% | -7,32% | +2,66% | FEEDBACK RAPIDO |
| SOL | 21g | Scanner grezzo | DIAGNOSTICO | 12 | 83,33% | -3,43% | +2,11% | -7,01% | +2,97% | FEEDBACK RAPIDO |
| SOL | 21g | Market regime grezzo | DIAGNOSTICO | 8 | 25,00% | -3,82% | -1,69% | -7,18% | +2,78% | FEEDBACK RAPIDO |
| SOL | 21g | Tecnico | CALIBRABILE | 13 | 61,54% | -3,11% | -0,06% | -7,01% | +3,02% | FEEDBACK RAPIDO |
| SOL | 21g | Classic technical | CALIBRABILE | 5 | 80,00% | -1,15% | +1,15% | -6,51% | +4,11% | FEEDBACK RAPIDO |
| SOL | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -3,18% | -3,18% | -9,62% | +0,62% | FEEDBACK RAPIDO |
| SOL | 21g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | FEEDBACK RAPIDO |
| SOL | 30g | Global confluence | BENCHMARK | 3 | 33,33% | -2,35% | -1,70% | -8,70% | +2,16% | FEEDBACK RAPIDO |
| SOL | 30g | Famiglia statistica | CALIBRABILE | 3 | 100,00% | -2,59% | +2,59% | -8,66% | +2,20% | FEEDBACK RAPIDO |
| SOL | 30g | Scanner grezzo | DIAGNOSTICO | 4 | 100,00% | -2,34% | +2,34% | -8,78% | +2,00% | FEEDBACK RAPIDO |
| SOL | 30g | Market regime grezzo | DIAGNOSTICO | 3 | 33,33% | -2,35% | -1,70% | -8,70% | +2,16% | FEEDBACK RAPIDO |
| SOL | 30g | Tecnico | CALIBRABILE | 4 | 0,00% | -2,34% | -2,34% | -8,78% | +2,00% | FEEDBACK RAPIDO |
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

Generato: 2026-08-11 05:23 UTC

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
| BTC | 34 | PRIMA CALIBRAZIONE | 33 | 3 | 0 | 0 | Famiglia statistica | 1g | 51,52% | +0,00% | prima calibrazione possibile, solo modifiche leggere |
| SOL | 34 | PRIMA CALIBRAZIONE | 32 | 3 | 0 | 0 | Tecnico | 1g | 50,00% | -0,02% | prima calibrazione possibile, solo modifiche leggere |
| DOGE | 34 | PRIMA CALIBRAZIONE | 33 | 6 | 0 | 0 | Famiglia statistica | 1g | 54,55% | +0,21% | prima calibrazione possibile, solo modifiche leggere |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Classic technical | 4 | 0,00% | -0,76% | +0,76% | +0,03% | +1,12% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Famiglia statistica | 33 | 51,52% | +0,00% | +0,00% | -0,31% | +0,50% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 1g | BREVE | Microstruttura exchange | 1 | 100,00% | +2,00% | +2,00% | +1,48% | +2,25% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 28 | 35,71% | -0,39% | +0,17% | -0,16% | +0,67% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Classic technical | 4 | 25,00% | -0,86% | +0,86% | +0,50% | +1,73% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Famiglia statistica | 32 | 50,00% | +0,10% | +0,10% | -0,36% | +0,75% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 2g | BREVE | Microstruttura exchange | 1 | 100,00% | +3,18% | +3,18% | +3,05% | +3,89% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 27 | 48,15% | -0,29% | +0,31% | -0,13% | +0,96% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Classic technical | 4 | 25,00% | -1,18% | +1,18% | -0,41% | +2,46% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Famiglia statistica | 31 | 54,84% | +0,14% | +0,14% | -1,26% | +1,68% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 3g | BREVE | Microstruttura exchange | 1 | 100,00% | +1,88% | +1,88% | +1,44% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 26 | 38,46% | -0,27% | +0,54% | -0,97% | +2,01% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Classic technical | 4 | 25,00% | -1,14% | +1,14% | -1,16% | +2,94% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 29 | 44,83% | +0,29% | +0,29% | -1,96% | +2,31% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -0,16% | -0,16% | -0,37% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 24 | 45,83% | -0,44% | +0,58% | -1,65% | +2,64% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Classic technical | 4 | 0,00% | -1,94% | +1,94% | -1,23% | +3,13% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 27 | 59,26% | +0,43% | +0,43% | -2,22% | +2,75% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Microstruttura exchange | 1 | 100,00% | +1,77% | +1,77% | -0,79% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 22 | 36,36% | -0,64% | +1,04% | -1,86% | +3,13% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Classic technical | 3 | 0,00% | -1,40% | +1,40% | -1,93% | +3,00% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 24 | 54,17% | +0,38% | +0,38% | -2,74% | +3,02% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -0,43% | -0,43% | -2,30% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 19 | 36,84% | -0,18% | +0,78% | -2,37% | +3,50% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Classic technical | 1 | 0,00% | -0,80% | +0,80% | -1,82% | +3,19% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Famiglia statistica | 20 | 50,00% | +0,02% | +0,02% | -3,12% | +3,48% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Microstruttura exchange | 1 | 0,00% | -2,25% | -2,25% | -3,05% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 16 | 50,00% | +0,04% | +0,27% | -2,71% | +3,94% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Famiglia statistica | 13 | 53,85% | +0,29% | +0,29% | -2,84% | +4,69% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Microstruttura exchange | 1 | 100,00% | +1,21% | +1,21% | -3,06% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Tecnico | 11 | 9,09% | -0,70% | +0,49% | -2,60% | +4,94% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Famiglia statistica | 4 | 100,00% | +1,41% | +1,41% | -3,09% | +4,98% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Tecnico | 3 | 33,33% | -1,36% | +1,43% | -3,03% | +5,05% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 22 | 40,91% | -0,18% | +0,18% | -0,35% | +0,74% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Famiglia statistica | 33 | 54,55% | +0,21% | -0,16% | -0,63% | +0,46% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 1g | BREVE | Microstruttura exchange | 4 | 50,00% | +1,13% | +1,92% | +0,84% | +2,11% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 30 | 50,00% | +0,12% | -0,12% | -0,60% | +0,51% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Classic technical | 22 | 50,00% | -0,17% | +0,17% | -0,49% | +1,24% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Famiglia statistica | 32 | 46,88% | +0,01% | -0,28% | -0,89% | +0,60% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Microstruttura exchange | 4 | 50,00% | +2,46% | +3,12% | +2,21% | +3,52% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 30 | 60,00% | +0,30% | -0,30% | -0,91% | +0,61% | PESO OK | 0,0 | MEDIA |
| DOGE | 3g | BREVE | Classic technical | 21 | 38,10% | +0,08% | -0,08% | -1,88% | +2,28% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Famiglia statistica | 31 | 48,39% | -0,07% | -0,48% | -2,00% | +1,64% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 3g | BREVE | Microstruttura exchange | 3 | 66,67% | +1,74% | +2,43% | +0,13% | +5,37% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 30 | 50,00% | +0,49% | -0,49% | -2,02% | +1,67% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 5g | SETTIMANALE | Classic technical | 20 | 55,00% | +0,45% | -0,45% | -2,87% | +2,58% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 29 | 48,28% | +0,08% | -0,81% | -2,98% | +1,94% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Microstruttura exchange | 2 | 100,00% | +1,26% | +1,26% | +0,02% | +6,57% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 28 | 64,29% | +0,83% | -0,83% | -3,03% | +1,94% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Classic technical | 20 | 55,00% | +1,01% | -1,01% | -3,42% | +2,68% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 27 | 55,56% | +0,41% | -1,17% | -3,58% | +2,12% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Microstruttura exchange | 2 | 100,00% | +1,19% | +1,19% | -0,23% | +6,57% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 27 | 66,67% | +1,17% | -1,17% | -3,58% | +2,12% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Classic technical | 20 | 65,00% | +1,32% | -1,32% | -4,00% | +2,72% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 24 | 54,17% | +0,90% | -1,74% | -4,37% | +2,22% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Microstruttura exchange | 2 | 100,00% | +1,09% | +1,09% | -1,85% | +6,57% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 24 | 70,83% | +1,74% | -1,74% | -4,37% | +2,22% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Classic technical | 17 | 76,47% | +2,45% | -2,45% | -5,18% | +2,87% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Famiglia statistica | 20 | 70,00% | +1,93% | -2,76% | -5,50% | +2,36% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Microstruttura exchange | 2 | 100,00% | +0,46% | +0,46% | -1,85% | +6,57% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 20 | 80,00% | +2,76% | -2,76% | -5,50% | +2,36% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Classic technical | 12 | 100,00% | +3,86% | -3,86% | -6,35% | +2,55% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Famiglia statistica | 13 | 100,00% | +3,98% | -3,98% | -6,48% | +2,40% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Tecnico | 13 | 100,00% | +3,98% | -3,98% | -6,48% | +2,40% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Classic technical | 4 | 100,00% | +4,73% | -4,73% | -7,38% | +2,68% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Famiglia statistica | 4 | 100,00% | +4,73% | -4,73% | -7,38% | +2,68% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Tecnico | 4 | 100,00% | +4,73% | -4,73% | -7,38% | +2,68% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Classic technical | 21 | 47,62% | -0,04% | +0,04% | -0,54% | +0,59% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Famiglia statistica | 29 | 62,07% | +0,01% | -0,29% | -0,75% | +0,33% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 2 | 50,00% | +0,17% | +0,17% | -0,04% | +0,81% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 32 | 50,00% | -0,02% | -0,10% | -0,59% | +0,53% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Classic technical | 21 | 47,62% | -0,02% | +0,02% | -0,52% | +0,51% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Famiglia statistica | 28 | 50,00% | -0,09% | -0,26% | -0,93% | +0,47% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Microstruttura exchange | 2 | 0,00% | -0,82% | -0,82% | -0,93% | +0,46% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 31 | 38,71% | -0,26% | -0,11% | -0,76% | +0,78% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 3g | BREVE | Classic technical | 21 | 42,86% | -0,13% | +0,13% | -1,91% | +1,82% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Famiglia statistica | 27 | 48,15% | -0,03% | -0,31% | -2,24% | +1,72% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Microstruttura exchange | 1 | 0,00% | -3,20% | -3,20% | -3,71% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 31 | 41,94% | -0,19% | -0,19% | -2,03% | +1,94% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 5g | SETTIMANALE | Classic technical | 20 | 55,00% | +0,06% | -0,06% | -2,79% | +2,42% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 25 | 52,00% | -0,25% | -0,53% | -3,29% | +2,19% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -3,99% | -3,99% | -6,07% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 29 | 48,28% | -0,10% | -0,47% | -3,14% | +2,41% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Classic technical | 19 | 47,37% | +0,37% | -0,37% | -3,44% | +2,85% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 23 | 60,87% | +0,15% | -0,85% | -3,92% | +2,49% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -6,33% | -6,33% | -6,71% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 27 | 40,74% | -0,04% | -0,71% | -3,76% | +2,69% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Classic technical | 16 | 68,75% | +1,08% | -1,08% | -4,56% | +2,99% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 20 | 45,00% | -0,09% | -1,17% | -4,89% | +2,56% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -5,36% | -5,36% | -7,47% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 24 | 62,50% | +0,94% | -1,14% | -4,70% | +2,77% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Classic technical | 12 | 66,67% | +1,88% | -1,88% | -5,83% | +3,15% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Famiglia statistica | 16 | 68,75% | +0,30% | -2,04% | -5,91% | +2,57% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Frattale SOL | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Microstruttura exchange | 1 | 0,00% | -5,80% | -5,80% | -9,62% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Tecnico | 20 | 55,00% | +1,28% | -2,30% | -5,66% | +2,82% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Classic technical | 5 | 80,00% | +1,15% | -1,15% | -6,51% | +4,11% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Famiglia statistica | 9 | 77,78% | +1,90% | -3,66% | -7,32% | +2,66% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Frattale SOL | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Microstruttura exchange | 1 | 0,00% | -3,18% | -3,18% | -9,62% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Tecnico | 13 | 61,54% | -0,06% | -3,11% | -7,01% | +3,02% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Famiglia statistica | 3 | 100,00% | +2,59% | -2,59% | -8,66% | +2,20% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Frattale SOL | 1 | 0,00% | -4,50% | -4,50% | -9,39% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Tecnico | 4 | 0,00% | -2,34% | -2,34% | -8,78% | +2,00% | OSSERVA | 0,0 | BASSA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 31 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 31 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 33 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Classic technical | 12 | 16,67% | -0,93% |
| BTC | BREVE | Famiglia statistica | 96 | 52,08% | +0,08% |
| BTC | BREVE | Microstruttura exchange | 3 | 100,00% | +2,36% |
| BTC | BREVE | Tecnico | 81 | 40,74% | -0,32% |
| BTC | SETTIMANALE | Classic technical | 11 | 9,09% | -1,50% |
| BTC | SETTIMANALE | Famiglia statistica | 80 | 52,50% | +0,36% |
| BTC | SETTIMANALE | Microstruttura exchange | 3 | 33,33% | +0,39% |
| BTC | SETTIMANALE | Tecnico | 65 | 40,00% | -0,43% |
| BTC | SWING | Classic technical | 1 | 0,00% | -0,80% |
| BTC | SWING | Famiglia statistica | 33 | 51,52% | +0,13% |
| BTC | SWING | Microstruttura exchange | 2 | 50,00% | -0,52% |
| BTC | SWING | Tecnico | 27 | 33,33% | -0,26% |
| BTC | MEDIO | Famiglia statistica | 4 | 100,00% | +1,41% |
| BTC | MEDIO | Tecnico | 3 | 33,33% | -1,36% |
| DOGE | BREVE | Classic technical | 65 | 43,08% | -0,09% |
| DOGE | BREVE | Famiglia statistica | 96 | 50,00% | +0,05% |
| DOGE | BREVE | Microstruttura exchange | 11 | 54,55% | +1,78% |
| DOGE | BREVE | Tecnico | 90 | 53,33% | +0,31% |
| DOGE | SETTIMANALE | Classic technical | 60 | 58,33% | +0,92% |
| DOGE | SETTIMANALE | Famiglia statistica | 80 | 52,50% | +0,44% |
| DOGE | SETTIMANALE | Microstruttura exchange | 6 | 100,00% | +1,18% |
| DOGE | SETTIMANALE | Tecnico | 79 | 67,09% | +1,22% |
| DOGE | SWING | Classic technical | 29 | 86,21% | +3,03% |
| DOGE | SWING | Famiglia statistica | 33 | 81,82% | +2,74% |
| DOGE | SWING | Microstruttura exchange | 2 | 100,00% | +0,46% |
| DOGE | SWING | Tecnico | 33 | 87,88% | +3,24% |
| DOGE | MEDIO | Classic technical | 4 | 100,00% | +4,73% |
| DOGE | MEDIO | Famiglia statistica | 4 | 100,00% | +4,73% |
| DOGE | MEDIO | Tecnico | 4 | 100,00% | +4,73% |
| SOL | BREVE | Classic technical | 63 | 46,03% | -0,06% |
| SOL | BREVE | Famiglia statistica | 84 | 53,57% | -0,04% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 5 | 20,00% | -0,90% |
| SOL | BREVE | Tecnico | 94 | 43,62% | -0,15% |
| SOL | SETTIMANALE | Classic technical | 55 | 56,36% | +0,46% |
| SOL | SETTIMANALE | Famiglia statistica | 68 | 52,94% | -0,07% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Microstruttura exchange | 3 | 0,00% | -5,22% |
| SOL | SETTIMANALE | Tecnico | 80 | 50,00% | +0,23% |
| SOL | SWING | Classic technical | 17 | 70,59% | +1,67% |
| SOL | SWING | Famiglia statistica | 25 | 72,00% | +0,88% |
| SOL | SWING | Frattale SOL | 2 | 0,00% | -3,49% |
| SOL | SWING | Microstruttura exchange | 2 | 0,00% | -4,49% |
| SOL | SWING | Tecnico | 33 | 57,58% | +0,76% |
| SOL | MEDIO | Famiglia statistica | 3 | 100,00% | +2,59% |
| SOL | MEDIO | Frattale SOL | 1 | 0,00% | -4,50% |
| SOL | MEDIO | Tecnico | 4 | 0,00% | -2,34% |

## Aree ancora in attesa

| Asset | Famiglia | Righe senza controlli | Stato |
| --- | --- | --- | --- |
| BTC | BREVE | 3 | in attesa di controlli maturati |
| BTC | SETTIMANALE | 3 | in attesa di controlli maturati |
| BTC | SWING | 3 | in attesa di controlli maturati |
| BTC | MEDIO | 13 | in attesa di controlli maturati |
| SOL | MEDIO | 12 | in attesa di controlli maturati |
| DOGE | BREVE | 3 | in attesa di controlli maturati |
| DOGE | SETTIMANALE | 3 | in attesa di controlli maturati |
| DOGE | SWING | 3 | in attesa di controlli maturati |
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
| BTC     |         34 |               4 |          30 | RACCOLTA DATI | 0,00%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| SOL     |         34 |               4 |          30 | RACCOLTA DATI | 0,00%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| DOGE    |         34 |               4 |          30 | RACCOLTA DATI | 0,00%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |

Regola: sotto 60 controlli osserva soltanto; da 100+ controlli può diventare utile per correggere rischio spot/leva nel Decision Report.

## Ultima lettura rapida

| Asset   | Rischio spot   | Rischio leva   | Nota leva                                                               |
|:--------|:---------------|:---------------|:------------------------------------------------------------------------|
| BTC     | BASSO          | ALTO           | leva da limitare; 2x/3x solo con invalidazione chiara                   |
| SOL     | BASSO          | ALTO           | leva da limitare; 2x/3x solo con invalidazione chiara                   |
| DOGE    | MEDIO          | MOLTO ALTO     | spot preferibile; leva molto pericolosa anche 2x/3x senza margine largo |
<!-- RISK_CALIBRATION_END -->

</details>
<!-- COMPACT_SECTION_END:risk_calibration -->

<!-- COMPACT_SECTION_START:global_confluence -->
<details open>
<summary><strong>🌐 Global Confluence — quadro finale</strong></summary>

<!-- GLOBAL_CONFLUENCE_START -->
# Sintesi finale di confluenza

Generato: 2026-08-11 05:22 UTC


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
| BTC | +6 | MODERATAMENTE POSITIVA | Costruttivo prudente | MEDIA | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE | Prima resistenza sopra 66.910; conferma del doppio minimo sopra 66.910. | Sotto 62.227 il quadro tecnico peggiora. |
| SOL | +4 | MODERATAMENTE POSITIVA | Costruttivo prudente | MEDIA | HOLD / TRANCHE PICCOLE, NO LEVA | conferma del doppio minimo sopra 83,81; nuova conferma tecnica sopra 78,73; milestone analogiche 79,78 / 93,47, valide soltanto se rientra anche il gap frattale. | Allarmi sotto 71,42 / 70,69 / 62,19. |
| DOGE | +4 | MODERATAMENTE POSITIVA | Costruttivo prudente | MEDIA | SOLO TRANCHE PICCOLE / NO LEVA | Sopra 0.07117 migliora; sopra 0.06966 viene invalidato il pattern ribassista dominante. | Sotto 0.06835 il rischio ribassista aumenta. |

## Punteggi per modulo

| Asset | Scanner grezzo | Market grezzo | Famiglia statistica | Scanner path | Tecnico | Classic tech | Frattale SOL | Fractal path | RSI top-cycle | Lifecycle EMA | Exchange flow | Futures | Daily change | Totale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +3 | +3 | +4 | 0 | +2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | +6 |
| SOL | +3 | +3 | +4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | +4 |
| DOGE | +3 | +3 | +4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | +4 |

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

- Famiglia statistica: **+4** — Scanner grezzo +3, Market Regime grezzo +3, match regime 16. Scanner e regime concordi con almeno 10 match: bonus massimo di 1 punto. Punteggio contato nel Global: +4.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **+3** — Casi positivi 80,00%, return centrale 30g +9,15%. Direzione scanner: SALITA. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **+3** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 16, positivi 30g 87,50%, return p50 +9,03%.
- Scanner path: **0** — Controlli disponibili 32. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **+2** — Score tecnico 4/12, verdetto costruttivo ma non confermato, trend misto, struttura rialzista con massimi e minimi crescenti, divergenza nessuna, Wyckoff possibile accumulazione, pattern score 0 (rialzista Doppio minimo / CANDIDATO; ribassista Doppio massimo / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **0** — Score classico -4/12, verdetto DEBOLE / NON CONFERMATO, stage STAGE 4 / MARKDOWN, struttura COMPRESSIONE / TRIANGOLO POSSIBILE, Wyckoff ACCUMULO POSSIBILE / RANGE BASSO, volatilità locale BASSO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Non applicabile a questo asset.
- Fractal path: **0** — Non applicabile a questo asset.
- RSI top-cycle: **0** — Non applicabile a questo asset.
- Lifecycle EMA: **0** — Non applicabile a questo asset.
- Exchange flow: **0** — Flow +1.75, derivati -1.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +0.00; exchange 3/3, copertura 100%, consenso bull 1, bear 1, divergenze 1, campioni 4h 9 su 4.00h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias MISTA / NEUTRALE; confidenza BASSA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Rischio sotto, forza 2/5.
- Daily change: **0** — BTC: nessun cambiamento forte in peggioramento rispetto a ieri.

Conferme: Prima resistenza sopra 66.910; conferma del doppio minimo sopra 66.910.

Invalidazioni: Sotto 62.227 il quadro tecnico peggiora.

### SOL

- Confluenza: **MODERATAMENTE POSITIVA**
- Bias: **Costruttivo prudente**
- Punteggio finale: **+4**
- Affidabilità: **MEDIA**
- Azione coerente: **HOLD / TRANCHE PICCOLE, NO LEVA**

SOL ha una confluenza costruttiva, ma va ancora trattato come setup anticipato. La conferma vera arriva solo sopra le resistenze tecniche e con rientro del gap frattale. Il modulo lifecycle/EMA200 resta utile come contesto, ma non aumenta il punteggio Global.

Dettaglio moduli:

- Famiglia statistica: **+4** — Scanner grezzo +3, Market Regime grezzo +3, match regime 11. Scanner e regime concordi con almeno 10 match: bonus massimo di 1 punto. Punteggio contato nel Global: +4.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **+3** — Casi positivi 72,50%, return centrale 30g +11,48%. Direzione scanner: SALITA. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **+3** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 11, positivi 30g 100,00%, return p50 +16,07%.
- Scanner path: **0** — Controlli disponibili 32. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **0** — Score tecnico 0/12, verdetto neutrale / misto, trend misto, struttura ribassista con massimi e minimi decrescenti, divergenza ribassista nascosta rsi, Wyckoff markdown / fase ribassista, pattern score 0 (rialzista Doppio minimo / CANDIDATO; ribassista Doppio massimo / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **0** — Score classico -3/12, verdetto DEBOLE / NON CONFERMATO, stage STAGE 4 / MARKDOWN, struttura MASSIMI E MINIMI DECRESCENTI, Wyckoff ACCUMULO POSSIBILE / RANGE BASSO, volatilità locale BASSO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Verdetto ANALOGIA DEBOLE / SCENARIO SECONDARIO, somiglianza strutturale +57,11%, aderenza live +69,55%, errore live +15,23%, gap corrente -16,26%, peso operativo 0, tracking STRUTTURA STABILE, fase FRATTALE SOLO DI CONTESTO, rischio ALTO.
- Fractal path: **0** — Controlli disponibili 28, ma percorso ancorato non aderente: gap -16,26%, errore live +15,23%. Peso 0.
- RSI top-cycle: **0** — Rischio top-cycle RSI: BASSO.
- Lifecycle EMA: **0** — Contesto non pesato nel Global. Lifecycle score 4, bias SQUEEZE SETUP MODERATO, EMA200 111,66 $, upside EMA200 +47,36%, gap EMA50/EMA200 -5,53%, hit EMA200 12w +36,67%, trend STABILE / DA CONFERMARE. Peso Global forzato a 0.
- Exchange flow: **0** — Flow +1.75, derivati +0.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +0.50; exchange 3/3, copertura 100%, consenso bull 1, bear 1, divergenze 0, campioni 4h 9 su 4.00h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias LEGGERMENTE POSITIVA / NON PESATA; confidenza BASSA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Rischio sotto, forza 2/5.
- Daily change: **0** — SOL: nessun cambiamento forte in peggioramento rispetto a ieri.

Conferme: conferma del doppio minimo sopra 83,81; nuova conferma tecnica sopra 78,73; milestone analogiche 79,78 / 93,47, valide soltanto se rientra anche il gap frattale.

Invalidazioni: Allarmi sotto 71,42 / 70,69 / 62,19.

### DOGE

- Confluenza: **MODERATAMENTE POSITIVA**
- Bias: **Costruttivo prudente**
- Punteggio finale: **+4**
- Affidabilità: **MEDIA**
- Azione coerente: **SOLO TRANCHE PICCOLE / NO LEVA**

DOGE non ha ancora una confluenza pulita. Serve conferma tecnica prima di trattarlo come asset forte.

Dettaglio moduli:

- Famiglia statistica: **+4** — Scanner grezzo +3, Market Regime grezzo +3, match regime 16. Scanner e regime concordi con almeno 10 match: bonus massimo di 1 punto. Punteggio contato nel Global: +4.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **+3** — Casi positivi 72,50%, return centrale 30g +15,50%. Direzione scanner: SALITA. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **+3** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 16, positivi 30g 87,50%, return p50 +21,42%.
- Scanner path: **0** — Controlli disponibili 32. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **0** — Score tecnico 0/12, verdetto neutrale / misto, trend ribassista, struttura compressione / triangolo, divergenza nessuna, Wyckoff possibile accumulazione, pattern score 0 (rialzista Doppio minimo / CANDIDATO; ribassista Adam and Eve Top / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **0** — Score classico -2/12, verdetto DEBOLE / NON CONFERMATO, stage STAGE 4 / MARKDOWN, struttura COMPRESSIONE / TRIANGOLO POSSIBILE, Wyckoff SPRING / TEST POSSIBILE, volatilità locale BASSO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Non applicabile a questo asset.
- Fractal path: **0** — Non applicabile a questo asset.
- RSI top-cycle: **0** — Non applicabile a questo asset.
- Lifecycle EMA: **0** — Non applicabile a questo asset.
- Exchange flow: **0** — Flow +0.75, derivati +0.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +0.00; exchange 3/3, copertura 100%, consenso bull 0, bear 3, divergenze 0, campioni 4h 9 su 4.00h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias MISTA / NEUTRALE; confidenza BASSA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Rischio sotto, forza 2/5.
- Daily change: **0** — DOGE: nessun cambiamento forte in peggioramento rispetto a ieri.

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

Generato: 2026-08-11 05:22 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [btc_macro_cycle_report.md](btc_macro_cycle_report.md)

Questo modulo descrive il contesto macro di Bitcoin. Non genera entrate tattiche, non autorizza leva e pesa **0** nel Global Confluence.

## Sintesi

| Voce | Valore | Lettura |
| --- | --- | --- |
| Prezzo BTC | 63.890 $ | prezzo corrente |
| Power Law centrale | 123.608 $ | deviazione -48,31% |
| Banda p10-p90 | 76.654 $ / 310.646 $ | SOTTO LA BANDA P10 |
| Percentile residuo | 0,99% | posizione storica nel corridoio |
| Esponente β | 5,8234 | R² log-log 91,95% |
| Stabilità β | BASSA | range 1,3135 cambiando finestra |
| Ultimo halving | 2024-04-19 | 844 giorni fa |
| Fase ciclo | 57,77% | percentuale indicativa del ciclo quadriennale |
| Peso Global | 0 | CONTESTO MACRO / DIAGNOSTICO |

La Power Law viene trattata come regressione empirica, non come legge fisica. Il report mostra quanto cambia l'esponente usando finestre iniziali diverse e la confronta con il benchmark ingenuo 'prezzo invariato'.

## Bitcoin Power Law

- Campione: 2014-09-17 → 2026-08-11 (4346 osservazioni)
- Formula stimata: prezzo ≈ exp(-39.2178) × giorni^5.8234
- Prezzo centrale oggi: **123.608 $**
- Posizione corrente: **SOTTO LA BANDA P10**, percentile 0,99%
- Scarto dal centro: **-48,31%**

![Bitcoin Power Law](btc_power_law_chart.png)

![Bitcoin Power Law log-log](btc_power_law_loglog_chart.png)

### Stabilità dell'esponente

| Inizio campione | β | R² log-log |
| --- | --- | --- |
| 2014 | 5,8234 | 91,95% |
| 2015 | 5,9079 | 91,51% |
| 2016 | 5,5946 | 87,74% |
| 2017 | 4,8646 | 82,86% |
| 2018 | 4,5944 | 78,33% |

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
| 2012-11-28 → 2016-07-09 | 2014-12-30 | -24,85% | -20,34% | -19,86% | +37,29% |
| 2016-07-09 → 2020-05-11 | 2018-09-27 | -2,94% | -42,23% | -40,31% | +23,59% |
| 2020-05-11 → 2024-04-19 | 2022-08-20 | -7,66% | -21,11% | +11,61% | +23,73% |

Campione molto piccolo: questi rendimenti sono contesto di ciclo, non probabilità affidabili.

## SOL/BTC e DOGE/BTC dentro il tempo Bitcoin

![Altcoin nel ciclo BTC](alt_btc_cycle_spirals.png)

| Asset | Coppia | Forza vs BTC | Score raw | Candidato | 30g | Peso Global |
| --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | RELATIVA MISTA / NON CONFERMATA | -3 | 0 | -1.6016623142149133 | 0 |
| DOGE | DOGE/BTC | SOTTOPERFORMA BTC | -4 | -1 | -4.8010438730600065 | 0 |

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

Generato: 2026-08-11 05:22 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [relative_strength_btc_report.md](relative_strength_btc_report.md)

Questo modulo controlla se SOL e DOGE stanno davvero battendo Bitcoin. Una salita in USD accompagnata da una coppia ALT/BTC ribassista è spesso soltanto trascinamento di BTC.

**Protezione iniziale:** il candidato relativo è limitato a -1/0/+1, ma il peso nel Global resta **0**. La coppia BTC conferma o indebolisce il tecnico USD; non viene sommata come secondo modulo indipendente.

## Sintesi

| Asset | Coppia | Prezzo | Score raw | Candidato | Peso Global | Forza vs BTC | Confidenza | 30g | Tecnico USD | Lettura combinata |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | 0.00118570 | -3 | 0 | 0 | RELATIVA MISTA / NON CONFERMATA | BASSA | -1,60% | MISTA | QUADRO MISTO / NESSUNA CONFERMA RELATIVA |
| DOGE | DOGE/BTC | 0.00000109 | -4 | -1 | 0 | SOTTOPERFORMA BTC | BASSA | -4,80% | MISTA | FORZA RELATIVA NEGATIVA, USD ANCORA MISTO |

## Matrice di lettura

| ALT/USD | ALT/BTC | Interpretazione |
| --- | --- | --- |
| Rialzista | Rialzista | Conferma migliore: sale e batte BTC |
| Rialzista | Ribassista | Sale soprattutto perché BTC trascina il mercato |
| Ribassista | Rialzista | Forza relativa nascosta / possibile rotazione futura |
| Ribassista | Ribassista | Debolezza completa |

## SOL/BTC

- **Verdetto relativo:** RELATIVA MISTA / NON CONFERMATA (-3)
- **Candidato futuro:** 0; **peso attuale Global: 0**
- **Lettura combinata USD/BTC:** QUADRO MISTO / NESSUNA CONFERMA RELATIVA
- **Struttura:** MASSIMI E MINIMI DECRESCENTI
- **Rendimenti relativi:** 7g +2,39%; 30g -1,60%; 90g +1,17%; 180g +0,31%
- **Daily:** RSI 56.75; MA50 0.00119061; MA200 0.00118806
- **Weekly:** MA30 0.00118832; RSI 46.99
- **Livelli:** supporto 0.00116400; resistenza 0.00119500; breakout 60g 0.00134900; breakdown 60g 0.00102000
- **Pattern:** DOPPIO MASSIMO / CANDIDATO; neckline 0.00113300; target 0.00108600
- **Fibonacci:** VICINO — 50.0% a 0.00117900
- **Fonte:** Yahoo Finance SOL-BTC (coppia diretta)
- **Motivi score:** prezzo sotto MA50 daily; prezzo sotto MA200 daily; MA50 daily in salita; prezzo sotto MA30 weekly; MA30 weekly in discesa; struttura con massimi/minimi decrescenti; MACD relativo positivo

![Grafico SOL/BTC](relative_strength_SOLBTC.png)

## DOGE/BTC

- **Verdetto relativo:** SOTTOPERFORMA BTC (-4)
- **Candidato futuro:** -1; **peso attuale Global: 0**
- **Lettura combinata USD/BTC:** FORZA RELATIVA NEGATIVA, USD ANCORA MISTO
- **Struttura:** COMPRESSIONE / TRIANGOLO POSSIBILE
- **Rendimenti relativi:** 7g -1,09%; 30g -4,80%; 90g -20,03%; 180g -19,56%
- **Daily:** RSI 44.56; MA50 0.00000115; MA200 0.00000131
- **Weekly:** MA30 0.00000130; RSI 31.81
- **Livelli:** supporto 0.00000105; resistenza 0.00000114; breakout 60g 0.00000146; breakdown 60g 0.00000104
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
| SOL | 90g | 196 | 53,57% | +10,26% | +2,02% |
| DOGE | 7g | 293 | 55,97% | +1,85% | -1,68% |
| DOGE | 30g | 290 | 53,10% | +2,05% | -3,94% |
| DOGE | 90g | 285 | 54,04% | +6,94% | -8,47% |

## Tracker live e gate futuro

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto | Stato | Peso Global |
| --- | --- | --- | --- | --- | --- | --- |
| SOL | 1g | 15 | 66,67% | -0,23% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 3g | 15 | 46,67% | -0,50% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 7g | 11 | 54,55% | -0,20% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 14g | 4 | 25,00% | -0,62% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 30g | 0 | n/a | n/a | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 1g | 31 | 70,97% | +0,41% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 3g | 29 | 65,52% | +0,86% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 7g | 25 | 88,00% | +1,84% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 14g | 18 | 88,89% | +2,46% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 30g | 2 | 100,00% | +5,30% | LOCKED / RACCOLTA LIVE | 0 |

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

Ultima candela SOL usata: **11 agosto 2026**

## Verdetto: ANALOGIA DEBOLE / SCENARIO SECONDARIO

- **Fase attuale:** FRATTALE SOLO DI CONTESTO
- **Somiglianza totale:** +57,11%
- **Somiglianza strutturale:** +57,11%
- **Aderenza prezzo live:** +69,55%
- **Errore medio live:** +15,23%
- **Gap prezzo corrente:** -16,26%
- **Peso operativo suggerito:** 0
- **Affidabilita:** BASSA
- **Rischio fase:** ALTO
- **Trend tracking:** STRUTTURA STABILE
- **Sintesi:** Esistono alcuni elementi comuni, ma non abbastanza per una conferma.
- **SOL è al giorno:** 66 dal bottom usato.
- **Giorno BTC equivalente:** 2023-01-26
- **Prossimo step:** Proiezione condizionale, non conferma operativa: **Prima spike, poi scarico.** Zona bassa **71,98 $** intorno al **25 agosto 2026**; zona alta **78,43 $** intorno al **14 agosto 2026**; fine step circa **71,98 $** entro il **25 agosto 2026**.

## Somiglianza prima e dopo inizio programma

Questa sezione separa la somiglianza della forma dall'aderenza reale del prezzo.

- **Inizio programma/scanner:** 3 luglio 2026
- **Prima del programma** = backtest retroattivo.
- **Da inizio programma** = verifica live: è la parte più importante per l'uso operativo.

| Periodo | Date | Giorni | Aderenza prezzo | Errore medio | Gap ultimo | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| Prima del programma | 6 giugno 2026 -> 2 luglio 2026 | 27 | +87,95% | +6,02% | +21,89% | ABBASTANZA ALLINEATO |
| Da inizio programma | 3 luglio 2026 -> 11 agosto 2026 | 40 | +69,55% | +15,23% | -16,26% | STACCATO / NON ADERENTE |
| Totale dal bottom | 6 giugno 2026 -> 11 agosto 2026 | 67 | +76,96% | +11,52% | -16,26% | DEVIAZIONE MODERATA |

Nota: un frattale può avere una forma simile ma un prezzo distante. In quel caso non è operativo finché il gap non rientra.

## Lettura operativa veloce

Il frattale non deve generare acquisti o leva adesso. La forma è un contesto, ma l'aderenza live del prezzo è insufficiente.

| Voce | Risposta | Perché |
| --- | --- | --- |
| Uso operativo | NO | Il frattale vale 0 punti operativi finché il prezzo resta non aderente. |
| Aderenza live | +69,55% | Errore medio live +15,23%. |
| Gap corrente | -16,26% | Deve rientrare circa entro ±12%. |
| Prima conferma prezzo | 79,78 $ | Serve anche miglioramento del gap, non solo una candela sopra il livello. |
| Seconda conferma | 93,47 $ | Rende più credibile il percorso, ma non sostituisce l'aderenza. |
| Invalidazione soft | 71,42 $ | Sotto questa zona il quadro peggiora. |
| Invalidazione forte | 62,19 $ | Sotto il bottom il paragone è quasi rotto. |

## Target ciclo fino al top BTC 2025

| Voce | Valore |
| --- | --- |
| Stato | CONTESTO / NON OPERATIVO |
| Top BTC 2025 | 6 ottobre 2025 - 124.753 $ |
| Data SOL equivalente | 21 aprile 2029 |
| Target ciclo base da oggi | 411,53 $ |
| Massimo percorso base | 411,53 $ (21 aprile 2029) |

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
| Prima conferma | 79,78 $ | Deve accompagnarsi al rientro del gap. |
| Seconda conferma | 93,47 $ | Scenario più credibile. |
| Invalidazione soft | 71,42 $ | Il frattale si indebolisce. |
| Invalidazione forte | 62,19 $ | Il paragone si rompe. |

## Proiezione veloce con date SOL

| Orizzonte | Data SOL | BTC fece | SOL base | Min percorso | Max percorso |
| --- | --- | --- | --- | --- | --- |
| 7 giorni | 18 agosto 2026 | +1,91% | 77,43 $ | 75,34 $ | 78,43 $ |
| 14 giorni | 25 agosto 2026 | -5,27% | 71,98 $ | 71,98 $ | 78,43 $ |
| 30 giorni | 10 settembre 2026 | +0,62% | 76,45 $ | 71,42 $ | 81,91 $ |
| 60 giorni | 10 ottobre 2026 | +17,83% | 89,53 $ | 66,59 $ | 93,47 $ |
| 90 giorni | 9 novembre 2026 | +23,40% | 93,76 $ | 66,59 $ | 100,57 $ |
| 120 giorni | 9 dicembre 2026 | +16,01% | 88,14 $ | 66,59 $ | 100,57 $ |

## Prossimi step se SOL segue BTC 2022

| Step | Date SOL | BTC fine | SOL zona bassa | SOL zona alta | SOL fine base | Lettura |
| --- | --- | --- | --- | --- | --- | --- |
| Step 1 - prossime 2 settimane | 11 agosto 2026 -> 25 agosto 2026 | -5,27% | 71,98 $ (25 agosto 2026) | 78,43 $ (14 agosto 2026) | 71,98 $ | Prima spike, poi scarico. |
| Step 2 - primo mese | 26 agosto 2026 -> 10 settembre 2026 | +0,62% | 71,42 $ (26 agosto 2026) | 81,91 $ (5 settembre 2026) | 76,45 $ | Prima retest / debolezza, poi recupero. |
| Step 3 - secondo mese | 11 settembre 2026 -> 10 ottobre 2026 | +17,83% | 66,59 $ (23 settembre 2026) | 93,47 $ (6 ottobre 2026) | 89,53 $ | Prima retest / debolezza, poi recupero. |
| Step 4 - terzo mese | 11 ottobre 2026 -> 9 novembre 2026 | +23,40% | 89,95 $ (11 ottobre 2026) | 100,57 $ (28 ottobre 2026) | 93,76 $ | Spinta rialzista abbastanza pulita. |

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
| Prezzo SOL | 75,98 $ |  |
| Weekly RSI | 40,56 / linea grezza 53,18 | LINEA NON AFFIDABILE / RISCHIO NON ATTIVO — IRREALISTICA / NON OPERATIVA |
| Monthly RSI | 41,05 / linea grezza 55,81 | RSI TROPPO BASSO PER RISCHIO TOP — VALIDA / USO PRUDENTE |
| Target ciclo base | 411,53 $ | Avanzamento +18,46% |
| Rischio top-cycle RSI | BASSO | Nessun segnale top-cycle macro attivo. Prezzo ancora lontano dal target ciclo; il filtro RSI resta solo di monitoraggio. |

## Lettura semplice

- Weekly: La top-line weekly non supera i controlli di qualità. Non viene usata per generare rischio top-cycle.
- Monthly: RSI monthly è 41,1, sotto la soglia prudente 55. Anche se fosse vicino alla linea, non è una vera zona di esaurimento ciclo.
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
| Prezzo SOL | 75,98 $ |
| TVL Solana | 4,83 mld $ |
| TVL 7g | +1,77% |
| DEX volume 24h | 1,55 mld $ |
| Fees 24h | 10,45 mln $ |
| Stablecoin su Solana | 16,26 mld $ |
| Stake ratio | 68,82% |
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
| Prezzo SOL | 75,98 $ |
| EMA200 weekly target | 111,66 $ |
| Upside verso EMA200 | +47,36% |
| Distanza prezzo da EMA200 | -32,14% |
| Gap EMA50/EMA200 | -5,53% |
| Stato cross | EMA50 SOTTO EMA200 |
| RSI weekly | 40,44 |
| Età SOL | 6,3 anni |
| Analoghi storici usati | 30 |
| Max analoghi per asset | 3 |
| Hit EMA200 12w analoghi | +36,67% |
| Max gain mediano 12w | +20,97% |
| Drawdown mediano 12w | -22,77% |

Lettura semplice:

**CONTESTO INTERESSANTE, SERVONO CONFERME DI PREZZO**

Autocontrollo: **STABILE / DA CONFERMARE**.

Questo modulo confronta SOL con altre crypto in fasi simili di età, distanza da EMA200, EMA50/EMA200 e RSI. Non usa stock market.

Nota importante: **questo modulo ora NON pesa più nel Global Confluence**. Resta solo come contesto di ciclo e come mappa verso EMA200 weekly. Il punteggio Global resta guidato da prezzo, scanner, regime, struttura tecnica, frattale, RSI e conferme reali.

Nota: se EMA50/EMA200 sono dentro ±2%, il modulo parla di medie sovrapposte / incrocio in corso, perché exchange diversi possono mostrare il cross leggermente prima o dopo.

<!-- Generato: 2026-08-11 05:22 UTC -->
<!-- MAJOR_ALT_LIFECYCLE_SQUEEZE_END -->

</details>
<!-- COMPACT_SECTION_END:major_alt_lifecycle -->

# Report giornaliero BTC / SOL / DOGE

Aggiornato il: **2026-08-11 05:12:33 UTC**

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
| BTC | NESSUN CAMBIAMENTO FORTE | peggioramento | RIALZISTA | +80.00% | -2.50 punti |
| SOL | NESSUN CAMBIAMENTO FORTE | peggioramento | RIALZISTA | +72.50% | -7.50 punti |
| DOGE | NESSUN CAMBIAMENTO FORTE | peggioramento | RIALZISTA | +72.50% | 0.00 punti |

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
| BTC | 60.778 $ | 70.374 $ | +53,33% | +15,79% | rimbalzo possibile | 70.374 $ | 60.778 $ | +3,33% | -13,64% | spike storicamente più resistente |
| SOL | 72,18 $ | 83,58 $ | +50,00% | +15,79% | rimbalzo possibile | 83,58 $ | 72,18 $ | 0,00% | -13,64% | spike storicamente più resistente |
| DOGE | 0,06650 $ | 0,07700 $ | +65,52% | +15,79% | buona zona storica di rimbalzo | 0,07700 $ | 0,06650 $ | +12,90% | -13,64% | spike storicamente più resistente |

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

- **BTC: su 40 casi simili, 15 prima sono scesi a -5,00%. Tra quei 15, 8 poi sono rimbalzati fino a +10,00%. Percentuale: +53,33% (8/15). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo possibile.**
- **BTC: su 40 casi simili, 30 prima sono saliti a +10,00%. Tra quei 30, 1 poi sono scaricati a -5,00%. Percentuale: +3,33% (1/30). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.**
- **SOL: su 40 casi simili, 18 prima sono scesi a -5,00%. Tra quei 18, 9 poi sono rimbalzati fino a +10,00%. Percentuale: +50,00% (9/18). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo possibile.**
- **SOL: su 40 casi simili, 28 prima sono saliti a +10,00%. Tra quei 28, 0 poi sono scaricati a -5,00%. Percentuale: 0,00% (0/28). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.**
- **DOGE: su 40 casi simili, 29 prima sono scesi a -5,00%. Tra quei 29, 19 poi sono rimbalzati fino a +10,00%. Percentuale: +65,52% (19/29). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: buona zona storica di rimbalzo.**
- **DOGE: su 40 casi simili, 31 prima sono saliti a +10,00%. Tra quei 31, 4 poi sono scaricati a -5,00%. Percentuale: +12,90% (4/31). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.**

<!-- BOUNCE_AFTER_DRAWDOWN_END -->

</details>
<!-- COMPACT_SECTION_END:bounce_after_drawdown -->

<!-- COMPACT_SECTION_START:scanner_forecast -->
<details>
<summary><strong>🔭 Cono probabilistico dello scanner</strong></summary>

<!-- SCANNER_FORECAST_TRACKER_START -->
# Scanner forecast path / cono probabilistico

Generato: 2026-08-11 05:20:58 UTC


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
| BTC | 2026-08-11 | 63.976 $ | SALITA | 80,00% | 55.067,34 $ | 66.780,22 $ | 69.830,06 $ | 74.536,95 $ | 86.401,32 $ |
| SOL | 2026-08-11 | 75,98 $ | SALITA | 72,50% | 71,51 $ | 75,17 $ | 84,70 $ | 91,93 $ | 120,41 $ |
| DOGE | 2026-08-11 | 0.07000 $ | SALITA | 72,50% | 0.05210 $ | 0.06932 $ | 0.08085 $ | 0.09531 $ | 0.10329 $ |

## Grafici

### BTC

![Scanner forecast BTC](scanner_forecast_BTC.png)

#### Verifica storica e discrepanza

![Verifica storica cono BTC](scanner_forecast_history_BTC.png)

- Cono congelato il **2026-07-12**; verificato fino al **2026-08-11**; stato **COMPLETO 30/30g**.
- Reale **63.902,07 $**; p50 previsto **69.210,01 $**; scarto **-7,67%**.
- Errore medio assoluto **2,50%**; massimo **9,19%**; DENTRO p10-p90; DENTRO p25-p75.

### SOL

![Scanner forecast SOL](scanner_forecast_SOL.png)

#### Verifica storica e discrepanza

![Verifica storica cono SOL](scanner_forecast_history_SOL.png)

- Cono congelato il **2026-07-12**; verificato fino al **2026-08-11**; stato **COMPLETO 30/30g**.
- Reale **75,81 $**; p50 previsto **74,45 $**; scarto **1,82%**.
- Errore medio assoluto **2,42%**; massimo **8,03%**; DENTRO p10-p90; DENTRO p25-p75.

### DOGE

![Scanner forecast DOGE](scanner_forecast_DOGE.png)

#### Verifica storica e discrepanza

![Verifica storica cono DOGE](scanner_forecast_history_DOGE.png)

- Cono congelato il **2026-07-12**; verificato fino al **2026-08-11**; stato **COMPLETO 30/30g**.
- Reale **0.06985 $**; p50 previsto **0.05848 $**; scarto **19,44%**.
- Errore medio assoluto **13,11%**; massimo **30,13%**; DENTRO p10-p90; FUORI p25-p75.

## Accuratezza percorso scanner

| Asset   | Giorno   |   Controlli | Dentro p10-p90   | Dentro p25-p75   | Errore medio abs vs p50   | Errore medio vs p50   |
|:--------|:---------|------------:|:-----------------|:-----------------|:--------------------------|:----------------------|
| BTC | 1g | 32 | 100,00% | 59,38% | 1,64% | -0,15% |
| BTC | 3g | 30 | 100,00% | 80,00% | 2,00% | -0,38% |
| BTC | 7g | 26 | 100,00% | 88,46% | 2,13% | 0,70% |
| BTC | 14g | 19 | 100,00% | 84,21% | 2,24% | 1,13% |
| BTC | 30g | 3 | 100,00% | 66,67% | 8,16% | -8,16% |
| SOL | 1g | 32 | 78,12% | 59,38% | 2,04% | -0,43% |
| SOL | 3g | 30 | 100,00% | 76,67% | 2,22% | -0,74% |
| SOL | 7g | 26 | 100,00% | 92,31% | 2,06% | 0,11% |
| SOL | 14g | 19 | 100,00% | 89,47% | 2,13% | 0,96% |
| SOL | 30g | 3 | 100,00% | 100,00% | 1,05% | 0,13% |
| DOGE | 1g | 32 | 96,88% | 65,62% | 2,36% | -0,01% |
| DOGE | 3g | 30 | 100,00% | 86,67% | 2,21% | 0,54% |
| DOGE | 7g | 26 | 92,31% | 92,31% | 5,41% | 3,03% |
| DOGE | 14g | 19 | 100,00% | 63,16% | 8,12% | 5,84% |
| DOGE | 30g | 3 | 100,00% | 0,00% | 14,92% | 14,92% |

## Calibratore shadow

Il cono ufficiale resta grezzo e invariato. Il calibratore usa soltanto previsioni passate già mature, campionate una volta a settimana per ridurre la falsa indipendenza. Ogni orizzonte si attiva a 30 controlli indipendenti: parte al 25% della correzione stimata e cresce gradualmente fino al 100% a 100 controlli.

| Asset   | Orizzonte   |   Controlli indipendenti |   Soglia | Stato                  | Forza correzione   | Shift p50   |   Scala p10-p90 |
|:--------|:------------|-------------------------:|---------:|:-----------------------|:-------------------|:------------|----------------:|
| BTC | 1g | 6 | 30 | RACCOLTA (24 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 3g | 5 | 30 | RACCOLTA (25 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 7g | 5 | 30 | RACCOLTA (25 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 14g | 4 | 30 | RACCOLTA (26 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 30g | 1 | 30 | RACCOLTA (29 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 1g | 6 | 30 | RACCOLTA (24 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 3g | 5 | 30 | RACCOLTA (25 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 7g | 5 | 30 | RACCOLTA (25 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 14g | 4 | 30 | RACCOLTA (26 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 30g | 1 | 30 | RACCOLTA (29 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 1g | 6 | 30 | RACCOLTA (24 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 3g | 5 | 30 | RACCOLTA (25 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 7g | 5 | 30 | RACCOLTA (25 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 14g | 4 | 30 | RACCOLTA (26 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 30g | 1 | 30 | RACCOLTA (29 mancanti) | 0,0% | 0,00% | 1,000 |

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

Righe salvate nello storico: **90**.

Questa sezione tiene un diario delle previsioni giornaliere a 30 giorni, senza appesantire il report principale.

| Data | Asset | Prezzo | Direzione | Casi positivi | Return p50 | Drawdown p50 | Max gain p50 | Controllo 30g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08-11 | BTC | 63.976 $ | SALITA | 80,00% | 69.830 $ | 62.029 $ | 74.130 $ | 2026-09-10 |
| 2026-08-11 | DOGE | 0,07000 $ | SALITA | 72,50% | 0,08000 $ | 0,06000 $ | 0,09000 $ | 2026-09-10 |
| 2026-08-11 | SOL | 75,98 $ | SALITA | 72,50% | 84,70 $ | 72,52 $ | 89,07 $ | 2026-09-10 |

<!-- FORECAST_30D_HISTORY_END -->

</details>
<!-- COMPACT_SECTION_END:scanner_forecast -->

<!-- COMPACT_SECTION_START:extreme_cases -->
<details>
<summary><strong>⚠️ Percorso dei casi estremi</strong></summary>

<!-- EXTREME_CASES_PATH_START -->
# Extreme cases path report

Generato: 2026-08-11 05:21 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [extreme_cases_path_report.md](extreme_cases_path_report.md)

Questo report si attiva quando i casi positivi o negativi sono almeno **80%**.

Ora misura anche il **rialzo massimo prima della discesa principale**, quindi distingue uno spike iniziale da una discesa quasi immediata.

## Trigger estremi

| Asset   | Direzione            | Trigger   | Percentuale   | Motivo                           |   Match disponibili |
|:--------|:---------------------|:----------|:--------------|:---------------------------------|--------------------:|
| BTC     | POSITIVO / RIALZISTA | SI        | +80,00%       | Casi positivi 80.00% >= 80%      |                  40 |
| SOL     | NESSUNO              | NO        | +72,50%       | Nessun lato sopra soglia estrema |                  40 |
| DOGE    | NESSUNO              | NO        | +72,50%       | Nessun lato sopra soglia estrema |                  40 |

## BTC — casi rialzisti

- Trigger: **Casi positivi 80.00% >= 80%**
- Casi usati nei grafici: **32**
- Return mediano 7g: **+4,51%**
- Return mediano 14g: **+9,08%**
- Return mediano 30g: **+10,75%**
- Drawdown mediano: **-0,73%**
- Max gain mediano: **+21,18%**

### Quanto salivano prima di scendere

- Spike massimo mediano prima del minimo: **+0,00%**
- Spike massimo medio prima del minimo: **+1,30%**
- Spike p75 prima del minimo: **+1,08%**
- Giorno mediano dello spike: **giorno 0**
- Giorno mediano del minimo: **giorno 1**
- Scarico mediano dal picco al minimo: **-2,49%**
- Casi con almeno +5% prima del minimo: **+9,38%**
- Casi con almeno +10% prima del minimo: **+3,12%**
- Casi con almeno +15% prima del minimo: **+0,00%**
- Discesa quasi immediata: **+65,62%**

Un segnale ribassista a 30 giorni non significa necessariamente discesa immediata: alcuni casi fanno prima uno spike e poi scaricano.

### Distribuzione 30 giorni

| P10    | P25    | P50     | P75     | P90     |
|:-------|:-------|:--------|:--------|:--------|
| +5,33% | +7,65% | +10,75% | +21,58% | +39,87% |

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

| Asset storico   | End        | Similarity   | Spike prima del minimo   |   Giorno spike | Minimo 30g   |   Giorno minimo | Dump dal picco   | Return 30g   | Sequenza                |
|:----------------|:-----------|:-------------|:-------------------------|---------------:|:-------------|----------------:|:-----------------|:-------------|:------------------------|
| 1INCH-USD       | 2024-10-13 | +86,67%      | +13,39%                  |              7 | -11,35%      |              22 | -21,82%          | +19,12%      | SPIKE PRIMA DEL DUMP    |
| LTC-USD         | 2020-05-15 | +85,21%      | +5,95%                   |              4 | -0,94%       |              11 | -6,50%           | +2,92%       | ECCEZIONE POSITIVA      |
| QTUM-USD        | 2026-04-14 | +84,83%      | +5,91%                   |              3 | -4,42%       |              16 | -9,75%           | +9,08%       | ECCEZIONE POSITIVA      |
| ALGO-USD        | 2020-05-19 | +85,63%      | +4,85%                   |              1 | -3,57%       |               2 | -8,04%           | +20,67%      | ECCEZIONE POSITIVA      |
| BTC-USD         | 2026-04-14 | +85,53%      | +3,97%                   |              3 | -0,44%       |               5 | -4,24%           | +9,26%       | ECCEZIONE POSITIVA      |
| THETA-USD       | 2022-07-18 | +84,48%      | +2,34%                   |              1 | -10,43%      |               7 | -12,48%          | +7,26%       | ECCEZIONE POSITIVA      |
| XLM-USD         | 2020-11-11 | +90,41%      | +2,02%                   |              2 | -0,49%       |               4 | -2,46%           | +87,35%      | DISCESA QUASI IMMEDIATA |
| BNB-USD         | 2019-01-26 | +84,50%      | +1,17%                   |              1 | -11,88%      |               4 | -12,89%          | +40,47%      | DISCESA QUASI IMMEDIATA |
| LTC-USD         | 2026-04-09 | +85,17%      | +1,05%                   |              2 | -1,86%       |               3 | -2,87%           | +6,43%       | DISCESA QUASI IMMEDIATA |
| ETC-USD         | 2020-11-11 | +86,62%      | +0,83%                   |              2 | -1,22%       |               4 | -2,03%           | +14,00%      | DISCESA QUASI IMMEDIATA |
| XRP-USD         | 2023-10-22 | +89,65%      | +0,00%                   |              0 | +0,00%       |               0 | +0,00%           | +11,10%      | DISCESA QUASI IMMEDIATA |
| XRP-USD         | 2026-04-14 | +88,54%      | +0,00%                   |              0 | +0,00%       |               0 | +0,00%           | +8,98%       | DISCESA QUASI IMMEDIATA |
| BTC-USD         | 2019-01-26 | +88,22%      | +0,00%                   |              0 | -5,63%       |              12 | -5,63%           | +7,78%       | ECCEZIONE POSITIVA      |
| LTC-USD         | 2023-10-22 | +88,05%      | +0,00%                   |              0 | +0,00%       |               0 | +0,00%           | +1,94%       | DISCESA QUASI IMMEDIATA |
| ETH-USD         | 2026-04-09 | +87,88%      | +0,00%                   |              0 | +0,00%       |               0 | +0,00%           | +6,28%       | DISCESA QUASI IMMEDIATA |
| DOGE-USD        | 2020-11-11 | +87,85%      | +0,00%                   |              0 | +0,00%       |               0 | +0,00%           | +11,20%      | DISCESA QUASI IMMEDIATA |
| ETC-USD         | 2023-10-22 | +87,82%      | +0,00%                   |              0 | +0,00%       |               0 | +0,00%           | +14,66%      | DISCESA QUASI IMMEDIATA |
| SOL-USD         | 2026-04-12 | +87,71%      | +0,00%                   |              0 | +0,00%       |               0 | +0,00%           | +15,64%      | DISCESA QUASI IMMEDIATA |
| MKR-USD         | 2020-05-21 | +87,18%      | +0,00%                   |              0 | +0,00%       |               0 | +0,00%           | +63,16%      | DISCESA QUASI IMMEDIATA |
| BNB-USD         | 2026-04-14 | +87,16%      | +0,00%                   |              0 | +0,00%       |               0 | +0,00%           | +10,41%      | DISCESA QUASI IMMEDIATA |

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
- Prezzo attuale: **63.976,47 $**
- Return normale fra 30 giorni: **69.830,06 $** (9,15%)
- Drawdown normale durante il mese: **62.029,35 $** (-3,04%)
- Drawdown brutto da rispettare: **56.716,25 $** (-11,35%)
- Max gain normale durante il mese: **74.130,27 $** (15,87%)
- Max gain buono / take profit ottimistico: **86.753,71 $** (35,60%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Solana
- Direzione più probabile a 30 giorni: **SALITA**
- Casi positivi / salita storica: **72,50%**
- Casi negativi / discesa storica: **27,50%**
- Quanto è netto il segnale: **forte**
- Prezzo attuale: **75,98 $**
- Return normale fra 30 giorni: **84,70 $** (11,48%)
- Drawdown normale durante il mese: **72,52 $** (-4,56%)
- Drawdown brutto da rispettare: **66,43 $** (-12,57%)
- Max gain normale durante il mese: **89,07 $** (17,23%)
- Max gain buono / take profit ottimistico: **98,65 $** (29,84%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Dogecoin
- Direzione più probabile a 30 giorni: **SALITA**
- Casi positivi / salita storica: **72,50%**
- Casi negativi / discesa storica: **27,50%**
- Quanto è netto il segnale: **forte**
- Prezzo attuale: **0,07 $**
- Return normale fra 30 giorni: **0,08 $** (15,50%)
- Drawdown normale durante il mese: **0,06 $** (-8,48%)
- Drawdown brutto da rispettare: **0,06 $** (-16,29%)
- Max gain normale durante il mese: **0,09 $** (22,24%)
- Max gain buono / take profit ottimistico: **0,10 $** (43,08%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Messaggio del giorno

Il quadro generale oggi è più favorevole. Lo scanner vede più possibilità di salita su più asset.

---

# Mappa semplice asset per asset

# Bitcoin — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟢 VERDE / Favorevole
**Prezzo attuale:** 63.976,47 $

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

- Se va molto male: **55.067,34 $** (-13,93%)
- Se va male: **66.780,22 $** (4,38%)
- Scenario normale: **69.830,06 $** (9,15%)
- Se va bene: **74.536,95 $** (16,51%)
- Se va molto bene: **86.401,32 $** (35,05%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **62.029,35 $** (-3,04%)
- Discesa brutta: **56.716,25 $** (-11,35%)
- Discesa molto brutta: **50.143,42 $** (-21,62%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **74.130,27 $** (15,87%)
- Rialzo buono: **86.753,71 $** (35,60%)
- Rialzo molto forte: **100.625,21 $** (57,28%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Bitcoin tendeva a muoversi tra una zona bassa intorno a **62.029,35 $** e uno spike normale intorno a **74.130,27 $**.

La chiusura a 30 giorni era più spesso positiva: salita 80,00%, discesa 20,00%. Quindi la lettura principale è favorevole.

Nota leva BTC: se la liquidazione è vicina a 51.000 $, guarda soprattutto la discesa brutta e molto brutta. Il prezzo può recuperare dopo, ma la leva può saltare prima.

---

# Solana — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟢 VERDE / Favorevole
**Prezzo attuale:** 75,98 $

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

- Se va molto male: **71,51 $** (-5,88%)
- Se va male: **75,17 $** (-1,06%)
- Scenario normale: **84,70 $** (11,48%)
- Se va bene: **91,93 $** (21,00%)
- Se va molto bene: **120,41 $** (58,48%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **72,52 $** (-4,56%)
- Discesa brutta: **66,43 $** (-12,57%)
- Discesa molto brutta: **62,35 $** (-17,94%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **89,07 $** (17,23%)
- Rialzo buono: **98,65 $** (29,84%)
- Rialzo molto forte: **129,82 $** (70,85%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Solana tendeva a muoversi tra una zona bassa intorno a **72,52 $** e uno spike normale intorno a **89,07 $**.

La chiusura a 30 giorni era più spesso positiva: salita 72,50%, discesa 27,50%. Quindi la lettura principale è favorevole.

---

# Dogecoin — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟢 VERDE / Favorevole
**Prezzo attuale:** 0,07 $

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

- Se va molto male: **0,05 $** (-25,57%)
- Se va male: **0,07 $** (-0,97%)
- Scenario normale: **0,08 $** (15,50%)
- Se va bene: **0,10 $** (36,15%)
- Se va molto bene: **0,10 $** (47,55%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **0,06 $** (-8,48%)
- Discesa brutta: **0,06 $** (-16,29%)
- Discesa molto brutta: **0,05 $** (-31,93%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **0,09 $** (22,24%)
- Rialzo buono: **0,10 $** (43,08%)
- Rialzo molto forte: **0,11 $** (64,24%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Dogecoin tendeva a muoversi tra una zona bassa intorno a **0,06 $** e uno spike normale intorno a **0,09 $**.

La chiusura a 30 giorni era più spesso positiva: salita 72,50%, discesa 27,50%. Quindi la lettura principale è favorevole.

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

- Previsioni già controllate: **10**
- Direzione corretta: **85,71%**
- Errore medio dello scenario centrale: **4,09%**
- Zona rischio toccata: **0,00%**
- Zona rialzo media toccata: **0,00%**
- Prezzo finale dentro lo scenario 10%-90%: **100,00%**

### Dogecoin

- Previsioni già controllate: **10**
- Direzione corretta: **100,00%**
- Errore medio dello scenario centrale: **12,11%**
- Zona rischio toccata: **0,00%**
- Zona rialzo media toccata: **0,00%**
- Prezzo finale dentro lo scenario 10%-90%: **100,00%**

### Solana

- Previsioni già controllate: **10**
- Direzione corretta: **100,00%**
- Errore medio dello scenario centrale: **4,95%**
- Zona rischio toccata: **20,00%**
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

Dati ancora insufficienti: previsioni controllate **10** su **30** necessarie.

Per ora si usa solo lo scanner storico grezzo. Quando ci saranno abbastanza previsioni controllate, qui apparirà la lettura autocalibrata.

## Solana

Dati ancora insufficienti: previsioni controllate **10** su **30** necessarie.

Per ora si usa solo lo scanner storico grezzo. Quando ci saranno abbastanza previsioni controllate, qui apparirà la lettura autocalibrata.

## Dogecoin

Dati ancora insufficienti: previsioni controllate **10** su **30** necessarie.

Per ora si usa solo lo scanner storico grezzo. Quando ci saranno abbastanza previsioni controllate, qui apparirà la lettura autocalibrata.

---

# Approfondimento tecnico — Bitcoin (BTC-USD)

## Semaforo: 🟢 VERDE / Favorevole

**Prezzo attuale:** 63.976,47 $

Bitcoin ha un segnale favorevole. La statistica dei casi simili indica più possibilità di salita che di discesa, ma resta comunque una probabilità, non una certezza.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **80,00%**
- Casi negativi dopo 30 giorni: **20,00%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **86,34%**
- Rendimento medio dopo 30 giorni: **12,78%**
- Rendimento centrale dopo 30 giorni: **9,15%**
- Discesa media durante i 30 giorni: **-7,26%**
- Massimo rialzo medio durante i 30 giorni: **29,98%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **72.152,68 $**
- Scenario centrale a 30 giorni: **69.830,06 $**
- Zona di rischio media: **59.332,36 $**
- Zona di rialzo media: **83.157,84 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -13,93% → **55.067,34 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: 4,38% → **66.780,22 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: 9,15% → **69.830,06 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 16,51% → **74.536,95 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 35,05% → **86.401,32 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -21,62% → **50.143,42 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -11,35% → **56.716,25 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -3,04% → **62.029,35 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: 0,00% → **63.976,47 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: 0,00% → **63.976,47 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 6,26% → **67.980,60 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 10,05% → **70.406,60 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 15,87% → **74.130,27 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 35,60% → **86.753,71 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 57,28% → **100.625,21 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| XLM-USD         | 2020-08-04   | 2020-11-11 |        90.41 |        87.35 |          -0.49 |         155.8  |
| XRP-USD         | 2023-07-15   | 2023-10-22 |        89.65 |        11.1  |           0    |          36.94 |
| XRP-USD         | 2026-01-05   | 2026-04-14 |        88.54 |         8.98 |           0    |           8.98 |
| BTC-USD         | 2018-10-19   | 2019-01-26 |        88.22 |         7.78 |          -5.63 |          14.99 |
| ONE-USD         | 2020-02-11   | 2020-05-20 |        88.1  |       -21.28 |         -21.28 |           3.36 |
| LTC-USD         | 2023-07-15   | 2023-10-22 |        88.05 |         1.94 |           0    |          15.31 |
| ETH-USD         | 2025-12-31   | 2026-04-09 |        87.88 |         6.28 |           0    |          10.59 |
| DOGE-USD        | 2020-08-04   | 2020-11-11 |        87.85 |        11.2  |           0    |          51.82 |
| ETC-USD         | 2023-07-15   | 2023-10-22 |        87.82 |        14.66 |           0    |          31.26 |
| SOL-USD         | 2026-01-03   | 2026-04-12 |        87.71 |        15.64 |           0    |          19.4  |

---

# Approfondimento tecnico — Solana (SOL-USD)

## Semaforo: 🟢 VERDE / Favorevole

**Prezzo attuale:** 75,98 $

Solana ha un segnale favorevole. La statistica dei casi simili indica più possibilità di salita che di discesa, ma resta comunque una probabilità, non una certezza.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **72,50%**
- Casi negativi dopo 30 giorni: **27,50%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **77,64%**
- Rendimento medio dopo 30 giorni: **16,38%**
- Rendimento centrale dopo 30 giorni: **11,48%**
- Discesa media durante i 30 giorni: **-7,36%**
- Massimo rialzo medio durante i 30 giorni: **27,52%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **88,43 $**
- Scenario centrale a 30 giorni: **84,70 $**
- Zona di rischio media: **70,39 $**
- Zona di rialzo media: **96,89 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -5,88% → **71,51 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -1,06% → **75,17 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: 11,48% → **84,70 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 21,00% → **91,93 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 58,48% → **120,41 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -17,94% → **62,35 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -12,57% → **66,43 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -4,56% → **72,52 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -0,81% → **75,36 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: 0,00% → **75,98 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 3,35% → **78,53 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 8,53% → **82,46 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 17,23% → **89,07 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 29,84% → **98,65 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 70,85% → **129,82 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| ENJ-USD         | 2018-10-19   | 2019-01-26 |        82.73 |       130.26 |         -26.2  |         130.26 |
| EOS-USD         | 2018-11-03   | 2019-02-10 |        81.13 |        29.01 |          -3.1  |          50.33 |
| ONE-USD         | 2020-02-11   | 2020-05-20 |        80.96 |       -21.28 |         -21.28 |           3.36 |
| RUNE-USD        | 2026-01-06   | 2026-04-15 |        80.3  |        20.91 |           0    |          53.03 |
| VET-USD         | 2020-02-08   | 2020-05-17 |        80.16 |       104.48 |          -3.96 |         120.09 |
| SOL-USD         | 2026-01-03   | 2026-04-12 |        79.66 |        15.64 |           0    |          19.4  |
| BNB-USD         | 2026-01-05   | 2026-04-14 |        79.36 |        10.41 |           0    |          10.41 |
| DASH-USD        | 2020-02-06   | 2020-05-15 |        79.22 |         0.71 |          -0.12 |          10.25 |
| NEAR-USD        | 2025-12-31   | 2026-04-09 |        79    |        14.61 |          -7.58 |          16.66 |
| ADA-USD         | 2023-05-11   | 2023-08-18 |        78.6  |        -6.28 |          -8.34 |           3.24 |

---

# Approfondimento tecnico — Dogecoin (DOGE-USD)

## Semaforo: 🟢 VERDE / Favorevole

**Prezzo attuale:** 0,07 $

Dogecoin ha un segnale favorevole. La statistica dei casi simili indica più possibilità di salita che di discesa, ma resta comunque una probabilità, non una certezza.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **72,50%**
- Casi negativi dopo 30 giorni: **27,50%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **88,36%**
- Rendimento medio dopo 30 giorni: **18,41%**
- Rendimento centrale dopo 30 giorni: **15,50%**
- Discesa media durante i 30 giorni: **-12,38%**
- Massimo rialzo medio durante i 30 giorni: **31,40%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **0,08 $**
- Scenario centrale a 30 giorni: **0,08 $**
- Zona di rischio media: **0,06 $**
- Zona di rialzo media: **0,09 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -25,57% → **0,05 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -0,97% → **0,07 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: 15,50% → **0,08 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 36,15% → **0,10 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 47,55% → **0,10 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -31,93% → **0,05 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -16,29% → **0,06 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -8,48% → **0,06 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -4,21% → **0,07 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: -1,26% → **0,07 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 0,00% → **0,07 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 12,89% → **0,08 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 22,24% → **0,09 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 43,08% → **0,10 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 64,24% → **0,11 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| ZEC-USD         | 2019-06-16   | 2019-09-23 |        91.73 |       -25.47 |         -25.47 |           0    |
| VET-USD         | 2022-03-24   | 2022-07-01 |        90.42 |        22.63 |          -3.05 |          23.68 |
| OP-USD          | 2026-01-01   | 2026-04-10 |        90.25 |        41.98 |          -7.1  |          49.82 |
| ETC-USD         | 2022-03-22   | 2022-06-29 |        89.68 |       167.71 |          -8.6  |         168.27 |
| ADA-USD         | 2019-06-11   | 2019-09-18 |        89.58 |       -28.56 |         -29.66 |           0    |
| AVAX-USD        | 2025-09-13   | 2025-12-21 |        89.57 |        -0.45 |          -0.48 |          21.42 |
| ADA-USD         | 2022-03-22   | 2022-06-29 |        89.51 |        12.42 |         -10.22 |          12.42 |
| SAND-USD        | 2025-01-04   | 2025-04-13 |        89.39 |        41.25 |          -5.3  |          42.72 |
| SNX-USD         | 2025-10-02   | 2026-01-09 |        89.08 |       -40.14 |         -42.18 |           4.27 |
| DASH-USD        | 2022-03-22   | 2022-06-29 |        89.07 |        14.27 |         -10.11 |          17.74 |

</details>
<!-- COMPACT_SECTION_END:scanner_full_detail -->

<!-- COMPACT_SECTION_START:market_regime -->
<details>
<summary><strong>🌦️ Market Regime Match</strong></summary>

<!-- MARKET_REGIME_MATCH_START -->
# Market Regime Match Report


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [market_regime_match_report.md](market_regime_match_report.md)

Generated: 2026-08-11 05:21 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | BEAR | 63.976 $ | False | -19.40% | -10.12% | BEAR | -19.40% | -10.12% |
| DOGE-USD | BEAR | 0.07000 $ | False | -38.04% | -16.72% | BEAR | -19.40% | -10.12% |
| SOL-USD | BEAR | 75,98 $ | False | -16.83% | -17.06% | BEAR | -19.40% | -10.12% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 80.00% | 9.15% | 16.51% | 35.05% | -3.04% | -21.62% | 15.87% | 35.60% | 57.28% | 57.50% | 13.11% | 56.37% | 102.63% |
| BTC-USD | SAME_BTC_REGIME | 17 | 88.24% | 9.08% | 10.41% | 21.20% | -4.42% | -14.77% | 12.45% | 15.90% | 26.01% | 41.18% | -13.16% | 24.79% | 86.54% |
| BTC-USD | SAME_ASSET_REGIME | 21 | 85.71% | 9.08% | 15.64% | 27.93% | -4.42% | -17.83% | 14.99% | 28.52% | 39.85% | 47.62% | -13.16% | 45.05% | 76.63% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 16 | 87.50% | 9.03% | 11.71% | 21.72% | -5.03% | -15.28% | 12.73% | 16.77% | 27.54% | 43.75% | -14.35% | 29.85% | 89.02% |
| DOGE-USD | ALL_MATCHES | 40 | 72.50% | 15.50% | 36.15% | 47.55% | -8.48% | -31.93% | 22.24% | 43.08% | 64.24% | 52.50% | 1.97% | 16.02% | 82.47% |
| DOGE-USD | SAME_BTC_REGIME | 21 | 90.48% | 23.14% | 41.46% | 53.58% | -8.37% | -16.39% | 23.68% | 44.13% | 64.24% | 57.14% | 3.08% | 8.64% | 28.58% |
| DOGE-USD | SAME_ASSET_REGIME | 17 | 88.24% | 22.63% | 31.89% | 57.85% | -7.10% | -21.57% | 23.41% | 31.89% | 72.64% | 52.94% | 0.86% | 8.64% | 49.34% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 16 | 87.50% | 21.42% | 28.53% | 47.78% | -7.73% | -22.86% | 22.75% | 28.53% | 57.03% | 50.00% | 0.11% | 5.93% | 19.21% |
| SOL-USD | ALL_MATCHES | 40 | 72.50% | 11.48% | 21.00% | 58.48% | -4.56% | -17.94% | 17.23% | 29.84% | 70.85% | 55.00% | 4.29% | 59.90% | 104.15% |
| SOL-USD | SAME_BTC_REGIME | 14 | 100.00% | 18.33% | 27.08% | 49.62% | -2.58% | -14.51% | 28.38% | 45.29% | 65.14% | 57.14% | 37.49% | 67.31% | 137.43% |
| SOL-USD | SAME_ASSET_REGIME | 14 | 85.71% | 15.36% | 20.83% | 29.51% | -2.58% | -22.05% | 24.18% | 30.07% | 52.22% | 50.00% | 25.73% | 81.58% | 138.73% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 11 | 100.00% | 16.07% | 24.96% | 29.72% | -2.05% | -7.89% | 29.47% | 40.25% | 53.03% | 54.55% | 55.80% | 74.90% | 158.51% |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 17 | 88.24% | 9.08% | -4.42% | 15.90% | 41.18% | -13.16% | 35.16% |
| BTC-USD | HISTORICAL_BTC_BULL | 11 | 72.73% | 14.00% | -1.22% | 58.04% | 72.73% | 55.25% | 141.90% |
| BTC-USD | HISTORICAL_BTC_DISTRIBUTION | 3 | 100.00% | 11.10% | 0.00% | 34.10% | 100.00% | 19.41% | 38.76% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 9 | 66.67% | 5.22% | -4.58% | 27.16% | 55.56% | 2.26% | 64.01% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 21 | 90.48% | 23.14% | -8.37% | 44.13% | 57.14% | 3.08% | 62.44% |
| DOGE-USD | HISTORICAL_BTC_BULL | 15 | 53.33% | 8.30% | -9.41% | 49.61% | 46.67% | -14.77% | 81.07% |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 100.00% | 11.10% | 0.00% | 36.94% | 100.00% | 19.41% | 36.94% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 3 | 33.33% | -21.24% | -21.24% | 7.30% | 33.33% | -7.71% | 89.52% |
| SOL-USD | HISTORICAL_BTC_BEAR | 14 | 100.00% | 18.33% | -2.58% | 45.29% | 57.14% | 37.49% | 104.25% |
| SOL-USD | HISTORICAL_BTC_BULL | 9 | 44.44% | -2.70% | -13.16% | 10.45% | 33.33% | -6.36% | 16.92% |
| SOL-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 100.00% | 15.09% | 0.00% | 23.49% | 100.00% | 92.57% | 95.28% |
| SOL-USD | HISTORICAL_BTC_MIXED | 1 | 100.00% | 104.48% | -3.96% | 120.09% | 100.00% | 307.28% | 352.55% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 15 | 60.00% | 0.71% | -4.54% | 18.59% | 60.00% | 6.32% | 54.46% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 21 | 85.71% | 9.08% | -4.42% | 28.52% | 47.62% | -13.16% | 45.05% |
| BTC-USD | HISTORICAL_ASSET_BULL | 7 | 85.71% | 11.20% | -0.49% | 58.04% | 85.71% | 74.76% | 198.54% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 3 | 100.00% | 10.41% | 0.00% | 66.00% | 66.67% | 8.80% | 68.47% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 9 | 55.56% | 2.92% | -4.58% | 24.82% | 55.56% | 2.26% | 64.01% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 17 | 88.24% | 22.63% | -7.10% | 31.89% | 52.94% | 0.86% | 64.24% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 8 | 62.50% | 9.70% | -5.90% | 46.27% | 75.00% | 16.61% | 96.16% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 100.00% | 36.77% | -11.51% | 42.76% | 100.00% | 9.69% | 61.11% |
| DOGE-USD | HISTORICAL_ASSET_MIXED | 3 | 100.00% | 16.41% | -9.41% | 42.38% | 33.33% | -31.97% | 42.38% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 10 | 40.00% | -1.50% | -12.62% | 20.06% | 30.00% | -17.60% | 64.60% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 14 | 85.71% | 15.36% | -2.58% | 30.07% | 50.00% | 25.73% | 104.25% |
| SOL-USD | HISTORICAL_ASSET_BULL | 4 | 75.00% | 10.75% | -9.90% | 39.35% | 75.00% | 58.65% | 169.92% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 3 | 100.00% | 10.45% | 0.00% | 63.57% | 33.33% | -0.73% | 66.80% |
| SOL-USD | HISTORICAL_ASSET_MIXED | 2 | 0.00% | -4.97% | -6.37% | 5.09% | 0.00% | -3.20% | 5.09% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 17 | 64.71% | 2.92% | -4.58% | 24.82% | 64.71% | 6.32% | 47.21% |

## Top regime-adjusted matches

The table below shows the top matches separately for each target, so BTC does not hide SOL and DOGE.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | XRP-USD | 2026-01-05 | 88.54% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 8.98% | 0.00% | 8.98% | -15.55% | -19.71% | 8.98% |
| BTC-USD | BTC-USD | 2018-10-19 | 88.22% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 7.78% | -5.63% | 14.99% | 13.45% | -5.63% | 14.99% |
| BTC-USD | ETH-USD | 2025-12-31 | 87.88% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 6.28% | 0.00% | 10.59% | -22.79% | -28.34% | 10.59% |
| BTC-USD | SOL-USD | 2026-01-03 | 87.71% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 15.64% | 0.00% | 19.40% | -18.05% | -23.73% | 19.40% |
| BTC-USD | 1INCH-USD | 2024-07-06 | 86.67% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 19.12% | -11.35% | 19.92% | 101.40% | -11.35% | 137.19% |
| BTC-USD | NEO-USD | 2018-10-19 | 86.63% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 24.31% | -8.94% | 35.16% | 24.79% | -8.94% | 35.16% |
| BTC-USD | XTZ-USD | 2026-01-05 | 86.50% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 9.21% | 0.00% | 15.85% | -31.20% | -34.31% | 15.85% |
| BTC-USD | 1INCH-USD | 2026-01-02 | 86.42% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 10.40% | -2.51% | 11.14% | -26.00% | -27.22% | 11.14% |
| BTC-USD | OMG-USD | 2018-10-19 | 85.88% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 6.73% | -17.83% | 7.53% | 45.05% | -17.83% | 45.05% |
| BTC-USD | ETC-USD | 2018-10-19 | 85.82% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -0.17% | -12.72% | 12.45% | 12.77% | -12.72% | 13.63% |
| DOGE-USD | VET-USD | 2022-03-24 | 90.42% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 22.63% | -3.05% | 23.68% | 9.84% | -3.05% | 50.90% |
| DOGE-USD | OP-USD | 2026-01-01 | 90.25% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 41.98% | -7.10% | 49.82% | -15.88% | -18.56% | 49.82% |
| DOGE-USD | ADA-USD | 2022-03-22 | 89.51% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 12.42% | -10.22% | 12.42% | -7.62% | -10.22% | 22.52% |
| DOGE-USD | DASH-USD | 2022-03-22 | 89.07% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 14.27% | -10.11% | 17.74% | -0.65% | -10.11% | 27.95% |
| DOGE-USD | BAT-USD | 2018-10-19 | 88.96% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 17.64% | -16.39% | 17.64% | 80.49% | -16.39% | 80.49% |
| DOGE-USD | NEO-USD | 2022-03-22 | 88.95% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 31.89% | -6.02% | 31.89% | 3.42% | -6.02% | 39.93% |
| DOGE-USD | LTC-USD | 2018-04-22 | 88.85% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -25.45% | -34.83% | 0.00% | -25.29% | -37.65% | 0.00% |
| DOGE-USD | XTZ-USD | 2026-01-05 | 88.25% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 9.21% | 0.00% | 15.85% | -31.20% | -34.31% | 15.85% |
| DOGE-USD | INJ-USD | 2022-03-24 | 87.98% | BEAR | BEAR | SAME_BTC_AND_ASSET | HIGH_SPIKE_60D | 20.22% | -1.35% | 21.97% | 28.58% | -1.35% | 76.25% |
| DOGE-USD | QTUM-USD | 2022-07-25 | 87.97% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -21.47% | -29.34% | 7.38% | -34.87% | -34.93% | 7.38% |
| SOL-USD | ENJ-USD | 2018-10-19 | 82.73% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 130.26% | -26.20% | 130.26% | 394.56% | -26.20% | 533.03% |
| SOL-USD | EOS-USD | 2018-11-03 | 81.13% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 29.01% | -3.10% | 50.33% | 88.25% | -3.10% | 105.67% |
| SOL-USD | RUNE-USD | 2026-01-06 | 80.30% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 20.91% | 0.00% | 53.03% | -4.33% | -22.03% | 53.03% |
| SOL-USD | SOL-USD | 2026-01-03 | 79.66% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 15.64% | 0.00% | 19.40% | -18.05% | -23.73% | 19.40% |
| SOL-USD | NEAR-USD | 2025-12-31 | 79.00% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 14.61% | -7.58% | 16.66% | 55.80% | -7.58% | 106.31% |
| SOL-USD | QTUM-USD | 2018-10-24 | 78.50% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 13.12% | -5.39% | 29.47% | 61.55% | -5.39% | 61.55% |
| SOL-USD | XTZ-USD | 2025-03-11 | 78.15% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 29.72% | -7.89% | 29.72% | 59.35% | -7.89% | 99.97% |
| SOL-USD | XTZ-USD | 2018-10-29 | 77.64% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 12.52% | -2.05% | 24.86% | 158.51% | -2.05% | 185.30% |
| SOL-USD | KAVA-USD | 2026-01-05 | 77.23% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 20.58% | 0.00% | 30.18% | -12.71% | -19.16% | 30.18% |
| SOL-USD | BTC-USD | 2026-01-05 | 76.59% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 9.26% | -0.44% | 10.73% | -13.16% | -17.95% | 10.73% |

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

Generato: 2026-08-11 05:21 UTC


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
| BTC | 63.976 $ | -4 | DEBOLE / NON CONFERMATO | STAGE 4 / MARKDOWN | COMPRESSIONE / TRIANGOLO POSSIBILE | ACCUMULO POSSIBILE / RANGE BASSO | BASSO | RIDUCI RISCHIO / NO LONG A LEVA |
| SOL | 75,98 $ | -3 | DEBOLE / NON CONFERMATO | STAGE 4 / MARKDOWN | MASSIMI E MINIMI DECRESCENTI | ACCUMULO POSSIBILE / RANGE BASSO | BASSO | NON INSEGUIRE / TAKE PROFIT SU SPIKE |
| DOGE | 0.07000 $ | -2 | DEBOLE / NON CONFERMATO | STAGE 4 / MARKDOWN | COMPRESSIONE / TRIANGOLO POSSIBILE | SPRING / TEST POSSIBILE | BASSO | NO LONG / SHORT SOLO DOPO SPIKE E REJECTION |

## Punteggi per area

| Asset | Trend | Struttura | Momentum | Volume | Prezzo | Candela | Wyckoff | Totale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | -4 | 0 | -1 | +1 | 0 | 0 | 0 | -4 |
| SOL | -4 | -2 | +3 | 0 | 0 | 0 | 0 | -3 |
| DOGE | -4 | 0 | +2 | -1 | 0 | 0 | +1 | -2 |

## Livelli tecnici

| Asset | Supporto | Resistenza | Breakout 60g | Breakdown 60g | ATR14 | Rendimento 30g | Rendimento 90g |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 62.227 $ | 64.186 $ | 67.248 $ | 57.748 $ | 1,93% | 0,16% | -20,59% |
| SOL | 74,16 $ | 75,94 $ | 83,81 $ | 62,00 $ | 2,54% | -1,40% | -19,66% |
| DOGE | 0.06961 $ | 0.07117 $ | 0.09169 $ | 0.06797 $ | 2,31% | -4,67% | -36,51% |

## Lettura dettagliata

### BTC

- Prezzo: **63.976 $**
- Score classico: **-4 / 12**
- Verdetto: **DEBOLE / NON CONFERMATO**
- Azione coerente: **RIDUCI RISCHIO / NO LONG A LEVA**
- Volatilità tecnica locale: **BASSO** — ATR14 1,93%; distanza supporto 2,70%; distanza resistenza 0,44%

Dettaglio:

- Trend: **-4** — prezzo sotto MA200 daily; MA200 daily in discesa; STAGE 4 / MARKDOWN
- Stage weekly: **STAGE 4 / MARKDOWN** — Prezzo sotto MA30 weekly con MA30 in discesa.
- Struttura: **0** — COMPRESSIONE / TRIANGOLO POSSIBILE
- Momentum: **-1** — RSI neutrale 48.3; RSI in peggioramento; MACD sopra signal; istogramma MACD in peggioramento
- Volume: **+1** — OBV sopra media; CMF neutrale -0.03; volume ratio 1.01
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **0** — Doji / indecisione
- Wyckoff: **0** — ACCUMULO POSSIBILE / RANGE BASSO. Prezzo nella metà bassa del range, ma senza spring confermato.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 48.32 |
| MACD histogram | 31.99916 |
| CMF20 | -0.031 |
| Volume ratio 20 | 1.01 |
| MA20 | 64.255 $ |
| MA50 | 63.331 $ |
| MA100 | 67.715 $ |
| MA200 | 70.002 $ |
| Pendenza MA50 20g | +0,38% |
| Pendenza MA200 60g | -10,26% |
| Bollinger width | 5,17% |
| Bollinger position | 0.39 |

### SOL

- Prezzo: **75,98 $**
- Score classico: **-3 / 12**
- Verdetto: **DEBOLE / NON CONFERMATO**
- Azione coerente: **NON INSEGUIRE / TAKE PROFIT SU SPIKE**
- Volatilità tecnica locale: **BASSO** — ATR14 2,54%; distanza supporto 2,14%; distanza resistenza 0,25%

Dettaglio:

- Trend: **-4** — prezzo sotto MA200 daily; MA200 daily in discesa; STAGE 4 / MARKDOWN
- Stage weekly: **STAGE 4 / MARKDOWN** — Prezzo sotto MA30 weekly con MA30 in discesa.
- Struttura: **-2** — MASSIMI E MINIMI DECRESCENTI
- Momentum: **+3** — RSI sano 53.4; RSI in miglioramento; MACD sopra signal; istogramma MACD in miglioramento
- Volume: **0** — OBV sopra media; CMF negativo -0.08; volume ratio 0.93
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **0** — ACCUMULO POSSIBILE / RANGE BASSO. Prezzo nella metà bassa del range, ma senza spring confermato.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 53.36 |
| MACD histogram | 0.30989 |
| CMF20 | -0.078 |
| Volume ratio 20 | 0.93 |
| MA20 | 74,40 $ |
| MA50 | 75,37 $ |
| MA100 | 77,56 $ |
| MA200 | 83,26 $ |
| Pendenza MA50 20g | +2,97% |
| Pendenza MA200 60g | -17,35% |
| Bollinger width | 8,00% |
| Bollinger position | 0.72 |

### DOGE

- Prezzo: **0.07000 $**
- Score classico: **-2 / 12**
- Verdetto: **DEBOLE / NON CONFERMATO**
- Azione coerente: **NO LONG / SHORT SOLO DOPO SPIKE E REJECTION**
- Volatilità tecnica locale: **BASSO** — ATR14 2,31%; distanza supporto 0,34%; distanza resistenza 1,89%

Dettaglio:

- Trend: **-4** — prezzo sotto MA200 daily; medie daily allineate ribassiste; MA50 daily in discesa; MA200 daily in discesa; STAGE 4 / MARKDOWN
- Stage weekly: **STAGE 4 / MARKDOWN** — Prezzo sotto MA30 weekly con MA30 in discesa.
- Struttura: **0** — COMPRESSIONE / TRIANGOLO POSSIBILE
- Momentum: **+2** — RSI neutrale 44.1; MACD sopra signal; istogramma MACD in miglioramento
- Volume: **-1** — OBV sotto media; CMF neutrale -0.03; volume ratio 0.67
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **+1** — SPRING / TEST POSSIBILE. Ha bucato un minimo importante e ha recuperato: possibile spring, da confermare.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 44.09 |
| MACD histogram | 0.00022 |
| CMF20 | -0.026 |
| Volume ratio 20 | 0.67 |
| MA20 | 0.07029 $ |
| MA50 | 0.07273 $ |
| MA100 | 0.08548 $ |
| MA200 | 0.09177 $ |
| Pendenza MA50 20g | -7,90% |
| Pendenza MA200 60g | -16,97% |
| Bollinger width | 6,72% |
| Bollinger position | 0.41 |

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

Generato: 2026-08-11 05:22 UTC


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
| BTC | 63.976 $ | Doppio minimo | CANDIDATO | rialzista | n/a | 71.619 $ | n/a | 4,59% | Fib 23,6% NON ATTIVO (0) @ 67.080 $ | NEL RANGE | 62.553 $ |
| SOL | 75,98 $ | Doppio minimo | CANDIDATO | rialzista | n/a | 99,70 $ | n/a | 10,30% | Fib 23,6% REJECTION (0) @ 77,20 $ | NEL RANGE | 73,40 $ |
| DOGE | 0.07000 $ | Doppio minimo | CANDIDATO | rialzista | n/a | 0.07931 $ | n/a | 5,43% | Fib 23,6% NON ATTIVO (0) @ 0.08013 $ | NEL RANGE | 0.06961 $ |

## BTC

![Classic visual BTC](classic_visual_BTC.png)

- Pattern principale: **Doppio minimo**
- Stato pattern: **CANDIDATO** (0)
- Famiglia: **rialzista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-06-18 -> 2026-08-03**
- Età formazione: **8 giorni**
- Breakout pattern: **n/a**
- Età breakout: **n/a**
- Neckline: **66.910 $**
- Target teorico: **71.619 $**
- Progresso verso target: **n/a**
- Distanza dalla neckline: **4,59%**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 23,6% NON ATTIVO (0) @ 67.080 $** — Swing DOWN 2026-05-06 82.792 -> 2026-08-03 62.227; livello più vicino 23.6% a 67.080; stato NON ATTIVO; confluenza: resistenza tecnica, neckline rialzista.
- Invalidazione: **65.572 $**
- Relazione prezzo/neckline: **sotto neckline**
- Dettaglio: Due minimi simili vicino a 62.201 tra 2026-06-18 e 2026-08-03. Neckline stimata: 66.910. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 8 giorni. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **NEL RANGE**
- Supporto: **62.553 $**
- Resistenza: **65.508 $**
- Breakout 60g: **67.248 $**
- Breakdown 60g: **57.748 $**
- RSI14: **48.72**
- ATR14: **1,92%**
- Volume ratio 20g: **1.00**
- Rendimento 30g: **+0,27%**
- Rendimento 90g: **-20,50%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Doppio minimo | CANDIDATO | 0 | rialzista | 66.910 $ | n/a | n/a | 71.619 $ | n/a | 4,59% | 65.572 $ | Due minimi simili a 62.201 $ e 62.227 $. Neckline circa 66.910 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 8 giorni. |
| Doppio massimo | CANDIDATO | 0 | ribassista | 57.748 $ | n/a | n/a | 48.247 $ | n/a | 10,79% | 58.903 $ | Due massimi simili a 67.248 $ e 66.910 $. Neckline circa 57.748 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 21 giorni. |

## SOL

![Classic visual SOL](classic_visual_SOL.png)

- Pattern principale: **Doppio minimo**
- Stato pattern: **CANDIDATO** (0)
- Famiglia: **rialzista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-06-19 -> 2026-08-01**
- Età formazione: **10 giorni**
- Breakout pattern: **n/a**
- Età breakout: **n/a**
- Neckline: **83,81 $**
- Target teorico: **99,70 $**
- Progresso verso target: **n/a**
- Distanza dalla neckline: **10,30%**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 23,6% REJECTION (0) @ 77,20 $** — Swing DOWN 2026-05-11 98,27 -> 2026-08-01 70,69; livello più vicino 23.6% a 77,20; stato REJECTION; confluenza: nessuna confluenza indipendente.
- Invalidazione: **82,13 $**
- Relazione prezzo/neckline: **sotto neckline**
- Dettaglio: Due minimi simili vicino a 67,92 tra 2026-06-19 e 2026-08-01. Neckline stimata: 83,81. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 10 giorni. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Doji / indecisione**
- Stato prezzo: **NEL RANGE**
- Supporto: **73,40 $**
- Resistenza: **78,73 $**
- Breakout 60g: **83,81 $**
- Breakdown 60g: **62,00 $**
- RSI14: **54.22**
- ATR14: **2,53%**
- Volume ratio 20g: **0.93**
- Rendimento 30g: **-1,10%**
- Rendimento 90g: **-19,41%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Doppio minimo | CANDIDATO | 0 | rialzista | 78,73 $ | n/a | n/a | 86,76 $ | n/a | 3,61% | 77,15 $ | Due minimi simili a 73,40 $ e 70,69 $. Neckline circa 78,73 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 10 giorni. |
| Triangolo discendente possibile | CANDIDATO | 0 | ribassista | n/a | n/a | n/a | n/a | n/a | n/a | n/a | Massimi decrescenti e supporto quasi piatto. Stato: CANDIDATO; il pattern non ha una neckline univoca da usare per il lifecycle. |
| Doppio massimo | CANDIDATO | 0 | ribassista | 64,42 $ | n/a | n/a | 50,11 $ | n/a | 17,95% | 65,71 $ | Due massimi simili a 75,94 $ e 78,73 $. Neckline circa 64,42 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 21 giorni. |
| Testa e spalle inverso | CANDIDATO | 0 | rialzista | 79,35 $ | n/a | n/a | 94,28 $ | n/a | 4,44% | 77,76 $ | Spalla sinistra 67,92 $, testa 64,42 $, spalla destra 73,40 $. Neckline circa 79,35 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 25 giorni. |
| Testa e spalle | TARGET RAGGIUNTO | 0 | ribassista | 82,57 $ | 2026-05-28 | 75g | 66,88 $ | 42,00% | n/a | 84,22 $ | Spalla sinistra 88,05 $, testa 98,27 $, spalla destra 87,79 $. Neckline circa 82,57 $. Breakout neckline: 2026-05-28 (75 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 66,88 $; progresso: 42,00%; prezzo sotto neckline. |

## DOGE

![Classic visual DOGE](classic_visual_DOGE.png)

- Pattern principale: **Doppio minimo**
- Stato pattern: **CANDIDATO** (0)
- Famiglia: **rialzista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-07-24 -> 2026-08-06**
- Età formazione: **5 giorni**
- Breakout pattern: **n/a**
- Età breakout: **n/a**
- Neckline: **0.07380 $**
- Target teorico: **0.07931 $**
- Progresso verso target: **n/a**
- Distanza dalla neckline: **5,43%**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 23,6% NON ATTIVO (0) @ 0.08013 $** — Swing DOWN 2026-05-14 0.11825 -> 2026-08-06 0.06835; livello più vicino 23.6% a 0.08013; stato NON ATTIVO; confluenza: nessuna confluenza indipendente.
- Invalidazione: **0.07233 $**
- Relazione prezzo/neckline: **sotto neckline**
- Dettaglio: Due minimi simili vicino a 0.06829 tra 2026-07-24 e 2026-08-06. Neckline stimata: 0.07380. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 5 giorni. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **NEL RANGE**
- Supporto: **0.06961 $**
- Resistenza: **0.07117 $**
- Breakout 60g: **0.09169 $**
- Breakdown 60g: **0.06797 $**
- RSI14: **44.73**
- ATR14: **2,30%**
- Volume ratio 20g: **0.67**
- Rendimento 30g: **-4,46%**
- Rendimento 90g: **-36,37%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Doppio massimo | MATURO | -1 | ribassista | 0.07809 $ | 2026-06-24 | 48g | 0.06035 $ | 45,63% | n/a | 0.07966 $ | Due massimi simili a 0.09584 $ e 0.09169 $. Neckline circa 0.07809 $. Breakout neckline: 2026-06-24 (48 giorni fa). Stato: MATURO. Target teorico: 0.06035 $; progresso: 45,63%; prezzo sotto neckline. |
| Doppio minimo | CANDIDATO | 0 | rialzista | 0.07380 $ | n/a | n/a | 0.07931 $ | n/a | 5,43% | 0.07233 $ | Due minimi simili a 0.06829 $ e 0.06835 $. Neckline circa 0.07380 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 5 giorni. |
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

Generato: 2026-08-11 05:21 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [fractal_path_tracker.md](fractal_path_tracker.md)

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-08-11**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-01-26**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **75,98 $**
- Verdetto principale: **ANALOGIA DEBOLE / SCENARIO SECONDARIO**
- Somiglianza strutturale: **+57,11%**
- Aderenza live principale: **+69,55%**
- Errore medio live principale: **15,23%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE SOLO DI CONTESTO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **66**
- Osservazioni inclusive dal bottom: **67**
- Osservazioni da inizio programma/scanner: **40**
- Errore assoluto medio dal bottom: **11,52%**
- Errore assoluto medio da inizio programma: **15,23%**
- Gap firmato medio ultimi 7 giorni: **-16,72%**
- Errore assoluto medio ultimi 7 giorni: **16,72%**
- Gap ultimo giorno: **-16,26%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **-16,26%**
- Gap firmato medio 7g: **-16,72%**
- Errore assoluto medio 7g: **16,72%**
- Variazione recente gap: **-0,35%**
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
| 57 | 2026-08-02 | 2023-01-17 | 73,45 $ | 83,36 $ | -11,89% | da inizio programma |
| 58 | 2026-08-03 | 2023-01-18 | 73,47 $ | 81,50 $ | -9,85% | da inizio programma |
| 59 | 2026-08-04 | 2023-01-19 | 73,72 $ | 83,07 $ | -11,25% | da inizio programma |
| 60 | 2026-08-05 | 2023-01-20 | 73,96 $ | 89,33 $ | -17,20% | da inizio programma |
| 61 | 2026-08-06 | 2023-01-21 | 72,58 $ | 89,73 $ | -19,11% | da inizio programma |
| 62 | 2026-08-07 | 2023-01-22 | 73,64 $ | 89,50 $ | -17,72% | da inizio programma |
| 63 | 2026-08-08 | 2023-01-23 | 75,97 $ | 90,34 $ | -15,91% | da inizio programma |
| 64 | 2026-08-09 | 2023-01-24 | 76,21 $ | 89,17 $ | -14,53% | da inizio programma |
| 65 | 2026-08-10 | 2023-01-25 | 76,21 $ | 91,07 $ | -16,31% | da inizio programma |
| 66 | 2026-08-11 | 2023-01-26 | 75,98 $ | 90,73 $ | -16,26% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-08-18 | 92,46 $ | 77,43 $ | 75,34 $ / 78,43 $ | no | n/a | n/a | n/a |
| 14g | 2026-08-25 | 85,95 $ | 71,98 $ | 71,98 $ / 78,43 $ | no | n/a | n/a | n/a |
| 21g | 2026-09-01 | 93,06 $ | 77,93 $ | 71,42 $ / 80,19 $ | no | n/a | n/a | n/a |
| 28g | 2026-09-08 | 94,33 $ | 79,00 $ | 71,42 $ / 81,91 $ | no | n/a | n/a | n/a |
| 35g | 2026-09-15 | 92,48 $ | 77,44 $ | 71,42 $ / 81,91 $ | no | n/a | n/a | n/a |
| 42g | 2026-09-22 | 80,21 $ | 67,17 $ | 67,17 $ / 81,91 $ | no | n/a | n/a | n/a |
| 49g | 2026-09-29 | 98,69 $ | 82,64 $ | 66,59 $ / 82,64 $ | no | n/a | n/a | n/a |
| 56g | 2026-10-06 | 111,61 $ | 93,47 $ | 66,59 $ / 93,47 $ | no | n/a | n/a | n/a |
| 63g | 2026-10-13 | 110,43 $ | 92,48 $ | 66,59 $ / 93,52 $ | no | n/a | n/a | n/a |
| 70g | 2026-10-20 | 110,47 $ | 92,51 $ | 66,59 $ / 93,94 $ | no | n/a | n/a | n/a |
| 77g | 2026-10-27 | 119,75 $ | 100,28 $ | 66,59 $ / 100,28 $ | no | n/a | n/a | n/a |
| 84g | 2026-11-03 | 111,27 $ | 93,18 $ | 66,59 $ / 100,57 $ | no | n/a | n/a | n/a |
| 91g | 2026-11-10 | 116,10 $ | 97,23 $ | 66,59 $ / 100,57 $ | no | n/a | n/a | n/a |
| 98g | 2026-11-17 | 113,64 $ | 95,16 $ | 66,59 $ / 100,57 $ | no | n/a | n/a | n/a |
| 105g | 2026-11-24 | 106,36 $ | 89,07 $ | 66,59 $ / 100,57 $ | no | n/a | n/a | n/a |
| 112g | 2026-12-01 | 105,70 $ | 88,51 $ | 66,59 $ / 100,57 $ | no | n/a | n/a | n/a |
| 119g | 2026-12-08 | 104,30 $ | 87,34 $ | 66,59 $ / 100,57 $ | no | n/a | n/a | n/a |
| 126g | 2026-12-15 | 105,65 $ | 88,47 $ | 66,59 $ / 100,57 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 28 | 42,86% | 8,14% | 13,04% |
| 14g | 21 | 19,05% | 17,92% | 12,01% |
| 21g | 14 | 21,43% | 26,05% | 14,61% |
| 28g | 7 | 28,57% | 28,97% | 16,15% |
| 35g | 0 | n/a | n/a | n/a |
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

Ultima lettura salvata: **2026-08-11** — SOL 75,98 $, gap -16,26%, somiglianza +57,11%.

Nel report principale lascio solo il link, così non diventa troppo lungo.

<!-- SOL_BTC_FRACTAL_HISTORY_END -->

</details>
<!-- COMPACT_SECTION_END:fractal_path -->

<!-- COMPACT_SECTION_START:exchange_microstructure -->
<details>
<summary><strong>🏦 Dati exchange, liquidità e leva</strong></summary>

<!-- EXCHANGE_MICROSTRUCTURE_START -->
# Dati exchange, liquidità e leva

Generato: 2026-08-11 05:22 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [exchange_microstructure_report.md](exchange_microstructure_report.md)

Questo modulo legge Kraken Futures, Bitget Futures e KuCoin Futures come nucleo derivati. OKX e Coinbase vengono raccolti come fonti ausiliarie non pesate.
Non modifica la formula matematica di RSI, Fibonacci o Wyckoff: controlla se quei segnali sono sostenuti da acquisti, vendite, OI, funding e liquidità.

**Limite importante:** questo nucleo non assume disponibile un feed pubblico completo delle liquidazioni. La componente liquidazioni resta neutrale; le zone future restano stime di pressione, non dati certi delle singole posizioni.

Diagnostica completa: [exchange_source_diagnostics.md](exchange_source_diagnostics.md)

## Sintesi

| Asset | Prezzo | Exchange | Segnale candidato | Peso Global | Bias exchange | Confidenza | Copertura | Funding 8h eq. | OI 24h | Taker flow (campione/4h) | Book 0,5% | Liq long campione | Liq short campione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 64.025 $ | 3 | 0 | 0 | MISTA / NEUTRALE | BASSA | 100% | +0,0075% | +4,21% | 1,94 | -7,22% | 0 $ | 0 $ |
| SOL | 76,02 $ | 3 | 0 | 0 | LEGGERMENTE POSITIVA / NON PESATA | BASSA | 100% | +0,0099% | +0,02% | 1,13 | +4,16% | 0 $ | 0 $ |
| DOGE | 0.07002 $ | 3 | 0 | 0 | MISTA / NEUTRALE | BASSA | 100% | +0,0098% | +1,22% | 0,86 | +10,68% | 0 $ | 0 $ |

Il segnale candidato è limitato a **±1**, ma il peso nel Global resta **0** finché il tracker a 7 giorni non raggiunge 30 controlli, almeno 55% di accuratezza e return corretto direzione positivo. Un singolo muro o funding non basta.

La colonna taker usa un campione recente nel primo run. Dopo almeno 3 fotografie distribuite su almeno 45 minuti viene sostituita automaticamente dalla media intraday 4h.

## Dati separati per exchange

| Asset | Exchange | Stato | Funding 8h eq. | Open interest | Taker flow | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | Kraken | OK | +0,0049% | 145,85 mln $ | 5,63 | -11,82% |
| BTC | Bitget | OK | +0,0100% | 2,50 mld $ | 17,57 | +18,27% |
| BTC | Kucoin | OK | +0,0100% | 1,44 mld $ | 3,39 | +0,31% |
| SOL | Kraken | OK | -0,0083% | 21,62 mln $ | 1,81 | -17,33% |
| SOL | Bitget | OK | +0,0100% | 348,99 mln $ | 1,48 | -8,69% |
| SOL | Kucoin | OK | +0,0096% | 232,21 mln $ | 0,30 | -9,28% |
| DOGE | Kraken | OK | +0,0183% | 4,15 mln $ | 0,29 | -14,90% |
| DOGE | Bitget | OK | +0,0100% | 95,62 mln $ | 0,27 | -5,69% |
| DOGE | Kucoin | OK | +0,0100% | 117,45 mln $ | 0,09 | -7,04% |

Kraken, Bitget e KuCoin contribuiscono a funding normalizzato, open interest, trade aggressivi e order book. Non viene inventato un long/short ratio pubblico né un feed completo delle liquidazioni.

## Conferme per indicatori tecnici

### BTC

- Score grezzo exchange: **+0,75**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 1, accuratezza +100,00%.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 1, bear 1, divergenze 1.
- Flusso taker/order book: **+1,75**.
- OI/funding/basis: **-1,00**.
- Affollamento long/short: **+0,00**.
- Liquidazioni: **NON PESATE / FEED COMPLETO NON ASSUNTO DISPONIBILE**.
- **Wyckoff:** Possibile accumulazione ancora neutrale nei dati exchange.
- **Fibonacci:** Fibonacci non_attivo; nessuna conferma exchange netta. Confluenza tecnica dichiarata: resistenza tecnica, neckline rialzista.
- **RSI:** RSI in zona non estrema o flusso exchange non abbastanza netto.
- **Pattern:** I pattern candidati restano non operativi: i dati exchange possono solo preparare la conferma.
- **Breakout/breakdown:** Prezzo non abbastanza vicino a un livello chiave o flusso non netto.
- **Mappa liquidità attuale:** muro bid: n/a; muro ask: n/a

![Microstruttura exchange BTC](exchange_microstructure_BTC.png)

### SOL

- Score grezzo exchange: **+2,00**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 1, accuratezza +0,00%.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 1, bear 1, divergenze 0.
- Flusso taker/order book: **+1,75**.
- OI/funding/basis: **+0,00**.
- Affollamento long/short: **+0,00**.
- Liquidazioni: **NON PESATE / FEED COMPLETO NON ASSUNTO DISPONIBILE**.
- **Wyckoff:** Markdown non pienamente confermato: compare assorbimento compratore.
- **Fibonacci:** Fibonacci rejection; nessuna conferma exchange netta.
- **RSI:** RSI in zona non estrema o flusso exchange non abbastanza netto.
- **Pattern:** I pattern candidati restano non operativi: i dati exchange possono solo preparare la conferma.
- **Breakout/breakdown:** Prezzo non abbastanza vicino a un livello chiave o flusso non netto.
- **Mappa liquidità attuale:** muro bid: n/a; muro ask: n/a

![Microstruttura exchange SOL](exchange_microstructure_SOL.png)

### DOGE

- Score grezzo exchange: **+0,75**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 2, accuratezza +100,00%.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 0, bear 3, divergenze 0.
- Flusso taker/order book: **+0,75**.
- OI/funding/basis: **+0,00**.
- Affollamento long/short: **+0,00**.
- Liquidazioni: **NON PESATE / FEED COMPLETO NON ASSUNTO DISPONIBILE**.
- **Wyckoff:** Possibile accumulazione ancora neutrale nei dati exchange.
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
| BTC | +80,00% | +9,15% | 0 | n/a | RACCOLTA DATI | 0,00 | +80,00% | +9,15% |
| SOL | +72,50% | +11,48% | 0 | n/a | RACCOLTA DATI | 0,00 | +72,50% | +11,48% |
| DOGE | +72,50% | +15,50% | 0 | n/a | RACCOLTA DATI | 0,00 | +72,50% | +15,50% |

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

Generato: 2026-08-11 05:22 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [exchange_signal_tracker_report.md](exchange_signal_tracker_report.md)

Questo tracker verifica se il segnale candidato exchange ±1 anticipa correttamente la direzione del prezzo a 1/3/7/14/30 giorni.
Il peso Global resta 0 finché l'orizzonte 7g non ha almeno 30 controlli, accuratezza almeno 55% e return corretto direzione positivo. L'overlay a 30g ha un gate separato.

Controlli maturati completati in questa esecuzione: **15**.

## Ultime fotografie giornaliere

| Data | Asset | Prezzo | Versione | Calibrazione | Candidato | Peso Global | Score raw | Confidenza | Taker 4h | OI 24h | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08-11 | BTC | 64.025,10 | V2.1.3 | OK | 0 | 0 | 0,75 | BASSA | 1,94 | +4,21% | -7,22% |
| 2026-08-11 | DOGE | 0.07002 | V2.1.3 | OK | 0 | 0 | 0,75 | BASSA | 0,86 | +1,22% | +10,68% |
| 2026-08-11 | SOL | 76,02 | V2.1.3 | OK | 0 | 0 | 2,00 | BASSA | 1,13 | +0,02% | +4,16% |
| 2026-08-10 | BTC | 65.017,50 | V2.1.3 | OK | 0 | 0 | 2,12 | MEDIA | 1,64 | +1,08% | -4,44% |
| 2026-08-10 | DOGE | 0.06975 | V2.1.3 | OK | 0 | 0 | 2,62 | MEDIA | 1,96 | +1,46% | +15,23% |
| 2026-08-10 | SOL | 76,63 | V2.1.3 | OK | 0 | 0 | 0,75 | BASSA | 1,26 | -0,14% | -8,62% |
| 2026-08-09 | BTC | 64.760,07 | V2.1.3 | OK | 0 | 0 | 2,12 | MEDIA | 1,35 | -0,59% | +1,41% |
| 2026-08-09 | DOGE | 0.07000 | V2.1.3 | OK | 1 | 0 | 2,62 | MEDIA | 1,41 | -2,68% | +10,90% |
| 2026-08-09 | SOL | 75,97 | V2.1.3 | OK | 1 | 0 | 3,25 | MEDIA | 1,61 | +6,67% | +10,58% |

## Accuratezza direzionale

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 1 | +100,00% | +1,59% | +1,07% | +1,84% | FEEDBACK RAPIDO |
| BTC | 3g | 1 | +100,00% | +1,47% | -1,13% | +3,82% | FEEDBACK RAPIDO |
| BTC | 7g | 1 | +100,00% | +1,35% | -1,18% | +3,82% | FEEDBACK RAPIDO |
| BTC | 14g | 1 | +0,00% | -2,63% | -3,44% | +3,82% | FEEDBACK RAPIDO |
| BTC | 30g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 1g | 2 | +50,00% | +0,20% | -0,04% | +0,81% | FEEDBACK RAPIDO |
| SOL | 3g | 1 | +0,00% | -3,12% | -3,63% | +0,73% | FEEDBACK RAPIDO |
| SOL | 7g | 1 | +0,00% | -6,27% | -6,64% | +0,73% | FEEDBACK RAPIDO |
| SOL | 14g | 1 | +0,00% | -5,72% | -9,55% | +0,73% | FEEDBACK RAPIDO |
| SOL | 30g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 1g | 4 | +50,00% | +1,05% | +0,76% | +2,03% | FEEDBACK RAPIDO |
| DOGE | 3g | 3 | +66,67% | +1,64% | -0,64% | +5,29% | FEEDBACK RAPIDO |
| DOGE | 7g | 2 | +100,00% | +1,07% | -0,93% | +6,44% | FEEDBACK RAPIDO |
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

**SOL** — SOL: i futures sembrano più vulnerabili verso una discesa improvvisa. Non significa che deve scendere, ma se rompe sotto può accelerare. Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale.

**DOGE** — DOGE: i futures sembrano più vulnerabili verso una discesa improvvisa. Non significa che deve scendere, ma se rompe sotto può accelerare. Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale.

| Asset | Prezzo | Funding | OI 24h | Long/Short | Lettura futures | Forza |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 63.976 $ | +0.0100% | -3.64% | 1.25 | Rischio sotto | 2/5 |
| SOL | 75,98 $ | +0.0100% | -0.16% | 2.18 | Rischio sotto | 2/5 |
| DOGE | 0.07000 $ | +0.0100% | -16.17% | 3.42 | Rischio sotto | 2/5 |

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

Generato: 2026-08-11 05:22 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [rsi_multitimeframe_divergence_report.md](rsi_multitimeframe_divergence_report.md)

Il modulo confronta prezzo e RSI 14 sui pivot confermati **daily e weekly**. Riconosce divergenze regolari e nascoste, segnali in formazione, invalidazioni e semplice conferma del momentum.

**Peso operativo: 0.** Non modifica il Global Confluence, non cambia le soglie del Paper Trading e non apre né blocca operazioni. I risultati vengono misurati prima di qualsiasi futura decisione sul peso.

## Sintesi corrente

| Asset   | Daily                       | Stato D    | Weekly              | Stato W    | Lettura weekly                                                                                                                |   Peso |
|:--------|:----------------------------|:-----------|:--------------------|:-----------|:------------------------------------------------------------------------------------------------------------------------------|-------:|
| BTC     | Misto / nessuna divergenza  | CONTESTO   | Bullish regolare    | CONFERMATA | Bullish regolare confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto. |      0 |
| SOL     | Misto / nessuna divergenza  | CONTESTO   | Hidden bearish      | CONFERMATA | Hidden bearish confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto.   |      0 |
| DOGE    | Bullish regolare invalidata | INVALIDATA | Conferma ribassista | CONTESTO   | Prezzo e RSI stanno scendendo insieme: momentum ribassista confermato, nessuna bullish divergence attiva.                     |      0 |

## Dettaglio dei pivot

| Asset   | TF   | Tipo                        | Stato      | Prezzo / RSI      | Pivot confrontati                                                 | Δ prezzo contesto   | Δ RSI contesto   |   Peso |
|:--------|:-----|:----------------------------|:-----------|:------------------|:------------------------------------------------------------------|:--------------------|:-----------------|-------:|
| BTC     | 1D   | Misto / nessuna divergenza  | CONTESTO   | 63.902 $ / 48,30  | n/a                                                               | +0,28%              | 0,58             |      0 |
| BTC     | 1W   | Bullish regolare            | CONFERMATA | 63.902 $ / 39,91  | 2026-06-07 59.109 $ / RSI 34,23 → 2026-07-05 57.748 $ / RSI 38,20 | n/a                 | n/a              |      0 |
| SOL     | 1D   | Misto / nessuna divergenza  | CONTESTO   | 75,76 $ / 53,40   | n/a                                                               | +2,18%              | 8,63             |      0 |
| SOL     | 1W   | Hidden bearish              | CONFERMATA | 75,76 $ / 40,43   | 2026-05-17 98,27 $ / RSI 38,29 → 2026-07-05 83,81 $ / RSI 42,25   | n/a                 | n/a              |      0 |
| DOGE    | 1D   | Bullish regolare invalidata | INVALIDATA | 0.06984 $ / 44,05 | n/a                                                               | -0,70%              | 4,05             |      0 |
| DOGE    | 1W   | Conferma ribassista         | CONTESTO   | 0.06984 $ / 32,91 | n/a                                                               | -10,16%             | -2,22            |      0 |

### BTC

- **1D — Misto / nessuna divergenza / CONTESTO**: Misto / nessuna divergenza. Non esiste una divergenza confermata sugli ultimi pivot.
- **1W — Bullish regolare / CONFERMATA**: Bullish regolare confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto.

### SOL

- **1D — Misto / nessuna divergenza / CONTESTO**: Misto / nessuna divergenza. Non esiste una divergenza confermata sugli ultimi pivot.
- **1W — Hidden bearish / CONFERMATA**: Hidden bearish confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto.

### DOGE

- **1D — Bullish regolare invalidata / INVALIDATA**: La precedente bullish regolare non è più sostenuta dalla relazione corrente tra pivot di prezzo e RSI.
- **1W — Conferma ribassista / CONTESTO**: Prezzo e RSI stanno scendendo insieme: momentum ribassista confermato, nessuna bullish divergence attiva.

## Tracker live delle divergenze confermate

Viene salvato un solo evento per combinazione di asset, timeframe, tipo e coppia di pivot. Gli esiti vengono controllati dopo 30, 60, 90 e 180 giorni.

- Eventi indipendenti salvati: **7**.
- Soglie di lettura: **30 / 60 / 100 controlli**.
- Anche oltre le soglie il peso resta **0** finché non viene presa una decisione esplicita.

| Asset   | TF   | Tipo           |   Orizzonte |   Controlli | Accuratezza   | Return corretto   | Stato         |   Peso |
|:--------|:-----|:---------------|------------:|------------:|:--------------|:------------------|:--------------|-------:|
| DOGE    | 1D   | Hidden bearish |          30 |           1 | +100,00%      | +4,98%            | RACCOLTA DATI |      0 |

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

Generato: 2026-08-11 05:22 UTC


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

| Asset   | Prezzo   |   Punteggio | Verdetto                      | Trend            | Momentum                  | Struttura                                             |   Pattern score | Fibonacci      | Pattern rialzista         | Pattern ribassista           | Supporto   | Resistenza   |
|:--------|:---------|------------:|:------------------------------|:-----------------|:--------------------------|:------------------------------------------------------|----------------:|:---------------|:--------------------------|:-----------------------------|:-----------|:-------------|
| BTC | 63.976 $ | 4 | COSTRUTTIVO MA NON CONFERMATO | Trend misto | Momentum misto | Struttura rialzista con massimi e minimi crescenti | 0 | 0 / NON ATTIVO | Doppio minimo / CANDIDATO | Doppio massimo / CANDIDATO | 62.227 | 66.910 |
| SOL | 75,98 $ | 0 | NEUTRALE / MISTO | Trend misto | Momentum in miglioramento | Struttura ribassista con massimi e minimi decrescenti | 0 | 0 / REJECTION | Doppio minimo / CANDIDATO | Doppio massimo / CANDIDATO | 70,69 | 78,73 |
| DOGE | 0.07000 $ | 0 | NEUTRALE / MISTO | Trend ribassista | Momentum in miglioramento | Compressione / triangolo | 0 | 0 / NON ATTIVO | Doppio minimo / CANDIDATO | Adam and Eve Top / CANDIDATO | 0.06835 | 0.07117 |

## Riepilogo ciclo di vita pattern

| Asset   | Doppio minimo   | Triplo minimo   | Adam/Eve Bottom                 | Doppio massimo   | Triplo massimo   | Adam/Eve Top                 |   Punteggio pattern |
|:--------|:----------------|:----------------|:--------------------------------|:-----------------|:-----------------|:-----------------------------|--------------------:|
| BTC | CANDIDATO | CANDIDATO | Adam and Eve Bottom — CANDIDATO | CANDIDATO | CANDIDATO | Adam and Eve Top — CANDIDATO | 0 |
| SOL | CANDIDATO | CANDIDATO | Adam and Eve Bottom — CANDIDATO | CANDIDATO | CANDIDATO | Adam and Eve Top — CANDIDATO | 0 |
| DOGE | CANDIDATO | CANDIDATO | Adam and Eve Bottom — CANDIDATO | ASSENTE | ASSENTE | Adam and Eve Top — CANDIDATO | 0 |

## Indicatori tecnici

| Asset   |   RSI 14 |   Istogramma MACD | MA20    | MA50    | MA200   | Pendenza MA50 20g   | Pendenza MA200 60g   | Rendimento 30g   | Rendimento 90g   |
|:--------|---------:|------------------:|:--------|:--------|:--------|:--------------------|:---------------------|:-----------------|:-----------------|
| BTC | 48.72 | 36.5741 | 64.258 | 63.332 | 70.003 | 0,40% | -10,12% | 0,34% | -19,30% |
| SOL | 54.22 | 0.32457 | 74,41 | 75,38 | 83,26 | 2,87% | -17,06% | -1,16% | -16,58% |
| DOGE | 44.73 | 0.00023 | 0.07030 | 0.07274 | 0.09177 | -7,44% | -16,72% | -3,69% | -37,89% |

## Dettaglio asset

### BTC

- Prezzo: **63.976 $**
- Punteggio tecnico: **4 / 12**
- Verdetto: **COSTRUTTIVO MA NON CONFERMATO**
- Trend: **Trend misto** (-1)
- Momentum: **Momentum misto** (1)
- Volume: **Volume da accumulazione** (1)
- Struttura: **Struttura rialzista con massimi e minimi crescenti** (2)
  - Dettaglio struttura: Ultimi minimi: 5.775e+04 -> 6.223e+04. Ultimi massimi: 6.551e+04 -> 6.691e+04.
- Divergenza: **Nessuna** (0)
- Fase Wyckoff candidata: **Possibile accumulazione** (1)
  - Dettaglio Wyckoff: Prezzo sotto MA200, vicino alla parte bassa del range a 120 giorni, RSI 48.7.
- Fibonacci automatico: **NON ATTIVO** (0)
  - Swing DOWN 2026-05-06 82.792 -> 2026-08-03 62.227; livello più vicino 23.6% a 67.080; stato NON ATTIVO; confluenza: resistenza tecnica, neckline rialzista.
- Punteggio pattern: **0**
  - rialzista dominante: Doppio minimo (CANDIDATO, 0); ribassista dominante: Doppio massimo (CANDIDATO, 0).
- Supporto più vicino: **62.227**
- Resistenza più vicina: **66.910**

Pattern classici e ciclo di vita:

- Doppio minimo: **CANDIDATO** (0)
  - Due minimi simili vicino a 62.201 tra 2026-06-18 e 2026-08-03. Neckline stimata: 66.910. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 8 giorni.
  - neckline 66.910; target 71.619; distanza dalla neckline 4,59%; prezzo sotto neckline.
- Triplo minimo: **CANDIDATO** (0)
  - Tre minimi simili vicino a 62.201 dal 2026-03-29 al 2026-08-03. Neckline stimata: 82.792. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 8 giorni.
  - neckline 82.792; target 103.383; distanza dalla neckline 29,41%; prezzo sotto neckline.
- Adam and Eve Bottom: **CANDIDATO** (0)
  - Pattern Adam and Eve Bottom vicino a 59.109 dal 2026-06-05 al 2026-08-03. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 67.248. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 8 giorni.
  - neckline 67.248; target 75.387; distanza dalla neckline 5,11%; prezzo sotto neckline.
- Doppio massimo: **CANDIDATO** (0)
  - Due massimi simili vicino a 67.248 tra 2026-06-15 e 2026-07-21. Neckline ribassista stimata: 57.748. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 21 giorni.
  - neckline 57.748; target 48.247; distanza dalla neckline 10,79%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 66.910 dal 2026-06-22 al 2026-07-21. Neckline ribassista stimata: 57.748. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 21 giorni.
  - neckline 57.748; target 48.585; distanza dalla neckline 10,79%; prezzo sopra neckline.
- Adam and Eve Top: **CANDIDATO** (0)
  - Pattern Adam and Eve Top vicino a 67.248 dal 2026-06-15 al 2026-07-21. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 57.748. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 21 giorni.
  - neckline 57.748; target 48.247; distanza dalla neckline 10,79%; prezzo sopra neckline.

### SOL

- Prezzo: **75,98 $**
- Punteggio tecnico: **0 / 12**
- Verdetto: **NEUTRALE / MISTO**
- Trend: **Trend misto** (1)
- Momentum: **Momentum in miglioramento** (3)
- Volume: **Volume da accumulazione** (1)
- Struttura: **Struttura ribassista con massimi e minimi decrescenti** (-2)
  - Dettaglio struttura: Ultimi minimi: 73.4 -> 70.69. Ultimi massimi: 78.88 -> 78.73.
- Divergenza: **Divergenza ribassista nascosta RSI** (-1)
- Fase Wyckoff candidata: **Markdown / fase ribassista** (-2)
  - Dettaglio Wyckoff: Prezzo sotto MA200 con trend a 90 giorni ancora debole.
- Fibonacci automatico: **REJECTION** (0)
  - Swing DOWN 2026-05-11 98,27 -> 2026-08-01 70,69; livello più vicino 23.6% a 77,20; stato REJECTION; confluenza: nessuna confluenza indipendente.
- Punteggio pattern: **0**
  - rialzista dominante: Doppio minimo (CANDIDATO, 0); ribassista dominante: Doppio massimo (CANDIDATO, 0).
- Supporto più vicino: **70,69**
- Resistenza più vicina: **78,73**

Pattern classici e ciclo di vita:

- Doppio minimo: **CANDIDATO** (0)
  - Due minimi simili vicino a 67,92 tra 2026-06-19 e 2026-08-01. Neckline stimata: 83,81. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 10 giorni.
  - neckline 83,81; target 99,70; distanza dalla neckline 10,30%; prezzo sotto neckline.
- Triplo minimo: **CANDIDATO** (0)
  - Tre minimi simili vicino a 67,92 dal 2026-06-19 al 2026-08-01. Neckline stimata: 83,81. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 10 giorni.
  - neckline 83,81; target 99,70; distanza dalla neckline 10,30%; prezzo sotto neckline.
- Adam and Eve Bottom: **CANDIDATO** (0)
  - Pattern Adam and Eve Bottom vicino a 67,92 dal 2026-06-19 al 2026-08-01. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 83,81. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 10 giorni.
  - neckline 83,81; target 99,70; distanza dalla neckline 10,30%; prezzo sotto neckline.
- Doppio massimo: **CANDIDATO** (0)
  - Due massimi simili vicino a 78,73 tra 2026-06-15 e 2026-07-21. Neckline ribassista stimata: 64,42. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 21 giorni.
  - neckline 64,42; target 50,11; distanza dalla neckline 17,95%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 78,88 dal 2026-06-15 al 2026-07-21. Neckline ribassista stimata: 64,42. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 21 giorni.
  - neckline 64,42; target 49,96; distanza dalla neckline 17,95%; prezzo sopra neckline.
- Adam and Eve Top: **CANDIDATO** (0)
  - Pattern Adam and Eve Top vicino a 78,73 dal 2026-06-15 al 2026-07-21. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 64,42. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 21 giorni.
  - neckline 64,42; target 50,11; distanza dalla neckline 17,95%; prezzo sopra neckline.

### DOGE

- Prezzo: **0.07000 $**
- Punteggio tecnico: **0 / 12**
- Verdetto: **NEUTRALE / MISTO**
- Trend: **Trend ribassista** (-3)
- Momentum: **Momentum in miglioramento** (3)
- Volume: **Volume da distribuzione** (-1)
- Struttura: **Compressione / triangolo** (0)
  - Dettaglio struttura: Ultimi minimi: 0.06797 -> 0.06835. Ultimi massimi: 0.0738 -> 0.07117.
- Divergenza: **Nessuna** (0)
- Fase Wyckoff candidata: **Possibile accumulazione** (1)
  - Dettaglio Wyckoff: Prezzo sotto MA200, vicino alla parte bassa del range a 120 giorni, RSI 44.7.
- Fibonacci automatico: **NON ATTIVO** (0)
  - Swing DOWN 2026-05-14 0.11825 -> 2026-08-06 0.06835; livello più vicino 23.6% a 0.08013; stato NON ATTIVO; confluenza: nessuna confluenza indipendente.
- Punteggio pattern: **0**
  - rialzista dominante: Doppio minimo (CANDIDATO, 0); ribassista dominante: Adam and Eve Top (CANDIDATO, 0).
- Supporto più vicino: **0.06835**
- Resistenza più vicina: **0.07117**

Pattern classici e ciclo di vita:

- Doppio minimo: **CANDIDATO** (0)
  - Due minimi simili vicino a 0.06829 tra 2026-07-24 e 2026-08-06. Neckline stimata: 0.07380. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 5 giorni.
  - neckline 0.07380; target 0.07931; distanza dalla neckline 5,43%; prezzo sotto neckline.
- Triplo minimo: **CANDIDATO** (0)
  - Tre minimi simili vicino a 0.06829 dal 2026-06-30 al 2026-08-06. Neckline stimata: 0.07923. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 5 giorni.
  - neckline 0.07923; target 0.09017; distanza dalla neckline 13,19%; prezzo sotto neckline.
- Adam and Eve Bottom: **CANDIDATO** (0)
  - Pattern Adam and Eve Bottom vicino a 0.06835 dal 2026-06-30 al 2026-08-06. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 0.07923. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 5 giorni.
  - neckline 0.07923; target 0.09012; distanza dalla neckline 13,19%; prezzo sotto neckline.
- Doppio massimo: **ASSENTE** (0)
- Triplo massimo: **ASSENTE** (0)
- Adam and Eve Top: **CANDIDATO** (0)
  - Pattern Adam and Eve Top vicino a 0.07923 dal 2026-07-04 al 2026-07-26. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 0.06829. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 16 giorni.
  - neckline 0.06829; target 0.05735; distanza dalla neckline 2,50%; prezzo sopra neckline.

## Fibonacci automatico

Il modulo seleziona uno swing recente tramite pivot confermati. Un semplice tocco vale 0: Fibonacci pesa al massimo ±1 soltanto quando il livello è tenuto, perso, recuperato o respinto e coincide con almeno un livello tecnico indipendente.

| Asset   | Swing                         | 23,6%   | 38,2%   | 50,0%   | 61,8%   | 78,6%   | Livello vicino   | Stato      | Confluenza                             |   Score |
|:--------|:------------------------------|:--------|:--------|:--------|:--------|:--------|:-----------------|:-----------|:---------------------------------------|--------:|
| BTC | DOWN 2026-05-06 -> 2026-08-03 | 67.080 | 70.083 | 72.509 | 74.936 | 78.391 | 23.6% / 67.080 | NON ATTIVO | resistenza tecnica, neckline rialzista | 0 |
| SOL | DOWN 2026-05-11 -> 2026-08-01 | 77,20 | 81,23 | 84,48 | 87,73 | 92,37 | 23.6% / 77,20 | REJECTION | nessuna confluenza indipendente | 0 |
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

- **BTC**: 10/30 previsioni controllate su 40 fatte. Stato: **RACCOLTA DATI**.
- **SOL**: 10/30 previsioni controllate su 40 fatte. Stato: **RACCOLTA DATI**.
- **DOGE**: 10/30 previsioni controllate su 40 fatte. Stato: **RACCOLTA DATI**.

| Asset | Previsioni fatte | Controllate | Progresso | In attesa | Stato | Prossimo controllo |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 40 | 10 | 10/30 [███░░░░░░░] | 30 | RACCOLTA DATI | 2026-08-12 / tra 1 giorno |
| SOL | 40 | 10 | 10/30 [███░░░░░░░] | 30 | RACCOLTA DATI | 2026-08-12 / tra 1 giorno |
| DOGE | 40 | 10 | 10/30 [███░░░░░░░] | 30 | RACCOLTA DATI | 2026-08-12 / tra 1 giorno |

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

Generato: 2026-08-11 05:23 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [data_quality_coherence_report.md](data_quality_coherence_report.md)

Questo controllo non modifica punteggi o decisioni. Verifica che tutti i moduli usino lo stesso prezzo corrente e che le nuove regole Technical/Classic Visual siano integre.

## Stato finale: **OK**

## Prezzo unico per modulo

| Modulo                  | Asset   | Campo             | Stato   | Prezzo snapshot   | Prezzo modulo   | Differenza   |
|:------------------------|:--------|:------------------|:--------|:------------------|:----------------|:-------------|
| Scanner                 | BTC     | current_price     | OK      | 63.976 $          | 63.976 $        | +0,0000%     |
| Scanner                 | DOGE    | current_price     | OK      | 0.07000 $         | 0.07000 $       | -0,0000%     |
| Scanner                 | SOL     | current_price     | OK      | 75,98 $           | 75,98 $         | +0,0000%     |
| Scanner Forecast        | BTC     | current_price     | OK      | 63.976 $          | 63.976 $        | +0,0000%     |
| Scanner Forecast        | SOL     | current_price     | OK      | 75,98 $           | 75,98 $         | +0,0000%     |
| Scanner Forecast        | DOGE    | current_price     | OK      | 0.07000 $         | 0.07000 $       | -0,0000%     |
| Technical Structure     | BTC     | price             | OK      | 63.976 $          | 63.976 $        | +0,0000%     |
| Technical Structure     | SOL     | price             | OK      | 75,98 $           | 75,98 $         | +0,0000%     |
| Technical Structure     | DOGE    | price             | OK      | 0.07000 $         | 0.07000 $       | -0,0000%     |
| Classic Technical       | BTC     | price             | OK      | 63.976 $          | 63.976 $        | +0,0000%     |
| Classic Technical       | SOL     | price             | OK      | 75,98 $           | 75,98 $         | +0,0000%     |
| Classic Technical       | DOGE    | price             | OK      | 0.07000 $         | 0.07000 $       | -0,0000%     |
| Classic Visual          | BTC     | price             | OK      | 63.976 $          | 63.976 $        | +0,0000%     |
| Classic Visual          | SOL     | price             | OK      | 75,98 $           | 75,98 $         | +0,0000%     |
| Classic Visual          | DOGE    | price             | OK      | 0.07000 $         | 0.07000 $       | -0,0000%     |
| Exchange Microstructure | BTC     | price             | OK      | 63.976 $          | 64.025 $        | +0,0760%     |
| Exchange Microstructure | SOL     | price             | OK      | 75,98 $           | 76,02 $         | +0,0513%     |
| Exchange Microstructure | DOGE    | price             | OK      | 0.07000 $         | 0.07002 $       | +0,0286%     |
| RSI top-cycle           | SOL     | current_price     | OK      | 75,98 $           | 75,98 $         | +0,0000%     |
| RSI top-cycle           | SOL     | current_price     | OK      | 75,98 $           | 75,98 $         | +0,0000%     |
| Frattale BTC/SOL        | SOL     | sol_current_price | OK      | 75,98 $           | 75,98 $         | +0,0000%     |
| Fractal path            | SOL     | current_price     | OK      | 75,98 $           | 75,98 $         | +0,0000%     |

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

<!-- SOL_SPOT_ADAPTIVE_START -->
# SOL Spot Adaptive Range — paper trading separato

Generato: 2026-08-12T16:17:39+00:00

- Modalità: **SOLO PAPER TRADING**
- Asset: **SOL spot**
- Leva: **nessuna (1x)**
- Capitale iniziale separato: **€40.000,00**
- Fonte mercato: **KUCOIN_PUBLIC_API**; nuove entrate: **CONSENTITE**

| Equity | Cash | SOL | Prezzo | Rendimento | Realizzato | Commissioni | Max DD | Operazioni |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €41.103,33 | €17.544,74 | 311.135932 | 75.7180 | +2.76% | €568,83 | €49,51 | 6.48% | 8 |

**Ultima decisione:** HOLD — Prezzo dentro la fascia neutrale.

Bande 4H: L2 71.1903 · L1 73.3177 · media 75.9769 · U1 78.6361 · U2 80.7634.

> Questo portafoglio non condivide capitale, posizioni o statistiche con il paper trading da €10.000.
<!-- SOL_SPOT_ADAPTIVE_END -->
