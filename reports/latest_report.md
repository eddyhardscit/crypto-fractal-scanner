<!-- COMPACT_REPORT_HEADER_START -->
> **Vista compatta:** Decisione operativa, Global Confluence e cambiamenti giornalieri restano aperti. Tocca il titolo di una sezione per mostrare o nascondere i dettagli.  
> Tutte le tabelle e tutti i dati restano nel file: copiando il Markdown raw viene copiato tutto.
<!-- COMPACT_REPORT_HEADER_END -->

<!-- COMPACT_SECTION_START:decision -->
<details open>
<summary><strong>🧭 Decisione operativa — da leggere per prima</strong></summary>

<!-- DECISION_REPORT_START -->

# Decisione operativa sintetica

Generato: 2026-08-24 05:32 UTC

Report separato completo: [decision_report.md](decision_report.md)

Sintesi automatica dello scanner: l'azione spot viene copiata direttamente dal Global Confluence; long, short e rischio restano filtri separati e più prudenti.

| Asset | Global | Direzione | Spot | Long leva | Short leva | Max long | Max short | Rischio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +6 | BULLISH | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE | LONG PRUDENTE | NO SHORT | max 2x isolated | nessuna | MEDIO |
| SOL | +6 | NEUTRALE / COSTRUTTIVO | HOLD / TRANCHE PICCOLE, NO LEVA | NO LONG A LEVA | NO SHORT | nessuna | nessuna | MOLTO ALTO |
| DOGE | +4 | NEUTRALE / COSTRUTTIVO | SOLO TRANCHE PICCOLE / NO LEVA | NO LONG A LEVA | NO SHORT | nessuna | nessuna | MOLTO ALTO |

## Lettura immediata

- **BTC**: Global = **+6**, spot = **ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE**, long = **LONG PRUDENTE**, short = **NO SHORT**, rischio = **MEDIO**.
- **SOL**: Global = **+6**, spot = **HOLD / TRANCHE PICCOLE, NO LEVA**, long = **NO LONG A LEVA**, short = **NO SHORT**, rischio = **MOLTO ALTO**.
- **DOGE**: Global = **+4**, spot = **SOLO TRANCHE PICCOLE / NO LEVA**, long = **NO LONG A LEVA**, short = **NO SHORT**, rischio = **MOLTO ALTO**.

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
- Conferme: Prima resistenza sopra 77.991; conferma del doppio minimo sopra 66.910.
- Invalidazioni: Sotto 62.488 il quadro tecnico peggiora.

### SOL

- Global Confluence: **+6**
- Confluenza: **MODERATAMENTE POSITIVA**
- Bias Global: **Costruttivo prudente**
- Direzione decisionale: **NEUTRALE / COSTRUTTIVO**
- Azione spot dal Global: **HOLD / TRANCHE PICCOLE, NO LEVA**
- Long leva: **NO LONG A LEVA**
- Short leva: **NO SHORT**
- Rischio: **MOLTO ALTO**
- Conferme: Doppio minimo target raggiunto finché mantiene 78,73; nuova conferma tecnica sopra 98,27; milestone analogiche 101,80 / 116,76, valide soltanto se rientra anche il gap frattale.
- Invalidazioni: Allarmi sotto 82,77 / 74,20 / 62,19.

### DOGE

- Global Confluence: **+4**
- Confluenza: **MODERATAMENTE POSITIVA**
- Bias Global: **Costruttivo prudente**
- Direzione decisionale: **NEUTRALE / COSTRUTTIVO**
- Azione spot dal Global: **SOLO TRANCHE PICCOLE / NO LEVA**
- Long leva: **NO LONG A LEVA**
- Short leva: **NO SHORT**
- Rischio: **MOLTO ALTO**
- Conferme: Sopra 0.11825 migliora; sopra 0.06933 viene invalidato il pattern ribassista dominante.
- Invalidazioni: Sotto 0.06895 il rischio ribassista aumenta.

## Nota semplice

- **Spot** = usa la stessa azione del Global Confluence, senza una seconda mappatura che possa produrre frasi diverse.
- **Zona alta storica** = zona dove non inseguire troppo; può essere zona da prendere profitto.
- **Zona bassa storica** = zona di rischio; con leva la liquidazione non dovrebbe stare lì vicino.
- **BTC leva** = nessun long a leva finché il prezzo snapshot non supera **67.248 $**; sotto quella soglia resta solo l'azione spot indicata dal Global.
- **Lifecycle EMA200** = per SOL resta solo contesto, peso Global 0; score interno 4; EMA200 circa 111,29 $; upside verso EMA200 +18,63%. Non autorizza leva e non aggiunge punti automatici.
- **NO LONG** non significa automaticamente **SHORT**. Lo short ha senso solo se il quadro è bearish o se lo spike viene spesso scaricato.
- Per SOL, se il Global è da **+3 in su**, la decisione non deve diventare bearish solo perché lo scanner grezzo a 30 giorni è incerto.

<!-- DECISION_REPORT_END -->

<!-- PAPER_TRADING_START -->
# Paper trading automatico KuCoin

Generato: 2026-08-24T05:33:00+00:00


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [paper_trading_report.md](paper_trading_report.md)

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-08-24T05:05:29+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-08-24T05:05:29+00:00 | 2026-08-24T05:05:29+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-08-24T04:45:00+00:00 | 2026-08-24T04:45:00+00:00 | 5,6 min | 25,0 min | OK |
| 60m | 12 | 2026-08-24T04:00:00+00:00 | 2026-08-24T04:00:00+00:00 | 5,6 min | 45,0 min | OK |
| 240m | 12 | 2026-08-24T00:00:00+00:00 | 2026-08-24T00:00:00+00:00 | 1,09 h | 1,00 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1H Fast V3 No Esports Mfe Lock V1 | ENA | 60m | LONG | 7,00 | 4,50 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 No Esports Long Only V1 | SUI | 60m | LONG | 4,68 | 4,50 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 No Esports V1 | SUI | 60m | LONG | 4,68 | 4,50 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 Cap75 V1 | SUI | 60m | LONG | 4,68 | 4,50 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Principale 4H | TRUMP | 240m | LONG | 8,25 | 6,00 | 0,00 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | HYPE | 240m | LONG | 7,75 | 6,00 | 0,00 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | XRP | 240m | LONG | 6,25 | 6,00 | 0,00 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | ETH | 240m | LONG | 5,90 | 6,00 | 0,10 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | DOGE | 240m | LONG | 5,54 | 6,00 | 0,46 | STALE_CANDLE | 1,09 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | SOL | 240m | LONG | 3,34 | 6,00 | 2,66 | STALE_CANDLE | 1,09 h | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | BTC | 240m | LONG | 3,25 | 6,00 | 2,75 | STALE_CANDLE | 1,09 h | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| 1H Balanced Long No Rhv V1 | ENA | 60m | LONG | 7,00 | 5,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Bilanciata 1H V3 Filtered | ENA | 60m | LONG | 7,00 | 6,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Fast Score 6 75 V1 | ENA | 60m | LONG | 7,00 | 6,00 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Score 6 75 No Trend Up V1 | ENA | 60m | LONG | 7,00 | 6,00 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Score 6 75 Cost Aware V1 | ENA | 60m | LONG | 7,00 | 6,00 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Long Btc 1 3 Cap75 V1 | ENA | 60m | LONG | 7,00 | 4,50 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast No Pepe V1 | ENA | 60m | LONG | 7,00 | 4,50 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Tp2 V1 | ENA | 60m | LONG | 7,00 | 4,50 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Rapida 1H V3 Filtered | ENA | 60m | LONG | 7,00 | 4,50 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 Cap75 V1 | ENA | 60m | LONG | 7,00 | 4,50 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 Long Only V1 | ENA | 60m | LONG | 7,00 | 4,50 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 No Esports V1 | ENA | 60m | LONG | 7,00 | 4,50 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 No Esports Long Only V1 | ENA | 60m | LONG | 7,00 | 4,50 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.813,31 | -1,87% | €64,97 | €3.000,00 | 2,17% | 6 | 51 | 37,25% | 0,87 | 6,39% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 51 | 2129 | PRIME INDICAZIONI | 100 (mancano 49) |

