<!-- COMPACT_REPORT_HEADER_START -->
> **Vista compatta:** Decisione operativa, Global Confluence e cambiamenti giornalieri restano aperti. Tocca il titolo di una sezione per mostrare o nascondere i dettagli.  
> Tutte le tabelle e tutti i dati restano nel file: copiando il Markdown raw viene copiato tutto.
<!-- COMPACT_REPORT_HEADER_END -->

<!-- COMPACT_SECTION_START:decision -->
<details open>
<summary><strong>🧭 Decisione operativa — da leggere per prima</strong></summary>

<!-- DECISION_REPORT_START -->

# Decisione operativa sintetica

Generato: 2026-09-13 05:33 UTC

Report separato completo: [decision_report.md](decision_report.md)

Sintesi automatica dello scanner: l'azione spot viene copiata direttamente dal Global Confluence; long, short e rischio restano filtri separati e più prudenti.

| Asset | Global | Direzione | Spot | Long leva | Short leva | Max long | Max short | Rischio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +6 | BULLISH | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE | LONG PRUDENTE | NO SHORT | max 2x isolated | nessuna | MEDIO |
| SOL | +4 | NEUTRALE / COSTRUTTIVO | HOLD / TRANCHE PICCOLE, NO LEVA | NO LONG A LEVA | NO SHORT | nessuna | nessuna | MOLTO ALTO |
| DOGE | -5 | BEARISH | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE | NO LONG A LEVA | SHORT SOLO DOPO SPIKE | nessuna | max 1x-2x isolated | MOLTO ALTO |

## Lettura immediata

- **BTC**: Global = **+6**, spot = **ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE**, long = **LONG PRUDENTE**, short = **NO SHORT**, rischio = **MEDIO**.
- **SOL**: Global = **+4**, spot = **HOLD / TRANCHE PICCOLE, NO LEVA**, long = **NO LONG A LEVA**, short = **NO SHORT**, rischio = **MOLTO ALTO**.
- **DOGE**: Global = **-5**, spot = **STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE**, long = **NO LONG A LEVA**, short = **SHORT SOLO DOPO SPIKE**, rischio = **MOLTO ALTO**.

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

- Global Confluence: **+4**
- Confluenza: **MODERATAMENTE POSITIVA**
- Bias Global: **Costruttivo prudente**
- Direzione decisionale: **NEUTRALE / COSTRUTTIVO**
- Azione spot dal Global: **HOLD / TRANCHE PICCOLE, NO LEVA**
- Long leva: **NO LONG A LEVA**
- Short leva: **NO SHORT**
- Rischio: **MOLTO ALTO**
- Conferme: Doppio minimo target raggiunto finché mantiene 78,73; nuova conferma tecnica sopra 107,12; milestone analogiche 108,90 / 134,15, valide soltanto se rientra anche il gap frattale.
- Invalidazioni: Allarmi sotto 88,83 / 97,45 / 62,19.

### DOGE

- Global Confluence: **-5**
- Confluenza: **NEGATIVA**
- Bias Global: **Ribassista**
- Direzione decisionale: **BEARISH**
- Azione spot dal Global: **STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE**
- Long leva: **NO LONG A LEVA**
- Short leva: **SHORT SOLO DOPO SPIKE**
- Rischio: **MOLTO ALTO**
- Conferme: Sopra 0.09421 migliora; sopra 0.06933 viene invalidato il pattern ribassista dominante.
- Invalidazioni: Sotto 0.08028 il rischio ribassista aumenta.

## Nota semplice

- **Spot** = usa la stessa azione del Global Confluence, senza una seconda mappatura che possa produrre frasi diverse.
- **Zona alta storica** = zona dove non inseguire troppo; può essere zona da prendere profitto.
- **Zona bassa storica** = zona di rischio; con leva la liquidazione non dovrebbe stare lì vicino.
- **BTC leva** = nessun long a leva finché il prezzo snapshot non supera **67.248 $**; sotto quella soglia resta solo l'azione spot indicata dal Global.
- **Lifecycle EMA200** = per SOL resta solo contesto, peso Global 0; score interno 2; EMA200 circa 111,24 $; upside verso EMA200 +9,25%. Non autorizza leva e non aggiunge punti automatici.
- **NO LONG** non significa automaticamente **SHORT**. Lo short ha senso solo se il quadro è bearish o se lo spike viene spesso scaricato.
- Per SOL, se il Global è da **+3 in su**, la decisione non deve diventare bearish solo perché lo scanner grezzo a 30 giorni è incerto.

<!-- DECISION_REPORT_END -->

<!-- PAPER_TRADING_START -->
# Paper trading automatico KuCoin

Generato: 2026-09-13T05:33:17+00:00


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [paper_trading_report.md](paper_trading_report.md)

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-09-13T05:05:33+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-09-13T05:05:33+00:00 | 2026-09-13T05:05:33+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-09-13T04:45:00+00:00 | 2026-09-13T04:45:00+00:00 | 5,7 min | 25,0 min | OK |
| 60m | 12 | 2026-09-13T04:00:00+00:00 | 2026-09-13T04:00:00+00:00 | 5,7 min | 45,0 min | OK |
| 240m | 12 | 2026-09-13T00:00:00+00:00 | 2026-09-13T00:00:00+00:00 | 1,10 h | 1,00 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | LONGXIA | 240m | LONG | 6,25 | 6,00 | 0,00 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | UNI | 240m | LONG | 5,08 | 6,00 | 0,92 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | RIVER | 240m | SHORT | -4,81 | 6,00 | 1,19 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | DOGE | 240m | SHORT | -4,21 | 6,00 | 1,79 | STALE_CANDLE | 1,10 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | BTC | 240m | SHORT | -3,75 | 6,00 | 2,25 | STALE_CANDLE | 1,10 h | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | ZEC | 240m | LONG | 3,50 | 6,00 | 2,50 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | HYPE | 240m | SHORT | -3,01 | 6,00 | 2,99 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | SOL | 240m | SHORT | -2,22 | 6,00 | 3,78 | STALE_CANDLE | 1,10 h | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | ADA | 240m | SHORT | -2,02 | 6,00 | 3,98 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | PEPE | 240m | LONG | 0,97 | 6,00 | 5,03 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | XRP | 240m | SHORT | -0,74 | 6,00 | 5,26 | STALE_CANDLE | 1,10 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| 1H Balanced Long No Rhv V1 | LONGXIA | 60m | LONG | 7,75 | 5,00 | 0,00 | READY | 5,7 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Bilanciata 1H V2 | LONGXIA | 60m | LONG | 7,75 | 5,50 | 0,00 | READY | 5,7 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Fast No Pepe V1 | LONGXIA | 60m | LONG | 7,75 | 4,50 | 0,00 | READY | 5,7 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Fast Tp2 V1 | LONGXIA | 60m | LONG | 7,75 | 4,50 | 0,00 | READY | 5,7 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Rapida 1H V3 Filtered | LONGXIA | 60m | LONG | 7,75 | 4,50 | 0,00 | READY | 5,7 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Fast V3 Nohigh V1 | LONGXIA | 60m | LONG | 7,75 | 4,50 | 0,00 | READY | 5,7 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Fast V3 Long Only V1 | LONGXIA | 60m | LONG | 7,75 | 4,50 | 0,00 | READY | 5,7 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Fast V3 No Esports V1 | LONGXIA | 60m | LONG | 7,75 | 4,50 | 0,00 | READY | 5,7 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Fast V3 No Esports Long Only V1 | LONGXIA | 60m | LONG | 7,75 | 4,50 | 0,00 | READY | 5,7 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.811,51 | -1,88% | €2,95 | €3.000,00 | 0,10% | 5 | 60 | 41,67% | 0,88 | 6,86% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 60 | 3476 | PRIME INDICAZIONI | 100 (mancano 40) |

