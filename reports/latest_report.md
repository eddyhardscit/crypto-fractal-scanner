<!-- COMPACT_REPORT_HEADER_START -->
> **Vista compatta:** Decisione operativa, Global Confluence e cambiamenti giornalieri restano aperti. Tocca il titolo di una sezione per mostrare o nascondere i dettagli.  
> Tutte le tabelle e tutti i dati restano nel file: copiando il Markdown raw viene copiato tutto.
<!-- COMPACT_REPORT_HEADER_END -->

<!-- COMPACT_SECTION_START:decision -->
<details open>
<summary><strong>🧭 Decisione operativa — da leggere per prima</strong></summary>

<!-- DECISION_REPORT_START -->

# Decisione operativa sintetica

Generato: 2026-07-21 05:14 UTC

Report separato completo: [decision_report.md](decision_report.md)

Sintesi automatica dello scanner: l'azione spot viene copiata direttamente dal Global Confluence; long, short e rischio restano filtri separati e più prudenti.

| Asset | Global | Direzione | Spot | Long leva | Short leva | Max long | Max short | Rischio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +3 | BULLISH | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE | NO LONG A LEVA / ATTENDI SOPRA 67.248 $ | NO SHORT | nessuna | nessuna | MEDIO |
| SOL | +1 | NEUTRALE / INCERTO | HOLD LEGGERO / ATTESA CONFERME | NO LONG A LEVA | NO SHORT | nessuna | nessuna | MOLTO ALTO |
| DOGE | -6 | BEARISH | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE | NO LONG A LEVA | SHORT SOLO DOPO SPIKE | nessuna | max 1x-2x isolated | MOLTO ALTO |

## Lettura immediata

- **BTC**: Global = **+3**, spot = **ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE**, long = **NO LONG A LEVA / ATTENDI SOPRA 67.248 $**, short = **NO SHORT**, rischio = **MEDIO**.
- **SOL**: Global = **+1**, spot = **HOLD LEGGERO / ATTESA CONFERME**, long = **NO LONG A LEVA**, short = **NO SHORT**, rischio = **MOLTO ALTO**.
- **DOGE**: Global = **-6**, spot = **STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE**, long = **NO LONG A LEVA**, short = **SHORT SOLO DOPO SPIKE**, rischio = **MOLTO ALTO**.

## Dettaglio logica

### BTC

- Global Confluence: **+3**
- Confluenza: **MODERATAMENTE POSITIVA**
- Bias Global: **Costruttivo prudente**
- Direzione decisionale: **BULLISH**
- Azione spot dal Global: **ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE**
- Long leva: **NO LONG A LEVA / ATTENDI SOPRA 67.248 $**
- Short leva: **NO SHORT**
- Rischio: **MEDIO**
- Conferme: Prima resistenza sopra 65.508; conferma del doppio minimo sopra 67.248.
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
- Conferme: Doppio minimo maturo finché mantiene 75,94; nuova conferma tecnica sopra 78,88; milestone analogiche 98,30 / 115,29, valide soltanto se rientra anche il gap frattale.
- Invalidazioni: Allarmi sotto 74,27 / 64,42 / 62,19.

### DOGE

- Global Confluence: **-6**
- Confluenza: **NEGATIVA**
- Bias Global: **Ribassista**
- Direzione decisionale: **BEARISH**
- Azione spot dal Global: **STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE**
- Long leva: **NO LONG A LEVA**
- Short leva: **SHORT SOLO DOPO SPIKE**
- Rischio: **MOLTO ALTO**
- Conferme: Sopra 0.07923 migliora; sopra 0.07966 viene invalidato il pattern ribassista dominante.
- Invalidazioni: Sotto 0.07097 il rischio ribassista aumenta.

## Nota semplice

- **Spot** = usa la stessa azione del Global Confluence, senza una seconda mappatura che possa produrre frasi diverse.
- **Zona alta storica** = zona dove non inseguire troppo; può essere zona da prendere profitto.
- **Zona bassa storica** = zona di rischio; con leva la liquidazione non dovrebbe stare lì vicino.
- **BTC leva** = nessun long a leva finché il prezzo snapshot non supera **67.248 $**; sotto quella soglia resta solo l'azione spot indicata dal Global.
- **Lifecycle EMA200** = per SOL resta solo contesto, peso Global 0; score interno 4; EMA200 circa 112,78 $; upside verso EMA200 +44,19%. Non autorizza leva e non aggiunge punti automatici.
- **NO LONG** non significa automaticamente **SHORT**. Lo short ha senso solo se il quadro è bearish o se lo spike viene spesso scaricato.
- Per SOL, se il Global è da **+3 in su**, la decisione non deve diventare bearish solo perché lo scanner grezzo a 30 giorni è incerto.

<!-- DECISION_REPORT_END -->

<!-- PAPER_TRADING_START -->
# Paper trading automatico KuCoin

Generato: 2026-07-21T05:14:52+00:00


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [paper_trading_report.md](paper_trading_report.md)

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-07-21T05:08:24+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-07-21T05:08:24+00:00 | 2026-07-21T05:08:25+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-07-21T04:45:00+00:00 | 2026-07-21T04:45:00+00:00 | 8,5 min | 25,0 min | OK |
| 60m | 12 | 2026-07-21T04:00:00+00:00 | 2026-07-21T04:00:00+00:00 | 8,5 min | 45,0 min | OK |
| 240m | 12 | 2026-07-21T00:00:00+00:00 | 2026-07-21T00:00:00+00:00 | 1,14 h | 1,00 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Benchmark trend following EMA 1H | ADA | 60m | LONG | 6,24 | 5,00 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 No Esports V1 | ETH | 60m | LONG | 6,07 | 4,50 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 No Esports V1 | ADA | 60m | LONG | 6,24 | 4,50 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 Long Only V1 | ETH | 60m | LONG | 6,07 | 4,50 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 Long Only V1 | ADA | 60m | LONG | 6,24 | 4,50 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 Cap75 V1 | ETH | 60m | LONG | 6,07 | 4,50 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 Cap75 V1 | ADA | 60m | LONG | 6,24 | 4,50 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida 1H V3 Filtered | ADA | 60m | LONG | 6,24 | 4,50 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Tp2 V1 | ETH | 60m | LONG | 6,07 | 4,50 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Tp2 V1 | ADA | 60m | LONG | 6,24 | 4,50 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast No Pepe V1 | ETH | 60m | LONG | 6,07 | 4,50 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast No Pepe V1 | ADA | 60m | LONG | 6,24 | 4,50 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Score 6 75 V1 | ETH | 60m | LONG | 6,07 | 6,00 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Score 6 75 V1 | ADA | 60m | LONG | 6,24 | 6,00 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Bilanciata 1H V3 Filtered | ADA | 60m | LONG | 6,24 | 6,00 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Principale 4H | ACE | 240m | LONG | 8,25 | 6,00 | 0,00 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | BANK | 240m | LONG | 7,75 | 6,00 | 0,00 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | ETH | 240m | LONG | 7,01 | 6,00 | 0,00 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | ADA | 240m | LONG | 6,94 | 6,00 | 0,00 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | PEPE | 240m | LONG | 6,80 | 6,00 | 0,00 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | AKE | 240m | LONG | 6,25 | 6,00 | 0,00 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | XRP | 240m | LONG | 4,82 | 6,00 | 1,18 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | BTC | 240m | LONG | 4,75 | 6,00 | 1,25 | STALE_CANDLE | 1,14 h | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | ZEC | 240m | LONG | 4,43 | 6,00 | 1,57 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | DOGE | 240m | SHORT | -4,18 | 6,00 | 1,82 | STALE_CANDLE | 1,14 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | SOL | 240m | LONG | 3,78 | 6,00 | 2,22 | STALE_CANDLE | 1,14 h | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | HYPE | 240m | LONG | 0,05 | 6,00 | 5,95 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Bilanciata 1H V1 | XRP | 60m | LONG | 7,50 | 5,00 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida 1H V1 | XRP | 60m | LONG | 7,50 | 4,50 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Score 6 75 V1 | XRP | 60m | LONG | 7,50 | 6,00 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast No Pepe V1 | XRP | 60m | LONG | 7,50 | 4,50 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Tp2 V1 | XRP | 60m | LONG | 7,50 | 4,50 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 Cap75 V1 | XRP | 60m | LONG | 7,50 | 4,50 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 Long Only V1 | XRP | 60m | LONG | 7,50 | 4,50 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 No Esports V1 | XRP | 60m | LONG | 7,50 | 4,50 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.884,55 | -1,15% | €-115,45 | €3.000,00 | -3,85% | 4 | 16 | 31,25% | 0,81 | 4,26% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 16 | 235 | CAMPIONE INSUFFICIENTE | 30 (mancano 14) |