- Trade del Principale 4H chiusi: **51**; win rate **37,25%**; profit factor **0,87**.
- Expectancy: **€-3,76** per trade; P&L netto: **€-191,70**; max drawdown: **6,39%**.
- Valutazione: **Si può osservare la direzione, ma il risultato resta fragile.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 6 | €9.813,31 | €700,92 | €2.102,75 | €194,16 | €6,11 |
| TEST | Benchmark Donchian breakout 1H | 3 | €11.378,40 | €2.377,87 | €4.755,73 | €165,71 | €-61,71 |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | 6 | €11.325,48 | €1.224,43 | €3.673,28 | €225,61 | €-39,94 |
| TEST | Combo Trend Side Regime Guard V1 | 4 | €11.191,12 | €983,31 | €1.966,61 | €170,14 | €-42,94 |
| TEST | Donchian 1H Gb20 120R V1 | 3 | €11.110,51 | €2.321,88 | €4.643,76 | €161,81 | €-60,26 |
| TEST | Scanner Top 5 Long 1H | 5 | €11.012,97 | €1.128,26 | €2.256,51 | €220,54 | €-32,78 |
| TEST | Main Side Regime Guard V1 | 6 | €10.837,07 | €677,33 | €2.031,99 | €163,22 | €46,06 |
| TEST | 1H Fast No Pepe V1 | 6 | €10.708,56 | €1.285,81 | €3.857,42 | €214,19 | €-49,09 |
| TEST | Combo Adaptive | 6 | €10.681,29 | €1.366,21 | €2.732,43 | €212,26 | €-33,59 |
| TEST | Combo Adaptive Long Only V1 | 3 | €10.584,00 | €1.266,54 | €2.533,08 | €152,56 | €-29,84 |
| TEST | Combo Adaptive Side Regime Guard V1 | 4 | €10.493,30 | €702,19 | €1.404,39 | €112,68 | €-4,50 |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | 6 | €10.445,90 | €1.478,68 | €4.436,03 | €208,92 | €-44,16 |
| TEST | Scanner Top5 Btc Tp3 V1 | 5 | €10.433,40 | €1.264,39 | €2.528,78 | €208,30 | €-9,06 |
| TEST | Scanner Top5 Btc Runner25 V1 | 5 | €10.427,30 | €1.263,65 | €2.527,30 | €208,18 | €-9,06 |
| TEST | Rapida 1H V3 Filtered | 6 | €10.378,79 | €1.469,18 | €4.407,53 | €207,58 | €-43,88 |
| TEST | Scanner Top10 Long | 5 | €10.347,42 | €2.774,91 | €5.549,82 | €206,57 | €-30,61 |
| TEST | Ampia 4H | 7 | €10.333,13 | €998,50 | €1.997,00 | €206,18 | €1,28 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 0 | €10.300,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top 5 + forza BTC 1H | 5 | €10.281,84 | €1.053,65 | €2.107,29 | €205,89 | €-30,58 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 0 | €10.271,73 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Tp2 V1 | 7 | €10.270,10 | €1.223,91 | €3.671,73 | €205,42 | €-33,04 |
| TEST | 1H Fast V3 Nohigh Range Only V1 | 0 | €10.247,95 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 0 | €10.239,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 0 | €10.235,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Main Dynamic Asset Selector V1 | 1 | €10.198,33 | €141,85 | €425,56 | €51,07 | €-14,72 |
| TEST | Sol Donchian 4H | 0 | €10.196,46 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 0 | €10.185,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V2 | 0 | €10.182,21 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 4H | 1 | €10.168,90 | €330,98 | €661,97 | €50,82 | €4,72 |
| TEST | Sol Donchian 1H | 0 | €10.156,88 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Score 6 75 Range Only V1 | 0 | €10.149,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 0 | €10.145,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | 0 | €10.140,84 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 1H | 0 | €10.138,40 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Partial 1R V1 | 4 | €10.124,24 | €674,61 | €1.349,21 | €100,68 | €-22,13 |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | 6 | €10.099,73 | €1.463,70 | €4.391,10 | €202,01 | €-14,56 |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 0 | €10.099,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 1H | 0 | €10.083,25 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 4H | 0 | €10.070,19 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H V3 Filtered | 6 | €10.069,51 | €1.077,05 | €3.231,16 | €202,98 | €-13,21 |
| TEST | Btc Donchian 1H | 0 | €10.067,96 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 No Esports Long Only V1 | 6 | €10.053,56 | €1.193,26 | €3.579,78 | €201,07 | €-41,85 |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 0 | €10.048,77 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Bollinger 1H | 0 | €10.046,17 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €10.045,08 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V1 | 0 | €10.043,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Balanced Short Trend Down Strict V1 | 0 | €10.035,46 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 4H | 0 | €10.029,45 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 4H | 1 | €10.029,09 | €356,10 | €712,19 | €50,12 | €5,07 |
| TEST | Scalp RSI Long 20 · prudente · 5x | 0 | €10.028,67 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Nohigh Cap75 V1 | 0 | €10.028,66 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 1H | 1 | €10.027,52 | €349,20 | €1.047,59 | €50,20 | €-10,86 |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | 2 | €10.020,91 | €545,14 | €1.090,27 | €100,72 | €-45,84 |
| TEST | Btc Ema 4H | 0 | €10.019,41 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €50 · 15x | 0 | €10.017,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €50 · 15x | 0 | €10.015,51 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | 0 | €10.013,82 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 0 | €10.009,02 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 0 | €10.008,92 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Ema 1H | 1 | €10.008,83 | €248,90 | €746,70 | €50,09 | €-8,41 |
| TEST | Scalp RSI Short 85 · €10 · 15x | 0 | €10.003,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 0 | €10.003,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €10 · 15x | 0 | €10.003,10 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Continuation V1 | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €10 · 15x | 0 | €9.999,33 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €10 · 15x | 0 | €9.997,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €50 · 15x | 0 | €9.996,64 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 0 | €9.995,23 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · prudente · 5x | 0 | €9.991,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €10 · 15x | 0 | €9.990,45 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €50 · 15x | 0 | €9.988,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 0 | €9.987,48 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 4H | 0 | €9.981,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · prudente · 5x | 0 | €9.980,94 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 4H | 0 | €9.965,81 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · prudente · 5x | 0 | €9.952,43 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €50 · 15x | 0 | €9.952,25 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top15 Long | 7 | €9.951,56 | €1.654,66 | €3.309,32 | €200,40 | €-53,72 |
| TEST | Scanner Top20 Long | 7 | €9.951,56 | €1.654,66 | €3.309,32 | €200,40 | €-53,72 |
| TEST | Btc Ema 1H | 0 | €9.941,95 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.939,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Ema 4H | 1 | €9.929,80 | €487,73 | €975,47 | €49,56 | €19,30 |
| TEST | Combo Adaptive Regime V1 | 2 | €9.924,39 | €720,33 | €1.440,66 | €98,38 | €-15,46 |
| TEST | Doge Donchian 1H | 0 | €9.911,95 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Adaptive 1H | 0 | €9.897,54 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Quality7 Regime V1 | 2 | €9.894,87 | €538,28 | €1.076,56 | €99,45 | €-45,26 |
| TEST | Sol Adaptive 1H | 1 | €9.884,90 | €344,23 | €1.032,69 | €49,48 | €-10,70 |
| TEST | Sol Bollinger 1H | 0 | €9.873,88 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 No Esports V1 | 5 | €9.871,67 | €1.305,96 | €3.917,88 | €197,46 | €-37,16 |
| TEST | Scanner Top5 Btc Guard V1 | 5 | €9.868,12 | €864,47 | €1.728,95 | €150,71 | €-6,89 |
| TEST | Eth Ema 1H | 0 | €9.866,33 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Scanner | 5 | €9.864,56 | €1.010,88 | €2.021,77 | €197,54 | €-29,34 |
| TEST | Combo Adaptive Quality7 V1 | 4 | €9.848,66 | €1.604,00 | €3.208,01 | €194,94 | €-47,65 |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 0 | €9.837,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 0 | €9.817,34 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Forza relativa 1H V2 | 3 | €9.801,99 | €843,27 | €1.686,53 | €97,62 | €-40,24 |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | 0 | €9.779,10 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 0 | €9.762,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Balanced Long No Rhv V1 | 5 | €9.754,28 | €1.495,69 | €4.487,08 | €194,67 | €-34,00 |
| TEST | Eth Donchian 1H | 0 | €9.730,51 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 0 | €9.723,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Bollinger 1H | 0 | €9.703,71 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | 6 | €9.665,74 | €1.188,02 | €2.376,05 | €146,41 | €-26,32 |
| TEST | Scanner Top5 Btc Mfe V1 | 5 | €9.638,72 | €987,74 | €1.975,48 | €193,02 | €-28,67 |
| TEST | Scanner Top5 Btc Guard Mfe V1 | 5 | €9.638,62 | €844,37 | €1.688,74 | €147,20 | €-6,73 |
| TEST | Global Confluence puro 1H | 0 | €9.628,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Score 6 75 V1 | 1 | €9.626,03 | €350,27 | €1.050,81 | €48,13 | €-0,21 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 0 | €9.579,83 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H V2 | 4 | €9.576,13 | €879,98 | €2.639,95 | €141,92 | €-1,49 |
| TEST | 1H Fast V3 Long Only V1 | 7 | €9.550,64 | €1.328,96 | €3.986,89 | €191,01 | €-38,57 |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | 6 | €9.547,78 | €1.247,34 | €2.494,67 | €144,18 | €21,79 |
| TEST | 1H Balanced V3 Long Only V1 | 5 | €9.525,12 | €1.008,33 | €3.025,00 | €189,53 | €-12,21 |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | 0 | €9.517,55 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Nohigh V1 | 0 | €9.435,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Trend | 5 | €9.434,55 | €988,41 | €1.976,81 | €143,49 | €-6,17 |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | 0 | €9.389,68 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom10 Short | 2 | €9.384,56 | €885,87 | €1.771,73 | €97,35 | €0,00 |
| TEST | Scanner Bottom15 Short | 2 | €9.384,56 | €885,87 | €1.771,73 | €97,35 | €0,00 |
| TEST | Scanner Bottom20 Short | 2 | €9.384,56 | €885,87 | €1.771,73 | €97,35 | €0,00 |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | 5 | €9.381,70 | €1.210,83 | €2.421,66 | €138,78 | €22,05 |
| TEST | Master Adaptive Runner25 V1 | 1 | €9.378,18 | €34,77 | €69,54 | €8,34 | €0,00 |
| TEST | Master Adaptive Gb20 Be V1 | 0 | €9.372,49 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | 1 | €9.370,10 | €340,96 | €1.022,87 | €46,85 | €-0,20 |
| TEST | Master Adaptive Gb20 Partial V1 | 0 | €9.362,52 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive No Alt V1 | 0 | €9.354,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Cap75 V1 | 3 | €9.347,45 | €1.212,30 | €3.636,90 | €140,27 | €-5,54 |
| TEST | Master Adaptive V1 | 0 | €9.326,30 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Expanded V1 | 1 | €9.319,82 | €197,50 | €395,01 | €47,40 | €0,00 |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | 2 | €9.319,54 | €879,76 | €1.759,52 | €96,67 | €0,00 |
| TEST | Scanner Bottom5 Short Profit Lock V1 | 2 | €9.305,36 | €878,42 | €1.756,85 | €96,53 | €0,00 |
| TEST | Master Adaptive Gb20 Loss Cap V1 | 1 | €9.252,08 | €195,70 | €391,41 | €45,67 | €0,00 |
| TEST | Scanner Bottom 5 Short 1H | 2 | €9.233,75 | €871,66 | €1.743,33 | €95,79 | €0,00 |
| TEST | Master Adaptive Gb20 V1 | 0 | €9.202,39 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Btc Le3 V1 | 6 | €9.193,60 | €1.129,99 | €2.259,98 | €139,26 | €-25,04 |
| TEST | Benchmark trend following EMA 1H | 5 | €9.188,59 | €1.686,73 | €3.373,47 | €138,42 | €-36,80 |
| TEST | Combo Adaptive Mfe Trail | 4 | €9.185,50 | €957,91 | €1.915,82 | €91,47 | €-16,11 |
| TEST | Bilanciata 1H V1 | 0 | €9.150,69 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Mean Reversion | 0 | €9.114,32 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Strict3 V1 | 0 | €9.056,84 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Runner25 V1 | 0 | €8.964,11 | €0,00 | €0,00 | €0,00 | €0,00 |
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
| PRINCIPALE | Principale 4H | Confluenza trend | €9.813,31 | €-191,70 | 51 | 51 | 37,25% | 0,87 | €-3,76 | 6,39% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €11.378,40 | €1.442,38 | 96 | 96 | 50,00% | 1,68 | €15,02 | 4,69% |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | Momentum / breakout | €11.325,48 | €1.368,06 | 130 | 130 | 55,38% | 1,54 | €10,52 | 4,41% |
| TEST | Combo Trend Side Regime Guard V1 | Combo Trend | €11.191,12 | €1.235,99 | 100 | 100 | 57,00% | 1,71 | €12,36 | 4,57% |
| TEST | Donchian 1H Gb20 120R V1 | Donchian breakout 20 barre | €11.110,51 | €1.172,98 | 64 | 64 | 50,00% | 1,94 | €18,33 | 4,69% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €11.012,97 | €1.047,57 | 129 | 129 | 50,39% | 1,41 | €8,12 | 8,85% |
| TEST | Main Side Regime Guard V1 | Confluenza trend | €10.837,07 | €792,57 | 33 | 33 | 54,55% | 2,27 | €24,02 | 2,40% |
| TEST | 1H Fast No Pepe V1 | Momentum / breakout | €10.708,56 | €760,43 | 192 | 192 | 50,52% | 1,21 | €3,96 | 6,39% |
| TEST | Combo Adaptive | Combo Adaptive | €10.681,29 | €717,21 | 139 | 139 | 46,04% | 1,31 | €5,16 | 7,91% |
| TEST | Combo Adaptive Long Only V1 | Combo Adaptive | €10.584,00 | €615,76 | 111 | 111 | 49,55% | 1,26 | €5,55 | 6,25% |
| TEST | Combo Adaptive Side Regime Guard V1 | Combo Adaptive | €10.493,30 | €499,27 | 108 | 108 | 49,07% | 1,23 | €4,62 | 8,68% |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | Momentum / breakout V3 Filtered | €10.445,90 | €492,81 | 177 | 177 | 51,98% | 1,16 | €2,78 | 9,50% |
| TEST | Scanner Top5 Btc Tp3 V1 | Scanner Top 5 + forza BTC | €10.433,40 | €444,40 | 95 | 95 | 44,21% | 1,21 | €4,68 | 11,78% |
| TEST | Scanner Top5 Btc Runner25 V1 | Scanner Top 5 + forza BTC | €10.427,30 | €438,28 | 99 | 99 | 44,44% | 1,20 | €4,43 | 12,06% |
| TEST | Rapida 1H V3 Filtered | Momentum / breakout V3 Filtered | €10.378,79 | €425,40 | 221 | 221 | 45,70% | 1,10 | €1,92 | 9,48% |
| TEST | Scanner Top10 Long | Scanner Top10 Long | €10.347,42 | €381,65 | 113 | 113 | 51,33% | 1,19 | €3,38 | 10,31% |
| TEST | Ampia 4H | Confluenza trend | €10.333,13 | €333,13 | 51 | 51 | 35,29% | 1,29 | €6,53 | 4,45% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | Momentum / breakout V3 Filtered | €10.300,05 | €300,05 | 33 | 33 | 48,48% | 2,04 | €9,09 | 2,01% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €10.281,84 | €314,11 | 116 | 116 | 46,55% | 1,13 | €2,71 | 11,27% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | Momentum / breakout V3 Filtered | €10.271,73 | €271,73 | 22 | 22 | 50,00% | 1,74 | €12,35 | 1,72% |
| TEST | 1H Fast Tp2 V1 | Momentum / breakout | €10.270,10 | €305,40 | 207 | 207 | 41,06% | 1,08 | €1,48 | 6,56% |
| TEST | 1H Fast V3 Nohigh Range Only V1 | Momentum / breakout V3 Filtered | €10.247,95 | €247,95 | 41 | 41 | 46,34% | 1,25 | €6,05 | 3,97% |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | Momentum / breakout V3 Filtered | €10.239,20 | €239,20 | 17 | 17 | 52,94% | 4,50 | €14,07 | 1,01% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | Momentum / breakout V3 Filtered | €10.235,18 | €235,18 | 20 | 20 | 50,00% | 1,90 | €11,76 | 2,73% |
| TEST | Main Dynamic Asset Selector V1 | Confluenza trend | €10.198,33 | €213,35 | 12 | 12 | 41,67% | 1,74 | €17,78 | 1,68% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €10.196,46 | €196,46 | 6 | 6 | 50,00% | 2,73 | €32,74 | 1,05% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | Momentum / breakout V3 Filtered | €10.185,37 | €185,37 | 22 | 22 | 40,91% | 1,57 | €8,43 | 2,27% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €10.182,21 | €182,21 | 45 | 40 | 46,67% | 1,16 | €4,05 | 3,89% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €10.168,90 | €164,84 | 6 | 6 | 50,00% | 2,46 | €27,47 | 1,01% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €10.156,88 | €156,88 | 12 | 12 | 50,00% | 1,63 | €13,07 | 2,77% |
| TEST | 1H Fast Score 6 75 Range Only V1 | Momentum / breakout | €10.149,62 | €149,62 | 38 | 38 | 44,74% | 1,14 | €3,94 | 3,35% |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | Momentum / breakout V3 Filtered | €10.145,12 | €145,12 | 44 | 44 | 45,45% | 1,20 | €3,30 | 2,91% |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | Momentum / breakout V3 Filtered | €10.140,84 | €140,84 | 63 | 63 | 44,44% | 1,10 | €2,24 | 5,24% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.138,40 | €138,40 | 5 | 5 | 80,00% | 3,42 | €27,68 | 0,85% |
| TEST | Combo Adaptive Partial 1R V1 | Combo Adaptive | €10.124,24 | €147,49 | 139 | 139 | 46,04% | 1,06 | €1,06 | 8,69% |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | Momentum / breakout | €10.099,73 | €117,74 | 50 | 50 | 48,00% | 1,11 | €2,35 | 3,73% |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | Momentum / breakout V3 Filtered | €10.099,04 | €99,04 | 55 | 55 | 54,55% | 1,12 | €1,80 | 3,59% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €10.083,25 | €83,25 | 6 | 6 | 66,67% | 1,77 | €13,88 | 1,13% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €10.070,19 | €70,19 | 2 | 2 | 50,00% | 2,39 | €35,09 | 0,96% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €10.069,51 | €85,29 | 145 | 145 | 43,45% | 1,03 | €0,59 | 9,12% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €10.067,96 | €67,96 | 8 | 8 | 62,50% | 1,41 | €8,50 | 1,49% |
| TEST | 1H Fast V3 No Esports Long Only V1 | Momentum / breakout V3 Filtered | €10.053,56 | €97,64 | 136 | 136 | 46,32% | 1,03 | €0,72 | 10,60% |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | Momentum / breakout V3 Filtered | €10.048,77 | €48,77 | 23 | 23 | 43,48% | 1,12 | €2,12 | 3,05% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €10.046,17 | €46,17 | 9 | 9 | 55,56% | 1,19 | €5,13 | 1,89% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €10.045,08 | €45,08 | 28 | 28 | 46,43% | 1,40 | €1,61 | 0,33% |
| TEST | Rapida 1H V1 | Momentum / breakout | €10.043,28 | €43,28 | 78 | 78 | 34,62% | 1,02 | €0,55 | 6,76% |
| TEST | 1H Balanced Short Trend Down Strict V1 | Confluenza trend | €10.035,46 | €35,46 | 13 | 13 | 38,46% | 1,13 | €2,73 | 1,80% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.029,45 | €29,45 | 2 | 2 | 50,00% | 1,54 | €14,72 | 0,82% |
| TEST | Sol Ema 4H | Trend following EMA | €10.029,09 | €24,73 | 7 | 7 | 28,57% | 1,11 | €3,53 | 2,27% |
| TEST | Scalp RSI Long 20 · prudente · 5x | Inversione RSI estrema 15m | €10.028,67 | €28,67 | 9 | 9 | 55,56% | 1,80 | €3,19 | 0,36% |
| TEST | 1H Fast Nohigh Cap75 V1 | Momentum / breakout | €10.028,66 | €28,66 | 122 | 122 | 43,44% | 1,01 | €0,23 | 7,10% |
| TEST | Sol Ema 1H | Trend following EMA | €10.027,52 | €39,53 | 13 | 13 | 38,46% | 1,10 | €3,04 | 3,33% |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | Combo Adaptive | €10.020,91 | €67,52 | 36 | 36 | 50,00% | 1,08 | €1,88 | 4,21% |
| TEST | Btc Ema 4H | Trend following EMA | €10.019,41 | €19,41 | 3 | 3 | 33,33% | 1,19 | €6,47 | 1,76% |
| TEST | Scalp RSI Short 85 · €50 · 15x | Inversione RSI estrema 15m | €10.017,98 | €17,98 | 5 | 5 | 60,00% | 1,69 | €3,60 | 0,31% |
| TEST | Scalp RSI Short 80 · €50 · 15x | Inversione RSI estrema 15m | €10.015,51 | €15,51 | 15 | 15 | 40,00% | 1,32 | €1,03 | 0,53% |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | Momentum / breakout V3 Filtered | €10.013,82 | €13,82 | 41 | 41 | 48,78% | 1,01 | €0,34 | 4,50% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €10.009,02 | €9,02 | 28 | 28 | 46,43% | 1,40 | €0,32 | 0,07% |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | Momentum / breakout V3 Filtered | €10.008,92 | €8,92 | 30 | 30 | 36,67% | 1,02 | €0,30 | 4,84% |
| TEST | Doge Ema 1H | Trend following EMA | €10.008,83 | €18,06 | 15 | 15 | 60,00% | 1,05 | €1,20 | 2,77% |
| TEST | Scalp RSI Short 85 · €10 · 15x | Inversione RSI estrema 15m | €10.003,60 | €3,60 | 5 | 5 | 60,00% | 1,69 | €0,72 | 0,06% |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | Momentum / breakout V3 Filtered | €10.003,37 | €3,37 | 8 | 8 | 37,50% | 1,02 | €0,42 | 2,15% |
| TEST | Scalp RSI Short 80 · €10 · 15x | Inversione RSI estrema 15m | €10.003,10 | €3,10 | 15 | 15 | 40,00% | 1,32 | €0,21 | 0,11% |
| TEST | Scanner Bottom5 Short Continuation V1 | Scanner Bottom5 Short Continuation | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 20 · €10 · 15x | Inversione RSI estrema 15m | €9.999,33 | €-0,67 | 9 | 9 | 44,44% | 0,85 | €-0,07 | 0,04% |
| TEST | Scalp RSI Long 15 · €10 · 15x | Inversione RSI estrema 15m | €9.997,60 | €-2,40 | 3 | 3 | 33,33% | 0,13 | €-0,80 | 0,02% |
| TEST | Scalp RSI Long 20 · €50 · 15x | Inversione RSI estrema 15m | €9.996,64 | €-3,36 | 9 | 9 | 44,44% | 0,85 | €-0,37 | 0,21% |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | Momentum / breakout V3 Filtered | €9.995,23 | €-4,77 | 15 | 15 | 46,67% | 0,99 | €-0,32 | 2,70% |
| TEST | Scalp RSI Short 85 · prudente · 5x | Inversione RSI estrema 15m | €9.991,38 | €-8,62 | 5 | 5 | 60,00% | 0,61 | €-1,72 | 0,30% |
| TEST | Scalp RSI Long 25 · €10 · 15x | Inversione RSI estrema 15m | €9.990,45 | €-9,55 | 15 | 15 | 40,00% | 0,36 | €-0,64 | 0,14% |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | €9.988,00 | €-12,00 | 3 | 3 | 33,33% | 0,13 | €-4,00 | 0,12% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €9.987,48 | €-12,52 | 15 | 15 | 40,00% | 0,83 | €-0,83 | 0,71% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €9.981,72 | €-18,28 | 3 | 3 | 33,33% | 0,83 | €-6,09 | 1,22% |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | €9.980,94 | €-19,06 | 3 | 3 | 33,33% | 0,19 | €-6,35 | 0,20% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €9.965,81 | €-34,19 | 4 | 4 | 25,00% | 0,80 | €-8,55 | 2,43% |
| TEST | Scalp RSI Short 80 · prudente · 5x | Inversione RSI estrema 15m | €9.952,43 | €-47,57 | 15 | 15 | 40,00% | 0,45 | €-3,17 | 0,89% |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | €9.952,25 | €-47,75 | 15 | 15 | 40,00% | 0,36 | €-3,18 | 0,72% |
| TEST | Scanner Top15 Long | Scanner Top15 Long | €9.951,56 | €7,69 | 112 | 112 | 50,89% | 1,00 | €0,07 | 10,31% |
| TEST | Scanner Top20 Long | Scanner Top20 Long | €9.951,56 | €7,69 | 112 | 112 | 50,89% | 1,00 | €0,07 | 10,31% |
| TEST | Btc Ema 1H | Trend following EMA | €9.941,95 | €-58,05 | 11 | 11 | 36,36% | 0,82 | €-5,28 | 1,94% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.939,62 | €-60,38 | 28 | 28 | 46,43% | 0,60 | €-2,16 | 0,84% |
| TEST | Eth Ema 4H | Trend following EMA | €9.929,80 | €-88,72 | 5 | 5 | 20,00% | 0,58 | €-17,74 | 1,83% |
| TEST | Combo Adaptive Regime V1 | Combo Adaptive | €9.924,39 | €-58,95 | 52 | 52 | 48,08% | 0,95 | €-1,13 | 5,38% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €9.911,95 | €-88,05 | 12 | 12 | 50,00% | 0,75 | €-7,34 | 3,08% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.897,54 | €-102,46 | 12 | 12 | 41,67% | 0,74 | €-8,54 | 3,14% |
| TEST | Combo Adaptive Quality7 Regime V1 | Combo Adaptive | €9.894,87 | €-59,11 | 36 | 36 | 44,44% | 0,93 | €-1,64 | 5,41% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €9.884,90 | €-103,26 | 14 | 14 | 35,71% | 0,77 | €-7,38 | 4,59% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.873,88 | €-126,12 | 10 | 10 | 40,00% | 0,69 | €-12,61 | 2,37% |
| TEST | 1H Fast V3 No Esports V1 | Momentum / breakout V3 Filtered | €9.871,67 | €-88,75 | 193 | 193 | 45,08% | 0,98 | €-0,46 | 9,00% |
| TEST | Scanner Top5 Btc Guard V1 | Scanner Top 5 + forza BTC | €9.868,12 | €-123,80 | 97 | 97 | 41,24% | 0,95 | €-1,28 | 7,34% |
| TEST | Eth Ema 1H | Trend following EMA | €9.866,33 | €-133,67 | 17 | 17 | 41,18% | 0,77 | €-7,86 | 4,80% |
| TEST | Combo Scanner | Combo Scanner | €9.864,56 | €-104,47 | 120 | 120 | 45,83% | 0,96 | €-0,87 | 11,38% |
| TEST | Combo Adaptive Quality7 V1 | Combo Adaptive | €9.848,66 | €-101,42 | 75 | 75 | 41,33% | 0,94 | €-1,35 | 8,88% |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | Momentum / breakout V3 Filtered | €9.837,38 | €-162,62 | 37 | 37 | 40,54% | 0,76 | €-4,40 | 3,08% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | Momentum / breakout V3 Filtered | €9.817,34 | €-182,66 | 24 | 24 | 41,67% | 0,64 | €-7,61 | 3,23% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €9.801,99 | €-156,48 | 104 | 99 | 42,31% | 0,95 | €-1,50 | 10,88% |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | Momentum / breakout | €9.779,10 | €-220,90 | 86 | 86 | 41,86% | 0,88 | €-2,57 | 7,10% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | Momentum / breakout V3 Filtered | €9.762,18 | €-237,82 | 7 | 7 | 14,29% | 0,02 | €-33,97 | 2,82% |
| TEST | 1H Balanced Long No Rhv V1 | Confluenza trend | €9.754,28 | €-208,93 | 90 | 90 | 46,67% | 0,89 | €-2,32 | 9,26% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.730,51 | €-269,49 | 12 | 12 | 25,00% | 0,51 | €-22,46 | 2,92% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | Momentum / breakout V3 Filtered | €9.723,72 | €-276,28 | 31 | 31 | 32,26% | 0,62 | €-8,91 | 4,83% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €9.703,71 | €-296,29 | 7 | 7 | 28,57% | 0,22 | €-42,33 | 4,16% |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | Scanner Top 5 + forza BTC | €9.665,74 | €-305,73 | 15 | 15 | 26,67% | 0,44 | €-20,38 | 5,46% |
| TEST | Scanner Top5 Btc Mfe V1 | Scanner Top 5 + forza BTC | €9.638,72 | €-331,03 | 108 | 108 | 45,37% | 0,85 | €-3,07 | 12,28% |
| TEST | Scanner Top5 Btc Guard Mfe V1 | Scanner Top 5 + forza BTC | €9.638,62 | €-353,48 | 114 | 114 | 42,11% | 0,87 | €-3,10 | 8,78% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.628,04 | €-371,96 | 16 | 16 | 25,00% | 0,32 | €-23,25 | 3,92% |
| TEST | 1H Fast Score 6 75 V1 | Momentum / breakout | €9.626,03 | €-373,13 | 130 | 130 | 41,54% | 0,89 | €-2,87 | 10,37% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | Momentum / breakout V3 Filtered | €9.579,83 | €-420,17 | 11 | 11 | 0,00% | 0,00 | €-38,20 | 4,20% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €9.576,13 | €-420,44 | 99 | 91 | 43,43% | 0,80 | €-4,25 | 8,84% |
| TEST | 1H Fast V3 Long Only V1 | Momentum / breakout V3 Filtered | €9.550,64 | €-408,32 | 149 | 149 | 41,61% | 0,88 | €-2,74 | 12,52% |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | Scanner Top 5 + forza BTC | €9.547,78 | €-471,84 | 62 | 62 | 38,71% | 0,75 | €-7,61 | 7,99% |
| TEST | 1H Balanced V3 Long Only V1 | Confluenza trend V3 Filtered | €9.525,12 | €-460,26 | 102 | 102 | 44,12% | 0,77 | €-4,51 | 8,85% |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | Momentum / breakout V3 Filtered | €9.517,55 | €-482,45 | 78 | 78 | 39,74% | 0,78 | €-6,19 | 6,59% |
| TEST | 1H Fast V3 Nohigh V1 | Momentum / breakout V3 Filtered | €9.435,38 | €-564,62 | 112 | 112 | 40,18% | 0,79 | €-5,04 | 6,91% |
| TEST | Combo Trend | Combo Trend | €9.434,55 | €-557,51 | 149 | 149 | 38,93% | 0,84 | €-3,74 | 10,85% |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | Momentum / breakout V3 Filtered | €9.389,68 | €-610,32 | 83 | 83 | 44,58% | 0,76 | €-7,35 | 7,69% |
| TEST | Scanner Bottom10 Short | Scanner Bottom10 Short | €9.384,56 | €-614,37 | 68 | 68 | 32,35% | 0,67 | €-9,03 | 8,29% |
| TEST | Scanner Bottom15 Short | Scanner Bottom15 Short | €9.384,56 | €-614,37 | 68 | 68 | 32,35% | 0,67 | €-9,03 | 8,29% |
| TEST | Scanner Bottom20 Short | Scanner Bottom20 Short | €9.384,56 | €-614,37 | 68 | 68 | 32,35% | 0,67 | €-9,03 | 8,29% |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | Scanner Top 5 + forza BTC | €9.381,70 | €-638,24 | 78 | 78 | 38,46% | 0,71 | €-8,18 | 7,27% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €9.378,18 | €-621,78 | 51 | 51 | 31,37% | 0,66 | €-12,19 | 8,18% |
| TEST | Master Adaptive Gb20 Be V1 | Master Adaptive Consensus | €9.372,49 | €-627,51 | 55 | 55 | 29,09% | 0,62 | €-11,41 | 8,39% |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | Momentum / breakout | €9.370,10 | €-629,09 | 88 | 88 | 43,18% | 0,78 | €-7,15 | 10,69% |
| TEST | Master Adaptive Gb20 Partial V1 | Master Adaptive Consensus | €9.362,52 | €-637,48 | 50 | 50 | 34,00% | 0,60 | €-12,75 | 7,98% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €9.354,60 | €-645,40 | 58 | 58 | 34,48% | 0,67 | €-11,13 | 7,26% |
| TEST | 1H Fast V3 Cap75 V1 | Momentum / breakout V3 Filtered | €9.347,45 | €-644,83 | 126 | 126 | 38,10% | 0,80 | €-5,12 | 11,84% |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | €9.326,30 | €-673,70 | 52 | 52 | 32,69% | 0,62 | €-12,96 | 7,80% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €9.319,82 | €-679,95 | 61 | 61 | 34,43% | 0,66 | €-11,15 | 7,96% |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | Scanner Bottom 5 Short | €9.319,54 | €-679,41 | 59 | 59 | 32,20% | 0,60 | €-11,52 | 8,31% |
| TEST | Scanner Bottom5 Short Profit Lock V1 | Scanner Bottom 5 Short | €9.305,36 | €-693,59 | 60 | 60 | 31,67% | 0,58 | €-11,56 | 8,31% |
| TEST | Master Adaptive Gb20 Loss Cap V1 | Master Adaptive Consensus | €9.252,08 | €-747,69 | 42 | 42 | 23,81% | 0,53 | €-17,80 | 11,41% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.233,75 | €-765,20 | 87 | 87 | 32,18% | 0,66 | €-8,80 | 9,41% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €9.202,39 | €-797,61 | 87 | 87 | 48,28% | 0,60 | €-9,17 | 9,02% |
| TEST | Scanner Top5 Btc Btc Le3 V1 | Scanner Top 5 + forza BTC | €9.193,60 | €-779,26 | 61 | 61 | 34,43% | 0,57 | €-12,77 | 11,72% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.188,59 | €-770,84 | 120 | 120 | 38,33% | 0,68 | €-6,42 | 12,31% |
| TEST | Combo Adaptive Mfe Trail | Combo Adaptive | €9.185,50 | €-796,48 | 149 | 149 | 41,61% | 0,74 | €-5,35 | 15,45% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €9.150,69 | €-849,31 | 121 | 121 | 36,36% | 0,69 | €-7,02 | 13,99% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €9.114,32 | €-885,68 | 38 | 38 | 36,84% | 0,48 | €-23,31 | 10,65% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €9.056,84 | €-943,16 | 53 | 53 | 28,30% | 0,59 | €-17,80 | 11,51% |
| TEST | Combo Adaptive Runner25 V1 | Combo Adaptive | €8.964,11 | €-1.035,89 | 94 | 94 | 30,85% | 0,53 | €-11,02 | 12,67% |
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
| Principale 4H | HYPE | LONG | Confluenza trend | 240m | 3,0x | 76,47929 | 79,80100 | 78,92617 | 51,36859 | 86,46833 | €10,44 | €31,32 | €0,00 | €1,36 |
| Principale 4H | TRUMP | LONG | Confluenza trend | 240m | 3,0x | 2,46049 | 2,48800 | 2,16523 | 1,65263 | 3,05101 | €134,98 | €404,95 | €48,59 | €4,53 |
| Principale 4H | XRP | LONG | Confluenza trend | 240m | 3,0x | 1,46057 | 1,47325 | 1,30460 | 0,98102 | 1,77252 | €8,58 | €25,73 | €2,75 | €0,22 |
| 1H Balanced Long No Rhv V1 | SKHYNIX | LONG | Confluenza trend | 60m | 3,0x | 1214,11277 | 1214,11277 | 1170,18211 | 815,47908 | 1301,97411 | €413,43 | €1.240,28 | €44,88 | €0,00 |
| 1H Balanced Long No Rhv V1 | BOME | LONG | Confluenza trend | 60m | 3,0x | 0,00129 | 0,00129 | 0,00114 | 0,00087 | 0,00160 | €134,98 | €404,95 | €48,59 | €0,00 |
| 1H Balanced Long No Rhv V1 | TAO | LONG | Confluenza trend | 60m | 3,0x | 247,38947 | 247,38947 | 237,94346 | 166,16326 | 266,28148 | €428,20 | €1.284,61 | €49,05 | €0,00 |
| 1H Balanced Long No Rhv V1 | PEPE | LONG | Confluenza trend | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €21,51 | €64,54 | €5,62 | €-2,39 |
| 1H Balanced Long No Rhv V1 | HYPE | LONG | Confluenza trend | 60m | 3,0x | 81,52730 | 79,80100 | 78,98606 | 54,75917 | 86,60979 | €497,57 | €1.492,70 | €46,53 | €-31,61 |
| Bilanciata 1H V2 | SKHYNIX | LONG | Confluenza trend V2 | 60m | 3,0x | 1214,11277 | 1214,11277 | 1170,18211 | 815,47908 | 1301,97411 | €422,38 | €1.267,15 | €45,85 | €0,00 |
| Bilanciata 1H V2 | PEPE | LONG | Confluenza trend V2 | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €184,87 | €554,60 | €48,28 | €-20,56 |
| Bilanciata 1H V2 | ZEC | LONG | Confluenza trend V2 | 60m | 3,0x | 798,37964 | 831,89000 | 817,96285 | 536,24499 | 927,34406 | €8,81 | €26,44 | €0,00 | €1,11 |
| Bilanciata 1H V2 | ENA | LONG | Confluenza trend V2 | 60m | 3,0x | 0,16380 | 0,16752 | 0,15392 | 0,11002 | 0,18358 | €263,92 | €791,77 | €47,79 | €17,97 |
| Bilanciata 1H V3 Filtered | SKHYNIX | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1220,85412 | 1220,85412 | 1177,63561 | 820,00702 | 1307,29117 | €460,42 | €1.381,27 | €48,90 | €0,00 |
| Bilanciata 1H V3 Filtered | ZEC | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 807,93155 | 831,89000 | 737,89694 | 542,66069 | 948,00078 | €195,29 | €585,88 | €50,79 | €17,37 |
| Bilanciata 1H V3 Filtered | XRP | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1,47399 | 1,47325 | 1,35380 | 0,99003 | 1,71438 | €205,84 | €617,51 | €50,35 | €-0,31 |
| Bilanciata 1H V3 Filtered | PEPE | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €8,77 | €26,32 | €2,02 | €0,04 |
| Bilanciata 1H V3 Filtered | PUMP | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,00523 | 0,00497 | 0,00479 | 0,00351 | 0,00611 | €197,24 | €591,72 | €49,81 | €-29,76 |
| Bilanciata 1H V3 Filtered | SUI | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,84147 | 0,82480 | 0,80853 | 0,56519 | 0,90734 | €9,48 | €28,45 | €1,11 | €-0,56 |
| 1H Fast Score 6 75 V1 | ENA | LONG | Momentum / breakout | 60m | 3,0x | 0,16755 | 0,16752 | 0,15988 | 0,11254 | 0,17907 | €350,27 | €1.050,81 | €48,13 | €-0,21 |
| 1H Fast Score 6 75 No Trend Up V1 | ENA | LONG | Momentum / breakout | 60m | 3,0x | 0,16755 | 0,16752 | 0,15988 | 0,11254 | 0,17907 | €340,96 | €1.022,87 | €46,85 | €-0,20 |
| 1H Fast Score 6 75 Cost Aware V1 | BTW | LONG | Momentum / breakout | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €8,91 | €26,72 | €3,13 | €0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00086 | 0,00146 | €215,92 | €647,76 | €57,03 | €0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | NEAR | LONG | Momentum / breakout | 60m | 3,0x | 2,08142 | 2,08142 | 2,02315 | 1,39802 | 2,16882 | €42,86 | €128,59 | €3,60 | €0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | XRP | LONG | Momentum / breakout | 60m | 3,0x | 1,47399 | 1,47325 | 1,38051 | 0,99003 | 1,61422 | €284,39 | €853,18 | €54,11 | €-0,43 |
| 1H Fast Score 6 75 Cost Aware V1 | PUMP | LONG | Momentum / breakout | 60m | 3,0x | 0,00523 | 0,00497 | 0,00489 | 0,00351 | 0,00574 | €260,23 | €780,70 | €51,11 | €-39,26 |
| 1H Fast Score 6 75 Cost Aware V1 | ENA | LONG | Momentum / breakout | 60m | 3,0x | 0,16755 | 0,16752 | 0,15988 | 0,11254 | 0,17907 | €412,11 | €1.236,33 | €56,63 | €-0,25 |
| 1H Fast Long Btc 1 3 Cap75 V1 | XRP | LONG | Momentum / breakout | 60m | 3,0x | 1,49738 | 1,47325 | 1,40463 | 1,00574 | 1,63650 | €272,47 | €817,41 | €50,63 | €-13,17 |
| 1H Fast Long Btc 1 3 Cap75 V1 | DOGE | LONG | Momentum / breakout | 60m | 3,0x | 0,09162 | 0,09209 | 0,08782 | 0,06154 | 0,09732 | €406,05 | €1.218,14 | €50,55 | €6,27 |
| 1H Fast Long Btc 1 3 Cap75 V1 | SUI | LONG | Momentum / breakout | 60m | 3,0x | 0,83617 | 0,82480 | 0,81103 | 0,56163 | 0,87387 | €22,96 | €68,87 | €2,07 | €-0,94 |
| 1H Fast Long Btc 1 3 Cap75 V1 | PUMP | LONG | Momentum / breakout | 60m | 3,0x | 0,00516 | 0,00497 | 0,00489 | 0,00347 | 0,00557 | €9,37 | €28,12 | €1,47 | €-1,06 |
| 1H Fast Long Btc 1 3 Cap75 V1 | ZEC | LONG | Momentum / breakout | 60m | 3,0x | 835,56708 | 831,89000 | 801,45253 | 561,22256 | 886,73890 | €413,29 | €1.239,88 | €50,62 | €-5,46 |
| 1H Fast Long Btc 1 3 Cap75 V1 | ENA | LONG | Momentum / breakout | 60m | 3,0x | 0,16755 | 0,16752 | 0,15988 | 0,11254 | 0,17907 | €339,56 | €1.018,68 | €46,66 | €-0,20 |
| 1H Fast No Pepe V1 | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €172,22 | €516,67 | €49,86 | €0,00 |
| 1H Fast No Pepe V1 | TAO | LONG | Momentum / breakout | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €47,93 | €143,78 | €4,27 | €0,00 |
| 1H Fast No Pepe V1 | XRP | LONG | Momentum / breakout | 60m | 3,0x | 1,49835 | 1,47325 | 1,43358 | 1,00639 | 1,59551 | €415,25 | €1.245,74 | €53,85 | €-20,87 |
| 1H Fast No Pepe V1 | PUMP | LONG | Momentum / breakout | 60m | 3,0x | 0,00515 | 0,00497 | 0,00480 | 0,00346 | 0,00567 | €266,74 | €800,21 | €53,85 | €-27,68 |
| 1H Fast No Pepe V1 | ZEC | LONG | Momentum / breakout | 60m | 3,0x | 835,56708 | 831,89000 | 801,45253 | 561,22256 | 886,73890 | €24,71 | €74,13 | €3,03 | €-0,33 |
| 1H Fast No Pepe V1 | ENA | LONG | Momentum / breakout | 60m | 3,0x | 0,16755 | 0,16752 | 0,15988 | 0,11254 | 0,17907 | €358,96 | €1.076,89 | €49,33 | €-0,22 |
| 1H Fast Tp2 V1 | BTW | LONG | Momentum / breakout | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,56752 | €142,85 | €428,56 | €50,25 | €0,00 |
| 1H Fast Tp2 V1 | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00132 | 0,00132 | 0,00119 | 0,00088 | 0,00158 | €18,87 | €56,62 | €5,59 | €0,00 |
| 1H Fast Tp2 V1 | DOGE | LONG | Momentum / breakout | 60m | 3,0x | 0,09162 | 0,09209 | 0,08782 | 0,06154 | 0,09922 | €9,51 | €28,53 | €1,18 | €0,15 |
| 1H Fast Tp2 V1 | SOL | LONG | Momentum / breakout | 60m | 3,0x | 95,16303 | 94,06500 | 93,13926 | 63,91783 | 99,21056 | €9,00 | €26,99 | €0,57 | €-0,31 |
| 1H Fast Tp2 V1 | PUMP | LONG | Momentum / breakout | 60m | 3,0x | 0,00515 | 0,00497 | 0,00484 | 0,00346 | 0,00576 | €261,16 | €783,47 | €46,57 | €-27,10 |
| 1H Fast Tp2 V1 | ZEC | LONG | Momentum / breakout | 60m | 3,0x | 835,56708 | 831,89000 | 801,45253 | 561,22256 | 903,79618 | €420,43 | €1.261,30 | €51,50 | €-5,55 |
| 1H Fast Tp2 V1 | ENA | LONG | Momentum / breakout | 60m | 3,0x | 0,16755 | 0,16752 | 0,15988 | 0,11254 | 0,18290 | €362,09 | €1.086,26 | €49,76 | €-0,22 |
| Rapida 1H V3 Filtered | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €172,00 | €515,99 | €49,79 | €0,00 |
| Rapida 1H V3 Filtered | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €589,98 | €1.769,95 | €52,56 | €0,00 |
| Rapida 1H V3 Filtered | PUMP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00522 | 0,00497 | 0,00488 | 0,00351 | 0,00573 | €262,56 | €787,69 | €51,10 | €-38,03 |
| Rapida 1H V3 Filtered | SOL | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 95,16303 | 94,06500 | 93,13926 | 63,91783 | 98,19868 | €10,94 | €32,83 | €0,70 | €-0,38 |
| Rapida 1H V3 Filtered | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 835,56708 | 831,89000 | 801,45253 | 561,22256 | 886,73890 | €413,22 | €1.239,66 | €50,61 | €-5,46 |
| Rapida 1H V3 Filtered | ENA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16755 | 0,16752 | 0,15988 | 0,11254 | 0,17907 | €20,47 | €61,41 | €2,81 | €-0,01 |
| 1H Fast V3 Cap75 V1 | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 835,56708 | 831,89000 | 801,45253 | 561,22256 | 886,73890 | €381,89 | €1.145,68 | €46,78 | €-5,04 |
| 1H Fast V3 Cap75 V1 | ENA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16755 | 0,16752 | 0,15988 | 0,11254 | 0,17907 | €340,18 | €1.020,53 | €46,75 | €-0,20 |
| 1H Fast V3 Cap75 V1 | SUI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,82496 | 0,82480 | 0,79875 | 0,55410 | 0,86429 | €490,23 | €1.470,69 | €46,74 | €-0,29 |
| 1H Fast V3 Long Only V1 | BTW | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €126,57 | €379,72 | €44,52 | €0,00 |
| 1H Fast V3 Long Only V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00147 | €9,56 | €28,69 | €2,66 | €0,00 |
| 1H Fast V3 Long Only V1 | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €554,42 | €1.663,26 | €49,39 | €0,00 |
| 1H Fast V3 Long Only V1 | PUMP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00522 | 0,00497 | 0,00488 | 0,00351 | 0,00573 | €229,21 | €687,62 | €44,60 | €-33,20 |
| 1H Fast V3 Long Only V1 | SOL | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 95,16303 | 94,06500 | 93,13926 | 63,91783 | 98,19868 | €9,77 | €29,31 | €0,62 | €-0,34 |
| 1H Fast V3 Long Only V1 | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 835,56708 | 831,89000 | 801,45253 | 561,22256 | 886,73890 | €380,44 | €1.141,32 | €46,60 | €-5,02 |
| 1H Fast V3 Long Only V1 | ENA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16755 | 0,16752 | 0,15988 | 0,11254 | 0,17907 | €18,99 | €56,97 | €2,61 | €-0,01 |
| 1H Fast V3 No Esports V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €169,36 | €508,09 | €49,03 | €0,00 |
| 1H Fast V3 No Esports V1 | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €27,04 | €81,13 | €2,41 | €0,00 |
| 1H Fast V3 No Esports V1 | PUMP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00522 | 0,00497 | 0,00488 | 0,00351 | 0,00573 | €252,96 | €758,88 | €49,23 | €-36,64 |
| 1H Fast V3 No Esports V1 | ENA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16755 | 0,16752 | 0,15988 | 0,11254 | 0,17907 | €359,25 | €1.077,76 | €49,37 | €-0,22 |
| 1H Fast V3 No Esports V1 | SUI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,82496 | 0,82480 | 0,79875 | 0,55410 | 0,86429 | €497,34 | €1.492,03 | €47,42 | €-0,30 |
| 1H Fast V3 No Esports Long Only V1 | BTW | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €132,94 | €398,81 | €46,76 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00147 | €10,06 | €30,18 | €2,80 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | PUMP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00522 | 0,00497 | 0,00488 | 0,00351 | 0,00573 | €249,75 | €749,26 | €48,60 | €-36,18 |
| 1H Fast V3 No Esports Long Only V1 | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 835,56708 | 831,89000 | 801,45253 | 561,22256 | 886,73890 | €412,37 | €1.237,11 | €50,51 | €-5,44 |
| 1H Fast V3 No Esports Long Only V1 | ENA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16755 | 0,16752 | 0,15988 | 0,11254 | 0,17907 | €365,83 | €1.097,49 | €50,27 | €-0,22 |
| 1H Fast V3 No Esports Long Only V1 | SUI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,82496 | 0,82480 | 0,79875 | 0,55410 | 0,86429 | €22,31 | €66,93 | €2,13 | €-0,01 |
| 1H Fast V3 No Esports Mfe Lock V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €173,11 | €519,32 | €50,11 | €0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €593,79 | €1.781,38 | €52,90 | €0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | PUMP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00522 | 0,00497 | 0,00488 | 0,00351 | 0,00573 | €264,26 | €792,79 | €51,43 | €-38,28 |
| 1H Fast V3 No Esports Mfe Lock V1 | SOL | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 95,16303 | 94,06500 | 93,13926 | 63,91783 | 98,19868 | €11,01 | €33,04 | €0,70 | €-0,38 |
| 1H Fast V3 No Esports Mfe Lock V1 | ZEC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 835,56708 | 831,89000 | 801,45253 | 561,22256 | 886,73890 | €415,89 | €1.247,68 | €50,94 | €-5,49 |
| 1H Fast V3 No Esports Mfe Lock V1 | ENA | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16755 | 0,16752 | 0,15988 | 0,11254 | 0,17907 | €20,60 | €61,81 | €2,83 | €-0,01 |
| Ampia 4H | SPCX | LONG | Confluenza trend | 240m | 2,0x | 136,56189 | 136,56189 | 126,46637 | 68,96375 | 164,82935 | €323,86 | €647,73 | €47,88 | €0,00 |
| Ampia 4H | VELVET | LONG | Confluenza trend | 240m | 2,0x | 0,55987 | 0,55987 | 0,49269 | 0,28274 | 0,74799 | €201,63 | €403,26 | €48,39 | €0,00 |
| Ampia 4H | LINK | LONG | Confluenza trend | 240m | 2,0x | 11,96839 | 11,96839 | 11,08055 | 6,04404 | 14,45436 | €14,07 | €28,15 | €2,09 | €0,00 |
| Ampia 4H | SUI | LONG | Confluenza trend | 240m | 2,0x | 0,86357 | 0,82480 | 0,75994 | 0,43610 | 1,15373 | €215,46 | €430,92 | €51,71 | €-19,35 |
| Ampia 4H | ETH | LONG | Confluenza trend | 240m | 2,0x | 2430,03591 | 2437,32000 | 2267,54364 | 1227,16813 | 2885,01426 | €18,82 | €37,65 | €2,52 | €0,11 |
| Ampia 4H | HYPE | LONG | Confluenza trend | 240m | 2,0x | 79,31286 | 79,80100 | 70,73982 | 40,05299 | 103,31737 | €13,82 | €27,64 | €2,99 | €0,17 |
| Ampia 4H | TRUMP | LONG | Confluenza trend | 240m | 2,0x | 2,37347 | 2,48800 | 2,08866 | 1,19860 | 3,17096 | €210,83 | €421,66 | €50,60 | €20,35 |
| Forza relativa 1H V2 | BEAT | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,25984 | 0,25984 | 0,25657 | 0,38847 | 0,19125 | €200,38 | €400,75 | €0,00 | €-0,00 |
| Forza relativa 1H V2 | PEPE | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €286,19 | €572,37 | €49,83 | €-21,22 |
| Forza relativa 1H V2 | PUMP | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,00510 | 0,00497 | 0,00476 | 0,00258 | 0,00586 | €356,70 | €713,40 | €47,79 | €-19,01 |
| Benchmark Donchian breakout 1H | SKHYNIX | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1174,33482 | 1174,33482 | 1128,44989 | 593,03908 | 1289,04713 | €641,25 | €1.282,50 | €50,11 | €0,00 |
| Benchmark Donchian breakout 1H | PUMP | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,00522 | 0,00497 | 0,00474 | 0,00264 | 0,00643 | €312,08 | €624,15 | €57,84 | €-30,14 |
| Benchmark Donchian breakout 1H | ETH | LONG | Donchian breakout 20 barre | 60m | 2,0x | 2464,63283 | 2437,32000 | 2414,66831 | 1244,63958 | 2589,54414 | €1.424,54 | €2.849,08 | €57,76 | €-31,57 |
| Donchian 1H Gb20 120R V1 | SKHYNIX | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1174,33482 | 1174,33482 | 1128,44989 | 593,03908 | 1289,04713 | €626,15 | €1.252,30 | €48,93 | €0,00 |
| Donchian 1H Gb20 120R V1 | PUMP | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,00522 | 0,00497 | 0,00474 | 0,00264 | 0,00643 | €304,73 | €609,46 | €56,48 | €-29,43 |
| Donchian 1H Gb20 120R V1 | ETH | LONG | Donchian breakout 20 barre | 60m | 2,0x | 2464,63283 | 2437,32000 | 2414,66831 | 1244,63958 | 2589,54414 | €1.391,00 | €2.782,00 | €56,40 | €-30,83 |
| Benchmark trend following EMA 1H | BEAT | SHORT | Trend following EMA | 60m | 2,0x | 0,28257 | 0,28257 | 0,25706 | 0,42244 | 0,20797 | €186,11 | €372,23 | €0,00 | €-0,00 |
| Benchmark trend following EMA 1H | BTC | LONG | Trend following EMA | 60m | 2,0x | 76719,31079 | 76954,40000 | 74671,22818 | 38743,25195 | 81225,09269 | €833,14 | €1.666,28 | €44,48 | €5,11 |
| Benchmark trend following EMA 1H | SOL | LONG | Trend following EMA | 60m | 2,0x | 95,05001 | 94,06500 | 89,98943 | 48,00025 | 106,18327 | €434,46 | €868,92 | €46,26 | €-9,00 |
| Benchmark trend following EMA 1H | ZEC | LONG | Trend following EMA | 60m | 2,0x | 807,93155 | 831,89000 | 730,11531 | 408,00543 | 979,12728 | €17,42 | €34,84 | €3,36 | €1,03 |
| Benchmark trend following EMA 1H | TRUMP | LONG | Trend following EMA | 60m | 2,0x | 2,70054 | 2,48800 | 2,42296 | 1,36377 | 3,31121 | €215,60 | €431,20 | €44,32 | €-33,94 |
| Scanner Top 5 Long 1H | BOME | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00160 | €218,24 | €436,47 | €52,38 | €0,00 |
| Scanner Top 5 Long 1H | PEPE | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €322,02 | €644,04 | €56,06 | €-23,88 |
| Scanner Top 5 Long 1H | PUMP | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,00502 | 0,00497 | 0,00460 | 0,00254 | 0,00587 | €316,31 | €632,61 | €53,01 | €-7,05 |
| Scanner Top 5 Long 1H | TRUMP | LONG | Scanner Top 5 Long | 60m | 2,0x | 2,50550 | 2,48800 | 2,21642 | 1,26528 | 3,08367 | €238,89 | €477,78 | €55,13 | €-3,34 |
| Scanner Top 5 Long 1H | ENA | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,16380 | 0,16752 | 0,15392 | 0,08272 | 0,18358 | €32,80 | €65,60 | €3,96 | €1,49 |
| Scanner Bottom 5 Short 1H | SOXL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €378,86 | €757,72 | €48,07 | €-0,00 |
| Scanner Bottom 5 Short 1H | SNDK | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €492,80 | €985,60 | €47,71 | €-0,00 |
| Scanner Top10 Long | TAO | LONG | Scanner Top10 Long | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €678,43 | €1.356,86 | €51,81 | €0,00 |
| Scanner Top10 Long | PEPE | LONG | Scanner Top10 Long | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €288,77 | €577,53 | €50,27 | €-21,42 |
| Scanner Top10 Long | SUI | LONG | Scanner Top10 Long | 60m | 2,0x | 0,83617 | 0,82480 | 0,80385 | 0,42226 | 0,90081 | €14,11 | €28,22 | €1,09 | €-0,38 |
| Scanner Top10 Long | ETH | LONG | Scanner Top10 Long | 60m | 2,0x | 2462,71244 | 2437,32000 | 2415,97708 | 1243,66978 | 2556,18319 | €1.366,78 | €2.733,55 | €51,88 | €-28,19 |
| Scanner Top10 Long | ENA | LONG | Scanner Top10 Long | 60m | 2,0x | 0,16380 | 0,16752 | 0,15392 | 0,08272 | 0,18358 | €426,83 | €853,65 | €51,52 | €19,37 |
| Scanner Bottom10 Short | SOXL | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom10 Short | SNDK | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Top15 Long | NEAR | LONG | Scanner Top15 Long | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €16,79 | €33,59 | €1,21 | €0,00 |
| Scanner Top15 Long | TAO | LONG | Scanner Top15 Long | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €88,53 | €177,07 | €6,76 | €0,00 |
| Scanner Top15 Long | PEPE | LONG | Scanner Top15 Long | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €291,03 | €582,05 | €50,67 | €-21,58 |
| Scanner Top15 Long | PUMP | LONG | Scanner Top15 Long | 60m | 2,0x | 0,00502 | 0,00497 | 0,00460 | 0,00254 | 0,00587 | €291,59 | €583,18 | €48,87 | €-6,50 |
| Scanner Top15 Long | TRUMP | LONG | Scanner Top15 Long | 60m | 2,0x | 2,50550 | 2,48800 | 2,21642 | 1,26528 | 3,08367 | €215,87 | €431,75 | €49,81 | €-3,02 |
| Scanner Top15 Long | HYPE | LONG | Scanner Top15 Long | 60m | 2,0x | 81,06421 | 79,80100 | 78,65294 | 40,93743 | 85,88675 | €677,13 | €1.354,27 | €40,28 | €-21,10 |
| Scanner Top15 Long | ETH | LONG | Scanner Top15 Long | 60m | 2,0x | 2462,71244 | 2437,32000 | 2415,97708 | 1243,66978 | 2556,18319 | €73,71 | €147,42 | €2,80 | €-1,52 |
| Scanner Bottom15 Short | SOXL | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom15 Short | SNDK | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Top20 Long | NEAR | LONG | Scanner Top20 Long | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €16,79 | €33,59 | €1,21 | €0,00 |
| Scanner Top20 Long | TAO | LONG | Scanner Top20 Long | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €88,53 | €177,07 | €6,76 | €0,00 |
| Scanner Top20 Long | PEPE | LONG | Scanner Top20 Long | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €291,03 | €582,05 | €50,67 | €-21,58 |
| Scanner Top20 Long | PUMP | LONG | Scanner Top20 Long | 60m | 2,0x | 0,00502 | 0,00497 | 0,00460 | 0,00254 | 0,00587 | €291,59 | €583,18 | €48,87 | €-6,50 |
| Scanner Top20 Long | TRUMP | LONG | Scanner Top20 Long | 60m | 2,0x | 2,50550 | 2,48800 | 2,21642 | 1,26528 | 3,08367 | €215,87 | €431,75 | €49,81 | €-3,02 |
| Scanner Top20 Long | HYPE | LONG | Scanner Top20 Long | 60m | 2,0x | 81,06421 | 79,80100 | 78,65294 | 40,93743 | 85,88675 | €677,13 | €1.354,27 | €40,28 | €-21,10 |
| Scanner Top20 Long | ETH | LONG | Scanner Top20 Long | 60m | 2,0x | 2462,71244 | 2437,32000 | 2415,97708 | 1243,66978 | 2556,18319 | €73,71 | €147,42 | €2,80 | €-1,52 |
| Scanner Bottom20 Short | SOXL | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom20 Short | SNDK | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Top 5 + forza BTC 1H | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €203,45 | €406,91 | €48,83 | €0,00 |
| Scanner Top 5 + forza BTC 1H | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €300,64 | €601,28 | €52,34 | €-22,30 |
| Scanner Top 5 + forza BTC 1H | PUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00502 | 0,00497 | 0,00460 | 0,00254 | 0,00595 | €295,30 | €590,60 | €49,49 | €-6,58 |
| Scanner Top 5 + forza BTC 1H | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,50550 | 2,48800 | 2,21642 | 1,26528 | 3,14149 | €223,03 | €446,06 | €51,47 | €-3,12 |
| Scanner Top 5 + forza BTC 1H | ENA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,16380 | 0,16752 | 0,15392 | 0,08272 | 0,18555 | €31,22 | €62,44 | €3,77 | €1,42 |
| Scanner Top5 Btc Mfe V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €190,73 | €381,46 | €45,77 | €0,00 |
| Scanner Top5 Btc Mfe V1 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €281,84 | €563,67 | €49,07 | €-20,90 |
| Scanner Top5 Btc Mfe V1 | PUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00502 | 0,00497 | 0,00460 | 0,00254 | 0,00595 | €276,83 | €553,66 | €46,39 | €-6,17 |
| Scanner Top5 Btc Mfe V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,50550 | 2,48800 | 2,21642 | 1,26528 | 3,14149 | €209,08 | €418,16 | €48,25 | €-2,92 |
| Scanner Top5 Btc Mfe V1 | ENA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,16380 | 0,16752 | 0,15392 | 0,08272 | 0,18555 | €29,27 | €58,53 | €3,53 | €1,33 |
| Scanner Top5 Btc Guard V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €197,27 | €394,55 | €47,35 | €0,00 |
| Scanner Top5 Btc Guard V1 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €34,88 | €69,75 | €6,07 | €-2,59 |
| Scanner Top5 Btc Guard V1 | PUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00502 | 0,00497 | 0,00460 | 0,00254 | 0,00595 | €276,09 | €552,19 | €46,27 | €-6,16 |
| Scanner Top5 Btc Guard V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,55551 | 2,48800 | 2,29388 | 1,29053 | 3,13109 | €13,03 | €26,06 | €2,67 | €-0,69 |
| Scanner Top5 Btc Guard V1 | ENA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,16690 | 0,16752 | 0,15515 | 0,08429 | 0,19277 | €343,20 | €686,40 | €48,35 | €2,54 |
| Scanner Top5 Btc Btc Le3 V1 | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 798,37964 | 831,89000 | 817,96285 | 403,18172 | 940,24050 | €285,92 | €571,84 | €0,00 | €24,00 |
| Scanner Top5 Btc Btc Le3 V1 | XRP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,50701 | 1,47325 | 1,39078 | 0,76104 | 1,76273 | €297,64 | €595,28 | €45,91 | €-13,34 |
| Scanner Top5 Btc Btc Le3 V1 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €298,93 | €597,86 | €44,42 | €1,48 |
| Scanner Top5 Btc Btc Le3 V1 | DOGE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,09338 | 0,09209 | 0,08853 | 0,04716 | 0,10406 | €12,59 | €25,17 | €1,31 | €-0,35 |
| Scanner Top5 Btc Btc Le3 V1 | PUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00527 | 0,00497 | 0,00486 | 0,00266 | 0,00618 | €14,29 | €28,58 | €2,23 | €-1,65 |
| Scanner Top5 Btc Btc Le3 V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,70354 | 2,48800 | 2,42548 | 1,36529 | 3,31528 | €220,63 | €441,25 | €45,38 | €-35,18 |
| Scanner Top5 Btc Btc 2 3 V1 | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 798,37964 | 831,89000 | 817,96285 | 403,18172 | 940,24050 | €300,60 | €601,20 | €0,00 | €25,23 |
| Scanner Top5 Btc Btc 2 3 V1 | XRP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,50701 | 1,47325 | 1,39078 | 0,76104 | 1,76273 | €312,93 | €625,85 | €48,27 | €-14,02 |
| Scanner Top5 Btc Btc 2 3 V1 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €314,28 | €628,56 | €46,70 | €1,55 |
| Scanner Top5 Btc Btc 2 3 V1 | DOGE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,09338 | 0,09209 | 0,08853 | 0,04716 | 0,10406 | €13,23 | €26,47 | €1,38 | €-0,37 |
| Scanner Top5 Btc Btc 2 3 V1 | PUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00527 | 0,00497 | 0,00486 | 0,00266 | 0,00618 | €15,02 | €30,05 | €2,35 | €-1,74 |
| Scanner Top5 Btc Btc 2 3 V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,70354 | 2,48800 | 2,42548 | 1,36529 | 3,31528 | €231,96 | €463,91 | €47,71 | €-36,99 |
| Scanner Top5 Btc Guard Mfe V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €192,69 | €385,37 | €46,24 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €34,07 | €68,13 | €5,93 | €-2,53 |
| Scanner Top5 Btc Guard Mfe V1 | PUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00502 | 0,00497 | 0,00460 | 0,00254 | 0,00595 | €269,67 | €539,35 | €45,19 | €-6,01 |
| Scanner Top5 Btc Guard Mfe V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,55551 | 2,48800 | 2,29388 | 1,29053 | 3,13109 | €12,72 | €25,45 | €2,61 | €-0,67 |
| Scanner Top5 Btc Guard Mfe V1 | ENA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,16690 | 0,16752 | 0,15515 | 0,08429 | 0,19277 | €335,22 | €670,44 | €47,23 | €2,48 |
| Scanner Top5 Btc Guard Btc Le3 V1 | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 798,37964 | 831,89000 | 817,96285 | 403,18172 | 940,24050 | €297,01 | €594,01 | €0,00 | €24,93 |
| Scanner Top5 Btc Guard Btc Le3 V1 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €313,56 | €627,12 | €46,59 | €1,55 |
| Scanner Top5 Btc Guard Btc Le3 V1 | XRP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,49793 | 1,47325 | 1,40541 | 0,75645 | 1,70147 | €13,15 | €26,30 | €1,62 | €-0,43 |
| Scanner Top5 Btc Guard Btc Le3 V1 | PUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00502 | 0,00497 | 0,00460 | 0,00254 | 0,00595 | €273,00 | €546,00 | €45,75 | €-6,09 |
| Scanner Top5 Btc Guard Btc Le3 V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,55551 | 2,48800 | 2,29388 | 1,29053 | 3,13109 | €12,70 | €25,40 | €2,60 | €-0,67 |
| Scanner Top5 Btc Guard Btc Le3 V1 | ENA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,16690 | 0,16752 | 0,15515 | 0,08429 | 0,19277 | €337,92 | €675,84 | €47,61 | €2,50 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 798,37964 | 831,89000 | 817,96285 | 403,18172 | 940,24050 | €291,91 | €583,82 | €0,00 | €24,50 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €308,18 | €616,36 | €45,79 | €1,52 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | XRP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,49793 | 1,47325 | 1,40541 | 0,75645 | 1,70147 | €12,92 | €25,84 | €1,60 | €-0,43 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | PUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00502 | 0,00497 | 0,00460 | 0,00254 | 0,00595 | €268,32 | €536,63 | €44,97 | €-5,98 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | ENA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,16690 | 0,16752 | 0,15515 | 0,08429 | 0,19277 | €329,50 | €659,00 | €46,42 | €2,43 |
| Scanner Top5 Btc Runner25 V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00176 | €210,95 | €421,90 | €50,63 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 818,21361 | 831,89000 | 764,43439 | 413,19787 | 979,55127 | €17,50 | €35,00 | €2,30 | €0,59 |
| Scanner Top5 Btc Runner25 V1 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00001 | €303,79 | €607,58 | €52,89 | €-22,53 |
| Scanner Top5 Btc Runner25 V1 | PUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00502 | 0,00497 | 0,00460 | 0,00254 | 0,00629 | €300,08 | €600,16 | €50,29 | €-6,69 |
| Scanner Top5 Btc Runner25 V1 | ENA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,16380 | 0,16752 | 0,15392 | 0,08272 | 0,19346 | €431,33 | €862,66 | €52,07 | €19,58 |
| Scanner Top5 Btc Tp3 V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00176 | €211,07 | €422,14 | €50,66 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 818,21361 | 831,89000 | 764,43439 | 413,19787 | 979,55127 | €17,51 | €35,02 | €2,30 | €0,59 |
| Scanner Top5 Btc Tp3 V1 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00001 | €303,97 | €607,94 | €52,92 | €-22,54 |
| Scanner Top5 Btc Tp3 V1 | PUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00502 | 0,00497 | 0,00460 | 0,00254 | 0,00629 | €300,25 | €600,51 | €50,32 | €-6,69 |
| Scanner Top5 Btc Tp3 V1 | ENA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,16380 | 0,16752 | 0,15392 | 0,08272 | 0,19346 | €431,58 | €863,17 | €52,10 | €19,59 |
| Combo Trend | BEAT | SHORT | Combo Trend | 60m | 2,0x | 0,25984 | 0,25984 | 0,25657 | 0,38847 | 0,19125 | €193,71 | €387,42 | €0,00 | €-0,00 |
| Combo Trend | ZEC | LONG | Combo Trend | 60m | 2,0x | 807,93155 | 831,89000 | 730,11531 | 408,00543 | 979,12728 | €247,61 | €495,23 | €47,70 | €14,69 |
| Combo Trend | PEPE | LONG | Combo Trend | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00001 | €246,56 | €493,12 | €47,70 | €-18,29 |
| Combo Trend | PUMP | LONG | Combo Trend | 60m | 2,0x | 0,00498 | 0,00497 | 0,00455 | 0,00252 | 0,00595 | €266,27 | €532,54 | €46,71 | €-1,82 |
| Combo Trend | ETH | LONG | Combo Trend | 60m | 2,0x | 2464,63283 | 2437,32000 | 2414,66831 | 1244,63958 | 2574,55479 | €34,26 | €68,51 | €1,39 | €-0,76 |
| Combo Scanner | BOME | LONG | Combo Scanner | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €195,20 | €390,40 | €46,85 | €0,00 |
| Combo Scanner | PEPE | LONG | Combo Scanner | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €288,44 | €576,88 | €50,22 | €-21,39 |
| Combo Scanner | PUMP | LONG | Combo Scanner | 60m | 2,0x | 0,00502 | 0,00497 | 0,00460 | 0,00254 | 0,00595 | €283,32 | €566,63 | €47,48 | €-6,32 |
| Combo Scanner | TRUMP | LONG | Combo Scanner | 60m | 2,0x | 2,50550 | 2,48800 | 2,21642 | 1,26528 | 3,14149 | €213,98 | €427,96 | €49,38 | €-2,99 |
| Combo Scanner | ENA | LONG | Combo Scanner | 60m | 2,0x | 0,16380 | 0,16752 | 0,15392 | 0,08272 | 0,18555 | €29,95 | €59,91 | €3,62 | €1,36 |
| Combo Adaptive | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,01735 | 121,01735 | 128,90956 | 180,92093 | 105,23292 | €367,30 | €734,61 | €47,91 | €-0,00 |
| Combo Adaptive | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €40,89 | €81,77 | €3,12 | €0,00 |
| Combo Adaptive | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 807,93155 | 831,89000 | 737,89694 | 408,00543 | 948,00078 | €307,94 | €615,88 | €53,39 | €18,26 |
| Combo Adaptive | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €306,63 | €613,26 | €53,38 | €-22,74 |
| Combo Adaptive | SOL | LONG | Combo Adaptive | 60m | 2,0x | 94,35487 | 94,06500 | 91,03919 | 47,64921 | 100,98622 | €14,11 | €28,23 | €0,99 | €-0,09 |
| Combo Adaptive | PUMP | LONG | Combo Adaptive | 60m | 2,0x | 0,00520 | 0,00497 | 0,00478 | 0,00262 | 0,00604 | €329,34 | €658,69 | €53,47 | €-29,03 |
| Combo Adaptive Mfe Trail | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €54,29 | €108,58 | €4,15 | €0,00 |
| Combo Adaptive Mfe Trail | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 807,93155 | 831,89000 | 808,90107 | 408,00543 | 948,00078 | €270,67 | €541,33 | €0,00 | €16,05 |
| Combo Adaptive Mfe Trail | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €269,51 | €539,03 | €46,92 | €-19,99 |
| Combo Adaptive Mfe Trail | XRP | LONG | Combo Adaptive | 60m | 2,0x | 1,49835 | 1,47325 | 1,41507 | 0,75667 | 1,66491 | €363,44 | €726,87 | €40,40 | €-12,18 |
| Combo Adaptive Quality7 V1 | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €371,68 | €743,36 | €47,16 | €-0,00 |
| Combo Adaptive Quality7 V1 | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €646,78 | €1.293,57 | €49,39 | €0,00 |
| Combo Adaptive Quality7 V1 | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €283,16 | €566,31 | €49,30 | €-21,00 |
| Combo Adaptive Quality7 V1 | PUMP | LONG | Combo Adaptive | 60m | 2,0x | 0,00520 | 0,00497 | 0,00478 | 0,00262 | 0,00604 | €302,38 | €604,77 | €49,09 | €-26,65 |
| Combo Adaptive Regime V1 | PUMP | LONG | Combo Adaptive | 60m | 2,0x | 0,00502 | 0,00497 | 0,00460 | 0,00254 | 0,00587 | €294,95 | €589,90 | €49,43 | €-6,58 |
| Combo Adaptive Regime V1 | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €425,38 | €850,76 | €48,95 | €-8,88 |
| Combo Adaptive Quality7 Regime V1 | PUMP | LONG | Combo Adaptive | 60m | 2,0x | 0,00502 | 0,00497 | 0,00460 | 0,00254 | 0,00587 | €295,78 | €591,56 | €49,57 | €-6,59 |
| Combo Adaptive Quality7 Regime V1 | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,70354 | 2,48800 | 2,42548 | 1,36529 | 3,25967 | €242,50 | €485,00 | €49,88 | €-38,67 |
| Combo Adaptive Long Only V1 | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €645,48 | €1.290,95 | €46,47 | €0,00 |
| Combo Adaptive Long Only V1 | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €308,39 | €616,77 | €53,69 | €-22,87 |
| Combo Adaptive Long Only V1 | PUMP | LONG | Combo Adaptive | 60m | 2,0x | 0,00502 | 0,00497 | 0,00460 | 0,00254 | 0,00587 | €312,68 | €625,36 | €52,40 | €-6,97 |
| Combo Adaptive Partial 1R V1 | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,01735 | 121,01735 | 128,90956 | 180,92093 | 105,23292 | €352,70 | €705,40 | €46,00 | €-0,00 |
| Combo Adaptive Partial 1R V1 | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €292,79 | €585,58 | €50,97 | €-21,71 |
| Combo Adaptive Partial 1R V1 | SOL | LONG | Combo Adaptive | 60m | 2,0x | 94,24985 | 94,06500 | 90,79388 | 47,59617 | 101,16178 | €12,54 | €25,08 | €0,92 | €-0,05 |
| Combo Adaptive Partial 1R V1 | PUMP | LONG | Combo Adaptive | 60m | 2,0x | 0,00502 | 0,00497 | 0,00460 | 0,00254 | 0,00587 | €16,58 | €33,16 | €2,78 | €-0,37 |
| Combo Adaptive Quality7 Regime Partial 1R V1 | PUMP | LONG | Combo Adaptive | 60m | 2,0x | 0,00502 | 0,00497 | 0,00460 | 0,00254 | 0,00587 | €299,55 | €599,09 | €50,20 | €-6,68 |
| Combo Adaptive Quality7 Regime Partial 1R V1 | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,70354 | 2,48800 | 2,42548 | 1,36529 | 3,25967 | €245,59 | €491,18 | €50,52 | €-39,16 |
| Sol Ema 1H | SOL | LONG | Trend following EMA | 60m | 3,0x | 95,05001 | 94,06500 | 90,49549 | 63,84192 | 104,15904 | €349,20 | €1.047,59 | €50,20 | €-10,86 |
| Sol Ema 4H | SOL | LONG | Trend following EMA | 240m | 2,0x | 93,39968 | 94,06500 | 86,82624 | 47,16684 | 109,83325 | €356,10 | €712,19 | €50,12 | €5,07 |
| Sol Adaptive 1H | SOL | LONG | Combo Adaptive | 60m | 3,0x | 95,05001 | 94,06500 | 90,49549 | 63,84192 | 104,15904 | €344,23 | €1.032,69 | €49,48 | €-10,70 |
| Sol Adaptive 4H | SOL | LONG | Combo Adaptive | 240m | 2,0x | 93,39968 | 94,06500 | 86,22866 | 47,16684 | 111,32722 | €330,98 | €661,97 | €50,82 | €4,72 |
| Eth Ema 4H | ETH | LONG | Trend following EMA | 240m | 2,0x | 2390,02791 | 2437,32000 | 2268,60778 | 1206,96409 | 2693,57826 | €487,73 | €975,47 | €49,56 | €19,30 |
| Doge Ema 1H | DOGE | LONG | Trend following EMA | 60m | 3,0x | 0,09314 | 0,09209 | 0,08689 | 0,06256 | 0,10563 | €248,90 | €746,70 | €50,09 | €-8,41 |
| Master Adaptive Expanded V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03814 | 0,02188 | 0,05374 | €197,50 | €395,01 | €47,40 | €0,00 |
| Master Adaptive Runner25 V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03814 | 0,02188 | 0,05894 | €34,77 | €69,54 | €8,34 | €0,00 |
| Combo Adaptive Side Regime Guard V1 | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €77,52 | €155,04 | €5,58 | €0,00 |
| Combo Adaptive Side Regime Guard V1 | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 807,93155 | 831,89000 | 737,89694 | 408,00543 | 948,00078 | €305,89 | €611,78 | €53,03 | €18,14 |
| Combo Adaptive Side Regime Guard V1 | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €304,59 | €609,17 | €53,03 | €-22,59 |
| Combo Adaptive Side Regime Guard V1 | SOL | LONG | Combo Adaptive | 60m | 2,0x | 94,24985 | 94,06500 | 90,79388 | 47,59617 | 101,16178 | €14,20 | €28,40 | €1,04 | €-0,06 |
| Master Adaptive Gb20 Loss Cap V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03828 | 0,02188 | 0,05682 | €195,70 | €391,41 | €45,67 | €0,00 |
| Main Side Regime Guard V1 | VELVET | LONG | Confluenza trend | 240m | 3,0x | 0,55987 | 0,55987 | 0,49269 | 0,37605 | 0,69424 | €142,25 | €426,74 | €51,21 | €0,00 |
| Main Side Regime Guard V1 | AKE | LONG | Confluenza trend | 240m | 3,0x | 0,01021 | 0,01021 | 0,00899 | 0,00686 | 0,01266 | €145,97 | €437,90 | €52,55 | €0,00 |
| Main Side Regime Guard V1 | PUMP | LONG | Confluenza trend | 240m | 3,0x | 0,00468 | 0,00497 | 0,00481 | 0,00314 | 0,00580 | €149,89 | €449,66 | €0,00 | €28,09 |
| Main Side Regime Guard V1 | HYPE | LONG | Confluenza trend | 240m | 3,0x | 77,65853 | 79,80100 | 71,20755 | 52,16065 | 90,56048 | €216,52 | €649,56 | €53,96 | €17,92 |
| Main Side Regime Guard V1 | XRP | LONG | Confluenza trend | 240m | 3,0x | 1,47102 | 1,47325 | 1,31178 | 0,98804 | 1,78951 | €12,77 | €38,31 | €4,15 | €0,06 |
| Main Side Regime Guard V1 | ETH | LONG | Confluenza trend | 240m | 3,0x | 2437,91749 | 2437,32000 | 2326,72117 | 1637,46791 | 2660,31012 | €9,94 | €29,83 | €1,36 | €-0,01 |
| Main Dynamic Asset Selector V1 | PUMP | LONG | Confluenza trend | 240m | 3,0x | 0,00515 | 0,00497 | 0,00453 | 0,00346 | 0,00638 | €141,85 | €425,56 | €51,07 | €-14,72 |
| Combo Trend Side Regime Guard V1 | ZEC | LONG | Combo Trend | 60m | 2,0x | 822,67450 | 831,89000 | 761,05343 | 415,45062 | 958,24084 | €381,00 | €762,00 | €57,08 | €8,54 |
| Combo Trend Side Regime Guard V1 | PEPE | LONG | Combo Trend | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00001 | €293,50 | €586,99 | €56,78 | €-21,77 |
| Combo Trend Side Regime Guard V1 | SOL | LONG | Combo Trend | 60m | 2,0x | 94,24985 | 94,06500 | 90,40989 | 47,59617 | 102,69776 | €13,97 | €27,94 | €1,14 | €-0,05 |
| Combo Trend Side Regime Guard V1 | PUMP | LONG | Combo Trend | 60m | 2,0x | 0,00523 | 0,00497 | 0,00474 | 0,00264 | 0,00631 | €294,84 | €589,68 | €55,15 | €-29,65 |
| 1H Balanced V3 Long Only V1 | SKHYNIX | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1220,85412 | 1220,85412 | 1177,63561 | 820,00702 | 1307,29117 | €435,49 | €1.306,46 | €46,25 | €0,00 |
| 1H Balanced V3 Long Only V1 | ZEC | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 807,93155 | 831,89000 | 737,89694 | 542,66069 | 948,00078 | €184,72 | €554,15 | €48,04 | €16,43 |
| 1H Balanced V3 Long Only V1 | XRP | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1,47399 | 1,47325 | 1,35380 | 0,99003 | 1,71438 | €194,69 | €584,07 | €47,63 | €-0,30 |
| 1H Balanced V3 Long Only V1 | PUMP | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,00523 | 0,00497 | 0,00479 | 0,00351 | 0,00611 | €184,35 | €553,04 | €46,55 | €-27,81 |
| 1H Balanced V3 Long Only V1 | SUI | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,84147 | 0,82480 | 0,80853 | 0,56519 | 0,90734 | €9,09 | €27,28 | €1,07 | €-0,54 |
| Scanner Bottom5 Short Profit Lock V1 | SOXL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €381,80 | €763,60 | €48,45 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | SNDK | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €496,62 | €993,25 | €48,08 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | SOXL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €382,38 | €764,76 | €48,52 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | SNDK | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €497,38 | €994,76 | €48,15 | €-0,00 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1H Fast V3 No Esports V1 | BTC | LONG | 2026-08-24T05:00:00+00:00 | 76820,29411 | €-0,51 | -1,12 | STOP |
| 1H Fast Score 6 75 Cost Aware V1 | BTC | LONG | 2026-08-24T05:00:00+00:00 | 76820,29411 | €-0,58 | -1,12 | STOP |
| Combo Trend Side Regime Guard V1 | HYPE | LONG | 2026-08-24T03:45:00+00:00 | 79,29354 | €-55,77 | -1,04 | STOP |
| Scanner Top5 Btc Guard V1 | HYPE | LONG | 2026-08-24T03:30:00+00:00 | 79,61608 | €-49,77 | -1,04 | STOP |
| Scanner Top5 Btc Guard Mfe V1 | HYPE | LONG | 2026-08-24T03:30:00+00:00 | 79,61608 | €-48,61 | -1,04 | STOP |
| Benchmark trend following EMA 1H | HYPE | LONG | 2026-08-24T03:30:00+00:00 | 79,33676 | €-1,51 | -1,04 | STOP |
| Donchian 1H Gb20 120R V1 | HYPE | LONG | 2026-08-24T03:30:00+00:00 | 79,61436 | €-57,76 | -1,04 | STOP |
| Benchmark Donchian breakout 1H | HYPE | LONG | 2026-08-24T03:30:00+00:00 | 79,61436 | €-59,15 | -1,04 | STOP |
| 1H Fast V3 No Esports Long Only V1 | SUI | LONG | 2026-08-24T02:15:00+00:00 | 0,81569 | €-0,85 | -1,05 | STOP |
| 1H Fast Tp2 V1 | SUI | LONG | 2026-08-24T02:15:00+00:00 | 0,81569 | €-0,86 | -1,05 | STOP |
| 1H Balanced Long No Rhv V1 | XRP | LONG | 2026-08-24T02:15:00+00:00 | 1,46240 | €-1,13 | -1,04 | STOP |
| 1H Fast V3 No Esports V1 | SUI | LONG | 2026-08-24T02:00:00+00:00 | 0,82310 | €-1,48 | -1,05 | STOP |

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

