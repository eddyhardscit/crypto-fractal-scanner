<!-- COMPACT_REPORT_HEADER_START -->
> **Vista compatta:** Decisione operativa, Global Confluence e cambiamenti giornalieri restano aperti. Tocca il titolo di una sezione per mostrare o nascondere i dettagli.  
> Tutte le tabelle e tutti i dati restano nel file: copiando il Markdown raw viene copiato tutto.
<!-- COMPACT_REPORT_HEADER_END -->

<!-- COMPACT_SECTION_START:decision -->
<details open>
<summary><strong>🧭 Decisione operativa — da leggere per prima</strong></summary>

<!-- DECISION_REPORT_START -->

# Decisione operativa sintetica

Generato: 2026-08-27 05:33 UTC

Report separato completo: [decision_report.md](decision_report.md)

Sintesi automatica dello scanner: l'azione spot viene copiata direttamente dal Global Confluence; long, short e rischio restano filtri separati e più prudenti.

| Asset | Global | Direzione | Spot | Long leva | Short leva | Max long | Max short | Rischio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +7 | BULLISH | ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA | LONG PRUDENTE | NO SHORT | max 2x isolated | nessuna | MEDIO |
| SOL | +7 | BULLISH | HOLD / ACCUMULO A TRANCHE, NO LEVA AGGRESSIVA | NO LONG A LEVA | NO SHORT | nessuna | nessuna | MOLTO ALTO |
| DOGE | -1 | LEGGERMENTE BEARISH | EVITA LONG / SOLO RIMBALZI VELOCI | NO LONG A LEVA | SHORT SOLO DOPO SPIKE | nessuna | max 1x-2x isolated | MOLTO ALTO |

## Lettura immediata

- **BTC**: Global = **+7**, spot = **ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA**, long = **LONG PRUDENTE**, short = **NO SHORT**, rischio = **MEDIO**.
- **SOL**: Global = **+7**, spot = **HOLD / ACCUMULO A TRANCHE, NO LEVA AGGRESSIVA**, long = **NO LONG A LEVA**, short = **NO SHORT**, rischio = **MOLTO ALTO**.
- **DOGE**: Global = **-1**, spot = **EVITA LONG / SOLO RIMBALZI VELOCI**, long = **NO LONG A LEVA**, short = **SHORT SOLO DOPO SPIKE**, rischio = **MOLTO ALTO**.

## Dettaglio logica

### BTC

- Global Confluence: **+7**
- Confluenza: **POSITIVA FORTE**
- Bias Global: **Rialzista**
- Direzione decisionale: **BULLISH**
- Azione spot dal Global: **ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA**
- Long leva: **LONG PRUDENTE**
- Short leva: **NO SHORT**
- Rischio: **MEDIO**
- Conferme: Prima resistenza sopra 82.792; conferma del doppio minimo sopra 66.910.
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
- Conferme: Doppio minimo target raggiunto finché mantiene 78,73; nuova conferma tecnica sopra 127,97; milestone analogiche 114,65 / 139,61, valide soltanto se rientra anche il gap frattale.
- Invalidazioni: Allarmi sotto 93,22 / 74,20 / 62,19.

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
- **Lifecycle EMA200** = per SOL resta solo contesto, peso Global 0; score interno 2; EMA200 circa 111,33 $; upside verso EMA200 +15,25%. Non autorizza leva e non aggiunge punti automatici.
- **NO LONG** non significa automaticamente **SHORT**. Lo short ha senso solo se il quadro è bearish o se lo spike viene spesso scaricato.
- Per SOL, se il Global è da **+3 in su**, la decisione non deve diventare bearish solo perché lo scanner grezzo a 30 giorni è incerto.

<!-- DECISION_REPORT_END -->

<!-- PAPER_TRADING_START -->
# Paper trading automatico KuCoin

Generato: 2026-08-27T05:33:24+00:00


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [paper_trading_report.md](paper_trading_report.md)

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-08-27T05:05:29+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-08-27T05:05:29+00:00 | 2026-08-27T05:05:29+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-08-27T04:45:00+00:00 | 2026-08-27T04:45:00+00:00 | 5,6 min | 25,0 min | OK |
| 60m | 12 | 2026-08-27T04:00:00+00:00 | 2026-08-27T04:00:00+00:00 | 5,6 min | 45,0 min | OK |
| 240m | 12 | 2026-08-27T00:00:00+00:00 | 2026-08-27T00:00:00+00:00 | 1,09 h | 1,00 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1H Fast Nohigh Cap75 Short Only V1 | BTR | 60m | LONG | 5,75 | 4,50 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Master Adaptive Gb20 Partial V1 | BTR | 60m | LONG | 5,75 | 0,00 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Master Adaptive Gb20 Be V1 | BTR | 60m | LONG | 5,75 | 0,00 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Master Adaptive Runner25 V1 | SKHYNIX | 60m | LONG | 5,20 | 0,00 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Master Adaptive Gb20 V1 | BTR | 60m | LONG | 5,75 | 0,00 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Master Adaptive No Alt V1 | SKHYNIX | 60m | LONG | 5,20 | 0,00 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Master Adaptive V1 | BTR | 60m | LONG | 5,75 | 0,00 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Principale 4H | ENA | 240m | LONG | 4,25 | 6,00 | 1,75 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | HYPE | 240m | LONG | 4,14 | 6,00 | 1,86 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | SKHYNIX | 240m | LONG | 3,54 | 6,00 | 2,46 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | BTC | 240m | LONG | 3,25 | 6,00 | 2,75 | STALE_CANDLE | 1,09 h | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | SUI | 240m | SHORT | -2,75 | 6,00 | 3,25 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | ZEC | 240m | LONG | 2,72 | 6,00 | 3,28 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | PEPE | 240m | LONG | 1,02 | 6,00 | 4,98 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | XRP | 240m | LONG | 0,89 | 6,00 | 5,11 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | DOGE | 240m | SHORT | -0,80 | 6,00 | 5,20 | STALE_CANDLE | 1,09 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| 1H Balanced Long No Rhv V1 | BTR | 60m | LONG | 5,75 | 5,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Fast Nohigh Cap75 V1 | BTR | 60m | LONG | 5,75 | 4,50 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Long Btc 1 3 Cap75 V1 | BTR | 60m | LONG | 5,75 | 4,50 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast No Pepe V1 | BTR | 60m | LONG | 5,75 | 4,50 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Tp2 V1 | BTR | 60m | LONG | 5,75 | 4,50 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Benchmark trend following EMA 1H | BTR | 60m | LONG | 5,75 | 5,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Scanner Top 5 Long 1H | BTR | 60m | LONG | 5,75 | 5,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Scanner Top10 Long | BTR | 60m | LONG | 5,75 | 5,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Scanner Top15 Long | BTR | 60m | LONG | 5,75 | 5,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Scanner Top20 Long | BTR | 60m | LONG | 5,75 | 5,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Scanner Top 5 + forza BTC 1H | BTR | 60m | LONG | 5,75 | 5,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.807,62 | -1,92% | €59,28 | €3.000,00 | 1,98% | 6 | 52 | 38,46% | 0,87 | 6,86% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 52 | 2289 | PRIME INDICAZIONI | 100 (mancano 48) |

