<!-- COMPACT_REPORT_HEADER_START -->
> **Vista compatta:** Decisione operativa, Global Confluence e cambiamenti giornalieri restano aperti. Tocca il titolo di una sezione per mostrare o nascondere i dettagli.  
> Tutte le tabelle e tutti i dati restano nel file: copiando il Markdown raw viene copiato tutto.
<!-- COMPACT_REPORT_HEADER_END -->

<!-- COMPACT_SECTION_START:decision -->
<details open>
<summary><strong>🧭 Decisione operativa — da leggere per prima</strong></summary>

<!-- DECISION_REPORT_START -->

# Decisione operativa sintetica

Generato: 2026-07-18 05:14 UTC

Report separato completo: [decision_report.md](decision_report.md)

Sintesi automatica dello scanner: l'azione spot viene copiata direttamente dal Global Confluence; long, short e rischio restano filtri separati e più prudenti.

| Asset | Global | Direzione | Spot | Long leva | Short leva | Max long | Max short | Rischio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 0 | NEUTRALE / COSTRUTTIVO | HOLD / ATTESA CONFERME | NO LONG A LEVA / ATTENDI SOPRA 67.248 $ | NO SHORT | nessuna | nessuna | MEDIO / ALTO |
| SOL | -3 | LEGGERMENTE BEARISH | TAKE PROFIT SU SPIKE / NON INSEGUIRE | NO LONG A LEVA | NO SHORT | nessuna | nessuna | MOLTO ALTO |
| DOGE | -6 | BEARISH | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE | NO LONG A LEVA | SHORT SOLO DOPO SPIKE | nessuna | max 1x-2x isolated | MOLTO ALTO |

## Lettura immediata

- **BTC**: Global = **0**, spot = **HOLD / ATTESA CONFERME**, long = **NO LONG A LEVA / ATTENDI SOPRA 67.248 $**, short = **NO SHORT**, rischio = **MEDIO / ALTO**.
- **SOL**: Global = **-3**, spot = **TAKE PROFIT SU SPIKE / NON INSEGUIRE**, long = **NO LONG A LEVA**, short = **NO SHORT**, rischio = **MOLTO ALTO**.
- **DOGE**: Global = **-6**, spot = **STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE**, long = **NO LONG A LEVA**, short = **SHORT SOLO DOPO SPIKE**, rischio = **MOLTO ALTO**.

## Dettaglio logica

### BTC

- Global Confluence: **0**
- Confluenza: **MISTA / PARZIALE**
- Bias Global: **Neutrale / misto**
- Direzione decisionale: **NEUTRALE / COSTRUTTIVO**
- Azione spot dal Global: **HOLD / ATTESA CONFERME**
- Long leva: **NO LONG A LEVA / ATTENDI SOPRA 67.248 $**
- Short leva: **NO SHORT**
- Rischio: **MEDIO / ALTO**
- Conferme: Prima resistenza sopra 65.544; conferma del doppio minimo sopra 67.248.
- Invalidazioni: Sotto 57.748 il quadro tecnico peggiora.

### SOL

- Global Confluence: **-3**
- Confluenza: **DEBOLE / FRAGILE**
- Bias Global: **Fragile**
- Direzione decisionale: **LEGGERMENTE BEARISH**
- Azione spot dal Global: **TAKE PROFIT SU SPIKE / NON INSEGUIRE**
- Long leva: **NO LONG A LEVA**
- Short leva: **NO SHORT**
- Rischio: **MOLTO ALTO**
- Conferme: conferma del doppio minimo sopra 75,94; nuova conferma tecnica sopra 83,81; milestone analogiche 95,05 / 111,48, valide soltanto se rientra anche il gap frattale.
- Invalidazioni: Allarmi sotto 71,18 / 74,16 / 62,19.

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
- **Lifecycle EMA200** = per SOL resta solo contesto, peso Global 0; score interno 4; EMA200 circa 113,12 $; upside verso EMA200 +50,94%. Non autorizza leva e non aggiunge punti automatici.
- **NO LONG** non significa automaticamente **SHORT**. Lo short ha senso solo se il quadro è bearish o se lo spike viene spesso scaricato.
- Per SOL, se il Global è da **+3 in su**, la decisione non deve diventare bearish solo perché lo scanner grezzo a 30 giorni è incerto.

<!-- DECISION_REPORT_END -->

<!-- PAPER_TRADING_START -->
# Paper trading automatico KuCoin

Generato: 2026-07-18T05:14:59+00:00


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [paper_trading_report.md](paper_trading_report.md)

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-07-18T05:08:25+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-07-18T05:08:25+00:00 | 2026-07-18T05:08:25+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-07-18T04:45:00+00:00 | 2026-07-18T04:45:00+00:00 | 8,5 min | 25,0 min | OK |
| 60m | 12 | 2026-07-18T04:00:00+00:00 | 2026-07-18T04:00:00+00:00 | 8,5 min | 45,0 min | OK |
| 240m | 12 | 2026-07-18T00:00:00+00:00 | 2026-07-18T00:00:00+00:00 | 1,14 h | 1,00 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | HYPE | 240m | SHORT | -7,75 | 6,00 | 0,00 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | GRAM | 240m | SHORT | -6,25 | 6,00 | 0,00 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | LAB | 240m | SHORT | -6,25 | 6,00 | 0,00 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | ZEC | 240m | LONG | 6,25 | 6,00 | 0,00 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | DOGE | 240m | SHORT | -6,19 | 6,00 | 0,00 | STALE_CANDLE | 1,14 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | AKE | 240m | LONG | 5,75 | 6,00 | 0,25 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | SOL | 240m | SHORT | -5,30 | 6,00 | 0,70 | STALE_CANDLE | 1,14 h | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | XRP | 240m | SHORT | -3,93 | 6,00 | 2,07 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | PEPE | 240m | LONG | 3,27 | 6,00 | 2,73 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | BTC | 240m | LONG | 2,50 | 6,00 | 3,50 | STALE_CANDLE | 1,14 h | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | ADA | 240m | LONG | 1,22 | 6,00 | 4,78 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | ETH | 240m | LONG | 1,09 | 6,00 | 4,91 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Rapida 1H V2 | LAB | 60m | SHORT | -7,00 | 5,00 | 0,00 | STRATEGY_FILTER | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro V2 non superato: regime, EMA, ritorni e RSI; per Rapida V2 servono anche breakout reale, volume e ADX. |
| Rapida 1H V1 | HYPE | 60m | SHORT | -6,72 | 4,50 | 0,00 | STRATEGY_FILTER | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout DOWN oppure movimento breve ≥1,5%; breakout=NONE, movimento=-0.89%. |
| Rapida 1H V2 | HYPE | 60m | SHORT | -6,72 | 5,00 | 0,00 | STRATEGY_FILTER | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro V2 non superato: regime, EMA, ritorni e RSI; per Rapida V2 servono anche breakout reale, volume e ADX. |
| Rapida 1H V1 | GRAM | 60m | SHORT | -6,40 | 4,50 | 0,00 | STRATEGY_FILTER | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout DOWN oppure movimento breve ≥1,5%; breakout=NONE, movimento=-0.60%. |
| Rapida 1H V2 | GRAM | 60m | SHORT | -6,40 | 5,00 | 0,00 | STRATEGY_FILTER | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro V2 non superato: regime, EMA, ritorni e RSI; per Rapida V2 servono anche breakout reale, volume e ADX. |
| Rapida 1H V1 | ADA | 60m | LONG | 4,92 | 4,50 | 0,00 | STRATEGY_FILTER | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout UP oppure movimento breve ≥1,5%; breakout=NONE, movimento=+0.60%. |
| Forza relativa 1H V1 | XRP | 60m | SHORT | -4,39 | 4,00 | 0,00 | STRATEGY_FILTER | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro forza relativa: serve almeno ±2,0% contro BTC; valore=-0.69%. |
| Bilanciata 1H V1 | LAB | 60m | SHORT | -7,00 | 5,00 | 0,00 | RISK_GATE | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro rischio/esecuzione: numero massimo posizioni. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €10.010,79 | +0,11% | €10,79 | €3.000,00 | 0,36% | 3 | 14 | 35,71% | 1,00 | 4,26% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 14 | 98 | CAMPIONE INSUFFICIENTE | 30 (mancano 16) |

- Trade del Principale 4H chiusi: **14**; win rate **35,71%**; profit factor **1,00**.
- Expectancy: **€0,01** per trade; P&L netto: **€0,14**; max drawdown: **4,26%**.
- Valutazione: **Servono altri eventi indipendenti prima di trarre conclusioni.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 3 | €10.010,79 | €1.023,95 | €3.071,86 | €147,60 | €11,61 |
| TEST | Scanner Top 5 Long 1H | 2 | €10.511,36 | €1.600,63 | €3.201,27 | €101,80 | €0,00 |
| TEST | Rapida 1H V1 | 4 | €10.423,97 | €2.247,92 | €6.743,77 | €206,48 | €21,53 |
| TEST | Scanner Top 5 + forza BTC 1H | 3 | €10.409,07 | €1.867,88 | €3.735,76 | €101,31 | €93,11 |
| TEST | Combo Adaptive | 2 | €10.308,10 | €1.574,33 | €3.148,66 | €101,81 | €3,24 |
| TEST | Forza relativa 1H V2 | 4 | €10.241,18 | €2.290,71 | €4.581,42 | €151,27 | €134,36 |
| TEST | Ampia 4H | 4 | €10.240,72 | €1.561,04 | €3.122,09 | €150,11 | €121,45 |
| TEST | Benchmark Donchian breakout 1H | 0 | €10.201,07 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H V2 | 3 | €10.196,24 | €1.362,71 | €4.088,13 | €149,36 | €55,11 |
| TEST | Combo Trend | 3 | €10.182,37 | €3.048,77 | €6.097,54 | €151,18 | €14,89 |
| TEST | Combo Scanner | 2 | €10.137,62 | €808,45 | €1.616,91 | €49,63 | €90,68 |
| TEST | Scanner Bottom 5 Short 1H | 3 | €10.123,49 | €1.476,89 | €2.953,77 | €100,15 | €110,02 |
| TEST | Combo Mean Reversion | 1 | €10.117,34 | €281,61 | €563,22 | €50,37 | €-29,75 |
| TEST | Bilanciata 1H V1 | 4 | €10.087,43 | €1.461,18 | €4.383,54 | €201,39 | €18,10 |
| TEST | Forza relativa 1H V1 | 4 | €10.087,26 | €2.607,73 | €5.215,46 | €200,81 | €0,00 |
| TEST | Btc Bollinger 1H | 0 | €10.068,69 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V2 | 0 | €10.062,78 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Benchmark trend following EMA 1H | 3 | €10.044,07 | €2.089,95 | €4.179,90 | €149,62 | €16,33 |
| TEST | Doge Donchian 1H | 0 | €10.026,22 | €0,00 | €0,00 | €0,00 | €0,00 |
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
| TEST | Btc Ema 4H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 4H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 4H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 4H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 4H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Donchian 4H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 4H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 4H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Ema 4H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Donchian 1H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Bollinger 1H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Bollinger 1H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 0 | €9.998,01 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.996,80 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Donchian 1H | 0 | €9.995,51 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 1H | 0 | €9.990,84 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €9.990,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Ema 1H | 0 | €9.986,22 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 1H | 0 | €9.981,55 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Benchmark Bollinger mean reversion 1H | 1 | €9.970,50 | €277,38 | €554,76 | €49,61 | €-29,30 |
| TEST | Btc Ema 1H | 0 | €9.945,45 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 1H | 0 | €9.945,45 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Ema 1H | 0 | €9.945,10 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Adaptive 1H | 0 | €9.945,10 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 1H | 0 | €9.944,88 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 1H | 0 | €9.944,21 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Global Confluence puro 1H | 0 | €9.928,81 | €0,00 | €0,00 | €0,00 | €0,00 |

**Importante:** ogni riga è un conto virtuale separato da €10.000. I margini dei diversi portafogli non vanno sommati come se appartenessero a un unico conto.

**Rischio agli stop** è la perdita residua stimata usando gli stop correnti. Se uno stop protegge già un profitto, il rischio residuo viene mostrato come €0.

## Legenda portafogli