Generato: 2026-08-24 05:32 UTC


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

Segnali totali salvati: **135**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08-24 | BTC | 76.958,14 | +6 | +2 | +2 | 0 | +3 | +1 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-08-24 | DOGE | 0.09174 | +4 | +1 | +1 | 0 | +3 | +1 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-08-24 | SOL | 93,82 | +6 | +1 | +1 | 0 | +3 | +1 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-08-23 | BTC | 76.280,85 | +7 | +2 | +2 | 0 | +3 | +1 | 0 | ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA |
| 2026-08-23 | DOGE | 0.09044 | +7 | +2 | +2 | 0 | +3 | +1 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-08-23 | SOL | 93,05 | +3 | -1 | -1 | 0 | +3 | +1 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-08-22 | BTC | 77.109,54 | +5 | +1 | +1 | 0 | +3 | +1 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-08-22 | DOGE | 0.09028 | +6 | +1 | +1 | 0 | +3 | +1 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-08-22 | SOL | 93,36 | +3 | -1 | -1 | 0 | +3 | +1 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-08-21 | BTC | 75.089,33 | +5 | +1 | +1 | 0 | +3 | +1 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-08-21 | DOGE | 0.08259 | +2 | +1 | +1 | 0 | +2 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-08-21 | SOL | 89,61 | +2 | -1 | -1 | 0 | +3 | +1 | 0 | HOLD LEGGERO / ATTESA CONFERME |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 45 | 44 | 43 | 42 | 40 | 38 | 35 | 33 | 26 | 17 | 2 | 0 |
| SOL | 45 | 44 | 43 | 42 | 40 | 38 | 35 | 33 | 26 | 17 | 2 | 0 |
| DOGE | 45 | 44 | 43 | 42 | 40 | 38 | 35 | 33 | 26 | 17 | 2 | 0 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-07-11 | 45g | 2026-08-25 | domani |
| SOL | 2026-07-11 | 45g | 2026-08-25 | domani |
| DOGE | 2026-07-11 | 45g | 2026-08-25 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 41 | 53,66% | +0,50% | +0,47% | PRIMA CALIBRAZIONE |
| BTC | 2g | 40 | 52,50% | +0,85% | +0,73% | PRIMA CALIBRAZIONE |
| BTC | 3g | 39 | 48,72% | +1,08% | +0,90% | PRIMA CALIBRAZIONE |
| BTC | 5g | 37 | 37,84% | +1,90% | +1,56% | PRIMA CALIBRAZIONE |
| BTC | 7g | 36 | 47,22% | +2,33% | +2,03% | PRIMA CALIBRAZIONE |
| BTC | 10g | 33 | 45,45% | +1,60% | +1,32% | PRIMA CALIBRAZIONE |
| BTC | 14g | 31 | 54,84% | +2,57% | +2,46% | PRIMA CALIBRAZIONE |
| BTC | 21g | 24 | 41,67% | +3,36% | +3,08% | FEEDBACK RAPIDO |
| BTC | 30g | 15 | 86,67% | +3,97% | +4,31% | FEEDBACK RAPIDO |
| BTC | 45g | 2 | 100,00% | +20,57% | +20,57% | FEEDBACK RAPIDO |
| BTC | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 1g | 37 | 56,76% | +0,62% | +0,45% | PRIMA CALIBRAZIONE |
| SOL | 2g | 36 | 52,78% | +1,25% | +1,06% | PRIMA CALIBRAZIONE |
| SOL | 3g | 35 | 54,29% | +2,05% | +1,79% | PRIMA CALIBRAZIONE |
| SOL | 5g | 33 | 57,58% | +3,02% | +2,86% | PRIMA CALIBRAZIONE |
| SOL | 7g | 31 | 61,29% | +2,88% | +3,05% | PRIMA CALIBRAZIONE |
| SOL | 10g | 28 | 60,71% | +1,91% | +2,18% | FEEDBACK RAPIDO |
| SOL | 14g | 26 | 69,23% | +3,30% | +4,70% | FEEDBACK RAPIDO |
| SOL | 21g | 20 | 60,00% | +4,15% | +2,37% | FEEDBACK RAPIDO |
| SOL | 30g | 14 | 42,86% | +2,59% | +0,37% | FEEDBACK RAPIDO |
| SOL | 45g | 1 | 100,00% | +19,26% | +19,26% | FEEDBACK RAPIDO |
| SOL | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 1g | 42 | 50,00% | +0,65% | +0,64% | PRIMA CALIBRAZIONE |
| DOGE | 2g | 41 | 51,22% | +1,29% | +1,28% | PRIMA CALIBRAZIONE |
| DOGE | 3g | 40 | 50,00% | +1,89% | +2,18% | PRIMA CALIBRAZIONE |
| DOGE | 5g | 38 | 57,89% | +2,54% | +3,20% | PRIMA CALIBRAZIONE |
| DOGE | 7g | 36 | 63,89% | +2,26% | +3,49% | PRIMA CALIBRAZIONE |
| DOGE | 10g | 33 | 57,58% | +0,56% | +2,44% | PRIMA CALIBRAZIONE |
| DOGE | 14g | 31 | 64,52% | +2,00% | +5,00% | PRIMA CALIBRAZIONE |
| DOGE | 21g | 25 | 68,00% | +1,97% | +0,39% | FEEDBACK RAPIDO |
| DOGE | 30g | 17 | 70,59% | +3,23% | -3,23% | FEEDBACK RAPIDO |
| DOGE | 45g | 2 | 0,00% | +24,16% | -24,16% | FEEDBACK RAPIDO |
| DOGE | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 41 | 53,66% | +0,50% | +0,47% | +0,10% | +1,10% | PRIMA CALIBRAZIONE |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 44 | 56,82% | +0,46% | +0,46% | +0,08% | +1,04% | PRIMA CALIBRAZIONE |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 44 | 56,82% | +0,46% | +0,46% | +0,08% | +1,04% | PRIMA CALIBRAZIONE |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,25% | +0,25% | -0,10% | +0,70% | PRIMA CALIBRAZIONE |
| BTC | 1g | Tecnico | CALIBRABILE | 39 | 38,46% | +0,64% | +0,12% | +0,24% | +1,23% | PRIMA CALIBRAZIONE |
| BTC | 1g | Classic technical | CALIBRABILE | 12 | 33,33% | +1,31% | +0,43% | +0,62% | +1,94% | FEEDBACK RAPIDO |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +1,45% | +1,45% | +1,10% | +2,07% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 40 | 52,50% | +0,85% | +0,73% | +0,32% | +1,59% | PRIMA CALIBRAZIONE |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 43 | 55,81% | +0,97% | +0,97% | +0,45% | +1,70% | PRIMA CALIBRAZIONE |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 43 | 55,81% | +0,97% | +0,97% | +0,45% | +1,70% | PRIMA CALIBRAZIONE |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,52% | +0,52% | -0,02% | +1,18% | PRIMA CALIBRAZIONE |
| BTC | 2g | Tecnico | CALIBRABILE | 38 | 42,11% | +1,23% | +0,14% | +0,72% | +1,97% | PRIMA CALIBRAZIONE |
| BTC | 2g | Classic technical | CALIBRABILE | 11 | 27,27% | +1,80% | +0,42% | +1,46% | +2,69% | FEEDBACK RAPIDO |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +3,18% | +3,18% | +3,05% | +3,89% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 39 | 48,72% | +1,08% | +0,90% | -0,80% | +2,77% | PRIMA CALIBRAZIONE |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 42 | 59,52% | +1,47% | +1,47% | -0,78% | +3,07% | PRIMA CALIBRAZIONE |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 42 | 59,52% | +1,47% | +1,47% | -0,78% | +3,07% | PRIMA CALIBRAZIONE |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 35 | 57,14% | +0,91% | +0,91% | -1,00% | +2,36% | PRIMA CALIBRAZIONE |
| BTC | 3g | Tecnico | CALIBRABILE | 37 | 35,14% | +1,93% | -0,34% | -0,52% | +3,48% | PRIMA CALIBRAZIONE |
| BTC | 3g | Classic technical | CALIBRABILE | 10 | 30,00% | +3,14% | -0,71% | +0,49% | +4,52% | FEEDBACK RAPIDO |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,88% | +1,88% | +1,44% | +4,24% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 37 | 37,84% | +1,90% | +1,56% | -1,64% | +3,97% | PRIMA CALIBRAZIONE |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 40 | 47,50% | +2,24% | +2,24% | -1,59% | +4,40% | PRIMA CALIBRAZIONE |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 40 | 47,50% | +2,24% | +2,24% | -1,59% | +4,40% | PRIMA CALIBRAZIONE |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 35 | 48,57% | +2,08% | +2,08% | -1,57% | +4,07% | PRIMA CALIBRAZIONE |
| BTC | 5g | Tecnico | CALIBRABILE | 35 | 34,29% | +2,71% | -2,12% | -1,33% | +4,92% | PRIMA CALIBRAZIONE |
| BTC | 5g | Classic technical | CALIBRABILE | 8 | 12,50% | +7,26% | -7,26% | -0,63% | +8,70% | FEEDBACK RAPIDO |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,16% | -0,16% | -0,37% | +4,24% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 36 | 47,22% | +2,33% | +2,03% | -2,11% | +4,78% | PRIMA CALIBRAZIONE |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 38 | 55,26% | +2,18% | +2,18% | -2,11% | +4,66% | PRIMA CALIBRAZIONE |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 38 | 55,26% | +2,18% | +2,18% | -2,11% | +4,66% | PRIMA CALIBRAZIONE |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 34 | 58,82% | +2,59% | +2,59% | -2,06% | +4,93% | PRIMA CALIBRAZIONE |
| BTC | 7g | Tecnico | CALIBRABILE | 33 | 30,30% | +2,85% | -3,31% | -1,86% | +5,21% | PRIMA CALIBRAZIONE |
| BTC | 7g | Classic technical | CALIBRABILE | 8 | 0,00% | +11,51% | -11,51% | -0,67% | +13,66% | FEEDBACK RAPIDO |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,77% | +1,77% | -0,79% | +4,24% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 33 | 45,45% | +1,60% | +1,32% | -2,59% | +4,11% | PRIMA CALIBRAZIONE |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 35 | 51,43% | +1,37% | +1,37% | -2,61% | +4,02% | PRIMA CALIBRAZIONE |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 35 | 51,43% | +1,37% | +1,37% | -2,61% | +4,02% | PRIMA CALIBRAZIONE |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 31 | 58,06% | +1,81% | +1,81% | -2,51% | +4,24% | PRIMA CALIBRAZIONE |
| BTC | 10g | Tecnico | CALIBRABILE | 30 | 33,33% | +1,79% | -0,28% | -2,35% | +4,49% | PRIMA CALIBRAZIONE |
| BTC | 10g | Classic technical | CALIBRABILE | 5 | 0,00% | +5,58% | -5,58% | -1,17% | +7,97% | FEEDBACK RAPIDO |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,43% | -0,43% | -2,30% | +4,24% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 31 | 54,84% | +2,57% | +2,46% | -2,91% | +5,73% | PRIMA CALIBRAZIONE |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 33 | 54,55% | +2,32% | +2,32% | -2,93% | +5,55% | PRIMA CALIBRAZIONE |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 33 | 54,55% | +2,32% | +2,32% | -2,93% | +5,55% | PRIMA CALIBRAZIONE |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 29 | 62,07% | +2,99% | +2,99% | -2,72% | +5,98% | FEEDBACK RAPIDO |
| BTC | 14g | Tecnico | CALIBRABILE | 28 | 64,29% | +2,97% | +2,91% | -2,65% | +6,24% | FEEDBACK RAPIDO |
| BTC | 14g | Classic technical | CALIBRABILE | 4 | 50,00% | +0,27% | -0,27% | -1,55% | +3,37% | FEEDBACK RAPIDO |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -2,25% | -2,25% | -3,05% | +4,24% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 24 | 41,67% | +3,36% | +3,08% | -2,93% | +7,10% | FEEDBACK RAPIDO |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 26 | 53,85% | +3,01% | +3,01% | -2,98% | +6,76% | FEEDBACK RAPIDO |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 26 | 53,85% | +3,01% | +3,01% | -2,98% | +6,76% | FEEDBACK RAPIDO |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 22 | 59,09% | +3,81% | +3,81% | -2,71% | +7,55% | FEEDBACK RAPIDO |
| BTC | 21g | Tecnico | CALIBRABILE | 21 | 19,05% | +3,36% | -3,68% | -2,63% | +7,21% | FEEDBACK RAPIDO |
| BTC | 21g | Classic technical | CALIBRABILE | 4 | 0,00% | +11,68% | -11,68% | -1,55% | +14,27% | FEEDBACK RAPIDO |
| BTC | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,21% | +1,21% | -3,06% | +4,24% | FEEDBACK RAPIDO |
| BTC | 30g | Global confluence | BENCHMARK | 15 | 86,67% | +3,97% | +4,31% | -3,21% | +7,97% | FEEDBACK RAPIDO |
| BTC | 30g | Famiglia statistica | CALIBRABILE | 17 | 70,59% | +4,45% | +4,45% | -3,26% | +8,58% | FEEDBACK RAPIDO |
| BTC | 30g | Scanner grezzo | DIAGNOSTICO | 17 | 70,59% | +4,45% | +4,45% | -3,26% | +8,58% | FEEDBACK RAPIDO |
| BTC | 30g | Market regime grezzo | DIAGNOSTICO | 13 | 69,23% | +4,37% | +4,37% | -2,88% | +9,05% | FEEDBACK RAPIDO |
| BTC | 30g | Tecnico | CALIBRABILE | 14 | 35,71% | +3,91% | -4,27% | -2,94% | +8,61% | FEEDBACK RAPIDO |
| BTC | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +0,16% | +0,16% | -3,06% | +4,24% | FEEDBACK RAPIDO |
| BTC | 45g | Global confluence | BENCHMARK | 2 | 100,00% | +20,57% | +20,57% | -2,80% | +25,05% | FEEDBACK RAPIDO |
| BTC | 45g | Famiglia statistica | CALIBRABILE | 2 | 100,00% | +20,57% | +20,57% | -2,80% | +25,05% | FEEDBACK RAPIDO |
| BTC | 45g | Scanner grezzo | DIAGNOSTICO | 2 | 100,00% | +20,57% | +20,57% | -2,80% | +25,05% | FEEDBACK RAPIDO |
| BTC | 45g | Market regime grezzo | DIAGNOSTICO | 2 | 100,00% | +20,57% | +20,57% | -2,80% | +25,05% | FEEDBACK RAPIDO |
| BTC | 45g | Tecnico | CALIBRABILE | 1 | 0,00% | +20,63% | -20,63% | -2,32% | +25,66% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 42 | 50,00% | +0,65% | +0,64% | +0,12% | +1,73% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 44 | 59,09% | +0,53% | +0,81% | -0,00% | +1,58% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 44 | 59,09% | +0,53% | +0,81% | -0,00% | +1,58% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,15% | +0,26% | -0,32% | +0,87% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Tecnico | CALIBRABILE | 37 | 56,76% | +0,47% | +0,70% | -0,10% | +1,49% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Classic technical | CALIBRABILE | 29 | 41,38% | +0,47% | -0,36% | -0,07% | +1,22% | FEEDBACK RAPIDO |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 6 | 66,67% | +3,11% | +2,58% | +1,68% | +3,93% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 41 | 51,22% | +1,29% | +1,28% | +0,60% | +2,70% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 43 | 53,49% | +1,13% | +1,35% | +0,45% | +2,50% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 43 | 53,49% | +1,13% | +1,35% | +0,45% | +2,50% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 38 | 50,00% | +0,36% | +0,74% | -0,26% | +1,41% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Tecnico | CALIBRABILE | 36 | 63,89% | +0,64% | +1,15% | +0,02% | +1,96% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Classic technical | CALIBRABILE | 28 | 46,43% | +1,10% | -0,98% | +0,41% | +2,12% | FEEDBACK RAPIDO |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 6 | 66,67% | +5,87% | +5,43% | +5,07% | +8,56% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 40 | 50,00% | +1,89% | +2,18% | -1,00% | +4,61% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 42 | 54,76% | +1,70% | +2,00% | -1,12% | +4,35% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 42 | 54,76% | +1,70% | +2,00% | -1,12% | +4,35% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,84% | +1,55% | -1,48% | +3,36% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Tecnico | CALIBRABILE | 35 | 51,43% | +0,68% | +1,16% | -1,38% | +3,07% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Classic technical | CALIBRABILE | 27 | 33,33% | +1,97% | -1,97% | -1,30% | +4,60% | FEEDBACK RAPIDO |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +5,63% | +5,21% | +1,37% | +9,34% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 38 | 57,89% | +2,54% | +3,20% | -2,12% | +5,98% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 40 | 55,00% | +2,31% | +2,95% | -2,20% | +5,67% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 40 | 55,00% | +2,31% | +2,95% | -2,20% | +5,67% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +2,45% | +3,08% | -2,17% | +5,74% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Tecnico | CALIBRABILE | 33 | 63,64% | +0,95% | +0,56% | -2,69% | +4,03% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Classic technical | CALIBRABILE | 27 | 44,44% | +3,71% | -3,71% | -1,98% | +7,48% | FEEDBACK RAPIDO |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 50,00% | +0,64% | +0,23% | -0,37% | +5,72% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 36 | 63,89% | +2,26% | +3,49% | -2,76% | +6,24% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 38 | 60,53% | +2,02% | +3,15% | -2,85% | +5,96% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 38 | 60,53% | +2,02% | +3,15% | -2,85% | +5,96% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 36 | 61,11% | +2,19% | +3,26% | -2,86% | +6,04% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Tecnico | CALIBRABILE | 33 | 63,64% | +1,75% | +1,79% | -3,12% | +5,79% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Classic technical | CALIBRABILE | 25 | 48,00% | +2,39% | -2,39% | -2,84% | +6,41% | FEEDBACK RAPIDO |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 50,00% | +0,63% | +0,36% | -0,50% | +5,72% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 33 | 57,58% | +0,56% | +2,44% | -3,42% | +4,74% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 35 | 57,14% | +0,42% | +2,23% | -3,48% | +4,53% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 35 | 57,14% | +0,42% | +2,23% | -3,48% | +4,53% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 33 | 57,58% | +0,50% | +2,31% | -3,48% | +4,53% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Tecnico | CALIBRABILE | 30 | 66,67% | -1,40% | +1,40% | -3,88% | +2,63% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Classic technical | CALIBRABILE | 23 | 56,52% | +0,32% | -0,32% | -3,55% | +4,70% | FEEDBACK RAPIDO |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 75,00% | +0,93% | +0,18% | -1,31% | +5,72% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 31 | 64,52% | +2,00% | +5,00% | -4,13% | +7,27% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 33 | 69,70% | +1,75% | +4,59% | -4,15% | +6,89% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 33 | 69,70% | +1,75% | +4,59% | -4,15% | +6,89% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 31 | 70,97% | +1,97% | +4,79% | -4,18% | +7,05% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Tecnico | CALIBRABILE | 30 | 66,67% | -0,31% | +0,31% | -4,43% | +4,70% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Classic technical | CALIBRABILE | 22 | 63,64% | +0,33% | -0,33% | -4,43% | +5,27% | FEEDBACK RAPIDO |
| DOGE | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 75,00% | +12,47% | +2,65% | -1,31% | +16,91% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 25 | 68,00% | +1,97% | +0,39% | -5,11% | +8,04% | FEEDBACK RAPIDO |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 26 | 80,77% | +1,75% | +6,30% | -5,17% | +7,73% | FEEDBACK RAPIDO |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 26 | 80,77% | +1,75% | +6,30% | -5,17% | +7,73% | FEEDBACK RAPIDO |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 24 | 83,33% | +2,00% | +6,72% | -5,29% | +8,00% | FEEDBACK RAPIDO |
| DOGE | 21g | Tecnico | CALIBRABILE | 26 | 73,08% | +1,75% | -1,75% | -5,17% | +7,73% | FEEDBACK RAPIDO |
| DOGE | 21g | Classic technical | CALIBRABILE | 20 | 75,00% | +0,03% | -0,03% | -5,18% | +6,01% | FEEDBACK RAPIDO |
| DOGE | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +0,76% | +0,76% | -1,85% | +6,57% | FEEDBACK RAPIDO |
| DOGE | 30g | Global confluence | BENCHMARK | 17 | 70,59% | +3,23% | -3,23% | -6,05% | +9,72% | FEEDBACK RAPIDO |
| DOGE | 30g | Famiglia statistica | CALIBRABILE | 17 | 76,47% | +3,23% | +0,54% | -6,05% | +9,72% | FEEDBACK RAPIDO |
| DOGE | 30g | Scanner grezzo | DIAGNOSTICO | 17 | 76,47% | +3,23% | +0,54% | -6,05% | +9,72% | FEEDBACK RAPIDO |
| DOGE | 30g | Market regime grezzo | DIAGNOSTICO | 15 | 86,67% | -0,07% | +4,34% | -6,36% | +6,05% | FEEDBACK RAPIDO |
| DOGE | 30g | Tecnico | CALIBRABILE | 17 | 70,59% | +3,23% | -3,23% | -6,05% | +9,72% | FEEDBACK RAPIDO |
| DOGE | 30g | Classic technical | CALIBRABILE | 16 | 68,75% | +3,81% | -3,81% | -5,92% | +10,30% | FEEDBACK RAPIDO |
| DOGE | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +31,53% | +31,53% | -1,85% | +40,20% | FEEDBACK RAPIDO |
| DOGE | 45g | Global confluence | BENCHMARK | 2 | 0,00% | +24,16% | -24,16% | -7,34% | +32,34% | FEEDBACK RAPIDO |
| DOGE | 45g | Famiglia statistica | CALIBRABILE | 2 | 0,00% | +24,16% | -24,16% | -7,34% | +32,34% | FEEDBACK RAPIDO |
| DOGE | 45g | Scanner grezzo | DIAGNOSTICO | 2 | 0,00% | +24,16% | -24,16% | -7,34% | +32,34% | FEEDBACK RAPIDO |
| DOGE | 45g | Market regime grezzo | DIAGNOSTICO | 2 | 0,00% | +24,16% | -24,16% | -7,34% | +32,34% | FEEDBACK RAPIDO |
| DOGE | 45g | Tecnico | CALIBRABILE | 2 | 0,00% | +24,16% | -24,16% | -7,34% | +32,34% | FEEDBACK RAPIDO |
| DOGE | 45g | Classic technical | CALIBRABILE | 2 | 0,00% | +24,16% | -24,16% | -7,34% | +32,34% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 37 | 56,76% | +0,62% | +0,45% | +0,04% | +1,61% | PRIMA CALIBRAZIONE |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 39 | 58,97% | +0,21% | +0,20% | -0,28% | +1,16% | PRIMA CALIBRAZIONE |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 42 | 57,14% | +0,28% | +0,10% | -0,23% | +1,21% | PRIMA CALIBRAZIONE |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +0,27% | +0,39% | -0,30% | +0,87% | PRIMA CALIBRAZIONE |
| SOL | 1g | Tecnico | CALIBRABILE | 41 | 51,22% | +0,22% | +0,19% | -0,33% | +1,11% | PRIMA CALIBRAZIONE |
| SOL | 1g | Classic technical | CALIBRABILE | 25 | 52,00% | +0,44% | +0,37% | -0,23% | +1,51% | FEEDBACK RAPIDO |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +1,51% | +1,51% | +0,99% | +5,02% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 36 | 52,78% | +1,25% | +1,06% | +0,52% | +2,44% | PRIMA CALIBRAZIONE |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 38 | 50,00% | +0,72% | +0,62% | -0,03% | +1,55% | PRIMA CALIBRAZIONE |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 41 | 48,78% | +0,69% | +0,55% | -0,03% | +1,64% | PRIMA CALIBRAZIONE |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +0,76% | +0,78% | -0,00% | +1,60% | PRIMA CALIBRAZIONE |
| SOL | 2g | Tecnico | CALIBRABILE | 40 | 42,50% | +0,60% | -0,17% | -0,07% | +1,78% | PRIMA CALIBRAZIONE |
| SOL | 2g | Classic technical | CALIBRABILE | 24 | 54,17% | +0,62% | +0,58% | +0,05% | +1,68% | FEEDBACK RAPIDO |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 33,33% | +0,74% | +0,74% | +0,30% | +2,88% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 35 | 54,29% | +2,05% | +1,79% | -1,11% | +4,27% | PRIMA CALIBRAZIONE |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 37 | 48,65% | +1,34% | +1,30% | -1,55% | +3,56% | PRIMA CALIBRAZIONE |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 40 | 47,50% | +1,26% | +1,18% | -1,53% | +3,55% | PRIMA CALIBRAZIONE |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +1,43% | +1,38% | -1,48% | +3,53% | PRIMA CALIBRAZIONE |
| SOL | 3g | Tecnico | CALIBRABILE | 39 | 43,59% | +1,06% | -0,63% | -1,63% | +3,17% | PRIMA CALIBRAZIONE |
| SOL | 3g | Classic technical | CALIBRABILE | 23 | 47,83% | +0,74% | +0,50% | -1,52% | +2,85% | FEEDBACK RAPIDO |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 33,33% | +0,33% | +0,33% | -1,17% | +5,20% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 33 | 57,58% | +3,02% | +2,86% | -1,94% | +6,07% | PRIMA CALIBRAZIONE |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 36 | 58,33% | +2,57% | +2,77% | -2,23% | +5,54% | PRIMA CALIBRAZIONE |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 39 | 56,41% | +2,43% | +2,50% | -2,22% | +5,41% | PRIMA CALIBRAZIONE |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +2,66% | +2,88% | -2,09% | +5,82% | PRIMA CALIBRAZIONE |
| SOL | 5g | Tecnico | CALIBRABILE | 37 | 40,54% | +1,93% | -2,38% | -2,58% | +4,84% | PRIMA CALIBRAZIONE |
| SOL | 5g | Classic technical | CALIBRABILE | 21 | 52,38% | +0,14% | -0,14% | -2,60% | +2,64% | FEEDBACK RAPIDO |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 0,00% | -2,33% | -2,33% | -3,87% | +1,03% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 31 | 61,29% | +2,88% | +3,05% | -2,80% | +6,36% | PRIMA CALIBRAZIONE |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 34 | 64,71% | +2,32% | +2,99% | -3,07% | +5,85% | PRIMA CALIBRAZIONE |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 37 | 64,86% | +2,12% | +2,76% | -3,04% | +5,69% | PRIMA CALIBRAZIONE |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 32 | 59,38% | +2,70% | +2,76% | -2,93% | +6,14% | PRIMA CALIBRAZIONE |
| SOL | 7g | Tecnico | CALIBRABILE | 36 | 33,33% | +2,22% | -2,78% | -3,11% | +5,86% | PRIMA CALIBRAZIONE |
| SOL | 7g | Classic technical | CALIBRABILE | 21 | 42,86% | -0,04% | +0,04% | -3,16% | +3,15% | FEEDBACK RAPIDO |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 0,00% | -3,55% | -3,55% | -4,19% | +1,03% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 28 | 60,71% | +1,91% | +2,18% | -3,36% | +5,53% | FEEDBACK RAPIDO |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 31 | 64,52% | +1,62% | +2,31% | -3,71% | +5,05% | PRIMA CALIBRAZIONE |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 34 | 61,76% | +1,46% | +2,13% | -3,68% | +4,95% | PRIMA CALIBRAZIONE |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 29 | 58,62% | +2,09% | +1,90% | -3,55% | +5,31% | FEEDBACK RAPIDO |
| SOL | 10g | Tecnico | CALIBRABILE | 33 | 45,45% | +0,80% | -0,95% | -3,81% | +4,59% | PRIMA CALIBRAZIONE |
| SOL | 10g | Classic technical | CALIBRABILE | 21 | 52,38% | -0,08% | +0,08% | -3,74% | +3,68% | FEEDBACK RAPIDO |
| SOL | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 50,00% | -2,05% | -2,05% | -4,86% | +1,05% | FEEDBACK RAPIDO |
| SOL | 10g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 14g | Global confluence | BENCHMARK | 26 | 69,23% | +3,30% | +4,70% | -4,03% | +8,25% | FEEDBACK RAPIDO |
| SOL | 14g | Famiglia statistica | CALIBRABILE | 29 | 82,76% | +3,44% | +4,73% | -4,20% | +7,65% | FEEDBACK RAPIDO |
| SOL | 14g | Scanner grezzo | DIAGNOSTICO | 32 | 84,38% | +2,83% | +4,58% | -4,18% | +7,30% | PRIMA CALIBRAZIONE |
| SOL | 14g | Market regime grezzo | DIAGNOSTICO | 27 | 66,67% | +3,94% | +4,07% | -3,89% | +8,12% | FEEDBACK RAPIDO |
| SOL | 14g | Tecnico | CALIBRABILE | 32 | 34,38% | +2,00% | -2,63% | -4,32% | +6,56% | PRIMA CALIBRAZIONE |
| SOL | 14g | Classic technical | CALIBRABILE | 21 | 38,10% | +1,19% | -1,19% | -4,25% | +5,07% | FEEDBACK RAPIDO |
| SOL | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 50,00% | +8,38% | +8,38% | -5,94% | +13,89% | FEEDBACK RAPIDO |
| SOL | 14g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 21g | Global confluence | BENCHMARK | 20 | 60,00% | +4,15% | +2,37% | -5,91% | +9,66% | FEEDBACK RAPIDO |
| SOL | 21g | Famiglia statistica | CALIBRABILE | 22 | 77,27% | +4,12% | +6,66% | -5,83% | +8,96% | FEEDBACK RAPIDO |
| SOL | 21g | Scanner grezzo | DIAGNOSTICO | 25 | 80,00% | +3,30% | +6,19% | -5,86% | +8,35% | FEEDBACK RAPIDO |
| SOL | 21g | Market regime grezzo | DIAGNOSTICO | 20 | 55,00% | +4,80% | +5,65% | -5,53% | +9,73% | FEEDBACK RAPIDO |
| SOL | 21g | Tecnico | CALIBRABILE | 26 | 46,15% | +3,20% | -4,78% | -5,90% | +8,17% | FEEDBACK RAPIDO |
| SOL | 21g | Classic technical | CALIBRABILE | 18 | 44,44% | +6,55% | -6,55% | -5,27% | +10,76% | FEEDBACK RAPIDO |
| SOL | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -3,18% | -3,18% | -9,62% | +0,62% | FEEDBACK RAPIDO |
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