- Trade del Principale 4H chiusi: **52**; win rate **38,46%**; profit factor **0,87**.
- Expectancy: **€-3,67** per trade; P&L netto: **€-190,76**; max drawdown: **6,86%**.
- Valutazione: **Si può osservare la direzione, ma il risultato resta fragile.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 6 | €9.807,62 | €699,00 | €2.096,99 | €196,05 | €-0,51 |
| TEST | Benchmark Donchian breakout 1H | 6 | €11.290,01 | €2.894,15 | €5.788,31 | €221,61 | €66,62 |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | 6 | €11.087,05 | €2.865,79 | €8.597,37 | €175,88 | €-18,15 |
| TEST | Combo Trend Side Regime Guard V1 | 5 | €11.059,81 | €3.827,11 | €7.654,22 | €167,60 | €-7,47 |
| TEST | Donchian 1H Gb20 120R V1 | 6 | €11.024,19 | €2.826,01 | €5.652,03 | €216,39 | €65,05 |
| TEST | Scanner Top 5 Long 1H | 5 | €10.847,57 | €3.462,60 | €6.925,20 | €216,98 | €-11,21 |
| TEST | Main Side Regime Guard V1 | 6 | €10.821,50 | €672,38 | €2.017,15 | €163,22 | €78,33 |
| TEST | 1H Fast No Pepe V1 | 9 | €10.599,14 | €2.055,48 | €6.166,45 | €211,40 | €-35,68 |
| TEST | Combo Adaptive | 7 | €10.561,80 | €3.499,76 | €6.999,53 | €212,39 | €-54,27 |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | 5 | €10.409,37 | €2.325,05 | €6.975,16 | €208,88 | €-32,33 |
| TEST | Rapida 1H V3 Filtered | 5 | €10.342,49 | €2.310,11 | €6.930,34 | €207,54 | €-32,12 |
| TEST | Combo Adaptive Side Regime Guard V1 | 5 | €10.342,22 | €2.490,20 | €4.980,39 | €155,69 | €-50,25 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 0 | €10.300,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Ampia 4H | 7 | €10.276,43 | €1.057,57 | €2.115,14 | €205,57 | €-2,91 |
| TEST | Combo Adaptive Long Only V1 | 5 | €10.274,96 | €4.512,56 | €9.025,12 | €206,73 | €-28,89 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 0 | €10.271,73 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Nohigh Cap75 V1 | 8 | €10.252,80 | €1.968,40 | €5.905,21 | €204,38 | €-34,46 |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | 4 | €10.250,92 | €2.678,99 | €8.036,96 | €151,87 | €-12,64 |
| TEST | 1H Fast V3 Nohigh Range Only V1 | 0 | €10.247,95 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 0 | €10.239,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 0 | €10.235,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 4H | 1 | €10.213,16 | €367,30 | €734,59 | €50,97 | €19,64 |
| TEST | Btc Bollinger 1H | 0 | €10.209,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Donchian 1H | 1 | €10.209,11 | €828,76 | €2.486,27 | €0,00 | €17,98 |
| TEST | Sol Donchian 4H | 0 | €10.196,46 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Tp2 V1 | 6 | €10.195,40 | €1.795,80 | €5.387,40 | €154,19 | €-31,25 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 0 | €10.185,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Main Dynamic Asset Selector V1 | 0 | €10.161,45 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Score 6 75 Range Only V1 | 0 | €10.149,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 0 | €10.145,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | 2 | €10.124,13 | €2.312,44 | €6.937,33 | €47,99 | €-11,27 |
| TEST | Rapida 1H V2 | 2 | €10.110,49 | €2.386,94 | €7.160,82 | €50,64 | €-13,04 |
| TEST | Sol Ema 1H | 1 | €10.099,15 | €728,87 | €2.186,61 | €50,42 | €15,82 |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 0 | €10.099,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 4H | 1 | €10.076,72 | €395,27 | €790,53 | €50,28 | €21,13 |
| TEST | Scanner Top 5 + forza BTC 1H | 5 | €10.073,02 | €3.227,27 | €6.454,55 | €202,28 | €-10,57 |
| TEST | Btc Bollinger 4H | 1 | €10.061,24 | €775,58 | €1.551,16 | €50,15 | €32,35 |
| TEST | Combo Adaptive Partial 1R V1 | 7 | €10.049,82 | €2.013,69 | €4.027,37 | €150,19 | €-26,06 |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 0 | €10.048,77 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €10.045,08 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V1 | 0 | €10.043,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 4H | 1 | €10.041,52 | €648,94 | €1.297,88 | €50,35 | €-27,57 |
| TEST | 1H Balanced Short Trend Down Strict V1 | 0 | €10.035,46 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · prudente · 5x | 0 | €10.028,67 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €50 · 15x | 0 | €10.017,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top10 Long | 4 | €10.014,31 | €4.430,46 | €8.860,92 | €201,18 | €-35,39 |
| TEST | Scalp RSI Short 80 · €50 · 15x | 0 | €10.009,36 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 0 | €10.009,02 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 0 | €10.008,92 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €10 · 15x | 0 | €10.003,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 0 | €10.003,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Tp3 V1 | 4 | €10.001,89 | €3.960,24 | €7.920,49 | €201,25 | €-28,69 |
| TEST | Scalp RSI Short 80 · €10 · 15x | 0 | €10.001,87 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Continuation V1 | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €10 · 15x | 0 | €9.999,33 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | 8 | €9.997,66 | €1.919,42 | €5.758,26 | €199,29 | €-33,60 |
| TEST | Scalp RSI Long 15 · €10 · 15x | 0 | €9.997,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €50 · 15x | 0 | €9.996,64 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Runner25 V1 | 4 | €9.996,04 | €3.957,93 | €7.915,85 | €201,13 | €-28,67 |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 0 | €9.995,23 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Bollinger 1H | 0 | €9.992,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · prudente · 5x | 0 | €9.991,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €10 · 15x | 0 | €9.990,45 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Ema 1H | 0 | €9.988,85 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 4H | 1 | €9.988,30 | €704,37 | €1.408,74 | €50,10 | €-29,93 |
| TEST | Scalp RSI Long 15 · €50 · 15x | 0 | €9.988,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 0 | €9.987,48 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · prudente · 5x | 0 | €9.980,94 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 4H | 1 | €9.974,11 | €435,50 | €871,00 | €49,91 | €-7,12 |
| TEST | Bilanciata 1H V3 Filtered | 6 | €9.973,34 | €1.587,80 | €4.763,39 | €200,34 | €-1,98 |
| TEST | Btc Adaptive 1H | 0 | €9.968,58 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 1H | 0 | €9.957,15 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 1H | 1 | €9.955,52 | €718,50 | €2.155,51 | €49,71 | €15,59 |
| TEST | Scalp RSI Long 25 · €50 · 15x | 0 | €9.952,25 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Ema 4H | 1 | €9.948,10 | €487,73 | €975,47 | €49,56 | €37,97 |
| TEST | Scalp RSI Short 80 · prudente · 5x | 0 | €9.940,42 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.939,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 4H | 1 | €9.934,86 | €700,60 | €1.401,20 | €49,83 | €-29,77 |
| TEST | Doge Donchian 1H | 0 | €9.924,84 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | 0 | €9.912,24 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | 5 | €9.869,22 | €3.124,54 | €9.373,63 | €197,39 | €-97,43 |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 0 | €9.837,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 1H | 1 | €9.835,77 | €797,97 | €2.393,90 | €49,11 | €16,01 |
| TEST | Btc Ema 1H | 0 | €9.833,66 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 No Esports Long Only V1 | 4 | €9.824,53 | €2.388,05 | €7.164,14 | €147,25 | €-50,27 |
| TEST | Combo Adaptive Regime V1 | 4 | €9.824,32 | €3.823,27 | €7.646,53 | €147,25 | €-4,33 |
| TEST | Eth Adaptive 1H | 1 | €9.817,39 | €1.094,40 | €3.283,20 | €49,22 | €-25,27 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 0 | €9.817,34 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Ema 1H | 1 | €9.798,25 | €1.072,00 | €3.216,01 | €49,07 | €-13,40 |
| TEST | Combo Adaptive Quality7 Regime V1 | 0 | €9.787,56 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 0 | €9.762,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Forza relativa 1H V2 | 4 | €9.739,55 | €2.188,10 | €4.376,21 | €97,76 | €5,01 |
| TEST | Combo Adaptive Quality7 V1 | 3 | €9.738,12 | €1.894,84 | €3.789,69 | €145,51 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 0 | €9.723,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Bollinger 1H | 0 | €9.703,71 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top15 Long | 6 | €9.685,66 | €3.793,14 | €7.586,29 | €194,49 | €-30,23 |
| TEST | Scanner Top20 Long | 6 | €9.685,66 | €3.793,14 | €7.586,29 | €194,49 | €-30,23 |
| TEST | Global Confluence puro 1H | 0 | €9.679,31 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Scanner | 5 | €9.677,88 | €3.099,48 | €6.198,96 | €194,35 | €-10,17 |
| TEST | Eth Donchian 1H | 1 | €9.647,94 | €1.210,37 | €3.631,11 | €48,39 | €-27,95 |
| TEST | 1H Fast V3 No Esports V1 | 5 | €9.629,18 | €1.800,27 | €5.400,81 | €193,25 | €-30,95 |
| TEST | 1H Balanced Long No Rhv V1 | 5 | €9.622,82 | €2.080,20 | €6.240,60 | €193,38 | €14,69 |
| TEST | 1H Fast V3 Nohigh V1 | 5 | €9.612,09 | €2.504,83 | €7.514,48 | €192,45 | €-49,56 |
| TEST | Scanner Top5 Btc Guard V1 | 4 | €9.604,38 | €1.449,43 | €2.898,86 | €97,98 | €64,91 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 0 | €9.579,83 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | 2 | €9.548,64 | €2.181,72 | €6.545,17 | €94,94 | €-48,86 |
| TEST | Master Adaptive Runner25 V1 | 6 | €9.472,98 | €3.655,55 | €7.311,11 | €189,46 | €152,60 |
| TEST | Bilanciata 1H V2 | 3 | €9.460,20 | €2.163,09 | €6.489,26 | €140,73 | €32,50 |
| TEST | 1H Fast V3 Long Only V1 | 5 | €9.458,74 | €2.846,04 | €8.538,13 | €190,06 | €-48,29 |
| TEST | Scanner Top5 Btc Mfe V1 | 5 | €9.442,96 | €3.025,41 | €6.050,82 | €189,63 | €-9,91 |
| TEST | Master Adaptive Gb20 Be V1 | 5 | €9.434,99 | €3.567,70 | €7.135,40 | €188,41 | €-13,11 |
| TEST | 1H Balanced V3 Long Only V1 | 6 | €9.433,84 | €1.505,55 | €4.516,64 | €189,51 | €-2,50 |
| TEST | Master Adaptive No Alt V1 | 5 | €9.426,72 | €3.594,72 | €7.189,44 | €188,54 | €39,26 |
| TEST | Master Adaptive Gb20 Partial V1 | 5 | €9.424,96 | €3.563,91 | €7.127,82 | €188,21 | €-13,10 |
| TEST | 1H Fast Score 6 75 V1 | 0 | €9.415,87 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive V1 | 5 | €9.388,50 | €3.550,12 | €7.100,25 | €187,48 | €-13,05 |
| TEST | Scanner Top5 Btc Guard Mfe V1 | 4 | €9.381,02 | €1.415,72 | €2.831,44 | €95,70 | €63,40 |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | 2 | €9.370,06 | €2.147,45 | €6.442,35 | €93,39 | €-48,09 |
| TEST | Master Adaptive Expanded V1 | 5 | €9.357,25 | €3.581,77 | €7.163,54 | €187,75 | €-28,86 |
| TEST | Combo Trend | 5 | €9.331,16 | €2.556,81 | €5.113,62 | €140,82 | €-37,73 |
| TEST | Scanner Bottom10 Short | 4 | €9.320,74 | €1.261,36 | €2.522,73 | €140,86 | €0,00 |
| TEST | Scanner Bottom15 Short | 4 | €9.320,74 | €1.261,36 | €2.522,73 | €140,86 | €0,00 |
| TEST | Scanner Bottom20 Short | 4 | €9.320,74 | €1.261,36 | €2.522,73 | €140,86 | €0,00 |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | 4 | €9.320,05 | €3.676,85 | €7.353,70 | €139,88 | €21,49 |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | 3 | €9.304,57 | €1.213,15 | €2.426,29 | €49,07 | €62,88 |
| TEST | Master Adaptive Gb20 V1 | 5 | €9.263,76 | €3.502,95 | €7.005,91 | €184,99 | €-12,88 |
| TEST | Master Adaptive Gb20 Loss Cap V1 | 4 | €9.261,89 | €3.376,65 | €6.753,29 | €137,95 | €-24,57 |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | 4 | €9.256,15 | €1.252,64 | €2.505,29 | €139,88 | €0,00 |
| TEST | Benchmark trend following EMA 1H | 5 | €9.255,55 | €1.267,77 | €2.535,55 | €140,48 | €-1,37 |
| TEST | Scanner Bottom5 Short Profit Lock V1 | 4 | €9.242,07 | €1.250,74 | €2.501,48 | €139,67 | €0,00 |
| TEST | Scanner Bottom 5 Short 1H | 4 | €9.170,95 | €1.241,11 | €2.482,23 | €138,60 | €0,00 |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | 0 | €9.165,52 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H V1 | 0 | €9.150,69 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | 2 | €9.142,42 | €1.179,53 | €2.359,05 | €45,66 | €61,79 |
| TEST | 1H Fast V3 Cap75 V1 | 0 | €9.106,22 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Mfe Trail | 6 | €9.072,48 | €2.850,43 | €5.700,85 | €182,13 | €-24,35 |
| TEST | Combo Mean Reversion | 0 | €8.967,07 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Runner25 V1 | 0 | €8.964,11 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Strict3 V1 | 2 | €8.881,45 | €2.396,63 | €4.793,26 | €89,27 | €-26,92 |
| TEST | Scanner Top5 Btc Btc Le3 V1 | 4 | €8.864,81 | €3.497,25 | €6.994,50 | €133,05 | €20,44 |
| TEST | Combo Adaptive Tp3 V1 | 0 | €8.796,64 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Benchmark Bollinger mean reversion 1H | 0 | €8.740,52 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Forza relativa 1H V1 | 0 | €8.445,51 | €0,00 | €0,00 | €0,00 | €0,00 |

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
| PRINCIPALE | Principale 4H | Confluenza trend | €9.807,62 | €-190,76 | 52 | 52 | 38,46% | 0,87 | €-3,67 | 6,86% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €11.290,01 | €1.225,61 | 105 | 105 | 47,62% | 1,51 | €11,67 | 5,85% |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | Momentum / breakout | €11.087,05 | €1.110,49 | 145 | 145 | 53,10% | 1,39 | €7,66 | 5,23% |
| TEST | Combo Trend Side Regime Guard V1 | Combo Trend | €11.059,81 | €1.071,48 | 111 | 111 | 54,05% | 1,53 | €9,65 | 6,20% |
| TEST | Donchian 1H Gb20 120R V1 | Donchian breakout 20 barre | €11.024,19 | €961,32 | 73 | 73 | 46,58% | 1,64 | €13,17 | 5,85% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.847,57 | €862,97 | 139 | 139 | 47,48% | 1,32 | €6,21 | 8,85% |
| TEST | Main Side Regime Guard V1 | Confluenza trend | €10.821,50 | €744,99 | 35 | 35 | 54,29% | 2,09 | €21,29 | 3,82% |
| TEST | 1H Fast No Pepe V1 | Momentum / breakout | €10.599,14 | €638,62 | 211 | 211 | 47,39% | 1,16 | €3,03 | 7,45% |
| TEST | Combo Adaptive | Combo Adaptive | €10.561,80 | €621,13 | 147 | 147 | 46,26% | 1,25 | €4,23 | 7,91% |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | Momentum / breakout V3 Filtered | €10.409,37 | €446,00 | 190 | 190 | 50,00% | 1,14 | €2,35 | 9,50% |
| TEST | Rapida 1H V3 Filtered | Momentum / breakout V3 Filtered | €10.342,49 | €378,89 | 234 | 234 | 44,44% | 1,09 | €1,62 | 9,48% |
| TEST | Combo Adaptive Side Regime Guard V1 | Combo Adaptive | €10.342,22 | €396,27 | 115 | 115 | 47,83% | 1,17 | €3,45 | 8,68% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | Momentum / breakout V3 Filtered | €10.300,05 | €300,05 | 33 | 33 | 48,48% | 2,04 | €9,09 | 2,01% |
| TEST | Ampia 4H | Confluenza trend | €10.276,43 | €280,43 | 52 | 52 | 34,62% | 1,24 | €5,39 | 4,45% |
| TEST | Combo Adaptive Long Only V1 | Combo Adaptive | €10.274,96 | €309,26 | 120 | 120 | 46,67% | 1,12 | €2,58 | 7,78% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | Momentum / breakout V3 Filtered | €10.271,73 | €271,73 | 22 | 22 | 50,00% | 1,74 | €12,35 | 1,72% |
| TEST | 1H Fast Nohigh Cap75 V1 | Momentum / breakout | €10.252,80 | €290,80 | 136 | 136 | 44,85% | 1,10 | €2,14 | 7,10% |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | Momentum / breakout V3 Filtered | €10.250,92 | €268,39 | 72 | 72 | 48,61% | 1,18 | €3,73 | 5,24% |
| TEST | 1H Fast V3 Nohigh Range Only V1 | Momentum / breakout V3 Filtered | €10.247,95 | €247,95 | 41 | 41 | 46,34% | 1,25 | €6,05 | 3,97% |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | Momentum / breakout V3 Filtered | €10.239,20 | €239,20 | 17 | 17 | 52,94% | 4,50 | €14,07 | 1,01% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | Momentum / breakout V3 Filtered | €10.235,18 | €235,18 | 20 | 20 | 50,00% | 1,90 | €11,76 | 2,73% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €10.213,16 | €193,98 | 7 | 7 | 57,14% | 2,72 | €27,71 | 1,01% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.209,20 | €209,20 | 6 | 6 | 83,33% | 4,66 | €34,87 | 0,85% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €10.209,11 | €192,62 | 13 | 13 | 53,85% | 1,78 | €14,82 | 2,77% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €10.196,46 | €196,46 | 6 | 6 | 50,00% | 2,73 | €32,74 | 1,05% |
| TEST | 1H Fast Tp2 V1 | Momentum / breakout | €10.195,40 | €229,87 | 227 | 227 | 40,09% | 1,06 | €1,01 | 6,56% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | Momentum / breakout V3 Filtered | €10.185,37 | €185,37 | 22 | 22 | 40,91% | 1,57 | €8,43 | 2,27% |
| TEST | Main Dynamic Asset Selector V1 | Confluenza trend | €10.161,45 | €161,45 | 13 | 13 | 38,46% | 1,47 | €12,42 | 2,04% |
| TEST | 1H Fast Score 6 75 Range Only V1 | Momentum / breakout | €10.149,62 | €149,62 | 38 | 38 | 44,74% | 1,14 | €3,94 | 3,35% |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | Momentum / breakout V3 Filtered | €10.145,12 | €145,12 | 44 | 44 | 45,45% | 1,20 | €3,30 | 2,91% |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | Momentum / breakout V3 Filtered | €10.124,13 | €139,56 | 53 | 53 | 50,94% | 1,12 | €2,63 | 4,50% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €10.110,49 | €127,83 | 46 | 41 | 45,65% | 1,11 | €2,78 | 3,89% |
| TEST | Sol Ema 1H | Trend following EMA | €10.099,15 | €84,65 | 14 | 14 | 42,86% | 1,22 | €6,05 | 3,33% |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | Momentum / breakout V3 Filtered | €10.099,04 | €99,04 | 55 | 55 | 54,55% | 1,12 | €1,80 | 3,59% |
| TEST | Sol Ema 4H | Trend following EMA | €10.076,72 | €56,08 | 8 | 8 | 37,50% | 1,26 | €7,01 | 2,27% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €10.073,02 | €87,49 | 125 | 125 | 44,00% | 1,03 | €0,70 | 11,27% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.061,24 | €29,45 | 2 | 2 | 50,00% | 1,54 | €14,72 | 0,91% |
| TEST | Combo Adaptive Partial 1R V1 | Combo Adaptive | €10.049,82 | €78,27 | 152 | 152 | 44,74% | 1,03 | €0,51 | 8,69% |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | Momentum / breakout V3 Filtered | €10.048,77 | €48,77 | 23 | 23 | 43,48% | 1,12 | €2,12 | 3,05% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €10.045,08 | €45,08 | 28 | 28 | 46,43% | 1,40 | €1,61 | 0,33% |
| TEST | Rapida 1H V1 | Momentum / breakout | €10.043,28 | €43,28 | 78 | 78 | 34,62% | 1,02 | €0,55 | 6,76% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €10.041,52 | €70,19 | 2 | 2 | 50,00% | 2,39 | €35,09 | 0,96% |
| TEST | 1H Balanced Short Trend Down Strict V1 | Confluenza trend | €10.035,46 | €35,46 | 13 | 13 | 38,46% | 1,13 | €2,73 | 1,80% |
| TEST | Scalp RSI Long 20 · prudente · 5x | Inversione RSI estrema 15m | €10.028,67 | €28,67 | 9 | 9 | 55,56% | 1,80 | €3,19 | 0,36% |
| TEST | Scalp RSI Short 85 · €50 · 15x | Inversione RSI estrema 15m | €10.017,98 | €17,98 | 5 | 5 | 60,00% | 1,69 | €3,60 | 0,31% |
| TEST | Scanner Top10 Long | Scanner Top10 Long | €10.014,31 | €55,02 | 128 | 128 | 47,66% | 1,02 | €0,43 | 10,31% |
| TEST | Scalp RSI Short 80 · €50 · 15x | Inversione RSI estrema 15m | €10.009,36 | €9,36 | 16 | 16 | 37,50% | 1,17 | €0,58 | 0,53% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €10.009,02 | €9,02 | 28 | 28 | 46,43% | 1,40 | €0,32 | 0,07% |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | Momentum / breakout V3 Filtered | €10.008,92 | €8,92 | 30 | 30 | 36,67% | 1,02 | €0,30 | 4,84% |
| TEST | Scalp RSI Short 85 · €10 · 15x | Inversione RSI estrema 15m | €10.003,60 | €3,60 | 5 | 5 | 60,00% | 1,69 | €0,72 | 0,06% |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | Momentum / breakout V3 Filtered | €10.003,37 | €3,37 | 8 | 8 | 37,50% | 1,02 | €0,42 | 2,15% |
| TEST | Scanner Top5 Btc Tp3 V1 | Scanner Top 5 + forza BTC | €10.001,89 | €35,33 | 105 | 105 | 40,95% | 1,01 | €0,34 | 11,78% |
| TEST | Scalp RSI Short 80 · €10 · 15x | Inversione RSI estrema 15m | €10.001,87 | €1,87 | 16 | 16 | 37,50% | 1,17 | €0,12 | 0,11% |
| TEST | Scanner Bottom5 Short Continuation V1 | Scanner Bottom5 Short Continuation | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 20 · €10 · 15x | Inversione RSI estrema 15m | €9.999,33 | €-0,67 | 9 | 9 | 44,44% | 0,85 | €-0,07 | 0,04% |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | Momentum / breakout | €9.997,66 | €34,72 | 100 | 100 | 44,00% | 1,02 | €0,35 | 7,10% |
| TEST | Scalp RSI Long 15 · €10 · 15x | Inversione RSI estrema 15m | €9.997,60 | €-2,40 | 3 | 3 | 33,33% | 0,13 | €-0,80 | 0,02% |
| TEST | Scalp RSI Long 20 · €50 · 15x | Inversione RSI estrema 15m | €9.996,64 | €-3,36 | 9 | 9 | 44,44% | 0,85 | €-0,37 | 0,21% |
| TEST | Scanner Top5 Btc Runner25 V1 | Scanner Top 5 + forza BTC | €9.996,04 | €29,46 | 109 | 109 | 41,28% | 1,01 | €0,27 | 12,06% |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | Momentum / breakout V3 Filtered | €9.995,23 | €-4,77 | 15 | 15 | 46,67% | 0,99 | €-0,32 | 2,70% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €9.992,60 | €-7,40 | 10 | 10 | 50,00% | 0,97 | €-0,74 | 1,89% |
| TEST | Scalp RSI Short 85 · prudente · 5x | Inversione RSI estrema 15m | €9.991,38 | €-8,62 | 5 | 5 | 60,00% | 0,61 | €-1,72 | 0,30% |
| TEST | Scalp RSI Long 25 · €10 · 15x | Inversione RSI estrema 15m | €9.990,45 | €-9,55 | 15 | 15 | 40,00% | 0,36 | €-0,64 | 0,14% |
| TEST | Doge Ema 1H | Trend following EMA | €9.988,85 | €-11,15 | 17 | 17 | 58,82% | 0,97 | €-0,66 | 2,77% |
| TEST | Btc Ema 4H | Trend following EMA | €9.988,30 | €19,41 | 3 | 3 | 33,33% | 1,19 | €6,47 | 1,76% |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | €9.988,00 | €-12,00 | 3 | 3 | 33,33% | 0,13 | €-4,00 | 0,12% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €9.987,48 | €-12,52 | 15 | 15 | 40,00% | 0,83 | €-0,83 | 0,71% |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | €9.980,94 | €-19,06 | 3 | 3 | 33,33% | 0,19 | €-6,35 | 0,20% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €9.974,11 | €-18,28 | 3 | 3 | 33,33% | 0,83 | €-6,09 | 1,36% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €9.973,34 | €-20,28 | 152 | 152 | 42,11% | 0,99 | €-0,13 | 9,12% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €9.968,58 | €-31,42 | 9 | 9 | 44,44% | 0,86 | €-3,49 | 1,23% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €9.957,15 | €-42,85 | 10 | 10 | 50,00% | 0,85 | €-4,29 | 1,49% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €9.955,52 | €-58,78 | 15 | 15 | 40,00% | 0,87 | €-3,92 | 4,59% |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | €9.952,25 | €-47,75 | 15 | 15 | 40,00% | 0,36 | €-3,18 | 0,72% |
| TEST | Eth Ema 4H | Trend following EMA | €9.948,10 | €-88,72 | 5 | 5 | 20,00% | 0,58 | €-17,74 | 1,83% |
| TEST | Scalp RSI Short 80 · prudente · 5x | Inversione RSI estrema 15m | €9.940,42 | €-59,58 | 16 | 16 | 37,50% | 0,40 | €-3,72 | 0,89% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.939,62 | €-60,38 | 28 | 28 | 46,43% | 0,60 | €-2,16 | 0,84% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €9.934,86 | €-34,19 | 4 | 4 | 25,00% | 0,80 | €-8,55 | 2,43% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €9.924,84 | €-75,16 | 13 | 13 | 53,85% | 0,79 | €-5,78 | 3,08% |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | Combo Adaptive | €9.912,24 | €-87,76 | 39 | 39 | 46,15% | 0,91 | €-2,25 | 4,21% |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | Momentum / breakout | €9.869,22 | €-27,73 | 63 | 63 | 41,27% | 0,98 | €-0,44 | 3,73% |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | Momentum / breakout V3 Filtered | €9.837,38 | €-162,62 | 37 | 37 | 40,54% | 0,76 | €-4,40 | 3,08% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.835,77 | €-178,80 | 11 | 11 | 36,36% | 0,61 | €-16,25 | 2,37% |
| TEST | Btc Ema 1H | Trend following EMA | €9.833,66 | €-166,34 | 13 | 13 | 30,77% | 0,61 | €-12,80 | 1,94% |
| TEST | 1H Fast V3 No Esports Long Only V1 | Momentum / breakout V3 Filtered | €9.824,53 | €-120,90 | 154 | 154 | 43,51% | 0,96 | €-0,79 | 10,60% |
| TEST | Combo Adaptive Regime V1 | Combo Adaptive | €9.824,32 | €-166,77 | 58 | 58 | 48,28% | 0,88 | €-2,88 | 5,38% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.817,39 | €-155,37 | 13 | 13 | 38,46% | 0,66 | €-11,95 | 3,14% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | Momentum / breakout V3 Filtered | €9.817,34 | €-182,66 | 24 | 24 | 41,67% | 0,64 | €-7,61 | 3,23% |
| TEST | Eth Ema 1H | Trend following EMA | €9.798,25 | €-186,42 | 18 | 18 | 38,89% | 0,71 | €-10,36 | 4,80% |
| TEST | Combo Adaptive Quality7 Regime V1 | Combo Adaptive | €9.787,56 | €-212,44 | 39 | 39 | 41,03% | 0,79 | €-5,45 | 5,41% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | Momentum / breakout V3 Filtered | €9.762,18 | €-237,82 | 7 | 7 | 14,29% | 0,02 | €-33,97 | 2,82% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €9.739,55 | €-262,74 | 112 | 106 | 41,96% | 0,92 | €-2,35 | 10,88% |
| TEST | Combo Adaptive Quality7 V1 | Combo Adaptive | €9.738,12 | €-259,61 | 80 | 80 | 38,75% | 0,87 | €-3,25 | 8,88% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | Momentum / breakout V3 Filtered | €9.723,72 | €-276,28 | 31 | 31 | 32,26% | 0,62 | €-8,91 | 4,83% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €9.703,71 | €-296,29 | 7 | 7 | 28,57% | 0,22 | €-42,33 | 4,16% |
| TEST | Scanner Top15 Long | Scanner Top15 Long | €9.685,66 | €-279,53 | 125 | 125 | 47,20% | 0,89 | €-2,24 | 10,31% |
| TEST | Scanner Top20 Long | Scanner Top20 Long | €9.685,66 | €-279,53 | 125 | 125 | 47,20% | 0,89 | €-2,24 | 10,31% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.679,31 | €-320,69 | 17 | 17 | 29,41% | 0,41 | €-18,86 | 3,93% |
| TEST | Combo Scanner | Combo Scanner | €9.677,88 | €-308,19 | 130 | 130 | 43,85% | 0,90 | €-2,37 | 11,38% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.647,94 | €-321,93 | 13 | 13 | 23,08% | 0,47 | €-24,76 | 3,74% |
| TEST | 1H Fast V3 No Esports V1 | Momentum / breakout V3 Filtered | €9.629,18 | €-336,51 | 204 | 204 | 43,14% | 0,92 | €-1,65 | 9,00% |
| TEST | 1H Balanced Long No Rhv V1 | Confluenza trend | €9.622,82 | €-388,06 | 99 | 99 | 44,44% | 0,82 | €-3,92 | 9,26% |
| TEST | 1H Fast V3 Nohigh V1 | Momentum / breakout V3 Filtered | €9.612,09 | €-333,85 | 123 | 123 | 43,09% | 0,88 | €-2,71 | 7,10% |
| TEST | Scanner Top5 Btc Guard V1 | Scanner Top 5 + forza BTC | €9.604,38 | €-458,79 | 106 | 106 | 38,68% | 0,83 | €-4,33 | 7,34% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | Momentum / breakout V3 Filtered | €9.579,83 | €-420,17 | 11 | 11 | 0,00% | 0,00 | €-38,20 | 4,20% |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | Momentum / breakout V3 Filtered | €9.548,64 | €-398,58 | 82 | 82 | 40,24% | 0,82 | €-4,86 | 6,64% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €9.472,98 | €-674,88 | 52 | 52 | 30,77% | 0,64 | €-12,98 | 8,18% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €9.460,20 | €-568,34 | 103 | 94 | 42,72% | 0,75 | €-5,52 | 8,84% |
| TEST | 1H Fast V3 Long Only V1 | Momentum / breakout V3 Filtered | €9.458,74 | €-487,84 | 165 | 165 | 40,61% | 0,86 | €-2,96 | 12,52% |
| TEST | Scanner Top5 Btc Mfe V1 | Scanner Top 5 + forza BTC | €9.442,96 | €-543,47 | 117 | 117 | 42,74% | 0,78 | €-4,65 | 12,28% |
| TEST | Master Adaptive Gb20 Be V1 | Master Adaptive Consensus | €9.434,99 | €-547,27 | 59 | 59 | 30,51% | 0,69 | €-9,28 | 8,39% |
| TEST | 1H Balanced V3 Long Only V1 | Confluenza trend V3 Filtered | €9.433,84 | €-559,50 | 106 | 106 | 42,45% | 0,73 | €-5,28 | 8,85% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €9.426,72 | €-607,88 | 60 | 60 | 35,00% | 0,70 | €-10,13 | 7,26% |
| TEST | Master Adaptive Gb20 Partial V1 | Master Adaptive Consensus | €9.424,96 | €-557,32 | 54 | 54 | 35,19% | 0,68 | €-10,32 | 7,98% |
| TEST | 1H Fast Score 6 75 V1 | Momentum / breakout | €9.415,87 | €-584,13 | 137 | 137 | 40,15% | 0,84 | €-4,26 | 12,33% |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | €9.388,50 | €-593,85 | 56 | 56 | 33,93% | 0,69 | €-10,60 | 7,80% |
| TEST | Scanner Top5 Btc Guard Mfe V1 | Scanner Top 5 + forza BTC | €9.381,02 | €-680,68 | 123 | 123 | 39,84% | 0,77 | €-5,53 | 8,78% |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | Momentum / breakout V3 Filtered | €9.370,06 | €-577,98 | 87 | 87 | 44,83% | 0,78 | €-6,64 | 8,22% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €9.357,25 | €-609,24 | 66 | 66 | 36,36% | 0,71 | €-9,23 | 7,96% |
| TEST | Combo Trend | Combo Trend | €9.331,16 | €-627,65 | 154 | 154 | 38,96% | 0,83 | €-4,08 | 10,85% |
| TEST | Scanner Bottom10 Short | Scanner Bottom10 Short | €9.320,74 | €-677,79 | 70 | 70 | 31,43% | 0,65 | €-9,68 | 9,06% |
| TEST | Scanner Bottom15 Short | Scanner Bottom15 Short | €9.320,74 | €-677,79 | 70 | 70 | 31,43% | 0,65 | €-9,68 | 9,06% |
| TEST | Scanner Bottom20 Short | Scanner Bottom20 Short | €9.320,74 | €-677,79 | 70 | 70 | 31,43% | 0,65 | €-9,68 | 9,06% |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | Scanner Top 5 + forza BTC | €9.320,05 | €-697,02 | 26 | 26 | 19,23% | 0,26 | €-26,81 | 8,44% |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | Scanner Top 5 + forza BTC | €9.304,57 | €-756,85 | 70 | 70 | 35,71% | 0,66 | €-10,81 | 9,79% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €9.263,76 | €-718,82 | 91 | 91 | 48,35% | 0,65 | €-7,90 | 9,02% |
| TEST | Master Adaptive Gb20 Loss Cap V1 | Master Adaptive Consensus | €9.261,89 | €-709,49 | 48 | 48 | 25,00% | 0,61 | €-14,78 | 11,41% |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | Scanner Bottom 5 Short | €9.256,15 | €-742,38 | 61 | 61 | 31,15% | 0,58 | €-12,17 | 9,08% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.255,55 | €-741,47 | 125 | 125 | 38,40% | 0,71 | €-5,93 | 12,31% |
| TEST | Scanner Bottom5 Short Profit Lock V1 | Scanner Bottom 5 Short | €9.242,07 | €-756,47 | 62 | 62 | 30,65% | 0,56 | €-12,20 | 9,08% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.170,95 | €-827,60 | 89 | 89 | 31,46% | 0,64 | €-9,30 | 10,17% |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | Momentum / breakout | €9.165,52 | €-834,48 | 95 | 95 | 41,05% | 0,72 | €-8,78 | 12,64% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €9.150,69 | €-849,31 | 121 | 121 | 36,36% | 0,69 | €-7,02 | 13,99% |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | Scanner Top 5 + forza BTC | €9.142,42 | €-917,95 | 86 | 86 | 36,05% | 0,63 | €-10,67 | 9,10% |
| TEST | 1H Fast V3 Cap75 V1 | Momentum / breakout V3 Filtered | €9.106,22 | €-893,78 | 136 | 136 | 36,03% | 0,75 | €-6,57 | 14,10% |
| TEST | Combo Adaptive Mfe Trail | Combo Adaptive | €9.072,48 | €-899,77 | 160 | 160 | 41,25% | 0,72 | €-5,62 | 15,45% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €8.967,07 | €-1.032,93 | 47 | 47 | 36,17% | 0,47 | €-21,98 | 12,56% |
| TEST | Combo Adaptive Runner25 V1 | Combo Adaptive | €8.964,11 | €-1.035,89 | 94 | 94 | 30,85% | 0,53 | €-11,02 | 12,67% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €8.881,45 | €-1.088,76 | 56 | 56 | 26,79% | 0,56 | €-19,44 | 11,51% |
| TEST | Scanner Top5 Btc Btc Le3 V1 | Scanner Top 5 + forza BTC | €8.864,81 | €-1.151,44 | 72 | 72 | 30,56% | 0,48 | €-15,99 | 13,50% |
| TEST | Combo Adaptive Tp3 V1 | Combo Adaptive | €8.796,64 | €-1.203,36 | 75 | 75 | 29,33% | 0,38 | €-16,04 | 12,67% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €8.740,52 | €-1.259,48 | 81 | 81 | 38,27% | 0,55 | €-15,55 | 14,60% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €8.445,51 | €-1.554,49 | 105 | 105 | 27,62% | 0,47 | €-14,80 | 17,39% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | SPCX | LONG | Confluenza trend | 240m | 3,0x | 136,56189 | 136,56189 | 128,79610 | 91,72407 | 152,09346 | €285,50 | €856,50 | €48,71 | €0,00 |
| Principale 4H | VELVET | LONG | Confluenza trend | 240m | 3,0x | 0,55987 | 0,55987 | 0,49269 | 0,37605 | 0,69424 | €131,08 | €393,24 | €47,19 | €0,00 |
| Principale 4H | EDEN | LONG | Confluenza trend | 240m | 3,0x | 0,06195 | 0,06195 | 0,05451 | 0,04161 | 0,07681 | €130,34 | €391,02 | €46,92 | €0,00 |
| Principale 4H | TRUMP | LONG | Confluenza trend | 240m | 3,0x | 2,46049 | 2,46049 | 2,16523 | 1,65263 | 3,05101 | €134,98 | €404,95 | €48,59 | €0,00 |
| Principale 4H | XRP | LONG | Confluenza trend | 240m | 3,0x | 1,46057 | 1,39828 | 1,30460 | 0,98102 | 1,77252 | €8,58 | €25,73 | €2,75 | €-1,10 |
| Principale 4H | HYPE | LONG | Confluenza trend | 240m | 3,0x | 78,87277 | 80,67500 | 73,04357 | 52,97621 | 90,53117 | €8,52 | €25,56 | €1,89 | €0,58 |
| 1H Balanced Long No Rhv V1 | SKHYNIX | LONG | Confluenza trend | 60m | 3,0x | 1214,11277 | 1254,35000 | 1170,18211 | 815,47908 | 1301,97411 | €413,43 | €1.240,28 | €44,88 | €41,10 |
| 1H Balanced Long No Rhv V1 | BOME | LONG | Confluenza trend | 60m | 3,0x | 0,00129 | 0,00129 | 0,00114 | 0,00087 | 0,00160 | €134,98 | €404,95 | €48,59 | €0,00 |
| 1H Balanced Long No Rhv V1 | TAO | LONG | Confluenza trend | 60m | 3,0x | 247,38947 | 247,38947 | 237,94346 | 166,16326 | 266,28148 | €428,20 | €1.284,61 | €49,05 | €0,00 |
| 1H Balanced Long No Rhv V1 | ETH | LONG | Confluenza trend | 60m | 3,0x | 2502,31036 | 2483,05000 | 2464,79465 | 1680,71846 | 2577,34176 | €1.075,18 | €3.225,54 | €48,36 | €-24,83 |
| 1H Balanced Long No Rhv V1 | HYPE | LONG | Confluenza trend | 60m | 3,0x | 82,20244 | 80,67500 | 79,78758 | 55,21264 | 87,03215 | €28,40 | €85,21 | €2,50 | €-1,58 |
| Bilanciata 1H V2 | SKHYNIX | LONG | Confluenza trend V2 | 60m | 3,0x | 1214,11277 | 1254,35000 | 1170,18211 | 815,47908 | 1301,97411 | €422,38 | €1.267,15 | €45,85 | €41,99 |
| Bilanciata 1H V2 | ETH | LONG | Confluenza trend V2 | 60m | 3,0x | 2502,31036 | 2483,05000 | 2464,79465 | 1680,71846 | 2577,34176 | €1.055,40 | €3.166,20 | €47,47 | €-24,37 |
| Bilanciata 1H V2 | SOL | LONG | Confluenza trend V2 | 60m | 3,0x | 100,22404 | 100,94900 | 97,91287 | 67,31715 | 104,84638 | €685,30 | €2.055,91 | €47,41 | €14,87 |
| Bilanciata 1H V3 Filtered | SKHYNIX | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1220,85412 | 1254,35000 | 1177,63561 | 820,00702 | 1307,29117 | €460,42 | €1.381,27 | €48,90 | €37,90 |
| Bilanciata 1H V3 Filtered | ZEC | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 807,93155 | 776,09000 | 737,89694 | 542,66069 | 948,00078 | €195,29 | €585,88 | €50,79 | €-23,09 |
| Bilanciata 1H V3 Filtered | XRP | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1,47399 | 1,39828 | 1,35380 | 0,99003 | 1,71438 | €205,84 | €617,51 | €50,35 | €-31,72 |
| Bilanciata 1H V3 Filtered | ADA | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,20238 | 0,20238 | 0,20803 | 0,26883 | 0,19107 | €19,31 | €57,92 | €1,62 | €-0,00 |
| Bilanciata 1H V3 Filtered | ETH | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 2502,31036 | 2483,05000 | 2464,79465 | 1680,71846 | 2577,34176 | €9,10 | €27,30 | €0,41 | €-0,21 |
| Bilanciata 1H V3 Filtered | SOL | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 100,22404 | 100,94900 | 97,91287 | 67,31715 | 104,84638 | €697,84 | €2.093,51 | €48,28 | €15,14 |
| 1H Fast Score 6 75 Cost Aware V1 | BTW | LONG | Momentum / breakout | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €8,91 | €26,72 | €3,13 | €0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00086 | 0,00146 | €215,92 | €647,76 | €57,03 | €0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | NEAR | LONG | Momentum / breakout | 60m | 3,0x | 2,08142 | 2,08142 | 2,02315 | 1,39802 | 2,16882 | €42,86 | €128,59 | €3,60 | €0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €157,13 | €471,39 | €56,57 | €-0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | ETH | LONG | Momentum / breakout | 60m | 3,0x | 2502,31036 | 2483,05000 | 2473,13147 | 1680,71846 | 2546,07867 | €1.587,89 | €4.763,66 | €55,55 | €-36,67 |
| 1H Fast Score 6 75 Cost Aware V1 | SOL | LONG | Momentum / breakout | 60m | 3,0x | 100,22404 | 100,94900 | 100,46539 | 67,31715 | 102,92041 | €853,08 | €2.559,25 | €0,00 | €18,51 |
| 1H Fast Nohigh Cap75 V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €139,29 | €417,86 | €50,14 | €-0,00 |
| 1H Fast Nohigh Cap75 V1 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €141,57 | €424,71 | €50,14 | €-0,00 |
| 1H Fast Nohigh Cap75 V1 | ADA | SHORT | Momentum / breakout | 60m | 3,0x | 0,20481 | 0,20481 | 0,20925 | 0,27205 | 0,19815 | €53,21 | €159,62 | €3,46 | €-0,00 |
| 1H Fast Nohigh Cap75 V1 | ETH | LONG | Momentum / breakout | 60m | 3,0x | 2502,31036 | 2483,05000 | 2473,13147 | 1680,71846 | 2546,07867 | €1.468,46 | €4.405,38 | €51,37 | €-33,91 |
| 1H Fast Nohigh Cap75 V1 | SOL | LONG | Momentum / breakout | 60m | 3,0x | 100,22404 | 100,94900 | 100,46539 | 67,31715 | 102,92041 | €12,71 | €38,12 | €0,00 | €0,28 |
| 1H Fast Nohigh Cap75 V1 | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 82,02040 | 80,67500 | 80,13051 | 55,09037 | 84,85524 | €8,75 | €26,25 | €0,60 | €-0,43 |
| 1H Fast Nohigh Cap75 V1 | SKHYNIX | LONG | Momentum / breakout | 60m | 3,0x | 1266,44941 | 1254,35000 | 1241,20633 | 850,63186 | 1304,31405 | €11,10 | €33,31 | €0,66 | €-0,32 |
| 1H Fast Nohigh Cap75 V1 | BTR | LONG | Momentum / breakout | 60m | 3,0x | 0,17284 | 0,17281 | 0,15210 | 0,11609 | 0,20396 | €133,32 | €399,96 | €48,00 | €-0,08 |
| 1H Fast Long Btc 1 3 Cap75 V1 | ETH | LONG | Momentum / breakout | 60m | 3,0x | 2502,31036 | 2483,05000 | 2473,13147 | 1680,71846 | 2546,07867 | €1.420,65 | €4.261,95 | €49,70 | €-32,80 |
| 1H Fast Long Btc 1 3 Cap75 V1 | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 82,20244 | 80,67500 | 80,32422 | 55,21264 | 85,01977 | €724,52 | €2.173,57 | €49,66 | €-40,39 |
| 1H Fast Long Btc 1 3 Cap75 V1 | SOL | LONG | Momentum / breakout | 60m | 3,0x | 101,66933 | 100,94900 | 99,72283 | 68,28790 | 104,58908 | €19,33 | €58,00 | €1,11 | €-0,41 |
| 1H Fast Long Btc 1 3 Cap75 V1 | SKHYNIX | LONG | Momentum / breakout | 60m | 3,0x | 1266,44941 | 1254,35000 | 1241,20633 | 850,63186 | 1304,31405 | €828,42 | €2.485,26 | €49,54 | €-23,74 |
| 1H Fast Long Btc 1 3 Cap75 V1 | BTR | LONG | Momentum / breakout | 60m | 3,0x | 0,17284 | 0,17281 | 0,15210 | 0,11609 | 0,20396 | €131,62 | €394,86 | €47,38 | €-0,08 |
| 1H Fast No Pepe V1 | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €172,22 | €516,67 | €49,86 | €0,00 |
| 1H Fast No Pepe V1 | TAO | LONG | Momentum / breakout | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €47,93 | €143,78 | €4,27 | €0,00 |
| 1H Fast No Pepe V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €136,27 | €408,80 | €49,06 | €-0,00 |
| 1H Fast No Pepe V1 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €9,48 | €28,43 | €3,41 | €-0,00 |
| 1H Fast No Pepe V1 | ETH | LONG | Momentum / breakout | 60m | 3,0x | 2502,31036 | 2483,05000 | 2473,13147 | 1680,71846 | 2546,07867 | €1.517,98 | €4.553,94 | €53,10 | €-35,05 |
| 1H Fast No Pepe V1 | SOL | LONG | Momentum / breakout | 60m | 3,0x | 100,22404 | 100,94900 | 100,46539 | 67,31715 | 102,92041 | €11,02 | €33,07 | €0,00 | €0,24 |
| 1H Fast No Pepe V1 | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 82,02040 | 80,67500 | 80,13051 | 55,09037 | 84,85524 | €9,11 | €27,32 | €0,63 | €-0,45 |
| 1H Fast No Pepe V1 | SKHYNIX | LONG | Momentum / breakout | 60m | 3,0x | 1266,44941 | 1254,35000 | 1241,20633 | 850,63186 | 1304,31405 | €11,54 | €34,62 | €0,69 | €-0,33 |
| 1H Fast No Pepe V1 | BTR | LONG | Momentum / breakout | 60m | 3,0x | 0,17284 | 0,17281 | 0,15210 | 0,11609 | 0,20396 | €139,94 | €419,82 | €50,38 | €-0,08 |
| 1H Fast Tp2 V1 | BTW | LONG | Momentum / breakout | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,56752 | €142,85 | €428,56 | €50,25 | €0,00 |
| 1H Fast Tp2 V1 | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00132 | 0,00132 | 0,00119 | 0,00088 | 0,00158 | €18,87 | €56,62 | €5,59 | €0,00 |
| 1H Fast Tp2 V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,17246 | 0,17246 | 0,17246 | 0,22908 | 0,13107 | €139,71 | €419,14 | €0,00 | €-0,00 |
| 1H Fast Tp2 V1 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03379 | €141,13 | €423,40 | €50,81 | €-0,00 |
| 1H Fast Tp2 V1 | ETH | LONG | Momentum / breakout | 60m | 3,0x | 2502,31036 | 2483,05000 | 2473,13147 | 1680,71846 | 2560,66812 | €1.344,34 | €4.033,01 | €47,03 | €-31,04 |
| 1H Fast Tp2 V1 | SOL | LONG | Momentum / breakout | 60m | 3,0x | 101,73634 | 100,94900 | 99,75933 | 68,33291 | 105,69037 | €8,89 | €26,67 | €0,52 | €-0,21 |
| Rapida 1H V2 | ETH | LONG | Momentum / breakout V2 | 60m | 3,0x | 2502,31036 | 2483,05000 | 2473,13147 | 1680,71846 | 2546,07867 | €1.447,56 | €4.342,69 | €50,64 | €-33,43 |
| Rapida 1H V2 | SOL | LONG | Momentum / breakout V2 | 60m | 3,0x | 100,22404 | 100,94900 | 100,46539 | 67,31715 | 102,92041 | €939,38 | €2.818,13 | €0,00 | €20,38 |
| Rapida 1H V3 Filtered | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €172,00 | €515,99 | €49,79 | €0,00 |
| Rapida 1H V3 Filtered | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €589,98 | €1.769,95 | €52,56 | €0,00 |
| Rapida 1H V3 Filtered | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €140,02 | €420,06 | €50,41 | €-0,00 |
| Rapida 1H V3 Filtered | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €16,99 | €50,96 | €6,11 | €-0,00 |
| Rapida 1H V3 Filtered | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2502,31036 | 2483,05000 | 2473,13147 | 1680,71846 | 2546,07867 | €1.391,13 | €4.173,39 | €48,66 | €-32,12 |
| 1H Fast V3 Nohigh V1 | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €131,05 | €393,14 | €47,18 | €-0,00 |
| 1H Fast V3 Nohigh V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €133,20 | €399,59 | €47,18 | €-0,00 |
| 1H Fast V3 Nohigh V1 | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,20238 | 0,20238 | 0,20677 | 0,26883 | 0,19578 | €27,66 | €82,98 | €1,80 | €-0,00 |
| 1H Fast V3 Nohigh V1 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2502,31036 | 2483,05000 | 2473,13147 | 1680,71846 | 2546,07867 | €1.372,20 | €4.116,59 | €48,00 | €-31,69 |
| 1H Fast V3 Nohigh V1 | SOL | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 101,66933 | 100,94900 | 99,72283 | 68,28790 | 104,58908 | €840,73 | €2.522,18 | €48,29 | €-17,87 |
| 1H Fast V3 Long Only V1 | BTW | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €126,57 | €379,72 | €44,52 | €0,00 |
| 1H Fast V3 Long Only V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00147 | €9,56 | €28,69 | €2,66 | €0,00 |
| 1H Fast V3 Long Only V1 | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €554,42 | €1.663,26 | €49,39 | €0,00 |
| 1H Fast V3 Long Only V1 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2502,31036 | 2483,05000 | 2473,13147 | 1680,71846 | 2546,07867 | €1.350,31 | €4.050,93 | €47,24 | €-31,18 |
| 1H Fast V3 Long Only V1 | SOL | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 101,66933 | 100,94900 | 99,72283 | 68,28790 | 104,58908 | €805,18 | €2.415,53 | €46,25 | €-17,11 |
| 1H Fast V3 Long Nohigh Cap75 V1 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2502,31036 | 2483,05000 | 2473,13147 | 1680,71846 | 2546,07867 | €1.352,71 | €4.058,14 | €47,32 | €-31,24 |
| 1H Fast V3 Long Nohigh Cap75 V1 | SOL | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 101,66933 | 100,94900 | 99,72283 | 68,28790 | 104,58908 | €829,01 | €2.487,02 | €47,62 | €-17,62 |
| 1H Fast V3 No Esports V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €169,36 | €508,09 | €49,03 | €0,00 |
| 1H Fast V3 No Esports V1 | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €27,04 | €81,13 | €2,41 | €0,00 |
| 1H Fast V3 No Esports V1 | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €133,96 | €401,88 | €48,23 | €-0,00 |
| 1H Fast V3 No Esports V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €129,73 | €389,20 | €46,70 | €-0,00 |
| 1H Fast V3 No Esports V1 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2502,31036 | 2483,05000 | 2473,13147 | 1680,71846 | 2546,07867 | €1.340,17 | €4.020,52 | €46,88 | €-30,95 |
| 1H Fast V3 No Esports Long Only V1 | BTW | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €132,94 | €398,81 | €46,76 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00147 | €10,06 | €30,18 | €2,80 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2502,31036 | 2483,05000 | 2473,13147 | 1680,71846 | 2546,07867 | €1.391,98 | €4.175,94 | €48,69 | €-32,14 |
| 1H Fast V3 No Esports Long Only V1 | SOL | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 101,66933 | 100,94900 | 99,72283 | 68,28790 | 104,58908 | €853,07 | €2.559,21 | €49,00 | €-18,13 |
| 1H Fast V3 No Esports Mfe Lock V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €173,11 | €519,32 | €50,11 | €0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €593,79 | €1.781,38 | €52,90 | €0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €140,93 | €422,78 | €50,73 | €-0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €17,09 | €51,28 | €6,15 | €-0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2502,31036 | 2483,05000 | 2473,13147 | 1680,71846 | 2546,07867 | €1.400,13 | €4.200,39 | €48,98 | €-32,33 |
| 1H Fast V3 No Esports Stress Guard V1 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2502,31036 | 2483,05000 | 2473,13147 | 1680,71846 | 2546,07867 | €1.371,88 | €4.115,65 | €47,99 | €-31,68 |
| 1H Fast V3 No Esports Stress Guard V1 | SOL | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 100,22404 | 100,94900 | 100,46539 | 67,31715 | 102,92041 | €940,56 | €2.821,68 | €0,00 | €20,41 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2502,31036 | 2483,05000 | 2473,13147 | 1680,71846 | 2546,07867 | €1.333,94 | €4.001,81 | €46,66 | €-30,80 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | SOL | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 101,66933 | 100,94900 | 99,72283 | 68,28790 | 104,58908 | €813,51 | €2.440,54 | €46,73 | €-17,29 |
| Ampia 4H | SPCX | LONG | Confluenza trend | 240m | 2,0x | 136,56189 | 136,56189 | 126,46637 | 68,96375 | 164,82935 | €323,86 | €647,73 | €47,88 | €0,00 |
| Ampia 4H | VELVET | LONG | Confluenza trend | 240m | 2,0x | 0,55987 | 0,55987 | 0,49269 | 0,28274 | 0,74799 | €201,63 | €403,26 | €48,39 | €0,00 |
| Ampia 4H | LINK | LONG | Confluenza trend | 240m | 2,0x | 11,96839 | 11,96839 | 11,08055 | 6,04404 | 14,45436 | €14,07 | €28,15 | €2,09 | €0,00 |
| Ampia 4H | ETH | LONG | Confluenza trend | 240m | 2,0x | 2430,03591 | 2483,05000 | 2267,54364 | 1227,16813 | 2885,01426 | €18,82 | €37,65 | €2,52 | €0,82 |
| Ampia 4H | HYPE | LONG | Confluenza trend | 240m | 2,0x | 79,31286 | 80,67500 | 70,73982 | 40,05299 | 103,31737 | €13,82 | €27,64 | €2,99 | €0,47 |
| Ampia 4H | TRUMP | LONG | Confluenza trend | 240m | 2,0x | 2,37347 | 2,37347 | 2,08866 | 1,19860 | 3,17096 | €210,83 | €421,66 | €50,60 | €0,00 |
| Ampia 4H | DOGE | SHORT | Confluenza trend | 240m | 2,0x | 0,08583 | 0,08649 | 0,09382 | 0,12832 | 0,06346 | €274,53 | €549,07 | €51,10 | €-4,20 |
| Forza relativa 1H V2 | BEAT | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,25984 | 0,25984 | 0,25657 | 0,38847 | 0,19125 | €200,38 | €400,75 | €0,00 | €-0,00 |
| Forza relativa 1H V2 | TUT | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,04452 | 0,04452 | 0,04986 | 0,06656 | 0,03277 | €204,64 | €409,28 | €49,11 | €-0,00 |
| Forza relativa 1H V2 | ADA | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,20989 | 0,20989 | 0,20756 | 0,31379 | 0,19609 | €816,97 | €1.633,95 | €0,00 | €-0,00 |
| Forza relativa 1H V2 | SOL | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 100,68813 | 100,94900 | 98,15309 | 50,84751 | 106,26524 | €966,11 | €1.932,23 | €48,65 | €5,01 |
| Benchmark Donchian breakout 1H | SKHYNIX | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1174,33482 | 1254,35000 | 1128,44989 | 593,03908 | 1289,04713 | €641,25 | €1.282,50 | €50,11 | €87,39 |
| Benchmark Donchian breakout 1H | VELVET | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,14787 | 0,14787 | 0,16561 | 0,22107 | 0,10351 | €237,23 | €474,47 | €56,94 | €-0,00 |
| Benchmark Donchian breakout 1H | DOGE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,08603 | 0,08649 | 0,08867 | 0,12862 | 0,07943 | €921,23 | €1.842,45 | €56,55 | €-9,79 |
| Benchmark Donchian breakout 1H | ETH | LONG | Donchian breakout 20 barre | 60m | 2,0x | 2502,31036 | 2483,05000 | 2460,62625 | 1263,66673 | 2606,52065 | €42,45 | €84,89 | €1,41 | €-0,65 |
| Benchmark Donchian breakout 1H | SOL | LONG | Donchian breakout 20 barre | 60m | 2,0x | 101,66933 | 100,94900 | 98,88861 | 51,34301 | 108,62113 | €1.034,66 | €2.069,32 | €56,60 | €-14,66 |
| Benchmark Donchian breakout 1H | BTR | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,15358 | 0,17281 | 0,15358 | 0,07756 | 0,19965 | €17,34 | €34,68 | €0,00 | €4,34 |
| Donchian 1H Gb20 120R V1 | SKHYNIX | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1174,33482 | 1254,35000 | 1128,44989 | 593,03908 | 1289,04713 | €626,15 | €1.252,30 | €48,93 | €85,33 |
| Donchian 1H Gb20 120R V1 | VELVET | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,14787 | 0,14787 | 0,16561 | 0,22107 | 0,10351 | €231,65 | €463,30 | €55,60 | €-0,00 |
| Donchian 1H Gb20 120R V1 | DOGE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,08603 | 0,08649 | 0,08867 | 0,12862 | 0,07943 | €899,54 | €1.799,07 | €55,22 | €-9,56 |
| Donchian 1H Gb20 120R V1 | ETH | LONG | Donchian breakout 20 barre | 60m | 2,0x | 2502,31036 | 2483,05000 | 2460,62625 | 1263,66673 | 2606,52065 | €41,45 | €82,89 | €1,38 | €-0,64 |
| Donchian 1H Gb20 120R V1 | SOL | LONG | Donchian breakout 20 barre | 60m | 2,0x | 101,66933 | 100,94900 | 98,88861 | 51,34301 | 108,62113 | €1.010,30 | €2.020,60 | €55,26 | €-14,32 |
| Donchian 1H Gb20 120R V1 | BTR | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,15358 | 0,17281 | 0,15358 | 0,07756 | 0,19965 | €16,93 | €33,86 | €0,00 | €4,24 |
| Benchmark trend following EMA 1H | BEAT | SHORT | Trend following EMA | 60m | 2,0x | 0,28257 | 0,28257 | 0,25706 | 0,42244 | 0,20797 | €186,11 | €372,23 | €0,00 | €-0,00 |
| Benchmark trend following EMA 1H | ZEC | LONG | Trend following EMA | 60m | 2,0x | 807,93155 | 776,09000 | 730,11531 | 408,00543 | 979,12728 | €17,42 | €34,84 | €3,36 | €-1,37 |
| Benchmark trend following EMA 1H | TUT | SHORT | Trend following EMA | 60m | 2,0x | 0,04446 | 0,04446 | 0,04980 | 0,06647 | 0,03272 | €194,70 | €389,39 | €46,73 | €-0,00 |
| Benchmark trend following EMA 1H | VELVET | SHORT | Trend following EMA | 60m | 2,0x | 0,14786 | 0,14786 | 0,16560 | 0,22105 | 0,10883 | €187,91 | €375,83 | €45,10 | €-0,00 |
| Benchmark trend following EMA 1H | ADA | SHORT | Trend following EMA | 60m | 2,0x | 0,20989 | 0,20989 | 0,21687 | 0,31379 | 0,19455 | €681,63 | €1.363,26 | €45,30 | €-0,00 |
| Scanner Top 5 Long 1H | BOME | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00160 | €218,24 | €436,47 | €52,38 | €0,00 |
| Scanner Top 5 Long 1H | TRUMP | LONG | Scanner Top 5 Long | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,08367 | €238,89 | €477,78 | €55,13 | €0,00 |
| Scanner Top 5 Long 1H | ETH | LONG | Scanner Top 5 Long | 60m | 2,0x | 2502,31036 | 2483,05000 | 2464,79465 | 1263,66673 | 2577,34176 | €1.811,62 | €3.623,23 | €54,32 | €-27,89 |
| Scanner Top 5 Long 1H | SOL | LONG | Scanner Top 5 Long | 60m | 2,0x | 100,22404 | 100,94900 | 97,91287 | 50,61314 | 104,84638 | €1.176,11 | €2.352,22 | €54,24 | €17,01 |
| Scanner Top 5 Long 1H | SKHYNIX | LONG | Scanner Top 5 Long | 60m | 2,0x | 1266,44941 | 1254,35000 | 1233,99401 | 639,55695 | 1331,36020 | €17,74 | €35,49 | €0,91 | €-0,34 |
| Scanner Bottom 5 Short 1H | SOXL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €378,86 | €757,72 | €48,07 | €-0,00 |
| Scanner Bottom 5 Short 1H | SNDK | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €492,80 | €985,60 | €47,71 | €-0,00 |
| Scanner Bottom 5 Short 1H | VELVET | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €191,07 | €382,14 | €0,00 | €-0,00 |
| Scanner Bottom 5 Short 1H | TUT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €178,38 | €356,76 | €42,81 | €-0,00 |
| Scanner Top10 Long | TAO | LONG | Scanner Top10 Long | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €678,43 | €1.356,86 | €51,81 | €0,00 |
| Scanner Top10 Long | ETH | LONG | Scanner Top10 Long | 60m | 2,0x | 2502,31036 | 2483,05000 | 2464,79465 | 1263,66673 | 2577,34176 | €1.685,15 | €3.370,31 | €50,53 | €-25,94 |
| Scanner Top10 Long | SOL | LONG | Scanner Top10 Long | 60m | 2,0x | 100,22404 | 100,94900 | 97,91287 | 50,61314 | 104,84638 | €1.094,01 | €2.188,02 | €50,46 | €15,83 |
| Scanner Top10 Long | SKHYNIX | LONG | Scanner Top10 Long | 60m | 2,0x | 1270,86206 | 1254,35000 | 1239,26059 | 641,78534 | 1334,06500 | €972,86 | €1.945,72 | €48,38 | €-25,28 |
| Scanner Bottom10 Short | SOXL | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom10 Short | SNDK | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Bottom10 Short | VELVET | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €194,19 | €388,38 | €0,00 | €-0,00 |
| Scanner Bottom10 Short | TUT | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €181,31 | €362,61 | €43,51 | €-0,00 |
| Scanner Top15 Long | NEAR | LONG | Scanner Top15 Long | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €16,79 | €33,59 | €1,21 | €0,00 |
| Scanner Top15 Long | TAO | LONG | Scanner Top15 Long | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €88,53 | €177,07 | €6,76 | €0,00 |
| Scanner Top15 Long | TRUMP | LONG | Scanner Top15 Long | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,08367 | €215,87 | €431,75 | €49,81 | €0,00 |
| Scanner Top15 Long | ETH | LONG | Scanner Top15 Long | 60m | 2,0x | 2502,31036 | 2483,05000 | 2464,79465 | 1263,66673 | 2577,34176 | €1.627,80 | €3.255,61 | €48,81 | €-25,06 |
| Scanner Top15 Long | SOL | LONG | Scanner Top15 Long | 60m | 2,0x | 100,22404 | 100,94900 | 97,91287 | 50,61314 | 104,84638 | €1.056,78 | €2.113,56 | €48,74 | €15,29 |
| Scanner Top15 Long | SKHYNIX | LONG | Scanner Top15 Long | 60m | 2,0x | 1270,86206 | 1254,35000 | 1239,26059 | 641,78534 | 1334,06500 | €787,36 | €1.574,72 | €39,16 | €-20,46 |
| Scanner Bottom15 Short | SOXL | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom15 Short | SNDK | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Bottom15 Short | VELVET | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €194,19 | €388,38 | €0,00 | €-0,00 |
| Scanner Bottom15 Short | TUT | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €181,31 | €362,61 | €43,51 | €-0,00 |
| Scanner Top20 Long | NEAR | LONG | Scanner Top20 Long | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €16,79 | €33,59 | €1,21 | €0,00 |
| Scanner Top20 Long | TAO | LONG | Scanner Top20 Long | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €88,53 | €177,07 | €6,76 | €0,00 |
| Scanner Top20 Long | TRUMP | LONG | Scanner Top20 Long | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,08367 | €215,87 | €431,75 | €49,81 | €0,00 |
| Scanner Top20 Long | ETH | LONG | Scanner Top20 Long | 60m | 2,0x | 2502,31036 | 2483,05000 | 2464,79465 | 1263,66673 | 2577,34176 | €1.627,80 | €3.255,61 | €48,81 | €-25,06 |
| Scanner Top20 Long | SOL | LONG | Scanner Top20 Long | 60m | 2,0x | 100,22404 | 100,94900 | 97,91287 | 50,61314 | 104,84638 | €1.056,78 | €2.113,56 | €48,74 | €15,29 |
| Scanner Top20 Long | SKHYNIX | LONG | Scanner Top20 Long | 60m | 2,0x | 1270,86206 | 1254,35000 | 1239,26059 | 641,78534 | 1334,06500 | €787,36 | €1.574,72 | €39,16 | €-20,46 |
| Scanner Bottom20 Short | SOXL | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom20 Short | SNDK | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Bottom20 Short | VELVET | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €194,19 | €388,38 | €0,00 | €-0,00 |
| Scanner Bottom20 Short | TUT | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €181,31 | €362,61 | €43,51 | €-0,00 |
| Scanner Top 5 + forza BTC 1H | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €203,45 | €406,91 | €48,83 | €0,00 |
| Scanner Top 5 + forza BTC 1H | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,14149 | €223,03 | €446,06 | €51,47 | €0,00 |
| Scanner Top 5 + forza BTC 1H | ETH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2502,31036 | 2483,05000 | 2464,79465 | 1263,66673 | 2584,84492 | €1.690,50 | €3.381,00 | €50,69 | €-26,02 |
| Scanner Top 5 + forza BTC 1H | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 100,22404 | 100,94900 | 97,91287 | 50,61314 | 105,30861 | €1.092,06 | €2.184,13 | €50,37 | €15,80 |
| Scanner Top 5 + forza BTC 1H | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1254,35000 | 1233,99401 | 639,55695 | 1337,85129 | €18,23 | €36,45 | €0,93 | €-0,35 |
| Scanner Top5 Btc Mfe V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €190,73 | €381,46 | €45,77 | €0,00 |
| Scanner Top5 Btc Mfe V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,14149 | €209,08 | €418,16 | €48,25 | €0,00 |
| Scanner Top5 Btc Mfe V1 | ETH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2502,31036 | 2483,05000 | 2464,79465 | 1263,66673 | 2584,84492 | €1.584,76 | €3.169,52 | €47,52 | €-24,40 |
| Scanner Top5 Btc Mfe V1 | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 100,22404 | 100,94900 | 97,91287 | 50,61314 | 105,30861 | €1.023,76 | €2.047,51 | €47,22 | €14,81 |
| Scanner Top5 Btc Mfe V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1254,35000 | 1233,99401 | 639,55695 | 1337,85129 | €17,09 | €34,17 | €0,88 | €-0,33 |
| Scanner Top5 Btc Guard V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €197,27 | €394,55 | €47,35 | €0,00 |
| Scanner Top5 Btc Guard V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,55551 | 2,55551 | 2,29388 | 1,29053 | 3,13109 | €13,03 | €26,06 | €2,67 | €0,00 |
| Scanner Top5 Btc Guard V1 | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 100,22404 | 100,94900 | 97,91287 | 50,61314 | 105,30861 | €1.040,01 | €2.080,02 | €47,97 | €15,05 |
| Scanner Top5 Btc Guard V1 | BTR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15358 | 0,17281 | 0,15358 | 0,07756 | 0,19413 | €199,12 | €398,24 | €0,00 | €49,86 |
| Scanner Top5 Btc Btc Le3 V1 | ETH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2502,31036 | 2483,05000 | 2464,79465 | 1263,66673 | 2584,84492 | €1.498,78 | €2.997,56 | €44,94 | €-23,07 |
| Scanner Top5 Btc Btc Le3 V1 | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 100,22404 | 100,94900 | 97,91287 | 50,61314 | 105,30861 | €968,21 | €1.936,42 | €44,65 | €14,01 |
| Scanner Top5 Btc Btc Le3 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1254,35000 | 1233,99401 | 639,55695 | 1337,85129 | €847,75 | €1.695,49 | €43,45 | €-16,20 |
| Scanner Top5 Btc Btc Le3 V1 | BTR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15358 | 0,17281 | 0,15358 | 0,07756 | 0,19413 | €182,51 | €365,03 | €0,00 | €45,70 |
| Scanner Top5 Btc Btc 2 3 V1 | ETH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2502,31036 | 2483,05000 | 2464,79465 | 1263,66673 | 2584,84492 | €1.575,75 | €3.151,50 | €47,25 | €-24,26 |
| Scanner Top5 Btc Btc 2 3 V1 | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 100,22404 | 100,94900 | 97,91287 | 50,61314 | 105,30861 | €1.017,93 | €2.035,86 | €46,95 | €14,73 |
| Scanner Top5 Btc Btc 2 3 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1254,35000 | 1233,99401 | 639,55695 | 1337,85129 | €891,28 | €1.782,56 | €45,68 | €-17,03 |
| Scanner Top5 Btc Btc 2 3 V1 | BTR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15358 | 0,17281 | 0,15358 | 0,07756 | 0,19413 | €191,89 | €383,78 | €0,00 | €48,05 |
| Scanner Top5 Btc Guard Mfe V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €192,69 | €385,37 | €46,24 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,55551 | 2,55551 | 2,29388 | 1,29053 | 3,13109 | €12,72 | €25,45 | €2,61 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 100,22404 | 100,94900 | 97,91287 | 50,61314 | 105,30861 | €1.015,82 | €2.031,64 | €46,85 | €14,70 |
| Scanner Top5 Btc Guard Mfe V1 | BTR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15358 | 0,17281 | 0,15358 | 0,07756 | 0,19413 | €194,49 | €388,97 | €0,00 | €48,70 |
| Scanner Top5 Btc Guard Btc Le3 V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,55551 | 2,55551 | 2,29388 | 1,29053 | 3,13109 | €12,70 | €25,40 | €2,60 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 100,22404 | 100,94900 | 97,91287 | 50,61314 | 105,30861 | €1.007,54 | €2.015,09 | €46,47 | €14,58 |
| Scanner Top5 Btc Guard Btc Le3 V1 | BTR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15358 | 0,17281 | 0,15358 | 0,07756 | 0,19413 | €192,90 | €385,80 | €0,00 | €48,31 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 100,22404 | 100,94900 | 97,91287 | 50,61314 | 105,30861 | €989,99 | €1.979,97 | €45,66 | €14,32 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | BTR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15358 | 0,17281 | 0,15358 | 0,07756 | 0,19413 | €189,54 | €379,08 | €0,00 | €47,46 |
| Scanner Top5 Btc Runner25 V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00176 | €210,95 | €421,90 | €50,63 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | ETH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2502,31036 | 2483,05000 | 2464,79465 | 1263,66673 | 2614,85748 | €1.689,83 | €3.379,66 | €50,67 | €-26,01 |
| Scanner Top5 Btc Runner25 V1 | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 100,22404 | 100,94900 | 97,91287 | 50,61314 | 107,15755 | €1.091,63 | €2.183,26 | €50,35 | €15,79 |
| Scanner Top5 Btc Runner25 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1254,35000 | 1233,99401 | 639,55695 | 1363,81560 | €965,52 | €1.931,04 | €49,49 | €-18,45 |
| Scanner Top5 Btc Tp3 V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00176 | €211,07 | €422,14 | €50,66 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | ETH | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2502,31036 | 2483,05000 | 2464,79465 | 1263,66673 | 2614,85748 | €1.690,82 | €3.381,63 | €50,70 | €-26,03 |
| Scanner Top5 Btc Tp3 V1 | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 100,22404 | 100,94900 | 97,91287 | 50,61314 | 107,15755 | €1.092,27 | €2.184,54 | €50,38 | €15,80 |
| Scanner Top5 Btc Tp3 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1254,35000 | 1233,99401 | 639,55695 | 1363,81560 | €966,09 | €1.932,17 | €49,52 | €-18,46 |
| Combo Trend | BEAT | SHORT | Combo Trend | 60m | 2,0x | 0,25984 | 0,25984 | 0,25657 | 0,38847 | 0,19125 | €193,71 | €387,42 | €0,00 | €-0,00 |
| Combo Trend | ZEC | LONG | Combo Trend | 60m | 2,0x | 807,93155 | 776,09000 | 730,11531 | 408,00543 | 979,12728 | €247,61 | €495,23 | €47,70 | €-19,52 |
| Combo Trend | DOGE | SHORT | Combo Trend | 60m | 2,0x | 0,08663 | 0,08649 | 0,08935 | 0,12952 | 0,08067 | €744,01 | €1.488,02 | €46,59 | €2,45 |
| Combo Trend | ADA | SHORT | Combo Trend | 60m | 2,0x | 0,20238 | 0,20238 | 0,20866 | 0,30256 | 0,18856 | €29,18 | €58,37 | €1,81 | €-0,00 |
| Combo Trend | ETH | LONG | Combo Trend | 60m | 2,0x | 2502,31036 | 2483,05000 | 2460,62625 | 1263,66673 | 2594,01541 | €1.342,29 | €2.684,59 | €44,72 | €-20,66 |
| Combo Scanner | BOME | LONG | Combo Scanner | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €195,20 | €390,40 | €46,85 | €0,00 |
| Combo Scanner | TRUMP | LONG | Combo Scanner | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,14149 | €213,98 | €427,96 | €49,38 | €0,00 |
| Combo Scanner | ETH | LONG | Combo Scanner | 60m | 2,0x | 2502,31036 | 2483,05000 | 2464,79465 | 1263,66673 | 2584,84492 | €1.616,25 | €3.232,50 | €48,46 | €-24,88 |
| Combo Scanner | SOL | LONG | Combo Scanner | 60m | 2,0x | 100,22404 | 100,94900 | 97,91287 | 50,61314 | 105,30861 | €1.049,28 | €2.098,56 | €48,39 | €15,18 |
| Combo Scanner | SKHYNIX | LONG | Combo Scanner | 60m | 2,0x | 1266,44941 | 1254,35000 | 1233,99401 | 639,55695 | 1337,85129 | €24,78 | €49,55 | €1,27 | €-0,47 |
| Combo Adaptive | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,01735 | 121,01735 | 128,90956 | 180,92093 | 105,23292 | €367,30 | €734,61 | €47,91 | €-0,00 |
| Combo Adaptive | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €40,89 | €81,77 | €3,12 | €0,00 |
| Combo Adaptive | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 807,93155 | 776,09000 | 737,89694 | 408,00543 | 948,00078 | €307,94 | €615,88 | €53,39 | €-24,27 |
| Combo Adaptive | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,52450 | 2,33981 | 1,27487 | 2,89389 | €18,69 | €37,37 | €2,73 | €0,00 |
| Combo Adaptive | ADA | SHORT | Combo Adaptive | 60m | 2,0x | 0,20238 | 0,20238 | 0,20803 | 0,30256 | 0,19107 | €40,31 | €80,63 | €2,25 | €-0,00 |
| Combo Adaptive | ETH | LONG | Combo Adaptive | 60m | 2,0x | 2493,43859 | 2483,05000 | 2455,39522 | 1259,18649 | 2569,52529 | €1.704,48 | €3.408,96 | €52,01 | €-14,20 |
| Combo Adaptive | SOL | LONG | Combo Adaptive | 60m | 2,0x | 101,73634 | 100,94900 | 99,19447 | 51,37685 | 106,82009 | €1.020,15 | €2.040,31 | €50,98 | €-15,79 |
| Combo Adaptive Mfe Trail | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €54,29 | €108,58 | €4,15 | €0,00 |
| Combo Adaptive Mfe Trail | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,52450 | 2,33981 | 1,27487 | 2,89389 | €315,75 | €631,50 | €46,20 | €0,00 |
| Combo Adaptive Mfe Trail | TUT | SHORT | Combo Adaptive | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €190,04 | €380,09 | €45,61 | €-0,00 |
| Combo Adaptive Mfe Trail | ADA | SHORT | Combo Adaptive | 60m | 2,0x | 0,20238 | 0,20238 | 0,20803 | 0,30256 | 0,19107 | €40,65 | €81,31 | €2,27 | €-0,00 |
| Combo Adaptive Mfe Trail | ETH | LONG | Combo Adaptive | 60m | 2,0x | 2493,43859 | 2483,05000 | 2455,39522 | 1259,18649 | 2569,52529 | €1.465,62 | €2.931,24 | €44,72 | €-12,21 |
| Combo Adaptive Mfe Trail | SOL | LONG | Combo Adaptive | 60m | 2,0x | 101,73634 | 100,94900 | 99,19447 | 51,37685 | 106,82009 | €784,07 | €1.568,13 | €39,18 | €-12,14 |
| Combo Adaptive Quality7 V1 | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €371,68 | €743,36 | €47,16 | €-0,00 |
| Combo Adaptive Quality7 V1 | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €646,78 | €1.293,57 | €49,39 | €0,00 |
| Combo Adaptive Quality7 V1 | ADA | SHORT | Combo Adaptive | 60m | 2,0x | 0,20238 | 0,20238 | 0,20803 | 0,30256 | 0,19107 | €876,38 | €1.752,76 | €48,96 | €-0,00 |
| Combo Adaptive Regime V1 | ETH | LONG | Combo Adaptive | 60m | 2,0x | 2502,31036 | 2483,05000 | 2464,79465 | 1263,66673 | 2577,34176 | €1.636,31 | €3.272,61 | €49,06 | €-25,19 |
| Combo Adaptive Regime V1 | SOL | LONG | Combo Adaptive | 60m | 2,0x | 101,16923 | 100,94900 | 98,67777 | 51,09046 | 106,15214 | €996,83 | €1.993,65 | €49,10 | €-4,34 |
| Combo Adaptive Regime V1 | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1270,86206 | 1254,35000 | 1239,26059 | 641,78534 | 1334,06500 | €987,06 | €1.974,12 | €49,09 | €-25,65 |
| Combo Adaptive Regime V1 | BTR | LONG | Combo Adaptive | 60m | 2,0x | 0,15358 | 0,17281 | 0,15358 | 0,07756 | 0,19044 | €203,07 | €406,14 | €0,00 | €50,85 |
| Combo Adaptive Long Only V1 | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €645,48 | €1.290,95 | €46,47 | €0,00 |
| Combo Adaptive Long Only V1 | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,52450 | 2,33981 | 1,27487 | 2,89389 | €48,12 | €96,24 | €7,04 | €0,00 |
| Combo Adaptive Long Only V1 | ETH | LONG | Combo Adaptive | 60m | 2,0x | 2502,31036 | 2483,05000 | 2464,79465 | 1263,66673 | 2577,34176 | €1.728,09 | €3.456,18 | €51,82 | €-26,60 |
| Combo Adaptive Long Only V1 | SOL | LONG | Combo Adaptive | 60m | 2,0x | 100,22404 | 100,94900 | 97,91287 | 50,61314 | 104,84638 | €1.121,89 | €2.243,77 | €51,74 | €16,23 |
| Combo Adaptive Long Only V1 | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1266,44941 | 1254,35000 | 1233,99401 | 639,55695 | 1331,36020 | €968,99 | €1.937,97 | €49,66 | €-18,52 |
| Combo Adaptive Partial 1R V1 | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,01735 | 121,01735 | 128,90956 | 180,92093 | 105,23292 | €352,70 | €705,40 | €46,00 | €-0,00 |
| Combo Adaptive Partial 1R V1 | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,52450 | 2,33981 | 1,27487 | 2,89389 | €347,19 | €694,38 | €50,80 | €0,00 |
| Combo Adaptive Partial 1R V1 | VELVET | SHORT | Combo Adaptive | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €207,76 | €415,52 | €0,00 | €-0,00 |
| Combo Adaptive Partial 1R V1 | ADA | SHORT | Combo Adaptive | 60m | 2,0x | 0,20989 | 0,20989 | 0,20688 | 0,31379 | 0,19734 | €18,50 | €37,00 | €0,00 | €-0,00 |
| Combo Adaptive Partial 1R V1 | ETH | LONG | Combo Adaptive | 60m | 2,0x | 2502,31036 | 2483,05000 | 2464,79465 | 1263,66673 | 2577,34176 | €27,02 | €54,03 | €0,81 | €-0,42 |
| Combo Adaptive Partial 1R V1 | SOL | LONG | Combo Adaptive | 60m | 2,0x | 100,22404 | 100,94900 | 97,91287 | 50,61314 | 104,84638 | €47,32 | €94,64 | €2,18 | €0,68 |
| Combo Adaptive Partial 1R V1 | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1270,86206 | 1254,35000 | 1239,26059 | 641,78534 | 1334,06500 | €1.013,20 | €2.026,40 | €50,39 | €-26,33 |
| Btc Ema 4H | BTC | LONG | Trend following EMA | 240m | 2,0x | 80355,23783 | 78648,03000 | 77497,66656 | 40579,39511 | 87499,16561 | €704,37 | €1.408,74 | €50,10 | €-29,93 |
| Btc Donchian 4H | BTC | LONG | Donchian breakout 20 barre | 240m | 2,0x | 80355,23783 | 78648,03000 | 77497,66656 | 40579,39511 | 88356,43707 | €700,60 | €1.401,20 | €49,83 | €-29,77 |
| Btc Bollinger 4H | BTC | SHORT | Bollinger mean reversion | 240m | 2,0x | 80323,10217 | 78648,03000 | 82919,85488 | 120083,03774 | 75648,94663 | €775,58 | €1.551,16 | €50,15 | €32,35 |
| Btc Adaptive 4H | BTC | LONG | Combo Adaptive | 240m | 2,0x | 80355,23783 | 78648,03000 | 77237,88772 | 40579,39511 | 88148,61352 | €648,94 | €1.297,88 | €50,35 | €-27,57 |
| Sol Ema 1H | SOL | LONG | Trend following EMA | 60m | 3,0x | 100,22404 | 100,94900 | 97,91287 | 67,31715 | 104,84638 | €728,87 | €2.186,61 | €50,42 | €15,82 |
| Sol Ema 4H | SOL | LONG | Trend following EMA | 240m | 2,0x | 98,32066 | 100,94900 | 92,06715 | 49,65193 | 113,95442 | €395,27 | €790,53 | €50,28 | €21,13 |
| Sol Donchian 1H | SOL | LONG | Donchian breakout 20 barre | 60m | 3,0x | 100,22404 | 100,94900 | 100,46539 | 67,31715 | 104,33279 | €828,76 | €2.486,27 | €0,00 | €17,98 |
| Sol Bollinger 1H | SOL | SHORT | Bollinger mean reversion | 60m | 3,0x | 101,62867 | 100,94900 | 103,71338 | 134,99675 | 98,50161 | €797,97 | €2.393,90 | €49,11 | €16,01 |
| Sol Bollinger 4H | SOL | SHORT | Bollinger mean reversion | 240m | 2,0x | 100,13097 | 100,94900 | 105,86849 | 149,69580 | 89,80342 | €435,50 | €871,00 | €49,91 | €-7,12 |
| Sol Adaptive 1H | SOL | LONG | Combo Adaptive | 60m | 3,0x | 100,22404 | 100,94900 | 97,91287 | 67,31715 | 104,84638 | €718,50 | €2.155,51 | €49,71 | €15,59 |
| Sol Adaptive 4H | SOL | LONG | Combo Adaptive | 240m | 2,0x | 98,32066 | 100,94900 | 91,49865 | 49,65193 | 115,37567 | €367,30 | €734,59 | €50,97 | €19,64 |
| Eth Ema 1H | ETH | LONG | Trend following EMA | 60m | 3,0x | 2493,43859 | 2483,05000 | 2455,39522 | 1674,75958 | 2569,52529 | €1.072,00 | €3.216,01 | €49,07 | €-13,40 |
| Eth Ema 4H | ETH | LONG | Trend following EMA | 240m | 2,0x | 2390,02791 | 2483,05000 | 2268,60778 | 1206,96409 | 2693,57826 | €487,73 | €975,47 | €49,56 | €37,97 |
| Eth Donchian 1H | ETH | LONG | Donchian breakout 20 barre | 60m | 3,0x | 2502,31036 | 2483,05000 | 2468,96307 | 1680,71846 | 2569,00494 | €1.210,37 | €3.631,11 | €48,39 | €-27,95 |
| Eth Adaptive 1H | ETH | LONG | Combo Adaptive | 60m | 3,0x | 2502,31036 | 2483,05000 | 2464,79465 | 1680,71846 | 2577,34176 | €1.094,40 | €3.283,20 | €49,22 | €-25,27 |
| Master Adaptive V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 80,35907 | 80,67500 | 78,17754 | 40,58133 | 84,72212 | €858,86 | €1.717,73 | €46,63 | €6,75 |
| Master Adaptive V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 2502,31036 | 2483,05000 | 2464,79465 | 1263,66673 | 2577,34181 | €1.560,29 | €3.120,58 | €46,79 | €-24,02 |
| Master Adaptive V1 | SOL | LONG | Master Adaptive Consensus | 60m | 2,0x | 100,68813 | 100,94900 | 98,15309 | 50,84751 | 105,75823 | €912,62 | €1.825,23 | €45,95 | €4,73 |
| Master Adaptive V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1254,35000 | 1233,99403 | 639,55695 | 1331,36019 | €22,75 | €45,50 | €1,17 | €-0,43 |
| Master Adaptive V1 | BTR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,17284 | 0,17281 | 0,15210 | 0,08729 | 0,21433 | €195,60 | €391,20 | €46,94 | €-0,08 |
| Master Adaptive No Alt V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 80,35907 | 80,67500 | 78,17754 | 40,58133 | 84,72212 | €861,47 | €1.722,94 | €46,77 | €6,77 |
| Master Adaptive No Alt V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 2502,31036 | 2483,05000 | 2464,79465 | 1263,66673 | 2577,34181 | €1.565,03 | €3.130,05 | €46,93 | €-24,09 |
| Master Adaptive No Alt V1 | BTR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,14959 | 0,17281 | 0,13164 | 0,07554 | 0,18549 | €195,68 | €391,35 | €46,96 | €60,75 |
| Master Adaptive No Alt V1 | SOL | LONG | Master Adaptive Consensus | 60m | 2,0x | 101,16923 | 100,94900 | 98,67777 | 51,09046 | 106,15214 | €953,46 | €1.906,91 | €46,96 | €-4,15 |
| Master Adaptive No Alt V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1255,10261 | 1254,35000 | 1225,12158 | 633,82682 | 1315,06467 | €19,09 | €38,19 | €0,91 | €-0,02 |
| Master Adaptive Strict3 V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 2502,31036 | 2483,05000 | 2464,79465 | 1263,66673 | 2577,34181 | €1.493,28 | €2.986,56 | €44,78 | €-22,99 |
| Master Adaptive Strict3 V1 | SOL | LONG | Master Adaptive Consensus | 60m | 2,0x | 101,16923 | 100,94900 | 98,67777 | 51,09046 | 106,15214 | €903,35 | €1.806,70 | €44,49 | €-3,93 |
| Master Adaptive Expanded V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03814 | 0,02188 | 0,05374 | €197,50 | €395,01 | €47,40 | €0,00 |
| Master Adaptive Expanded V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 80,35907 | 80,67500 | 78,17754 | 40,58133 | 84,72212 | €861,38 | €1.722,77 | €46,77 | €6,77 |
| Master Adaptive Expanded V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 2502,31036 | 2483,05000 | 2464,79465 | 1263,66673 | 2577,34181 | €1.572,67 | €3.145,34 | €47,16 | €-24,21 |
| Master Adaptive Expanded V1 | SOL | LONG | Master Adaptive Consensus | 60m | 2,0x | 101,73634 | 100,94900 | 99,19447 | 51,37685 | 106,82009 | €15,99 | €31,99 | €0,80 | €-0,25 |
| Master Adaptive Expanded V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1261,89668 | 1254,35000 | 1231,08309 | 637,25783 | 1323,52387 | €934,21 | €1.868,43 | €45,62 | €-11,17 |
| Master Adaptive Gb20 V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 80,35907 | 80,67500 | 78,17754 | 40,58133 | 84,72212 | €847,45 | €1.694,91 | €46,01 | €6,66 |
| Master Adaptive Gb20 V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 2502,31036 | 2483,05000 | 2464,79465 | 1263,66673 | 2577,34181 | €1.539,56 | €3.079,12 | €46,16 | €-23,70 |
| Master Adaptive Gb20 V1 | SOL | LONG | Master Adaptive Consensus | 60m | 2,0x | 100,68813 | 100,94900 | 98,15309 | 50,84751 | 105,75823 | €900,49 | €1.800,98 | €45,34 | €4,67 |
| Master Adaptive Gb20 V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1254,35000 | 1233,99403 | 639,55695 | 1331,36019 | €22,45 | €44,90 | €1,15 | €-0,43 |
| Master Adaptive Gb20 V1 | BTR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,17284 | 0,17281 | 0,15210 | 0,08729 | 0,21433 | €193,00 | €386,00 | €46,32 | €-0,08 |
| Master Adaptive Runner25 V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03814 | 0,02188 | 0,05894 | €34,77 | €69,54 | €8,34 | €0,00 |
| Master Adaptive Runner25 V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 80,35907 | 80,67500 | 78,17754 | 40,58133 | 86,90364 | €864,19 | €1.728,38 | €46,92 | €6,80 |
| Master Adaptive Runner25 V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 2502,31036 | 2483,05000 | 2464,79465 | 1263,66673 | 2614,85753 | €1.568,97 | €3.137,94 | €47,05 | €-24,15 |
| Master Adaptive Runner25 V1 | SOL | LONG | Master Adaptive Consensus | 60m | 2,0x | 98,42868 | 100,94900 | 96,44960 | 49,70648 | 104,36592 | €964,43 | €1.928,85 | €38,78 | €49,39 |
| Master Adaptive Runner25 V1 | BTR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,13218 | 0,17281 | 0,11632 | 0,06675 | 0,17976 | €196,14 | €392,29 | €47,07 | €120,60 |
| Master Adaptive Runner25 V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1255,10261 | 1254,35000 | 1225,12158 | 633,82682 | 1345,04570 | €27,05 | €54,10 | €1,29 | €-0,03 |
| Combo Adaptive Side Regime Guard V1 | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €77,52 | €155,04 | €5,58 | €0,00 |
| Combo Adaptive Side Regime Guard V1 | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 807,93155 | 776,09000 | 737,89694 | 408,00543 | 948,00078 | €305,89 | €611,78 | €53,03 | €-24,11 |
| Combo Adaptive Side Regime Guard V1 | VELVET | SHORT | Combo Adaptive | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €216,61 | €433,23 | €0,00 | €-0,00 |
| Combo Adaptive Side Regime Guard V1 | TUT | SHORT | Combo Adaptive | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €192,40 | €384,79 | €46,18 | €-0,00 |
| Combo Adaptive Side Regime Guard V1 | ETH | LONG | Combo Adaptive | 60m | 2,0x | 2502,31036 | 2483,05000 | 2464,79465 | 1263,66673 | 2577,34176 | €1.697,78 | €3.395,56 | €50,91 | €-26,14 |
| Master Adaptive Gb20 Be V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 80,35907 | 80,67500 | 78,17754 | 40,58133 | 84,72212 | €863,12 | €1.726,23 | €46,86 | €6,79 |
| Master Adaptive Gb20 Be V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 2502,31036 | 2483,05000 | 2464,79465 | 1263,66673 | 2577,34181 | €1.568,02 | €3.136,03 | €47,02 | €-24,14 |
| Master Adaptive Gb20 Be V1 | SOL | LONG | Master Adaptive Consensus | 60m | 2,0x | 100,68813 | 100,94900 | 98,15309 | 50,84751 | 105,75823 | €917,13 | €1.834,27 | €46,18 | €4,75 |
| Master Adaptive Gb20 Be V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1254,35000 | 1233,99403 | 639,55695 | 1331,36019 | €22,86 | €45,73 | €1,17 | €-0,44 |
| Master Adaptive Gb20 Be V1 | BTR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,17284 | 0,17281 | 0,15210 | 0,08729 | 0,21433 | €196,57 | €393,14 | €47,18 | €-0,08 |
| Master Adaptive Gb20 Partial V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 80,35907 | 80,67500 | 78,17754 | 40,58133 | 84,72212 | €862,20 | €1.724,40 | €46,81 | €6,78 |
| Master Adaptive Gb20 Partial V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 2502,31036 | 2483,05000 | 2464,79465 | 1263,66673 | 2577,34181 | €1.566,35 | €3.132,70 | €46,97 | €-24,11 |
| Master Adaptive Gb20 Partial V1 | SOL | LONG | Master Adaptive Consensus | 60m | 2,0x | 100,68813 | 100,94900 | 98,15309 | 50,84751 | 105,75823 | €916,16 | €1.832,32 | €46,13 | €4,75 |
| Master Adaptive Gb20 Partial V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1254,35000 | 1233,99403 | 639,55695 | 1331,36019 | €22,84 | €45,68 | €1,17 | €-0,44 |
| Master Adaptive Gb20 Partial V1 | BTR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,17284 | 0,17281 | 0,15210 | 0,08729 | 0,21433 | €196,36 | €392,72 | €47,13 | €-0,08 |
| Master Adaptive Gb20 Loss Cap V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03828 | 0,02188 | 0,05682 | €195,70 | €391,41 | €45,67 | €0,00 |
| Master Adaptive Gb20 Loss Cap V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 2502,31036 | 2483,05000 | 2474,17356 | 1263,66673 | 2577,34181 | €1.829,31 | €3.658,61 | €41,14 | €-28,16 |
| Master Adaptive Gb20 Loss Cap V1 | SOL | LONG | Master Adaptive Consensus | 60m | 2,0x | 100,68813 | 100,94900 | 98,78685 | 50,84751 | 105,75823 | €1.211,09 | €2.422,17 | €45,74 | €6,28 |
| Master Adaptive Gb20 Loss Cap V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1254,35000 | 1242,10788 | 639,55695 | 1331,36019 | €140,55 | €281,10 | €5,40 | €-2,69 |
| 1H Fast V3 Nohigh Regime Guard V1 | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €140,84 | €422,53 | €50,70 | €-0,00 |
| 1H Fast V3 Nohigh Regime Guard V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €143,15 | €429,46 | €50,70 | €-0,00 |
| 1H Fast V3 Nohigh Regime Guard V1 | ETH | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2502,31036 | 2483,05000 | 2473,13147 | 1680,71846 | 2546,07867 | €1.442,59 | €4.327,77 | €50,47 | €-33,31 |
| 1H Fast V3 Nohigh Regime Guard V1 | SOL | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 100,22404 | 100,94900 | 100,46539 | 67,31715 | 102,92041 | €952,40 | €2.857,19 | €0,00 | €20,67 |
| Main Side Regime Guard V1 | VELVET | LONG | Confluenza trend | 240m | 3,0x | 0,55987 | 0,55987 | 0,49269 | 0,37605 | 0,69424 | €142,25 | €426,74 | €51,21 | €0,00 |
| Main Side Regime Guard V1 | AKE | LONG | Confluenza trend | 240m | 3,0x | 0,01021 | 0,01021 | 0,00899 | 0,00686 | 0,01266 | €145,97 | €437,90 | €52,55 | €0,00 |
| Main Side Regime Guard V1 | HYPE | LONG | Confluenza trend | 240m | 3,0x | 77,65853 | 80,67500 | 71,20755 | 52,16065 | 90,56048 | €216,52 | €649,56 | €53,96 | €25,23 |
| Main Side Regime Guard V1 | XRP | LONG | Confluenza trend | 240m | 3,0x | 1,47102 | 1,39828 | 1,31178 | 0,98804 | 1,78951 | €12,77 | €38,31 | €4,15 | €-1,89 |
| Main Side Regime Guard V1 | ETH | LONG | Confluenza trend | 240m | 3,0x | 2437,91749 | 2483,05000 | 2326,72117 | 1637,46791 | 2660,31012 | €9,94 | €29,83 | €1,36 | €0,55 |
| Main Side Regime Guard V1 | BTR | LONG | Confluenza trend | 240m | 3,0x | 0,15358 | 0,17281 | 0,15358 | 0,10316 | 0,19044 | €144,94 | €434,83 | €0,00 | €54,44 |
| Combo Trend Side Regime Guard V1 | VELVET | SHORT | Combo Trend | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,12693 | €217,86 | €435,73 | €0,00 | €-0,00 |
| Combo Trend Side Regime Guard V1 | TUT | SHORT | Combo Trend | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03364 | €12,81 | €25,62 | €3,07 | €-0,00 |
| Combo Trend Side Regime Guard V1 | DOGE | SHORT | Combo Trend | 60m | 2,0x | 0,08663 | 0,08649 | 0,08935 | 0,12952 | 0,08067 | €881,95 | €1.763,89 | €55,22 | €2,90 |
| Combo Trend Side Regime Guard V1 | ETH | LONG | Combo Trend | 60m | 2,0x | 2502,31036 | 2483,05000 | 2460,62625 | 1263,66673 | 2594,01541 | €1.662,43 | €3.324,85 | €55,39 | €-25,59 |
| Combo Trend Side Regime Guard V1 | SOL | LONG | Combo Trend | 60m | 2,0x | 100,22404 | 100,94900 | 97,65607 | 50,61314 | 105,87357 | €1.052,06 | €2.104,12 | €53,91 | €15,22 |
| 1H Fast Nohigh Cap75 Short Only V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €135,82 | €407,46 | €48,90 | €-0,00 |
| 1H Fast Nohigh Cap75 Short Only V1 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €138,05 | €414,14 | €48,89 | €-0,00 |
| 1H Fast Nohigh Cap75 Short Only V1 | ADA | SHORT | Momentum / breakout | 60m | 3,0x | 0,20481 | 0,20481 | 0,20925 | 0,27205 | 0,19815 | €51,88 | €155,65 | €3,37 | €-0,00 |
| 1H Fast Nohigh Cap75 Short Only V1 | ETH | LONG | Momentum / breakout | 60m | 3,0x | 2502,31036 | 2483,05000 | 2473,13147 | 1680,71846 | 2546,07867 | €1.431,92 | €4.295,75 | €50,09 | €-33,06 |
| 1H Fast Nohigh Cap75 Short Only V1 | SOL | LONG | Momentum / breakout | 60m | 3,0x | 100,22404 | 100,94900 | 100,46539 | 67,31715 | 102,92041 | €12,39 | €37,17 | €0,00 | €0,27 |
| 1H Fast Nohigh Cap75 Short Only V1 | HYPE | LONG | Momentum / breakout | 60m | 3,0x | 82,02040 | 80,67500 | 80,13051 | 55,09037 | 84,85524 | €8,53 | €25,60 | €0,59 | €-0,42 |
| 1H Fast Nohigh Cap75 Short Only V1 | SKHYNIX | LONG | Momentum / breakout | 60m | 3,0x | 1266,44941 | 1254,35000 | 1241,20633 | 850,63186 | 1304,31405 | €10,83 | €32,48 | €0,65 | €-0,31 |
| 1H Fast Nohigh Cap75 Short Only V1 | BTR | LONG | Momentum / breakout | 60m | 3,0x | 0,17284 | 0,17281 | 0,15210 | 0,11609 | 0,20396 | €130,00 | €390,01 | €46,80 | €-0,08 |
| 1H Balanced V3 Long Only V1 | SKHYNIX | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1220,85412 | 1254,35000 | 1177,63561 | 820,00702 | 1307,29117 | €435,49 | €1.306,46 | €46,25 | €35,84 |
| 1H Balanced V3 Long Only V1 | ZEC | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 807,93155 | 776,09000 | 737,89694 | 542,66069 | 948,00078 | €184,72 | €554,15 | €48,04 | €-21,84 |
| 1H Balanced V3 Long Only V1 | XRP | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1,47399 | 1,39828 | 1,35380 | 0,99003 | 1,71438 | €194,69 | €584,07 | €47,63 | €-30,00 |
| 1H Balanced V3 Long Only V1 | DOGE | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,08603 | 0,08649 | 0,08841 | 0,11428 | 0,08128 | €18,32 | €54,97 | €1,52 | €-0,29 |
| 1H Balanced V3 Long Only V1 | ETH | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 2502,31036 | 2483,05000 | 2464,79465 | 1680,71846 | 2577,34176 | €17,97 | €53,92 | €0,81 | €-0,42 |
| 1H Balanced V3 Long Only V1 | SOL | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 100,22404 | 100,94900 | 97,91287 | 67,31715 | 104,84638 | €654,36 | €1.963,07 | €45,27 | €14,20 |
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
| Master Adaptive Gb20 Loss Cap V1 | BTR | LONG | 2026-08-27T04:45:00+00:00 | 0,17444 | €122,19 | 2,65 | TARGET |
| Master Adaptive V1 | BTR | LONG | 2026-08-27T03:15:00+00:00 | 0,16387 | €93,29 | 1,99 | TARGET |
| Master Adaptive Gb20 V1 | BTR | LONG | 2026-08-27T03:15:00+00:00 | 0,16387 | €92,05 | 1,99 | TARGET |
| Master Adaptive Gb20 Partial V1 | BTR | LONG | 2026-08-27T03:15:00+00:00 | 0,16387 | €93,65 | 1,99 | TARGET |
| Master Adaptive Gb20 Be V1 | BTR | LONG | 2026-08-27T03:15:00+00:00 | 0,16387 | €93,75 | 1,99 | TARGET |
| Master Adaptive Expanded V1 | BTR | LONG | 2026-08-27T03:15:00+00:00 | 0,16292 | €89,05 | 1,99 | TARGET |
| 1H Fast V3 No Esports Long Only V1 | BTR | LONG | 2026-08-27T03:15:00+00:00 | 0,15504 | €71,31 | 1,49 | TARGET |
| 1H Fast V3 Long Nohigh Cap75 V1 | BTR | LONG | 2026-08-27T03:15:00+00:00 | 0,15504 | €70,53 | 1,49 | TARGET |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | BTR | LONG | 2026-08-27T03:15:00+00:00 | 0,15504 | €69,21 | 1,49 | TARGET |
| 1H Fast No Pepe V1 | BTR | LONG | 2026-08-27T03:15:00+00:00 | 0,15504 | €74,21 | 1,49 | TARGET |
| 1H Fast Nohigh Cap75 V1 | BTR | LONG | 2026-08-27T03:15:00+00:00 | 0,15504 | €70,71 | 1,49 | TARGET |
| 1H Fast Nohigh Cap75 Short Only V1 | BTR | LONG | 2026-08-27T03:15:00+00:00 | 0,15504 | €68,96 | 1,49 | TARGET |

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

