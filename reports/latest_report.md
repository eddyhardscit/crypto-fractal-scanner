<!-- COMPACT_REPORT_HEADER_START -->
> **Vista compatta:** Decisione operativa, Global Confluence e cambiamenti giornalieri restano aperti. Tocca il titolo di una sezione per mostrare o nascondere i dettagli.  
> Tutte le tabelle e tutti i dati restano nel file: copiando il Markdown raw viene copiato tutto.
<!-- COMPACT_REPORT_HEADER_END -->

<!-- COMPACT_SECTION_START:decision -->
<details open>
<summary><strong>🧭 Decisione operativa — da leggere per prima</strong></summary>

<!-- DECISION_REPORT_START -->

# Decisione operativa sintetica

Generato: 2026-09-10 05:33 UTC

Report separato completo: [decision_report.md](decision_report.md)

Sintesi automatica dello scanner: l'azione spot viene copiata direttamente dal Global Confluence; long, short e rischio restano filtri separati e più prudenti.

| Asset | Global | Direzione | Spot | Long leva | Short leva | Max long | Max short | Rischio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +6 | BULLISH | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE | LONG PRUDENTE | NO SHORT | max 2x isolated | nessuna | MEDIO |
| SOL | +5 | NEUTRALE / COSTRUTTIVO | HOLD / TRANCHE PICCOLE, NO LEVA | NO LONG A LEVA | NO SHORT | nessuna | nessuna | MOLTO ALTO |
| DOGE | -4 | BEARISH | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE | NO LONG A LEVA | SHORT SOLO DOPO SPIKE | nessuna | max 1x-2x isolated | MOLTO ALTO |

## Lettura immediata

- **BTC**: Global = **+6**, spot = **ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE**, long = **LONG PRUDENTE**, short = **NO SHORT**, rischio = **MEDIO**.
- **SOL**: Global = **+5**, spot = **HOLD / TRANCHE PICCOLE, NO LEVA**, long = **NO LONG A LEVA**, short = **NO SHORT**, rischio = **MOLTO ALTO**.
- **DOGE**: Global = **-4**, spot = **STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE**, long = **NO LONG A LEVA**, short = **SHORT SOLO DOPO SPIKE**, rischio = **MOLTO ALTO**.

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

- Global Confluence: **+5**
- Confluenza: **MODERATAMENTE POSITIVA**
- Bias Global: **Costruttivo prudente**
- Direzione decisionale: **NEUTRALE / COSTRUTTIVO**
- Azione spot dal Global: **HOLD / TRANCHE PICCOLE, NO LEVA**
- Long leva: **NO LONG A LEVA**
- Short leva: **NO SHORT**
- Rischio: **MOLTO ALTO**
- Conferme: Doppio minimo target raggiunto finché mantiene 78,73; nuova conferma tecnica sopra 110,04; milestone analogiche 107,12 / 134,20, valide soltanto se rientra anche il gap frattale.
- Invalidazioni: Allarmi sotto 88,87 / 97,45 / 62,19.

### DOGE

- Global Confluence: **-4**
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
- **Lifecycle EMA200** = per SOL resta solo contesto, peso Global 0; score interno 2; EMA200 circa 111,24 $; upside verso EMA200 +9,03%. Non autorizza leva e non aggiunge punti automatici.
- **NO LONG** non significa automaticamente **SHORT**. Lo short ha senso solo se il quadro è bearish o se lo spike viene spesso scaricato.
- Per SOL, se il Global è da **+3 in su**, la decisione non deve diventare bearish solo perché lo scanner grezzo a 30 giorni è incerto.

<!-- DECISION_REPORT_END -->

<!-- PAPER_TRADING_START -->
# Paper trading automatico KuCoin

Generato: 2026-09-10T05:33:21+00:00


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [paper_trading_report.md](paper_trading_report.md)

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-09-10T05:05:33+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-09-10T05:05:33+00:00 | 2026-09-10T05:05:33+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-09-10T04:45:00+00:00 | 2026-09-10T04:45:00+00:00 | 5,7 min | 25,0 min | OK |
| 60m | 12 | 2026-09-10T04:00:00+00:00 | 2026-09-10T04:00:00+00:00 | 5,7 min | 45,0 min | OK |
| 240m | 12 | 2026-09-10T00:00:00+00:00 | 2026-09-10T00:00:00+00:00 | 1,09 h | 1,00 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | DOGE | 240m | SHORT | -3,71 | 6,00 | 2,29 | STALE_CANDLE | 1,09 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | BTC | 240m | SHORT | -3,00 | 6,00 | 3,00 | STALE_CANDLE | 1,09 h | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | PEPE | 240m | SHORT | -2,83 | 6,00 | 3,17 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | ETH | 240m | LONG | 1,64 | 6,00 | 4,36 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | SOL | 240m | SHORT | -1,45 | 6,00 | 4,55 | STALE_CANDLE | 1,09 h | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | PUMP | 240m | SHORT | -1,23 | 6,00 | 4,77 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | SUI | 240m | SHORT | -0,75 | 6,00 | 5,25 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | DASH | 240m | SHORT | -0,64 | 6,00 | 5,36 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | HYPE | 240m | LONG | 0,14 | 6,00 | 5,86 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Principale 4H | XRP | 240m | SHORT | -0,05 | 6,00 | 5,95 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.7 minuti; tolleranza 60 minuti. |
| Bilanciata 1H V3 Filtered | DASH | 60m | SHORT | -6,25 | 6,00 | 0,00 | READY | 5,7 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Forza relativa 1H V1 | DASH | 60m | SHORT | -6,25 | 4,00 | 0,00 | READY | 5,7 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Forza relativa 1H V2 | DASH | 60m | SHORT | -6,25 | 5,50 | 0,00 | READY | 5,7 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Benchmark trend following EMA 1H | DASH | 60m | SHORT | -6,25 | 5,00 | 0,00 | READY | 5,7 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Scanner Bottom 5 Short 1H | DASH | 60m | SHORT | -6,25 | 5,00 | 0,00 | READY | 5,7 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Scanner Bottom10 Short | DASH | 60m | SHORT | -6,25 | 5,00 | 0,00 | READY | 5,7 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Scanner Bottom15 Short | DASH | 60m | SHORT | -6,25 | 5,00 | 0,00 | READY | 5,7 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Scanner Bottom20 Short | DASH | 60m | SHORT | -6,25 | 5,00 | 0,00 | READY | 5,7 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Combo Trend | DASH | 60m | SHORT | -6,25 | 5,00 | 0,00 | READY | 5,7 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Combo Adaptive | DASH | 60m | SHORT | -6,25 | 5,00 | 0,00 | READY | 5,7 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.816,14 | -1,84% | €7,58 | €3.000,00 | 0,25% | 5 | 60 | 41,67% | 0,88 | 6,86% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 60 | 3367 | PRIME INDICAZIONI | 100 (mancano 40) |

