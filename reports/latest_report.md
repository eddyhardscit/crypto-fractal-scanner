<!-- COMPACT_REPORT_HEADER_START -->
> **Vista compatta:** Decisione operativa, Global Confluence e cambiamenti giornalieri restano aperti. Tocca il titolo di una sezione per mostrare o nascondere i dettagli.  
> Tutte le tabelle e tutti i dati restano nel file: copiando il Markdown raw viene copiato tutto.
<!-- COMPACT_REPORT_HEADER_END -->

<!-- COMPACT_SECTION_START:decision -->
<details open>
<summary><strong>🧭 Decisione operativa — da leggere per prima</strong></summary>

<!-- DECISION_REPORT_START -->

# Decisione operativa sintetica

Generato: 2026-08-18 05:32 UTC

Report separato completo: [decision_report.md](decision_report.md)

Sintesi automatica dello scanner: l'azione spot viene copiata direttamente dal Global Confluence; long, short e rischio restano filtri separati e più prudenti.

| Asset | Global | Direzione | Spot | Long leva | Short leva | Max long | Max short | Rischio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 0 | NEUTRALE / COSTRUTTIVO | HOLD / ATTESA CONFERME | NO LONG A LEVA / ATTENDI SOPRA 67.248 $ | NO SHORT | nessuna | nessuna | MEDIO / ALTO |
| SOL | +1 | NEUTRALE / INCERTO | HOLD LEGGERO / ATTESA CONFERME | NO LONG A LEVA | NO SHORT | nessuna | nessuna | MOLTO ALTO |
| DOGE | +3 | NEUTRALE / COSTRUTTIVO | SOLO TRANCHE PICCOLE / NO LEVA | NO LONG A LEVA | NO SHORT | nessuna | nessuna | MOLTO ALTO |

## Lettura immediata

- **BTC**: Global = **0**, spot = **HOLD / ATTESA CONFERME**, long = **NO LONG A LEVA / ATTENDI SOPRA 67.248 $**, short = **NO SHORT**, rischio = **MEDIO / ALTO**.
- **SOL**: Global = **+1**, spot = **HOLD LEGGERO / ATTESA CONFERME**, long = **NO LONG A LEVA**, short = **NO SHORT**, rischio = **MOLTO ALTO**.
- **DOGE**: Global = **+3**, spot = **SOLO TRANCHE PICCOLE / NO LEVA**, long = **NO LONG A LEVA**, short = **NO SHORT**, rischio = **MOLTO ALTO**.

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
- Conferme: Prima resistenza sopra 65.402; conferma del doppio minimo sopra 66.910.
- Invalidazioni: Sotto 62.227 il quadro tecnico peggiora.

### SOL

- Global Confluence: **+1**
- Confluenza: **MISTA / PARZIALE**
- Bias Global: **Neutrale / misto**
- Direzione decisionale: **NEUTRALE / INCERTO**
- Azione spot dal Global: **HOLD LEGGERO / ATTESA CONFERME**
- Long leva: **NO LONG A LEVA**
- Short leva: **NO SHORT**
- Rischio: **MOLTO ALTO**
- Conferme: conferma del doppio minimo sopra 83,81; nuova conferma tecnica sopra 77,62; milestone analogiche 79,48 / 91,85, valide soltanto se rientra anche il gap frattale.
- Invalidazioni: Allarmi sotto 69,83 / 70,69 / 62,19.

### DOGE

- Global Confluence: **+3**
- Confluenza: **MODERATAMENTE POSITIVA**
- Bias Global: **Costruttivo prudente**
- Direzione decisionale: **NEUTRALE / COSTRUTTIVO**
- Azione spot dal Global: **SOLO TRANCHE PICCOLE / NO LEVA**
- Long leva: **NO LONG A LEVA**
- Short leva: **NO SHORT**
- Rischio: **MOLTO ALTO**
- Conferme: Sopra 0.07286 migliora; sopra 0.06933 viene invalidato il pattern ribassista dominante.
- Invalidazioni: Sotto 0.06895 il rischio ribassista aumenta.

## Nota semplice

- **Spot** = usa la stessa azione del Global Confluence, senza una seconda mappatura che possa produrre frasi diverse.
- **Zona alta storica** = zona dove non inseguire troppo; può essere zona da prendere profitto.
- **Zona bassa storica** = zona di rischio; con leva la liquidazione non dovrebbe stare lì vicino.
- **BTC leva** = nessun long a leva finché il prezzo snapshot non supera **67.248 $**; sotto quella soglia resta solo l'azione spot indicata dal Global.
- **Lifecycle EMA200** = per SOL resta solo contesto, peso Global 0; score interno 4; EMA200 circa 111,29 $; upside verso EMA200 +47,09%. Non autorizza leva e non aggiunge punti automatici.
- **NO LONG** non significa automaticamente **SHORT**. Lo short ha senso solo se il quadro è bearish o se lo spike viene spesso scaricato.
- Per SOL, se il Global è da **+3 in su**, la decisione non deve diventare bearish solo perché lo scanner grezzo a 30 giorni è incerto.

<!-- DECISION_REPORT_END -->

<!-- PAPER_TRADING_START -->
# Paper trading automatico KuCoin

Generato: 2026-08-18T05:33:06+00:00


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [paper_trading_report.md](paper_trading_report.md)

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-08-18T05:05:27+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-08-18T05:05:27+00:00 | 2026-08-18T05:05:27+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-08-18T04:45:00+00:00 | 2026-08-18T04:45:00+00:00 | 5,6 min | 25,0 min | OK |
| 60m | 12 | 2026-08-18T04:00:00+00:00 | 2026-08-18T04:00:00+00:00 | 5,6 min | 45,0 min | OK |
| 240m | 12 | 2026-08-18T00:00:00+00:00 | 2026-08-18T00:00:00+00:00 | 1,09 h | 1,00 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | SNDK | 240m | LONG | 8,25 | 6,00 | 0,00 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | XRP | 240m | SHORT | -6,98 | 6,00 | 0,00 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | BEAT | 240m | SHORT | -6,75 | 6,00 | 0,00 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | GPS | 240m | LONG | 6,75 | 6,00 | 0,00 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | DOGE | 240m | SHORT | -6,39 | 6,00 | 0,00 | STALE_CANDLE | 1,09 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | HYPE | 240m | LONG | 5,63 | 6,00 | 0,37 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | TUT | 240m | LONG | 5,50 | 6,00 | 0,50 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | ZEC | 240m | LONG | 4,61 | 6,00 | 1,39 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | BTC | 240m | LONG | 1,25 | 6,00 | 4,75 | STALE_CANDLE | 1,09 h | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | SKHYNIX | 240m | LONG | 1,15 | 6,00 | 4,85 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | SOL | 240m | SHORT | -0,24 | 6,00 | 5,76 | STALE_CANDLE | 1,09 h | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | ETH | 240m | SHORT | -0,07 | 6,00 | 5,93 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Bilanciata 1H V3 Filtered | BEAT | 60m | SHORT | -6,25 | 6,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Fast Score 6 75 V1 | BEAT | 60m | SHORT | -6,25 | 6,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Fast Score 6 75 No Trend Up V1 | BEAT | 60m | SHORT | -6,25 | 6,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Fast V3 Cap75 V1 | BEAT | 60m | SHORT | -6,25 | 4,50 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Forza relativa 1H V1 | BEAT | 60m | SHORT | -6,25 | 4,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Balanced V3 Long Only V1 | BEAT | 60m | SHORT | -6,25 | 6,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Balanced Long No Rhv V1 | HYPE | 60m | LONG | 5,21 | 5,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Bilanciata 1H V2 | BEAT | 60m | SHORT | -6,25 | 5,50 | 0,00 | STRATEGY_FILTER | 5,6 min | D: n/a | W: n/a | peso 0 | Filtro V2 non superato: regime, EMA, ritorni e RSI; per Rapida V2 servono anche breakout reale, volume e ADX. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.654,24 | -3,46% | €-94,11 | €3.000,00 | -3,14% | 5 | 42 | 33,33% | 0,72 | 6,36% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 42 | 1558 | PRIME INDICAZIONI | 100 (mancano 58) |