- Trade del Principale 4H chiusi: **60**; win rate **41,67%**; profit factor **0,88**.
- Expectancy: **€-3,05** per trade; P&L netto: **€-182,77**; max drawdown: **6,86%**.
- Valutazione: **Si può osservare la direzione, ma il risultato resta fragile.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 5 | €9.811,51 | €700,63 | €2.101,90 | €196,32 | €-4,63 |
| TEST | Benchmark Donchian breakout 1H | 7 | €11.416,15 | €2.011,40 | €4.022,79 | €174,04 | €28,61 |
| TEST | Donchian 1H Gb20 120R V1 | 7 | €11.147,37 | €1.964,04 | €3.928,08 | €169,94 | €27,94 |
| TEST | Main Side Regime Guard V1 | 7 | €11.064,75 | €772,48 | €2.317,44 | €221,25 | €-0,06 |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | 7 | €11.014,85 | €712,13 | €2.136,38 | €166,65 | €0,00 |
| TEST | Scanner Top 5 Long 1H | 6 | €10.940,10 | €1.183,06 | €2.366,13 | €218,81 | €-0,29 |
| TEST | Combo Trend Side Regime Guard V1 | 6 | €10.682,78 | €1.449,24 | €2.898,47 | €167,65 | €-107,54 |
| TEST | 1H Fast No Pepe V1 | 7 | €10.503,89 | €1.326,22 | €3.978,66 | €210,07 | €-64,75 |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | 3 | €10.484,46 | €1.582,70 | €4.748,11 | €105,12 | €-88,96 |
| TEST | Combo Adaptive Long Only V1 | 7 | €10.478,86 | €2.484,93 | €4.969,86 | €213,31 | €-5,13 |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | 6 | €10.443,34 | €1.586,40 | €4.759,20 | €210,71 | €49,41 |
| TEST | Rapida 1H V2 | 2 | €10.428,35 | €2.179,16 | €6.537,48 | €103,84 | €-33,08 |
| TEST | Rapida 1H V3 Filtered | 6 | €10.376,25 | €1.576,21 | €4.728,62 | €209,35 | €49,10 |
| TEST | Combo Adaptive | 8 | €10.362,05 | €1.318,43 | €2.636,85 | €156,30 | €-2,85 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 0 | €10.300,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | 5 | €10.278,78 | €1.273,61 | €3.820,82 | €155,39 | €-42,00 |
| TEST | Sol Donchian 1H | 0 | €10.276,07 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Main Dynamic Asset Selector V1 | 2 | €10.272,37 | €326,63 | €979,88 | €101,99 | €-20,57 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 0 | €10.271,73 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top 5 + forza BTC 1H | 6 | €10.254,47 | €1.100,94 | €2.201,87 | €205,39 | €-3,70 |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 0 | €10.239,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 0 | €10.235,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top15 Long | 6 | €10.191,75 | €1.622,59 | €3.245,18 | €154,79 | €-18,83 |
| TEST | Scanner Top20 Long | 6 | €10.191,75 | €1.622,59 | €3.245,18 | €154,79 | €-18,83 |
| TEST | Scanner Top10 Long | 6 | €10.185,49 | €2.349,71 | €4.699,42 | €203,79 | €-3,86 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 0 | €10.185,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Donchian 1H | 0 | €10.164,08 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Ampia 4H | 8 | €10.154,52 | €1.042,60 | €2.085,19 | €203,85 | €-38,40 |
| TEST | Btc Bollinger 1H | 0 | €10.151,49 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Scanner | 6 | €10.149,08 | €1.541,44 | €3.082,88 | €207,77 | €-119,93 |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 0 | €10.145,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 4H | 0 | €10.138,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Score 6 75 Range Only V1 | 5 | €10.115,29 | €1.263,43 | €3.790,30 | €154,78 | €-55,83 |
| TEST | Btc Bollinger 4H | 0 | €10.101,88 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 0 | €10.099,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Partial 1R V1 | 5 | €10.049,05 | €1.969,94 | €3.939,88 | €151,12 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 0 | €10.048,77 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V1 | 0 | €10.043,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Tp2 V1 | 6 | €10.042,03 | €604,62 | €1.813,85 | €150,55 | €0,00 |
| TEST | Sol Donchian 4H | 0 | €10.040,14 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Ema 1H | 1 | €10.037,01 | €694,33 | €2.082,98 | €50,26 | €-15,03 |
| TEST | Scalp RSI Long 20 · prudente · 5x | 0 | €10.032,32 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Nohigh Range Only V1 | 3 | €10.023,56 | €1.671,72 | €5.015,16 | €101,51 | €-87,28 |
| TEST | Scalp RSI Short 85 · €50 · 15x | 0 | €10.022,70 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | 2 | €10.020,28 | €362,84 | €1.088,52 | €96,64 | €0,00 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €10.014,08 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €50 · 15x | 0 | €10.009,44 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 0 | €10.008,92 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 4H | 0 | €10.005,51 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €10 · 15x | 0 | €10.004,54 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 0 | €10.003,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 0 | €10.002,82 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Balanced Short Trend Down Strict V1 | 0 | €10.002,17 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €10 · 15x | 0 | €10.001,89 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Continuation V1 | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €10 · 15x | 0 | €9.998,68 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · prudente · 5x | 0 | €9.996,83 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 0 | €9.995,23 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €10 · 15x | 0 | €9.994,07 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €50 · 15x | 0 | €9.993,42 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €10 · 15x | 0 | €9.988,91 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 4H | 0 | €9.980,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €50 · 15x | 0 | €9.970,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · prudente · 5x | 0 | €9.970,34 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 4H | 0 | €9.964,84 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 0 | €9.964,27 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €50 · 15x | 0 | €9.944,53 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 1H | 0 | €9.942,44 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 No Esports Long Only V1 | 5 | €9.941,16 | €515,90 | €1.547,71 | €149,35 | €0,00 |
| TEST | Scalp RSI Short 80 · prudente · 5x | 0 | €9.939,55 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 1H | 0 | €9.939,44 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | 0 | €9.935,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Bollinger 1H | 0 | €9.925,44 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.917,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 4H | 0 | €9.914,14 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 1H | 0 | €9.899,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Side Regime Guard V1 | 6 | €9.889,77 | €1.079,81 | €2.159,63 | €99,18 | €-2,80 |
| TEST | Btc Adaptive 1H | 0 | €9.888,02 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | 2 | €9.864,62 | €354,62 | €1.063,86 | €94,46 | €0,00 |
| TEST | Scanner Top5 Btc Tp3 V1 | 6 | €9.860,83 | €2.894,41 | €5.788,83 | €197,66 | €-20,25 |
| TEST | Scanner Top5 Btc Runner25 V1 | 6 | €9.855,06 | €2.892,72 | €5.785,44 | €197,55 | €-20,24 |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 0 | €9.837,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Forza relativa 1H V2 | 6 | €9.834,39 | €841,03 | €1.682,06 | €99,39 | €-0,77 |
| TEST | Eth Ema 4H | 1 | €9.822,24 | €599,05 | €1.198,10 | €49,17 | €-11,50 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 0 | €9.817,34 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Quality7 Regime V1 | 0 | €9.810,21 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 4H | 0 | €9.808,89 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Nohigh V1 | 4 | €9.805,15 | €1.180,13 | €3.540,40 | €192,13 | €-63,04 |
| TEST | Eth Bollinger 1H | 0 | €9.800,08 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 0 | €9.762,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Nohigh Cap75 V1 | 5 | €9.759,15 | €1.024,07 | €3.072,22 | €146,80 | €40,81 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 0 | €9.723,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 1H | 0 | €9.711,69 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Global Confluence puro 1H | 1 | €9.689,84 | €847,30 | €1.694,61 | €48,51 | €-11,21 |
| TEST | 1H Fast V3 Long Only V1 | 4 | €9.680,11 | €861,15 | €2.583,46 | €145,36 | €0,00 |
| TEST | Scanner Top5 Btc Guard V1 | 6 | €9.674,83 | €1.071,35 | €2.142,71 | €193,51 | €-0,79 |
| TEST | Eth Donchian 1H | 0 | €9.638,99 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Balanced Long No Rhv V1 | 5 | €9.633,54 | €1.170,56 | €3.511,67 | €192,69 | €-1,01 |
| TEST | Scanner Top5 Btc Mfe V1 | 6 | €9.613,06 | €1.032,07 | €2.064,15 | €192,55 | €-3,47 |
| TEST | 1H Fast V3 No Esports V1 | 6 | €9.596,58 | €1.075,56 | €3.226,67 | €193,64 | €45,96 |
| TEST | Eth Adaptive 1H | 1 | €9.594,42 | €1.112,86 | €3.338,57 | €48,08 | €-18,19 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 0 | €9.579,83 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Ema 1H | 1 | €9.547,07 | €1.107,07 | €3.321,22 | €47,83 | €-15,50 |
| TEST | Combo Adaptive Regime V1 | 1 | €9.538,51 | €987,06 | €1.974,12 | €49,09 | €0,00 |
| TEST | Master Adaptive Gb20 Be V1 | 4 | €9.517,70 | €869,45 | €1.738,90 | €144,16 | €0,00 |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | 5 | €9.516,08 | €998,53 | €2.995,59 | €143,15 | €39,79 |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | 5 | €9.515,12 | €2.453,48 | €7.360,45 | €147,03 | €-58,02 |
| TEST | Combo Adaptive Quality7 V1 | 4 | €9.512,30 | €1.438,51 | €2.877,02 | €190,29 | €0,00 |
| TEST | Master Adaptive Gb20 Partial V1 | 4 | €9.507,58 | €868,53 | €1.737,05 | €144,01 | €0,00 |
| TEST | 1H Fast Score 6 75 V1 | 5 | €9.477,84 | €2.395,99 | €7.187,98 | €145,07 | €-57,33 |
| TEST | Master Adaptive Runner25 V1 | 6 | €9.475,88 | €1.860,94 | €3.721,87 | €189,63 | €-4,71 |
| TEST | Master Adaptive V1 | 4 | €9.470,81 | €865,17 | €1.730,33 | €143,45 | €0,00 |
| TEST | Scanner Top5 Btc Guard Mfe V1 | 6 | €9.449,84 | €1.046,45 | €2.092,89 | €189,01 | €-0,78 |
| TEST | Btc Ema 1H | 1 | €9.428,75 | €980,04 | €2.940,12 | €47,16 | €-2,31 |
| TEST | Master Adaptive Expanded V1 | 5 | €9.369,38 | €1.578,17 | €3.156,34 | €187,39 | €-0,07 |
| TEST | Bilanciata 1H V3 Filtered | 7 | €9.350,73 | €1.422,34 | €4.267,01 | €187,13 | €-52,41 |
| TEST | Master Adaptive Gb20 V1 | 4 | €9.345,84 | €853,78 | €1.707,57 | €141,57 | €0,00 |
| TEST | Scanner Bottom10 Short | 4 | €9.320,74 | €1.261,36 | €2.522,73 | €140,86 | €0,00 |
| TEST | Scanner Bottom15 Short | 4 | €9.320,74 | €1.261,36 | €2.522,73 | €140,86 | €0,00 |
| TEST | Scanner Bottom20 Short | 4 | €9.320,74 | €1.261,36 | €2.522,73 | €140,86 | €0,00 |
| TEST | Master Adaptive Gb20 Loss Cap V1 | 7 | €9.317,20 | €2.204,65 | €4.409,30 | €186,51 | €-6,52 |
| TEST | Bilanciata 1H V2 | 5 | €9.309,30 | €1.041,98 | €3.125,94 | €140,50 | €0,00 |
| TEST | Master Adaptive No Alt V1 | 6 | €9.277,66 | €2.405,32 | €4.810,63 | €185,53 | €-5,28 |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | 4 | €9.256,15 | €1.252,64 | €2.505,29 | €139,88 | €0,00 |
| TEST | Scanner Bottom5 Short Profit Lock V1 | 4 | €9.242,07 | €1.250,74 | €2.501,48 | €139,67 | €0,00 |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | 1 | €9.214,28 | €205,67 | €617,01 | €48,38 | €0,00 |
| TEST | Benchmark trend following EMA 1H | 5 | €9.172,75 | €981,82 | €1.963,65 | €144,18 | €-14,38 |
| TEST | Scanner Bottom 5 Short 1H | 4 | €9.170,95 | €1.241,11 | €2.482,23 | €138,60 | €0,00 |
| TEST | Bilanciata 1H V1 | 3 | €9.134,06 | €400,34 | €1.201,03 | €48,28 | €1,31 |
| TEST | Combo Adaptive Runner25 V1 | 6 | €9.108,17 | €1.390,30 | €2.780,60 | €138,36 | €-3,79 |
| TEST | Combo Adaptive Mfe Trail | 7 | €9.035,37 | €1.113,12 | €2.226,24 | €146,48 | €0,00 |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | 6 | €9.023,63 | €2.107,97 | €4.215,95 | €180,90 | €-19,04 |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | 2 | €8.983,79 | €909,26 | €1.818,52 | €47,26 | €-3,70 |
| TEST | Combo Trend | 5 | €8.972,54 | €1.983,96 | €3.967,91 | €94,84 | €-103,09 |
| TEST | Master Adaptive Strict3 V1 | 6 | €8.948,64 | €1.098,44 | €2.196,88 | €178,97 | €0,00 |
| TEST | Combo Adaptive Tp3 V1 | 6 | €8.937,78 | €1.364,31 | €2.728,62 | €135,78 | €-3,72 |
| TEST | 1H Balanced V3 Long Only V1 | 7 | €8.844,27 | €1.349,86 | €4.049,58 | €176,99 | €-49,37 |
| TEST | Combo Mean Reversion | 1 | €8.756,35 | €942,00 | €1.883,99 | €44,59 | €41,04 |
| TEST | 1H Fast V3 Cap75 V1 | 4 | €8.704,67 | €2.209,29 | €6.627,87 | €131,06 | €-44,66 |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | 4 | €8.675,89 | €2.746,43 | €5.492,85 | €173,87 | €-15,53 |
| TEST | Forza relativa 1H V1 | 6 | €8.476,84 | €1.889,51 | €3.779,02 | €128,95 | €30,93 |
| TEST | Scanner Top5 Btc Btc Le3 V1 | 5 | €8.375,72 | €2.844,82 | €5.689,64 | €167,92 | €-18,37 |
| TEST | Benchmark Bollinger mean reversion 1H | 1 | €8.353,29 | €497,61 | €995,23 | €41,84 | €0,00 |

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
| PRINCIPALE | Principale 4H | Confluenza trend | €9.811,51 | €-182,77 | 60 | 60 | 41,67% | 0,88 | €-3,05 | 6,86% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €11.416,15 | €1.389,43 | 153 | 153 | 43,14% | 1,41 | €9,08 | 6,75% |
| TEST | Donchian 1H Gb20 120R V1 | Donchian breakout 20 barre | €11.147,37 | €1.121,28 | 121 | 121 | 41,32% | 1,46 | €9,27 | 6,75% |
| TEST | Main Side Regime Guard V1 | Confluenza trend | €11.064,75 | €1.066,55 | 54 | 54 | 59,26% | 2,21 | €19,75 | 4,35% |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | Momentum / breakout | €11.014,85 | €1.016,26 | 205 | 205 | 48,78% | 1,25 | €4,96 | 7,95% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.940,10 | €941,85 | 181 | 181 | 45,86% | 1,30 | €5,20 | 8,85% |
| TEST | Combo Trend Side Regime Guard V1 | Combo Trend | €10.682,78 | €792,30 | 155 | 155 | 50,32% | 1,27 | €5,11 | 10,10% |
| TEST | 1H Fast No Pepe V1 | Momentum / breakout | €10.503,89 | €569,95 | 282 | 281 | 43,62% | 1,12 | €2,02 | 9,28% |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | Momentum / breakout V3 Filtered | €10.484,46 | €575,83 | 159 | 159 | 48,43% | 1,17 | €3,62 | 5,29% |
| TEST | Combo Adaptive Long Only V1 | Combo Adaptive | €10.478,86 | €487,02 | 173 | 173 | 45,09% | 1,16 | €2,82 | 7,78% |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | Momentum / breakout V3 Filtered | €10.443,34 | €396,91 | 229 | 229 | 48,91% | 1,11 | €1,73 | 9,50% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €10.428,35 | €465,15 | 84 | 75 | 47,62% | 1,22 | €5,54 | 3,89% |
| TEST | Rapida 1H V3 Filtered | Momentum / breakout V3 Filtered | €10.376,25 | €330,11 | 273 | 273 | 44,32% | 1,07 | €1,21 | 9,48% |
| TEST | Combo Adaptive | Combo Adaptive | €10.362,05 | €366,67 | 212 | 212 | 46,70% | 1,11 | €1,73 | 8,17% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | Momentum / breakout V3 Filtered | €10.300,05 | €300,05 | 33 | 33 | 48,48% | 2,04 | €9,09 | 2,01% |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | Momentum / breakout V3 Filtered | €10.278,78 | €267,24 | 161 | 160 | 47,83% | 1,10 | €1,66 | 5,24% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €10.276,07 | €276,07 | 21 | 21 | 57,14% | 1,75 | €13,15 | 2,77% |
| TEST | Main Dynamic Asset Selector V1 | Confluenza trend | €10.272,37 | €293,98 | 22 | 22 | 40,91% | 1,48 | €13,36 | 3,39% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | Momentum / breakout V3 Filtered | €10.271,73 | €271,73 | 22 | 22 | 50,00% | 1,74 | €12,35 | 1,72% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €10.254,47 | €259,52 | 156 | 156 | 44,87% | 1,09 | €1,66 | 11,27% |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | Momentum / breakout V3 Filtered | €10.239,20 | €239,20 | 17 | 17 | 52,94% | 4,50 | €14,07 | 1,01% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | Momentum / breakout V3 Filtered | €10.235,18 | €235,18 | 20 | 20 | 50,00% | 1,90 | €11,76 | 2,73% |
| TEST | Scanner Top15 Long | Scanner Top15 Long | €10.191,75 | €212,57 | 203 | 203 | 46,80% | 1,07 | €1,05 | 10,31% |
| TEST | Scanner Top20 Long | Scanner Top20 Long | €10.191,75 | €212,57 | 203 | 203 | 46,80% | 1,07 | €1,05 | 10,31% |
| TEST | Scanner Top10 Long | Scanner Top10 Long | €10.185,49 | €192,18 | 188 | 188 | 45,74% | 1,07 | €1,02 | 10,31% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | Momentum / breakout V3 Filtered | €10.185,37 | €185,37 | 22 | 22 | 40,91% | 1,57 | €8,43 | 2,27% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €10.164,08 | €164,08 | 18 | 18 | 61,11% | 1,40 | €9,12 | 3,08% |
| TEST | Ampia 4H | Confluenza trend | €10.154,52 | €194,04 | 59 | 59 | 35,59% | 1,15 | €3,29 | 4,45% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.151,49 | €151,49 | 7 | 7 | 71,43% | 2,32 | €21,64 | 0,85% |
| TEST | Combo Scanner | Combo Scanner | €10.149,08 | €270,98 | 188 | 188 | 43,62% | 1,08 | €1,44 | 11,38% |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | Momentum / breakout V3 Filtered | €10.145,12 | €145,12 | 44 | 44 | 45,45% | 1,20 | €3,30 | 2,91% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €10.138,72 | €138,72 | 10 | 10 | 50,00% | 1,64 | €13,87 | 1,37% |
| TEST | 1H Fast Score 6 75 Range Only V1 | Momentum / breakout | €10.115,29 | €173,18 | 63 | 63 | 42,86% | 1,12 | €2,75 | 6,49% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.101,88 | €101,88 | 4 | 4 | 75,00% | 2,86 | €25,47 | 0,91% |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | Momentum / breakout V3 Filtered | €10.099,04 | €99,04 | 55 | 55 | 54,55% | 1,12 | €1,80 | 3,59% |
| TEST | Combo Adaptive Partial 1R V1 | Combo Adaptive | €10.049,05 | €51,39 | 178 | 178 | 44,38% | 1,02 | €0,29 | 8,69% |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | Momentum / breakout V3 Filtered | €10.048,77 | €48,77 | 23 | 23 | 43,48% | 1,12 | €2,12 | 3,05% |
| TEST | Rapida 1H V1 | Momentum / breakout | €10.043,28 | €43,28 | 78 | 78 | 34,62% | 1,02 | €0,55 | 6,76% |
| TEST | 1H Fast Tp2 V1 | Momentum / breakout | €10.042,03 | €43,12 | 283 | 283 | 39,58% | 1,01 | €0,15 | 6,56% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €10.040,14 | €40,14 | 9 | 9 | 33,33% | 1,15 | €4,46 | 2,25% |
| TEST | Doge Ema 1H | Trend following EMA | €10.037,01 | €52,95 | 28 | 28 | 57,14% | 1,08 | €1,89 | 2,77% |
| TEST | Scalp RSI Long 20 · prudente · 5x | Inversione RSI estrema 15m | €10.032,32 | €32,32 | 11 | 11 | 54,55% | 1,85 | €2,94 | 0,36% |
| TEST | 1H Fast V3 Nohigh Range Only V1 | Momentum / breakout V3 Filtered | €10.023,56 | €113,43 | 97 | 97 | 43,30% | 1,05 | €1,17 | 7,07% |
| TEST | Scalp RSI Short 85 · €50 · 15x | Inversione RSI estrema 15m | €10.022,70 | €22,70 | 6 | 6 | 66,67% | 1,87 | €3,78 | 0,31% |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | Momentum / breakout V3 Filtered | €10.020,28 | €20,93 | 180 | 180 | 43,89% | 1,01 | €0,12 | 6,64% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €10.014,08 | €14,08 | 30 | 30 | 43,33% | 1,10 | €0,47 | 0,33% |
| TEST | Scalp RSI Short 80 · €50 · 15x | Inversione RSI estrema 15m | €10.009,44 | €9,44 | 17 | 17 | 41,18% | 1,17 | €0,56 | 0,53% |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | Momentum / breakout V3 Filtered | €10.008,92 | €8,92 | 30 | 30 | 36,67% | 1,02 | €0,30 | 4,84% |
| TEST | Sol Ema 4H | Trend following EMA | €10.005,51 | €5,51 | 11 | 11 | 36,36% | 1,02 | €0,50 | 2,27% |
| TEST | Scalp RSI Short 85 · €10 · 15x | Inversione RSI estrema 15m | €10.004,54 | €4,54 | 6 | 6 | 66,67% | 1,87 | €0,76 | 0,06% |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | Momentum / breakout V3 Filtered | €10.003,37 | €3,37 | 8 | 8 | 37,50% | 1,02 | €0,42 | 2,15% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €10.002,82 | €2,82 | 30 | 30 | 43,33% | 1,10 | €0,09 | 0,07% |
| TEST | 1H Balanced Short Trend Down Strict V1 | Confluenza trend | €10.002,17 | €2,17 | 15 | 15 | 40,00% | 1,01 | €0,14 | 1,80% |
| TEST | Scalp RSI Short 80 · €10 · 15x | Inversione RSI estrema 15m | €10.001,89 | €1,89 | 17 | 17 | 41,18% | 1,17 | €0,11 | 0,11% |
| TEST | Scanner Bottom5 Short Continuation V1 | Scanner Bottom5 Short Continuation | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 20 · €10 · 15x | Inversione RSI estrema 15m | €9.998,68 | €-1,32 | 11 | 11 | 36,36% | 0,74 | €-0,12 | 0,04% |
| TEST | Scalp RSI Short 85 · prudente · 5x | Inversione RSI estrema 15m | €9.996,83 | €-3,17 | 6 | 6 | 66,67% | 0,86 | €-0,53 | 0,30% |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | Momentum / breakout V3 Filtered | €9.995,23 | €-4,77 | 15 | 15 | 46,67% | 0,99 | €-0,32 | 2,70% |
| TEST | Scalp RSI Long 15 · €10 · 15x | Inversione RSI estrema 15m | €9.994,07 | €-5,93 | 4 | 4 | 25,00% | 0,06 | €-1,48 | 0,06% |
| TEST | Scalp RSI Long 20 · €50 · 15x | Inversione RSI estrema 15m | €9.993,42 | €-6,58 | 11 | 11 | 36,36% | 0,74 | €-0,60 | 0,21% |
| TEST | Scalp RSI Long 25 · €10 · 15x | Inversione RSI estrema 15m | €9.988,91 | €-11,09 | 20 | 20 | 40,00% | 0,37 | €-0,55 | 0,15% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €9.980,98 | €-19,02 | 5 | 5 | 40,00% | 0,88 | €-3,80 | 1,96% |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | €9.970,37 | €-29,63 | 4 | 4 | 25,00% | 0,06 | €-7,41 | 0,30% |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | €9.970,34 | €-29,66 | 4 | 4 | 25,00% | 0,13 | €-7,42 | 0,30% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €9.964,84 | €-35,16 | 4 | 4 | 25,00% | 0,77 | €-8,79 | 1,10% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €9.964,27 | €-35,73 | 20 | 20 | 35,00% | 0,65 | €-1,79 | 0,71% |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | €9.944,53 | €-55,47 | 20 | 20 | 40,00% | 0,37 | €-2,77 | 0,77% |
| TEST | Sol Ema 1H | Trend following EMA | €9.942,44 | €-57,56 | 27 | 27 | 40,74% | 0,93 | €-2,13 | 3,33% |
| TEST | 1H Fast V3 No Esports Long Only V1 | Momentum / breakout V3 Filtered | €9.941,16 | €-57,91 | 262 | 262 | 41,98% | 0,99 | €-0,22 | 10,60% |
| TEST | Scalp RSI Short 80 · prudente · 5x | Inversione RSI estrema 15m | €9.939,55 | €-60,45 | 17 | 17 | 35,29% | 0,39 | €-3,56 | 0,89% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €9.939,44 | €-60,56 | 27 | 27 | 44,44% | 0,92 | €-2,24 | 4,59% |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | Combo Adaptive | €9.935,18 | €-64,82 | 58 | 58 | 50,00% | 0,95 | €-1,12 | 4,27% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €9.925,44 | €-74,56 | 16 | 16 | 56,25% | 0,82 | €-4,66 | 1,89% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.917,05 | €-82,95 | 30 | 30 | 43,33% | 0,52 | €-2,77 | 0,84% |
| TEST | Btc Ema 4H | Trend following EMA | €9.914,14 | €-85,86 | 5 | 5 | 20,00% | 0,58 | €-17,17 | 1,76% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €9.899,28 | €-100,72 | 15 | 15 | 46,67% | 0,74 | €-6,71 | 1,98% |
| TEST | Combo Adaptive Side Regime Guard V1 | Combo Adaptive | €9.889,77 | €-105,91 | 170 | 170 | 42,94% | 0,97 | €-0,62 | 11,68% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €9.888,02 | €-111,98 | 12 | 12 | 41,67% | 0,66 | €-9,33 | 2,03% |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | Momentum / breakout V3 Filtered | €9.864,62 | €-134,74 | 179 | 179 | 46,37% | 0,97 | €-0,75 | 8,44% |
| TEST | Scanner Top5 Btc Tp3 V1 | Scanner Top 5 + forza BTC | €9.860,83 | €-115,03 | 159 | 159 | 41,51% | 0,97 | €-0,72 | 11,78% |
| TEST | Scanner Top5 Btc Runner25 V1 | Scanner Top 5 + forza BTC | €9.855,06 | €-120,81 | 163 | 163 | 41,72% | 0,97 | €-0,74 | 12,06% |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | Momentum / breakout V3 Filtered | €9.837,38 | €-162,62 | 37 | 37 | 40,54% | 0,76 | €-4,40 | 3,08% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €9.834,39 | €-163,55 | 145 | 138 | 40,00% | 0,95 | €-1,13 | 10,88% |
| TEST | Eth Ema 4H | Trend following EMA | €9.822,24 | €-165,26 | 8 | 8 | 25,00% | 0,47 | €-20,66 | 1,98% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | Momentum / breakout V3 Filtered | €9.817,34 | €-182,66 | 24 | 24 | 41,67% | 0,64 | €-7,61 | 3,23% |
| TEST | Combo Adaptive Quality7 Regime V1 | Combo Adaptive | €9.810,21 | €-189,79 | 58 | 58 | 46,55% | 0,86 | €-3,27 | 5,41% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €9.808,89 | €-191,11 | 7 | 7 | 14,29% | 0,41 | €-27,30 | 2,43% |
| TEST | 1H Fast V3 Nohigh V1 | Momentum / breakout V3 Filtered | €9.805,15 | €-134,18 | 189 | 188 | 44,44% | 0,96 | €-0,71 | 7,10% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €9.800,08 | €-199,92 | 11 | 11 | 45,45% | 0,54 | €-18,17 | 4,16% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | Momentum / breakout V3 Filtered | €9.762,18 | €-237,82 | 7 | 7 | 14,29% | 0,02 | €-33,97 | 2,82% |
| TEST | 1H Fast Nohigh Cap75 V1 | Momentum / breakout | €9.759,15 | €-279,81 | 206 | 206 | 40,78% | 0,93 | €-1,36 | 10,86% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | Momentum / breakout V3 Filtered | €9.723,72 | €-276,28 | 31 | 31 | 32,26% | 0,62 | €-8,91 | 4,83% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.711,69 | €-288,31 | 18 | 18 | 38,89% | 0,57 | €-16,02 | 3,26% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.689,84 | €-298,29 | 22 | 22 | 36,36% | 0,54 | €-13,56 | 3,93% |
| TEST | 1H Fast V3 Long Only V1 | Momentum / breakout V3 Filtered | €9.680,11 | €-318,34 | 266 | 266 | 41,35% | 0,94 | €-1,20 | 12,52% |
| TEST | Scanner Top5 Btc Guard V1 | Scanner Top 5 + forza BTC | €9.674,83 | €-323,56 | 150 | 150 | 37,33% | 0,90 | €-2,16 | 7,34% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.638,99 | €-361,01 | 21 | 21 | 33,33% | 0,53 | €-17,19 | 3,83% |
| TEST | 1H Balanced Long No Rhv V1 | Confluenza trend | €9.633,54 | €-363,25 | 132 | 132 | 43,18% | 0,84 | €-2,75 | 9,26% |
| TEST | Scanner Top5 Btc Mfe V1 | Scanner Top 5 + forza BTC | €9.613,06 | €-382,21 | 148 | 148 | 43,92% | 0,86 | €-2,58 | 12,28% |
| TEST | 1H Fast V3 No Esports V1 | Momentum / breakout V3 Filtered | €9.596,58 | €-447,32 | 237 | 237 | 42,19% | 0,91 | €-1,89 | 10,92% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.594,42 | €-384,92 | 22 | 22 | 36,36% | 0,50 | €-17,50 | 4,11% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | Momentum / breakout V3 Filtered | €9.579,83 | €-420,17 | 11 | 11 | 0,00% | 0,00 | €-38,20 | 4,20% |
| TEST | Eth Ema 1H | Trend following EMA | €9.547,07 | €-434,90 | 30 | 30 | 36,67% | 0,57 | €-14,50 | 4,80% |
| TEST | Combo Adaptive Regime V1 | Combo Adaptive | €9.538,51 | €-460,31 | 90 | 90 | 45,56% | 0,79 | €-5,11 | 6,28% |
| TEST | Master Adaptive Gb20 Be V1 | Master Adaptive Consensus | €9.517,70 | €-482,47 | 111 | 111 | 30,63% | 0,83 | €-4,35 | 8,39% |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | Momentum / breakout | €9.516,08 | €-521,91 | 169 | 169 | 39,05% | 0,84 | €-3,09 | 10,86% |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | Momentum / breakout | €9.515,12 | €-422,66 | 178 | 178 | 44,38% | 0,91 | €-2,37 | 15,94% |
| TEST | Combo Adaptive Quality7 V1 | Combo Adaptive | €9.512,30 | €-486,49 | 99 | 99 | 38,38% | 0,80 | €-4,91 | 8,88% |
| TEST | Master Adaptive Gb20 Partial V1 | Master Adaptive Consensus | €9.507,58 | €-492,59 | 106 | 106 | 33,02% | 0,82 | €-4,65 | 7,98% |
| TEST | 1H Fast Score 6 75 V1 | Momentum / breakout | €9.477,84 | €-460,73 | 217 | 217 | 42,40% | 0,92 | €-2,12 | 15,64% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €9.475,88 | €-518,39 | 96 | 96 | 31,25% | 0,81 | €-5,40 | 8,44% |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | €9.470,81 | €-529,36 | 108 | 108 | 32,41% | 0,82 | €-4,90 | 7,80% |
| TEST | Scanner Top5 Btc Guard Mfe V1 | Scanner Top 5 + forza BTC | €9.449,84 | €-548,59 | 167 | 167 | 38,32% | 0,84 | €-3,28 | 8,78% |
| TEST | Btc Ema 1H | Trend following EMA | €9.428,75 | €-567,26 | 24 | 24 | 25,00% | 0,37 | €-23,64 | 5,90% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €9.369,38 | €-629,86 | 91 | 91 | 34,07% | 0,73 | €-6,92 | 7,96% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €9.350,73 | €-594,52 | 211 | 211 | 41,23% | 0,86 | €-2,82 | 14,04% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €9.345,84 | €-654,32 | 142 | 142 | 42,25% | 0,79 | €-4,61 | 9,02% |
| TEST | Scanner Bottom10 Short | Scanner Bottom10 Short | €9.320,74 | €-677,79 | 70 | 70 | 31,43% | 0,65 | €-9,68 | 9,06% |
| TEST | Scanner Bottom15 Short | Scanner Bottom15 Short | €9.320,74 | €-677,79 | 70 | 70 | 31,43% | 0,65 | €-9,68 | 9,06% |
| TEST | Scanner Bottom20 Short | Scanner Bottom20 Short | €9.320,74 | €-677,79 | 70 | 70 | 31,43% | 0,65 | €-9,68 | 9,06% |
| TEST | Master Adaptive Gb20 Loss Cap V1 | Master Adaptive Consensus | €9.317,20 | €-675,25 | 105 | 105 | 25,71% | 0,77 | €-6,43 | 11,41% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €9.309,30 | €-687,93 | 175 | 161 | 43,43% | 0,81 | €-3,93 | 11,82% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €9.277,66 | €-714,20 | 110 | 110 | 33,64% | 0,78 | €-6,49 | 10,13% |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | Scanner Bottom 5 Short | €9.256,15 | €-742,38 | 61 | 61 | 31,15% | 0,58 | €-12,17 | 9,08% |
| TEST | Scanner Bottom5 Short Profit Lock V1 | Scanner Bottom 5 Short | €9.242,07 | €-756,47 | 62 | 62 | 30,65% | 0,56 | €-12,20 | 9,08% |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | Momentum / breakout | €9.214,28 | €-785,35 | 146 | 146 | 38,36% | 0,78 | €-5,38 | 9,99% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.172,75 | €-811,71 | 158 | 158 | 39,24% | 0,71 | €-5,14 | 12,31% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.170,95 | €-827,60 | 89 | 89 | 31,46% | 0,64 | €-9,30 | 10,17% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €9.134,06 | €-866,26 | 181 | 181 | 38,12% | 0,75 | €-4,79 | 15,68% |
| TEST | Combo Adaptive Runner25 V1 | Combo Adaptive | €9.108,17 | €-886,34 | 154 | 154 | 35,71% | 0,69 | €-5,76 | 14,10% |
| TEST | Combo Adaptive Mfe Trail | Combo Adaptive | €9.035,37 | €-963,32 | 227 | 227 | 41,41% | 0,76 | €-4,24 | 15,45% |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | Scanner Top 5 + forza BTC | €9.023,63 | €-954,87 | 116 | 116 | 37,07% | 0,70 | €-8,23 | 12,02% |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | Scanner Top 5 + forza BTC | €8.983,79 | €-1.011,42 | 54 | 54 | 25,93% | 0,42 | €-18,73 | 12,23% |
| TEST | Combo Trend | Combo Trend | €8.972,54 | €-921,72 | 192 | 192 | 39,58% | 0,78 | €-4,80 | 14,08% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €8.948,64 | €-1.050,04 | 82 | 82 | 28,05% | 0,65 | €-12,81 | 13,60% |
| TEST | Combo Adaptive Tp3 V1 | Combo Adaptive | €8.937,78 | €-1.056,83 | 134 | 134 | 35,07% | 0,59 | €-7,89 | 14,10% |
| TEST | 1H Balanced V3 Long Only V1 | Confluenza trend V3 Filtered | €8.844,27 | €-1.104,13 | 165 | 165 | 41,21% | 0,65 | €-6,69 | 13,79% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €8.756,35 | €-1.283,39 | 67 | 67 | 35,82% | 0,49 | €-19,16 | 16,01% |
| TEST | 1H Fast V3 Cap75 V1 | Momentum / breakout V3 Filtered | €8.704,67 | €-1.246,89 | 228 | 228 | 38,60% | 0,77 | €-5,47 | 17,89% |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | Scanner Top 5 + forza BTC | €8.675,89 | €-1.305,36 | 143 | 143 | 37,06% | 0,65 | €-9,13 | 13,91% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €8.476,84 | €-1.551,70 | 167 | 167 | 33,53% | 0,57 | €-9,29 | 19,11% |
| TEST | Scanner Top5 Btc Btc Le3 V1 | Scanner Top 5 + forza BTC | €8.375,72 | €-1.602,12 | 119 | 119 | 33,61% | 0,50 | €-13,46 | 18,08% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €8.353,29 | €-1.645,91 | 127 | 127 | 40,94% | 0,58 | €-12,96 | 19,96% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | SPCX | LONG | Confluenza trend | 240m | 3,0x | 136,56189 | 136,56189 | 128,79610 | 91,72407 | 152,09346 | €285,50 | €856,50 | €48,71 | €0,00 |
| Principale 4H | VELVET | LONG | Confluenza trend | 240m | 3,0x | 0,55987 | 0,55987 | 0,49269 | 0,37605 | 0,69424 | €131,08 | €393,24 | €47,19 | €0,00 |
| Principale 4H | EDEN | LONG | Confluenza trend | 240m | 3,0x | 0,06195 | 0,06195 | 0,05451 | 0,04161 | 0,07681 | €130,34 | €391,02 | €46,92 | €0,00 |
| Principale 4H | TRUMP | LONG | Confluenza trend | 240m | 3,0x | 2,46049 | 2,46049 | 2,16523 | 1,65263 | 3,05101 | €134,98 | €404,95 | €48,59 | €0,00 |
| Principale 4H | UNI | LONG | Confluenza trend | 240m | 3,0x | 6,93739 | 6,36600 | 6,33086 | 4,65961 | 8,15044 | €18,73 | €56,20 | €4,91 | €-4,63 |
| Bilanciata 1H V1 | BTR | SHORT | Confluenza trend | 60m | 3,0x | 0,05109 | 0,05109 | 0,05109 | 0,06786 | 0,03883 | €125,78 | €377,33 | €0,00 | €-0,00 |
| Bilanciata 1H V1 | ARB | LONG | Confluenza trend | 60m | 3,0x | 0,13283 | 0,13283 | 0,12480 | 0,08922 | 0,14889 | €256,10 | €768,31 | €46,46 | €0,00 |
| Bilanciata 1H V1 | PEPE | SHORT | Confluenza trend | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €18,46 | €55,39 | €1,83 | €1,31 |
| 1H Balanced Long No Rhv V1 | SKHYNIX | LONG | Confluenza trend | 60m | 3,0x | 1214,11277 | 1214,11277 | 1170,18211 | 815,47908 | 1301,97411 | €413,43 | €1.240,28 | €44,88 | €0,00 |
| 1H Balanced Long No Rhv V1 | BOME | LONG | Confluenza trend | 60m | 3,0x | 0,00129 | 0,00129 | 0,00114 | 0,00087 | 0,00160 | €134,98 | €404,95 | €48,59 | €0,00 |
| 1H Balanced Long No Rhv V1 | TAO | LONG | Confluenza trend | 60m | 3,0x | 247,38947 | 247,38947 | 237,94346 | 166,16326 | 266,28148 | €428,20 | €1.284,61 | €49,05 | €0,00 |
| 1H Balanced Long No Rhv V1 | HEMI | LONG | Confluenza trend | 60m | 3,0x | 0,01177 | 0,01177 | 0,01036 | 0,00790 | 0,01459 | €131,93 | €395,78 | €47,49 | €0,00 |
| 1H Balanced Long No Rhv V1 | ETH | LONG | Confluenza trend | 60m | 3,0x | 2534,63683 | 2520,83000 | 2498,13806 | 1702,43107 | 2607,63437 | €62,02 | €186,05 | €2,68 | €-1,01 |
| Bilanciata 1H V2 | SKHYNIX | LONG | Confluenza trend V2 | 60m | 3,0x | 1214,11277 | 1214,11277 | 1170,18211 | 815,47908 | 1301,97411 | €422,38 | €1.267,15 | €45,85 | €0,00 |
| Bilanciata 1H V2 | BTR | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,05545 | 0,05545 | 0,05545 | 0,07365 | 0,04214 | €126,95 | €380,86 | €0,00 | €-0,00 |
| Bilanciata 1H V2 | ARB | LONG | Confluenza trend V2 | 60m | 3,0x | 0,13495 | 0,13495 | 0,12685 | 0,09064 | 0,15116 | €19,71 | €59,12 | €3,55 | €0,00 |
| Bilanciata 1H V2 | SOPH | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,00528 | 0,00528 | 0,00591 | 0,00701 | 0,00401 | €129,45 | €388,36 | €46,60 | €-0,00 |
| Bilanciata 1H V2 | ENA | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,14148 | 0,14148 | 0,14759 | 0,18793 | 0,12926 | €343,49 | €1.030,46 | €44,49 | €-0,00 |
| Bilanciata 1H V3 Filtered | SKHYNIX | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1220,85412 | 1220,85412 | 1177,63561 | 820,00702 | 1307,29117 | €460,42 | €1.381,27 | €48,90 | €0,00 |
| Bilanciata 1H V3 Filtered | ADA | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,20138 | 0,20726 | 0,20719 | 0,26750 | 0,18976 | €559,88 | €1.679,63 | €48,45 | €-49,05 |
| Bilanciata 1H V3 Filtered | ARB | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,13283 | 0,13283 | 0,12480 | 0,08922 | 0,14889 | €262,61 | €787,82 | €47,64 | €0,00 |
| Bilanciata 1H V3 Filtered | UNI | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 7,14143 | 6,36600 | 6,87560 | 4,79666 | 7,67309 | €9,58 | €28,74 | €1,07 | €-3,12 |
| Bilanciata 1H V3 Filtered | SOPH | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,00528 | 0,00528 | 0,00591 | 0,00701 | 0,00401 | €109,03 | €327,10 | €39,25 | €-0,00 |
| Bilanciata 1H V3 Filtered | ETH | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 2544,14873 | 2520,83000 | 2482,39288 | 1708,81990 | 2667,66041 | €8,53 | €25,60 | €0,62 | €-0,23 |
| Bilanciata 1H V3 Filtered | SUI | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,73075 | 0,73075 | 0,75468 | 0,97068 | 0,68290 | €12,28 | €36,85 | €1,21 | €-0,00 |
| 1H Fast Score 6 75 V1 | BTR | SHORT | Momentum / breakout | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €126,75 | €380,26 | €0,00 | €-0,00 |
| 1H Fast Score 6 75 V1 | ARB | LONG | Momentum / breakout | 60m | 3,0x | 0,13189 | 0,13189 | 0,12574 | 0,08858 | 0,14110 | €21,85 | €65,56 | €3,05 | €0,00 |
| 1H Fast Score 6 75 V1 | SOPH | SHORT | Momentum / breakout | 60m | 3,0x | 0,00528 | 0,00528 | 0,00591 | 0,00701 | 0,00433 | €134,54 | €403,62 | €48,43 | €-0,00 |
| 1H Fast Score 6 75 V1 | ZEC | SHORT | Momentum / breakout | 60m | 3,0x | 1121,89558 | 1144,70000 | 1145,76963 | 1490,25129 | 1086,08450 | €747,08 | €2.241,24 | €47,69 | €-45,56 |
| 1H Fast Score 6 75 V1 | ADA | SHORT | Momentum / breakout | 60m | 3,0x | 0,20667 | 0,20726 | 0,20898 | 0,27452 | 0,20319 | €1.365,77 | €4.097,31 | €45,89 | €-11,78 |
| 1H Fast Score 6 75 No Trend Up V1 | BTR | SHORT | Momentum / breakout | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €123,38 | €370,15 | €0,00 | €-0,00 |
| 1H Fast Score 6 75 No Trend Up V1 | ARB | LONG | Momentum / breakout | 60m | 3,0x | 0,13189 | 0,13189 | 0,12574 | 0,08858 | 0,14110 | €21,27 | €63,82 | €2,97 | €0,00 |
| 1H Fast Score 6 75 No Trend Up V1 | SOPH | SHORT | Momentum / breakout | 60m | 3,0x | 0,00528 | 0,00528 | 0,00591 | 0,00701 | 0,00433 | €134,17 | €402,52 | €48,30 | €-0,00 |
| 1H Fast Score 6 75 No Trend Up V1 | ZEC | SHORT | Momentum / breakout | 60m | 3,0x | 1121,89558 | 1144,70000 | 1145,76963 | 1490,25129 | 1086,08450 | €750,06 | €2.250,19 | €47,88 | €-45,74 |
| 1H Fast Score 6 75 No Trend Up V1 | ADA | SHORT | Momentum / breakout | 60m | 3,0x | 0,20667 | 0,20726 | 0,20898 | 0,27452 | 0,20319 | €1.424,59 | €4.273,77 | €47,87 | €-12,29 |
| 1H Fast Score 6 75 Range Only V1 | ADA | SHORT | Momentum / breakout | 60m | 3,0x | 0,20260 | 0,20726 | 0,20707 | 0,26912 | 0,19589 | €765,21 | €2.295,64 | €50,71 | €-52,82 |
| 1H Fast Score 6 75 Range Only V1 | HEMI | LONG | Momentum / breakout | 60m | 3,0x | 0,01177 | 0,01177 | 0,01065 | 0,00790 | 0,01345 | €178,53 | €535,59 | €51,05 | €0,00 |
| 1H Fast Score 6 75 Range Only V1 | BTR | SHORT | Momentum / breakout | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €131,87 | €395,61 | €0,00 | €-0,00 |
| 1H Fast Score 6 75 Range Only V1 | SOPH | SHORT | Momentum / breakout | 60m | 3,0x | 0,00528 | 0,00528 | 0,00591 | 0,00701 | 0,00433 | €138,52 | €415,55 | €49,87 | €-0,00 |
| 1H Fast Score 6 75 Range Only V1 | ZEC | SHORT | Momentum / breakout | 60m | 3,0x | 1121,89558 | 1144,70000 | 1145,76963 | 1490,25129 | 1086,08450 | €49,30 | €147,91 | €3,15 | €-3,01 |
| 1H Fast Score 6 75 Cost Aware V1 | BTW | LONG | Momentum / breakout | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €8,91 | €26,72 | €3,13 | €0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00086 | 0,00146 | €215,92 | €647,76 | €57,03 | €0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | NEAR | LONG | Momentum / breakout | 60m | 3,0x | 2,08142 | 2,08142 | 2,02315 | 1,39802 | 2,16882 | €42,86 | €128,59 | €3,60 | €0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €157,13 | €471,39 | €56,57 | €-0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | BTR | SHORT | Momentum / breakout | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €150,22 | €450,66 | €0,00 | €-0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | SOPH | SHORT | Momentum / breakout | 60m | 3,0x | 0,00528 | 0,00528 | 0,00591 | 0,00701 | 0,00433 | €126,49 | €379,47 | €45,54 | €-0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | SUI | SHORT | Momentum / breakout | 60m | 3,0x | 0,72256 | 0,72256 | 0,74037 | 0,95979 | 0,69583 | €10,60 | €31,79 | €0,78 | €-0,00 |
| 1H Fast Nohigh Cap75 V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €139,29 | €417,86 | €50,14 | €-0,00 |
| 1H Fast Nohigh Cap75 V1 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €141,57 | €424,71 | €50,14 | €-0,00 |
| 1H Fast Nohigh Cap75 V1 | BTR | SHORT | Momentum / breakout | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €135,62 | €406,85 | €0,00 | €-0,00 |
| 1H Fast Nohigh Cap75 V1 | PEPE | SHORT | Momentum / breakout | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €588,23 | €1.764,70 | €45,30 | €41,75 |
| 1H Fast Nohigh Cap75 V1 | ZEC | SHORT | Momentum / breakout | 60m | 3,0x | 1126,41467 | 1144,70000 | 1150,15748 | 1496,25416 | 1090,80047 | €19,36 | €58,09 | €1,22 | €-0,94 |
| 1H Fast Long Btc 1 3 Cap75 V1 | PROM | LONG | Momentum / breakout | 60m | 3,0x | 6,93686 | 6,93686 | 6,39299 | 4,65926 | 7,75266 | €205,67 | €617,01 | €48,38 | €0,00 |
| 1H Fast No Pepe V1 | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €172,22 | €516,67 | €49,86 | €0,00 |
| 1H Fast No Pepe V1 | TAO | LONG | Momentum / breakout | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €47,93 | €143,78 | €4,27 | €0,00 |
| 1H Fast No Pepe V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €136,27 | €408,80 | €49,06 | €-0,00 |
| 1H Fast No Pepe V1 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €9,48 | €28,43 | €3,41 | €-0,00 |
| 1H Fast No Pepe V1 | ADA | SHORT | Momentum / breakout | 60m | 3,0x | 0,20138 | 0,20726 | 0,20590 | 0,26750 | 0,19460 | €739,08 | €2.217,23 | €49,74 | €-64,75 |
| 1H Fast No Pepe V1 | 0G | LONG | Momentum / breakout | 60m | 3,0x | 0,23904 | 0,23904 | 0,21901 | 0,16056 | 0,26909 | €210,41 | €631,23 | €52,89 | €0,00 |
| 1H Fast No Pepe V1 | SUI | SHORT | Momentum / breakout | 60m | 3,0x | 0,72256 | 0,72256 | 0,74134 | 0,95979 | 0,69438 | €10,84 | €32,53 | €0,85 | €-0,00 |
| 1H Fast Tp2 V1 | BTW | LONG | Momentum / breakout | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,56752 | €142,85 | €428,56 | €50,25 | €0,00 |
| 1H Fast Tp2 V1 | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00132 | 0,00132 | 0,00119 | 0,00088 | 0,00158 | €18,87 | €56,62 | €5,59 | €0,00 |
| 1H Fast Tp2 V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,17246 | 0,17246 | 0,17246 | 0,22908 | 0,13107 | €139,71 | €419,14 | €0,00 | €-0,00 |
| 1H Fast Tp2 V1 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03379 | €141,13 | €423,40 | €50,81 | €-0,00 |
| 1H Fast Tp2 V1 | 4 | LONG | Momentum / breakout | 60m | 3,0x | 0,03351 | 0,03351 | 0,03024 | 0,02251 | 0,04003 | €142,67 | €428,01 | €41,68 | €0,00 |
| 1H Fast Tp2 V1 | ENA | SHORT | Momentum / breakout | 60m | 3,0x | 0,13916 | 0,13916 | 0,14448 | 0,18485 | 0,12852 | €19,37 | €58,12 | €2,22 | €-0,00 |
| Rapida 1H V2 | ADA | SHORT | Momentum / breakout V2 | 60m | 3,0x | 0,20283 | 0,20726 | 0,20750 | 0,26943 | 0,19582 | €749,31 | €2.247,94 | €51,80 | €-49,10 |
| Rapida 1H V2 | PEPE | LONG | Momentum / breakout V2 | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.429,85 | €4.289,54 | €52,04 | €16,02 |
| Rapida 1H V3 Filtered | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €172,00 | €515,99 | €49,79 | €0,00 |
| Rapida 1H V3 Filtered | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €589,98 | €1.769,95 | €52,56 | €0,00 |
| Rapida 1H V3 Filtered | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €140,02 | €420,06 | €50,41 | €-0,00 |
| Rapida 1H V3 Filtered | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €16,99 | €50,96 | €6,11 | €-0,00 |
| Rapida 1H V3 Filtered | PEPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €633,48 | €1.900,43 | €47,75 | €49,10 |
| Rapida 1H V3 Filtered | ENA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,13916 | 0,13916 | 0,14448 | 0,18485 | 0,13118 | €23,75 | €71,25 | €2,72 | €-0,00 |
| 1H Fast V3 Cap75 V1 | BTR | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €122,50 | €367,49 | €0,00 | €-0,00 |
| 1H Fast V3 Cap75 V1 | SOPH | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00528 | 0,00528 | 0,00591 | 0,00701 | 0,00433 | €123,86 | €371,59 | €44,59 | €-0,00 |
| 1H Fast V3 Cap75 V1 | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 1126,41467 | 1144,70000 | 1150,15748 | 1496,25416 | 1090,80047 | €692,08 | €2.076,23 | €43,76 | €-33,70 |
| 1H Fast V3 Cap75 V1 | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,20667 | 0,20726 | 0,20898 | 0,27452 | 0,20319 | €1.270,85 | €3.812,56 | €42,70 | €-10,96 |
| 1H Fast V3 Nohigh V1 | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €131,05 | €393,14 | €47,18 | €-0,00 |
| 1H Fast V3 Nohigh V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €133,20 | €399,59 | €47,18 | €-0,00 |
| 1H Fast V3 Nohigh V1 | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,20138 | 0,20726 | 0,20590 | 0,26750 | 0,19460 | €719,57 | €2.158,72 | €48,43 | €-63,04 |
| 1H Fast V3 Nohigh V1 | 0G | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,23904 | 0,23904 | 0,21901 | 0,16056 | 0,26909 | €196,32 | €588,95 | €49,35 | €0,00 |
| 1H Fast V3 Long Only V1 | BTW | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €126,57 | €379,72 | €44,52 | €0,00 |
| 1H Fast V3 Long Only V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00147 | €9,56 | €28,69 | €2,66 | €0,00 |
| 1H Fast V3 Long Only V1 | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €554,42 | €1.663,26 | €49,39 | €0,00 |
| 1H Fast V3 Long Only V1 | HEMI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01177 | 0,01177 | 0,01065 | 0,00790 | 0,01345 | €170,60 | €511,79 | €48,79 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 V1 | HEMI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01177 | 0,01177 | 0,01065 | 0,00790 | 0,01345 | €166,97 | €500,92 | €47,75 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 V1 | PROM | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 6,92735 | 6,92735 | 6,35093 | 4,65287 | 7,79198 | €195,87 | €587,60 | €48,89 | €0,00 |
| 1H Fast V3 No Esports V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €169,36 | €508,09 | €49,03 | €0,00 |
| 1H Fast V3 No Esports V1 | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €27,04 | €81,13 | €2,41 | €0,00 |
| 1H Fast V3 No Esports V1 | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €133,96 | €401,88 | €48,23 | €-0,00 |
| 1H Fast V3 No Esports V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €129,73 | €389,20 | €46,70 | €-0,00 |
| 1H Fast V3 No Esports V1 | PEPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €593,05 | €1.779,15 | €44,70 | €45,96 |
| 1H Fast V3 No Esports V1 | ENA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,13916 | 0,13916 | 0,14448 | 0,18485 | 0,13118 | €22,41 | €67,23 | €2,57 | €-0,00 |
| 1H Fast V3 No Esports Long Only V1 | BTW | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €132,94 | €398,81 | €46,76 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00147 | €10,06 | €30,18 | €2,80 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | HEMI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01177 | 0,01177 | 0,01065 | 0,00790 | 0,01345 | €175,30 | €525,91 | €50,13 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | PROM | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 6,92735 | 6,92735 | 6,35093 | 4,65287 | 7,79198 | €9,71 | €29,12 | €2,42 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | 0G | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,23904 | 0,23904 | 0,21901 | 0,16056 | 0,26909 | €187,89 | €563,68 | €47,23 | €0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €173,11 | €519,32 | €50,11 | €0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €593,79 | €1.781,38 | €52,90 | €0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €140,93 | €422,78 | €50,73 | €-0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €17,09 | €51,28 | €6,15 | €-0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | PEPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €637,57 | €1.912,72 | €48,06 | €49,41 |
| 1H Fast V3 No Esports Mfe Lock V1 | ENA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,13916 | 0,13916 | 0,14448 | 0,18485 | 0,13118 | €23,90 | €71,71 | €2,74 | €-0,00 |
| 1H Fast V3 No Esports Stress Guard V1 | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,20283 | 0,20726 | 0,20750 | 0,26943 | 0,19582 | €739,04 | €2.217,11 | €51,09 | €-48,43 |
| 1H Fast V3 No Esports Stress Guard V1 | PUMP | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00383 | 0,00383 | 0,00398 | 0,00508 | 0,00359 | €11,48 | €34,44 | €1,41 | €-0,00 |
| 1H Fast V3 No Esports Stress Guard V1 | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 1126,41467 | 1144,70000 | 1150,15748 | 1496,25416 | 1090,80047 | €832,19 | €2.496,56 | €52,62 | €-40,53 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | HEMI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01177 | 0,01177 | 0,01065 | 0,00790 | 0,01345 | €163,25 | €489,75 | €46,69 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | PROM | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 6,92735 | 6,92735 | 6,35093 | 4,65287 | 7,79198 | €191,37 | €574,11 | €47,77 | €0,00 |
| Ampia 4H | SPCX | LONG | Confluenza trend | 240m | 2,0x | 136,56189 | 136,56189 | 126,46637 | 68,96375 | 164,82935 | €323,86 | €647,73 | €47,88 | €0,00 |
| Ampia 4H | VELVET | LONG | Confluenza trend | 240m | 2,0x | 0,55987 | 0,55987 | 0,49269 | 0,28274 | 0,74799 | €201,63 | €403,26 | €48,39 | €0,00 |
| Ampia 4H | LINK | LONG | Confluenza trend | 240m | 2,0x | 11,96839 | 11,96839 | 11,08055 | 6,04404 | 14,45436 | €14,07 | €28,15 | €2,09 | €0,00 |
| Ampia 4H | TRUMP | LONG | Confluenza trend | 240m | 2,0x | 2,37347 | 2,37347 | 2,08866 | 1,19860 | 3,17096 | €210,83 | €421,66 | €50,60 | €0,00 |
| Ampia 4H | SOL | LONG | Confluenza trend | 240m | 2,0x | 103,77875 | 101,74400 | 96,79200 | 52,40827 | 123,34165 | €13,62 | €27,23 | €1,83 | €-0,53 |
| Ampia 4H | UNI | LONG | Confluenza trend | 240m | 2,0x | 6,98040 | 6,36600 | 6,22147 | 3,52510 | 9,10539 | €214,19 | €428,38 | €46,57 | €-37,70 |
| Ampia 4H | SUI | SHORT | Confluenza trend | 240m | 2,0x | 0,72745 | 0,72745 | 0,78235 | 1,08754 | 0,57376 | €23,11 | €46,21 | €3,49 | €-0,00 |
| Ampia 4H | ETH | LONG | Confluenza trend | 240m | 2,0x | 2525,71504 | 2520,83000 | 2434,21611 | 1275,48610 | 2781,91203 | €41,29 | €82,58 | €2,99 | €-0,16 |
| Forza relativa 1H V1 | BTR | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,05109 | 0,05109 | 0,05109 | 0,07638 | 0,03760 | €174,72 | €349,43 | €0,00 | €-0,00 |
| Forza relativa 1H V1 | ARB | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,15050 | €352,71 | €705,43 | €42,65 | €0,00 |
| Forza relativa 1H V1 | PEPE | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00001 | 0,00000 | €661,53 | €1.323,06 | €41,35 | €33,93 |
| Forza relativa 1H V1 | UNI | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 7,16543 | 6,36600 | 6,92567 | 3,61854 | 7,69291 | €13,42 | €26,84 | €0,90 | €-2,99 |
| Forza relativa 1H V1 | ENA | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,14025 | 0,14025 | 0,14705 | 0,20968 | 0,12529 | €14,26 | €28,51 | €1,38 | €-0,00 |
| Forza relativa 1H V1 | SUI | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,72256 | 0,72256 | 0,74546 | 1,08022 | 0,67216 | €672,88 | €1.345,76 | €42,66 | €-0,00 |
| Forza relativa 1H V2 | BEAT | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,25984 | 0,25984 | 0,25657 | 0,38847 | 0,19125 | €200,38 | €400,75 | €0,00 | €-0,00 |
| Forza relativa 1H V2 | TUT | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,04452 | 0,04452 | 0,04986 | 0,06656 | 0,03277 | €204,64 | €409,28 | €49,11 | €-0,00 |
| Forza relativa 1H V2 | ADA | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,20283 | 0,20726 | 0,20884 | 0,30323 | 0,18961 | €17,52 | €35,04 | €1,04 | €-0,77 |
| Forza relativa 1H V2 | HEMI | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €200,86 | €401,72 | €48,21 | €0,00 |
| Forza relativa 1H V2 | BTR | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,05109 | 0,05109 | 0,05109 | 0,07638 | 0,03760 | €205,02 | €410,03 | €0,00 | €-0,00 |
| Forza relativa 1H V2 | ENA | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,14147 | 0,14147 | 0,14728 | 0,21150 | 0,12869 | €12,62 | €25,24 | €1,04 | €-0,00 |
| Benchmark Donchian breakout 1H | SKHYNIX | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1174,33482 | 1174,33482 | 1128,44989 | 593,03908 | 1289,04713 | €641,25 | €1.282,50 | €50,11 | €0,00 |
| Benchmark Donchian breakout 1H | VELVET | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,14787 | 0,14787 | 0,16561 | 0,22107 | 0,10351 | €237,23 | €474,47 | €56,94 | €-0,00 |
| Benchmark Donchian breakout 1H | ADA | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,20283 | 0,20726 | 0,20951 | 0,30323 | 0,18614 | €72,87 | €145,74 | €4,80 | €-3,18 |
| Benchmark Donchian breakout 1H | PEPE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00001 | 0,00000 | €794,09 | €1.588,18 | €58,23 | €37,57 |
| Benchmark Donchian breakout 1H | DASH | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 56,56868 | 56,56868 | 59,42929 | 84,57018 | 49,41718 | €19,03 | €38,06 | €1,92 | €-0,00 |
| Benchmark Donchian breakout 1H | ENA | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,13916 | 0,13916 | 0,14676 | 0,20805 | 0,12016 | €18,63 | €37,26 | €2,03 | €-0,00 |
| Benchmark Donchian breakout 1H | LONGXIA | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,15106 | 0,14915 | 0,15244 | 0,07629 | 0,19638 | €228,29 | €456,59 | €0,00 | €-5,78 |
| Donchian 1H Gb20 120R V1 | SKHYNIX | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1174,33482 | 1174,33482 | 1128,44989 | 593,03908 | 1289,04713 | €626,15 | €1.252,30 | €48,93 | €0,00 |
| Donchian 1H Gb20 120R V1 | VELVET | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,14787 | 0,14787 | 0,16561 | 0,22107 | 0,10351 | €231,65 | €463,30 | €55,60 | €-0,00 |
| Donchian 1H Gb20 120R V1 | ADA | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,20283 | 0,20726 | 0,20951 | 0,30323 | 0,18614 | €71,16 | €142,31 | €4,68 | €-3,11 |
| Donchian 1H Gb20 120R V1 | PEPE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00001 | 0,00000 | €775,40 | €1.550,79 | €56,86 | €36,69 |
| Donchian 1H Gb20 120R V1 | DASH | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 56,56868 | 56,56868 | 59,42929 | 84,57018 | 49,41718 | €18,58 | €37,16 | €1,88 | €-0,00 |
| Donchian 1H Gb20 120R V1 | ENA | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,13916 | 0,13916 | 0,14676 | 0,20805 | 0,12016 | €18,19 | €36,38 | €1,99 | €-0,00 |
| Donchian 1H Gb20 120R V1 | LONGXIA | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,15106 | 0,14915 | 0,15244 | 0,07629 | 0,19638 | €222,92 | €445,84 | €0,00 | €-5,64 |
| Benchmark Bollinger mean reversion 1H | DASH | LONG | Bollinger mean reversion | 60m | 2,0x | 57,17143 | 57,17143 | 54,76797 | 28,87157 | 60,77663 | €497,61 | €995,23 | €41,84 | €0,00 |
| Benchmark trend following EMA 1H | BEAT | SHORT | Trend following EMA | 60m | 2,0x | 0,28257 | 0,28257 | 0,25706 | 0,42244 | 0,20797 | €186,11 | €372,23 | €0,00 | €-0,00 |
| Benchmark trend following EMA 1H | TUT | SHORT | Trend following EMA | 60m | 2,0x | 0,04446 | 0,04446 | 0,04980 | 0,06647 | 0,03272 | €194,70 | €389,39 | €46,73 | €-0,00 |
| Benchmark trend following EMA 1H | VELVET | SHORT | Trend following EMA | 60m | 2,0x | 0,14786 | 0,14786 | 0,16560 | 0,22105 | 0,10883 | €187,91 | €375,83 | €45,10 | €-0,00 |
| Benchmark trend following EMA 1H | ARB | LONG | Trend following EMA | 60m | 2,0x | 0,13283 | 0,13283 | 0,12390 | 0,06708 | 0,15246 | €341,57 | €683,14 | €45,90 | €0,00 |
| Benchmark trend following EMA 1H | UNI | LONG | Trend following EMA | 60m | 2,0x | 7,07742 | 6,36600 | 6,75804 | 3,57409 | 7,78005 | €71,53 | €143,05 | €6,46 | €-14,38 |
| Scanner Top 5 Long 1H | BOME | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00160 | €218,24 | €436,47 | €52,38 | €0,00 |
| Scanner Top 5 Long 1H | TRUMP | LONG | Scanner Top 5 Long | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,08367 | €238,89 | €477,78 | €55,13 | €0,00 |
| Scanner Top 5 Long 1H | SKHYNIX | LONG | Scanner Top 5 Long | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1331,36020 | €17,74 | €35,49 | €0,91 | €0,00 |
| Scanner Top 5 Long 1H | HEMI | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €228,24 | €456,48 | €54,78 | €0,00 |
| Scanner Top 5 Long 1H | ARB | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,14889 | €453,65 | €907,29 | €54,86 | €0,00 |
| Scanner Top 5 Long 1H | ETH | LONG | Scanner Top 5 Long | 60m | 2,0x | 2534,63683 | 2520,83000 | 2498,13806 | 1279,99160 | 2607,63437 | €26,30 | €52,61 | €0,76 | €-0,29 |
| Scanner Bottom 5 Short 1H | SOXL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €378,86 | €757,72 | €48,07 | €-0,00 |
| Scanner Bottom 5 Short 1H | SNDK | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €492,80 | €985,60 | €47,71 | €-0,00 |
| Scanner Bottom 5 Short 1H | VELVET | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €191,07 | €382,14 | €0,00 | €-0,00 |
| Scanner Bottom 5 Short 1H | TUT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €178,38 | €356,76 | €42,81 | €-0,00 |
| Scanner Top10 Long | TAO | LONG | Scanner Top10 Long | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €678,43 | €1.356,86 | €51,81 | €0,00 |
| Scanner Top10 Long | SKHYNIX | LONG | Scanner Top10 Long | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €972,86 | €1.945,72 | €48,38 | €0,00 |
| Scanner Top10 Long | HEMI | LONG | Scanner Top10 Long | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €207,88 | €415,77 | €49,89 | €0,00 |
| Scanner Top10 Long | ARB | LONG | Scanner Top10 Long | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,14889 | €422,09 | €844,19 | €51,04 | €0,00 |
| Scanner Top10 Long | UNI | LONG | Scanner Top10 Long | 60m | 2,0x | 7,14143 | 6,36600 | 6,87560 | 3,60642 | 7,67309 | €15,10 | €30,20 | €1,12 | €-3,28 |
| Scanner Top10 Long | ETH | LONG | Scanner Top10 Long | 60m | 2,0x | 2534,63683 | 2520,83000 | 2498,13806 | 1279,99160 | 2607,63437 | €53,34 | €106,69 | €1,54 | €-0,58 |
| Scanner Bottom10 Short | SOXL | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom10 Short | SNDK | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Bottom10 Short | VELVET | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €194,19 | €388,38 | €0,00 | €-0,00 |
| Scanner Bottom10 Short | TUT | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €181,31 | €362,61 | €43,51 | €-0,00 |
| Scanner Top15 Long | NEAR | LONG | Scanner Top15 Long | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €16,79 | €33,59 | €1,21 | €0,00 |
| Scanner Top15 Long | TAO | LONG | Scanner Top15 Long | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €88,53 | €177,07 | €6,76 | €0,00 |
| Scanner Top15 Long | TRUMP | LONG | Scanner Top15 Long | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,08367 | €215,87 | €431,75 | €49,81 | €0,00 |
| Scanner Top15 Long | SKHYNIX | LONG | Scanner Top15 Long | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €787,36 | €1.574,72 | €39,16 | €0,00 |
| Scanner Top15 Long | ARB | LONG | Scanner Top15 Long | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,14889 | €426,02 | €852,04 | €51,52 | €0,00 |
| Scanner Top15 Long | UNI | LONG | Scanner Top15 Long | 60m | 2,0x | 7,12843 | 6,36600 | 6,87194 | 3,59985 | 7,64140 | €88,01 | €176,02 | €6,33 | €-18,83 |
| Scanner Bottom15 Short | SOXL | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom15 Short | SNDK | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Bottom15 Short | VELVET | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €194,19 | €388,38 | €0,00 | €-0,00 |
| Scanner Bottom15 Short | TUT | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €181,31 | €362,61 | €43,51 | €-0,00 |
| Scanner Top20 Long | NEAR | LONG | Scanner Top20 Long | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €16,79 | €33,59 | €1,21 | €0,00 |
| Scanner Top20 Long | TAO | LONG | Scanner Top20 Long | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €88,53 | €177,07 | €6,76 | €0,00 |
| Scanner Top20 Long | TRUMP | LONG | Scanner Top20 Long | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,08367 | €215,87 | €431,75 | €49,81 | €0,00 |
| Scanner Top20 Long | SKHYNIX | LONG | Scanner Top20 Long | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €787,36 | €1.574,72 | €39,16 | €0,00 |
| Scanner Top20 Long | ARB | LONG | Scanner Top20 Long | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,14889 | €426,02 | €852,04 | €51,52 | €0,00 |
| Scanner Top20 Long | UNI | LONG | Scanner Top20 Long | 60m | 2,0x | 7,12843 | 6,36600 | 6,87194 | 3,59985 | 7,64140 | €88,01 | €176,02 | €6,33 | €-18,83 |
| Scanner Bottom20 Short | SOXL | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom20 Short | SNDK | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Bottom20 Short | VELVET | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €194,19 | €388,38 | €0,00 | €-0,00 |
| Scanner Bottom20 Short | TUT | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €181,31 | €362,61 | €43,51 | €-0,00 |
| Scanner Top 5 + forza BTC 1H | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €203,45 | €406,91 | €48,83 | €0,00 |
| Scanner Top 5 + forza BTC 1H | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,14149 | €223,03 | €446,06 | €51,47 | €0,00 |
| Scanner Top 5 + forza BTC 1H | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €18,23 | €36,45 | €0,93 | €0,00 |
| Scanner Top 5 + forza BTC 1H | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €213,35 | €426,70 | €51,20 | €0,00 |
| Scanner Top 5 + forza BTC 1H | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,15050 | €424,88 | €849,77 | €51,38 | €0,00 |
| Scanner Top 5 + forza BTC 1H | UNI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 7,09542 | 6,36600 | 6,78408 | 3,58319 | 7,78036 | €17,99 | €35,98 | €1,58 | €-3,70 |
| Scanner Top5 Btc Mfe V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €190,73 | €381,46 | €45,77 | €0,00 |
| Scanner Top5 Btc Mfe V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,14149 | €209,08 | €418,16 | €48,25 | €0,00 |
| Scanner Top5 Btc Mfe V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €17,09 | €34,17 | €0,88 | €0,00 |
| Scanner Top5 Btc Mfe V1 | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €200,01 | €400,01 | €48,00 | €0,00 |
| Scanner Top5 Btc Mfe V1 | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,15050 | €398,31 | €796,61 | €48,17 | €0,00 |
| Scanner Top5 Btc Mfe V1 | UNI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 7,09542 | 6,36600 | 6,78408 | 3,58319 | 7,78036 | €16,86 | €33,73 | €1,48 | €-3,47 |
| Scanner Top5 Btc Guard V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €197,27 | €394,55 | €47,35 | €0,00 |
| Scanner Top5 Btc Guard V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,55551 | 2,55551 | 2,29388 | 1,29053 | 3,13109 | €13,03 | €26,06 | €2,67 | €0,00 |
| Scanner Top5 Btc Guard V1 | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €195,03 | €390,06 | €46,81 | €0,00 |
| Scanner Top5 Btc Guard V1 | ZORA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00942 | 0,00942 | 0,00829 | 0,00476 | 0,01191 | €192,06 | €384,12 | €46,09 | €0,00 |
| Scanner Top5 Btc Guard V1 | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,15050 | €401,05 | €802,11 | €48,50 | €0,00 |
| Scanner Top5 Btc Guard V1 | ETH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2534,63683 | 2520,83000 | 2498,13806 | 1279,99160 | 2614,93412 | €72,91 | €145,82 | €2,10 | €-0,79 |
| Scanner Top5 Btc Btc Le3 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €847,75 | €1.695,49 | €43,45 | €0,00 |
| Scanner Top5 Btc Btc Le3 V1 | 0G | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,24373 | 0,24373 | 0,21916 | 0,12308 | 0,29778 | €215,80 | €431,60 | €43,51 | €0,00 |
| Scanner Top5 Btc Btc Le3 V1 | UNI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 7,16543 | 6,36600 | 6,92567 | 3,61854 | 7,69291 | €17,38 | €34,75 | €1,16 | €-3,88 |
| Scanner Top5 Btc Btc Le3 V1 | WLD | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,46919 | 0,46919 | 0,44675 | 0,23694 | 0,51857 | €433,72 | €867,43 | €41,49 | €0,00 |
| Scanner Top5 Btc Btc Le3 V1 | ETH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2534,63683 | 2520,83000 | 2498,13806 | 1279,99160 | 2614,93412 | €1.330,18 | €2.660,36 | €38,31 | €-14,49 |
| Scanner Top5 Btc Btc 2 3 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €891,28 | €1.782,56 | €45,68 | €0,00 |
| Scanner Top5 Btc Btc 2 3 V1 | UNI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 7,09542 | 6,36600 | 6,78408 | 3,58319 | 7,78036 | €17,98 | €35,96 | €1,58 | €-3,70 |
| Scanner Top5 Btc Guard Mfe V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €192,69 | €385,37 | €46,24 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,55551 | 2,55551 | 2,29388 | 1,29053 | 3,13109 | €12,72 | €25,45 | €2,61 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €190,49 | €380,99 | €45,72 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | ZORA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00942 | 0,00942 | 0,00829 | 0,00476 | 0,01191 | €187,59 | €375,19 | €45,02 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,15050 | €391,73 | €783,45 | €47,37 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | ETH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2534,63683 | 2520,83000 | 2498,13806 | 1279,99160 | 2614,93412 | €71,22 | €142,44 | €2,05 | €-0,78 |
| Scanner Top5 Btc Guard Btc Le3 V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,55551 | 2,55551 | 2,29388 | 1,29053 | 3,13109 | €12,70 | €25,40 | €2,60 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €191,20 | €382,39 | €45,89 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | PROM | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 7,01991 | 7,01991 | 6,30832 | 3,54505 | 8,58541 | €213,89 | €427,78 | €43,36 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | ZORA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00942 | 0,00942 | 0,00829 | 0,00476 | 0,01191 | €188,34 | €376,68 | €45,20 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | UNI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 7,14143 | 6,36600 | 6,87560 | 3,60642 | 7,72626 | €12,97 | €25,94 | €0,97 | €-2,82 |
| Scanner Top5 Btc Guard Btc Le3 V1 | ETH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2534,63683 | 2520,83000 | 2498,13806 | 1279,99160 | 2614,93412 | €1.488,88 | €2.977,76 | €42,88 | €-16,22 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | ZORA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00942 | 0,00942 | 0,00829 | 0,00476 | 0,01191 | €185,37 | €370,74 | €44,49 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | LINK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 13,22564 | 13,22564 | 12,79229 | 6,67895 | 14,17903 | €673,21 | €1.346,41 | €44,12 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | WLD | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,46919 | 0,46919 | 0,44675 | 0,23694 | 0,51857 | €462,02 | €924,05 | €44,20 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | ETH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2534,63683 | 2520,83000 | 2498,13806 | 1279,99160 | 2614,93412 | €1.425,82 | €2.851,65 | €41,06 | €-15,53 |
| Scanner Top5 Btc Runner25 V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00176 | €210,95 | €421,90 | €50,63 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1363,81560 | €965,52 | €1.931,04 | €49,49 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01601 | €209,51 | €419,03 | €50,28 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,15692 | €27,23 | €54,45 | €3,29 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | UNI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 7,09542 | 6,36600 | 6,78408 | 3,58319 | 8,02944 | €21,18 | €42,36 | €1,86 | €-4,35 |
| Scanner Top5 Btc Runner25 V1 | ETH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2534,63683 | 2520,83000 | 2498,13806 | 1279,99160 | 2644,13314 | €1.458,33 | €2.916,66 | €42,00 | €-15,89 |
| Scanner Top5 Btc Tp3 V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00176 | €211,07 | €422,14 | €50,66 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1363,81560 | €966,09 | €1.932,17 | €49,52 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01601 | €209,64 | €419,27 | €50,31 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,15692 | €27,24 | €54,49 | €3,29 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | UNI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 7,09542 | 6,36600 | 6,78408 | 3,58319 | 8,02944 | €21,19 | €42,39 | €1,86 | €-4,36 |
| Scanner Top5 Btc Tp3 V1 | ETH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2534,63683 | 2520,83000 | 2498,13806 | 1279,99160 | 2644,13314 | €1.459,18 | €2.918,36 | €42,02 | €-15,90 |
| Global Confluence puro 1H | DOGE | SHORT | Global Confluence puro | 60m | 2,0x | 0,08414 | 0,08470 | 0,08655 | 0,12579 | 0,07812 | €847,30 | €1.694,61 | €48,51 | €-11,21 |
| Combo Trend | BEAT | SHORT | Combo Trend | 60m | 2,0x | 0,25984 | 0,25984 | 0,25657 | 0,38847 | 0,19125 | €193,71 | €387,42 | €0,00 | €-0,00 |
| Combo Trend | ADA | SHORT | Combo Trend | 60m | 2,0x | 0,19986 | 0,20726 | 0,20356 | 0,29879 | 0,19173 | €1.205,82 | €2.411,64 | €44,61 | €-89,29 |
| Combo Trend | BTR | SHORT | Combo Trend | 60m | 2,0x | 0,05109 | 0,05109 | 0,05109 | 0,07638 | 0,03760 | €188,04 | €376,08 | €0,00 | €-0,00 |
| Combo Trend | ARB | LONG | Combo Trend | 60m | 2,0x | 0,13283 | 0,13283 | 0,12390 | 0,06708 | 0,15246 | €327,77 | €655,53 | €44,04 | €0,00 |
| Combo Trend | UNI | LONG | Combo Trend | 60m | 2,0x | 7,07742 | 6,36600 | 6,75804 | 3,57409 | 7,78005 | €68,62 | €137,24 | €6,19 | €-13,80 |
| Combo Mean Reversion | ADA | LONG | Combo Mean Reversion | 60m | 2,0x | 0,20284 | 0,20726 | 0,19804 | 0,10244 | 0,21052 | €942,00 | €1.883,99 | €44,59 | €41,04 |
| Combo Scanner | BOME | LONG | Combo Scanner | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €195,20 | €390,40 | €46,85 | €0,00 |
| Combo Scanner | TRUMP | LONG | Combo Scanner | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,14149 | €213,98 | €427,96 | €49,38 | €0,00 |
| Combo Scanner | SKHYNIX | LONG | Combo Scanner | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €24,78 | €49,55 | €1,27 | €0,00 |
| Combo Scanner | ARB | LONG | Combo Scanner | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,15050 | €419,07 | €838,14 | €50,68 | €0,00 |
| Combo Scanner | UNI | LONG | Combo Scanner | 60m | 2,0x | 7,09542 | 6,36600 | 6,78408 | 3,58319 | 7,78036 | €583,31 | €1.166,62 | €51,19 | €-119,93 |
| Combo Scanner | TAO | LONG | Combo Scanner | 60m | 2,0x | 264,91297 | 264,91297 | 254,31765 | 133,78105 | 288,22268 | €105,11 | €210,22 | €8,41 | €0,00 |
| Combo Adaptive | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,01735 | 121,01735 | 128,90956 | 180,92093 | 105,23292 | €367,30 | €734,61 | €47,91 | €-0,00 |
| Combo Adaptive | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €40,89 | €81,77 | €3,12 | €0,00 |
| Combo Adaptive | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,52450 | 2,33981 | 1,27487 | 2,89389 | €18,69 | €37,37 | €2,73 | €0,00 |
| Combo Adaptive | 0G | LONG | Combo Adaptive | 60m | 2,0x | 0,23904 | 0,23904 | 0,21329 | 0,12072 | 0,29055 | €230,13 | €460,26 | €49,58 | €0,00 |
| Combo Adaptive | BTR | SHORT | Combo Adaptive | 60m | 2,0x | 0,04853 | 0,04853 | 0,04853 | 0,07255 | 0,03688 | €212,51 | €425,02 | €0,00 | €-0,00 |
| Combo Adaptive | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,14889 | €420,61 | €841,21 | €50,86 | €0,00 |
| Combo Adaptive | UNI | LONG | Combo Adaptive | 60m | 2,0x | 7,16543 | 6,36600 | 6,92567 | 3,61854 | 7,64496 | €12,79 | €25,58 | €0,86 | €-2,85 |
| Combo Adaptive | DASH | SHORT | Combo Adaptive | 60m | 2,0x | 55,60888 | 55,60888 | 57,81052 | 83,13527 | 51,20558 | €15,51 | €31,02 | €1,23 | €-0,00 |
| Combo Adaptive Mfe Trail | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €54,29 | €108,58 | €4,15 | €0,00 |
| Combo Adaptive Mfe Trail | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,52450 | 2,33981 | 1,27487 | 2,89389 | €315,75 | €631,50 | €46,20 | €0,00 |
| Combo Adaptive Mfe Trail | TUT | SHORT | Combo Adaptive | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €190,04 | €380,09 | €45,61 | €-0,00 |
| Combo Adaptive Mfe Trail | PROM | LONG | Combo Adaptive | 60m | 2,0x | 7,01991 | 7,01991 | 6,30832 | 3,54505 | 8,44309 | €21,72 | €43,45 | €4,40 | €0,00 |
| Combo Adaptive Mfe Trail | BTR | SHORT | Combo Adaptive | 60m | 2,0x | 0,04991 | 0,04991 | 0,04841 | 0,07462 | 0,03793 | €142,63 | €285,27 | €0,00 | €-0,00 |
| Combo Adaptive Mfe Trail | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,14889 | €367,37 | €734,74 | €44,43 | €0,00 |
| Combo Adaptive Mfe Trail | DASH | SHORT | Combo Adaptive | 60m | 2,0x | 55,60888 | 55,60888 | 57,81052 | 83,13527 | 51,20558 | €21,30 | €42,61 | €1,69 | €-0,00 |
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
| Combo Adaptive Long Only V1 | UNI | LONG | Combo Adaptive | 60m | 2,0x | 7,16543 | 6,36600 | 6,92567 | 3,61854 | 7,64496 | €15,48 | €30,96 | €1,04 | €-3,45 |
| Combo Adaptive Long Only V1 | ETH | LONG | Combo Adaptive | 60m | 2,0x | 2534,63683 | 2520,83000 | 2498,13806 | 1279,99160 | 2607,63437 | €154,12 | €308,25 | €4,44 | €-1,68 |
| Combo Adaptive Partial 1R V1 | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,01735 | 121,01735 | 128,90956 | 180,92093 | 105,23292 | €352,70 | €705,40 | €46,00 | €-0,00 |
| Combo Adaptive Partial 1R V1 | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,52450 | 2,33981 | 1,27487 | 2,89389 | €347,19 | €694,38 | €50,80 | €0,00 |
| Combo Adaptive Partial 1R V1 | VELVET | SHORT | Combo Adaptive | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €207,76 | €415,52 | €0,00 | €-0,00 |
| Combo Adaptive Partial 1R V1 | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €1.013,20 | €2.026,40 | €50,39 | €0,00 |
| Combo Adaptive Partial 1R V1 | TAO | LONG | Combo Adaptive | 60m | 2,0x | 264,91297 | 264,91297 | 254,31765 | 133,78105 | 286,10361 | €49,09 | €98,18 | €3,93 | €0,00 |
| Combo Adaptive Runner25 V1 | 0G | LONG | Combo Adaptive | 60m | 2,0x | 0,23904 | 0,23904 | 0,21329 | 0,12072 | 0,31630 | €204,19 | €408,39 | €43,99 | €0,00 |
| Combo Adaptive Runner25 V1 | BTR | SHORT | Combo Adaptive | 60m | 2,0x | 0,04991 | 0,04991 | 0,04991 | 0,07462 | 0,03194 | €182,83 | €365,66 | €0,00 | €-0,00 |
| Combo Adaptive Runner25 V1 | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,15692 | €376,21 | €752,41 | €45,50 | €0,00 |
| Combo Adaptive Runner25 V1 | UNI | LONG | Combo Adaptive | 60m | 2,0x | 7,16543 | 6,36600 | 6,92567 | 3,61854 | 7,88472 | €17,00 | €34,01 | €1,14 | €-3,79 |
| Combo Adaptive Runner25 V1 | TAO | LONG | Combo Adaptive | 60m | 2,0x | 264,91297 | 264,91297 | 254,31765 | 133,78105 | 296,69893 | €536,57 | €1.073,13 | €42,92 | €0,00 |
| Combo Adaptive Runner25 V1 | SUI | SHORT | Combo Adaptive | 60m | 2,0x | 0,73075 | 0,73075 | 0,75468 | 1,09248 | 0,65898 | €73,50 | €146,99 | €4,81 | €-0,00 |
| Combo Adaptive Tp3 V1 | 0G | LONG | Combo Adaptive | 60m | 2,0x | 0,23904 | 0,23904 | 0,21329 | 0,12072 | 0,31630 | €200,38 | €400,76 | €43,17 | €0,00 |
| Combo Adaptive Tp3 V1 | BTR | SHORT | Combo Adaptive | 60m | 2,0x | 0,04991 | 0,04991 | 0,04991 | 0,07462 | 0,03194 | €179,40 | €358,80 | €0,00 | €-0,00 |
| Combo Adaptive Tp3 V1 | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,15692 | €369,17 | €738,34 | €44,64 | €0,00 |
| Combo Adaptive Tp3 V1 | UNI | LONG | Combo Adaptive | 60m | 2,0x | 7,16543 | 6,36600 | 6,92567 | 3,61854 | 7,88472 | €16,69 | €33,37 | €1,12 | €-3,72 |
| Combo Adaptive Tp3 V1 | TAO | LONG | Combo Adaptive | 60m | 2,0x | 264,91297 | 264,91297 | 254,31765 | 133,78105 | 296,69893 | €526,53 | €1.053,06 | €42,12 | €0,00 |
| Combo Adaptive Tp3 V1 | SUI | SHORT | Combo Adaptive | 60m | 2,0x | 0,73075 | 0,73075 | 0,75468 | 1,09248 | 0,65898 | €72,15 | €144,29 | €4,72 | €-0,00 |
| Btc Ema 1H | BTC | SHORT | Trend following EMA | 60m | 3,0x | 77124,03211 | 77184,70000 | 78361,20879 | 102446,42265 | 74649,67798 | €980,04 | €2.940,12 | €47,16 | €-2,31 |
| Eth Ema 1H | ETH | LONG | Trend following EMA | 60m | 3,0x | 2532,64643 | 2520,83000 | 2496,17632 | 1701,09418 | 2605,58665 | €1.107,07 | €3.321,22 | €47,83 | €-15,50 |
| Eth Ema 4H | ETH | LONG | Trend following EMA | 240m | 2,0x | 2545,25895 | 2520,83000 | 2440,79376 | 1285,35577 | 2806,42191 | €599,05 | €1.198,10 | €49,17 | €-11,50 |
| Eth Adaptive 1H | ETH | LONG | Combo Adaptive | 60m | 3,0x | 2534,63683 | 2520,83000 | 2498,13806 | 1702,43107 | 2607,63437 | €1.112,86 | €3.338,57 | €48,08 | €-18,19 |
| Doge Ema 1H | DOGE | SHORT | Trend following EMA | 60m | 3,0x | 0,08409 | 0,08470 | 0,08612 | 0,11170 | 0,08003 | €694,33 | €2.082,98 | €50,26 | €-15,03 |
| Master Adaptive V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99403 | 639,55695 | 1331,36019 | €22,75 | €45,50 | €1,17 | €0,00 |
| Master Adaptive V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €195,57 | €391,15 | €46,94 | €0,00 |
| Master Adaptive V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,20498 | 0,11491 | 0,27267 | €236,54 | €473,08 | €46,91 | €0,00 |
| Master Adaptive V1 | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,13517 | 0,13517 | 0,12719 | 0,06826 | 0,15112 | €410,30 | €820,61 | €48,44 | €0,00 |
| Master Adaptive No Alt V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1255,10261 | 1255,10261 | 1225,12158 | 633,82682 | 1315,06467 | €19,09 | €38,19 | €0,91 | €0,00 |
| Master Adaptive No Alt V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €183,81 | €367,62 | €44,11 | €0,00 |
| Master Adaptive No Alt V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 530,08600 | 530,08600 | 509,10047 | 267,69343 | 572,05705 | €589,91 | €1.179,82 | €46,71 | €0,00 |
| Master Adaptive No Alt V1 | WLD | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,46919 | 0,46919 | 0,44675 | 0,23694 | 0,51408 | €481,98 | €963,96 | €46,11 | €0,00 |
| Master Adaptive No Alt V1 | SOL | LONG | Master Adaptive Consensus | 60m | 2,0x | 101,98939 | 101,74400 | 99,81288 | 51,50464 | 106,34243 | €1.087,63 | €2.175,26 | €46,42 | €-5,23 |
| Master Adaptive No Alt V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 2522,04431 | 2520,83000 | 2485,03048 | 1273,63238 | 2596,07196 | €42,89 | €85,77 | €1,26 | €-0,04 |
| Master Adaptive Strict3 V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €178,16 | €356,31 | €42,76 | €0,00 |
| Master Adaptive Strict3 V1 | PROM | LONG | Master Adaptive Consensus | 60m | 2,0x | 7,01991 | 7,01991 | 6,30832 | 3,54505 | 8,44309 | €215,49 | €430,99 | €43,69 | €0,00 |
| Master Adaptive Strict3 V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,24076 | 0,24076 | 0,21579 | 0,12159 | 0,29071 | €209,83 | €419,66 | €43,53 | €0,00 |
| Master Adaptive Strict3 V1 | LINK | LONG | Master Adaptive Consensus | 60m | 2,0x | 13,22564 | 13,22564 | 12,79229 | 6,67895 | 14,09236 | €13,27 | €26,55 | €0,87 | €0,00 |
| Master Adaptive Strict3 V1 | WLD | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,46919 | 0,46919 | 0,44675 | 0,23694 | 0,51408 | €465,87 | €931,73 | €44,57 | €0,00 |
| Master Adaptive Strict3 V1 | USELESS | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,28110 | 0,28110 | 0,24944 | 0,14195 | 0,34441 | €15,82 | €31,64 | €3,56 | €0,00 |
| Master Adaptive Expanded V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03814 | 0,02188 | 0,05374 | €197,50 | €395,01 | €47,40 | €0,00 |
| Master Adaptive Expanded V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1261,89668 | 1261,89668 | 1231,08309 | 637,25783 | 1323,52387 | €934,21 | €1.868,43 | €45,62 | €0,00 |
| Master Adaptive Expanded V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01194 | 0,01194 | 0,01050 | 0,00603 | 0,01480 | €195,34 | €390,67 | €46,88 | €0,00 |
| Master Adaptive Expanded V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,20498 | 0,11491 | 0,27267 | €236,25 | €472,49 | €46,85 | €0,00 |
| Master Adaptive Expanded V1 | SOL | LONG | Master Adaptive Consensus | 60m | 2,0x | 101,98939 | 101,74400 | 99,81288 | 51,50464 | 106,34243 | €14,87 | €29,75 | €0,63 | €-0,07 |
| Master Adaptive Gb20 V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99403 | 639,55695 | 1331,36019 | €22,45 | €44,90 | €1,15 | €0,00 |
| Master Adaptive Gb20 V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €193,03 | €386,06 | €46,33 | €0,00 |
| Master Adaptive Gb20 V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,20498 | 0,11491 | 0,27267 | €233,42 | €466,83 | €46,29 | €0,00 |
| Master Adaptive Gb20 V1 | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,13517 | 0,13517 | 0,12719 | 0,06826 | 0,15112 | €404,89 | €809,78 | €47,80 | €0,00 |
| Master Adaptive Runner25 V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03814 | 0,02188 | 0,05894 | €34,77 | €69,54 | €8,34 | €0,00 |
| Master Adaptive Runner25 V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1255,10261 | 1255,10261 | 1225,12158 | 633,82682 | 1345,04570 | €27,05 | €54,10 | €1,29 | €0,00 |
| Master Adaptive Runner25 V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01601 | €185,86 | €371,72 | €44,61 | €0,00 |
| Master Adaptive Runner25 V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,20498 | 0,11491 | 0,29523 | €233,84 | €467,69 | €46,37 | €0,00 |
| Master Adaptive Runner25 V1 | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,13517 | 0,13517 | 0,12719 | 0,06826 | 0,15910 | €399,89 | €799,78 | €47,21 | €0,00 |
| Master Adaptive Runner25 V1 | SOL | LONG | Master Adaptive Consensus | 60m | 2,0x | 101,98939 | 101,74400 | 99,81288 | 51,50464 | 108,51894 | €979,52 | €1.959,05 | €41,81 | €-4,71 |
| Combo Adaptive Side Regime Guard V1 | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €77,52 | €155,04 | €5,58 | €0,00 |
| Combo Adaptive Side Regime Guard V1 | VELVET | SHORT | Combo Adaptive | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €216,61 | €433,23 | €0,00 | €-0,00 |
| Combo Adaptive Side Regime Guard V1 | TUT | SHORT | Combo Adaptive | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €192,40 | €384,79 | €46,18 | €-0,00 |
| Combo Adaptive Side Regime Guard V1 | BTR | SHORT | Combo Adaptive | 60m | 2,0x | 0,05109 | 0,05109 | 0,05109 | 0,07638 | 0,03883 | €195,57 | €391,13 | €0,00 | €-0,00 |
| Combo Adaptive Side Regime Guard V1 | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,14889 | €385,18 | €770,35 | €46,58 | €0,00 |
| Combo Adaptive Side Regime Guard V1 | UNI | LONG | Combo Adaptive | 60m | 2,0x | 7,16543 | 6,36600 | 6,92567 | 3,61854 | 7,64496 | €12,54 | €25,08 | €0,84 | €-2,80 |
| Master Adaptive Gb20 Be V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99403 | 639,55695 | 1331,36019 | €22,86 | €45,73 | €1,17 | €0,00 |
| Master Adaptive Gb20 Be V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €196,54 | €393,08 | €47,17 | €0,00 |
| Master Adaptive Gb20 Be V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,20498 | 0,11491 | 0,27267 | €237,71 | €475,42 | €47,14 | €0,00 |
| Master Adaptive Gb20 Be V1 | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,13517 | 0,13517 | 0,12719 | 0,06826 | 0,15112 | €412,34 | €824,67 | €48,68 | €0,00 |
| Master Adaptive Gb20 Partial V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99403 | 639,55695 | 1331,36019 | €22,84 | €45,68 | €1,17 | €0,00 |
| Master Adaptive Gb20 Partial V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €196,33 | €392,67 | €47,12 | €0,00 |
| Master Adaptive Gb20 Partial V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,20498 | 0,11491 | 0,27267 | €237,46 | €474,91 | €47,09 | €0,00 |
| Master Adaptive Gb20 Partial V1 | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,13517 | 0,13517 | 0,12719 | 0,06826 | 0,15112 | €411,90 | €823,79 | €48,63 | €0,00 |
| Master Adaptive Gb20 Loss Cap V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03828 | 0,02188 | 0,05682 | €195,70 | €391,41 | €45,67 | €0,00 |
| Master Adaptive Gb20 Loss Cap V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01069 | 0,00594 | 0,01465 | €210,34 | €420,68 | €38,67 | €0,00 |
| Master Adaptive Gb20 Loss Cap V1 | PROM | LONG | Master Adaptive Consensus | 60m | 2,0x | 7,01991 | 7,01991 | 6,48622 | 3,54505 | 8,44309 | €34,75 | €69,51 | €5,28 | €0,00 |
| Master Adaptive Gb20 Loss Cap V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,21062 | 0,11491 | 0,27267 | €309,65 | €619,30 | €46,05 | €0,00 |
| Master Adaptive Gb20 Loss Cap V1 | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,13517 | 0,13517 | 0,12918 | 0,06826 | 0,15112 | €19,32 | €38,65 | €1,71 | €0,00 |
| Master Adaptive Gb20 Loss Cap V1 | WLD | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,46919 | 0,46919 | 0,45236 | 0,23694 | 0,51408 | €80,25 | €160,51 | €5,76 | €0,00 |
| Master Adaptive Gb20 Loss Cap V1 | SOL | LONG | Master Adaptive Consensus | 60m | 2,0x | 101,98939 | 101,74400 | 100,35701 | 51,50464 | 106,34243 | €1.354,62 | €2.709,25 | €43,36 | €-6,52 |
| 1H Fast V3 Nohigh Range Only V1 | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,20283 | 0,20726 | 0,20750 | 0,26943 | 0,19582 | €740,69 | €2.222,07 | €51,20 | €-48,54 |
| 1H Fast V3 Nohigh Range Only V1 | BTR | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €135,43 | €406,30 | €0,00 | €-0,00 |
| 1H Fast V3 Nohigh Range Only V1 | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 1126,41467 | 1144,70000 | 1150,15748 | 1496,25416 | 1090,80047 | €795,60 | €2.386,79 | €50,31 | €-38,75 |
| 1H Fast V3 Nohigh Regime Guard V1 | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €140,84 | €422,53 | €50,70 | €-0,00 |
| 1H Fast V3 Nohigh Regime Guard V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €143,15 | €429,46 | €50,70 | €-0,00 |
| 1H Fast V3 Nohigh Regime Guard V1 | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,20283 | 0,20726 | 0,20750 | 0,26943 | 0,19582 | €34,57 | €103,71 | €2,39 | €-2,27 |
| 1H Fast V3 Nohigh Regime Guard V1 | BTR | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,05154 | 0,05154 | 0,05154 | 0,06846 | 0,04226 | €139,06 | €417,17 | €0,00 | €-0,00 |
| 1H Fast V3 Nohigh Regime Guard V1 | ZEC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 1126,41467 | 1144,70000 | 1150,15748 | 1496,25416 | 1090,80047 | €815,98 | €2.447,95 | €51,60 | €-39,74 |
| Main Side Regime Guard V1 | VELVET | LONG | Confluenza trend | 240m | 3,0x | 0,55987 | 0,55987 | 0,49269 | 0,37605 | 0,69424 | €142,25 | €426,74 | €51,21 | €0,00 |
| Main Side Regime Guard V1 | AKE | LONG | Confluenza trend | 240m | 3,0x | 0,01021 | 0,01021 | 0,00899 | 0,00686 | 0,01266 | €145,97 | €437,90 | €52,55 | €0,00 |
| Main Side Regime Guard V1 | ENA | LONG | Confluenza trend | 240m | 3,0x | 0,16108 | 0,16108 | 0,14175 | 0,10819 | 0,19974 | €150,44 | €451,33 | €54,16 | €0,00 |
| Main Side Regime Guard V1 | BTR | SHORT | Confluenza trend | 240m | 3,0x | 0,04853 | 0,04853 | 0,05435 | 0,06446 | 0,03688 | €12,76 | €38,29 | €4,59 | €-0,00 |
| Main Side Regime Guard V1 | NEAR | LONG | Confluenza trend | 240m | 3,0x | 2,49550 | 2,49550 | 2,26921 | 1,67614 | 2,94807 | €15,83 | €47,48 | €4,31 | €0,00 |
| Main Side Regime Guard V1 | SUI | SHORT | Confluenza trend | 240m | 3,0x | 0,72995 | 0,72995 | 0,77421 | 0,96962 | 0,64144 | €294,19 | €882,58 | €53,51 | €-0,00 |
| Main Side Regime Guard V1 | ETH | LONG | Confluenza trend | 240m | 3,0x | 2525,71504 | 2520,83000 | 2455,33124 | 1696,43860 | 2666,48261 | €11,04 | €33,13 | €0,92 | €-0,06 |
| Main Dynamic Asset Selector V1 | ENA | LONG | Confluenza trend | 240m | 3,0x | 0,16108 | 0,16108 | 0,14175 | 0,10819 | 0,19974 | €140,98 | €422,93 | €50,75 | €0,00 |
| Main Dynamic Asset Selector V1 | ZEC | LONG | Confluenza trend | 240m | 3,0x | 1188,60767 | 1144,70000 | 1079,26876 | 798,34815 | 1407,28551 | €185,65 | €556,95 | €51,23 | €-20,57 |
| Combo Trend Side Regime Guard V1 | VELVET | SHORT | Combo Trend | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,12693 | €217,86 | €435,73 | €0,00 | €-0,00 |
| Combo Trend Side Regime Guard V1 | TUT | SHORT | Combo Trend | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03364 | €12,81 | €25,62 | €3,07 | €-0,00 |
| Combo Trend Side Regime Guard V1 | BTR | SHORT | Combo Trend | 60m | 2,0x | 0,04853 | 0,04853 | 0,05435 | 0,07255 | 0,03572 | €222,18 | €444,37 | €53,32 | €-0,00 |
| Combo Trend Side Regime Guard V1 | ARB | LONG | Combo Trend | 60m | 2,0x | 0,13283 | 0,13283 | 0,12390 | 0,06708 | 0,15246 | €399,57 | €799,13 | €53,69 | €0,00 |
| Combo Trend Side Regime Guard V1 | UNI | LONG | Combo Trend | 60m | 2,0x | 7,09542 | 6,36600 | 6,74949 | 3,58319 | 7,85647 | €523,05 | €1.046,10 | €51,00 | €-107,54 |
| Combo Trend Side Regime Guard V1 | TAO | LONG | Combo Trend | 60m | 2,0x | 264,91297 | 264,91297 | 253,14039 | 133,78105 | 290,81264 | €73,76 | €147,52 | €6,56 | €0,00 |
| 1H Fast Nohigh Cap75 Short Only V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €135,82 | €407,46 | €48,90 | €-0,00 |
| 1H Fast Nohigh Cap75 Short Only V1 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €138,05 | €414,14 | €48,89 | €-0,00 |
| 1H Fast Nohigh Cap75 Short Only V1 | BTR | SHORT | Momentum / breakout | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €132,24 | €396,72 | €0,00 | €-0,00 |
| 1H Fast Nohigh Cap75 Short Only V1 | PEPE | SHORT | Momentum / breakout | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €573,54 | €1.720,62 | €44,16 | €40,71 |
| 1H Fast Nohigh Cap75 Short Only V1 | ZEC | SHORT | Momentum / breakout | 60m | 3,0x | 1126,41467 | 1144,70000 | 1150,15748 | 1496,25416 | 1090,80047 | €18,88 | €56,64 | €1,19 | €-0,92 |
| 1H Balanced V3 Long Only V1 | SKHYNIX | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1220,85412 | 1220,85412 | 1177,63561 | 820,00702 | 1307,29117 | €435,49 | €1.306,46 | €46,25 | €0,00 |
| 1H Balanced V3 Long Only V1 | ADA | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,20138 | 0,20726 | 0,20719 | 0,26750 | 0,18976 | €529,53 | €1.588,58 | €45,82 | €-46,39 |
| 1H Balanced V3 Long Only V1 | ARB | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,13283 | 0,13283 | 0,12480 | 0,08922 | 0,14889 | €248,38 | €745,13 | €45,06 | €0,00 |
| 1H Balanced V3 Long Only V1 | UNI | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 7,14143 | 6,36600 | 6,87560 | 4,79666 | 7,67309 | €9,06 | €27,18 | €1,01 | €-2,95 |
| 1H Balanced V3 Long Only V1 | SOPH | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,00528 | 0,00528 | 0,00591 | 0,00701 | 0,00401 | €103,13 | €309,38 | €37,13 | €-0,00 |
| 1H Balanced V3 Long Only V1 | BTC | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 77124,03211 | 77184,70000 | 78361,20879 | 102446,42265 | 74649,67798 | €13,16 | €39,48 | €0,63 | €-0,03 |
| 1H Balanced V3 Long Only V1 | SUI | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,73075 | 0,73075 | 0,75468 | 0,97068 | 0,68290 | €11,12 | €33,36 | €1,09 | €-0,00 |
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
| 1H Fast V3 No Esports Long Only V1 | LONGXIA | LONG | 2026-09-13T04:00:00+00:00 | 0,17660 | €71,22 | 1,48 | TARGET |
| 1H Fast V3 Nohigh V1 | LONGXIA | LONG | 2026-09-13T04:00:00+00:00 | 0,17626 | €5,66 | 1,48 | TARGET |
| 1H Fast V3 Long Only V1 | LONGXIA | LONG | 2026-09-13T04:00:00+00:00 | 0,17660 | €69,44 | 1,48 | TARGET |
| 1H Fast V3 Long Nohigh Cap75 V1 | LONGXIA | LONG | 2026-09-13T04:00:00+00:00 | 0,17660 | €73,71 | 1,48 | TARGET |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | LONGXIA | LONG | 2026-09-13T04:00:00+00:00 | 0,17660 | €72,57 | 1,48 | TARGET |
| Scalp RSI Long 25 · prudente · 5x | ETH | LONG | 2026-09-13T02:15:00+00:00 | 2521,48560 | €-2,31 | -0,23 | TIME_EXIT |
| Scalp RSI Long 25 · €50 · 15x | ETH | LONG | 2026-09-13T00:15:00+00:00 | 2523,87512 | €0,02 | 0,01 | TIME_EXIT |
| Scalp RSI Long 25 · €10 · 15x | ETH | LONG | 2026-09-13T00:15:00+00:00 | 2523,87512 | €0,00 | 0,01 | TIME_EXIT |
| Ampia 4H | HYPE | LONG | 2026-09-12T20:06:36+00:00 | 79,81903 | €0,07 | 0,02 | TIME_EXIT_MARK |
| 1H Fast V3 No Esports Long Only V1 | LAB | LONG | 2026-09-12T19:45:00+00:00 | 0,06535 | €-49,84 | -1,02 | STOP |
| 1H Fast V3 Long Only V1 | LAB | LONG | 2026-09-12T19:45:00+00:00 | 0,06535 | €-48,59 | -1,02 | STOP |
| Donchian 1H Gb20 120R V1 | HYPE | SHORT | 2026-09-12T17:45:00+00:00 | 80,60182 | €-58,29 | -1,05 | STOP |

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