- Trade del Principale 4H chiusi: **60**; win rate **41,67%**; profit factor **0,88**.
- Expectancy: **€-3,05** per trade; P&L netto: **€-182,77**; max drawdown: **6,86%**.
- Valutazione: **Si può osservare la direzione, ma il risultato resta fragile.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 5 | €9.816,14 | €700,63 | €2.101,90 | €196,32 | €0,00 |
| TEST | Benchmark Donchian breakout 1H | 7 | €11.400,31 | €2.905,10 | €5.810,19 | €227,87 | €45,25 |
| TEST | Donchian 1H Gb20 120R V1 | 7 | €11.131,90 | €2.836,70 | €5.673,40 | €222,51 | €44,19 |
| TEST | Main Side Regime Guard V1 | 6 | €11.115,61 | €706,41 | €2.119,24 | €222,42 | €-5,71 |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | 7 | €11.043,61 | €719,65 | €2.158,94 | €165,87 | €26,62 |
| TEST | Scanner Top 5 Long 1H | 5 | €10.942,98 | €1.156,76 | €2.313,52 | €218,05 | €0,00 |
| TEST | Combo Trend Side Regime Guard V1 | 6 | €10.790,32 | €1.449,24 | €2.898,47 | €167,65 | €0,00 |
| TEST | Combo Adaptive Long Only V1 | 7 | €10.772,68 | €2.424,05 | €4.848,11 | €216,01 | €257,83 |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | 6 | €10.586,75 | €3.847,77 | €11.543,32 | €106,90 | €76,62 |
| TEST | 1H Fast No Pepe V1 | 7 | €10.571,30 | €1.358,62 | €4.075,86 | €209,22 | €1,87 |
| TEST | Rapida 1H V2 | 1 | €10.464,00 | €749,31 | €2.247,94 | €51,80 | €0,00 |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | 6 | €10.444,81 | €1.574,84 | €4.724,51 | €208,59 | €48,87 |
| TEST | Rapida 1H V3 Filtered | 6 | €10.377,70 | €1.564,72 | €4.694,15 | €207,25 | €48,56 |
| TEST | Main Dynamic Asset Selector V1 | 2 | €10.369,72 | €344,54 | €1.033,63 | €101,76 | €24,84 |
| TEST | Combo Adaptive | 8 | €10.362,62 | €1.329,94 | €2.659,89 | €156,24 | €0,47 |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | 6 | €10.348,30 | €2.030,03 | €6.090,09 | €155,60 | €-8,41 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 0 | €10.300,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 0 | €10.271,73 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Scanner | 6 | €10.269,01 | €1.541,44 | €3.082,88 | €207,77 | €0,00 |
| TEST | Scanner Top15 Long | 7 | €10.260,66 | €2.283,82 | €4.567,64 | €205,41 | €-1,57 |
| TEST | Scanner Top20 Long | 7 | €10.260,66 | €2.283,82 | €4.567,64 | €205,41 | €-1,57 |
| TEST | Scanner Top 5 + forza BTC 1H | 6 | €10.258,16 | €1.100,94 | €2.201,87 | €205,39 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 0 | €10.239,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 0 | €10.235,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Donchian 1H | 1 | €10.223,65 | €1.140,45 | €3.421,36 | €51,18 | €-11,05 |
| TEST | Btc Bollinger 1H | 0 | €10.209,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top10 Long | 6 | €10.197,67 | €2.315,96 | €4.631,92 | €203,96 | €-0,35 |
| TEST | Ampia 4H | 9 | €10.194,67 | €1.023,36 | €2.046,73 | €203,96 | €1,11 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 0 | €10.185,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Score 6 75 Range Only V1 | 5 | €10.172,36 | €1.298,57 | €3.895,72 | €151,63 | €3,83 |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 0 | €10.145,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 4H | 0 | €10.138,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Nohigh Range Only V1 | 3 | €10.135,95 | €1.885,17 | €5.655,50 | €51,20 | €43,71 |
| TEST | Sol Donchian 4H | 1 | €10.115,63 | €574,98 | €1.149,96 | €50,72 | €-28,42 |
| TEST | Scanner Top5 Btc Tp3 V1 | 6 | €10.108,68 | €1.971,13 | €3.942,26 | €202,38 | €-9,57 |
| TEST | Scanner Top5 Btc Runner25 V1 | 6 | €10.102,76 | €1.969,98 | €3.939,95 | €202,26 | €-9,56 |
| TEST | Btc Bollinger 4H | 0 | €10.101,88 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 0 | €10.099,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 No Esports Long Only V1 | 6 | €10.085,04 | €1.025,59 | €3.076,78 | €199,91 | €-26,17 |
| TEST | Doge Donchian 1H | 1 | €10.073,14 | €817,40 | €2.452,21 | €50,33 | €8,09 |
| TEST | Combo Adaptive Partial 1R V1 | 5 | €10.049,05 | €1.969,94 | €3.939,88 | €151,12 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 0 | €10.048,77 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Tp2 V1 | 6 | €10.045,91 | €629,94 | €1.889,82 | €148,32 | €2,03 |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | 2 | €10.044,18 | €362,84 | €1.088,52 | €96,64 | €0,00 |
| TEST | Rapida 1H V1 | 0 | €10.043,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Balanced Short Trend Down Strict V1 | 0 | €10.035,46 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · prudente · 5x | 0 | €10.032,32 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €50 · 15x | 0 | €10.022,70 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €10.014,08 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €50 · 15x | 0 | €10.009,44 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 0 | €10.008,92 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Ema 1H | 1 | €10.008,16 | €767,12 | €2.301,36 | €49,95 | €20,08 |
| TEST | Sol Ema 4H | 0 | €10.005,51 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €10 · 15x | 0 | €10.004,54 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 0 | €10.003,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 0 | €10.002,82 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €10 · 15x | 0 | €10.001,89 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Continuation V1 | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €10 · 15x | 0 | €9.998,68 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · prudente · 5x | 0 | €9.996,83 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 0 | €9.995,23 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €10 · 15x | 0 | €9.994,07 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €50 · 15x | 0 | €9.993,42 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €10 · 15x | 0 | €9.988,90 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 4H | 0 | €9.980,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €50 · 15x | 0 | €9.970,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · prudente · 5x | 0 | €9.970,34 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 0 | €9.966,58 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 4H | 0 | €9.964,84 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Bollinger 1H | 1 | €9.952,59 | €919,62 | €2.758,86 | €49,90 | €-25,17 |
| TEST | Sol Ema 1H | 1 | €9.951,35 | €986,59 | €2.959,78 | €49,81 | €-9,56 |
| TEST | Sol Adaptive 1H | 1 | €9.948,32 | €987,60 | €2.962,81 | €49,77 | €-3,77 |
| TEST | Scalp RSI Long 25 · €50 · 15x | 0 | €9.944,51 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · prudente · 5x | 0 | €9.939,55 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | 0 | €9.935,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Side Regime Guard V1 | 7 | €9.923,16 | €1.093,08 | €2.186,17 | €99,60 | €31,16 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.917,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 4H | 0 | €9.914,14 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 1H | 1 | €9.912,40 | €1.292,04 | €3.876,13 | €49,61 | €-8,16 |
| TEST | Btc Adaptive 1H | 1 | €9.905,18 | €1.147,51 | €3.442,53 | €49,57 | €-7,24 |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | 2 | €9.888,15 | €354,62 | €1.063,86 | €94,46 | €0,00 |
| TEST | Eth Ema 4H | 1 | €9.870,92 | €690,19 | €1.380,39 | €49,44 | €-14,38 |
| TEST | 1H Fast V3 Nohigh V1 | 6 | €9.863,49 | €1.301,47 | €3.904,40 | €194,04 | €2,43 |
| TEST | Btc Donchian 4H | 0 | €9.861,10 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 0 | €9.837,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Forza relativa 1H V2 | 6 | €9.836,16 | €845,40 | €1.690,80 | €99,43 | €0,02 |
| TEST | 1H Fast V3 Long Only V1 | 5 | €9.820,32 | €1.357,46 | €4.072,39 | €194,60 | €-25,48 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 0 | €9.817,34 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Quality7 Regime V1 | 0 | €9.810,21 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Adaptive 1H | 0 | €9.771,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 1H | 0 | €9.765,13 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 0 | €9.762,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Nohigh Cap75 V1 | 5 | €9.760,22 | €1.014,96 | €3.044,88 | €146,10 | €41,22 |
| TEST | Eth Bollinger 1H | 0 | €9.731,13 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | 8 | €9.729,73 | €1.679,75 | €5.039,26 | €53,74 | €80,96 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 0 | €9.723,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Score 6 75 V1 | 7 | €9.690,83 | €1.656,27 | €4.968,80 | €52,64 | €80,21 |
| TEST | Eth Donchian 1H | 1 | €9.682,56 | €1.264,47 | €3.793,40 | €48,56 | €-26,27 |
| TEST | Scanner Top5 Btc Guard V1 | 6 | €9.681,65 | €1.024,75 | €2.049,50 | €193,65 | €-0,90 |
| TEST | Global Confluence puro 1H | 1 | €9.675,64 | €1.011,45 | €2.022,91 | €48,24 | €29,21 |
| TEST | Eth Ema 1H | 0 | €9.667,53 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Balanced Long No Rhv V1 | 5 | €9.645,38 | €1.130,75 | €3.392,26 | €192,92 | €-0,59 |
| TEST | Scanner Top5 Btc Mfe V1 | 6 | €9.616,52 | €1.032,07 | €2.064,15 | €192,55 | €0,00 |
| TEST | 1H Fast V3 No Esports V1 | 6 | €9.597,96 | €1.065,02 | €3.195,07 | €191,67 | €45,47 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 0 | €9.579,83 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Runner25 V1 | 6 | €9.560,03 | €1.480,80 | €2.961,61 | €191,41 | €-9,65 |
| TEST | Master Adaptive Gb20 Be V1 | 5 | €9.519,42 | €884,48 | €1.768,97 | €145,28 | €0,57 |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | 5 | €9.517,12 | €989,64 | €2.968,93 | €142,46 | €40,19 |
| TEST | Combo Adaptive Quality7 V1 | 4 | €9.512,30 | €1.438,51 | €2.877,02 | €190,29 | €0,00 |
| TEST | Master Adaptive Gb20 Partial V1 | 5 | €9.509,29 | €883,54 | €1.767,09 | €145,13 | €0,57 |
| TEST | Combo Adaptive Regime V1 | 1 | €9.495,26 | €987,06 | €1.974,12 | €49,09 | €0,00 |
| TEST | Master Adaptive V1 | 5 | €9.472,51 | €880,13 | €1.760,25 | €144,57 | €0,57 |
| TEST | Scanner Top5 Btc Guard Mfe V1 | 6 | €9.456,50 | €1.000,92 | €2.001,84 | €189,15 | €-0,88 |
| TEST | Btc Ema 1H | 1 | €9.451,09 | €1.091,81 | €3.275,44 | €47,17 | €19,67 |
| TEST | Bilanciata 1H V3 Filtered | 6 | €9.403,89 | €1.441,51 | €4.324,53 | €188,07 | €0,40 |
| TEST | Master Adaptive Expanded V1 | 4 | €9.369,67 | €1.563,30 | €3.126,60 | €186,75 | €0,00 |
| TEST | Master Adaptive Gb20 V1 | 5 | €9.347,51 | €868,43 | €1.736,86 | €142,66 | €0,55 |
| TEST | Bilanciata 1H V2 | 5 | €9.328,74 | €1.729,35 | €5.188,06 | €140,54 | €18,57 |
| TEST | Scanner Bottom10 Short | 4 | €9.320,74 | €1.261,36 | €2.522,73 | €140,86 | €0,00 |
| TEST | Scanner Bottom15 Short | 4 | €9.320,74 | €1.261,36 | €2.522,73 | €140,86 | €0,00 |
| TEST | Scanner Bottom20 Short | 4 | €9.320,74 | €1.261,36 | €2.522,73 | €140,86 | €0,00 |
| TEST | Master Adaptive Gb20 Loss Cap V1 | 8 | €9.303,70 | €1.496,37 | €2.992,74 | €186,13 | €-0,99 |
| TEST | Master Adaptive No Alt V1 | 6 | €9.262,21 | €1.905,74 | €3.811,49 | €185,38 | €21,56 |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | 4 | €9.256,15 | €1.252,64 | €2.505,29 | €139,88 | €0,00 |
| TEST | Scanner Bottom5 Short Profit Lock V1 | 4 | €9.242,07 | €1.250,74 | €2.501,48 | €139,67 | €0,00 |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | 1 | €9.214,28 | €205,67 | €617,01 | €48,38 | €0,00 |
| TEST | Benchmark trend following EMA 1H | 5 | €9.187,13 | €981,82 | €1.963,65 | €144,18 | €0,00 |
| TEST | Scanner Bottom 5 Short 1H | 4 | €9.170,95 | €1.241,11 | €2.482,23 | €138,60 | €0,00 |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | 6 | €9.165,73 | €1.156,30 | €2.312,61 | €183,70 | €-18,39 |
| TEST | Bilanciata 1H V1 | 3 | €9.134,04 | €400,34 | €1.201,03 | €48,28 | €1,29 |
| TEST | Combo Adaptive Runner25 V1 | 6 | €9.108,71 | €1.425,33 | €2.850,66 | €138,26 | €1,89 |
| TEST | Combo Trend | 5 | €9.075,62 | €1.983,96 | €3.967,91 | €94,84 | €0,00 |
| TEST | Combo Adaptive Mfe Trail | 7 | €9.031,62 | €1.128,66 | €2.257,33 | €146,39 | €0,64 |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | 2 | €8.987,49 | €909,26 | €1.818,52 | €47,26 | €0,00 |
| TEST | Master Adaptive Strict3 V1 | 6 | €8.948,64 | €1.098,44 | €2.196,88 | €178,97 | €0,00 |
| TEST | Combo Adaptive Tp3 V1 | 6 | €8.938,30 | €1.398,70 | €2.797,39 | €135,68 | €1,86 |
| TEST | 1H Balanced V3 Long Only V1 | 6 | €8.894,36 | €1.363,40 | €4.090,20 | €177,88 | €0,37 |
| TEST | 1H Fast V3 Cap75 V1 | 5 | €8.888,34 | €1.854,83 | €5.564,49 | €89,66 | €39,18 |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | 4 | €8.809,27 | €1.835,06 | €3.670,12 | €176,55 | €-17,61 |
| TEST | Scanner Top5 Btc Btc Le3 V1 | 5 | €8.601,57 | €2.003,16 | €4.006,32 | €172,22 | €-8,72 |
| TEST | Combo Mean Reversion | 1 | €8.581,38 | €942,00 | €1.883,99 | €44,59 | €0,00 |
| TEST | Forza relativa 1H V1 | 6 | €8.494,35 | €2.133,95 | €4.267,89 | €128,10 | €39,23 |
| TEST | Benchmark Bollinger mean reversion 1H | 3 | €8.380,83 | €2.456,72 | €4.913,44 | €125,78 | €-17,78 |

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
| PRINCIPALE | Principale 4H | Confluenza trend | €9.816,14 | €-182,77 | 60 | 60 | 41,67% | 0,88 | €-3,05 | 6,86% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €11.400,31 | €1.357,64 | 144 | 144 | 43,75% | 1,42 | €9,43 | 6,75% |
| TEST | Donchian 1H Gb20 120R V1 | Donchian breakout 20 barre | €11.131,90 | €1.090,24 | 112 | 112 | 41,96% | 1,47 | €9,73 | 6,75% |
| TEST | Main Side Regime Guard V1 | Confluenza trend | €11.115,61 | €1.123,15 | 53 | 53 | 60,38% | 2,36 | €21,19 | 3,82% |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | Momentum / breakout | €11.043,61 | €1.018,41 | 201 | 201 | 49,25% | 1,25 | €5,07 | 7,95% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.942,98 | €944,40 | 178 | 178 | 46,63% | 1,30 | €5,31 | 8,85% |
| TEST | Combo Trend Side Regime Guard V1 | Combo Trend | €10.790,32 | €792,30 | 155 | 155 | 50,32% | 1,27 | €5,11 | 10,10% |
| TEST | Combo Adaptive Long Only V1 | Combo Adaptive | €10.772,68 | €517,76 | 169 | 169 | 46,15% | 1,17 | €3,06 | 7,78% |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | Momentum / breakout V3 Filtered | €10.586,75 | €516,57 | 143 | 143 | 46,85% | 1,17 | €3,61 | 5,29% |
| TEST | 1H Fast No Pepe V1 | Momentum / breakout | €10.571,30 | €571,68 | 275 | 275 | 44,00% | 1,12 | €2,08 | 9,28% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €10.464,00 | €465,15 | 84 | 75 | 47,62% | 1,22 | €5,54 | 3,89% |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | Momentum / breakout V3 Filtered | €10.444,81 | €398,88 | 217 | 217 | 49,31% | 1,11 | €1,84 | 9,50% |
| TEST | Rapida 1H V3 Filtered | Momentum / breakout V3 Filtered | €10.377,70 | €332,07 | 261 | 261 | 44,44% | 1,07 | €1,27 | 9,48% |
| TEST | Main Dynamic Asset Selector V1 | Confluenza trend | €10.369,72 | €345,60 | 21 | 21 | 42,86% | 1,62 | €16,46 | 3,39% |
| TEST | Combo Adaptive | Combo Adaptive | €10.362,62 | €363,92 | 210 | 210 | 46,19% | 1,11 | €1,73 | 8,17% |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | Momentum / breakout V3 Filtered | €10.348,30 | €360,47 | 149 | 149 | 48,32% | 1,15 | €2,42 | 5,24% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | Momentum / breakout V3 Filtered | €10.300,05 | €300,05 | 33 | 33 | 48,48% | 2,04 | €9,09 | 2,01% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | Momentum / breakout V3 Filtered | €10.271,73 | €271,73 | 22 | 22 | 50,00% | 1,74 | €12,35 | 1,72% |
| TEST | Combo Scanner | Combo Scanner | €10.269,01 | €270,98 | 188 | 188 | 43,62% | 1,08 | €1,44 | 11,38% |
| TEST | Scanner Top15 Long | Scanner Top15 Long | €10.260,66 | €265,01 | 202 | 202 | 47,03% | 1,08 | €1,31 | 10,31% |
| TEST | Scanner Top20 Long | Scanner Top20 Long | €10.260,66 | €265,01 | 202 | 202 | 47,03% | 1,08 | €1,31 | 10,31% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €10.258,16 | €259,52 | 156 | 156 | 44,87% | 1,09 | €1,66 | 11,27% |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | Momentum / breakout V3 Filtered | €10.239,20 | €239,20 | 17 | 17 | 52,94% | 4,50 | €14,07 | 1,01% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | Momentum / breakout V3 Filtered | €10.235,18 | €235,18 | 20 | 20 | 50,00% | 1,90 | €11,76 | 2,73% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €10.223,65 | €236,75 | 20 | 20 | 55,00% | 1,65 | €11,84 | 2,77% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.209,20 | €209,20 | 6 | 6 | 83,33% | 4,66 | €34,87 | 0,85% |
| TEST | Scanner Top10 Long | Scanner Top10 Long | €10.197,67 | €200,80 | 183 | 183 | 46,99% | 1,07 | €1,10 | 10,31% |
| TEST | Ampia 4H | Confluenza trend | €10.194,67 | €194,83 | 55 | 55 | 34,55% | 1,15 | €3,54 | 4,45% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | Momentum / breakout V3 Filtered | €10.185,37 | €185,37 | 22 | 22 | 40,91% | 1,57 | €8,43 | 2,27% |
| TEST | 1H Fast Score 6 75 Range Only V1 | Momentum / breakout | €10.172,36 | €170,67 | 61 | 61 | 42,62% | 1,12 | €2,80 | 6,49% |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | Momentum / breakout V3 Filtered | €10.145,12 | €145,12 | 44 | 44 | 45,45% | 1,20 | €3,30 | 2,91% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €10.138,72 | €138,72 | 10 | 10 | 50,00% | 1,64 | €13,87 | 1,37% |
| TEST | 1H Fast V3 Nohigh Range Only V1 | Momentum / breakout V3 Filtered | €10.135,95 | €95,16 | 95 | 95 | 43,16% | 1,04 | €1,00 | 7,07% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €10.115,63 | €144,72 | 7 | 7 | 42,86% | 1,87 | €20,67 | 1,61% |
| TEST | Scanner Top5 Btc Tp3 V1 | Scanner Top 5 + forza BTC | €10.108,68 | €120,61 | 154 | 154 | 42,86% | 1,04 | €0,78 | 11,78% |
| TEST | Scanner Top5 Btc Runner25 V1 | Scanner Top 5 + forza BTC | €10.102,76 | €114,69 | 158 | 158 | 43,04% | 1,04 | €0,73 | 12,06% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.101,88 | €101,88 | 4 | 4 | 75,00% | 2,86 | €25,47 | 0,91% |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | Momentum / breakout V3 Filtered | €10.099,04 | €99,04 | 55 | 55 | 54,55% | 1,12 | €1,80 | 3,59% |
| TEST | 1H Fast V3 No Esports Long Only V1 | Momentum / breakout V3 Filtered | €10.085,04 | €113,05 | 252 | 252 | 42,86% | 1,02 | €0,45 | 10,60% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €10.073,14 | €66,52 | 17 | 17 | 58,82% | 1,16 | €3,91 | 3,08% |
| TEST | Combo Adaptive Partial 1R V1 | Combo Adaptive | €10.049,05 | €51,39 | 178 | 178 | 44,38% | 1,02 | €0,29 | 8,69% |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | Momentum / breakout V3 Filtered | €10.048,77 | €48,77 | 23 | 23 | 43,48% | 1,12 | €2,12 | 3,05% |
| TEST | 1H Fast Tp2 V1 | Momentum / breakout | €10.045,91 | €45,01 | 277 | 277 | 39,35% | 1,01 | €0,16 | 6,56% |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | Momentum / breakout V3 Filtered | €10.044,18 | €44,83 | 175 | 175 | 44,00% | 1,01 | €0,26 | 6,64% |
| TEST | Rapida 1H V1 | Momentum / breakout | €10.043,28 | €43,28 | 78 | 78 | 34,62% | 1,02 | €0,55 | 6,76% |
| TEST | 1H Balanced Short Trend Down Strict V1 | Confluenza trend | €10.035,46 | €35,46 | 13 | 13 | 38,46% | 1,13 | €2,73 | 1,80% |
| TEST | Scalp RSI Long 20 · prudente · 5x | Inversione RSI estrema 15m | €10.032,32 | €32,32 | 11 | 11 | 54,55% | 1,85 | €2,94 | 0,36% |
| TEST | Scalp RSI Short 85 · €50 · 15x | Inversione RSI estrema 15m | €10.022,70 | €22,70 | 6 | 6 | 66,67% | 1,87 | €3,78 | 0,31% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €10.014,08 | €14,08 | 30 | 30 | 43,33% | 1,10 | €0,47 | 0,33% |
| TEST | Scalp RSI Short 80 · €50 · 15x | Inversione RSI estrema 15m | €10.009,44 | €9,44 | 17 | 17 | 41,18% | 1,17 | €0,56 | 0,53% |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | Momentum / breakout V3 Filtered | €10.008,92 | €8,92 | 30 | 30 | 36,67% | 1,02 | €0,30 | 4,84% |
| TEST | Doge Ema 1H | Trend following EMA | €10.008,16 | €-10,54 | 26 | 26 | 57,69% | 0,98 | €-0,41 | 2,77% |
| TEST | Sol Ema 4H | Trend following EMA | €10.005,51 | €5,51 | 11 | 11 | 36,36% | 1,02 | €0,50 | 2,27% |
| TEST | Scalp RSI Short 85 · €10 · 15x | Inversione RSI estrema 15m | €10.004,54 | €4,54 | 6 | 6 | 66,67% | 1,87 | €0,76 | 0,06% |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | Momentum / breakout V3 Filtered | €10.003,37 | €3,37 | 8 | 8 | 37,50% | 1,02 | €0,42 | 2,15% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €10.002,82 | €2,82 | 30 | 30 | 43,33% | 1,10 | €0,09 | 0,07% |
| TEST | Scalp RSI Short 80 · €10 · 15x | Inversione RSI estrema 15m | €10.001,89 | €1,89 | 17 | 17 | 41,18% | 1,17 | €0,11 | 0,11% |
| TEST | Scanner Bottom5 Short Continuation V1 | Scanner Bottom5 Short Continuation | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 20 · €10 · 15x | Inversione RSI estrema 15m | €9.998,68 | €-1,32 | 11 | 11 | 36,36% | 0,74 | €-0,12 | 0,04% |
| TEST | Scalp RSI Short 85 · prudente · 5x | Inversione RSI estrema 15m | €9.996,83 | €-3,17 | 6 | 6 | 66,67% | 0,86 | €-0,53 | 0,30% |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | Momentum / breakout V3 Filtered | €9.995,23 | €-4,77 | 15 | 15 | 46,67% | 0,99 | €-0,32 | 2,70% |
| TEST | Scalp RSI Long 15 · €10 · 15x | Inversione RSI estrema 15m | €9.994,07 | €-5,93 | 4 | 4 | 25,00% | 0,06 | €-1,48 | 0,06% |
| TEST | Scalp RSI Long 20 · €50 · 15x | Inversione RSI estrema 15m | €9.993,42 | €-6,58 | 11 | 11 | 36,36% | 0,74 | €-0,60 | 0,21% |
| TEST | Scalp RSI Long 25 · €10 · 15x | Inversione RSI estrema 15m | €9.988,90 | €-11,10 | 19 | 19 | 36,84% | 0,37 | €-0,58 | 0,15% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €9.980,98 | €-19,02 | 5 | 5 | 40,00% | 0,88 | €-3,80 | 1,96% |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | €9.970,37 | €-29,63 | 4 | 4 | 25,00% | 0,06 | €-7,41 | 0,30% |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | €9.970,34 | €-29,66 | 4 | 4 | 25,00% | 0,13 | €-7,42 | 0,30% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €9.966,58 | €-33,42 | 19 | 19 | 36,84% | 0,66 | €-1,76 | 0,71% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €9.964,84 | €-35,16 | 4 | 4 | 25,00% | 0,77 | €-8,79 | 1,10% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €9.952,59 | €-20,58 | 15 | 15 | 60,00% | 0,94 | €-1,37 | 1,89% |
| TEST | Sol Ema 1H | Trend following EMA | €9.951,35 | €-37,32 | 25 | 25 | 40,00% | 0,95 | €-1,49 | 3,33% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €9.948,32 | €-46,13 | 25 | 25 | 44,00% | 0,94 | €-1,85 | 4,59% |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | €9.944,51 | €-55,49 | 19 | 19 | 36,84% | 0,37 | €-2,92 | 0,77% |
| TEST | Scalp RSI Short 80 · prudente · 5x | Inversione RSI estrema 15m | €9.939,55 | €-60,45 | 17 | 17 | 35,29% | 0,39 | €-3,56 | 0,89% |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | Combo Adaptive | €9.935,18 | €-64,82 | 58 | 58 | 50,00% | 0,95 | €-1,12 | 4,27% |
| TEST | Combo Adaptive Side Regime Guard V1 | Combo Adaptive | €9.923,16 | €-106,45 | 166 | 166 | 42,77% | 0,97 | €-0,64 | 11,68% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.917,05 | €-82,95 | 30 | 30 | 43,33% | 0,52 | €-2,77 | 0,84% |
| TEST | Btc Ema 4H | Trend following EMA | €9.914,14 | €-85,86 | 5 | 5 | 20,00% | 0,58 | €-17,17 | 1,76% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €9.912,40 | €-77,12 | 13 | 13 | 46,15% | 0,77 | €-5,93 | 1,98% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €9.905,18 | €-85,51 | 10 | 10 | 40,00% | 0,69 | €-8,55 | 1,94% |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | Momentum / breakout V3 Filtered | €9.888,15 | €-111,22 | 174 | 174 | 46,55% | 0,97 | €-0,64 | 8,44% |
| TEST | Eth Ema 4H | Trend following EMA | €9.870,92 | €-112,70 | 7 | 7 | 28,57% | 0,57 | €-16,10 | 1,83% |
| TEST | 1H Fast V3 Nohigh V1 | Momentum / breakout V3 Filtered | €9.863,49 | €-136,89 | 179 | 179 | 44,13% | 0,96 | €-0,76 | 7,10% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €9.861,10 | €-138,90 | 6 | 6 | 16,67% | 0,49 | €-23,15 | 2,43% |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | Momentum / breakout V3 Filtered | €9.837,38 | €-162,62 | 37 | 37 | 40,54% | 0,76 | €-4,40 | 3,08% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €9.836,16 | €-162,56 | 142 | 135 | 40,14% | 0,95 | €-1,14 | 10,88% |
| TEST | 1H Fast V3 Long Only V1 | Momentum / breakout V3 Filtered | €9.820,32 | €-151,75 | 256 | 256 | 42,19% | 0,97 | €-0,59 | 12,52% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | Momentum / breakout V3 Filtered | €9.817,34 | €-182,66 | 24 | 24 | 41,67% | 0,64 | €-7,61 | 3,23% |
| TEST | Combo Adaptive Quality7 Regime V1 | Combo Adaptive | €9.810,21 | €-189,79 | 58 | 58 | 46,55% | 0,86 | €-3,27 | 5,41% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.771,60 | €-228,40 | 19 | 19 | 42,11% | 0,63 | €-12,02 | 3,14% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.765,13 | €-234,87 | 17 | 17 | 41,18% | 0,62 | €-13,82 | 2,91% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | Momentum / breakout V3 Filtered | €9.762,18 | €-237,82 | 7 | 7 | 14,29% | 0,02 | €-33,97 | 2,82% |
| TEST | 1H Fast Nohigh Cap75 V1 | Momentum / breakout | €9.760,22 | €-279,18 | 199 | 199 | 40,20% | 0,93 | €-1,40 | 10,86% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €9.731,13 | €-268,87 | 10 | 10 | 40,00% | 0,38 | €-26,89 | 4,16% |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | Momentum / breakout | €9.729,73 | €-348,20 | 162 | 162 | 43,83% | 0,92 | €-2,15 | 15,94% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | Momentum / breakout V3 Filtered | €9.723,72 | €-276,28 | 31 | 31 | 32,26% | 0,62 | €-8,91 | 4,83% |
| TEST | 1H Fast Score 6 75 V1 | Momentum / breakout | €9.690,83 | €-386,40 | 205 | 205 | 41,95% | 0,93 | €-1,88 | 15,64% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.682,56 | €-288,89 | 18 | 18 | 33,33% | 0,56 | €-16,05 | 3,74% |
| TEST | Scanner Top5 Btc Guard V1 | Scanner Top 5 + forza BTC | €9.681,65 | €-316,71 | 147 | 147 | 38,10% | 0,90 | €-2,15 | 7,34% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.675,64 | €-352,54 | 21 | 21 | 33,33% | 0,46 | €-16,79 | 3,93% |
| TEST | Eth Ema 1H | Trend following EMA | €9.667,53 | €-332,47 | 28 | 28 | 39,29% | 0,63 | €-11,87 | 4,80% |
| TEST | 1H Balanced Long No Rhv V1 | Confluenza trend | €9.645,38 | €-351,93 | 127 | 127 | 44,09% | 0,84 | €-2,77 | 9,26% |
| TEST | Scanner Top5 Btc Mfe V1 | Scanner Top 5 + forza BTC | €9.616,52 | €-382,21 | 148 | 148 | 43,92% | 0,86 | €-2,58 | 12,28% |
| TEST | 1H Fast V3 No Esports V1 | Momentum / breakout V3 Filtered | €9.597,96 | €-445,48 | 225 | 225 | 42,22% | 0,91 | €-1,98 | 10,92% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | Momentum / breakout V3 Filtered | €9.579,83 | €-420,17 | 11 | 11 | 0,00% | 0,00 | €-38,20 | 4,20% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €9.560,03 | €-429,74 | 92 | 92 | 31,52% | 0,83 | €-4,67 | 8,44% |
| TEST | Master Adaptive Gb20 Be V1 | Master Adaptive Consensus | €9.519,42 | €-481,31 | 110 | 110 | 30,91% | 0,83 | €-4,38 | 8,39% |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | Momentum / breakout | €9.517,12 | €-521,29 | 162 | 162 | 38,27% | 0,84 | €-3,22 | 10,86% |
| TEST | Combo Adaptive Quality7 V1 | Combo Adaptive | €9.512,30 | €-486,49 | 99 | 99 | 38,38% | 0,80 | €-4,91 | 8,88% |
| TEST | Master Adaptive Gb20 Partial V1 | Master Adaptive Consensus | €9.509,29 | €-491,43 | 105 | 105 | 33,33% | 0,82 | €-4,68 | 7,98% |
| TEST | Combo Adaptive Regime V1 | Combo Adaptive | €9.495,26 | €-503,55 | 88 | 88 | 45,45% | 0,77 | €-5,72 | 6,28% |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | €9.472,51 | €-528,21 | 107 | 107 | 32,71% | 0,82 | €-4,94 | 7,80% |
| TEST | Scanner Top5 Btc Guard Mfe V1 | Scanner Top 5 + forza BTC | €9.456,50 | €-541,90 | 164 | 164 | 39,02% | 0,84 | €-3,30 | 8,78% |
| TEST | Btc Ema 1H | Trend following EMA | €9.451,09 | €-566,72 | 22 | 22 | 22,73% | 0,34 | €-25,76 | 5,79% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €9.403,89 | €-594,13 | 208 | 208 | 41,35% | 0,86 | €-2,86 | 14,04% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €9.369,67 | €-629,66 | 88 | 88 | 34,09% | 0,73 | €-7,16 | 7,96% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €9.347,51 | €-653,20 | 141 | 141 | 42,55% | 0,79 | €-4,63 | 9,02% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €9.328,74 | €-686,01 | 173 | 159 | 43,35% | 0,81 | €-3,97 | 11,82% |
| TEST | Scanner Bottom10 Short | Scanner Bottom10 Short | €9.320,74 | €-677,79 | 70 | 70 | 31,43% | 0,65 | €-9,68 | 9,06% |
| TEST | Scanner Bottom15 Short | Scanner Bottom15 Short | €9.320,74 | €-677,79 | 70 | 70 | 31,43% | 0,65 | €-9,68 | 9,06% |
| TEST | Scanner Bottom20 Short | Scanner Bottom20 Short | €9.320,74 | €-677,79 | 70 | 70 | 31,43% | 0,65 | €-9,68 | 9,06% |
| TEST | Master Adaptive Gb20 Loss Cap V1 | Master Adaptive Consensus | €9.303,70 | €-695,11 | 100 | 100 | 25,00% | 0,75 | €-6,95 | 11,41% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €9.262,21 | €-757,28 | 106 | 106 | 33,02% | 0,76 | €-7,14 | 10,13% |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | Scanner Bottom 5 Short | €9.256,15 | €-742,38 | 61 | 61 | 31,15% | 0,58 | €-12,17 | 9,08% |
| TEST | Scanner Bottom5 Short Profit Lock V1 | Scanner Bottom 5 Short | €9.242,07 | €-756,47 | 62 | 62 | 30,65% | 0,56 | €-12,20 | 9,08% |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | Momentum / breakout | €9.214,28 | €-785,35 | 146 | 146 | 38,36% | 0,78 | €-5,38 | 9,99% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.187,13 | €-811,71 | 158 | 158 | 39,24% | 0,71 | €-5,14 | 12,31% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.170,95 | €-827,60 | 89 | 89 | 31,46% | 0,64 | €-9,30 | 10,17% |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | Scanner Top 5 + forza BTC | €9.165,73 | €-814,98 | 113 | 113 | 38,05% | 0,73 | €-7,21 | 11,79% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €9.134,04 | €-866,26 | 181 | 181 | 38,12% | 0,75 | €-4,79 | 15,68% |
| TEST | Combo Adaptive Runner25 V1 | Combo Adaptive | €9.108,71 | €-891,42 | 149 | 149 | 35,57% | 0,69 | €-5,98 | 14,10% |
| TEST | Combo Trend | Combo Trend | €9.075,62 | €-921,72 | 192 | 192 | 39,58% | 0,78 | €-4,80 | 14,08% |
| TEST | Combo Adaptive Mfe Trail | Combo Adaptive | €9.031,62 | €-967,69 | 225 | 225 | 40,89% | 0,75 | €-4,30 | 15,45% |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | Scanner Top 5 + forza BTC | €8.987,49 | €-1.011,42 | 54 | 54 | 25,93% | 0,42 | €-18,73 | 12,23% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €8.948,64 | €-1.050,04 | 82 | 82 | 28,05% | 0,65 | €-12,81 | 13,60% |
| TEST | Combo Adaptive Tp3 V1 | Combo Adaptive | €8.938,30 | €-1.061,82 | 129 | 129 | 34,88% | 0,59 | €-8,23 | 14,10% |
| TEST | 1H Balanced V3 Long Only V1 | Confluenza trend V3 Filtered | €8.894,36 | €-1.103,76 | 162 | 162 | 41,36% | 0,65 | €-6,81 | 13,79% |
| TEST | 1H Fast V3 Cap75 V1 | Momentum / breakout V3 Filtered | €8.888,34 | €-1.147,50 | 214 | 214 | 38,79% | 0,77 | €-5,36 | 17,41% |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | Scanner Top 5 + forza BTC | €8.809,27 | €-1.171,40 | 140 | 140 | 37,86% | 0,68 | €-8,37 | 13,91% |
| TEST | Scanner Top5 Btc Btc Le3 V1 | Scanner Top 5 + forza BTC | €8.601,57 | €-1.387,31 | 114 | 114 | 35,09% | 0,54 | €-12,17 | 16,19% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €8.581,38 | €-1.417,33 | 65 | 65 | 33,85% | 0,44 | €-21,81 | 16,00% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €8.494,35 | €-1.542,08 | 156 | 156 | 32,05% | 0,57 | €-9,89 | 19,11% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €8.380,83 | €-1.598,44 | 116 | 116 | 41,38% | 0,56 | €-13,78 | 19,96% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | SPCX | LONG | Confluenza trend | 240m | 3,0x | 136,56189 | 136,56189 | 128,79610 | 91,72407 | 152,09346 | €285,50 | €856,50 | €48,71 | €0,00 |
| Principale 4H | VELVET | LONG | Confluenza trend | 240m | 3,0x | 0,55987 | 0,55987 | 0,49269 | 0,37605 | 0,69424 | €131,08 | €393,24 | €47,19 | €0,00 |
| Principale 4H | EDEN | LONG | Confluenza trend | 240m | 3,0x | 0,06195 | 0,06195 | 0,05451 | 0,04161 | 0,07681 | €130,34 | €391,02 | €46,92 | €0,00 |
| Principale 4H | TRUMP | LONG | Confluenza trend | 240m | 3,0x | 2,46049 | 2,46049 | 2,16523 | 1,65263 | 3,05101 | €134,98 | €404,95 | €48,59 | €0,00 |
| Principale 4H | UNI | LONG | Confluenza trend | 240m | 3,0x | 6,93739 | 6,93739 | 6,33086 | 4,65961 | 8,15044 | €18,73 | €56,20 | €4,91 | €0,00 |
| Bilanciata 1H V1 | BTR | SHORT | Confluenza trend | 60m | 3,0x | 0,05109 | 0,05109 | 0,05109 | 0,06786 | 0,03883 | €125,78 | €377,33 | €0,00 | €-0,00 |
| Bilanciata 1H V1 | ARB | LONG | Confluenza trend | 60m | 3,0x | 0,13283 | 0,13283 | 0,12480 | 0,08922 | 0,14889 | €256,10 | €768,31 | €46,46 | €0,00 |
| Bilanciata 1H V1 | PEPE | SHORT | Confluenza trend | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €18,46 | €55,39 | €1,83 | €1,29 |
| 1H Balanced Long No Rhv V1 | SKHYNIX | LONG | Confluenza trend | 60m | 3,0x | 1214,11277 | 1214,11277 | 1170,18211 | 815,47908 | 1301,97411 | €413,43 | €1.240,28 | €44,88 | €0,00 |
| 1H Balanced Long No Rhv V1 | BOME | LONG | Confluenza trend | 60m | 3,0x | 0,00129 | 0,00129 | 0,00114 | 0,00087 | 0,00160 | €134,98 | €404,95 | €48,59 | €0,00 |
| 1H Balanced Long No Rhv V1 | TAO | LONG | Confluenza trend | 60m | 3,0x | 247,38947 | 247,38947 | 237,94346 | 166,16326 | 266,28148 | €428,20 | €1.284,61 | €49,05 | €0,00 |
| 1H Balanced Long No Rhv V1 | HEMI | LONG | Confluenza trend | 60m | 3,0x | 0,01177 | 0,01177 | 0,01036 | 0,00790 | 0,01459 | €131,93 | €395,78 | €47,49 | €0,00 |
| 1H Balanced Long No Rhv V1 | NEAR | LONG | Confluenza trend | 60m | 3,0x | 2,52150 | 2,49900 | 2,41155 | 1,69361 | 2,74141 | €22,21 | €66,63 | €2,91 | €-0,59 |
| Bilanciata 1H V2 | SKHYNIX | LONG | Confluenza trend V2 | 60m | 3,0x | 1214,11277 | 1214,11277 | 1170,18211 | 815,47908 | 1301,97411 | €422,38 | €1.267,15 | €45,85 | €0,00 |
| Bilanciata 1H V2 | BTR | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,05545 | 0,05545 | 0,05545 | 0,07365 | 0,04214 | €126,95 | €380,86 | €0,00 | €-0,00 |
| Bilanciata 1H V2 | ARB | LONG | Confluenza trend V2 | 60m | 3,0x | 0,13495 | 0,13495 | 0,12685 | 0,09064 | 0,15116 | €19,71 | €59,12 | €3,55 | €0,00 |
| Bilanciata 1H V2 | SOPH | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,00528 | 0,00528 | 0,00591 | 0,00701 | 0,00401 | €129,45 | €388,36 | €46,60 | €-0,00 |
| Bilanciata 1H V2 | BTC | SHORT | Confluenza trend V2 | 60m | 3,0x | 78718,15322 | 78245,50000 | 79851,69463 | 104563,94686 | 76451,07041 | €1.030,86 | €3.092,57 | €44,53 | €18,57 |
| Bilanciata 1H V3 Filtered | SKHYNIX | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1220,85412 | 1220,85412 | 1177,63561 | 820,00702 | 1307,29117 | €460,42 | €1.381,27 | €48,90 | €0,00 |
| Bilanciata 1H V3 Filtered | ADA | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,20138 | 0,20138 | 0,20719 | 0,26750 | 0,18976 | €559,88 | €1.679,63 | €48,45 | €-0,00 |
| Bilanciata 1H V3 Filtered | ARB | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,13283 | 0,13283 | 0,12480 | 0,08922 | 0,14889 | €262,61 | €787,82 | €47,64 | €0,00 |
| Bilanciata 1H V3 Filtered | UNI | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 7,14143 | 7,14143 | 6,87560 | 4,79666 | 7,67309 | €9,58 | €28,74 | €1,07 | €0,00 |
| Bilanciata 1H V3 Filtered | SOPH | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,00528 | 0,00528 | 0,00591 | 0,00701 | 0,00401 | €109,03 | €327,10 | €39,25 | €-0,00 |
| Bilanciata 1H V3 Filtered | DOGE | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,08578 | 0,08550 | 0,08776 | 0,11395 | 0,08182 | €39,99 | €119,96 | €2,77 | €0,40 |
| 1H Fast Score 6 75 V1 | BTR | SHORT | Momentum / breakout | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €126,75 | €380,26 | €0,00 | €-0,00 |
| 1H Fast Score 6 75 V1 | ARB | LONG | Momentum / breakout | 60m | 3,0x | 0,13189 | 0,13189 | 0,12574 | 0,08858 | 0,14110 | €21,85 | €65,56 | €3,05 | €0,00 |
| 1H Fast Score 6 75 V1 | SOPH | SHORT | Momentum / breakout | 60m | 3,0x | 0,00528 | 0,00528 | 0,00591 | 0,00701 | 0,00433 | €134,54 | €403,62 | €48,43 | €-0,00 |
| 1H Fast Score 6 75 V1 | DOGE | SHORT | Momentum / breakout | 60m | 3,0x | 0,08681 | 0,08550 | 0,08655 | 0,11532 | 0,08462 | €950,70 | €2.852,10 | €0,00 | €43,12 |
| 1H Fast Score 6 75 V1 | DASH | SHORT | Momentum / breakout | 60m | 3,0x | 59,29814 | 57,46000 | 58,91237 | 78,76769 | 55,77892 | €401,93 | €1.205,79 | €0,00 | €37,38 |
| 1H Fast Score 6 75 V1 | SOL | SHORT | Momentum / breakout | 60m | 3,0x | 101,36072 | 101,65600 | 102,67497 | 134,64083 | 99,38936 | €8,89 | €26,67 | €0,35 | €-0,08 |
| 1H Fast Score 6 75 V1 | SUI | SHORT | Momentum / breakout | 60m | 3,0x | 0,76095 | 0,76570 | 0,77858 | 1,01079 | 0,73449 | €11,60 | €34,80 | €0,81 | €-0,22 |
| 1H Fast Score 6 75 No Trend Up V1 | BTR | SHORT | Momentum / breakout | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €123,38 | €370,15 | €0,00 | €-0,00 |
| 1H Fast Score 6 75 No Trend Up V1 | ARB | LONG | Momentum / breakout | 60m | 3,0x | 0,13189 | 0,13189 | 0,12574 | 0,08858 | 0,14110 | €21,27 | €63,82 | €2,97 | €0,00 |
| 1H Fast Score 6 75 No Trend Up V1 | SOPH | SHORT | Momentum / breakout | 60m | 3,0x | 0,00528 | 0,00528 | 0,00591 | 0,00701 | 0,00433 | €134,17 | €402,52 | €48,30 | €-0,00 |
| 1H Fast Score 6 75 No Trend Up V1 | DOGE | SHORT | Momentum / breakout | 60m | 3,0x | 0,08681 | 0,08550 | 0,08655 | 0,11532 | 0,08462 | €954,48 | €2.863,44 | €0,00 | €43,30 |
| 1H Fast Score 6 75 No Trend Up V1 | DASH | SHORT | Momentum / breakout | 60m | 3,0x | 59,29814 | 57,46000 | 58,91237 | 78,76769 | 55,77892 | €407,89 | €1.223,67 | €0,00 | €37,93 |
| 1H Fast Score 6 75 No Trend Up V1 | PEPE | SHORT | Momentum / breakout | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €17,32 | €51,96 | €1,27 | €0,03 |
| 1H Fast Score 6 75 No Trend Up V1 | SOL | SHORT | Momentum / breakout | 60m | 3,0x | 101,36072 | 101,65600 | 102,67497 | 134,64083 | 99,38936 | €9,39 | €28,16 | €0,37 | €-0,08 |
| 1H Fast Score 6 75 No Trend Up V1 | SUI | SHORT | Momentum / breakout | 60m | 3,0x | 0,76095 | 0,76570 | 0,77858 | 1,01079 | 0,73449 | €11,85 | €35,54 | €0,82 | €-0,22 |
| 1H Fast Score 6 75 Range Only V1 | ADA | SHORT | Momentum / breakout | 60m | 3,0x | 0,20260 | 0,20260 | 0,20707 | 0,26912 | 0,19589 | €765,21 | €2.295,64 | €50,71 | €-0,00 |
| 1H Fast Score 6 75 Range Only V1 | HEMI | LONG | Momentum / breakout | 60m | 3,0x | 0,01177 | 0,01177 | 0,01065 | 0,00790 | 0,01345 | €178,53 | €535,59 | €51,05 | €0,00 |
| 1H Fast Score 6 75 Range Only V1 | BTR | SHORT | Momentum / breakout | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €131,87 | €395,61 | €0,00 | €-0,00 |
| 1H Fast Score 6 75 Range Only V1 | SOPH | SHORT | Momentum / breakout | 60m | 3,0x | 0,00528 | 0,00528 | 0,00591 | 0,00701 | 0,00433 | €138,52 | €415,55 | €49,87 | €-0,00 |
| 1H Fast Score 6 75 Range Only V1 | DOGE | SHORT | Momentum / breakout | 60m | 3,0x | 0,08681 | 0,08550 | 0,08655 | 0,11532 | 0,08462 | €84,44 | €253,33 | €0,00 | €3,83 |
| 1H Fast Score 6 75 Cost Aware V1 | BTW | LONG | Momentum / breakout | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €8,91 | €26,72 | €3,13 | €0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00086 | 0,00146 | €215,92 | €647,76 | €57,03 | €0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | NEAR | LONG | Momentum / breakout | 60m | 3,0x | 2,08142 | 2,49900 | 2,02315 | 1,39802 | 2,16882 | €42,86 | €128,59 | €3,60 | €25,80 |
| 1H Fast Score 6 75 Cost Aware V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €157,13 | €471,39 | €56,57 | €-0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | BTR | SHORT | Momentum / breakout | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €150,22 | €450,66 | €0,00 | €-0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | SOPH | SHORT | Momentum / breakout | 60m | 3,0x | 0,00528 | 0,00528 | 0,00591 | 0,00701 | 0,00433 | €126,49 | €379,47 | €45,54 | €-0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | DOGE | SHORT | Momentum / breakout | 60m | 3,0x | 0,08681 | 0,08550 | 0,08655 | 0,11532 | 0,08462 | €18,12 | €54,35 | €0,00 | €0,82 |
| 1H Fast Nohigh Cap75 V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €139,29 | €417,86 | €50,14 | €-0,00 |
| 1H Fast Nohigh Cap75 V1 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €141,57 | €424,71 | €50,14 | €-0,00 |
| 1H Fast Nohigh Cap75 V1 | BTR | SHORT | Momentum / breakout | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €135,62 | €406,85 | €0,00 | €-0,00 |
| 1H Fast Nohigh Cap75 V1 | PEPE | SHORT | Momentum / breakout | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €588,23 | €1.764,70 | €45,30 | €40,95 |
| 1H Fast Nohigh Cap75 V1 | DOGE | SHORT | Momentum / breakout | 60m | 3,0x | 0,08625 | 0,08550 | 0,08771 | 0,11457 | 0,08407 | €10,25 | €30,75 | €0,52 | €0,27 |
| 1H Fast Long Btc 1 3 Cap75 V1 | PROM | LONG | Momentum / breakout | 60m | 3,0x | 6,93686 | 6,93686 | 6,39299 | 4,65926 | 7,75266 | €205,67 | €617,01 | €48,38 | €0,00 |
| 1H Fast No Pepe V1 | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €172,22 | €516,67 | €49,86 | €0,00 |
| 1H Fast No Pepe V1 | TAO | LONG | Momentum / breakout | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €47,93 | €143,78 | €4,27 | €0,00 |
| 1H Fast No Pepe V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €136,27 | €408,80 | €49,06 | €-0,00 |
| 1H Fast No Pepe V1 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €9,48 | €28,43 | €3,41 | €-0,00 |
| 1H Fast No Pepe V1 | ADA | SHORT | Momentum / breakout | 60m | 3,0x | 0,20138 | 0,20138 | 0,20590 | 0,26750 | 0,19460 | €739,08 | €2.217,23 | €49,74 | €-0,00 |
| 1H Fast No Pepe V1 | 0G | LONG | Momentum / breakout | 60m | 3,0x | 0,23904 | 0,23904 | 0,21901 | 0,16056 | 0,26909 | €210,41 | €631,23 | €52,89 | €0,00 |
| 1H Fast No Pepe V1 | DOGE | SHORT | Momentum / breakout | 60m | 3,0x | 0,08675 | 0,08550 | 0,08654 | 0,11524 | 0,08458 | €43,24 | €129,72 | €0,00 | €1,87 |
| 1H Fast Tp2 V1 | BTW | LONG | Momentum / breakout | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,56752 | €142,85 | €428,56 | €50,25 | €0,00 |
| 1H Fast Tp2 V1 | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00132 | 0,00132 | 0,00119 | 0,00088 | 0,00158 | €18,87 | €56,62 | €5,59 | €0,00 |
| 1H Fast Tp2 V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,17246 | 0,17246 | 0,17246 | 0,22908 | 0,13107 | €139,71 | €419,14 | €0,00 | €-0,00 |
| 1H Fast Tp2 V1 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03379 | €141,13 | €423,40 | €50,81 | €-0,00 |
| 1H Fast Tp2 V1 | 4 | LONG | Momentum / breakout | 60m | 3,0x | 0,03351 | 0,03351 | 0,03024 | 0,02251 | 0,04003 | €142,67 | €428,01 | €41,68 | €0,00 |
| 1H Fast Tp2 V1 | DOGE | SHORT | Momentum / breakout | 60m | 3,0x | 0,08681 | 0,08550 | 0,08655 | 0,11532 | 0,08389 | €44,70 | €134,09 | €0,00 | €2,03 |
| Rapida 1H V2 | ADA | SHORT | Momentum / breakout V2 | 60m | 3,0x | 0,20283 | 0,20283 | 0,20750 | 0,26943 | 0,19582 | €749,31 | €2.247,94 | €51,80 | €-0,00 |
| Rapida 1H V3 Filtered | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €172,00 | €515,99 | €49,79 | €0,00 |
| Rapida 1H V3 Filtered | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €589,98 | €1.769,95 | €52,56 | €0,00 |
| Rapida 1H V3 Filtered | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €140,02 | €420,06 | €50,41 | €-0,00 |
| Rapida 1H V3 Filtered | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €16,99 | €50,96 | €6,11 | €-0,00 |
| Rapida 1H V3 Filtered | PEPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €633,48 | €1.900,43 | €47,75 | €48,24 |
| Rapida 1H V3 Filtered | DOGE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,08625 | 0,08550 | 0,08771 | 0,11457 | 0,08407 | €12,26 | €36,78 | €0,62 | €0,32 |
| 1H Fast V3 Cap75 V1 | BTR | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €122,50 | €367,49 | €0,00 | €-0,00 |
| 1H Fast V3 Cap75 V1 | SOPH | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00528 | 0,00528 | 0,00591 | 0,00701 | 0,00433 | €123,86 | €371,59 | €44,59 | €-0,00 |
| 1H Fast V3 Cap75 V1 | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,21686 | 0,21686 | 0,22128 | 0,28806 | 0,21022 | €726,90 | €2.180,71 | €44,50 | €-0,00 |
| 1H Fast V3 Cap75 V1 | DOGE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,08681 | 0,08550 | 0,08655 | 0,11532 | 0,08462 | €866,91 | €2.600,73 | €0,00 | €39,32 |
| 1H Fast V3 Cap75 V1 | SOL | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 101,32873 | 101,65600 | 102,65513 | 134,59833 | 99,33913 | €14,66 | €43,97 | €0,58 | €-0,14 |
| 1H Fast V3 Nohigh V1 | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €131,05 | €393,14 | €47,18 | €-0,00 |
| 1H Fast V3 Nohigh V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €133,20 | €399,59 | €47,18 | €-0,00 |
| 1H Fast V3 Nohigh V1 | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,20138 | 0,20138 | 0,20590 | 0,26750 | 0,19460 | €719,57 | €2.158,72 | €48,43 | €-0,00 |
| 1H Fast V3 Nohigh V1 | 0G | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,23904 | 0,23904 | 0,21901 | 0,16056 | 0,26909 | €196,32 | €588,95 | €49,35 | €0,00 |
| 1H Fast V3 Nohigh V1 | DOGE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,08675 | 0,08550 | 0,08654 | 0,11524 | 0,08458 | €64,47 | €193,40 | €0,00 | €2,79 |
| 1H Fast V3 Nohigh V1 | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 78081,18064 | 78245,50000 | 78955,68986 | 103717,83495 | 76769,41681 | €56,87 | €170,61 | €1,91 | €-0,36 |
| 1H Fast V3 Long Only V1 | BTW | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €126,57 | €379,72 | €44,52 | €0,00 |
| 1H Fast V3 Long Only V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00147 | €9,56 | €28,69 | €2,66 | €0,00 |
| 1H Fast V3 Long Only V1 | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €554,42 | €1.663,26 | €49,39 | €0,00 |
| 1H Fast V3 Long Only V1 | HEMI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01177 | 0,01177 | 0,01065 | 0,00790 | 0,01345 | €170,60 | €511,79 | €48,79 | €0,00 |
| 1H Fast V3 Long Only V1 | NEAR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,54251 | 2,49900 | 2,45844 | 1,70772 | 2,66862 | €496,31 | €1.488,93 | €49,23 | €-25,48 |
| 1H Fast V3 Long Nohigh Cap75 V1 | HEMI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01177 | 0,01177 | 0,01065 | 0,00790 | 0,01345 | €166,97 | €500,92 | €47,75 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 V1 | PROM | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 6,92735 | 6,92735 | 6,35093 | 4,65287 | 7,79198 | €195,87 | €587,60 | €48,89 | €0,00 |
| 1H Fast V3 No Esports V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €169,36 | €508,09 | €49,03 | €0,00 |
| 1H Fast V3 No Esports V1 | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €27,04 | €81,13 | €2,41 | €0,00 |
| 1H Fast V3 No Esports V1 | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €133,96 | €401,88 | €48,23 | €-0,00 |
| 1H Fast V3 No Esports V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €129,73 | €389,20 | €46,70 | €-0,00 |
| 1H Fast V3 No Esports V1 | PEPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €593,05 | €1.779,15 | €44,70 | €45,16 |
| 1H Fast V3 No Esports V1 | DOGE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,08625 | 0,08550 | 0,08771 | 0,11457 | 0,08407 | €11,88 | €35,63 | €0,60 | €0,31 |
| 1H Fast V3 No Esports Long Only V1 | BTW | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €132,94 | €398,81 | €46,76 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00147 | €10,06 | €30,18 | €2,80 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | HEMI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01177 | 0,01177 | 0,01065 | 0,00790 | 0,01345 | €175,30 | €525,91 | €50,13 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | PROM | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 6,92735 | 6,92735 | 6,35093 | 4,65287 | 7,79198 | €9,71 | €29,12 | €2,42 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | 0G | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,23904 | 0,23904 | 0,21901 | 0,16056 | 0,26909 | €187,89 | €563,68 | €47,23 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | NEAR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,54251 | 2,49900 | 2,45844 | 1,70772 | 2,66862 | €509,69 | €1.529,07 | €50,56 | €-26,17 |
| 1H Fast V3 No Esports Mfe Lock V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €173,11 | €519,32 | €50,11 | €0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €593,79 | €1.781,38 | €52,90 | €0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €140,93 | €422,78 | €50,73 | €-0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €17,09 | €51,28 | €6,15 | €-0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | PEPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €637,57 | €1.912,72 | €48,06 | €48,55 |
| 1H Fast V3 No Esports Mfe Lock V1 | DOGE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,08625 | 0,08550 | 0,08771 | 0,11457 | 0,08407 | €12,34 | €37,02 | €0,62 | €0,32 |
| 1H Fast V3 No Esports Stress Guard V1 | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,20283 | 0,20283 | 0,20750 | 0,26943 | 0,19582 | €739,04 | €2.217,11 | €51,09 | €-0,00 |
| 1H Fast V3 No Esports Stress Guard V1 | DOGE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,08675 | 0,08550 | 0,08654 | 0,11524 | 0,08458 | €1.052,02 | €3.156,06 | €0,00 | €45,57 |
| 1H Fast V3 No Esports Stress Guard V1 | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 78081,18064 | 78245,50000 | 78955,68986 | 103717,83495 | 76769,41681 | €1.569,67 | €4.709,01 | €52,74 | €-9,91 |
| 1H Fast V3 No Esports Stress Guard V1 | DASH | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 59,29814 | 57,46000 | 58,91237 | 78,76769 | 55,77892 | €444,18 | €1.332,54 | €0,00 | €41,31 |
| 1H Fast V3 No Esports Stress Guard V1 | PEPE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €22,26 | €66,77 | €1,64 | €0,04 |
| 1H Fast V3 No Esports Stress Guard V1 | SUI | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,76095 | 0,76570 | 0,77858 | 1,01079 | 0,73449 | €20,61 | €61,84 | €1,43 | €-0,39 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | HEMI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01177 | 0,01177 | 0,01065 | 0,00790 | 0,01345 | €163,25 | €489,75 | €46,69 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | PROM | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 6,92735 | 6,92735 | 6,35093 | 4,65287 | 7,79198 | €191,37 | €574,11 | €47,77 | €0,00 |
| Ampia 4H | SPCX | LONG | Confluenza trend | 240m | 2,0x | 136,56189 | 136,56189 | 126,46637 | 68,96375 | 164,82935 | €323,86 | €647,73 | €47,88 | €0,00 |
| Ampia 4H | VELVET | LONG | Confluenza trend | 240m | 2,0x | 0,55987 | 0,55987 | 0,49269 | 0,28274 | 0,74799 | €201,63 | €403,26 | €48,39 | €0,00 |
| Ampia 4H | LINK | LONG | Confluenza trend | 240m | 2,0x | 11,96839 | 11,96839 | 11,08055 | 6,04404 | 14,45436 | €14,07 | €28,15 | €2,09 | €0,00 |
| Ampia 4H | ETH | LONG | Confluenza trend | 240m | 2,0x | 2430,03591 | 2473,30000 | 2267,54364 | 1227,16813 | 2885,01426 | €18,82 | €37,65 | €2,52 | €0,67 |
| Ampia 4H | HYPE | LONG | Confluenza trend | 240m | 2,0x | 79,31286 | 83,92600 | 70,73982 | 40,05299 | 103,31737 | €13,82 | €27,64 | €2,99 | €1,61 |
| Ampia 4H | TRUMP | LONG | Confluenza trend | 240m | 2,0x | 2,37347 | 2,37347 | 2,08866 | 1,19860 | 3,17096 | €210,83 | €421,66 | €50,60 | €0,00 |
| Ampia 4H | SOL | LONG | Confluenza trend | 240m | 2,0x | 103,77875 | 101,65600 | 96,79200 | 52,40827 | 123,34165 | €13,62 | €27,23 | €1,83 | €-0,56 |
| Ampia 4H | XRP | LONG | Confluenza trend | 240m | 2,0x | 1,42001 | 1,38526 | 1,35851 | 0,71711 | 1,59222 | €12,52 | €25,04 | €1,08 | €-0,61 |
| Ampia 4H | UNI | LONG | Confluenza trend | 240m | 2,0x | 6,98040 | 6,98040 | 6,22147 | 3,52510 | 9,10539 | €214,19 | €428,38 | €46,57 | €0,00 |
| Forza relativa 1H V1 | BTR | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,05109 | 0,05109 | 0,05109 | 0,07638 | 0,03760 | €174,72 | €349,43 | €0,00 | €-0,00 |
| Forza relativa 1H V1 | ARB | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,15050 | €352,71 | €705,43 | €42,65 | €0,00 |
| Forza relativa 1H V1 | PEPE | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00001 | 0,00000 | €661,53 | €1.323,06 | €41,35 | €33,33 |
| Forza relativa 1H V1 | UNI | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 7,16543 | 7,16543 | 6,92567 | 3,61854 | 7,69291 | €13,42 | €26,84 | €0,90 | €0,00 |
| Forza relativa 1H V1 | DOGE | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,08578 | 0,08550 | 0,08776 | 0,12825 | 0,08143 | €919,03 | €1.838,05 | €42,44 | €6,06 |
| Forza relativa 1H V1 | SUI | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,76095 | 0,76570 | 0,78362 | 1,13762 | 0,71106 | €12,54 | €25,08 | €0,75 | €-0,16 |
| Forza relativa 1H V2 | BEAT | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,25984 | 0,25984 | 0,25657 | 0,38847 | 0,19125 | €200,38 | €400,75 | €0,00 | €-0,00 |
| Forza relativa 1H V2 | TUT | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,04452 | 0,04452 | 0,04986 | 0,06656 | 0,03277 | €204,64 | €409,28 | €49,11 | €-0,00 |
| Forza relativa 1H V2 | ADA | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,20283 | 0,20283 | 0,20884 | 0,30323 | 0,18961 | €17,52 | €35,04 | €1,04 | €-0,00 |
| Forza relativa 1H V2 | HEMI | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €200,86 | €401,72 | €48,21 | €0,00 |
| Forza relativa 1H V2 | BTR | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,05109 | 0,05109 | 0,05109 | 0,07638 | 0,03760 | €205,02 | €410,03 | €0,00 | €-0,00 |
| Forza relativa 1H V2 | PEPE | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00001 | 0,00000 | €16,99 | €33,97 | €1,07 | €0,02 |
| Benchmark Donchian breakout 1H | SKHYNIX | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1174,33482 | 1174,33482 | 1128,44989 | 593,03908 | 1289,04713 | €641,25 | €1.282,50 | €50,11 | €0,00 |
| Benchmark Donchian breakout 1H | VELVET | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,14787 | 0,14787 | 0,16561 | 0,22107 | 0,10351 | €237,23 | €474,47 | €56,94 | €-0,00 |
| Benchmark Donchian breakout 1H | ADA | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,20283 | 0,20283 | 0,20951 | 0,30323 | 0,18614 | €72,87 | €145,74 | €4,80 | €-0,00 |
| Benchmark Donchian breakout 1H | PEPE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00001 | 0,00000 | €794,09 | €1.588,18 | €58,23 | €36,85 |
| Benchmark Donchian breakout 1H | BTC | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 78821,06263 | 78245,50000 | 80082,19964 | 117837,48864 | 75668,22013 | €123,54 | €247,07 | €3,95 | €1,80 |
| Benchmark Donchian breakout 1H | NEAR | LONG | Donchian breakout 20 barre | 60m | 2,0x | 2,50850 | 2,49900 | 2,39321 | 1,26679 | 2,79672 | €16,57 | €33,14 | €1,52 | €-0,13 |
| Benchmark Donchian breakout 1H | DOGE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,08578 | 0,08550 | 0,08798 | 0,12825 | 0,08028 | €1.019,54 | €2.039,09 | €52,32 | €6,72 |
| Donchian 1H Gb20 120R V1 | SKHYNIX | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1174,33482 | 1174,33482 | 1128,44989 | 593,03908 | 1289,04713 | €626,15 | €1.252,30 | €48,93 | €0,00 |
| Donchian 1H Gb20 120R V1 | VELVET | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,14787 | 0,14787 | 0,16561 | 0,22107 | 0,10351 | €231,65 | €463,30 | €55,60 | €-0,00 |
| Donchian 1H Gb20 120R V1 | ADA | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,20283 | 0,20283 | 0,20951 | 0,30323 | 0,18614 | €71,16 | €142,31 | €4,68 | €-0,00 |
| Donchian 1H Gb20 120R V1 | PEPE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00001 | 0,00000 | €775,40 | €1.550,79 | €56,86 | €35,99 |
| Donchian 1H Gb20 120R V1 | BTC | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 78821,06263 | 78245,50000 | 80082,19964 | 117837,48864 | 75668,22013 | €120,63 | €241,25 | €3,86 | €1,76 |
| Donchian 1H Gb20 120R V1 | NEAR | LONG | Donchian breakout 20 barre | 60m | 2,0x | 2,50850 | 2,49900 | 2,39321 | 1,26679 | 2,79672 | €16,18 | €32,36 | €1,49 | €-0,12 |
| Donchian 1H Gb20 120R V1 | DOGE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,08578 | 0,08550 | 0,08798 | 0,12825 | 0,08028 | €995,54 | €1.991,08 | €51,08 | €6,56 |
| Benchmark Bollinger mean reversion 1H | DOGE | LONG | Bollinger mean reversion | 60m | 2,0x | 0,08629 | 0,08550 | 0,08473 | 0,04358 | 0,08863 | €1.161,33 | €2.322,65 | €42,01 | €-21,19 |
| Benchmark Bollinger mean reversion 1H | PEPE | LONG | Bollinger mean reversion | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €797,78 | €1.595,56 | €41,94 | €-1,61 |
| Benchmark Bollinger mean reversion 1H | DASH | LONG | Bollinger mean reversion | 60m | 2,0x | 57,17143 | 57,46000 | 54,76797 | 28,87157 | 60,77663 | €497,61 | €995,23 | €41,84 | €5,02 |
| Benchmark trend following EMA 1H | BEAT | SHORT | Trend following EMA | 60m | 2,0x | 0,28257 | 0,28257 | 0,25706 | 0,42244 | 0,20797 | €186,11 | €372,23 | €0,00 | €-0,00 |
| Benchmark trend following EMA 1H | TUT | SHORT | Trend following EMA | 60m | 2,0x | 0,04446 | 0,04446 | 0,04980 | 0,06647 | 0,03272 | €194,70 | €389,39 | €46,73 | €-0,00 |
| Benchmark trend following EMA 1H | VELVET | SHORT | Trend following EMA | 60m | 2,0x | 0,14786 | 0,14786 | 0,16560 | 0,22105 | 0,10883 | €187,91 | €375,83 | €45,10 | €-0,00 |
| Benchmark trend following EMA 1H | ARB | LONG | Trend following EMA | 60m | 2,0x | 0,13283 | 0,13283 | 0,12390 | 0,06708 | 0,15246 | €341,57 | €683,14 | €45,90 | €0,00 |
| Benchmark trend following EMA 1H | UNI | LONG | Trend following EMA | 60m | 2,0x | 7,07742 | 7,07742 | 6,75804 | 3,57409 | 7,78005 | €71,53 | €143,05 | €6,46 | €0,00 |
| Scanner Top 5 Long 1H | BOME | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00160 | €218,24 | €436,47 | €52,38 | €0,00 |
| Scanner Top 5 Long 1H | TRUMP | LONG | Scanner Top 5 Long | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,08367 | €238,89 | €477,78 | €55,13 | €0,00 |
| Scanner Top 5 Long 1H | SKHYNIX | LONG | Scanner Top 5 Long | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1331,36020 | €17,74 | €35,49 | €0,91 | €0,00 |
| Scanner Top 5 Long 1H | HEMI | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €228,24 | €456,48 | €54,78 | €0,00 |
| Scanner Top 5 Long 1H | ARB | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,14889 | €453,65 | €907,29 | €54,86 | €0,00 |
| Scanner Bottom 5 Short 1H | SOXL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €378,86 | €757,72 | €48,07 | €-0,00 |
| Scanner Bottom 5 Short 1H | SNDK | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €492,80 | €985,60 | €47,71 | €-0,00 |
| Scanner Bottom 5 Short 1H | VELVET | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €191,07 | €382,14 | €0,00 | €-0,00 |
| Scanner Bottom 5 Short 1H | TUT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €178,38 | €356,76 | €42,81 | €-0,00 |
| Scanner Top10 Long | TAO | LONG | Scanner Top10 Long | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €678,43 | €1.356,86 | €51,81 | €0,00 |
| Scanner Top10 Long | SKHYNIX | LONG | Scanner Top10 Long | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €972,86 | €1.945,72 | €48,38 | €0,00 |
| Scanner Top10 Long | HEMI | LONG | Scanner Top10 Long | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €207,88 | €415,77 | €49,89 | €0,00 |
| Scanner Top10 Long | ARB | LONG | Scanner Top10 Long | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,14889 | €422,09 | €844,19 | €51,04 | €0,00 |
| Scanner Top10 Long | UNI | LONG | Scanner Top10 Long | 60m | 2,0x | 7,14143 | 7,14143 | 6,87560 | 3,60642 | 7,67309 | €15,10 | €30,20 | €1,12 | €0,00 |
| Scanner Top10 Long | NEAR | LONG | Scanner Top10 Long | 60m | 2,0x | 2,52150 | 2,49900 | 2,41155 | 1,27336 | 2,74141 | €19,59 | €39,18 | €1,71 | €-0,35 |
| Scanner Bottom10 Short | SOXL | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom10 Short | SNDK | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Bottom10 Short | VELVET | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €194,19 | €388,38 | €0,00 | €-0,00 |
| Scanner Bottom10 Short | TUT | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €181,31 | €362,61 | €43,51 | €-0,00 |
| Scanner Top15 Long | NEAR | LONG | Scanner Top15 Long | 60m | 2,0x | 2,08142 | 2,49900 | 2,00650 | 1,05112 | 2,23125 | €16,79 | €33,59 | €1,21 | €6,74 |
| Scanner Top15 Long | TAO | LONG | Scanner Top15 Long | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €88,53 | €177,07 | €6,76 | €0,00 |
| Scanner Top15 Long | TRUMP | LONG | Scanner Top15 Long | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,08367 | €215,87 | €431,75 | €49,81 | €0,00 |
| Scanner Top15 Long | SKHYNIX | LONG | Scanner Top15 Long | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €787,36 | €1.574,72 | €39,16 | €0,00 |
| Scanner Top15 Long | ARB | LONG | Scanner Top15 Long | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,14889 | €426,02 | €852,04 | €51,52 | €0,00 |
| Scanner Top15 Long | UNI | LONG | Scanner Top15 Long | 60m | 2,0x | 7,12843 | 7,12843 | 6,87194 | 3,59985 | 7,64140 | €88,01 | €176,02 | €6,33 | €0,00 |
| Scanner Top15 Long | ZEC | LONG | Scanner Top15 Long | 60m | 2,0x | 1246,65928 | 1238,83000 | 1198,94620 | 629,56294 | 1342,08543 | €661,23 | €1.322,46 | €50,61 | €-8,31 |
| Scanner Bottom15 Short | SOXL | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom15 Short | SNDK | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Bottom15 Short | VELVET | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €194,19 | €388,38 | €0,00 | €-0,00 |
| Scanner Bottom15 Short | TUT | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €181,31 | €362,61 | €43,51 | €-0,00 |
| Scanner Top20 Long | NEAR | LONG | Scanner Top20 Long | 60m | 2,0x | 2,08142 | 2,49900 | 2,00650 | 1,05112 | 2,23125 | €16,79 | €33,59 | €1,21 | €6,74 |
| Scanner Top20 Long | TAO | LONG | Scanner Top20 Long | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €88,53 | €177,07 | €6,76 | €0,00 |
| Scanner Top20 Long | TRUMP | LONG | Scanner Top20 Long | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,08367 | €215,87 | €431,75 | €49,81 | €0,00 |
| Scanner Top20 Long | SKHYNIX | LONG | Scanner Top20 Long | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €787,36 | €1.574,72 | €39,16 | €0,00 |
| Scanner Top20 Long | ARB | LONG | Scanner Top20 Long | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,14889 | €426,02 | €852,04 | €51,52 | €0,00 |
| Scanner Top20 Long | UNI | LONG | Scanner Top20 Long | 60m | 2,0x | 7,12843 | 7,12843 | 6,87194 | 3,59985 | 7,64140 | €88,01 | €176,02 | €6,33 | €0,00 |
| Scanner Top20 Long | ZEC | LONG | Scanner Top20 Long | 60m | 2,0x | 1246,65928 | 1238,83000 | 1198,94620 | 629,56294 | 1342,08543 | €661,23 | €1.322,46 | €50,61 | €-8,31 |
| Scanner Bottom20 Short | SOXL | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom20 Short | SNDK | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Bottom20 Short | VELVET | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €194,19 | €388,38 | €0,00 | €-0,00 |
| Scanner Bottom20 Short | TUT | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €181,31 | €362,61 | €43,51 | €-0,00 |
| Scanner Top 5 + forza BTC 1H | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €203,45 | €406,91 | €48,83 | €0,00 |
| Scanner Top 5 + forza BTC 1H | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,14149 | €223,03 | €446,06 | €51,47 | €0,00 |
| Scanner Top 5 + forza BTC 1H | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €18,23 | €36,45 | €0,93 | €0,00 |
| Scanner Top 5 + forza BTC 1H | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €213,35 | €426,70 | €51,20 | €0,00 |
| Scanner Top 5 + forza BTC 1H | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,15050 | €424,88 | €849,77 | €51,38 | €0,00 |
| Scanner Top 5 + forza BTC 1H | UNI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 7,09542 | 7,09542 | 6,78408 | 3,58319 | 7,78036 | €17,99 | €35,98 | €1,58 | €0,00 |
| Scanner Top5 Btc Mfe V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €190,73 | €381,46 | €45,77 | €0,00 |
| Scanner Top5 Btc Mfe V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,14149 | €209,08 | €418,16 | €48,25 | €0,00 |
| Scanner Top5 Btc Mfe V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €17,09 | €34,17 | €0,88 | €0,00 |
| Scanner Top5 Btc Mfe V1 | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €200,01 | €400,01 | €48,00 | €0,00 |
| Scanner Top5 Btc Mfe V1 | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,15050 | €398,31 | €796,61 | €48,17 | €0,00 |
| Scanner Top5 Btc Mfe V1 | UNI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 7,09542 | 7,09542 | 6,78408 | 3,58319 | 7,78036 | €16,86 | €33,73 | €1,48 | €0,00 |
| Scanner Top5 Btc Guard V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €197,27 | €394,55 | €47,35 | €0,00 |
| Scanner Top5 Btc Guard V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,55551 | 2,55551 | 2,29388 | 1,29053 | 3,13109 | €13,03 | €26,06 | €2,67 | €0,00 |
| Scanner Top5 Btc Guard V1 | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €195,03 | €390,06 | €46,81 | €0,00 |
| Scanner Top5 Btc Guard V1 | ZORA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00942 | 0,00942 | 0,00829 | 0,00476 | 0,01191 | €192,06 | €384,12 | €46,09 | €0,00 |
| Scanner Top5 Btc Guard V1 | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,15050 | €401,05 | €802,11 | €48,50 | €0,00 |
| Scanner Top5 Btc Guard V1 | NEAR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,54251 | 2,49900 | 2,43442 | 1,28397 | 2,78031 | €26,31 | €52,61 | €2,24 | €-0,90 |
| Scanner Top5 Btc Btc Le3 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €847,75 | €1.695,49 | €43,45 | €0,00 |
| Scanner Top5 Btc Btc Le3 V1 | 0G | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,24373 | 0,24373 | 0,21916 | 0,12308 | 0,29778 | €215,80 | €431,60 | €43,51 | €0,00 |
| Scanner Top5 Btc Btc Le3 V1 | UNI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 7,16543 | 7,16543 | 6,92567 | 3,61854 | 7,69291 | €17,38 | €34,75 | €1,16 | €0,00 |
| Scanner Top5 Btc Btc Le3 V1 | WLD | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,46919 | 0,46919 | 0,44675 | 0,23694 | 0,51857 | €433,72 | €867,43 | €41,49 | €0,00 |
| Scanner Top5 Btc Btc Le3 V1 | NEAR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,52150 | 2,49900 | 2,41155 | 1,27336 | 2,76340 | €488,52 | €977,04 | €42,61 | €-8,72 |
| Scanner Top5 Btc Btc 2 3 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €891,28 | €1.782,56 | €45,68 | €0,00 |
| Scanner Top5 Btc Btc 2 3 V1 | UNI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 7,09542 | 7,09542 | 6,78408 | 3,58319 | 7,78036 | €17,98 | €35,96 | €1,58 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €192,69 | €385,37 | €46,24 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,55551 | 2,55551 | 2,29388 | 1,29053 | 3,13109 | €12,72 | €25,45 | €2,61 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €190,49 | €380,99 | €45,72 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | ZORA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00942 | 0,00942 | 0,00829 | 0,00476 | 0,01191 | €187,59 | €375,19 | €45,02 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,15050 | €391,73 | €783,45 | €47,37 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | NEAR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,54251 | 2,49900 | 2,43442 | 1,28397 | 2,78031 | €25,70 | €51,40 | €2,19 | €-0,88 |
| Scanner Top5 Btc Guard Btc Le3 V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,55551 | 2,55551 | 2,29388 | 1,29053 | 3,13109 | €12,70 | €25,40 | €2,60 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01488 | €191,20 | €382,39 | €45,89 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | PROM | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 7,01991 | 7,01991 | 6,30832 | 3,54505 | 8,58541 | €213,89 | €427,78 | €43,36 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | ZORA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00942 | 0,00942 | 0,00829 | 0,00476 | 0,01191 | €188,34 | €376,68 | €45,20 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | UNI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 7,14143 | 7,14143 | 6,87560 | 3,60642 | 7,72626 | €12,97 | €25,94 | €0,97 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | NEAR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,54251 | 2,49900 | 2,43442 | 1,28397 | 2,78031 | €537,21 | €1.074,41 | €45,68 | €-18,39 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | ZORA | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00942 | 0,00942 | 0,00829 | 0,00476 | 0,01191 | €185,37 | €370,74 | €44,49 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | LINK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 13,22564 | 13,22564 | 12,79229 | 6,67895 | 14,17903 | €673,21 | €1.346,41 | €44,12 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | WLD | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,46919 | 0,46919 | 0,44675 | 0,23694 | 0,51857 | €462,02 | €924,05 | €44,20 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | NEAR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,54251 | 2,49900 | 2,43442 | 1,28397 | 2,78031 | €514,46 | €1.028,91 | €43,74 | €-17,61 |
| Scanner Top5 Btc Runner25 V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00176 | €210,95 | €421,90 | €50,63 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1363,81560 | €965,52 | €1.931,04 | €49,49 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01601 | €209,51 | €419,03 | €50,28 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,15692 | €27,23 | €54,45 | €3,29 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | UNI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 7,09542 | 7,09542 | 6,78408 | 3,58319 | 8,02944 | €21,18 | €42,36 | €1,86 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | NEAR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,52150 | 2,49900 | 2,41155 | 1,27336 | 2,85137 | €535,58 | €1.071,17 | €46,71 | €-9,56 |
| Scanner Top5 Btc Tp3 V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00176 | €211,07 | €422,14 | €50,66 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1363,81560 | €966,09 | €1.932,17 | €49,52 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | HEMI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01601 | €209,64 | €419,27 | €50,31 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | ARB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,15692 | €27,24 | €54,49 | €3,29 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | UNI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 7,09542 | 7,09542 | 6,78408 | 3,58319 | 8,02944 | €21,19 | €42,39 | €1,86 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | NEAR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,52150 | 2,49900 | 2,41155 | 1,27336 | 2,85137 | €535,90 | €1.071,80 | €46,74 | €-9,57 |
| Global Confluence puro 1H | DOGE | SHORT | Global Confluence puro | 60m | 2,0x | 0,08675 | 0,08550 | 0,08882 | 0,12970 | 0,08158 | €1.011,45 | €2.022,91 | €48,24 | €29,21 |
| Combo Trend | BEAT | SHORT | Combo Trend | 60m | 2,0x | 0,25984 | 0,25984 | 0,25657 | 0,38847 | 0,19125 | €193,71 | €387,42 | €0,00 | €-0,00 |
| Combo Trend | ADA | SHORT | Combo Trend | 60m | 2,0x | 0,19986 | 0,19986 | 0,20356 | 0,29879 | 0,19173 | €1.205,82 | €2.411,64 | €44,61 | €-0,00 |
| Combo Trend | BTR | SHORT | Combo Trend | 60m | 2,0x | 0,05109 | 0,05109 | 0,05109 | 0,07638 | 0,03760 | €188,04 | €376,08 | €0,00 | €-0,00 |
| Combo Trend | ARB | LONG | Combo Trend | 60m | 2,0x | 0,13283 | 0,13283 | 0,12390 | 0,06708 | 0,15246 | €327,77 | €655,53 | €44,04 | €0,00 |
| Combo Trend | UNI | LONG | Combo Trend | 60m | 2,0x | 7,07742 | 7,07742 | 6,75804 | 3,57409 | 7,78005 | €68,62 | €137,24 | €6,19 | €0,00 |
| Combo Mean Reversion | ADA | LONG | Combo Mean Reversion | 60m | 2,0x | 0,20284 | 0,20284 | 0,19804 | 0,10244 | 0,21052 | €942,00 | €1.883,99 | €44,59 | €0,00 |
| Combo Scanner | BOME | LONG | Combo Scanner | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €195,20 | €390,40 | €46,85 | €0,00 |
| Combo Scanner | TRUMP | LONG | Combo Scanner | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,14149 | €213,98 | €427,96 | €49,38 | €0,00 |
| Combo Scanner | SKHYNIX | LONG | Combo Scanner | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €24,78 | €49,55 | €1,27 | €0,00 |
| Combo Scanner | ARB | LONG | Combo Scanner | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,15050 | €419,07 | €838,14 | €50,68 | €0,00 |
| Combo Scanner | UNI | LONG | Combo Scanner | 60m | 2,0x | 7,09542 | 7,09542 | 6,78408 | 3,58319 | 7,78036 | €583,31 | €1.166,62 | €51,19 | €0,00 |
| Combo Scanner | TAO | LONG | Combo Scanner | 60m | 2,0x | 264,91297 | 264,91297 | 254,31765 | 133,78105 | 288,22268 | €105,11 | €210,22 | €8,41 | €0,00 |
| Combo Adaptive | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,01735 | 121,01735 | 128,90956 | 180,92093 | 105,23292 | €367,30 | €734,61 | €47,91 | €-0,00 |
| Combo Adaptive | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €40,89 | €81,77 | €3,12 | €0,00 |
| Combo Adaptive | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,52450 | 2,33981 | 1,27487 | 2,89389 | €18,69 | €37,37 | €2,73 | €0,00 |
| Combo Adaptive | 0G | LONG | Combo Adaptive | 60m | 2,0x | 0,23904 | 0,23904 | 0,21329 | 0,12072 | 0,29055 | €230,13 | €460,26 | €49,58 | €0,00 |
| Combo Adaptive | BTR | SHORT | Combo Adaptive | 60m | 2,0x | 0,04853 | 0,04853 | 0,04853 | 0,07255 | 0,03688 | €212,51 | €425,02 | €0,00 | €-0,00 |
| Combo Adaptive | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,14889 | €420,61 | €841,21 | €50,86 | €0,00 |
| Combo Adaptive | UNI | LONG | Combo Adaptive | 60m | 2,0x | 7,16543 | 7,16543 | 6,92567 | 3,61854 | 7,64496 | €12,79 | €25,58 | €0,86 | €0,00 |
| Combo Adaptive | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,08625 | 0,08550 | 0,08812 | 0,12895 | 0,08251 | €27,03 | €54,06 | €1,17 | €0,47 |
| Combo Adaptive Mfe Trail | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €54,29 | €108,58 | €4,15 | €0,00 |
| Combo Adaptive Mfe Trail | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,52450 | 2,33981 | 1,27487 | 2,89389 | €315,75 | €631,50 | €46,20 | €0,00 |
| Combo Adaptive Mfe Trail | TUT | SHORT | Combo Adaptive | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €190,04 | €380,09 | €45,61 | €-0,00 |
| Combo Adaptive Mfe Trail | PROM | LONG | Combo Adaptive | 60m | 2,0x | 7,01991 | 7,01991 | 6,30832 | 3,54505 | 8,44309 | €21,72 | €43,45 | €4,40 | €0,00 |
| Combo Adaptive Mfe Trail | BTR | SHORT | Combo Adaptive | 60m | 2,0x | 0,04991 | 0,04991 | 0,04841 | 0,07462 | 0,03793 | €142,63 | €285,27 | €0,00 | €-0,00 |
| Combo Adaptive Mfe Trail | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,14889 | €367,37 | €734,74 | €44,43 | €0,00 |
| Combo Adaptive Mfe Trail | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,08625 | 0,08550 | 0,08812 | 0,12895 | 0,08251 | €36,85 | €73,70 | €1,60 | €0,64 |
| Combo Adaptive Quality7 V1 | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €371,68 | €743,36 | €47,16 | €-0,00 |
| Combo Adaptive Quality7 V1 | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €646,78 | €1.293,57 | €49,39 | €0,00 |
| Combo Adaptive Quality7 V1 | ZORA | LONG | Combo Adaptive | 60m | 2,0x | 0,00942 | 0,00942 | 0,00829 | 0,00476 | 0,01169 | €199,23 | €398,46 | €47,81 | €0,00 |
| Combo Adaptive Quality7 V1 | 0G | LONG | Combo Adaptive | 60m | 2,0x | 0,24605 | 0,24605 | 0,22046 | 0,12425 | 0,29722 | €220,81 | €441,63 | €45,92 | €0,00 |
| Combo Adaptive Regime V1 | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €987,06 | €1.974,12 | €49,09 | €0,00 |
| Combo Adaptive Long Only V1 | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 2,08142 | 2,49900 | 2,00650 | 1,05112 | 2,23125 | €645,48 | €1.290,95 | €46,47 | €259,00 |
| Combo Adaptive Long Only V1 | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,52450 | 2,33981 | 1,27487 | 2,89389 | €48,12 | €96,24 | €7,04 | €0,00 |
| Combo Adaptive Long Only V1 | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1331,36020 | €968,99 | €1.937,97 | €49,66 | €0,00 |
| Combo Adaptive Long Only V1 | HEMI | LONG | Combo Adaptive | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €216,09 | €432,18 | €51,86 | €0,00 |
| Combo Adaptive Long Only V1 | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,14889 | €436,65 | €873,31 | €52,81 | €0,00 |
| Combo Adaptive Long Only V1 | UNI | LONG | Combo Adaptive | 60m | 2,0x | 7,16543 | 7,16543 | 6,92567 | 3,61854 | 7,64496 | €15,48 | €30,96 | €1,04 | €0,00 |
| Combo Adaptive Long Only V1 | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 1246,65928 | 1238,83000 | 1198,94620 | 629,56294 | 1342,08543 | €93,25 | €186,49 | €7,14 | €-1,17 |
| Combo Adaptive Partial 1R V1 | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,01735 | 121,01735 | 128,90956 | 180,92093 | 105,23292 | €352,70 | €705,40 | €46,00 | €-0,00 |
| Combo Adaptive Partial 1R V1 | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,52450 | 2,33981 | 1,27487 | 2,89389 | €347,19 | €694,38 | €50,80 | €0,00 |
| Combo Adaptive Partial 1R V1 | VELVET | SHORT | Combo Adaptive | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €207,76 | €415,52 | €0,00 | €-0,00 |
| Combo Adaptive Partial 1R V1 | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €1.013,20 | €2.026,40 | €50,39 | €0,00 |
| Combo Adaptive Partial 1R V1 | TAO | LONG | Combo Adaptive | 60m | 2,0x | 264,91297 | 264,91297 | 254,31765 | 133,78105 | 286,10361 | €49,09 | €98,18 | €3,93 | €0,00 |
| Combo Adaptive Runner25 V1 | 0G | LONG | Combo Adaptive | 60m | 2,0x | 0,23904 | 0,23904 | 0,21329 | 0,12072 | 0,31630 | €204,19 | €408,39 | €43,99 | €0,00 |
| Combo Adaptive Runner25 V1 | BTR | SHORT | Combo Adaptive | 60m | 2,0x | 0,04991 | 0,04991 | 0,04991 | 0,07462 | 0,03194 | €182,83 | €365,66 | €0,00 | €-0,00 |
| Combo Adaptive Runner25 V1 | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,15692 | €376,21 | €752,41 | €45,50 | €0,00 |
| Combo Adaptive Runner25 V1 | UNI | LONG | Combo Adaptive | 60m | 2,0x | 7,16543 | 7,16543 | 6,92567 | 3,61854 | 7,88472 | €17,00 | €34,01 | €1,14 | €0,00 |
| Combo Adaptive Runner25 V1 | TAO | LONG | Combo Adaptive | 60m | 2,0x | 264,91297 | 264,91297 | 254,31765 | 133,78105 | 296,69893 | €536,57 | €1.073,13 | €42,92 | €0,00 |
| Combo Adaptive Runner25 V1 | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,08625 | 0,08550 | 0,08812 | 0,12895 | 0,08064 | €108,53 | €217,05 | €4,71 | €1,89 |
| Combo Adaptive Tp3 V1 | 0G | LONG | Combo Adaptive | 60m | 2,0x | 0,23904 | 0,23904 | 0,21329 | 0,12072 | 0,31630 | €200,38 | €400,76 | €43,17 | €0,00 |
| Combo Adaptive Tp3 V1 | BTR | SHORT | Combo Adaptive | 60m | 2,0x | 0,04991 | 0,04991 | 0,04991 | 0,07462 | 0,03194 | €179,40 | €358,80 | €0,00 | €-0,00 |
| Combo Adaptive Tp3 V1 | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,15692 | €369,17 | €738,34 | €44,64 | €0,00 |
| Combo Adaptive Tp3 V1 | UNI | LONG | Combo Adaptive | 60m | 2,0x | 7,16543 | 7,16543 | 6,92567 | 3,61854 | 7,88472 | €16,69 | €33,37 | €1,12 | €0,00 |
| Combo Adaptive Tp3 V1 | TAO | LONG | Combo Adaptive | 60m | 2,0x | 264,91297 | 264,91297 | 254,31765 | 133,78105 | 296,69893 | €526,53 | €1.053,06 | €42,12 | €0,00 |
| Combo Adaptive Tp3 V1 | DOGE | SHORT | Combo Adaptive | 60m | 2,0x | 0,08625 | 0,08550 | 0,08812 | 0,12895 | 0,08064 | €106,53 | €213,07 | €4,62 | €1,86 |
| Btc Ema 1H | BTC | SHORT | Trend following EMA | 60m | 3,0x | 78718,15322 | 78245,50000 | 79851,69463 | 104563,94686 | 76451,07041 | €1.091,81 | €3.275,44 | €47,17 | €19,67 |
| Btc Donchian 1H | BTC | SHORT | Donchian breakout 20 barre | 60m | 3,0x | 78081,18064 | 78245,50000 | 79080,61975 | 103717,83495 | 76082,30242 | €1.292,04 | €3.876,13 | €49,61 | €-8,16 |
| Btc Adaptive 1H | BTC | SHORT | Combo Adaptive | 60m | 3,0x | 78081,18064 | 78245,50000 | 79205,54964 | 103717,83495 | 75832,44264 | €1.147,51 | €3.442,53 | €49,57 | €-7,24 |
| Sol Ema 1H | SOL | SHORT | Trend following EMA | 60m | 3,0x | 101,32873 | 101,65600 | 103,03410 | 134,59833 | 97,91799 | €986,59 | €2.959,78 | €49,81 | €-9,56 |
| Sol Donchian 1H | SOL | SHORT | Donchian breakout 20 barre | 60m | 3,0x | 101,32873 | 101,65600 | 102,84462 | 134,59833 | 98,29696 | €1.140,45 | €3.421,36 | €51,18 | €-11,05 |
| Sol Donchian 4H | SOL | LONG | Donchian breakout 20 barre | 240m | 2,0x | 104,23184 | 101,65600 | 99,63427 | 52,63708 | 117,10505 | €574,98 | €1.149,96 | €50,72 | €-28,42 |
| Sol Adaptive 1H | SOL | SHORT | Combo Adaptive | 60m | 3,0x | 101,52669 | 101,65600 | 103,23214 | 134,86129 | 98,11580 | €987,60 | €2.962,81 | €49,77 | €-3,77 |
| Eth Ema 4H | ETH | LONG | Trend following EMA | 240m | 2,0x | 2499,33977 | 2473,30000 | 2409,82951 | 1262,16658 | 2723,11538 | €690,19 | €1.380,39 | €49,44 | €-14,38 |
| Eth Donchian 1H | ETH | SHORT | Donchian breakout 20 barre | 60m | 3,0x | 2456,28864 | 2473,30000 | 2487,72914 | 3262,77008 | 2393,40765 | €1.264,47 | €3.793,40 | €48,56 | €-26,27 |
| Doge Ema 1H | DOGE | SHORT | Trend following EMA | 60m | 3,0x | 0,08625 | 0,08550 | 0,08812 | 0,11457 | 0,08251 | €767,12 | €2.301,36 | €49,95 | €20,08 |
| Doge Donchian 1H | DOGE | SHORT | Donchian breakout 20 barre | 60m | 3,0x | 0,08578 | 0,08550 | 0,08754 | 0,11395 | 0,08226 | €817,40 | €2.452,21 | €50,33 | €8,09 |
| Doge Bollinger 1H | DOGE | LONG | Bollinger mean reversion | 60m | 3,0x | 0,08629 | 0,08550 | 0,08473 | 0,05796 | 0,08863 | €919,62 | €2.758,86 | €49,90 | €-25,17 |
| Master Adaptive V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99403 | 639,55695 | 1331,36019 | €22,75 | €45,50 | €1,17 | €0,00 |
| Master Adaptive V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €195,57 | €391,15 | €46,94 | €0,00 |
| Master Adaptive V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,20498 | 0,11491 | 0,27267 | €236,54 | €473,08 | €46,91 | €0,00 |
| Master Adaptive V1 | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,13517 | 0,13517 | 0,12719 | 0,06826 | 0,15112 | €410,30 | €820,61 | €48,44 | €0,00 |
| Master Adaptive V1 | ZEC | LONG | Master Adaptive Consensus | 60m | 2,0x | 1215,80311 | 1238,83000 | 1170,51942 | 613,98057 | 1306,37049 | €14,96 | €29,92 | €1,11 | €0,57 |
| Master Adaptive No Alt V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1255,10261 | 1255,10261 | 1225,12158 | 633,82682 | 1315,06467 | €19,09 | €38,19 | €0,91 | €0,00 |
| Master Adaptive No Alt V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €183,81 | €367,62 | €44,11 | €0,00 |
| Master Adaptive No Alt V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 530,08600 | 530,08600 | 509,10047 | 267,69343 | 572,05705 | €589,91 | €1.179,82 | €46,71 | €0,00 |
| Master Adaptive No Alt V1 | WLD | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,46919 | 0,46919 | 0,44675 | 0,23694 | 0,51408 | €481,98 | €963,96 | €46,11 | €0,00 |
| Master Adaptive No Alt V1 | ZEC | LONG | Master Adaptive Consensus | 60m | 2,0x | 1215,80311 | 1238,83000 | 1170,51942 | 613,98057 | 1306,37049 | €588,97 | €1.177,95 | €43,87 | €22,31 |
| Master Adaptive No Alt V1 | NEAR | LONG | Master Adaptive Consensus | 60m | 2,0x | 2,52150 | 2,49900 | 2,41155 | 1,27336 | 2,74141 | €41,97 | €83,94 | €3,66 | €-0,75 |
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
| Master Adaptive Gb20 V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99403 | 639,55695 | 1331,36019 | €22,45 | €44,90 | €1,15 | €0,00 |
| Master Adaptive Gb20 V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €193,03 | €386,06 | €46,33 | €0,00 |
| Master Adaptive Gb20 V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,20498 | 0,11491 | 0,27267 | €233,42 | €466,83 | €46,29 | €0,00 |
| Master Adaptive Gb20 V1 | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,13517 | 0,13517 | 0,12719 | 0,06826 | 0,15112 | €404,89 | €809,78 | €47,80 | €0,00 |
| Master Adaptive Gb20 V1 | ZEC | LONG | Master Adaptive Consensus | 60m | 2,0x | 1215,80311 | 1238,83000 | 1170,51942 | 613,98057 | 1306,37049 | €14,65 | €29,29 | €1,09 | €0,55 |
| Master Adaptive Runner25 V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03814 | 0,02188 | 0,05894 | €34,77 | €69,54 | €8,34 | €0,00 |
| Master Adaptive Runner25 V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1255,10261 | 1255,10261 | 1225,12158 | 633,82682 | 1345,04570 | €27,05 | €54,10 | €1,29 | €0,00 |
| Master Adaptive Runner25 V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01601 | €185,86 | €371,72 | €44,61 | €0,00 |
| Master Adaptive Runner25 V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,20498 | 0,11491 | 0,29523 | €233,84 | €467,69 | €46,37 | €0,00 |
| Master Adaptive Runner25 V1 | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,13517 | 0,13517 | 0,12719 | 0,06826 | 0,15910 | €399,89 | €799,78 | €47,21 | €0,00 |
| Master Adaptive Runner25 V1 | ZEC | LONG | Master Adaptive Consensus | 60m | 2,0x | 1248,87973 | 1238,83000 | 1203,47828 | 630,68426 | 1385,08406 | €599,39 | €1.198,78 | €43,58 | €-9,65 |
| Combo Adaptive Side Regime Guard V1 | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 2,08142 | 2,49900 | 2,00650 | 1,05112 | 2,23125 | €77,52 | €155,04 | €5,58 | €31,10 |
| Combo Adaptive Side Regime Guard V1 | VELVET | SHORT | Combo Adaptive | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €216,61 | €433,23 | €0,00 | €-0,00 |
| Combo Adaptive Side Regime Guard V1 | TUT | SHORT | Combo Adaptive | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €192,40 | €384,79 | €46,18 | €-0,00 |
| Combo Adaptive Side Regime Guard V1 | BTR | SHORT | Combo Adaptive | 60m | 2,0x | 0,05109 | 0,05109 | 0,05109 | 0,07638 | 0,03883 | €195,57 | €391,13 | €0,00 | €-0,00 |
| Combo Adaptive Side Regime Guard V1 | ARB | LONG | Combo Adaptive | 60m | 2,0x | 0,13283 | 0,13283 | 0,12480 | 0,06708 | 0,14889 | €385,18 | €770,35 | €46,58 | €0,00 |
| Combo Adaptive Side Regime Guard V1 | UNI | LONG | Combo Adaptive | 60m | 2,0x | 7,16543 | 7,16543 | 6,92567 | 3,61854 | 7,64496 | €12,54 | €25,08 | €0,84 | €0,00 |
| Combo Adaptive Side Regime Guard V1 | SOL | SHORT | Combo Adaptive | 60m | 2,0x | 101,87362 | 101,65600 | 103,51750 | 152,30106 | 98,58587 | €13,27 | €26,54 | €0,43 | €0,06 |
| Master Adaptive Gb20 Be V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99403 | 639,55695 | 1331,36019 | €22,86 | €45,73 | €1,17 | €0,00 |
| Master Adaptive Gb20 Be V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €196,54 | €393,08 | €47,17 | €0,00 |
| Master Adaptive Gb20 Be V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,20498 | 0,11491 | 0,27267 | €237,71 | €475,42 | €47,14 | €0,00 |
| Master Adaptive Gb20 Be V1 | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,13517 | 0,13517 | 0,12719 | 0,06826 | 0,15112 | €412,34 | €824,67 | €48,68 | €0,00 |
| Master Adaptive Gb20 Be V1 | ZEC | LONG | Master Adaptive Consensus | 60m | 2,0x | 1215,80311 | 1238,83000 | 1170,51942 | 613,98057 | 1306,37049 | €15,03 | €30,07 | €1,12 | €0,57 |
| Master Adaptive Gb20 Partial V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99403 | 639,55695 | 1331,36019 | €22,84 | €45,68 | €1,17 | €0,00 |
| Master Adaptive Gb20 Partial V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01036 | 0,00594 | 0,01459 | €196,33 | €392,67 | €47,12 | €0,00 |
| Master Adaptive Gb20 Partial V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,20498 | 0,11491 | 0,27267 | €237,46 | €474,91 | €47,09 | €0,00 |
| Master Adaptive Gb20 Partial V1 | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,13517 | 0,13517 | 0,12719 | 0,06826 | 0,15112 | €411,90 | €823,79 | €48,63 | €0,00 |
| Master Adaptive Gb20 Partial V1 | ZEC | LONG | Master Adaptive Consensus | 60m | 2,0x | 1215,80311 | 1238,83000 | 1170,51942 | 613,98057 | 1306,37049 | €15,02 | €30,03 | €1,12 | €0,57 |
| Master Adaptive Gb20 Loss Cap V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03828 | 0,02188 | 0,05682 | €195,70 | €391,41 | €45,67 | €0,00 |
| Master Adaptive Gb20 Loss Cap V1 | HEMI | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,01177 | 0,01177 | 0,01069 | 0,00594 | 0,01465 | €210,34 | €420,68 | €38,67 | €0,00 |
| Master Adaptive Gb20 Loss Cap V1 | PROM | LONG | Master Adaptive Consensus | 60m | 2,0x | 7,01991 | 7,01991 | 6,48622 | 3,54505 | 8,44309 | €34,75 | €69,51 | €5,28 | €0,00 |
| Master Adaptive Gb20 Loss Cap V1 | 0G | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,22755 | 0,22755 | 0,21062 | 0,11491 | 0,27267 | €309,65 | €619,30 | €46,05 | €0,00 |
| Master Adaptive Gb20 Loss Cap V1 | ARB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,13517 | 0,13517 | 0,12918 | 0,06826 | 0,15112 | €19,32 | €38,65 | €1,71 | €0,00 |
| Master Adaptive Gb20 Loss Cap V1 | WLD | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,46919 | 0,46919 | 0,45236 | 0,23694 | 0,51408 | €80,25 | €160,51 | €5,76 | €0,00 |
| Master Adaptive Gb20 Loss Cap V1 | ZEC | LONG | Master Adaptive Consensus | 60m | 2,0x | 1215,80311 | 1238,83000 | 1181,84035 | 613,98057 | 1306,37049 | €20,23 | €40,46 | €1,13 | €0,77 |
| Master Adaptive Gb20 Loss Cap V1 | NEAR | LONG | Master Adaptive Consensus | 60m | 2,0x | 2,50250 | 2,49900 | 2,41886 | 1,26376 | 2,72555 | €626,11 | €1.252,23 | €41,85 | €-1,75 |
| 1H Fast V3 Nohigh Range Only V1 | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,20283 | 0,20283 | 0,20750 | 0,26943 | 0,19582 | €740,69 | €2.222,07 | €51,20 | €-0,00 |
| 1H Fast V3 Nohigh Range Only V1 | BTR | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €135,43 | €406,30 | €0,00 | €-0,00 |
| 1H Fast V3 Nohigh Range Only V1 | DOGE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,08675 | 0,08550 | 0,08654 | 0,11524 | 0,08458 | €1.009,04 | €3.027,13 | €0,00 | €43,71 |
| 1H Fast V3 Nohigh Regime Guard V1 | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €140,84 | €422,53 | €50,70 | €-0,00 |
| 1H Fast V3 Nohigh Regime Guard V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €143,15 | €429,46 | €50,70 | €-0,00 |
| 1H Fast V3 Nohigh Regime Guard V1 | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,20283 | 0,20283 | 0,20750 | 0,26943 | 0,19582 | €34,57 | €103,71 | €2,39 | €-0,00 |
| 1H Fast V3 Nohigh Regime Guard V1 | BTR | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,05154 | 0,05154 | 0,05154 | 0,06846 | 0,04226 | €139,06 | €417,17 | €0,00 | €-0,00 |
| 1H Fast V3 Nohigh Regime Guard V1 | DOGE | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,08675 | 0,08550 | 0,08654 | 0,11524 | 0,08458 | €30,67 | €92,00 | €0,00 | €1,33 |
| 1H Fast V3 Nohigh Regime Guard V1 | BTC | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 78081,18064 | 78245,50000 | 78955,68986 | 103717,83495 | 76769,41681 | €1.541,74 | €4.625,22 | €51,80 | €-9,73 |
| Main Side Regime Guard V1 | VELVET | LONG | Confluenza trend | 240m | 3,0x | 0,55987 | 0,55987 | 0,49269 | 0,37605 | 0,69424 | €142,25 | €426,74 | €51,21 | €0,00 |
| Main Side Regime Guard V1 | AKE | LONG | Confluenza trend | 240m | 3,0x | 0,01021 | 0,01021 | 0,00899 | 0,00686 | 0,01266 | €145,97 | €437,90 | €52,55 | €0,00 |
| Main Side Regime Guard V1 | ENA | LONG | Confluenza trend | 240m | 3,0x | 0,16108 | 0,16108 | 0,14175 | 0,10819 | 0,19974 | €150,44 | €451,33 | €54,16 | €0,00 |
| Main Side Regime Guard V1 | BTR | SHORT | Confluenza trend | 240m | 3,0x | 0,04853 | 0,04853 | 0,05435 | 0,06446 | 0,03688 | €12,76 | €38,29 | €4,59 | €-0,00 |
| Main Side Regime Guard V1 | ZEC | LONG | Confluenza trend | 240m | 3,0x | 1248,87973 | 1238,83000 | 1152,08799 | 838,83088 | 1442,46321 | €239,17 | €717,51 | €55,61 | €-5,77 |
| Main Side Regime Guard V1 | NEAR | LONG | Confluenza trend | 240m | 3,0x | 2,49550 | 2,49900 | 2,26921 | 1,67614 | 2,94807 | €15,83 | €47,48 | €4,31 | €0,07 |
| Main Dynamic Asset Selector V1 | ENA | LONG | Confluenza trend | 240m | 3,0x | 0,16108 | 0,16108 | 0,14175 | 0,10819 | 0,19974 | €140,98 | €422,93 | €50,75 | €0,00 |
| Main Dynamic Asset Selector V1 | ZEC | LONG | Confluenza trend | 240m | 3,0x | 1190,40803 | 1238,83000 | 1090,98250 | 799,55740 | 1389,25911 | €203,57 | €610,70 | €51,01 | €24,84 |
| Combo Trend Side Regime Guard V1 | VELVET | SHORT | Combo Trend | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,12693 | €217,86 | €435,73 | €0,00 | €-0,00 |
| Combo Trend Side Regime Guard V1 | TUT | SHORT | Combo Trend | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03364 | €12,81 | €25,62 | €3,07 | €-0,00 |
| Combo Trend Side Regime Guard V1 | BTR | SHORT | Combo Trend | 60m | 2,0x | 0,04853 | 0,04853 | 0,05435 | 0,07255 | 0,03572 | €222,18 | €444,37 | €53,32 | €-0,00 |
| Combo Trend Side Regime Guard V1 | ARB | LONG | Combo Trend | 60m | 2,0x | 0,13283 | 0,13283 | 0,12390 | 0,06708 | 0,15246 | €399,57 | €799,13 | €53,69 | €0,00 |
| Combo Trend Side Regime Guard V1 | UNI | LONG | Combo Trend | 60m | 2,0x | 7,09542 | 7,09542 | 6,74949 | 3,58319 | 7,85647 | €523,05 | €1.046,10 | €51,00 | €0,00 |
| Combo Trend Side Regime Guard V1 | TAO | LONG | Combo Trend | 60m | 2,0x | 264,91297 | 264,91297 | 253,14039 | 133,78105 | 290,81264 | €73,76 | €147,52 | €6,56 | €0,00 |
| 1H Fast Nohigh Cap75 Short Only V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €135,82 | €407,46 | €48,90 | €-0,00 |
| 1H Fast Nohigh Cap75 Short Only V1 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €138,05 | €414,14 | €48,89 | €-0,00 |
| 1H Fast Nohigh Cap75 Short Only V1 | BTR | SHORT | Momentum / breakout | 60m | 3,0x | 0,05031 | 0,05031 | 0,05031 | 0,06683 | 0,04125 | €132,24 | €396,72 | €0,00 | €-0,00 |
| 1H Fast Nohigh Cap75 Short Only V1 | PEPE | SHORT | Momentum / breakout | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €573,54 | €1.720,62 | €44,16 | €39,93 |
| 1H Fast Nohigh Cap75 Short Only V1 | DOGE | SHORT | Momentum / breakout | 60m | 3,0x | 0,08625 | 0,08550 | 0,08771 | 0,11457 | 0,08407 | €10,00 | €29,99 | €0,51 | €0,26 |
| 1H Balanced V3 Long Only V1 | SKHYNIX | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1220,85412 | 1220,85412 | 1177,63561 | 820,00702 | 1307,29117 | €435,49 | €1.306,46 | €46,25 | €0,00 |
| 1H Balanced V3 Long Only V1 | ADA | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,20138 | 0,20138 | 0,20719 | 0,26750 | 0,18976 | €529,53 | €1.588,58 | €45,82 | €-0,00 |
| 1H Balanced V3 Long Only V1 | ARB | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,13283 | 0,13283 | 0,12480 | 0,08922 | 0,14889 | €248,38 | €745,13 | €45,06 | €0,00 |
| 1H Balanced V3 Long Only V1 | UNI | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 7,14143 | 7,14143 | 6,87560 | 4,79666 | 7,67309 | €9,06 | €27,18 | €1,01 | €0,00 |
| 1H Balanced V3 Long Only V1 | SOPH | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,00528 | 0,00528 | 0,00591 | 0,00701 | 0,00401 | €103,13 | €309,38 | €37,13 | €-0,00 |
| 1H Balanced V3 Long Only V1 | DOGE | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,08578 | 0,08550 | 0,08776 | 0,11395 | 0,08182 | €37,82 | €113,46 | €2,62 | €0,37 |
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
| Sol Adaptive 4H | SOL | LONG | 2026-09-09T22:15:00+00:00 | 100,97395 | €-52,51 | -1,03 | STOP |
| Scanner Top20 Long | ZEC | LONG | 2026-09-09T22:15:00+00:00 | 1222,33789 | €-53,46 | -1,04 | STOP |
| Scanner Top15 Long | ZEC | LONG | 2026-09-09T22:15:00+00:00 | 1222,33789 | €-53,46 | -1,04 | STOP |
| Forza relativa 1H V2 | ZEC | LONG | 2026-09-09T22:15:00+00:00 | 1227,94873 | €-1,08 | -1,04 | STOP |
| Forza relativa 1H V1 | ZEC | LONG | 2026-09-09T22:15:00+00:00 | 1224,21981 | €-43,99 | -1,04 | STOP |
| Master Adaptive Runner25 V1 | ZEC | LONG | 2026-09-09T22:15:00+00:00 | 1227,94873 | €-44,79 | -1,04 | STOP |
| Combo Adaptive Long Only V1 | ZEC | LONG | 2026-09-09T22:15:00+00:00 | 1221,84007 | €-1,28 | -1,03 | STOP |
| 1H Balanced V3 Long Only V1 | ZEC | LONG | 2026-09-09T22:15:00+00:00 | 1222,33789 | €-2,77 | -1,04 | STOP |
| Bilanciata 1H V3 Filtered | ZEC | LONG | 2026-09-09T22:15:00+00:00 | 1222,33789 | €-2,93 | -1,04 | STOP |
| 1H Balanced Long No Rhv V1 | ZEC | LONG | 2026-09-09T22:15:00+00:00 | 1227,94873 | €-3,07 | -1,04 | STOP |
| Master Adaptive No Alt V1 | XRP | LONG | 2026-09-09T22:00:00+00:00 | 1,39152 | €-1,41 | -1,10 | STOP |
| Master Adaptive Expanded V1 | XRP | LONG | 2026-09-09T22:00:00+00:00 | 1,39152 | €-0,72 | -1,10 | STOP |

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

