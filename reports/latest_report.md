<!-- COMPACT_REPORT_HEADER_START -->
> **Vista compatta:** Decisione operativa, Global Confluence e cambiamenti giornalieri restano aperti. Tocca il titolo di una sezione per mostrare o nascondere i dettagli.  
> Tutte le tabelle e tutti i dati restano nel file: copiando il Markdown raw viene copiato tutto.
<!-- COMPACT_REPORT_HEADER_END -->

<!-- COMPACT_SECTION_START:decision -->
<details open>
<summary><strong>🧭 Decisione operativa — da leggere per prima</strong></summary>

<!-- DECISION_REPORT_START -->

# Decisione operativa sintetica

Generato: 2026-07-29 05:15 UTC

Report separato completo: [decision_report.md](decision_report.md)

Sintesi automatica dello scanner: l'azione spot viene copiata direttamente dal Global Confluence; long, short e rischio restano filtri separati e più prudenti.

| Asset | Global | Direzione | Spot | Long leva | Short leva | Max long | Max short | Rischio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +2 | NEUTRALE / COSTRUTTIVO | HOLD / ATTESA CONFERME | NO LONG A LEVA / ATTENDI SOPRA 67.248 $ | NO SHORT | nessuna | nessuna | MEDIO / ALTO |
| SOL | 0 | NEUTRALE / INCERTO | HOLD LEGGERO / ATTESA CONFERME | NO LONG A LEVA | NO SHORT | nessuna | nessuna | MOLTO ALTO |
| DOGE | +1 | NEUTRALE / INCERTO | STAI ALLA FINESTRA | NO LONG A LEVA | NO SHORT | nessuna | nessuna | MOLTO ALTO |

## Lettura immediata

- **BTC**: Global = **+2**, spot = **HOLD / ATTESA CONFERME**, long = **NO LONG A LEVA / ATTENDI SOPRA 67.248 $**, short = **NO SHORT**, rischio = **MEDIO / ALTO**.
- **SOL**: Global = **0**, spot = **HOLD LEGGERO / ATTESA CONFERME**, long = **NO LONG A LEVA**, short = **NO SHORT**, rischio = **MOLTO ALTO**.
- **DOGE**: Global = **+1**, spot = **STAI ALLA FINESTRA**, long = **NO LONG A LEVA**, short = **NO SHORT**, rischio = **MOLTO ALTO**.

## Dettaglio logica

### BTC

- Global Confluence: **+2**
- Confluenza: **MISTA / PARZIALE**
- Bias Global: **Neutrale / misto**
- Direzione decisionale: **NEUTRALE / COSTRUTTIVO**
- Azione spot dal Global: **HOLD / ATTESA CONFERME**
- Long leva: **NO LONG A LEVA / ATTENDI SOPRA 67.248 $**
- Short leva: **NO SHORT**
- Rischio: **MEDIO / ALTO**
- Conferme: Prima resistenza sopra 66.910; conferma del doppio minimo sopra 67.248.
- Invalidazioni: Sotto 57.748 il quadro tecnico peggiora.

### SOL

- Global Confluence: **0**
- Confluenza: **MISTA / PARZIALE**
- Bias Global: **Neutrale / misto**
- Direzione decisionale: **NEUTRALE / INCERTO**
- Azione spot dal Global: **HOLD LEGGERO / ATTESA CONFERME**
- Long leva: **NO LONG A LEVA**
- Short leva: **NO SHORT**
- Rischio: **MOLTO ALTO**
- Conferme: conferma del adam and eve bottom sopra 83,81; nuova conferma tecnica sopra 78,73; milestone analogiche 85,31 / 91,62, valide soltanto se rientra anche il gap frattale.
- Invalidazioni: Allarmi sotto 69,80 / 73,40 / 62,19.

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
- Invalidazioni: Sotto 0.06829 il rischio ribassista aumenta.

## Nota semplice

- **Spot** = usa la stessa azione del Global Confluence, senza una seconda mappatura che possa produrre frasi diverse.
- **Zona alta storica** = zona dove non inseguire troppo; può essere zona da prendere profitto.
- **Zona bassa storica** = zona di rischio; con leva la liquidazione non dovrebbe stare lì vicino.
- **BTC leva** = nessun long a leva finché il prezzo snapshot non supera **67.248 $**; sotto quella soglia resta solo l'azione spot indicata dal Global.
- **Lifecycle EMA200** = per SOL resta solo contesto, peso Global 0; score interno 4; EMA200 circa 112,38 $; upside verso EMA200 +52,98%. Non autorizza leva e non aggiunge punti automatici.
- **NO LONG** non significa automaticamente **SHORT**. Lo short ha senso solo se il quadro è bearish o se lo spike viene spesso scaricato.
- Per SOL, se il Global è da **+3 in su**, la decisione non deve diventare bearish solo perché lo scanner grezzo a 30 giorni è incerto.

<!-- DECISION_REPORT_END -->

<!-- PAPER_TRADING_START -->
# Paper trading automatico KuCoin

Generato: 2026-07-29T05:15:12+00:00


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [paper_trading_report.md](paper_trading_report.md)

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-07-29T05:08:25+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-07-29T05:08:25+00:00 | 2026-07-29T05:08:25+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-07-29T04:45:00+00:00 | 2026-07-29T04:45:00+00:00 | 8,5 min | 25,0 min | OK |
| 60m | 12 | 2026-07-29T04:00:00+00:00 | 2026-07-29T04:00:00+00:00 | 8,5 min | 45,0 min | OK |
| 240m | 12 | 2026-07-29T00:00:00+00:00 | 2026-07-29T00:00:00+00:00 | 1,14 h | 1,00 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | ZEC | 240m | SHORT | -7,70 | 6,00 | 0,00 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | DOGE | 240m | SHORT | -7,05 | 6,00 | 0,00 | STALE_CANDLE | 1,14 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | HYPE | 240m | SHORT | -7,05 | 6,00 | 0,00 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | COTI | 240m | LONG | 5,75 | 6,00 | 0,25 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | SOL | 240m | SHORT | -4,84 | 6,00 | 1,16 | STALE_CANDLE | 1,14 h | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | AKE | 240m | LONG | 4,75 | 6,00 | 1,25 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | XRP | 240m | SHORT | -2,58 | 6,00 | 3,42 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | BTC | 240m | SHORT | -2,25 | 6,00 | 3,75 | STALE_CANDLE | 1,14 h | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | ADA | 240m | LONG | 2,16 | 6,00 | 3,84 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | ETH | 240m | LONG | 1,94 | 6,00 | 4,06 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | BANK | 240m | SHORT | -0,75 | 6,00 | 5,25 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | PEPE | 240m | SHORT | -0,61 | 6,00 | 5,39 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Bilanciata 1H V2 | BANK | 60m | SHORT | -8,25 | 5,50 | 0,00 | STRATEGY_FILTER | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro V2 non superato: regime, EMA, ritorni e RSI; per Rapida V2 servono anche breakout reale, volume e ADX. |
| Rapida 1H V2 | BANK | 60m | SHORT | -8,25 | 5,00 | 0,00 | STRATEGY_FILTER | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro V2 non superato: regime, EMA, ritorni e RSI; per Rapida V2 servono anche breakout reale, volume e ADX. |
| Bilanciata 1H V2 | HYPE | 60m | SHORT | -6,73 | 5,50 | 0,00 | STRATEGY_FILTER | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro V2 non superato: regime, EMA, ritorni e RSI; per Rapida V2 servono anche breakout reale, volume e ADX. |
| Rapida 1H V1 | HYPE | 60m | SHORT | -6,73 | 4,50 | 0,00 | STRATEGY_FILTER | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout DOWN oppure movimento breve ≥1,5%; breakout=NONE, movimento=-0.83%. |
| 1H Fast Score 6 75 V1 | HYPE | 60m | SHORT | -6,73 | 6,00 | 0,00 | STRATEGY_FILTER | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout DOWN oppure movimento breve ≥1,5%; breakout=NONE, movimento=-0.83%. |
| 1H Fast Score 6 75 No Trend Up V1 | HYPE | 60m | SHORT | -6,73 | 6,00 | 0,00 | STRATEGY_FILTER | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout DOWN oppure movimento breve ≥1,5%; breakout=NONE, movimento=-0.83%. |
| 1H Fast Score 6 75 Range Only V1 | HYPE | 60m | SHORT | -6,73 | 6,00 | 0,00 | STRATEGY_FILTER | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout DOWN oppure movimento breve ≥1,5%; breakout=NONE, movimento=-0.83%. |
| 1H Fast Score 6 75 Cost Aware V1 | HYPE | 60m | SHORT | -6,73 | 6,00 | 0,00 | STRATEGY_FILTER | 8,5 min | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout DOWN oppure movimento breve ≥1,5%; breakout=NONE, movimento=-0.83%. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.689,08 | -3,11% | €-310,92 | €3.000,00 | -10,36% | 6 | 27 | 33,33% | 0,70 | 6,36% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 27 | 964 | CAMPIONE INSUFFICIENTE | 30 (mancano 3) |