- Trade del Principale 4H chiusi: **42**; win rate **33,33%**; profit factor **0,72**.
- Expectancy: **€-9,04** per trade; P&L netto: **€-379,65**; max drawdown: **6,36%**.
- Valutazione: **Si può osservare la direzione, ma il risultato resta fragile.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 5 | €9.654,24 | €1.270,03 | €3.810,09 | €192,07 | €32,73 |
| TEST | Benchmark Donchian breakout 1H | 3 | €10.640,49 | €4.573,29 | €9.146,58 | €104,61 | €-12,72 |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | 2 | €10.590,59 | €1.769,88 | €5.309,64 | €106,16 | €-11,20 |
| TEST | Main Side Regime Guard V1 | 6 | €10.396,51 | €1.442,14 | €4.326,41 | €208,48 | €-6,46 |
| TEST | Donchian 1H Gb20 120R V1 | 3 | €10.389,97 | €4.465,62 | €8.931,24 | €102,14 | €-12,42 |
| TEST | 1H Fast Score 6 75 V1 | 4 | €10.366,63 | €3.442,13 | €10.326,38 | €207,57 | €1,53 |
| TEST | 1H Fast Score 6 75 Range Only V1 | 2 | €10.348,78 | €386,22 | €1.158,67 | €51,78 | €0,00 |
| TEST | 1H Fast V3 Nohigh Range Only V1 | 0 | €10.332,02 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 0 | €10.300,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 0 | €10.271,73 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Nohigh Cap75 V1 | 1 | €10.266,86 | €189,64 | €568,93 | €49,82 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 0 | €10.239,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 0 | €10.235,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Main Dynamic Asset Selector V1 | 0 | €10.230,30 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | 1 | €10.204,58 | €1.508,82 | €4.526,45 | €50,70 | €-16,70 |
| TEST | 1H Fast No Pepe V1 | 2 | €10.197,53 | €196,80 | €590,40 | €2,05 | €13,15 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 0 | €10.185,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Trend Side Regime Guard V1 | 4 | €10.150,13 | €3.391,14 | €6.782,27 | €152,57 | €19,75 |
| TEST | Scanner Top 5 Long 1H | 4 | €10.145,62 | €3.689,68 | €7.379,37 | €199,50 | €31,61 |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 0 | €10.145,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 1H | 0 | €10.138,40 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Balanced Short Trend Down Strict V1 | 2 | €10.115,05 | €2.326,70 | €6.980,10 | €100,51 | €10,12 |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 0 | €10.099,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | 4 | €10.091,00 | €3.350,61 | €10.051,82 | €202,05 | €1,49 |
| TEST | Sol Bollinger 4H | 0 | €10.086,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 4H | 0 | €10.084,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 0 | €10.048,77 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V1 | 0 | €10.043,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 1H | 0 | €10.039,30 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | 0 | €10.032,43 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · prudente · 5x | 0 | €10.028,67 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Cap75 V1 | 5 | €10.013,99 | €3.355,77 | €10.067,30 | €200,64 | €1,23 |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | 1 | €10.011,37 | €184,93 | €554,78 | €48,58 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 0 | €10.008,92 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €10.007,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 0 | €10.003,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 0 | €10.001,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €50 · 15x | 0 | €10.001,42 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €10 · 15x | 0 | €10.000,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Continuation V1 | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · prudente · 5x | 0 | €9.999,47 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €10 · 15x | 0 | €9.999,33 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Ema 1H | 1 | €9.999,04 | €1.155,63 | €3.466,88 | €49,92 | €12,65 |
| TEST | Scalp RSI Long 15 · €10 · 15x | 0 | €9.997,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €50 · 15x | 0 | €9.996,64 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 0 | €9.995,23 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €10 · 15x | 0 | €9.994,61 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €10 · 15x | 0 | €9.990,45 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 1H | 0 | €9.988,31 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €50 · 15x | 0 | €9.988,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 0 | €9.987,48 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · prudente · 5x | 0 | €9.980,94 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Ampia 4H | 6 | €9.977,89 | €1.662,17 | €3.324,34 | €199,40 | €23,81 |
| TEST | Doge Bollinger 1H | 0 | €9.975,30 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 1H | 0 | €9.973,77 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €50 · 15x | 0 | €9.973,06 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | 0 | €9.968,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Bollinger 1H | 0 | €9.959,49 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €50 · 15x | 0 | €9.952,25 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 4H | 0 | €9.949,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Donchian 4H | 0 | €9.931,19 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.931,14 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 4H | 1 | €9.929,52 | €1.413,45 | €2.826,90 | €49,75 | €-22,30 |
| TEST | Sol Adaptive 4H | 0 | €9.928,55 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · prudente · 5x | 0 | €9.926,30 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H V3 Filtered | 6 | €9.919,03 | €3.389,27 | €10.167,82 | €198,48 | €-12,82 |
| TEST | Combo Adaptive Side Regime Guard V1 | 4 | €9.902,77 | €4.838,90 | €9.677,80 | €99,33 | €13,98 |
| TEST | Doge Donchian 1H | 0 | €9.894,47 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Donchian 1H | 0 | €9.875,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 4H | 1 | €9.871,52 | €1.406,00 | €2.812,00 | €49,49 | €-28,23 |
| TEST | Btc Ema 1H | 0 | €9.848,58 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Ema 4H | 0 | €9.842,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V2 | 0 | €9.838,66 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 0 | €9.837,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive | 3 | €9.825,19 | €1.660,65 | €3.321,30 | €101,25 | €-9,40 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 0 | €9.817,34 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom10 Short | 3 | €9.815,06 | €1.923,37 | €3.846,75 | €98,53 | €13,66 |
| TEST | Scanner Bottom15 Short | 3 | €9.815,06 | €1.923,37 | €3.846,75 | €98,53 | €13,66 |
| TEST | Scanner Bottom20 Short | 3 | €9.815,06 | €1.923,37 | €3.846,75 | €98,53 | €13,66 |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | 0 | €9.811,70 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Regime V1 | 2 | €9.805,38 | €1.690,92 | €3.381,84 | €49,43 | €0,00 |
| TEST | Sol Ema 4H | 0 | €9.792,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Donchian 1H | 0 | €9.762,69 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 0 | €9.762,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 1H | 0 | €9.760,52 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | 2 | €9.746,63 | €1.892,84 | €3.785,69 | €97,35 | €13,85 |
| TEST | Scanner Bottom5 Short Profit Lock V1 | 2 | €9.731,81 | €1.889,96 | €3.779,93 | €97,20 | €13,83 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 0 | €9.723,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | 3 | €9.720,12 | €436,17 | €872,34 | €50,02 | €0,00 |
| TEST | Combo Mean Reversion | 0 | €9.720,09 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Adaptive 1H | 0 | €9.692,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | 4 | €9.690,60 | €369,55 | €1.108,64 | €43,76 | €12,50 |
| TEST | Global Confluence puro 1H | 1 | €9.689,94 | €1.512,09 | €3.024,18 | €48,39 | €11,04 |
| TEST | 1H Fast V3 Nohigh V1 | 1 | €9.668,04 | €215,12 | €645,36 | €48,02 | €0,00 |
| TEST | 1H Fast Tp2 V1 | 2 | €9.667,61 | €279,72 | €839,17 | €3,88 | €11,54 |
| TEST | Scanner Bottom 5 Short 1H | 2 | €9.656,92 | €1.875,42 | €3.750,84 | €96,45 | €13,72 |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | 1 | €9.630,78 | €196,64 | €589,91 | €45,15 | €0,00 |
| TEST | Rapida 1H V3 Filtered | 4 | €9.627,28 | €367,13 | €1.101,40 | €43,47 | €12,41 |
| TEST | Sol Adaptive 1H | 0 | €9.621,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Forza relativa 1H V2 | 2 | €9.608,24 | €1.930,62 | €3.861,24 | €96,38 | €2,81 |
| TEST | Bilanciata 1H V2 | 3 | €9.600,79 | €1.189,62 | €3.568,85 | €97,21 | €-10,05 |
| TEST | Combo Adaptive Quality7 Regime V1 | 3 | €9.597,86 | €430,68 | €861,36 | €49,39 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 0 | €9.579,83 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Long Only V1 | 4 | €9.570,12 | €3.405,47 | €6.810,95 | €146,43 | €21,22 |
| TEST | Benchmark Bollinger mean reversion 1H | 1 | €9.564,42 | €202,90 | €405,81 | €0,00 | €0,00 |
| TEST | 1H Fast V3 No Esports Long Only V1 | 1 | €9.556,73 | €174,37 | €523,12 | €0,00 | €12,25 |
| TEST | Eth Ema 1H | 1 | €9.526,32 | €1.105,17 | €3.315,52 | €47,74 | €-20,30 |
| TEST | Combo Adaptive Quality7 V1 | 0 | €9.515,13 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | 4 | €9.508,14 | €2.591,80 | €7.775,40 | €141,13 | €14,51 |
| TEST | Master Adaptive Gb20 Be V1 | 3 | €9.502,15 | €2.959,04 | €5.918,08 | €94,61 | €34,55 |
| TEST | Master Adaptive Gb20 Partial V1 | 3 | €9.492,04 | €2.955,89 | €5.911,79 | €94,51 | €34,51 |
| TEST | Master Adaptive No Alt V1 | 5 | €9.488,34 | €4.571,18 | €9.142,35 | €141,05 | €53,58 |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | 3 | €9.480,20 | €1.938,06 | €3.876,12 | €139,84 | €33,16 |
| TEST | Master Adaptive Expanded V1 | 4 | €9.471,36 | €2.726,64 | €5.453,28 | €94,96 | €18,20 |
| TEST | Master Adaptive V1 | 3 | €9.455,33 | €2.944,46 | €5.888,92 | €94,15 | €34,38 |
| TEST | Scanner Top 5 + forza BTC 1H | 3 | €9.445,03 | €1.687,33 | €3.374,66 | €97,16 | €9,39 |
| TEST | Combo Adaptive Partial 1R V1 | 3 | €9.434,59 | €1.594,63 | €3.189,26 | €97,22 | €-9,02 |
| TEST | Master Adaptive Runner25 V1 | 5 | €9.417,72 | €3.311,30 | €6.622,61 | €133,15 | €57,18 |
| TEST | 1H Fast V3 No Esports V1 | 3 | €9.412,32 | €201,44 | €604,33 | €2,94 | €12,13 |
| TEST | Bilanciata 1H V1 | 5 | €9.398,92 | €1.443,61 | €4.330,82 | €96,37 | €12,04 |
| TEST | 1H Balanced V3 Long Only V1 | 6 | €9.381,81 | €3.205,71 | €9.617,13 | €187,73 | €-12,13 |
| TEST | Scanner Top5 Btc Guard V1 | 3 | €9.365,15 | €1.914,54 | €3.829,08 | €138,14 | €32,76 |
| TEST | 1H Balanced Long No Rhv V1 | 5 | €9.330,79 | €1.427,09 | €4.281,27 | €186,61 | €0,14 |
| TEST | Master Adaptive Gb20 V1 | 3 | €9.329,70 | €2.905,34 | €5.810,68 | €92,90 | €33,92 |
| TEST | Scanner Top10 Long | 5 | €9.322,38 | €3.427,93 | €6.855,87 | €184,64 | €7,56 |
| TEST | Scanner Top15 Long | 5 | €9.322,38 | €3.427,93 | €6.855,87 | €184,64 | €7,56 |
| TEST | Scanner Top20 Long | 5 | €9.322,38 | €3.427,93 | €6.855,87 | €184,64 | €7,56 |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | 3 | €9.317,55 | €1.904,81 | €3.809,61 | €137,44 | €32,59 |
| TEST | Combo Trend | 6 | €9.264,10 | €1.769,19 | €3.538,39 | €96,87 | €31,52 |
| TEST | Combo Adaptive Runner25 V1 | 4 | €9.223,42 | €1.462,29 | €2.924,57 | €52,74 | €7,57 |
| TEST | Master Adaptive Gb20 Loss Cap V1 | 2 | €9.148,58 | €3.642,04 | €7.284,08 | €78,67 | €25,65 |
| TEST | Scanner Top5 Btc Guard Mfe V1 | 3 | €9.147,35 | €1.870,01 | €3.740,03 | €134,93 | €32,00 |
| TEST | Scanner Top5 Btc Tp3 V1 | 3 | €9.132,44 | €3.195,37 | €6.390,74 | €138,94 | €12,85 |
| TEST | Benchmark trend following EMA 1H | 9 | €9.131,75 | €2.873,93 | €5.747,85 | €136,93 | €-15,78 |
| TEST | Scanner Top5 Btc Runner25 V1 | 3 | €9.127,09 | €3.193,50 | €6.387,00 | €138,86 | €12,84 |
| TEST | Master Adaptive Strict3 V1 | 2 | €9.106,10 | €1.605,81 | €3.211,63 | €85,72 | €21,93 |
| TEST | 1H Fast V3 Long Only V1 | 1 | €9.099,05 | €166,02 | €498,07 | €0,00 | €11,66 |
| TEST | Forza relativa 1H V1 | 5 | €9.089,95 | €5.037,46 | €10.074,93 | €180,32 | €5,04 |
| TEST | Combo Scanner | 3 | €9.063,75 | €1.831,17 | €3.662,33 | €92,80 | €10,14 |
| TEST | Combo Adaptive Tp3 V1 | 4 | €9.051,11 | €1.434,97 | €2.869,94 | €51,75 | €7,43 |
| TEST | Scanner Top5 Btc Btc Le3 V1 | 3 | €9.025,67 | €1.612,41 | €3.224,82 | €92,84 | €8,97 |
| TEST | Scanner Top5 Btc Mfe V1 | 3 | €8.853,35 | €1.581,63 | €3.163,25 | €91,07 | €8,80 |
| TEST | Combo Adaptive Mfe Trail | 4 | €8.747,34 | €1.479,67 | €2.959,34 | €90,13 | €-8,70 |

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
| PRINCIPALE | Principale 4H | Confluenza trend | €9.654,24 | €-379,65 | 42 | 42 | 33,33% | 0,72 | €-9,04 | 6,36% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €10.640,49 | €657,21 | 63 | 63 | 47,62% | 1,44 | €10,43 | 3,63% |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | Momentum / breakout | €10.590,59 | €604,98 | 72 | 72 | 50,00% | 1,40 | €8,40 | 3,35% |
| TEST | Main Side Regime Guard V1 | Confluenza trend | €10.396,51 | €402,00 | 23 | 23 | 47,83% | 1,80 | €17,48 | 2,40% |
| TEST | Donchian 1H Gb20 120R V1 | Donchian breakout 20 barre | €10.389,97 | €406,30 | 31 | 31 | 45,16% | 1,64 | €13,11 | 3,63% |
| TEST | 1H Fast Score 6 75 V1 | Momentum / breakout | €10.366,63 | €303,70 | 125 | 124 | 44,00% | 1,11 | €2,43 | 4,89% |
| TEST | 1H Fast Score 6 75 Range Only V1 | Momentum / breakout | €10.348,78 | €349,47 | 33 | 33 | 51,52% | 1,41 | €10,59 | 2,31% |
| TEST | 1H Fast V3 Nohigh Range Only V1 | Momentum / breakout V3 Filtered | €10.332,02 | €332,02 | 34 | 34 | 47,06% | 1,47 | €9,77 | 3,55% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | Momentum / breakout V3 Filtered | €10.300,05 | €300,05 | 33 | 33 | 48,48% | 2,04 | €9,09 | 2,01% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | Momentum / breakout V3 Filtered | €10.271,73 | €271,73 | 22 | 22 | 50,00% | 1,74 | €12,35 | 1,72% |
| TEST | 1H Fast Nohigh Cap75 V1 | Momentum / breakout | €10.266,86 | €267,44 | 114 | 114 | 43,86% | 1,11 | €2,35 | 6,52% |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | Momentum / breakout V3 Filtered | €10.239,20 | €239,20 | 17 | 17 | 52,94% | 4,50 | €14,07 | 1,01% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | Momentum / breakout V3 Filtered | €10.235,18 | €235,18 | 20 | 20 | 50,00% | 1,90 | €11,76 | 2,73% |
| TEST | Main Dynamic Asset Selector V1 | Confluenza trend | €10.230,30 | €230,30 | 11 | 11 | 45,45% | 1,85 | €20,94 | 1,50% |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | Momentum / breakout V3 Filtered | €10.204,58 | €224,39 | 56 | 56 | 44,64% | 1,19 | €4,01 | 5,24% |
| TEST | 1H Fast No Pepe V1 | Momentum / breakout | €10.197,53 | €184,72 | 128 | 128 | 43,75% | 1,08 | €1,44 | 3,64% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | Momentum / breakout V3 Filtered | €10.185,37 | €185,37 | 22 | 22 | 40,91% | 1,57 | €8,43 | 2,27% |
| TEST | Combo Trend Side Regime Guard V1 | Combo Trend | €10.150,13 | €127,70 | 48 | 48 | 50,00% | 1,14 | €2,66 | 2,94% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.145,62 | €118,64 | 77 | 77 | 42,86% | 1,06 | €1,54 | 8,85% |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | Momentum / breakout V3 Filtered | €10.145,12 | €145,12 | 44 | 44 | 45,45% | 1,20 | €3,30 | 2,91% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.138,40 | €138,40 | 5 | 5 | 80,00% | 3,42 | €27,68 | 0,85% |
| TEST | 1H Balanced Short Trend Down Strict V1 | Confluenza trend | €10.115,05 | €104,33 | 11 | 11 | 36,36% | 1,53 | €9,48 | 1,80% |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | Momentum / breakout V3 Filtered | €10.099,04 | €99,04 | 55 | 55 | 54,55% | 1,12 | €1,80 | 3,59% |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | Momentum / breakout | €10.091,00 | €29,75 | 83 | 82 | 46,99% | 1,01 | €0,36 | 5,23% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €10.086,98 | €86,98 | 1 | 1 | 100,00% | ∞ | €86,98 | 0,40% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.084,12 | €84,12 | 1 | 1 | 100,00% | ∞ | €84,12 | 0,30% |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | Momentum / breakout V3 Filtered | €10.048,77 | €48,77 | 23 | 23 | 43,48% | 1,12 | €2,12 | 3,05% |
| TEST | Rapida 1H V1 | Momentum / breakout | €10.043,28 | €43,28 | 78 | 78 | 34,62% | 1,02 | €0,55 | 6,76% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €10.039,30 | €39,30 | 6 | 6 | 50,00% | 1,24 | €6,55 | 1,89% |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | Momentum / breakout | €10.032,43 | €32,43 | 29 | 29 | 37,93% | 1,05 | €1,12 | 2,27% |
| TEST | Scalp RSI Long 20 · prudente · 5x | Inversione RSI estrema 15m | €10.028,67 | €28,67 | 9 | 9 | 55,56% | 1,80 | €3,19 | 0,36% |
| TEST | 1H Fast V3 Cap75 V1 | Momentum / breakout V3 Filtered | €10.013,99 | €18,81 | 118 | 118 | 40,68% | 1,01 | €0,16 | 6,72% |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | Momentum / breakout | €10.011,37 | €11,94 | 78 | 78 | 42,31% | 1,01 | €0,15 | 6,52% |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | Momentum / breakout V3 Filtered | €10.008,92 | €8,92 | 30 | 30 | 36,67% | 1,02 | €0,30 | 4,84% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €10.007,98 | €7,98 | 24 | 24 | 45,83% | 1,09 | €0,33 | 0,33% |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | Momentum / breakout V3 Filtered | €10.003,37 | €3,37 | 8 | 8 | 37,50% | 1,02 | €0,42 | 2,15% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €10.001,60 | €1,60 | 24 | 24 | 45,83% | 1,09 | €0,07 | 0,07% |
| TEST | Scalp RSI Short 85 · €50 · 15x | Inversione RSI estrema 15m | €10.001,42 | €1,42 | 3 | 3 | 66,67% | 2,74 | €0,47 | 0,08% |
| TEST | Scalp RSI Short 85 · €10 · 15x | Inversione RSI estrema 15m | €10.000,28 | €0,28 | 3 | 3 | 66,67% | 2,74 | €0,09 | 0,02% |
| TEST | Scanner Bottom5 Short Continuation V1 | Scanner Bottom5 Short Continuation | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 85 · prudente · 5x | Inversione RSI estrema 15m | €9.999,47 | €-0,53 | 3 | 3 | 66,67% | 0,77 | €-0,18 | 0,16% |
| TEST | Scalp RSI Long 20 · €10 · 15x | Inversione RSI estrema 15m | €9.999,33 | €-0,67 | 9 | 9 | 44,44% | 0,85 | €-0,07 | 0,04% |
| TEST | Doge Ema 1H | Trend following EMA | €9.999,04 | €-15,39 | 12 | 12 | 58,33% | 0,94 | €-1,28 | 2,10% |
| TEST | Scalp RSI Long 15 · €10 · 15x | Inversione RSI estrema 15m | €9.997,60 | €-2,40 | 3 | 3 | 33,33% | 0,13 | €-0,80 | 0,02% |
| TEST | Scalp RSI Long 20 · €50 · 15x | Inversione RSI estrema 15m | €9.996,64 | €-3,36 | 9 | 9 | 44,44% | 0,85 | €-0,37 | 0,21% |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | Momentum / breakout V3 Filtered | €9.995,23 | €-4,77 | 15 | 15 | 46,67% | 0,99 | €-0,32 | 2,70% |
| TEST | Scalp RSI Short 80 · €10 · 15x | Inversione RSI estrema 15m | €9.994,61 | €-5,39 | 12 | 12 | 33,33% | 0,40 | €-0,45 | 0,11% |
| TEST | Scalp RSI Long 25 · €10 · 15x | Inversione RSI estrema 15m | €9.990,45 | €-9,55 | 15 | 15 | 40,00% | 0,36 | €-0,64 | 0,14% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €9.988,31 | €-11,69 | 5 | 5 | 60,00% | 0,89 | €-2,34 | 1,13% |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | €9.988,00 | €-12,00 | 3 | 3 | 33,33% | 0,13 | €-4,00 | 0,12% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €9.987,48 | €-12,52 | 15 | 15 | 40,00% | 0,83 | €-0,83 | 0,71% |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | €9.980,94 | €-19,06 | 3 | 3 | 33,33% | 0,19 | €-6,35 | 0,20% |
| TEST | Ampia 4H | Confluenza trend | €9.977,89 | €-46,73 | 37 | 37 | 24,32% | 0,95 | €-1,26 | 4,45% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €9.975,30 | €-24,70 | 6 | 6 | 50,00% | 0,85 | €-4,12 | 1,89% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €9.973,77 | €-26,23 | 7 | 7 | 57,14% | 0,84 | €-3,75 | 1,49% |
| TEST | Scalp RSI Short 80 · €50 · 15x | Inversione RSI estrema 15m | €9.973,06 | €-26,94 | 12 | 12 | 33,33% | 0,40 | €-2,25 | 0,53% |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | Scanner Top 5 + forza BTC | €9.968,72 | €-31,28 | 10 | 10 | 30,00% | 0,87 | €-3,13 | 2,84% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €9.959,49 | €-40,51 | 2 | 2 | 50,00% | 0,28 | €-20,26 | 0,91% |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | €9.952,25 | €-47,75 | 15 | 15 | 40,00% | 0,36 | €-3,18 | 0,72% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €9.949,62 | €-50,38 | 1 | 1 | 0,00% | 0,00 | €-50,38 | 0,74% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €9.931,19 | €-68,81 | 3 | 3 | 33,33% | 0,35 | €-22,94 | 0,87% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.931,14 | €-68,86 | 24 | 24 | 45,83% | 0,47 | €-2,87 | 0,84% |
| TEST | Btc Ema 4H | Trend following EMA | €9.929,52 | €-49,32 | 1 | 1 | 0,00% | 0,00 | €-49,32 | 1,28% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €9.928,55 | €-71,45 | 3 | 3 | 33,33% | 0,32 | €-23,82 | 0,84% |
| TEST | Scalp RSI Short 80 · prudente · 5x | Inversione RSI estrema 15m | €9.926,30 | €-73,70 | 12 | 12 | 33,33% | 0,12 | €-6,14 | 0,89% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €9.919,03 | €-61,85 | 100 | 100 | 38,00% | 0,97 | €-0,62 | 7,25% |
| TEST | Combo Adaptive Side Regime Guard V1 | Combo Adaptive | €9.902,77 | €-112,57 | 58 | 58 | 41,38% | 0,91 | €-1,94 | 6,97% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €9.894,47 | €-105,53 | 10 | 10 | 50,00% | 0,62 | €-10,55 | 2,13% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €9.875,62 | €-124,38 | 8 | 8 | 37,50% | 0,49 | €-15,55 | 2,74% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €9.871,52 | €-101,74 | 2 | 2 | 0,00% | 0,00 | €-50,87 | 1,86% |
| TEST | Btc Ema 1H | Trend following EMA | €9.848,58 | €-151,42 | 9 | 9 | 33,33% | 0,53 | €-16,82 | 1,72% |
| TEST | Eth Ema 4H | Trend following EMA | €9.842,00 | €-158,00 | 3 | 3 | 0,00% | 0,00 | €-52,67 | 1,73% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €9.838,66 | €-161,34 | 31 | 28 | 38,71% | 0,80 | €-5,20 | 3,89% |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | Momentum / breakout V3 Filtered | €9.837,38 | €-162,62 | 37 | 37 | 40,54% | 0,76 | €-4,40 | 3,08% |
| TEST | Combo Adaptive | Combo Adaptive | €9.825,19 | €-163,51 | 83 | 83 | 38,55% | 0,90 | €-1,97 | 5,40% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | Momentum / breakout V3 Filtered | €9.817,34 | €-182,66 | 24 | 24 | 41,67% | 0,64 | €-7,61 | 3,23% |
| TEST | Scanner Bottom10 Short | Scanner Bottom10 Short | €9.815,06 | €-196,29 | 61 | 61 | 34,43% | 0,86 | €-3,22 | 5,27% |
| TEST | Scanner Bottom15 Short | Scanner Bottom15 Short | €9.815,06 | €-196,29 | 61 | 61 | 34,43% | 0,86 | €-3,22 | 5,27% |
| TEST | Scanner Bottom20 Short | Scanner Bottom20 Short | €9.815,06 | €-196,29 | 61 | 61 | 34,43% | 0,86 | €-3,22 | 5,27% |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | Momentum / breakout V3 Filtered | €9.811,70 | €-188,30 | 38 | 38 | 44,74% | 0,80 | €-4,96 | 4,50% |
| TEST | Combo Adaptive Regime V1 | Combo Adaptive | €9.805,38 | €-192,61 | 32 | 32 | 40,62% | 0,75 | €-6,02 | 3,91% |
| TEST | Sol Ema 4H | Trend following EMA | €9.792,72 | €-207,28 | 4 | 4 | 0,00% | 0,00 | €-51,82 | 2,10% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.762,69 | €-237,31 | 7 | 7 | 14,29% | 0,28 | €-33,90 | 2,60% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | Momentum / breakout V3 Filtered | €9.762,18 | €-237,82 | 7 | 7 | 14,29% | 0,02 | €-33,97 | 2,82% |
| TEST | Sol Ema 1H | Trend following EMA | €9.760,52 | €-239,48 | 9 | 9 | 22,22% | 0,37 | €-26,61 | 3,16% |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | Scanner Bottom 5 Short | €9.746,63 | €-264,94 | 53 | 53 | 33,96% | 0,78 | €-5,00 | 5,27% |
| TEST | Scanner Bottom5 Short Profit Lock V1 | Scanner Bottom 5 Short | €9.731,81 | €-279,75 | 54 | 54 | 33,33% | 0,75 | €-5,18 | 5,27% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | Momentum / breakout V3 Filtered | €9.723,72 | €-276,28 | 31 | 31 | 32,26% | 0,62 | €-8,91 | 4,83% |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | Combo Adaptive | €9.720,12 | €-282,28 | 22 | 22 | 36,36% | 0,63 | €-12,83 | 4,21% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €9.720,09 | €-279,91 | 34 | 34 | 41,18% | 0,74 | €-8,23 | 5,09% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.692,38 | €-307,62 | 8 | 8 | 25,00% | 0,05 | €-38,45 | 3,11% |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | Momentum / breakout V3 Filtered | €9.690,60 | €-326,79 | 106 | 105 | 44,34% | 0,84 | €-3,08 | 7,17% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.689,94 | €-322,64 | 15 | 15 | 26,67% | 0,35 | €-21,51 | 3,53% |
| TEST | 1H Fast V3 Nohigh V1 | Momentum / breakout V3 Filtered | €9.668,04 | €-331,57 | 104 | 104 | 42,31% | 0,87 | €-3,19 | 6,10% |
| TEST | 1H Fast Tp2 V1 | Momentum / breakout | €9.667,61 | €-399,79 | 142 | 141 | 35,21% | 0,87 | €-2,82 | 4,95% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.656,92 | €-354,55 | 81 | 81 | 33,33% | 0,79 | €-4,38 | 6,41% |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | Momentum / breakout V3 Filtered | €9.630,78 | €-368,87 | 72 | 72 | 40,28% | 0,81 | €-5,12 | 5,23% |
| TEST | Rapida 1H V3 Filtered | Momentum / breakout V3 Filtered | €9.627,28 | €-390,00 | 150 | 149 | 37,33% | 0,87 | €-2,60 | 7,14% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €9.621,05 | €-378,95 | 10 | 10 | 20,00% | 0,15 | €-37,89 | 4,47% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €9.608,24 | €-392,25 | 78 | 75 | 39,74% | 0,85 | €-5,03 | 8,11% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €9.600,79 | €-386,92 | 70 | 64 | 41,43% | 0,77 | €-5,53 | 7,26% |
| TEST | Combo Adaptive Quality7 Regime V1 | Combo Adaptive | €9.597,86 | €-404,51 | 22 | 22 | 27,27% | 0,48 | €-18,39 | 5,41% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | Momentum / breakout V3 Filtered | €9.579,83 | €-420,17 | 11 | 11 | 0,00% | 0,00 | €-38,20 | 4,20% |
| TEST | Combo Adaptive Long Only V1 | Combo Adaptive | €9.570,12 | €-446,93 | 49 | 49 | 36,73% | 0,66 | €-9,12 | 5,16% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €9.564,42 | €-435,33 | 73 | 73 | 42,47% | 0,78 | €-5,96 | 6,55% |
| TEST | 1H Fast V3 No Esports Long Only V1 | Momentum / breakout V3 Filtered | €9.556,73 | €-455,22 | 70 | 70 | 34,29% | 0,74 | €-6,50 | 8,59% |
| TEST | Eth Ema 1H | Trend following EMA | €9.526,32 | €-451,30 | 11 | 11 | 18,18% | 0,11 | €-41,03 | 4,80% |
| TEST | Combo Adaptive Quality7 V1 | Combo Adaptive | €9.515,13 | €-484,87 | 46 | 46 | 30,43% | 0,64 | €-10,54 | 7,10% |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | Momentum / breakout V3 Filtered | €9.508,14 | €-564,16 | 75 | 75 | 44,00% | 0,75 | €-7,52 | 6,85% |
| TEST | Master Adaptive Gb20 Be V1 | Master Adaptive Consensus | €9.502,15 | €-528,84 | 46 | 46 | 26,09% | 0,62 | €-11,50 | 8,39% |
| TEST | Master Adaptive Gb20 Partial V1 | Master Adaptive Consensus | €9.492,04 | €-538,91 | 41 | 41 | 31,71% | 0,60 | €-13,14 | 7,98% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €9.488,34 | €-559,67 | 47 | 47 | 31,91% | 0,67 | €-11,91 | 6,80% |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | Scanner Top 5 + forza BTC | €9.480,20 | €-550,50 | 50 | 50 | 36,00% | 0,66 | €-11,01 | 7,74% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €9.471,36 | €-543,27 | 50 | 50 | 34,00% | 0,68 | €-10,87 | 6,90% |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | €9.455,33 | €-575,51 | 43 | 43 | 30,23% | 0,62 | €-13,38 | 7,80% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €9.445,03 | €-562,34 | 69 | 69 | 36,23% | 0,70 | €-8,15 | 11,27% |
| TEST | Combo Adaptive Partial 1R V1 | Combo Adaptive | €9.434,59 | €-554,55 | 84 | 84 | 36,90% | 0,68 | €-6,60 | 6,20% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €9.417,72 | €-638,09 | 42 | 42 | 26,19% | 0,59 | €-15,19 | 8,18% |
| TEST | 1H Fast V3 No Esports V1 | Momentum / breakout V3 Filtered | €9.412,32 | €-654,02 | 124 | 123 | 37,10% | 0,76 | €-5,27 | 7,03% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €9.398,92 | €-610,53 | 114 | 114 | 38,60% | 0,75 | €-5,36 | 11,66% |
| TEST | 1H Balanced V3 Long Only V1 | Confluenza trend V3 Filtered | €9.381,81 | €-600,10 | 56 | 56 | 33,93% | 0,52 | €-10,72 | 6,98% |
| TEST | Scanner Top5 Btc Guard V1 | Scanner Top 5 + forza BTC | €9.365,15 | €-665,17 | 55 | 55 | 32,73% | 0,62 | €-12,09 | 7,34% |
| TEST | 1H Balanced Long No Rhv V1 | Confluenza trend | €9.330,79 | €-669,24 | 48 | 48 | 33,33% | 0,58 | €-13,94 | 9,05% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €9.329,70 | €-700,73 | 78 | 78 | 48,72% | 0,59 | €-8,98 | 9,02% |
| TEST | Scanner Top10 Long | Scanner Top10 Long | €9.322,38 | €-680,88 | 49 | 49 | 34,69% | 0,53 | €-13,90 | 10,31% |
| TEST | Scanner Top15 Long | Scanner Top15 Long | €9.322,38 | €-680,88 | 49 | 49 | 34,69% | 0,53 | €-13,90 | 10,31% |
| TEST | Scanner Top20 Long | Scanner Top20 Long | €9.322,38 | €-680,88 | 49 | 49 | 34,69% | 0,53 | €-13,90 | 10,31% |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | Scanner Top 5 + forza BTC | €9.317,55 | €-712,63 | 65 | 65 | 36,92% | 0,63 | €-10,96 | 7,02% |
| TEST | Combo Trend | Combo Trend | €9.264,10 | €-765,22 | 110 | 110 | 33,64% | 0,75 | €-6,96 | 9,82% |
| TEST | Combo Adaptive Runner25 V1 | Combo Adaptive | €9.223,42 | €-782,06 | 87 | 87 | 33,33% | 0,60 | €-8,99 | 10,14% |
| TEST | Master Adaptive Gb20 Loss Cap V1 | Master Adaptive Consensus | €9.148,58 | €-872,67 | 33 | 33 | 18,18% | 0,37 | €-26,44 | 11,09% |
| TEST | Scanner Top5 Btc Guard Mfe V1 | Scanner Top 5 + forza BTC | €9.147,35 | €-882,27 | 72 | 72 | 36,11% | 0,58 | €-12,25 | 8,78% |
| TEST | Scanner Top5 Btc Tp3 V1 | Scanner Top 5 + forza BTC | €9.132,44 | €-876,59 | 54 | 54 | 31,48% | 0,49 | €-16,23 | 11,61% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.131,75 | €-848,62 | 76 | 76 | 28,95% | 0,54 | €-11,17 | 9,53% |
| TEST | Scanner Top5 Btc Runner25 V1 | Scanner Top 5 + forza BTC | €9.127,09 | €-881,93 | 58 | 58 | 32,76% | 0,49 | €-15,21 | 11,90% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €9.106,10 | €-913,48 | 47 | 47 | 27,66% | 0,57 | €-19,44 | 11,51% |
| TEST | 1H Fast V3 Long Only V1 | Momentum / breakout V3 Filtered | €9.099,05 | €-912,33 | 90 | 90 | 28,89% | 0,62 | €-10,14 | 10,56% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €9.089,95 | €-909,05 | 94 | 94 | 29,79% | 0,61 | €-9,67 | 11,15% |
| TEST | Combo Scanner | Combo Scanner | €9.063,75 | €-948,24 | 74 | 74 | 35,14% | 0,58 | €-12,81 | 11,38% |
| TEST | Combo Adaptive Tp3 V1 | Combo Adaptive | €9.051,11 | €-954,26 | 68 | 68 | 32,35% | 0,43 | €-14,03 | 10,14% |
| TEST | Scanner Top5 Btc Btc Le3 V1 | Scanner Top 5 + forza BTC | €9.025,67 | €-981,37 | 50 | 50 | 32,00% | 0,39 | €-19,63 | 11,72% |
| TEST | Scanner Top5 Btc Mfe V1 | Scanner Top 5 + forza BTC | €8.853,35 | €-1.153,56 | 62 | 62 | 32,26% | 0,32 | €-18,61 | 12,28% |
| TEST | Combo Adaptive Mfe Trail | Combo Adaptive | €8.747,34 | €-1.242,21 | 94 | 94 | 31,91% | 0,44 | €-13,21 | 12,57% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | XRP | SHORT | Confluenza trend | 240m | 3,0x | 1,01047 | 0,99491 | 1,03352 | 1,34224 | 0,96437 | €711,84 | €2.135,52 | €48,72 | €32,88 |
| Principale 4H | SPCX | LONG | Confluenza trend | 240m | 3,0x | 136,56189 | 136,56189 | 128,79610 | 91,72407 | 152,09346 | €285,50 | €856,50 | €48,71 | €0,00 |
| Principale 4H | VELVET | LONG | Confluenza trend | 240m | 3,0x | 0,55987 | 0,55987 | 0,49269 | 0,37605 | 0,69424 | €131,08 | €393,24 | €47,19 | €0,00 |
| Principale 4H | EDEN | LONG | Confluenza trend | 240m | 3,0x | 0,06195 | 0,06195 | 0,05451 | 0,04161 | 0,07681 | €130,34 | €391,02 | €46,92 | €0,00 |
| Principale 4H | DOGE | SHORT | Confluenza trend | 240m | 3,0x | 0,06958 | 0,06988 | 0,07069 | 0,09242 | 0,06735 | €11,27 | €33,82 | €0,54 | €-0,15 |
| Bilanciata 1H V1 | CYS | SHORT | Confluenza trend | 60m | 3,0x | 0,76314 | 0,76314 | 0,70300 | 1,01371 | 0,57999 | €135,05 | €405,16 | €0,00 | €-0,00 |
| Bilanciata 1H V1 | ETH | SHORT | Confluenza trend | 60m | 3,0x | 1889,17209 | 1895,77000 | 1916,37617 | 2509,45026 | 1834,76393 | €43,74 | €131,21 | €1,89 | €-0,46 |
| Bilanciata 1H V1 | PEPE | SHORT | Confluenza trend | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €34,93 | €104,79 | €1,51 | €-0,00 |
| Bilanciata 1H V1 | GPS | LONG | Confluenza trend | 60m | 3,0x | 0,01630 | 0,01662 | 0,01445 | 0,01095 | 0,02000 | €133,98 | €401,93 | €45,63 | €7,90 |
| Bilanciata 1H V1 | DOGE | SHORT | Confluenza trend | 60m | 3,0x | 0,06998 | 0,06988 | 0,07099 | 0,09295 | 0,06796 | €1.095,91 | €3.287,73 | €47,34 | €4,60 |
| 1H Balanced Long No Rhv V1 | XOM | LONG | Confluenza trend | 60m | 3,0x | 160,24609 | 160,24609 | 157,58464 | 107,63196 | 165,56900 | €952,03 | €2.856,08 | €47,44 | €0,00 |
| 1H Balanced Long No Rhv V1 | CAP | LONG | Confluenza trend | 60m | 3,0x | 0,06539 | 0,06539 | 0,05754 | 0,04392 | 0,08108 | €121,21 | €363,62 | €43,63 | €0,00 |
| 1H Balanced Long No Rhv V1 | AKE | LONG | Confluenza trend | 60m | 3,0x | 0,01042 | 0,01042 | 0,00943 | 0,00700 | 0,01242 | €161,02 | €483,05 | €46,21 | €0,00 |
| 1H Balanced Long No Rhv V1 | ZEC | LONG | Confluenza trend | 60m | 3,0x | 512,07239 | 510,22000 | 503,16526 | 343,94196 | 529,88667 | €65,27 | €195,80 | €3,41 | €-0,71 |
| 1H Balanced Long No Rhv V1 | GPS | LONG | Confluenza trend | 60m | 3,0x | 0,01658 | 0,01662 | 0,01459 | 0,01114 | 0,02056 | €127,57 | €382,70 | €45,92 | €0,85 |
| 1H Balanced Short Trend Down Strict V1 | DOGE | SHORT | Confluenza trend | 60m | 3,0x | 0,07014 | 0,06988 | 0,07115 | 0,09316 | 0,06812 | €1.155,95 | €3.467,86 | €49,94 | €12,66 |
| 1H Balanced Short Trend Down Strict V1 | XRP | SHORT | Confluenza trend | 60m | 3,0x | 0,99419 | 0,99491 | 1,00851 | 1,32062 | 0,96556 | €1.170,75 | €3.512,25 | €50,58 | €-2,53 |
| Bilanciata 1H V2 | AKE | LONG | Confluenza trend V2 | 60m | 3,0x | 0,01007 | 0,01007 | 0,00886 | 0,00676 | 0,01249 | €135,82 | €407,45 | €48,89 | €0,00 |
| Bilanciata 1H V2 | CYS | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,73666 | 0,73666 | 0,70420 | 0,97853 | 0,55986 | €127,95 | €383,85 | €0,00 | €-0,00 |
| Bilanciata 1H V2 | ZEC | LONG | Confluenza trend V2 | 60m | 3,0x | 512,07239 | 510,22000 | 503,16526 | 343,94196 | 529,88667 | €925,85 | €2.777,56 | €48,31 | €-10,05 |
| Bilanciata 1H V3 Filtered | DOGE | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,06964 | 0,06988 | 0,07064 | 0,09250 | 0,06763 | €14,62 | €43,87 | €0,63 | €-0,15 |
| Bilanciata 1H V3 Filtered | XRP | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,99900 | 0,99491 | 1,01339 | 1,32701 | 0,97023 | €49,41 | €148,23 | €2,13 | €0,61 |
| Bilanciata 1H V3 Filtered | PEPE | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.164,76 | €3.494,29 | €50,32 | €-0,00 |
| Bilanciata 1H V3 Filtered | ZEC | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 514,86295 | 510,22000 | 506,12617 | 345,81628 | 532,33652 | €992,76 | €2.978,27 | €50,54 | €-26,86 |
| Bilanciata 1H V3 Filtered | GPS | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,01624 | 0,01662 | 0,01431 | 0,01091 | 0,02011 | €141,49 | €424,46 | €50,53 | €9,94 |
| Bilanciata 1H V3 Filtered | HYPE | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 59,29886 | 59,36900 | 58,44495 | 39,82907 | 61,00666 | €1.026,23 | €3.078,69 | €44,33 | €3,64 |
| 1H Fast Score 6 75 V1 | APR | SHORT | Momentum / breakout | 60m | 3,0x | 0,15465 | 0,15465 | 0,17320 | 0,20542 | 0,12681 | €144,97 | €434,90 | €52,19 | €-0,00 |
| 1H Fast Score 6 75 V1 | PEPE | SHORT | Momentum / breakout | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.575,03 | €4.725,08 | €52,92 | €-0,00 |
| 1H Fast Score 6 75 V1 | GPS | LONG | Momentum / breakout | 60m | 3,0x | 0,01666 | 0,01662 | 0,01524 | 0,01119 | 0,01879 | €201,11 | €603,33 | €51,36 | €-1,45 |
| 1H Fast Score 6 75 V1 | XRP | SHORT | Momentum / breakout | 60m | 3,0x | 0,99556 | 0,99491 | 1,00671 | 1,32244 | 0,97884 | €1.521,02 | €4.563,07 | €51,11 | €2,98 |
| 1H Fast Score 6 75 No Trend Up V1 | APR | SHORT | Momentum / breakout | 60m | 3,0x | 0,15465 | 0,15465 | 0,17320 | 0,20542 | 0,12681 | €141,11 | €423,34 | €50,80 | €-0,00 |
| 1H Fast Score 6 75 No Trend Up V1 | PEPE | SHORT | Momentum / breakout | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.533,15 | €4.599,45 | €51,51 | €-0,00 |
| 1H Fast Score 6 75 No Trend Up V1 | GPS | LONG | Momentum / breakout | 60m | 3,0x | 0,01666 | 0,01662 | 0,01524 | 0,01119 | 0,01879 | €195,76 | €587,29 | €49,99 | €-1,41 |
| 1H Fast Score 6 75 No Trend Up V1 | XRP | SHORT | Momentum / breakout | 60m | 3,0x | 0,99556 | 0,99491 | 1,00671 | 1,32244 | 0,97884 | €1.480,58 | €4.441,75 | €49,75 | €2,90 |
| 1H Fast Score 6 75 Range Only V1 | CYS | SHORT | Momentum / breakout | 60m | 3,0x | 0,73666 | 0,73666 | 0,69266 | 0,97853 | 0,60406 | €143,00 | €428,99 | €0,00 | €-0,00 |
| 1H Fast Score 6 75 Range Only V1 | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,01019 | 0,01019 | 0,00946 | 0,00684 | 0,01127 | €243,23 | €729,68 | €51,78 | €0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | XRP | SHORT | Momentum / breakout | 60m | 3,0x | 0,99556 | 0,99491 | 1,00671 | 1,32244 | 0,97884 | €1.578,12 | €4.734,36 | €53,02 | €3,10 |
| 1H Fast Score 6 75 Cost Aware V1 | GPS | LONG | Momentum / breakout | 60m | 3,0x | 0,01704 | 0,01662 | 0,01547 | 0,01145 | 0,01940 | €191,76 | €575,28 | €53,13 | €-14,29 |
| 1H Fast Nohigh Cap75 V1 | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,01003 | 0,01003 | 0,00915 | 0,00674 | 0,01134 | €189,64 | €568,93 | €49,82 | €0,00 |
| 1H Fast No Pepe V1 | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,01019 | 0,01019 | 0,00946 | 0,00684 | 0,01127 | €9,63 | €28,88 | €2,05 | €0,00 |
| 1H Fast No Pepe V1 | GPS | LONG | Momentum / breakout | 60m | 3,0x | 0,01624 | 0,01662 | 0,01624 | 0,01091 | 0,01850 | €187,17 | €561,52 | €0,00 | €13,15 |
| 1H Fast Tp2 V1 | PEPE | SHORT | Momentum / breakout | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €115,44 | €346,32 | €3,88 | €-0,00 |
| 1H Fast Tp2 V1 | GPS | LONG | Momentum / breakout | 60m | 3,0x | 0,01624 | 0,01662 | 0,01624 | 0,01091 | 0,01925 | €164,28 | €492,85 | €0,00 | €11,54 |
| Rapida 1H V3 Filtered | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01042 | 0,01042 | 0,00965 | 0,00700 | 0,01159 | €11,81 | €35,44 | €2,64 | €0,00 |
| Rapida 1H V3 Filtered | PEPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €24,35 | €73,04 | €0,82 | €-0,00 |
| Rapida 1H V3 Filtered | GPS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01624 | 0,01662 | 0,01624 | 0,01091 | 0,01850 | €176,73 | €530,19 | €0,00 | €12,41 |
| Rapida 1H V3 Filtered | BTW | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,35651 | 0,35651 | 0,32568 | 0,23946 | 0,40276 | €154,24 | €462,73 | €40,02 | €0,00 |
| 1H Fast V3 Cap75 V1 | APR | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,15465 | 0,15465 | 0,17320 | 0,20542 | 0,12681 | €136,16 | €408,49 | €49,02 | €-0,00 |
| 1H Fast V3 Cap75 V1 | PEPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.494,66 | €4.483,99 | €50,22 | €-0,00 |
| 1H Fast V3 Cap75 V1 | GPS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01666 | 0,01662 | 0,01524 | 0,01119 | 0,01879 | €195,87 | €587,61 | €50,02 | €-1,41 |
| 1H Fast V3 Cap75 V1 | XRP | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,99556 | 0,99491 | 1,00671 | 1,32244 | 0,97884 | €1.491,98 | €4.475,94 | €50,13 | €2,93 |
| 1H Fast V3 Cap75 V1 | DOGE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,06970 | 0,06988 | 0,07048 | 0,09258 | 0,06853 | €37,09 | €111,27 | €1,25 | €-0,29 |
| 1H Fast V3 Nohigh V1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01042 | 0,01042 | 0,00965 | 0,00700 | 0,01159 | €215,12 | €645,36 | €48,02 | €0,00 |
| 1H Fast V3 Long Only V1 | GPS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01624 | 0,01662 | 0,01624 | 0,01091 | 0,01850 | €166,02 | €498,07 | €0,00 | €11,66 |
| 1H Fast V3 Long Nohigh Cap75 V1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00999 | 0,00999 | 0,00922 | 0,00671 | 0,01113 | €196,64 | €589,91 | €45,15 | €0,00 |
| 1H Fast V3 No Esports V1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01042 | 0,01042 | 0,00965 | 0,00700 | 0,01159 | €10,40 | €31,21 | €2,32 | €0,00 |
| 1H Fast V3 No Esports V1 | PEPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €18,35 | €55,04 | €0,62 | €-0,00 |
| 1H Fast V3 No Esports V1 | GPS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01624 | 0,01662 | 0,01624 | 0,01091 | 0,01850 | €172,70 | €518,09 | €0,00 | €12,13 |
| 1H Fast V3 No Esports Long Only V1 | GPS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01624 | 0,01662 | 0,01624 | 0,01091 | 0,01850 | €174,37 | €523,12 | €0,00 | €12,25 |
| 1H Fast V3 No Esports Mfe Lock V1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01042 | 0,01042 | 0,00965 | 0,00700 | 0,01159 | €11,89 | €35,67 | €2,65 | €0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | PEPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €24,51 | €73,52 | €0,82 | €-0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | GPS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01624 | 0,01662 | 0,01624 | 0,01091 | 0,01850 | €177,89 | €533,68 | €0,00 | €12,50 |
| 1H Fast V3 No Esports Mfe Lock V1 | BTW | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,35651 | 0,35651 | 0,32568 | 0,23946 | 0,40276 | €155,26 | €465,77 | €40,28 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | LINK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 9,38563 | 9,38563 | 9,22869 | 6,30401 | 9,62103 | €949,50 | €2.848,50 | €47,63 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1889,64785 | 1895,77000 | 1868,48380 | 1269,21348 | 1921,39394 | €1.413,33 | €4.239,98 | €47,49 | €13,74 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00999 | 0,00999 | 0,00922 | 0,00671 | 0,01113 | €195,47 | €586,41 | €44,88 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | HYPE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 58,91378 | 59,36900 | 58,25395 | 39,57042 | 59,90353 | €33,51 | €100,52 | €1,13 | €0,78 |
| Ampia 4H | XRP | SHORT | Confluenza trend | 240m | 2,0x | 1,01047 | 0,99491 | 1,04043 | 1,51065 | 0,92656 | €831,51 | €1.663,02 | €49,32 | €25,60 |
| Ampia 4H | SPCX | LONG | Confluenza trend | 240m | 2,0x | 136,56189 | 136,56189 | 126,46637 | 68,96375 | 164,82935 | €323,86 | €647,73 | €47,88 | €0,00 |
| Ampia 4H | VELVET | LONG | Confluenza trend | 240m | 2,0x | 0,55987 | 0,55987 | 0,49269 | 0,28274 | 0,74799 | €201,63 | €403,26 | €48,39 | €0,00 |
| Ampia 4H | BTC | SHORT | Confluenza trend | 240m | 2,0x | 63404,51656 | 64182,18000 | 64723,33050 | 94789,75226 | 59711,83752 | €59,90 | €119,81 | €2,49 | €-1,47 |
| Ampia 4H | DOGE | SHORT | Confluenza trend | 240m | 2,0x | 0,06958 | 0,06988 | 0,07103 | 0,10402 | 0,06553 | €38,05 | €76,11 | €1,58 | €-0,33 |
| Ampia 4H | BTW | LONG | Confluenza trend | 240m | 2,0x | 0,32695 | 0,32695 | 0,28771 | 0,16511 | 0,43680 | €207,21 | €414,42 | €49,73 | €0,00 |
| Forza relativa 1H V1 | ADA | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17946 | €1.677,78 | €3.355,57 | €48,32 | €-0,00 |
| Forza relativa 1H V1 | PEPE | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €16,88 | €33,76 | €0,49 | €-0,00 |
| Forza relativa 1H V1 | GPS | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,01630 | 0,01662 | 0,01445 | 0,00823 | 0,02037 | €177,71 | €355,43 | €40,35 | €6,98 |
| Forza relativa 1H V1 | HYPE | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 59,44389 | 59,36900 | 58,58789 | 30,01916 | 61,32707 | €1.587,77 | €3.175,54 | €45,73 | €-4,00 |
| Forza relativa 1H V1 | XRP | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,99556 | 0,99491 | 1,00990 | 1,48836 | 0,96402 | €1.577,31 | €3.154,62 | €45,43 | €2,06 |
| Forza relativa 1H V2 | ADA | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,18533 | 0,18533 | 0,18800 | 0,27707 | 0,17946 | €1.698,68 | €3.397,35 | €48,92 | €-0,00 |
| Forza relativa 1H V2 | GPS | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,01652 | 0,01662 | 0,01483 | 0,00834 | 0,02024 | €231,94 | €463,89 | €47,46 | €2,81 |
| Benchmark Donchian breakout 1H | PEPE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.304,34 | €2.608,68 | €0,00 | €-0,00 |
| Benchmark Donchian breakout 1H | DOGE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,06952 | 0,06988 | 0,07063 | 0,10393 | 0,06674 | €1.669,15 | €3.338,30 | €53,41 | €-17,37 |
| Benchmark Donchian breakout 1H | HYPE | LONG | Donchian breakout 20 barre | 60m | 2,0x | 59,28285 | 59,36900 | 58,33433 | 29,93784 | 61,65417 | €1.599,80 | €3.199,61 | €51,19 | €4,65 |
| Donchian 1H Gb20 120R V1 | PEPE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.273,63 | €2.547,26 | €0,00 | €-0,00 |
| Donchian 1H Gb20 120R V1 | DOGE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,06952 | 0,06988 | 0,07063 | 0,10393 | 0,06674 | €1.629,85 | €3.259,70 | €52,16 | €-16,96 |
| Donchian 1H Gb20 120R V1 | HYPE | LONG | Donchian breakout 20 barre | 60m | 2,0x | 59,28285 | 59,36900 | 58,33433 | 29,93784 | 61,65417 | €1.562,14 | €3.124,27 | €49,99 | €4,54 |
| Benchmark Bollinger mean reversion 1H | H | LONG | Bollinger mean reversion | 60m | 2,0x | 0,10874 | 0,10874 | 0,10874 | 0,05491 | 0,12831 | €202,90 | €405,81 | €0,00 | €0,00 |
| Benchmark trend following EMA 1H | ADA | SHORT | Trend following EMA | 60m | 2,0x | 0,18533 | 0,18533 | 0,18829 | 0,27707 | 0,17881 | €28,20 | €56,39 | €0,90 | €-0,00 |
| Benchmark trend following EMA 1H | PEPE | SHORT | Trend following EMA | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.036,54 | €2.073,07 | €0,00 | €-0,00 |
| Benchmark trend following EMA 1H | DOGE | SHORT | Trend following EMA | 60m | 2,0x | 0,07014 | 0,06988 | 0,07126 | 0,10485 | 0,06767 | €23,05 | €46,10 | €0,74 | €0,17 |
| Benchmark trend following EMA 1H | XRP | SHORT | Trend following EMA | 60m | 2,0x | 0,99940 | 0,99491 | 1,01539 | 1,49410 | 0,96422 | €29,63 | €59,25 | €0,95 | €0,27 |
| Benchmark trend following EMA 1H | SOL | SHORT | Trend following EMA | 60m | 2,0x | 74,94501 | 75,79700 | 76,14413 | 112,04279 | 72,30694 | €1.248,89 | €2.497,78 | €39,96 | €-28,40 |
| Benchmark trend following EMA 1H | HYPE | LONG | Trend following EMA | 60m | 2,0x | 59,17783 | 59,36900 | 58,23099 | 29,88481 | 61,26089 | €74,07 | €148,13 | €2,37 | €0,48 |
| Benchmark trend following EMA 1H | ETH | LONG | Trend following EMA | 60m | 2,0x | 1911,30218 | 1895,77000 | 1880,72135 | 965,20760 | 1978,58002 | €44,44 | €88,89 | €1,42 | €-0,72 |
| Benchmark trend following EMA 1H | GPS | LONG | Trend following EMA | 60m | 2,0x | 0,01697 | 0,01662 | 0,01505 | 0,00857 | 0,02119 | €203,01 | €406,01 | €45,92 | €-8,38 |
| Benchmark trend following EMA 1H | BEAT | SHORT | Trend following EMA | 60m | 2,0x | 0,28257 | 0,26678 | 0,31648 | 0,42244 | 0,20797 | €186,11 | €372,23 | €44,67 | €20,80 |
| Scanner Top 5 Long 1H | XOM | LONG | Scanner Top 5 Long | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 165,56900 | €1.527,62 | €3.055,23 | €50,74 | €0,00 |
| Scanner Top 5 Long 1H | AKE | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01255 | €204,03 | €408,06 | €48,97 | €0,00 |
| Scanner Top 5 Long 1H | HYPE | LONG | Scanner Top 5 Long | 60m | 2,0x | 59,03881 | 59,36900 | 58,18865 | 29,81460 | 60,73912 | €1.703,71 | €3.407,43 | €49,07 | €19,06 |
| Scanner Top 5 Long 1H | GPS | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,01622 | 0,01662 | 0,01460 | 0,00819 | 0,01945 | €254,32 | €508,64 | €50,72 | €12,55 |
| Scanner Bottom 5 Short 1H | BEAT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,28257 | 0,26678 | 0,31648 | 0,42244 | 0,21475 | €200,95 | €401,89 | €48,23 | €22,46 |
| Scanner Bottom 5 Short 1H | DOGE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,06970 | 0,06988 | 0,07070 | 0,10420 | 0,06769 | €1.674,47 | €3.348,95 | €48,22 | €-8,74 |
| Scanner Top10 Long | XOM | LONG | Scanner Top10 Long | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 165,56900 | €1.407,05 | €2.814,11 | €46,74 | €0,00 |
| Scanner Top10 Long | AKE | LONG | Scanner Top10 Long | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01255 | €187,94 | €375,88 | €45,11 | €0,00 |
| Scanner Top10 Long | HYPE | LONG | Scanner Top10 Long | 60m | 2,0x | 59,03881 | 59,36900 | 58,18865 | 29,81460 | 60,73912 | €1.569,93 | €3.139,86 | €45,21 | €17,56 |
| Scanner Top10 Long | ETH | LONG | Scanner Top10 Long | 60m | 2,0x | 1911,30218 | 1895,77000 | 1883,77943 | 965,20760 | 1966,34769 | €34,09 | €68,19 | €0,98 | €-0,55 |
| Scanner Top10 Long | GPS | LONG | Scanner Top10 Long | 60m | 2,0x | 0,01697 | 0,01662 | 0,01524 | 0,00857 | 0,02043 | €228,91 | €457,83 | €46,60 | €-9,45 |
| Scanner Bottom10 Short | SOL | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 75,16396 | 75,79700 | 76,24633 | 112,37013 | 72,99924 | €17,20 | €34,40 | €0,50 | €-0,29 |
| Scanner Bottom10 Short | BEAT | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,28257 | 0,26678 | 0,31648 | 0,42244 | 0,21475 | €204,24 | €408,48 | €49,02 | €22,83 |
| Scanner Bottom10 Short | DOGE | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,06970 | 0,06988 | 0,07070 | 0,10420 | 0,06769 | €1.701,93 | €3.403,86 | €49,02 | €-8,88 |
| Scanner Top15 Long | XOM | LONG | Scanner Top15 Long | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 165,56900 | €1.407,05 | €2.814,11 | €46,74 | €0,00 |
| Scanner Top15 Long | AKE | LONG | Scanner Top15 Long | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01255 | €187,94 | €375,88 | €45,11 | €0,00 |
| Scanner Top15 Long | HYPE | LONG | Scanner Top15 Long | 60m | 2,0x | 59,03881 | 59,36900 | 58,18865 | 29,81460 | 60,73912 | €1.569,93 | €3.139,86 | €45,21 | €17,56 |
| Scanner Top15 Long | ETH | LONG | Scanner Top15 Long | 60m | 2,0x | 1911,30218 | 1895,77000 | 1883,77943 | 965,20760 | 1966,34769 | €34,09 | €68,19 | €0,98 | €-0,55 |
| Scanner Top15 Long | GPS | LONG | Scanner Top15 Long | 60m | 2,0x | 0,01697 | 0,01662 | 0,01524 | 0,00857 | 0,02043 | €228,91 | €457,83 | €46,60 | €-9,45 |
| Scanner Bottom15 Short | SOL | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 75,16396 | 75,79700 | 76,24633 | 112,37013 | 72,99924 | €17,20 | €34,40 | €0,50 | €-0,29 |
| Scanner Bottom15 Short | BEAT | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,28257 | 0,26678 | 0,31648 | 0,42244 | 0,21475 | €204,24 | €408,48 | €49,02 | €22,83 |
| Scanner Bottom15 Short | DOGE | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,06970 | 0,06988 | 0,07070 | 0,10420 | 0,06769 | €1.701,93 | €3.403,86 | €49,02 | €-8,88 |
| Scanner Top20 Long | XOM | LONG | Scanner Top20 Long | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 165,56900 | €1.407,05 | €2.814,11 | €46,74 | €0,00 |
| Scanner Top20 Long | AKE | LONG | Scanner Top20 Long | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01255 | €187,94 | €375,88 | €45,11 | €0,00 |
| Scanner Top20 Long | HYPE | LONG | Scanner Top20 Long | 60m | 2,0x | 59,03881 | 59,36900 | 58,18865 | 29,81460 | 60,73912 | €1.569,93 | €3.139,86 | €45,21 | €17,56 |
| Scanner Top20 Long | ETH | LONG | Scanner Top20 Long | 60m | 2,0x | 1911,30218 | 1895,77000 | 1883,77943 | 965,20760 | 1966,34769 | €34,09 | €68,19 | €0,98 | €-0,55 |
| Scanner Top20 Long | GPS | LONG | Scanner Top20 Long | 60m | 2,0x | 0,01697 | 0,01662 | 0,01524 | 0,00857 | 0,02043 | €228,91 | €457,83 | €46,60 | €-9,45 |
| Scanner Bottom20 Short | SOL | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 75,16396 | 75,79700 | 76,24633 | 112,37013 | 72,99924 | €17,20 | €34,40 | €0,50 | €-0,29 |
| Scanner Bottom20 Short | BEAT | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,28257 | 0,26678 | 0,31648 | 0,42244 | 0,21475 | €204,24 | €408,48 | €49,02 | €22,83 |
| Scanner Bottom20 Short | DOGE | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,06970 | 0,06988 | 0,07070 | 0,10420 | 0,06769 | €1.701,93 | €3.403,86 | €49,02 | €-8,88 |
| Scanner Top 5 + forza BTC 1H | XOM | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 166,10129 | €1.470,86 | €2.941,72 | €48,86 | €0,00 |
| Scanner Top 5 + forza BTC 1H | GPS | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01624 | 0,01662 | 0,01431 | 0,00820 | 0,02049 | €201,00 | €402,01 | €47,85 | €9,41 |
| Scanner Top 5 + forza BTC 1H | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 59,41588 | 59,36900 | 58,56029 | 30,00502 | 61,29818 | €15,47 | €30,93 | €0,45 | €-0,02 |
| Scanner Top5 Btc Mfe V1 | XOM | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 166,10129 | €1.378,72 | €2.757,43 | €45,80 | €0,00 |
| Scanner Top5 Btc Mfe V1 | GPS | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01624 | 0,01662 | 0,01431 | 0,00820 | 0,02049 | €188,41 | €376,82 | €44,86 | €8,82 |
| Scanner Top5 Btc Mfe V1 | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 59,41588 | 59,36900 | 58,56029 | 30,00502 | 61,29818 | €14,50 | €29,00 | €0,42 | €-0,02 |
| Scanner Top5 Btc Guard V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01279 | €196,77 | €393,54 | €47,23 | €0,00 |
| Scanner Top5 Btc Guard V1 | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 58,91378 | 59,36900 | 58,06542 | 29,75146 | 60,78017 | €1.519,74 | €3.039,48 | €43,77 | €23,49 |
| Scanner Top5 Btc Guard V1 | GPS | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01624 | 0,01662 | 0,01431 | 0,00820 | 0,02049 | €198,03 | €396,06 | €47,14 | €9,27 |
| Scanner Top5 Btc Btc Le3 V1 | XOM | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 166,10129 | €1.405,55 | €2.811,11 | €46,69 | €0,00 |
| Scanner Top5 Btc Btc Le3 V1 | GPS | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01624 | 0,01662 | 0,01431 | 0,00820 | 0,02049 | €192,08 | €384,16 | €45,73 | €9,00 |
| Scanner Top5 Btc Btc Le3 V1 | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 59,41588 | 59,36900 | 58,56029 | 30,00502 | 61,29818 | €14,78 | €29,56 | €0,43 | €-0,02 |
| Scanner Top5 Btc Guard Mfe V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01279 | €192,20 | €384,39 | €46,13 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 58,91378 | 59,36900 | 58,06542 | 29,75146 | 60,78017 | €1.484,39 | €2.968,79 | €42,75 | €22,94 |
| Scanner Top5 Btc Guard Mfe V1 | GPS | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01624 | 0,01662 | 0,01431 | 0,00820 | 0,02049 | €193,42 | €386,84 | €46,05 | €9,06 |
| Scanner Top5 Btc Guard Btc Le3 V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01279 | €199,19 | €398,38 | €47,81 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 58,91378 | 59,36900 | 58,06542 | 29,75146 | 60,78017 | €1.538,41 | €3.076,82 | €44,31 | €23,77 |
| Scanner Top5 Btc Guard Btc Le3 V1 | GPS | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01624 | 0,01662 | 0,01431 | 0,00820 | 0,02049 | €200,46 | €400,92 | €47,72 | €9,39 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01012 | 0,01012 | 0,00891 | 0,00511 | 0,01279 | €195,77 | €391,54 | €46,99 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 58,91378 | 59,36900 | 58,06542 | 29,75146 | 60,78017 | €1.512,01 | €3.024,03 | €43,55 | €23,37 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | GPS | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01624 | 0,01662 | 0,01431 | 0,00820 | 0,02049 | €197,02 | €394,04 | €46,91 | €9,23 |
| Scanner Top5 Btc Runner25 V1 | XOM | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 168,23045 | €1.415,24 | €2.830,48 | €47,01 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | GPS | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01624 | 0,01662 | 0,01431 | 0,00820 | 0,02204 | €194,18 | €388,37 | €46,23 | €9,09 |
| Scanner Top5 Btc Runner25 V1 | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 59,29886 | 59,36900 | 58,44495 | 29,94592 | 61,86057 | €1.584,08 | €3.168,15 | €45,62 | €3,75 |
| Scanner Top5 Btc Tp3 V1 | XOM | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 168,23045 | €1.416,07 | €2.832,14 | €47,04 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | GPS | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01624 | 0,01662 | 0,01431 | 0,00820 | 0,02204 | €194,30 | €388,60 | €46,26 | €9,10 |
| Scanner Top5 Btc Tp3 V1 | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 59,29886 | 59,36900 | 58,44495 | 29,94592 | 61,86057 | €1.585,00 | €3.170,01 | €45,65 | €3,75 |
| Global Confluence puro 1H | DOGE | SHORT | Global Confluence puro | 60m | 2,0x | 0,07014 | 0,06988 | 0,07126 | 0,10485 | 0,06733 | €1.512,09 | €3.024,18 | €48,39 | €11,04 |
| Combo Trend | ADA | SHORT | Combo Trend | 60m | 2,0x | 0,18533 | 0,18533 | 0,18829 | 0,27707 | 0,17881 | €56,81 | €113,62 | €1,82 | €-0,00 |
| Combo Trend | DOGE | SHORT | Combo Trend | 60m | 2,0x | 0,07014 | 0,06988 | 0,07126 | 0,10485 | 0,06767 | €29,09 | €58,19 | €0,93 | €0,21 |
| Combo Trend | HYPE | LONG | Combo Trend | 60m | 2,0x | 58,85077 | 59,36900 | 57,90916 | 29,71964 | 60,92231 | €1.350,47 | €2.700,94 | €43,22 | €23,78 |
| Combo Trend | ZEC | LONG | Combo Trend | 60m | 2,0x | 510,90216 | 510,22000 | 501,16840 | 258,00559 | 532,31642 | €21,03 | €42,06 | €0,80 | €-0,06 |
| Combo Trend | PEPE | SHORT | Combo Trend | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €118,87 | €237,73 | €3,80 | €-0,00 |
| Combo Trend | GPS | LONG | Combo Trend | 60m | 2,0x | 0,01630 | 0,01662 | 0,01434 | 0,00823 | 0,02060 | €192,92 | €385,84 | €46,30 | €7,58 |
| Combo Scanner | DOGE | SHORT | Combo Scanner | 60m | 2,0x | 0,06991 | 0,06988 | 0,07091 | 0,10451 | 0,06769 | €1.619,52 | €3.239,04 | €46,64 | €1,21 |
| Combo Scanner | GPS | LONG | Combo Scanner | 60m | 2,0x | 0,01624 | 0,01662 | 0,01431 | 0,00820 | 0,02049 | €191,44 | €382,89 | €45,58 | €8,97 |
| Combo Scanner | HYPE | LONG | Combo Scanner | 60m | 2,0x | 59,41588 | 59,36900 | 58,56029 | 30,00502 | 61,29818 | €20,21 | €40,41 | €0,58 | €-0,03 |
| Combo Adaptive | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,07014 | 0,06988 | 0,07115 | 0,10485 | 0,06812 | €31,23 | €62,47 | €0,90 | €0,23 |
| Combo Adaptive | GPS | LONG | Combo Adaptive | 60m | 2,0x | 0,01624 | 0,01662 | 0,01431 | 0,00820 | 0,02011 | €210,12 | €420,24 | €50,02 | €9,84 |
| Combo Adaptive | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 513,74273 | 510,22000 | 504,63443 | 259,44008 | 531,95932 | €1.419,29 | €2.838,59 | €50,33 | €-19,46 |
| Combo Adaptive Mfe Trail | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,06959 | 0,06988 | 0,07059 | 0,10403 | 0,06758 | €12,71 | €25,42 | €0,37 | €-0,11 |
| Combo Adaptive Mfe Trail | GPS | LONG | Combo Adaptive | 60m | 2,0x | 0,01624 | 0,01662 | 0,01431 | 0,00820 | 0,02011 | €186,88 | €373,75 | €44,49 | €8,75 |
| Combo Adaptive Mfe Trail | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 513,74273 | 510,22000 | 504,63443 | 259,44008 | 531,95932 | €1.263,05 | €2.526,11 | €44,79 | €-17,32 |
| Combo Adaptive Mfe Trail | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 59,41588 | 59,36900 | 58,56029 | 30,00502 | 61,12706 | €17,03 | €34,06 | €0,49 | €-0,03 |
| Combo Adaptive Regime V1 | XOM | LONG | Combo Adaptive | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 165,56900 | €1.488,00 | €2.976,01 | €49,43 | €0,00 |
| Combo Adaptive Regime V1 | CYS | SHORT | Combo Adaptive | 60m | 2,0x | 0,73555 | 0,73555 | 0,73555 | 1,09965 | 0,55902 | €202,91 | €405,83 | €0,00 | €-0,00 |
| Combo Adaptive Quality7 Regime V1 | CAP | LONG | Combo Adaptive | 60m | 2,0x | 0,06429 | 0,06429 | 0,05657 | 0,03247 | 0,07972 | €200,61 | €401,22 | €48,15 | €0,00 |
| Combo Adaptive Quality7 Regime V1 | LINK | LONG | Combo Adaptive | 60m | 2,0x | 9,45467 | 9,45467 | 9,26418 | 4,77461 | 9,83564 | €30,88 | €61,77 | €1,24 | €0,00 |
| Combo Adaptive Quality7 Regime V1 | CYS | SHORT | Combo Adaptive | 60m | 2,0x | 0,73555 | 0,73555 | 0,73555 | 1,09965 | 0,55902 | €199,19 | €398,38 | €0,00 | €-0,00 |
| Combo Adaptive Long Only V1 | XOM | LONG | Combo Adaptive | 60m | 2,0x | 160,24609 | 160,24609 | 157,58464 | 80,92428 | 165,56900 | €1.463,27 | €2.926,54 | €48,61 | €0,00 |
| Combo Adaptive Long Only V1 | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 59,03881 | 59,36900 | 58,18865 | 29,81460 | 60,73912 | €1.675,98 | €3.351,96 | €48,27 | €18,75 |
| Combo Adaptive Long Only V1 | GPS | LONG | Combo Adaptive | 60m | 2,0x | 0,01652 | 0,01662 | 0,01483 | 0,00834 | 0,01990 | €237,17 | €474,34 | €48,53 | €2,87 |
| Combo Adaptive Long Only V1 | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 513,74273 | 510,22000 | 504,63443 | 259,44008 | 531,95932 | €29,05 | €58,10 | €1,03 | €-0,40 |
| Combo Adaptive Partial 1R V1 | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,07014 | 0,06988 | 0,07115 | 0,10485 | 0,06812 | €29,99 | €59,98 | €0,86 | €0,22 |
| Combo Adaptive Partial 1R V1 | GPS | LONG | Combo Adaptive | 60m | 2,0x | 0,01624 | 0,01662 | 0,01431 | 0,00820 | 0,02011 | €201,77 | €403,54 | €48,04 | €9,45 |
| Combo Adaptive Partial 1R V1 | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 513,74273 | 510,22000 | 504,63443 | 259,44008 | 531,95932 | €1.362,87 | €2.725,74 | €48,33 | €-18,69 |
| Combo Adaptive Quality7 Regime Partial 1R V1 | CAP | LONG | Combo Adaptive | 60m | 2,0x | 0,06429 | 0,06429 | 0,05657 | 0,03247 | 0,07972 | €203,16 | €406,33 | €48,76 | €0,00 |
| Combo Adaptive Quality7 Regime Partial 1R V1 | LINK | LONG | Combo Adaptive | 60m | 2,0x | 9,45467 | 9,45467 | 9,26418 | 4,77461 | 9,83564 | €31,28 | €62,56 | €1,26 | €0,00 |
| Combo Adaptive Quality7 Regime Partial 1R V1 | CYS | SHORT | Combo Adaptive | 60m | 2,0x | 0,73555 | 0,73555 | 0,73555 | 1,09965 | 0,55902 | €201,73 | €403,45 | €0,00 | €-0,00 |
| Combo Adaptive Runner25 V1 | PEPE | SHORT | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.096,14 | €2.192,28 | €0,00 | €-0,00 |
| Combo Adaptive Runner25 V1 | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,07014 | 0,06988 | 0,07115 | 0,10485 | 0,06711 | €30,90 | €61,81 | €0,89 | €0,23 |
| Combo Adaptive Runner25 V1 | GPS | LONG | Combo Adaptive | 60m | 2,0x | 0,01624 | 0,01662 | 0,01431 | 0,00820 | 0,02204 | €197,23 | €394,46 | €46,96 | €9,24 |
| Combo Adaptive Runner25 V1 | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 513,74273 | 510,22000 | 504,63443 | 259,44008 | 541,06761 | €138,01 | €276,03 | €4,89 | €-1,89 |
| Combo Adaptive Tp3 V1 | PEPE | SHORT | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.075,66 | €2.151,32 | €0,00 | €-0,00 |
| Combo Adaptive Tp3 V1 | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,07014 | 0,06988 | 0,07115 | 0,10485 | 0,06711 | €30,33 | €60,65 | €0,87 | €0,22 |
| Combo Adaptive Tp3 V1 | GPS | LONG | Combo Adaptive | 60m | 2,0x | 0,01624 | 0,01662 | 0,01431 | 0,00820 | 0,02204 | €193,55 | €387,09 | €46,08 | €9,06 |
| Combo Adaptive Tp3 V1 | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 513,74273 | 510,22000 | 504,63443 | 259,44008 | 541,06761 | €135,44 | €270,87 | €4,80 | €-1,86 |
| Btc Ema 4H | BTC | SHORT | Trend following EMA | 240m | 2,0x | 63679,75150 | 64182,18000 | 64800,51513 | 95201,22850 | 60877,84244 | €1.413,45 | €2.826,90 | €49,75 | €-22,30 |
| Btc Donchian 4H | BTC | SHORT | Donchian breakout 20 barre | 240m | 2,0x | 63544,23861 | 64182,18000 | 64662,61721 | 94998,63672 | 60412,77853 | €1.406,00 | €2.812,00 | €49,49 | €-28,23 |
| Eth Ema 1H | ETH | LONG | Trend following EMA | 60m | 3,0x | 1907,45141 | 1895,77000 | 1879,98411 | 1281,17153 | 1962,38601 | €1.105,17 | €3.315,52 | €47,74 | €-20,30 |
| Doge Ema 1H | DOGE | SHORT | Trend following EMA | 60m | 3,0x | 0,07014 | 0,06988 | 0,07115 | 0,09316 | 0,06812 | €1.155,63 | €3.466,88 | €49,92 | €12,65 |
| Master Adaptive V1 | XOM | LONG | Master Adaptive Consensus | 60m | 2,0x | 159,95592 | 159,95592 | 157,06873 | 80,77774 | 165,73030 | €1.280,33 | €2.560,66 | €46,22 | €0,00 |
| Master Adaptive V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 1902,79048 | 1895,77000 | 1875,39030 | 960,90919 | 1957,59085 | €47,34 | €94,69 | €1,36 | €-0,35 |
| Master Adaptive V1 | BTC | LONG | Master Adaptive Consensus | 60m | 2,0x | 63500,19750 | 64182,18000 | 62585,79466 | 32067,59974 | 65329,00319 | €1.616,79 | €3.233,57 | €46,56 | €34,73 |
| Master Adaptive No Alt V1 | XOM | LONG | Master Adaptive Consensus | 60m | 2,0x | 159,95592 | 159,95592 | 157,06873 | 80,77774 | 165,73030 | €1.263,27 | €2.526,54 | €45,60 | €0,00 |
| Master Adaptive No Alt V1 | LINK | LONG | Master Adaptive Consensus | 60m | 2,0x | 9,45467 | 9,45467 | 9,26418 | 4,77461 | 9,83564 | €15,67 | €31,33 | €0,63 | €0,00 |
| Master Adaptive No Alt V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 1889,64785 | 1895,77000 | 1862,43692 | 954,27217 | 1944,06971 | €18,64 | €37,28 | €0,54 | €0,12 |
| Master Adaptive No Alt V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 59,03881 | 59,36900 | 58,18865 | 29,81460 | 60,73912 | €1.637,93 | €3.275,87 | €47,17 | €18,32 |
| Master Adaptive No Alt V1 | BTC | LONG | Master Adaptive Consensus | 60m | 2,0x | 63500,19750 | 64182,18000 | 62585,79466 | 32067,59974 | 65329,00319 | €1.635,66 | €3.271,33 | €47,11 | €35,13 |
| Master Adaptive Strict3 V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01007 | 0,01007 | 0,00886 | 0,00509 | 0,01249 | €186,88 | €373,77 | €44,85 | €0,00 |
| Master Adaptive Strict3 V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 58,91378 | 59,36900 | 58,06542 | 29,75146 | 60,61050 | €1.418,93 | €2.837,86 | €40,87 | €21,93 |
| Master Adaptive Expanded V1 | NEAR | LONG | Master Adaptive Consensus | 60m | 2,0x | 1,64799 | 1,64799 | 1,61151 | 0,83223 | 1,72094 | €1.046,99 | €2.093,97 | €46,35 | €0,00 |
| Master Adaptive Expanded V1 | XOM | LONG | Master Adaptive Consensus | 60m | 2,0x | 159,97593 | 159,97593 | 156,99846 | 80,78784 | 165,93086 | €27,82 | €55,63 | €1,04 | €0,00 |
| Master Adaptive Expanded V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 1902,79048 | 1895,77000 | 1875,39030 | 960,90919 | 1957,59085 | €15,15 | €30,30 | €0,44 | €-0,11 |
| Master Adaptive Expanded V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 59,03881 | 59,36900 | 58,18865 | 29,81460 | 60,73912 | €1.636,69 | €3.273,37 | €47,14 | €18,31 |
| Master Adaptive Gb20 V1 | XOM | LONG | Master Adaptive Consensus | 60m | 2,0x | 159,95592 | 159,95592 | 157,06873 | 80,77774 | 165,73030 | €1.263,32 | €2.526,64 | €45,61 | €0,00 |
| Master Adaptive Gb20 V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 1902,79048 | 1895,77000 | 1875,39030 | 960,90919 | 1957,59085 | €46,71 | €93,43 | €1,35 | €-0,34 |
| Master Adaptive Gb20 V1 | BTC | LONG | Master Adaptive Consensus | 60m | 2,0x | 63500,19750 | 64182,18000 | 62585,79466 | 32067,59974 | 65329,00319 | €1.595,31 | €3.190,61 | €45,94 | €34,27 |
| Master Adaptive Runner25 V1 | XOM | LONG | Master Adaptive Consensus | 60m | 2,0x | 159,95592 | 159,95592 | 157,06873 | 80,77774 | 168,61749 | €28,89 | €57,79 | €1,04 | €0,00 |
| Master Adaptive Runner25 V1 | CAP | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,06539 | 0,06539 | 0,05754 | 0,03302 | 0,08893 | €176,29 | €352,58 | €42,31 | €0,00 |
| Master Adaptive Runner25 V1 | LINK | LONG | Master Adaptive Consensus | 60m | 2,0x | 9,45467 | 9,45467 | 9,26418 | 4,77461 | 10,02613 | €29,62 | €59,24 | €1,19 | €0,00 |
| Master Adaptive Runner25 V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 58,91378 | 59,36900 | 58,06542 | 29,75146 | 61,45886 | €1.476,62 | €2.953,25 | €42,53 | €22,82 |
| Master Adaptive Runner25 V1 | BTC | LONG | Master Adaptive Consensus | 60m | 2,0x | 63500,19750 | 64182,18000 | 62585,79466 | 32067,59974 | 66243,40603 | €1.599,88 | €3.199,76 | €46,08 | €34,36 |
| Combo Adaptive Side Regime Guard V1 | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,06991 | 0,06988 | 0,07091 | 0,10451 | 0,06789 | €1.659,52 | €3.319,05 | €47,79 | €1,24 |
| Combo Adaptive Side Regime Guard V1 | XRP | SHORT | Combo Adaptive | 60m | 2,0x | 1,00430 | 0,99491 | 0,99748 | 1,50143 | 0,97538 | €1.713,05 | €3.426,11 | €0,00 | €32,03 |
| Combo Adaptive Side Regime Guard V1 | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 513,74273 | 510,22000 | 504,63443 | 259,44008 | 531,95932 | €1.398,25 | €2.796,51 | €49,58 | €-19,18 |
| Combo Adaptive Side Regime Guard V1 | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 59,41588 | 59,36900 | 58,56029 | 30,00502 | 61,12706 | €68,07 | €136,14 | €1,96 | €-0,11 |
| Master Adaptive Gb20 Be V1 | XOM | LONG | Master Adaptive Consensus | 60m | 2,0x | 159,95592 | 159,95592 | 157,06873 | 80,77774 | 165,73030 | €1.286,67 | €2.573,34 | €46,45 | €0,00 |
| Master Adaptive Gb20 Be V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 1902,79048 | 1895,77000 | 1875,39030 | 960,90919 | 1957,59085 | €47,58 | €95,15 | €1,37 | €-0,35 |
| Master Adaptive Gb20 Be V1 | BTC | LONG | Master Adaptive Consensus | 60m | 2,0x | 63500,19750 | 64182,18000 | 62585,79466 | 32067,59974 | 65329,00319 | €1.624,79 | €3.249,59 | €46,79 | €34,90 |
| Master Adaptive Gb20 Partial V1 | XOM | LONG | Master Adaptive Consensus | 60m | 2,0x | 159,95592 | 159,95592 | 157,06873 | 80,77774 | 165,73030 | €1.285,30 | €2.570,60 | €46,40 | €0,00 |
| Master Adaptive Gb20 Partial V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 1902,79048 | 1895,77000 | 1875,39030 | 960,90919 | 1957,59085 | €47,53 | €95,05 | €1,37 | €-0,35 |
| Master Adaptive Gb20 Partial V1 | BTC | LONG | Master Adaptive Consensus | 60m | 2,0x | 63500,19750 | 64182,18000 | 62585,79466 | 32067,59974 | 65329,00319 | €1.623,07 | €3.246,13 | €46,74 | €34,86 |
| Master Adaptive Gb20 Loss Cap V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 1902,79048 | 1895,77000 | 1882,24034 | 960,90919 | 1957,59085 | €1.821,95 | €3.643,90 | €39,35 | €-13,44 |
| Master Adaptive Gb20 Loss Cap V1 | BTC | LONG | Master Adaptive Consensus | 60m | 2,0x | 63500,19750 | 64182,18000 | 62814,39537 | 32067,59974 | 65329,00319 | €1.820,09 | €3.640,18 | €39,31 | €39,09 |
| 1H Fast V3 Nohigh Regime Guard V1 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1902,79048 | 1895,77000 | 1881,47923 | 1278,04094 | 1934,75736 | €1.508,82 | €4.526,45 | €50,70 | €-16,70 |
| Main Side Regime Guard V1 | XRP | SHORT | Confluenza trend | 240m | 3,0x | 1,01047 | 0,99491 | 1,03352 | 1,34224 | 0,96437 | €747,08 | €2.241,25 | €51,13 | €34,51 |
| Main Side Regime Guard V1 | VELVET | LONG | Confluenza trend | 240m | 3,0x | 0,55987 | 0,55987 | 0,49269 | 0,37605 | 0,69424 | €142,25 | €426,74 | €51,21 | €0,00 |
| Main Side Regime Guard V1 | PEPE | SHORT | Confluenza trend | 240m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €16,24 | €48,72 | €1,84 | €-0,00 |
| Main Side Regime Guard V1 | AKE | LONG | Confluenza trend | 240m | 3,0x | 0,01021 | 0,01021 | 0,00899 | 0,00686 | 0,01266 | €145,97 | €437,90 | €52,55 | €0,00 |
| Main Side Regime Guard V1 | HYPE | LONG | Confluenza trend | 240m | 3,0x | 59,42488 | 59,36900 | 57,77054 | 39,91371 | 62,73356 | €20,16 | €60,47 | €1,68 | €-0,06 |
| Main Side Regime Guard V1 | SNDK | LONG | Confluenza trend | 240m | 3,0x | 1787,69747 | 1721,89000 | 1707,14791 | 1200,73680 | 1948,79656 | €370,44 | €1.111,33 | €50,07 | €-40,91 |
| Combo Trend Side Regime Guard V1 | VELVET | LONG | Combo Trend | 60m | 2,0x | 0,60867 | 0,60867 | 0,53563 | 0,30738 | 0,76936 | €210,36 | €420,71 | €50,49 | €0,00 |
| Combo Trend Side Regime Guard V1 | DOGE | SHORT | Combo Trend | 60m | 2,0x | 0,06967 | 0,06988 | 0,07078 | 0,10415 | 0,06721 | €1.571,45 | €3.142,90 | €50,29 | €-9,65 |
| Combo Trend Side Regime Guard V1 | XRP | SHORT | Combo Trend | 60m | 2,0x | 1,00446 | 0,99491 | 1,02053 | 1,50167 | 0,96910 | €1.563,61 | €3.127,21 | €50,04 | €29,73 |
| Combo Trend Side Regime Guard V1 | ZEC | LONG | Combo Trend | 60m | 2,0x | 512,07239 | 510,22000 | 502,17558 | 258,59656 | 533,84539 | €45,72 | €91,45 | €1,77 | €-0,33 |
| 1H Fast Nohigh Cap75 Short Only V1 | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,01003 | 0,01003 | 0,00915 | 0,00674 | 0,01134 | €184,93 | €554,78 | €48,58 | €0,00 |
| 1H Balanced V3 Long Only V1 | DOGE | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,06964 | 0,06988 | 0,07064 | 0,09250 | 0,06763 | €13,83 | €41,49 | €0,60 | €-0,14 |
| 1H Balanced V3 Long Only V1 | XRP | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,99900 | 0,99491 | 1,01339 | 1,32701 | 0,97023 | €46,73 | €140,20 | €2,02 | €0,57 |
| 1H Balanced V3 Long Only V1 | PEPE | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.101,68 | €3.305,04 | €47,59 | €-0,00 |
| 1H Balanced V3 Long Only V1 | ZEC | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 514,86295 | 510,22000 | 506,12617 | 345,81628 | 532,33652 | €938,99 | €2.816,96 | €47,80 | €-25,40 |
| 1H Balanced V3 Long Only V1 | GPS | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,01624 | 0,01662 | 0,01431 | 0,01091 | 0,02011 | €133,83 | €401,48 | €47,79 | €9,40 |
| 1H Balanced V3 Long Only V1 | HYPE | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 59,29886 | 59,36900 | 58,44495 | 39,82907 | 61,00666 | €970,65 | €2.911,95 | €41,93 | €3,44 |
| Scanner Bottom5 Short Profit Lock V1 | BEAT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,28257 | 0,26678 | 0,31648 | 0,42244 | 0,21475 | €202,51 | €405,01 | €48,60 | €22,63 |
| Scanner Bottom5 Short Profit Lock V1 | DOGE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,06970 | 0,06988 | 0,07070 | 0,10420 | 0,06769 | €1.687,46 | €3.374,92 | €48,60 | €-8,81 |
| Scanner Bottom5 Short Mfe Trail V1 | BEAT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,28257 | 0,26678 | 0,31648 | 0,42244 | 0,21475 | €202,81 | €405,63 | €48,68 | €22,67 |
| Scanner Bottom5 Short Mfe Trail V1 | DOGE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,06970 | 0,06988 | 0,07070 | 0,10420 | 0,06769 | €1.690,03 | €3.380,06 | €48,67 | €-8,82 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1H Fast V3 No Esports V1 | CAP | LONG | 2026-08-18T04:05:47+00:00 | 0,06914 | €1,12 | 0,02 | TIME_EXIT_NO_CANDLES |
| 1H Fast V3 No Esports Mfe Lock V1 | CAP | LONG | 2026-08-18T04:05:47+00:00 | 0,06914 | €0,11 | 0,02 | TIME_EXIT_NO_CANDLES |
| Rapida 1H V3 Filtered | CAP | LONG | 2026-08-18T04:05:47+00:00 | 0,06914 | €0,11 | 0,02 | TIME_EXIT_NO_CANDLES |
| 1H Fast Tp2 V1 | CAP | LONG | 2026-08-18T04:05:47+00:00 | 0,06914 | €1,15 | 0,02 | TIME_EXIT_NO_CANDLES |
| Scanner Top 5 Long 1H | SKHYNIX | LONG | 2026-08-18T03:06:15+00:00 | 1183,67180 | €-4,72 | -1,38 | STOP_GAP_STRESS |
| Scanner Top5 Btc Tp3 V1 | SKHYNIX | LONG | 2026-08-18T03:06:15+00:00 | 1183,67180 | €-63,39 | -1,38 | STOP_GAP_STRESS |
| Scanner Top5 Btc Runner25 V1 | SKHYNIX | LONG | 2026-08-18T03:06:15+00:00 | 1183,67180 | €-63,35 | -1,38 | STOP_GAP_STRESS |
| Scanner Top5 Btc Mfe V1 | SKHYNIX | LONG | 2026-08-18T03:06:15+00:00 | 1183,67180 | €-61,46 | -1,38 | STOP_GAP_STRESS |
| Scanner Top5 Btc Guard V1 | SKHYNIX | LONG | 2026-08-18T03:06:15+00:00 | 1183,67180 | €-64,92 | -1,38 | STOP_GAP_STRESS |
| Scanner Top5 Btc Guard Mfe V1 | SKHYNIX | LONG | 2026-08-18T03:06:15+00:00 | 1183,67180 | €-63,41 | -1,38 | STOP_GAP_STRESS |
| Scanner Top5 Btc Guard Btc Le3 V1 | SKHYNIX | LONG | 2026-08-18T03:06:15+00:00 | 1183,67180 | €-65,72 | -1,38 | STOP_GAP_STRESS |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | SKHYNIX | LONG | 2026-08-18T03:06:15+00:00 | 1183,67180 | €-64,59 | -1,38 | STOP_GAP_STRESS |

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