Generato: 2026-09-13 05:33 UTC


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

Segnali totali salvati: **195**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-09-13 | BTC | 77.274,99 | +6 | +3 | +3 | 0 | +2 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-09-13 | DOGE | 0.08485 | -5 | -2 | -2 | 0 | -2 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-09-13 | SOL | 101,86 | +4 | +3 | +3 | 0 | +1 | 0 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-09-12 | BTC | 77.204,26 | +3 | +3 | +3 | 0 | +1 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-09-12 | DOGE | 0.08434 | -5 | -2 | -2 | 0 | -2 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-09-12 | SOL | 101,54 | +4 | +3 | +3 | 0 | 0 | 0 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-09-11 | BTC | 77.053,66 | +5 | +3 | +3 | 0 | +2 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-09-11 | DOGE | 0.08388 | -6 | -2 | -2 | 0 | -2 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-09-11 | SOL | 99,59 | +2 | +2 | +2 | 0 | 0 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-09-10 | BTC | 78.479,28 | +6 | +3 | +3 | 0 | +2 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-09-10 | DOGE | 0.08593 | -4 | -2 | -2 | 0 | -1 | 0 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-09-10 | SOL | 102,04 | +5 | +2 | +2 | 0 | +2 | 0 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 65 | 64 | 63 | 62 | 60 | 58 | 55 | 51 | 44 | 35 | 22 | 7 |
| SOL | 65 | 64 | 63 | 62 | 60 | 58 | 55 | 51 | 44 | 35 | 22 | 7 |
| DOGE | 65 | 64 | 63 | 62 | 60 | 58 | 55 | 51 | 44 | 35 | 22 | 7 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-07-16 | 60g | 2026-09-14 | domani |
| SOL | 2026-07-16 | 60g | 2026-09-14 | domani |
| DOGE | 2026-07-16 | 60g | 2026-09-14 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 61 | 50,82% | +0,35% | +0,33% | UTILE |
| BTC | 2g | 60 | 50,00% | +0,60% | +0,52% | UTILE |
| BTC | 3g | 59 | 44,07% | +0,75% | +0,63% | PRIMA CALIBRAZIONE |
| BTC | 5g | 57 | 43,86% | +1,59% | +1,37% | PRIMA CALIBRAZIONE |
| BTC | 7g | 55 | 52,73% | +2,28% | +2,08% | PRIMA CALIBRAZIONE |
| BTC | 10g | 52 | 59,62% | +3,36% | +3,18% | PRIMA CALIBRAZIONE |
| BTC | 14g | 48 | 58,33% | +5,14% | +5,07% | PRIMA CALIBRAZIONE |
| BTC | 21g | 41 | 65,85% | +9,94% | +9,78% | PRIMA CALIBRAZIONE |
| BTC | 30g | 33 | 90,91% | +14,43% | +13,13% | PRIMA CALIBRAZIONE |
| BTC | 45g | 20 | 85,00% | +22,20% | +15,59% | FEEDBACK RAPIDO |
| BTC | 60g | 7 | 100,00% | +23,11% | +23,11% | FEEDBACK RAPIDO |
| SOL | 1g | 57 | 54,39% | +0,57% | +0,46% | PRIMA CALIBRAZIONE |
| SOL | 2g | 56 | 50,00% | +1,13% | +1,01% | PRIMA CALIBRAZIONE |
| SOL | 3g | 55 | 54,55% | +1,76% | +1,60% | PRIMA CALIBRAZIONE |
| SOL | 5g | 53 | 58,49% | +3,05% | +2,95% | PRIMA CALIBRAZIONE |
| SOL | 7g | 51 | 62,75% | +4,36% | +4,46% | PRIMA CALIBRAZIONE |
| SOL | 10g | 48 | 66,67% | +6,24% | +6,40% | PRIMA CALIBRAZIONE |
| SOL | 14g | 44 | 75,00% | +9,34% | +10,17% | PRIMA CALIBRAZIONE |
| SOL | 21g | 37 | 78,38% | +16,80% | +15,84% | PRIMA CALIBRAZIONE |
| SOL | 30g | 28 | 64,29% | +20,87% | +13,81% | FEEDBACK RAPIDO |
| SOL | 45g | 16 | 37,50% | +33,69% | -9,86% | FEEDBACK RAPIDO |
| SOL | 60g | 6 | 50,00% | +33,33% | +0,21% | FEEDBACK RAPIDO |
| DOGE | 1g | 60 | 43,33% | +0,37% | +0,06% | UTILE |
| DOGE | 2g | 59 | 44,07% | +0,74% | +0,17% | PRIMA CALIBRAZIONE |
| DOGE | 3g | 58 | 39,66% | +1,07% | +0,39% | PRIMA CALIBRAZIONE |
| DOGE | 5g | 56 | 46,43% | +1,90% | +1,30% | PRIMA CALIBRAZIONE |
| DOGE | 7g | 54 | 59,26% | +2,54% | +2,88% | PRIMA CALIBRAZIONE |
| DOGE | 10g | 51 | 54,90% | +2,92% | +3,67% | PRIMA CALIBRAZIONE |
| DOGE | 14g | 48 | 66,67% | +4,76% | +6,71% | PRIMA CALIBRAZIONE |
| DOGE | 21g | 42 | 76,19% | +9,09% | +8,15% | PRIMA CALIBRAZIONE |
| DOGE | 30g | 33 | 75,76% | +13,03% | +6,27% | PRIMA CALIBRAZIONE |
| DOGE | 45g | 21 | 19,05% | +20,47% | -12,47% | FEEDBACK RAPIDO |
| DOGE | 60g | 7 | 0,00% | +19,08% | -19,08% | FEEDBACK RAPIDO |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 61 | 50,82% | +0,35% | +0,33% | -0,09% | +0,87% | UTILE |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 64 | 53,12% | +0,33% | +0,33% | -0,10% | +0,84% | UTILE |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 64 | 53,12% | +0,33% | +0,33% | -0,10% | +0,84% | UTILE |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,25% | +0,25% | -0,10% | +0,70% | PRIMA CALIBRAZIONE |
| BTC | 1g | Tecnico | CALIBRABILE | 59 | 40,68% | +0,44% | +0,09% | -0,01% | +0,95% | PRIMA CALIBRAZIONE |
| BTC | 1g | Classic technical | CALIBRABILE | 24 | 37,50% | +0,81% | +0,37% | +0,13% | +1,33% | FEEDBACK RAPIDO |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | -0,17% | -0,17% | -0,60% | +0,27% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 60 | 50,00% | +0,60% | +0,52% | +0,03% | +1,26% | UTILE |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 63 | 52,38% | +0,69% | +0,69% | +0,13% | +1,35% | UTILE |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 63 | 52,38% | +0,69% | +0,69% | +0,13% | +1,35% | UTILE |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,52% | +0,52% | -0,02% | +1,18% | PRIMA CALIBRAZIONE |
| BTC | 2g | Tecnico | CALIBRABILE | 58 | 43,10% | +0,84% | +0,13% | +0,28% | +1,49% | PRIMA CALIBRAZIONE |
| BTC | 2g | Classic technical | CALIBRABILE | 24 | 41,67% | +1,18% | +0,55% | +0,59% | +1,89% | FEEDBACK RAPIDO |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +0,73% | +0,73% | +0,13% | +1,27% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 59 | 44,07% | +0,75% | +0,63% | -1,10% | +2,48% | PRIMA CALIBRAZIONE |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 62 | 51,61% | +1,03% | +1,03% | -1,07% | +2,69% | UTILE |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 62 | 51,61% | +1,03% | +1,03% | -1,07% | +2,69% | UTILE |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 35 | 57,14% | +0,91% | +0,91% | -1,00% | +2,36% | PRIMA CALIBRAZIONE |
| BTC | 3g | Tecnico | CALIBRABILE | 57 | 35,09% | +1,29% | -0,19% | -0,92% | +2,93% | PRIMA CALIBRAZIONE |
| BTC | 3g | Classic technical | CALIBRABILE | 24 | 41,67% | +1,81% | +0,20% | -0,58% | +3,31% | FEEDBACK RAPIDO |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +0,35% | +0,35% | -1,11% | +1,90% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 57 | 43,86% | +1,59% | +1,37% | -1,66% | +3,91% | PRIMA CALIBRAZIONE |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 60 | 50,00% | +1,83% | +1,83% | -1,63% | +4,20% | UTILE |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 60 | 50,00% | +1,83% | +1,83% | -1,63% | +4,20% | UTILE |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 35 | 48,57% | +2,08% | +2,08% | -1,57% | +4,07% | PRIMA CALIBRAZIONE |
| BTC | 5g | Tecnico | CALIBRABILE | 55 | 41,82% | +2,10% | -0,98% | -1,46% | +4,51% | PRIMA CALIBRAZIONE |
| BTC | 5g | Classic technical | CALIBRABILE | 24 | 50,00% | +3,70% | -1,14% | -1,03% | +5,94% | FEEDBACK RAPIDO |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 20,00% | -0,98% | -0,98% | -2,20% | +2,18% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 55 | 52,73% | +2,28% | +2,08% | -1,90% | +5,11% | PRIMA CALIBRAZIONE |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 58 | 58,62% | +2,59% | +2,59% | -1,87% | +5,39% | PRIMA CALIBRAZIONE |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 58 | 58,62% | +2,59% | +2,59% | -1,87% | +5,39% | PRIMA CALIBRAZIONE |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 35 | 60,00% | +3,17% | +3,17% | -1,80% | +5,49% | PRIMA CALIBRAZIONE |
| BTC | 7g | Tecnico | CALIBRABILE | 53 | 41,51% | +3,04% | -1,77% | -1,69% | +5,80% | PRIMA CALIBRAZIONE |
| BTC | 7g | Classic technical | CALIBRABILE | 24 | 45,83% | +4,87% | -2,81% | -1,33% | +8,02% | FEEDBACK RAPIDO |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | -1,21% | -1,21% | -3,03% | +2,32% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 52 | 59,62% | +3,36% | +3,18% | -2,01% | +6,40% | PRIMA CALIBRAZIONE |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 55 | 63,64% | +3,53% | +3,53% | -2,01% | +6,63% | PRIMA CALIBRAZIONE |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 55 | 63,64% | +3,53% | +3,53% | -2,01% | +6,63% | PRIMA CALIBRAZIONE |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 35 | 62,86% | +4,42% | +4,42% | -2,02% | +6,89% | PRIMA CALIBRAZIONE |
| BTC | 10g | Tecnico | CALIBRABILE | 50 | 46,00% | +4,00% | -1,32% | -1,79% | +7,18% | PRIMA CALIBRAZIONE |
| BTC | 10g | Classic technical | CALIBRABILE | 23 | 52,17% | +5,61% | -3,56% | -1,40% | +9,17% | FEEDBACK RAPIDO |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +0,54% | +0,54% | -2,46% | +3,88% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 48 | 58,33% | +5,14% | +5,07% | -2,16% | +8,71% | PRIMA CALIBRAZIONE |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 51 | 58,82% | +5,24% | +5,24% | -2,16% | +8,83% | PRIMA CALIBRAZIONE |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 51 | 58,82% | +5,24% | +5,24% | -2,16% | +8,83% | PRIMA CALIBRAZIONE |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 35 | 68,57% | +6,60% | +6,60% | -2,13% | +9,78% | PRIMA CALIBRAZIONE |
| BTC | 14g | Tecnico | CALIBRABILE | 46 | 54,35% | +5,94% | +0,68% | -1,91% | +9,61% | PRIMA CALIBRAZIONE |
| BTC | 14g | Classic technical | CALIBRABILE | 19 | 36,84% | +6,37% | -3,97% | -1,30% | +10,56% | FEEDBACK RAPIDO |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 33,33% | -0,03% | -0,03% | -2,90% | +4,64% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 41 | 65,85% | +9,94% | +9,78% | -2,06% | +13,84% | PRIMA CALIBRAZIONE |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 44 | 72,73% | +9,73% | +9,73% | -2,08% | +13,66% | PRIMA CALIBRAZIONE |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 44 | 72,73% | +9,73% | +9,73% | -2,08% | +13,66% | PRIMA CALIBRAZIONE |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 35 | 74,29% | +11,25% | +11,25% | -2,21% | +14,88% | PRIMA CALIBRAZIONE |
| BTC | 21g | Tecnico | CALIBRABILE | 39 | 41,03% | +10,77% | -0,91% | -1,78% | +14,79% | PRIMA CALIBRAZIONE |
| BTC | 21g | Classic technical | CALIBRABILE | 12 | 33,33% | +14,30% | -11,49% | -0,25% | +18,32% | FEEDBACK RAPIDO |
| BTC | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +1,26% | +1,26% | -1,61% | +6,04% | FEEDBACK RAPIDO |
| BTC | 30g | Global confluence | BENCHMARK | 33 | 90,91% | +14,43% | +13,13% | -2,87% | +18,56% | PRIMA CALIBRAZIONE |
| BTC | 30g | Famiglia statistica | CALIBRABILE | 35 | 85,71% | +14,07% | +14,07% | -2,92% | +18,26% | PRIMA CALIBRAZIONE |
| BTC | 30g | Scanner grezzo | DIAGNOSTICO | 35 | 85,71% | +14,07% | +14,07% | -2,92% | +18,26% | PRIMA CALIBRAZIONE |
| BTC | 30g | Market regime grezzo | DIAGNOSTICO | 31 | 87,10% | +15,28% | +15,28% | -2,71% | +19,70% | PRIMA CALIBRAZIONE |
| BTC | 30g | Tecnico | CALIBRABILE | 30 | 43,33% | +14,30% | -2,29% | -2,66% | +18,83% | PRIMA CALIBRAZIONE |
| BTC | 30g | Classic technical | CALIBRABILE | 5 | 0,00% | +23,88% | -23,88% | -1,27% | +29,00% | FEEDBACK RAPIDO |
| BTC | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +0,16% | +0,16% | -3,06% | +4,24% | FEEDBACK RAPIDO |
| BTC | 45g | Global confluence | BENCHMARK | 20 | 85,00% | +22,20% | +15,59% | -3,17% | +26,88% | FEEDBACK RAPIDO |
| BTC | 45g | Famiglia statistica | CALIBRABILE | 22 | 100,00% | +22,27% | +22,27% | -3,21% | +26,86% | FEEDBACK RAPIDO |
| BTC | 45g | Scanner grezzo | DIAGNOSTICO | 22 | 100,00% | +22,27% | +22,27% | -3,21% | +26,86% | FEEDBACK RAPIDO |
| BTC | 45g | Market regime grezzo | DIAGNOSTICO | 18 | 100,00% | +22,54% | +22,54% | -2,93% | +27,22% | FEEDBACK RAPIDO |
| BTC | 45g | Tecnico | CALIBRABILE | 18 | 27,78% | +22,53% | -10,08% | -2,87% | +27,34% | FEEDBACK RAPIDO |
| BTC | 45g | Classic technical | CALIBRABILE | 2 | 0,00% | +21,18% | -21,18% | -2,23% | +29,25% | FEEDBACK RAPIDO |
| BTC | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +20,42% | +20,42% | -3,06% | +26,73% | FEEDBACK RAPIDO |
| BTC | 60g | Global confluence | BENCHMARK | 7 | 100,00% | +23,11% | +23,11% | -2,47% | +29,48% | FEEDBACK RAPIDO |
| BTC | 60g | Famiglia statistica | CALIBRABILE | 7 | 100,00% | +23,11% | +23,11% | -2,47% | +29,48% | FEEDBACK RAPIDO |
| BTC | 60g | Scanner grezzo | DIAGNOSTICO | 7 | 100,00% | +23,11% | +23,11% | -2,47% | +29,48% | FEEDBACK RAPIDO |
| BTC | 60g | Market regime grezzo | DIAGNOSTICO | 7 | 100,00% | +23,11% | +23,11% | -2,47% | +29,48% | FEEDBACK RAPIDO |
| BTC | 60g | Tecnico | CALIBRABILE | 6 | 50,00% | +23,08% | -1,25% | -2,34% | +29,59% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 60 | 43,33% | +0,37% | +0,06% | -0,28% | +1,33% | UTILE |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 63 | 57,14% | +0,27% | +0,50% | -0,40% | +1,17% | UTILE |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 63 | 57,14% | +0,27% | +0,50% | -0,40% | +1,17% | UTILE |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,15% | +0,26% | -0,32% | +0,87% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Tecnico | CALIBRABILE | 57 | 50,88% | +0,18% | +0,38% | -0,51% | +1,07% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Classic technical | CALIBRABILE | 36 | 38,89% | +0,24% | -0,49% | -0,39% | +0,95% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 55,56% | +2,13% | +1,78% | +0,65% | +2,81% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 59 | 44,07% | +0,74% | +0,17% | -0,05% | +1,97% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 62 | 56,45% | +0,55% | +0,84% | -0,22% | +1,70% | UTILE |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 62 | 56,45% | +0,55% | +0,84% | -0,22% | +1,70% | UTILE |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 38 | 50,00% | +0,36% | +0,74% | -0,26% | +1,41% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Tecnico | CALIBRABILE | 56 | 53,57% | +0,17% | +0,53% | -0,59% | +1,30% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Classic technical | CALIBRABILE | 35 | 40,00% | +0,47% | -1,26% | -0,28% | +1,41% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 44,44% | +2,90% | +2,61% | +2,02% | +4,90% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 58 | 39,66% | +1,07% | +0,39% | -1,85% | +4,08% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 61 | 55,74% | +0,88% | +1,25% | -1,98% | +3,73% | UTILE |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 61 | 55,74% | +0,88% | +1,25% | -1,98% | +3,73% | UTILE |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,84% | +1,55% | -1,48% | +3,36% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Tecnico | CALIBRABILE | 55 | 45,45% | +0,07% | +0,42% | -2,26% | +2,83% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Classic technical | CALIBRABILE | 34 | 29,41% | +0,82% | -2,31% | -2,19% | +3,95% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 44,44% | +2,49% | +2,26% | -0,95% | +6,11% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 56 | 46,43% | +1,90% | +1,30% | -2,73% | +6,43% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 59 | 50,85% | +1,76% | +2,02% | -2,80% | +6,16% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 59 | 50,85% | +1,76% | +2,02% | -2,80% | +6,16% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +2,45% | +3,08% | -2,17% | +5,74% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Tecnico | CALIBRABILE | 53 | 56,60% | +0,72% | +0,48% | -3,25% | +5,15% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Classic technical | CALIBRABILE | 34 | 35,29% | +1,67% | -4,23% | -3,21% | +6,23% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 33,33% | +0,52% | +0,34% | -2,37% | +7,26% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 54 | 59,26% | +2,54% | +2,88% | -3,06% | +8,38% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 57 | 56,14% | +2,57% | +2,55% | -3,13% | +8,16% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 57 | 56,14% | +2,57% | +2,55% | -3,13% | +8,16% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,59% | +4,60% | -2,54% | +8,00% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Tecnico | CALIBRABILE | 51 | 56,86% | +1,26% | +1,28% | -3,66% | +6,80% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Classic technical | CALIBRABILE | 32 | 37,50% | +2,47% | -4,86% | -3,47% | +7,93% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 44,44% | -0,37% | -0,49% | -2,97% | +7,69% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 51 | 54,90% | +2,92% | +3,67% | -3,49% | +9,93% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 54 | 50,00% | +2,84% | +2,88% | -3,54% | +9,74% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 54 | 50,00% | +2,84% | +2,88% | -3,54% | +9,74% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,79% | +5,36% | -2,91% | +9,59% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Tecnico | CALIBRABILE | 48 | 66,67% | +1,00% | +1,79% | -4,15% | +7,58% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Classic technical | CALIBRABILE | 31 | 41,94% | +2,22% | -4,39% | -3,95% | +9,25% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 62,50% | +0,72% | +0,35% | -3,12% | +9,19% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 48 | 66,67% | +4,76% | +6,71% | -4,04% | +13,21% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 50 | 74,00% | +4,32% | +6,43% | -4,08% | +12,70% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 50 | 74,00% | +4,32% | +6,43% | -4,08% | +12,70% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 38 | 76,32% | +5,76% | +8,06% | -3,33% | +13,70% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Tecnico | CALIBRABILE | 44 | 59,09% | +1,29% | +0,89% | -4,83% | +8,72% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Classic technical | CALIBRABILE | 31 | 48,39% | +3,26% | -3,87% | -4,53% | +11,11% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 50,00% | +6,58% | +1,67% | -3,33% | +14,96% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 42 | 76,19% | +9,09% | +8,15% | -3,59% | +19,67% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 44 | 84,09% | +9,14% | +11,83% | -3,63% | +19,75% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 44 | 84,09% | +9,14% | +11,83% | -3,63% | +19,75% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 38 | 89,47% | +10,54% | +13,52% | -3,55% | +20,95% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Tecnico | CALIBRABILE | 37 | 62,16% | +6,37% | -3,31% | -4,34% | +15,31% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Classic technical | CALIBRABILE | 29 | 51,72% | +6,17% | -7,05% | -4,21% | +14,94% | FEEDBACK RAPIDO |
| DOGE | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 6 | 66,67% | +9,78% | +0,82% | -1,43% | +23,27% | FEEDBACK RAPIDO |
| DOGE | 30g | Global confluence | BENCHMARK | 33 | 75,76% | +13,03% | +6,27% | -4,23% | +25,66% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Famiglia statistica | CALIBRABILE | 35 | 88,57% | +13,53% | +12,22% | -4,24% | +26,48% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Scanner grezzo | DIAGNOSTICO | 35 | 88,57% | +13,53% | +12,22% | -4,24% | +26,48% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Market regime grezzo | DIAGNOSTICO | 33 | 93,94% | +12,65% | +14,66% | -4,27% | +25,83% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Tecnico | CALIBRABILE | 30 | 40,00% | +11,60% | -11,60% | -4,76% | +23,68% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Classic technical | CALIBRABILE | 23 | 47,83% | +9,94% | -9,94% | -4,66% | +20,37% | FEEDBACK RAPIDO |
| DOGE | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 75,00% | +30,85% | +15,03% | -1,31% | +42,05% | FEEDBACK RAPIDO |
| DOGE | 45g | Global confluence | BENCHMARK | 21 | 19,05% | +20,47% | -12,47% | -5,68% | +38,36% | FEEDBACK RAPIDO |
| DOGE | 45g | Famiglia statistica | CALIBRABILE | 22 | 27,27% | +20,35% | -8,41% | -5,72% | +38,31% | FEEDBACK RAPIDO |
| DOGE | 45g | Scanner grezzo | DIAGNOSTICO | 22 | 27,27% | +20,35% | -8,41% | -5,72% | +38,31% | FEEDBACK RAPIDO |
| DOGE | 45g | Market regime grezzo | DIAGNOSTICO | 20 | 30,00% | +19,57% | -6,42% | -5,92% | +37,98% | FEEDBACK RAPIDO |
| DOGE | 45g | Tecnico | CALIBRABILE | 22 | 0,00% | +20,35% | -20,35% | -5,72% | +38,31% | FEEDBACK RAPIDO |
| DOGE | 45g | Classic technical | CALIBRABILE | 18 | 0,00% | +20,70% | -20,70% | -5,55% | +38,48% | FEEDBACK RAPIDO |
| DOGE | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +30,17% | +30,17% | -1,85% | +44,37% | FEEDBACK RAPIDO |
| DOGE | 60g | Global confluence | BENCHMARK | 7 | 0,00% | +19,08% | -19,08% | -7,01% | +36,77% | FEEDBACK RAPIDO |
| DOGE | 60g | Famiglia statistica | CALIBRABILE | 7 | 0,00% | +19,08% | -19,08% | -7,01% | +36,77% | FEEDBACK RAPIDO |
| DOGE | 60g | Scanner grezzo | DIAGNOSTICO | 7 | 0,00% | +19,08% | -19,08% | -7,01% | +36,77% | FEEDBACK RAPIDO |
| DOGE | 60g | Market regime grezzo | DIAGNOSTICO | 7 | 0,00% | +19,08% | -19,08% | -7,01% | +36,77% | FEEDBACK RAPIDO |
| DOGE | 60g | Tecnico | CALIBRABILE | 7 | 0,00% | +19,08% | -19,08% | -7,01% | +36,77% | FEEDBACK RAPIDO |
| DOGE | 60g | Classic technical | CALIBRABILE | 6 | 0,00% | +19,80% | -19,80% | -6,84% | +37,03% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 57 | 54,39% | +0,57% | +0,46% | -0,14% | +1,44% | PRIMA CALIBRAZIONE |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 59 | 55,93% | +0,30% | +0,29% | -0,34% | +1,15% | PRIMA CALIBRAZIONE |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 62 | 54,84% | +0,34% | +0,22% | -0,31% | +1,18% | UTILE |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +0,27% | +0,39% | -0,30% | +0,87% | PRIMA CALIBRAZIONE |
| SOL | 1g | Tecnico | CALIBRABILE | 59 | 49,15% | +0,27% | +0,25% | -0,43% | +1,09% | PRIMA CALIBRAZIONE |
| SOL | 1g | Classic technical | CALIBRABILE | 42 | 50,00% | +0,49% | +0,45% | -0,33% | +1,40% | PRIMA CALIBRAZIONE |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 56 | 50,00% | +1,13% | +1,01% | +0,21% | +2,18% | PRIMA CALIBRAZIONE |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 58 | 46,55% | +0,79% | +0,38% | -0,14% | +1,60% | PRIMA CALIBRAZIONE |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 61 | 45,90% | +0,77% | +0,34% | -0,14% | +1,66% | UTILE |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +0,76% | +0,78% | -0,00% | +1,60% | PRIMA CALIBRAZIONE |
| SOL | 2g | Tecnico | CALIBRABILE | 59 | 42,37% | +0,68% | +0,16% | -0,20% | +1,73% | PRIMA CALIBRAZIONE |
| SOL | 2g | Classic technical | CALIBRABILE | 42 | 50,00% | +0,75% | +0,73% | -0,18% | +1,69% | PRIMA CALIBRAZIONE |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 55 | 54,55% | +1,76% | +1,60% | -1,52% | +4,08% | PRIMA CALIBRAZIONE |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 57 | 47,37% | +1,31% | +0,80% | -1,80% | +3,62% | PRIMA CALIBRAZIONE |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 60 | 46,67% | +1,26% | +0,74% | -1,77% | +3,61% | UTILE |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +1,43% | +1,38% | -1,48% | +3,53% | PRIMA CALIBRAZIONE |
| SOL | 3g | Tecnico | CALIBRABILE | 59 | 47,46% | +1,12% | +0,01% | -1,84% | +3,37% | PRIMA CALIBRAZIONE |
| SOL | 3g | Classic technical | CALIBRABILE | 42 | 52,38% | +1,01% | +0,88% | -1,83% | +3,26% | PRIMA CALIBRAZIONE |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 53 | 58,49% | +3,05% | +2,95% | -2,17% | +6,47% | PRIMA CALIBRAZIONE |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 55 | 52,73% | +2,43% | +1,44% | -2,45% | +5,84% | PRIMA CALIBRAZIONE |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 58 | 51,72% | +2,34% | +1,33% | -2,43% | +5,74% | PRIMA CALIBRAZIONE |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +2,66% | +2,88% | -2,09% | +5,82% | PRIMA CALIBRAZIONE |
| SOL | 5g | Tecnico | CALIBRABILE | 57 | 47,37% | +2,34% | -0,46% | -2,57% | +5,64% | PRIMA CALIBRAZIONE |
| SOL | 5g | Classic technical | CALIBRABILE | 41 | 56,10% | +1,58% | +1,44% | -2,57% | +4,83% | PRIMA CALIBRAZIONE |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 51 | 62,75% | +4,36% | +4,46% | -2,50% | +8,37% | PRIMA CALIBRAZIONE |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 53 | 58,49% | +3,64% | +2,45% | -2,79% | +7,70% | PRIMA CALIBRAZIONE |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 56 | 58,93% | +3,44% | +2,32% | -2,79% | +7,49% | PRIMA CALIBRAZIONE |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 34 | 61,76% | +4,35% | +4,41% | -2,45% | +7,76% | PRIMA CALIBRAZIONE |
| SOL | 7g | Tecnico | CALIBRABILE | 55 | 41,82% | +3,40% | -1,16% | -2,94% | +7,43% | PRIMA CALIBRAZIONE |
| SOL | 7g | Classic technical | CALIBRABILE | 39 | 51,28% | +1,81% | +1,86% | -3,01% | +5,86% | PRIMA CALIBRAZIONE |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 48 | 66,67% | +6,24% | +6,40% | -2,66% | +10,69% | PRIMA CALIBRAZIONE |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 50 | 62,00% | +5,45% | +4,54% | -3,03% | +9,70% | PRIMA CALIBRAZIONE |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 53 | 60,38% | +5,13% | +4,29% | -3,06% | +9,37% | PRIMA CALIBRAZIONE |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 34 | 64,71% | +6,91% | +6,75% | -2,80% | +10,27% | PRIMA CALIBRAZIONE |
| SOL | 10g | Tecnico | CALIBRABILE | 52 | 48,08% | +4,57% | -1,90% | -3,24% | +8,97% | PRIMA CALIBRAZIONE |
| SOL | 10g | Classic technical | CALIBRABILE | 36 | 58,33% | +1,94% | +2,04% | -3,32% | +6,67% | PRIMA CALIBRAZIONE |
| SOL | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 80,00% | +3,41% | +3,41% | -2,87% | +9,17% | FEEDBACK RAPIDO |
| SOL | 10g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 14g | Global confluence | BENCHMARK | 44 | 75,00% | +9,34% | +10,17% | -2,90% | +15,08% | PRIMA CALIBRAZIONE |

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