- Trade del Principale 4H chiusi: **16**; win rate **31,25%**; profit factor **0,81**.
- Expectancy: **€-6,29** per trade; P&L netto: **€-100,68**; max drawdown: **4,26%**.
- Valutazione: **Servono altri eventi indipendenti prima di trarre conclusioni.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 4 | €9.884,55 | €1.552,19 | €4.656,58 | €197,65 | €-13,85 |
| TEST | Scanner Top 5 + forza BTC 1H | 3 | €10.453,88 | €3.363,52 | €6.727,04 | €103,50 | €71,48 |
| TEST | Scanner Top 5 Long 1H | 3 | €10.448,28 | €3.644,27 | €7.288,54 | €155,12 | €124,18 |
| TEST | Combo Adaptive | 3 | €10.240,79 | €2.743,84 | €5.487,67 | €153,54 | €-1,84 |
| TEST | Bilanciata 1H V3 Filtered | 4 | €10.236,65 | €3.152,26 | €9.456,78 | €51,19 | €122,30 |
| TEST | Combo Mean Reversion | 0 | €10.195,13 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Forza relativa 1H V2 | 4 | €10.193,67 | €1.522,73 | €3.045,46 | €151,81 | €-33,79 |
| TEST | Benchmark Donchian breakout 1H | 2 | €10.191,93 | €1.589,62 | €3.179,25 | €102,21 | €-26,07 |
| TEST | Benchmark Bollinger mean reversion 1H | 0 | €10.152,11 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Ampia 4H | 4 | €10.131,56 | €1.846,89 | €3.693,78 | €200,81 | €-7,34 |
| TEST | Bilanciata 1H V1 | 4 | €10.124,13 | €2.802,69 | €8.408,06 | €151,29 | €47,52 |
| TEST | Scanner Top5 Btc Runner25 V1 | 3 | €10.100,56 | €3.909,27 | €7.818,54 | €149,97 | €105,25 |
| TEST | Scanner Top5 Btc Tp3 V1 | 3 | €10.100,56 | €3.909,27 | €7.818,54 | €149,97 | €105,25 |
| TEST | Forza relativa 1H V1 | 4 | €10.091,49 | €2.508,00 | €5.016,01 | €151,36 | €-1,81 |
| TEST | Scanner Top5 Btc Btc Le3 V1 | 3 | €10.078,16 | €3.985,76 | €7.971,52 | €149,97 | €82,94 |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | 3 | €10.078,16 | €3.985,76 | €7.971,52 | €149,97 | €82,94 |
| TEST | Scanner Top5 Btc Mfe V1 | 3 | €10.074,45 | €4.852,44 | €9.704,89 | €99,98 | €80,68 |
| TEST | Btc Bollinger 1H | 0 | €10.068,69 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Trend | 3 | €10.054,14 | €1.639,93 | €3.279,86 | €150,82 | €-1,63 |
| TEST | Sol Donchian 1H | 1 | €10.022,50 | €1.127,14 | €3.381,43 | €49,98 | €29,06 |
| TEST | Eth Bollinger 1H | 0 | €10.015,45 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 1H | 1 | €10.014,82 | €1.001,44 | €3.004,32 | €49,95 | €25,82 |
| TEST | Combo Adaptive Long Only V1 | 2 | €10.011,18 | €1.376,57 | €2.753,14 | €100,00 | €13,31 |
| TEST | Sol Adaptive 1H | 1 | €10.005,50 | €1.000,51 | €3.001,52 | €49,91 | €25,79 |
| TEST | Rapida 1H V2 | 0 | €10.004,31 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 4H | 1 | €10.002,28 | €1.105,63 | €2.211,26 | €50,00 | €3,06 |
| TEST | Btc Donchian 4H | 1 | €10.002,28 | €1.105,63 | €2.211,26 | €50,00 | €3,06 |
| TEST | 1H Fast Nohigh Cap75 V1 | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Nohigh V1 | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €10 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €10 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €10 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €50 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €50 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €50 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · prudente · 5x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · prudente · 5x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €10 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €10 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €50 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €50 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · prudente · 5x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · prudente · 5x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Quality7 V1 | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Quality7 Regime V1 | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 4H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 4H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 4H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Donchian 4H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 4H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 4H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Ema 4H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Bollinger 1H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 0 | €9.995,97 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Runner25 V1 | 3 | €9.993,05 | €4.484,54 | €8.969,08 | €99,95 | €-1,57 |
| TEST | Combo Adaptive Tp3 V1 | 3 | €9.993,05 | €4.484,54 | €8.969,08 | €99,95 | €-1,57 |
| TEST | 1H Fast Score 6 75 V1 | 3 | €9.990,45 | €3.979,16 | €11.937,49 | €149,95 | €-2,39 |
| TEST | 1H Fast No Pepe V1 | 3 | €9.990,45 | €3.979,16 | €11.937,49 | €149,95 | €-2,39 |
| TEST | 1H Fast Tp2 V1 | 3 | €9.990,45 | €3.979,16 | €11.937,49 | €149,95 | €-2,39 |
| TEST | 1H Fast V3 Cap75 V1 | 3 | €9.990,45 | €3.979,16 | €11.937,49 | €149,95 | €-2,39 |
| TEST | 1H Fast V3 Long Only V1 | 3 | €9.990,45 | €3.979,16 | €11.937,49 | €149,95 | €-2,39 |
| TEST | 1H Fast V3 No Esports V1 | 3 | €9.990,45 | €3.979,16 | €11.937,49 | €149,95 | €-2,39 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.982,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €9.979,87 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Donchian 1H | 0 | €9.968,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Adaptive 1H | 1 | €9.966,28 | €1.054,45 | €3.163,36 | €49,74 | €20,32 |
| TEST | Combo Scanner | 3 | €9.965,83 | €3.315,37 | €6.630,74 | €149,74 | €-46,94 |
| TEST | Bilanciata 1H V2 | 4 | €9.964,64 | €1.532,77 | €4.598,30 | €99,11 | €34,80 |
| TEST | Combo Adaptive Regime V1 | 3 | €9.964,13 | €3.107,23 | €6.214,47 | €149,84 | €-31,66 |
| TEST | Combo Adaptive Partial 1R V1 | 3 | €9.963,18 | €2.523,11 | €5.046,23 | €124,84 | €-58,90 |
| TEST | Btc Adaptive 1H | 1 | €9.949,01 | €1.151,09 | €3.453,28 | €49,73 | €4,77 |
| TEST | Doge Ema 1H | 0 | €9.948,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 1H | 0 | €9.944,21 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | 2 | €9.939,80 | €416,21 | €832,42 | €99,89 | €-59,70 |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | 2 | €9.939,80 | €416,21 | €832,42 | €99,89 | €-59,70 |
| TEST | Eth Donchian 1H | 1 | €9.939,63 | €1.144,51 | €3.433,53 | €0,00 | €52,87 |
| TEST | Scanner Top5 Btc Guard V1 | 2 | €9.935,58 | €416,12 | €832,24 | €99,87 | €-63,68 |
| TEST | Scanner Top5 Btc Guard Mfe V1 | 2 | €9.935,58 | €416,12 | €832,24 | €99,87 | €-63,68 |
| TEST | Rapida 1H V3 Filtered | 4 | €9.929,58 | €3.872,62 | €11.617,85 | €148,72 | €93,36 |
| TEST | Btc Ema 1H | 1 | €9.926,36 | €1.144,78 | €3.434,35 | €49,45 | €36,04 |
| TEST | Benchmark trend following EMA 1H | 3 | €9.924,93 | €2.212,42 | €4.424,84 | €149,11 | €-0,42 |
| TEST | Rapida 1H V1 | 4 | €9.917,55 | €3.037,61 | €9.112,84 | €196,10 | €3,69 |
| TEST | Btc Donchian 1H | 1 | €9.893,66 | €1.287,72 | €3.863,16 | €49,45 | €5,34 |
| TEST | Eth Ema 1H | 1 | €9.889,64 | €1.012,80 | €3.038,40 | €0,00 | €46,79 |
| TEST | Scanner Bottom 5 Short 1H | 2 | €9.818,74 | €1.920,13 | €3.840,25 | €49,33 | €-44,50 |
| TEST | Global Confluence puro 1H | 1 | €9.785,72 | €1.535,54 | €3.071,08 | €49,14 | €-39,90 |
| TEST | Combo Adaptive Mfe Trail | 3 | €9.717,63 | €2.612,79 | €5.225,58 | €48,50 | €23,39 |

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
| PRINCIPALE | Principale 4H | Confluenza trend | €9.884,55 | €-100,68 | 16 | 16 | 31,25% | 0,81 | €-6,29 | 4,26% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €10.453,88 | €386,68 | 17 | 17 | 47,06% | 2,37 | €22,75 | 1,62% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.448,28 | €328,90 | 23 | 23 | 47,83% | 1,78 | €14,30 | 2,70% |
| TEST | Combo Adaptive | Combo Adaptive | €10.240,79 | €246,18 | 16 | 16 | 43,75% | 2,08 | €15,39 | 1,27% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €10.236,65 | €120,58 | 23 | 23 | 39,13% | 1,19 | €5,24 | 2,20% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €10.195,13 | €195,13 | 7 | 7 | 57,14% | 2,81 | €27,88 | 0,59% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €10.193,67 | €229,40 | 17 | 17 | 35,29% | 1,54 | €13,49 | 2,32% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €10.191,93 | €221,19 | 14 | 14 | 50,00% | 1,80 | €15,80 | 1,98% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €10.152,11 | €152,11 | 15 | 15 | 46,67% | 1,66 | €10,14 | 2,06% |
| TEST | Ampia 4H | Confluenza trend | €10.131,56 | €139,54 | 11 | 11 | 27,27% | 1,50 | €12,69 | 2,08% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €10.124,13 | €81,68 | 21 | 21 | 42,86% | 1,21 | €3,89 | 1,81% |
| TEST | Scanner Top5 Btc Runner25 V1 | Scanner Top 5 + forza BTC | €10.100,56 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,49% |
| TEST | Scanner Top5 Btc Tp3 V1 | Scanner Top 5 + forza BTC | €10.100,56 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,49% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €10.091,49 | €96,51 | 16 | 16 | 37,50% | 1,37 | €6,03 | 2,29% |
| TEST | Scanner Top5 Btc Btc Le3 V1 | Scanner Top 5 + forza BTC | €10.078,16 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,51% |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | Scanner Top 5 + forza BTC | €10.078,16 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,51% |
| TEST | Scanner Top5 Btc Mfe V1 | Scanner Top 5 + forza BTC | €10.074,45 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,54% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.068,69 | €68,69 | 1 | 1 | 100,00% | ∞ | €68,69 | 0,31% |
| TEST | Combo Trend | Combo Trend | €10.054,14 | €57,96 | 15 | 15 | 33,33% | 1,15 | €3,86 | 2,19% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €10.022,50 | €-4,49 | 1 | 1 | 0,00% | 0,00 | €-4,49 | 0,55% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €10.015,45 | €15,45 | 1 | 1 | 100,00% | ∞ | €15,45 | 0,51% |
| TEST | Sol Ema 1H | Trend following EMA | €10.014,82 | €-9,16 | 2 | 2 | 50,00% | 0,83 | €-4,58 | 0,98% |
| TEST | Combo Adaptive Long Only V1 | Combo Adaptive | €10.011,18 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,50% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €10.005,50 | €-18,45 | 2 | 2 | 50,00% | 0,67 | €-9,23 | 0,99% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €10.004,31 | €4,31 | 3 | 2 | 33,33% | 1,07 | €1,44 | 0,93% |
| TEST | Btc Ema 4H | Trend following EMA | €10.002,28 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,19% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €10.002,28 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,19% |
| TEST | 1H Fast Nohigh Cap75 V1 | Momentum / breakout | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | Momentum / breakout | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | 1H Fast V3 Nohigh V1 | Momentum / breakout V3 Filtered | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | Momentum / breakout V3 Filtered | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | Momentum / breakout V3 Filtered | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 15 · €10 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 20 · €10 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 25 · €10 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 20 · €50 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 20 · prudente · 5x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 85 · €10 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 80 · €10 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 85 · €50 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 80 · €50 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 85 · prudente · 5x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 80 · prudente · 5x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Combo Adaptive Quality7 V1 | Combo Adaptive | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Combo Adaptive Quality7 Regime V1 | Combo Adaptive | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | Combo Adaptive | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Sol Ema 4H | Trend following EMA | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Eth Ema 4H | Trend following EMA | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €9.995,97 | €-4,03 | 4 | 4 | 25,00% | 0,18 | €-1,01 | 0,04% |
| TEST | Combo Adaptive Runner25 V1 | Combo Adaptive | €9.993,05 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,33% |
| TEST | Combo Adaptive Tp3 V1 | Combo Adaptive | €9.993,05 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,33% |
| TEST | 1H Fast Score 6 75 V1 | Momentum / breakout | €9.990,45 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,10% |
| TEST | 1H Fast No Pepe V1 | Momentum / breakout | €9.990,45 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,10% |
| TEST | 1H Fast Tp2 V1 | Momentum / breakout | €9.990,45 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,10% |
| TEST | 1H Fast V3 Cap75 V1 | Momentum / breakout V3 Filtered | €9.990,45 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,10% |
| TEST | 1H Fast V3 Long Only V1 | Momentum / breakout V3 Filtered | €9.990,45 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,10% |
| TEST | 1H Fast V3 No Esports V1 | Momentum / breakout V3 Filtered | €9.990,45 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,10% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.982,18 | €-17,82 | 4 | 4 | 25,00% | 0,30 | €-4,46 | 0,18% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €9.979,87 | €-20,13 | 4 | 4 | 25,00% | 0,18 | €-5,03 | 0,20% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €9.968,98 | €-31,02 | 2 | 2 | 50,00% | 0,46 | €-15,51 | 0,93% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.966,28 | €-51,89 | 2 | 2 | 50,00% | 0,05 | €-25,94 | 1,02% |
| TEST | Combo Scanner | Combo Scanner | €9.965,83 | €17,00 | 17 | 17 | 41,18% | 1,04 | €1,00 | 1,88% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €9.964,64 | €-67,37 | 16 | 14 | 43,75% | 0,84 | €-4,21 | 2,75% |
| TEST | Combo Adaptive Regime V1 | Combo Adaptive | €9.964,13 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,68% |
| TEST | Combo Adaptive Partial 1R V1 | Combo Adaptive | €9.963,18 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,68% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €9.949,01 | €-54,55 | 1 | 1 | 0,00% | 0,00 | €-54,55 | 0,89% |
| TEST | Doge Ema 1H | Trend following EMA | €9.948,28 | €-51,72 | 4 | 4 | 50,00% | 0,54 | €-12,93 | 1,27% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.944,21 | €-55,79 | 1 | 1 | 0,00% | 0,00 | €-55,79 | 0,62% |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | Scanner Top 5 + forza BTC | €9.939,80 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,60% |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | Scanner Top 5 + forza BTC | €9.939,80 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,60% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.939,63 | €-110,95 | 2 | 2 | 0,00% | 0,00 | €-55,48 | 1,38% |
| TEST | Scanner Top5 Btc Guard V1 | Scanner Top 5 + forza BTC | €9.935,58 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,71% |
| TEST | Scanner Top5 Btc Guard Mfe V1 | Scanner Top 5 + forza BTC | €9.935,58 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,71% |
| TEST | Rapida 1H V3 Filtered | Momentum / breakout V3 Filtered | €9.929,58 | €-156,37 | 36 | 36 | 33,33% | 0,81 | €-4,34 | 2,89% |
| TEST | Btc Ema 1H | Trend following EMA | €9.926,36 | €-109,08 | 2 | 2 | 0,00% | 0,00 | €-54,54 | 1,56% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.924,93 | €-72,00 | 9 | 9 | 33,33% | 0,77 | €-8,00 | 2,25% |
| TEST | Rapida 1H V1 | Momentum / breakout | €9.917,55 | €-80,68 | 47 | 47 | 34,04% | 0,93 | €-1,72 | 4,86% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €9.893,66 | €-110,32 | 2 | 2 | 0,00% | 0,00 | €-55,16 | 1,49% |
| TEST | Eth Ema 1H | Trend following EMA | €9.889,64 | €-155,12 | 4 | 4 | 25,00% | 0,05 | €-38,78 | 1,59% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.818,74 | €-134,45 | 11 | 11 | 27,27% | 0,50 | €-12,22 | 3,67% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.785,72 | €-172,54 | 6 | 6 | 33,33% | 0,21 | €-28,76 | 2,35% |
| TEST | Combo Adaptive Mfe Trail | Combo Adaptive | €9.717,63 | €-302,40 | 21 | 21 | 28,57% | 0,36 | €-14,40 | 3,44% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | DOGE | SHORT | Confluenza trend | 240m | 3,0x | 0,07292 | 0,07286 | 0,07500 | 0,09686 | 0,06875 | €574,44 | €1.723,33 | €49,28 | €1,31 |
| Principale 4H | LAB | SHORT | Confluenza trend | 240m | 3,0x | 0,17841 | 0,17841 | 0,19982 | 0,23699 | 0,13559 | €136,26 | €408,77 | €49,05 | €-0,00 |
| Principale 4H | ZEC | LONG | Confluenza trend | 240m | 3,0x | 556,07119 | 546,51000 | 524,63715 | 373,49448 | 618,93927 | €293,97 | €881,92 | €49,85 | €-15,16 |
| Principale 4H | SUI | LONG | Confluenza trend | 240m | 3,0x | 0,76296 | 0,76296 | 0,73998 | 0,51245 | 0,80891 | €547,52 | €1.642,56 | €49,46 | €0,00 |
| Bilanciata 1H V1 | LAB | SHORT | Confluenza trend | 60m | 3,0x | 0,18667 | 0,18667 | 0,20845 | 0,24796 | 0,14311 | €143,84 | €431,52 | €50,35 | €-0,00 |
| Bilanciata 1H V1 | ONDO | LONG | Confluenza trend | 60m | 3,0x | 0,37613 | 0,37613 | 0,36189 | 0,25263 | 0,40460 | €442,89 | €1.328,68 | €50,30 | €0,00 |
| Bilanciata 1H V1 | ETH | LONG | Confluenza trend | 60m | 3,0x | 1894,43881 | 1923,61000 | 1905,59197 | 1272,43140 | 1955,82155 | €1.043,85 | €3.131,56 | €0,00 | €48,22 |
| Bilanciata 1H V1 | XRP | LONG | Confluenza trend | 60m | 3,0x | 1,13540 | 1,13517 | 1,11905 | 0,76261 | 1,16810 | €1.172,10 | €3.516,30 | €50,63 | €-0,70 |
| Bilanciata 1H V2 | LAB | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,18667 | 0,18667 | 0,20845 | 0,24796 | 0,14311 | €139,69 | €419,08 | €48,90 | €-0,00 |
| Bilanciata 1H V2 | GRAM | SHORT | Confluenza trend V2 | 60m | 3,0x | 1,49240 | 1,49240 | 1,53621 | 1,98241 | 1,40478 | €570,19 | €1.710,58 | €50,21 | €-0,00 |
| Bilanciata 1H V2 | ESPORTS | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,02164 | 0,02164 | 0,02164 | 0,02874 | 0,01644 | €138,69 | €416,06 | €0,00 | €-0,00 |
| Bilanciata 1H V2 | PEPE | LONG | Confluenza trend V2 | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €684,20 | €2.052,59 | €0,00 | €34,80 |
| Bilanciata 1H V3 Filtered | ESPORTS | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,02126 | 0,02126 | 0,02126 | 0,02823 | 0,01615 | €141,51 | €424,52 | €0,00 | €-0,00 |
| Bilanciata 1H V3 Filtered | ETH | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1894,43881 | 1923,61000 | 1905,59197 | 1272,43140 | 1955,82155 | €1.047,36 | €3.142,08 | €0,00 | €48,38 |
| Bilanciata 1H V3 Filtered | XRP | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1,11148 | 1,13517 | 1,11148 | 0,74655 | 1,14349 | €1.163,70 | €3.491,09 | €0,00 | €74,40 |
| Bilanciata 1H V3 Filtered | ADA | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,17417 | 0,17414 | 0,17046 | 0,11699 | 0,18161 | €799,70 | €2.399,09 | €51,19 | €-0,48 |
| Rapida 1H V1 | ESPORTS | SHORT | Momentum / breakout | 60m | 3,0x | 0,01984 | 0,01984 | 0,02222 | 0,02635 | 0,01627 | €129,65 | €388,96 | €46,68 | €-0,00 |
| Rapida 1H V1 | SUI | LONG | Momentum / breakout | 60m | 3,0x | 0,76416 | 0,76416 | 0,75422 | 0,51326 | 0,77907 | €1.284,19 | €3.852,58 | €50,12 | €0,00 |
| Rapida 1H V1 | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00173 | 0,00175 | 0,00154 | 0,00116 | 0,00202 | €147,41 | €442,24 | €49,70 | €4,58 |
| Rapida 1H V1 | XRP | LONG | Momentum / breakout | 60m | 3,0x | 1,13540 | 1,13517 | 1,12268 | 0,76261 | 1,15447 | €1.476,35 | €4.429,06 | €49,61 | €-0,89 |
| 1H Fast Score 6 75 V1 | XRP | LONG | Momentum / breakout | 60m | 3,0x | 1,13540 | 1,13517 | 1,12268 | 0,76261 | 1,15447 | €1.488,10 | €4.464,29 | €50,00 | €-0,89 |
| 1H Fast Score 6 75 V1 | ADA | LONG | Momentum / breakout | 60m | 3,0x | 0,17417 | 0,17414 | 0,17128 | 0,11699 | 0,17851 | €1.003,86 | €3.011,59 | €49,98 | €-0,60 |
| 1H Fast Score 6 75 V1 | ETH | LONG | Momentum / breakout | 60m | 3,0x | 1923,99472 | 1923,61000 | 1902,44598 | 1292,28312 | 1956,31783 | €1.487,21 | €4.461,62 | €49,97 | €-0,89 |
| 1H Fast No Pepe V1 | XRP | LONG | Momentum / breakout | 60m | 3,0x | 1,13540 | 1,13517 | 1,12268 | 0,76261 | 1,15447 | €1.488,10 | €4.464,29 | €50,00 | €-0,89 |
| 1H Fast No Pepe V1 | ADA | LONG | Momentum / breakout | 60m | 3,0x | 0,17417 | 0,17414 | 0,17128 | 0,11699 | 0,17851 | €1.003,86 | €3.011,59 | €49,98 | €-0,60 |
| 1H Fast No Pepe V1 | ETH | LONG | Momentum / breakout | 60m | 3,0x | 1923,99472 | 1923,61000 | 1902,44598 | 1292,28312 | 1956,31783 | €1.487,21 | €4.461,62 | €49,97 | €-0,89 |
| 1H Fast Tp2 V1 | XRP | LONG | Momentum / breakout | 60m | 3,0x | 1,13540 | 1,13517 | 1,12268 | 0,76261 | 1,16083 | €1.488,10 | €4.464,29 | €50,00 | €-0,89 |
| 1H Fast Tp2 V1 | ADA | LONG | Momentum / breakout | 60m | 3,0x | 0,17417 | 0,17414 | 0,17128 | 0,11699 | 0,17996 | €1.003,86 | €3.011,59 | €49,98 | €-0,60 |
| 1H Fast Tp2 V1 | ETH | LONG | Momentum / breakout | 60m | 3,0x | 1923,99472 | 1923,61000 | 1902,44598 | 1292,28312 | 1967,09220 | €1.487,21 | €4.461,62 | €49,97 | €-0,89 |
| Rapida 1H V3 Filtered | ESPORTS | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01977 | 0,01977 | 0,02214 | 0,02626 | 0,01621 | €137,70 | €413,09 | €49,57 | €-0,00 |
| Rapida 1H V3 Filtered | XRP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,11148 | 1,13517 | 1,12495 | 0,74655 | 1,13016 | €1.469,55 | €4.408,66 | €0,00 | €93,96 |
| Rapida 1H V3 Filtered | SUI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,76416 | 0,76416 | 0,75422 | 0,51326 | 0,77907 | €1.267,97 | €3.803,92 | €49,49 | €0,00 |
| Rapida 1H V3 Filtered | ADA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,17417 | 0,17414 | 0,17128 | 0,11699 | 0,17851 | €997,39 | €2.992,17 | €49,66 | €-0,60 |
| 1H Fast V3 Cap75 V1 | XRP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,13540 | 1,13517 | 1,12268 | 0,76261 | 1,15447 | €1.488,10 | €4.464,29 | €50,00 | €-0,89 |
| 1H Fast V3 Cap75 V1 | ADA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,17417 | 0,17414 | 0,17128 | 0,11699 | 0,17851 | €1.003,86 | €3.011,59 | €49,98 | €-0,60 |
| 1H Fast V3 Cap75 V1 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1923,99472 | 1923,61000 | 1902,44598 | 1292,28312 | 1956,31783 | €1.487,21 | €4.461,62 | €49,97 | €-0,89 |
| 1H Fast V3 Long Only V1 | XRP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,13540 | 1,13517 | 1,12268 | 0,76261 | 1,15447 | €1.488,10 | €4.464,29 | €50,00 | €-0,89 |
| 1H Fast V3 Long Only V1 | ADA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,17417 | 0,17414 | 0,17128 | 0,11699 | 0,17851 | €1.003,86 | €3.011,59 | €49,98 | €-0,60 |
| 1H Fast V3 Long Only V1 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1923,99472 | 1923,61000 | 1902,44598 | 1292,28312 | 1956,31783 | €1.487,21 | €4.461,62 | €49,97 | €-0,89 |
| 1H Fast V3 No Esports V1 | XRP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,13540 | 1,13517 | 1,12268 | 0,76261 | 1,15447 | €1.488,10 | €4.464,29 | €50,00 | €-0,89 |
| 1H Fast V3 No Esports V1 | ADA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,17417 | 0,17414 | 0,17128 | 0,11699 | 0,17851 | €1.003,86 | €3.011,59 | €49,98 | €-0,60 |
| 1H Fast V3 No Esports V1 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1923,99472 | 1923,61000 | 1902,44598 | 1292,28312 | 1956,31783 | €1.487,21 | €4.461,62 | €49,97 | €-0,89 |
| Ampia 4H | DOGE | SHORT | Confluenza trend | 240m | 2,0x | 0,07237 | 0,07286 | 0,07515 | 0,10819 | 0,06457 | €649,49 | €1.298,97 | €50,00 | €-8,86 |
| Ampia 4H | ZEC | LONG | Confluenza trend | 240m | 2,0x | 522,36445 | 546,51000 | 483,09844 | 263,79405 | 632,30930 | €332,53 | €665,06 | €49,99 | €30,74 |
| Ampia 4H | HYPE | SHORT | Confluenza trend | 240m | 2,0x | 59,36013 | 62,91800 | 63,40544 | 88,74339 | 48,03325 | €367,70 | €735,40 | €50,12 | €-44,08 |
| Ampia 4H | PEPE | LONG | Confluenza trend | 240m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €497,18 | €994,35 | €50,70 | €14,85 |
| Forza relativa 1H V1 | NEAR | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 2,02421 | 2,02421 | 1,97233 | 1,02223 | 2,13836 | €984,05 | €1.968,10 | €50,44 | €0,00 |
| Forza relativa 1H V1 | ALLO | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,37581 | 0,37581 | 0,40458 | 0,56184 | 0,31252 | €329,44 | €658,87 | €50,44 | €-0,00 |
| Forza relativa 1H V1 | ESPORTS | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,02126 | 0,02126 | 0,02126 | 0,03178 | 0,01564 | €208,05 | €416,10 | €0,00 | €-0,00 |
| Forza relativa 1H V1 | PEPE | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €986,47 | €1.972,93 | €50,47 | €-1,81 |
| Forza relativa 1H V2 | LAB | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,18833 | 0,18833 | 0,20950 | 0,28155 | 0,14176 | €222,78 | €445,56 | €50,08 | €-0,00 |
| Forza relativa 1H V2 | GRAM | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 1,47771 | 1,47771 | 1,52060 | 2,20918 | 1,38336 | €871,54 | €1.743,07 | €50,59 | €-0,00 |
| Forza relativa 1H V2 | ESPORTS | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,02126 | 0,02126 | 0,02126 | 0,03178 | 0,01564 | €215,33 | €430,67 | €0,00 | €-0,00 |
| Forza relativa 1H V2 | BANK | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,27910 | 0,25697 | 0,24560 | 0,14094 | 0,35278 | €213,08 | €426,17 | €51,14 | €-33,79 |
| Benchmark Donchian breakout 1H | BANK | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,27375 | 0,25697 | 0,24090 | 0,13825 | 0,35588 | €212,62 | €425,25 | €51,03 | €-26,07 |
| Benchmark Donchian breakout 1H | SUI | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,76606 | 0,76606 | 0,75182 | 0,38686 | 0,80165 | €1.377,00 | €2.754,00 | €51,18 | €0,00 |
| Benchmark trend following EMA 1H | NEAR | LONG | Trend following EMA | 60m | 2,0x | 2,02421 | 2,02421 | 1,96657 | 1,02223 | 2,15104 | €873,40 | €1.746,81 | €49,75 | €0,00 |
| Benchmark trend following EMA 1H | ALLO | SHORT | Trend following EMA | 60m | 2,0x | 0,37581 | 0,37581 | 0,40778 | 0,56184 | 0,30549 | €292,32 | €584,65 | €49,73 | €-0,00 |
| Benchmark trend following EMA 1H | ADA | LONG | Trend following EMA | 60m | 2,0x | 0,17417 | 0,17414 | 0,17005 | 0,08796 | 0,18326 | €1.046,69 | €2.093,39 | €49,63 | €-0,42 |
| Scanner Top 5 Long 1H | ONDO | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,37282 | 0,37282 | 0,35738 | 0,18828 | 0,40370 | €625,48 | €1.250,97 | €51,81 | €0,00 |
| Scanner Top 5 Long 1H | XRP | LONG | Scanner Top 5 Long | 60m | 2,0x | 1,11469 | 1,13517 | 1,09864 | 0,56292 | 1,14680 | €1.796,54 | €3.593,08 | €51,74 | €66,01 |
| Scanner Top 5 Long 1H | ADA | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,17009 | 0,17414 | 0,16650 | 0,08590 | 0,17727 | €1.222,25 | €2.444,49 | €51,57 | €58,18 |
| Scanner Bottom 5 Short 1H | ESPORTS | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,02150 | 0,02150 | 0,02150 | 0,03214 | 0,01634 | €207,40 | €414,80 | €0,00 | €-0,00 |
| Scanner Bottom 5 Short 1H | DOGE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,07193 | 0,07286 | 0,07296 | 0,10753 | 0,06985 | €1.712,73 | €3.425,45 | €49,33 | €-44,50 |
| Scanner Top 5 + forza BTC 1H | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,37613 | 0,37613 | 0,36189 | 0,18994 | 0,40745 | €677,81 | €1.355,62 | €51,32 | €0,00 |
| Scanner Top 5 + forza BTC 1H | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.070,89 | €2.141,78 | €0,00 | €49,76 |
| Scanner Top 5 + forza BTC 1H | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 77,70854 | 78,23100 | 76,45304 | 39,24281 | 80,47063 | €1.614,82 | €3.229,64 | €52,18 | €21,71 |
| Scanner Top5 Btc Mfe V1 | SUI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,76776 | 0,76776 | 0,75508 | 0,38772 | 0,79565 | €1.514,04 | €3.028,08 | €50,00 | €0,00 |
| Scanner Top5 Btc Mfe V1 | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 77,76655 | 78,23100 | 76,55444 | 39,27211 | 80,43319 | €1.603,37 | €3.206,74 | €49,98 | €19,15 |
| Scanner Top5 Btc Mfe V1 | XRP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,11539 | 1,13517 | 1,11539 | 0,56327 | 1,15073 | €1.735,04 | €3.470,07 | €0,00 | €61,53 |
| Scanner Top5 Btc Guard V1 | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,28515 | 0,25697 | 0,25093 | 0,14400 | 0,36043 | €208,33 | €416,67 | €50,00 | €-41,17 |
| Scanner Top5 Btc Guard V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00185 | 0,00175 | 0,00163 | 0,00093 | 0,00234 | €207,79 | €415,58 | €49,87 | €-22,50 |
| Scanner Top5 Btc Btc Le3 V1 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.063,01 | €2.126,01 | €50,00 | €2,86 |
| Scanner Top5 Btc Btc Le3 V1 | ADA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,16982 | 0,17414 | 0,16625 | 0,08576 | 0,17769 | €1.187,43 | €2.374,86 | €49,99 | €60,39 |
| Scanner Top5 Btc Btc Le3 V1 | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 77,78955 | 78,23100 | 76,66939 | 39,28373 | 80,25393 | €1.735,32 | €3.470,64 | €49,98 | €19,70 |
| Scanner Top5 Btc Btc 2 3 V1 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.063,01 | €2.126,01 | €50,00 | €2,86 |
| Scanner Top5 Btc Btc 2 3 V1 | ADA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,16982 | 0,17414 | 0,16625 | 0,08576 | 0,17769 | €1.187,43 | €2.374,86 | €49,99 | €60,39 |
| Scanner Top5 Btc Btc 2 3 V1 | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 77,78955 | 78,23100 | 76,66939 | 39,28373 | 80,25393 | €1.735,32 | €3.470,64 | €49,98 | €19,70 |
| Scanner Top5 Btc Guard Mfe V1 | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,28515 | 0,25697 | 0,25093 | 0,14400 | 0,36043 | €208,33 | €416,67 | €50,00 | €-41,17 |
| Scanner Top5 Btc Guard Mfe V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00185 | 0,00175 | 0,00163 | 0,00093 | 0,00234 | €207,79 | €415,58 | €49,87 | €-22,50 |
| Scanner Top5 Btc Guard Btc Le3 V1 | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,28216 | 0,25697 | 0,24830 | 0,14249 | 0,35665 | €208,33 | €416,67 | €50,00 | €-37,19 |
| Scanner Top5 Btc Guard Btc Le3 V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00185 | 0,00175 | 0,00163 | 0,00093 | 0,00234 | €207,88 | €415,75 | €49,89 | €-22,51 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,28216 | 0,25697 | 0,24830 | 0,14249 | 0,35665 | €208,33 | €416,67 | €50,00 | €-37,19 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00185 | 0,00175 | 0,00163 | 0,00093 | 0,00234 | €207,88 | €415,75 | €49,89 | €-22,51 |
| Scanner Top5 Btc Runner25 V1 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.031,84 | €2.063,68 | €50,00 | €1,43 |
| Scanner Top5 Btc Runner25 V1 | ADA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,16962 | 0,17414 | 0,16597 | 0,08566 | 0,18059 | €1.159,50 | €2.319,01 | €49,99 | €61,77 |
| Scanner Top5 Btc Runner25 V1 | ETH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1900,34999 | 1923,61000 | 1872,70756 | 959,67675 | 1983,27732 | €1.717,93 | €3.435,85 | €49,98 | €42,05 |
| Scanner Top5 Btc Tp3 V1 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.031,84 | €2.063,68 | €50,00 | €1,43 |
| Scanner Top5 Btc Tp3 V1 | ADA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,16962 | 0,17414 | 0,16597 | 0,08566 | 0,18059 | €1.159,50 | €2.319,01 | €49,99 | €61,77 |
| Scanner Top5 Btc Tp3 V1 | ETH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1900,34999 | 1923,61000 | 1872,70756 | 959,67675 | 1983,27732 | €1.717,93 | €3.435,85 | €49,98 | €42,05 |
| Global Confluence puro 1H | DOGE | SHORT | Global Confluence puro | 60m | 2,0x | 0,07193 | 0,07286 | 0,07308 | 0,10753 | 0,06905 | €1.535,54 | €3.071,08 | €49,14 | €-39,90 |
| Combo Trend | ONDO | LONG | Combo Trend | 60m | 2,0x | 0,37282 | 0,37282 | 0,35567 | 0,18828 | 0,41057 | €545,86 | €1.091,71 | €50,24 | €0,00 |
| Combo Trend | ESPORTS | SHORT | Combo Trend | 60m | 2,0x | 0,01883 | 0,01883 | 0,02109 | 0,02815 | 0,01386 | €209,57 | €419,14 | €50,30 | €-0,00 |
| Combo Trend | PEPE | LONG | Combo Trend | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €884,51 | €1.769,01 | €50,29 | €-1,63 |
| Combo Scanner | ONDO | LONG | Combo Scanner | 60m | 2,0x | 0,37282 | 0,37282 | 0,35738 | 0,18828 | 0,40679 | €599,14 | €1.198,28 | €49,63 | €0,00 |
| Combo Scanner | PEPE | LONG | Combo Scanner | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €978,80 | €1.957,60 | €50,08 | €-1,80 |
| Combo Scanner | DOGE | SHORT | Combo Scanner | 60m | 2,0x | 0,07193 | 0,07286 | 0,07296 | 0,10753 | 0,06965 | €1.737,43 | €3.474,87 | €50,04 | €-45,14 |
| Combo Adaptive | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,37282 | 0,37282 | 0,35738 | 0,18828 | 0,40370 | €613,42 | €1.226,85 | €50,81 | €0,00 |
| Combo Adaptive | GRAM | SHORT | Combo Adaptive | 60m | 2,0x | 1,48181 | 1,48181 | 1,51561 | 2,21531 | 1,41422 | €1.129,35 | €2.258,70 | €51,51 | €-0,00 |
| Combo Adaptive | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.001,06 | €2.002,12 | €51,22 | €-1,84 |
| Combo Adaptive Mfe Trail | ESPORTS | SHORT | Combo Adaptive | 60m | 2,0x | 0,02156 | 0,02156 | 0,02091 | 0,03223 | 0,01638 | €202,62 | €405,24 | €0,00 | €-0,00 |
| Combo Adaptive Mfe Trail | SOL | LONG | Combo Adaptive | 60m | 2,0x | 77,56451 | 78,23100 | 77,65759 | 39,17008 | 80,14392 | €1.462,23 | €2.924,45 | €0,00 | €25,13 |
| Combo Adaptive Mfe Trail | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €947,94 | €1.895,88 | €48,50 | €-1,74 |
| Combo Adaptive Regime V1 | BANK | LONG | Combo Adaptive | 60m | 2,0x | 0,28515 | 0,25697 | 0,25093 | 0,14400 | 0,35358 | €208,33 | €416,67 | €50,00 | €-41,17 |
| Combo Adaptive Regime V1 | ADA | LONG | Combo Adaptive | 60m | 2,0x | 0,17017 | 0,17414 | 0,16653 | 0,08594 | 0,17746 | €1.168,24 | €2.336,48 | €50,00 | €54,48 |
| Combo Adaptive Regime V1 | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,07193 | 0,07286 | 0,07296 | 0,10753 | 0,06985 | €1.730,66 | €3.461,32 | €49,84 | €-44,97 |
| Combo Adaptive Long Only V1 | BANK | LONG | Combo Adaptive | 60m | 2,0x | 0,28515 | 0,25697 | 0,25093 | 0,14400 | 0,35358 | €208,33 | €416,67 | €50,00 | €-41,17 |
| Combo Adaptive Long Only V1 | ADA | LONG | Combo Adaptive | 60m | 2,0x | 0,17017 | 0,17414 | 0,16653 | 0,08594 | 0,17746 | €1.168,24 | €2.336,48 | €50,00 | €54,48 |
| Combo Adaptive Partial 1R V1 | BANK | LONG | Combo Adaptive | 60m | 2,0x | 0,28515 | 0,25697 | 0,25093 | 0,14400 | 0,35358 | €208,33 | €416,67 | €50,00 | €-41,17 |
| Combo Adaptive Partial 1R V1 | ADA | LONG | Combo Adaptive | 60m | 2,0x | 0,17017 | 0,17414 | 0,16653 | 0,08594 | 0,17746 | €584,12 | €1.168,24 | €25,00 | €27,24 |
| Combo Adaptive Partial 1R V1 | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,07193 | 0,07286 | 0,07296 | 0,10753 | 0,06985 | €1.730,66 | €3.461,32 | €49,84 | €-44,97 |
| Combo Adaptive Runner25 V1 | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.031,84 | €2.063,68 | €50,00 | €1,43 |
| Combo Adaptive Runner25 V1 | ETH | LONG | Combo Adaptive | 60m | 2,0x | 1900,34999 | 1923,61000 | 1903,18396 | 959,67675 | 1983,27732 | €1.718,41 | €3.436,81 | €0,00 | €42,07 |
| Combo Adaptive Runner25 V1 | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,07193 | 0,07286 | 0,07296 | 0,10753 | 0,06882 | €1.734,29 | €3.468,58 | €49,95 | €-45,06 |
| Combo Adaptive Tp3 V1 | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.031,84 | €2.063,68 | €50,00 | €1,43 |
| Combo Adaptive Tp3 V1 | ETH | LONG | Combo Adaptive | 60m | 2,0x | 1900,34999 | 1923,61000 | 1903,18396 | 959,67675 | 1983,27732 | €1.718,41 | €3.436,81 | €0,00 | €42,07 |
| Combo Adaptive Tp3 V1 | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,07193 | 0,07286 | 0,07296 | 0,10753 | 0,06882 | €1.734,29 | €3.468,58 | €49,95 | €-45,06 |
| Btc Ema 1H | BTC | LONG | Trend following EMA | 60m | 3,0x | 64820,68154 | 65501,00000 | 63887,26373 | 43537,89110 | 66687,51717 | €1.144,78 | €3.434,35 | €49,45 | €36,04 |
| Btc Ema 4H | BTC | LONG | Trend following EMA | 240m | 2,0x | 65410,57950 | 65501,00000 | 63931,54687 | 33032,34265 | 69108,16107 | €1.105,63 | €2.211,26 | €50,00 | €3,06 |
| Btc Donchian 1H | BTC | LONG | Donchian breakout 20 barre | 60m | 3,0x | 65410,57950 | 65501,00000 | 64573,32408 | 43934,10590 | 67085,09034 | €1.287,72 | €3.863,16 | €49,45 | €5,34 |
| Btc Donchian 4H | BTC | LONG | Donchian breakout 20 barre | 240m | 2,0x | 65410,57950 | 65501,00000 | 63931,54687 | 33032,34265 | 69551,87112 | €1.105,63 | €2.211,26 | €50,00 | €3,06 |
| Btc Adaptive 1H | BTC | LONG | Combo Adaptive | 60m | 3,0x | 65410,57950 | 65501,00000 | 64468,66716 | 43934,10590 | 67294,40419 | €1.151,09 | €3.453,28 | €49,73 | €4,77 |
| Sol Ema 1H | SOL | LONG | Trend following EMA | 60m | 3,0x | 77,56451 | 78,23100 | 76,27481 | 52,09750 | 80,14392 | €1.001,44 | €3.004,32 | €49,95 | €25,82 |
| Sol Donchian 1H | SOL | LONG | Donchian breakout 20 barre | 60m | 3,0x | 77,56451 | 78,23100 | 76,41811 | 52,09750 | 79,85731 | €1.127,14 | €3.381,43 | €49,98 | €29,06 |
| Sol Adaptive 1H | SOL | LONG | Combo Adaptive | 60m | 3,0x | 77,56451 | 78,23100 | 76,27481 | 52,09750 | 80,14392 | €1.000,51 | €3.001,52 | €49,91 | €25,79 |
| Eth Ema 1H | ETH | LONG | Trend following EMA | 60m | 3,0x | 1894,43881 | 1923,61000 | 1909,06598 | 1272,43140 | 1955,82155 | €1.012,80 | €3.038,40 | €0,00 | €46,79 |
| Eth Donchian 1H | ETH | LONG | Donchian breakout 20 barre | 60m | 3,0x | 1894,43881 | 1923,61000 | 1909,06598 | 1272,43140 | 1949,00125 | €1.144,51 | €3.433,53 | €0,00 | €52,87 |
| Eth Adaptive 1H | ETH | LONG | Combo Adaptive | 60m | 3,0x | 1911,33219 | 1923,61000 | 1881,27848 | 1283,77812 | 1971,43961 | €1.054,45 | €3.163,36 | €49,74 | €20,32 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Benchmark trend following EMA 1H | BANK | LONG | 2026-07-21T04:38:31+00:00 | 0,25216 | €-53,23 | -1,07 | STOP_STRESS_SLIPPAGE |
| Rapida 1H V3 Filtered | BANK | LONG | 2026-07-21T04:38:31+00:00 | 0,25330 | €-53,88 | -1,09 | STOP_STRESS_SLIPPAGE |
| Rapida 1H V1 | BANK | LONG | 2026-07-21T04:38:31+00:00 | 0,25330 | €-55,00 | -1,09 | STOP_STRESS_SLIPPAGE |
| Bilanciata 1H V3 Filtered | BANK | LONG | 2026-07-21T04:38:31+00:00 | 0,25239 | €-55,20 | -1,07 | STOP_STRESS_SLIPPAGE |
| Bilanciata 1H V1 | BANK | LONG | 2026-07-21T04:38:31+00:00 | 0,25357 | €2,87 | 0,06 | STOP_STRESS_SLIPPAGE |
| Rapida 1H V1 | DOGE | SHORT | 2026-07-21T03:23:31+00:00 | 0,07275 | €-56,25 | -1,13 | STOP |
| Benchmark Bollinger mean reversion 1H | BANK | SHORT | 2026-07-21T01:23:31+00:00 | 0,29357 | €-5,46 | -0,11 | STOP_STRESS_SLIPPAGE |
| Scanner Top 5 Long 1H | PEPE | LONG | 2026-07-20T22:53:31+00:00 | 0,00000 | €5,97 | 0,12 | STOP |
| Rapida 1H V1 | GRAM | SHORT | 2026-07-20T22:38:32+00:00 | 1,49330 | €-4,09 | -0,08 | TIME_EXIT_NO_CANDLES |
| Rapida 1H V3 Filtered | ETH | LONG | 2026-07-20T19:23:30+00:00 | 1894,05992 | €-5,50 | -0,11 | STOP |
| Rapida 1H V1 | ETH | LONG | 2026-07-20T19:23:30+00:00 | 1894,05992 | €-5,58 | -0,11 | STOP |
| Benchmark Donchian breakout 1H | ETH | LONG | 2026-07-20T19:08:30+00:00 | 1897,10014 | €44,88 | 0,88 | STOP |

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