Generato: 2026-09-10 05:33 UTC


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

Segnali totali salvati: **186**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-09-10 | BTC | 78.479,28 | +6 | +3 | +3 | 0 | +2 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-09-10 | DOGE | 0.08593 | -4 | -2 | -2 | 0 | -1 | 0 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-09-10 | SOL | 102,04 | +5 | +2 | +2 | 0 | +2 | 0 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-09-09 | BTC | 78.978,35 | +6 | +3 | +3 | 0 | +3 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-09-09 | DOGE | 0.09017 | +3 | -1 | -1 | 0 | +3 | 0 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-09-09 | SOL | 104,26 | +5 | +2 | +2 | 0 | +3 | +1 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-09-08 | BTC | 78.724,26 | +6 | +3 | +3 | 0 | +3 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-09-08 | DOGE | 0.09002 | +3 | -2 | -2 | 0 | +3 | +1 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-09-08 | SOL | 103,26 | +8 | +3 | +3 | 0 | +3 | +1 | 0 | HOLD / ACCUMULO A TRANCHE, NO LEVA AGGRESSIVA |
| 2026-09-07 | BTC | 79.828,11 | +7 | +3 | +3 | 0 | +3 | 0 | 0 | ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA |
| 2026-09-07 | DOGE | 0.09027 | +1 | -2 | -2 | 0 | +3 | +1 | 0 | STAI ALLA FINESTRA |
| 2026-09-07 | SOL | 105,55 | +8 | +3 | +3 | 0 | +3 | +1 | 0 | HOLD / ACCUMULO A TRANCHE, NO LEVA AGGRESSIVA |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 62 | 61 | 60 | 59 | 57 | 55 | 52 | 48 | 41 | 34 | 19 | 4 |
| SOL | 62 | 61 | 60 | 59 | 57 | 55 | 52 | 48 | 41 | 34 | 19 | 4 |
| DOGE | 62 | 61 | 60 | 59 | 57 | 55 | 52 | 48 | 41 | 34 | 19 | 4 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-07-13 | 60g | 2026-09-11 | domani |
| SOL | 2026-07-13 | 60g | 2026-09-11 | domani |
| DOGE | 2026-07-13 | 60g | 2026-09-11 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 58 | 50,00% | +0,39% | +0,37% | PRIMA CALIBRAZIONE |
| BTC | 2g | 57 | 50,88% | +0,70% | +0,62% | PRIMA CALIBRAZIONE |
| BTC | 3g | 56 | 46,43% | +0,89% | +0,77% | PRIMA CALIBRAZIONE |
| BTC | 5g | 54 | 46,30% | +1,84% | +1,61% | PRIMA CALIBRAZIONE |
| BTC | 7g | 52 | 55,77% | +2,62% | +2,42% | PRIMA CALIBRAZIONE |
| BTC | 10g | 49 | 63,27% | +3,63% | +3,44% | PRIMA CALIBRAZIONE |
| BTC | 14g | 45 | 62,22% | +5,60% | +5,52% | PRIMA CALIBRAZIONE |
| BTC | 21g | 38 | 63,16% | +10,62% | +10,44% | PRIMA CALIBRAZIONE |
| BTC | 30g | 32 | 90,62% | +14,16% | +12,82% | PRIMA CALIBRAZIONE |
| BTC | 45g | 17 | 88,24% | +22,40% | +17,15% | FEEDBACK RAPIDO |
| BTC | 60g | 4 | 100,00% | +23,95% | +23,95% | FEEDBACK RAPIDO |
| SOL | 1g | 54 | 53,70% | +0,60% | +0,48% | PRIMA CALIBRAZIONE |
| SOL | 2g | 53 | 50,94% | +1,25% | +1,12% | PRIMA CALIBRAZIONE |
| SOL | 3g | 52 | 57,69% | +1,98% | +1,81% | PRIMA CALIBRAZIONE |
| SOL | 5g | 50 | 62,00% | +3,46% | +3,35% | PRIMA CALIBRAZIONE |
| SOL | 7g | 48 | 66,67% | +4,81% | +4,92% | PRIMA CALIBRAZIONE |
| SOL | 10g | 45 | 66,67% | +6,69% | +6,86% | PRIMA CALIBRAZIONE |
| SOL | 14g | 41 | 80,49% | +10,31% | +11,20% | PRIMA CALIBRAZIONE |
| SOL | 21g | 34 | 76,47% | +17,42% | +16,38% | PRIMA CALIBRAZIONE |
| SOL | 30g | 27 | 62,96% | +20,35% | +13,02% | FEEDBACK RAPIDO |
| SOL | 45g | 14 | 35,71% | +33,18% | -11,07% | FEEDBACK RAPIDO |
| SOL | 60g | 3 | 66,67% | +34,24% | +11,96% | FEEDBACK RAPIDO |
| DOGE | 1g | 57 | 43,86% | +0,41% | +0,04% | PRIMA CALIBRAZIONE |
| DOGE | 2g | 56 | 44,64% | +0,91% | +0,29% | PRIMA CALIBRAZIONE |
| DOGE | 3g | 55 | 40,00% | +1,39% | +0,63% | PRIMA CALIBRAZIONE |
| DOGE | 5g | 53 | 49,06% | +2,39% | +1,75% | PRIMA CALIBRAZIONE |
| DOGE | 7g | 51 | 58,82% | +2,91% | +3,08% | PRIMA CALIBRAZIONE |
| DOGE | 10g | 48 | 58,33% | +2,96% | +4,04% | PRIMA CALIBRAZIONE |
| DOGE | 14g | 46 | 69,57% | +4,99% | +7,03% | PRIMA CALIBRAZIONE |
| DOGE | 21g | 39 | 79,49% | +10,08% | +9,06% | PRIMA CALIBRAZIONE |
| DOGE | 30g | 32 | 75,00% | +12,74% | +5,77% | PRIMA CALIBRAZIONE |
| DOGE | 45g | 18 | 5,56% | +20,48% | -17,95% | FEEDBACK RAPIDO |
| DOGE | 60g | 4 | 0,00% | +21,40% | -21,40% | FEEDBACK RAPIDO |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 58 | 50,00% | +0,39% | +0,37% | -0,06% | +0,94% | PRIMA CALIBRAZIONE |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 61 | 52,46% | +0,37% | +0,37% | -0,07% | +0,90% | UTILE |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 61 | 52,46% | +0,37% | +0,37% | -0,07% | +0,90% | UTILE |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,25% | +0,25% | -0,10% | +0,70% | PRIMA CALIBRAZIONE |
| BTC | 1g | Tecnico | CALIBRABILE | 56 | 39,29% | +0,49% | +0,12% | +0,03% | +1,02% | PRIMA CALIBRAZIONE |
| BTC | 1g | Classic technical | CALIBRABILE | 24 | 37,50% | +0,81% | +0,37% | +0,13% | +1,33% | FEEDBACK RAPIDO |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | -0,17% | -0,17% | -0,60% | +0,27% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 57 | 50,88% | +0,70% | +0,62% | +0,12% | +1,38% | PRIMA CALIBRAZIONE |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 60 | 53,33% | +0,79% | +0,79% | +0,22% | +1,47% | UTILE |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 60 | 53,33% | +0,79% | +0,79% | +0,22% | +1,47% | UTILE |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,52% | +0,52% | -0,02% | +1,18% | PRIMA CALIBRAZIONE |
| BTC | 2g | Tecnico | CALIBRABILE | 55 | 43,64% | +0,96% | +0,21% | +0,38% | +1,64% | PRIMA CALIBRAZIONE |
| BTC | 2g | Classic technical | CALIBRABILE | 24 | 41,67% | +1,18% | +0,55% | +0,59% | +1,89% | FEEDBACK RAPIDO |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +0,73% | +0,73% | +0,13% | +1,27% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 56 | 46,43% | +0,89% | +0,77% | -1,00% | +2,57% | PRIMA CALIBRAZIONE |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 59 | 54,24% | +1,18% | +1,18% | -0,98% | +2,79% | PRIMA CALIBRAZIONE |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 59 | 54,24% | +1,18% | +1,18% | -0,98% | +2,79% | PRIMA CALIBRAZIONE |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 35 | 57,14% | +0,91% | +0,91% | -1,00% | +2,36% | PRIMA CALIBRAZIONE |
| BTC | 3g | Tecnico | CALIBRABILE | 54 | 37,04% | +1,47% | -0,09% | -0,81% | +3,05% | PRIMA CALIBRAZIONE |
| BTC | 3g | Classic technical | CALIBRABILE | 24 | 41,67% | +1,81% | +0,20% | -0,58% | +3,31% | FEEDBACK RAPIDO |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +0,35% | +0,35% | -1,11% | +1,90% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 54 | 46,30% | +1,84% | +1,61% | -1,54% | +4,09% | PRIMA CALIBRAZIONE |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 57 | 52,63% | +2,08% | +2,08% | -1,51% | +4,39% | PRIMA CALIBRAZIONE |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 57 | 52,63% | +2,08% | +2,08% | -1,51% | +4,39% | PRIMA CALIBRAZIONE |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 35 | 48,57% | +2,08% | +2,08% | -1,57% | +4,07% | PRIMA CALIBRAZIONE |
| BTC | 5g | Tecnico | CALIBRABILE | 52 | 44,23% | +2,39% | -0,87% | -1,32% | +4,74% | PRIMA CALIBRAZIONE |
| BTC | 5g | Classic technical | CALIBRABILE | 24 | 50,00% | +3,70% | -1,14% | -1,03% | +5,94% | FEEDBACK RAPIDO |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 25,00% | -0,34% | -0,34% | -1,71% | +2,56% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 52 | 55,77% | +2,62% | +2,42% | -1,73% | +5,39% | PRIMA CALIBRAZIONE |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 55 | 61,82% | +2,93% | +2,93% | -1,72% | +5,67% | PRIMA CALIBRAZIONE |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 55 | 61,82% | +2,93% | +2,93% | -1,72% | +5,67% | PRIMA CALIBRAZIONE |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 35 | 60,00% | +3,17% | +3,17% | -1,80% | +5,49% | PRIMA CALIBRAZIONE |
| BTC | 7g | Tecnico | CALIBRABILE | 50 | 44,00% | +3,45% | -1,65% | -1,51% | +6,12% | PRIMA CALIBRAZIONE |
| BTC | 7g | Classic technical | CALIBRABILE | 23 | 47,83% | +5,29% | -2,72% | -1,15% | +8,39% | FEEDBACK RAPIDO |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +0,68% | +0,68% | -1,68% | +3,81% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 49 | 63,27% | +3,63% | +3,44% | -2,00% | +6,48% | PRIMA CALIBRAZIONE |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 52 | 67,31% | +3,79% | +3,79% | -2,00% | +6,72% | PRIMA CALIBRAZIONE |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 52 | 67,31% | +3,79% | +3,79% | -2,00% | +6,72% | PRIMA CALIBRAZIONE |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 35 | 62,86% | +4,42% | +4,42% | -2,02% | +6,89% | PRIMA CALIBRAZIONE |
| BTC | 10g | Tecnico | CALIBRABILE | 47 | 48,94% | +4,32% | -1,34% | -1,77% | +7,31% | PRIMA CALIBRAZIONE |
| BTC | 10g | Classic technical | CALIBRABILE | 20 | 60,00% | +6,61% | -3,94% | -1,28% | +9,78% | FEEDBACK RAPIDO |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +0,54% | +0,54% | -2,46% | +3,88% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 45 | 62,22% | +5,60% | +5,52% | -2,11% | +8,97% | PRIMA CALIBRAZIONE |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 48 | 62,50% | +5,67% | +5,67% | -2,12% | +9,08% | PRIMA CALIBRAZIONE |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 48 | 62,50% | +5,67% | +5,67% | -2,12% | +9,08% | PRIMA CALIBRAZIONE |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 35 | 68,57% | +6,60% | +6,60% | -2,13% | +9,78% | PRIMA CALIBRAZIONE |
| BTC | 14g | Tecnico | CALIBRABILE | 43 | 58,14% | +6,48% | +0,84% | -1,85% | +9,94% | PRIMA CALIBRAZIONE |
| BTC | 14g | Classic technical | CALIBRABILE | 16 | 43,75% | +7,88% | -4,40% | -1,01% | +11,63% | FEEDBACK RAPIDO |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 33,33% | -0,03% | -0,03% | -2,90% | +4,64% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 38 | 63,16% | +10,62% | +10,44% | -2,18% | +14,30% | PRIMA CALIBRAZIONE |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 41 | 70,73% | +10,34% | +10,34% | -2,20% | +14,07% | PRIMA CALIBRAZIONE |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 41 | 70,73% | +10,34% | +10,34% | -2,20% | +14,07% | PRIMA CALIBRAZIONE |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 35 | 74,29% | +11,25% | +11,25% | -2,21% | +14,88% | PRIMA CALIBRAZIONE |
| BTC | 21g | Tecnico | CALIBRABILE | 36 | 36,11% | +11,56% | -1,09% | -1,89% | +15,35% | PRIMA CALIBRAZIONE |
| BTC | 21g | Classic technical | CALIBRABILE | 9 | 11,11% | +18,62% | -15,77% | -0,19% | +21,75% | FEEDBACK RAPIDO |
| BTC | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,21% | +1,21% | -3,06% | +4,24% | FEEDBACK RAPIDO |
| BTC | 30g | Global confluence | BENCHMARK | 32 | 90,62% | +14,16% | +12,82% | -2,96% | +18,17% | PRIMA CALIBRAZIONE |
| BTC | 30g | Famiglia statistica | CALIBRABILE | 34 | 85,29% | +13,80% | +13,80% | -3,00% | +17,88% | PRIMA CALIBRAZIONE |
| BTC | 30g | Scanner grezzo | DIAGNOSTICO | 34 | 85,29% | +13,80% | +13,80% | -3,00% | +17,88% | PRIMA CALIBRAZIONE |
| BTC | 30g | Market regime grezzo | DIAGNOSTICO | 30 | 86,67% | +15,02% | +15,02% | -2,80% | +19,32% | PRIMA CALIBRAZIONE |
| BTC | 30g | Tecnico | CALIBRABILE | 29 | 44,83% | +13,99% | -1,57% | -2,74% | +18,41% | FEEDBACK RAPIDO |
| BTC | 30g | Classic technical | CALIBRABILE | 4 | 0,00% | +24,06% | -24,06% | -1,55% | +28,48% | FEEDBACK RAPIDO |
| BTC | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +0,16% | +0,16% | -3,06% | +4,24% | FEEDBACK RAPIDO |
| BTC | 45g | Global confluence | BENCHMARK | 17 | 88,24% | +22,40% | +17,15% | -3,31% | +26,49% | FEEDBACK RAPIDO |
| BTC | 45g | Famiglia statistica | CALIBRABILE | 19 | 100,00% | +22,46% | +22,46% | -3,35% | +26,51% | FEEDBACK RAPIDO |
| BTC | 45g | Scanner grezzo | DIAGNOSTICO | 19 | 100,00% | +22,46% | +22,46% | -3,35% | +26,51% | FEEDBACK RAPIDO |
| BTC | 45g | Market regime grezzo | DIAGNOSTICO | 15 | 100,00% | +22,83% | +22,83% | -3,04% | +26,85% | FEEDBACK RAPIDO |
| BTC | 45g | Tecnico | CALIBRABILE | 15 | 33,33% | +22,81% | -7,88% | -2,97% | +26,99% | FEEDBACK RAPIDO |
| BTC | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +20,42% | +20,42% | -3,06% | +26,73% | FEEDBACK RAPIDO |
| BTC | 60g | Global confluence | BENCHMARK | 4 | 100,00% | +23,95% | +23,95% | -3,09% | +29,06% | FEEDBACK RAPIDO |
| BTC | 60g | Famiglia statistica | CALIBRABILE | 4 | 100,00% | +23,95% | +23,95% | -3,09% | +29,06% | FEEDBACK RAPIDO |
| BTC | 60g | Scanner grezzo | DIAGNOSTICO | 4 | 100,00% | +23,95% | +23,95% | -3,09% | +29,06% | FEEDBACK RAPIDO |
| BTC | 60g | Market regime grezzo | DIAGNOSTICO | 4 | 100,00% | +23,95% | +23,95% | -3,09% | +29,06% | FEEDBACK RAPIDO |
| BTC | 60g | Tecnico | CALIBRABILE | 3 | 33,33% | +24,18% | -8,86% | -3,03% | +29,15% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 57 | 43,86% | +0,41% | +0,04% | -0,25% | +1,41% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 60 | 58,33% | +0,31% | +0,50% | -0,37% | +1,24% | UTILE |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 60 | 58,33% | +0,31% | +0,50% | -0,37% | +1,24% | UTILE |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,15% | +0,26% | -0,32% | +0,87% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Tecnico | CALIBRABILE | 54 | 51,85% | +0,21% | +0,37% | -0,48% | +1,13% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Classic technical | CALIBRABILE | 34 | 41,18% | +0,22% | -0,49% | -0,44% | +0,96% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 55,56% | +2,13% | +1,78% | +0,65% | +2,81% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 56 | 44,64% | +0,91% | +0,29% | +0,12% | +2,20% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 59 | 55,93% | +0,71% | +0,76% | -0,08% | +1,91% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 59 | 55,93% | +0,71% | +0,76% | -0,08% | +1,91% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 38 | 50,00% | +0,36% | +0,74% | -0,26% | +1,41% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Tecnico | CALIBRABILE | 53 | 54,72% | +0,33% | +0,67% | -0,45% | +1,51% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Classic technical | CALIBRABILE | 34 | 41,18% | +0,45% | -1,26% | -0,31% | +1,41% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 44,44% | +2,90% | +2,61% | +2,02% | +4,90% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 55 | 40,00% | +1,39% | +0,63% | -1,59% | +4,32% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 58 | 53,45% | +1,17% | +1,07% | -1,75% | +3,93% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 58 | 53,45% | +1,17% | +1,07% | -1,75% | +3,93% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,84% | +1,55% | -1,48% | +3,36% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Tecnico | CALIBRABILE | 52 | 46,15% | +0,35% | +0,68% | -2,02% | +3,00% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Classic technical | CALIBRABILE | 33 | 30,30% | +1,05% | -2,17% | -2,02% | +4,02% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 9 | 44,44% | +2,49% | +2,26% | -0,95% | +6,11% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 53 | 49,06% | +2,39% | +1,75% | -2,41% | +6,72% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 56 | 48,21% | +2,21% | +1,77% | -2,51% | +6,42% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 56 | 48,21% | +2,21% | +1,77% | -2,51% | +6,42% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +2,45% | +3,08% | -2,17% | +5,74% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Tecnico | CALIBRABILE | 50 | 60,00% | +1,17% | +0,91% | -2,95% | +5,39% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Classic technical | CALIBRABILE | 31 | 38,71% | +2,48% | -3,99% | -2,71% | +6,71% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 37,50% | +1,54% | +1,34% | -1,56% | +8,05% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 51 | 58,82% | +2,91% | +3,08% | -2,91% | +8,55% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 54 | 53,70% | +2,92% | +2,47% | -2,99% | +8,30% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 54 | 53,70% | +2,92% | +2,47% | -2,99% | +8,30% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,59% | +4,60% | -2,54% | +8,00% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Tecnico | CALIBRABILE | 48 | 60,42% | +1,58% | +1,61% | -3,54% | +6,88% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Classic technical | CALIBRABILE | 31 | 38,71% | +2,76% | -4,80% | -3,30% | +8,15% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 50,00% | +0,41% | +0,28% | -2,23% | +8,54% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 48 | 58,33% | +2,96% | +4,04% | -3,63% | +9,67% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 51 | 52,94% | +2,88% | +3,18% | -3,67% | +9,48% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 51 | 52,94% | +2,88% | +3,18% | -3,67% | +9,48% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,79% | +5,36% | -2,91% | +9,59% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Tecnico | CALIBRABILE | 45 | 64,44% | +0,92% | +1,77% | -4,34% | +7,15% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Classic technical | CALIBRABILE | 31 | 41,94% | +2,22% | -4,39% | -3,95% | +9,25% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 8 | 62,50% | +0,72% | +0,35% | -3,12% | +9,19% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 46 | 69,57% | +4,99% | +7,03% | -3,97% | +13,31% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 47 | 72,34% | +4,71% | +6,72% | -3,92% | +12,89% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 47 | 72,34% | +4,71% | +6,72% | -3,92% | +12,89% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 38 | 76,32% | +5,76% | +8,06% | -3,33% | +13,70% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Tecnico | CALIBRABILE | 41 | 63,41% | +1,51% | +1,09% | -4,70% | +8,65% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Classic technical | CALIBRABILE | 31 | 48,39% | +3,26% | -3,87% | -4,53% | +11,11% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 57,14% | +7,65% | +2,04% | -2,99% | +15,57% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 39 | 79,49% | +10,08% | +9,06% | -3,22% | +20,42% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 41 | 87,80% | +10,08% | +12,96% | -3,28% | +20,47% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 41 | 87,80% | +10,08% | +12,96% | -3,28% | +20,47% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 38 | 89,47% | +10,54% | +13,52% | -3,55% | +20,95% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Tecnico | CALIBRABILE | 34 | 64,71% | +7,26% | -3,28% | -3,99% | +15,79% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Classic technical | CALIBRABILE | 27 | 55,56% | +7,10% | -7,10% | -3,69% | +15,72% | FEEDBACK RAPIDO |
| DOGE | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 80,00% | +13,05% | +2,29% | +0,50% | +27,01% | FEEDBACK RAPIDO |
| DOGE | 30g | Global confluence | BENCHMARK | 32 | 75,00% | +12,74% | +5,77% | -4,35% | +25,08% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Famiglia statistica | CALIBRABILE | 34 | 88,24% | +13,27% | +11,92% | -4,36% | +25,97% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Scanner grezzo | DIAGNOSTICO | 34 | 88,24% | +13,27% | +11,92% | -4,36% | +25,97% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Market regime grezzo | DIAGNOSTICO | 32 | 93,75% | +12,35% | +14,42% | -4,40% | +25,26% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Tecnico | CALIBRABILE | 30 | 40,00% | +11,60% | -11,60% | -4,76% | +23,68% | PRIMA CALIBRAZIONE |
| DOGE | 30g | Classic technical | CALIBRABILE | 22 | 50,00% | +9,38% | -9,38% | -4,86% | +19,29% | FEEDBACK RAPIDO |
| DOGE | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 75,00% | +30,85% | +15,03% | -1,31% | +42,05% | FEEDBACK RAPIDO |
| DOGE | 45g | Global confluence | BENCHMARK | 18 | 5,56% | +20,48% | -17,95% | -6,13% | +37,64% | FEEDBACK RAPIDO |
| DOGE | 45g | Famiglia statistica | CALIBRABILE | 19 | 15,79% | +20,35% | -12,96% | -6,16% | +37,61% | FEEDBACK RAPIDO |
| DOGE | 45g | Scanner grezzo | DIAGNOSTICO | 19 | 15,79% | +20,35% | -12,96% | -6,16% | +37,61% | FEEDBACK RAPIDO |
| DOGE | 45g | Market regime grezzo | DIAGNOSTICO | 17 | 17,65% | +19,42% | -11,16% | -6,44% | +37,15% | FEEDBACK RAPIDO |
| DOGE | 45g | Tecnico | CALIBRABILE | 19 | 0,00% | +20,35% | -20,35% | -6,16% | +37,61% | FEEDBACK RAPIDO |
| DOGE | 45g | Classic technical | CALIBRABILE | 16 | 0,00% | +20,67% | -20,67% | -5,92% | +37,88% | FEEDBACK RAPIDO |
| DOGE | 45g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +30,17% | +30,17% | -1,85% | +44,37% | FEEDBACK RAPIDO |
| DOGE | 60g | Global confluence | BENCHMARK | 4 | 0,00% | +21,40% | -21,40% | -7,38% | +36,23% | FEEDBACK RAPIDO |
| DOGE | 60g | Famiglia statistica | CALIBRABILE | 4 | 0,00% | +21,40% | -21,40% | -7,38% | +36,23% | FEEDBACK RAPIDO |
| DOGE | 60g | Scanner grezzo | DIAGNOSTICO | 4 | 0,00% | +21,40% | -21,40% | -7,38% | +36,23% | FEEDBACK RAPIDO |
| DOGE | 60g | Market regime grezzo | DIAGNOSTICO | 4 | 0,00% | +21,40% | -21,40% | -7,38% | +36,23% | FEEDBACK RAPIDO |
| DOGE | 60g | Tecnico | CALIBRABILE | 4 | 0,00% | +21,40% | -21,40% | -7,38% | +36,23% | FEEDBACK RAPIDO |
| DOGE | 60g | Classic technical | CALIBRABILE | 4 | 0,00% | +21,40% | -21,40% | -7,38% | +36,23% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 54 | 53,70% | +0,60% | +0,48% | -0,12% | +1,49% | PRIMA CALIBRAZIONE |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 56 | 55,36% | +0,32% | +0,31% | -0,34% | +1,18% | PRIMA CALIBRAZIONE |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 59 | 54,24% | +0,36% | +0,23% | -0,30% | +1,22% | PRIMA CALIBRAZIONE |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +0,27% | +0,39% | -0,30% | +0,87% | PRIMA CALIBRAZIONE |
| SOL | 1g | Tecnico | CALIBRABILE | 58 | 50,00% | +0,32% | +0,30% | -0,38% | +1,15% | PRIMA CALIBRAZIONE |
| SOL | 1g | Classic technical | CALIBRABILE | 42 | 50,00% | +0,49% | +0,45% | -0,33% | +1,40% | PRIMA CALIBRAZIONE |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 53 | 50,94% | +1,25% | +1,12% | +0,29% | +2,32% | PRIMA CALIBRAZIONE |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 55 | 47,27% | +0,88% | +0,44% | -0,08% | +1,71% | PRIMA CALIBRAZIONE |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 58 | 46,55% | +0,86% | +0,40% | -0,08% | +1,76% | PRIMA CALIBRAZIONE |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +0,76% | +0,78% | -0,00% | +1,60% | PRIMA CALIBRAZIONE |
| SOL | 2g | Tecnico | CALIBRABILE | 57 | 43,86% | +0,79% | +0,25% | -0,11% | +1,86% | PRIMA CALIBRAZIONE |
| SOL | 2g | Classic technical | CALIBRABILE | 41 | 51,22% | +0,88% | +0,85% | -0,05% | +1,84% | PRIMA CALIBRAZIONE |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 52 | 57,69% | +1,98% | +1,81% | -1,36% | +4,25% | PRIMA CALIBRAZIONE |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 54 | 50,00% | +1,50% | +0,96% | -1,65% | +3,76% | PRIMA CALIBRAZIONE |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 57 | 49,12% | +1,44% | +0,89% | -1,63% | +3,74% | PRIMA CALIBRAZIONE |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +1,43% | +1,38% | -1,48% | +3,53% | PRIMA CALIBRAZIONE |
| SOL | 3g | Tecnico | CALIBRABILE | 56 | 50,00% | +1,30% | +0,13% | -1,70% | +3,49% | PRIMA CALIBRAZIONE |
| SOL | 3g | Classic technical | CALIBRABILE | 40 | 55,00% | +1,21% | +1,08% | -1,67% | +3,42% | PRIMA CALIBRAZIONE |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 50 | 62,00% | +3,46% | +3,35% | -1,94% | +6,81% | PRIMA CALIBRAZIONE |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 52 | 55,77% | +2,79% | +1,74% | -2,25% | +6,13% | PRIMA CALIBRAZIONE |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 55 | 54,55% | +2,68% | +1,61% | -2,23% | +6,01% | PRIMA CALIBRAZIONE |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +2,66% | +2,88% | -2,09% | +5,82% | PRIMA CALIBRAZIONE |
| SOL | 5g | Tecnico | CALIBRABILE | 54 | 50,00% | +2,68% | -0,27% | -2,38% | +5,91% | PRIMA CALIBRAZIONE |
| SOL | 5g | Classic technical | CALIBRABILE | 38 | 60,53% | +2,00% | +1,85% | -2,31% | +5,14% | PRIMA CALIBRAZIONE |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 48 | 66,67% | +4,81% | +4,92% | -2,34% | +8,71% | PRIMA CALIBRAZIONE |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 50 | 62,00% | +4,03% | +2,76% | -2,65% | +7,98% | PRIMA CALIBRAZIONE |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 53 | 62,26% | +3,80% | +2,61% | -2,66% | +7,75% | PRIMA CALIBRAZIONE |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 34 | 61,76% | +4,35% | +4,41% | -2,45% | +7,76% | PRIMA CALIBRAZIONE |
| SOL | 7g | Tecnico | CALIBRABILE | 52 | 44,23% | +3,76% | -1,07% | -2,82% | +7,68% | PRIMA CALIBRAZIONE |
| SOL | 7g | Classic technical | CALIBRABILE | 36 | 55,56% | +2,20% | +2,25% | -2,84% | +6,10% | PRIMA CALIBRAZIONE |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 45 | 66,67% | +6,69% | +6,86% | -2,63% | +11,03% | PRIMA CALIBRAZIONE |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 47 | 61,70% | +5,83% | +4,85% | -3,03% | +9,96% | PRIMA CALIBRAZIONE |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 50 | 60,00% | +5,46% | +4,57% | -3,05% | +9,60% | PRIMA CALIBRAZIONE |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 34 | 64,71% | +6,91% | +6,75% | -2,80% | +10,27% | PRIMA CALIBRAZIONE |
| SOL | 10g | Tecnico | CALIBRABILE | 49 | 46,94% | +4,87% | -1,99% | -3,25% | +9,18% | PRIMA CALIBRAZIONE |
| SOL | 10g | Classic technical | CALIBRABILE | 33 | 57,58% | +2,16% | +2,27% | -3,34% | +6,77% | PRIMA CALIBRAZIONE |
| SOL | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 80,00% | +3,41% | +3,41% | -2,87% | +9,17% | FEEDBACK RAPIDO |
| SOL | 10g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 14g | Global confluence | BENCHMARK | 41 | 80,49% | +10,31% | +11,20% | -2,57% | +16,04% | PRIMA CALIBRAZIONE |
| SOL | 14g | Famiglia statistica | CALIBRABILE | 43 | 81,40% | +9,74% | +8,79% | -2,93% | +14,78% | PRIMA CALIBRAZIONE |

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