- Trade del Principale 4H chiusi: **27**; win rate **33,33%**; profit factor **0,70**.
- Expectancy: **€-11,65** per trade; P&L netto: **€-314,59**; max drawdown: **6,36%**.
- Valutazione: **Servono altri eventi indipendenti prima di trarre conclusioni.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 6 | €9.689,08 | €1.248,21 | €3.744,64 | €144,37 | €5,05 |
| TEST | Benchmark Donchian breakout 1H | 4 | €10.584,01 | €2.771,86 | €5.543,73 | €151,77 | €8,92 |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | 1 | €10.506,90 | €211,20 | €633,59 | €51,83 | €0,00 |
| TEST | 1H Fast Nohigh Cap75 V1 | 2 | €10.493,60 | €413,70 | €1.241,11 | €103,78 | €0,00 |
| TEST | 1H Fast Score 6 75 V1 | 2 | €10.487,01 | €403,79 | €1.211,37 | €105,23 | €0,00 |
| TEST | Bilanciata 1H V3 Filtered | 6 | €10.477,46 | €1.856,16 | €5.568,48 | €209,35 | €9,35 |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | 0 | €10.399,89 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H V1 | 5 | €10.365,00 | €2.197,27 | €6.591,81 | €106,40 | €17,18 |
| TEST | Scanner Top 5 Long 1H | 1 | €10.355,69 | €70,71 | €141,42 | €2,58 | €0,00 |
| TEST | Donchian 1H Gb20 120R V1 | 2 | €10.303,06 | €1.168,08 | €2.336,15 | €55,91 | €23,24 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 2 | €10.301,29 | €346,30 | €1.038,89 | €51,11 | €0,00 |
| TEST | 1H Fast V3 Nohigh Range Only V1 | 1 | €10.296,23 | €142,68 | €428,04 | €51,37 | €0,00 |
| TEST | Bilanciata 1H V2 | 2 | €10.279,42 | €173,21 | €519,64 | €49,92 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 0 | €10.271,73 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Side Regime Guard V1 | 3 | €10.262,84 | €1.902,44 | €3.804,89 | €153,05 | €10,69 |
| TEST | Main Dynamic Asset Selector V1 | 1 | €10.253,49 | €142,81 | €428,44 | €51,41 | €-28,67 |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 2 | €10.240,41 | €336,78 | €1.010,33 | €50,80 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 1 | €10.235,86 | €187,44 | €562,31 | €52,01 | €0,00 |
| TEST | Main Side Regime Guard V1 | 4 | €10.232,50 | €1.389,97 | €4.169,92 | €152,72 | €22,21 |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | 2 | €10.232,44 | €395,88 | €1.187,64 | €99,47 | €0,00 |
| TEST | Scanner Top 5 + forza BTC 1H | 1 | €10.224,31 | €37,16 | €74,32 | €1,36 | €0,00 |
| TEST | 1H Fast Score 6 75 Range Only V1 | 1 | €10.218,59 | €143,01 | €429,04 | €51,48 | €0,00 |
| TEST | 1H Fast V3 Cap75 V1 | 1 | €10.218,03 | €227,32 | €681,96 | €52,06 | €0,00 |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | 2 | €10.208,22 | €405,03 | €1.215,10 | €101,79 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 0 | €10.185,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast No Pepe V1 | 1 | €10.185,07 | €185,40 | €556,20 | €51,45 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 2 | €10.145,87 | €206,10 | €618,29 | €52,56 | €0,00 |
| TEST | Combo Adaptive | 4 | €10.114,12 | €1.205,67 | €2.411,33 | €104,15 | €0,33 |
| TEST | Sol Donchian 1H | 0 | €10.113,92 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 1H | 0 | €10.110,96 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 2 | €10.099,98 | €263,10 | €789,31 | €51,07 | €0,00 |
| TEST | Doge Ema 1H | 0 | €10.096,23 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | 0 | €10.096,10 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 4H | 0 | €10.086,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 4H | 0 | €10.084,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | 0 | €10.075,90 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Runner25 V1 | 5 | €10.054,19 | €2.334,73 | €4.669,45 | €151,91 | €10,50 |
| TEST | Combo Trend Side Regime Guard V1 | 5 | €10.050,48 | €3.091,48 | €6.182,96 | €199,05 | €-5,34 |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 1 | €10.049,44 | €184,02 | €552,07 | €51,07 | €0,00 |
| TEST | Rapida 1H V1 | 0 | €10.043,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Donchian 1H | 0 | €10.038,53 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V3 Filtered | 1 | €10.030,78 | €183,89 | €551,67 | €51,03 | €0,00 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €10.010,91 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 1 | €10.009,58 | €182,35 | €547,06 | €50,60 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 1 | €10.003,88 | €141,08 | €423,23 | €50,79 | €0,00 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 0 | €10.002,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Ampia 4H | 7 | €10.001,83 | €1.775,58 | €3.551,16 | €200,37 | €27,35 |
| TEST | Scalp RSI Short 85 · €50 · 15x | 0 | €10.000,61 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €10 · 15x | 0 | €10.000,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Continuation V1 | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €10 · 15x | 0 | €9.999,70 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €10 · 15x | 0 | €9.998,96 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · prudente · 5x | 0 | €9.998,64 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €50 · 15x | 0 | €9.998,52 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €10 · 15x | 0 | €9.998,50 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 1H | 0 | €9.996,84 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | 0 | €9.996,45 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 0 | €9.995,23 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €50 · 15x | 0 | €9.994,81 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Quality7 V1 | 3 | €9.994,10 | €2.293,91 | €4.587,82 | €150,23 | €10,64 |
| TEST | Btc Adaptive 1H | 1 | €9.993,77 | €1.158,94 | €3.476,83 | €50,07 | €-18,41 |
| TEST | 1H Balanced Short Trend Down Strict V1 | 1 | €9.993,76 | €675,44 | €2.026,32 | €49,98 | €-0,89 |
| TEST | Scalp RSI Long 15 · €50 · 15x | 0 | €9.992,50 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €10 · 15x | 0 | €9.991,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · prudente · 5x | 0 | €9.990,24 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Profit Lock V1 | 6 | €9.990,06 | €3.097,46 | €6.194,92 | €146,85 | €-31,88 |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | 4 | €9.988,39 | €1.388,29 | €2.776,58 | €149,15 | €0,00 |
| TEST | Scalp RSI Long 15 · prudente · 5x | 0 | €9.988,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Forza relativa 1H V2 | 3 | €9.987,62 | €2.495,25 | €4.990,50 | €104,10 | €-0,88 |
| TEST | Sol Donchian 4H | 0 | €9.985,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · prudente · 5x | 0 | €9.983,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 4H | 0 | €9.982,09 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V2 | 0 | €9.974,21 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Tp2 V1 | 3 | €9.974,12 | €221,90 | €665,70 | €51,17 | €0,00 |
| TEST | Sol Bollinger 1H | 0 | €9.970,30 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | 0 | €9.968,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Bollinger 1H | 0 | €9.959,49 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom10 Short | 5 | €9.958,94 | €489,81 | €979,63 | €51,01 | €-0,39 |
| TEST | Scanner Bottom15 Short | 5 | €9.958,94 | €489,81 | €979,63 | €51,01 | €-0,39 |
| TEST | Scanner Bottom20 Short | 5 | €9.958,94 | €489,81 | €979,63 | €51,01 | €-0,39 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 0 | €9.955,61 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €50 · 15x | 0 | €9.955,59 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.952,81 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 4H | 0 | €9.950,68 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 4H | 0 | €9.949,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Long Only V1 | 2 | €9.935,21 | €1.397,03 | €2.794,06 | €51,31 | €0,00 |
| TEST | Scanner Bottom 5 Short 1H | 6 | €9.934,33 | €3.366,63 | €6.733,26 | €100,30 | €-4,33 |
| TEST | 1H Balanced V3 Long Only V1 | 4 | €9.928,52 | €1.871,48 | €5.614,43 | €149,15 | €-0,87 |
| TEST | Btc Donchian 4H | 1 | €9.925,82 | €1.196,13 | €2.392,26 | €49,75 | €-24,14 |
| TEST | 1H Fast V3 No Esports Long Only V1 | 1 | €9.925,47 | €180,82 | €542,46 | €50,18 | €0,00 |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | 0 | €9.923,70 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | 0 | €9.922,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 1H | 1 | €9.909,36 | €1.148,42 | €3.445,25 | €49,61 | €-10,89 |
| TEST | Combo Adaptive Regime V1 | 0 | €9.903,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Bollinger 1H | 0 | €9.902,02 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Ema 4H | 0 | €9.894,27 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 1H | 1 | €9.892,55 | €1.147,21 | €3.441,62 | €49,56 | €-18,22 |
| TEST | Sol Ema 4H | 1 | €9.888,11 | €780,22 | €1.560,44 | €49,48 | €-7,03 |
| TEST | Eth Donchian 1H | 0 | €9.871,99 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Nohigh V1 | 0 | €9.870,43 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Tp3 V1 | 3 | €9.864,96 | €2.278,82 | €4.557,64 | €147,95 | €10,22 |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | 0 | €9.857,49 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Tp3 V1 | 1 | €9.843,56 | €85,15 | €170,29 | €3,11 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 2 | €9.838,56 | €327,41 | €982,22 | €49,25 | €0,00 |
| TEST | Scanner Top5 Btc Runner25 V1 | 1 | €9.837,77 | €70,70 | €141,40 | €2,58 | €0,00 |
| TEST | Combo Mean Reversion | 0 | €9.832,55 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 No Esports V1 | 1 | €9.826,60 | €180,15 | €540,44 | €49,99 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 1 | €9.818,04 | €194,51 | €583,53 | €49,25 | €0,00 |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | 0 | €9.807,66 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Gb20 Be V1 | 1 | €9.806,54 | €1.403,77 | €2.807,55 | €50,57 | €0,00 |
| TEST | Eth Adaptive 1H | 0 | €9.799,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Expanded V1 | 1 | €9.799,16 | €33,54 | €67,08 | €1,22 | €0,00 |
| TEST | Combo Adaptive Quality7 Regime V1 | 0 | €9.797,24 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Gb20 Partial V1 | 1 | €9.796,05 | €1.376,47 | €2.752,95 | €50,21 | €0,00 |
| TEST | Sol Adaptive 1H | 0 | €9.781,19 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Runner25 V1 | 1 | €9.771,73 | €20,87 | €41,74 | €0,76 | €0,00 |
| TEST | Scanner Top5 Btc Btc Le3 V1 | 1 | €9.770,35 | €37,63 | €75,26 | €1,37 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 0 | €9.762,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Benchmark Bollinger mean reversion 1H | 0 | €9.761,49 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Global Confluence puro 1H | 1 | €9.760,94 | €1.529,14 | €3.058,29 | €48,93 | €-23,74 |
| TEST | Master Adaptive No Alt V1 | 1 | €9.758,94 | €21,54 | €43,08 | €0,79 | €0,00 |
| TEST | Master Adaptive V1 | 1 | €9.754,92 | €21,54 | €43,08 | €0,79 | €0,00 |
| TEST | Eth Ema 1H | 0 | €9.727,87 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 1 | €9.724,36 | €177,16 | €531,47 | €49,16 | €0,00 |
| TEST | Benchmark trend following EMA 1H | 7 | €9.710,78 | €1.344,77 | €2.689,54 | €102,28 | €28,48 |
| TEST | Master Adaptive Gb20 Loss Cap V1 | 2 | €9.710,17 | €2.043,62 | €4.087,25 | €100,09 | €-23,61 |
| TEST | Combo Scanner | 1 | €9.693,06 | €23,89 | €47,78 | €0,87 | €0,00 |
| TEST | Combo Adaptive Partial 1R V1 | 3 | €9.692,34 | €2.124,48 | €4.248,96 | €121,20 | €10,31 |
| TEST | Scanner Top5 Btc Guard V1 | 0 | €9.688,64 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Balanced Long No Rhv V1 | 2 | €9.660,53 | €1.051,34 | €3.154,01 | €98,63 | €0,00 |
| TEST | Forza relativa 1H V1 | 6 | €9.660,48 | €2.436,58 | €4.873,16 | €103,52 | €32,72 |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | 0 | €9.639,39 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Gb20 V1 | 2 | €9.628,98 | €1.549,90 | €3.099,79 | €97,01 | €0,00 |
| TEST | Scanner Top5 Btc Mfe V1 | 1 | €9.587,00 | €1.363,71 | €2.727,43 | €49,13 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 1 | €9.580,46 | €174,53 | €523,60 | €48,43 | €0,00 |
| TEST | Scanner Top10 Long | 2 | €9.541,58 | €1.395,50 | €2.791,00 | €52,73 | €0,00 |
| TEST | Scanner Top15 Long | 2 | €9.541,58 | €1.395,50 | €2.791,00 | €52,73 | €0,00 |
| TEST | Scanner Top20 Long | 2 | €9.541,58 | €1.395,50 | €2.791,00 | €52,73 | €0,00 |
| TEST | Combo Trend | 6 | €9.499,16 | €3.508,09 | €7.016,18 | €141,66 | €19,46 |
| TEST | Scanner Top5 Btc Guard Mfe V1 | 0 | €9.463,31 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Long Only V1 | 1 | €9.450,13 | €172,16 | €516,48 | €47,77 | €0,00 |
| TEST | Master Adaptive Strict3 V1 | 1 | €9.408,26 | €1.330,61 | €2.661,21 | €48,54 | €0,00 |
| TEST | Combo Adaptive Mfe Trail | 1 | €9.333,92 | €883,78 | €1.767,56 | €48,23 | €0,00 |

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
| PRINCIPALE | Principale 4H | Confluenza trend | €9.689,08 | €-314,59 | 27 | 27 | 33,33% | 0,70 | €-11,65 | 6,36% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €10.584,01 | €577,97 | 36 | 36 | 55,56% | 1,67 | €16,05 | 3,09% |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | Momentum / breakout | €10.506,90 | €507,28 | 35 | 35 | 54,29% | 1,94 | €14,49 | 1,96% |
| TEST | 1H Fast Nohigh Cap75 V1 | Momentum / breakout | €10.493,60 | €494,34 | 62 | 62 | 48,39% | 1,41 | €7,97 | 2,83% |
| TEST | 1H Fast Score 6 75 V1 | Momentum / breakout | €10.487,01 | €487,73 | 73 | 73 | 45,21% | 1,37 | €6,68 | 2,49% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €10.477,46 | €471,30 | 60 | 60 | 41,67% | 1,37 | €7,85 | 2,49% |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | Momentum / breakout V3 Filtered | €10.399,89 | €399,89 | 20 | 20 | 65,00% | 3,42 | €19,99 | 1,39% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €10.365,00 | €351,55 | 70 | 70 | 47,14% | 1,29 | €5,02 | 3,56% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.355,69 | €355,77 | 49 | 49 | 44,90% | 1,31 | €7,26 | 4,79% |
| TEST | Donchian 1H Gb20 120R V1 | Donchian breakout 20 barre | €10.303,06 | €281,00 | 6 | 6 | 66,67% | 5,76 | €46,83 | 1,61% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | Momentum / breakout V3 Filtered | €10.301,29 | €301,92 | 31 | 31 | 51,61% | 2,05 | €9,74 | 2,01% |
| TEST | 1H Fast V3 Nohigh Range Only V1 | Momentum / breakout V3 Filtered | €10.296,23 | €296,59 | 11 | 11 | 63,64% | 2,82 | €26,96 | 1,78% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €10.279,42 | €279,74 | 39 | 37 | 53,85% | 1,36 | €7,17 | 2,75% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | Momentum / breakout V3 Filtered | €10.271,73 | €271,73 | 22 | 22 | 50,00% | 1,74 | €12,35 | 1,72% |
| TEST | Combo Adaptive Side Regime Guard V1 | Combo Adaptive | €10.262,84 | €254,67 | 30 | 30 | 56,67% | 1,73 | €8,49 | 1,58% |
| TEST | Main Dynamic Asset Selector V1 | Confluenza trend | €10.253,49 | €282,54 | 10 | 10 | 50,00% | 2,29 | €28,25 | 1,50% |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | Momentum / breakout V3 Filtered | €10.240,41 | €241,67 | 15 | 15 | 60,00% | 4,66 | €16,11 | 1,01% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | Momentum / breakout V3 Filtered | €10.235,86 | €236,20 | 19 | 19 | 52,63% | 1,90 | €12,43 | 2,72% |
| TEST | Main Side Regime Guard V1 | Confluenza trend | €10.232,50 | €212,50 | 13 | 13 | 46,15% | 1,65 | €16,35 | 2,40% |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | Momentum / breakout | €10.232,44 | €233,15 | 26 | 26 | 50,00% | 1,70 | €8,97 | 1,76% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €10.224,31 | €224,35 | 40 | 40 | 40,00% | 1,25 | €5,61 | 3,94% |
| TEST | 1H Fast Score 6 75 Range Only V1 | Momentum / breakout | €10.218,59 | €218,95 | 12 | 12 | 58,33% | 1,75 | €18,25 | 2,28% |
| TEST | 1H Fast V3 Cap75 V1 | Momentum / breakout V3 Filtered | €10.218,03 | €218,44 | 67 | 67 | 44,78% | 1,16 | €3,26 | 3,61% |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | Momentum / breakout | €10.208,22 | €208,95 | 31 | 31 | 54,84% | 1,32 | €6,74 | 2,77% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | Momentum / breakout V3 Filtered | €10.185,37 | €185,37 | 22 | 22 | 40,91% | 1,57 | €8,43 | 2,27% |
| TEST | 1H Fast No Pepe V1 | Momentum / breakout | €10.185,07 | €185,40 | 71 | 71 | 45,07% | 1,14 | €2,61 | 2,15% |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | Momentum / breakout V3 Filtered | €10.145,87 | €146,24 | 42 | 42 | 47,62% | 1,20 | €3,48 | 2,91% |
| TEST | Combo Adaptive | Combo Adaptive | €10.114,12 | €116,12 | 36 | 36 | 44,44% | 1,22 | €3,23 | 2,58% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €10.113,92 | €113,92 | 4 | 4 | 75,00% | 26,39 | €28,48 | 0,79% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.110,96 | €110,96 | 4 | 4 | 75,00% | 2,94 | €27,74 | 0,70% |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | Momentum / breakout V3 Filtered | €10.099,98 | €100,46 | 53 | 53 | 56,60% | 1,12 | €1,90 | 3,59% |
| TEST | Doge Ema 1H | Trend following EMA | €10.096,23 | €96,23 | 10 | 10 | 70,00% | 1,57 | €9,62 | 1,36% |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | Momentum / breakout V3 Filtered | €10.096,10 | €96,10 | 59 | 59 | 50,85% | 1,11 | €1,63 | 2,98% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €10.086,98 | €86,98 | 1 | 1 | 100,00% | ∞ | €86,98 | 0,40% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.084,12 | €84,12 | 1 | 1 | 100,00% | ∞ | €84,12 | 0,30% |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | Momentum / breakout V3 Filtered | €10.075,90 | €75,90 | 20 | 20 | 45,00% | 1,17 | €3,80 | 2,17% |
| TEST | Combo Adaptive Runner25 V1 | Combo Adaptive | €10.054,19 | €47,13 | 38 | 38 | 39,47% | 1,07 | €1,24 | 2,31% |
| TEST | Combo Trend Side Regime Guard V1 | Combo Trend | €10.050,48 | €58,63 | 25 | 25 | 52,00% | 1,15 | €2,35 | 2,23% |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | Momentum / breakout V3 Filtered | €10.049,44 | €49,77 | 22 | 22 | 45,45% | 1,12 | €2,26 | 3,05% |
| TEST | Rapida 1H V1 | Momentum / breakout | €10.043,28 | €43,28 | 78 | 78 | 34,62% | 1,02 | €0,55 | 6,76% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €10.038,53 | €38,53 | 6 | 6 | 66,67% | 1,34 | €6,42 | 1,08% |
| TEST | Rapida 1H V3 Filtered | Momentum / breakout V3 Filtered | €10.030,78 | €31,11 | 102 | 102 | 38,24% | 1,02 | €0,31 | 2,94% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €10.010,91 | €10,91 | 11 | 11 | 36,36% | 1,23 | €0,99 | 0,25% |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | Momentum / breakout V3 Filtered | €10.009,58 | €9,91 | 29 | 29 | 37,93% | 1,02 | €0,34 | 4,84% |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | Momentum / breakout V3 Filtered | €10.003,88 | €4,24 | 7 | 7 | 42,86% | 1,03 | €0,61 | 2,15% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €10.002,18 | €2,18 | 11 | 11 | 36,36% | 1,23 | €0,20 | 0,05% |
| TEST | Ampia 4H | Confluenza trend | €10.001,83 | €-23,91 | 22 | 22 | 22,73% | 0,96 | €-1,09 | 3,68% |
| TEST | Scalp RSI Short 85 · €50 · 15x | Inversione RSI estrema 15m | €10.000,61 | €0,61 | 2 | 2 | 50,00% | 1,74 | €0,30 | 0,07% |
| TEST | Scalp RSI Short 85 · €10 · 15x | Inversione RSI estrema 15m | €10.000,12 | €0,12 | 2 | 2 | 50,00% | 1,74 | €0,06 | 0,01% |
| TEST | Scanner Bottom5 Short Continuation V1 | Scanner Bottom5 Short Continuation | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 80 · €10 · 15x | Inversione RSI estrema 15m | €9.999,70 | €-0,30 | 3 | 3 | 66,67% | 0,63 | €-0,10 | 0,02% |
| TEST | Scalp RSI Long 20 · €10 · 15x | Inversione RSI estrema 15m | €9.998,96 | €-1,04 | 2 | 2 | 0,00% | 0,00 | €-0,52 | 0,02% |
| TEST | Scalp RSI Short 85 · prudente · 5x | Inversione RSI estrema 15m | €9.998,64 | €-1,36 | 2 | 2 | 50,00% | 0,42 | €-0,68 | 0,11% |
| TEST | Scalp RSI Short 80 · €50 · 15x | Inversione RSI estrema 15m | €9.998,52 | €-1,48 | 3 | 3 | 66,67% | 0,63 | €-0,49 | 0,09% |
| TEST | Scalp RSI Long 15 · €10 · 15x | Inversione RSI estrema 15m | €9.998,50 | €-1,50 | 1 | 1 | 0,00% | 0,00 | €-1,50 | 0,02% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €9.996,84 | €-3,16 | 5 | 5 | 60,00% | 0,97 | €-0,63 | 1,49% |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | Momentum / breakout | €9.996,45 | €-3,55 | 25 | 25 | 36,00% | 0,99 | €-0,14 | 2,27% |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | Momentum / breakout V3 Filtered | €9.995,23 | €-4,77 | 15 | 15 | 46,67% | 0,99 | €-0,32 | 2,70% |
| TEST | Scalp RSI Long 20 · €50 · 15x | Inversione RSI estrema 15m | €9.994,81 | €-5,19 | 2 | 2 | 0,00% | 0,00 | €-2,59 | 0,08% |
| TEST | Combo Adaptive Quality7 V1 | Combo Adaptive | €9.994,10 | €-13,15 | 23 | 23 | 34,78% | 0,96 | €-0,57 | 2,48% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €9.993,77 | €13,28 | 3 | 3 | 66,67% | 1,24 | €4,43 | 0,89% |
| TEST | 1H Balanced Short Trend Down Strict V1 | Confluenza trend | €9.993,76 | €-4,13 | 1 | 1 | 0,00% | 0,00 | €-4,13 | 0,90% |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | €9.992,50 | €-7,50 | 1 | 1 | 0,00% | 0,00 | €-7,50 | 0,11% |
| TEST | Scalp RSI Long 25 · €10 · 15x | Inversione RSI estrema 15m | €9.991,12 | €-8,88 | 7 | 7 | 28,57% | 0,24 | €-1,27 | 0,12% |
| TEST | Scalp RSI Short 80 · prudente · 5x | Inversione RSI estrema 15m | €9.990,24 | €-9,76 | 3 | 3 | 66,67% | 0,28 | €-3,25 | 0,21% |
| TEST | Scanner Bottom5 Short Profit Lock V1 | Scanner Bottom 5 Short | €9.990,06 | €26,01 | 14 | 14 | 50,00% | 1,16 | €1,86 | 1,53% |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | Scanner Bottom 5 Short | €9.988,39 | €-9,84 | 15 | 15 | 53,33% | 0,96 | €-0,66 | 1,38% |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | €9.988,38 | €-11,62 | 1 | 1 | 0,00% | 0,00 | €-11,62 | 0,17% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €9.987,62 | €-8,51 | 52 | 51 | 40,38% | 0,99 | €-0,16 | 5,53% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €9.985,00 | €-15,00 | 2 | 2 | 50,00% | 0,71 | €-7,50 | 0,79% |
| TEST | Scalp RSI Long 20 · prudente · 5x | Inversione RSI estrema 15m | €9.983,60 | €-16,40 | 2 | 2 | 0,00% | 0,00 | €-8,20 | 0,24% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €9.982,09 | €-17,91 | 2 | 2 | 50,00% | 0,65 | €-8,96 | 0,77% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €9.974,21 | €-25,79 | 17 | 15 | 41,18% | 0,93 | €-1,52 | 1,69% |
| TEST | 1H Fast Tp2 V1 | Momentum / breakout | €9.974,12 | €-25,48 | 76 | 76 | 36,84% | 0,98 | €-0,34 | 2,58% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.970,30 | €-29,70 | 5 | 5 | 40,00% | 0,82 | €-5,94 | 1,89% |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | Scanner Top 5 + forza BTC | €9.968,72 | €-31,28 | 10 | 10 | 30,00% | 0,87 | €-3,13 | 2,84% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €9.959,49 | €-40,51 | 2 | 2 | 50,00% | 0,28 | €-20,26 | 0,91% |
| TEST | Scanner Bottom10 Short | Scanner Bottom10 Short | €9.958,94 | €-39,45 | 20 | 20 | 45,00% | 0,91 | €-1,97 | 2,72% |
| TEST | Scanner Bottom15 Short | Scanner Bottom15 Short | €9.958,94 | €-39,45 | 20 | 20 | 45,00% | 0,91 | €-1,97 | 2,72% |
| TEST | Scanner Bottom20 Short | Scanner Bottom20 Short | €9.958,94 | €-39,45 | 20 | 20 | 45,00% | 0,91 | €-1,97 | 2,72% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €9.955,61 | €-44,39 | 7 | 7 | 14,29% | 0,12 | €-6,34 | 0,58% |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | €9.955,59 | €-44,41 | 7 | 7 | 28,57% | 0,24 | €-6,34 | 0,58% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.952,81 | €-47,19 | 11 | 11 | 36,36% | 0,29 | €-4,29 | 0,58% |
| TEST | Btc Ema 4H | Trend following EMA | €9.950,68 | €-49,32 | 1 | 1 | 0,00% | 0,00 | €-49,32 | 0,96% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €9.949,62 | €-50,38 | 1 | 1 | 0,00% | 0,00 | €-50,38 | 0,74% |
| TEST | Combo Adaptive Long Only V1 | Combo Adaptive | €9.935,21 | €-63,10 | 18 | 18 | 27,78% | 0,82 | €-3,51 | 2,34% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.934,33 | €-56,24 | 41 | 41 | 39,02% | 0,93 | €-1,37 | 5,48% |
| TEST | 1H Balanced V3 Long Only V1 | Confluenza trend V3 Filtered | €9.928,52 | €-66,58 | 18 | 18 | 38,89% | 0,83 | €-3,70 | 1,76% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €9.925,82 | €-49,32 | 1 | 1 | 0,00% | 0,00 | €-49,32 | 1,25% |
| TEST | 1H Fast V3 No Esports Long Only V1 | Momentum / breakout V3 Filtered | €9.925,47 | €-74,20 | 35 | 35 | 40,00% | 0,90 | €-2,12 | 4,40% |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | Momentum / breakout V3 Filtered | €9.923,70 | €-76,30 | 49 | 49 | 46,94% | 0,93 | €-1,56 | 3,21% |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | Combo Adaptive | €9.922,04 | €-77,96 | 11 | 11 | 45,45% | 0,71 | €-7,09 | 1,95% |
| TEST | Sol Ema 1H | Trend following EMA | €9.909,36 | €-77,68 | 6 | 6 | 33,33% | 0,64 | €-12,95 | 1,88% |
| TEST | Combo Adaptive Regime V1 | Combo Adaptive | €9.903,28 | €-96,72 | 22 | 22 | 45,45% | 0,79 | €-4,40 | 2,18% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €9.902,02 | €-97,98 | 4 | 4 | 25,00% | 0,41 | €-24,49 | 1,89% |
| TEST | Eth Ema 4H | Trend following EMA | €9.894,27 | €-105,73 | 2 | 2 | 0,00% | 0,00 | €-52,87 | 1,21% |
| TEST | Btc Ema 1H | Trend following EMA | €9.892,55 | €-88,14 | 6 | 6 | 33,33% | 0,59 | €-14,69 | 1,56% |
| TEST | Sol Ema 4H | Trend following EMA | €9.888,11 | €-103,69 | 2 | 2 | 0,00% | 0,00 | €-51,84 | 1,35% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.871,99 | €-128,01 | 5 | 5 | 20,00% | 0,42 | €-25,60 | 1,62% |
| TEST | 1H Fast V3 Nohigh V1 | Momentum / breakout V3 Filtered | €9.870,43 | €-129,57 | 62 | 62 | 38,71% | 0,90 | €-2,09 | 2,96% |
| TEST | Combo Adaptive Tp3 V1 | Combo Adaptive | €9.864,96 | €-141,67 | 21 | 21 | 38,10% | 0,64 | €-6,75 | 2,44% |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | Momentum / breakout V3 Filtered | €9.857,49 | €-142,51 | 44 | 44 | 40,91% | 0,86 | €-3,24 | 2,86% |
| TEST | Scanner Top5 Btc Tp3 V1 | Scanner Top 5 + forza BTC | €9.843,56 | €-156,34 | 25 | 25 | 32,00% | 0,80 | €-6,25 | 4,68% |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | Momentum / breakout V3 Filtered | €9.838,56 | €-160,85 | 35 | 35 | 42,86% | 0,76 | €-4,60 | 3,08% |
| TEST | Scanner Top5 Btc Runner25 V1 | Scanner Top 5 + forza BTC | €9.837,77 | €-162,15 | 29 | 29 | 34,48% | 0,79 | €-5,59 | 4,99% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €9.832,55 | €-167,45 | 20 | 20 | 35,00% | 0,76 | €-8,37 | 3,60% |
| TEST | 1H Fast V3 No Esports V1 | Momentum / breakout V3 Filtered | €9.826,60 | €-173,07 | 76 | 76 | 38,16% | 0,89 | €-2,28 | 2,91% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | Momentum / breakout V3 Filtered | €9.818,04 | €-181,61 | 23 | 23 | 43,48% | 0,64 | €-7,90 | 3,23% |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | Scanner Top 5 + forza BTC | €9.807,66 | €-192,34 | 19 | 19 | 31,58% | 0,70 | €-10,12 | 4,36% |
| TEST | Master Adaptive Gb20 Be V1 | Master Adaptive Consensus | €9.806,54 | €-191,77 | 21 | 21 | 19,05% | 0,67 | €-9,13 | 3,32% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.799,60 | €-200,40 | 6 | 6 | 33,33% | 0,08 | €-33,40 | 2,09% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €9.799,16 | €-200,80 | 21 | 21 | 33,33% | 0,74 | €-9,56 | 3,64% |
| TEST | Combo Adaptive Quality7 Regime V1 | Combo Adaptive | €9.797,24 | €-202,76 | 11 | 11 | 27,27% | 0,31 | €-18,43 | 2,32% |
| TEST | Master Adaptive Gb20 Partial V1 | Master Adaptive Consensus | €9.796,05 | €-202,30 | 16 | 16 | 31,25% | 0,62 | €-12,64 | 2,89% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €9.781,19 | €-218,81 | 7 | 7 | 28,57% | 0,24 | €-31,26 | 2,92% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €9.771,73 | €-228,24 | 20 | 20 | 30,00% | 0,69 | €-11,41 | 3,98% |
| TEST | Scanner Top5 Btc Btc Le3 V1 | Scanner Top 5 + forza BTC | €9.770,35 | €-229,60 | 21 | 21 | 33,33% | 0,64 | €-10,93 | 4,42% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | Momentum / breakout V3 Filtered | €9.762,18 | €-237,82 | 7 | 7 | 14,29% | 0,02 | €-33,97 | 2,82% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €9.761,49 | €-238,51 | 50 | 50 | 40,00% | 0,82 | €-4,77 | 5,70% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.760,94 | €-213,48 | 12 | 12 | 33,33% | 0,45 | €-17,79 | 2,92% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €9.758,94 | €-241,03 | 18 | 18 | 27,78% | 0,66 | €-13,39 | 4,03% |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | €9.754,92 | €-245,05 | 18 | 18 | 27,78% | 0,66 | €-13,61 | 4,07% |
| TEST | Eth Ema 1H | Trend following EMA | €9.727,87 | €-272,13 | 8 | 8 | 25,00% | 0,16 | €-34,02 | 2,76% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | Momentum / breakout V3 Filtered | €9.724,36 | €-275,32 | 30 | 30 | 33,33% | 0,62 | €-9,18 | 4,83% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.710,78 | €-315,16 | 39 | 39 | 30,77% | 0,68 | €-8,08 | 3,97% |
| TEST | Master Adaptive Gb20 Loss Cap V1 | Master Adaptive Consensus | €9.710,17 | €-263,40 | 17 | 17 | 23,53% | 0,60 | €-15,49 | 4,36% |
| TEST | Combo Scanner | Combo Scanner | €9.693,06 | €-306,92 | 49 | 49 | 36,73% | 0,77 | €-6,26 | 5,08% |
| TEST | Combo Adaptive Partial 1R V1 | Combo Adaptive | €9.692,34 | €-315,24 | 38 | 38 | 39,47% | 0,56 | €-8,30 | 3,97% |
| TEST | Scanner Top5 Btc Guard V1 | Scanner Top 5 + forza BTC | €9.688,64 | €-311,36 | 24 | 24 | 25,00% | 0,59 | €-12,97 | 3,94% |
| TEST | 1H Balanced Long No Rhv V1 | Confluenza trend | €9.660,53 | €-337,58 | 18 | 18 | 27,78% | 0,48 | €-18,75 | 4,32% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €9.660,48 | €-369,44 | 46 | 46 | 28,26% | 0,70 | €-8,03 | 7,55% |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | Scanner Top 5 + forza BTC | €9.639,39 | €-360,61 | 34 | 34 | 35,29% | 0,61 | €-10,61 | 3,93% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €9.628,98 | €-369,16 | 52 | 52 | 57,69% | 0,60 | €-7,10 | 4,27% |
| TEST | Scanner Top5 Btc Mfe V1 | Scanner Top 5 + forza BTC | €9.587,00 | €-411,37 | 33 | 33 | 33,33% | 0,46 | €-12,47 | 5,00% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | Momentum / breakout V3 Filtered | €9.580,46 | €-419,23 | 10 | 10 | 0,00% | 0,00 | €-41,92 | 4,20% |
| TEST | Scanner Top10 Long | Scanner Top10 Long | €9.541,58 | €-456,73 | 20 | 20 | 30,00% | 0,34 | €-22,84 | 6,28% |
| TEST | Scanner Top15 Long | Scanner Top15 Long | €9.541,58 | €-456,73 | 20 | 20 | 30,00% | 0,34 | €-22,84 | 6,28% |
| TEST | Scanner Top20 Long | Scanner Top20 Long | €9.541,58 | €-456,73 | 20 | 20 | 30,00% | 0,34 | €-22,84 | 6,28% |
| TEST | Combo Trend | Combo Trend | €9.499,16 | €-515,52 | 56 | 56 | 30,36% | 0,71 | €-9,21 | 7,64% |
| TEST | Scanner Top5 Btc Guard Mfe V1 | Scanner Top 5 + forza BTC | €9.463,31 | €-536,69 | 41 | 41 | 34,15% | 0,53 | €-13,09 | 5,43% |
| TEST | 1H Fast V3 Long Only V1 | Momentum / breakout V3 Filtered | €9.450,13 | €-549,56 | 55 | 55 | 29,09% | 0,62 | €-9,99 | 6,46% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €9.408,26 | €-590,15 | 26 | 26 | 23,08% | 0,49 | €-22,70 | 6,12% |
| TEST | Combo Adaptive Mfe Trail | Combo Adaptive | €9.333,92 | €-665,02 | 49 | 49 | 28,57% | 0,42 | €-13,57 | 6,69% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | LAB | SHORT | Confluenza trend | 240m | 3,0x | 0,17841 | 0,17841 | 0,17841 | 0,23699 | 0,13559 | €136,26 | €408,77 | €0,00 | €-0,00 |
| Principale 4H | ONDO | LONG | Confluenza trend | 240m | 3,0x | 0,40344 | 0,40344 | 0,37762 | 0,27098 | 0,45509 | €254,70 | €764,09 | €48,91 | €0,00 |
| Principale 4H | SHIB | LONG | Confluenza trend | 240m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €8,88 | €26,63 | €2,22 | €0,00 |
| Principale 4H | SOL | SHORT | Confluenza trend | 240m | 3,0x | 73,19036 | 73,52000 | 75,30024 | 97,22119 | 68,97060 | €9,18 | €27,53 | €0,79 | €-0,12 |
| Principale 4H | DOGE | SHORT | Confluenza trend | 240m | 3,0x | 0,07019 | 0,07062 | 0,07248 | 0,09323 | 0,06560 | €485,79 | €1.457,36 | €47,61 | €-9,01 |
| Principale 4H | HYPE | SHORT | Confluenza trend | 240m | 3,0x | 55,30294 | 54,56300 | 57,64134 | 73,46073 | 50,62613 | €353,42 | €1.060,27 | €44,83 | €14,19 |
| Bilanciata 1H V1 | ALLO | SHORT | Confluenza trend | 60m | 3,0x | 0,36179 | 0,36179 | 0,40521 | 0,48058 | 0,27496 | €141,53 | €424,59 | €50,95 | €-0,00 |
| Bilanciata 1H V1 | NEAR | SHORT | Confluenza trend | 60m | 3,0x | 1,73096 | 1,73096 | 1,69553 | 2,29929 | 1,66292 | €19,50 | €58,51 | €0,00 | €-0,00 |
| Bilanciata 1H V1 | BTC | SHORT | Confluenza trend | 60m | 3,0x | 63620,87328 | 63957,69000 | 64537,01386 | 84509,72667 | 61788,59213 | €1.153,42 | €3.460,26 | €49,83 | €-18,32 |
| Bilanciata 1H V1 | HYPE | SHORT | Confluenza trend | 60m | 3,0x | 55,31793 | 54,56300 | 55,05561 | 73,48066 | 53,09375 | €867,03 | €2.601,09 | €0,00 | €35,50 |
| Bilanciata 1H V1 | BEAT | LONG | Confluenza trend | 60m | 3,0x | 3,34076 | 3,34076 | 2,94410 | 2,24388 | 4,13409 | €15,79 | €47,36 | €5,62 | €0,00 |
| 1H Balanced Long No Rhv V1 | XMR | LONG | Confluenza trend | 60m | 3,0x | 366,72991 | 366,72991 | 360,04130 | 246,32025 | 380,10712 | €915,26 | €2.745,79 | €50,08 | €0,00 |
| 1H Balanced Long No Rhv V1 | BEAT | LONG | Confluenza trend | 60m | 3,0x | 3,38464 | 3,38464 | 2,98212 | 2,27335 | 4,18968 | €136,07 | €408,22 | €48,55 | €0,00 |
| 1H Balanced Short Trend Down Strict V1 | ZEC | SHORT | Confluenza trend | 60m | 3,0x | 461,87761 | 462,08000 | 473,26988 | 613,52742 | 439,09306 | €675,44 | €2.026,32 | €49,98 | €-0,89 |
| Bilanciata 1H V2 | WLD | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,34349 | 0,34349 | 0,35287 | 0,45627 | 0,32475 | €26,53 | €79,60 | €2,17 | €-0,00 |
| Bilanciata 1H V2 | ALLO | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,35543 | 0,35543 | 0,39400 | 0,47213 | 0,27829 | €146,68 | €440,04 | €47,75 | €-0,00 |
| Bilanciata 1H V3 Filtered | WLD | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,34349 | 0,34349 | 0,35287 | 0,45627 | 0,32475 | €23,43 | €70,29 | €1,92 | €-0,00 |
| Bilanciata 1H V3 Filtered | ALLO | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,34255 | 0,34255 | 0,37914 | 0,45502 | 0,26938 | €160,61 | €481,84 | €51,46 | €-0,00 |
| Bilanciata 1H V3 Filtered | ESPORTS | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,02905 | 0,02905 | 0,03254 | 0,03859 | 0,02208 | €142,96 | €428,87 | €51,46 | €-0,00 |
| Bilanciata 1H V3 Filtered | HYPE | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 54,81304 | 54,56300 | 55,99251 | 72,80998 | 52,45408 | €780,21 | €2.340,62 | €50,37 | €10,68 |
| Bilanciata 1H V3 Filtered | ZEC | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 461,87761 | 462,08000 | 473,26988 | 613,52742 | 439,09306 | €707,43 | €2.122,30 | €52,35 | €-0,93 |
| Bilanciata 1H V3 Filtered | SOL | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 73,28834 | 73,52000 | 74,34369 | 97,35134 | 71,17764 | €41,52 | €124,56 | €1,79 | €-0,39 |
| 1H Fast Score 6 75 V1 | ALLO | SHORT | Momentum / breakout | 60m | 3,0x | 0,33713 | 0,33713 | 0,36471 | 0,44782 | 0,29576 | €212,67 | €638,01 | €52,19 | €-0,00 |
| 1H Fast Score 6 75 V1 | BEAT | LONG | Momentum / breakout | 60m | 3,0x | 3,38464 | 3,38464 | 3,07157 | 2,27335 | 3,85425 | €191,12 | €573,36 | €53,03 | €0,00 |
| 1H Fast Score 6 75 No Trend Up V1 | ALLO | SHORT | Momentum / breakout | 60m | 3,0x | 0,33808 | 0,33808 | 0,36389 | 0,44909 | 0,29937 | €218,91 | €656,73 | €50,14 | €-0,00 |
| 1H Fast Score 6 75 No Trend Up V1 | BEAT | LONG | Momentum / breakout | 60m | 3,0x | 3,38464 | 3,38464 | 3,07157 | 2,27335 | 3,85425 | €186,12 | €558,37 | €51,65 | €0,00 |
| 1H Fast Score 6 75 Range Only V1 | ESPORTS | SHORT | Momentum / breakout | 60m | 3,0x | 0,02828 | 0,02828 | 0,03168 | 0,03757 | 0,02319 | €143,01 | €429,04 | €51,48 | €-0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | ALLO | SHORT | Momentum / breakout | 60m | 3,0x | 0,33713 | 0,33713 | 0,36471 | 0,44782 | 0,29576 | €211,20 | €633,59 | €51,83 | €-0,00 |
| 1H Fast Nohigh Cap75 V1 | ALLO | SHORT | Momentum / breakout | 60m | 3,0x | 0,33808 | 0,33808 | 0,36389 | 0,44909 | 0,29937 | €225,73 | €677,19 | €51,70 | €-0,00 |
| 1H Fast Nohigh Cap75 V1 | BEAT | LONG | Momentum / breakout | 60m | 3,0x | 3,34076 | 3,34076 | 3,03225 | 2,24388 | 3,80354 | €187,97 | €563,92 | €52,08 | €0,00 |
| 1H Fast No Pepe V1 | BEAT | LONG | Momentum / breakout | 60m | 3,0x | 3,38464 | 3,38464 | 3,07157 | 2,27335 | 3,85425 | €185,40 | €556,20 | €51,45 | €0,00 |
| 1H Fast Tp2 V1 | ALLO | SHORT | Momentum / breakout | 60m | 3,0x | 0,35543 | 0,35543 | 0,38543 | 0,47213 | 0,29543 | €187,33 | €561,99 | €47,43 | €-0,00 |
| 1H Fast Tp2 V1 | NEAR | SHORT | Momentum / breakout | 60m | 3,0x | 1,67599 | 1,67599 | 1,70517 | 2,22628 | 1,61763 | €25,97 | €77,91 | €1,36 | €-0,00 |
| 1H Fast Tp2 V1 | BEAT | LONG | Momentum / breakout | 60m | 3,0x | 3,38464 | 3,38464 | 3,07157 | 2,27335 | 4,01078 | €8,60 | €25,80 | €2,39 | €0,00 |
| Rapida 1H V3 Filtered | BEAT | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 3,38464 | 3,38464 | 3,07157 | 2,27335 | 3,85425 | €183,89 | €551,67 | €51,03 | €0,00 |
| 1H Fast V3 Cap75 V1 | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,33808 | 0,33808 | 0,36389 | 0,44909 | 0,29937 | €227,32 | €681,96 | €52,06 | €-0,00 |
| 1H Fast V3 Long Only V1 | BEAT | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 3,38464 | 3,38464 | 3,07157 | 2,27335 | 3,85425 | €172,16 | €516,48 | €47,77 | €0,00 |
| 1H Fast V3 No Esports V1 | BEAT | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 3,38464 | 3,38464 | 3,07157 | 2,27335 | 3,85425 | €180,15 | €540,44 | €49,99 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | BEAT | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 3,38464 | 3,38464 | 3,07157 | 2,27335 | 3,85425 | €180,82 | €542,46 | €50,18 | €0,00 |
| Ampia 4H | HYPE | SHORT | Confluenza trend | 240m | 2,0x | 58,36732 | 54,56300 | 61,80927 | 87,25915 | 48,72988 | €424,03 | €848,06 | €50,01 | €55,28 |
| Ampia 4H | TAO | SHORT | Confluenza trend | 240m | 2,0x | 189,05650 | 189,05650 | 197,51338 | 282,63946 | 165,37722 | €558,68 | €1.117,36 | €49,98 | €-0,00 |
| Ampia 4H | XMR | LONG | Confluenza trend | 240m | 2,0x | 364,45854 | 364,45854 | 347,94701 | 184,05156 | 410,69083 | €544,42 | €1.088,84 | €49,33 | €0,00 |
| Ampia 4H | XRP | SHORT | Confluenza trend | 240m | 2,0x | 1,06427 | 1,08535 | 1,09657 | 1,59108 | 0,97382 | €13,35 | €26,70 | €0,81 | €-0,53 |
| Ampia 4H | BTC | SHORT | Confluenza trend | 240m | 2,0x | 63318,66373 | 63957,69000 | 64874,97444 | 94661,40228 | 58960,99415 | €18,28 | €36,56 | €0,90 | €-0,37 |
| Ampia 4H | DOGE | SHORT | Confluenza trend | 240m | 2,0x | 0,07002 | 0,07062 | 0,07288 | 0,10467 | 0,06199 | €17,06 | €34,13 | €1,40 | €-0,29 |
| Ampia 4H | AKE | LONG | Confluenza trend | 240m | 2,0x | 0,00411 | 0,00383 | 0,00361 | 0,00207 | 0,00549 | €199,76 | €399,51 | €47,94 | €-26,74 |
| Forza relativa 1H V1 | ONDO | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,42171 | €891,90 | €1.783,80 | €49,29 | €0,00 |
| Forza relativa 1H V1 | WLD | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,32287 | €14,97 | €29,93 | €0,82 | €-0,00 |
| Forza relativa 1H V1 | NEAR | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 1,70198 | 1,70198 | 1,73908 | 2,54446 | 1,62035 | €112,91 | €225,83 | €4,92 | €-0,00 |
| Forza relativa 1H V1 | HYPE | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 55,31793 | 54,56300 | 55,29611 | 82,70031 | 52,87133 | €1.199,49 | €2.398,97 | €0,00 | €32,74 |
| Forza relativa 1H V1 | BEAT | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 3,34076 | 3,34076 | 2,94410 | 1,68709 | 4,21342 | €200,74 | €401,49 | €47,67 | €0,00 |
| Forza relativa 1H V1 | ZEC | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 461,87761 | 462,08000 | 473,26988 | 690,50702 | 436,81461 | €16,57 | €33,14 | €0,82 | €-0,01 |
| Forza relativa 1H V2 | WLD | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,32287 | €47,70 | €95,39 | €2,60 | €-0,00 |
| Forza relativa 1H V2 | XMR | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 367,08012 | 367,08012 | 360,46822 | 185,37546 | 381,62629 | €1.446,12 | €2.892,24 | €52,10 | €0,00 |
| Forza relativa 1H V2 | ZEC | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 461,87761 | 462,08000 | 473,26988 | 690,50702 | 436,81461 | €1.001,44 | €2.002,88 | €49,40 | €-0,88 |
| Benchmark Donchian breakout 1H | ALLO | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,35678 | 0,35678 | 0,39959 | 0,53338 | 0,24974 | €215,19 | €430,38 | €51,65 | €-0,00 |
| Benchmark Donchian breakout 1H | NEAR | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 1,70198 | 1,70198 | 1,74321 | 2,54446 | 1,59891 | €52,48 | €104,96 | €2,54 | €-0,00 |
| Benchmark Donchian breakout 1H | BTC | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 63620,87328 | 63957,69000 | 64638,80725 | 95113,20555 | 61076,03835 | €1.401,20 | €2.802,39 | €44,84 | €-14,84 |
| Benchmark Donchian breakout 1H | HYPE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 55,15697 | 54,56300 | 56,47572 | 82,45966 | 51,86008 | €1.103,00 | €2.206,00 | €52,74 | €23,76 |
| Donchian 1H Gb20 120R V1 | NEAR | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 1,70198 | 1,70198 | 1,74321 | 2,54446 | 1,59891 | €88,92 | €177,84 | €4,31 | €-0,00 |
| Donchian 1H Gb20 120R V1 | HYPE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 55,15697 | 54,56300 | 56,47572 | 82,45966 | 51,86008 | €1.079,15 | €2.158,31 | €51,60 | €23,24 |
| Benchmark trend following EMA 1H | LAB | LONG | Trend following EMA | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €207,05 | €414,10 | €49,69 | €0,00 |
| Benchmark trend following EMA 1H | ALLO | SHORT | Trend following EMA | 60m | 2,0x | 0,35372 | 0,35372 | 0,39616 | 0,52881 | 0,26034 | €209,15 | €418,30 | €50,20 | €-0,00 |
| Benchmark trend following EMA 1H | XMR | LONG | Trend following EMA | 60m | 2,0x | 367,08012 | 367,08012 | 359,73357 | 185,37546 | 383,24253 | €17,91 | €35,83 | €0,72 | €0,00 |
| Benchmark trend following EMA 1H | NEAR | SHORT | Trend following EMA | 60m | 2,0x | 1,73096 | 1,73096 | 1,69735 | 2,58779 | 1,64780 | €22,55 | €45,10 | €0,00 | €-0,00 |
| Benchmark trend following EMA 1H | HYPE | SHORT | Trend following EMA | 60m | 2,0x | 55,41391 | 54,56300 | 56,77767 | 82,84380 | 52,41364 | €13,15 | €26,30 | €0,65 | €0,40 |
| Benchmark trend following EMA 1H | ZEC | SHORT | Trend following EMA | 60m | 2,0x | 469,96599 | 462,08000 | 461,84959 | 702,59915 | 442,94188 | €842,70 | €1.685,39 | €0,00 | €28,28 |
| Benchmark trend following EMA 1H | SOL | SHORT | Trend following EMA | 60m | 2,0x | 73,28834 | 73,52000 | 74,46095 | 109,56607 | 70,70859 | €32,26 | €64,53 | €1,03 | €-0,20 |
| Scanner Top 5 Long 1H | XMR | LONG | Scanner Top 5 Long | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10712 | €70,71 | €141,42 | €2,58 | €0,00 |
| Scanner Bottom 5 Short 1H | ALLO | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,36179 | 0,36179 | 0,40521 | 0,54088 | 0,27496 | €202,53 | €405,06 | €48,61 | €-0,00 |
| Scanner Bottom 5 Short 1H | ESPORTS | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,03342 | 0,03342 | 0,03342 | 0,04997 | 0,02540 | €202,66 | €405,32 | €0,00 | €-0,00 |
| Scanner Bottom 5 Short 1H | NEAR | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1,70198 | 1,70198 | 1,73908 | 2,54446 | 1,62777 | €17,87 | €35,75 | €0,78 | €-0,00 |
| Scanner Bottom 5 Short 1H | BTC | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 63294,93848 | 63957,69000 | 64206,38559 | 94625,93303 | 61472,04425 | €1.726,79 | €3.453,57 | €49,73 | €-36,16 |
| Scanner Bottom 5 Short 1H | HYPE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 55,31793 | 54,56300 | 55,05561 | 82,70031 | 53,09375 | €1.175,62 | €2.351,23 | €0,00 | €32,09 |
| Scanner Bottom 5 Short 1H | SOL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 73,28834 | 73,52000 | 74,34369 | 109,56607 | 71,17764 | €41,16 | €82,32 | €1,19 | €-0,26 |
| Scanner Top10 Long | XMR | LONG | Scanner Top10 Long | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10712 | €1.371,36 | €2.742,71 | €50,02 | €0,00 |
| Scanner Top10 Long | SHIB | LONG | Scanner Top10 Long | 60m | 2,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €24,14 | €48,29 | €2,71 | €0,00 |
| Scanner Bottom10 Short | ALLO | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,35250 | 0,35250 | 0,39075 | 0,52699 | 0,27600 | €224,69 | €449,38 | €48,76 | €-0,00 |
| Scanner Bottom10 Short | ESPORTS | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,03342 | 0,03342 | 0,03342 | 0,04997 | 0,02540 | €203,44 | €406,87 | €0,00 | €-0,00 |
| Scanner Bottom10 Short | NEAR | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 1,70198 | 1,70198 | 1,73908 | 2,54446 | 1,62777 | €17,73 | €35,46 | €0,77 | €-0,00 |
| Scanner Bottom10 Short | BTC | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 63364,29461 | 63957,69000 | 64276,74045 | 94729,62044 | 61539,40292 | €28,28 | €56,57 | €0,81 | €-0,53 |
| Scanner Bottom10 Short | HYPE | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 54,80404 | 54,56300 | 55,95929 | 81,93204 | 52,49353 | €15,67 | €31,35 | €0,66 | €0,14 |
| Scanner Top15 Long | XMR | LONG | Scanner Top15 Long | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10712 | €1.371,36 | €2.742,71 | €50,02 | €0,00 |
| Scanner Top15 Long | SHIB | LONG | Scanner Top15 Long | 60m | 2,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €24,14 | €48,29 | €2,71 | €0,00 |
| Scanner Bottom15 Short | ALLO | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,35250 | 0,35250 | 0,39075 | 0,52699 | 0,27600 | €224,69 | €449,38 | €48,76 | €-0,00 |
| Scanner Bottom15 Short | ESPORTS | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,03342 | 0,03342 | 0,03342 | 0,04997 | 0,02540 | €203,44 | €406,87 | €0,00 | €-0,00 |
| Scanner Bottom15 Short | NEAR | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 1,70198 | 1,70198 | 1,73908 | 2,54446 | 1,62777 | €17,73 | €35,46 | €0,77 | €-0,00 |
| Scanner Bottom15 Short | BTC | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 63364,29461 | 63957,69000 | 64276,74045 | 94729,62044 | 61539,40292 | €28,28 | €56,57 | €0,81 | €-0,53 |
| Scanner Bottom15 Short | HYPE | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 54,80404 | 54,56300 | 55,95929 | 81,93204 | 52,49353 | €15,67 | €31,35 | €0,66 | €0,14 |
| Scanner Top20 Long | XMR | LONG | Scanner Top20 Long | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10712 | €1.371,36 | €2.742,71 | €50,02 | €0,00 |
| Scanner Top20 Long | SHIB | LONG | Scanner Top20 Long | 60m | 2,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €24,14 | €48,29 | €2,71 | €0,00 |
| Scanner Bottom20 Short | ALLO | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,35250 | 0,35250 | 0,39075 | 0,52699 | 0,27600 | €224,69 | €449,38 | €48,76 | €-0,00 |
| Scanner Bottom20 Short | ESPORTS | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,03342 | 0,03342 | 0,03342 | 0,04997 | 0,02540 | €203,44 | €406,87 | €0,00 | €-0,00 |
| Scanner Bottom20 Short | NEAR | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 1,70198 | 1,70198 | 1,73908 | 2,54446 | 1,62777 | €17,73 | €35,46 | €0,77 | €-0,00 |
| Scanner Bottom20 Short | BTC | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 63364,29461 | 63957,69000 | 64276,74045 | 94729,62044 | 61539,40292 | €28,28 | €56,57 | €0,81 | €-0,53 |
| Scanner Bottom20 Short | HYPE | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 54,80404 | 54,56300 | 55,95929 | 81,93204 | 52,49353 | €15,67 | €31,35 | €0,66 | €0,14 |
| Scanner Top 5 + forza BTC 1H | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 381,44484 | €37,16 | €74,32 | €1,36 | €0,00 |
| Scanner Top5 Btc Mfe V1 | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 367,08012 | 367,08012 | 360,46822 | 185,37546 | 381,62629 | €1.363,71 | €2.727,43 | €49,13 | €0,00 |
| Scanner Top5 Btc Btc Le3 V1 | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 381,44484 | €37,63 | €75,26 | €1,37 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 386,79573 | €70,70 | €141,40 | €2,58 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 386,79573 | €85,15 | €170,29 | €3,11 | €0,00 |
| Global Confluence puro 1H | DOGE | SHORT | Global Confluence puro | 60m | 2,0x | 0,07008 | 0,07062 | 0,07120 | 0,10476 | 0,06727 | €1.529,14 | €3.058,29 | €48,93 | €-23,74 |
| Combo Trend | ALLO | SHORT | Combo Trend | 60m | 2,0x | 0,35372 | 0,35372 | 0,39616 | 0,52881 | 0,26034 | €209,35 | €418,70 | €50,24 | €-0,00 |
| Combo Trend | NEAR | SHORT | Combo Trend | 60m | 2,0x | 1,73096 | 1,73096 | 1,69735 | 2,58779 | 1,64780 | €26,55 | €53,10 | €0,00 | €-0,00 |
| Combo Trend | SUI | SHORT | Combo Trend | 60m | 2,0x | 0,67989 | 0,67989 | 0,69410 | 1,01644 | 0,64864 | €67,05 | €134,10 | €2,80 | €-0,00 |
| Combo Trend | ZEC | SHORT | Combo Trend | 60m | 2,0x | 469,96599 | 462,08000 | 461,84959 | 702,59915 | 442,94188 | €907,09 | €1.814,17 | €0,00 | €30,44 |
| Combo Trend | HYPE | SHORT | Combo Trend | 60m | 2,0x | 54,80404 | 54,56300 | 56,08765 | 81,93204 | 51,98009 | €1.015,43 | €2.030,86 | €47,57 | €8,93 |
| Combo Trend | DOGE | SHORT | Combo Trend | 60m | 2,0x | 0,07008 | 0,07062 | 0,07120 | 0,10476 | 0,06761 | €1.282,62 | €2.565,24 | €41,04 | €-19,91 |
| Combo Scanner | XMR | LONG | Combo Scanner | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 381,44484 | €23,89 | €47,78 | €0,87 | €0,00 |
| Combo Adaptive | WLD | SHORT | Combo Adaptive | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,32475 | €929,60 | €1.859,20 | €50,73 | €-0,00 |
| Combo Adaptive | ALLO | SHORT | Combo Adaptive | 60m | 2,0x | 0,36179 | 0,36179 | 0,40521 | 0,54088 | 0,27496 | €210,64 | €421,27 | €50,55 | €-0,00 |
| Combo Adaptive | NEAR | SHORT | Combo Adaptive | 60m | 2,0x | 1,67499 | 1,67499 | 1,71358 | 2,50412 | 1,59783 | €28,25 | €56,50 | €1,30 | €-0,00 |
| Combo Adaptive | HYPE | SHORT | Combo Adaptive | 60m | 2,0x | 54,80404 | 54,56300 | 55,95929 | 81,93204 | 52,49353 | €37,18 | €74,35 | €1,57 | €0,33 |
| Combo Adaptive Mfe Trail | WLD | SHORT | Combo Adaptive | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,32475 | €883,78 | €1.767,56 | €48,23 | €-0,00 |
| Combo Adaptive Quality7 V1 | WLD | SHORT | Combo Adaptive | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,32475 | €919,99 | €1.839,97 | €50,21 | €-0,00 |
| Combo Adaptive Quality7 V1 | ALLO | SHORT | Combo Adaptive | 60m | 2,0x | 0,36179 | 0,36179 | 0,40521 | 0,54088 | 0,27496 | €207,61 | €415,23 | €49,83 | €-0,00 |
| Combo Adaptive Quality7 V1 | HYPE | SHORT | Combo Adaptive | 60m | 2,0x | 54,81304 | 54,56300 | 55,99251 | 81,94549 | 52,45408 | €1.166,31 | €2.332,62 | €50,19 | €10,64 |
| Combo Adaptive Long Only V1 | XMR | LONG | Combo Adaptive | 60m | 2,0x | 367,08012 | 367,08012 | 360,46822 | 185,37546 | 380,30391 | €1.384,19 | €2.768,37 | €49,86 | €0,00 |
| Combo Adaptive Long Only V1 | SHIB | LONG | Combo Adaptive | 60m | 2,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €12,85 | €25,69 | €1,44 | €0,00 |
| Combo Adaptive Partial 1R V1 | WLD | SHORT | Combo Adaptive | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,32475 | €895,30 | €1.790,60 | €48,86 | €-0,00 |
| Combo Adaptive Partial 1R V1 | ALLO | SHORT | Combo Adaptive | 60m | 2,0x | 0,36179 | 0,36179 | 0,40521 | 0,54088 | 0,27496 | €98,69 | €197,38 | €23,69 | €-0,00 |
| Combo Adaptive Partial 1R V1 | HYPE | SHORT | Combo Adaptive | 60m | 2,0x | 54,81304 | 54,56300 | 55,99251 | 81,94549 | 52,45408 | €1.130,49 | €2.260,99 | €48,65 | €10,31 |
| Combo Adaptive Runner25 V1 | WLD | SHORT | Combo Adaptive | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,31537 | €919,67 | €1.839,35 | €50,19 | €-0,00 |
| Combo Adaptive Runner25 V1 | XMR | LONG | Combo Adaptive | 60m | 2,0x | 367,08012 | 367,08012 | 360,46822 | 185,37546 | 386,91580 | €27,35 | €54,70 | €0,99 | €0,00 |
| Combo Adaptive Runner25 V1 | ALLO | SHORT | Combo Adaptive | 60m | 2,0x | 0,36179 | 0,36179 | 0,40521 | 0,54088 | 0,23155 | €207,78 | €415,57 | €49,87 | €-0,00 |
| Combo Adaptive Runner25 V1 | NEAR | SHORT | Combo Adaptive | 60m | 2,0x | 1,67499 | 1,67499 | 1,71358 | 2,50412 | 1,55924 | €28,88 | €57,76 | €1,33 | €-0,00 |
| Combo Adaptive Runner25 V1 | HYPE | SHORT | Combo Adaptive | 60m | 2,0x | 54,81304 | 54,56300 | 55,99251 | 81,94549 | 51,27460 | €1.151,04 | €2.302,07 | €49,54 | €10,50 |
| Combo Adaptive Tp3 V1 | WLD | SHORT | Combo Adaptive | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,31537 | €911,80 | €1.823,59 | €49,76 | €-0,00 |
| Combo Adaptive Tp3 V1 | ALLO | SHORT | Combo Adaptive | 60m | 2,0x | 0,36179 | 0,36179 | 0,40521 | 0,54088 | 0,23155 | €205,00 | €410,00 | €49,20 | €-0,00 |
| Combo Adaptive Tp3 V1 | HYPE | SHORT | Combo Adaptive | 60m | 2,0x | 54,80404 | 54,56300 | 55,95929 | 81,93204 | 51,33828 | €1.162,02 | €2.324,05 | €48,99 | €10,22 |
| Btc Ema 1H | BTC | SHORT | Trend following EMA | 60m | 3,0x | 63620,87328 | 63957,69000 | 64537,01386 | 84509,72667 | 61788,59213 | €1.147,21 | €3.441,62 | €49,56 | €-18,22 |
| Btc Donchian 4H | BTC | SHORT | Donchian breakout 20 barre | 240m | 2,0x | 63318,66373 | 63957,69000 | 64635,54187 | 94661,40228 | 59631,40456 | €1.196,13 | €2.392,26 | €49,75 | €-24,14 |
| Btc Adaptive 1H | BTC | SHORT | Combo Adaptive | 60m | 3,0x | 63620,87328 | 63957,69000 | 64537,01386 | 84509,72667 | 61788,59213 | €1.158,94 | €3.476,83 | €50,07 | €-18,41 |
| Sol Ema 1H | SOL | SHORT | Trend following EMA | 60m | 3,0x | 73,28834 | 73,52000 | 74,34369 | 97,35134 | 71,17764 | €1.148,42 | €3.445,25 | €49,61 | €-10,89 |
| Sol Ema 4H | SOL | SHORT | Trend following EMA | 240m | 2,0x | 73,19036 | 73,52000 | 75,51123 | 109,41959 | 67,38819 | €780,22 | €1.560,44 | €49,48 | €-7,03 |
| Master Adaptive V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10713 | €21,54 | €43,08 | €0,79 | €0,00 |
| Master Adaptive No Alt V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10713 | €21,54 | €43,08 | €0,79 | €0,00 |
| Master Adaptive Strict3 V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10713 | €1.330,61 | €2.661,21 | €48,54 | €0,00 |
| Master Adaptive Expanded V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10713 | €33,54 | €67,08 | €1,22 | €0,00 |
| Master Adaptive Gb20 V1 | RIF | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,10582 | 0,10582 | 0,09312 | 0,05344 | 0,13122 | €201,89 | €403,77 | €48,45 | €0,00 |
| Master Adaptive Gb20 V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 367,08012 | 367,08012 | 360,46822 | 185,37546 | 380,30391 | €1.348,01 | €2.696,02 | €48,56 | €0,00 |
| Master Adaptive Runner25 V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 386,79573 | €20,87 | €41,74 | €0,76 | €0,00 |
| Combo Adaptive Side Regime Guard V1 | ALLO | SHORT | Combo Adaptive | 60m | 2,0x | 0,35250 | 0,35250 | 0,39075 | 0,52699 | 0,27600 | €235,86 | €471,72 | €51,19 | €-0,00 |
| Combo Adaptive Side Regime Guard V1 | SHIB | LONG | Combo Adaptive | 60m | 2,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €450,93 | €901,86 | €50,61 | €0,00 |
| Combo Adaptive Side Regime Guard V1 | HYPE | SHORT | Combo Adaptive | 60m | 2,0x | 54,80404 | 54,56300 | 55,95929 | 81,93204 | 52,49353 | €1.215,65 | €2.431,30 | €51,25 | €10,69 |
| Master Adaptive Gb20 Be V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 367,86058 | 367,86058 | 361,23463 | 185,76959 | 381,11249 | €1.403,77 | €2.807,55 | €50,57 | €0,00 |
| Master Adaptive Gb20 Partial V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10713 | €1.376,47 | €2.752,95 | €50,21 | €0,00 |
| Master Adaptive Gb20 Loss Cap V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 361,71345 | 185,19860 | 380,10713 | €1.835,86 | €3.671,71 | €50,22 | €0,00 |
| Master Adaptive Gb20 Loss Cap V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00406 | 0,00383 | 0,00357 | 0,00205 | 0,00536 | €207,77 | €415,53 | €49,86 | €-23,61 |
| 1H Fast V3 Nohigh Range Only V1 | ESPORTS | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,02828 | 0,02828 | 0,03168 | 0,03757 | 0,02319 | €142,68 | €428,04 | €51,37 | €-0,00 |
| Main Side Regime Guard V1 | ALLO | SHORT | Confluenza trend | 240m | 3,0x | 0,38070 | 0,38070 | 0,37357 | 0,50570 | 0,28933 | €140,03 | €420,08 | €0,00 | €-0,00 |
| Main Side Regime Guard V1 | DOGE | SHORT | Confluenza trend | 240m | 3,0x | 0,07018 | 0,07062 | 0,07254 | 0,09322 | 0,06545 | €501,87 | €1.505,61 | €50,72 | €-9,53 |
| Main Side Regime Guard V1 | ZEC | SHORT | Confluenza trend | 240m | 3,0x | 469,12616 | 462,08000 | 492,16341 | 623,15591 | 423,05164 | €346,80 | €1.040,39 | €51,09 | €15,63 |
| Main Side Regime Guard V1 | HYPE | SHORT | Confluenza trend | 240m | 3,0x | 55,30294 | 54,56300 | 57,64134 | 73,46073 | 50,62613 | €401,28 | €1.203,85 | €50,90 | €16,11 |
| Main Dynamic Asset Selector V1 | AKE | LONG | Confluenza trend | 240m | 3,0x | 0,00411 | 0,00383 | 0,00361 | 0,00276 | 0,00509 | €142,81 | €428,44 | €51,41 | €-28,67 |
| Combo Trend Side Regime Guard V1 | ALLO | SHORT | Combo Trend | 60m | 2,0x | 0,35250 | 0,35250 | 0,39480 | 0,52699 | 0,25944 | €209,77 | €419,55 | €50,35 | €-0,00 |
| Combo Trend Side Regime Guard V1 | ESPORTS | SHORT | Combo Trend | 60m | 2,0x | 0,02845 | 0,02845 | 0,03187 | 0,04254 | 0,02094 | €202,36 | €404,73 | €48,57 | €-0,00 |
| Combo Trend Side Regime Guard V1 | BTC | SHORT | Combo Trend | 60m | 2,0x | 63620,87328 | 63957,69000 | 64638,80725 | 95113,20555 | 61381,41854 | €1.578,90 | €3.157,81 | €50,52 | €-16,72 |
| Combo Trend Side Regime Guard V1 | ZEC | SHORT | Combo Trend | 60m | 2,0x | 473,90520 | 462,08000 | 461,70335 | 708,48827 | 447,10337 | €41,28 | €82,56 | €0,00 | €2,06 |
| Combo Trend Side Regime Guard V1 | HYPE | SHORT | Combo Trend | 60m | 2,0x | 54,80404 | 54,56300 | 56,08765 | 81,93204 | 51,98009 | €1.059,16 | €2.118,31 | €49,61 | €9,32 |
| 1H Fast Nohigh Cap75 Short Only V1 | ALLO | SHORT | Momentum / breakout | 60m | 3,0x | 0,33808 | 0,33808 | 0,36389 | 0,44909 | 0,29937 | €212,58 | €637,75 | €48,69 | €-0,00 |
| 1H Fast Nohigh Cap75 Short Only V1 | BEAT | LONG | Momentum / breakout | 60m | 3,0x | 3,34076 | 3,34076 | 3,03225 | 2,24388 | 3,80354 | €183,30 | €549,89 | €50,78 | €0,00 |
| 1H Balanced V3 Long Only V1 | XMR | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 366,72991 | 366,72991 | 360,04130 | 246,32025 | 380,10712 | €913,56 | €2.740,69 | €49,99 | €0,00 |
| 1H Balanced V3 Long Only V1 | ALLO | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,34255 | 0,34255 | 0,37914 | 0,45502 | 0,26938 | €156,01 | €468,04 | €49,99 | €-0,00 |
| 1H Balanced V3 Long Only V1 | ESPORTS | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,03342 | 0,03342 | 0,03342 | 0,04440 | 0,02540 | €137,40 | €412,21 | €0,00 | €-0,00 |
| 1H Balanced V3 Long Only V1 | ZEC | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 461,87761 | 462,08000 | 473,26988 | 613,52742 | 439,09306 | €664,50 | €1.993,49 | €49,17 | €-0,87 |
| Scanner Bottom5 Short Profit Lock V1 | WLD | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,34449 | 0,34449 | 0,35368 | 0,51502 | 0,32613 | €937,87 | €1.875,74 | €50,00 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | ALLO | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,35250 | 0,35250 | 0,39075 | 0,52699 | 0,27600 | €227,60 | €455,20 | €49,39 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | ESPORTS | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,03342 | 0,03342 | 0,03262 | 0,04997 | 0,02540 | €206,07 | €412,14 | €0,00 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | NEAR | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1,70198 | 1,70198 | 1,69456 | 2,54446 | 1,62777 | €18,15 | €36,30 | €0,00 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | BTC | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 63294,93848 | 63957,69000 | 64206,38559 | 94625,93303 | 61472,04425 | €1.647,88 | €3.295,77 | €47,46 | €-34,51 |
| Scanner Bottom5 Short Profit Lock V1 | PEPE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €59,89 | €119,78 | €0,00 | €2,63 |
| Scanner Bottom5 Short Mfe Trail V1 | WLD | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,34449 | 0,34449 | 0,35368 | 0,51502 | 0,32613 | €937,87 | €1.875,74 | €50,00 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | ALLO | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,35653 | 0,35653 | 0,39522 | 0,53301 | 0,27915 | €228,22 | €456,45 | €49,53 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | ESPORTS | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,02828 | 0,02828 | 0,03168 | 0,04229 | 0,02150 | €206,75 | €413,50 | €49,62 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | NEAR | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1,70198 | 1,70198 | 1,69456 | 2,54446 | 1,62777 | €15,45 | €30,90 | €0,00 | €-0,00 |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | BEAT | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 3,38464 | 3,38464 | 3,07157 | 2,27335 | 4,16732 | €187,44 | €562,31 | €52,01 | €0,00 |
| Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,35250 | 0,35250 | 0,38225 | 0,46824 | 0,29300 | €194,51 | €583,53 | €49,25 | €-0,00 |
| Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | ESPORTS | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,02998 | 0,02998 | 0,02998 | 0,03983 | 0,02279 | €132,90 | €398,69 | €0,00 | €-0,00 |
| Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | ESPORTS | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,02828 | 0,02828 | 0,03168 | 0,03757 | 0,02150 | €141,08 | €423,23 | €50,79 | €-0,00 |
| Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,35250 | 0,35250 | 0,38225 | 0,46824 | 0,29300 | €190,72 | €572,15 | €48,29 | €-0,00 |
| Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | BEAT | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 3,38464 | 3,38464 | 3,07157 | 2,27335 | 4,01078 | €15,38 | €46,14 | €4,27 | €0,00 |
| Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | BEAT | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 3,38464 | 3,38464 | 3,07157 | 2,27335 | 4,16732 | €184,02 | €552,07 | €51,07 | €0,00 |
| Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,33808 | 0,33808 | 0,36389 | 0,44909 | 0,28646 | €211,10 | €633,31 | €48,35 | €-0,00 |
| Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | NEAR | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,66900 | 1,66900 | 1,69806 | 2,21699 | 1,61088 | €52,00 | €156,00 | €2,72 | €-0,00 |
| Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | BEAT | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 3,38464 | 3,38464 | 3,07157 | 2,27335 | 4,01078 | €177,16 | €531,47 | €49,16 | €0,00 |
| Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | BEAT | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 3,38464 | 3,38464 | 3,07157 | 2,27335 | 4,01078 | €182,35 | €547,06 | €50,60 | €0,00 |
| Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,35250 | 0,35250 | 0,38225 | 0,46824 | 0,29300 | €194,51 | €583,53 | €49,25 | €-0,00 |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,33713 | 0,33713 | 0,36471 | 0,44782 | 0,28197 | €208,24 | €624,73 | €51,11 | €-0,00 |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | ESPORTS | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,03070 | 0,03070 | 0,03070 | 0,04078 | 0,02333 | €138,06 | €414,17 | €0,00 | €-0,00 |
| Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,35250 | 0,35250 | 0,38225 | 0,46824 | 0,29300 | €200,65 | €601,96 | €50,80 | €-0,00 |
| Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | ESPORTS | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,03342 | 0,03342 | 0,03342 | 0,04440 | 0,02540 | €136,12 | €408,37 | €0,00 | €-0,00 |
| Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | BEAT | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 3,38464 | 3,38464 | 3,07157 | 2,27335 | 4,16732 | €174,53 | €523,60 | €48,43 | €0,00 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Scanner Bottom 5 Short 1H | ZEC | SHORT | 2026-07-29T04:53:40+00:00 | 461,34987 | €1,91 | 0,73 | STOP |
| Scanner Bottom20 Short | ZEC | SHORT | 2026-07-29T04:53:40+00:00 | 461,34987 | €35,13 | 0,73 | STOP |
| Scanner Bottom15 Short | ZEC | SHORT | 2026-07-29T04:53:40+00:00 | 461,34987 | €35,13 | 0,73 | STOP |
| Scanner Bottom10 Short | ZEC | SHORT | 2026-07-29T04:53:40+00:00 | 461,34987 | €35,13 | 0,73 | STOP |
| Combo Adaptive Tp3 V1 | ZEC | SHORT | 2026-07-29T04:53:40+00:00 | 460,75778 | €38,41 | 0,78 | STOP |
| Combo Adaptive Side Regime Guard V1 | ZEC | SHORT | 2026-07-29T04:53:40+00:00 | 460,75778 | €39,96 | 0,78 | STOP |
| Combo Adaptive Runner25 V1 | ZEC | SHORT | 2026-07-29T04:53:40+00:00 | 460,75778 | €37,16 | 0,78 | STOP |
| Combo Adaptive Partial 1R V1 | ZEC | SHORT | 2026-07-29T04:53:40+00:00 | 460,63101 | €46,70 | 0,97 | STOP |
| Combo Adaptive | ZEC | SHORT | 2026-07-29T04:53:40+00:00 | 460,75778 | €39,06 | 0,78 | STOP |
| 1H Fast V3 No Esports V1 | ZEC | SHORT | 2026-07-29T04:53:40+00:00 | 460,51046 | €4,53 | 0,09 | STOP |
| 1H Fast V3 No Esports Stress Guard V1 | ZEC | SHORT | 2026-07-29T04:53:40+00:00 | 460,51046 | €4,62 | 0,09 | STOP |
| 1H Fast V3 No Esports Mfe Lock V1 | ZEC | SHORT | 2026-07-29T04:53:40+00:00 | 460,51046 | €4,65 | 0,09 | STOP |

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