Generato: 2026-08-24 05:32 UTC

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
| BTC | 45 | PRIMA CALIBRAZIONE | 44 | 13 | 0 | 0 | Famiglia statistica | 1g | 56,82% | +0,46% | prima calibrazione possibile, solo modifiche leggere |
| SOL | 45 | PRIMA CALIBRAZIONE | 41 | 13 | 0 | 0 | Tecnico | 1g | 51,22% | +0,19% | prima calibrazione possibile, solo modifiche leggere |
| DOGE | 45 | PRIMA CALIBRAZIONE | 44 | 14 | 0 | 0 | Famiglia statistica | 1g | 59,09% | +0,81% | prima calibrazione possibile, solo modifiche leggere |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Classic technical | 12 | 33,33% | +0,43% | +1,31% | +0,62% | +1,94% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Famiglia statistica | 44 | 56,82% | +0,46% | +0,46% | +0,08% | +1,04% | PESO OK | 0,0 | MEDIA |
| BTC | 1g | BREVE | Microstruttura exchange | 2 | 100,00% | +1,45% | +1,45% | +1,10% | +2,07% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 39 | 38,46% | +0,12% | +0,64% | +0,24% | +1,23% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 2g | BREVE | Classic technical | 11 | 27,27% | +0,42% | +1,80% | +1,46% | +2,69% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Famiglia statistica | 43 | 55,81% | +0,97% | +0,97% | +0,45% | +1,70% | PESO OK | 0,0 | MEDIA |
| BTC | 2g | BREVE | Microstruttura exchange | 1 | 100,00% | +3,18% | +3,18% | +3,05% | +3,89% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 38 | 42,11% | +0,14% | +1,23% | +0,72% | +1,97% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 3g | BREVE | Classic technical | 10 | 30,00% | -0,71% | +3,14% | +0,49% | +4,52% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Famiglia statistica | 42 | 59,52% | +1,47% | +1,47% | -0,78% | +3,07% | PESO OK | 0,0 | MEDIA |
| BTC | 3g | BREVE | Microstruttura exchange | 1 | 100,00% | +1,88% | +1,88% | +1,44% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 37 | 35,14% | -0,34% | +1,93% | -0,52% | +3,48% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 5g | SETTIMANALE | Classic technical | 8 | 12,50% | -7,26% | +7,26% | -0,63% | +8,70% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 40 | 47,50% | +2,24% | +2,24% | -1,59% | +4,40% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 5g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -0,16% | -0,16% | -0,37% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 35 | 34,29% | -2,12% | +2,71% | -1,33% | +4,92% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 7g | SETTIMANALE | Classic technical | 8 | 0,00% | -11,51% | +11,51% | -0,67% | +13,66% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 38 | 55,26% | +2,18% | +2,18% | -2,11% | +4,66% | PESO OK | 0,0 | MEDIA |
| BTC | 7g | SETTIMANALE | Microstruttura exchange | 1 | 100,00% | +1,77% | +1,77% | -0,79% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 33 | 30,30% | -3,31% | +2,85% | -1,86% | +5,21% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 10g | SETTIMANALE | Classic technical | 5 | 0,00% | -5,58% | +5,58% | -1,17% | +7,97% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 35 | 51,43% | +1,37% | +1,37% | -2,61% | +4,02% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 10g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -0,43% | -0,43% | -2,30% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 30 | 33,33% | -0,28% | +1,79% | -2,35% | +4,49% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 14g | SWING | Classic technical | 4 | 50,00% | -0,27% | +0,27% | -1,55% | +3,37% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Famiglia statistica | 33 | 54,55% | +2,32% | +2,32% | -2,93% | +5,55% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 14g | SWING | Microstruttura exchange | 1 | 0,00% | -2,25% | -2,25% | -3,05% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 28 | 64,29% | +2,91% | +2,97% | -2,65% | +6,24% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Classic technical | 4 | 0,00% | -11,68% | +11,68% | -1,55% | +14,27% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Famiglia statistica | 26 | 53,85% | +3,01% | +3,01% | -2,98% | +6,76% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Microstruttura exchange | 1 | 100,00% | +1,21% | +1,21% | -3,06% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Tecnico | 21 | 19,05% | -3,68% | +3,36% | -2,63% | +7,21% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Famiglia statistica | 17 | 70,59% | +4,45% | +4,45% | -3,26% | +8,58% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Microstruttura exchange | 1 | 100,00% | +0,16% | +0,16% | -3,06% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Tecnico | 14 | 35,71% | -4,27% | +3,91% | -2,94% | +8,61% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Famiglia statistica | 2 | 100,00% | +20,57% | +20,57% | -2,80% | +25,05% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Tecnico | 1 | 0,00% | -20,63% | +20,63% | -2,32% | +25,66% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 29 | 41,38% | -0,36% | +0,47% | -0,07% | +1,22% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Famiglia statistica | 44 | 59,09% | +0,81% | +0,53% | -0,00% | +1,58% | PESO OK | 0,0 | MEDIA |
| DOGE | 1g | BREVE | Microstruttura exchange | 6 | 66,67% | +2,58% | +3,11% | +1,68% | +3,93% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 37 | 56,76% | +0,70% | +0,47% | -0,10% | +1,49% | PESO OK | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Classic technical | 28 | 46,43% | -0,98% | +1,10% | +0,41% | +2,12% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Famiglia statistica | 43 | 53,49% | +1,35% | +1,13% | +0,45% | +2,50% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Microstruttura exchange | 6 | 66,67% | +5,43% | +5,87% | +5,07% | +8,56% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 36 | 63,89% | +1,15% | +0,64% | +0,02% | +1,96% | PESO OK | 0,0 | MEDIA |
| DOGE | 3g | BREVE | Classic technical | 27 | 33,33% | -1,97% | +1,97% | -1,30% | +4,60% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Famiglia statistica | 42 | 54,76% | +2,00% | +1,70% | -1,12% | +4,35% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 3g | BREVE | Microstruttura exchange | 5 | 60,00% | +5,21% | +5,63% | +1,37% | +9,34% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 35 | 51,43% | +1,16% | +0,68% | -1,38% | +3,07% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 5g | SETTIMANALE | Classic technical | 27 | 44,44% | -3,71% | +3,71% | -1,98% | +7,48% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 40 | 55,00% | +2,95% | +2,31% | -2,20% | +5,67% | PESO OK | 0,0 | MEDIA |
| DOGE | 5g | SETTIMANALE | Microstruttura exchange | 4 | 50,00% | +0,23% | +0,64% | -0,37% | +5,72% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 33 | 63,64% | +0,56% | +0,95% | -2,69% | +4,03% | PESO OK | 0,0 | MEDIA |
| DOGE | 7g | SETTIMANALE | Classic technical | 25 | 48,00% | -2,39% | +2,39% | -2,84% | +6,41% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 38 | 60,53% | +3,15% | +2,02% | -2,85% | +5,96% | PESO OK | 0,0 | MEDIA |
| DOGE | 7g | SETTIMANALE | Microstruttura exchange | 4 | 50,00% | +0,36% | +0,63% | -0,50% | +5,72% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 33 | 63,64% | +1,79% | +1,75% | -3,12% | +5,79% | PESO OK | 0,0 | MEDIA |
| DOGE | 10g | SETTIMANALE | Classic technical | 23 | 56,52% | -0,32% | +0,32% | -3,55% | +4,70% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 35 | 57,14% | +2,23% | +0,42% | -3,48% | +4,53% | PESO OK | 0,0 | MEDIA |
| DOGE | 10g | SETTIMANALE | Microstruttura exchange | 4 | 75,00% | +0,18% | +0,93% | -1,31% | +5,72% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 30 | 66,67% | +1,40% | -1,40% | -3,88% | +2,63% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 14g | SWING | Classic technical | 22 | 63,64% | -0,33% | +0,33% | -4,43% | +5,27% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Famiglia statistica | 33 | 69,70% | +4,59% | +1,75% | -4,15% | +6,89% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 14g | SWING | Microstruttura exchange | 4 | 75,00% | +2,65% | +12,47% | -1,31% | +16,91% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 30 | 66,67% | +0,31% | -0,31% | -4,43% | +4,70% | PESO OK | 0,0 | MEDIA |
| DOGE | 21g | SWING | Classic technical | 20 | 75,00% | -0,03% | +0,03% | -5,18% | +6,01% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Famiglia statistica | 26 | 80,77% | +6,30% | +1,75% | -5,17% | +7,73% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Microstruttura exchange | 2 | 100,00% | +0,76% | +0,76% | -1,85% | +6,57% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Tecnico | 26 | 73,08% | -1,75% | +1,75% | -5,17% | +7,73% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Classic technical | 16 | 68,75% | -3,81% | +3,81% | -5,92% | +10,30% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Famiglia statistica | 17 | 76,47% | +0,54% | +3,23% | -6,05% | +9,72% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Microstruttura exchange | 2 | 100,00% | +31,53% | +31,53% | -1,85% | +40,20% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Tecnico | 17 | 70,59% | -3,23% | +3,23% | -6,05% | +9,72% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Classic technical | 2 | 0,00% | -24,16% | +24,16% | -7,34% | +32,34% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Famiglia statistica | 2 | 0,00% | -24,16% | +24,16% | -7,34% | +32,34% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Tecnico | 2 | 0,00% | -24,16% | +24,16% | -7,34% | +32,34% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Classic technical | 25 | 52,00% | +0,37% | +0,44% | -0,23% | +1,51% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Famiglia statistica | 39 | 58,97% | +0,20% | +0,21% | -0,28% | +1,16% | PESO OK | 0,0 | MEDIA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 3 | 66,67% | +1,51% | +1,51% | +0,99% | +5,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 41 | 51,22% | +0,19% | +0,22% | -0,33% | +1,11% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Classic technical | 24 | 54,17% | +0,58% | +0,62% | +0,05% | +1,68% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Famiglia statistica | 38 | 50,00% | +0,62% | +0,72% | -0,03% | +1,55% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Microstruttura exchange | 3 | 33,33% | +0,74% | +0,74% | +0,30% | +2,88% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 40 | 42,50% | -0,17% | +0,60% | -0,07% | +1,78% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Classic technical | 23 | 47,83% | +0,50% | +0,74% | -1,52% | +2,85% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Famiglia statistica | 37 | 48,65% | +1,30% | +1,34% | -1,55% | +3,56% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Microstruttura exchange | 3 | 33,33% | +0,33% | +0,33% | -1,17% | +5,20% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 39 | 43,59% | -0,63% | +1,06% | -1,63% | +3,17% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Classic technical | 21 | 52,38% | -0,14% | +0,14% | -2,60% | +2,64% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 36 | 58,33% | +2,77% | +2,57% | -2,23% | +5,54% | PESO OK | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Microstruttura exchange | 2 | 0,00% | -2,33% | -2,33% | -3,87% | +1,03% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 37 | 40,54% | -2,38% | +1,93% | -2,58% | +4,84% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 7g | SETTIMANALE | Classic technical | 21 | 42,86% | +0,04% | -0,04% | -3,16% | +3,15% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 34 | 64,71% | +2,99% | +2,32% | -3,07% | +5,85% | PESO OK | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Microstruttura exchange | 2 | 0,00% | -3,55% | -3,55% | -4,19% | +1,03% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 36 | 33,33% | -2,78% | +2,22% | -3,11% | +5,86% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 10g | SETTIMANALE | Classic technical | 21 | 52,38% | +0,08% | -0,08% | -3,74% | +3,68% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 31 | 64,52% | +2,31% | +1,62% | -3,71% | +5,05% | PESO OK | 0,0 | MEDIA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Microstruttura exchange | 2 | 50,00% | -2,05% | -2,05% | -4,86% | +1,05% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 33 | 45,45% | -0,95% | +0,80% | -3,81% | +4,59% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 14g | SWING | Classic technical | 21 | 38,10% | -1,19% | +1,19% | -4,25% | +5,07% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Famiglia statistica | 29 | 82,76% | +4,73% | +3,44% | -4,20% | +7,65% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Frattale SOL | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Microstruttura exchange | 2 | 50,00% | +8,38% | +8,38% | -5,94% | +13,89% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Tecnico | 32 | 34,38% | -2,63% | +2,00% | -4,32% | +6,56% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 21g | SWING | Classic technical | 18 | 44,44% | -6,55% | +6,55% | -5,27% | +10,76% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Famiglia statistica | 22 | 77,27% | +6,66% | +4,12% | -5,83% | +8,96% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Frattale SOL | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Microstruttura exchange | 1 | 0,00% | -3,18% | -3,18% | -9,62% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Tecnico | 26 | 46,15% | -4,78% | +3,20% | -5,90% | +8,17% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Classic technical | 9 | 22,22% | -9,59% | +9,59% | -6,82% | +14,73% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Famiglia statistica | 13 | 76,92% | +5,45% | +6,26% | -7,74% | +11,14% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Frattale SOL | 1 | 0,00% | -4,50% | -4,50% | -9,39% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Microstruttura exchange | 1 | 100,00% | +8,54% | +8,54% | -9,62% | +9,47% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Tecnico | 17 | 23,53% | -6,00% | +4,90% | -7,53% | +9,42% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Famiglia statistica | 2 | 0,00% | -20,01% | +20,01% | -9,20% | +27,34% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Frattale SOL | 1 | 100,00% | +19,26% | +19,26% | -9,39% | +23,73% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Tecnico | 2 | 100,00% | +20,01% | +20,01% | -9,20% | +27,34% | OSSERVA | 0,0 | BASSA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 42 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 38 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 44 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Classic technical | 33 | 30,30% | +0,08% |
| BTC | BREVE | Famiglia statistica | 129 | 57,36% | +0,96% |
| BTC | BREVE | Microstruttura exchange | 4 | 100,00% | +1,99% |
| BTC | BREVE | Tecnico | 114 | 38,60% | -0,02% |
| BTC | SETTIMANALE | Classic technical | 21 | 4,76% | -8,48% |
| BTC | SETTIMANALE | Famiglia statistica | 113 | 51,33% | +1,95% |
| BTC | SETTIMANALE | Microstruttura exchange | 3 | 33,33% | +0,39% |
| BTC | SETTIMANALE | Tecnico | 98 | 32,65% | -1,96% |
| BTC | SWING | Classic technical | 8 | 25,00% | -5,98% |
| BTC | SWING | Famiglia statistica | 59 | 54,24% | +2,63% |
| BTC | SWING | Microstruttura exchange | 2 | 50,00% | -0,52% |
| BTC | SWING | Tecnico | 49 | 44,90% | +0,09% |
| BTC | MEDIO | Famiglia statistica | 19 | 73,68% | +6,15% |
| BTC | MEDIO | Microstruttura exchange | 1 | 100,00% | +0,16% |
| BTC | MEDIO | Tecnico | 15 | 33,33% | -5,36% |
| DOGE | BREVE | Classic technical | 84 | 40,48% | -1,08% |
| DOGE | BREVE | Famiglia statistica | 129 | 55,81% | +1,38% |
| DOGE | BREVE | Microstruttura exchange | 17 | 64,71% | +4,36% |
| DOGE | BREVE | Tecnico | 108 | 57,41% | +1,00% |
| DOGE | SETTIMANALE | Classic technical | 75 | 49,33% | -2,23% |
| DOGE | SETTIMANALE | Famiglia statistica | 113 | 57,52% | +2,79% |
| DOGE | SETTIMANALE | Microstruttura exchange | 12 | 58,33% | +0,26% |
| DOGE | SETTIMANALE | Tecnico | 96 | 64,58% | +1,25% |
| DOGE | SWING | Classic technical | 42 | 69,05% | -0,19% |
| DOGE | SWING | Famiglia statistica | 59 | 74,58% | +5,35% |
| DOGE | SWING | Microstruttura exchange | 6 | 83,33% | +2,02% |
| DOGE | SWING | Tecnico | 56 | 69,64% | -0,64% |
| DOGE | MEDIO | Classic technical | 18 | 61,11% | -6,07% |
| DOGE | MEDIO | Famiglia statistica | 19 | 68,42% | -2,06% |
| DOGE | MEDIO | Microstruttura exchange | 2 | 100,00% | +31,53% |
| DOGE | MEDIO | Tecnico | 19 | 63,16% | -5,43% |
| SOL | BREVE | Classic technical | 72 | 51,39% | +0,48% |
| SOL | BREVE | Famiglia statistica | 114 | 52,63% | +0,69% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 9 | 44,44% | +0,86% |
| SOL | BREVE | Tecnico | 120 | 45,83% | -0,20% |
| SOL | SETTIMANALE | Classic technical | 63 | 49,21% | -0,00% |
| SOL | SETTIMANALE | Famiglia statistica | 101 | 62,38% | +2,70% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Microstruttura exchange | 6 | 16,67% | -2,65% |
| SOL | SETTIMANALE | Tecnico | 106 | 39,62% | -2,07% |
| SOL | SWING | Classic technical | 39 | 41,03% | -3,66% |
| SOL | SWING | Famiglia statistica | 51 | 80,39% | +5,57% |
| SOL | SWING | Frattale SOL | 2 | 0,00% | -3,49% |
| SOL | SWING | Microstruttura exchange | 3 | 33,33% | +4,53% |
| SOL | SWING | Tecnico | 58 | 39,66% | -3,60% |
| SOL | MEDIO | Classic technical | 9 | 22,22% | -9,59% |
| SOL | MEDIO | Famiglia statistica | 15 | 66,67% | +2,06% |
| SOL | MEDIO | Frattale SOL | 2 | 50,00% | +7,38% |
| SOL | MEDIO | Microstruttura exchange | 1 | 100,00% | +8,54% |
| SOL | MEDIO | Tecnico | 19 | 31,58% | -3,26% |