| Tipo | Nome leggibile | Metodo | Significato |
| --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | Confluenza trend | Riferimento principale: confluenza di trend su 4 ore, soglia più selettiva. |
| TEST | Bilanciata 1H V1 | Confluenza trend | Versione originale V1 a 1 ora basata sulla confluenza di trend. |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | Versione V2 selettiva: esclude i regimi storicamente peggiori, richiede trend e ritorni coerenti e limita i segnali correlati. |
| TEST | Rapida 1H V1 | Momentum / breakout | Versione originale V1 a 1 ora che cerca momentum e breakout. |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | Versione V2 selettiva: richiede vero breakout, volume, ADX, trend tecnico coerente e limita i segnali correlati. |
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
| PRINCIPALE | Principale 4H | Confluenza trend | €10.010,79 | €0,14 | 14 | 14 | 35,71% | 1,00 | €0,01 | 4,26% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.511,36 | €513,34 | 11 | 11 | 72,73% | 5,57 | €46,67 | 1,04% |
| TEST | Rapida 1H V1 | Momentum / breakout | €10.423,97 | €406,61 | 30 | 30 | 50,00% | 1,74 | €13,55 | 2,34% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €10.409,07 | €318,20 | 9 | 9 | 55,56% | 3,88 | €35,36 | 1,62% |
| TEST | Combo Adaptive | Combo Adaptive | €10.308,10 | €306,61 | 12 | 12 | 50,00% | 2,85 | €25,55 | 0,75% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €10.241,18 | €109,31 | 1 | 1 | 100,00% | ∞ | €109,31 | 0,22% |
| TEST | Ampia 4H | Confluenza trend | €10.240,72 | €120,20 | 6 | 6 | 33,33% | 1,76 | €20,03 | 2,08% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €10.201,07 | €201,07 | 7 | 7 | 57,14% | 2,89 | €28,72 | 1,35% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €10.196,24 | €143,31 | 7 | 5 | 71,43% | 2,29 | €20,47 | 1,46% |
| TEST | Combo Trend | Combo Trend | €10.182,37 | €170,64 | 8 | 8 | 50,00% | 2,07 | €21,33 | 1,48% |
| TEST | Combo Scanner | Combo Scanner | €10.137,62 | €47,97 | 7 | 7 | 42,86% | 1,30 | €6,85 | 1,69% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €10.123,49 | €14,60 | 4 | 4 | 50,00% | 1,14 | €3,65 | 1,14% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €10.117,34 | €147,74 | 2 | 2 | 100,00% | ∞ | €73,87 | 0,59% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €10.087,43 | €71,78 | 10 | 10 | 50,00% | 1,44 | €7,18 | 1,06% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €10.087,26 | €88,40 | 7 | 7 | 57,14% | 1,56 | €12,63 | 1,36% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.068,69 | €68,69 | 1 | 1 | 100,00% | ∞ | €68,69 | 0,31% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €10.062,78 | €62,78 | 2 | 1 | 50,00% | 11,45 | €31,39 | 0,93% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €10.044,07 | €30,25 | 4 | 4 | 50,00% | 1,28 | €7,56 | 1,10% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €10.026,22 | €26,22 | 1 | 1 | 100,00% | ∞ | €26,22 | 0,36% |
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
| TEST | Btc Ema 4H | Trend following EMA | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Sol Ema 4H | Trend following EMA | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Eth Ema 4H | Trend following EMA | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €9.998,01 | €-1,99 | 2 | 2 | 50,00% | 0,31 | €-1,00 | 0,04% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.996,80 | €-3,20 | 2 | 2 | 50,00% | 0,70 | €-1,60 | 0,16% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €9.995,51 | €-4,49 | 1 | 1 | 0,00% | 0,00 | €-4,49 | 0,43% |
| TEST | Sol Ema 1H | Trend following EMA | €9.990,84 | €-9,16 | 2 | 2 | 50,00% | 0,83 | €-4,58 | 0,87% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €9.990,05 | €-9,95 | 2 | 2 | 50,00% | 0,31 | €-4,98 | 0,18% |
| TEST | Doge Ema 1H | Trend following EMA | €9.986,22 | €-13,78 | 2 | 2 | 50,00% | 0,75 | €-6,89 | 0,87% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €9.981,55 | €-18,45 | 2 | 2 | 50,00% | 0,67 | €-9,23 | 0,89% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €9.970,50 | €0,44 | 9 | 9 | 44,44% | 1,00 | €0,05 | 2,06% |
| TEST | Btc Ema 1H | Trend following EMA | €9.945,45 | €-54,55 | 1 | 1 | 0,00% | 0,00 | €-54,55 | 0,65% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €9.945,45 | €-54,55 | 1 | 1 | 0,00% | 0,00 | €-54,55 | 0,65% |
| TEST | Eth Ema 1H | Trend following EMA | €9.945,10 | €-54,90 | 1 | 1 | 0,00% | 0,00 | €-54,90 | 0,55% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.945,10 | €-54,90 | 1 | 1 | 0,00% | 0,00 | €-54,90 | 0,55% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €9.944,88 | €-55,12 | 1 | 1 | 0,00% | 0,00 | €-55,12 | 0,67% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.944,21 | €-55,79 | 1 | 1 | 0,00% | 0,00 | €-55,79 | 0,62% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.928,81 | €-71,19 | 3 | 3 | 33,33% | 0,35 | €-23,73 | 1,18% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | DOGE | SHORT | Confluenza trend | 240m | 3,0x | 0,07292 | 0,07245 | 0,07500 | 0,09686 | 0,06875 | €574,44 | €1.723,33 | €49,28 | €11,00 |
| Principale 4H | HYPE | SHORT | Confluenza trend | 240m | 3,0x | 59,36013 | 59,26000 | 62,47190 | 78,85003 | 53,13657 | €313,25 | €939,76 | €49,26 | €1,59 |
| Principale 4H | LAB | SHORT | Confluenza trend | 240m | 3,0x | 0,17841 | 0,17884 | 0,19982 | 0,23699 | 0,13559 | €136,26 | €408,77 | €49,05 | €-0,98 |
| Bilanciata 1H V1 | NEAR | LONG | Confluenza trend | 60m | 3,0x | 2,02421 | 2,02421 | 1,97233 | 1,35960 | 2,12798 | €655,13 | €1.965,38 | €50,37 | €0,00 |
| Bilanciata 1H V1 | ALLO | SHORT | Confluenza trend | 60m | 3,0x | 0,37581 | 0,37581 | 0,40458 | 0,49921 | 0,31828 | €219,32 | €657,96 | €50,37 | €-0,00 |
| Bilanciata 1H V1 | LAB | SHORT | Confluenza trend | 60m | 3,0x | 0,18667 | 0,17884 | 0,20845 | 0,24796 | 0,14311 | €143,84 | €431,52 | €50,35 | €18,10 |
| Bilanciata 1H V1 | ONDO | LONG | Confluenza trend | 60m | 3,0x | 0,37613 | 0,37613 | 0,36189 | 0,25263 | 0,40460 | €442,89 | €1.328,68 | €50,30 | €0,00 |
| Bilanciata 1H V2 | LAB | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,18667 | 0,17884 | 0,20845 | 0,24796 | 0,14311 | €139,69 | €419,08 | €48,90 | €17,57 |
| Bilanciata 1H V2 | HYPE | SHORT | Confluenza trend V2 | 60m | 3,0x | 59,96001 | 59,26000 | 61,49831 | 79,64687 | 56,88340 | €652,82 | €1.958,47 | €50,25 | €22,86 |
| Bilanciata 1H V2 | GRAM | SHORT | Confluenza trend V2 | 60m | 3,0x | 1,49240 | 1,47960 | 1,53621 | 1,98241 | 1,40478 | €570,19 | €1.710,58 | €50,21 | €14,68 |
| Rapida 1H V1 | LAB | SHORT | Momentum / breakout | 60m | 3,0x | 0,18833 | 0,17884 | 0,20479 | 0,25016 | 0,16363 | €195,85 | €587,54 | €51,37 | €29,60 |
| Rapida 1H V1 | ONDO | LONG | Momentum / breakout | 60m | 3,0x | 0,37292 | 0,37292 | 0,36188 | 0,25048 | 0,38949 | €580,83 | €1.742,48 | €51,60 | €0,00 |
| Rapida 1H V1 | ZEC | LONG | Momentum / breakout | 60m | 3,0x | 550,22002 | 543,14000 | 536,95307 | 369,56445 | 570,12046 | €713,94 | €2.141,81 | €51,64 | €-27,56 |
| Rapida 1H V1 | GRAM | SHORT | Momentum / breakout | 60m | 3,0x | 1,49240 | 1,47960 | 1,52648 | 1,98241 | 1,44129 | €757,31 | €2.271,94 | €51,87 | €19,49 |
| Ampia 4H | DOGE | SHORT | Confluenza trend | 240m | 2,0x | 0,07237 | 0,07245 | 0,07515 | 0,10819 | 0,06457 | €649,49 | €1.298,97 | €50,00 | €-1,50 |
| Ampia 4H | ZEC | LONG | Confluenza trend | 240m | 2,0x | 522,36445 | 543,14000 | 483,09844 | 263,79405 | 632,30930 | €332,53 | €665,06 | €49,99 | €26,45 |
| Ampia 4H | HYPE | SHORT | Confluenza trend | 240m | 2,0x | 59,36013 | 59,26000 | 63,40544 | 88,74339 | 48,03325 | €367,70 | €735,40 | €50,12 | €1,24 |
| Ampia 4H | AKE | LONG | Confluenza trend | 240m | 2,0x | 0,00142 | 0,00174 | 0,00142 | 0,00072 | 0,00190 | €211,33 | €422,66 | €0,00 | €95,26 |
| Forza relativa 1H V1 | AAVE | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 98,87929 | 98,87929 | 96,58018 | n/a | 103,93735 | €1.075,02 | €2.150,03 | €49,99 | €0,00 |
| Forza relativa 1H V1 | T | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,00540 | 0,00540 | 0,00479 | n/a | 0,00676 | €219,23 | €438,46 | €49,94 | €0,00 |
| Forza relativa 1H V1 | NEAR | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 2,02421 | 2,02421 | 1,97233 | 1,02223 | 2,13836 | €984,05 | €1.968,10 | €50,44 | €0,00 |
| Forza relativa 1H V1 | ALLO | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,37581 | 0,37581 | 0,40458 | 0,56184 | 0,31252 | €329,44 | €658,87 | €50,44 | €-0,00 |
| Forza relativa 1H V2 | LAB | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,18833 | 0,17884 | 0,20950 | 0,28155 | 0,14176 | €222,78 | €445,56 | €50,08 | €22,44 |
| Forza relativa 1H V2 | HYPE | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 59,96001 | 59,26000 | 61,49831 | 89,64021 | 56,57573 | €986,06 | €1.972,12 | €50,60 | €23,02 |
| Forza relativa 1H V2 | GRAM | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 1,47771 | 1,47960 | 1,52060 | 2,20918 | 1,38336 | €871,54 | €1.743,07 | €50,59 | €-2,23 |
| Forza relativa 1H V2 | AKE | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,00143 | 0,00174 | 0,00143 | 0,00072 | 0,00181 | €210,34 | €420,67 | €0,00 | €91,12 |
| Benchmark Bollinger mean reversion 1H | LAB | LONG | Bollinger mean reversion | 60m | 2,0x | 0,18881 | 0,17884 | 0,17193 | 0,09535 | 0,21414 | €277,38 | €554,76 | €49,61 | €-29,30 |
| Benchmark trend following EMA 1H | NEAR | LONG | Trend following EMA | 60m | 2,0x | 2,02421 | 2,02421 | 1,96657 | 1,02223 | 2,15104 | €873,40 | €1.746,81 | €49,75 | €0,00 |
| Benchmark trend following EMA 1H | ALLO | SHORT | Trend following EMA | 60m | 2,0x | 0,37581 | 0,37581 | 0,40778 | 0,56184 | 0,30549 | €292,32 | €584,65 | €49,73 | €-0,00 |
| Benchmark trend following EMA 1H | HYPE | SHORT | Trend following EMA | 60m | 2,0x | 59,78804 | 59,26000 | 61,40996 | 89,38312 | 56,21982 | €924,22 | €1.848,44 | €50,14 | €16,33 |
| Scanner Top 5 Long 1H | NEAR | LONG | Scanner Top 5 Long | 60m | 2,0x | 2,02421 | 2,02421 | 1,97233 | 1,02223 | 2,12798 | €975,15 | €1.950,30 | €49,99 | €0,00 |
| Scanner Top 5 Long 1H | ONDO | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,37282 | 0,37282 | 0,35738 | 0,18828 | 0,40370 | €625,48 | €1.250,97 | €51,81 | €0,00 |
| Scanner Bottom 5 Short 1H | ALLO | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,37581 | 0,37581 | 0,40458 | 0,56184 | 0,31828 | €324,92 | €649,84 | €49,75 | €-0,00 |
| Scanner Bottom 5 Short 1H | LAB | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,22091 | 0,17884 | 0,20438 | 0,33025 | 0,16789 | €209,34 | €418,67 | €0,00 | €79,73 |
| Scanner Bottom 5 Short 1H | HYPE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 60,22795 | 59,26000 | 61,83817 | 90,04079 | 57,00752 | €942,63 | €1.885,26 | €50,40 | €30,30 |
| Scanner Top 5 + forza BTC 1H | NEAR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,02421 | 2,02421 | 1,97233 | 1,02223 | 2,13836 | €975,15 | €1.950,30 | €49,99 | €0,00 |
| Scanner Top 5 + forza BTC 1H | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,37613 | 0,37613 | 0,36189 | 0,18994 | 0,40745 | €677,81 | €1.355,62 | €51,32 | €0,00 |
| Scanner Top 5 + forza BTC 1H | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00143 | 0,00174 | 0,00145 | 0,00072 | 0,00181 | €214,92 | €429,84 | €0,00 | €93,11 |
| Combo Trend | ONDO | LONG | Combo Trend | 60m | 2,0x | 0,37282 | 0,37282 | 0,35567 | 0,18828 | 0,41057 | €545,86 | €1.091,71 | €50,24 | €0,00 |
| Combo Trend | XRP | SHORT | Combo Trend | 60m | 2,0x | 1,08689 | 1,08747 | 1,10428 | 1,62490 | 1,04863 | €1.565,99 | €3.131,98 | €50,11 | €-1,66 |
| Combo Trend | HYPE | SHORT | Combo Trend | 60m | 2,0x | 59,78804 | 59,26000 | 61,40996 | 89,38312 | 56,21982 | €936,92 | €1.873,85 | €50,83 | €16,55 |
| Combo Mean Reversion | LAB | LONG | Combo Mean Reversion | 60m | 2,0x | 0,18881 | 0,17884 | 0,17193 | 0,09535 | 0,21583 | €281,61 | €563,22 | €50,37 | €-29,75 |
| Combo Scanner | ONDO | LONG | Combo Scanner | 60m | 2,0x | 0,37282 | 0,37282 | 0,35738 | 0,18828 | 0,40679 | €599,14 | €1.198,28 | €49,63 | €0,00 |
| Combo Scanner | AKE | LONG | Combo Scanner | 60m | 2,0x | 0,00143 | 0,00174 | 0,00145 | 0,00072 | 0,00181 | €209,32 | €418,63 | €0,00 | €90,68 |
| Combo Adaptive | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,37282 | 0,37282 | 0,35738 | 0,18828 | 0,40370 | €613,42 | €1.226,85 | €50,81 | €0,00 |
| Combo Adaptive | HYPE | SHORT | Combo Adaptive | 60m | 2,0x | 59,36013 | 59,26000 | 60,93558 | 88,74339 | 56,20922 | €960,91 | €1.921,82 | €51,01 | €3,24 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Scanner Top 5 Long 1H | AKE | LONG | 2026-07-18T05:08:29+00:00 | 0,00177 | €103,39 | 1,99 | TARGET |
| Combo Adaptive | AKE | LONG | 2026-07-18T05:08:29+00:00 | 0,00177 | €101,23 | 1,99 | TARGET |
| Bilanciata 1H V2 | AKE | LONG | 2026-07-18T05:08:29+00:00 | 0,00177 | €99,77 | 1,99 | TARGET |
| Principale 4H | AKE | LONG | 2026-07-18T05:08:29+00:00 | 0,00176 | €98,25 | 1,99 | TARGET |
| Benchmark Bollinger mean reversion 1H | AKE | SHORT | 2026-07-18T04:07:13+00:00 | 0,00155 | €9,92 | 0,20 | STOP |
| Scanner Top 5 Long 1H | AKE | LONG | 2026-07-17T22:27:59+00:00 | 0,00145 | €-0,61 | -0,01 | STOP |
| Scanner Top 5 + forza BTC 1H | AKE | LONG | 2026-07-17T22:27:59+00:00 | 0,00145 | €-0,60 | -0,01 | STOP |
| Benchmark Donchian breakout 1H | AKE | LONG | 2026-07-17T22:27:59+00:00 | 0,00145 | €-0,60 | -0,01 | STOP |
| Combo Scanner | AKE | LONG | 2026-07-17T22:27:59+00:00 | 0,00145 | €-0,59 | -0,01 | STOP |
| Combo Adaptive | AKE | LONG | 2026-07-17T22:27:59+00:00 | 0,00145 | €-0,59 | -0,01 | STOP |
| Benchmark trend following EMA 1H | AKE | LONG | 2026-07-17T21:36:35+00:00 | 0,00155 | €108,46 | 2,19 | TARGET |
| Combo Trend | AKE | LONG | 2026-07-17T21:36:35+00:00 | 0,00155 | €110,30 | 2,19 | TARGET |

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

Generato: 2026-07-18 05:14 UTC


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

Segnali totali salvati: **30**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-07-18 | BTC | 63.883,71 | 0 | +1 | +1 | +3 | -1 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-07-18 | DOGE | 0.07234 | -6 | -3 | -2 | -2 | -2 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-07-18 | SOL | 74,93 | -3 | 0 | -1 | +1 | -2 | -1 | 0 | TAKE PROFIT SU SPIKE / NON INSEGUIRE |
| 2026-07-17 | BTC | 63.638,61 | -1 | +1 | +1 | +3 | -2 | 0 | 0 | NON INSEGUIRE / RIDUCI RISCHIO |
| 2026-07-17 | DOGE | 0.07218 | -6 | -3 | -2 | -3 | -2 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-07-17 | SOL | 75,11 | -5 | -1 | -1 | 0 | -3 | -1 | 0 | STAI FUORI / VENDI PARZIALE |
| 2026-07-16 | BTC | 64.033,70 | -1 | +1 | +1 | +3 | -1 | 0 | 0 | NON INSEGUIRE / RIDUCI RISCHIO |
| 2026-07-16 | DOGE | 0.07304 | -6 | -3 | -2 | -3 | -2 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-07-16 | SOL | 76,00 | -6 | -1 | -1 | 0 | -3 | -1 | 0 | STAI FUORI / VENDI PARZIALE |
| 2026-07-15 | BTC | 64.529,99 | +5 | +3 | +3 | +3 | +2 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-07-15 | DOGE | 0.07394 | -5 | -4 | -3 | -3 | -1 | 0 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-07-15 | SOL | 77,56 | +2 | +2 | +1 | +2 | -1 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 10 | 9 | 8 | 7 | 5 | 3 | 0 | 0 | 0 | 0 | 0 | 0 |
| SOL | 10 | 9 | 8 | 7 | 5 | 3 | 0 | 0 | 0 | 0 | 0 | 0 |
| DOGE | 10 | 9 | 8 | 7 | 5 | 3 | 0 | 0 | 0 | 0 | 0 | 0 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-07-09 | 10g | 2026-07-19 | domani |
| SOL | 2026-07-09 | 10g | 2026-07-19 | domani |
| DOGE | 2026-07-09 | 10g | 2026-07-19 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 9 | 33,33% | -0,02% | +0,03% | FEEDBACK RAPIDO |
| BTC | 2g | 8 | 50,00% | +0,10% | +0,16% | FEEDBACK RAPIDO |
| BTC | 3g | 7 | 57,14% | +0,11% | +0,11% | FEEDBACK RAPIDO |
| BTC | 5g | 5 | 40,00% | +0,29% | +0,29% | FEEDBACK RAPIDO |
| BTC | 7g | 3 | 33,33% | +0,22% | +0,22% | FEEDBACK RAPIDO |
| BTC | 10g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 14g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 21g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 30g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 1g | 8 | 50,00% | -0,47% | -0,49% | FEEDBACK RAPIDO |
| SOL | 2g | 7 | 28,57% | -0,82% | -0,69% | FEEDBACK RAPIDO |
| SOL | 3g | 6 | 16,67% | -1,31% | -1,70% | FEEDBACK RAPIDO |
| SOL | 5g | 4 | 50,00% | -2,49% | -0,65% | FEEDBACK RAPIDO |
| SOL | 7g | 2 | 0,00% | -3,14% | -3,14% | FEEDBACK RAPIDO |
| SOL | 10g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 14g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 21g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 30g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 1g | 9 | 66,67% | -0,24% | +0,24% | FEEDBACK RAPIDO |
| DOGE | 2g | 8 | 62,50% | -0,36% | +0,36% | FEEDBACK RAPIDO |
| DOGE | 3g | 7 | 57,14% | -0,61% | +0,61% | FEEDBACK RAPIDO |
| DOGE | 5g | 5 | 60,00% | -0,61% | +0,61% | FEEDBACK RAPIDO |
| DOGE | 7g | 3 | 66,67% | -1,43% | +1,43% | FEEDBACK RAPIDO |
| DOGE | 10g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 14g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 21g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 30g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 9 | 33,33% | -0,02% | +0,03% | -0,18% | +0,69% | FEEDBACK RAPIDO |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 9 | 33,33% | -0,02% | -0,02% | -0,18% | +0,69% | FEEDBACK RAPIDO |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 9 | 33,33% | -0,02% | -0,02% | -0,18% | +0,69% | FEEDBACK RAPIDO |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 9 | 33,33% | -0,02% | -0,02% | -0,18% | +0,69% | FEEDBACK RAPIDO |
| BTC | 1g | Tecnico | CALIBRABILE | 8 | 37,50% | -0,06% | -0,63% | -0,23% | +0,72% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 8 | 50,00% | +0,10% | +0,16% | -0,61% | +1,35% | FEEDBACK RAPIDO |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 8 | 37,50% | +0,10% | +0,10% | -0,61% | +1,35% | FEEDBACK RAPIDO |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 8 | 37,50% | +0,10% | +0,10% | -0,61% | +1,35% | FEEDBACK RAPIDO |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 8 | 37,50% | +0,10% | +0,10% | -0,61% | +1,35% | FEEDBACK RAPIDO |
| BTC | 2g | Tecnico | CALIBRABILE | 7 | 42,86% | +0,12% | -0,28% | -0,64% | +1,42% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 7 | 57,14% | +0,11% | +0,11% | -1,37% | +2,22% | FEEDBACK RAPIDO |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 7 | 57,14% | +0,11% | +0,11% | -1,37% | +2,22% | FEEDBACK RAPIDO |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 7 | 57,14% | +0,11% | +0,11% | -1,37% | +2,22% | FEEDBACK RAPIDO |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 7 | 57,14% | +0,11% | +0,11% | -1,37% | +2,22% | FEEDBACK RAPIDO |
| BTC | 3g | Tecnico | CALIBRABILE | 6 | 50,00% | +0,41% | +0,30% | -1,26% | +2,43% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 5 | 40,00% | +0,29% | +0,29% | -2,65% | +2,73% | FEEDBACK RAPIDO |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 5 | 40,00% | +0,29% | +0,29% | -2,65% | +2,73% | FEEDBACK RAPIDO |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 5 | 40,00% | +0,29% | +0,29% | -2,65% | +2,73% | FEEDBACK RAPIDO |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 5 | 40,00% | +0,29% | +0,29% | -2,65% | +2,73% | FEEDBACK RAPIDO |
| BTC | 5g | Tecnico | CALIBRABILE | 4 | 75,00% | +0,10% | +0,65% | -2,49% | +2,89% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 3 | 33,33% | +0,22% | +0,22% | -3,05% | +2,82% | FEEDBACK RAPIDO |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 3 | 33,33% | +0,22% | +0,22% | -3,05% | +2,82% | FEEDBACK RAPIDO |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 3 | 33,33% | +0,22% | +0,22% | -3,05% | +2,82% | FEEDBACK RAPIDO |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 3 | 33,33% | +0,22% | +0,22% | -3,05% | +2,82% | FEEDBACK RAPIDO |
| BTC | 7g | Tecnico | CALIBRABILE | 2 | 50,00% | +0,51% | -0,51% | -2,93% | +2,94% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 9 | 66,67% | -0,24% | +0,24% | -0,53% | +0,56% | FEEDBACK RAPIDO |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 9 | 66,67% | -0,24% | +0,24% | -0,53% | +0,56% | FEEDBACK RAPIDO |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 9 | 66,67% | -0,24% | +0,24% | -0,53% | +0,56% | FEEDBACK RAPIDO |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 9 | 66,67% | -0,24% | +0,24% | -0,53% | +0,56% | FEEDBACK RAPIDO |
| DOGE | 1g | Tecnico | CALIBRABILE | 9 | 66,67% | -0,24% | +0,24% | -0,53% | +0,56% | FEEDBACK RAPIDO |
| DOGE | 1g | Classic technical | CALIBRABILE | 8 | 62,50% | -0,12% | +0,12% | -0,38% | +0,56% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 8 | 62,50% | -0,36% | +0,36% | -1,16% | +1,38% | FEEDBACK RAPIDO |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 8 | 62,50% | -0,36% | +0,36% | -1,16% | +1,38% | FEEDBACK RAPIDO |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 8 | 62,50% | -0,36% | +0,36% | -1,16% | +1,38% | FEEDBACK RAPIDO |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 8 | 62,50% | -0,36% | +0,36% | -1,16% | +1,38% | FEEDBACK RAPIDO |
| DOGE | 2g | Tecnico | CALIBRABILE | 8 | 62,50% | -0,36% | +0,36% | -1,16% | +1,38% | FEEDBACK RAPIDO |
| DOGE | 2g | Classic technical | CALIBRABILE | 7 | 57,14% | -0,07% | +0,07% | -1,01% | +1,88% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 7 | 57,14% | -0,61% | +0,61% | -1,89% | +2,57% | FEEDBACK RAPIDO |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 7 | 57,14% | -0,61% | +0,61% | -1,89% | +2,57% | FEEDBACK RAPIDO |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 7 | 57,14% | -0,61% | +0,61% | -1,89% | +2,57% | FEEDBACK RAPIDO |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 7 | 57,14% | -0,61% | +0,61% | -1,89% | +2,57% | FEEDBACK RAPIDO |
| DOGE | 3g | Tecnico | CALIBRABILE | 7 | 57,14% | -0,61% | +0,61% | -1,89% | +2,57% | FEEDBACK RAPIDO |
| DOGE | 3g | Classic technical | CALIBRABILE | 6 | 50,00% | -0,35% | +0,35% | -1,80% | +2,92% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 5 | 60,00% | -0,61% | +0,61% | -2,85% | +2,99% | FEEDBACK RAPIDO |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 5 | 60,00% | -0,61% | +0,61% | -2,85% | +2,99% | FEEDBACK RAPIDO |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 5 | 60,00% | -0,61% | +0,61% | -2,85% | +2,99% | FEEDBACK RAPIDO |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 5 | 60,00% | -0,61% | +0,61% | -2,85% | +2,99% | FEEDBACK RAPIDO |
| DOGE | 5g | Tecnico | CALIBRABILE | 5 | 60,00% | -0,61% | +0,61% | -2,85% | +2,99% | FEEDBACK RAPIDO |
| DOGE | 5g | Classic technical | CALIBRABILE | 5 | 60,00% | -0,61% | +0,61% | -2,85% | +2,99% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 3 | 66,67% | -1,43% | +1,43% | -3,54% | +2,47% | FEEDBACK RAPIDO |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 3 | 66,67% | -1,43% | +1,43% | -3,54% | +2,47% | FEEDBACK RAPIDO |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 3 | 66,67% | -1,43% | +1,43% | -3,54% | +2,47% | FEEDBACK RAPIDO |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 3 | 66,67% | -1,43% | +1,43% | -3,54% | +2,47% | FEEDBACK RAPIDO |
| DOGE | 7g | Tecnico | CALIBRABILE | 3 | 66,67% | -1,43% | +1,43% | -3,54% | +2,47% | FEEDBACK RAPIDO |
| DOGE | 7g | Classic technical | CALIBRABILE | 3 | 66,67% | -1,43% | +1,43% | -3,54% | +2,47% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 8 | 50,00% | -0,47% | -0,49% | -0,84% | +0,44% | FEEDBACK RAPIDO |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 7 | 71,43% | -0,78% | +0,20% | -1,00% | +0,04% | FEEDBACK RAPIDO |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 9 | 66,67% | -0,40% | -0,05% | -0,73% | +0,44% | FEEDBACK RAPIDO |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 6 | 50,00% | -0,39% | +0,29% | -0,92% | +0,68% | FEEDBACK RAPIDO |
| SOL | 1g | Tecnico | CALIBRABILE | 9 | 55,56% | -0,40% | -0,00% | -0,73% | +0,44% | FEEDBACK RAPIDO |
| SOL | 1g | Classic technical | CALIBRABILE | 2 | 100,00% | -0,71% | +0,71% | -0,59% | -0,30% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 7 | 28,57% | -0,82% | -0,69% | -1,67% | +0,93% | FEEDBACK RAPIDO |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 6 | 66,67% | -1,15% | +0,09% | -2,07% | +0,39% | FEEDBACK RAPIDO |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 8 | 62,50% | -0,91% | +0,12% | -1,75% | +0,97% | FEEDBACK RAPIDO |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 6 | 33,33% | -0,72% | -0,56% | -1,73% | +1,23% | FEEDBACK RAPIDO |
| SOL | 2g | Tecnico | CALIBRABILE | 8 | 25,00% | -0,91% | -0,52% | -1,75% | +0,97% | FEEDBACK RAPIDO |
| SOL | 2g | Classic technical | CALIBRABILE | 1 | 100,00% | -1,41% | +1,41% | -1,33% | -0,87% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 6 | 16,67% | -1,31% | -1,70% | -2,63% | +2,21% | FEEDBACK RAPIDO |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 5 | 60,00% | -1,23% | -0,13% | -2,82% | +1,80% | FEEDBACK RAPIDO |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 7 | 57,14% | -1,37% | +0,40% | -2,63% | +2,08% | FEEDBACK RAPIDO |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 6 | 33,33% | -1,31% | -1,62% | -2,63% | +2,21% | FEEDBACK RAPIDO |
| SOL | 3g | Tecnico | CALIBRABILE | 7 | 42,86% | -1,37% | -0,33% | -2,63% | +2,08% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 4 | 50,00% | -2,49% | -0,65% | -3,76% | +2,44% | FEEDBACK RAPIDO |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 4 | 100,00% | -1,95% | +1,95% | -3,73% | +2,42% | FEEDBACK RAPIDO |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 5 | 100,00% | -2,03% | +2,03% | -3,92% | +2,22% | FEEDBACK RAPIDO |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 4 | 50,00% | -2,49% | -0,65% | -3,76% | +2,44% | FEEDBACK RAPIDO |
| SOL | 5g | Tecnico | CALIBRABILE | 5 | 20,00% | -2,03% | -1,27% | -3,92% | +2,22% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 2 | 0,00% | -3,14% | -3,14% | -4,81% | +1,67% | FEEDBACK RAPIDO |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 2 | 100,00% | -2,96% | +2,96% | -4,75% | +1,74% | FEEDBACK RAPIDO |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 3 | 100,00% | -3,20% | +3,20% | -4,73% | +1,62% | FEEDBACK RAPIDO |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 2 | 0,00% | -3,14% | -3,14% | -4,81% | +1,67% | FEEDBACK RAPIDO |
| SOL | 7g | Tecnico | CALIBRABILE | 3 | 0,00% | -3,20% | -3,20% | -4,73% | +1,62% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |

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