Generato: 2026-09-13 05:33 UTC

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
| BTC | 65 | UTILE | 64 | 18 | 4 | 0 | Famiglia statistica | 1g | 53,12% | +0,33% | campione utile, valutare con prudenza |
| SOL | 65 | PRIMA CALIBRAZIONE | 59 | 25 | 0 | 0 | Famiglia statistica | 1g | 55,93% | +0,29% | prima calibrazione possibile, solo modifiche leggere |
| DOGE | 65 | UTILE | 63 | 25 | 3 | 0 | Famiglia statistica | 1g | 57,14% | +0,50% | campione utile, valutare con prudenza |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Classic technical | 24 | 37,50% | +0,37% | +0,81% | +0,13% | +1,33% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Famiglia statistica | 64 | 53,12% | +0,33% | +0,33% | -0,10% | +0,84% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 1g | BREVE | Microstruttura exchange | 5 | 40,00% | -0,17% | -0,17% | -0,60% | +0,27% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 59 | 40,68% | +0,09% | +0,44% | -0,01% | +0,95% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 2g | BREVE | Classic technical | 24 | 41,67% | +0,55% | +1,18% | +0,59% | +1,89% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Famiglia statistica | 63 | 52,38% | +0,69% | +0,69% | +0,13% | +1,35% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 2g | BREVE | Microstruttura exchange | 5 | 40,00% | +0,73% | +0,73% | +0,13% | +1,27% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 58 | 43,10% | +0,13% | +0,84% | +0,28% | +1,49% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 3g | BREVE | Classic technical | 24 | 41,67% | +0,20% | +1,81% | -0,58% | +3,31% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Famiglia statistica | 62 | 51,61% | +1,03% | +1,03% | -1,07% | +2,69% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 3g | BREVE | Microstruttura exchange | 5 | 40,00% | +0,35% | +0,35% | -1,11% | +1,90% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 57 | 35,09% | -0,19% | +1,29% | -0,92% | +2,93% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 5g | SETTIMANALE | Classic technical | 24 | 50,00% | -1,14% | +3,70% | -1,03% | +5,94% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 60 | 50,00% | +1,83% | +1,83% | -1,63% | +4,20% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 5g | SETTIMANALE | Microstruttura exchange | 5 | 20,00% | -0,98% | -0,98% | -2,20% | +2,18% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 55 | 41,82% | -0,98% | +2,10% | -1,46% | +4,51% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 7g | SETTIMANALE | Classic technical | 24 | 45,83% | -2,81% | +4,87% | -1,33% | +8,02% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 58 | 58,62% | +2,59% | +2,59% | -1,87% | +5,39% | PESO OK | 0,0 | MEDIA |
| BTC | 7g | SETTIMANALE | Microstruttura exchange | 5 | 40,00% | -1,21% | -1,21% | -3,03% | +2,32% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 53 | 41,51% | -1,77% | +3,04% | -1,69% | +5,80% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 10g | SETTIMANALE | Classic technical | 23 | 52,17% | -3,56% | +5,61% | -1,40% | +9,17% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 55 | 63,64% | +3,53% | +3,53% | -2,01% | +6,63% | PESO OK | 0,0 | MEDIA |
| BTC | 10g | SETTIMANALE | Microstruttura exchange | 3 | 66,67% | +0,54% | +0,54% | -2,46% | +3,88% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 50 | 46,00% | -1,32% | +4,00% | -1,79% | +7,18% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 14g | SWING | Classic technical | 19 | 36,84% | -3,97% | +6,37% | -1,30% | +10,56% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Famiglia statistica | 51 | 58,82% | +5,24% | +5,24% | -2,16% | +8,83% | PESO OK | 0,0 | MEDIA |
| BTC | 14g | SWING | Microstruttura exchange | 3 | 33,33% | -0,03% | -0,03% | -2,90% | +4,64% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 46 | 54,35% | +0,68% | +5,94% | -1,91% | +9,61% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 21g | SWING | Classic technical | 12 | 33,33% | -11,49% | +14,30% | -0,25% | +18,32% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Famiglia statistica | 44 | 72,73% | +9,73% | +9,73% | -2,08% | +13,66% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| BTC | 21g | SWING | Microstruttura exchange | 2 | 100,00% | +1,26% | +1,26% | -1,61% | +6,04% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Tecnico | 39 | 41,03% | -0,91% | +10,77% | -1,78% | +14,79% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 30g | MEDIO | Classic technical | 5 | 0,00% | -23,88% | +23,88% | -1,27% | +29,00% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Famiglia statistica | 35 | 85,71% | +14,07% | +14,07% | -2,92% | +18,26% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| BTC | 30g | MEDIO | Microstruttura exchange | 1 | 100,00% | +0,16% | +0,16% | -3,06% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Tecnico | 30 | 43,33% | -2,29% | +14,30% | -2,66% | +18,83% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 45g | MEDIO | Classic technical | 2 | 0,00% | -21,18% | +21,18% | -2,23% | +29,25% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Famiglia statistica | 22 | 100,00% | +22,27% | +22,27% | -3,21% | +26,86% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Microstruttura exchange | 1 | 100,00% | +20,42% | +20,42% | -3,06% | +26,73% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Tecnico | 18 | 27,78% | -10,08% | +22,53% | -2,87% | +27,34% | OSSERVA | 0,0 | BASSA |
| BTC | 60g | MEDIO | Famiglia statistica | 7 | 100,00% | +23,11% | +23,11% | -2,47% | +29,48% | OSSERVA | 0,0 | BASSA |
| BTC | 60g | MEDIO | Tecnico | 6 | 50,00% | -1,25% | +23,08% | -2,34% | +29,59% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 36 | 38,89% | -0,49% | +0,24% | -0,39% | +0,95% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 1g | BREVE | Famiglia statistica | 63 | 57,14% | +0,50% | +0,27% | -0,40% | +1,17% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 1g | BREVE | Microstruttura exchange | 9 | 55,56% | +1,78% | +2,13% | +0,65% | +2,81% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 57 | 50,88% | +0,38% | +0,18% | -0,51% | +1,07% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Classic technical | 35 | 40,00% | -1,26% | +0,47% | -0,28% | +1,41% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 2g | BREVE | Famiglia statistica | 62 | 56,45% | +0,84% | +0,55% | -0,22% | +1,70% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 2g | BREVE | Microstruttura exchange | 9 | 44,44% | +2,61% | +2,90% | +2,02% | +4,90% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 56 | 53,57% | +0,53% | +0,17% | -0,59% | +1,30% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 3g | BREVE | Classic technical | 34 | 29,41% | -2,31% | +0,82% | -2,19% | +3,95% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 3g | BREVE | Famiglia statistica | 61 | 55,74% | +1,25% | +0,88% | -1,98% | +3,73% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 3g | BREVE | Microstruttura exchange | 9 | 44,44% | +2,26% | +2,49% | -0,95% | +6,11% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 55 | 45,45% | +0,42% | +0,07% | -2,26% | +2,83% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 5g | SETTIMANALE | Classic technical | 34 | 35,29% | -4,23% | +1,67% | -3,21% | +6,23% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 59 | 50,85% | +2,02% | +1,76% | -2,80% | +6,16% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 5g | SETTIMANALE | Microstruttura exchange | 9 | 33,33% | +0,34% | +0,52% | -2,37% | +7,26% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 53 | 56,60% | +0,48% | +0,72% | -3,25% | +5,15% | PESO OK | 0,0 | MEDIA |
| DOGE | 7g | SETTIMANALE | Classic technical | 32 | 37,50% | -4,86% | +2,47% | -3,47% | +7,93% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 57 | 56,14% | +2,55% | +2,57% | -3,13% | +8,16% | PESO OK | 0,0 | MEDIA |
| DOGE | 7g | SETTIMANALE | Microstruttura exchange | 9 | 44,44% | -0,49% | -0,37% | -2,97% | +7,69% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 51 | 56,86% | +1,28% | +1,26% | -3,66% | +6,80% | PESO OK | 0,0 | MEDIA |
| DOGE | 10g | SETTIMANALE | Classic technical | 31 | 41,94% | -4,39% | +2,22% | -3,95% | +9,25% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 54 | 50,00% | +2,88% | +2,84% | -3,54% | +9,74% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 10g | SETTIMANALE | Microstruttura exchange | 8 | 62,50% | +0,35% | +0,72% | -3,12% | +9,19% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 48 | 66,67% | +1,79% | +1,00% | -4,15% | +7,58% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 14g | SWING | Classic technical | 31 | 48,39% | -3,87% | +3,26% | -4,53% | +11,11% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 14g | SWING | Famiglia statistica | 50 | 74,00% | +6,43% | +4,32% | -4,08% | +12,70% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 14g | SWING | Microstruttura exchange | 8 | 50,00% | +1,67% | +6,58% | -3,33% | +14,96% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 44 | 59,09% | +0,89% | +1,29% | -4,83% | +8,72% | PESO OK | 0,0 | MEDIA |
| DOGE | 21g | SWING | Classic technical | 29 | 51,72% | -7,05% | +6,17% | -4,21% | +14,94% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Famiglia statistica | 44 | 84,09% | +11,83% | +9,14% | -3,63% | +19,75% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 21g | SWING | Microstruttura exchange | 6 | 66,67% | +0,82% | +9,78% | -1,43% | +23,27% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Tecnico | 37 | 62,16% | -3,31% | +6,37% | -4,34% | +15,31% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 30g | MEDIO | Classic technical | 23 | 47,83% | -9,94% | +9,94% | -4,66% | +20,37% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Famiglia statistica | 35 | 88,57% | +12,22% | +13,53% | -4,24% | +26,48% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 30g | MEDIO | Microstruttura exchange | 4 | 75,00% | +15,03% | +30,85% | -1,31% | +42,05% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Tecnico | 30 | 40,00% | -11,60% | +11,60% | -4,76% | +23,68% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 45g | MEDIO | Classic technical | 18 | 0,00% | -20,70% | +20,70% | -5,55% | +38,48% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Famiglia statistica | 22 | 27,27% | -8,41% | +20,35% | -5,72% | +38,31% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Microstruttura exchange | 2 | 100,00% | +30,17% | +30,17% | -1,85% | +44,37% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Tecnico | 22 | 0,00% | -20,35% | +20,35% | -5,72% | +38,31% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Classic technical | 6 | 0,00% | -19,80% | +19,80% | -6,84% | +37,03% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Famiglia statistica | 7 | 0,00% | -19,08% | +19,08% | -7,01% | +36,77% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Tecnico | 7 | 0,00% | -19,08% | +19,08% | -7,01% | +36,77% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Classic technical | 42 | 50,00% | +0,45% | +0,49% | -0,33% | +1,40% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 1g | BREVE | Famiglia statistica | 59 | 55,93% | +0,29% | +0,30% | -0,34% | +1,15% | PESO OK | 0,0 | MEDIA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 59 | 49,15% | +0,25% | +0,27% | -0,43% | +1,09% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Classic technical | 42 | 50,00% | +0,73% | +0,75% | -0,18% | +1,69% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Famiglia statistica | 58 | 46,55% | +0,38% | +0,79% | -0,14% | +1,60% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Microstruttura exchange | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 59 | 42,37% | +0,16% | +0,68% | -0,20% | +1,73% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Classic technical | 42 | 52,38% | +0,88% | +1,01% | -1,83% | +3,26% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Famiglia statistica | 57 | 47,37% | +0,80% | +1,31% | -1,80% | +3,62% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Microstruttura exchange | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 59 | 47,46% | +0,01% | +1,12% | -1,84% | +3,37% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Classic technical | 41 | 56,10% | +1,44% | +1,58% | -2,57% | +4,83% | PESO OK | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 55 | 52,73% | +1,44% | +2,43% | -2,45% | +5,84% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 57 | 47,37% | -0,46% | +2,34% | -2,57% | +5,64% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Classic technical | 39 | 51,28% | +1,86% | +1,81% | -3,01% | +5,86% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 53 | 58,49% | +2,45% | +3,64% | -2,79% | +7,70% | PESO OK | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 55 | 41,82% | -1,16% | +3,40% | -2,94% | +7,43% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 10g | SETTIMANALE | Classic technical | 36 | 58,33% | +2,04% | +1,94% | -3,32% | +6,67% | PESO OK | 0,0 | MEDIA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 50 | 62,00% | +4,54% | +5,45% | -3,03% | +9,70% | PESO OK | 0,0 | MEDIA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Microstruttura exchange | 5 | 80,00% | +3,41% | +3,41% | -2,87% | +9,17% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 52 | 48,08% | -1,90% | +4,57% | -3,24% | +8,97% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 14g | SWING | Classic technical | 32 | 50,00% | +1,32% | +2,88% | -3,62% | +7,75% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 14g | SWING | Famiglia statistica | 46 | 76,09% | +7,96% | +8,85% | -3,21% | +13,94% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 14g | SWING | Frattale SOL | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Microstruttura exchange | 5 | 80,00% | +8,16% | +8,16% | -3,30% | +14,31% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Tecnico | 48 | 39,58% | -4,36% | +6,74% | -3,51% | +12,10% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 21g | SWING | Classic technical | 25 | 48,00% | -7,41% | +11,38% | -3,75% | +16,41% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Famiglia statistica | 39 | 79,49% | +16,55% | +16,62% | -3,45% | +22,47% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 21g | SWING | Frattale SOL | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Microstruttura exchange | 3 | 66,67% | +15,44% | +15,44% | -3,34% | +22,79% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Tecnico | 41 | 39,02% | -11,99% | +13,40% | -3,94% | +19,22% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 30g | MEDIO | Classic technical | 21 | 9,52% | -26,53% | +26,53% | -4,64% | +32,91% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Famiglia statistica | 31 | 90,32% | +24,63% | +24,97% | -4,79% | +31,59% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 30g | MEDIO | Frattale SOL | 1 | 0,00% | -4,50% | -4,50% | -9,39% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Microstruttura exchange | 2 | 100,00% | +22,28% | +22,28% | -5,94% | +27,20% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Tecnico | 33 | 12,12% | -21,93% | +21,36% | -5,20% | +27,41% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 45g | MEDIO | Classic technical | 14 | 0,00% | -36,41% | +36,41% | -6,13% | +46,12% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Famiglia statistica | 18 | 55,56% | +7,27% | +33,58% | -6,94% | +42,15% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Frattale SOL | 1 | 100,00% | +19,26% | +19,26% | -9,39% | +23,73% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Microstruttura exchange | 1 | 100,00% | +32,54% | +32,54% | -9,62% | +40,68% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Tecnico | 22 | 18,18% | -25,10% | +34,05% | -6,93% | +42,20% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Famiglia statistica | 5 | 20,00% | -20,14% | +32,67% | -8,45% | +42,50% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Frattale SOL | 1 | 100,00% | +35,29% | +35,29% | -9,39% | +41,04% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Tecnico | 7 | 57,14% | +5,48% | +33,27% | -8,15% | +42,97% | OSSERVA | 0,0 | BASSA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 61 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 38 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 64 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Classic technical | 72 | 40,28% | +0,37% |
| BTC | BREVE | Famiglia statistica | 189 | 52,38% | +0,68% |
| BTC | BREVE | Microstruttura exchange | 15 | 40,00% | +0,30% |
| BTC | BREVE | Tecnico | 174 | 39,66% | +0,01% |
| BTC | SETTIMANALE | Classic technical | 71 | 49,30% | -2,49% |
| BTC | SETTIMANALE | Famiglia statistica | 173 | 57,23% | +2,63% |
| BTC | SETTIMANALE | Microstruttura exchange | 13 | 38,46% | -0,72% |
| BTC | SETTIMANALE | Tecnico | 158 | 43,04% | -1,35% |
| BTC | SWING | Classic technical | 31 | 35,48% | -6,88% |
| BTC | SWING | Famiglia statistica | 95 | 65,26% | +7,32% |
| BTC | SWING | Microstruttura exchange | 5 | 60,00% | +0,49% |
| BTC | SWING | Tecnico | 85 | 48,24% | -0,05% |
| BTC | MEDIO | Classic technical | 7 | 0,00% | -23,11% |
| BTC | MEDIO | Famiglia statistica | 64 | 92,19% | +17,88% |
| BTC | MEDIO | Microstruttura exchange | 2 | 100,00% | +10,29% |
| BTC | MEDIO | Tecnico | 54 | 38,89% | -4,77% |
| DOGE | BREVE | Classic technical | 105 | 36,19% | -1,34% |
| DOGE | BREVE | Famiglia statistica | 186 | 56,45% | +0,86% |
| DOGE | BREVE | Microstruttura exchange | 27 | 48,15% | +2,22% |
| DOGE | BREVE | Tecnico | 168 | 50,00% | +0,44% |
| DOGE | SETTIMANALE | Classic technical | 97 | 38,14% | -4,49% |
| DOGE | SETTIMANALE | Famiglia statistica | 170 | 52,35% | +2,47% |
| DOGE | SETTIMANALE | Microstruttura exchange | 26 | 46,15% | +0,05% |
| DOGE | SETTIMANALE | Tecnico | 152 | 59,87% | +1,16% |
| DOGE | SWING | Classic technical | 60 | 50,00% | -5,41% |
| DOGE | SWING | Famiglia statistica | 94 | 78,72% | +8,95% |
| DOGE | SWING | Microstruttura exchange | 14 | 57,14% | +1,30% |
| DOGE | SWING | Tecnico | 81 | 60,49% | -1,03% |
| DOGE | MEDIO | Classic technical | 47 | 23,40% | -15,32% |
| DOGE | MEDIO | Famiglia statistica | 64 | 57,81% | +1,71% |
| DOGE | MEDIO | Microstruttura exchange | 6 | 83,33% | +20,07% |
| DOGE | MEDIO | Tecnico | 59 | 20,34% | -15,75% |
| SOL | BREVE | Classic technical | 126 | 50,79% | +0,69% |
| SOL | BREVE | Famiglia statistica | 174 | 50,00% | +0,48% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 15 | 53,33% | +1,74% |
| SOL | BREVE | Tecnico | 177 | 46,33% | +0,14% |
| SOL | SETTIMANALE | Classic technical | 116 | 55,17% | +1,77% |
| SOL | SETTIMANALE | Famiglia statistica | 158 | 57,59% | +2,76% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Microstruttura exchange | 15 | 66,67% | +3,06% |
| SOL | SETTIMANALE | Tecnico | 164 | 45,73% | -1,15% |
| SOL | SWING | Classic technical | 57 | 49,12% | -2,51% |
| SOL | SWING | Famiglia statistica | 85 | 77,65% | +11,90% |
| SOL | SWING | Frattale SOL | 2 | 0,00% | -3,49% |
| SOL | SWING | Microstruttura exchange | 8 | 75,00% | +10,89% |
| SOL | SWING | Tecnico | 89 | 39,33% | -7,87% |
| SOL | MEDIO | Classic technical | 35 | 5,71% | -30,49% |
| SOL | MEDIO | Famiglia statistica | 54 | 72,22% | +14,70% |
| SOL | MEDIO | Frattale SOL | 3 | 66,67% | +16,68% |
| SOL | MEDIO | Microstruttura exchange | 3 | 100,00% | +25,70% |
| SOL | MEDIO | Tecnico | 62 | 19,35% | -19,96% |

