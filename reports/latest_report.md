<!-- COMPACT_REPORT_HEADER_START -->
> **Vista compatta:** Decisione operativa, Global Confluence e cambiamenti giornalieri restano aperti. Tocca il titolo di una sezione per mostrare o nascondere i dettagli.  
> Tutte le tabelle e tutti i dati restano nel file: copiando il Markdown raw viene copiato tutto.
<!-- COMPACT_REPORT_HEADER_END -->

<!-- COMPACT_SECTION_START:decision -->
<details open>
<summary><strong>🧭 Decisione operativa — da leggere per prima</strong></summary>

<!-- DECISION_REPORT_START -->

# Decisione operativa sintetica

Generato: 2026-08-05 05:15 UTC

Report separato completo: [decision_report.md](decision_report.md)

Sintesi automatica dello scanner: l'azione spot viene copiata direttamente dal Global Confluence; long, short e rischio restano filtri separati e più prudenti.

| Asset | Global | Direzione | Spot | Long leva | Short leva | Max long | Max short | Rischio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +2 | NEUTRALE / COSTRUTTIVO | HOLD / ATTESA CONFERME | NO LONG A LEVA / ATTENDI SOPRA 67.248 $ | NO SHORT | nessuna | nessuna | MEDIO / ALTO |
| SOL | +1 | NEUTRALE / INCERTO | HOLD LEGGERO / ATTESA CONFERME | NO LONG A LEVA | NO SHORT | nessuna | nessuna | MOLTO ALTO |
| DOGE | 0 | NEUTRALE / INCERTO | STAI ALLA FINESTRA | NO LONG A LEVA | NO SHORT | nessuna | nessuna | MOLTO ALTO |

## Lettura immediata

- **BTC**: Global = **+2**, spot = **HOLD / ATTESA CONFERME**, long = **NO LONG A LEVA / ATTENDI SOPRA 67.248 $**, short = **NO SHORT**, rischio = **MEDIO / ALTO**.
- **SOL**: Global = **+1**, spot = **HOLD LEGGERO / ATTESA CONFERME**, long = **NO LONG A LEVA**, short = **NO SHORT**, rischio = **MOLTO ALTO**.
- **DOGE**: Global = **0**, spot = **STAI ALLA FINESTRA**, long = **NO LONG A LEVA**, short = **NO SHORT**, rischio = **MOLTO ALTO**.

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

- Global Confluence: **+1**
- Confluenza: **MISTA / PARZIALE**
- Bias Global: **Neutrale / misto**
- Direzione decisionale: **NEUTRALE / INCERTO**
- Azione spot dal Global: **HOLD LEGGERO / ATTESA CONFERME**
- Long leva: **NO LONG A LEVA**
- Short leva: **NO SHORT**
- Rischio: **MOLTO ALTO**
- Conferme: conferma del adam and eve bottom sopra 83,81; nuova conferma tecnica sopra 78,73; milestone analogiche 77,61 / 91,83, valide soltanto se rientra anche il gap frattale.
- Invalidazioni: Allarmi sotto 70,21 / 73,40 / 62,19.

### DOGE

- Global Confluence: **0**
- Confluenza: **MISTA / PARZIALE**
- Bias Global: **Neutrale / misto**
- Direzione decisionale: **NEUTRALE / INCERTO**
- Azione spot dal Global: **STAI ALLA FINESTRA**
- Long leva: **NO LONG A LEVA**
- Short leva: **NO SHORT**
- Rischio: **MOLTO ALTO**
- Conferme: Sopra 0.07380 migliora; sopra 0.06966 viene invalidato il pattern ribassista dominante.
- Invalidazioni: Sotto 0.06829 il rischio ribassista aumenta.

## Nota semplice

- **Spot** = usa la stessa azione del Global Confluence, senza una seconda mappatura che possa produrre frasi diverse.
- **Zona alta storica** = zona dove non inseguire troppo; può essere zona da prendere profitto.
- **Zona bassa storica** = zona di rischio; con leva la liquidazione non dovrebbe stare lì vicino.
- **BTC leva** = nessun long a leva finché il prezzo snapshot non supera **67.248 $**; sotto quella soglia resta solo l'azione spot indicata dal Global.
- **Lifecycle EMA200** = per SOL resta solo contesto, peso Global 0; score interno 4; EMA200 circa 111,99 $; upside verso EMA200 +51,55%. Non autorizza leva e non aggiunge punti automatici.
- **NO LONG** non significa automaticamente **SHORT**. Lo short ha senso solo se il quadro è bearish o se lo spike viene spesso scaricato.
- Per SOL, se il Global è da **+3 in su**, la decisione non deve diventare bearish solo perché lo scanner grezzo a 30 giorni è incerto.

<!-- DECISION_REPORT_END -->

<!-- PAPER_TRADING_START -->
# Paper trading automatico KuCoin

Generato: 2026-08-05T05:16:05+00:00


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [paper_trading_report.md](paper_trading_report.md)

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-08-05T05:08:31+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-08-05T05:08:31+00:00 | 2026-08-05T05:08:31+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-08-05T04:45:00+00:00 | 2026-08-05T04:45:00+00:00 | 8,7 min | 25,0 min | OK |
| 60m | 12 | 2026-08-05T04:00:00+00:00 | 2026-08-05T04:00:00+00:00 | 8,7 min | 45,0 min | OK |
| 240m | 12 | 2026-08-05T00:00:00+00:00 | 2026-08-05T00:00:00+00:00 | 1,15 h | 1,00 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | ZEC | 240m | LONG | 7,05 | 6,00 | 0,00 | STALE_CANDLE | 1,15 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.7 minuti; tolleranza 60 minuti. |
| Principale 4H | BANK | 240m | SHORT | -7,00 | 6,00 | 0,00 | STALE_CANDLE | 1,15 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.7 minuti; tolleranza 60 minuti. |
| Principale 4H | HOME | 240m | LONG | 6,75 | 6,00 | 0,00 | STALE_CANDLE | 1,15 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.7 minuti; tolleranza 60 minuti. |
| Principale 4H | ADA | 240m | LONG | 6,25 | 6,00 | 0,00 | STALE_CANDLE | 1,15 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.7 minuti; tolleranza 60 minuti. |
| Principale 4H | XRP | 240m | SHORT | -5,87 | 6,00 | 0,13 | STALE_CANDLE | 1,15 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.7 minuti; tolleranza 60 minuti. |
| Principale 4H | DOGE | 240m | SHORT | -5,63 | 6,00 | 0,37 | STALE_CANDLE | 1,15 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.7 minuti; tolleranza 60 minuti. |
| Principale 4H | SNDK | 240m | LONG | 4,03 | 6,00 | 1,97 | STALE_CANDLE | 1,15 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.7 minuti; tolleranza 60 minuti. |
| Principale 4H | HYPE | 240m | LONG | 2,79 | 6,00 | 3,21 | STALE_CANDLE | 1,15 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.7 minuti; tolleranza 60 minuti. |
| Principale 4H | SOL | 240m | SHORT | -2,67 | 6,00 | 3,33 | STALE_CANDLE | 1,15 h | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.7 minuti; tolleranza 60 minuti. |
| Principale 4H | BTC | 240m | LONG | 2,00 | 6,00 | 4,00 | STALE_CANDLE | 1,15 h | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.7 minuti; tolleranza 60 minuti. |
| Principale 4H | SPCX | 240m | LONG | 0,69 | 6,00 | 5,31 | STALE_CANDLE | 1,15 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.7 minuti; tolleranza 60 minuti. |
| Principale 4H | ETH | 240m | SHORT | -0,67 | 6,00 | 5,33 | STALE_CANDLE | 1,15 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.7 minuti; tolleranza 60 minuti. |
| Rapida 1H V2 | HOME | 60m | LONG | 7,75 | 5,00 | 0,00 | STRATEGY_FILTER | 8,8 min | D: n/a | W: n/a | peso 0 | Filtro V2 non superato: regime, EMA, ritorni e RSI; per Rapida V2 servono anche breakout reale, volume e ADX. |
| Rapida 1H V2 | SNDK | 60m | LONG | 7,75 | 5,00 | 0,00 | STRATEGY_FILTER | 8,8 min | D: n/a | W: n/a | peso 0 | Filtro V2 non superato: regime, EMA, ritorni e RSI; per Rapida V2 servono anche breakout reale, volume e ADX. |
| Rapida 1H V1 | DOGE | 60m | SHORT | -7,23 | 4,50 | 0,00 | STRATEGY_FILTER | 8,8 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Filtro momentum: serve breakout DOWN oppure movimento breve ≥1,5%; breakout=NONE, movimento=-0.80%. |
| 1H Fast Score 6 75 V1 | DOGE | 60m | SHORT | -7,23 | 6,00 | 0,00 | STRATEGY_FILTER | 8,8 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Filtro momentum: serve breakout DOWN oppure movimento breve ≥1,5%; breakout=NONE, movimento=-0.80%. |
| 1H Fast Score 6 75 No Trend Up V1 | DOGE | 60m | SHORT | -7,23 | 6,00 | 0,00 | STRATEGY_FILTER | 8,8 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Filtro momentum: serve breakout DOWN oppure movimento breve ≥1,5%; breakout=NONE, movimento=-0.80%. |
| 1H Fast Score 6 75 Range Only V1 | DOGE | 60m | SHORT | -7,23 | 6,00 | 0,00 | STRATEGY_FILTER | 8,8 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Filtro momentum: serve breakout DOWN oppure movimento breve ≥1,5%; breakout=NONE, movimento=-0.80%. |
| 1H Fast Score 6 75 Cost Aware V1 | DOGE | 60m | SHORT | -7,23 | 6,00 | 0,00 | STRATEGY_FILTER | 8,8 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Filtro momentum: serve breakout DOWN oppure movimento breve ≥1,5%; breakout=NONE, movimento=-0.80%. |
| 1H Fast Nohigh Cap75 V1 | DOGE | 60m | SHORT | -7,23 | 4,50 | 0,00 | STRATEGY_FILTER | 8,8 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Filtro momentum: serve breakout DOWN oppure movimento breve ≥1,5%; breakout=NONE, movimento=-0.80%. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.734,37 | -2,66% | €-13,98 | €3.000,00 | -0,47% | 2 | 31 | 35,48% | 0,74 | 6,36% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 31 | 1020 | PRIME INDICAZIONI | 100 (mancano 69) |