Generato: 2026-09-10 05:33 UTC

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
| BTC | 62 | UTILE | 61 | 17 | 2 | 0 | Famiglia statistica | 1g | 52,46% | +0,37% | campione utile, valutare con prudenza |
| SOL | 62 | PRIMA CALIBRAZIONE | 58 | 24 | 0 | 0 | Tecnico | 1g | 50,00% | +0,30% | prima calibrazione possibile, solo modifiche leggere |
| DOGE | 62 | UTILE | 60 | 25 | 1 | 0 | Famiglia statistica | 1g | 58,33% | +0,50% | campione utile, valutare con prudenza |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Classic technical | 24 | 37,50% | +0,37% | +0,81% | +0,13% | +1,33% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Famiglia statistica | 61 | 52,46% | +0,37% | +0,37% | -0,07% | +0,90% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 1g | BREVE | Microstruttura exchange | 5 | 40,00% | -0,17% | -0,17% | -0,60% | +0,27% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 56 | 39,29% | +0,12% | +0,49% | +0,03% | +1,02% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 2g | BREVE | Classic technical | 24 | 41,67% | +0,55% | +1,18% | +0,59% | +1,89% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Famiglia statistica | 60 | 53,33% | +0,79% | +0,79% | +0,22% | +1,47% | NON AUMENTARE | 0,0 | MEDIA / ALTA |
| BTC | 2g | BREVE | Microstruttura exchange | 5 | 40,00% | +0,73% | +0,73% | +0,13% | +1,27% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 55 | 43,64% | +0,21% | +0,96% | +0,38% | +1,64% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 3g | BREVE | Classic technical | 24 | 41,67% | +0,20% | +1,81% | -0,58% | +3,31% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Famiglia statistica | 59 | 54,24% | +1,18% | +1,18% | -0,98% | +2,79% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 3g | BREVE | Microstruttura exchange | 5 | 40,00% | +0,35% | +0,35% | -1,11% | +1,90% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 54 | 37,04% | -0,09% | +1,47% | -0,81% | +3,05% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 5g | SETTIMANALE | Classic technical | 24 | 50,00% | -1,14% | +3,70% | -1,03% | +5,94% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 57 | 52,63% | +2,08% | +2,08% | -1,51% | +4,39% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 5g | SETTIMANALE | Microstruttura exchange | 4 | 25,00% | -0,34% | -0,34% | -1,71% | +2,56% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 52 | 44,23% | -0,87% | +2,39% | -1,32% | +4,74% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 7g | SETTIMANALE | Classic technical | 23 | 47,83% | -2,72% | +5,29% | -1,15% | +8,39% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 55 | 61,82% | +2,93% | +2,93% | -1,72% | +5,67% | PESO OK | 0,0 | MEDIA |
| BTC | 7g | SETTIMANALE | Microstruttura exchange | 3 | 66,67% | +0,68% | +0,68% | -1,68% | +3,81% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 50 | 44,00% | -1,65% | +3,45% | -1,51% | +6,12% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 10g | SETTIMANALE | Classic technical | 20 | 60,00% | -3,94% | +6,61% | -1,28% | +9,78% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 52 | 67,31% | +3,79% | +3,79% | -2,00% | +6,72% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| BTC | 10g | SETTIMANALE | Microstruttura exchange | 3 | 66,67% | +0,54% | +0,54% | -2,46% | +3,88% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 47 | 48,94% | -1,34% | +4,32% | -1,77% | +7,31% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 14g | SWING | Classic technical | 16 | 43,75% | -4,40% | +7,88% | -1,01% | +11,63% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Famiglia statistica | 48 | 62,50% | +5,67% | +5,67% | -2,12% | +9,08% | PESO OK | 0,0 | MEDIA |
| BTC | 14g | SWING | Microstruttura exchange | 3 | 33,33% | -0,03% | -0,03% | -2,90% | +4,64% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 43 | 58,14% | +0,84% | +6,48% | -1,85% | +9,94% | PESO OK | 0,0 | MEDIA |
| BTC | 21g | SWING | Classic technical | 9 | 11,11% | -15,77% | +18,62% | -0,19% | +21,75% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Famiglia statistica | 41 | 70,73% | +10,34% | +10,34% | -2,20% | +14,07% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| BTC | 21g | SWING | Microstruttura exchange | 1 | 100,00% | +1,21% | +1,21% | -3,06% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Tecnico | 36 | 36,11% | -1,09% | +11,56% | -1,89% | +15,35% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 30g | MEDIO | Classic technical | 4 | 0,00% | -24,06% | +24,06% | -1,55% | +28,48% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Famiglia statistica | 34 | 85,29% | +13,80% | +13,80% | -3,00% | +17,88% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| BTC | 30g | MEDIO | Microstruttura exchange | 1 | 100,00% | +0,16% | +0,16% | -3,06% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Tecnico | 29 | 44,83% | -1,57% | +13,99% | -2,74% | +18,41% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Famiglia statistica | 19 | 100,00% | +22,46% | +22,46% | -3,35% | +26,51% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Microstruttura exchange | 1 | 100,00% | +20,42% | +20,42% | -3,06% | +26,73% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Tecnico | 15 | 33,33% | -7,88% | +22,81% | -2,97% | +26,99% | OSSERVA | 0,0 | BASSA |
| BTC | 60g | MEDIO | Famiglia statistica | 4 | 100,00% | +23,95% | +23,95% | -3,09% | +29,06% | OSSERVA | 0,0 | BASSA |
| BTC | 60g | MEDIO | Tecnico | 3 | 33,33% | -8,86% | +24,18% | -3,03% | +29,15% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 34 | 41,18% | -0,49% | +0,22% | -0,44% | +0,96% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 1g | BREVE | Famiglia statistica | 60 | 58,33% | +0,50% | +0,31% | -0,37% | +1,24% | MANTIENI / OSSERVA | 0,0 | MEDIA / ALTA |
| DOGE | 1g | BREVE | Microstruttura exchange | 9 | 55,56% | +1,78% | +2,13% | +0,65% | +2,81% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 54 | 51,85% | +0,37% | +0,21% | -0,48% | +1,13% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Classic technical | 34 | 41,18% | -1,26% | +0,45% | -0,31% | +1,41% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 2g | BREVE | Famiglia statistica | 59 | 55,93% | +0,76% | +0,71% | -0,08% | +1,91% | PESO OK | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Microstruttura exchange | 9 | 44,44% | +2,61% | +2,90% | +2,02% | +4,90% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 53 | 54,72% | +0,67% | +0,33% | -0,45% | +1,51% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 3g | BREVE | Classic technical | 33 | 30,30% | -2,17% | +1,05% | -2,02% | +4,02% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 3g | BREVE | Famiglia statistica | 58 | 53,45% | +1,07% | +1,17% | -1,75% | +3,93% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 3g | BREVE | Microstruttura exchange | 9 | 44,44% | +2,26% | +2,49% | -0,95% | +6,11% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 52 | 46,15% | +0,68% | +0,35% | -2,02% | +3,00% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 5g | SETTIMANALE | Classic technical | 31 | 38,71% | -3,99% | +2,48% | -2,71% | +6,71% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 56 | 48,21% | +1,77% | +2,21% | -2,51% | +6,42% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 5g | SETTIMANALE | Microstruttura exchange | 8 | 37,50% | +1,34% | +1,54% | -1,56% | +8,05% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 50 | 60,00% | +0,91% | +1,17% | -2,95% | +5,39% | PESO OK | 0,0 | MEDIA |
| DOGE | 7g | SETTIMANALE | Classic technical | 31 | 38,71% | -4,80% | +2,76% | -3,30% | +8,15% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 54 | 53,70% | +2,47% | +2,92% | -2,99% | +8,30% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 7g | SETTIMANALE | Microstruttura exchange | 8 | 50,00% | +0,28% | +0,41% | -2,23% | +8,54% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 48 | 60,42% | +1,61% | +1,58% | -3,54% | +6,88% | PESO OK | 0,0 | MEDIA |
| DOGE | 10g | SETTIMANALE | Classic technical | 31 | 41,94% | -4,39% | +2,22% | -3,95% | +9,25% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 51 | 52,94% | +3,18% | +2,88% | -3,67% | +9,48% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 10g | SETTIMANALE | Microstruttura exchange | 8 | 62,50% | +0,35% | +0,72% | -3,12% | +9,19% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 45 | 64,44% | +1,77% | +0,92% | -4,34% | +7,15% | PESO OK | 0,0 | MEDIA |
| DOGE | 14g | SWING | Classic technical | 31 | 48,39% | -3,87% | +3,26% | -4,53% | +11,11% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 14g | SWING | Famiglia statistica | 47 | 72,34% | +6,72% | +4,71% | -3,92% | +12,89% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 14g | SWING | Microstruttura exchange | 7 | 57,14% | +2,04% | +7,65% | -2,99% | +15,57% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 41 | 63,41% | +1,09% | +1,51% | -4,70% | +8,65% | PESO OK | 0,0 | MEDIA |
| DOGE | 21g | SWING | Classic technical | 27 | 55,56% | -7,10% | +7,10% | -3,69% | +15,72% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Famiglia statistica | 41 | 87,80% | +12,96% | +10,08% | -3,28% | +20,47% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 21g | SWING | Microstruttura exchange | 5 | 80,00% | +2,29% | +13,05% | +0,50% | +27,01% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Tecnico | 34 | 64,71% | -3,28% | +7,26% | -3,99% | +15,79% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 30g | MEDIO | Classic technical | 22 | 50,00% | -9,38% | +9,38% | -4,86% | +19,29% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Famiglia statistica | 34 | 88,24% | +11,92% | +13,27% | -4,36% | +25,97% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 30g | MEDIO | Microstruttura exchange | 4 | 75,00% | +15,03% | +30,85% | -1,31% | +42,05% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Tecnico | 30 | 40,00% | -11,60% | +11,60% | -4,76% | +23,68% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 45g | MEDIO | Classic technical | 16 | 0,00% | -20,67% | +20,67% | -5,92% | +37,88% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Famiglia statistica | 19 | 15,79% | -12,96% | +20,35% | -6,16% | +37,61% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Microstruttura exchange | 2 | 100,00% | +30,17% | +30,17% | -1,85% | +44,37% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Tecnico | 19 | 0,00% | -20,35% | +20,35% | -6,16% | +37,61% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Classic technical | 4 | 0,00% | -21,40% | +21,40% | -7,38% | +36,23% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Famiglia statistica | 4 | 0,00% | -21,40% | +21,40% | -7,38% | +36,23% | OSSERVA | 0,0 | BASSA |
| DOGE | 60g | MEDIO | Tecnico | 4 | 0,00% | -21,40% | +21,40% | -7,38% | +36,23% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Classic technical | 42 | 50,00% | +0,45% | +0,49% | -0,33% | +1,40% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 1g | BREVE | Famiglia statistica | 56 | 55,36% | +0,31% | +0,32% | -0,34% | +1,18% | PESO OK | 0,0 | MEDIA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 58 | 50,00% | +0,30% | +0,32% | -0,38% | +1,15% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Classic technical | 41 | 51,22% | +0,85% | +0,88% | -0,05% | +1,84% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Famiglia statistica | 55 | 47,27% | +0,44% | +0,88% | -0,08% | +1,71% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Microstruttura exchange | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 57 | 43,86% | +0,25% | +0,79% | -0,11% | +1,86% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Classic technical | 40 | 55,00% | +1,08% | +1,21% | -1,67% | +3,42% | PESO OK | 0,0 | MEDIA |
| SOL | 3g | BREVE | Famiglia statistica | 54 | 50,00% | +0,96% | +1,50% | -1,65% | +3,76% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Microstruttura exchange | 5 | 60,00% | +2,46% | +2,46% | -1,34% | +7,31% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 56 | 50,00% | +0,13% | +1,30% | -1,70% | +3,49% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Classic technical | 38 | 60,53% | +1,85% | +2,00% | -2,31% | +5,14% | PESO OK | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 52 | 55,77% | +1,74% | +2,79% | -2,25% | +6,13% | PESO OK | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +2,38% | +2,38% | -1,81% | +7,31% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 54 | 50,00% | -0,27% | +2,68% | -2,38% | +5,91% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Classic technical | 36 | 55,56% | +2,25% | +2,20% | -2,84% | +6,10% | PESO OK | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 50 | 62,00% | +2,76% | +4,03% | -2,65% | +7,98% | PESO OK | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +3,38% | +3,38% | -2,33% | +9,16% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 52 | 44,23% | -1,07% | +3,76% | -2,82% | +7,68% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 10g | SETTIMANALE | Classic technical | 33 | 57,58% | +2,27% | +2,16% | -3,34% | +6,77% | PESO OK | 0,0 | MEDIA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 47 | 61,70% | +4,85% | +5,83% | -3,03% | +9,96% | PESO OK | 0,0 | MEDIA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Microstruttura exchange | 5 | 80,00% | +3,41% | +3,41% | -2,87% | +9,17% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 49 | 46,94% | -1,99% | +4,87% | -3,25% | +9,18% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 14g | SWING | Classic technical | 29 | 55,17% | +1,87% | +3,59% | -3,24% | +8,35% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Famiglia statistica | 43 | 81,40% | +8,79% | +9,74% | -2,93% | +14,78% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 14g | SWING | Frattale SOL | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Microstruttura exchange | 5 | 80,00% | +8,16% | +8,16% | -3,30% | +14,31% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Tecnico | 45 | 42,22% | -4,38% | +7,45% | -3,25% | +12,78% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 21g | SWING | Classic technical | 22 | 40,91% | -9,76% | +11,59% | -4,29% | +15,97% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Famiglia statistica | 36 | 86,11% | +18,74% | +17,19% | -3,75% | +22,71% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 21g | SWING | Frattale SOL | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Microstruttura exchange | 2 | 50,00% | +17,59% | +17,59% | -5,94% | +22,78% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Tecnico | 38 | 34,21% | -13,71% | +13,68% | -4,27% | +19,19% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 30g | MEDIO | Classic technical | 21 | 9,52% | -26,53% | +26,53% | -4,64% | +32,91% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Famiglia statistica | 30 | 90,00% | +24,28% | +24,63% | -4,89% | +31,11% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 30g | MEDIO | Frattale SOL | 1 | 0,00% | -4,50% | -4,50% | -9,39% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Microstruttura exchange | 2 | 100,00% | +22,28% | +22,28% | -5,94% | +27,20% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Tecnico | 32 | 12,50% | -21,52% | +20,94% | -5,31% | +26,83% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 45g | MEDIO | Classic technical | 11 | 0,00% | -36,09% | +36,09% | -6,79% | +45,08% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Famiglia statistica | 15 | 46,67% | +1,21% | +32,78% | -7,60% | +40,59% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Frattale SOL | 1 | 100,00% | +19,26% | +19,26% | -9,39% | +23,73% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Microstruttura exchange | 1 | 100,00% | +32,54% | +32,54% | -9,62% | +40,68% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Tecnico | 19 | 21,05% | -23,13% | +33,49% | -7,44% | +40,99% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Famiglia statistica | 3 | 0,00% | -33,87% | +33,87% | -8,66% | +42,18% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Frattale SOL | 1 | 100,00% | +35,29% | +35,29% | -9,39% | +41,04% | OSSERVA | 0,0 | BASSA |
| SOL | 60g | MEDIO | Tecnico | 4 | 100,00% | +33,90% | +33,90% | -8,78% | +41,99% | OSSERVA | 0,0 | BASSA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 58 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 38 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 61 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Classic technical | 72 | 40,28% | +0,37% |
| BTC | BREVE | Famiglia statistica | 180 | 53,33% | +0,78% |
| BTC | BREVE | Microstruttura exchange | 15 | 40,00% | +0,30% |
| BTC | BREVE | Tecnico | 165 | 40,00% | +0,08% |
| BTC | SETTIMANALE | Classic technical | 67 | 52,24% | -2,52% |
| BTC | SETTIMANALE | Famiglia statistica | 164 | 60,37% | +2,91% |
| BTC | SETTIMANALE | Microstruttura exchange | 10 | 50,00% | +0,23% |
| BTC | SETTIMANALE | Tecnico | 149 | 45,64% | -1,28% |
| BTC | SWING | Classic technical | 25 | 32,00% | -8,49% |
| BTC | SWING | Famiglia statistica | 89 | 66,29% | +7,82% |
| BTC | SWING | Microstruttura exchange | 4 | 50,00% | +0,28% |
| BTC | SWING | Tecnico | 79 | 48,10% | -0,04% |
| BTC | MEDIO | Classic technical | 4 | 0,00% | -24,06% |
| BTC | MEDIO | Famiglia statistica | 57 | 91,23% | +17,40% |
| BTC | MEDIO | Microstruttura exchange | 2 | 100,00% | +10,29% |
| BTC | MEDIO | Tecnico | 47 | 40,43% | -4,05% |
| DOGE | BREVE | Classic technical | 101 | 37,62% | -1,30% |
| DOGE | BREVE | Famiglia statistica | 177 | 55,93% | +0,77% |
| DOGE | BREVE | Microstruttura exchange | 27 | 48,15% | +2,22% |
| DOGE | BREVE | Tecnico | 159 | 50,94% | +0,57% |
| DOGE | SETTIMANALE | Classic technical | 93 | 39,78% | -4,39% |
| DOGE | SETTIMANALE | Famiglia statistica | 161 | 51,55% | +2,45% |
| DOGE | SETTIMANALE | Microstruttura exchange | 24 | 50,00% | +0,65% |
| DOGE | SETTIMANALE | Tecnico | 143 | 61,54% | +1,41% |
| DOGE | SWING | Classic technical | 58 | 51,72% | -5,37% |
| DOGE | SWING | Famiglia statistica | 88 | 79,55% | +9,63% |
| DOGE | SWING | Microstruttura exchange | 12 | 66,67% | +2,15% |
| DOGE | SWING | Tecnico | 75 | 64,00% | -0,89% |
| DOGE | MEDIO | Classic technical | 42 | 26,19% | -14,83% |
| DOGE | MEDIO | Famiglia statistica | 57 | 57,89% | +1,29% |
| DOGE | MEDIO | Microstruttura exchange | 6 | 83,33% | +20,07% |
| DOGE | MEDIO | Tecnico | 53 | 22,64% | -15,47% |
| SOL | BREVE | Classic technical | 123 | 52,03% | +0,79% |
| SOL | BREVE | Famiglia statistica | 165 | 50,91% | +0,57% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 15 | 53,33% | +1,74% |
| SOL | BREVE | Tecnico | 171 | 47,95% | +0,23% |
| SOL | SETTIMANALE | Classic technical | 107 | 57,94% | +2,11% |
| SOL | SETTIMANALE | Famiglia statistica | 149 | 59,73% | +3,07% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Microstruttura exchange | 15 | 66,67% | +3,06% |
| SOL | SETTIMANALE | Tecnico | 155 | 47,10% | -1,08% |
| SOL | SWING | Classic technical | 51 | 49,02% | -3,15% |
| SOL | SWING | Famiglia statistica | 79 | 83,54% | +13,33% |
| SOL | SWING | Frattale SOL | 2 | 0,00% | -3,49% |
| SOL | SWING | Microstruttura exchange | 7 | 71,43% | +10,86% |
| SOL | SWING | Tecnico | 83 | 38,55% | -8,65% |
| SOL | MEDIO | Classic technical | 32 | 6,25% | -29,82% |
| SOL | MEDIO | Famiglia statistica | 48 | 70,83% | +13,43% |
| SOL | MEDIO | Frattale SOL | 3 | 66,67% | +16,68% |
| SOL | MEDIO | Microstruttura exchange | 3 | 100,00% | +25,70% |
| SOL | MEDIO | Tecnico | 55 | 21,82% | -18,05% |