Generato: 2026-08-18 05:32 UTC


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

Segnali totali salvati: **117**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08-18 | BTC | 64.145,05 | 0 | +2 | +2 | 0 | -1 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-08-18 | DOGE | 0.06969 | +3 | +4 | +3 | +2 | 0 | -1 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-08-18 | SOL | 75,65 | +1 | +3 | +3 | +2 | -2 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-08-17 | BTC | 63.428,86 | +1 | +4 | +3 | +1 | -2 | -1 | 0 | HOLD / ATTESA CONFERME |
| 2026-08-17 | DOGE | 0.07007 | +2 | +4 | +3 | +2 | -1 | -1 | 0 | STAI ALLA FINESTRA |
| 2026-08-17 | SOL | 75,40 | +1 | +3 | +3 | +2 | -2 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-08-16 | BTC | 63.005,56 | +1 | +4 | +3 | +2 | -2 | -1 | 0 | HOLD / ATTESA CONFERME |
| 2026-08-16 | DOGE | 0.06966 | +4 | +4 | +3 | +2 | +1 | -1 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-08-16 | SOL | 75,33 | +1 | +3 | +3 | +3 | -2 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-08-15 | BTC | 63.058,07 | +1 | +4 | +3 | +2 | -2 | -1 | 0 | HOLD / ATTESA CONFERME |
| 2026-08-15 | DOGE | 0.07017 | +4 | +4 | +3 | +2 | +1 | 0 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-08-15 | SOL | 75,40 | +2 | +4 | +3 | +2 | -2 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 39 | 38 | 37 | 36 | 34 | 34 | 31 | 27 | 20 | 11 | 0 | 0 |
| SOL | 39 | 38 | 37 | 36 | 34 | 34 | 31 | 27 | 20 | 11 | 0 | 0 |
| DOGE | 39 | 38 | 37 | 36 | 34 | 34 | 31 | 27 | 20 | 11 | 0 | 0 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-07-20 | 30g | 2026-08-19 | domani |
| SOL | 2026-07-20 | 30g | 2026-08-19 | domani |
| DOGE | 2026-07-20 | 30g | 2026-08-19 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 36 | 50,00% | +0,05% | +0,02% | PRIMA CALIBRAZIONE |
| BTC | 2g | 35 | 48,57% | +0,10% | -0,03% | PRIMA CALIBRAZIONE |
| BTC | 3g | 34 | 41,18% | -0,05% | -0,26% | PRIMA CALIBRAZIONE |
| BTC | 5g | 32 | 28,12% | -0,09% | -0,49% | PRIMA CALIBRAZIONE |
| BTC | 7g | 32 | 40,62% | -0,02% | -0,35% | PRIMA CALIBRAZIONE |
| BTC | 10g | 29 | 41,38% | +0,21% | -0,10% | FEEDBACK RAPIDO |
| BTC | 14g | 25 | 44,00% | +0,02% | -0,12% | FEEDBACK RAPIDO |
| BTC | 21g | 18 | 22,22% | -0,60% | -0,97% | FEEDBACK RAPIDO |
| BTC | 30g | 10 | 80,00% | +0,18% | +0,69% | FEEDBACK RAPIDO |
| BTC | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 1g | 31 | 51,61% | +0,02% | -0,18% | PRIMA CALIBRAZIONE |
| SOL | 2g | 30 | 43,33% | +0,00% | -0,23% | PRIMA CALIBRAZIONE |
| SOL | 3g | 29 | 44,83% | +0,10% | -0,21% | FEEDBACK RAPIDO |
| SOL | 5g | 27 | 48,15% | -0,10% | -0,30% | FEEDBACK RAPIDO |
| SOL | 7g | 27 | 55,56% | -0,05% | +0,15% | FEEDBACK RAPIDO |
| SOL | 10g | 24 | 54,17% | -0,06% | +0,26% | FEEDBACK RAPIDO |
| SOL | 14g | 20 | 60,00% | -1,32% | +0,49% | FEEDBACK RAPIDO |
| SOL | 21g | 15 | 60,00% | -2,44% | +0,07% | FEEDBACK RAPIDO |
| SOL | 30g | 10 | 40,00% | -0,97% | -0,80% | FEEDBACK RAPIDO |
| SOL | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 1g | 36 | 41,67% | -0,03% | -0,05% | PRIMA CALIBRAZIONE |
| DOGE | 2g | 35 | 45,71% | -0,12% | -0,13% | PRIMA CALIBRAZIONE |
| DOGE | 3g | 34 | 41,18% | -0,33% | +0,01% | PRIMA CALIBRAZIONE |
| DOGE | 5g | 32 | 50,00% | -0,59% | +0,19% | PRIMA CALIBRAZIONE |
| DOGE | 7g | 32 | 59,38% | -0,84% | +0,54% | PRIMA CALIBRAZIONE |
| DOGE | 10g | 29 | 51,72% | -1,34% | +0,80% | FEEDBACK RAPIDO |
| DOGE | 14g | 26 | 57,69% | -2,06% | +1,51% | FEEDBACK RAPIDO |
| DOGE | 21g | 19 | 78,95% | -3,35% | +2,77% | FEEDBACK RAPIDO |
| DOGE | 30g | 11 | 100,00% | -4,16% | +4,16% | FEEDBACK RAPIDO |
| DOGE | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 36 | 50,00% | +0,05% | +0,02% | -0,27% | +0,58% | PRIMA CALIBRAZIONE |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 38 | 52,63% | +0,04% | +0,04% | -0,28% | +0,54% | PRIMA CALIBRAZIONE |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 38 | 52,63% | +0,04% | +0,04% | -0,28% | +0,54% | PRIMA CALIBRAZIONE |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 34 | 52,94% | +0,01% | +0,01% | -0,32% | +0,47% | PRIMA CALIBRAZIONE |
| BTC | 1g | Tecnico | CALIBRABILE | 33 | 33,33% | +0,19% | -0,42% | -0,15% | +0,69% | PRIMA CALIBRAZIONE |
| BTC | 1g | Classic technical | CALIBRABILE | 8 | 12,50% | +0,66% | -0,66% | +0,09% | +0,94% | FEEDBACK RAPIDO |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +2,00% | +2,00% | +1,48% | +2,25% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 35 | 48,57% | +0,10% | -0,03% | -0,38% | +0,78% | PRIMA CALIBRAZIONE |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 37 | 51,35% | +0,07% | +0,07% | -0,39% | +0,75% | PRIMA CALIBRAZIONE |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 37 | 51,35% | +0,07% | +0,07% | -0,39% | +0,75% | PRIMA CALIBRAZIONE |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 33 | 51,52% | -0,00% | -0,00% | -0,48% | +0,66% | PRIMA CALIBRAZIONE |
| BTC | 2g | Tecnico | CALIBRABILE | 32 | 40,62% | +0,25% | -0,43% | -0,20% | +0,92% | PRIMA CALIBRAZIONE |
| BTC | 2g | Classic technical | CALIBRABILE | 7 | 14,29% | +0,89% | -0,89% | +0,49% | +1,50% | FEEDBACK RAPIDO |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +3,18% | +3,18% | +3,05% | +3,89% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 34 | 41,18% | -0,05% | -0,26% | -1,34% | +1,58% | PRIMA CALIBRAZIONE |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 36 | 52,78% | +0,02% | +0,02% | -1,31% | +1,57% | PRIMA CALIBRAZIONE |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 36 | 52,78% | +0,02% | +0,02% | -1,31% | +1,57% | PRIMA CALIBRAZIONE |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 32 | 53,12% | +0,00% | +0,00% | -1,33% | +1,48% | PRIMA CALIBRAZIONE |
| BTC | 3g | Tecnico | CALIBRABILE | 31 | 32,26% | +0,34% | -0,52% | -1,08% | +1,83% | PRIMA CALIBRAZIONE |
| BTC | 3g | Classic technical | CALIBRABILE | 6 | 16,67% | +1,26% | -1,26% | -0,39% | +2,22% | FEEDBACK RAPIDO |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,88% | +1,88% | +1,44% | +4,24% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 32 | 28,12% | -0,09% | -0,49% | -2,11% | +2,04% | PRIMA CALIBRAZIONE |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 34 | 38,24% | -0,08% | -0,08% | -2,07% | +2,08% | PRIMA CALIBRAZIONE |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 34 | 38,24% | -0,08% | -0,08% | -2,07% | +2,08% | PRIMA CALIBRAZIONE |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 30 | 40,00% | -0,01% | -0,01% | -2,06% | +2,03% | PRIMA CALIBRAZIONE |
| BTC | 5g | Tecnico | CALIBRABILE | 29 | 37,93% | +0,10% | -0,74% | -1,83% | +2,30% | FEEDBACK RAPIDO |
| BTC | 5g | Classic technical | CALIBRABILE | 4 | 25,00% | +1,14% | -1,14% | -1,16% | +2,94% | FEEDBACK RAPIDO |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,16% | -0,16% | -0,37% | +4,24% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 32 | 40,62% | -0,02% | -0,35% | -2,37% | +2,35% | PRIMA CALIBRAZIONE |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 34 | 50,00% | -0,05% | -0,05% | -2,35% | +2,37% | PRIMA CALIBRAZIONE |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 34 | 50,00% | -0,05% | -0,05% | -2,35% | +2,37% | PRIMA CALIBRAZIONE |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 30 | 53,33% | +0,12% | +0,12% | -2,33% | +2,37% | PRIMA CALIBRAZIONE |
| BTC | 7g | Tecnico | CALIBRABILE | 29 | 34,48% | +0,33% | -0,86% | -2,10% | +2,59% | FEEDBACK RAPIDO |
| BTC | 7g | Classic technical | CALIBRABILE | 4 | 0,00% | +1,94% | -1,94% | -1,23% | +3,13% | FEEDBACK RAPIDO |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,77% | +1,77% | -0,79% | +4,24% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 29 | 41,38% | +0,21% | -0,10% | -2,61% | +2,84% | FEEDBACK RAPIDO |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 31 | 48,39% | +0,05% | +0,05% | -2,64% | +2,83% | PRIMA CALIBRAZIONE |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 31 | 48,39% | +0,05% | +0,05% | -2,64% | +2,83% | PRIMA CALIBRAZIONE |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 27 | 55,56% | +0,36% | +0,36% | -2,52% | +2,89% | FEEDBACK RAPIDO |
| BTC | 10g | Tecnico | CALIBRABILE | 26 | 30,77% | +0,28% | -0,37% | -2,34% | +3,14% | FEEDBACK RAPIDO |
| BTC | 10g | Classic technical | CALIBRABILE | 4 | 0,00% | +1,32% | -1,32% | -1,42% | +3,31% | FEEDBACK RAPIDO |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,43% | -0,43% | -2,30% | +4,24% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 25 | 44,00% | +0,02% | -0,12% | -2,80% | +3,37% | FEEDBACK RAPIDO |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 27 | 44,44% | -0,10% | -0,10% | -2,83% | +3,32% | FEEDBACK RAPIDO |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 27 | 44,44% | -0,10% | -0,10% | -2,83% | +3,32% | FEEDBACK RAPIDO |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 23 | 52,17% | +0,32% | +0,32% | -2,56% | +3,48% | FEEDBACK RAPIDO |
| BTC | 14g | Tecnico | CALIBRABILE | 22 | 59,09% | +0,17% | +0,10% | -2,46% | +3,69% | FEEDBACK RAPIDO |
| BTC | 14g | Classic technical | CALIBRABILE | 4 | 50,00% | +0,27% | -0,27% | -1,55% | +3,37% | FEEDBACK RAPIDO |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -2,25% | -2,25% | -3,05% | +4,24% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 18 | 22,22% | -0,60% | -0,97% | -3,23% | +3,58% | FEEDBACK RAPIDO |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 20 | 40,00% | -0,65% | -0,65% | -3,27% | +3,49% | FEEDBACK RAPIDO |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 20 | 40,00% | -0,65% | -0,65% | -3,27% | +3,49% | FEEDBACK RAPIDO |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 16 | 43,75% | -0,47% | -0,47% | -2,96% | +3,77% | FEEDBACK RAPIDO |
| BTC | 21g | Tecnico | CALIBRABILE | 16 | 25,00% | -0,26% | -0,16% | -2,90% | +3,94% | FEEDBACK RAPIDO |
| BTC | 21g | Classic technical | CALIBRABILE | 1 | 0,00% | +1,21% | -1,21% | -1,82% | +3,19% | FEEDBACK RAPIDO |
| BTC | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,21% | +1,21% | -3,06% | +4,24% | FEEDBACK RAPIDO |
| BTC | 30g | Global confluence | BENCHMARK | 10 | 80,00% | +0,18% | +0,69% | -2,63% | +5,02% | FEEDBACK RAPIDO |
| BTC | 30g | Famiglia statistica | CALIBRABILE | 11 | 54,55% | +0,10% | +0,10% | -2,62% | +4,99% | FEEDBACK RAPIDO |
| BTC | 30g | Scanner grezzo | DIAGNOSTICO | 11 | 54,55% | +0,10% | +0,10% | -2,62% | +4,99% | FEEDBACK RAPIDO |
| BTC | 30g | Market regime grezzo | DIAGNOSTICO | 10 | 60,00% | +0,21% | +0,21% | -2,50% | +5,16% | FEEDBACK RAPIDO |
| BTC | 30g | Tecnico | CALIBRABILE | 10 | 50,00% | -0,02% | -0,49% | -2,56% | +5,01% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 36 | 41,67% | -0,03% | -0,05% | -0,50% | +0,67% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 38 | 52,63% | -0,14% | +0,18% | -0,61% | +0,55% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 38 | 52,63% | -0,14% | +0,18% | -0,61% | +0,55% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 36 | 52,78% | -0,04% | +0,08% | -0,53% | +0,67% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Tecnico | CALIBRABILE | 33 | 51,52% | -0,13% | +0,13% | -0,60% | +0,48% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Classic technical | CALIBRABILE | 25 | 40,00% | +0,20% | -0,20% | -0,31% | +0,75% | FEEDBACK RAPIDO |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 50,00% | +1,92% | +1,13% | +0,84% | +2,11% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 35 | 45,71% | -0,12% | -0,13% | -0,75% | +0,92% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 37 | 48,65% | -0,23% | +0,02% | -0,86% | +0,78% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 37 | 48,65% | -0,23% | +0,02% | -0,86% | +0,78% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 35 | 48,57% | -0,32% | +0,09% | -0,90% | +0,75% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Tecnico | CALIBRABILE | 32 | 59,38% | -0,29% | +0,28% | -0,89% | +0,60% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Classic technical | CALIBRABILE | 24 | 45,83% | +0,18% | -0,18% | -0,45% | +1,20% | FEEDBACK RAPIDO |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 50,00% | +3,12% | +2,46% | +2,21% | +3,52% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 34 | 41,18% | -0,33% | +0,01% | -1,77% | +1,95% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 36 | 47,22% | -0,42% | -0,07% | -1,86% | +1,80% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 36 | 47,22% | -0,42% | -0,07% | -1,86% | +1,80% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | -0,66% | +0,13% | -1,82% | +1,67% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Tecnico | CALIBRABILE | 31 | 48,39% | -0,50% | +0,45% | -1,99% | +1,63% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Classic technical | CALIBRABILE | 23 | 39,13% | -0,05% | +0,05% | -1,78% | +2,33% | FEEDBACK RAPIDO |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 50,00% | +1,70% | +1,18% | -0,25% | +5,07% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 32 | 50,00% | -0,59% | +0,19% | -2,65% | +2,44% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 34 | 47,06% | -0,68% | +0,08% | -2,71% | +2,30% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 34 | 47,06% | -0,68% | +0,08% | -2,71% | +2,30% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 32 | 46,88% | -0,69% | +0,05% | -2,71% | +2,16% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Tecnico | CALIBRABILE | 30 | 63,33% | -0,75% | +0,75% | -2,89% | +2,13% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Classic technical | CALIBRABILE | 22 | 54,55% | -0,40% | +0,40% | -2,68% | +2,79% | FEEDBACK RAPIDO |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 50,00% | +0,64% | +0,23% | -0,37% | +5,72% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 32 | 59,38% | -0,84% | +0,54% | -3,04% | +2,67% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 34 | 55,88% | -0,93% | +0,33% | -3,12% | +2,57% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 34 | 55,88% | -0,93% | +0,33% | -3,12% | +2,57% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 32 | 56,25% | -0,92% | +0,28% | -3,15% | +2,45% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Tecnico | CALIBRABILE | 30 | 63,33% | -1,05% | +1,05% | -3,36% | +2,36% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Classic technical | CALIBRABILE | 22 | 54,55% | -0,91% | +0,91% | -3,18% | +2,88% | FEEDBACK RAPIDO |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 50,00% | +0,63% | +0,36% | -0,50% | +5,72% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 29 | 51,72% | -1,34% | +0,80% | -3,76% | +2,79% | FEEDBACK RAPIDO |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 31 | 51,61% | -1,37% | +0,67% | -3,80% | +2,68% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 31 | 51,61% | -1,37% | +0,67% | -3,80% | +2,68% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 29 | 51,72% | -1,41% | +0,65% | -3,82% | +2,55% | FEEDBACK RAPIDO |
| DOGE | 10g | Tecnico | CALIBRABILE | 30 | 66,67% | -1,40% | +1,40% | -3,88% | +2,63% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Classic technical | CALIBRABILE | 21 | 61,90% | -1,18% | +1,18% | -3,82% | +2,85% | FEEDBACK RAPIDO |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +1,23% | +0,22% | -1,27% | +6,23% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 26 | 57,69% | -2,06% | +1,51% | -4,70% | +2,96% | FEEDBACK RAPIDO |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 27 | 62,96% | -2,14% | +1,33% | -4,77% | +2,77% | FEEDBACK RAPIDO |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 27 | 62,96% | -2,14% | +1,33% | -4,77% | +2,77% | FEEDBACK RAPIDO |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 25 | 64,00% | -2,19% | +1,31% | -4,86% | +2,63% | FEEDBACK RAPIDO |
| DOGE | 14g | Tecnico | CALIBRABILE | 27 | 74,07% | -2,14% | +2,14% | -4,77% | +2,77% | FEEDBACK RAPIDO |
| DOGE | 14g | Classic technical | CALIBRABILE | 20 | 70,00% | -2,09% | +2,09% | -4,80% | +3,07% | FEEDBACK RAPIDO |
| DOGE | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +0,46% | +0,46% | -1,85% | +6,57% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 19 | 78,95% | -3,35% | +2,77% | -5,86% | +2,70% | FEEDBACK RAPIDO |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 20 | 80,00% | -3,38% | +2,54% | -5,90% | +2,56% | FEEDBACK RAPIDO |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 20 | 80,00% | -3,38% | +2,54% | -5,90% | +2,56% | FEEDBACK RAPIDO |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 18 | 83,33% | -3,61% | +2,68% | -6,14% | +2,34% | FEEDBACK RAPIDO |
| DOGE | 21g | Tecnico | CALIBRABILE | 20 | 90,00% | -3,38% | +3,38% | -5,90% | +2,56% | FEEDBACK RAPIDO |
| DOGE | 21g | Classic technical | CALIBRABILE | 17 | 88,24% | -3,12% | +3,12% | -5,64% | +2,99% | FEEDBACK RAPIDO |
| DOGE | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +0,76% | +0,76% | -1,85% | +6,57% | FEEDBACK RAPIDO |
| DOGE | 30g | Global confluence | BENCHMARK | 11 | 100,00% | -4,16% | +4,16% | -6,73% | +2,45% | FEEDBACK RAPIDO |
| DOGE | 30g | Famiglia statistica | CALIBRABILE | 11 | 100,00% | -4,16% | +4,16% | -6,73% | +2,45% | FEEDBACK RAPIDO |
| DOGE | 30g | Scanner grezzo | DIAGNOSTICO | 11 | 100,00% | -4,16% | +4,16% | -6,73% | +2,45% | FEEDBACK RAPIDO |
| DOGE | 30g | Market regime grezzo | DIAGNOSTICO | 11 | 100,00% | -4,16% | +4,16% | -6,73% | +2,45% | FEEDBACK RAPIDO |
| DOGE | 30g | Tecnico | CALIBRABILE | 11 | 100,00% | -4,16% | +4,16% | -6,73% | +2,45% | FEEDBACK RAPIDO |
| DOGE | 30g | Classic technical | CALIBRABILE | 10 | 100,00% | -3,96% | +3,96% | -6,60% | +2,65% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 31 | 51,61% | +0,02% | -0,18% | -0,48% | +0,68% | PRIMA CALIBRAZIONE |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 34 | 58,82% | -0,25% | +0,01% | -0,71% | +0,37% | PRIMA CALIBRAZIONE |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 37 | 56,76% | -0,14% | -0,08% | -0,62% | +0,49% | PRIMA CALIBRAZIONE |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 32 | 53,12% | -0,09% | +0,04% | -0,66% | +0,51% | PRIMA CALIBRAZIONE |
| SOL | 1g | Tecnico | CALIBRABILE | 36 | 50,00% | -0,08% | -0,02% | -0,58% | +0,51% | PRIMA CALIBRAZIONE |
| SOL | 1g | Classic technical | CALIBRABILE | 21 | 47,62% | +0,04% | -0,04% | -0,54% | +0,59% | FEEDBACK RAPIDO |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 50,00% | +0,17% | +0,17% | -0,04% | +0,81% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 30 | 43,33% | +0,00% | -0,23% | -0,67% | +0,86% | PRIMA CALIBRAZIONE |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 33 | 48,48% | -0,23% | -0,09% | -0,94% | +0,50% | PRIMA CALIBRAZIONE |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 36 | 47,22% | -0,18% | -0,11% | -0,87% | +0,69% | PRIMA CALIBRAZIONE |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 31 | 45,16% | -0,16% | -0,13% | -0,87% | +0,71% | PRIMA CALIBRAZIONE |
| SOL | 2g | Tecnico | CALIBRABILE | 35 | 40,00% | -0,13% | -0,20% | -0,79% | +0,75% | PRIMA CALIBRAZIONE |
| SOL | 2g | Classic technical | CALIBRABILE | 21 | 47,62% | +0,02% | -0,02% | -0,52% | +0,51% | FEEDBACK RAPIDO |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 0,00% | -0,82% | -0,82% | -0,93% | +0,46% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 29 | 44,83% | +0,10% | -0,21% | -1,83% | +1,90% | FEEDBACK RAPIDO |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 32 | 43,75% | -0,30% | -0,06% | -2,14% | +1,60% | PRIMA CALIBRAZIONE |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 35 | 42,86% | -0,25% | -0,08% | -2,06% | +1,75% | PRIMA CALIBRAZIONE |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 30 | 43,33% | -0,19% | -0,26% | -1,98% | +1,77% | PRIMA CALIBRAZIONE |
| SOL | 3g | Tecnico | CALIBRABILE | 34 | 44,12% | -0,18% | -0,17% | -2,01% | +1,82% | PRIMA CALIBRAZIONE |
| SOL | 3g | Classic technical | CALIBRABILE | 21 | 42,86% | +0,13% | -0,13% | -1,91% | +1,82% | FEEDBACK RAPIDO |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 0,00% | -1,86% | -1,86% | -2,68% | +1,03% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 27 | 48,15% | -0,10% | -0,30% | -2,59% | +2,61% | FEEDBACK RAPIDO |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 30 | 50,00% | -0,33% | -0,09% | -2,88% | +2,31% | PRIMA CALIBRAZIONE |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 33 | 48,48% | -0,23% | -0,15% | -2,80% | +2,46% | PRIMA CALIBRAZIONE |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 28 | 46,43% | -0,42% | -0,16% | -2,75% | +2,42% | FEEDBACK RAPIDO |
| SOL | 5g | Tecnico | CALIBRABILE | 32 | 46,88% | -0,28% | -0,24% | -2,88% | +2,55% | PRIMA CALIBRAZIONE |
| SOL | 5g | Classic technical | CALIBRABILE | 21 | 52,38% | +0,14% | -0,14% | -2,60% | +2,64% | FEEDBACK RAPIDO |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 0,00% | -2,33% | -2,33% | -3,87% | +1,03% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 27 | 55,56% | -0,05% | +0,15% | -3,04% | +2,97% | FEEDBACK RAPIDO |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 30 | 60,00% | -0,40% | +0,37% | -3,32% | +2,72% | PRIMA CALIBRAZIONE |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 33 | 60,61% | -0,37% | +0,35% | -3,26% | +2,83% | PRIMA CALIBRAZIONE |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 28 | 53,57% | -0,15% | -0,08% | -3,18% | +2,83% | FEEDBACK RAPIDO |
| SOL | 7g | Tecnico | CALIBRABILE | 32 | 37,50% | -0,34% | -0,30% | -3,35% | +2,93% | PRIMA CALIBRAZIONE |
| SOL | 7g | Classic technical | CALIBRABILE | 21 | 42,86% | -0,04% | +0,04% | -3,16% | +3,15% | FEEDBACK RAPIDO |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 0,00% | -3,55% | -3,55% | -4,19% | +1,03% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 24 | 54,17% | -0,06% | +0,26% | -3,55% | +3,66% | FEEDBACK RAPIDO |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 27 | 59,26% | -0,18% | +0,63% | -3,92% | +3,31% | FEEDBACK RAPIDO |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 30 | 56,67% | -0,18% | +0,58% | -3,88% | +3,37% | PRIMA CALIBRAZIONE |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 25 | 52,00% | +0,23% | +0,01% | -3,76% | +3,48% | FEEDBACK RAPIDO |
| SOL | 10g | Tecnico | CALIBRABILE | 31 | 48,39% | -0,28% | +0,13% | -3,90% | +3,38% | PRIMA CALIBRAZIONE |
| SOL | 10g | Classic technical | CALIBRABILE | 21 | 52,38% | -0,08% | +0,08% | -3,74% | +3,68% | FEEDBACK RAPIDO |
| SOL | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -5,36% | -5,36% | -7,47% | +0,62% | FEEDBACK RAPIDO |
| SOL | 10g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 14g | Global confluence | BENCHMARK | 20 | 60,00% | -1,32% | +0,49% | -4,80% | +3,68% | FEEDBACK RAPIDO |
| SOL | 14g | Famiglia statistica | CALIBRABILE | 23 | 78,26% | -0,54% | +1,09% | -4,92% | +3,52% | FEEDBACK RAPIDO |
| SOL | 14g | Scanner grezzo | DIAGNOSTICO | 26 | 80,77% | -0,84% | +1,32% | -4,80% | +3,56% | FEEDBACK RAPIDO |
| SOL | 14g | Market regime grezzo | DIAGNOSTICO | 21 | 57,14% | -0,28% | -0,12% | -4,58% | +3,73% | FEEDBACK RAPIDO |
| SOL | 14g | Tecnico | CALIBRABILE | 27 | 40,74% | -0,96% | +0,21% | -4,88% | +3,57% | FEEDBACK RAPIDO |
| SOL | 14g | Classic technical | CALIBRABILE | 19 | 42,11% | -0,13% | +0,13% | -4,66% | +4,08% | FEEDBACK RAPIDO |
| SOL | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -5,80% | -5,80% | -9,62% | +0,62% | FEEDBACK RAPIDO |
| SOL | 14g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 21g | Global confluence | BENCHMARK | 15 | 60,00% | -2,44% | +0,07% | -7,02% | +3,01% | FEEDBACK RAPIDO |
| SOL | 21g | Famiglia statistica | CALIBRABILE | 16 | 68,75% | -2,10% | +1,39% | -6,97% | +2,71% | FEEDBACK RAPIDO |
| SOL | 21g | Scanner grezzo | DIAGNOSTICO | 19 | 73,68% | -2,20% | +1,60% | -6,83% | +2,90% | FEEDBACK RAPIDO |
| SOL | 21g | Market regime grezzo | DIAGNOSTICO | 14 | 35,71% | -2,02% | -0,80% | -6,71% | +2,92% | FEEDBACK RAPIDO |
| SOL | 21g | Tecnico | CALIBRABILE | 20 | 60,00% | -2,06% | -0,00% | -6,84% | +2,94% | FEEDBACK RAPIDO |
| SOL | 21g | Classic technical | CALIBRABILE | 12 | 66,67% | -0,54% | +0,54% | -6,52% | +3,34% | FEEDBACK RAPIDO |
| SOL | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -3,18% | -3,18% | -9,62% | +0,62% | FEEDBACK RAPIDO |
| SOL | 21g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | FEEDBACK RAPIDO |
| SOL | 30g | Global confluence | BENCHMARK | 10 | 40,00% | -0,97% | -0,80% | -7,36% | +3,35% | FEEDBACK RAPIDO |
| SOL | 30g | Famiglia statistica | CALIBRABILE | 8 | 75,00% | -1,58% | +0,89% | -7,77% | +2,92% | FEEDBACK RAPIDO |
| SOL | 30g | Scanner grezzo | DIAGNOSTICO | 11 | 63,64% | -1,09% | +0,58% | -7,51% | +3,19% | FEEDBACK RAPIDO |
| SOL | 30g | Market regime grezzo | DIAGNOSTICO | 7 | 57,14% | -1,24% | -0,64% | -7,67% | +3,09% | FEEDBACK RAPIDO |
| SOL | 30g | Tecnico | CALIBRABILE | 11 | 36,36% | -1,09% | -0,61% | -7,51% | +3,19% | FEEDBACK RAPIDO |
| SOL | 30g | Classic technical | CALIBRABILE | 4 | 50,00% | -0,10% | +0,10% | -6,39% | +4,25% | FEEDBACK RAPIDO |
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

