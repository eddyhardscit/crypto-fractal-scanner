<!-- COMPACT_REPORT_HEADER_START -->
> **Vista compatta:** Decisione operativa, Global Confluence e cambiamenti giornalieri restano aperti. Tocca il titolo di una sezione per mostrare o nascondere i dettagli.  
> Tutte le tabelle e tutti i dati restano nel file: copiando il Markdown raw viene copiato tutto.
<!-- COMPACT_REPORT_HEADER_END -->

<!-- COMPACT_SECTION_START:decision -->
<details open>
<summary><strong>🧭 Decisione operativa — da leggere per prima</strong></summary>

<!-- DECISION_REPORT_START -->

# Decisione operativa sintetica

Generato: 2026-07-28 05:15 UTC

Report separato completo: [decision_report.md](decision_report.md)

Sintesi automatica dello scanner: l'azione spot viene copiata direttamente dal Global Confluence; long, short e rischio restano filtri separati e più prudenti.

| Asset | Global | Direzione | Spot | Long leva | Short leva | Max long | Max short | Rischio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | -1 | LEGGERMENTE BEARISH | NON INSEGUIRE / RIDUCI RISCHIO | NO LONG A LEVA / ATTENDI SOPRA 67.248 $ | NO SHORT | nessuna | nessuna | ALTO |
| SOL | +1 | NEUTRALE / INCERTO | HOLD LEGGERO / ATTESA CONFERME | NO LONG A LEVA | NO SHORT | nessuna | nessuna | MOLTO ALTO |
| DOGE | +1 | NEUTRALE / INCERTO | STAI ALLA FINESTRA | NO LONG A LEVA | NO SHORT | nessuna | nessuna | MOLTO ALTO |

## Lettura immediata

- **BTC**: Global = **-1**, spot = **NON INSEGUIRE / RIDUCI RISCHIO**, long = **NO LONG A LEVA / ATTENDI SOPRA 67.248 $**, short = **NO SHORT**, rischio = **ALTO**.
- **SOL**: Global = **+1**, spot = **HOLD LEGGERO / ATTESA CONFERME**, long = **NO LONG A LEVA**, short = **NO SHORT**, rischio = **MOLTO ALTO**.
- **DOGE**: Global = **+1**, spot = **STAI ALLA FINESTRA**, long = **NO LONG A LEVA**, short = **NO SHORT**, rischio = **MOLTO ALTO**.

## Dettaglio logica

### BTC

- Global Confluence: **-1**
- Confluenza: **DEBOLE / FRAGILE**
- Bias Global: **Fragile**
- Direzione decisionale: **LEGGERMENTE BEARISH**
- Azione spot dal Global: **NON INSEGUIRE / RIDUCI RISCHIO**
- Long leva: **NO LONG A LEVA / ATTENDI SOPRA 67.248 $**
- Short leva: **NO SHORT**
- Rischio: **ALTO**
- Conferme: Prima resistenza sopra 66.910; conferma del doppio minimo sopra 67.248.
- Invalidazioni: Sotto 57.748 il quadro tecnico peggiora.

### SOL

- Global Confluence: **+1**
- Confluenza: **MISTA / PARZIALE**
- Bias Global: **Neutrale / misto**
- Direzione decisionale: **NEUTRALE / INCERTO**
- Azione spot dal Global: **HOLD LEGGERO / ATTESA CONFERME**
- Long leva: **NO LONG A LEVA**
- Short leva: **NO SHORT**
- Rischio: **MOLTO ALTO**
- Conferme: conferma del doppio minimo sopra 75,94; nuova conferma tecnica sopra 78,73; milestone analogiche 89,78 / 96,42, valide soltanto se rientra anche il gap frattale.
- Invalidazioni: Allarmi sotto 69,65 / 64,42 / 62,19.

### DOGE

- Global Confluence: **+1**
- Confluenza: **MISTA / PARZIALE**
- Bias Global: **Neutrale / misto**
- Direzione decisionale: **NEUTRALE / INCERTO**
- Azione spot dal Global: **STAI ALLA FINESTRA**
- Long leva: **NO LONG A LEVA**
- Short leva: **NO SHORT**
- Rischio: **MOLTO ALTO**
- Conferme: Sopra 0.07923 migliora; sopra 0.07966 viene invalidato il pattern ribassista dominante.
- Invalidazioni: Sotto 0.06961 il rischio ribassista aumenta.

## Nota semplice

- **Spot** = usa la stessa azione del Global Confluence, senza una seconda mappatura che possa produrre frasi diverse.
- **Zona alta storica** = zona dove non inseguire troppo; può essere zona da prendere profitto.
- **Zona bassa storica** = zona di rischio; con leva la liquidazione non dovrebbe stare lì vicino.
- **BTC leva** = nessun long a leva finché il prezzo snapshot non supera **67.248 $**; sotto quella soglia resta solo l'azione spot indicata dal Global.
- **Lifecycle EMA200** = per SOL resta solo contesto, peso Global 0; score interno 4; EMA200 circa 112,37 $; upside verso EMA200 +53,41%. Non autorizza leva e non aggiunge punti automatici.
- **NO LONG** non significa automaticamente **SHORT**. Lo short ha senso solo se il quadro è bearish o se lo spike viene spesso scaricato.
- Per SOL, se il Global è da **+3 in su**, la decisione non deve diventare bearish solo perché lo scanner grezzo a 30 giorni è incerto.

<!-- DECISION_REPORT_END -->

<!-- PAPER_TRADING_START -->
# Paper trading automatico KuCoin

Generato: 2026-07-28T05:15:11+00:00


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [paper_trading_report.md](paper_trading_report.md)

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-07-28T05:08:25+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-07-28T05:08:25+00:00 | 2026-07-28T05:08:25+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-07-28T04:45:00+00:00 | 2026-07-28T04:45:00+00:00 | 8,5 min | 25,0 min | OK |
| 60m | 12 | 2026-07-28T04:00:00+00:00 | 2026-07-28T04:00:00+00:00 | 8,5 min | 45,0 min | OK |
| 240m | 12 | 2026-07-28T00:00:00+00:00 | 2026-07-28T00:00:00+00:00 | 1,14 h | 1,00 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Combo Adaptive Mfe Trail | AKE | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | AKE | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 Cap75 V1 | BEAT | 60m | SHORT | -4,75 | 4,50 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Principale 4H | SUI | 240m | SHORT | -7,49 | 6,00 | 0,00 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | DOGE | 240m | SHORT | -7,39 | 6,00 | 0,00 | STALE_CANDLE | 1,14 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | SOL | 240m | SHORT | -6,72 | 6,00 | 0,00 | STALE_CANDLE | 1,14 h | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | HYPE | 240m | SHORT | -6,69 | 6,00 | 0,00 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | BTC | 240m | SHORT | -6,50 | 6,00 | 0,00 | STALE_CANDLE | 1,14 h | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | AKE | 240m | LONG | 6,25 | 6,00 | 0,00 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | XRP | 240m | SHORT | -5,90 | 6,00 | 0,10 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | ZEC | 240m | SHORT | -5,72 | 6,00 | 0,28 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | BANK | 240m | LONG | 2,75 | 6,00 | 3,25 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | BEAT | 240m | SHORT | -1,43 | 6,00 | 4,57 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | ETH | 240m | SHORT | -0,82 | 6,00 | 5,18 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | PEPE | 240m | SHORT | -0,03 | 6,00 | 5,97 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Bilanciata 1H V1 | AKE | 60m | LONG | 7,75 | 5,00 | 0,00 | READY | 8,5 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Fast No Pepe V1 | AKE | 60m | LONG | 7,75 | 4,50 | 0,00 | READY | 8,5 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Fast Tp2 V1 | AKE | 60m | LONG | 7,75 | 4,50 | 0,00 | READY | 8,5 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Rapida 1H V3 Filtered | AKE | 60m | LONG | 7,75 | 4,50 | 0,00 | READY | 8,5 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Fast V3 No Esports V1 | AKE | 60m | LONG | 7,75 | 4,50 | 0,00 | READY | 8,5 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Forza relativa 1H V1 | AKE | 60m | LONG | 7,75 | 4,00 | 0,00 | READY | 8,5 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Scanner Top5 Btc Mfe V1 | AKE | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top5 Btc Guard Mfe V1 | AKE | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.607,10 | -3,93% | €-392,90 | €3.000,00 | -13,10% | 6 | 25 | 28,00% | 0,58 | 6,36% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 25 | 867 | CAMPIONE INSUFFICIENTE | 30 (mancano 5) |