Generato: 2026-08-27 05:33 UTC


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

Segnali totali salvati: **144**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08-27 | BTC | 78.624,75 | +7 | +3 | +3 | 0 | +3 | +1 | 0 | ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA |
| 2026-08-27 | DOGE | 0.08623 | -1 | -1 | -1 | 0 | +1 | 0 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-08-27 | SOL | 100,81 | +7 | +2 | +2 | 0 | +3 | +1 | 0 | HOLD / ACCUMULO A TRANCHE, NO LEVA AGGRESSIVA |
| 2026-08-26 | BTC | 79.104,96 | +8 | +3 | +3 | 0 | +3 | +1 | 0 | ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA |
| 2026-08-26 | DOGE | 0.08675 | +1 | 0 | 0 | 0 | +2 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-08-26 | SOL | 96,96 | +6 | +1 | +1 | 0 | +3 | +1 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-08-25 | BTC | 80.778,18 | +6 | +2 | +2 | 0 | +3 | +1 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-08-25 | DOGE | 0.09299 | +5 | +1 | +1 | 0 | +3 | +1 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-08-25 | SOL | 102,40 | +6 | +1 | +1 | 0 | +3 | +1 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-08-24 | BTC | 76.958,14 | +6 | +2 | +2 | 0 | +3 | +1 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-08-24 | DOGE | 0.09174 | +4 | +1 | +1 | 0 | +3 | +1 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-08-24 | SOL | 93,82 | +6 | +1 | +1 | 0 | +3 | +1 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 48 | 47 | 46 | 45 | 43 | 41 | 38 | 34 | 29 | 20 | 5 | 0 |
| SOL | 48 | 47 | 46 | 45 | 43 | 41 | 38 | 34 | 29 | 20 | 5 | 0 |
| DOGE | 48 | 47 | 46 | 45 | 43 | 41 | 38 | 34 | 29 | 20 | 5 | 0 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-07-14 | 45g | 2026-08-28 | domani |
| SOL | 2026-07-14 | 45g | 2026-08-28 | domani |
| DOGE | 2026-07-14 | 45g | 2026-08-28 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 44 | 52,27% | +0,52% | +0,49% | PRIMA CALIBRAZIONE |
| BTC | 2g | 43 | 53,49% | +0,93% | +0,82% | PRIMA CALIBRAZIONE |
| BTC | 3g | 42 | 52,38% | +1,25% | +1,09% | PRIMA CALIBRAZIONE |
| BTC | 5g | 40 | 42,50% | +2,34% | +2,03% | PRIMA CALIBRAZIONE |
| BTC | 7g | 38 | 50,00% | +3,15% | +2,87% | PRIMA CALIBRAZIONE |
| BTC | 10g | 36 | 50,00% | +3,62% | +3,37% | PRIMA CALIBRAZIONE |
| BTC | 14g | 32 | 56,25% | +3,32% | +3,21% | PRIMA CALIBRAZIONE |
| BTC | 21g | 27 | 48,15% | +5,61% | +5,37% | FEEDBACK RAPIDO |
| BTC | 30g | 18 | 83,33% | +7,23% | +4,83% | FEEDBACK RAPIDO |
| BTC | 45g | 5 | 100,00% | +23,30% | +23,30% | FEEDBACK RAPIDO |
| BTC | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 1g | 40 | 57,50% | +0,77% | +0,61% | PRIMA CALIBRAZIONE |
| SOL | 2g | 39 | 53,85% | +1,46% | +1,28% | PRIMA CALIBRAZIONE |
| SOL | 3g | 38 | 57,89% | +2,45% | +2,21% | PRIMA CALIBRAZIONE |
| SOL | 5g | 36 | 61,11% | +3,79% | +3,64% | PRIMA CALIBRAZIONE |
| SOL | 7g | 34 | 64,71% | +4,99% | +5,14% | PRIMA CALIBRAZIONE |
| SOL | 10g | 31 | 64,52% | +4,89% | +5,14% | PRIMA CALIBRAZIONE |
| SOL | 14g | 27 | 70,37% | +4,48% | +5,83% | FEEDBACK RAPIDO |
| SOL | 21g | 22 | 63,64% | +6,83% | +5,21% | FEEDBACK RAPIDO |
| SOL | 30g | 15 | 46,67% | +4,92% | +2,85% | FEEDBACK RAPIDO |
| SOL | 45g | 4 | 50,00% | +27,42% | -1,97% | FEEDBACK RAPIDO |
| SOL | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 1g | 45 | 48,89% | +0,48% | +0,47% | PRIMA CALIBRAZIONE |
| DOGE | 2g | 44 | 50,00% | +0,98% | +0,97% | PRIMA CALIBRAZIONE |
| DOGE | 3g | 43 | 48,84% | +1,60% | +1,86% | PRIMA CALIBRAZIONE |
| DOGE | 5g | 41 | 58,54% | +2,97% | +3,58% | PRIMA CALIBRAZIONE |
| DOGE | 7g | 39 | 66,67% | +3,96% | +5,10% | PRIMA CALIBRAZIONE |
| DOGE | 10g | 36 | 61,11% | +2,74% | +4,46% | PRIMA CALIBRAZIONE |
| DOGE | 14g | 32 | 65,62% | +2,98% | +5,88% | PRIMA CALIBRAZIONE |
| DOGE | 21g | 27 | 70,37% | +3,89% | +2,42% | FEEDBACK RAPIDO |
| DOGE | 30g | 19 | 73,68% | +5,52% | -0,26% | FEEDBACK RAPIDO |
| DOGE | 45g | 5 | 0,00% | +22,50% | -22,50% | FEEDBACK RAPIDO |
| DOGE | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 44 | 52,27% | +0,52% | +0,49% | +0,07% | +1,10% | PRIMA CALIBRAZIONE |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 47 | 55,32% | +0,48% | +0,48% | +0,05% | +1,04% | PRIMA CALIBRAZIONE |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 47 | 55,32% | +0,48% | +0,48% | +0,05% | +1,04% | PRIMA CALIBRAZIONE |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,25% | +0,25% | -0,10% | +0,70% | PRIMA CALIBRAZIONE |
| BTC | 1g | Tecnico | CALIBRABILE | 42 | 38,10% | +0,65% | +0,16% | +0,19% | +1,22% | PRIMA CALIBRAZIONE |
| BTC | 1g | Classic technical | CALIBRABILE | 15 | 33,33% | +1,20% | +0,50% | +0,41% | +1,77% | FEEDBACK RAPIDO |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +0,27% | +0,27% | -0,26% | +0,74% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 43 | 53,49% | +0,93% | +0,82% | +0,36% | +1,65% | PRIMA CALIBRAZIONE |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 46 | 56,52% | +1,04% | +1,04% | +0,47% | +1,74% | PRIMA CALIBRAZIONE |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 46 | 56,52% | +1,04% | +1,04% | +0,47% | +1,74% | PRIMA CALIBRAZIONE |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,52% | +0,52% | -0,02% | +1,18% | PRIMA CALIBRAZIONE |
| BTC | 2g | Tecnico | CALIBRABILE | 41 | 43,90% | +1,29% | +0,28% | +0,72% | +2,00% | PRIMA CALIBRAZIONE |
| BTC | 2g | Classic technical | CALIBRABILE | 14 | 35,71% | +1,85% | +0,76% | +1,32% | +2,61% | FEEDBACK RAPIDO |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +2,14% | +2,14% | +1,22% | +2,65% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 42 | 52,38% | +1,25% | +1,09% | -0,75% | +2,94% | PRIMA CALIBRAZIONE |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 45 | 62,22% | +1,61% | +1,61% | -0,74% | +3,20% | PRIMA CALIBRAZIONE |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 45 | 62,22% | +1,61% | +1,61% | -0,74% | +3,20% | PRIMA CALIBRAZIONE |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 35 | 57,14% | +0,91% | +0,91% | -1,00% | +2,36% | PRIMA CALIBRAZIONE |
| BTC | 3g | Tecnico | CALIBRABILE | 40 | 40,00% | +2,05% | -0,05% | -0,48% | +3,61% | PRIMA CALIBRAZIONE |
| BTC | 3g | Classic technical | CALIBRABILE | 13 | 46,15% | +3,23% | +0,27% | +0,36% | +4,67% | FEEDBACK RAPIDO |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +2,79% | +2,79% | +0,99% | +4,54% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 40 | 42,50% | +2,34% | +2,03% | -1,42% | +4,38% | PRIMA CALIBRAZIONE |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 43 | 51,16% | +2,63% | +2,63% | -1,39% | +4,75% | PRIMA CALIBRAZIONE |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 43 | 51,16% | +2,63% | +2,63% | -1,39% | +4,75% | PRIMA CALIBRAZIONE |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 35 | 48,57% | +2,08% | +2,08% | -1,57% | +4,07% | PRIMA CALIBRAZIONE |
| BTC | 5g | Tecnico | CALIBRABILE | 38 | 39,47% | +3,12% | -1,34% | -1,13% | +5,28% | PRIMA CALIBRAZIONE |
| BTC | 5g | Classic technical | CALIBRABILE | 11 | 36,36% | +7,41% | -3,15% | -0,12% | +8,91% | FEEDBACK RAPIDO |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,16% | -0,16% | -0,37% | +4,24% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 38 | 50,00% | +3,15% | +2,87% | -1,69% | +5,61% | PRIMA CALIBRAZIONE |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 41 | 58,54% | +3,53% | +3,53% | -1,67% | +5,97% | PRIMA CALIBRAZIONE |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 41 | 58,54% | +3,53% | +3,53% | -1,67% | +5,97% | PRIMA CALIBRAZIONE |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 35 | 60,00% | +3,17% | +3,17% | -1,80% | +5,49% | PRIMA CALIBRAZIONE |
| BTC | 7g | Tecnico | CALIBRABILE | 36 | 33,33% | +4,33% | -2,75% | -1,37% | +6,65% | PRIMA CALIBRAZIONE |
| BTC | 7g | Classic technical | CALIBRABILE | 9 | 11,11% | +11,68% | -8,79% | -0,04% | +14,00% | FEEDBACK RAPIDO |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,77% | +1,77% | -0,79% | +4,24% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 36 | 50,00% | +3,62% | +3,37% | -2,38% | +6,08% | PRIMA CALIBRAZIONE |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 38 | 55,26% | +3,30% | +3,30% | -2,41% | +5,90% | PRIMA CALIBRAZIONE |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 38 | 55,26% | +3,30% | +3,30% | -2,41% | +5,90% | PRIMA CALIBRAZIONE |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 34 | 61,76% | +3,94% | +3,94% | -2,29% | +6,32% | PRIMA CALIBRAZIONE |
| BTC | 10g | Tecnico | CALIBRABILE | 33 | 30,30% | +3,98% | -2,61% | -2,14% | +6,61% | PRIMA CALIBRAZIONE |
| BTC | 10g | Classic technical | CALIBRABILE | 8 | 0,00% | +13,19% | -13,19% | -0,77% | +15,42% | FEEDBACK RAPIDO |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,43% | -0,43% | -2,30% | +4,24% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 32 | 56,25% | +3,32% | +3,21% | -2,89% | +6,39% | PRIMA CALIBRAZIONE |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 34 | 55,88% | +3,03% | +3,03% | -2,91% | +6,17% | PRIMA CALIBRAZIONE |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 34 | 55,88% | +3,03% | +3,03% | -2,91% | +6,17% | PRIMA CALIBRAZIONE |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 30 | 63,33% | +3,77% | +3,77% | -2,71% | +6,68% | PRIMA CALIBRAZIONE |
| BTC | 14g | Tecnico | CALIBRABILE | 29 | 65,52% | +3,77% | +3,72% | -2,64% | +6,95% | FEEDBACK RAPIDO |
| BTC | 14g | Classic technical | CALIBRABILE | 4 | 50,00% | +0,27% | -0,27% | -1,55% | +3,37% | FEEDBACK RAPIDO |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -2,25% | -2,25% | -3,05% | +4,24% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 27 | 48,15% | +5,61% | +5,37% | -2,91% | +9,15% | FEEDBACK RAPIDO |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 29 | 58,62% | +5,15% | +5,15% | -2,97% | +8,70% | FEEDBACK RAPIDO |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 29 | 58,62% | +5,15% | +5,15% | -2,97% | +8,70% | FEEDBACK RAPIDO |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 25 | 64,00% | +6,19% | +6,19% | -2,72% | +9,71% | FEEDBACK RAPIDO |
| BTC | 21g | Tecnico | CALIBRABILE | 24 | 25,00% | +5,89% | -2,19% | -2,65% | +9,50% | FEEDBACK RAPIDO |
| BTC | 21g | Classic technical | CALIBRABILE | 4 | 0,00% | +11,68% | -11,68% | -1,55% | +14,27% | FEEDBACK RAPIDO |
| BTC | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,21% | +1,21% | -3,06% | +4,24% | FEEDBACK RAPIDO |
| BTC | 30g | Global confluence | BENCHMARK | 18 | 83,33% | +7,23% | +4,83% | -3,23% | +10,88% | FEEDBACK RAPIDO |
| BTC | 30g | Famiglia statistica | CALIBRABILE | 20 | 75,00% | +7,31% | +7,31% | -3,27% | +11,11% | FEEDBACK RAPIDO |
| BTC | 30g | Scanner grezzo | DIAGNOSTICO | 20 | 75,00% | +7,31% | +7,31% | -3,27% | +11,11% | FEEDBACK RAPIDO |
| BTC | 30g | Market regime grezzo | DIAGNOSTICO | 16 | 75,00% | +7,96% | +7,96% | -2,97% | +12,12% | FEEDBACK RAPIDO |
| BTC | 30g | Tecnico | CALIBRABILE | 16 | 37,50% | +6,51% | -3,66% | -2,90% | +10,90% | FEEDBACK RAPIDO |
| BTC | 30g | Classic technical | CALIBRABILE | 1 | 0,00% | +24,05% | -24,05% | -1,82% | +28,17% | FEEDBACK RAPIDO |
| BTC | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +0,16% | +0,16% | -3,06% | +4,24% | FEEDBACK RAPIDO |
| BTC | 45g | Global confluence | BENCHMARK | 5 | 100,00% | +23,30% | +23,30% | -2,65% | +26,27% | FEEDBACK RAPIDO |
| BTC | 45g | Famiglia statistica | CALIBRABILE | 5 | 100,00% | +23,30% | +23,30% | -2,65% | +26,27% | FEEDBACK RAPIDO |
| BTC | 45g | Scanner grezzo | DIAGNOSTICO | 5 | 100,00% | +23,30% | +23,30% | -2,65% | +26,27% | FEEDBACK RAPIDO |
| BTC | 45g | Market regime grezzo | DIAGNOSTICO | 5 | 100,00% | +23,30% | +23,30% | -2,65% | +26,27% | FEEDBACK RAPIDO |
| BTC | 45g | Tecnico | CALIBRABILE | 4 | 50,00% | +24,00% | +0,62% | -2,49% | +26,73% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 45 | 48,89% | +0,48% | +0,47% | -0,12% | +1,52% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 46 | 58,70% | +0,39% | +0,66% | -0,22% | +1,39% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 46 | 58,70% | +0,39% | +0,66% | -0,22% | +1,39% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,15% | +0,26% | -0,32% | +0,87% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Tecnico | CALIBRABILE | 40 | 55,00% | +0,28% | +0,50% | -0,35% | +1,27% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Classic technical | CALIBRABILE | 31 | 41,94% | +0,27% | -0,51% | -0,38% | +0,97% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 71,43% | +2,86% | +2,41% | +1,15% | +3,54% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 44 | 50,00% | +0,98% | +0,97% | +0,23% | +2,33% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 46 | 52,17% | +0,84% | +1,04% | +0,11% | +2,15% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 46 | 52,17% | +0,84% | +1,04% | +0,11% | +2,15% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 38 | 50,00% | +0,36% | +0,74% | -0,26% | +1,41% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Tecnico | CALIBRABILE | 39 | 61,54% | +0,33% | +0,81% | -0,35% | +1,60% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Classic technical | CALIBRABILE | 31 | 45,16% | +0,67% | -1,20% | -0,10% | +1,65% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 57,14% | +4,25% | +3,88% | +3,39% | +6,58% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 43 | 48,84% | +1,60% | +1,86% | -1,25% | +4,51% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 45 | 53,33% | +1,43% | +1,71% | -1,35% | +4,27% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 45 | 53,33% | +1,43% | +1,71% | -1,35% | +4,27% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,84% | +1,55% | -1,48% | +3,36% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Tecnico | CALIBRABILE | 38 | 50,00% | +0,44% | +0,88% | -1,64% | +3,07% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Classic technical | CALIBRABILE | 30 | 33,33% | +1,54% | -2,01% | -1,63% | +4,45% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 57,14% | +3,59% | +3,29% | -0,23% | +7,51% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 41 | 58,54% | +2,97% | +3,58% | -1,82% | +7,00% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 43 | 55,81% | +2,74% | +3,33% | -1,90% | +6,67% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 43 | 55,81% | +2,74% | +3,33% | -1,90% | +6,67% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +2,45% | +3,08% | -2,17% | +5,74% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Tecnico | CALIBRABILE | 36 | 63,89% | +1,57% | +1,21% | -2,30% | +5,35% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Classic technical | CALIBRABILE | 28 | 42,86% | +3,42% | -3,74% | -2,10% | +7,38% | FEEDBACK RAPIDO |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 6 | 50,00% | +3,80% | +3,53% | +0,14% | +10,26% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 39 | 66,67% | +3,96% | +5,10% | -2,18% | +8,85% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 41 | 63,41% | +3,66% | +4,70% | -2,29% | +8,46% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 41 | 63,41% | +3,66% | +4,70% | -2,29% | +8,46% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,59% | +4,60% | -2,54% | +8,00% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Tecnico | CALIBRABILE | 34 | 64,71% | +2,16% | +2,20% | -2,79% | +6,62% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Classic technical | CALIBRABILE | 27 | 44,44% | +4,34% | -4,34% | -2,39% | +9,14% | FEEDBACK RAPIDO |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +3,64% | +3,43% | +1,17% | +11,40% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 36 | 61,11% | +2,74% | +4,46% | -3,20% | +7,92% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 38 | 60,53% | +2,50% | +4,16% | -3,27% | +7,55% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 38 | 60,53% | +2,50% | +4,16% | -3,27% | +7,55% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 36 | 61,11% | +2,68% | +4,34% | -3,25% | +7,72% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Tecnico | CALIBRABILE | 33 | 66,67% | +1,15% | +2,31% | -3,59% | +6,29% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Classic technical | CALIBRABILE | 25 | 52,00% | +2,20% | -2,20% | -3,31% | +7,77% | FEEDBACK RAPIDO |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 75,00% | +0,93% | +0,18% | -1,31% | +5,72% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 32 | 65,62% | +2,98% | +5,88% | -4,04% | +8,39% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 34 | 70,59% | +2,68% | +5,43% | -4,07% | +7,96% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 34 | 70,59% | +2,68% | +5,43% | -4,07% | +7,96% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 32 | 71,88% | +2,94% | +5,67% | -4,09% | +8,18% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Tecnico | CALIBRABILE | 30 | 66,67% | -0,31% | +0,31% | -4,43% | +4,70% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Classic technical | CALIBRABILE | 22 | 63,64% | +0,33% | -0,33% | -4,43% | +5,27% | FEEDBACK RAPIDO |
| DOGE | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 75,00% | +12,47% | +2,65% | -1,31% | +16,91% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 27 | 70,37% | +3,89% | +2,42% | -4,88% | +10,61% | FEEDBACK RAPIDO |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 29 | 82,76% | +4,32% | +8,40% | -4,86% | +11,36% | FEEDBACK RAPIDO |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 29 | 82,76% | +4,32% | +8,40% | -4,86% | +11,36% | FEEDBACK RAPIDO |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 27 | 85,19% | +4,73% | +8,93% | -4,94% | +11,86% | FEEDBACK RAPIDO |
| DOGE | 21g | Tecnico | CALIBRABILE | 28 | 67,86% | +3,64% | -3,64% | -4,97% | +10,23% | FEEDBACK RAPIDO |
| DOGE | 21g | Classic technical | CALIBRABILE | 20 | 75,00% | +0,03% | -0,03% | -5,18% | +6,01% | FEEDBACK RAPIDO |
| DOGE | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +0,76% | +0,76% | -1,85% | +6,57% | FEEDBACK RAPIDO |
| DOGE | 30g | Global confluence | BENCHMARK | 19 | 73,68% | +5,52% | -0,26% | -5,95% | +12,86% | FEEDBACK RAPIDO |
| DOGE | 30g | Famiglia statistica | CALIBRABILE | 20 | 80,00% | +6,19% | +3,90% | -5,99% | +14,08% | FEEDBACK RAPIDO |
| DOGE | 30g | Scanner grezzo | DIAGNOSTICO | 20 | 80,00% | +6,19% | +3,90% | -5,99% | +14,08% | FEEDBACK RAPIDO |
| DOGE | 30g | Market regime grezzo | DIAGNOSTICO | 18 | 88,89% | +3,77% | +7,44% | -6,24% | +11,50% | FEEDBACK RAPIDO |
| DOGE | 30g | Tecnico | CALIBRABILE | 20 | 60,00% | +6,19% | -6,19% | -5,99% | +14,08% | FEEDBACK RAPIDO |
| DOGE | 30g | Classic technical | CALIBRABILE | 17 | 64,71% | +4,96% | -4,96% | -5,74% | +12,22% | FEEDBACK RAPIDO |
| DOGE | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +31,53% | +31,53% | -1,85% | +40,20% | FEEDBACK RAPIDO |
| DOGE | 45g | Global confluence | BENCHMARK | 5 | 0,00% | +22,50% | -22,50% | -7,07% | +35,10% | FEEDBACK RAPIDO |
| DOGE | 45g | Famiglia statistica | CALIBRABILE | 5 | 0,00% | +22,50% | -22,50% | -7,07% | +35,10% | FEEDBACK RAPIDO |
| DOGE | 45g | Scanner grezzo | DIAGNOSTICO | 5 | 0,00% | +22,50% | -22,50% | -7,07% | +35,10% | FEEDBACK RAPIDO |
| DOGE | 45g | Market regime grezzo | DIAGNOSTICO | 5 | 0,00% | +22,50% | -22,50% | -7,07% | +35,10% | FEEDBACK RAPIDO |
| DOGE | 45g | Tecnico | CALIBRABILE | 5 | 0,00% | +22,50% | -22,50% | -7,07% | +35,10% | FEEDBACK RAPIDO |
| DOGE | 45g | Classic technical | CALIBRABILE | 5 | 0,00% | +22,50% | -22,50% | -7,07% | +35,10% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 40 | 57,50% | +0,77% | +0,61% | +0,11% | +1,72% | PRIMA CALIBRAZIONE |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 42 | 59,52% | +0,38% | +0,37% | -0,19% | +1,30% | PRIMA CALIBRAZIONE |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 45 | 57,78% | +0,43% | +0,27% | -0,15% | +1,34% | PRIMA CALIBRAZIONE |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +0,27% | +0,39% | -0,30% | +0,87% | PRIMA CALIBRAZIONE |
| SOL | 1g | Tecnico | CALIBRABILE | 44 | 52,27% | +0,38% | +0,35% | -0,24% | +1,25% | PRIMA CALIBRAZIONE |
| SOL | 1g | Classic technical | CALIBRABILE | 28 | 53,57% | +0,67% | +0,61% | -0,10% | +1,68% | FEEDBACK RAPIDO |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 39 | 53,85% | +1,46% | +1,28% | +0,66% | +2,60% | PRIMA CALIBRAZIONE |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 41 | 48,78% | +0,96% | +0,37% | +0,14% | +1,76% | PRIMA CALIBRAZIONE |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 44 | 47,73% | +0,92% | +0,32% | +0,13% | +1,83% | PRIMA CALIBRAZIONE |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +0,76% | +0,78% | -0,00% | +1,60% | PRIMA CALIBRAZIONE |
| SOL | 2g | Tecnico | CALIBRABILE | 43 | 44,19% | +0,83% | +0,12% | +0,09% | +1,97% | PRIMA CALIBRAZIONE |
| SOL | 2g | Classic technical | CALIBRABILE | 27 | 55,56% | +0,99% | +0,95% | +0,30% | +1,99% | FEEDBACK RAPIDO |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 25,00% | +0,16% | +0,16% | -0,21% | +2,10% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 38 | 57,89% | +2,45% | +2,21% | -0,99% | +4,58% | PRIMA CALIBRAZIONE |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 40 | 47,50% | +1,77% | +1,04% | -1,41% | +3,91% | PRIMA CALIBRAZIONE |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 43 | 46,51% | +1,67% | +0,94% | -1,39% | +3,88% | PRIMA CALIBRAZIONE |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +1,43% | +1,38% | -1,48% | +3,53% | PRIMA CALIBRAZIONE |
| SOL | 3g | Tecnico | CALIBRABILE | 42 | 47,62% | +1,49% | -0,08% | -1,49% | +3,54% | PRIMA CALIBRAZIONE |
| SOL | 3g | Classic technical | CALIBRABILE | 26 | 53,85% | +1,48% | +1,27% | -1,31% | +3,48% | FEEDBACK RAPIDO |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 33,33% | +0,33% | +0,33% | -1,17% | +5,20% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 36 | 61,11% | +3,79% | +3,64% | -1,68% | +6,78% | PRIMA CALIBRAZIONE |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 38 | 55,26% | +2,86% | +2,20% | -2,11% | +5,86% | PRIMA CALIBRAZIONE |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 41 | 53,66% | +2,70% | +1,98% | -2,10% | +5,72% | PRIMA CALIBRAZIONE |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +2,66% | +2,88% | -2,09% | +5,82% | PRIMA CALIBRAZIONE |
| SOL | 5g | Tecnico | CALIBRABILE | 40 | 45,00% | +2,70% | -1,28% | -2,30% | +5,57% | PRIMA CALIBRAZIONE |
| SOL | 5g | Classic technical | CALIBRABILE | 24 | 58,33% | +1,65% | +1,41% | -2,13% | +4,13% | FEEDBACK RAPIDO |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 33,33% | +1,18% | +1,18% | -1,95% | +5,20% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 34 | 64,71% | +4,99% | +5,14% | -2,15% | +8,40% | PRIMA CALIBRAZIONE |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 36 | 66,67% | +3,90% | +4,53% | -2,60% | +7,40% | PRIMA CALIBRAZIONE |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 39 | 66,67% | +3,59% | +4,19% | -2,61% | +7,13% | PRIMA CALIBRAZIONE |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 34 | 61,76% | +4,35% | +4,41% | -2,45% | +7,76% | PRIMA CALIBRAZIONE |
| SOL | 7g | Tecnico | CALIBRABILE | 38 | 34,21% | +3,52% | -3,07% | -2,83% | +7,03% | PRIMA CALIBRAZIONE |
| SOL | 7g | Classic technical | CALIBRABILE | 22 | 45,45% | +0,81% | +0,89% | -2,87% | +3,95% | FEEDBACK RAPIDO |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 0,00% | -3,55% | -3,55% | -4,19% | +1,03% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 31 | 64,52% | +4,89% | +5,14% | -3,14% | +8,44% | PRIMA CALIBRAZIONE |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 34 | 67,65% | +4,36% | +5,00% | -3,47% | +7,74% | PRIMA CALIBRAZIONE |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 37 | 64,86% | +3,99% | +4,61% | -3,47% | +7,43% | PRIMA CALIBRAZIONE |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 32 | 62,50% | +4,96% | +4,79% | -3,31% | +8,14% | PRIMA CALIBRAZIONE |
| SOL | 10g | Tecnico | CALIBRABILE | 36 | 41,67% | +3,47% | -3,60% | -3,58% | +7,17% | PRIMA CALIBRAZIONE |
| SOL | 10g | Classic technical | CALIBRABILE | 21 | 52,38% | -0,08% | +0,08% | -3,74% | +3,68% | FEEDBACK RAPIDO |
| SOL | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 50,00% | -2,05% | -2,05% | -4,86% | +1,05% | FEEDBACK RAPIDO |
| SOL | 10g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 14g | Global confluence | BENCHMARK | 27 | 70,37% | +4,48% | +5,83% | -3,95% | +9,24% | FEEDBACK RAPIDO |
| SOL | 14g | Famiglia statistica | CALIBRABILE | 30 | 83,33% | +4,50% | +5,75% | -4,13% | +8,56% | PRIMA CALIBRAZIONE |
| SOL | 14g | Scanner grezzo | DIAGNOSTICO | 33 | 84,85% | +3,81% | +5,51% | -4,11% | +8,14% | PRIMA CALIBRAZIONE |
| SOL | 14g | Market regime grezzo | DIAGNOSTICO | 28 | 67,86% | +5,06% | +5,18% | -3,82% | +9,08% | FEEDBACK RAPIDO |
| SOL | 14g | Tecnico | CALIBRABILE | 32 | 34,38% | +2,00% | -2,63% | -4,32% | +6,56% | PRIMA CALIBRAZIONE |
| SOL | 14g | Classic technical | CALIBRABILE | 21 | 38,10% | +1,19% | -1,19% | -4,25% | +5,07% | FEEDBACK RAPIDO |
| SOL | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 50,00% | +8,38% | +8,38% | -5,94% | +13,89% | FEEDBACK RAPIDO |
| SOL | 14g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 21g | Global confluence | BENCHMARK | 22 | 63,64% | +6,83% | +5,21% | -5,57% | +12,24% | FEEDBACK RAPIDO |
| SOL | 21g | Famiglia statistica | CALIBRABILE | 25 | 80,00% | +7,87% | +10,11% | -5,38% | +12,48% | FEEDBACK RAPIDO |
| SOL | 21g | Scanner grezzo | DIAGNOSTICO | 28 | 82,14% | +6,74% | +9,32% | -5,45% | +11,56% | FEEDBACK RAPIDO |
| SOL | 21g | Market regime grezzo | DIAGNOSTICO | 23 | 60,87% | +8,79% | +9,53% | -5,08% | +13,45% | FEEDBACK RAPIDO |
| SOL | 21g | Tecnico | CALIBRABILE | 29 | 41,38% | +6,53% | -7,95% | -5,51% | +11,28% | FEEDBACK RAPIDO |
| SOL | 21g | Classic technical | CALIBRABILE | 20 | 40,00% | +9,40% | -9,40% | -4,94% | +13,51% | FEEDBACK RAPIDO |
| SOL | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -3,18% | -3,18% | -9,62% | +0,62% | FEEDBACK RAPIDO |

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