## Aree ancora in attesa

| Asset | Famiglia | Righe senza controlli | Stato |
| --- | --- | --- | --- |
| BTC | BREVE | 3 | in attesa di controlli maturati |
| BTC | SETTIMANALE | 3 | in attesa di controlli maturati |
| BTC | SWING | 2 | in attesa di controlli maturati |
| BTC | MEDIO | 6 | in attesa di controlli maturati |
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
| BTC     |         62 |              34 |          28 | OSSERVAZIONE 30+ | 0,00%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| SOL     |         62 |              34 |          28 | OSSERVAZIONE 30+ | 2,94%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| DOGE    |         62 |              34 |          28 | OSSERVAZIONE 30+ | 5,88%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |

Regola: sotto 60 controlli osserva soltanto; da 100+ controlli può diventare utile per correggere rischio spot/leva nel Decision Report.

## Ultima lettura rapida

| Asset   | Rischio spot   | Rischio leva   | Nota leva                                                               |
|:--------|:---------------|:---------------|:------------------------------------------------------------------------|
| BTC     | BASSO          | MEDIO          | spot preferibile; leva molto pericolosa anche 2x/3x senza margine largo |
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

Generato: 2026-09-10 05:33 UTC


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
| SOL | +5 | MODERATAMENTE POSITIVA | Costruttivo prudente | MEDIA | HOLD / TRANCHE PICCOLE, NO LEVA | Doppio minimo target raggiunto finché mantiene 78,73; nuova conferma tecnica sopra 110,04; milestone analogiche 107,12 / 134,20, valide soltanto se rientra anche il gap frattale. | Allarmi sotto 88,87 / 97,45 / 62,19. |
| DOGE | -4 | NEGATIVA | Ribassista | MEDIA | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE | Sopra 0.09421 migliora; sopra 0.06933 viene invalidato il pattern ribassista dominante. | Sotto 0.08028 il rischio ribassista aumenta. |

## Punteggi per modulo