- Trade del Principale 4H chiusi: **31**; win rate **35,48%**; profit factor **0,74**.
- Expectancy: **€-8,77** per trade; P&L netto: **€-271,94**; max drawdown: **6,36%**.
- Valutazione: **Si può osservare la direzione, ma il risultato resta fragile.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 2 | €9.734,37 | €494,66 | €1.483,99 | €49,83 | €4,48 |
| TEST | Benchmark Donchian breakout 1H | 1 | €10.562,88 | €52,48 | €104,96 | €2,54 | €0,00 |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | 0 | €10.506,14 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Nohigh Cap75 V1 | 0 | €10.492,11 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Score 6 75 V1 | 0 | €10.485,55 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H V3 Filtered | 0 | €10.440,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | 0 | €10.399,89 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top 5 Long 1H | 0 | €10.355,52 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Donchian 1H Gb20 120R V1 | 1 | €10.314,28 | €88,92 | €177,84 | €4,31 | €0,00 |
| TEST | Bilanciata 1H V1 | 0 | €10.305,06 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 0 | €10.300,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Nohigh Range Only V1 | 0 | €10.295,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Side Regime Guard V1 | 0 | €10.283,50 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H V2 | 0 | €10.278,80 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 0 | €10.271,73 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 0 | €10.239,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 0 | €10.235,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | 0 | €10.231,01 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Main Dynamic Asset Selector V1 | 0 | €10.230,30 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top 5 + forza BTC 1H | 0 | €10.224,22 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Score 6 75 Range Only V1 | 0 | €10.218,07 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Cap75 V1 | 0 | €10.217,21 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Main Side Regime Guard V1 | 2 | €10.217,08 | €641,89 | €1.925,68 | €50,72 | €4,42 |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | 0 | €10.206,76 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 0 | €10.185,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast No Pepe V1 | 0 | €10.184,40 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 0 | €10.145,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Donchian 1H | 0 | €10.113,92 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive | 0 | €10.111,99 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 1H | 0 | €10.110,96 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 0 | €10.099,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Ema 1H | 0 | €10.096,23 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | 0 | €10.096,10 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 4H | 0 | €10.086,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 4H | 0 | €10.084,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | 0 | €10.075,90 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Runner25 V1 | 0 | €10.071,76 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 0 | €10.048,77 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V1 | 0 | €10.043,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Donchian 1H | 0 | €10.038,53 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V3 Filtered | 0 | €10.030,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Trend Side Regime Guard V1 | 0 | €10.027,65 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Quality7 V1 | 0 | €10.012,08 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · prudente · 5x | 0 | €10.009,69 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 0 | €10.008,92 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 1 | €10.005,50 | €50,00 | €750,00 | €7,26 | €-3,48 |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 0 | €10.003,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 1 | €10.001,10 | €10,00 | €150,00 | €1,45 | €-0,70 |
| TEST | Scalp RSI Short 85 · €50 · 15x | 0 | €10.000,61 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €10 · 15x | 0 | €10.000,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Continuation V1 | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €10 · 15x | 0 | €9.998,86 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · prudente · 5x | 0 | €9.998,64 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €10 · 15x | 0 | €9.997,95 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 1H | 0 | €9.996,84 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | 0 | €9.996,45 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €10 · 15x | 0 | €9.996,22 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 0 | €9.995,23 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €50 · 15x | 0 | €9.994,31 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · prudente · 5x | 0 | €9.992,92 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €50 · 15x | 0 | €9.989,77 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €10 · 15x | 0 | €9.989,19 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | 0 | €9.985,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Donchian 4H | 0 | €9.985,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 4H | 0 | €9.982,09 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €50 · 15x | 0 | €9.981,10 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V2 | 0 | €9.974,21 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Tp2 V1 | 0 | €9.973,32 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Ampia 4H | 4 | €9.971,53 | €1.133,51 | €2.267,02 | €101,52 | €-0,09 |
| TEST | Sol Bollinger 1H | 0 | €9.970,30 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Profit Lock V1 | 0 | €9.969,87 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | 0 | €9.968,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · prudente · 5x | 0 | €9.961,01 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 1H | 0 | €9.959,54 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Bollinger 1H | 0 | €9.959,49 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom10 Short | 0 | €9.957,79 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom15 Short | 0 | €9.957,79 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom20 Short | 0 | €9.957,79 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 0 | €9.955,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 4H | 0 | €9.950,68 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 4H | 0 | €9.949,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €50 · 15x | 0 | €9.945,97 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 1 | €9.943,99 | €205,50 | €1.027,51 | €9,95 | €-4,77 |
| TEST | 1H Balanced Short Trend Down Strict V1 | 0 | €9.943,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Forza relativa 1H V2 | 0 | €9.934,23 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Long Only V1 | 0 | €9.931,86 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 No Esports Long Only V1 | 0 | €9.924,82 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | 0 | €9.923,70 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | 0 | €9.922,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Regime V1 | 0 | €9.903,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Bollinger 1H | 0 | €9.902,02 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 4H | 0 | €9.898,26 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Ema 4H | 0 | €9.894,27 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom 5 Short 1H | 0 | €9.893,14 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Tp3 V1 | 0 | €9.883,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 4H | 1 | €9.878,73 | €780,22 | €1.560,44 | €49,48 | €-17,30 |
| TEST | 1H Balanced V3 Long Only V1 | 0 | €9.874,61 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Donchian 1H | 0 | €9.871,99 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Nohigh V1 | 0 | €9.870,43 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 1H | 0 | €9.867,86 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 1H | 0 | €9.858,67 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | 0 | €9.857,49 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Tp3 V1 | 0 | €9.843,36 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Runner25 V1 | 0 | €9.837,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 0 | €9.837,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Mean Reversion | 0 | €9.832,55 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 No Esports V1 | 0 | €9.825,96 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 0 | €9.817,34 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | 0 | €9.807,66 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Gb20 Be V1 | 0 | €9.803,17 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Adaptive 1H | 0 | €9.799,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Expanded V1 | 0 | €9.799,08 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Quality7 Regime V1 | 0 | €9.797,24 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Gb20 Partial V1 | 0 | €9.792,75 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Global Confluence puro 1H | 0 | €9.784,49 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 1H | 0 | €9.781,19 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Runner25 V1 | 0 | €9.771,68 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Btc Le3 V1 | 0 | €9.770,26 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 0 | €9.762,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Benchmark Bollinger mean reversion 1H | 0 | €9.761,49 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive No Alt V1 | 0 | €9.758,89 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive V1 | 0 | €9.754,87 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Ema 1H | 0 | €9.727,87 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 0 | €9.723,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Partial 1R V1 | 0 | €9.710,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Benchmark trend following EMA 1H | 0 | €9.708,46 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Scanner | 0 | €9.693,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Guard V1 | 0 | €9.688,64 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Gb20 Loss Cap V1 | 0 | €9.679,07 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Balanced Long No Rhv V1 | 0 | €9.656,74 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | 0 | €9.639,39 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Forza relativa 1H V1 | 0 | €9.632,30 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Gb20 V1 | 0 | €9.625,26 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Mfe V1 | 0 | €9.583,73 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 0 | €9.579,83 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top10 Long | 0 | €9.538,24 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top15 Long | 0 | €9.538,24 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top20 Long | 0 | €9.538,24 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Trend | 0 | €9.529,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Guard Mfe V1 | 0 | €9.463,31 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Long Only V1 | 0 | €9.449,51 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Strict3 V1 | 0 | €9.405,07 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Mfe Trail | 0 | €9.331,79 | €0,00 | €0,00 | €0,00 | €0,00 |

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
| PRINCIPALE | Principale 4H | Confluenza trend | €9.734,37 | €-271,94 | 31 | 31 | 35,48% | 0,74 | €-8,77 | 6,36% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €10.562,88 | €562,95 | 39 | 39 | 53,85% | 1,62 | €14,43 | 3,09% |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | Momentum / breakout | €10.506,14 | €506,14 | 36 | 36 | 52,78% | 1,93 | €14,06 | 1,96% |
| TEST | 1H Fast Nohigh Cap75 V1 | Momentum / breakout | €10.492,11 | €492,11 | 64 | 64 | 46,88% | 1,41 | €7,69 | 2,83% |
| TEST | 1H Fast Score 6 75 V1 | Momentum / breakout | €10.485,55 | €485,55 | 75 | 75 | 44,00% | 1,37 | €6,47 | 2,49% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €10.440,04 | €440,04 | 66 | 66 | 39,39% | 1,33 | €6,67 | 2,82% |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | Momentum / breakout V3 Filtered | €10.399,89 | €399,89 | 20 | 20 | 65,00% | 3,42 | €19,99 | 1,39% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.355,52 | €355,52 | 50 | 50 | 44,00% | 1,30 | €7,11 | 4,79% |
| TEST | Donchian 1H Gb20 120R V1 | Donchian breakout 20 barre | €10.314,28 | €314,39 | 7 | 7 | 71,43% | 6,32 | €44,91 | 1,61% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €10.305,06 | €305,06 | 75 | 75 | 45,33% | 1,24 | €4,07 | 3,56% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | Momentum / breakout V3 Filtered | €10.300,05 | €300,05 | 33 | 33 | 48,48% | 2,04 | €9,09 | 2,01% |
| TEST | 1H Fast V3 Nohigh Range Only V1 | Momentum / breakout V3 Filtered | €10.295,72 | €295,72 | 12 | 12 | 58,33% | 2,80 | €24,64 | 1,78% |
| TEST | Combo Adaptive Side Regime Guard V1 | Combo Adaptive | €10.283,50 | €283,50 | 33 | 33 | 54,55% | 1,80 | €8,59 | 1,58% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €10.278,80 | €278,80 | 41 | 39 | 51,22% | 1,36 | €6,80 | 2,75% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | Momentum / breakout V3 Filtered | €10.271,73 | €271,73 | 22 | 22 | 50,00% | 1,74 | €12,35 | 1,72% |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | Momentum / breakout V3 Filtered | €10.239,20 | €239,20 | 17 | 17 | 52,94% | 4,50 | €14,07 | 1,01% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | Momentum / breakout V3 Filtered | €10.235,18 | €235,18 | 20 | 20 | 50,00% | 1,90 | €11,76 | 2,73% |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | Momentum / breakout | €10.231,01 | €231,01 | 28 | 28 | 46,43% | 1,69 | €8,25 | 1,76% |
| TEST | Main Dynamic Asset Selector V1 | Confluenza trend | €10.230,30 | €230,30 | 11 | 11 | 45,45% | 1,85 | €20,94 | 1,50% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €10.224,22 | €224,22 | 41 | 41 | 39,02% | 1,25 | €5,47 | 3,94% |
| TEST | 1H Fast Score 6 75 Range Only V1 | Momentum / breakout | €10.218,07 | €218,07 | 13 | 13 | 53,85% | 1,74 | €16,77 | 2,28% |
| TEST | 1H Fast V3 Cap75 V1 | Momentum / breakout V3 Filtered | €10.217,21 | €217,21 | 68 | 68 | 44,12% | 1,16 | €3,19 | 3,62% |
| TEST | Main Side Regime Guard V1 | Confluenza trend | €10.217,08 | €211,24 | 15 | 15 | 46,67% | 1,56 | €14,08 | 2,40% |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | Momentum / breakout | €10.206,76 | €206,76 | 33 | 33 | 51,52% | 1,32 | €6,27 | 2,77% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | Momentum / breakout V3 Filtered | €10.185,37 | €185,37 | 22 | 22 | 40,91% | 1,57 | €8,43 | 2,27% |
| TEST | 1H Fast No Pepe V1 | Momentum / breakout | €10.184,40 | €184,40 | 72 | 72 | 44,44% | 1,14 | €2,56 | 2,15% |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | Momentum / breakout V3 Filtered | €10.145,12 | €145,12 | 44 | 44 | 45,45% | 1,20 | €3,30 | 2,91% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €10.113,92 | €113,92 | 4 | 4 | 75,00% | 26,39 | €28,48 | 0,79% |
| TEST | Combo Adaptive | Combo Adaptive | €10.111,99 | €111,99 | 40 | 40 | 42,50% | 1,21 | €2,80 | 2,58% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.110,96 | €110,96 | 4 | 4 | 75,00% | 2,94 | €27,74 | 0,70% |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | Momentum / breakout V3 Filtered | €10.099,04 | €99,04 | 55 | 55 | 54,55% | 1,12 | €1,80 | 3,59% |
| TEST | Doge Ema 1H | Trend following EMA | €10.096,23 | €96,23 | 10 | 10 | 70,00% | 1,57 | €9,62 | 1,36% |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | Momentum / breakout V3 Filtered | €10.096,10 | €96,10 | 59 | 59 | 50,85% | 1,11 | €1,63 | 2,98% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €10.086,98 | €86,98 | 1 | 1 | 100,00% | ∞ | €86,98 | 0,40% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.084,12 | €84,12 | 1 | 1 | 100,00% | ∞ | €84,12 | 0,30% |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | Momentum / breakout V3 Filtered | €10.075,90 | €75,90 | 20 | 20 | 45,00% | 1,17 | €3,80 | 2,17% |
| TEST | Combo Adaptive Runner25 V1 | Combo Adaptive | €10.071,76 | €71,76 | 43 | 43 | 37,21% | 1,11 | €1,67 | 2,31% |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | Momentum / breakout V3 Filtered | €10.048,77 | €48,77 | 23 | 23 | 43,48% | 1,12 | €2,12 | 3,05% |
| TEST | Rapida 1H V1 | Momentum / breakout | €10.043,28 | €43,28 | 78 | 78 | 34,62% | 1,02 | €0,55 | 6,76% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €10.038,53 | €38,53 | 6 | 6 | 66,67% | 1,34 | €6,42 | 1,08% |
| TEST | Rapida 1H V3 Filtered | Momentum / breakout V3 Filtered | €10.030,12 | €30,12 | 103 | 103 | 37,86% | 1,02 | €0,29 | 2,95% |
| TEST | Combo Trend Side Regime Guard V1 | Combo Trend | €10.027,65 | €27,65 | 30 | 30 | 50,00% | 1,06 | €0,92 | 2,61% |
| TEST | Combo Adaptive Quality7 V1 | Combo Adaptive | €10.012,08 | €12,08 | 26 | 26 | 34,62% | 1,03 | €0,46 | 2,48% |
| TEST | Scalp RSI Long 20 · prudente · 5x | Inversione RSI estrema 15m | €10.009,69 | €9,69 | 6 | 6 | 50,00% | 1,40 | €1,62 | 0,36% |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | Momentum / breakout V3 Filtered | €10.008,92 | €8,92 | 30 | 30 | 36,67% | 1,02 | €0,30 | 4,84% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €10.005,50 | €9,43 | 18 | 18 | 44,44% | 1,15 | €0,52 | 0,25% |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | Momentum / breakout V3 Filtered | €10.003,37 | €3,37 | 8 | 8 | 37,50% | 1,02 | €0,42 | 2,15% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €10.001,10 | €1,89 | 18 | 18 | 44,44% | 1,15 | €0,10 | 0,05% |
| TEST | Scalp RSI Short 85 · €50 · 15x | Inversione RSI estrema 15m | €10.000,61 | €0,61 | 2 | 2 | 50,00% | 1,74 | €0,30 | 0,07% |
| TEST | Scalp RSI Short 85 · €10 · 15x | Inversione RSI estrema 15m | €10.000,12 | €0,12 | 2 | 2 | 50,00% | 1,74 | €0,06 | 0,01% |
| TEST | Scanner Bottom5 Short Continuation V1 | Scanner Bottom5 Short Continuation | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 15 · €10 · 15x | Inversione RSI estrema 15m | €9.998,86 | €-1,14 | 2 | 2 | 50,00% | 0,24 | €-0,57 | 0,02% |
| TEST | Scalp RSI Short 85 · prudente · 5x | Inversione RSI estrema 15m | €9.998,64 | €-1,36 | 2 | 2 | 50,00% | 0,42 | €-0,68 | 0,11% |
| TEST | Scalp RSI Long 20 · €10 · 15x | Inversione RSI estrema 15m | €9.997,95 | €-2,05 | 6 | 6 | 33,33% | 0,34 | €-0,34 | 0,03% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €9.996,84 | €-3,16 | 5 | 5 | 60,00% | 0,97 | €-0,63 | 1,49% |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | Momentum / breakout | €9.996,45 | €-3,55 | 25 | 25 | 36,00% | 0,99 | €-0,14 | 2,27% |
| TEST | Scalp RSI Short 80 · €10 · 15x | Inversione RSI estrema 15m | €9.996,22 | €-3,78 | 5 | 5 | 40,00% | 0,12 | €-0,76 | 0,05% |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | Momentum / breakout V3 Filtered | €9.995,23 | €-4,77 | 15 | 15 | 46,67% | 0,99 | €-0,32 | 2,70% |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | €9.994,31 | €-5,69 | 2 | 2 | 50,00% | 0,24 | €-2,84 | 0,11% |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | €9.992,92 | €-7,08 | 2 | 2 | 50,00% | 0,39 | €-3,54 | 0,17% |
| TEST | Scalp RSI Long 20 · €50 · 15x | Inversione RSI estrema 15m | €9.989,77 | €-10,23 | 6 | 6 | 33,33% | 0,34 | €-1,71 | 0,17% |
| TEST | Scalp RSI Long 25 · €10 · 15x | Inversione RSI estrema 15m | €9.989,19 | €-10,81 | 12 | 12 | 33,33% | 0,26 | €-0,90 | 0,14% |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | Scanner Bottom 5 Short | €9.985,05 | €-14,95 | 19 | 19 | 42,11% | 0,95 | €-0,79 | 1,38% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €9.985,00 | €-15,00 | 2 | 2 | 50,00% | 0,71 | €-7,50 | 0,79% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €9.982,09 | €-17,91 | 2 | 2 | 50,00% | 0,65 | €-8,96 | 0,77% |
| TEST | Scalp RSI Short 80 · €50 · 15x | Inversione RSI estrema 15m | €9.981,10 | €-18,90 | 5 | 5 | 40,00% | 0,12 | €-3,78 | 0,27% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €9.974,21 | €-25,79 | 17 | 15 | 41,18% | 0,93 | €-1,52 | 1,69% |
| TEST | 1H Fast Tp2 V1 | Momentum / breakout | €9.973,32 | €-26,68 | 79 | 79 | 35,44% | 0,98 | €-0,34 | 2,58% |
| TEST | Ampia 4H | Confluenza trend | €9.971,53 | €-27,14 | 25 | 25 | 24,00% | 0,96 | €-1,09 | 3,68% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.970,30 | €-29,70 | 5 | 5 | 40,00% | 0,82 | €-5,94 | 1,89% |
| TEST | Scanner Bottom5 Short Profit Lock V1 | Scanner Bottom 5 Short | €9.969,87 | €-30,13 | 20 | 20 | 40,00% | 0,86 | €-1,51 | 1,53% |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | Scanner Top 5 + forza BTC | €9.968,72 | €-31,28 | 10 | 10 | 30,00% | 0,87 | €-3,13 | 2,84% |
| TEST | Scalp RSI Short 80 · prudente · 5x | Inversione RSI estrema 15m | €9.961,01 | €-38,99 | 5 | 5 | 40,00% | 0,09 | €-7,80 | 0,50% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €9.959,54 | €-40,46 | 4 | 4 | 50,00% | 0,63 | €-10,11 | 0,89% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €9.959,49 | €-40,51 | 2 | 2 | 50,00% | 0,28 | €-20,26 | 0,91% |
| TEST | Scanner Bottom10 Short | Scanner Bottom10 Short | €9.957,79 | €-42,21 | 25 | 25 | 40,00% | 0,91 | €-1,69 | 2,72% |
| TEST | Scanner Bottom15 Short | Scanner Bottom15 Short | €9.957,79 | €-42,21 | 25 | 25 | 40,00% | 0,91 | €-1,69 | 2,72% |
| TEST | Scanner Bottom20 Short | Scanner Bottom20 Short | €9.957,79 | €-42,21 | 25 | 25 | 40,00% | 0,91 | €-1,69 | 2,72% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €9.955,72 | €-44,28 | 12 | 12 | 33,33% | 0,38 | €-3,69 | 0,71% |
| TEST | Btc Ema 4H | Trend following EMA | €9.950,68 | €-49,32 | 1 | 1 | 0,00% | 0,00 | €-49,32 | 0,96% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €9.949,62 | €-50,38 | 1 | 1 | 0,00% | 0,00 | €-50,38 | 0,74% |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | €9.945,97 | €-54,03 | 12 | 12 | 33,33% | 0,26 | €-4,50 | 0,72% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.943,99 | €-50,63 | 18 | 18 | 44,44% | 0,46 | €-2,81 | 0,58% |
| TEST | 1H Balanced Short Trend Down Strict V1 | Confluenza trend | €9.943,38 | €-56,62 | 2 | 2 | 0,00% | 0,00 | €-28,31 | 1,11% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €9.934,23 | €-65,77 | 55 | 54 | 38,18% | 0,96 | €-1,20 | 5,53% |
| TEST | Combo Adaptive Long Only V1 | Combo Adaptive | €9.931,86 | €-68,14 | 20 | 20 | 25,00% | 0,81 | €-3,41 | 2,34% |
| TEST | 1H Fast V3 No Esports Long Only V1 | Momentum / breakout V3 Filtered | €9.924,82 | €-75,18 | 36 | 36 | 38,89% | 0,90 | €-2,09 | 4,41% |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | Momentum / breakout V3 Filtered | €9.923,70 | €-76,30 | 49 | 49 | 46,94% | 0,93 | €-1,56 | 3,21% |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | Combo Adaptive | €9.922,04 | €-77,96 | 11 | 11 | 45,45% | 0,71 | €-7,09 | 1,95% |
| TEST | Combo Adaptive Regime V1 | Combo Adaptive | €9.903,28 | €-96,72 | 22 | 22 | 45,45% | 0,79 | €-4,40 | 2,18% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €9.902,02 | €-97,98 | 4 | 4 | 25,00% | 0,41 | €-24,49 | 1,89% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €9.898,26 | €-101,74 | 2 | 2 | 0,00% | 0,00 | €-50,87 | 1,48% |
| TEST | Eth Ema 4H | Trend following EMA | €9.894,27 | €-105,73 | 2 | 2 | 0,00% | 0,00 | €-52,87 | 1,21% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.893,14 | €-106,86 | 47 | 47 | 36,17% | 0,87 | €-2,27 | 5,48% |
| TEST | Combo Adaptive Tp3 V1 | Combo Adaptive | €9.883,60 | €-116,40 | 24 | 24 | 37,50% | 0,71 | €-4,85 | 2,44% |
| TEST | Sol Ema 4H | Trend following EMA | €9.878,73 | €-103,69 | 2 | 2 | 0,00% | 0,00 | €-51,84 | 1,44% |
| TEST | 1H Balanced V3 Long Only V1 | Confluenza trend V3 Filtered | €9.874,61 | €-125,39 | 22 | 22 | 31,82% | 0,72 | €-5,70 | 2,01% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.871,99 | €-128,01 | 5 | 5 | 20,00% | 0,42 | €-25,60 | 1,62% |
| TEST | 1H Fast V3 Nohigh V1 | Momentum / breakout V3 Filtered | €9.870,43 | €-129,57 | 62 | 62 | 38,71% | 0,90 | €-2,09 | 2,96% |
| TEST | Sol Ema 1H | Trend following EMA | €9.867,86 | €-132,14 | 7 | 7 | 28,57% | 0,52 | €-18,88 | 2,09% |
| TEST | Btc Ema 1H | Trend following EMA | €9.858,67 | €-141,33 | 7 | 7 | 28,57% | 0,48 | €-20,19 | 1,56% |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | Momentum / breakout V3 Filtered | €9.857,49 | €-142,51 | 44 | 44 | 40,91% | 0,86 | €-3,24 | 2,86% |
| TEST | Scanner Top5 Btc Tp3 V1 | Scanner Top 5 + forza BTC | €9.843,36 | €-156,64 | 26 | 26 | 30,77% | 0,80 | €-6,02 | 4,68% |
| TEST | Scanner Top5 Btc Runner25 V1 | Scanner Top 5 + forza BTC | €9.837,60 | €-162,40 | 30 | 30 | 33,33% | 0,79 | €-5,41 | 4,99% |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | Momentum / breakout V3 Filtered | €9.837,38 | €-162,62 | 37 | 37 | 40,54% | 0,76 | €-4,40 | 3,08% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €9.832,55 | €-167,45 | 20 | 20 | 35,00% | 0,76 | €-8,37 | 3,60% |
| TEST | 1H Fast V3 No Esports V1 | Momentum / breakout V3 Filtered | €9.825,96 | €-174,04 | 77 | 77 | 37,66% | 0,89 | €-2,26 | 2,91% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | Momentum / breakout V3 Filtered | €9.817,34 | €-182,66 | 24 | 24 | 41,67% | 0,64 | €-7,61 | 3,23% |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | Scanner Top 5 + forza BTC | €9.807,66 | €-192,34 | 19 | 19 | 31,58% | 0,70 | €-10,12 | 4,36% |
| TEST | Master Adaptive Gb20 Be V1 | Master Adaptive Consensus | €9.803,17 | €-196,83 | 22 | 22 | 18,18% | 0,66 | €-8,95 | 3,35% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.799,60 | €-200,40 | 6 | 6 | 33,33% | 0,08 | €-33,40 | 2,09% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €9.799,08 | €-200,92 | 22 | 22 | 31,82% | 0,74 | €-9,13 | 3,64% |
| TEST | Combo Adaptive Quality7 Regime V1 | Combo Adaptive | €9.797,24 | €-202,76 | 11 | 11 | 27,27% | 0,31 | €-18,43 | 2,32% |
| TEST | Master Adaptive Gb20 Partial V1 | Master Adaptive Consensus | €9.792,75 | €-207,25 | 17 | 17 | 29,41% | 0,62 | €-12,19 | 2,93% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.784,49 | €-215,51 | 13 | 13 | 30,77% | 0,44 | €-16,58 | 2,92% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €9.781,19 | €-218,81 | 7 | 7 | 28,57% | 0,24 | €-31,26 | 2,92% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €9.771,68 | €-228,32 | 21 | 21 | 28,57% | 0,68 | €-10,87 | 3,98% |
| TEST | Scanner Top5 Btc Btc Le3 V1 | Scanner Top 5 + forza BTC | €9.770,26 | €-229,74 | 22 | 22 | 31,82% | 0,64 | €-10,44 | 4,43% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | Momentum / breakout V3 Filtered | €9.762,18 | €-237,82 | 7 | 7 | 14,29% | 0,02 | €-33,97 | 2,82% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €9.761,49 | €-238,51 | 50 | 50 | 40,00% | 0,82 | €-4,77 | 5,70% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €9.758,89 | €-241,11 | 19 | 19 | 26,32% | 0,66 | €-12,69 | 4,03% |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | €9.754,87 | €-245,13 | 19 | 19 | 26,32% | 0,66 | €-12,90 | 4,07% |
| TEST | Eth Ema 1H | Trend following EMA | €9.727,87 | €-272,13 | 8 | 8 | 25,00% | 0,16 | €-34,02 | 2,76% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | Momentum / breakout V3 Filtered | €9.723,72 | €-276,28 | 31 | 31 | 32,26% | 0,62 | €-8,91 | 4,83% |
| TEST | Combo Adaptive Partial 1R V1 | Combo Adaptive | €9.710,00 | €-290,00 | 41 | 41 | 39,02% | 0,60 | €-7,07 | 3,97% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.708,46 | €-291,54 | 46 | 46 | 30,43% | 0,71 | €-6,34 | 3,97% |
| TEST | Combo Scanner | Combo Scanner | €9.693,00 | €-307,00 | 50 | 50 | 36,00% | 0,77 | €-6,14 | 5,08% |
| TEST | Scanner Top5 Btc Guard V1 | Scanner Top 5 + forza BTC | €9.688,64 | €-311,36 | 24 | 24 | 25,00% | 0,59 | €-12,97 | 3,94% |
| TEST | Master Adaptive Gb20 Loss Cap V1 | Master Adaptive Consensus | €9.679,07 | €-320,93 | 19 | 19 | 21,05% | 0,55 | €-16,89 | 4,64% |
| TEST | 1H Balanced Long No Rhv V1 | Confluenza trend | €9.656,74 | €-343,26 | 20 | 20 | 25,00% | 0,47 | €-17,16 | 4,32% |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | Scanner Top 5 + forza BTC | €9.639,39 | €-360,61 | 34 | 34 | 35,29% | 0,61 | €-10,61 | 3,93% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €9.632,30 | €-367,70 | 52 | 52 | 26,92% | 0,70 | €-7,07 | 7,55% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €9.625,26 | €-374,74 | 54 | 54 | 55,56% | 0,59 | €-6,94 | 4,27% |
| TEST | Scanner Top5 Btc Mfe V1 | Scanner Top 5 + forza BTC | €9.583,73 | €-416,27 | 34 | 34 | 32,35% | 0,46 | €-12,24 | 5,03% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | Momentum / breakout V3 Filtered | €9.579,83 | €-420,17 | 11 | 11 | 0,00% | 0,00 | €-38,20 | 4,20% |
| TEST | Scanner Top10 Long | Scanner Top10 Long | €9.538,24 | €-461,76 | 22 | 22 | 27,27% | 0,34 | €-20,99 | 6,31% |
| TEST | Scanner Top15 Long | Scanner Top15 Long | €9.538,24 | €-461,76 | 22 | 22 | 27,27% | 0,34 | €-20,99 | 6,31% |
| TEST | Scanner Top20 Long | Scanner Top20 Long | €9.538,24 | €-461,76 | 22 | 22 | 27,27% | 0,34 | €-20,99 | 6,31% |
| TEST | Combo Trend | Combo Trend | €9.529,98 | €-470,02 | 62 | 62 | 30,65% | 0,74 | €-7,58 | 7,64% |
| TEST | Scanner Top5 Btc Guard Mfe V1 | Scanner Top 5 + forza BTC | €9.463,31 | €-536,69 | 41 | 41 | 34,15% | 0,53 | €-13,09 | 5,43% |
| TEST | 1H Fast V3 Long Only V1 | Momentum / breakout V3 Filtered | €9.449,51 | €-550,49 | 56 | 56 | 28,57% | 0,62 | €-9,83 | 6,47% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €9.405,07 | €-594,93 | 27 | 27 | 22,22% | 0,49 | €-22,03 | 6,15% |
| TEST | Combo Adaptive Mfe Trail | Combo Adaptive | €9.331,79 | €-668,21 | 50 | 50 | 28,00% | 0,42 | €-13,36 | 6,71% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | SHIB | LONG | Confluenza trend | 240m | 3,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €8,88 | €26,63 | €2,22 | €0,00 |
| Principale 4H | DOGE | SHORT | Confluenza trend | 240m | 3,0x | 0,07019 | 0,06997 | 0,07248 | 0,09323 | 0,06560 | €485,79 | €1.457,36 | €47,61 | €4,48 |
| Ampia 4H | TAO | SHORT | Confluenza trend | 240m | 2,0x | 189,05650 | 189,05650 | 197,51338 | 282,63946 | 165,37722 | €558,68 | €1.117,36 | €49,98 | €-0,00 |
| Ampia 4H | XMR | LONG | Confluenza trend | 240m | 2,0x | 364,45854 | 364,45854 | 347,94701 | 184,05156 | 410,69083 | €544,42 | €1.088,84 | €49,33 | €0,00 |
| Ampia 4H | XRP | SHORT | Confluenza trend | 240m | 2,0x | 1,06427 | 1,06886 | 1,09657 | 1,59108 | 0,97382 | €13,35 | €26,70 | €0,81 | €-0,12 |
| Ampia 4H | DOGE | SHORT | Confluenza trend | 240m | 2,0x | 0,07002 | 0,06997 | 0,07288 | 0,10467 | 0,06199 | €17,06 | €34,13 | €1,40 | €0,02 |
| Scalp RSI Short 75 · €10 · 15x | ZEC | SHORT | Inversione RSI estrema 15m | 15m | 15,0x | 513,71724 | 516,10000 | 518,69157 | 545,39647 | 506,25574 | €10,00 | €150,00 | €1,45 | €-0,70 |
| Scalp RSI Short 75 · €50 · 15x | ZEC | SHORT | Inversione RSI estrema 15m | 15m | 15,0x | 513,71724 | 516,10000 | 518,69157 | 545,39647 | 506,25574 | €50,00 | €750,00 | €7,26 | €-3,48 |
| Scalp RSI Short 75 · prudente · 5x | ZEC | SHORT | Inversione RSI estrema 15m | 15m | 5,0x | 513,71724 | 516,10000 | 518,69157 | 613,89210 | 503,76857 | €205,50 | €1.027,51 | €9,95 | €-4,77 |
| Benchmark Donchian breakout 1H | NEAR | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 1,70198 | 1,70198 | 1,74321 | 2,54446 | 1,59891 | €52,48 | €104,96 | €2,54 | €-0,00 |
| Donchian 1H Gb20 120R V1 | NEAR | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 1,70198 | 1,70198 | 1,74321 | 2,54446 | 1,59891 | €88,92 | €177,84 | €4,31 | €-0,00 |
| Sol Ema 4H | SOL | SHORT | Trend following EMA | 240m | 2,0x | 73,19036 | 74,00200 | 75,51123 | 109,41959 | 67,38819 | €780,22 | €1.560,44 | €49,48 | €-17,30 |
| Main Side Regime Guard V1 | ALLO | SHORT | Confluenza trend | 240m | 3,0x | 0,38070 | 0,38070 | 0,37357 | 0,50570 | 0,28933 | €140,03 | €420,08 | €0,00 | €-0,00 |
| Main Side Regime Guard V1 | DOGE | SHORT | Confluenza trend | 240m | 3,0x | 0,07018 | 0,06997 | 0,07254 | 0,09322 | 0,06545 | €501,87 | €1.505,61 | €50,72 | €4,42 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | ONDO | LONG | 2026-08-05T04:24:47+00:00 | 0,40320 | €-1,38 | -0,03 | TIME_EXIT_NO_CANDLES |
| Scalp RSI Short 75 · prudente · 5x | ZEC | SHORT | 2026-08-04T17:38:57+00:00 | 500,04656 | €-11,39 | -1,14 | STOP |
| Scalp RSI Short 75 · €50 · 15x | ZEC | SHORT | 2026-08-04T17:38:57+00:00 | 500,04656 | €-8,40 | -1,14 | STOP |
| Scalp RSI Short 75 · €10 · 15x | ZEC | SHORT | 2026-08-04T17:38:57+00:00 | 500,04656 | €-1,68 | -1,14 | STOP |
| Scalp RSI Short 75 · prudente · 5x | HYPE | SHORT | 2026-08-04T14:38:53+00:00 | 55,63767 | €-3,52 | -0,35 | STOP_GAP_STRESS |
| Benchmark Donchian breakout 1H | ALLO | SHORT | 2026-08-04T14:38:53+00:00 | 0,35699 | €-1,35 | -0,03 | TIME_EXIT_NO_CANDLES |
| Scalp RSI Short 75 · €50 · 15x | HYPE | SHORT | 2026-08-04T14:24:49+00:00 | 55,12482 | €5,40 | 1,26 | TARGET |
| Scalp RSI Short 75 · €10 · 15x | HYPE | SHORT | 2026-08-04T14:24:49+00:00 | 55,12482 | €1,08 | 1,26 | TARGET |
| Combo Trend | SUI | SHORT | 2026-08-04T00:08:52+00:00 | 0,68030 | €-0,25 | -0,09 | TIME_EXIT_NO_CANDLES |
| Forza relativa 1H V1 | NEAR | SHORT | 2026-08-03T23:09:14+00:00 | 1,70300 | €-0,41 | -0,08 | TIME_EXIT_NO_CANDLES |
| Benchmark trend following EMA 1H | NEAR | SHORT | 2026-08-03T22:08:54+00:00 | 1,73200 | €-0,08 | -0,08 | TIME_EXIT_NO_CANDLES |
| Combo Trend | NEAR | SHORT | 2026-08-03T22:08:54+00:00 | 1,73200 | €-0,10 | -0,08 | TIME_EXIT_NO_CANDLES |

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

Generato: 2026-08-05 05:15 UTC


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