- Trade del Principale 4H chiusi: **25**; win rate **28,00%**; profit factor **0,58**.
- Expectancy: **€-17,67** per trade; P&L netto: **€-441,81**; max drawdown: **6,36%**.
- Valutazione: **Servono altri eventi indipendenti prima di trarre conclusioni.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 6 | €9.607,10 | €956,55 | €2.869,65 | €97,18 | €49,86 |
| TEST | Bilanciata 1H V3 Filtered | 6 | €10.564,66 | €1.610,58 | €4.831,74 | €157,52 | €-20,88 |
| TEST | 1H Fast Score 6 75 V1 | 6 | €10.555,92 | €3.844,61 | €11.533,83 | €53,79 | €96,95 |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | 6 | €10.515,98 | €3.841,03 | €11.523,10 | €53,42 | €96,50 |
| TEST | Benchmark Donchian breakout 1H | 7 | €10.505,24 | €4.754,01 | €9.508,03 | €101,35 | €191,20 |
| TEST | Scanner Top 5 Long 1H | 2 | €10.497,24 | €289,14 | €578,29 | €55,00 | €12,81 |
| TEST | 1H Fast V3 Cap75 V1 | 6 | €10.438,71 | €3.029,24 | €9.087,73 | €102,58 | €63,09 |
| TEST | 1H Fast Nohigh Cap75 V1 | 1 | €10.415,57 | €225,73 | €677,19 | €51,70 | €0,00 |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | 1 | €10.395,73 | €172,19 | €516,57 | €51,51 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 6 | €10.389,49 | €3.471,87 | €10.415,61 | €154,43 | €10,01 |
| TEST | Scanner Top 5 + forza BTC 1H | 3 | €10.364,59 | €469,39 | €938,78 | €105,09 | €12,65 |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | 7 | €10.328,24 | €3.399,82 | €10.199,45 | €156,26 | €-6,63 |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | 5 | €10.327,26 | €2.397,44 | €7.192,33 | €51,15 | €58,07 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 6 | €10.323,87 | €2.975,89 | €8.927,68 | €52,77 | €62,76 |
| TEST | Combo Adaptive Side Regime Guard V1 | 6 | €10.299,20 | €4.213,47 | €8.426,95 | €153,60 | €-7,39 |
| TEST | Bilanciata 1H V1 | 7 | €10.297,10 | €3.167,53 | €9.502,58 | €104,00 | €40,30 |
| TEST | 1H Fast V3 Nohigh Range Only V1 | 2 | €10.296,85 | €313,60 | €940,79 | €102,49 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 0 | €10.271,73 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast No Pepe V1 | 8 | €10.266,65 | €4.918,20 | €14.754,61 | €153,30 | €15,00 |
| TEST | Main Dynamic Asset Selector V1 | 1 | €10.264,58 | €142,13 | €426,38 | €0,00 | €31,69 |
| TEST | Donchian 1H Gb20 120R V1 | 5 | €10.237,04 | €3.980,81 | €7.961,62 | €56,76 | €193,93 |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 2 | €10.235,71 | €336,78 | €1.010,33 | €50,80 | €0,00 |
| TEST | 1H Fast Score 6 75 Range Only V1 | 1 | €10.218,59 | €143,01 | €429,04 | €51,48 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 6 | €10.200,35 | €5.014,59 | €15.043,76 | €52,28 | €114,51 |
| TEST | Combo Adaptive | 6 | €10.195,96 | €1.603,92 | €3.207,84 | €203,73 | €12,52 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 0 | €10.185,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V3 Filtered | 7 | €10.185,10 | €4.877,60 | €14.632,81 | €152,97 | €14,29 |
| TEST | Bilanciata 1H V2 | 3 | €10.181,14 | €1.358,78 | €4.076,33 | €101,14 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 7 | €10.177,60 | €3.768,54 | €11.305,62 | €102,66 | €46,28 |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 1 | €10.175,99 | €141,59 | €424,78 | €50,97 | €-18,52 |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | 2 | €10.159,32 | €1.034,94 | €3.104,81 | €98,69 | €0,00 |
| TEST | Btc Bollinger 1H | 1 | €10.144,18 | €1.412,24 | €4.236,72 | €50,84 | €-21,40 |
| TEST | Combo Adaptive Runner25 V1 | 7 | €10.134,76 | €2.324,06 | €4.648,11 | €201,56 | €13,42 |
| TEST | Main Side Regime Guard V1 | 4 | €10.127,11 | €1.253,51 | €3.760,52 | €101,62 | €57,26 |
| TEST | Sol Donchian 1H | 1 | €10.123,46 | €1.254,69 | €3.764,07 | €0,00 | €33,59 |
| TEST | Combo Trend Side Regime Guard V1 | 7 | €10.112,64 | €3.527,57 | €7.055,14 | €202,63 | €3,85 |
| TEST | Doge Ema 1H | 1 | €10.102,84 | €1.101,76 | €3.305,29 | €50,46 | €12,96 |
| TEST | 1H Fast V3 No Esports Long Only V1 | 1 | €10.090,48 | €141,78 | €425,35 | €51,04 | €-18,54 |
| TEST | Sol Bollinger 4H | 0 | €10.086,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 4H | 0 | €10.084,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Donchian 1H | 1 | €10.074,08 | €1.220,11 | €3.660,32 | €50,47 | €-17,53 |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | 0 | €10.071,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V1 | 1 | €10.048,63 | €1.486,90 | €4.460,70 | €49,96 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 7 | €10.045,64 | €4.960,33 | €14.880,99 | €101,09 | €65,52 |
| TEST | Ampia 4H | 6 | €10.036,04 | €1.767,28 | €3.534,57 | €201,08 | €60,97 |
| TEST | Combo Adaptive Quality7 V1 | 3 | €10.034,70 | €1.337,04 | €2.674,08 | €150,30 | €-18,26 |
| TEST | 1H Fast Tp2 V1 | 7 | €10.034,69 | €4.199,61 | €12.598,83 | €149,89 | €14,63 |
| TEST | Btc Adaptive 1H | 1 | €10.020,48 | €1.158,94 | €3.476,83 | €50,07 | €9,29 |
| TEST | 1H Balanced V3 Long Only V1 | 6 | €10.018,01 | €2.386,15 | €7.158,46 | €148,70 | €-19,82 |
| TEST | Forza relativa 1H V2 | 4 | €10.015,98 | €2.768,37 | €5.536,73 | €155,16 | €-21,63 |
| TEST | Scanner Top5 Btc Tp3 V1 | 3 | €10.013,11 | €502,10 | €1.004,20 | €103,17 | €-18,22 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €10.010,36 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Long Only V1 | 5 | €10.008,47 | €2.704,17 | €5.408,34 | €199,93 | €12,19 |
| TEST | Scanner Top5 Btc Runner25 V1 | 3 | €10.007,22 | €487,53 | €975,06 | €102,62 | €-18,21 |
| TEST | Sol Donchian 4H | 1 | €10.005,46 | €830,21 | €1.660,43 | €0,00 | €57,99 |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 1 | €10.003,88 | €141,08 | €423,23 | €50,79 | €0,00 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 0 | €10.002,07 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 4H | 1 | €10.000,84 | €761,04 | €1.522,08 | €0,00 | €53,15 |
| TEST | Scalp RSI Short 85 · €50 · 15x | 0 | €10.000,61 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €10 · 15x | 0 | €10.000,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Continuation V1 | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €10 · 15x | 0 | €9.999,70 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €10 · 15x | 0 | €9.998,96 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · prudente · 5x | 0 | €9.998,64 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €50 · 15x | 0 | €9.998,52 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €10 · 15x | 0 | €9.998,50 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | 0 | €9.996,45 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 1H | 1 | €9.996,42 | €1.299,56 | €3.898,68 | €49,90 | €18,14 |
| TEST | 1H Balanced Short Trend Down Strict V1 | 0 | €9.995,87 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €50 · 15x | 0 | €9.994,81 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €50 · 15x | 0 | €9.992,50 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €10 · 15x | 0 | €9.991,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 0 | €9.990,65 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · prudente · 5x | 0 | €9.990,24 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · prudente · 5x | 0 | €9.988,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · prudente · 5x | 0 | €9.983,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V2 | 1 | €9.979,60 | €1.494,54 | €4.483,63 | €50,22 | €0,00 |
| TEST | 1H Fast V3 No Esports V1 | 7 | €9.977,73 | €4.778,27 | €14.334,80 | €149,83 | €14,01 |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | 1 | €9.969,22 | €207,87 | €415,74 | €49,89 | €0,00 |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | 5 | €9.966,45 | €2.739,02 | €5.478,05 | €198,53 | €-36,07 |
| TEST | Eth Bollinger 1H | 0 | €9.959,49 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 0 | €9.955,61 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €50 · 15x | 0 | €9.955,59 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 1H | 1 | €9.953,65 | €1.091,78 | €3.275,34 | €49,89 | €-21,48 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.951,70 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 4H | 0 | €9.950,68 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 4H | 0 | €9.949,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Profit Lock V1 | 7 | €9.948,75 | €2.599,68 | €5.199,37 | €100,20 | €31,39 |
| TEST | Btc Donchian 4H | 1 | €9.944,25 | €1.196,13 | €2.392,26 | €49,75 | €-4,99 |
| TEST | Scanner Top5 Btc Btc Le3 V1 | 3 | €9.938,65 | €452,98 | €905,96 | €101,06 | €-18,09 |
| TEST | Combo Adaptive Tp3 V1 | 4 | €9.929,58 | €2.226,41 | €4.452,81 | €198,61 | €0,00 |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | 0 | €9.923,70 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 1H | 1 | €9.922,91 | €1.300,18 | €3.900,53 | €49,51 | €24,01 |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | 0 | €9.922,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 1H | 1 | €9.918,99 | €1.147,21 | €3.441,62 | €49,56 | €9,20 |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | 2 | €9.915,06 | €412,83 | €825,66 | €99,08 | €-18,05 |
| TEST | Combo Scanner | 3 | €9.914,45 | €438,70 | €877,39 | €100,43 | €-18,07 |
| TEST | Combo Adaptive Regime V1 | 1 | €9.903,77 | €206,52 | €413,04 | €49,56 | €0,00 |
| TEST | Eth Ema 4H | 0 | €9.894,27 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 4H | 1 | €9.892,80 | €780,22 | €1.560,44 | €49,48 | €-2,57 |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 7 | €9.892,65 | €2.817,91 | €8.453,74 | €98,64 | €14,94 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 1 | €9.886,03 | €137,56 | €412,68 | €49,52 | €-17,99 |
| TEST | 1H Fast V3 Nohigh V1 | 2 | €9.874,22 | €2.309,61 | €6.928,83 | €100,01 | €0,00 |
| TEST | Eth Donchian 1H | 0 | €9.871,99 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Mean Reversion | 1 | €9.863,73 | €1.988,26 | €3.976,53 | €47,72 | €-20,08 |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | 0 | €9.857,49 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Bollinger 1H | 1 | €9.848,43 | €1.267,95 | €3.803,86 | €49,17 | €16,68 |
| TEST | Benchmark trend following EMA 1H | 7 | €9.842,81 | €2.117,13 | €4.234,26 | €150,04 | €98,96 |
| TEST | Global Confluence puro 1H | 1 | €9.833,51 | €1.428,07 | €2.856,13 | €49,20 | €-4,24 |
| TEST | Scanner Bottom10 Short | 7 | €9.820,87 | €3.359,18 | €6.718,36 | €100,19 | €30,67 |
| TEST | Scanner Bottom15 Short | 7 | €9.820,87 | €3.359,18 | €6.718,36 | €100,19 | €30,67 |
| TEST | Scanner Bottom20 Short | 7 | €9.820,87 | €3.359,18 | €6.718,36 | €100,19 | €30,67 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 1 | €9.813,54 | €194,51 | €583,53 | €49,25 | €0,00 |
| TEST | Sol Adaptive 1H | 1 | €9.812,08 | €1.076,25 | €3.228,75 | €49,18 | €-21,17 |
| TEST | Master Adaptive Gb20 Be V1 | 1 | €9.806,54 | €1.403,77 | €2.807,55 | €50,57 | €0,00 |
| TEST | Eth Adaptive 1H | 0 | €9.799,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Quality7 Regime V1 | 0 | €9.797,24 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Gb20 Partial V1 | 1 | €9.796,05 | €1.376,47 | €2.752,95 | €50,21 | €0,00 |
| TEST | 1H Balanced Long No Rhv V1 | 2 | €9.792,95 | €1.052,18 | €3.156,55 | €99,37 | €12,05 |
| TEST | Scanner Bottom 5 Short 1H | 7 | €9.775,26 | €2.995,81 | €5.991,63 | €50,19 | €30,92 |
| TEST | Master Adaptive Gb20 Loss Cap V1 | 2 | €9.770,94 | €2.043,62 | €4.087,25 | €100,09 | €36,90 |
| TEST | Scanner Top5 Btc Guard V1 | 2 | €9.761,07 | €405,59 | €811,17 | €97,34 | €11,91 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 0 | €9.757,70 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Benchmark Bollinger mean reversion 1H | 4 | €9.754,29 | €6.802,28 | €13.604,57 | €169,04 | €-26,15 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 1 | €9.739,73 | €135,52 | €406,57 | €48,79 | €-17,73 |
| TEST | Master Adaptive Expanded V1 | 3 | €9.738,67 | €440,31 | €880,62 | €98,85 | €36,05 |
| TEST | Scanner Top5 Btc Mfe V1 | 2 | €9.737,45 | €1.566,58 | €3.133,17 | €97,82 | €-0,08 |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | 1 | €9.730,44 | €202,72 | €405,45 | €48,65 | €-0,08 |
| TEST | Combo Adaptive Partial 1R V1 | 7 | €9.729,81 | €2.381,10 | €4.762,20 | €194,74 | €3,16 |
| TEST | Eth Ema 1H | 0 | €9.727,87 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Runner25 V1 | 3 | €9.726,39 | €427,39 | €854,79 | €98,33 | €36,01 |
| TEST | Scanner Top10 Long | 3 | €9.705,45 | €1.598,07 | €3.196,14 | €101,35 | €-17,66 |
| TEST | Scanner Top15 Long | 3 | €9.705,45 | €1.598,07 | €3.196,14 | €101,35 | €-17,66 |
| TEST | Scanner Top20 Long | 3 | €9.705,45 | €1.598,07 | €3.196,14 | €101,35 | €-17,66 |
| TEST | Master Adaptive No Alt V1 | 3 | €9.698,71 | €427,48 | €854,96 | €98,21 | €35,90 |
| TEST | Master Adaptive V1 | 3 | €9.694,71 | €427,40 | €854,79 | €98,19 | €35,89 |
| TEST | Combo Trend | 7 | €9.682,06 | €3.374,06 | €6.748,11 | €146,39 | €90,23 |
| TEST | Master Adaptive Gb20 V1 | 2 | €9.628,98 | €1.549,90 | €3.099,79 | €97,01 | €0,00 |
| TEST | 1H Fast V3 Long Only V1 | 1 | €9.607,23 | €135,03 | €405,10 | €48,61 | €-17,66 |
| TEST | Forza relativa 1H V1 | 7 | €9.556,70 | €3.372,93 | €6.745,86 | €106,19 | €57,39 |
| TEST | Scanner Top5 Btc Guard Mfe V1 | 1 | €9.552,70 | €199,02 | €398,04 | €47,77 | €-0,08 |
| TEST | Combo Adaptive Mfe Trail | 5 | €9.551,78 | €2.468,48 | €4.936,95 | €143,18 | €15,99 |
| TEST | Master Adaptive Strict3 V1 | 2 | €9.410,39 | €2.217,67 | €4.435,35 | €97,56 | €0,00 |

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
| PRINCIPALE | Principale 4H | Confluenza trend | €9.607,10 | €-441,81 | 25 | 25 | 28,00% | 0,58 | €-17,67 | 6,36% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €10.564,66 | €588,53 | 54 | 54 | 42,59% | 1,52 | €10,90 | 2,20% |
| TEST | 1H Fast Score 6 75 V1 | Momentum / breakout | €10.555,92 | €465,66 | 59 | 59 | 44,07% | 1,45 | €7,89 | 2,49% |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | Momentum / breakout | €10.515,98 | €426,16 | 22 | 22 | 54,55% | 2,38 | €19,37 | 1,96% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €10.505,24 | €319,85 | 32 | 32 | 53,12% | 1,37 | €10,00 | 3,09% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.497,24 | €484,78 | 46 | 46 | 47,83% | 1,47 | €10,54 | 3,91% |
| TEST | 1H Fast V3 Cap75 V1 | Momentum / breakout V3 Filtered | €10.438,71 | €380,90 | 53 | 53 | 47,17% | 1,40 | €7,19 | 2,49% |
| TEST | 1H Fast Nohigh Cap75 V1 | Momentum / breakout | €10.415,57 | €415,97 | 60 | 60 | 46,67% | 1,35 | €6,93 | 2,83% |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | Momentum / breakout V3 Filtered | €10.395,73 | €396,49 | 18 | 18 | 66,67% | 3,42 | €22,03 | 1,39% |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | Momentum / breakout V3 Filtered | €10.389,49 | €385,73 | 38 | 38 | 63,16% | 1,81 | €10,15 | 2,51% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €10.364,59 | €352,90 | 36 | 36 | 44,44% | 1,46 | €9,80 | 3,23% |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | Momentum / breakout V3 Filtered | €10.328,24 | €341,43 | 41 | 41 | 60,98% | 1,69 | €8,33 | 2,05% |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | Momentum / breakout | €10.327,26 | €273,27 | 18 | 18 | 66,67% | 1,79 | €15,18 | 2,01% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | Momentum / breakout V3 Filtered | €10.323,87 | €266,30 | 20 | 20 | 50,00% | 2,64 | €13,32 | 2,01% |
| TEST | Combo Adaptive Side Regime Guard V1 | Combo Adaptive | €10.299,20 | €311,88 | 19 | 19 | 68,42% | 2,34 | €16,41 | 1,41% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €10.297,10 | €265,54 | 58 | 58 | 50,00% | 1,24 | €4,58 | 3,56% |
| TEST | 1H Fast V3 Nohigh Range Only V1 | Momentum / breakout V3 Filtered | €10.296,85 | €297,96 | 10 | 10 | 70,00% | 2,84 | €29,80 | 1,78% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | Momentum / breakout V3 Filtered | €10.271,73 | €271,73 | 22 | 22 | 50,00% | 1,74 | €12,35 | 1,72% |
| TEST | 1H Fast No Pepe V1 | Momentum / breakout | €10.266,65 | €260,35 | 54 | 54 | 46,30% | 1,26 | €4,82 | 2,15% |
| TEST | Main Dynamic Asset Selector V1 | Confluenza trend | €10.264,58 | €233,14 | 8 | 8 | 50,00% | 2,39 | €29,14 | 1,50% |
| TEST | Donchian 1H Gb20 120R V1 | Donchian breakout 20 barre | €10.237,04 | €47,40 | 1 | 1 | 100,00% | ∞ | €47,40 | 1,09% |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | Momentum / breakout V3 Filtered | €10.235,71 | €236,97 | 14 | 14 | 57,14% | 4,59 | €16,93 | 1,01% |
| TEST | 1H Fast Score 6 75 Range Only V1 | Momentum / breakout | €10.218,59 | €218,95 | 12 | 12 | 58,33% | 1,75 | €18,25 | 2,28% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | Momentum / breakout V3 Filtered | €10.200,35 | €94,65 | 6 | 6 | 33,33% | 2,13 | €15,77 | 1,14% |
| TEST | Combo Adaptive | Combo Adaptive | €10.195,96 | €186,48 | 28 | 28 | 46,43% | 1,44 | €6,66 | 1,77% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | Momentum / breakout V3 Filtered | €10.185,37 | €185,37 | 22 | 22 | 40,91% | 1,57 | €8,43 | 2,27% |
| TEST | Rapida 1H V3 Filtered | Momentum / breakout V3 Filtered | €10.185,10 | €179,43 | 87 | 87 | 39,08% | 1,11 | €2,06 | 2,89% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €10.181,14 | €183,58 | 38 | 36 | 52,63% | 1,24 | €4,83 | 2,75% |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | Momentum / breakout V3 Filtered | €10.177,60 | €137,88 | 29 | 29 | 44,83% | 1,28 | €4,75 | 2,70% |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | Momentum / breakout V3 Filtered | €10.175,99 | €194,76 | 25 | 25 | 44,00% | 1,52 | €7,79 | 3,34% |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | Momentum / breakout | €10.159,32 | €161,18 | 23 | 23 | 47,83% | 1,49 | €7,01 | 1,76% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.144,18 | €168,12 | 3 | 3 | 100,00% | ∞ | €56,04 | 0,63% |
| TEST | Combo Adaptive Runner25 V1 | Combo Adaptive | €10.134,76 | €125,00 | 28 | 28 | 46,43% | 1,24 | €4,46 | 2,12% |
| TEST | Main Side Regime Guard V1 | Confluenza trend | €10.127,11 | €72,40 | 11 | 11 | 36,36% | 1,22 | €6,58 | 2,40% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €10.123,46 | €92,12 | 3 | 3 | 66,67% | 21,53 | €30,71 | 0,79% |
| TEST | Combo Trend Side Regime Guard V1 | Combo Trend | €10.112,64 | €113,03 | 21 | 21 | 52,38% | 1,33 | €5,38 | 1,73% |
| TEST | Doge Ema 1H | Trend following EMA | €10.102,84 | €91,86 | 8 | 8 | 62,50% | 1,55 | €11,48 | 1,36% |
| TEST | 1H Fast V3 No Esports Long Only V1 | Momentum / breakout V3 Filtered | €10.090,48 | €109,28 | 31 | 31 | 45,16% | 1,19 | €3,53 | 2,82% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €10.086,98 | €86,98 | 1 | 1 | 100,00% | ∞ | €86,98 | 0,40% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.084,12 | €84,12 | 1 | 1 | 100,00% | ∞ | €84,12 | 0,30% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €10.074,08 | €93,80 | 5 | 5 | 80,00% | 2,64 | €18,76 | 1,08% |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | Momentum / breakout V3 Filtered | €10.071,28 | €71,28 | 19 | 19 | 42,11% | 1,16 | €3,75 | 2,17% |
| TEST | Rapida 1H V1 | Momentum / breakout | €10.048,63 | €51,31 | 77 | 77 | 35,06% | 1,03 | €0,67 | 6,76% |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | Momentum / breakout V3 Filtered | €10.045,64 | €-11,16 | 9 | 9 | 33,33% | 0,94 | €-1,24 | 1,99% |
| TEST | Ampia 4H | Confluenza trend | €10.036,04 | €-23,31 | 21 | 21 | 23,81% | 0,96 | €-1,11 | 3,68% |
| TEST | Combo Adaptive Quality7 V1 | Combo Adaptive | €10.034,70 | €55,43 | 21 | 21 | 38,10% | 1,19 | €2,64 | 1,64% |
| TEST | 1H Fast Tp2 V1 | Momentum / breakout | €10.034,69 | €27,46 | 60 | 60 | 36,67% | 1,02 | €0,46 | 2,58% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €10.020,48 | €13,28 | 3 | 3 | 66,67% | 1,24 | €4,43 | 0,89% |
| TEST | 1H Balanced V3 Long Only V1 | Confluenza trend V3 Filtered | €10.018,01 | €42,78 | 13 | 13 | 38,46% | 1,16 | €3,29 | 1,46% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €10.015,98 | €40,94 | 45 | 44 | 40,00% | 1,03 | €0,91 | 5,10% |
| TEST | Scanner Top5 Btc Tp3 V1 | Scanner Top 5 + forza BTC | €10.013,11 | €32,32 | 20 | 20 | 40,00% | 1,06 | €1,62 | 3,22% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €10.010,36 | €10,36 | 10 | 10 | 30,00% | 1,22 | €1,04 | 0,25% |
| TEST | Combo Adaptive Long Only V1 | Combo Adaptive | €10.008,47 | €-0,10 | 14 | 14 | 35,71% | 1,00 | €-0,01 | 2,34% |
| TEST | Scanner Top5 Btc Runner25 V1 | Scanner Top 5 + forza BTC | €10.007,22 | €26,39 | 24 | 24 | 41,67% | 1,04 | €1,10 | 3,44% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €10.005,46 | €-52,00 | 1 | 1 | 0,00% | 0,00 | €-52,00 | 0,79% |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | Momentum / breakout V3 Filtered | €10.003,88 | €4,24 | 7 | 7 | 42,86% | 1,03 | €0,61 | 2,15% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €10.002,07 | €2,07 | 10 | 10 | 30,00% | 1,22 | €0,21 | 0,05% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €10.000,84 | €-51,83 | 1 | 1 | 0,00% | 0,00 | €-51,83 | 0,77% |
| TEST | Scalp RSI Short 85 · €50 · 15x | Inversione RSI estrema 15m | €10.000,61 | €0,61 | 2 | 2 | 50,00% | 1,74 | €0,30 | 0,07% |
| TEST | Scalp RSI Short 85 · €10 · 15x | Inversione RSI estrema 15m | €10.000,12 | €0,12 | 2 | 2 | 50,00% | 1,74 | €0,06 | 0,01% |
| TEST | Scanner Bottom5 Short Continuation V1 | Scanner Bottom5 Short Continuation | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 80 · €10 · 15x | Inversione RSI estrema 15m | €9.999,70 | €-0,30 | 3 | 3 | 66,67% | 0,63 | €-0,10 | 0,02% |
| TEST | Scalp RSI Long 20 · €10 · 15x | Inversione RSI estrema 15m | €9.998,96 | €-1,04 | 2 | 2 | 0,00% | 0,00 | €-0,52 | 0,02% |
| TEST | Scalp RSI Short 85 · prudente · 5x | Inversione RSI estrema 15m | €9.998,64 | €-1,36 | 2 | 2 | 50,00% | 0,42 | €-0,68 | 0,11% |
| TEST | Scalp RSI Short 80 · €50 · 15x | Inversione RSI estrema 15m | €9.998,52 | €-1,48 | 3 | 3 | 66,67% | 0,63 | €-0,49 | 0,09% |
| TEST | Scalp RSI Long 15 · €10 · 15x | Inversione RSI estrema 15m | €9.998,50 | €-1,50 | 1 | 1 | 0,00% | 0,00 | €-1,50 | 0,02% |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | Momentum / breakout | €9.996,45 | €-3,55 | 25 | 25 | 36,00% | 0,99 | €-0,14 | 2,27% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €9.996,42 | €-19,38 | 4 | 4 | 50,00% | 0,82 | €-4,84 | 1,49% |
| TEST | 1H Balanced Short Trend Down Strict V1 | Confluenza trend | €9.995,87 | €-4,13 | 1 | 1 | 0,00% | 0,00 | €-4,13 | 0,59% |
| TEST | Scalp RSI Long 20 · €50 · 15x | Inversione RSI estrema 15m | €9.994,81 | €-5,19 | 2 | 2 | 0,00% | 0,00 | €-2,59 | 0,08% |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | €9.992,50 | €-7,50 | 1 | 1 | 0,00% | 0,00 | €-7,50 | 0,11% |
| TEST | Scalp RSI Long 25 · €10 · 15x | Inversione RSI estrema 15m | €9.991,12 | €-8,88 | 7 | 7 | 28,57% | 0,24 | €-1,27 | 0,12% |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | Momentum / breakout V3 Filtered | €9.990,65 | €-9,35 | 14 | 14 | 42,86% | 0,97 | €-0,67 | 2,46% |
| TEST | Scalp RSI Short 80 · prudente · 5x | Inversione RSI estrema 15m | €9.990,24 | €-9,76 | 3 | 3 | 66,67% | 0,28 | €-3,25 | 0,21% |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | €9.988,38 | €-11,62 | 1 | 1 | 0,00% | 0,00 | €-11,62 | 0,17% |
| TEST | Scalp RSI Long 20 · prudente · 5x | Inversione RSI estrema 15m | €9.983,60 | €-16,40 | 2 | 2 | 0,00% | 0,00 | €-8,20 | 0,24% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €9.979,60 | €-17,71 | 16 | 14 | 43,75% | 0,95 | €-1,11 | 1,69% |
| TEST | 1H Fast V3 No Esports V1 | Momentum / breakout V3 Filtered | €9.977,73 | €-27,83 | 61 | 61 | 39,34% | 0,98 | €-0,46 | 2,49% |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | Scanner Top 5 + forza BTC | €9.969,22 | €-30,15 | 9 | 9 | 33,33% | 0,87 | €-3,35 | 2,84% |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | Scanner Bottom 5 Short | €9.966,45 | €5,91 | 10 | 10 | 70,00% | 1,04 | €0,59 | 1,38% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €9.959,49 | €-40,51 | 2 | 2 | 50,00% | 0,28 | €-20,26 | 0,91% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €9.955,61 | €-44,39 | 7 | 7 | 14,29% | 0,12 | €-6,34 | 0,58% |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | €9.955,59 | €-44,41 | 7 | 7 | 28,57% | 0,24 | €-6,34 | 0,58% |
| TEST | Sol Ema 1H | Trend following EMA | €9.953,65 | €-22,91 | 5 | 5 | 40,00% | 0,86 | €-4,58 | 1,67% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.951,70 | €-48,30 | 10 | 10 | 30,00% | 0,27 | €-4,83 | 0,58% |
| TEST | Btc Ema 4H | Trend following EMA | €9.950,68 | €-49,32 | 1 | 1 | 0,00% | 0,00 | €-49,32 | 0,96% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €9.949,62 | €-50,38 | 1 | 1 | 0,00% | 0,00 | €-50,38 | 0,74% |
| TEST | Scanner Bottom5 Short Profit Lock V1 | Scanner Bottom 5 Short | €9.948,75 | €-78,99 | 7 | 7 | 57,14% | 0,50 | €-11,28 | 1,53% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €9.944,25 | €-49,32 | 1 | 1 | 0,00% | 0,00 | €-49,32 | 1,02% |
| TEST | Scanner Top5 Btc Btc Le3 V1 | Scanner Top 5 + forza BTC | €9.938,65 | €-42,34 | 16 | 16 | 43,75% | 0,91 | €-2,65 | 3,23% |
| TEST | Combo Adaptive Tp3 V1 | Combo Adaptive | €9.929,58 | €-66,67 | 13 | 13 | 46,15% | 0,76 | €-5,13 | 1,41% |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | Momentum / breakout V3 Filtered | €9.923,70 | €-76,30 | 49 | 49 | 46,94% | 0,93 | €-1,56 | 3,21% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.922,91 | €-98,75 | 4 | 4 | 25,00% | 0,41 | €-24,69 | 1,89% |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | Combo Adaptive | €9.922,04 | €-77,96 | 11 | 11 | 45,45% | 0,71 | €-7,09 | 1,95% |
| TEST | Btc Ema 1H | Trend following EMA | €9.918,99 | €-88,14 | 6 | 6 | 33,33% | 0,59 | €-14,69 | 1,56% |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | Scanner Top 5 + forza BTC | €9.915,06 | €-66,02 | 15 | 15 | 40,00% | 0,87 | €-4,40 | 3,38% |
| TEST | Combo Scanner | Combo Scanner | €9.914,45 | €-66,57 | 43 | 43 | 41,86% | 0,94 | €-1,55 | 3,25% |
| TEST | Combo Adaptive Regime V1 | Combo Adaptive | €9.903,77 | €-95,76 | 21 | 21 | 47,62% | 0,79 | €-4,56 | 2,18% |
| TEST | Eth Ema 4H | Trend following EMA | €9.894,27 | €-105,73 | 2 | 2 | 0,00% | 0,00 | €-52,87 | 1,21% |
| TEST | Sol Ema 4H | Trend following EMA | €9.892,80 | €-103,69 | 2 | 2 | 0,00% | 0,00 | €-51,84 | 1,10% |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | Momentum / breakout V3 Filtered | €9.892,65 | €-117,37 | 24 | 24 | 45,83% | 0,77 | €-4,89 | 3,08% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | Momentum / breakout V3 Filtered | €9.886,03 | €-95,73 | 26 | 26 | 38,46% | 0,83 | €-3,68 | 3,33% |
| TEST | 1H Fast V3 Nohigh V1 | Momentum / breakout V3 Filtered | €9.874,22 | €-121,63 | 59 | 59 | 38,98% | 0,91 | €-2,06 | 2,96% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.871,99 | €-128,01 | 5 | 5 | 20,00% | 0,42 | €-25,60 | 1,62% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €9.863,73 | €-113,80 | 19 | 19 | 36,84% | 0,82 | €-5,99 | 3,60% |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | Momentum / breakout V3 Filtered | €9.857,49 | €-142,51 | 44 | 44 | 40,91% | 0,86 | €-3,24 | 2,86% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €9.848,43 | €-165,97 | 3 | 3 | 0,00% | 0,00 | €-55,32 | 1,82% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.842,81 | €-252,96 | 32 | 32 | 34,38% | 0,69 | €-7,91 | 3,34% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.833,51 | €-160,53 | 11 | 11 | 36,36% | 0,52 | €-14,59 | 2,92% |
| TEST | Scanner Bottom10 Short | Scanner Bottom10 Short | €9.820,87 | €-205,24 | 8 | 8 | 37,50% | 0,26 | €-25,65 | 2,72% |
| TEST | Scanner Bottom15 Short | Scanner Bottom15 Short | €9.820,87 | €-205,24 | 8 | 8 | 37,50% | 0,26 | €-25,65 | 2,72% |
| TEST | Scanner Bottom20 Short | Scanner Bottom20 Short | €9.820,87 | €-205,24 | 8 | 8 | 37,50% | 0,26 | €-25,65 | 2,72% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | Momentum / breakout V3 Filtered | €9.813,54 | €-186,11 | 22 | 22 | 40,91% | 0,63 | €-8,46 | 2,93% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €9.812,08 | €-164,81 | 6 | 6 | 33,33% | 0,29 | €-27,47 | 2,61% |
| TEST | Master Adaptive Gb20 Be V1 | Master Adaptive Consensus | €9.806,54 | €-191,77 | 21 | 21 | 19,05% | 0,67 | €-9,13 | 3,32% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.799,60 | €-200,40 | 6 | 6 | 33,33% | 0,08 | €-33,40 | 2,09% |
| TEST | Combo Adaptive Quality7 Regime V1 | Combo Adaptive | €9.797,24 | €-202,76 | 11 | 11 | 27,27% | 0,31 | €-18,43 | 2,32% |
| TEST | Master Adaptive Gb20 Partial V1 | Master Adaptive Consensus | €9.796,05 | €-202,30 | 16 | 16 | 31,25% | 0,62 | €-12,64 | 2,89% |
| TEST | 1H Balanced Long No Rhv V1 | Confluenza trend | €9.792,95 | €-217,20 | 15 | 15 | 33,33% | 0,59 | €-14,48 | 2,95% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.775,26 | €-248,55 | 31 | 31 | 35,48% | 0,67 | €-8,02 | 5,48% |
| TEST | Master Adaptive Gb20 Loss Cap V1 | Master Adaptive Consensus | €9.770,94 | €-263,40 | 17 | 17 | 23,53% | 0,60 | €-15,49 | 3,74% |
| TEST | Scanner Top5 Btc Guard V1 | Scanner Top 5 + forza BTC | €9.761,07 | €-249,98 | 21 | 21 | 28,57% | 0,64 | €-11,90 | 3,65% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | Momentum / breakout V3 Filtered | €9.757,70 | €-242,30 | 6 | 6 | 0,00% | 0,00 | €-40,38 | 2,42% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €9.754,29 | €-211,40 | 46 | 46 | 39,13% | 0,83 | €-4,60 | 5,30% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | Momentum / breakout V3 Filtered | €9.739,73 | €-242,30 | 6 | 6 | 0,00% | 0,00 | €-40,38 | 2,69% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €9.738,67 | €-296,38 | 19 | 19 | 31,58% | 0,62 | €-15,60 | 3,64% |
| TEST | Scanner Top5 Btc Mfe V1 | Scanner Top 5 + forza BTC | €9.737,45 | €-260,59 | 29 | 29 | 37,93% | 0,57 | €-8,99 | 3,95% |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | Scanner Top 5 + forza BTC | €9.730,44 | €-269,23 | 31 | 31 | 38,71% | 0,68 | €-8,68 | 3,93% |
| TEST | Combo Adaptive Partial 1R V1 | Combo Adaptive | €9.729,81 | €-269,71 | 26 | 26 | 46,15% | 0,56 | €-10,37 | 3,32% |
| TEST | Eth Ema 1H | Trend following EMA | €9.727,87 | €-272,13 | 8 | 8 | 25,00% | 0,16 | €-34,02 | 2,76% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €9.726,39 | €-308,63 | 18 | 18 | 27,78% | 0,57 | €-17,15 | 3,98% |
| TEST | Scanner Top10 Long | Scanner Top10 Long | €9.705,45 | €-274,96 | 16 | 16 | 37,50% | 0,47 | €-17,18 | 4,75% |
| TEST | Scanner Top15 Long | Scanner Top15 Long | €9.705,45 | €-274,96 | 16 | 16 | 37,50% | 0,47 | €-17,18 | 4,75% |
| TEST | Scanner Top20 Long | Scanner Top20 Long | €9.705,45 | €-274,96 | 16 | 16 | 37,50% | 0,47 | €-17,18 | 4,75% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €9.698,71 | €-336,21 | 16 | 16 | 25,00% | 0,53 | €-21,01 | 4,03% |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | €9.694,71 | €-340,19 | 16 | 16 | 25,00% | 0,53 | €-21,26 | 4,07% |
| TEST | Combo Trend | Combo Trend | €9.682,06 | €-403,86 | 47 | 47 | 34,04% | 0,75 | €-8,59 | 7,02% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €9.628,98 | €-369,16 | 52 | 52 | 57,69% | 0,60 | €-7,10 | 4,27% |
| TEST | 1H Fast V3 Long Only V1 | Momentum / breakout V3 Filtered | €9.607,23 | €-374,86 | 51 | 51 | 31,37% | 0,71 | €-7,35 | 4,91% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €9.556,70 | €-496,80 | 36 | 36 | 25,00% | 0,54 | €-13,80 | 7,55% |
| TEST | Scanner Top5 Btc Guard Mfe V1 | Scanner Top 5 + forza BTC | €9.552,70 | €-446,98 | 38 | 38 | 36,84% | 0,57 | €-11,76 | 5,08% |
| TEST | Combo Adaptive Mfe Trail | Combo Adaptive | €9.551,78 | €-461,15 | 37 | 37 | 32,43% | 0,48 | €-12,46 | 5,33% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €9.410,39 | €-586,95 | 25 | 25 | 24,00% | 0,49 | €-23,48 | 6,09% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | LAB | SHORT | Confluenza trend | 240m | 3,0x | 0,17841 | 0,17841 | 0,17841 | 0,23699 | 0,13559 | €136,26 | €408,77 | €0,00 | €-0,00 |
| Principale 4H | ONDO | LONG | Confluenza trend | 240m | 3,0x | 0,40344 | 0,40344 | 0,37762 | 0,27098 | 0,45509 | €254,70 | €764,09 | €48,91 | €0,00 |
| Principale 4H | SHIB | LONG | Confluenza trend | 240m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €8,88 | €26,63 | €2,22 | €0,00 |
| Principale 4H | HYPE | SHORT | Confluenza trend | 240m | 3,0x | 57,27654 | 56,30800 | 59,33830 | 76,08234 | 53,15302 | €419,05 | €1.257,15 | €45,25 | €21,26 |
| Principale 4H | AKE | LONG | Confluenza trend | 240m | 3,0x | 0,00412 | 0,00442 | 0,00412 | 0,00276 | 0,00510 | €128,49 | €385,48 | €0,00 | €28,65 |
| Principale 4H | SOL | SHORT | Confluenza trend | 240m | 3,0x | 73,19036 | 73,31100 | 75,30024 | 97,22119 | 68,97060 | €9,18 | €27,53 | €0,79 | €-0,05 |
| Bilanciata 1H V1 | ADA | SHORT | Confluenza trend | 60m | 3,0x | 0,16703 | 0,16703 | 0,16365 | 0,22187 | 0,16112 | €978,72 | €2.936,17 | €0,00 | €-0,00 |
| Bilanciata 1H V1 | ALLO | SHORT | Confluenza trend | 60m | 3,0x | 0,36179 | 0,36179 | 0,40521 | 0,48058 | 0,27496 | €141,53 | €424,59 | €50,95 | €-0,00 |
| Bilanciata 1H V1 | ZEC | SHORT | Confluenza trend | 60m | 3,0x | 483,74323 | 478,27000 | 481,86559 | 642,57226 | 461,39195 | €17,56 | €52,68 | €0,00 | €0,60 |
| Bilanciata 1H V1 | HYPE | SHORT | Confluenza trend | 60m | 3,0x | 57,07858 | 56,30800 | 56,70908 | 75,81938 | 54,73013 | €786,25 | €2.358,74 | €0,00 | €31,84 |
| Bilanciata 1H V1 | NEAR | SHORT | Confluenza trend | 60m | 3,0x | 1,73096 | 1,73096 | 1,69553 | 2,29929 | 1,66292 | €19,50 | €58,51 | €0,00 | €-0,00 |
| Bilanciata 1H V1 | BTC | SHORT | Confluenza trend | 60m | 3,0x | 63620,87328 | 63450,80000 | 64537,01386 | 84509,72667 | 61788,59213 | €1.153,42 | €3.460,26 | €49,83 | €9,25 |
| Bilanciata 1H V1 | SOL | SHORT | Confluenza trend | 60m | 3,0x | 72,83343 | 73,31100 | 73,94273 | 96,74707 | 70,61483 | €70,54 | €211,63 | €3,22 | €-1,39 |
| 1H Balanced Long No Rhv V1 | XMR | LONG | Confluenza trend | 60m | 3,0x | 366,72991 | 366,72991 | 360,04130 | 246,32025 | 380,10712 | €915,26 | €2.745,79 | €50,08 | €0,00 |
| 1H Balanced Long No Rhv V1 | AKE | LONG | Confluenza trend | 60m | 3,0x | 0,00430 | 0,00442 | 0,00378 | 0,00289 | 0,00533 | €136,92 | €410,76 | €49,29 | €12,05 |
| Bilanciata 1H V2 | ADA | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,16276 | 0,16276 | 0,16511 | 0,21620 | 0,15807 | €1.185,56 | €3.556,68 | €51,22 | €-0,00 |
| Bilanciata 1H V2 | WLD | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,34349 | 0,34349 | 0,35287 | 0,45627 | 0,32475 | €26,53 | €79,60 | €2,17 | €-0,00 |
| Bilanciata 1H V2 | ALLO | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,35543 | 0,35543 | 0,39400 | 0,47213 | 0,27829 | €146,68 | €440,04 | €47,75 | €-0,00 |
| Bilanciata 1H V3 Filtered | WLD | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,34349 | 0,34349 | 0,35287 | 0,45627 | 0,32475 | €23,43 | €70,29 | €1,92 | €-0,00 |
| Bilanciata 1H V3 Filtered | ALLO | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,34255 | 0,34255 | 0,37914 | 0,45502 | 0,26938 | €160,61 | €481,84 | €51,46 | €-0,00 |
| Bilanciata 1H V3 Filtered | ESPORTS | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,02905 | 0,02905 | 0,03254 | 0,03859 | 0,02208 | €142,96 | €428,87 | €51,46 | €-0,00 |
| Bilanciata 1H V3 Filtered | ZEC | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 488,51228 | 478,27000 | 481,68165 | 648,90714 | 465,56407 | €24,50 | €73,51 | €0,00 | €1,54 |
| Bilanciata 1H V3 Filtered | SOL | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 73,97120 | 73,31100 | 73,95646 | 98,25841 | 71,73999 | €39,75 | €119,24 | €0,00 | €1,06 |
| Bilanciata 1H V3 Filtered | BTC | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 63046,01827 | 63450,80000 | 63953,88094 | 83746,12761 | 61230,29295 | €1.219,33 | €3.657,98 | €52,67 | €-23,49 |
| Rapida 1H V1 | ADA | SHORT | Momentum / breakout | 60m | 3,0x | 0,16185 | 0,16185 | 0,16367 | 0,21499 | 0,15913 | €1.486,90 | €4.460,70 | €49,96 | €-0,00 |
| 1H Fast Score 6 75 V1 | ALLO | SHORT | Momentum / breakout | 60m | 3,0x | 0,33713 | 0,33713 | 0,36471 | 0,44782 | 0,29576 | €212,67 | €638,01 | €52,19 | €-0,00 |
| 1H Fast Score 6 75 V1 | ZEC | SHORT | Momentum / breakout | 60m | 3,0x | 483,74323 | 478,27000 | 480,32558 | 642,57226 | 470,70499 | €972,21 | €2.916,64 | €0,00 | €33,00 |
| 1H Fast Score 6 75 V1 | HYPE | SHORT | Momentum / breakout | 60m | 3,0x | 56,71366 | 56,30800 | 56,57805 | 75,33464 | 55,35861 | €1.094,57 | €3.283,72 | €0,00 | €23,49 |
| 1H Fast Score 6 75 V1 | SOL | SHORT | Momentum / breakout | 60m | 3,0x | 73,97120 | 73,31100 | 73,78447 | 98,25841 | 72,66966 | €1.496,78 | €4.490,35 | €0,00 | €40,08 |
| 1H Fast Score 6 75 V1 | BTC | SHORT | Momentum / breakout | 60m | 3,0x | 63747,34798 | 63450,80000 | 63562,15308 | 84677,72723 | 62676,39253 | €30,97 | €92,90 | €0,00 | €0,43 |
| 1H Fast Score 6 75 V1 | SUI | SHORT | Momentum / breakout | 60m | 3,0x | 0,68319 | 0,68350 | 0,69289 | 0,90750 | 0,66864 | €37,40 | €112,21 | €1,59 | €-0,05 |
| 1H Fast Score 6 75 No Trend Up V1 | ALLO | SHORT | Momentum / breakout | 60m | 3,0x | 0,33808 | 0,33808 | 0,36389 | 0,44909 | 0,29937 | €218,91 | €656,73 | €50,14 | €-0,00 |
| 1H Fast Score 6 75 No Trend Up V1 | ZEC | SHORT | Momentum / breakout | 60m | 3,0x | 483,74323 | 478,27000 | 480,32558 | 642,57226 | 470,70499 | €961,25 | €2.883,74 | €0,00 | €32,63 |
| 1H Fast Score 6 75 No Trend Up V1 | HYPE | SHORT | Momentum / breakout | 60m | 3,0x | 56,71366 | 56,30800 | 56,57805 | 75,33464 | 55,35861 | €1.083,98 | €3.251,95 | €0,00 | €23,26 |
| 1H Fast Score 6 75 No Trend Up V1 | SOL | SHORT | Momentum / breakout | 60m | 3,0x | 73,97120 | 73,31100 | 73,78447 | 98,25841 | 72,66966 | €103,21 | €309,64 | €0,00 | €2,76 |
| 1H Fast Score 6 75 No Trend Up V1 | BTC | SHORT | Momentum / breakout | 60m | 3,0x | 63046,01827 | 63450,80000 | 63752,13368 | 83746,12761 | 61986,84517 | €30,09 | €90,27 | €1,01 | €-0,58 |
| 1H Fast Score 6 75 Range Only V1 | ESPORTS | SHORT | Momentum / breakout | 60m | 3,0x | 0,02828 | 0,02828 | 0,03168 | 0,03757 | 0,02319 | €143,01 | €429,04 | €51,48 | €-0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | ALLO | SHORT | Momentum / breakout | 60m | 3,0x | 0,33713 | 0,33713 | 0,36471 | 0,44782 | 0,29576 | €211,20 | €633,59 | €51,83 | €-0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | ZEC | SHORT | Momentum / breakout | 60m | 3,0x | 483,74323 | 478,27000 | 480,32558 | 642,57226 | 470,70499 | €968,54 | €2.905,63 | €0,00 | €32,88 |
| 1H Fast Score 6 75 Cost Aware V1 | HYPE | SHORT | Momentum / breakout | 60m | 3,0x | 56,71366 | 56,30800 | 56,57805 | 75,33464 | 55,35861 | €1.090,44 | €3.271,33 | €0,00 | €23,40 |
| 1H Fast Score 6 75 Cost Aware V1 | SOL | SHORT | Momentum / breakout | 60m | 3,0x | 73,97120 | 73,31100 | 73,78447 | 98,25841 | 72,66966 | €1.491,13 | €4.473,40 | €0,00 | €39,93 |
| 1H Fast Score 6 75 Cost Aware V1 | BTC | SHORT | Momentum / breakout | 60m | 3,0x | 63747,34798 | 63450,80000 | 63562,15308 | 84677,72723 | 62676,39253 | €35,76 | €107,29 | €0,00 | €0,50 |
| 1H Fast Score 6 75 Cost Aware V1 | DOGE | SHORT | Momentum / breakout | 60m | 3,0x | 0,06998 | 0,07008 | 0,07082 | 0,09295 | 0,06871 | €43,95 | €131,85 | €1,59 | €-0,20 |
| 1H Fast Nohigh Cap75 V1 | ALLO | SHORT | Momentum / breakout | 60m | 3,0x | 0,33808 | 0,33808 | 0,36389 | 0,44909 | 0,29937 | €225,73 | €677,19 | €51,70 | €-0,00 |
| 1H Fast No Pepe V1 | ADA | SHORT | Momentum / breakout | 60m | 3,0x | 0,16185 | 0,16185 | 0,16367 | 0,21499 | 0,15913 | €1.512,75 | €4.538,24 | €50,83 | €-0,00 |
| 1H Fast No Pepe V1 | WLD | SHORT | Momentum / breakout | 60m | 3,0x | 0,34959 | 0,34959 | 0,35668 | 0,46437 | 0,33896 | €838,72 | €2.516,16 | €51,00 | €-0,00 |
| 1H Fast No Pepe V1 | ZEC | SHORT | Momentum / breakout | 60m | 3,0x | 483,74323 | 478,27000 | 480,32558 | 642,57226 | 470,70499 | €28,82 | €86,46 | €0,00 | €0,98 |
| 1H Fast No Pepe V1 | HYPE | SHORT | Momentum / breakout | 60m | 3,0x | 56,71366 | 56,30800 | 56,57805 | 75,33464 | 55,35861 | €1.064,33 | €3.192,99 | €0,00 | €22,84 |
| 1H Fast No Pepe V1 | BTC | SHORT | Momentum / breakout | 60m | 3,0x | 63620,87328 | 63450,80000 | 64333,42706 | 84509,72667 | 62552,04261 | €19,21 | €57,62 | €0,65 | €0,15 |
| 1H Fast No Pepe V1 | SOL | SHORT | Momentum / breakout | 60m | 3,0x | 73,18636 | 73,31100 | 74,08780 | 97,21588 | 71,83419 | €8,54 | €25,63 | €0,32 | €-0,04 |
| 1H Fast No Pepe V1 | XRP | SHORT | Momentum / breakout | 60m | 3,0x | 1,05690 | 1,05906 | 1,06874 | 1,40391 | 1,03914 | €9,88 | €29,65 | €0,33 | €-0,06 |
| 1H Fast No Pepe V1 | DOGE | SHORT | Momentum / breakout | 60m | 3,0x | 0,06994 | 0,07008 | 0,07075 | 0,09290 | 0,06871 | €1.435,95 | €4.307,84 | €50,18 | €-8,87 |
| 1H Fast Tp2 V1 | ADA | SHORT | Momentum / breakout | 60m | 3,0x | 0,16185 | 0,16185 | 0,16367 | 0,21499 | 0,15823 | €1.482,83 | €4.448,49 | €49,82 | €-0,00 |
| 1H Fast Tp2 V1 | WLD | SHORT | Momentum / breakout | 60m | 3,0x | 0,34959 | 0,34959 | 0,35668 | 0,46437 | 0,33542 | €42,01 | €126,02 | €2,55 | €-0,00 |
| 1H Fast Tp2 V1 | ALLO | SHORT | Momentum / breakout | 60m | 3,0x | 0,35543 | 0,35543 | 0,38543 | 0,47213 | 0,29543 | €187,33 | €561,99 | €47,43 | €-0,00 |
| 1H Fast Tp2 V1 | ZEC | SHORT | Momentum / breakout | 60m | 3,0x | 483,74323 | 478,27000 | 480,32558 | 642,57226 | 466,35890 | €27,61 | €82,84 | €0,00 | €0,94 |
| 1H Fast Tp2 V1 | HYPE | SHORT | Momentum / breakout | 60m | 3,0x | 56,71366 | 56,30800 | 56,57805 | 75,33464 | 54,90694 | €1.039,45 | €3.118,34 | €0,00 | €22,30 |
| 1H Fast Tp2 V1 | NEAR | SHORT | Momentum / breakout | 60m | 3,0x | 1,67599 | 1,67599 | 1,70517 | 2,22628 | 1,61763 | €25,97 | €77,91 | €1,36 | €-0,00 |
| 1H Fast Tp2 V1 | DOGE | SHORT | Momentum / breakout | 60m | 3,0x | 0,06994 | 0,07008 | 0,07075 | 0,09290 | 0,06831 | €1.394,41 | €4.183,24 | €48,73 | €-8,61 |
| Rapida 1H V2 | ADA | SHORT | Momentum / breakout V2 | 60m | 3,0x | 0,16185 | 0,16185 | 0,16367 | 0,21499 | 0,15913 | €1.494,54 | €4.483,63 | €50,22 | €-0,00 |
| Rapida 1H V3 Filtered | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16185 | 0,16185 | 0,16367 | 0,21499 | 0,15913 | €1.521,20 | €4.563,60 | €51,11 | €-0,00 |
| Rapida 1H V3 Filtered | WLD | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,34959 | 0,34959 | 0,35668 | 0,46437 | 0,33896 | €843,41 | €2.530,22 | €51,28 | €-0,00 |
| Rapida 1H V3 Filtered | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 483,74323 | 478,27000 | 480,32558 | 642,57226 | 470,70499 | €27,86 | €83,58 | €0,00 | €0,95 |
| Rapida 1H V3 Filtered | HYPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 56,71366 | 56,30800 | 56,57805 | 75,33464 | 55,35861 | €1.037,92 | €3.113,75 | €0,00 | €22,27 |
| Rapida 1H V3 Filtered | SOL | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 73,18636 | 73,31100 | 74,08780 | 97,21588 | 71,83419 | €8,54 | €25,62 | €0,32 | €-0,04 |
| Rapida 1H V3 Filtered | XRP | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,05690 | 1,05906 | 1,06874 | 1,40391 | 1,03914 | €9,49 | €28,48 | €0,32 | €-0,06 |
| Rapida 1H V3 Filtered | DOGE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,06994 | 0,07008 | 0,07075 | 0,09290 | 0,06871 | €1.429,19 | €4.287,56 | €49,95 | €-8,83 |
| 1H Fast V3 Cap75 V1 | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,33808 | 0,33808 | 0,36389 | 0,44909 | 0,29937 | €227,32 | €681,96 | €52,06 | €-0,00 |
| 1H Fast V3 Cap75 V1 | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 483,74323 | 478,27000 | 480,32558 | 642,57226 | 470,70499 | €30,24 | €90,72 | €0,00 | €1,03 |
| 1H Fast V3 Cap75 V1 | HYPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 56,71366 | 56,30800 | 56,57805 | 75,33464 | 55,35861 | €1.087,88 | €3.263,64 | €0,00 | €23,34 |
| 1H Fast V3 Cap75 V1 | SOL | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 73,97120 | 73,31100 | 73,78447 | 98,25841 | 72,66966 | €1.494,31 | €4.482,92 | €0,00 | €40,01 |
| 1H Fast V3 Cap75 V1 | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 63046,01827 | 63450,80000 | 63752,13368 | 83746,12761 | 61986,84517 | €54,22 | €162,67 | €1,82 | €-1,04 |
| 1H Fast V3 Cap75 V1 | BEAT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,91758 | 2,91933 | 3,26769 | 3,87552 | 2,39241 | €135,27 | €405,82 | €48,70 | €-0,24 |
| 1H Fast V3 Nohigh V1 | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16185 | 0,16185 | 0,16367 | 0,21499 | 0,15913 | €1.485,86 | €4.457,58 | €49,92 | €-0,00 |
| 1H Fast V3 Nohigh V1 | WLD | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,34959 | 0,34959 | 0,35668 | 0,46437 | 0,33896 | €823,75 | €2.471,25 | €50,08 | €-0,00 |
| 1H Fast V3 Long Only V1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00462 | 0,00442 | 0,00407 | 0,00311 | 0,00546 | €135,03 | €405,10 | €48,61 | €-17,66 |
| 1H Fast V3 No Esports V1 | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16185 | 0,16185 | 0,16367 | 0,21499 | 0,15913 | €1.489,89 | €4.469,66 | €50,06 | €-0,00 |
| 1H Fast V3 No Esports V1 | WLD | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,34959 | 0,34959 | 0,35668 | 0,46437 | 0,33896 | €825,98 | €2.477,95 | €50,22 | €-0,00 |
| 1H Fast V3 No Esports V1 | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 483,74323 | 478,27000 | 480,32558 | 642,57226 | 470,70499 | €27,30 | €81,91 | €0,00 | €0,93 |
| 1H Fast V3 No Esports V1 | HYPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 56,71366 | 56,30800 | 56,57805 | 75,33464 | 55,35861 | €1.017,33 | €3.051,98 | €0,00 | €21,83 |
| 1H Fast V3 No Esports V1 | SOL | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 73,18636 | 73,31100 | 74,08780 | 97,21588 | 71,83419 | €8,36 | €25,09 | €0,31 | €-0,04 |
| 1H Fast V3 No Esports V1 | XRP | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,05690 | 1,05906 | 1,06874 | 1,40391 | 1,03914 | €9,31 | €27,93 | €0,31 | €-0,06 |
| 1H Fast V3 No Esports V1 | DOGE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,06994 | 0,07008 | 0,07075 | 0,09290 | 0,06871 | €1.400,09 | €4.200,28 | €48,93 | €-8,65 |
| 1H Fast V3 No Esports Long Only V1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00462 | 0,00442 | 0,00407 | 0,00311 | 0,00546 | €141,78 | €425,35 | €51,04 | €-18,54 |
| 1H Fast V3 No Esports Mfe Lock V1 | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16185 | 0,16185 | 0,16367 | 0,21499 | 0,15913 | €1.510,84 | €4.532,53 | €50,76 | €-0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | WLD | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,34959 | 0,34959 | 0,35668 | 0,46437 | 0,33896 | €11,86 | €35,57 | €0,72 | €-0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,33165 | 0,33165 | 0,36472 | 0,44055 | 0,28205 | €170,96 | €512,89 | €51,14 | €-0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 63620,87328 | 63450,80000 | 63620,87328 | 84509,72667 | 62552,04261 | €1.511,01 | €4.533,03 | €0,00 | €12,12 |
| 1H Fast V3 No Esports Mfe Lock V1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00462 | 0,00442 | 0,00407 | 0,00311 | 0,00546 | €143,94 | €431,82 | €51,82 | €-18,83 |
| 1H Fast V3 No Esports Mfe Lock V1 | SOL | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 73,18636 | 73,31100 | 74,08780 | 97,21588 | 71,83419 | €13,72 | €41,16 | €0,51 | €-0,07 |
| 1H Fast V3 No Esports Mfe Lock V1 | DOGE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,07018 | 0,07008 | 0,07099 | 0,09322 | 0,06895 | €37,48 | €112,45 | €1,31 | €0,15 |
| Ampia 4H | HYPE | SHORT | Confluenza trend | 240m | 2,0x | 58,36732 | 56,30800 | 61,80927 | 87,25915 | 48,72988 | €424,03 | €848,06 | €50,01 | €29,92 |
| Ampia 4H | TAO | SHORT | Confluenza trend | 240m | 2,0x | 189,05650 | 189,05650 | 197,51338 | 282,63946 | 165,37722 | €558,68 | €1.117,36 | €49,98 | €-0,00 |
| Ampia 4H | XMR | LONG | Confluenza trend | 240m | 2,0x | 364,45854 | 364,45854 | 347,94701 | 184,05156 | 410,69083 | €544,42 | €1.088,84 | €49,33 | €0,00 |
| Ampia 4H | AKE | LONG | Confluenza trend | 240m | 2,0x | 0,00412 | 0,00442 | 0,00362 | 0,00208 | 0,00550 | €208,53 | €417,05 | €50,05 | €31,00 |
| Ampia 4H | XRP | SHORT | Confluenza trend | 240m | 2,0x | 1,06427 | 1,05906 | 1,09657 | 1,59108 | 0,97382 | €13,35 | €26,70 | €0,81 | €0,13 |
| Ampia 4H | BTC | SHORT | Confluenza trend | 240m | 2,0x | 63318,66373 | 63450,80000 | 64874,97444 | 94661,40228 | 58960,99415 | €18,28 | €36,56 | €0,90 | €-0,08 |
| Forza relativa 1H V1 | NIGHT | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,02031 | 0,02031 | 0,02210 | 0,03036 | 0,01637 | €285,91 | €571,83 | €50,45 | €-0,00 |
| Forza relativa 1H V1 | ONDO | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,42171 | €891,90 | €1.783,80 | €49,29 | €0,00 |
| Forza relativa 1H V1 | WLD | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,32287 | €14,97 | €29,93 | €0,82 | €-0,00 |
| Forza relativa 1H V1 | ZEC | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 483,74323 | 478,27000 | 482,47314 | 723,19613 | 459,15682 | €1.028,52 | €2.057,03 | €0,00 | €23,27 |
| Forza relativa 1H V1 | HYPE | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 57,27654 | 56,30800 | 56,68219 | 85,62843 | 54,89695 | €1.014,19 | €2.028,38 | €0,00 | €34,30 |
| Forza relativa 1H V1 | NEAR | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 1,70198 | 1,70198 | 1,73908 | 2,54446 | 1,62035 | €112,91 | €225,83 | €4,92 | €-0,00 |
| Forza relativa 1H V1 | XRP | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 1,05518 | 1,05906 | 1,07037 | 1,57749 | 1,02175 | €24,53 | €49,07 | €0,71 | €-0,18 |
| Forza relativa 1H V2 | WLD | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,32287 | €47,70 | €95,39 | €2,60 | €-0,00 |
| Forza relativa 1H V2 | XMR | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 367,08012 | 367,08012 | 360,46822 | 185,37546 | 381,62629 | €1.446,12 | €2.892,24 | €52,10 | €0,00 |
| Forza relativa 1H V2 | ZEC | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 477,51448 | 478,27000 | 488,76646 | 713,88414 | 452,76011 | €1.065,11 | €2.130,22 | €50,20 | €-3,37 |
| Forza relativa 1H V2 | AKE | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,00462 | 0,00442 | 0,00407 | 0,00234 | 0,00584 | €209,44 | €418,88 | €50,27 | €-18,26 |
| Benchmark Donchian breakout 1H | ALLO | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,35678 | 0,35678 | 0,39959 | 0,53338 | 0,24974 | €215,19 | €430,38 | €51,65 | €-0,00 |
| Benchmark Donchian breakout 1H | HYPE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 58,25535 | 56,30800 | 56,67469 | 87,09174 | 55,41491 | €1.364,10 | €2.728,20 | €0,00 | €91,20 |
| Benchmark Donchian breakout 1H | XRP | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 1,08939 | 1,05906 | 1,06529 | 1,62864 | 1,04582 | €1.662,45 | €3.324,89 | €0,00 | €92,58 |
| Benchmark Donchian breakout 1H | ZEC | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 483,74323 | 478,27000 | 496,16061 | 723,19613 | 452,69979 | €19,59 | €39,18 | €1,01 | €0,44 |
| Benchmark Donchian breakout 1H | NEAR | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 1,70198 | 1,70198 | 1,74321 | 2,54446 | 1,59891 | €52,48 | €104,96 | €2,54 | €-0,00 |
| Benchmark Donchian breakout 1H | BTC | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 63620,87328 | 63450,80000 | 64638,80725 | 95113,20555 | 61076,03835 | €1.401,20 | €2.802,39 | €44,84 | €7,49 |
| Benchmark Donchian breakout 1H | SOL | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 72,83343 | 73,31100 | 74,06598 | 108,88598 | 69,75205 | €39,01 | €78,03 | €1,32 | €-0,51 |
| Donchian 1H Gb20 120R V1 | HYPE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 58,25535 | 56,30800 | 56,67469 | 87,09174 | 55,41491 | €1.281,83 | €2.563,66 | €0,00 | €85,70 |
| Donchian 1H Gb20 120R V1 | XRP | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 1,08939 | 1,05906 | 1,06529 | 1,62864 | 1,04582 | €1.562,18 | €3.124,36 | €0,00 | €86,99 |
| Donchian 1H Gb20 120R V1 | ZEC | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 483,74323 | 478,27000 | 496,16061 | 723,19613 | 452,69979 | €978,17 | €1.956,34 | €50,22 | €22,13 |
| Donchian 1H Gb20 120R V1 | NEAR | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 1,70198 | 1,70198 | 1,74321 | 2,54446 | 1,59891 | €88,92 | €177,84 | €4,31 | €-0,00 |
| Donchian 1H Gb20 120R V1 | BTC | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 63046,01827 | 63450,80000 | 64054,75457 | 94253,79732 | 60524,17754 | €69,70 | €139,41 | €2,23 | €-0,90 |
| Benchmark Bollinger mean reversion 1H | BTC | LONG | Bollinger mean reversion | 60m | 2,0x | 63772,85202 | 63450,80000 | 63007,57780 | 32205,29027 | 64920,76336 | €1.981,46 | €3.962,93 | €47,56 | €-20,01 |
| Benchmark Bollinger mean reversion 1H | XRP | LONG | Bollinger mean reversion | 60m | 2,0x | 1,06582 | 1,05906 | 1,05303 | 0,53824 | 1,08501 | €1.980,83 | €3.961,66 | €47,54 | €-25,14 |
| Benchmark Bollinger mean reversion 1H | DOGE | LONG | Bollinger mean reversion | 60m | 2,0x | 0,06977 | 0,07008 | 0,06887 | 0,03524 | 0,07113 | €1.881,64 | €3.763,27 | €48,65 | €16,51 |
| Benchmark Bollinger mean reversion 1H | SOL | LONG | Bollinger mean reversion | 60m | 2,0x | 73,21564 | 73,31100 | 72,24942 | 36,97390 | 74,66497 | €958,36 | €1.916,71 | €25,29 | €2,50 |
| Benchmark trend following EMA 1H | LAB | LONG | Trend following EMA | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €207,05 | €414,10 | €49,69 | €0,00 |
| Benchmark trend following EMA 1H | ALLO | SHORT | Trend following EMA | 60m | 2,0x | 0,35372 | 0,35372 | 0,39616 | 0,52881 | 0,26034 | €209,15 | €418,30 | €50,20 | €-0,00 |
| Benchmark trend following EMA 1H | XMR | LONG | Trend following EMA | 60m | 2,0x | 367,08012 | 367,08012 | 359,73357 | 185,37546 | 383,24253 | €17,91 | €35,83 | €0,72 | €0,00 |
| Benchmark trend following EMA 1H | XRP | SHORT | Trend following EMA | 60m | 2,0x | 1,09230 | 1,05906 | 1,06496 | 1,63299 | 1,05385 | €1.438,76 | €2.877,52 | €0,00 | €87,57 |
| Benchmark trend following EMA 1H | NEAR | SHORT | Trend following EMA | 60m | 2,0x | 1,73096 | 1,73096 | 1,69735 | 2,58779 | 1,64780 | €22,55 | €45,10 | €0,00 | €-0,00 |
| Benchmark trend following EMA 1H | AKE | LONG | Trend following EMA | 60m | 2,0x | 0,00430 | 0,00442 | 0,00378 | 0,00217 | 0,00543 | €202,78 | €405,56 | €48,67 | €11,89 |
| Benchmark trend following EMA 1H | SUI | SHORT | Trend following EMA | 60m | 2,0x | 0,67450 | 0,68350 | 0,68819 | 1,00837 | 0,64436 | €18,93 | €37,85 | €0,77 | €-0,51 |
| Scanner Top 5 Long 1H | XMR | LONG | Scanner Top 5 Long | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10712 | €70,71 | €141,42 | €2,58 | €0,00 |
| Scanner Top 5 Long 1H | AKE | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,00430 | 0,00442 | 0,00378 | 0,00217 | 0,00533 | €218,43 | €436,86 | €52,42 | €12,81 |
| Scanner Bottom 5 Short 1H | ADA | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,16703 | 0,16703 | 0,16365 | 0,24971 | 0,16112 | €1.381,07 | €2.762,13 | €0,00 | €-0,00 |
| Scanner Bottom 5 Short 1H | ALLO | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,36179 | 0,36179 | 0,40521 | 0,54088 | 0,27496 | €202,53 | €405,06 | €48,61 | €-0,00 |
| Scanner Bottom 5 Short 1H | ESPORTS | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,03342 | 0,03342 | 0,03342 | 0,04997 | 0,02540 | €202,66 | €405,32 | €0,00 | €-0,00 |
| Scanner Bottom 5 Short 1H | ZEC | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 483,74323 | 478,27000 | 481,86559 | 723,19613 | 461,39195 | €18,93 | €37,87 | €0,00 | €0,43 |
| Scanner Bottom 5 Short 1H | HYPE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 57,07858 | 56,30800 | 56,70908 | 85,33248 | 54,73013 | €1.150,85 | €2.301,70 | €0,00 | €31,07 |
| Scanner Bottom 5 Short 1H | NEAR | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1,70198 | 1,70198 | 1,73908 | 2,54446 | 1,62777 | €17,87 | €35,75 | €0,78 | €-0,00 |
| Scanner Bottom 5 Short 1H | SUI | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,67450 | 0,68350 | 0,68682 | 1,00837 | 0,64984 | €21,90 | €43,79 | €0,80 | €-0,58 |
| Scanner Top10 Long | XMR | LONG | Scanner Top10 Long | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10712 | €1.371,36 | €2.742,71 | €50,02 | €0,00 |
| Scanner Top10 Long | SHIB | LONG | Scanner Top10 Long | 60m | 2,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €24,14 | €48,29 | €2,71 | €0,00 |
| Scanner Top10 Long | AKE | LONG | Scanner Top10 Long | 60m | 2,0x | 0,00462 | 0,00442 | 0,00407 | 0,00234 | 0,00573 | €202,57 | €405,14 | €48,62 | €-17,66 |
| Scanner Bottom10 Short | ADA | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,16193 | 0,16193 | 0,16426 | 0,24209 | 0,15727 | €1.731,26 | €3.462,51 | €49,86 | €-0,00 |
| Scanner Bottom10 Short | ALLO | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,35250 | 0,35250 | 0,39075 | 0,52699 | 0,27600 | €224,69 | €449,38 | €48,76 | €-0,00 |
| Scanner Bottom10 Short | ESPORTS | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,03342 | 0,03342 | 0,03342 | 0,04997 | 0,02540 | €203,44 | €406,87 | €0,00 | €-0,00 |
| Scanner Bottom10 Short | ZEC | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 483,74323 | 478,27000 | 481,86559 | 723,19613 | 461,39195 | €18,78 | €37,56 | €0,00 | €0,42 |
| Scanner Bottom10 Short | HYPE | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 57,07858 | 56,30800 | 56,70908 | 85,33248 | 54,73013 | €1.141,57 | €2.283,13 | €0,00 | €30,82 |
| Scanner Bottom10 Short | NEAR | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 1,70198 | 1,70198 | 1,73908 | 2,54446 | 1,62777 | €17,73 | €35,46 | €0,77 | €-0,00 |
| Scanner Bottom10 Short | SUI | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,67450 | 0,68350 | 0,68682 | 1,00837 | 0,64984 | €21,72 | €43,44 | €0,79 | €-0,58 |
| Scanner Top15 Long | XMR | LONG | Scanner Top15 Long | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10712 | €1.371,36 | €2.742,71 | €50,02 | €0,00 |
| Scanner Top15 Long | SHIB | LONG | Scanner Top15 Long | 60m | 2,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €24,14 | €48,29 | €2,71 | €0,00 |
| Scanner Top15 Long | AKE | LONG | Scanner Top15 Long | 60m | 2,0x | 0,00462 | 0,00442 | 0,00407 | 0,00234 | 0,00573 | €202,57 | €405,14 | €48,62 | €-17,66 |
| Scanner Bottom15 Short | ADA | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,16193 | 0,16193 | 0,16426 | 0,24209 | 0,15727 | €1.731,26 | €3.462,51 | €49,86 | €-0,00 |
| Scanner Bottom15 Short | ALLO | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,35250 | 0,35250 | 0,39075 | 0,52699 | 0,27600 | €224,69 | €449,38 | €48,76 | €-0,00 |
| Scanner Bottom15 Short | ESPORTS | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,03342 | 0,03342 | 0,03342 | 0,04997 | 0,02540 | €203,44 | €406,87 | €0,00 | €-0,00 |
| Scanner Bottom15 Short | ZEC | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 483,74323 | 478,27000 | 481,86559 | 723,19613 | 461,39195 | €18,78 | €37,56 | €0,00 | €0,42 |
| Scanner Bottom15 Short | HYPE | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 57,07858 | 56,30800 | 56,70908 | 85,33248 | 54,73013 | €1.141,57 | €2.283,13 | €0,00 | €30,82 |
| Scanner Bottom15 Short | NEAR | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 1,70198 | 1,70198 | 1,73908 | 2,54446 | 1,62777 | €17,73 | €35,46 | €0,77 | €-0,00 |
| Scanner Bottom15 Short | SUI | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,67450 | 0,68350 | 0,68682 | 1,00837 | 0,64984 | €21,72 | €43,44 | €0,79 | €-0,58 |
| Scanner Top20 Long | XMR | LONG | Scanner Top20 Long | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10712 | €1.371,36 | €2.742,71 | €50,02 | €0,00 |
| Scanner Top20 Long | SHIB | LONG | Scanner Top20 Long | 60m | 2,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €24,14 | €48,29 | €2,71 | €0,00 |
| Scanner Top20 Long | AKE | LONG | Scanner Top20 Long | 60m | 2,0x | 0,00462 | 0,00442 | 0,00407 | 0,00234 | 0,00573 | €202,57 | €405,14 | €48,62 | €-17,66 |
| Scanner Bottom20 Short | ADA | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,16193 | 0,16193 | 0,16426 | 0,24209 | 0,15727 | €1.731,26 | €3.462,51 | €49,86 | €-0,00 |
| Scanner Bottom20 Short | ALLO | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,35250 | 0,35250 | 0,39075 | 0,52699 | 0,27600 | €224,69 | €449,38 | €48,76 | €-0,00 |
| Scanner Bottom20 Short | ESPORTS | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,03342 | 0,03342 | 0,03342 | 0,04997 | 0,02540 | €203,44 | €406,87 | €0,00 | €-0,00 |
| Scanner Bottom20 Short | ZEC | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 483,74323 | 478,27000 | 481,86559 | 723,19613 | 461,39195 | €18,78 | €37,56 | €0,00 | €0,42 |
| Scanner Bottom20 Short | HYPE | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 57,07858 | 56,30800 | 56,70908 | 85,33248 | 54,73013 | €1.141,57 | €2.283,13 | €0,00 | €30,82 |
| Scanner Bottom20 Short | NEAR | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 1,70198 | 1,70198 | 1,73908 | 2,54446 | 1,62777 | €17,73 | €35,46 | €0,77 | €-0,00 |
| Scanner Bottom20 Short | SUI | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,67450 | 0,68350 | 0,68682 | 1,00837 | 0,64984 | €21,72 | €43,44 | €0,79 | €-0,58 |
| Scanner Top 5 + forza BTC 1H | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €216,56 | €433,12 | €51,97 | €0,00 |
| Scanner Top 5 + forza BTC 1H | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 381,44484 | €37,16 | €74,32 | €1,36 | €0,00 |
| Scanner Top 5 + forza BTC 1H | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00430 | 0,00442 | 0,00378 | 0,00217 | 0,00543 | €215,67 | €431,34 | €51,76 | €12,65 |
| Scanner Top5 Btc Mfe V1 | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 367,08012 | 367,08012 | 360,46822 | 185,37546 | 381,62629 | €1.363,71 | €2.727,43 | €49,13 | €0,00 |
| Scanner Top5 Btc Mfe V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00442 | 0,00442 | 0,00389 | 0,00223 | 0,00559 | €202,87 | €405,74 | €48,69 | €-0,08 |
| Scanner Top5 Btc Guard V1 | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €202,47 | €404,95 | €48,59 | €0,00 |
| Scanner Top5 Btc Guard V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00430 | 0,00442 | 0,00378 | 0,00217 | 0,00543 | €203,11 | €406,23 | €48,75 | €11,91 |
| Scanner Top5 Btc Btc Le3 V1 | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €207,87 | €415,74 | €49,89 | €0,00 |
| Scanner Top5 Btc Btc Le3 V1 | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 381,44484 | €37,63 | €75,26 | €1,37 | €0,00 |
| Scanner Top5 Btc Btc Le3 V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00462 | 0,00442 | 0,00407 | 0,00234 | 0,00584 | €207,48 | €414,96 | €49,80 | €-18,09 |
| Scanner Top5 Btc Btc 2 3 V1 | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €207,87 | €415,74 | €49,89 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00442 | 0,00442 | 0,00389 | 0,00223 | 0,00559 | €199,02 | €398,04 | €47,77 | €-0,08 |
| Scanner Top5 Btc Guard Btc Le3 V1 | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €205,84 | €411,68 | €49,40 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00462 | 0,00442 | 0,00407 | 0,00234 | 0,00584 | €206,99 | €413,98 | €49,68 | €-18,05 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00442 | 0,00442 | 0,00389 | 0,00223 | 0,00559 | €202,72 | €405,45 | €48,65 | €-0,08 |
| Scanner Top5 Btc Runner25 V1 | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,21338 | €207,96 | €415,92 | €49,91 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 386,79573 | €70,70 | €141,40 | €2,58 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00462 | 0,00442 | 0,00407 | 0,00234 | 0,00629 | €208,87 | €417,74 | €50,13 | €-18,21 |
| Scanner Top5 Btc Tp3 V1 | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,21338 | €207,96 | €415,92 | €49,91 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 386,79573 | €85,15 | €170,29 | €3,11 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00462 | 0,00442 | 0,00407 | 0,00234 | 0,00629 | €208,99 | €417,98 | €50,16 | €-18,22 |
| Global Confluence puro 1H | DOGE | SHORT | Global Confluence puro | 60m | 2,0x | 0,06998 | 0,07008 | 0,07118 | 0,10461 | 0,06696 | €1.428,07 | €2.856,13 | €49,20 | €-4,24 |
| Combo Trend | ALLO | SHORT | Combo Trend | 60m | 2,0x | 0,35372 | 0,35372 | 0,39616 | 0,52881 | 0,26034 | €209,35 | €418,70 | €50,24 | €-0,00 |
| Combo Trend | XRP | SHORT | Combo Trend | 60m | 2,0x | 1,09094 | 1,05906 | 1,06516 | 1,63096 | 1,05254 | €1.454,27 | €2.908,55 | €0,00 | €85,00 |
| Combo Trend | NEAR | SHORT | Combo Trend | 60m | 2,0x | 1,73096 | 1,73096 | 1,69735 | 2,58779 | 1,64780 | €26,55 | €53,10 | €0,00 | €-0,00 |
| Combo Trend | AKE | LONG | Combo Trend | 60m | 2,0x | 0,00430 | 0,00442 | 0,00378 | 0,00217 | 0,00543 | €183,87 | €367,73 | €44,13 | €10,78 |
| Combo Trend | SUI | SHORT | Combo Trend | 60m | 2,0x | 0,67989 | 0,68350 | 0,69410 | 1,01644 | 0,64864 | €67,05 | €134,10 | €2,80 | €-0,71 |
| Combo Trend | BTC | SHORT | Combo Trend | 60m | 2,0x | 63046,01827 | 63450,80000 | 64054,75457 | 94253,79732 | 60826,79843 | €59,43 | €118,86 | €1,90 | €-0,76 |
| Combo Trend | DOGE | SHORT | Combo Trend | 60m | 2,0x | 0,06998 | 0,07008 | 0,07118 | 0,10461 | 0,06732 | €1.373,53 | €2.747,07 | €47,32 | €-4,08 |
| Combo Mean Reversion | BTC | LONG | Combo Mean Reversion | 60m | 2,0x | 63772,85202 | 63450,80000 | 63007,57780 | 32205,29027 | 64997,29078 | €1.988,26 | €3.976,53 | €47,72 | €-20,08 |
| Combo Scanner | LAB | LONG | Combo Scanner | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €207,54 | €415,08 | €49,81 | €0,00 |
| Combo Scanner | XMR | LONG | Combo Scanner | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 381,44484 | €23,89 | €47,78 | €0,87 | €0,00 |
| Combo Scanner | AKE | LONG | Combo Scanner | 60m | 2,0x | 0,00462 | 0,00442 | 0,00407 | 0,00234 | 0,00584 | €207,27 | €414,53 | €49,74 | €-18,07 |
| Combo Adaptive | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15861 | 0,13958 | 0,08010 | 0,19668 | €213,13 | €426,26 | €51,15 | €0,00 |
| Combo Adaptive | WLD | SHORT | Combo Adaptive | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,32475 | €929,60 | €1.859,20 | €50,73 | €-0,00 |
| Combo Adaptive | ALLO | SHORT | Combo Adaptive | 60m | 2,0x | 0,36179 | 0,36179 | 0,40521 | 0,54088 | 0,27496 | €210,64 | €421,27 | €50,55 | €-0,00 |
| Combo Adaptive | HYPE | SHORT | Combo Adaptive | 60m | 2,0x | 56,91461 | 56,30800 | 56,70720 | 85,08735 | 54,57291 | €13,99 | €27,97 | €0,00 | €0,30 |
| Combo Adaptive | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,00430 | 0,00442 | 0,00378 | 0,00217 | 0,00533 | €208,31 | €416,62 | €49,99 | €12,22 |
| Combo Adaptive | NEAR | SHORT | Combo Adaptive | 60m | 2,0x | 1,67499 | 1,67499 | 1,71358 | 2,50412 | 1,59783 | €28,25 | €56,50 | €1,30 | €-0,00 |
| Combo Adaptive Mfe Trail | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15861 | 0,13958 | 0,08010 | 0,19668 | €201,70 | €403,39 | €48,41 | €0,00 |
| Combo Adaptive Mfe Trail | WLD | SHORT | Combo Adaptive | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,32475 | €883,78 | €1.767,56 | €48,23 | €-0,00 |
| Combo Adaptive Mfe Trail | HYPE | SHORT | Combo Adaptive | 60m | 2,0x | 56,71366 | 56,30800 | 56,71366 | 84,78691 | 54,39073 | €1.168,54 | €2.337,08 | €0,00 | €16,72 |
| Combo Adaptive Mfe Trail | SUI | SHORT | Combo Adaptive | 60m | 2,0x | 0,67450 | 0,68350 | 0,68682 | 1,00837 | 0,64984 | €24,23 | €48,47 | €0,89 | €-0,65 |
| Combo Adaptive Mfe Trail | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,00442 | 0,00442 | 0,00389 | 0,00223 | 0,00548 | €190,23 | €380,45 | €45,65 | €-0,08 |
| Combo Adaptive Quality7 V1 | WLD | SHORT | Combo Adaptive | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,32475 | €919,99 | €1.839,97 | €50,21 | €-0,00 |
| Combo Adaptive Quality7 V1 | ALLO | SHORT | Combo Adaptive | 60m | 2,0x | 0,36179 | 0,36179 | 0,40521 | 0,54088 | 0,27496 | €207,61 | €415,23 | €49,83 | €-0,00 |
| Combo Adaptive Quality7 V1 | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,00462 | 0,00442 | 0,00407 | 0,00234 | 0,00573 | €209,44 | €418,88 | €50,27 | €-18,26 |
| Combo Adaptive Regime V1 | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15861 | 0,13958 | 0,08010 | 0,19668 | €206,52 | €413,04 | €49,56 | €0,00 |
| Combo Adaptive Long Only V1 | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,41951 | €893,67 | €1.787,34 | €49,39 | €0,00 |
| Combo Adaptive Long Only V1 | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €205,55 | €411,10 | €49,33 | €0,00 |
| Combo Adaptive Long Only V1 | XMR | LONG | Combo Adaptive | 60m | 2,0x | 367,08012 | 367,08012 | 360,46822 | 185,37546 | 380,30391 | €1.384,19 | €2.768,37 | €49,86 | €0,00 |
| Combo Adaptive Long Only V1 | SHIB | LONG | Combo Adaptive | 60m | 2,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €12,85 | €25,69 | €1,44 | €0,00 |
| Combo Adaptive Long Only V1 | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,00430 | 0,00442 | 0,00378 | 0,00217 | 0,00533 | €207,92 | €415,84 | €49,90 | €12,19 |
| Combo Adaptive Partial 1R V1 | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,41951 | €893,02 | €1.786,04 | €49,36 | €0,00 |
| Combo Adaptive Partial 1R V1 | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €205,22 | €410,44 | €49,25 | €0,00 |
| Combo Adaptive Partial 1R V1 | WLD | SHORT | Combo Adaptive | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,32475 | €895,30 | €1.790,60 | €48,86 | €-0,00 |
| Combo Adaptive Partial 1R V1 | ALLO | SHORT | Combo Adaptive | 60m | 2,0x | 0,36179 | 0,36179 | 0,40521 | 0,54088 | 0,27496 | €98,69 | €197,38 | €23,69 | €-0,00 |
| Combo Adaptive Partial 1R V1 | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,00430 | 0,00442 | 0,00378 | 0,00217 | 0,00533 | €71,80 | €143,60 | €17,23 | €4,21 |
| Combo Adaptive Partial 1R V1 | SUI | SHORT | Combo Adaptive | 60m | 2,0x | 0,67450 | 0,68350 | 0,68682 | 1,00837 | 0,64984 | €12,97 | €25,95 | €0,47 | €-0,35 |
| Combo Adaptive Partial 1R V1 | XRP | SHORT | Combo Adaptive | 60m | 2,0x | 1,05724 | 1,05906 | 1,07246 | 1,58057 | 1,02679 | €204,10 | €408,19 | €5,88 | €-0,70 |
| Combo Adaptive Runner25 V1 | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,43050 | €902,18 | €1.804,37 | €49,86 | €0,00 |
| Combo Adaptive Runner25 V1 | WLD | SHORT | Combo Adaptive | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,31537 | €919,67 | €1.839,35 | €50,19 | €-0,00 |
| Combo Adaptive Runner25 V1 | XMR | LONG | Combo Adaptive | 60m | 2,0x | 367,08012 | 367,08012 | 360,46822 | 185,37546 | 386,91580 | €27,35 | €54,70 | €0,99 | €0,00 |
| Combo Adaptive Runner25 V1 | ALLO | SHORT | Combo Adaptive | 60m | 2,0x | 0,36179 | 0,36179 | 0,40521 | 0,54088 | 0,23155 | €207,78 | €415,57 | €49,87 | €-0,00 |
| Combo Adaptive Runner25 V1 | ZEC | SHORT | Combo Adaptive | 60m | 2,0x | 488,51228 | 478,27000 | 481,06439 | 730,32586 | 454,08996 | €32,69 | €65,39 | €0,00 | €1,37 |
| Combo Adaptive Runner25 V1 | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,00430 | 0,00442 | 0,00378 | 0,00217 | 0,00584 | €205,49 | €410,98 | €49,32 | €12,05 |
| Combo Adaptive Runner25 V1 | NEAR | SHORT | Combo Adaptive | 60m | 2,0x | 1,67499 | 1,67499 | 1,71358 | 2,50412 | 1,55924 | €28,88 | €57,76 | €1,33 | €-0,00 |
| Combo Adaptive Tp3 V1 | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,43050 | €902,18 | €1.804,37 | €49,86 | €0,00 |
| Combo Adaptive Tp3 V1 | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15861 | 0,13958 | 0,08010 | 0,21571 | €207,43 | €414,86 | €49,78 | €0,00 |
| Combo Adaptive Tp3 V1 | WLD | SHORT | Combo Adaptive | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,31537 | €911,80 | €1.823,59 | €49,76 | €-0,00 |
| Combo Adaptive Tp3 V1 | ALLO | SHORT | Combo Adaptive | 60m | 2,0x | 0,36179 | 0,36179 | 0,40521 | 0,54088 | 0,23155 | €205,00 | €410,00 | €49,20 | €-0,00 |
| Btc Ema 1H | BTC | SHORT | Trend following EMA | 60m | 3,0x | 63620,87328 | 63450,80000 | 64537,01386 | 84509,72667 | 61788,59213 | €1.147,21 | €3.441,62 | €49,56 | €9,20 |
| Btc Donchian 1H | BTC | SHORT | Donchian breakout 20 barre | 60m | 3,0x | 63747,34798 | 63450,80000 | 64563,31403 | 84677,72723 | 62115,41587 | €1.299,56 | €3.898,68 | €49,90 | €18,14 |
| Btc Donchian 4H | BTC | SHORT | Donchian breakout 20 barre | 240m | 2,0x | 63318,66373 | 63450,80000 | 64635,54187 | 94661,40228 | 59631,40456 | €1.196,13 | €2.392,26 | €49,75 | €-4,99 |
| Btc Bollinger 1H | BTC | LONG | Bollinger mean reversion | 60m | 3,0x | 63772,85202 | 63450,80000 | 63007,57780 | 42834,09894 | 64920,76336 | €1.412,24 | €4.236,72 | €50,84 | €-21,40 |
| Btc Adaptive 1H | BTC | SHORT | Combo Adaptive | 60m | 3,0x | 63620,87328 | 63450,80000 | 64537,01386 | 84509,72667 | 61788,59213 | €1.158,94 | €3.476,83 | €50,07 | €9,29 |
| Sol Ema 1H | SOL | SHORT | Trend following EMA | 60m | 3,0x | 72,83343 | 73,31100 | 73,94273 | 96,74707 | 70,61483 | €1.091,78 | €3.275,34 | €49,89 | €-21,48 |
| Sol Ema 4H | SOL | SHORT | Trend following EMA | 240m | 2,0x | 73,19036 | 73,31100 | 75,51123 | 109,41959 | 67,38819 | €780,22 | €1.560,44 | €49,48 | €-2,57 |
| Sol Donchian 1H | SOL | SHORT | Donchian breakout 20 barre | 60m | 3,0x | 73,97120 | 73,31100 | 73,83397 | 98,25841 | 71,98791 | €1.254,69 | €3.764,07 | €0,00 | €33,59 |
| Sol Donchian 4H | SOL | SHORT | Donchian breakout 20 barre | 240m | 2,0x | 75,96380 | 73,31100 | 74,54202 | 113,56589 | 69,59218 | €830,21 | €1.660,43 | €0,00 | €57,99 |
| Sol Bollinger 1H | SOL | LONG | Bollinger mean reversion | 60m | 3,0x | 72,86257 | 73,31100 | 71,93778 | 48,93936 | 74,24975 | €1.300,18 | €3.900,53 | €49,51 | €24,01 |
| Sol Adaptive 1H | SOL | SHORT | Combo Adaptive | 60m | 3,0x | 72,83343 | 73,31100 | 73,94273 | 96,74707 | 70,61483 | €1.076,25 | €3.228,75 | €49,18 | €-21,17 |
| Sol Adaptive 4H | SOL | SHORT | Combo Adaptive | 240m | 2,0x | 75,96380 | 73,31100 | 74,59202 | 113,56589 | 69,75767 | €761,04 | €1.522,08 | €0,00 | €53,15 |
| Doge Ema 1H | DOGE | SHORT | Trend following EMA | 60m | 3,0x | 0,07036 | 0,07008 | 0,07143 | 0,09346 | 0,06821 | €1.101,76 | €3.305,29 | €50,46 | €12,96 |
| Doge Donchian 1H | DOGE | SHORT | Donchian breakout 20 barre | 60m | 3,0x | 0,06975 | 0,07008 | 0,07071 | 0,09265 | 0,06782 | €1.220,11 | €3.660,32 | €50,47 | €-17,53 |
| Doge Bollinger 1H | DOGE | LONG | Bollinger mean reversion | 60m | 3,0x | 0,06977 | 0,07008 | 0,06887 | 0,04686 | 0,07113 | €1.267,95 | €3.803,86 | €49,17 | €16,68 |
| Master Adaptive V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €203,80 | €407,60 | €48,91 | €0,00 |
| Master Adaptive V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10713 | €21,54 | €43,08 | €0,79 | €0,00 |
| Master Adaptive V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00406 | 0,00442 | 0,00357 | 0,00205 | 0,00504 | €202,05 | €404,11 | €48,49 | €35,89 |
| Master Adaptive No Alt V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €203,80 | €407,60 | €48,91 | €0,00 |
| Master Adaptive No Alt V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10713 | €21,54 | €43,08 | €0,79 | €0,00 |
| Master Adaptive No Alt V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00406 | 0,00442 | 0,00357 | 0,00205 | 0,00504 | €202,14 | €404,28 | €48,51 | €35,90 |
| Master Adaptive Strict3 V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,41951 | €887,07 | €1.774,14 | €49,03 | €0,00 |
| Master Adaptive Strict3 V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10713 | €1.330,61 | €2.661,21 | €48,54 | €0,00 |
| Master Adaptive Expanded V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €203,80 | €407,60 | €48,91 | €0,00 |
| Master Adaptive Expanded V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10713 | €33,54 | €67,08 | €1,22 | €0,00 |
| Master Adaptive Expanded V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00406 | 0,00442 | 0,00357 | 0,00205 | 0,00504 | €202,97 | €405,94 | €48,71 | €36,05 |
| Master Adaptive Gb20 V1 | RIF | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,10582 | 0,10582 | 0,09312 | 0,05344 | 0,13122 | €201,89 | €403,77 | €48,45 | €0,00 |
| Master Adaptive Gb20 V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 367,08012 | 367,08012 | 360,46822 | 185,37546 | 380,30391 | €1.348,01 | €2.696,02 | €48,56 | €0,00 |
| Master Adaptive Runner25 V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,21338 | €203,80 | €407,60 | €48,91 | €0,00 |
| Master Adaptive Runner25 V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 386,79573 | €20,87 | €41,74 | €0,76 | €0,00 |
| Master Adaptive Runner25 V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00406 | 0,00442 | 0,00357 | 0,00205 | 0,00552 | €202,72 | €405,45 | €48,65 | €36,01 |
| Combo Adaptive Side Regime Guard V1 | ALLO | SHORT | Combo Adaptive | 60m | 2,0x | 0,35250 | 0,35250 | 0,39075 | 0,52699 | 0,27600 | €235,86 | €471,72 | €51,19 | €-0,00 |
| Combo Adaptive Side Regime Guard V1 | SHIB | LONG | Combo Adaptive | 60m | 2,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €450,93 | €901,86 | €50,61 | €0,00 |
| Combo Adaptive Side Regime Guard V1 | ZEC | SHORT | Combo Adaptive | 60m | 2,0x | 483,74323 | 478,27000 | 481,25805 | 723,19613 | 461,39195 | €34,68 | €69,35 | €0,00 | €0,78 |
| Combo Adaptive Side Regime Guard V1 | HYPE | SHORT | Combo Adaptive | 60m | 2,0x | 57,22855 | 56,30800 | 56,60840 | 85,55669 | 54,94411 | €29,04 | €58,08 | €0,00 | €0,93 |
| Combo Adaptive Side Regime Guard V1 | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,07038 | 0,07008 | 0,07031 | 0,10521 | 0,06823 | €1.664,07 | €3.328,14 | €0,00 | €13,99 |
| Combo Adaptive Side Regime Guard V1 | BTC | SHORT | Combo Adaptive | 60m | 2,0x | 63046,01827 | 63450,80000 | 63953,88094 | 94253,79732 | 61230,29295 | €1.798,90 | €3.597,79 | €51,81 | €-23,10 |
| Master Adaptive Gb20 Be V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 367,86058 | 367,86058 | 361,23463 | 185,76959 | 381,11249 | €1.403,77 | €2.807,55 | €50,57 | €0,00 |
| Master Adaptive Gb20 Partial V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10713 | €1.376,47 | €2.752,95 | €50,21 | €0,00 |
| Master Adaptive Gb20 Loss Cap V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 361,71345 | 185,19860 | 380,10713 | €1.835,86 | €3.671,71 | €50,22 | €0,00 |
| Master Adaptive Gb20 Loss Cap V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00406 | 0,00442 | 0,00357 | 0,00205 | 0,00536 | €207,77 | €415,53 | €49,86 | €36,90 |
| 1H Fast V3 Nohigh Range Only V1 | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,33165 | 0,33165 | 0,36472 | 0,44055 | 0,28205 | €170,92 | €512,75 | €51,13 | €-0,00 |
| 1H Fast V3 Nohigh Range Only V1 | ESPORTS | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,02828 | 0,02828 | 0,03168 | 0,03757 | 0,02319 | €142,68 | €428,04 | €51,37 | €-0,00 |
| 1H Fast V3 Nohigh Regime Guard V1 | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,33165 | 0,33165 | 0,36472 | 0,44055 | 0,28205 | €172,19 | €516,57 | €51,51 | €-0,00 |
| Main Side Regime Guard V1 | ALLO | SHORT | Confluenza trend | 240m | 3,0x | 0,38070 | 0,38070 | 0,37357 | 0,50570 | 0,28933 | €140,03 | €420,08 | €0,00 | €-0,00 |
| Main Side Regime Guard V1 | HYPE | SHORT | Confluenza trend | 240m | 3,0x | 57,27654 | 56,30800 | 59,33830 | 76,08234 | 53,15302 | €471,26 | €1.413,79 | €50,89 | €23,91 |
| Main Side Regime Guard V1 | AKE | LONG | Confluenza trend | 240m | 3,0x | 0,00412 | 0,00442 | 0,00412 | 0,00276 | 0,00510 | €140,35 | €421,05 | €0,00 | €31,30 |
| Main Side Regime Guard V1 | DOGE | SHORT | Confluenza trend | 240m | 3,0x | 0,07018 | 0,07008 | 0,07254 | 0,09322 | 0,06545 | €501,87 | €1.505,61 | €50,72 | €2,06 |
| Main Dynamic Asset Selector V1 | AKE | LONG | Confluenza trend | 240m | 3,0x | 0,00412 | 0,00442 | 0,00412 | 0,00276 | 0,00510 | €142,13 | €426,38 | €0,00 | €31,69 |
| Combo Trend Side Regime Guard V1 | ALLO | SHORT | Combo Trend | 60m | 2,0x | 0,35250 | 0,35250 | 0,39480 | 0,52699 | 0,25944 | €209,77 | €419,55 | €50,35 | €-0,00 |
| Combo Trend Side Regime Guard V1 | ESPORTS | SHORT | Combo Trend | 60m | 2,0x | 0,02845 | 0,02845 | 0,03187 | 0,04254 | 0,02094 | €202,36 | €404,73 | €48,57 | €-0,00 |
| Combo Trend Side Regime Guard V1 | ZEC | SHORT | Combo Trend | 60m | 2,0x | 477,71444 | 478,27000 | 490,38685 | 714,18308 | 449,83512 | €19,75 | €39,50 | €1,05 | €-0,05 |
| Combo Trend Side Regime Guard V1 | BTC | SHORT | Combo Trend | 60m | 2,0x | 63620,87328 | 63450,80000 | 64638,80725 | 95113,20555 | 61381,41854 | €1.578,90 | €3.157,81 | €50,52 | €8,44 |
| Combo Trend Side Regime Guard V1 | XRP | SHORT | Combo Trend | 60m | 2,0x | 1,06427 | 1,05906 | 1,08130 | 1,59108 | 1,02680 | €32,70 | €65,39 | €1,05 | €0,32 |
| Combo Trend Side Regime Guard V1 | SOL | SHORT | Combo Trend | 60m | 2,0x | 72,83343 | 73,31100 | 74,06598 | 108,88598 | 70,12181 | €45,02 | €90,04 | €1,52 | €-0,59 |
| Combo Trend Side Regime Guard V1 | DOGE | SHORT | Combo Trend | 60m | 2,0x | 0,06998 | 0,07008 | 0,07118 | 0,10461 | 0,06732 | €1.439,06 | €2.878,12 | €49,58 | €-4,28 |
| 1H Fast Nohigh Cap75 Short Only V1 | WLD | SHORT | Momentum / breakout | 60m | 3,0x | 0,34959 | 0,34959 | 0,35668 | 0,46437 | 0,33896 | €822,35 | €2.467,06 | €50,00 | €-0,00 |
| 1H Fast Nohigh Cap75 Short Only V1 | ALLO | SHORT | Momentum / breakout | 60m | 3,0x | 0,33808 | 0,33808 | 0,36389 | 0,44909 | 0,29937 | €212,58 | €637,75 | €48,69 | €-0,00 |
| 1H Balanced V3 Long Only V1 | XMR | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 366,72991 | 366,72991 | 360,04130 | 246,32025 | 380,10712 | €913,56 | €2.740,69 | €49,99 | €0,00 |
| 1H Balanced V3 Long Only V1 | ALLO | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,34255 | 0,34255 | 0,37914 | 0,45502 | 0,26938 | €156,01 | €468,04 | €49,99 | €-0,00 |
| 1H Balanced V3 Long Only V1 | ESPORTS | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,03342 | 0,03342 | 0,03342 | 0,04440 | 0,02540 | €137,40 | €412,21 | €0,00 | €-0,00 |
| 1H Balanced V3 Long Only V1 | ZEC | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 488,51228 | 478,27000 | 481,68165 | 648,90714 | 465,56407 | €14,72 | €44,15 | €0,00 | €0,93 |
| 1H Balanced V3 Long Only V1 | SOL | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 73,97120 | 73,31100 | 73,95646 | 98,25841 | 71,73999 | €36,55 | €109,64 | €0,00 | €0,98 |
| 1H Balanced V3 Long Only V1 | BTC | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 63046,01827 | 63450,80000 | 63953,88094 | 83746,12761 | 61230,29295 | €1.127,91 | €3.383,73 | €48,73 | €-21,72 |
| Scanner Bottom5 Short Profit Lock V1 | WLD | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,34449 | 0,34449 | 0,35368 | 0,51502 | 0,32613 | €937,87 | €1.875,74 | €50,00 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | ALLO | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,35250 | 0,35250 | 0,39075 | 0,52699 | 0,27600 | €227,60 | €455,20 | €49,39 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | ESPORTS | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,03342 | 0,03342 | 0,03262 | 0,04997 | 0,02540 | €206,07 | €412,14 | €0,00 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | ZEC | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 483,74323 | 478,27000 | 481,50810 | 723,19613 | 461,39195 | €19,22 | €38,45 | €0,00 | €0,44 |
| Scanner Bottom5 Short Profit Lock V1 | HYPE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 57,07858 | 56,30800 | 56,70908 | 85,33248 | 54,73013 | €1.168,54 | €2.337,08 | €0,00 | €31,55 |
| Scanner Bottom5 Short Profit Lock V1 | NEAR | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1,70198 | 1,70198 | 1,69456 | 2,54446 | 1,62777 | €18,15 | €36,30 | €0,00 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | SUI | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,67450 | 0,68350 | 0,68682 | 1,00837 | 0,64984 | €22,23 | €44,47 | €0,81 | €-0,59 |
| Scanner Bottom5 Short Mfe Trail V1 | WLD | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,34449 | 0,34449 | 0,35368 | 0,51502 | 0,32613 | €937,87 | €1.875,74 | €50,00 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | ALLO | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,35653 | 0,35653 | 0,39522 | 0,53301 | 0,27915 | €228,22 | €456,45 | €49,53 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | ESPORTS | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,02828 | 0,02828 | 0,03168 | 0,04229 | 0,02150 | €206,75 | €413,50 | €49,62 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | NEAR | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1,70198 | 1,70198 | 1,69456 | 2,54446 | 1,62777 | €15,45 | €30,90 | €0,00 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | SUI | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,67450 | 0,68350 | 0,68682 | 1,00837 | 0,64984 | €1.350,73 | €2.701,46 | €49,38 | €-36,07 |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 483,74323 | 478,27000 | 480,32558 | 642,57226 | 462,01282 | €927,74 | €2.783,21 | €0,00 | €31,49 |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | HYPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 57,07858 | 56,30800 | 56,56934 | 75,81938 | 54,79537 | €1.027,90 | €3.083,70 | €0,00 | €41,63 |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | SOL | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 73,97120 | 73,31100 | 73,78447 | 98,25841 | 71,80197 | €1.442,22 | €4.326,65 | €0,00 | €38,62 |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 63747,34798 | 63450,80000 | 63562,15308 | 84677,72723 | 61962,42224 | €84,44 | €253,33 | €0,00 | €1,18 |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | XRP | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,05948 | 1,05906 | 1,07134 | 1,40734 | 1,02981 | €1.444,58 | €4.333,74 | €48,54 | €1,71 |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | SUI | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,68319 | 0,68350 | 0,69289 | 0,90750 | 0,65893 | €87,71 | €263,14 | €3,74 | €-0,12 |
| Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,35250 | 0,35250 | 0,38225 | 0,46824 | 0,29300 | €194,51 | €583,53 | €49,25 | €-0,00 |
| Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | ESPORTS | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,02998 | 0,02998 | 0,02998 | 0,03983 | 0,02279 | €132,90 | €398,69 | €0,00 | €-0,00 |
| Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 483,74323 | 478,27000 | 480,32558 | 642,57226 | 466,35890 | €43,20 | €129,60 | €0,00 | €1,47 |
| Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | HYPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 56,71366 | 56,30800 | 56,57805 | 75,33464 | 54,90694 | €1.034,08 | €3.102,24 | €0,00 | €22,19 |
| Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | SOL | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 73,18636 | 73,31100 | 74,08780 | 97,21588 | 71,38347 | €8,38 | €25,15 | €0,31 | €-0,04 |
| Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | XRP | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,05690 | 1,05906 | 1,06874 | 1,40391 | 1,03322 | €9,61 | €28,84 | €0,32 | €-0,06 |
| Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | DOGE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,06994 | 0,07008 | 0,07075 | 0,09290 | 0,06831 | €1.395,23 | €4.185,70 | €48,76 | €-8,62 |
| Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | ESPORTS | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,02828 | 0,02828 | 0,03168 | 0,03757 | 0,02150 | €141,08 | €423,23 | €50,79 | €-0,00 |
| Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,35250 | 0,35250 | 0,38225 | 0,46824 | 0,29300 | €190,72 | €572,15 | €48,29 | €-0,00 |
| Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 483,74323 | 478,27000 | 480,32558 | 642,57226 | 466,35890 | €939,82 | €2.819,46 | €0,00 | €31,90 |
| Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | HYPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 56,71366 | 56,30800 | 56,57805 | 75,33464 | 54,90694 | €1.054,69 | €3.164,08 | €0,00 | €22,63 |
| Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | SOL | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 73,97120 | 73,31100 | 73,78447 | 98,25841 | 72,23582 | €21,56 | €64,67 | €0,00 | €0,58 |
| Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | XRP | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,06424 | 1,05906 | 1,07616 | 1,41366 | 1,04040 | €82,60 | €247,81 | €2,78 | €1,21 |
| Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 63046,01827 | 63450,80000 | 63752,13368 | 83746,12761 | 61633,78746 | €68,64 | €205,91 | €2,31 | €-1,32 |
| Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | DOGE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,06994 | 0,07008 | 0,07075 | 0,09290 | 0,06831 | €1.410,51 | €4.231,54 | €49,29 | €-8,71 |
| Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 483,74323 | 478,27000 | 480,32558 | 642,57226 | 462,01282 | €919,87 | €2.759,61 | €0,00 | €31,22 |
| Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | HYPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 57,07858 | 56,30800 | 56,56934 | 75,81938 | 54,79537 | €1.012,65 | €3.037,94 | €0,00 | €41,01 |
| Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | SOL | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 73,97120 | 73,31100 | 73,78447 | 98,25841 | 71,80197 | €78,41 | €235,23 | €0,00 | €2,10 |
| Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 63046,01827 | 63450,80000 | 63752,13368 | 83746,12761 | 61280,72976 | €90,53 | €271,58 | €3,04 | €-1,74 |
| Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | XRP | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,05948 | 1,05906 | 1,07134 | 1,40734 | 1,02981 | €1.431,80 | €4.295,40 | €48,11 | €1,69 |
| Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | SUI | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,68319 | 0,68350 | 0,69289 | 0,90750 | 0,65893 | €8,84 | €26,52 | €0,38 | €-0,01 |
| Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | DOGE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,06994 | 0,07008 | 0,07075 | 0,09290 | 0,06790 | €1.418,23 | €4.254,70 | €49,56 | €-8,76 |
| Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,33808 | 0,33808 | 0,36389 | 0,44909 | 0,28646 | €211,10 | €633,31 | €48,35 | €-0,00 |
| Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | XRP | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,06424 | 1,05906 | 1,06424 | 1,41366 | 1,04040 | €1.539,70 | €4.619,09 | €0,00 | €22,47 |
| Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 63620,87328 | 63450,80000 | 63620,87328 | 84509,72667 | 62195,76572 | €58,03 | €174,10 | €0,00 | €0,47 |
| Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | NEAR | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,66900 | 1,66900 | 1,69806 | 2,21699 | 1,61088 | €52,00 | €156,00 | €2,72 | €-0,00 |
| Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00462 | 0,00442 | 0,00407 | 0,00311 | 0,00573 | €144,80 | €434,39 | €52,13 | €-18,94 |
| Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | DOGE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,07018 | 0,07008 | 0,07099 | 0,09322 | 0,06854 | €1.466,24 | €4.398,72 | €51,24 | €6,02 |
| Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00462 | 0,00442 | 0,00407 | 0,00311 | 0,00573 | €137,56 | €412,68 | €49,52 | €-17,99 |
| Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00462 | 0,00442 | 0,00407 | 0,00311 | 0,00573 | €141,59 | €424,78 | €50,97 | €-18,52 |
| Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,35250 | 0,35250 | 0,38225 | 0,46824 | 0,29300 | €194,51 | €583,53 | €49,25 | €-0,00 |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,33713 | 0,33713 | 0,36471 | 0,44782 | 0,28197 | €208,24 | €624,73 | €51,11 | €-0,00 |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | ESPORTS | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,03070 | 0,03070 | 0,03070 | 0,04078 | 0,02333 | €138,06 | €414,17 | €0,00 | €-0,00 |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 483,74323 | 478,27000 | 480,32558 | 642,57226 | 466,35890 | €46,24 | €138,72 | €0,00 | €1,57 |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | HYPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 56,71366 | 56,30800 | 56,57805 | 75,33464 | 54,90694 | €1.073,18 | €3.219,54 | €0,00 | €23,03 |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | SOL | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 73,97120 | 73,31100 | 73,78447 | 98,25841 | 72,23582 | €1.460,75 | €4.382,26 | €0,00 | €39,11 |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 63046,01827 | 63450,80000 | 63752,13368 | 83746,12761 | 61633,78746 | €49,42 | €148,27 | €1,66 | €-0,95 |
| Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,35250 | 0,35250 | 0,38225 | 0,46824 | 0,29300 | €200,65 | €601,96 | €50,80 | €-0,00 |
| Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | ESPORTS | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,03342 | 0,03342 | 0,03342 | 0,04440 | 0,02540 | €136,12 | €408,37 | €0,00 | €-0,00 |
| Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00462 | 0,00442 | 0,00407 | 0,00311 | 0,00601 | €135,52 | €406,57 | €48,79 | €-17,73 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Scanner Top5 Btc Mfe V1 | AKE | LONG | 2026-07-28T04:53:40+00:00 | 0,00430 | €-0,57 | -0,01 | STOP |
| Scanner Top5 Btc Guard Mfe V1 | AKE | LONG | 2026-07-28T04:53:40+00:00 | 0,00430 | €-0,56 | -0,01 | STOP |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | AKE | LONG | 2026-07-28T04:53:40+00:00 | 0,00430 | €-0,57 | -0,01 | STOP |
| Master Adaptive Gb20 Partial V1 | BEAT | LONG | 2026-07-28T04:53:40+00:00 | 2,85482 | €-77,67 | -1,55 | STOP_GAP_STRESS |
| Master Adaptive Gb20 Loss Cap V1 | BEAT | LONG | 2026-07-28T04:53:40+00:00 | 2,85482 | €-103,62 | -2,07 | STOP_GAP_STRESS |
| Master Adaptive Gb20 Be V1 | BEAT | LONG | 2026-07-28T04:53:40+00:00 | 2,85482 | €-77,75 | -1,55 | STOP_GAP_STRESS |
| Combo Adaptive Mfe Trail | AKE | LONG | 2026-07-28T04:53:40+00:00 | 0,00430 | €-0,54 | -0,01 | STOP |
| 1H Fast V3 No Esports Long Only V1 | BEAT | LONG | 2026-07-28T04:53:40+00:00 | 2,85482 | €-99,59 | -1,99 | STOP_GAP_STRESS |
| 1H Fast V3 Long Only V1 | BEAT | LONG | 2026-07-28T04:53:40+00:00 | 2,85482 | €-97,66 | -1,99 | STOP_GAP_STRESS |
| 1H Fast V3 Long Nohigh Cap75 V1 | BEAT | LONG | 2026-07-28T04:53:40+00:00 | 2,85482 | €-98,73 | -1,99 | STOP_GAP_STRESS |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | BEAT | LONG | 2026-07-28T04:53:40+00:00 | 2,85482 | €-98,14 | -1,99 | STOP_GAP_STRESS |
| 1H Fast V3 Cap75 V1 | BEAT | LONG | 2026-07-28T04:53:40+00:00 | 2,85482 | €-103,59 | -1,99 | STOP_GAP_STRESS |

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