| Asset | Scanner grezzo | Market grezzo | Famiglia statistica | Scanner path | Tecnico | Classic tech | Frattale SOL | Fractal path | RSI top-cycle | Lifecycle EMA | Exchange flow | Futures | Daily change | Totale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +3 | 0 | +3 | 0 | +2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | +1 | +6 |
| SOL | +2 | 0 | +2 | 0 | +2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | +1 | +5 |
| DOGE | -2 | 0 | -2 | 0 | -1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | -1 | -4 |

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
- Scanner (diagnostico, già incluso nella Famiglia statistica): **+3** — Casi positivi 87,50%, return centrale 30g +37,26%. Direzione scanner: SALITA. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **0** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 0, positivi 30g n/a, return p50 n/a.
- Scanner path: **0** — Controlli disponibili 59. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **+2** — Score tecnico 3/12, verdetto costruttivo ma non confermato, trend misto, struttura rialzista con massimi e minimi crescenti, divergenza nessuna, Wyckoff markup / fase rialzista, pattern score 0 (rialzista Doppio minimo / TARGET RAGGIUNTO; ribassista Doppio massimo / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **0** — Score classico 0/12, verdetto NEUTRALE / MISTO, stage STAGE 3 / DISTRIBUZIONE O PAUSA, struttura VOLATILITÀ IN ESPANSIONE, Wyckoff SIGN OF STRENGTH POSSIBILE, volatilità locale MEDIO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Non applicabile a questo asset.
- Fractal path: **0** — Non applicabile a questo asset.
- RSI top-cycle: **0** — Non applicabile a questo asset.
- Lifecycle EMA: **0** — Non applicabile a questo asset.
- Exchange flow: **0** — Flow +1.75, derivati +0.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +0.00; exchange 3/3, copertura 100%, consenso bull 0, bear 2, divergenze 1, campioni 4h 9 su 4.00h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias LEGGERMENTE POSITIVA / NON PESATA; confidenza BASSA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Misto, forza 1/5.
- Daily change: **+1** — BTC: cambiamento forte in miglioramento rispetto a ieri.

Conferme: Prima resistenza sopra 82.262; conferma del doppio minimo sopra 65.402.

Invalidazioni: Sotto 76.248 il quadro tecnico peggiora.

### SOL

- Confluenza: **MODERATAMENTE POSITIVA**
- Bias: **Costruttivo prudente**
- Punteggio finale: **+5**
- Affidabilità: **MEDIA**
- Azione coerente: **HOLD / TRANCHE PICCOLE, NO LEVA**

SOL ha una confluenza costruttiva, ma va ancora trattato come setup anticipato. La conferma vera arriva solo sopra le resistenze tecniche e con rientro del gap frattale. Il modulo lifecycle/EMA200 resta utile come contesto, ma non aumenta il punteggio Global.

Dettaglio moduli:

- Famiglia statistica: **+2** — Scanner grezzo +2, Market Regime grezzo 0, match regime 0. Regime ignorato: meno di 5 match utili. Punteggio contato nel Global: +2.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **+2** — Casi positivi 62,50%, return centrale 30g +28,93%. Direzione scanner: SALITA. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **0** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 0, positivi 30g n/a, return p50 n/a.
- Scanner path: **0** — Controlli disponibili 59. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **+2** — Score tecnico 6/12, verdetto costruttivo ma non confermato, trend rialzista, struttura rialzista con massimi e minimi crescenti, divergenza nessuna, Wyckoff markup / fase rialzista, pattern score 0 (rialzista Doppio minimo / TARGET RAGGIUNTO; ribassista Doppio massimo / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **0** — Score classico 2/12, verdetto ANTICIPATO / COSTRUTTIVO MA NON CONFERMATO, stage STAGE 3 / DISTRIBUZIONE O PAUSA, struttura COMPRESSIONE / TRIANGOLO POSSIBILE, Wyckoff SIGN OF STRENGTH POSSIBILE, volatilità locale MEDIO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Verdetto ANALOGIA DEBOLE / SCENARIO SECONDARIO, somiglianza strutturale +69,32%, aderenza live +72,09%, errore live +13,95%, gap corrente +11,75%, peso operativo 0, tracking STRUTTURA STABILE, fase FRATTALE SOLO DI CONTESTO, rischio ALTO.
- Fractal path: **0** — Controlli disponibili 56, ma percorso ancorato non aderente: gap +11,75%, errore live +13,95%. Peso 0.
- RSI top-cycle: **0** — Rischio top-cycle RSI: BASSO.
- Lifecycle EMA: **0** — Contesto non pesato nel Global. Lifecycle score 2, bias CONTESTO DA OSSERVARE, EMA200 111,24 $, upside EMA200 +9,03%, gap EMA50/EMA200 -5,73%, hit EMA200 12w +73,33%, trend STABILE / DA CONFERMARE. Peso Global forzato a 0.
- Exchange flow: **0** — Flow +1.75, derivati +0.50, affollamento +0.00, liquidazioni +0.00, conferme tecniche +0.50; exchange 3/3, copertura 100%, consenso bull 1, bear 1, divergenze 0, campioni 4h 9 su 4.00h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias LEGGERMENTE POSITIVA / NON PESATA; confidenza BASSA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Misto, forza 1/5.
- Daily change: **+1** — SOL: cambiamento medio in miglioramento rispetto a ieri.

Conferme: Doppio minimo target raggiunto finché mantiene 78,73; nuova conferma tecnica sopra 110,04; milestone analogiche 107,12 / 134,20, valide soltanto se rientra anche il gap frattale.

Invalidazioni: Allarmi sotto 88,87 / 97,45 / 62,19.

### DOGE

- Confluenza: **NEGATIVA**
- Bias: **Ribassista**
- Punteggio finale: **-4**
- Affidabilità: **MEDIA**
- Azione coerente: **STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE**

DOGE resta l'asset più debole. Anche senza contare due volte Scanner e Market Regime, la confluenza generale resta chiaramente negativa rispetto a BTC e SOL.

Dettaglio moduli:

- Famiglia statistica: **-2** — Scanner grezzo -2, Market Regime grezzo 0, match regime 1. Regime ignorato: meno di 5 match utili. Punteggio contato nel Global: -2.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **-2** — Casi positivi 32,50%, return centrale 30g -11,41%. Direzione scanner: DISCESA. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **0** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 1, positivi 30g 0,00%, return p50 -1,77%.
- Scanner path: **0** — Controlli disponibili 59. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **-1** — Score tecnico -2/12, verdetto neutrale / misto, trend misto, struttura compressione / triangolo, divergenza nessuna, Wyckoff range / fase non chiara, pattern score 0 (rialzista Doppio minimo / TARGET RAGGIUNTO; ribassista Doppio massimo / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **0** — Score classico -4/12, verdetto DEBOLE / NON CONFERMATO, stage STAGE 4 / MARKDOWN, struttura COMPRESSIONE / TRIANGOLO POSSIBILE, Wyckoff ACCUMULO POSSIBILE / RANGE BASSO, volatilità locale MEDIO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Non applicabile a questo asset.
- Fractal path: **0** — Non applicabile a questo asset.
- RSI top-cycle: **0** — Non applicabile a questo asset.
- Lifecycle EMA: **0** — Non applicabile a questo asset.
- Exchange flow: **0** — Flow +1.75, derivati +0.50, affollamento +0.00, liquidazioni +0.00, conferme tecniche +0.50; exchange 3/3, copertura 100%, consenso bull 0, bear 1, divergenze 0, campioni 4h 9 su 4.00h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias LEGGERMENTE POSITIVA / NON PESATA; confidenza BASSA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Misto, forza 1/5.
- Daily change: **-1** — DOGE: cambiamento medio in peggioramento rispetto a ieri.

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

Generato: 2026-09-10 05:33 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [btc_macro_cycle_report.md](btc_macro_cycle_report.md)

Questo modulo descrive il contesto macro di Bitcoin. Non genera entrate tattiche, non autorizza leva e pesa **0** nel Global Confluence.

## Sintesi

| Voce | Valore | Lettura |
| --- | --- | --- |
| Prezzo BTC | 78.468 $ | prezzo corrente |
| Power Law centrale | 125.049 $ | deviazione -37,25% |
| Banda p10-p90 | 77.635 $ / 315.302 $ | BASSA NEL CORRIDOIO |
| Percentile residuo | 10,97% | posizione storica nel corridoio |
| Esponente β | 5,8030 | R² log-log 91,93% |
| Stabilità β | BASSA | range 1,3166 cambiando finestra |
| Ultimo halving | 2024-04-19 | 874 giorni fa |
| Fase ciclo | 59,82% | percentuale indicativa del ciclo quadriennale |
| Peso Global | 0 | CONTESTO MACRO / DIAGNOSTICO |

La Power Law viene trattata come regressione empirica, non come legge fisica. Il report mostra quanto cambia l'esponente usando finestre iniziali diverse e la confronta con il benchmark ingenuo 'prezzo invariato'.

## Bitcoin Power Law

- Campione: 2014-09-17 → 2026-09-10 (4376 osservazioni)
- Formula stimata: prezzo ≈ exp(-39.0531) × giorni^5.8030
- Prezzo centrale oggi: **125.049 $**
- Posizione corrente: **BASSA NEL CORRIDOIO**, percentile 10,97%
- Scarto dal centro: **-37,25%**

![Bitcoin Power Law](btc_power_law_chart.png)

![Bitcoin Power Law log-log](btc_power_law_loglog_chart.png)

### Stabilità dell'esponente

| Inizio campione | β | R² log-log |
| --- | --- | --- |
| 2014 | 5,8030 | 91,93% |
| 2015 | 5,8851 | 91,48% |
| 2016 | 5,5690 | 87,73% |
| 2017 | 4,8415 | 82,92% |
| 2018 | 4,5686 | 78,43% |

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
| 2012-11-28 → 2016-07-09 | 2015-01-26 | -13,17% | -19,76% | +5,57% | +43,40% |
| 2016-07-09 → 2020-05-11 | 2018-10-26 | -38,07% | -44,39% | -15,60% | +42,79% |
| 2020-05-11 → 2024-04-19 | 2022-09-19 | -2,07% | -14,26% | +37,97% | +39,23% |

Campione molto piccolo: questi rendimenti sono contesto di ciclo, non probabilità affidabili.

## SOL/BTC e DOGE/BTC dentro il tempo Bitcoin

![Altcoin nel ciclo BTC](alt_btc_cycle_spirals.png)

| Asset | Coppia | Forza vs BTC | Score raw | Candidato | 30g | Peso Global |
| --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | RELATIVA MISTA / NON CONFERMATA | 3 | 0 | 9.444448037510034 | 0 |
| DOGE | DOGE/BTC | SOTTOPERFORMA BTC | -5 | -1 | 0.4312912908936317 | 0 |

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

Generato: 2026-09-10 05:33 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [relative_strength_btc_report.md](relative_strength_btc_report.md)

Questo modulo controlla se SOL e DOGE stanno davvero battendo Bitcoin. Una salita in USD accompagnata da una coppia ALT/BTC ribassista è spesso soltanto trascinamento di BTC.

**Protezione iniziale:** il candidato relativo è limitato a -1/0/+1, ma il peso nel Global resta **0**. La coppia BTC conferma o indebolisce il tecnico USD; non viene sommata come secondo modulo indipendente.

## Sintesi

| Asset | Coppia | Prezzo | Score raw | Candidato | Peso Global | Forza vs BTC | Confidenza | 30g | Tecnico USD | Lettura combinata |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | 0.00130020 | +3 | 0 | 0 | RELATIVA MISTA / NON CONFERMATA | BASSA | +9,44% | RIALZISTA | QUADRO MISTO / NESSUNA CONFERMA RELATIVA |
| DOGE | DOGE/BTC | 0.00000110 | -5 | -1 | 0 | SOTTOPERFORMA BTC | MEDIA | +0,43% | MISTA | FORZA RELATIVA NEGATIVA, USD ANCORA MISTO |

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
- **Struttura:** MASSIMI E MINIMI CRESCENTI
- **Rendimenti relativi:** 7g +0,17%; 30g +9,44%; 90g +23,71%; 180g +4,69%
- **Daily:** RSI 56.48; MA50 0.00121818; MA200 0.00118292
- **Weekly:** MA30 0.00118811; RSI 55.98
- **Livelli:** supporto 0.00127500; resistenza 0.00134900; breakout 60g 0.00136900; breakdown 60g 0.00112700
- **Pattern:** DOPPIO MINIMO / TARGET RAGGIUNTO; neckline 0.00120200; target 0.00125350
- **Fibonacci:** VICINO — 23.6% a 0.00128404
- **Fonte:** Yahoo Finance SOL-BTC (coppia diretta)
- **Motivi score:** prezzo sopra MA50 daily; prezzo sopra MA200 daily; MA50 daily in salita; prezzo sopra MA30 weekly; MA30 weekly in discesa; struttura con massimi/minimi crescenti; MACD relativo negativo

![Grafico SOL/BTC](relative_strength_SOLBTC.png)

## DOGE/BTC

- **Verdetto relativo:** SOTTOPERFORMA BTC (-5)
- **Candidato futuro:** -1; **peso attuale Global: 0**
- **Lettura combinata USD/BTC:** FORZA RELATIVA NEGATIVA, USD ANCORA MISTO
- **Struttura:** MASSIMI E MINIMI DECRESCENTI
- **Rendimenti relativi:** 7g +3,69%; 30g +0,43%; 90g -19,04%; 180g -19,00%
- **Daily:** RSI 47.89; MA50 0.00000110; MA200 0.00000126
- **Weekly:** MA30 0.00000126; RSI 38.99
- **Livelli:** supporto 0.00000105; resistenza 0.00000114; breakout 60g 0.00000131; breakdown 60g 0.00000099
- **Pattern:** DOPPIO MINIMO / TARGET RAGGIUNTO; neckline 0.00000115; target 0.00000128
- **Fibonacci:** VICINO — 23.6% a 0.00000112
- **Fonte:** Rapporto sintetico DOGE-USD / BTC-USD (sintetica)
- **Motivi score:** prezzo sotto MA50 daily; prezzo sotto MA200 daily; MA50 daily in discesa; prezzo sotto MA30 weekly; MA30 weekly in discesa; struttura con massimi/minimi decrescenti; MACD relativo positivo

![Grafico DOGE/BTC](relative_strength_DOGEBTC.png)

## Backtest storico diagnostico

Il backtest usa soltanto indicatori disponibili alla data del segnale e campiona una volta a settimana. È utile subito, ma non sostituisce il tracker live: le soglie sono state definite prima di vedere il risultato.

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto direzione | Return futuro mediano |
| --- | --- | --- | --- | --- | --- |
| SOL | 7g | 207 | 52,17% | +1,95% | -1,06% |
| SOL | 30g | 204 | 47,06% | +4,50% | +0,44% |
| SOL | 90g | 199 | 52,76% | +9,91% | +3,03% |
| DOGE | 7g | 294 | 55,78% | +1,84% | -1,68% |
| DOGE | 30g | 294 | 53,06% | +1,97% | -3,49% |
| DOGE | 90g | 286 | 53,85% | +6,84% | -8,85% |

## Tracker live e gate futuro

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto | Stato | Peso Global |
| --- | --- | --- | --- | --- | --- | --- |
| SOL | 1g | 35 | 54,29% | +0,13% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 3g | 33 | 54,55% | +0,50% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 7g | 31 | 48,39% | +0,70% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 14g | 24 | 41,67% | +0,31% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 30g | 15 | 0,00% | -12,60% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 1g | 46 | 67,39% | -0,10% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 3g | 46 | 56,52% | -0,14% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 7g | 44 | 56,82% | -0,16% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 14g | 37 | 70,27% | +0,19% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 30g | 32 | 62,50% | +0,21% | LOCKED / RACCOLTA LIVE | 0 |

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

Ultima candela SOL usata: **10 settembre 2026**

## SOL PRICE CONTEXT

| Voce | Valore | Provenienza / significato |
| --- | --- | --- |
| Anchor computazionale | 102,02 $ | 2026-09-10T05:30:23Z \| Yahoo Finance daily shared snapshot \| Close 1d |
| Candela anchor completata | NO | Stato esplicito; il valore non viene sostituito dal prezzo pubblico. |
| Riferimento pubblico corrente | 102,07 $ | 2026-09-10T05:32:00Z \| Yahoo Finance \| solo display |
| Età anchor alla generazione | 0h 1m | WITHIN_DAILY_REPORT_CADENCE |
| Gap corrente vs anchor | 0,05000 $ | +0,05% |
| Validità input modello | REPRODUCIBLE_SHARED_SNAPSHOT | Non è una dichiarazione di validità del segnale/trading. |

```text
COMPUTATIONAL_ANCHOR_PRICE=102.0199966430664
COMPUTATIONAL_ANCHOR_FIELD=Close
COMPUTATIONAL_ANCHOR_TIMESTAMP=2026-09-10T05:30:23Z
COMPUTATIONAL_ANCHOR_SYMBOL=SOL-USD
COMPUTATIONAL_ANCHOR_PROVIDER=Yahoo Finance daily shared snapshot
COMPUTATIONAL_ANCHOR_TIMEFRAME=1d
COMPUTATIONAL_ANCHOR_COMPLETED=NO
CURRENT_PUBLIC_REFERENCE_PRICE=102.06999969482422
CURRENT_PUBLIC_REFERENCE_TIMESTAMP=2026-09-10T05:32:00Z
CURRENT_PUBLIC_REFERENCE_ACQUIRED_AT=2026-09-10T05:32:16Z
CURRENT_PUBLIC_REFERENCE_SYMBOL=SOL-USD
CURRENT_PUBLIC_REFERENCE_PROVIDER=Yahoo Finance
CURRENT_PUBLIC_REFERENCE_FIELD=Close
CURRENT_PUBLIC_REFERENCE_TIMEFRAME=1m
CURRENT_PUBLIC_REFERENCE_STATUS=AVAILABLE
ANCHOR_AGE_SECONDS=113.674443
ANCHOR_AGE_HOURS=0.03157623416666667
CURRENT_VS_ANCHOR_GAP_USD=0.0500030517578125
CURRENT_VS_ANCHOR_GAP_PCT=0.049012990985253246
```

## Verdetto: ANALOGIA DEBOLE / SCENARIO SECONDARIO

- **Fase attuale:** FRATTALE SOLO DI CONTESTO
- **Somiglianza totale:** +69,32%
- **Somiglianza strutturale:** +69,32%
- **Aderenza prezzo live:** +72,09%
- **Errore medio live:** +13,95%
- **Gap prezzo corrente:** +11,75%
- **Peso operativo suggerito:** 0
- **Affidabilita:** BASSA
- **Rischio fase:** ALTO
- **Trend tracking:** STRUTTURA STABILE
- **Sintesi:** Esistono alcuni elementi comuni, ma non abbastanza per una conferma.
- **SOL è al giorno:** 96 dal bottom usato.
- **Giorno BTC equivalente:** 2023-02-25
- **Prossimo step:** Proiezione condizionale, non conferma operativa: **Fase negativa / rischio discesa.** Zona bassa **88,87 $** intorno al **23 settembre 2026**; zona alta **104,09 $** intorno al **14 settembre 2026**; fine step circa **90,83 $** entro il **24 settembre 2026**.

### Metadata aderenza prezzo

```text
OPERATIONAL_VERDICT_REASON=ANALOGIA DEBOLE / SCENARIO SECONDARIO
PRICE_ADHERENCE_FAILED=NO
PRICE_ADHERENCE_LIVE_AVG_GAP_FAILED=NO
PRICE_ADHERENCE_LAST_GAP_FAILED=NO
PRICE_ADHERENCE_LIVE_AVG_GAP_THRESHOLD_PCT=15.0
PRICE_ADHERENCE_LAST_GAP_THRESHOLD_PCT=18.0
PRICE_ADHERENCE_OBSERVED_LIVE_AVG_GAP_PCT=13.952892453891506
PRICE_ADHERENCE_OBSERVED_LAST_GAP_PCT=11.749804668889553
```

## Somiglianza prima e dopo inizio programma

Questa sezione separa la somiglianza della forma dall'aderenza reale del prezzo.

- **Inizio programma/scanner:** 3 luglio 2026
- **Prima del programma** = backtest retroattivo.
- **Da inizio programma** = verifica live: è la parte più importante per l'uso operativo.

| Periodo | Date | Giorni | Aderenza prezzo | Errore medio | Gap ultimo | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| Prima del programma | 6 giugno 2026 -> 2 luglio 2026 | 27 | +87,95% | +6,02% | +21,89% | ABBASTANZA ALLINEATO |
| Da inizio programma | 3 luglio 2026 -> 10 settembre 2026 | 70 | +72,09% | +13,95% | +11,75% | DEVIAZIONE MODERATA |
| Totale dal bottom | 6 giugno 2026 -> 10 settembre 2026 | 97 | +76,51% | +11,75% | +11,75% | DEVIAZIONE MODERATA |

Nota: un frattale può avere una forma simile ma un prezzo distante. In quel caso non è operativo finché il gap non rientra.

## Lettura operativa veloce

Il frattale resta non operativo. Motivo effettivo: ANALOGIA DEBOLE / SCENARIO SECONDARIO.

| Voce | Risposta | Perché |
| --- | --- | --- |
| Uso operativo | NO | Peso 0 per il verdetto: ANALOGIA DEBOLE / SCENARIO SECONDARIO. |
| Aderenza live | +72,09% | Errore medio live +13,95%. |
| Gap corrente | +11,75% | Metrica separata dal motivo del verdetto. |
| Prima conferma prezzo | 107,12 $ | Serve anche miglioramento del gap, non solo una candela sopra il livello. |
| Seconda conferma | 134,20 $ | Rende più credibile il percorso, ma non sostituisce l'aderenza. |
| Invalidazione soft | 88,87 $ | Sotto questa zona il quadro peggiora. |
| Invalidazione forte | 62,19 $ | Sotto il bottom il paragone è quasi rotto. |

## Target ciclo fino al top BTC 2025

| Voce | Valore |
| --- | --- |
| Stato | CONTESTO / NON OPERATIVO |
| Top BTC 2025 | 6 ottobre 2025 - 124.753 $ |
| Data SOL equivalente | 21 aprile 2029 |
| Target ciclo base dall'anchor modello | 549,17 $ |
| Massimo percorso base | 549,17 $ (21 aprile 2029) |

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
| Prima conferma | 107,12 $ | Deve accompagnarsi al rientro del gap. |
| Seconda conferma | 134,20 $ | Scenario più credibile. |
| Invalidazione soft | 88,87 $ | Il frattale si indebolisce. |
| Invalidazione forte | 62,19 $ | Il paragone si rompe. |

## Proiezione veloce con date SOL

| Orizzonte | Data SOL | BTC fece | SOL base | Min percorso | Max percorso |
| --- | --- | --- | --- | --- | --- |
| 7 giorni | 17 settembre 2026 | -3,55% | 98,40 $ | 98,40 $ | 104,09 $ |
| 14 giorni | 24 settembre 2026 | -10,97% | 90,83 $ | 88,87 $ | 104,09 $ |
| 30 giorni | 10 ottobre 2026 | +17,11% | 119,47 $ | 88,87 $ | 124,73 $ |
| 60 giorni | 9 novembre 2026 | +22,64% | 125,12 $ | 88,87 $ | 134,20 $ |
| 90 giorni | 9 dicembre 2026 | +15,29% | 117,62 $ | 88,87 $ | 134,20 $ |
| 120 giorni | 8 gennaio 2027 | +31,52% | 134,18 $ | 88,87 $ | 135,12 $ |

## Prossimi step se SOL segue BTC 2022

| Step | Date SOL | BTC fine | SOL zona bassa | SOL zona alta | SOL fine base | Lettura |
| --- | --- | --- | --- | --- | --- | --- |
| Step 1 - prossime 2 settimane | 10 settembre 2026 -> 24 settembre 2026 | -10,97% | 88,87 $ (23 settembre 2026) | 104,09 $ (14 settembre 2026) | 90,83 $ | Fase negativa / rischio discesa. |
| Step 2 - primo mese | 25 settembre 2026 -> 10 ottobre 2026 | +17,11% | 97,57 $ (25 settembre 2026) | 124,73 $ (6 ottobre 2026) | 119,47 $ | Prima retest / debolezza, poi recupero. |
| Step 3 - secondo mese | 11 ottobre 2026 -> 9 novembre 2026 | +22,64% | 120,04 $ (11 ottobre 2026) | 134,20 $ (28 ottobre 2026) | 125,12 $ | Spinta rialzista abbastanza pulita. |
| Step 4 - terzo mese | 10 novembre 2026 -> 9 dicembre 2026 | +15,29% | 115,93 $ (7 dicembre 2026) | 130,01 $ (18 novembre 2026) | 117,62 $ | Spinta rialzista abbastanza pulita. |

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
| Prezzo SOL | 102,02 $ |  |
| Weekly RSI | 57,01 / linea grezza 52,24 | LINEA NON AFFIDABILE / RISCHIO NON ATTIVO — IRREALISTICA / NON OPERATIVA |
| Monthly RSI | 46,80 / linea grezza 55,48 | RSI TROPPO BASSO PER RISCHIO TOP — VALIDA / USO PRUDENTE |
| Target ciclo base | 549,17 $ | Avanzamento +18,58% |
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
| Score on-chain | 4 |
| Bias | POSITIVA |
| Azione coerente | CONFERMA MODERATA / BUONO SE IL FRATTALE REGGE |
| Prezzo SOL | 102,02 $ |
| TVL Solana | 5,86 mld $ |
| TVL 7g | +2,37% |
| DEX volume 24h | 2,56 mld $ |
| Fees 24h | 15,57 mln $ |
| Stablecoin su Solana | 16,51 mld $ |
| Stake ratio | 69,22% |
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
| Prezzo SOL | 102,02 $ |
| EMA200 weekly target | 111,24 $ |
| Upside verso EMA200 | +9,03% |
| Distanza prezzo da EMA200 | -8,28% |
| Gap EMA50/EMA200 | -5,73% |
| Stato cross | EMA50 SOTTO EMA200 |
| RSI weekly | 57,01 |
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

<!-- Generato: 2026-09-10 05:32 UTC -->
<!-- MAJOR_ALT_LIFECYCLE_SQUEEZE_END -->

</details>
<!-- COMPACT_SECTION_END:major_alt_lifecycle -->

# Report giornaliero BTC / SOL / DOGE

Aggiornato il: **2026-09-10 05:30:23 UTC**

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
- SOL: cambiamento importante in miglioramento rispetto a ieri.
- DOGE: cambiamento importante in peggioramento rispetto a ieri.

| Asset | Cambio | Tono | Verdetto oggi | Casi positivi oggi | Δ casi positivi |
| --- | --- | --- | --- | --- | --- |
| BTC | CAMBIAMENTO FORTE | miglioramento | RIALZISTA | +87.50% | +7.50 punti |
| SOL | CAMBIAMENTO MEDIO | miglioramento | RIALZISTA | +62.50% | 0.00 punti |
| DOGE | CAMBIAMENTO MEDIO | peggioramento | RIBASSISTA | +32.50% | -5.00 punti |

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
| BTC | 74.534 $ | 86.302 $ | +77,78% | +15,79% | buona zona storica di rimbalzo | 86.302 $ | 74.534 $ | +10,81% | -13,64% | spike storicamente più resistente |
| SOL | 96,92 $ | 112,22 $ | +53,85% | +15,79% | rimbalzo possibile | 112,22 $ | 96,92 $ | +24,14% | -13,64% | spike storicamente più resistente |
| DOGE | 0,08163 $ | 0,09452 $ | +21,88% | +15,79% | rimbalzo poco frequente | 0,09452 $ | 0,08163 $ | +55,00% | -13,64% | attenzione a prendere profitto |

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

- **BTC: su 40 casi simili, 18 prima sono scesi a -5,00%. Tra quei 18, 14 poi sono rimbalzati fino a +10,00%. Percentuale: +77,78% (14/18). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: buona zona storica di rimbalzo.**
- **BTC: su 40 casi simili, 37 prima sono saliti a +10,00%. Tra quei 37, 4 poi sono scaricati a -5,00%. Percentuale: +10,81% (4/37). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.**
- **SOL: su 40 casi simili, 26 prima sono scesi a -5,00%. Tra quei 26, 14 poi sono rimbalzati fino a +10,00%. Percentuale: +53,85% (14/26). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo possibile.**
- **SOL: su 40 casi simili, 29 prima sono saliti a +10,00%. Tra quei 29, 7 poi sono scaricati a -5,00%. Percentuale: +24,14% (7/29). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.**
- **DOGE: su 40 casi simili, 32 prima sono scesi a -5,00%. Tra quei 32, 7 poi sono rimbalzati fino a +10,00%. Percentuale: +21,88% (7/32). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.**
- **DOGE: su 40 casi simili, 20 prima sono saliti a +10,00%. Tra quei 20, 11 poi sono scaricati a -5,00%. Percentuale: +55,00% (11/20). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: attenzione a prendere profitto.**

<!-- BOUNCE_AFTER_DRAWDOWN_END -->

</details>
<!-- COMPACT_SECTION_END:bounce_after_drawdown -->

<!-- COMPACT_SECTION_START:scanner_forecast -->
<details>
<summary><strong>🔭 Cono probabilistico dello scanner</strong></summary>

<!-- SCANNER_FORECAST_TRACKER_START -->
# Scanner forecast path / cono probabilistico

Generato: 2026-09-10 05:31:55 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [scanner_forecast_tracker_report.md](scanner_forecast_tracker_report.md)

## Snapshot effettivamente usato

| Asset   | Snapshot prezzo   | Generazione snapshot prezzo   | Snapshot match scanner   |
|:--------|:------------------|:------------------------------|:-------------------------|
| BTC | 2026-09-10 | 2026-09-10T05:30:23Z | 2026-09-10 05:30:23 |
| SOL | 2026-09-10 | 2026-09-10T05:30:23Z | 2026-09-10 05:30:23 |
| DOGE | 2026-09-10 | 2026-09-10T05:30:23Z | 2026-09-10 05:30:23 |

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
| BTC | 2026-09-10 | 78.457 $ | SALITA | 87,50% | 53.379,54 $ | 91.371,96 $ | 107.687,94 $ | 122.570,83 $ | 148.571,98 $ |
| SOL | 2026-09-10 | 102,02 $ | SALITA | 62,50% | 71,85 $ | 87,77 $ | 131,54 $ | 158,39 $ | 208,12 $ |
| DOGE | 2026-09-10 | 0.08593 $ | DISCESA | 32,50% | 0.06310 $ | 0.06662 $ | 0.07613 $ | 0.09062 $ | 0.12620 $ |

## Confronto raw / regime-adjusted

Il cono raw continua a usare i 40 casi dello scanner. Il cono regime-adjusted sceglie una sola coorte nella gerarchia SAME_BTC_AND_ASSET_REGIME → SAME_ASSET_REGIME → SAME_BTC_REGIME. Ogni livello richiede almeno 5 match; le coorti non vengono mai combinate e ogni fallback è dichiarato.

| Asset   | Stato adjusted              | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level        | selection_reason              | Raw p50 30g   | Adjusted p50 30g   | Raw p90 30g   | Adjusted p90 30g   |
|:--------|:----------------------------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:----------------------|:------------------------------|:--------------|:-------------------|:--------------|:-------------------|
| BTC | INSUFFICIENT_REGIME_MATCHES | NONE | 0 | 4 | 0 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES | 107.687,94 $ | n/a | 148.571,98 $ | n/a |
| SOL | INSUFFICIENT_REGIME_MATCHES | NONE | 0 | 4 | 0 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES | 131,54 $ | n/a | 208,12 $ | n/a |
| DOGE | AVAILABLE | SAME_ASSET_REGIME | 1 | 18 | 1 | 18 | 5 | 1_SAME_ASSET_FALLBACK | FALLBACK_TO_SAME_ASSET_REGIME | 0.07613 $ | 0.07952 $ | 0.12620 $ | 0.11030 $ |

## Grafici

### BTC

![Scanner forecast BTC](scanner_forecast_BTC.png)

#### Verifica storica e discrepanza

![Verifica storica cono BTC](scanner_forecast_history_BTC.png)

- Cono congelato il **2026-08-11**; verificato fino al **2026-09-10**; stato **COMPLETO 30/30g**.
- Reale **78.486,64 $**; p50 previsto **69.830,06 $**; scarto **12,40%**.
- Errore medio assoluto **10,81%**; massimo **19,61%**; DENTRO p10-p90; FUORI p25-p75.

#### Cono regime-adjusted

Gruppo selezionato: **NONE**; fallback: **NONE**; motivo: **INSUFFICIENT_REGIME_MATCHES**.

Non disponibile: INSUFFICIENT_REGIME_MATCHES (campione selezionato 0/5 match).

### SOL

![Scanner forecast SOL](scanner_forecast_SOL.png)

#### Verifica storica e discrepanza

![Verifica storica cono SOL](scanner_forecast_history_SOL.png)

- Cono congelato il **2026-08-11**; verificato fino al **2026-09-10**; stato **COMPLETO 30/30g**.
- Reale **102,09 $**; p50 previsto **84,70 $**; scarto **20,53%**.
- Errore medio assoluto **18,11%**; massimo **37,03%**; DENTRO p10-p90; FUORI p25-p75.

#### Cono regime-adjusted

Gruppo selezionato: **NONE**; fallback: **NONE**; motivo: **INSUFFICIENT_REGIME_MATCHES**.

Non disponibile: INSUFFICIENT_REGIME_MATCHES (campione selezionato 0/5 match).

### DOGE

![Scanner forecast DOGE](scanner_forecast_DOGE.png)

#### Verifica storica e discrepanza

![Verifica storica cono DOGE](scanner_forecast_history_DOGE.png)

- Cono congelato il **2026-08-11**; verificato fino al **2026-09-10**; stato **COMPLETO 30/30g**.
- Reale **0.08592 $**; p50 previsto **0.08085 $**; scarto **6,27%**.
- Errore medio assoluto **13,00%**; massimo **36,33%**; DENTRO p10-p90; DENTRO p25-p75.

#### Cono regime-adjusted

Gruppo selezionato: **SAME_ASSET_REGIME**; fallback: **1_SAME_ASSET_FALLBACK**; motivo: **FALLBACK_TO_SAME_ASSET_REGIME**.

**WARNING:** coorte fallback meno stringente rispetto a SAME_BTC_AND_ASSET_REGIME.

![Scanner forecast regime-adjusted DOGE](scanner_forecast_DOGE_regime_adjusted.png)

## Accuratezza percorso scanner

| Asset   | Giorno   |   Controlli | Dentro p10-p90   | Dentro p25-p75   | Errore medio abs vs p50   | Errore medio vs p50   |
|:--------|:---------|------------:|:-----------------|:-----------------|:--------------------------|:----------------------|
| BTC | 1g | 59 | 93,22% | 66,10% | 2,10% | 0,55% |
| BTC | 3g | 55 | 90,91% | 70,91% | 3,24% | 1,05% |
| BTC | 7g | 47 | 89,36% | 70,21% | 5,42% | 2,68% |
| BTC | 14g | 37 | 97,30% | 64,86% | 6,56% | 3,96% |
| BTC | 30g | 23 | 100,00% | 91,30% | 8,90% | 3,16% |
| SOL | 1g | 59 | 79,66% | 59,32% | 2,84% | 1,08% |
| SOL | 3g | 55 | 89,09% | 72,73% | 4,09% | 2,01% |
| SOL | 7g | 47 | 87,23% | 70,21% | 5,79% | 4,20% |
| SOL | 14g | 37 | 81,08% | 64,86% | 8,61% | 7,61% |
| SOL | 30g | 23 | 91,30% | 47,83% | 15,48% | 14,92% |
| DOGE | 1g | 59 | 86,44% | 59,32% | 3,34% | 0,83% |
| DOGE | 3g | 55 | 89,09% | 67,27% | 4,73% | 2,26% |
| DOGE | 7g | 47 | 74,47% | 72,34% | 9,06% | 6,59% |
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

<!-- FORECAST_30D_HISTORY_START -->

---

# Storico previsioni 30 giorni

Report separato completo: [forecast_30d_history.md](forecast_30d_history.md)

Righe salvate nello storico: **174**.

Questa sezione tiene un diario delle previsioni giornaliere a 30 giorni, senza appesantire il report principale.

| Data | Asset | Prezzo | Direzione | Casi positivi | Return p50 | Drawdown p50 | Max gain p50 | Controllo 30g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-09-10 | BTC | 78.457 $ | SALITA | 87,50% | 107.688 $ | 76.155 $ | 110.885 $ | 2026-10-10 |
| 2026-09-10 | DOGE | 0,09000 $ | DISCESA | 32,50% | 0,08000 $ | 0,07000 $ | 0,09000 $ | 2026-10-10 |
| 2026-09-10 | SOL | 102,02 $ | SALITA | 62,50% | 131,54 $ | 92,18 $ | 141,22 $ | 2026-10-10 |

<!-- FORECAST_30D_HISTORY_END -->

</details>
<!-- COMPACT_SECTION_END:scanner_forecast -->

<!-- COMPACT_SECTION_START:extreme_cases -->
<details>
<summary><strong>⚠️ Percorso dei casi estremi</strong></summary>

<!-- EXTREME_CASES_PATH_START -->
# Extreme cases path report

Generato: 2026-09-10 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [extreme_cases_path_report.md](extreme_cases_path_report.md)

Questo report si attiva quando i casi positivi o negativi sono almeno **80%**.

Ora misura anche il **rialzo massimo prima della discesa principale**, quindi distingue uno spike iniziale da una discesa quasi immediata.

## Trigger estremi

| Asset   | Direzione            | Trigger   | Percentuale   | Motivo                           |   Match disponibili |
|:--------|:---------------------|:----------|:--------------|:---------------------------------|--------------------:|
| BTC     | POSITIVO / RIALZISTA | SI        | +87,50%       | Casi positivi 87.50% >= 80%      |                  40 |
| SOL     | NESSUNO              | NO        | +62,50%       | Nessun lato sopra soglia estrema |                  40 |
| DOGE    | NESSUNO              | NO        | +67,50%       | Nessun lato sopra soglia estrema |                  40 |

## BTC — casi rialzisti

- Trigger: **Casi positivi 87.50% >= 80%**
- Casi usati nei grafici: **35**
- Return mediano 7g: **+5,48%**
- Return mediano 14g: **+14,39%**
- Return mediano 30g: **+39,60%**
- Drawdown mediano: **-1,96%**
- Max gain mediano: **+43,15%**

### Quanto salivano prima di scendere

- Spike massimo mediano prima del minimo: **+0,00%**
- Spike massimo medio prima del minimo: **+2,62%**
- Spike p75 prima del minimo: **+1,23%**
- Giorno mediano dello spike: **giorno 0**
- Giorno mediano del minimo: **giorno 1**
- Scarico mediano dal picco al minimo: **-3,26%**
- Casi con almeno +5% prima del minimo: **+11,43%**
- Casi con almeno +10% prima del minimo: **+8,57%**
- Casi con almeno +15% prima del minimo: **+8,57%**
- Discesa quasi immediata: **+68,57%**

Un segnale ribassista a 30 giorni non significa necessariamente discesa immediata: alcuni casi fanno prima uno spike e poi scaricano.

### Distribuzione 30 giorni

| P10     | P25     | P50     | P75     | P90     |
|:--------|:--------|:--------|:--------|:--------|
| +12,59% | +23,68% | +39,60% | +61,15% | +90,27% |

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
| XLM-USD         | 2020-12-11 | +90,75%      | +26,60%                  |              5 | -16,34%      |              12 | -33,92%          | +91,00%      | SPIKE PRIMA DEL DUMP    |
| ADA-USD         | 2020-12-11 | +86,28%      | +20,18%                  |              5 | -2,19%       |              12 | -18,61%          | +118,64%     | ECCEZIONE POSITIVA      |
| DASH-USD        | 2020-12-11 | +84,66%      | +17,30%                  |              9 | -6,83%       |              22 | -20,57%          | +58,96%      | ECCEZIONE POSITIVA      |
| INJ-USD         | 2023-11-13 | +88,99%      | +9,93%                   |              2 | -7,66%       |               8 | -16,00%          | +89,19%      | ECCEZIONE POSITIVA      |
| BTC-USD         | 2019-04-21 | +86,56%      | +4,85%                   |              2 | -1,96%       |               4 | -6,49%           | +49,84%      | ECCEZIONE POSITIVA      |
| QTUM-USD        | 2023-11-16 | +85,17%      | +3,34%                   |              4 | -5,87%       |               5 | -8,91%           | +3,09%       | ECCEZIONE POSITIVA      |
| 1INCH-USD       | 2023-11-23 | +87,81%      | +3,34%                   |              2 | -4,97%       |               7 | -8,04%           | +17,36%      | ECCEZIONE POSITIVA      |
| ZIL-USD         | 2023-11-23 | +84,88%      | +2,25%                   |              2 | -1,34%       |               4 | -3,51%           | +21,53%      | DISCESA QUASI IMMEDIATA |
| DOGE-USD        | 2019-04-21 | +85,36%      | +1,38%                   |              1 | -10,65%      |               8 | -11,87%          | +11,81%      | ECCEZIONE POSITIVA      |
| ZEC-USD         | 2019-04-21 | +86,28%      | +1,09%                   |              1 | -17,25%      |              18 | -18,15%          | +9,64%       | ECCEZIONE POSITIVA      |
| BCH-USD         | 2019-04-21 | +87,36%      | +0,80%                   |              1 | -18,54%      |               8 | -19,19%          | +43,74%      | ECCEZIONE POSITIVA      |
| ETC-USD         | 2019-04-21 | +83,88%      | +0,49%                   |              2 | -8,95%       |               4 | -9,40%           | +25,82%      | DISCESA QUASI IMMEDIATA |
| BNB-USD         | 2019-02-25 | +88,99%      | +0,00%                   |              0 | -3,26%       |               1 | -3,26%           | +70,51%      | DISCESA QUASI IMMEDIATA |
| THETA-USD       | 2023-11-25 | +88,16%      | +0,00%                   |              0 | -6,15%       |               2 | -6,15%           | +39,60%      | DISCESA QUASI IMMEDIATA |
| ADA-USD         | 2023-11-21 | +87,50%      | +0,00%                   |              0 | +0,00%       |               0 | +0,00%           | +77,51%      | DISCESA QUASI IMMEDIATA |
| ETC-USD         | 2023-11-21 | +87,23%      | +0,00%                   |              0 | +0,00%       |               0 | +0,00%           | +13,76%      | DISCESA QUASI IMMEDIATA |
| EGLD-USD        | 2023-11-21 | +87,13%      | +0,00%                   |              0 | +0,00%       |               0 | +0,00%           | +55,32%      | DISCESA QUASI IMMEDIATA |
| XRP-USD         | 2023-11-21 | +86,62%      | +0,00%                   |              0 | +0,00%       |               0 | +0,00%           | +7,49%       | DISCESA QUASI IMMEDIATA |
| MANA-USD        | 2023-11-21 | +86,28%      | +0,00%                   |              0 | +0,00%       |               0 | +0,00%           | +37,82%      | DISCESA QUASI IMMEDIATA |
| ALGO-USD        | 2023-11-25 | +86,16%      | +0,00%                   |              0 | -6,07%       |               2 | -6,07%           | +69,64%      | DISCESA QUASI IMMEDIATA |

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
- Casi positivi / salita storica: **87,50%**
- Casi negativi / discesa storica: **12,50%**
- Quanto è netto il segnale: **forte**
- Prezzo attuale: **78.456,64 $**
- Return normale fra 30 giorni: **107.687,94 $** (37,26%)
- Drawdown normale durante il mese: **76.155,39 $** (-2,93%)
- Drawdown brutto da rispettare: **71.099,65 $** (-9,38%)
- Max gain normale durante il mese: **110.884,63 $** (41,33%)
- Max gain buono / take profit ottimistico: **135.130,58 $** (72,24%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Solana
- Direzione più probabile a 30 giorni: **SALITA**
- Casi positivi / salita storica: **62,50%**
- Casi negativi / discesa storica: **37,50%**
- Quanto è netto il segnale: **medio**
- Prezzo attuale: **102,02 $**
- Return normale fra 30 giorni: **131,54 $** (28,93%)
- Drawdown normale durante il mese: **92,18 $** (-9,65%)
- Drawdown brutto da rispettare: **75,25 $** (-26,24%)
- Max gain normale durante il mese: **141,22 $** (38,43%)
- Max gain buono / take profit ottimistico: **173,43 $** (69,99%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Dogecoin
- Direzione più probabile a 30 giorni: **DISCESA**
- Casi positivi / salita storica: **32,50%**
- Casi negativi / discesa storica: **67,50%**
- Quanto è netto il segnale: **medio**
- Prezzo attuale: **0,09 $**
- Return normale fra 30 giorni: **0,08 $** (-11,41%)
- Drawdown normale durante il mese: **0,07 $** (-16,34%)
- Drawdown brutto da rispettare: **0,06 $** (-29,11%)
- Max gain normale durante il mese: **0,09 $** (10,18%)
- Max gain buono / take profit ottimistico: **0,11 $** (26,05%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Messaggio del giorno

Il quadro generale oggi è più favorevole. Lo scanner vede più possibilità di salita su più asset.

---

# Mappa semplice asset per asset

# Bitcoin — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟢 VERDE / Favorevole
**Prezzo attuale:** 78.456,64 $

**Direzione più probabile a 30 giorni:** **SALITA**
- Probabilità storica di salita: **87,50%**
- Probabilità storica di discesa: **12,50%**
- Quanto è netto il segnale: **forte**

## Come leggere questa parte

- **Probabilità storica di salita** = su 40 casi simili, quanti hanno chiuso sopra dopo 30 giorni.
- **Probabilità storica di discesa** = su 40 casi simili, quanti hanno chiuso sotto dopo 30 giorni.
- **Quanto è netto il segnale** = quanto è grande la differenza tra salita e discesa. Non vuol dire certezza, vuol dire solo che il risultato storico non è vicino al 50/50.

La lettura principale è rialzista, con segnale forte. Nei casi storici simili, il prezzo ha chiuso sopra dopo 30 giorni più spesso di quanto abbia chiuso sotto.

## 1. Return 30d — prezzo fra 30 giorni

**Return** significa rendimento finale. Qui guardiamo dove potrebbe stare il prezzo **alla fine dei 30 giorni**, non durante il percorso.

- Se va molto male: **53.379,54 $** (-31,96%)
- Se va male: **91.371,96 $** (16,46%)
- Scenario normale: **107.687,94 $** (37,26%)
- Se va bene: **122.570,83 $** (56,23%)
- Se va molto bene: **148.571,98 $** (89,37%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **76.155,39 $** (-2,93%)
- Discesa brutta: **71.099,65 $** (-9,38%)
- Discesa molto brutta: **49.804,21 $** (-36,52%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **110.884,63 $** (41,33%)
- Rialzo buono: **135.130,58 $** (72,24%)
- Rialzo molto forte: **165.856,09 $** (111,40%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Bitcoin tendeva a muoversi tra una zona bassa intorno a **76.155,39 $** e uno spike normale intorno a **110.884,63 $**.

La chiusura a 30 giorni era più spesso positiva: salita 87,50%, discesa 12,50%. Quindi la lettura principale è favorevole.

Nota leva BTC: se la liquidazione è vicina a 51.000 $, guarda soprattutto la discesa brutta e molto brutta. Il prezzo può recuperare dopo, ma la leva può saltare prima.

---

# Solana — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟢 VERDE / Favorevole
**Prezzo attuale:** 102,02 $

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

- Se va molto male: **71,85 $** (-29,57%)
- Se va male: **87,77 $** (-13,96%)
- Scenario normale: **131,54 $** (28,93%)
- Se va bene: **158,39 $** (55,25%)
- Se va molto bene: **208,12 $** (103,99%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **92,18 $** (-9,65%)
- Discesa brutta: **75,25 $** (-26,24%)
- Discesa molto brutta: **63,86 $** (-37,41%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **141,22 $** (38,43%)
- Rialzo buono: **173,43 $** (69,99%)
- Rialzo molto forte: **253,25 $** (148,24%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Solana tendeva a muoversi tra una zona bassa intorno a **92,18 $** e uno spike normale intorno a **141,22 $**.

La chiusura a 30 giorni era più spesso positiva: salita 62,50%, discesa 37,50%. Quindi la lettura principale è favorevole.

---

# Dogecoin — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🔴 ROSSO / Prudenza
**Prezzo attuale:** 0,09 $

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

- Se va molto male: **0,06 $** (-26,57%)
- Se va male: **0,07 $** (-22,47%)
- Scenario normale: **0,08 $** (-11,41%)
- Se va bene: **0,09 $** (5,46%)
- Se va molto bene: **0,13 $** (46,86%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **0,07 $** (-16,34%)
- Discesa brutta: **0,06 $** (-29,11%)
- Discesa molto brutta: **0,06 $** (-33,55%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **0,09 $** (10,18%)
- Rialzo buono: **0,11 $** (26,05%)
- Rialzo molto forte: **0,13 $** (46,86%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Dogecoin tendeva a muoversi tra una zona bassa intorno a **0,07 $** e uno spike normale intorno a **0,09 $**.

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

- Grezzo: **37,26%** → **107.687,94 $**
- Correzione imparata dagli errori: **2,01%**
- Calibrato: **39,27%** → **109.263,29 $**
- Lettura: Lo scanner è stato troppo pessimista sul prezzo finale.

### Drawdown 30d — rischio di discesa durante il mese

- Grezzo: **-2,93%** → **76.155,39 $**
- Correzione imparata dagli errori: **4,72%**
- Calibrato: **1,79%** → **79.861,15 $**
- Lettura: Lo scanner è stato troppo prudente: nella realtà il prezzo è sceso meno del previsto.

### Max gain 30d — rialzo/spike durante il mese

- Grezzo: **41,33%** → **110.884,63 $**
- Correzione imparata dagli errori: **-2,82%**
- Calibrato: **38,51%** → **108.668,30 $**
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

- Grezzo: **28,93%** → **131,54 $**
- Correzione imparata dagli errori: **8,80%**
- Calibrato: **37,73%** → **140,51 $**
- Lettura: Lo scanner è stato troppo pessimista sul prezzo finale.

### Drawdown 30d — rischio di discesa durante il mese

- Grezzo: **-9,65%** → **92,18 $**
- Correzione imparata dagli errori: **2,99%**
- Calibrato: **-6,66%** → **95,23 $**
- Lettura: Lo scanner è stato troppo prudente: nella realtà il prezzo è sceso meno del previsto.

### Max gain 30d — rialzo/spike durante il mese

- Grezzo: **38,43%** → **141,22 $**
- Correzione imparata dagli errori: **4,02%**
- Calibrato: **42,44%** → **145,32 $**
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
- Direzione calibrata oggi: **SALITA**

### Return 30d — prezzo finale fra 30 giorni

- Grezzo: **-11,41%** → **0,08 $**
- Correzione imparata dagli errori: **15,19%**
- Calibrato: **3,78%** → **0,09 $**
- Lettura: Lo scanner è stato troppo pessimista sul prezzo finale.

### Drawdown 30d — rischio di discesa durante il mese

- Grezzo: **-16,34%** → **0,07 $**
- Correzione imparata dagli errori: **15,34%**
- Calibrato: **-1,00%** → **0,09 $**
- Lettura: Lo scanner è stato troppo prudente: nella realtà il prezzo è sceso meno del previsto.

### Max gain 30d — rialzo/spike durante il mese

- Grezzo: **10,18%** → **0,09 $**
- Correzione imparata dagli errori: **2,52%**
- Calibrato: **12,70%** → **0,10 $**
- Lettura: Lo scanner ha sottostimato gli spike: nella realtà il prezzo è salito più del previsto.

### Come leggerlo

La parte grezza ti dice cosa mostrano i vecchi pattern storici. La parte calibrata ti dice come cambia quella lettura dopo aver visto se lo scanner, nel mercato reale, è stato troppo ottimista o troppo pessimista.

---

# Approfondimento tecnico — Bitcoin (BTC-USD)

## Semaforo: 🟢 VERDE / Favorevole

**Prezzo attuale:** 78.456,64 $

Bitcoin ha un segnale favorevole. La statistica dei casi simili indica più possibilità di salita che di discesa, ma resta comunque una probabilità, non una certezza.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **87,50%**
- Casi negativi dopo 30 giorni: **12,50%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **86,11%**
- Rendimento medio dopo 30 giorni: **34,99%**
- Rendimento centrale dopo 30 giorni: **37,26%**
- Discesa media durante i 30 giorni: **-9,59%**
- Massimo rialzo medio durante i 30 giorni: **56,81%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **105.911,44 $**
- Scenario centrale a 30 giorni: **107.687,94 $**
- Zona di rischio media: **70.935,90 $**
- Zona di rialzo media: **123.024,11 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -31,96% → **53.379,54 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: 16,46% → **91.371,96 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: 37,26% → **107.687,94 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 56,23% → **122.570,83 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 89,37% → **148.571,98 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -36,52% → **49.804,21 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -9,38% → **71.099,65 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -2,93% → **76.155,39 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: 0,00% → **78.456,64 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: 0,00% → **78.456,64 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 14,34% → **89.706,52 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 22,30% → **95.951,56 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 41,33% → **110.884,63 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 72,24% → **135.130,58 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 111,40% → **165.856,09 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| XLM-USD         | 2020-09-03   | 2020-12-11 |        90.75 |        91    |         -16.34 |         125.42 |
| INJ-USD         | 2023-08-06   | 2023-11-13 |        88.99 |        89.19 |          -7.66 |          89.19 |
| BNB-USD         | 2018-11-18   | 2019-02-25 |        88.99 |        70.51 |          -3.26 |          75.63 |
| UNI-USD         | 2023-04-07   | 2023-07-15 |        88.48 |       -47.87 |         -48.23 |         315.96 |
| THETA-USD       | 2023-08-18   | 2023-11-25 |        88.16 |        39.6  |          -6.15 |          39.6  |
| 1INCH-USD       | 2023-08-16   | 2023-11-23 |        87.81 |        17.36 |          -4.97 |          17.36 |
| LRC-USD         | 2019-11-18   | 2020-02-25 |        87.74 |       -31.73 |         -38.57 |          19.06 |
| XRP-USD         | 2020-09-03   | 2020-12-11 |        87.57 |       -41.75 |         -61.24 |           6.92 |
| ADA-USD         | 2023-08-14   | 2023-11-21 |        87.5  |        77.51 |           0    |          85.5  |
| BCH-USD         | 2019-01-12   | 2019-04-21 |        87.36 |        43.74 |         -18.54 |          45.1  |

---

# Approfondimento tecnico — Solana (SOL-USD)

## Semaforo: 🟢 VERDE / Favorevole

**Prezzo attuale:** 102,02 $

Solana ha un segnale favorevole. La statistica dei casi simili indica più possibilità di salita che di discesa, ma resta comunque una probabilità, non una certezza.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **62,50%**
- Casi negativi dopo 30 giorni: **37,50%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **84,90%**
- Rendimento medio dopo 30 giorni: **32,67%**
- Rendimento centrale dopo 30 giorni: **28,93%**
- Discesa media durante i 30 giorni: **-16,08%**
- Massimo rialzo medio durante i 30 giorni: **63,02%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **135,35 $**
- Scenario centrale a 30 giorni: **131,54 $**
- Zona di rischio media: **85,61 $**
- Zona di rialzo media: **166,31 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -29,57% → **71,85 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -13,96% → **87,77 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: 28,93% → **131,54 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 55,25% → **158,39 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 103,99% → **208,12 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -37,41% → **63,86 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -26,24% → **75,25 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -9,65% → **92,18 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -2,35% → **99,62 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: 0,00% → **102,02 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 3,59% → **105,69 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 7,44% → **109,61 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 38,43% → **141,22 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 69,99% → **173,43 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 148,24% → **253,25 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| VET-USD         | 2020-03-14   | 2020-06-21 |        87.95 |       103.01 |           0    |         132.4  |
| RUNE-USD        | 2020-03-18   | 2020-06-25 |        87.84 |        36.51 |         -13.77 |          57.1  |
| ZIL-USD         | 2020-09-05   | 2020-12-13 |        87.69 |        90.17 |           0    |         174.35 |
| BNB-USD         | 2023-10-03   | 2024-01-10 |        87.16 |         6.14 |          -4.32 |           6.14 |
| VET-USD         | 2023-08-16   | 2023-11-23 |        86.45 |        67.32 |           0    |          69.67 |
| RUNE-USD        | 2026-02-05   | 2026-05-15 |        86.39 |       -20.87 |         -35.52 |           0    |
| 1INCH-USD       | 2023-08-16   | 2023-11-23 |        86.34 |        17.36 |          -4.97 |          17.36 |
| ALGO-USD        | 2023-08-18   | 2023-11-25 |        86.03 |        69.64 |          -6.07 |          71.11 |
| XRP-USD         | 2020-09-03   | 2020-12-11 |        86    |       -41.75 |         -61.24 |           6.92 |
| ENJ-USD         | 2020-10-28   | 2021-02-04 |        85.92 |       221.5  |           0    |         261.65 |

---

# Approfondimento tecnico — Dogecoin (DOGE-USD)

## Semaforo: 🔴 ROSSO / Prudenza

**Prezzo attuale:** 0,09 $

Dogecoin richiede prudenza. La statistica dei casi simili indica più possibilità di discesa che di salita. Con leva, il rischio principale è il drawdown durante il percorso.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **32,50%**
- Casi negativi dopo 30 giorni: **67,50%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **80,01%**
- Rendimento medio dopo 30 giorni: **-1,73%**
- Rendimento centrale dopo 30 giorni: **-11,41%**
- Discesa media durante i 30 giorni: **-18,01%**
- Massimo rialzo medio durante i 30 giorni: **19,02%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **0,08 $**
- Scenario centrale a 30 giorni: **0,08 $**
- Zona di rischio media: **0,07 $**
- Zona di rialzo media: **0,10 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -26,57% → **0,06 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -22,47% → **0,07 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: -11,41% → **0,08 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 5,46% → **0,09 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 46,86% → **0,13 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -33,55% → **0,06 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -29,11% → **0,06 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -16,34% → **0,07 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -8,26% → **0,08 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: -1,28% → **0,08 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 0,00% → **0,09 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 6,09% → **0,09 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 10,18% → **0,09 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 26,05% → **0,11 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 46,86% → **0,13 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| SAND-USD        | 2021-04-20   | 2021-07-28 |        84.6  |         4.11 |         -14.27 |           8.86 |
| BTC-USD         | 2025-02-04   | 2025-05-14 |        82.82 |         2.46 |          -1.9  |           7.86 |
| YFI-USD         | 2022-05-10   | 2022-08-17 |        82.77 |       -22.15 |         -23.92 |           0    |
| FIL-USD         | 2022-05-10   | 2022-08-17 |        82.74 |       -28.78 |         -31.42 |           0    |
| ETH-USD         | 2025-02-19   | 2025-05-29 |        82.74 |        -7.43 |         -15.36 |           6.87 |
| MANA-USD        | 2022-10-23   | 2023-01-30 |        82.32 |       -12.23 |         -16.35 |           7.7  |
| XTZ-USD         | 2019-08-20   | 2019-11-27 |        82.21 |        10.11 |          -1.42 |          40.85 |
| NEO-USD         | 2019-08-10   | 2019-11-17 |        81.02 |       -35.14 |         -35.14 |           0    |
| MATIC-USD       | 2022-04-26   | 2022-08-03 |        80.98 |        -1.77 |         -13.97 |          15.45 |
| XLM-USD         | 2021-05-26   | 2021-09-02 |        80.7  |       -12.1  |         -28.8  |          17.43 |

</details>
<!-- COMPACT_SECTION_END:scanner_full_detail -->

<!-- COMPACT_SECTION_START:market_regime -->
<details>
<summary><strong>🌦️ Market Regime Match</strong></summary>

<!-- MARKET_REGIME_MATCH_START -->
# Market Regime Match Report


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [market_regime_match_report.md](market_regime_match_report.md)

Generated: 2026-09-10 05:31 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | snapshot_date   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | 2026-09-10 | RECOVERY | 78.457 $ | True | 23.47% | -5.34% | RECOVERY | 23.47% | -5.34% |
| DOGE-USD | 2026-09-10 | BEAR | 0.08593 $ | False | -0.04% | -12.60% | RECOVERY | 23.47% | -5.34% |
| SOL-USD | 2026-09-10 | RECOVERY | 102,02 $ | True | 52.84% | -9.83% | RECOVERY | 23.47% | -5.34% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 87.50% | 37.26% | 56.23% | 89.37% | -2.93% | -36.52% | 41.33% | 72.24% | 111.40% | 77.50% | 23.52% | 58.30% | 132.80% |
| BTC-USD | SAME_BTC_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| BTC-USD | SAME_ASSET_REGIME | 4 | 75.00% | 19.89% | 38.18% | 40.84% | -12.97% | -39.78% | 40.90% | 112.82% | 234.70% | 75.00% | 12.78% | 41.24% | 70.16% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| DOGE-USD | ALL_MATCHES | 40 | 32.50% | -11.41% | 5.46% | 46.86% | -16.34% | -33.55% | 10.18% | 26.05% | 46.86% | 35.00% | -9.23% | 10.11% | 43.96% |
| DOGE-USD | SAME_BTC_REGIME | 1 | 0.00% | -1.77% | -1.77% | -1.77% | -13.97% | -13.97% | 15.45% | 15.45% | 15.45% | 0.00% | -13.91% | -13.91% | -13.91% |
| DOGE-USD | SAME_ASSET_REGIME | 18 | 33.33% | -7.46% | 7.27% | 28.36% | -14.26% | -32.20% | 8.43% | 23.40% | 42.11% | 33.33% | -12.83% | 5.75% | 41.93% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 1 | 0.00% | -1.77% | -1.77% | -1.77% | -13.97% | -13.97% | 15.45% | 15.45% | 15.45% | 0.00% | -13.91% | -13.91% | -13.91% |
| SOL-USD | ALL_MATCHES | 40 | 62.50% | 28.93% | 55.25% | 103.99% | -9.65% | -37.41% | 38.43% | 69.99% | 148.24% | 60.00% | 16.10% | 86.08% | 201.68% |
| SOL-USD | SAME_BTC_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL-USD | SAME_ASSET_REGIME | 4 | 75.00% | 39.66% | 81.40% | 151.20% | -13.26% | -39.78% | 180.53% | 321.36% | 331.09% | 75.00% | 57.31% | 116.05% | 163.93% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 18 | 88.89% | 37.15% | -6.11% | 66.93% | 77.78% | 29.29% | 102.35% |
| BTC-USD | HISTORICAL_BTC_BULL | 22 | 86.36% | 37.26% | 0.00% | 80.31% | 77.27% | 23.52% | 84.74% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 20 | 15.00% | -13.39% | -21.14% | 16.97% | 20.00% | -12.49% | 18.21% |
| DOGE-USD | HISTORICAL_BTC_BULL | 15 | 60.00% | 4.11% | -14.27% | 43.74% | 60.00% | 8.47% | 79.20% |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION | 4 | 25.00% | -15.43% | -23.46% | 29.01% | 25.00% | -12.36% | 41.17% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 1 | 0.00% | -1.77% | -13.97% | 15.45% | 0.00% | -13.91% | 15.45% |
| SOL-USD | HISTORICAL_BTC_BEAR | 24 | 58.33% | 14.09% | -14.32% | 46.64% | 54.17% | 10.35% | 74.95% |
| SOL-USD | HISTORICAL_BTC_BULL | 14 | 78.57% | 69.13% | -3.58% | 167.10% | 78.57% | 93.80% | 314.75% |
| SOL-USD | HISTORICAL_BTC_DISTRIBUTION | 2 | 0.00% | -17.13% | -29.26% | 8.45% | 0.00% | -12.35% | 8.45% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 30 | 93.33% | 38.01% | -1.76% | 63.95% | 83.33% | 23.52% | 81.66% |
| BTC-USD | HISTORICAL_ASSET_BULL | 5 | 60.00% | 7.49% | -7.66% | 89.19% | 40.00% | -4.71% | 179.49% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 100.00% | 91.00% | -16.34% | 125.42% | 100.00% | 162.43% | 162.43% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 4 | 75.00% | 19.89% | -12.97% | 112.82% | 75.00% | 12.78% | 156.26% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 18 | 33.33% | -7.46% | -14.26% | 23.40% | 33.33% | -12.83% | 38.08% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 17 | 35.29% | -17.32% | -26.32% | 27.97% | 41.18% | -2.67% | 48.00% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 100.00% | 10.11% | -1.42% | 40.85% | 100.00% | 21.20% | 40.85% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 4 | 0.00% | -22.68% | -24.67% | 4.00% | 0.00% | -11.03% | 4.00% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 29 | 65.52% | 21.36% | -6.59% | 57.10% | 62.07% | 15.99% | 79.60% |
| SOL-USD | HISTORICAL_ASSET_BULL | 3 | 33.33% | -16.13% | -19.11% | 82.75% | 33.33% | -13.63% | 215.61% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 4 | 50.00% | 40.24% | -19.07% | 137.65% | 50.00% | 76.43% | 185.36% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 4 | 75.00% | 39.66% | -13.26% | 321.36% | 75.00% | 57.31% | 321.36% |

## Top regime-adjusted matches

A single cohort is selected deterministically: SAME_BTC_AND_ASSET_REGIME, otherwise SAME_ASSET_REGIME, otherwise SAME_BTC_REGIME. Each level must have at least 5 matches; cohorts are never combined.

| target   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level        | selection_reason              |
|:---------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:----------------------|:------------------------------|
| BTC-USD | NONE | 0 | 4 | 0 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES |
| DOGE-USD | SAME_ASSET_REGIME | 1 | 18 | 1 | 18 | 5 | 1_SAME_ASSET_FALLBACK | FALLBACK_TO_SAME_ASSET_REGIME |
| SOL-USD | NONE | 0 | 4 | 0 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES |

- WARNING DOGE-USD: SAME_ASSET_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| DOGE-USD | YFI-USD | 2022-05-10 | 82.77% | BEAR | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -22.15% | -23.92% | 0.00% | -30.34% | -32.23% | 0.00% |
| DOGE-USD | FIL-USD | 2022-05-10 | 82.74% | BEAR | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -28.78% | -31.42% | 0.00% | -36.98% | -38.04% | 0.00% |
| DOGE-USD | ETH-USD | 2025-02-19 | 82.74% | DISTRIBUTION | BEAR | SAME_ASSET_ONLY | MIXED | -7.43% | -15.36% | 6.87% | 43.86% | -15.36% | 47.20% |
| DOGE-USD | MANA-USD | 2022-10-23 | 82.32% | BEAR | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -12.23% | -16.35% | 7.70% | -21.40% | -30.92% | 7.70% |
| DOGE-USD | MATIC-USD | 2022-04-26 | 80.98% | RECOVERY | BEAR | SAME_BTC_AND_ASSET | MIXED | -1.77% | -13.97% | 15.45% | -13.91% | -20.67% | 15.45% |
| DOGE-USD | NEAR-USD | 2022-10-23 | 80.43% | BEAR | BEAR | SAME_ASSET_ONLY | MIXED | 0.56% | -5.20% | 16.82% | -13.69% | -22.51% | 16.82% |
| DOGE-USD | CHZ-USD | 2024-07-08 | 80.43% | BEAR | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -23.74% | -34.03% | 0.00% | 34.22% | -34.03% | 60.89% |
| DOGE-USD | THETA-USD | 2026-01-29 | 80.25% | BEAR | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -34.68% | -36.16% | 5.54% | -40.86% | -45.71% | 5.54% |
| DOGE-USD | KAVA-USD | 2023-08-14 | 80.20% | BULL | BEAR | SAME_ASSET_ONLY | BULLISH_30D | 19.52% | 0.00% | 25.59% | 3.12% | 0.00% | 34.81% |
| DOGE-USD | ALGO-USD | 2026-01-14 | 80.09% | BEAR | BEAR | SAME_ASSET_ONLY | MIXED | 9.51% | 0.00% | 27.32% | -14.61% | -17.13% | 27.32% |

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

Generato: 2026-09-10 05:32 UTC


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
| BTC | 78.457 $ | 0 | NEUTRALE / MISTO | STAGE 3 / DISTRIBUZIONE O PAUSA | VOLATILITÀ IN ESPANSIONE | SIGN OF STRENGTH POSSIBILE | MEDIO | HOLD / ASPETTA ROTTURA RESISTENZA |
| SOL | 102,02 $ | +2 | ANTICIPATO / COSTRUTTIVO MA NON CONFERMATO | STAGE 3 / DISTRIBUZIONE O PAUSA | COMPRESSIONE / TRIANGOLO POSSIBILE | SIGN OF STRENGTH POSSIBILE | MEDIO | HOLD LEGGERO / ATTESA CONFERME |
| DOGE | 0.08593 $ | -4 | DEBOLE / NON CONFERMATO | STAGE 4 / MARKDOWN | COMPRESSIONE / TRIANGOLO POSSIBILE | ACCUMULO POSSIBILE / RANGE BASSO | MEDIO | NO LONG / SHORT SOLO DOPO SPIKE E REJECTION |

## Punteggi per area

| Asset | Trend | Struttura | Momentum | Volume | Prezzo | Candela | Wyckoff | Totale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 0 | 0 | -2 | 0 | 0 | 0 | +2 | 0 |
| SOL | +1 | 0 | -2 | 0 | 0 | +1 | +2 | +2 |
| DOGE | -3 | 0 | -1 | 0 | 0 | 0 | 0 | -4 |

## Livelli tecnici

| Asset | Supporto | Resistenza | Breakout 60g | Breakdown 60g | ATR14 | Rendimento 30g | Rendimento 90g |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 76.909 $ | 79.468 $ | 82.262 $ | 61.493 $ | 2,75% | 22,81% | 23,48% |
| SOL | 97,45 $ | 107,12 $ | 110,04 $ | 70,69 $ | 4,52% | 34,40% | 52,75% |
| DOGE | 0.08189 $ | 0.09169 $ | 0.09998 $ | 0.06797 $ | 4,99% | 23,35% | -0,02% |

## Lettura dettagliata

### BTC

- Prezzo: **78.457 $**
- Score classico: **0 / 12**
- Verdetto: **NEUTRALE / MISTO**
- Azione coerente: **HOLD / ASPETTA ROTTURA RESISTENZA**
- Volatilità tecnica locale: **MEDIO** — ATR14 2,75%; distanza supporto 2,05%; distanza resistenza 1,25%

Dettaglio:

- Trend: **0** — prezzo sopra MA200 daily; MA50 daily in salita; MA200 daily in discesa; STAGE 3 / DISTRIBUZIONE O PAUSA
- Stage weekly: **STAGE 3 / DISTRIBUZIONE O PAUSA** — Prezzo sopra MA30 weekly ma pendenza debole o piatta.
- Struttura: **0** — VOLATILITÀ IN ESPANSIONE
- Momentum: **-2** — RSI sano 60.2; RSI in peggioramento; MACD sotto signal; istogramma MACD in peggioramento
- Volume: **0** — OBV sotto media; CMF positivo 0.17; volume ratio 0.86
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **+2** — SIGN OF STRENGTH POSSIBILE. Prezzo nella parte alta del range con flusso volume positivo.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 60.21 |
| MACD histogram | -487.16206 |
| CMF20 | 0.171 |
| Volume ratio 20 | 0.86 |
| MA20 | 78.707 $ |
| MA50 | 70.198 $ |
| MA100 | 66.645 $ |
| MA200 | 69.919 $ |
| Pendenza MA50 20g | +9,29% |
| Pendenza MA200 60g | -5,50% |
| Bollinger width | 5,70% |
| Bollinger position | 0.45 |

### SOL

- Prezzo: **102,02 $**
- Score classico: **+2 / 12**
- Verdetto: **ANTICIPATO / COSTRUTTIVO MA NON CONFERMATO**
- Azione coerente: **HOLD LEGGERO / ATTESA CONFERME**
- Volatilità tecnica locale: **MEDIO** — ATR14 4,52%; distanza supporto 4,74%; distanza resistenza 4,94%

Dettaglio:

- Trend: **+1** — prezzo sopra MA200 daily; breve termine sopra MA20/MA50; MA50 daily in salita; MA200 daily in discesa; STAGE 3 / DISTRIBUZIONE O PAUSA
- Stage weekly: **STAGE 3 / DISTRIBUZIONE O PAUSA** — Prezzo sopra MA30 weekly ma pendenza debole o piatta.
- Struttura: **0** — COMPRESSIONE / TRIANGOLO POSSIBILE
- Momentum: **-2** — RSI sano 59.6; RSI in peggioramento; MACD sotto signal; istogramma MACD in peggioramento
- Volume: **0** — OBV sotto media; CMF positivo 0.18; volume ratio 0.70
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **+1** — Hammer / rejection basso
- Wyckoff: **+2** — SIGN OF STRENGTH POSSIBILE. Prezzo nella parte alta del range con flusso volume positivo.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 59.56 |
| MACD histogram | -0.78858 |
| CMF20 | 0.175 |
| Volume ratio 20 | 0.70 |
| MA20 | 101,47 $ |
| MA50 | 85,93 $ |
| MA100 | 79,56 $ |
| MA200 | 82,72 $ |
| Pendenza MA50 20g | +12,15% |
| Pendenza MA200 60g | -10,06% |
| Bollinger width | 16,11% |
| Bollinger position | 0.54 |

### DOGE

- Prezzo: **0.08593 $**
- Score classico: **-4 / 12**
- Verdetto: **DEBOLE / NON CONFERMATO**
- Azione coerente: **NO LONG / SHORT SOLO DOPO SPIKE E REJECTION**
- Volatilità tecnica locale: **MEDIO** — ATR14 4,99%; distanza supporto 4,97%; distanza resistenza 6,67%

Dettaglio:

- Trend: **-3** — prezzo sotto MA200 daily; MA50 daily in salita; MA200 daily in discesa; STAGE 4 / MARKDOWN
- Stage weekly: **STAGE 4 / MARKDOWN** — Prezzo sotto MA30 weekly con MA30 in discesa.
- Struttura: **0** — COMPRESSIONE / TRIANGOLO POSSIBILE
- Momentum: **-1** — RSI sano 53.9; MACD sotto signal; istogramma MACD in peggioramento
- Volume: **0** — OBV sotto media; CMF positivo 0.07; volume ratio 0.95
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **0** — ACCUMULO POSSIBILE / RANGE BASSO. Prezzo nella metà bassa del range, ma senza spring confermato.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 53.92 |
| MACD histogram | -0.00016 |
| CMF20 | 0.068 |
| Volume ratio 20 | 0.95 |
| MA20 | 0.08739 $ |
| MA50 | 0.07740 $ |
| MA100 | 0.07819 $ |
| MA200 | 0.08828 $ |
| Pendenza MA50 20g | +7,49% |
| Pendenza MA200 60g | -12,84% |
| Bollinger width | 17,04% |
| Bollinger position | 0.40 |

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

Generato: 2026-09-10 05:32 UTC


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
| BTC | 78.457 $ | Doppio massimo | CANDIDATO | ribassista | n/a | 58.946 $ | n/a | 26,08% | Fib 23,6% IN AVVICINAMENTO (0) @ 76.477 $ | NEL RANGE | 76.248 $ |
| SOL | 102,02 $ | Doppio massimo | CANDIDATO | ribassista | n/a | 62,51 $ | n/a | 44,31% | Fib 23,6% TENUTO (+1) @ 98,33 $ | NEL RANGE | 97,45 $ |
| DOGE | 0.08593 $ | Doppio massimo | CANDIDATO | ribassista | n/a | 0.06214 $ | n/a | 26,42% | Fib 38,2% TENUTO (0) @ 0.08419 $ | NEL RANGE | 0.08157 $ |

## BTC

![Classic visual BTC](classic_visual_BTC.png)

- Pattern principale: **Doppio massimo**
- Stato pattern: **CANDIDATO** (0)
- Famiglia: **ribassista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-07-15 -> 2026-08-09**
- Età formazione: **32 giorni**
- Breakout pattern: **n/a**
- Età breakout: **n/a**
- Neckline: **62.227 $**
- Target teorico: **58.946 $**
- Progresso verso target: **n/a**
- Distanza dalla neckline: **26,08%**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 23,6% IN AVVICINAMENTO (0) @ 76.477 $** — Swing UP 2026-07-01 57.748 -> 2026-09-03 82.262; livello più vicino 23.6% a 76.477; stato IN AVVICINAMENTO; confluenza: supporto tecnico.
- Invalidazione: **63.471 $**
- Relazione prezzo/neckline: **sopra neckline**
- Dettaglio: Due massimi simili vicino a 65.508 tra 2026-07-15 e 2026-08-09. Neckline ribassista stimata: 62.227. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 32 giorni. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Hammer / rejection basso**
- Stato prezzo: **NEL RANGE**
- Supporto: **76.248 $**
- Resistenza: **79.468 $**
- Breakout 60g: **82.262 $**
- Breakdown 60g: **61.493 $**
- RSI14: **60.14**
- ATR14: **2,75%**
- Volume ratio 20g: **0.86**
- Rendimento 30g: **+22,76%**
- Rendimento 90g: **+23,44%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Triangolo ascendente possibile | CANDIDATO | 0 | rialzista | n/a | n/a | n/a | n/a | n/a | n/a | n/a | Resistenza quasi piatta e minimi crescenti. Stato: CANDIDATO; il pattern non ha una neckline univoca da usare per il lifecycle. |
| Doppio minimo | CANDIDATO | 0 | rialzista | 82.792 $ | n/a | n/a | 90.626 $ | n/a | 5,53% | 81.136 $ | Due minimi simili a 74.959 $ e 76.248 $. Neckline circa 82.792 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 8 giorni. |
| Doppio massimo | CANDIDATO | 0 | ribassista | 62.227 $ | n/a | n/a | 58.946 $ | n/a | 26,08% | 63.471 $ | Due massimi simili a 65.508 $ e 65.402 $. Neckline circa 62.227 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 32 giorni. |

## SOL

![Classic visual SOL](classic_visual_SOL.png)

- Pattern principale: **Doppio massimo**
- Stato pattern: **CANDIDATO** (0)
- Famiglia: **ribassista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-07-15 -> 2026-08-09**
- Età formazione: **32 giorni**
- Breakout pattern: **n/a**
- Età breakout: **n/a**
- Neckline: **70,69 $**
- Target teorico: **62,51 $**
- Progresso verso target: **n/a**
- Distanza dalla neckline: **44,31%**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 23,6% TENUTO (+1) @ 98,33 $** — Swing UP 2026-06-06 60,41 -> 2026-08-27 110,04; livello più vicino 23.6% a 98,33; stato TENUTO; confluenza: supporto tecnico.
- Invalidazione: **72,11 $**
- Relazione prezzo/neckline: **sopra neckline**
- Dettaglio: Due massimi simili vicino a 78,88 tra 2026-07-15 e 2026-08-09. Neckline ribassista stimata: 70,69. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 32 giorni. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Hammer / rejection basso**
- Stato prezzo: **NEL RANGE**
- Supporto: **97,45 $**
- Resistenza: **110,04 $**
- Breakout 60g: **110,04 $**
- Breakdown 60g: **70,69 $**
- RSI14: **59.46**
- ATR14: **4,52%**
- Volume ratio 20g: **0.70**
- Rendimento 30g: **+34,33%**
- Rendimento 90g: **+52,67%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Doppio massimo | CANDIDATO | 0 | ribassista | 70,69 $ | n/a | n/a | 62,66 $ | n/a | 44,31% | 72,11 $ | Due massimi simili a 78,73 $ e 77,62 $. Neckline circa 70,69 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 32 giorni. |
| Testa e spalle inverso | TARGET RAGGIUNTO | 0 | rialzista | 78,17 $ | 2026-08-19 | 22g | 85,65 $ | 318,95% | n/a | 76,61 $ | Spalla sinistra 73,40 $, testa 70,69 $, spalla destra 74,20 $. Neckline circa 78,17 $. Breakout neckline: 2026-08-19 (22 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 85,65 $; progresso: 318,95%; prezzo sopra neckline. |
| Doppio minimo | TARGET RAGGIUNTO | 0 | rialzista | 78,73 $ | 2026-08-19 | 22g | 84,05 $ | 437,51% | n/a | 77,15 $ | Due minimi simili a 73,40 $ e 74,20 $. Neckline circa 78,73 $. Breakout neckline: 2026-08-19 (22 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 84,05 $; progresso: 437,51%; prezzo sopra neckline. |

## DOGE

![Classic visual DOGE](classic_visual_DOGE.png)

- Pattern principale: **Doppio massimo**
- Stato pattern: **CANDIDATO** (0)
- Famiglia: **ribassista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-07-26 -> 2026-08-11**
- Età formazione: **30 giorni**
- Breakout pattern: **n/a**
- Età breakout: **n/a**
- Neckline: **0.06797 $**
- Target teorico: **0.06214 $**
- Progresso verso target: **n/a**
- Distanza dalla neckline: **26,42%**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 38,2% TENUTO (0) @ 0.08419 $** — Swing UP 2026-08-01 0.06797 -> 2026-09-05 0.09421; livello più vicino 38.2% a 0.08419; stato TENUTO; confluenza: nessuna confluenza indipendente.
- Invalidazione: **0.06933 $**
- Relazione prezzo/neckline: **sopra neckline**
- Dettaglio: Due massimi simili vicino a 0.07380 tra 2026-07-26 e 2026-08-11. Neckline ribassista stimata: 0.06797. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 30 giorni. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **NEL RANGE**
- Supporto: **0.08157 $**
- Resistenza: **0.09169 $**
- Breakout 60g: **0.09998 $**
- Breakdown 60g: **0.06797 $**
- RSI14: **53.86**
- ATR14: **4,99%**
- Volume ratio 20g: **0.95**
- Rendimento 30g: **+23,31%**
- Rendimento 90g: **-0,05%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Doppio massimo | CANDIDATO | 0 | ribassista | 0.06797 $ | n/a | n/a | 0.04174 $ | n/a | 26,42% | 0.06933 $ | Due massimi simili a 0.09169 $ e 0.09421 $. Neckline circa 0.06797 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 5 giorni. |
| Triangolo ascendente possibile | CANDIDATO | 0 | rialzista | n/a | n/a | n/a | n/a | n/a | n/a | n/a | Resistenza quasi piatta e minimi crescenti. Stato: CANDIDATO; il pattern non ha una neckline univoca da usare per il lifecycle. |
| Doppio minimo | TARGET RAGGIUNTO | 0 | rialzista | 0.07923 $ | 2026-08-20 | 21g | 0.08952 $ | 65,12% | n/a | 0.07765 $ | Due minimi simili a 0.06961 $ e 0.06895 $. Neckline circa 0.07923 $. Breakout neckline: 2026-08-20 (21 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 0.08952 $; progresso: 65,12%; prezzo sopra neckline. |

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

Generato: 2026-09-10 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [fractal_path_tracker.md](fractal_path_tracker.md)

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-09-10**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-02-25**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **102,02 $**
- Verdetto principale: **ANALOGIA DEBOLE / SCENARIO SECONDARIO**
- Somiglianza strutturale: **+69,32%**
- Aderenza live principale: **+72,09%**
- Errore medio live principale: **13,95%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE SOLO DI CONTESTO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **96**
- Osservazioni inclusive dal bottom: **97**
- Osservazioni da inizio programma/scanner: **70**
- Errore assoluto medio dal bottom: **11,75%**
- Errore assoluto medio da inizio programma: **13,95%**
- Gap firmato medio ultimi 7 giorni: **+9,40%**
- Errore assoluto medio ultimi 7 giorni: **9,40%**
- Gap ultimo giorno: **+11,75%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **+11,75%**
- Gap firmato medio 7g: **+9,40%**
- Errore assoluto medio 7g: **9,40%**
- Variazione recente gap: **+2,74%**
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
| 87 | 2026-09-01 | 2023-02-16 | 99,99 $ | 93,06 $ | +7,45% | da inizio programma |
| 88 | 2026-09-02 | 2023-02-17 | 100,39 $ | 96,77 $ | +3,74% | da inizio programma |
| 89 | 2026-09-03 | 2023-02-18 | 103,98 $ | 97,07 $ | +7,12% | da inizio programma |
| 90 | 2026-09-04 | 2023-02-19 | 101,95 $ | 95,83 $ | +6,38% | da inizio programma |
| 91 | 2026-09-05 | 2023-02-20 | 103,19 $ | 97,81 $ | +5,50% | da inizio programma |
| 92 | 2026-09-06 | 2023-02-21 | 106,45 $ | 96,26 $ | +10,58% | da inizio programma |
| 93 | 2026-09-07 | 2023-02-22 | 103,87 $ | 95,29 $ | +9,01% | da inizio programma |
| 94 | 2026-09-08 | 2023-02-23 | 103,33 $ | 94,33 $ | +9,53% | da inizio programma |
| 95 | 2026-09-09 | 2023-02-24 | 103,33 $ | 91,38 $ | +13,07% | da inizio programma |
| 96 | 2026-09-10 | 2023-02-25 | 102,02 $ | 91,29 $ | +11,75% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-09-17 | 88,06 $ | 98,40 $ | 98,40 $ / 104,09 $ | no | n/a | n/a | n/a |
| 14g | 2026-09-24 | 81,28 $ | 90,83 $ | 88,87 $ / 104,09 $ | no | n/a | n/a | n/a |
| 21g | 2026-10-01 | 106,22 $ | 118,71 $ | 88,87 $ / 120,72 $ | no | n/a | n/a | n/a |
| 28g | 2026-10-08 | 108,31 $ | 121,03 $ | 88,87 $ / 124,73 $ | no | n/a | n/a | n/a |
| 35g | 2026-10-15 | 111,92 $ | 125,07 $ | 88,87 $ / 125,36 $ | no | n/a | n/a | n/a |
| 42g | 2026-10-22 | 110,09 $ | 123,03 $ | 88,87 $ / 125,36 $ | no | n/a | n/a | n/a |
| 49g | 2026-10-29 | 119,43 $ | 133,46 $ | 88,87 $ / 134,20 $ | no | n/a | n/a | n/a |
| 56g | 2026-11-05 | 109,58 $ | 122,46 $ | 88,87 $ / 134,20 $ | no | n/a | n/a | n/a |
| 63g | 2026-11-12 | 115,22 $ | 128,75 $ | 88,87 $ / 134,20 $ | no | n/a | n/a | n/a |
| 70g | 2026-11-19 | 113,86 $ | 127,24 $ | 88,87 $ / 134,20 $ | no | n/a | n/a | n/a |
| 77g | 2026-11-26 | 105,51 $ | 117,91 $ | 88,87 $ / 134,20 $ | no | n/a | n/a | n/a |
| 84g | 2026-12-03 | 106,87 $ | 119,43 $ | 88,87 $ / 134,20 $ | no | n/a | n/a | n/a |
| 91g | 2026-12-10 | 105,84 $ | 118,28 $ | 88,87 $ / 134,20 $ | no | n/a | n/a | n/a |
| 98g | 2026-12-17 | 106,66 $ | 119,19 $ | 88,87 $ / 134,20 $ | no | n/a | n/a | n/a |
| 105g | 2026-12-24 | 101,83 $ | 113,80 $ | 88,87 $ / 134,20 $ | no | n/a | n/a | n/a |
| 112g | 2026-12-31 | 104,43 $ | 116,70 $ | 88,87 $ / 134,20 $ | no | n/a | n/a | n/a |
| 119g | 2027-01-07 | 120,34 $ | 134,48 $ | 88,87 $ / 135,12 $ | no | n/a | n/a | n/a |
| 126g | 2027-01-14 | 120,50 $ | 134,66 $ | 88,87 $ / 135,12 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 56 | 35,71% | 10,97% | 12,86% |
| 14g | 49 | 28,57% | 17,90% | 11,69% |
| 21g | 42 | 14,29% | 27,51% | 13,30% |
| 28g | 35 | 31,43% | 25,65% | 12,84% |
| 35g | 30 | 43,33% | 18,11% | 11,95% |
| 42g | 23 | 86,96% | 8,96% | 11,09% |
| 49g | 16 | 100,00% | 6,04% | 10,88% |
| 56g | 9 | 100,00% | 7,01% | 9,40% |
| 63g | 2 | 100,00% | 4,86% | n/a |
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

Ultima lettura salvata: **2026-09-10** — SOL 102,02 $, gap +11,75%, somiglianza +69,32%.

Nel report principale lascio solo il link, così non diventa troppo lungo.

<!-- SOL_BTC_FRACTAL_HISTORY_END -->

</details>
<!-- COMPACT_SECTION_END:fractal_path -->

<!-- COMPACT_SECTION_START:exchange_microstructure -->
<details>
<summary><strong>🏦 Dati exchange, liquidità e leva</strong></summary>

<!-- EXCHANGE_MICROSTRUCTURE_START -->
# Dati exchange, liquidità e leva

Generato: 2026-09-10 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [exchange_microstructure_report.md](exchange_microstructure_report.md)

Questo modulo legge Kraken Futures, Bitget Futures e KuCoin Futures come nucleo derivati. OKX e Coinbase vengono raccolti come fonti ausiliarie non pesate.
Non modifica la formula matematica di RSI, Fibonacci o Wyckoff: controlla se quei segnali sono sostenuti da acquisti, vendite, OI, funding e liquidità.

**Limite importante:** questo nucleo non assume disponibile un feed pubblico completo delle liquidazioni. La componente liquidazioni resta neutrale; le zone future restano stime di pressione, non dati certi delle singole posizioni.

Diagnostica completa: [exchange_source_diagnostics.md](exchange_source_diagnostics.md)

## Sintesi

| Asset | Prezzo | Exchange | Segnale candidato | Peso Global | Bias exchange | Confidenza | Copertura | Funding 8h eq. | OI 24h | Taker flow (campione/4h) | Book 0,5% | Liq long campione | Liq short campione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 78.268 $ | 3 | 0 | 0 | LEGGERMENTE POSITIVA / NON PESATA | BASSA | 100% | +0,0084% | -0,81% | 1,15 | -0,66% | 0 $ | 0 $ |
| SOL | 101,73 $ | 3 | 0 | 0 | LEGGERMENTE POSITIVA / NON PESATA | BASSA | 100% | -0,0038% | -3,76% | 1,58 | -6,27% | 0 $ | 0 $ |
| DOGE | 0.08551 $ | 3 | 0 | 0 | LEGGERMENTE POSITIVA / NON PESATA | BASSA | 100% | +0,0075% | -5,38% | 1,69 | +2,33% | 0 $ | 0 $ |

Il segnale candidato è limitato a **±1**, ma il peso nel Global resta **0** finché il tracker a 7 giorni non raggiunge 30 controlli, almeno 55% di accuratezza e return corretto direzione positivo. Un singolo muro o funding non basta.

La colonna taker usa un campione recente nel primo run. Dopo almeno 3 fotografie distribuite su almeno 45 minuti viene sostituita automaticamente dalla media intraday 4h.

## Dati separati per exchange

| Asset | Exchange | Stato | Funding 8h eq. | Open interest | Taker flow | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | Kraken | OK | +0,0148% | 165,44 mln $ | 0,31 | -5,54% |
| BTC | Bitget | OK | +0,0100% | 2,79 mld $ | 0,09 | +27,08% |
| BTC | Kucoin | OK | +0,0050% | 1,08 mld $ | 1,45 | +2,89% |
| SOL | Kraken | OK | +0,0031% | 29,63 mln $ | 36,23 | -13,90% |
| SOL | Bitget | OK | -0,0037% | 460,55 mln $ | 0,08 | +62,13% |
| SOL | Kucoin | OK | -0,0079% | 179,27 mln $ | 5,72 | -20,36% |
| DOGE | Kraken | OK | -0,0007% | 4,33 mln $ | 2,42 | +2,11% |
| DOGE | Bitget | OK | +0,0077% | 109,64 mln $ | 0,46 | +25,69% |
| DOGE | Kucoin | OK | +0,0094% | 70,68 mln $ | 0,86 | +1,52% |

Kraken, Bitget e KuCoin contribuiscono a funding normalizzato, open interest, trade aggressivi e order book. Non viene inventato un long/short ratio pubblico né un feed completo delle liquidazioni.

## Conferme per indicatori tecnici

### BTC

- Score grezzo exchange: **+1,75**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 3, accuratezza +66,67%.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 0, bear 2, divergenze 1.
- Flusso taker/order book: **+1,75**.
- OI/funding/basis: **+0,00**.
- Affollamento long/short: **+0,00**.
- Liquidazioni: **NON PESATE / FEED COMPLETO NON ASSUNTO DISPONIBILE**.
- **Wyckoff:** Fase Wyckoff non abbastanza chiara per una conferma exchange.
- **Fibonacci:** Fibonacci in_avvicinamento; nessuna conferma exchange netta. Confluenza tecnica dichiarata: supporto tecnico.
- **RSI:** RSI in zona non estrema o flusso exchange non abbastanza netto.
- **Pattern:** I pattern candidati restano non operativi: i dati exchange possono solo preparare la conferma.
- **Breakout/breakdown:** Prezzo non abbastanza vicino a un livello chiave o flusso non netto.
- **Mappa liquidità attuale:** muro bid: n/a; muro ask: n/a

![Microstruttura exchange BTC](exchange_microstructure_BTC.png)

### SOL

- Score grezzo exchange: **+2,50**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 5, accuratezza +60,00%.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 1, bear 1, divergenze 0.
- Flusso taker/order book: **+1,75**.
- OI/funding/basis: **+0,50**.
- Affollamento long/short: **+0,00**.
- Liquidazioni: **NON PESATE / FEED COMPLETO NON ASSUNTO DISPONIBILE**.
- **Wyckoff:** Fase Wyckoff non abbastanza chiara per una conferma exchange.
- **Fibonacci:** Fibonacci tenuto con acquisti/assorbimento coerenti: conferma positiva. Confluenza tecnica dichiarata: supporto tecnico.
- **RSI:** RSI in zona non estrema o flusso exchange non abbastanza netto.
- **Pattern:** I pattern candidati restano non operativi: i dati exchange possono solo preparare la conferma.
- **Breakout/breakdown:** Prezzo non abbastanza vicino a un livello chiave o flusso non netto.
- **Mappa liquidità attuale:** muro bid: n/a; muro ask: n/a

![Microstruttura exchange SOL](exchange_microstructure_SOL.png)

### DOGE

- Score grezzo exchange: **+2,50**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 8, accuratezza +50,00%.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 0, bear 1, divergenze 0.
- Flusso taker/order book: **+1,75**.
- OI/funding/basis: **+0,50**.
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
| BTC | +87,50% | +37,26% | 1 | +0,00% | RACCOLTA DATI | 0,00 | +87,50% | +37,26% |
| SOL | +62,50% | +28,93% | 2 | +100,00% | RACCOLTA DATI | 0,00 | +62,50% | +28,93% |
| DOGE | +32,50% | -11,41% | 4 | +75,00% | RACCOLTA DATI | 0,00 | +32,50% | -11,41% |

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

Generato: 2026-09-10 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [exchange_signal_tracker_report.md](exchange_signal_tracker_report.md)

Questo tracker verifica se il segnale candidato exchange ±1 anticipa correttamente la direzione del prezzo a 1/3/7/14/30 giorni.
Il peso Global resta 0 finché l'orizzonte 7g non ha almeno 30 controlli, accuratezza almeno 55% e return corretto direzione positivo. L'overlay a 30g ha un gate separato.

Controlli maturati completati in questa esecuzione: **15**.

## Ultime fotografie giornaliere

| Data | Asset | Prezzo | Versione | Calibrazione | Candidato | Peso Global | Score raw | Confidenza | Taker 4h | OI 24h | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-09-10 | BTC | 78.267,60 | V2.1.3 | OK | 0 | 0 | 1,75 | BASSA | 1,15 | -0,81% | -0,66% |
| 2026-09-10 | DOGE | 0.08551 | V2.1.3 | OK | 0 | 0 | 2,50 | BASSA | 1,69 | -5,38% | +2,33% |
| 2026-09-10 | SOL | 101,73 | V2.1.3 | OK | 0 | 0 | 2,50 | BASSA | 1,58 | -3,76% | -6,27% |
| 2026-09-09 | BTC | 79.100,00 | V2.1.3 | OK | 0 | 0 | 1,75 | BASSA | 9,11 | +1,21% | -1,05% |
| 2026-09-09 | DOGE | 0.09035 | V2.1.3 | OK | 0 | 0 | 1,75 | BASSA | 2,82 | -1,20% | -0,63% |
| 2026-09-09 | SOL | 104,15 | V2.1.3 | OK | 0 | 0 | 1,75 | BASSA | 2,40 | -0,20% | +1,45% |
| 2026-09-08 | BTC | 78.728,60 | V2.1.3 | OK | 0 | 0 | 1,75 | BASSA | 1,33 | +0,59% | -1,63% |
| 2026-09-08 | DOGE | 0.08985 | V2.1.3 | OK | 0 | 0 | 1,75 | BASSA | 1,16 | -2,94% | +1,74% |
| 2026-09-08 | SOL | 103,18 | V2.1.3 | OK | 0 | 0 | 1,75 | BASSA | 1,63 | -2,35% | -2,79% |

## Accuratezza direzionale

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 5 | +40,00% | -0,26% | -0,89% | +0,60% | FEEDBACK RAPIDO |
| BTC | 3g | 5 | +40,00% | +0,25% | -2,11% | +2,12% | FEEDBACK RAPIDO |
| BTC | 7g | 3 | +66,67% | +0,53% | -2,29% | +3,66% | FEEDBACK RAPIDO |
| BTC | 14g | 3 | +33,33% | -0,17% | -3,31% | +4,48% | FEEDBACK RAPIDO |
| BTC | 30g | 1 | +0,00% | -0,24% | -3,45% | +3,82% | FEEDBACK RAPIDO |
| SOL | 1g | 5 | +60,00% | +0,93% | +0,43% | +3,39% | FEEDBACK RAPIDO |
| SOL | 3g | 5 | +60,00% | +2,75% | -3,02% | +7,77% | FEEDBACK RAPIDO |
| SOL | 7g | 5 | +60,00% | +3,63% | -3,62% | +9,63% | FEEDBACK RAPIDO |
| SOL | 14g | 5 | +80,00% | +8,45% | -4,32% | +14,61% | FEEDBACK RAPIDO |
| SOL | 30g | 2 | +100,00% | +22,28% | -5,94% | +27,20% | FEEDBACK RAPIDO |
| DOGE | 1g | 9 | +44,44% | +0,77% | -0,33% | +1,78% | FEEDBACK RAPIDO |
| DOGE | 3g | 9 | +33,33% | +1,22% | -3,22% | +5,78% | FEEDBACK RAPIDO |
| DOGE | 7g | 8 | +50,00% | -0,83% | -4,47% | +8,09% | FEEDBACK RAPIDO |
| DOGE | 14g | 7 | +42,86% | +0,79% | -5,33% | +14,98% | FEEDBACK RAPIDO |
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

**BTC** — BTC: i futures non danno una lettura chiara. Non si vede uno sbilanciamento forte né long né short. Qui pesa di più il report frattale.

**SOL** — SOL: i futures non danno una lettura chiara. Non si vede uno sbilanciamento forte né long né short. Qui pesa di più il report frattale.

**DOGE** — DOGE: i futures non danno una lettura chiara. Non si vede uno sbilanciamento forte né long né short. Qui pesa di più il report frattale.

| Asset | Prezzo | Funding | OI 24h | Long/Short | Lettura futures | Forza |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 78.457 $ | +0.0084% | -3.84% | 1.62 | Misto | 1/5 |
| SOL | 102,02 $ | -0.0061% | -13.95% | 2.05 | Misto | 1/5 |
| DOGE | 0.08593 $ | +0.0035% | -8.62% | 5.12 | Misto | 1/5 |

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

Generato: 2026-09-10 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [rsi_multitimeframe_divergence_report.md](rsi_multitimeframe_divergence_report.md)

Il modulo confronta prezzo e RSI 14 sui pivot confermati **daily e weekly**. Riconosce divergenze regolari e nascoste, segnali in formazione, invalidazioni e semplice conferma del momentum.

**Peso operativo: 0.** Non modifica il Global Confluence, non cambia le soglie del Paper Trading e non apre né blocca operazioni. I risultati vengono misurati prima di qualsiasi futura decisione sul peso.

## Sintesi corrente

| Asset   | Daily                      | Stato D       | Weekly             | Stato W       | Lettura weekly                                                                                                              |   Peso |
|:--------|:---------------------------|:--------------|:-------------------|:--------------|:----------------------------------------------------------------------------------------------------------------------------|-------:|
| BTC     | Hidden bullish             | IN_FORMAZIONE | Conferma rialzista | CONTESTO      | Prezzo e RSI stanno salendo insieme: momentum rialzista confermato.                                                         |      0 |
| SOL     | Hidden bullish             | IN_FORMAZIONE | Hidden bearish     | IN_FORMAZIONE | Hidden bearish in formazione: il secondo estremo non è ancora un pivot confermato. Peso operativo sempre 0.                 |      0 |
| DOGE    | Misto / nessuna divergenza | CONTESTO      | Hidden bearish     | CONFERMATA    | Hidden bearish confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto. |      0 |

## Dettaglio dei pivot

| Asset   | TF   | Tipo                       | Stato         | Prezzo / RSI      | Pivot confrontati                                                   | Δ prezzo contesto   | Δ RSI contesto   |   Peso |
|:--------|:-----|:---------------------------|:--------------|:------------------|:--------------------------------------------------------------------|:--------------------|:-----------------|-------:|
| BTC     | 1D   | Hidden bullish             | IN_FORMAZIONE | 78.467 $ / 60,16  | 2026-09-02 76.248 $ / RSI 65,21 → 2026-09-08 77.636 $ / RSI 60,09   | n/a                 | n/a              |      0 |
| BTC     | 1W   | Conferma rialzista         | CONTESTO      | 78.467 $ / 56,58  | n/a                                                                 | +23,61%             | 17,74            |      0 |
| SOL     | 1D   | Hidden bullish             | IN_FORMAZIONE | 102,03 $ / 59,48  | 2026-09-02 97,45 $ / RSI 63,79 → 2026-09-10 100,63 $ / RSI 59,48    | n/a                 | n/a              |      0 |
| SOL     | 1W   | Hidden bearish             | IN_FORMAZIONE | 102,03 $ / 57,01  | 2026-08-30 110,04 $ / RSI 57,95 → 2026-09-06 107,12 $ / RSI 60,25   | n/a                 | n/a              |      0 |
| DOGE    | 1D   | Misto / nessuna divergenza | CONTESTO      | 0.08596 $ / 53,92 | n/a                                                                 | -2,03%              | -12,77           |      0 |
| DOGE    | 1W   | Hidden bearish             | CONFERMATA    | 0.08596 $ / 46,46 | 2026-05-17 0.11825 $ / RSI 44,25 → 2026-08-23 0.09998 $ / RSI 49,72 | n/a                 | n/a              |      0 |

### BTC

- **1D — Hidden bullish / IN_FORMAZIONE**: Hidden bullish in formazione: il secondo estremo non è ancora un pivot confermato. Peso operativo sempre 0.
- **1W — Conferma rialzista / CONTESTO**: Prezzo e RSI stanno salendo insieme: momentum rialzista confermato.

### SOL

- **1D — Hidden bullish / IN_FORMAZIONE**: Hidden bullish in formazione: il secondo estremo non è ancora un pivot confermato. Peso operativo sempre 0.
- **1W — Hidden bearish / IN_FORMAZIONE**: Hidden bearish in formazione: il secondo estremo non è ancora un pivot confermato. Peso operativo sempre 0.

### DOGE

- **1D — Misto / nessuna divergenza / CONTESTO**: Misto / nessuna divergenza. Non esiste una divergenza confermata sugli ultimi pivot.
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
| BTC     | 1W   | Bullish regolare |          30 |           1 | +100,00%      | +1,03%            | RACCOLTA DATI |      0 |
| DOGE    | 1D   | Bullish regolare |          30 |           1 | +100,00%      | +22,35%           | RACCOLTA DATI |      0 |
| DOGE    | 1D   | Hidden bearish   |          30 |           2 | +50,00%       | -8,18%            | RACCOLTA DATI |      0 |
| DOGE    | 1D   | Hidden bearish   |          60 |           1 | 0,00%         | -16,95%           | RACCOLTA DATI |      0 |
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

Generato: 2026-09-10 05:32 UTC


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

| Asset   | Prezzo   |   Punteggio | Verdetto                      | Trend           | Momentum        | Struttura                                          |   Pattern score | Fibonacci            | Pattern rialzista                | Pattern ribassista         | Supporto   | Resistenza   |
|:--------|:---------|------------:|:------------------------------|:----------------|:----------------|:---------------------------------------------------|----------------:|:---------------------|:---------------------------------|:---------------------------|:-----------|:-------------|
| BTC | 78.457 $ | 3 | COSTRUTTIVO MA NON CONFERMATO | Trend misto | Momentum debole | Struttura rialzista con massimi e minimi crescenti | 0 | 0 / IN AVVICINAMENTO | Doppio minimo / TARGET RAGGIUNTO | Doppio massimo / CANDIDATO | 76.248 | 82.262 |
| SOL | 102,02 $ | 6 | COSTRUTTIVO MA NON CONFERMATO | Trend rialzista | Momentum debole | Struttura rialzista con massimi e minimi crescenti | 0 | +1 / TENUTO | Doppio minimo / TARGET RAGGIUNTO | Doppio massimo / CANDIDATO | 97,45 | 110,04 |
| DOGE | 0.08593 $ | -2 | NEUTRALE / MISTO | Trend misto | Momentum misto | Compressione / triangolo | 0 | 0 / TENUTO | Doppio minimo / TARGET RAGGIUNTO | Doppio massimo / CANDIDATO | 0.08028 | 0.09421 |

## Riepilogo ciclo di vita pattern

| Asset   | Doppio minimo    | Triplo minimo    | Adam/Eve Bottom                        | Doppio massimo   | Triplo massimo   | Adam/Eve Top                 |   Punteggio pattern |
|:--------|:-----------------|:-----------------|:---------------------------------------|:-----------------|:-----------------|:-----------------------------|--------------------:|
| BTC | TARGET RAGGIUNTO | TARGET RAGGIUNTO | Adam and Eve Bottom — TARGET RAGGIUNTO | CANDIDATO | CANDIDATO | ASSENTE | 0 |
| SOL | TARGET RAGGIUNTO | TARGET RAGGIUNTO | Adam and Eve Bottom — TARGET RAGGIUNTO | CANDIDATO | CANDIDATO | Adam and Eve Top — CANDIDATO | 0 |
| DOGE | TARGET RAGGIUNTO | TARGET RAGGIUNTO | Adam and Eve Bottom — TARGET RAGGIUNTO | CANDIDATO | CANDIDATO | Adam and Eve Top — CANDIDATO | 0 |

## Indicatori tecnici

| Asset   |   RSI 14 |   Istogramma MACD | MA20    | MA50    | MA200   | Pendenza MA50 20g   | Pendenza MA200 60g   | Rendimento 30g   | Rendimento 90g   |
|:--------|---------:|------------------:|:--------|:--------|:--------|:--------------------|:---------------------|:-----------------|:-----------------|
| BTC | 60.14 | -489.018 | 78.706 | 70.198 | 69.919 | 8,71% | -5,34% | 23,45% | 23,47% |
| SOL | 59.46 | -0.79177 | 101,47 | 85,93 | 82,72 | 11,77% | -9,83% | 33,89% | 52,84% |
| DOGE | 53.86 | -0.00016 | 0.08739 | 0.07740 | 0.08828 | 6,97% | -12,60% | 19,63% | -0,04% |

## Dettaglio asset

### BTC

- Prezzo: **78.457 $**
- Punteggio tecnico: **3 / 12**
- Verdetto: **COSTRUTTIVO MA NON CONFERMATO**
- Trend: **Trend misto** (1)
- Momentum: **Momentum debole** (-2)
- Volume: **Volume neutrale** (0)
- Struttura: **Struttura rialzista con massimi e minimi crescenti** (2)
  - Dettaglio struttura: Ultimi minimi: 6.249e+04 -> 7.625e+04. Ultimi massimi: 8.135e+04 -> 8.226e+04.
- Divergenza: **Nessuna** (0)
- Fase Wyckoff candidata: **Markup / fase rialzista** (2)
  - Dettaglio Wyckoff: Prezzo sopra MA200, MA50 in salita e trend a 30 giorni positivo.
- Fibonacci automatico: **IN AVVICINAMENTO** (0)
  - Swing UP 2026-07-01 57.748 -> 2026-09-03 82.262; livello più vicino 23.6% a 76.477; stato IN AVVICINAMENTO; confluenza: supporto tecnico.
- Punteggio pattern: **0**
  - rialzista dominante: Doppio minimo (TARGET RAGGIUNTO, 0); ribassista dominante: Doppio massimo (CANDIDATO, 0).
- Supporto più vicino: **76.248**
- Resistenza più vicina: **82.262**

Pattern classici e ciclo di vita:

- Doppio minimo: **TARGET RAGGIUNTO** (0)
  - Due minimi simili vicino a 62.227 tra 2026-08-03 e 2026-08-14. Neckline stimata: 65.402. Breakout neckline: 2026-08-19 (22 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 68.577; progresso corrente: 411,16%. Relazione prezzo/neckline: sopra neckline.
  - neckline 65.402; target 68.577; breakout 2026-08-19 (22g); progresso 411,16%; prezzo sopra neckline.
- Triplo minimo: **TARGET RAGGIUNTO** (0)
  - Tre minimi simili vicino a 62.201 dal 2026-06-18 al 2026-08-14. Neckline stimata: 66.910. Breakout neckline: 2026-08-19 (22 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 71.619; progresso corrente: 245,21%. Relazione prezzo/neckline: sopra neckline.
  - neckline 66.910; target 71.619; breakout 2026-08-19 (22g); progresso 245,21%; prezzo sopra neckline.
- Adam and Eve Bottom: **TARGET RAGGIUNTO** (0)
  - Pattern Adam and Eve Bottom vicino a 58.076 dal 2026-06-25 al 2026-08-14. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 66.910. Breakout neckline: 2026-08-19 (22 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 75.744; progresso corrente: 130,70%. Relazione prezzo/neckline: sopra neckline.
  - neckline 66.910; target 75.744; breakout 2026-08-19 (22g); progresso 130,70%; prezzo sopra neckline.
- Doppio massimo: **CANDIDATO** (0)
  - Due massimi simili vicino a 65.508 tra 2026-07-15 e 2026-08-09. Neckline ribassista stimata: 62.227. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 32 giorni.
  - neckline 62.227; target 58.946; distanza dalla neckline 26,08%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 65.544 dal 2026-06-22 al 2026-08-09. Neckline ribassista stimata: 57.748. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 32 giorni.
  - neckline 57.748; target 49.952; distanza dalla neckline 35,86%; prezzo sopra neckline.
- Adam/Eve Top: **ASSENTE** (0)

### SOL

- Prezzo: **102,02 $**
- Punteggio tecnico: **6 / 12**
- Verdetto: **COSTRUTTIVO MA NON CONFERMATO**
- Trend: **Trend rialzista** (3)
- Momentum: **Momentum debole** (-2)
- Volume: **Volume neutrale** (0)
- Struttura: **Struttura rialzista con massimi e minimi crescenti** (2)
  - Dettaglio struttura: Ultimi minimi: 74.2 -> 97.45. Ultimi massimi: 77.62 -> 110.
- Divergenza: **Nessuna** (0)
- Fase Wyckoff candidata: **Markup / fase rialzista** (2)
  - Dettaglio Wyckoff: Prezzo sopra MA200, MA50 in salita e trend a 30 giorni positivo.
- Fibonacci automatico: **TENUTO** (+1)
  - Swing UP 2026-06-06 60,41 -> 2026-08-27 110,04; livello più vicino 23.6% a 98,33; stato TENUTO; confluenza: supporto tecnico.
- Punteggio pattern: **0**
  - rialzista dominante: Doppio minimo (TARGET RAGGIUNTO, 0); ribassista dominante: Doppio massimo (CANDIDATO, 0).
- Supporto più vicino: **97,45**
- Resistenza più vicina: **110,04**

Pattern classici e ciclo di vita:

- Doppio minimo: **TARGET RAGGIUNTO** (0)
  - Due minimi simili vicino a 73,40 tra 2026-07-17 e 2026-08-16. Neckline stimata: 78,73. Breakout neckline: 2026-08-19 (22 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 84,05; progresso corrente: 437,51%. Relazione prezzo/neckline: sopra neckline.
  - neckline 78,73; target 84,05; breakout 2026-08-19 (22g); progresso 437,51%; prezzo sopra neckline.
- Triplo minimo: **TARGET RAGGIUNTO** (0)
  - Tre minimi simili vicino a 70,69 dal 2026-07-17 al 2026-08-16. Neckline stimata: 78,73. Breakout neckline: 2026-08-19 (22 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 86,76; progresso corrente: 290,02%. Relazione prezzo/neckline: sopra neckline.
  - neckline 78,73; target 86,76; breakout 2026-08-19 (22g); progresso 290,02%; prezzo sopra neckline.
- Adam and Eve Bottom: **TARGET RAGGIUNTO** (0)
  - Pattern Adam and Eve Bottom vicino a 67,92 dal 2026-06-19 al 2026-08-01. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 83,81. Breakout neckline: 2026-08-19 (22 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 99,70; progresso corrente: 114,61%. Relazione prezzo/neckline: sopra neckline.
  - neckline 83,81; target 99,70; breakout 2026-08-19 (22g); progresso 114,61%; prezzo sopra neckline.
- Doppio massimo: **CANDIDATO** (0)
  - Due massimi simili vicino a 78,88 tra 2026-07-15 e 2026-08-09. Neckline ribassista stimata: 70,69. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 32 giorni.
  - neckline 70,69; target 62,51; distanza dalla neckline 44,31%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 78,88 dal 2026-07-15 al 2026-08-09. Neckline ribassista stimata: 70,69. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 32 giorni.
  - neckline 70,69; target 62,51; distanza dalla neckline 44,31%; prezzo sopra neckline.
- Adam and Eve Top: **CANDIDATO** (0)
  - Pattern Adam and Eve Top vicino a 77,62 dal 2026-06-22 al 2026-08-09. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 64,42. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 32 giorni.
  - neckline 64,42; target 51,22; distanza dalla neckline 58,37%; prezzo sopra neckline.

### DOGE

- Prezzo: **0.08593 $**
- Punteggio tecnico: **-2 / 12**
- Verdetto: **NEUTRALE / MISTO**
- Trend: **Trend misto** (-1)
- Momentum: **Momentum misto** (-1)
- Volume: **Volume neutrale** (0)
- Struttura: **Compressione / triangolo** (0)
  - Dettaglio struttura: Ultimi minimi: 0.06895 -> 0.08028. Ultimi massimi: 0.09998 -> 0.09421.
- Divergenza: **Nessuna** (0)
- Fase Wyckoff candidata: **Range / fase non chiara** (0)
  - Dettaglio Wyckoff: Posizione nel range a 120 giorni: 35,71%. Fase non abbastanza chiara.
- Fibonacci automatico: **TENUTO** (0)
  - Swing UP 2026-08-01 0.06797 -> 2026-09-05 0.09421; livello più vicino 38.2% a 0.08419; stato TENUTO; confluenza: nessuna confluenza indipendente.
- Punteggio pattern: **0**
  - rialzista dominante: Doppio minimo (TARGET RAGGIUNTO, 0); ribassista dominante: Doppio massimo (CANDIDATO, 0).
- Supporto più vicino: **0.08028**
- Resistenza più vicina: **0.09421**

Pattern classici e ciclo di vita:

- Doppio minimo: **TARGET RAGGIUNTO** (0)
  - Due minimi simili vicino a 0.06829 tra 2026-07-24 e 2026-08-12. Neckline stimata: 0.07380. Breakout neckline: 2026-08-19 (22 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 0.07931; progresso corrente: 220,03%. Relazione prezzo/neckline: sopra neckline.
  - neckline 0.07380; target 0.07931; breakout 2026-08-19 (22g); progresso 220,03%; prezzo sopra neckline.
- Triplo minimo: **TARGET RAGGIUNTO** (0)
  - Tre minimi simili vicino a 0.06895 dal 2026-07-08 al 2026-08-12. Neckline stimata: 0.07380. Breakout neckline: 2026-08-19 (22 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 0.07866; progresso corrente: 249,87%. Relazione prezzo/neckline: sopra neckline.
  - neckline 0.07380; target 0.07866; breakout 2026-08-19 (22g); progresso 249,87%; prezzo sopra neckline.
- Adam and Eve Bottom: **TARGET RAGGIUNTO** (0)
  - Pattern Adam and Eve Bottom vicino a 0.06829 dal 2026-07-24 al 2026-08-06. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 0.07380. Breakout neckline: 2026-08-19 (22 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 0.07931; progresso corrente: 220,03%. Relazione prezzo/neckline: sopra neckline.
  - neckline 0.07380; target 0.07931; breakout 2026-08-19 (22g); progresso 220,03%; prezzo sopra neckline.
- Doppio massimo: **CANDIDATO** (0)
  - Due massimi simili vicino a 0.07380 tra 2026-07-26 e 2026-08-11. Neckline ribassista stimata: 0.06797. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 30 giorni.
  - neckline 0.06797; target 0.06214; distanza dalla neckline 26,42%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 0.07923 dal 2026-07-04 al 2026-08-11. Neckline ribassista stimata: 0.06797. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 30 giorni.
  - neckline 0.06797; target 0.05671; distanza dalla neckline 26,42%; prezzo sopra neckline.
- Adam and Eve Top: **CANDIDATO** (0)
  - Pattern Adam and Eve Top vicino a 0.07923 dal 2026-07-04 al 2026-08-11. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 0.06797. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 30 giorni.
  - neckline 0.06797; target 0.05671; distanza dalla neckline 26,42%; prezzo sopra neckline.

## Fibonacci automatico

Il modulo seleziona uno swing recente tramite pivot confermati. Un semplice tocco vale 0: Fibonacci pesa al massimo ±1 soltanto quando il livello è tenuto, perso, recuperato o respinto e coincide con almeno un livello tecnico indipendente.

| Asset   | Swing                       | 23,6%   | 38,2%   | 50,0%   | 61,8%   | 78,6%   | Livello vicino   | Stato            | Confluenza                      |   Score |
|:--------|:----------------------------|:--------|:--------|:--------|:--------|:--------|:-----------------|:-----------------|:--------------------------------|--------:|
| BTC | UP 2026-07-01 -> 2026-09-03 | 76.477 | 72.898 | 70.005 | 67.112 | 62.994 | 23.6% / 76.477 | IN AVVICINAMENTO | supporto tecnico | 0 |
| SOL | UP 2026-06-06 -> 2026-08-27 | 98,33 | 91,08 | 85,23 | 79,37 | 71,03 | 23.6% / 98,33 | TENUTO | supporto tecnico | +1 |
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

- **BTC**: 30/30 previsioni controllate su 68 fatte. Stato: **ATTIVA**.
- **SOL**: 30/30 previsioni controllate su 68 fatte. Stato: **ATTIVA**.
- **DOGE**: 30/30 previsioni controllate su 68 fatte. Stato: **ATTIVA**.

| Asset | Previsioni fatte | Controllate | Progresso | In attesa | Stato | Prossimo controllo |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 68 | 30 | 30/30 [██████████] | 38 | ATTIVA | 2026-09-13 / tra 3 giorni |
| SOL | 68 | 30 | 30/30 [██████████] | 38 | ATTIVA | 2026-09-13 / tra 3 giorni |
| DOGE | 68 | 30 | 30/30 [██████████] | 38 | ATTIVA | 2026-09-13 / tra 3 giorni |

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

Generato: 2026-09-10 05:33 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [data_quality_coherence_report.md](data_quality_coherence_report.md)

Questo controllo non modifica punteggi o decisioni. Verifica che tutti i moduli usino lo stesso prezzo corrente e che le nuove regole Technical/Classic Visual siano integre.

## Stato finale: **WARN**

## Avvisi

- 3 campi prezzo superano la tolleranza specifica del modulo.

## Prezzo unico per modulo

| Modulo                  | Asset   | Campo             | Stato   | Prezzo snapshot   | Prezzo modulo   | Differenza   |
|:------------------------|:--------|:------------------|:--------|:------------------|:----------------|:-------------|
| Scanner                 | BTC     | current_price     | OK      | 78.457 $          | 78.457 $        | +0,0000%     |
| Scanner                 | DOGE    | current_price     | OK      | 0.08593 $         | 0.08593 $       | +0,0000%     |
| Scanner                 | SOL     | current_price     | OK      | 102,02 $          | 102,02 $        | +0,0000%     |
| Scanner Forecast        | BTC     | current_price     | OK      | 78.457 $          | 78.457 $        | +0,0000%     |
| Scanner Forecast        | SOL     | current_price     | OK      | 102,02 $          | 102,02 $        | +0,0000%     |
| Scanner Forecast        | DOGE    | current_price     | OK      | 0.08593 $         | 0.08593 $       | +0,0000%     |
| Technical Structure     | BTC     | price             | OK      | 78.457 $          | 78.457 $        | +0,0000%     |
| Technical Structure     | SOL     | price             | OK      | 102,02 $          | 102,02 $        | +0,0000%     |
| Technical Structure     | DOGE    | price             | OK      | 0.08593 $         | 0.08593 $       | +0,0000%     |
| Classic Technical       | BTC     | price             | OK      | 78.457 $          | 78.457 $        | +0,0000%     |
| Classic Technical       | SOL     | price             | OK      | 102,02 $          | 102,02 $        | +0,0000%     |
| Classic Technical       | DOGE    | price             | OK      | 0.08593 $         | 0.08593 $       | +0,0000%     |
| Classic Visual          | BTC     | price             | OK      | 78.457 $          | 78.457 $        | +0,0000%     |
| Classic Visual          | SOL     | price             | OK      | 102,02 $          | 102,02 $        | +0,0000%     |
| Classic Visual          | DOGE    | price             | OK      | 0.08593 $         | 0.08593 $       | +0,0000%     |
| Exchange Microstructure | BTC     | price             | WARN    | 78.457 $          | 78.268 $        | -0,2409%     |
| Exchange Microstructure | SOL     | price             | WARN    | 102,02 $          | 101,73 $        | -0,2843%     |
| Exchange Microstructure | DOGE    | price             | WARN    | 0.08593 $         | 0.08551 $       | -0,4888%     |
| RSI top-cycle           | SOL     | current_price     | OK      | 102,02 $          | 102,02 $        | +0,0000%     |
| RSI top-cycle           | SOL     | current_price     | OK      | 102,02 $          | 102,02 $        | +0,0000%     |
| Frattale BTC/SOL        | SOL     | sol_current_price | OK      | 102,02 $          | 102,02 $        | +0,0000%     |
| Fractal path            | SOL     | current_price     | OK      | 102,02 $          | 102,02 $        | +0,0000%     |

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

Generato: 2026-09-10T20:30:34+00:00

- Modalità: **SOLO PAPER TRADING**
- Asset: **SOL spot**
- Leva: **nessuna (1x)**
- Capitale iniziale separato: **€40.000,00**
- Fonte mercato: **KUCOIN_PUBLIC_API**; nuove entrate: **CONSENTITE**

| Equity | Cash | SOL | Prezzo | Rendimento | Realizzato | Commissioni | Max DD | Operazioni |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €44.508,76 | €14.502,17 | 301.189315 | 99.6270 | +11.27% | €4.505,48 | €138,25 | 6.48% | 66 |

**Ultima decisione:** BUY_TRANCHE — SOL sotto la prima banda adattiva.

Bande 4H: L2 96.9988 · L1 99.8974 · media 103.5206 · U1 107.1438 · U2 110.0424.

> Questo portafoglio non condivide capitale, posizioni o statistiche con il paper trading da €10.000.
<!-- SOL_SPOT_ADAPTIVE_END -->