## Aree ancora in attesa

| Asset | Famiglia | Righe senza controlli | Stato |
| --- | --- | --- | --- |
| BTC | BREVE | 3 | in attesa di controlli maturati |
| BTC | SETTIMANALE | 3 | in attesa di controlli maturati |
| BTC | SWING | 2 | in attesa di controlli maturati |
| BTC | MEDIO | 5 | in attesa di controlli maturati |
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
| BTC     |         65 |              35 |          30 | OSSERVAZIONE 30+ | 0,00%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| SOL     |         65 |              35 |          30 | OSSERVAZIONE 30+ | 2,86%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| DOGE    |         65 |              35 |          30 | OSSERVAZIONE 30+ | 5,71%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |

Regola: sotto 60 controlli osserva soltanto; da 100+ controlli può diventare utile per correggere rischio spot/leva nel Decision Report.

## Ultima lettura rapida

| Asset   | Rischio spot   | Rischio leva   | Nota leva                                                               |
|:--------|:---------------|:---------------|:------------------------------------------------------------------------|
| BTC     | BASSO          | ALTO           | spot preferibile; leva molto pericolosa anche 2x/3x senza margine largo |
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

Generato: 2026-09-13 05:33 UTC


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
| SOL | +4 | MODERATAMENTE POSITIVA | Costruttivo prudente | MEDIA | HOLD / TRANCHE PICCOLE, NO LEVA | Doppio minimo target raggiunto finché mantiene 78,73; nuova conferma tecnica sopra 107,12; milestone analogiche 108,90 / 134,15, valide soltanto se rientra anche il gap frattale. | Allarmi sotto 88,83 / 97,45 / 62,19. |
| DOGE | -5 | NEGATIVA | Ribassista | MEDIA | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE | Sopra 0.09421 migliora; sopra 0.06933 viene invalidato il pattern ribassista dominante. | Sotto 0.08028 il rischio ribassista aumenta. |

## Punteggi per modulo