Segnali totali salvati: **84**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08-05 | BTC | 64.252,74 | +2 | +4 | +3 | +3 | -1 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-08-05 | DOGE | 0.06992 | 0 | +2 | +1 | +2 | -2 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-08-05 | SOL | 73,88 | +1 | +4 | +3 | +2 | -2 | -1 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-08-04 | BTC | 63.800,01 | +5 | +4 | +3 | +3 | +1 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-08-04 | DOGE | 0.07017 | +1 | +2 | +1 | +2 | -2 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-08-04 | SOL | 73,68 | 0 | +4 | +3 | +2 | -2 | -1 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-08-03 | BTC | 62.745,61 | +2 | +4 | +3 | +3 | -2 | -1 | 0 | HOLD / ATTESA CONFERME |
| 2026-08-03 | DOGE | 0.06985 | -2 | +2 | +1 | +2 | -3 | 0 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-08-03 | SOL | 72,93 | +1 | +4 | +3 | +3 | -3 | -1 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-08-02 | BTC | 63.392,32 | +3 | +4 | +3 | +3 | -1 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-08-02 | DOGE | 0.07018 | +2 | +4 | +3 | +2 | -2 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-08-02 | SOL | 73,42 | +1 | +4 | +3 | +3 | -3 | -1 | 0 | HOLD LEGGERO / ATTESA CONFERME |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 28 | 27 | 26 | 25 | 23 | 21 | 18 | 14 | 7 | 0 | 0 | 0 |
| SOL | 28 | 27 | 26 | 25 | 23 | 21 | 18 | 14 | 7 | 0 | 0 | 0 |
| DOGE | 28 | 27 | 26 | 25 | 23 | 21 | 18 | 14 | 7 | 0 | 0 | 0 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-07-16 | 21g | 2026-08-06 | domani |
| SOL | 2026-07-16 | 21g | 2026-08-06 | domani |
| DOGE | 2026-07-16 | 21g | 2026-08-06 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 25 | 48,00% | +0,04% | -0,01% | FEEDBACK RAPIDO |
| BTC | 2g | 24 | 41,67% | +0,11% | -0,09% | FEEDBACK RAPIDO |
| BTC | 3g | 23 | 34,78% | -0,12% | -0,42% | FEEDBACK RAPIDO |
| BTC | 5g | 21 | 19,05% | -0,03% | -0,63% | FEEDBACK RAPIDO |
| BTC | 7g | 19 | 36,84% | +0,15% | -0,42% | FEEDBACK RAPIDO |
| BTC | 10g | 16 | 37,50% | +0,51% | +0,09% | FEEDBACK RAPIDO |
| BTC | 14g | 13 | 53,85% | +0,17% | +0,03% | FEEDBACK RAPIDO |
| BTC | 21g | 7 | 42,86% | +0,17% | +0,17% | FEEDBACK RAPIDO |
| BTC | 30g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 1g | 20 | 50,00% | -0,10% | -0,41% | FEEDBACK RAPIDO |
| SOL | 2g | 20 | 40,00% | -0,27% | -0,62% | FEEDBACK RAPIDO |
| SOL | 3g | 19 | 36,84% | -0,42% | -0,89% | FEEDBACK RAPIDO |
| SOL | 5g | 17 | 41,18% | -0,84% | -1,16% | FEEDBACK RAPIDO |
| SOL | 7g | 15 | 46,67% | -1,21% | -0,99% | FEEDBACK RAPIDO |
| SOL | 10g | 14 | 42,86% | -1,94% | -0,42% | FEEDBACK RAPIDO |
| SOL | 14g | 13 | 61,54% | -3,12% | +0,53% | FEEDBACK RAPIDO |
| SOL | 21g | 6 | 50,00% | -4,46% | -1,07% | FEEDBACK RAPIDO |
| SOL | 30g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 1g | 26 | 42,31% | -0,04% | -0,06% | FEEDBACK RAPIDO |
| DOGE | 2g | 25 | 44,00% | -0,21% | -0,22% | FEEDBACK RAPIDO |
| DOGE | 3g | 24 | 45,83% | -0,41% | +0,08% | FEEDBACK RAPIDO |
| DOGE | 5g | 22 | 59,09% | -0,79% | +0,37% | FEEDBACK RAPIDO |
| DOGE | 7g | 20 | 60,00% | -1,28% | +0,77% | FEEDBACK RAPIDO |
| DOGE | 10g | 18 | 61,11% | -1,97% | +1,44% | FEEDBACK RAPIDO |
| DOGE | 14g | 14 | 85,71% | -3,12% | +3,12% | FEEDBACK RAPIDO |
| DOGE | 21g | 7 | 100,00% | -4,26% | +4,26% | FEEDBACK RAPIDO |
| DOGE | 30g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 25 | 48,00% | +0,04% | -0,01% | -0,30% | +0,64% | FEEDBACK RAPIDO |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 27 | 51,85% | +0,02% | +0,02% | -0,31% | +0,58% | FEEDBACK RAPIDO |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 27 | 51,85% | +0,02% | +0,02% | -0,31% | +0,58% | FEEDBACK RAPIDO |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 23 | 52,17% | -0,02% | -0,02% | -0,38% | +0,49% | FEEDBACK RAPIDO |
| BTC | 1g | Tecnico | CALIBRABILE | 22 | 36,36% | +0,24% | -0,39% | -0,12% | +0,81% | FEEDBACK RAPIDO |
| BTC | 1g | Classic technical | CALIBRABILE | 4 | 0,00% | +0,76% | -0,76% | +0,03% | +1,12% | FEEDBACK RAPIDO |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +2,00% | +2,00% | +1,48% | +2,25% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 24 | 41,67% | +0,11% | -0,09% | -0,42% | +0,87% | FEEDBACK RAPIDO |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 26 | 46,15% | +0,07% | +0,07% | -0,44% | +0,82% | FEEDBACK RAPIDO |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 26 | 46,15% | +0,07% | +0,07% | -0,44% | +0,82% | FEEDBACK RAPIDO |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 22 | 45,45% | -0,04% | -0,04% | -0,57% | +0,71% | FEEDBACK RAPIDO |
| BTC | 2g | Tecnico | CALIBRABILE | 21 | 38,10% | +0,34% | -0,44% | -0,16% | +1,10% | FEEDBACK RAPIDO |
| BTC | 2g | Classic technical | CALIBRABILE | 4 | 25,00% | +0,86% | -0,86% | +0,50% | +1,73% | FEEDBACK RAPIDO |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +3,18% | +3,18% | +3,05% | +3,89% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 23 | 34,78% | -0,12% | -0,42% | -1,56% | +1,74% | FEEDBACK RAPIDO |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 25 | 52,00% | -0,01% | -0,01% | -1,51% | +1,71% | FEEDBACK RAPIDO |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 25 | 52,00% | -0,01% | -0,01% | -1,51% | +1,71% | FEEDBACK RAPIDO |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 21 | 52,38% | -0,04% | -0,04% | -1,57% | +1,61% | FEEDBACK RAPIDO |
| BTC | 3g | Tecnico | CALIBRABILE | 20 | 40,00% | +0,48% | -0,12% | -1,19% | +2,15% | FEEDBACK RAPIDO |
| BTC | 3g | Classic technical | CALIBRABILE | 3 | 33,33% | +0,46% | -0,46% | -0,83% | +2,15% | FEEDBACK RAPIDO |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,88% | +1,88% | +1,44% | +4,24% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 21 | 19,05% | -0,03% | -0,63% | -2,37% | +2,28% | FEEDBACK RAPIDO |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 23 | 34,78% | -0,01% | -0,01% | -2,29% | +2,32% | FEEDBACK RAPIDO |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 23 | 34,78% | -0,01% | -0,01% | -2,29% | +2,32% | FEEDBACK RAPIDO |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 19 | 36,84% | +0,10% | +0,10% | -2,33% | +2,30% | FEEDBACK RAPIDO |
| BTC | 5g | Tecnico | CALIBRABILE | 18 | 55,56% | +0,29% | -0,10% | -1,98% | +2,75% | FEEDBACK RAPIDO |
| BTC | 5g | Classic technical | CALIBRABILE | 2 | 50,00% | -0,90% | +0,90% | -2,08% | +2,64% | FEEDBACK RAPIDO |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,16% | -0,16% | -0,37% | +4,24% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 19 | 36,84% | +0,15% | -0,42% | -2,50% | +2,79% | FEEDBACK RAPIDO |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 21 | 52,38% | +0,08% | +0,08% | -2,46% | +2,78% | FEEDBACK RAPIDO |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 21 | 52,38% | +0,08% | +0,08% | -2,46% | +2,78% | FEEDBACK RAPIDO |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 17 | 58,82% | +0,42% | +0,42% | -2,45% | +2,87% | FEEDBACK RAPIDO |
| BTC | 7g | Tecnico | CALIBRABILE | 17 | 41,18% | +0,75% | -0,24% | -2,12% | +3,17% | FEEDBACK RAPIDO |
| BTC | 7g | Classic technical | CALIBRABILE | 2 | 0,00% | +0,60% | -0,60% | -2,23% | +2,64% | FEEDBACK RAPIDO |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,77% | +1,77% | -0,79% | +4,24% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 16 | 37,50% | +0,51% | +0,09% | -2,71% | +3,40% | FEEDBACK RAPIDO |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 18 | 44,44% | +0,19% | +0,19% | -2,74% | +3,32% | FEEDBACK RAPIDO |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 18 | 44,44% | +0,19% | +0,19% | -2,74% | +3,32% | FEEDBACK RAPIDO |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 14 | 57,14% | +0,83% | +0,83% | -2,55% | +3,59% | FEEDBACK RAPIDO |
| BTC | 10g | Tecnico | CALIBRABILE | 15 | 46,67% | +0,63% | +0,13% | -2,44% | +3,68% | FEEDBACK RAPIDO |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,43% | -0,43% | -2,30% | +4,24% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 13 | 53,85% | +0,17% | +0,03% | -2,92% | +4,33% | FEEDBACK RAPIDO |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 14 | 50,00% | +0,07% | +0,07% | -2,85% | +4,36% | FEEDBACK RAPIDO |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 14 | 50,00% | +0,07% | +0,07% | -2,85% | +4,36% | FEEDBACK RAPIDO |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 10 | 70,00% | +1,09% | +1,09% | -2,22% | +5,16% | FEEDBACK RAPIDO |
| BTC | 14g | Tecnico | CALIBRABILE | 11 | 45,45% | +0,39% | -0,02% | -2,32% | +4,94% | FEEDBACK RAPIDO |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -2,25% | -2,25% | -3,05% | +4,24% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 7 | 42,86% | +0,17% | +0,17% | -2,47% | +5,31% | FEEDBACK RAPIDO |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 7 | 42,86% | +0,17% | +0,17% | -2,47% | +5,31% | FEEDBACK RAPIDO |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 7 | 42,86% | +0,17% | +0,17% | -2,47% | +5,31% | FEEDBACK RAPIDO |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 7 | 42,86% | +0,17% | +0,17% | -2,47% | +5,31% | FEEDBACK RAPIDO |
| BTC | 21g | Tecnico | CALIBRABILE | 6 | 16,67% | +0,07% | -0,44% | -2,34% | +5,40% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 26 | 42,31% | -0,04% | -0,06% | -0,51% | +0,63% | FEEDBACK RAPIDO |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 27 | 55,56% | -0,19% | +0,26% | -0,66% | +0,48% | FEEDBACK RAPIDO |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 27 | 55,56% | -0,19% | +0,26% | -0,66% | +0,48% | FEEDBACK RAPIDO |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 25 | 56,00% | -0,05% | +0,12% | -0,55% | +0,63% | FEEDBACK RAPIDO |
| DOGE | 1g | Tecnico | CALIBRABILE | 27 | 51,85% | -0,19% | +0,19% | -0,66% | +0,48% | FEEDBACK RAPIDO |
| DOGE | 1g | Classic technical | CALIBRABILE | 20 | 40,00% | +0,13% | -0,13% | -0,37% | +0,71% | FEEDBACK RAPIDO |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +3,18% | +3,18% | +1,82% | +3,24% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 25 | 44,00% | -0,21% | -0,22% | -0,84% | +0,80% | FEEDBACK RAPIDO |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 26 | 50,00% | -0,32% | +0,04% | -0,96% | +0,67% | FEEDBACK RAPIDO |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 26 | 50,00% | -0,32% | +0,04% | -0,96% | +0,67% | FEEDBACK RAPIDO |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 24 | 50,00% | -0,45% | +0,15% | -1,03% | +0,61% | FEEDBACK RAPIDO |
| DOGE | 2g | Tecnico | CALIBRABILE | 26 | 57,69% | -0,32% | +0,32% | -0,96% | +0,67% | FEEDBACK RAPIDO |
| DOGE | 2g | Classic technical | CALIBRABILE | 20 | 50,00% | +0,13% | -0,13% | -0,57% | +1,24% | FEEDBACK RAPIDO |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +5,65% | +5,65% | +4,05% | +5,83% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 24 | 45,83% | -0,41% | +0,08% | -2,09% | +1,92% | FEEDBACK RAPIDO |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 25 | 48,00% | -0,57% | -0,07% | -2,20% | +1,75% | FEEDBACK RAPIDO |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 25 | 48,00% | -0,57% | -0,07% | -2,20% | +1,75% | FEEDBACK RAPIDO |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 23 | 52,17% | -0,93% | +0,24% | -2,17% | +1,56% | FEEDBACK RAPIDO |
| DOGE | 3g | Tecnico | CALIBRABILE | 25 | 52,00% | -0,57% | +0,57% | -2,20% | +1,75% | FEEDBACK RAPIDO |
| DOGE | 3g | Classic technical | CALIBRABILE | 20 | 40,00% | -0,14% | +0,14% | -1,99% | +2,22% | FEEDBACK RAPIDO |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +3,13% | +3,13% | +0,09% | +6,33% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 22 | 59,09% | -0,79% | +0,37% | -3,15% | +2,31% | FEEDBACK RAPIDO |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 23 | 56,52% | -0,92% | +0,19% | -3,24% | +2,11% | FEEDBACK RAPIDO |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 23 | 56,52% | -0,92% | +0,19% | -3,24% | +2,11% | FEEDBACK RAPIDO |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 21 | 57,14% | -0,96% | +0,16% | -3,30% | +1,88% | FEEDBACK RAPIDO |
| DOGE | 5g | Tecnico | CALIBRABILE | 23 | 60,87% | -0,92% | +0,92% | -3,24% | +2,11% | FEEDBACK RAPIDO |
| DOGE | 5g | Classic technical | CALIBRABILE | 19 | 52,63% | -0,46% | +0,46% | -2,93% | +2,63% | FEEDBACK RAPIDO |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +1,26% | +1,26% | +0,02% | +6,57% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 20 | 60,00% | -1,28% | +0,77% | -3,73% | +2,47% | FEEDBACK RAPIDO |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 21 | 61,90% | -1,42% | +0,62% | -3,88% | +2,24% | FEEDBACK RAPIDO |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 21 | 61,90% | -1,42% | +0,62% | -3,88% | +2,24% | FEEDBACK RAPIDO |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 19 | 63,16% | -1,45% | +0,57% | -4,00% | +2,01% | FEEDBACK RAPIDO |
| DOGE | 7g | Tecnico | CALIBRABILE | 21 | 66,67% | -1,42% | +1,42% | -3,88% | +2,24% | FEEDBACK RAPIDO |
| DOGE | 7g | Classic technical | CALIBRABILE | 17 | 58,82% | -1,13% | +1,13% | -3,57% | +2,84% | FEEDBACK RAPIDO |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +1,19% | +1,19% | -0,23% | +6,57% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 18 | 61,11% | -1,97% | +1,44% | -4,66% | +2,61% | FEEDBACK RAPIDO |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 18 | 66,67% | -1,97% | +1,55% | -4,66% | +2,61% | FEEDBACK RAPIDO |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 18 | 66,67% | -1,97% | +1,55% | -4,66% | +2,61% | FEEDBACK RAPIDO |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 16 | 68,75% | -2,11% | +1,63% | -4,80% | +2,37% | FEEDBACK RAPIDO |
| DOGE | 10g | Tecnico | CALIBRABILE | 18 | 66,67% | -1,97% | +1,97% | -4,66% | +2,61% | FEEDBACK RAPIDO |
| DOGE | 10g | Classic technical | CALIBRABILE | 16 | 62,50% | -1,54% | +1,54% | -4,33% | +2,91% | FEEDBACK RAPIDO |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +1,09% | +1,09% | -1,85% | +6,57% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 14 | 85,71% | -3,12% | +3,12% | -5,95% | +2,29% | FEEDBACK RAPIDO |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 14 | 85,71% | -3,12% | +3,12% | -5,95% | +2,29% | FEEDBACK RAPIDO |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 14 | 85,71% | -3,12% | +3,12% | -5,95% | +2,29% | FEEDBACK RAPIDO |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 14 | 85,71% | -3,12% | +3,12% | -5,95% | +2,29% | FEEDBACK RAPIDO |
| DOGE | 14g | Tecnico | CALIBRABILE | 14 | 85,71% | -3,12% | +3,12% | -5,95% | +2,29% | FEEDBACK RAPIDO |
| DOGE | 14g | Classic technical | CALIBRABILE | 13 | 84,62% | -3,01% | +3,01% | -5,82% | +2,42% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 7 | 100,00% | -4,26% | +4,26% | -6,76% | +2,82% | FEEDBACK RAPIDO |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 7 | 100,00% | -4,26% | +4,26% | -6,76% | +2,82% | FEEDBACK RAPIDO |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 7 | 100,00% | -4,26% | +4,26% | -6,76% | +2,82% | FEEDBACK RAPIDO |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 7 | 100,00% | -4,26% | +4,26% | -6,76% | +2,82% | FEEDBACK RAPIDO |
| DOGE | 21g | Tecnico | CALIBRABILE | 7 | 100,00% | -4,26% | +4,26% | -6,76% | +2,82% | FEEDBACK RAPIDO |
| DOGE | 21g | Classic technical | CALIBRABILE | 6 | 100,00% | -4,06% | +4,06% | -6,55% | +3,21% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 20 | 50,00% | -0,10% | -0,41% | -0,60% | +0,66% | FEEDBACK RAPIDO |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 23 | 60,87% | -0,48% | -0,10% | -0,92% | +0,22% | FEEDBACK RAPIDO |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 26 | 57,69% | -0,30% | -0,22% | -0,77% | +0,41% | FEEDBACK RAPIDO |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 21 | 52,38% | -0,26% | -0,07% | -0,86% | +0,41% | FEEDBACK RAPIDO |
| SOL | 1g | Tecnico | CALIBRABILE | 27 | 51,85% | -0,18% | +0,04% | -0,66% | +0,51% | FEEDBACK RAPIDO |
| SOL | 1g | Classic technical | CALIBRABILE | 19 | 52,63% | -0,11% | +0,11% | -0,63% | +0,46% | FEEDBACK RAPIDO |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,51% | -0,51% | -0,47% | +0,31% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 20 | 40,00% | -0,27% | -0,62% | -0,93% | +0,73% | FEEDBACK RAPIDO |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 22 | 45,45% | -0,62% | -0,41% | -1,34% | +0,21% | FEEDBACK RAPIDO |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 25 | 44,00% | -0,51% | -0,40% | -1,18% | +0,52% | FEEDBACK RAPIDO |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 20 | 40,00% | -0,55% | -0,51% | -1,27% | +0,51% | FEEDBACK RAPIDO |
| SOL | 2g | Tecnico | CALIBRABILE | 26 | 42,31% | -0,39% | -0,05% | -1,04% | +0,62% | FEEDBACK RAPIDO |
| SOL | 2g | Classic technical | CALIBRABILE | 18 | 50,00% | -0,17% | +0,17% | -0,72% | +0,38% | FEEDBACK RAPIDO |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -1,38% | -1,38% | -1,57% | +0,62% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 19 | 36,84% | -0,42% | -0,89% | -2,30% | +1,81% | FEEDBACK RAPIDO |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 21 | 38,10% | -0,91% | -0,54% | -2,74% | +1,39% | FEEDBACK RAPIDO |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 24 | 37,50% | -0,75% | -0,51% | -2,55% | +1,64% | FEEDBACK RAPIDO |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 19 | 36,84% | -0,80% | -0,90% | -2,56% | +1,63% | FEEDBACK RAPIDO |
| SOL | 3g | Tecnico | CALIBRABILE | 25 | 48,00% | -0,66% | +0,19% | -2,40% | +1,72% | FEEDBACK RAPIDO |
| SOL | 3g | Classic technical | CALIBRABILE | 17 | 47,06% | -0,22% | +0,22% | -2,22% | +1,63% | FEEDBACK RAPIDO |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -3,20% | -3,20% | -3,71% | +0,62% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 17 | 41,18% | -0,84% | -1,16% | -3,35% | +2,40% | FEEDBACK RAPIDO |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 19 | 42,11% | -1,30% | -0,92% | -3,76% | +1,93% | FEEDBACK RAPIDO |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 22 | 40,91% | -1,02% | -0,89% | -3,53% | +2,20% | FEEDBACK RAPIDO |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 17 | 35,29% | -1,56% | -1,13% | -3,66% | +2,07% | FEEDBACK RAPIDO |
| SOL | 5g | Tecnico | CALIBRABILE | 23 | 56,52% | -1,08% | +0,37% | -3,49% | +2,26% | FEEDBACK RAPIDO |
| SOL | 5g | Classic technical | CALIBRABILE | 15 | 66,67% | -0,68% | +0,68% | -3,15% | +2,34% | FEEDBACK RAPIDO |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -3,99% | -3,99% | -6,07% | +0,62% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 15 | 46,67% | -1,21% | -0,99% | -4,00% | +2,73% | FEEDBACK RAPIDO |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 17 | 52,94% | -1,86% | -0,51% | -4,44% | +2,19% | FEEDBACK RAPIDO |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 20 | 55,00% | -1,59% | -0,42% | -4,18% | +2,45% | FEEDBACK RAPIDO |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 15 | 40,00% | -1,60% | -1,46% | -4,34% | +2,32% | FEEDBACK RAPIDO |
| SOL | 7g | Tecnico | CALIBRABILE | 21 | 47,62% | -1,49% | +0,52% | -4,14% | +2,50% | FEEDBACK RAPIDO |
| SOL | 7g | Classic technical | CALIBRABILE | 13 | 61,54% | -1,47% | +1,47% | -3,90% | +2,64% | FEEDBACK RAPIDO |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -6,33% | -6,33% | -6,71% | +0,62% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 14 | 42,86% | -1,94% | -0,42% | -4,67% | +2,77% | FEEDBACK RAPIDO |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 14 | 35,71% | -2,24% | -0,69% | -5,21% | +2,47% | FEEDBACK RAPIDO |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 17 | 35,29% | -1,88% | -0,53% | -4,90% | +2,72% | FEEDBACK RAPIDO |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 12 | 16,67% | -1,74% | -2,20% | -5,08% | +2,67% | FEEDBACK RAPIDO |
| SOL | 10g | Tecnico | CALIBRABILE | 18 | 72,22% | -1,96% | +1,69% | -4,89% | +2,77% | FEEDBACK RAPIDO |
| SOL | 10g | Classic technical | CALIBRABILE | 10 | 90,00% | -2,52% | +2,52% | -4,82% | +3,12% | FEEDBACK RAPIDO |
| SOL | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -5,36% | -5,36% | -7,47% | +0,62% | FEEDBACK RAPIDO |
| SOL | 10g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 14g | Global confluence | BENCHMARK | 13 | 61,54% | -3,12% | +0,53% | -5,48% | +2,97% | FEEDBACK RAPIDO |
| SOL | 14g | Famiglia statistica | CALIBRABILE | 10 | 70,00% | -2,98% | +0,77% | -5,81% | +2,48% | FEEDBACK RAPIDO |
| SOL | 14g | Scanner grezzo | DIAGNOSTICO | 13 | 76,92% | -3,01% | +1,30% | -5,37% | +2,81% | FEEDBACK RAPIDO |
| SOL | 14g | Market regime grezzo | DIAGNOSTICO | 8 | 12,50% | -2,91% | -2,46% | -5,15% | +2,78% | FEEDBACK RAPIDO |
| SOL | 14g | Tecnico | CALIBRABILE | 14 | 64,29% | -3,08% | +1,63% | -5,48% | +2,86% | FEEDBACK RAPIDO |
| SOL | 14g | Classic technical | CALIBRABILE | 6 | 100,00% | -3,29% | +3,29% | -5,57% | +3,56% | FEEDBACK RAPIDO |
| SOL | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -5,80% | -5,80% | -9,62% | +0,62% | FEEDBACK RAPIDO |
| SOL | 14g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 21g | Global confluence | BENCHMARK | 6 | 50,00% | -4,46% | -1,07% | -7,03% | +2,76% | FEEDBACK RAPIDO |
| SOL | 21g | Famiglia statistica | CALIBRABILE | 5 | 80,00% | -4,77% | +2,87% | -7,28% | +2,28% | FEEDBACK RAPIDO |
| SOL | 21g | Scanner grezzo | DIAGNOSTICO | 7 | 85,71% | -4,50% | +3,14% | -7,00% | +2,58% | FEEDBACK RAPIDO |
| SOL | 21g | Market regime grezzo | DIAGNOSTICO | 6 | 33,33% | -4,46% | -1,63% | -7,03% | +2,76% | FEEDBACK RAPIDO |
| SOL | 21g | Tecnico | CALIBRABILE | 7 | 42,86% | -4,50% | -1,38% | -7,00% | +2,58% | FEEDBACK RAPIDO |
| SOL | 21g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | FEEDBACK RAPIDO |

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