Generato: 2026-07-29 05:15 UTC


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

Segnali totali salvati: **63**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-07-29 | BTC | 63.913,12 | +2 | +4 | +3 | +3 | -2 | -1 | 0 | HOLD / ATTESA CONFERME |
| 2026-07-29 | DOGE | 0.07061 | +1 | +4 | +3 | +2 | -2 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-07-29 | SOL | 73,48 | 0 | +4 | +3 | +3 | -3 | -1 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-07-28 | BTC | 63.381,14 | -1 | +3 | +2 | +2 | -2 | -1 | 0 | NON INSEGUIRE / RIDUCI RISCHIO |
| 2026-07-28 | DOGE | 0.06994 | +1 | +4 | +3 | +2 | -3 | -1 | 0 | STAI ALLA FINESTRA |
| 2026-07-28 | SOL | 73,27 | +1 | +4 | +3 | +3 | -3 | -1 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-07-27 | BTC | 65.325,99 | +5 | +4 | +3 | +3 | 0 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-07-27 | DOGE | 0.07289 | 0 | +3 | +2 | +2 | -3 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-07-27 | SOL | 76,40 | 0 | +4 | +3 | +2 | -3 | -1 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-07-26 | BTC | 64.454,23 | +5 | +4 | +3 | +2 | +1 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-07-26 | DOGE | 0.07344 | +2 | +3 | +2 | +2 | -2 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-07-26 | SOL | 75,10 | 0 | +4 | +3 | +2 | -3 | -1 | 0 | HOLD LEGGERO / ATTESA CONFERME |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 21 | 20 | 19 | 18 | 16 | 14 | 11 | 7 | 0 | 0 | 0 | 0 |
| SOL | 21 | 20 | 19 | 18 | 16 | 14 | 11 | 7 | 0 | 0 | 0 | 0 |
| DOGE | 21 | 20 | 19 | 18 | 16 | 14 | 11 | 7 | 0 | 0 | 0 | 0 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-07-09 | 21g | 2026-07-30 | domani |
| SOL | 2026-07-09 | 21g | 2026-07-30 | domani |
| DOGE | 2026-07-09 | 21g | 2026-07-30 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 18 | 38,89% | +0,03% | -0,04% | FEEDBACK RAPIDO |
| BTC | 2g | 17 | 41,18% | +0,08% | -0,09% | FEEDBACK RAPIDO |
| BTC | 3g | 16 | 37,50% | +0,00% | -0,25% | FEEDBACK RAPIDO |
| BTC | 5g | 14 | 28,57% | +0,39% | -0,51% | FEEDBACK RAPIDO |
| BTC | 7g | 13 | 46,15% | +0,85% | +0,12% | FEEDBACK RAPIDO |
| BTC | 10g | 10 | 60,00% | +1,89% | +1,23% | FEEDBACK RAPIDO |
| BTC | 14g | 7 | 85,71% | +1,60% | +1,60% | FEEDBACK RAPIDO |
| BTC | 21g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 30g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 1g | 15 | 46,67% | -0,16% | -0,63% | FEEDBACK RAPIDO |
| SOL | 2g | 14 | 21,43% | -0,41% | -1,09% | FEEDBACK RAPIDO |
| SOL | 3g | 14 | 14,29% | -0,64% | -1,49% | FEEDBACK RAPIDO |
| SOL | 5g | 14 | 35,71% | -1,05% | -1,42% | FEEDBACK RAPIDO |
| SOL | 7g | 13 | 46,15% | -1,07% | -0,82% | FEEDBACK RAPIDO |
| SOL | 10g | 10 | 40,00% | -0,76% | -0,51% | FEEDBACK RAPIDO |
| SOL | 14g | 6 | 33,33% | -2,51% | -1,18% | FEEDBACK RAPIDO |
| SOL | 21g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 30g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 1g | 19 | 52,63% | -0,01% | +0,03% | FEEDBACK RAPIDO |
| DOGE | 2g | 18 | 50,00% | -0,26% | -0,27% | FEEDBACK RAPIDO |
| DOGE | 3g | 18 | 44,44% | -0,53% | +0,10% | FEEDBACK RAPIDO |
| DOGE | 5g | 16 | 62,50% | -0,80% | +0,80% | FEEDBACK RAPIDO |
| DOGE | 7g | 14 | 71,43% | -1,38% | +1,38% | FEEDBACK RAPIDO |
| DOGE | 10g | 11 | 63,64% | -1,72% | +1,72% | FEEDBACK RAPIDO |
| DOGE | 14g | 7 | 71,43% | -2,73% | +2,73% | FEEDBACK RAPIDO |
| DOGE | 21g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 30g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 18 | 38,89% | +0,03% | -0,04% | -0,25% | +0,63% | FEEDBACK RAPIDO |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 20 | 45,00% | -0,00% | -0,00% | -0,27% | +0,55% | FEEDBACK RAPIDO |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 20 | 45,00% | -0,00% | -0,00% | -0,27% | +0,55% | FEEDBACK RAPIDO |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 16 | 43,75% | -0,07% | -0,07% | -0,35% | +0,41% | FEEDBACK RAPIDO |
| BTC | 1g | Tecnico | CALIBRABILE | 16 | 37,50% | +0,17% | -0,46% | -0,12% | +0,70% | FEEDBACK RAPIDO |
| BTC | 1g | Classic technical | CALIBRABILE | 1 | 0,00% | +0,84% | -0,84% | +0,30% | +1,01% | FEEDBACK RAPIDO |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +2,00% | +2,00% | +1,48% | +2,25% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 17 | 41,18% | +0,08% | -0,09% | -0,46% | +0,91% | FEEDBACK RAPIDO |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 19 | 42,11% | +0,03% | +0,03% | -0,47% | +0,84% | FEEDBACK RAPIDO |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 19 | 42,11% | +0,03% | +0,03% | -0,47% | +0,84% | FEEDBACK RAPIDO |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 15 | 40,00% | -0,15% | -0,15% | -0,68% | +0,68% | FEEDBACK RAPIDO |
| BTC | 2g | Tecnico | CALIBRABILE | 15 | 40,00% | +0,29% | -0,44% | -0,24% | +1,10% | FEEDBACK RAPIDO |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +3,18% | +3,18% | +3,05% | +3,89% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 16 | 37,50% | +0,00% | -0,25% | -1,37% | +2,05% | FEEDBACK RAPIDO |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 18 | 55,56% | +0,14% | +0,14% | -1,32% | +1,97% | FEEDBACK RAPIDO |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 18 | 55,56% | +0,14% | +0,14% | -1,32% | +1,97% | FEEDBACK RAPIDO |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 14 | 57,14% | +0,13% | +0,13% | -1,36% | +1,88% | FEEDBACK RAPIDO |
| BTC | 3g | Tecnico | CALIBRABILE | 15 | 40,00% | +0,52% | -0,04% | -1,15% | +2,18% | FEEDBACK RAPIDO |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,88% | +1,88% | +1,44% | +4,24% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 14 | 28,57% | +0,39% | -0,51% | -2,21% | +2,60% | FEEDBACK RAPIDO |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 16 | 43,75% | +0,36% | +0,36% | -2,11% | +2,61% | FEEDBACK RAPIDO |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 16 | 43,75% | +0,36% | +0,36% | -2,11% | +2,61% | FEEDBACK RAPIDO |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 12 | 50,00% | +0,66% | +0,66% | -2,11% | +2,68% | FEEDBACK RAPIDO |
| BTC | 5g | Tecnico | CALIBRABILE | 13 | 53,85% | +0,58% | -0,30% | -1,84% | +2,90% | FEEDBACK RAPIDO |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,16% | -0,16% | -0,37% | +4,24% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 13 | 46,15% | +0,85% | +0,12% | -2,23% | +3,30% | FEEDBACK RAPIDO |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 14 | 64,29% | +0,81% | +0,81% | -2,08% | +3,40% | FEEDBACK RAPIDO |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 14 | 64,29% | +0,81% | +0,81% | -2,08% | +3,40% | FEEDBACK RAPIDO |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 10 | 80,00% | +1,68% | +1,68% | -1,90% | +3,81% | FEEDBACK RAPIDO |
| BTC | 7g | Tecnico | CALIBRABILE | 11 | 36,36% | +1,68% | -0,60% | -1,65% | +3,92% | FEEDBACK RAPIDO |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,77% | +1,77% | -0,79% | +4,24% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 10 | 60,00% | +1,89% | +1,23% | -2,07% | +4,34% | FEEDBACK RAPIDO |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 11 | 72,73% | +1,64% | +1,64% | -2,00% | +4,38% | FEEDBACK RAPIDO |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 11 | 72,73% | +1,64% | +1,64% | -2,00% | +4,38% | FEEDBACK RAPIDO |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 10 | 80,00% | +1,94% | +1,94% | -2,01% | +4,48% | FEEDBACK RAPIDO |
| BTC | 10g | Tecnico | CALIBRABILE | 10 | 30,00% | +1,76% | -0,56% | -1,87% | +4,56% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 7 | 85,71% | +1,60% | +1,60% | -2,36% | +5,31% | FEEDBACK RAPIDO |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 7 | 85,71% | +1,60% | +1,60% | -2,36% | +5,31% | FEEDBACK RAPIDO |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 7 | 85,71% | +1,60% | +1,60% | -2,36% | +5,31% | FEEDBACK RAPIDO |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 7 | 85,71% | +1,60% | +1,60% | -2,36% | +5,31% | FEEDBACK RAPIDO |
| BTC | 14g | Tecnico | CALIBRABILE | 6 | 33,33% | +1,49% | -0,12% | -2,20% | +5,40% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 19 | 52,63% | -0,01% | +0,03% | -0,45% | +0,66% | FEEDBACK RAPIDO |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 20 | 55,00% | -0,21% | +0,39% | -0,66% | +0,46% | FEEDBACK RAPIDO |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 20 | 55,00% | -0,21% | +0,39% | -0,66% | +0,46% | FEEDBACK RAPIDO |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 18 | 55,56% | -0,02% | +0,22% | -0,50% | +0,67% | FEEDBACK RAPIDO |
| DOGE | 1g | Tecnico | CALIBRABILE | 20 | 55,00% | -0,21% | +0,21% | -0,66% | +0,46% | FEEDBACK RAPIDO |
| DOGE | 1g | Classic technical | CALIBRABILE | 17 | 47,06% | +0,11% | -0,11% | -0,33% | +0,72% | FEEDBACK RAPIDO |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +3,18% | +3,18% | +1,82% | +3,24% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 18 | 50,00% | -0,26% | -0,27% | -0,92% | +0,88% | FEEDBACK RAPIDO |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 19 | 52,63% | -0,41% | +0,09% | -1,08% | +0,70% | FEEDBACK RAPIDO |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 19 | 52,63% | -0,41% | +0,09% | -1,08% | +0,70% | FEEDBACK RAPIDO |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 17 | 52,94% | -0,60% | +0,25% | -1,20% | +0,63% | FEEDBACK RAPIDO |
| DOGE | 2g | Tecnico | CALIBRABILE | 19 | 57,89% | -0,41% | +0,41% | -1,08% | +0,70% | FEEDBACK RAPIDO |
| DOGE | 2g | Classic technical | CALIBRABILE | 16 | 50,00% | +0,16% | -0,16% | -0,56% | +1,39% | FEEDBACK RAPIDO |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +5,65% | +5,65% | +4,05% | +5,83% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 18 | 44,44% | -0,53% | +0,10% | -2,22% | +2,17% | FEEDBACK RAPIDO |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 18 | 50,00% | -0,53% | +0,17% | -2,22% | +2,17% | FEEDBACK RAPIDO |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 18 | 50,00% | -0,53% | +0,17% | -2,22% | +2,17% | FEEDBACK RAPIDO |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 16 | 56,25% | -1,04% | +0,64% | -2,17% | +1,95% | FEEDBACK RAPIDO |
| DOGE | 3g | Tecnico | CALIBRABILE | 18 | 50,00% | -0,53% | +0,53% | -2,22% | +2,17% | FEEDBACK RAPIDO |
| DOGE | 3g | Classic technical | CALIBRABILE | 16 | 43,75% | -0,22% | +0,22% | -2,05% | +2,42% | FEEDBACK RAPIDO |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +3,13% | +3,13% | +0,09% | +6,33% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 16 | 62,50% | -0,80% | +0,80% | -3,27% | +2,44% | FEEDBACK RAPIDO |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 16 | 62,50% | -0,80% | +0,80% | -3,27% | +2,44% | FEEDBACK RAPIDO |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 16 | 62,50% | -0,80% | +0,80% | -3,27% | +2,44% | FEEDBACK RAPIDO |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 14 | 64,29% | -0,85% | +0,85% | -3,36% | +2,14% | FEEDBACK RAPIDO |
| DOGE | 5g | Tecnico | CALIBRABILE | 16 | 62,50% | -0,80% | +0,80% | -3,27% | +2,44% | FEEDBACK RAPIDO |
| DOGE | 5g | Classic technical | CALIBRABILE | 15 | 60,00% | -0,66% | +0,66% | -3,23% | +2,56% | FEEDBACK RAPIDO |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +2,30% | +2,30% | +0,26% | +6,93% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 14 | 71,43% | -1,38% | +1,38% | -3,98% | +2,27% | FEEDBACK RAPIDO |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 14 | 71,43% | -1,38% | +1,38% | -3,98% | +2,27% | FEEDBACK RAPIDO |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 14 | 71,43% | -1,38% | +1,38% | -3,98% | +2,27% | FEEDBACK RAPIDO |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 14 | 71,43% | -1,38% | +1,38% | -3,98% | +2,27% | FEEDBACK RAPIDO |
| DOGE | 7g | Tecnico | CALIBRABILE | 14 | 71,43% | -1,38% | +1,38% | -3,98% | +2,27% | FEEDBACK RAPIDO |
| DOGE | 7g | Classic technical | CALIBRABILE | 13 | 69,23% | -1,40% | +1,40% | -3,99% | +2,40% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 11 | 63,64% | -1,72% | +1,72% | -4,49% | +2,44% | FEEDBACK RAPIDO |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 11 | 63,64% | -1,72% | +1,72% | -4,49% | +2,44% | FEEDBACK RAPIDO |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 11 | 63,64% | -1,72% | +1,72% | -4,49% | +2,44% | FEEDBACK RAPIDO |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 11 | 63,64% | -1,72% | +1,72% | -4,49% | +2,44% | FEEDBACK RAPIDO |
| DOGE | 10g | Tecnico | CALIBRABILE | 11 | 63,64% | -1,72% | +1,72% | -4,49% | +2,44% | FEEDBACK RAPIDO |
| DOGE | 10g | Classic technical | CALIBRABILE | 10 | 60,00% | -1,29% | +1,29% | -4,23% | +2,64% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 7 | 71,43% | -2,73% | +2,73% | -5,85% | +2,82% | FEEDBACK RAPIDO |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 7 | 71,43% | -2,73% | +2,73% | -5,85% | +2,82% | FEEDBACK RAPIDO |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 7 | 71,43% | -2,73% | +2,73% | -5,85% | +2,82% | FEEDBACK RAPIDO |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 7 | 71,43% | -2,73% | +2,73% | -5,85% | +2,82% | FEEDBACK RAPIDO |
| DOGE | 14g | Tecnico | CALIBRABILE | 7 | 71,43% | -2,73% | +2,73% | -5,85% | +2,82% | FEEDBACK RAPIDO |
| DOGE | 14g | Classic technical | CALIBRABILE | 6 | 66,67% | -2,43% | +2,43% | -5,56% | +3,21% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 15 | 46,67% | -0,16% | -0,63% | -0,54% | +0,69% | FEEDBACK RAPIDO |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 16 | 62,50% | -0,72% | -0,18% | -1,03% | +0,04% | FEEDBACK RAPIDO |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 19 | 57,89% | -0,44% | -0,33% | -0,81% | +0,33% | FEEDBACK RAPIDO |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 14 | 50,00% | -0,43% | -0,14% | -0,95% | +0,30% | FEEDBACK RAPIDO |
| SOL | 1g | Tecnico | CALIBRABILE | 20 | 55,00% | -0,27% | +0,09% | -0,66% | +0,46% | FEEDBACK RAPIDO |
| SOL | 1g | Classic technical | CALIBRABILE | 12 | 58,33% | -0,22% | +0,22% | -0,61% | +0,37% | FEEDBACK RAPIDO |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,51% | -0,51% | -0,47% | +0,31% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 14 | 21,43% | -0,41% | -1,09% | -1,02% | +0,84% | FEEDBACK RAPIDO |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 15 | 40,00% | -0,99% | -0,68% | -1,69% | -0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 18 | 38,89% | -0,76% | -0,62% | -1,41% | +0,44% | FEEDBACK RAPIDO |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 13 | 30,77% | -0,94% | -0,86% | -1,63% | +0,40% | FEEDBACK RAPIDO |
| SOL | 2g | Tecnico | CALIBRABILE | 19 | 42,11% | -0,60% | -0,00% | -1,21% | +0,59% | FEEDBACK RAPIDO |
| SOL | 2g | Classic technical | CALIBRABILE | 11 | 54,55% | -0,37% | +0,37% | -0,80% | +0,17% | FEEDBACK RAPIDO |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -1,38% | -1,38% | -1,57% | +0,62% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 14 | 14,29% | -0,64% | -1,49% | -2,30% | +2,00% | FEEDBACK RAPIDO |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 14 | 35,71% | -1,11% | -0,56% | -2,85% | +1,68% | FEEDBACK RAPIDO |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 17 | 35,29% | -0,86% | -0,52% | -2,56% | +1,98% | FEEDBACK RAPIDO |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 12 | 33,33% | -0,98% | -1,14% | -2,58% | +2,10% | FEEDBACK RAPIDO |
| SOL | 3g | Tecnico | CALIBRABILE | 18 | 44,44% | -0,73% | +0,07% | -2,34% | +2,07% | FEEDBACK RAPIDO |
| SOL | 3g | Classic technical | CALIBRABILE | 10 | 40,00% | -0,03% | +0,03% | -2,00% | +2,20% | FEEDBACK RAPIDO |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -3,20% | -3,20% | -3,71% | +0,62% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 14 | 35,71% | -1,05% | -1,42% | -3,34% | +2,55% | FEEDBACK RAPIDO |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 12 | 50,00% | -1,46% | -0,87% | -3,85% | +2,00% | FEEDBACK RAPIDO |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 15 | 46,67% | -1,03% | -0,84% | -3,49% | +2,38% | FEEDBACK RAPIDO |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 10 | 40,00% | -1,95% | -1,21% | -3,70% | +2,25% | FEEDBACK RAPIDO |
| SOL | 5g | Tecnico | CALIBRABILE | 16 | 50,00% | -1,11% | +0,08% | -3,44% | +2,45% | FEEDBACK RAPIDO |
| SOL | 5g | Classic technical | CALIBRABILE | 8 | 62,50% | -0,40% | +0,40% | -2,75% | +2,81% | FEEDBACK RAPIDO |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -3,99% | -3,99% | -6,07% | +0,62% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 13 | 46,15% | -1,07% | -0,82% | -3,87% | +2,94% | FEEDBACK RAPIDO |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 10 | 70,00% | -1,75% | +0,55% | -4,34% | +2,44% | FEEDBACK RAPIDO |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 13 | 69,23% | -1,37% | +0,45% | -3,96% | +2,78% | FEEDBACK RAPIDO |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 8 | 50,00% | -1,24% | -0,98% | -4,13% | +2,74% | FEEDBACK RAPIDO |
| SOL | 7g | Tecnico | CALIBRABILE | 14 | 35,71% | -1,23% | -0,22% | -3,92% | +2,84% | FEEDBACK RAPIDO |
| SOL | 7g | Classic technical | CALIBRABILE | 6 | 50,00% | -0,83% | +0,83% | -3,11% | +3,56% | FEEDBACK RAPIDO |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -6,33% | -6,33% | -6,71% | +0,62% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 10 | 40,00% | -0,76% | -0,51% | -3,93% | +3,35% | FEEDBACK RAPIDO |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 8 | 50,00% | -1,14% | +0,05% | -4,31% | +2,92% | FEEDBACK RAPIDO |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 11 | 45,45% | -0,89% | +0,09% | -4,07% | +3,19% | FEEDBACK RAPIDO |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 7 | 28,57% | -0,68% | -1,47% | -4,21% | +3,09% | FEEDBACK RAPIDO |
| SOL | 10g | Tecnico | CALIBRABILE | 11 | 54,55% | -0,89% | +0,45% | -4,07% | +3,19% | FEEDBACK RAPIDO |
| SOL | 10g | Classic technical | CALIBRABILE | 4 | 75,00% | -1,26% | +1,26% | -3,10% | +4,25% | FEEDBACK RAPIDO |
| SOL | 10g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 14g | Global confluence | BENCHMARK | 6 | 33,33% | -2,51% | -1,18% | -4,69% | +2,76% | FEEDBACK RAPIDO |
| SOL | 14g | Famiglia statistica | CALIBRABILE | 5 | 60,00% | -2,14% | +0,04% | -5,08% | +2,28% | FEEDBACK RAPIDO |
| SOL | 14g | Scanner grezzo | DIAGNOSTICO | 7 | 71,43% | -2,51% | +1,01% | -4,81% | +2,58% | FEEDBACK RAPIDO |
| SOL | 14g | Market regime grezzo | DIAGNOSTICO | 6 | 16,67% | -2,51% | -1,92% | -4,69% | +2,76% | FEEDBACK RAPIDO |
| SOL | 14g | Tecnico | CALIBRABILE | 7 | 28,57% | -2,51% | -0,39% | -4,81% | +2,58% | FEEDBACK RAPIDO |
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