Generato: 2026-07-21 05:14 UTC


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

Segnali totali salvati: **39**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-07-21 | BTC | 65.476,52 | +3 | +2 | +2 | 0 | 0 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-07-21 | DOGE | 0.07281 | -6 | -3 | -2 | -2 | -3 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-07-21 | SOL | 78,22 | +1 | +2 | +1 | +2 | -1 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-07-20 | BTC | 64.190,23 | +2 | +2 | +2 | 0 | -1 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-07-20 | DOGE | 0.07180 | -7 | -3 | -2 | -2 | -3 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-07-20 | SOL | 76,01 | -4 | 0 | 0 | 0 | -3 | -1 | 0 | STAI FUORI / VENDI PARZIALE |
| 2026-07-19 | BTC | 64.750,69 | +3 | +1 | +1 | 0 | +2 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-07-19 | DOGE | 0.07243 | -6 | -3 | -2 | -2 | -2 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-07-19 | SOL | 76,04 | -4 | -1 | -1 | 0 | -2 | -1 | 0 | STAI FUORI / VENDI PARZIALE |
| 2026-07-18 | BTC | 63.883,71 | 0 | +1 | +1 | +3 | -1 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-07-18 | DOGE | 0.07234 | -6 | -3 | -2 | -2 | -2 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-07-18 | SOL | 74,93 | -3 | 0 | -1 | +1 | -2 | -1 | 0 | TAKE PROFIT SU SPIKE / NON INSEGUIRE |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 13 | 12 | 11 | 10 | 8 | 6 | 3 | 0 | 0 | 0 | 0 | 0 |
| SOL | 13 | 12 | 11 | 10 | 8 | 6 | 3 | 0 | 0 | 0 | 0 | 0 |
| DOGE | 13 | 12 | 11 | 10 | 8 | 6 | 3 | 0 | 0 | 0 | 0 | 0 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-07-12 | 10g | 2026-07-22 | domani |
| SOL | 2026-07-12 | 10g | 2026-07-22 | domani |
| DOGE | 2026-07-12 | 10g | 2026-07-22 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 11 | 36,36% | +0,08% | +0,13% | FEEDBACK RAPIDO |
| BTC | 2g | 10 | 50,00% | +0,37% | +0,06% | FEEDBACK RAPIDO |
| BTC | 3g | 9 | 44,44% | +0,30% | -0,14% | FEEDBACK RAPIDO |
| BTC | 5g | 8 | 37,50% | +0,84% | +0,27% | FEEDBACK RAPIDO |
| BTC | 7g | 6 | 66,67% | +1,52% | +1,52% | FEEDBACK RAPIDO |
| BTC | 10g | 3 | 100,00% | +1,72% | +1,72% | FEEDBACK RAPIDO |
| BTC | 14g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 21g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 30g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 1g | 11 | 45,45% | +0,06% | -0,75% | FEEDBACK RAPIDO |
| SOL | 2g | 10 | 20,00% | -0,02% | -1,04% | FEEDBACK RAPIDO |
| SOL | 3g | 9 | 11,11% | -0,25% | -1,76% | FEEDBACK RAPIDO |
| SOL | 5g | 7 | 28,57% | -1,08% | -1,29% | FEEDBACK RAPIDO |
| SOL | 7g | 5 | 40,00% | -0,59% | -1,92% | FEEDBACK RAPIDO |
| SOL | 10g | 2 | 50,00% | -1,00% | -1,00% | FEEDBACK RAPIDO |
| SOL | 14g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 21g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 30g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 1g | 12 | 58,33% | -0,12% | +0,12% | FEEDBACK RAPIDO |
| DOGE | 2g | 11 | 54,55% | -0,25% | +0,25% | FEEDBACK RAPIDO |
| DOGE | 3g | 10 | 60,00% | -0,50% | +0,50% | FEEDBACK RAPIDO |
| DOGE | 5g | 8 | 62,50% | -0,71% | +0,71% | FEEDBACK RAPIDO |
| DOGE | 7g | 6 | 66,67% | -0,72% | +0,72% | FEEDBACK RAPIDO |
| DOGE | 10g | 3 | 100,00% | -1,67% | +1,67% | FEEDBACK RAPIDO |
| DOGE | 14g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 21g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 30g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 11 | 36,36% | +0,08% | +0,13% | -0,10% | +0,80% | FEEDBACK RAPIDO |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 12 | 41,67% | +0,19% | +0,19% | -0,00% | +0,86% | FEEDBACK RAPIDO |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 12 | 41,67% | +0,19% | +0,19% | -0,00% | +0,86% | FEEDBACK RAPIDO |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 10 | 40,00% | +0,11% | +0,11% | -0,05% | +0,77% | FEEDBACK RAPIDO |
| BTC | 1g | Tecnico | CALIBRABILE | 11 | 27,27% | +0,18% | -0,84% | -0,02% | +0,90% | FEEDBACK RAPIDO |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +2,00% | +2,00% | +1,48% | +2,25% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 10 | 50,00% | +0,37% | +0,06% | -0,28% | +1,41% | FEEDBACK RAPIDO |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 11 | 54,55% | +0,38% | +0,38% | -0,22% | +1,44% | FEEDBACK RAPIDO |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 11 | 54,55% | +0,38% | +0,38% | -0,22% | +1,44% | FEEDBACK RAPIDO |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 10 | 50,00% | +0,30% | +0,30% | -0,30% | +1,45% | FEEDBACK RAPIDO |
| BTC | 2g | Tecnico | CALIBRABILE | 10 | 40,00% | +0,42% | -0,31% | -0,21% | +1,49% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 9 | 44,44% | +0,30% | -0,14% | -1,30% | +2,10% | FEEDBACK RAPIDO |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 10 | 70,00% | +0,52% | +0,52% | -1,11% | +2,17% | FEEDBACK RAPIDO |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 10 | 70,00% | +0,52% | +0,52% | -1,11% | +2,17% | FEEDBACK RAPIDO |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 10 | 70,00% | +0,52% | +0,52% | -1,11% | +2,17% | FEEDBACK RAPIDO |
| BTC | 3g | Tecnico | CALIBRABILE | 9 | 33,33% | +0,77% | -0,30% | -1,01% | +2,31% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 8 | 37,50% | +0,84% | +0,27% | -2,36% | +2,70% | FEEDBACK RAPIDO |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 8 | 50,00% | +0,84% | +0,84% | -2,36% | +2,70% | FEEDBACK RAPIDO |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 8 | 50,00% | +0,84% | +0,84% | -2,36% | +2,70% | FEEDBACK RAPIDO |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 8 | 50,00% | +0,84% | +0,84% | -2,36% | +2,70% | FEEDBACK RAPIDO |
| BTC | 5g | Tecnico | CALIBRABILE | 7 | 42,86% | +0,81% | -0,53% | -2,23% | +2,79% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 6 | 66,67% | +1,52% | +1,52% | -2,22% | +3,40% | FEEDBACK RAPIDO |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 6 | 66,67% | +1,52% | +1,52% | -2,22% | +3,40% | FEEDBACK RAPIDO |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 6 | 66,67% | +1,52% | +1,52% | -2,22% | +3,40% | FEEDBACK RAPIDO |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 6 | 66,67% | +1,52% | +1,52% | -2,22% | +3,40% | FEEDBACK RAPIDO |
| BTC | 7g | Tecnico | CALIBRABILE | 5 | 60,00% | +1,89% | -0,39% | -2,01% | +3,57% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 3 | 100,00% | +1,72% | +1,72% | -3,05% | +2,89% | FEEDBACK RAPIDO |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 3 | 100,00% | +1,72% | +1,72% | -3,05% | +2,89% | FEEDBACK RAPIDO |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 3 | 100,00% | +1,72% | +1,72% | -3,05% | +2,89% | FEEDBACK RAPIDO |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 3 | 100,00% | +1,72% | +1,72% | -3,05% | +2,89% | FEEDBACK RAPIDO |
| BTC | 10g | Tecnico | CALIBRABILE | 2 | 0,00% | +2,32% | -2,32% | -2,93% | +3,04% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 12 | 58,33% | -0,12% | +0,12% | -0,45% | +0,63% | FEEDBACK RAPIDO |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 12 | 58,33% | -0,12% | +0,12% | -0,45% | +0,63% | FEEDBACK RAPIDO |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 12 | 58,33% | -0,12% | +0,12% | -0,45% | +0,63% | FEEDBACK RAPIDO |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 12 | 58,33% | -0,12% | +0,12% | -0,45% | +0,63% | FEEDBACK RAPIDO |
| DOGE | 1g | Tecnico | CALIBRABILE | 12 | 58,33% | -0,12% | +0,12% | -0,45% | +0,63% | FEEDBACK RAPIDO |
| DOGE | 1g | Classic technical | CALIBRABILE | 11 | 54,55% | -0,02% | +0,02% | -0,33% | +0,64% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 11 | 54,55% | -0,25% | +0,25% | -0,95% | +1,19% | FEEDBACK RAPIDO |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 11 | 54,55% | -0,25% | +0,25% | -0,95% | +1,19% | FEEDBACK RAPIDO |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 11 | 54,55% | -0,25% | +0,25% | -0,95% | +1,19% | FEEDBACK RAPIDO |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 11 | 54,55% | -0,25% | +0,25% | -0,95% | +1,19% | FEEDBACK RAPIDO |
| DOGE | 2g | Tecnico | CALIBRABILE | 11 | 54,55% | -0,25% | +0,25% | -0,95% | +1,19% | FEEDBACK RAPIDO |
| DOGE | 2g | Classic technical | CALIBRABILE | 10 | 50,00% | -0,04% | +0,04% | -0,82% | +1,52% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 10 | 60,00% | -0,50% | +0,50% | -1,70% | +1,94% | FEEDBACK RAPIDO |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 10 | 60,00% | -0,50% | +0,50% | -1,70% | +1,94% | FEEDBACK RAPIDO |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 10 | 60,00% | -0,50% | +0,50% | -1,70% | +1,94% | FEEDBACK RAPIDO |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 10 | 60,00% | -0,50% | +0,50% | -1,70% | +1,94% | FEEDBACK RAPIDO |
| DOGE | 3g | Tecnico | CALIBRABILE | 10 | 60,00% | -0,50% | +0,50% | -1,70% | +1,94% | FEEDBACK RAPIDO |
| DOGE | 3g | Classic technical | CALIBRABILE | 9 | 55,56% | -0,31% | +0,31% | -1,62% | +2,10% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 8 | 62,50% | -0,71% | +0,71% | -2,77% | +2,44% | FEEDBACK RAPIDO |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 8 | 62,50% | -0,71% | +0,71% | -2,77% | +2,44% | FEEDBACK RAPIDO |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 8 | 62,50% | -0,71% | +0,71% | -2,77% | +2,44% | FEEDBACK RAPIDO |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 8 | 62,50% | -0,71% | +0,71% | -2,77% | +2,44% | FEEDBACK RAPIDO |
| DOGE | 5g | Tecnico | CALIBRABILE | 8 | 62,50% | -0,71% | +0,71% | -2,77% | +2,44% | FEEDBACK RAPIDO |
| DOGE | 5g | Classic technical | CALIBRABILE | 7 | 57,14% | -0,40% | +0,40% | -2,62% | +2,71% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 6 | 66,67% | -0,72% | +0,72% | -2,68% | +3,21% | FEEDBACK RAPIDO |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 6 | 66,67% | -0,72% | +0,72% | -2,68% | +3,21% | FEEDBACK RAPIDO |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 6 | 66,67% | -0,72% | +0,72% | -2,68% | +3,21% | FEEDBACK RAPIDO |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 6 | 66,67% | -0,72% | +0,72% | -2,68% | +3,21% | FEEDBACK RAPIDO |
| DOGE | 7g | Tecnico | CALIBRABILE | 6 | 66,67% | -0,72% | +0,72% | -2,68% | +3,21% | FEEDBACK RAPIDO |
| DOGE | 7g | Classic technical | CALIBRABILE | 6 | 66,67% | -0,72% | +0,72% | -2,68% | +3,21% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 3 | 100,00% | -1,67% | +1,67% | -3,54% | +2,47% | FEEDBACK RAPIDO |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 3 | 100,00% | -1,67% | +1,67% | -3,54% | +2,47% | FEEDBACK RAPIDO |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 3 | 100,00% | -1,67% | +1,67% | -3,54% | +2,47% | FEEDBACK RAPIDO |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 3 | 100,00% | -1,67% | +1,67% | -3,54% | +2,47% | FEEDBACK RAPIDO |
| DOGE | 10g | Tecnico | CALIBRABILE | 3 | 100,00% | -1,67% | +1,67% | -3,54% | +2,47% | FEEDBACK RAPIDO |
| DOGE | 10g | Classic technical | CALIBRABILE | 3 | 100,00% | -1,67% | +1,67% | -3,54% | +2,47% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 11 | 45,45% | +0,06% | -0,75% | -0,35% | +0,89% | FEEDBACK RAPIDO |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 8 | 75,00% | -0,68% | +0,18% | -0,88% | +0,20% | FEEDBACK RAPIDO |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 11 | 63,64% | -0,20% | -0,17% | -0,54% | +0,66% | FEEDBACK RAPIDO |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 7 | 57,14% | -0,12% | +0,46% | -0,69% | +0,86% | FEEDBACK RAPIDO |
| SOL | 1g | Tecnico | CALIBRABILE | 12 | 50,00% | +0,06% | -0,36% | -0,31% | +0,86% | FEEDBACK RAPIDO |
| SOL | 1g | Classic technical | CALIBRABILE | 5 | 60,00% | +0,59% | -0,59% | +0,34% | +1,15% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 10 | 20,00% | -0,02% | -1,04% | -0,76% | +1,40% | FEEDBACK RAPIDO |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 8 | 50,00% | -0,35% | -0,44% | -1,23% | +0,88% | FEEDBACK RAPIDO |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 11 | 45,45% | -0,16% | -0,42% | -0,91% | +1,40% | FEEDBACK RAPIDO |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 7 | 42,86% | -0,41% | -0,28% | -1,27% | +1,46% | FEEDBACK RAPIDO |
| SOL | 2g | Tecnico | CALIBRABILE | 11 | 18,18% | -0,16% | -0,88% | -0,91% | +1,40% | FEEDBACK RAPIDO |
| SOL | 2g | Classic technical | CALIBRABILE | 4 | 25,00% | +1,03% | -1,03% | +0,68% | +1,67% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 9 | 11,11% | -0,25% | -1,76% | -2,14% | +2,32% | FEEDBACK RAPIDO |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 7 | 42,86% | -0,70% | -0,27% | -2,61% | +1,72% | FEEDBACK RAPIDO |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 10 | 40,00% | -0,40% | -0,28% | -2,19% | +2,22% | FEEDBACK RAPIDO |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 7 | 42,86% | -0,50% | -0,76% | -2,15% | +2,54% | FEEDBACK RAPIDO |
| SOL | 3g | Tecnico | CALIBRABILE | 10 | 30,00% | -0,40% | -0,80% | -2,19% | +2,22% | FEEDBACK RAPIDO |
| SOL | 3g | Classic technical | CALIBRABILE | 3 | 0,00% | +1,88% | -1,88% | -1,17% | +2,55% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 7 | 28,57% | -1,08% | -1,29% | -3,69% | +2,57% | FEEDBACK RAPIDO |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 6 | 66,67% | -1,15% | +0,48% | -3,95% | +2,11% | FEEDBACK RAPIDO |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 8 | 62,50% | -0,97% | +0,47% | -3,80% | +2,41% | FEEDBACK RAPIDO |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 6 | 50,00% | -1,74% | -0,52% | -3,74% | +2,48% | FEEDBACK RAPIDO |
| SOL | 5g | Tecnico | CALIBRABILE | 8 | 25,00% | -0,97% | -1,10% | -3,80% | +2,41% | FEEDBACK RAPIDO |
| SOL | 5g | Classic technical | CALIBRABILE | 1 | 0,00% | +2,92% | -2,92% | -3,42% | +3,10% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 5 | 40,00% | -0,59% | -1,92% | -3,91% | +3,01% | FEEDBACK RAPIDO |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 4 | 100,00% | -1,74% | +1,74% | -4,35% | +2,47% | FEEDBACK RAPIDO |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 6 | 83,33% | -1,04% | +1,04% | -4,02% | +2,76% | FEEDBACK RAPIDO |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 5 | 60,00% | -0,59% | -0,17% | -3,91% | +3,01% | FEEDBACK RAPIDO |
| SOL | 7g | Tecnico | CALIBRABILE | 6 | 16,67% | -1,04% | -2,35% | -4,02% | +2,76% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 2 | 50,00% | -1,00% | -1,00% | -5,79% | +1,67% | FEEDBACK RAPIDO |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 2 | 100,00% | -2,36% | +2,36% | -5,73% | +1,74% | FEEDBACK RAPIDO |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 3 | 66,67% | -1,39% | +1,39% | -5,70% | +1,62% | FEEDBACK RAPIDO |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 2 | 50,00% | -1,00% | -1,00% | -5,79% | +1,67% | FEEDBACK RAPIDO |
| SOL | 10g | Tecnico | CALIBRABILE | 3 | 33,33% | -1,39% | -1,39% | -5,70% | +1,62% | FEEDBACK RAPIDO |
| SOL | 10g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | FEEDBACK RAPIDO |

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