Generato: 2026-08-18 05:32 UTC

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
| BTC | 39 | PRIMA CALIBRAZIONE | 38 | 9 | 0 | 0 | Famiglia statistica | 1g | 52,63% | +0,04% | prima calibrazione possibile, solo modifiche leggere |
| SOL | 39 | PRIMA CALIBRAZIONE | 36 | 11 | 0 | 0 | Tecnico | 1g | 50,00% | -0,02% | prima calibrazione possibile, solo modifiche leggere |
| DOGE | 39 | PRIMA CALIBRAZIONE | 38 | 12 | 0 | 0 | Famiglia statistica | 1g | 52,63% | +0,18% | prima calibrazione possibile, solo modifiche leggere |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Classic technical | 8 | 12,50% | -0,66% | +0,66% | +0,09% | +0,94% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Famiglia statistica | 38 | 52,63% | +0,04% | +0,04% | -0,28% | +0,54% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 1g | BREVE | Microstruttura exchange | 1 | 100,00% | +2,00% | +2,00% | +1,48% | +2,25% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 33 | 33,33% | -0,42% | +0,19% | -0,15% | +0,69% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 2g | BREVE | Classic technical | 7 | 14,29% | -0,89% | +0,89% | +0,49% | +1,50% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Famiglia statistica | 37 | 51,35% | +0,07% | +0,07% | -0,39% | +0,75% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 2g | BREVE | Microstruttura exchange | 1 | 100,00% | +3,18% | +3,18% | +3,05% | +3,89% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 32 | 40,62% | -0,43% | +0,25% | -0,20% | +0,92% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 3g | BREVE | Classic technical | 6 | 16,67% | -1,26% | +1,26% | -0,39% | +2,22% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Famiglia statistica | 36 | 52,78% | +0,02% | +0,02% | -1,31% | +1,57% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 3g | BREVE | Microstruttura exchange | 1 | 100,00% | +1,88% | +1,88% | +1,44% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 31 | 32,26% | -0,52% | +0,34% | -1,08% | +1,83% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 5g | SETTIMANALE | Classic technical | 4 | 25,00% | -1,14% | +1,14% | -1,16% | +2,94% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 34 | 38,24% | -0,08% | -0,08% | -2,07% | +2,08% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 5g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -0,16% | -0,16% | -0,37% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 29 | 37,93% | -0,74% | +0,10% | -1,83% | +2,30% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Classic technical | 4 | 0,00% | -1,94% | +1,94% | -1,23% | +3,13% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 34 | 50,00% | -0,05% | -0,05% | -2,35% | +2,37% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 7g | SETTIMANALE | Microstruttura exchange | 1 | 100,00% | +1,77% | +1,77% | -0,79% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 29 | 34,48% | -0,86% | +0,33% | -2,10% | +2,59% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Classic technical | 4 | 0,00% | -1,32% | +1,32% | -1,42% | +3,31% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 31 | 48,39% | +0,05% | +0,05% | -2,64% | +2,83% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 10g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -0,43% | -0,43% | -2,30% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 26 | 30,77% | -0,37% | +0,28% | -2,34% | +3,14% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Classic technical | 4 | 50,00% | -0,27% | +0,27% | -1,55% | +3,37% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Famiglia statistica | 27 | 44,44% | -0,10% | -0,10% | -2,83% | +3,32% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Microstruttura exchange | 1 | 0,00% | -2,25% | -2,25% | -3,05% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 22 | 59,09% | +0,10% | +0,17% | -2,46% | +3,69% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Classic technical | 1 | 0,00% | -1,21% | +1,21% | -1,82% | +3,19% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Famiglia statistica | 20 | 40,00% | -0,65% | -0,65% | -3,27% | +3,49% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Microstruttura exchange | 1 | 100,00% | +1,21% | +1,21% | -3,06% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Tecnico | 16 | 25,00% | -0,16% | -0,26% | -2,90% | +3,94% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Famiglia statistica | 11 | 54,55% | +0,10% | +0,10% | -2,62% | +4,99% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Tecnico | 10 | 50,00% | -0,49% | -0,02% | -2,56% | +5,01% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 25 | 40,00% | -0,20% | +0,20% | -0,31% | +0,75% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Famiglia statistica | 38 | 52,63% | +0,18% | -0,14% | -0,61% | +0,55% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 1g | BREVE | Microstruttura exchange | 4 | 50,00% | +1,13% | +1,92% | +0,84% | +2,11% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 33 | 51,52% | +0,13% | -0,13% | -0,60% | +0,48% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Classic technical | 24 | 45,83% | -0,18% | +0,18% | -0,45% | +1,20% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Famiglia statistica | 37 | 48,65% | +0,02% | -0,23% | -0,86% | +0,78% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Microstruttura exchange | 4 | 50,00% | +2,46% | +3,12% | +2,21% | +3,52% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 32 | 59,38% | +0,28% | -0,29% | -0,89% | +0,60% | PESO OK | 0,0 | MEDIA |
| DOGE | 3g | BREVE | Classic technical | 23 | 39,13% | +0,05% | -0,05% | -1,78% | +2,33% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Famiglia statistica | 36 | 47,22% | -0,07% | -0,42% | -1,86% | +1,80% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 3g | BREVE | Microstruttura exchange | 4 | 50,00% | +1,18% | +1,70% | -0,25% | +5,07% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 31 | 48,39% | +0,45% | -0,50% | -1,99% | +1,63% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 5g | SETTIMANALE | Classic technical | 22 | 54,55% | +0,40% | -0,40% | -2,68% | +2,79% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 34 | 47,06% | +0,08% | -0,68% | -2,71% | +2,30% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 5g | SETTIMANALE | Microstruttura exchange | 4 | 50,00% | +0,23% | +0,64% | -0,37% | +5,72% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 30 | 63,33% | +0,75% | -0,75% | -2,89% | +2,13% | PESO OK | 0,0 | MEDIA |
| DOGE | 7g | SETTIMANALE | Classic technical | 22 | 54,55% | +0,91% | -0,91% | -3,18% | +2,88% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 34 | 55,88% | +0,33% | -0,93% | -3,12% | +2,57% | PESO OK | 0,0 | MEDIA |
| DOGE | 7g | SETTIMANALE | Microstruttura exchange | 4 | 50,00% | +0,36% | +0,63% | -0,50% | +5,72% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 30 | 63,33% | +1,05% | -1,05% | -3,36% | +2,36% | PESO OK | 0,0 | MEDIA |
| DOGE | 10g | SETTIMANALE | Classic technical | 21 | 61,90% | +1,18% | -1,18% | -3,82% | +2,85% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 31 | 51,61% | +0,67% | -1,37% | -3,80% | +2,68% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 10g | SETTIMANALE | Microstruttura exchange | 3 | 66,67% | +0,22% | +1,23% | -1,27% | +6,23% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 30 | 66,67% | +1,40% | -1,40% | -3,88% | +2,63% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 14g | SWING | Classic technical | 20 | 70,00% | +2,09% | -2,09% | -4,80% | +3,07% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Famiglia statistica | 27 | 62,96% | +1,33% | -2,14% | -4,77% | +2,77% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Microstruttura exchange | 2 | 100,00% | +0,46% | +0,46% | -1,85% | +6,57% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 27 | 74,07% | +2,14% | -2,14% | -4,77% | +2,77% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Classic technical | 17 | 88,24% | +3,12% | -3,12% | -5,64% | +2,99% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Famiglia statistica | 20 | 80,00% | +2,54% | -3,38% | -5,90% | +2,56% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Microstruttura exchange | 2 | 100,00% | +0,76% | +0,76% | -1,85% | +6,57% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Tecnico | 20 | 90,00% | +3,38% | -3,38% | -5,90% | +2,56% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Classic technical | 10 | 100,00% | +3,96% | -3,96% | -6,60% | +2,65% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Famiglia statistica | 11 | 100,00% | +4,16% | -4,16% | -6,73% | +2,45% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Tecnico | 11 | 100,00% | +4,16% | -4,16% | -6,73% | +2,45% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Classic technical | 21 | 47,62% | -0,04% | +0,04% | -0,54% | +0,59% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Famiglia statistica | 34 | 58,82% | +0,01% | -0,25% | -0,71% | +0,37% | PESO OK | 0,0 | MEDIA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 2 | 50,00% | +0,17% | +0,17% | -0,04% | +0,81% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 36 | 50,00% | -0,02% | -0,08% | -0,58% | +0,51% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Classic technical | 21 | 47,62% | -0,02% | +0,02% | -0,52% | +0,51% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Famiglia statistica | 33 | 48,48% | -0,09% | -0,23% | -0,94% | +0,50% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Microstruttura exchange | 2 | 0,00% | -0,82% | -0,82% | -0,93% | +0,46% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 35 | 40,00% | -0,20% | -0,13% | -0,79% | +0,75% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 3g | BREVE | Classic technical | 21 | 42,86% | -0,13% | +0,13% | -1,91% | +1,82% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Famiglia statistica | 32 | 43,75% | -0,06% | -0,30% | -2,14% | +1,60% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Microstruttura exchange | 2 | 0,00% | -1,86% | -1,86% | -2,68% | +1,03% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 34 | 44,12% | -0,17% | -0,18% | -2,01% | +1,82% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Classic technical | 21 | 52,38% | -0,14% | +0,14% | -2,60% | +2,64% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 30 | 50,00% | -0,09% | -0,33% | -2,88% | +2,31% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Microstruttura exchange | 2 | 0,00% | -2,33% | -2,33% | -3,87% | +1,03% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 32 | 46,88% | -0,24% | -0,28% | -2,88% | +2,55% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Classic technical | 21 | 42,86% | +0,04% | -0,04% | -3,16% | +3,15% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 30 | 60,00% | +0,37% | -0,40% | -3,32% | +2,72% | PESO OK | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Microstruttura exchange | 2 | 0,00% | -3,55% | -3,55% | -4,19% | +1,03% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 32 | 37,50% | -0,30% | -0,34% | -3,35% | +2,93% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 10g | SETTIMANALE | Classic technical | 21 | 52,38% | +0,08% | -0,08% | -3,74% | +3,68% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 27 | 59,26% | +0,63% | -0,18% | -3,92% | +3,31% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -5,36% | -5,36% | -7,47% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 31 | 48,39% | +0,13% | -0,28% | -3,90% | +3,38% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 14g | SWING | Classic technical | 19 | 42,11% | +0,13% | -0,13% | -4,66% | +4,08% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Famiglia statistica | 23 | 78,26% | +1,09% | -0,54% | -4,92% | +3,52% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Frattale SOL | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Microstruttura exchange | 1 | 0,00% | -5,80% | -5,80% | -9,62% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Tecnico | 27 | 40,74% | +0,21% | -0,96% | -4,88% | +3,57% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Classic technical | 12 | 66,67% | +0,54% | -0,54% | -6,52% | +3,34% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Famiglia statistica | 16 | 68,75% | +1,39% | -2,10% | -6,97% | +2,71% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Frattale SOL | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Microstruttura exchange | 1 | 0,00% | -3,18% | -3,18% | -9,62% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Tecnico | 20 | 60,00% | -0,00% | -2,06% | -6,84% | +2,94% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Classic technical | 4 | 50,00% | +0,10% | -0,10% | -6,39% | +4,25% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Famiglia statistica | 8 | 75,00% | +0,89% | -1,58% | -7,77% | +2,92% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Frattale SOL | 1 | 0,00% | -4,50% | -4,50% | -9,39% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Tecnico | 11 | 36,36% | -0,61% | -1,09% | -7,51% | +3,19% | OSSERVA | 0,0 | BASSA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 36 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 36 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 38 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Classic technical | 21 | 14,29% | -0,91% |
| BTC | BREVE | Famiglia statistica | 111 | 52,25% | +0,05% |
| BTC | BREVE | Microstruttura exchange | 3 | 100,00% | +2,36% |
| BTC | BREVE | Tecnico | 96 | 35,42% | -0,45% |
| BTC | SETTIMANALE | Classic technical | 12 | 8,33% | -1,47% |
| BTC | SETTIMANALE | Famiglia statistica | 99 | 45,45% | -0,03% |
| BTC | SETTIMANALE | Microstruttura exchange | 3 | 33,33% | +0,39% |
| BTC | SETTIMANALE | Tecnico | 84 | 34,52% | -0,67% |
| BTC | SWING | Classic technical | 5 | 40,00% | -0,46% |
| BTC | SWING | Famiglia statistica | 47 | 42,55% | -0,33% |
| BTC | SWING | Microstruttura exchange | 2 | 50,00% | -0,52% |
| BTC | SWING | Tecnico | 38 | 44,74% | -0,01% |
| BTC | MEDIO | Famiglia statistica | 11 | 54,55% | +0,10% |
| BTC | MEDIO | Tecnico | 10 | 50,00% | -0,49% |
| DOGE | BREVE | Classic technical | 72 | 41,67% | -0,11% |
| DOGE | BREVE | Famiglia statistica | 111 | 49,55% | +0,05% |
| DOGE | BREVE | Microstruttura exchange | 12 | 50,00% | +1,59% |
| DOGE | BREVE | Tecnico | 96 | 53,12% | +0,28% |
| DOGE | SETTIMANALE | Classic technical | 65 | 56,92% | +0,83% |
| DOGE | SETTIMANALE | Famiglia statistica | 99 | 51,52% | +0,35% |
| DOGE | SETTIMANALE | Microstruttura exchange | 11 | 54,55% | +0,28% |
| DOGE | SETTIMANALE | Tecnico | 90 | 64,44% | +1,07% |
| DOGE | SWING | Classic technical | 37 | 78,38% | +2,56% |
| DOGE | SWING | Famiglia statistica | 47 | 70,21% | +1,84% |
| DOGE | SWING | Microstruttura exchange | 4 | 100,00% | +0,61% |
| DOGE | SWING | Tecnico | 47 | 80,85% | +2,67% |
| DOGE | MEDIO | Classic technical | 10 | 100,00% | +3,96% |
| DOGE | MEDIO | Famiglia statistica | 11 | 100,00% | +4,16% |
| DOGE | MEDIO | Tecnico | 11 | 100,00% | +4,16% |
| SOL | BREVE | Classic technical | 63 | 46,03% | -0,06% |
| SOL | BREVE | Famiglia statistica | 99 | 50,51% | -0,05% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 6 | 16,67% | -0,83% |
| SOL | BREVE | Tecnico | 105 | 44,76% | -0,13% |
| SOL | SETTIMANALE | Classic technical | 63 | 49,21% | -0,00% |
| SOL | SETTIMANALE | Famiglia statistica | 87 | 56,32% | +0,29% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Microstruttura exchange | 5 | 0,00% | -3,42% |
| SOL | SETTIMANALE | Tecnico | 95 | 44,21% | -0,14% |
| SOL | SWING | Classic technical | 31 | 51,61% | +0,29% |
| SOL | SWING | Famiglia statistica | 39 | 74,36% | +1,21% |
| SOL | SWING | Frattale SOL | 2 | 0,00% | -3,49% |
| SOL | SWING | Microstruttura exchange | 2 | 0,00% | -4,49% |
| SOL | SWING | Tecnico | 47 | 48,94% | +0,12% |
| SOL | MEDIO | Classic technical | 4 | 50,00% | +0,10% |
| SOL | MEDIO | Famiglia statistica | 8 | 75,00% | +0,89% |
| SOL | MEDIO | Frattale SOL | 1 | 0,00% | -4,50% |
| SOL | MEDIO | Tecnico | 11 | 36,36% | -0,61% |