Generato: 2026-07-29 05:15 UTC

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
| BTC | 21 | FEEDBACK RAPIDO | 20 | 0 | 0 | 0 | Famiglia statistica | 1g | 45,00% | -0,00% | feedback rapido: utile da osservare, non da pesare |
| SOL | 21 | FEEDBACK RAPIDO | 20 | 0 | 0 | 0 | Tecnico | 1g | 55,00% | +0,09% | feedback rapido: utile da osservare, non da pesare |
| DOGE | 21 | FEEDBACK RAPIDO | 20 | 0 | 0 | 0 | Famiglia statistica | 1g | 55,00% | +0,39% | feedback rapido: utile da osservare, non da pesare |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Classic technical | 1 | 0,00% | -0,84% | +0,84% | +0,30% | +1,01% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Famiglia statistica | 20 | 45,00% | -0,00% | -0,00% | -0,27% | +0,55% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Microstruttura exchange | 1 | 100,00% | +2,00% | +2,00% | +1,48% | +2,25% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 16 | 37,50% | -0,46% | +0,17% | -0,12% | +0,70% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Famiglia statistica | 19 | 42,11% | +0,03% | +0,03% | -0,47% | +0,84% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Microstruttura exchange | 1 | 100,00% | +3,18% | +3,18% | +3,05% | +3,89% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 15 | 40,00% | -0,44% | +0,29% | -0,24% | +1,10% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Famiglia statistica | 18 | 55,56% | +0,14% | +0,14% | -1,32% | +1,97% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Microstruttura exchange | 1 | 100,00% | +1,88% | +1,88% | +1,44% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 15 | 40,00% | -0,04% | +0,52% | -1,15% | +2,18% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 16 | 43,75% | +0,36% | +0,36% | -2,11% | +2,61% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -0,16% | -0,16% | -0,37% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 13 | 53,85% | -0,30% | +0,58% | -1,84% | +2,90% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 14 | 64,29% | +0,81% | +0,81% | -2,08% | +3,40% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Microstruttura exchange | 1 | 100,00% | +1,77% | +1,77% | -0,79% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 11 | 36,36% | -0,60% | +1,68% | -1,65% | +3,92% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 11 | 72,73% | +1,64% | +1,64% | -2,00% | +4,38% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 10 | 30,00% | -0,56% | +1,76% | -1,87% | +4,56% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Famiglia statistica | 7 | 85,71% | +1,60% | +1,60% | -2,36% | +5,31% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 6 | 33,33% | -0,12% | +1,49% | -2,20% | +5,40% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 17 | 47,06% | -0,11% | +0,11% | -0,33% | +0,72% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Famiglia statistica | 20 | 55,00% | +0,39% | -0,21% | -0,66% | +0,46% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Microstruttura exchange | 2 | 100,00% | +3,18% | +3,18% | +1,82% | +3,24% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 20 | 55,00% | +0,21% | -0,21% | -0,66% | +0,46% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Classic technical | 16 | 50,00% | -0,16% | +0,16% | -0,56% | +1,39% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Famiglia statistica | 19 | 52,63% | +0,09% | -0,41% | -1,08% | +0,70% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Microstruttura exchange | 2 | 100,00% | +5,65% | +5,65% | +4,05% | +5,83% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 19 | 57,89% | +0,41% | -0,41% | -1,08% | +0,70% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Classic technical | 16 | 43,75% | +0,22% | -0,22% | -2,05% | +2,42% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Famiglia statistica | 18 | 50,00% | +0,17% | -0,53% | -2,22% | +2,17% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Microstruttura exchange | 2 | 100,00% | +3,13% | +3,13% | +0,09% | +6,33% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 18 | 50,00% | +0,53% | -0,53% | -2,22% | +2,17% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Classic technical | 15 | 60,00% | +0,66% | -0,66% | -3,23% | +2,56% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 16 | 62,50% | +0,80% | -0,80% | -3,27% | +2,44% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Microstruttura exchange | 1 | 100,00% | +2,30% | +2,30% | +0,26% | +6,93% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 16 | 62,50% | +0,80% | -0,80% | -3,27% | +2,44% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Classic technical | 13 | 69,23% | +1,40% | -1,40% | -3,99% | +2,40% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 14 | 71,43% | +1,38% | -1,38% | -3,98% | +2,27% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 14 | 71,43% | +1,38% | -1,38% | -3,98% | +2,27% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Classic technical | 10 | 60,00% | +1,29% | -1,29% | -4,23% | +2,64% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 11 | 63,64% | +1,72% | -1,72% | -4,49% | +2,44% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 11 | 63,64% | +1,72% | -1,72% | -4,49% | +2,44% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Classic technical | 6 | 66,67% | +2,43% | -2,43% | -5,56% | +3,21% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Famiglia statistica | 7 | 71,43% | +2,73% | -2,73% | -5,85% | +2,82% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 7 | 71,43% | +2,73% | -2,73% | -5,85% | +2,82% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Classic technical | 12 | 58,33% | +0,22% | -0,22% | -0,61% | +0,37% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Famiglia statistica | 16 | 62,50% | -0,18% | -0,72% | -1,03% | +0,04% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 1 | 0,00% | -0,51% | -0,51% | -0,47% | +0,31% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 20 | 55,00% | +0,09% | -0,27% | -0,66% | +0,46% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Classic technical | 11 | 54,55% | +0,37% | -0,37% | -0,80% | +0,17% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Famiglia statistica | 15 | 40,00% | -0,68% | -0,99% | -1,69% | -0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Microstruttura exchange | 1 | 0,00% | -1,38% | -1,38% | -1,57% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 19 | 42,11% | -0,00% | -0,60% | -1,21% | +0,59% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Classic technical | 10 | 40,00% | +0,03% | -0,03% | -2,00% | +2,20% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Famiglia statistica | 14 | 35,71% | -0,56% | -1,11% | -2,85% | +1,68% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Microstruttura exchange | 1 | 0,00% | -3,20% | -3,20% | -3,71% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 18 | 44,44% | +0,07% | -0,73% | -2,34% | +2,07% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Classic technical | 8 | 62,50% | +0,40% | -0,40% | -2,75% | +2,81% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 12 | 50,00% | -0,87% | -1,46% | -3,85% | +2,00% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -3,99% | -3,99% | -6,07% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 16 | 50,00% | +0,08% | -1,11% | -3,44% | +2,45% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Classic technical | 6 | 50,00% | +0,83% | -0,83% | -3,11% | +3,56% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 10 | 70,00% | +0,55% | -1,75% | -4,34% | +2,44% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -6,33% | -6,33% | -6,71% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 14 | 35,71% | -0,22% | -1,23% | -3,92% | +2,84% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Classic technical | 4 | 75,00% | +1,26% | -1,26% | -3,10% | +4,25% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 8 | 50,00% | +0,05% | -1,14% | -4,31% | +2,92% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 11 | 54,55% | +0,45% | -0,89% | -4,07% | +3,19% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Famiglia statistica | 5 | 60,00% | +0,04% | -2,14% | -5,08% | +2,28% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Frattale SOL | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Tecnico | 7 | 28,57% | -0,39% | -2,51% | -4,81% | +2,58% | OSSERVA | 0,0 | BASSA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 19 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 18 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 20 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Classic technical | 1 | 0,00% | -0,84% |
| BTC | BREVE | Famiglia statistica | 57 | 47,37% | +0,05% |
| BTC | BREVE | Microstruttura exchange | 3 | 100,00% | +2,36% |
| BTC | BREVE | Tecnico | 46 | 39,13% | -0,31% |
| BTC | SETTIMANALE | Famiglia statistica | 41 | 58,54% | +0,86% |
| BTC | SETTIMANALE | Microstruttura exchange | 2 | 50,00% | +0,81% |
| BTC | SETTIMANALE | Tecnico | 34 | 41,18% | -0,47% |
| BTC | SWING | Famiglia statistica | 7 | 85,71% | +1,60% |
| BTC | SWING | Tecnico | 6 | 33,33% | -0,12% |
| DOGE | BREVE | Classic technical | 49 | 46,94% | -0,02% |
| DOGE | BREVE | Famiglia statistica | 57 | 52,63% | +0,22% |
| DOGE | BREVE | Microstruttura exchange | 6 | 100,00% | +3,99% |
| DOGE | BREVE | Tecnico | 57 | 54,39% | +0,38% |
| DOGE | SETTIMANALE | Classic technical | 38 | 63,16% | +1,08% |
| DOGE | SETTIMANALE | Famiglia statistica | 41 | 65,85% | +1,24% |
| DOGE | SETTIMANALE | Microstruttura exchange | 1 | 100,00% | +2,30% |
| DOGE | SETTIMANALE | Tecnico | 41 | 65,85% | +1,24% |
| DOGE | SWING | Classic technical | 6 | 66,67% | +2,43% |
| DOGE | SWING | Famiglia statistica | 7 | 71,43% | +2,73% |
| DOGE | SWING | Tecnico | 7 | 71,43% | +2,73% |
| SOL | BREVE | Classic technical | 33 | 51,52% | +0,21% |
| SOL | BREVE | Famiglia statistica | 45 | 46,67% | -0,46% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 3 | 0,00% | -1,70% |
| SOL | BREVE | Tecnico | 57 | 47,37% | +0,05% |
| SOL | SETTIMANALE | Classic technical | 18 | 61,11% | +0,73% |
| SOL | SETTIMANALE | Famiglia statistica | 30 | 56,67% | -0,15% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Microstruttura exchange | 2 | 0,00% | -5,16% |
| SOL | SETTIMANALE | Tecnico | 41 | 46,34% | +0,08% |
| SOL | SWING | Famiglia statistica | 5 | 60,00% | +0,04% |
| SOL | SWING | Frattale SOL | 1 | 0,00% | -1,13% |
| SOL | SWING | Tecnico | 7 | 28,57% | -0,39% |