Generato: 2026-07-28 05:15 UTC


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

Segnali totali salvati: **60**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-07-28 | BTC | 63.381,14 | -1 | +3 | +2 | +2 | -2 | -1 | 0 | NON INSEGUIRE / RIDUCI RISCHIO |
| 2026-07-28 | DOGE | 0.06994 | +1 | +4 | +3 | +2 | -3 | -1 | 0 | STAI ALLA FINESTRA |
| 2026-07-28 | SOL | 73,27 | +1 | +4 | +3 | +3 | -3 | -1 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-07-27 | BTC | 65.325,99 | +5 | +4 | +3 | +3 | 0 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-07-27 | DOGE | 0.07289 | 0 | +3 | +2 | +2 | -3 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-07-27 | SOL | 76,40 | 0 | +4 | +3 | +2 | -3 | -1 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-07-26 | BTC | 64.454,23 | +5 | +4 | +3 | +2 | +1 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-07-26 | DOGE | 0.07344 | +2 | +3 | +2 | +2 | -2 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-07-26 | SOL | 75,10 | 0 | +4 | +3 | +2 | -3 | -1 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-07-25 | BTC | 64.087,96 | +2 | +3 | +3 | +2 | -2 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-07-25 | DOGE | 0.06949 | -1 | +2 | +1 | +2 | -3 | -1 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-07-25 | SOL | 74,17 | 0 | +4 | +3 | +2 | -3 | -1 | 0 | HOLD LEGGERO / ATTESA CONFERME |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 20 | 19 | 18 | 17 | 15 | 13 | 10 | 6 | 0 | 0 | 0 | 0 |
| SOL | 20 | 19 | 18 | 17 | 15 | 13 | 10 | 6 | 0 | 0 | 0 | 0 |
| DOGE | 20 | 19 | 18 | 17 | 15 | 13 | 10 | 6 | 0 | 0 | 0 | 0 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-07-15 | 14g | 2026-07-29 | domani |
| SOL | 2026-07-15 | 14g | 2026-07-29 | domani |
| DOGE | 2026-07-15 | 14g | 2026-07-29 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 17 | 41,18% | -0,02% | +0,01% | FEEDBACK RAPIDO |
| BTC | 2g | 16 | 43,75% | +0,22% | +0,03% | FEEDBACK RAPIDO |
| BTC | 3g | 15 | 40,00% | +0,06% | -0,21% | FEEDBACK RAPIDO |
| BTC | 5g | 14 | 28,57% | +0,39% | -0,51% | FEEDBACK RAPIDO |
| BTC | 7g | 12 | 50,00% | +1,22% | +0,42% | FEEDBACK RAPIDO |
| BTC | 10g | 9 | 66,67% | +2,24% | +1,51% | FEEDBACK RAPIDO |
| BTC | 14g | 6 | 100,00% | +2,03% | +2,03% | FEEDBACK RAPIDO |
| BTC | 21g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 30g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 1g | 14 | 42,86% | -0,19% | -0,69% | FEEDBACK RAPIDO |
| SOL | 2g | 14 | 21,43% | -0,41% | -1,09% | FEEDBACK RAPIDO |
| SOL | 3g | 14 | 14,29% | -0,64% | -1,49% | FEEDBACK RAPIDO |
| SOL | 5g | 14 | 35,71% | -1,05% | -1,42% | FEEDBACK RAPIDO |
| SOL | 7g | 12 | 41,67% | -0,70% | -1,35% | FEEDBACK RAPIDO |
| SOL | 10g | 9 | 33,33% | -0,47% | -0,94% | FEEDBACK RAPIDO |
| SOL | 14g | 5 | 40,00% | -1,95% | -0,36% | FEEDBACK RAPIDO |
| SOL | 21g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 30g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 1g | 18 | 50,00% | -0,06% | -0,02% | FEEDBACK RAPIDO |
| DOGE | 2g | 18 | 50,00% | -0,26% | -0,27% | FEEDBACK RAPIDO |
| DOGE | 3g | 17 | 47,06% | -0,33% | +0,33% | FEEDBACK RAPIDO |
| DOGE | 5g | 15 | 66,67% | -1,01% | +1,01% | FEEDBACK RAPIDO |
| DOGE | 7g | 13 | 69,23% | -1,21% | +1,21% | FEEDBACK RAPIDO |
| DOGE | 10g | 10 | 60,00% | -1,64% | +1,64% | FEEDBACK RAPIDO |
| DOGE | 14g | 6 | 66,67% | -2,43% | +2,43% | FEEDBACK RAPIDO |
| DOGE | 21g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 30g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 17 | 41,18% | -0,02% | +0,01% | -0,28% | +0,60% | FEEDBACK RAPIDO |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 19 | 42,11% | -0,05% | -0,05% | -0,30% | +0,53% | FEEDBACK RAPIDO |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 19 | 42,11% | -0,05% | -0,05% | -0,30% | +0,53% | FEEDBACK RAPIDO |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 15 | 40,00% | -0,13% | -0,13% | -0,39% | +0,37% | FEEDBACK RAPIDO |
| BTC | 1g | Tecnico | CALIBRABILE | 15 | 40,00% | +0,13% | -0,43% | -0,15% | +0,68% | FEEDBACK RAPIDO |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +2,00% | +2,00% | +1,48% | +2,25% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 16 | 43,75% | +0,22% | +0,03% | -0,32% | +1,09% | FEEDBACK RAPIDO |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 18 | 44,44% | +0,15% | +0,15% | -0,35% | +1,00% | FEEDBACK RAPIDO |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 18 | 44,44% | +0,15% | +0,15% | -0,35% | +1,00% | FEEDBACK RAPIDO |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 14 | 42,86% | -0,00% | -0,00% | -0,54% | +0,87% | FEEDBACK RAPIDO |
| BTC | 2g | Tecnico | CALIBRABILE | 15 | 40,00% | +0,29% | -0,44% | -0,24% | +1,10% | FEEDBACK RAPIDO |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +3,18% | +3,18% | +3,05% | +3,89% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 15 | 40,00% | +0,06% | -0,21% | -1,37% | +2,06% | FEEDBACK RAPIDO |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 17 | 58,82% | +0,20% | +0,20% | -1,32% | +1,98% | FEEDBACK RAPIDO |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 17 | 58,82% | +0,20% | +0,20% | -1,32% | +1,98% | FEEDBACK RAPIDO |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 13 | 61,54% | +0,21% | +0,21% | -1,36% | +1,88% | FEEDBACK RAPIDO |
| BTC | 3g | Tecnico | CALIBRABILE | 14 | 42,86% | +0,62% | +0,02% | -1,13% | +2,20% | FEEDBACK RAPIDO |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,88% | +1,88% | +1,44% | +4,24% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 14 | 28,57% | +0,39% | -0,51% | -2,21% | +2,60% | FEEDBACK RAPIDO |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 15 | 46,67% | +0,52% | +0,52% | -2,08% | +2,74% | FEEDBACK RAPIDO |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 15 | 46,67% | +0,52% | +0,52% | -2,08% | +2,74% | FEEDBACK RAPIDO |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 11 | 54,55% | +0,92% | +0,92% | -2,06% | +2,88% | FEEDBACK RAPIDO |
| BTC | 5g | Tecnico | CALIBRABILE | 12 | 50,00% | +0,81% | -0,50% | -1,77% | +3,10% | FEEDBACK RAPIDO |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,16% | -0,16% | -0,37% | +4,24% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 12 | 50,00% | +1,22% | +0,42% | -2,07% | +3,57% | FEEDBACK RAPIDO |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 13 | 69,23% | +1,15% | +1,15% | -1,93% | +3,66% | FEEDBACK RAPIDO |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 13 | 69,23% | +1,15% | +1,15% | -1,93% | +3,66% | FEEDBACK RAPIDO |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 10 | 80,00% | +1,68% | +1,68% | -1,90% | +3,81% | FEEDBACK RAPIDO |
| BTC | 7g | Tecnico | CALIBRABILE | 11 | 36,36% | +1,68% | -0,60% | -1,65% | +3,92% | FEEDBACK RAPIDO |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,77% | +1,77% | -0,79% | +4,24% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 9 | 66,67% | +2,24% | +1,51% | -2,09% | +4,45% | FEEDBACK RAPIDO |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 10 | 80,00% | +1,94% | +1,94% | -2,01% | +4,48% | FEEDBACK RAPIDO |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 10 | 80,00% | +1,94% | +1,94% | -2,01% | +4,48% | FEEDBACK RAPIDO |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 10 | 80,00% | +1,94% | +1,94% | -2,01% | +4,48% | FEEDBACK RAPIDO |
| BTC | 10g | Tecnico | CALIBRABILE | 9 | 33,33% | +2,10% | -0,47% | -1,87% | +4,69% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 6 | 100,00% | +2,03% | +2,03% | -2,22% | +5,58% | FEEDBACK RAPIDO |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 6 | 100,00% | +2,03% | +2,03% | -2,22% | +5,58% | FEEDBACK RAPIDO |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 6 | 100,00% | +2,03% | +2,03% | -2,22% | +5,58% | FEEDBACK RAPIDO |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 6 | 100,00% | +2,03% | +2,03% | -2,22% | +5,58% | FEEDBACK RAPIDO |
| BTC | 14g | Tecnico | CALIBRABILE | 5 | 40,00% | +1,98% | +0,05% | -2,01% | +5,75% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 18 | 50,00% | -0,06% | -0,02% | -0,48% | +0,61% | FEEDBACK RAPIDO |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 19 | 52,63% | -0,27% | +0,36% | -0,70% | +0,40% | FEEDBACK RAPIDO |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 19 | 52,63% | -0,27% | +0,36% | -0,70% | +0,40% | FEEDBACK RAPIDO |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 17 | 52,94% | -0,08% | +0,18% | -0,54% | +0,63% | FEEDBACK RAPIDO |
| DOGE | 1g | Tecnico | CALIBRABILE | 19 | 57,89% | -0,27% | +0,27% | -0,70% | +0,40% | FEEDBACK RAPIDO |
| DOGE | 1g | Classic technical | CALIBRABILE | 16 | 50,00% | +0,05% | -0,05% | -0,35% | +0,67% | FEEDBACK RAPIDO |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +3,18% | +3,18% | +1,82% | +3,24% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 18 | 50,00% | -0,26% | -0,27% | -0,92% | +0,88% | FEEDBACK RAPIDO |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 18 | 55,56% | -0,26% | +0,27% | -0,92% | +0,88% | FEEDBACK RAPIDO |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 18 | 55,56% | -0,26% | +0,27% | -0,92% | +0,88% | FEEDBACK RAPIDO |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 16 | 56,25% | -0,45% | +0,46% | -1,03% | +0,83% | FEEDBACK RAPIDO |
| DOGE | 2g | Tecnico | CALIBRABILE | 18 | 55,56% | -0,26% | +0,26% | -0,92% | +0,88% | FEEDBACK RAPIDO |
| DOGE | 2g | Classic technical | CALIBRABILE | 16 | 50,00% | +0,16% | -0,16% | -0,56% | +1,39% | FEEDBACK RAPIDO |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +5,65% | +5,65% | +4,05% | +5,83% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 17 | 47,06% | -0,33% | +0,33% | -2,07% | +2,31% | FEEDBACK RAPIDO |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 17 | 52,94% | -0,33% | +0,41% | -2,07% | +2,31% | FEEDBACK RAPIDO |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 17 | 52,94% | -0,33% | +0,41% | -2,07% | +2,31% | FEEDBACK RAPIDO |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 15 | 60,00% | -0,86% | +0,94% | -2,00% | +2,10% | FEEDBACK RAPIDO |
| DOGE | 3g | Tecnico | CALIBRABILE | 17 | 47,06% | -0,33% | +0,33% | -2,07% | +2,31% | FEEDBACK RAPIDO |
| DOGE | 3g | Classic technical | CALIBRABILE | 16 | 43,75% | -0,22% | +0,22% | -2,05% | +2,42% | FEEDBACK RAPIDO |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +3,13% | +3,13% | +0,09% | +6,33% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 15 | 66,67% | -1,01% | +1,01% | -3,50% | +2,14% | FEEDBACK RAPIDO |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 15 | 66,67% | -1,01% | +1,01% | -3,50% | +2,14% | FEEDBACK RAPIDO |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 15 | 66,67% | -1,01% | +1,01% | -3,50% | +2,14% | FEEDBACK RAPIDO |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 14 | 64,29% | -0,85% | +0,85% | -3,36% | +2,14% | FEEDBACK RAPIDO |
| DOGE | 5g | Tecnico | CALIBRABILE | 15 | 66,67% | -1,01% | +1,01% | -3,50% | +2,14% | FEEDBACK RAPIDO |
| DOGE | 5g | Classic technical | CALIBRABILE | 14 | 64,29% | -0,87% | +0,87% | -3,47% | +2,25% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 13 | 69,23% | -1,21% | +1,21% | -3,77% | +2,38% | FEEDBACK RAPIDO |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 13 | 69,23% | -1,21% | +1,21% | -3,77% | +2,38% | FEEDBACK RAPIDO |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 13 | 69,23% | -1,21% | +1,21% | -3,77% | +2,38% | FEEDBACK RAPIDO |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 13 | 69,23% | -1,21% | +1,21% | -3,77% | +2,38% | FEEDBACK RAPIDO |
| DOGE | 7g | Tecnico | CALIBRABILE | 13 | 69,23% | -1,21% | +1,21% | -3,77% | +2,38% | FEEDBACK RAPIDO |
| DOGE | 7g | Classic technical | CALIBRABILE | 12 | 66,67% | -1,23% | +1,23% | -3,76% | +2,53% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 10 | 60,00% | -1,64% | +1,64% | -4,36% | +2,50% | FEEDBACK RAPIDO |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 10 | 60,00% | -1,64% | +1,64% | -4,36% | +2,50% | FEEDBACK RAPIDO |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 10 | 60,00% | -1,64% | +1,64% | -4,36% | +2,50% | FEEDBACK RAPIDO |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 10 | 60,00% | -1,64% | +1,64% | -4,36% | +2,50% | FEEDBACK RAPIDO |
| DOGE | 10g | Tecnico | CALIBRABILE | 10 | 60,00% | -1,64% | +1,64% | -4,36% | +2,50% | FEEDBACK RAPIDO |
| DOGE | 10g | Classic technical | CALIBRABILE | 9 | 55,56% | -1,16% | +1,16% | -4,07% | +2,72% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 6 | 66,67% | -2,43% | +2,43% | -5,56% | +3,21% | FEEDBACK RAPIDO |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 6 | 66,67% | -2,43% | +2,43% | -5,56% | +3,21% | FEEDBACK RAPIDO |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 6 | 66,67% | -2,43% | +2,43% | -5,56% | +3,21% | FEEDBACK RAPIDO |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 6 | 66,67% | -2,43% | +2,43% | -5,56% | +3,21% | FEEDBACK RAPIDO |
| DOGE | 14g | Tecnico | CALIBRABILE | 6 | 66,67% | -2,43% | +2,43% | -5,56% | +3,21% | FEEDBACK RAPIDO |
| DOGE | 14g | Classic technical | CALIBRABILE | 6 | 66,67% | -2,43% | +2,43% | -5,56% | +3,21% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 14 | 42,86% | -0,19% | -0,69% | -0,54% | +0,67% | FEEDBACK RAPIDO |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 15 | 60,00% | -0,79% | -0,21% | -1,06% | -0,03% | FEEDBACK RAPIDO |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 18 | 55,56% | -0,48% | -0,36% | -0,82% | +0,29% | FEEDBACK RAPIDO |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 13 | 46,15% | -0,49% | -0,18% | -0,99% | +0,25% | FEEDBACK RAPIDO |
| SOL | 1g | Tecnico | CALIBRABILE | 19 | 57,89% | -0,30% | +0,11% | -0,66% | +0,44% | FEEDBACK RAPIDO |
| SOL | 1g | Classic technical | CALIBRABILE | 11 | 63,64% | -0,27% | +0,27% | -0,61% | +0,31% | FEEDBACK RAPIDO |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,51% | -0,51% | -0,47% | +0,31% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 14 | 21,43% | -0,41% | -1,09% | -1,02% | +0,84% | FEEDBACK RAPIDO |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 14 | 42,86% | -0,78% | -0,45% | -1,48% | +0,20% | FEEDBACK RAPIDO |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 17 | 41,18% | -0,58% | -0,43% | -1,23% | +0,65% | FEEDBACK RAPIDO |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 12 | 33,33% | -0,70% | -0,62% | -1,38% | +0,69% | FEEDBACK RAPIDO |
| SOL | 2g | Tecnico | CALIBRABILE | 18 | 38,89% | -0,42% | -0,22% | -1,02% | +0,80% | FEEDBACK RAPIDO |
| SOL | 2g | Classic technical | CALIBRABILE | 10 | 50,00% | -0,03% | +0,03% | -0,41% | +0,50% | FEEDBACK RAPIDO |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -1,38% | -1,38% | -1,57% | +0,62% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 14 | 14,29% | -0,64% | -1,49% | -2,30% | +2,00% | FEEDBACK RAPIDO |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 13 | 38,46% | -1,03% | -0,44% | -2,84% | +1,57% | FEEDBACK RAPIDO |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 16 | 37,50% | -0,78% | -0,41% | -2,53% | +1,91% | FEEDBACK RAPIDO |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 11 | 36,36% | -0,88% | -1,05% | -2,54% | +2,02% | FEEDBACK RAPIDO |
| SOL | 3g | Tecnico | CALIBRABILE | 17 | 41,18% | -0,65% | -0,06% | -2,30% | +2,01% | FEEDBACK RAPIDO |
| SOL | 3g | Classic technical | CALIBRABILE | 9 | 33,33% | +0,20% | -0,20% | -1,90% | +2,11% | FEEDBACK RAPIDO |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -3,20% | -3,20% | -3,71% | +0,62% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 14 | 35,71% | -1,05% | -1,42% | -3,34% | +2,55% | FEEDBACK RAPIDO |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 11 | 54,55% | -1,32% | -0,68% | -3,86% | +1,98% | FEEDBACK RAPIDO |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 14 | 50,00% | -0,89% | -0,68% | -3,47% | +2,39% | FEEDBACK RAPIDO |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 9 | 44,44% | -1,84% | -1,02% | -3,69% | +2,25% | FEEDBACK RAPIDO |
| SOL | 5g | Tecnico | CALIBRABILE | 15 | 46,67% | -0,99% | -0,11% | -3,42% | +2,47% | FEEDBACK RAPIDO |
| SOL | 5g | Classic technical | CALIBRABILE | 7 | 57,14% | -0,03% | +0,03% | -2,61% | +2,89% | FEEDBACK RAPIDO |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -3,99% | -3,99% | -6,07% | +0,62% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 12 | 41,67% | -0,70% | -1,35% | -3,66% | +3,12% | FEEDBACK RAPIDO |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 9 | 66,67% | -1,32% | -0,01% | -4,12% | +2,62% | FEEDBACK RAPIDO |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 12 | 66,67% | -1,02% | +0,02% | -3,76% | +2,94% | FEEDBACK RAPIDO |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 8 | 50,00% | -1,24% | -0,98% | -4,13% | +2,74% | FEEDBACK RAPIDO |
| SOL | 7g | Tecnico | CALIBRABILE | 13 | 30,77% | -0,90% | -0,67% | -3,73% | +2,99% | FEEDBACK RAPIDO |
| SOL | 7g | Classic technical | CALIBRABILE | 5 | 40,00% | +0,11% | -0,11% | -2,46% | +4,11% | FEEDBACK RAPIDO |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -6,33% | -6,33% | -6,71% | +0,62% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 9 | 33,33% | -0,47% | -0,94% | -3,90% | +3,33% | FEEDBACK RAPIDO |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 7 | 42,86% | -0,83% | -0,42% | -4,33% | +2,83% | FEEDBACK RAPIDO |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 10 | 40,00% | -0,64% | -0,23% | -4,06% | +3,15% | FEEDBACK RAPIDO |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 7 | 28,57% | -0,68% | -1,47% | -4,21% | +3,09% | FEEDBACK RAPIDO |
| SOL | 10g | Tecnico | CALIBRABILE | 10 | 50,00% | -0,64% | +0,16% | -4,06% | +3,15% | FEEDBACK RAPIDO |
| SOL | 10g | Classic technical | CALIBRABILE | 3 | 66,67% | -0,56% | +0,56% | -2,74% | +4,49% | FEEDBACK RAPIDO |
| SOL | 10g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 14g | Global confluence | BENCHMARK | 5 | 40,00% | -1,95% | -0,36% | -4,42% | +3,01% | FEEDBACK RAPIDO |
| SOL | 14g | Famiglia statistica | CALIBRABILE | 4 | 75,00% | -1,36% | +1,36% | -4,84% | +2,47% | FEEDBACK RAPIDO |
| SOL | 14g | Scanner grezzo | DIAGNOSTICO | 6 | 83,33% | -2,05% | +2,05% | -4,61% | +2,76% | FEEDBACK RAPIDO |
| SOL | 14g | Market regime grezzo | DIAGNOSTICO | 5 | 20,00% | -1,95% | -1,25% | -4,42% | +3,01% | FEEDBACK RAPIDO |
| SOL | 14g | Tecnico | CALIBRABILE | 6 | 16,67% | -2,05% | -1,33% | -4,61% | +2,76% | FEEDBACK RAPIDO |
| SOL | 14g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | FEEDBACK RAPIDO |

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