## Aree ancora in attesa

| Asset | Famiglia | Righe senza controlli | Stato |
| --- | --- | --- | --- |
| BTC | BREVE | 3 | in attesa di controlli maturati |
| BTC | SETTIMANALE | 3 | in attesa di controlli maturati |
| BTC | SWING | 2 | in attesa di controlli maturati |
| BTC | MEDIO | 13 | in attesa di controlli maturati |
| SOL | MEDIO | 11 | in attesa di controlli maturati |
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
| BTC     |         39 |              11 |          28 | RACCOLTA DATI | 0,00%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| SOL     |         39 |              11 |          28 | RACCOLTA DATI | 9,09%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| DOGE    |         39 |              11 |          28 | RACCOLTA DATI | 0,00%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |

Regola: sotto 60 controlli osserva soltanto; da 100+ controlli può diventare utile per correggere rischio spot/leva nel Decision Report.

## Ultima lettura rapida

| Asset   | Rischio spot   | Rischio leva   | Nota leva                                             |
|:--------|:---------------|:---------------|:------------------------------------------------------|
| BTC     | BASSO          | ALTO           | leva da limitare; 2x/3x solo con invalidazione chiara |
| SOL     | BASSO          | MEDIO          | leva moderata possibile solo con stop e margine       |
| DOGE    | MEDIO          | MOLTO ALTO     | leva da limitare; 2x/3x solo con invalidazione chiara |
<!-- RISK_CALIBRATION_END -->

</details>
<!-- COMPACT_SECTION_END:risk_calibration -->

<!-- COMPACT_SECTION_START:global_confluence -->
<details open>
<summary><strong>🌐 Global Confluence — quadro finale</strong></summary>

<!-- GLOBAL_CONFLUENCE_START -->
# Sintesi finale di confluenza

Generato: 2026-08-18 05:32 UTC


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
| BTC | 0 | MISTA / PARZIALE | Neutrale / misto | BASSA / RACCOLTA DATI | HOLD / ATTESA CONFERME | Prima resistenza sopra 65.402; conferma del doppio minimo sopra 66.910. | Sotto 62.227 il quadro tecnico peggiora. |
| SOL | +1 | MISTA / PARZIALE | Neutrale / misto | BASSA / RACCOLTA DATI | HOLD LEGGERO / ATTESA CONFERME | conferma del doppio minimo sopra 83,81; nuova conferma tecnica sopra 77,62; milestone analogiche 79,48 / 91,85, valide soltanto se rientra anche il gap frattale. | Allarmi sotto 69,83 / 70,69 / 62,19. |
| DOGE | +3 | MODERATAMENTE POSITIVA | Costruttivo prudente | MEDIA | SOLO TRANCHE PICCOLE / NO LEVA | Sopra 0.07286 migliora; sopra 0.06933 viene invalidato il pattern ribassista dominante. | Sotto 0.06895 il rischio ribassista aumenta. |

## Punteggi per modulo

| Asset | Scanner grezzo | Market grezzo | Famiglia statistica | Scanner path | Tecnico | Classic tech | Frattale SOL | Fractal path | RSI top-cycle | Lifecycle EMA | Exchange flow | Futures | Daily change | Totale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +2 | 0 | +2 | 0 | -1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | -1 | 0 |
| SOL | +3 | +2 | +3 | 0 | -2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | +1 |
| DOGE | +3 | +2 | +4 | 0 | 0 | -1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | +3 |

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