Generato: 2026-08-05 05:15 UTC

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
| BTC | 28 | FEEDBACK RAPIDO | 27 | 0 | 0 | 0 | Famiglia statistica | 1g | 51,85% | +0,02% | feedback rapido: utile da osservare, non da pesare |
| SOL | 28 | FEEDBACK RAPIDO | 27 | 0 | 0 | 0 | Tecnico | 1g | 51,85% | +0,04% | feedback rapido: utile da osservare, non da pesare |
| DOGE | 28 | FEEDBACK RAPIDO | 27 | 0 | 0 | 0 | Famiglia statistica | 1g | 55,56% | +0,26% | feedback rapido: utile da osservare, non da pesare |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Classic technical | 4 | 0,00% | -0,76% | +0,76% | +0,03% | +1,12% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Famiglia statistica | 27 | 51,85% | +0,02% | +0,02% | -0,31% | +0,58% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Microstruttura exchange | 1 | 100,00% | +2,00% | +2,00% | +1,48% | +2,25% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 22 | 36,36% | -0,39% | +0,24% | -0,12% | +0,81% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Classic technical | 4 | 25,00% | -0,86% | +0,86% | +0,50% | +1,73% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Famiglia statistica | 26 | 46,15% | +0,07% | +0,07% | -0,44% | +0,82% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Microstruttura exchange | 1 | 100,00% | +3,18% | +3,18% | +3,05% | +3,89% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 21 | 38,10% | -0,44% | +0,34% | -0,16% | +1,10% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Classic technical | 3 | 33,33% | -0,46% | +0,46% | -0,83% | +2,15% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Famiglia statistica | 25 | 52,00% | -0,01% | -0,01% | -1,51% | +1,71% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Microstruttura exchange | 1 | 100,00% | +1,88% | +1,88% | +1,44% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 20 | 40,00% | -0,12% | +0,48% | -1,19% | +2,15% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Classic technical | 2 | 50,00% | +0,90% | -0,90% | -2,08% | +2,64% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 23 | 34,78% | -0,01% | -0,01% | -2,29% | +2,32% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -0,16% | -0,16% | -0,37% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 18 | 55,56% | -0,10% | +0,29% | -1,98% | +2,75% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Classic technical | 2 | 0,00% | -0,60% | +0,60% | -2,23% | +2,64% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 21 | 52,38% | +0,08% | +0,08% | -2,46% | +2,78% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Microstruttura exchange | 1 | 100,00% | +1,77% | +1,77% | -0,79% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 17 | 41,18% | -0,24% | +0,75% | -2,12% | +3,17% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 18 | 44,44% | +0,19% | +0,19% | -2,74% | +3,32% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -0,43% | -0,43% | -2,30% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 15 | 46,67% | +0,13% | +0,63% | -2,44% | +3,68% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Famiglia statistica | 14 | 50,00% | +0,07% | +0,07% | -2,85% | +4,36% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Microstruttura exchange | 1 | 0,00% | -2,25% | -2,25% | -3,05% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 11 | 45,45% | -0,02% | +0,39% | -2,32% | +4,94% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Famiglia statistica | 7 | 42,86% | +0,17% | +0,17% | -2,47% | +5,31% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Tecnico | 6 | 16,67% | -0,44% | +0,07% | -2,34% | +5,40% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 20 | 40,00% | -0,13% | +0,13% | -0,37% | +0,71% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Famiglia statistica | 27 | 55,56% | +0,26% | -0,19% | -0,66% | +0,48% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Microstruttura exchange | 2 | 100,00% | +3,18% | +3,18% | +1,82% | +3,24% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 27 | 51,85% | +0,19% | -0,19% | -0,66% | +0,48% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Classic technical | 20 | 50,00% | -0,13% | +0,13% | -0,57% | +1,24% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Famiglia statistica | 26 | 50,00% | +0,04% | -0,32% | -0,96% | +0,67% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Microstruttura exchange | 2 | 100,00% | +5,65% | +5,65% | +4,05% | +5,83% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 26 | 57,69% | +0,32% | -0,32% | -0,96% | +0,67% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Classic technical | 20 | 40,00% | +0,14% | -0,14% | -1,99% | +2,22% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Famiglia statistica | 25 | 48,00% | -0,07% | -0,57% | -2,20% | +1,75% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Microstruttura exchange | 2 | 100,00% | +3,13% | +3,13% | +0,09% | +6,33% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 25 | 52,00% | +0,57% | -0,57% | -2,20% | +1,75% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Classic technical | 19 | 52,63% | +0,46% | -0,46% | -2,93% | +2,63% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 23 | 56,52% | +0,19% | -0,92% | -3,24% | +2,11% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Microstruttura exchange | 2 | 100,00% | +1,26% | +1,26% | +0,02% | +6,57% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 23 | 60,87% | +0,92% | -0,92% | -3,24% | +2,11% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Classic technical | 17 | 58,82% | +1,13% | -1,13% | -3,57% | +2,84% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 21 | 61,90% | +0,62% | -1,42% | -3,88% | +2,24% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Microstruttura exchange | 2 | 100,00% | +1,19% | +1,19% | -0,23% | +6,57% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 21 | 66,67% | +1,42% | -1,42% | -3,88% | +2,24% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Classic technical | 16 | 62,50% | +1,54% | -1,54% | -4,33% | +2,91% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 18 | 66,67% | +1,55% | -1,97% | -4,66% | +2,61% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Microstruttura exchange | 2 | 100,00% | +1,09% | +1,09% | -1,85% | +6,57% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 18 | 66,67% | +1,97% | -1,97% | -4,66% | +2,61% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Classic technical | 13 | 84,62% | +3,01% | -3,01% | -5,82% | +2,42% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Famiglia statistica | 14 | 85,71% | +3,12% | -3,12% | -5,95% | +2,29% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 14 | 85,71% | +3,12% | -3,12% | -5,95% | +2,29% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Classic technical | 6 | 100,00% | +4,06% | -4,06% | -6,55% | +3,21% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Famiglia statistica | 7 | 100,00% | +4,26% | -4,26% | -6,76% | +2,82% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Tecnico | 7 | 100,00% | +4,26% | -4,26% | -6,76% | +2,82% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Classic technical | 19 | 52,63% | +0,11% | -0,11% | -0,63% | +0,46% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Famiglia statistica | 23 | 60,87% | -0,10% | -0,48% | -0,92% | +0,22% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 1 | 0,00% | -0,51% | -0,51% | -0,47% | +0,31% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 27 | 51,85% | +0,04% | -0,18% | -0,66% | +0,51% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Classic technical | 18 | 50,00% | +0,17% | -0,17% | -0,72% | +0,38% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Famiglia statistica | 22 | 45,45% | -0,41% | -0,62% | -1,34% | +0,21% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Microstruttura exchange | 1 | 0,00% | -1,38% | -1,38% | -1,57% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 26 | 42,31% | -0,05% | -0,39% | -1,04% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Classic technical | 17 | 47,06% | +0,22% | -0,22% | -2,22% | +1,63% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Famiglia statistica | 21 | 38,10% | -0,54% | -0,91% | -2,74% | +1,39% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Microstruttura exchange | 1 | 0,00% | -3,20% | -3,20% | -3,71% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 25 | 48,00% | +0,19% | -0,66% | -2,40% | +1,72% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Classic technical | 15 | 66,67% | +0,68% | -0,68% | -3,15% | +2,34% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 19 | 42,11% | -0,92% | -1,30% | -3,76% | +1,93% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -3,99% | -3,99% | -6,07% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 23 | 56,52% | +0,37% | -1,08% | -3,49% | +2,26% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Classic technical | 13 | 61,54% | +1,47% | -1,47% | -3,90% | +2,64% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 17 | 52,94% | -0,51% | -1,86% | -4,44% | +2,19% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -6,33% | -6,33% | -6,71% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 21 | 47,62% | +0,52% | -1,49% | -4,14% | +2,50% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Classic technical | 10 | 90,00% | +2,52% | -2,52% | -4,82% | +3,12% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 14 | 35,71% | -0,69% | -2,24% | -5,21% | +2,47% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -5,36% | -5,36% | -7,47% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 18 | 72,22% | +1,69% | -1,96% | -4,89% | +2,77% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Classic technical | 6 | 100,00% | +3,29% | -3,29% | -5,57% | +3,56% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Famiglia statistica | 10 | 70,00% | +0,77% | -2,98% | -5,81% | +2,48% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Frattale SOL | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Microstruttura exchange | 1 | 0,00% | -5,80% | -5,80% | -9,62% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Tecnico | 14 | 64,29% | +1,63% | -3,08% | -5,48% | +2,86% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Famiglia statistica | 5 | 80,00% | +2,87% | -4,77% | -7,28% | +2,28% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Frattale SOL | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Tecnico | 7 | 42,86% | -1,38% | -4,50% | -7,00% | +2,58% | OSSERVA | 0,0 | BASSA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 26 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 25 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 27 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Classic technical | 11 | 18,18% | -0,71% |
| BTC | BREVE | Famiglia statistica | 78 | 50,00% | +0,03% |
| BTC | BREVE | Microstruttura exchange | 3 | 100,00% | +2,36% |
| BTC | BREVE | Tecnico | 63 | 38,10% | -0,32% |
| BTC | SETTIMANALE | Classic technical | 4 | 25,00% | +0,15% |
| BTC | SETTIMANALE | Famiglia statistica | 62 | 43,55% | +0,08% |
| BTC | SETTIMANALE | Microstruttura exchange | 3 | 33,33% | +0,39% |
| BTC | SETTIMANALE | Tecnico | 50 | 48,00% | -0,08% |
| BTC | SWING | Famiglia statistica | 21 | 47,62% | +0,10% |
| BTC | SWING | Microstruttura exchange | 1 | 0,00% | -2,25% |
| BTC | SWING | Tecnico | 17 | 35,29% | -0,17% |
| DOGE | BREVE | Classic technical | 60 | 43,33% | -0,04% |
| DOGE | BREVE | Famiglia statistica | 78 | 51,28% | +0,08% |
| DOGE | BREVE | Microstruttura exchange | 6 | 100,00% | +3,99% |
| DOGE | BREVE | Tecnico | 78 | 53,85% | +0,36% |
| DOGE | SETTIMANALE | Classic technical | 52 | 57,69% | +1,01% |
| DOGE | SETTIMANALE | Famiglia statistica | 62 | 61,29% | +0,73% |
| DOGE | SETTIMANALE | Microstruttura exchange | 6 | 100,00% | +1,18% |
| DOGE | SETTIMANALE | Tecnico | 62 | 64,52% | +1,39% |
| DOGE | SWING | Classic technical | 19 | 89,47% | +3,34% |
| DOGE | SWING | Famiglia statistica | 21 | 90,48% | +3,50% |
| DOGE | SWING | Tecnico | 21 | 90,48% | +3,50% |
| SOL | BREVE | Classic technical | 54 | 50,00% | +0,16% |
| SOL | BREVE | Famiglia statistica | 66 | 48,48% | -0,34% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 3 | 0,00% | -1,70% |
| SOL | BREVE | Tecnico | 78 | 47,44% | +0,06% |
| SOL | SETTIMANALE | Classic technical | 38 | 71,05% | +1,44% |
| SOL | SETTIMANALE | Famiglia statistica | 50 | 44,00% | -0,72% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Microstruttura exchange | 3 | 0,00% | -5,22% |
| SOL | SETTIMANALE | Tecnico | 62 | 58,06% | +0,80% |
| SOL | SWING | Classic technical | 6 | 100,00% | +3,29% |
| SOL | SWING | Famiglia statistica | 15 | 73,33% | +1,47% |
| SOL | SWING | Frattale SOL | 2 | 0,00% | -3,49% |
| SOL | SWING | Microstruttura exchange | 1 | 0,00% | -5,80% |
| SOL | SWING | Tecnico | 21 | 57,14% | +0,63% |

## Aree ancora in attesa

| Asset | Famiglia | Righe senza controlli | Stato |
| --- | --- | --- | --- |
| BTC | BREVE | 3 | in attesa di controlli maturati |
| BTC | SETTIMANALE | 4 | in attesa di controlli maturati |
| BTC | SWING | 5 | in attesa di controlli maturati |
| BTC | MEDIO | 15 | in attesa di controlli maturati |
| SOL | SWING | 2 | in attesa di controlli maturati |
| SOL | MEDIO | 15 | in attesa di controlli maturati |
| DOGE | BREVE | 3 | in attesa di controlli maturati |
| DOGE | SETTIMANALE | 3 | in attesa di controlli maturati |
| DOGE | SWING | 4 | in attesa di controlli maturati |
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
| BTC     |         28 |               0 |          28 | RACCOLTA DATI | n/a              | n/a             | n/a                   | n/a            |
| SOL     |         28 |               0 |          28 | RACCOLTA DATI | n/a              | n/a             | n/a                   | n/a            |
| DOGE    |         28 |               0 |          28 | RACCOLTA DATI | n/a              | n/a             | n/a                   | n/a            |

Regola: sotto 60 controlli osserva soltanto; da 100+ controlli può diventare utile per correggere rischio spot/leva nel Decision Report.

## Ultima lettura rapida

| Asset   | Rischio spot   | Rischio leva   | Nota leva                                                         |
|:--------|:---------------|:---------------|:------------------------------------------------------------------|
| BTC     | BASSO          | ALTO           | leva da limitare; 2x/3x solo con invalidazione chiara             |
| SOL     | BASSO          | ALTO           | spot/tranche; se proprio leva, massimo 2x con margine molto largo |
| DOGE    | ALTO           | MOLTO ALTO     | spot/tranche; se proprio leva, massimo 2x con margine molto largo |
<!-- RISK_CALIBRATION_END -->

</details>
<!-- COMPACT_SECTION_END:risk_calibration -->

<!-- COMPACT_SECTION_START:global_confluence -->
<details open>
<summary><strong>🌐 Global Confluence — quadro finale</strong></summary>

<!-- GLOBAL_CONFLUENCE_START -->
# Sintesi finale di confluenza

Generato: 2026-08-05 05:15 UTC


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
| SOL | +1 | MISTA / PARZIALE | Neutrale / misto | BASSA / RACCOLTA DATI | HOLD LEGGERO / ATTESA CONFERME | conferma del adam and eve bottom sopra 83,81; nuova conferma tecnica sopra 78,73; milestone analogiche 77,61 / 91,83, valide soltanto se rientra anche il gap frattale. | Allarmi sotto 70,21 / 73,40 / 62,19. |
| DOGE | 0 | MISTA / PARZIALE | Neutrale / misto | BASSA / RACCOLTA DATI | STAI ALLA FINESTRA | Sopra 0.07380 migliora; sopra 0.06966 viene invalidato il pattern ribassista dominante. | Sotto 0.06829 il rischio ribassista aumenta. |

## Punteggi per modulo

| Asset | Scanner grezzo | Market grezzo | Famiglia statistica | Scanner path | Tecnico | Classic tech | Frattale SOL | Fractal path | RSI top-cycle | Lifecycle EMA | Exchange flow | Futures | Daily change | Totale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +3 | +3 | +4 | 0 | -1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | -1 | +2 |
| SOL | +3 | +2 | +4 | 0 | -2 | -1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | +1 |
| DOGE | +1 | +2 | +2 | 0 | -2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

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