## Aree ancora in attesa

| Asset | Famiglia | Righe senza controlli | Stato |
| --- | --- | --- | --- |
| BTC | BREVE | 3 | in attesa di controlli maturati |
| BTC | SETTIMANALE | 3 | in attesa di controlli maturati |
| BTC | SWING | 2 | in attesa di controlli maturati |
| BTC | MEDIO | 10 | in attesa di controlli maturati |
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
| BTC     |         45 |              17 |          28 | RACCOLTA DATI | 0,00%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| SOL     |         45 |              17 |          28 | RACCOLTA DATI | 5,88%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| DOGE    |         45 |              17 |          28 | RACCOLTA DATI | 0,00%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |

Regola: sotto 60 controlli osserva soltanto; da 100+ controlli può diventare utile per correggere rischio spot/leva nel Decision Report.

## Ultima lettura rapida

| Asset   | Rischio spot   | Rischio leva   | Nota leva                                                               |
|:--------|:---------------|:---------------|:------------------------------------------------------------------------|
| BTC     | MEDIO          | ALTO           | leva da limitare; 2x/3x solo con invalidazione chiara                   |
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

Generato: 2026-08-24 05:32 UTC


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
| BTC | +6 | MODERATAMENTE POSITIVA | Costruttivo prudente | MEDIA | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE | Prima resistenza sopra 77.991; conferma del doppio minimo sopra 66.910. | Sotto 62.488 il quadro tecnico peggiora. |
| SOL | +6 | MODERATAMENTE POSITIVA | Costruttivo prudente | MEDIA | HOLD / TRANCHE PICCOLE, NO LEVA | Doppio minimo target raggiunto finché mantiene 78,73; nuova conferma tecnica sopra 98,27; milestone analogiche 101,80 / 116,76, valide soltanto se rientra anche il gap frattale. | Allarmi sotto 82,77 / 74,20 / 62,19. |
| DOGE | +4 | MODERATAMENTE POSITIVA | Costruttivo prudente | MEDIA | SOLO TRANCHE PICCOLE / NO LEVA | Sopra 0.11825 migliora; sopra 0.06933 viene invalidato il pattern ribassista dominante. | Sotto 0.06895 il rischio ribassista aumenta. |

## Punteggi per modulo

| Asset | Scanner grezzo | Market grezzo | Famiglia statistica | Scanner path | Tecnico | Classic tech | Frattale SOL | Fractal path | RSI top-cycle | Lifecycle EMA | Exchange flow | Futures | Daily change | Totale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +2 | 0 | +2 | 0 | +3 | +1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | +6 |
| SOL | +1 | 0 | +1 | 0 | +3 | +1 | 0 | 0 | 0 | 0 | 0 | 0 | +1 | +6 |
| DOGE | +1 | 0 | +1 | 0 | +3 | +1 | 0 | 0 | 0 | 0 | 0 | 0 | -1 | +4 |

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