## Aree ancora in attesa

| Asset | Famiglia | Righe senza controlli | Stato |
| --- | --- | --- | --- |
| BTC | BREVE | 5 | in attesa di controlli maturati |
| BTC | SETTIMANALE | 7 | in attesa di controlli maturati |
| BTC | SWING | 8 | in attesa di controlli maturati |
| BTC | MEDIO | 15 | in attesa di controlli maturati |
| SOL | SETTIMANALE | 1 | in attesa di controlli maturati |
| SOL | SWING | 7 | in attesa di controlli maturati |
| SOL | MEDIO | 15 | in attesa di controlli maturati |
| DOGE | BREVE | 3 | in attesa di controlli maturati |
| DOGE | SETTIMANALE | 5 | in attesa di controlli maturati |
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
| BTC     |         21 |               0 |          21 | RACCOLTA DATI | n/a              | n/a             | n/a                   | n/a            |
| SOL     |         21 |               0 |          21 | RACCOLTA DATI | n/a              | n/a             | n/a                   | n/a            |
| DOGE    |         21 |               0 |          21 | RACCOLTA DATI | n/a              | n/a             | n/a                   | n/a            |

Regola: sotto 60 controlli osserva soltanto; da 100+ controlli può diventare utile per correggere rischio spot/leva nel Decision Report.

## Ultima lettura rapida

| Asset   | Rischio spot   | Rischio leva   | Nota leva                                                               |
|:--------|:---------------|:---------------|:------------------------------------------------------------------------|
| BTC     | MEDIO          | MOLTO ALTO     | spot preferibile; leva molto pericolosa anche 2x/3x senza margine largo |
| SOL     | BASSO          | ALTO           | leva da limitare; 2x/3x solo con invalidazione chiara                   |
| DOGE    | ALTO           | MOLTO ALTO     | leva da limitare; 2x/3x solo con invalidazione chiara                   |
<!-- RISK_CALIBRATION_END -->

</details>
<!-- COMPACT_SECTION_END:risk_calibration -->

<!-- COMPACT_SECTION_START:global_confluence -->
<details open>
<summary><strong>🌐 Global Confluence — quadro finale</strong></summary>

<!-- GLOBAL_CONFLUENCE_START -->
# Sintesi finale di confluenza

Generato: 2026-07-29 05:15 UTC


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
| BTC | +2 | MISTA / PARZIALE | Neutrale / misto | BASSA / RACCOLTA DATI | HOLD / ATTESA CONFERME | Prima resistenza sopra 66.910; conferma del doppio minimo sopra 67.248. | Sotto 57.748 il quadro tecnico peggiora. |
| SOL | 0 | MISTA / PARZIALE | Neutrale / misto | BASSA / RACCOLTA DATI | HOLD LEGGERO / ATTESA CONFERME | conferma del adam and eve bottom sopra 83,81; nuova conferma tecnica sopra 78,73; milestone analogiche 85,31 / 91,62, valide soltanto se rientra anche il gap frattale. | Allarmi sotto 69,80 / 73,40 / 62,19. |
| DOGE | +1 | MISTA / PARZIALE | Neutrale / misto | BASSA / RACCOLTA DATI | STAI ALLA FINESTRA | Sopra 0.07923 migliora; sopra 0.07966 viene invalidato il pattern ribassista dominante. | Sotto 0.06829 il rischio ribassista aumenta. |

## Punteggi per modulo

| Asset | Scanner grezzo | Market grezzo | Famiglia statistica | Scanner path | Tecnico | Classic tech | Frattale SOL | Fractal path | RSI top-cycle | Lifecycle EMA | Exchange flow | Futures | Daily change | Totale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +3 | +3 | +4 | 0 | -2 | -1 | 0 | 0 | 0 | 0 | 0 | 0 | +1 | +2 |
| SOL | +3 | +3 | +4 | 0 | -3 | -1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| DOGE | +3 | +2 | +4 | 0 | -2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | -1 | +1 |

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