Generato: 2026-07-18 05:14 UTC

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
| BTC | 10 | FEEDBACK RAPIDO | 9 | 0 | 0 | 0 | Famiglia statistica | 1g | 33,33% | -0,02% | feedback rapido: utile da osservare, non da pesare |
| SOL | 10 | FEEDBACK RAPIDO | 9 | 0 | 0 | 0 | Tecnico | 1g | 55,56% | -0,00% | feedback rapido: utile da osservare, non da pesare |
| DOGE | 10 | FEEDBACK RAPIDO | 9 | 0 | 0 | 0 | Famiglia statistica | 1g | 66,67% | +0,24% | feedback rapido: utile da osservare, non da pesare |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Famiglia statistica | 9 | 33,33% | -0,02% | -0,02% | -0,18% | +0,69% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 8 | 37,50% | -0,63% | -0,06% | -0,23% | +0,72% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Famiglia statistica | 8 | 37,50% | +0,10% | +0,10% | -0,61% | +1,35% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 7 | 42,86% | -0,28% | +0,12% | -0,64% | +1,42% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Famiglia statistica | 7 | 57,14% | +0,11% | +0,11% | -1,37% | +2,22% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 6 | 50,00% | +0,30% | +0,41% | -1,26% | +2,43% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 5 | 40,00% | +0,29% | +0,29% | -2,65% | +2,73% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 4 | 75,00% | +0,65% | +0,10% | -2,49% | +2,89% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 3 | 33,33% | +0,22% | +0,22% | -3,05% | +2,82% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 2 | 50,00% | -0,51% | +0,51% | -2,93% | +2,94% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 8 | 62,50% | +0,12% | -0,12% | -0,38% | +0,56% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Famiglia statistica | 9 | 66,67% | +0,24% | -0,24% | -0,53% | +0,56% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 9 | 66,67% | +0,24% | -0,24% | -0,53% | +0,56% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Classic technical | 7 | 57,14% | +0,07% | -0,07% | -1,01% | +1,88% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Famiglia statistica | 8 | 62,50% | +0,36% | -0,36% | -1,16% | +1,38% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 8 | 62,50% | +0,36% | -0,36% | -1,16% | +1,38% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Classic technical | 6 | 50,00% | +0,35% | -0,35% | -1,80% | +2,92% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Famiglia statistica | 7 | 57,14% | +0,61% | -0,61% | -1,89% | +2,57% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 7 | 57,14% | +0,61% | -0,61% | -1,89% | +2,57% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Classic technical | 5 | 60,00% | +0,61% | -0,61% | -2,85% | +2,99% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 5 | 60,00% | +0,61% | -0,61% | -2,85% | +2,99% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 5 | 60,00% | +0,61% | -0,61% | -2,85% | +2,99% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Classic technical | 3 | 66,67% | +1,43% | -1,43% | -3,54% | +2,47% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 3 | 66,67% | +1,43% | -1,43% | -3,54% | +2,47% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 3 | 66,67% | +1,43% | -1,43% | -3,54% | +2,47% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Classic technical | 2 | 100,00% | +0,71% | -0,71% | -0,59% | -0,30% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Famiglia statistica | 7 | 71,43% | +0,20% | -0,78% | -1,00% | +0,04% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 9 | 55,56% | -0,00% | -0,40% | -0,73% | +0,44% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Classic technical | 1 | 100,00% | +1,41% | -1,41% | -1,33% | -0,87% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Famiglia statistica | 6 | 66,67% | +0,09% | -1,15% | -2,07% | +0,39% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 8 | 25,00% | -0,52% | -0,91% | -1,75% | +0,97% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Famiglia statistica | 5 | 60,00% | -0,13% | -1,23% | -2,82% | +1,80% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 7 | 42,86% | -0,33% | -1,37% | -2,63% | +2,08% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 4 | 100,00% | +1,95% | -1,95% | -3,73% | +2,42% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 5 | 20,00% | -1,27% | -2,03% | -3,92% | +2,22% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 2 | 100,00% | +2,96% | -2,96% | -4,75% | +1,74% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 3 | 0,00% | -3,20% | -3,20% | -4,73% | +1,62% | OSSERVA | 0,0 | BASSA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 9 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 9 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 9 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Famiglia statistica | 24 | 41,67% | +0,06% |
| BTC | BREVE | Tecnico | 21 | 42,86% | -0,25% |
| BTC | SETTIMANALE | Famiglia statistica | 8 | 37,50% | +0,26% |
| BTC | SETTIMANALE | Tecnico | 6 | 66,67% | +0,27% |
| DOGE | BREVE | Classic technical | 21 | 57,14% | +0,17% |
| DOGE | BREVE | Famiglia statistica | 24 | 62,50% | +0,39% |
| DOGE | BREVE | Tecnico | 24 | 62,50% | +0,39% |
| DOGE | SETTIMANALE | Classic technical | 8 | 62,50% | +0,92% |
| DOGE | SETTIMANALE | Famiglia statistica | 8 | 62,50% | +0,92% |
| DOGE | SETTIMANALE | Tecnico | 8 | 62,50% | +0,92% |
| SOL | BREVE | Classic technical | 3 | 100,00% | +0,94% |
| SOL | BREVE | Famiglia statistica | 18 | 66,67% | +0,07% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Tecnico | 24 | 41,67% | -0,27% |
| SOL | SETTIMANALE | Famiglia statistica | 6 | 100,00% | +2,29% |
| SOL | SETTIMANALE | Frattale SOL | 2 | 0,00% | -3,27% |
| SOL | SETTIMANALE | Tecnico | 8 | 12,50% | -2,00% |

## Aree ancora in attesa

| Asset | Famiglia | Righe senza controlli | Stato |
| --- | --- | --- | --- |
| BTC | BREVE | 9 | in attesa di controlli maturati |
| BTC | SETTIMANALE | 11 | in attesa di controlli maturati |
| BTC | SWING | 10 | in attesa di controlli maturati |
| BTC | MEDIO | 15 | in attesa di controlli maturati |
| SOL | BREVE | 4 | in attesa di controlli maturati |
| SOL | SETTIMANALE | 9 | in attesa di controlli maturati |
| SOL | SWING | 10 | in attesa di controlli maturati |
| SOL | MEDIO | 15 | in attesa di controlli maturati |
| DOGE | BREVE | 6 | in attesa di controlli maturati |
| DOGE | SETTIMANALE | 9 | in attesa di controlli maturati |
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
| BTC     |         10 |               0 |          10 | RACCOLTA DATI | n/a              | n/a             | n/a                   | n/a            |
| SOL     |         10 |               0 |          10 | RACCOLTA DATI | n/a              | n/a             | n/a                   | n/a            |
| DOGE    |         10 |               0 |          10 | RACCOLTA DATI | n/a              | n/a             | n/a                   | n/a            |

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

Generato: 2026-07-18 05:14 UTC


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
| BTC | 0 | MISTA / PARZIALE | Neutrale / misto | BASSA / RACCOLTA DATI | HOLD / ATTESA CONFERME | Prima resistenza sopra 65.544; conferma del doppio minimo sopra 67.248. | Sotto 57.748 il quadro tecnico peggiora. |
| SOL | -3 | DEBOLE / FRAGILE | Fragile | MEDIA | TAKE PROFIT SU SPIKE / NON INSEGUIRE | conferma del doppio minimo sopra 75,94; nuova conferma tecnica sopra 83,81; milestone analogiche 95,05 / 111,48, valide soltanto se rientra anche il gap frattale. | Allarmi sotto 71,18 / 74,16 / 62,19. |
| DOGE | -6 | NEGATIVA | Ribassista | MEDIA | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE | Sopra 0.07923 migliora; sopra 0.07966 viene invalidato il pattern ribassista dominante. | Sotto 0.07097 il rischio ribassista aumenta. |

## Punteggi per modulo

| Asset | Scanner grezzo | Market grezzo | Famiglia statistica | Scanner path | Tecnico | Classic tech | Frattale SOL | Fractal path | RSI top-cycle | Lifecycle EMA | Exchange flow | Futures | Daily change | Totale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +1 | +3 | +1 | 0 | -1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| SOL | -1 | +1 | 0 | 0 | -2 | -1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | -3 |
| DOGE | -2 | -2 | -3 | 0 | -2 | -1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | -6 |

Le colonne **Scanner grezzo** e **Market grezzo** sono diagnostiche: nel totale entra soltanto la colonna **Famiglia statistica**.

## Lettura asset per asset

### BTC

- Confluenza: **MISTA / PARZIALE**
- Bias: **Neutrale / misto**
- Punteggio finale: **0**
- Affidabilità: **BASSA / RACCOLTA DATI**
- Azione coerente: **HOLD / ATTESA CONFERME**

BTC è in fase mista. Non è abbastanza debole da autorizzare short semplici, ma non ha ancora una conferma piena.

Dettaglio moduli:

- Famiglia statistica: **+1** — Scanner grezzo +1, Market Regime grezzo +3, match regime 5. Scanner e regime concordi, ma i match sono meno di 10: nessun bonus. Punteggio contato nel Global: +1.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **+1** — Casi positivi 57,50%, return centrale 30g +3,00%. Direzione scanner: INCERTO. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **+3** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 5, positivi 30g 100,00%, return p50 +29,37%.
- Scanner path: **0** — Controlli disponibili 8. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **-1** — Score tecnico -1/12, verdetto neutrale / misto, trend misto, struttura ribassista con massimi e minimi decrescenti, divergenza rialzista rsi, Wyckoff possibile accumulazione, pattern score 0 (rialzista Doppio minimo / CANDIDATO; ribassista Doppio massimo / TARGET RAGGIUNTO). Fonte: technical_structure_metrics.csv.
- Classic technical: **0** — Score classico -2/12, verdetto DEBOLE / NON CONFERMATO, stage STAGE 4 / MARKDOWN, struttura MASSIMI E MINIMI CRESCENTI, Wyckoff ACCUMULO POSSIBILE / RANGE BASSO, volatilità locale BASSO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Non applicabile a questo asset.
- Fractal path: **0** — Non applicabile a questo asset.
- RSI top-cycle: **0** — Non applicabile a questo asset.
- Lifecycle EMA: **0** — Non applicabile a questo asset.
- Exchange flow: **0** — Flow +1.00, derivati +0.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +0.75; exchange 3/3, copertura 100%, consenso bull 1, bear 1, divergenze 0, campioni 4h 2 su 0.99h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias LEGGERMENTE POSITIVA / NON PESATA; confidenza BASSA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Rischio sotto, forza 4/5.
- Daily change: **0** — BTC: nessun cambiamento forte in miglioramento rispetto a ieri.

Conferme: Prima resistenza sopra 65.544; conferma del doppio minimo sopra 67.248.

Invalidazioni: Sotto 57.748 il quadro tecnico peggiora.

### SOL

- Confluenza: **DEBOLE / FRAGILE**
- Bias: **Fragile**
- Punteggio finale: **-3**
- Affidabilità: **MEDIA**
- Azione coerente: **TAKE PROFIT SU SPIKE / NON INSEGUIRE**

SOL è fragile nel breve. Il frattale da solo non basta: se non recupera le conferme e il gap non rientra, il rischio è di inseguire uno spike scaricato.

Dettaglio moduli:

- Famiglia statistica: **0** — Scanner grezzo -1, Market Regime grezzo +1, match regime 14. Scanner e regime fortemente discordanti: famiglia neutralizzata. Punteggio contato nel Global: 0.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **-1** — Casi positivi 47,50%, return centrale 30g -0,89%. Direzione scanner: INCERTO. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **+1** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 14, positivi 30g 57,14%, return p50 +0,87%.
- Scanner path: **0** — Controlli disponibili 8. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **-2** — Score tecnico -6/12, verdetto debole, trend ribassista, struttura rialzista con massimi e minimi crescenti, divergenza nessuna, Wyckoff markdown / fase ribassista, pattern score +1 (rialzista Doppio minimo / MATURO; ribassista Doppio massimo / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **-1** — Score classico -9/12, verdetto RIBASSISTA / FRAGILE, stage STAGE 4 / MARKDOWN, struttura VOLATILITÀ IN ESPANSIONE, Wyckoff ACCUMULO POSSIBILE / RANGE BASSO, volatilità locale BASSO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Verdetto ANALOGIA DEBOLE / SCENARIO SECONDARIO, somiglianza strutturale +64,35%, aderenza live +62,62%, errore live +18,69%, gap corrente +13,98%, peso operativo 0, tracking STRUTTURA STABILE, fase FRATTALE SOLO DI CONTESTO, rischio ALTO.
- Fractal path: **0** — Raccolta dati. Controlli disponibili 4, gap corrente +13,98%, errore live +18,69%. Servono almeno 5 controlli prima di pesare il percorso frattale.
- RSI top-cycle: **0** — Rischio top-cycle RSI: BASSO.
- Lifecycle EMA: **0** — Contesto non pesato nel Global. Lifecycle score 4, bias SQUEEZE SETUP MODERATO, EMA200 113,12 $, upside EMA200 +50,94%, gap EMA50/EMA200 -2,20%, hit EMA200 12w +16,67%, trend STABILE / DA CONFERMARE. Peso Global forzato a 0.
- Exchange flow: **0** — Flow +0.00, derivati +0.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +0.00; exchange 3/3, copertura 100%, consenso bull 1, bear 0, divergenze 1, campioni 4h 2 su 0.99h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias MISTA / NEUTRALE; confidenza BASSA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Misto, forza 1/5.
- Daily change: **0** — SOL: nessun cambiamento forte in misto rispetto a ieri.

Conferme: conferma del doppio minimo sopra 75,94; nuova conferma tecnica sopra 83,81; milestone analogiche 95,05 / 111,48, valide soltanto se rientra anche il gap frattale.

Invalidazioni: Allarmi sotto 71,18 / 74,16 / 62,19.

### DOGE

- Confluenza: **NEGATIVA**
- Bias: **Ribassista**
- Punteggio finale: **-6**
- Affidabilità: **MEDIA**
- Azione coerente: **STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE**

DOGE resta l'asset più debole. Anche senza contare due volte Scanner e Market Regime, la confluenza generale resta chiaramente negativa rispetto a BTC e SOL.

Dettaglio moduli:

- Famiglia statistica: **-3** — Scanner grezzo -2, Market Regime grezzo -2, match regime 29. Scanner e regime concordi con almeno 10 match: bonus massimo di 1 punto. Punteggio contato nel Global: -3.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **-2** — Casi positivi 30,00%, return centrale 30g -14,61%. Direzione scanner: DISCESA. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **-2** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 29, positivi 30g 20,69%, return p50 -20,06%.
- Scanner path: **0** — Controlli disponibili 8. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **-2** — Score tecnico -6/12, verdetto debole, trend ribassista, struttura ribassista con massimi e minimi decrescenti, divergenza ribassista nascosta rsi, Wyckoff possibile accumulazione, pattern score -1 (rialzista Doppio minimo / CANDIDATO; ribassista Triplo massimo / MATURO). Fonte: technical_structure_metrics.csv.
- Classic technical: **-1** — Score classico -11/12, verdetto RIBASSISTA / FRAGILE, stage STAGE 4 / MARKDOWN, struttura MASSIMI E MINIMI DECRESCENTI, Wyckoff MARKDOWN / DEBOLEZZA, volatilità locale BASSO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Non applicabile a questo asset.
- Fractal path: **0** — Non applicabile a questo asset.
- RSI top-cycle: **0** — Non applicabile a questo asset.
- Lifecycle EMA: **0** — Non applicabile a questo asset.
- Exchange flow: **0** — Flow -1.00, derivati +0.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche -1.00; exchange 3/3, copertura 100%, consenso bull 0, bear 2, divergenze 0, campioni 4h 2 su 0.99h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias LEGGERMENTE NEGATIVA / NON PESATA; confidenza BASSA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Rischio sotto, forza 2/5.
- Daily change: **0** — DOGE: nessun cambiamento forte in peggioramento rispetto a ieri.

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

Generato: 2026-07-18 05:14 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [btc_macro_cycle_report.md](btc_macro_cycle_report.md)

Questo modulo descrive il contesto macro di Bitcoin. Non genera entrate tattiche, non autorizza leva e pesa **0** nel Global Confluence.

## Sintesi

| Voce | Valore | Lettura |
| --- | --- | --- |
| Prezzo BTC | 63.884 $ | prezzo corrente |
| Power Law centrale | 122.459 $ | deviazione -47,83% |
| Banda p10-p90 | 76.315 $ / 307.457 $ | SOTTO LA BANDA P10 |
| Percentile residuo | 1,64% | posizione storica nel corridoio |
| Esponente β | 5,8431 | R² log-log 91,99% |
| Stabilità β | BASSA | range 1,3063 cambiando finestra |
| Ultimo halving | 2024-04-19 | 820 giorni fa |
| Fase ciclo | 56,13% | percentuale indicativa del ciclo quadriennale |
| Peso Global | 0 | CONTESTO MACRO / DIAGNOSTICO |

La Power Law viene trattata come regressione empirica, non come legge fisica. Il report mostra quanto cambia l'esponente usando finestre iniziali diverse e la confronta con il benchmark ingenuo 'prezzo invariato'.

## Bitcoin Power Law

- Campione: 2014-09-17 → 2026-07-18 (4322 osservazioni)
- Formula stimata: prezzo ≈ exp(-39.3770) × giorni^5.8431
- Prezzo centrale oggi: **122.459 $**
- Posizione corrente: **SOTTO LA BANDA P10**, percentile 1,64%
- Scarto dal centro: **-47,83%**

![Bitcoin Power Law](btc_power_law_chart.png)

![Bitcoin Power Law log-log](btc_power_law_loglog_chart.png)

### Stabilità dell'esponente

| Inizio campione | β | R² log-log |
| --- | --- | --- |
| 2014 | 5,8431 | 91,99% |
| 2015 | 5,9298 | 91,56% |
| 2016 | 5,6200 | 87,80% |
| 2017 | 4,8895 | 82,89% |
| 2018 | 4,6235 | 78,36% |

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
| 2012-11-28 → 2016-07-09 | 2014-12-08 | -18,67% | -24,19% | -37,66% | +14,83% |
| 2016-07-09 → 2020-05-11 | 2018-09-04 | -10,66% | -47,10% | -47,74% | +43,91% |
| 2020-05-11 → 2024-04-19 | 2022-07-28 | -15,95% | -12,89% | -5,06% | +22,96% |

Campione molto piccolo: questi rendimenti sono contesto di ciclo, non probabilità affidabili.

## SOL/BTC e DOGE/BTC dentro il tempo Bitcoin

![Altcoin nel ciclo BTC](alt_btc_cycle_spirals.png)

| Asset | Coppia | Forza vs BTC | Score raw | Candidato | 30g | Peso Global |
| --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | RELATIVA MISTA / NON CONFERMATA | -2 | 0 | 5.125445332939993 | 0 |
| DOGE | DOGE/BTC | SOTTOPERFORMA BTC | -6 | -1 | -14.943679762195138 | 0 |

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

Generato: 2026-07-18 05:14 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [relative_strength_btc_report.md](relative_strength_btc_report.md)

Questo modulo controlla se SOL e DOGE stanno davvero battendo Bitcoin. Una salita in USD accompagnata da una coppia ALT/BTC ribassista è spesso soltanto trascinamento di BTC.

**Protezione iniziale:** il candidato relativo è limitato a -1/0/+1, ma il peso nel Global resta **0**. La coppia BTC conferma o indebolisce il tecnico USD; non viene sommata come secondo modulo indipendente.

## Sintesi

| Asset | Coppia | Prezzo | Score raw | Candidato | Peso Global | Forza vs BTC | Confidenza | 30g | Tecnico USD | Lettura combinata |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | 0.00117320 | -2 | 0 | 0 | RELATIVA MISTA / NON CONFERMATA | BASSA | +5,13% | RIBASSISTA | QUADRO MISTO / NESSUNA CONFERMA RELATIVA |
| DOGE | DOGE/BTC | 0.00000113 | -6 | -1 | 0 | SOTTOPERFORMA BTC | MEDIA | -14,94% | RIBASSISTA | DEBOLEZZA COMPLETA: scende in USD e contro BTC |

## Matrice di lettura

| ALT/USD | ALT/BTC | Interpretazione |
| --- | --- | --- |
| Rialzista | Rialzista | Conferma migliore: sale e batte BTC |
| Rialzista | Ribassista | Sale soprattutto perché BTC trascina il mercato |
| Ribassista | Rialzista | Forza relativa nascosta / possibile rotazione futura |
| Ribassista | Ribassista | Debolezza completa |

## SOL/BTC

- **Verdetto relativo:** RELATIVA MISTA / NON CONFERMATA (-2)
- **Candidato futuro:** 0; **peso attuale Global: 0**
- **Lettura combinata USD/BTC:** QUADRO MISTO / NESSUNA CONFERMA RELATIVA
- **Struttura:** MASSIMI E MINIMI CRESCENTI
- **Rendimenti relativi:** 7g -3,60%; 30g +5,13%; 90g +3,09%; 180g -20,41%
- **Daily:** RSI 41.86; MA50 0.00115600; MA200 0.00122617
- **Weekly:** MA30 0.00122831; RSI 45.52
- **Livelli:** supporto 0.00117300; resistenza 0.00119800; breakout 60g 0.00134900; breakdown 60g 0.00100900
- **Pattern:** DOPPIO MINIMO / TARGET RAGGIUNTO; neckline 0.00113200; target 0.00117200
- **Fibonacci:** VICINO — 50.0% a 0.00117900
- **Fonte:** Yahoo Finance SOL-BTC (coppia diretta)
- **Motivi score:** prezzo sopra MA50 daily; prezzo sotto MA200 daily; MA50 daily in salita; prezzo sotto MA30 weekly; MA30 weekly in discesa; struttura con massimi/minimi crescenti; RSI relativo debole; MACD relativo negativo

![Grafico SOL/BTC](relative_strength_SOLBTC.png)

## DOGE/BTC

- **Verdetto relativo:** SOTTOPERFORMA BTC (-6)
- **Candidato futuro:** -1; **peso attuale Global: 0**
- **Lettura combinata USD/BTC:** DEBOLEZZA COMPLETA: scende in USD e contro BTC
- **Struttura:** MASSIMI E MINIMI DECRESCENTI
- **Rendimenti relativi:** 7g -1,89%; 30g -14,94%; 90g -9,61%; 180g -19,43%
- **Daily:** RSI 26.40; MA50 0.00000127; MA200 0.00000135
- **Weekly:** MA30 0.00000135; RSI 31.79
- **Livelli:** supporto 0.00000112; resistenza 0.00000128; breakout 60g 0.00000153; breakdown 60g 0.00000110
- **Pattern:** DOPPIO MASSIMO / TARGET RAGGIUNTO; neckline 0.00000131; target 0.00000113
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
| DOGE | 30g | 286 | 52,45% | +1,93% | -3,49% |
| DOGE | 90g | 284 | 53,87% | +6,93% | -8,33% |

## Tracker live e gate futuro

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto | Stato | Peso Global |
| --- | --- | --- | --- | --- | --- | --- |
| SOL | 1g | 0 | n/a | n/a | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 3g | 0 | n/a | n/a | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 7g | 0 | n/a | n/a | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 14g | 0 | n/a | n/a | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 30g | 0 | n/a | n/a | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 1g | 7 | 85,71% | +0,63% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 3g | 5 | 80,00% | +1,22% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 7g | 1 | 100,00% | +3,00% | LOCKED / RACCOLTA LIVE | 0 |
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

Ultima candela SOL usata: **18 luglio 2026**

## Verdetto: ANALOGIA DEBOLE / SCENARIO SECONDARIO

- **Fase attuale:** FRATTALE SOLO DI CONTESTO
- **Somiglianza totale:** +64,35%
- **Somiglianza strutturale:** +64,35%
- **Aderenza prezzo live:** +62,62%
- **Errore medio live:** +18,69%
- **Gap prezzo corrente:** +13,98%
- **Peso operativo suggerito:** 0
- **Affidabilita:** BASSA
- **Rischio fase:** ALTO
- **Trend tracking:** STRUTTURA STABILE
- **Sintesi:** Esistono alcuni elementi comuni, ma non abbastanza per una conferma.
- **SOL è al giorno:** 42 dal bottom usato.
- **Giorno BTC equivalente:** 2023-01-02
- **Prossimo step:** Proiezione condizionale, non conferma operativa: **Spinta rialzista abbastanza pulita.** Zona bassa **74,89 $** intorno al **19 luglio 2026**; zona alta **95,05 $** intorno al **1 agosto 2026**; fine step circa **95,05 $** entro il **1 agosto 2026**.

## Somiglianza prima e dopo inizio programma

Questa sezione separa la somiglianza della forma dall'aderenza reale del prezzo.

- **Inizio programma/scanner:** 3 luglio 2026
- **Prima del programma** = backtest retroattivo.
- **Da inizio programma** = verifica live: è la parte più importante per l'uso operativo.

| Periodo | Date | Giorni | Aderenza prezzo | Errore medio | Gap ultimo | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| Prima del programma | 6 giugno 2026 -> 2 luglio 2026 | 27 | +87,95% | +6,02% | +21,89% | ABBASTANZA ALLINEATO |
| Da inizio programma | 3 luglio 2026 -> 18 luglio 2026 | 16 | +62,62% | +18,69% | +13,98% | STACCATO / NON ADERENTE |
| Totale dal bottom | 6 giugno 2026 -> 18 luglio 2026 | 43 | +78,52% | +10,74% | +13,98% | DEVIAZIONE MODERATA |

Nota: un frattale può avere una forma simile ma un prezzo distante. In quel caso non è operativo finché il gap non rientra.

## Lettura operativa veloce

Il frattale non deve generare acquisti o leva adesso. La forma è un contesto, ma l'aderenza live del prezzo è insufficiente.

| Voce | Risposta | Perché |
| --- | --- | --- |
| Uso operativo | NO | Il frattale vale 0 punti operativi finché il prezzo resta non aderente. |
| Aderenza live | +62,62% | Errore medio live +18,69%. |
| Gap corrente | +13,98% | Deve rientrare circa entro ±12%. |
| Prima conferma prezzo | 95,05 $ | Serve anche miglioramento del gap, non solo una candela sopra il livello. |
| Seconda conferma | 111,48 $ | Rende più credibile il percorso, ma non sostituisce l'aderenza. |
| Invalidazione soft | 71,18 $ | Sotto questa zona il quadro peggiora. |
| Invalidazione forte | 62,19 $ | Sotto il bottom il paragone è quasi rotto. |

## Target ciclo fino al top BTC 2025

| Voce | Valore |
| --- | --- |
| Stato | CONTESTO / NON OPERATIVO |
| Top BTC 2025 | 6 ottobre 2025 - 124.753 $ |
| Data SOL equivalente | 21 aprile 2029 |
| Target ciclo base da oggi | 560,13 $ |
| Massimo percorso base | 560,13 $ (21 aprile 2029) |

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
| Prima conferma | 95,05 $ | Deve accompagnarsi al rientro del gap. |
| Seconda conferma | 111,48 $ | Scenario più credibile. |
| Invalidazione soft | 71,18 $ | Il frattale si indebolisce. |
| Invalidazione forte | 62,19 $ | Il paragone si rompe. |

## Proiezione veloce con date SOL

| Orizzonte | Data SOL | BTC fece | SOL base | Min percorso | Max percorso |
| --- | --- | --- | --- | --- | --- |
| 7 giorni | 25 luglio 2026 | +3,04% | 77,21 $ | 74,89 $ | 77,21 $ |
| 14 giorni | 1 agosto 2026 | +26,85% | 95,05 $ | 74,89 $ | 95,05 $ |
| 30 giorni | 17 agosto 2026 | +42,16% | 106,52 $ | 74,89 $ | 106,75 $ |
| 60 giorni | 16 settembre 2026 | +34,00% | 100,41 $ | 74,89 $ | 111,48 $ |
| 90 giorni | 16 ottobre 2026 | +68,97% | 126,61 $ | 74,89 $ | 127,87 $ |
| 120 giorni | 15 novembre 2026 | +71,86% | 128,77 $ | 74,89 $ | 136,88 $ |

## Prossimi step se SOL segue BTC 2022

| Step | Date SOL | BTC fine | SOL zona bassa | SOL zona alta | SOL fine base | Lettura |
| --- | --- | --- | --- | --- | --- | --- |
| Step 1 - prossime 2 settimane | 18 luglio 2026 -> 1 agosto 2026 | +26,85% | 74,89 $ (19 luglio 2026) | 95,05 $ (1 agosto 2026) | 95,05 $ | Spinta rialzista abbastanza pulita. |
| Step 2 - primo mese | 2 agosto 2026 -> 17 agosto 2026 | +42,16% | 92,89 $ (3 agosto 2026) | 106,75 $ (14 agosto 2026) | 106,52 $ | Spinta rialzista abbastanza pulita. |
| Step 3 - secondo mese | 18 agosto 2026 -> 16 settembre 2026 | +34,00% | 97,21 $ (26 agosto 2026) | 111,48 $ (5 settembre 2026) | 100,41 $ | Spinta rialzista abbastanza pulita. |
| Step 4 - terzo mese | 17 settembre 2026 -> 16 ottobre 2026 | +68,97% | 90,64 $ (23 settembre 2026) | 127,87 $ (14 ottobre 2026) | 126,61 $ | Spinta rialzista abbastanza pulita. |

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
| Prezzo SOL | 74,93 $ |  |
| Weekly RSI | 39,17 / linea grezza 54,13 | LINEA NON AFFIDABILE / RISCHIO NON ATTIVO — IRREALISTICA / NON OPERATIVA |
| Monthly RSI | 40,70 / linea grezza 56,16 | RSI TROPPO BASSO PER RISCHIO TOP — VALIDA / USO PRUDENTE |
| Target ciclo base | 560,13 $ | Avanzamento +13,38% |
| Rischio top-cycle RSI | BASSO | Nessun segnale top-cycle macro attivo. Prezzo ancora lontano dal target ciclo; il filtro RSI resta solo di monitoraggio. |

## Lettura semplice

- Weekly: La top-line weekly non supera i controlli di qualità. Non viene usata per generare rischio top-cycle.
- Monthly: RSI monthly è 40,7, sotto la soglia prudente 55. Anche se fosse vicino alla linea, non è una vera zona di esaurimento ciclo.
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
| Prezzo SOL | 74,93 $ |
| TVL Solana | 4,82 mld $ |
| TVL 7g | -2,21% |
| DEX volume 24h | 1,43 mld $ |
| Fees 24h | 5,61 mln $ |
| Stablecoin su Solana | 15,63 mld $ |
| Stake ratio | 67,59% |
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
| Confronto precedente | 2026-07-13 |
| Fonte prezzi | Yahoo Finance SOL-USD weekly |
| Prezzo SOL | 74,93 $ |
| EMA200 weekly target | 113,12 $ |
| Upside verso EMA200 | +50,94% |
| Distanza prezzo da EMA200 | -33,75% |
| Gap EMA50/EMA200 | -2,20% |
| Stato cross | EMA50 SOTTO EMA200 |
| RSI weekly | 39,18 |
| Età SOL | 6,3 anni |
| Analoghi storici usati | 30 |
| Max analoghi per asset | 3 |
| Hit EMA200 12w analoghi | +16,67% |
| Max gain mediano 12w | +23,66% |
| Drawdown mediano 12w | -21,62% |

Lettura semplice:

**CONTESTO INTERESSANTE, SERVONO CONFERME DI PREZZO**

Autocontrollo: **STABILE / DA CONFERMARE**.

Questo modulo confronta SOL con altre crypto in fasi simili di età, distanza da EMA200, EMA50/EMA200 e RSI. Non usa stock market.

Nota importante: **questo modulo ora NON pesa più nel Global Confluence**. Resta solo come contesto di ciclo e come mappa verso EMA200 weekly. Il punteggio Global resta guidato da prezzo, scanner, regime, struttura tecnica, frattale, RSI e conferme reali.

Nota: se EMA50/EMA200 sono dentro ±2%, il modulo parla di medie sovrapposte / incrocio in corso, perché exchange diversi possono mostrare il cross leggermente prima o dopo.

<!-- Generato: 2026-07-18 05:14 UTC -->
<!-- MAJOR_ALT_LIFECYCLE_SQUEEZE_END -->

</details>
<!-- COMPACT_SECTION_END:major_alt_lifecycle -->

# Report giornaliero BTC / SOL / DOGE

Aggiornato il: **2026-07-18 05:12:23 UTC**

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
| BTC | NESSUN CAMBIAMENTO FORTE | miglioramento | NEUTRALE / INCERTO | +57.50% | +2.50 punti |
| SOL | NESSUN CAMBIAMENTO FORTE | misto | NEUTRALE / INCERTO | +47.50% | 0.00 punti |
| DOGE | NESSUN CAMBIAMENTO FORTE | peggioramento | RIBASSISTA | +30.00% | 0.00 punti |

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
| BTC | 60.695 $ | 70.278 $ | +38,71% | +15,79% | rimbalzo debole | 70.278 $ | 60.695 $ | +19,05% | -13,64% | spike storicamente più resistente |
| SOL | 71,18 $ | 82,42 $ | +16,67% | +15,79% | rimbalzo poco frequente | 82,42 $ | 71,18 $ | +18,75% | -13,64% | spike storicamente più resistente |
| DOGE | 0,06875 $ | 0,07961 $ | +15,15% | +15,79% | rimbalzo poco frequente | 0,07961 $ | 0,06875 $ | +33,33% | -13,64% | spike storicamente più resistente |

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

- **BTC: su 40 casi simili, 31 prima sono scesi a -5,00%. Tra quei 31, 12 poi sono rimbalzati fino a +10,00%. Percentuale: +38,71% (12/31). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.**
- **BTC: su 40 casi simili, 21 prima sono saliti a +10,00%. Tra quei 21, 4 poi sono scaricati a -5,00%. Percentuale: +19,05% (4/21). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.**
- **SOL: su 40 casi simili, 30 prima sono scesi a -5,00%. Tra quei 30, 5 poi sono rimbalzati fino a +10,00%. Percentuale: +16,67% (5/30). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.**
- **SOL: su 40 casi simili, 16 prima sono saliti a +10,00%. Tra quei 16, 3 poi sono scaricati a -5,00%. Percentuale: +18,75% (3/16). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.**
- **DOGE: su 40 casi simili, 33 prima sono scesi a -5,00%. Tra quei 33, 5 poi sono rimbalzati fino a +10,00%. Percentuale: +15,15% (5/33). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.**
- **DOGE: su 40 casi simili, 15 prima sono saliti a +10,00%. Tra quei 15, 5 poi sono scaricati a -5,00%. Percentuale: +33,33% (5/15). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.**

<!-- BOUNCE_AFTER_DRAWDOWN_END -->

</details>
<!-- COMPACT_SECTION_END:bounce_after_drawdown -->

<!-- COMPACT_SECTION_START:scanner_forecast -->
<details>
<summary><strong>🔭 Cono probabilistico dello scanner</strong></summary>

<!-- SCANNER_FORECAST_TRACKER_START -->
# Scanner forecast path / cono probabilistico

Generato: 2026-07-18 05:13:52 UTC


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
| BTC | 2026-07-18 | 63.889 $ | INCERTO | 57,50% | 49.270,98 $ | 54.170,66 $ | 65.807,17 $ | 71.284,57 $ | 80.961,75 $ |
| SOL | 2026-07-18 | 74,93 $ | INCERTO | 47,50% | 57,58 $ | 65,39 $ | 74,26 $ | 82,76 $ | 89,46 $ |
| DOGE | 2026-07-18 | 0.07237 $ | DISCESA | 30,00% | 0.05122 $ | 0.05502 $ | 0.06180 $ | 0.07421 $ | 0.08596 $ |

## Grafici

### BTC

![Scanner forecast BTC](scanner_forecast_BTC.png)

#### Verifica storica e discrepanza

![Verifica storica cono BTC](scanner_forecast_history_BTC.png)

- Cono congelato il **2026-07-10**; verificato fino al **2026-07-18**; stato **PARZIALE 8/30g**.
- Reale **63.883,71 $**; p50 previsto **68.812,08 $**; scarto **-7,16%**.
- Errore medio assoluto **3,33%**; massimo **7,16%**; DENTRO p10-p90; FUORI p25-p75.

### SOL

![Scanner forecast SOL](scanner_forecast_SOL.png)

#### Verifica storica e discrepanza

![Verifica storica cono SOL](scanner_forecast_history_SOL.png)

- Cono congelato il **2026-07-10**; verificato fino al **2026-07-18**; stato **PARZIALE 8/30g**.
- Reale **74,94 $**; p50 previsto **78,55 $**; scarto **-4,59%**.
- Errore medio assoluto **2,93%**; massimo **5,47%**; DENTRO p10-p90; DENTRO p25-p75.

### DOGE

![Scanner forecast DOGE](scanner_forecast_DOGE.png)

#### Verifica storica e discrepanza

![Verifica storica cono DOGE](scanner_forecast_history_DOGE.png)

- Cono congelato il **2026-07-10**; verificato fino al **2026-07-18**; stato **PARZIALE 8/30g**.
- Reale **0.07235 $**; p50 previsto **0.07196 $**; scarto **0,54%**.
- Errore medio assoluto **1,08%**; massimo **2,71%**; DENTRO p10-p90; DENTRO p25-p75.

## Accuratezza percorso scanner

| Asset   | Giorno   |   Controlli | Dentro p10-p90   | Dentro p25-p75   | Errore medio abs vs p50   | Errore medio vs p50   |
|:--------|:---------|------------:|:-----------------|:-----------------|:--------------------------|:----------------------|
| BTC | 1g | 8 | 100,00% | 87,50% | 1,86% | -0,86% |
| BTC | 3g | 6 | 100,00% | 66,67% | 3,50% | -3,50% |
| BTC | 7g | 2 | 100,00% | 0,00% | 6,19% | -6,19% |
| BTC | 14g | 0 | n/a | n/a | n/a | n/a |
| BTC | 30g | 0 | n/a | n/a | n/a | n/a |
| SOL | 1g | 8 | 87,50% | 75,00% | 2,08% | -1,46% |
| SOL | 3g | 6 | 100,00% | 50,00% | 2,79% | -2,54% |
| SOL | 7g | 2 | 100,00% | 100,00% | 3,94% | -3,94% |
| SOL | 14g | 0 | n/a | n/a | n/a | n/a |
| SOL | 30g | 0 | n/a | n/a | n/a | n/a |
| DOGE | 1g | 8 | 100,00% | 50,00% | 2,02% | -0,05% |
| DOGE | 3g | 6 | 100,00% | 100,00% | 1,42% | -1,10% |
| DOGE | 7g | 2 | 100,00% | 100,00% | 1,56% | 1,56% |
| DOGE | 14g | 0 | n/a | n/a | n/a | n/a |
| DOGE | 30g | 0 | n/a | n/a | n/a | n/a |

## Calibratore shadow

Il cono ufficiale resta grezzo e invariato. Il calibratore usa soltanto previsioni passate già mature, campionate una volta a settimana per ridurre la falsa indipendenza. Ogni orizzonte si attiva a 30 controlli indipendenti: parte al 25% della correzione stimata e cresce gradualmente fino al 100% a 100 controlli.

| Asset   | Orizzonte   |   Controlli indipendenti |   Soglia | Stato                  | Forza correzione   | Shift p50   |   Scala p10-p90 |
|:--------|:------------|-------------------------:|---------:|:-----------------------|:-------------------|:------------|----------------:|
| BTC | 1g | 2 | 30 | RACCOLTA (28 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 3g | 2 | 30 | RACCOLTA (28 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 7g | 1 | 30 | RACCOLTA (29 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 14g | 0 | 30 | RACCOLTA (30 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 30g | 0 | 30 | RACCOLTA (30 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 1g | 2 | 30 | RACCOLTA (28 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 3g | 2 | 30 | RACCOLTA (28 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 7g | 1 | 30 | RACCOLTA (29 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 14g | 0 | 30 | RACCOLTA (30 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 30g | 0 | 30 | RACCOLTA (30 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 1g | 2 | 30 | RACCOLTA (28 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 3g | 2 | 30 | RACCOLTA (28 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 7g | 1 | 30 | RACCOLTA (29 mancanti) | 0,0% | 0,00% | 1,000 |
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

Righe salvate nello storico: **18**.

Questa sezione tiene un diario delle previsioni giornaliere a 30 giorni, senza appesantire il report principale.

| Data | Asset | Prezzo | Direzione | Casi positivi | Return p50 | Drawdown p50 | Max gain p50 | Controllo 30g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-07-18 | BTC | 63.889 $ | INCERTO | 57,50% | 65.807 $ | 58.184 $ | 71.021 $ | 2026-08-17 |
| 2026-07-18 | DOGE | 0,07000 $ | DISCESA | 30,00% | 0,06000 $ | 0,06000 $ | 0,07000 $ | 2026-08-17 |
| 2026-07-18 | SOL | 74,93 $ | INCERTO | 47,50% | 74,26 $ | 67,16 $ | 80,80 $ | 2026-08-17 |

<!-- FORECAST_30D_HISTORY_END -->

</details>
<!-- COMPACT_SECTION_END:scanner_forecast -->

<!-- COMPACT_SECTION_START:extreme_cases -->
<details>
<summary><strong>⚠️ Percorso dei casi estremi</strong></summary>

<!-- EXTREME_CASES_PATH_START -->
# Extreme cases path report

Generato: 2026-07-18 05:14 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [extreme_cases_path_report.md](extreme_cases_path_report.md)

Questo report si attiva quando i casi positivi o negativi sono almeno **80%**.

Ora misura anche il **rialzo massimo prima della discesa principale**, quindi distingue uno spike iniziale da una discesa quasi immediata.

## Trigger estremi

| Asset   | Direzione   | Trigger   | Percentuale   | Motivo                           |   Match disponibili |
|:--------|:------------|:----------|:--------------|:---------------------------------|--------------------:|
| BTC     | NESSUNO     | NO        | +57,50%       | Nessun lato sopra soglia estrema |                  40 |
| SOL     | NESSUNO     | NO        | +52,50%       | Nessun lato sopra soglia estrema |                  40 |
| DOGE    | NESSUNO     | NO        | +70,00%       | Nessun lato sopra soglia estrema |                  40 |

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
- Prezzo attuale: **63.889,06 $**
- Return normale fra 30 giorni: **65.807,17 $** (3,00%)
- Drawdown normale durante il mese: **58.184,02 $** (-8,93%)
- Drawdown brutto da rispettare: **53.351,38 $** (-16,49%)
- Max gain normale durante il mese: **71.020,60 $** (11,16%)
- Max gain buono / take profit ottimistico: **76.221,01 $** (19,30%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Solana
- Direzione più probabile a 30 giorni: **INCERTO**
- Casi positivi / salita storica: **47,50%**
- Casi negativi / discesa storica: **52,50%**
- Quanto è netto il segnale: **molto debole / quasi pari**
- Prezzo attuale: **74,93 $**
- Return normale fra 30 giorni: **74,26 $** (-0,89%)
- Drawdown normale durante il mese: **67,16 $** (-10,37%)
- Drawdown brutto da rispettare: **60,91 $** (-18,71%)
- Max gain normale durante il mese: **80,80 $** (7,84%)
- Max gain buono / take profit ottimistico: **86,64 $** (15,62%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Dogecoin
- Direzione più probabile a 30 giorni: **DISCESA**
- Casi positivi / salita storica: **30,00%**
- Casi negativi / discesa storica: **70,00%**
- Quanto è netto il segnale: **forte**
- Prezzo attuale: **0,07 $**
- Return normale fra 30 giorni: **0,06 $** (-14,61%)
- Drawdown normale durante il mese: **0,06 $** (-23,99%)
- Drawdown brutto da rispettare: **0,05 $** (-32,67%)
- Max gain normale durante il mese: **0,07 $** (2,22%)
- Max gain buono / take profit ottimistico: **0,08 $** (16,45%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Messaggio del giorno

Il quadro generale oggi è misto. Alcuni asset possono avere lettura diversa, quindi è meglio valutare asset per asset.

---

# Mappa semplice asset per asset

# Bitcoin — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟡 GIALLO / Incerto
**Prezzo attuale:** 63.889,06 $

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

- Se va molto male: **49.270,98 $** (-22,88%)
- Se va male: **54.170,66 $** (-15,21%)
- Scenario normale: **65.807,17 $** (3,00%)
- Se va bene: **71.284,57 $** (11,58%)
- Se va molto bene: **80.961,75 $** (26,72%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **58.184,02 $** (-8,93%)
- Discesa brutta: **53.351,38 $** (-16,49%)
- Discesa molto brutta: **45.136,89 $** (-29,35%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **71.020,60 $** (11,16%)
- Rialzo buono: **76.221,01 $** (19,30%)
- Rialzo molto forte: **85.265,29 $** (33,46%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Bitcoin tendeva a muoversi tra una zona bassa intorno a **58.184,02 $** e uno spike normale intorno a **71.020,60 $**.

La chiusura a 30 giorni è incerta: salita 57,50%, discesa 42,50%. Non c'è un vantaggio netto.

Nota leva BTC: se la liquidazione è vicina a 51.000 $, guarda soprattutto la discesa brutta e molto brutta. Il prezzo può recuperare dopo, ma la leva può saltare prima.

---

# Solana — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟡 GIALLO / Incerto
**Prezzo attuale:** 74,93 $

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

- Se va molto male: **57,58 $** (-23,15%)
- Se va male: **65,39 $** (-12,73%)
- Scenario normale: **74,26 $** (-0,89%)
- Se va bene: **82,76 $** (10,45%)
- Se va molto bene: **89,46 $** (19,40%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **67,16 $** (-10,37%)
- Discesa brutta: **60,91 $** (-18,71%)
- Discesa molto brutta: **54,33 $** (-27,49%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **80,80 $** (7,84%)
- Rialzo buono: **86,64 $** (15,62%)
- Rialzo molto forte: **101,63 $** (35,63%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Solana tendeva a muoversi tra una zona bassa intorno a **67,16 $** e uno spike normale intorno a **80,80 $**.

La chiusura a 30 giorni è incerta: salita 47,50%, discesa 52,50%. Non c'è un vantaggio netto.

---

# Dogecoin — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🔴 ROSSO / Prudenza
**Prezzo attuale:** 0,07 $

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

- Se va molto male: **0,05 $** (-29,23%)
- Se va male: **0,06 $** (-23,97%)
- Scenario normale: **0,06 $** (-14,61%)
- Se va bene: **0,07 $** (2,55%)
- Se va molto bene: **0,09 $** (18,77%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **0,06 $** (-23,99%)
- Discesa brutta: **0,05 $** (-32,67%)
- Discesa molto brutta: **0,04 $** (-40,41%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **0,07 $** (2,22%)
- Rialzo buono: **0,08 $** (16,45%)
- Rialzo molto forte: **0,10 $** (37,74%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Dogecoin tendeva a muoversi tra una zona bassa intorno a **0,06 $** e uno spike normale intorno a **0,07 $**.

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

## Semaforo: 🟡 GIALLO / Incerto

**Prezzo attuale:** 63.889,06 $

Bitcoin è in una situazione incerta. Lo scanner non vede un vantaggio chiaro né per la salita né per la discesa. In questi casi è meglio non forzare la previsione.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **57,50%**
- Casi negativi dopo 30 giorni: **42,50%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **86,14%**
- Rendimento medio dopo 30 giorni: **1,23%**
- Rendimento centrale dopo 30 giorni: **3,00%**
- Discesa media durante i 30 giorni: **-12,80%**
- Massimo rialzo medio durante i 30 giorni: **16,47%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **64.677,21 $**
- Scenario centrale a 30 giorni: **65.807,17 $**
- Zona di rischio media: **55.709,15 $**
- Zona di rialzo media: **74.409,62 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -22,88% → **49.270,98 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -15,21% → **54.170,66 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: 3,00% → **65.807,17 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 11,58% → **71.284,57 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 26,72% → **80.961,75 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -29,35% → **45.136,89 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -16,49% → **53.351,38 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -8,93% → **58.184,02 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -6,76% → **59.572,33 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: -0,35% → **63.666,68 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 0,00% → **63.889,06 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 3,54% → **66.151,33 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 11,16% → **71.020,60 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 19,30% → **76.221,01 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 33,46% → **85.265,29 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| LRC-USD         | 2018-09-24   | 2019-01-01 |        90.61 |        30.68 |          -8.53 |         146.68 |
| FIL-USD         | 2023-06-24   | 2023-10-01 |        89.47 |        10.53 |          -8.25 |          11.57 |
| SAND-USD        | 2023-06-24   | 2023-10-01 |        89.19 |         7.39 |         -12.66 |          11.3  |
| XLM-USD         | 2020-07-10   | 2020-10-17 |        89.02 |        -0.02 |          -8.94 |           4.3  |
| ONE-USD         | 2020-01-17   | 2020-04-25 |        87.77 |         4.38 |          -2.69 |          13.22 |
| NEAR-USD        | 2024-04-20   | 2024-07-28 |        87.58 |       -16.86 |         -35.24 |           0    |
| XRP-USD         | 2019-10-04   | 2020-01-11 |        87.1  |        29.37 |           0    |          33.33 |
| EGLD-USD        | 2024-02-15   | 2024-05-24 |        87.04 |       -27.26 |         -27.26 |           3.6  |
| EOS-USD         | 2023-06-25   | 2023-10-02 |        86.8  |        11.5  |          -8.92 |          11.5  |
| DOT-USD         | 2023-06-25   | 2023-10-02 |        86.75 |        14.72 |         -11.52 |          14.72 |

---

# Approfondimento tecnico — Solana (SOL-USD)

## Semaforo: 🟡 GIALLO / Incerto

**Prezzo attuale:** 74,93 $

Solana è in una situazione incerta. Lo scanner non vede un vantaggio chiaro né per la salita né per la discesa. In questi casi è meglio non forzare la previsione.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **47,50%**
- Casi negativi dopo 30 giorni: **52,50%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **76,58%**
- Rendimento medio dopo 30 giorni: **-1,01%**
- Rendimento centrale dopo 30 giorni: **-0,89%**
- Discesa media durante i 30 giorni: **-12,42%**
- Massimo rialzo medio durante i 30 giorni: **14,73%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **74,17 $**
- Scenario centrale a 30 giorni: **74,26 $**
- Zona di rischio media: **65,62 $**
- Zona di rialzo media: **85,96 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -23,15% → **57,58 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -12,73% → **65,39 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: -0,89% → **74,26 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 10,45% → **82,76 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 19,40% → **89,46 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -27,49% → **54,33 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -18,71% → **60,91 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -10,37% → **67,16 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -5,53% → **70,79 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: 0,00% → **74,93 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 0,27% → **75,14 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 1,97% → **76,40 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 7,84% → **80,80 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 15,62% → **86,64 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 35,63% → **101,63 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| WAVES-USD       | 2019-03-03   | 2019-06-10 |        80.87 |       -27.46 |         -27.46 |           4.37 |
| QTUM-USD        | 2018-09-29   | 2019-01-06 |        79.76 |       -23.14 |         -23.14 |           4.01 |
| RUNE-USD        | 2025-12-12   | 2026-03-21 |        78.86 |         2.99 |          -7.87 |           5.19 |
| SOL-USD         | 2025-12-09   | 2026-03-18 |        78.76 |        -1.32 |         -12.34 |           1.82 |
| VET-USD         | 2020-01-14   | 2020-04-22 |        78.63 |        19.21 |           0    |          23.27 |
| NEAR-USD        | 2024-04-20   | 2024-07-28 |        78.46 |       -16.86 |         -35.24 |           0    |
| BNB-USD         | 2025-12-11   | 2026-03-20 |        78.31 |        -4    |          -9.19 |           0.8  |
| ZIL-USD         | 2018-09-26   | 2019-01-03 |        77.98 |        -8.08 |          -8.08 |          21.45 |
| APT-USD         | 2024-09-11   | 2024-12-19 |        77.67 |       -23.26 |         -23.26 |           3.72 |
| LRC-USD         | 2018-09-29   | 2019-01-06 |        77.47 |        21.04 |         -13.46 |         133.38 |

---

# Approfondimento tecnico — Dogecoin (DOGE-USD)

## Semaforo: 🔴 ROSSO / Prudenza

**Prezzo attuale:** 0,07 $

Dogecoin richiede prudenza. La statistica dei casi simili indica più possibilità di discesa che di salita. Con leva, il rischio principale è il drawdown durante il percorso.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **30,00%**
- Casi negativi dopo 30 giorni: **70,00%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **86,72%**
- Rendimento medio dopo 30 giorni: **-9,22%**
- Rendimento centrale dopo 30 giorni: **-14,61%**
- Discesa media durante i 30 giorni: **-22,23%**
- Massimo rialzo medio durante i 30 giorni: **11,90%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **0,07 $**
- Scenario centrale a 30 giorni: **0,06 $**
- Zona di rischio media: **0,06 $**
- Zona di rialzo media: **0,08 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -29,23% → **0,05 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -23,97% → **0,06 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: -14,61% → **0,06 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 2,55% → **0,07 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 18,77% → **0,09 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -40,41% → **0,04 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -32,67% → **0,05 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -23,99% → **0,06 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -8,10% → **0,07 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: -3,68% → **0,07 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 0,00% → **0,07 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 0,00% → **0,07 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 2,22% → **0,07 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 16,45% → **0,08 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 37,74% → **0,10 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| ZEC-USD         | 2019-05-27   | 2019-09-03 |        89.52 |       -18.14 |         -23.06 |          15.5  |
| VET-USD         | 2022-03-04   | 2022-06-11 |        88.88 |       -20.06 |         -21.27 |           0    |
| XRP-USD         | 2019-09-29   | 2020-01-06 |        88.76 |        25.26 |          -7.5  |          25.26 |
| DASH-USD        | 2022-02-25   | 2022-06-04 |        88.59 |       -24.48 |         -29.01 |           2.36 |
| NEAR-USD        | 2022-03-12   | 2022-06-19 |        88.19 |        38.17 |          -2.98 |          38.17 |
| OP-USD          | 2025-12-12   | 2026-03-21 |        88.12 |         5.52 |         -13.3  |          14.55 |
| OMG-USD         | 2022-03-02   | 2022-06-09 |        88.02 |       -28.92 |         -36.72 |           0    |
| INJ-USD         | 2022-02-27   | 2022-06-06 |        87.91 |       -37.21 |         -41.89 |           0    |
| QTUM-USD        | 2022-03-02   | 2022-06-09 |        87.79 |       -22.26 |         -33.72 |           0    |
| ENJ-USD         | 2022-03-02   | 2022-06-09 |        87.69 |       -10.4  |         -33.49 |           0    |

</details>
<!-- COMPACT_SECTION_END:scanner_full_detail -->

<!-- COMPACT_SECTION_START:market_regime -->
<details>
<summary><strong>🌦️ Market Regime Match</strong></summary>

<!-- MARKET_REGIME_MATCH_START -->
# Market Regime Match Report


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [market_regime_match_report.md](market_regime_match_report.md)

Generated: 2026-07-18 05:14 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | BEAR | 63.889 $ | False | -13.50% | -9.83% | BEAR | -13.50% | -9.83% |
| DOGE-USD | BEAR | 0.07237 $ | False | -22.25% | -15.83% | BEAR | -13.50% | -9.83% |
| SOL-USD | BEAR | 74,93 $ | False | -10.34% | -17.11% | BEAR | -13.50% | -9.83% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 57.50% | 3.00% | 11.58% | 26.72% | -8.93% | -29.35% | 11.16% | 19.30% | 33.46% | 55.00% | 2.46% | 32.99% | 48.78% |
| BTC-USD | SAME_BTC_REGIME | 6 | 100.00% | 17.45% | 38.84% | 44.72% | 0.00% | -6.13% | 26.92% | 46.51% | 55.27% | 33.33% | -1.25% | 4.02% | 22.09% |
| BTC-USD | SAME_ASSET_REGIME | 19 | 89.47% | 10.53% | 24.23% | 32.94% | -8.08% | -11.93% | 15.79% | 25.93% | 52.65% | 73.68% | 26.74% | 44.28% | 59.75% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 5 | 100.00% | 29.37% | 41.99% | 45.26% | 0.00% | -4.58% | 33.33% | 50.91% | 56.14% | 40.00% | -1.70% | 5.62% | 25.38% |
| DOGE-USD | ALL_MATCHES | 40 | 30.00% | -14.61% | 2.55% | 18.77% | -23.99% | -40.41% | 2.22% | 16.45% | 37.74% | 57.50% | 3.00% | 24.62% | 40.00% |
| DOGE-USD | SAME_BTC_REGIME | 31 | 22.58% | -16.19% | -0.30% | 21.54% | -27.66% | -41.89% | 0.00% | 14.71% | 32.19% | 58.06% | 2.52% | 15.48% | 39.29% |
| DOGE-USD | SAME_ASSET_REGIME | 33 | 27.27% | -16.19% | 2.30% | 18.32% | -27.10% | -41.56% | 1.91% | 15.11% | 31.31% | 60.61% | 5.97% | 25.86% | 39.81% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 29 | 20.69% | -20.06% | -0.32% | 12.13% | -27.66% | -41.96% | 0.00% | 14.55% | 28.68% | 55.17% | 0.93% | 10.77% | 32.17% |
| SOL-USD | ALL_MATCHES | 40 | 47.50% | -0.89% | 10.45% | 19.40% | -10.37% | -27.49% | 7.84% | 15.62% | 35.63% | 60.00% | 2.82% | 26.74% | 39.78% |
| SOL-USD | SAME_BTC_REGIME | 16 | 50.00% | 0.18% | 6.96% | 21.21% | -8.53% | -21.15% | 5.73% | 12.69% | 34.29% | 62.50% | 1.33% | 7.61% | 28.61% |
| SOL-USD | SAME_ASSET_REGIME | 24 | 58.33% | 1.96% | 10.84% | 27.31% | -8.16% | -23.22% | 8.67% | 20.68% | 48.18% | 70.83% | 5.03% | 27.51% | 47.15% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 14 | 57.14% | 0.87% | 8.94% | 25.52% | -7.82% | -17.44% | 7.10% | 13.58% | 38.43% | 71.43% | 2.75% | 11.02% | 31.42% |

## Breakdown by historical BTC regime

| target   | group                   |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 6 | 100.00% | 17.45% | 0.00% | 46.51% | 33.33% | -1.25% | 59.23% |
| BTC-USD | HISTORICAL_BTC_BULL | 23 | 56.52% | 2.05% | -11.54% | 11.53% | 65.22% | 24.24% | 52.74% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 11 | 36.36% | -8.08% | -8.53% | 20.34% | 45.45% | -2.44% | 71.01% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 31 | 22.58% | -16.19% | -27.66% | 14.71% | 58.06% | 2.52% | 35.52% |
| DOGE-USD | HISTORICAL_BTC_BULL | 5 | 60.00% | 1.12% | -4.42% | 19.33% | 40.00% | -20.41% | 44.20% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 4 | 50.00% | -7.42% | -17.74% | 47.20% | 75.00% | 16.25% | 47.20% |
| SOL-USD | HISTORICAL_BTC_BEAR | 16 | 50.00% | 0.18% | -8.53% | 12.69% | 62.50% | 1.33% | 23.43% |
| SOL-USD | HISTORICAL_BTC_BULL | 11 | 36.36% | -9.88% | -15.76% | 9.62% | 54.55% | 1.96% | 25.37% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 13 | 53.85% | 4.38% | -8.08% | 25.06% | 61.54% | 23.83% | 99.95% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 19 | 89.47% | 10.53% | -8.08% | 25.93% | 73.68% | 26.74% | 66.84% |
| BTC-USD | HISTORICAL_ASSET_BULL | 11 | 27.27% | -16.88% | -20.68% | 6.28% | 45.45% | -5.26% | 25.00% |
| BTC-USD | HISTORICAL_ASSET_MIXED | 2 | 0.00% | -21.38% | -25.29% | 5.95% | 50.00% | -5.81% | 74.96% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 8 | 37.50% | -12.34% | -13.84% | 19.30% | 25.00% | -3.83% | 19.30% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 33 | 27.27% | -16.19% | -27.10% | 15.11% | 60.61% | 5.97% | 44.44% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 1 | 0.00% | -11.42% | -12.91% | 8.02% | 0.00% | -23.03% | 8.02% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 3 | 33.33% | -13.25% | -23.44% | 19.38% | 66.67% | 24.21% | 54.33% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 3 | 66.67% | 1.12% | -12.43% | 27.05% | 33.33% | -17.22% | 27.05% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 24 | 58.33% | 1.96% | -8.16% | 20.68% | 70.83% | 5.03% | 51.49% |
| SOL-USD | HISTORICAL_ASSET_BULL | 7 | 14.29% | -12.52% | -18.60% | 4.67% | 42.86% | -0.32% | 9.57% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 0.00% | -4.00% | -9.19% | 0.80% | 0.00% | -0.43% | 5.57% |
| SOL-USD | HISTORICAL_ASSET_MIXED | 2 | 50.00% | 4.99% | -4.53% | 20.78% | 100.00% | 34.99% | 85.23% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 6 | 50.00% | -3.56% | -7.11% | 20.76% | 33.33% | -10.93% | 39.22% |

## Top regime-adjusted matches

The table below shows the top matches separately for each target, so BTC does not hide SOL and DOGE.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | XRP-USD | 2019-10-04 | 87.10% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 29.37% | 0.00% | 33.33% | -1.77% | -2.34% | 58.05% |
| BTC-USD | LTC-USD | 2020-01-13 | 85.47% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 4.15% | 0.00% | 20.51% | 5.62% | 0.00% | 20.51% |
| BTC-USD | XLM-USD | 2019-10-09 | 85.01% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 47.44% | 0.00% | 59.63% | -34.58% | -37.78% | 59.63% |
| BTC-USD | XLM-USD | 2020-01-12 | 84.72% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 41.99% | 0.00% | 50.91% | 38.55% | 0.00% | 65.27% |
| BTC-USD | ETH-USD | 2025-12-11 | 84.40% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 5.52% | -7.64% | 12.79% | -1.70% | -7.64% | 12.79% |
| BTC-USD | EOS-USD | 2020-01-12 | 84.52% | BEAR | RECOVERY | SAME_BTC_ONLY | MIXED | 2.83% | -4.62% | 19.52% | -0.79% | -4.62% | 19.52% |
| BTC-USD | LRC-USD | 2018-09-24 | 90.61% | RECOVERY | BEAR | SAME_ASSET_ONLY | HIGH_SPIKE_60D | 30.68% | -8.53% | 146.68% | 36.85% | -8.53% | 146.68% |
| BTC-USD | FIL-USD | 2023-06-24 | 89.47% | BULL | BEAR | SAME_ASSET_ONLY | BULLISH_30D | 10.53% | -8.25% | 11.57% | 26.74% | -8.25% | 50.97% |
| BTC-USD | SAND-USD | 2023-06-24 | 89.19% | BULL | BEAR | SAME_ASSET_ONLY | MIXED | 7.39% | -12.66% | 11.30% | 26.71% | -12.66% | 37.05% |
| BTC-USD | EOS-USD | 2023-06-25 | 86.80% | BULL | BEAR | SAME_ASSET_ONLY | BULLISH_30D | 11.50% | -8.92% | 11.50% | 17.48% | -8.92% | 24.73% |
| DOGE-USD | VET-USD | 2022-03-04 | 88.88% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -20.06% | -21.27% | 0.00% | 18.68% | -22.08% | 18.68% |
| DOGE-USD | XRP-USD | 2019-09-29 | 88.76% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 25.26% | -7.50% | 25.26% | 10.19% | -7.50% | 51.15% |
| DOGE-USD | DASH-USD | 2022-02-25 | 88.59% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -24.48% | -29.01% | 2.36% | -17.05% | -31.84% | 2.36% |
| DOGE-USD | OP-USD | 2025-12-12 | 88.12% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 5.52% | -13.30% | 14.55% | 9.63% | -13.30% | 46.69% |
| DOGE-USD | OMG-USD | 2022-03-02 | 88.02% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -28.92% | -36.72% | 0.00% | -11.78% | -39.47% | 0.00% |
| DOGE-USD | INJ-USD | 2022-02-27 | 87.91% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -37.21% | -41.89% | 0.00% | -21.93% | -42.67% | 0.00% |
| DOGE-USD | QTUM-USD | 2022-03-02 | 87.79% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -22.26% | -33.72% | 0.00% | 6.79% | -33.72% | 19.77% |
| DOGE-USD | ENJ-USD | 2022-03-02 | 87.69% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -10.40% | -33.49% | 0.00% | 12.28% | -33.49% | 13.74% |
| DOGE-USD | DOT-USD | 2022-03-02 | 87.29% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -21.34% | -27.10% | 0.00% | 0.39% | -31.78% | 0.39% |
| DOGE-USD | 1INCH-USD | 2022-02-27 | 87.25% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -28.47% | -36.99% | 0.00% | -5.00% | -36.99% | 0.00% |
| SOL-USD | RUNE-USD | 2025-12-12 | 78.86% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 2.99% | -7.87% | 5.19% | 5.91% | -7.87% | 53.05% |
| SOL-USD | SOL-USD | 2025-12-09 | 78.76% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -1.32% | -12.34% | 1.82% | -5.43% | -12.34% | 8.09% |
| SOL-USD | APT-USD | 2024-09-11 | 77.67% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -23.26% | -23.26% | 3.72% | -33.02% | -33.49% | 3.72% |
| SOL-USD | LINK-USD | 2025-12-11 | 77.40% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -0.47% | -7.77% | 5.62% | 3.69% | -7.77% | 17.55% |
| SOL-USD | BTC-USD | 2025-12-12 | 77.17% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 10.42% | -4.01% | 12.25% | 12.73% | -4.01% | 19.54% |
| SOL-USD | NEAR-USD | 2025-12-11 | 76.96% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 0.92% | -11.77% | 8.98% | 21.58% | -11.77% | 23.26% |
| SOL-USD | DOT-USD | 2025-12-06 | 76.82% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -19.05% | -19.05% | 14.02% | -5.32% | -19.05% | 14.02% |
| SOL-USD | XLM-USD | 2020-01-12 | 76.75% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 41.99% | 0.00% | 50.91% | 38.55% | 0.00% | 65.27% |
| SOL-USD | CRV-USD | 2025-12-10 | 76.57% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -3.04% | -12.48% | 1.18% | 0.44% | -12.48% | 19.29% |
| SOL-USD | OMG-USD | 2025-12-11 | 76.32% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 5.97% | -5.71% | 8.37% | 4.15% | -5.71% | 17.41% |

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

Generato: 2026-07-18 05:14 UTC


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
| BTC | 63.889 $ | -2 | DEBOLE / NON CONFERMATO | STAGE 4 / MARKDOWN | MASSIMI E MINIMI CRESCENTI | ACCUMULO POSSIBILE / RANGE BASSO | BASSO | RIDUCI RISCHIO / NO LONG A LEVA |
| SOL | 74,93 $ | -9 | RIBASSISTA / FRAGILE | STAGE 4 / MARKDOWN | VOLATILITÀ IN ESPANSIONE | ACCUMULO POSSIBILE / RANGE BASSO | BASSO | NON INSEGUIRE / TAKE PROFIT SU SPIKE |
| DOGE | 0.07237 $ | -11 | RIBASSISTA / FRAGILE | STAGE 4 / MARKDOWN | MASSIMI E MINIMI DECRESCENTI | MARKDOWN / DEBOLEZZA | BASSO | NO LONG / SHORT SOLO DOPO SPIKE E REJECTION |

## Punteggi per area

| Asset | Trend | Struttura | Momentum | Volume | Prezzo | Candela | Wyckoff | Totale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | -4 | +2 | +1 | -1 | 0 | 0 | 0 | -2 |
| SOL | -4 | 0 | -3 | -1 | 0 | -1 | 0 | -9 |
| DOGE | -4 | -2 | -1 | -2 | 0 | 0 | -2 | -11 |

## Livelli tecnici

| Asset | Supporto | Resistenza | Breakout 60g | Breakdown 60g | ATR14 | Rendimento 30g | Rendimento 90g |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 63.062 $ | 64.186 $ | 82.006 $ | 57.748 $ | 2,52% | -0,83% | -15,64% |
| SOL | 74,16 $ | 75,94 $ | 93,58 $ | 60,41 $ | 3,32% | 4,18% | -13,07% |
| DOGE | 0.07206 $ | 0.07546 $ | 0.11825 $ | 0.06961 $ | 3,34% | -15,65% | -23,74% |

## Lettura dettagliata

### BTC

- Prezzo: **63.889 $**
- Score classico: **-2 / 12**
- Verdetto: **DEBOLE / NON CONFERMATO**
- Azione coerente: **RIDUCI RISCHIO / NO LONG A LEVA**
- Volatilità tecnica locale: **BASSO** — ATR14 2,52%; distanza supporto 1,30%; distanza resistenza 0,47%

Dettaglio:

- Trend: **-4** — prezzo sotto MA200 daily; MA50 daily in discesa; MA200 daily in discesa; STAGE 4 / MARKDOWN
- Stage weekly: **STAGE 4 / MARKDOWN** — Prezzo sotto MA30 weekly con MA30 in discesa.
- Struttura: **+2** — MASSIMI E MINIMI CRESCENTI
- Momentum: **+1** — RSI sano 51.7; MACD sopra signal; istogramma MACD in peggioramento
- Volume: **-1** — OBV sotto media; CMF neutrale 0.05; volume ratio 0.91
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **0** — Doji / indecisione
- Wyckoff: **0** — ACCUMULO POSSIBILE / RANGE BASSO. Prezzo nella metà bassa del range, ma senza spring confermato.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 51.68 |
| MACD histogram | 340.56610 |
| CMF20 | 0.050 |
| Volume ratio 20 | 0.91 |
| MA20 | 62.646 $ |
| MA50 | 63.708 $ |
| MA100 | 70.441 $ |
| MA200 | 73.277 $ |
| Pendenza MA50 20g | -8,76% |
| Pendenza MA200 60g | -10,02% |
| Bollinger width | 11,32% |
| Bollinger position | 0.67 |

### SOL

- Prezzo: **74,93 $**
- Score classico: **-9 / 12**
- Verdetto: **RIBASSISTA / FRAGILE**
- Azione coerente: **NON INSEGUIRE / TAKE PROFIT SU SPIKE**
- Volatilità tecnica locale: **BASSO** — ATR14 3,32%; distanza supporto 1,05%; distanza resistenza 1,33%

Dettaglio:

- Trend: **-4** — prezzo sotto MA200 daily; MA50 daily in discesa; MA200 daily in discesa; STAGE 4 / MARKDOWN
- Stage weekly: **STAGE 4 / MARKDOWN** — Prezzo sotto MA30 weekly con MA30 in discesa.
- Struttura: **0** — VOLATILITÀ IN ESPANSIONE
- Momentum: **-3** — RSI neutrale 46.6; RSI in peggioramento; MACD sotto signal; istogramma MACD in peggioramento
- Volume: **-1** — OBV sotto media; CMF neutrale 0.00; volume ratio 0.63
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **-1** — Shooting star / rejection alto
- Wyckoff: **0** — ACCUMULO POSSIBILE / RANGE BASSO. Prezzo nella metà bassa del range, ma senza spring confermato.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 46.63 |
| MACD histogram | -0.51809 |
| CMF20 | 0.000 |
| Volume ratio 20 | 0.63 |
| MA20 | 77,67 $ |
| MA50 | 73,60 $ |
| MA100 | 80,04 $ |
| MA200 | 90,57 $ |
| Pendenza MA50 20g | -5,22% |
| Pendenza MA200 60g | -17,50% |
| Bollinger width | 16,20% |
| Bollinger position | 0.27 |

### DOGE

- Prezzo: **0.07237 $**
- Score classico: **-11 / 12**
- Verdetto: **RIBASSISTA / FRAGILE**
- Azione coerente: **NO LONG / SHORT SOLO DOPO SPIKE E REJECTION**
- Volatilità tecnica locale: **BASSO** — ATR14 3,34%; distanza supporto 0,43%; distanza resistenza 4,28%

Dettaglio:

- Trend: **-4** — prezzo sotto MA200 daily; medie daily allineate ribassiste; MA50 daily in discesa; MA200 daily in discesa; STAGE 4 / MARKDOWN
- Stage weekly: **STAGE 4 / MARKDOWN** — Prezzo sotto MA30 weekly con MA30 in discesa.
- Struttura: **-2** — MASSIMI E MINIMI DECRESCENTI
- Momentum: **-1** — RSI debole 37.7; MACD sopra signal; istogramma MACD in peggioramento
- Volume: **-2** — OBV sotto media; CMF negativo -0.07; volume ratio 0.77
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **-2** — MARKDOWN / DEBOLEZZA. Prezzo basso nel range e sotto medie principali.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 37.66 |
| MACD histogram | 0.00044 |
| CMF20 | -0.071 |
| Volume ratio 20 | 0.77 |
| MA20 | 0.07392 $ |
| MA50 | 0.08119 $ |
| MA100 | 0.09195 $ |
| MA200 | 0.09975 $ |
| Pendenza MA50 20g | -13,81% |
| Pendenza MA200 60g | -16,12% |
| Bollinger width | 10,68% |
| Bollinger position | 0.30 |

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

Generato: 2026-07-18 05:14 UTC


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
| BTC | 63.889 $ | Doppio minimo | CANDIDATO | rialzista | n/a | 76.748 $ | n/a | 5,26% | Fib 23,6% TESTATO (0) @ 63.658 $ | NEL RANGE | 62.553 $ |
| SOL | 74,93 $ | Doppio minimo | MATURO | rialzista | 2026-07-01 | 91,46 $ | -6,50% | n/a | Fib 23,6% REJECTION (0) @ 79,85 $ | NEL RANGE | 74,16 $ |
| DOGE | 0.07237 $ | Triplo massimo | MATURO | ribassista | 2026-06-24 | 0.05847 $ | 29,17% | n/a | Fib 23,6% NON ATTIVO (0) @ 0.08213 $ | NEL RANGE | 0.07107 $ |

## BTC

![Classic visual BTC](classic_visual_BTC.png)

- Pattern principale: **Doppio minimo**
- Stato pattern: **CANDIDATO** (0)
- Famiglia: **rialzista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-06-05 -> 2026-07-01**
- Età formazione: **17 giorni**
- Breakout pattern: **n/a**
- Età breakout: **n/a**
- Neckline: **67.248 $**
- Target teorico: **76.748 $**
- Progresso verso target: **n/a**
- Distanza dalla neckline: **5,26%**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 23,6% TESTATO (0) @ 63.658 $** — Swing DOWN 2026-05-06 82.792 -> 2026-07-01 57.748; livello più vicino 23.6% a 63.658; stato TESTATO; confluenza: nessuna confluenza indipendente.
- Invalidazione: **65.903 $**
- Relazione prezzo/neckline: **sotto neckline**
- Dettaglio: Due minimi simili vicino a 57.748 tra 2026-06-05 e 2026-07-01. Neckline stimata: 67.248. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 17 giorni. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Doji / indecisione**
- Stato prezzo: **NEL RANGE**
- Supporto: **62.553 $**
- Resistenza: **65.544 $**
- Breakout 60g: **82.006 $**
- Breakdown 60g: **57.748 $**
- RSI14: **51.70**
- ATR14: **2,52%**
- Volume ratio 20g: **0.91**
- Rendimento 30g: **-0,82%**
- Rendimento 90g: **-15,63%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Doppio minimo | CANDIDATO | 0 | rialzista | 67.248 $ | n/a | n/a | 76.748 $ | n/a | 5,26% | 65.903 $ | Due minimi simili a 59.109 $ e 57.748 $. Neckline circa 67.248 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 17 giorni. |
| Triangolo discendente possibile | CANDIDATO | 0 | ribassista | n/a | n/a | n/a | n/a | n/a | n/a | n/a | Massimi decrescenti e supporto quasi piatto. Stato: CANDIDATO; il pattern non ha una neckline univoca da usare per il lifecycle. |
| Doppio massimo | TARGET RAGGIUNTO | 0 | ribassista | 74.959 $ | 2026-05-27 | 52g | 71.596 $ | 329,24% | n/a | 76.458 $ | Due massimi simili a 78.321 $ e 77.991 $. Neckline circa 74.959 $. Breakout neckline: 2026-05-27 (52 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 71.596 $; progresso: 329,24%; prezzo sotto neckline. |

## SOL

![Classic visual SOL](classic_visual_SOL.png)

- Pattern principale: **Doppio minimo**
- Stato pattern: **MATURO** (+1)
- Famiglia: **rialzista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-06-06 -> 2026-06-25**
- Età formazione: **23 giorni**
- Breakout pattern: **2026-07-01**
- Età breakout: **17 giorni**
- Neckline: **75,94 $**
- Target teorico: **91,46 $**
- Progresso verso target: **-6,50%**
- Distanza dalla neckline: **n/a**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 23,6% REJECTION (0) @ 79,85 $** — Swing DOWN 2026-05-11 98,27 -> 2026-07-13 74,16; livello più vicino 23.6% a 79,85; stato REJECTION; confluenza: nessuna confluenza indipendente.
- Invalidazione: **74,42 $**
- Relazione prezzo/neckline: **sotto neckline**
- Dettaglio: Due minimi simili vicino a 60,41 tra 2026-06-06 e 2026-06-25. Neckline stimata: 75,94. Breakout neckline: 2026-07-01 (17 giorni fa). Stato: MATURO. Target teorico: 91,46; progresso corrente: -6,50%. Relazione prezzo/neckline: sotto neckline. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Shooting star / rejection alto**
- Stato prezzo: **NEL RANGE**
- Supporto: **74,16 $**
- Resistenza: **75,94 $**
- Breakout 60g: **93,58 $**
- Breakdown 60g: **60,41 $**
- RSI14: **46.60**
- ATR14: **3,33%**
- Volume ratio 20g: **0.63**
- Rendimento 30g: **+4,17%**
- Rendimento 90g: **-13,08%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Doppio minimo | MATURO | +1 | rialzista | 75,94 $ | 2026-07-01 | 17g | 91,46 $ | -6,50% | n/a | 74,42 $ | Due minimi simili vicino a 60,41 tra 2026-06-06 e 2026-06-25. Neckline stimata: 75,94. Breakout neckline: 2026-07-01 (17 giorni fa). Stato: MATURO. Target teorico: 91,46; progresso corrente: -6,50%. Relazione prezzo/neckline: sotto neckline. Fonte lifecycle: technical_structure_metrics.csv. |
| Doppio massimo | CANDIDATO | 0 | ribassista | 60,41 $ | n/a | n/a | 33,04 $ | n/a | 24,03% | 61,62 $ | Due massimi simili a 87,79 $ e 83,81 $. Neckline circa 60,41 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 14 giorni. |
| Doppio minimo | CANDIDATO | 0 | rialzista | 98,27 $ | n/a | n/a | 114,91 $ | n/a | 31,14% | 96,30 $ | Due minimi simili a 81,63 $ e 81,69 $. Neckline circa 98,27 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 56 giorni. |
| Testa e spalle | TARGET RAGGIUNTO | 0 | ribassista | 82,57 $ | 2026-05-28 | 51g | 66,88 $ | 48,69% | n/a | 84,22 $ | Spalla sinistra 88,05 $, testa 98,27 $, spalla destra 87,79 $. Neckline circa 82,57 $. Breakout neckline: 2026-05-28 (51 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 66,88 $; progresso: 48,69%; prezzo sotto neckline. |

## DOGE

![Classic visual DOGE](classic_visual_DOGE.png)

- Pattern principale: **Triplo massimo**
- Stato pattern: **MATURO** (-1)
- Famiglia: **ribassista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-03-25 -> 2026-06-12**
- Età formazione: **36 giorni**
- Breakout pattern: **2026-06-24**
- Età breakout: **24 giorni**
- Neckline: **0.07809 $**
- Target teorico: **0.05847 $**
- Progresso verso target: **29,17%**
- Distanza dalla neckline: **n/a**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 23,6% NON ATTIVO (0) @ 0.08213 $** — Swing DOWN 2026-05-14 0.11825 -> 2026-07-13 0.07097; livello più vicino 23.6% a 0.08213; stato NON ATTIVO; confluenza: nessuna confluenza indipendente.
- Invalidazione: **0.07966 $**
- Relazione prezzo/neckline: **sotto neckline**
- Dettaglio: Tre massimi simili vicino a 0.09772 dal 2026-03-25 al 2026-06-12. Neckline ribassista stimata: 0.07809. Breakout neckline: 2026-06-24 (24 giorni fa). Stato: MATURO. Target teorico: 0.05847; progresso corrente: 29,17%. Relazione prezzo/neckline: sotto neckline. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **NEL RANGE**
- Supporto: **0.07107 $**
- Resistenza: **0.07923 $**
- Breakout 60g: **0.11825 $**
- Breakdown 60g: **0.06961 $**
- RSI14: **37.66**
- ATR14: **3,34%**
- Volume ratio 20g: **0.77**
- Rendimento 30g: **-15,65%**
- Rendimento 90g: **-23,74%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Triplo massimo | MATURO | -1 | ribassista | 0.07809 $ | 2026-06-24 | 24g | 0.05847 $ | 29,17% | n/a | 0.07966 $ | Tre massimi simili vicino a 0.09772 dal 2026-03-25 al 2026-06-12. Neckline ribassista stimata: 0.07809. Breakout neckline: 2026-06-24 (24 giorni fa). Stato: MATURO. Target teorico: 0.05847; progresso corrente: 29,17%. Relazione prezzo/neckline: sotto neckline. Fonte lifecycle: technical_structure_metrics.csv. |
| Doppio massimo | MATURO | -1 | ribassista | 0.07809 $ | 2026-06-24 | 24g | 0.06035 $ | 32,27% | n/a | 0.07966 $ | Due massimi simili a 0.09584 $ e 0.09169 $. Neckline circa 0.07809 $. Breakout neckline: 2026-06-24 (24 giorni fa). Stato: MATURO. Target teorico: 0.06035 $; progresso: 32,27%; prezzo sotto neckline. |
| Doppio minimo | CANDIDATO | 0 | rialzista | 0.07923 $ | n/a | n/a | 0.08886 $ | n/a | 9,48% | 0.07765 $ | Due minimi simili a 0.06961 $ e 0.07097 $. Neckline circa 0.07923 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 5 giorni. |
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

Generato: 2026-07-18 05:14 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [fractal_path_tracker.md](fractal_path_tracker.md)

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-07-18**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-01-02**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **74,93 $**
- Verdetto principale: **ANALOGIA DEBOLE / SCENARIO SECONDARIO**
- Somiglianza strutturale: **+64,35%**
- Aderenza live principale: **+62,62%**
- Errore medio live principale: **18,69%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE SOLO DI CONTESTO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **42**
- Osservazioni inclusive dal bottom: **43**
- Osservazioni da inizio programma/scanner: **16**
- Errore assoluto medio dal bottom: **10,74%**
- Errore assoluto medio da inizio programma: **18,69%**
- Gap firmato medio ultimi 7 giorni: **+16,10%**
- Errore assoluto medio ultimi 7 giorni: **16,10%**
- Gap ultimo giorno: **+13,98%**
- Stato aderenza: **STACCATO / MOLTO IN ANTICIPO**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **+13,98%**
- Gap firmato medio 7g: **+16,10%**
- Errore assoluto medio 7g: **16,10%**
- Variazione recente gap: **-4,16%**
- Stato gap: **IN DEVIAZIONE SOPRA IL FRATTALE**
- Trend gap: **SOL resta sopra il percorso ancorato, ma sta riducendo il distacco**

Soglie operative del grafico:

- entro **±5%**: percorso vicino;
- tra **±5% e ±12%**: deviazione gestibile;
- oltre **±12%**: frattale non abbastanza aderente per conferma operativa;
- oltre **±18%**: disallineamento marcato.

## Ultimi giorni del confronto ancorato

|   Giorno | Data SOL   | Data BTC eq.   | SOL reale   | Percorso ancorato   | Gap firmato   | Fase                |
|---------:|:-----------|:---------------|:------------|:--------------------|:--------------|:--------------------|
| 33 | 2026-07-09 | 2022-12-24 | 78,05 $ | 66,37 $ | +17,60% | da inizio programma |
| 34 | 2026-07-10 | 2022-12-25 | 78,07 $ | 66,34 $ | +17,67% | da inizio programma |
| 35 | 2026-07-11 | 2022-12-26 | 76,82 $ | 66,65 $ | +15,26% | da inizio programma |
| 36 | 2026-07-12 | 2022-12-27 | 76,87 $ | 65,85 $ | +16,74% | da inizio programma |
| 37 | 2026-07-13 | 2022-12-28 | 74,86 $ | 65,20 $ | +14,81% | da inizio programma |
| 38 | 2026-07-14 | 2022-12-29 | 77,76 $ | 65,56 $ | +18,62% | da inizio programma |
| 39 | 2026-07-15 | 2022-12-30 | 77,26 $ | 65,40 $ | +18,14% | da inizio programma |
| 40 | 2026-07-16 | 2022-12-31 | 75,27 $ | 65,18 $ | +15,48% | da inizio programma |
| 41 | 2026-07-17 | 2023-01-01 | 75,27 $ | 65,49 $ | +14,94% | da inizio programma |
| 42 | 2026-07-18 | 2023-01-02 | 74,93 $ | 65,74 $ | +13,98% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-07-25 | 67,74 $ | 77,21 $ | 74,89 $ / 77,21 $ | no | n/a | n/a | n/a |
| 14g | 2026-08-01 | 83,39 $ | 95,05 $ | 74,89 $ / 95,05 $ | no | n/a | n/a | n/a |
| 21g | 2026-08-08 | 90,34 $ | 102,97 $ | 74,89 $ / 102,97 $ | no | n/a | n/a | n/a |
| 28g | 2026-08-15 | 89,97 $ | 102,55 $ | 74,89 $ / 106,75 $ | no | n/a | n/a | n/a |
| 35g | 2026-08-22 | 89,66 $ | 102,19 $ | 74,89 $ / 106,75 $ | no | n/a | n/a | n/a |
| 42g | 2026-08-29 | 85,91 $ | 97,92 $ | 74,89 $ / 106,75 $ | no | n/a | n/a | n/a |
| 49g | 2026-09-05 | 97,81 $ | 111,48 $ | 74,89 $ / 111,48 $ | no | n/a | n/a | n/a |
| 56g | 2026-09-12 | 92,66 $ | 105,62 $ | 74,89 $ / 111,48 $ | no | n/a | n/a | n/a |
| 63g | 2026-09-19 | 88,36 $ | 100,71 $ | 74,89 $ / 111,48 $ | no | n/a | n/a | n/a |
| 70g | 2026-09-26 | 95,32 $ | 108,65 $ | 74,89 $ / 111,48 $ | no | n/a | n/a | n/a |
| 77g | 2026-10-03 | 109,38 $ | 124,67 $ | 74,89 $ / 125,89 $ | no | n/a | n/a | n/a |
| 84g | 2026-10-10 | 106,91 $ | 121,86 $ | 74,89 $ / 127,22 $ | no | n/a | n/a | n/a |
| 91g | 2026-10-17 | 109,47 $ | 124,78 $ | 74,89 $ / 127,87 $ | no | n/a | n/a | n/a |
| 98g | 2026-10-24 | 116,81 $ | 133,14 $ | 74,89 $ / 133,14 $ | no | n/a | n/a | n/a |
| 105g | 2026-10-31 | 115,99 $ | 132,21 $ | 74,89 $ / 136,88 $ | no | n/a | n/a | n/a |
| 112g | 2026-11-07 | 108,43 $ | 123,59 $ | 74,89 $ / 136,88 $ | no | n/a | n/a | n/a |
| 119g | 2026-11-14 | 110,66 $ | 126,13 $ | 74,89 $ / 136,88 $ | no | n/a | n/a | n/a |
| 126g | 2026-11-21 | 109,09 $ | 124,35 $ | 74,89 $ / 136,88 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 4 | 0,00% | 2,06% | 14,46% |
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

Ultima lettura salvata: **2026-07-18** — SOL 74,93 $, gap +13,98%, somiglianza +64,35%.

Nel report principale lascio solo il link, così non diventa troppo lungo.

<!-- SOL_BTC_FRACTAL_HISTORY_END -->

</details>
<!-- COMPACT_SECTION_END:fractal_path -->

<!-- COMPACT_SECTION_START:exchange_microstructure -->
<details>
<summary><strong>🏦 Dati exchange, liquidità e leva</strong></summary>

<!-- EXCHANGE_MICROSTRUCTURE_START -->
# Dati exchange, liquidità e leva

Generato: 2026-07-18 05:14 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [exchange_microstructure_report.md](exchange_microstructure_report.md)

Questo modulo legge Kraken Futures, Bitget Futures e KuCoin Futures come nucleo derivati. OKX e Coinbase vengono raccolti come fonti ausiliarie non pesate.
Non modifica la formula matematica di RSI, Fibonacci o Wyckoff: controlla se quei segnali sono sostenuti da acquisti, vendite, OI, funding e liquidità.

**Limite importante:** questo nucleo non assume disponibile un feed pubblico completo delle liquidazioni. La componente liquidazioni resta neutrale; le zone future restano stime di pressione, non dati certi delle singole posizioni.

Diagnostica completa: [exchange_source_diagnostics.md](exchange_source_diagnostics.md)

## Sintesi

| Asset | Prezzo | Exchange | Segnale candidato | Peso Global | Bias exchange | Confidenza | Copertura | Funding 8h eq. | OI 24h | Taker flow (campione/4h) | Book 0,5% | Liq long campione | Liq short campione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 63.945 $ | 3 | 0 | 0 | LEGGERMENTE POSITIVA / NON PESATA | BASSA | 100% | +0,0065% | n/a | 1,30 | -2,32% | 0 $ | 0 $ |
| SOL | 75,06 $ | 3 | 0 | 0 | MISTA / NEUTRALE | BASSA | 100% | +0,0020% | n/a | 1,06 | -3,22% | 0 $ | 0 $ |
| DOGE | 0.07244 $ | 3 | 0 | 0 | LEGGERMENTE NEGATIVA / NON PESATA | BASSA | 100% | +0,0050% | n/a | 0,60 | -7,49% | 0 $ | 0 $ |

Il segnale candidato è limitato a **±1**, ma il peso nel Global resta **0** finché il tracker a 7 giorni non raggiunge 30 controlli, almeno 55% di accuratezza e return corretto direzione positivo. Un singolo muro o funding non basta.

La colonna taker usa un campione recente nel primo run. Dopo almeno 3 fotografie distribuite su almeno 45 minuti viene sostituita automaticamente dalla media intraday 4h.

## Dati separati per exchange

| Asset | Exchange | Stato | Funding 8h eq. | Open interest | Taker flow | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | Kraken | OK | +0,0047% | 121,64 mln $ | 1,30 | +7,64% |
| BTC | Bitget | OK | +0,0033% | 2,18 mld $ | 2,42 | -55,67% |
| BTC | Kucoin | OK | +0,0100% | 2,01 mld $ | 1,16 | -7,08% |
| SOL | Kraken | OK | -0,0038% | 17,06 mln $ | 4,65 | -4,63% |
| SOL | Bitget | OK | +0,0040% | 371,86 mln $ | 0,09 | -8,60% |
| SOL | Kucoin | OK | -0,0004% | 270,58 mln $ | 1,06 | +5,74% |
| DOGE | Kraken | OK | +0,0050% | 2,90 mln $ | 0,15 | -12,52% |
| DOGE | Bitget | OK | +0,0039% | 77,19 mln $ | 0,60 | -8,43% |
| DOGE | Kucoin | OK | +0,0058% | 116,58 mln $ | 1,38 | +0,80% |

Kraken, Bitget e KuCoin contribuiscono a funding normalizzato, open interest, trade aggressivi e order book. Non viene inventato un long/short ratio pubblico né un feed completo delle liquidazioni.

## Conferme per indicatori tecnici

### BTC

- Score grezzo exchange: **+1,38**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 0, accuratezza n/a.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 1, bear 1, divergenze 0.
- Flusso taker/order book: **+1,00**.
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

- Score grezzo exchange: **+0,00**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 0, accuratezza n/a.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 1, bear 0, divergenze 1.
- Flusso taker/order book: **+0,00**.
- OI/funding/basis: **+0,00**.
- Affollamento long/short: **+0,00**.
- Liquidazioni: **NON PESATE / FEED COMPLETO NON ASSUNTO DISPONIBILE**.
- **Wyckoff:** Fase Wyckoff debole ma senza conferma exchange netta.
- **Fibonacci:** Fibonacci rejection; nessuna conferma exchange netta.
- **RSI:** RSI in zona non estrema o flusso exchange non abbastanza netto.
- **Pattern:** I pattern candidati restano non operativi: i dati exchange possono solo preparare la conferma.
- **Breakout/breakdown:** Prezzo non abbastanza vicino a un livello chiave o flusso non netto.
- **Mappa liquidità attuale:** muro bid: n/a; muro ask: n/a

![Microstruttura exchange SOL](exchange_microstructure_SOL.png)

### DOGE

- Score grezzo exchange: **-1,50**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 0, accuratezza n/a.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 0, bear 2, divergenze 0.
- Flusso taker/order book: **-1,00**.
- OI/funding/basis: **+0,00**.
- Affollamento long/short: **+0,00**.
- Liquidazioni: **NON PESATE / FEED COMPLETO NON ASSUNTO DISPONIBILE**.
- **Wyckoff:** Possibile accumulazione non confermata: il flusso aggressivo resta venditore.
- **Fibonacci:** Fibonacci non_attivo; nessuna conferma exchange netta.
- **RSI:** RSI in zona non estrema o flusso exchange non abbastanza netto.
- **Pattern:** Triplo massimo maturo sostenuto dal flusso exchange.
- **Breakout/breakdown:** Prezzo non abbastanza vicino a un livello chiave o flusso non netto.
- **Mappa liquidità attuale:** muro bid: n/a; muro ask: n/a

![Microstruttura exchange DOGE](exchange_microstructure_DOGE.png)

## Overlay sulle previsioni a 30 giorni

La previsione storica grezza dello scanner resta intatta. L'overlay exchange può correggerla solo dopo almeno 30 controlli maturati a 30 giorni e solo se il modulo dimostra accuratezza direzionale almeno del 55%.

| Asset | Prob. grezza salita | Return p50 grezzo | Controlli 30g | Accuratezza exchange | Stato overlay | Peso | Prob. corretta | Return corretto |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +57,50% | +3,00% | 0 | n/a | RACCOLTA DATI | 0,00 | +57,50% | +3,00% |
| SOL | +47,50% | -0,89% | 0 | n/a | RACCOLTA DATI | 0,00 | +47,50% | -0,89% |
| DOGE | +30,00% | -14,61% | 0 | n/a | RACCOLTA DATI | 0,00 | +30,00% | -14,61% |

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

Generato: 2026-07-18 05:14 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [exchange_signal_tracker_report.md](exchange_signal_tracker_report.md)

Questo tracker verifica se il segnale candidato exchange ±1 anticipa correttamente la direzione del prezzo a 1/3/7/14/30 giorni.
Il peso Global resta 0 finché l'orizzonte 7g non ha almeno 30 controlli, accuratezza almeno 55% e return corretto direzione positivo. L'overlay a 30g ha un gate separato.

Controlli maturati completati in questa esecuzione: **9**.

## Ultime fotografie giornaliere

| Data | Asset | Prezzo | Versione | Calibrazione | Candidato | Peso Global | Score raw | Confidenza | Taker 4h | OI 24h | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-07-18 | BTC | 63.944,60 | V2.1.3 | OK | 0 | 0 | 1,38 | BASSA | 1,30 | n/a | -2,32% |
| 2026-07-18 | DOGE | 0.07244 | V2.1.3 | OK | 0 | 0 | -1,50 | BASSA | 0,60 | n/a | -7,49% |
| 2026-07-18 | SOL | 75,06 | V2.1.3 | OK | 0 | 0 | 0,00 | BASSA | 1,06 | n/a | -3,22% |
| 2026-07-17 | BTC | 63.769,90 | V2.1.3 | OK | 0 | 0 | 1,38 | MEDIA | 1,79 | n/a | -1,25% |
| 2026-07-17 | DOGE | 0.07233 | V2.1.3 | OK | 0 | 0 | -1,75 | MEDIA | 0,77 | n/a | -2,14% |
| 2026-07-17 | SOL | 75,27 | V2.1.3 | OK | 0 | 0 | 0,00 | BASSA | 0,96 | n/a | +1,46% |
| 2026-07-16 | BTC | 64.090,10 | V2.1.3 | OK | 0 | 0 | 1,38 | BASSA | 1,64 | n/a | +3,10% |
| 2026-07-16 | DOGE | 0.07308 | V2.1.3 | OK | 0 | 0 | 1,38 | BASSA | 1,25 | n/a | +2,57% |
| 2026-07-16 | SOL | 76,09 | V2.1.3 | OK | 0 | 0 | 1,75 | BASSA | 1,99 | n/a | +4,06% |

## Accuratezza direzionale

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
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

**BTC** — BTC: i futures sembrano più vulnerabili verso una discesa improvvisa. Non significa che deve scendere, ma se rompe sotto può accelerare. Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale.

**SOL** — SOL: i futures non danno una lettura chiara. Non si vede uno sbilanciamento forte né long né short. Qui pesa di più il report frattale.

**DOGE** — DOGE: i futures sembrano più vulnerabili verso una discesa improvvisa. Non significa che deve scendere, ma se rompe sotto può accelerare. Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale.

| Asset | Prezzo | Funding | OI 24h | Long/Short | Lettura futures | Forza |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 63.889 $ | +0.0062% | +2.22% | 1.65 | Rischio sotto | 4/5 |
| SOL | 74,93 $ | +0.0018% | -14.19% | 2.38 | Misto | 1/5 |
| DOGE | 0.07237 $ | +0.0100% | +1.97% | 4.40 | Rischio sotto | 2/5 |

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

Generato: 2026-07-18 05:14 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [rsi_multitimeframe_divergence_report.md](rsi_multitimeframe_divergence_report.md)

Il modulo confronta prezzo e RSI 14 sui pivot confermati **daily e weekly**. Riconosce divergenze regolari e nascoste, segnali in formazione, invalidazioni e semplice conferma del momentum.

**Peso operativo: 0.** Non modifica il Global Confluence, non cambia le soglie del Paper Trading e non apre né blocca operazioni. I risultati vengono misurati prima di qualsiasi futura decisione sul peso.

## Sintesi corrente

| Asset   | Daily               | Stato D    | Weekly                    | Stato W    | Lettura weekly                                                                                                                |   Peso |
|:--------|:--------------------|:-----------|:--------------------------|:-----------|:------------------------------------------------------------------------------------------------------------------------------|-------:|
| BTC     | Bullish regolare    | CONFERMATA | Bullish regolare          | CONFERMATA | Bullish regolare confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto. |      0 |
| SOL     | Conferma ribassista | CONTESTO   | Hidden bearish            | CONFERMATA | Hidden bearish confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto.   |      0 |
| DOGE    | Hidden bearish      | CONFERMATA | Hidden bullish invalidata | INVALIDATA | La precedente hidden bullish non è più sostenuta dalla relazione corrente tra pivot di prezzo e RSI.                          |      0 |

## Dettaglio dei pivot

| Asset   | TF   | Tipo                      | Stato      | Prezzo / RSI      | Pivot confrontati                                                   | Δ prezzo contesto   | Δ RSI contesto   |   Peso |
|:--------|:-----|:--------------------------|:-----------|:------------------|:--------------------------------------------------------------------|:--------------------|:-----------------|-------:|
| BTC     | 1D   | Bullish regolare          | CONFERMATA | 63.884 $ / 51,68  | 2026-06-25 58.076 $ / RSI 30,46 → 2026-07-01 57.748 $ / RSI 37,26   | n/a                 | n/a              |      0 |
| BTC     | 1W   | Bullish regolare          | CONFERMATA | 63.884 $ / 38,65  | 2026-06-07 59.109 $ / RSI 34,23 → 2026-07-05 57.748 $ / RSI 38,20   | n/a                 | n/a              |      0 |
| SOL     | 1D   | Conferma ribassista       | CONTESTO   | 74,93 $ / 46,60   | n/a                                                                 | -8,93%              | -19,12           |      0 |
| SOL     | 1W   | Hidden bearish            | CONFERMATA | 74,93 $ / 39,17   | 2026-05-17 98,27 $ / RSI 38,29 → 2026-07-05 83,81 $ / RSI 42,25     | n/a                 | n/a              |      0 |
| DOGE    | 1D   | Hidden bearish            | CONFERMATA | 0.07237 $ / 37,66 | 2026-06-12 0.09169 $ / RSI 35,18 → 2026-07-04 0.07923 $ / RSI 41,65 | n/a                 | n/a              |      0 |
| DOGE    | 1W   | Hidden bullish invalidata | INVALIDATA | 0.07237 $ / 33,29 | n/a                                                                 | -15,94%             | -2,50            |      0 |

### BTC

- **1D — Bullish regolare / CONFERMATA**: Bullish regolare confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto.
- **1W — Bullish regolare / CONFERMATA**: Bullish regolare confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto.

### SOL

- **1D — Conferma ribassista / CONTESTO**: Prezzo e RSI stanno scendendo insieme: momentum ribassista confermato, nessuna bullish divergence attiva.
- **1W — Hidden bearish / CONFERMATA**: Hidden bearish confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto.

### DOGE

- **1D — Hidden bearish / CONFERMATA**: Hidden bearish confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto.
- **1W — Hidden bullish invalidata / INVALIDATA**: La precedente hidden bullish non è più sostenuta dalla relazione corrente tra pivot di prezzo e RSI.

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

Generato: 2026-07-18 05:14 UTC


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

| Asset   | Prezzo   |   Punteggio | Verdetto         | Trend            | Momentum                  | Struttura                                             |   Pattern score | Fibonacci      | Pattern rialzista         | Pattern ribassista                | Supporto   | Resistenza   |
|:--------|:---------|------------:|:-----------------|:-----------------|:--------------------------|:------------------------------------------------------|----------------:|:---------------|:--------------------------|:----------------------------------|:-----------|:-------------|
| BTC | 63.889 $ | -1 | NEUTRALE / MISTO | Trend misto | Momentum misto | Struttura ribassista con massimi e minimi decrescenti | 0 | 0 / TESTATO | Doppio minimo / CANDIDATO | Doppio massimo / TARGET RAGGIUNTO | 57.748 | 65.544 |
| SOL | 74,93 $ | -6 | DEBOLE | Trend ribassista | Momentum debole | Struttura rialzista con massimi e minimi crescenti | +1 | 0 / REJECTION | Doppio minimo / MATURO | Doppio massimo / CANDIDATO | 74,16 | 83,81 |
| DOGE | 0.07237 $ | -6 | DEBOLE | Trend ribassista | Momentum in miglioramento | Struttura ribassista con massimi e minimi decrescenti | -1 | 0 / NON ATTIVO | Doppio minimo / CANDIDATO | Triplo massimo / MATURO | 0.07097 | 0.07923 |

## Riepilogo ciclo di vita pattern

| Asset   | Doppio minimo   | Triplo minimo   | Adam/Eve Bottom                 | Doppio massimo   | Triplo massimo   | Adam/Eve Top                        |   Punteggio pattern |
|:--------|:----------------|:----------------|:--------------------------------|:-----------------|:-----------------|:------------------------------------|--------------------:|
| BTC | CANDIDATO | CANDIDATO | Adam and Eve Bottom — CANDIDATO | TARGET RAGGIUNTO | TARGET RAGGIUNTO | Eve and Adam Top — TARGET RAGGIUNTO | 0 |
| SOL | MATURO | CANDIDATO | Adam and Eve Bottom — MATURO | CANDIDATO | CANDIDATO | Eve and Adam Top — CANDIDATO | 1 |
| DOGE | CANDIDATO | ASSENTE | Adam and Eve Bottom — CANDIDATO | ASSENTE | MATURO | Eve and Adam Top — MATURO | -1 |

## Indicatori tecnici

| Asset   |   RSI 14 |   Istogramma MACD | MA20    | MA50    | MA200   | Pendenza MA50 20g   | Pendenza MA200 60g   | Rendimento 30g   | Rendimento 90g   |
|:--------|---------:|------------------:|:--------|:--------|:--------|:--------------------|:---------------------|:-----------------|:-----------------|
| BTC | 51.7 | 340.907 | 62.646 | 63.709 | 73.277 | -8,21% | -9,83% | 1,58% | -13,50% |
| SOL | 46.6 | -0.51873 | 77,67 | 73,60 | 90,57 | -4,69% | -17,11% | 7,62% | -10,35% |
| DOGE | 37.66 | 0.00044 | 0.07392 | 0.08119 | 0.09975 | -13,15% | -15,83% | -13,25% | -22,23% |

## Dettaglio asset

### BTC

- Prezzo: **63.889 $**
- Punteggio tecnico: **-1 / 12**
- Verdetto: **NEUTRALE / MISTO**
- Trend: **Trend misto** (-1)
- Momentum: **Momentum misto** (-1)
- Volume: **Volume neutrale** (0)
- Struttura: **Struttura ribassista con massimi e minimi decrescenti** (-2)
  - Dettaglio struttura: Ultimi minimi: 5.808e+04 -> 5.775e+04. Ultimi massimi: 6.725e+04 -> 6.554e+04.
- Divergenza: **Divergenza rialzista RSI** (2)
- Fase Wyckoff candidata: **Possibile accumulazione** (1)
  - Dettaglio Wyckoff: Prezzo sotto MA200, vicino alla parte bassa del range a 120 giorni, RSI 51.7.
- Fibonacci automatico: **TESTATO** (0)
  - Swing DOWN 2026-05-06 82.792 -> 2026-07-01 57.748; livello più vicino 23.6% a 63.658; stato TESTATO; confluenza: nessuna confluenza indipendente.
- Punteggio pattern: **0**
  - rialzista dominante: Doppio minimo (CANDIDATO, 0); ribassista dominante: Doppio massimo (TARGET RAGGIUNTO, 0).
- Supporto più vicino: **57.748**
- Resistenza più vicina: **65.544**

Pattern classici e ciclo di vita:

- Doppio minimo: **CANDIDATO** (0)
  - Due minimi simili vicino a 57.748 tra 2026-06-05 e 2026-07-01. Neckline stimata: 67.248. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 17 giorni.
  - neckline 67.248; target 76.748; distanza dalla neckline 5,26%; prezzo sotto neckline.
- Triplo minimo: **CANDIDATO** (0)
  - Tre minimi simili vicino a 57.748 dal 2026-06-05 al 2026-07-01. Neckline stimata: 67.248. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 17 giorni.
  - neckline 67.248; target 76.748; distanza dalla neckline 5,26%; prezzo sotto neckline.
- Adam and Eve Bottom: **CANDIDATO** (0)
  - Pattern Adam and Eve Bottom vicino a 57.748 dal 2026-06-05 al 2026-07-01. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 67.248. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 17 giorni.
  - neckline 67.248; target 76.748; distanza dalla neckline 5,26%; prezzo sotto neckline.
- Doppio massimo: **TARGET RAGGIUNTO** (0)
  - Due massimi simili vicino a 79.488 tra 2026-04-27 e 2026-05-26. Neckline ribassista stimata: 74.959. Breakout neckline: 2026-05-27 (52 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 70.429; progresso corrente: 244,38%. Relazione prezzo/neckline: sotto neckline.
  - neckline 74.959; target 70.429; breakout 2026-05-27 (52g); progresso 244,38%; prezzo sotto neckline.
- Triplo massimo: **TARGET RAGGIUNTO** (0)
  - Tre massimi simili vicino a 79.468 dal 2026-04-17 al 2026-05-26. Neckline ribassista stimata: 74.959. Breakout neckline: 2026-05-27 (52 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 70.449; progresso corrente: 245,47%. Relazione prezzo/neckline: sotto neckline.
  - neckline 74.959; target 70.449; breakout 2026-05-27 (52g); progresso 245,47%; prezzo sotto neckline.
- Eve and Adam Top: **TARGET RAGGIUNTO** (0)
  - Pattern Eve and Adam Top vicino a 82.792 dal 2026-04-22 al 2026-05-06. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 74.959. Breakout neckline: 2026-05-27 (52 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 67.125; progresso corrente: 141,31%. Relazione prezzo/neckline: sotto neckline.
  - neckline 74.959; target 67.125; breakout 2026-05-27 (52g); progresso 141,31%; prezzo sotto neckline.

### SOL

- Prezzo: **74,93 $**
- Punteggio tecnico: **-6 / 12**
- Verdetto: **DEBOLE**
- Trend: **Trend ribassista** (-3)
- Momentum: **Momentum debole** (-3)
- Volume: **Volume da distribuzione** (-1)
- Struttura: **Struttura rialzista con massimi e minimi crescenti** (2)
  - Dettaglio struttura: Ultimi minimi: 64.42 -> 74.16. Ultimi massimi: 74.89 -> 83.81.
- Divergenza: **Nessuna** (0)
- Fase Wyckoff candidata: **Markdown / fase ribassista** (-2)
  - Dettaglio Wyckoff: Prezzo sotto MA200 con trend a 90 giorni ancora debole.
- Fibonacci automatico: **REJECTION** (0)
  - Swing DOWN 2026-05-11 98,27 -> 2026-07-13 74,16; livello più vicino 23.6% a 79,85; stato REJECTION; confluenza: nessuna confluenza indipendente.
- Punteggio pattern: **+1**
  - rialzista dominante: Doppio minimo (MATURO, +1); ribassista dominante: Doppio massimo (CANDIDATO, 0).
- Supporto più vicino: **74,16**
- Resistenza più vicina: **83,81**

Pattern classici e ciclo di vita:

- Doppio minimo: **MATURO** (+1)
  - Due minimi simili vicino a 60,41 tra 2026-06-06 e 2026-06-25. Neckline stimata: 75,94. Breakout neckline: 2026-07-01 (17 giorni fa). Stato: MATURO. Target teorico: 91,46; progresso corrente: -6,50%. Relazione prezzo/neckline: sotto neckline.
  - neckline 75,94; target 91,46; breakout 2026-07-01 (17g); progresso -6,50%; prezzo sotto neckline.
- Triplo minimo: **CANDIDATO** (0)
  - Tre minimi simili vicino a 81,63 dal 2026-04-29 al 2026-05-23. Neckline stimata: 98,27. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 56 giorni.
  - neckline 98,27; target 114,91; distanza dalla neckline 31,14%; prezzo sotto neckline.
- Adam and Eve Bottom: **MATURO** (+1)
  - Pattern Adam and Eve Bottom vicino a 60,41 dal 2026-06-06 al 2026-06-25. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 75,94. Breakout neckline: 2026-07-01 (17 giorni fa). Stato: MATURO. Target teorico: 91,46; progresso corrente: -6,50%. Relazione prezzo/neckline: sotto neckline.
  - neckline 75,94; target 91,46; breakout 2026-07-01 (17g); progresso -6,50%; prezzo sotto neckline.
- Doppio massimo: **CANDIDATO** (0)
  - Due massimi simili vicino a 87,79 tra 2026-05-21 e 2026-07-04. Neckline ribassista stimata: 60,41. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 14 giorni.
  - neckline 60,41; target 33,04; distanza dalla neckline 24,03%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 88,05 dal 2026-04-27 al 2026-07-04. Neckline ribassista stimata: 60,41. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 14 giorni.
  - neckline 60,41; target 32,78; distanza dalla neckline 24,03%; prezzo sopra neckline.
- Eve and Adam Top: **CANDIDATO** (0)
  - Pattern Eve and Adam Top vicino a 87,79 dal 2026-05-21 al 2026-07-04. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 60,41. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 14 giorni.
  - neckline 60,41; target 33,04; distanza dalla neckline 24,03%; prezzo sopra neckline.

### DOGE

- Prezzo: **0.07237 $**
- Punteggio tecnico: **-6 / 12**
- Verdetto: **DEBOLE**
- Trend: **Trend ribassista** (-3)
- Momentum: **Momentum in miglioramento** (2)
- Volume: **Volume da distribuzione** (-2)
- Struttura: **Struttura ribassista con massimi e minimi decrescenti** (-2)
  - Dettaglio struttura: Ultimi minimi: 0.07107 -> 0.07097. Ultimi massimi: 0.09169 -> 0.07923.
- Divergenza: **Divergenza ribassista nascosta RSI** (-1)
- Fase Wyckoff candidata: **Possibile accumulazione** (1)
  - Dettaglio Wyckoff: Prezzo sotto MA200, vicino alla parte bassa del range a 120 giorni, RSI 37.7.
- Fibonacci automatico: **NON ATTIVO** (0)
  - Swing DOWN 2026-05-14 0.11825 -> 2026-07-13 0.07097; livello più vicino 23.6% a 0.08213; stato NON ATTIVO; confluenza: nessuna confluenza indipendente.
- Punteggio pattern: **-1**
  - rialzista dominante: Doppio minimo (CANDIDATO, 0); ribassista dominante: Triplo massimo (MATURO, -1).
- Supporto più vicino: **0.07097**
- Resistenza più vicina: **0.07923**

Pattern classici e ciclo di vita:

- Doppio minimo: **CANDIDATO** (0)
  - Due minimi simili vicino a 0.06961 tra 2026-06-30 e 2026-07-13. Neckline stimata: 0.07923. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 5 giorni.
  - neckline 0.07923; target 0.08886; distanza dalla neckline 9,48%; prezzo sotto neckline.
- Triplo minimo: **ASSENTE** (0)
- Adam and Eve Bottom: **CANDIDATO** (0)
  - Pattern Adam and Eve Bottom vicino a 0.06961 dal 2026-06-30 al 2026-07-13. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 0.07923. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 5 giorni.
  - neckline 0.07923; target 0.08886; distanza dalla neckline 9,48%; prezzo sotto neckline.
- Doppio massimo: **ASSENTE** (0)
- Triplo massimo: **MATURO** (-1)
  - Tre massimi simili vicino a 0.09772 dal 2026-03-25 al 2026-06-12. Neckline ribassista stimata: 0.07809. Breakout neckline: 2026-06-24 (24 giorni fa). Stato: MATURO. Target teorico: 0.05847; progresso corrente: 29,17%. Relazione prezzo/neckline: sotto neckline.
  - neckline 0.07809; target 0.05847; breakout 2026-06-24 (24g); progresso 29,17%; prezzo sotto neckline.
- Eve and Adam Top: **MATURO** (-1)
  - Pattern Eve and Adam Top vicino a 0.09584 dal 2026-04-07 al 2026-06-12. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 0.07809. Breakout neckline: 2026-06-24 (24 giorni fa). Stato: MATURO. Target teorico: 0.06035; progresso corrente: 32,27%. Relazione prezzo/neckline: sotto neckline.
  - neckline 0.07809; target 0.06035; breakout 2026-06-24 (24g); progresso 32,27%; prezzo sotto neckline.

## Fibonacci automatico

Il modulo seleziona uno swing recente tramite pivot confermati. Un semplice tocco vale 0: Fibonacci pesa al massimo ±1 soltanto quando il livello è tenuto, perso, recuperato o respinto e coincide con almeno un livello tecnico indipendente.

| Asset   | Swing                         | 23,6%   | 38,2%   | 50,0%   | 61,8%   | 78,6%   | Livello vicino   | Stato      | Confluenza                      |   Score |
|:--------|:------------------------------|:--------|:--------|:--------|:--------|:--------|:-----------------|:-----------|:--------------------------------|--------:|
| BTC | DOWN 2026-05-06 -> 2026-07-01 | 63.658 | 67.315 | 70.270 | 73.225 | 77.433 | 23.6% / 63.658 | TESTATO | nessuna confluenza indipendente | 0 |
| SOL | DOWN 2026-05-11 -> 2026-07-13 | 79,85 | 83,37 | 86,21 | 89,06 | 93,11 | 23.6% / 79,85 | REJECTION | nessuna confluenza indipendente | 0 |
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

- **BTC**: 0/30 previsioni controllate su 16 fatte. Stato: **RACCOLTA DATI**.
- **SOL**: 0/30 previsioni controllate su 16 fatte. Stato: **RACCOLTA DATI**.
- **DOGE**: 0/30 previsioni controllate su 16 fatte. Stato: **RACCOLTA DATI**.

| Asset | Previsioni fatte | Controllate | Progresso | In attesa | Stato | Prossimo controllo |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 16 | 0 | 0/30 [░░░░░░░░░░] | 16 | RACCOLTA DATI | 2026-08-02 / tra 15 giorni |
| SOL | 16 | 0 | 0/30 [░░░░░░░░░░] | 16 | RACCOLTA DATI | 2026-08-02 / tra 15 giorni |
| DOGE | 16 | 0 | 0/30 [░░░░░░░░░░] | 16 | RACCOLTA DATI | 2026-08-02 / tra 15 giorni |

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

Generato: 2026-07-18 05:14 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [data_quality_coherence_report.md](data_quality_coherence_report.md)

Questo controllo non modifica punteggi o decisioni. Verifica che tutti i moduli usino lo stesso prezzo corrente e che le nuove regole Technical/Classic Visual siano integre.

## Stato finale: **OK**

## Prezzo unico per modulo

| Modulo                  | Asset   | Campo             | Stato   | Prezzo snapshot   | Prezzo modulo   | Differenza   |
|:------------------------|:--------|:------------------|:--------|:------------------|:----------------|:-------------|
| Scanner                 | BTC     | current_price     | OK      | 63.889 $          | 63.889 $        | +0,0000%     |
| Scanner                 | DOGE    | current_price     | OK      | 0.07237 $         | 0.07237 $       | +0,0000%     |
| Scanner                 | SOL     | current_price     | OK      | 74,93 $           | 74,93 $         | +0,0000%     |
| Scanner Forecast        | BTC     | current_price     | OK      | 63.889 $          | 63.889 $        | +0,0000%     |
| Scanner Forecast        | SOL     | current_price     | OK      | 74,93 $           | 74,93 $         | +0,0000%     |
| Scanner Forecast        | DOGE    | current_price     | OK      | 0.07237 $         | 0.07237 $       | +0,0000%     |
| Technical Structure     | BTC     | price             | OK      | 63.889 $          | 63.889 $        | +0,0000%     |
| Technical Structure     | SOL     | price             | OK      | 74,93 $           | 74,93 $         | +0,0000%     |
| Technical Structure     | DOGE    | price             | OK      | 0.07237 $         | 0.07237 $       | +0,0000%     |
| Classic Technical       | BTC     | price             | OK      | 63.889 $          | 63.889 $        | +0,0000%     |
| Classic Technical       | SOL     | price             | OK      | 74,93 $           | 74,93 $         | +0,0000%     |
| Classic Technical       | DOGE    | price             | OK      | 0.07237 $         | 0.07237 $       | +0,0000%     |
| Classic Visual          | BTC     | price             | OK      | 63.889 $          | 63.889 $        | +0,0000%     |
| Classic Visual          | SOL     | price             | OK      | 74,93 $           | 74,93 $         | +0,0000%     |
| Classic Visual          | DOGE    | price             | OK      | 0.07237 $         | 0.07237 $       | +0,0000%     |
| Exchange Microstructure | BTC     | price             | OK      | 63.889 $          | 63.945 $        | +0,0869%     |
| Exchange Microstructure | SOL     | price             | OK      | 74,93 $           | 75,06 $         | +0,1722%     |
| Exchange Microstructure | DOGE    | price             | OK      | 0.07237 $         | 0.07244 $       | +0,0979%     |
| RSI top-cycle           | SOL     | current_price     | OK      | 74,93 $           | 74,93 $         | +0,0000%     |
| RSI top-cycle           | SOL     | current_price     | OK      | 74,93 $           | 74,93 $         | +0,0000%     |
| Frattale BTC/SOL        | SOL     | sol_current_price | OK      | 74,93 $           | 74,93 $         | +0,0000%     |
| Fractal path            | SOL     | current_price     | OK      | 74,93 $           | 74,93 $         | +0,0000%     |

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

Generato: 2026-07-18T08:17:34+00:00

- Modalità: **SOLO PAPER TRADING**
- Asset: **SOL spot**
- Leva: **nessuna (1x)**
- Capitale iniziale separato: **€40.000,00**
- Fonte mercato: **KUCOIN_PUBLIC_API**; nuove entrate: **CONSENTITE**

| Equity | Cash | SOL | Prezzo | Rendimento | Realizzato | Commissioni | Max DD | Operazioni |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €40.000,00 | €40.000,00 | 0.000000 | 74.9260 | +0.00% | €0,00 | €0,00 | 0.00% | 0 |

**Ultima decisione:** HOLD — Prezzo dentro la fascia neutrale.

Bande 4H: L2 71.2661 · L1 73.3957 · media 76.0577 · U1 78.7198 · U2 80.8494.

> Questo portafoglio non condivide capitale, posizioni o statistiche con il paper trading da €10.000.
<!-- SOL_SPOT_ADAPTIVE_END -->