Generato: 2026-08-27 05:33 UTC

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
| BTC | 48 | PRIMA CALIBRAZIONE | 47 | 13 | 0 | 0 | Famiglia statistica | 1g | 55,32% | +0,48% | prima calibrazione possibile, solo modifiche leggere |
| SOL | 48 | PRIMA CALIBRAZIONE | 44 | 14 | 0 | 0 | Tecnico | 1g | 52,27% | +0,35% | prima calibrazione possibile, solo modifiche leggere |
| DOGE | 48 | PRIMA CALIBRAZIONE | 46 | 17 | 0 | 0 | Famiglia statistica | 1g | 58,70% | +0,66% | prima calibrazione possibile, solo modifiche leggere |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Classic technical | 15 | 33,33% | +0,50% | +1,20% | +0,41% | +1,77% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Famiglia statistica | 47 | 55,32% | +0,48% | +0,48% | +0,05% | +1,04% | PESO OK | 0,0 | MEDIA |
| BTC | 1g | BREVE | Microstruttura exchange | 3 | 66,67% | +0,27% | +0,27% | -0,26% | +0,74% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 42 | 38,10% | +0,16% | +0,65% | +0,19% | +1,22% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 2g | BREVE | Classic technical | 14 | 35,71% | +0,76% | +1,85% | +1,32% | +2,61% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Famiglia statistica | 46 | 56,52% | +1,04% | +1,04% | +0,47% | +1,74% | PESO OK | 0,0 | MEDIA |
| BTC | 2g | BREVE | Microstruttura exchange | 3 | 66,67% | +2,14% | +2,14% | +1,22% | +2,65% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 41 | 43,90% | +0,28% | +1,29% | +0,72% | +2,00% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 3g | BREVE | Classic technical | 13 | 46,15% | +0,27% | +3,23% | +0,36% | +4,67% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Famiglia statistica | 45 | 62,22% | +1,61% | +1,61% | -0,74% | +3,20% | PESO OK | 0,0 | MEDIA |
| BTC | 3g | BREVE | Microstruttura exchange | 2 | 100,00% | +2,79% | +2,79% | +0,99% | +4,54% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 40 | 40,00% | -0,05% | +2,05% | -0,48% | +3,61% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 5g | SETTIMANALE | Classic technical | 11 | 36,36% | -3,15% | +7,41% | -0,12% | +8,91% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 43 | 51,16% | +2,63% | +2,63% | -1,39% | +4,75% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 5g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -0,16% | -0,16% | -0,37% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 38 | 39,47% | -1,34% | +3,12% | -1,13% | +5,28% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 7g | SETTIMANALE | Classic technical | 9 | 11,11% | -8,79% | +11,68% | -0,04% | +14,00% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 41 | 58,54% | +3,53% | +3,53% | -1,67% | +5,97% | PESO OK | 0,0 | MEDIA |
| BTC | 7g | SETTIMANALE | Microstruttura exchange | 1 | 100,00% | +1,77% | +1,77% | -0,79% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 36 | 33,33% | -2,75% | +4,33% | -1,37% | +6,65% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 10g | SETTIMANALE | Classic technical | 8 | 0,00% | -13,19% | +13,19% | -0,77% | +15,42% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 38 | 55,26% | +3,30% | +3,30% | -2,41% | +5,90% | PESO OK | 0,0 | MEDIA |
| BTC | 10g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -0,43% | -0,43% | -2,30% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 33 | 30,30% | -2,61% | +3,98% | -2,14% | +6,61% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 14g | SWING | Classic technical | 4 | 50,00% | -0,27% | +0,27% | -1,55% | +3,37% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Famiglia statistica | 34 | 55,88% | +3,03% | +3,03% | -2,91% | +6,17% | PESO OK | 0,0 | MEDIA |
| BTC | 14g | SWING | Microstruttura exchange | 1 | 0,00% | -2,25% | -2,25% | -3,05% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 29 | 65,52% | +3,72% | +3,77% | -2,64% | +6,95% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Classic technical | 4 | 0,00% | -11,68% | +11,68% | -1,55% | +14,27% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Famiglia statistica | 29 | 58,62% | +5,15% | +5,15% | -2,97% | +8,70% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Microstruttura exchange | 1 | 100,00% | +1,21% | +1,21% | -3,06% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Tecnico | 24 | 25,00% | -2,19% | +5,89% | -2,65% | +9,50% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Classic technical | 1 | 0,00% | -24,05% | +24,05% | -1,82% | +28,17% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Famiglia statistica | 20 | 75,00% | +7,31% | +7,31% | -3,27% | +11,11% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Microstruttura exchange | 1 | 100,00% | +0,16% | +0,16% | -3,06% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Tecnico | 16 | 37,50% | -3,66% | +6,51% | -2,90% | +10,90% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Famiglia statistica | 5 | 100,00% | +23,30% | +23,30% | -2,65% | +26,27% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Tecnico | 4 | 50,00% | +0,62% | +24,00% | -2,49% | +26,73% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 31 | 41,94% | -0,51% | +0,27% | -0,38% | +0,97% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 1g | BREVE | Famiglia statistica | 46 | 58,70% | +0,66% | +0,39% | -0,22% | +1,39% | PESO OK | 0,0 | MEDIA |
| DOGE | 1g | BREVE | Microstruttura exchange | 7 | 71,43% | +2,41% | +2,86% | +1,15% | +3,54% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 40 | 55,00% | +0,50% | +0,28% | -0,35% | +1,27% | PESO OK | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Classic technical | 31 | 45,16% | -1,20% | +0,67% | -0,10% | +1,65% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Famiglia statistica | 46 | 52,17% | +1,04% | +0,84% | +0,11% | +2,15% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Microstruttura exchange | 7 | 57,14% | +3,88% | +4,25% | +3,39% | +6,58% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 39 | 61,54% | +0,81% | +0,33% | -0,35% | +1,60% | PESO OK | 0,0 | MEDIA |
| DOGE | 3g | BREVE | Classic technical | 30 | 33,33% | -2,01% | +1,54% | -1,63% | +4,45% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 3g | BREVE | Famiglia statistica | 45 | 53,33% | +1,71% | +1,43% | -1,35% | +4,27% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 3g | BREVE | Microstruttura exchange | 7 | 57,14% | +3,29% | +3,59% | -0,23% | +7,51% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 38 | 50,00% | +0,88% | +0,44% | -1,64% | +3,07% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 5g | SETTIMANALE | Classic technical | 28 | 42,86% | -3,74% | +3,42% | -2,10% | +7,38% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 43 | 55,81% | +3,33% | +2,74% | -1,90% | +6,67% | PESO OK | 0,0 | MEDIA |
| DOGE | 5g | SETTIMANALE | Microstruttura exchange | 6 | 50,00% | +3,53% | +3,80% | +0,14% | +10,26% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 36 | 63,89% | +1,21% | +1,57% | -2,30% | +5,35% | PESO OK | 0,0 | MEDIA |
| DOGE | 7g | SETTIMANALE | Classic technical | 27 | 44,44% | -4,34% | +4,34% | -2,39% | +9,14% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 41 | 63,41% | +4,70% | +3,66% | -2,29% | +8,46% | PESO OK | 0,0 | MEDIA |
| DOGE | 7g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +3,43% | +3,64% | +1,17% | +11,40% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 34 | 64,71% | +2,20% | +2,16% | -2,79% | +6,62% | PESO OK | 0,0 | MEDIA |
| DOGE | 10g | SETTIMANALE | Classic technical | 25 | 52,00% | -2,20% | +2,20% | -3,31% | +7,77% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 38 | 60,53% | +4,16% | +2,50% | -3,27% | +7,55% | PESO OK | 0,0 | MEDIA |
| DOGE | 10g | SETTIMANALE | Microstruttura exchange | 4 | 75,00% | +0,18% | +0,93% | -1,31% | +5,72% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 33 | 66,67% | +2,31% | +1,15% | -3,59% | +6,29% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 14g | SWING | Classic technical | 22 | 63,64% | -0,33% | +0,33% | -4,43% | +5,27% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Famiglia statistica | 34 | 70,59% | +5,43% | +2,68% | -4,07% | +7,96% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 14g | SWING | Microstruttura exchange | 4 | 75,00% | +2,65% | +12,47% | -1,31% | +16,91% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 30 | 66,67% | +0,31% | -0,31% | -4,43% | +4,70% | PESO OK | 0,0 | MEDIA |
| DOGE | 21g | SWING | Classic technical | 20 | 75,00% | -0,03% | +0,03% | -5,18% | +6,01% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Famiglia statistica | 29 | 82,76% | +8,40% | +4,32% | -4,86% | +11,36% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Microstruttura exchange | 2 | 100,00% | +0,76% | +0,76% | -1,85% | +6,57% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Tecnico | 28 | 67,86% | -3,64% | +3,64% | -4,97% | +10,23% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Classic technical | 17 | 64,71% | -4,96% | +4,96% | -5,74% | +12,22% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Famiglia statistica | 20 | 80,00% | +3,90% | +6,19% | -5,99% | +14,08% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Microstruttura exchange | 2 | 100,00% | +31,53% | +31,53% | -1,85% | +40,20% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Tecnico | 20 | 60,00% | -6,19% | +6,19% | -5,99% | +14,08% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Classic technical | 5 | 0,00% | -22,50% | +22,50% | -7,07% | +35,10% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Famiglia statistica | 5 | 0,00% | -22,50% | +22,50% | -7,07% | +35,10% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Tecnico | 5 | 0,00% | -22,50% | +22,50% | -7,07% | +35,10% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Classic technical | 28 | 53,57% | +0,61% | +0,67% | -0,10% | +1,68% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Famiglia statistica | 42 | 59,52% | +0,37% | +0,38% | -0,19% | +1,30% | PESO OK | 0,0 | MEDIA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 44 | 52,27% | +0,35% | +0,38% | -0,24% | +1,25% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Classic technical | 27 | 55,56% | +0,95% | +0,99% | +0,30% | +1,99% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Famiglia statistica | 41 | 48,78% | +0,37% | +0,96% | +0,14% | +1,76% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Microstruttura exchange | 4 | 25,00% | +0,16% | +0,16% | -0,21% | +2,10% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 43 | 44,19% | +0,12% | +0,83% | +0,09% | +1,97% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Classic technical | 26 | 53,85% | +1,27% | +1,48% | -1,31% | +3,48% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Famiglia statistica | 40 | 47,50% | +1,04% | +1,77% | -1,41% | +3,91% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Microstruttura exchange | 3 | 33,33% | +0,33% | +0,33% | -1,17% | +5,20% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 42 | 47,62% | -0,08% | +1,49% | -1,49% | +3,54% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Classic technical | 24 | 58,33% | +1,41% | +1,65% | -2,13% | +4,13% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 38 | 55,26% | +2,20% | +2,86% | -2,11% | +5,86% | PESO OK | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Microstruttura exchange | 3 | 33,33% | +1,18% | +1,18% | -1,95% | +5,20% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 40 | 45,00% | -1,28% | +2,70% | -2,30% | +5,57% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Classic technical | 22 | 45,45% | +0,89% | +0,81% | -2,87% | +3,95% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 36 | 66,67% | +4,53% | +3,90% | -2,60% | +7,40% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Microstruttura exchange | 2 | 0,00% | -3,55% | -3,55% | -4,19% | +1,03% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 38 | 34,21% | -3,07% | +3,52% | -2,83% | +7,03% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 10g | SETTIMANALE | Classic technical | 21 | 52,38% | +0,08% | -0,08% | -3,74% | +3,68% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 34 | 67,65% | +5,00% | +4,36% | -3,47% | +7,74% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Microstruttura exchange | 2 | 50,00% | -2,05% | -2,05% | -4,86% | +1,05% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 36 | 41,67% | -3,60% | +3,47% | -3,58% | +7,17% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 14g | SWING | Classic technical | 21 | 38,10% | -1,19% | +1,19% | -4,25% | +5,07% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Famiglia statistica | 30 | 83,33% | +5,75% | +4,50% | -4,13% | +8,56% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 14g | SWING | Frattale SOL | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Microstruttura exchange | 2 | 50,00% | +8,38% | +8,38% | -5,94% | +13,89% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Tecnico | 32 | 34,38% | -2,63% | +2,00% | -4,32% | +6,56% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 21g | SWING | Classic technical | 20 | 40,00% | -9,40% | +9,40% | -4,94% | +13,51% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Famiglia statistica | 25 | 80,00% | +10,11% | +7,87% | -5,38% | +12,48% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Frattale SOL | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Microstruttura exchange | 1 | 0,00% | -3,18% | -3,18% | -9,62% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Tecnico | 29 | 41,38% | -7,95% | +6,53% | -5,51% | +11,28% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Classic technical | 12 | 16,67% | -15,60% | +15,60% | -6,52% | +20,16% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Famiglia statistica | 16 | 81,25% | +10,73% | +11,39% | -7,34% | +15,88% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Frattale SOL | 1 | 0,00% | -4,50% | -4,50% | -9,39% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Microstruttura exchange | 1 | 100,00% | +8,54% | +8,54% | -9,62% | +9,47% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Tecnico | 20 | 20,00% | -10,14% | +9,21% | -7,24% | +13,47% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Famiglia statistica | 4 | 0,00% | -24,70% | +24,70% | -8,35% | +30,51% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Frattale SOL | 1 | 100,00% | +19,26% | +19,26% | -9,39% | +23,73% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Tecnico | 5 | 80,00% | +13,28% | +26,08% | -8,51% | +30,69% | OSSERVA | 0,0 | BASSA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 45 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 38 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 47 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Classic technical | 42 | 38,10% | +0,52% |
| BTC | BREVE | Famiglia statistica | 138 | 57,97% | +1,03% |
| BTC | BREVE | Microstruttura exchange | 8 | 75,00% | +1,60% |
| BTC | BREVE | Tecnico | 123 | 40,65% | +0,13% |
| BTC | SETTIMANALE | Classic technical | 28 | 17,86% | -7,83% |
| BTC | SETTIMANALE | Famiglia statistica | 122 | 54,92% | +3,14% |
| BTC | SETTIMANALE | Microstruttura exchange | 3 | 33,33% | +0,39% |
| BTC | SETTIMANALE | Tecnico | 107 | 34,58% | -2,20% |
| BTC | SWING | Classic technical | 8 | 25,00% | -5,98% |
| BTC | SWING | Famiglia statistica | 63 | 57,14% | +4,01% |
| BTC | SWING | Microstruttura exchange | 2 | 50,00% | -0,52% |
| BTC | SWING | Tecnico | 53 | 47,17% | +1,04% |
| BTC | MEDIO | Classic technical | 1 | 0,00% | -24,05% |
| BTC | MEDIO | Famiglia statistica | 25 | 80,00% | +10,51% |
| BTC | MEDIO | Microstruttura exchange | 1 | 100,00% | +0,16% |
| BTC | MEDIO | Tecnico | 20 | 40,00% | -2,80% |
| DOGE | BREVE | Classic technical | 92 | 40,22% | -1,23% |
| DOGE | BREVE | Famiglia statistica | 137 | 54,74% | +1,13% |
| DOGE | BREVE | Microstruttura exchange | 21 | 61,90% | +3,19% |
| DOGE | BREVE | Tecnico | 117 | 55,56% | +0,73% |
| DOGE | SETTIMANALE | Classic technical | 80 | 46,25% | -3,46% |
| DOGE | SETTIMANALE | Famiglia statistica | 122 | 59,84% | +4,05% |
| DOGE | SETTIMANALE | Microstruttura exchange | 15 | 60,00% | +2,60% |
| DOGE | SETTIMANALE | Tecnico | 103 | 65,05% | +1,89% |
| DOGE | SWING | Classic technical | 42 | 69,05% | -0,19% |
| DOGE | SWING | Famiglia statistica | 63 | 76,19% | +6,80% |
| DOGE | SWING | Microstruttura exchange | 6 | 83,33% | +2,02% |
| DOGE | SWING | Tecnico | 58 | 67,24% | -1,60% |
| DOGE | MEDIO | Classic technical | 22 | 50,00% | -8,95% |
| DOGE | MEDIO | Famiglia statistica | 25 | 64,00% | -1,38% |
| DOGE | MEDIO | Microstruttura exchange | 2 | 100,00% | +31,53% |
| DOGE | MEDIO | Tecnico | 25 | 48,00% | -9,45% |
| SOL | BREVE | Classic technical | 81 | 54,32% | +0,94% |
| SOL | BREVE | Famiglia statistica | 123 | 52,03% | +0,59% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 12 | 41,67% | +0,40% |
| SOL | BREVE | Tecnico | 129 | 48,06% | +0,14% |
| SOL | SETTIMANALE | Classic technical | 67 | 52,24% | +0,83% |
| SOL | SETTIMANALE | Famiglia statistica | 108 | 62,96% | +3,86% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Microstruttura exchange | 7 | 28,57% | -1,10% |
| SOL | SETTIMANALE | Tecnico | 114 | 40,35% | -2,61% |
| SOL | SWING | Classic technical | 41 | 39,02% | -5,20% |
| SOL | SWING | Famiglia statistica | 55 | 81,82% | +7,73% |
| SOL | SWING | Frattale SOL | 2 | 0,00% | -3,49% |
| SOL | SWING | Microstruttura exchange | 3 | 33,33% | +4,53% |
| SOL | SWING | Tecnico | 61 | 37,70% | -5,16% |
| SOL | MEDIO | Classic technical | 12 | 16,67% | -15,60% |
| SOL | MEDIO | Famiglia statistica | 20 | 65,00% | +3,65% |
| SOL | MEDIO | Frattale SOL | 2 | 50,00% | +7,38% |
| SOL | MEDIO | Microstruttura exchange | 1 | 100,00% | +8,54% |
| SOL | MEDIO | Tecnico | 25 | 32,00% | -5,46% |