Generato: 2026-07-28 05:15 UTC

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
| BTC | 20 | FEEDBACK RAPIDO | 19 | 0 | 0 | 0 | Famiglia statistica | 1g | 42,11% | -0,05% | feedback rapido: utile da osservare, non da pesare |
| SOL | 20 | FEEDBACK RAPIDO | 19 | 0 | 0 | 0 | Tecnico | 1g | 57,89% | +0,11% | feedback rapido: utile da osservare, non da pesare |
| DOGE | 20 | FEEDBACK RAPIDO | 19 | 0 | 0 | 0 | Tecnico | 1g | 57,89% | +0,27% | feedback rapido: utile da osservare, non da pesare |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Famiglia statistica | 19 | 42,11% | -0,05% | -0,05% | -0,30% | +0,53% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Microstruttura exchange | 1 | 100,00% | +2,00% | +2,00% | +1,48% | +2,25% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 15 | 40,00% | -0,43% | +0,13% | -0,15% | +0,68% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Famiglia statistica | 18 | 44,44% | +0,15% | +0,15% | -0,35% | +1,00% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Microstruttura exchange | 1 | 100,00% | +3,18% | +3,18% | +3,05% | +3,89% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 15 | 40,00% | -0,44% | +0,29% | -0,24% | +1,10% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Famiglia statistica | 17 | 58,82% | +0,20% | +0,20% | -1,32% | +1,98% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Microstruttura exchange | 1 | 100,00% | +1,88% | +1,88% | +1,44% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 14 | 42,86% | +0,02% | +0,62% | -1,13% | +2,20% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 15 | 46,67% | +0,52% | +0,52% | -2,08% | +2,74% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -0,16% | -0,16% | -0,37% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 12 | 50,00% | -0,50% | +0,81% | -1,77% | +3,10% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 13 | 69,23% | +1,15% | +1,15% | -1,93% | +3,66% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Microstruttura exchange | 1 | 100,00% | +1,77% | +1,77% | -0,79% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 11 | 36,36% | -0,60% | +1,68% | -1,65% | +3,92% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 10 | 80,00% | +1,94% | +1,94% | -2,01% | +4,48% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 9 | 33,33% | -0,47% | +2,10% | -1,87% | +4,69% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Famiglia statistica | 6 | 100,00% | +2,03% | +2,03% | -2,22% | +5,58% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 5 | 40,00% | +0,05% | +1,98% | -2,01% | +5,75% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 16 | 50,00% | -0,05% | +0,05% | -0,35% | +0,67% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Famiglia statistica | 19 | 52,63% | +0,36% | -0,27% | -0,70% | +0,40% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Microstruttura exchange | 2 | 100,00% | +3,18% | +3,18% | +1,82% | +3,24% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 19 | 57,89% | +0,27% | -0,27% | -0,70% | +0,40% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Classic technical | 16 | 50,00% | -0,16% | +0,16% | -0,56% | +1,39% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Famiglia statistica | 18 | 55,56% | +0,27% | -0,26% | -0,92% | +0,88% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Microstruttura exchange | 2 | 100,00% | +5,65% | +5,65% | +4,05% | +5,83% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 18 | 55,56% | +0,26% | -0,26% | -0,92% | +0,88% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Classic technical | 16 | 43,75% | +0,22% | -0,22% | -2,05% | +2,42% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Famiglia statistica | 17 | 52,94% | +0,41% | -0,33% | -2,07% | +2,31% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Microstruttura exchange | 2 | 100,00% | +3,13% | +3,13% | +0,09% | +6,33% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 17 | 47,06% | +0,33% | -0,33% | -2,07% | +2,31% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Classic technical | 14 | 64,29% | +0,87% | -0,87% | -3,47% | +2,25% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 15 | 66,67% | +1,01% | -1,01% | -3,50% | +2,14% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 15 | 66,67% | +1,01% | -1,01% | -3,50% | +2,14% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Classic technical | 12 | 66,67% | +1,23% | -1,23% | -3,76% | +2,53% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 13 | 69,23% | +1,21% | -1,21% | -3,77% | +2,38% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 13 | 69,23% | +1,21% | -1,21% | -3,77% | +2,38% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Classic technical | 9 | 55,56% | +1,16% | -1,16% | -4,07% | +2,72% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 10 | 60,00% | +1,64% | -1,64% | -4,36% | +2,50% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 10 | 60,00% | +1,64% | -1,64% | -4,36% | +2,50% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Classic technical | 6 | 66,67% | +2,43% | -2,43% | -5,56% | +3,21% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Famiglia statistica | 6 | 66,67% | +2,43% | -2,43% | -5,56% | +3,21% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 6 | 66,67% | +2,43% | -2,43% | -5,56% | +3,21% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Classic technical | 11 | 63,64% | +0,27% | -0,27% | -0,61% | +0,31% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Famiglia statistica | 15 | 60,00% | -0,21% | -0,79% | -1,06% | -0,03% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 1 | 0,00% | -0,51% | -0,51% | -0,47% | +0,31% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 19 | 57,89% | +0,11% | -0,30% | -0,66% | +0,44% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Classic technical | 10 | 50,00% | +0,03% | -0,03% | -0,41% | +0,50% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Famiglia statistica | 14 | 42,86% | -0,45% | -0,78% | -1,48% | +0,20% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Microstruttura exchange | 1 | 0,00% | -1,38% | -1,38% | -1,57% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 18 | 38,89% | -0,22% | -0,42% | -1,02% | +0,80% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Classic technical | 9 | 33,33% | -0,20% | +0,20% | -1,90% | +2,11% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Famiglia statistica | 13 | 38,46% | -0,44% | -1,03% | -2,84% | +1,57% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Microstruttura exchange | 1 | 0,00% | -3,20% | -3,20% | -3,71% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 17 | 41,18% | -0,06% | -0,65% | -2,30% | +2,01% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Classic technical | 7 | 57,14% | +0,03% | -0,03% | -2,61% | +2,89% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 11 | 54,55% | -0,68% | -1,32% | -3,86% | +1,98% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -3,99% | -3,99% | -6,07% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 15 | 46,67% | -0,11% | -0,99% | -3,42% | +2,47% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Classic technical | 5 | 40,00% | -0,11% | +0,11% | -2,46% | +4,11% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 9 | 66,67% | -0,01% | -1,32% | -4,12% | +2,62% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -6,33% | -6,33% | -6,71% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 13 | 30,77% | -0,67% | -0,90% | -3,73% | +2,99% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Classic technical | 3 | 66,67% | +0,56% | -0,56% | -2,74% | +4,49% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 7 | 42,86% | -0,42% | -0,83% | -4,33% | +2,83% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 10 | 50,00% | +0,16% | -0,64% | -4,06% | +3,15% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Famiglia statistica | 4 | 75,00% | +1,36% | -1,36% | -4,84% | +2,47% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Frattale SOL | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Tecnico | 6 | 16,67% | -1,33% | -2,05% | -4,61% | +2,76% | OSSERVA | 0,0 | BASSA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 18 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 17 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 19 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Famiglia statistica | 54 | 48,15% | +0,10% |
| BTC | BREVE | Microstruttura exchange | 3 | 100,00% | +2,36% |
| BTC | BREVE | Tecnico | 44 | 40,91% | -0,29% |
| BTC | SETTIMANALE | Famiglia statistica | 38 | 63,16% | +1,11% |
| BTC | SETTIMANALE | Microstruttura exchange | 2 | 50,00% | +0,81% |
| BTC | SETTIMANALE | Tecnico | 32 | 40,62% | -0,53% |
| BTC | SWING | Famiglia statistica | 6 | 100,00% | +2,03% |
| BTC | SWING | Tecnico | 5 | 40,00% | +0,05% |
| DOGE | BREVE | Classic technical | 48 | 47,92% | +0,00% |
| DOGE | BREVE | Famiglia statistica | 54 | 53,70% | +0,35% |
| DOGE | BREVE | Microstruttura exchange | 6 | 100,00% | +3,99% |
| DOGE | BREVE | Tecnico | 54 | 53,70% | +0,28% |
| DOGE | SETTIMANALE | Classic technical | 35 | 62,86% | +1,07% |
| DOGE | SETTIMANALE | Famiglia statistica | 38 | 65,79% | +1,24% |
| DOGE | SETTIMANALE | Tecnico | 38 | 65,79% | +1,24% |
| DOGE | SWING | Classic technical | 6 | 66,67% | +2,43% |
| DOGE | SWING | Famiglia statistica | 6 | 66,67% | +2,43% |
| DOGE | SWING | Tecnico | 6 | 66,67% | +2,43% |
| SOL | BREVE | Classic technical | 30 | 50,00% | +0,05% |
| SOL | BREVE | Famiglia statistica | 42 | 47,62% | -0,36% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 3 | 0,00% | -1,70% |
| SOL | BREVE | Tecnico | 54 | 46,30% | -0,05% |
| SOL | SETTIMANALE | Classic technical | 15 | 53,33% | +0,09% |
| SOL | SETTIMANALE | Famiglia statistica | 27 | 55,56% | -0,39% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Microstruttura exchange | 2 | 0,00% | -5,16% |
| SOL | SETTIMANALE | Tecnico | 38 | 42,11% | -0,23% |
| SOL | SWING | Famiglia statistica | 4 | 75,00% | +1,36% |
| SOL | SWING | Frattale SOL | 1 | 0,00% | -1,13% |
| SOL | SWING | Tecnico | 6 | 16,67% | -1,33% |