- Famiglia statistica: **+4** — Scanner grezzo +3, Market Regime grezzo +3, match regime 12. Scanner e regime concordi con almeno 10 match: bonus massimo di 1 punto. Punteggio contato nel Global: +4.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **+3** — Casi positivi 72,50%, return centrale 30g +13,10%. Direzione scanner: SALITA. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **+3** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 12, positivi 30g 91,67%, return p50 +10,38%.
- Scanner path: **0** — Controlli disponibili 19. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **-2** — Score tecnico -3/12, verdetto debole, trend ribassista, struttura volatilità in espansione, divergenza rialzista rsi, Wyckoff possibile accumulazione, pattern score 0 (rialzista Doppio minimo / CANDIDATO; ribassista Doppio massimo / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **-1** — Score classico -6/12, verdetto RIBASSISTA / FRAGILE, stage STAGE 4 / MARKDOWN, struttura MASSIMI E MINIMI CRESCENTI, Wyckoff ACCUMULO POSSIBILE / RANGE BASSO, volatilità locale BASSO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Non applicabile a questo asset.
- Fractal path: **0** — Non applicabile a questo asset.
- RSI top-cycle: **0** — Non applicabile a questo asset.
- Lifecycle EMA: **0** — Non applicabile a questo asset.
- Exchange flow: **0** — Flow +1.75, derivati +0.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +1.25; exchange 3/3, copertura 100%, consenso bull 2, bear 1, divergenze 0, campioni 4h 9 su 4.00h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias LEGGERMENTE POSITIVA / NON PESATA; confidenza MEDIA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Misto, forza 1/5.
- Daily change: **+1** — BTC: cambiamento forte in miglioramento rispetto a ieri.

Conferme: Prima resistenza sopra 66.910; conferma del doppio minimo sopra 67.248.

Invalidazioni: Sotto 57.748 il quadro tecnico peggiora.

### SOL

- Confluenza: **MISTA / PARZIALE**
- Bias: **Neutrale / misto**
- Punteggio finale: **0**
- Affidabilità: **BASSA / RACCOLTA DATI**
- Azione coerente: **HOLD LEGGERO / ATTESA CONFERME**

SOL è ancora in zona mista. Il frattale resta soltanto uno scenario contestuale: non è confermato dal prezzo e vale 0 punti operativi finché il gap non rientra. Meglio evitare leva e ragionare solo a tranche piccole.

Dettaglio moduli:

- Famiglia statistica: **+4** — Scanner grezzo +3, Market Regime grezzo +3, match regime 19. Scanner e regime concordi con almeno 10 match: bonus massimo di 1 punto. Punteggio contato nel Global: +4.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **+3** — Casi positivi 72,50%, return centrale 30g +9,45%. Direzione scanner: SALITA. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **+3** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 19, positivi 30g 89,47%, return p50 +9,45%.
- Scanner path: **0** — Controlli disponibili 19. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **-3** — Score tecnico -8/12, verdetto ribassista tecnico, trend ribassista, struttura compressione / triangolo, divergenza ribassista nascosta rsi, Wyckoff possibile accumulazione, pattern score 0 (rialzista Adam and Eve Bottom / CANDIDATO; ribassista Doppio massimo / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **-1** — Score classico -11/12, verdetto RIBASSISTA / FRAGILE, stage STAGE 4 / MARKDOWN, struttura COMPRESSIONE / TRIANGOLO POSSIBILE, Wyckoff MARKDOWN / DEBOLEZZA, volatilità locale BASSO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Verdetto ANALOGIA DEBOLE / SCENARIO SECONDARIO, somiglianza strutturale +60,46%, aderenza live +68,64%, errore live +15,68%, gap corrente -6,32%, peso operativo 0, tracking STRUTTURA IN PEGGIORAMENTO, fase FRATTALE SOLO DI CONTESTO, rischio ALTO.
- Fractal path: **0** — Controlli disponibili 15, ma percorso ancorato non aderente: gap -6,32%, errore live +15,68%. Peso 0.
- RSI top-cycle: **0** — Rischio top-cycle RSI: BASSO.
- Lifecycle EMA: **0** — Contesto non pesato nel Global. Lifecycle score 4, bias SQUEEZE SETUP MODERATO, EMA200 112,38 $, upside EMA200 +52,98%, gap EMA50/EMA200 -3,94%, hit EMA200 12w +16,67%, trend STABILE / DA CONFERMARE. Peso Global forzato a 0.
- Exchange flow: **0** — Flow +1.75, derivati +0.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +1.25; exchange 3/3, copertura 100%, consenso bull 2, bear 0, divergenze 0, campioni 4h 9 su 4.00h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias LEGGERMENTE POSITIVA / NON PESATA; confidenza MEDIA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Misto, forza 1/5.
- Daily change: **0** — SOL: nessun cambiamento forte in miglioramento rispetto a ieri.

Conferme: conferma del adam and eve bottom sopra 83,81; nuova conferma tecnica sopra 78,73; milestone analogiche 85,31 / 91,62, valide soltanto se rientra anche il gap frattale.

Invalidazioni: Allarmi sotto 69,80 / 73,40 / 62,19.

### DOGE

- Confluenza: **MISTA / PARZIALE**
- Bias: **Neutrale / misto**
- Punteggio finale: **+1**
- Affidabilità: **BASSA / RACCOLTA DATI**
- Azione coerente: **STAI ALLA FINESTRA**

DOGE non ha ancora una confluenza pulita. Serve conferma tecnica prima di trattarlo come asset forte.

Dettaglio moduli:

- Famiglia statistica: **+4** — Scanner grezzo +3, Market Regime grezzo +2, match regime 20. Scanner e regime concordi con almeno 10 match: bonus massimo di 1 punto. Punteggio contato nel Global: +4.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **+3** — Casi positivi 65,00%, return centrale 30g +4,54%. Direzione scanner: SALITA. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **+2** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 20, positivi 30g 80,00%, return p50 +7,13%.
- Scanner path: **0** — Controlli disponibili 19. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **-2** — Score tecnico -3/12, verdetto debole, trend ribassista, struttura ribassista con massimi e minimi decrescenti, divergenza ribassista nascosta rsi, Wyckoff possibile accumulazione, pattern score -1 (rialzista Doppio minimo / CANDIDATO; ribassista Triplo massimo / MATURO). Fonte: technical_structure_metrics.csv.
- Classic technical: **0** — Score classico -2/12, verdetto DEBOLE / NON CONFERMATO, stage STAGE 4 / MARKDOWN, struttura MASSIMI E MINIMI DECRESCENTI, Wyckoff SPRING / TEST POSSIBILE, volatilità locale BASSO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Non applicabile a questo asset.
- Fractal path: **0** — Non applicabile a questo asset.
- RSI top-cycle: **0** — Non applicabile a questo asset.
- Lifecycle EMA: **0** — Non applicabile a questo asset.
- Exchange flow: **0** — Flow +1.75, derivati +0.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +0.75; exchange 3/3, copertura 100%, consenso bull 1, bear 1, divergenze 0, campioni 4h 9 su 4.00h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias LEGGERMENTE POSITIVA / NON PESATA; confidenza MEDIA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Misto, forza 1/5.
- Daily change: **-1** — DOGE: cambiamento medio in peggioramento rispetto a ieri.

Conferme: Sopra 0.07923 migliora; sopra 0.07966 viene invalidato il pattern ribassista dominante.

Invalidazioni: Sotto 0.06829 il rischio ribassista aumenta.


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

Generato: 2026-07-29 05:15 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [btc_macro_cycle_report.md](btc_macro_cycle_report.md)

Questo modulo descrive il contesto macro di Bitcoin. Non genera entrate tattiche, non autorizza leva e pesa **0** nel Global Confluence.

## Sintesi

| Voce | Valore | Lettura |
| --- | --- | --- |
| Prezzo BTC | 63.913 $ | prezzo corrente |
| Power Law centrale | 122.993 $ | deviazione -48,04% |
| Banda p10-p90 | 76.456 $ / 308.680 $ | SOTTO LA BANDA P10 |
| Percentile residuo | 1,27% | posizione storica nel corridoio |
| Esponente β | 5,8341 | R² log-log 91,97% |
| Stabilità β | BASSA | range 1,3095 cambiando finestra |
| Ultimo halving | 2024-04-19 | 831 giorni fa |
| Fase ciclo | 56,88% | percentuale indicativa del ciclo quadriennale |
| Peso Global | 0 | CONTESTO MACRO / DIAGNOSTICO |

La Power Law viene trattata come regressione empirica, non come legge fisica. Il report mostra quanto cambia l'esponente usando finestre iniziali diverse e la confronta con il benchmark ingenuo 'prezzo invariato'.

## Bitcoin Power Law

- Campione: 2014-09-17 → 2026-07-29 (4333 osservazioni)
- Formula stimata: prezzo ≈ exp(-39.3048) × giorni^5.8341
- Prezzo centrale oggi: **122.993 $**
- Posizione corrente: **SOTTO LA BANDA P10**, percentile 1,27%
- Scarto dal centro: **-48,04%**

![Bitcoin Power Law](btc_power_law_chart.png)

![Bitcoin Power Law log-log](btc_power_law_loglog_chart.png)

### Stabilità dell'esponente

| Inizio campione | β | R² log-log |
| --- | --- | --- |
| 2014 | 5,8341 | 91,97% |
| 2015 | 5,9199 | 91,54% |
| 2016 | 5,6085 | 87,78% |
| 2017 | 4,8782 | 82,88% |
| 2018 | 4,6104 | 78,35% |

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
| 2012-11-28 → 2016-07-09 | 2014-12-18 | -36,01% | -17,69% | -19,43% | +48,88% |
| 2016-07-09 → 2020-05-11 | 2018-09-14 | -3,41% | -49,12% | -40,01% | +59,04% |
| 2020-05-11 → 2024-04-19 | 2022-08-08 | -18,98% | -12,11% | -2,01% | +25,02% |

Campione molto piccolo: questi rendimenti sono contesto di ciclo, non probabilità affidabili.

## SOL/BTC e DOGE/BTC dentro il tempo Bitcoin

![Altcoin nel ciclo BTC](alt_btc_cycle_spirals.png)

| Asset | Coppia | Forza vs BTC | Score raw | Candidato | 30g | Peso Global |
| --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | SOTTOPERFORMA BTC | -5 | -1 | -4.28690909274504 | 0 |
| DOGE | DOGE/BTC | SOTTOPERFORMA BTC | -6 | -1 | -10.018469024076815 | 0 |

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

Generato: 2026-07-29 05:15 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [relative_strength_btc_report.md](relative_strength_btc_report.md)

Questo modulo controlla se SOL e DOGE stanno davvero battendo Bitcoin. Una salita in USD accompagnata da una coppia ALT/BTC ribassista è spesso soltanto trascinamento di BTC.

**Protezione iniziale:** il candidato relativo è limitato a -1/0/+1, ma il peso nel Global resta **0**. La coppia BTC conferma o indebolisce il tecnico USD; non viene sommata come secondo modulo indipendente.

## Sintesi

| Asset | Coppia | Prezzo | Score raw | Candidato | Peso Global | Forza vs BTC | Confidenza | 30g | Tecnico USD | Lettura combinata |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | 0.00114760 | -5 | -1 | 0 | SOTTOPERFORMA BTC | MEDIA | -4,29% | RIBASSISTA | DEBOLEZZA COMPLETA: scende in USD e contro BTC |
| DOGE | DOGE/BTC | 0.00000110 | -6 | -1 | 0 | SOTTOPERFORMA BTC | MEDIA | -10,02% | RIBASSISTA | DEBOLEZZA COMPLETA: scende in USD e contro BTC |

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
- **Rendimenti relativi:** 7g -2,25%; 30g -4,29%; 90g +4,71%; 180g -17,50%
- **Daily:** RSI 39.39; MA50 0.00117371; MA200 0.00120965
- **Weekly:** MA30 0.00120962; RSI 43.67
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
- **Rendimenti relativi:** 7g +0,26%; 30g -10,02%; 90g -19,52%; 180g -20,22%
- **Daily:** RSI 37.49; MA50 0.00000121; MA200 0.00000133
- **Weekly:** MA30 0.00000132; RSI 30.65
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
| SOL | 1g | 4 | 75,00% | -0,08% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 3g | 3 | 66,67% | +0,62% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 7g | 0 | n/a | n/a | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 14g | 0 | n/a | n/a | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 30g | 0 | n/a | n/a | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 1g | 18 | 77,78% | +0,61% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 3g | 16 | 68,75% | +1,10% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 7g | 12 | 91,67% | +2,75% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 14g | 5 | 100,00% | +3,65% | LOCKED / RACCOLTA LIVE | 0 |
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

Ultima candela SOL usata: **29 luglio 2026**

## Verdetto: ANALOGIA DEBOLE / SCENARIO SECONDARIO

- **Fase attuale:** FRATTALE SOLO DI CONTESTO
- **Somiglianza totale:** +60,46%
- **Somiglianza strutturale:** +60,46%
- **Aderenza prezzo live:** +68,64%
- **Errore medio live:** +15,68%
- **Gap prezzo corrente:** -6,32%
- **Peso operativo suggerito:** 0
- **Affidabilita:** BASSA
- **Rischio fase:** ALTO
- **Trend tracking:** STRUTTURA IN PEGGIORAMENTO
- **Sintesi:** Esistono alcuni elementi comuni, ma non abbastanza per una conferma.
- **SOL è al giorno:** 53 dal bottom usato.
- **Giorno BTC equivalente:** 2023-01-13
- **Prossimo step:** Proiezione condizionale, non conferma operativa: **Spinta rialzista abbastanza pulita.** Zona bassa **73,47 $** intorno al **29 luglio 2026**; zona alta **85,31 $** intorno al **10 agosto 2026**; fine step circa **85,16 $** entro il **12 agosto 2026**.

## Somiglianza prima e dopo inizio programma

Questa sezione separa la somiglianza della forma dall'aderenza reale del prezzo.

- **Inizio programma/scanner:** 3 luglio 2026
- **Prima del programma** = backtest retroattivo.
- **Da inizio programma** = verifica live: è la parte più importante per l'uso operativo.

| Periodo | Date | Giorni | Aderenza prezzo | Errore medio | Gap ultimo | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| Prima del programma | 6 giugno 2026 -> 2 luglio 2026 | 27 | +87,95% | +6,02% | +21,89% | ABBASTANZA ALLINEATO |
| Da inizio programma | 3 luglio 2026 -> 29 luglio 2026 | 27 | +68,64% | +15,68% | -6,32% | STACCATO / NON ADERENTE |
| Totale dal bottom | 6 giugno 2026 -> 29 luglio 2026 | 54 | +78,29% | +10,85% | -6,32% | DEVIAZIONE MODERATA |

Nota: un frattale può avere una forma simile ma un prezzo distante. In quel caso non è operativo finché il gap non rientra.

## Lettura operativa veloce

Il frattale non deve generare acquisti o leva adesso. La forma è un contesto, ma l'aderenza live del prezzo è insufficiente.

| Voce | Risposta | Perché |
| --- | --- | --- |
| Uso operativo | NO | Il frattale vale 0 punti operativi finché il prezzo resta non aderente. |
| Aderenza live | +68,64% | Errore medio live +15,68%. |
| Gap corrente | -6,32% | Deve rientrare circa entro ±12%. |
| Prima conferma prezzo | 85,31 $ | Serve anche miglioramento del gap, non solo una candela sopra il livello. |
| Seconda conferma | 91,62 $ | Rende più credibile il percorso, ma non sostituisce l'aderenza. |
| Invalidazione soft | 69,80 $ | Sotto questa zona il quadro peggiora. |
| Invalidazione forte | 62,19 $ | Sotto il bottom il paragone è quasi rotto. |

## Target ciclo fino al top BTC 2025

| Voce | Valore |
| --- | --- |
| Stato | CONTESTO / NON OPERATIVO |
| Top BTC 2025 | 6 ottobre 2025 - 124.753 $ |
| Data SOL equivalente | 21 aprile 2029 |
| Target ciclo base da oggi | 460,36 $ |
| Massimo percorso base | 460,36 $ (21 aprile 2029) |

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
| Prima conferma | 85,31 $ | Deve accompagnarsi al rientro del gap. |
| Seconda conferma | 91,62 $ | Scenario più credibile. |
| Invalidazione soft | 69,80 $ | Il frattale si indebolisce. |
| Invalidazione forte | 62,19 $ | Il paragone si rompe. |

## Proiezione veloce con date SOL

| Orizzonte | Data SOL | BTC fece | SOL base | Min percorso | Max percorso |
| --- | --- | --- | --- | --- | --- |
| 7 giorni | 5 agosto 2026 | +13,90% | 83,68 $ | 73,47 $ | 83,68 $ |
| 14 giorni | 12 agosto 2026 | +15,92% | 85,16 $ | 73,47 $ | 85,31 $ |
| 30 giorni | 28 agosto 2026 | +9,44% | 80,40 $ | 73,47 $ | 87,73 $ |
| 60 giorni | 27 settembre 2026 | +24,29% | 91,32 $ | 73,47 $ | 91,62 $ |
| 90 giorni | 27 ottobre 2026 | +52,69% | 112,18 $ | 73,47 $ | 112,18 $ |
| 120 giorni | 26 novembre 2026 | +34,53% | 98,84 $ | 73,47 $ | 112,50 $ |

## Prossimi step se SOL segue BTC 2022

| Step | Date SOL | BTC fine | SOL zona bassa | SOL zona alta | SOL fine base | Lettura |
| --- | --- | --- | --- | --- | --- | --- |
| Step 1 - prossime 2 settimane | 29 luglio 2026 -> 12 agosto 2026 | +15,92% | 73,47 $ (29 luglio 2026) | 85,31 $ (10 agosto 2026) | 85,16 $ | Spinta rialzista abbastanza pulita. |
| Step 2 - primo mese | 13 agosto 2026 -> 28 agosto 2026 | +9,44% | 79,90 $ (26 agosto 2026) | 87,73 $ (14 agosto 2026) | 80,40 $ | Spinta rialzista abbastanza pulita. |
| Step 3 - secondo mese | 29 agosto 2026 -> 27 settembre 2026 | +24,29% | 74,49 $ (23 settembre 2026) | 91,62 $ (5 settembre 2026) | 91,32 $ | Spinta rialzista abbastanza pulita. |
| Step 4 - terzo mese | 28 settembre 2026 -> 27 ottobre 2026 | +52,69% | 89,95 $ (28 settembre 2026) | 112,18 $ (27 ottobre 2026) | 112,18 $ | Spinta rialzista abbastanza pulita. |

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
| Prezzo SOL | 73,47 $ |  |
| Weekly RSI | 38,37 / linea grezza 53,65 | LINEA NON AFFIDABILE / RISCHIO NON ATTIVO — IRREALISTICA / NON OPERATIVA |
| Monthly RSI | 40,37 / linea grezza 56,16 | RSI TROPPO BASSO PER RISCHIO TOP — VALIDA / USO PRUDENTE |
| Target ciclo base | 460,36 $ | Avanzamento +15,96% |
| Rischio top-cycle RSI | BASSO | Nessun segnale top-cycle macro attivo. Prezzo ancora lontano dal target ciclo; il filtro RSI resta solo di monitoraggio. |

## Lettura semplice

- Weekly: La top-line weekly non supera i controlli di qualità. Non viene usata per generare rischio top-cycle.
- Monthly: RSI monthly è 40,4, sotto la soglia prudente 55. Anche se fosse vicino alla linea, non è una vera zona di esaurimento ciclo.
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
| Prezzo SOL | 73,47 $ |
| TVL Solana | 4,77 mld $ |
| TVL 7g | -4,29% |
| DEX volume 24h | 1,75 mld $ |
| Fees 24h | 7,33 mln $ |
| Stablecoin su Solana | 16,12 mld $ |
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
| Prezzo SOL | 73,47 $ |
| EMA200 weekly target | 112,38 $ |
| Upside verso EMA200 | +52,98% |
| Distanza prezzo da EMA200 | -34,63% |
| Gap EMA50/EMA200 | -3,94% |
| Stato cross | EMA50 SOTTO EMA200 |
| RSI weekly | 38,36 |
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

<!-- Generato: 2026-07-29 05:14 UTC -->
<!-- MAJOR_ALT_LIFECYCLE_SQUEEZE_END -->

</details>
<!-- COMPACT_SECTION_END:major_alt_lifecycle -->

# Report giornaliero BTC / SOL / DOGE

Aggiornato il: **2026-07-29 05:12:22 UTC**

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
- DOGE: cambiamento importante in peggioramento rispetto a ieri.

| Asset | Cambio | Tono | Verdetto oggi | Casi positivi oggi | Δ casi positivi |
| --- | --- | --- | --- | --- | --- |
| BTC | CAMBIAMENTO FORTE | miglioramento | RIALZISTA | +72.50% | +10.00 punti |
| SOL | NESSUN CAMBIAMENTO FORTE | miglioramento | RIALZISTA | +72.50% | +2.50 punti |
| DOGE | CAMBIAMENTO MEDIO | peggioramento | RIALZISTA | +65.00% | -2.50 punti |

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
| BTC | 60.726 $ | 70.314 $ | +36,84% | +15,79% | rimbalzo debole | 70.314 $ | 60.726 $ | +3,85% | -13,64% | spike storicamente più resistente |
| SOL | 69,80 $ | 80,82 $ | +31,58% | +15,79% | rimbalzo poco frequente | 80,82 $ | 69,80 $ | 0,00% | -13,64% | spike storicamente più resistente |
| DOGE | 0,06708 $ | 0,07767 $ | +36,67% | +15,79% | rimbalzo debole | 0,07767 $ | 0,06708 $ | +55,17% | -13,64% | attenzione a prendere profitto |

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

- **BTC: su 40 casi simili, 19 prima sono scesi a -5,00%. Tra quei 19, 7 poi sono rimbalzati fino a +10,00%. Percentuale: +36,84% (7/19). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.**
- **BTC: su 40 casi simili, 26 prima sono saliti a +10,00%. Tra quei 26, 1 poi sono scaricati a -5,00%. Percentuale: +3,85% (1/26). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.**
- **SOL: su 40 casi simili, 19 prima sono scesi a -5,00%. Tra quei 19, 6 poi sono rimbalzati fino a +10,00%. Percentuale: +31,58% (6/19). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.**
- **SOL: su 40 casi simili, 25 prima sono saliti a +10,00%. Tra quei 25, 0 poi sono scaricati a -5,00%. Percentuale: 0,00% (0/25). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.**
- **DOGE: su 40 casi simili, 30 prima sono scesi a -5,00%. Tra quei 30, 11 poi sono rimbalzati fino a +10,00%. Percentuale: +36,67% (11/30). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.**
- **DOGE: su 40 casi simili, 29 prima sono saliti a +10,00%. Tra quei 29, 16 poi sono scaricati a -5,00%. Percentuale: +55,17% (16/29). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: attenzione a prendere profitto.**

<!-- BOUNCE_AFTER_DRAWDOWN_END -->

</details>
<!-- COMPACT_SECTION_END:bounce_after_drawdown -->

<!-- COMPACT_SECTION_START:scanner_forecast -->
<details>
<summary><strong>🔭 Cono probabilistico dello scanner</strong></summary>

<!-- SCANNER_FORECAST_TRACKER_START -->
# Scanner forecast path / cono probabilistico

Generato: 2026-07-29 05:14:01 UTC


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
| BTC | 2026-07-29 | 63.922 $ | SALITA | 72,50% | 44.465,35 $ | 61.788,22 $ | 72.294,72 $ | 86.378,20 $ | 95.477,04 $ |
| SOL | 2026-07-29 | 73,47 $ | SALITA | 72,50% | 65,89 $ | 72,50 $ | 80,42 $ | 92,04 $ | 107,90 $ |
| DOGE | 2026-07-29 | 0.07061 $ | SALITA | 65,00% | 0.06251 $ | 0.06737 $ | 0.07382 $ | 0.07943 $ | 0.09054 $ |

## Grafici

### BTC

![Scanner forecast BTC](scanner_forecast_BTC.png)

#### Verifica storica e discrepanza

![Verifica storica cono BTC](scanner_forecast_history_BTC.png)

- Cono congelato il **2026-07-10**; verificato fino al **2026-07-29**; stato **PARZIALE 19/30g**.
- Reale **63.920,90 $**; p50 previsto **67.794,45 $**; scarto **-5,71%**.
- Errore medio assoluto **3,93%**; massimo **7,75%**; DENTRO p10-p90; DENTRO p25-p75.

### SOL

![Scanner forecast SOL](scanner_forecast_SOL.png)

#### Verifica storica e discrepanza

![Verifica storica cono SOL](scanner_forecast_history_SOL.png)

- Cono congelato il **2026-07-10**; verificato fino al **2026-07-29**; stato **PARZIALE 19/30g**.
- Reale **73,47 $**; p50 previsto **71,78 $**; scarto **2,36%**.
- Errore medio assoluto **2,65%**; massimo **5,38%**; DENTRO p10-p90; DENTRO p25-p75.

### DOGE

![Scanner forecast DOGE](scanner_forecast_DOGE.png)

#### Verifica storica e discrepanza

![Verifica storica cono DOGE](scanner_forecast_history_DOGE.png)

- Cono congelato il **2026-07-10**; verificato fino al **2026-07-29**; stato **PARZIALE 19/30g**.
- Reale **0.07060 $**; p50 previsto **0.05663 $**; scarto **24,67%**.
- Errore medio assoluto **9,87%**; massimo **25,63%**; DENTRO p10-p90; FUORI p25-p75.

## Accuratezza percorso scanner

| Asset   | Giorno   |   Controlli | Dentro p10-p90   | Dentro p25-p75   | Errore medio abs vs p50   | Errore medio vs p50   |
|:--------|:---------|------------:|:-----------------|:-----------------|:--------------------------|:----------------------|
| BTC | 1g | 19 | 100,00% | 57,89% | 1,80% | -0,05% |
| BTC | 3g | 17 | 100,00% | 70,59% | 2,32% | -0,16% |
| BTC | 7g | 13 | 100,00% | 84,62% | 2,88% | 0,73% |
| BTC | 14g | 6 | 100,00% | 83,33% | 1,85% | 0,14% |
| BTC | 30g | 0 | n/a | n/a | n/a | n/a |
| SOL | 1g | 19 | 73,68% | 47,37% | 2,43% | -0,51% |
| SOL | 3g | 17 | 100,00% | 64,71% | 2,67% | -0,82% |
| SOL | 7g | 13 | 100,00% | 92,31% | 2,61% | 0,72% |
| SOL | 14g | 6 | 100,00% | 83,33% | 2,95% | 2,56% |
| SOL | 30g | 0 | n/a | n/a | n/a | n/a |
| DOGE | 1g | 19 | 89,47% | 52,63% | 3,17% | -0,10% |
| DOGE | 3g | 17 | 100,00% | 88,24% | 2,24% | 0,92% |
| DOGE | 7g | 13 | 100,00% | 100,00% | 7,38% | 7,38% |
| DOGE | 14g | 6 | 100,00% | 16,67% | 18,41% | 18,41% |
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

Righe salvate nello storico: **51**.

Questa sezione tiene un diario delle previsioni giornaliere a 30 giorni, senza appesantire il report principale.

| Data | Asset | Prezzo | Direzione | Casi positivi | Return p50 | Drawdown p50 | Max gain p50 | Controllo 30g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-07-29 | BTC | 63.922 $ | SALITA | 72,50% | 72.295 $ | 61.054 $ | 75.960 $ | 2026-08-28 |
| 2026-07-29 | DOGE | 0,07000 $ | SALITA | 65,00% | 0,07000 $ | 0,06000 $ | 0,08000 $ | 2026-08-28 |
| 2026-07-29 | SOL | 73,47 $ | SALITA | 72,50% | 80,42 $ | 70,29 $ | 84,48 $ | 2026-08-28 |

<!-- FORECAST_30D_HISTORY_END -->

</details>
<!-- COMPACT_SECTION_END:scanner_forecast -->

<!-- COMPACT_SECTION_START:extreme_cases -->
<details>
<summary><strong>⚠️ Percorso dei casi estremi</strong></summary>

<!-- EXTREME_CASES_PATH_START -->
# Extreme cases path report

Generato: 2026-07-29 05:14 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [extreme_cases_path_report.md](extreme_cases_path_report.md)

Questo report si attiva quando i casi positivi o negativi sono almeno **80%**.

Ora misura anche il **rialzo massimo prima della discesa principale**, quindi distingue uno spike iniziale da una discesa quasi immediata.

## Trigger estremi

| Asset   | Direzione   | Trigger   | Percentuale   | Motivo                           |   Match disponibili |
|:--------|:------------|:----------|:--------------|:---------------------------------|--------------------:|
| BTC     | NESSUNO     | NO        | +72,50%       | Nessun lato sopra soglia estrema |                  40 |
| SOL     | NESSUNO     | NO        | +72,50%       | Nessun lato sopra soglia estrema |                  40 |
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
- Casi positivi / salita storica: **72,50%**
- Casi negativi / discesa storica: **27,50%**
- Quanto è netto il segnale: **forte**
- Prezzo attuale: **63.921,65 $**
- Return normale fra 30 giorni: **72.294,72 $** (13,10%)
- Drawdown normale durante il mese: **61.054,09 $** (-4,49%)
- Drawdown brutto da rispettare: **53.160,07 $** (-16,84%)
- Max gain normale durante il mese: **75.959,88 $** (18,83%)
- Max gain buono / take profit ottimistico: **90.403,40 $** (41,43%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Solana
- Direzione più probabile a 30 giorni: **SALITA**
- Casi positivi / salita storica: **72,50%**
- Casi negativi / discesa storica: **27,50%**
- Quanto è netto il segnale: **forte**
- Prezzo attuale: **73,47 $**
- Return normale fra 30 giorni: **80,42 $** (9,45%)
- Drawdown normale durante il mese: **70,29 $** (-4,33%)
- Drawdown brutto da rispettare: **65,72 $** (-10,55%)
- Max gain normale durante il mese: **84,48 $** (14,98%)
- Max gain buono / take profit ottimistico: **100,19 $** (36,36%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Dogecoin
- Direzione più probabile a 30 giorni: **SALITA**
- Casi positivi / salita storica: **65,00%**
- Casi negativi / discesa storica: **35,00%**
- Quanto è netto il segnale: **medio**
- Prezzo attuale: **0,07 $**
- Return normale fra 30 giorni: **0,07 $** (4,54%)
- Drawdown normale durante il mese: **0,06 $** (-12,71%)
- Drawdown brutto da rispettare: **0,06 $** (-17,90%)
- Max gain normale durante il mese: **0,08 $** (14,17%)
- Max gain buono / take profit ottimistico: **0,09 $** (24,03%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Messaggio del giorno

Il quadro generale oggi è più favorevole. Lo scanner vede più possibilità di salita su più asset.

---

# Mappa semplice asset per asset

# Bitcoin — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟢 VERDE / Favorevole
**Prezzo attuale:** 63.921,65 $

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

- Se va molto male: **44.465,35 $** (-30,44%)
- Se va male: **61.788,22 $** (-3,34%)
- Scenario normale: **72.294,72 $** (13,10%)
- Se va bene: **86.378,20 $** (35,13%)
- Se va molto bene: **95.477,04 $** (49,37%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **61.054,09 $** (-4,49%)
- Discesa brutta: **53.160,07 $** (-16,84%)
- Discesa molto brutta: **43.388,03 $** (-32,12%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **75.959,88 $** (18,83%)
- Rialzo buono: **90.403,40 $** (41,43%)
- Rialzo molto forte: **104.160,88 $** (62,95%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Bitcoin tendeva a muoversi tra una zona bassa intorno a **61.054,09 $** e uno spike normale intorno a **75.959,88 $**.

La chiusura a 30 giorni era più spesso positiva: salita 72,50%, discesa 27,50%. Quindi la lettura principale è favorevole.

Nota leva BTC: se la liquidazione è vicina a 51.000 $, guarda soprattutto la discesa brutta e molto brutta. Il prezzo può recuperare dopo, ma la leva può saltare prima.

---

# Solana — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟢 VERDE / Favorevole
**Prezzo attuale:** 73,47 $

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

- Se va molto male: **65,89 $** (-10,32%)
- Se va male: **72,50 $** (-1,32%)
- Scenario normale: **80,42 $** (9,45%)
- Se va bene: **92,04 $** (25,28%)
- Se va molto bene: **107,90 $** (46,86%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **70,29 $** (-4,33%)
- Discesa brutta: **65,72 $** (-10,55%)
- Discesa molto brutta: **58,33 $** (-20,60%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **84,48 $** (14,98%)
- Rialzo buono: **100,19 $** (36,36%)
- Rialzo molto forte: **114,25 $** (55,50%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Solana tendeva a muoversi tra una zona bassa intorno a **70,29 $** e uno spike normale intorno a **84,48 $**.

La chiusura a 30 giorni era più spesso positiva: salita 72,50%, discesa 27,50%. Quindi la lettura principale è favorevole.

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

- Se va molto male: **0,06 $** (-11,48%)
- Se va male: **0,07 $** (-4,59%)
- Scenario normale: **0,07 $** (4,54%)
- Se va bene: **0,08 $** (12,49%)
- Se va molto bene: **0,09 $** (28,22%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **0,06 $** (-12,71%)
- Discesa brutta: **0,06 $** (-17,90%)
- Discesa molto brutta: **0,06 $** (-21,40%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **0,08 $** (14,17%)
- Rialzo buono: **0,09 $** (24,03%)
- Rialzo molto forte: **0,09 $** (33,74%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Dogecoin tendeva a muoversi tra una zona bassa intorno a **0,06 $** e uno spike normale intorno a **0,08 $**.

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

**Prezzo attuale:** 63.921,65 $

Bitcoin ha un segnale favorevole. La statistica dei casi simili indica più possibilità di salita che di discesa, ma resta comunque una probabilità, non una certezza.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **72,50%**
- Casi negativi dopo 30 giorni: **27,50%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **86,56%**
- Rendimento medio dopo 30 giorni: **13,23%**
- Rendimento centrale dopo 30 giorni: **13,10%**
- Discesa media durante i 30 giorni: **-10,85%**
- Massimo rialzo medio durante i 30 giorni: **29,34%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **72.380,51 $**
- Scenario centrale a 30 giorni: **72.294,72 $**
- Zona di rischio media: **56.985,57 $**
- Zona di rialzo media: **82.679,10 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -30,44% → **44.465,35 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -3,34% → **61.788,22 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: 13,10% → **72.294,72 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 35,13% → **86.378,20 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 49,37% → **95.477,04 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -32,12% → **43.388,03 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -16,84% → **53.160,07 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -4,49% → **61.054,09 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -0,50% → **63.602,71 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: 0,00% → **63.921,65 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 0,00% → **63.921,65 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 4,74% → **66.948,87 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 18,83% → **75.959,88 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 41,43% → **90.403,40 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 62,95% → **104.160,88 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| LRC-USD         | 2018-10-04   | 2019-01-11 |        89.87 |        35.3  |          -5.72 |         154.28 |
| SAND-USD        | 2023-07-04   | 2023-10-11 |        89.66 |        49.54 |          -0.05 |          49.54 |
| FIL-USD         | 2023-07-04   | 2023-10-11 |        89.57 |        44.46 |          -0.01 |          44.46 |
| ONE-USD         | 2020-01-27   | 2020-05-05 |        89.2  |         9.39 |          -4.18 |          11.48 |
| XLM-USD         | 2020-07-20   | 2020-10-27 |        88.95 |       104.8  |          -8.82 |         138.95 |
| XRP-USD         | 2025-12-21   | 2026-03-30 |        88.61 |         3.53 |          -0.53 |          11.68 |
| ETH-USD         | 2025-12-21   | 2026-03-30 |        87.92 |        11.36 |           0    |          19.65 |
| BTC-USD         | 2018-10-06   | 2019-01-13 |        87.84 |         2.83 |          -4.32 |           4.94 |
| MKR-USD         | 2020-01-28   | 2020-05-06 |        87.4  |        44.12 |          -4.48 |          54.19 |
| XRP-USD         | 2019-10-14   | 2020-01-21 |        87.28 |        14.85 |          -7.06 |          41.18 |

---

# Approfondimento tecnico — Solana (SOL-USD)

## Semaforo: 🟢 VERDE / Favorevole

**Prezzo attuale:** 73,47 $

Solana ha un segnale favorevole. La statistica dei casi simili indica più possibilità di salita che di discesa, ma resta comunque una probabilità, non una certezza.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **72,50%**
- Casi negativi dopo 30 giorni: **27,50%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **76,55%**
- Rendimento medio dopo 30 giorni: **13,37%**
- Rendimento centrale dopo 30 giorni: **9,45%**
- Discesa media durante i 30 giorni: **-8,06%**
- Massimo rialzo medio durante i 30 giorni: **24,57%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **83,30 $**
- Scenario centrale a 30 giorni: **80,42 $**
- Zona di rischio media: **67,55 $**
- Zona di rialzo media: **91,52 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -10,32% → **65,89 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -1,32% → **72,50 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: 9,45% → **80,42 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 25,28% → **92,04 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 46,86% → **107,90 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -20,60% → **58,33 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -10,55% → **65,72 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -4,33% → **70,29 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -0,33% → **73,23 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: 0,00% → **73,47 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 2,23% → **75,11 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 6,25% → **78,06 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 14,98% → **84,48 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 36,36% → **100,19 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 55,50% → **114,25 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| WAVES-USD       | 2019-03-13   | 2019-06-20 |        83.24 |       -36.8  |         -40.77 |           1.46 |
| NEAR-USD        | 2025-12-21   | 2026-03-30 |        80.32 |        14.29 |           0    |          23.51 |
| ENJ-USD         | 2018-10-09   | 2019-01-16 |        80.14 |        -9    |         -26.72 |           3.73 |
| QTUM-USD        | 2018-10-09   | 2019-01-16 |        80.04 |       -10.22 |         -17.99 |           1.51 |
| RUNE-USD        | 2025-12-27   | 2026-04-05 |        78.73 |        41.91 |          -0.37 |          41.91 |
| LINK-USD        | 2025-12-21   | 2026-03-30 |        78.7  |         5.89 |           0    |          11.78 |
| BNB-USD         | 2025-12-26   | 2026-04-04 |        78.36 |         4.95 |          -0.18 |           8.46 |
| EOS-USD         | 2018-10-19   | 2019-01-26 |        77.7  |        47.4  |          -7.62 |          75.2  |
| SOL-USD         | 2025-12-24   | 2026-04-02 |        77.68 |         6.75 |           0    |          12.72 |
| ONE-USD         | 2020-01-27   | 2020-05-05 |        77.55 |         9.39 |          -4.18 |          11.48 |

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

- Somiglianza media dei pattern: **88,14%**
- Rendimento medio dopo 30 giorni: **5,58%**
- Rendimento centrale dopo 30 giorni: **4,54%**
- Discesa media durante i 30 giorni: **-12,56%**
- Massimo rialzo medio durante i 30 giorni: **17,77%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **0,07 $**
- Scenario centrale a 30 giorni: **0,07 $**
- Zona di rischio media: **0,06 $**
- Zona di rialzo media: **0,08 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -11,48% → **0,06 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -4,59% → **0,07 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: 4,54% → **0,07 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 12,49% → **0,08 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 28,22% → **0,09 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -21,40% → **0,06 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -17,90% → **0,06 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -12,71% → **0,06 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -4,90% → **0,07 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: -0,61% → **0,07 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 4,01% → **0,07 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 8,45% → **0,08 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 14,17% → **0,08 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 24,03% → **0,09 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 33,74% → **0,09 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| ZEC-USD         | 2019-06-06   | 2019-09-13 |        92.97 |       -17.01 |         -21.22 |          18.25 |
| OP-USD          | 2025-12-22   | 2026-03-31 |        90.2  |         8.81 |          -3.72 |          21.82 |
| AVAX-USD        | 2025-09-03   | 2025-12-11 |        90.02 |         2.15 |         -14.86 |           8.65 |
| MKR-USD         | 2022-09-29   | 2023-01-06 |        89.92 |        28.84 |           0    |          32.75 |
| VET-USD         | 2022-03-14   | 2022-06-21 |        89.92 |         7.68 |          -8.95 |          11.1  |
| THETA-USD       | 2022-03-16   | 2022-06-23 |        89.11 |         0.32 |         -16.14 |          13.49 |
| WAVES-USD       | 2021-10-03   | 2022-01-10 |        88.99 |       -10.84 |         -37.18 |          10.13 |
| NEAR-USD        | 2022-03-22   | 2022-06-29 |        88.8  |        28.15 |          -6.55 |          33.07 |
| ZIL-USD         | 2019-05-29   | 2019-09-05 |        88.7  |       -21.47 |         -29.04 |          10.68 |
| LTC-USD         | 2018-04-14   | 2018-07-22 |        88.66 |       -32.24 |         -35.07 |           7.37 |

</details>
<!-- COMPACT_SECTION_END:scanner_full_detail -->

<!-- COMPACT_SECTION_START:market_regime -->
<details>
<summary><strong>🌦️ Market Regime Match</strong></summary>

<!-- MARKET_REGIME_MATCH_START -->
# Market Regime Match Report


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [market_regime_match_report.md](market_regime_match_report.md)

Generated: 2026-07-29 05:14 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | BEAR | 63.922 $ | False | -16.23% | -9.79% | BEAR | -16.23% | -9.79% |
| DOGE-USD | BEAR | 0.07061 $ | False | -33.70% | -16.13% | BEAR | -16.23% | -9.79% |
| SOL-USD | BEAR | 73,47 $ | False | -11.51% | -16.59% | BEAR | -16.23% | -9.79% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 72.50% | 13.10% | 35.13% | 49.37% | -4.49% | -32.12% | 18.83% | 41.43% | 62.95% | 62.50% | 9.43% | 42.05% | 67.22% |
| BTC-USD | SAME_BTC_REGIME | 14 | 85.71% | 10.38% | 18.13% | 34.89% | -4.25% | -13.63% | 13.61% | 32.90% | 48.49% | 57.14% | 2.99% | 9.43% | 43.04% |
| BTC-USD | SAME_ASSET_REGIME | 21 | 90.48% | 14.84% | 35.65% | 49.54% | -2.71% | -14.37% | 19.65% | 42.19% | 51.62% | 71.43% | 10.45% | 43.28% | 65.83% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 12 | 91.67% | 10.38% | 15.95% | 33.69% | -4.25% | -8.79% | 13.61% | 26.88% | 50.58% | 58.33% | 2.99% | 9.69% | 52.35% |
| DOGE-USD | ALL_MATCHES | 40 | 65.00% | 4.54% | 12.49% | 28.22% | -12.71% | -21.40% | 14.17% | 24.03% | 33.74% | 60.00% | 8.85% | 20.62% | 72.14% |
| DOGE-USD | SAME_BTC_REGIME | 22 | 81.82% | 7.13% | 15.11% | 28.00% | -10.31% | -18.52% | 14.97% | 22.19% | 33.32% | 77.27% | 11.89% | 18.70% | 36.52% |
| DOGE-USD | SAME_ASSET_REGIME | 26 | 76.92% | 7.13% | 17.37% | 30.43% | -10.31% | -19.81% | 14.17% | 22.19% | 33.05% | 76.92% | 14.66% | 35.64% | 76.78% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 20 | 80.00% | 7.13% | 13.93% | 27.20% | -10.31% | -19.20% | 14.17% | 19.04% | 32.15% | 75.00% | 11.60% | 17.78% | 37.15% |
| SOL-USD | ALL_MATCHES | 40 | 72.50% | 9.45% | 25.28% | 46.86% | -4.33% | -20.60% | 14.98% | 36.36% | 55.50% | 72.50% | 5.41% | 36.76% | 105.22% |
| SOL-USD | SAME_BTC_REGIME | 23 | 91.30% | 9.53% | 19.49% | 40.31% | -3.06% | -10.69% | 15.01% | 27.20% | 40.82% | 73.91% | 2.71% | 23.32% | 77.78% |
| SOL-USD | SAME_ASSET_REGIME | 30 | 73.33% | 9.42% | 17.91% | 42.46% | -3.45% | -20.60% | 13.49% | 23.75% | 56.49% | 70.00% | 4.61% | 28.82% | 80.60% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 19 | 89.47% | 9.45% | 14.56% | 24.41% | -3.06% | -10.47% | 14.26% | 19.57% | 37.44% | 68.42% | 2.51% | 14.56% | 77.45% |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 14 | 85.71% | 10.38% | -4.25% | 32.90% | 57.14% | 2.99% | 32.90% |
| BTC-USD | HISTORICAL_BTC_BULL | 22 | 68.18% | 19.31% | -3.60% | 43.89% | 63.64% | 30.11% | 62.95% |
| BTC-USD | HISTORICAL_BTC_MIXED | 1 | 100.00% | 44.12% | -4.48% | 54.19% | 100.00% | 41.64% | 108.28% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 3 | 33.33% | -11.19% | -20.14% | 3.93% | 66.67% | 16.42% | 19.52% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 22 | 81.82% | 7.13% | -10.31% | 22.19% | 77.27% | 11.89% | 55.83% |
| DOGE-USD | HISTORICAL_BTC_BULL | 8 | 62.50% | 4.54% | -11.06% | 30.02% | 37.50% | -12.89% | 52.97% |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 0.00% | -8.74% | -20.84% | 2.91% | 100.00% | 14.25% | 20.66% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 9 | 33.33% | -10.84% | -18.65% | 19.23% | 33.33% | -6.60% | 65.99% |
| SOL-USD | HISTORICAL_BTC_BEAR | 23 | 91.30% | 9.53% | -3.06% | 27.20% | 73.91% | 2.71% | 41.84% |
| SOL-USD | HISTORICAL_BTC_BULL | 7 | 71.43% | 23.40% | -2.31% | 51.15% | 85.71% | 23.57% | 82.85% |
| SOL-USD | HISTORICAL_BTC_MIXED | 1 | 100.00% | 44.12% | -4.48% | 54.19% | 100.00% | 41.64% | 108.28% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 9 | 22.22% | -10.22% | -20.14% | 4.69% | 55.56% | 18.07% | 111.01% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 21 | 90.48% | 14.84% | -2.71% | 42.19% | 71.43% | 10.45% | 59.40% |
| BTC-USD | HISTORICAL_ASSET_BULL | 11 | 45.45% | -19.69% | -26.89% | 28.98% | 45.45% | -26.19% | 54.07% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 100.00% | 49.35% | 0.00% | 64.13% | 100.00% | 46.87% | 64.13% |
| BTC-USD | HISTORICAL_ASSET_MIXED | 3 | 66.67% | 33.93% | -4.48% | 45.34% | 66.67% | 9.42% | 72.39% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 4 | 50.00% | -1.17% | -12.13% | 33.38% | 50.00% | -6.07% | 39.45% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 26 | 76.92% | 7.13% | -10.31% | 22.19% | 76.92% | 14.66% | 68.77% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 5 | 60.00% | 7.72% | -6.55% | 33.07% | 40.00% | -5.85% | 75.34% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 9 | 33.33% | -7.26% | -17.65% | 18.25% | 22.22% | -8.44% | 18.25% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 30 | 73.33% | 9.42% | -3.45% | 23.75% | 70.00% | 4.61% | 62.89% |
| SOL-USD | HISTORICAL_ASSET_BULL | 4 | 50.00% | 2.34% | -8.74% | 29.92% | 75.00% | 4.36% | 128.48% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 100.00% | 30.90% | -1.74% | 30.90% | 100.00% | 35.13% | 47.19% |
| SOL-USD | HISTORICAL_ASSET_MIXED | 2 | 100.00% | 39.02% | -2.24% | 49.77% | 100.00% | 25.53% | 90.33% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 3 | 66.67% | 14.95% | -10.48% | 30.87% | 66.67% | 2.44% | 65.72% |

## Top regime-adjusted matches

The table below shows the top matches separately for each target, so BTC does not hide SOL and DOGE.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | LRC-USD | 2018-10-04 | 89.87% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 35.30% | -5.72% | 154.28% | 57.00% | -5.72% | 154.28% |
| BTC-USD | ONE-USD | 2020-01-27 | 89.20% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 9.39% | -4.18% | 11.48% | -11.35% | -20.74% | 11.52% |
| BTC-USD | XRP-USD | 2025-12-21 | 88.61% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 3.53% | -0.53% | 11.68% | 0.43% | -1.24% | 12.21% |
| BTC-USD | ETH-USD | 2025-12-21 | 87.92% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 11.36% | 0.00% | 19.65% | -0.57% | -0.79% | 19.65% |
| BTC-USD | BTC-USD | 2018-10-06 | 87.84% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 2.83% | -4.32% | 4.94% | 10.45% | -4.32% | 16.59% |
| BTC-USD | XRP-USD | 2019-10-14 | 87.28% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 14.85% | -7.06% | 41.18% | -33.30% | -41.12% | 41.18% |
| BTC-USD | BNB-USD | 2018-10-04 | 86.00% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 51.62% | -8.34% | 51.62% | 153.58% | -8.34% | 153.58% |
| BTC-USD | XTZ-USD | 2025-12-26 | 85.96% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 3.95% | -2.03% | 10.38% | -15.12% | -15.41% | 15.04% |
| BTC-USD | BTC-USD | 2025-12-23 | 85.89% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 14.84% | -1.75% | 15.54% | 8.08% | -1.75% | 20.65% |
| BTC-USD | QTUM-USD | 2020-01-27 | 85.83% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 19.22% | -8.83% | 22.12% | 9.44% | -8.83% | 22.12% |
| DOGE-USD | OP-USD | 2025-12-22 | 90.20% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 8.81% | -3.72% | 21.82% | 8.70% | -3.72% | 56.00% |
| DOGE-USD | VET-USD | 2022-03-14 | 89.92% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 7.68% | -8.95% | 11.10% | 9.39% | -8.95% | 41.71% |
| DOGE-USD | THETA-USD | 2022-03-16 | 89.11% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 0.32% | -16.14% | 13.49% | -6.06% | -16.14% | 28.27% |
| DOGE-USD | LTC-USD | 2018-04-14 | 88.66% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -32.24% | -35.07% | 7.37% | -31.89% | -37.88% | 7.37% |
| DOGE-USD | HBAR-USD | 2022-03-14 | 88.65% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -2.78% | -18.79% | 1.28% | -7.73% | -18.79% | 12.96% |
| DOGE-USD | ENJ-USD | 2022-03-17 | 88.38% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 7.44% | -14.62% | 14.24% | 4.04% | -14.62% | 29.60% |
| DOGE-USD | FIL-USD | 2022-03-16 | 88.18% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -3.69% | -12.34% | 5.53% | 8.99% | -12.34% | 69.70% |
| DOGE-USD | DASH-USD | 2022-03-12 | 88.14% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 13.34% | -9.62% | 18.11% | 13.82% | -9.62% | 28.65% |
| DOGE-USD | INJ-USD | 2022-03-14 | 87.99% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -0.78% | -13.07% | 7.82% | 19.15% | -13.07% | 55.30% |
| DOGE-USD | RUNE-USD | 2022-03-08 | 87.94% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 6.81% | -22.98% | 22.31% | 37.54% | -22.98% | 46.15% |
| SOL-USD | NEAR-USD | 2025-12-21 | 80.32% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 14.29% | 0.00% | 23.51% | 104.94% | 0.00% | 139.37% |
| SOL-USD | RUNE-USD | 2025-12-27 | 78.73% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 41.91% | -0.37% | 41.91% | -5.22% | -5.22% | 62.96% |
| SOL-USD | LINK-USD | 2025-12-21 | 78.70% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 5.89% | 0.00% | 11.78% | 4.70% | 0.00% | 24.41% |
| SOL-USD | BNB-USD | 2025-12-26 | 78.36% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 4.95% | -0.18% | 8.46% | 4.52% | -0.18% | 21.01% |
| SOL-USD | EOS-USD | 2018-10-19 | 77.70% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 47.40% | -7.62% | 75.20% | 77.34% | -7.62% | 77.34% |
| SOL-USD | SOL-USD | 2025-12-24 | 77.68% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 6.75% | 0.00% | 12.72% | 2.71% | 0.00% | 23.30% |
| SOL-USD | ONE-USD | 2020-01-27 | 77.55% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 9.39% | -4.18% | 11.48% | -11.35% | -20.74% | 11.52% |
| SOL-USD | BTC-USD | 2025-12-23 | 76.74% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 14.84% | -1.75% | 15.54% | 8.08% | -1.75% | 20.65% |
| SOL-USD | DOT-USD | 2025-12-21 | 76.18% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -2.50% | -6.20% | 7.56% | -4.04% | -6.20% | 11.28% |
| SOL-USD | KAVA-USD | 2025-12-21 | 76.08% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 5.72% | -7.96% | 14.26% | 2.51% | -7.96% | 24.10% |

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

Generato: 2026-07-29 05:14 UTC


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
| BTC | 63.922 $ | -6 | RIBASSISTA / FRAGILE | STAGE 4 / MARKDOWN | MASSIMI E MINIMI CRESCENTI | ACCUMULO POSSIBILE / RANGE BASSO | BASSO | RIDUCI RISCHIO / NO LONG A LEVA |
| SOL | 73,47 $ | -11 | RIBASSISTA / FRAGILE | STAGE 4 / MARKDOWN | COMPRESSIONE / TRIANGOLO POSSIBILE | MARKDOWN / DEBOLEZZA | BASSO | NON INSEGUIRE / TAKE PROFIT SU SPIKE |
| DOGE | 0.07061 $ | -2 | DEBOLE / NON CONFERMATO | STAGE 4 / MARKDOWN | MASSIMI E MINIMI DECRESCENTI | SPRING / TEST POSSIBILE | BASSO | NO LONG / SHORT SOLO DOPO SPIKE E REJECTION |

## Punteggi per area

| Asset | Trend | Struttura | Momentum | Volume | Prezzo | Candela | Wyckoff | Totale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | -4 | +2 | -3 | -1 | 0 | 0 | 0 | -6 |
| SOL | -4 | 0 | -3 | -2 | 0 | 0 | -2 | -11 |
| DOGE | -4 | -2 | +3 | 0 | 0 | 0 | +1 | -2 |

## Livelli tecnici

| Asset | Supporto | Resistenza | Breakout 60g | Breakdown 60g | ATR14 | Rendimento 30g | Rendimento 90g |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 63.062 $ | 64.186 $ | 77.991 $ | 57.748 $ | 2,12% | 7,36% | -15,65% |
| SOL | 73,47 $ | 74,89 $ | 86,37 $ | 60,41 $ | 2,75% | 3,02% | -11,51% |
| DOGE | 0.06961 $ | 0.07377 $ | 0.10365 $ | 0.06829 $ | 3,00% | -3,40% | -32,12% |

## Lettura dettagliata

### BTC

- Prezzo: **63.922 $**
- Score classico: **-6 / 12**
- Verdetto: **RIBASSISTA / FRAGILE**
- Azione coerente: **RIDUCI RISCHIO / NO LONG A LEVA**
- Volatilità tecnica locale: **BASSO** — ATR14 2,12%; distanza supporto 1,35%; distanza resistenza 0,42%

Dettaglio:

- Trend: **-4** — prezzo sotto MA200 daily; MA50 daily in discesa; MA200 daily in discesa; STAGE 4 / MARKDOWN
- Stage weekly: **STAGE 4 / MARKDOWN** — Prezzo sotto MA30 weekly con MA30 in discesa.
- Struttura: **+2** — MASSIMI E MINIMI CRESCENTI
- Momentum: **-3** — RSI neutrale 48.6; RSI in peggioramento; MACD sotto signal; istogramma MACD in peggioramento
- Volume: **-1** — OBV sotto media; CMF neutrale 0.05; volume ratio 0.98
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **0** — ACCUMULO POSSIBILE / RANGE BASSO. Prezzo nella metà bassa del range, ma senza spring confermato.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 48.59 |
| MACD histogram | -79.26040 |
| CMF20 | 0.049 |
| Volume ratio 20 | 0.98 |
| MA20 | 64.412 $ |
| MA50 | 63.291 $ |
| MA100 | 69.440 $ |
| MA200 | 71.860 $ |
| Pendenza MA50 20g | -3,99% |
| Pendenza MA200 60g | -9,96% |
| Bollinger width | 6,15% |
| Bollinger position | 0.37 |

### SOL

- Prezzo: **73,47 $**
- Score classico: **-11 / 12**
- Verdetto: **RIBASSISTA / FRAGILE**
- Azione coerente: **NON INSEGUIRE / TAKE PROFIT SU SPIKE**
- Volatilità tecnica locale: **BASSO** — ATR14 2,75%; distanza supporto 0,00%; distanza resistenza 1,93%

Dettaglio:

- Trend: **-4** — prezzo sotto MA200 daily; MA200 daily in discesa; STAGE 4 / MARKDOWN
- Stage weekly: **STAGE 4 / MARKDOWN** — Prezzo sotto MA30 weekly con MA30 in discesa.
- Struttura: **0** — COMPRESSIONE / TRIANGOLO POSSIBILE
- Momentum: **-3** — RSI neutrale 43.2; RSI in peggioramento; MACD sotto signal; istogramma MACD in peggioramento
- Volume: **-2** — OBV sotto media; CMF negativo -0.07; volume ratio 1.13
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **-2** — MARKDOWN / DEBOLEZZA. Prezzo basso nel range e sotto medie principali.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 43.18 |
| MACD histogram | -0.44037 |
| CMF20 | -0.065 |
| Volume ratio 20 | 1.13 |
| MA20 | 76,20 $ |
| MA50 | 74,26 $ |
| MA100 | 79,01 $ |
| MA200 | 87,41 $ |
| Pendenza MA50 20g | -1,03% |
| Pendenza MA200 60g | -16,88% |
| Bollinger width | 8,43% |
| Bollinger position | 0.06 |

### DOGE

- Prezzo: **0.07061 $**
- Score classico: **-2 / 12**
- Verdetto: **DEBOLE / NON CONFERMATO**
- Azione coerente: **NO LONG / SHORT SOLO DOPO SPIKE E REJECTION**
- Volatilità tecnica locale: **BASSO** — ATR14 3,00%; distanza supporto 1,44%; distanza resistenza 4,47%

Dettaglio:

- Trend: **-4** — prezzo sotto MA200 daily; medie daily allineate ribassiste; MA50 daily in discesa; MA200 daily in discesa; STAGE 4 / MARKDOWN
- Stage weekly: **STAGE 4 / MARKDOWN** — Prezzo sotto MA30 weekly con MA30 in discesa.
- Struttura: **-2** — MASSIMI E MINIMI DECRESCENTI
- Momentum: **+3** — RSI neutrale 40.9; RSI in miglioramento; MACD sopra signal; istogramma MACD in miglioramento
- Volume: **0** — OBV sopra media; CMF negativo -0.05; volume ratio 1.06
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **+1** — SPRING / TEST POSSIBILE. Ha bucato un minimo importante e ha recuperato: possibile spring, da confermare.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 40.94 |
| MACD histogram | 0.00024 |
| CMF20 | -0.053 |
| Volume ratio 20 | 1.06 |
| MA20 | 0.07229 $ |
| MA50 | 0.07677 $ |
| MA100 | 0.08944 $ |
| MA200 | 0.09603 $ |
| Pendenza MA50 20g | -11,17% |
| Pendenza MA200 60g | -16,39% |
| Bollinger width | 8,18% |
| Bollinger position | 0.21 |

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

Generato: 2026-07-29 05:14 UTC


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
| BTC | 63.922 $ | Doppio massimo | CANDIDATO | ribassista | n/a | 48.247 $ | n/a | 10,69% | Fib 38,2% TENUTO (0) @ 63.410 $ | NEL RANGE | 62.553 $ |
| SOL | 73,47 $ | Doppio massimo | CANDIDATO | ribassista | n/a | 50,11 $ | n/a | 14,05% | Fib 23,6% TESTATO (0) @ 74,40 $ | NEL RANGE | 73,40 $ |
| DOGE | 0.07061 $ | Triplo massimo | MATURO | ribassista | 2026-06-24 | 0.05847 $ | 38,14% | n/a | Fib 23,6% NON ATTIVO (0) @ 0.08008 $ | NEL RANGE | 0.06961 $ |

## BTC

![Classic visual BTC](classic_visual_BTC.png)

- Pattern principale: **Doppio massimo**
- Stato pattern: **CANDIDATO** (0)
- Famiglia: **ribassista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-06-15 -> 2026-07-21**
- Età formazione: **8 giorni**
- Breakout pattern: **n/a**
- Età breakout: **n/a**
- Neckline: **57.748 $**
- Target teorico: **48.247 $**
- Progresso verso target: **n/a**
- Distanza dalla neckline: **10,69%**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 38,2% TENUTO (0) @ 63.410 $** — Swing UP 2026-07-01 57.748 -> 2026-07-21 66.910; livello più vicino 38.2% a 63.410; stato TENUTO; confluenza: nessuna confluenza indipendente.
- Invalidazione: **58.903 $**
- Relazione prezzo/neckline: **sopra neckline**
- Dettaglio: Due massimi simili vicino a 67.248 tra 2026-06-15 e 2026-07-21. Neckline ribassista stimata: 57.748. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 8 giorni. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **NEL RANGE**
- Supporto: **62.553 $**
- Resistenza: **65.508 $**
- Breakout 60g: **77.991 $**
- Breakdown 60g: **57.748 $**
- RSI14: **48.62**
- ATR14: **2,12%**
- Volume ratio 20g: **0.98**
- Rendimento 30g: **+7,37%**
- Rendimento 90g: **-15,64%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Doppio massimo | CANDIDATO | 0 | ribassista | 57.748 $ | n/a | n/a | 48.247 $ | n/a | 10,69% | 58.903 $ | Due massimi simili a 67.248 $ e 66.910 $. Neckline circa 57.748 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 8 giorni. |
| Doppio minimo | CANDIDATO | 0 | rialzista | 67.248 $ | n/a | n/a | 76.748 $ | n/a | 5,20% | 65.903 $ | Due minimi simili a 59.109 $ e 57.748 $. Neckline circa 67.248 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 28 giorni. |

## SOL

![Classic visual SOL](classic_visual_SOL.png)

- Pattern principale: **Doppio massimo**
- Stato pattern: **CANDIDATO** (0)
- Famiglia: **ribassista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-06-15 -> 2026-07-21**
- Età formazione: **8 giorni**
- Breakout pattern: **n/a**
- Età breakout: **n/a**
- Neckline: **64,42 $**
- Target teorico: **50,11 $**
- Progresso verso target: **n/a**
- Distanza dalla neckline: **14,05%**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 23,6% TESTATO (0) @ 74,40 $** — Swing UP 2026-06-06 60,41 -> 2026-07-21 78,73; livello più vicino 23.6% a 74,40; stato TESTATO; confluenza: supporto tecnico.
- Invalidazione: **65,71 $**
- Relazione prezzo/neckline: **sopra neckline**
- Dettaglio: Due massimi simili vicino a 78,73 tra 2026-06-15 e 2026-07-21. Neckline ribassista stimata: 64,42. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 8 giorni. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **NEL RANGE**
- Supporto: **73,40 $**
- Resistenza: **74,89 $**
- Breakout 60g: **86,37 $**
- Breakdown 60g: **60,41 $**
- RSI14: **43.18**
- ATR14: **2,75%**
- Volume ratio 20g: **1.13**
- Rendimento 30g: **+3,02%**
- Rendimento 90g: **-11,51%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Doppio massimo | CANDIDATO | 0 | ribassista | 64,42 $ | n/a | n/a | 50,11 $ | n/a | 14,05% | 65,71 $ | Due massimi simili a 75,94 $ e 78,73 $. Neckline circa 64,42 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 8 giorni. |
| Testa e spalle inverso | CANDIDATO | 0 | rialzista | 79,35 $ | n/a | n/a | 94,28 $ | n/a | 8,00% | 77,76 $ | Spalla sinistra 67,92 $, testa 64,42 $, spalla destra 73,40 $. Neckline circa 79,35 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 12 giorni. |
| Doppio minimo | CANDIDATO | 0 | rialzista | 98,27 $ | n/a | n/a | 114,91 $ | n/a | 33,75% | 96,30 $ | Due minimi simili a 81,63 $ e 81,69 $. Neckline circa 98,27 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 67 giorni. |
| Testa e spalle | TARGET RAGGIUNTO | 0 | ribassista | 82,57 $ | 2026-05-28 | 62g | 66,88 $ | 58,00% | n/a | 84,22 $ | Spalla sinistra 88,05 $, testa 98,27 $, spalla destra 87,79 $. Neckline circa 82,57 $. Breakout neckline: 2026-05-28 (62 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 66,88 $; progresso: 58,00%; prezzo sotto neckline. |

## DOGE

![Classic visual DOGE](classic_visual_DOGE.png)

- Pattern principale: **Triplo massimo**
- Stato pattern: **MATURO** (-1)
- Famiglia: **ribassista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-03-25 -> 2026-06-12**
- Età formazione: **47 giorni**
- Breakout pattern: **2026-06-24**
- Età breakout: **35 giorni**
- Neckline: **0.07809 $**
- Target teorico: **0.05847 $**
- Progresso verso target: **38,14%**
- Distanza dalla neckline: **n/a**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 23,6% NON ATTIVO (0) @ 0.08008 $** — Swing DOWN 2026-05-14 0.11825 -> 2026-07-24 0.06829; livello più vicino 23.6% a 0.08008; stato NON ATTIVO; confluenza: resistenza tecnica, neckline rialzista, invalidazione ribassista.
- Invalidazione: **0.07966 $**
- Relazione prezzo/neckline: **sotto neckline**
- Dettaglio: Tre massimi simili vicino a 0.09772 dal 2026-03-25 al 2026-06-12. Neckline ribassista stimata: 0.07809. Breakout neckline: 2026-06-24 (35 giorni fa). Stato: MATURO. Target teorico: 0.05847; progresso corrente: 38,14%. Relazione prezzo/neckline: sotto neckline. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **NEL RANGE**
- Supporto: **0.06961 $**
- Resistenza: **0.07923 $**
- Breakout 60g: **0.10365 $**
- Breakdown 60g: **0.06829 $**
- RSI14: **40.94**
- ATR14: **3,00%**
- Volume ratio 20g: **1.06**
- Rendimento 30g: **-3,40%**
- Rendimento 90g: **-32,12%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Triplo massimo | MATURO | -1 | ribassista | 0.07809 $ | 2026-06-24 | 35g | 0.05847 $ | 38,14% | n/a | 0.07966 $ | Tre massimi simili vicino a 0.09772 dal 2026-03-25 al 2026-06-12. Neckline ribassista stimata: 0.07809. Breakout neckline: 2026-06-24 (35 giorni fa). Stato: MATURO. Target teorico: 0.05847; progresso corrente: 38,14%. Relazione prezzo/neckline: sotto neckline. Fonte lifecycle: technical_structure_metrics.csv. |
| Doppio massimo | MATURO | -1 | ribassista | 0.07809 $ | 2026-06-24 | 35g | 0.06035 $ | 42,19% | n/a | 0.07966 $ | Due massimi simili a 0.09584 $ e 0.09169 $. Neckline circa 0.07809 $. Breakout neckline: 2026-06-24 (35 giorni fa). Stato: MATURO. Target teorico: 0.06035 $; progresso: 42,19%; prezzo sotto neckline. |
| Doppio minimo | CANDIDATO | 0 | rialzista | 0.07923 $ | n/a | n/a | 0.09017 $ | n/a | 12,21% | 0.07765 $ | Due minimi simili a 0.06961 $ e 0.06829 $. Neckline circa 0.07923 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 5 giorni. |
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

Generato: 2026-07-29 05:14 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [fractal_path_tracker.md](fractal_path_tracker.md)

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-07-29**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-01-13**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **73,47 $**
- Verdetto principale: **ANALOGIA DEBOLE / SCENARIO SECONDARIO**
- Somiglianza strutturale: **+60,46%**
- Aderenza live principale: **+68,64%**
- Errore medio live principale: **15,68%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE SOLO DI CONTESTO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **53**
- Osservazioni inclusive dal bottom: **54**
- Osservazioni da inizio programma/scanner: **27**
- Errore assoluto medio dal bottom: **10,85%**
- Errore assoluto medio da inizio programma: **15,68%**
- Gap firmato medio ultimi 7 giorni: **+6,14%**
- Errore assoluto medio ultimi 7 giorni: **8,02%**
- Gap ultimo giorno: **-6,32%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **-6,32%**
- Gap firmato medio 7g: **+6,14%**
- Errore assoluto medio 7g: **8,02%**
- Variazione recente gap: **-17,78%**
- Stato gap: **SOTTO IL FRATTALE**
- Trend gap: **SOL si sta allontanando sotto il percorso ancorato**

Soglie operative del grafico:

- entro **±5%**: percorso vicino;
- tra **±5% e ±12%**: deviazione gestibile;
- oltre **±12%**: frattale non abbastanza aderente per conferma operativa;
- oltre **±18%**: disallineamento marcato.

## Ultimi giorni del confronto ancorato

|   Giorno | Data SOL   | Data BTC eq.   | SOL reale   | Percorso ancorato   | Gap firmato   | Fase                |
|---------:|:-----------|:---------------|:------------|:--------------------|:--------------|:--------------------|
| 44 | 2026-07-20 | 2023-01-04 | 77,79 $ | 66,43 $ | +17,11% | da inizio programma |
| 45 | 2026-07-21 | 2023-01-05 | 78,11 $ | 66,32 $ | +17,77% | da inizio programma |
| 46 | 2026-07-22 | 2023-01-06 | 77,91 $ | 66,78 $ | +16,66% | da inizio programma |
| 47 | 2026-07-23 | 2023-01-07 | 75,86 $ | 66,79 $ | +13,58% | da inizio programma |
| 48 | 2026-07-24 | 2023-01-08 | 73,88 $ | 67,33 $ | +9,73% | da inizio programma |
| 49 | 2026-07-25 | 2023-01-09 | 74,43 $ | 67,74 $ | +9,87% | da inizio programma |
| 50 | 2026-07-26 | 2023-01-10 | 76,60 $ | 68,73 $ | +11,46% | da inizio programma |
| 51 | 2026-07-27 | 2023-01-11 | 74,14 $ | 70,65 $ | +4,94% | da inizio programma |
| 52 | 2026-07-28 | 2023-01-12 | 74,14 $ | 74,33 $ | -0,26% | da inizio programma |
| 53 | 2026-07-29 | 2023-01-13 | 73,47 $ | 78,43 $ | -6,32% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-08-05 | 89,33 $ | 83,68 $ | 73,47 $ / 83,68 $ | no | n/a | n/a | n/a |
| 14g | 2026-08-12 | 90,91 $ | 85,16 $ | 73,47 $ / 85,31 $ | no | n/a | n/a | n/a |
| 21g | 2026-08-19 | 92,37 $ | 86,53 $ | 73,47 $ / 87,73 $ | no | n/a | n/a | n/a |
| 28g | 2026-08-26 | 85,29 $ | 79,90 $ | 73,47 $ / 87,73 $ | no | n/a | n/a | n/a |
| 35g | 2026-09-02 | 96,77 $ | 90,65 $ | 73,47 $ / 90,65 $ | no | n/a | n/a | n/a |
| 42g | 2026-09-09 | 91,38 $ | 85,61 $ | 73,47 $ / 91,62 $ | no | n/a | n/a | n/a |
| 49g | 2026-09-16 | 88,09 $ | 82,52 $ | 73,47 $ / 91,62 $ | no | n/a | n/a | n/a |
| 56g | 2026-09-23 | 79,52 $ | 74,49 $ | 73,47 $ / 91,62 $ | no | n/a | n/a | n/a |
| 63g | 2026-09-30 | 108,03 $ | 101,20 $ | 73,47 $ / 101,20 $ | no | n/a | n/a | n/a |
| 70g | 2026-10-07 | 108,30 $ | 101,46 $ | 73,47 $ / 104,56 $ | no | n/a | n/a | n/a |
| 77g | 2026-10-14 | 112,18 $ | 105,09 $ | 73,47 $ / 105,09 $ | no | n/a | n/a | n/a |
| 84g | 2026-10-21 | 110,01 $ | 103,05 $ | 73,47 $ / 105,09 $ | no | n/a | n/a | n/a |
| 91g | 2026-10-28 | 120,09 $ | 112,50 $ | 73,47 $ / 112,50 $ | no | n/a | n/a | n/a |
| 98g | 2026-11-04 | 107,45 $ | 100,66 $ | 73,47 $ / 112,50 $ | no | n/a | n/a | n/a |
| 105g | 2026-11-11 | 115,58 $ | 108,27 $ | 73,47 $ / 112,50 $ | no | n/a | n/a | n/a |
| 112g | 2026-11-18 | 116,34 $ | 108,99 $ | 73,47 $ / 112,50 $ | no | n/a | n/a | n/a |
| 119g | 2026-11-25 | 105,59 $ | 98,92 $ | 73,47 $ / 112,50 $ | no | n/a | n/a | n/a |
| 126g | 2026-12-02 | 105,93 $ | 99,23 $ | 73,47 $ / 112,50 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 15 | 26,67% | 4,58% | 11,79% |
| 14g | 8 | 12,50% | 8,55% | 7,10% |
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

Ultima lettura salvata: **2026-07-29** — SOL 73,47 $, gap -6,32%, somiglianza +60,46%.

Nel report principale lascio solo il link, così non diventa troppo lungo.

<!-- SOL_BTC_FRACTAL_HISTORY_END -->

</details>
<!-- COMPACT_SECTION_END:fractal_path -->

<!-- COMPACT_SECTION_START:exchange_microstructure -->
<details>
<summary><strong>🏦 Dati exchange, liquidità e leva</strong></summary>

<!-- EXCHANGE_MICROSTRUCTURE_START -->
# Dati exchange, liquidità e leva

Generato: 2026-07-29 05:14 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [exchange_microstructure_report.md](exchange_microstructure_report.md)

Questo modulo legge Kraken Futures, Bitget Futures e KuCoin Futures come nucleo derivati. OKX e Coinbase vengono raccolti come fonti ausiliarie non pesate.
Non modifica la formula matematica di RSI, Fibonacci o Wyckoff: controlla se quei segnali sono sostenuti da acquisti, vendite, OI, funding e liquidità.

**Limite importante:** questo nucleo non assume disponibile un feed pubblico completo delle liquidazioni. La componente liquidazioni resta neutrale; le zone future restano stime di pressione, non dati certi delle singole posizioni.

Diagnostica completa: [exchange_source_diagnostics.md](exchange_source_diagnostics.md)

## Sintesi

| Asset | Prezzo | Exchange | Segnale candidato | Peso Global | Bias exchange | Confidenza | Copertura | Funding 8h eq. | OI 24h | Taker flow (campione/4h) | Book 0,5% | Liq long campione | Liq short campione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 63.940 $ | 3 | 0 | 0 | LEGGERMENTE POSITIVA / NON PESATA | MEDIA | 100% | +0,0066% | -1,46% | 1,94 | +5,06% | 0 $ | 0 $ |
| SOL | 73,46 $ | 3 | 0 | 0 | LEGGERMENTE POSITIVA / NON PESATA | MEDIA | 100% | -0,0032% | +1,25% | 2,01 | +1,41% | 0 $ | 0 $ |
| DOGE | 0.07058 $ | 3 | 0 | 0 | LEGGERMENTE POSITIVA / NON PESATA | MEDIA | 100% | +0,0049% | -0,21% | 2,01 | +3,11% | 0 $ | 0 $ |

Il segnale candidato è limitato a **±1**, ma il peso nel Global resta **0** finché il tracker a 7 giorni non raggiunge 30 controlli, almeno 55% di accuratezza e return corretto direzione positivo. Un singolo muro o funding non basta.

La colonna taker usa un campione recente nel primo run. Dopo almeno 3 fotografie distribuite su almeno 45 minuti viene sostituita automaticamente dalla media intraday 4h.

## Dati separati per exchange

| Asset | Exchange | Stato | Funding 8h eq. | Open interest | Taker flow | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | Kraken | OK | +0,0160% | 127,27 mln $ | 3,39 | +2,84% |
| BTC | Bitget | OK | +0,0070% | 2,19 mld $ | 0,01 | +63,72% |
| BTC | Kucoin | OK | +0,0100% | 1,52 mld $ | 1,59 | +12,72% |
| SOL | Kraken | OK | +0,0203% | 16,09 mln $ | 1,03 | +5,32% |
| SOL | Bitget | OK | -0,0004% | 336,58 mln $ | 3,78 | +14,98% |
| SOL | Kucoin | OK | -0,0088% | 227,91 mln $ | 2,39 | +0,15% |
| DOGE | Kraken | OK | +0,0110% | 4,35 mln $ | 0,64 | +12,36% |
| DOGE | Bitget | OK | +0,0024% | 88,62 mln $ | 13,29 | -6,15% |
| DOGE | Kucoin | OK | +0,0061% | 114,44 mln $ | 9,04 | -5,39% |

Kraken, Bitget e KuCoin contribuiscono a funding normalizzato, open interest, trade aggressivi e order book. Non viene inventato un long/short ratio pubblico né un feed completo delle liquidazioni.

## Conferme per indicatori tecnici

### BTC

- Score grezzo exchange: **+2,38**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 1, accuratezza +100,00%.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 2, bear 1, divergenze 0.
- Flusso taker/order book: **+1,75**.
- OI/funding/basis: **+0,00**.
- Affollamento long/short: **+0,00**.
- Liquidazioni: **NON PESATE / FEED COMPLETO NON ASSUNTO DISPONIBILE**.
- **Wyckoff:** Possibile accumulazione/spring sostenuto da pressione compratrice o assorbimento.
- **Fibonacci:** Fibonacci tenuto con acquisti/assorbimento coerenti: conferma positiva.
- **RSI:** RSI in zona non estrema o flusso exchange non abbastanza netto.
- **Pattern:** I pattern candidati restano non operativi: i dati exchange possono solo preparare la conferma.
- **Breakout/breakdown:** Prezzo non abbastanza vicino a un livello chiave o flusso non netto.
- **Mappa liquidità attuale:** muro bid: n/a; muro ask: n/a

![Microstruttura exchange BTC](exchange_microstructure_BTC.png)

### SOL

- Score grezzo exchange: **+2,38**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 1, accuratezza +0,00%.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 2, bear 0, divergenze 0.
- Flusso taker/order book: **+1,75**.
- OI/funding/basis: **+0,00**.
- Affollamento long/short: **+0,00**.
- Liquidazioni: **NON PESATE / FEED COMPLETO NON ASSUNTO DISPONIBILE**.
- **Wyckoff:** Possibile accumulazione/spring sostenuto da pressione compratrice o assorbimento.
- **Fibonacci:** Livello Fibonacci soltanto testato: order book e taker flow non bastano ancora per dichiararlo tenuto o perso. Confluenza tecnica dichiarata: supporto tecnico.
- **RSI:** RSI in zona non estrema o flusso exchange non abbastanza netto.
- **Pattern:** I pattern candidati restano non operativi: i dati exchange possono solo preparare la conferma.
- **Breakout/breakdown:** Supporto vicino con assorbimento/acquisti: tenuta più credibile.
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
- **Fibonacci:** Fibonacci non_attivo; nessuna conferma exchange netta. Confluenza tecnica dichiarata: resistenza tecnica, neckline rialzista, invalidazione ribassista.
- **RSI:** RSI in zona non estrema o flusso exchange non abbastanza netto.
- **Pattern:** I pattern candidati restano non operativi: i dati exchange possono solo preparare la conferma.
- **Breakout/breakdown:** Prezzo non abbastanza vicino a un livello chiave o flusso non netto.
- **Mappa liquidità attuale:** muro bid: n/a; muro ask: n/a

![Microstruttura exchange DOGE](exchange_microstructure_DOGE.png)

## Overlay sulle previsioni a 30 giorni

La previsione storica grezza dello scanner resta intatta. L'overlay exchange può correggerla solo dopo almeno 30 controlli maturati a 30 giorni e solo se il modulo dimostra accuratezza direzionale almeno del 55%.

| Asset | Prob. grezza salita | Return p50 grezzo | Controlli 30g | Accuratezza exchange | Stato overlay | Peso | Prob. corretta | Return corretto |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +72,50% | +13,10% | 0 | n/a | RACCOLTA DATI | 0,00 | +72,50% | +13,10% |
| SOL | +72,50% | +9,45% | 0 | n/a | RACCOLTA DATI | 0,00 | +72,50% | +9,45% |
| DOGE | +65,00% | +4,54% | 0 | n/a | RACCOLTA DATI | 0,00 | +65,00% | +4,54% |

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

Generato: 2026-07-29 05:14 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [exchange_signal_tracker_report.md](exchange_signal_tracker_report.md)

Questo tracker verifica se il segnale candidato exchange ±1 anticipa correttamente la direzione del prezzo a 1/3/7/14/30 giorni.
Il peso Global resta 0 finché l'orizzonte 7g non ha almeno 30 controlli, accuratezza almeno 55% e return corretto direzione positivo. L'overlay a 30g ha un gate separato.

Controlli maturati completati in questa esecuzione: **12**.

## Ultime fotografie giornaliere

| Data | Asset | Prezzo | Versione | Calibrazione | Candidato | Peso Global | Score raw | Confidenza | Taker 4h | OI 24h | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-07-29 | BTC | 63.939,70 | V2.1.3 | OK | 0 | 0 | 2,38 | MEDIA | 1,94 | -1,46% | +5,06% |
| 2026-07-29 | DOGE | 0.07058 | V2.1.3 | OK | 0 | 0 | 2,12 | MEDIA | 2,01 | -0,21% | +3,11% |
| 2026-07-29 | SOL | 73,46 | V2.1.3 | OK | 0 | 0 | 2,38 | MEDIA | 2,01 | +1,25% | +1,41% |
| 2026-07-28 | BTC | 63.446,30 | V2.1.3 | OK | 0 | 0 | 2,12 | MEDIA | 2,67 | -1,38% | +7,93% |
| 2026-07-28 | DOGE | 0.07006 | V2.1.3 | OK | 0 | 0 | 0,75 | BASSA | 0,95 | +1,18% | -4,54% |
| 2026-07-28 | SOL | 73,32 | V2.1.3 | OK | 0 | 0 | 2,88 | MEDIA | 1,49 | -14,97% | -7,39% |
| 2026-07-27 | BTC | 65.281,70 | V2.1.3 | OK | 0 | 0 | 2,12 | MEDIA | 2,18 | -3,17% | +5,05% |
| 2026-07-27 | DOGE | 0.07287 | V2.1.3 | OK | 0 | 0 | 2,38 | MEDIA | 1,27 | +1,92% | +1,33% |
| 2026-07-27 | SOL | 76,31 | V2.1.3 | OK | 0 | 0 | 2,25 | MEDIA | 1,33 | -3,21% | +2,79% |

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
| BTC | 63.922 $ | +0.0032% | -3.04% | 2.01 | Misto | 1/5 |
| SOL | 73,47 $ | -0.0023% | -0.67% | 2.15 | Misto | 1/5 |
| DOGE | 0.07061 $ | +0.0027% | -22.98% | 3.27 | Misto | 1/5 |

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

Generato: 2026-07-29 05:14 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [rsi_multitimeframe_divergence_report.md](rsi_multitimeframe_divergence_report.md)

Il modulo confronta prezzo e RSI 14 sui pivot confermati **daily e weekly**. Riconosce divergenze regolari e nascoste, segnali in formazione, invalidazioni e semplice conferma del momentum.

**Peso operativo: 0.** Non modifica il Global Confluence, non cambia le soglie del Paper Trading e non apre né blocca operazioni. I risultati vengono misurati prima di qualsiasi futura decisione sul peso.

## Sintesi corrente

| Asset   | Daily               | Stato D       | Weekly              | Stato W    | Lettura weekly                                                                                                                |   Peso |
|:--------|:--------------------|:--------------|:--------------------|:-----------|:------------------------------------------------------------------------------------------------------------------------------|-------:|
| BTC     | Bullish regolare    | CONFERMATA    | Bullish regolare    | CONFERMATA | Bullish regolare confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto. |      0 |
| SOL     | Conferma ribassista | CONTESTO      | Hidden bearish      | CONFERMATA | Hidden bearish confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto.   |      0 |
| DOGE    | Hidden bearish      | IN_FORMAZIONE | Conferma ribassista | CONTESTO   | Prezzo e RSI stanno scendendo insieme: momentum ribassista confermato, nessuna bullish divergence attiva.                     |      0 |

## Dettaglio dei pivot

| Asset   | TF   | Tipo                | Stato         | Prezzo / RSI      | Pivot confrontati                                                   | Δ prezzo contesto   | Δ RSI contesto   |   Peso |
|:--------|:-----|:--------------------|:--------------|:------------------|:--------------------------------------------------------------------|:--------------------|:-----------------|-------:|
| BTC     | 1D   | Bullish regolare    | CONFERMATA    | 63.908 $ / 48,56  | 2026-06-25 58.076 $ / RSI 30,46 → 2026-07-01 57.748 $ / RSI 37,26   | n/a                 | n/a              |      0 |
| BTC     | 1W   | Bullish regolare    | CONFERMATA    | 63.908 $ / 39,24  | 2026-06-07 59.109 $ / RSI 34,23 → 2026-07-05 57.748 $ / RSI 38,20   | n/a                 | n/a              |      0 |
| SOL     | 1D   | Conferma ribassista | CONTESTO      | 73,47 $ / 43,18   | n/a                                                                 | -5,52%              | -10,35           |      0 |
| SOL     | 1W   | Hidden bearish      | CONFERMATA    | 73,47 $ / 38,37   | 2026-05-17 98,27 $ / RSI 38,29 → 2026-07-05 83,81 $ / RSI 42,25     | n/a                 | n/a              |      0 |
| DOGE    | 1D   | Hidden bearish      | IN_FORMAZIONE | 0.07061 $ / 40,94 | 2026-07-04 0.07923 $ / RSI 41,65 → 2026-07-26 0.07380 $ / RSI 47,51 | n/a                 | n/a              |      0 |
| DOGE    | 1W   | Conferma ribassista | CONTESTO      | 0.07061 $ / 32,94 | n/a                                                                 | -14,07%             | -2,13            |      0 |

### BTC

- **1D — Bullish regolare / CONFERMATA**: Bullish regolare confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto.
- **1W — Bullish regolare / CONFERMATA**: Bullish regolare confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto.

### SOL

- **1D — Conferma ribassista / CONTESTO**: Prezzo e RSI stanno scendendo insieme: momentum ribassista confermato, nessuna bullish divergence attiva.
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

Generato: 2026-07-29 05:14 UTC


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

| Asset   | Prezzo   |   Punteggio | Verdetto           | Trend            | Momentum                  | Struttura                                             |   Pattern score | Fibonacci      | Pattern rialzista               | Pattern ribassista         | Supporto   | Resistenza   |
|:--------|:---------|------------:|:-------------------|:-----------------|:--------------------------|:------------------------------------------------------|----------------:|:---------------|:--------------------------------|:---------------------------|:-----------|:-------------|
| BTC | 63.922 $ | -3 | DEBOLE | Trend ribassista | Momentum debole | Volatilità in espansione | 0 | 0 / TENUTO | Doppio minimo / CANDIDATO | Doppio massimo / CANDIDATO | 57.748 | 66.910 |
| SOL | 73,47 $ | -8 | RIBASSISTA TECNICO | Trend ribassista | Momentum debole | Compressione / triangolo | 0 | 0 / TESTATO | Adam and Eve Bottom / CANDIDATO | Doppio massimo / CANDIDATO | 73,40 | 78,73 |
| DOGE | 0.07061 $ | -3 | DEBOLE | Trend ribassista | Momentum in miglioramento | Struttura ribassista con massimi e minimi decrescenti | -1 | 0 / NON ATTIVO | Doppio minimo / CANDIDATO | Triplo massimo / MATURO | 0.06829 | 0.07923 |

## Riepilogo ciclo di vita pattern

| Asset   | Doppio minimo   | Triplo minimo   | Adam/Eve Bottom                 | Doppio massimo   | Triplo massimo   | Adam/Eve Top                 |   Punteggio pattern |
|:--------|:----------------|:----------------|:--------------------------------|:-----------------|:-----------------|:-----------------------------|--------------------:|
| BTC | CANDIDATO | CANDIDATO | Adam and Eve Bottom — CANDIDATO | CANDIDATO | CANDIDATO | Adam and Eve Top — CANDIDATO | 0 |
| SOL | INVALIDATO | CANDIDATO | Adam and Eve Bottom — CANDIDATO | CANDIDATO | CANDIDATO | Adam and Eve Top — CANDIDATO | 0 |
| DOGE | CANDIDATO | CANDIDATO | Adam and Eve Bottom — CANDIDATO | ASSENTE | MATURO | Eve and Adam Top — MATURO | -1 |

## Indicatori tecnici

| Asset   |   RSI 14 |   Istogramma MACD | MA20    | MA50    | MA200   | Pendenza MA50 20g   | Pendenza MA200 60g   | Rendimento 30g   | Rendimento 90g   |
|:--------|---------:|------------------:|:--------|:--------|:--------|:--------------------|:---------------------|:-----------------|:-----------------|
| BTC | 48.62 | -78.8872 | 64.412 | 63.291 | 71.860 | -3,57% | -9,79% | 6,29% | -16,23% |
| SOL | 43.18 | -0.44037 | 76,20 | 74,26 | 87,41 | -0,81% | -16,59% | -1,97% | -11,51% |
| DOGE | 40.94 | 0.00024 | 0.07229 | 0.07677 | 0.09603 | -10,53% | -16,13% | -3,65% | -33,70% |

## Dettaglio asset

### BTC

- Prezzo: **63.922 $**
- Punteggio tecnico: **-3 / 12**
- Verdetto: **DEBOLE**
- Trend: **Trend ribassista** (-3)
- Momentum: **Momentum debole** (-3)
- Volume: **Volume neutrale** (0)
- Struttura: **Volatilità in espansione** (0)
  - Dettaglio struttura: Ultimi minimi: 5.808e+04 -> 5.775e+04. Ultimi massimi: 6.551e+04 -> 6.691e+04.
- Divergenza: **Divergenza rialzista RSI** (2)
- Fase Wyckoff candidata: **Possibile accumulazione** (1)
  - Dettaglio Wyckoff: Prezzo sotto MA200, vicino alla parte bassa del range a 120 giorni, RSI 48.6.
- Fibonacci automatico: **TENUTO** (0)
  - Swing UP 2026-07-01 57.748 -> 2026-07-21 66.910; livello più vicino 38.2% a 63.410; stato TENUTO; confluenza: nessuna confluenza indipendente.
- Punteggio pattern: **0**
  - rialzista dominante: Doppio minimo (CANDIDATO, 0); ribassista dominante: Doppio massimo (CANDIDATO, 0).
- Supporto più vicino: **57.748**
- Resistenza più vicina: **66.910**

Pattern classici e ciclo di vita:

- Doppio minimo: **CANDIDATO** (0)
  - Due minimi simili vicino a 57.748 tra 2026-06-05 e 2026-07-01. Neckline stimata: 67.248. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 28 giorni.
  - neckline 67.248; target 76.748; distanza dalla neckline 5,20%; prezzo sotto neckline.
- Triplo minimo: **CANDIDATO** (0)
  - Tre minimi simili vicino a 57.748 dal 2026-06-05 al 2026-07-01. Neckline stimata: 67.248. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 28 giorni.
  - neckline 67.248; target 76.748; distanza dalla neckline 5,20%; prezzo sotto neckline.
- Adam and Eve Bottom: **CANDIDATO** (0)
  - Pattern Adam and Eve Bottom vicino a 57.748 dal 2026-06-05 al 2026-07-01. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 67.248. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 28 giorni.
  - neckline 67.248; target 76.748; distanza dalla neckline 5,20%; prezzo sotto neckline.
- Doppio massimo: **CANDIDATO** (0)
  - Due massimi simili vicino a 67.248 tra 2026-06-15 e 2026-07-21. Neckline ribassista stimata: 57.748. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 8 giorni.
  - neckline 57.748; target 48.247; distanza dalla neckline 10,69%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 66.910 dal 2026-06-22 al 2026-07-21. Neckline ribassista stimata: 57.748. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 8 giorni.
  - neckline 57.748; target 48.585; distanza dalla neckline 10,69%; prezzo sopra neckline.
- Adam and Eve Top: **CANDIDATO** (0)
  - Pattern Adam and Eve Top vicino a 67.248 dal 2026-06-15 al 2026-07-21. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 57.748. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 8 giorni.
  - neckline 57.748; target 48.247; distanza dalla neckline 10,69%; prezzo sopra neckline.

### SOL

- Prezzo: **73,47 $**
- Punteggio tecnico: **-8 / 12**
- Verdetto: **RIBASSISTA TECNICO**
- Trend: **Trend ribassista** (-3)
- Momentum: **Momentum debole** (-3)
- Volume: **Volume da distribuzione** (-2)
- Struttura: **Compressione / triangolo** (0)
  - Dettaglio struttura: Ultimi minimi: 64.42 -> 73.4. Ultimi massimi: 78.88 -> 78.73.
- Divergenza: **Divergenza ribassista nascosta RSI** (-1)
- Fase Wyckoff candidata: **Possibile accumulazione** (1)
  - Dettaglio Wyckoff: Prezzo sotto MA200, vicino alla parte bassa del range a 120 giorni, RSI 43.2.
- Fibonacci automatico: **TESTATO** (0)
  - Swing UP 2026-06-06 60,41 -> 2026-07-21 78,73; livello più vicino 23.6% a 74,40; stato TESTATO; confluenza: supporto tecnico.
- Punteggio pattern: **0**
  - rialzista dominante: Adam and Eve Bottom (CANDIDATO, 0); ribassista dominante: Doppio massimo (CANDIDATO, 0).
- Supporto più vicino: **73,40**
- Resistenza più vicina: **78,73**

Pattern classici e ciclo di vita:

- Doppio minimo: **INVALIDATO** (0)
  - Due minimi simili vicino a 60,41 tra 2026-06-06 e 2026-06-25. Neckline stimata: 75,94. Breakout neckline: 2026-07-01 (28 giorni fa). Stato: INVALIDATO. Target teorico: 91,46; progresso corrente: -15,90%. Relazione prezzo/neckline: sotto neckline.
  - neckline 75,94; target 91,46; breakout 2026-07-01 (28g); progresso -15,90%; prezzo sotto neckline.
- Triplo minimo: **CANDIDATO** (0)
  - Tre minimi simili vicino a 81,63 dal 2026-04-29 al 2026-05-23. Neckline stimata: 98,27. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 67 giorni.
  - neckline 98,27; target 114,91; distanza dalla neckline 33,75%; prezzo sotto neckline.
- Adam and Eve Bottom: **CANDIDATO** (0)
  - Pattern Adam and Eve Bottom vicino a 67,92 dal 2026-06-19 al 2026-07-17. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 83,81. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 12 giorni.
  - neckline 83,81; target 99,70; distanza dalla neckline 14,07%; prezzo sotto neckline.
- Doppio massimo: **CANDIDATO** (0)
  - Due massimi simili vicino a 78,73 tra 2026-06-15 e 2026-07-21. Neckline ribassista stimata: 64,42. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 8 giorni.
  - neckline 64,42; target 50,11; distanza dalla neckline 14,05%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 78,88 dal 2026-06-15 al 2026-07-21. Neckline ribassista stimata: 64,42. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 8 giorni.
  - neckline 64,42; target 49,96; distanza dalla neckline 14,05%; prezzo sopra neckline.
- Adam and Eve Top: **CANDIDATO** (0)
  - Pattern Adam and Eve Top vicino a 78,73 dal 2026-06-15 al 2026-07-21. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 64,42. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 8 giorni.
  - neckline 64,42; target 50,11; distanza dalla neckline 14,05%; prezzo sopra neckline.

### DOGE

- Prezzo: **0.07061 $**
- Punteggio tecnico: **-3 / 12**
- Verdetto: **DEBOLE**
- Trend: **Trend ribassista** (-3)
- Momentum: **Momentum in miglioramento** (3)
- Volume: **Volume neutrale** (0)
- Struttura: **Struttura ribassista con massimi e minimi decrescenti** (-2)
  - Dettaglio struttura: Ultimi minimi: 0.07097 -> 0.06829. Ultimi massimi: 0.09169 -> 0.07923.
- Divergenza: **Divergenza ribassista nascosta RSI** (-1)
- Fase Wyckoff candidata: **Possibile accumulazione** (1)
  - Dettaglio Wyckoff: Prezzo sotto MA200, vicino alla parte bassa del range a 120 giorni, RSI 40.9.
- Fibonacci automatico: **NON ATTIVO** (0)
  - Swing DOWN 2026-05-14 0.11825 -> 2026-07-24 0.06829; livello più vicino 23.6% a 0.08008; stato NON ATTIVO; confluenza: resistenza tecnica, neckline rialzista, invalidazione ribassista.
- Punteggio pattern: **-1**
  - rialzista dominante: Doppio minimo (CANDIDATO, 0); ribassista dominante: Triplo massimo (MATURO, -1).
- Supporto più vicino: **0.06829**
- Resistenza più vicina: **0.07923**

Pattern classici e ciclo di vita:

- Doppio minimo: **CANDIDATO** (0)
  - Due minimi simili vicino a 0.06829 tra 2026-06-30 e 2026-07-24. Neckline stimata: 0.07923. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 5 giorni.
  - neckline 0.07923; target 0.09017; distanza dalla neckline 12,21%; prezzo sotto neckline.
- Triplo minimo: **CANDIDATO** (0)
  - Tre minimi simili vicino a 0.06829 dal 2026-06-30 al 2026-07-24. Neckline stimata: 0.07923. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 5 giorni.
  - neckline 0.07923; target 0.09017; distanza dalla neckline 12,21%; prezzo sotto neckline.
- Adam and Eve Bottom: **CANDIDATO** (0)
  - Pattern Adam and Eve Bottom vicino a 0.06829 dal 2026-06-30 al 2026-07-24. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 0.07923. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 5 giorni.
  - neckline 0.07923; target 0.09017; distanza dalla neckline 12,21%; prezzo sotto neckline.
- Doppio massimo: **ASSENTE** (0)
- Triplo massimo: **MATURO** (-1)
  - Tre massimi simili vicino a 0.09772 dal 2026-03-25 al 2026-06-12. Neckline ribassista stimata: 0.07809. Breakout neckline: 2026-06-24 (35 giorni fa). Stato: MATURO. Target teorico: 0.05847; progresso corrente: 38,14%. Relazione prezzo/neckline: sotto neckline.
  - neckline 0.07809; target 0.05847; breakout 2026-06-24 (35g); progresso 38,14%; prezzo sotto neckline.
- Eve and Adam Top: **MATURO** (-1)
  - Pattern Eve and Adam Top vicino a 0.09584 dal 2026-04-07 al 2026-06-12. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 0.07809. Breakout neckline: 2026-06-24 (35 giorni fa). Stato: MATURO. Target teorico: 0.06035; progresso corrente: 42,19%. Relazione prezzo/neckline: sotto neckline.
  - neckline 0.07809; target 0.06035; breakout 2026-06-24 (35g); progresso 42,19%; prezzo sotto neckline.

## Fibonacci automatico

Il modulo seleziona uno swing recente tramite pivot confermati. Un semplice tocco vale 0: Fibonacci pesa al massimo ±1 soltanto quando il livello è tenuto, perso, recuperato o respinto e coincide con almeno un livello tecnico indipendente.

| Asset   | Swing                         | 23,6%   | 38,2%   | 50,0%   | 61,8%   | 78,6%   | Livello vicino   | Stato      | Confluenza                                                       |   Score |
|:--------|:------------------------------|:--------|:--------|:--------|:--------|:--------|:-----------------|:-----------|:-----------------------------------------------------------------|--------:|
| BTC | UP 2026-07-01 -> 2026-07-21 | 64.748 | 63.410 | 62.329 | 61.248 | 59.708 | 38.2% / 63.410 | TENUTO | nessuna confluenza indipendente | 0 |
| SOL | UP 2026-06-06 -> 2026-07-21 | 74,40 | 71,73 | 69,57 | 67,41 | 64,33 | 23.6% / 74,40 | TESTATO | supporto tecnico | 0 |
| DOGE | DOWN 2026-05-14 -> 2026-07-24 | 0.08008 | 0.08738 | 0.09327 | 0.09917 | 0.10756 | 23.6% / 0.08008 | NON ATTIVO | resistenza tecnica, neckline rialzista, invalidazione ribassista | 0 |

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

- **BTC**: 0/30 previsioni controllate su 27 fatte. Stato: **RACCOLTA DATI**.
- **SOL**: 0/30 previsioni controllate su 27 fatte. Stato: **RACCOLTA DATI**.
- **DOGE**: 0/30 previsioni controllate su 27 fatte. Stato: **RACCOLTA DATI**.

| Asset | Previsioni fatte | Controllate | Progresso | In attesa | Stato | Prossimo controllo |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 27 | 0 | 0/30 [░░░░░░░░░░] | 27 | RACCOLTA DATI | 2026-08-02 / tra 4 giorni |
| SOL | 27 | 0 | 0/30 [░░░░░░░░░░] | 27 | RACCOLTA DATI | 2026-08-02 / tra 4 giorni |
| DOGE | 27 | 0 | 0/30 [░░░░░░░░░░] | 27 | RACCOLTA DATI | 2026-08-02 / tra 4 giorni |

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

Generato: 2026-07-29 05:15 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [data_quality_coherence_report.md](data_quality_coherence_report.md)

Questo controllo non modifica punteggi o decisioni. Verifica che tutti i moduli usino lo stesso prezzo corrente e che le nuove regole Technical/Classic Visual siano integre.

## Stato finale: **OK**

## Prezzo unico per modulo

| Modulo                  | Asset   | Campo             | Stato   | Prezzo snapshot   | Prezzo modulo   | Differenza   |
|:------------------------|:--------|:------------------|:--------|:------------------|:----------------|:-------------|
| Scanner                 | BTC     | current_price     | OK      | 63.922 $          | 63.922 $        | +0,0000%     |
| Scanner                 | DOGE    | current_price     | OK      | 0.07061 $         | 0.07061 $       | -0,0000%     |
| Scanner                 | SOL     | current_price     | OK      | 73,47 $           | 73,47 $         | +0,0000%     |
| Scanner Forecast        | BTC     | current_price     | OK      | 63.922 $          | 63.922 $        | +0,0000%     |
| Scanner Forecast        | SOL     | current_price     | OK      | 73,47 $           | 73,47 $         | +0,0000%     |
| Scanner Forecast        | DOGE    | current_price     | OK      | 0.07061 $         | 0.07061 $       | -0,0000%     |
| Technical Structure     | BTC     | price             | OK      | 63.922 $          | 63.922 $        | +0,0000%     |
| Technical Structure     | SOL     | price             | OK      | 73,47 $           | 73,47 $         | +0,0000%     |
| Technical Structure     | DOGE    | price             | OK      | 0.07061 $         | 0.07061 $       | -0,0000%     |
| Classic Technical       | BTC     | price             | OK      | 63.922 $          | 63.922 $        | +0,0000%     |
| Classic Technical       | SOL     | price             | OK      | 73,47 $           | 73,47 $         | +0,0000%     |
| Classic Technical       | DOGE    | price             | OK      | 0.07061 $         | 0.07061 $       | -0,0000%     |
| Classic Visual          | BTC     | price             | OK      | 63.922 $          | 63.922 $        | +0,0000%     |
| Classic Visual          | SOL     | price             | OK      | 73,47 $           | 73,47 $         | +0,0000%     |
| Classic Visual          | DOGE    | price             | OK      | 0.07061 $         | 0.07061 $       | -0,0000%     |
| Exchange Microstructure | BTC     | price             | OK      | 63.922 $          | 63.940 $        | +0,0282%     |
| Exchange Microstructure | SOL     | price             | OK      | 73,47 $           | 73,46 $         | -0,0109%     |
| Exchange Microstructure | DOGE    | price             | OK      | 0.07061 $         | 0.07058 $       | -0,0425%     |
| RSI top-cycle           | SOL     | current_price     | OK      | 73,47 $           | 73,47 $         | +0,0000%     |
| RSI top-cycle           | SOL     | current_price     | OK      | 73,47 $           | 73,47 $         | +0,0000%     |
| Frattale BTC/SOL        | SOL     | sol_current_price | OK      | 73,47 $           | 73,47 $         | +0,0000%     |
| Fractal path            | SOL     | current_price     | OK      | 73,47 $           | 73,47 $         | +0,0000%     |

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

Generato: 2026-07-29T08:17:34+00:00

- Modalità: **SOLO PAPER TRADING**
- Asset: **SOL spot**
- Leva: **nessuna (1x)**
- Capitale iniziale separato: **€40.000,00**
- Fonte mercato: **KUCOIN_PUBLIC_API**; nuove entrate: **CONSENTITE**

| Equity | Cash | SOL | Prezzo | Rendimento | Realizzato | Commissioni | Max DD | Operazioni |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €40.098,63 | €4.024,85 | 486.149894 | 74.2030 | +0.25% | €0,00 | €35,98 | 4.35% | 6 |

**Ultima decisione:** HOLD — Prezzo dentro la fascia neutrale.

Bande 4H: L2 69.9014 · L1 71.9902 · media 74.6012 · U1 77.2123 · U2 79.3011.

> Questo portafoglio non condivide capitale, posizioni o statistiche con il paper trading da €10.000.
<!-- SOL_SPOT_ADAPTIVE_END -->