| Asset | Scanner grezzo | Market grezzo | Famiglia statistica | Scanner path | Tecnico | Classic tech | Frattale SOL | Fractal path | RSI top-cycle | Lifecycle EMA | Exchange flow | Futures | Daily change | Totale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +3 | 0 | +3 | 0 | +2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | +1 | +6 |
| SOL | +3 | 0 | +3 | 0 | +1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | +4 |
| DOGE | -2 | 0 | -2 | 0 | -2 | -1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | -5 |

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
- Scanner (diagnostico, già incluso nella Famiglia statistica): **+3** — Casi positivi 85,00%, return centrale 30g +36,97%. Direzione scanner: SALITA. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **0** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 0, positivi 30g n/a, return p50 n/a.
- Scanner path: **0** — Controlli disponibili 62. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **+2** — Score tecnico 3/12, verdetto costruttivo ma non confermato, trend misto, struttura rialzista con massimi e minimi crescenti, divergenza nessuna, Wyckoff markup / fase rialzista, pattern score 0 (rialzista Doppio minimo / TARGET RAGGIUNTO; ribassista Doppio massimo / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **0** — Score classico -3/12, verdetto DEBOLE / NON CONFERMATO, stage STAGE 3 / DISTRIBUZIONE O PAUSA, struttura VOLATILITÀ IN ESPANSIONE, Wyckoff RANGE / FASE NON CHIARA, volatilità locale MEDIO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Non applicabile a questo asset.
- Fractal path: **0** — Non applicabile a questo asset.
- RSI top-cycle: **0** — Non applicabile a questo asset.
- Lifecycle EMA: **0** — Non applicabile a questo asset.
- Exchange flow: **0** — Flow +1.75, derivati +0.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +1.00; exchange 3/3, copertura 100%, consenso bull 1, bear 0, divergenze 0, campioni 4h 9 su 4.00h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias LEGGERMENTE POSITIVA / NON PESATA; confidenza MEDIA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Rischio sotto, forza 2/5.
- Daily change: **+1** — BTC: cambiamento medio in miglioramento rispetto a ieri.

Conferme: Prima resistenza sopra 82.262; conferma del doppio minimo sopra 65.402.

Invalidazioni: Sotto 76.248 il quadro tecnico peggiora.

### SOL

- Confluenza: **MODERATAMENTE POSITIVA**
- Bias: **Costruttivo prudente**
- Punteggio finale: **+4**
- Affidabilità: **MEDIA**
- Azione coerente: **HOLD / TRANCHE PICCOLE, NO LEVA**

SOL ha una confluenza costruttiva, ma va ancora trattato come setup anticipato. La conferma vera arriva solo sopra le resistenze tecniche e con rientro del gap frattale. Il modulo lifecycle/EMA200 resta utile come contesto, ma non aumenta il punteggio Global.

Dettaglio moduli:

- Famiglia statistica: **+3** — Scanner grezzo +3, Market Regime grezzo 0, match regime 0. Regime ignorato: meno di 5 match utili. Punteggio contato nel Global: +3.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **+3** — Casi positivi 67,50%, return centrale 30g +33,19%. Direzione scanner: SALITA. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **0** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 0, positivi 30g n/a, return p50 n/a.
- Scanner path: **0** — Controlli disponibili 62. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **+1** — Score tecnico 1/12, verdetto neutrale / misto, trend misto, struttura compressione / triangolo, divergenza nessuna, Wyckoff markup / fase rialzista, pattern score 0 (rialzista Doppio minimo / TARGET RAGGIUNTO; ribassista Doppio massimo / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **0** — Score classico 0/12, verdetto NEUTRALE / MISTO, stage STAGE 3 / DISTRIBUZIONE O PAUSA, struttura COMPRESSIONE / TRIANGOLO POSSIBILE, Wyckoff SIGN OF STRENGTH POSSIBILE, volatilità locale BASSO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Verdetto ANALOGIA DEBOLE / SCENARIO SECONDARIO, somiglianza strutturale +70,17%, aderenza live +72,50%, errore live +13,75%, gap corrente +11,71%, peso operativo 0, tracking STRUTTURA STABILE, fase FRATTALE SOLO DI CONTESTO, rischio ALTO.
- Fractal path: **0** — Controlli disponibili 59, ma percorso ancorato non aderente: gap +11,71%, errore live +13,75%. Peso 0.
- RSI top-cycle: **0** — Rischio top-cycle RSI: BASSO.
- Lifecycle EMA: **0** — Contesto non pesato nel Global. Lifecycle score 2, bias CONTESTO DA OSSERVARE, EMA200 111,24 $, upside EMA200 +9,25%, gap EMA50/EMA200 -5,74%, hit EMA200 12w +73,33%, trend STABILE / DA CONFERMARE. Peso Global forzato a 0.
- Exchange flow: **0** — Flow +2.00, derivati +0.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +0.00; exchange 3/3, copertura 100%, consenso bull 2, bear 0, divergenze 0, campioni 4h 9 su 4.00h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias LEGGERMENTE POSITIVA / NON PESATA; confidenza BASSA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Rischio sotto, forza 2/5.
- Daily change: **0** — SOL: nessun cambiamento forte in miglioramento rispetto a ieri.

Conferme: Doppio minimo target raggiunto finché mantiene 78,73; nuova conferma tecnica sopra 107,12; milestone analogiche 108,90 / 134,15, valide soltanto se rientra anche il gap frattale.

Invalidazioni: Allarmi sotto 88,83 / 97,45 / 62,19.

### DOGE

- Confluenza: **NEGATIVA**
- Bias: **Ribassista**
- Punteggio finale: **-5**
- Affidabilità: **MEDIA**
- Azione coerente: **STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE**

DOGE resta l'asset più debole. Anche senza contare due volte Scanner e Market Regime, la confluenza generale resta chiaramente negativa rispetto a BTC e SOL.

Dettaglio moduli:

- Famiglia statistica: **-2** — Scanner grezzo -2, Market Regime grezzo 0, match regime 0. Regime ignorato: meno di 5 match utili. Punteggio contato nel Global: -2.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **-2** — Casi positivi 25,00%, return centrale 30g -14,87%. Direzione scanner: DISCESA. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **0** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 0, positivi 30g n/a, return p50 n/a.
- Scanner path: **0** — Controlli disponibili 62. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **-2** — Score tecnico -6/12, verdetto debole, trend misto, struttura compressione / triangolo, divergenza nessuna, Wyckoff range / fase non chiara, pattern score 0 (rialzista Doppio minimo / TARGET RAGGIUNTO; ribassista Doppio massimo / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **-1** — Score classico -7/12, verdetto RIBASSISTA / FRAGILE, stage STAGE 4 / MARKDOWN, struttura COMPRESSIONE / TRIANGOLO POSSIBILE, Wyckoff ACCUMULO POSSIBILE / RANGE BASSO, volatilità locale MEDIO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Non applicabile a questo asset.
- Fractal path: **0** — Non applicabile a questo asset.
- RSI top-cycle: **0** — Non applicabile a questo asset.
- Lifecycle EMA: **0** — Non applicabile a questo asset.
- Exchange flow: **0** — Flow +1.75, derivati +0.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +0.50; exchange 3/3, copertura 100%, consenso bull 0, bear 2, divergenze 0, campioni 4h 9 su 4.00h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias LEGGERMENTE POSITIVA / NON PESATA; confidenza BASSA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Rischio sotto, forza 2/5.
- Daily change: **0** — DOGE: nessun cambiamento forte in misto rispetto a ieri.

Conferme: Sopra 0.09421 migliora; sopra 0.06933 viene invalidato il pattern ribassista dominante.

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

Generato: 2026-09-13 05:33 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [btc_macro_cycle_report.md](btc_macro_cycle_report.md)

Questo modulo descrive il contesto macro di Bitcoin. Non genera entrate tattiche, non autorizza leva e pesa **0** nel Global Confluence.

## Sintesi

| Voce | Valore | Lettura |
| --- | --- | --- |
| Prezzo BTC | 77.275 $ | prezzo corrente |
| Power Law centrale | 125.234 $ | deviazione -38,30% |
| Banda p10-p90 | 77.701 $ / 315.510 $ | SOTTO LA BANDA P10 |
| Percentile residuo | 9,43% | posizione storica nel corridoio |
| Esponente β | 5,8011 | R² log-log 91,93% |
| Stabilità β | BASSA | range 1,3167 cambiando finestra |
| Ultimo halving | 2024-04-19 | 877 giorni fa |
| Fase ciclo | 60,03% | percentuale indicativa del ciclo quadriennale |
| Peso Global | 0 | CONTESTO MACRO / DIAGNOSTICO |

La Power Law viene trattata come regressione empirica, non come legge fisica. Il report mostra quanto cambia l'esponente usando finestre iniziali diverse e la confronta con il benchmark ingenuo 'prezzo invariato'.

## Bitcoin Power Law

- Campione: 2014-09-17 → 2026-09-13 (4379 osservazioni)
- Formula stimata: prezzo ≈ exp(-39.0376) × giorni^5.8011
- Prezzo centrale oggi: **125.234 $**
- Posizione corrente: **SOTTO LA BANDA P10**, percentile 9,43%
- Scarto dal centro: **-38,30%**

![Bitcoin Power Law](btc_power_law_chart.png)

![Bitcoin Power Law log-log](btc_power_law_loglog_chart.png)

### Stabilità dell'esponente

| Inizio campione | β | R² log-log |
| --- | --- | --- |
| 2014 | 5,8011 | 91,93% |
| 2015 | 5,8830 | 91,48% |
| 2016 | 5,5666 | 87,74% |
| 2017 | 4,8394 | 82,93% |
| 2018 | 4,5663 | 78,45% |

### Backtest walk-forward contro prezzo invariato

| Orizzonte | Controlli | Vittorie vs naive | Errore mediano modello | Errore mediano naive |
| --- | --- | --- | --- | --- |
| 90g | 81 | 28,40% | 50,97% | 20,89% |
| 180g | 81 | 41,98% | 59,41% | 47,18% |
| 365g | 81 | 58,02% | 72,28% | 81,57% |
| 730g | 81 | 58,02% | 72,72% | 108,81% |

## Bitcoin Four-Year Spiral

Nel grafico l'angolo rappresenta il tempo dentro una finestra di quattro anni e il raggio rappresenta il prezzo in scala logaritmica. ATH, bottom storici e halving sono marker descrittivi: la spirale rende visibili le ricorrenze, ma non dimostra che il ciclo futuro debba ripetersi.

![Bitcoin Four-Year Spiral](bitcoin_four_year_spiral.png)

## Stessa fase dei cicli halving precedenti

| Ciclo | Data analoga | +30g | +90g | +180g | +365g |
| --- | --- | --- | --- | --- | --- |
| 2012-11-28 → 2016-07-09 | 2015-01-29 | +8,89% | -3,30% | +26,09% | +62,51% |
| 2016-07-09 → 2020-05-11 | 2018-10-29 | -32,77% | -43,40% | -16,81% | +48,87% |
| 2020-05-11 → 2024-04-19 | 2022-09-22 | -1,06% | -13,37% | +45,13% | +36,91% |

Campione molto piccolo: questi rendimenti sono contesto di ciclo, non probabilità affidabili.

## SOL/BTC e DOGE/BTC dentro il tempo Bitcoin

![Altcoin nel ciclo BTC](alt_btc_cycle_spirals.png)

| Asset | Coppia | Forza vs BTC | Score raw | Candidato | 30g | Peso Global |
| --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | RELATIVA MISTA / NON CONFERMATA | 3 | 0 | 9.708582678775791 | 0 |
| DOGE | DOGE/BTC | SOTTOPERFORMA BTC | -5 | -1 | -0.6730373097583064 | 0 |

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

Generato: 2026-09-13 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [relative_strength_btc_report.md](relative_strength_btc_report.md)

Questo modulo controlla se SOL e DOGE stanno davvero battendo Bitcoin. Una salita in USD accompagnata da una coppia ALT/BTC ribassista è spesso soltanto trascinamento di BTC.

**Protezione iniziale:** il candidato relativo è limitato a -1/0/+1, ma il peso nel Global resta **0**. La coppia BTC conferma o indebolisce il tecnico USD; non viene sommata come secondo modulo indipendente.

## Sintesi

| Asset | Coppia | Prezzo | Score raw | Candidato | Peso Global | Forza vs BTC | Confidenza | 30g | Tecnico USD | Lettura combinata |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | 0.00131760 | +3 | 0 | 0 | RELATIVA MISTA / NON CONFERMATA | BASSA | +9,71% | MISTA | QUADRO MISTO / NESSUNA CONFERMA RELATIVA |
| DOGE | DOGE/BTC | 0.00000110 | -5 | -1 | 0 | SOTTOPERFORMA BTC | MEDIA | -0,67% | RIBASSISTA | DEBOLEZZA COMPLETA: scende in USD e contro BTC |

## Matrice di lettura

| ALT/USD | ALT/BTC | Interpretazione |
| --- | --- | --- |
| Rialzista | Rialzista | Conferma migliore: sale e batte BTC |
| Rialzista | Ribassista | Sale soprattutto perché BTC trascina il mercato |
| Ribassista | Rialzista | Forza relativa nascosta / possibile rotazione futura |
| Ribassista | Ribassista | Debolezza completa |

## SOL/BTC

- **Verdetto relativo:** RELATIVA MISTA / NON CONFERMATA (+3)
- **Candidato futuro:** 0; **peso attuale Global: 0**
- **Lettura combinata USD/BTC:** QUADRO MISTO / NESSUNA CONFERMA RELATIVA
- **Struttura:** COMPRESSIONE / TRIANGOLO POSSIBILE
- **Rendimenti relativi:** 7g +1,90%; 30g +9,71%; 90g +21,66%; 180g +2,54%
- **Daily:** RSI 58.46; MA50 0.00122683; MA200 0.00118426
- **Weekly:** MA30 0.00118869; RSI 57.74
- **Livelli:** supporto 0.00127500; resistenza 0.00133900; breakout 60g 0.00136900; breakdown 60g 0.00112700
- **Pattern:** DOPPIO MINIMO / TARGET RAGGIUNTO; neckline 0.00120200; target 0.00125350
- **Fibonacci:** NON ATTIVO — 23.6% a 0.00128404
- **Fonte:** Yahoo Finance SOL-BTC (coppia diretta)
- **Motivi score:** prezzo sopra MA50 daily; prezzo sopra MA200 daily; MA50 daily in salita; prezzo sopra MA30 weekly; MA30 weekly in discesa; RSI relativo forte; MACD relativo negativo

![Grafico SOL/BTC](relative_strength_SOLBTC.png)

## DOGE/BTC

- **Verdetto relativo:** SOTTOPERFORMA BTC (-5)
- **Candidato futuro:** -1; **peso attuale Global: 0**
- **Lettura combinata USD/BTC:** DEBOLEZZA COMPLETA: scende in USD e contro BTC
- **Struttura:** MASSIMI E MINIMI DECRESCENTI
- **Rendimenti relativi:** 7g -2,27%; 30g -0,67%; 90g -18,72%; 180g -20,30%
- **Daily:** RSI 48.83; MA50 0.00000110; MA200 0.00000126
- **Weekly:** MA30 0.00000126; RSI 39.14
- **Livelli:** supporto 0.00000110; resistenza 0.00000114; breakout 60g 0.00000131; breakdown 60g 0.00000099
- **Pattern:** DOPPIO MINIMO / TARGET RAGGIUNTO; neckline 0.00000115; target 0.00000128
- **Fibonacci:** VICINO — 23.6% a 0.00000112
- **Fonte:** Rapporto sintetico DOGE-USD / BTC-USD (sintetica)
- **Motivi score:** prezzo sotto MA50 daily; prezzo sotto MA200 daily; MA50 daily in discesa; prezzo sotto MA30 weekly; MA30 weekly in discesa; struttura con massimi/minimi decrescenti; MACD relativo positivo

![Grafico DOGE/BTC](relative_strength_DOGEBTC.png)

## Backtest storico diagnostico

Il backtest usa soltanto indicatori disponibili alla data del segnale e campiona una volta a settimana. È utile subito, ma non sostituisce il tracker live: le soglie sono state definite prima di vedere il risultato.

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto direzione | Return futuro mediano |
| --- | --- | --- | --- | --- | --- |
| SOL | 7g | 208 | 52,40% | +1,95% | -1,06% |
| SOL | 30g | 204 | 47,06% | +4,50% | +0,44% |
| SOL | 90g | 200 | 52,50% | +9,74% | +3,06% |
| DOGE | 7g | 295 | 55,59% | +1,83% | -1,68% |
| DOGE | 30g | 294 | 53,06% | +1,97% | -3,49% |
| DOGE | 90g | 286 | 53,85% | +6,84% | -8,85% |

## Tracker live e gate futuro

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto | Stato | Peso Global |
| --- | --- | --- | --- | --- | --- | --- |
| SOL | 1g | 35 | 54,29% | +0,10% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 3g | 35 | 54,29% | +0,48% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 7g | 32 | 46,88% | +0,76% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 14g | 27 | 37,04% | +0,08% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 30g | 16 | 6,25% | -11,21% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 1g | 49 | 65,31% | -0,11% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 3g | 47 | 55,32% | -0,14% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 7g | 46 | 54,35% | -0,23% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 14g | 40 | 65,00% | +0,18% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 30g | 33 | 66,67% | +0,25% | LOCKED / RACCOLTA LIVE | 0 |

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

Ultima candela SOL usata: **13 settembre 2026**

## SOL PRICE CONTEXT

| Voce | Valore | Provenienza / significato |
| --- | --- | --- |
| Anchor computazionale | 101,86 $ | 2026-09-13T05:30:22Z \| Yahoo Finance daily shared snapshot \| Close 1d |
| Candela anchor completata | NO | Stato esplicito; il valore non viene sostituito dal prezzo pubblico. |
| Riferimento pubblico corrente | 101,86 $ | 2026-09-13T05:32:00Z \| Yahoo Finance \| solo display |
| Età anchor alla generazione | 0h 1m | WITHIN_DAILY_REPORT_CADENCE |
| Gap corrente vs anchor | 0,00000 $ | 0,00% |
| Validità input modello | REPRODUCIBLE_SHARED_SNAPSHOT | Non è una dichiarazione di validità del segnale/trading. |

```text
COMPUTATIONAL_ANCHOR_PRICE=101.86000061035156
COMPUTATIONAL_ANCHOR_FIELD=Close
COMPUTATIONAL_ANCHOR_TIMESTAMP=2026-09-13T05:30:22Z
COMPUTATIONAL_ANCHOR_SYMBOL=SOL-USD
COMPUTATIONAL_ANCHOR_PROVIDER=Yahoo Finance daily shared snapshot
COMPUTATIONAL_ANCHOR_TIMEFRAME=1d
COMPUTATIONAL_ANCHOR_COMPLETED=NO
CURRENT_PUBLIC_REFERENCE_PRICE=101.86000061035156
CURRENT_PUBLIC_REFERENCE_TIMESTAMP=2026-09-13T05:32:00Z
CURRENT_PUBLIC_REFERENCE_ACQUIRED_AT=2026-09-13T05:32:12Z
CURRENT_PUBLIC_REFERENCE_SYMBOL=SOL-USD
CURRENT_PUBLIC_REFERENCE_PROVIDER=Yahoo Finance
CURRENT_PUBLIC_REFERENCE_FIELD=Close
CURRENT_PUBLIC_REFERENCE_TIMEFRAME=1m
CURRENT_PUBLIC_REFERENCE_STATUS=AVAILABLE
ANCHOR_AGE_SECONDS=110.346314
ANCHOR_AGE_HOURS=0.03065175388888889
CURRENT_VS_ANCHOR_GAP_USD=0.0
CURRENT_VS_ANCHOR_GAP_PCT=0.0
```

## Verdetto: ANALOGIA DEBOLE / SCENARIO SECONDARIO

- **Fase attuale:** FRATTALE SOLO DI CONTESTO
- **Somiglianza totale:** +70,17%
- **Somiglianza strutturale:** +70,17%
- **Aderenza prezzo live:** +72,50%
- **Errore medio live:** +13,75%
- **Gap prezzo corrente:** +11,71%
- **Peso operativo suggerito:** 0
- **Affidabilita:** BASSA
- **Rischio fase:** ALTO
- **Trend tracking:** STRUTTURA STABILE
- **Sintesi:** Esistono alcuni elementi comuni, ma non abbastanza per una conferma.
- **SOL è al giorno:** 99 dal bottom usato.
- **Giorno BTC equivalente:** 2023-02-28
- **Prossimo step:** Proiezione condizionale, non conferma operativa: **Prima retest / debolezza, poi recupero.** Zona bassa **88,83 $** intorno al **23 settembre 2026**; zona alta **108,90 $** intorno al **27 settembre 2026**; fine step circa **108,90 $** entro il **27 settembre 2026**.

### Metadata aderenza prezzo

```text
OPERATIONAL_VERDICT_REASON=ANALOGIA DEBOLE / SCENARIO SECONDARIO
PRICE_ADHERENCE_FAILED=NO
PRICE_ADHERENCE_LIVE_AVG_GAP_FAILED=NO
PRICE_ADHERENCE_LAST_GAP_FAILED=NO
PRICE_ADHERENCE_LIVE_AVG_GAP_THRESHOLD_PCT=15.0
PRICE_ADHERENCE_LAST_GAP_THRESHOLD_PCT=18.0
PRICE_ADHERENCE_OBSERVED_LIVE_AVG_GAP_PCT=13.74952896689689
PRICE_ADHERENCE_OBSERVED_LAST_GAP_PCT=11.709618329062854
```

## Somiglianza prima e dopo inizio programma

Questa sezione separa la somiglianza della forma dall'aderenza reale del prezzo.

- **Inizio programma/scanner:** 3 luglio 2026
- **Prima del programma** = backtest retroattivo.
- **Da inizio programma** = verifica live: è la parte più importante per l'uso operativo.

| Periodo | Date | Giorni | Aderenza prezzo | Errore medio | Gap ultimo | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| Prima del programma | 6 giugno 2026 -> 2 luglio 2026 | 27 | +87,95% | +6,02% | +21,89% | ABBASTANZA ALLINEATO |
| Da inizio programma | 3 luglio 2026 -> 13 settembre 2026 | 73 | +72,50% | +13,75% | +11,71% | DEVIAZIONE MODERATA |
| Totale dal bottom | 6 giugno 2026 -> 13 settembre 2026 | 100 | +76,67% | +11,66% | +11,71% | DEVIAZIONE MODERATA |

Nota: un frattale può avere una forma simile ma un prezzo distante. In quel caso non è operativo finché il gap non rientra.

## Lettura operativa veloce

Il frattale resta non operativo. Motivo effettivo: ANALOGIA DEBOLE / SCENARIO SECONDARIO.

| Voce | Risposta | Perché |
| --- | --- | --- |
| Uso operativo | NO | Peso 0 per il verdetto: ANALOGIA DEBOLE / SCENARIO SECONDARIO. |
| Aderenza live | +72,50% | Errore medio live +13,75%. |
| Gap corrente | +11,71% | Metrica separata dal motivo del verdetto. |
| Prima conferma prezzo | 108,90 $ | Serve anche miglioramento del gap, non solo una candela sopra il livello. |
| Seconda conferma | 134,15 $ | Rende più credibile il percorso, ma non sostituisce l'aderenza. |
| Invalidazione soft | 88,83 $ | Sotto questa zona il quadro peggiora. |
| Invalidazione forte | 62,19 $ | Sotto il bottom il paragone è quasi rotto. |

## Target ciclo fino al top BTC 2025

| Voce | Valore |
| --- | --- |
| Stato | CONTESTO / NON OPERATIVO |
| Top BTC 2025 | 6 ottobre 2025 - 124.753 $ |
| Data SOL equivalente | 21 aprile 2029 |
| Target ciclo base dall'anchor modello | 548,97 $ |
| Massimo percorso base | 548,97 $ (21 aprile 2029) |

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
| Prima conferma | 108,90 $ | Deve accompagnarsi al rientro del gap. |
| Seconda conferma | 134,15 $ | Scenario più credibile. |
| Invalidazione soft | 88,83 $ | Il frattale si indebolisce. |
| Invalidazione forte | 62,19 $ | Il paragone si rompe. |

## Proiezione veloce con date SOL

| Orizzonte | Data SOL | BTC fece | SOL base | Min percorso | Max percorso |
| --- | --- | --- | --- | --- | --- |
| 7 giorni | 20 settembre 2026 | -4,01% | 97,78 $ | 97,78 $ | 104,06 $ |
| 14 giorni | 27 settembre 2026 | +6,91% | 108,90 $ | 88,83 $ | 108,90 $ |
| 30 giorni | 13 ottobre 2026 | +21,11% | 123,36 $ | 88,83 $ | 124,75 $ |
| 60 giorni | 12 novembre 2026 | +26,36% | 128,71 $ | 88,83 $ | 134,15 $ |
| 90 giorni | 12 dicembre 2026 | +19,87% | 122,10 $ | 88,83 $ | 134,15 $ |
| 120 giorni | 11 gennaio 2027 | +29,98% | 132,39 $ | 88,83 $ | 135,08 $ |

## Prossimi step se SOL segue BTC 2022

| Step | Date SOL | BTC fine | SOL zona bassa | SOL zona alta | SOL fine base | Lettura |
| --- | --- | --- | --- | --- | --- | --- |
| Step 1 - prossime 2 settimane | 13 settembre 2026 -> 27 settembre 2026 | +6,91% | 88,83 $ (23 settembre 2026) | 108,90 $ (27 settembre 2026) | 108,90 $ | Prima retest / debolezza, poi recupero. |
| Step 2 - primo mese | 28 settembre 2026 -> 13 ottobre 2026 | +21,11% | 107,27 $ (28 settembre 2026) | 124,75 $ (12 ottobre 2026) | 123,36 $ | Spinta rialzista abbastanza pulita. |
| Step 3 - secondo mese | 14 ottobre 2026 -> 12 novembre 2026 | +26,36% | 120,03 $ (4 novembre 2026) | 134,15 $ (28 ottobre 2026) | 128,71 $ | Spinta rialzista abbastanza pulita. |
| Step 4 - terzo mese | 13 novembre 2026 -> 12 dicembre 2026 | +19,87% | 115,89 $ (7 dicembre 2026) | 129,97 $ (18 novembre 2026) | 122,10 $ | Spinta rialzista abbastanza pulita. |

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
| Prezzo SOL | 101,86 $ |  |
| Weekly RSI | 56,90 / linea grezza 52,24 | LINEA NON AFFIDABILE / RISCHIO NON ATTIVO — IRREALISTICA / NON OPERATIVA |
| Monthly RSI | 46,77 / linea grezza 55,48 | RSI TROPPO BASSO PER RISCHIO TOP — VALIDA / USO PRUDENTE |
| Target ciclo base | 548,97 $ | Avanzamento +18,55% |
| Rischio top-cycle RSI | BASSO | Nessun segnale top-cycle macro attivo. Prezzo ancora lontano dal target ciclo; il filtro RSI resta solo di monitoraggio. |

## Lettura semplice

- Weekly: La top-line weekly non supera i controlli di qualità. Non viene usata per generare rischio top-cycle.
- Monthly: RSI monthly è 46,8, sotto la soglia prudente 55. Anche se fosse vicino alla linea, non è una vera zona di esaurimento ciclo.
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
| Prezzo SOL | 101,86 $ |
| TVL Solana | 5,91 mld $ |
| TVL 7g | -0,09% |
| DEX volume 24h | 2,47 mld $ |
| Fees 24h | 13,91 mln $ |
| Stablecoin su Solana | 16,46 mld $ |
| Stake ratio | 68,91% |
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
| Prezzo SOL | 101,86 $ |
| EMA200 weekly target | 111,24 $ |
| Upside verso EMA200 | +9,25% |
| Distanza prezzo da EMA200 | -8,47% |
| Gap EMA50/EMA200 | -5,74% |
| Stato cross | EMA50 SOTTO EMA200 |
| RSI weekly | 56,87 |
| Età SOL | 6,4 anni |
| Analoghi storici usati | 30 |
| Max analoghi per asset | 3 |
| Hit EMA200 12w analoghi | +73,33% |
| Max gain mediano 12w | +20,78% |
| Drawdown mediano 12w | -37,06% |

Lettura semplice:

**SOLO OSSERVAZIONE**

Autocontrollo: **STABILE / DA CONFERMARE**.

Questo modulo confronta SOL con altre crypto in fasi simili di età, distanza da EMA200, EMA50/EMA200 e RSI. Non usa stock market.

Nota importante: **questo modulo ora NON pesa più nel Global Confluence**. Resta solo come contesto di ciclo e come mappa verso EMA200 weekly. Il punteggio Global resta guidato da prezzo, scanner, regime, struttura tecnica, frattale, RSI e conferme reali.

Nota: se EMA50/EMA200 sono dentro ±2%, il modulo parla di medie sovrapposte / incrocio in corso, perché exchange diversi possono mostrare il cross leggermente prima o dopo.

<!-- Generato: 2026-09-13 05:32 UTC -->
<!-- MAJOR_ALT_LIFECYCLE_SQUEEZE_END -->

</details>
<!-- COMPACT_SECTION_END:major_alt_lifecycle -->

# Report giornaliero BTC / SOL / DOGE

Aggiornato il: **2026-09-13 05:30:23 UTC**

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
- DOGE: nessun cambiamento forte rispetto a ieri.

| Asset | Cambio | Tono | Verdetto oggi | Casi positivi oggi | Δ casi positivi |
| --- | --- | --- | --- | --- | --- |
| BTC | CAMBIAMENTO MEDIO | miglioramento | RIALZISTA | +85.00% | +2.50 punti |
| SOL | NESSUN CAMBIAMENTO FORTE | miglioramento | RIALZISTA | +67.50% | +2.50 punti |
| DOGE | NESSUN CAMBIAMENTO FORTE | misto | RIBASSISTA | +25.00% | -2.50 punti |

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
| BTC | 73.410 $ | 85.001 $ | +73,68% | +15,79% | buona zona storica di rimbalzo | 85.001 $ | 73.410 $ | +8,57% | -13,64% | spike storicamente più resistente |
| SOL | 96,77 $ | 112,05 $ | +40,00% | +15,79% | rimbalzo debole | 112,05 $ | 96,77 $ | +16,13% | -13,64% | spike storicamente più resistente |
| DOGE | 0,08057 $ | 0,09329 $ | +26,47% | +15,79% | rimbalzo poco frequente | 0,09329 $ | 0,08057 $ | +70,83% | -13,64% | spike spesso scaricato |

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

- **BTC: su 40 casi simili, 19 prima sono scesi a -5,00%. Tra quei 19, 14 poi sono rimbalzati fino a +10,00%. Percentuale: +73,68% (14/19). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: buona zona storica di rimbalzo.**
- **BTC: su 40 casi simili, 35 prima sono saliti a +10,00%. Tra quei 35, 3 poi sono scaricati a -5,00%. Percentuale: +8,57% (3/35). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.**
- **SOL: su 40 casi simili, 20 prima sono scesi a -5,00%. Tra quei 20, 8 poi sono rimbalzati fino a +10,00%. Percentuale: +40,00% (8/20). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.**
- **SOL: su 40 casi simili, 31 prima sono saliti a +10,00%. Tra quei 31, 5 poi sono scaricati a -5,00%. Percentuale: +16,13% (5/31). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.**
- **DOGE: su 40 casi simili, 34 prima sono scesi a -5,00%. Tra quei 34, 9 poi sono rimbalzati fino a +10,00%. Percentuale: +26,47% (9/34). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.**
- **DOGE: su 40 casi simili, 24 prima sono saliti a +10,00%. Tra quei 24, 17 poi sono scaricati a -5,00%. Percentuale: +70,83% (17/24). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike spesso scaricato.**

<!-- BOUNCE_AFTER_DRAWDOWN_END -->

</details>
<!-- COMPACT_SECTION_END:bounce_after_drawdown -->

<!-- COMPACT_SECTION_START:scanner_forecast -->
<details>
<summary><strong>🔭 Cono probabilistico dello scanner</strong></summary>

<!-- SCANNER_FORECAST_TRACKER_START -->
# Scanner forecast path / cono probabilistico

Generato: 2026-09-13 05:31:53 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [scanner_forecast_tracker_report.md](scanner_forecast_tracker_report.md)

## Snapshot effettivamente usato

| Asset   | Snapshot prezzo   | Generazione snapshot prezzo   | Snapshot match scanner   |
|:--------|:------------------|:------------------------------|:-------------------------|
| BTC | 2026-09-13 | 2026-09-13T05:30:22Z | 2026-09-13 05:30:23 |
| SOL | 2026-09-13 | 2026-09-13T05:30:22Z | 2026-09-13 05:30:23 |
| DOGE | 2026-09-13 | 2026-09-13T05:30:22Z | 2026-09-13 05:30:23 |

La data di generazione del report non sostituisce la data degli input: se gli snapshot locali sono più vecchi, i valori restano riferiti agli snapshot indicati in tabella.

Questo report trasforma i 40 casi simili dello scanner in un cono previsionale leggibile.

Per ogni asset crea:

- banda larga p10-p90
- banda centrale p25-p75
- scenario centrale p50
- prezzo reale sovrapposto quando sono disponibili dati successivi

Correzione importante: il cono ora viene calcolato dai percorsi reali dei match storici, non solo dai percentili finali a 30 giorni. Quindi il grafico non deve più mostrare solo due puntini.

## Ultimo cono previsionale salvato

| Asset   | Data       | Prezzo iniziale   | Direzione scanner   | Casi positivi   | P10 30g     | P25 30g     | P50 30g      | P75 30g      | P90 30g      |
|:--------|:-----------|:------------------|:--------------------|:----------------|:------------|:------------|:-------------|:-------------|:-------------|
| BTC | 2026-09-13 | 77.274 $ | SALITA | 85,00% | 60.589,60 $ | 89.830,99 $ | 105.839,20 $ | 121.346,64 $ | 132.527,19 $ |
| SOL | 2026-09-13 | 101,86 $ | SALITA | 67,50% | 80,55 $ | 95,63 $ | 135,67 $ | 171,03 $ | 223,29 $ |
| DOGE | 2026-09-13 | 0.08481 $ | DISCESA | 25,00% | 0.06214 $ | 0.06449 $ | 0.07220 $ | 0.08365 $ | 0.12565 $ |

## Confronto raw / regime-adjusted

Il cono raw continua a usare i 40 casi dello scanner. Il cono regime-adjusted sceglie una sola coorte nella gerarchia SAME_BTC_AND_ASSET_REGIME → SAME_ASSET_REGIME → SAME_BTC_REGIME. Ogni livello richiede almeno 5 match; le coorti non vengono mai combinate e ogni fallback è dichiarato.

| Asset   | Stato adjusted              | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level        | selection_reason              | Raw p50 30g   | Adjusted p50 30g   | Raw p90 30g   | Adjusted p90 30g   |
|:--------|:----------------------------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:----------------------|:------------------------------|:--------------|:-------------------|:--------------|:-------------------|
| BTC | INSUFFICIENT_REGIME_MATCHES | NONE | 0 | 1 | 0 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES | 105.839,20 $ | n/a | 132.527,19 $ | n/a |
| SOL | INSUFFICIENT_REGIME_MATCHES | NONE | 0 | 3 | 0 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES | 135,67 $ | n/a | 223,29 $ | n/a |
| DOGE | AVAILABLE | SAME_ASSET_REGIME | 0 | 20 | 1 | 20 | 5 | 1_SAME_ASSET_FALLBACK | FALLBACK_TO_SAME_ASSET_REGIME | 0.07220 $ | 0.07140 $ | 0.12565 $ | 0.08655 $ |

## Grafici

### BTC

![Scanner forecast BTC](scanner_forecast_BTC.png)

#### Verifica storica e discrepanza

![Verifica storica cono BTC](scanner_forecast_history_BTC.png)

- Cono congelato il **2026-08-14**; verificato fino al **2026-09-13**; stato **COMPLETO 30/30g**.
- Reale **77.274,99 $**; p50 previsto **68.207,55 $**; scarto **13,29%**.
- Errore medio assoluto **13,15%**; massimo **23,38%**; DENTRO p10-p90; FUORI p25-p75.

#### Cono regime-adjusted

Gruppo selezionato: **NONE**; fallback: **NONE**; motivo: **INSUFFICIENT_REGIME_MATCHES**.

Non disponibile: INSUFFICIENT_REGIME_MATCHES (campione selezionato 0/5 match).

### SOL

![Scanner forecast SOL](scanner_forecast_SOL.png)

#### Verifica storica e discrepanza

![Verifica storica cono SOL](scanner_forecast_history_SOL.png)

- Cono congelato il **2026-08-14**; verificato fino al **2026-09-13**; stato **COMPLETO 30/30g**.
- Reale **101,85 $**; p50 previsto **79,32 $**; scarto **28,40%**.
- Errore medio assoluto **21,35%**; massimo **36,55%**; DENTRO p10-p90; FUORI p25-p75.

#### Cono regime-adjusted

Gruppo selezionato: **NONE**; fallback: **NONE**; motivo: **INSUFFICIENT_REGIME_MATCHES**.

Non disponibile: INSUFFICIENT_REGIME_MATCHES (campione selezionato 0/5 match).

### DOGE

![Scanner forecast DOGE](scanner_forecast_DOGE.png)

#### Verifica storica e discrepanza

![Verifica storica cono DOGE](scanner_forecast_history_DOGE.png)

- Cono congelato il **2026-08-14**; verificato fino al **2026-09-13**; stato **COMPLETO 30/30g**.
- Reale **0.08482 $**; p50 previsto **0.07858 $**; scarto **7,95%**.
- Errore medio assoluto **14,81%**; massimo **39,08%**; DENTRO p10-p90; DENTRO p25-p75.

#### Cono regime-adjusted

Gruppo selezionato: **SAME_ASSET_REGIME**; fallback: **1_SAME_ASSET_FALLBACK**; motivo: **FALLBACK_TO_SAME_ASSET_REGIME**.

**WARNING:** coorte fallback meno stringente rispetto a SAME_BTC_AND_ASSET_REGIME.

![Scanner forecast regime-adjusted DOGE](scanner_forecast_DOGE_regime_adjusted.png)

## Accuratezza percorso scanner

| Asset   | Giorno   |   Controlli | Dentro p10-p90   | Dentro p25-p75   | Errore medio abs vs p50   | Errore medio vs p50   |
|:--------|:---------|------------:|:-----------------|:-----------------|:--------------------------|:----------------------|
| BTC | 1g | 62 | 93,55% | 66,13% | 2,08% | 0,47% |
| BTC | 3g | 58 | 91,38% | 72,41% | 3,29% | 0,78% |
| BTC | 7g | 50 | 90,00% | 72,00% | 5,14% | 2,48% |
| BTC | 14g | 37 | 97,30% | 64,86% | 6,56% | 3,96% |
| BTC | 30g | 23 | 100,00% | 91,30% | 8,90% | 3,16% |
| SOL | 1g | 62 | 80,65% | 61,29% | 2,77% | 1,02% |
| SOL | 3g | 58 | 89,66% | 74,14% | 4,01% | 1,78% |
| SOL | 7g | 50 | 88,00% | 72,00% | 5,55% | 3,85% |
| SOL | 14g | 37 | 81,08% | 64,86% | 8,61% | 7,61% |
| SOL | 30g | 23 | 91,30% | 47,83% | 15,48% | 14,92% |
| DOGE | 1g | 62 | 87,10% | 61,29% | 3,24% | 0,77% |
| DOGE | 3g | 58 | 89,66% | 68,97% | 4,73% | 1,90% |
| DOGE | 7g | 50 | 76,00% | 74,00% | 8,63% | 6,17% |
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
| BTC | 3g | 10 | 30 | RACCOLTA (20 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 7g | 9 | 30 | RACCOLTA (21 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 14g | 8 | 30 | RACCOLTA (22 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 30g | 6 | 30 | RACCOLTA (24 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 1g | 10 | 30 | RACCOLTA (20 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 3g | 10 | 30 | RACCOLTA (20 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 7g | 9 | 30 | RACCOLTA (21 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 14g | 8 | 30 | RACCOLTA (22 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 30g | 6 | 30 | RACCOLTA (24 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 1g | 10 | 30 | RACCOLTA (20 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 3g | 10 | 30 | RACCOLTA (20 mancanti) | 0,0% | 0,00% | 1,000 |
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

</details>
<!-- COMPACT_SECTION_END:scanner_forecast -->

<!-- COMPACT_SECTION_START:extreme_cases -->
<details>
<summary><strong>⚠️ Percorso dei casi estremi</strong></summary>

<!-- EXTREME_CASES_PATH_START -->
# Extreme cases path report

Generato: 2026-09-13 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [extreme_cases_path_report.md](extreme_cases_path_report.md)

Questo report si attiva quando i casi positivi o negativi sono almeno **80%**.

Ora misura anche il **rialzo massimo prima della discesa principale**, quindi distingue uno spike iniziale da una discesa quasi immediata.

## Trigger estremi

| Asset   | Direzione            | Trigger   | Percentuale   | Motivo                           |   Match disponibili |
|:--------|:---------------------|:----------|:--------------|:---------------------------------|--------------------:|
| BTC     | POSITIVO / RIALZISTA | SI        | +85,00%       | Casi positivi 85.00% >= 80%      |                  40 |
| SOL     | NESSUNO              | NO        | +67,50%       | Nessun lato sopra soglia estrema |                  40 |
| DOGE    | NESSUNO              | NO        | +75,00%       | Nessun lato sopra soglia estrema |                  40 |

## BTC — casi rialzisti

- Trigger: **Casi positivi 85.00% >= 80%**
- Casi usati nei grafici: **34**
- Return mediano 7g: **+3,86%**
- Return mediano 14g: **+16,22%**
- Return mediano 30g: **+40,47%**
- Drawdown mediano: **-3,67%**
- Max gain mediano: **+42,24%**

### Quanto salivano prima di scendere

- Spike massimo mediano prima del minimo: **+0,00%**
- Spike massimo medio prima del minimo: **+1,70%**
- Spike p75 prima del minimo: **+0,02%**
- Giorno mediano dello spike: **giorno 0**
- Giorno mediano del minimo: **giorno 2**
- Scarico mediano dal picco al minimo: **-3,99%**
- Casi con almeno +5% prima del minimo: **+8,82%**
- Casi con almeno +10% prima del minimo: **+5,88%**
- Casi con almeno +15% prima del minimo: **+5,88%**
- Discesa quasi immediata: **+76,47%**

Un segnale ribassista a 30 giorni non significa necessariamente discesa immediata: alcuni casi fanno prima uno spike e poi scaricano.

### Distribuzione 30 giorni

| P10     | P25     | P50     | P75     | P90     |
|:--------|:--------|:--------|:--------|:--------|
| +15,04% | +22,22% | +40,47% | +58,63% | +82,65% |

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
| ADA-USD         | 2020-12-11 | +86,29%      | +20,18%                  |              5 | -2,19%       |              12 | -18,61%          | +118,64%     | ECCEZIONE POSITIVA            |
| DASH-USD        | 2020-12-11 | +87,46%      | +17,30%                  |              9 | -6,83%       |              22 | -20,57%          | +58,96%      | ECCEZIONE POSITIVA            |
| LRC-USD         | 2020-06-24 | +86,20%      | +7,85%                   |              2 | -6,93%       |               5 | -13,71%          | +47,51%      | ECCEZIONE POSITIVA            |
| INJ-USD         | 2023-11-18 | +88,80%      | +4,94%                   |              1 | -10,45%      |               3 | -14,67%          | +131,17%     | RIALZO MODESTO PRIMA DEL DUMP |
| 1INCH-USD       | 2023-11-23 | +88,90%      | +3,34%                   |              2 | -4,97%       |               7 | -8,04%           | +17,36%      | ECCEZIONE POSITIVA            |
| ZIL-USD         | 2023-11-23 | +87,22%      | +2,25%                   |              2 | -1,34%       |               4 | -3,51%           | +21,53%      | DISCESA QUASI IMMEDIATA       |
| ZEC-USD         | 2019-04-21 | +85,13%      | +1,09%                   |              1 | -17,25%      |              18 | -18,15%          | +9,64%       | ECCEZIONE POSITIVA            |
| DASH-USD        | 2019-04-21 | +85,36%      | +0,93%                   |              1 | -11,07%      |               8 | -11,89%          | +37,08%      | ECCEZIONE POSITIVA            |
| BCH-USD         | 2019-04-26 | +85,36%      | +0,02%                   |              1 | -10,33%      |               3 | -10,35%          | +64,03%      | DISCESA QUASI IMMEDIATA       |
| XLM-USD         | 2020-12-16 | +90,51%      | +0,00%                   |              0 | -33,92%      |               7 | -33,92%          | +48,87%      | ECCEZIONE POSITIVA            |
| THETA-USD       | 2023-11-25 | +88,91%      | +0,00%                   |              0 | -6,15%       |               2 | -6,15%           | +39,60%      | DISCESA QUASI IMMEDIATA       |
| BNB-USD         | 2019-03-02 | +88,78%      | +0,00%                   |              0 | -2,80%       |               1 | -2,80%           | +51,23%      | DISCESA QUASI IMMEDIATA       |
| ALGO-USD        | 2023-11-25 | +87,84%      | +0,00%                   |              0 | -6,07%       |               2 | -6,07%           | +69,64%      | DISCESA QUASI IMMEDIATA       |
| EGLD-USD        | 2023-11-26 | +87,14%      | +0,00%                   |              0 | -3,88%       |               4 | -3,88%           | +57,64%      | DISCESA QUASI IMMEDIATA       |
| ADA-USD         | 2023-11-26 | +86,98%      | +0,00%                   |              0 | -3,17%       |               4 | -3,17%           | +56,83%      | DISCESA QUASI IMMEDIATA       |
| MATIC-USD       | 2023-11-26 | +86,89%      | +0,00%                   |              0 | -2,61%       |               1 | -2,61%           | +33,08%      | DISCESA QUASI IMMEDIATA       |
| BTC-USD         | 2019-04-24 | +86,86%      | +0,00%                   |              0 | -4,65%       |               1 | -4,65%           | +46,16%      | DISCESA QUASI IMMEDIATA       |
| ETC-USD         | 2023-11-26 | +86,83%      | +0,00%                   |              0 | -2,88%       |               1 | -2,88%           | +8,94%       | DISCESA QUASI IMMEDIATA       |
| QTUM-USD        | 2023-11-21 | +86,57%      | +0,00%                   |              0 | +0,00%       |               0 | +0,00%           | +14,24%      | DISCESA QUASI IMMEDIATA       |
| EOS-USD         | 2023-11-26 | +86,40%      | +0,00%                   |              0 | -3,46%       |               1 | -3,46%           | +24,65%      | DISCESA QUASI IMMEDIATA       |

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
- Casi positivi / salita storica: **85,00%**
- Casi negativi / discesa storica: **15,00%**
- Quanto è netto il segnale: **forte**
- Prezzo attuale: **77.273,82 $**
- Return normale fra 30 giorni: **105.839,20 $** (36,97%)
- Drawdown normale durante il mese: **73.554,23 $** (-4,81%)
- Drawdown brutto da rispettare: **69.265,79 $** (-10,36%)
- Max gain normale durante il mese: **108.565,73 $** (40,49%)
- Max gain buono / take profit ottimistico: **130.693,47 $** (69,13%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Solana
- Direzione più probabile a 30 giorni: **SALITA**
- Casi positivi / salita storica: **67,50%**
- Casi negativi / discesa storica: **32,50%**
- Quanto è netto il segnale: **medio**
- Prezzo attuale: **101,86 $**
- Return normale fra 30 giorni: **135,67 $** (33,19%)
- Drawdown normale durante il mese: **96,47 $** (-5,29%)
- Drawdown brutto da rispettare: **79,14 $** (-22,30%)
- Max gain normale durante il mese: **149,38 $** (46,65%)
- Max gain buono / take profit ottimistico: **176,06 $** (72,84%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Dogecoin
- Direzione più probabile a 30 giorni: **DISCESA**
- Casi positivi / salita storica: **25,00%**
- Casi negativi / discesa storica: **75,00%**
- Quanto è netto il segnale: **forte**
- Prezzo attuale: **0,08 $**
- Return normale fra 30 giorni: **0,07 $** (-14,87%)
- Drawdown normale durante il mese: **0,07 $** (-18,58%)
- Drawdown brutto da rispettare: **0,06 $** (-29,75%)
- Max gain normale durante il mese: **0,10 $** (12,36%)
- Max gain buono / take profit ottimistico: **0,11 $** (25,39%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Messaggio del giorno

Il quadro generale oggi è più favorevole. Lo scanner vede più possibilità di salita su più asset.

---

# Mappa semplice asset per asset

# Bitcoin — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟢 VERDE / Favorevole
**Prezzo attuale:** 77.273,82 $

**Direzione più probabile a 30 giorni:** **SALITA**
- Probabilità storica di salita: **85,00%**
- Probabilità storica di discesa: **15,00%**
- Quanto è netto il segnale: **forte**

## Come leggere questa parte

- **Probabilità storica di salita** = su 40 casi simili, quanti hanno chiuso sopra dopo 30 giorni.
- **Probabilità storica di discesa** = su 40 casi simili, quanti hanno chiuso sotto dopo 30 giorni.
- **Quanto è netto il segnale** = quanto è grande la differenza tra salita e discesa. Non vuol dire certezza, vuol dire solo che il risultato storico non è vicino al 50/50.

La lettura principale è rialzista, con segnale forte. Nei casi storici simili, il prezzo ha chiuso sopra dopo 30 giorni più spesso di quanto abbia chiuso sotto.

## 1. Return 30d — prezzo fra 30 giorni

**Return** significa rendimento finale. Qui guardiamo dove potrebbe stare il prezzo **alla fine dei 30 giorni**, non durante il percorso.

- Se va molto male: **60.589,60 $** (-21,59%)
- Se va male: **89.830,99 $** (16,25%)
- Scenario normale: **105.839,20 $** (36,97%)
- Se va bene: **121.346,64 $** (57,03%)
- Se va molto bene: **132.527,19 $** (71,50%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **73.554,23 $** (-4,81%)
- Discesa brutta: **69.265,79 $** (-10,36%)
- Discesa molto brutta: **51.093,67 $** (-33,88%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **108.565,73 $** (40,49%)
- Rialzo buono: **130.693,47 $** (69,13%)
- Rialzo molto forte: **160.927,62 $** (108,26%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Bitcoin tendeva a muoversi tra una zona bassa intorno a **73.554,23 $** e uno spike normale intorno a **108.565,73 $**.

La chiusura a 30 giorni era più spesso positiva: salita 85,00%, discesa 15,00%. Quindi la lettura principale è favorevole.

Nota leva BTC: se la liquidazione è vicina a 51.000 $, guarda soprattutto la discesa brutta e molto brutta. Il prezzo può recuperare dopo, ma la leva può saltare prima.

---

# Solana — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟢 VERDE / Favorevole
**Prezzo attuale:** 101,86 $

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

- Se va molto male: **80,55 $** (-20,92%)
- Se va male: **95,63 $** (-6,12%)
- Scenario normale: **135,67 $** (33,19%)
- Se va bene: **171,03 $** (67,90%)
- Se va molto bene: **223,29 $** (119,22%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **96,47 $** (-5,29%)
- Discesa brutta: **79,14 $** (-22,30%)
- Discesa molto brutta: **67,36 $** (-33,87%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **149,38 $** (46,65%)
- Rialzo buono: **176,06 $** (72,84%)
- Rialzo molto forte: **284,97 $** (179,77%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Solana tendeva a muoversi tra una zona bassa intorno a **96,47 $** e uno spike normale intorno a **149,38 $**.

La chiusura a 30 giorni era più spesso positiva: salita 67,50%, discesa 32,50%. Quindi la lettura principale è favorevole.

---

# Dogecoin — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🔴 ROSSO / Prudenza
**Prezzo attuale:** 0,08 $

**Direzione più probabile a 30 giorni:** **DISCESA**
- Probabilità storica di salita: **25,00%**
- Probabilità storica di discesa: **75,00%**
- Quanto è netto il segnale: **forte**

## Come leggere questa parte

- **Probabilità storica di salita** = su 40 casi simili, quanti hanno chiuso sopra dopo 30 giorni.
- **Probabilità storica di discesa** = su 40 casi simili, quanti hanno chiuso sotto dopo 30 giorni.
- **Quanto è netto il segnale** = quanto è grande la differenza tra salita e discesa. Non vuol dire certezza, vuol dire solo che il risultato storico non è vicino al 50/50.

La lettura principale è ribassista, con segnale forte. Nei casi storici simili, il prezzo ha chiuso sotto dopo 30 giorni più spesso di quanto abbia chiuso sopra.

## 1. Return 30d — prezzo fra 30 giorni

**Return** significa rendimento finale. Qui guardiamo dove potrebbe stare il prezzo **alla fine dei 30 giorni**, non durante il percorso.

- Se va molto male: **0,06 $** (-26,74%)
- Se va male: **0,06 $** (-23,96%)
- Scenario normale: **0,07 $** (-14,87%)
- Se va bene: **0,08 $** (-1,36%)
- Se va molto bene: **0,13 $** (48,16%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **0,07 $** (-18,58%)
- Discesa brutta: **0,06 $** (-29,75%)
- Discesa molto brutta: **0,06 $** (-32,15%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **0,10 $** (12,36%)
- Rialzo buono: **0,11 $** (25,39%)
- Rialzo molto forte: **0,13 $** (48,36%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Dogecoin tendeva a muoversi tra una zona bassa intorno a **0,07 $** e uno spike normale intorno a **0,10 $**.

La chiusura a 30 giorni era più spesso negativa: salita 25,00%, discesa 75,00%. Quindi la lettura principale è prudente/debole.

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

- Grezzo: **36,97%** → **105.839,20 $**
- Correzione imparata dagli errori: **2,01%**
- Calibrato: **38,97%** → **107.390,80 $**
- Lettura: Lo scanner è stato troppo pessimista sul prezzo finale.

### Drawdown 30d — rischio di discesa durante il mese

- Grezzo: **-4,81%** → **73.554,23 $**
- Correzione imparata dagli errori: **4,72%**
- Calibrato: **-0,09%** → **77.204,12 $**
- Lettura: Lo scanner è stato troppo prudente: nella realtà il prezzo è sceso meno del previsto.

### Max gain 30d — rialzo/spike durante il mese

- Grezzo: **40,49%** → **108.565,73 $**
- Correzione imparata dagli errori: **-2,82%**
- Calibrato: **37,67%** → **106.382,81 $**
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

- Grezzo: **33,19%** → **135,67 $**
- Correzione imparata dagli errori: **8,80%**
- Calibrato: **41,99%** → **144,63 $**
- Lettura: Lo scanner è stato troppo pessimista sul prezzo finale.

### Drawdown 30d — rischio di discesa durante il mese

- Grezzo: **-5,29%** → **96,47 $**
- Correzione imparata dagli errori: **2,99%**
- Calibrato: **-2,30%** → **99,52 $**
- Lettura: Lo scanner è stato troppo prudente: nella realtà il prezzo è sceso meno del previsto.

### Max gain 30d — rialzo/spike durante il mese

- Grezzo: **46,65%** → **149,38 $**
- Correzione imparata dagli errori: **4,02%**
- Calibrato: **50,67%** → **153,47 $**
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
- Direzione calibrata oggi: **INCERTO**

### Return 30d — prezzo finale fra 30 giorni

- Grezzo: **-14,87%** → **0,07 $**
- Correzione imparata dagli errori: **15,19%**
- Calibrato: **0,32%** → **0,09 $**
- Lettura: Lo scanner è stato troppo pessimista sul prezzo finale.

### Drawdown 30d — rischio di discesa durante il mese

- Grezzo: **-18,58%** → **0,07 $**
- Correzione imparata dagli errori: **15,34%**
- Calibrato: **-3,24%** → **0,08 $**
- Lettura: Lo scanner è stato troppo prudente: nella realtà il prezzo è sceso meno del previsto.

### Max gain 30d — rialzo/spike durante il mese

- Grezzo: **12,36%** → **0,10 $**
- Correzione imparata dagli errori: **2,52%**
- Calibrato: **14,89%** → **0,10 $**
- Lettura: Lo scanner ha sottostimato gli spike: nella realtà il prezzo è salito più del previsto.

### Come leggerlo

La parte grezza ti dice cosa mostrano i vecchi pattern storici. La parte calibrata ti dice come cambia quella lettura dopo aver visto se lo scanner, nel mercato reale, è stato troppo ottimista o troppo pessimista.

---

# Approfondimento tecnico — Bitcoin (BTC-USD)

## Semaforo: 🟢 VERDE / Favorevole

**Prezzo attuale:** 77.273,82 $

Bitcoin ha un segnale favorevole. La statistica dei casi simili indica più possibilità di salita che di discesa, ma resta comunque una probabilità, non una certezza.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **85,00%**
- Casi negativi dopo 30 giorni: **15,00%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **86,39%**
- Rendimento medio dopo 30 giorni: **33,32%**
- Rendimento centrale dopo 30 giorni: **36,97%**
- Discesa media durante i 30 giorni: **-11,11%**
- Massimo rialzo medio durante i 30 giorni: **48,78%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **103.018,81 $**
- Scenario centrale a 30 giorni: **105.839,20 $**
- Zona di rischio media: **68.690,86 $**
- Zona di rialzo media: **114.967,67 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -21,59% → **60.589,60 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: 16,25% → **89.830,99 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: 36,97% → **105.839,20 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 57,03% → **121.346,64 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 71,50% → **132.527,19 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -33,88% → **51.093,67 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -10,36% → **69.265,79 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -4,81% → **73.554,23 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -1,87% → **75.825,72 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: 0,00% → **77.273,82 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 8,91% → **84.158,25 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 20,92% → **93.440,72 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 40,49% → **108.565,73 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 69,13% → **130.693,47 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 108,26% → **160.927,62 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| XLM-USD         | 2020-09-08   | 2020-12-16 |        90.51 |        48.87 |         -33.92 |          78.05 |
| THETA-USD       | 2023-08-18   | 2023-11-25 |        88.91 |        39.6  |          -6.15 |          39.6  |
| 1INCH-USD       | 2023-08-16   | 2023-11-23 |        88.9  |        17.36 |          -4.97 |          17.36 |
| INJ-USD         | 2023-08-11   | 2023-11-18 |        88.8  |       131.17 |         -10.45 |         131.17 |
| BNB-USD         | 2018-11-23   | 2019-03-02 |        88.78 |        51.23 |          -2.8  |          51.23 |
| ALGO-USD        | 2023-08-18   | 2023-11-25 |        87.84 |        69.64 |          -6.07 |          71.11 |
| XRP-USD         | 2020-09-03   | 2020-12-11 |        87.6  |       -41.75 |         -61.24 |           6.92 |
| DASH-USD        | 2020-09-03   | 2020-12-11 |        87.46 |        58.96 |          -6.83 |          58.96 |
| ZIL-USD         | 2023-08-16   | 2023-11-23 |        87.22 |        21.53 |          -1.34 |          23.44 |
| EGLD-USD        | 2023-08-19   | 2023-11-26 |        87.14 |        57.64 |          -3.88 |          61.35 |

---

# Approfondimento tecnico — Solana (SOL-USD)

## Semaforo: 🟢 VERDE / Favorevole

**Prezzo attuale:** 101,86 $

Solana ha un segnale favorevole. La statistica dei casi simili indica più possibilità di salita che di discesa, ma resta comunque una probabilità, non una certezza.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **67,50%**
- Casi negativi dopo 30 giorni: **32,50%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **84,77%**
- Rendimento medio dopo 30 giorni: **44,85%**
- Rendimento centrale dopo 30 giorni: **33,19%**
- Discesa media durante i 30 giorni: **-11,97%**
- Massimo rialzo medio durante i 30 giorni: **70,23%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **147,54 $**
- Scenario centrale a 30 giorni: **135,67 $**
- Zona di rischio media: **89,67 $**
- Zona di rialzo media: **173,40 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -20,92% → **80,55 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -6,12% → **95,63 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: 33,19% → **135,67 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 67,90% → **171,03 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 119,22% → **223,29 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -33,87% → **67,36 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -22,30% → **79,14 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -5,29% → **96,47 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -1,13% → **100,71 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: 0,00% → **101,86 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 3,15% → **105,06 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 14,96% → **117,10 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 46,65% → **149,38 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 72,84% → **176,06 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 179,77% → **284,97 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| RUNE-USD        | 2020-03-23   | 2020-06-30 |        88.53 |        34.53 |           0    |          68.29 |
| VET-USD         | 2020-03-14   | 2020-06-21 |        87.86 |       103.01 |           0    |         132.4  |
| ZIL-USD         | 2020-09-05   | 2020-12-13 |        87.54 |        90.17 |           0    |         174.35 |
| HBAR-USD        | 2020-10-30   | 2021-02-06 |        87.49 |        70.94 |          -5.6  |          70.94 |
| BNB-USD         | 2023-10-08   | 2024-01-15 |        87.44 |         5.25 |          -8.08 |           5.25 |
| VET-USD         | 2023-08-16   | 2023-11-23 |        86.86 |        67.32 |           0    |          69.67 |
| BNB-USD         | 2018-11-23   | 2019-03-02 |        86.35 |        51.23 |          -2.8  |          51.23 |
| RUNE-USD        | 2026-02-05   | 2026-05-15 |        86.32 |       -20.87 |         -35.52 |           0    |
| ETH-USD         | 2020-05-11   | 2020-08-18 |        86.04 |        -8.18 |         -20.87 |          12.6  |
| THETA-USD       | 2023-08-18   | 2023-11-25 |        86.03 |        39.6  |          -6.15 |          39.6  |

---

# Approfondimento tecnico — Dogecoin (DOGE-USD)

## Semaforo: 🔴 ROSSO / Prudenza

**Prezzo attuale:** 0,08 $

Dogecoin richiede prudenza. La statistica dei casi simili indica più possibilità di discesa che di salita. Con leva, il rischio principale è il drawdown durante il percorso.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **25,00%**
- Casi negativi dopo 30 giorni: **75,00%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **79,83%**
- Rendimento medio dopo 30 giorni: **-5,05%**
- Rendimento centrale dopo 30 giorni: **-14,87%**
- Discesa media durante i 30 giorni: **-20,13%**
- Massimo rialzo medio durante i 30 giorni: **22,07%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **0,08 $**
- Scenario centrale a 30 giorni: **0,07 $**
- Zona di rischio media: **0,07 $**
- Zona di rialzo media: **0,10 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -26,74% → **0,06 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -23,96% → **0,06 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: -14,87% → **0,07 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: -1,36% → **0,08 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 48,16% → **0,13 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -32,15% → **0,06 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -29,75% → **0,06 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -18,58% → **0,07 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -11,13% → **0,08 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: -4,61% → **0,08 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 2,70% → **0,09 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 6,70% → **0,09 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 12,36% → **0,10 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 25,39% → **0,11 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 48,36% → **0,13 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| MANA-USD        | 2022-10-28   | 2023-02-04 |        85.64 |       -21.58 |         -26.1  |           3.31 |
| DASH-USD        | 2019-10-29   | 2020-02-05 |        82.87 |       -23.73 |         -30.58 |           9.23 |
| FIL-USD         | 2022-05-15   | 2022-08-22 |        82.68 |       -16.45 |         -16.88 |           3.53 |
| QTUM-USD        | 2021-05-21   | 2021-08-28 |        82.33 |       -26.32 |         -26.32 |          27.97 |
| BTC-USD         | 2025-02-07   | 2025-05-17 |        82.1  |         3.49 |          -1.57 |           8.22 |
| SAND-USD        | 2021-04-25   | 2021-08-02 |        81.82 |        63.91 |          -4.99 |          63.91 |
| EOS-USD         | 2019-10-29   | 2020-02-05 |        81.8  |       -15.18 |         -22.3  |          18.74 |
| NEAR-USD        | 2022-10-28   | 2023-02-04 |        81.31 |       -17.77 |         -18.69 |           7.88 |
| MANA-USD        | 2025-02-04   | 2025-05-14 |        81.28 |       -25.9  |         -27.91 |           0    |
| XRP-USD         | 2021-05-26   | 2021-09-02 |        81.21 |       -17.32 |         -30.25 |          10.59 |

</details>
<!-- COMPACT_SECTION_END:scanner_full_detail -->

<!-- COMPACT_SECTION_START:market_regime -->
<details>
<summary><strong>🌦️ Market Regime Match</strong></summary>

<!-- MARKET_REGIME_MATCH_START -->
# Market Regime Match Report


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [market_regime_match_report.md](market_regime_match_report.md)

Generated: 2026-09-13 05:31 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | snapshot_date   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | 2026-09-13 | RECOVERY | 77.274 $ | True | 16.57% | -4.66% | RECOVERY | 16.57% | -4.66% |
| DOGE-USD | 2026-09-13 | BEAR | 0.08481 $ | False | -3.74% | -12.08% | RECOVERY | 16.57% | -4.66% |
| SOL-USD | 2026-09-13 | RECOVERY | 101,86 $ | True | 37.69% | -8.81% | RECOVERY | 16.57% | -4.66% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 85.00% | 36.97% | 57.03% | 71.50% | -4.81% | -33.88% | 40.49% | 69.13% | 108.26% | 72.50% | 19.47% | 65.68% | 136.80% |
| BTC-USD | SAME_BTC_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| BTC-USD | SAME_ASSET_REGIME | 1 | 100.00% | 47.51% | 47.51% | 47.51% | -6.93% | -6.93% | 68.95% | 68.95% | 68.95% | 100.00% | 137.57% | 137.57% | 137.57% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| DOGE-USD | ALL_MATCHES | 40 | 25.00% | -14.87% | -1.36% | 48.16% | -18.58% | -32.15% | 12.36% | 25.39% | 48.36% | 35.00% | -8.57% | 7.07% | 44.50% |
| DOGE-USD | SAME_BTC_REGIME | 1 | 0.00% | -31.54% | -31.54% | -31.54% | -34.03% | -34.03% | 7.07% | 7.07% | 7.07% | 0.00% | -69.31% | -69.31% | -69.31% |
| DOGE-USD | SAME_ASSET_REGIME | 20 | 15.00% | -15.82% | -10.24% | 2.06% | -17.80% | -30.83% | 9.93% | 15.47% | 26.34% | 25.00% | -16.09% | -1.25% | 44.50% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL-USD | ALL_MATCHES | 40 | 67.50% | 33.19% | 67.90% | 119.22% | -5.29% | -33.87% | 46.65% | 72.84% | 179.77% | 67.50% | 18.89% | 132.32% | 199.13% |
| SOL-USD | SAME_BTC_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL-USD | SAME_ASSET_REGIME | 3 | 33.33% | -1.22% | 23.15% | 37.77% | -6.93% | -19.62% | 59.94% | 64.45% | 67.15% | 33.33% | -13.67% | 61.95% | 107.32% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 26 | 88.46% | 35.08% | -4.94% | 63.36% | 69.23% | 18.19% | 94.47% |
| BTC-USD | HISTORICAL_BTC_BULL | 14 | 78.57% | 37.34% | -3.58% | 75.96% | 78.57% | 20.72% | 106.11% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 23 | 13.04% | -16.45% | -18.69% | 21.71% | 21.74% | -10.67% | 23.36% |
| DOGE-USD | HISTORICAL_BTC_BULL | 10 | 60.00% | 6.80% | -11.08% | 59.59% | 70.00% | 18.13% | 100.76% |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION | 6 | 16.67% | -18.12% | -26.27% | 16.83% | 33.33% | -46.33% | 29.41% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 1 | 0.00% | -31.54% | -34.03% | 7.07% | 0.00% | -69.31% | 7.07% |
| SOL-USD | HISTORICAL_BTC_BEAR | 24 | 62.50% | 16.05% | -6.37% | 59.90% | 62.50% | 12.12% | 98.80% |
| SOL-USD | HISTORICAL_BTC_BULL | 14 | 85.71% | 69.13% | -1.10% | 174.31% | 85.71% | 148.45% | 291.62% |
| SOL-USD | HISTORICAL_BTC_DISTRIBUTION | 2 | 0.00% | -18.29% | -27.18% | 9.56% | 0.00% | -18.67% | 9.56% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 33 | 87.88% | 36.85% | -4.10% | 61.35% | 72.73% | 16.21% | 81.97% |
| BTC-USD | HISTORICAL_ASSET_BULL | 5 | 60.00% | 0.90% | -10.45% | 131.17% | 60.00% | 18.76% | 171.02% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 100.00% | 48.87% | -33.92% | 78.05% | 100.00% | 170.45% | 192.55% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 1 | 100.00% | 47.51% | -6.93% | 68.95% | 100.00% | 137.57% | 144.47% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 20 | 15.00% | -15.82% | -17.80% | 15.47% | 25.00% | -16.09% | 20.48% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 14 | 42.86% | -7.73% | -20.94% | 46.04% | 57.14% | 1.14% | 59.08% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 50.00% | -10.17% | -15.94% | 34.33% | 50.00% | 9.46% | 34.50% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 4 | 0.00% | -28.72% | -30.97% | 9.30% | 0.00% | -12.71% | 9.30% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 28 | 67.86% | 26.15% | -5.84% | 63.09% | 67.86% | 15.60% | 98.80% |
| SOL-USD | HISTORICAL_ASSET_BULL | 4 | 75.00% | 112.37% | -1.27% | 191.58% | 75.00% | 132.76% | 283.98% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 5 | 80.00% | 90.17% | -2.53% | 228.48% | 80.00% | 170.45% | 282.85% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 3 | 33.33% | -1.22% | -6.93% | 64.45% | 33.33% | -13.67% | 102.21% |

## Top regime-adjusted matches

A single cohort is selected deterministically: SAME_BTC_AND_ASSET_REGIME, otherwise SAME_ASSET_REGIME, otherwise SAME_BTC_REGIME. Each level must have at least 5 matches; cohorts are never combined.

| target   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level        | selection_reason              |
|:---------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:----------------------|:------------------------------|
| BTC-USD | NONE | 0 | 1 | 0 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES |
| DOGE-USD | SAME_ASSET_REGIME | 0 | 20 | 1 | 20 | 5 | 1_SAME_ASSET_FALLBACK | FALLBACK_TO_SAME_ASSET_REGIME |
| SOL-USD | NONE | 0 | 3 | 0 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES |

- WARNING DOGE-USD: SAME_ASSET_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| DOGE-USD | MANA-USD | 2022-10-28 | 85.64% | BEAR | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -21.58% | -26.10% | 3.31% | -21.11% | -33.73% | 3.31% |
| DOGE-USD | DASH-USD | 2019-10-29 | 82.87% | DISTRIBUTION | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -23.73% | -30.58% | 9.23% | -45.15% | -64.88% | 9.23% |
| DOGE-USD | FIL-USD | 2022-05-15 | 82.68% | BEAR | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -16.45% | -16.88% | 3.53% | -21.51% | -21.73% | 3.53% |
| DOGE-USD | EOS-USD | 2019-10-29 | 81.80% | DISTRIBUTION | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -15.18% | -22.30% | 18.74% | -47.68% | -59.08% | 18.74% |
| DOGE-USD | NEAR-USD | 2022-10-28 | 81.31% | BEAR | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -17.77% | -18.69% | 7.88% | -18.91% | -28.44% | 7.88% |
| DOGE-USD | YFI-USD | 2025-02-08 | 81.03% | BULL | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -11.00% | -11.00% | 5.38% | 5.57% | -17.54% | 5.57% |
| DOGE-USD | ENJ-USD | 2022-10-28 | 80.91% | BEAR | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -10.74% | -12.44% | 14.38% | -10.30% | -25.78% | 14.38% |
| DOGE-USD | ETH-USD | 2025-02-19 | 80.29% | DISTRIBUTION | BEAR | SAME_ASSET_ONLY | MIXED | -7.43% | -15.36% | 6.87% | 43.86% | -15.36% | 47.20% |
| DOGE-USD | QTUM-USD | 2022-05-11 | 79.94% | BEAR | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -18.16% | -20.89% | 0.00% | -27.54% | -30.31% | 0.00% |
| DOGE-USD | CRV-USD | 2022-10-27 | 79.77% | BEAR | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -16.58% | -18.47% | 13.52% | -10.67% | -24.70% | 13.52% |

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

Generato: 2026-09-13 05:32 UTC


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
| BTC | 77.274 $ | -3 | DEBOLE / NON CONFERMATO | STAGE 3 / DISTRIBUZIONE O PAUSA | VOLATILITÀ IN ESPANSIONE | RANGE / FASE NON CHIARA | MEDIO | RIDUCI RISCHIO / NO LONG A LEVA |
| SOL | 101,86 $ | 0 | NEUTRALE / MISTO | STAGE 3 / DISTRIBUZIONE O PAUSA | COMPRESSIONE / TRIANGOLO POSSIBILE | SIGN OF STRENGTH POSSIBILE | BASSO | HOLD LEGGERO / ATTESA CONFERME |
| DOGE | 0.08481 $ | -7 | RIBASSISTA / FRAGILE | STAGE 4 / MARKDOWN | COMPRESSIONE / TRIANGOLO POSSIBILE | ACCUMULO POSSIBILE / RANGE BASSO | MEDIO | NO LONG / SHORT SOLO DOPO SPIKE E REJECTION |

## Punteggi per area

| Asset | Trend | Struttura | Momentum | Volume | Prezzo | Candela | Wyckoff | Totale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 0 | 0 | -2 | -1 | 0 | 0 | 0 | -3 |
| SOL | 0 | 0 | -2 | 0 | 0 | 0 | +2 | 0 |
| DOGE | -3 | 0 | -2 | -2 | 0 | 0 | 0 | -7 |

## Livelli tecnici

| Asset | Supporto | Resistenza | Breakout 60g | Breakdown 60g | ATR14 | Rendimento 30g | Rendimento 90g |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 76.909 $ | 77.991 $ | 82.262 $ | 61.769 $ | 2,76% | 21,88% | 17,60% |
| SOL | 97,45 $ | 107,12 $ | 110,04 $ | 70,69 $ | 4,06% | 33,71% | 43,13% |
| DOGE | 0.08189 $ | 0.08494 $ | 0.09998 $ | 0.06797 $ | 4,99% | 21,02% | -4,45% |

## Lettura dettagliata

### BTC

- Prezzo: **77.274 $**
- Score classico: **-3 / 12**
- Verdetto: **DEBOLE / NON CONFERMATO**
- Azione coerente: **RIDUCI RISCHIO / NO LONG A LEVA**
- Volatilità tecnica locale: **MEDIO** — ATR14 2,76%; distanza supporto 0,48%; distanza resistenza 0,93%

Dettaglio:

- Trend: **0** — prezzo sopra MA200 daily; MA50 daily in salita; MA200 daily in discesa; STAGE 3 / DISTRIBUZIONE O PAUSA
- Stage weekly: **STAGE 3 / DISTRIBUZIONE O PAUSA** — Prezzo sopra MA30 weekly ma pendenza debole o piatta.
- Struttura: **0** — VOLATILITÀ IN ESPANSIONE
- Momentum: **-2** — RSI sano 55.1; RSI in peggioramento; MACD sotto signal; istogramma MACD in peggioramento
- Volume: **-1** — OBV sotto media; CMF neutrale -0.03; volume ratio 0.40
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **0** — Doji / indecisione
- Wyckoff: **0** — RANGE / FASE NON CHIARA. Nessuna fase Wyckoff pulita.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 55.11 |
| MACD histogram | -760.09159 |
| CMF20 | -0.029 |
| Volume ratio 20 | 0.40 |
| MA20 | 78.588 $ |
| MA50 | 70.909 $ |
| MA100 | 67.008 $ |
| MA200 | 70.091 $ |
| Pendenza MA50 20g | +8,83% |
| Pendenza MA200 60g | -4,80% |
| Bollinger width | 6,39% |
| Bollinger position | 0.23 |

### SOL

- Prezzo: **101,86 $**
- Score classico: **0 / 12**
- Verdetto: **NEUTRALE / MISTO**
- Azione coerente: **HOLD LEGGERO / ATTESA CONFERME**
- Volatilità tecnica locale: **BASSO** — ATR14 4,06%; distanza supporto 4,52%; distanza resistenza 5,16%

Dettaglio:

- Trend: **0** — prezzo sopra MA200 daily; MA50 daily in salita; MA200 daily in discesa; STAGE 3 / DISTRIBUZIONE O PAUSA
- Stage weekly: **STAGE 3 / DISTRIBUZIONE O PAUSA** — Prezzo sopra MA30 weekly ma pendenza debole o piatta.
- Struttura: **0** — COMPRESSIONE / TRIANGOLO POSSIBILE
- Momentum: **-2** — RSI sano 57.5; RSI in peggioramento; MACD sotto signal; istogramma MACD in peggioramento
- Volume: **0** — OBV sotto media; CMF positivo 0.07; volume ratio 0.40
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **0** — Doji / indecisione
- Wyckoff: **+2** — SIGN OF STRENGTH POSSIBILE. Prezzo nella parte alta del range con flusso volume positivo.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 57.53 |
| MACD histogram | -1.14544 |
| CMF20 | 0.065 |
| Volume ratio 20 | 0.40 |
| MA20 | 102,44 $ |
| MA50 | 87,43 $ |
| MA100 | 80,44 $ |
| MA200 | 83,04 $ |
| Pendenza MA50 20g | +12,97% |
| Pendenza MA200 60g | -9,05% |
| Bollinger width | 11,26% |
| Bollinger position | 0.45 |

### DOGE

- Prezzo: **0.08481 $**
- Score classico: **-7 / 12**
- Verdetto: **RIBASSISTA / FRAGILE**
- Azione coerente: **NO LONG / SHORT SOLO DOPO SPIKE E REJECTION**
- Volatilità tecnica locale: **MEDIO** — ATR14 4,99%; distanza supporto 3,58%; distanza resistenza 0,14%

Dettaglio:

- Trend: **-3** — prezzo sotto MA200 daily; MA50 daily in salita; MA200 daily in discesa; STAGE 4 / MARKDOWN
- Stage weekly: **STAGE 4 / MARKDOWN** — Prezzo sotto MA30 weekly con MA30 in discesa.
- Struttura: **0** — COMPRESSIONE / TRIANGOLO POSSIBILE
- Momentum: **-2** — RSI sano 51.9; RSI in peggioramento; MACD sotto signal; istogramma MACD in peggioramento
- Volume: **-2** — OBV sotto media; CMF negativo -0.13; volume ratio 0.39
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **0** — Doji / indecisione
- Wyckoff: **0** — ACCUMULO POSSIBILE / RANGE BASSO. Prezzo nella metà bassa del range, ma senza spring confermato.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 51.90 |
| MACD histogram | -0.00078 |
| CMF20 | -0.129 |
| Volume ratio 20 | 0.39 |
| MA20 | 0.08616 $ |
| MA50 | 0.07821 $ |
| MA100 | 0.07799 $ |
| MA200 | 0.08815 $ |
| Pendenza MA50 20g | +7,19% |
| Pendenza MA200 60g | -12,30% |
| Bollinger width | 14,71% |
| Bollinger position | 0.39 |

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

Generato: 2026-09-13 05:32 UTC


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
| BTC | 77.274 $ | Doppio massimo | CANDIDATO | ribassista | n/a | 58.946 $ | n/a | 24,18% | Fib 23,6% TENUTO (+1) @ 76.477 $ | NEL RANGE | 76.248 $ |
| SOL | 101,86 $ | Doppio massimo | CANDIDATO | ribassista | n/a | 84,86 $ | n/a | 4,52% | Fib 23,6% NON ATTIVO (0) @ 96,09 $ | NEL RANGE | 97,45 $ |
| DOGE | 0.08481 $ | Doppio massimo | CANDIDATO | ribassista | n/a | 0.06214 $ | n/a | 24,77% | Fib 38,2% TENUTO (0) @ 0.08419 $ | NEL RANGE | 0.08028 $ |

## BTC

![Classic visual BTC](classic_visual_BTC.png)

- Pattern principale: **Doppio massimo**
- Stato pattern: **CANDIDATO** (0)
- Famiglia: **ribassista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-07-15 -> 2026-08-09**
- Età formazione: **35 giorni**
- Breakout pattern: **n/a**
- Età breakout: **n/a**
- Neckline: **62.227 $**
- Target teorico: **58.946 $**
- Progresso verso target: **n/a**
- Distanza dalla neckline: **24,18%**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 23,6% TENUTO (+1) @ 76.477 $** — Swing UP 2026-07-01 57.748 -> 2026-09-03 82.262; livello più vicino 23.6% a 76.477; stato TENUTO; confluenza: supporto tecnico.
- Invalidazione: **63.471 $**
- Relazione prezzo/neckline: **sopra neckline**
- Dettaglio: Due massimi simili vicino a 65.508 tra 2026-07-15 e 2026-08-09. Neckline ribassista stimata: 62.227. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 35 giorni. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Doji / indecisione**
- Stato prezzo: **NEL RANGE**
- Supporto: **76.248 $**
- Resistenza: **77.991 $**
- Breakout 60g: **82.262 $**
- Breakdown 60g: **61.769 $**
- RSI14: **55.11**
- ATR14: **2,76%**
- Volume ratio 20g: **0.40**
- Rendimento 30g: **+21,88%**
- Rendimento 90g: **+17,60%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Triangolo ascendente possibile | CANDIDATO | 0 | rialzista | n/a | n/a | n/a | n/a | n/a | n/a | n/a | Resistenza quasi piatta e minimi crescenti. Stato: CANDIDATO; il pattern non ha una neckline univoca da usare per il lifecycle. |
| Doppio minimo | CANDIDATO | 0 | rialzista | 82.792 $ | n/a | n/a | 90.626 $ | n/a | 7,14% | 81.136 $ | Due minimi simili a 74.959 $ e 76.248 $. Neckline circa 82.792 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 11 giorni. |
| Doppio massimo | CANDIDATO | 0 | ribassista | 62.227 $ | n/a | n/a | 58.946 $ | n/a | 24,18% | 63.471 $ | Due massimi simili a 65.508 $ e 65.402 $. Neckline circa 62.227 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 35 giorni. |

## SOL

![Classic visual SOL](classic_visual_SOL.png)

- Pattern principale: **Doppio massimo**
- Stato pattern: **CANDIDATO** (0)
- Famiglia: **ribassista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-08-27 -> 2026-09-06**
- Età formazione: **7 giorni**
- Breakout pattern: **n/a**
- Età breakout: **n/a**
- Neckline: **97,45 $**
- Target teorico: **84,86 $**
- Progresso verso target: **n/a**
- Distanza dalla neckline: **4,52%**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 23,6% NON ATTIVO (0) @ 96,09 $** — Swing UP 2026-06-06 60,41 -> 2026-09-06 107,12; livello più vicino 23.6% a 96,09; stato NON ATTIVO; confluenza: supporto tecnico, neckline ribassista.
- Invalidazione: **99,40 $**
- Relazione prezzo/neckline: **sopra neckline**
- Dettaglio: Due massimi simili vicino a 110,04 tra 2026-08-27 e 2026-09-06. Neckline ribassista stimata: 97,45. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 7 giorni. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Doji / indecisione**
- Stato prezzo: **NEL RANGE**
- Supporto: **97,45 $**
- Resistenza: **107,12 $**
- Breakout 60g: **110,04 $**
- Breakdown 60g: **70,69 $**
- RSI14: **57.53**
- ATR14: **4,06%**
- Volume ratio 20g: **0.40**
- Rendimento 30g: **+33,71%**
- Rendimento 90g: **+43,13%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Doppio massimo | CANDIDATO | 0 | ribassista | 97,45 $ | n/a | n/a | 84,86 $ | n/a | 4,52% | 99,40 $ | Due massimi simili a 110,04 $ e 107,12 $. Neckline circa 97,45 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 7 giorni. |
| Triangolo ascendente possibile | CANDIDATO | 0 | rialzista | n/a | n/a | n/a | n/a | n/a | n/a | n/a | Resistenza quasi piatta e minimi crescenti. Stato: CANDIDATO; il pattern non ha una neckline univoca da usare per il lifecycle. |
| Testa e spalle inverso | TARGET RAGGIUNTO | 0 | rialzista | 78,17 $ | 2026-08-19 | 25g | 85,65 $ | 316,81% | n/a | 76,61 $ | Spalla sinistra 73,40 $, testa 70,69 $, spalla destra 74,20 $. Neckline circa 78,17 $. Breakout neckline: 2026-08-19 (25 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 85,65 $; progresso: 316,81%; prezzo sopra neckline. |
| Doppio minimo | TARGET RAGGIUNTO | 0 | rialzista | 78,73 $ | 2026-08-19 | 25g | 84,05 $ | 434,50% | n/a | 77,15 $ | Due minimi simili a 73,40 $ e 74,20 $. Neckline circa 78,73 $. Breakout neckline: 2026-08-19 (25 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 84,05 $; progresso: 434,50%; prezzo sopra neckline. |

## DOGE

![Classic visual DOGE](classic_visual_DOGE.png)

- Pattern principale: **Doppio massimo**
- Stato pattern: **CANDIDATO** (0)
- Famiglia: **ribassista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-07-26 -> 2026-08-11**
- Età formazione: **33 giorni**
- Breakout pattern: **n/a**
- Età breakout: **n/a**
- Neckline: **0.06797 $**
- Target teorico: **0.06214 $**
- Progresso verso target: **n/a**
- Distanza dalla neckline: **24,77%**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 38,2% TENUTO (0) @ 0.08419 $** — Swing UP 2026-08-01 0.06797 -> 2026-09-05 0.09421; livello più vicino 38.2% a 0.08419; stato TENUTO; confluenza: nessuna confluenza indipendente.
- Invalidazione: **0.06933 $**
- Relazione prezzo/neckline: **sopra neckline**
- Dettaglio: Due massimi simili vicino a 0.07380 tra 2026-07-26 e 2026-08-11. Neckline ribassista stimata: 0.06797. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 33 giorni. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Doji / indecisione**
- Stato prezzo: **NEL RANGE**
- Supporto: **0.08028 $**
- Resistenza: **0.09169 $**
- Breakout 60g: **0.09998 $**
- Breakdown 60g: **0.06797 $**
- RSI14: **51.88**
- ATR14: **5,00%**
- Volume ratio 20g: **0.39**
- Rendimento 30g: **+21,00%**
- Rendimento 90g: **-4,46%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Doppio massimo | CANDIDATO | 0 | ribassista | 0.06797 $ | n/a | n/a | 0.04174 $ | n/a | 24,77% | 0.06933 $ | Due massimi simili a 0.09169 $ e 0.09421 $. Neckline circa 0.06797 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 8 giorni. |
| Triangolo ascendente possibile | CANDIDATO | 0 | rialzista | n/a | n/a | n/a | n/a | n/a | n/a | n/a | Resistenza quasi piatta e minimi crescenti. Stato: CANDIDATO; il pattern non ha una neckline univoca da usare per il lifecycle. |
| Doppio minimo | TARGET RAGGIUNTO | 0 | rialzista | 0.07923 $ | 2026-08-20 | 24g | 0.08952 $ | 54,23% | n/a | 0.07765 $ | Due minimi simili a 0.06961 $ e 0.06895 $. Neckline circa 0.07923 $. Breakout neckline: 2026-08-20 (24 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 0.08952 $; progresso: 54,23%; prezzo sopra neckline. |

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

Generato: 2026-09-13 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [fractal_path_tracker.md](fractal_path_tracker.md)

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-09-13**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-02-28**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **101,86 $**
- Verdetto principale: **ANALOGIA DEBOLE / SCENARIO SECONDARIO**
- Somiglianza strutturale: **+70,17%**
- Aderenza live principale: **+72,50%**
- Errore medio live principale: **13,75%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE SOLO DI CONTESTO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **99**
- Osservazioni inclusive dal bottom: **100**
- Osservazioni da inizio programma/scanner: **73**
- Errore assoluto medio dal bottom: **11,66%**
- Errore assoluto medio da inizio programma: **13,75%**
- Gap firmato medio ultimi 7 giorni: **+10,05%**
- Errore assoluto medio ultimi 7 giorni: **10,05%**
- Gap ultimo giorno: **+11,71%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **+11,71%**
- Gap firmato medio 7g: **+10,05%**
- Errore assoluto medio 7g: **10,05%**
- Variazione recente gap: **+3,61%**
- Stato gap: **SOPRA IL FRATTALE**
- Trend gap: **SOL sta aumentando il distacco sopra il percorso ancorato**

Soglie operative del grafico:

- entro **±5%**: percorso vicino;
- tra **±5% e ±12%**: deviazione gestibile;
- oltre **±12%**: frattale non abbastanza aderente per conferma operativa;
- oltre **±18%**: disallineamento marcato.

## Ultimi giorni del confronto ancorato

|   Giorno | Data SOL   | Data BTC eq.   | SOL reale   | Percorso ancorato   | Gap firmato   | Fase                |
|---------:|:-----------|:---------------|:------------|:--------------------|:--------------|:--------------------|
| 90 | 2026-09-04 | 2023-02-19 | 101,95 $ | 95,83 $ | +6,38% | da inizio programma |
| 91 | 2026-09-05 | 2023-02-20 | 103,19 $ | 97,81 $ | +5,50% | da inizio programma |
| 92 | 2026-09-06 | 2023-02-21 | 106,45 $ | 96,26 $ | +10,58% | da inizio programma |
| 93 | 2026-09-07 | 2023-02-22 | 103,87 $ | 95,29 $ | +9,01% | da inizio programma |
| 94 | 2026-09-08 | 2023-02-23 | 103,33 $ | 94,33 $ | +9,53% | da inizio programma |
| 95 | 2026-09-09 | 2023-02-24 | 101,61 $ | 91,38 $ | +11,19% | da inizio programma |
| 96 | 2026-09-10 | 2023-02-25 | 98,69 $ | 91,29 $ | +8,10% | da inizio programma |
| 97 | 2026-09-11 | 2023-02-26 | 102,40 $ | 92,81 $ | +10,33% | da inizio programma |
| 98 | 2026-09-12 | 2023-02-27 | 102,40 $ | 92,66 $ | +10,51% | da inizio programma |
| 99 | 2026-09-13 | 2023-02-28 | 101,86 $ | 91,18 $ | +11,71% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-09-20 | 87,53 $ | 97,78 $ | 97,78 $ / 104,06 $ | no | n/a | n/a | n/a |
| 14g | 2026-09-27 | 97,48 $ | 108,90 $ | 88,83 $ / 108,90 $ | no | n/a | n/a | n/a |
| 21g | 2026-10-04 | 110,99 $ | 123,99 $ | 88,83 $ / 123,99 $ | no | n/a | n/a | n/a |
| 28g | 2026-10-11 | 107,42 $ | 119,99 $ | 88,83 $ / 124,68 $ | no | n/a | n/a | n/a |
| 35g | 2026-10-18 | 110,96 $ | 123,95 $ | 88,83 $ / 125,32 $ | no | n/a | n/a | n/a |
| 42g | 2026-10-25 | 119,10 $ | 133,05 $ | 88,83 $ / 133,05 $ | no | n/a | n/a | n/a |
| 49g | 2026-11-01 | 119,74 $ | 133,76 $ | 88,83 $ / 134,15 $ | no | n/a | n/a | n/a |
| 56g | 2026-11-08 | 111,51 $ | 124,57 $ | 88,83 $ / 134,15 $ | no | n/a | n/a | n/a |
| 63g | 2026-11-15 | 112,98 $ | 126,21 $ | 88,83 $ / 134,15 $ | no | n/a | n/a | n/a |
| 70g | 2026-11-22 | 108,95 $ | 121,71 $ | 88,83 $ / 134,15 $ | no | n/a | n/a | n/a |
| 77g | 2026-11-29 | 106,50 $ | 118,97 $ | 88,83 $ / 134,15 $ | no | n/a | n/a | n/a |
| 84g | 2026-12-06 | 107,25 $ | 119,81 $ | 88,83 $ / 134,15 $ | no | n/a | n/a | n/a |
| 91g | 2026-12-13 | 109,13 $ | 121,90 $ | 88,83 $ / 134,15 $ | no | n/a | n/a | n/a |
| 98g | 2026-12-20 | 107,30 $ | 119,86 $ | 88,83 $ / 134,15 $ | no | n/a | n/a | n/a |
| 105g | 2026-12-27 | 102,10 $ | 114,06 $ | 88,83 $ / 134,15 $ | no | n/a | n/a | n/a |
| 112g | 2027-01-03 | 111,59 $ | 124,66 $ | 88,83 $ / 134,15 $ | no | n/a | n/a | n/a |
| 119g | 2027-01-10 | 120,89 $ | 135,04 $ | 88,83 $ / 135,08 $ | no | n/a | n/a | n/a |
| 126g | 2027-01-17 | 121,24 $ | 135,44 $ | 88,83 $ / 137,10 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 59 | 38,98% | 10,48% | 12,66% |
| 14g | 52 | 25,00% | 17,47% | 11,53% |
| 21g | 45 | 13,33% | 26,14% | 13,00% |
| 28g | 38 | 28,95% | 26,37% | 12,67% |
| 35g | 33 | 39,39% | 19,32% | 11,67% |
| 42g | 26 | 76,92% | 10,59% | 10,83% |
| 49g | 19 | 100,00% | 5,61% | 10,55% |
| 56g | 12 | 100,00% | 6,43% | 9,28% |
| 63g | 5 | 100,00% | 6,29% | 10,85% |
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

</details>
<!-- COMPACT_SECTION_END:fractal_path -->

<!-- COMPACT_SECTION_START:exchange_microstructure -->
<details>
<summary><strong>🏦 Dati exchange, liquidità e leva</strong></summary>

<!-- EXCHANGE_MICROSTRUCTURE_START -->
# Dati exchange, liquidità e leva

Generato: 2026-09-13 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [exchange_microstructure_report.md](exchange_microstructure_report.md)

Questo modulo legge Kraken Futures, Bitget Futures e KuCoin Futures come nucleo derivati. OKX e Coinbase vengono raccolti come fonti ausiliarie non pesate.
Non modifica la formula matematica di RSI, Fibonacci o Wyckoff: controlla se quei segnali sono sostenuti da acquisti, vendite, OI, funding e liquidità.

**Limite importante:** questo nucleo non assume disponibile un feed pubblico completo delle liquidazioni. La componente liquidazioni resta neutrale; le zone future restano stime di pressione, non dati certi delle singole posizioni.

Diagnostica completa: [exchange_source_diagnostics.md](exchange_source_diagnostics.md)

## Sintesi

| Asset | Prezzo | Exchange | Segnale candidato | Peso Global | Bias exchange | Confidenza | Copertura | Funding 8h eq. | OI 24h | Taker flow (campione/4h) | Book 0,5% | Liq long campione | Liq short campione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 77.195 $ | 3 | 0 | 0 | LEGGERMENTE POSITIVA / NON PESATA | MEDIA | 100% | +0,0060% | +0,69% | 7,57 | +0,52% | 0 $ | 0 $ |
| SOL | 101,72 $ | 3 | 0 | 0 | LEGGERMENTE POSITIVA / NON PESATA | BASSA | 100% | +0,0023% | -1,45% | 1,61 | +10,62% | 0 $ | 0 $ |
| DOGE | 0.08469 $ | 3 | 0 | 0 | LEGGERMENTE POSITIVA / NON PESATA | BASSA | 100% | +0,0072% | -2,64% | 2,19 | +2,48% | 0 $ | 0 $ |

Il segnale candidato è limitato a **±1**, ma il peso nel Global resta **0** finché il tracker a 7 giorni non raggiunge 30 controlli, almeno 55% di accuratezza e return corretto direzione positivo. Un singolo muro o funding non basta.

La colonna taker usa un campione recente nel primo run. Dopo almeno 3 fotografie distribuite su almeno 45 minuti viene sostituita automaticamente dalla media intraday 4h.

## Dati separati per exchange

| Asset | Exchange | Stato | Funding 8h eq. | Open interest | Taker flow | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | Kraken | OK | +0,0094% | 141,15 mln $ | 515,69 | +4,76% |
| BTC | Bitget | OK | +0,0081% | 2,73 mld $ | 1,65 | -16,17% |
| BTC | Kucoin | OK | +0,0025% | 887,44 mln $ | 0,97 | -4,61% |
| SOL | Kraken | OK | +0,0016% | 26,26 mln $ | 0,85 | +9,29% |
| SOL | Bitget | OK | +0,0032% | 434,44 mln $ | 3,26 | +30,09% |
| SOL | Kucoin | OK | +0,0036% | 181,49 mln $ | 1,40 | -4,63% |
| DOGE | Kraken | OK | -0,0045% | 4,07 mln $ | 0,77 | +1,91% |
| DOGE | Bitget | OK | +0,0097% | 109,17 mln $ | 0,25 | -10,98% |
| DOGE | Kucoin | OK | +0,0056% | 60,37 mln $ | 0,61 | -6,94% |

Kraken, Bitget e KuCoin contribuiscono a funding normalizzato, open interest, trade aggressivi e order book. Non viene inventato un long/short ratio pubblico né un feed completo delle liquidazioni.

## Conferme per indicatori tecnici

### BTC

- Score grezzo exchange: **+2,25**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 5, accuratezza +40,00%.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 1, bear 0, divergenze 0.
- Flusso taker/order book: **+1,75**.
- OI/funding/basis: **+0,00**.
- Affollamento long/short: **+0,00**.
- Liquidazioni: **NON PESATE / FEED COMPLETO NON ASSUNTO DISPONIBILE**.
- **Wyckoff:** Fase Wyckoff non abbastanza chiara per una conferma exchange.
- **Fibonacci:** Fibonacci tenuto con acquisti/assorbimento coerenti: conferma positiva. Confluenza tecnica dichiarata: supporto tecnico.
- **RSI:** RSI in zona non estrema o flusso exchange non abbastanza netto.
- **Pattern:** I pattern candidati restano non operativi: i dati exchange possono solo preparare la conferma.
- **Breakout/breakdown:** Supporto vicino con assorbimento/acquisti: tenuta più credibile.
- **Mappa liquidità attuale:** muro bid: n/a; muro ask: n/a

![Microstruttura exchange BTC](exchange_microstructure_BTC.png)

### SOL

- Score grezzo exchange: **+2,00**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 5, accuratezza +60,00%.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 2, bear 0, divergenze 0.
- Flusso taker/order book: **+2,00**.
- OI/funding/basis: **+0,00**.
- Affollamento long/short: **+0,00**.
- Liquidazioni: **NON PESATE / FEED COMPLETO NON ASSUNTO DISPONIBILE**.
- **Wyckoff:** Fase Wyckoff non abbastanza chiara per una conferma exchange.
- **Fibonacci:** Fibonacci non_attivo; nessuna conferma exchange netta. Confluenza tecnica dichiarata: supporto tecnico, neckline ribassista.
- **RSI:** RSI in zona non estrema o flusso exchange non abbastanza netto.
- **Pattern:** I pattern candidati restano non operativi: i dati exchange possono solo preparare la conferma.
- **Breakout/breakdown:** Prezzo non abbastanza vicino a un livello chiave o flusso non netto.
- **Mappa liquidità attuale:** muro bid: n/a; muro ask: n/a

![Microstruttura exchange SOL](exchange_microstructure_SOL.png)

### DOGE

- Score grezzo exchange: **+2,00**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 9, accuratezza +44,44%.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 0, bear 2, divergenze 0.
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

![Microstruttura exchange DOGE](exchange_microstructure_DOGE.png)

## Overlay sulle previsioni a 30 giorni

La previsione storica grezza dello scanner resta intatta. L'overlay exchange può correggerla solo dopo almeno 30 controlli maturati a 30 giorni e solo se il modulo dimostra accuratezza direzionale almeno del 55%.

| Asset | Prob. grezza salita | Return p50 grezzo | Controlli 30g | Accuratezza exchange | Stato overlay | Peso | Prob. corretta | Return corretto |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +85,00% | +36,97% | 1 | +0,00% | RACCOLTA DATI | 0,00 | +85,00% | +36,97% |
| SOL | +67,50% | +33,19% | 2 | +100,00% | RACCOLTA DATI | 0,00 | +67,50% | +33,19% |
| DOGE | +25,00% | -14,87% | 4 | +75,00% | RACCOLTA DATI | 0,00 | +25,00% | -14,87% |

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

Generato: 2026-09-13 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [exchange_signal_tracker_report.md](exchange_signal_tracker_report.md)

Questo tracker verifica se il segnale candidato exchange ±1 anticipa correttamente la direzione del prezzo a 1/3/7/14/30 giorni.
Il peso Global resta 0 finché l'orizzonte 7g non ha almeno 30 controlli, accuratezza almeno 55% e return corretto direzione positivo. L'overlay a 30g ha un gate separato.

Controlli maturati completati in questa esecuzione: **15**.

## Ultime fotografie giornaliere

| Data | Asset | Prezzo | Versione | Calibrazione | Candidato | Peso Global | Score raw | Confidenza | Taker 4h | OI 24h | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-09-13 | BTC | 77.195,40 | V2.1.3 | OK | 0 | 0 | 2,25 | MEDIA | 7,57 | +0,69% | +0,52% |
| 2026-09-13 | DOGE | 0.08469 | V2.1.3 | OK | 0 | 0 | 2,00 | BASSA | 2,19 | -2,64% | +2,48% |
| 2026-09-13 | SOL | 101,72 | V2.1.3 | OK | 0 | 0 | 2,00 | BASSA | 1,61 | -1,45% | +10,62% |
| 2026-09-12 | BTC | 77.153,40 | V2.1.3 | OK | 0 | 0 | 2,25 | MEDIA | 1,38 | -7,50% | -2,19% |
| 2026-09-12 | DOGE | 0.08429 | V2.1.3 | OK | 0 | 0 | 2,12 | MEDIA | 4,01 | -4,06% | +1,39% |
| 2026-09-12 | SOL | 101,52 | V2.1.3 | OK | 0 | 0 | 2,00 | BASSA | 2,94 | +0,13% | +11,01% |
| 2026-09-11 | BTC | 77.056,60 | V2.1.3 | OK | 0 | 0 | 2,25 | MEDIA | 2,04 | -0,21% | -2,41% |
| 2026-09-11 | DOGE | 0.08400 | V2.1.3 | OK | 0 | 0 | 2,12 | MEDIA | 1,48 | +0,38% | +4,35% |
| 2026-09-11 | SOL | 99,66 | V2.1.3 | OK | 0 | 0 | 2,50 | BASSA | 2,37 | -3,07% | +8,26% |

## Accuratezza direzionale

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 5 | +40,00% | -0,26% | -0,89% | +0,60% | FEEDBACK RAPIDO |
| BTC | 3g | 5 | +40,00% | +0,25% | -2,11% | +2,12% | FEEDBACK RAPIDO |
| BTC | 7g | 5 | +40,00% | -1,30% | -3,40% | +2,47% | FEEDBACK RAPIDO |
| BTC | 14g | 3 | +33,33% | -0,17% | -3,31% | +4,48% | FEEDBACK RAPIDO |
| BTC | 30g | 1 | +0,00% | -0,24% | -3,45% | +3,82% | FEEDBACK RAPIDO |
| SOL | 1g | 5 | +60,00% | +0,93% | +0,43% | +3,39% | FEEDBACK RAPIDO |
| SOL | 3g | 5 | +60,00% | +2,75% | -3,02% | +7,77% | FEEDBACK RAPIDO |
| SOL | 7g | 5 | +60,00% | +3,63% | -3,62% | +9,63% | FEEDBACK RAPIDO |
| SOL | 14g | 5 | +80,00% | +8,45% | -4,32% | +14,61% | FEEDBACK RAPIDO |
| SOL | 30g | 2 | +100,00% | +22,28% | -5,94% | +27,20% | FEEDBACK RAPIDO |
| DOGE | 1g | 9 | +44,44% | +0,77% | -0,33% | +1,78% | FEEDBACK RAPIDO |
| DOGE | 3g | 9 | +33,33% | +1,22% | -3,22% | +5,78% | FEEDBACK RAPIDO |
| DOGE | 7g | 9 | +44,44% | -1,43% | -4,92% | +7,35% | FEEDBACK RAPIDO |
| DOGE | 14g | 8 | +37,50% | +0,57% | -5,38% | +14,44% | FEEDBACK RAPIDO |
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

**BTC** — BTC: i futures sembrano più vulnerabili verso una discesa improvvisa. Non significa che deve scendere, ma se rompe sotto può accelerare. Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale.

**SOL** — SOL: i futures sembrano più vulnerabili verso una discesa improvvisa. Non significa che deve scendere, ma se rompe sotto può accelerare. Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale.

**DOGE** — DOGE: i futures sembrano più vulnerabili verso una discesa improvvisa. Non significa che deve scendere, ma se rompe sotto può accelerare. Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale.

| Asset | Prezzo | Funding | OI 24h | Long/Short | Lettura futures | Forza |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 77.274 $ | +0.0100% | -5.79% | 1.97 | Rischio sotto | 2/5 |
| SOL | 101,86 $ | +0.0100% | -21.13% | 2.20 | Rischio sotto | 2/5 |
| DOGE | 0.08481 $ | +0.0100% | -7.04% | 5.26 | Rischio sotto | 2/5 |

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

Generato: 2026-09-13 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [rsi_multitimeframe_divergence_report.md](rsi_multitimeframe_divergence_report.md)

Il modulo confronta prezzo e RSI 14 sui pivot confermati **daily e weekly**. Riconosce divergenze regolari e nascoste, segnali in formazione, invalidazioni e semplice conferma del momentum.

**Peso operativo: 0.** Non modifica il Global Confluence, non cambia le soglie del Paper Trading e non apre né blocca operazioni. I risultati vengono misurati prima di qualsiasi futura decisione sul peso.

## Sintesi corrente

| Asset   | Daily                     | Stato D       | Weekly             | Stato W       | Lettura weekly                                                                                                              |   Peso |
|:--------|:--------------------------|:--------------|:-------------------|:--------------|:----------------------------------------------------------------------------------------------------------------------------|-------:|
| BTC     | Hidden bullish invalidata | INVALIDATA    | Conferma rialzista | CONTESTO      | Prezzo e RSI stanno salendo insieme: momentum rialzista confermato.                                                         |      0 |
| SOL     | Hidden bullish            | IN_FORMAZIONE | Hidden bearish     | IN_FORMAZIONE | Hidden bearish in formazione: il secondo estremo non è ancora un pivot confermato. Peso operativo sempre 0.                 |      0 |
| DOGE    | Hidden bullish            | IN_FORMAZIONE | Hidden bearish     | CONFERMATA    | Hidden bearish confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto. |      0 |

## Dettaglio dei pivot

| Asset   | TF   | Tipo                      | Stato         | Prezzo / RSI      | Pivot confrontati                                                   | Δ prezzo contesto   | Δ RSI contesto   |   Peso |
|:--------|:-----|:--------------------------|:--------------|:------------------|:--------------------------------------------------------------------|:--------------------|:-----------------|-------:|
| BTC     | 1D   | Hidden bullish invalidata | INVALIDATA    | 77.275 $ / 55,11  | n/a                                                                 | -1,24%              | -16,53           |      0 |
| BTC     | 1W   | Conferma rialzista        | CONTESTO      | 77.275 $ / 55,14  | n/a                                                                 | +21,73%             | 16,30            |      0 |
| SOL     | 1D   | Hidden bullish            | IN_FORMAZIONE | 101,87 $ / 57,55  | 2026-09-02 97,45 $ / RSI 63,79 → 2026-09-11 98,63 $ / RSI 58,52     | n/a                 | n/a              |      0 |
| SOL     | 1W   | Hidden bearish            | IN_FORMAZIONE | 101,87 $ / 56,90  | 2026-08-30 110,04 $ / RSI 57,95 → 2026-09-06 107,12 $ / RSI 60,25   | n/a                 | n/a              |      0 |
| DOGE    | 1D   | Hidden bullish            | IN_FORMAZIONE | 0.08482 $ / 51,90 | 2026-09-02 0.08028 $ / RSI 52,52 → 2026-09-10 0.08285 $ / RSI 48,72 | n/a                 | n/a              |      0 |
| DOGE    | 1W   | Hidden bearish            | CONFERMATA    | 0.08482 $ / 45,93 | 2026-05-17 0.11825 $ / RSI 44,25 → 2026-08-23 0.09998 $ / RSI 49,72 | n/a                 | n/a              |      0 |

### BTC

- **1D — Hidden bullish invalidata / INVALIDATA**: La precedente hidden bullish non è più sostenuta dalla relazione corrente tra pivot di prezzo e RSI.
- **1W — Conferma rialzista / CONTESTO**: Prezzo e RSI stanno salendo insieme: momentum rialzista confermato.

### SOL

- **1D — Hidden bullish / IN_FORMAZIONE**: Hidden bullish in formazione: il secondo estremo non è ancora un pivot confermato. Peso operativo sempre 0.
- **1W — Hidden bearish / IN_FORMAZIONE**: Hidden bearish in formazione: il secondo estremo non è ancora un pivot confermato. Peso operativo sempre 0.

### DOGE

- **1D — Hidden bullish / IN_FORMAZIONE**: Hidden bullish in formazione: il secondo estremo non è ancora un pivot confermato. Peso operativo sempre 0.
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
| BTC     | 1D   | Hidden bearish   |          60 |           1 | 0,00%         | -23,44%           | RACCOLTA DATI |      0 |
| BTC     | 1W   | Bullish regolare |          30 |           1 | +100,00%      | +1,03%            | RACCOLTA DATI |      0 |
| BTC     | 1W   | Bullish regolare |          60 |           1 | +100,00%      | +22,85%           | RACCOLTA DATI |      0 |
| DOGE    | 1D   | Bullish regolare |          30 |           1 | +100,00%      | +22,35%           | RACCOLTA DATI |      0 |
| DOGE    | 1D   | Hidden bearish   |          30 |           2 | +50,00%       | -8,18%            | RACCOLTA DATI |      0 |
| DOGE    | 1D   | Hidden bearish   |          60 |           1 | 0,00%         | -16,95%           | RACCOLTA DATI |      0 |
| SOL     | 1W   | Hidden bearish   |          30 |           1 | +100,00%      | +1,11%            | RACCOLTA DATI |      0 |
| SOL     | 1W   | Hidden bearish   |          60 |           1 | 0,00%         | -30,59%           | RACCOLTA DATI |      0 |

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

Generato: 2026-09-13 05:32 UTC


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

| Asset   | Prezzo   |   Punteggio | Verdetto                      | Trend       | Momentum        | Struttura                                          |   Pattern score | Fibonacci      | Pattern rialzista                | Pattern ribassista         | Supporto   | Resistenza   |
|:--------|:---------|------------:|:------------------------------|:------------|:----------------|:---------------------------------------------------|----------------:|:---------------|:---------------------------------|:---------------------------|:-----------|:-------------|
| BTC | 77.274 $ | 3 | COSTRUTTIVO MA NON CONFERMATO | Trend misto | Momentum debole | Struttura rialzista con massimi e minimi crescenti | 0 | +1 / TENUTO | Doppio minimo / TARGET RAGGIUNTO | Doppio massimo / CANDIDATO | 76.248 | 82.262 |
| SOL | 101,86 $ | 1 | NEUTRALE / MISTO | Trend misto | Momentum debole | Compressione / triangolo | 0 | 0 / NON ATTIVO | Doppio minimo / TARGET RAGGIUNTO | Doppio massimo / CANDIDATO | 97,45 | 107,12 |
| DOGE | 0.08481 $ | -6 | DEBOLE | Trend misto | Momentum debole | Compressione / triangolo | 0 | 0 / TENUTO | Doppio minimo / TARGET RAGGIUNTO | Doppio massimo / CANDIDATO | 0.08028 | 0.09421 |

## Riepilogo ciclo di vita pattern

| Asset   | Doppio minimo    | Triplo minimo    | Adam/Eve Bottom                        | Doppio massimo   | Triplo massimo   | Adam/Eve Top                 |   Punteggio pattern |
|:--------|:-----------------|:-----------------|:---------------------------------------|:-----------------|:-----------------|:-----------------------------|--------------------:|
| BTC | TARGET RAGGIUNTO | TARGET RAGGIUNTO | Adam and Eve Bottom — TARGET RAGGIUNTO | CANDIDATO | CANDIDATO | ASSENTE | 0 |
| SOL | TARGET RAGGIUNTO | TARGET RAGGIUNTO | Adam and Eve Bottom — TARGET RAGGIUNTO | CANDIDATO | CANDIDATO | Adam and Eve Top — CANDIDATO | 0 |
| DOGE | TARGET RAGGIUNTO | TARGET RAGGIUNTO | Adam and Eve Bottom — TARGET RAGGIUNTO | CANDIDATO | CANDIDATO | Adam and Eve Top — CANDIDATO | 0 |

## Indicatori tecnici

| Asset   |   RSI 14 |   Istogramma MACD | MA20    | MA50    | MA200   | Pendenza MA50 20g   | Pendenza MA200 60g   | Rendimento 30g   | Rendimento 90g   |
|:--------|---------:|------------------:|:--------|:--------|:--------|:--------------------|:---------------------|:-----------------|:-----------------|
| BTC | 55.11 | -760.165 | 78.588 | 70.909 | 70.091 | 8,32% | -4,66% | 22,70% | 16,57% |
| SOL | 57.53 | -1.14544 | 102,44 | 87,43 | 83,04 | 12,47% | -8,81% | 35,22% | 37,69% |
| DOGE | 51.88 | -0.00078 | 0.08615 | 0.07821 | 0.08814 | 6,84% | -12,08% | 21,15% | -3,74% |

## Dettaglio asset

### BTC

- Prezzo: **77.274 $**
- Punteggio tecnico: **3 / 12**
- Verdetto: **COSTRUTTIVO MA NON CONFERMATO**
- Trend: **Trend misto** (1)
- Momentum: **Momentum debole** (-2)
- Volume: **Volume da distribuzione** (-1)
- Struttura: **Struttura rialzista con massimi e minimi crescenti** (2)
  - Dettaglio struttura: Ultimi minimi: 6.249e+04 -> 7.625e+04. Ultimi massimi: 8.135e+04 -> 8.226e+04.
- Divergenza: **Nessuna** (0)
- Fase Wyckoff candidata: **Markup / fase rialzista** (2)
  - Dettaglio Wyckoff: Prezzo sopra MA200, MA50 in salita e trend a 30 giorni positivo.
- Fibonacci automatico: **TENUTO** (+1)
  - Swing UP 2026-07-01 57.748 -> 2026-09-03 82.262; livello più vicino 23.6% a 76.477; stato TENUTO; confluenza: supporto tecnico.
- Punteggio pattern: **0**
  - rialzista dominante: Doppio minimo (TARGET RAGGIUNTO, 0); ribassista dominante: Doppio massimo (CANDIDATO, 0).
- Supporto più vicino: **76.248**
- Resistenza più vicina: **82.262**

Pattern classici e ciclo di vita:

- Doppio minimo: **TARGET RAGGIUNTO** (0)
  - Due minimi simili vicino a 62.227 tra 2026-08-03 e 2026-08-14. Neckline stimata: 65.402. Breakout neckline: 2026-08-19 (25 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 68.577; progresso corrente: 373,91%. Relazione prezzo/neckline: sopra neckline.
  - neckline 65.402; target 68.577; breakout 2026-08-19 (25g); progresso 373,91%; prezzo sopra neckline.
- Triplo minimo: **TARGET RAGGIUNTO** (0)
  - Tre minimi simili vicino a 62.201 dal 2026-06-18 al 2026-08-14. Neckline stimata: 66.910. Breakout neckline: 2026-08-19 (25 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 71.619; progresso corrente: 220,09%. Relazione prezzo/neckline: sopra neckline.
  - neckline 66.910; target 71.619; breakout 2026-08-19 (25g); progresso 220,09%; prezzo sopra neckline.
- Adam and Eve Bottom: **TARGET RAGGIUNTO** (0)
  - Pattern Adam and Eve Bottom vicino a 58.076 dal 2026-06-25 al 2026-08-14. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 66.910. Breakout neckline: 2026-08-19 (25 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 75.744; progresso corrente: 117,31%. Relazione prezzo/neckline: sopra neckline.
  - neckline 66.910; target 75.744; breakout 2026-08-19 (25g); progresso 117,31%; prezzo sopra neckline.
- Doppio massimo: **CANDIDATO** (0)
  - Due massimi simili vicino a 65.508 tra 2026-07-15 e 2026-08-09. Neckline ribassista stimata: 62.227. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 35 giorni.
  - neckline 62.227; target 58.946; distanza dalla neckline 24,18%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 65.544 dal 2026-06-22 al 2026-08-09. Neckline ribassista stimata: 57.748. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 35 giorni.
  - neckline 57.748; target 49.952; distanza dalla neckline 33,81%; prezzo sopra neckline.
- Adam/Eve Top: **ASSENTE** (0)

### SOL

- Prezzo: **101,86 $**
- Punteggio tecnico: **1 / 12**
- Verdetto: **NEUTRALE / MISTO**
- Trend: **Trend misto** (1)
- Momentum: **Momentum debole** (-2)
- Volume: **Volume neutrale** (0)
- Struttura: **Compressione / triangolo** (0)
  - Dettaglio struttura: Ultimi minimi: 74.2 -> 97.45. Ultimi massimi: 110 -> 107.1.
- Divergenza: **Nessuna** (0)
- Fase Wyckoff candidata: **Markup / fase rialzista** (2)
  - Dettaglio Wyckoff: Prezzo sopra MA200, MA50 in salita e trend a 30 giorni positivo.
- Fibonacci automatico: **NON ATTIVO** (0)
  - Swing UP 2026-06-06 60,41 -> 2026-09-06 107,12; livello più vicino 23.6% a 96,09; stato NON ATTIVO; confluenza: supporto tecnico, neckline ribassista.
- Punteggio pattern: **0**
  - rialzista dominante: Doppio minimo (TARGET RAGGIUNTO, 0); ribassista dominante: Doppio massimo (CANDIDATO, 0).
- Supporto più vicino: **97,45**
- Resistenza più vicina: **107,12**

Pattern classici e ciclo di vita:

- Doppio minimo: **TARGET RAGGIUNTO** (0)
  - Due minimi simili vicino a 73,40 tra 2026-07-17 e 2026-08-16. Neckline stimata: 78,73. Breakout neckline: 2026-08-19 (25 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 84,05; progresso corrente: 434,50%. Relazione prezzo/neckline: sopra neckline.
  - neckline 78,73; target 84,05; breakout 2026-08-19 (25g); progresso 434,50%; prezzo sopra neckline.
- Triplo minimo: **TARGET RAGGIUNTO** (0)
  - Tre minimi simili vicino a 70,69 dal 2026-07-17 al 2026-08-16. Neckline stimata: 78,73. Breakout neckline: 2026-08-19 (25 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 86,76; progresso corrente: 288,03%. Relazione prezzo/neckline: sopra neckline.
  - neckline 78,73; target 86,76; breakout 2026-08-19 (25g); progresso 288,03%; prezzo sopra neckline.
- Adam and Eve Bottom: **TARGET RAGGIUNTO** (0)
  - Pattern Adam and Eve Bottom vicino a 67,92 dal 2026-06-19 al 2026-08-01. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 83,81. Breakout neckline: 2026-08-19 (25 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 99,70; progresso corrente: 113,60%. Relazione prezzo/neckline: sopra neckline.
  - neckline 83,81; target 99,70; breakout 2026-08-19 (25g); progresso 113,60%; prezzo sopra neckline.
- Doppio massimo: **CANDIDATO** (0)
  - Due massimi simili vicino a 110,04 tra 2026-08-27 e 2026-09-06. Neckline ribassista stimata: 97,45. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 7 giorni.
  - neckline 97,45; target 84,86; distanza dalla neckline 4,52%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 78,88 dal 2026-07-15 al 2026-08-09. Neckline ribassista stimata: 70,69. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 35 giorni.
  - neckline 70,69; target 62,51; distanza dalla neckline 44,09%; prezzo sopra neckline.
- Adam and Eve Top: **CANDIDATO** (0)
  - Pattern Adam and Eve Top vicino a 83,81 dal 2026-07-04 al 2026-08-09. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 70,69. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 35 giorni.
  - neckline 70,69; target 57,58; distanza dalla neckline 44,09%; prezzo sopra neckline.

### DOGE

- Prezzo: **0.08481 $**
- Punteggio tecnico: **-6 / 12**
- Verdetto: **DEBOLE**
- Trend: **Trend misto** (-1)
- Momentum: **Momentum debole** (-3)
- Volume: **Volume da distribuzione** (-2)
- Struttura: **Compressione / triangolo** (0)
  - Dettaglio struttura: Ultimi minimi: 0.06895 -> 0.08028. Ultimi massimi: 0.09998 -> 0.09421.
- Divergenza: **Nessuna** (0)
- Fase Wyckoff candidata: **Range / fase non chiara** (0)
  - Dettaglio Wyckoff: Posizione nel range a 120 giorni: 37,10%. Fase non abbastanza chiara.
- Fibonacci automatico: **TENUTO** (0)
  - Swing UP 2026-08-01 0.06797 -> 2026-09-05 0.09421; livello più vicino 38.2% a 0.08419; stato TENUTO; confluenza: nessuna confluenza indipendente.
- Punteggio pattern: **0**
  - rialzista dominante: Doppio minimo (TARGET RAGGIUNTO, 0); ribassista dominante: Doppio massimo (CANDIDATO, 0).
- Supporto più vicino: **0.08028**
- Resistenza più vicina: **0.09421**

Pattern classici e ciclo di vita:

- Doppio minimo: **TARGET RAGGIUNTO** (0)
  - Due minimi simili vicino a 0.06829 tra 2026-07-24 e 2026-08-12. Neckline stimata: 0.07380. Breakout neckline: 2026-08-19 (25 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 0.07931; progresso corrente: 199,71%. Relazione prezzo/neckline: sopra neckline.
  - neckline 0.07380; target 0.07931; breakout 2026-08-19 (25g); progresso 199,71%; prezzo sopra neckline.
- Triplo minimo: **TARGET RAGGIUNTO** (0)
  - Tre minimi simili vicino a 0.06895 dal 2026-07-08 al 2026-08-12. Neckline stimata: 0.07380. Breakout neckline: 2026-08-19 (25 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 0.07866; progresso corrente: 226,79%. Relazione prezzo/neckline: sopra neckline.
  - neckline 0.07380; target 0.07866; breakout 2026-08-19 (25g); progresso 226,79%; prezzo sopra neckline.
- Adam and Eve Bottom: **TARGET RAGGIUNTO** (0)
  - Pattern Adam and Eve Bottom vicino a 0.06829 dal 2026-07-24 al 2026-08-06. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 0.07380. Breakout neckline: 2026-08-19 (25 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 0.07931; progresso corrente: 199,71%. Relazione prezzo/neckline: sopra neckline.
  - neckline 0.07380; target 0.07931; breakout 2026-08-19 (25g); progresso 199,71%; prezzo sopra neckline.
- Doppio massimo: **CANDIDATO** (0)
  - Due massimi simili vicino a 0.07380 tra 2026-07-26 e 2026-08-11. Neckline ribassista stimata: 0.06797. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 33 giorni.
  - neckline 0.06797; target 0.06214; distanza dalla neckline 24,77%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 0.07923 dal 2026-07-04 al 2026-08-11. Neckline ribassista stimata: 0.06797. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 33 giorni.
  - neckline 0.06797; target 0.05671; distanza dalla neckline 24,77%; prezzo sopra neckline.
- Adam and Eve Top: **CANDIDATO** (0)
  - Pattern Adam and Eve Top vicino a 0.07923 dal 2026-07-04 al 2026-08-11. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 0.06797. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 33 giorni.
  - neckline 0.06797; target 0.05671; distanza dalla neckline 24,77%; prezzo sopra neckline.

## Fibonacci automatico

Il modulo seleziona uno swing recente tramite pivot confermati. Un semplice tocco vale 0: Fibonacci pesa al massimo ±1 soltanto quando il livello è tenuto, perso, recuperato o respinto e coincide con almeno un livello tecnico indipendente.

| Asset   | Swing                       | 23,6%   | 38,2%   | 50,0%   | 61,8%   | 78,6%   | Livello vicino   | Stato      | Confluenza                            |   Score |
|:--------|:----------------------------|:--------|:--------|:--------|:--------|:--------|:-----------------|:-----------|:--------------------------------------|--------:|
| BTC | UP 2026-07-01 -> 2026-09-03 | 76.477 | 72.898 | 70.005 | 67.112 | 62.994 | 23.6% / 76.477 | TENUTO | supporto tecnico | +1 |
| SOL | UP 2026-06-06 -> 2026-09-06 | 96,09 | 89,28 | 83,77 | 78,25 | 70,41 | 23.6% / 96,09 | NON ATTIVO | supporto tecnico, neckline ribassista | 0 |
| DOGE | UP 2026-08-01 -> 2026-09-05 | 0.08802 | 0.08419 | 0.08109 | 0.07800 | 0.07359 | 38.2% / 0.08419 | TENUTO | nessuna confluenza indipendente | 0 |

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

- **BTC**: 30/30 previsioni controllate su 71 fatte. Stato: **ATTIVA**.
- **SOL**: 30/30 previsioni controllate su 71 fatte. Stato: **ATTIVA**.
- **DOGE**: 30/30 previsioni controllate su 71 fatte. Stato: **ATTIVA**.

| Asset | Previsioni fatte | Controllate | Progresso | In attesa | Stato | Prossimo controllo |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 71 | 30 | 30/30 [██████████] | 41 | ATTIVA | 2026-09-14 / tra 1 giorno |
| SOL | 71 | 30 | 30/30 [██████████] | 41 | ATTIVA | 2026-09-14 / tra 1 giorno |
| DOGE | 71 | 30 | 30/30 [██████████] | 41 | ATTIVA | 2026-09-14 / tra 1 giorno |

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

Generato: 2026-09-13 05:33 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [data_quality_coherence_report.md](data_quality_coherence_report.md)

Questo controllo non modifica punteggi o decisioni. Verifica che tutti i moduli usino lo stesso prezzo corrente e che le nuove regole Technical/Classic Visual siano integre.

## Stato finale: **OK**

## Prezzo unico per modulo

| Modulo                  | Asset   | Campo             | Stato   | Prezzo snapshot   | Prezzo modulo   | Differenza   |
|:------------------------|:--------|:------------------|:--------|:------------------|:----------------|:-------------|
| Scanner                 | BTC     | current_price     | OK      | 77.274 $          | 77.274 $        | +0,0000%     |
| Scanner                 | DOGE    | current_price     | OK      | 0.08481 $         | 0.08481 $       | -0,0000%     |
| Scanner                 | SOL     | current_price     | OK      | 101,86 $          | 101,86 $        | +0,0000%     |
| Scanner Forecast        | BTC     | current_price     | OK      | 77.274 $          | 77.274 $        | +0,0000%     |
| Scanner Forecast        | SOL     | current_price     | OK      | 101,86 $          | 101,86 $        | +0,0000%     |
| Scanner Forecast        | DOGE    | current_price     | OK      | 0.08481 $         | 0.08481 $       | -0,0000%     |
| Technical Structure     | BTC     | price             | OK      | 77.274 $          | 77.274 $        | +0,0000%     |
| Technical Structure     | SOL     | price             | OK      | 101,86 $          | 101,86 $        | +0,0000%     |
| Technical Structure     | DOGE    | price             | OK      | 0.08481 $         | 0.08481 $       | -0,0000%     |
| Classic Technical       | BTC     | price             | OK      | 77.274 $          | 77.274 $        | +0,0000%     |
| Classic Technical       | SOL     | price             | OK      | 101,86 $          | 101,86 $        | +0,0000%     |
| Classic Technical       | DOGE    | price             | OK      | 0.08481 $         | 0.08481 $       | -0,0000%     |
| Classic Visual          | BTC     | price             | OK      | 77.274 $          | 77.274 $        | +0,0000%     |
| Classic Visual          | SOL     | price             | OK      | 101,86 $          | 101,86 $        | +0,0000%     |
| Classic Visual          | DOGE    | price             | OK      | 0.08481 $         | 0.08481 $       | -0,0000%     |
| Exchange Microstructure | BTC     | price             | OK      | 77.274 $          | 77.195 $        | -0,1015%     |
| Exchange Microstructure | SOL     | price             | OK      | 101,86 $          | 101,72 $        | -0,1384%     |
| Exchange Microstructure | DOGE    | price             | OK      | 0.08481 $         | 0.08469 $       | -0,1415%     |
| RSI top-cycle           | SOL     | current_price     | OK      | 101,86 $          | 101,86 $        | +0,0000%     |
| RSI top-cycle           | SOL     | current_price     | OK      | 101,86 $          | 101,86 $        | +0,0000%     |
| Frattale BTC/SOL        | SOL     | sol_current_price | OK      | 101,86 $          | 101,86 $        | +0,0000%     |
| Fractal path            | SOL     | current_price     | OK      | 101,86 $          | 101,86 $        | +0,0000%     |

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