- Famiglia statistica: **+4** — Scanner grezzo +3, Market Regime grezzo +3, match regime 18. Scanner e regime concordi con almeno 10 match: bonus massimo di 1 punto. Punteggio contato nel Global: +4.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **+3** — Casi positivi 80,00%, return centrale 30g +9,97%. Direzione scanner: SALITA. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **+3** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 18, positivi 30g 88,89%, return p50 +9,57%.
- Scanner path: **0** — Controlli disponibili 26. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **-1** — Score tecnico -1/12, verdetto neutrale / misto, trend ribassista, struttura volatilità in espansione, divergenza rialzista rsi, Wyckoff possibile accumulazione, pattern score 0 (rialzista Doppio minimo / CANDIDATO; ribassista Doppio massimo / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **0** — Score classico -1/12, verdetto NEUTRALE / MISTO, stage STAGE 4 / MARKDOWN, struttura COMPRESSIONE / TRIANGOLO POSSIBILE, Wyckoff ACCUMULO POSSIBILE / RANGE BASSO, volatilità locale BASSO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Non applicabile a questo asset.
- Fractal path: **0** — Non applicabile a questo asset.
- RSI top-cycle: **0** — Non applicabile a questo asset.
- Lifecycle EMA: **0** — Non applicabile a questo asset.
- Exchange flow: **0** — Flow +1.75, derivati +0.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +0.75; exchange 3/3, copertura 100%, consenso bull 2, bear 0, divergenze 0, campioni 4h 9 su 4.00h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias LEGGERMENTE POSITIVA / NON PESATA; confidenza MEDIA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Misto, forza 1/5.
- Daily change: **-1** — BTC: cambiamento medio in peggioramento rispetto a ieri.

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

- Famiglia statistica: **+4** — Scanner grezzo +3, Market Regime grezzo +2, match regime 16. Scanner e regime concordi con almeno 10 match: bonus massimo di 1 punto. Punteggio contato nel Global: +4.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **+3** — Casi positivi 72,50%, return centrale 30g +8,72%. Direzione scanner: SALITA. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **+2** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 16, positivi 30g 81,25%, return p50 +7,41%.
- Scanner path: **0** — Controlli disponibili 26. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **-2** — Score tecnico -6/12, verdetto debole, trend ribassista, struttura compressione / triangolo, divergenza ribassista nascosta rsi, Wyckoff markdown / fase ribassista, pattern score 0 (rialzista Adam and Eve Bottom / CANDIDATO; ribassista Doppio massimo / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **-1** — Score classico -7/12, verdetto RIBASSISTA / FRAGILE, stage STAGE 4 / MARKDOWN, struttura MASSIMI E MINIMI DECRESCENTI, Wyckoff ACCUMULO POSSIBILE / RANGE BASSO, volatilità locale BASSO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Verdetto ANALOGIA DEBOLE / SCENARIO SECONDARIO, somiglianza strutturale +56,86%, aderenza live +70,03%, errore live +14,99%, gap corrente -17,26%, peso operativo 0, tracking STRUTTURA STABILE, fase FRATTALE SOLO DI CONTESTO, rischio ALTO.
- Fractal path: **0** — Controlli disponibili 22, ma percorso ancorato non aderente: gap -17,26%, errore live +14,99%. Peso 0.
- RSI top-cycle: **0** — Rischio top-cycle RSI: BASSO.
- Lifecycle EMA: **0** — Contesto non pesato nel Global. Lifecycle score 4, bias SQUEEZE SETUP MODERATO, EMA200 111,99 $, upside EMA200 +51,55%, gap EMA50/EMA200 -4,81%, hit EMA200 12w +20,00%, trend STABILE / DA CONFERMARE. Peso Global forzato a 0.
- Exchange flow: **0** — Flow +1.75, derivati +0.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +1.00; exchange 3/3, copertura 100%, consenso bull 1, bear 0, divergenze 0, campioni 4h 9 su 4.00h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias LEGGERMENTE POSITIVA / NON PESATA; confidenza MEDIA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Rischio sotto, forza 5/5.
- Daily change: **0** — SOL: nessun cambiamento forte in miglioramento rispetto a ieri.

Conferme: conferma del adam and eve bottom sopra 83,81; nuova conferma tecnica sopra 78,73; milestone analogiche 77,61 / 91,83, valide soltanto se rientra anche il gap frattale.

Invalidazioni: Allarmi sotto 70,21 / 73,40 / 62,19.

### DOGE

- Confluenza: **MISTA / PARZIALE**
- Bias: **Neutrale / misto**
- Punteggio finale: **0**
- Affidabilità: **BASSA / RACCOLTA DATI**
- Azione coerente: **STAI ALLA FINESTRA**

DOGE non ha ancora una confluenza pulita. Serve conferma tecnica prima di trattarlo come asset forte.

Dettaglio moduli:

- Famiglia statistica: **+2** — Scanner grezzo +1, Market Regime grezzo +2, match regime 22. Scanner e regime concordi con almeno 10 match: bonus massimo di 1 punto. Punteggio contato nel Global: +2.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **+1** — Casi positivi 55,00%, return centrale 30g +4,72%. Direzione scanner: INCERTO. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **+2** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 22, positivi 30g 63,64%, return p50 +6,69%.
- Scanner path: **0** — Controlli disponibili 26. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **-2** — Score tecnico -5/12, verdetto debole, trend ribassista, struttura ribassista con massimi e minimi decrescenti, divergenza ribassista nascosta rsi, Wyckoff possibile accumulazione, pattern score 0 (rialzista Doppio minimo / CANDIDATO; ribassista Adam and Eve Top / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **0** — Score classico -2/12, verdetto DEBOLE / NON CONFERMATO, stage STAGE 4 / MARKDOWN, struttura VOLATILITÀ IN ESPANSIONE, Wyckoff SPRING / TEST POSSIBILE, volatilità locale BASSO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Non applicabile a questo asset.
- Fractal path: **0** — Non applicabile a questo asset.
- RSI top-cycle: **0** — Non applicabile a questo asset.
- Lifecycle EMA: **0** — Non applicabile a questo asset.
- Exchange flow: **0** — Flow +1.75, derivati +0.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +0.75; exchange 3/3, copertura 100%, consenso bull 1, bear 2, divergenze 0, campioni 4h 9 su 4.00h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias LEGGERMENTE POSITIVA / NON PESATA; confidenza MEDIA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Misto, forza 1/5.
- Daily change: **0** — DOGE: nessun cambiamento forte in peggioramento rispetto a ieri.

Conferme: Sopra 0.07380 migliora; sopra 0.06966 viene invalidato il pattern ribassista dominante.

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

Generato: 2026-08-05 05:15 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [btc_macro_cycle_report.md](btc_macro_cycle_report.md)

Questo modulo descrive il contesto macro di Bitcoin. Non genera entrate tattiche, non autorizza leva e pesa **0** nel Global Confluence.

## Sintesi

| Voce | Valore | Lettura |
| --- | --- | --- |
| Prezzo BTC | 64.253 $ | prezzo corrente |
| Power Law centrale | 123.371 $ | deviazione -47,92% |
| Banda p10-p90 | 76.478 $ / 309.644 $ | SOTTO LA BANDA P10 |
| Percentile residuo | 1,45% | posizione storica nel corridoio |
| Esponente β | 5,8283 | R² log-log 91,96% |
| Stabilità β | BASSA | range 1,3117 cambiando finestra |
| Ultimo halving | 2024-04-19 | 838 giorni fa |
| Fase ciclo | 57,36% | percentuale indicativa del ciclo quadriennale |
| Peso Global | 0 | CONTESTO MACRO / DIAGNOSTICO |

La Power Law viene trattata come regressione empirica, non come legge fisica. Il report mostra quanto cambia l'esponente usando finestre iniziali diverse e la confronta con il benchmark ingenuo 'prezzo invariato'.

## Bitcoin Power Law

- Campione: 2014-09-17 → 2026-08-05 (4340 osservazioni)
- Formula stimata: prezzo ≈ exp(-39.2576) × giorni^5.8283
- Prezzo centrale oggi: **123.371 $**
- Posizione corrente: **SOTTO LA BANDA P10**, percentile 1,45%
- Scarto dal centro: **-47,92%**

![Bitcoin Power Law](btc_power_law_chart.png)

![Bitcoin Power Law log-log](btc_power_law_loglog_chart.png)

### Stabilità dell'esponente

| Inizio campione | β | R² log-log |
| --- | --- | --- |
| 2014 | 5,8283 | 91,96% |
| 2015 | 5,9134 | 91,52% |
| 2016 | 5,6010 | 87,76% |
| 2017 | 4,8708 | 82,87% |
| 2018 | 4,6017 | 78,33% |

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
| 2012-11-28 → 2016-07-09 | 2014-12-25 | -22,31% | -22,82% | -23,42% | +42,83% |
| 2016-07-09 → 2020-05-11 | 2018-09-21 | -3,75% | -38,61% | -39,31% | +48,77% |
| 2020-05-11 → 2024-04-19 | 2022-08-14 | -16,54% | -30,92% | -10,97% | +20,93% |

Campione molto piccolo: questi rendimenti sono contesto di ciclo, non probabilità affidabili.

## SOL/BTC e DOGE/BTC dentro il tempo Bitcoin

![Altcoin nel ciclo BTC](alt_btc_cycle_spirals.png)

| Asset | Coppia | Forza vs BTC | Score raw | Candidato | 30g | Peso Global |
| --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | SOTTOPERFORMA BTC | -6 | -1 | -10.296871811084118 | 0 |
| DOGE | DOGE/BTC | SOTTOPERFORMA BTC | -5 | -1 | -11.026235741153933 | 0 |

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

Generato: 2026-08-05 05:15 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [relative_strength_btc_report.md](relative_strength_btc_report.md)

Questo modulo controlla se SOL e DOGE stanno davvero battendo Bitcoin. Una salita in USD accompagnata da una coppia ALT/BTC ribassista è spesso soltanto trascinamento di BTC.

**Protezione iniziale:** il candidato relativo è limitato a -1/0/+1, ma il peso nel Global resta **0**. La coppia BTC conferma o indebolisce il tecnico USD; non viene sommata come secondo modulo indipendente.

## Sintesi

| Asset | Coppia | Prezzo | Score raw | Candidato | Peso Global | Forza vs BTC | Confidenza | 30g | Tecnico USD | Lettura combinata |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | 0.00114820 | -6 | -1 | 0 | SOTTOPERFORMA BTC | MEDIA | -10,30% | RIBASSISTA | DEBOLEZZA COMPLETA: scende in USD e contro BTC |
| DOGE | DOGE/BTC | 0.00000109 | -5 | -1 | 0 | SOTTOPERFORMA BTC | MEDIA | -11,03% | RIBASSISTA | DEBOLEZZA COMPLETA: scende in USD e contro BTC |

## Matrice di lettura

| ALT/USD | ALT/BTC | Interpretazione |
| --- | --- | --- |
| Rialzista | Rialzista | Conferma migliore: sale e batte BTC |
| Rialzista | Ribassista | Sale soprattutto perché BTC trascina il mercato |
| Ribassista | Rialzista | Forza relativa nascosta / possibile rotazione futura |
| Ribassista | Ribassista | Debolezza completa |

## SOL/BTC

- **Verdetto relativo:** SOTTOPERFORMA BTC (-6)
- **Candidato futuro:** -1; **peso attuale Global: 0**
- **Lettura combinata USD/BTC:** DEBOLEZZA COMPLETA: scende in USD e contro BTC
- **Struttura:** MASSIMI E MINIMI DECRESCENTI
- **Rendimenti relativi:** 7g -0,50%; 30g -10,30%; 90g +4,86%; 180g -7,78%
- **Daily:** RSI 41.46; MA50 0.00118624; MA200 0.00119700
- **Weekly:** MA30 0.00119704; RSI 43.67
- **Livelli:** supporto 0.00114600; resistenza 0.00116300; breakout 60g 0.00134900; breakdown 60g 0.00100900
- **Pattern:** DOPPIO MINIMO / TARGET RAGGIUNTO; neckline 0.00113200; target 0.00117200
- **Fibonacci:** VICINO — 61.8% a 0.00113888
- **Fonte:** Yahoo Finance SOL-BTC (coppia diretta)
- **Motivi score:** prezzo sotto MA50 daily; prezzo sotto MA200 daily; MA50 daily in salita; prezzo sotto MA30 weekly; MA30 weekly in discesa; struttura con massimi/minimi decrescenti; RSI relativo debole; MACD relativo negativo

![Grafico SOL/BTC](relative_strength_SOLBTC.png)

## DOGE/BTC

- **Verdetto relativo:** SOTTOPERFORMA BTC (-5)
- **Candidato futuro:** -1; **peso attuale Global: 0**
- **Lettura combinata USD/BTC:** DEBOLEZZA COMPLETA: scende in USD e contro BTC
- **Struttura:** COMPRESSIONE / TRIANGOLO POSSIBILE
- **Rendimenti relativi:** 7g -1,75%; 30g -11,03%; 90g -21,17%; 180g -22,70%
- **Daily:** RSI 37.72; MA50 0.00000118; MA200 0.00000132
- **Weekly:** MA30 0.00000131; RSI 29.77
- **Livelli:** supporto 0.00000105; resistenza 0.00000115; breakout 60g 0.00000153; breakdown 60g 0.00000104
- **Pattern:** DOPPIO MASSIMO / CONFERMATO; neckline 0.00000112; target 0.00000099
- **Fibonacci:** NON ATTIVO — 23.6% a 0.00000115
- **Fonte:** Rapporto sintetico DOGE-USD / BTC-USD (sintetica)
- **Motivi score:** prezzo sotto MA50 daily; prezzo sotto MA200 daily; MA50 daily in discesa; prezzo sotto MA30 weekly; MA30 weekly in discesa; RSI relativo debole; MACD relativo positivo

![Grafico DOGE/BTC](relative_strength_DOGEBTC.png)

## Backtest storico diagnostico

Il backtest usa soltanto indicatori disponibili alla data del segnale e campiona una volta a settimana. È utile subito, ma non sostituisce il tracker live: le soglie sono state definite prima di vedere il risultato.

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto direzione | Return futuro mediano |
| --- | --- | --- | --- | --- | --- |
| SOL | 7g | 203 | 52,22% | +1,96% | -1,30% |
| SOL | 30g | 202 | 47,52% | +4,66% | +0,36% |
| SOL | 90g | 196 | 53,57% | +10,26% | +2,02% |
| DOGE | 7g | 292 | 55,82% | +1,85% | -1,73% |
| DOGE | 30g | 289 | 52,94% | +2,03% | -3,93% |
| DOGE | 90g | 285 | 54,04% | +6,94% | -8,47% |

## Tracker live e gate futuro

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto | Stato | Peso Global |
| --- | --- | --- | --- | --- | --- | --- |
| SOL | 1g | 11 | 72,73% | +0,00% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 3g | 9 | 55,56% | +0,13% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 7g | 5 | 60,00% | +0,47% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 14g | 0 | n/a | n/a | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 30g | 0 | n/a | n/a | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 1g | 25 | 76,00% | +0,54% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 3g | 23 | 65,22% | +0,89% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 7g | 19 | 84,21% | +1,83% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 14g | 12 | 100,00% | +2,81% | LOCKED / RACCOLTA LIVE | 0 |
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

Ultima candela SOL usata: **5 agosto 2026**

## Verdetto: ANALOGIA DEBOLE / SCENARIO SECONDARIO

- **Fase attuale:** FRATTALE SOLO DI CONTESTO
- **Somiglianza totale:** +56,86%
- **Somiglianza strutturale:** +56,86%
- **Aderenza prezzo live:** +70,03%
- **Errore medio live:** +14,99%
- **Gap prezzo corrente:** -17,26%
- **Peso operativo suggerito:** 0
- **Affidabilita:** BASSA
- **Rischio fase:** ALTO
- **Trend tracking:** STRUTTURA STABILE
- **Sintesi:** Esistono alcuni elementi comuni, ma non abbastanza per una conferma.
- **SOL è al giorno:** 60 dal bottom usato.
- **Giorno BTC equivalente:** 2023-01-20
- **Prossimo step:** Proiezione condizionale, non conferma operativa: **Laterale / movimento non forte.** Zona bassa **73,78 $** intorno al **9 agosto 2026**; zona alta **77,49 $** intorno al **14 agosto 2026**; fine step circa **76,43 $** entro il **19 agosto 2026**.

## Somiglianza prima e dopo inizio programma

Questa sezione separa la somiglianza della forma dall'aderenza reale del prezzo.

- **Inizio programma/scanner:** 3 luglio 2026
- **Prima del programma** = backtest retroattivo.
- **Da inizio programma** = verifica live: è la parte più importante per l'uso operativo.

| Periodo | Date | Giorni | Aderenza prezzo | Errore medio | Gap ultimo | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| Prima del programma | 6 giugno 2026 -> 2 luglio 2026 | 27 | +87,95% | +6,02% | +21,89% | ABBASTANZA ALLINEATO |
| Da inizio programma | 3 luglio 2026 -> 5 agosto 2026 | 34 | +70,03% | +14,99% | -17,26% | DEVIAZIONE MODERATA |
| Totale dal bottom | 6 giugno 2026 -> 5 agosto 2026 | 61 | +77,96% | +11,02% | -17,26% | DEVIAZIONE MODERATA |

Nota: un frattale può avere una forma simile ma un prezzo distante. In quel caso non è operativo finché il gap non rientra.

## Lettura operativa veloce

Il frattale non deve generare acquisti o leva adesso. La forma è un contesto, ma l'aderenza live del prezzo è insufficiente.

| Voce | Risposta | Perché |
| --- | --- | --- |
| Uso operativo | NO | Il frattale vale 0 punti operativi finché il prezzo resta non aderente. |
| Aderenza live | +70,03% | Errore medio live +14,99%. |
| Gap corrente | -17,26% | Deve rientrare circa entro ±12%. |
| Prima conferma prezzo | 77,61 $ | Serve anche miglioramento del gap, non solo una candela sopra il livello. |
| Seconda conferma | 91,83 $ | Rende più credibile il percorso, ma non sostituisce l'aderenza. |
| Invalidazione soft | 70,21 $ | Sotto questa zona il quadro peggiora. |
| Invalidazione forte | 62,19 $ | Sotto il bottom il paragone è quasi rotto. |

## Target ciclo fino al top BTC 2025

| Voce | Valore |
| --- | --- |
| Stato | CONTESTO / NON OPERATIVO |
| Top BTC 2025 | 6 ottobre 2025 - 124.753 $ |
| Data SOL equivalente | 21 aprile 2029 |
| Target ciclo base da oggi | 406,61 $ |
| Massimo percorso base | 406,61 $ (21 aprile 2029) |

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
| Prima conferma | 77,61 $ | Deve accompagnarsi al rientro del gap. |
| Seconda conferma | 91,83 $ | Scenario più credibile. |
| Invalidazione soft | 70,21 $ | Il frattale si indebolisce. |
| Invalidazione forte | 62,19 $ | Il paragone si rompe. |

## Proiezione veloce con date SOL

| Orizzonte | Data SOL | BTC fece | SOL base | Min percorso | Max percorso |
| --- | --- | --- | --- | --- | --- |
| 7 giorni | 12 agosto 2026 | +1,77% | 75,22 $ | 73,78 $ | 75,35 $ |
| 14 giorni | 19 agosto 2026 | +3,41% | 76,43 $ | 73,78 $ | 77,49 $ |
| 30 giorni | 4 settembre 2026 | +7,28% | 79,29 $ | 70,57 $ | 80,31 $ |
| 60 giorni | 4 ottobre 2026 | +24,25% | 91,83 $ | 65,80 $ | 91,83 $ |
| 90 giorni | 3 novembre 2026 | +24,56% | 92,06 $ | 65,80 $ | 99,36 $ |
| 120 giorni | 3 dicembre 2026 | +19,64% | 88,42 $ | 65,80 $ | 99,36 $ |

## Prossimi step se SOL segue BTC 2022

| Step | Date SOL | BTC fine | SOL zona bassa | SOL zona alta | SOL fine base | Lettura |
| --- | --- | --- | --- | --- | --- | --- |
| Step 1 - prossime 2 settimane | 5 agosto 2026 -> 19 agosto 2026 | +3,41% | 73,78 $ (9 agosto 2026) | 77,49 $ (14 agosto 2026) | 76,43 $ | Laterale / movimento non forte. |
| Step 2 - primo mese | 20 agosto 2026 -> 4 settembre 2026 | +7,28% | 70,57 $ (26 agosto 2026) | 80,31 $ (3 settembre 2026) | 79,29 $ | Prima retest / debolezza, poi recupero. |
| Step 3 - secondo mese | 5 settembre 2026 -> 4 ottobre 2026 | +24,25% | 65,80 $ (23 settembre 2026) | 91,83 $ (4 ottobre 2026) | 91,83 $ | Prima retest / debolezza, poi recupero. |
| Step 4 - terzo mese | 5 ottobre 2026 -> 3 novembre 2026 | +24,56% | 88,46 $ (10 ottobre 2026) | 99,36 $ (28 ottobre 2026) | 92,06 $ | Spinta rialzista abbastanza pulita. |

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
| Prezzo SOL | 73,91 $ |  |
| Weekly RSI | 38,76 / linea grezza 53,42 | LINEA NON AFFIDABILE / RISCHIO NON ATTIVO — IRREALISTICA / NON OPERATIVA |
| Monthly RSI | 40,54 / linea grezza 55,81 | RSI TROPPO BASSO PER RISCHIO TOP — VALIDA / USO PRUDENTE |
| Target ciclo base | 406,61 $ | Avanzamento +18,18% |
| Rischio top-cycle RSI | BASSO | Nessun segnale top-cycle macro attivo. Prezzo ancora lontano dal target ciclo; il filtro RSI resta solo di monitoraggio. |

## Lettura semplice

- Weekly: La top-line weekly non supera i controlli di qualità. Non viene usata per generare rischio top-cycle.
- Monthly: RSI monthly è 40,5, sotto la soglia prudente 55. Anche se fosse vicino alla linea, non è una vera zona di esaurimento ciclo.
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
| Prezzo SOL | 73,91 $ |
| TVL Solana | 4,80 mld $ |
| TVL 7g | +0,44% |
| DEX volume 24h | 1,74 mld $ |
| Fees 24h | 9,96 mln $ |
| Stablecoin su Solana | 16,49 mld $ |
| Stake ratio | 68,78% |
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
| Confronto precedente | 2026-08-03 |
| Fonte prezzi | Yahoo Finance SOL-USD weekly |
| Prezzo SOL | 73,91 $ |
| EMA200 weekly target | 111,99 $ |
| Upside verso EMA200 | +51,55% |
| Distanza prezzo da EMA200 | -34,01% |
| Gap EMA50/EMA200 | -4,81% |
| Stato cross | EMA50 SOTTO EMA200 |
| RSI weekly | 38,75 |
| Età SOL | 6,3 anni |
| Analoghi storici usati | 30 |
| Max analoghi per asset | 3 |
| Hit EMA200 12w analoghi | +20,00% |
| Max gain mediano 12w | +20,86% |
| Drawdown mediano 12w | -22,52% |

Lettura semplice:

**CONTESTO INTERESSANTE, SERVONO CONFERME DI PREZZO**

Autocontrollo: **STABILE / DA CONFERMARE**.

Questo modulo confronta SOL con altre crypto in fasi simili di età, distanza da EMA200, EMA50/EMA200 e RSI. Non usa stock market.

Nota importante: **questo modulo ora NON pesa più nel Global Confluence**. Resta solo come contesto di ciclo e come mappa verso EMA200 weekly. Il punteggio Global resta guidato da prezzo, scanner, regime, struttura tecnica, frattale, RSI e conferme reali.

Nota: se EMA50/EMA200 sono dentro ±2%, il modulo parla di medie sovrapposte / incrocio in corso, perché exchange diversi possono mostrare il cross leggermente prima o dopo.

<!-- Generato: 2026-08-05 05:15 UTC -->
<!-- MAJOR_ALT_LIFECYCLE_SQUEEZE_END -->

</details>
<!-- COMPACT_SECTION_END:major_alt_lifecycle -->

# Report giornaliero BTC / SOL / DOGE

Aggiornato il: **2026-08-05 05:12:23 UTC**

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
- SOL: nessun cambiamento forte rispetto a ieri.
- DOGE: nessun cambiamento forte rispetto a ieri.

| Asset | Cambio | Tono | Verdetto oggi | Casi positivi oggi | Δ casi positivi |
| --- | --- | --- | --- | --- | --- |
| BTC | CAMBIAMENTO MEDIO | peggioramento | RIALZISTA | +80.00% | 0.00 punti |
| SOL | NESSUN CAMBIAMENTO FORTE | miglioramento | RIALZISTA | +72.50% | 0.00 punti |
| DOGE | NESSUN CAMBIAMENTO FORTE | peggioramento | NEUTRALE / INCERTO | +55.00% | -2.50 punti |

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
| BTC | 61.046 $ | 70.684 $ | +27,78% | +15,79% | rimbalzo poco frequente | 70.684 $ | 61.046 $ | +7,69% | -13,64% | spike storicamente più resistente |
| SOL | 70,21 $ | 81,30 $ | +21,43% | +15,79% | rimbalzo poco frequente | 81,30 $ | 70,21 $ | 0,00% | -13,64% | spike storicamente più resistente |
| DOGE | 0,06642 $ | 0,07691 $ | +33,33% | +15,79% | rimbalzo poco frequente | 0,07691 $ | 0,06642 $ | +22,73% | -13,64% | spike storicamente più resistente |

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

- **BTC: su 40 casi simili, 18 prima sono scesi a -5,00%. Tra quei 18, 5 poi sono rimbalzati fino a +10,00%. Percentuale: +27,78% (5/18). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.**
- **BTC: su 40 casi simili, 26 prima sono saliti a +10,00%. Tra quei 26, 2 poi sono scaricati a -5,00%. Percentuale: +7,69% (2/26). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.**
- **SOL: su 40 casi simili, 14 prima sono scesi a -5,00%. Tra quei 14, 3 poi sono rimbalzati fino a +10,00%. Percentuale: +21,43% (3/14). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.**
- **SOL: su 40 casi simili, 24 prima sono saliti a +10,00%. Tra quei 24, 0 poi sono scaricati a -5,00%. Percentuale: 0,00% (0/24). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.**
- **DOGE: su 40 casi simili, 33 prima sono scesi a -5,00%. Tra quei 33, 11 poi sono rimbalzati fino a +10,00%. Percentuale: +33,33% (11/33). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.**
- **DOGE: su 40 casi simili, 22 prima sono saliti a +10,00%. Tra quei 22, 5 poi sono scaricati a -5,00%. Percentuale: +22,73% (5/22). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.**

<!-- BOUNCE_AFTER_DRAWDOWN_END -->

</details>
<!-- COMPACT_SECTION_END:bounce_after_drawdown -->

<!-- COMPACT_SECTION_START:scanner_forecast -->
<details>
<summary><strong>🔭 Cono probabilistico dello scanner</strong></summary>

<!-- SCANNER_FORECAST_TRACKER_START -->
# Scanner forecast path / cono probabilistico

Generato: 2026-08-05 05:14:31 UTC


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
| BTC | 2026-08-05 | 64.258 $ | SALITA | 80,00% | 54.866,26 $ | 66.661,19 $ | 70.663,01 $ | 77.361,89 $ | 90.745,35 $ |
| SOL | 2026-08-05 | 73,91 $ | SALITA | 72,50% | 61,38 $ | 73,36 $ | 80,36 $ | 90,99 $ | 112,10 $ |
| DOGE | 2026-08-05 | 0.06992 $ | INCERTO | 55,00% | 0.05495 $ | 0.06370 $ | 0.07322 $ | 0.08186 $ | 0.09098 $ |

## Grafici

### BTC

![Scanner forecast BTC](scanner_forecast_BTC.png)

#### Verifica storica e discrepanza

![Verifica storica cono BTC](scanner_forecast_history_BTC.png)

- Cono congelato il **2026-07-10**; verificato fino al **2026-08-05**; stato **PARZIALE 26/30g**.
- Reale **64.256,54 $**; p50 previsto **65.558,88 $**; scarto **-1,99%**.
- Errore medio assoluto **3,73%**; massimo **7,75%**; DENTRO p10-p90; DENTRO p25-p75.

### SOL

![Scanner forecast SOL](scanner_forecast_SOL.png)

#### Verifica storica e discrepanza

![Verifica storica cono SOL](scanner_forecast_history_SOL.png)

- Cono congelato il **2026-07-10**; verificato fino al **2026-08-05**; stato **PARZIALE 26/30g**.
- Reale **73,90 $**; p50 previsto **72,92 $**; scarto **1,35%**.
- Errore medio assoluto **2,33%**; massimo **5,38%**; DENTRO p10-p90; DENTRO p25-p75.

### DOGE

![Scanner forecast DOGE](scanner_forecast_DOGE.png)

#### Verifica storica e discrepanza

![Verifica storica cono DOGE](scanner_forecast_history_DOGE.png)

- Cono congelato il **2026-07-10**; verificato fino al **2026-08-05**; stato **PARZIALE 26/30g**.
- Reale **0.06994 $**; p50 previsto **0.06135 $**; scarto **14,00%**.
- Errore medio assoluto **11,07%**; massimo **25,63%**; DENTRO p10-p90; FUORI p25-p75.

## Accuratezza percorso scanner

| Asset   | Giorno   |   Controlli | Dentro p10-p90   | Dentro p25-p75   | Errore medio abs vs p50   | Errore medio vs p50   |
|:--------|:---------|------------:|:-----------------|:-----------------|:--------------------------|:----------------------|
| BTC | 1g | 26 | 100,00% | 61,54% | 1,72% | -0,01% |
| BTC | 3g | 24 | 100,00% | 75,00% | 2,14% | -0,59% |
| BTC | 7g | 20 | 100,00% | 85,00% | 2,47% | 0,92% |
| BTC | 14g | 13 | 100,00% | 76,92% | 2,36% | 1,38% |
| BTC | 30g | 0 | n/a | n/a | n/a | n/a |
| SOL | 1g | 26 | 76,92% | 57,69% | 2,08% | -0,49% |
| SOL | 3g | 24 | 100,00% | 70,83% | 2,33% | -1,02% |
| SOL | 7g | 20 | 100,00% | 90,00% | 2,25% | -0,09% |
| SOL | 14g | 13 | 100,00% | 92,31% | 2,35% | 1,69% |
| SOL | 30g | 0 | n/a | n/a | n/a | n/a |
| DOGE | 1g | 26 | 96,15% | 61,54% | 2,61% | -0,22% |
| DOGE | 3g | 24 | 100,00% | 83,33% | 2,19% | 0,10% |
| DOGE | 7g | 20 | 90,00% | 90,00% | 6,17% | 3,52% |
| DOGE | 14g | 13 | 100,00% | 53,85% | 10,11% | 9,63% |
| DOGE | 30g | 0 | n/a | n/a | n/a | n/a |

## Calibratore shadow

Il cono ufficiale resta grezzo e invariato. Il calibratore usa soltanto previsioni passate già mature, campionate una volta a settimana per ridurre la falsa indipendenza. Ogni orizzonte si attiva a 30 controlli indipendenti: parte al 25% della correzione stimata e cresce gradualmente fino al 100% a 100 controlli.

| Asset   | Orizzonte   |   Controlli indipendenti |   Soglia | Stato                  | Forza correzione   | Shift p50   |   Scala p10-p90 |
|:--------|:------------|-------------------------:|---------:|:-----------------------|:-------------------|:------------|----------------:|
| BTC | 1g | 5 | 30 | RACCOLTA (25 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 3g | 4 | 30 | RACCOLTA (26 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 7g | 4 | 30 | RACCOLTA (26 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 14g | 3 | 30 | RACCOLTA (27 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 30g | 0 | 30 | RACCOLTA (30 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 1g | 5 | 30 | RACCOLTA (25 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 3g | 4 | 30 | RACCOLTA (26 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 7g | 4 | 30 | RACCOLTA (26 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 14g | 3 | 30 | RACCOLTA (27 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 30g | 0 | 30 | RACCOLTA (30 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 1g | 5 | 30 | RACCOLTA (25 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 3g | 4 | 30 | RACCOLTA (26 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 7g | 4 | 30 | RACCOLTA (26 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 14g | 3 | 30 | RACCOLTA (27 mancanti) | 0,0% | 0,00% | 1,000 |
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

Righe salvate nello storico: **72**.

Questa sezione tiene un diario delle previsioni giornaliere a 30 giorni, senza appesantire il report principale.

| Data | Asset | Prezzo | Direzione | Casi positivi | Return p50 | Drawdown p50 | Max gain p50 | Controllo 30g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08-05 | BTC | 64.258 $ | SALITA | 80,00% | 70.663 $ | 61.186 $ | 73.471 $ | 2026-09-04 |
| 2026-08-05 | DOGE | 0,07000 $ | INCERTO | 55,00% | 0,07000 $ | 0,06000 $ | 0,08000 $ | 2026-09-04 |
| 2026-08-05 | SOL | 73,91 $ | SALITA | 72,50% | 80,36 $ | 71,20 $ | 82,87 $ | 2026-09-04 |

<!-- FORECAST_30D_HISTORY_END -->

</details>
<!-- COMPACT_SECTION_END:scanner_forecast -->

<!-- COMPACT_SECTION_START:extreme_cases -->
<details>
<summary><strong>⚠️ Percorso dei casi estremi</strong></summary>

<!-- EXTREME_CASES_PATH_START -->
# Extreme cases path report

Generato: 2026-08-05 05:14 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [extreme_cases_path_report.md](extreme_cases_path_report.md)

Questo report si attiva quando i casi positivi o negativi sono almeno **80%**.

Ora misura anche il **rialzo massimo prima della discesa principale**, quindi distingue uno spike iniziale da una discesa quasi immediata.

## Trigger estremi

| Asset   | Direzione            | Trigger   | Percentuale   | Motivo                           |   Match disponibili |
|:--------|:---------------------|:----------|:--------------|:---------------------------------|--------------------:|
| BTC     | POSITIVO / RIALZISTA | SI        | +80,00%       | Casi positivi 80.00% >= 80%      |                  40 |
| SOL     | NESSUNO              | NO        | +72,50%       | Nessun lato sopra soglia estrema |                  40 |
| DOGE    | NESSUNO              | NO        | +55,00%       | Nessun lato sopra soglia estrema |                  40 |

## BTC — casi rialzisti

- Trigger: **Casi positivi 80.00% >= 80%**
- Casi usati nei grafici: **32**
- Return mediano 7g: **+3,29%**
- Return mediano 14g: **+7,02%**
- Return mediano 30g: **+12,86%**
- Drawdown mediano: **-3,25%**
- Max gain mediano: **+16,27%**

### Quanto salivano prima di scendere

- Spike massimo mediano prima del minimo: **+0,00%**
- Spike massimo medio prima del minimo: **+1,47%**
- Spike p75 prima del minimo: **+1,61%**
- Giorno mediano dello spike: **giorno 0**
- Giorno mediano del minimo: **giorno 3**
- Scarico mediano dal picco al minimo: **-4,75%**
- Casi con almeno +5% prima del minimo: **+9,38%**
- Casi con almeno +10% prima del minimo: **+3,12%**
- Casi con almeno +15% prima del minimo: **+0,00%**
- Discesa quasi immediata: **+65,62%**

Un segnale ribassista a 30 giorni non significa necessariamente discesa immediata: alcuni casi fanno prima uno spike e poi scaricano.

### Distribuzione 30 giorni

| P10    | P25    | P50     | P75     | P90     |
|:-------|:-------|:--------|:--------|:--------|
| +4,45% | +9,46% | +12,86% | +23,13% | +49,39% |

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
| 1INCH-USD       | 2024-10-08 | +86,80%      | +14,18%                  |             12 | -10,73%      |              27 | -21,82%          | +3,24%       | SPIKE PRIMA DEL DUMP    |
| HBAR-USD        | 2020-11-08 | +85,08%      | +8,68%                   |              3 | -0,34%       |              11 | -8,29%           | +20,03%      | ECCEZIONE POSITIVA      |
| BNB-USD         | 2019-01-21 | +85,74%      | +8,17%                   |              6 | -5,78%       |               9 | -12,89%          | +67,34%      | ECCEZIONE POSITIVA      |
| NEO-USD         | 2026-04-09 | +85,53%      | +3,33%                   |              2 | -2,80%       |               3 | -5,94%           | +10,08%      | ECCEZIONE POSITIVA      |
| BTC-USD         | 2026-04-08 | +87,04%      | +2,71%                   |              3 | -0,52%       |               4 | -3,15%           | +12,74%      | DISCESA QUASI IMMEDIATA |
| NEO-USD         | 2019-01-21 | +86,93%      | +2,10%                   |              3 | -9,47%       |              16 | -11,34%          | +21,47%      | ECCEZIONE POSITIVA      |
| OMG-USD         | 2019-01-21 | +87,68%      | +1,65%                   |              1 | -19,94%      |              16 | -21,23%          | +4,30%       | ECCEZIONE POSITIVA      |
| MKR-USD         | 2020-05-16 | +86,49%      | +1,63%                   |              1 | -4,76%       |               5 | -6,29%           | +63,84%      | DISCESA QUASI IMMEDIATA |
| XTZ-USD         | 2026-04-09 | +87,41%      | +1,60%                   |              1 | -3,24%       |               3 | -4,76%           | +9,66%       | DISCESA QUASI IMMEDIATA |
| ETC-USD         | 2019-01-21 | +85,50%      | +1,18%                   |              4 | -12,63%      |              16 | -13,64%          | +9,27%       | ECCEZIONE POSITIVA      |
| BNB-USD         | 2026-04-09 | +87,66%      | +0,76%                   |              2 | -1,76%       |               3 | -2,50%           | +7,78%       | DISCESA QUASI IMMEDIATA |
| EGLD-USD        | 2024-06-13 | +85,14%      | +0,62%                   |              3 | -14,80%      |              10 | -15,32%          | +7,25%       | ECCEZIONE POSITIVA      |
| XTZ-USD         | 2019-01-21 | +87,01%      | +0,44%                   |              2 | -14,08%      |              17 | -14,45%          | +9,53%       | ECCEZIONE POSITIVA      |
| BTC-USD         | 2019-01-20 | +88,53%      | +0,10%                   |              2 | -5,60%       |              18 | -5,69%           | +9,61%       | ECCEZIONE POSITIVA      |
| XLM-USD         | 2020-11-06 | +89,87%      | +0,00%                   |              0 | -5,08%       |               1 | -5,08%           | +109,40%     | DISCESA QUASI IMMEDIATA |
| ETH-USD         | 2026-04-04 | +88,77%      | +0,00%                   |              0 | +0,00%       |               0 | +0,00%           | +13,61%      | DISCESA QUASI IMMEDIATA |
| SAND-USD        | 2023-10-16 | +88,66%      | +0,00%                   |              0 | -3,59%       |               2 | -3,59%           | +50,41%      | DISCESA QUASI IMMEDIATA |
| DOGE-USD        | 2020-11-06 | +88,42%      | +0,00%                   |              0 | -3,26%       |               3 | -3,26%           | +22,75%      | DISCESA QUASI IMMEDIATA |
| FIL-USD         | 2023-10-21 | +88,29%      | +0,00%                   |              0 | +0,00%       |               0 | +0,00%           | +40,20%      | DISCESA QUASI IMMEDIATA |
| ONE-USD         | 2020-05-10 | +88,00%      | +0,00%                   |              0 | -0,35%       |               1 | -0,35%           | +12,97%      | DISCESA QUASI IMMEDIATA |

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
- Prezzo attuale: **64.258,42 $**
- Return normale fra 30 giorni: **70.663,01 $** (9,97%)
- Drawdown normale durante il mese: **61.185,59 $** (-4,78%)
- Drawdown brutto da rispettare: **55.911,67 $** (-12,99%)
- Max gain normale durante il mese: **73.470,66 $** (14,34%)
- Max gain buono / take profit ottimistico: **84.641,16 $** (31,72%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Solana
- Direzione più probabile a 30 giorni: **SALITA**
- Casi positivi / salita storica: **72,50%**
- Casi negativi / discesa storica: **27,50%**
- Quanto è netto il segnale: **forte**
- Prezzo attuale: **73,91 $**
- Return normale fra 30 giorni: **80,36 $** (8,72%)
- Drawdown normale durante il mese: **71,20 $** (-3,67%)
- Drawdown brutto da rispettare: **63,91 $** (-13,53%)
- Max gain normale durante il mese: **82,87 $** (12,12%)
- Max gain buono / take profit ottimistico: **93,44 $** (26,42%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Dogecoin
- Direzione più probabile a 30 giorni: **INCERTO**
- Casi positivi / salita storica: **55,00%**
- Casi negativi / discesa storica: **45,00%**
- Quanto è netto il segnale: **molto debole / quasi pari**
- Prezzo attuale: **0,07 $**
- Return normale fra 30 giorni: **0,07 $** (4,72%)
- Drawdown normale durante il mese: **0,06 $** (-13,85%)
- Drawdown brutto da rispettare: **0,06 $** (-18,67%)
- Max gain normale durante il mese: **0,08 $** (12,20%)
- Max gain buono / take profit ottimistico: **0,09 $** (23,00%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Messaggio del giorno

Il quadro generale oggi è più favorevole. Lo scanner vede più possibilità di salita su più asset.

---

# Mappa semplice asset per asset

# Bitcoin — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟢 VERDE / Favorevole
**Prezzo attuale:** 64.258,42 $

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

- Se va molto male: **54.866,26 $** (-14,62%)
- Se va male: **66.661,19 $** (3,74%)
- Scenario normale: **70.663,01 $** (9,97%)
- Se va bene: **77.361,89 $** (20,39%)
- Se va molto bene: **90.745,35 $** (41,22%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **61.185,59 $** (-4,78%)
- Discesa brutta: **55.911,67 $** (-12,99%)
- Discesa molto brutta: **51.072,38 $** (-20,52%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **73.470,66 $** (14,34%)
- Rialzo buono: **84.641,16 $** (31,72%)
- Rialzo molto forte: **98.134,90 $** (52,72%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Bitcoin tendeva a muoversi tra una zona bassa intorno a **61.185,59 $** e uno spike normale intorno a **73.470,66 $**.

La chiusura a 30 giorni era più spesso positiva: salita 80,00%, discesa 20,00%. Quindi la lettura principale è favorevole.

Nota leva BTC: se la liquidazione è vicina a 51.000 $, guarda soprattutto la discesa brutta e molto brutta. Il prezzo può recuperare dopo, ma la leva può saltare prima.

---

# Solana — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟢 VERDE / Favorevole
**Prezzo attuale:** 73,91 $

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

- Se va molto male: **61,38 $** (-16,95%)
- Se va male: **73,36 $** (-0,75%)
- Scenario normale: **80,36 $** (8,72%)
- Se va bene: **90,99 $** (23,11%)
- Se va molto bene: **112,10 $** (51,67%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **71,20 $** (-3,67%)
- Discesa brutta: **63,91 $** (-13,53%)
- Discesa molto brutta: **55,32 $** (-25,16%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **82,87 $** (12,12%)
- Rialzo buono: **93,44 $** (26,42%)
- Rialzo molto forte: **117,58 $** (59,08%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Solana tendeva a muoversi tra una zona bassa intorno a **71,20 $** e uno spike normale intorno a **82,87 $**.

La chiusura a 30 giorni era più spesso positiva: salita 72,50%, discesa 27,50%. Quindi la lettura principale è favorevole.

---

# Dogecoin — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟡 GIALLO / Incerto
**Prezzo attuale:** 0,07 $

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

- Se va molto male: **0,05 $** (-21,41%)
- Se va male: **0,06 $** (-8,89%)
- Scenario normale: **0,07 $** (4,72%)
- Se va bene: **0,08 $** (17,08%)
- Se va molto bene: **0,09 $** (30,12%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **0,06 $** (-13,85%)
- Discesa brutta: **0,06 $** (-18,67%)
- Discesa molto brutta: **0,05 $** (-28,37%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **0,08 $** (12,20%)
- Rialzo buono: **0,09 $** (23,00%)
- Rialzo molto forte: **0,09 $** (31,53%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Dogecoin tendeva a muoversi tra una zona bassa intorno a **0,06 $** e uno spike normale intorno a **0,08 $**.

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

- Previsioni già controllate: **4**
- Direzione corretta: **0,00%**
- Errore medio dello scenario centrale: **3,20%**
- Zona rischio toccata: **0,00%**
- Zona rialzo media toccata: **0,00%**
- Prezzo finale dentro lo scenario 10%-90%: **100,00%**

### Dogecoin

- Previsioni già controllate: **4**
- Direzione corretta: **100,00%**
- Errore medio dello scenario centrale: **8,07%**
- Zona rischio toccata: **0,00%**
- Zona rialzo media toccata: **0,00%**
- Prezzo finale dentro lo scenario 10%-90%: **100,00%**

### Solana

- Previsioni già controllate: **4**
- Direzione corretta: non ancora calcolabile, perché molti segnali erano neutrali.
- Errore medio dello scenario centrale: **8,43%**
- Zona rischio toccata: **50,00%**
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

Dati ancora insufficienti: previsioni controllate **4** su **30** necessarie.

Per ora si usa solo lo scanner storico grezzo. Quando ci saranno abbastanza previsioni controllate, qui apparirà la lettura autocalibrata.

## Solana

Dati ancora insufficienti: previsioni controllate **4** su **30** necessarie.

Per ora si usa solo lo scanner storico grezzo. Quando ci saranno abbastanza previsioni controllate, qui apparirà la lettura autocalibrata.

## Dogecoin

Dati ancora insufficienti: previsioni controllate **4** su **30** necessarie.

Per ora si usa solo lo scanner storico grezzo. Quando ci saranno abbastanza previsioni controllate, qui apparirà la lettura autocalibrata.

---

# Approfondimento tecnico — Bitcoin (BTC-USD)

## Semaforo: 🟢 VERDE / Favorevole

**Prezzo attuale:** 64.258,42 $

Bitcoin ha un segnale favorevole. La statistica dei casi simili indica più possibilità di salita che di discesa, ma resta comunque una probabilità, non una certezza.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **80,00%**
- Casi negativi dopo 30 giorni: **20,00%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **86,78%**
- Rendimento medio dopo 30 giorni: **13,76%**
- Rendimento centrale dopo 30 giorni: **9,97%**
- Discesa media durante i 30 giorni: **-8,07%**
- Massimo rialzo medio durante i 30 giorni: **25,53%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **73.102,36 $**
- Scenario centrale a 30 giorni: **70.663,01 $**
- Zona di rischio media: **59.075,65 $**
- Zona di rialzo media: **80.663,31 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -14,62% → **54.866,26 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: 3,74% → **66.661,19 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: 9,97% → **70.663,01 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 20,39% → **77.361,89 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 41,22% → **90.745,35 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -20,52% → **51.072,38 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -12,99% → **55.911,67 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -4,78% → **61.185,59 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -1,57% → **63.248,17 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: 0,00% → **64.258,42 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 4,27% → **67.005,26 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 8,90% → **69.974,93 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 14,34% → **73.470,66 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 31,72% → **84.641,16 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 52,72% → **98.134,90 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| XLM-USD         | 2020-07-30   | 2020-11-06 |        89.87 |       109.4  |          -5.08 |         146.09 |
| ETH-USD         | 2025-12-26   | 2026-04-04 |        88.77 |        13.61 |           0    |          17.22 |
| SAND-USD        | 2023-07-09   | 2023-10-16 |        88.66 |        50.41 |          -3.59 |          50.41 |
| BTC-USD         | 2018-10-13   | 2019-01-20 |        88.53 |         9.61 |          -5.6  |           9.61 |
| DOGE-USD        | 2020-07-30   | 2020-11-06 |        88.42 |        22.75 |          -3.26 |          52.32 |
| FIL-USD         | 2023-07-14   | 2023-10-21 |        88.29 |        40.2  |           0    |          56.32 |
| ONE-USD         | 2020-02-01   | 2020-05-10 |        88    |        12.97 |          -0.35 |          15.31 |
| XRP-USD         | 2025-12-26   | 2026-04-04 |        87.87 |         5.81 |           0    |          12.27 |
| ETC-USD         | 2023-07-10   | 2023-10-17 |        87.75 |        28.95 |          -1.01 |          38.89 |
| LTC-USD         | 2023-07-09   | 2023-10-16 |        87.74 |        16.96 |          -4.83 |          18.69 |

---

# Approfondimento tecnico — Solana (SOL-USD)

## Semaforo: 🟢 VERDE / Favorevole

**Prezzo attuale:** 73,91 $

Solana ha un segnale favorevole. La statistica dei casi simili indica più possibilità di salita che di discesa, ma resta comunque una probabilità, non una certezza.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **72,50%**
- Casi negativi dopo 30 giorni: **27,50%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **77,25%**
- Rendimento medio dopo 30 giorni: **13,14%**
- Rendimento centrale dopo 30 giorni: **8,72%**
- Discesa media durante i 30 giorni: **-8,36%**
- Massimo rialzo medio durante i 30 giorni: **23,30%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **83,62 $**
- Scenario centrale a 30 giorni: **80,36 $**
- Zona di rischio media: **67,73 $**
- Zona di rialzo media: **91,13 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -16,95% → **61,38 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -0,75% → **73,36 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: 8,72% → **80,36 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 23,11% → **90,99 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 51,67% → **112,10 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -25,16% → **55,32 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -13,53% → **63,91 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -3,67% → **71,20 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -1,16% → **73,05 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: 0,00% → **73,91 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 0,37% → **74,18 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 4,62% → **77,33 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 12,12% → **82,87 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 26,42% → **93,44 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 59,08% → **117,58 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| ENJ-USD         | 2018-10-14   | 2019-01-21 |        84.23 |        11.62 |         -25.1  |          11.62 |
| WAVES-USD       | 2019-03-18   | 2019-06-25 |        81.26 |       -39.1  |         -40.7  |           0    |
| NEAR-USD        | 2025-12-26   | 2026-04-04 |        80.64 |         0.47 |          -0.75 |          14.11 |
| RUNE-USD        | 2026-01-01   | 2026-04-10 |        80.13 |        51.69 |          -4.54 |          51.69 |
| ADA-USD         | 2023-05-06   | 2023-08-13 |        79.62 |       -15.08 |         -16.46 |           0.37 |
| QTUM-USD        | 2018-10-14   | 2019-01-21 |        79.49 |         6.45 |         -14.45 |           6.45 |
| BNB-USD         | 2025-12-31   | 2026-04-09 |        79.42 |         7.78 |          -1.76 |           7.78 |
| SOL-USD         | 2025-12-29   | 2026-04-07 |        78.99 |         3.22 |          -4.8  |           4.08 |
| KAVA-USD        | 2025-12-31   | 2026-04-09 |        78.9  |        22.73 |          -3.48 |          25.59 |
| DASH-USD        | 2024-05-10   | 2024-08-17 |        78.45 |       -10.37 |         -12.9  |           3.5  |

---

# Approfondimento tecnico — Dogecoin (DOGE-USD)

## Semaforo: 🟡 GIALLO / Incerto

**Prezzo attuale:** 0,07 $

Dogecoin è in una situazione incerta. Lo scanner non vede un vantaggio chiaro né per la salita né per la discesa. In questi casi è meglio non forzare la previsione.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **55,00%**
- Casi negativi dopo 30 giorni: **45,00%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **88,89%**
- Rendimento medio dopo 30 giorni: **4,32%**
- Rendimento centrale dopo 30 giorni: **4,72%**
- Discesa media durante i 30 giorni: **-14,95%**
- Massimo rialzo medio durante i 30 giorni: **15,88%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **0,07 $**
- Scenario centrale a 30 giorni: **0,07 $**
- Zona di rischio media: **0,06 $**
- Zona di rialzo media: **0,08 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -21,41% → **0,05 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -8,89% → **0,06 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: 4,72% → **0,07 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 17,08% → **0,08 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 30,12% → **0,09 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -28,37% → **0,05 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -18,67% → **0,06 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -13,85% → **0,06 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -7,70% → **0,06 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: -2,70% → **0,07 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 0,00% → **0,07 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 3,75% → **0,07 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 12,20% → **0,08 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 23,00% → **0,09 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 31,53% → **0,09 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| ZEC-USD         | 2019-06-11   | 2019-09-18 |        91.79 |       -31.87 |         -33.38 |           0    |
| AVAX-USD        | 2025-09-08   | 2025-12-16 |        91.19 |        11.95 |          -7.37 |          19.38 |
| ADA-USD         | 2019-06-06   | 2019-09-13 |        90.86 |        -9.68 |         -18.07 |          16.48 |
| OP-USD          | 2025-12-27   | 2026-04-05 |        90.27 |        16.75 |          -2.92 |          22.25 |
| VET-USD         | 2022-03-19   | 2022-06-26 |        90.05 |        -4    |         -11.66 |           7.24 |
| DASH-USD        | 2022-03-17   | 2022-06-24 |        89.97 |        -5.39 |         -22.75 |           0.95 |
| WAVES-USD       | 2021-10-08   | 2022-01-15 |        89.95 |       -36.07 |         -42.45 |           0    |
| ETC-USD         | 2022-03-17   | 2022-06-24 |        89.74 |        56.33 |         -15.35 |          59    |
| LTC-USD         | 2018-04-16   | 2018-07-24 |        89.58 |       -35.55 |         -39.52 |           0    |
| SNX-USD         | 2025-09-27   | 2026-01-04 |        89.57 |       -26.52 |         -27.43 |          15.53 |

</details>
<!-- COMPACT_SECTION_END:scanner_full_detail -->

<!-- COMPACT_SECTION_START:market_regime -->
<details>
<summary><strong>🌦️ Market Regime Match</strong></summary>

<!-- MARKET_REGIME_MATCH_START -->
# Market Regime Match Report


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [market_regime_match_report.md](market_regime_match_report.md)

Generated: 2026-08-05 05:15 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | BEAR | 64.258 $ | False | -19.69% | -9.93% | BEAR | -19.69% | -9.93% |
| DOGE-USD | BEAR | 0.06992 $ | False | -35.13% | -16.51% | BEAR | -19.69% | -9.93% |
| SOL-USD | BEAR | 73,91 $ | False | -16.41% | -16.97% | BEAR | -19.69% | -9.93% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 80.00% | 9.97% | 20.39% | 41.22% | -4.78% | -20.52% | 14.34% | 31.72% | 52.72% | 50.00% | 4.07% | 37.04% | 81.05% |
| BTC-USD | SAME_BTC_REGIME | 18 | 88.89% | 9.57% | 10.31% | 15.97% | -4.02% | -16.08% | 11.08% | 16.54% | 46.67% | 33.33% | -11.06% | 13.24% | 44.83% |
| BTC-USD | SAME_ASSET_REGIME | 22 | 90.91% | 9.63% | 13.39% | 39.07% | -3.41% | -14.40% | 12.06% | 34.54% | 50.40% | 45.45% | -4.48% | 36.56% | 76.99% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 18 | 88.89% | 9.57% | 10.31% | 15.97% | -4.02% | -16.08% | 11.08% | 16.54% | 46.67% | 33.33% | -11.06% | 13.24% | 44.83% |
| DOGE-USD | ALL_MATCHES | 40 | 55.00% | 4.72% | 17.08% | 30.12% | -13.85% | -28.37% | 12.20% | 23.00% | 31.53% | 50.00% | 0.31% | 18.71% | 82.99% |
| DOGE-USD | SAME_BTC_REGIME | 26 | 61.54% | 6.69% | 16.60% | 25.62% | -13.85% | -24.29% | 9.47% | 21.62% | 29.78% | 50.00% | 0.31% | 13.88% | 52.16% |
| DOGE-USD | SAME_ASSET_REGIME | 24 | 66.67% | 7.34% | 16.77% | 27.59% | -13.69% | -18.20% | 9.47% | 20.36% | 30.54% | 54.17% | 1.43% | 33.72% | 89.54% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 22 | 63.64% | 6.69% | 15.12% | 17.72% | -13.85% | -18.22% | 8.09% | 17.65% | 23.85% | 50.00% | 0.31% | 12.02% | 60.30% |
| SOL-USD | ALL_MATCHES | 40 | 72.50% | 8.72% | 23.11% | 51.67% | -3.67% | -25.16% | 12.12% | 26.42% | 59.08% | 55.00% | 5.47% | 51.12% | 127.77% |
| SOL-USD | SAME_BTC_REGIME | 17 | 76.47% | 7.22% | 12.74% | 35.88% | -3.86% | -24.56% | 10.72% | 22.40% | 49.67% | 47.06% | -0.20% | 32.48% | 138.27% |
| SOL-USD | SAME_ASSET_REGIME | 27 | 74.07% | 7.60% | 21.32% | 44.78% | -3.86% | -25.33% | 11.62% | 26.24% | 53.54% | 51.85% | 2.39% | 55.46% | 107.36% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 16 | 81.25% | 7.41% | 15.24% | 38.51% | -3.67% | -19.65% | 11.17% | 23.20% | 50.01% | 43.75% | -1.61% | 44.62% | 141.78% |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 18 | 88.89% | 9.57% | -4.02% | 16.54% | 33.33% | -11.06% | 33.43% |
| BTC-USD | HISTORICAL_BTC_BULL | 13 | 69.23% | 16.96% | -5.08% | 50.41% | 61.54% | 28.24% | 69.91% |
| BTC-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 100.00% | 3.24% | -10.73% | 14.18% | 100.00% | 109.39% | 115.00% |
| BTC-USD | HISTORICAL_BTC_MIXED | 6 | 83.33% | 15.94% | -2.63% | 25.96% | 66.67% | 21.48% | 46.11% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 2 | 50.00% | 20.57% | -15.48% | 80.74% | 50.00% | 8.10% | 80.74% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 26 | 61.54% | 6.69% | -13.85% | 21.62% | 50.00% | 0.31% | 56.29% |
| DOGE-USD | HISTORICAL_BTC_BULL | 10 | 50.00% | 3.43% | -10.21% | 29.38% | 50.00% | -0.62% | 58.41% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 4 | 25.00% | -14.40% | -19.80% | 19.71% | 50.00% | 1.68% | 46.07% |
| SOL-USD | HISTORICAL_BTC_BEAR | 17 | 76.47% | 7.22% | -3.86% | 22.40% | 47.06% | -0.20% | 56.14% |
| SOL-USD | HISTORICAL_BTC_BULL | 9 | 44.44% | -10.37% | -12.90% | 56.32% | 44.44% | -7.92% | 69.91% |
| SOL-USD | HISTORICAL_BTC_DISTRIBUTION | 3 | 100.00% | 28.98% | 0.00% | 76.01% | 100.00% | 96.08% | 233.92% |
| SOL-USD | HISTORICAL_BTC_MIXED | 9 | 100.00% | 12.97% | -2.60% | 25.03% | 77.78% | 8.35% | 38.00% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 2 | 0.00% | -26.16% | -27.30% | 1.90% | 0.00% | -29.07% | 1.90% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 22 | 90.91% | 9.63% | -3.41% | 34.54% | 45.45% | -4.48% | 49.87% |
| BTC-USD | HISTORICAL_ASSET_BULL | 9 | 66.67% | 15.05% | -6.13% | 35.54% | 55.56% | 12.03% | 35.54% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 100.00% | 63.84% | -4.76% | 106.37% | 100.00% | 36.55% | 106.37% |
| BTC-USD | HISTORICAL_ASSET_MIXED | 1 | 100.00% | 25.21% | -2.65% | 30.40% | 100.00% | 47.58% | 47.58% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 7 | 57.14% | 12.72% | -4.75% | 20.17% | 42.86% | -0.32% | 28.92% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 24 | 66.67% | 7.34% | -13.69% | 20.36% | 54.17% | 1.43% | 59.76% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 4 | 50.00% | -0.60% | -13.36% | 30.92% | 50.00% | 4.85% | 68.75% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 100.00% | 35.55% | -7.36% | 43.09% | 100.00% | 16.24% | 72.34% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 10 | 20.00% | -12.87% | -22.92% | 18.66% | 30.00% | -11.64% | 27.85% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 27 | 74.07% | 7.60% | -3.86% | 26.24% | 51.85% | 2.39% | 78.03% |
| SOL-USD | HISTORICAL_ASSET_BULL | 2 | 50.00% | 42.91% | -12.23% | 70.27% | 100.00% | 166.06% | 324.13% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 3 | 33.33% | -15.08% | -16.46% | 15.30% | 33.33% | -15.06% | 19.19% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 8 | 87.50% | 12.85% | -2.92% | 25.34% | 62.50% | 5.47% | 44.00% |

## Top regime-adjusted matches

The table below shows the top matches separately for each target, so BTC does not hide SOL and DOGE.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | ETH-USD | 2025-12-26 | 88.77% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 13.61% | 0.00% | 17.22% | -12.28% | -12.28% | 17.22% |
| BTC-USD | BTC-USD | 2018-10-13 | 88.53% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 9.61% | -5.60% | 9.61% | 11.89% | -5.60% | 15.04% |
| BTC-USD | XRP-USD | 2025-12-26 | 87.87% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 5.81% | 0.00% | 12.27% | -8.77% | -8.77% | 12.81% |
| BTC-USD | OMG-USD | 2018-10-14 | 87.68% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 4.30% | -19.94% | 4.30% | 30.65% | -19.94% | 30.65% |
| BTC-USD | BNB-USD | 2025-12-31 | 87.66% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 7.78% | -1.76% | 7.78% | -0.20% | -5.10% | 19.09% |
| BTC-USD | XTZ-USD | 2025-12-31 | 87.41% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 9.66% | -3.24% | 11.77% | -30.35% | -31.31% | 13.59% |
| BTC-USD | SOL-USD | 2025-12-29 | 87.28% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 3.22% | -4.80% | 4.08% | -27.39% | -27.39% | 13.66% |
| BTC-USD | BTC-USD | 2025-12-30 | 87.04% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 12.74% | -0.52% | 14.49% | -11.08% | -14.42% | 15.49% |
| BTC-USD | XTZ-USD | 2018-10-14 | 87.01% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 9.53% | -14.08% | 9.53% | 77.90% | -14.08% | 96.71% |
| BTC-USD | NEO-USD | 2018-10-14 | 86.93% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 21.47% | -9.47% | 21.47% | 21.84% | -9.47% | 34.36% |
| DOGE-USD | OP-USD | 2025-12-27 | 90.27% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 16.75% | -2.92% | 22.25% | 1.62% | -2.92% | 56.55% |
| DOGE-USD | VET-USD | 2022-03-19 | 90.05% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -4.00% | -11.66% | 7.24% | 10.13% | -11.66% | 37.50% |
| DOGE-USD | DASH-USD | 2022-03-17 | 89.97% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -5.39% | -22.75% | 0.95% | -6.32% | -22.75% | 9.96% |
| DOGE-USD | ETC-USD | 2022-03-17 | 89.74% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 56.33% | -15.35% | 59.00% | 109.41% | -15.35% | 165.75% |
| DOGE-USD | LTC-USD | 2018-04-16 | 89.58% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -35.55% | -39.52% | 0.00% | -32.31% | -42.14% | 0.00% |
| DOGE-USD | NEO-USD | 2022-03-17 | 89.28% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 6.51% | -16.44% | 8.94% | 2.89% | -16.44% | 24.41% |
| DOGE-USD | XTZ-USD | 2025-12-31 | 89.20% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 9.66% | -3.24% | 11.77% | -30.35% | -31.31% | 13.59% |
| DOGE-USD | MKR-USD | 2022-10-04 | 89.17% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 11.99% | -0.27% | 24.02% | 41.98% | -0.27% | 48.95% |
| DOGE-USD | ADA-USD | 2022-03-17 | 89.16% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 2.92% | -16.28% | 3.63% | -6.81% | -16.28% | 14.25% |
| DOGE-USD | BAT-USD | 2018-10-14 | 88.95% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 16.84% | -13.62% | 17.16% | 62.34% | -13.62% | 69.37% |
| SOL-USD | ENJ-USD | 2018-10-14 | 84.23% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 11.62% | -25.10% | 11.62% | 465.84% | -25.10% | 542.51% |
| SOL-USD | NEAR-USD | 2025-12-26 | 80.64% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 0.47% | -0.75% | 14.11% | 124.27% | -0.75% | 124.27% |
| SOL-USD | RUNE-USD | 2026-01-01 | 80.13% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 51.69% | -4.54% | 51.69% | -3.02% | -20.45% | 56.14% |
| SOL-USD | QTUM-USD | 2018-10-14 | 79.49% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 6.45% | -14.45% | 6.45% | 24.60% | -14.45% | 33.28% |
| SOL-USD | BNB-USD | 2025-12-31 | 79.42% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 7.78% | -1.76% | 7.78% | -0.20% | -5.10% | 19.09% |
| SOL-USD | SOL-USD | 2025-12-29 | 78.99% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 3.22% | -4.80% | 4.08% | -27.39% | -27.39% | 13.66% |
| SOL-USD | KAVA-USD | 2025-12-31 | 78.90% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 22.73% | -3.48% | 25.59% | -18.69% | -20.93% | 27.22% |
| SOL-USD | EOS-USD | 2018-10-24 | 77.73% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 51.66% | 0.00% | 83.90% | 81.05% | 0.00% | 86.15% |
| SOL-USD | LINK-USD | 2025-12-26 | 76.82% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 7.60% | 0.00% | 10.72% | -4.12% | -4.12% | 23.23% |
| SOL-USD | BTC-USD | 2025-12-30 | 76.66% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 12.74% | -0.52% | 14.49% | -11.08% | -14.42% | 15.49% |

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

Generato: 2026-08-05 05:15 UTC


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
| BTC | 64.258 $ | -1 | NEUTRALE / MISTO | STAGE 4 / MARKDOWN | COMPRESSIONE / TRIANGOLO POSSIBILE | ACCUMULO POSSIBILE / RANGE BASSO | BASSO | RIDUCI RISCHIO / NO LONG A LEVA |
| SOL | 73,91 $ | -7 | RIBASSISTA / FRAGILE | STAGE 4 / MARKDOWN | MASSIMI E MINIMI DECRESCENTI | ACCUMULO POSSIBILE / RANGE BASSO | BASSO | NON INSEGUIRE / TAKE PROFIT SU SPIKE |
| DOGE | 0.06992 $ | -2 | DEBOLE / NON CONFERMATO | STAGE 4 / MARKDOWN | VOLATILITÀ IN ESPANSIONE | SPRING / TEST POSSIBILE | BASSO | NO LONG / SHORT SOLO DOPO SPIKE E REJECTION |

## Punteggi per area

| Asset | Trend | Struttura | Momentum | Volume | Prezzo | Candela | Wyckoff | Totale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | -4 | 0 | +1 | +2 | 0 | 0 | 0 | -1 |
| SOL | -4 | -2 | 0 | -1 | 0 | 0 | 0 | -7 |
| DOGE | -4 | 0 | +2 | -1 | 0 | 0 | +1 | -2 |

## Livelli tecnici

| Asset | Supporto | Resistenza | Breakout 60g | Breakdown 60g | ATR14 | Rendimento 30g | Rendimento 90g |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 62.201 $ | 64.598 $ | 73.970 $ | 57.748 $ | 2,30% | 1,12% | -21,09% |
| SOL | 73,47 $ | 74,89 $ | 83,81 $ | 60,41 $ | 2,95% | -9,24% | -17,10% |
| DOGE | 0.06961 $ | 0.07377 $ | 0.10134 $ | 0.06797 $ | 3,20% | -10,03% | -37,79% |

## Lettura dettagliata

### BTC

- Prezzo: **64.258 $**
- Score classico: **-1 / 12**
- Verdetto: **NEUTRALE / MISTO**
- Azione coerente: **RIDUCI RISCHIO / NO LONG A LEVA**
- Volatilità tecnica locale: **BASSO** — ATR14 2,30%; distanza supporto 3,30%; distanza resistenza 0,53%

Dettaglio:

- Trend: **-4** — prezzo sotto MA200 daily; MA200 daily in discesa; STAGE 4 / MARKDOWN
- Stage weekly: **STAGE 4 / MARKDOWN** — Prezzo sotto MA30 weekly con MA30 in discesa.
- Struttura: **0** — COMPRESSIONE / TRIANGOLO POSSIBILE
- Momentum: **+1** — RSI sano 51.5; MACD sotto signal; istogramma MACD in miglioramento
- Volume: **+2** — OBV sopra media; CMF positivo 0.11; volume ratio 0.99
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **0** — ACCUMULO POSSIBILE / RANGE BASSO. Prezzo nella metà bassa del range, ma senza spring confermato.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 51.48 |
| MACD histogram | -122.43450 |
| CMF20 | 0.112 |
| Volume ratio 20 | 0.99 |
| MA20 | 64.341 $ |
| MA50 | 63.266 $ |
| MA100 | 68.469 $ |
| MA200 | 70.808 $ |
| Pendenza MA50 20g | -1,32% |
| Pendenza MA200 60g | -10,12% |
| Bollinger width | 6,10% |
| Bollinger position | 0.48 |

### SOL

- Prezzo: **73,91 $**
- Score classico: **-7 / 12**
- Verdetto: **RIBASSISTA / FRAGILE**
- Azione coerente: **NON INSEGUIRE / TAKE PROFIT SU SPIKE**
- Volatilità tecnica locale: **BASSO** — ATR14 2,95%; distanza supporto 0,59%; distanza resistenza 1,34%

Dettaglio:

- Trend: **-4** — prezzo sotto MA200 daily; medie daily allineate ribassiste; MA200 daily in discesa; STAGE 4 / MARKDOWN
- Stage weekly: **STAGE 4 / MARKDOWN** — Prezzo sotto MA30 weekly con MA30 in discesa.
- Struttura: **-2** — MASSIMI E MINIMI DECRESCENTI
- Momentum: **0** — RSI neutrale 46.7; MACD sotto signal; istogramma MACD in miglioramento
- Volume: **-1** — OBV sotto media; CMF neutrale 0.04; volume ratio 1.03
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **0** — ACCUMULO POSSIBILE / RANGE BASSO. Prezzo nella metà bassa del range, ma senza spring confermato.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 46.68 |
| MACD histogram | -0.21037 |
| CMF20 | 0.043 |
| Volume ratio 20 | 1.03 |
| MA20 | 74,90 $ |
| MA50 | 75,02 $ |
| MA100 | 78,11 $ |
| MA200 | 85,01 $ |
| Pendenza MA50 20g | +1,54% |
| Pendenza MA200 60g | -17,29% |
| Bollinger width | 9,46% |
| Bollinger position | 0.36 |

### DOGE

- Prezzo: **0.06992 $**
- Score classico: **-2 / 12**
- Verdetto: **DEBOLE / NON CONFERMATO**
- Azione coerente: **NO LONG / SHORT SOLO DOPO SPIKE E REJECTION**
- Volatilità tecnica locale: **BASSO** — ATR14 3,20%; distanza supporto 0,47%; distanza resistenza 5,47%

Dettaglio:

- Trend: **-4** — prezzo sotto MA200 daily; medie daily allineate ribassiste; MA50 daily in discesa; MA200 daily in discesa; STAGE 4 / MARKDOWN
- Stage weekly: **STAGE 4 / MARKDOWN** — Prezzo sotto MA30 weekly con MA30 in discesa.
- Struttura: **0** — VOLATILITÀ IN ESPANSIONE
- Momentum: **+2** — RSI neutrale 41.9; MACD sopra signal; istogramma MACD in miglioramento
- Volume: **-1** — OBV sotto media; CMF neutrale 0.03; volume ratio 0.77
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **+1** — SPRING / TEST POSSIBILE. Ha bucato un minimo importante e ha recuperato: possibile spring, da confermare.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 41.88 |
| MACD histogram | 0.00020 |
| CMF20 | 0.032 |
| Volume ratio 20 | 0.77 |
| MA20 | 0.07113 $ |
| MA50 | 0.07448 $ |
| MA100 | 0.08755 $ |
| MA200 | 0.09354 $ |
| Pendenza MA50 20g | -9,49% |
| Pendenza MA200 60g | -16,81% |
| Bollinger width | 8,17% |
| Bollinger position | 0.29 |

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

Generato: 2026-08-05 05:15 UTC


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
| BTC | 64.258 $ | Doppio massimo | CANDIDATO | ribassista | n/a | 48.247 $ | n/a | 11,27% | Fib 23,6% TESTATO (0) @ 64.748 $ | NEL RANGE | 62.553 $ |
| SOL | 73,91 $ | Doppio massimo | CANDIDATO | ribassista | n/a | 50,11 $ | n/a | 14,73% | Fib 23,6% TESTATO (0) @ 74,40 $ | NEL RANGE | 73,40 $ |
| DOGE | 0.06992 $ | Adam and Eve Top | CANDIDATO | ribassista | n/a | 0.05735 $ | n/a | 2,38% | Fib 23,6% NON ATTIVO (0) @ 0.08008 $ | NEL RANGE | 0.06961 $ |

## BTC

![Classic visual BTC](classic_visual_BTC.png)

- Pattern principale: **Doppio massimo**
- Stato pattern: **CANDIDATO** (0)
- Famiglia: **ribassista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-06-15 -> 2026-07-21**
- Età formazione: **15 giorni**
- Breakout pattern: **n/a**
- Età breakout: **n/a**
- Neckline: **57.748 $**
- Target teorico: **48.247 $**
- Progresso verso target: **n/a**
- Distanza dalla neckline: **11,27%**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 23,6% TESTATO (0) @ 64.748 $** — Swing UP 2026-07-01 57.748 -> 2026-07-21 66.910; livello più vicino 23.6% a 64.748; stato TESTATO; confluenza: nessuna confluenza indipendente.
- Invalidazione: **58.903 $**
- Relazione prezzo/neckline: **sopra neckline**
- Dettaglio: Due massimi simili vicino a 67.248 tra 2026-06-15 e 2026-07-21. Neckline ribassista stimata: 57.748. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 15 giorni. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **NEL RANGE**
- Supporto: **62.553 $**
- Resistenza: **65.508 $**
- Breakout 60g: **73.970 $**
- Breakdown 60g: **57.748 $**
- RSI14: **51.49**
- ATR14: **2,30%**
- Volume ratio 20g: **0.99**
- Rendimento 30g: **+1,12%**
- Rendimento 90g: **-21,09%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Doppio massimo | CANDIDATO | 0 | ribassista | 57.748 $ | n/a | n/a | 48.247 $ | n/a | 11,27% | 58.903 $ | Due massimi simili a 67.248 $ e 66.910 $. Neckline circa 57.748 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 15 giorni. |
| Doppio minimo | CANDIDATO | 0 | rialzista | 67.248 $ | n/a | n/a | 76.748 $ | n/a | 4,65% | 65.903 $ | Due minimi simili a 59.109 $ e 57.748 $. Neckline circa 67.248 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 35 giorni. |

## SOL

![Classic visual SOL](classic_visual_SOL.png)

- Pattern principale: **Doppio massimo**
- Stato pattern: **CANDIDATO** (0)
- Famiglia: **ribassista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-06-15 -> 2026-07-21**
- Età formazione: **15 giorni**
- Breakout pattern: **n/a**
- Età breakout: **n/a**
- Neckline: **64,42 $**
- Target teorico: **50,11 $**
- Progresso verso target: **n/a**
- Distanza dalla neckline: **14,73%**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 23,6% TESTATO (0) @ 74,40 $** — Swing UP 2026-06-06 60,41 -> 2026-07-21 78,73; livello più vicino 23.6% a 74,40; stato TESTATO; confluenza: supporto tecnico.
- Invalidazione: **65,71 $**
- Relazione prezzo/neckline: **sopra neckline**
- Dettaglio: Due massimi simili vicino a 78,73 tra 2026-06-15 e 2026-07-21. Neckline ribassista stimata: 64,42. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 15 giorni. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **NEL RANGE**
- Supporto: **73,40 $**
- Resistenza: **74,89 $**
- Breakout 60g: **83,81 $**
- Breakdown 60g: **60,41 $**
- RSI14: **46.71**
- ATR14: **2,95%**
- Volume ratio 20g: **1.03**
- Rendimento 30g: **-9,23%**
- Rendimento 90g: **-17,09%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Doppio massimo | CANDIDATO | 0 | ribassista | 64,42 $ | n/a | n/a | 50,11 $ | n/a | 14,73% | 65,71 $ | Due massimi simili a 75,94 $ e 78,73 $. Neckline circa 64,42 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 15 giorni. |
| Testa e spalle inverso | CANDIDATO | 0 | rialzista | 79,35 $ | n/a | n/a | 94,28 $ | n/a | 7,36% | 77,76 $ | Spalla sinistra 67,92 $, testa 64,42 $, spalla destra 73,40 $. Neckline circa 79,35 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 19 giorni. |
| Doppio minimo | CANDIDATO | 0 | rialzista | 98,27 $ | n/a | n/a | 114,91 $ | n/a | 32,95% | 96,30 $ | Due minimi simili a 81,63 $ e 81,69 $. Neckline circa 98,27 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 74 giorni. |
| Testa e spalle | TARGET RAGGIUNTO | 0 | ribassista | 82,57 $ | 2026-05-28 | 69g | 66,88 $ | 55,19% | n/a | 84,22 $ | Spalla sinistra 88,05 $, testa 98,27 $, spalla destra 87,79 $. Neckline circa 82,57 $. Breakout neckline: 2026-05-28 (69 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 66,88 $; progresso: 55,19%; prezzo sotto neckline. |

## DOGE

![Classic visual DOGE](classic_visual_DOGE.png)

- Pattern principale: **Adam and Eve Top**
- Stato pattern: **CANDIDATO** (0)
- Famiglia: **ribassista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-07-04 -> 2026-07-26**
- Età formazione: **10 giorni**
- Breakout pattern: **n/a**
- Età breakout: **n/a**
- Neckline: **0.06829 $**
- Target teorico: **0.05735 $**
- Progresso verso target: **n/a**
- Distanza dalla neckline: **2,38%**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 23,6% NON ATTIVO (0) @ 0.08008 $** — Swing DOWN 2026-05-14 0.11825 -> 2026-07-24 0.06829; livello più vicino 23.6% a 0.08008; stato NON ATTIVO; confluenza: neckline rialzista.
- Invalidazione: **0.06966 $**
- Relazione prezzo/neckline: **sopra neckline**
- Dettaglio: Pattern Adam and Eve Top vicino a 0.07923 dal 2026-07-04 al 2026-07-26. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 0.06829. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 10 giorni. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **NEL RANGE**
- Supporto: **0.06961 $**
- Resistenza: **0.07380 $**
- Breakout 60g: **0.10134 $**
- Breakdown 60g: **0.06797 $**
- RSI14: **41.82**
- ATR14: **3,20%**
- Volume ratio 20g: **0.77**
- Rendimento 30g: **-10,05%**
- Rendimento 90g: **-37,81%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Adam and Eve Top | CANDIDATO | 0 | ribassista | 0.06829 $ | n/a | n/a | 0.05735 $ | n/a | 2,38% | 0.06966 $ | Pattern Adam and Eve Top vicino a 0.07923 dal 2026-07-04 al 2026-07-26. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 0.06829. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 10 giorni. Fonte lifecycle: technical_structure_metrics.csv. |
| Doppio massimo | MATURO | -1 | ribassista | 0.07809 $ | 2026-06-24 | 42g | 0.06035 $ | 46,08% | n/a | 0.07966 $ | Due massimi simili a 0.09584 $ e 0.09169 $. Neckline circa 0.07809 $. Breakout neckline: 2026-06-24 (42 giorni fa). Stato: MATURO. Target teorico: 0.06035 $; progresso: 46,08%; prezzo sotto neckline. |
| Triangolo discendente possibile | CANDIDATO | 0 | ribassista | n/a | n/a | n/a | n/a | n/a | n/a | n/a | Massimi decrescenti e supporto quasi piatto. Stato: CANDIDATO; il pattern non ha una neckline univoca da usare per il lifecycle. |
| Doppio minimo | CANDIDATO | 0 | rialzista | 0.07923 $ | n/a | n/a | 0.09017 $ | n/a | 13,32% | 0.07765 $ | Due minimi simili a 0.06961 $ e 0.06829 $. Neckline circa 0.07923 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 12 giorni. |

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

Generato: 2026-08-05 05:15 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [fractal_path_tracker.md](fractal_path_tracker.md)

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-08-05**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-01-20**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **73,91 $**
- Verdetto principale: **ANALOGIA DEBOLE / SCENARIO SECONDARIO**
- Somiglianza strutturale: **+56,86%**
- Aderenza live principale: **+70,03%**
- Errore medio live principale: **14,99%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE SOLO DI CONTESTO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **60**
- Osservazioni inclusive dal bottom: **61**
- Osservazioni da inizio programma/scanner: **34**
- Errore assoluto medio dal bottom: **11,02%**
- Errore assoluto medio da inizio programma: **14,99%**
- Gap firmato medio ultimi 7 giorni: **-12,25%**
- Errore assoluto medio ultimi 7 giorni: **12,25%**
- Gap ultimo giorno: **-17,26%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **-17,26%**
- Gap firmato medio 7g: **-12,25%**
- Errore assoluto medio 7g: **12,25%**
- Variazione recente gap: **-5,37%**
- Stato gap: **IN DEVIAZIONE SOTTO IL FRATTALE**
- Trend gap: **SOL si sta allontanando sotto il percorso ancorato**

Soglie operative del grafico:

- entro **±5%**: percorso vicino;
- tra **±5% e ±12%**: deviazione gestibile;
- oltre **±12%**: frattale non abbastanza aderente per conferma operativa;
- oltre **±18%**: disallineamento marcato.

## Ultimi giorni del confronto ancorato

|   Giorno | Data SOL   | Data BTC eq.   | SOL reale   | Percorso ancorato   | Gap firmato   | Fase                |
|---------:|:-----------|:---------------|:------------|:--------------------|:--------------|:--------------------|
| 51 | 2026-07-27 | 2023-01-11 | 74,14 $ | 70,65 $ | +4,94% | da inizio programma |
| 52 | 2026-07-28 | 2023-01-12 | 73,70 $ | 74,33 $ | -0,85% | da inizio programma |
| 53 | 2026-07-29 | 2023-01-13 | 73,60 $ | 78,43 $ | -6,16% | da inizio programma |
| 54 | 2026-07-30 | 2023-01-14 | 74,47 $ | 82,63 $ | -9,88% | da inizio programma |
| 55 | 2026-07-31 | 2023-01-15 | 72,79 $ | 82,25 $ | -11,51% | da inizio programma |
| 56 | 2026-08-01 | 2023-01-16 | 71,87 $ | 83,39 $ | -13,82% | da inizio programma |
| 57 | 2026-08-02 | 2023-01-17 | 73,45 $ | 83,36 $ | -11,89% | da inizio programma |
| 58 | 2026-08-03 | 2023-01-18 | 73,47 $ | 81,50 $ | -9,85% | da inizio programma |
| 59 | 2026-08-04 | 2023-01-19 | 73,47 $ | 83,07 $ | -11,55% | da inizio programma |
| 60 | 2026-08-05 | 2023-01-20 | 73,91 $ | 89,33 $ | -17,26% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-08-12 | 90,91 $ | 75,22 $ | 73,78 $ / 75,35 $ | no | n/a | n/a | n/a |
| 14g | 2026-08-19 | 92,37 $ | 76,43 $ | 73,78 $ / 77,49 $ | no | n/a | n/a | n/a |
| 21g | 2026-08-26 | 85,29 $ | 70,57 $ | 70,57 $ / 77,49 $ | no | n/a | n/a | n/a |
| 28g | 2026-09-02 | 96,77 $ | 80,07 $ | 70,57 $ / 80,07 $ | no | n/a | n/a | n/a |
| 35g | 2026-09-09 | 91,38 $ | 75,61 $ | 70,57 $ / 80,93 $ | no | n/a | n/a | n/a |
| 42g | 2026-09-16 | 88,09 $ | 72,89 $ | 70,57 $ / 80,93 $ | no | n/a | n/a | n/a |
| 49g | 2026-09-23 | 79,52 $ | 65,80 $ | 65,80 $ / 80,93 $ | no | n/a | n/a | n/a |
| 56g | 2026-09-30 | 108,03 $ | 89,38 $ | 65,80 $ / 89,38 $ | no | n/a | n/a | n/a |
| 63g | 2026-10-07 | 108,30 $ | 89,61 $ | 65,80 $ / 92,35 $ | no | n/a | n/a | n/a |
| 70g | 2026-10-14 | 112,18 $ | 92,82 $ | 65,80 $ / 92,82 $ | no | n/a | n/a | n/a |
| 77g | 2026-10-21 | 110,01 $ | 91,02 $ | 65,80 $ / 92,82 $ | no | n/a | n/a | n/a |
| 84g | 2026-10-28 | 120,09 $ | 99,36 $ | 65,80 $ / 99,36 $ | no | n/a | n/a | n/a |
| 91g | 2026-11-04 | 107,45 $ | 88,90 $ | 65,80 $ / 99,36 $ | no | n/a | n/a | n/a |
| 98g | 2026-11-11 | 115,58 $ | 95,63 $ | 65,80 $ / 99,36 $ | no | n/a | n/a | n/a |
| 105g | 2026-11-18 | 116,34 $ | 96,26 $ | 65,80 $ / 99,36 $ | no | n/a | n/a | n/a |
| 112g | 2026-11-25 | 105,59 $ | 87,37 $ | 65,80 $ / 99,36 $ | no | n/a | n/a | n/a |
| 119g | 2026-12-02 | 105,93 $ | 87,64 $ | 65,80 $ / 99,36 $ | no | n/a | n/a | n/a |
| 126g | 2026-12-09 | 105,25 $ | 87,09 $ | 65,80 $ / 99,36 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 22 | 27,27% | 8,70% | 11,97% |
| 14g | 15 | 6,67% | 15,82% | 9,91% |
| 21g | 8 | 0,00% | 24,80% | 12,65% |
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

Ultima lettura salvata: **2026-08-05** — SOL 73,91 $, gap -17,26%, somiglianza +56,86%.

Nel report principale lascio solo il link, così non diventa troppo lungo.

<!-- SOL_BTC_FRACTAL_HISTORY_END -->

</details>
<!-- COMPACT_SECTION_END:fractal_path -->

<!-- COMPACT_SECTION_START:exchange_microstructure -->
<details>
<summary><strong>🏦 Dati exchange, liquidità e leva</strong></summary>

<!-- EXCHANGE_MICROSTRUCTURE_START -->
# Dati exchange, liquidità e leva

Generato: 2026-08-05 05:15 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [exchange_microstructure_report.md](exchange_microstructure_report.md)

Questo modulo legge Kraken Futures, Bitget Futures e KuCoin Futures come nucleo derivati. OKX e Coinbase vengono raccolti come fonti ausiliarie non pesate.
Non modifica la formula matematica di RSI, Fibonacci o Wyckoff: controlla se quei segnali sono sostenuti da acquisti, vendite, OI, funding e liquidità.

**Limite importante:** questo nucleo non assume disponibile un feed pubblico completo delle liquidazioni. La componente liquidazioni resta neutrale; le zone future restano stime di pressione, non dati certi delle singole posizioni.

Diagnostica completa: [exchange_source_diagnostics.md](exchange_source_diagnostics.md)

## Sintesi

| Asset | Prezzo | Exchange | Segnale candidato | Peso Global | Bias exchange | Confidenza | Copertura | Funding 8h eq. | OI 24h | Taker flow (campione/4h) | Book 0,5% | Liq long campione | Liq short campione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 64.294 $ | 3 | 0 | 0 | LEGGERMENTE POSITIVA / NON PESATA | MEDIA | 100% | +0,0009% | +3,99% | 1,64 | +3,61% | 0 $ | 0 $ |
| SOL | 74,03 $ | 3 | 0 | 0 | LEGGERMENTE POSITIVA / NON PESATA | MEDIA | 100% | +0,0042% | -1,99% | 3,59 | -0,08% | 0 $ | 0 $ |
| DOGE | 0.06998 $ | 3 | 0 | 0 | LEGGERMENTE POSITIVA / NON PESATA | MEDIA | 100% | +0,0099% | +2,51% | 1,29 | -5,11% | 0 $ | 0 $ |

Il segnale candidato è limitato a **±1**, ma il peso nel Global resta **0** finché il tracker a 7 giorni non raggiunge 30 controlli, almeno 55% di accuratezza e return corretto direzione positivo. Un singolo muro o funding non basta.

La colonna taker usa un campione recente nel primo run. Dopo almeno 3 fotografie distribuite su almeno 45 minuti viene sostituita automaticamente dalla media intraday 4h.

## Dati separati per exchange

| Asset | Exchange | Stato | Funding 8h eq. | Open interest | Taker flow | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | Kraken | OK | -0,0001% | 150,33 mln $ | 2,67 | +7,50% |
| BTC | Bitget | OK | -0,0014% | 2,35 mld $ | 0,93 | +8,18% |
| BTC | Kucoin | OK | -0,0002% | 1,36 mld $ | 2,01 | +5,02% |
| SOL | Kraken | OK | -0,0079% | 17,25 mln $ | 1,52 | -2,44% |
| SOL | Bitget | OK | -0,0008% | 349,46 mln $ | 23,54 | -3,89% |
| SOL | Kucoin | OK | +0,0002% | 193,34 mln $ | 0,71 | +2,66% |
| DOGE | Kraken | OK | -0,0095% | 4,06 mln $ | 0,55 | -3,16% |
| DOGE | Bitget | OK | +0,0100% | 97,68 mln $ | 2,16 | -7,76% |
| DOGE | Kucoin | OK | +0,0100% | 98,21 mln $ | 1,27 | -14,29% |

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

- Score grezzo exchange: **+2,25**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 1, accuratezza +0,00%.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 1, bear 0, divergenze 0.
- Flusso taker/order book: **+1,75**.
- OI/funding/basis: **+0,00**.
- Affollamento long/short: **+0,00**.
- Liquidazioni: **NON PESATE / FEED COMPLETO NON ASSUNTO DISPONIBILE**.
- **Wyckoff:** Markdown non pienamente confermato: compare assorbimento compratore.
- **Fibonacci:** Livello Fibonacci soltanto testato: order book e taker flow non bastano ancora per dichiararlo tenuto o perso. Confluenza tecnica dichiarata: supporto tecnico.
- **RSI:** RSI in zona non estrema o flusso exchange non abbastanza netto.
- **Pattern:** I pattern candidati restano non operativi: i dati exchange possono solo preparare la conferma.
- **Breakout/breakdown:** Supporto vicino con assorbimento/acquisti: tenuta più credibile.
- **Mappa liquidità attuale:** muro bid: n/a; muro ask: n/a

![Microstruttura exchange SOL](exchange_microstructure_SOL.png)

### DOGE

- Score grezzo exchange: **+2,12**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 2, accuratezza +100,00%.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 1, bear 2, divergenze 0.
- Flusso taker/order book: **+1,75**.
- OI/funding/basis: **+0,00**.
- Affollamento long/short: **+0,00**.
- Liquidazioni: **NON PESATE / FEED COMPLETO NON ASSUNTO DISPONIBILE**.
- **Wyckoff:** Possibile accumulazione/spring sostenuto da pressione compratrice o assorbimento.
- **Fibonacci:** Fibonacci non_attivo; nessuna conferma exchange netta. Confluenza tecnica dichiarata: neckline rialzista.
- **RSI:** RSI in zona non estrema o flusso exchange non abbastanza netto.
- **Pattern:** I pattern candidati restano non operativi: i dati exchange possono solo preparare la conferma.
- **Breakout/breakdown:** Prezzo non abbastanza vicino a un livello chiave o flusso non netto.
- **Mappa liquidità attuale:** muro bid: n/a; muro ask: n/a

![Microstruttura exchange DOGE](exchange_microstructure_DOGE.png)

## Overlay sulle previsioni a 30 giorni

La previsione storica grezza dello scanner resta intatta. L'overlay exchange può correggerla solo dopo almeno 30 controlli maturati a 30 giorni e solo se il modulo dimostra accuratezza direzionale almeno del 55%.

| Asset | Prob. grezza salita | Return p50 grezzo | Controlli 30g | Accuratezza exchange | Stato overlay | Peso | Prob. corretta | Return corretto |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +80,00% | +9,97% | 0 | n/a | RACCOLTA DATI | 0,00 | +80,00% | +9,97% |
| SOL | +72,50% | +8,72% | 0 | n/a | RACCOLTA DATI | 0,00 | +72,50% | +8,72% |
| DOGE | +55,00% | +4,72% | 0 | n/a | RACCOLTA DATI | 0,00 | +55,00% | +4,72% |

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

Generato: 2026-08-05 05:15 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [exchange_signal_tracker_report.md](exchange_signal_tracker_report.md)

Questo tracker verifica se il segnale candidato exchange ±1 anticipa correttamente la direzione del prezzo a 1/3/7/14/30 giorni.
Il peso Global resta 0 finché l'orizzonte 7g non ha almeno 30 controlli, accuratezza almeno 55% e return corretto direzione positivo. L'overlay a 30g ha un gate separato.

Controlli maturati completati in questa esecuzione: **12**.

## Ultime fotografie giornaliere

| Data | Asset | Prezzo | Versione | Calibrazione | Candidato | Peso Global | Score raw | Confidenza | Taker 4h | OI 24h | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08-05 | BTC | 64.293,70 | V2.1.3 | OK | 0 | 0 | 2,12 | MEDIA | 1,64 | +3,99% | +3,61% |
| 2026-08-05 | DOGE | 0.06998 | V2.1.3 | OK | 0 | 0 | 2,12 | MEDIA | 1,29 | +2,51% | -5,11% |
| 2026-08-05 | SOL | 74,03 | V2.1.3 | OK | 0 | 0 | 2,25 | MEDIA | 3,59 | -1,99% | -0,08% |
| 2026-08-04 | BTC | 63.909,20 | V2.1.3 | OK | 0 | 0 | -0,25 | BASSA | 0,91 | -2,81% | +1,62% |
| 2026-08-04 | DOGE | 0.07022 | V2.1.3 | OK | 0 | 0 | 2,12 | MEDIA | 1,87 | -1,85% | +0,95% |
| 2026-08-04 | SOL | 73,75 | V2.1.3 | OK | 0 | 0 | 2,25 | MEDIA | 1,29 | +1,23% | -3,33% |
| 2026-08-03 | BTC | 62.770,98 | V2.1.3 | OK | 0 | 0 | 2,38 | MEDIA | 1,51 | -1,33% | +2,59% |
| 2026-08-03 | DOGE | 0.06977 | V2.1.3 | OK | 0 | 0 | 2,12 | MEDIA | 1,27 | -1,69% | -0,89% |
| 2026-08-03 | SOL | 72,88 | V2.1.3 | OK | 0 | 0 | 2,38 | MEDIA | 1,86 | -2,67% | +1,16% |

## Accuratezza direzionale

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 1 | +100,00% | +1,59% | +1,07% | +1,84% | FEEDBACK RAPIDO |
| BTC | 3g | 1 | +100,00% | +1,47% | -1,13% | +3,82% | FEEDBACK RAPIDO |
| BTC | 7g | 1 | +100,00% | +1,35% | -1,18% | +3,82% | FEEDBACK RAPIDO |
| BTC | 14g | 1 | +0,00% | -2,63% | -3,44% | +3,82% | FEEDBACK RAPIDO |
| BTC | 30g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 1g | 1 | +0,00% | -0,43% | -0,39% | +0,39% | FEEDBACK RAPIDO |
| SOL | 3g | 1 | +0,00% | -3,12% | -3,63% | +0,73% | FEEDBACK RAPIDO |
| SOL | 7g | 1 | +0,00% | -6,27% | -6,64% | +0,73% | FEEDBACK RAPIDO |
| SOL | 14g | 1 | +0,00% | -5,72% | -9,55% | +0,73% | FEEDBACK RAPIDO |
| SOL | 30g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 1g | 2 | +100,00% | +3,08% | +1,70% | +3,12% | FEEDBACK RAPIDO |
| DOGE | 3g | 2 | +100,00% | +2,99% | -0,85% | +6,21% | FEEDBACK RAPIDO |
| DOGE | 7g | 2 | +100,00% | +1,07% | -0,93% | +6,44% | FEEDBACK RAPIDO |
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

**SOL** — SOL: i futures sembrano più vulnerabili verso una discesa improvvisa. Non significa che deve scendere, ma se rompe sotto può accelerare. Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale.

**DOGE** — DOGE: i futures non danno una lettura chiara. Non si vede uno sbilanciamento forte né long né short. Qui pesa di più il report frattale.

| Asset | Prezzo | Funding | OI 24h | Long/Short | Lettura futures | Forza |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 64.258 $ | +0.0049% | -1.39% | 1.54 | Misto | 1/5 |
| SOL | 73,91 $ | +0.0043% | +26.08% | 1.71 | Rischio sotto | 5/5 |
| DOGE | 0.06992 $ | +0.0072% | -15.37% | 3.04 | Misto | 1/5 |

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

Generato: 2026-08-05 05:15 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [rsi_multitimeframe_divergence_report.md](rsi_multitimeframe_divergence_report.md)

Il modulo confronta prezzo e RSI 14 sui pivot confermati **daily e weekly**. Riconosce divergenze regolari e nascoste, segnali in formazione, invalidazioni e semplice conferma del momentum.

**Peso operativo: 0.** Non modifica il Global Confluence, non cambia le soglie del Paper Trading e non apre né blocca operazioni. I risultati vengono misurati prima di qualsiasi futura decisione sul peso.

## Sintesi corrente

| Asset   | Daily               | Stato D       | Weekly                     | Stato W    | Lettura weekly                                                                                                                |   Peso |
|:--------|:--------------------|:--------------|:---------------------------|:-----------|:------------------------------------------------------------------------------------------------------------------------------|-------:|
| BTC     | Bullish regolare    | CONFERMATA    | Bullish regolare           | CONFERMATA | Bullish regolare confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto. |      0 |
| SOL     | Conferma ribassista | CONTESTO      | Hidden bearish             | CONFERMATA | Hidden bearish confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto.   |      0 |
| DOGE    | Bullish regolare    | IN_FORMAZIONE | Misto / nessuna divergenza | CONTESTO   | Misto / nessuna divergenza. Non esiste una divergenza confermata sugli ultimi pivot.                                          |      0 |

## Dettaglio dei pivot

| Asset   | TF   | Tipo                       | Stato         | Prezzo / RSI      | Pivot confrontati                                                   | Δ prezzo contesto   | Δ RSI contesto   |   Peso |
|:--------|:-----|:---------------------------|:--------------|:------------------|:--------------------------------------------------------------------|:--------------------|:-----------------|-------:|
| BTC     | 1D   | Bullish regolare           | CONFERMATA    | 64.248 $ / 51,44  | 2026-06-25 58.076 $ / RSI 30,46 → 2026-07-01 57.748 $ / RSI 37,26   | n/a                 | n/a              |      0 |
| BTC     | 1W   | Bullish regolare           | CONFERMATA    | 64.248 $ / 40,03  | 2026-06-07 59.109 $ / RSI 34,23 → 2026-07-05 57.748 $ / RSI 38,20   | n/a                 | n/a              |      0 |
| SOL     | 1D   | Conferma ribassista        | CONTESTO      | 73,88 $ / 46,61   | n/a                                                                 | -5,41%              | -8,50            |      0 |
| SOL     | 1W   | Hidden bearish             | CONFERMATA    | 73,88 $ / 38,73   | 2026-05-17 98,27 $ / RSI 38,29 → 2026-07-05 83,81 $ / RSI 42,25     | n/a                 | n/a              |      0 |
| DOGE    | 1D   | Bullish regolare           | IN_FORMAZIONE | 0.06993 $ / 41,85 | 2026-07-24 0.06829 $ / RSI 33,29 → 2026-08-01 0.06797 $ / RSI 37,78 | n/a                 | n/a              |      0 |
| DOGE    | 1W   | Misto / nessuna divergenza | CONTESTO      | 0.06993 $ / 32,66 | n/a                                                                 | -4,33%              | 0,53             |      0 |

### BTC

- **1D — Bullish regolare / CONFERMATA**: Bullish regolare confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto.
- **1W — Bullish regolare / CONFERMATA**: Bullish regolare confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto.

### SOL

- **1D — Conferma ribassista / CONTESTO**: Prezzo e RSI stanno scendendo insieme: momentum ribassista confermato, nessuna bullish divergence attiva.
- **1W — Hidden bearish / CONFERMATA**: Hidden bearish confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto.

### DOGE

- **1D — Bullish regolare / IN_FORMAZIONE**: Bullish regolare in formazione: il secondo estremo non è ancora un pivot confermato. Peso operativo sempre 0.
- **1W — Misto / nessuna divergenza / CONTESTO**: Misto / nessuna divergenza. Non esiste una divergenza confermata sugli ultimi pivot.

## Tracker live delle divergenze confermate

Viene salvato un solo evento per combinazione di asset, timeframe, tipo e coppia di pivot. Gli esiti vengono controllati dopo 30, 60, 90 e 180 giorni.

- Eventi indipendenti salvati: **6**.
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

Generato: 2026-08-05 05:15 UTC


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

| Asset   | Prezzo   |   Punteggio | Verdetto         | Trend            | Momentum        | Struttura                                             |   Pattern score | Fibonacci      | Pattern rialzista               | Pattern ribassista           | Supporto   | Resistenza   |
|:--------|:---------|------------:|:-----------------|:-----------------|:----------------|:------------------------------------------------------|----------------:|:---------------|:--------------------------------|:-----------------------------|:-----------|:-------------|
| BTC | 64.258 $ | -1 | NEUTRALE / MISTO | Trend ribassista | Momentum debole | Volatilità in espansione | 0 | 0 / TESTATO | Doppio minimo / CANDIDATO | Doppio massimo / CANDIDATO | 57.748 | 66.910 |
| SOL | 73,91 $ | -6 | DEBOLE | Trend ribassista | Momentum misto | Compressione / triangolo | 0 | 0 / TESTATO | Adam and Eve Bottom / CANDIDATO | Doppio massimo / CANDIDATO | 73,40 | 78,73 |
| DOGE | 0.06992 $ | -5 | DEBOLE | Trend ribassista | Momentum misto | Struttura ribassista con massimi e minimi decrescenti | 0 | 0 / NON ATTIVO | Doppio minimo / CANDIDATO | Adam and Eve Top / CANDIDATO | 0.06829 | 0.07380 |

## Riepilogo ciclo di vita pattern

| Asset   | Doppio minimo   | Triplo minimo   | Adam/Eve Bottom                 | Doppio massimo   | Triplo massimo   | Adam/Eve Top                 |   Punteggio pattern |
|:--------|:----------------|:----------------|:--------------------------------|:-----------------|:-----------------|:-----------------------------|--------------------:|
| BTC | CANDIDATO | CANDIDATO | Adam and Eve Bottom — CANDIDATO | CANDIDATO | CANDIDATO | Adam and Eve Top — CANDIDATO | 0 |
| SOL | INVALIDATO | CANDIDATO | Adam and Eve Bottom — CANDIDATO | CANDIDATO | CANDIDATO | Adam and Eve Top — CANDIDATO | 0 |
| DOGE | CANDIDATO | CANDIDATO | Adam and Eve Bottom — CANDIDATO | ASSENTE | ASSENTE | Adam and Eve Top — CANDIDATO | 0 |

## Indicatori tecnici

| Asset   |   RSI 14 |   Istogramma MACD | MA20    | MA50    | MA200   | Pendenza MA50 20g   | Pendenza MA200 60g   | Rendimento 30g   | Rendimento 90g   |
|:--------|---------:|------------------:|:--------|:--------|:--------|:--------------------|:---------------------|:-----------------|:-----------------|
| BTC | 51.49 | -122.335 | 64.341 | 63.266 | 70.808 | -1,00% | -9,93% | 0,41% | -19,69% |
| SOL | 46.71 | -0.20974 | 74,90 | 75,02 | 85,01 | 1,74% | -16,97% | -9,77% | -16,40% |
| DOGE | 41.82 | 0.0002 | 0.07113 | 0.07448 | 0.09354 | -8,87% | -16,51% | -8,70% | -35,15% |

## Dettaglio asset

### BTC

- Prezzo: **64.258 $**
- Punteggio tecnico: **-1 / 12**
- Verdetto: **NEUTRALE / MISTO**
- Trend: **Trend ribassista** (-3)
- Momentum: **Momentum debole** (-3)
- Volume: **Volume da accumulazione** (2)
- Struttura: **Volatilità in espansione** (0)
  - Dettaglio struttura: Ultimi minimi: 5.808e+04 -> 5.775e+04. Ultimi massimi: 6.551e+04 -> 6.691e+04.
- Divergenza: **Divergenza rialzista RSI** (2)
- Fase Wyckoff candidata: **Possibile accumulazione** (1)
  - Dettaglio Wyckoff: Prezzo sotto MA200, vicino alla parte bassa del range a 120 giorni, RSI 51.5.
- Fibonacci automatico: **TESTATO** (0)
  - Swing UP 2026-07-01 57.748 -> 2026-07-21 66.910; livello più vicino 23.6% a 64.748; stato TESTATO; confluenza: nessuna confluenza indipendente.
- Punteggio pattern: **0**
  - rialzista dominante: Doppio minimo (CANDIDATO, 0); ribassista dominante: Doppio massimo (CANDIDATO, 0).
- Supporto più vicino: **57.748**
- Resistenza più vicina: **66.910**

Pattern classici e ciclo di vita:

- Doppio minimo: **CANDIDATO** (0)
  - Due minimi simili vicino a 57.748 tra 2026-06-05 e 2026-07-01. Neckline stimata: 67.248. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 35 giorni.
  - neckline 67.248; target 76.748; distanza dalla neckline 4,65%; prezzo sotto neckline.
- Triplo minimo: **CANDIDATO** (0)
  - Tre minimi simili vicino a 57.748 dal 2026-06-05 al 2026-07-01. Neckline stimata: 67.248. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 35 giorni.
  - neckline 67.248; target 76.748; distanza dalla neckline 4,65%; prezzo sotto neckline.
- Adam and Eve Bottom: **CANDIDATO** (0)
  - Pattern Adam and Eve Bottom vicino a 57.748 dal 2026-06-05 al 2026-07-01. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 67.248. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 35 giorni.
  - neckline 67.248; target 76.748; distanza dalla neckline 4,65%; prezzo sotto neckline.
- Doppio massimo: **CANDIDATO** (0)
  - Due massimi simili vicino a 67.248 tra 2026-06-15 e 2026-07-21. Neckline ribassista stimata: 57.748. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 15 giorni.
  - neckline 57.748; target 48.247; distanza dalla neckline 11,27%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 66.910 dal 2026-06-22 al 2026-07-21. Neckline ribassista stimata: 57.748. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 15 giorni.
  - neckline 57.748; target 48.585; distanza dalla neckline 11,27%; prezzo sopra neckline.
- Adam and Eve Top: **CANDIDATO** (0)
  - Pattern Adam and Eve Top vicino a 67.248 dal 2026-06-15 al 2026-07-21. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 57.748. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 15 giorni.
  - neckline 57.748; target 48.247; distanza dalla neckline 11,27%; prezzo sopra neckline.

### SOL

- Prezzo: **73,91 $**
- Punteggio tecnico: **-6 / 12**
- Verdetto: **DEBOLE**
- Trend: **Trend ribassista** (-3)
- Momentum: **Momentum misto** (1)
- Volume: **Volume da distribuzione** (-1)
- Struttura: **Compressione / triangolo** (0)
  - Dettaglio struttura: Ultimi minimi: 64.42 -> 73.4. Ultimi massimi: 78.88 -> 78.73.
- Divergenza: **Divergenza ribassista nascosta RSI** (-1)
- Fase Wyckoff candidata: **Markdown / fase ribassista** (-2)
  - Dettaglio Wyckoff: Prezzo sotto MA200 con trend a 90 giorni ancora debole.
- Fibonacci automatico: **TESTATO** (0)
  - Swing UP 2026-06-06 60,41 -> 2026-07-21 78,73; livello più vicino 23.6% a 74,40; stato TESTATO; confluenza: supporto tecnico.
- Punteggio pattern: **0**
  - rialzista dominante: Adam and Eve Bottom (CANDIDATO, 0); ribassista dominante: Doppio massimo (CANDIDATO, 0).
- Supporto più vicino: **73,40**
- Resistenza più vicina: **78,73**

Pattern classici e ciclo di vita:

- Doppio minimo: **INVALIDATO** (0)
  - Due minimi simili vicino a 60,41 tra 2026-06-06 e 2026-06-25. Neckline stimata: 75,94. Breakout neckline: 2026-07-01 (35 giorni fa). Stato: INVALIDATO. Target teorico: 91,46; progresso corrente: -13,07%. Relazione prezzo/neckline: sotto neckline.
  - neckline 75,94; target 91,46; breakout 2026-07-01 (35g); progresso -13,07%; prezzo sotto neckline.
- Triplo minimo: **CANDIDATO** (0)
  - Tre minimi simili vicino a 81,63 dal 2026-04-29 al 2026-05-23. Neckline stimata: 98,27. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 74 giorni.
  - neckline 98,27; target 114,91; distanza dalla neckline 32,95%; prezzo sotto neckline.
- Adam and Eve Bottom: **CANDIDATO** (0)
  - Pattern Adam and Eve Bottom vicino a 67,92 dal 2026-06-19 al 2026-07-17. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 83,81. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 19 giorni.
  - neckline 83,81; target 99,70; distanza dalla neckline 13,39%; prezzo sotto neckline.
- Doppio massimo: **CANDIDATO** (0)
  - Due massimi simili vicino a 78,73 tra 2026-06-15 e 2026-07-21. Neckline ribassista stimata: 64,42. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 15 giorni.
  - neckline 64,42; target 50,11; distanza dalla neckline 14,73%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 78,88 dal 2026-06-15 al 2026-07-21. Neckline ribassista stimata: 64,42. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 15 giorni.
  - neckline 64,42; target 49,96; distanza dalla neckline 14,73%; prezzo sopra neckline.
- Adam and Eve Top: **CANDIDATO** (0)
  - Pattern Adam and Eve Top vicino a 78,73 dal 2026-06-15 al 2026-07-21. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 64,42. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 15 giorni.
  - neckline 64,42; target 50,11; distanza dalla neckline 14,73%; prezzo sopra neckline.

### DOGE

- Prezzo: **0.06992 $**
- Punteggio tecnico: **-5 / 12**
- Verdetto: **DEBOLE**
- Trend: **Trend ribassista** (-3)
- Momentum: **Momentum misto** (1)
- Volume: **Volume da distribuzione** (-1)
- Struttura: **Struttura ribassista con massimi e minimi decrescenti** (-2)
  - Dettaglio struttura: Ultimi minimi: 0.07097 -> 0.06829. Ultimi massimi: 0.07923 -> 0.0738.
- Divergenza: **Divergenza ribassista nascosta RSI** (-1)
- Fase Wyckoff candidata: **Possibile accumulazione** (1)
  - Dettaglio Wyckoff: Prezzo sotto MA200, vicino alla parte bassa del range a 120 giorni, RSI 41.8.
- Fibonacci automatico: **NON ATTIVO** (0)
  - Swing DOWN 2026-05-14 0.11825 -> 2026-07-24 0.06829; livello più vicino 23.6% a 0.08008; stato NON ATTIVO; confluenza: neckline rialzista.
- Punteggio pattern: **0**
  - rialzista dominante: Doppio minimo (CANDIDATO, 0); ribassista dominante: Adam and Eve Top (CANDIDATO, 0).
- Supporto più vicino: **0.06829**
- Resistenza più vicina: **0.07380**

Pattern classici e ciclo di vita:

- Doppio minimo: **CANDIDATO** (0)
  - Due minimi simili vicino a 0.06829 tra 2026-06-30 e 2026-07-24. Neckline stimata: 0.07923. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 12 giorni.
  - neckline 0.07923; target 0.09017; distanza dalla neckline 13,32%; prezzo sotto neckline.
- Triplo minimo: **CANDIDATO** (0)
  - Tre minimi simili vicino a 0.06829 dal 2026-06-30 al 2026-07-24. Neckline stimata: 0.07923. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 12 giorni.
  - neckline 0.07923; target 0.09017; distanza dalla neckline 13,32%; prezzo sotto neckline.
- Adam and Eve Bottom: **CANDIDATO** (0)
  - Pattern Adam and Eve Bottom vicino a 0.06829 dal 2026-06-30 al 2026-07-24. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 0.07923. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 12 giorni.
  - neckline 0.07923; target 0.09017; distanza dalla neckline 13,32%; prezzo sotto neckline.
- Doppio massimo: **ASSENTE** (0)
- Triplo massimo: **ASSENTE** (0)
- Adam and Eve Top: **CANDIDATO** (0)
  - Pattern Adam and Eve Top vicino a 0.07923 dal 2026-07-04 al 2026-07-26. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 0.06829. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 10 giorni.
  - neckline 0.06829; target 0.05735; distanza dalla neckline 2,38%; prezzo sopra neckline.

## Fibonacci automatico

Il modulo seleziona uno swing recente tramite pivot confermati. Un semplice tocco vale 0: Fibonacci pesa al massimo ±1 soltanto quando il livello è tenuto, perso, recuperato o respinto e coincide con almeno un livello tecnico indipendente.

| Asset   | Swing                         | 23,6%   | 38,2%   | 50,0%   | 61,8%   | 78,6%   | Livello vicino   | Stato      | Confluenza                      |   Score |
|:--------|:------------------------------|:--------|:--------|:--------|:--------|:--------|:-----------------|:-----------|:--------------------------------|--------:|
| BTC | UP 2026-07-01 -> 2026-07-21 | 64.748 | 63.410 | 62.329 | 61.248 | 59.708 | 23.6% / 64.748 | TESTATO | nessuna confluenza indipendente | 0 |
| SOL | UP 2026-06-06 -> 2026-07-21 | 74,40 | 71,73 | 69,57 | 67,41 | 64,33 | 23.6% / 74,40 | TESTATO | supporto tecnico | 0 |
| DOGE | DOWN 2026-05-14 -> 2026-07-24 | 0.08008 | 0.08738 | 0.09327 | 0.09917 | 0.10756 | 23.6% / 0.08008 | NON ATTIVO | neckline rialzista | 0 |

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

- **BTC**: 4/30 previsioni controllate su 34 fatte. Stato: **RACCOLTA DATI**.
- **SOL**: 4/30 previsioni controllate su 34 fatte. Stato: **RACCOLTA DATI**.
- **DOGE**: 4/30 previsioni controllate su 34 fatte. Stato: **RACCOLTA DATI**.

| Asset | Previsioni fatte | Controllate | Progresso | In attesa | Stato | Prossimo controllo |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 34 | 4 | 4/30 [█░░░░░░░░░] | 30 | RACCOLTA DATI | 2026-08-06 / tra 1 giorno |
| SOL | 34 | 4 | 4/30 [█░░░░░░░░░] | 30 | RACCOLTA DATI | 2026-08-06 / tra 1 giorno |
| DOGE | 34 | 4 | 4/30 [█░░░░░░░░░] | 30 | RACCOLTA DATI | 2026-08-06 / tra 1 giorno |

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

Generato: 2026-08-05 05:16 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [data_quality_coherence_report.md](data_quality_coherence_report.md)

Questo controllo non modifica punteggi o decisioni. Verifica che tutti i moduli usino lo stesso prezzo corrente e che le nuove regole Technical/Classic Visual siano integre.

## Stato finale: **OK**

## Prezzo unico per modulo

| Modulo                  | Asset   | Campo             | Stato   | Prezzo snapshot   | Prezzo modulo   | Differenza   |
|:------------------------|:--------|:------------------|:--------|:------------------|:----------------|:-------------|
| Scanner                 | BTC     | current_price     | OK      | 64.258 $          | 64.258 $        | +0,0000%     |
| Scanner                 | DOGE    | current_price     | OK      | 0.06992 $         | 0.06992 $       | -0,0000%     |
| Scanner                 | SOL     | current_price     | OK      | 73,91 $           | 73,91 $         | +0,0000%     |
| Scanner Forecast        | BTC     | current_price     | OK      | 64.258 $          | 64.258 $        | +0,0000%     |
| Scanner Forecast        | SOL     | current_price     | OK      | 73,91 $           | 73,91 $         | +0,0000%     |
| Scanner Forecast        | DOGE    | current_price     | OK      | 0.06992 $         | 0.06992 $       | -0,0000%     |
| Technical Structure     | BTC     | price             | OK      | 64.258 $          | 64.258 $        | +0,0000%     |
| Technical Structure     | SOL     | price             | OK      | 73,91 $           | 73,91 $         | +0,0000%     |
| Technical Structure     | DOGE    | price             | OK      | 0.06992 $         | 0.06992 $       | -0,0000%     |
| Classic Technical       | BTC     | price             | OK      | 64.258 $          | 64.258 $        | +0,0000%     |
| Classic Technical       | SOL     | price             | OK      | 73,91 $           | 73,91 $         | +0,0000%     |
| Classic Technical       | DOGE    | price             | OK      | 0.06992 $         | 0.06992 $       | -0,0000%     |
| Classic Visual          | BTC     | price             | OK      | 64.258 $          | 64.258 $        | +0,0000%     |
| Classic Visual          | SOL     | price             | OK      | 73,91 $           | 73,91 $         | +0,0000%     |
| Classic Visual          | DOGE    | price             | OK      | 0.06992 $         | 0.06992 $       | -0,0000%     |
| Exchange Microstructure | BTC     | price             | OK      | 64.258 $          | 64.294 $        | +0,0549%     |
| Exchange Microstructure | SOL     | price             | OK      | 73,91 $           | 74,03 $         | +0,1651%     |
| Exchange Microstructure | DOGE    | price             | OK      | 0.06992 $         | 0.06998 $       | +0,0858%     |
| RSI top-cycle           | SOL     | current_price     | OK      | 73,91 $           | 73,91 $         | +0,0000%     |
| RSI top-cycle           | SOL     | current_price     | OK      | 73,91 $           | 73,91 $         | +0,0000%     |
| Frattale BTC/SOL        | SOL     | sol_current_price | OK      | 73,91 $           | 73,91 $         | +0,0000%     |
| Fractal path            | SOL     | current_price     | OK      | 73,91 $           | 73,91 $         | +0,0000%     |

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

Generato: 2026-08-06T00:17:34+00:00

- Modalità: **SOLO PAPER TRADING**
- Asset: **SOL spot**
- Leva: **nessuna (1x)**
- Capitale iniziale separato: **€40.000,00**
- Fonte mercato: **KUCOIN_PUBLIC_API**; nuove entrate: **CONSENTITE**

| Equity | Cash | SOL | Prezzo | Rendimento | Realizzato | Commissioni | Max DD | Operazioni |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €39.997,03 | €4.024,85 | 486.149894 | 73.9940 | -0.01% | €0,00 | €35,98 | 6.48% | 6 |

**Ultima decisione:** HOLD — Prezzo dentro la fascia neutrale.

Bande 4H: L2 68.7194 · L1 70.7729 · media 73.3398 · U1 75.9067 · U2 77.9602.

> Questo portafoglio non condivide capitale, posizioni o statistiche con il paper trading da €10.000.
<!-- SOL_SPOT_ADAPTIVE_END -->