## Aree ancora in attesa

| Asset | Famiglia | Righe senza controlli | Stato |
| --- | --- | --- | --- |
| BTC | BREVE | 3 | in attesa di controlli maturati |
| BTC | SETTIMANALE | 3 | in attesa di controlli maturati |
| BTC | SWING | 2 | in attesa di controlli maturati |
| BTC | MEDIO | 9 | in attesa di controlli maturati |
| SOL | MEDIO | 7 | in attesa di controlli maturati |
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
| BTC     |         48 |              20 |          28 | RACCOLTA DATI | 0,00%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| SOL     |         48 |              20 |          28 | RACCOLTA DATI | 5,00%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| DOGE    |         48 |              20 |          28 | RACCOLTA DATI | 10,00%           | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |

Regola: sotto 60 controlli osserva soltanto; da 100+ controlli può diventare utile per correggere rischio spot/leva nel Decision Report.

## Ultima lettura rapida

| Asset   | Rischio spot   | Rischio leva   | Nota leva                                                               |
|:--------|:---------------|:---------------|:------------------------------------------------------------------------|
| BTC     | MEDIO          | MOLTO ALTO     | leva da limitare; 2x/3x solo con invalidazione chiara                   |
| SOL     | MEDIO          | MOLTO ALTO     | leva da limitare; 2x/3x solo con invalidazione chiara                   |
| DOGE    | MEDIO          | MOLTO ALTO     | spot preferibile; leva molto pericolosa anche 2x/3x senza margine largo |
<!-- RISK_CALIBRATION_END -->

</details>
<!-- COMPACT_SECTION_END:risk_calibration -->

<!-- COMPACT_SECTION_START:global_confluence -->
<details open>
<summary><strong>🌐 Global Confluence — quadro finale</strong></summary>

<!-- GLOBAL_CONFLUENCE_START -->
# Sintesi finale di confluenza

Generato: 2026-08-27 05:33 UTC


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
| BTC | +7 | POSITIVA FORTE | Rialzista | MEDIA / ALTA | ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA | Prima resistenza sopra 82.792; conferma del doppio minimo sopra 66.910. | Sotto 62.488 il quadro tecnico peggiora. |
| SOL | +7 | POSITIVA FORTE | Rialzista | MEDIA / ALTA | HOLD / ACCUMULO A TRANCHE, NO LEVA AGGRESSIVA | Doppio minimo target raggiunto finché mantiene 78,73; nuova conferma tecnica sopra 127,97; milestone analogiche 114,65 / 139,61, valide soltanto se rientra anche il gap frattale. | Allarmi sotto 93,22 / 74,20 / 62,19. |
| DOGE | -1 | DEBOLE / FRAGILE | Fragile | BASSA / RACCOLTA DATI | EVITA LONG / SOLO RIMBALZI VELOCI | Sopra 0.09998 migliora; sopra 0.06933 viene invalidato il pattern ribassista dominante. | Sotto 0.06895 il rischio ribassista aumenta. |

## Punteggi per modulo

| Asset | Scanner grezzo | Market grezzo | Famiglia statistica | Scanner path | Tecnico | Classic tech | Frattale SOL | Fractal path | RSI top-cycle | Lifecycle EMA | Exchange flow | Futures | Daily change | Totale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +3 | 0 | +3 | 0 | +3 | +1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | +7 |
| SOL | +2 | 0 | +2 | 0 | +3 | +1 | 0 | 0 | 0 | 0 | 0 | 0 | +1 | +7 |
| DOGE | -1 | 0 | -1 | 0 | +1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | -1 | -1 |

Le colonne **Scanner grezzo** e **Market grezzo** sono diagnostiche: nel totale entra soltanto la colonna **Famiglia statistica**.

## Lettura asset per asset

### BTC

- Confluenza: **POSITIVA FORTE**
- Bias: **Rialzista**
- Punteggio finale: **+7**
- Affidabilità: **MEDIA / ALTA**
- Azione coerente: **ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA**

BTC ha una confluenza positiva forte. Resta comunque necessario evitare leva eccessiva: la conferma deve arrivare da prezzo e resistenze, non solo dallo score.

Dettaglio moduli:

- Famiglia statistica: **+3** — Scanner grezzo +3, Market Regime grezzo 0, match regime 0. Regime ignorato: meno di 5 match utili. Punteggio contato nel Global: +3.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **+3** — Casi positivi 70,00%, return centrale 30g +11,54%. Direzione scanner: SALITA. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **0** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 0, positivi 30g n/a, return p50 n/a.
- Scanner path: **0** — Controlli disponibili 46. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **+3** — Score tecnico 10/12, verdetto rialzista tecnico, trend rialzista, struttura compressione / triangolo, divergenza rialzista nascosta rsi, Wyckoff markup / fase rialzista, pattern score 0 (rialzista Doppio minimo / TARGET RAGGIUNTO; ribassista Doppio massimo / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **+1** — Score classico 5/12, verdetto COSTRUTTIVO / CONFERMA PARZIALE, stage STAGE 3 / DISTRIBUZIONE O PAUSA, struttura MASSIMI E MINIMI CRESCENTI, Wyckoff SIGN OF STRENGTH POSSIBILE, volatilità locale MEDIO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Non applicabile a questo asset.
- Fractal path: **0** — Non applicabile a questo asset.
- RSI top-cycle: **0** — Non applicabile a questo asset.
- Lifecycle EMA: **0** — Non applicabile a questo asset.
- Exchange flow: **0** — Flow +1.75, derivati +0.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +0.50; exchange 3/3, copertura 100%, consenso bull 1, bear 0, divergenze 0, campioni 4h 9 su 4.00h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias LEGGERMENTE POSITIVA / NON PESATA; confidenza BASSA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Misto, forza 1/5.
- Daily change: **0** — BTC: nessun cambiamento forte in miglioramento rispetto a ieri.

Conferme: Prima resistenza sopra 82.792; conferma del doppio minimo sopra 66.910.

Invalidazioni: Sotto 62.488 il quadro tecnico peggiora.

### SOL

- Confluenza: **POSITIVA FORTE**
- Bias: **Rialzista**
- Punteggio finale: **+7**
- Affidabilità: **MEDIA / ALTA**
- Azione coerente: **HOLD / ACCUMULO A TRANCHE, NO LEVA AGGRESSIVA**

SOL ha una confluenza molto interessante, ma resta più rischiosa di BTC. Le conferme tecniche e frattali devono comunque reggere prima di usare leva.

Dettaglio moduli:

- Famiglia statistica: **+2** — Scanner grezzo +2, Market Regime grezzo 0, match regime 0. Regime ignorato: meno di 5 match utili. Punteggio contato nel Global: +2.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **+2** — Casi positivi 62,50%, return centrale 30g +3,92%. Direzione scanner: SALITA. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **0** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 0, positivi 30g n/a, return p50 n/a.
- Scanner path: **0** — Controlli disponibili 46. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **+3** — Score tecnico 9/12, verdetto rialzista tecnico, trend rialzista, struttura compressione / triangolo, divergenza nessuna, Wyckoff markup / fase rialzista, pattern score 0 (rialzista Doppio minimo / TARGET RAGGIUNTO; ribassista Doppio massimo / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **+1** — Score classico 7/12, verdetto COSTRUTTIVO / CONFERMA PARZIALE, stage STAGE 3 / DISTRIBUZIONE O PAUSA, struttura MASSIMI E MINIMI CRESCENTI, Wyckoff SIGN OF STRENGTH POSSIBILE, volatilità locale MEDIO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Verdetto ANALOGIA DEBOLE / SCENARIO SECONDARIO, somiglianza strutturale +64,58%, aderenza live +71,13%, errore live +14,43%, gap corrente +17,22%, peso operativo 0, tracking STRUTTURA STABILE, fase FRATTALE SOLO DI CONTESTO, rischio ALTO.
- Fractal path: **0** — Controlli disponibili 42, ma percorso ancorato non aderente: gap +17,22%, errore live +14,43%. Peso 0.
- RSI top-cycle: **0** — Rischio top-cycle RSI: BASSO.
- Lifecycle EMA: **0** — Contesto non pesato nel Global. Lifecycle score 2, bias CONTESTO DA OSSERVARE, EMA200 111,33 $, upside EMA200 +15,25%, gap EMA50/EMA200 -5,95%, hit EMA200 12w +53,33%, trend STABILE / DA CONFERMARE. Peso Global forzato a 0.
- Exchange flow: **0** — Flow +1.75, derivati +0.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +1.00; exchange 3/3, copertura 100%, consenso bull 2, bear 1, divergenze 0, campioni 4h 9 su 4.00h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias LEGGERMENTE POSITIVA / NON PESATA; confidenza MEDIA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Rischio sotto, forza 2/5.
- Daily change: **+1** — SOL: cambiamento forte in miglioramento rispetto a ieri.

Conferme: Doppio minimo target raggiunto finché mantiene 78,73; nuova conferma tecnica sopra 127,97; milestone analogiche 114,65 / 139,61, valide soltanto se rientra anche il gap frattale.

Invalidazioni: Allarmi sotto 93,22 / 74,20 / 62,19.

### DOGE

- Confluenza: **DEBOLE / FRAGILE**
- Bias: **Fragile**
- Punteggio finale: **-1**
- Affidabilità: **BASSA / RACCOLTA DATI**
- Azione coerente: **EVITA LONG / SOLO RIMBALZI VELOCI**

DOGE non ha ancora una confluenza pulita. Serve conferma tecnica prima di trattarlo come asset forte.

Dettaglio moduli:

- Famiglia statistica: **-1** — Scanner grezzo -1, Market Regime grezzo 0, match regime 0. Regime ignorato: meno di 5 match utili. Punteggio contato nel Global: -1.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **-1** — Casi positivi 40,00%, return centrale 30g -4,56%. Direzione scanner: DISCESA. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **0** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 0, positivi 30g n/a, return p50 n/a.
- Scanner path: **0** — Controlli disponibili 46. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **+1** — Score tecnico 2/12, verdetto neutrale / misto, trend misto, struttura rialzista con massimi e minimi crescenti, divergenza nessuna, Wyckoff markdown / fase ribassista, pattern score 0 (rialzista Triplo minimo / TARGET RAGGIUNTO; ribassista Doppio massimo / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **0** — Score classico 0/12, verdetto NEUTRALE / MISTO, stage STAGE 4 / MARKDOWN, struttura MASSIMI E MINIMI CRESCENTI, Wyckoff ACCUMULO POSSIBILE / RANGE BASSO, volatilità locale MEDIO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Non applicabile a questo asset.
- Fractal path: **0** — Non applicabile a questo asset.
- RSI top-cycle: **0** — Non applicabile a questo asset.
- Lifecycle EMA: **0** — Non applicabile a questo asset.
- Exchange flow: **0** — Flow +0.75, derivati +0.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +0.00; exchange 3/3, copertura 100%, consenso bull 1, bear 1, divergenze 0, campioni 4h 9 su 4.00h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias MISTA / NEUTRALE; confidenza BASSA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Misto, forza 1/5.
- Daily change: **-1** — DOGE: cambiamento forte in peggioramento rispetto a ieri.

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

Generato: 2026-08-27 05:33 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [btc_macro_cycle_report.md](btc_macro_cycle_report.md)

Questo modulo descrive il contesto macro di Bitcoin. Non genera entrate tattiche, non autorizza leva e pesa **0** nel Global Confluence.

## Sintesi

| Voce | Valore | Lettura |
| --- | --- | --- |
| Prezzo BTC | 78.625 $ | prezzo corrente |
| Power Law centrale | 124.102 $ | deviazione -36,64% |
| Banda p10-p90 | 77.092 $ / 313.625 $ | BASSA NEL CORRIDOIO |
| Percentile residuo | 11,81% | posizione storica nel corridoio |
| Esponente β | 5,8116 | R² log-log 91,93% |
| Stabilità β | BASSA | range 1,3164 cambiando finestra |
| Ultimo halving | 2024-04-19 | 860 giorni fa |
| Fase ciclo | 58,87% | percentuale indicativa del ciclo quadriennale |
| Peso Global | 0 | CONTESTO MACRO / DIAGNOSTICO |

La Power Law viene trattata come regressione empirica, non come legge fisica. Il report mostra quanto cambia l'esponente usando finestre iniziali diverse e la confronta con il benchmark ingenuo 'prezzo invariato'.

## Bitcoin Power Law

- Campione: 2014-09-17 → 2026-08-27 (4362 osservazioni)
- Formula stimata: prezzo ≈ exp(-39.1222) × giorni^5.8116
- Prezzo centrale oggi: **124.102 $**
- Posizione corrente: **BASSA NEL CORRIDOIO**, percentile 11,81%
- Scarto dal centro: **-36,64%**

![Bitcoin Power Law](btc_power_law_chart.png)

![Bitcoin Power Law log-log](btc_power_law_loglog_chart.png)

### Stabilità dell'esponente

| Inizio campione | β | R² log-log |
| --- | --- | --- |
| 2014 | 5,8116 | 91,93% |
| 2015 | 5,8947 | 91,48% |
| 2016 | 5,5796 | 87,72% |
| 2017 | 4,8505 | 82,87% |
| 2018 | 4,5783 | 78,35% |

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
| 2012-11-28 → 2016-07-09 | 2015-01-13 | -1,81% | -0,56% | +37,64% | +91,43% |
| 2016-07-09 → 2020-05-11 | 2018-10-12 | +2,18% | -41,37% | -15,14% | +32,86% |
| 2020-05-11 → 2024-04-19 | 2022-09-05 | +1,76% | -13,54% | +12,83% | +30,12% |

Campione molto piccolo: questi rendimenti sono contesto di ciclo, non probabilità affidabili.

## SOL/BTC e DOGE/BTC dentro il tempo Bitcoin

![Altcoin nel ciclo BTC](alt_btc_cycle_spirals.png)

| Asset | Coppia | Forza vs BTC | Score raw | Candidato | 30g | Peso Global |
| --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | SOVRAPERFORMA BTC | 5 | 1 | 10.240547656071541 | 0 |
| DOGE | DOGE/BTC | SOTTOPERFORMA BTC | -4 | -1 | -0.6386901121812616 | 0 |

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

Generato: 2026-08-27 05:33 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [relative_strength_btc_report.md](relative_strength_btc_report.md)

Questo modulo controlla se SOL e DOGE stanno davvero battendo Bitcoin. Una salita in USD accompagnata da una coppia ALT/BTC ribassista è spesso soltanto trascinamento di BTC.

**Protezione iniziale:** il candidato relativo è limitato a -1/0/+1, ma il peso nel Global resta **0**. La coppia BTC conferma o indebolisce il tecnico USD; non viene sommata come secondo modulo indipendente.

## Sintesi

| Asset | Coppia | Prezzo | Score raw | Candidato | Peso Global | Forza vs BTC | Confidenza | 30g | Tecnico USD | Lettura combinata |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | 0.00128320 | +5 | +1 | 0 | SOVRAPERFORMA BTC | MEDIA | +10,24% | RIALZISTA | CONFERMA FORTE: sale in USD e batte BTC |
| DOGE | DOGE/BTC | 0.00000110 | -4 | -1 | 0 | SOTTOPERFORMA BTC | BASSA | -0,64% | MISTA | FORZA RELATIVA NEGATIVA, USD ANCORA MISTO |

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
- **Rendimenti relativi:** 7g +4,16%; 30g +10,24%; 90g +15,09%; 180g +3,15%
- **Daily:** RSI 68.53; MA50 0.00118608; MA200 0.00117732
- **Weekly:** MA30 0.00118261; RSI 55.50
- **Livelli:** supporto 0.00122200; resistenza 0.00129400; breakout 60g 0.00134900; breakdown 60g 0.00109300
- **Pattern:** DOPPIO MINIMO / TARGET RAGGIUNTO; neckline 0.00120200; target 0.00125350
- **Fibonacci:** VICINO — 23.6% a 0.00126876
- **Fonte:** Yahoo Finance SOL-BTC (coppia diretta)
- **Motivi score:** prezzo sopra MA50 daily; prezzo sopra MA200 daily; prezzo sopra MA30 weekly; MA30 weekly in discesa; struttura con massimi/minimi crescenti; RSI relativo forte; MACD relativo positivo

![Grafico SOL/BTC](relative_strength_SOLBTC.png)

## DOGE/BTC

- **Verdetto relativo:** SOTTOPERFORMA BTC (-4)
- **Candidato futuro:** -1; **peso attuale Global: 0**
- **Lettura combinata USD/BTC:** FORZA RELATIVA NEGATIVA, USD ANCORA MISTO
- **Struttura:** VOLATILITÀ IN ESPANSIONE
- **Rendimenti relativi:** 7g +1,32%; 30g -0,64%; 90g -18,88%; 180g -22,62%
- **Daily:** RSI 45.85; MA50 0.00000111; MA200 0.00000129
- **Weekly:** MA30 0.00000128; RSI 36.65
- **Livelli:** supporto 0.00000105; resistenza 0.00000114; breakout 60g 0.00000135; breakdown 60g 0.00000100
- **Pattern:** DOPPIO MINIMO / TARGET RAGGIUNTO; neckline 0.00000115; target 0.00000128
- **Fibonacci:** NON ATTIVO — 23.6% a 0.00000112
- **Fonte:** Rapporto sintetico DOGE-USD / BTC-USD (sintetica)
- **Motivi score:** prezzo sotto MA50 daily; prezzo sotto MA200 daily; MA50 daily in discesa; prezzo sotto MA30 weekly; MA30 weekly in discesa; MACD relativo positivo

![Grafico DOGE/BTC](relative_strength_DOGEBTC.png)

## Backtest storico diagnostico

Il backtest usa soltanto indicatori disponibili alla data del segnale e campiona una volta a settimana. È utile subito, ma non sostituisce il tracker live: le soglie sono state definite prima di vedere il risultato.

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto direzione | Return futuro mediano |
| --- | --- | --- | --- | --- | --- |
| SOL | 7g | 205 | 52,20% | +1,94% | -1,06% |
| SOL | 30g | 203 | 47,29% | +4,60% | +0,36% |
| SOL | 90g | 198 | 53,03% | +10,08% | +2,72% |
| DOGE | 7g | 294 | 55,78% | +1,84% | -1,68% |
| DOGE | 30g | 292 | 53,08% | +2,00% | -3,71% |
| DOGE | 90g | 286 | 53,85% | +6,84% | -8,85% |

## Tracker live e gate futuro

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto | Stato | Peso Global |
| --- | --- | --- | --- | --- | --- | --- |
| SOL | 1g | 23 | 69,57% | +0,16% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 3g | 21 | 57,14% | +0,15% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 7g | 18 | 44,44% | -0,56% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 14g | 15 | 6,67% | -3,37% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 30g | 4 | 0,00% | -7,60% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 1g | 36 | 69,44% | +0,02% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 3g | 35 | 60,00% | +0,21% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 7g | 35 | 62,86% | +0,44% | ELIGIBILE FUTURO ±1 | 0 |
| DOGE | 14g | 32 | 68,75% | +0,15% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 30g | 18 | 77,78% | +0,57% | LOCKED / RACCOLTA LIVE | 0 |

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

Ultima candela SOL usata: **27 agosto 2026**

## SOL PRICE CONTEXT

| Voce | Valore | Provenienza / significato |
| --- | --- | --- |
| Anchor computazionale | 100,99 $ | 2026-08-27T05:30:23Z \| Yahoo Finance daily shared snapshot \| Close 1d |
| Candela anchor completata | NO | Stato esplicito; il valore non viene sostituito dal prezzo pubblico. |
| Riferimento pubblico corrente | 100,88 $ | 2026-08-27T05:32:00Z \| Yahoo Finance \| solo display |
| Età anchor alla generazione | 0h 1m | WITHIN_DAILY_REPORT_CADENCE |
| Gap corrente vs anchor | -0,11000 $ | -0,11% |
| Validità input modello | REPRODUCIBLE_SHARED_SNAPSHOT | Non è una dichiarazione di validità del segnale/trading. |

```text
COMPUTATIONAL_ANCHOR_PRICE=100.98999786376953
COMPUTATIONAL_ANCHOR_FIELD=Close
COMPUTATIONAL_ANCHOR_TIMESTAMP=2026-08-27T05:30:23Z
COMPUTATIONAL_ANCHOR_SYMBOL=SOL-USD
COMPUTATIONAL_ANCHOR_PROVIDER=Yahoo Finance daily shared snapshot
COMPUTATIONAL_ANCHOR_TIMEFRAME=1d
COMPUTATIONAL_ANCHOR_COMPLETED=NO
CURRENT_PUBLIC_REFERENCE_PRICE=100.87999725341797
CURRENT_PUBLIC_REFERENCE_TIMESTAMP=2026-08-27T05:32:00Z
CURRENT_PUBLIC_REFERENCE_ACQUIRED_AT=2026-08-27T05:32:16Z
CURRENT_PUBLIC_REFERENCE_SYMBOL=SOL-USD
CURRENT_PUBLIC_REFERENCE_PROVIDER=Yahoo Finance
CURRENT_PUBLIC_REFERENCE_FIELD=Close
CURRENT_PUBLIC_REFERENCE_TIMEFRAME=1m
CURRENT_PUBLIC_REFERENCE_STATUS=AVAILABLE
ANCHOR_AGE_SECONDS=114.146453
ANCHOR_AGE_HOURS=0.031707348055555556
CURRENT_VS_ANCHOR_GAP_USD=-0.1100006103515625
CURRENT_VS_ANCHOR_GAP_PCT=-0.10892228208574384
```

## Verdetto: ANALOGIA DEBOLE / SCENARIO SECONDARIO

- **Fase attuale:** FRATTALE SOLO DI CONTESTO
- **Somiglianza totale:** +64,58%
- **Somiglianza strutturale:** +64,58%
- **Aderenza prezzo live:** +71,13%
- **Errore medio live:** +14,43%
- **Gap prezzo corrente:** +17,22%
- **Peso operativo suggerito:** 0
- **Affidabilita:** BASSA
- **Rischio fase:** ALTO
- **Trend tracking:** STRUTTURA STABILE
- **Sintesi:** Esistono alcuni elementi comuni, ma non abbastanza per una conferma.
- **SOL è al giorno:** 82 dal bottom usato.
- **Giorno BTC equivalente:** 2023-02-11
- **Prossimo step:** Proiezione condizionale, non conferma operativa: **Leggera continuazione rialzista.** Zona bassa **100,61 $** intorno al **28 agosto 2026**; zona alta **114,65 $** intorno al **5 settembre 2026**; fine step circa **107,01 $** entro il **10 settembre 2026**.

### Metadata aderenza prezzo

```text
OPERATIONAL_VERDICT_REASON=ANALOGIA DEBOLE / SCENARIO SECONDARIO
PRICE_ADHERENCE_FAILED=NO
PRICE_ADHERENCE_LIVE_AVG_GAP_FAILED=NO
PRICE_ADHERENCE_LAST_GAP_FAILED=NO
PRICE_ADHERENCE_LIVE_AVG_GAP_THRESHOLD_PCT=15.0
PRICE_ADHERENCE_LAST_GAP_THRESHOLD_PCT=18.0
PRICE_ADHERENCE_OBSERVED_LIVE_AVG_GAP_PCT=14.433297760902224
PRICE_ADHERENCE_OBSERVED_LAST_GAP_PCT=17.219655998185136
```

## Somiglianza prima e dopo inizio programma

Questa sezione separa la somiglianza della forma dall'aderenza reale del prezzo.

- **Inizio programma/scanner:** 3 luglio 2026
- **Prima del programma** = backtest retroattivo.
- **Da inizio programma** = verifica live: è la parte più importante per l'uso operativo.

| Periodo | Date | Giorni | Aderenza prezzo | Errore medio | Gap ultimo | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| Prima del programma | 6 giugno 2026 -> 2 luglio 2026 | 27 | +87,95% | +6,02% | +21,89% | ABBASTANZA ALLINEATO |
| Da inizio programma | 3 luglio 2026 -> 27 agosto 2026 | 56 | +71,13% | +14,43% | +17,22% | DEVIAZIONE MODERATA |
| Totale dal bottom | 6 giugno 2026 -> 27 agosto 2026 | 83 | +76,60% | +11,70% | +17,22% | DEVIAZIONE MODERATA |

Nota: un frattale può avere una forma simile ma un prezzo distante. In quel caso non è operativo finché il gap non rientra.

## Lettura operativa veloce

Il frattale resta non operativo. Motivo effettivo: ANALOGIA DEBOLE / SCENARIO SECONDARIO.

| Voce | Risposta | Perché |
| --- | --- | --- |
| Uso operativo | NO | Peso 0 per il verdetto: ANALOGIA DEBOLE / SCENARIO SECONDARIO. |
| Aderenza live | +71,13% | Errore medio live +14,43%. |
| Gap corrente | +17,22% | Metrica separata dal motivo del verdetto. |
| Prima conferma prezzo | 114,65 $ | Serve anche miglioramento del gap, non solo una candela sopra il livello. |
| Seconda conferma | 139,61 $ | Rende più credibile il percorso, ma non sostituisce l'aderenza. |
| Invalidazione soft | 93,22 $ | Sotto questa zona il quadro peggiora. |
| Invalidazione forte | 62,19 $ | Sotto il bottom il paragone è quasi rotto. |

## Target ciclo fino al top BTC 2025

| Voce | Valore |
| --- | --- |
| Stato | CONTESTO / NON OPERATIVO |
| Top BTC 2025 | 6 ottobre 2025 - 124.753 $ |
| Data SOL equivalente | 21 aprile 2029 |
| Target ciclo base dall'anchor modello | 576,05 $ |
| Massimo percorso base | 576,05 $ (21 aprile 2029) |

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
| Prima conferma | 114,65 $ | Deve accompagnarsi al rientro del gap. |
| Seconda conferma | 139,61 $ | Scenario più credibile. |
| Invalidazione soft | 93,22 $ | Il frattale si indebolisce. |
| Invalidazione forte | 62,19 $ | Il paragone si rompe. |

## Proiezione veloce con date SOL

| Orizzonte | Data SOL | BTC fece | SOL base | Min percorso | Max percorso |
| --- | --- | --- | --- | --- | --- |
| 7 giorni | 3 settembre 2026 | +12,67% | 113,78 $ | 100,61 $ | 113,78 $ |
| 14 giorni | 10 settembre 2026 | +5,96% | 107,01 $ | 100,61 $ | 114,65 $ |
| 30 giorni | 26 settembre 2026 | +10,64% | 111,73 $ | 93,22 $ | 114,65 $ |
| 60 giorni | 26 ottobre 2026 | +37,80% | 139,17 $ | 93,22 $ | 139,61 $ |
| 90 giorni | 25 novembre 2026 | +22,56% | 123,77 $ | 93,22 $ | 140,77 $ |
| 120 giorni | 25 dicembre 2026 | +18,61% | 119,78 $ | 93,22 $ | 140,77 $ |

## Prossimi step se SOL segue BTC 2022

| Step | Date SOL | BTC fine | SOL zona bassa | SOL zona alta | SOL fine base | Lettura |
| --- | --- | --- | --- | --- | --- | --- |
| Step 1 - prossime 2 settimane | 27 agosto 2026 -> 10 settembre 2026 | +5,96% | 100,61 $ (28 agosto 2026) | 114,65 $ (5 settembre 2026) | 107,01 $ | Leggera continuazione rialzista. |
| Step 2 - primo mese | 11 settembre 2026 -> 26 settembre 2026 | +10,64% | 93,22 $ (23 settembre 2026) | 111,73 $ (26 settembre 2026) | 111,73 $ | Prima retest / debolezza, poi recupero. |
| Step 3 - secondo mese | 27 settembre 2026 -> 26 ottobre 2026 | +37,80% | 112,56 $ (28 settembre 2026) | 139,61 $ (25 ottobre 2026) | 139,17 $ | Spinta rialzista abbastanza pulita. |
| Step 4 - terzo mese | 27 ottobre 2026 -> 25 novembre 2026 | +22,56% | 123,77 $ (25 novembre 2026) | 140,77 $ (28 ottobre 2026) | 123,77 $ | Spinta rialzista abbastanza pulita. |

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
| Prezzo SOL | 100,99 $ |  |
| Weekly RSI | 57,51 / linea grezza 52,71 | LINEA NON AFFIDABILE / RISCHIO NON ATTIVO — IRREALISTICA / NON OPERATIVA |
| Monthly RSI | 46,58 / linea grezza 55,81 | RSI TROPPO BASSO PER RISCHIO TOP — VALIDA / USO PRUDENTE |
| Target ciclo base | 576,05 $ | Avanzamento +17,53% |
| Rischio top-cycle RSI | BASSO | Nessun segnale top-cycle macro attivo. Prezzo ancora lontano dal target ciclo; il filtro RSI resta solo di monitoraggio. |

## Lettura semplice

- Weekly: La top-line weekly non supera i controlli di qualità. Non viene usata per generare rischio top-cycle.
- Monthly: RSI monthly è 46,6, sotto la soglia prudente 55. Anche se fosse vicino alla linea, non è una vera zona di esaurimento ciclo.
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
| Score on-chain | 1 |
| Bias | NEUTRALE / MISTA |
| Azione coerente | NESSUNA CONFERMA FORTE / LEGGERE INSIEME AL FRATTALE |
| Prezzo SOL | 100,99 $ |
| TVL Solana | 5,77 mld $ |
| TVL 7g | +10,39% |
| DEX volume 24h | 2,48 mld $ |
| Fees 24h | 14,68 mln $ |
| Stablecoin su Solana | 16,22 mld $ |
| Stake ratio | 69,02% |
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
| Confronto precedente | 2026-08-24 |
| Fonte prezzi | Yahoo Finance SOL-USD weekly |
| Prezzo SOL | 100,99 $ |
| EMA200 weekly target | 111,33 $ |
| Upside verso EMA200 | +15,25% |
| Distanza prezzo da EMA200 | -13,23% |
| Gap EMA50/EMA200 | -5,95% |
| Stato cross | EMA50 SOTTO EMA200 |
| RSI weekly | 55,19 |
| Età SOL | 6,4 anni |
| Analoghi storici usati | 30 |
| Max analoghi per asset | 3 |
| Hit EMA200 12w analoghi | +53,33% |
| Max gain mediano 12w | +19,24% |
| Drawdown mediano 12w | -31,57% |

Lettura semplice:

**SOLO OSSERVAZIONE**

Autocontrollo: **STABILE / DA CONFERMARE**.

Questo modulo confronta SOL con altre crypto in fasi simili di età, distanza da EMA200, EMA50/EMA200 e RSI. Non usa stock market.

Nota importante: **questo modulo ora NON pesa più nel Global Confluence**. Resta solo come contesto di ciclo e come mappa verso EMA200 weekly. Il punteggio Global resta guidato da prezzo, scanner, regime, struttura tecnica, frattale, RSI e conferme reali.

Nota: se EMA50/EMA200 sono dentro ±2%, il modulo parla di medie sovrapposte / incrocio in corso, perché exchange diversi possono mostrare il cross leggermente prima o dopo.

<!-- Generato: 2026-08-27 05:32 UTC -->
<!-- MAJOR_ALT_LIFECYCLE_SQUEEZE_END -->

</details>
<!-- COMPACT_SECTION_END:major_alt_lifecycle -->

# Report giornaliero BTC / SOL / DOGE

Aggiornato il: **2026-08-27 05:30:24 UTC**

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
- SOL: cambiamento importante in miglioramento rispetto a ieri.
- DOGE: cambiamento importante in peggioramento rispetto a ieri.

| Asset | Cambio | Tono | Verdetto oggi | Casi positivi oggi | Δ casi positivi |
| --- | --- | --- | --- | --- | --- |
| BTC | NESSUN CAMBIAMENTO FORTE | miglioramento | RIALZISTA | +70.00% | +2.50 punti |
| SOL | CAMBIAMENTO FORTE | miglioramento | RIALZISTA | +62.50% | +5.00 punti |
| DOGE | CAMBIAMENTO FORTE | peggioramento | NEUTRALE / INCERTO | +40.00% | -10.00 punti |

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
| BTC | 74.721 $ | 86.519 $ | +61,29% | +15,79% | rimbalzo possibile | 86.519 $ | 74.721 $ | +35,48% | -13,64% | scarico possibile |
| SOL | 95,94 $ | 111,09 $ | +54,55% | +15,79% | rimbalzo possibile | 111,09 $ | 95,94 $ | +17,86% | -13,64% | spike storicamente più resistente |
| DOGE | 0,08217 $ | 0,09515 $ | +43,33% | +15,79% | rimbalzo debole | 0,09515 $ | 0,08217 $ | +51,61% | -13,64% | attenzione a prendere profitto |

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

- **BTC: su 40 casi simili, 31 prima sono scesi a -5,00%. Tra quei 31, 19 poi sono rimbalzati fino a +10,00%. Percentuale: +61,29% (19/31). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo possibile.**
- **BTC: su 40 casi simili, 31 prima sono saliti a +10,00%. Tra quei 31, 11 poi sono scaricati a -5,00%. Percentuale: +35,48% (11/31). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: scarico possibile.**
- **SOL: su 40 casi simili, 33 prima sono scesi a -5,00%. Tra quei 33, 18 poi sono rimbalzati fino a +10,00%. Percentuale: +54,55% (18/33). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo possibile.**
- **SOL: su 40 casi simili, 28 prima sono saliti a +10,00%. Tra quei 28, 5 poi sono scaricati a -5,00%. Percentuale: +17,86% (5/28). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.**
- **DOGE: su 40 casi simili, 30 prima sono scesi a -5,00%. Tra quei 30, 13 poi sono rimbalzati fino a +10,00%. Percentuale: +43,33% (13/30). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.**
- **DOGE: su 40 casi simili, 31 prima sono saliti a +10,00%. Tra quei 31, 16 poi sono scaricati a -5,00%. Percentuale: +51,61% (16/31). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: attenzione a prendere profitto.**

<!-- BOUNCE_AFTER_DRAWDOWN_END -->

</details>
<!-- COMPACT_SECTION_END:bounce_after_drawdown -->

<!-- COMPACT_SECTION_START:scanner_forecast -->
<details>
<summary><strong>🔭 Cono probabilistico dello scanner</strong></summary>

<!-- SCANNER_FORECAST_TRACKER_START -->
# Scanner forecast path / cono probabilistico

Generato: 2026-08-27 05:31:47 UTC


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

| Asset   | Data       | Prezzo iniziale   | Direzione scanner   | Casi positivi   | P10 30g     | P25 30g     | P50 30g     | P75 30g     | P90 30g      |
|:--------|:-----------|:------------------|:--------------------|:----------------|:------------|:------------|:------------|:------------|:-------------|
| BTC | 2026-08-27 | 78.653 $ | SALITA | 70,00% | 69.633,83 $ | 77.036,02 $ | 87.726,91 $ | 94.069,53 $ | 110.479,34 $ |
| SOL | 2026-08-27 | 100,99 $ | SALITA | 62,50% | 89,12 $ | 98,05 $ | 104,95 $ | 120,32 $ | 196,29 $ |
| DOGE | 2026-08-27 | 0.08650 $ | DISCESA | 40,00% | 0.06503 $ | 0.07575 $ | 0.08256 $ | 0.09074 $ | 0.10718 $ |

## Grafici

### BTC

![Scanner forecast BTC](scanner_forecast_BTC.png)

#### Verifica storica e discrepanza

![Verifica storica cono BTC](scanner_forecast_history_BTC.png)

- Cono congelato il **2026-07-28**; verificato fino al **2026-08-27**; stato **COMPLETO 30/30g**.
- Reale **78.623,64 $**; p50 previsto **68.129,01 $**; scarto **15,40%**.
- Errore medio assoluto **5,13%**; massimo **16,81%**; DENTRO p10-p90; DENTRO p25-p75.

### SOL

![Scanner forecast SOL](scanner_forecast_SOL.png)

#### Verifica storica e discrepanza

![Verifica storica cono SOL](scanner_forecast_history_SOL.png)

- Cono congelato il **2026-07-28**; verificato fino al **2026-08-27**; stato **COMPLETO 30/30g**.
- Reale **100,93 $**; p50 previsto **78,88 $**; scarto **27,95%**.
- Errore medio assoluto **6,47%**; massimo **27,95%**; DENTRO p10-p90; FUORI p25-p75.

### DOGE

![Scanner forecast DOGE](scanner_forecast_DOGE.png)

#### Verifica storica e discrepanza

![Verifica storica cono DOGE](scanner_forecast_history_DOGE.png)

- Cono congelato il **2026-07-28**; verificato fino al **2026-08-27**; stato **COMPLETO 30/30g**.
- Reale **0.08642 $**; p50 previsto **0.07461 $**; scarto **15,83%**.
- Errore medio assoluto **7,47%**; massimo **33,18%**; DENTRO p10-p90; FUORI p25-p75.

## Accuratezza percorso scanner

| Asset   | Giorno   |   Controlli | Dentro p10-p90   | Dentro p25-p75   | Errore medio abs vs p50   | Errore medio vs p50   |
|:--------|:---------|------------:|:-----------------|:-----------------|:--------------------------|:----------------------|
| BTC | 1g | 46 | 93,48% | 58,70% | 2,25% | 0,76% |
| BTC | 3g | 44 | 88,64% | 72,73% | 3,35% | 1,23% |
| BTC | 7g | 40 | 90,00% | 70,00% | 5,59% | 2,90% |
| BTC | 14g | 33 | 96,97% | 72,73% | 5,01% | 2,10% |
| BTC | 30g | 19 | 100,00% | 94,74% | 7,71% | 0,75% |
| SOL | 1g | 46 | 76,09% | 56,52% | 2,93% | 1,09% |
| SOL | 3g | 44 | 86,36% | 65,91% | 4,15% | 1,68% |
| SOL | 7g | 40 | 87,50% | 75,00% | 5,23% | 3,37% |
| SOL | 14g | 33 | 90,91% | 72,73% | 6,13% | 5,01% |
| SOL | 30g | 19 | 94,74% | 57,89% | 11,06% | 10,38% |
| DOGE | 1g | 46 | 84,78% | 58,70% | 3,49% | 1,02% |
| DOGE | 3g | 44 | 88,64% | 70,45% | 4,69% | 2,66% |
| DOGE | 7g | 40 | 80,00% | 75,00% | 9,34% | 7,80% |
| DOGE | 14g | 33 | 81,82% | 57,58% | 11,01% | 9,78% |
| DOGE | 30g | 19 | 89,47% | 36,84% | 17,98% | 17,98% |

## Calibratore shadow

Il cono ufficiale resta grezzo e invariato. Il calibratore usa soltanto previsioni passate già mature, campionate una volta a settimana per ridurre la falsa indipendenza. Ogni orizzonte si attiva a 30 controlli indipendenti: parte al 25% della correzione stimata e cresce gradualmente fino al 100% a 100 controlli.

| Asset   | Orizzonte   |   Controlli indipendenti |   Soglia | Stato                  | Forza correzione   | Shift p50   |   Scala p10-p90 |
|:--------|:------------|-------------------------:|---------:|:-----------------------|:-------------------|:------------|----------------:|
| BTC | 1g | 8 | 30 | RACCOLTA (22 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 3g | 8 | 30 | RACCOLTA (22 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 7g | 7 | 30 | RACCOLTA (23 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 14g | 6 | 30 | RACCOLTA (24 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 30g | 4 | 30 | RACCOLTA (26 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 1g | 8 | 30 | RACCOLTA (22 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 3g | 8 | 30 | RACCOLTA (22 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 7g | 7 | 30 | RACCOLTA (23 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 14g | 6 | 30 | RACCOLTA (24 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 30g | 4 | 30 | RACCOLTA (26 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 1g | 8 | 30 | RACCOLTA (22 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 3g | 8 | 30 | RACCOLTA (22 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 7g | 7 | 30 | RACCOLTA (23 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 14g | 6 | 30 | RACCOLTA (24 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 30g | 4 | 30 | RACCOLTA (26 mancanti) | 0,0% | 0,00% | 1,000 |

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

Righe salvate nello storico: **132**.

Questa sezione tiene un diario delle previsioni giornaliere a 30 giorni, senza appesantire il report principale.

| Data | Asset | Prezzo | Direzione | Casi positivi | Return p50 | Drawdown p50 | Max gain p50 | Controllo 30g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08-27 | BTC | 78.653 $ | SALITA | 70,00% | 87.727 $ | 71.176 $ | 92.526 $ | 2026-09-26 |
| 2026-08-27 | DOGE | 0,09000 $ | DISCESA | 40,00% | 0,08000 $ | 0,08000 $ | 0,10000 $ | 2026-09-26 |
| 2026-08-27 | SOL | 100,99 $ | SALITA | 62,50% | 104,95 $ | 89,49 $ | 115,81 $ | 2026-09-26 |

<!-- FORECAST_30D_HISTORY_END -->

</details>
<!-- COMPACT_SECTION_END:scanner_forecast -->

<!-- COMPACT_SECTION_START:extreme_cases -->
<details>
<summary><strong>⚠️ Percorso dei casi estremi</strong></summary>

<!-- EXTREME_CASES_PATH_START -->
# Extreme cases path report

Generato: 2026-08-27 05:31 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [extreme_cases_path_report.md](extreme_cases_path_report.md)

Questo report si attiva quando i casi positivi o negativi sono almeno **80%**.

Ora misura anche il **rialzo massimo prima della discesa principale**, quindi distingue uno spike iniziale da una discesa quasi immediata.

## Trigger estremi

| Asset   | Direzione   | Trigger   | Percentuale   | Motivo                           |   Match disponibili |
|:--------|:------------|:----------|:--------------|:---------------------------------|--------------------:|
| BTC     | NESSUNO     | NO        | +70,00%       | Nessun lato sopra soglia estrema |                  40 |
| SOL     | NESSUNO     | NO        | +62,50%       | Nessun lato sopra soglia estrema |                  40 |
| DOGE    | NESSUNO     | NO        | +60,00%       | Nessun lato sopra soglia estrema |                  40 |

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
- Casi positivi / salita storica: **70,00%**
- Casi negativi / discesa storica: **30,00%**
- Quanto è netto il segnale: **forte**
- Prezzo attuale: **78.653,26 $**
- Return normale fra 30 giorni: **87.726,91 $** (11,54%)
- Drawdown normale durante il mese: **71.175,56 $** (-9,51%)
- Drawdown brutto da rispettare: **66.849,42 $** (-15,01%)
- Max gain normale durante il mese: **92.525,71 $** (17,64%)
- Max gain buono / take profit ottimistico: **101.453,45 $** (28,99%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Solana
- Direzione più probabile a 30 giorni: **SALITA**
- Casi positivi / salita storica: **62,50%**
- Casi negativi / discesa storica: **37,50%**
- Quanto è netto il segnale: **medio**
- Prezzo attuale: **100,99 $**
- Return normale fra 30 giorni: **104,95 $** (3,92%)
- Drawdown normale durante il mese: **89,49 $** (-11,39%)
- Drawdown brutto da rispettare: **85,43 $** (-15,41%)
- Max gain normale durante il mese: **115,81 $** (14,68%)
- Max gain buono / take profit ottimistico: **132,02 $** (30,72%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Dogecoin
- Direzione più probabile a 30 giorni: **DISCESA**
- Casi positivi / salita storica: **40,00%**
- Casi negativi / discesa storica: **60,00%**
- Quanto è netto il segnale: **debole**
- Prezzo attuale: **0,09 $**
- Return normale fra 30 giorni: **0,08 $** (-4,56%)
- Drawdown normale durante il mese: **0,08 $** (-9,82%)
- Drawdown brutto da rispettare: **0,07 $** (-17,78%)
- Max gain normale durante il mese: **0,10 $** (17,61%)
- Max gain buono / take profit ottimistico: **0,11 $** (24,51%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Messaggio del giorno

Il quadro generale oggi è più favorevole. Lo scanner vede più possibilità di salita su più asset.

---

# Mappa semplice asset per asset

# Bitcoin — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟢 VERDE / Favorevole
**Prezzo attuale:** 78.653,26 $

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

- Se va molto male: **69.633,83 $** (-11,47%)
- Se va male: **77.036,02 $** (-2,06%)
- Scenario normale: **87.726,91 $** (11,54%)
- Se va bene: **94.069,53 $** (19,60%)
- Se va molto bene: **110.479,34 $** (40,46%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **71.175,56 $** (-9,51%)
- Discesa brutta: **66.849,42 $** (-15,01%)
- Discesa molto brutta: **63.660,30 $** (-19,06%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **92.525,71 $** (17,64%)
- Rialzo buono: **101.453,45 $** (28,99%)
- Rialzo molto forte: **117.419,79 $** (49,29%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Bitcoin tendeva a muoversi tra una zona bassa intorno a **71.175,56 $** e uno spike normale intorno a **92.525,71 $**.

La chiusura a 30 giorni era più spesso positiva: salita 70,00%, discesa 30,00%. Quindi la lettura principale è favorevole.

Nota leva BTC: se la liquidazione è vicina a 51.000 $, guarda soprattutto la discesa brutta e molto brutta. Il prezzo può recuperare dopo, ma la leva può saltare prima.

---

# Solana — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟢 VERDE / Favorevole
**Prezzo attuale:** 100,99 $

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

- Se va molto male: **89,12 $** (-11,75%)
- Se va male: **98,05 $** (-2,91%)
- Scenario normale: **104,95 $** (3,92%)
- Se va bene: **120,32 $** (19,14%)
- Se va molto bene: **196,29 $** (94,36%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **89,49 $** (-11,39%)
- Discesa brutta: **85,43 $** (-15,41%)
- Discesa molto brutta: **79,15 $** (-21,63%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **115,81 $** (14,68%)
- Rialzo buono: **132,02 $** (30,72%)
- Rialzo molto forte: **201,13 $** (99,16%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Solana tendeva a muoversi tra una zona bassa intorno a **89,49 $** e uno spike normale intorno a **115,81 $**.

La chiusura a 30 giorni era più spesso positiva: salita 62,50%, discesa 37,50%. Quindi la lettura principale è favorevole.

---

# Dogecoin — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟡 GIALLO / Incerto
**Prezzo attuale:** 0,09 $

**Direzione più probabile a 30 giorni:** **DISCESA**
- Probabilità storica di salita: **40,00%**
- Probabilità storica di discesa: **60,00%**
- Quanto è netto il segnale: **debole**

## Come leggere questa parte

- **Probabilità storica di salita** = su 40 casi simili, quanti hanno chiuso sopra dopo 30 giorni.
- **Probabilità storica di discesa** = su 40 casi simili, quanti hanno chiuso sotto dopo 30 giorni.
- **Quanto è netto il segnale** = quanto è grande la differenza tra salita e discesa. Non vuol dire certezza, vuol dire solo che il risultato storico non è vicino al 50/50.

La lettura principale è ribassista, con segnale debole. Nei casi storici simili, il prezzo ha chiuso sotto dopo 30 giorni più spesso di quanto abbia chiuso sopra.

## 1. Return 30d — prezzo fra 30 giorni

**Return** significa rendimento finale. Qui guardiamo dove potrebbe stare il prezzo **alla fine dei 30 giorni**, non durante il percorso.

- Se va molto male: **0,07 $** (-24,82%)
- Se va male: **0,08 $** (-12,43%)
- Scenario normale: **0,08 $** (-4,56%)
- Se va bene: **0,09 $** (4,90%)
- Se va molto bene: **0,11 $** (23,91%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **0,08 $** (-9,82%)
- Discesa brutta: **0,07 $** (-17,78%)
- Discesa molto brutta: **0,06 $** (-30,87%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **0,10 $** (17,61%)
- Rialzo buono: **0,11 $** (24,51%)
- Rialzo molto forte: **0,14 $** (65,37%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Dogecoin tendeva a muoversi tra una zona bassa intorno a **0,08 $** e uno spike normale intorno a **0,10 $**.

La chiusura a 30 giorni era più spesso negativa: salita 40,00%, discesa 60,00%. Quindi la lettura principale è prudente/debole.

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

- Previsioni già controllate: **26**
- Direzione corretta: **84,21%**
- Errore medio dello scenario centrale: **6,08%**
- Zona rischio toccata: **0,00%**
- Zona rialzo media toccata: **3,85%**
- Prezzo finale dentro lo scenario 10%-90%: **100,00%**

### Dogecoin

- Previsioni già controllate: **26**
- Direzione corretta: **91,30%**
- Errore medio dello scenario centrale: **15,17%**
- Zona rischio toccata: **0,00%**
- Zona rialzo media toccata: **23,08%**
- Prezzo finale dentro lo scenario 10%-90%: **92,31%**

### Solana

- Previsioni già controllate: **26**
- Direzione corretta: **100,00%**
- Errore medio dello scenario centrale: **8,78%**
- Zona rischio toccata: **7,69%**
- Zona rialzo media toccata: **26,92%**
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

Dati ancora insufficienti: previsioni controllate **26** su **30** necessarie.

Per ora si usa solo lo scanner storico grezzo. Quando ci saranno abbastanza previsioni controllate, qui apparirà la lettura autocalibrata.

## Solana

Dati ancora insufficienti: previsioni controllate **26** su **30** necessarie.

Per ora si usa solo lo scanner storico grezzo. Quando ci saranno abbastanza previsioni controllate, qui apparirà la lettura autocalibrata.

## Dogecoin

Dati ancora insufficienti: previsioni controllate **26** su **30** necessarie.

Per ora si usa solo lo scanner storico grezzo. Quando ci saranno abbastanza previsioni controllate, qui apparirà la lettura autocalibrata.

---

# Approfondimento tecnico — Bitcoin (BTC-USD)

## Semaforo: 🟢 VERDE / Favorevole

**Prezzo attuale:** 78.653,26 $

Bitcoin ha un segnale favorevole. La statistica dei casi simili indica più possibilità di salita che di discesa, ma resta comunque una probabilità, non una certezza.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **70,00%**
- Casi negativi dopo 30 giorni: **30,00%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **79,98%**
- Rendimento medio dopo 30 giorni: **14,63%**
- Rendimento centrale dopo 30 giorni: **11,54%**
- Discesa media durante i 30 giorni: **-10,29%**
- Massimo rialzo medio durante i 30 giorni: **25,23%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **90.159,04 $**
- Scenario centrale a 30 giorni: **87.726,91 $**
- Zona di rischio media: **70.559,74 $**
- Zona di rialzo media: **98.494,05 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -11,47% → **69.633,83 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -2,06% → **77.036,02 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: 11,54% → **87.726,91 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 19,60% → **94.069,53 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 40,46% → **110.479,34 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -19,06% → **63.660,30 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -15,01% → **66.849,42 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -9,51% → **71.175,56 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -5,49% → **74.338,71 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: -2,37% → **76.787,98 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 2,06% → **80.275,43 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 11,35% → **87.582,28 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 17,64% → **92.525,71 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 28,99% → **101.453,45 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 49,29% → **117.419,79 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| ETC-USD         | 2020-08-19   | 2020-11-26 |        85.18 |        -4.88 |         -17.07 |           9.66 |
| DOGE-USD        | 2020-08-19   | 2020-11-26 |        84.66 |        38.28 |          -5.26 |          47.29 |
| BNB-USD         | 2018-11-03   | 2019-02-10 |        84.1  |        67.25 |          -4.66 |          67.25 |
| XRP-USD         | 2023-07-30   | 2023-11-06 |        83.68 |       -10.51 |         -18.88 |           0    |
| ETC-USD         | 2023-07-30   | 2023-11-06 |        83.2  |         9.48 |          -1.99 |          12.3  |
| XLM-USD         | 2020-08-19   | 2020-11-26 |        82.94 |       -12.24 |         -24.52 |          23.19 |
| DASH-USD        | 2020-08-19   | 2020-11-26 |        82.8  |        17.57 |          -0.51 |          23.3  |
| CRV-USD         | 2023-08-03   | 2023-11-10 |        82.71 |        18.89 |         -13.32 |          18.89 |
| LTC-USD         | 2018-11-04   | 2019-02-11 |        82.54 |        29.53 |          -3.57 |          34.51 |
| 1INCH-USD       | 2023-08-01   | 2023-11-08 |        82.31 |        11.79 |         -11.52 |          11.79 |

---

# Approfondimento tecnico — Solana (SOL-USD)

## Semaforo: 🟢 VERDE / Favorevole

**Prezzo attuale:** 100,99 $

Solana ha un segnale favorevole. La statistica dei casi simili indica più possibilità di salita che di discesa, ma resta comunque una probabilità, non una certezza.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **62,50%**
- Casi negativi dopo 30 giorni: **37,50%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **73,55%**
- Rendimento medio dopo 30 giorni: **38,18%**
- Rendimento centrale dopo 30 giorni: **3,92%**
- Discesa media durante i 30 giorni: **-13,55%**
- Massimo rialzo medio durante i 30 giorni: **50,68%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **139,55 $**
- Scenario centrale a 30 giorni: **104,95 $**
- Zona di rischio media: **87,31 $**
- Zona di rialzo media: **152,17 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -11,75% → **89,12 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -2,91% → **98,05 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: 3,92% → **104,95 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 19,14% → **120,32 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 94,36% → **196,29 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -21,63% → **79,15 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -15,41% → **85,43 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -11,39% → **89,49 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -8,11% → **92,80 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: -2,48% → **98,49 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 1,21% → **102,21 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 9,06% → **110,14 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 14,68% → **115,81 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 30,72% → **132,02 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 99,16% → **201,13 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| EOS-USD         | 2018-11-18   | 2019-02-25 |        82.99 |        20.31 |          -8.74 |          20.31 |
| ZIL-USD         | 2020-08-21   | 2020-11-28 |        80.66 |       235.51 |           0    |         235.51 |
| VET-USD         | 2020-02-28   | 2020-06-06 |        80.09 |        98.37 |          -0.47 |          98.37 |
| VET-USD         | 2023-08-01   | 2023-11-08 |        79.81 |        18.75 |         -14.56 |          18.75 |
| FTM-USD         | 2020-10-13   | 2021-01-20 |        79.67 |       748.91 |          -8.15 |         748.91 |
| BNB-USD         | 2018-11-08   | 2019-02-15 |        78.83 |        69.95 |          -1.56 |          73.81 |
| ADA-USD         | 2020-08-19   | 2020-11-26 |        77.54 |        14.13 |          -1.36 |          23.88 |
| 1INCH-USD       | 2023-08-01   | 2023-11-08 |        77.19 |        11.79 |         -11.52 |          11.79 |
| NEO-USD         | 2023-07-30   | 2023-11-06 |        75.23 |       -10.02 |         -22.76 |           4.43 |
| MKR-USD         | 2020-02-27   | 2020-06-05 |        75.19 |        -1.72 |          -7.24 |          44.52 |

---

# Approfondimento tecnico — Dogecoin (DOGE-USD)

## Semaforo: 🟡 GIALLO / Incerto

**Prezzo attuale:** 0,09 $

Dogecoin è in una situazione incerta. Lo scanner non vede un vantaggio chiaro né per la salita né per la discesa. In questi casi è meglio non forzare la previsione.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **40,00%**
- Casi negativi dopo 30 giorni: **60,00%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **83,28%**
- Rendimento medio dopo 30 giorni: **2,80%**
- Rendimento centrale dopo 30 giorni: **-4,56%**
- Discesa media durante i 30 giorni: **-13,01%**
- Massimo rialzo medio durante i 30 giorni: **27,69%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **0,09 $**
- Scenario centrale a 30 giorni: **0,08 $**
- Zona di rischio media: **0,08 $**
- Zona di rialzo media: **0,11 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -24,82% → **0,07 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -12,43% → **0,08 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: -4,56% → **0,08 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 4,90% → **0,09 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 23,91% → **0,11 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -30,87% → **0,06 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -17,78% → **0,07 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -9,82% → **0,08 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -5,28% → **0,08 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: -0,97% → **0,09 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 5,80% → **0,09 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 10,63% → **0,10 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 17,61% → **0,10 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 24,51% → **0,11 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 65,37% → **0,14 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| SAND-USD        | 2025-01-19   | 2025-04-28 |        87.69 |         2.06 |          -9.85 |          22.79 |
| YFI-USD         | 2022-04-25   | 2022-08-02 |        86.7  |       -14.5  |         -21.51 |          13.63 |
| ALGO-USD        | 2025-01-19   | 2025-04-28 |        86.06 |        -5.72 |         -13.55 |           9.8  |
| MANA-USD        | 2025-01-20   | 2025-04-29 |        85.89 |        -5.09 |          -5.62 |          24.61 |
| DOT-USD         | 2023-07-30   | 2023-11-06 |        85.81 |        21.64 |          -1.59 |          21.64 |
| KAVA-USD        | 2023-07-30   | 2023-11-06 |        85.52 |         8.9  |          -6.74 |          11.72 |
| EGLD-USD        | 2023-07-20   | 2023-10-27 |        85.31 |        57.59 |           0    |          66.83 |
| FIL-USD         | 2022-04-25   | 2022-08-02 |        84.82 |       -29.26 |         -31.16 |          16.04 |
| DOGE-USD        | 2025-01-20   | 2025-04-29 |        84.33 |        23.02 |          -2.34 |          42.4  |
| INJ-USD         | 2021-05-08   | 2021-08-15 |        83.81 |        20.12 |          -3    |          65.27 |

</details>
<!-- COMPACT_SECTION_END:scanner_full_detail -->

<!-- COMPACT_SECTION_START:market_regime -->
<details>
<summary><strong>🌦️ Market Regime Match</strong></summary>

<!-- MARKET_REGIME_MATCH_START -->
# Market Regime Match Report


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [market_regime_match_report.md](market_regime_match_report.md)

Generated: 2026-08-27 05:32 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | MIXED | 78.653 $ | True | 7.17% | -8.59% | MIXED | 7.17% | -8.59% |
| DOGE-USD | BEAR | 0.08650 $ | False | -13.33% | -15.15% | MIXED | 7.17% | -8.59% |
| SOL-USD | RECOVERY | 100,99 $ | True | 23.15% | -14.48% | MIXED | 7.17% | -8.59% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 70.00% | 11.54% | 19.60% | 40.46% | -9.51% | -19.06% | 17.64% | 28.99% | 49.29% | 67.50% | 12.54% | 32.43% | 93.87% |
| BTC-USD | SAME_BTC_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| BTC-USD | SAME_ASSET_REGIME | 1 | 0.00% | -1.72% | -1.72% | -1.72% | -7.24% | -7.24% | 44.52% | 44.52% | 44.52% | 100.00% | 22.36% | 22.36% | 22.36% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| DOGE-USD | ALL_MATCHES | 40 | 40.00% | -4.56% | 4.90% | 23.91% | -9.82% | -30.87% | 17.61% | 24.51% | 65.37% | 35.00% | -11.11% | 12.19% | 53.31% |
| DOGE-USD | SAME_BTC_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| DOGE-USD | SAME_ASSET_REGIME | 8 | 50.00% | -1.79% | 24.21% | 39.63% | -10.23% | -32.40% | 17.63% | 42.59% | 59.83% | 25.00% | -13.53% | 11.51% | 79.43% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL-USD | ALL_MATCHES | 40 | 62.50% | 3.92% | 19.14% | 94.36% | -11.39% | -21.63% | 14.68% | 30.72% | 99.16% | 72.50% | 22.50% | 57.85% | 130.70% |
| SOL-USD | SAME_BTC_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL-USD | SAME_ASSET_REGIME | 8 | 37.50% | -3.27% | 2.71% | 6.80% | -13.65% | -17.07% | 10.66% | 12.63% | 15.70% | 100.00% | 46.21% | 55.19% | 57.89% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 5 | 60.00% | 29.53% | -6.28% | 67.25% | 60.00% | 26.93% | 114.38% |
| BTC-USD | HISTORICAL_BTC_BULL | 27 | 70.37% | 11.53% | -9.35% | 25.54% | 77.78% | 14.56% | 93.19% |
| BTC-USD | HISTORICAL_BTC_DISTRIBUTION | 7 | 85.71% | 12.12% | -13.32% | 22.40% | 28.57% | -1.95% | 42.82% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 1 | 0.00% | -1.72% | -7.24% | 44.52% | 100.00% | 22.36% | 44.52% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 3 | 33.33% | -7.14% | -16.21% | 24.27% | 0.00% | -16.66% | 24.27% |
| DOGE-USD | HISTORICAL_BTC_BULL | 31 | 45.16% | -1.17% | -8.29% | 24.54% | 45.16% | -6.27% | 48.87% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 6 | 16.67% | -19.59% | -24.39% | 20.84% | 0.00% | -28.72% | 20.84% |
| SOL-USD | HISTORICAL_BTC_BEAR | 5 | 40.00% | -2.00% | -11.54% | 21.08% | 40.00% | -22.47% | 44.56% |
| SOL-USD | HISTORICAL_BTC_BULL | 20 | 70.00% | 9.26% | -11.97% | 56.60% | 70.00% | 18.43% | 115.17% |
| SOL-USD | HISTORICAL_BTC_DISTRIBUTION | 4 | 75.00% | 11.11% | -12.23% | 24.71% | 50.00% | 8.79% | 71.26% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 11 | 54.55% | 3.23% | -10.39% | 32.55% | 100.00% | 54.31% | 89.25% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 25 | 80.00% | 11.79% | -9.92% | 29.84% | 72.00% | 8.80% | 65.84% |
| BTC-USD | HISTORICAL_ASSET_BULL | 9 | 66.67% | 14.13% | -5.26% | 27.19% | 55.56% | 14.99% | 103.40% |
| BTC-USD | HISTORICAL_ASSET_MIXED | 1 | 0.00% | -1.72% | -7.24% | 44.52% | 100.00% | 22.36% | 44.52% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 5 | 40.00% | -4.88% | -17.07% | 17.27% | 60.00% | 22.65% | 45.32% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 8 | 50.00% | -1.79% | -10.23% | 42.59% | 25.00% | -13.53% | 64.06% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 27 | 40.74% | -4.02% | -9.79% | 24.54% | 37.04% | -10.37% | 41.78% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 5 | 20.00% | -24.68% | -27.27% | 11.72% | 40.00% | -20.52% | 16.04% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 20 | 65.00% | 5.07% | -11.29% | 20.50% | 55.00% | 0.36% | 63.43% |
| SOL-USD | HISTORICAL_ASSET_BULL | 9 | 77.78% | 83.57% | -11.26% | 182.90% | 77.78% | 106.74% | 182.90% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 100.00% | 98.37% | -0.47% | 98.37% | 100.00% | 158.76% | 174.79% |
| SOL-USD | HISTORICAL_ASSET_MIXED | 2 | 50.00% | 0.76% | -8.82% | 36.50% | 100.00% | 13.06% | 36.59% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 8 | 37.50% | -3.27% | -13.65% | 12.63% | 100.00% | 46.21% | 60.27% |

## Top regime-adjusted matches

The table below shows the top matches separately for each target, so BTC does not hide SOL and DOGE.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | MKR-USD | 2020-02-27 | 80.67% | RECOVERY | MIXED | SAME_ASSET_ONLY | MIXED | -1.72% | -7.24% | 44.52% | 22.36% | -7.36% | 44.52% |
| BTC-USD | ETC-USD | 2020-08-19 | 85.18% | BULL | RECOVERY | DIFFERENT | MIXED | -4.88% | -17.07% | 9.66% | 22.65% | -17.07% | 45.22% |
| BTC-USD | DOGE-USD | 2020-08-19 | 84.66% | BULL | BULL | DIFFERENT | EXPLOSIVE_60D | 38.28% | -5.26% | 47.29% | 157.94% | -5.26% | 226.62% |
| BTC-USD | BNB-USD | 2018-11-03 | 84.10% | BEAR | BEAR | DIFFERENT | EXPLOSIVE_60D | 67.25% | -4.66% | 67.25% | 92.16% | -4.66% | 114.84% |
| BTC-USD | XRP-USD | 2023-07-30 | 83.68% | BULL | BULL | DIFFERENT | BEARISH_30D | -10.51% | -18.88% | 0.00% | -19.43% | -19.43% | 0.00% |
| BTC-USD | ETC-USD | 2023-07-30 | 83.20% | BULL | BEAR | DIFFERENT | MIXED | 9.48% | -1.99% | 12.30% | 8.74% | -1.99% | 22.62% |
| BTC-USD | XLM-USD | 2020-08-19 | 82.94% | BULL | BULL | DIFFERENT | EXPLOSIVE_60D | -12.24% | -24.52% | 23.19% | 56.48% | -24.52% | 103.40% |
| BTC-USD | DASH-USD | 2020-08-19 | 82.80% | BULL | BULL | DIFFERENT | BULLISH_30D | 17.57% | -0.51% | 23.30% | 14.99% | -5.04% | 62.02% |
| BTC-USD | CRV-USD | 2023-08-03 | 82.71% | DISTRIBUTION | BEAR | DIFFERENT | BULLISH_30D | 18.89% | -13.32% | 18.89% | -13.86% | -14.48% | 18.89% |
| BTC-USD | LTC-USD | 2018-11-04 | 82.54% | BEAR | BEAR | DIFFERENT | EXPLOSIVE_60D | 29.53% | -3.57% | 34.51% | 82.86% | -3.57% | 114.38% |
| DOGE-USD | YFI-USD | 2022-04-25 | 86.70% | RECOVERY | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -14.50% | -21.51% | 13.63% | -25.07% | -25.52% | 13.63% |
| DOGE-USD | DOT-USD | 2023-07-30 | 85.81% | BULL | BEAR | SAME_ASSET_ONLY | HIGH_SPIKE_60D | 21.64% | -1.59% | 21.64% | 49.86% | -1.59% | 85.75% |
| DOGE-USD | EGLD-USD | 2023-07-20 | 85.31% | BULL | BEAR | SAME_ASSET_ONLY | EXPLOSIVE_60D | 57.59% | 0.00% | 66.83% | 148.44% | 0.00% | 154.29% |
| DOGE-USD | OP-USD | 2026-01-16 | 82.68% | BEAR | BEAR | SAME_ASSET_ONLY | MIXED | 3.57% | -4.25% | 37.84% | -16.66% | -27.25% | 37.84% |
| DOGE-USD | MATIC-USD | 2022-04-11 | 82.39% | BEAR | BEAR | SAME_ASSET_ONLY | MIXED | -7.14% | -16.21% | 10.70% | -10.40% | -17.51% | 10.70% |
| DOGE-USD | EOS-USD | 2022-04-26 | 82.19% | RECOVERY | BEAR | SAME_ASSET_ONLY | BULLISH_30D | 31.93% | 0.00% | 56.82% | -1.27% | -2.15% | 56.82% |
| DOGE-USD | NEAR-USD | 2022-05-06 | 82.01% | BEAR | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -13.38% | -36.06% | 0.00% | -46.25% | -46.25% | 0.00% |
| DOGE-USD | KSM-USD | 2022-04-24 | 81.88% | RECOVERY | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -26.09% | -30.83% | 3.57% | -34.28% | -38.46% | 3.57% |
| DOGE-USD | SAND-USD | 2025-01-19 | 87.69% | BULL | BULL | DIFFERENT | MIXED | 2.06% | -9.85% | 22.79% | -20.44% | -22.67% | 22.79% |
| DOGE-USD | ALGO-USD | 2025-01-19 | 86.06% | BULL | BULL | DIFFERENT | MIXED | -5.72% | -13.55% | 9.80% | -24.18% | -30.69% | 9.80% |
| SOL-USD | ZEC-USD | 2020-02-26 | 74.30% | RECOVERY | RECOVERY | SAME_ASSET_ONLY | EXPLOSIVE_60D | -1.66% | -4.67% | 11.66% | 57.83% | -4.67% | 71.76% |
| SOL-USD | ETC-USD | 2020-08-19 | 73.46% | BULL | RECOVERY | SAME_ASSET_ONLY | MIXED | -4.88% | -17.07% | 9.66% | 22.65% | -17.07% | 45.22% |
| SOL-USD | WAVES-USD | 2023-08-04 | 73.27% | BULL | RECOVERY | SAME_ASSET_ONLY | MIXED | 2.14% | -12.76% | 13.61% | 15.52% | -12.76% | 36.03% |
| SOL-USD | ETH-USD | 2020-02-26 | 71.39% | RECOVERY | RECOVERY | SAME_ASSET_ONLY | EXPLOSIVE_60D | -6.28% | -8.78% | 1.23% | 58.04% | -8.78% | 58.04% |
| SOL-USD | LRC-USD | 2020-03-02 | 70.99% | RECOVERY | RECOVERY | SAME_ASSET_ONLY | EXPLOSIVE_60D | 4.44% | -17.07% | 20.58% | 50.29% | -17.07% | 50.55% |
| SOL-USD | QTUM-USD | 2020-02-26 | 70.71% | RECOVERY | RECOVERY | SAME_ASSET_ONLY | MIXED | -8.20% | -13.76% | 0.78% | 42.12% | -13.76% | 43.18% |
| SOL-USD | ADA-USD | 2020-02-26 | 70.38% | RECOVERY | RECOVERY | SAME_ASSET_ONLY | EXPLOSIVE_60D | 12.31% | -15.33% | 12.31% | 54.31% | -15.33% | 66.96% |
| SOL-USD | BNB-USD | 2020-02-26 | 70.00% | RECOVERY | RECOVERY | SAME_ASSET_ONLY | BEARISH_30D | -11.46% | -13.55% | 0.70% | 25.56% | -13.55% | 25.56% |
| SOL-USD | EOS-USD | 2018-11-18 | 82.99% | BEAR | BEAR | DIFFERENT | BULLISH_30D | 20.31% | -8.74% | 20.31% | 32.13% | -8.74% | 62.62% |
| SOL-USD | ZIL-USD | 2020-08-21 | 80.66% | BULL | BULL | DIFFERENT | EXPLOSIVE_60D | 235.51% | 0.00% | 235.51% | 133.98% | 0.00% | 235.51% |

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

Generato: 2026-08-27 05:32 UTC


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
| BTC | 78.653 $ | +5 | COSTRUTTIVO / CONFERMA PARZIALE | STAGE 3 / DISTRIBUZIONE O PAUSA | MASSIMI E MINIMI CRESCENTI | SIGN OF STRENGTH POSSIBILE | MEDIO | SPOT OK / LONG SOLO PRUDENTE SU CONFERMA |
| SOL | 100,99 $ | +7 | COSTRUTTIVO / CONFERMA PARZIALE | STAGE 3 / DISTRIBUZIONE O PAUSA | MASSIMI E MINIMI CRESCENTI | SIGN OF STRENGTH POSSIBILE | MEDIO | TRANCHE PICCOLE / NO LEVA FINCHÉ NON ROMPE CONFERME |
| DOGE | 0.08650 $ | 0 | NEUTRALE / MISTO | STAGE 4 / MARKDOWN | MASSIMI E MINIMI CRESCENTI | ACCUMULO POSSIBILE / RANGE BASSO | MEDIO | STAI ALLA FINESTRA |

## Punteggi per area

| Asset | Trend | Struttura | Momentum | Volume | Prezzo | Candela | Wyckoff | Totale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +1 | +2 | -2 | +2 | 0 | 0 | +2 | +5 |
| SOL | +1 | +2 | -1 | +3 | 0 | 0 | +2 | +7 |
| DOGE | -3 | +2 | 0 | +1 | 0 | 0 | 0 | 0 |

## Livelli tecnici

| Asset | Supporto | Resistenza | Breakout 60g | Breakdown 60g | ATR14 | Rendimento 30g | Rendimento 90g |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 76.029 $ | 79.468 $ | 79.464 $ | 57.748 $ | 3,14% | 23,40% | 6,94% |
| SOL | 85,25 $ | 102,59 $ | 101,75 $ | 64,42 $ | 4,44% | 36,06% | 23,05% |
| DOGE | 0.08189 $ | 0.09169 $ | 0.09998 $ | 0.06797 $ | 5,53% | 22,74% | -13,16% |

## Lettura dettagliata

### BTC

- Prezzo: **78.653 $**
- Score classico: **+5 / 12**
- Verdetto: **COSTRUTTIVO / CONFERMA PARZIALE**
- Azione coerente: **SPOT OK / LONG SOLO PRUDENTE SU CONFERMA**
- Volatilità tecnica locale: **MEDIO** — ATR14 3,14%; distanza supporto 3,43%; distanza resistenza 1,05%

Dettaglio:

- Trend: **+1** — prezzo sopra MA200 daily; breve termine sopra MA20/MA50; MA50 daily in salita; MA200 daily in discesa; STAGE 3 / DISTRIBUZIONE O PAUSA
- Stage weekly: **STAGE 3 / DISTRIBUZIONE O PAUSA** — Prezzo sopra MA30 weekly ma pendenza debole o piatta.
- Struttura: **+2** — MASSIMI E MINIMI CRESCENTI
- Momentum: **-2** — RSI alto 80.4; RSI in peggioramento; MACD sopra signal; istogramma MACD in peggioramento
- Volume: **+2** — OBV sopra media; CMF positivo 0.13; volume ratio 0.95
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **+2** — SIGN OF STRENGTH POSSIBILE. Prezzo nella parte alta del range con flusso volume positivo.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 80.39 |
| MACD histogram | 1396.07129 |
| CMF20 | 0.129 |
| Volume ratio 20 | 0.95 |
| MA20 | 68.927 $ |
| MA50 | 66.061 $ |
| MA100 | 66.136 $ |
| MA200 | 69.173 $ |
| Pendenza MA50 20g | +4,46% |
| Pendenza MA200 60g | -8,79% |
| Bollinger width | 33,97% |
| Bollinger position | 0.86 |

### SOL

- Prezzo: **100,99 $**
- Score classico: **+7 / 12**
- Verdetto: **COSTRUTTIVO / CONFERMA PARZIALE**
- Azione coerente: **TRANCHE PICCOLE / NO LEVA FINCHÉ NON ROMPE CONFERME**
- Volatilità tecnica locale: **MEDIO** — ATR14 4,44%; distanza supporto 18,33%; distanza resistenza 1,69%

Dettaglio:

- Trend: **+1** — prezzo sopra MA200 daily; breve termine sopra MA20/MA50; MA50 daily in salita; MA200 daily in discesa; STAGE 3 / DISTRIBUZIONE O PAUSA
- Stage weekly: **STAGE 3 / DISTRIBUZIONE O PAUSA** — Prezzo sopra MA30 weekly ma pendenza debole o piatta.
- Struttura: **+2** — MASSIMI E MINIMI CRESCENTI
- Momentum: **-1** — RSI alto 82.7; MACD sopra signal; istogramma MACD in peggioramento
- Volume: **+3** — OBV sopra media; CMF positivo 0.16; rialzo con volume sopra media
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **+2** — SIGN OF STRENGTH POSSIBILE. Prezzo nella parte alta del range con flusso volume positivo.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 82.73 |
| MACD histogram | 2.27567 |
| CMF20 | 0.158 |
| Volume ratio 20 | 1.30 |
| MA20 | 82,99 $ |
| MA50 | 78,44 $ |
| MA100 | 76,80 $ |
| MA200 | 81,36 $ |
| Pendenza MA50 20g | +4,53% |
| Pendenza MA200 60g | -14,77% |
| Bollinger width | 38,79% |
| Bollinger position | 0.96 |

### DOGE

- Prezzo: **0.08650 $**
- Score classico: **0 / 12**
- Verdetto: **NEUTRALE / MISTO**
- Azione coerente: **STAI ALLA FINESTRA**
- Volatilità tecnica locale: **MEDIO** — ATR14 5,53%; distanza supporto 5,42%; distanza resistenza 6,21%

Dettaglio:

- Trend: **-3** — prezzo sotto MA200 daily; breve termine sopra MA20/MA50; MA200 daily in discesa; STAGE 4 / MARKDOWN
- Stage weekly: **STAGE 4 / MARKDOWN** — Prezzo sotto MA30 weekly con MA30 in discesa.
- Struttura: **+2** — MASSIMI E MINIMI CRESCENTI
- Momentum: **0** — RSI sano 65.1; RSI in peggioramento; MACD sopra signal; istogramma MACD in peggioramento
- Volume: **+1** — OBV sopra media; CMF neutrale -0.02; volume ratio 0.85
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **0** — ACCUMULO POSSIBILE / RANGE BASSO. Prezzo nella metà bassa del range, ma senza spring confermato.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 65.08 |
| MACD histogram | 0.00165 |
| CMF20 | -0.017 |
| Volume ratio 20 | 0.85 |
| MA20 | 0.07672 $ |
| MA50 | 0.07363 $ |
| MA100 | 0.08033 $ |
| MA200 | 0.08912 $ |
| Pendenza MA50 20g | -0,23% |
| Pendenza MA200 60g | -15,43% |
| Bollinger width | 43,09% |
| Bollinger position | 0.76 |

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

Generato: 2026-08-27 05:32 UTC


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
| BTC | 78.653 $ | Doppio massimo | CANDIDATO | ribassista | n/a | 49.952 $ | n/a | 36,20% | Fib 78,6% TESTATO (0) @ 78.447 $ | NEL RANGE | 74.959 $ |
| SOL | 100,99 $ | Doppio massimo | CANDIDATO | ribassista | n/a | 51,22 $ | n/a | 56,77% | Fib 78,6% RECUPERATO (0) @ 93,12 $ | NEL RANGE | 83,52 $ |
| DOGE | 0.08650 $ | Doppio massimo | CANDIDATO | ribassista | n/a | 0.06214 $ | n/a | 27,26% | Fib 38,2% TESTATO (0) @ 0.08775 $ | NEL RANGE | 0.08157 $ |

## BTC

![Classic visual BTC](classic_visual_BTC.png)

- Pattern principale: **Doppio massimo**
- Stato pattern: **CANDIDATO** (0)
- Famiglia: **ribassista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-06-22 -> 2026-08-09**
- Età formazione: **18 giorni**
- Breakout pattern: **n/a**
- Età breakout: **n/a**
- Neckline: **57.748 $**
- Target teorico: **49.952 $**
- Progresso verso target: **n/a**
- Distanza dalla neckline: **36,20%**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 78,6% TESTATO (0) @ 78.447 $** — Swing DOWN 2026-05-06 82.792 -> 2026-08-14 62.488; livello più vicino 78.6% a 78.447; stato TESTATO; confluenza: nessuna confluenza indipendente.
- Invalidazione: **58.903 $**
- Relazione prezzo/neckline: **sopra neckline**
- Dettaglio: Due massimi simili vicino a 65.544 tra 2026-06-22 e 2026-08-09. Neckline ribassista stimata: 57.748. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 18 giorni. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **NEL RANGE**
- Supporto: **74.959 $**
- Resistenza: **79.468 $**
- Breakout 60g: **79.464 $**
- Breakdown 60g: **57.748 $**
- RSI14: **80.41**
- ATR14: **3,14%**
- Volume ratio 20g: **0.95**
- Rendimento 30g: **+23,43%**
- Rendimento 90g: **+6,96%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Triangolo ascendente possibile | CANDIDATO | 0 | rialzista | n/a | n/a | n/a | n/a | n/a | n/a | n/a | Resistenza quasi piatta e minimi crescenti. Stato: CANDIDATO; il pattern non ha una neckline univoca da usare per il lifecycle. |
| Doppio massimo | CANDIDATO | 0 | ribassista | 62.227 $ | n/a | n/a | 58.946 $ | n/a | 26,40% | 63.471 $ | Due massimi simili a 65.508 $ e 65.402 $. Neckline circa 62.227 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 18 giorni. |
| Doppio minimo | TARGET RAGGIUNTO | 0 | rialzista | 65.402 $ | 2026-08-19 | 8g | 68.577 $ | 417,36% | n/a | 64.094 $ | Due minimi simili a 62.227 $ e 62.488 $. Neckline circa 65.402 $. Breakout neckline: 2026-08-19 (8 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 68.577 $; progresso: 417,36%; prezzo sopra neckline. |

## SOL

![Classic visual SOL](classic_visual_SOL.png)

- Pattern principale: **Doppio massimo**
- Stato pattern: **CANDIDATO** (0)
- Famiglia: **ribassista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-06-22 -> 2026-08-09**
- Età formazione: **18 giorni**
- Breakout pattern: **n/a**
- Età breakout: **n/a**
- Neckline: **64,42 $**
- Target teorico: **51,22 $**
- Progresso verso target: **n/a**
- Distanza dalla neckline: **56,77%**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 78,6% RECUPERATO (0) @ 93,12 $** — Swing DOWN 2026-05-11 98,27 -> 2026-08-16 74,20; livello più vicino 78.6% a 93,12; stato RECUPERATO; confluenza: nessuna confluenza indipendente.
- Invalidazione: **65,71 $**
- Relazione prezzo/neckline: **sopra neckline**
- Dettaglio: Due massimi simili vicino a 77,62 tra 2026-06-22 e 2026-08-09. Neckline ribassista stimata: 64,42. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 18 giorni. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **NEL RANGE**
- Supporto: **83,52 $**
- Resistenza: **127,97 $**
- Breakout 60g: **101,75 $**
- Breakdown 60g: **64,42 $**
- RSI14: **82.79**
- ATR14: **4,44%**
- Volume ratio 20g: **1.30**
- Rendimento 30g: **+36,21%**
- Rendimento 90g: **+23,18%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Triangolo discendente possibile | CANDIDATO | 0 | ribassista | n/a | n/a | n/a | n/a | n/a | n/a | n/a | Massimi decrescenti e supporto quasi piatto. Stato: CANDIDATO; il pattern non ha una neckline univoca da usare per il lifecycle. |
| Doppio massimo | CANDIDATO | 0 | ribassista | 70,69 $ | n/a | n/a | 62,66 $ | n/a | 42,85% | 72,11 $ | Due massimi simili a 78,73 $ e 77,62 $. Neckline circa 70,69 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 18 giorni. |
| Testa e spalle inverso | TARGET RAGGIUNTO | 0 | rialzista | 78,17 $ | 2026-08-19 | 8g | 85,65 $ | 305,17% | n/a | 76,61 $ | Spalla sinistra 73,40 $, testa 70,69 $, spalla destra 74,20 $. Neckline circa 78,17 $. Breakout neckline: 2026-08-19 (8 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 85,65 $; progresso: 305,17%; prezzo sopra neckline. |
| Doppio minimo | TARGET RAGGIUNTO | 0 | rialzista | 78,73 $ | 2026-08-19 | 8g | 84,05 $ | 418,16% | n/a | 77,15 $ | Due minimi simili a 73,40 $ e 74,20 $. Neckline circa 78,73 $. Breakout neckline: 2026-08-19 (8 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 84,05 $; progresso: 418,16%; prezzo sopra neckline. |

## DOGE

![Classic visual DOGE](classic_visual_DOGE.png)

- Pattern principale: **Doppio massimo**
- Stato pattern: **CANDIDATO** (0)
- Famiglia: **ribassista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-07-26 -> 2026-08-11**
- Età formazione: **16 giorni**
- Breakout pattern: **n/a**
- Età breakout: **n/a**
- Neckline: **0.06797 $**
- Target teorico: **0.06214 $**
- Progresso verso target: **n/a**
- Distanza dalla neckline: **27,26%**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 38,2% TESTATO (0) @ 0.08775 $** — Swing UP 2026-08-01 0.06797 -> 2026-08-22 0.09998; livello più vicino 38.2% a 0.08775; stato TESTATO; confluenza: nessuna confluenza indipendente.
- Invalidazione: **0.06933 $**
- Relazione prezzo/neckline: **sopra neckline**
- Dettaglio: Due massimi simili vicino a 0.07380 tra 2026-07-26 e 2026-08-11. Neckline ribassista stimata: 0.06797. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 16 giorni. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **NEL RANGE**
- Supporto: **0.08157 $**
- Resistenza: **0.09169 $**
- Breakout 60g: **0.09998 $**
- Breakdown 60g: **0.06797 $**
- RSI14: **65.28**
- ATR14: **5,52%**
- Volume ratio 20g: **0.85**
- Rendimento 30g: **+22,98%**
- Rendimento 90g: **-12,99%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Doppio massimo | CANDIDATO | 0 | ribassista | 0.06797 $ | n/a | n/a | 0.06214 $ | n/a | 27,26% | 0.06933 $ | Due massimi simili a 0.07380 $ e 0.07286 $. Neckline circa 0.06797 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 16 giorni. |
| Doppio minimo | TARGET RAGGIUNTO | 0 | rialzista | 0.07923 $ | 2026-08-20 | 7g | 0.08952 $ | 70,66% | n/a | 0.07765 $ | Due minimi simili a 0.06961 $ e 0.06895 $. Neckline circa 0.07923 $. Breakout neckline: 2026-08-20 (7 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 0.08952 $; progresso: 70,66%; prezzo sopra neckline. |

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

Generato: 2026-08-27 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [fractal_path_tracker.md](fractal_path_tracker.md)

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-08-27**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-02-11**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **100,99 $**
- Verdetto principale: **ANALOGIA DEBOLE / SCENARIO SECONDARIO**
- Somiglianza strutturale: **+64,58%**
- Aderenza live principale: **+71,13%**
- Errore medio live principale: **14,43%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE SOLO DI CONTESTO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **82**
- Osservazioni inclusive dal bottom: **83**
- Osservazioni da inizio programma/scanner: **56**
- Errore assoluto medio dal bottom: **11,70%**
- Errore assoluto medio da inizio programma: **14,43%**
- Gap firmato medio ultimi 7 giorni: **+9,20%**
- Errore assoluto medio ultimi 7 giorni: **9,20%**
- Gap ultimo giorno: **+17,22%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **+17,22%**
- Gap firmato medio 7g: **+9,20%**
- Errore assoluto medio 7g: **9,20%**
- Variazione recente gap: **+8,15%**
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
| 73 | 2026-08-18 | 2023-02-02 | 77,03 $ | 92,46 $ | -16,69% | da inizio programma |
| 74 | 2026-08-19 | 2023-02-03 | 85,37 $ | 92,37 $ | -7,58% | da inizio programma |
| 75 | 2026-08-20 | 2023-02-04 | 87,64 $ | 91,91 $ | -4,65% | da inizio programma |
| 76 | 2026-08-21 | 2023-02-05 | 93,65 $ | 90,43 $ | +3,57% | da inizio programma |
| 77 | 2026-08-22 | 2023-02-06 | 93,91 $ | 89,66 $ | +4,75% | da inizio programma |
| 78 | 2026-08-23 | 2023-02-07 | 95,44 $ | 91,64 $ | +4,15% | da inizio programma |
| 79 | 2026-08-24 | 2023-02-08 | 98,56 $ | 90,36 $ | +9,07% | da inizio programma |
| 80 | 2026-08-25 | 2023-02-09 | 96,60 $ | 85,95 $ | +12,39% | da inizio programma |
| 81 | 2026-08-26 | 2023-02-10 | 96,60 $ | 85,29 $ | +13,27% | da inizio programma |
| 82 | 2026-08-27 | 2023-02-11 | 100,99 $ | 86,15 $ | +17,22% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-09-03 | 97,07 $ | 113,78 $ | 100,61 $ / 113,78 $ | no | n/a | n/a | n/a |
| 14g | 2026-09-10 | 91,29 $ | 107,01 $ | 100,61 $ / 114,65 $ | no | n/a | n/a | n/a |
| 21g | 2026-09-17 | 88,06 $ | 103,22 $ | 100,61 $ / 114,65 $ | no | n/a | n/a | n/a |
| 28g | 2026-09-24 | 81,28 $ | 95,27 $ | 93,22 $ / 114,65 $ | no | n/a | n/a | n/a |
| 35g | 2026-10-01 | 106,22 $ | 124,52 $ | 93,22 $ / 126,63 $ | no | n/a | n/a | n/a |
| 42g | 2026-10-08 | 108,31 $ | 126,96 $ | 93,22 $ / 130,83 $ | no | n/a | n/a | n/a |
| 49g | 2026-10-15 | 111,92 $ | 131,19 $ | 93,22 $ / 131,50 $ | no | n/a | n/a | n/a |
| 56g | 2026-10-22 | 110,09 $ | 129,05 $ | 93,22 $ / 131,50 $ | no | n/a | n/a | n/a |
| 63g | 2026-10-29 | 119,43 $ | 140,00 $ | 93,22 $ / 140,77 $ | no | n/a | n/a | n/a |
| 70g | 2026-11-05 | 109,58 $ | 128,45 $ | 93,22 $ / 140,77 $ | no | n/a | n/a | n/a |
| 77g | 2026-11-12 | 115,22 $ | 135,06 $ | 93,22 $ / 140,77 $ | no | n/a | n/a | n/a |
| 84g | 2026-11-19 | 113,86 $ | 133,47 $ | 93,22 $ / 140,77 $ | no | n/a | n/a | n/a |
| 91g | 2026-11-26 | 105,51 $ | 123,68 $ | 93,22 $ / 140,77 $ | no | n/a | n/a | n/a |
| 98g | 2026-12-03 | 106,87 $ | 125,27 $ | 93,22 $ / 140,77 $ | no | n/a | n/a | n/a |
| 105g | 2026-12-10 | 105,84 $ | 124,07 $ | 93,22 $ / 140,77 $ | no | n/a | n/a | n/a |
| 112g | 2026-12-17 | 106,66 $ | 125,02 $ | 93,22 $ / 140,77 $ | no | n/a | n/a | n/a |
| 119g | 2026-12-24 | 101,83 $ | 119,37 $ | 93,22 $ / 140,77 $ | no | n/a | n/a | n/a |
| 126g | 2026-12-31 | 104,43 $ | 122,41 $ | 93,22 $ / 140,77 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 42 | 38,10% | 10,84% | 13,15% |
| 14g | 35 | 31,43% | 17,10% | 12,03% |
| 21g | 30 | 20,00% | 24,24% | 13,38% |
| 28g | 23 | 47,83% | 22,93% | 13,33% |
| 35g | 16 | 68,75% | 17,90% | 11,87% |
| 42g | 9 | 100,00% | 9,41% | 9,20% |
| 49g | 2 | 100,00% | 0,20% | n/a |
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

Ultima lettura salvata: **2026-08-27** — SOL 100,99 $, gap +17,22%, somiglianza +64,58%.

Nel report principale lascio solo il link, così non diventa troppo lungo.

<!-- SOL_BTC_FRACTAL_HISTORY_END -->

</details>
<!-- COMPACT_SECTION_END:fractal_path -->

<!-- COMPACT_SECTION_START:exchange_microstructure -->
<details>
<summary><strong>🏦 Dati exchange, liquidità e leva</strong></summary>

<!-- EXCHANGE_MICROSTRUCTURE_START -->
# Dati exchange, liquidità e leva

Generato: 2026-08-27 05:33 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [exchange_microstructure_report.md](exchange_microstructure_report.md)

Questo modulo legge Kraken Futures, Bitget Futures e KuCoin Futures come nucleo derivati. OKX e Coinbase vengono raccolti come fonti ausiliarie non pesate.
Non modifica la formula matematica di RSI, Fibonacci o Wyckoff: controlla se quei segnali sono sostenuti da acquisti, vendite, OI, funding e liquidità.

**Limite importante:** questo nucleo non assume disponibile un feed pubblico completo delle liquidazioni. La componente liquidazioni resta neutrale; le zone future restano stime di pressione, non dati certi delle singole posizioni.

Diagnostica completa: [exchange_source_diagnostics.md](exchange_source_diagnostics.md)

## Sintesi

| Asset | Prezzo | Exchange | Segnale candidato | Peso Global | Bias exchange | Confidenza | Copertura | Funding 8h eq. | OI 24h | Taker flow (campione/4h) | Book 0,5% | Liq long campione | Liq short campione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 78.648 $ | 3 | 0 | 0 | LEGGERMENTE POSITIVA / NON PESATA | BASSA | 100% | +0,0025% | -0,57% | 2,39 | -0,55% | 0 $ | 0 $ |
| SOL | 100,90 $ | 3 | 0 | 0 | LEGGERMENTE POSITIVA / NON PESATA | MEDIA | 100% | +0,0034% | +1,70% | 0,96 | +10,07% | 0 $ | 0 $ |
| DOGE | 0.08647 $ | 3 | 0 | 0 | MISTA / NEUTRALE | BASSA | 100% | +0,0080% | -1,20% | 1,07 | -4,58% | 0 $ | 0 $ |

Il segnale candidato è limitato a **±1**, ma il peso nel Global resta **0** finché il tracker a 7 giorni non raggiunge 30 controlli, almeno 55% di accuratezza e return corretto direzione positivo. Un singolo muro o funding non basta.

La colonna taker usa un campione recente nel primo run. Dopo almeno 3 fotografie distribuite su almeno 45 minuti viene sostituita automaticamente dalla media intraday 4h.

## Dati separati per exchange

| Asset | Exchange | Stato | Funding 8h eq. | Open interest | Taker flow | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | Kraken | OK | +0,0081% | 151,26 mln $ | 3,99 | -2,44% |
| BTC | Bitget | OK | +0,0010% | 2,77 mld $ | 5,24 | +12,17% |
| BTC | Kucoin | OK | +0,0007% | 1,62 mld $ | 0,21 | -4,68% |
| SOL | Kraken | OK | +0,0150% | 34,76 mln $ | 101,68 | +8,19% |
| SOL | Bitget | OK | +0,0100% | 422,39 mln $ | 1,00 | +41,76% |
| SOL | Kucoin | OK | +0,0100% | 280,64 mln $ | 1,55 | +5,61% |
| DOGE | Kraken | OK | -0,0022% | 4,83 mln $ | 1,63 | -22,49% |
| DOGE | Bitget | OK | +0,0097% | 112,10 mln $ | 26,60 | +5,68% |
| DOGE | Kucoin | OK | +0,0050% | 133,22 mln $ | 0,20 | -21,21% |

Kraken, Bitget e KuCoin contribuiscono a funding normalizzato, open interest, trade aggressivi e order book. Non viene inventato un long/short ratio pubblico né un feed completo delle liquidazioni.

## Conferme per indicatori tecnici

### BTC

- Score grezzo exchange: **+2,00**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 1, accuratezza +100,00%.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 1, bear 0, divergenze 0.
- Flusso taker/order book: **+1,75**.
- OI/funding/basis: **+0,00**.
- Affollamento long/short: **+0,00**.
- Liquidazioni: **NON PESATE / FEED COMPLETO NON ASSUNTO DISPONIBILE**.
- **Wyckoff:** Fase Wyckoff non abbastanza chiara per una conferma exchange.
- **Fibonacci:** Livello Fibonacci soltanto testato: order book e taker flow non bastano ancora per dichiararlo tenuto o perso.
- **RSI:** RSI alto ma sostenuto da acquisti e leva non estrema: momentum ancora credibile.
- **Pattern:** I pattern candidati restano non operativi: i dati exchange possono solo preparare la conferma.
- **Breakout/breakdown:** Prezzo non abbastanza vicino a un livello chiave o flusso non netto.
- **Mappa liquidità attuale:** muro bid: n/a; muro ask: n/a

![Microstruttura exchange BTC](exchange_microstructure_BTC.png)

### SOL

- Score grezzo exchange: **+2,25**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 2, accuratezza +0,00%.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 2, bear 1, divergenze 0.
- Flusso taker/order book: **+1,75**.
- OI/funding/basis: **+0,00**.
- Affollamento long/short: **+0,00**.
- Liquidazioni: **NON PESATE / FEED COMPLETO NON ASSUNTO DISPONIBILE**.
- **Wyckoff:** Fase Wyckoff non abbastanza chiara per una conferma exchange.
- **Fibonacci:** Fibonacci recuperato con acquisti/assorbimento coerenti: conferma positiva.
- **RSI:** RSI alto ma sostenuto da acquisti e leva non estrema: momentum ancora credibile.
- **Pattern:** I pattern candidati restano non operativi: i dati exchange possono solo preparare la conferma.
- **Breakout/breakdown:** Prezzo non abbastanza vicino a un livello chiave o flusso non netto.
- **Mappa liquidità attuale:** muro bid: n/a; muro ask: n/a

![Microstruttura exchange SOL](exchange_microstructure_SOL.png)

### DOGE

- Score grezzo exchange: **+0,75**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 5, accuratezza +60,00%.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 1, bear 1, divergenze 0.
- Flusso taker/order book: **+0,75**.
- OI/funding/basis: **+0,00**.
- Affollamento long/short: **+0,00**.
- Liquidazioni: **NON PESATE / FEED COMPLETO NON ASSUNTO DISPONIBILE**.
- **Wyckoff:** Fase Wyckoff debole ma senza conferma exchange netta.
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
| BTC | +70,00% | +11,54% | 1 | +0,00% | RACCOLTA DATI | 0,00 | +70,00% | +11,54% |
| SOL | +62,50% | +3,92% | 1 | +100,00% | RACCOLTA DATI | 0,00 | +62,50% | +3,92% |
| DOGE | +40,00% | -4,56% | 2 | +100,00% | RACCOLTA DATI | 0,00 | +40,00% | -4,56% |

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

Generato: 2026-08-27 05:33 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [exchange_signal_tracker_report.md](exchange_signal_tracker_report.md)

Questo tracker verifica se il segnale candidato exchange ±1 anticipa correttamente la direzione del prezzo a 1/3/7/14/30 giorni.
Il peso Global resta 0 finché l'orizzonte 7g non ha almeno 30 controlli, accuratezza almeno 55% e return corretto direzione positivo. L'overlay a 30g ha un gate separato.

Controlli maturati completati in questa esecuzione: **12**.

## Ultime fotografie giornaliere

| Data | Asset | Prezzo | Versione | Calibrazione | Candidato | Peso Global | Score raw | Confidenza | Taker 4h | OI 24h | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08-27 | BTC | 78.647,60 | V2.1.3 | OK | 0 | 0 | 2,00 | BASSA | 2,39 | -0,57% | -0,55% |
| 2026-08-27 | DOGE | 0.08647 | V2.1.3 | OK | 0 | 0 | 0,75 | BASSA | 1,07 | -1,20% | -4,58% |
| 2026-08-27 | SOL | 100,90 | V2.1.3 | OK | 0 | 0 | 2,25 | MEDIA | 0,96 | +1,70% | +10,07% |
| 2026-08-26 | BTC | 78.654,90 | V2.1.3 | OK | 0 | 0 | 2,00 | BASSA | 1,31 | -1,63% | -1,02% |
| 2026-08-26 | DOGE | 0.08606 | V2.1.3 | OK | 0 | 0 | -0,25 | BASSA | 0,79 | -1,68% | -1,23% |
| 2026-08-26 | SOL | 96,32 | V2.1.3 | OK | 1 | 0 | 3,25 | MEDIA | 3,71 | -4,29% | +9,82% |
| 2026-08-25 | BTC | 80.493,33 | V2.1.3 | OK | 1 | 0 | 3,00 | MEDIA | 3,56 | +2,28% | -1,39% |
| 2026-08-25 | DOGE | 0.09243 | V2.1.3 | OK | 0 | 0 | 2,00 | BASSA | 1,20 | -4,18% | -0,09% |
| 2026-08-25 | SOL | 101,92 | V2.1.3 | OK | 1 | 0 | 3,25 | ALTA | 1,32 | +7,13% | +5,91% |

## Accuratezza direzionale

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 3 | +66,67% | +0,12% | -0,41% | +0,59% | FEEDBACK RAPIDO |
| BTC | 3g | 2 | +100,00% | +2,38% | -1,18% | +4,13% | FEEDBACK RAPIDO |
| BTC | 7g | 1 | +100,00% | +1,35% | -1,18% | +3,82% | FEEDBACK RAPIDO |
| BTC | 14g | 1 | +0,00% | -2,63% | -3,44% | +3,82% | FEEDBACK RAPIDO |
| BTC | 30g | 1 | +0,00% | -0,24% | -3,45% | +3,82% | FEEDBACK RAPIDO |
| SOL | 1g | 5 | +60,00% | +0,93% | +0,43% | +3,39% | FEEDBACK RAPIDO |
| SOL | 3g | 3 | +33,33% | +0,40% | -2,47% | +5,55% | FEEDBACK RAPIDO |
| SOL | 7g | 2 | +0,00% | -3,56% | -4,18% | +1,44% | FEEDBACK RAPIDO |
| SOL | 14g | 2 | +50,00% | +8,38% | -5,94% | +13,89% | FEEDBACK RAPIDO |
| SOL | 30g | 1 | +100,00% | +8,60% | -9,55% | +9,55% | FEEDBACK RAPIDO |
| DOGE | 1g | 7 | +57,14% | +1,05% | -0,16% | +2,16% | FEEDBACK RAPIDO |
| DOGE | 3g | 7 | +42,86% | +1,91% | -3,12% | +7,00% | FEEDBACK RAPIDO |
| DOGE | 7g | 5 | +60,00% | +3,28% | -0,81% | +11,24% | FEEDBACK RAPIDO |
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

**SOL** — SOL: i futures sembrano più vulnerabili verso una discesa improvvisa. Non significa che deve scendere, ma se rompe sotto può accelerare. Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale.

**DOGE** — DOGE: i futures non danno una lettura chiara. Non si vede uno sbilanciamento forte né long né short. Qui pesa di più il report frattale.

| Asset | Prezzo | Funding | OI 24h | Long/Short | Lettura futures | Forza |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 78.653 $ | +0.0060% | -10.17% | 1.81 | Misto | 1/5 |
| SOL | 100,99 $ | +0.0100% | -34.34% | 2.79 | Rischio sotto | 2/5 |
| DOGE | 0.08650 $ | +0.0028% | -12.64% | 3.48 | Misto | 1/5 |

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

Generato: 2026-08-27 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [rsi_multitimeframe_divergence_report.md](rsi_multitimeframe_divergence_report.md)

Il modulo confronta prezzo e RSI 14 sui pivot confermati **daily e weekly**. Riconosce divergenze regolari e nascoste, segnali in formazione, invalidazioni e semplice conferma del momentum.

**Peso operativo: 0.** Non modifica il Global Confluence, non cambia le soglie del Paper Trading e non apre né blocca operazioni. I risultati vengono misurati prima di qualsiasi futura decisione sul peso.

## Sintesi corrente

| Asset   | Daily              | Stato D    | Weekly             | Stato W       | Lettura weekly                                                                                                              |   Peso |
|:--------|:-------------------|:-----------|:-------------------|:--------------|:----------------------------------------------------------------------------------------------------------------------------|-------:|
| BTC     | Hidden bullish     | CONFERMATA | Conferma rialzista | CONTESTO      | Prezzo e RSI stanno salendo insieme: momentum rialzista confermato.                                                         |      0 |
| SOL     | Conferma rialzista | CONTESTO   | Hidden bearish     | CONFERMATA    | Hidden bearish confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto. |      0 |
| DOGE    | Conferma rialzista | CONTESTO   | Hidden bearish     | IN_FORMAZIONE | Hidden bearish in formazione: il secondo estremo non è ancora un pivot confermato. Peso operativo sempre 0.                 |      0 |

## Dettaglio dei pivot

| Asset   | TF   | Tipo               | Stato         | Prezzo / RSI      | Pivot confrontati                                                   | Δ prezzo contesto   | Δ RSI contesto   |   Peso |
|:--------|:-----|:-------------------|:--------------|:------------------|:--------------------------------------------------------------------|:--------------------|:-----------------|-------:|
| BTC     | 1D   | Hidden bullish     | CONFERMATA    | 78.638 $ / 80,39  | 2026-08-03 62.227 $ / RSI 47,40 → 2026-08-14 62.488 $ / RSI 42,71   | n/a                 | n/a              |      0 |
| BTC     | 1W   | Conferma rialzista | CONTESTO      | 78.638 $ / 57,44  | n/a                                                                 | +21,56%             | 17,70            |      0 |
| SOL     | 1D   | Conferma rialzista | CONTESTO      | 100,88 $ / 82,73  | n/a                                                                 | +33,57%             | 30,56            |      0 |
| SOL     | 1W   | Hidden bearish     | CONFERMATA    | 100,88 $ / 57,46  | 2026-05-17 98,27 $ / RSI 38,29 → 2026-07-05 83,81 $ / RSI 42,25     | n/a                 | n/a              |      0 |
| DOGE    | 1D   | Conferma rialzista | CONTESTO      | 0.08630 $ / 65,05 | n/a                                                                 | +24,01%             | 20,65            |      0 |
| DOGE    | 1W   | Hidden bearish     | IN_FORMAZIONE | 0.08630 $ / 45,98 | 2026-05-17 0.11825 $ / RSI 44,25 → 2026-08-23 0.09998 $ / RSI 49,72 | n/a                 | n/a              |      0 |

### BTC

- **1D — Hidden bullish / CONFERMATA**: Hidden bullish confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto.
- **1W — Conferma rialzista / CONTESTO**: Prezzo e RSI stanno salendo insieme: momentum rialzista confermato.

### SOL

- **1D — Conferma rialzista / CONTESTO**: Prezzo e RSI stanno salendo insieme: momentum rialzista confermato.
- **1W — Hidden bearish / CONFERMATA**: Hidden bearish confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto.

### DOGE

- **1D — Conferma rialzista / CONTESTO**: Prezzo e RSI stanno salendo insieme: momentum rialzista confermato.
- **1W — Hidden bearish / IN_FORMAZIONE**: Hidden bearish in formazione: il secondo estremo non è ancora un pivot confermato. Peso operativo sempre 0.

## Tracker live delle divergenze confermate

Viene salvato un solo evento per combinazione di asset, timeframe, tipo e coppia di pivot. Gli esiti vengono controllati dopo 30, 60, 90 e 180 giorni.

- Eventi indipendenti salvati: **8**.
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

Generato: 2026-08-27 05:32 UTC


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
| BTC | 78.653 $ | 10 | RIALZISTA TECNICO | Trend rialzista | Momentum in miglioramento | Compressione / triangolo | 0 | 0 / TESTATO | Doppio minimo / TARGET RAGGIUNTO | Doppio massimo / CANDIDATO | 62.488 | 82.792 |
| SOL | 100,99 $ | 9 | RIALZISTA TECNICO | Trend rialzista | Momentum in miglioramento | Compressione / triangolo | 0 | 0 / RECUPERATO | Doppio minimo / TARGET RAGGIUNTO | Doppio massimo / CANDIDATO | 74,20 | 127,97 |
| DOGE | 0.08650 $ | 2 | NEUTRALE / MISTO | Trend misto | Momentum misto | Struttura rialzista con massimi e minimi crescenti | 0 | 0 / TESTATO | Triplo minimo / TARGET RAGGIUNTO | Doppio massimo / CANDIDATO | 0.06895 | 0.09998 |

## Riepilogo ciclo di vita pattern

| Asset   | Doppio minimo    | Triplo minimo    | Adam/Eve Bottom                        | Doppio massimo   | Triplo massimo   | Adam/Eve Top                 |   Punteggio pattern |
|:--------|:-----------------|:-----------------|:---------------------------------------|:-----------------|:-----------------|:-----------------------------|--------------------:|
| BTC | TARGET RAGGIUNTO | TARGET RAGGIUNTO | Adam and Eve Bottom — TARGET RAGGIUNTO | CANDIDATO | CANDIDATO | Adam and Eve Top — CANDIDATO | 0 |
| SOL | TARGET RAGGIUNTO | TARGET RAGGIUNTO | Adam and Eve Bottom — TARGET RAGGIUNTO | CANDIDATO | CANDIDATO | Adam and Eve Top — CANDIDATO | 0 |
| DOGE | TARGET RAGGIUNTO | TARGET RAGGIUNTO | Adam and Eve Bottom — TARGET RAGGIUNTO | CANDIDATO | CANDIDATO | Adam and Eve Top — CANDIDATO | 0 |

## Indicatori tecnici

| Asset   |   RSI 14 |   Istogramma MACD | MA20    | MA50    | MA200   | Pendenza MA50 20g   | Pendenza MA200 60g   | Rendimento 30g   | Rendimento 90g   |
|:--------|---------:|------------------:|:--------|:--------|:--------|:--------------------|:---------------------|:-----------------|:-----------------|
| BTC | 80.41 | 1397.01 | 68.928 | 66.062 | 69.173 | 4,40% | -8,59% | 23,14% | 7,20% |
| SOL | 82.79 | 2.28269 | 83,00 | 78,44 | 81,36 | 4,42% | -14,48% | 37,03% | 23,26% |
| DOGE | 65.28 | 0.00166 | 0.07673 | 0.07364 | 0.08912 | 0,14% | -15,15% | 22,26% | -13,19% |

## Dettaglio asset

### BTC

- Prezzo: **78.653 $**
- Punteggio tecnico: **10 / 12**
- Verdetto: **RIALZISTA TECNICO**
- Trend: **Trend rialzista** (3)
- Momentum: **Momentum in miglioramento** (2)
- Volume: **Volume da accumulazione** (2)
- Struttura: **Compressione / triangolo** (0)
  - Dettaglio struttura: Ultimi minimi: 6.223e+04 -> 6.249e+04. Ultimi massimi: 6.691e+04 -> 6.54e+04.
- Divergenza: **Divergenza rialzista nascosta RSI** (1)
- Fase Wyckoff candidata: **Markup / fase rialzista** (2)
  - Dettaglio Wyckoff: Prezzo sopra MA200, MA50 in salita e trend a 30 giorni positivo.
- Fibonacci automatico: **TESTATO** (0)
  - Swing DOWN 2026-05-06 82.792 -> 2026-08-14 62.488; livello più vicino 78.6% a 78.447; stato TESTATO; confluenza: nessuna confluenza indipendente.
- Punteggio pattern: **0**
  - rialzista dominante: Doppio minimo (TARGET RAGGIUNTO, 0); ribassista dominante: Doppio massimo (CANDIDATO, 0).
- Supporto più vicino: **62.488**
- Resistenza più vicina: **82.792**

Pattern classici e ciclo di vita:

- Doppio minimo: **TARGET RAGGIUNTO** (0)
  - Due minimi simili vicino a 62.201 tra 2026-06-18 e 2026-08-14. Neckline stimata: 66.910. Breakout neckline: 2026-08-19 (8 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 71.619; progresso corrente: 249,38%. Relazione prezzo/neckline: sopra neckline.
  - neckline 66.910; target 71.619; breakout 2026-08-19 (8g); progresso 249,38%; prezzo sopra neckline.
- Triplo minimo: **TARGET RAGGIUNTO** (0)
  - Tre minimi simili vicino a 62.201 dal 2026-06-18 al 2026-08-14. Neckline stimata: 66.910. Breakout neckline: 2026-08-19 (8 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 71.619; progresso corrente: 249,38%. Relazione prezzo/neckline: sopra neckline.
  - neckline 66.910; target 71.619; breakout 2026-08-19 (8g); progresso 249,38%; prezzo sopra neckline.
- Adam and Eve Bottom: **TARGET RAGGIUNTO** (0)
  - Pattern Adam and Eve Bottom vicino a 59.109 dal 2026-06-05 al 2026-08-14. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 67.248. Breakout neckline: 2026-08-19 (8 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 75.387; progresso corrente: 140,13%. Relazione prezzo/neckline: sopra neckline.
  - neckline 67.248; target 75.387; breakout 2026-08-19 (8g); progresso 140,13%; prezzo sopra neckline.
- Doppio massimo: **CANDIDATO** (0)
  - Due massimi simili vicino a 65.544 tra 2026-06-22 e 2026-08-09. Neckline ribassista stimata: 57.748. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 18 giorni.
  - neckline 57.748; target 49.952; distanza dalla neckline 36,20%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 65.544 dal 2026-06-22 al 2026-08-09. Neckline ribassista stimata: 57.748. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 18 giorni.
  - neckline 57.748; target 49.952; distanza dalla neckline 36,20%; prezzo sopra neckline.
- Adam and Eve Top: **CANDIDATO** (0)
  - Pattern Adam and Eve Top vicino a 67.248 dal 2026-06-15 al 2026-07-21. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 57.748. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 37 giorni.
  - neckline 57.748; target 48.247; distanza dalla neckline 36,20%; prezzo sopra neckline.

### SOL

- Prezzo: **100,99 $**
- Punteggio tecnico: **9 / 12**
- Verdetto: **RIALZISTA TECNICO**
- Trend: **Trend rialzista** (3)
- Momentum: **Momentum in miglioramento** (2)
- Volume: **Volume da accumulazione** (2)
- Struttura: **Compressione / triangolo** (0)
  - Dettaglio struttura: Ultimi minimi: 70.69 -> 74.2. Ultimi massimi: 78.73 -> 77.62.
- Divergenza: **Nessuna** (0)
- Fase Wyckoff candidata: **Markup / fase rialzista** (2)
  - Dettaglio Wyckoff: Prezzo sopra MA200, MA50 in salita e trend a 30 giorni positivo.
- Fibonacci automatico: **RECUPERATO** (0)
  - Swing DOWN 2026-05-11 98,27 -> 2026-08-16 74,20; livello più vicino 78.6% a 93,12; stato RECUPERATO; confluenza: nessuna confluenza indipendente.
- Punteggio pattern: **0**
  - rialzista dominante: Doppio minimo (TARGET RAGGIUNTO, 0); ribassista dominante: Doppio massimo (CANDIDATO, 0).
- Supporto più vicino: **74,20**
- Resistenza più vicina: **127,97**

Pattern classici e ciclo di vita:

- Doppio minimo: **TARGET RAGGIUNTO** (0)
  - Due minimi simili vicino a 73,40 tra 2026-07-17 e 2026-08-16. Neckline stimata: 78,73. Breakout neckline: 2026-08-19 (8 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 84,05; progresso corrente: 418,16%. Relazione prezzo/neckline: sopra neckline.
  - neckline 78,73; target 84,05; breakout 2026-08-19 (8g); progresso 418,16%; prezzo sopra neckline.
- Triplo minimo: **TARGET RAGGIUNTO** (0)
  - Tre minimi simili vicino a 70,69 dal 2026-07-17 al 2026-08-16. Neckline stimata: 78,73. Breakout neckline: 2026-08-19 (8 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 86,76; progresso corrente: 277,20%. Relazione prezzo/neckline: sopra neckline.
  - neckline 78,73; target 86,76; breakout 2026-08-19 (8g); progresso 277,20%; prezzo sopra neckline.
- Adam and Eve Bottom: **TARGET RAGGIUNTO** (0)
  - Pattern Adam and Eve Bottom vicino a 67,92 dal 2026-06-19 al 2026-08-01. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 83,81. Breakout neckline: 2026-08-19 (8 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 99,70; progresso corrente: 108,12%. Relazione prezzo/neckline: sopra neckline.
  - neckline 83,81; target 99,70; breakout 2026-08-19 (8g); progresso 108,12%; prezzo sopra neckline.
- Doppio massimo: **CANDIDATO** (0)
  - Due massimi simili vicino a 77,62 tra 2026-06-22 e 2026-08-09. Neckline ribassista stimata: 64,42. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 18 giorni.
  - neckline 64,42; target 51,22; distanza dalla neckline 56,77%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 78,88 dal 2026-07-15 al 2026-08-09. Neckline ribassista stimata: 70,69. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 18 giorni.
  - neckline 70,69; target 62,51; distanza dalla neckline 42,85%; prezzo sopra neckline.
- Adam and Eve Top: **CANDIDATO** (0)
  - Pattern Adam and Eve Top vicino a 77,62 dal 2026-06-15 al 2026-08-09. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 64,42. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 18 giorni.
  - neckline 64,42; target 51,22; distanza dalla neckline 56,77%; prezzo sopra neckline.

### DOGE

- Prezzo: **0.08650 $**
- Punteggio tecnico: **2 / 12**
- Verdetto: **NEUTRALE / MISTO**
- Trend: **Trend misto** (1)
- Momentum: **Momentum misto** (0)
- Volume: **Volume da accumulazione** (1)
- Struttura: **Struttura rialzista con massimi e minimi crescenti** (2)
  - Dettaglio struttura: Ultimi minimi: 0.06835 -> 0.06895. Ultimi massimi: 0.07286 -> 0.09998.
- Divergenza: **Nessuna** (0)
- Fase Wyckoff candidata: **Markdown / fase ribassista** (-2)
  - Dettaglio Wyckoff: Prezzo sotto MA200 con trend a 90 giorni ancora debole.
- Fibonacci automatico: **TESTATO** (0)
  - Swing UP 2026-08-01 0.06797 -> 2026-08-22 0.09998; livello più vicino 38.2% a 0.08775; stato TESTATO; confluenza: nessuna confluenza indipendente.
- Punteggio pattern: **0**
  - rialzista dominante: Triplo minimo (TARGET RAGGIUNTO, 0); ribassista dominante: Doppio massimo (CANDIDATO, 0).
- Supporto più vicino: **0.06895**
- Resistenza più vicina: **0.09998**

Pattern classici e ciclo di vita:

- Doppio minimo: **TARGET RAGGIUNTO** (0)
  - Due minimi simili vicino a 0.06829 tra 2026-07-24 e 2026-08-12. Neckline stimata: 0.07380. Breakout neckline: 2026-08-19 (8 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 0.07931; progresso corrente: 230,38%. Relazione prezzo/neckline: sopra neckline.
  - neckline 0.07380; target 0.07931; breakout 2026-08-19 (8g); progresso 230,38%; prezzo sopra neckline.
- Triplo minimo: **TARGET RAGGIUNTO** (0)
  - Tre minimi simili vicino a 0.06835 dal 2026-06-30 al 2026-08-12. Neckline stimata: 0.07923. Breakout neckline: 2026-08-20 (7 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 0.09012; progresso corrente: 66,75%. Relazione prezzo/neckline: sopra neckline.
  - neckline 0.07923; target 0.09012; breakout 2026-08-20 (7g); progresso 66,75%; prezzo sopra neckline.
- Adam and Eve Bottom: **TARGET RAGGIUNTO** (0)
  - Pattern Adam and Eve Bottom vicino a 0.06829 dal 2026-07-24 al 2026-08-06. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 0.07380. Breakout neckline: 2026-08-19 (8 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 0.07931; progresso corrente: 230,38%. Relazione prezzo/neckline: sopra neckline.
  - neckline 0.07380; target 0.07931; breakout 2026-08-19 (8g); progresso 230,38%; prezzo sopra neckline.
- Doppio massimo: **CANDIDATO** (0)
  - Due massimi simili vicino a 0.07380 tra 2026-07-26 e 2026-08-11. Neckline ribassista stimata: 0.06797. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 16 giorni.
  - neckline 0.06797; target 0.06214; distanza dalla neckline 27,26%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 0.07923 dal 2026-07-04 al 2026-08-11. Neckline ribassista stimata: 0.06797. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 16 giorni.
  - neckline 0.06797; target 0.05671; distanza dalla neckline 27,26%; prezzo sopra neckline.
- Adam and Eve Top: **CANDIDATO** (0)
  - Pattern Adam and Eve Top vicino a 0.07923 dal 2026-07-04 al 2026-08-11. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 0.06797. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 16 giorni.
  - neckline 0.06797; target 0.05671; distanza dalla neckline 27,26%; prezzo sopra neckline.

## Fibonacci automatico

Il modulo seleziona uno swing recente tramite pivot confermati. Un semplice tocco vale 0: Fibonacci pesa al massimo ±1 soltanto quando il livello è tenuto, perso, recuperato o respinto e coincide con almeno un livello tecnico indipendente.

| Asset   | Swing                         | 23,6%   | 38,2%   | 50,0%   | 61,8%   | 78,6%   | Livello vicino   | Stato      | Confluenza                      |   Score |
|:--------|:------------------------------|:--------|:--------|:--------|:--------|:--------|:-----------------|:-----------|:--------------------------------|--------:|
| BTC | DOWN 2026-05-06 -> 2026-08-14 | 67.280 | 70.244 | 72.640 | 75.036 | 78.447 | 78.6% / 78.447 | TESTATO | nessuna confluenza indipendente | 0 |
| SOL | DOWN 2026-05-11 -> 2026-08-16 | 79,88 | 83,40 | 86,24 | 89,07 | 93,12 | 78.6% / 93,12 | RECUPERATO | nessuna confluenza indipendente | 0 |
| DOGE | UP 2026-08-01 -> 2026-08-22 | 0.09243 | 0.08775 | 0.08398 | 0.08020 | 0.07482 | 38.2% / 0.08775 | TESTATO | nessuna confluenza indipendente | 0 |

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

- **BTC**: 26/30 previsioni controllate su 54 fatte. Stato: **RACCOLTA DATI**.
- **SOL**: 26/30 previsioni controllate su 54 fatte. Stato: **RACCOLTA DATI**.
- **DOGE**: 26/30 previsioni controllate su 54 fatte. Stato: **RACCOLTA DATI**.

| Asset | Previsioni fatte | Controllate | Progresso | In attesa | Stato | Prossimo controllo |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 54 | 26 | 26/30 [█████████░] | 28 | RACCOLTA DATI | 2026-08-28 / tra 1 giorno |
| SOL | 54 | 26 | 26/30 [█████████░] | 28 | RACCOLTA DATI | 2026-08-28 / tra 1 giorno |
| DOGE | 54 | 26 | 26/30 [█████████░] | 28 | RACCOLTA DATI | 2026-08-28 / tra 1 giorno |

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

Generato: 2026-08-27 05:33 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [data_quality_coherence_report.md](data_quality_coherence_report.md)

Questo controllo non modifica punteggi o decisioni. Verifica che tutti i moduli usino lo stesso prezzo corrente e che le nuove regole Technical/Classic Visual siano integre.

## Stato finale: **OK**

## Prezzo unico per modulo

| Modulo                  | Asset   | Campo             | Stato   | Prezzo snapshot   | Prezzo modulo   | Differenza   |
|:------------------------|:--------|:------------------|:--------|:------------------|:----------------|:-------------|
| Scanner                 | BTC     | current_price     | OK      | 78.653 $          | 78.653 $        | +0,0000%     |
| Scanner                 | DOGE    | current_price     | OK      | 0.08650 $         | 0.08650 $       | -0,0000%     |
| Scanner                 | SOL     | current_price     | OK      | 100,99 $          | 100,99 $        | -0,0000%     |
| Scanner Forecast        | BTC     | current_price     | OK      | 78.653 $          | 78.653 $        | +0,0000%     |
| Scanner Forecast        | SOL     | current_price     | OK      | 100,99 $          | 100,99 $        | -0,0000%     |
| Scanner Forecast        | DOGE    | current_price     | OK      | 0.08650 $         | 0.08650 $       | -0,0000%     |
| Technical Structure     | BTC     | price             | OK      | 78.653 $          | 78.653 $        | +0,0000%     |
| Technical Structure     | SOL     | price             | OK      | 100,99 $          | 100,99 $        | -0,0000%     |
| Technical Structure     | DOGE    | price             | OK      | 0.08650 $         | 0.08650 $       | -0,0000%     |
| Classic Technical       | BTC     | price             | OK      | 78.653 $          | 78.653 $        | +0,0000%     |
| Classic Technical       | SOL     | price             | OK      | 100,99 $          | 100,99 $        | -0,0000%     |
| Classic Technical       | DOGE    | price             | OK      | 0.08650 $         | 0.08650 $       | -0,0000%     |
| Classic Visual          | BTC     | price             | OK      | 78.653 $          | 78.653 $        | +0,0000%     |
| Classic Visual          | SOL     | price             | OK      | 100,99 $          | 100,99 $        | -0,0000%     |
| Classic Visual          | DOGE    | price             | OK      | 0.08650 $         | 0.08650 $       | -0,0000%     |
| Exchange Microstructure | BTC     | price             | OK      | 78.653 $          | 78.648 $        | -0,0072%     |
| Exchange Microstructure | SOL     | price             | OK      | 100,99 $          | 100,90 $        | -0,0891%     |
| Exchange Microstructure | DOGE    | price             | OK      | 0.08650 $         | 0.08647 $       | -0,0347%     |
| RSI top-cycle           | SOL     | current_price     | OK      | 100,99 $          | 100,99 $        | -0,0000%     |
| RSI top-cycle           | SOL     | current_price     | OK      | 100,99 $          | 100,99 $        | -0,0000%     |
| Frattale BTC/SOL        | SOL     | sol_current_price | OK      | 100,99 $          | 100,99 $        | -0,0000%     |
| Fractal path            | SOL     | current_price     | OK      | 100,99 $          | 100,99 $        | -0,0000%     |

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