Generato: 2026-07-21 05:14 UTC

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
| BTC | 13 | FEEDBACK RAPIDO | 12 | 0 | 0 | 0 | Famiglia statistica | 1g | 41,67% | +0,19% | feedback rapido: utile da osservare, non da pesare |
| SOL | 13 | FEEDBACK RAPIDO | 12 | 0 | 0 | 0 | Tecnico | 1g | 50,00% | -0,36% | feedback rapido: utile da osservare, non da pesare |
| DOGE | 13 | FEEDBACK RAPIDO | 12 | 0 | 0 | 0 | Famiglia statistica | 1g | 58,33% | +0,12% | feedback rapido: utile da osservare, non da pesare |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Famiglia statistica | 12 | 41,67% | +0,19% | +0,19% | -0,00% | +0,86% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Microstruttura exchange | 1 | 100,00% | +2,00% | +2,00% | +1,48% | +2,25% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 11 | 27,27% | -0,84% | +0,18% | -0,02% | +0,90% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Famiglia statistica | 11 | 54,55% | +0,38% | +0,38% | -0,22% | +1,44% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 10 | 40,00% | -0,31% | +0,42% | -0,21% | +1,49% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Famiglia statistica | 10 | 70,00% | +0,52% | +0,52% | -1,11% | +2,17% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 9 | 33,33% | -0,30% | +0,77% | -1,01% | +2,31% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 8 | 50,00% | +0,84% | +0,84% | -2,36% | +2,70% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 7 | 42,86% | -0,53% | +0,81% | -2,23% | +2,79% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 6 | 66,67% | +1,52% | +1,52% | -2,22% | +3,40% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 5 | 60,00% | -0,39% | +1,89% | -2,01% | +3,57% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 3 | 100,00% | +1,72% | +1,72% | -3,05% | +2,89% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 2 | 0,00% | -2,32% | +2,32% | -2,93% | +3,04% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 11 | 54,55% | +0,02% | -0,02% | -0,33% | +0,64% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Famiglia statistica | 12 | 58,33% | +0,12% | -0,12% | -0,45% | +0,63% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 12 | 58,33% | +0,12% | -0,12% | -0,45% | +0,63% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Classic technical | 10 | 50,00% | +0,04% | -0,04% | -0,82% | +1,52% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Famiglia statistica | 11 | 54,55% | +0,25% | -0,25% | -0,95% | +1,19% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 11 | 54,55% | +0,25% | -0,25% | -0,95% | +1,19% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Classic technical | 9 | 55,56% | +0,31% | -0,31% | -1,62% | +2,10% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Famiglia statistica | 10 | 60,00% | +0,50% | -0,50% | -1,70% | +1,94% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 10 | 60,00% | +0,50% | -0,50% | -1,70% | +1,94% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Classic technical | 7 | 57,14% | +0,40% | -0,40% | -2,62% | +2,71% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 8 | 62,50% | +0,71% | -0,71% | -2,77% | +2,44% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 8 | 62,50% | +0,71% | -0,71% | -2,77% | +2,44% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Classic technical | 6 | 66,67% | +0,72% | -0,72% | -2,68% | +3,21% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 6 | 66,67% | +0,72% | -0,72% | -2,68% | +3,21% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 6 | 66,67% | +0,72% | -0,72% | -2,68% | +3,21% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Classic technical | 3 | 100,00% | +1,67% | -1,67% | -3,54% | +2,47% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 3 | 100,00% | +1,67% | -1,67% | -3,54% | +2,47% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 3 | 100,00% | +1,67% | -1,67% | -3,54% | +2,47% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Classic technical | 5 | 60,00% | -0,59% | +0,59% | +0,34% | +1,15% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Famiglia statistica | 8 | 75,00% | +0,18% | -0,68% | -0,88% | +0,20% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 12 | 50,00% | -0,36% | +0,06% | -0,31% | +0,86% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Classic technical | 4 | 25,00% | -1,03% | +1,03% | +0,68% | +1,67% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Famiglia statistica | 8 | 50,00% | -0,44% | -0,35% | -1,23% | +0,88% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 11 | 18,18% | -0,88% | -0,16% | -0,91% | +1,40% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Classic technical | 3 | 0,00% | -1,88% | +1,88% | -1,17% | +2,55% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Famiglia statistica | 7 | 42,86% | -0,27% | -0,70% | -2,61% | +1,72% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 10 | 30,00% | -0,80% | -0,40% | -2,19% | +2,22% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Classic technical | 1 | 0,00% | -2,92% | +2,92% | -3,42% | +3,10% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 6 | 66,67% | +0,48% | -1,15% | -3,95% | +2,11% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 8 | 25,00% | -1,10% | -0,97% | -3,80% | +2,41% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 4 | 100,00% | +1,74% | -1,74% | -4,35% | +2,47% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 6 | 16,67% | -2,35% | -1,04% | -4,02% | +2,76% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 2 | 100,00% | +2,36% | -2,36% | -5,73% | +1,74% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 3 | 33,33% | -1,39% | -1,39% | -5,70% | +1,62% | OSSERVA | 0,0 | BASSA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 12 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 12 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 12 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Famiglia statistica | 33 | 54,55% | +0,35% |
| BTC | BREVE | Microstruttura exchange | 1 | 100,00% | +2,00% |
| BTC | BREVE | Tecnico | 30 | 33,33% | -0,50% |
| BTC | SETTIMANALE | Famiglia statistica | 17 | 64,71% | +1,23% |
| BTC | SETTIMANALE | Tecnico | 14 | 42,86% | -0,74% |
| DOGE | BREVE | Classic technical | 30 | 53,33% | +0,12% |
| DOGE | BREVE | Famiglia statistica | 33 | 57,58% | +0,28% |
| DOGE | BREVE | Tecnico | 33 | 57,58% | +0,28% |
| DOGE | SETTIMANALE | Classic technical | 16 | 68,75% | +0,76% |
| DOGE | SETTIMANALE | Famiglia statistica | 17 | 70,59% | +0,89% |
| DOGE | SETTIMANALE | Tecnico | 17 | 70,59% | +0,89% |
| SOL | BREVE | Classic technical | 12 | 33,33% | -1,06% |
| SOL | BREVE | Famiglia statistica | 23 | 56,52% | -0,17% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Tecnico | 33 | 33,33% | -0,67% |
| SOL | SETTIMANALE | Classic technical | 1 | 0,00% | -2,92% |
| SOL | SETTIMANALE | Famiglia statistica | 12 | 83,33% | +1,22% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Tecnico | 17 | 23,53% | -1,59% |

## Aree ancora in attesa

| Asset | Famiglia | Righe senza controlli | Stato |
| --- | --- | --- | --- |
| BTC | BREVE | 8 | in attesa di controlli maturati |
| BTC | SETTIMANALE | 9 | in attesa di controlli maturati |
| BTC | SWING | 10 | in attesa di controlli maturati |
| BTC | MEDIO | 15 | in attesa di controlli maturati |
| SOL | BREVE | 3 | in attesa di controlli maturati |
| SOL | SETTIMANALE | 5 | in attesa di controlli maturati |
| SOL | SWING | 10 | in attesa di controlli maturati |
| SOL | MEDIO | 15 | in attesa di controlli maturati |
| DOGE | BREVE | 6 | in attesa di controlli maturati |
| DOGE | SETTIMANALE | 6 | in attesa di controlli maturati |
| DOGE | SWING | 10 | in attesa di controlli maturati |
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
| BTC     |         13 |               0 |          13 | RACCOLTA DATI | n/a              | n/a             | n/a                   | n/a            |
| SOL     |         13 |               0 |          13 | RACCOLTA DATI | n/a              | n/a             | n/a                   | n/a            |
| DOGE    |         13 |               0 |          13 | RACCOLTA DATI | n/a              | n/a             | n/a                   | n/a            |

Regola: sotto 60 controlli osserva soltanto; da 100+ controlli può diventare utile per correggere rischio spot/leva nel Decision Report.

## Ultima lettura rapida

| Asset   | Rischio spot   | Rischio leva   | Nota leva                                                               |
|:--------|:---------------|:---------------|:------------------------------------------------------------------------|
| BTC     | MEDIO          | MOLTO ALTO     | spot/tranche; se proprio leva, massimo 2x con margine molto largo       |
| SOL     | MEDIO          | MOLTO ALTO     | spot/tranche; se proprio leva, massimo 2x con margine molto largo       |
| DOGE    | MOLTO ALTO     | MOLTO ALTO     | spot preferibile; leva molto pericolosa anche 2x/3x senza margine largo |
<!-- RISK_CALIBRATION_END -->

</details>
<!-- COMPACT_SECTION_END:risk_calibration -->

<!-- COMPACT_SECTION_START:global_confluence -->
<details open>
<summary><strong>🌐 Global Confluence — quadro finale</strong></summary>

<!-- GLOBAL_CONFLUENCE_START -->
# Sintesi finale di confluenza

Generato: 2026-07-21 05:14 UTC


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
| BTC | +3 | MODERATAMENTE POSITIVA | Costruttivo prudente | MEDIA | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE | Prima resistenza sopra 65.508; conferma del doppio minimo sopra 67.248. | Sotto 57.748 il quadro tecnico peggiora. |
| SOL | +1 | MISTA / PARZIALE | Neutrale / misto | BASSA / RACCOLTA DATI | HOLD LEGGERO / ATTESA CONFERME | Doppio minimo maturo finché mantiene 75,94; nuova conferma tecnica sopra 78,88; milestone analogiche 98,30 / 115,29, valide soltanto se rientra anche il gap frattale. | Allarmi sotto 74,27 / 64,42 / 62,19. |
| DOGE | -6 | NEGATIVA | Ribassista | MEDIA | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE | Sopra 0.07923 migliora; sopra 0.07966 viene invalidato il pattern ribassista dominante. | Sotto 0.07097 il rischio ribassista aumenta. |

## Punteggi per modulo

| Asset | Scanner grezzo | Market grezzo | Famiglia statistica | Scanner path | Tecnico | Classic tech | Frattale SOL | Fractal path | RSI top-cycle | Lifecycle EMA | Exchange flow | Futures | Daily change | Totale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +2 | 0 | +2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | +1 | +3 |
| SOL | +1 | +2 | +2 | 0 | -1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | +1 |
| DOGE | -2 | -2 | -3 | 0 | -3 | -1 | 0 | 0 | 0 | 0 | 0 | 0 | +1 | -6 |

Le colonne **Scanner grezzo** e **Market grezzo** sono diagnostiche: nel totale entra soltanto la colonna **Famiglia statistica**.

## Lettura asset per asset

### BTC

- Confluenza: **MODERATAMENTE POSITIVA**
- Bias: **Costruttivo prudente**
- Punteggio finale: **+3**
- Affidabilità: **MEDIA**
- Azione coerente: **ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE**

BTC è l'asset messo meglio nel breve, ma lo score statistico ora conta Scanner e Market Regime una sola volta. La struttura macro resta debole: ha più senso accumulare a tranche sui pullback che inseguire il prezzo vicino alle resistenze.

Dettaglio moduli:

- Famiglia statistica: **+2** — Scanner grezzo +2, Market Regime grezzo 0, match regime 3. Regime ignorato: meno di 5 match utili. Punteggio contato nel Global: +2.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **+2** — Casi positivi 60,00%, return centrale 30g +5,34%. Direzione scanner: SALITA. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **0** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 3, positivi 30g 100,00%, return p50 +29,37%.
- Scanner path: **0** — Controlli disponibili 11. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **0** — Score tecnico 0/12, verdetto neutrale / misto, trend misto, struttura ribassista con massimi e minimi decrescenti, divergenza rialzista rsi, ribassista nascosta rsi, Wyckoff markdown / fase ribassista, pattern score 0 (rialzista Doppio minimo / CANDIDATO; ribassista Doppio massimo / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **0** — Score classico 3/12, verdetto ANTICIPATO / COSTRUTTIVO MA NON CONFERMATO, stage STAGE 4 / MARKDOWN, struttura MASSIMI E MINIMI CRESCENTI, Wyckoff ACCUMULO POSSIBILE / RANGE BASSO, volatilità locale BASSO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Non applicabile a questo asset.
- Fractal path: **0** — Non applicabile a questo asset.
- RSI top-cycle: **0** — Non applicabile a questo asset.
- Lifecycle EMA: **0** — Non applicabile a questo asset.
- Exchange flow: **0** — Flow +1.75, derivati +1.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +1.50; exchange 3/3, copertura 100%, consenso bull 0, bear 1, divergenze 0, campioni 4h 9 su 4.00h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias LEGGERMENTE POSITIVA / NON PESATA; confidenza ALTA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Misto, forza 1/5.
- Daily change: **+1** — BTC: cambiamento medio in miglioramento rispetto a ieri.

Conferme: Prima resistenza sopra 65.508; conferma del doppio minimo sopra 67.248.

Invalidazioni: Sotto 57.748 il quadro tecnico peggiora.

### SOL

- Confluenza: **MISTA / PARZIALE**
- Bias: **Neutrale / misto**
- Punteggio finale: **+1**
- Affidabilità: **BASSA / RACCOLTA DATI**
- Azione coerente: **HOLD LEGGERO / ATTESA CONFERME**

SOL è ancora in zona mista. Il frattale resta soltanto uno scenario contestuale: non è confermato dal prezzo e vale 0 punti operativi finché il gap non rientra. Meglio evitare leva e ragionare solo a tranche piccole.

Dettaglio moduli:

- Famiglia statistica: **+2** — Scanner grezzo +1, Market Regime grezzo +2, match regime 10. Scanner e regime concordi con almeno 10 match: bonus massimo di 1 punto. Punteggio contato nel Global: +2.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **+1** — Casi positivi 52,50%, return centrale 30g +0,70%. Direzione scanner: INCERTO. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **+2** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 10, positivi 30g 60,00%, return p50 +0,87%.
- Scanner path: **0** — Controlli disponibili 11. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **-1** — Score tecnico -2/12, verdetto neutrale / misto, trend ribassista, struttura ribassista con massimi e minimi decrescenti, divergenza nessuna, Wyckoff markdown / fase ribassista, pattern score +1 (rialzista Doppio minimo / MATURO; ribassista Doppio massimo / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **0** — Score classico -3/12, verdetto DEBOLE / NON CONFERMATO, stage STAGE 4 / MARKDOWN, struttura MASSIMI E MINIMI DECRESCENTI, Wyckoff RANGE / FASE NON CHIARA, volatilità locale BASSO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Verdetto ANALOGIA DEBOLE / SCENARIO SECONDARIO, somiglianza strutturale +64,43%, aderenza live +63,32%, errore live +18,34%, gap corrente +17,88%, peso operativo 0, tracking STRUTTURA STABILE, fase FRATTALE SOLO DI CONTESTO, rischio ALTO.
- Fractal path: **0** — Controlli disponibili 7, ma percorso ancorato non aderente: gap +17,88%, errore live +18,34%. Peso 0.
- RSI top-cycle: **0** — Rischio top-cycle RSI: BASSO.
- Lifecycle EMA: **0** — Contesto non pesato nel Global. Lifecycle score 4, bias SQUEEZE SETUP MODERATO, EMA200 112,78 $, upside EMA200 +44,19%, gap EMA50/EMA200 -2,99%, hit EMA200 12w +30,00%, trend STABILE / DA CONFERMARE. Peso Global forzato a 0.
- Exchange flow: **0** — Flow +1.75, derivati +0.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +1.50; exchange 3/3, copertura 100%, consenso bull 1, bear 1, divergenze 0, campioni 4h 9 su 4.00h; candidato +1, peso Global +0 (LOCKED / RACCOLTA 7G). Bias POSITIVA / CANDIDATA, ANCORA NON PESATA; confidenza MEDIA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +1 resta misurato separatamente.
- Futures: **0** — Lettura futures Misto, forza 1/5.
- Daily change: **0** — SOL: nessun cambiamento forte in miglioramento rispetto a ieri.

Conferme: Doppio minimo maturo finché mantiene 75,94; nuova conferma tecnica sopra 78,88; milestone analogiche 98,30 / 115,29, valide soltanto se rientra anche il gap frattale.

Invalidazioni: Allarmi sotto 74,27 / 64,42 / 62,19.

### DOGE

- Confluenza: **NEGATIVA**
- Bias: **Ribassista**
- Punteggio finale: **-6**
- Affidabilità: **MEDIA**
- Azione coerente: **STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE**

DOGE resta l'asset più debole. Anche senza contare due volte Scanner e Market Regime, la confluenza generale resta chiaramente negativa rispetto a BTC e SOL.

Dettaglio moduli:

- Famiglia statistica: **-3** — Scanner grezzo -2, Market Regime grezzo -2, match regime 29. Scanner e regime concordi con almeno 10 match: bonus massimo di 1 punto. Punteggio contato nel Global: -3.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **-2** — Casi positivi 32,50%, return centrale 30g -12,28%. Direzione scanner: DISCESA. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **-2** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 29, positivi 30g 31,03%, return p50 -13,83%.
- Scanner path: **0** — Controlli disponibili 11. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **-3** — Score tecnico -8/12, verdetto ribassista tecnico, trend ribassista, struttura ribassista con massimi e minimi decrescenti, divergenza ribassista nascosta rsi, Wyckoff possibile accumulazione, pattern score -1 (rialzista Doppio minimo / CANDIDATO; ribassista Triplo massimo / MATURO). Fonte: technical_structure_metrics.csv.
- Classic technical: **-1** — Score classico -5/12, verdetto RIBASSISTA / FRAGILE, stage STAGE 4 / MARKDOWN, struttura COMPRESSIONE / TRIANGOLO POSSIBILE, Wyckoff MARKDOWN / DEBOLEZZA, volatilità locale BASSO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Non applicabile a questo asset.
- Fractal path: **0** — Non applicabile a questo asset.
- RSI top-cycle: **0** — Non applicabile a questo asset.
- Lifecycle EMA: **0** — Non applicabile a questo asset.
- Exchange flow: **0** — Flow +1.75, derivati +0.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +0.75; exchange 3/3, copertura 100%, consenso bull 1, bear 1, divergenze 0, campioni 4h 9 su 4.00h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias LEGGERMENTE POSITIVA / NON PESATA; confidenza MEDIA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Rischio sotto, forza 2/5.
- Daily change: **+1** — DOGE: cambiamento medio in miglioramento rispetto a ieri.

Conferme: Sopra 0.07923 migliora; sopra 0.07966 viene invalidato il pattern ribassista dominante.

Invalidazioni: Sotto 0.07097 il rischio ribassista aumenta.


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

Generato: 2026-07-21 05:14 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [btc_macro_cycle_report.md](btc_macro_cycle_report.md)

Questo modulo descrive il contesto macro di Bitcoin. Non genera entrate tattiche, non autorizza leva e pesa **0** nel Global Confluence.

## Sintesi

| Voce | Valore | Lettura |
| --- | --- | --- |
| Prezzo BTC | 65.475 $ | prezzo corrente |
| Power Law centrale | 122.642 $ | deviazione -46,61% |
| Banda p10-p90 | 76.362 $ / 307.748 $ | SOTTO LA BANDA P10 |
| Percentile residuo | 2,59% | posizione storica nel corridoio |
| Esponente β | 5,8406 | R² log-log 91,99% |
| Stabilità β | BASSA | range 1,3072 cambiando finestra |
| Ultimo halving | 2024-04-19 | 823 giorni fa |
| Fase ciclo | 56,33% | percentuale indicativa del ciclo quadriennale |
| Peso Global | 0 | CONTESTO MACRO / DIAGNOSTICO |

La Power Law viene trattata come regressione empirica, non come legge fisica. Il report mostra quanto cambia l'esponente usando finestre iniziali diverse e la confronta con il benchmark ingenuo 'prezzo invariato'.

## Bitcoin Power Law

- Campione: 2014-09-17 → 2026-07-21 (4325 osservazioni)
- Formula stimata: prezzo ≈ exp(-39.3573) × giorni^5.8406
- Prezzo centrale oggi: **122.642 $**
- Posizione corrente: **SOTTO LA BANDA P10**, percentile 2,59%
- Scarto dal centro: **-46,61%**

![Bitcoin Power Law](btc_power_law_chart.png)

![Bitcoin Power Law log-log](btc_power_law_loglog_chart.png)

### Stabilità dell'esponente

| Inizio campione | β | R² log-log |
| --- | --- | --- |
| 2014 | 5,8406 | 91,99% |
| 2015 | 5,9271 | 91,56% |
| 2016 | 5,6168 | 87,80% |
| 2017 | 4,8864 | 82,89% |
| 2018 | 4,6199 | 78,35% |

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
| 2012-11-28 → 2016-07-09 | 2014-12-11 | -21,60% | -15,44% | -34,65% | +28,94% |
| 2016-07-09 → 2020-05-11 | 2018-09-07 | +2,10% | -45,55% | -39,63% | +62,63% |
| 2020-05-11 → 2024-04-19 | 2022-07-31 | -15,17% | -10,79% | -1,11% | +25,25% |

Campione molto piccolo: questi rendimenti sono contesto di ciclo, non probabilità affidabili.

## SOL/BTC e DOGE/BTC dentro il tempo Bitcoin

![Altcoin nel ciclo BTC](alt_btc_cycle_spirals.png)

| Asset | Coppia | Forza vs BTC | Score raw | Candidato | 30g | Peso Global |
| --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | RELATIVA MISTA / NON CONFERMATA | -1 | 0 | 4.644419178539194 | 0 |
| DOGE | DOGE/BTC | SOTTOPERFORMA BTC | -6 | -1 | -14.545270277076305 | 0 |

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

Generato: 2026-07-21 05:14 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [relative_strength_btc_report.md](relative_strength_btc_report.md)

Questo modulo controlla se SOL e DOGE stanno davvero battendo Bitcoin. Una salita in USD accompagnata da una coppia ALT/BTC ribassista è spesso soltanto trascinamento di BTC.

**Protezione iniziale:** il candidato relativo è limitato a -1/0/+1, ma il peso nel Global resta **0**. La coppia BTC conferma o indebolisce il tecnico USD; non viene sommata come secondo modulo indipendente.

## Sintesi

| Asset | Coppia | Prezzo | Score raw | Candidato | Peso Global | Forza vs BTC | Confidenza | 30g | Tecnico USD | Lettura combinata |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | 0.00119190 | -1 | 0 | 0 | RELATIVA MISTA / NON CONFERMATA | BASSA | +4,64% | MISTA | QUADRO MISTO / NESSUNA CONFERMA RELATIVA |
| DOGE | DOGE/BTC | 0.00000111 | -6 | -1 | 0 | SOTTOPERFORMA BTC | MEDIA | -14,55% | RIBASSISTA | DEBOLEZZA COMPLETA: scende in USD e contro BTC |

## Matrice di lettura

| ALT/USD | ALT/BTC | Interpretazione |
| --- | --- | --- |
| Rialzista | Rialzista | Conferma migliore: sale e batte BTC |
| Rialzista | Ribassista | Sale soprattutto perché BTC trascina il mercato |
| Ribassista | Rialzista | Forza relativa nascosta / possibile rotazione futura |
| Ribassista | Ribassista | Debolezza completa |

## SOL/BTC

- **Verdetto relativo:** RELATIVA MISTA / NON CONFERMATA (-1)
- **Candidato futuro:** 0; **peso attuale Global: 0**
- **Lettura combinata USD/BTC:** QUADRO MISTO / NESSUNA CONFERMA RELATIVA
- **Struttura:** MASSIMI E MINIMI CRESCENTI
- **Rendimenti relativi:** 7g -0,84%; 30g +4,64%; 90g +5,76%; 180g -17,69%
- **Daily:** RSI 48.52; MA50 0.00115968; MA200 0.00122254
- **Weekly:** MA30 0.00122080; RSI 46.91
- **Livelli:** supporto 0.00117300; resistenza 0.00119800; breakout 60g 0.00134900; breakdown 60g 0.00100900
- **Pattern:** DOPPIO MINIMO / TARGET RAGGIUNTO; neckline 0.00113200; target 0.00117200
- **Fibonacci:** VICINO — 50.0% a 0.00117900
- **Fonte:** Yahoo Finance SOL-BTC (coppia diretta)
- **Motivi score:** prezzo sopra MA50 daily; prezzo sotto MA200 daily; MA50 daily in salita; prezzo sotto MA30 weekly; MA30 weekly in discesa; struttura con massimi/minimi crescenti; MACD relativo negativo

![Grafico SOL/BTC](relative_strength_SOLBTC.png)

## DOGE/BTC

- **Verdetto relativo:** SOTTOPERFORMA BTC (-6)
- **Candidato futuro:** -1; **peso attuale Global: 0**
- **Lettura combinata USD/BTC:** DEBOLEZZA COMPLETA: scende in USD e contro BTC
- **Struttura:** MASSIMI E MINIMI DECRESCENTI
- **Rendimenti relativi:** 7g -3,67%; 30g -14,55%; 90g -10,77%; 180g -21,42%
- **Daily:** RSI 23.08; MA50 0.00000126; MA200 0.00000135
- **Weekly:** MA30 0.00000134; RSI 30.82
- **Livelli:** supporto 0.00000110; resistenza 0.00000121; breakout 60g 0.00000153; breakdown 60g 0.00000110
- **Pattern:** DOPPIO MASSIMO / CONFERMATO; neckline 0.00000124; target 0.00000098
- **Fibonacci:** NON ATTIVO — 23.6% a 0.00000120
- **Fonte:** Rapporto sintetico DOGE-USD / BTC-USD (sintetica)
- **Motivi score:** prezzo sotto MA50 daily; prezzo sotto MA200 daily; MA50 daily in discesa; prezzo sotto MA30 weekly; MA30 weekly in discesa; struttura con massimi/minimi decrescenti; RSI relativo debole; MACD relativo positivo

![Grafico DOGE/BTC](relative_strength_DOGEBTC.png)

## Backtest storico diagnostico

Il backtest usa soltanto indicatori disponibili alla data del segnale e campiona una volta a settimana. È utile subito, ma non sostituisce il tracker live: le soglie sono state definite prima di vedere il risultato.

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto direzione | Return futuro mediano |
| --- | --- | --- | --- | --- | --- |
| SOL | 7g | 202 | 51,98% | +1,96% | -1,34% |
| SOL | 30g | 200 | 48,00% | +4,76% | +0,44% |
| SOL | 90g | 194 | 54,12% | +10,43% | +1,07% |
| DOGE | 7g | 290 | 55,86% | +1,85% | -1,73% |
| DOGE | 30g | 287 | 52,61% | +1,98% | -3,49% |
| DOGE | 90g | 284 | 53,87% | +6,93% | -8,33% |

## Tracker live e gate futuro

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto | Stato | Peso Global |
| --- | --- | --- | --- | --- | --- | --- |
| SOL | 1g | 0 | n/a | n/a | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 3g | 0 | n/a | n/a | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 7g | 0 | n/a | n/a | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 14g | 0 | n/a | n/a | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 30g | 0 | n/a | n/a | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 1g | 10 | 90,00% | +0,80% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 3g | 8 | 87,50% | +1,63% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 7g | 4 | 100,00% | +3,32% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 14g | 0 | n/a | n/a | LOCKED / RACCOLTA LIVE | 0 |
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

Ultima candela SOL usata: **21 luglio 2026**

## Verdetto: ANALOGIA DEBOLE / SCENARIO SECONDARIO

- **Fase attuale:** FRATTALE SOLO DI CONTESTO
- **Somiglianza totale:** +64,43%
- **Somiglianza strutturale:** +64,43%
- **Aderenza prezzo live:** +63,32%
- **Errore medio live:** +18,34%
- **Gap prezzo corrente:** +17,88%
- **Peso operativo suggerito:** 0
- **Affidabilita:** BASSA
- **Rischio fase:** ALTO
- **Trend tracking:** STRUTTURA STABILE
- **Sintesi:** Esistono alcuni elementi comuni, ma non abbastanza per una conferma.
- **SOL è al giorno:** 45 dal bottom usato.
- **Giorno BTC equivalente:** 2023-01-05
- **Prossimo step:** Proiezione condizionale, non conferma operativa: **Spinta rialzista abbastanza pulita.** Zona bassa **78,18 $** intorno al **21 luglio 2026**; zona alta **98,30 $** intorno al **1 agosto 2026**; fine step circa **97,91 $** entro il **4 agosto 2026**.

## Somiglianza prima e dopo inizio programma

Questa sezione separa la somiglianza della forma dall'aderenza reale del prezzo.

- **Inizio programma/scanner:** 3 luglio 2026
- **Prima del programma** = backtest retroattivo.
- **Da inizio programma** = verifica live: è la parte più importante per l'uso operativo.

| Periodo | Date | Giorni | Aderenza prezzo | Errore medio | Gap ultimo | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| Prima del programma | 6 giugno 2026 -> 2 luglio 2026 | 27 | +87,95% | +6,02% | +21,89% | ABBASTANZA ALLINEATO |
| Da inizio programma | 3 luglio 2026 -> 21 luglio 2026 | 19 | +63,32% | +18,34% | +17,88% | STACCATO / NON ADERENTE |
| Totale dal bottom | 6 giugno 2026 -> 21 luglio 2026 | 46 | +77,78% | +11,11% | +17,88% | DEVIAZIONE MODERATA |

Nota: un frattale può avere una forma simile ma un prezzo distante. In quel caso non è operativo finché il gap non rientra.

## Lettura operativa veloce

Il frattale non deve generare acquisti o leva adesso. La forma è un contesto, ma l'aderenza live del prezzo è insufficiente.

| Voce | Risposta | Perché |
| --- | --- | --- |
| Uso operativo | NO | Il frattale vale 0 punti operativi finché il prezzo resta non aderente. |
| Aderenza live | +63,32% | Errore medio live +18,34%. |
| Gap corrente | +17,88% | Deve rientrare circa entro ±12%. |
| Prima conferma prezzo | 98,30 $ | Serve anche miglioramento del gap, non solo una candela sopra il livello. |
| Seconda conferma | 115,29 $ | Rende più credibile il percorso, ma non sostituisce l'aderenza. |
| Invalidazione soft | 74,27 $ | Sotto questa zona il quadro peggiora. |
| Invalidazione forte | 62,19 $ | Sotto il bottom il paragone è quasi rotto. |

## Target ciclo fino al top BTC 2025

| Voce | Valore |
| --- | --- |
| Stato | CONTESTO / NON OPERATIVO |
| Top BTC 2025 | 6 ottobre 2025 - 124.753 $ |
| Data SOL equivalente | 21 aprile 2029 |
| Target ciclo base da oggi | 579,28 $ |
| Massimo percorso base | 579,28 $ (21 aprile 2029) |

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
| Prima conferma | 98,30 $ | Deve accompagnarsi al rientro del gap. |
| Seconda conferma | 115,29 $ | Scenario più credibile. |
| Invalidazione soft | 74,27 $ | Il frattale si indebolisce. |
| Invalidazione forte | 62,19 $ | Il paragone si rompe. |

## Proiezione veloce con date SOL

| Orizzonte | Data SOL | BTC fece | SOL base | Min percorso | Max percorso |
| --- | --- | --- | --- | --- | --- |
| 7 giorni | 28 luglio 2026 | +12,07% | 87,62 $ | 78,18 $ | 87,62 $ |
| 14 giorni | 4 agosto 2026 | +25,24% | 97,91 $ | 78,18 $ | 98,30 $ |
| 30 giorni | 20 agosto 2026 | +38,58% | 108,34 $ | 78,18 $ | 110,40 $ |
| 60 giorni | 19 settembre 2026 | +33,22% | 104,15 $ | 78,18 $ | 115,29 $ |
| 90 giorni | 19 ottobre 2026 | +67,36% | 130,84 $ | 78,18 $ | 132,24 $ |
| 120 giorni | 18 novembre 2026 | +75,42% | 137,14 $ | 78,18 $ | 141,56 $ |

## Prossimi step se SOL segue BTC 2022

| Step | Date SOL | BTC fine | SOL zona bassa | SOL zona alta | SOL fine base | Lettura |
| --- | --- | --- | --- | --- | --- | --- |
| Step 1 - prossime 2 settimane | 21 luglio 2026 -> 4 agosto 2026 | +25,24% | 78,18 $ (21 luglio 2026) | 98,30 $ (1 agosto 2026) | 97,91 $ | Spinta rialzista abbastanza pulita. |
| Step 2 - primo mese | 5 agosto 2026 -> 20 agosto 2026 | +38,58% | 105,11 $ (9 agosto 2026) | 110,40 $ (14 agosto 2026) | 108,34 $ | Spinta rialzista abbastanza pulita. |
| Step 3 - secondo mese | 21 agosto 2026 -> 19 settembre 2026 | +33,22% | 100,54 $ (26 agosto 2026) | 115,29 $ (5 settembre 2026) | 104,15 $ | Spinta rialzista abbastanza pulita. |
| Step 4 - terzo mese | 20 settembre 2026 -> 19 ottobre 2026 | +67,36% | 93,74 $ (23 settembre 2026) | 132,24 $ (14 ottobre 2026) | 130,84 $ | Spinta rialzista abbastanza pulita. |

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
| Prezzo SOL | 78,18 $ |  |
| Weekly RSI | 41,23 / linea grezza 53,89 | LINEA NON AFFIDABILE / RISCHIO NON ATTIVO — IRREALISTICA / NON OPERATIVA |
| Monthly RSI | 41,44 / linea grezza 56,16 | RSI TROPPO BASSO PER RISCHIO TOP — VALIDA / USO PRUDENTE |
| Target ciclo base | 579,28 $ | Avanzamento +13,50% |
| Rischio top-cycle RSI | BASSO | Nessun segnale top-cycle macro attivo. Prezzo ancora lontano dal target ciclo; il filtro RSI resta solo di monitoraggio. |

## Lettura semplice

- Weekly: La top-line weekly non supera i controlli di qualità. Non viene usata per generare rischio top-cycle.
- Monthly: RSI monthly è 41,4, sotto la soglia prudente 55. Anche se fosse vicino alla linea, non è una vera zona di esaurimento ciclo.
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
| Prezzo SOL | 78,18 $ |
| TVL Solana | 4,97 mld $ |
| TVL 7g | +3,45% |
| DEX volume 24h | 1,83 mld $ |
| Fees 24h | 6,97 mln $ |
| Stablecoin su Solana | 15,71 mld $ |
| Stake ratio | 67,60% |
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
| Confronto precedente | 2026-07-20 |
| Fonte prezzi | Yahoo Finance SOL-USD weekly |
| Prezzo SOL | 78,18 $ |
| EMA200 weekly target | 112,78 $ |
| Upside verso EMA200 | +44,19% |
| Distanza prezzo da EMA200 | -30,65% |
| Gap EMA50/EMA200 | -2,99% |
| Stato cross | EMA50 SOTTO EMA200 |
| RSI weekly | 41,26 |
| Età SOL | 6,3 anni |
| Analoghi storici usati | 30 |
| Max analoghi per asset | 3 |
| Hit EMA200 12w analoghi | +30,00% |
| Max gain mediano 12w | +21,56% |
| Drawdown mediano 12w | -22,52% |

Lettura semplice:

**CONTESTO INTERESSANTE, SERVONO CONFERME DI PREZZO**

Autocontrollo: **STABILE / DA CONFERMARE**.

Questo modulo confronta SOL con altre crypto in fasi simili di età, distanza da EMA200, EMA50/EMA200 e RSI. Non usa stock market.

Nota importante: **questo modulo ora NON pesa più nel Global Confluence**. Resta solo come contesto di ciclo e come mappa verso EMA200 weekly. Il punteggio Global resta guidato da prezzo, scanner, regime, struttura tecnica, frattale, RSI e conferme reali.

Nota: se EMA50/EMA200 sono dentro ±2%, il modulo parla di medie sovrapposte / incrocio in corso, perché exchange diversi possono mostrare il cross leggermente prima o dopo.

<!-- Generato: 2026-07-21 05:14 UTC -->
<!-- MAJOR_ALT_LIFECYCLE_SQUEEZE_END -->

</details>
<!-- COMPACT_SECTION_END:major_alt_lifecycle -->

# Report giornaliero BTC / SOL / DOGE

Aggiornato il: **2026-07-21 05:12:23 UTC**

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
- SOL: nessun cambiamento forte rispetto a ieri.
- DOGE: cambiamento importante in miglioramento rispetto a ieri.

| Asset | Cambio | Tono | Verdetto oggi | Casi positivi oggi | Δ casi positivi |
| --- | --- | --- | --- | --- | --- |
| BTC | CAMBIAMENTO MEDIO | miglioramento | RIALZISTA | +60.00% | 0.00 punti |
| SOL | NESSUN CAMBIAMENTO FORTE | miglioramento | NEUTRALE / INCERTO | +52.50% | +2.50 punti |
| DOGE | CAMBIAMENTO MEDIO | miglioramento | RIBASSISTA | +32.50% | +2.50 punti |

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
| BTC | 62.198 $ | 72.019 $ | +44,12% | +15,79% | rimbalzo debole | 72.019 $ | 62.198 $ | +20,00% | -13,64% | spike storicamente più resistente |
| SOL | 74,27 $ | 86,00 $ | +31,03% | +15,79% | rimbalzo poco frequente | 86,00 $ | 74,27 $ | +15,79% | -13,64% | spike storicamente più resistente |
| DOGE | 0,06913 $ | 0,08005 $ | +25,71% | +15,79% | rimbalzo poco frequente | 0,08005 $ | 0,06913 $ | +50,00% | -13,64% | attenzione a prendere profitto |

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

- **BTC: su 40 casi simili, 34 prima sono scesi a -5,00%. Tra quei 34, 15 poi sono rimbalzati fino a +10,00%. Percentuale: +44,12% (15/34). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.**
- **BTC: su 40 casi simili, 25 prima sono saliti a +10,00%. Tra quei 25, 5 poi sono scaricati a -5,00%. Percentuale: +20,00% (5/25). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.**
- **SOL: su 40 casi simili, 29 prima sono scesi a -5,00%. Tra quei 29, 9 poi sono rimbalzati fino a +10,00%. Percentuale: +31,03% (9/29). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.**
- **SOL: su 40 casi simili, 19 prima sono saliti a +10,00%. Tra quei 19, 3 poi sono scaricati a -5,00%. Percentuale: +15,79% (3/19). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.**
- **DOGE: su 40 casi simili, 35 prima sono scesi a -5,00%. Tra quei 35, 9 poi sono rimbalzati fino a +10,00%. Percentuale: +25,71% (9/35). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.**
- **DOGE: su 40 casi simili, 20 prima sono saliti a +10,00%. Tra quei 20, 10 poi sono scaricati a -5,00%. Percentuale: +50,00% (10/20). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: attenzione a prendere profitto.**

<!-- BOUNCE_AFTER_DRAWDOWN_END -->

</details>
<!-- COMPACT_SECTION_END:bounce_after_drawdown -->

<!-- COMPACT_SECTION_START:scanner_forecast -->
<details>
<summary><strong>🔭 Cono probabilistico dello scanner</strong></summary>

<!-- SCANNER_FORECAST_TRACKER_START -->
# Scanner forecast path / cono probabilistico

Generato: 2026-07-21 05:13:51 UTC


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
| BTC | 2026-07-21 | 65.472 $ | SALITA | 60,00% | 47.826,22 $ | 58.392,28 $ | 68.968,40 $ | 80.082,47 $ | 83.516,80 $ |
| SOL | 2026-07-21 | 78,18 $ | INCERTO | 52,50% | 60,08 $ | 68,09 $ | 78,73 $ | 87,79 $ | 91,80 $ |
| DOGE | 2026-07-21 | 0.07277 $ | DISCESA | 32,50% | 0.05162 $ | 0.05680 $ | 0.06383 $ | 0.07996 $ | 0.09210 $ |

## Grafici

### BTC

![Scanner forecast BTC](scanner_forecast_BTC.png)

#### Verifica storica e discrepanza

![Verifica storica cono BTC](scanner_forecast_history_BTC.png)

- Cono congelato il **2026-07-10**; verificato fino al **2026-07-21**; stato **PARZIALE 11/30g**.
- Reale **65.471,66 $**; p50 previsto **69.497,05 $**; scarto **-5,79%**.
- Errore medio assoluto **3,96%**; massimo **7,75%**; DENTRO p10-p90; DENTRO p25-p75.

### SOL

![Scanner forecast SOL](scanner_forecast_SOL.png)

#### Verifica storica e discrepanza

![Verifica storica cono SOL](scanner_forecast_history_SOL.png)

- Cono congelato il **2026-07-10**; verificato fino al **2026-07-21**; stato **PARZIALE 11/30g**.
- Reale **78,21 $**; p50 previsto **75,15 $**; scarto **4,07%**.
- Errore medio assoluto **2,80%**; massimo **5,38%**; DENTRO p10-p90; DENTRO p25-p75.

### DOGE

![Scanner forecast DOGE](scanner_forecast_DOGE.png)

#### Verifica storica e discrepanza

![Verifica storica cono DOGE](scanner_forecast_history_DOGE.png)

- Cono congelato il **2026-07-10**; verificato fino al **2026-07-21**; stato **PARZIALE 11/30g**.
- Reale **0.07281 $**; p50 previsto **0.06693 $**; scarto **8,78%**.
- Errore medio assoluto **2,04%**; massimo **8,78%**; DENTRO p10-p90; DENTRO p25-p75.

## Accuratezza percorso scanner

| Asset   | Giorno   |   Controlli | Dentro p10-p90   | Dentro p25-p75   | Errore medio abs vs p50   | Errore medio vs p50   |
|:--------|:---------|------------:|:-----------------|:-----------------|:--------------------------|:----------------------|
| BTC | 1g | 11 | 100,00% | 72,73% | 1,97% | -0,01% |
| BTC | 3g | 9 | 100,00% | 66,67% | 2,99% | -1,35% |
| BTC | 7g | 5 | 100,00% | 60,00% | 2,74% | -2,74% |
| BTC | 14g | 0 | n/a | n/a | n/a | n/a |
| BTC | 30g | 0 | n/a | n/a | n/a | n/a |
| SOL | 1g | 11 | 72,73% | 45,45% | 2,70% | 0,14% |
| SOL | 3g | 9 | 100,00% | 44,44% | 2,90% | -0,48% |
| SOL | 7g | 5 | 100,00% | 100,00% | 3,01% | 0,16% |
| SOL | 14g | 0 | n/a | n/a | n/a | n/a |
| SOL | 30g | 0 | n/a | n/a | n/a | n/a |
| DOGE | 1g | 11 | 100,00% | 54,55% | 2,49% | 0,98% |
| DOGE | 3g | 9 | 100,00% | 88,89% | 2,14% | 0,55% |
| DOGE | 7g | 5 | 100,00% | 100,00% | 4,68% | 4,68% |
| DOGE | 14g | 0 | n/a | n/a | n/a | n/a |
| DOGE | 30g | 0 | n/a | n/a | n/a | n/a |

## Calibratore shadow

Il cono ufficiale resta grezzo e invariato. Il calibratore usa soltanto previsioni passate già mature, campionate una volta a settimana per ridurre la falsa indipendenza. Ogni orizzonte si attiva a 30 controlli indipendenti: parte al 25% della correzione stimata e cresce gradualmente fino al 100% a 100 controlli.

| Asset   | Orizzonte   |   Controlli indipendenti |   Soglia | Stato                  | Forza correzione   | Shift p50   |   Scala p10-p90 |
|:--------|:------------|-------------------------:|---------:|:-----------------------|:-------------------|:------------|----------------:|
| BTC | 1g | 3 | 30 | RACCOLTA (27 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 3g | 2 | 30 | RACCOLTA (28 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 7g | 2 | 30 | RACCOLTA (28 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 14g | 0 | 30 | RACCOLTA (30 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 30g | 0 | 30 | RACCOLTA (30 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 1g | 3 | 30 | RACCOLTA (27 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 3g | 2 | 30 | RACCOLTA (28 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 7g | 2 | 30 | RACCOLTA (28 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 14g | 0 | 30 | RACCOLTA (30 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 30g | 0 | 30 | RACCOLTA (30 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 1g | 3 | 30 | RACCOLTA (27 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 3g | 2 | 30 | RACCOLTA (28 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 7g | 2 | 30 | RACCOLTA (28 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 14g | 0 | 30 | RACCOLTA (30 mancanti) | 0,0% | 0,00% | 1,000 |
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

Righe salvate nello storico: **27**.

Questa sezione tiene un diario delle previsioni giornaliere a 30 giorni, senza appesantire il report principale.

| Data | Asset | Prezzo | Direzione | Casi positivi | Return p50 | Drawdown p50 | Max gain p50 | Controllo 30g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-07-21 | BTC | 65.472 $ | SALITA | 60,00% | 68.968 $ | 58.162 $ | 73.422 $ | 2026-08-20 |
| 2026-07-21 | DOGE | 0,07000 $ | DISCESA | 32,50% | 0,06000 $ | 0,06000 $ | 0,08000 $ | 2026-08-20 |
| 2026-07-21 | SOL | 78,18 $ | INCERTO | 52,50% | 78,73 $ | 70,65 $ | 85,76 $ | 2026-08-20 |

<!-- FORECAST_30D_HISTORY_END -->

</details>
<!-- COMPACT_SECTION_END:scanner_forecast -->

<!-- COMPACT_SECTION_START:extreme_cases -->
<details>
<summary><strong>⚠️ Percorso dei casi estremi</strong></summary>

<!-- EXTREME_CASES_PATH_START -->
# Extreme cases path report

Generato: 2026-07-21 05:13 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [extreme_cases_path_report.md](extreme_cases_path_report.md)

Questo report si attiva quando i casi positivi o negativi sono almeno **80%**.

Ora misura anche il **rialzo massimo prima della discesa principale**, quindi distingue uno spike iniziale da una discesa quasi immediata.

## Trigger estremi

| Asset   | Direzione   | Trigger   | Percentuale   | Motivo                           |   Match disponibili |
|:--------|:------------|:----------|:--------------|:---------------------------------|--------------------:|
| BTC     | NESSUNO     | NO        | +60,00%       | Nessun lato sopra soglia estrema |                  40 |
| SOL     | NESSUNO     | NO        | +52,50%       | Nessun lato sopra soglia estrema |                  40 |
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
- Casi positivi / salita storica: **60,00%**
- Casi negativi / discesa storica: **40,00%**
- Quanto è netto il segnale: **debole**
- Prezzo attuale: **65.471,66 $**
- Return normale fra 30 giorni: **68.968,40 $** (5,34%)
- Drawdown normale durante il mese: **58.161,65 $** (-11,17%)
- Drawdown brutto da rispettare: **54.626,54 $** (-16,56%)
- Max gain normale durante il mese: **73.422,14 $** (12,14%)
- Max gain buono / take profit ottimistico: **80.559,93 $** (23,05%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Solana
- Direzione più probabile a 30 giorni: **INCERTO**
- Casi positivi / salita storica: **52,50%**
- Casi negativi / discesa storica: **47,50%**
- Quanto è netto il segnale: **molto debole / quasi pari**
- Prezzo attuale: **78,18 $**
- Return normale fra 30 giorni: **78,73 $** (0,70%)
- Drawdown normale durante il mese: **70,65 $** (-9,63%)
- Drawdown brutto da rispettare: **64,58 $** (-17,40%)
- Max gain normale durante il mese: **85,76 $** (9,69%)
- Max gain buono / take profit ottimistico: **93,68 $** (19,83%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Dogecoin
- Direzione più probabile a 30 giorni: **DISCESA**
- Casi positivi / salita storica: **32,50%**
- Casi negativi / discesa storica: **67,50%**
- Quanto è netto il segnale: **medio**
- Prezzo attuale: **0,07 $**
- Return normale fra 30 giorni: **0,06 $** (-12,28%)
- Drawdown normale durante il mese: **0,06 $** (-20,97%)
- Drawdown brutto da rispettare: **0,05 $** (-30,24%)
- Max gain normale durante il mese: **0,08 $** (11,92%)
- Max gain buono / take profit ottimistico: **0,09 $** (23,40%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Messaggio del giorno

Il quadro generale oggi è misto. Alcuni asset possono avere lettura diversa, quindi è meglio valutare asset per asset.

---

# Mappa semplice asset per asset

# Bitcoin — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟢 VERDE / Favorevole
**Prezzo attuale:** 65.471,66 $

**Direzione più probabile a 30 giorni:** **SALITA**
- Probabilità storica di salita: **60,00%**
- Probabilità storica di discesa: **40,00%**
- Quanto è netto il segnale: **debole**

## Come leggere questa parte

- **Probabilità storica di salita** = su 40 casi simili, quanti hanno chiuso sopra dopo 30 giorni.
- **Probabilità storica di discesa** = su 40 casi simili, quanti hanno chiuso sotto dopo 30 giorni.
- **Quanto è netto il segnale** = quanto è grande la differenza tra salita e discesa. Non vuol dire certezza, vuol dire solo che il risultato storico non è vicino al 50/50.

La lettura principale è rialzista, con segnale debole. Nei casi storici simili, il prezzo ha chiuso sopra dopo 30 giorni più spesso di quanto abbia chiuso sotto.

## 1. Return 30d — prezzo fra 30 giorni

**Return** significa rendimento finale. Qui guardiamo dove potrebbe stare il prezzo **alla fine dei 30 giorni**, non durante il percorso.

- Se va molto male: **47.826,22 $** (-26,95%)
- Se va male: **58.392,28 $** (-10,81%)
- Scenario normale: **68.968,40 $** (5,34%)
- Se va bene: **80.082,47 $** (22,32%)
- Se va molto bene: **83.516,80 $** (27,56%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **58.161,65 $** (-11,17%)
- Discesa brutta: **54.626,54 $** (-16,56%)
- Discesa molto brutta: **46.260,81 $** (-29,34%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **73.422,14 $** (12,14%)
- Rialzo buono: **80.559,93 $** (23,05%)
- Rialzo molto forte: **86.562,81 $** (32,21%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Bitcoin tendeva a muoversi tra una zona bassa intorno a **58.161,65 $** e uno spike normale intorno a **73.422,14 $**.

La chiusura a 30 giorni era più spesso positiva: salita 60,00%, discesa 40,00%. Quindi la lettura principale è favorevole.

Nota leva BTC: se la liquidazione è vicina a 51.000 $, guarda soprattutto la discesa brutta e molto brutta. Il prezzo può recuperare dopo, ma la leva può saltare prima.

---

# Solana — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟡 GIALLO / Incerto
**Prezzo attuale:** 78,18 $

**Direzione più probabile a 30 giorni:** **INCERTO**
- Probabilità storica di salita: **52,50%**
- Probabilità storica di discesa: **47,50%**
- Quanto è netto il segnale: **molto debole / quasi pari**

## Come leggere questa parte

- **Probabilità storica di salita** = su 40 casi simili, quanti hanno chiuso sopra dopo 30 giorni.
- **Probabilità storica di discesa** = su 40 casi simili, quanti hanno chiuso sotto dopo 30 giorni.
- **Quanto è netto il segnale** = quanto è grande la differenza tra salita e discesa. Non vuol dire certezza, vuol dire solo che il risultato storico non è vicino al 50/50.

La lettura principale è incerta, con segnale molto debole / quasi pari. Nei casi storici simili non c'è stato un vantaggio chiaro né per salita né per discesa.

## 1. Return 30d — prezzo fra 30 giorni

**Return** significa rendimento finale. Qui guardiamo dove potrebbe stare il prezzo **alla fine dei 30 giorni**, non durante il percorso.

- Se va molto male: **60,08 $** (-23,15%)
- Se va male: **68,09 $** (-12,91%)
- Scenario normale: **78,73 $** (0,70%)
- Se va bene: **87,79 $** (12,29%)
- Se va molto bene: **91,80 $** (17,42%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **70,65 $** (-9,63%)
- Discesa brutta: **64,58 $** (-17,40%)
- Discesa molto brutta: **59,88 $** (-23,41%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **85,76 $** (9,69%)
- Rialzo buono: **93,68 $** (19,83%)
- Rialzo molto forte: **99,86 $** (27,74%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Solana tendeva a muoversi tra una zona bassa intorno a **70,65 $** e uno spike normale intorno a **85,76 $**.

La chiusura a 30 giorni è incerta: salita 52,50%, discesa 47,50%. Non c'è un vantaggio netto.

---

# Dogecoin — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🔴 ROSSO / Prudenza
**Prezzo attuale:** 0,07 $

**Direzione più probabile a 30 giorni:** **DISCESA**
- Probabilità storica di salita: **32,50%**
- Probabilità storica di discesa: **67,50%**
- Quanto è netto il segnale: **medio**

## Come leggere questa parte

- **Probabilità storica di salita** = su 40 casi simili, quanti hanno chiuso sopra dopo 30 giorni.
- **Probabilità storica di discesa** = su 40 casi simili, quanti hanno chiuso sotto dopo 30 giorni.
- **Quanto è netto il segnale** = quanto è grande la differenza tra salita e discesa. Non vuol dire certezza, vuol dire solo che il risultato storico non è vicino al 50/50.

La lettura principale è ribassista, con segnale medio. Nei casi storici simili, il prezzo ha chiuso sotto dopo 30 giorni più spesso di quanto abbia chiuso sopra.

## 1. Return 30d — prezzo fra 30 giorni

**Return** significa rendimento finale. Qui guardiamo dove potrebbe stare il prezzo **alla fine dei 30 giorni**, non durante il percorso.

- Se va molto male: **0,05 $** (-29,07%)
- Se va male: **0,06 $** (-21,94%)
- Scenario normale: **0,06 $** (-12,28%)
- Se va bene: **0,08 $** (9,88%)
- Se va molto bene: **0,09 $** (26,56%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **0,06 $** (-20,97%)
- Discesa brutta: **0,05 $** (-30,24%)
- Discesa molto brutta: **0,05 $** (-37,07%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **0,08 $** (11,92%)
- Rialzo buono: **0,09 $** (23,40%)
- Rialzo molto forte: **0,10 $** (31,64%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Dogecoin tendeva a muoversi tra una zona bassa intorno a **0,06 $** e uno spike normale intorno a **0,08 $**.

La chiusura a 30 giorni era più spesso negativa: salita 32,50%, discesa 67,50%. Quindi la lettura principale è prudente/debole.

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

**Prezzo attuale:** 65.471,66 $

Bitcoin ha un segnale favorevole. La statistica dei casi simili indica più possibilità di salita che di discesa, ma resta comunque una probabilità, non una certezza.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **60,00%**
- Casi negativi dopo 30 giorni: **40,00%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **86,28%**
- Rendimento medio dopo 30 giorni: **3,37%**
- Rendimento centrale dopo 30 giorni: **5,34%**
- Discesa media durante i 30 giorni: **-13,79%**
- Massimo rialzo medio durante i 30 giorni: **17,48%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **67.679,72 $**
- Scenario centrale a 30 giorni: **68.968,40 $**
- Zona di rischio media: **56.443,08 $**
- Zona di rialzo media: **76.917,81 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -26,95% → **47.826,22 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -10,81% → **58.392,28 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: 5,34% → **68.968,40 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 22,32% → **80.082,47 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 27,56% → **83.516,80 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -29,34% → **46.260,81 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -16,56% → **54.626,54 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -11,17% → **58.161,65 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -7,66% → **60.454,93 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: -3,82% → **62.969,74 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 0,00% → **65.471,66 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 6,14% → **69.493,78 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 12,14% → **73.422,14 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 23,05% → **80.559,93 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 32,21% → **86.562,81 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| LRC-USD         | 2018-09-29   | 2019-01-06 |        91.57 |        21.04 |         -13.46 |         133.38 |
| XRP-USD         | 2019-10-04   | 2020-01-11 |        90.29 |        29.37 |           0    |          33.33 |
| FIL-USD         | 2023-06-29   | 2023-10-06 |        88.82 |        23.33 |          -4.87 |          23.33 |
| XLM-USD         | 2020-07-15   | 2020-10-22 |        88.52 |        27.12 |         -12.53 |          27.12 |
| SAND-USD        | 2023-06-24   | 2023-10-01 |        88.52 |         7.39 |         -12.66 |          11.3  |
| DOGE-USD        | 2020-07-15   | 2020-10-22 |        88    |        32.09 |          -5.2  |          32.09 |
| ONE-USD         | 2020-01-17   | 2020-04-25 |        87.88 |         4.38 |          -2.69 |          13.22 |
| ADA-USD         | 2019-05-22   | 2019-08-29 |        87.45 |       -13.13 |         -15.94 |          19.23 |
| KSM-USD         | 2024-02-18   | 2024-05-27 |        87.13 |       -29.07 |         -29.08 |           0.39 |
| APT-USD         | 2024-05-27   | 2024-09-05 |        87.04 |        -1.32 |          -3.95 |           7.11 |

---

# Approfondimento tecnico — Solana (SOL-USD)

## Semaforo: 🟡 GIALLO / Incerto

**Prezzo attuale:** 78,18 $

Solana è in una situazione incerta. Lo scanner non vede un vantaggio chiaro né per la salita né per la discesa. In questi casi è meglio non forzare la previsione.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **52,50%**
- Casi negativi dopo 30 giorni: **47,50%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **77,37%**
- Rendimento medio dopo 30 giorni: **-0,50%**
- Rendimento centrale dopo 30 giorni: **0,70%**
- Discesa media durante i 30 giorni: **-11,64%**
- Massimo rialzo medio durante i 30 giorni: **15,01%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **77,79 $**
- Scenario centrale a 30 giorni: **78,73 $**
- Zona di rischio media: **69,08 $**
- Zona di rialzo media: **89,91 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -23,15% → **60,08 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -12,91% → **68,09 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: 0,70% → **78,73 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 12,29% → **87,79 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 17,42% → **91,80 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -23,41% → **59,88 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -17,40% → **64,58 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -9,63% → **70,65 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -4,96% → **74,30 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: -0,50% → **77,79 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 0,08% → **78,24 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 3,94% → **81,26 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 9,69% → **85,76 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 19,83% → **93,68 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 27,74% → **99,86 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| DASH-USD        | 2024-04-25   | 2024-08-02 |        81.7  |        -6.67 |          -9.34 |          10.9  |
| WAVES-USD       | 2019-03-03   | 2019-06-10 |        80.84 |       -27.46 |         -27.46 |           4.37 |
| QTUM-USD        | 2018-09-29   | 2019-01-06 |        80.47 |       -23.14 |         -23.14 |           4.01 |
| BNB-USD         | 2025-12-16   | 2026-03-25 |        79.73 |        -1.69 |          -9.92 |           0    |
| RUNE-USD        | 2025-12-17   | 2026-03-26 |        79.6  |        18.5  |          -7.03 |          20.04 |
| XLM-USD         | 2020-01-17   | 2020-04-25 |        79.32 |         6.35 |           0    |          21.39 |
| XRP-USD         | 2020-01-17   | 2020-04-25 |        78.84 |         1.17 |          -0.51 |          16.6  |
| ENJ-USD         | 2018-09-29   | 2019-01-06 |        78.64 |       -29.18 |         -29.18 |           0    |
| SOL-USD         | 2025-12-14   | 2026-03-23 |        78.63 |        -4.93 |         -13.64 |           0.31 |
| NEAR-USD        | 2024-04-25   | 2024-08-02 |        78.39 |       -16.23 |         -23.24 |           9.72 |

---

# Approfondimento tecnico — Dogecoin (DOGE-USD)

## Semaforo: 🔴 ROSSO / Prudenza

**Prezzo attuale:** 0,07 $

Dogecoin richiede prudenza. La statistica dei casi simili indica più possibilità di discesa che di salita. Con leva, il rischio principale è il drawdown durante il percorso.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **32,50%**
- Casi negativi dopo 30 giorni: **67,50%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **87,30%**
- Rendimento medio dopo 30 giorni: **-5,44%**
- Rendimento centrale dopo 30 giorni: **-12,28%**
- Discesa media durante i 30 giorni: **-19,88%**
- Massimo rialzo medio durante i 30 giorni: **13,09%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **0,07 $**
- Scenario centrale a 30 giorni: **0,06 $**
- Zona di rischio media: **0,06 $**
- Zona di rialzo media: **0,08 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -29,07% → **0,05 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -21,94% → **0,06 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: -12,28% → **0,06 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 9,88% → **0,08 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 26,56% → **0,09 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -37,07% → **0,05 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -30,24% → **0,05 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -20,97% → **0,06 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -7,23% → **0,07 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: -4,35% → **0,07 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 0,00% → **0,07 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 0,00% → **0,07 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 11,92% → **0,08 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 23,40% → **0,09 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 31,64% → **0,10 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| DASH-USD        | 2022-03-02   | 2022-06-09 |        90.18 |       -17.14 |         -27.85 |           0    |
| ZEC-USD         | 2019-05-27   | 2019-09-03 |        89.9  |       -18.14 |         -23.06 |          15.5  |
| INJ-USD         | 2022-03-04   | 2022-06-11 |        88.94 |       -32.36 |         -35.14 |           0    |
| VET-USD         | 2022-03-04   | 2022-06-11 |        88.55 |       -20.06 |         -21.27 |           0    |
| QTUM-USD        | 2022-03-02   | 2022-06-09 |        88.53 |       -22.26 |         -33.72 |           0    |
| 1INCH-USD       | 2022-03-04   | 2022-06-11 |        88.44 |       -14.71 |         -20.68 |           8.97 |
| ENJ-USD         | 2022-03-07   | 2022-06-14 |        88.42 |        10.19 |          -8.9  |          29.08 |
| NEAR-USD        | 2022-03-12   | 2022-06-19 |        88.39 |        38.17 |          -2.98 |          38.17 |
| THETA-USD       | 2022-03-06   | 2022-06-13 |        88.35 |        -0.29 |          -5.56 |          27.8  |
| OMG-USD         | 2022-03-02   | 2022-06-09 |        88.26 |       -28.92 |         -36.72 |           0    |

</details>
<!-- COMPACT_SECTION_END:scanner_full_detail -->

<!-- COMPACT_SECTION_START:market_regime -->
<details>
<summary><strong>🌦️ Market Regime Match</strong></summary>

<!-- MARKET_REGIME_MATCH_START -->
# Market Regime Match Report


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [market_regime_match_report.md](market_regime_match_report.md)

Generated: 2026-07-21 05:14 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | BEAR | 65.472 $ | False | -16.27% | -9.73% | BEAR | -16.27% | -9.73% |
| DOGE-USD | BEAR | 0.07277 $ | False | -23.94% | -15.64% | BEAR | -16.27% | -9.73% |
| SOL-USD | BEAR | 78,18 $ | False | -10.02% | -16.70% | BEAR | -16.27% | -9.73% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 60.00% | 5.34% | 22.32% | 27.56% | -11.17% | -29.34% | 12.14% | 23.05% | 32.21% | 60.00% | 7.92% | 34.47% | 78.22% |
| BTC-USD | SAME_BTC_REGIME | 4 | 75.00% | 17.45% | 29.38% | 29.40% | -8.78% | -10.66% | 23.06% | 35.92% | 40.58% | 50.00% | -0.17% | 8.00% | 19.96% |
| BTC-USD | SAME_ASSET_REGIME | 18 | 88.89% | 21.58% | 23.24% | 29.39% | -10.00% | -13.09% | 22.19% | 26.20% | 36.44% | 77.78% | 29.98% | 44.79% | 57.68% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 3 | 100.00% | 29.37% | 29.40% | 29.41% | -7.64% | -10.31% | 33.33% | 38.51% | 41.62% | 33.33% | -1.70% | 13.12% | 22.01% |
| DOGE-USD | ALL_MATCHES | 40 | 32.50% | -12.28% | 9.88% | 26.56% | -20.97% | -37.07% | 11.92% | 23.40% | 31.64% | 67.50% | 8.67% | 41.29% | 72.43% |
| DOGE-USD | SAME_BTC_REGIME | 30 | 33.33% | -13.63% | 9.49% | 19.66% | -22.47% | -37.07% | 1.04% | 21.78% | 29.33% | 70.00% | 7.11% | 42.84% | 65.48% |
| DOGE-USD | SAME_ASSET_REGIME | 32 | 31.25% | -13.63% | 8.91% | 18.64% | -22.47% | -36.57% | 1.38% | 21.66% | 28.95% | 71.88% | 8.67% | 41.29% | 71.42% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 29 | 31.03% | -13.83% | 8.62% | 15.82% | -23.04% | -37.42% | 0.00% | 17.32% | 28.06% | 68.97% | 7.07% | 40.52% | 66.22% |
| SOL-USD | ALL_MATCHES | 40 | 52.50% | 0.70% | 12.29% | 17.42% | -9.63% | -23.41% | 9.69% | 19.83% | 27.74% | 57.50% | 2.52% | 22.14% | 44.32% |
| SOL-USD | SAME_BTC_REGIME | 12 | 50.00% | 0.18% | 9.38% | 12.50% | -8.84% | -23.16% | 5.73% | 10.00% | 12.50% | 66.67% | 2.52% | 8.80% | 9.82% |
| SOL-USD | SAME_ASSET_REGIME | 23 | 65.22% | 1.17% | 14.12% | 20.53% | -7.77% | -22.97% | 9.67% | 20.23% | 26.49% | 60.87% | 3.69% | 16.44% | 41.76% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 10 | 60.00% | 0.87% | 10.45% | 13.26% | -7.66% | -22.41% | 7.41% | 10.66% | 13.41% | 70.00% | 5.72% | 8.95% | 11.08% |

## Breakdown by historical BTC regime

| target   | group                   |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 4 | 75.00% | 17.45% | -8.78% | 35.92% | 50.00% | -0.17% | 67.06% |
| BTC-USD | HISTORICAL_BTC_BULL | 23 | 65.22% | 9.93% | -11.54% | 23.14% | 65.22% | 25.46% | 53.73% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 13 | 46.15% | -5.27% | -11.49% | 19.23% | 53.85% | 1.53% | 29.68% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 30 | 33.33% | -13.63% | -22.47% | 21.78% | 70.00% | 7.11% | 57.36% |
| DOGE-USD | HISTORICAL_BTC_BULL | 6 | 50.00% | 12.63% | -6.01% | 31.53% | 66.67% | 33.05% | 78.26% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 4 | 0.00% | -21.59% | -24.05% | 16.43% | 50.00% | 7.36% | 22.20% |
| SOL-USD | HISTORICAL_BTC_BEAR | 12 | 50.00% | 0.18% | -8.84% | 10.00% | 66.67% | 2.52% | 19.92% |
| SOL-USD | HISTORICAL_BTC_BULL | 9 | 33.33% | -6.67% | -13.82% | 19.76% | 55.56% | 5.32% | 36.59% |
| SOL-USD | HISTORICAL_BTC_MIXED | 1 | 0.00% | -16.48% | -17.11% | 2.98% | 0.00% | -21.33% | 2.98% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 18 | 66.67% | 4.77% | -7.43% | 24.14% | 55.56% | 6.05% | 45.24% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 18 | 88.89% | 21.58% | -10.00% | 26.20% | 77.78% | 29.98% | 74.78% |
| BTC-USD | HISTORICAL_ASSET_BULL | 10 | 40.00% | -11.28% | -20.62% | 22.15% | 40.00% | -4.58% | 27.06% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 0.00% | -1.69% | -9.92% | 0.00% | 100.00% | 1.35% | 4.73% |
| BTC-USD | HISTORICAL_ASSET_MIXED | 1 | 0.00% | -40.58% | -42.28% | 0.00% | 0.00% | -45.29% | 0.00% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 10 | 40.00% | -5.91% | -10.83% | 18.12% | 50.00% | 0.06% | 27.05% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 32 | 31.25% | -13.63% | -22.47% | 21.66% | 71.88% | 8.67% | 56.31% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 4 | 50.00% | 10.33% | -9.05% | 34.69% | 75.00% | 29.15% | 74.17% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 100.00% | 38.17% | -2.98% | 38.17% | 100.00% | 47.83% | 82.05% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 3 | 0.00% | -13.13% | -15.94% | 17.58% | 0.00% | -14.97% | 17.58% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 23 | 65.22% | 1.17% | -7.77% | 20.23% | 60.87% | 3.69% | 34.77% |
| SOL-USD | HISTORICAL_ASSET_BULL | 4 | 0.00% | -10.50% | -16.47% | 12.23% | 50.00% | 2.50% | 24.30% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 0.00% | -1.69% | -9.92% | 0.00% | 100.00% | 1.35% | 4.73% |
| SOL-USD | HISTORICAL_ASSET_MIXED | 1 | 100.00% | 12.15% | -0.77% | 25.06% | 100.00% | 36.30% | 41.07% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 11 | 45.45% | -6.67% | -9.34% | 16.45% | 45.45% | -6.89% | 40.64% |

## Top regime-adjusted matches

The table below shows the top matches separately for each target, so BTC does not hide SOL and DOGE.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | XRP-USD | 2019-10-04 | 90.29% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 29.37% | 0.00% | 33.33% | -1.77% | -2.34% | 58.05% |
| BTC-USD | ETH-USD | 2025-12-11 | 85.41% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 5.52% | -7.64% | 12.79% | -1.70% | -7.64% | 12.79% |
| BTC-USD | MKR-USD | 2020-01-23 | 84.96% | BEAR | BEAR | SAME_BTC_AND_ASSET | HIGH_SPIKE_60D | 29.42% | -10.98% | 43.69% | 27.94% | -10.98% | 94.10% |
| BTC-USD | BNB-USD | 2025-12-16 | 85.29% | BEAR | DISTRIBUTION | SAME_BTC_ONLY | MIXED | -1.69% | -9.92% | 0.00% | 1.35% | -9.92% | 4.73% |
| BTC-USD | LRC-USD | 2018-09-29 | 91.57% | RECOVERY | BEAR | SAME_ASSET_ONLY | HIGH_SPIKE_60D | 21.04% | -13.46% | 133.38% | 29.74% | -13.46% | 133.38% |
| BTC-USD | FIL-USD | 2023-06-29 | 88.82% | BULL | BEAR | SAME_ASSET_ONLY | BULLISH_30D | 23.33% | -4.87% | 23.33% | 43.44% | -4.87% | 56.53% |
| BTC-USD | SAND-USD | 2023-06-24 | 88.52% | BULL | BEAR | SAME_ASSET_ONLY | MIXED | 7.39% | -12.66% | 11.30% | 26.71% | -12.66% | 37.05% |
| BTC-USD | APT-USD | 2024-05-27 | 87.04% | BULL | BEAR | SAME_ASSET_ONLY | MIXED | -1.32% | -3.95% | 7.11% | -53.95% | -53.95% | 7.11% |
| BTC-USD | OMG-USD | 2018-09-29 | 86.36% | RECOVERY | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -31.70% | -31.70% | 0.00% | -21.19% | -35.29% | 0.00% |
| BTC-USD | ETC-USD | 2023-06-25 | 85.86% | BULL | BEAR | SAME_ASSET_ONLY | MIXED | 9.93% | -8.65% | 9.93% | 17.30% | -8.65% | 28.49% |
| DOGE-USD | DASH-USD | 2022-03-02 | 90.18% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -17.14% | -27.85% | 0.00% | -2.98% | -30.72% | 0.00% |
| DOGE-USD | INJ-USD | 2022-03-04 | 88.94% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -32.36% | -35.14% | 0.00% | 0.31% | -36.02% | 0.31% |
| DOGE-USD | VET-USD | 2022-03-04 | 88.55% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -20.06% | -21.27% | 0.00% | 18.68% | -22.08% | 18.68% |
| DOGE-USD | QTUM-USD | 2022-03-02 | 88.53% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -22.26% | -33.72% | 0.00% | 6.79% | -33.72% | 19.77% |
| DOGE-USD | 1INCH-USD | 2022-03-04 | 88.44% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -14.71% | -20.68% | 8.97% | 26.51% | -20.68% | 26.51% |
| DOGE-USD | ENJ-USD | 2022-03-07 | 88.42% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 10.19% | -8.90% | 29.08% | 54.45% | -8.90% | 55.79% |
| DOGE-USD | THETA-USD | 2022-03-06 | 88.35% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -0.29% | -5.56% | 27.80% | 40.52% | -5.56% | 44.44% |
| DOGE-USD | OMG-USD | 2022-03-02 | 88.26% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -28.92% | -36.72% | 0.00% | -11.78% | -39.47% | 0.00% |
| DOGE-USD | XRP-USD | 2019-09-29 | 87.96% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 25.26% | -7.50% | 25.26% | 10.19% | -7.50% | 51.15% |
| DOGE-USD | CHZ-USD | 2022-03-06 | 87.91% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 8.62% | -7.36% | 16.30% | 74.78% | -7.36% | 74.78% |
| SOL-USD | RUNE-USD | 2025-12-17 | 79.60% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 18.50% | -7.03% | 20.04% | 9.91% | -7.03% | 54.43% |
| SOL-USD | SOL-USD | 2025-12-14 | 78.63% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -4.93% | -13.64% | 0.31% | -7.78% | -13.64% | 6.48% |
| SOL-USD | NEAR-USD | 2025-12-11 | 78.26% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 0.92% | -11.77% | 8.98% | 21.58% | -11.77% | 23.26% |
| SOL-USD | LINK-USD | 2025-12-11 | 77.42% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -0.47% | -7.77% | 5.62% | 3.69% | -7.77% | 17.55% |
| SOL-USD | KAVA-USD | 2025-12-16 | 77.01% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 12.67% | -7.55% | 12.67% | 9.02% | -7.55% | 24.66% |
| SOL-USD | BTC-USD | 2025-12-15 | 76.87% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 10.99% | -6.47% | 10.99% | 8.73% | -6.47% | 16.48% |
| SOL-USD | AVAX-USD | 2025-12-12 | 76.85% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 0.82% | -6.61% | 5.84% | 0.86% | -6.61% | 11.16% |
| SOL-USD | APT-USD | 2024-09-11 | 76.69% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -23.26% | -23.26% | 3.72% | -33.02% | -33.49% | 3.72% |
| SOL-USD | OMG-USD | 2025-12-16 | 76.25% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 8.84% | -4.58% | 9.67% | 7.75% | -4.58% | 18.81% |
| SOL-USD | DOT-USD | 2025-12-11 | 75.90% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -17.31% | -22.31% | 0.00% | -18.37% | -22.31% | 0.00% |

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

Generato: 2026-07-21 05:14 UTC


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
| BTC | 65.472 $ | +3 | ANTICIPATO / COSTRUTTIVO MA NON CONFERMATO | STAGE 4 / MARKDOWN | MASSIMI E MINIMI CRESCENTI | ACCUMULO POSSIBILE / RANGE BASSO | BASSO | HOLD / ASPETTA ROTTURA RESISTENZA |
| SOL | 78,18 $ | -3 | DEBOLE / NON CONFERMATO | STAGE 4 / MARKDOWN | MASSIMI E MINIMI DECRESCENTI | RANGE / FASE NON CHIARA | BASSO | NON INSEGUIRE / TAKE PROFIT SU SPIKE |
| DOGE | 0.07277 $ | -5 | RIBASSISTA / FRAGILE | STAGE 4 / MARKDOWN | COMPRESSIONE / TRIANGOLO POSSIBILE | MARKDOWN / DEBOLEZZA | BASSO | NO LONG / SHORT SOLO DOPO SPIKE E REJECTION |

## Punteggi per area

| Asset | Trend | Struttura | Momentum | Volume | Prezzo | Candela | Wyckoff | Totale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | -4 | +2 | +3 | +2 | 0 | 0 | 0 | +3 |
| SOL | -4 | -2 | +2 | +1 | 0 | 0 | 0 | -3 |
| DOGE | -4 | 0 | 0 | 0 | 0 | +1 | -2 | -5 |

## Livelli tecnici

| Asset | Supporto | Resistenza | Breakout 60g | Breakdown 60g | ATR14 | Rendimento 30g | Rendimento 90g |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 64.972 $ | 65.508 $ | 78.539 $ | 57.748 $ | 2,27% | 1,93% | -14,24% |
| SOL | 77,45 $ | 78,88 $ | 87,79 $ | 60,41 $ | 2,94% | 6,88% | -9,09% |
| DOGE | 0.07206 $ | 0.07546 $ | 0.11262 $ | 0.06961 $ | 2,76% | -12,89% | -23,47% |

## Lettura dettagliata

### BTC

- Prezzo: **65.472 $**
- Score classico: **+3 / 12**
- Verdetto: **ANTICIPATO / COSTRUTTIVO MA NON CONFERMATO**
- Azione coerente: **HOLD / ASPETTA ROTTURA RESISTENZA**
- Volatilità tecnica locale: **BASSO** — ATR14 2,27%; distanza supporto 0,78%; distanza resistenza 0,05%

Dettaglio:

- Trend: **-4** — prezzo sotto MA200 daily; breve termine sopra MA20/MA50; MA50 daily in discesa; MA200 daily in discesa; STAGE 4 / MARKDOWN
- Stage weekly: **STAGE 4 / MARKDOWN** — Prezzo sotto MA30 weekly con MA30 in discesa.
- Struttura: **+2** — MASSIMI E MINIMI CRESCENTI
- Momentum: **+3** — RSI sano 57.8; MACD sopra signal; istogramma MACD in miglioramento
- Volume: **+2** — OBV sopra media; CMF positivo 0.18; volume ratio 1.18
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **0** — ACCUMULO POSSIBILE / RANGE BASSO. Prezzo nella metà bassa del range, ma senza spring confermato.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 57.82 |
| MACD histogram | 347.51769 |
| CMF20 | 0.175 |
| Volume ratio 20 | 1.18 |
| MA20 | 63.483 $ |
| MA50 | 63.194 $ |
| MA100 | 70.213 $ |
| MA200 | 72.928 $ |
| Pendenza MA50 20g | -7,75% |
| Pendenza MA200 60g | -9,90% |
| Bollinger width | 7,96% |
| Bollinger position | 0.88 |

### SOL

- Prezzo: **78,18 $**
- Score classico: **-3 / 12**
- Verdetto: **DEBOLE / NON CONFERMATO**
- Azione coerente: **NON INSEGUIRE / TAKE PROFIT SU SPIKE**
- Volatilità tecnica locale: **BASSO** — ATR14 2,94%; distanza supporto 0,99%; distanza resistenza 0,85%

Dettaglio:

- Trend: **-4** — prezzo sotto MA200 daily; breve termine sopra MA20/MA50; MA50 daily in discesa; MA200 daily in discesa; STAGE 4 / MARKDOWN
- Stage weekly: **STAGE 4 / MARKDOWN** — Prezzo sotto MA30 weekly con MA30 in discesa.
- Struttura: **-2** — MASSIMI E MINIMI DECRESCENTI
- Momentum: **+2** — RSI sano 55.3; RSI in miglioramento; MACD sotto signal; istogramma MACD in miglioramento
- Volume: **+1** — OBV sopra media; CMF neutrale 0.05; volume ratio 0.96
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **0** — RANGE / FASE NON CHIARA. Nessuna fase Wyckoff pulita.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 55.29 |
| MACD histogram | -0.26425 |
| CMF20 | 0.048 |
| Volume ratio 20 | 0.96 |
| MA20 | 78,19 $ |
| MA50 | 73,26 $ |
| MA100 | 79,81 $ |
| MA200 | 89,84 $ |
| Pendenza MA50 20g | -3,99% |
| Pendenza MA200 60g | -17,02% |
| Bollinger width | 12,37% |
| Bollinger position | 0.50 |

### DOGE

- Prezzo: **0.07277 $**
- Score classico: **-5 / 12**
- Verdetto: **RIBASSISTA / FRAGILE**
- Azione coerente: **NO LONG / SHORT SOLO DOPO SPIKE E REJECTION**
- Volatilità tecnica locale: **BASSO** — ATR14 2,76%; distanza supporto 1,06%; distanza resistenza 3,63%

Dettaglio:

- Trend: **-4** — prezzo sotto MA200 daily; medie daily allineate ribassiste; MA50 daily in discesa; MA200 daily in discesa; STAGE 4 / MARKDOWN
- Stage weekly: **STAGE 4 / MARKDOWN** — Prezzo sotto MA30 weekly con MA30 in discesa.
- Struttura: **0** — COMPRESSIONE / TRIANGOLO POSSIBILE
- Momentum: **0** — RSI neutrale 39.9; MACD sopra signal; istogramma MACD in peggioramento
- Volume: **0** — OBV sotto media; CMF positivo 0.05; volume ratio 1.24
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **+1** — Bullish engulfing
- Wyckoff: **-2** — MARKDOWN / DEBOLEZZA. Prezzo basso nel range e sotto medie principali.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 39.89 |
| MACD histogram | 0.00043 |
| CMF20 | 0.053 |
| Volume ratio 20 | 1.24 |
| MA20 | 0.07389 $ |
| MA50 | 0.07954 $ |
| MA100 | 0.09134 $ |
| MA200 | 0.09900 $ |
| Pendenza MA50 20g | -13,47% |
| Pendenza MA200 60g | -15,87% |
| Bollinger width | 10,66% |
| Bollinger position | 0.36 |

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

Generato: 2026-07-21 05:14 UTC


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
| BTC | 65.472 $ | Doppio massimo | CANDIDATO | ribassista | n/a | 49.952 $ | n/a | 13,38% | Fib 23,6% TENUTO (0) @ 63.676 $ | NEL RANGE | 65.092 $ |
| SOL | 78,18 $ | Doppio minimo | MATURO | rialzista | 2026-07-01 | 91,46 $ | 14,44% | n/a | Fib 23,6% TENUTO (+1) @ 74,52 $ | NEL RANGE | 76,82 $ |
| DOGE | 0.07277 $ | Triplo massimo | MATURO | ribassista | 2026-06-24 | 0.05847 $ | 27,13% | n/a | Fib 23,6% NON ATTIVO (0) @ 0.08213 $ | NEL RANGE | 0.07107 $ |

## BTC

![Classic visual BTC](classic_visual_BTC.png)

- Pattern principale: **Doppio massimo**
- Stato pattern: **CANDIDATO** (0)
- Famiglia: **ribassista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-06-22 -> 2026-07-15**
- Età formazione: **6 giorni**
- Breakout pattern: **n/a**
- Età breakout: **n/a**
- Neckline: **57.748 $**
- Target teorico: **49.952 $**
- Progresso verso target: **n/a**
- Distanza dalla neckline: **13,38%**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 23,6% TENUTO (0) @ 63.676 $** — Swing UP 2026-07-01 57.748 -> 2026-07-15 65.508; livello più vicino 23.6% a 63.676; stato TENUTO; confluenza: nessuna confluenza indipendente.
- Invalidazione: **58.903 $**
- Relazione prezzo/neckline: **sopra neckline**
- Dettaglio: Due massimi simili vicino a 65.544 tra 2026-06-22 e 2026-07-15. Neckline ribassista stimata: 57.748. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 6 giorni. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **NEL RANGE**
- Supporto: **65.092 $**
- Resistenza: **65.508 $**
- Breakout 60g: **78.539 $**
- Breakdown 60g: **57.748 $**
- RSI14: **57.79**
- ATR14: **2,27%**
- Volume ratio 20g: **1.18**
- Rendimento 30g: **+1,92%**
- Rendimento 90g: **-14,25%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Doppio massimo | CANDIDATO | 0 | ribassista | 57.748 $ | n/a | n/a | 49.952 $ | n/a | 13,38% | 58.903 $ | Due massimi simili a 65.544 $ e 65.508 $. Neckline circa 57.748 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 6 giorni. |
| Triangolo discendente possibile | CANDIDATO | 0 | ribassista | n/a | n/a | n/a | n/a | n/a | n/a | n/a | Massimi decrescenti e supporto quasi piatto. Stato: CANDIDATO; il pattern non ha una neckline univoca da usare per il lifecycle. |
| Doppio minimo | CANDIDATO | 0 | rialzista | 67.248 $ | n/a | n/a | 76.748 $ | n/a | 2,71% | 65.903 $ | Due minimi simili a 59.109 $ e 57.748 $. Neckline circa 67.248 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 20 giorni. |

## SOL

![Classic visual SOL](classic_visual_SOL.png)

- Pattern principale: **Doppio minimo**
- Stato pattern: **MATURO** (+1)
- Famiglia: **rialzista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-06-06 -> 2026-06-25**
- Età formazione: **26 giorni**
- Breakout pattern: **2026-07-01**
- Età breakout: **20 giorni**
- Neckline: **75,94 $**
- Target teorico: **91,46 $**
- Progresso verso target: **14,44%**
- Distanza dalla neckline: **n/a**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 23,6% TENUTO (+1) @ 74,52 $** — Swing UP 2026-06-06 60,41 -> 2026-07-15 78,88; livello più vicino 23.6% a 74,52; stato TENUTO; confluenza: neckline rialzista, invalidazione rialzista.
- Invalidazione: **74,42 $**
- Relazione prezzo/neckline: **sopra neckline**
- Dettaglio: Due minimi simili vicino a 60,41 tra 2026-06-06 e 2026-06-25. Neckline stimata: 75,94. Breakout neckline: 2026-07-01 (20 giorni fa). Stato: MATURO. Target teorico: 91,46; progresso corrente: 14,44%. Relazione prezzo/neckline: sopra neckline. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **NEL RANGE**
- Supporto: **76,82 $**
- Resistenza: **78,88 $**
- Breakout 60g: **87,79 $**
- Breakdown 60g: **60,41 $**
- RSI14: **55.22**
- ATR14: **2,94%**
- Volume ratio 20g: **0.95**
- Rendimento 30g: **+6,84%**
- Rendimento 90g: **-9,12%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Doppio minimo | MATURO | +1 | rialzista | 75,94 $ | 2026-07-01 | 20g | 91,46 $ | 14,44% | n/a | 74,42 $ | Due minimi simili vicino a 60,41 tra 2026-06-06 e 2026-06-25. Neckline stimata: 75,94. Breakout neckline: 2026-07-01 (20 giorni fa). Stato: MATURO. Target teorico: 91,46; progresso corrente: 14,44%. Relazione prezzo/neckline: sopra neckline. Fonte lifecycle: technical_structure_metrics.csv. |
| Doppio massimo | CANDIDATO | 0 | ribassista | 64,42 $ | n/a | n/a | 49,96 $ | n/a | 21,36% | 65,71 $ | Due massimi simili a 75,94 $ e 78,88 $. Neckline circa 64,42 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 6 giorni. |
| Doppio minimo | CANDIDATO | 0 | rialzista | 98,27 $ | n/a | n/a | 114,91 $ | n/a | 25,69% | 96,30 $ | Due minimi simili a 81,63 $ e 81,69 $. Neckline circa 98,27 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 59 giorni. |
| Testa e spalle | TARGET RAGGIUNTO | 0 | ribassista | 82,57 $ | 2026-05-28 | 54g | 66,88 $ | 27,99% | n/a | 84,22 $ | Spalla sinistra 88,05 $, testa 98,27 $, spalla destra 87,79 $. Neckline circa 82,57 $. Breakout neckline: 2026-05-28 (54 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 66,88 $; progresso: 27,99%; prezzo sotto neckline. |

## DOGE

![Classic visual DOGE](classic_visual_DOGE.png)

- Pattern principale: **Triplo massimo**
- Stato pattern: **MATURO** (-1)
- Famiglia: **ribassista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-03-25 -> 2026-06-12**
- Età formazione: **39 giorni**
- Breakout pattern: **2026-06-24**
- Età breakout: **27 giorni**
- Neckline: **0.07809 $**
- Target teorico: **0.05847 $**
- Progresso verso target: **27,13%**
- Distanza dalla neckline: **n/a**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 23,6% NON ATTIVO (0) @ 0.08213 $** — Swing DOWN 2026-05-14 0.11825 -> 2026-07-13 0.07097; livello più vicino 23.6% a 0.08213; stato NON ATTIVO; confluenza: nessuna confluenza indipendente.
- Invalidazione: **0.07966 $**
- Relazione prezzo/neckline: **sotto neckline**
- Dettaglio: Tre massimi simili vicino a 0.09772 dal 2026-03-25 al 2026-06-12. Neckline ribassista stimata: 0.07809. Breakout neckline: 2026-06-24 (27 giorni fa). Stato: MATURO. Target teorico: 0.05847; progresso corrente: 27,13%. Relazione prezzo/neckline: sotto neckline. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Bullish engulfing**
- Stato prezzo: **NEL RANGE**
- Supporto: **0.07107 $**
- Resistenza: **0.07923 $**
- Breakout 60g: **0.11262 $**
- Breakdown 60g: **0.06961 $**
- RSI14: **39.68**
- ATR14: **2,76%**
- Volume ratio 20g: **1.24**
- Rendimento 30g: **-12,95%**
- Rendimento 90g: **-23,52%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Triplo massimo | MATURO | -1 | ribassista | 0.07809 $ | 2026-06-24 | 27g | 0.05847 $ | 27,13% | n/a | 0.07966 $ | Tre massimi simili vicino a 0.09772 dal 2026-03-25 al 2026-06-12. Neckline ribassista stimata: 0.07809. Breakout neckline: 2026-06-24 (27 giorni fa). Stato: MATURO. Target teorico: 0.05847; progresso corrente: 27,13%. Relazione prezzo/neckline: sotto neckline. Fonte lifecycle: technical_structure_metrics.csv. |
| Doppio massimo | MATURO | -1 | ribassista | 0.07809 $ | 2026-06-24 | 27g | 0.06035 $ | 30,01% | n/a | 0.07966 $ | Due massimi simili a 0.09584 $ e 0.09169 $. Neckline circa 0.07809 $. Breakout neckline: 2026-06-24 (27 giorni fa). Stato: MATURO. Target teorico: 0.06035 $; progresso: 30,01%; prezzo sotto neckline. |
| Doppio minimo | CANDIDATO | 0 | rialzista | 0.07923 $ | n/a | n/a | 0.08886 $ | n/a | 8,88% | 0.07765 $ | Due minimi simili a 0.06961 $ e 0.07097 $. Neckline circa 0.07923 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 8 giorni. |
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

Generato: 2026-07-21 05:14 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [fractal_path_tracker.md](fractal_path_tracker.md)

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-07-21**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-01-05**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **78,18 $**
- Verdetto principale: **ANALOGIA DEBOLE / SCENARIO SECONDARIO**
- Somiglianza strutturale: **+64,43%**
- Aderenza live principale: **+63,32%**
- Errore medio live principale: **18,34%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE SOLO DI CONTESTO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **45**
- Osservazioni inclusive dal bottom: **46**
- Osservazioni da inizio programma/scanner: **19**
- Errore assoluto medio dal bottom: **11,11%**
- Errore assoluto medio da inizio programma: **18,34%**
- Gap firmato medio ultimi 7 giorni: **+16,00%**
- Errore assoluto medio ultimi 7 giorni: **16,00%**
- Gap ultimo giorno: **+17,88%**
- Stato aderenza: **STACCATO / MOLTO IN ANTICIPO**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **+17,88%**
- Gap firmato medio 7g: **+16,00%**
- Errore assoluto medio 7g: **16,00%**
- Variazione recente gap: **+3,09%**
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
| 36 | 2026-07-12 | 2022-12-27 | 76,87 $ | 65,85 $ | +16,74% | da inizio programma |
| 37 | 2026-07-13 | 2022-12-28 | 74,86 $ | 65,20 $ | +14,81% | da inizio programma |
| 38 | 2026-07-14 | 2022-12-29 | 77,76 $ | 65,56 $ | +18,62% | da inizio programma |
| 39 | 2026-07-15 | 2022-12-30 | 77,26 $ | 65,40 $ | +18,14% | da inizio programma |
| 40 | 2026-07-16 | 2022-12-31 | 75,27 $ | 65,18 $ | +15,48% | da inizio programma |
| 41 | 2026-07-17 | 2023-01-01 | 75,01 $ | 65,49 $ | +14,54% | da inizio programma |
| 42 | 2026-07-18 | 2023-01-02 | 75,46 $ | 65,74 $ | +14,79% | da inizio programma |
| 43 | 2026-07-19 | 2023-01-03 | 76,36 $ | 65,71 $ | +16,21% | da inizio programma |
| 44 | 2026-07-20 | 2023-01-04 | 76,36 $ | 66,43 $ | +14,94% | da inizio programma |
| 45 | 2026-07-21 | 2023-01-05 | 78,18 $ | 66,32 $ | +17,88% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-07-28 | 74,33 $ | 87,62 $ | 78,18 $ / 87,62 $ | no | n/a | n/a | n/a |
| 14g | 2026-08-04 | 83,07 $ | 97,91 $ | 78,18 $ / 98,30 $ | no | n/a | n/a | n/a |
| 21g | 2026-08-11 | 90,73 $ | 106,95 $ | 78,18 $ / 107,35 $ | no | n/a | n/a | n/a |
| 28g | 2026-08-18 | 92,46 $ | 108,99 $ | 78,18 $ / 110,40 $ | no | n/a | n/a | n/a |
| 35g | 2026-08-25 | 85,95 $ | 101,31 $ | 78,18 $ / 110,40 $ | no | n/a | n/a | n/a |
| 42g | 2026-09-01 | 93,06 $ | 109,69 $ | 78,18 $ / 112,87 $ | no | n/a | n/a | n/a |
| 49g | 2026-09-08 | 94,33 $ | 111,20 $ | 78,18 $ / 115,29 $ | no | n/a | n/a | n/a |
| 56g | 2026-09-15 | 92,48 $ | 109,01 $ | 78,18 $ / 115,29 $ | no | n/a | n/a | n/a |
| 63g | 2026-09-22 | 80,21 $ | 94,55 $ | 78,18 $ / 115,29 $ | no | n/a | n/a | n/a |
| 70g | 2026-09-29 | 98,69 $ | 116,33 $ | 78,18 $ / 116,33 $ | no | n/a | n/a | n/a |
| 77g | 2026-10-06 | 111,61 $ | 131,57 $ | 78,18 $ / 131,57 $ | no | n/a | n/a | n/a |
| 84g | 2026-10-13 | 110,43 $ | 130,17 $ | 78,18 $ / 131,63 $ | no | n/a | n/a | n/a |
| 91g | 2026-10-20 | 110,47 $ | 130,22 $ | 78,18 $ / 132,24 $ | no | n/a | n/a | n/a |
| 98g | 2026-10-27 | 119,75 $ | 141,16 $ | 78,18 $ / 141,16 $ | no | n/a | n/a | n/a |
| 105g | 2026-11-03 | 111,27 $ | 131,16 $ | 78,18 $ / 141,56 $ | no | n/a | n/a | n/a |
| 112g | 2026-11-10 | 116,10 $ | 136,86 $ | 78,18 $ / 141,56 $ | no | n/a | n/a | n/a |
| 119g | 2026-11-17 | 113,64 $ | 133,95 $ | 78,18 $ / 141,56 $ | no | n/a | n/a | n/a |
| 126g | 2026-11-24 | 106,36 $ | 125,38 $ | 78,18 $ / 141,56 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 7 | 28,57% | 1,18% | 15,67% |
| 14g | 0 | n/a | n/a | n/a |
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

Ultima lettura salvata: **2026-07-21** — SOL 78,18 $, gap +17,88%, somiglianza +64,43%.

Nel report principale lascio solo il link, così non diventa troppo lungo.

<!-- SOL_BTC_FRACTAL_HISTORY_END -->

</details>
<!-- COMPACT_SECTION_END:fractal_path -->

<!-- COMPACT_SECTION_START:exchange_microstructure -->
<details>
<summary><strong>🏦 Dati exchange, liquidità e leva</strong></summary>

<!-- EXCHANGE_MICROSTRUCTURE_START -->
# Dati exchange, liquidità e leva

Generato: 2026-07-21 05:14 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [exchange_microstructure_report.md](exchange_microstructure_report.md)

Questo modulo legge Kraken Futures, Bitget Futures e KuCoin Futures come nucleo derivati. OKX e Coinbase vengono raccolti come fonti ausiliarie non pesate.
Non modifica la formula matematica di RSI, Fibonacci o Wyckoff: controlla se quei segnali sono sostenuti da acquisti, vendite, OI, funding e liquidità.

**Limite importante:** questo nucleo non assume disponibile un feed pubblico completo delle liquidazioni. La componente liquidazioni resta neutrale; le zone future restano stime di pressione, non dati certi delle singole posizioni.

Diagnostica completa: [exchange_source_diagnostics.md](exchange_source_diagnostics.md)

## Sintesi

| Asset | Prezzo | Exchange | Segnale candidato | Peso Global | Bias exchange | Confidenza | Copertura | Funding 8h eq. | OI 24h | Taker flow (campione/4h) | Book 0,5% | Liq long campione | Liq short campione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 65.482 $ | 3 | 0 | 0 | LEGGERMENTE POSITIVA / NON PESATA | ALTA | 100% | -0,0044% | +2,64% | 1,98 | +0,77% | 0 $ | 0 $ |
| SOL | 78,16 $ | 3 | +1 | 0 | POSITIVA / CANDIDATA, ANCORA NON PESATA | MEDIA | 100% | +0,0027% | +1,19% | 3,05 | +3,26% | 0 $ | 0 $ |
| DOGE | 0.07279 $ | 3 | 0 | 0 | LEGGERMENTE POSITIVA / NON PESATA | MEDIA | 100% | +0,0095% | -1,89% | 1,70 | -0,20% | 0 $ | 0 $ |

Il segnale candidato è limitato a **±1**, ma il peso nel Global resta **0** finché il tracker a 7 giorni non raggiunge 30 controlli, almeno 55% di accuratezza e return corretto direzione positivo. Un singolo muro o funding non basta.

La colonna taker usa un campione recente nel primo run. Dopo almeno 3 fotografie distribuite su almeno 45 minuti viene sostituita automaticamente dalla media intraday 4h.

## Dati separati per exchange

| Asset | Exchange | Stato | Funding 8h eq. | Open interest | Taker flow | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | Kraken | OK | -0,0008% | 124,44 mln $ | 0,97 | -7,23% |
| BTC | Bitget | OK | -0,0005% | 2,29 mld $ | 0,76 | +4,30% |
| BTC | Kucoin | OK | -0,0230% | 1,76 mld $ | 0,85 | +2,37% |
| SOL | Kraken | OK | +0,0064% | 18,31 mln $ | 0,86 | +9,69% |
| SOL | Bitget | OK | +0,0080% | 356,24 mln $ | 7,69 | -6,61% |
| SOL | Kucoin | OK | +0,0023% | 264,11 mln $ | 1,20 | -6,85% |
| DOGE | Kraken | OK | +0,0145% | 2,80 mln $ | 3,18 | -0,57% |
| DOGE | Bitget | OK | +0,0100% | 83,67 mln $ | 1,10 | -2,92% |
| DOGE | Kucoin | OK | +0,0100% | 119,90 mln $ | 3,75 | +35,26% |

Kraken, Bitget e KuCoin contribuiscono a funding normalizzato, open interest, trade aggressivi e order book. Non viene inventato un long/short ratio pubblico né un feed completo delle liquidazioni.

## Conferme per indicatori tecnici

### BTC

- Score grezzo exchange: **+3,50**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 0, accuratezza n/a.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 0, bear 1, divergenze 0.
- Flusso taker/order book: **+1,75**.
- OI/funding/basis: **+1,00**.
- Affollamento long/short: **+0,00**.
- Liquidazioni: **NON PESATE / FEED COMPLETO NON ASSUNTO DISPONIBILE**.
- **Wyckoff:** Markdown non pienamente confermato: compare assorbimento compratore.
- **Fibonacci:** Fibonacci tenuto con acquisti/assorbimento coerenti: conferma positiva.
- **RSI:** RSI in zona non estrema o flusso exchange non abbastanza netto.
- **Pattern:** I pattern candidati restano non operativi: i dati exchange possono solo preparare la conferma.
- **Breakout/breakdown:** Resistenza vicina con acquisti aggressivi: breakout più credibile, ma serve chiusura sopra il livello.
- **Mappa liquidità attuale:** muro bid: n/a; muro ask: n/a

![Microstruttura exchange BTC](exchange_microstructure_BTC.png)

### SOL

- Score grezzo exchange: **+2,50**; candidato: **+1**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 0, accuratezza n/a.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 1, bear 1, divergenze 0.
- Flusso taker/order book: **+1,75**.
- OI/funding/basis: **+0,00**.
- Affollamento long/short: **+0,00**.
- Liquidazioni: **NON PESATE / FEED COMPLETO NON ASSUNTO DISPONIBILE**.
- **Wyckoff:** Markdown non pienamente confermato: compare assorbimento compratore.
- **Fibonacci:** Fibonacci tenuto con acquisti/assorbimento coerenti: conferma positiva. Confluenza tecnica dichiarata: neckline rialzista, invalidazione rialzista.
- **RSI:** RSI in zona non estrema o flusso exchange non abbastanza netto.
- **Pattern:** Doppio minimo maturo sostenuto dal flusso exchange.
- **Breakout/breakdown:** Resistenza vicina con acquisti aggressivi: breakout più credibile, ma serve chiusura sopra il livello.
- **Mappa liquidità attuale:** muro bid: n/a; muro ask: n/a

![Microstruttura exchange SOL](exchange_microstructure_SOL.png)

### DOGE

- Score grezzo exchange: **+2,12**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 0, accuratezza n/a.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 1, bear 1, divergenze 0.
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
| BTC | +60,00% | +5,34% | 0 | n/a | RACCOLTA DATI | 0,00 | +60,00% | +5,34% |
| SOL | +52,50% | +0,70% | 0 | n/a | RACCOLTA DATI | 0,00 | +52,50% | +0,70% |
| DOGE | +32,50% | -12,28% | 0 | n/a | RACCOLTA DATI | 0,00 | +32,50% | -12,28% |

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

Generato: 2026-07-21 05:14 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [exchange_signal_tracker_report.md](exchange_signal_tracker_report.md)

Questo tracker verifica se il segnale candidato exchange ±1 anticipa correttamente la direzione del prezzo a 1/3/7/14/30 giorni.
Il peso Global resta 0 finché l'orizzonte 7g non ha almeno 30 controlli, accuratezza almeno 55% e return corretto direzione positivo. L'overlay a 30g ha un gate separato.

Controlli maturati completati in questa esecuzione: **9**.

## Ultime fotografie giornaliere

| Data | Asset | Prezzo | Versione | Calibrazione | Candidato | Peso Global | Score raw | Confidenza | Taker 4h | OI 24h | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-07-21 | BTC | 65.482,28 | V2.1.3 | OK | 0 | 0 | 3,50 | ALTA | 1,98 | +2,64% | +0,77% |
| 2026-07-21 | DOGE | 0.07279 | V2.1.3 | OK | 0 | 0 | 2,12 | MEDIA | 1,70 | -1,89% | -0,20% |
| 2026-07-21 | SOL | 78,16 | V2.1.3 | OK | 1 | 0 | 2,50 | MEDIA | 3,05 | +1,19% | +3,26% |
| 2026-07-20 | BTC | 64.448,63 | V2.1.3 | OK | 1 | 0 | 2,50 | MEDIA | 1,39 | +1,07% | +4,99% |
| 2026-07-20 | DOGE | 0.07216 | V2.1.3 | OK | 0 | 0 | -0,25 | BASSA | 0,86 | +4,68% | -1,67% |
| 2026-07-20 | SOL | 76,36 | V2.1.3 | OK | 0 | 0 | 0,75 | BASSA | 0,95 | +0,11% | -2,20% |
| 2026-07-19 | BTC | 64.720,62 | V2.1.3 | OK | 0 | 0 | -0,50 | BASSA | 0,79 | -6,65% | -0,41% |
| 2026-07-19 | DOGE | 0.07239 | V2.1.3 | OK | 0 | 0 | 2,38 | MEDIA | 4,21 | +2,17% | -2,34% |
| 2026-07-19 | SOL | 75,98 | V2.1.3 | OK | 0 | 0 | -0,25 | BASSA | 0,74 | -4,40% | +0,28% |

## Accuratezza direzionale

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 1 | +100,00% | +1,59% | +1,07% | +1,84% | FEEDBACK RAPIDO |
| BTC | 3g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 7g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 14g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 30g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 1g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 3g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 7g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 14g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 30g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 1g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 3g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
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

**DOGE** — DOGE: i futures sembrano più vulnerabili verso una discesa improvvisa. Non significa che deve scendere, ma se rompe sotto può accelerare. Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale.

| Asset | Prezzo | Funding | OI 24h | Long/Short | Lettura futures | Forza |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 65.472 $ | +0.0015% | -0.54% | 1.40 | Misto | 1/5 |
| SOL | 78,18 $ | +0.0069% | -16.15% | 2.18 | Misto | 1/5 |
| DOGE | 0.07277 $ | +0.0100% | -5.58% | 4.48 | Rischio sotto | 2/5 |

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

Generato: 2026-07-21 05:14 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [rsi_multitimeframe_divergence_report.md](rsi_multitimeframe_divergence_report.md)

Il modulo confronta prezzo e RSI 14 sui pivot confermati **daily e weekly**. Riconosce divergenze regolari e nascoste, segnali in formazione, invalidazioni e semplice conferma del momentum.

**Peso operativo: 0.** Non modifica il Global Confluence, non cambia le soglie del Paper Trading e non apre né blocca operazioni. I risultati vengono misurati prima di qualsiasi futura decisione sul peso.

## Sintesi corrente

| Asset   | Daily            | Stato D       | Weekly              | Stato W    | Lettura weekly                                                                                                                |   Peso |
|:--------|:-----------------|:--------------|:--------------------|:-----------|:------------------------------------------------------------------------------------------------------------------------------|-------:|
| BTC     | Bullish regolare | CONFERMATA    | Bullish regolare    | CONFERMATA | Bullish regolare confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto. |      0 |
| SOL     | Hidden bearish   | IN_FORMAZIONE | Hidden bearish      | CONFERMATA | Hidden bearish confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto.   |      0 |
| DOGE    | Hidden bearish   | CONFERMATA    | Conferma ribassista | CONTESTO   | Prezzo e RSI stanno scendendo insieme: momentum ribassista confermato, nessuna bullish divergence attiva.                     |      0 |

## Dettaglio dei pivot

| Asset   | TF   | Tipo                | Stato         | Prezzo / RSI      | Pivot confrontati                                                   | Δ prezzo contesto   | Δ RSI contesto   |   Peso |
|:--------|:-----|:--------------------|:--------------|:------------------|:--------------------------------------------------------------------|:--------------------|:-----------------|-------:|
| BTC     | 1D   | Bullish regolare    | CONFERMATA    | 65.480 $ / 57,82  | 2026-06-25 58.076 $ / RSI 30,46 → 2026-07-01 57.748 $ / RSI 37,26   | n/a                 | n/a              |      0 |
| BTC     | 1W   | Bullish regolare    | CONFERMATA    | 65.480 $ / 40,85  | 2026-06-07 59.109 $ / RSI 34,23 → 2026-07-05 57.748 $ / RSI 38,20   | n/a                 | n/a              |      0 |
| SOL     | 1D   | Hidden bearish      | IN_FORMAZIONE | 78,23 $ / 55,34   | 2026-07-15 78,88 $ / RSI 52,25 → 2026-07-21 78,36 $ / RSI 55,34     | n/a                 | n/a              |      0 |
| SOL     | 1W   | Hidden bearish      | CONFERMATA    | 78,23 $ / 41,27   | 2026-05-17 98,27 $ / RSI 38,29 → 2026-07-05 83,81 $ / RSI 42,25     | n/a                 | n/a              |      0 |
| DOGE    | 1D   | Hidden bearish      | CONFERMATA    | 0.07282 $ / 39,89 | 2026-06-12 0.09169 $ / RSI 35,18 → 2026-07-04 0.07923 $ / RSI 41,65 | n/a                 | n/a              |      0 |
| DOGE    | 1W   | Conferma ribassista | CONTESTO      | 0.07282 $ / 33,65 | n/a                                                                 | -17,96%             | -3,74            |      0 |

### BTC

- **1D — Bullish regolare / CONFERMATA**: Bullish regolare confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto.
- **1W — Bullish regolare / CONFERMATA**: Bullish regolare confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto.

### SOL

- **1D — Hidden bearish / IN_FORMAZIONE**: Hidden bearish in formazione: il secondo estremo non è ancora un pivot confermato. Peso operativo sempre 0.
- **1W — Hidden bearish / CONFERMATA**: Hidden bearish confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto.

### DOGE

- **1D — Hidden bearish / CONFERMATA**: Hidden bearish confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto.
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

Generato: 2026-07-21 05:14 UTC


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

| Asset   | Prezzo   |   Punteggio | Verdetto           | Trend            | Momentum                  | Struttura                                             |   Pattern score | Fibonacci      | Pattern rialzista         | Pattern ribassista         | Supporto   | Resistenza   |
|:--------|:---------|------------:|:-------------------|:-----------------|:--------------------------|:------------------------------------------------------|----------------:|:---------------|:--------------------------|:---------------------------|:-----------|:-------------|
| BTC | 65.472 $ | 0 | NEUTRALE / MISTO | Trend misto | Momentum in miglioramento | Struttura ribassista con massimi e minimi decrescenti | 0 | 0 / TENUTO | Doppio minimo / CANDIDATO | Doppio massimo / CANDIDATO | 57.748 | 65.508 |
| SOL | 78,18 $ | -2 | NEUTRALE / MISTO | Trend ribassista | Momentum in miglioramento | Struttura ribassista con massimi e minimi decrescenti | +1 | +1 / TENUTO | Doppio minimo / MATURO | Doppio massimo / CANDIDATO | 64,42 | 78,88 |
| DOGE | 0.07277 $ | -8 | RIBASSISTA TECNICO | Trend ribassista | Momentum debole | Struttura ribassista con massimi e minimi decrescenti | -1 | 0 / NON ATTIVO | Doppio minimo / CANDIDATO | Triplo massimo / MATURO | 0.07097 | 0.07923 |

## Riepilogo ciclo di vita pattern

| Asset   | Doppio minimo   | Triplo minimo   | Adam/Eve Bottom                 | Doppio massimo   | Triplo massimo   | Adam/Eve Top                 |   Punteggio pattern |
|:--------|:----------------|:----------------|:--------------------------------|:-----------------|:-----------------|:-----------------------------|--------------------:|
| BTC | CANDIDATO | CANDIDATO | Adam and Eve Bottom — CANDIDATO | CANDIDATO | CANDIDATO | Adam and Eve Top — CANDIDATO | 0 |
| SOL | MATURO | CANDIDATO | Adam and Eve Bottom — MATURO | CANDIDATO | CANDIDATO | Adam and Eve Top — CANDIDATO | 1 |
| DOGE | CANDIDATO | ASSENTE | Adam and Eve Bottom — CANDIDATO | ASSENTE | MATURO | Eve and Adam Top — MATURO | -1 |

## Indicatori tecnici

| Asset   |   RSI 14 |   Istogramma MACD | MA20    | MA50    | MA200   | Pendenza MA50 20g   | Pendenza MA200 60g   | Rendimento 30g   | Rendimento 90g   |
|:--------|---------:|------------------:|:--------|:--------|:--------|:--------------------|:---------------------|:-----------------|:-----------------|
| BTC | 57.79 | 347.127 | 63.483 | 63.194 | 72.928 | -7,19% | -9,73% | 3,53% | -16,28% |
| SOL | 55.22 | -0.26616 | 78,19 | 73,26 | 89,84 | -3,57% | -16,70% | 7,96% | -10,05% |
| DOGE | 39.68 | 0.00043 | 0.07389 | 0.07954 | 0.09900 | -12,75% | -15,64% | -11,44% | -23,99% |

## Dettaglio asset

### BTC

- Prezzo: **65.472 $**
- Punteggio tecnico: **0 / 12**
- Verdetto: **NEUTRALE / MISTO**
- Trend: **Trend misto** (-1)
- Momentum: **Momentum in miglioramento** (2)
- Volume: **Volume da accumulazione** (2)
- Struttura: **Struttura ribassista con massimi e minimi decrescenti** (-2)
  - Dettaglio struttura: Ultimi minimi: 5.808e+04 -> 5.775e+04. Ultimi massimi: 6.554e+04 -> 6.551e+04.
- Divergenza: **Divergenza rialzista RSI, Divergenza ribassista nascosta RSI** (1)
- Fase Wyckoff candidata: **Markdown / fase ribassista** (-2)
  - Dettaglio Wyckoff: Prezzo sotto MA200 con trend a 90 giorni ancora debole.
- Fibonacci automatico: **TENUTO** (0)
  - Swing UP 2026-07-01 57.748 -> 2026-07-15 65.508; livello più vicino 23.6% a 63.676; stato TENUTO; confluenza: nessuna confluenza indipendente.
- Punteggio pattern: **0**
  - rialzista dominante: Doppio minimo (CANDIDATO, 0); ribassista dominante: Doppio massimo (CANDIDATO, 0).
- Supporto più vicino: **57.748**
- Resistenza più vicina: **65.508**

Pattern classici e ciclo di vita:

- Doppio minimo: **CANDIDATO** (0)
  - Due minimi simili vicino a 57.748 tra 2026-06-05 e 2026-07-01. Neckline stimata: 67.248. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 20 giorni.
  - neckline 67.248; target 76.748; distanza dalla neckline 2,71%; prezzo sotto neckline.
- Triplo minimo: **CANDIDATO** (0)
  - Tre minimi simili vicino a 57.748 dal 2026-06-05 al 2026-07-01. Neckline stimata: 67.248. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 20 giorni.
  - neckline 67.248; target 76.748; distanza dalla neckline 2,71%; prezzo sotto neckline.
- Adam and Eve Bottom: **CANDIDATO** (0)
  - Pattern Adam and Eve Bottom vicino a 57.748 dal 2026-06-05 al 2026-07-01. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 67.248. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 20 giorni.
  - neckline 67.248; target 76.748; distanza dalla neckline 2,71%; prezzo sotto neckline.
- Doppio massimo: **CANDIDATO** (0)
  - Due massimi simili vicino a 65.544 tra 2026-06-22 e 2026-07-15. Neckline ribassista stimata: 57.748. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 6 giorni.
  - neckline 57.748; target 49.952; distanza dalla neckline 13,38%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 67.248 dal 2026-06-15 al 2026-07-15. Neckline ribassista stimata: 57.748. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 6 giorni.
  - neckline 57.748; target 48.247; distanza dalla neckline 13,38%; prezzo sopra neckline.
- Adam and Eve Top: **CANDIDATO** (0)
  - Pattern Adam and Eve Top vicino a 67.248 dal 2026-06-15 al 2026-07-15. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 57.748. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 6 giorni.
  - neckline 57.748; target 48.247; distanza dalla neckline 13,38%; prezzo sopra neckline.

### SOL

- Prezzo: **78,18 $**
- Punteggio tecnico: **-2 / 12**
- Verdetto: **NEUTRALE / MISTO**
- Trend: **Trend ribassista** (-3)
- Momentum: **Momentum in miglioramento** (2)
- Volume: **Volume da accumulazione** (1)
- Struttura: **Struttura ribassista con massimi e minimi decrescenti** (-2)
  - Dettaglio struttura: Ultimi minimi: 67.92 -> 64.42. Ultimi massimi: 83.81 -> 78.88.
- Divergenza: **Nessuna** (0)
- Fase Wyckoff candidata: **Markdown / fase ribassista** (-2)
  - Dettaglio Wyckoff: Prezzo sotto MA200 con trend a 90 giorni ancora debole.
- Fibonacci automatico: **TENUTO** (+1)
  - Swing UP 2026-06-06 60,41 -> 2026-07-15 78,88; livello più vicino 23.6% a 74,52; stato TENUTO; confluenza: neckline rialzista, invalidazione rialzista.
- Punteggio pattern: **+1**
  - rialzista dominante: Doppio minimo (MATURO, +1); ribassista dominante: Doppio massimo (CANDIDATO, 0).
- Supporto più vicino: **64,42**
- Resistenza più vicina: **78,88**

Pattern classici e ciclo di vita:

- Doppio minimo: **MATURO** (+1)
  - Due minimi simili vicino a 60,41 tra 2026-06-06 e 2026-06-25. Neckline stimata: 75,94. Breakout neckline: 2026-07-01 (20 giorni fa). Stato: MATURO. Target teorico: 91,46; progresso corrente: 14,44%. Relazione prezzo/neckline: sopra neckline.
  - neckline 75,94; target 91,46; breakout 2026-07-01 (20g); progresso 14,44%; prezzo sopra neckline.
- Triplo minimo: **CANDIDATO** (0)
  - Tre minimi simili vicino a 81,41 dal 2026-04-12 al 2026-05-23. Neckline stimata: 98,27. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 59 giorni.
  - neckline 98,27; target 115,13; distanza dalla neckline 25,69%; prezzo sotto neckline.
- Adam and Eve Bottom: **MATURO** (+1)
  - Pattern Adam and Eve Bottom vicino a 60,41 dal 2026-06-06 al 2026-06-25. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 75,94. Breakout neckline: 2026-07-01 (20 giorni fa). Stato: MATURO. Target teorico: 91,46; progresso corrente: 14,44%. Relazione prezzo/neckline: sopra neckline.
  - neckline 75,94; target 91,46; breakout 2026-07-01 (20g); progresso 14,44%; prezzo sopra neckline.
- Doppio massimo: **CANDIDATO** (0)
  - Due massimi simili vicino a 78,88 tra 2026-06-15 e 2026-07-15. Neckline ribassista stimata: 64,42. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 6 giorni.
  - neckline 64,42; target 49,96; distanza dalla neckline 21,36%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 78,88 dal 2026-06-15 al 2026-07-15. Neckline ribassista stimata: 64,42. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 6 giorni.
  - neckline 64,42; target 49,96; distanza dalla neckline 21,36%; prezzo sopra neckline.
- Adam and Eve Top: **CANDIDATO** (0)
  - Pattern Adam and Eve Top vicino a 78,88 dal 2026-06-15 al 2026-07-15. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 64,42. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 6 giorni.
  - neckline 64,42; target 49,96; distanza dalla neckline 21,36%; prezzo sopra neckline.

### DOGE

- Prezzo: **0.07277 $**
- Punteggio tecnico: **-8 / 12**
- Verdetto: **RIBASSISTA TECNICO**
- Trend: **Trend ribassista** (-3)
- Momentum: **Momentum debole** (-2)
- Volume: **Volume neutrale** (0)
- Struttura: **Struttura ribassista con massimi e minimi decrescenti** (-2)
  - Dettaglio struttura: Ultimi minimi: 0.07107 -> 0.07097. Ultimi massimi: 0.09169 -> 0.07923.
- Divergenza: **Divergenza ribassista nascosta RSI** (-1)
- Fase Wyckoff candidata: **Possibile accumulazione** (1)
  - Dettaglio Wyckoff: Prezzo sotto MA200, vicino alla parte bassa del range a 120 giorni, RSI 39.7.
- Fibonacci automatico: **NON ATTIVO** (0)
  - Swing DOWN 2026-05-14 0.11825 -> 2026-07-13 0.07097; livello più vicino 23.6% a 0.08213; stato NON ATTIVO; confluenza: nessuna confluenza indipendente.
- Punteggio pattern: **-1**
  - rialzista dominante: Doppio minimo (CANDIDATO, 0); ribassista dominante: Triplo massimo (MATURO, -1).
- Supporto più vicino: **0.07097**
- Resistenza più vicina: **0.07923**

Pattern classici e ciclo di vita:

- Doppio minimo: **CANDIDATO** (0)
  - Due minimi simili vicino a 0.06961 tra 2026-06-30 e 2026-07-13. Neckline stimata: 0.07923. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 8 giorni.
  - neckline 0.07923; target 0.08886; distanza dalla neckline 8,88%; prezzo sotto neckline.
- Triplo minimo: **ASSENTE** (0)
- Adam and Eve Bottom: **CANDIDATO** (0)
  - Pattern Adam and Eve Bottom vicino a 0.06961 dal 2026-06-30 al 2026-07-13. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 0.07923. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 8 giorni.
  - neckline 0.07923; target 0.08886; distanza dalla neckline 8,88%; prezzo sotto neckline.
- Doppio massimo: **ASSENTE** (0)
- Triplo massimo: **MATURO** (-1)
  - Tre massimi simili vicino a 0.09772 dal 2026-03-25 al 2026-06-12. Neckline ribassista stimata: 0.07809. Breakout neckline: 2026-06-24 (27 giorni fa). Stato: MATURO. Target teorico: 0.05847; progresso corrente: 27,13%. Relazione prezzo/neckline: sotto neckline.
  - neckline 0.07809; target 0.05847; breakout 2026-06-24 (27g); progresso 27,13%; prezzo sotto neckline.
- Eve and Adam Top: **MATURO** (-1)
  - Pattern Eve and Adam Top vicino a 0.09584 dal 2026-04-07 al 2026-06-12. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 0.07809. Breakout neckline: 2026-06-24 (27 giorni fa). Stato: MATURO. Target teorico: 0.06035; progresso corrente: 30,01%. Relazione prezzo/neckline: sotto neckline.
  - neckline 0.07809; target 0.06035; breakout 2026-06-24 (27g); progresso 30,01%; prezzo sotto neckline.

## Fibonacci automatico

Il modulo seleziona uno swing recente tramite pivot confermati. Un semplice tocco vale 0: Fibonacci pesa al massimo ±1 soltanto quando il livello è tenuto, perso, recuperato o respinto e coincide con almeno un livello tecnico indipendente.

| Asset   | Swing                         | 23,6%   | 38,2%   | 50,0%   | 61,8%   | 78,6%   | Livello vicino   | Stato      | Confluenza                                  |   Score |
|:--------|:------------------------------|:--------|:--------|:--------|:--------|:--------|:-----------------|:-----------|:--------------------------------------------|--------:|
| BTC | UP 2026-07-01 -> 2026-07-15 | 63.676 | 62.543 | 61.628 | 60.712 | 59.408 | 23.6% / 63.676 | TENUTO | nessuna confluenza indipendente | 0 |
| SOL | UP 2026-06-06 -> 2026-07-15 | 74,52 | 71,82 | 69,65 | 67,47 | 64,37 | 23.6% / 74,52 | TENUTO | neckline rialzista, invalidazione rialzista | +1 |
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

- **BTC**: 0/30 previsioni controllate su 19 fatte. Stato: **RACCOLTA DATI**.
- **SOL**: 0/30 previsioni controllate su 19 fatte. Stato: **RACCOLTA DATI**.
- **DOGE**: 0/30 previsioni controllate su 19 fatte. Stato: **RACCOLTA DATI**.

| Asset | Previsioni fatte | Controllate | Progresso | In attesa | Stato | Prossimo controllo |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 19 | 0 | 0/30 [░░░░░░░░░░] | 19 | RACCOLTA DATI | 2026-08-02 / tra 12 giorni |
| SOL | 19 | 0 | 0/30 [░░░░░░░░░░] | 19 | RACCOLTA DATI | 2026-08-02 / tra 12 giorni |
| DOGE | 19 | 0 | 0/30 [░░░░░░░░░░] | 19 | RACCOLTA DATI | 2026-08-02 / tra 12 giorni |

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

Generato: 2026-07-21 05:14 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [data_quality_coherence_report.md](data_quality_coherence_report.md)

Questo controllo non modifica punteggi o decisioni. Verifica che tutti i moduli usino lo stesso prezzo corrente e che le nuove regole Technical/Classic Visual siano integre.

## Stato finale: **OK**

## Prezzo unico per modulo

| Modulo                  | Asset   | Campo             | Stato   | Prezzo snapshot   | Prezzo modulo   | Differenza   |
|:------------------------|:--------|:------------------|:--------|:------------------|:----------------|:-------------|
| Scanner                 | BTC     | current_price     | OK      | 65.472 $          | 65.472 $        | +0,0000%     |
| Scanner                 | DOGE    | current_price     | OK      | 0.07277 $         | 0.07277 $       | -0,0000%     |
| Scanner                 | SOL     | current_price     | OK      | 78,18 $           | 78,18 $         | +0,0000%     |
| Scanner Forecast        | BTC     | current_price     | OK      | 65.472 $          | 65.472 $        | +0,0000%     |
| Scanner Forecast        | SOL     | current_price     | OK      | 78,18 $           | 78,18 $         | +0,0000%     |
| Scanner Forecast        | DOGE    | current_price     | OK      | 0.07277 $         | 0.07277 $       | -0,0000%     |
| Technical Structure     | BTC     | price             | OK      | 65.472 $          | 65.472 $        | +0,0000%     |
| Technical Structure     | SOL     | price             | OK      | 78,18 $           | 78,18 $         | +0,0000%     |
| Technical Structure     | DOGE    | price             | OK      | 0.07277 $         | 0.07277 $       | -0,0000%     |
| Classic Technical       | BTC     | price             | OK      | 65.472 $          | 65.472 $        | +0,0000%     |
| Classic Technical       | SOL     | price             | OK      | 78,18 $           | 78,18 $         | +0,0000%     |
| Classic Technical       | DOGE    | price             | OK      | 0.07277 $         | 0.07277 $       | -0,0000%     |
| Classic Visual          | BTC     | price             | OK      | 65.472 $          | 65.472 $        | +0,0000%     |
| Classic Visual          | SOL     | price             | OK      | 78,18 $           | 78,18 $         | +0,0000%     |
| Classic Visual          | DOGE    | price             | OK      | 0.07277 $         | 0.07277 $       | -0,0000%     |
| Exchange Microstructure | BTC     | price             | OK      | 65.472 $          | 65.482 $        | +0,0162%     |
| Exchange Microstructure | SOL     | price             | OK      | 78,18 $           | 78,16 $         | -0,0269%     |
| Exchange Microstructure | DOGE    | price             | OK      | 0.07277 $         | 0.07279 $       | +0,0275%     |
| RSI top-cycle           | SOL     | current_price     | OK      | 78,18 $           | 78,18 $         | +0,0000%     |
| RSI top-cycle           | SOL     | current_price     | OK      | 78,18 $           | 78,18 $         | +0,0000%     |
| Frattale BTC/SOL        | SOL     | sol_current_price | OK      | 78,18 $           | 78,18 $         | +0,0000%     |
| Fractal path            | SOL     | current_price     | OK      | 78,18 $           | 78,18 $         | +0,0000%     |

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