## Aree ancora in attesa

| Asset | Famiglia | Righe senza controlli | Stato |
| --- | --- | --- | --- |
| BTC | BREVE | 6 | in attesa di controlli maturati |
| BTC | SETTIMANALE | 7 | in attesa di controlli maturati |
| BTC | SWING | 8 | in attesa di controlli maturati |
| BTC | MEDIO | 15 | in attesa di controlli maturati |
| SOL | SETTIMANALE | 1 | in attesa di controlli maturati |
| SOL | SWING | 7 | in attesa di controlli maturati |
| SOL | MEDIO | 15 | in attesa di controlli maturati |
| DOGE | BREVE | 3 | in attesa di controlli maturati |
| DOGE | SETTIMANALE | 6 | in attesa di controlli maturati |
| DOGE | SWING | 7 | in attesa di controlli maturati |
| DOGE | MEDIO | 15 | in attesa di controlli maturati |

## Come leggere le raccomandazioni

- **OSSERVA**: meno di 30 controlli, nessuna modifica.
- **PESO OK / MANTIENI**: il modulo sta aiutando, ma non serve cambiare peso.
- **NON AUMENTARE**: il modulo non dimostra ancora un vantaggio sufficiente.
- **POSSIBILE AUMENTO LEGGERO**: proposta prudente, mai automatica.
- **POSSIBILE RIDUZIONE**: modulo debole con campione già abbastanza maturo.
- **ESCLUSO**: benchmark o diagnostica già inclusa in un'altra famiglia.

Nota decisiva: **non sommare mai una modifica alla Famiglia statistica e altre modifiche separate a Scanner o Market Regime**. Scanner e Market servono soltanto a capire quale parte della famiglia sta funzionando o fallendo.

## Stato attuale

Siamo ancora in feedback rapido. Non bisogna modificare i pesi del Global. La nuova struttura serve ad accumulare dati corretti senza doppio conteggio.
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

| Asset   |   Snapshot |   Controlli 30g |   In attesa | Stato         | DD normale hit   | DD brutto hit   | DD molto brutto hit   | Bias rischio   |
|:--------|-----------:|----------------:|------------:|:--------------|:-----------------|:----------------|:----------------------|:---------------|
| BTC     |         20 |               0 |          20 | RACCOLTA DATI | n/a              | n/a             | n/a                   | n/a            |
| SOL     |         20 |               0 |          20 | RACCOLTA DATI | n/a              | n/a             | n/a                   | n/a            |
| DOGE    |         20 |               0 |          20 | RACCOLTA DATI | n/a              | n/a             | n/a                   | n/a            |

Regola: sotto 60 controlli osserva soltanto; da 100+ controlli può diventare utile per correggere rischio spot/leva nel Decision Report.

## Ultima lettura rapida

| Asset   | Rischio spot   | Rischio leva   | Nota leva                                                               |
|:--------|:---------------|:---------------|:------------------------------------------------------------------------|
| BTC     | MEDIO          | MOLTO ALTO     | spot preferibile; leva molto pericolosa anche 2x/3x senza margine largo |
| SOL     | BASSO          | ALTO           | leva da limitare; 2x/3x solo con invalidazione chiara                   |
| DOGE    | MEDIO          | MOLTO ALTO     | leva da limitare; 2x/3x solo con invalidazione chiara                   |
<!-- RISK_CALIBRATION_END -->

</details>
<!-- COMPACT_SECTION_END:risk_calibration -->

<!-- COMPACT_SECTION_START:global_confluence -->
<details open>
<summary><strong>🌐 Global Confluence — quadro finale</strong></summary>

<!-- GLOBAL_CONFLUENCE_START -->
# Sintesi finale di confluenza

Generato: 2026-07-28 05:15 UTC


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
| BTC | -1 | DEBOLE / FRAGILE | Fragile | BASSA / RACCOLTA DATI | NON INSEGUIRE / RIDUCI RISCHIO | Prima resistenza sopra 66.910; conferma del doppio minimo sopra 67.248. | Sotto 57.748 il quadro tecnico peggiora. |
| SOL | +1 | MISTA / PARZIALE | Neutrale / misto | BASSA / RACCOLTA DATI | HOLD LEGGERO / ATTESA CONFERME | conferma del doppio minimo sopra 75,94; nuova conferma tecnica sopra 78,73; milestone analogiche 89,78 / 96,42, valide soltanto se rientra anche il gap frattale. | Allarmi sotto 69,65 / 64,42 / 62,19. |
| DOGE | +1 | MISTA / PARZIALE | Neutrale / misto | BASSA / RACCOLTA DATI | STAI ALLA FINESTRA | Sopra 0.07923 migliora; sopra 0.07966 viene invalidato il pattern ribassista dominante. | Sotto 0.06961 il rischio ribassista aumenta. |

## Punteggi per modulo

| Asset | Scanner grezzo | Market grezzo | Famiglia statistica | Scanner path | Tecnico | Classic tech | Frattale SOL | Fractal path | RSI top-cycle | Lifecycle EMA | Exchange flow | Futures | Daily change | Totale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +2 | +2 | +3 | 0 | -2 | -1 | 0 | 0 | 0 | 0 | 0 | 0 | -1 | -1 |
| SOL | +3 | +3 | +4 | 0 | -3 | -1 | 0 | 0 | 0 | 0 | 0 | 0 | +1 | +1 |
| DOGE | +3 | +2 | +4 | 0 | -3 | -1 | 0 | 0 | 0 | 0 | 0 | 0 | +1 | +1 |

Le colonne **Scanner grezzo** e **Market grezzo** sono diagnostiche: nel totale entra soltanto la colonna **Famiglia statistica**.

## Lettura asset per asset

### BTC

- Confluenza: **DEBOLE / FRAGILE**
- Bias: **Fragile**
- Punteggio finale: **-1**
- Affidabilità: **BASSA / RACCOLTA DATI**
- Azione coerente: **NON INSEGUIRE / RIDUCI RISCHIO**

BTC si è indebolito. In questo caso conta più proteggere il rischio che inseguire un recupero non confermato.

Dettaglio moduli:

- Famiglia statistica: **+3** — Scanner grezzo +2, Market Regime grezzo +2, match regime 14. Scanner e regime concordi con almeno 10 match: bonus massimo di 1 punto. Punteggio contato nel Global: +3.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **+2** — Casi positivi 62,50%, return centrale 30g +7,47%. Direzione scanner: SALITA. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **+2** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 14, positivi 30g 71,43%, return p50 +6,67%.
- Scanner path: **0** — Controlli disponibili 18. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **-2** — Score tecnico -3/12, verdetto debole, trend ribassista, struttura volatilità in espansione, divergenza rialzista rsi, Wyckoff possibile accumulazione, pattern score 0 (rialzista Doppio minimo / CANDIDATO; ribassista Doppio massimo / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **-1** — Score classico -6/12, verdetto RIBASSISTA / FRAGILE, stage STAGE 4 / MARKDOWN, struttura MASSIMI E MINIMI CRESCENTI, Wyckoff ACCUMULO POSSIBILE / RANGE BASSO, volatilità locale BASSO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Non applicabile a questo asset.
- Fractal path: **0** — Non applicabile a questo asset.
- RSI top-cycle: **0** — Non applicabile a questo asset.
- Lifecycle EMA: **0** — Non applicabile a questo asset.
- Exchange flow: **0** — Flow +1.75, derivati +0.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +0.75; exchange 3/3, copertura 100%, consenso bull 2, bear 0, divergenze 0, campioni 4h 9 su 4.00h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias LEGGERMENTE POSITIVA / NON PESATA; confidenza MEDIA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Misto, forza 1/5.
- Daily change: **-1** — BTC: cambiamento forte in peggioramento rispetto a ieri.

Conferme: Prima resistenza sopra 66.910; conferma del doppio minimo sopra 67.248.

Invalidazioni: Sotto 57.748 il quadro tecnico peggiora.

### SOL

- Confluenza: **MISTA / PARZIALE**
- Bias: **Neutrale / misto**
- Punteggio finale: **+1**
- Affidabilità: **BASSA / RACCOLTA DATI**
- Azione coerente: **HOLD LEGGERO / ATTESA CONFERME**

SOL è ancora in zona mista. Il frattale resta soltanto uno scenario contestuale: non è confermato dal prezzo e vale 0 punti operativi finché il gap non rientra. Meglio evitare leva e ragionare solo a tranche piccole.

Dettaglio moduli:

- Famiglia statistica: **+4** — Scanner grezzo +3, Market Regime grezzo +3, match regime 18. Scanner e regime concordi con almeno 10 match: bonus massimo di 1 punto. Punteggio contato nel Global: +4.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **+3** — Casi positivi 70,00%, return centrale 30g +7,64%. Direzione scanner: SALITA. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **+3** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 18, positivi 30g 88,89%, return p50 +9,45%.
- Scanner path: **0** — Controlli disponibili 18. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **-3** — Score tecnico -7/12, verdetto ribassista tecnico, trend ribassista, struttura compressione / triangolo, divergenza ribassista nascosta rsi, Wyckoff possibile accumulazione, pattern score +1 (rialzista Doppio minimo / MATURO; ribassista Doppio massimo / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **-1** — Score classico -12/12, verdetto RIBASSISTA / FRAGILE, stage STAGE 4 / MARKDOWN, struttura MASSIMI E MINIMI DECRESCENTI, Wyckoff MARKDOWN / DEBOLEZZA, volatilità locale BASSO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Verdetto ANALOGIA DEBOLE / SCENARIO SECONDARIO, somiglianza strutturale +64,21%, aderenza live +67,56%, errore live +16,22%, gap corrente -1,41%, peso operativo 0, tracking STRUTTURA STABILE, fase FRATTALE SOLO DI CONTESTO, rischio ALTO.
- Fractal path: **0** — Controlli disponibili 14, ma percorso ancorato non aderente: gap -1,41%, errore live +16,22%. Peso 0.
- RSI top-cycle: **0** — Rischio top-cycle RSI: BASSO.
- Lifecycle EMA: **0** — Contesto non pesato nel Global. Lifecycle score 4, bias SQUEEZE SETUP MODERATO, EMA200 112,37 $, upside EMA200 +53,41%, gap EMA50/EMA200 -3,95%, hit EMA200 12w +16,67%, trend STABILE / DA CONFERMARE. Peso Global forzato a 0.
- Exchange flow: **0** — Flow +1.75, derivati +0.50, affollamento +0.00, liquidazioni +0.00, conferme tecniche +1.25; exchange 3/3, copertura 100%, consenso bull 0, bear 2, divergenze 0, campioni 4h 9 su 4.00h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias LEGGERMENTE POSITIVA / NON PESATA; confidenza MEDIA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Misto, forza 2/5.
- Daily change: **+1** — SOL: cambiamento medio in miglioramento rispetto a ieri.

Conferme: conferma del doppio minimo sopra 75,94; nuova conferma tecnica sopra 78,73; milestone analogiche 89,78 / 96,42, valide soltanto se rientra anche il gap frattale.

Invalidazioni: Allarmi sotto 69,65 / 64,42 / 62,19.

### DOGE

- Confluenza: **MISTA / PARZIALE**
- Bias: **Neutrale / misto**
- Punteggio finale: **+1**
- Affidabilità: **BASSA / RACCOLTA DATI**
- Azione coerente: **STAI ALLA FINESTRA**

DOGE non ha ancora una confluenza pulita. Serve conferma tecnica prima di trattarlo come asset forte.

Dettaglio moduli:

- Famiglia statistica: **+4** — Scanner grezzo +3, Market Regime grezzo +2, match regime 21. Scanner e regime concordi con almeno 10 match: bonus massimo di 1 punto. Punteggio contato nel Global: +4.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **+3** — Casi positivi 67,50%, return centrale 30g +6,65%. Direzione scanner: SALITA. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **+2** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 21, positivi 30g 76,19%, return p50 +6,81%.
- Scanner path: **0** — Controlli disponibili 18. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **-3** — Score tecnico -9/12, verdetto ribassista tecnico, trend ribassista, struttura ribassista con massimi e minimi decrescenti, divergenza ribassista nascosta rsi, Wyckoff possibile accumulazione, pattern score -1 (rialzista Doppio minimo / CANDIDATO; ribassista Triplo massimo / MATURO). Fonte: technical_structure_metrics.csv.
- Classic technical: **-1** — Score classico -7/12, verdetto RIBASSISTA / FRAGILE, stage STAGE 4 / MARKDOWN, struttura MASSIMI E MINIMI DECRESCENTI, Wyckoff MARKDOWN / DEBOLEZZA, volatilità locale BASSO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Non applicabile a questo asset.
- Fractal path: **0** — Non applicabile a questo asset.
- RSI top-cycle: **0** — Non applicabile a questo asset.
- Lifecycle EMA: **0** — Non applicabile a questo asset.
- Exchange flow: **0** — Flow +0.75, derivati +0.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +0.00; exchange 3/3, copertura 100%, consenso bull 1, bear 1, divergenze 1, campioni 4h 9 su 4.00h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias MISTA / NEUTRALE; confidenza BASSA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Misto, forza 1/5.
- Daily change: **+1** — DOGE: cambiamento medio in miglioramento rispetto a ieri.

Conferme: Sopra 0.07923 migliora; sopra 0.07966 viene invalidato il pattern ribassista dominante.

Invalidazioni: Sotto 0.06961 il rischio ribassista aumenta.


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

Generato: 2026-07-28 05:15 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [btc_macro_cycle_report.md](btc_macro_cycle_report.md)

Questo modulo descrive il contesto macro di Bitcoin. Non genera entrate tattiche, non autorizza leva e pesa **0** nel Global Confluence.

## Sintesi

| Voce | Valore | Lettura |
| --- | --- | --- |
| Prezzo BTC | 63.381 $ | prezzo corrente |
| Power Law centrale | 122.930 $ | deviazione -48,44% |
| Banda p10-p90 | 76.417 $ / 308.540 $ | SOTTO LA BANDA P10 |
| Percentile residuo | 0,76% | posizione storica nel corridoio |
| Esponente β | 5,8349 | R² log-log 91,97% |
| Stabilità β | BASSA | range 1,3092 cambiando finestra |
| Ultimo halving | 2024-04-19 | 830 giorni fa |
| Fase ciclo | 56,81% | percentuale indicativa del ciclo quadriennale |
| Peso Global | 0 | CONTESTO MACRO / DIAGNOSTICO |

La Power Law viene trattata come regressione empirica, non come legge fisica. Il report mostra quanto cambia l'esponente usando finestre iniziali diverse e la confronta con il benchmark ingenuo 'prezzo invariato'.

## Bitcoin Power Law

- Campione: 2014-09-17 → 2026-07-28 (4332 osservazioni)
- Formula stimata: prezzo ≈ exp(-39.3114) × giorni^5.8349
- Prezzo centrale oggi: **122.930 $**
- Posizione corrente: **SOTTO LA BANDA P10**, percentile 0,76%
- Scarto dal centro: **-48,44%**

![Bitcoin Power Law](btc_power_law_chart.png)

![Bitcoin Power Law log-log](btc_power_law_loglog_chart.png)

### Stabilità dell'esponente

| Inizio campione | β | R² log-log |
| --- | --- | --- |
| 2014 | 5,8349 | 91,97% |
| 2015 | 5,9208 | 91,54% |
| 2016 | 5,6095 | 87,78% |
| 2017 | 4,8793 | 82,88% |
| 2018 | 4,6116 | 78,35% |

### Backtest walk-forward contro prezzo invariato

| Orizzonte | Controlli | Vittorie vs naive | Errore mediano modello | Errore mediano naive |
| --- | --- | --- | --- | --- |
| 90g | 79 | 26,58% | 55,14% | 20,89% |
| 180g | 79 | 40,51% | 60,84% | 45,16% |
| 365g | 79 | 56,96% | 73,12% | 81,57% |
| 730g | 79 | 59,49% | 72,50% | 109,89% |

## Bitcoin Four-Year Spiral

Nel grafico l'angolo rappresenta il tempo dentro una finestra di quattro anni e il raggio rappresenta il prezzo in scala logaritmica. ATH, bottom storici e halving sono marker descrittivi: la spirale rende visibili le ricorrenze, ma non dimostra che il ciclo futuro debba ripetersi.

![Bitcoin Four-Year Spiral](bitcoin_four_year_spiral.png)

## Stessa fase dei cicli halving precedenti

| Ciclo | Data analoga | +30g | +90g | +180g | +365g |
| --- | --- | --- | --- | --- | --- |
| 2012-11-28 → 2016-07-09 | 2014-12-17 | -34,92% | -10,72% | -25,94% | +42,62% |
| 2016-07-09 → 2020-05-11 | 2018-09-13 | -3,55% | -46,50% | -40,02% | +58,97% |
| 2020-05-11 → 2024-04-19 | 2022-08-07 | -18,72% | -8,17% | +1,18% | +25,91% |

Campione molto piccolo: questi rendimenti sono contesto di ciclo, non probabilità affidabili.

## SOL/BTC e DOGE/BTC dentro il tempo Bitcoin

![Altcoin nel ciclo BTC](alt_btc_cycle_spirals.png)

| Asset | Coppia | Forza vs BTC | Score raw | Candidato | 30g | Peso Global |
| --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | SOTTOPERFORMA BTC | -5 | -1 | -1.6170237050330938 | 0 |
| DOGE | DOGE/BTC | SOTTOPERFORMA BTC | -6 | -1 | -11.134134025142838 | 0 |

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

Generato: 2026-07-28 05:14 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [relative_strength_btc_report.md](relative_strength_btc_report.md)

Questo modulo controlla se SOL e DOGE stanno davvero battendo Bitcoin. Una salita in USD accompagnata da una coppia ALT/BTC ribassista è spesso soltanto trascinamento di BTC.

**Protezione iniziale:** il candidato relativo è limitato a -1/0/+1, ma il peso nel Global resta **0**. La coppia BTC conferma o indebolisce il tecnico USD; non viene sommata come secondo modulo indipendente.

## Sintesi

| Asset | Coppia | Prezzo | Score raw | Candidato | Peso Global | Forza vs BTC | Confidenza | 30g | Tecnico USD | Lettura combinata |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | 0.00115600 | -5 | -1 | 0 | SOTTOPERFORMA BTC | MEDIA | -1,62% | RIBASSISTA | DEBOLEZZA COMPLETA: scende in USD e contro BTC |
| DOGE | DOGE/BTC | 0.00000110 | -6 | -1 | 0 | SOTTOPERFORMA BTC | MEDIA | -11,13% | RIBASSISTA | DEBOLEZZA COMPLETA: scende in USD e contro BTC |

## Matrice di lettura

| ALT/USD | ALT/BTC | Interpretazione |
| --- | --- | --- |
| Rialzista | Rialzista | Conferma migliore: sale e batte BTC |
| Rialzista | Ribassista | Sale soprattutto perché BTC trascina il mercato |
| Ribassista | Rialzista | Forza relativa nascosta / possibile rotazione futura |
| Ribassista | Ribassista | Debolezza completa |

## SOL/BTC

- **Verdetto relativo:** SOTTOPERFORMA BTC (-5)
- **Candidato futuro:** -1; **peso attuale Global: 0**
- **Lettura combinata USD/BTC:** DEBOLEZZA COMPLETA: scende in USD e contro BTC
- **Struttura:** COMPRESSIONE / TRIANGOLO POSSIBILE
- **Rendimenti relativi:** 7g -3,10%; 30g -1,62%; 90g +5,00%; 180g -17,61%
- **Daily:** RSI 41.54; MA50 0.00117178; MA200 0.00121138
- **Weekly:** MA30 0.00120990; RSI 44.25
- **Livelli:** supporto 0.00114300; resistenza 0.00116300; breakout 60g 0.00134900; breakdown 60g 0.00100900
- **Pattern:** DOPPIO MINIMO / TARGET RAGGIUNTO; neckline 0.00113200; target 0.00117200
- **Fibonacci:** VICINO — 61.8% a 0.00113888
- **Fonte:** Yahoo Finance SOL-BTC (coppia diretta)
- **Motivi score:** prezzo sotto MA50 daily; prezzo sotto MA200 daily; MA50 daily in salita; prezzo sotto MA30 weekly; MA30 weekly in discesa; RSI relativo debole; MACD relativo negativo

![Grafico SOL/BTC](relative_strength_SOLBTC.png)

## DOGE/BTC

- **Verdetto relativo:** SOTTOPERFORMA BTC (-6)
- **Candidato futuro:** -1; **peso attuale Global: 0**
- **Lettura combinata USD/BTC:** DEBOLEZZA COMPLETA: scende in USD e contro BTC
- **Struttura:** MASSIMI E MINIMI DECRESCENTI
- **Rendimenti relativi:** 7g -0,22%; 30g -11,13%; 90g -15,22%; 180g -21,19%
- **Daily:** RSI 37.07; MA50 0.00000122; MA200 0.00000133
- **Weekly:** MA30 0.00000132; RSI 30.59
- **Livelli:** supporto 0.00000110; resistenza 0.00000121; breakout 60g 0.00000153; breakdown 60g 0.00000104
- **Pattern:** DOPPIO MASSIMO / CONFERMATO; neckline 0.00000112; target 0.00000099
- **Fibonacci:** NON ATTIVO — 23.6% a 0.00000115
- **Fonte:** Rapporto sintetico DOGE-USD / BTC-USD (sintetica)
- **Motivi score:** prezzo sotto MA50 daily; prezzo sotto MA200 daily; MA50 daily in discesa; prezzo sotto MA30 weekly; MA30 weekly in discesa; struttura con massimi/minimi decrescenti; RSI relativo debole; MACD relativo positivo

![Grafico DOGE/BTC](relative_strength_DOGEBTC.png)

## Backtest storico diagnostico

Il backtest usa soltanto indicatori disponibili alla data del segnale e campiona una volta a settimana. È utile subito, ma non sostituisce il tracker live: le soglie sono state definite prima di vedere il risultato.

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto direzione | Return futuro mediano |
| --- | --- | --- | --- | --- | --- |
| SOL | 7g | 202 | 51,98% | +1,96% | -1,34% |
| SOL | 30g | 201 | 47,76% | +4,73% | +0,36% |
| SOL | 90g | 195 | 53,85% | +10,36% | +1,62% |
| DOGE | 7g | 291 | 56,01% | +1,87% | -1,77% |
| DOGE | 30g | 288 | 52,78% | +2,01% | -3,71% |
| DOGE | 90g | 285 | 54,04% | +6,94% | -8,47% |

## Tracker live e gate futuro

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto | Stato | Peso Global |
| --- | --- | --- | --- | --- | --- | --- |
| SOL | 1g | 3 | 66,67% | -0,12% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 3g | 2 | 100,00% | +0,16% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 7g | 0 | n/a | n/a | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 14g | 0 | n/a | n/a | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 30g | 0 | n/a | n/a | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 1g | 17 | 82,35% | +0,66% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 3g | 15 | 66,67% | +0,98% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 7g | 11 | 90,91% | +3,01% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 14g | 4 | 100,00% | +3,69% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 30g | 0 | n/a | n/a | LOCKED / RACCOLTA LIVE | 0 |

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

Ultima candela SOL usata: **28 luglio 2026**

## Verdetto: ANALOGIA DEBOLE / SCENARIO SECONDARIO

- **Fase attuale:** FRATTALE SOLO DI CONTESTO
- **Somiglianza totale:** +64,21%
- **Somiglianza strutturale:** +64,21%
- **Aderenza prezzo live:** +67,56%
- **Errore medio live:** +16,22%
- **Gap prezzo corrente:** -1,41%
- **Peso operativo suggerito:** 0
- **Affidabilita:** BASSA
- **Rischio fase:** ALTO
- **Trend tracking:** STRUTTURA STABILE
- **Sintesi:** Esistono alcuni elementi comuni, ma non abbastanza per una conferma.
- **SOL è al giorno:** 52 dal bottom usato.
- **Giorno BTC equivalente:** 2023-01-12
- **Prossimo step:** Proiezione condizionale, non conferma operativa: **Spinta rialzista abbastanza pulita.** Zona bassa **73,28 $** intorno al **28 luglio 2026**; zona alta **89,78 $** intorno al **10 agosto 2026**; fine step circa **89,45 $** entro il **11 agosto 2026**.

## Somiglianza prima e dopo inizio programma

Questa sezione separa la somiglianza della forma dall'aderenza reale del prezzo.

- **Inizio programma/scanner:** 3 luglio 2026
- **Prima del programma** = backtest retroattivo.
- **Da inizio programma** = verifica live: è la parte più importante per l'uso operativo.

| Periodo | Date | Giorni | Aderenza prezzo | Errore medio | Gap ultimo | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| Prima del programma | 6 giugno 2026 -> 2 luglio 2026 | 27 | +87,95% | +6,02% | +21,89% | ABBASTANZA ALLINEATO |
| Da inizio programma | 3 luglio 2026 -> 28 luglio 2026 | 26 | +67,56% | +16,22% | -1,41% | STACCATO / NON ADERENTE |
| Totale dal bottom | 6 giugno 2026 -> 28 luglio 2026 | 53 | +77,95% | +11,03% | -1,41% | DEVIAZIONE MODERATA |

Nota: un frattale può avere una forma simile ma un prezzo distante. In quel caso non è operativo finché il gap non rientra.

## Lettura operativa veloce

Il frattale non deve generare acquisti o leva adesso. La forma è un contesto, ma l'aderenza live del prezzo è insufficiente.

| Voce | Risposta | Perché |
| --- | --- | --- |
| Uso operativo | NO | Il frattale vale 0 punti operativi finché il prezzo resta non aderente. |
| Aderenza live | +67,56% | Errore medio live +16,22%. |
| Gap corrente | -1,41% | Deve rientrare circa entro ±12%. |
| Prima conferma prezzo | 89,78 $ | Serve anche miglioramento del gap, non solo una candela sopra il livello. |
| Seconda conferma | 96,42 $ | Rende più credibile il percorso, ma non sostituisce l'aderenza. |
| Invalidazione soft | 69,65 $ | Sotto questa zona il quadro peggiora. |
| Invalidazione forte | 62,19 $ | Sotto il bottom il paragone è quasi rotto. |

## Target ciclo fino al top BTC 2025

| Voce | Valore |
| --- | --- |
| Stato | CONTESTO / NON OPERATIVO |
| Top BTC 2025 | 6 ottobre 2025 - 124.753 $ |
| Data SOL equivalente | 21 aprile 2029 |
| Target ciclo base da oggi | 484,48 $ |
| Massimo percorso base | 484,48 $ (21 aprile 2029) |

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
| Prima conferma | 89,78 $ | Deve accompagnarsi al rientro del gap. |
| Seconda conferma | 96,42 $ | Scenario più credibile. |
| Invalidazione soft | 69,65 $ | Il frattale si indebolisce. |
| Invalidazione forte | 62,19 $ | Il paragone si rompe. |

## Proiezione veloce con date SOL

| Orizzonte | Data SOL | BTC fece | SOL base | Min percorso | Max percorso |
| --- | --- | --- | --- | --- | --- |
| 7 giorni | 4 agosto 2026 | +11,75% | 81,89 $ | 73,28 $ | 82,21 $ |
| 14 giorni | 11 agosto 2026 | +22,06% | 89,45 $ | 73,28 $ | 89,78 $ |
| 30 giorni | 27 agosto 2026 | +15,91% | 84,94 $ | 73,28 $ | 92,33 $ |
| 60 giorni | 26 settembre 2026 | +28,24% | 93,97 $ | 73,28 $ | 96,42 $ |
| 90 giorni | 26 ottobre 2026 | +59,72% | 117,04 $ | 73,28 $ | 117,42 $ |
| 120 giorni | 25 novembre 2026 | +42,05% | 104,10 $ | 73,28 $ | 118,39 $ |

## Prossimi step se SOL segue BTC 2022

| Step | Date SOL | BTC fine | SOL zona bassa | SOL zona alta | SOL fine base | Lettura |
| --- | --- | --- | --- | --- | --- | --- |
| Step 1 - prossime 2 settimane | 28 luglio 2026 -> 11 agosto 2026 | +22,06% | 73,28 $ (28 luglio 2026) | 89,78 $ (10 agosto 2026) | 89,45 $ | Spinta rialzista abbastanza pulita. |
| Step 2 - primo mese | 12 agosto 2026 -> 27 agosto 2026 | +15,91% | 84,08 $ (26 agosto 2026) | 92,33 $ (14 agosto 2026) | 84,94 $ | Spinta rialzista abbastanza pulita. |
| Step 3 - secondo mese | 28 agosto 2026 -> 26 settembre 2026 | +28,24% | 78,40 $ (23 settembre 2026) | 96,42 $ (5 settembre 2026) | 93,97 $ | Spinta rialzista abbastanza pulita. |
| Step 4 - terzo mese | 27 settembre 2026 -> 26 ottobre 2026 | +59,72% | 94,66 $ (28 settembre 2026) | 117,42 $ (25 ottobre 2026) | 117,04 $ | Spinta rialzista abbastanza pulita. |

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
| Prezzo SOL | 73,28 $ |  |
| Weekly RSI | 38,27 / linea grezza 53,65 | LINEA NON AFFIDABILE / RISCHIO NON ATTIVO — IRREALISTICA / NON OPERATIVA |
| Monthly RSI | 40,34 / linea grezza 56,16 | RSI TROPPO BASSO PER RISCHIO TOP — VALIDA / USO PRUDENTE |
| Target ciclo base | 484,48 $ | Avanzamento +15,13% |
| Rischio top-cycle RSI | BASSO | Nessun segnale top-cycle macro attivo. Prezzo ancora lontano dal target ciclo; il filtro RSI resta solo di monitoraggio. |

## Lettura semplice

- Weekly: La top-line weekly non supera i controlli di qualità. Non viene usata per generare rischio top-cycle.
- Monthly: RSI monthly è 40,3, sotto la soglia prudente 55. Anche se fosse vicino alla linea, non è una vera zona di esaurimento ciclo.
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
| Prezzo SOL | 73,28 $ |
| TVL Solana | 4,78 mld $ |
| TVL 7g | -3,65% |
| DEX volume 24h | 1,77 mld $ |
| Fees 24h | 8,39 mln $ |
| Stablecoin su Solana | 17,20 mld $ |
| Stake ratio | 67,93% |
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
| Confronto precedente | 2026-07-27 |
| Fonte prezzi | Yahoo Finance SOL-USD weekly |
| Prezzo SOL | 73,28 $ |
| EMA200 weekly target | 112,37 $ |
| Upside verso EMA200 | +53,41% |
| Distanza prezzo da EMA200 | -34,82% |
| Gap EMA50/EMA200 | -3,95% |
| Stato cross | EMA50 SOTTO EMA200 |
| RSI weekly | 38,26 |
| Età SOL | 6,3 anni |
| Analoghi storici usati | 30 |
| Max analoghi per asset | 3 |
| Hit EMA200 12w analoghi | +16,67% |
| Max gain mediano 12w | +23,77% |
| Drawdown mediano 12w | -22,03% |

Lettura semplice:

**CONTESTO INTERESSANTE, SERVONO CONFERME DI PREZZO**

Autocontrollo: **STABILE / DA CONFERMARE**.

Questo modulo confronta SOL con altre crypto in fasi simili di età, distanza da EMA200, EMA50/EMA200 e RSI. Non usa stock market.

Nota importante: **questo modulo ora NON pesa più nel Global Confluence**. Resta solo come contesto di ciclo e come mappa verso EMA200 weekly. Il punteggio Global resta guidato da prezzo, scanner, regime, struttura tecnica, frattale, RSI e conferme reali.

Nota: se EMA50/EMA200 sono dentro ±2%, il modulo parla di medie sovrapposte / incrocio in corso, perché exchange diversi possono mostrare il cross leggermente prima o dopo.

<!-- Generato: 2026-07-28 05:14 UTC -->
<!-- MAJOR_ALT_LIFECYCLE_SQUEEZE_END -->

</details>
<!-- COMPACT_SECTION_END:major_alt_lifecycle -->

# Report giornaliero BTC / SOL / DOGE

Aggiornato il: **2026-07-28 05:12:23 UTC**

Questo report confronta il grafico attuale di Bitcoin, Solana e Dogecoin con tanti grafici storici di altre crypto.

Non è una previsione certa. È uno scanner statistico: guarda situazioni simili già successe e mostra cosa accadde dopo nei 30 giorni successivi.

<!-- COMPACT_SECTION_START:daily_change -->
<details open>
<summary><strong>🗓️ Cambiamenti rispetto a ieri</strong></summary>

<!-- DAILY_CHANGE_START -->

---

# Mini report cambiamenti da ieri

Report separato completo: [daily_change_report.md](daily_change_report.md)

- BTC: cambiamento importante in peggioramento rispetto a ieri.
- SOL: cambiamento importante in miglioramento rispetto a ieri.
- DOGE: cambiamento importante in miglioramento rispetto a ieri.

| Asset | Cambio | Tono | Verdetto oggi | Casi positivi oggi | Δ casi positivi |
| --- | --- | --- | --- | --- | --- |
| BTC | CAMBIAMENTO FORTE | peggioramento | RIALZISTA | +62.50% | -10.00 punti |
| SOL | CAMBIAMENTO MEDIO | miglioramento | RIALZISTA | +70.00% | +5.00 punti |
| DOGE | CAMBIAMENTO MEDIO | miglioramento | RIALZISTA | +67.50% | +5.00 punti |

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
| BTC | 60.222 $ | 69.731 $ | +30,43% | +15,79% | rimbalzo poco frequente | 69.731 $ | 60.222 $ | +4,35% | -13,64% | spike storicamente più resistente |
| SOL | 69,62 $ | 80,61 $ | +27,78% | +15,79% | rimbalzo poco frequente | 80,61 $ | 69,62 $ | +4,00% | -13,64% | spike storicamente più resistente |
| DOGE | 0,06646 $ | 0,07696 $ | +29,63% | +15,79% | rimbalzo poco frequente | 0,07696 $ | 0,06646 $ | +50,00% | -13,64% | attenzione a prendere profitto |

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

- **BTC: su 40 casi simili, 23 prima sono scesi a -5,00%. Tra quei 23, 7 poi sono rimbalzati fino a +10,00%. Percentuale: +30,43% (7/23). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.**
- **BTC: su 40 casi simili, 23 prima sono saliti a +10,00%. Tra quei 23, 1 poi sono scaricati a -5,00%. Percentuale: +4,35% (1/23). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.**
- **SOL: su 40 casi simili, 18 prima sono scesi a -5,00%. Tra quei 18, 5 poi sono rimbalzati fino a +10,00%. Percentuale: +27,78% (5/18). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.**
- **SOL: su 40 casi simili, 25 prima sono saliti a +10,00%. Tra quei 25, 1 poi sono scaricati a -5,00%. Percentuale: +4,00% (1/25). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.**
- **DOGE: su 40 casi simili, 27 prima sono scesi a -5,00%. Tra quei 27, 8 poi sono rimbalzati fino a +10,00%. Percentuale: +29,63% (8/27). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.**
- **DOGE: su 40 casi simili, 30 prima sono saliti a +10,00%. Tra quei 30, 15 poi sono scaricati a -5,00%. Percentuale: +50,00% (15/30). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: attenzione a prendere profitto.**

<!-- BOUNCE_AFTER_DRAWDOWN_END -->

</details>
<!-- COMPACT_SECTION_END:bounce_after_drawdown -->

<!-- COMPACT_SECTION_START:scanner_forecast -->
<details>
<summary><strong>🔭 Cono probabilistico dello scanner</strong></summary>

<!-- SCANNER_FORECAST_TRACKER_START -->
# Scanner forecast path / cono probabilistico

Generato: 2026-07-28 05:13:53 UTC


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
| BTC | 2026-07-28 | 63.392 $ | SALITA | 62,50% | 44.096,70 $ | 58.227,10 $ | 68.129,01 $ | 84.908,54 $ | 91.898,18 $ |
| SOL | 2026-07-28 | 73,28 $ | SALITA | 70,00% | 65,84 $ | 71,22 $ | 78,88 $ | 87,47 $ | 107,62 $ |
| DOGE | 2026-07-28 | 0.06996 $ | SALITA | 67,50% | 0.05799 $ | 0.06807 $ | 0.07461 $ | 0.08368 $ | 0.09241 $ |

## Grafici

### BTC

![Scanner forecast BTC](scanner_forecast_BTC.png)

#### Verifica storica e discrepanza

![Verifica storica cono BTC](scanner_forecast_history_BTC.png)

- Cono congelato il **2026-07-10**; verificato fino al **2026-07-28**; stato **PARZIALE 18/30g**.
- Reale **63.388,28 $**; p50 previsto **67.219,12 $**; scarto **-5,70%**.
- Errore medio assoluto **3,90%**; massimo **7,75%**; DENTRO p10-p90; DENTRO p25-p75.

### SOL

![Scanner forecast SOL](scanner_forecast_SOL.png)

#### Verifica storica e discrepanza

![Verifica storica cono SOL](scanner_forecast_history_SOL.png)

- Cono congelato il **2026-07-10**; verificato fino al **2026-07-28**; stato **PARZIALE 18/30g**.
- Reale **73,27 $**; p50 previsto **71,52 $**; scarto **2,44%**.
- Errore medio assoluto **2,58%**; massimo **5,38%**; DENTRO p10-p90; DENTRO p25-p75.

### DOGE

![Scanner forecast DOGE](scanner_forecast_DOGE.png)

#### Verifica storica e discrepanza

![Verifica storica cono DOGE](scanner_forecast_history_DOGE.png)

- Cono congelato il **2026-07-10**; verificato fino al **2026-07-28**; stato **PARZIALE 18/30g**.
- Reale **0.06996 $**; p50 previsto **0.05804 $**; scarto **20,53%**.
- Errore medio assoluto **8,99%**; massimo **24,96%**; DENTRO p10-p90; FUORI p25-p75.

## Accuratezza percorso scanner

| Asset   | Giorno   |   Controlli | Dentro p10-p90   | Dentro p25-p75   | Errore medio abs vs p50   | Errore medio vs p50   |
|:--------|:---------|------------:|:-----------------|:-----------------|:--------------------------|:----------------------|
| BTC | 1g | 18 | 94,44% | 55,56% | 1,95% | -0,16% |
| BTC | 3g | 16 | 100,00% | 68,75% | 2,39% | -0,20% |
| BTC | 7g | 12 | 100,00% | 83,33% | 2,90% | 0,57% |
| BTC | 14g | 5 | 100,00% | 80,00% | 1,66% | -0,47% |
| BTC | 30g | 0 | n/a | n/a | n/a | n/a |
| SOL | 1g | 18 | 72,22% | 38,89% | 2,62% | -0,60% |
| SOL | 3g | 16 | 100,00% | 62,50% | 2,78% | -0,82% |
| SOL | 7g | 12 | 100,00% | 91,67% | 2,55% | 0,86% |
| SOL | 14g | 5 | 100,00% | 80,00% | 3,02% | 3,02% |
| SOL | 30g | 0 | n/a | n/a | n/a | n/a |
| DOGE | 1g | 18 | 88,89% | 50,00% | 3,38% | -0,13% |
| DOGE | 3g | 16 | 100,00% | 93,75% | 2,05% | 1,12% |
| DOGE | 7g | 12 | 100,00% | 100,00% | 7,78% | 7,78% |
| DOGE | 14g | 5 | 100,00% | 20,00% | 18,84% | 18,84% |
| DOGE | 30g | 0 | n/a | n/a | n/a | n/a |

## Calibratore shadow

Il cono ufficiale resta grezzo e invariato. Il calibratore usa soltanto previsioni passate già mature, campionate una volta a settimana per ridurre la falsa indipendenza. Ogni orizzonte si attiva a 30 controlli indipendenti: parte al 25% della correzione stimata e cresce gradualmente fino al 100% a 100 controlli.

| Asset   | Orizzonte   |   Controlli indipendenti |   Soglia | Stato                  | Forza correzione   | Shift p50   |   Scala p10-p90 |
|:--------|:------------|-------------------------:|---------:|:-----------------------|:-------------------|:------------|----------------:|
| BTC | 1g | 4 | 30 | RACCOLTA (26 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 3g | 3 | 30 | RACCOLTA (27 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 7g | 3 | 30 | RACCOLTA (27 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 14g | 2 | 30 | RACCOLTA (28 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 30g | 0 | 30 | RACCOLTA (30 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 1g | 4 | 30 | RACCOLTA (26 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 3g | 3 | 30 | RACCOLTA (27 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 7g | 3 | 30 | RACCOLTA (27 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 14g | 2 | 30 | RACCOLTA (28 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 30g | 0 | 30 | RACCOLTA (30 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 1g | 4 | 30 | RACCOLTA (26 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 3g | 3 | 30 | RACCOLTA (27 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 7g | 3 | 30 | RACCOLTA (27 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 14g | 2 | 30 | RACCOLTA (28 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 30g | 0 | 30 | RACCOLTA (30 mancanti) | 0,0% | 0,00% | 1,000 |

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

Righe salvate nello storico: **48**.

Questa sezione tiene un diario delle previsioni giornaliere a 30 giorni, senza appesantire il report principale.

| Data | Asset | Prezzo | Direzione | Casi positivi | Return p50 | Drawdown p50 | Max gain p50 | Controllo 30g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-07-28 | BTC | 63.392 $ | SALITA | 62,50% | 68.129 $ | 59.231 $ | 71.936 $ | 2026-08-27 |
| 2026-07-28 | DOGE | 0,07000 $ | SALITA | 67,50% | 0,07000 $ | 0,06000 $ | 0,08000 $ | 2026-08-27 |
| 2026-07-28 | SOL | 73,28 $ | SALITA | 70,00% | 78,88 $ | 70,22 $ | 85,52 $ | 2026-08-27 |

<!-- FORECAST_30D_HISTORY_END -->

</details>
<!-- COMPACT_SECTION_END:scanner_forecast -->

<!-- COMPACT_SECTION_START:extreme_cases -->
<details>
<summary><strong>⚠️ Percorso dei casi estremi</strong></summary>

<!-- EXTREME_CASES_PATH_START -->
# Extreme cases path report

Generato: 2026-07-28 05:14 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [extreme_cases_path_report.md](extreme_cases_path_report.md)

Questo report si attiva quando i casi positivi o negativi sono almeno **80%**.

Ora misura anche il **rialzo massimo prima della discesa principale**, quindi distingue uno spike iniziale da una discesa quasi immediata.

## Trigger estremi

| Asset   | Direzione   | Trigger   | Percentuale   | Motivo                           |   Match disponibili |
|:--------|:------------|:----------|:--------------|:---------------------------------|--------------------:|
| BTC     | NESSUNO     | NO        | +62,50%       | Nessun lato sopra soglia estrema |                  40 |
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
- Casi positivi / salita storica: **62,50%**
- Casi negativi / discesa storica: **37,50%**
- Quanto è netto il segnale: **medio**
- Prezzo attuale: **63.391,68 $**
- Return normale fra 30 giorni: **68.129,01 $** (7,47%)
- Drawdown normale durante il mese: **59.230,62 $** (-6,56%)
- Drawdown brutto da rispettare: **52.338,77 $** (-17,44%)
- Max gain normale durante il mese: **71.935,77 $** (13,48%)
- Max gain buono / take profit ottimistico: **88.017,04 $** (38,85%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Solana
- Direzione più probabile a 30 giorni: **SALITA**
- Casi positivi / salita storica: **70,00%**
- Casi negativi / discesa storica: **30,00%**
- Quanto è netto il segnale: **forte**
- Prezzo attuale: **73,28 $**
- Return normale fra 30 giorni: **78,88 $** (7,64%)
- Drawdown normale durante il mese: **70,22 $** (-4,18%)
- Drawdown brutto da rispettare: **64,93 $** (-11,39%)
- Max gain normale durante il mese: **85,52 $** (16,70%)
- Max gain buono / take profit ottimistico: **96,02 $** (31,03%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Dogecoin
- Direzione più probabile a 30 giorni: **SALITA**
- Casi positivi / salita storica: **67,50%**
- Casi negativi / discesa storica: **32,50%**
- Quanto è netto il segnale: **medio**
- Prezzo attuale: **0,07 $**
- Return normale fra 30 giorni: **0,07 $** (6,65%)
- Drawdown normale durante il mese: **0,06 $** (-9,10%)
- Drawdown brutto da rispettare: **0,06 $** (-16,51%)
- Max gain normale durante il mese: **0,08 $** (17,52%)
- Max gain buono / take profit ottimistico: **0,09 $** (32,20%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Messaggio del giorno

Il quadro generale oggi è più favorevole. Lo scanner vede più possibilità di salita su più asset.

---

# Mappa semplice asset per asset

# Bitcoin — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟢 VERDE / Favorevole
**Prezzo attuale:** 63.391,68 $

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

- Se va molto male: **44.096,70 $** (-30,44%)
- Se va male: **58.227,10 $** (-8,15%)
- Scenario normale: **68.129,01 $** (7,47%)
- Se va bene: **84.908,54 $** (33,94%)
- Se va molto bene: **91.898,18 $** (44,97%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **59.230,62 $** (-6,56%)
- Discesa brutta: **52.338,77 $** (-17,44%)
- Discesa molto brutta: **43.028,31 $** (-32,12%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **71.935,77 $** (13,48%)
- Rialzo buono: **88.017,04 $** (38,85%)
- Rialzo molto forte: **97.924,04 $** (54,47%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Bitcoin tendeva a muoversi tra una zona bassa intorno a **59.230,62 $** e uno spike normale intorno a **71.935,77 $**.

La chiusura a 30 giorni era più spesso positiva: salita 62,50%, discesa 37,50%. Quindi la lettura principale è favorevole.

Nota leva BTC: se la liquidazione è vicina a 51.000 $, guarda soprattutto la discesa brutta e molto brutta. Il prezzo può recuperare dopo, ma la leva può saltare prima.

---

# Solana — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟢 VERDE / Favorevole
**Prezzo attuale:** 73,28 $

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

- Se va molto male: **65,84 $** (-10,15%)
- Se va male: **71,22 $** (-2,81%)
- Scenario normale: **78,88 $** (7,64%)
- Se va bene: **87,47 $** (19,37%)
- Se va molto bene: **107,62 $** (46,86%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **70,22 $** (-4,18%)
- Discesa brutta: **64,93 $** (-11,39%)
- Discesa molto brutta: **59,94 $** (-18,20%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **85,52 $** (16,70%)
- Rialzo buono: **96,02 $** (31,03%)
- Rialzo molto forte: **113,95 $** (55,50%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Solana tendeva a muoversi tra una zona bassa intorno a **70,22 $** e uno spike normale intorno a **85,52 $**.

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

- Se va molto male: **0,06 $** (-17,11%)
- Se va male: **0,07 $** (-2,70%)
- Scenario normale: **0,07 $** (6,65%)
- Se va bene: **0,08 $** (19,61%)
- Se va molto bene: **0,09 $** (32,09%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **0,06 $** (-9,10%)
- Discesa brutta: **0,06 $** (-16,51%)
- Discesa molto brutta: **0,05 $** (-21,40%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **0,08 $** (17,52%)
- Rialzo buono: **0,09 $** (32,20%)
- Rialzo molto forte: **0,10 $** (41,63%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Dogecoin tendeva a muoversi tra una zona bassa intorno a **0,06 $** e uno spike normale intorno a **0,08 $**.

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

Per ora non ci sono ancora previsioni vecchie di 30 giorni da controllare.
Il controllo vero inizierà automaticamente dopo il primo mese di utilizzo.

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

Dati ancora insufficienti: previsioni controllate **0** su **30** necessarie.

Per ora si usa solo lo scanner storico grezzo. Quando ci saranno abbastanza previsioni controllate, qui apparirà la lettura autocalibrata.

## Solana

Dati ancora insufficienti: previsioni controllate **0** su **30** necessarie.

Per ora si usa solo lo scanner storico grezzo. Quando ci saranno abbastanza previsioni controllate, qui apparirà la lettura autocalibrata.

## Dogecoin

Dati ancora insufficienti: previsioni controllate **0** su **30** necessarie.

Per ora si usa solo lo scanner storico grezzo. Quando ci saranno abbastanza previsioni controllate, qui apparirà la lettura autocalibrata.

---

# Approfondimento tecnico — Bitcoin (BTC-USD)

## Semaforo: 🟢 VERDE / Favorevole

**Prezzo attuale:** 63.391,68 $

Bitcoin ha un segnale favorevole. La statistica dei casi simili indica più possibilità di salita che di discesa, ma resta comunque una probabilità, non una certezza.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **62,50%**
- Casi negativi dopo 30 giorni: **37,50%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **86,33%**
- Rendimento medio dopo 30 giorni: **10,82%**
- Rendimento centrale dopo 30 giorni: **7,47%**
- Discesa media durante i 30 giorni: **-11,52%**
- Massimo rialzo medio durante i 30 giorni: **26,16%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **70.252,53 $**
- Scenario centrale a 30 giorni: **68.129,01 $**
- Zona di rischio media: **56.091,49 $**
- Zona di rialzo media: **79.974,80 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -30,44% → **44.096,70 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -8,15% → **58.227,10 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: 7,47% → **68.129,01 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 33,94% → **84.908,54 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 44,97% → **91.898,18 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -32,12% → **43.028,31 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -17,44% → **52.338,77 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -6,56% → **59.230,62 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -2,09% → **62.067,67 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: -0,01% → **63.388,39 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 0,00% → **63.391,68 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 3,37% → **65.525,31 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 13,48% → **71.935,77 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 38,85% → **88.017,04 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 54,47% → **97.924,04 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| LRC-USD         | 2018-10-04   | 2019-01-11 |        90.62 |        35.3  |          -5.72 |         154.28 |
| XLM-USD         | 2020-07-20   | 2020-10-27 |        89.93 |       104.8  |          -8.82 |         138.95 |
| FIL-USD         | 2023-07-04   | 2023-10-11 |        89.56 |        44.46 |          -0.01 |          44.46 |
| SAND-USD        | 2023-07-04   | 2023-10-11 |        89.35 |        49.54 |          -0.05 |          49.54 |
| ONE-USD         | 2020-01-27   | 2020-05-05 |        88.71 |         9.39 |          -4.18 |          11.48 |
| XRP-USD         | 2019-10-09   | 2020-01-16 |        88.25 |        33.98 |          -3.56 |          46.48 |
| MKR-USD         | 2020-01-28   | 2020-05-06 |        88.19 |        44.12 |          -4.48 |          54.19 |
| XRP-USD         | 2025-12-21   | 2026-03-30 |        87.68 |         3.53 |          -0.53 |          11.68 |
| BTC-USD         | 2018-10-05   | 2019-01-12 |        87.67 |        -0.35 |          -7.15 |           1.84 |
| DOGE-USD        | 2020-07-20   | 2020-10-27 |        87.63 |        21.4  |          -5.98 |          57.04 |

---

# Approfondimento tecnico — Solana (SOL-USD)

## Semaforo: 🟢 VERDE / Favorevole

**Prezzo attuale:** 73,28 $

Solana ha un segnale favorevole. La statistica dei casi simili indica più possibilità di salita che di discesa, ma resta comunque una probabilità, non una certezza.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **70,00%**
- Casi negativi dopo 30 giorni: **30,00%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **76,18%**
- Rendimento medio dopo 30 giorni: **11,81%**
- Rendimento centrale dopo 30 giorni: **7,64%**
- Discesa media durante i 30 giorni: **-7,94%**
- Massimo rialzo medio durante i 30 giorni: **24,29%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **81,94 $**
- Scenario centrale a 30 giorni: **78,88 $**
- Zona di rischio media: **67,46 $**
- Zona di rialzo media: **91,08 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -10,15% → **65,84 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -2,81% → **71,22 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: 7,64% → **78,88 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 19,37% → **87,47 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 46,86% → **107,62 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -18,20% → **59,94 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -11,39% → **64,93 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -4,18% → **70,22 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -1,35% → **72,29 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: 0,00% → **73,28 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 2,23% → **74,91 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 5,61% → **77,39 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 16,70% → **85,52 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 31,03% → **96,02 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 55,50% → **113,95 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| WAVES-USD       | 2019-03-13   | 2019-06-20 |        81.34 |       -36.8  |         -40.77 |           1.46 |
| QTUM-USD        | 2018-10-09   | 2019-01-16 |        79.25 |       -10.22 |         -17.99 |           1.51 |
| RUNE-USD        | 2025-12-22   | 2026-03-31 |        79.1  |        20.64 |          -8.4  |          23.46 |
| SOL-USD         | 2025-12-19   | 2026-03-28 |        78.69 |         3.42 |          -3.74 |           8.51 |
| NEAR-USD        | 2025-12-21   | 2026-03-30 |        78.66 |        14.29 |           0    |          23.51 |
| BNB-USD         | 2025-12-21   | 2026-03-30 |        78.03 |         1.44 |          -4.18 |           5.73 |
| VET-USD         | 2020-01-24   | 2020-05-02 |        77.96 |        46.8  |          -8.35 |          46.8  |
| EOS-USD         | 2018-10-19   | 2019-01-26 |        77.57 |        47.4  |          -7.62 |          75.2  |
| KAVA-USD        | 2025-12-21   | 2026-03-30 |        77.52 |         5.72 |          -7.96 |          14.26 |
| LINK-USD        | 2025-12-21   | 2026-03-30 |        77.5  |         5.89 |           0    |          11.78 |

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

- Somiglianza media dei pattern: **87,94%**
- Rendimento medio dopo 30 giorni: **6,86%**
- Rendimento centrale dopo 30 giorni: **6,65%**
- Discesa media durante i 30 giorni: **-11,34%**
- Massimo rialzo medio durante i 30 giorni: **21,18%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **0,07 $**
- Scenario centrale a 30 giorni: **0,07 $**
- Zona di rischio media: **0,06 $**
- Zona di rialzo media: **0,08 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -17,11% → **0,06 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -2,70% → **0,07 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: 6,65% → **0,07 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 19,61% → **0,08 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 32,09% → **0,09 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -21,40% → **0,05 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -16,51% → **0,06 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -9,10% → **0,06 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -3,69% → **0,07 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: 0,00% → **0,07 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 5,39% → **0,07 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 10,23% → **0,08 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 17,52% → **0,08 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 32,20% → **0,09 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 41,63% → **0,10 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| ZEC-USD         | 2019-06-06   | 2019-09-13 |        92.52 |       -17.01 |         -21.22 |          18.25 |
| OP-USD          | 2025-12-22   | 2026-03-31 |        89.94 |         8.81 |          -3.72 |          21.82 |
| VET-USD         | 2022-03-14   | 2022-06-21 |        89.63 |         7.68 |          -8.95 |          11.1  |
| MKR-USD         | 2022-09-29   | 2023-01-06 |        89.5  |        28.84 |           0    |          32.75 |
| DASH-USD        | 2022-03-07   | 2022-06-14 |        89.24 |         0.01 |          -8.31 |          19.82 |
| AVAX-USD        | 2025-08-29   | 2025-12-06 |        89.1  |         7.79 |         -14.74 |           8.89 |
| NEAR-USD        | 2022-03-22   | 2022-06-29 |        88.82 |        28.15 |          -6.55 |          33.07 |
| LTC-USD         | 2018-04-13   | 2018-07-21 |        88.62 |       -36.07 |         -36.07 |           5.71 |
| RUNE-USD        | 2022-03-08   | 2022-06-15 |        88.54 |         6.81 |         -22.98 |          22.31 |
| INJ-USD         | 2022-03-09   | 2022-06-16 |        88.53 |        -2.67 |         -13.24 |           7.61 |

</details>
<!-- COMPACT_SECTION_END:scanner_full_detail -->

<!-- COMPACT_SECTION_START:market_regime -->
<details>
<summary><strong>🌦️ Market Regime Match</strong></summary>

<!-- MARKET_REGIME_MATCH_START -->
# Market Regime Match Report


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [market_regime_match_report.md](market_regime_match_report.md)

Generated: 2026-07-28 05:14 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | BEAR | 63.392 $ | False | -16.36% | -9.80% | BEAR | -16.36% | -9.80% |
| DOGE-USD | BEAR | 0.06996 $ | False | -32.74% | -16.09% | BEAR | -16.36% | -9.80% |
| SOL-USD | BEAR | 73,28 $ | False | -11.76% | -16.58% | BEAR | -16.36% | -9.80% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 62.50% | 7.47% | 33.94% | 44.97% | -6.56% | -32.12% | 13.48% | 38.85% | 54.47% | 55.00% | 6.12% | 41.82% | 66.03% |
| BTC-USD | SAME_BTC_REGIME | 16 | 68.75% | 6.67% | 22.90% | 34.64% | -4.95% | -15.04% | 13.48% | 28.91% | 49.05% | 50.00% | -0.07% | 8.42% | 33.22% |
| BTC-USD | SAME_ASSET_REGIME | 23 | 78.26% | 11.36% | 35.19% | 48.53% | -4.18% | -14.04% | 19.65% | 43.32% | 51.21% | 65.22% | 8.09% | 42.82% | 65.06% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 14 | 71.43% | 6.67% | 17.37% | 34.90% | -4.95% | -12.10% | 13.48% | 25.32% | 50.08% | 50.00% | -0.07% | 7.74% | 42.73% |
| DOGE-USD | ALL_MATCHES | 40 | 67.50% | 6.65% | 19.61% | 32.09% | -9.10% | -21.40% | 17.52% | 32.20% | 41.63% | 65.00% | 9.67% | 33.17% | 68.19% |
| DOGE-USD | SAME_BTC_REGIME | 23 | 78.26% | 6.81% | 23.60% | 32.54% | -8.31% | -18.26% | 19.82% | 32.55% | 41.28% | 73.91% | 9.96% | 30.87% | 39.61% |
| DOGE-USD | SAME_ASSET_REGIME | 26 | 76.92% | 6.92% | 26.96% | 35.18% | -7.54% | -17.46% | 20.47% | 31.91% | 42.84% | 76.92% | 21.36% | 39.48% | 76.78% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 21 | 76.19% | 6.81% | 19.04% | 32.67% | -8.31% | -18.79% | 16.79% | 31.59% | 41.33% | 71.43% | 9.39% | 31.22% | 40.13% |
| SOL-USD | ALL_MATCHES | 40 | 70.00% | 7.64% | 19.37% | 46.86% | -4.18% | -18.20% | 16.70% | 31.03% | 55.50% | 77.50% | 8.68% | 36.76% | 105.22% |
| SOL-USD | SAME_BTC_REGIME | 21 | 90.48% | 9.53% | 18.94% | 33.93% | -3.74% | -10.59% | 19.46% | 23.51% | 36.50% | 80.95% | 4.70% | 25.61% | 77.90% |
| SOL-USD | SAME_ASSET_REGIME | 29 | 68.97% | 9.39% | 14.29% | 39.07% | -4.18% | -18.42% | 14.26% | 23.46% | 58.57% | 75.86% | 5.54% | 29.89% | 83.31% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 18 | 88.89% | 9.45% | 13.67% | 19.45% | -3.79% | -11.64% | 15.14% | 21.37% | 24.37% | 77.78% | 2.91% | 11.08% | 77.51% |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 16 | 68.75% | 6.67% | -4.95% | 28.91% | 50.00% | -0.07% | 28.91% |
| BTC-USD | HISTORICAL_BTC_BULL | 20 | 60.00% | 19.81% | -7.40% | 42.75% | 60.00% | 32.71% | 60.68% |
| BTC-USD | HISTORICAL_BTC_MIXED | 1 | 100.00% | 44.12% | -4.48% | 54.19% | 100.00% | 41.64% | 108.28% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 3 | 33.33% | -2.53% | -15.01% | 4.77% | 33.33% | -16.17% | 11.33% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 23 | 78.26% | 6.81% | -8.31% | 32.55% | 73.91% | 9.96% | 59.11% |
| DOGE-USD | HISTORICAL_BTC_BULL | 9 | 66.67% | 7.72% | -6.83% | 37.34% | 55.56% | 7.71% | 78.82% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 8 | 37.50% | -14.15% | -19.83% | 20.16% | 50.00% | 8.74% | 43.14% |
| SOL-USD | HISTORICAL_BTC_BEAR | 21 | 90.48% | 9.53% | -3.74% | 23.51% | 80.95% | 4.70% | 47.19% |
| SOL-USD | HISTORICAL_BTC_BULL | 7 | 85.71% | 5.61% | -2.06% | 51.15% | 100.00% | 24.11% | 82.85% |
| SOL-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 0.00% | -5.89% | -15.62% | 6.07% | 100.00% | 26.02% | 83.19% |
| SOL-USD | HISTORICAL_BTC_MIXED | 1 | 100.00% | 44.12% | -4.48% | 54.19% | 100.00% | 41.64% | 108.28% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 10 | 20.00% | -9.57% | -17.86% | 5.11% | 50.00% | 1.42% | 90.20% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 23 | 78.26% | 11.36% | -4.18% | 43.32% | 65.22% | 8.09% | 55.62% |
| BTC-USD | HISTORICAL_ASSET_BULL | 10 | 40.00% | -15.35% | -21.20% | 33.82% | 40.00% | -23.29% | 46.73% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 100.00% | 18.22% | -5.61% | 18.22% | 100.00% | 29.43% | 32.77% |
| BTC-USD | HISTORICAL_ASSET_MIXED | 3 | 66.67% | 33.93% | -4.48% | 45.34% | 66.67% | 9.42% | 72.39% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 3 | 0.00% | -5.27% | -17.34% | 1.99% | 0.00% | -21.02% | 1.99% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 26 | 76.92% | 6.92% | -7.54% | 31.91% | 76.92% | 21.36% | 64.58% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 5 | 80.00% | 12.21% | -5.98% | 37.34% | 60.00% | 9.96% | 75.34% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 9 | 33.33% | -8.09% | -19.76% | 14.07% | 33.33% | -6.60% | 18.25% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 29 | 68.97% | 9.39% | -4.18% | 23.46% | 75.86% | 5.54% | 77.34% |
| SOL-USD | HISTORICAL_ASSET_BULL | 4 | 50.00% | 2.34% | -8.74% | 29.92% | 75.00% | 4.36% | 128.48% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 100.00% | 30.90% | -1.74% | 30.90% | 100.00% | 35.13% | 47.19% |
| SOL-USD | HISTORICAL_ASSET_MIXED | 2 | 100.00% | 39.02% | -2.24% | 49.77% | 100.00% | 25.53% | 90.33% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 4 | 75.00% | 3.82% | -4.18% | 35.28% | 75.00% | 16.69% | 58.92% |

## Top regime-adjusted matches

The table below shows the top matches separately for each target, so BTC does not hide SOL and DOGE.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | LRC-USD | 2018-10-04 | 90.62% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 35.30% | -5.72% | 154.28% | 57.00% | -5.72% | 154.28% |
| BTC-USD | ONE-USD | 2020-01-27 | 88.71% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 9.39% | -4.18% | 11.48% | -11.35% | -20.74% | 11.52% |
| BTC-USD | XRP-USD | 2019-10-09 | 88.25% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 33.98% | -3.56% | 46.48% | -38.29% | -38.91% | 46.48% |
| BTC-USD | XRP-USD | 2025-12-21 | 87.68% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 3.53% | -0.53% | 11.68% | 0.43% | -1.24% | 12.21% |
| BTC-USD | BTC-USD | 2018-10-05 | 87.67% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -0.35% | -7.15% | 1.84% | 6.70% | -7.15% | 13.14% |
| BTC-USD | ETH-USD | 2025-12-21 | 86.93% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 11.36% | 0.00% | 19.65% | -0.57% | -0.79% | 19.65% |
| BTC-USD | BTC-USD | 2025-12-22 | 85.76% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 11.83% | -1.97% | 15.28% | 8.09% | -1.97% | 20.38% |
| BTC-USD | BNB-USD | 2025-12-21 | 85.73% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 1.44% | -4.18% | 5.73% | 5.54% | -4.18% | 11.40% |
| BTC-USD | BNB-USD | 2018-10-04 | 85.69% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 51.62% | -8.34% | 51.62% | 153.58% | -8.34% | 153.58% |
| BTC-USD | QTUM-USD | 2020-01-27 | 85.46% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 19.22% | -8.83% | 22.12% | 9.44% | -8.83% | 22.12% |
| DOGE-USD | OP-USD | 2025-12-22 | 89.94% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 8.81% | -3.72% | 21.82% | 8.70% | -3.72% | 56.00% |
| DOGE-USD | VET-USD | 2022-03-14 | 89.63% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 7.68% | -8.95% | 11.10% | 9.39% | -8.95% | 41.71% |
| DOGE-USD | DASH-USD | 2022-03-07 | 89.24% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 0.01% | -8.31% | 19.82% | 30.52% | -8.31% | 30.52% |
| DOGE-USD | LTC-USD | 2018-04-13 | 88.62% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -36.07% | -36.07% | 5.71% | -35.67% | -38.84% | 5.71% |
| DOGE-USD | RUNE-USD | 2022-03-08 | 88.54% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 6.81% | -22.98% | 22.31% | 37.54% | -22.98% | 46.15% |
| DOGE-USD | INJ-USD | 2022-03-09 | 88.53% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -2.67% | -13.24% | 7.61% | 32.39% | -13.24% | 54.99% |
| DOGE-USD | HBAR-USD | 2022-03-14 | 88.25% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -2.78% | -18.79% | 1.28% | -7.73% | -18.79% | 12.96% |
| DOGE-USD | AVAX-USD | 2022-03-13 | 88.09% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 37.69% | -6.20% | 44.34% | 31.22% | -6.20% | 71.22% |
| DOGE-USD | THETA-USD | 2022-03-16 | 88.04% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 0.32% | -16.14% | 13.49% | -6.06% | -16.14% | 28.27% |
| DOGE-USD | OMG-USD | 2022-03-12 | 87.76% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 10.56% | -9.26% | 12.35% | 16.89% | -9.26% | 32.62% |
| SOL-USD | RUNE-USD | 2025-12-22 | 79.10% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 20.64% | -8.40% | 23.46% | 3.30% | -8.40% | 52.16% |
| SOL-USD | SOL-USD | 2025-12-19 | 78.69% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 3.42% | -3.74% | 8.51% | 0.43% | -3.74% | 18.70% |
| SOL-USD | NEAR-USD | 2025-12-21 | 78.66% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 14.29% | 0.00% | 23.51% | 104.94% | 0.00% | 139.37% |
| SOL-USD | BNB-USD | 2025-12-21 | 78.03% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 1.44% | -4.18% | 5.73% | 5.54% | -4.18% | 11.40% |
| SOL-USD | EOS-USD | 2018-10-19 | 77.57% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 47.40% | -7.62% | 75.20% | 77.34% | -7.62% | 77.34% |
| SOL-USD | KAVA-USD | 2025-12-21 | 77.52% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 5.72% | -7.96% | 14.26% | 2.51% | -7.96% | 24.10% |
| SOL-USD | LINK-USD | 2025-12-21 | 77.50% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 5.89% | 0.00% | 11.78% | 4.70% | 0.00% | 24.41% |
| SOL-USD | DOT-USD | 2025-12-16 | 77.19% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -7.88% | -14.40% | 0.00% | -8.57% | -14.40% | 1.55% |
| SOL-USD | BTC-USD | 2025-12-22 | 76.64% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 11.83% | -1.97% | 15.28% | 8.09% | -1.97% | 20.38% |
| SOL-USD | ZIL-USD | 2018-10-06 | 76.62% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -7.19% | -10.59% | 26.39% | -0.95% | -11.40% | 26.39% |

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

Generato: 2026-07-28 05:14 UTC


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
| BTC | 63.392 $ | -6 | RIBASSISTA / FRAGILE | STAGE 4 / MARKDOWN | MASSIMI E MINIMI CRESCENTI | ACCUMULO POSSIBILE / RANGE BASSO | BASSO | RIDUCI RISCHIO / NO LONG A LEVA |
| SOL | 73,28 $ | -12 | RIBASSISTA / FRAGILE | STAGE 4 / MARKDOWN | MASSIMI E MINIMI DECRESCENTI | MARKDOWN / DEBOLEZZA | BASSO | NON INSEGUIRE / TAKE PROFIT SU SPIKE |
| DOGE | 0.06996 $ | -7 | RIBASSISTA / FRAGILE | STAGE 4 / MARKDOWN | MASSIMI E MINIMI DECRESCENTI | MARKDOWN / DEBOLEZZA | BASSO | NO LONG / SHORT SOLO DOPO SPIKE E REJECTION |

## Punteggi per area

| Asset | Trend | Struttura | Momentum | Volume | Prezzo | Candela | Wyckoff | Totale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | -4 | +2 | -3 | -1 | 0 | 0 | 0 | -6 |
| SOL | -4 | -2 | -3 | -2 | 0 | 0 | -2 | -12 |
| DOGE | -4 | -2 | +2 | -1 | 0 | 0 | -2 | -7 |

## Livelli tecnici

| Asset | Supporto | Resistenza | Breakout 60g | Breakdown 60g | ATR14 | Rendimento 30g | Rendimento 90g |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 63.062 $ | 64.186 $ | 77.991 $ | 57.748 $ | 2,43% | 5,74% | -16,99% |
| SOL | 67,92 $ | 74,89 $ | 86,76 $ | 60,41 $ | 2,96% | 4,03% | -12,84% |
| DOGE | 0.06961 $ | 0.07377 $ | 0.10365 $ | 0.06829 $ | 3,40% | -6,01% | -29,60% |

## Lettura dettagliata

### BTC

- Prezzo: **63.392 $**
- Score classico: **-6 / 12**
- Verdetto: **RIBASSISTA / FRAGILE**
- Azione coerente: **RIDUCI RISCHIO / NO LONG A LEVA**
- Volatilità tecnica locale: **BASSO** — ATR14 2,43%; distanza supporto 0,50%; distanza resistenza 1,27%

Dettaglio:

- Trend: **-4** — prezzo sotto MA200 daily; MA50 daily in discesa; MA200 daily in discesa; STAGE 4 / MARKDOWN
- Stage weekly: **STAGE 4 / MARKDOWN** — Prezzo sotto MA30 weekly con MA30 in discesa.
- Struttura: **+2** — MASSIMI E MINIMI CRESCENTI
- Momentum: **-3** — RSI neutrale 46.4; RSI in peggioramento; MACD sotto signal; istogramma MACD in peggioramento
- Volume: **-1** — OBV sotto media; CMF neutrale 0.05; volume ratio 1.14
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **0** — ACCUMULO POSSIBILE / RANGE BASSO. Prezzo nella metà bassa del range, ma senza spring confermato.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 46.40 |
| MACD histogram | -44.17116 |
| CMF20 | 0.049 |
| Volume ratio 20 | 1.14 |
| MA20 | 64.312 $ |
| MA50 | 63.267 $ |
| MA100 | 69.536 $ |
| MA200 | 71.991 $ |
| Pendenza MA50 20g | -4,45% |
| Pendenza MA200 60g | -9,98% |
| Bollinger width | 6,96% |
| Bollinger position | 0.29 |

### SOL

- Prezzo: **73,28 $**
- Score classico: **-12 / 12**
- Verdetto: **RIBASSISTA / FRAGILE**
- Azione coerente: **NON INSEGUIRE / TAKE PROFIT SU SPIKE**
- Volatilità tecnica locale: **BASSO** — ATR14 2,96%; distanza supporto 7,85%; distanza resistenza 2,24%

Dettaglio:

- Trend: **-4** — prezzo sotto MA200 daily; MA200 daily in discesa; STAGE 4 / MARKDOWN
- Stage weekly: **STAGE 4 / MARKDOWN** — Prezzo sotto MA30 weekly con MA30 in discesa.
- Struttura: **-2** — MASSIMI E MINIMI DECRESCENTI
- Momentum: **-3** — RSI neutrale 42.8; RSI in peggioramento; MACD sotto signal; istogramma MACD in peggioramento
- Volume: **-2** — OBV sotto media; CMF negativo -0.08; volume ratio 1.19
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **-2** — MARKDOWN / DEBOLEZZA. Prezzo basso nel range e sotto medie principali.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 42.82 |
| MACD histogram | -0.42882 |
| CMF20 | -0.076 |
| Volume ratio 20 | 1.19 |
| MA20 | 76,37 $ |
| MA50 | 74,11 $ |
| MA100 | 79,10 $ |
| MA200 | 87,72 $ |
| Pendenza MA50 20g | -1,40% |
| Pendenza MA200 60g | -16,92% |
| Bollinger width | 8,35% |
| Bollinger position | -0.01 |

### DOGE

- Prezzo: **0.06996 $**
- Score classico: **-7 / 12**
- Verdetto: **RIBASSISTA / FRAGILE**
- Azione coerente: **NO LONG / SHORT SOLO DOPO SPIKE E REJECTION**
- Volatilità tecnica locale: **BASSO** — ATR14 3,40%; distanza supporto 0,50%; distanza resistenza 5,44%

Dettaglio:

- Trend: **-4** — prezzo sotto MA200 daily; medie daily allineate ribassiste; MA50 daily in discesa; MA200 daily in discesa; STAGE 4 / MARKDOWN
- Stage weekly: **STAGE 4 / MARKDOWN** — Prezzo sotto MA30 weekly con MA30 in discesa.
- Struttura: **-2** — MASSIMI E MINIMI DECRESCENTI
- Momentum: **+2** — RSI neutrale 39.2; MACD sopra signal; istogramma MACD in miglioramento
- Volume: **-1** — OBV sotto media; CMF neutrale -0.03; volume ratio 1.11
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **-2** — MARKDOWN / DEBOLEZZA. Prezzo basso nel range e sotto medie principali.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 39.22 |
| MACD histogram | 0.00025 |
| CMF20 | -0.026 |
| Volume ratio 20 | 1.11 |
| MA20 | 0.07235 $ |
| MA50 | 0.07708 $ |
| MA100 | 0.08966 $ |
| MA200 | 0.09637 $ |
| Pendenza MA50 20g | -11,44% |
| Pendenza MA200 60g | -16,39% |
| Bollinger width | 8,12% |
| Bollinger position | 0.08 |

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

Generato: 2026-07-28 05:14 UTC


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
| BTC | 63.392 $ | Doppio massimo | CANDIDATO | ribassista | n/a | 48.247 $ | n/a | 9,77% | Fib 38,2% TESTATO (0) @ 63.410 $ | NEL RANGE | 62.553 $ |
| SOL | 73,28 $ | Doppio minimo | MATURO | rialzista | 2026-07-01 | 91,46 $ | -17,13% | n/a | Fib 23,6% TESTATO (0) @ 74,40 $ | NEL RANGE | 68,69 $ |
| DOGE | 0.06996 $ | Triplo massimo | MATURO | ribassista | 2026-06-24 | 0.05847 $ | 41,45% | n/a | Fib 23,6% NON ATTIVO (0) @ 0.08213 $ | NEL RANGE | 0.06961 $ |

## BTC

![Classic visual BTC](classic_visual_BTC.png)

- Pattern principale: **Doppio massimo**
- Stato pattern: **CANDIDATO** (0)
- Famiglia: **ribassista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-06-15 -> 2026-07-21**
- Età formazione: **7 giorni**
- Breakout pattern: **n/a**
- Età breakout: **n/a**
- Neckline: **57.748 $**
- Target teorico: **48.247 $**
- Progresso verso target: **n/a**
- Distanza dalla neckline: **9,77%**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 38,2% TESTATO (0) @ 63.410 $** — Swing UP 2026-07-01 57.748 -> 2026-07-21 66.910; livello più vicino 38.2% a 63.410; stato TESTATO; confluenza: nessuna confluenza indipendente.
- Invalidazione: **58.903 $**
- Relazione prezzo/neckline: **sopra neckline**
- Dettaglio: Due massimi simili vicino a 67.248 tra 2026-06-15 e 2026-07-21. Neckline ribassista stimata: 57.748. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 7 giorni. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **NEL RANGE**
- Supporto: **62.553 $**
- Resistenza: **65.508 $**
- Breakout 60g: **77.991 $**
- Breakdown 60g: **57.748 $**
- RSI14: **46.45**
- ATR14: **2,43%**
- Volume ratio 20g: **1.14**
- Rendimento 30g: **+5,76%**
- Rendimento 90g: **-16,97%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Doppio massimo | CANDIDATO | 0 | ribassista | 57.748 $ | n/a | n/a | 48.247 $ | n/a | 9,77% | 58.903 $ | Due massimi simili a 67.248 $ e 66.910 $. Neckline circa 57.748 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 7 giorni. |
| Doppio minimo | CANDIDATO | 0 | rialzista | 67.248 $ | n/a | n/a | 76.748 $ | n/a | 6,08% | 65.903 $ | Due minimi simili a 59.109 $ e 57.748 $. Neckline circa 67.248 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 27 giorni. |

## SOL

![Classic visual SOL](classic_visual_SOL.png)

- Pattern principale: **Doppio minimo**
- Stato pattern: **MATURO** (+1)
- Famiglia: **rialzista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-06-06 -> 2026-06-25**
- Età formazione: **33 giorni**
- Breakout pattern: **2026-07-01**
- Età breakout: **27 giorni**
- Neckline: **75,94 $**
- Target teorico: **91,46 $**
- Progresso verso target: **-17,13%**
- Distanza dalla neckline: **n/a**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 23,6% TESTATO (0) @ 74,40 $** — Swing UP 2026-06-06 60,41 -> 2026-07-21 78,73; livello più vicino 23.6% a 74,40; stato TESTATO; confluenza: neckline rialzista, invalidazione rialzista.
- Invalidazione: **74,42 $**
- Relazione prezzo/neckline: **sotto neckline**
- Dettaglio: Due minimi simili vicino a 60,41 tra 2026-06-06 e 2026-06-25. Neckline stimata: 75,94. Breakout neckline: 2026-07-01 (27 giorni fa). Stato: MATURO. Target teorico: 91,46; progresso corrente: -17,13%. Relazione prezzo/neckline: sotto neckline. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **NEL RANGE**
- Supporto: **68,69 $**
- Resistenza: **74,89 $**
- Breakout 60g: **86,76 $**
- Breakdown 60g: **60,41 $**
- RSI14: **42.89**
- ATR14: **2,96%**
- Volume ratio 20g: **1.19**
- Rendimento 30g: **+4,08%**
- Rendimento 90g: **-12,80%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Doppio minimo | MATURO | +1 | rialzista | 75,94 $ | 2026-07-01 | 27g | 91,46 $ | -17,13% | n/a | 74,42 $ | Due minimi simili vicino a 60,41 tra 2026-06-06 e 2026-06-25. Neckline stimata: 75,94. Breakout neckline: 2026-07-01 (27 giorni fa). Stato: MATURO. Target teorico: 91,46; progresso corrente: -17,13%. Relazione prezzo/neckline: sotto neckline. Fonte lifecycle: technical_structure_metrics.csv. |
| Doppio massimo | CANDIDATO | 0 | ribassista | 64,42 $ | n/a | n/a | 50,11 $ | n/a | 13,76% | 65,71 $ | Due massimi simili a 75,94 $ e 78,73 $. Neckline circa 64,42 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 7 giorni. |
| Testa e spalle inverso | CANDIDATO | 0 | rialzista | 79,35 $ | n/a | n/a | 94,28 $ | n/a | 8,28% | 77,76 $ | Spalla sinistra 67,92 $, testa 64,42 $, spalla destra 73,40 $. Neckline circa 79,35 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 11 giorni. |
| Doppio minimo | CANDIDATO | 0 | rialzista | 98,27 $ | n/a | n/a | 114,91 $ | n/a | 34,10% | 96,30 $ | Due minimi simili a 81,63 $ e 81,69 $. Neckline circa 98,27 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 66 giorni. |
| Testa e spalle | TARGET RAGGIUNTO | 0 | ribassista | 82,57 $ | 2026-05-28 | 61g | 66,88 $ | 59,21% | n/a | 84,22 $ | Spalla sinistra 88,05 $, testa 98,27 $, spalla destra 87,79 $. Neckline circa 82,57 $. Breakout neckline: 2026-05-28 (61 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 66,88 $; progresso: 59,21%; prezzo sotto neckline. |

## DOGE

![Classic visual DOGE](classic_visual_DOGE.png)

- Pattern principale: **Triplo massimo**
- Stato pattern: **MATURO** (-1)
- Famiglia: **ribassista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-03-25 -> 2026-06-12**
- Età formazione: **46 giorni**
- Breakout pattern: **2026-06-24**
- Età breakout: **34 giorni**
- Neckline: **0.07809 $**
- Target teorico: **0.05847 $**
- Progresso verso target: **41,45%**
- Distanza dalla neckline: **n/a**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 23,6% NON ATTIVO (0) @ 0.08213 $** — Swing DOWN 2026-05-14 0.11825 -> 2026-07-13 0.07097; livello più vicino 23.6% a 0.08213; stato NON ATTIVO; confluenza: nessuna confluenza indipendente.
- Invalidazione: **0.07966 $**
- Relazione prezzo/neckline: **sotto neckline**
- Dettaglio: Tre massimi simili vicino a 0.09772 dal 2026-03-25 al 2026-06-12. Neckline ribassista stimata: 0.07809. Breakout neckline: 2026-06-24 (34 giorni fa). Stato: MATURO. Target teorico: 0.05847; progresso corrente: 41,45%. Relazione prezzo/neckline: sotto neckline. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **NEL RANGE**
- Supporto: **0.06961 $**
- Resistenza: **0.07923 $**
- Breakout 60g: **0.10365 $**
- Breakdown 60g: **0.06829 $**
- RSI14: **39.22**
- ATR14: **3,40%**
- Volume ratio 20g: **1.11**
- Rendimento 30g: **-6,01%**
- Rendimento 90g: **-29,60%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Triplo massimo | MATURO | -1 | ribassista | 0.07809 $ | 2026-06-24 | 34g | 0.05847 $ | 41,45% | n/a | 0.07966 $ | Tre massimi simili vicino a 0.09772 dal 2026-03-25 al 2026-06-12. Neckline ribassista stimata: 0.07809. Breakout neckline: 2026-06-24 (34 giorni fa). Stato: MATURO. Target teorico: 0.05847; progresso corrente: 41,45%. Relazione prezzo/neckline: sotto neckline. Fonte lifecycle: technical_structure_metrics.csv. |
| Doppio massimo | MATURO | -1 | ribassista | 0.07809 $ | 2026-06-24 | 34g | 0.06035 $ | 45,85% | n/a | 0.07966 $ | Due massimi simili a 0.09584 $ e 0.09169 $. Neckline circa 0.07809 $. Breakout neckline: 2026-06-24 (34 giorni fa). Stato: MATURO. Target teorico: 0.06035 $; progresso: 45,85%; prezzo sotto neckline. |
| Doppio minimo | CANDIDATO | 0 | rialzista | 0.07923 $ | n/a | n/a | 0.08886 $ | n/a | 13,26% | 0.07765 $ | Due minimi simili a 0.06961 $ e 0.07097 $. Neckline circa 0.07923 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 15 giorni. |
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

Generato: 2026-07-28 05:14 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [fractal_path_tracker.md](fractal_path_tracker.md)

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-07-28**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-01-12**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **73,28 $**
- Verdetto principale: **ANALOGIA DEBOLE / SCENARIO SECONDARIO**
- Somiglianza strutturale: **+64,21%**
- Aderenza live principale: **+67,56%**
- Errore medio live principale: **16,22%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE SOLO DI CONTESTO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **52**
- Osservazioni inclusive dal bottom: **53**
- Osservazioni da inizio programma/scanner: **26**
- Errore assoluto medio dal bottom: **11,03%**
- Errore assoluto medio da inizio programma: **16,22%**
- Gap firmato medio ultimi 7 giorni: **+9,76%**
- Errore assoluto medio ultimi 7 giorni: **10,16%**
- Gap ultimo giorno: **-1,41%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **-1,41%**
- Gap firmato medio 7g: **+9,76%**
- Errore assoluto medio 7g: **10,16%**
- Variazione recente gap: **-11,29%**
- Stato gap: **VICINO AL FRATTALE**
- Trend gap: **SOL si sta allontanando sotto il percorso ancorato**

Soglie operative del grafico:

- entro **±5%**: percorso vicino;
- tra **±5% e ±12%**: deviazione gestibile;
- oltre **±12%**: frattale non abbastanza aderente per conferma operativa;
- oltre **±18%**: disallineamento marcato.

## Ultimi giorni del confronto ancorato

|   Giorno | Data SOL   | Data BTC eq.   | SOL reale   | Percorso ancorato   | Gap firmato   | Fase                |
|---------:|:-----------|:---------------|:------------|:--------------------|:--------------|:--------------------|
| 43 | 2026-07-19 | 2023-01-03 | 76,36 $ | 65,71 $ | +16,21% | da inizio programma |
| 44 | 2026-07-20 | 2023-01-04 | 77,79 $ | 66,43 $ | +17,11% | da inizio programma |
| 45 | 2026-07-21 | 2023-01-05 | 78,11 $ | 66,32 $ | +17,77% | da inizio programma |
| 46 | 2026-07-22 | 2023-01-06 | 77,91 $ | 66,78 $ | +16,66% | da inizio programma |
| 47 | 2026-07-23 | 2023-01-07 | 75,86 $ | 66,79 $ | +13,58% | da inizio programma |
| 48 | 2026-07-24 | 2023-01-08 | 73,88 $ | 67,33 $ | +9,73% | da inizio programma |
| 49 | 2026-07-25 | 2023-01-09 | 74,43 $ | 67,74 $ | +9,87% | da inizio programma |
| 50 | 2026-07-26 | 2023-01-10 | 76,60 $ | 68,73 $ | +11,46% | da inizio programma |
| 51 | 2026-07-27 | 2023-01-11 | 76,60 $ | 70,65 $ | +8,43% | da inizio programma |
| 52 | 2026-07-28 | 2023-01-12 | 73,28 $ | 74,33 $ | -1,41% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-08-04 | 83,07 $ | 81,89 $ | 73,28 $ / 82,21 $ | no | n/a | n/a | n/a |
| 14g | 2026-08-11 | 90,73 $ | 89,45 $ | 73,28 $ / 89,78 $ | no | n/a | n/a | n/a |
| 21g | 2026-08-18 | 92,46 $ | 91,15 $ | 73,28 $ / 92,33 $ | no | n/a | n/a | n/a |
| 28g | 2026-08-25 | 85,95 $ | 84,73 $ | 73,28 $ / 92,33 $ | no | n/a | n/a | n/a |
| 35g | 2026-09-01 | 93,06 $ | 91,74 $ | 73,28 $ / 94,40 $ | no | n/a | n/a | n/a |
| 42g | 2026-09-08 | 94,33 $ | 93,00 $ | 73,28 $ / 96,42 $ | no | n/a | n/a | n/a |
| 49g | 2026-09-15 | 92,48 $ | 91,17 $ | 73,28 $ / 96,42 $ | no | n/a | n/a | n/a |
| 56g | 2026-09-22 | 80,21 $ | 79,08 $ | 73,28 $ / 96,42 $ | no | n/a | n/a | n/a |
| 63g | 2026-09-29 | 98,69 $ | 97,29 $ | 73,28 $ / 97,29 $ | no | n/a | n/a | n/a |
| 70g | 2026-10-06 | 111,61 $ | 110,03 $ | 73,28 $ / 110,03 $ | no | n/a | n/a | n/a |
| 77g | 2026-10-13 | 110,43 $ | 108,87 $ | 73,28 $ / 110,09 $ | no | n/a | n/a | n/a |
| 84g | 2026-10-20 | 110,47 $ | 108,91 $ | 73,28 $ / 110,60 $ | no | n/a | n/a | n/a |
| 91g | 2026-10-27 | 119,75 $ | 118,05 $ | 73,28 $ / 118,05 $ | no | n/a | n/a | n/a |
| 98g | 2026-11-03 | 111,27 $ | 109,69 $ | 73,28 $ / 118,39 $ | no | n/a | n/a | n/a |
| 105g | 2026-11-10 | 116,10 $ | 114,46 $ | 73,28 $ / 118,39 $ | no | n/a | n/a | n/a |
| 112g | 2026-11-17 | 113,64 $ | 112,03 $ | 73,28 $ / 118,39 $ | no | n/a | n/a | n/a |
| 119g | 2026-11-24 | 106,36 $ | 104,86 $ | 73,28 $ / 118,39 $ | no | n/a | n/a | n/a |
| 126g | 2026-12-01 | 105,70 $ | 104,20 $ | 73,28 $ / 118,39 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 14 | 35,71% | 3,36% | 12,63% |
| 14g | 7 | 28,57% | 6,46% | 8,18% |
| 21g | 0 | n/a | n/a | n/a |
| 28g | 0 | n/a | n/a | n/a |
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

Ultima lettura salvata: **2026-07-28** — SOL 73,28 $, gap -1,41%, somiglianza +64,21%.

Nel report principale lascio solo il link, così non diventa troppo lungo.

<!-- SOL_BTC_FRACTAL_HISTORY_END -->

</details>
<!-- COMPACT_SECTION_END:fractal_path -->

<!-- COMPACT_SECTION_START:exchange_microstructure -->
<details>
<summary><strong>🏦 Dati exchange, liquidità e leva</strong></summary>

<!-- EXCHANGE_MICROSTRUCTURE_START -->
# Dati exchange, liquidità e leva

Generato: 2026-07-28 05:14 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [exchange_microstructure_report.md](exchange_microstructure_report.md)

Questo modulo legge Kraken Futures, Bitget Futures e KuCoin Futures come nucleo derivati. OKX e Coinbase vengono raccolti come fonti ausiliarie non pesate.
Non modifica la formula matematica di RSI, Fibonacci o Wyckoff: controlla se quei segnali sono sostenuti da acquisti, vendite, OI, funding e liquidità.

**Limite importante:** questo nucleo non assume disponibile un feed pubblico completo delle liquidazioni. La componente liquidazioni resta neutrale; le zone future restano stime di pressione, non dati certi delle singole posizioni.

Diagnostica completa: [exchange_source_diagnostics.md](exchange_source_diagnostics.md)

## Sintesi

| Asset | Prezzo | Exchange | Segnale candidato | Peso Global | Bias exchange | Confidenza | Copertura | Funding 8h eq. | OI 24h | Taker flow (campione/4h) | Book 0,5% | Liq long campione | Liq short campione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 63.446 $ | 3 | 0 | 0 | LEGGERMENTE POSITIVA / NON PESATA | MEDIA | 100% | +0,0068% | -1,38% | 2,67 | +7,93% | 0 $ | 0 $ |
| SOL | 73,32 $ | 3 | 0 | 0 | LEGGERMENTE POSITIVA / NON PESATA | MEDIA | 100% | +0,0006% | -14,97% | 1,49 | -7,39% | 0 $ | 0 $ |
| DOGE | 0.07006 $ | 3 | 0 | 0 | MISTA / NEUTRALE | BASSA | 100% | +0,0076% | +1,18% | 0,95 | -4,54% | 0 $ | 0 $ |

Il segnale candidato è limitato a **±1**, ma il peso nel Global resta **0** finché il tracker a 7 giorni non raggiunge 30 controlli, almeno 55% di accuratezza e return corretto direzione positivo. Un singolo muro o funding non basta.

La colonna taker usa un campione recente nel primo run. Dopo almeno 3 fotografie distribuite su almeno 45 minuti viene sostituita automaticamente dalla media intraday 4h.

## Dati separati per exchange

| Asset | Exchange | Stato | Funding 8h eq. | Open interest | Taker flow | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | Kraken | OK | +0,0089% | 122,60 mln $ | 8,28 | +4,65% |
| BTC | Bitget | OK | +0,0091% | 2,27 mld $ | 0,97 | +7,01% |
| BTC | Kucoin | OK | +0,0100% | 1,49 mld $ | 3,77 | +7,13% |
| SOL | Kraken | OK | -0,0136% | 14,40 mln $ | 0,42 | -9,93% |
| SOL | Bitget | OK | -0,0089% | 332,85 mln $ | 0,10 | +2,95% |
| SOL | Kucoin | OK | -0,0094% | 222,06 mln $ | 0,74 | -11,15% |
| DOGE | Kraken | OK | -0,0148% | 3,58 mln $ | 1,31 | -22,79% |
| DOGE | Bitget | OK | -0,0087% | 87,68 mln $ | 1,25 | -3,43% |
| DOGE | Kucoin | OK | +0,0100% | 115,34 mln $ | 0,74 | -9,72% |

Kraken, Bitget e KuCoin contribuiscono a funding normalizzato, open interest, trade aggressivi e order book. Non viene inventato un long/short ratio pubblico né un feed completo delle liquidazioni.

## Conferme per indicatori tecnici

### BTC

- Score grezzo exchange: **+2,12**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 1, accuratezza +100,00%.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 2, bear 0, divergenze 0.
- Flusso taker/order book: **+1,75**.
- OI/funding/basis: **+0,00**.
- Affollamento long/short: **+0,00**.
- Liquidazioni: **NON PESATE / FEED COMPLETO NON ASSUNTO DISPONIBILE**.
- **Wyckoff:** Possibile accumulazione/spring sostenuto da pressione compratrice o assorbimento.
- **Fibonacci:** Livello Fibonacci soltanto testato: order book e taker flow non bastano ancora per dichiararlo tenuto o perso.
- **RSI:** RSI in zona non estrema o flusso exchange non abbastanza netto.
- **Pattern:** I pattern candidati restano non operativi: i dati exchange possono solo preparare la conferma.
- **Breakout/breakdown:** Prezzo non abbastanza vicino a un livello chiave o flusso non netto.
- **Mappa liquidità attuale:** muro bid: n/a; muro ask: n/a

![Microstruttura exchange BTC](exchange_microstructure_BTC.png)

### SOL

- Score grezzo exchange: **+2,88**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 1, accuratezza +0,00%.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 0, bear 2, divergenze 0.
- Flusso taker/order book: **+1,75**.
- OI/funding/basis: **+0,50**.
- Affollamento long/short: **+0,00**.
- Liquidazioni: **NON PESATE / FEED COMPLETO NON ASSUNTO DISPONIBILE**.
- **Wyckoff:** Possibile accumulazione/spring sostenuto da pressione compratrice o assorbimento.
- **Fibonacci:** Livello Fibonacci soltanto testato: order book e taker flow non bastano ancora per dichiararlo tenuto o perso. Confluenza tecnica dichiarata: neckline rialzista, invalidazione rialzista.
- **RSI:** RSI in zona non estrema o flusso exchange non abbastanza netto.
- **Pattern:** Doppio minimo maturo sostenuto dal flusso exchange.
- **Breakout/breakdown:** Prezzo non abbastanza vicino a un livello chiave o flusso non netto.
- **Mappa liquidità attuale:** muro bid: n/a; muro ask: n/a

![Microstruttura exchange SOL](exchange_microstructure_SOL.png)

### DOGE

- Score grezzo exchange: **+0,75**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 0, accuratezza n/a.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 1, bear 1, divergenze 1.
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
| BTC | +62,50% | +7,47% | 0 | n/a | RACCOLTA DATI | 0,00 | +62,50% | +7,47% |
| SOL | +70,00% | +7,64% | 0 | n/a | RACCOLTA DATI | 0,00 | +70,00% | +7,64% |
| DOGE | +67,50% | +6,65% | 0 | n/a | RACCOLTA DATI | 0,00 | +67,50% | +6,65% |

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

Generato: 2026-07-28 05:14 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [exchange_signal_tracker_report.md](exchange_signal_tracker_report.md)

Questo tracker verifica se il segnale candidato exchange ±1 anticipa correttamente la direzione del prezzo a 1/3/7/14/30 giorni.
Il peso Global resta 0 finché l'orizzonte 7g non ha almeno 30 controlli, accuratezza almeno 55% e return corretto direzione positivo. L'overlay a 30g ha un gate separato.

Controlli maturati completati in questa esecuzione: **12**.

## Ultime fotografie giornaliere

| Data | Asset | Prezzo | Versione | Calibrazione | Candidato | Peso Global | Score raw | Confidenza | Taker 4h | OI 24h | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-07-28 | BTC | 63.446,30 | V2.1.3 | OK | 0 | 0 | 2,12 | MEDIA | 2,67 | -1,38% | +7,93% |
| 2026-07-28 | DOGE | 0.07006 | V2.1.3 | OK | 0 | 0 | 0,75 | BASSA | 0,95 | +1,18% | -4,54% |
| 2026-07-28 | SOL | 73,32 | V2.1.3 | OK | 0 | 0 | 2,88 | MEDIA | 1,49 | -14,97% | -7,39% |
| 2026-07-27 | BTC | 65.281,70 | V2.1.3 | OK | 0 | 0 | 2,12 | MEDIA | 2,18 | -3,17% | +5,05% |
| 2026-07-27 | DOGE | 0.07287 | V2.1.3 | OK | 0 | 0 | 2,38 | MEDIA | 1,27 | +1,92% | +1,33% |
| 2026-07-27 | SOL | 76,31 | V2.1.3 | OK | 0 | 0 | 2,25 | MEDIA | 1,33 | -3,21% | +2,79% |
| 2026-07-26 | BTC | 64.469,20 | V2.1.3 | OK | 0 | 0 | -0,25 | BASSA | 0,80 | -0,46% | +7,17% |
| 2026-07-26 | DOGE | 0.07319 | V2.1.3 | OK | 0 | 0 | 1,62 | MEDIA | 1,35 | -5,19% | -2,50% |
| 2026-07-26 | SOL | 75,00 | V2.1.3 | OK | 0 | 0 | 2,25 | MEDIA | 2,52 | +0,37% | +5,87% |

## Accuratezza direzionale

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 1 | +100,00% | +1,59% | +1,07% | +1,84% | FEEDBACK RAPIDO |
| BTC | 3g | 1 | +100,00% | +1,47% | -1,13% | +3,82% | FEEDBACK RAPIDO |
| BTC | 7g | 1 | +100,00% | +1,35% | -1,18% | +3,82% | FEEDBACK RAPIDO |
| BTC | 14g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 30g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 1g | 1 | +0,00% | -0,43% | -0,39% | +0,39% | FEEDBACK RAPIDO |
| SOL | 3g | 1 | +0,00% | -3,12% | -3,63% | +0,73% | FEEDBACK RAPIDO |
| SOL | 7g | 1 | +0,00% | -6,27% | -6,64% | +0,73% | FEEDBACK RAPIDO |
| SOL | 14g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 30g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 1g | 2 | +100,00% | +3,08% | +1,70% | +3,12% | FEEDBACK RAPIDO |
| DOGE | 3g | 2 | +100,00% | +2,99% | -0,85% | +6,21% | FEEDBACK RAPIDO |
| DOGE | 7g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 14g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
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

**DOGE** — DOGE: i futures non danno una lettura chiara. Non si vede uno sbilanciamento forte né long né short. Qui pesa di più il report frattale.

| Asset | Prezzo | Funding | OI 24h | Long/Short | Lettura futures | Forza |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 63.392 $ | -0.0045% | -4.76% | 1.91 | Misto | 1/5 |
| SOL | 73,28 $ | -0.0097% | +2.66% | 1.98 | Misto | 2/5 |
| DOGE | 0.06996 $ | -0.0017% | -23.69% | 3.07 | Misto | 1/5 |

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

Generato: 2026-07-28 05:14 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [rsi_multitimeframe_divergence_report.md](rsi_multitimeframe_divergence_report.md)

Il modulo confronta prezzo e RSI 14 sui pivot confermati **daily e weekly**. Riconosce divergenze regolari e nascoste, segnali in formazione, invalidazioni e semplice conferma del momentum.

**Peso operativo: 0.** Non modifica il Global Confluence, non cambia le soglie del Paper Trading e non apre né blocca operazioni. I risultati vengono misurati prima di qualsiasi futura decisione sul peso.

## Sintesi corrente

| Asset   | Daily                      | Stato D       | Weekly              | Stato W    | Lettura weekly                                                                                                                |   Peso |
|:--------|:---------------------------|:--------------|:--------------------|:-----------|:------------------------------------------------------------------------------------------------------------------------------|-------:|
| BTC     | Bullish regolare           | CONFERMATA    | Bullish regolare    | CONFERMATA | Bullish regolare confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto. |      0 |
| SOL     | Misto / nessuna divergenza | CONTESTO      | Hidden bearish      | CONFERMATA | Hidden bearish confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto.   |      0 |
| DOGE    | Hidden bearish             | IN_FORMAZIONE | Conferma ribassista | CONTESTO   | Prezzo e RSI stanno scendendo insieme: momentum ribassista confermato, nessuna bullish divergence attiva.                     |      0 |

## Dettaglio dei pivot

| Asset   | TF   | Tipo                       | Stato         | Prezzo / RSI      | Pivot confrontati                                                   | Δ prezzo contesto   | Δ RSI contesto   |   Peso |
|:--------|:-----|:---------------------------|:--------------|:------------------|:--------------------------------------------------------------------|:--------------------|:-----------------|-------:|
| BTC     | 1D   | Bullish regolare           | CONFERMATA    | 63.381 $ / 46,41  | 2026-06-25 58.076 $ / RSI 30,46 → 2026-07-01 57.748 $ / RSI 37,26   | n/a                 | n/a              |      0 |
| BTC     | 1W   | Bullish regolare           | CONFERMATA    | 63.381 $ / 38,74  | 2026-06-07 59.109 $ / RSI 34,23 → 2026-07-05 57.748 $ / RSI 38,20   | n/a                 | n/a              |      0 |
| SOL     | 1D   | Misto / nessuna divergenza | CONTESTO      | 73,27 $ / 42,87   | n/a                                                                 | -2,13%              | -3,62            |      0 |
| SOL     | 1W   | Hidden bearish             | CONFERMATA    | 73,27 $ / 38,27   | 2026-05-17 98,27 $ / RSI 38,29 → 2026-07-05 83,81 $ / RSI 42,25     | n/a                 | n/a              |      0 |
| DOGE    | 1D   | Hidden bearish             | IN_FORMAZIONE | 0.06996 $ / 39,22 | 2026-07-04 0.07923 $ / RSI 41,65 → 2026-07-26 0.07380 $ / RSI 47,51 | n/a                 | n/a              |      0 |
| DOGE    | 1W   | Conferma ribassista        | CONTESTO      | 0.06996 $ / 32,69 | n/a                                                                 | -14,86%             | -2,38            |      0 |

### BTC

- **1D — Bullish regolare / CONFERMATA**: Bullish regolare confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto.
- **1W — Bullish regolare / CONFERMATA**: Bullish regolare confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto.

### SOL

- **1D — Misto / nessuna divergenza / CONTESTO**: Misto / nessuna divergenza. Non esiste una divergenza confermata sugli ultimi pivot.
- **1W — Hidden bearish / CONFERMATA**: Hidden bearish confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto.

### DOGE

- **1D — Hidden bearish / IN_FORMAZIONE**: Hidden bearish in formazione: il secondo estremo non è ancora un pivot confermato. Peso operativo sempre 0.
- **1W — Conferma ribassista / CONTESTO**: Prezzo e RSI stanno scendendo insieme: momentum ribassista confermato, nessuna bullish divergence attiva.

## Tracker live delle divergenze confermate

Viene salvato un solo evento per combinazione di asset, timeframe, tipo e coppia di pivot. Gli esiti vengono controllati dopo 30, 60, 90 e 180 giorni.

- Eventi indipendenti salvati: **5**.
- Soglie di lettura: **30 / 60 / 100 controlli**.
- Anche oltre le soglie il peso resta **0** finché non viene presa una decisione esplicita.

_Nessun controllo maturato: il tracker ha appena iniziato a raccogliere dati._

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

Generato: 2026-07-28 05:14 UTC


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

| Asset   | Prezzo   |   Punteggio | Verdetto           | Trend            | Momentum        | Struttura                                             |   Pattern score | Fibonacci      | Pattern rialzista         | Pattern ribassista         | Supporto   | Resistenza   |
|:--------|:---------|------------:|:-------------------|:-----------------|:----------------|:------------------------------------------------------|----------------:|:---------------|:--------------------------|:---------------------------|:-----------|:-------------|
| BTC | 63.392 $ | -3 | DEBOLE | Trend ribassista | Momentum debole | Volatilità in espansione | 0 | 0 / TESTATO | Doppio minimo / CANDIDATO | Doppio massimo / CANDIDATO | 57.748 | 66.910 |
| SOL | 73,28 $ | -7 | RIBASSISTA TECNICO | Trend ribassista | Momentum debole | Compressione / triangolo | +1 | 0 / TESTATO | Doppio minimo / MATURO | Doppio massimo / CANDIDATO | 64,42 | 78,73 |
| DOGE | 0.06996 $ | -9 | RIBASSISTA TECNICO | Trend ribassista | Momentum debole | Struttura ribassista con massimi e minimi decrescenti | -1 | 0 / NON ATTIVO | Doppio minimo / CANDIDATO | Triplo massimo / MATURO | 0.06961 | 0.07923 |

## Riepilogo ciclo di vita pattern

| Asset   | Doppio minimo   | Triplo minimo   | Adam/Eve Bottom                 | Doppio massimo   | Triplo massimo   | Adam/Eve Top                 |   Punteggio pattern |
|:--------|:----------------|:----------------|:--------------------------------|:-----------------|:-----------------|:-----------------------------|--------------------:|
| BTC | CANDIDATO | CANDIDATO | Adam and Eve Bottom — CANDIDATO | CANDIDATO | CANDIDATO | Adam and Eve Top — CANDIDATO | 0 |
| SOL | MATURO | CANDIDATO | Adam and Eve Bottom — CANDIDATO | CANDIDATO | CANDIDATO | Adam and Eve Top — CANDIDATO | 1 |
| DOGE | CANDIDATO | ASSENTE | Adam and Eve Bottom — CANDIDATO | ASSENTE | MATURO | Eve and Adam Top — MATURO | -1 |

## Indicatori tecnici

| Asset   |   RSI 14 |   Istogramma MACD | MA20    | MA50    | MA200   | Pendenza MA50 20g   | Pendenza MA200 60g   | Rendimento 30g   | Rendimento 90g   |
|:--------|---------:|------------------:|:--------|:--------|:--------|:--------------------|:---------------------|:-----------------|:-----------------|
| BTC | 46.45 | -43.4672 | 64.312 | 63.267 | 71.992 | -4,03% | -9,80% | 6,48% | -16,34% |
| SOL | 42.89 | -0.4269 | 76,37 | 74,11 | 87,72 | -1,23% | -16,58% | 2,76% | -11,74% |
| DOGE | 39.22 | 0.00025 | 0.07235 | 0.07708 | 0.09637 | -10,81% | -16,09% | -4,29% | -32,74% |

## Dettaglio asset

### BTC

- Prezzo: **63.392 $**
- Punteggio tecnico: **-3 / 12**
- Verdetto: **DEBOLE**
- Trend: **Trend ribassista** (-3)
- Momentum: **Momentum debole** (-3)
- Volume: **Volume neutrale** (0)
- Struttura: **Volatilità in espansione** (0)
  - Dettaglio struttura: Ultimi minimi: 5.808e+04 -> 5.775e+04. Ultimi massimi: 6.551e+04 -> 6.691e+04.
- Divergenza: **Divergenza rialzista RSI** (2)
- Fase Wyckoff candidata: **Possibile accumulazione** (1)
  - Dettaglio Wyckoff: Prezzo sotto MA200, vicino alla parte bassa del range a 120 giorni, RSI 46.4.
- Fibonacci automatico: **TESTATO** (0)
  - Swing UP 2026-07-01 57.748 -> 2026-07-21 66.910; livello più vicino 38.2% a 63.410; stato TESTATO; confluenza: nessuna confluenza indipendente.
- Punteggio pattern: **0**
  - rialzista dominante: Doppio minimo (CANDIDATO, 0); ribassista dominante: Doppio massimo (CANDIDATO, 0).
- Supporto più vicino: **57.748**
- Resistenza più vicina: **66.910**

Pattern classici e ciclo di vita:

- Doppio minimo: **CANDIDATO** (0)
  - Due minimi simili vicino a 57.748 tra 2026-06-05 e 2026-07-01. Neckline stimata: 67.248. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 27 giorni.
  - neckline 67.248; target 76.748; distanza dalla neckline 6,08%; prezzo sotto neckline.
- Triplo minimo: **CANDIDATO** (0)
  - Tre minimi simili vicino a 57.748 dal 2026-06-05 al 2026-07-01. Neckline stimata: 67.248. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 27 giorni.
  - neckline 67.248; target 76.748; distanza dalla neckline 6,08%; prezzo sotto neckline.
- Adam and Eve Bottom: **CANDIDATO** (0)
  - Pattern Adam and Eve Bottom vicino a 57.748 dal 2026-06-05 al 2026-07-01. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 67.248. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 27 giorni.
  - neckline 67.248; target 76.748; distanza dalla neckline 6,08%; prezzo sotto neckline.
- Doppio massimo: **CANDIDATO** (0)
  - Due massimi simili vicino a 67.248 tra 2026-06-15 e 2026-07-21. Neckline ribassista stimata: 57.748. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 7 giorni.
  - neckline 57.748; target 48.247; distanza dalla neckline 9,77%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 66.910 dal 2026-06-22 al 2026-07-21. Neckline ribassista stimata: 57.748. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 7 giorni.
  - neckline 57.748; target 48.585; distanza dalla neckline 9,77%; prezzo sopra neckline.
- Adam and Eve Top: **CANDIDATO** (0)
  - Pattern Adam and Eve Top vicino a 67.248 dal 2026-06-15 al 2026-07-21. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 57.748. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 7 giorni.
  - neckline 57.748; target 48.247; distanza dalla neckline 9,77%; prezzo sopra neckline.

### SOL

- Prezzo: **73,28 $**
- Punteggio tecnico: **-7 / 12**
- Verdetto: **RIBASSISTA TECNICO**
- Trend: **Trend ribassista** (-3)
- Momentum: **Momentum debole** (-3)
- Volume: **Volume da distribuzione** (-2)
- Struttura: **Compressione / triangolo** (0)
  - Dettaglio struttura: Ultimi minimi: 64.42 -> 73.4. Ultimi massimi: 78.88 -> 78.73.
- Divergenza: **Divergenza ribassista nascosta RSI** (-1)
- Fase Wyckoff candidata: **Possibile accumulazione** (1)
  - Dettaglio Wyckoff: Prezzo sotto MA200, vicino alla parte bassa del range a 120 giorni, RSI 42.9.
- Fibonacci automatico: **TESTATO** (0)
  - Swing UP 2026-06-06 60,41 -> 2026-07-21 78,73; livello più vicino 23.6% a 74,40; stato TESTATO; confluenza: neckline rialzista, invalidazione rialzista.
- Punteggio pattern: **+1**
  - rialzista dominante: Doppio minimo (MATURO, +1); ribassista dominante: Doppio massimo (CANDIDATO, 0).
- Supporto più vicino: **64,42**
- Resistenza più vicina: **78,73**

Pattern classici e ciclo di vita:

- Doppio minimo: **MATURO** (+1)
  - Due minimi simili vicino a 60,41 tra 2026-06-06 e 2026-06-25. Neckline stimata: 75,94. Breakout neckline: 2026-07-01 (27 giorni fa). Stato: MATURO. Target teorico: 91,46; progresso corrente: -17,13%. Relazione prezzo/neckline: sotto neckline.
  - neckline 75,94; target 91,46; breakout 2026-07-01 (27g); progresso -17,13%; prezzo sotto neckline.
- Triplo minimo: **CANDIDATO** (0)
  - Tre minimi simili vicino a 81,63 dal 2026-04-29 al 2026-05-23. Neckline stimata: 98,27. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 66 giorni.
  - neckline 98,27; target 114,91; distanza dalla neckline 34,10%; prezzo sotto neckline.
- Adam and Eve Bottom: **CANDIDATO** (0)
  - Pattern Adam and Eve Bottom vicino a 67,92 dal 2026-06-19 al 2026-07-17. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 83,81. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 11 giorni.
  - neckline 83,81; target 99,70; distanza dalla neckline 14,37%; prezzo sotto neckline.
- Doppio massimo: **CANDIDATO** (0)
  - Due massimi simili vicino a 78,73 tra 2026-06-15 e 2026-07-21. Neckline ribassista stimata: 64,42. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 7 giorni.
  - neckline 64,42; target 50,11; distanza dalla neckline 13,76%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 78,88 dal 2026-06-15 al 2026-07-21. Neckline ribassista stimata: 64,42. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 7 giorni.
  - neckline 64,42; target 49,96; distanza dalla neckline 13,76%; prezzo sopra neckline.
- Adam and Eve Top: **CANDIDATO** (0)
  - Pattern Adam and Eve Top vicino a 78,73 dal 2026-06-15 al 2026-07-21. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 64,42. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 7 giorni.
  - neckline 64,42; target 50,11; distanza dalla neckline 13,76%; prezzo sopra neckline.

### DOGE

- Prezzo: **0.06996 $**
- Punteggio tecnico: **-9 / 12**
- Verdetto: **RIBASSISTA TECNICO**
- Trend: **Trend ribassista** (-3)
- Momentum: **Momentum debole** (-2)
- Volume: **Volume da distribuzione** (-1)
- Struttura: **Struttura ribassista con massimi e minimi decrescenti** (-2)
  - Dettaglio struttura: Ultimi minimi: 0.07107 -> 0.07097. Ultimi massimi: 0.09169 -> 0.07923.
- Divergenza: **Divergenza ribassista nascosta RSI** (-1)
- Fase Wyckoff candidata: **Possibile accumulazione** (1)
  - Dettaglio Wyckoff: Prezzo sotto MA200, vicino alla parte bassa del range a 120 giorni, RSI 39.2.
- Fibonacci automatico: **NON ATTIVO** (0)
  - Swing DOWN 2026-05-14 0.11825 -> 2026-07-13 0.07097; livello più vicino 23.6% a 0.08213; stato NON ATTIVO; confluenza: nessuna confluenza indipendente.
- Punteggio pattern: **-1**
  - rialzista dominante: Doppio minimo (CANDIDATO, 0); ribassista dominante: Triplo massimo (MATURO, -1).
- Supporto più vicino: **0.06961**
- Resistenza più vicina: **0.07923**

Pattern classici e ciclo di vita:

- Doppio minimo: **CANDIDATO** (0)
  - Due minimi simili vicino a 0.06961 tra 2026-06-30 e 2026-07-13. Neckline stimata: 0.07923. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 15 giorni.
  - neckline 0.07923; target 0.08886; distanza dalla neckline 13,26%; prezzo sotto neckline.
- Triplo minimo: **ASSENTE** (0)
- Adam and Eve Bottom: **CANDIDATO** (0)
  - Pattern Adam and Eve Bottom vicino a 0.06961 dal 2026-06-30 al 2026-07-13. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 0.07923. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 15 giorni.
  - neckline 0.07923; target 0.08886; distanza dalla neckline 13,26%; prezzo sotto neckline.
- Doppio massimo: **ASSENTE** (0)
- Triplo massimo: **MATURO** (-1)
  - Tre massimi simili vicino a 0.09772 dal 2026-03-25 al 2026-06-12. Neckline ribassista stimata: 0.07809. Breakout neckline: 2026-06-24 (34 giorni fa). Stato: MATURO. Target teorico: 0.05847; progresso corrente: 41,45%. Relazione prezzo/neckline: sotto neckline.
  - neckline 0.07809; target 0.05847; breakout 2026-06-24 (34g); progresso 41,45%; prezzo sotto neckline.
- Eve and Adam Top: **MATURO** (-1)
  - Pattern Eve and Adam Top vicino a 0.09584 dal 2026-04-07 al 2026-06-12. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 0.07809. Breakout neckline: 2026-06-24 (34 giorni fa). Stato: MATURO. Target teorico: 0.06035; progresso corrente: 45,85%. Relazione prezzo/neckline: sotto neckline.
  - neckline 0.07809; target 0.06035; breakout 2026-06-24 (34g); progresso 45,85%; prezzo sotto neckline.

## Fibonacci automatico

Il modulo seleziona uno swing recente tramite pivot confermati. Un semplice tocco vale 0: Fibonacci pesa al massimo ±1 soltanto quando il livello è tenuto, perso, recuperato o respinto e coincide con almeno un livello tecnico indipendente.

| Asset   | Swing                         | 23,6%   | 38,2%   | 50,0%   | 61,8%   | 78,6%   | Livello vicino   | Stato      | Confluenza                                  |   Score |
|:--------|:------------------------------|:--------|:--------|:--------|:--------|:--------|:-----------------|:-----------|:--------------------------------------------|--------:|
| BTC | UP 2026-07-01 -> 2026-07-21 | 64.748 | 63.410 | 62.329 | 61.248 | 59.708 | 38.2% / 63.410 | TESTATO | nessuna confluenza indipendente | 0 |
| SOL | UP 2026-06-06 -> 2026-07-21 | 74,40 | 71,73 | 69,57 | 67,41 | 64,33 | 23.6% / 74,40 | TESTATO | neckline rialzista, invalidazione rialzista | 0 |
| DOGE | DOWN 2026-05-14 -> 2026-07-13 | 0.08213 | 0.08904 | 0.09461 | 0.10019 | 0.10814 | 23.6% / 0.08213 | NON ATTIVO | nessuna confluenza indipendente | 0 |

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

- **BTC**: 0/30 previsioni controllate su 26 fatte. Stato: **RACCOLTA DATI**.
- **SOL**: 0/30 previsioni controllate su 26 fatte. Stato: **RACCOLTA DATI**.
- **DOGE**: 0/30 previsioni controllate su 26 fatte. Stato: **RACCOLTA DATI**.

| Asset | Previsioni fatte | Controllate | Progresso | In attesa | Stato | Prossimo controllo |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 26 | 0 | 0/30 [░░░░░░░░░░] | 26 | RACCOLTA DATI | 2026-08-02 / tra 5 giorni |
| SOL | 26 | 0 | 0/30 [░░░░░░░░░░] | 26 | RACCOLTA DATI | 2026-08-02 / tra 5 giorni |
| DOGE | 26 | 0 | 0/30 [░░░░░░░░░░] | 26 | RACCOLTA DATI | 2026-08-02 / tra 5 giorni |

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

Generato: 2026-07-28 05:15 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [data_quality_coherence_report.md](data_quality_coherence_report.md)

Questo controllo non modifica punteggi o decisioni. Verifica che tutti i moduli usino lo stesso prezzo corrente e che le nuove regole Technical/Classic Visual siano integre.

## Stato finale: **OK**

## Prezzo unico per modulo

| Modulo                  | Asset   | Campo             | Stato   | Prezzo snapshot   | Prezzo modulo   | Differenza   |
|:------------------------|:--------|:------------------|:--------|:------------------|:----------------|:-------------|
| Scanner                 | BTC     | current_price     | OK      | 63.392 $          | 63.392 $        | +0,0000%     |
| Scanner                 | DOGE    | current_price     | OK      | 0.06996 $         | 0.06996 $       | -0,0000%     |
| Scanner                 | SOL     | current_price     | OK      | 73,28 $           | 73,28 $         | +0,0000%     |
| Scanner Forecast        | BTC     | current_price     | OK      | 63.392 $          | 63.392 $        | +0,0000%     |
| Scanner Forecast        | SOL     | current_price     | OK      | 73,28 $           | 73,28 $         | +0,0000%     |
| Scanner Forecast        | DOGE    | current_price     | OK      | 0.06996 $         | 0.06996 $       | -0,0000%     |
| Technical Structure     | BTC     | price             | OK      | 63.392 $          | 63.392 $        | +0,0000%     |
| Technical Structure     | SOL     | price             | OK      | 73,28 $           | 73,28 $         | +0,0000%     |
| Technical Structure     | DOGE    | price             | OK      | 0.06996 $         | 0.06996 $       | -0,0000%     |
| Classic Technical       | BTC     | price             | OK      | 63.392 $          | 63.392 $        | +0,0000%     |
| Classic Technical       | SOL     | price             | OK      | 73,28 $           | 73,28 $         | +0,0000%     |
| Classic Technical       | DOGE    | price             | OK      | 0.06996 $         | 0.06996 $       | -0,0000%     |
| Classic Visual          | BTC     | price             | OK      | 63.392 $          | 63.392 $        | +0,0000%     |
| Classic Visual          | SOL     | price             | OK      | 73,28 $           | 73,28 $         | +0,0000%     |
| Classic Visual          | DOGE    | price             | OK      | 0.06996 $         | 0.06996 $       | -0,0000%     |
| Exchange Microstructure | BTC     | price             | OK      | 63.392 $          | 63.446 $        | +0,0862%     |
| Exchange Microstructure | SOL     | price             | OK      | 73,28 $           | 73,32 $         | +0,0519%     |
| Exchange Microstructure | DOGE    | price             | OK      | 0.06996 $         | 0.07006 $       | +0,1429%     |
| RSI top-cycle           | SOL     | current_price     | OK      | 73,28 $           | 73,28 $         | +0,0000%     |
| RSI top-cycle           | SOL     | current_price     | OK      | 73,28 $           | 73,28 $         | +0,0000%     |
| Frattale BTC/SOL        | SOL     | sol_current_price | OK      | 73,28 $           | 73,28 $         | +0,0000%     |
| Fractal path            | SOL     | current_price     | OK      | 73,28 $           | 73,28 $         | +0,0000%     |

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

Generato: 2026-07-29T04:17:34+00:00

- Modalità: **SOLO PAPER TRADING**
- Asset: **SOL spot**
- Leva: **nessuna (1x)**
- Capitale iniziale separato: **€40.000,00**
- Fonte mercato: **KUCOIN_PUBLIC_API**; nuove entrate: **CONSENTITE**

| Equity | Cash | SOL | Prezzo | Rendimento | Realizzato | Commissioni | Max DD | Operazioni |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €39.527,41 | €4.024,85 | 486.149894 | 73.0280 | -1.18% | €0,00 | €35,98 | 4.35% | 6 |

**Ultima decisione:** HOLD — Prezzo dentro la fascia neutrale.

Bande 4H: L2 69.9583 · L1 72.0488 · media 74.6620 · U1 77.2751 · U2 79.3657.

> Questo portafoglio non condivide capitale, posizioni o statistiche con il paper trading da €10.000.
<!-- SOL_SPOT_ADAPTIVE_END -->