- Famiglia statistica: **+2** — Scanner grezzo +2, Market Regime grezzo 0, match regime 24. Regime neutro: resta il punteggio Scanner. Punteggio contato nel Global: +2.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **+2** — Casi positivi 62,50%, return centrale 30g +4,07%. Direzione scanner: SALITA. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **0** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 24, positivi 30g 54,17%, return p50 +4,07%.
- Scanner path: **0** — Controlli disponibili 37. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **-1** — Score tecnico -1/12, verdetto neutrale / misto, trend misto, struttura compressione / triangolo, divergenza nessuna, Wyckoff possibile accumulazione, pattern score 0 (rialzista Doppio minimo / CANDIDATO; ribassista Doppio massimo / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **0** — Score classico -1/12, verdetto NEUTRALE / MISTO, stage STAGE 4 / MARKDOWN, struttura MASSIMI E MINIMI CRESCENTI, Wyckoff ACCUMULO POSSIBILE / RANGE BASSO, volatilità locale BASSO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Non applicabile a questo asset.
- Fractal path: **0** — Non applicabile a questo asset.
- RSI top-cycle: **0** — Non applicabile a questo asset.
- Lifecycle EMA: **0** — Non applicabile a questo asset.
- Exchange flow: **0** — Flow +1.75, derivati +0.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +1.25; exchange 3/3, copertura 100%, consenso bull 1, bear 0, divergenze 0, campioni 4h 8 su 3.50h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias LEGGERMENTE POSITIVA / NON PESATA; confidenza MEDIA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Misto, forza 1/5.
- Daily change: **-1** — BTC: cambiamento medio in peggioramento rispetto a ieri.

Conferme: Prima resistenza sopra 65.402; conferma del doppio minimo sopra 66.910.

Invalidazioni: Sotto 62.227 il quadro tecnico peggiora.

### SOL

- Confluenza: **MISTA / PARZIALE**
- Bias: **Neutrale / misto**
- Punteggio finale: **+1**
- Affidabilità: **BASSA / RACCOLTA DATI**
- Azione coerente: **HOLD LEGGERO / ATTESA CONFERME**

SOL è ancora in zona mista. Il frattale resta soltanto uno scenario contestuale: non è confermato dal prezzo e vale 0 punti operativi finché il gap non rientra. Meglio evitare leva e ragionare solo a tranche piccole.

Dettaglio moduli:

- Famiglia statistica: **+3** — Scanner grezzo +3, Market Regime grezzo +2, match regime 9. Scanner e regime concordi, ma i match sono meno di 10: nessun bonus. Punteggio contato nel Global: +3.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **+3** — Casi positivi 70,00%, return centrale 30g +6,93%. Direzione scanner: SALITA. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **+2** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 9, positivi 30g 77,78%, return p50 +4,18%.
- Scanner path: **0** — Controlli disponibili 37. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **-2** — Score tecnico -3/12, verdetto debole, trend misto, struttura ribassista con massimi e minimi decrescenti, divergenza nessuna, Wyckoff markdown / fase ribassista, pattern score 0 (rialzista Doppio minimo / CANDIDATO; ribassista Doppio massimo / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **0** — Score classico -2/12, verdetto DEBOLE / NON CONFERMATO, stage STAGE 4 / MARKDOWN, struttura VOLATILITÀ IN ESPANSIONE, Wyckoff ACCUMULO POSSIBILE / RANGE BASSO, volatilità locale BASSO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Verdetto ANALOGIA DEBOLE / SCENARIO SECONDARIO, somiglianza strutturale +57,65%, aderenza live +68,74%, errore live +15,63%, gap corrente -18,13%, peso operativo 0, tracking STRUTTURA STABILE, fase FRATTALE SOLO DI CONTESTO, rischio ALTO.
- Fractal path: **0** — Controlli disponibili 35, ma percorso ancorato non aderente: gap -18,13%, errore live +15,63%. Peso 0.
- RSI top-cycle: **0** — Rischio top-cycle RSI: BASSO.
- Lifecycle EMA: **0** — Contesto non pesato nel Global. Lifecycle score 4, bias SQUEEZE SETUP MODERATO, EMA200 111,29 $, upside EMA200 +47,09%, gap EMA50/EMA200 -6,30%, hit EMA200 12w +33,33%, trend STABILE / DA CONFERMARE. Peso Global forzato a 0.
- Exchange flow: **0** — Flow +1.75, derivati +0.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +1.00; exchange 3/3, copertura 100%, consenso bull 1, bear 0, divergenze 0, campioni 4h 8 su 3.50h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias LEGGERMENTE POSITIVA / NON PESATA; confidenza MEDIA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Misto, forza 1/5.
- Daily change: **0** — SOL: nessun cambiamento forte in miglioramento rispetto a ieri.

Conferme: conferma del doppio minimo sopra 83,81; nuova conferma tecnica sopra 77,62; milestone analogiche 79,48 / 91,85, valide soltanto se rientra anche il gap frattale.

Invalidazioni: Allarmi sotto 69,83 / 70,69 / 62,19.

### DOGE

- Confluenza: **MODERATAMENTE POSITIVA**
- Bias: **Costruttivo prudente**
- Punteggio finale: **+3**
- Affidabilità: **MEDIA**
- Azione coerente: **SOLO TRANCHE PICCOLE / NO LEVA**

DOGE non ha ancora una confluenza pulita. Serve conferma tecnica prima di trattarlo come asset forte.

Dettaglio moduli:

- Famiglia statistica: **+4** — Scanner grezzo +3, Market Regime grezzo +2, match regime 11. Scanner e regime concordi con almeno 10 match: bonus massimo di 1 punto. Punteggio contato nel Global: +4.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **+3** — Casi positivi 72,50%, return centrale 30g +14,02%. Direzione scanner: SALITA. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **+2** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 11, positivi 30g 72,73%, return p50 +9,84%.
- Scanner path: **0** — Controlli disponibili 37. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **0** — Score tecnico 0/12, verdetto neutrale / misto, trend ribassista, struttura rialzista con massimi e minimi crescenti, divergenza nessuna, Wyckoff possibile accumulazione, pattern score 0 (rialzista Doppio minimo / CANDIDATO; ribassista Doppio massimo / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **-1** — Score classico -5/12, verdetto RIBASSISTA / FRAGILE, stage STAGE 4 / MARKDOWN, struttura MASSIMI E MINIMI CRESCENTI, Wyckoff MARKDOWN / DEBOLEZZA, volatilità locale BASSO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Non applicabile a questo asset.
- Fractal path: **0** — Non applicabile a questo asset.
- RSI top-cycle: **0** — Non applicabile a questo asset.
- Lifecycle EMA: **0** — Non applicabile a questo asset.
- Exchange flow: **0** — Flow +1.75, derivati +0.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +1.25; exchange 3/3, copertura 100%, consenso bull 1, bear 1, divergenze 0, campioni 4h 8 su 3.50h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias LEGGERMENTE POSITIVA / NON PESATA; confidenza MEDIA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Misto, forza 1/5.
- Daily change: **0** — DOGE: nessun cambiamento forte in peggioramento rispetto a ieri.

Conferme: Sopra 0.07286 migliora; sopra 0.06933 viene invalidato il pattern ribassista dominante.

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

Generato: 2026-08-18 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [btc_macro_cycle_report.md](btc_macro_cycle_report.md)

Questo modulo descrive il contesto macro di Bitcoin. Non genera entrate tattiche, non autorizza leva e pesa **0** nel Global Confluence.

## Sintesi

| Voce | Valore | Lettura |
| --- | --- | --- |
| Prezzo BTC | 64.145 $ | prezzo corrente |
| Power Law centrale | 123.774 $ | deviazione -48,18% |
| Banda p10-p90 | 76.628 $ / 311.866 $ | SOTTO LA BANDA P10 |
| Percentile residuo | 1,17% | posizione storica nel corridoio |
| Esponente β | 5,8175 | R² log-log 91,93% |
| Stabilità β | BASSA | range 1,3157 cambiando finestra |
| Ultimo halving | 2024-04-19 | 851 giorni fa |
| Fase ciclo | 58,25% | percentuale indicativa del ciclo quadriennale |
| Peso Global | 0 | CONTESTO MACRO / DIAGNOSTICO |

La Power Law viene trattata come regressione empirica, non come legge fisica. Il report mostra quanto cambia l'esponente usando finestre iniziali diverse e la confronta con il benchmark ingenuo 'prezzo invariato'.

## Bitcoin Power Law

- Campione: 2014-09-17 → 2026-08-18 (4353 osservazioni)
- Formula stimata: prezzo ≈ exp(-39.1703) × giorni^5.8175
- Prezzo centrale oggi: **123.774 $**
- Posizione corrente: **SOTTO LA BANDA P10**, percentile 1,17%
- Scarto dal centro: **-48,18%**

![Bitcoin Power Law](btc_power_law_chart.png)

![Bitcoin Power Law log-log](btc_power_law_loglog_chart.png)

### Stabilità dell'esponente

| Inizio campione | β | R² log-log |
| --- | --- | --- |
| 2014 | 5,8175 | 91,93% |
| 2015 | 5,9014 | 91,49% |
| 2016 | 5,5871 | 87,72% |
| 2017 | 4,8572 | 82,85% |
| 2018 | 4,5857 | 78,31% |

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
| 2012-11-28 → 2016-07-09 | 2015-01-05 | -17,35% | -5,06% | -4,95% | +57,38% |
| 2016-07-09 → 2020-05-11 | 2018-10-04 | -3,28% | -40,04% | -25,80% | +24,77% |
| 2020-05-11 → 2024-04-19 | 2022-08-27 | -4,09% | -17,56% | +19,49% | +30,18% |

Campione molto piccolo: questi rendimenti sono contesto di ciclo, non probabilità affidabili.

## SOL/BTC e DOGE/BTC dentro il tempo Bitcoin

![Altcoin nel ciclo BTC](alt_btc_cycle_spirals.png)

| Asset | Coppia | Forza vs BTC | Score raw | Candidato | 30g | Peso Global |
| --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | RELATIVA MISTA / NON CONFERMATA | 0 | 0 | 1.373390995389956 | 0 |
| DOGE | DOGE/BTC | RELATIVA MISTA / NON CONFERMATA | -3 | 0 | -2.857957902771402 | 0 |

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

Generato: 2026-08-18 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [relative_strength_btc_report.md](relative_strength_btc_report.md)

Questo modulo controlla se SOL e DOGE stanno davvero battendo Bitcoin. Una salita in USD accompagnata da una coppia ALT/BTC ribassista è spesso soltanto trascinamento di BTC.

**Protezione iniziale:** il candidato relativo è limitato a -1/0/+1, ma il peso nel Global resta **0**. La coppia BTC conferma o indebolisce il tecnico USD; non viene sommata come secondo modulo indipendente.

## Sintesi

| Asset | Coppia | Prezzo | Score raw | Candidato | Peso Global | Forza vs BTC | Confidenza | 30g | Tecnico USD | Lettura combinata |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | 0.00118100 | 0 | 0 | 0 | RELATIVA MISTA / NON CONFERMATA | BASSA | +1,37% | RIBASSISTA | QUADRO MISTO / NESSUNA CONFERMA RELATIVA |
| DOGE | DOGE/BTC | 0.00000109 | -3 | 0 | 0 | RELATIVA MISTA / NON CONFERMATA | BASSA | -2,86% | MISTA | QUADRO MISTO / NESSUNA CONFERMA RELATIVA |

## Matrice di lettura

| ALT/USD | ALT/BTC | Interpretazione |
| --- | --- | --- |
| Rialzista | Rialzista | Conferma migliore: sale e batte BTC |
| Rialzista | Ribassista | Sale soprattutto perché BTC trascina il mercato |
| Ribassista | Rialzista | Forza relativa nascosta / possibile rotazione futura |
| Ribassista | Ribassista | Debolezza completa |

## SOL/BTC

- **Verdetto relativo:** RELATIVA MISTA / NON CONFERMATA (0)
- **Candidato futuro:** 0; **peso attuale Global: 0**
- **Lettura combinata USD/BTC:** QUADRO MISTO / NESSUNA CONFERMA RELATIVA
- **Struttura:** VOLATILITÀ IN ESPANSIONE
- **Rendimenti relativi:** 7g -0,59%; 30g +1,37%; 90g +7,66%; 180g -3,83%
- **Daily:** RSI 51.74; MA50 0.00119656; MA200 0.00118058
- **Weekly:** MA30 0.00118197; RSI 46.58
- **Livelli:** supporto 0.00116400; resistenza 0.00119500; breakout 60g 0.00134900; breakdown 60g 0.00104800
- **Pattern:** DOPPIO MASSIMO / CANDIDATO; neckline 0.00112700; target 0.00107050
- **Fibonacci:** VICINO — 50.0% a 0.00117900
- **Fonte:** Yahoo Finance SOL-BTC (coppia diretta)
- **Motivi score:** prezzo sotto MA50 daily; prezzo sopra MA200 daily; MA50 daily in salita; prezzo sotto MA30 weekly; MA30 weekly in discesa; MACD relativo positivo

![Grafico SOL/BTC](relative_strength_SOLBTC.png)

## DOGE/BTC

- **Verdetto relativo:** RELATIVA MISTA / NON CONFERMATA (-3)
- **Candidato futuro:** 0; **peso attuale Global: 0**
- **Lettura combinata USD/BTC:** QUADRO MISTO / NESSUNA CONFERMA RELATIVA
- **Struttura:** MASSIMI E MINIMI CRESCENTI
- **Rendimenti relativi:** 7g -0,36%; 30g -2,86%; 90g -18,98%; 180g -26,74%
- **Daily:** RSI 43.82; MA50 0.00000113; MA200 0.00000130
- **Weekly:** MA30 0.00000129; RSI 32.13
- **Livelli:** supporto 0.00000105; resistenza 0.00000114; breakout 60g 0.00000140; breakdown 60g 0.00000104
- **Pattern:** DOPPIO MASSIMO / CONFERMATO; neckline 0.00000112; target 0.00000099
- **Fibonacci:** NON ATTIVO — 23.6% a 0.00000115
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
| SOL | 1g | 16 | 62,50% | -0,25% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 3g | 16 | 43,75% | -0,65% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 7g | 15 | 40,00% | -1,47% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 14g | 11 | 9,09% | -2,34% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 30g | 0 | n/a | n/a | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 1g | 34 | 70,59% | +0,29% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 3g | 34 | 61,76% | +0,58% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 7g | 32 | 68,75% | +0,97% | ELIGIBILE FUTURO ±1 | 0 |
| DOGE | 14g | 25 | 80,00% | +1,71% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 30g | 9 | 100,00% | +3,58% | LOCKED / RACCOLTA LIVE | 0 |

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

Ultima candela SOL usata: **18 agosto 2026**

## Verdetto: ANALOGIA DEBOLE / SCENARIO SECONDARIO

- **Fase attuale:** FRATTALE SOLO DI CONTESTO
- **Somiglianza totale:** +57,65%
- **Somiglianza strutturale:** +57,65%
- **Aderenza prezzo live:** +68,74%
- **Errore medio live:** +15,63%
- **Gap prezzo corrente:** -18,13%
- **Peso operativo suggerito:** 0
- **Affidabilita:** BASSA
- **Rischio fase:** ALTO
- **Trend tracking:** STRUTTURA STABILE
- **Sintesi:** Esistono alcuni elementi comuni, ma non abbastanza per una conferma.
- **SOL è al giorno:** 73 dal bottom usato.
- **Giorno BTC equivalente:** 2023-02-02
- **Prossimo step:** Proiezione condizionale, non conferma operativa: **Prima retest / debolezza, poi recupero.** Zona bassa **69,83 $** intorno al **26 agosto 2026**; zona alta **78,40 $** intorno al **31 agosto 2026**; fine step circa **76,19 $** entro il **1 settembre 2026**.

## Somiglianza prima e dopo inizio programma

Questa sezione separa la somiglianza della forma dall'aderenza reale del prezzo.

- **Inizio programma/scanner:** 3 luglio 2026
- **Prima del programma** = backtest retroattivo.
- **Da inizio programma** = verifica live: è la parte più importante per l'uso operativo.

| Periodo | Date | Giorni | Aderenza prezzo | Errore medio | Gap ultimo | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| Prima del programma | 6 giugno 2026 -> 2 luglio 2026 | 27 | +87,95% | +6,02% | +21,89% | ABBASTANZA ALLINEATO |
| Da inizio programma | 3 luglio 2026 -> 18 agosto 2026 | 47 | +68,74% | +15,63% | -18,13% | STACCATO / NON ADERENTE |
| Totale dal bottom | 6 giugno 2026 -> 18 agosto 2026 | 74 | +75,75% | +12,12% | -18,13% | DEVIAZIONE MODERATA |

Nota: un frattale può avere una forma simile ma un prezzo distante. In quel caso non è operativo finché il gap non rientra.

## Lettura operativa veloce

Il frattale non deve generare acquisti o leva adesso. La forma è un contesto, ma l'aderenza live del prezzo è insufficiente.

| Voce | Risposta | Perché |
| --- | --- | --- |
| Uso operativo | NO | Il frattale vale 0 punti operativi finché il prezzo resta non aderente. |
| Aderenza live | +68,74% | Errore medio live +15,63%. |
| Gap corrente | -18,13% | Deve rientrare circa entro ±12%. |
| Prima conferma prezzo | 79,48 $ | Serve anche miglioramento del gap, non solo una candela sopra il livello. |
| Seconda conferma | 91,85 $ | Rende più credibile il percorso, ma non sostituisce l'aderenza. |
| Invalidazione soft | 69,83 $ | Sotto questa zona il quadro peggiora. |
| Invalidazione forte | 62,19 $ | Sotto il bottom il paragone è quasi rotto. |

## Target ciclo fino al top BTC 2025

| Voce | Valore |
| --- | --- |
| Stato | CONTESTO / NON OPERATIVO |
| Top BTC 2025 | 6 ottobre 2025 - 124.753 $ |
| Data SOL equivalente | 21 aprile 2029 |
| Target ciclo base da oggi | 402,34 $ |
| Massimo percorso base | 402,34 $ (21 aprile 2029) |

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
| Prima conferma | 79,48 $ | Deve accompagnarsi al rientro del gap. |
| Seconda conferma | 91,85 $ | Scenario più credibile. |
| Invalidazione soft | 69,83 $ | Il frattale si indebolisce. |
| Invalidazione forte | 62,19 $ | Il paragone si rompe. |

## Proiezione veloce con date SOL

| Orizzonte | Data SOL | BTC fece | SOL base | Min percorso | Max percorso |
| --- | --- | --- | --- | --- | --- |
| 7 giorni | 25 agosto 2026 | -7,04% | 70,37 $ | 70,37 $ | 75,70 $ |
| 14 giorni | 1 settembre 2026 | +0,65% | 76,19 $ | 69,83 $ | 78,40 $ |
| 30 giorni | 17 settembre 2026 | -4,77% | 72,09 $ | 69,83 $ | 80,08 $ |
| 60 giorni | 17 ottobre 2026 | +18,40% | 89,63 $ | 65,11 $ | 91,85 $ |
| 90 giorni | 16 novembre 2026 | +23,58% | 93,55 $ | 65,11 $ | 98,32 $ |
| 120 giorni | 16 dicembre 2026 | +16,09% | 87,88 $ | 65,11 $ | 98,32 $ |

## Prossimi step se SOL segue BTC 2022

| Step | Date SOL | BTC fine | SOL zona bassa | SOL zona alta | SOL fine base | Lettura |
| --- | --- | --- | --- | --- | --- | --- |
| Step 1 - prossime 2 settimane | 18 agosto 2026 -> 1 settembre 2026 | +0,65% | 69,83 $ (26 agosto 2026) | 78,40 $ (31 agosto 2026) | 76,19 $ | Prima retest / debolezza, poi recupero. |
| Step 2 - primo mese | 2 settembre 2026 -> 17 settembre 2026 | -4,77% | 72,09 $ (17 settembre 2026) | 80,08 $ (5 settembre 2026) | 72,09 $ | Prima spike, poi scarico. |
| Step 3 - secondo mese | 18 settembre 2026 -> 17 ottobre 2026 | +18,40% | 65,11 $ (23 settembre 2026) | 91,85 $ (14 ottobre 2026) | 89,63 $ | Prima retest / debolezza, poi recupero. |
| Step 4 - terzo mese | 18 ottobre 2026 -> 16 novembre 2026 | +23,58% | 87,97 $ (4 novembre 2026) | 98,32 $ (28 ottobre 2026) | 93,55 $ | Spinta rialzista abbastanza pulita. |

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
| Prezzo SOL | 75,70 $ |  |
| Weekly RSI | 40,79 / linea grezza 52,95 | LINEA NON AFFIDABILE / RISCHIO NON ATTIVO — IRREALISTICA / NON OPERATIVA |
| Monthly RSI | 40,98 / linea grezza 55,81 | RSI TROPPO BASSO PER RISCHIO TOP — VALIDA / USO PRUDENTE |
| Target ciclo base | 402,34 $ | Avanzamento +18,81% |
| Rischio top-cycle RSI | BASSO | Nessun segnale top-cycle macro attivo. Prezzo ancora lontano dal target ciclo; il filtro RSI resta solo di monitoraggio. |

## Lettura semplice

- Weekly: La top-line weekly non supera i controlli di qualità. Non viene usata per generare rischio top-cycle.
- Monthly: RSI monthly è 41,0, sotto la soglia prudente 55. Anche se fosse vicino alla linea, non è una vera zona di esaurimento ciclo.
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
| Prezzo SOL | 75,70 $ |
| TVL Solana | 4,84 mld $ |
| TVL 7g | +0,01% |
| DEX volume 24h | 1,43 mld $ |
| Fees 24h | 10,77 mln $ |
| Stablecoin su Solana | 15,92 mld $ |
| Stake ratio | 68,89% |
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
| Confronto precedente | 2026-08-17 |
| Fonte prezzi | Yahoo Finance SOL-USD weekly |
| Prezzo SOL | 75,70 $ |
| EMA200 weekly target | 111,29 $ |
| Upside verso EMA200 | +47,09% |
| Distanza prezzo da EMA200 | -32,01% |
| Gap EMA50/EMA200 | -6,30% |
| Stato cross | EMA50 SOTTO EMA200 |
| RSI weekly | 40,75 |
| Età SOL | 6,4 anni |
| Analoghi storici usati | 30 |
| Max analoghi per asset | 3 |
| Hit EMA200 12w analoghi | +33,33% |
| Max gain mediano 12w | +21,66% |
| Drawdown mediano 12w | -20,91% |

Lettura semplice:

**CONTESTO INTERESSANTE, SERVONO CONFERME DI PREZZO**

Autocontrollo: **STABILE / DA CONFERMARE**.

Questo modulo confronta SOL con altre crypto in fasi simili di età, distanza da EMA200, EMA50/EMA200 e RSI. Non usa stock market.

Nota importante: **questo modulo ora NON pesa più nel Global Confluence**. Resta solo come contesto di ciclo e come mappa verso EMA200 weekly. Il punteggio Global resta guidato da prezzo, scanner, regime, struttura tecnica, frattale, RSI e conferme reali.

Nota: se EMA50/EMA200 sono dentro ±2%, il modulo parla di medie sovrapposte / incrocio in corso, perché exchange diversi possono mostrare il cross leggermente prima o dopo.

<!-- Generato: 2026-08-18 05:32 UTC -->
<!-- MAJOR_ALT_LIFECYCLE_SQUEEZE_END -->

</details>
<!-- COMPACT_SECTION_END:major_alt_lifecycle -->

# Report giornaliero BTC / SOL / DOGE

Aggiornato il: **2026-08-18 05:30:23 UTC**

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
| BTC | CAMBIAMENTO MEDIO | peggioramento | RIALZISTA | +62.50% | -5.00 punti |
| SOL | NESSUN CAMBIAMENTO FORTE | miglioramento | RIALZISTA | +70.00% | 0.00 punti |
| DOGE | NESSUN CAMBIAMENTO FORTE | peggioramento | RIALZISTA | +72.50% | +5.00 punti |

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
| BTC | 60.969 $ | 70.595 $ | +41,18% | +15,79% | rimbalzo debole | 70.595 $ | 60.969 $ | +12,00% | -13,64% | spike storicamente più resistente |
| SOL | 71,91 $ | 83,27 $ | +41,67% | +15,79% | rimbalzo debole | 83,27 $ | 71,91 $ | +3,45% | -13,64% | spike storicamente più resistente |
| DOGE | 0,06627 $ | 0,07674 $ | +55,17% | +15,79% | rimbalzo possibile | 0,07674 $ | 0,06627 $ | +25,81% | -13,64% | spike storicamente più resistente |

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

- **BTC: su 40 casi simili, 17 prima sono scesi a -5,00%. Tra quei 17, 7 poi sono rimbalzati fino a +10,00%. Percentuale: +41,18% (7/17). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.**
- **BTC: su 40 casi simili, 25 prima sono saliti a +10,00%. Tra quei 25, 3 poi sono scaricati a -5,00%. Percentuale: +12,00% (3/25). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.**
- **SOL: su 40 casi simili, 12 prima sono scesi a -5,00%. Tra quei 12, 5 poi sono rimbalzati fino a +10,00%. Percentuale: +41,67% (5/12). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.**
- **SOL: su 40 casi simili, 29 prima sono saliti a +10,00%. Tra quei 29, 1 poi sono scaricati a -5,00%. Percentuale: +3,45% (1/29). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.**
- **DOGE: su 40 casi simili, 29 prima sono scesi a -5,00%. Tra quei 29, 16 poi sono rimbalzati fino a +10,00%. Percentuale: +55,17% (16/29). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo possibile.**
- **DOGE: su 40 casi simili, 31 prima sono saliti a +10,00%. Tra quei 31, 8 poi sono scaricati a -5,00%. Percentuale: +25,81% (8/31). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.**

<!-- BOUNCE_AFTER_DRAWDOWN_END -->

</details>
<!-- COMPACT_SECTION_END:bounce_after_drawdown -->

<!-- COMPACT_SECTION_START:scanner_forecast -->
<details>
<summary><strong>🔭 Cono probabilistico dello scanner</strong></summary>

<!-- SCANNER_FORECAST_TRACKER_START -->
# Scanner forecast path / cono probabilistico

Generato: 2026-08-18 05:31:42 UTC


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
| BTC | 2026-08-18 | 64.178 $ | SALITA | 62,50% | 54.661,39 $ | 61.476,14 $ | 66.790,72 $ | 72.963,28 $ | 86.743,11 $ |
| SOL | 2026-08-18 | 75,70 $ | SALITA | 70,00% | 70,35 $ | 74,55 $ | 80,95 $ | 92,71 $ | 126,83 $ |
| DOGE | 2026-08-18 | 0.06976 $ | SALITA | 72,50% | 0.05643 $ | 0.06715 $ | 0.07954 $ | 0.08993 $ | 0.10126 $ |

## Grafici

### BTC

![Scanner forecast BTC](scanner_forecast_BTC.png)

#### Verifica storica e discrepanza

![Verifica storica cono BTC](scanner_forecast_history_BTC.png)

- Cono congelato il **2026-07-19**; verificato fino al **2026-08-18**; stato **COMPLETO 30/30g**.
- Reale **64.151,99 $**; p50 previsto **67.925,63 $**; scarto **-5,56%**.
- Errore medio assoluto **3,20%**; massimo **6,65%**; DENTRO p10-p90; DENTRO p25-p75.

### SOL

![Scanner forecast SOL](scanner_forecast_SOL.png)

#### Verifica storica e discrepanza

![Verifica storica cono SOL](scanner_forecast_history_SOL.png)

- Cono congelato il **2026-07-19**; verificato fino al **2026-08-18**; stato **COMPLETO 30/30g**.
- Reale **75,65 $**; p50 previsto **75,30 $**; scarto **0,47%**.
- Errore medio assoluto **1,88%**; massimo **6,07%**; DENTRO p10-p90; DENTRO p25-p75.

### DOGE

![Scanner forecast DOGE](scanner_forecast_DOGE.png)

#### Verifica storica e discrepanza

![Verifica storica cono DOGE](scanner_forecast_history_DOGE.png)

- Cono congelato il **2026-07-19**; verificato fino al **2026-08-18**; stato **COMPLETO 30/30g**.
- Reale **0.06971 $**; p50 previsto **0.06223 $**; scarto **12,02%**.
- Errore medio assoluto **6,76%**; massimo **17,13%**; DENTRO p10-p90; DENTRO p25-p75.

## Accuratezza percorso scanner

| Asset   | Giorno   |   Controlli | Dentro p10-p90   | Dentro p25-p75   | Errore medio abs vs p50   | Errore medio vs p50   |
|:--------|:---------|------------:|:-----------------|:-----------------|:--------------------------|:----------------------|
| BTC | 1g | 37 | 100,00% | 64,86% | 1,53% | -0,17% |
| BTC | 3g | 35 | 100,00% | 80,00% | 2,02% | -0,63% |
| BTC | 7g | 33 | 100,00% | 84,85% | 2,79% | -0,56% |
| BTC | 14g | 26 | 100,00% | 88,46% | 3,13% | -0,67% |
| BTC | 30g | 10 | 100,00% | 90,00% | 6,74% | -6,74% |
| SOL | 1g | 37 | 81,08% | 67,57% | 1,85% | -0,35% |
| SOL | 3g | 35 | 100,00% | 80,00% | 2,25% | -0,96% |
| SOL | 7g | 33 | 100,00% | 90,91% | 2,05% | -0,29% |
| SOL | 14g | 26 | 100,00% | 92,31% | 2,00% | 0,54% |
| SOL | 30g | 10 | 100,00% | 100,00% | 1,56% | 0,27% |
| DOGE | 1g | 37 | 97,30% | 67,57% | 2,20% | 0,01% |
| DOGE | 3g | 35 | 100,00% | 88,57% | 2,21% | 0,58% |
| DOGE | 7g | 33 | 93,94% | 90,91% | 4,91% | 3,03% |
| DOGE | 14g | 26 | 100,00% | 73,08% | 6,42% | 4,86% |
| DOGE | 30g | 10 | 100,00% | 50,00% | 13,13% | 13,13% |

## Calibratore shadow

Il cono ufficiale resta grezzo e invariato. Il calibratore usa soltanto previsioni passate già mature, campionate una volta a settimana per ridurre la falsa indipendenza. Ogni orizzonte si attiva a 30 controlli indipendenti: parte al 25% della correzione stimata e cresce gradualmente fino al 100% a 100 controlli.

| Asset   | Orizzonte   |   Controlli indipendenti |   Soglia | Stato                  | Forza correzione   | Shift p50   |   Scala p10-p90 |
|:--------|:------------|-------------------------:|---------:|:-----------------------|:-------------------|:------------|----------------:|
| BTC | 1g | 7 | 30 | RACCOLTA (23 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 3g | 6 | 30 | RACCOLTA (24 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 7g | 6 | 30 | RACCOLTA (24 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 14g | 5 | 30 | RACCOLTA (25 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 30g | 2 | 30 | RACCOLTA (28 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 1g | 7 | 30 | RACCOLTA (23 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 3g | 6 | 30 | RACCOLTA (24 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 7g | 6 | 30 | RACCOLTA (24 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 14g | 5 | 30 | RACCOLTA (25 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 30g | 2 | 30 | RACCOLTA (28 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 1g | 7 | 30 | RACCOLTA (23 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 3g | 6 | 30 | RACCOLTA (24 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 7g | 6 | 30 | RACCOLTA (24 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 14g | 5 | 30 | RACCOLTA (25 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 30g | 2 | 30 | RACCOLTA (28 mancanti) | 0,0% | 0,00% | 1,000 |

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

Righe salvate nello storico: **105**.

Questa sezione tiene un diario delle previsioni giornaliere a 30 giorni, senza appesantire il report principale.

| Data | Asset | Prezzo | Direzione | Casi positivi | Return p50 | Drawdown p50 | Max gain p50 | Controllo 30g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08-18 | BTC | 64.178 $ | SALITA | 62,50% | 66.791 $ | 61.506 $ | 75.615 $ | 2026-09-17 |
| 2026-08-18 | DOGE | 0,07000 $ | SALITA | 72,50% | 0,08000 $ | 0,06000 $ | 0,09000 $ | 2026-09-17 |
| 2026-08-18 | SOL | 75,70 $ | SALITA | 70,00% | 80,95 $ | 73,57 $ | 91,85 $ | 2026-09-17 |

<!-- FORECAST_30D_HISTORY_END -->

</details>
<!-- COMPACT_SECTION_END:scanner_forecast -->

<!-- COMPACT_SECTION_START:extreme_cases -->
<details>
<summary><strong>⚠️ Percorso dei casi estremi</strong></summary>

<!-- EXTREME_CASES_PATH_START -->
# Extreme cases path report

Generato: 2026-08-18 05:31 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [extreme_cases_path_report.md](extreme_cases_path_report.md)

Questo report si attiva quando i casi positivi o negativi sono almeno **80%**.

Ora misura anche il **rialzo massimo prima della discesa principale**, quindi distingue uno spike iniziale da una discesa quasi immediata.

## Trigger estremi

| Asset   | Direzione   | Trigger   | Percentuale   | Motivo                           |   Match disponibili |
|:--------|:------------|:----------|:--------------|:---------------------------------|--------------------:|
| BTC     | NESSUNO     | NO        | +62,50%       | Nessun lato sopra soglia estrema |                  40 |
| SOL     | NESSUNO     | NO        | +70,00%       | Nessun lato sopra soglia estrema |                  40 |
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
- Casi positivi / salita storica: **62,50%**
- Casi negativi / discesa storica: **37,50%**
- Quanto è netto il segnale: **medio**
- Prezzo attuale: **64.177,53 $**
- Return normale fra 30 giorni: **66.790,72 $** (4,07%)
- Drawdown normale durante il mese: **61.506,14 $** (-4,16%)
- Drawdown brutto da rispettare: **57.224,82 $** (-10,83%)
- Max gain normale durante il mese: **75.615,49 $** (17,82%)
- Max gain buono / take profit ottimistico: **83.220,62 $** (29,67%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Solana
- Direzione più probabile a 30 giorni: **SALITA**
- Casi positivi / salita storica: **70,00%**
- Casi negativi / discesa storica: **30,00%**
- Quanto è netto il segnale: **forte**
- Prezzo attuale: **75,70 $**
- Return normale fra 30 giorni: **80,95 $** (6,93%)
- Drawdown normale durante il mese: **73,57 $** (-2,81%)
- Drawdown brutto da rispettare: **70,65 $** (-6,67%)
- Max gain normale durante il mese: **91,85 $** (21,33%)
- Max gain buono / take profit ottimistico: **98,69 $** (30,37%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Dogecoin
- Direzione più probabile a 30 giorni: **SALITA**
- Casi positivi / salita storica: **72,50%**
- Casi negativi / discesa storica: **27,50%**
- Quanto è netto il segnale: **forte**
- Prezzo attuale: **0,07 $**
- Return normale fra 30 giorni: **0,08 $** (14,02%)
- Drawdown normale durante il mese: **0,06 $** (-8,15%)
- Drawdown brutto da rispettare: **0,06 $** (-12,49%)
- Max gain normale durante il mese: **0,09 $** (24,22%)
- Max gain buono / take profit ottimistico: **0,10 $** (37,00%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Messaggio del giorno

Il quadro generale oggi è più favorevole. Lo scanner vede più possibilità di salita su più asset.

---

# Mappa semplice asset per asset

# Bitcoin — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟢 VERDE / Favorevole
**Prezzo attuale:** 64.177,53 $

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

- Se va molto male: **54.661,39 $** (-14,83%)
- Se va male: **61.476,14 $** (-4,21%)
- Scenario normale: **66.790,72 $** (4,07%)
- Se va bene: **72.963,28 $** (13,69%)
- Se va molto bene: **86.743,11 $** (35,16%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **61.506,14 $** (-4,16%)
- Discesa brutta: **57.224,82 $** (-10,83%)
- Discesa molto brutta: **53.486,58 $** (-16,66%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **75.615,49 $** (17,82%)
- Rialzo buono: **83.220,62 $** (29,67%)
- Rialzo molto forte: **99.117,47 $** (54,44%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Bitcoin tendeva a muoversi tra una zona bassa intorno a **61.506,14 $** e uno spike normale intorno a **75.615,49 $**.

La chiusura a 30 giorni era più spesso positiva: salita 62,50%, discesa 37,50%. Quindi la lettura principale è favorevole.

Nota leva BTC: se la liquidazione è vicina a 51.000 $, guarda soprattutto la discesa brutta e molto brutta. Il prezzo può recuperare dopo, ma la leva può saltare prima.

---

# Solana — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟢 VERDE / Favorevole
**Prezzo attuale:** 75,70 $

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

- Se va molto male: **70,35 $** (-7,07%)
- Se va male: **74,55 $** (-1,52%)
- Scenario normale: **80,95 $** (6,93%)
- Se va bene: **92,71 $** (22,47%)
- Se va molto bene: **126,83 $** (67,54%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **73,57 $** (-2,81%)
- Discesa brutta: **70,65 $** (-6,67%)
- Discesa molto brutta: **67,81 $** (-10,42%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **91,85 $** (21,33%)
- Rialzo buono: **98,69 $** (30,37%)
- Rialzo molto forte: **147,01 $** (94,20%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Solana tendeva a muoversi tra una zona bassa intorno a **73,57 $** e uno spike normale intorno a **91,85 $**.

La chiusura a 30 giorni era più spesso positiva: salita 70,00%, discesa 30,00%. Quindi la lettura principale è favorevole.

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

- Se va molto male: **0,06 $** (-19,10%)
- Se va male: **0,07 $** (-3,74%)
- Scenario normale: **0,08 $** (14,02%)
- Se va bene: **0,09 $** (28,91%)
- Se va molto bene: **0,10 $** (45,15%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **0,06 $** (-8,15%)
- Discesa brutta: **0,06 $** (-12,49%)
- Discesa molto brutta: **0,06 $** (-19,70%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **0,09 $** (24,22%)
- Rialzo buono: **0,10 $** (37,00%)
- Rialzo molto forte: **0,10 $** (50,30%)

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

- Previsioni già controllate: **17**
- Direzione corretta: **70,00%**
- Errore medio dello scenario centrale: **4,96%**
- Zona rischio toccata: **0,00%**
- Zona rialzo media toccata: **0,00%**
- Prezzo finale dentro lo scenario 10%-90%: **100,00%**

### Dogecoin

- Previsioni già controllate: **17**
- Direzione corretta: **100,00%**
- Errore medio dello scenario centrale: **12,11%**
- Zona rischio toccata: **0,00%**
- Zona rialzo media toccata: **0,00%**
- Prezzo finale dentro lo scenario 10%-90%: **100,00%**

### Solana

- Previsioni già controllate: **17**
- Direzione corretta: **100,00%**
- Errore medio dello scenario centrale: **3,68%**
- Zona rischio toccata: **11,76%**
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

Dati ancora insufficienti: previsioni controllate **17** su **30** necessarie.

Per ora si usa solo lo scanner storico grezzo. Quando ci saranno abbastanza previsioni controllate, qui apparirà la lettura autocalibrata.

## Solana

Dati ancora insufficienti: previsioni controllate **17** su **30** necessarie.

Per ora si usa solo lo scanner storico grezzo. Quando ci saranno abbastanza previsioni controllate, qui apparirà la lettura autocalibrata.

## Dogecoin

Dati ancora insufficienti: previsioni controllate **17** su **30** necessarie.

Per ora si usa solo lo scanner storico grezzo. Quando ci saranno abbastanza previsioni controllate, qui apparirà la lettura autocalibrata.

---

# Approfondimento tecnico — Bitcoin (BTC-USD)

## Semaforo: 🟢 VERDE / Favorevole

**Prezzo attuale:** 64.177,53 $

Bitcoin ha un segnale favorevole. La statistica dei casi simili indica più possibilità di salita che di discesa, ma resta comunque una probabilità, non una certezza.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **62,50%**
- Casi negativi dopo 30 giorni: **37,50%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **83,98%**
- Rendimento medio dopo 30 giorni: **11,06%**
- Rendimento centrale dopo 30 giorni: **4,07%**
- Discesa media durante i 30 giorni: **-7,77%**
- Massimo rialzo medio durante i 30 giorni: **28,22%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **71.273,69 $**
- Scenario centrale a 30 giorni: **66.790,72 $**
- Zona di rischio media: **59.191,03 $**
- Zona di rialzo media: **82.290,98 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -14,83% → **54.661,39 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -4,21% → **61.476,14 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: 4,07% → **66.790,72 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 13,69% → **72.963,28 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 35,16% → **86.743,11 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -16,66% → **53.486,58 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -10,83% → **57.224,82 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -4,16% → **61.506,14 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -1,22% → **63.396,88 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: 0,00% → **64.177,53 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 6,41% → **68.291,39 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 8,77% → **69.808,97 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 17,82% → **75.615,49 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 29,67% → **83.220,62 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 54,44% → **99.117,47 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| XRP-USD         | 2026-01-10   | 2026-04-19 |        88.63 |        -2.44 |          -2.44 |           6.41 |
| XLM-USD         | 2020-08-09   | 2020-11-16 |        87.49 |       133.71 |           0    |         152.04 |
| BTC-USD         | 2018-10-26   | 2019-02-02 |        87.32 |         6.83 |          -3.45 |          17.65 |
| LTC-USD         | 2023-07-22   | 2023-10-29 |        86.22 |         1.36 |          -3.41 |           9.26 |
| ONE-USD         | 2020-02-16   | 2020-05-25 |        86.1  |       -22.88 |         -22.88 |           8.51 |
| 1INCH-USD       | 2024-07-11   | 2024-10-18 |        86    |        11.07 |         -15.97 |          17.08 |
| NEO-USD         | 2018-10-29   | 2019-02-05 |        85.69 |        30.74 |          -2.98 |          44    |
| ETH-USD         | 2026-01-10   | 2026-04-19 |        85.6  |        -6.84 |          -6.84 |           4.91 |
| XRP-USD         | 2023-07-25   | 2023-11-01 |        85.58 |         0.55 |          -4.77 |          17.39 |
| APT-USD         | 2023-06-02   | 2023-09-09 |        85.07 |         8.78 |         -12.16 |          20.27 |

---

# Approfondimento tecnico — Solana (SOL-USD)

## Semaforo: 🟢 VERDE / Favorevole

**Prezzo attuale:** 75,70 $

Solana ha un segnale favorevole. La statistica dei casi simili indica più possibilità di salita che di discesa, ma resta comunque una probabilità, non una certezza.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **70,00%**
- Casi negativi dopo 30 giorni: **30,00%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **77,66%**
- Rendimento medio dopo 30 giorni: **21,71%**
- Rendimento centrale dopo 30 giorni: **6,93%**
- Discesa media durante i 30 giorni: **-4,78%**
- Massimo rialzo medio durante i 30 giorni: **35,29%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **92,13 $**
- Scenario centrale a 30 giorni: **80,95 $**
- Zona di rischio media: **72,08 $**
- Zona di rialzo media: **102,41 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -7,07% → **70,35 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -1,52% → **74,55 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: 6,93% → **80,95 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 22,47% → **92,71 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 67,54% → **126,83 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -10,42% → **67,81 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -6,67% → **70,65 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -2,81% → **73,57 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -0,60% → **75,24 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: 0,00% → **75,70 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 6,55% → **80,66 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 9,60% → **82,97 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 21,33% → **91,85 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 30,37% → **98,69 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 94,20% → **147,01 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| ONE-USD         | 2020-02-16   | 2020-05-25 |        83.11 |       -22.88 |         -22.88 |           8.51 |
| ZIL-USD         | 2020-08-11   | 2020-11-18 |        82.35 |       101.63 |          -2.99 |         101.63 |
| EOS-USD         | 2020-02-16   | 2020-05-25 |        81.61 |        -1.75 |          -1.75 |          11.2  |
| BNB-USD         | 2020-02-16   | 2020-05-25 |        81.58 |        -2.28 |          -3.01 |           9.23 |
| EOS-USD         | 2018-11-08   | 2019-02-15 |        80.93 |        34.78 |           0    |          52.35 |
| ENJ-USD         | 2018-10-29   | 2019-02-05 |        80.63 |       269.45 |          -9.43 |         270.52 |
| ALGO-USD        | 2020-02-20   | 2020-05-29 |        80.08 |        -9.13 |         -10.1  |           8.93 |
| MKR-USD         | 2025-07-25   | 2025-11-01 |        79.78 |        -4.43 |         -26.84 |           0.05 |
| MKR-USD         | 2020-02-17   | 2020-05-26 |        79.68 |        36.64 |           0    |         104.38 |
| DASH-USD        | 2020-02-16   | 2020-05-25 |        79.59 |        -1.44 |          -4.98 |           8.64 |

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

- Somiglianza media dei pattern: **85,55%**
- Rendimento medio dopo 30 giorni: **16,11%**
- Rendimento centrale dopo 30 giorni: **14,02%**
- Discesa media durante i 30 giorni: **-10,51%**
- Massimo rialzo medio durante i 30 giorni: **29,20%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **0,08 $**
- Scenario centrale a 30 giorni: **0,08 $**
- Zona di rischio media: **0,06 $**
- Zona di rialzo media: **0,09 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -19,10% → **0,06 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -3,74% → **0,07 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: 14,02% → **0,08 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 28,91% → **0,09 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 45,15% → **0,10 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -19,70% → **0,06 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -12,49% → **0,06 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -8,15% → **0,06 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -4,37% → **0,07 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: -0,44% → **0,07 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 2,84% → **0,07 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 12,87% → **0,08 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 24,22% → **0,09 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 37,00% → **0,10 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 50,30% → **0,10 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| OP-USD          | 2026-01-11   | 2026-04-20 |        89.83 |         3.89 |          -3.44 |          39.02 |
| HBAR-USD        | 2020-08-11   | 2020-11-18 |        89.08 |        16.65 |          -0.47 |          30.28 |
| XTZ-USD         | 2020-08-09   | 2020-11-16 |        87.9  |        13.45 |          -0.15 |          27.99 |
| VET-USD         | 2022-03-29   | 2022-07-06 |        87.84 |        33.03 |          -9.15 |          33.03 |
| DOGE-USD        | 2025-01-10   | 2025-04-19 |        86.96 |        42.64 |          -1.37 |          58.07 |
| SNX-USD         | 2025-10-12   | 2026-01-19 |        86.92 |       -32.4  |         -36.26 |           0    |
| WAVES-USD       | 2022-03-27   | 2022-07-04 |        86.84 |         2.44 |         -14.68 |          13.6  |
| SAND-USD        | 2025-01-09   | 2025-04-18 |        86.82 |        23.74 |           0    |          41.88 |
| ZEC-USD         | 2019-06-21   | 2019-09-28 |        86.53 |        -6.19 |         -18.51 |           0    |
| AVAX-USD        | 2025-09-18   | 2025-12-26 |        86.25 |        -6.95 |          -6.95 |          19.4  |

</details>
<!-- COMPACT_SECTION_END:scanner_full_detail -->

<!-- COMPACT_SECTION_START:market_regime -->
<details>
<summary><strong>🌦️ Market Regime Match</strong></summary>

<!-- MARKET_REGIME_MATCH_START -->
# Market Regime Match Report


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [market_regime_match_report.md](market_regime_match_report.md)

Generated: 2026-08-18 05:32 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | BEAR | 64.178 $ | False | -17.18% | -10.22% | BEAR | -17.18% | -10.22% |
| DOGE-USD | BEAR | 0.06976 $ | False | -32.69% | -16.74% | BEAR | -17.18% | -10.22% |
| SOL-USD | BEAR | 75,70 $ | False | -12.05% | -16.85% | BEAR | -17.18% | -10.22% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 62.50% | 4.07% | 13.69% | 35.16% | -4.16% | -16.66% | 17.82% | 29.67% | 54.44% | 55.00% | 12.51% | 62.82% | 119.58% |
| BTC-USD | SAME_BTC_REGIME | 26 | 53.85% | 3.84% | 12.16% | 32.87% | -4.58% | -14.95% | 17.82% | 27.11% | 47.28% | 46.15% | -9.02% | 70.37% | 131.72% |
| BTC-USD | SAME_ASSET_REGIME | 27 | 55.56% | 4.18% | 12.82% | 32.44% | -5.26% | -15.02% | 17.99% | 26.36% | 46.63% | 51.85% | 13.51% | 69.97% | 128.69% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 24 | 54.17% | 4.07% | 12.67% | 33.72% | -4.58% | -13.02% | 17.82% | 25.61% | 48.59% | 50.00% | 4.65% | 76.24% | 137.80% |
| DOGE-USD | ALL_MATCHES | 40 | 72.50% | 14.02% | 28.91% | 45.15% | -8.15% | -19.70% | 24.22% | 37.00% | 50.30% | 50.00% | -0.16% | 20.49% | 103.09% |
| DOGE-USD | SAME_BTC_REGIME | 15 | 73.33% | 9.84% | 30.77% | 54.72% | -9.97% | -22.57% | 23.01% | 37.08% | 54.72% | 46.67% | -3.21% | 6.32% | 99.73% |
| DOGE-USD | SAME_ASSET_REGIME | 16 | 81.25% | 24.60% | 34.06% | 44.33% | -8.93% | -19.86% | 32.42% | 39.07% | 46.30% | 62.50% | 3.83% | 11.91% | 74.29% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 11 | 72.73% | 9.84% | 26.21% | 34.01% | -9.75% | -26.92% | 23.01% | 34.58% | 39.02% | 45.45% | -3.21% | 4.02% | 7.64% |
| SOL-USD | ALL_MATCHES | 40 | 70.00% | 6.93% | 22.47% | 67.54% | -2.81% | -10.42% | 21.33% | 30.37% | 94.20% | 70.00% | 21.68% | 58.48% | 157.46% |
| SOL-USD | SAME_BTC_REGIME | 13 | 76.92% | 4.18% | 34.36% | 88.13% | -3.35% | -9.29% | 22.14% | 48.60% | 92.04% | 46.15% | -2.78% | 82.67% | 134.53% |
| SOL-USD | SAME_ASSET_REGIME | 11 | 72.73% | 4.18% | 17.98% | 93.69% | -4.48% | -9.63% | 22.14% | 40.50% | 93.69% | 45.45% | -7.07% | 113.56% | 157.07% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 9 | 77.78% | 4.18% | 20.47% | 128.84% | -3.25% | -7.36% | 22.14% | 48.60% | 129.05% | 44.44% | -7.07% | 82.67% | 205.52% |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 26 | 53.85% | 3.84% | -4.58% | 27.11% | 46.15% | -9.02% | 83.99% |
| BTC-USD | HISTORICAL_BTC_BULL | 7 | 100.00% | 8.78% | -3.41% | 33.46% | 85.71% | 13.51% | 85.01% |
| BTC-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 100.00% | 30.61% | -14.39% | 37.23% | 100.00% | 66.62% | 144.58% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 6 | 50.00% | 0.09% | -2.67% | 18.96% | 50.00% | 18.60% | 61.52% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 15 | 73.33% | 9.84% | -9.97% | 37.08% | 46.67% | -3.21% | 49.65% |
| DOGE-USD | HISTORICAL_BTC_BULL | 20 | 75.00% | 15.95% | -5.64% | 39.89% | 55.00% | 2.60% | 55.92% |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 0.00% | -32.40% | -36.26% | 0.00% | 0.00% | -27.09% | 0.00% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 4 | 75.00% | 19.46% | -8.93% | 26.50% | 50.00% | -0.95% | 46.83% |
| SOL-USD | HISTORICAL_BTC_BEAR | 13 | 76.92% | 4.18% | -3.35% | 48.60% | 46.15% | -2.78% | 98.06% |
| SOL-USD | HISTORICAL_BTC_BULL | 5 | 80.00% | 17.17% | -5.52% | 29.69% | 60.00% | 6.51% | 39.06% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 22 | 63.64% | 5.34% | -1.56% | 25.59% | 86.36% | 30.68% | 68.90% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 27 | 55.56% | 4.18% | -5.26% | 26.36% | 51.85% | 13.51% | 108.15% |
| BTC-USD | HISTORICAL_ASSET_BULL | 5 | 100.00% | 8.41% | -3.41% | 30.28% | 80.00% | 11.51% | 102.58% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 50.00% | -14.46% | -17.03% | 27.03% | 0.00% | -24.07% | 28.66% |
| BTC-USD | HISTORICAL_ASSET_MIXED | 1 | 100.00% | 36.64% | 0.00% | 104.38% | 100.00% | 55.18% | 104.38% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 5 | 60.00% | 2.71% | -1.33% | 20.49% | 60.00% | 38.53% | 66.99% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 16 | 81.25% | 24.60% | -8.93% | 39.07% | 62.50% | 3.83% | 56.43% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 11 | 72.73% | 15.25% | -1.37% | 39.10% | 54.55% | 0.57% | 49.97% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 3 | 100.00% | 23.86% | -7.19% | 44.78% | 100.00% | 29.43% | 104.94% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 10 | 50.00% | -1.55% | -13.37% | 18.20% | 10.00% | -19.53% | 20.05% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 11 | 72.73% | 4.18% | -4.48% | 40.50% | 45.45% | -7.07% | 132.65% |
| SOL-USD | HISTORICAL_ASSET_BULL | 4 | 75.00% | 25.76% | -5.86% | 60.14% | 75.00% | 29.28% | 126.19% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 4 | 75.00% | 12.32% | -5.64% | 26.76% | 50.00% | 1.87% | 30.51% |
| SOL-USD | HISTORICAL_ASSET_MIXED | 1 | 100.00% | 36.64% | 0.00% | 104.38% | 100.00% | 55.18% | 104.38% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 20 | 65.00% | 5.34% | -1.56% | 27.31% | 85.00% | 28.91% | 67.63% |

## Top regime-adjusted matches

The table below shows the top matches separately for each target, so BTC does not hide SOL and DOGE.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | XRP-USD | 2026-01-10 | 88.63% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -2.44% | -2.44% | 6.41% | -17.87% | -21.60% | 6.41% |
| BTC-USD | BTC-USD | 2018-10-26 | 87.32% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 6.83% | -3.45% | 17.65% | 41.24% | -3.45% | 41.24% |
| BTC-USD | 1INCH-USD | 2024-07-11 | 86.00% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 11.07% | -15.97% | 17.08% | 73.31% | -15.97% | 124.84% |
| BTC-USD | NEO-USD | 2018-10-29 | 85.69% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 30.74% | -2.98% | 44.00% | 85.04% | -2.98% | 91.46% |
| BTC-USD | ETH-USD | 2026-01-10 | 85.60% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -6.84% | -6.84% | 4.91% | -24.52% | -30.74% | 4.91% |
| BTC-USD | THETA-USD | 2022-04-15 | 84.35% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -6.36% | -10.88% | 27.86% | -20.52% | -20.52% | 27.86% |
| BTC-USD | SOL-USD | 2026-01-08 | 84.12% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -4.16% | -6.58% | 9.54% | -17.40% | -30.02% | 9.54% |
| BTC-USD | LTC-USD | 2018-10-26 | 84.05% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 35.00% | -4.25% | 50.56% | 146.90% | -4.25% | 146.90% |
| BTC-USD | QTUM-USD | 2026-01-10 | 84.04% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -0.32% | -2.69% | 17.99% | -18.21% | -22.94% | 17.99% |
| BTC-USD | ETC-USD | 2018-10-24 | 84.01% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 8.28% | -4.92% | 22.50% | 22.00% | -4.92% | 23.79% |
| DOGE-USD | OP-USD | 2026-01-11 | 89.83% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 3.89% | -3.44% | 39.02% | -16.51% | -26.63% | 39.02% |
| DOGE-USD | THETA-USD | 2022-03-31 | 85.91% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 34.01% | -12.38% | 34.01% | -13.72% | -13.72% | 34.01% |
| DOGE-USD | ADA-USD | 2022-03-27 | 85.78% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 6.67% | -11.01% | 11.91% | -3.21% | -11.01% | 21.44% |
| DOGE-USD | NEO-USD | 2022-03-27 | 85.39% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 24.88% | -6.07% | 31.81% | 4.99% | -6.07% | 39.85% |
| DOGE-USD | XTZ-USD | 2026-01-10 | 85.21% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -5.85% | -5.85% | 13.19% | -34.77% | -35.82% | 13.19% |
| DOGE-USD | ETH-USD | 2018-07-21 | 85.18% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -46.43% | -47.25% | 6.37% | -43.24% | -58.95% | 6.37% |
| DOGE-USD | LTC-USD | 2018-04-29 | 85.08% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -20.91% | -26.92% | 0.00% | -20.47% | -30.09% | 0.00% |
| DOGE-USD | CHZ-USD | 2022-03-31 | 85.02% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 49.44% | -3.88% | 49.44% | 83.06% | -3.88% | 146.71% |
| DOGE-USD | DASH-USD | 2022-03-27 | 84.60% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 9.84% | -9.75% | 18.21% | 3.04% | -9.75% | 28.47% |
| DOGE-USD | LINK-USD | 2022-03-27 | 84.52% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 13.28% | -7.21% | 23.01% | 7.64% | -7.21% | 45.11% |
| SOL-USD | ENJ-USD | 2018-10-29 | 80.63% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 269.45% | -9.43% | 270.52% | 449.81% | -9.43% | 676.95% |
| SOL-USD | NEAR-USD | 2026-01-10 | 78.27% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 20.47% | -4.92% | 22.14% | 68.39% | -4.92% | 112.24% |
| SOL-USD | SOL-USD | 2026-01-13 | 77.84% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -3.00% | -4.48% | 12.01% | -16.68% | -28.45% | 12.01% |
| SOL-USD | LINK-USD | 2026-01-10 | 76.86% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 4.18% | 0.00% | 18.10% | -11.79% | -18.96% | 18.10% |
| SOL-USD | RUNE-USD | 2026-01-11 | 76.19% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 2.83% | 0.00% | 48.60% | -7.07% | -24.29% | 48.60% |
| SOL-USD | QTUM-USD | 2018-10-29 | 75.94% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 15.48% | -3.25% | 32.41% | 82.67% | -3.25% | 86.97% |
| SOL-USD | BTC-USD | 2026-01-12 | 75.17% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 1.55% | -0.76% | 7.58% | -15.86% | -20.28% | 7.58% |
| SOL-USD | ETH-USD | 2026-01-10 | 75.04% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -6.84% | -6.84% | 4.91% | -24.52% | -30.74% | 4.91% |
| SOL-USD | BNB-USD | 2018-10-29 | 74.57% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 93.69% | -1.14% | 93.69% | 144.45% | -1.14% | 153.07% |
| SOL-USD | BNB-USD | 2026-01-15 | 79.13% | BEAR | DISTRIBUTION | SAME_BTC_ONLY | MIXED | 3.09% | -3.35% | 6.53% | -9.24% | -10.10% | 12.81% |

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

Generato: 2026-08-18 05:32 UTC


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
| BTC | 64.178 $ | -1 | NEUTRALE / MISTO | STAGE 4 / MARKDOWN | MASSIMI E MINIMI CRESCENTI | ACCUMULO POSSIBILE / RANGE BASSO | BASSO | RIDUCI RISCHIO / NO LONG A LEVA |
| SOL | 75,70 $ | -2 | DEBOLE / NON CONFERMATO | STAGE 4 / MARKDOWN | VOLATILITÀ IN ESPANSIONE | ACCUMULO POSSIBILE / RANGE BASSO | BASSO | NON INSEGUIRE / TAKE PROFIT SU SPIKE |
| DOGE | 0.06976 $ | -5 | RIBASSISTA / FRAGILE | STAGE 4 / MARKDOWN | MASSIMI E MINIMI CRESCENTI | MARKDOWN / DEBOLEZZA | BASSO | NO LONG / SHORT SOLO DOPO SPIKE E REJECTION |

## Punteggi per area

| Asset | Trend | Struttura | Momentum | Volume | Prezzo | Candela | Wyckoff | Totale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | -3 | +2 | +2 | -2 | 0 | 0 | 0 | -1 |
| SOL | -4 | 0 | +1 | +1 | 0 | 0 | 0 | -2 |
| DOGE | -4 | +2 | 0 | -1 | 0 | 0 | -2 | -5 |

## Livelli tecnici

| Asset | Supporto | Resistenza | Breakout 60g | Breakdown 60g | ATR14 | Rendimento 30g | Rendimento 90g |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 62.488 $ | 64.186 $ | 67.248 $ | 57.748 $ | 1,58% | -0,99% | -16,42% |
| SOL | 74,16 $ | 75,94 $ | 83,81 $ | 64,42 $ | 2,14% | 0,28% | -10,14% |
| DOGE | 0.06961 $ | 0.07117 $ | 0.09075 $ | 0.06797 $ | 2,11% | -3,79% | -32,26% |

## Lettura dettagliata

### BTC

- Prezzo: **64.178 $**
- Score classico: **-1 / 12**
- Verdetto: **NEUTRALE / MISTO**
- Azione coerente: **RIDUCI RISCHIO / NO LONG A LEVA**
- Volatilità tecnica locale: **BASSO** — ATR14 1,58%; distanza supporto 2,66%; distanza resistenza 0,05%

Dettaglio:

- Trend: **-3** — prezzo sotto MA200 daily; breve termine sopra MA20/MA50; MA200 daily in discesa; STAGE 4 / MARKDOWN
- Stage weekly: **STAGE 4 / MARKDOWN** — Prezzo sotto MA30 weekly con MA30 in discesa.
- Struttura: **+2** — MASSIMI E MINIMI CRESCENTI
- Momentum: **+2** — RSI sano 52.3; RSI in miglioramento; MACD sotto signal; istogramma MACD in miglioramento
- Volume: **-2** — OBV sotto media; CMF negativo -0.10; volume ratio 1.06
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **0** — ACCUMULO POSSIBILE / RANGE BASSO. Prezzo nella metà bassa del range, ma senza spring confermato.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 52.32 |
| MACD histogram | -78.96053 |
| CMF20 | -0.104 |
| Volume ratio 20 | 1.06 |
| MA20 | 63.797 $ |
| MA50 | 63.661 $ |
| MA100 | 66.532 $ |
| MA200 | 69.137 $ |
| Pendenza MA50 20g | +0,59% |
| Pendenza MA200 60g | -10,36% |
| Bollinger width | 4,59% |
| Bollinger position | 0.62 |

### SOL

- Prezzo: **75,70 $**
- Score classico: **-2 / 12**
- Verdetto: **DEBOLE / NON CONFERMATO**
- Azione coerente: **NON INSEGUIRE / TAKE PROFIT SU SPIKE**
- Volatilità tecnica locale: **BASSO** — ATR14 2,14%; distanza supporto 2,03%; distanza resistenza 0,36%

Dettaglio:

- Trend: **-4** — prezzo sotto MA200 daily; MA200 daily in discesa; STAGE 4 / MARKDOWN
- Stage weekly: **STAGE 4 / MARKDOWN** — Prezzo sotto MA30 weekly con MA30 in discesa.
- Struttura: **0** — VOLATILITÀ IN ESPANSIONE
- Momentum: **+1** — RSI sano 52.5; MACD sopra signal; istogramma MACD in peggioramento
- Volume: **+1** — OBV sopra media; CMF neutrale 0.00; volume ratio 1.04
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **0** — ACCUMULO POSSIBILE / RANGE BASSO. Prezzo nella metà bassa del range, ma senza spring confermato.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 52.48 |
| MACD histogram | 0.13379 |
| CMF20 | 0.000 |
| Volume ratio 20 | 1.04 |
| MA20 | 74,52 $ |
| MA50 | 76,14 $ |
| MA100 | 76,68 $ |
| MA200 | 81,57 $ |
| Pendenza MA50 20g | +2,52% |
| Pendenza MA200 60g | -17,09% |
| Bollinger width | 7,15% |
| Bollinger position | 0.71 |

### DOGE

- Prezzo: **0.06976 $**
- Score classico: **-5 / 12**
- Verdetto: **RIBASSISTA / FRAGILE**
- Azione coerente: **NO LONG / SHORT SOLO DOPO SPIKE E REJECTION**
- Volatilità tecnica locale: **BASSO** — ATR14 2,11%; distanza supporto 0,16%; distanza resistenza 2,08%

Dettaglio:

- Trend: **-4** — prezzo sotto MA200 daily; medie daily allineate ribassiste; MA50 daily in discesa; MA200 daily in discesa; STAGE 4 / MARKDOWN
- Stage weekly: **STAGE 4 / MARKDOWN** — Prezzo sotto MA30 weekly con MA30 in discesa.
- Struttura: **+2** — MASSIMI E MINIMI CRESCENTI
- Momentum: **0** — RSI neutrale 45.3; MACD sopra signal; istogramma MACD in peggioramento
- Volume: **-1** — OBV sotto media; CMF neutrale -0.05; volume ratio 0.75
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **-2** — MARKDOWN / DEBOLEZZA. Prezzo basso nel range e sotto medie principali.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 45.31 |
| MACD histogram | 0.00018 |
| CMF20 | -0.049 |
| Volume ratio 20 | 0.75 |
| MA20 | 0.06991 $ |
| MA50 | 0.07183 $ |
| MA100 | 0.08266 $ |
| MA200 | 0.08993 $ |
| Pendenza MA50 20g | -6,43% |
| Pendenza MA200 60g | -16,94% |
| Bollinger width | 3,67% |
| Bollinger position | 0.42 |

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

Generato: 2026-08-18 05:32 UTC


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
| BTC | 64.178 $ | Doppio massimo | CANDIDATO | ribassista | n/a | 49.952 $ | n/a | 11,13% | Fib 23,6% TESTATO (0) @ 63.595 $ | NEL RANGE | 62.553 $ |
| SOL | 75,70 $ | Doppio massimo | CANDIDATO | ribassista | n/a | 51,22 $ | n/a | 17,51% | Fib 23,6% TENUTO (0) @ 73,56 $ | NEL RANGE | 73,40 $ |
| DOGE | 0.06976 $ | Doppio minimo | CANDIDATO | rialzista | n/a | 0.07931 $ | n/a | 5,80% | Fib 23,6% NON ATTIVO (0) @ 0.08059 $ | NEL RANGE | 0.06961 $ |

## BTC

![Classic visual BTC](classic_visual_BTC.png)

- Pattern principale: **Doppio massimo**
- Stato pattern: **CANDIDATO** (0)
- Famiglia: **ribassista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-06-22 -> 2026-08-09**
- Età formazione: **9 giorni**
- Breakout pattern: **n/a**
- Età breakout: **n/a**
- Neckline: **57.748 $**
- Target teorico: **49.952 $**
- Progresso verso target: **n/a**
- Distanza dalla neckline: **11,13%**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 23,6% TESTATO (0) @ 63.595 $** — Swing UP 2026-07-01 57.748 -> 2026-08-09 65.402; livello più vicino 23.6% a 63.595; stato TESTATO; confluenza: nessuna confluenza indipendente.
- Invalidazione: **58.903 $**
- Relazione prezzo/neckline: **sopra neckline**
- Dettaglio: Due massimi simili vicino a 65.544 tra 2026-06-22 e 2026-08-09. Neckline ribassista stimata: 57.748. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 9 giorni. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **NEL RANGE**
- Supporto: **62.553 $**
- Resistenza: **65.402 $**
- Breakout 60g: **67.248 $**
- Breakdown 60g: **57.748 $**
- RSI14: **52.48**
- ATR14: **1,58%**
- Volume ratio 20g: **1.06**
- Rendimento 30g: **-0,96%**
- Rendimento 90g: **-16,38%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Doppio massimo | CANDIDATO | 0 | ribassista | 62.227 $ | n/a | n/a | 58.946 $ | n/a | 3,14% | 63.471 $ | Due massimi simili a 65.508 $ e 65.402 $. Neckline circa 62.227 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 9 giorni. |
| Doppio minimo | CANDIDATO | 0 | rialzista | 66.910 $ | n/a | n/a | 71.619 $ | n/a | 4,26% | 65.572 $ | Due minimi simili a 62.201 $ e 62.227 $. Neckline circa 66.910 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 15 giorni. |

## SOL

![Classic visual SOL](classic_visual_SOL.png)

- Pattern principale: **Doppio massimo**
- Stato pattern: **CANDIDATO** (0)
- Famiglia: **ribassista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-06-22 -> 2026-08-09**
- Età formazione: **9 giorni**
- Breakout pattern: **n/a**
- Età breakout: **n/a**
- Neckline: **64,42 $**
- Target teorico: **51,22 $**
- Progresso verso target: **n/a**
- Distanza dalla neckline: **17,51%**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 23,6% TENUTO (0) @ 73,56 $** — Swing UP 2026-06-06 60,41 -> 2026-08-09 77,62; livello più vicino 23.6% a 73,56; stato TENUTO; confluenza: nessuna confluenza indipendente.
- Invalidazione: **65,71 $**
- Relazione prezzo/neckline: **sopra neckline**
- Dettaglio: Due massimi simili vicino a 77,62 tra 2026-06-22 e 2026-08-09. Neckline ribassista stimata: 64,42. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 9 giorni. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **NEL RANGE**
- Supporto: **73,40 $**
- Resistenza: **75,94 $**
- Breakout 60g: **83,81 $**
- Breakdown 60g: **64,42 $**
- RSI14: **52.59**
- ATR14: **2,14%**
- Volume ratio 20g: **1.04**
- Rendimento 30g: **+0,32%**
- Rendimento 90g: **-10,10%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Doppio massimo | CANDIDATO | 0 | ribassista | 70,69 $ | n/a | n/a | 62,66 $ | n/a | 7,08% | 72,11 $ | Due massimi simili a 78,73 $ e 77,62 $. Neckline circa 70,69 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 9 giorni. |
| Triangolo discendente possibile | CANDIDATO | 0 | ribassista | n/a | n/a | n/a | n/a | n/a | n/a | n/a | Massimi decrescenti e supporto quasi piatto. Stato: CANDIDATO; il pattern non ha una neckline univoca da usare per il lifecycle. |
| Doppio minimo | CANDIDATO | 0 | rialzista | 78,73 $ | n/a | n/a | 86,76 $ | n/a | 4,00% | 77,15 $ | Due minimi simili a 73,40 $ e 70,69 $. Neckline circa 78,73 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 17 giorni. |
| Testa e spalle inverso | CANDIDATO | 0 | rialzista | 79,35 $ | n/a | n/a | 94,28 $ | n/a | 4,82% | 77,76 $ | Spalla sinistra 67,92 $, testa 64,42 $, spalla destra 73,40 $. Neckline circa 79,35 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 32 giorni. |

## DOGE

![Classic visual DOGE](classic_visual_DOGE.png)

- Pattern principale: **Doppio minimo**
- Stato pattern: **CANDIDATO** (0)
- Famiglia: **rialzista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-07-24 -> 2026-08-12**
- Età formazione: **6 giorni**
- Breakout pattern: **n/a**
- Età breakout: **n/a**
- Neckline: **0.07380 $**
- Target teorico: **0.07931 $**
- Progresso verso target: **n/a**
- Distanza dalla neckline: **5,80%**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 23,6% NON ATTIVO (0) @ 0.08059 $** — Swing DOWN 2026-05-14 0.11825 -> 2026-08-12 0.06895; livello più vicino 23.6% a 0.08059; stato NON ATTIVO; confluenza: nessuna confluenza indipendente.
- Invalidazione: **0.07233 $**
- Relazione prezzo/neckline: **sotto neckline**
- Dettaglio: Due minimi simili vicino a 0.06829 tra 2026-07-24 e 2026-08-12. Neckline stimata: 0.07380. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 6 giorni. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **NEL RANGE**
- Supporto: **0.06961 $**
- Resistenza: **0.07117 $**
- Breakout 60g: **0.09075 $**
- Breakdown 60g: **0.06797 $**
- RSI14: **45.50**
- ATR14: **2,11%**
- Volume ratio 20g: **0.75**
- Rendimento 30g: **-3,74%**
- Rendimento 90g: **-32,22%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Doppio minimo | CANDIDATO | 0 | rialzista | 0.07923 $ | n/a | n/a | 0.08952 $ | n/a | 13,58% | 0.07765 $ | Due minimi simili a 0.06961 $ e 0.06895 $. Neckline circa 0.07923 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 6 giorni. |
| Triangolo ascendente possibile | CANDIDATO | 0 | rialzista | n/a | n/a | n/a | n/a | n/a | n/a | n/a | Resistenza quasi piatta e minimi crescenti. Stato: CANDIDATO; il pattern non ha una neckline univoca da usare per il lifecycle. |
| Doppio massimo | CANDIDATO | 0 | ribassista | 0.06797 $ | n/a | n/a | 0.06214 $ | n/a | 2,63% | 0.06933 $ | Due massimi simili a 0.07380 $ e 0.07286 $. Neckline circa 0.06797 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 7 giorni. |

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

Generato: 2026-08-18 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [fractal_path_tracker.md](fractal_path_tracker.md)

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-08-18**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-02-02**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **75,70 $**
- Verdetto principale: **ANALOGIA DEBOLE / SCENARIO SECONDARIO**
- Somiglianza strutturale: **+57,65%**
- Aderenza live principale: **+68,74%**
- Errore medio live principale: **15,63%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE SOLO DI CONTESTO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **73**
- Osservazioni inclusive dal bottom: **74**
- Osservazioni da inizio programma/scanner: **47**
- Errore assoluto medio dal bottom: **12,12%**
- Errore assoluto medio da inizio programma: **15,63%**
- Gap firmato medio ultimi 7 giorni: **-17,92%**
- Errore assoluto medio ultimi 7 giorni: **17,92%**
- Gap ultimo giorno: **-18,13%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **-18,13%**
- Gap firmato medio 7g: **-17,92%**
- Errore assoluto medio 7g: **17,92%**
- Variazione recente gap: **-1,79%**
- Stato gap: **DISALLINEATO SOTTO IL FRATTALE**
- Trend gap: **SOL si sta allontanando sotto il percorso ancorato**

Soglie operative del grafico:

- entro **±5%**: percorso vicino;
- tra **±5% e ±12%**: deviazione gestibile;
- oltre **±12%**: frattale non abbastanza aderente per conferma operativa;
- oltre **±18%**: disallineamento marcato.

## Ultimi giorni del confronto ancorato

|   Giorno | Data SOL   | Data BTC eq.   | SOL reale   | Percorso ancorato   | Gap firmato   | Fase                |
|---------:|:-----------|:---------------|:------------|:--------------------|:--------------|:--------------------|
| 64 | 2026-08-09 | 2023-01-24 | 76,21 $ | 89,17 $ | -14,53% | da inizio programma |
| 65 | 2026-08-10 | 2023-01-25 | 75,95 $ | 91,07 $ | -16,60% | da inizio programma |
| 66 | 2026-08-11 | 2023-01-26 | 76,20 $ | 90,73 $ | -16,02% | da inizio programma |
| 67 | 2026-08-12 | 2023-01-27 | 75,53 $ | 90,91 $ | -16,93% | da inizio programma |
| 68 | 2026-08-13 | 2023-01-28 | 76,18 $ | 90,72 $ | -16,03% | da inizio programma |
| 69 | 2026-08-14 | 2023-01-29 | 75,33 $ | 93,65 $ | -19,57% | da inizio programma |
| 70 | 2026-08-15 | 2023-01-30 | 75,27 $ | 89,97 $ | -16,34% | da inizio programma |
| 71 | 2026-08-16 | 2023-01-31 | 74,54 $ | 91,15 $ | -18,22% | da inizio programma |
| 72 | 2026-08-17 | 2023-02-01 | 74,54 $ | 93,45 $ | -20,24% | da inizio programma |
| 73 | 2026-08-18 | 2023-02-02 | 75,70 $ | 92,46 $ | -18,13% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-08-25 | 85,95 $ | 70,37 $ | 70,37 $ / 75,70 $ | no | n/a | n/a | n/a |
| 14g | 2026-09-01 | 93,06 $ | 76,19 $ | 69,83 $ / 78,40 $ | no | n/a | n/a | n/a |
| 21g | 2026-09-08 | 94,33 $ | 77,23 $ | 69,83 $ / 80,08 $ | no | n/a | n/a | n/a |
| 28g | 2026-09-15 | 92,48 $ | 75,71 $ | 69,83 $ / 80,08 $ | no | n/a | n/a | n/a |
| 35g | 2026-09-22 | 80,21 $ | 65,67 $ | 65,67 $ / 80,08 $ | no | n/a | n/a | n/a |
| 42g | 2026-09-29 | 98,69 $ | 80,80 $ | 65,11 $ / 80,80 $ | no | n/a | n/a | n/a |
| 49g | 2026-10-06 | 111,61 $ | 91,38 $ | 65,11 $ / 91,38 $ | no | n/a | n/a | n/a |
| 56g | 2026-10-13 | 110,43 $ | 90,41 $ | 65,11 $ / 91,43 $ | no | n/a | n/a | n/a |
| 63g | 2026-10-20 | 110,47 $ | 90,45 $ | 65,11 $ / 91,85 $ | no | n/a | n/a | n/a |
| 70g | 2026-10-27 | 119,75 $ | 98,04 $ | 65,11 $ / 98,04 $ | no | n/a | n/a | n/a |
| 77g | 2026-11-03 | 111,27 $ | 91,10 $ | 65,11 $ / 98,32 $ | no | n/a | n/a | n/a |
| 84g | 2026-11-10 | 116,10 $ | 95,06 $ | 65,11 $ / 98,32 $ | no | n/a | n/a | n/a |
| 91g | 2026-11-17 | 113,64 $ | 93,04 $ | 65,11 $ / 98,32 $ | no | n/a | n/a | n/a |
| 98g | 2026-11-24 | 106,36 $ | 87,08 $ | 65,11 $ / 98,32 $ | no | n/a | n/a | n/a |
| 105g | 2026-12-01 | 105,70 $ | 86,54 $ | 65,11 $ / 98,32 $ | no | n/a | n/a | n/a |
| 112g | 2026-12-08 | 104,30 $ | 85,39 $ | 65,11 $ / 98,32 $ | no | n/a | n/a | n/a |
| 119g | 2026-12-15 | 105,65 $ | 86,50 $ | 65,11 $ / 98,32 $ | no | n/a | n/a | n/a |
| 126g | 2026-12-22 | 104,42 $ | 85,49 $ | 65,11 $ / 98,32 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 35 | 42,86% | 6,96% | 14,07% |
| 14g | 28 | 39,29% | 15,50% | 13,61% |
| 21g | 21 | 23,81% | 25,77% | 15,84% |
| 28g | 14 | 28,57% | 29,08% | 17,19% |
| 35g | 7 | 0,00% | 29,67% | 18,50% |
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

Ultima lettura salvata: **2026-08-18** — SOL 75,70 $, gap -18,13%, somiglianza +57,65%.

Nel report principale lascio solo il link, così non diventa troppo lungo.

<!-- SOL_BTC_FRACTAL_HISTORY_END -->

</details>
<!-- COMPACT_SECTION_END:fractal_path -->

<!-- COMPACT_SECTION_START:exchange_microstructure -->
<details>
<summary><strong>🏦 Dati exchange, liquidità e leva</strong></summary>

<!-- EXCHANGE_MICROSTRUCTURE_START -->
# Dati exchange, liquidità e leva

Generato: 2026-08-18 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [exchange_microstructure_report.md](exchange_microstructure_report.md)

Questo modulo legge Kraken Futures, Bitget Futures e KuCoin Futures come nucleo derivati. OKX e Coinbase vengono raccolti come fonti ausiliarie non pesate.
Non modifica la formula matematica di RSI, Fibonacci o Wyckoff: controlla se quei segnali sono sostenuti da acquisti, vendite, OI, funding e liquidità.

**Limite importante:** questo nucleo non assume disponibile un feed pubblico completo delle liquidazioni. La componente liquidazioni resta neutrale; le zone future restano stime di pressione, non dati certi delle singole posizioni.

Diagnostica completa: [exchange_source_diagnostics.md](exchange_source_diagnostics.md)

## Sintesi

| Asset | Prezzo | Exchange | Segnale candidato | Peso Global | Bias exchange | Confidenza | Copertura | Funding 8h eq. | OI 24h | Taker flow (campione/4h) | Book 0,5% | Liq long campione | Liq short campione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 64.192 $ | 3 | 0 | 0 | LEGGERMENTE POSITIVA / NON PESATA | MEDIA | 100% | -0,0022% | +0,58% | 4,56 | +0,21% | 0 $ | 0 $ |
| SOL | 75,81 $ | 3 | 0 | 0 | LEGGERMENTE POSITIVA / NON PESATA | MEDIA | 100% | +0,0026% | -3,72% | 2,04 | -7,27% | 0 $ | 0 $ |
| DOGE | 0.06989 $ | 3 | 0 | 0 | LEGGERMENTE POSITIVA / NON PESATA | MEDIA | 100% | +0,0096% | -1,38% | 1,51 | -3,78% | 0 $ | 0 $ |

Il segnale candidato è limitato a **±1**, ma il peso nel Global resta **0** finché il tracker a 7 giorni non raggiunge 30 controlli, almeno 55% di accuratezza e return corretto direzione positivo. Un singolo muro o funding non basta.

La colonna taker usa un campione recente nel primo run. Dopo almeno 3 fotografie distribuite su almeno 45 minuti viene sostituita automaticamente dalla media intraday 4h.

## Dati separati per exchange

| Asset | Exchange | Stato | Funding 8h eq. | Open interest | Taker flow | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | Kraken | OK | +0,0005% | 157,44 mln $ | 0,19 | -2,87% |
| BTC | Bitget | OK | +0,0062% | 2,54 mld $ | 3,30 | +3,78% |
| BTC | Kucoin | OK | +0,0000% | 1,53 mld $ | 11,63 | -2,20% |
| SOL | Kraken | OK | -0,0053% | 20,02 mln $ | 1,99 | -1,44% |
| SOL | Bitget | OK | +0,0100% | 356,34 mln $ | 0,38 | +0,83% |
| SOL | Kucoin | OK | +0,0049% | 226,43 mln $ | 2,98 | -10,14% |
| DOGE | Kraken | OK | -0,0150% | 3,95 mln $ | 3,59 | -8,39% |
| DOGE | Bitget | OK | +0,0084% | 92,55 mln $ | 8,27 | -4,17% |
| DOGE | Kucoin | OK | +0,0097% | 116,25 mln $ | 2,38 | -9,64% |

Kraken, Bitget e KuCoin contribuiscono a funding normalizzato, open interest, trade aggressivi e order book. Non viene inventato un long/short ratio pubblico né un feed completo delle liquidazioni.

## Conferme per indicatori tecnici

### BTC

- Score grezzo exchange: **+2,38**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 1, accuratezza +100,00%.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 1, bear 0, divergenze 0.
- Flusso taker/order book: **+1,75**.
- OI/funding/basis: **+0,00**.
- Affollamento long/short: **+0,00**.
- Liquidazioni: **NON PESATE / FEED COMPLETO NON ASSUNTO DISPONIBILE**.
- **Wyckoff:** Possibile accumulazione/spring sostenuto da pressione compratrice o assorbimento.
- **Fibonacci:** Livello Fibonacci soltanto testato: order book e taker flow non bastano ancora per dichiararlo tenuto o perso.
- **RSI:** RSI in zona non estrema o flusso exchange non abbastanza netto.
- **Pattern:** I pattern candidati restano non operativi: i dati exchange possono solo preparare la conferma.
- **Breakout/breakdown:** Resistenza vicina con acquisti aggressivi: breakout più credibile, ma serve chiusura sopra il livello.
- **Mappa liquidità attuale:** muro bid: n/a; muro ask: n/a

![Microstruttura exchange BTC](exchange_microstructure_BTC.png)

### SOL

- Score grezzo exchange: **+2,25**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 2, accuratezza +0,00%.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 1, bear 0, divergenze 0.
- Flusso taker/order book: **+1,75**.
- OI/funding/basis: **+0,00**.
- Affollamento long/short: **+0,00**.
- Liquidazioni: **NON PESATE / FEED COMPLETO NON ASSUNTO DISPONIBILE**.
- **Wyckoff:** Markdown non pienamente confermato: compare assorbimento compratore.
- **Fibonacci:** Fibonacci tenuto con acquisti/assorbimento coerenti: conferma positiva.
- **RSI:** RSI in zona non estrema o flusso exchange non abbastanza netto.
- **Pattern:** I pattern candidati restano non operativi: i dati exchange possono solo preparare la conferma.
- **Breakout/breakdown:** Prezzo non abbastanza vicino a un livello chiave o flusso non netto.
- **Mappa liquidità attuale:** muro bid: n/a; muro ask: n/a

![Microstruttura exchange SOL](exchange_microstructure_SOL.png)

### DOGE

- Score grezzo exchange: **+2,38**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 4, accuratezza +50,00%.
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
- **Breakout/breakdown:** Supporto vicino con assorbimento/acquisti: tenuta più credibile.
- **Mappa liquidità attuale:** muro bid: n/a; muro ask: n/a

![Microstruttura exchange DOGE](exchange_microstructure_DOGE.png)

## Overlay sulle previsioni a 30 giorni

La previsione storica grezza dello scanner resta intatta. L'overlay exchange può correggerla solo dopo almeno 30 controlli maturati a 30 giorni e solo se il modulo dimostra accuratezza direzionale almeno del 55%.

| Asset | Prob. grezza salita | Return p50 grezzo | Controlli 30g | Accuratezza exchange | Stato overlay | Peso | Prob. corretta | Return corretto |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +62,50% | +4,07% | 0 | n/a | RACCOLTA DATI | 0,00 | +62,50% | +4,07% |
| SOL | +70,00% | +6,93% | 0 | n/a | RACCOLTA DATI | 0,00 | +70,00% | +6,93% |
| DOGE | +72,50% | +14,02% | 0 | n/a | RACCOLTA DATI | 0,00 | +72,50% | +14,02% |

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

Generato: 2026-08-18 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [exchange_signal_tracker_report.md](exchange_signal_tracker_report.md)

Questo tracker verifica se il segnale candidato exchange ±1 anticipa correttamente la direzione del prezzo a 1/3/7/14/30 giorni.
Il peso Global resta 0 finché l'orizzonte 7g non ha almeno 30 controlli, accuratezza almeno 55% e return corretto direzione positivo. L'overlay a 30g ha un gate separato.

Controlli maturati completati in questa esecuzione: **15**.

## Ultime fotografie giornaliere

| Data | Asset | Prezzo | Versione | Calibrazione | Candidato | Peso Global | Score raw | Confidenza | Taker 4h | OI 24h | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08-18 | BTC | 64.191,70 | V2.1.3 | OK | 0 | 0 | 2,38 | MEDIA | 4,56 | +0,58% | +0,21% |
| 2026-08-18 | DOGE | 0.06989 | V2.1.3 | OK | 0 | 0 | 2,38 | MEDIA | 1,51 | -1,38% | -3,78% |
| 2026-08-18 | SOL | 75,81 | V2.1.3 | OK | 0 | 0 | 2,25 | MEDIA | 2,04 | -3,72% | -7,27% |
| 2026-08-17 | BTC | 63.443,80 | V2.1.3 | OK | 0 | 0 | 2,38 | MEDIA | 1,11 | -0,53% | -3,55% |
| 2026-08-17 | DOGE | 0.07017 | V2.1.3 | OK | 0 | 0 | 2,38 | MEDIA | 2,45 | +2,30% | -4,25% |
| 2026-08-17 | SOL | 75,44 | V2.1.3 | OK | 0 | 0 | 2,00 | BASSA | 1,31 | -4,07% | +1,92% |
| 2026-08-16 | BTC | 63.060,70 | V2.1.3 | OK | 0 | 0 | 0,25 | BASSA | 1,64 | +0,59% | -3,23% |
| 2026-08-16 | DOGE | 0.06977 | V2.1.3 | OK | 0 | 0 | 2,12 | MEDIA | 2,19 | -4,27% | -0,62% |
| 2026-08-16 | SOL | 75,43 | V2.1.3 | OK | 0 | 0 | 2,00 | BASSA | 1,83 | +1,84% | -2,70% |

## Accuratezza direzionale

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 1 | +100,00% | +1,59% | +1,07% | +1,84% | FEEDBACK RAPIDO |
| BTC | 3g | 1 | +100,00% | +1,47% | -1,13% | +3,82% | FEEDBACK RAPIDO |
| BTC | 7g | 1 | +100,00% | +1,35% | -1,18% | +3,82% | FEEDBACK RAPIDO |
| BTC | 14g | 1 | +0,00% | -2,63% | -3,44% | +3,82% | FEEDBACK RAPIDO |
| BTC | 30g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 1g | 2 | +50,00% | +0,20% | -0,04% | +0,81% | FEEDBACK RAPIDO |
| SOL | 3g | 2 | +0,00% | -1,86% | -2,68% | +1,44% | FEEDBACK RAPIDO |
| SOL | 7g | 2 | +0,00% | -3,56% | -4,18% | +1,44% | FEEDBACK RAPIDO |
| SOL | 14g | 1 | +0,00% | -5,72% | -9,55% | +0,73% | FEEDBACK RAPIDO |
| SOL | 30g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 1g | 4 | +50,00% | +1,05% | +0,76% | +2,03% | FEEDBACK RAPIDO |
| DOGE | 3g | 4 | +50,00% | +1,09% | -0,86% | +4,99% | FEEDBACK RAPIDO |
| DOGE | 7g | 4 | +50,00% | +0,28% | -0,90% | +5,64% | FEEDBACK RAPIDO |
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

**BTC** — BTC: i futures non danno una lettura chiara. Non si vede uno sbilanciamento forte né long né short. Qui pesa di più il report frattale.

**SOL** — SOL: i futures non danno una lettura chiara. Non si vede uno sbilanciamento forte né long né short. Qui pesa di più il report frattale.

**DOGE** — DOGE: i futures non danno una lettura chiara. Non si vede uno sbilanciamento forte né long né short. Qui pesa di più il report frattale.

| Asset | Prezzo | Funding | OI 24h | Long/Short | Lettura futures | Forza |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 64.178 $ | +0.0038% | -3.90% | 1.38 | Misto | 1/5 |
| SOL | 75,70 $ | +0.0039% | -0.51% | 2.77 | Misto | 1/5 |
| DOGE | 0.06976 $ | +0.0009% | -12.18% | 4.85 | Misto | 1/5 |

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

Generato: 2026-08-18 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [rsi_multitimeframe_divergence_report.md](rsi_multitimeframe_divergence_report.md)

Il modulo confronta prezzo e RSI 14 sui pivot confermati **daily e weekly**. Riconosce divergenze regolari e nascoste, segnali in formazione, invalidazioni e semplice conferma del momentum.

**Peso operativo: 0.** Non modifica il Global Confluence, non cambia le soglie del Paper Trading e non apre né blocca operazioni. I risultati vengono misurati prima di qualsiasi futura decisione sul peso.

## Sintesi corrente

| Asset   | Daily                                                | Stato D       | Weekly                     | Stato W    | Lettura weekly                                                                                                              |   Peso |
|:--------|:-----------------------------------------------------|:--------------|:---------------------------|:-----------|:----------------------------------------------------------------------------------------------------------------------------|-------:|
| BTC     | Hidden bullish                                       | IN_FORMAZIONE | Misto / nessuna divergenza | CONTESTO   | Misto / nessuna divergenza. Non esiste una divergenza confermata sugli ultimi pivot.                                        |      0 |
| SOL     | Misto / nessuna divergenza                           | CONTESTO      | Hidden bearish             | CONFERMATA | Hidden bearish confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto. |      0 |
| DOGE    | Momentum in miglioramento, divergenza non confermata | CONTESTO      | Misto / nessuna divergenza | CONTESTO   | Misto / nessuna divergenza. Non esiste una divergenza confermata sugli ultimi pivot.                                        |      0 |

## Dettaglio dei pivot

| Asset   | TF   | Tipo                                                 | Stato         | Prezzo / RSI      | Pivot confrontati                                                 | Δ prezzo contesto   | Δ RSI contesto   |   Peso |
|:--------|:-----|:-----------------------------------------------------|:--------------|:------------------|:------------------------------------------------------------------|:--------------------|:-----------------|-------:|
| BTC     | 1D   | Hidden bullish                                       | IN_FORMAZIONE | 64.150 $ / 52,31  | 2026-08-03 62.227 $ / RSI 47,40 → 2026-08-14 62.488 $ / RSI 42,71 | n/a                 | n/a              |      0 |
| BTC     | 1W   | Misto / nessuna divergenza                           | CONTESTO      | 64.150 $ / 40,97  | n/a                                                               | +0,61%              | 2,50             |      0 |
| SOL     | 1D   | Misto / nessuna divergenza                           | CONTESTO      | 75,67 $ / 52,48   | n/a                                                               | +2,99%              | 7,30             |      0 |
| SOL     | 1W   | Hidden bearish                                       | CONFERMATA    | 75,67 $ / 40,76   | 2026-05-17 98,27 $ / RSI 38,29 → 2026-07-05 83,81 $ / RSI 42,25   | n/a                 | n/a              |      0 |
| DOGE    | 1D   | Momentum in miglioramento, divergenza non confermata | CONTESTO      | 0.06972 $ / 45,31 | n/a                                                               | -0,60%              | 2,84             |      0 |
| DOGE    | 1W   | Misto / nessuna divergenza                           | CONTESTO      | 0.06972 $ / 32,82 | n/a                                                               | -4,08%              | -0,58            |      0 |

### BTC

- **1D — Hidden bullish / IN_FORMAZIONE**: Hidden bullish in formazione: il secondo estremo non è ancora un pivot confermato. Peso operativo sempre 0.
- **1W — Misto / nessuna divergenza / CONTESTO**: Misto / nessuna divergenza. Non esiste una divergenza confermata sugli ultimi pivot.

### SOL

- **1D — Misto / nessuna divergenza / CONTESTO**: Misto / nessuna divergenza. Non esiste una divergenza confermata sugli ultimi pivot.
- **1W — Hidden bearish / CONFERMATA**: Hidden bearish confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto.

### DOGE

- **1D — Momentum in miglioramento, divergenza non confermata / CONTESTO**: Momentum in miglioramento, divergenza non confermata. Non esiste una divergenza confermata sugli ultimi pivot.
- **1W — Misto / nessuna divergenza / CONTESTO**: Misto / nessuna divergenza. Non esiste una divergenza confermata sugli ultimi pivot.

## Tracker live delle divergenze confermate

Viene salvato un solo evento per combinazione di asset, timeframe, tipo e coppia di pivot. Gli esiti vengono controllati dopo 30, 60, 90 e 180 giorni.

- Eventi indipendenti salvati: **7**.
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

Generato: 2026-08-18 05:32 UTC


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

| Asset   | Prezzo   |   Punteggio | Verdetto         | Trend            | Momentum       | Struttura                                             |   Pattern score | Fibonacci      | Pattern rialzista         | Pattern ribassista         | Supporto   | Resistenza   |
|:--------|:---------|------------:|:-----------------|:-----------------|:---------------|:------------------------------------------------------|----------------:|:---------------|:--------------------------|:---------------------------|:-----------|:-------------|
| BTC | 64.178 $ | -1 | NEUTRALE / MISTO | Trend misto | Momentum misto | Compressione / triangolo | 0 | 0 / TESTATO | Doppio minimo / CANDIDATO | Doppio massimo / CANDIDATO | 62.227 | 65.402 |
| SOL | 75,70 $ | -3 | DEBOLE | Trend misto | Momentum misto | Struttura ribassista con massimi e minimi decrescenti | 0 | 0 / TENUTO | Doppio minimo / CANDIDATO | Doppio massimo / CANDIDATO | 70,69 | 77,62 |
| DOGE | 0.06976 $ | 0 | NEUTRALE / MISTO | Trend ribassista | Momentum misto | Struttura rialzista con massimi e minimi crescenti | 0 | 0 / NON ATTIVO | Doppio minimo / CANDIDATO | Doppio massimo / CANDIDATO | 0.06895 | 0.07286 |

## Riepilogo ciclo di vita pattern

| Asset   | Doppio minimo   | Triplo minimo   | Adam/Eve Bottom                 | Doppio massimo   | Triplo massimo   | Adam/Eve Top                 |   Punteggio pattern |
|:--------|:----------------|:----------------|:--------------------------------|:-----------------|:-----------------|:-----------------------------|--------------------:|
| BTC | CANDIDATO | CANDIDATO | Adam and Eve Bottom — CANDIDATO | CANDIDATO | CANDIDATO | Adam and Eve Top — CANDIDATO | 0 |
| SOL | CANDIDATO | CANDIDATO | Adam and Eve Bottom — CANDIDATO | CANDIDATO | CANDIDATO | Adam and Eve Top — CANDIDATO | 0 |
| DOGE | CANDIDATO | CANDIDATO | Adam and Eve Bottom — CANDIDATO | CANDIDATO | CANDIDATO | Adam and Eve Top — CANDIDATO | 0 |

## Indicatori tecnici

| Asset   |   RSI 14 |   Istogramma MACD | MA20    | MA50    | MA200   | Pendenza MA50 20g   | Pendenza MA200 60g   | Rendimento 30g   | Rendimento 90g   |
|:--------|---------:|------------------:|:--------|:--------|:--------|:--------------------|:---------------------|:-----------------|:-----------------|
| BTC | 52.48 | -77.3312 | 63.798 | 63.661 | 69.137 | 0,52% | -10,22% | -0,79% | -17,15% |
| SOL | 52.59 | 0.13571 | 74,52 | 76,14 | 81,57 | 2,29% | -16,85% | -0,86% | -12,02% |
| DOGE | 45.5 | 0.00019 | 0.06992 | 0.07183 | 0.08993 | -6,07% | -16,74% | -3,53% | -32,65% |

## Dettaglio asset

### BTC

- Prezzo: **64.178 $**
- Punteggio tecnico: **-1 / 12**
- Verdetto: **NEUTRALE / MISTO**
- Trend: **Trend misto** (1)
- Momentum: **Momentum misto** (-1)
- Volume: **Volume da distribuzione** (-2)
- Struttura: **Compressione / triangolo** (0)
  - Dettaglio struttura: Ultimi minimi: 5.775e+04 -> 6.223e+04. Ultimi massimi: 6.691e+04 -> 6.54e+04.
- Divergenza: **Nessuna** (0)
- Fase Wyckoff candidata: **Possibile accumulazione** (1)
  - Dettaglio Wyckoff: Prezzo sotto MA200, vicino alla parte bassa del range a 120 giorni, RSI 52.5.
- Fibonacci automatico: **TESTATO** (0)
  - Swing UP 2026-07-01 57.748 -> 2026-08-09 65.402; livello più vicino 23.6% a 63.595; stato TESTATO; confluenza: nessuna confluenza indipendente.
- Punteggio pattern: **0**
  - rialzista dominante: Doppio minimo (CANDIDATO, 0); ribassista dominante: Doppio massimo (CANDIDATO, 0).
- Supporto più vicino: **62.227**
- Resistenza più vicina: **65.402**

Pattern classici e ciclo di vita:

- Doppio minimo: **CANDIDATO** (0)
  - Due minimi simili vicino a 62.201 tra 2026-06-18 e 2026-08-03. Neckline stimata: 66.910. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 15 giorni.
  - neckline 66.910; target 71.619; distanza dalla neckline 4,26%; prezzo sotto neckline.
- Triplo minimo: **CANDIDATO** (0)
  - Tre minimi simili vicino a 62.201 dal 2026-03-29 al 2026-08-03. Neckline stimata: 82.792. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 15 giorni.
  - neckline 82.792; target 103.383; distanza dalla neckline 29,00%; prezzo sotto neckline.
- Adam and Eve Bottom: **CANDIDATO** (0)
  - Pattern Adam and Eve Bottom vicino a 59.109 dal 2026-06-05 al 2026-08-03. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 67.248. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 15 giorni.
  - neckline 67.248; target 75.387; distanza dalla neckline 4,78%; prezzo sotto neckline.
- Doppio massimo: **CANDIDATO** (0)
  - Due massimi simili vicino a 65.544 tra 2026-06-22 e 2026-08-09. Neckline ribassista stimata: 57.748. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 9 giorni.
  - neckline 57.748; target 49.952; distanza dalla neckline 11,13%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 65.544 dal 2026-06-22 al 2026-08-09. Neckline ribassista stimata: 57.748. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 9 giorni.
  - neckline 57.748; target 49.952; distanza dalla neckline 11,13%; prezzo sopra neckline.
- Adam and Eve Top: **CANDIDATO** (0)
  - Pattern Adam and Eve Top vicino a 67.248 dal 2026-06-15 al 2026-07-21. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 57.748. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 28 giorni.
  - neckline 57.748; target 48.247; distanza dalla neckline 11,13%; prezzo sopra neckline.

### SOL

- Prezzo: **75,70 $**
- Punteggio tecnico: **-3 / 12**
- Verdetto: **DEBOLE**
- Trend: **Trend misto** (-1)
- Momentum: **Momentum misto** (1)
- Volume: **Volume da accumulazione** (1)
- Struttura: **Struttura ribassista con massimi e minimi decrescenti** (-2)
  - Dettaglio struttura: Ultimi minimi: 73.4 -> 70.69. Ultimi massimi: 78.73 -> 77.62.
- Divergenza: **Nessuna** (0)
- Fase Wyckoff candidata: **Markdown / fase ribassista** (-2)
  - Dettaglio Wyckoff: Prezzo sotto MA200 con trend a 90 giorni ancora debole.
- Fibonacci automatico: **TENUTO** (0)
  - Swing UP 2026-06-06 60,41 -> 2026-08-09 77,62; livello più vicino 23.6% a 73,56; stato TENUTO; confluenza: nessuna confluenza indipendente.
- Punteggio pattern: **0**
  - rialzista dominante: Doppio minimo (CANDIDATO, 0); ribassista dominante: Doppio massimo (CANDIDATO, 0).
- Supporto più vicino: **70,69**
- Resistenza più vicina: **77,62**

Pattern classici e ciclo di vita:

- Doppio minimo: **CANDIDATO** (0)
  - Due minimi simili vicino a 67,92 tra 2026-06-19 e 2026-08-01. Neckline stimata: 83,81. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 17 giorni.
  - neckline 83,81; target 99,70; distanza dalla neckline 10,71%; prezzo sotto neckline.
- Triplo minimo: **CANDIDATO** (0)
  - Tre minimi simili vicino a 67,92 dal 2026-06-19 al 2026-08-01. Neckline stimata: 83,81. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 17 giorni.
  - neckline 83,81; target 99,70; distanza dalla neckline 10,71%; prezzo sotto neckline.
- Adam and Eve Bottom: **CANDIDATO** (0)
  - Pattern Adam and Eve Bottom vicino a 67,92 dal 2026-06-19 al 2026-08-01. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 83,81. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 17 giorni.
  - neckline 83,81; target 99,70; distanza dalla neckline 10,71%; prezzo sotto neckline.
- Doppio massimo: **CANDIDATO** (0)
  - Due massimi simili vicino a 77,62 tra 2026-06-22 e 2026-08-09. Neckline ribassista stimata: 64,42. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 9 giorni.
  - neckline 64,42; target 51,22; distanza dalla neckline 17,51%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 78,88 dal 2026-07-15 al 2026-08-09. Neckline ribassista stimata: 70,69. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 9 giorni.
  - neckline 70,69; target 62,51; distanza dalla neckline 7,08%; prezzo sopra neckline.
- Adam and Eve Top: **CANDIDATO** (0)
  - Pattern Adam and Eve Top vicino a 77,62 dal 2026-06-15 al 2026-08-09. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 64,42. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 9 giorni.
  - neckline 64,42; target 51,22; distanza dalla neckline 17,51%; prezzo sopra neckline.

### DOGE

- Prezzo: **0.06976 $**
- Punteggio tecnico: **0 / 12**
- Verdetto: **NEUTRALE / MISTO**
- Trend: **Trend ribassista** (-3)
- Momentum: **Momentum misto** (1)
- Volume: **Volume da distribuzione** (-1)
- Struttura: **Struttura rialzista con massimi e minimi crescenti** (2)
  - Dettaglio struttura: Ultimi minimi: 0.06835 -> 0.06895. Ultimi massimi: 0.07117 -> 0.07286.
- Divergenza: **Nessuna** (0)
- Fase Wyckoff candidata: **Possibile accumulazione** (1)
  - Dettaglio Wyckoff: Prezzo sotto MA200, vicino alla parte bassa del range a 120 giorni, RSI 45.5.
- Fibonacci automatico: **NON ATTIVO** (0)
  - Swing DOWN 2026-05-14 0.11825 -> 2026-08-12 0.06895; livello più vicino 23.6% a 0.08059; stato NON ATTIVO; confluenza: nessuna confluenza indipendente.
- Punteggio pattern: **0**
  - rialzista dominante: Doppio minimo (CANDIDATO, 0); ribassista dominante: Doppio massimo (CANDIDATO, 0).
- Supporto più vicino: **0.06895**
- Resistenza più vicina: **0.07286**

Pattern classici e ciclo di vita:

- Doppio minimo: **CANDIDATO** (0)
  - Due minimi simili vicino a 0.06829 tra 2026-07-24 e 2026-08-12. Neckline stimata: 0.07380. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 6 giorni.
  - neckline 0.07380; target 0.07931; distanza dalla neckline 5,80%; prezzo sotto neckline.
- Triplo minimo: **CANDIDATO** (0)
  - Tre minimi simili vicino a 0.06835 dal 2026-06-30 al 2026-08-12. Neckline stimata: 0.07923. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 6 giorni.
  - neckline 0.07923; target 0.09012; distanza dalla neckline 13,58%; prezzo sotto neckline.
- Adam and Eve Bottom: **CANDIDATO** (0)
  - Pattern Adam and Eve Bottom vicino a 0.06829 dal 2026-07-24 al 2026-08-06. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 0.07380. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 12 giorni.
  - neckline 0.07380; target 0.07931; distanza dalla neckline 5,80%; prezzo sotto neckline.
- Doppio massimo: **CANDIDATO** (0)
  - Due massimi simili vicino a 0.07380 tra 2026-07-26 e 2026-08-11. Neckline ribassista stimata: 0.06797. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 7 giorni.
  - neckline 0.06797; target 0.06214; distanza dalla neckline 2,63%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 0.07923 dal 2026-07-04 al 2026-08-11. Neckline ribassista stimata: 0.06797. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 7 giorni.
  - neckline 0.06797; target 0.05671; distanza dalla neckline 2,63%; prezzo sopra neckline.
- Adam and Eve Top: **CANDIDATO** (0)
  - Pattern Adam and Eve Top vicino a 0.07923 dal 2026-07-04 al 2026-08-11. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 0.06797. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 7 giorni.
  - neckline 0.06797; target 0.05671; distanza dalla neckline 2,63%; prezzo sopra neckline.

## Fibonacci automatico

Il modulo seleziona uno swing recente tramite pivot confermati. Un semplice tocco vale 0: Fibonacci pesa al massimo ±1 soltanto quando il livello è tenuto, perso, recuperato o respinto e coincide con almeno un livello tecnico indipendente.

| Asset   | Swing                         | 23,6%   | 38,2%   | 50,0%   | 61,8%   | 78,6%   | Livello vicino   | Stato      | Confluenza                      |   Score |
|:--------|:------------------------------|:--------|:--------|:--------|:--------|:--------|:-----------------|:-----------|:--------------------------------|--------:|
| BTC | UP 2026-07-01 -> 2026-08-09 | 63.595 | 62.478 | 61.575 | 60.672 | 59.386 | 23.6% / 63.595 | TESTATO | nessuna confluenza indipendente | 0 |
| SOL | UP 2026-06-06 -> 2026-08-09 | 73,56 | 71,05 | 69,02 | 66,99 | 64,10 | 23.6% / 73,56 | TENUTO | nessuna confluenza indipendente | 0 |
| DOGE | DOWN 2026-05-14 -> 2026-08-12 | 0.08059 | 0.08779 | 0.09360 | 0.09942 | 0.10770 | 23.6% / 0.08059 | NON ATTIVO | nessuna confluenza indipendente | 0 |

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

- **BTC**: 17/30 previsioni controllate su 45 fatte. Stato: **RACCOLTA DATI**.
- **SOL**: 17/30 previsioni controllate su 45 fatte. Stato: **RACCOLTA DATI**.
- **DOGE**: 17/30 previsioni controllate su 45 fatte. Stato: **RACCOLTA DATI**.

| Asset | Previsioni fatte | Controllate | Progresso | In attesa | Stato | Prossimo controllo |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 45 | 17 | 17/30 [██████░░░░] | 28 | RACCOLTA DATI | 2026-08-19 / tra 1 giorno |
| SOL | 45 | 17 | 17/30 [██████░░░░] | 28 | RACCOLTA DATI | 2026-08-19 / tra 1 giorno |
| DOGE | 45 | 17 | 17/30 [██████░░░░] | 28 | RACCOLTA DATI | 2026-08-19 / tra 1 giorno |

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

Generato: 2026-08-18 05:33 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [data_quality_coherence_report.md](data_quality_coherence_report.md)

Questo controllo non modifica punteggi o decisioni. Verifica che tutti i moduli usino lo stesso prezzo corrente e che le nuove regole Technical/Classic Visual siano integre.

## Stato finale: **OK**

## Prezzo unico per modulo

| Modulo                  | Asset   | Campo             | Stato   | Prezzo snapshot   | Prezzo modulo   | Differenza   |
|:------------------------|:--------|:------------------|:--------|:------------------|:----------------|:-------------|
| Scanner                 | BTC     | current_price     | OK      | 64.178 $          | 64.178 $        | +0,0000%     |
| Scanner                 | DOGE    | current_price     | OK      | 0.06976 $         | 0.06976 $       | -0,0000%     |
| Scanner                 | SOL     | current_price     | OK      | 75,70 $           | 75,70 $         | +0,0000%     |
| Scanner Forecast        | BTC     | current_price     | OK      | 64.178 $          | 64.178 $        | +0,0000%     |
| Scanner Forecast        | SOL     | current_price     | OK      | 75,70 $           | 75,70 $         | +0,0000%     |
| Scanner Forecast        | DOGE    | current_price     | OK      | 0.06976 $         | 0.06976 $       | -0,0000%     |
| Technical Structure     | BTC     | price             | OK      | 64.178 $          | 64.178 $        | +0,0000%     |
| Technical Structure     | SOL     | price             | OK      | 75,70 $           | 75,70 $         | +0,0000%     |
| Technical Structure     | DOGE    | price             | OK      | 0.06976 $         | 0.06976 $       | -0,0000%     |
| Classic Technical       | BTC     | price             | OK      | 64.178 $          | 64.178 $        | +0,0000%     |
| Classic Technical       | SOL     | price             | OK      | 75,70 $           | 75,70 $         | +0,0000%     |
| Classic Technical       | DOGE    | price             | OK      | 0.06976 $         | 0.06976 $       | -0,0000%     |
| Classic Visual          | BTC     | price             | OK      | 64.178 $          | 64.178 $        | +0,0000%     |
| Classic Visual          | SOL     | price             | OK      | 75,70 $           | 75,70 $         | +0,0000%     |
| Classic Visual          | DOGE    | price             | OK      | 0.06976 $         | 0.06976 $       | -0,0000%     |
| Exchange Microstructure | BTC     | price             | OK      | 64.178 $          | 64.192 $        | +0,0221%     |
| Exchange Microstructure | SOL     | price             | OK      | 75,70 $           | 75,81 $         | +0,1493%     |
| Exchange Microstructure | DOGE    | price             | OK      | 0.06976 $         | 0.06989 $       | +0,1864%     |
| RSI top-cycle           | SOL     | current_price     | OK      | 75,70 $           | 75,70 $         | +0,0000%     |
| RSI top-cycle           | SOL     | current_price     | OK      | 75,70 $           | 75,70 $         | +0,0000%     |
| Frattale BTC/SOL        | SOL     | sol_current_price | OK      | 75,70 $           | 75,70 $         | +0,0000%     |
| Fractal path            | SOL     | current_price     | OK      | 75,70 $           | 75,70 $         | +0,0000%     |

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

Generato: 2026-08-18T20:30:35+00:00

- Modalità: **SOLO PAPER TRADING**
- Asset: **SOL spot**
- Leva: **nessuna (1x)**
- Capitale iniziale separato: **€40.000,00**
- Fonte mercato: **KUCOIN_PUBLIC_API**; nuove entrate: **CONSENTITE**

| Equity | Cash | SOL | Prezzo | Rendimento | Realizzato | Commissioni | Max DD | Operazioni |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €41.544,83 | €17.544,74 | 311.135932 | 77.1370 | +3.86% | €568,83 | €49,51 | 6.48% | 8 |

**Ultima decisione:** HOLD — Prezzo dentro la fascia neutrale.

Bande 4H: L2 70.8816 · L1 72.9997 · media 75.6474 · U1 78.2951 · U2 80.4132.

> Questo portafoglio non condivide capitale, posizioni o statistiche con il paper trading da €10.000.
<!-- SOL_SPOT_ADAPTIVE_END -->