- Famiglia statistica: **+2** — Scanner grezzo +2, Market Regime grezzo 0, match regime 0. Regime ignorato: meno di 5 match utili. Punteggio contato nel Global: +2.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **+2** — Casi positivi 60,00%, return centrale 30g +5,87%. Direzione scanner: SALITA. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **0** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 0, positivi 30g n/a, return p50 n/a.
- Scanner path: **0** — Controlli disponibili 43. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **+3** — Score tecnico 9/12, verdetto rialzista tecnico, trend rialzista, struttura compressione / triangolo, divergenza rialzista nascosta rsi, Wyckoff markup / fase rialzista, pattern score 0 (rialzista Doppio minimo / TARGET RAGGIUNTO; ribassista Doppio massimo / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **+1** — Score classico 11/12, verdetto CONFERMATO RIALZISTA, stage STAGE 3 / DISTRIBUZIONE O PAUSA, struttura MASSIMI E MINIMI CRESCENTI, Wyckoff SIGN OF STRENGTH POSSIBILE, volatilità locale MEDIO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Non applicabile a questo asset.
- Fractal path: **0** — Non applicabile a questo asset.
- RSI top-cycle: **0** — Non applicabile a questo asset.
- Lifecycle EMA: **0** — Non applicabile a questo asset.
- Exchange flow: **0** — Flow +1.75, derivati +0.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +1.00; exchange 3/3, copertura 100%, consenso bull 1, bear 1, divergenze 0, campioni 4h 9 su 4.00h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias LEGGERMENTE POSITIVA / NON PESATA; confidenza MEDIA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Rischio sotto, forza 2/5.
- Daily change: **0** — BTC: nessun cambiamento forte in peggioramento rispetto a ieri.

Conferme: Prima resistenza sopra 77.991; conferma del doppio minimo sopra 66.910.

Invalidazioni: Sotto 62.488 il quadro tecnico peggiora.

### SOL

- Confluenza: **MODERATAMENTE POSITIVA**
- Bias: **Costruttivo prudente**
- Punteggio finale: **+6**
- Affidabilità: **MEDIA**
- Azione coerente: **HOLD / TRANCHE PICCOLE, NO LEVA**

SOL ha una confluenza costruttiva, ma va ancora trattato come setup anticipato. La conferma vera arriva solo sopra le resistenze tecniche e con rientro del gap frattale. Il modulo lifecycle/EMA200 resta utile come contesto, ma non aumenta il punteggio Global.

Dettaglio moduli:

- Famiglia statistica: **+1** — Scanner grezzo +1, Market Regime grezzo 0, match regime 0. Regime ignorato: meno di 5 match utili. Punteggio contato nel Global: +1.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **+1** — Casi positivi 52,50%, return centrale 30g +1,63%. Direzione scanner: INCERTO. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **0** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 0, positivi 30g n/a, return p50 n/a.
- Scanner path: **0** — Controlli disponibili 43. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **+3** — Score tecnico 10/12, verdetto rialzista tecnico, trend rialzista, struttura compressione / triangolo, divergenza nessuna, Wyckoff markup / fase rialzista, pattern score 0 (rialzista Doppio minimo / TARGET RAGGIUNTO; ribassista Doppio massimo / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **+1** — Score classico 12/12, verdetto CONFERMATO RIALZISTA, stage STAGE 3 / DISTRIBUZIONE O PAUSA, struttura MASSIMI E MINIMI CRESCENTI, Wyckoff SIGN OF STRENGTH POSSIBILE, volatilità locale BASSO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Verdetto ANALOGIA DEBOLE / SCENARIO SECONDARIO, somiglianza strutturale +63,62%, aderenza live +71,37%, errore live +14,32%, gap corrente +4,08%, peso operativo 0, tracking STRUTTURA STABILE, fase FRATTALE SOLO DI CONTESTO, rischio ALTO.
- Fractal path: **0** — Controlli disponibili 39, ma percorso ancorato non aderente: gap +4,08%, errore live +14,32%. Peso 0.
- RSI top-cycle: **0** — Rischio top-cycle RSI: BASSO.
- Lifecycle EMA: **0** — Contesto non pesato nel Global. Lifecycle score 4, bias SQUEEZE SETUP MODERATO, EMA200 111,29 $, upside EMA200 +18,63%, gap EMA50/EMA200 -6,06%, hit EMA200 12w +50,00%, trend STABILE / DA CONFERMARE. Peso Global forzato a 0.
- Exchange flow: **0** — Flow +0.75, derivati +0.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +0.00; exchange 3/3, copertura 100%, consenso bull 1, bear 2, divergenze 0, campioni 4h 9 su 4.00h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias MISTA / NEUTRALE; confidenza BASSA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Rischio sotto, forza 2/5.
- Daily change: **+1** — SOL: cambiamento medio in miglioramento rispetto a ieri.

Conferme: Doppio minimo target raggiunto finché mantiene 78,73; nuova conferma tecnica sopra 98,27; milestone analogiche 101,80 / 116,76, valide soltanto se rientra anche il gap frattale.

Invalidazioni: Allarmi sotto 82,77 / 74,20 / 62,19.

### DOGE

- Confluenza: **MODERATAMENTE POSITIVA**
- Bias: **Costruttivo prudente**
- Punteggio finale: **+4**
- Affidabilità: **MEDIA**
- Azione coerente: **SOLO TRANCHE PICCOLE / NO LEVA**

DOGE non ha ancora una confluenza pulita. Serve conferma tecnica prima di trattarlo come asset forte.

Dettaglio moduli:

- Famiglia statistica: **+1** — Scanner grezzo +1, Market Regime grezzo 0, match regime 0. Regime ignorato: meno di 5 match utili. Punteggio contato nel Global: +1.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **+1** — Casi positivi 52,50%, return centrale 30g +1,87%. Direzione scanner: INCERTO. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **0** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 0, positivi 30g n/a, return p50 n/a.
- Scanner path: **0** — Controlli disponibili 43. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **+3** — Score tecnico 8/12, verdetto rialzista tecnico, trend misto, struttura rialzista con massimi e minimi crescenti, divergenza nessuna, Wyckoff range / fase non chiara, pattern score 0 (rialzista Triplo minimo / TARGET RAGGIUNTO; ribassista Doppio massimo / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **+1** — Score classico 8/12, verdetto CONFERMATO RIALZISTA, stage STAGE 3 / DISTRIBUZIONE O PAUSA, struttura MASSIMI E MINIMI CRESCENTI, Wyckoff RANGE / FASE NON CHIARA, volatilità locale MEDIO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Non applicabile a questo asset.
- Fractal path: **0** — Non applicabile a questo asset.
- RSI top-cycle: **0** — Non applicabile a questo asset.
- Lifecycle EMA: **0** — Non applicabile a questo asset.
- Exchange flow: **0** — Flow +2.00, derivati +1.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +0.50; exchange 3/3, copertura 100%, consenso bull 1, bear 2, divergenze 0, campioni 4h 9 su 4.00h; candidato +1, peso Global +0 (LOCKED / RACCOLTA 7G). Bias POSITIVA / CANDIDATA, ANCORA NON PESATA; confidenza MEDIA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +1 resta misurato separatamente.
- Futures: **0** — Lettura futures Rischio sotto, forza 2/5.
- Daily change: **-1** — DOGE: cambiamento forte in peggioramento rispetto a ieri.

Conferme: Sopra 0.11825 migliora; sopra 0.06933 viene invalidato il pattern ribassista dominante.

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

Generato: 2026-08-24 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [btc_macro_cycle_report.md](btc_macro_cycle_report.md)

Questo modulo descrive il contesto macro di Bitcoin. Non genera entrate tattiche, non autorizza leva e pesa **0** nel Global Confluence.

## Sintesi

| Voce | Valore | Lettura |
| --- | --- | --- |
| Prezzo BTC | 76.962 $ | prezzo corrente |
| Power Law centrale | 123.948 $ | deviazione -37,91% |
| Banda p10-p90 | 76.919 $ / 313.068 $ | BASSA NEL CORRIDOIO |
| Percentile residuo | 10,07% | posizione storica nel corridoio |
| Esponente β | 5,8134 | R² log-log 91,93% |
| Stabilità β | BASSA | range 1,3164 cambiando finestra |
| Ultimo halving | 2024-04-19 | 857 giorni fa |
| Fase ciclo | 58,66% | percentuale indicativa del ciclo quadriennale |
| Peso Global | 0 | CONTESTO MACRO / DIAGNOSTICO |

La Power Law viene trattata come regressione empirica, non come legge fisica. Il report mostra quanto cambia l'esponente usando finestre iniziali diverse e la confronta con il benchmark ingenuo 'prezzo invariato'.

## Bitcoin Power Law

- Campione: 2014-09-17 → 2026-08-24 (4359 osservazioni)
- Formula stimata: prezzo ≈ exp(-39.1370) × giorni^5.8134
- Prezzo centrale oggi: **123.948 $**
- Posizione corrente: **BASSA NEL CORRIDOIO**, percentile 10,07%
- Scarto dal centro: **-37,91%**

![Bitcoin Power Law](btc_power_law_chart.png)

![Bitcoin Power Law log-log](btc_power_law_loglog_chart.png)

### Stabilità dell'esponente

| Inizio campione | β | R² log-log |
| --- | --- | --- |
| 2014 | 5,8134 | 91,93% |
| 2015 | 5,8968 | 91,48% |
| 2016 | 5,5819 | 87,72% |
| 2017 | 4,8525 | 82,86% |
| 2018 | 4,5804 | 78,33% |

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
| 2012-11-28 → 2016-07-09 | 2015-01-11 | -17,25% | -10,96% | +7,24% | +68,80% |
| 2016-07-09 → 2020-05-11 | 2018-10-09 | -2,84% | -39,40% | -21,73% | +29,40% |
| 2020-05-11 → 2024-04-19 | 2022-09-02 | -4,64% | -15,04% | +18,41% | +29,54% |

Campione molto piccolo: questi rendimenti sono contesto di ciclo, non probabilità affidabili.

## SOL/BTC e DOGE/BTC dentro il tempo Bitcoin

![Altcoin nel ciclo BTC](alt_btc_cycle_spirals.png)

| Asset | Coppia | Forza vs BTC | Score raw | Candidato | 30g | Peso Global |
| --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | SOVRAPERFORMA BTC | 4 | 1 | 6.227229976792659 | 0 |
| DOGE | DOGE/BTC | RELATIVA MISTA / NON CONFERMATA | -1 | 0 | 9.904800106119293 | 0 |

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

Generato: 2026-08-24 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [relative_strength_btc_report.md](relative_strength_btc_report.md)

Questo modulo controlla se SOL e DOGE stanno davvero battendo Bitcoin. Una salita in USD accompagnata da una coppia ALT/BTC ribassista è spesso soltanto trascinamento di BTC.

**Protezione iniziale:** il candidato relativo è limitato a -1/0/+1, ma il peso nel Global resta **0**. La coppia BTC conferma o indebolisce il tecnico USD; non viene sommata come secondo modulo indipendente.

## Sintesi

| Asset | Coppia | Prezzo | Score raw | Candidato | Peso Global | Forza vs BTC | Confidenza | 30g | Tecnico USD | Lettura combinata |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | 0.00122480 | +4 | +1 | 0 | SOVRAPERFORMA BTC | BASSA | +6,23% | RIALZISTA | CONFERMA FORTE: sale in USD e batte BTC |
| DOGE | DOGE/BTC | 0.00000119 | -1 | 0 | 0 | RELATIVA MISTA / NON CONFERMATA | BASSA | +9,90% | RIALZISTA | QUADRO MISTO / NESSUNA CONFERMA RELATIVA |

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
- **Struttura:** VOLATILITÀ IN ESPANSIONE
- **Rendimenti relativi:** 7g +3,27%; 30g +6,23%; 90g +11,35%; 180g -0,75%
- **Daily:** RSI 60.62; MA50 0.00118748; MA200 0.00117724
- **Weekly:** MA30 0.00118033; RSI 50.66
- **Livelli:** supporto 0.00122200; resistenza 0.00134900; breakout 60g 0.00134900; breakdown 60g 0.00109300
- **Pattern:** DOPPIO MINIMO / TARGET RAGGIUNTO; neckline 0.00120200; target 0.00125350
- **Fibonacci:** VICINO — 38.2% a 0.00121912
- **Fonte:** Yahoo Finance SOL-BTC (coppia diretta)
- **Motivi score:** prezzo sopra MA50 daily; prezzo sopra MA200 daily; prezzo sopra MA30 weekly; MA30 weekly in discesa; RSI relativo forte; MACD relativo positivo

![Grafico SOL/BTC](relative_strength_SOLBTC.png)

## DOGE/BTC

- **Verdetto relativo:** RELATIVA MISTA / NON CONFERMATA (-1)
- **Candidato futuro:** 0; **peso attuale Global: 0**
- **Lettura combinata USD/BTC:** QUADRO MISTO / NESSUNA CONFERMA RELATIVA
- **Struttura:** VOLATILITÀ IN ESPANSIONE
- **Rendimenti relativi:** 7g +7,77%; 30g +9,90%; 90g -9,75%; 180g -16,48%
- **Daily:** RSI 67.38; MA50 0.00000112; MA200 0.00000129
- **Weekly:** MA30 0.00000129; RSI 42.12
- **Livelli:** supporto 0.00000116; resistenza 0.00000121; breakout 60g 0.00000135; breakdown 60g 0.00000100
- **Pattern:** DOPPIO MINIMO / TARGET RAGGIUNTO; neckline 0.00000115; target 0.00000128
- **Fibonacci:** VICINO — 38.2% a 0.00000120
- **Fonte:** Rapporto sintetico DOGE-USD / BTC-USD (sintetica)
- **Motivi score:** prezzo sopra MA50 daily; prezzo sotto MA200 daily; MA50 daily in discesa; prezzo sotto MA30 weekly; MA30 weekly in discesa; RSI relativo forte; MACD relativo positivo

![Grafico DOGE/BTC](relative_strength_DOGEBTC.png)

## Backtest storico diagnostico

Il backtest usa soltanto indicatori disponibili alla data del segnale e campiona una volta a settimana. È utile subito, ma non sostituisce il tracker live: le soglie sono state definite prima di vedere il risultato.

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto direzione | Return futuro mediano |
| --- | --- | --- | --- | --- | --- |
| SOL | 7g | 205 | 52,20% | +1,94% | -1,06% |
| SOL | 30g | 202 | 47,52% | +4,66% | +0,36% |
| SOL | 90g | 198 | 53,03% | +10,08% | +2,72% |
| DOGE | 7g | 294 | 55,78% | +1,84% | -1,68% |
| DOGE | 30g | 292 | 53,08% | +2,00% | -3,71% |
| DOGE | 90g | 286 | 53,85% | +6,84% | -8,85% |

## Tracker live e gate futuro

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto | Stato | Peso Global |
| --- | --- | --- | --- | --- | --- | --- |
| SOL | 1g | 20 | 65,00% | -0,22% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 3g | 18 | 50,00% | -0,48% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 7g | 16 | 37,50% | -1,41% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 14g | 15 | 6,67% | -3,37% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 30g | 2 | 0,00% | -5,78% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 1g | 35 | 68,57% | +0,02% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 3g | 35 | 60,00% | +0,23% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 7g | 34 | 64,71% | +0,52% | ELIGIBILE FUTURO ±1 | 0 |
| DOGE | 14g | 31 | 67,74% | +0,01% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 30g | 15 | 73,33% | -0,02% | LOCKED / RACCOLTA LIVE | 0 |

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

Ultima candela SOL usata: **24 agosto 2026**

## Verdetto: ANALOGIA DEBOLE / SCENARIO SECONDARIO

- **Fase attuale:** FRATTALE SOLO DI CONTESTO
- **Somiglianza totale:** +63,62%
- **Somiglianza strutturale:** +63,62%
- **Aderenza prezzo live:** +71,37%
- **Errore medio live:** +14,32%
- **Gap prezzo corrente:** +4,08%
- **Peso operativo suggerito:** 0
- **Affidabilita:** BASSA
- **Rischio fase:** ALTO
- **Trend tracking:** STRUTTURA STABILE
- **Sintesi:** Esistono alcuni elementi comuni, ma non abbastanza per una conferma.
- **SOL è al giorno:** 79 dal bottom usato.
- **Giorno BTC equivalente:** 2023-02-08
- **Prossimo step:** Proiezione condizionale, non conferma operativa: **Prima retest / debolezza, poi recupero.** Zona bassa **88,77 $** intorno al **26 agosto 2026**; zona alta **101,80 $** intorno al **5 settembre 2026**; fine step circa **99,17 $** entro il **7 settembre 2026**.

## Somiglianza prima e dopo inizio programma

Questa sezione separa la somiglianza della forma dall'aderenza reale del prezzo.

- **Inizio programma/scanner:** 3 luglio 2026
- **Prima del programma** = backtest retroattivo.
- **Da inizio programma** = verifica live: è la parte più importante per l'uso operativo.

| Periodo | Date | Giorni | Aderenza prezzo | Errore medio | Gap ultimo | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| Prima del programma | 6 giugno 2026 -> 2 luglio 2026 | 27 | +87,95% | +6,02% | +21,89% | ABBASTANZA ALLINEATO |
| Da inizio programma | 3 luglio 2026 -> 24 agosto 2026 | 53 | +71,37% | +14,32% | +4,08% | DEVIAZIONE MODERATA |
| Totale dal bottom | 6 giugno 2026 -> 24 agosto 2026 | 80 | +76,97% | +11,52% | +4,08% | DEVIAZIONE MODERATA |

Nota: un frattale può avere una forma simile ma un prezzo distante. In quel caso non è operativo finché il gap non rientra.

## Lettura operativa veloce

Il frattale non deve generare acquisti o leva adesso. La forma è un contesto, ma l'aderenza live del prezzo è insufficiente.

| Voce | Risposta | Perché |
| --- | --- | --- |
| Uso operativo | NO | Il frattale vale 0 punti operativi finché il prezzo resta non aderente. |
| Aderenza live | +71,37% | Errore medio live +14,32%. |
| Gap corrente | +4,08% | Deve rientrare circa entro ±12%. |
| Prima conferma prezzo | 101,80 $ | Serve anche miglioramento del gap, non solo una candela sopra il livello. |
| Seconda conferma | 116,76 $ | Rende più credibile il percorso, ma non sostituisce l'aderenza. |
| Invalidazione soft | 82,77 $ | Sotto questa zona il quadro peggiora. |
| Invalidazione forte | 62,19 $ | Sotto il bottom il paragone è quasi rotto. |

## Target ciclo fino al top BTC 2025

| Voce | Valore |
| --- | --- |
| Stato | CONTESTO / NON OPERATIVO |
| Top BTC 2025 | 6 ottobre 2025 - 124.753 $ |
| Data SOL equivalente | 21 aprile 2029 |
| Target ciclo base da oggi | 511,48 $ |
| Massimo percorso base | 511,48 $ (21 aprile 2029) |

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
| Prima conferma | 101,80 $ | Deve accompagnarsi al rientro del gap. |
| Seconda conferma | 116,76 $ | Scenario più credibile. |
| Invalidazione soft | 82,77 $ | Il frattale si indebolisce. |
| Invalidazione forte | 62,19 $ | Il paragone si rompe. |

## Proiezione veloce con date SOL

| Orizzonte | Data SOL | BTC fece | SOL base | Min percorso | Max percorso |
| --- | --- | --- | --- | --- | --- |
| 7 giorni | 31 agosto 2026 | +5,97% | 99,66 $ | 88,77 $ | 99,66 $ |
| 14 giorni | 7 settembre 2026 | +5,45% | 99,17 $ | 88,77 $ | 101,80 $ |
| 30 giorni | 23 settembre 2026 | -12,00% | 82,77 $ | 82,77 $ | 101,80 $ |
| 60 giorni | 23 ottobre 2026 | +23,51% | 116,16 $ | 82,77 $ | 116,76 $ |
| 90 giorni | 22 novembre 2026 | +20,57% | 113,40 $ | 82,77 $ | 124,99 $ |
| 120 giorni | 22 dicembre 2026 | +15,56% | 108,68 $ | 82,77 $ | 124,99 $ |

## Prossimi step se SOL segue BTC 2022

| Step | Date SOL | BTC fine | SOL zona bassa | SOL zona alta | SOL fine base | Lettura |
| --- | --- | --- | --- | --- | --- | --- |
| Step 1 - prossime 2 settimane | 24 agosto 2026 -> 7 settembre 2026 | +5,45% | 88,77 $ (26 agosto 2026) | 101,80 $ (5 settembre 2026) | 99,17 $ | Prima retest / debolezza, poi recupero. |
| Step 2 - primo mese | 8 settembre 2026 -> 23 settembre 2026 | -12,00% | 82,77 $ (23 settembre 2026) | 98,18 $ (8 settembre 2026) | 82,77 $ | Prima spike, poi scarico. |
| Step 3 - secondo mese | 24 settembre 2026 -> 23 ottobre 2026 | +23,51% | 84,59 $ (24 settembre 2026) | 116,76 $ (14 ottobre 2026) | 116,16 $ | Prima retest / debolezza, poi recupero. |
| Step 4 - terzo mese | 24 ottobre 2026 -> 22 novembre 2026 | +20,57% | 111,83 $ (4 novembre 2026) | 124,99 $ (28 ottobre 2026) | 113,40 $ | Spinta rialzista abbastanza pulita. |

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
| Prezzo SOL | 94,05 $ |  |
| Weekly RSI | 53,78 / linea grezza 52,71 | LINEA NON AFFIDABILE / RISCHIO NON ATTIVO — IRREALISTICA / NON OPERATIVA |
| Monthly RSI | 45,15 / linea grezza 55,81 | RSI TROPPO BASSO PER RISCHIO TOP — VALIDA / USO PRUDENTE |
| Target ciclo base | 511,48 $ | Avanzamento +18,39% |
| Rischio top-cycle RSI | BASSO | Nessun segnale top-cycle macro attivo. Prezzo ancora lontano dal target ciclo; il filtro RSI resta solo di monitoraggio. |

## Lettura semplice

- Weekly: La top-line weekly non supera i controlli di qualità. Non viene usata per generare rischio top-cycle.
- Monthly: RSI monthly è 45,2, sotto la soglia prudente 55. Anche se fosse vicino alla linea, non è una vera zona di esaurimento ciclo.
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
| Prezzo SOL | 94,05 $ |
| TVL Solana | 5,56 mld $ |
| TVL 7g | +16,32% |
| DEX volume 24h | 3,12 mld $ |
| Fees 24h | 12,45 mln $ |
| Stablecoin su Solana | 16,39 mld $ |
| Stake ratio | 68,50% |
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
| Prezzo SOL | 94,05 $ |
| EMA200 weekly target | 111,29 $ |
| Upside verso EMA200 | +18,63% |
| Distanza prezzo da EMA200 | -15,71% |
| Gap EMA50/EMA200 | -6,06% |
| Stato cross | EMA50 SOTTO EMA200 |
| RSI weekly | 53,63 |
| Età SOL | 6,4 anni |
| Analoghi storici usati | 30 |
| Max analoghi per asset | 3 |
| Hit EMA200 12w analoghi | +50,00% |
| Max gain mediano 12w | +21,62% |
| Drawdown mediano 12w | -31,21% |

Lettura semplice:

**CONTESTO INTERESSANTE, SERVONO CONFERME DI PREZZO**

Autocontrollo: **STABILE / DA CONFERMARE**.

Questo modulo confronta SOL con altre crypto in fasi simili di età, distanza da EMA200, EMA50/EMA200 e RSI. Non usa stock market.

Nota importante: **questo modulo ora NON pesa più nel Global Confluence**. Resta solo come contesto di ciclo e come mappa verso EMA200 weekly. Il punteggio Global resta guidato da prezzo, scanner, regime, struttura tecnica, frattale, RSI e conferme reali.

Nota: se EMA50/EMA200 sono dentro ±2%, il modulo parla di medie sovrapposte / incrocio in corso, perché exchange diversi possono mostrare il cross leggermente prima o dopo.

<!-- Generato: 2026-08-24 05:32 UTC -->
<!-- MAJOR_ALT_LIFECYCLE_SQUEEZE_END -->

</details>
<!-- COMPACT_SECTION_END:major_alt_lifecycle -->

# Report giornaliero BTC / SOL / DOGE

Aggiornato il: **2026-08-24 05:30:23 UTC**

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
| BTC | NESSUN CAMBIAMENTO FORTE | peggioramento | RIALZISTA | +60.00% | -2.50 punti |
| SOL | CAMBIAMENTO MEDIO | miglioramento | NEUTRALE / INCERTO | +52.50% | +7.50 punti |
| DOGE | CAMBIAMENTO FORTE | peggioramento | NEUTRALE / INCERTO | +52.50% | -7.50 punti |

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
| BTC | 73.177 $ | 84.731 $ | +20,00% | +15,79% | rimbalzo poco frequente | 84.731 $ | 73.177 $ | +36,00% | -13,64% | scarico possibile |
| SOL | 89,35 $ | 103,46 $ | +24,14% | +15,79% | rimbalzo poco frequente | 103,46 $ | 89,35 $ | +23,81% | -13,64% | spike storicamente più resistente |
| DOGE | 0,08750 $ | 0,10131 $ | +55,17% | +15,79% | rimbalzo possibile | 0,10131 $ | 0,08750 $ | +35,29% | -13,64% | scarico possibile |

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

- **BTC: su 40 casi simili, 25 prima sono scesi a -5,00%. Tra quei 25, 5 poi sono rimbalzati fino a +10,00%. Percentuale: +20,00% (5/25). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.**
- **BTC: su 40 casi simili, 25 prima sono saliti a +10,00%. Tra quei 25, 9 poi sono scaricati a -5,00%. Percentuale: +36,00% (9/25). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: scarico possibile.**
- **SOL: su 40 casi simili, 29 prima sono scesi a -5,00%. Tra quei 29, 7 poi sono rimbalzati fino a +10,00%. Percentuale: +24,14% (7/29). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.**
- **SOL: su 40 casi simili, 21 prima sono saliti a +10,00%. Tra quei 21, 5 poi sono scaricati a -5,00%. Percentuale: +23,81% (5/21). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.**
- **DOGE: su 40 casi simili, 29 prima sono scesi a -5,00%. Tra quei 29, 16 poi sono rimbalzati fino a +10,00%. Percentuale: +55,17% (16/29). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo possibile.**
- **DOGE: su 40 casi simili, 34 prima sono saliti a +10,00%. Tra quei 34, 12 poi sono scaricati a -5,00%. Percentuale: +35,29% (12/34). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: scarico possibile.**

<!-- BOUNCE_AFTER_DRAWDOWN_END -->

</details>
<!-- COMPACT_SECTION_END:bounce_after_drawdown -->

<!-- COMPACT_SECTION_START:scanner_forecast -->
<details>
<summary><strong>🔭 Cono probabilistico dello scanner</strong></summary>

<!-- SCANNER_FORECAST_TRACKER_START -->
# Scanner forecast path / cono probabilistico

Generato: 2026-08-24 05:31:41 UTC


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
| BTC | 2026-08-24 | 77.028 $ | SALITA | 60,00% | 67.998,22 $ | 71.028,38 $ | 81.546,42 $ | 88.464,28 $ | 105.410,12 $ |
| SOL | 2026-08-24 | 94,05 $ | INCERTO | 52,50% | 82,16 $ | 87,01 $ | 95,58 $ | 111,63 $ | 135,52 $ |
| DOGE | 2026-08-24 | 0.09210 $ | INCERTO | 52,50% | 0.06658 $ | 0.08086 $ | 0.09383 $ | 0.10762 $ | 0.12320 $ |

## Grafici

### BTC

![Scanner forecast BTC](scanner_forecast_BTC.png)

#### Verifica storica e discrepanza

![Verifica storica cono BTC](scanner_forecast_history_BTC.png)

- Cono congelato il **2026-07-25**; verificato fino al **2026-08-24**; stato **COMPLETO 30/30g**.
- Reale **76.934,81 $**; p50 previsto **74.111,71 $**; scarto **3,81%**.
- Errore medio assoluto **4,36%**; massimo **12,32%**; DENTRO p10-p90; DENTRO p25-p75.

### SOL

![Scanner forecast SOL](scanner_forecast_SOL.png)

#### Verifica storica e discrepanza

![Verifica storica cono SOL](scanner_forecast_history_SOL.png)

- Cono congelato il **2026-07-25**; verificato fino al **2026-08-24**; stato **COMPLETO 30/30g**.
- Reale **93,76 $**; p50 previsto **78,07 $**; scarto **20,09%**.
- Errore medio assoluto **4,69%**; massimo **23,23%**; DENTRO p10-p90; FUORI p25-p75.

### DOGE

![Scanner forecast DOGE](scanner_forecast_DOGE.png)

#### Verifica storica e discrepanza

![Verifica storica cono DOGE](scanner_forecast_history_DOGE.png)

- Cono congelato il **2026-07-25**; verificato fino al **2026-08-24**; stato **COMPLETO 30/30g**.
- Reale **0.09169 $**; p50 previsto **0.07047 $**; scarto **30,11%**.
- Errore medio assoluto **7,04%**; massimo **35,70%**; FUORI p10-p90; FUORI p25-p75.

## Accuratezza percorso scanner

| Asset   | Giorno   |   Controlli | Dentro p10-p90   | Dentro p25-p75   | Errore medio abs vs p50   | Errore medio vs p50   |
|:--------|:---------|------------:|:-----------------|:-----------------|:--------------------------|:----------------------|
| BTC | 1g | 43 | 93,02% | 58,14% | 2,26% | 0,76% |
| BTC | 3g | 41 | 90,24% | 70,73% | 3,43% | 1,20% |
| BTC | 7g | 37 | 97,30% | 75,68% | 4,69% | 1,78% |
| BTC | 14g | 32 | 96,88% | 81,25% | 4,48% | 1,48% |
| BTC | 30g | 16 | 100,00% | 93,75% | 6,46% | -1,80% |
| SOL | 1g | 43 | 76,74% | 60,47% | 2,76% | 0,87% |
| SOL | 3g | 41 | 87,80% | 70,73% | 3,73% | 1,09% |
| SOL | 7g | 37 | 89,19% | 81,08% | 3,88% | 1,86% |
| SOL | 14g | 32 | 93,75% | 75,00% | 5,31% | 4,15% |
| SOL | 30g | 16 | 93,75% | 68,75% | 7,55% | 6,75% |
| DOGE | 1g | 43 | 88,37% | 62,79% | 3,27% | 1,46% |
| DOGE | 3g | 41 | 87,80% | 75,61% | 4,60% | 3,28% |
| DOGE | 7g | 37 | 83,78% | 81,08% | 8,27% | 6,60% |
| DOGE | 14g | 32 | 84,38% | 59,38% | 10,64% | 9,37% |
| DOGE | 30g | 16 | 87,50% | 37,50% | 18,69% | 18,69% |

## Calibratore shadow

Il cono ufficiale resta grezzo e invariato. Il calibratore usa soltanto previsioni passate già mature, campionate una volta a settimana per ridurre la falsa indipendenza. Ogni orizzonte si attiva a 30 controlli indipendenti: parte al 25% della correzione stimata e cresce gradualmente fino al 100% a 100 controlli.

| Asset   | Orizzonte   |   Controlli indipendenti |   Soglia | Stato                  | Forza correzione   | Shift p50   |   Scala p10-p90 |
|:--------|:------------|-------------------------:|---------:|:-----------------------|:-------------------|:------------|----------------:|
| BTC | 1g | 7 | 30 | RACCOLTA (23 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 3g | 7 | 30 | RACCOLTA (23 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 7g | 7 | 30 | RACCOLTA (23 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 14g | 6 | 30 | RACCOLTA (24 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 30g | 3 | 30 | RACCOLTA (27 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 1g | 7 | 30 | RACCOLTA (23 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 3g | 7 | 30 | RACCOLTA (23 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 7g | 7 | 30 | RACCOLTA (23 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 14g | 6 | 30 | RACCOLTA (24 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 30g | 3 | 30 | RACCOLTA (27 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 1g | 7 | 30 | RACCOLTA (23 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 3g | 7 | 30 | RACCOLTA (23 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 7g | 7 | 30 | RACCOLTA (23 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 14g | 6 | 30 | RACCOLTA (24 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 30g | 3 | 30 | RACCOLTA (27 mancanti) | 0,0% | 0,00% | 1,000 |

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

Righe salvate nello storico: **123**.

Questa sezione tiene un diario delle previsioni giornaliere a 30 giorni, senza appesantire il report principale.

| Data | Asset | Prezzo | Direzione | Casi positivi | Return p50 | Drawdown p50 | Max gain p50 | Controllo 30g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08-24 | BTC | 77.028 $ | SALITA | 60,00% | 81.546 $ | 71.472 $ | 87.040 $ | 2026-09-23 |
| 2026-08-24 | DOGE | 0,09000 $ | INCERTO | 52,50% | 0,09000 $ | 0,08000 $ | 0,11000 $ | 2026-09-23 |
| 2026-08-24 | SOL | 94,05 $ | INCERTO | 52,50% | 95,58 $ | 84,78 $ | 105,18 $ | 2026-09-23 |

<!-- FORECAST_30D_HISTORY_END -->

</details>
<!-- COMPACT_SECTION_END:scanner_forecast -->

<!-- COMPACT_SECTION_START:extreme_cases -->
<details>
<summary><strong>⚠️ Percorso dei casi estremi</strong></summary>

<!-- EXTREME_CASES_PATH_START -->
# Extreme cases path report

Generato: 2026-08-24 05:31 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [extreme_cases_path_report.md](extreme_cases_path_report.md)

Questo report si attiva quando i casi positivi o negativi sono almeno **80%**.

Ora misura anche il **rialzo massimo prima della discesa principale**, quindi distingue uno spike iniziale da una discesa quasi immediata.

## Trigger estremi

| Asset   | Direzione   | Trigger   | Percentuale   | Motivo                           |   Match disponibili |
|:--------|:------------|:----------|:--------------|:---------------------------------|--------------------:|
| BTC     | NESSUNO     | NO        | +60,00%       | Nessun lato sopra soglia estrema |                  40 |
| SOL     | NESSUNO     | NO        | +52,50%       | Nessun lato sopra soglia estrema |                  40 |
| DOGE    | NESSUNO     | NO        | +52,50%       | Nessun lato sopra soglia estrema |                  40 |

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
- Prezzo attuale: **77.028,36 $**
- Return normale fra 30 giorni: **81.546,42 $** (5,87%)
- Drawdown normale durante il mese: **71.472,13 $** (-7,21%)
- Drawdown brutto da rispettare: **66.780,76 $** (-13,30%)
- Max gain normale durante il mese: **87.039,59 $** (13,00%)
- Max gain buono / take profit ottimistico: **98.994,36 $** (28,52%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Solana
- Direzione più probabile a 30 giorni: **INCERTO**
- Casi positivi / salita storica: **52,50%**
- Casi negativi / discesa storica: **47,50%**
- Quanto è netto il segnale: **molto debole / quasi pari**
- Prezzo attuale: **94,05 $**
- Return normale fra 30 giorni: **95,58 $** (1,63%)
- Drawdown normale durante il mese: **84,78 $** (-9,86%)
- Drawdown brutto da rispettare: **80,46 $** (-14,45%)
- Max gain normale durante il mese: **105,18 $** (11,83%)
- Max gain buono / take profit ottimistico: **116,67 $** (24,05%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Dogecoin
- Direzione più probabile a 30 giorni: **INCERTO**
- Casi positivi / salita storica: **52,50%**
- Casi negativi / discesa storica: **47,50%**
- Quanto è netto il segnale: **molto debole / quasi pari**
- Prezzo attuale: **0,09 $**
- Return normale fra 30 giorni: **0,09 $** (1,87%)
- Drawdown normale durante il mese: **0,08 $** (-10,26%)
- Drawdown brutto da rispettare: **0,08 $** (-16,76%)
- Max gain normale durante il mese: **0,11 $** (20,29%)
- Max gain buono / take profit ottimistico: **0,13 $** (36,69%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Messaggio del giorno

Il quadro generale oggi è misto. Alcuni asset possono avere lettura diversa, quindi è meglio valutare asset per asset.

---

# Mappa semplice asset per asset

# Bitcoin — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟢 VERDE / Favorevole
**Prezzo attuale:** 77.028,36 $

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

- Se va molto male: **67.998,22 $** (-11,72%)
- Se va male: **71.028,38 $** (-7,79%)
- Scenario normale: **81.546,42 $** (5,87%)
- Se va bene: **88.464,28 $** (14,85%)
- Se va molto bene: **105.410,12 $** (36,85%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **71.472,13 $** (-7,21%)
- Discesa brutta: **66.780,76 $** (-13,30%)
- Discesa molto brutta: **63.685,24 $** (-17,32%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **87.039,59 $** (13,00%)
- Rialzo buono: **98.994,36 $** (28,52%)
- Rialzo molto forte: **111.054,89 $** (44,17%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Bitcoin tendeva a muoversi tra una zona bassa intorno a **71.472,13 $** e uno spike normale intorno a **87.039,59 $**.

La chiusura a 30 giorni era più spesso positiva: salita 60,00%, discesa 40,00%. Quindi la lettura principale è favorevole.

Nota leva BTC: se la liquidazione è vicina a 51.000 $, guarda soprattutto la discesa brutta e molto brutta. Il prezzo può recuperare dopo, ma la leva può saltare prima.

---

# Solana — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟡 GIALLO / Incerto
**Prezzo attuale:** 94,05 $

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

- Se va molto male: **82,16 $** (-12,64%)
- Se va male: **87,01 $** (-7,49%)
- Scenario normale: **95,58 $** (1,63%)
- Se va bene: **111,63 $** (18,70%)
- Se va molto bene: **135,52 $** (44,10%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **84,78 $** (-9,86%)
- Discesa brutta: **80,46 $** (-14,45%)
- Discesa molto brutta: **77,83 $** (-17,25%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **105,18 $** (11,83%)
- Rialzo buono: **116,67 $** (24,05%)
- Rialzo molto forte: **142,68 $** (51,71%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Solana tendeva a muoversi tra una zona bassa intorno a **84,78 $** e uno spike normale intorno a **105,18 $**.

La chiusura a 30 giorni è incerta: salita 52,50%, discesa 47,50%. Non c'è un vantaggio netto.

---

# Dogecoin — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟡 GIALLO / Incerto
**Prezzo attuale:** 0,09 $

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

- Se va molto male: **0,07 $** (-27,71%)
- Se va male: **0,08 $** (-12,21%)
- Scenario normale: **0,09 $** (1,87%)
- Se va bene: **0,11 $** (16,86%)
- Se va molto bene: **0,12 $** (33,77%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **0,08 $** (-10,26%)
- Discesa brutta: **0,08 $** (-16,76%)
- Discesa molto brutta: **0,06 $** (-31,21%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **0,11 $** (20,29%)
- Rialzo buono: **0,13 $** (36,69%)
- Rialzo molto forte: **0,14 $** (48,21%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Dogecoin tendeva a muoversi tra una zona bassa intorno a **0,08 $** e uno spike normale intorno a **0,11 $**.

La chiusura a 30 giorni è incerta: salita 52,50%, discesa 47,50%. Non c'è un vantaggio netto.

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

- Previsioni già controllate: **23**
- Direzione corretta: **81,25%**
- Errore medio dello scenario centrale: **5,03%**
- Zona rischio toccata: **0,00%**
- Zona rialzo media toccata: **4,35%**
- Prezzo finale dentro lo scenario 10%-90%: **100,00%**

### Dogecoin

- Previsioni già controllate: **23**
- Direzione corretta: **90,00%**
- Errore medio dello scenario centrale: **14,85%**
- Zona rischio toccata: **0,00%**
- Zona rialzo media toccata: **13,04%**
- Prezzo finale dentro lo scenario 10%-90%: **91,30%**

### Solana

- Previsioni già controllate: **23**
- Direzione corretta: **100,00%**
- Errore medio dello scenario centrale: **6,31%**
- Zona rischio toccata: **8,70%**
- Zona rialzo media toccata: **17,39%**
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

Dati ancora insufficienti: previsioni controllate **23** su **30** necessarie.

Per ora si usa solo lo scanner storico grezzo. Quando ci saranno abbastanza previsioni controllate, qui apparirà la lettura autocalibrata.

## Solana

Dati ancora insufficienti: previsioni controllate **23** su **30** necessarie.

Per ora si usa solo lo scanner storico grezzo. Quando ci saranno abbastanza previsioni controllate, qui apparirà la lettura autocalibrata.

## Dogecoin

Dati ancora insufficienti: previsioni controllate **23** su **30** necessarie.

Per ora si usa solo lo scanner storico grezzo. Quando ci saranno abbastanza previsioni controllate, qui apparirà la lettura autocalibrata.

---

# Approfondimento tecnico — Bitcoin (BTC-USD)

## Semaforo: 🟢 VERDE / Favorevole

**Prezzo attuale:** 77.028,36 $

Bitcoin ha un segnale favorevole. La statistica dei casi simili indica più possibilità di salita che di discesa, ma resta comunque una probabilità, non una certezza.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **60,00%**
- Casi negativi dopo 30 giorni: **40,00%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **79,51%**
- Rendimento medio dopo 30 giorni: **9,31%**
- Rendimento centrale dopo 30 giorni: **5,87%**
- Discesa media durante i 30 giorni: **-8,87%**
- Massimo rialzo medio durante i 30 giorni: **22,29%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **84.201,98 $**
- Scenario centrale a 30 giorni: **81.546,42 $**
- Zona di rischio media: **70.192,46 $**
- Zona di rialzo media: **94.197,05 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -11,72% → **67.998,22 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -7,79% → **71.028,38 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: 5,87% → **81.546,42 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 14,85% → **88.464,28 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 36,85% → **105.410,12 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -17,32% → **63.685,24 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -13,30% → **66.780,76 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -7,21% → **71.472,13 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -3,10% → **74.640,38 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: 0,00% → **77.028,36 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 0,00% → **77.028,36 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 5,90% → **81.571,76 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 13,00% → **87.039,59 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 28,52% → **98.994,36 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 44,17% → **111.054,89 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| XRP-USD         | 2023-07-30   | 2023-11-06 |        86.54 |       -10.51 |         -18.88 |           0    |
| BNB-USD         | 2018-11-03   | 2019-02-10 |        85.25 |        67.25 |          -4.66 |          67.25 |
| THETA-USD       | 2018-11-02   | 2019-02-09 |        83.27 |        93.12 |           0    |         137.2  |
| XLM-USD         | 2020-08-14   | 2020-11-21 |        82.55 |        53.46 |          -4.5  |          90.41 |
| EOS-USD         | 2023-07-30   | 2023-11-06 |        82.38 |         5.82 |          -7    |           6.19 |
| LTC-USD         | 2023-07-28   | 2023-11-04 |        82.33 |         3.33 |          -5.7  |           6.67 |
| LTC-USD         | 2018-11-01   | 2019-02-08 |        82.02 |        31.56 |          -4.2  |          33.64 |
| ETC-USD         | 2023-07-30   | 2023-11-06 |        81.54 |         9.48 |          -1.99 |          12.3  |
| ETC-USD         | 2020-08-19   | 2020-11-26 |        81.38 |        -4.88 |         -17.07 |           9.66 |
| RUNE-USD        | 2026-01-16   | 2026-04-25 |        81.29 |        -7.25 |         -12.51 |          30.32 |

---

# Approfondimento tecnico — Solana (SOL-USD)

## Semaforo: 🟡 GIALLO / Incerto

**Prezzo attuale:** 94,05 $

Solana è in una situazione incerta. Lo scanner non vede un vantaggio chiaro né per la salita né per la discesa. In questi casi è meglio non forzare la previsione.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **52,50%**
- Casi negativi dopo 30 giorni: **47,50%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **71,02%**
- Rendimento medio dopo 30 giorni: **23,20%**
- Rendimento centrale dopo 30 giorni: **1,63%**
- Discesa media durante i 30 giorni: **-9,97%**
- Massimo rialzo medio durante i 30 giorni: **34,81%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **115,87 $**
- Scenario centrale a 30 giorni: **95,58 $**
- Zona di rischio media: **84,67 $**
- Zona di rialzo media: **126,79 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -12,64% → **82,16 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -7,49% → **87,01 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: 1,63% → **95,58 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 18,70% → **111,63 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 44,10% → **135,52 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -17,25% → **77,83 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -14,45% → **80,46 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -9,86% → **84,78 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -4,55% → **89,77 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: -0,05% → **94,01 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 1,13% → **95,11 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 4,25% → **98,05 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 11,83% → **105,18 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 24,05% → **116,67 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 51,71% → **142,68 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| VET-USD         | 2020-02-23   | 2020-06-01 |        80.79 |        41.53 |           0    |          46.55 |
| ZIL-USD         | 2020-08-16   | 2020-11-23 |        79.03 |       135.96 |           0    |         135.96 |
| BNB-USD         | 2018-11-03   | 2019-02-10 |        78.08 |        67.25 |          -4.66 |          67.25 |
| EOS-USD         | 2018-11-18   | 2019-02-25 |        76.53 |        20.31 |          -8.74 |          20.31 |
| ZEC-USD         | 2023-07-30   | 2023-11-06 |        74.61 |         4.51 |          -9.53 |           6.34 |
| ZEC-USD         | 2020-02-21   | 2020-05-30 |        74.56 |        -4.23 |          -9.12 |           6.45 |
| NEAR-USD        | 2026-01-15   | 2026-04-24 |        74.33 |        69.91 |         -10.37 |          74.31 |
| MKR-USD         | 2020-02-22   | 2020-05-31 |        73.89 |        -1.14 |          -7.47 |          49.98 |
| ETC-USD         | 2020-08-19   | 2020-11-26 |        73.42 |        -4.88 |         -17.07 |           9.66 |
| ALGO-USD        | 2020-02-25   | 2020-06-03 |        73.37 |       -15.75 |         -15.75 |           2.83 |

---

# Approfondimento tecnico — Dogecoin (DOGE-USD)

## Semaforo: 🟡 GIALLO / Incerto

**Prezzo attuale:** 0,09 $

Dogecoin è in una situazione incerta. Lo scanner non vede un vantaggio chiaro né per la salita né per la discesa. In questi casi è meglio non forzare la previsione.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **52,50%**
- Casi negativi dopo 30 giorni: **47,50%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **83,10%**
- Rendimento medio dopo 30 giorni: **5,62%**
- Rendimento centrale dopo 30 giorni: **1,87%**
- Discesa media durante i 30 giorni: **-12,31%**
- Massimo rialzo medio durante i 30 giorni: **29,81%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **0,10 $**
- Scenario centrale a 30 giorni: **0,09 $**
- Zona di rischio media: **0,08 $**
- Zona di rialzo media: **0,12 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -27,71% → **0,07 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -12,21% → **0,08 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: 1,87% → **0,09 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 16,86% → **0,11 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 33,77% → **0,12 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -31,21% → **0,06 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -16,76% → **0,08 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -10,26% → **0,08 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -4,15% → **0,09 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: 0,00% → **0,09 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 8,80% → **0,10 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 13,16% → **0,10 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 20,29% → **0,11 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 36,69% → **0,13 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 48,21% → **0,14 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| MANA-USD        | 2025-01-15   | 2025-04-24 |        87.6  |        -4.31 |         -10.11 |          18.69 |
| VET-USD         | 2025-01-17   | 2025-04-26 |        86.57 |         1.03 |          -8.45 |          18.77 |
| FIL-USD         | 2022-04-25   | 2022-08-02 |        86.24 |       -29.26 |         -31.16 |          16.04 |
| OP-USD          | 2026-01-16   | 2026-04-25 |        85.45 |         3.57 |          -4.25 |          37.84 |
| AVAX-USD        | 2025-01-16   | 2025-04-25 |        85.43 |         5.65 |         -11.98 |          16.68 |
| IOTA-USD        | 2025-01-16   | 2025-04-25 |        85.24 |        -0.35 |          -6.45 |          21.79 |
| SAND-USD        | 2025-01-14   | 2025-04-23 |        85.13 |         3.56 |          -8.98 |          23.97 |
| AVAX-USD        | 2025-09-28   | 2026-01-05 |        84.37 |       -32.83 |         -32.83 |           1.94 |
| QTUM-USD        | 2022-04-21   | 2022-07-29 |        84.37 |       -36.05 |         -36.05 |           0    |
| HBAR-USD        | 2020-08-16   | 2020-11-23 |        84.1  |       -12.5  |         -12.5  |          13.17 |

</details>
<!-- COMPACT_SECTION_END:scanner_full_detail -->

<!-- COMPACT_SECTION_START:market_regime -->
<details>
<summary><strong>🌦️ Market Regime Match</strong></summary>

<!-- MARKET_REGIME_MATCH_START -->
# Market Regime Match Report


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [market_regime_match_report.md](market_regime_match_report.md)

Generated: 2026-08-24 05:31 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | MIXED | 77.028 $ | True | 1.47% | -9.39% | MIXED | 1.47% | -9.39% |
| DOGE-USD | DISTRIBUTION | 0.09210 $ | True | -9.05% | -15.89% | MIXED | 1.47% | -9.39% |
| SOL-USD | RECOVERY | 94,05 $ | True | 12.18% | -15.58% | MIXED | 1.47% | -9.39% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 60.00% | 5.87% | 14.85% | 36.85% | -7.21% | -17.32% | 13.00% | 28.52% | 44.17% | 70.00% | 16.96% | 43.67% | 92.30% |
| BTC-USD | SAME_BTC_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| BTC-USD | SAME_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| DOGE-USD | ALL_MATCHES | 40 | 52.50% | 1.87% | 16.86% | 33.77% | -10.26% | -31.21% | 20.29% | 36.69% | 48.21% | 42.50% | -10.49% | 29.18% | 93.88% |
| DOGE-USD | SAME_BTC_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| DOGE-USD | SAME_ASSET_REGIME | 1 | 0.00% | -27.61% | -27.61% | -27.61% | -34.07% | -34.07% | 0.00% | 0.00% | 0.00% | 0.00% | -25.08% | -25.08% | -25.08% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL-USD | ALL_MATCHES | 40 | 52.50% | 1.63% | 18.70% | 44.10% | -9.86% | -17.25% | 11.83% | 24.05% | 51.71% | 75.00% | 23.92% | 32.48% | 110.93% |
| SOL-USD | SAME_BTC_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL-USD | SAME_ASSET_REGIME | 16 | 25.00% | -5.89% | 1.69% | 24.60% | -11.51% | -16.41% | 5.09% | 18.79% | 48.01% | 93.75% | 24.48% | 31.51% | 37.80% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 11 | 36.36% | -5.83% | -6.97% | 31.98% | 54.55% | 12.70% | 91.53% |
| BTC-USD | HISTORICAL_BTC_BULL | 23 | 78.26% | 9.48% | -7.00% | 26.15% | 78.26% | 15.86% | 72.89% |
| BTC-USD | HISTORICAL_BTC_DISTRIBUTION | 3 | 66.67% | 14.34% | 0.00% | 20.24% | 66.67% | 30.12% | 49.06% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 3 | 0.00% | -15.07% | -15.75% | 35.71% | 66.67% | 23.44% | 55.17% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 6 | 33.33% | -5.92% | -17.12% | 34.47% | 16.67% | -22.88% | 34.47% |
| DOGE-USD | HISTORICAL_BTC_BULL | 27 | 66.67% | 8.90% | -6.74% | 39.10% | 59.26% | 7.49% | 77.00% |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 0.00% | -27.61% | -34.07% | 0.00% | 0.00% | -25.08% | 0.00% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 6 | 16.67% | -15.45% | -18.95% | 20.85% | 0.00% | -28.72% | 20.85% |
| SOL-USD | HISTORICAL_BTC_BEAR | 9 | 66.67% | 12.26% | -6.90% | 49.47% | 66.67% | 5.41% | 62.62% |
| SOL-USD | HISTORICAL_BTC_BULL | 14 | 71.43% | 7.35% | -9.71% | 22.60% | 64.29% | 23.60% | 68.34% |
| SOL-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 100.00% | 18.89% | -13.32% | 18.89% | 0.00% | -13.86% | 18.89% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 16 | 25.00% | -7.07% | -12.23% | 14.80% | 93.75% | 26.93% | 56.46% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 26 | 65.38% | 7.69% | -6.27% | 26.53% | 73.08% | 14.42% | 64.53% |
| BTC-USD | HISTORICAL_ASSET_BULL | 7 | 71.43% | 11.17% | -5.70% | 40.01% | 57.14% | 29.10% | 163.32% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 7 | 28.57% | -4.88% | -15.75% | 27.81% | 71.43% | 22.65% | 55.17% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 8 | 37.50% | -5.92% | -14.31% | 27.72% | 25.00% | -19.33% | 49.82% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 24 | 62.50% | 4.61% | -8.71% | 42.30% | 54.17% | 4.67% | 71.74% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 0.00% | -27.61% | -34.07% | 0.00% | 0.00% | -25.08% | 0.00% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 7 | 42.86% | -20.28% | -31.16% | 26.14% | 28.57% | -32.36% | 33.51% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 17 | 70.59% | 4.51% | -9.89% | 20.31% | 52.94% | 0.43% | 62.62% |
| SOL-USD | HISTORICAL_ASSET_BULL | 7 | 71.43% | 14.13% | -2.94% | 80.25% | 85.71% | 106.74% | 221.20% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 16 | 25.00% | -5.89% | -11.51% | 18.79% | 93.75% | 24.48% | 51.28% |

## Top regime-adjusted matches

The table below shows the top matches separately for each target, so BTC does not hide SOL and DOGE.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | XRP-USD | 2023-07-30 | 86.54% | BULL | BULL | DIFFERENT | BEARISH_30D | -10.51% | -18.88% | 0.00% | -19.43% | -19.43% | 0.00% |
| BTC-USD | BNB-USD | 2018-11-03 | 85.25% | BEAR | BEAR | DIFFERENT | EXPLOSIVE_60D | 67.25% | -4.66% | 67.25% | 92.16% | -4.66% | 114.84% |
| BTC-USD | THETA-USD | 2018-11-02 | 83.27% | BEAR | BEAR | DIFFERENT | EXPLOSIVE_60D | 93.12% | 0.00% | 137.20% | 61.21% | 0.00% | 137.20% |
| BTC-USD | XLM-USD | 2020-08-14 | 82.55% | BULL | BULL | DIFFERENT | EXPLOSIVE_60D | 53.46% | -4.50% | 90.41% | 171.53% | -4.50% | 214.37% |
| BTC-USD | EOS-USD | 2023-07-30 | 82.38% | BULL | BEAR | DIFFERENT | MIXED | 5.82% | -7.00% | 6.19% | 6.95% | -7.00% | 29.44% |
| BTC-USD | LTC-USD | 2023-07-28 | 82.33% | BULL | BULL | DIFFERENT | MIXED | 3.33% | -5.70% | 6.67% | -7.34% | -7.34% | 11.25% |
| BTC-USD | LTC-USD | 2018-11-01 | 82.02% | BEAR | BEAR | DIFFERENT | EXPLOSIVE_60D | 31.56% | -4.20% | 33.64% | 99.67% | -4.20% | 112.99% |
| BTC-USD | ETC-USD | 2023-07-30 | 81.54% | BULL | BEAR | DIFFERENT | MIXED | 9.48% | -1.99% | 12.30% | 8.74% | -1.99% | 22.62% |
| BTC-USD | ETC-USD | 2020-08-19 | 81.38% | BULL | RECOVERY | DIFFERENT | MIXED | -4.88% | -17.07% | 9.66% | 22.65% | -17.07% | 45.22% |
| BTC-USD | RUNE-USD | 2026-01-16 | 81.29% | BEAR | BEAR | DIFFERENT | MIXED | -7.25% | -12.51% | 30.32% | -16.10% | -33.60% | 30.32% |
| DOGE-USD | BTC-USD | 2025-10-10 | 81.88% | DISTRIBUTION | DISTRIBUTION | SAME_ASSET_ONLY | BEARISH_30D | -27.61% | -34.07% | 0.00% | -25.08% | -34.07% | 0.00% |
| DOGE-USD | MANA-USD | 2025-01-15 | 87.60% | BULL | BULL | DIFFERENT | MIXED | -4.31% | -10.11% | 18.69% | -19.03% | -26.84% | 18.69% |
| DOGE-USD | VET-USD | 2025-01-17 | 86.57% | BULL | BULL | DIFFERENT | MIXED | 1.03% | -8.45% | 18.77% | -22.61% | -29.05% | 18.77% |
| DOGE-USD | FIL-USD | 2022-04-25 | 86.24% | RECOVERY | RECOVERY | DIFFERENT | BEARISH_30D | -29.26% | -31.16% | 16.04% | -32.36% | -35.61% | 16.04% |
| DOGE-USD | OP-USD | 2026-01-16 | 85.45% | BEAR | BEAR | DIFFERENT | MIXED | 3.57% | -4.25% | 37.84% | -16.66% | -27.25% | 37.84% |
| DOGE-USD | AVAX-USD | 2025-01-16 | 85.43% | BULL | BULL | DIFFERENT | MIXED | 5.65% | -11.98% | 16.68% | -17.86% | -25.64% | 16.68% |
| DOGE-USD | IOTA-USD | 2025-01-16 | 85.24% | BULL | BULL | DIFFERENT | MIXED | -0.35% | -6.45% | 21.79% | -22.35% | -30.21% | 21.79% |
| DOGE-USD | SAND-USD | 2025-01-14 | 85.13% | BULL | BULL | DIFFERENT | MIXED | 3.56% | -8.98% | 23.97% | -21.92% | -21.92% | 23.97% |
| DOGE-USD | AVAX-USD | 2025-09-28 | 84.37% | BULL | RECOVERY | DIFFERENT | BEARISH_30D | -32.83% | -32.83% | 1.94% | -37.57% | -42.62% | 1.94% |
| DOGE-USD | QTUM-USD | 2022-04-21 | 84.37% | RECOVERY | RECOVERY | DIFFERENT | BEARISH_30D | -36.05% | -36.05% | 0.00% | -38.23% | -40.91% | 0.00% |
| SOL-USD | VET-USD | 2020-02-23 | 80.79% | RECOVERY | RECOVERY | SAME_ASSET_ONLY | EXPLOSIVE_60D | 41.53% | 0.00% | 46.55% | 159.81% | 0.00% | 201.34% |
| SOL-USD | ZEC-USD | 2020-02-21 | 74.56% | RECOVERY | RECOVERY | SAME_ASSET_ONLY | MIXED | -4.23% | -9.12% | 6.45% | 32.15% | -9.12% | 32.15% |
| SOL-USD | MKR-USD | 2020-02-22 | 73.89% | RECOVERY | RECOVERY | SAME_ASSET_ONLY | MIXED | -1.14% | -7.47% | 49.98% | 23.44% | -7.47% | 49.98% |
| SOL-USD | ETC-USD | 2020-08-19 | 73.42% | BULL | RECOVERY | SAME_ASSET_ONLY | MIXED | -4.88% | -17.07% | 9.66% | 22.65% | -17.07% | 45.22% |
| SOL-USD | ALGO-USD | 2020-02-25 | 73.37% | RECOVERY | RECOVERY | SAME_ASSET_ONLY | BEARISH_30D | -15.75% | -15.75% | 2.83% | 24.41% | -15.75% | 60.35% |
| SOL-USD | BNB-USD | 2020-02-21 | 72.24% | RECOVERY | RECOVERY | SAME_ASSET_ONLY | BEARISH_30D | -12.61% | -14.42% | 0.97% | 12.13% | -14.42% | 13.70% |
| SOL-USD | WAVES-USD | 2023-07-30 | 72.01% | BULL | RECOVERY | SAME_ASSET_ONLY | BULLISH_30D | 10.19% | -6.81% | 17.27% | 24.55% | -6.81% | 45.32% |
| SOL-USD | DASH-USD | 2020-02-21 | 71.11% | RECOVERY | RECOVERY | SAME_ASSET_ONLY | BEARISH_30D | -12.85% | -14.87% | 1.15% | 3.43% | -15.78% | 3.43% |
| SOL-USD | QTUM-USD | 2020-02-26 | 70.36% | RECOVERY | RECOVERY | SAME_ASSET_ONLY | MIXED | -8.20% | -13.76% | 0.78% | 42.12% | -13.76% | 43.18% |
| SOL-USD | BAT-USD | 2020-02-21 | 69.11% | RECOVERY | RECOVERY | SAME_ASSET_ONLY | BULLISH_30D | 18.68% | -4.23% | 23.34% | 12.07% | -4.23% | 23.75% |

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

Generato: 2026-08-24 05:31 UTC


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
| BTC | 77.028 $ | +11 | CONFERMATO RIALZISTA | STAGE 3 / DISTRIBUZIONE O PAUSA | MASSIMI E MINIMI CRESCENTI | SIGN OF STRENGTH POSSIBILE | MEDIO | SPOT OK / LONG SOLO PRUDENTE SU CONFERMA |
| SOL | 94,05 $ | +12 | CONFERMATO RIALZISTA | STAGE 3 / DISTRIBUZIONE O PAUSA | MASSIMI E MINIMI CRESCENTI | SIGN OF STRENGTH POSSIBILE | BASSO | TRANCHE PICCOLE / NO LEVA FINCHÉ NON ROMPE CONFERME |
| DOGE | 0.09210 $ | +8 | CONFERMATO RIALZISTA | STAGE 3 / DISTRIBUZIONE O PAUSA | MASSIMI E MINIMI CRESCENTI | RANGE / FASE NON CHIARA | MEDIO | SOLO TRADING VELOCE / NO LEVA AGGRESSIVA |

## Punteggi per area

| Asset | Trend | Struttura | Momentum | Volume | Prezzo | Candela | Wyckoff | Totale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 0 | +2 | +2 | +2 | +3 | 0 | +2 | +11 |
| SOL | +1 | +2 | +2 | +2 | +3 | 0 | +2 | +12 |
| DOGE | 0 | +2 | +2 | +1 | +3 | 0 | 0 | +8 |

## Livelli tecnici

| Asset | Supporto | Resistenza | Breakout 60g | Breakdown 60g | ATR14 | Rendimento 30g | Rendimento 90g |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 76.029 $ | 77.991 $ | 73.370 $ | 57.748 $ | 2,78% | 20,05% | -0,42% |
| SOL | 85,25 $ | 98,27 $ | 87,90 $ | 64,42 $ | 3,59% | 26,92% | 10,30% |
| DOGE | 0.09044 $ | 0.09435 $ | 0.08494 $ | 0.06797 $ | 4,43% | 32,02% | -10,08% |

## Lettura dettagliata

### BTC

- Prezzo: **77.028 $**
- Score classico: **+11 / 12**
- Verdetto: **CONFERMATO RIALZISTA**
- Azione coerente: **SPOT OK / LONG SOLO PRUDENTE SU CONFERMA**
- Volatilità tecnica locale: **MEDIO** — ATR14 2,78%; distanza supporto 1,21%; distanza resistenza 1,35%

Dettaglio:

- Trend: **0** — prezzo sopra MA200 daily; breve termine sopra MA20/MA50; MA200 daily in discesa; STAGE 3 / DISTRIBUZIONE O PAUSA
- Stage weekly: **STAGE 3 / DISTRIBUZIONE O PAUSA** — Prezzo sopra MA30 weekly ma pendenza debole o piatta.
- Struttura: **+2** — MASSIMI E MINIMI CRESCENTI
- Momentum: **+2** — RSI alto 79.6; RSI in miglioramento; MACD sopra signal; istogramma MACD in miglioramento
- Volume: **+2** — OBV sopra media; CMF positivo 0.12; volume ratio 1.23
- Conferma prezzo: **+3** — Breakout sopra resistenza 60g con volume.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **+2** — SIGN OF STRENGTH POSSIBILE. Prezzo nella parte alta del range con flusso volume positivo.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 79.59 |
| MACD histogram | 1599.66853 |
| CMF20 | 0.125 |
| Volume ratio 20 | 1.23 |
| MA20 | 66.724 $ |
| MA50 | 65.139 $ |
| MA100 | 66.092 $ |
| MA200 | 69.001 $ |
| Pendenza MA50 20g | +2,89% |
| Pendenza MA200 60g | -9,58% |
| Bollinger width | 27,01% |
| Bollinger position | 0.99 |

### SOL

- Prezzo: **94,05 $**
- Score classico: **+12 / 12**
- Verdetto: **CONFERMATO RIALZISTA**
- Azione coerente: **TRANCHE PICCOLE / NO LEVA FINCHÉ NON ROMPE CONFERME**
- Volatilità tecnica locale: **BASSO** — ATR14 3,59%; distanza supporto 9,99%; distanza resistenza 4,80%

Dettaglio:

- Trend: **+1** — prezzo sopra MA200 daily; breve termine sopra MA20/MA50; MA50 daily in salita; MA200 daily in discesa; STAGE 3 / DISTRIBUZIONE O PAUSA
- Stage weekly: **STAGE 3 / DISTRIBUZIONE O PAUSA** — Prezzo sopra MA30 weekly ma pendenza debole o piatta.
- Struttura: **+2** — MASSIMI E MINIMI CRESCENTI
- Momentum: **+2** — RSI alto 82.7; RSI in miglioramento; MACD sopra signal; istogramma MACD in miglioramento
- Volume: **+2** — OBV sopra media; CMF positivo 0.10; volume ratio 1.59
- Conferma prezzo: **+3** — Breakout sopra resistenza 60g con volume.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **+2** — SIGN OF STRENGTH POSSIBILE. Prezzo nella parte alta del range con flusso volume positivo.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 82.70 |
| MACD histogram | 2.18525 |
| CMF20 | 0.101 |
| Volume ratio 20 | 1.59 |
| MA20 | 79,12 $ |
| MA50 | 77,36 $ |
| MA100 | 76,39 $ |
| MA200 | 81,14 $ |
| Pendenza MA50 20g | +3,12% |
| Pendenza MA200 60g | -15,86% |
| Bollinger width | 31,07% |
| Bollinger position | 1.00 |

### DOGE

- Prezzo: **0.09210 $**
- Score classico: **+8 / 12**
- Verdetto: **CONFERMATO RIALZISTA**
- Azione coerente: **SOLO TRADING VELOCE / NO LEVA AGGRESSIVA**
- Volatilità tecnica locale: **MEDIO** — ATR14 4,43%; distanza supporto 1,48%; distanza resistenza 2,80%

Dettaglio:

- Trend: **0** — prezzo sopra MA200 daily; breve termine sopra MA20/MA50; MA200 daily in discesa; STAGE 3 / DISTRIBUZIONE O PAUSA
- Stage weekly: **STAGE 3 / DISTRIBUZIONE O PAUSA** — Prezzo sopra MA30 weekly ma pendenza debole o piatta.
- Struttura: **+2** — MASSIMI E MINIMI CRESCENTI
- Momentum: **+2** — RSI alto 83.3; RSI in miglioramento; MACD sopra signal; istogramma MACD in miglioramento
- Volume: **+1** — OBV sopra media; CMF neutrale 0.05; volume ratio 1.62
- Conferma prezzo: **+3** — Breakout sopra resistenza 60g con volume.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **0** — RANGE / FASE NON CHIARA. Nessuna fase Wyckoff pulita.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 83.30 |
| MACD histogram | 0.00276 |
| CMF20 | 0.047 |
| Volume ratio 20 | 1.62 |
| MA20 | 0.07399 $ |
| MA50 | 0.07293 $ |
| MA100 | 0.08092 $ |
| MA200 | 0.08923 $ |
| Pendenza MA50 20g | -2,56% |
| Pendenza MA200 60g | -16,14% |
| Bollinger width | 35,28% |
| Bollinger position | 1.05 |

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

Generato: 2026-08-24 05:32 UTC


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
| BTC | 77.028 $ | Doppio massimo | CANDIDATO | ribassista | n/a | 49.952 $ | n/a | 33,39% | Fib 78,6% REJECTION (-1) @ 78.447 $ | BREAKOUT 60G | 74.959 $ |
| SOL | 94,05 $ | Doppio massimo | CANDIDATO | ribassista | n/a | 51,22 $ | n/a | 46,00% | Fib 78,6% TESTATO (0) @ 93,12 $ | BREAKOUT 60G | 83,52 $ |
| DOGE | 0.09210 $ | Doppio massimo | CANDIDATO | ribassista | n/a | 0.06214 $ | n/a | 35,49% | Fib 50,0% REJECTION (0) @ 0.09360 $ | BREAKOUT 60G | 0.09044 $ |

## BTC

![Classic visual BTC](classic_visual_BTC.png)

- Pattern principale: **Doppio massimo**
- Stato pattern: **CANDIDATO** (0)
- Famiglia: **ribassista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-06-22 -> 2026-08-09**
- Età formazione: **15 giorni**
- Breakout pattern: **n/a**
- Età breakout: **n/a**
- Neckline: **57.748 $**
- Target teorico: **49.952 $**
- Progresso verso target: **n/a**
- Distanza dalla neckline: **33,39%**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 78,6% REJECTION (-1) @ 78.447 $** — Swing DOWN 2026-05-06 82.792 -> 2026-08-14 62.488; livello più vicino 78.6% a 78.447; stato REJECTION; confluenza: resistenza tecnica.
- Invalidazione: **58.903 $**
- Relazione prezzo/neckline: **sopra neckline**
- Dettaglio: Due massimi simili vicino a 65.544 tra 2026-06-22 e 2026-08-09. Neckline ribassista stimata: 57.748. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 15 giorni. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **BREAKOUT 60G**
- Supporto: **74.959 $**
- Resistenza: **77.991 $**
- Breakout 60g: **73.370 $**
- Breakdown 60g: **57.748 $**
- RSI14: **79.94**
- ATR14: **2,78%**
- Volume ratio 20g: **1.23**
- Rendimento 30g: **+20,17%**
- Rendimento 90g: **-0,33%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Triangolo ascendente possibile | CANDIDATO | 0 | rialzista | n/a | n/a | n/a | n/a | n/a | n/a | n/a | Resistenza quasi piatta e minimi crescenti. Stato: CANDIDATO; il pattern non ha una neckline univoca da usare per il lifecycle. |
| Doppio massimo | CANDIDATO | 0 | ribassista | 62.227 $ | n/a | n/a | 58.946 $ | n/a | 23,79% | 63.471 $ | Due massimi simili a 65.508 $ e 65.402 $. Neckline circa 62.227 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 15 giorni. |
| Doppio minimo | TARGET RAGGIUNTO | 0 | rialzista | 65.402 $ | 2026-08-19 | 5g | 68.577 $ | 366,18% | n/a | 64.094 $ | Due minimi simili a 62.227 $ e 62.488 $. Neckline circa 65.402 $. Breakout neckline: 2026-08-19 (5 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 68.577 $; progresso: 366,18%; prezzo sopra neckline. |

## SOL

![Classic visual SOL](classic_visual_SOL.png)

- Pattern principale: **Doppio massimo**
- Stato pattern: **CANDIDATO** (0)
- Famiglia: **ribassista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-06-22 -> 2026-08-09**
- Età formazione: **15 giorni**
- Breakout pattern: **n/a**
- Età breakout: **n/a**
- Neckline: **64,42 $**
- Target teorico: **51,22 $**
- Progresso verso target: **n/a**
- Distanza dalla neckline: **46,00%**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 78,6% TESTATO (0) @ 93,12 $** — Swing DOWN 2026-05-11 98,27 -> 2026-08-16 74,20; livello più vicino 78.6% a 93,12; stato TESTATO; confluenza: nessuna confluenza indipendente.
- Invalidazione: **65,71 $**
- Relazione prezzo/neckline: **sopra neckline**
- Dettaglio: Due massimi simili vicino a 77,62 tra 2026-06-22 e 2026-08-09. Neckline ribassista stimata: 64,42. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 15 giorni. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **BREAKOUT 60G**
- Supporto: **83,52 $**
- Resistenza: **97,42 $**
- Breakout 60g: **87,90 $**
- Breakdown 60g: **64,42 $**
- RSI14: **83.33**
- ATR14: **3,58%**
- Volume ratio 20g: **1.59**
- Rendimento 30g: **+27,30%**
- Rendimento 90g: **+10,63%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Triangolo discendente possibile | CANDIDATO | 0 | ribassista | n/a | n/a | n/a | n/a | n/a | n/a | n/a | Massimi decrescenti e supporto quasi piatto. Stato: CANDIDATO; il pattern non ha una neckline univoca da usare per il lifecycle. |
| Doppio massimo | CANDIDATO | 0 | ribassista | 70,69 $ | n/a | n/a | 62,66 $ | n/a | 33,04% | 72,11 $ | Due massimi simili a 78,73 $ e 77,62 $. Neckline circa 70,69 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 15 giorni. |
| Testa e spalle inverso | TARGET RAGGIUNTO | 0 | rialzista | 78,17 $ | 2026-08-19 | 5g | 85,65 $ | 212,36% | n/a | 76,61 $ | Spalla sinistra 73,40 $, testa 70,69 $, spalla destra 74,20 $. Neckline circa 78,17 $. Breakout neckline: 2026-08-19 (5 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 85,65 $; progresso: 212,36%; prezzo sopra neckline. |
| Doppio minimo | TARGET RAGGIUNTO | 0 | rialzista | 78,73 $ | 2026-08-19 | 5g | 84,05 $ | 287,82% | n/a | 77,15 $ | Due minimi simili a 73,40 $ e 74,20 $. Neckline circa 78,73 $. Breakout neckline: 2026-08-19 (5 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 84,05 $; progresso: 287,82%; prezzo sopra neckline. |

## DOGE

![Classic visual DOGE](classic_visual_DOGE.png)

- Pattern principale: **Doppio massimo**
- Stato pattern: **CANDIDATO** (0)
- Famiglia: **ribassista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-07-26 -> 2026-08-11**
- Età formazione: **13 giorni**
- Breakout pattern: **n/a**
- Età breakout: **n/a**
- Neckline: **0.06797 $**
- Target teorico: **0.06214 $**
- Progresso verso target: **n/a**
- Distanza dalla neckline: **35,49%**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 50,0% REJECTION (0) @ 0.09360 $** — Swing DOWN 2026-05-14 0.11825 -> 2026-08-12 0.06895; livello più vicino 50.0% a 0.09360; stato REJECTION; confluenza: nessuna confluenza indipendente.
- Invalidazione: **0.06933 $**
- Relazione prezzo/neckline: **sopra neckline**
- Dettaglio: Due massimi simili vicino a 0.07380 tra 2026-07-26 e 2026-08-11. Neckline ribassista stimata: 0.06797. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 13 giorni. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **BREAKOUT 60G**
- Supporto: **0.09044 $**
- Resistenza: **0.09584 $**
- Breakout 60g: **0.08494 $**
- Breakdown 60g: **0.06797 $**
- RSI14: **83.94**
- ATR14: **4,41%**
- Volume ratio 20g: **1.61**
- Rendimento 30g: **+32,48%**
- Rendimento 90g: **-9,77%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Triangolo ascendente possibile | CANDIDATO | 0 | rialzista | n/a | n/a | n/a | n/a | n/a | n/a | n/a | Resistenza quasi piatta e minimi crescenti. Stato: CANDIDATO; il pattern non ha una neckline univoca da usare per il lifecycle. |
| Doppio massimo | CANDIDATO | 0 | ribassista | 0.06797 $ | n/a | n/a | 0.06214 $ | n/a | 35,49% | 0.06933 $ | Due massimi simili a 0.07380 $ e 0.07286 $. Neckline circa 0.06797 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 13 giorni. |
| Doppio minimo | TARGET RAGGIUNTO | 0 | rialzista | 0.07923 $ | 2026-08-20 | 4g | 0.08952 $ | 125,12% | n/a | 0.07765 $ | Due minimi simili a 0.06961 $ e 0.06895 $. Neckline circa 0.07923 $. Breakout neckline: 2026-08-20 (4 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 0.08952 $; progresso: 125,12%; prezzo sopra neckline. |

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

Generato: 2026-08-24 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [fractal_path_tracker.md](fractal_path_tracker.md)

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-08-24**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-02-08**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **94,05 $**
- Verdetto principale: **ANALOGIA DEBOLE / SCENARIO SECONDARIO**
- Somiglianza strutturale: **+63,62%**
- Aderenza live principale: **+71,37%**
- Errore medio live principale: **14,32%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE SOLO DI CONTESTO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **79**
- Osservazioni inclusive dal bottom: **80**
- Osservazioni da inizio programma/scanner: **53**
- Errore assoluto medio dal bottom: **11,52%**
- Errore assoluto medio da inizio programma: **14,32%**
- Gap firmato medio ultimi 7 giorni: **-2,01%**
- Errore assoluto medio ultimi 7 giorni: **6,25%**
- Gap ultimo giorno: **+4,08%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **+4,08%**
- Gap firmato medio 7g: **-2,01%**
- Errore assoluto medio 7g: **6,25%**
- Variazione recente gap: **+0,51%**
- Stato gap: **VICINO AL FRATTALE**
- Trend gap: **SOL resta sopra il percorso ancorato con distacco quasi stabile**

Soglie operative del grafico:

- entro **±5%**: percorso vicino;
- tra **±5% e ±12%**: deviazione gestibile;
- oltre **±12%**: frattale non abbastanza aderente per conferma operativa;
- oltre **±18%**: disallineamento marcato.

## Ultimi giorni del confronto ancorato

|   Giorno | Data SOL   | Data BTC eq.   | SOL reale   | Percorso ancorato   | Gap firmato   | Fase                |
|---------:|:-----------|:---------------|:------------|:--------------------|:--------------|:--------------------|
| 70 | 2026-08-15 | 2023-01-30 | 75,27 $ | 89,97 $ | -16,34% | da inizio programma |
| 71 | 2026-08-16 | 2023-01-31 | 74,54 $ | 91,15 $ | -18,22% | da inizio programma |
| 72 | 2026-08-17 | 2023-02-01 | 75,94 $ | 93,45 $ | -18,74% | da inizio programma |
| 73 | 2026-08-18 | 2023-02-02 | 77,03 $ | 92,46 $ | -16,69% | da inizio programma |
| 74 | 2026-08-19 | 2023-02-03 | 85,37 $ | 92,37 $ | -7,58% | da inizio programma |
| 75 | 2026-08-20 | 2023-02-04 | 87,64 $ | 91,91 $ | -4,65% | da inizio programma |
| 76 | 2026-08-21 | 2023-02-05 | 93,65 $ | 90,43 $ | +3,57% | da inizio programma |
| 77 | 2026-08-22 | 2023-02-06 | 93,91 $ | 89,66 $ | +4,75% | da inizio programma |
| 78 | 2026-08-23 | 2023-02-07 | 93,91 $ | 91,64 $ | +2,48% | da inizio programma |
| 79 | 2026-08-24 | 2023-02-08 | 94,05 $ | 90,36 $ | +4,08% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-08-31 | 95,75 $ | 99,66 $ | 88,77 $ / 99,66 $ | no | n/a | n/a | n/a |
| 14g | 2026-09-07 | 95,29 $ | 99,17 $ | 88,77 $ / 101,80 $ | no | n/a | n/a | n/a |
| 21g | 2026-09-14 | 93,15 $ | 96,95 $ | 88,77 $ / 101,80 $ | no | n/a | n/a | n/a |
| 28g | 2026-09-21 | 85,55 $ | 89,04 $ | 88,77 $ / 101,80 $ | no | n/a | n/a | n/a |
| 35g | 2026-09-28 | 96,02 $ | 99,94 $ | 82,77 $ / 101,80 $ | no | n/a | n/a | n/a |
| 42g | 2026-10-05 | 107,57 $ | 111,96 $ | 82,77 $ / 115,52 $ | no | n/a | n/a | n/a |
| 49g | 2026-10-12 | 111,67 $ | 116,23 $ | 82,77 $ / 116,23 $ | no | n/a | n/a | n/a |
| 56g | 2026-10-19 | 111,00 $ | 115,53 $ | 82,77 $ / 116,76 $ | no | n/a | n/a | n/a |
| 63g | 2026-10-26 | 118,72 $ | 123,57 $ | 82,77 $ / 123,96 $ | no | n/a | n/a | n/a |
| 70g | 2026-11-02 | 113,54 $ | 118,17 $ | 82,77 $ / 124,99 $ | no | n/a | n/a | n/a |
| 77g | 2026-11-09 | 111,96 $ | 116,53 $ | 82,77 $ / 124,99 $ | no | n/a | n/a | n/a |
| 84g | 2026-11-16 | 114,26 $ | 118,92 $ | 82,77 $ / 124,99 $ | no | n/a | n/a | n/a |
| 91g | 2026-11-23 | 108,81 $ | 113,25 $ | 82,77 $ / 124,99 $ | no | n/a | n/a | n/a |
| 98g | 2026-11-30 | 107,93 $ | 112,33 $ | 82,77 $ / 124,99 $ | no | n/a | n/a | n/a |
| 105g | 2026-12-07 | 103,74 $ | 107,97 $ | 82,77 $ / 124,99 $ | no | n/a | n/a | n/a |
| 112g | 2026-12-14 | 107,22 $ | 111,60 $ | 82,77 $ / 124,99 $ | no | n/a | n/a | n/a |
| 119g | 2026-12-21 | 103,78 $ | 108,02 $ | 82,77 $ / 124,99 $ | no | n/a | n/a | n/a |
| 126g | 2026-12-28 | 98,97 $ | 103,01 $ | 82,77 $ / 124,99 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 39 | 41,03% | 8,89% | 12,87% |
| 14g | 34 | 32,35% | 16,37% | 11,81% |
| 21g | 27 | 22,22% | 22,75% | 13,00% |
| 28g | 20 | 55,00% | 23,24% | 12,80% |
| 35g | 13 | 61,54% | 21,79% | 10,60% |
| 42g | 6 | 100,00% | 13,52% | 3,72% |
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

Ultima lettura salvata: **2026-08-24** — SOL 94,05 $, gap +4,08%, somiglianza +63,62%.

Nel report principale lascio solo il link, così non diventa troppo lungo.

<!-- SOL_BTC_FRACTAL_HISTORY_END -->

</details>
<!-- COMPACT_SECTION_END:fractal_path -->

<!-- COMPACT_SECTION_START:exchange_microstructure -->
<details>
<summary><strong>🏦 Dati exchange, liquidità e leva</strong></summary>

<!-- EXCHANGE_MICROSTRUCTURE_START -->
# Dati exchange, liquidità e leva

Generato: 2026-08-24 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [exchange_microstructure_report.md](exchange_microstructure_report.md)

Questo modulo legge Kraken Futures, Bitget Futures e KuCoin Futures come nucleo derivati. OKX e Coinbase vengono raccolti come fonti ausiliarie non pesate.
Non modifica la formula matematica di RSI, Fibonacci o Wyckoff: controlla se quei segnali sono sostenuti da acquisti, vendite, OI, funding e liquidità.

**Limite importante:** questo nucleo non assume disponibile un feed pubblico completo delle liquidazioni. La componente liquidazioni resta neutrale; le zone future restano stime di pressione, non dati certi delle singole posizioni.

Diagnostica completa: [exchange_source_diagnostics.md](exchange_source_diagnostics.md)

## Sintesi

| Asset | Prezzo | Exchange | Segnale candidato | Peso Global | Bias exchange | Confidenza | Copertura | Funding 8h eq. | OI 24h | Taker flow (campione/4h) | Book 0,5% | Liq long campione | Liq short campione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 76.901 $ | 3 | 0 | 0 | LEGGERMENTE POSITIVA / NON PESATA | MEDIA | 100% | +0,0095% | +2,92% | 3,80 | +1,83% | 0 $ | 0 $ |
| SOL | 93,87 $ | 3 | 0 | 0 | MISTA / NEUTRALE | BASSA | 100% | +0,0107% | -4,62% | 0,55 | +13,79% | 0 $ | 0 $ |
| DOGE | 0.09180 $ | 3 | +1 | 0 | POSITIVA / CANDIDATA, ANCORA NON PESATA | MEDIA | 100% | +0,0100% | +2,91% | 1,09 | +15,94% | 0 $ | 0 $ |

Il segnale candidato è limitato a **±1**, ma il peso nel Global resta **0** finché il tracker a 7 giorni non raggiunge 30 controlli, almeno 55% di accuratezza e return corretto direzione positivo. Un singolo muro o funding non basta.

La colonna taker usa un campione recente nel primo run. Dopo almeno 3 fotografie distribuite su almeno 45 minuti viene sostituita automaticamente dalla media intraday 4h.

## Dati separati per exchange

| Asset | Exchange | Stato | Funding 8h eq. | Open interest | Taker flow | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | Kraken | OK | +0,0080% | 156,58 mln $ | 2,44 | +4,80% |
| BTC | Bitget | OK | +0,0100% | 2,71 mld $ | 0,33 | -0,39% |
| BTC | Kucoin | OK | +0,0100% | 1,64 mld $ | 1,56 | +2,47% |
| SOL | Kraken | OK | -0,0188% | 31,52 mln $ | 1,19 | -6,83% |
| SOL | Bitget | OK | +0,0100% | 395,64 mln $ | 0,00 | +41,38% |
| SOL | Kucoin | OK | +0,0100% | 230,28 mln $ | 0,91 | +13,01% |
| DOGE | Kraken | OK | +0,0157% | 4,96 mln $ | 1,31 | +23,43% |
| DOGE | Bitget | OK | +0,0100% | 120,34 mln $ | 0,11 | +48,16% |
| DOGE | Kucoin | OK | +0,0100% | 141,87 mln $ | 0,81 | +23,64% |

Kraken, Bitget e KuCoin contribuiscono a funding normalizzato, open interest, trade aggressivi e order book. Non viene inventato un long/short ratio pubblico né un feed completo delle liquidazioni.

## Conferme per indicatori tecnici

### BTC

- Score grezzo exchange: **+2,25**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 1, accuratezza +100,00%.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 1, bear 1, divergenze 0.
- Flusso taker/order book: **+1,75**.
- OI/funding/basis: **+0,00**.
- Affollamento long/short: **+0,00**.
- Liquidazioni: **NON PESATE / FEED COMPLETO NON ASSUNTO DISPONIBILE**.
- **Wyckoff:** Fase Wyckoff non abbastanza chiara per una conferma exchange.
- **Fibonacci:** Fibonacci rejection; nessuna conferma exchange netta. Confluenza tecnica dichiarata: resistenza tecnica.
- **RSI:** RSI alto ma sostenuto da acquisti e leva non estrema: momentum ancora credibile.
- **Pattern:** I pattern candidati restano non operativi: i dati exchange possono solo preparare la conferma.
- **Breakout/breakdown:** Resistenza vicina con acquisti aggressivi: breakout più credibile, ma serve chiusura sopra il livello.
- **Mappa liquidità attuale:** muro bid: n/a; muro ask: n/a

![Microstruttura exchange BTC](exchange_microstructure_BTC.png)

### SOL

- Score grezzo exchange: **+0,75**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 2, accuratezza +0,00%.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 1, bear 2, divergenze 0.
- Flusso taker/order book: **+0,75**.
- OI/funding/basis: **+0,00**.
- Affollamento long/short: **+0,00**.
- Liquidazioni: **NON PESATE / FEED COMPLETO NON ASSUNTO DISPONIBILE**.
- **Wyckoff:** Fase Wyckoff non abbastanza chiara per una conferma exchange.
- **Fibonacci:** Livello Fibonacci soltanto testato: order book e taker flow non bastano ancora per dichiararlo tenuto o perso.
- **RSI:** RSI in zona non estrema o flusso exchange non abbastanza netto.
- **Pattern:** I pattern candidati restano non operativi: i dati exchange possono solo preparare la conferma.
- **Breakout/breakdown:** Prezzo non abbastanza vicino a un livello chiave o flusso non netto.
- **Mappa liquidità attuale:** muro bid: n/a; muro ask: n/a

![Microstruttura exchange SOL](exchange_microstructure_SOL.png)

### DOGE

- Score grezzo exchange: **+3,25**; candidato: **+1**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 4, accuratezza +50,00%.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 1, bear 2, divergenze 0.
- Flusso taker/order book: **+2,00**.
- OI/funding/basis: **+1,00**.
- Affollamento long/short: **+0,00**.
- Liquidazioni: **NON PESATE / FEED COMPLETO NON ASSUNTO DISPONIBILE**.
- **Wyckoff:** Fase Wyckoff non abbastanza chiara per una conferma exchange.
- **Fibonacci:** Fibonacci rejection; nessuna conferma exchange netta.
- **RSI:** RSI alto ma sostenuto da acquisti e leva non estrema: momentum ancora credibile.
- **Pattern:** I pattern candidati restano non operativi: i dati exchange possono solo preparare la conferma.
- **Breakout/breakdown:** Prezzo non abbastanza vicino a un livello chiave o flusso non netto.
- **Mappa liquidità attuale:** muro bid: n/a; muro ask: n/a

![Microstruttura exchange DOGE](exchange_microstructure_DOGE.png)

## Overlay sulle previsioni a 30 giorni

La previsione storica grezza dello scanner resta intatta. L'overlay exchange può correggerla solo dopo almeno 30 controlli maturati a 30 giorni e solo se il modulo dimostra accuratezza direzionale almeno del 55%.

| Asset | Prob. grezza salita | Return p50 grezzo | Controlli 30g | Accuratezza exchange | Stato overlay | Peso | Prob. corretta | Return corretto |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +60,00% | +5,87% | 1 | +0,00% | RACCOLTA DATI | 0,00 | +60,00% | +5,87% |
| SOL | +52,50% | +1,63% | 1 | +100,00% | RACCOLTA DATI | 0,00 | +52,50% | +1,63% |
| DOGE | +52,50% | +1,87% | 2 | +100,00% | RACCOLTA DATI | 0,00 | +52,50% | +1,87% |

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

Generato: 2026-08-24 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [exchange_signal_tracker_report.md](exchange_signal_tracker_report.md)

Questo tracker verifica se il segnale candidato exchange ±1 anticipa correttamente la direzione del prezzo a 1/3/7/14/30 giorni.
Il peso Global resta 0 finché l'orizzonte 7g non ha almeno 30 controlli, accuratezza almeno 55% e return corretto direzione positivo. L'overlay a 30g ha un gate separato.

Controlli maturati completati in questa esecuzione: **15**.

## Ultime fotografie giornaliere

| Data | Asset | Prezzo | Versione | Calibrazione | Candidato | Peso Global | Score raw | Confidenza | Taker 4h | OI 24h | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08-24 | BTC | 76.901,40 | V2.1.3 | OK | 0 | 0 | 2,25 | MEDIA | 3,80 | +2,92% | +1,83% |
| 2026-08-24 | DOGE | 0.09180 | V2.1.3 | OK | 1 | 0 | 3,25 | MEDIA | 1,09 | +2,91% | +15,94% |
| 2026-08-24 | SOL | 93,87 | V2.1.3 | OK | 0 | 0 | 0,75 | BASSA | 0,55 | -4,62% | +13,79% |
| 2026-08-23 | BTC | 76.568,40 | V2.1.3 | OK | 1 | 0 | 2,50 | MEDIA | 2,97 | +1,29% | +6,02% |
| 2026-08-23 | DOGE | 0.08987 | V2.1.3 | OK | 0 | 0 | 3,00 | MEDIA | 0,96 | -8,05% | +28,88% |
| 2026-08-23 | SOL | 92,73 | V2.1.3 | OK | 0 | 0 | 2,25 | BASSA | 1,39 | +0,09% | +8,75% |
| 2026-08-22 | BTC | 78.429,65 | V2.1.3 | OK | 0 | 0 | 2,25 | MEDIA | 3,22 | +0,83% | +1,96% |
| 2026-08-22 | DOGE | 0.09866 | V2.1.3 | OK | 1 | 0 | 3,00 | MEDIA | 1,28 | +14,08% | -2,18% |
| 2026-08-22 | SOL | 99,08 | V2.1.3 | OK | 0 | 0 | 0,75 | BASSA | 0,82 | +2,53% | -4,64% |

## Accuratezza direzionale

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 2 | +100,00% | +1,05% | +0,71% | +1,68% | FEEDBACK RAPIDO |
| BTC | 3g | 1 | +100,00% | +1,47% | -1,13% | +3,82% | FEEDBACK RAPIDO |
| BTC | 7g | 1 | +100,00% | +1,35% | -1,18% | +3,82% | FEEDBACK RAPIDO |
| BTC | 14g | 1 | +0,00% | -2,63% | -3,44% | +3,82% | FEEDBACK RAPIDO |
| BTC | 30g | 1 | +0,00% | -0,24% | -3,45% | +3,82% | FEEDBACK RAPIDO |
| SOL | 1g | 3 | +66,67% | +1,62% | +1,05% | +5,09% | FEEDBACK RAPIDO |
| SOL | 3g | 3 | +33,33% | +0,40% | -2,47% | +5,55% | FEEDBACK RAPIDO |
| SOL | 7g | 2 | +0,00% | -3,56% | -4,18% | +1,44% | FEEDBACK RAPIDO |
| SOL | 14g | 2 | +50,00% | +8,38% | -5,94% | +13,89% | FEEDBACK RAPIDO |
| SOL | 30g | 1 | +100,00% | +8,60% | -9,55% | +9,55% | FEEDBACK RAPIDO |
| DOGE | 1g | 6 | +50,00% | +1,03% | +0,16% | +2,33% | FEEDBACK RAPIDO |
| DOGE | 3g | 5 | +60,00% | +5,05% | -0,78% | +9,18% | FEEDBACK RAPIDO |
| DOGE | 7g | 4 | +50,00% | +0,28% | -0,90% | +5,64% | FEEDBACK RAPIDO |
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

**BTC** — BTC: i futures sembrano più vulnerabili verso una discesa improvvisa. Non significa che deve scendere, ma se rompe sotto può accelerare. Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale.

**SOL** — SOL: i futures sembrano più vulnerabili verso una discesa improvvisa. Non significa che deve scendere, ma se rompe sotto può accelerare. Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale.

**DOGE** — DOGE: i futures sembrano più vulnerabili verso una discesa improvvisa. Non significa che deve scendere, ma se rompe sotto può accelerare. Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale.

| Asset | Prezzo | Funding | OI 24h | Long/Short | Lettura futures | Forza |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 77.028 $ | +0.0100% | -11.44% | 1.72 | Rischio sotto | 2/5 |
| SOL | 94,05 $ | +0.0100% | -17.34% | 2.78 | Rischio sotto | 2/5 |
| DOGE | 0.09210 $ | +0.0100% | -15.96% | 3.71 | Rischio sotto | 2/5 |

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

Generato: 2026-08-24 05:32 UTC


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
| BTC     | 1D   | Hidden bullish     | CONFERMATA    | 76.962 $ / 79,64  | 2026-08-03 62.227 $ / RSI 47,40 → 2026-08-14 62.488 $ / RSI 42,71   | n/a                 | n/a              |      0 |
| BTC     | 1W   | Conferma rialzista | CONTESTO      | 76.962 $ / 55,92  | n/a                                                                 | +18,97%             | 16,18            |      0 |
| SOL     | 1D   | Conferma rialzista | CONTESTO      | 93,82 $ / 82,88   | n/a                                                                 | +23,10%             | 27,78            |      0 |
| SOL     | 1W   | Hidden bearish     | CONFERMATA    | 93,82 $ / 53,63   | 2026-05-17 98,27 $ / RSI 38,29 → 2026-07-05 83,81 $ / RSI 42,25     | n/a                 | n/a              |      0 |
| DOGE    | 1D   | Conferma rialzista | CONTESTO      | 0.09174 $ / 83,17 | n/a                                                                 | +32,47%             | 41,79            |      0 |
| DOGE    | 1W   | Hidden bearish     | IN_FORMAZIONE | 0.09174 $ / 48,80 | 2026-05-17 0.11825 $ / RSI 44,25 → 2026-08-23 0.09998 $ / RSI 48,92 | n/a                 | n/a              |      0 |

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

Generato: 2026-08-24 05:32 UTC


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
| BTC | 77.028 $ | 9 | RIALZISTA TECNICO | Trend rialzista | Momentum in miglioramento | Compressione / triangolo | 0 | -1 / REJECTION | Doppio minimo / TARGET RAGGIUNTO | Doppio massimo / CANDIDATO | 62.488 | 77.991 |
| SOL | 94,05 $ | 10 | RIALZISTA TECNICO | Trend rialzista | Momentum in miglioramento | Compressione / triangolo | 0 | 0 / TESTATO | Doppio minimo / TARGET RAGGIUNTO | Doppio massimo / CANDIDATO | 74,20 | 98,27 |
| DOGE | 0.09210 $ | 8 | RIALZISTA TECNICO | Trend misto | Momentum in miglioramento | Struttura rialzista con massimi e minimi crescenti | 0 | 0 / REJECTION | Triplo minimo / TARGET RAGGIUNTO | Doppio massimo / CANDIDATO | 0.06895 | 0.11825 |

## Riepilogo ciclo di vita pattern

| Asset   | Doppio minimo    | Triplo minimo    | Adam/Eve Bottom                        | Doppio massimo   | Triplo massimo   | Adam/Eve Top                 |   Punteggio pattern |
|:--------|:-----------------|:-----------------|:---------------------------------------|:-----------------|:-----------------|:-----------------------------|--------------------:|
| BTC | TARGET RAGGIUNTO | TARGET RAGGIUNTO | Adam and Eve Bottom — TARGET RAGGIUNTO | CANDIDATO | CANDIDATO | Adam and Eve Top — CANDIDATO | 0 |
| SOL | TARGET RAGGIUNTO | TARGET RAGGIUNTO | Adam and Eve Bottom — TARGET RAGGIUNTO | CANDIDATO | CANDIDATO | Adam and Eve Top — CANDIDATO | 0 |
| DOGE | TARGET RAGGIUNTO | TARGET RAGGIUNTO | Adam and Eve Bottom — TARGET RAGGIUNTO | CANDIDATO | CANDIDATO | Adam and Eve Top — CANDIDATO | 0 |

## Indicatori tecnici

| Asset   |   RSI 14 |   Istogramma MACD | MA20    | MA50    | MA200   | Pendenza MA50 20g   | Pendenza MA200 60g   | Rendimento 30g   | Rendimento 90g   |
|:--------|---------:|------------------:|:--------|:--------|:--------|:--------------------|:---------------------|:-----------------|:-----------------|
| BTC | 79.94 | 1604.54 | 66.728 | 65.140 | 69.001 | 2,97% | -9,39% | 19,77% | 1,59% |
| SOL | 83.33 | 2.20312 | 79,13 | 77,37 | 81,14 | 3,13% | -15,57% | 26,36% | 12,52% |
| DOGE | 83.94 | 0.00278 | 0.07401 | 0.07294 | 0.08923 | -2,08% | -15,89% | 28,50% | -8,73% |

## Dettaglio asset

### BTC

- Prezzo: **77.028 $**
- Punteggio tecnico: **9 / 12**
- Verdetto: **RIALZISTA TECNICO**
- Trend: **Trend rialzista** (3)
- Momentum: **Momentum in miglioramento** (3)
- Volume: **Volume da accumulazione** (1)
- Struttura: **Compressione / triangolo** (0)
  - Dettaglio struttura: Ultimi minimi: 6.223e+04 -> 6.249e+04. Ultimi massimi: 6.691e+04 -> 6.54e+04.
- Divergenza: **Divergenza rialzista nascosta RSI** (1)
- Fase Wyckoff candidata: **Markup / fase rialzista** (2)
  - Dettaglio Wyckoff: Prezzo sopra MA200, MA50 in salita e trend a 30 giorni positivo.
- Fibonacci automatico: **REJECTION** (-1)
  - Swing DOWN 2026-05-06 82.792 -> 2026-08-14 62.488; livello più vicino 78.6% a 78.447; stato REJECTION; confluenza: resistenza tecnica.
- Punteggio pattern: **0**
  - rialzista dominante: Doppio minimo (TARGET RAGGIUNTO, 0); ribassista dominante: Doppio massimo (CANDIDATO, 0).
- Supporto più vicino: **62.488**
- Resistenza più vicina: **77.991**

Pattern classici e ciclo di vita:

- Doppio minimo: **TARGET RAGGIUNTO** (0)
  - Due minimi simili vicino a 62.201 tra 2026-06-18 e 2026-08-14. Neckline stimata: 66.910. Breakout neckline: 2026-08-19 (5 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 71.619; progresso corrente: 214,88%. Relazione prezzo/neckline: sopra neckline.
  - neckline 66.910; target 71.619; breakout 2026-08-19 (5g); progresso 214,88%; prezzo sopra neckline.
- Triplo minimo: **TARGET RAGGIUNTO** (0)
  - Tre minimi simili vicino a 62.201 dal 2026-06-18 al 2026-08-14. Neckline stimata: 66.910. Breakout neckline: 2026-08-19 (5 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 71.619; progresso corrente: 214,88%. Relazione prezzo/neckline: sopra neckline.
  - neckline 66.910; target 71.619; breakout 2026-08-19 (5g); progresso 214,88%; prezzo sopra neckline.
- Adam and Eve Bottom: **TARGET RAGGIUNTO** (0)
  - Pattern Adam and Eve Bottom vicino a 59.109 dal 2026-06-05 al 2026-08-14. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 67.248. Breakout neckline: 2026-08-19 (5 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 75.387; progresso corrente: 120,16%. Relazione prezzo/neckline: sopra neckline.
  - neckline 67.248; target 75.387; breakout 2026-08-19 (5g); progresso 120,16%; prezzo sopra neckline.
- Doppio massimo: **CANDIDATO** (0)
  - Due massimi simili vicino a 65.544 tra 2026-06-22 e 2026-08-09. Neckline ribassista stimata: 57.748. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 15 giorni.
  - neckline 57.748; target 49.952; distanza dalla neckline 33,39%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 65.544 dal 2026-06-22 al 2026-08-09. Neckline ribassista stimata: 57.748. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 15 giorni.
  - neckline 57.748; target 49.952; distanza dalla neckline 33,39%; prezzo sopra neckline.
- Adam and Eve Top: **CANDIDATO** (0)
  - Pattern Adam and Eve Top vicino a 67.248 dal 2026-06-15 al 2026-07-21. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 57.748. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 34 giorni.
  - neckline 57.748; target 48.247; distanza dalla neckline 33,39%; prezzo sopra neckline.

### SOL

- Prezzo: **94,05 $**
- Punteggio tecnico: **10 / 12**
- Verdetto: **RIALZISTA TECNICO**
- Trend: **Trend rialzista** (3)
- Momentum: **Momentum in miglioramento** (3)
- Volume: **Volume da accumulazione** (2)
- Struttura: **Compressione / triangolo** (0)
  - Dettaglio struttura: Ultimi minimi: 70.69 -> 74.2. Ultimi massimi: 78.73 -> 77.62.
- Divergenza: **Nessuna** (0)
- Fase Wyckoff candidata: **Markup / fase rialzista** (2)
  - Dettaglio Wyckoff: Prezzo sopra MA200, MA50 in salita e trend a 30 giorni positivo.
- Fibonacci automatico: **TESTATO** (0)
  - Swing DOWN 2026-05-11 98,27 -> 2026-08-16 74,20; livello più vicino 78.6% a 93,12; stato TESTATO; confluenza: nessuna confluenza indipendente.
- Punteggio pattern: **0**
  - rialzista dominante: Doppio minimo (TARGET RAGGIUNTO, 0); ribassista dominante: Doppio massimo (CANDIDATO, 0).
- Supporto più vicino: **74,20**
- Resistenza più vicina: **98,27**

Pattern classici e ciclo di vita:

- Doppio minimo: **TARGET RAGGIUNTO** (0)
  - Due minimi simili vicino a 73,40 tra 2026-07-17 e 2026-08-16. Neckline stimata: 78,73. Breakout neckline: 2026-08-19 (5 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 84,05; progresso corrente: 287,82%. Relazione prezzo/neckline: sopra neckline.
  - neckline 78,73; target 84,05; breakout 2026-08-19 (5g); progresso 287,82%; prezzo sopra neckline.
- Triplo minimo: **TARGET RAGGIUNTO** (0)
  - Tre minimi simili vicino a 70,69 dal 2026-07-17 al 2026-08-16. Neckline stimata: 78,73. Breakout neckline: 2026-08-19 (5 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 86,76; progresso corrente: 190,79%. Relazione prezzo/neckline: sopra neckline.
  - neckline 78,73; target 86,76; breakout 2026-08-19 (5g); progresso 190,79%; prezzo sopra neckline.
- Adam and Eve Bottom: **TARGET RAGGIUNTO** (0)
  - Pattern Adam and Eve Bottom vicino a 67,92 dal 2026-06-19 al 2026-08-01. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 83,81. Breakout neckline: 2026-08-19 (5 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 99,70; progresso corrente: 64,45%. Relazione prezzo/neckline: sopra neckline.
  - neckline 83,81; target 99,70; breakout 2026-08-19 (5g); progresso 64,45%; prezzo sopra neckline.
- Doppio massimo: **CANDIDATO** (0)
  - Due massimi simili vicino a 77,62 tra 2026-06-22 e 2026-08-09. Neckline ribassista stimata: 64,42. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 15 giorni.
  - neckline 64,42; target 51,22; distanza dalla neckline 46,00%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 78,88 dal 2026-07-15 al 2026-08-09. Neckline ribassista stimata: 70,69. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 15 giorni.
  - neckline 70,69; target 62,51; distanza dalla neckline 33,04%; prezzo sopra neckline.
- Adam and Eve Top: **CANDIDATO** (0)
  - Pattern Adam and Eve Top vicino a 77,62 dal 2026-06-15 al 2026-08-09. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 64,42. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 15 giorni.
  - neckline 64,42; target 51,22; distanza dalla neckline 46,00%; prezzo sopra neckline.

### DOGE

- Prezzo: **0.09210 $**
- Punteggio tecnico: **8 / 12**
- Verdetto: **RIALZISTA TECNICO**
- Trend: **Trend misto** (1)
- Momentum: **Momentum in miglioramento** (3)
- Volume: **Volume da accumulazione** (2)
- Struttura: **Struttura rialzista con massimi e minimi crescenti** (2)
  - Dettaglio struttura: Ultimi minimi: 0.06835 -> 0.06895. Ultimi massimi: 0.07117 -> 0.07286.
- Divergenza: **Nessuna** (0)
- Fase Wyckoff candidata: **Range / fase non chiara** (0)
  - Dettaglio Wyckoff: Posizione nel range a 120 giorni: 47,98%. Fase non abbastanza chiara.
- Fibonacci automatico: **REJECTION** (0)
  - Swing DOWN 2026-05-14 0.11825 -> 2026-08-12 0.06895; livello più vicino 50.0% a 0.09360; stato REJECTION; confluenza: nessuna confluenza indipendente.
- Punteggio pattern: **0**
  - rialzista dominante: Triplo minimo (TARGET RAGGIUNTO, 0); ribassista dominante: Doppio massimo (CANDIDATO, 0).
- Supporto più vicino: **0.06895**
- Resistenza più vicina: **0.11825**

Pattern classici e ciclo di vita:

- Doppio minimo: **TARGET RAGGIUNTO** (0)
  - Due minimi simili vicino a 0.06829 tra 2026-07-24 e 2026-08-12. Neckline stimata: 0.07380. Breakout neckline: 2026-08-19 (5 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 0.07931; progresso corrente: 331,99%. Relazione prezzo/neckline: sopra neckline.
  - neckline 0.07380; target 0.07931; breakout 2026-08-19 (5g); progresso 331,99%; prezzo sopra neckline.
- Triplo minimo: **TARGET RAGGIUNTO** (0)
  - Tre minimi simili vicino a 0.06835 dal 2026-06-30 al 2026-08-12. Neckline stimata: 0.07923. Breakout neckline: 2026-08-20 (4 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 0.09012; progresso corrente: 118,20%. Relazione prezzo/neckline: sopra neckline.
  - neckline 0.07923; target 0.09012; breakout 2026-08-20 (4g); progresso 118,20%; prezzo sopra neckline.
- Adam and Eve Bottom: **TARGET RAGGIUNTO** (0)
  - Pattern Adam and Eve Bottom vicino a 0.06829 dal 2026-07-24 al 2026-08-06. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 0.07380. Breakout neckline: 2026-08-19 (5 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 0.07931; progresso corrente: 331,99%. Relazione prezzo/neckline: sopra neckline.
  - neckline 0.07380; target 0.07931; breakout 2026-08-19 (5g); progresso 331,99%; prezzo sopra neckline.
- Doppio massimo: **CANDIDATO** (0)
  - Due massimi simili vicino a 0.07380 tra 2026-07-26 e 2026-08-11. Neckline ribassista stimata: 0.06797. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 13 giorni.
  - neckline 0.06797; target 0.06214; distanza dalla neckline 35,49%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 0.07923 dal 2026-07-04 al 2026-08-11. Neckline ribassista stimata: 0.06797. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 13 giorni.
  - neckline 0.06797; target 0.05671; distanza dalla neckline 35,49%; prezzo sopra neckline.
- Adam and Eve Top: **CANDIDATO** (0)
  - Pattern Adam and Eve Top vicino a 0.07923 dal 2026-07-04 al 2026-08-11. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 0.06797. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 13 giorni.
  - neckline 0.06797; target 0.05671; distanza dalla neckline 35,49%; prezzo sopra neckline.

## Fibonacci automatico

Il modulo seleziona uno swing recente tramite pivot confermati. Un semplice tocco vale 0: Fibonacci pesa al massimo ±1 soltanto quando il livello è tenuto, perso, recuperato o respinto e coincide con almeno un livello tecnico indipendente.

| Asset   | Swing                         | 23,6%   | 38,2%   | 50,0%   | 61,8%   | 78,6%   | Livello vicino   | Stato     | Confluenza                      |   Score |
|:--------|:------------------------------|:--------|:--------|:--------|:--------|:--------|:-----------------|:----------|:--------------------------------|--------:|
| BTC | DOWN 2026-05-06 -> 2026-08-14 | 67.280 | 70.244 | 72.640 | 75.036 | 78.447 | 78.6% / 78.447 | REJECTION | resistenza tecnica | -1 |
| SOL | DOWN 2026-05-11 -> 2026-08-16 | 79,88 | 83,40 | 86,24 | 89,07 | 93,12 | 78.6% / 93,12 | TESTATO | nessuna confluenza indipendente | 0 |
| DOGE | DOWN 2026-05-14 -> 2026-08-12 | 0.08059 | 0.08779 | 0.09360 | 0.09942 | 0.10770 | 50.0% / 0.09360 | REJECTION | nessuna confluenza indipendente | 0 |

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

- **BTC**: 23/30 previsioni controllate su 51 fatte. Stato: **RACCOLTA DATI**.
- **SOL**: 23/30 previsioni controllate su 51 fatte. Stato: **RACCOLTA DATI**.
- **DOGE**: 23/30 previsioni controllate su 51 fatte. Stato: **RACCOLTA DATI**.

| Asset | Previsioni fatte | Controllate | Progresso | In attesa | Stato | Prossimo controllo |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 51 | 23 | 23/30 [████████░░] | 28 | RACCOLTA DATI | 2026-08-25 / tra 1 giorno |
| SOL | 51 | 23 | 23/30 [████████░░] | 28 | RACCOLTA DATI | 2026-08-25 / tra 1 giorno |
| DOGE | 51 | 23 | 23/30 [████████░░] | 28 | RACCOLTA DATI | 2026-08-25 / tra 1 giorno |

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

Generato: 2026-08-24 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [data_quality_coherence_report.md](data_quality_coherence_report.md)

Questo controllo non modifica punteggi o decisioni. Verifica che tutti i moduli usino lo stesso prezzo corrente e che le nuove regole Technical/Classic Visual siano integre.

## Stato finale: **WARN**

## Avvisi

- 1 campi prezzo superano la tolleranza specifica del modulo.

## Prezzo unico per modulo

| Modulo                  | Asset   | Campo             | Stato   | Prezzo snapshot   | Prezzo modulo   | Differenza   |
|:------------------------|:--------|:------------------|:--------|:------------------|:----------------|:-------------|
| Scanner                 | BTC     | current_price     | OK      | 77.028 $          | 77.028 $        | +0,0000%     |
| Scanner                 | DOGE    | current_price     | OK      | 0.09210 $         | 0.09210 $       | -0,0000%     |
| Scanner                 | SOL     | current_price     | OK      | 94,05 $           | 94,05 $         | -0,0000%     |
| Scanner Forecast        | BTC     | current_price     | OK      | 77.028 $          | 77.028 $        | +0,0000%     |
| Scanner Forecast        | SOL     | current_price     | OK      | 94,05 $           | 94,05 $         | -0,0000%     |
| Scanner Forecast        | DOGE    | current_price     | OK      | 0.09210 $         | 0.09210 $       | -0,0000%     |
| Technical Structure     | BTC     | price             | OK      | 77.028 $          | 77.028 $        | +0,0000%     |
| Technical Structure     | SOL     | price             | OK      | 94,05 $           | 94,05 $         | -0,0000%     |
| Technical Structure     | DOGE    | price             | OK      | 0.09210 $         | 0.09210 $       | -0,0000%     |
| Classic Technical       | BTC     | price             | OK      | 77.028 $          | 77.028 $        | +0,0000%     |
| Classic Technical       | SOL     | price             | OK      | 94,05 $           | 94,05 $         | -0,0000%     |
| Classic Technical       | DOGE    | price             | OK      | 0.09210 $         | 0.09210 $       | -0,0000%     |
| Classic Visual          | BTC     | price             | OK      | 77.028 $          | 77.028 $        | +0,0000%     |
| Classic Visual          | SOL     | price             | OK      | 94,05 $           | 94,05 $         | -0,0000%     |
| Classic Visual          | DOGE    | price             | OK      | 0.09210 $         | 0.09210 $       | -0,0000%     |
| Exchange Microstructure | BTC     | price             | OK      | 77.028 $          | 76.901 $        | -0,1648%     |
| Exchange Microstructure | SOL     | price             | OK      | 94,05 $           | 93,87 $         | -0,1882%     |
| Exchange Microstructure | DOGE    | price             | WARN    | 0.09210 $         | 0.09180 $       | -0,3257%     |
| RSI top-cycle           | SOL     | current_price     | OK      | 94,05 $           | 94,05 $         | -0,0000%     |
| RSI top-cycle           | SOL     | current_price     | OK      | 94,05 $           | 94,05 $         | -0,0000%     |
| Frattale BTC/SOL        | SOL     | sol_current_price | OK      | 94,05 $           | 94,05 $         | -0,0000%     |
| Fractal path            | SOL     | current_price     | OK      | 94,05 $           | 94,05 $         | -0,0000%     |

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

Generato: 2026-08-25T00:30:34+00:00

- Modalità: **SOLO PAPER TRADING**
- Asset: **SOL spot**
- Leva: **nessuna (1x)**
- Capitale iniziale separato: **€40.000,00**
- Fonte mercato: **KUCOIN_PUBLIC_API**; nuove entrate: **CONSENTITE**

| Equity | Cash | SOL | Prezzo | Rendimento | Realizzato | Commissioni | Max DD | Operazioni |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €43.453,09 | €43.453,09 | 0.000083 | 98.9480 | +8.63% | €3.453,09 | €75,44 | 6.48% | 41 |

**Ultima decisione:** SELL_40_PERCENT — SOL sopra la seconda banda adattiva.

Bande 4H: L2 86.6319 · L1 89.2207 · media 92.4567 · U1 95.6926 · U2 98.2814.

> Questo portafoglio non condivide capitale, posizioni o statistiche con il paper trading da €10.000.
<!-- SOL_SPOT_ADAPTIVE_END -->
