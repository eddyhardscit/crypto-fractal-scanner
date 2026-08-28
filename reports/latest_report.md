<!-- COMPACT_REPORT_HEADER_START -->
> **Vista compatta:** Decisione operativa, Global Confluence e cambiamenti giornalieri restano aperti. Tocca il titolo di una sezione per mostrare o nascondere i dettagli.  
> Tutte le tabelle e tutti i dati restano nel file: copiando il Markdown raw viene copiato tutto.
<!-- COMPACT_REPORT_HEADER_END -->

<!-- COMPACT_SECTION_START:decision -->
<details open>
<summary><strong>🧭 Decisione operativa — da leggere per prima</strong></summary>

<!-- DECISION_REPORT_START -->

# Decisione operativa sintetica

Generato: 2026-08-28 08:02 UTC

Report separato completo: [decision_report.md](decision_report.md)

Sintesi automatica dello scanner: l'azione spot viene copiata direttamente dal Global Confluence; long, short e rischio restano filtri separati e più prudenti.

| Asset | Global | Direzione | Spot | Long leva | Short leva | Max long | Max short | Rischio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +7 | BULLISH | ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA | LONG PRUDENTE | NO SHORT | max 2x isolated | nessuna | MEDIO |
| SOL | +8 | BULLISH | HOLD / ACCUMULO A TRANCHE, NO LEVA AGGRESSIVA | NO LONG A LEVA | NO SHORT | nessuna | nessuna | MOLTO ALTO |
| DOGE | 0 | NEUTRALE / INCERTO | STAI ALLA FINESTRA | NO LONG A LEVA | NO SHORT | nessuna | nessuna | MOLTO ALTO |

## Lettura immediata

- **BTC**: Global = **+7**, spot = **ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA**, long = **LONG PRUDENTE**, short = **NO SHORT**, rischio = **MEDIO**.
- **SOL**: Global = **+8**, spot = **HOLD / ACCUMULO A TRANCHE, NO LEVA AGGRESSIVA**, long = **NO LONG A LEVA**, short = **NO SHORT**, rischio = **MOLTO ALTO**.
- **DOGE**: Global = **0**, spot = **STAI ALLA FINESTRA**, long = **NO LONG A LEVA**, short = **NO SHORT**, rischio = **MOLTO ALTO**.

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

- Global Confluence: **+8**
- Confluenza: **POSITIVA FORTE**
- Bias Global: **Rialzista**
- Direzione decisionale: **BULLISH**
- Azione spot dal Global: **HOLD / ACCUMULO A TRANCHE, NO LEVA AGGRESSIVA**
- Long leva: **NO LONG A LEVA**
- Short leva: **NO SHORT**
- Rischio: **MOLTO ALTO**
- Conferme: Doppio minimo target raggiunto finché mantiene 78,73; nuova conferma tecnica sopra 127,97; milestone analogiche 121,18 / 148,37, valide soltanto se rientra anche il gap frattale.
- Invalidazioni: Allarmi sotto 98,53 / 74,20 / 62,19.

### DOGE

- Global Confluence: **0**
- Confluenza: **MISTA / PARZIALE**
- Bias Global: **Neutrale / misto**
- Direzione decisionale: **NEUTRALE / INCERTO**
- Azione spot dal Global: **STAI ALLA FINESTRA**
- Long leva: **NO LONG A LEVA**
- Short leva: **NO SHORT**
- Rischio: **MOLTO ALTO**
- Conferme: Sopra 0.09998 migliora; sopra 0.06933 viene invalidato il pattern ribassista dominante.
- Invalidazioni: Sotto 0.06895 il rischio ribassista aumenta.

## Nota semplice

- **Spot** = usa la stessa azione del Global Confluence, senza una seconda mappatura che possa produrre frasi diverse.
- **Zona alta storica** = zona dove non inseguire troppo; può essere zona da prendere profitto.
- **Zona bassa storica** = zona di rischio; con leva la liquidazione non dovrebbe stare lì vicino.
- **BTC leva** = nessun long a leva finché il prezzo snapshot non supera **67.248 $**; sotto quella soglia resta solo l'azione spot indicata dal Global.
- **Lifecycle EMA200** = per SOL resta solo contesto, peso Global 0; score interno 2; EMA200 circa 111,43 $; upside verso EMA200 +4,59%. Non autorizza leva e non aggiunge punti automatici.
- **NO LONG** non significa automaticamente **SHORT**. Lo short ha senso solo se il quadro è bearish o se lo spike viene spesso scaricato.
- Per SOL, se il Global è da **+3 in su**, la decisione non deve diventare bearish solo perché lo scanner grezzo a 30 giorni è incerto.

<!-- DECISION_REPORT_END -->

<!-- PAPER_TRADING_START -->
# Paper trading automatico KuCoin

Generato: 2026-08-28T08:02:46+00:00


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [paper_trading_report.md](paper_trading_report.md)

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-08-28T07:05:30+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-08-28T07:05:30+00:00 | 2026-08-28T07:05:30+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-08-28T06:45:00+00:00 | 2026-08-28T06:45:00+00:00 | 5,6 min | 25,0 min | OK |
| 60m | 12 | 2026-08-28T06:00:00+00:00 | 2026-08-28T06:00:00+00:00 | 5,6 min | 45,0 min | OK |
| 240m | 12 | 2026-08-28T00:00:00+00:00 | 2026-08-28T00:00:00+00:00 | 3,09 h | 1,00 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | TRUMP | 240m | LONG | 8,25 | 6,00 | 0,00 | STALE_CANDLE | 3,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 185.6 minuti; tolleranza 60 minuti. |
| Principale 4H | HYPE | 240m | LONG | 7,36 | 6,00 | 0,00 | STALE_CANDLE | 3,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 185.6 minuti; tolleranza 60 minuti. |
| Principale 4H | TAO | 240m | LONG | 5,82 | 6,00 | 0,18 | STALE_CANDLE | 3,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 185.6 minuti; tolleranza 60 minuti. |
| Principale 4H | BTC | 240m | LONG | 4,75 | 6,00 | 1,25 | STALE_CANDLE | 3,09 h | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 185.6 minuti; tolleranza 60 minuti. |
| Principale 4H | ETH | 240m | LONG | 4,49 | 6,00 | 1,51 | STALE_CANDLE | 3,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 185.6 minuti; tolleranza 60 minuti. |
| Principale 4H | ZEC | 240m | LONG | 3,60 | 6,00 | 2,40 | STALE_CANDLE | 3,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 185.6 minuti; tolleranza 60 minuti. |
| Principale 4H | XRP | 240m | LONG | 2,60 | 6,00 | 3,40 | STALE_CANDLE | 3,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 185.6 minuti; tolleranza 60 minuti. |
| Principale 4H | PEPE | 240m | LONG | 2,30 | 6,00 | 3,70 | STALE_CANDLE | 3,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 185.6 minuti; tolleranza 60 minuti. |
| Principale 4H | DOGE | 240m | SHORT | -1,53 | 6,00 | 4,47 | STALE_CANDLE | 3,09 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 185.6 minuti; tolleranza 60 minuti. |
| Principale 4H | SUI | 240m | SHORT | 0,00 | 6,00 | 6,00 | STALE_CANDLE | 3,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 185.6 minuti; tolleranza 60 minuti. |
| Benchmark trend following EMA 1H | TRUMP | 60m | LONG | 8,25 | 5,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Master Adaptive Expanded V1 | TRUMP | 60m | LONG | 8,25 | 0,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Master Adaptive Runner25 V1 | TRUMP | 60m | LONG | 8,25 | 0,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Combo Adaptive Side Regime Guard V1 | TRUMP | 60m | LONG | 8,25 | 5,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Master Adaptive Gb20 Loss Cap V1 | TRUMP | 60m | LONG | 8,25 | 0,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Master Adaptive No Alt V1 | ENA | 60m | LONG | 4,46 | 0,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Master Adaptive Expanded V1 | ENA | 60m | LONG | 4,46 | 0,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Bilanciata 1H V2 | TRUMP | 60m | LONG | 8,25 | 5,50 | 0,00 | STRATEGY_FILTER | 5,6 min | D: n/a | W: n/a | peso 0 | Filtro V2 non superato: regime, EMA, ritorni e RSI; per Rapida V2 servono anche breakout reale, volume e ADX. |
| Rapida 1H V2 | TRUMP | 60m | LONG | 8,25 | 5,00 | 0,00 | STRATEGY_FILTER | 5,6 min | D: n/a | W: n/a | peso 0 | Filtro V2 non superato: regime, EMA, ritorni e RSI; per Rapida V2 servono anche breakout reale, volume e ADX. |
| Bilanciata 1H V1 | TRUMP | 60m | LONG | 8,25 | 5,00 | 0,00 | RISK_GATE | 5,6 min | D: n/a | W: n/a | peso 0 | Filtro rischio/esecuzione: blocco perdita monthly raggiunto. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.864,93 | -1,35% | €116,59 | €3.000,00 | 3,89% | 6 | 52 | 38,46% | 0,87 | 6,86% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 52 | 2382 | PRIME INDICAZIONI | 100 (mancano 48) |

- Trade del Principale 4H chiusi: **52**; win rate **38,46%**; profit factor **0,87**.
- Expectancy: **€-3,67** per trade; P&L netto: **€-190,76**; max drawdown: **6,86%**.
- Valutazione: **Si può osservare la direzione, ma il risultato resta fragile.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 6 | €9.864,93 | €699,00 | €2.096,99 | €194,16 | €56,81 |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | 5 | €11.345,14 | €563,84 | €1.691,51 | €170,37 | €0,00 |
| TEST | Benchmark Donchian breakout 1H | 3 | €11.190,04 | €921,22 | €1.842,43 | €109,41 | €-2,11 |
| TEST | Combo Trend Side Regime Guard V1 | 5 | €11.131,79 | €858,00 | €1.715,99 | €116,13 | €14,48 |
| TEST | Scanner Top 5 Long 1H | 4 | €11.070,19 | €511,90 | €1.023,79 | €110,47 | €55,24 |
| TEST | Donchian 1H Gb20 120R V1 | 3 | €10.926,58 | €899,53 | €1.799,06 | €106,84 | €-2,06 |
| TEST | Main Side Regime Guard V1 | 6 | €10.879,75 | €677,89 | €2.033,66 | €163,42 | €58,77 |
| TEST | 1H Fast No Pepe V1 | 6 | €10.701,25 | €843,47 | €2.530,42 | €212,30 | €20,13 |
| TEST | Combo Adaptive | 6 | €10.675,17 | €985,07 | €1.970,13 | €162,16 | €-10,97 |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | 6 | €10.667,77 | €1.243,40 | €3.730,21 | €212,77 | €10,19 |
| TEST | Rapida 1H V3 Filtered | 6 | €10.599,23 | €1.235,42 | €3.706,25 | €211,41 | €10,12 |
| TEST | Combo Adaptive Long Only V1 | 4 | €10.473,08 | €1.693,60 | €3.387,21 | €104,90 | €9,61 |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | 3 | €10.471,49 | €609,19 | €1.827,57 | €153,66 | €20,43 |
| TEST | Combo Adaptive Side Regime Guard V1 | 6 | €10.407,47 | €1.016,95 | €2.033,90 | €156,23 | €-14,03 |
| TEST | 1H Fast Tp2 V1 | 5 | €10.395,04 | €757,29 | €2.271,86 | €157,22 | €19,77 |
| TEST | Rapida 1H V2 | 0 | €10.359,25 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Ampia 4H | 7 | €10.344,68 | €1.057,57 | €2.115,14 | €205,57 | €65,26 |
| TEST | Sol Donchian 1H | 0 | €10.305,79 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 0 | €10.300,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top 5 + forza BTC 1H | 4 | €10.293,40 | €474,73 | €949,47 | €102,86 | €51,95 |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | 0 | €10.277,64 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 0 | €10.271,73 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 4H | 1 | €10.259,35 | €367,30 | €734,59 | €0,00 | €65,92 |
| TEST | 1H Fast V3 Nohigh Range Only V1 | 0 | €10.247,95 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 0 | €10.239,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 0 | €10.235,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Donchian 4H | 1 | €10.222,37 | €449,62 | €899,24 | €50,98 | €26,41 |
| TEST | Scanner Top5 Btc Tp3 V1 | 5 | €10.220,71 | €1.771,68 | €3.543,37 | €202,54 | €15,23 |
| TEST | Scanner Top5 Btc Runner25 V1 | 5 | €10.214,73 | €1.770,65 | €3.541,29 | €202,42 | €15,22 |
| TEST | Btc Bollinger 1H | 0 | €10.209,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top10 Long | 4 | €10.204,14 | €2.227,69 | €4.455,38 | €200,73 | €8,41 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 0 | €10.185,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 1H | 0 | €10.177,93 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Main Dynamic Asset Selector V1 | 2 | €10.160,27 | €429,03 | €1.287,09 | €101,56 | €-0,41 |
| TEST | Combo Adaptive Partial 1R V1 | 4 | €10.153,18 | €1.920,85 | €3.841,70 | €147,19 | €76,05 |
| TEST | 1H Fast Score 6 75 Range Only V1 | 0 | €10.149,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 0 | €10.145,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Nohigh Cap75 V1 | 3 | €10.140,52 | €413,61 | €1.240,82 | €148,08 | €0,00 |
| TEST | 1H Fast V3 No Esports Long Only V1 | 4 | €10.137,17 | €597,50 | €1.792,49 | €150,44 | €19,78 |
| TEST | Sol Ema 4H | 1 | €10.126,43 | €395,27 | €790,53 | €0,00 | €70,93 |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 0 | €10.099,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 4H | 1 | €10.058,90 | €648,94 | €1.297,88 | €50,35 | €-10,13 |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 0 | €10.048,77 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €10.045,08 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V1 | 0 | €10.043,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 4H | 1 | €10.040,46 | €775,58 | €1.551,16 | €50,15 | €11,49 |
| TEST | 1H Balanced Short Trend Down Strict V1 | 0 | €10.035,46 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 1H | 0 | €10.033,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · prudente · 5x | 0 | €10.028,67 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €50 · 15x | 0 | €10.017,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | 0 | €10.011,54 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €50 · 15x | 0 | €10.009,44 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 0 | €10.009,02 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 0 | €10.008,92 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 4H | 1 | €10.007,16 | €704,37 | €1.408,74 | €50,10 | €-10,99 |
| TEST | Scalp RSI Short 85 · €10 · 15x | 0 | €10.003,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 0 | €10.003,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €10 · 15x | 0 | €10.001,89 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Continuation V1 | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €10 · 15x | 0 | €9.999,33 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €10 · 15x | 0 | €9.997,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €50 · 15x | 0 | €9.996,64 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 0 | €9.995,23 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Bollinger 1H | 0 | €9.992,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · prudente · 5x | 0 | €9.991,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €10 · 15x | 0 | €9.990,45 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Ema 1H | 0 | €9.988,85 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €50 · 15x | 0 | €9.988,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 0 | €9.987,48 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · prudente · 5x | 0 | €9.980,94 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 1H | 0 | €9.968,58 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | 1 | €9.962,53 | €361,10 | €722,20 | €49,74 | €15,12 |
| TEST | Btc Donchian 1H | 0 | €9.957,15 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Ema 4H | 1 | €9.954,28 | €487,73 | €975,47 | €0,00 | €44,17 |
| TEST | Btc Donchian 4H | 1 | €9.953,62 | €700,60 | €1.401,20 | €49,83 | €-10,93 |
| TEST | Scalp RSI Long 25 · €50 · 15x | 0 | €9.952,25 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.939,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · prudente · 5x | 0 | €9.939,55 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 4H | 1 | €9.931,32 | €478,97 | €957,94 | €49,65 | €1,25 |
| TEST | Doge Donchian 1H | 0 | €9.924,84 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top15 Long | 7 | €9.907,76 | €1.336,00 | €2.672,00 | €146,37 | €49,08 |
| TEST | Scanner Top20 Long | 7 | €9.907,76 | €1.336,00 | €2.672,00 | €146,37 | €49,08 |
| TEST | 1H Fast V3 Nohigh V1 | 4 | €9.905,36 | €581,14 | €1.743,42 | €147,13 | €19,32 |
| TEST | Combo Scanner | 4 | €9.889,79 | €458,53 | €917,05 | €98,83 | €49,93 |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | 3 | €9.888,18 | €403,32 | €1.209,95 | €144,39 | €0,00 |
| TEST | Combo Adaptive Regime V1 | 3 | €9.874,22 | €1.549,75 | €3.099,50 | €147,54 | €14,99 |
| TEST | Eth Adaptive 1H | 0 | €9.873,49 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H V3 Filtered | 3 | €9.850,95 | €1.031,61 | €3.094,83 | €100,21 | €-31,44 |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 0 | €9.837,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Quality7 Regime V1 | 1 | €9.837,22 | €356,56 | €713,12 | €49,11 | €14,93 |
| TEST | 1H Fast V3 No Esports V1 | 5 | €9.832,09 | €765,42 | €2.296,25 | €195,43 | €18,76 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 0 | €9.817,34 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Long Only V1 | 5 | €9.807,73 | €1.130,28 | €3.390,83 | €194,23 | €10,45 |
| TEST | Forza relativa 1H V2 | 4 | €9.804,86 | €961,34 | €1.922,67 | €146,29 | €14,88 |
| TEST | Btc Ema 1H | 1 | €9.803,39 | €1.138,16 | €3.414,47 | €49,17 | €-28,19 |
| TEST | Eth Ema 1H | 0 | €9.799,26 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 1H | 1 | €9.799,11 | €697,47 | €2.092,40 | €0,00 | €31,47 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 0 | €9.762,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 0 | €9.723,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Balanced Long No Rhv V1 | 5 | €9.714,51 | €1.239,35 | €3.718,05 | €193,34 | €6,77 |
| TEST | Eth Donchian 1H | 0 | €9.709,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Quality7 V1 | 3 | €9.708,45 | €1.370,09 | €2.740,18 | €144,99 | €7,98 |
| TEST | Eth Bollinger 1H | 0 | €9.703,71 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Global Confluence puro 1H | 0 | €9.679,31 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Mfe V1 | 4 | €9.649,56 | €445,04 | €890,08 | €96,43 | €48,70 |
| TEST | Master Adaptive Gb20 Be V1 | 6 | €9.619,28 | €2.958,17 | €5.916,35 | €191,69 | €15,16 |
| TEST | Master Adaptive Gb20 Partial V1 | 6 | €9.609,05 | €2.955,03 | €5.910,05 | €191,48 | €15,15 |
| TEST | Master Adaptive Runner25 V1 | 7 | €9.603,54 | €3.588,44 | €7.176,88 | €191,71 | €71,44 |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | 1 | €9.600,44 | €134,26 | €402,77 | €48,33 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 0 | €9.579,83 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive V1 | 6 | €9.571,88 | €2.943,60 | €5.887,19 | €190,74 | €15,09 |
| TEST | Scanner Top5 Btc Guard V1 | 4 | €9.544,43 | €413,49 | €826,99 | €96,32 | €2,04 |
| TEST | Master Adaptive No Alt V1 | 5 | €9.481,14 | €2.981,09 | €5.962,17 | €188,97 | €12,92 |
| TEST | Master Adaptive Expanded V1 | 5 | €9.472,68 | €2.920,91 | €5.841,82 | €188,69 | €-5,15 |
| TEST | Bilanciata 1H V2 | 3 | €9.460,09 | €782,72 | €2.348,15 | €140,51 | €14,36 |
| TEST | Master Adaptive Gb20 V1 | 6 | €9.444,42 | €2.909,31 | €5.818,62 | €188,82 | €14,61 |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | 1 | €9.433,66 | €130,02 | €390,07 | €46,81 | €0,00 |
| TEST | 1H Fast Score 6 75 V1 | 0 | €9.415,87 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Mfe Trail | 5 | €9.361,85 | €738,35 | €1.476,69 | €136,03 | €68,01 |
| TEST | Master Adaptive Gb20 Loss Cap V1 | 5 | €9.360,46 | €3.414,16 | €6.828,32 | €186,74 | €3,22 |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | 1 | €9.340,10 | €891,28 | €1.782,56 | €45,68 | €0,00 |
| TEST | Scanner Top5 Btc Guard Mfe V1 | 4 | €9.322,46 | €403,88 | €807,75 | €94,08 | €1,99 |
| TEST | Scanner Bottom10 Short | 4 | €9.320,74 | €1.261,36 | €2.522,73 | €140,86 | €0,00 |
| TEST | Scanner Bottom15 Short | 4 | €9.320,74 | €1.261,36 | €2.522,73 | €140,86 | €0,00 |
| TEST | Scanner Bottom20 Short | 4 | €9.320,74 | €1.261,36 | €2.522,73 | €140,86 | €0,00 |
| TEST | 1H Balanced V3 Long Only V1 | 2 | €9.316,85 | €953,76 | €2.861,28 | €93,22 | €-28,47 |
| TEST | Combo Trend | 5 | €9.308,41 | €1.476,84 | €2.953,67 | €139,33 | €-22,13 |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | 4 | €9.256,15 | €1.252,64 | €2.505,29 | €139,88 | €0,00 |
| TEST | Scanner Bottom5 Short Profit Lock V1 | 4 | €9.242,07 | €1.250,74 | €2.501,48 | €139,67 | €0,00 |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | 1 | €9.215,49 | €12,70 | €25,40 | €2,60 | €2,44 |
| TEST | Benchmark trend following EMA 1H | 5 | €9.198,97 | €1.286,85 | €2.573,71 | €139,56 | €-10,99 |
| TEST | Scanner Bottom 5 Short 1H | 4 | €9.170,95 | €1.241,11 | €2.482,23 | €138,60 | €0,00 |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | 0 | €9.165,52 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H V1 | 0 | €9.150,69 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Cap75 V1 | 0 | €9.106,22 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | 0 | €9.052,49 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Runner25 V1 | 0 | €8.964,11 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Mean Reversion | 0 | €8.918,97 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Btc Le3 V1 | 1 | €8.883,87 | €847,75 | €1.695,49 | €43,45 | €0,00 |
| TEST | Master Adaptive Strict3 V1 | 3 | €8.862,92 | €1.998,95 | €3.997,90 | €133,34 | €8,60 |
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
| PRINCIPALE | Principale 4H | Confluenza trend | €9.864,93 | €-190,76 | 52 | 52 | 38,46% | 0,87 | €-3,67 | 6,86% |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | Momentum / breakout | €11.345,14 | €1.346,38 | 151 | 151 | 53,64% | 1,46 | €8,92 | 5,23% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €11.190,04 | €1.192,45 | 113 | 113 | 46,90% | 1,46 | €10,55 | 6,27% |
| TEST | Combo Trend Side Regime Guard V1 | Combo Trend | €11.131,79 | €1.118,65 | 119 | 119 | 53,78% | 1,53 | €9,40 | 6,20% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €11.070,19 | €1.015,60 | 148 | 148 | 47,97% | 1,36 | €6,86 | 8,85% |
| TEST | Donchian 1H Gb20 120R V1 | Donchian breakout 20 barre | €10.926,58 | €928,94 | 81 | 81 | 45,68% | 1,55 | €11,47 | 6,27% |
| TEST | Main Side Regime Guard V1 | Confluenza trend | €10.879,75 | €822,88 | 37 | 37 | 54,05% | 2,16 | €22,24 | 3,82% |
| TEST | 1H Fast No Pepe V1 | Momentum / breakout | €10.701,25 | €682,86 | 224 | 224 | 46,88% | 1,16 | €3,05 | 7,45% |
| TEST | Combo Adaptive | Combo Adaptive | €10.675,17 | €688,70 | 155 | 155 | 47,10% | 1,27 | €4,44 | 7,91% |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | Momentum / breakout V3 Filtered | €10.667,77 | €659,94 | 194 | 194 | 51,03% | 1,21 | €3,40 | 9,50% |
| TEST | Rapida 1H V3 Filtered | Momentum / breakout V3 Filtered | €10.599,23 | €591,45 | 238 | 238 | 45,38% | 1,14 | €2,49 | 9,48% |
| TEST | Combo Adaptive Long Only V1 | Combo Adaptive | €10.473,08 | €465,50 | 128 | 128 | 47,66% | 1,17 | €3,64 | 7,78% |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | Momentum / breakout V3 Filtered | €10.471,49 | €452,16 | 82 | 82 | 50,00% | 1,28 | €5,51 | 5,24% |
| TEST | Combo Adaptive Side Regime Guard V1 | Combo Adaptive | €10.407,47 | €424,02 | 117 | 117 | 48,72% | 1,19 | €3,62 | 8,68% |
| TEST | 1H Fast Tp2 V1 | Momentum / breakout | €10.395,04 | €376,63 | 237 | 237 | 40,51% | 1,09 | €1,59 | 6,56% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €10.359,25 | €359,25 | 50 | 45 | 50,00% | 1,31 | €7,18 | 3,89% |
| TEST | Ampia 4H | Confluenza trend | €10.344,68 | €280,43 | 52 | 52 | 34,62% | 1,24 | €5,39 | 4,45% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €10.305,79 | €305,79 | 15 | 15 | 60,00% | 2,24 | €20,39 | 2,77% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | Momentum / breakout V3 Filtered | €10.300,05 | €300,05 | 33 | 33 | 48,48% | 2,04 | €9,09 | 2,01% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €10.293,40 | €242,06 | 132 | 132 | 44,70% | 1,09 | €1,83 | 11,27% |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | Momentum / breakout V3 Filtered | €10.277,64 | €277,64 | 62 | 62 | 51,61% | 1,21 | €4,48 | 4,50% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | Momentum / breakout V3 Filtered | €10.271,73 | €271,73 | 22 | 22 | 50,00% | 1,74 | €12,35 | 1,72% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €10.259,35 | €193,98 | 7 | 7 | 57,14% | 2,72 | €27,71 | 1,01% |
| TEST | 1H Fast V3 Nohigh Range Only V1 | Momentum / breakout V3 Filtered | €10.247,95 | €247,95 | 41 | 41 | 46,34% | 1,25 | €6,05 | 3,97% |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | Momentum / breakout V3 Filtered | €10.239,20 | €239,20 | 17 | 17 | 52,94% | 4,50 | €14,07 | 1,01% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | Momentum / breakout V3 Filtered | €10.235,18 | €235,18 | 20 | 20 | 50,00% | 1,90 | €11,76 | 2,73% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €10.222,37 | €196,46 | 6 | 6 | 50,00% | 2,73 | €32,74 | 1,05% |
| TEST | Scanner Top5 Btc Tp3 V1 | Scanner Top 5 + forza BTC | €10.220,71 | €207,92 | 111 | 111 | 42,34% | 1,08 | €1,87 | 11,78% |
| TEST | Scanner Top5 Btc Runner25 V1 | Scanner Top 5 + forza BTC | €10.214,73 | €201,94 | 115 | 115 | 42,61% | 1,08 | €1,76 | 12,06% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.209,20 | €209,20 | 6 | 6 | 83,33% | 4,66 | €34,87 | 0,85% |
| TEST | Scanner Top10 Long | Scanner Top10 Long | €10.204,14 | €198,71 | 138 | 138 | 48,55% | 1,08 | €1,44 | 10,31% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | Momentum / breakout V3 Filtered | €10.185,37 | €185,37 | 22 | 22 | 40,91% | 1,57 | €8,43 | 2,27% |
| TEST | Sol Ema 1H | Trend following EMA | €10.177,93 | €177,93 | 17 | 17 | 47,06% | 1,41 | €10,47 | 3,33% |
| TEST | Main Dynamic Asset Selector V1 | Confluenza trend | €10.160,27 | €161,45 | 13 | 13 | 38,46% | 1,47 | €12,42 | 2,17% |
| TEST | Combo Adaptive Partial 1R V1 | Combo Adaptive | €10.153,18 | €79,41 | 159 | 159 | 45,28% | 1,03 | €0,50 | 8,69% |
| TEST | 1H Fast Score 6 75 Range Only V1 | Momentum / breakout | €10.149,62 | €149,62 | 38 | 38 | 44,74% | 1,14 | €3,94 | 3,35% |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | Momentum / breakout V3 Filtered | €10.145,12 | €145,12 | 44 | 44 | 45,45% | 1,20 | €3,30 | 2,91% |
| TEST | 1H Fast Nohigh Cap75 V1 | Momentum / breakout | €10.140,52 | €141,36 | 152 | 152 | 42,76% | 1,05 | €0,93 | 7,10% |
| TEST | 1H Fast V3 No Esports Long Only V1 | Momentum / breakout V3 Filtered | €10.137,17 | €118,57 | 164 | 164 | 43,90% | 1,03 | €0,72 | 10,60% |
| TEST | Sol Ema 4H | Trend following EMA | €10.126,43 | €56,08 | 8 | 8 | 37,50% | 1,26 | €7,01 | 2,27% |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | Momentum / breakout V3 Filtered | €10.099,04 | €99,04 | 55 | 55 | 54,55% | 1,12 | €1,80 | 3,59% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €10.058,90 | €70,19 | 2 | 2 | 50,00% | 2,39 | €35,09 | 0,96% |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | Momentum / breakout V3 Filtered | €10.048,77 | €48,77 | 23 | 23 | 43,48% | 1,12 | €2,12 | 3,05% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €10.045,08 | €45,08 | 28 | 28 | 46,43% | 1,40 | €1,61 | 0,33% |
| TEST | Rapida 1H V1 | Momentum / breakout | €10.043,28 | €43,28 | 78 | 78 | 34,62% | 1,02 | €0,55 | 6,76% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.040,46 | €29,45 | 2 | 2 | 50,00% | 1,54 | €14,72 | 0,91% |
| TEST | 1H Balanced Short Trend Down Strict V1 | Confluenza trend | €10.035,46 | €35,46 | 13 | 13 | 38,46% | 1,13 | €2,73 | 1,80% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €10.033,18 | €33,18 | 18 | 18 | 44,44% | 1,07 | €1,84 | 4,59% |
| TEST | Scalp RSI Long 20 · prudente · 5x | Inversione RSI estrema 15m | €10.028,67 | €28,67 | 9 | 9 | 55,56% | 1,80 | €3,19 | 0,36% |
| TEST | Scalp RSI Short 85 · €50 · 15x | Inversione RSI estrema 15m | €10.017,98 | €17,98 | 5 | 5 | 60,00% | 1,69 | €3,60 | 0,31% |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | Momentum / breakout | €10.011,54 | €11,54 | 73 | 73 | 42,47% | 1,01 | €0,16 | 4,16% |
| TEST | Scalp RSI Short 80 · €50 · 15x | Inversione RSI estrema 15m | €10.009,44 | €9,44 | 17 | 17 | 41,18% | 1,17 | €0,56 | 0,53% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €10.009,02 | €9,02 | 28 | 28 | 46,43% | 1,40 | €0,32 | 0,07% |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | Momentum / breakout V3 Filtered | €10.008,92 | €8,92 | 30 | 30 | 36,67% | 1,02 | €0,30 | 4,84% |
| TEST | Btc Ema 4H | Trend following EMA | €10.007,16 | €19,41 | 3 | 3 | 33,33% | 1,19 | €6,47 | 1,76% |
| TEST | Scalp RSI Short 85 · €10 · 15x | Inversione RSI estrema 15m | €10.003,60 | €3,60 | 5 | 5 | 60,00% | 1,69 | €0,72 | 0,06% |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | Momentum / breakout V3 Filtered | €10.003,37 | €3,37 | 8 | 8 | 37,50% | 1,02 | €0,42 | 2,15% |
| TEST | Scalp RSI Short 80 · €10 · 15x | Inversione RSI estrema 15m | €10.001,89 | €1,89 | 17 | 17 | 41,18% | 1,17 | €0,11 | 0,11% |
| TEST | Scanner Bottom5 Short Continuation V1 | Scanner Bottom5 Short Continuation | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 20 · €10 · 15x | Inversione RSI estrema 15m | €9.999,33 | €-0,67 | 9 | 9 | 44,44% | 0,85 | €-0,07 | 0,04% |
| TEST | Scalp RSI Long 15 · €10 · 15x | Inversione RSI estrema 15m | €9.997,60 | €-2,40 | 3 | 3 | 33,33% | 0,13 | €-0,80 | 0,02% |
| TEST | Scalp RSI Long 20 · €50 · 15x | Inversione RSI estrema 15m | €9.996,64 | €-3,36 | 9 | 9 | 44,44% | 0,85 | €-0,37 | 0,21% |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | Momentum / breakout V3 Filtered | €9.995,23 | €-4,77 | 15 | 15 | 46,67% | 0,99 | €-0,32 | 2,70% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €9.992,60 | €-7,40 | 10 | 10 | 50,00% | 0,97 | €-0,74 | 1,89% |
| TEST | Scalp RSI Short 85 · prudente · 5x | Inversione RSI estrema 15m | €9.991,38 | €-8,62 | 5 | 5 | 60,00% | 0,61 | €-1,72 | 0,30% |
| TEST | Scalp RSI Long 25 · €10 · 15x | Inversione RSI estrema 15m | €9.990,45 | €-9,55 | 15 | 15 | 40,00% | 0,36 | €-0,64 | 0,14% |
| TEST | Doge Ema 1H | Trend following EMA | €9.988,85 | €-11,15 | 17 | 17 | 58,82% | 0,97 | €-0,66 | 2,77% |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | €9.988,00 | €-12,00 | 3 | 3 | 33,33% | 0,13 | €-4,00 | 0,12% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €9.987,48 | €-12,52 | 15 | 15 | 40,00% | 0,83 | €-0,83 | 0,71% |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | €9.980,94 | €-19,06 | 3 | 3 | 33,33% | 0,19 | €-6,35 | 0,20% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €9.968,58 | €-31,42 | 9 | 9 | 44,44% | 0,86 | €-3,49 | 1,23% |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | Combo Adaptive | €9.962,53 | €-52,16 | 40 | 40 | 47,50% | 0,95 | €-1,30 | 4,21% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €9.957,15 | €-42,85 | 10 | 10 | 50,00% | 0,85 | €-4,29 | 1,49% |
| TEST | Eth Ema 4H | Trend following EMA | €9.954,28 | €-88,72 | 5 | 5 | 20,00% | 0,58 | €-17,74 | 1,83% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €9.953,62 | €-34,19 | 4 | 4 | 25,00% | 0,80 | €-8,55 | 2,43% |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | €9.952,25 | €-47,75 | 15 | 15 | 40,00% | 0,36 | €-3,18 | 0,72% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.939,62 | €-60,38 | 28 | 28 | 46,43% | 0,60 | €-2,16 | 0,84% |
| TEST | Scalp RSI Short 80 · prudente · 5x | Inversione RSI estrema 15m | €9.939,55 | €-60,45 | 17 | 17 | 35,29% | 0,39 | €-3,56 | 0,89% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €9.931,32 | €-69,33 | 4 | 4 | 25,00% | 0,56 | €-17,33 | 1,96% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €9.924,84 | €-75,16 | 13 | 13 | 53,85% | 0,79 | €-5,78 | 3,08% |
| TEST | Scanner Top15 Long | Scanner Top15 Long | €9.907,76 | €-139,40 | 134 | 134 | 48,51% | 0,94 | €-1,04 | 10,31% |
| TEST | Scanner Top20 Long | Scanner Top20 Long | €9.907,76 | €-139,40 | 134 | 134 | 48,51% | 0,94 | €-1,04 | 10,31% |
| TEST | 1H Fast V3 Nohigh V1 | Momentum / breakout V3 Filtered | €9.905,36 | €-112,91 | 132 | 132 | 43,94% | 0,96 | €-0,86 | 7,10% |
| TEST | Combo Scanner | Combo Scanner | €9.889,79 | €-159,56 | 137 | 137 | 44,53% | 0,95 | €-1,16 | 11,38% |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | Momentum / breakout | €9.888,18 | €-111,00 | 116 | 116 | 41,38% | 0,95 | €-0,96 | 7,10% |
| TEST | Combo Adaptive Regime V1 | Combo Adaptive | €9.874,22 | €-138,61 | 65 | 65 | 49,23% | 0,91 | €-2,13 | 5,38% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.873,49 | €-126,51 | 14 | 14 | 42,86% | 0,72 | €-9,04 | 3,14% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €9.850,95 | €-115,67 | 163 | 163 | 41,72% | 0,96 | €-0,71 | 9,12% |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | Momentum / breakout V3 Filtered | €9.837,38 | €-162,62 | 37 | 37 | 40,54% | 0,76 | €-4,40 | 3,08% |
| TEST | Combo Adaptive Quality7 Regime V1 | Combo Adaptive | €9.837,22 | €-177,28 | 40 | 40 | 42,50% | 0,83 | €-4,43 | 5,41% |
| TEST | 1H Fast V3 No Esports V1 | Momentum / breakout V3 Filtered | €9.832,09 | €-185,17 | 210 | 210 | 43,81% | 0,96 | €-0,88 | 9,00% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | Momentum / breakout V3 Filtered | €9.817,34 | €-182,66 | 24 | 24 | 41,67% | 0,64 | €-7,61 | 3,23% |
| TEST | 1H Fast V3 Long Only V1 | Momentum / breakout V3 Filtered | €9.807,73 | €-200,58 | 173 | 173 | 42,20% | 0,94 | €-1,16 | 12,52% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €9.804,86 | €-208,87 | 119 | 112 | 42,86% | 0,94 | €-1,76 | 10,88% |
| TEST | Btc Ema 1H | Trend following EMA | €9.803,39 | €-166,34 | 13 | 13 | 30,77% | 0,61 | €-12,80 | 2,10% |
| TEST | Eth Ema 1H | Trend following EMA | €9.799,26 | €-200,74 | 20 | 20 | 40,00% | 0,71 | €-10,04 | 4,80% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.799,11 | €-231,06 | 12 | 12 | 33,33% | 0,55 | €-19,26 | 2,91% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | Momentum / breakout V3 Filtered | €9.762,18 | €-237,82 | 7 | 7 | 14,29% | 0,02 | €-33,97 | 2,82% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | Momentum / breakout V3 Filtered | €9.723,72 | €-276,28 | 31 | 31 | 32,26% | 0,62 | €-8,91 | 4,83% |
| TEST | 1H Balanced Long No Rhv V1 | Confluenza trend | €9.714,51 | €-289,97 | 105 | 105 | 45,71% | 0,87 | €-2,76 | 9,26% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.709,98 | €-290,02 | 14 | 14 | 28,57% | 0,52 | €-20,72 | 3,74% |
| TEST | Combo Adaptive Quality7 V1 | Combo Adaptive | €9.708,45 | €-297,89 | 83 | 83 | 39,76% | 0,85 | €-3,59 | 8,88% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €9.703,71 | €-296,29 | 7 | 7 | 28,57% | 0,22 | €-42,33 | 4,16% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.679,31 | €-320,69 | 17 | 17 | 29,41% | 0,41 | €-18,86 | 3,93% |
| TEST | Scanner Top5 Btc Mfe V1 | Scanner Top 5 + forza BTC | €9.649,56 | €-398,57 | 124 | 124 | 43,55% | 0,84 | €-3,21 | 12,28% |
| TEST | Master Adaptive Gb20 Be V1 | Master Adaptive Consensus | €9.619,28 | €-392,08 | 65 | 65 | 32,31% | 0,79 | €-6,03 | 8,39% |
| TEST | Master Adaptive Gb20 Partial V1 | Master Adaptive Consensus | €9.609,05 | €-402,29 | 60 | 60 | 36,67% | 0,78 | €-6,70 | 7,98% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €9.603,54 | €-463,09 | 55 | 55 | 32,73% | 0,76 | €-8,42 | 8,18% |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | Momentum / breakout V3 Filtered | €9.600,44 | €-399,22 | 94 | 94 | 40,43% | 0,84 | €-4,25 | 6,64% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | Momentum / breakout V3 Filtered | €9.579,83 | €-420,17 | 11 | 11 | 0,00% | 0,00 | €-38,20 | 4,20% |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | €9.571,88 | €-439,42 | 62 | 62 | 35,48% | 0,78 | €-7,09 | 7,80% |
| TEST | Scanner Top5 Btc Guard V1 | Scanner Top 5 + forza BTC | €9.544,43 | €-456,83 | 114 | 114 | 38,60% | 0,84 | €-4,01 | 7,34% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €9.481,14 | €-527,93 | 65 | 65 | 35,38% | 0,75 | €-8,12 | 7,26% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €9.472,68 | €-518,66 | 69 | 69 | 37,68% | 0,75 | €-7,52 | 7,96% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €9.460,09 | €-552,71 | 111 | 101 | 44,14% | 0,77 | €-4,98 | 8,85% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €9.444,42 | €-566,44 | 97 | 97 | 48,45% | 0,74 | €-5,84 | 9,02% |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | Momentum / breakout V3 Filtered | €9.433,66 | €-565,77 | 98 | 98 | 44,90% | 0,80 | €-5,77 | 8,22% |
| TEST | 1H Fast Score 6 75 V1 | Momentum / breakout | €9.415,87 | €-584,13 | 137 | 137 | 40,15% | 0,84 | €-4,26 | 12,33% |
| TEST | Combo Adaptive Mfe Trail | Combo Adaptive | €9.361,85 | €-705,05 | 168 | 168 | 42,26% | 0,78 | €-4,20 | 15,45% |
| TEST | Master Adaptive Gb20 Loss Cap V1 | Master Adaptive Consensus | €9.360,46 | €-638,42 | 54 | 54 | 25,93% | 0,66 | €-11,82 | 11,41% |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | Scanner Top 5 + forza BTC | €9.340,10 | €-658,83 | 33 | 33 | 24,24% | 0,38 | €-19,96 | 8,80% |
| TEST | Scanner Top5 Btc Guard Mfe V1 | Scanner Top 5 + forza BTC | €9.322,46 | €-678,77 | 131 | 131 | 39,69% | 0,78 | €-5,18 | 8,78% |
| TEST | Scanner Bottom10 Short | Scanner Bottom10 Short | €9.320,74 | €-677,79 | 70 | 70 | 31,43% | 0,65 | €-9,68 | 9,06% |
| TEST | Scanner Bottom15 Short | Scanner Bottom15 Short | €9.320,74 | €-677,79 | 70 | 70 | 31,43% | 0,65 | €-9,68 | 9,06% |
| TEST | Scanner Bottom20 Short | Scanner Bottom20 Short | €9.320,74 | €-677,79 | 70 | 70 | 31,43% | 0,65 | €-9,68 | 9,06% |
| TEST | 1H Balanced V3 Long Only V1 | Confluenza trend V3 Filtered | €9.316,85 | €-652,88 | 118 | 118 | 41,53% | 0,72 | €-5,53 | 8,85% |
| TEST | Combo Trend | Combo Trend | €9.308,41 | €-666,88 | 160 | 160 | 39,38% | 0,82 | €-4,17 | 10,85% |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | Scanner Bottom 5 Short | €9.256,15 | €-742,38 | 61 | 61 | 31,15% | 0,58 | €-12,17 | 9,08% |
| TEST | Scanner Bottom5 Short Profit Lock V1 | Scanner Bottom 5 Short | €9.242,07 | €-756,47 | 62 | 62 | 30,65% | 0,56 | €-12,20 | 9,08% |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | Scanner Top 5 + forza BTC | €9.215,49 | €-786,94 | 76 | 76 | 35,53% | 0,67 | €-10,35 | 10,16% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.198,97 | €-788,48 | 126 | 126 | 38,10% | 0,69 | €-6,26 | 12,31% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.170,95 | €-827,60 | 89 | 89 | 31,46% | 0,64 | €-9,30 | 10,17% |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | Momentum / breakout | €9.165,52 | €-834,48 | 95 | 95 | 41,05% | 0,72 | €-8,78 | 12,64% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €9.150,69 | €-849,31 | 121 | 121 | 36,36% | 0,69 | €-7,02 | 13,99% |
| TEST | 1H Fast V3 Cap75 V1 | Momentum / breakout V3 Filtered | €9.106,22 | €-893,78 | 136 | 136 | 36,03% | 0,75 | €-6,57 | 14,10% |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | Scanner Top 5 + forza BTC | €9.052,49 | €-947,51 | 92 | 92 | 35,87% | 0,64 | €-10,30 | 9,48% |
| TEST | Combo Adaptive Runner25 V1 | Combo Adaptive | €8.964,11 | €-1.035,89 | 94 | 94 | 30,85% | 0,53 | €-11,02 | 12,67% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €8.918,97 | €-1.081,03 | 48 | 48 | 35,42% | 0,46 | €-22,52 | 12,56% |
| TEST | Scanner Top5 Btc Btc Le3 V1 | Scanner Top 5 + forza BTC | €8.883,87 | €-1.115,11 | 79 | 79 | 31,65% | 0,52 | €-14,12 | 13,85% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €8.862,92 | €-1.143,10 | 60 | 60 | 26,67% | 0,56 | €-19,05 | 11,95% |
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
| Principale 4H | TRUMP | LONG | Confluenza trend | 240m | 3,0x | 2,46049 | 2,80100 | 2,16523 | 1,65263 | 3,05101 | €134,98 | €404,95 | €48,59 | €56,04 |
| Principale 4H | XRP | LONG | Confluenza trend | 240m | 3,0x | 1,46057 | 1,42154 | 1,30460 | 0,98102 | 1,77252 | €8,58 | €25,73 | €2,75 | €-0,69 |
| Principale 4H | HYPE | LONG | Confluenza trend | 240m | 3,0x | 78,87277 | 83,35500 | 81,67793 | 52,97621 | 90,53117 | €8,52 | €25,56 | €0,00 | €1,45 |
| 1H Balanced Long No Rhv V1 | SKHYNIX | LONG | Confluenza trend | 60m | 3,0x | 1214,11277 | 1214,11277 | 1170,18211 | 815,47908 | 1301,97411 | €413,43 | €1.240,28 | €44,88 | €0,00 |
| 1H Balanced Long No Rhv V1 | BOME | LONG | Confluenza trend | 60m | 3,0x | 0,00129 | 0,00129 | 0,00114 | 0,00087 | 0,00160 | €134,98 | €404,95 | €48,59 | €0,00 |
| 1H Balanced Long No Rhv V1 | TAO | LONG | Confluenza trend | 60m | 3,0x | 247,38947 | 246,10000 | 237,94346 | 166,16326 | 266,28148 | €428,20 | €1.284,61 | €49,05 | €-6,70 |
| 1H Balanced Long No Rhv V1 | SOL | LONG | Confluenza trend | 60m | 3,0x | 108,77575 | 107,14300 | 105,75101 | 73,06105 | 114,82524 | €28,18 | €84,53 | €2,35 | €-1,27 |
| 1H Balanced Long No Rhv V1 | TRUMP | LONG | Confluenza trend | 60m | 3,0x | 2,74355 | 2,80100 | 2,55460 | 1,84275 | 3,12145 | €234,56 | €703,68 | €48,46 | €14,74 |
| Bilanciata 1H V2 | SKHYNIX | LONG | Confluenza trend V2 | 60m | 3,0x | 1214,11277 | 1214,11277 | 1170,18211 | 815,47908 | 1301,97411 | €422,38 | €1.267,15 | €45,85 | €0,00 |
| Bilanciata 1H V2 | BTR | LONG | Confluenza trend V2 | 60m | 3,0x | 0,16110 | 0,16110 | 0,14177 | 0,10821 | 0,19977 | €131,74 | €395,21 | €47,43 | €0,00 |
| Bilanciata 1H V2 | TRUMP | LONG | Confluenza trend V2 | 60m | 3,0x | 2,74355 | 2,80100 | 2,55460 | 1,84275 | 3,12145 | €228,59 | €685,78 | €47,23 | €14,36 |
| Bilanciata 1H V3 Filtered | SKHYNIX | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1220,85412 | 1220,85412 | 1177,63561 | 820,00702 | 1307,29117 | €460,42 | €1.381,27 | €48,90 | €0,00 |
| Bilanciata 1H V3 Filtered | HYPE | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 84,90998 | 83,35500 | 82,34469 | 57,03120 | 90,04056 | €548,05 | €1.644,14 | €49,67 | €-30,11 |
| Bilanciata 1H V3 Filtered | XRP | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1,44929 | 1,42154 | 1,41511 | 0,97344 | 1,51766 | €23,14 | €69,42 | €1,64 | €-1,33 |
| 1H Fast Score 6 75 Cost Aware V1 | BTW | LONG | Momentum / breakout | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €8,91 | €26,72 | €3,13 | €0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00086 | 0,00146 | €215,92 | €647,76 | €57,03 | €0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | NEAR | LONG | Momentum / breakout | 60m | 3,0x | 2,08142 | 2,08142 | 2,02315 | 1,39802 | 2,16882 | €42,86 | €128,59 | €3,60 | €0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €157,13 | €471,39 | €56,57 | €-0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | BTR | LONG | Momentum / breakout | 60m | 3,0x | 0,16110 | 0,16110 | 0,14177 | 0,10821 | 0,19010 | €139,02 | €417,05 | €50,05 | €0,00 |
| 1H Fast Nohigh Cap75 V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €139,29 | €417,86 | €50,14 | €-0,00 |
| 1H Fast Nohigh Cap75 V1 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €141,57 | €424,71 | €50,14 | €-0,00 |
| 1H Fast Nohigh Cap75 V1 | BTR | LONG | Momentum / breakout | 60m | 3,0x | 0,16110 | 0,16110 | 0,14177 | 0,10821 | 0,19010 | €132,75 | €398,25 | €47,79 | €0,00 |
| 1H Fast No Pepe V1 | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €172,22 | €516,67 | €49,86 | €0,00 |
| 1H Fast No Pepe V1 | TAO | LONG | Momentum / breakout | 60m | 3,0x | 247,38947 | 246,10000 | 240,04257 | 166,16326 | 258,40981 | €47,93 | €143,78 | €4,27 | €-0,75 |
| 1H Fast No Pepe V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €136,27 | €408,80 | €49,06 | €-0,00 |
| 1H Fast No Pepe V1 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €9,48 | €28,43 | €3,41 | €-0,00 |
| 1H Fast No Pepe V1 | BTR | LONG | Momentum / breakout | 60m | 3,0x | 0,16110 | 0,16110 | 0,14177 | 0,10821 | 0,19010 | €145,28 | €435,84 | €52,30 | €0,00 |
| 1H Fast No Pepe V1 | TRUMP | LONG | Momentum / breakout | 60m | 3,0x | 2,74355 | 2,80100 | 2,59659 | 1,84275 | 2,96399 | €332,30 | €996,90 | €53,40 | €20,88 |
| 1H Fast Tp2 V1 | BTW | LONG | Momentum / breakout | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,56752 | €142,85 | €428,56 | €50,25 | €0,00 |
| 1H Fast Tp2 V1 | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00132 | 0,00132 | 0,00119 | 0,00088 | 0,00158 | €18,87 | €56,62 | €5,59 | €0,00 |
| 1H Fast Tp2 V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,17246 | 0,17246 | 0,17246 | 0,22908 | 0,13107 | €139,71 | €419,14 | €0,00 | €-0,00 |
| 1H Fast Tp2 V1 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03379 | €141,13 | €423,40 | €50,81 | €-0,00 |
| 1H Fast Tp2 V1 | TRUMP | LONG | Momentum / breakout | 60m | 3,0x | 2,74355 | 2,80100 | 2,59659 | 1,84275 | 3,03747 | €314,71 | €944,14 | €50,57 | €19,77 |
| Rapida 1H V3 Filtered | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €172,00 | €515,99 | €49,79 | €0,00 |
| Rapida 1H V3 Filtered | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 246,10000 | 240,04257 | 166,16326 | 258,40981 | €589,98 | €1.769,95 | €52,56 | €-9,23 |
| Rapida 1H V3 Filtered | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €140,02 | €420,06 | €50,41 | €-0,00 |
| Rapida 1H V3 Filtered | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €16,99 | €50,96 | €6,11 | €-0,00 |
| Rapida 1H V3 Filtered | BTR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16110 | 0,16110 | 0,14177 | 0,10821 | 0,19010 | €8,42 | €25,27 | €3,03 | €0,00 |
| Rapida 1H V3 Filtered | TRUMP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,74355 | 2,80100 | 2,59659 | 1,84275 | 2,96399 | €308,01 | €924,04 | €49,50 | €19,35 |
| 1H Fast V3 Nohigh V1 | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €131,05 | €393,14 | €47,18 | €-0,00 |
| 1H Fast V3 Nohigh V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €133,20 | €399,59 | €47,18 | €-0,00 |
| 1H Fast V3 Nohigh V1 | BTR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16110 | 0,16110 | 0,14177 | 0,10821 | 0,19010 | €9,29 | €27,86 | €3,34 | €0,00 |
| 1H Fast V3 Nohigh V1 | TRUMP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,74355 | 2,80100 | 2,59659 | 1,84275 | 2,96399 | €307,61 | €922,83 | €49,43 | €19,32 |
| 1H Fast V3 Long Only V1 | BTW | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €126,57 | €379,72 | €44,52 | €0,00 |
| 1H Fast V3 Long Only V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00147 | €9,56 | €28,69 | €2,66 | €0,00 |
| 1H Fast V3 Long Only V1 | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 246,10000 | 240,04257 | 166,16326 | 258,40981 | €554,42 | €1.663,26 | €49,39 | €-8,67 |
| 1H Fast V3 Long Only V1 | BTR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16110 | 0,16110 | 0,14177 | 0,10821 | 0,19010 | €135,44 | €406,31 | €48,76 | €0,00 |
| 1H Fast V3 Long Only V1 | TRUMP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,74355 | 2,80100 | 2,59659 | 1,84275 | 2,96399 | €304,28 | €912,85 | €48,90 | €19,12 |
| 1H Fast V3 Long Nohigh Cap75 V1 | BTR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16110 | 0,16110 | 0,14177 | 0,10821 | 0,19010 | €134,26 | €402,77 | €48,33 | €0,00 |
| 1H Fast V3 No Esports V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €169,36 | €508,09 | €49,03 | €0,00 |
| 1H Fast V3 No Esports V1 | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 246,10000 | 240,04257 | 166,16326 | 258,40981 | €27,04 | €81,13 | €2,41 | €-0,42 |
| 1H Fast V3 No Esports V1 | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €133,96 | €401,88 | €48,23 | €-0,00 |
| 1H Fast V3 No Esports V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €129,73 | €389,20 | €46,70 | €-0,00 |
| 1H Fast V3 No Esports V1 | TRUMP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,74355 | 2,80100 | 2,59659 | 1,84275 | 2,96399 | €305,32 | €915,96 | €49,06 | €19,18 |
| 1H Fast V3 No Esports Long Only V1 | BTW | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €132,94 | €398,81 | €46,76 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00147 | €10,06 | €30,18 | €2,80 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | BTR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16110 | 0,16110 | 0,14177 | 0,10821 | 0,19010 | €139,69 | €419,06 | €50,29 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | TRUMP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,74355 | 2,80100 | 2,59659 | 1,84275 | 2,96399 | €314,81 | €944,43 | €50,59 | €19,78 |
| 1H Fast V3 No Esports Mfe Lock V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €173,11 | €519,32 | €50,11 | €0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 246,10000 | 240,04257 | 166,16326 | 258,40981 | €593,79 | €1.781,38 | €52,90 | €-9,29 |
| 1H Fast V3 No Esports Mfe Lock V1 | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14742 | 0,14742 | 0,16511 | 0,19582 | 0,12088 | €140,93 | €422,78 | €50,73 | €-0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04446 | 0,04446 | 0,04980 | 0,05906 | 0,03646 | €17,09 | €51,28 | €6,15 | €-0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | BTR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16110 | 0,16110 | 0,14177 | 0,10821 | 0,19010 | €8,48 | €25,43 | €3,05 | €0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | TRUMP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,74355 | 2,80100 | 2,59659 | 1,84275 | 2,96399 | €310,01 | €930,02 | €49,82 | €19,48 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | BTR | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,15804 | 0,15804 | 0,13908 | 0,10615 | 0,18649 | €130,02 | €390,07 | €46,81 | €0,00 |
| Ampia 4H | SPCX | LONG | Confluenza trend | 240m | 2,0x | 136,56189 | 136,56189 | 126,46637 | 68,96375 | 164,82935 | €323,86 | €647,73 | €47,88 | €0,00 |
| Ampia 4H | VELVET | LONG | Confluenza trend | 240m | 2,0x | 0,55987 | 0,55987 | 0,49269 | 0,28274 | 0,74799 | €201,63 | €403,26 | €48,39 | €0,00 |
| Ampia 4H | LINK | LONG | Confluenza trend | 240m | 2,0x | 11,96839 | 11,96839 | 11,08055 | 6,04404 | 14,45436 | €14,07 | €28,15 | €2,09 | €0,00 |
| Ampia 4H | ETH | LONG | Confluenza trend | 240m | 2,0x | 2430,03591 | 2498,26000 | 2267,54364 | 1227,16813 | 2885,01426 | €18,82 | €37,65 | €2,52 | €1,06 |
| Ampia 4H | HYPE | LONG | Confluenza trend | 240m | 2,0x | 79,31286 | 83,35500 | 70,73982 | 40,05299 | 103,31737 | €13,82 | €27,64 | €2,99 | €1,41 |
| Ampia 4H | TRUMP | LONG | Confluenza trend | 240m | 2,0x | 2,37347 | 2,80100 | 2,08866 | 1,19860 | 3,17096 | €210,83 | €421,66 | €50,60 | €75,95 |
| Ampia 4H | DOGE | SHORT | Confluenza trend | 240m | 2,0x | 0,08583 | 0,08789 | 0,09382 | 0,12832 | 0,06346 | €274,53 | €549,07 | €51,10 | €-13,16 |
| Forza relativa 1H V2 | BEAT | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,25984 | 0,25984 | 0,25657 | 0,38847 | 0,19125 | €200,38 | €400,75 | €0,00 | €-0,00 |
| Forza relativa 1H V2 | TUT | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,04452 | 0,04452 | 0,04986 | 0,06656 | 0,03277 | €204,64 | €409,28 | €49,11 | €-0,00 |
| Forza relativa 1H V2 | BTR | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,15974 | 0,15974 | 0,14057 | 0,08067 | 0,20191 | €200,93 | €401,87 | €48,22 | €0,00 |
| Forza relativa 1H V2 | TRUMP | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 2,74355 | 2,80100 | 2,55460 | 1,38549 | 3,15924 | €355,39 | €710,77 | €48,95 | €14,88 |
| Benchmark Donchian breakout 1H | SKHYNIX | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1174,33482 | 1174,33482 | 1128,44989 | 593,03908 | 1289,04713 | €641,25 | €1.282,50 | €50,11 | €0,00 |
| Benchmark Donchian breakout 1H | VELVET | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,14787 | 0,14787 | 0,16561 | 0,22107 | 0,10351 | €237,23 | €474,47 | €56,94 | €-0,00 |
| Benchmark Donchian breakout 1H | XRP | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1,45759 | 1,42154 | 1,41723 | 0,73608 | 1,55848 | €42,73 | €85,47 | €2,37 | €-2,11 |
| Donchian 1H Gb20 120R V1 | SKHYNIX | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1174,33482 | 1174,33482 | 1128,44989 | 593,03908 | 1289,04713 | €626,15 | €1.252,30 | €48,93 | €0,00 |
| Donchian 1H Gb20 120R V1 | VELVET | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,14787 | 0,14787 | 0,16561 | 0,22107 | 0,10351 | €231,65 | €463,30 | €55,60 | €-0,00 |
| Donchian 1H Gb20 120R V1 | XRP | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1,45759 | 1,42154 | 1,41723 | 0,73608 | 1,55848 | €41,73 | €83,46 | €2,31 | €-2,06 |
| Benchmark trend following EMA 1H | BEAT | SHORT | Trend following EMA | 60m | 2,0x | 0,28257 | 0,28257 | 0,25706 | 0,42244 | 0,20797 | €186,11 | €372,23 | €0,00 | €-0,00 |
| Benchmark trend following EMA 1H | ZEC | LONG | Trend following EMA | 60m | 2,0x | 807,93155 | 790,17000 | 730,11531 | 408,00543 | 979,12728 | €17,42 | €34,84 | €3,36 | €-0,77 |
| Benchmark trend following EMA 1H | TUT | SHORT | Trend following EMA | 60m | 2,0x | 0,04446 | 0,04446 | 0,04980 | 0,06647 | 0,03272 | €194,70 | €389,39 | €46,73 | €-0,00 |
| Benchmark trend following EMA 1H | VELVET | SHORT | Trend following EMA | 60m | 2,0x | 0,14786 | 0,14786 | 0,16560 | 0,22105 | 0,10883 | €187,91 | €375,83 | €45,10 | €-0,00 |
| Benchmark trend following EMA 1H | SOL | LONG | Trend following EMA | 60m | 2,0x | 107,93058 | 107,14300 | 104,51281 | 54,50494 | 115,44967 | €700,71 | €1.401,42 | €44,38 | €-10,23 |
| Scanner Top 5 Long 1H | BOME | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00160 | €218,24 | €436,47 | €52,38 | €0,00 |
| Scanner Top 5 Long 1H | TRUMP | LONG | Scanner Top 5 Long | 60m | 2,0x | 2,50550 | 2,80100 | 2,21642 | 1,26528 | 3,08367 | €238,89 | €477,78 | €55,13 | €56,35 |
| Scanner Top 5 Long 1H | SKHYNIX | LONG | Scanner Top 5 Long | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1331,36020 | €17,74 | €35,49 | €0,91 | €0,00 |
| Scanner Top 5 Long 1H | SOL | LONG | Scanner Top 5 Long | 60m | 2,0x | 108,77575 | 107,14300 | 105,75101 | 54,93175 | 114,82524 | €37,02 | €74,04 | €2,06 | €-1,11 |
| Scanner Bottom 5 Short 1H | SOXL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €378,86 | €757,72 | €48,07 | €-0,00 |
| Scanner Bottom 5 Short 1H | SNDK | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €492,80 | €985,60 | €47,71 | €-0,00 |
| Scanner Bottom 5 Short 1H | VELVET | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €191,07 | €382,14 | €0,00 | €-0,00 |
| Scanner Bottom 5 Short 1H | TUT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €178,38 | €356,76 | €42,81 | €-0,00 |
| Scanner Top10 Long | TAO | LONG | Scanner Top10 Long | 60m | 2,0x | 247,38947 | 246,10000 | 237,94346 | 124,93168 | 266,28148 | €678,43 | €1.356,86 | €51,81 | €-7,07 |
| Scanner Top10 Long | SKHYNIX | LONG | Scanner Top10 Long | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €972,86 | €1.945,72 | €48,38 | €0,00 |
| Scanner Top10 Long | BTR | LONG | Scanner Top10 Long | 60m | 2,0x | 0,16596 | 0,16596 | 0,14605 | 0,08381 | 0,20579 | €206,82 | €413,63 | €49,64 | €0,00 |
| Scanner Top10 Long | TRUMP | LONG | Scanner Top10 Long | 60m | 2,0x | 2,74355 | 2,80100 | 2,55460 | 1,38549 | 3,12145 | €369,58 | €739,16 | €50,91 | €15,48 |
| Scanner Bottom10 Short | SOXL | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom10 Short | SNDK | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Bottom10 Short | VELVET | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €194,19 | €388,38 | €0,00 | €-0,00 |
| Scanner Bottom10 Short | TUT | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €181,31 | €362,61 | €43,51 | €-0,00 |
| Scanner Top15 Long | NEAR | LONG | Scanner Top15 Long | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €16,79 | €33,59 | €1,21 | €0,00 |
| Scanner Top15 Long | TAO | LONG | Scanner Top15 Long | 60m | 2,0x | 247,38947 | 246,10000 | 237,94346 | 124,93168 | 266,28148 | €88,53 | €177,07 | €6,76 | €-0,92 |
| Scanner Top15 Long | TRUMP | LONG | Scanner Top15 Long | 60m | 2,0x | 2,50550 | 2,80100 | 2,21642 | 1,26528 | 3,08367 | €215,87 | €431,75 | €49,81 | €50,92 |
| Scanner Top15 Long | SKHYNIX | LONG | Scanner Top15 Long | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €787,36 | €1.574,72 | €39,16 | €0,00 |
| Scanner Top15 Long | BTR | LONG | Scanner Top15 Long | 60m | 2,0x | 0,16596 | 0,16596 | 0,14605 | 0,08381 | 0,20579 | €199,31 | €398,63 | €47,84 | €0,00 |
| Scanner Top15 Long | SOL | LONG | Scanner Top15 Long | 60m | 2,0x | 108,77575 | 107,14300 | 105,75101 | 54,93175 | 114,82524 | €14,08 | €28,16 | €0,78 | €-0,42 |
| Scanner Top15 Long | HYPE | LONG | Scanner Top15 Long | 60m | 2,0x | 84,84797 | 83,35500 | 82,41506 | 42,84822 | 89,71377 | €14,05 | €28,10 | €0,81 | €-0,49 |
| Scanner Bottom15 Short | SOXL | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom15 Short | SNDK | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Bottom15 Short | VELVET | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €194,19 | €388,38 | €0,00 | €-0,00 |
| Scanner Bottom15 Short | TUT | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €181,31 | €362,61 | €43,51 | €-0,00 |
| Scanner Top20 Long | NEAR | LONG | Scanner Top20 Long | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €16,79 | €33,59 | €1,21 | €0,00 |
| Scanner Top20 Long | TAO | LONG | Scanner Top20 Long | 60m | 2,0x | 247,38947 | 246,10000 | 237,94346 | 124,93168 | 266,28148 | €88,53 | €177,07 | €6,76 | €-0,92 |
| Scanner Top20 Long | TRUMP | LONG | Scanner Top20 Long | 60m | 2,0x | 2,50550 | 2,80100 | 2,21642 | 1,26528 | 3,08367 | €215,87 | €431,75 | €49,81 | €50,92 |
| Scanner Top20 Long | SKHYNIX | LONG | Scanner Top20 Long | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €787,36 | €1.574,72 | €39,16 | €0,00 |
| Scanner Top20 Long | BTR | LONG | Scanner Top20 Long | 60m | 2,0x | 0,16596 | 0,16596 | 0,14605 | 0,08381 | 0,20579 | €199,31 | €398,63 | €47,84 | €0,00 |
| Scanner Top20 Long | SOL | LONG | Scanner Top20 Long | 60m | 2,0x | 108,77575 | 107,14300 | 105,75101 | 54,93175 | 114,82524 | €14,08 | €28,16 | €0,78 | €-0,42 |
| Scanner Top20 Long | HYPE | LONG | Scanner Top20 Long | 60m | 2,0x | 84,84797 | 83,35500 | 82,41506 | 42,84822 | 89,71377 | €14,05 | €28,10 | €0,81 | €-0,49 |
| Scanner Bottom20 Short | SOXL | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom20 Short | SNDK | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Bottom20 Short | VELVET | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €194,19 | €388,38 | €0,00 | €-0,00 |
| Scanner Bottom20 Short | TUT | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €181,31 | €362,61 | €43,51 | €-0,00 |
| Scanner Top 5 + forza BTC 1H | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €203,45 | €406,91 | €48,83 | €0,00 |
| Scanner Top 5 + forza BTC 1H | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,50550 | 2,80100 | 2,21642 | 1,26528 | 3,14149 | €223,03 | €446,06 | €51,47 | €52,61 |
| Scanner Top 5 + forza BTC 1H | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €18,23 | €36,45 | €0,93 | €0,00 |
| Scanner Top 5 + forza BTC 1H | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 84,28485 | 83,35500 | 81,99407 | 42,56385 | 89,32457 | €30,02 | €60,05 | €1,63 | €-0,66 |
| Scanner Top5 Btc Mfe V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €190,73 | €381,46 | €45,77 | €0,00 |
| Scanner Top5 Btc Mfe V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,50550 | 2,80100 | 2,21642 | 1,26528 | 3,14149 | €209,08 | €418,16 | €48,25 | €49,32 |
| Scanner Top5 Btc Mfe V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €17,09 | €34,17 | €0,88 | €0,00 |
| Scanner Top5 Btc Mfe V1 | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 84,28485 | 83,35500 | 81,99407 | 42,56385 | 89,32457 | €28,15 | €56,29 | €1,53 | €-0,62 |
| Scanner Top5 Btc Guard V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €197,27 | €394,55 | €47,35 | €0,00 |
| Scanner Top5 Btc Guard V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,55551 | 2,80100 | 2,29388 | 1,29053 | 3,13109 | €13,03 | €26,06 | €2,67 | €2,50 |
| Scanner Top5 Btc Guard V1 | BTR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,16596 | 0,16596 | 0,14605 | 0,08381 | 0,20978 | €189,80 | €379,60 | €45,55 | €0,00 |
| Scanner Top5 Btc Guard V1 | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 84,83196 | 83,35500 | 82,43497 | 42,84014 | 90,10534 | €13,39 | €26,78 | €0,76 | €-0,47 |
| Scanner Top5 Btc Btc Le3 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €847,75 | €1.695,49 | €43,45 | €0,00 |
| Scanner Top5 Btc Btc 2 3 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €891,28 | €1.782,56 | €45,68 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €192,69 | €385,37 | €46,24 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,55551 | 2,80100 | 2,29388 | 1,29053 | 3,13109 | €12,72 | €25,45 | €2,61 | €2,44 |
| Scanner Top5 Btc Guard Mfe V1 | BTR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,16596 | 0,16596 | 0,14605 | 0,08381 | 0,20978 | €185,39 | €370,78 | €44,49 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 84,83196 | 83,35500 | 82,43497 | 42,84014 | 90,10534 | €13,08 | €26,16 | €0,74 | €-0,46 |
| Scanner Top5 Btc Guard Btc Le3 V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,55551 | 2,80100 | 2,29388 | 1,29053 | 3,13109 | €12,70 | €25,40 | €2,60 | €2,44 |
| Scanner Top5 Btc Runner25 V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00176 | €210,95 | €421,90 | €50,63 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1363,81560 | €965,52 | €1.931,04 | €49,49 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | BTR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,16596 | 0,16596 | 0,14605 | 0,08381 | 0,22571 | €210,82 | €421,64 | €50,60 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 84,28485 | 83,35500 | 81,99407 | 42,56385 | 91,15720 | €13,12 | €26,23 | €0,71 | €-0,29 |
| Scanner Top5 Btc Runner25 V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,74355 | 2,80100 | 2,55460 | 1,38549 | 3,31040 | €370,24 | €740,48 | €51,00 | €15,51 |
| Scanner Top5 Btc Tp3 V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00176 | €211,07 | €422,14 | €50,66 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | SKHYNIX | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1363,81560 | €966,09 | €1.932,17 | €49,52 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | BTR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,16596 | 0,16596 | 0,14605 | 0,08381 | 0,22571 | €210,94 | €421,89 | €50,63 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | HYPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 84,28485 | 83,35500 | 81,99407 | 42,56385 | 91,15720 | €13,12 | €26,25 | €0,71 | €-0,29 |
| Scanner Top5 Btc Tp3 V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,74355 | 2,80100 | 2,55460 | 1,38549 | 3,31040 | €370,46 | €740,92 | €51,03 | €15,52 |
| Combo Trend | BEAT | SHORT | Combo Trend | 60m | 2,0x | 0,25984 | 0,25984 | 0,25657 | 0,38847 | 0,19125 | €193,71 | €387,42 | €0,00 | €-0,00 |
| Combo Trend | ZEC | LONG | Combo Trend | 60m | 2,0x | 807,93155 | 790,17000 | 730,11531 | 408,00543 | 979,12728 | €247,61 | €495,23 | €47,70 | €-10,89 |
| Combo Trend | HYPE | LONG | Combo Trend | 60m | 2,0x | 84,28485 | 83,35500 | 81,73954 | 42,56385 | 89,88454 | €13,36 | €26,72 | €0,81 | €-0,29 |
| Combo Trend | SOL | LONG | Combo Trend | 60m | 2,0x | 108,89978 | 107,14300 | 105,49381 | 54,99439 | 116,39291 | €725,00 | €1.450,01 | €45,35 | €-23,39 |
| Combo Trend | TRUMP | LONG | Combo Trend | 60m | 2,0x | 2,74355 | 2,80100 | 2,53360 | 1,38549 | 3,20543 | €297,16 | €594,31 | €45,48 | €12,45 |
| Combo Scanner | BOME | LONG | Combo Scanner | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €195,20 | €390,40 | €46,85 | €0,00 |
| Combo Scanner | TRUMP | LONG | Combo Scanner | 60m | 2,0x | 2,50550 | 2,80100 | 2,21642 | 1,26528 | 3,14149 | €213,98 | €427,96 | €49,38 | €50,47 |
| Combo Scanner | SKHYNIX | LONG | Combo Scanner | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1337,85129 | €24,78 | €49,55 | €1,27 | €0,00 |
| Combo Scanner | HYPE | LONG | Combo Scanner | 60m | 2,0x | 84,28485 | 83,35500 | 81,99407 | 42,56385 | 89,32457 | €24,57 | €49,15 | €1,34 | €-0,54 |
| Combo Adaptive | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,01735 | 121,01735 | 128,90956 | 180,92093 | 105,23292 | €367,30 | €734,61 | €47,91 | €-0,00 |
| Combo Adaptive | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 246,10000 | 237,94346 | 124,93168 | 266,28148 | €40,89 | €81,77 | €3,12 | €-0,43 |
| Combo Adaptive | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 807,93155 | 790,17000 | 737,89694 | 408,00543 | 948,00078 | €307,94 | €615,88 | €53,39 | €-13,54 |
| Combo Adaptive | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,80100 | 2,33981 | 1,27487 | 2,89389 | €18,69 | €37,37 | €2,73 | €4,09 |
| Combo Adaptive | BTR | LONG | Combo Adaptive | 60m | 2,0x | 0,16596 | 0,16596 | 0,14605 | 0,08381 | 0,20579 | €222,35 | €444,69 | €53,36 | €0,00 |
| Combo Adaptive | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 85,03100 | 83,35500 | 82,51607 | 42,94066 | 90,06086 | €27,91 | €55,81 | €1,65 | €-1,10 |
| Combo Adaptive Mfe Trail | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 246,10000 | 237,94346 | 124,93168 | 266,28148 | €54,29 | €108,58 | €4,15 | €-0,57 |
| Combo Adaptive Mfe Trail | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,80100 | 2,33981 | 1,27487 | 2,89389 | €315,75 | €631,50 | €46,20 | €69,16 |
| Combo Adaptive Mfe Trail | TUT | SHORT | Combo Adaptive | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €190,04 | €380,09 | €45,61 | €-0,00 |
| Combo Adaptive Mfe Trail | BTR | LONG | Combo Adaptive | 60m | 2,0x | 0,16596 | 0,16596 | 0,14605 | 0,08381 | 0,20579 | €163,28 | €326,55 | €39,19 | €0,00 |
| Combo Adaptive Mfe Trail | HYPE | LONG | Combo Adaptive | 60m | 2,0x | 85,03100 | 83,35500 | 82,51607 | 42,94066 | 90,06086 | €14,98 | €29,97 | €0,89 | €-0,59 |
| Combo Adaptive Quality7 V1 | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €371,68 | €743,36 | €47,16 | €-0,00 |
| Combo Adaptive Quality7 V1 | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 246,10000 | 237,94346 | 124,93168 | 266,28148 | €646,78 | €1.293,57 | €49,39 | €-6,74 |
| Combo Adaptive Quality7 V1 | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,74355 | 2,80100 | 2,55460 | 1,38549 | 3,12145 | €351,63 | €703,25 | €48,43 | €14,73 |
| Combo Adaptive Regime V1 | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €987,06 | €1.974,12 | €49,09 | €0,00 |
| Combo Adaptive Regime V1 | BTR | LONG | Combo Adaptive | 60m | 2,0x | 0,16596 | 0,16596 | 0,14605 | 0,08381 | 0,20579 | €204,79 | €409,58 | €49,15 | €0,00 |
| Combo Adaptive Regime V1 | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,74355 | 2,80100 | 2,55460 | 1,38549 | 3,12145 | €357,90 | €715,80 | €49,30 | €14,99 |
| Combo Adaptive Quality7 Regime V1 | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,74355 | 2,80100 | 2,55460 | 1,38549 | 3,12145 | €356,56 | €713,12 | €49,11 | €14,93 |
| Combo Adaptive Long Only V1 | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €645,48 | €1.290,95 | €46,47 | €0,00 |
| Combo Adaptive Long Only V1 | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,80100 | 2,33981 | 1,27487 | 2,89389 | €48,12 | €96,24 | €7,04 | €10,54 |
| Combo Adaptive Long Only V1 | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99401 | 639,55695 | 1331,36020 | €968,99 | €1.937,97 | €49,66 | €0,00 |
| Combo Adaptive Long Only V1 | SOL | LONG | Combo Adaptive | 60m | 2,0x | 108,77575 | 107,14300 | 105,75101 | 54,93175 | 114,82524 | €31,02 | €62,04 | €1,73 | €-0,93 |
| Combo Adaptive Partial 1R V1 | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,01735 | 121,01735 | 128,90956 | 180,92093 | 105,23292 | €352,70 | €705,40 | €46,00 | €-0,00 |
| Combo Adaptive Partial 1R V1 | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,80100 | 2,33981 | 1,27487 | 2,89389 | €347,19 | €694,38 | €50,80 | €76,05 |
| Combo Adaptive Partial 1R V1 | VELVET | SHORT | Combo Adaptive | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €207,76 | €415,52 | €0,00 | €-0,00 |
| Combo Adaptive Partial 1R V1 | SKHYNIX | LONG | Combo Adaptive | 60m | 2,0x | 1270,86206 | 1270,86206 | 1239,26059 | 641,78534 | 1334,06500 | €1.013,20 | €2.026,40 | €50,39 | €0,00 |
| Combo Adaptive Quality7 Regime Partial 1R V1 | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,74355 | 2,80100 | 2,55460 | 1,38549 | 3,12145 | €361,10 | €722,20 | €49,74 | €15,12 |
| Btc Ema 1H | BTC | LONG | Trend following EMA | 60m | 3,0x | 80391,81515 | 79728,20000 | 79234,17301 | 53996,50251 | 82707,09942 | €1.138,16 | €3.414,47 | €49,17 | €-28,19 |
| Btc Ema 4H | BTC | LONG | Trend following EMA | 240m | 2,0x | 80355,23783 | 79728,20000 | 77497,66656 | 40579,39511 | 87499,16561 | €704,37 | €1.408,74 | €50,10 | €-10,99 |
| Btc Donchian 4H | BTC | LONG | Donchian breakout 20 barre | 240m | 2,0x | 80355,23783 | 79728,20000 | 77497,66656 | 40579,39511 | 88356,43707 | €700,60 | €1.401,20 | €49,83 | €-10,93 |
| Btc Bollinger 4H | BTC | SHORT | Bollinger mean reversion | 240m | 2,0x | 80323,10217 | 79728,20000 | 82919,85488 | 120083,03774 | 75648,94663 | €775,58 | €1.551,16 | €50,15 | €11,49 |
| Btc Adaptive 4H | BTC | LONG | Combo Adaptive | 240m | 2,0x | 80355,23783 | 79728,20000 | 77237,88772 | 40579,39511 | 88148,61352 | €648,94 | €1.297,88 | €50,35 | €-10,13 |
| Sol Ema 4H | SOL | LONG | Trend following EMA | 240m | 2,0x | 98,32066 | 107,14300 | 105,07574 | 49,65193 | 113,95442 | €395,27 | €790,53 | €0,00 | €70,93 |
| Sol Donchian 4H | SOL | LONG | Donchian breakout 20 barre | 240m | 2,0x | 104,08581 | 107,14300 | 98,18471 | 52,56334 | 120,60890 | €449,62 | €899,24 | €50,98 | €26,41 |
| Sol Bollinger 1H | SOL | SHORT | Bollinger mean reversion | 60m | 3,0x | 108,77924 | 107,14300 | 108,09773 | 144,49509 | 104,97024 | €697,47 | €2.092,40 | €0,00 | €31,47 |
| Sol Bollinger 4H | SOL | SHORT | Bollinger mean reversion | 240m | 2,0x | 107,28254 | 107,14300 | 112,84334 | 160,38740 | 97,27311 | €478,97 | €957,94 | €49,65 | €1,25 |
| Sol Adaptive 4H | SOL | LONG | Combo Adaptive | 240m | 2,0x | 98,32066 | 107,14300 | 105,07574 | 49,65193 | 115,37567 | €367,30 | €734,59 | €0,00 | €65,92 |
| Eth Ema 4H | ETH | LONG | Trend following EMA | 240m | 2,0x | 2390,02791 | 2498,26000 | 2464,86772 | 1206,96409 | 2693,57826 | €487,73 | €975,47 | €0,00 | €44,17 |
| Master Adaptive V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 2502,31036 | 2498,26000 | 2464,79465 | 1263,66673 | 2577,34181 | €1.560,29 | €3.120,58 | €46,79 | €-5,05 |
| Master Adaptive V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99403 | 639,55695 | 1331,36019 | €22,75 | €45,50 | €1,17 | €0,00 |
| Master Adaptive V1 | BTR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15804 | 0,15804 | 0,13908 | 0,07981 | 0,19597 | €191,23 | €382,45 | €45,89 | €0,00 |
| Master Adaptive V1 | SOL | LONG | Master Adaptive Consensus | 60m | 2,0x | 106,86837 | 107,14300 | 103,93146 | 53,96853 | 112,74219 | €863,53 | €1.727,06 | €47,46 | €4,44 |
| Master Adaptive V1 | ENA | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,16108 | 0,16525 | 0,14798 | 0,08135 | 0,18729 | €293,22 | €586,43 | €47,70 | €15,17 |
| Master Adaptive V1 | TRUMP | LONG | Master Adaptive Consensus | 60m | 2,0x | 2,74355 | 2,80100 | 2,55460 | 1,38549 | 3,12145 | €12,58 | €25,16 | €1,73 | €0,53 |
| Master Adaptive No Alt V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 2502,31036 | 2498,26000 | 2464,79465 | 1263,66673 | 2577,34181 | €1.565,03 | €3.130,05 | €46,93 | €-5,07 |
| Master Adaptive No Alt V1 | BTR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,14959 | 0,14959 | 0,13164 | 0,07554 | 0,18549 | €195,68 | €391,35 | €46,96 | €0,00 |
| Master Adaptive No Alt V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1255,10261 | 1255,10261 | 1225,12158 | 633,82682 | 1315,06467 | €19,09 | €38,19 | €0,91 | €0,00 |
| Master Adaptive No Alt V1 | TRUMP | LONG | Master Adaptive Consensus | 60m | 2,0x | 2,74355 | 2,80100 | 2,55460 | 1,38549 | 3,12145 | €343,00 | €686,01 | €47,25 | €14,37 |
| Master Adaptive No Alt V1 | SOL | LONG | Master Adaptive Consensus | 60m | 2,0x | 106,91738 | 107,14300 | 103,99458 | 53,99328 | 112,76299 | €858,29 | €1.716,58 | €46,93 | €3,62 |
| Master Adaptive Strict3 V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 2502,31036 | 2498,26000 | 2464,79465 | 1263,66673 | 2577,34181 | €1.493,28 | €2.986,56 | €44,78 | €-4,83 |
| Master Adaptive Strict3 V1 | BTR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,16596 | 0,16596 | 0,14605 | 0,08381 | 0,20579 | €184,95 | €369,91 | €44,39 | €0,00 |
| Master Adaptive Strict3 V1 | TRUMP | LONG | Master Adaptive Consensus | 60m | 2,0x | 2,74355 | 2,80100 | 2,55460 | 1,38549 | 3,12145 | €320,71 | €641,43 | €44,18 | €13,43 |
| Master Adaptive Expanded V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03814 | 0,02188 | 0,05374 | €197,50 | €395,01 | €47,40 | €0,00 |
| Master Adaptive Expanded V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 2502,31036 | 2498,26000 | 2464,79465 | 1263,66673 | 2577,34181 | €1.572,67 | €3.145,34 | €47,16 | €-5,09 |
| Master Adaptive Expanded V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1261,89668 | 1261,89668 | 1231,08309 | 637,25783 | 1323,52387 | €934,21 | €1.868,43 | €45,62 | €0,00 |
| Master Adaptive Expanded V1 | BTR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,16110 | 0,16110 | 0,14177 | 0,08136 | 0,19977 | €197,88 | €395,75 | €47,49 | €0,00 |
| Master Adaptive Expanded V1 | SOL | LONG | Master Adaptive Consensus | 60m | 2,0x | 107,32546 | 107,14300 | 104,39936 | 54,19936 | 113,17765 | €18,64 | €37,29 | €1,02 | €-0,06 |
| Master Adaptive Gb20 V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 2502,31036 | 2498,26000 | 2464,79465 | 1263,66673 | 2577,34181 | €1.539,56 | €3.079,12 | €46,16 | €-4,98 |
| Master Adaptive Gb20 V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99403 | 639,55695 | 1331,36019 | €22,45 | €44,90 | €1,15 | €0,00 |
| Master Adaptive Gb20 V1 | BTR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15804 | 0,15804 | 0,13908 | 0,07981 | 0,19597 | €188,69 | €377,37 | €45,28 | €0,00 |
| Master Adaptive Gb20 V1 | SOL | LONG | Master Adaptive Consensus | 60m | 2,0x | 106,86837 | 107,14300 | 103,93146 | 53,96853 | 112,74219 | €852,06 | €1.704,12 | €46,83 | €4,38 |
| Master Adaptive Gb20 V1 | ENA | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,16108 | 0,16525 | 0,14798 | 0,08135 | 0,18729 | €289,32 | €578,64 | €47,07 | €14,97 |
| Master Adaptive Gb20 V1 | TRUMP | LONG | Master Adaptive Consensus | 60m | 2,0x | 2,78156 | 2,80100 | 2,59415 | 1,40469 | 3,15637 | €17,24 | €34,47 | €2,32 | €0,24 |
| Master Adaptive Runner25 V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03814 | 0,02188 | 0,05894 | €34,77 | €69,54 | €8,34 | €0,00 |
| Master Adaptive Runner25 V1 | HYPE | LONG | Master Adaptive Consensus | 60m | 2,0x | 80,35907 | 83,35500 | 78,17754 | 40,58133 | 86,90364 | €864,19 | €1.728,38 | €46,92 | €64,44 |
| Master Adaptive Runner25 V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 2502,31036 | 2498,26000 | 2464,79465 | 1263,66673 | 2614,85753 | €1.568,97 | €3.137,94 | €47,05 | €-5,08 |
| Master Adaptive Runner25 V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1255,10261 | 1255,10261 | 1225,12158 | 633,82682 | 1345,04570 | €27,05 | €54,10 | €1,29 | €0,00 |
| Master Adaptive Runner25 V1 | SOL | LONG | Master Adaptive Consensus | 60m | 2,0x | 106,43928 | 107,14300 | 103,65189 | 53,75184 | 114,80148 | €920,14 | €1.840,29 | €48,19 | €12,17 |
| Master Adaptive Runner25 V1 | ENA | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,16574 | 0,16525 | 0,15522 | 0,08370 | 0,19732 | €14,90 | €29,81 | €1,89 | €-0,09 |
| Master Adaptive Runner25 V1 | BTR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15905 | 0,15905 | 0,13997 | 0,08032 | 0,21631 | €158,41 | €316,83 | €38,02 | €0,00 |
| Combo Adaptive Side Regime Guard V1 | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €77,52 | €155,04 | €5,58 | €0,00 |
| Combo Adaptive Side Regime Guard V1 | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 807,93155 | 790,17000 | 737,89694 | 408,00543 | 948,00078 | €305,89 | €611,78 | €53,03 | €-13,45 |
| Combo Adaptive Side Regime Guard V1 | VELVET | SHORT | Combo Adaptive | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,13107 | €216,61 | €433,23 | €0,00 | €-0,00 |
| Combo Adaptive Side Regime Guard V1 | TUT | SHORT | Combo Adaptive | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03473 | €192,40 | €384,79 | €46,18 | €-0,00 |
| Combo Adaptive Side Regime Guard V1 | BTR | LONG | Combo Adaptive | 60m | 2,0x | 0,16596 | 0,16596 | 0,14605 | 0,08381 | 0,20579 | €210,11 | €420,21 | €50,43 | €0,00 |
| Combo Adaptive Side Regime Guard V1 | TAO | LONG | Combo Adaptive | 60m | 2,0x | 251,13022 | 246,10000 | 242,26367 | 126,82076 | 268,86331 | €14,43 | €28,86 | €1,02 | €-0,58 |
| Master Adaptive Gb20 Be V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 2502,31036 | 2498,26000 | 2464,79465 | 1263,66673 | 2577,34181 | €1.568,02 | €3.136,03 | €47,02 | €-5,08 |
| Master Adaptive Gb20 Be V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99403 | 639,55695 | 1331,36019 | €22,86 | €45,73 | €1,17 | €0,00 |
| Master Adaptive Gb20 Be V1 | BTR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15804 | 0,15804 | 0,13908 | 0,07981 | 0,19597 | €192,17 | €384,35 | €46,12 | €0,00 |
| Master Adaptive Gb20 Be V1 | SOL | LONG | Master Adaptive Consensus | 60m | 2,0x | 106,86837 | 107,14300 | 103,93146 | 53,96853 | 112,74219 | €867,81 | €1.735,61 | €47,70 | €4,46 |
| Master Adaptive Gb20 Be V1 | ENA | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,16108 | 0,16525 | 0,14798 | 0,08135 | 0,18729 | €294,67 | €589,34 | €47,94 | €15,25 |
| Master Adaptive Gb20 Be V1 | TRUMP | LONG | Master Adaptive Consensus | 60m | 2,0x | 2,74355 | 2,80100 | 2,55460 | 1,38549 | 3,12145 | €12,64 | €25,28 | €1,74 | €0,53 |
| Master Adaptive Gb20 Partial V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 2502,31036 | 2498,26000 | 2464,79465 | 1263,66673 | 2577,34181 | €1.566,35 | €3.132,70 | €46,97 | €-5,07 |
| Master Adaptive Gb20 Partial V1 | SKHYNIX | LONG | Master Adaptive Consensus | 60m | 2,0x | 1266,44941 | 1266,44941 | 1233,99403 | 639,55695 | 1331,36019 | €22,84 | €45,68 | €1,17 | €0,00 |
| Master Adaptive Gb20 Partial V1 | BTR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15804 | 0,15804 | 0,13908 | 0,07981 | 0,19597 | €191,97 | €383,94 | €46,07 | €0,00 |
| Master Adaptive Gb20 Partial V1 | SOL | LONG | Master Adaptive Consensus | 60m | 2,0x | 106,86837 | 107,14300 | 103,93146 | 53,96853 | 112,74219 | €866,88 | €1.733,77 | €47,65 | €4,46 |
| Master Adaptive Gb20 Partial V1 | ENA | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,16108 | 0,16525 | 0,14798 | 0,08135 | 0,18729 | €294,36 | €588,71 | €47,89 | €15,23 |
| Master Adaptive Gb20 Partial V1 | TRUMP | LONG | Master Adaptive Consensus | 60m | 2,0x | 2,74355 | 2,80100 | 2,55460 | 1,38549 | 3,12145 | €12,63 | €25,26 | €1,74 | €0,53 |
| Master Adaptive Gb20 Loss Cap V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04334 | 0,03828 | 0,02188 | 0,05682 | €195,70 | €391,41 | €45,67 | €0,00 |
| Master Adaptive Gb20 Loss Cap V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 2502,31036 | 2498,26000 | 2474,17356 | 1263,66673 | 2577,34181 | €1.829,31 | €3.658,61 | €41,14 | €-5,92 |
| Master Adaptive Gb20 Loss Cap V1 | BTR | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15804 | 0,15804 | 0,13908 | 0,07981 | 0,20861 | €188,78 | €377,55 | €45,31 | €0,00 |
| Master Adaptive Gb20 Loss Cap V1 | SOL | LONG | Master Adaptive Consensus | 60m | 2,0x | 106,86837 | 107,14300 | 104,66569 | 53,96853 | 112,74219 | €1.136,69 | €2.273,37 | €46,86 | €5,84 |
| Master Adaptive Gb20 Loss Cap V1 | ENA | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,16108 | 0,16525 | 0,15126 | 0,08135 | 0,18729 | €63,69 | €127,37 | €7,77 | €3,30 |
| 1H Fast V3 Nohigh Regime Guard V1 | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €140,84 | €422,53 | €50,70 | €-0,00 |
| 1H Fast V3 Nohigh Regime Guard V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €143,15 | €429,46 | €50,70 | €-0,00 |
| 1H Fast V3 Nohigh Regime Guard V1 | TRUMP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,74355 | 2,80100 | 2,59659 | 1,84275 | 2,96399 | €325,19 | €975,57 | €52,26 | €20,43 |
| Main Side Regime Guard V1 | VELVET | LONG | Confluenza trend | 240m | 3,0x | 0,55987 | 0,55987 | 0,49269 | 0,37605 | 0,69424 | €142,25 | €426,74 | €51,21 | €0,00 |
| Main Side Regime Guard V1 | AKE | LONG | Confluenza trend | 240m | 3,0x | 0,01021 | 0,01021 | 0,00899 | 0,00686 | 0,01266 | €145,97 | €437,90 | €52,55 | €0,00 |
| Main Side Regime Guard V1 | HYPE | LONG | Confluenza trend | 240m | 3,0x | 77,65853 | 83,35500 | 81,08374 | 52,16065 | 90,56048 | €216,52 | €649,56 | €0,00 | €47,65 |
| Main Side Regime Guard V1 | XRP | LONG | Confluenza trend | 240m | 3,0x | 1,47102 | 1,42154 | 1,31178 | 0,98804 | 1,78951 | €12,77 | €38,31 | €4,15 | €-1,29 |
| Main Side Regime Guard V1 | ETH | LONG | Confluenza trend | 240m | 3,0x | 2437,91749 | 2498,26000 | 2326,72117 | 1637,46791 | 2660,31012 | €9,94 | €29,83 | €1,36 | €0,74 |
| Main Side Regime Guard V1 | ENA | LONG | Confluenza trend | 240m | 3,0x | 0,16108 | 0,16525 | 0,14175 | 0,10819 | 0,19974 | €150,44 | €451,33 | €54,16 | €11,68 |
| Main Dynamic Asset Selector V1 | HYPE | LONG | Confluenza trend | 240m | 3,0x | 84,46489 | 83,35500 | 79,49888 | 56,73225 | 94,39691 | €288,05 | €864,16 | €50,81 | €-11,36 |
| Main Dynamic Asset Selector V1 | ENA | LONG | Confluenza trend | 240m | 3,0x | 0,16108 | 0,16525 | 0,14175 | 0,10819 | 0,19974 | €140,98 | €422,93 | €50,75 | €10,94 |
| Combo Trend Side Regime Guard V1 | VELVET | SHORT | Combo Trend | 60m | 2,0x | 0,17246 | 0,17246 | 0,17246 | 0,25782 | 0,12693 | €217,86 | €435,73 | €0,00 | €-0,00 |
| Combo Trend Side Regime Guard V1 | TUT | SHORT | Combo Trend | 60m | 2,0x | 0,04570 | 0,04570 | 0,05118 | 0,06832 | 0,03364 | €12,81 | €25,62 | €3,07 | €-0,00 |
| Combo Trend Side Regime Guard V1 | BTR | LONG | Combo Trend | 60m | 2,0x | 0,16596 | 0,16596 | 0,14605 | 0,08381 | 0,20978 | €231,16 | €462,32 | €55,48 | €0,00 |
| Combo Trend Side Regime Guard V1 | HYPE | LONG | Combo Trend | 60m | 2,0x | 84,28485 | 83,35500 | 81,73954 | 42,56385 | 89,88454 | €32,97 | €65,95 | €1,99 | €-0,73 |
| Combo Trend Side Regime Guard V1 | TRUMP | LONG | Combo Trend | 60m | 2,0x | 2,74355 | 2,80100 | 2,53360 | 1,38549 | 3,20543 | €363,18 | €726,37 | €55,58 | €15,21 |
| 1H Fast Nohigh Cap75 Short Only V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14786 | 0,14786 | 0,16560 | 0,19641 | 0,12125 | €135,82 | €407,46 | €48,90 | €-0,00 |
| 1H Fast Nohigh Cap75 Short Only V1 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04589 | 0,04589 | 0,05131 | 0,06096 | 0,03776 | €138,05 | €414,14 | €48,89 | €-0,00 |
| 1H Fast Nohigh Cap75 Short Only V1 | BTR | LONG | Momentum / breakout | 60m | 3,0x | 0,16110 | 0,16110 | 0,14177 | 0,10821 | 0,19010 | €129,45 | €388,34 | €46,60 | €0,00 |
| 1H Balanced V3 Long Only V1 | SKHYNIX | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1220,85412 | 1220,85412 | 1177,63561 | 820,00702 | 1307,29117 | €435,49 | €1.306,46 | €46,25 | €0,00 |
| 1H Balanced V3 Long Only V1 | HYPE | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 84,90998 | 83,35500 | 82,34469 | 57,03120 | 90,04056 | €518,27 | €1.554,82 | €46,97 | €-28,47 |
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
| Scanner Top20 Long | ETH | LONG | 2026-08-28T04:15:00+00:00 | 2476,94587 | €-0,58 | -1,09 | STOP |
| Scanner Top15 Long | ETH | LONG | 2026-08-28T04:15:00+00:00 | 2476,94587 | €-0,58 | -1,09 | STOP |
| Master Adaptive Strict3 V1 | ENA | LONG | 2026-08-28T04:15:00+00:00 | 0,16043 | €-45,79 | -1,02 | STOP |
| Master Adaptive No Alt V1 | ENA | LONG | 2026-08-28T04:15:00+00:00 | 0,16043 | €-49,30 | -1,02 | STOP |
| Eth Ema 1H | ETH | LONG | 2026-08-28T04:15:00+00:00 | 2476,94587 | €-53,50 | -1,09 | STOP |
| Donchian 1H Gb20 120R V1 | HYPE | LONG | 2026-08-28T04:15:00+00:00 | 82,96658 | €-4,61 | -1,04 | STOP |
| Benchmark Donchian breakout 1H | HYPE | LONG | 2026-08-28T04:15:00+00:00 | 82,96658 | €-4,72 | -1,04 | STOP |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | HYPE | LONG | 2026-08-28T04:15:00+00:00 | 82,95105 | €-50,91 | -1,07 | STOP |
| 1H Fast Tp2 V1 | TAO | LONG | 2026-08-28T04:15:00+00:00 | 243,33545 | €-1,55 | -1,05 | STOP |
| 1H Balanced Long No Rhv V1 | XRP | LONG | 2026-08-28T04:15:00+00:00 | 1,42099 | €-1,01 | -1,06 | STOP |
| Sol Ema 1H | SOL | LONG | 2026-08-28T03:15:00+00:00 | 105,81324 | €-53,66 | -1,05 | STOP |
| Sol Adaptive 1H | SOL | LONG | 2026-08-28T03:15:00+00:00 | 105,81324 | €-52,90 | -1,05 | STOP |

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

Generato: 2026-08-28 08:02 UTC


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

Segnali totali salvati: **147**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08-28 | BTC | 79.717,91 | +7 | +3 | +3 | 0 | +3 | +1 | 0 | ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA |
| 2026-08-28 | DOGE | 0.08759 | 0 | -1 | -1 | 0 | +1 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-08-28 | SOL | 106,61 | +8 | +3 | +3 | 0 | +3 | +1 | 0 | HOLD / ACCUMULO A TRANCHE, NO LEVA AGGRESSIVA |
| 2026-08-27 | BTC | 78.624,75 | +7 | +3 | +3 | 0 | +3 | +1 | 0 | ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA |
| 2026-08-27 | DOGE | 0.08623 | -1 | -1 | -1 | 0 | +1 | 0 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-08-27 | SOL | 100,81 | +7 | +2 | +2 | 0 | +3 | +1 | 0 | HOLD / ACCUMULO A TRANCHE, NO LEVA AGGRESSIVA |
| 2026-08-26 | BTC | 79.104,96 | +8 | +3 | +3 | 0 | +3 | +1 | 0 | ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA |
| 2026-08-26 | DOGE | 0.08675 | +1 | 0 | 0 | 0 | +2 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-08-26 | SOL | 96,96 | +6 | +1 | +1 | 0 | +3 | +1 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-08-25 | BTC | 80.778,18 | +6 | +2 | +2 | 0 | +3 | +1 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-08-25 | DOGE | 0.09299 | +5 | +1 | +1 | 0 | +3 | +1 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-08-25 | SOL | 102,40 | +6 | +1 | +1 | 0 | +3 | +1 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 49 | 48 | 47 | 46 | 44 | 42 | 39 | 35 | 30 | 21 | 6 | 0 |
| SOL | 49 | 48 | 47 | 46 | 44 | 42 | 39 | 35 | 30 | 21 | 6 | 0 |
| DOGE | 49 | 48 | 47 | 46 | 44 | 42 | 39 | 35 | 30 | 21 | 6 | 0 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-07-15 | 45g | 2026-08-29 | domani |
| SOL | 2026-07-15 | 45g | 2026-08-29 | domani |
| DOGE | 2026-07-15 | 45g | 2026-08-29 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 45 | 53,33% | +0,54% | +0,51% | PRIMA CALIBRAZIONE |
| BTC | 2g | 44 | 54,55% | +0,93% | +0,82% | PRIMA CALIBRAZIONE |
| BTC | 3g | 43 | 51,16% | +1,20% | +1,03% | PRIMA CALIBRAZIONE |
| BTC | 5g | 41 | 43,90% | +2,40% | +2,09% | PRIMA CALIBRAZIONE |
| BTC | 7g | 39 | 51,28% | +3,23% | +2,95% | PRIMA CALIBRAZIONE |
| BTC | 10g | 36 | 50,00% | +3,62% | +3,37% | PRIMA CALIBRAZIONE |
| BTC | 14g | 33 | 57,58% | +4,04% | +3,93% | PRIMA CALIBRAZIONE |
| BTC | 21g | 28 | 50,00% | +6,28% | +6,04% | FEEDBACK RAPIDO |
| BTC | 30g | 19 | 84,21% | +8,15% | +5,88% | FEEDBACK RAPIDO |
| BTC | 45g | 6 | 100,00% | +23,99% | +23,99% | FEEDBACK RAPIDO |
| BTC | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 1g | 41 | 58,54% | +0,89% | +0,74% | PRIMA CALIBRAZIONE |
| SOL | 2g | 40 | 55,00% | +1,67% | +1,50% | PRIMA CALIBRAZIONE |
| SOL | 3g | 39 | 58,97% | +2,49% | +2,26% | PRIMA CALIBRAZIONE |
| SOL | 5g | 37 | 62,16% | +4,08% | +3,94% | PRIMA CALIBRAZIONE |
| SOL | 7g | 35 | 65,71% | +5,39% | +5,54% | PRIMA CALIBRAZIONE |
| SOL | 10g | 32 | 65,62% | +6,02% | +6,26% | PRIMA CALIBRAZIONE |
| SOL | 14g | 28 | 71,43% | +5,80% | +7,10% | FEEDBACK RAPIDO |
| SOL | 21g | 23 | 65,22% | +8,57% | +7,02% | FEEDBACK RAPIDO |
| SOL | 30g | 15 | 46,67% | +4,92% | +2,85% | FEEDBACK RAPIDO |
| SOL | 45g | 5 | 40,00% | +30,39% | -10,04% | FEEDBACK RAPIDO |
| SOL | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 1g | 46 | 47,83% | +0,50% | +0,42% | PRIMA CALIBRAZIONE |
| DOGE | 2g | 45 | 51,11% | +0,98% | +0,97% | PRIMA CALIBRAZIONE |
| DOGE | 3g | 44 | 47,73% | +1,43% | +1,68% | PRIMA CALIBRAZIONE |
| DOGE | 5g | 42 | 57,14% | +2,82% | +3,42% | PRIMA CALIBRAZIONE |
| DOGE | 7g | 40 | 67,50% | +4,02% | +5,12% | PRIMA CALIBRAZIONE |
| DOGE | 10g | 37 | 62,16% | +3,36% | +5,04% | PRIMA CALIBRAZIONE |
| DOGE | 14g | 33 | 66,67% | +3,68% | +6,50% | PRIMA CALIBRAZIONE |
| DOGE | 21g | 28 | 71,43% | +4,71% | +3,30% | FEEDBACK RAPIDO |
| DOGE | 30g | 20 | 75,00% | +6,44% | +0,95% | FEEDBACK RAPIDO |
| DOGE | 45g | 6 | 0,00% | +22,35% | -22,35% | FEEDBACK RAPIDO |
| DOGE | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 45 | 53,33% | +0,54% | +0,51% | +0,09% | +1,14% | PRIMA CALIBRAZIONE |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 48 | 56,25% | +0,50% | +0,50% | +0,07% | +1,09% | PRIMA CALIBRAZIONE |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 48 | 56,25% | +0,50% | +0,50% | +0,07% | +1,09% | PRIMA CALIBRAZIONE |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,25% | +0,25% | -0,10% | +0,70% | PRIMA CALIBRAZIONE |
| BTC | 1g | Tecnico | CALIBRABILE | 43 | 39,53% | +0,67% | +0,19% | +0,21% | +1,26% | PRIMA CALIBRAZIONE |
| BTC | 1g | Classic technical | CALIBRABILE | 16 | 37,50% | +1,21% | +0,55% | +0,46% | +1,86% | FEEDBACK RAPIDO |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +0,27% | +0,27% | -0,26% | +0,74% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 44 | 54,55% | +0,93% | +0,82% | +0,34% | +1,67% | PRIMA CALIBRAZIONE |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 47 | 57,45% | +1,03% | +1,03% | +0,45% | +1,76% | PRIMA CALIBRAZIONE |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 47 | 57,45% | +1,03% | +1,03% | +0,45% | +1,76% | PRIMA CALIBRAZIONE |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,52% | +0,52% | -0,02% | +1,18% | PRIMA CALIBRAZIONE |
| BTC | 2g | Tecnico | CALIBRABILE | 42 | 45,24% | +1,28% | +0,29% | +0,69% | +2,01% | PRIMA CALIBRAZIONE |
| BTC | 2g | Classic technical | CALIBRABILE | 15 | 40,00% | +1,78% | +0,76% | +1,19% | +2,61% | FEEDBACK RAPIDO |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +2,14% | +2,14% | +1,22% | +2,65% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 43 | 51,16% | +1,20% | +1,03% | -0,82% | +2,89% | PRIMA CALIBRAZIONE |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 46 | 60,87% | +1,54% | +1,54% | -0,81% | +3,15% | PRIMA CALIBRAZIONE |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 46 | 60,87% | +1,54% | +1,54% | -0,81% | +3,15% | PRIMA CALIBRAZIONE |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 35 | 57,14% | +0,91% | +0,91% | -1,00% | +2,36% | PRIMA CALIBRAZIONE |
| BTC | 3g | Tecnico | CALIBRABILE | 41 | 39,02% | +1,97% | -0,08% | -0,57% | +3,53% | PRIMA CALIBRAZIONE |
| BTC | 3g | Classic technical | CALIBRABILE | 14 | 42,86% | +2,91% | +0,16% | +0,06% | +4,37% | FEEDBACK RAPIDO |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +1,42% | +1,42% | -0,64% | +3,18% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 41 | 43,90% | +2,40% | +2,09% | -1,38% | +4,43% | PRIMA CALIBRAZIONE |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 44 | 52,27% | +2,67% | +2,67% | -1,35% | +4,79% | PRIMA CALIBRAZIONE |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 44 | 52,27% | +2,67% | +2,67% | -1,35% | +4,79% | PRIMA CALIBRAZIONE |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 35 | 48,57% | +2,08% | +2,08% | -1,57% | +4,07% | PRIMA CALIBRAZIONE |
| BTC | 5g | Tecnico | CALIBRABILE | 39 | 41,03% | +3,15% | -1,19% | -1,08% | +5,31% | PRIMA CALIBRAZIONE |
| BTC | 5g | Classic technical | CALIBRABILE | 12 | 41,67% | +7,17% | -2,51% | -0,07% | +8,71% | FEEDBACK RAPIDO |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 50,00% | +2,17% | +2,17% | +0,08% | +5,37% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 39 | 51,28% | +3,23% | +2,95% | -1,62% | +5,68% | PRIMA CALIBRAZIONE |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 42 | 59,52% | +3,59% | +3,59% | -1,61% | +6,02% | PRIMA CALIBRAZIONE |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 42 | 59,52% | +3,59% | +3,59% | -1,61% | +6,02% | PRIMA CALIBRAZIONE |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 35 | 60,00% | +3,17% | +3,17% | -1,80% | +5,49% | PRIMA CALIBRAZIONE |
| BTC | 7g | Tecnico | CALIBRABILE | 37 | 35,14% | +4,38% | -2,51% | -1,31% | +6,69% | PRIMA CALIBRAZIONE |
| BTC | 7g | Classic technical | CALIBRABILE | 10 | 20,00% | +11,13% | -7,29% | +0,03% | +13,42% | FEEDBACK RAPIDO |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,77% | +1,77% | -0,79% | +4,24% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 36 | 50,00% | +3,62% | +3,37% | -2,38% | +6,08% | PRIMA CALIBRAZIONE |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 39 | 56,41% | +3,84% | +3,84% | -2,35% | +6,44% | PRIMA CALIBRAZIONE |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 39 | 56,41% | +3,84% | +3,84% | -2,35% | +6,44% | PRIMA CALIBRAZIONE |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 34 | 61,76% | +3,94% | +3,94% | -2,29% | +6,32% | PRIMA CALIBRAZIONE |
| BTC | 10g | Tecnico | CALIBRABILE | 34 | 29,41% | +4,58% | -3,24% | -2,08% | +7,20% | PRIMA CALIBRAZIONE |
| BTC | 10g | Classic technical | CALIBRABILE | 8 | 0,00% | +13,19% | -13,19% | -0,77% | +15,42% | FEEDBACK RAPIDO |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,43% | -0,43% | -2,30% | +4,24% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 33 | 57,58% | +4,04% | +3,93% | -2,80% | +7,09% | PRIMA CALIBRAZIONE |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 35 | 57,14% | +3,72% | +3,72% | -2,83% | +6,84% | PRIMA CALIBRAZIONE |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 35 | 57,14% | +3,72% | +3,72% | -2,83% | +6,84% | PRIMA CALIBRAZIONE |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 31 | 64,52% | +4,52% | +4,52% | -2,62% | +7,41% | PRIMA CALIBRAZIONE |
| BTC | 14g | Tecnico | CALIBRABILE | 30 | 63,33% | +4,55% | +2,70% | -2,56% | +7,70% | PRIMA CALIBRAZIONE |
| BTC | 14g | Classic technical | CALIBRABILE | 5 | 40,00% | +5,63% | -5,63% | -1,27% | +8,59% | FEEDBACK RAPIDO |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -2,25% | -2,25% | -3,05% | +4,24% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 28 | 50,00% | +6,28% | +6,04% | -2,90% | +9,77% | FEEDBACK RAPIDO |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 30 | 60,00% | +5,78% | +5,78% | -2,95% | +9,30% | PRIMA CALIBRAZIONE |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 30 | 60,00% | +5,78% | +5,78% | -2,95% | +9,30% | PRIMA CALIBRAZIONE |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 26 | 65,38% | +6,89% | +6,89% | -2,72% | +10,36% | FEEDBACK RAPIDO |
| BTC | 21g | Tecnico | CALIBRABILE | 25 | 28,00% | +6,63% | -1,13% | -2,65% | +10,19% | FEEDBACK RAPIDO |
| BTC | 21g | Classic technical | CALIBRABILE | 4 | 0,00% | +11,68% | -11,68% | -1,55% | +14,27% | FEEDBACK RAPIDO |
| BTC | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,21% | +1,21% | -3,06% | +4,24% | FEEDBACK RAPIDO |
| BTC | 30g | Global confluence | BENCHMARK | 19 | 84,21% | +8,15% | +5,88% | -3,20% | +11,73% | FEEDBACK RAPIDO |
| BTC | 30g | Famiglia statistica | CALIBRABILE | 21 | 76,19% | +8,14% | +8,14% | -3,24% | +11,87% | FEEDBACK RAPIDO |
| BTC | 30g | Scanner grezzo | DIAGNOSTICO | 21 | 76,19% | +8,14% | +8,14% | -3,24% | +11,87% | FEEDBACK RAPIDO |
| BTC | 30g | Market regime grezzo | DIAGNOSTICO | 17 | 76,47% | +8,94% | +8,94% | -2,95% | +13,00% | FEEDBACK RAPIDO |
| BTC | 30g | Tecnico | CALIBRABILE | 17 | 35,29% | +7,58% | -4,90% | -2,88% | +11,85% | FEEDBACK RAPIDO |
| BTC | 30g | Classic technical | CALIBRABILE | 2 | 0,00% | +24,39% | -24,39% | -2,23% | +27,64% | FEEDBACK RAPIDO |
| BTC | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +0,16% | +0,16% | -3,06% | +4,24% | FEEDBACK RAPIDO |
| BTC | 45g | Global confluence | BENCHMARK | 6 | 100,00% | +23,99% | +23,99% | -2,29% | +26,87% | FEEDBACK RAPIDO |
| BTC | 45g | Famiglia statistica | CALIBRABILE | 6 | 100,00% | +23,99% | +23,99% | -2,29% | +26,87% | FEEDBACK RAPIDO |
| BTC | 45g | Scanner grezzo | DIAGNOSTICO | 6 | 100,00% | +23,99% | +23,99% | -2,29% | +26,87% | FEEDBACK RAPIDO |
| BTC | 45g | Market regime grezzo | DIAGNOSTICO | 6 | 100,00% | +23,99% | +23,99% | -2,29% | +26,87% | FEEDBACK RAPIDO |
| BTC | 45g | Tecnico | CALIBRABILE | 5 | 40,00% | +24,69% | -5,00% | -2,09% | +27,36% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 46 | 47,83% | +0,50% | +0,42% | -0,08% | +1,58% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 47 | 57,45% | +0,42% | +0,61% | -0,18% | +1,46% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 47 | 57,45% | +0,42% | +0,61% | -0,18% | +1,46% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,15% | +0,26% | -0,32% | +0,87% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Tecnico | CALIBRABILE | 41 | 56,10% | +0,32% | +0,52% | -0,31% | +1,35% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Classic technical | CALIBRABILE | 31 | 41,94% | +0,27% | -0,51% | -0,38% | +0,97% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 71,43% | +2,86% | +2,41% | +1,15% | +3,54% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 45 | 51,11% | +0,98% | +0,97% | +0,22% | +2,36% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 46 | 52,17% | +0,84% | +1,04% | +0,11% | +2,15% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 46 | 52,17% | +0,84% | +1,04% | +0,11% | +2,15% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 38 | 50,00% | +0,36% | +0,74% | -0,26% | +1,41% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Tecnico | CALIBRABILE | 40 | 62,50% | +0,35% | +0,81% | -0,35% | +1,66% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Classic technical | CALIBRABILE | 31 | 45,16% | +0,67% | -1,20% | -0,10% | +1,65% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 57,14% | +4,25% | +3,88% | +3,39% | +6,58% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 44 | 47,73% | +1,43% | +1,68% | -1,44% | +4,33% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 46 | 52,17% | +1,28% | +1,55% | -1,53% | +4,11% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 46 | 52,17% | +1,28% | +1,55% | -1,53% | +4,11% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,84% | +1,55% | -1,48% | +3,36% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Tecnico | CALIBRABILE | 39 | 48,72% | +0,28% | +0,71% | -1,84% | +2,91% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Classic technical | CALIBRABILE | 31 | 32,26% | +1,30% | -2,13% | -1,89% | +4,20% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 57,14% | +3,59% | +3,29% | -0,23% | +7,51% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 42 | 57,14% | +2,82% | +3,42% | -1,94% | +6,91% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 44 | 54,55% | +2,60% | +3,18% | -2,02% | +6,59% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 44 | 54,55% | +2,60% | +3,18% | -2,02% | +6,59% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +2,45% | +3,08% | -2,17% | +5,74% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Tecnico | CALIBRABILE | 37 | 62,16% | +1,44% | +1,09% | -2,43% | +5,30% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Classic technical | CALIBRABILE | 29 | 41,38% | +3,19% | -3,72% | -2,28% | +7,24% | FEEDBACK RAPIDO |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 6 | 50,00% | +3,80% | +3,53% | +0,14% | +10,26% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 40 | 67,50% | +4,02% | +5,12% | -2,08% | +9,15% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 42 | 64,29% | +3,71% | +4,73% | -2,20% | +8,76% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 42 | 64,29% | +3,71% | +4,73% | -2,20% | +8,76% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,59% | +4,60% | -2,54% | +8,00% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Tecnico | CALIBRABILE | 35 | 65,71% | +2,27% | +2,31% | -2,67% | +7,03% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Classic technical | CALIBRABILE | 27 | 44,44% | +4,34% | -4,34% | -2,39% | +9,14% | FEEDBACK RAPIDO |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +3,64% | +3,43% | +1,17% | +11,40% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 37 | 62,16% | +3,36% | +5,04% | -3,11% | +8,88% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 39 | 61,54% | +3,09% | +4,71% | -3,18% | +8,48% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 39 | 61,54% | +3,09% | +4,71% | -3,18% | +8,48% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 37 | 62,16% | +3,30% | +4,92% | -3,16% | +8,69% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Tecnico | CALIBRABILE | 33 | 66,67% | +1,15% | +2,31% | -3,59% | +6,29% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Classic technical | CALIBRABILE | 26 | 50,00% | +3,10% | -3,10% | -3,17% | +9,15% | FEEDBACK RAPIDO |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 75,00% | +0,93% | +0,18% | -1,31% | +5,72% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 33 | 66,67% | +3,68% | +6,50% | -3,93% | +9,47% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 35 | 71,43% | +3,35% | +6,03% | -3,96% | +8,99% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 35 | 71,43% | +3,35% | +6,03% | -3,96% | +8,99% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 33 | 72,73% | +3,65% | +6,30% | -3,97% | +9,26% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Tecnico | CALIBRABILE | 30 | 66,67% | -0,31% | +0,31% | -4,43% | +4,70% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Classic technical | CALIBRABILE | 23 | 60,87% | +1,45% | -1,45% | -4,25% | +6,95% | FEEDBACK RAPIDO |
| DOGE | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 75,00% | +12,47% | +2,65% | -1,31% | +16,91% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 28 | 71,43% | +4,71% | +3,30% | -4,71% | +11,83% | FEEDBACK RAPIDO |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 30 | 83,33% | +5,07% | +9,02% | -4,70% | +12,47% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 30 | 83,33% | +5,07% | +9,02% | -4,70% | +12,47% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 28 | 85,71% | +5,52% | +9,57% | -4,77% | +13,04% | FEEDBACK RAPIDO |
| DOGE | 21g | Tecnico | CALIBRABILE | 29 | 65,52% | +4,45% | -4,45% | -4,81% | +11,42% | FEEDBACK RAPIDO |
| DOGE | 21g | Classic technical | CALIBRABILE | 21 | 71,43% | +1,31% | -1,31% | -4,94% | +7,86% | FEEDBACK RAPIDO |
| DOGE | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +9,47% | -8,45% | -1,27% | +19,32% | FEEDBACK RAPIDO |
| DOGE | 30g | Global confluence | BENCHMARK | 20 | 75,00% | +6,44% | +0,95% | -5,84% | +14,30% | FEEDBACK RAPIDO |
| DOGE | 30g | Famiglia statistica | CALIBRABILE | 21 | 80,95% | +7,04% | +4,86% | -5,88% | +15,39% | FEEDBACK RAPIDO |
| DOGE | 30g | Scanner grezzo | DIAGNOSTICO | 21 | 80,95% | +7,04% | +4,86% | -5,88% | +15,39% | FEEDBACK RAPIDO |
| DOGE | 30g | Market regime grezzo | DIAGNOSTICO | 19 | 89,47% | +4,84% | +8,32% | -6,11% | +13,09% | FEEDBACK RAPIDO |
| DOGE | 30g | Tecnico | CALIBRABILE | 21 | 57,14% | +7,04% | -7,04% | -5,88% | +15,39% | FEEDBACK RAPIDO |
| DOGE | 30g | Classic technical | CALIBRABILE | 17 | 64,71% | +4,96% | -4,96% | -5,74% | +12,22% | FEEDBACK RAPIDO |
| DOGE | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +31,53% | +31,53% | -1,85% | +40,20% | FEEDBACK RAPIDO |
| DOGE | 45g | Global confluence | BENCHMARK | 6 | 0,00% | +22,35% | -22,35% | -6,84% | +35,71% | FEEDBACK RAPIDO |
| DOGE | 45g | Famiglia statistica | CALIBRABILE | 6 | 0,00% | +22,35% | -22,35% | -6,84% | +35,71% | FEEDBACK RAPIDO |
| DOGE | 45g | Scanner grezzo | DIAGNOSTICO | 6 | 0,00% | +22,35% | -22,35% | -6,84% | +35,71% | FEEDBACK RAPIDO |
| DOGE | 45g | Market regime grezzo | DIAGNOSTICO | 6 | 0,00% | +22,35% | -22,35% | -6,84% | +35,71% | FEEDBACK RAPIDO |
| DOGE | 45g | Tecnico | CALIBRABILE | 6 | 0,00% | +22,35% | -22,35% | -6,84% | +35,71% | FEEDBACK RAPIDO |
| DOGE | 45g | Classic technical | CALIBRABILE | 6 | 0,00% | +22,35% | -22,35% | -6,84% | +35,71% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 41 | 58,54% | +0,89% | +0,74% | +0,24% | +1,90% | PRIMA CALIBRAZIONE |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 43 | 60,47% | +0,51% | +0,49% | -0,06% | +1,48% | PRIMA CALIBRAZIONE |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 46 | 58,70% | +0,55% | +0,39% | -0,04% | +1,51% | PRIMA CALIBRAZIONE |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +0,27% | +0,39% | -0,30% | +0,87% | PRIMA CALIBRAZIONE |
| SOL | 1g | Tecnico | CALIBRABILE | 45 | 53,33% | +0,50% | +0,47% | -0,12% | +1,42% | PRIMA CALIBRAZIONE |
| SOL | 1g | Classic technical | CALIBRABILE | 29 | 55,17% | +0,85% | +0,79% | +0,08% | +1,93% | FEEDBACK RAPIDO |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 40 | 55,00% | +1,67% | +1,50% | +0,74% | +2,87% | PRIMA CALIBRAZIONE |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 42 | 50,00% | +1,17% | +0,60% | +0,23% | +2,04% | PRIMA CALIBRAZIONE |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 45 | 48,89% | +1,12% | +0,54% | +0,21% | +2,09% | PRIMA CALIBRAZIONE |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +0,76% | +0,78% | -0,00% | +1,60% | PRIMA CALIBRAZIONE |
| SOL | 2g | Tecnico | CALIBRABILE | 44 | 45,45% | +1,04% | +0,34% | +0,18% | +2,23% | PRIMA CALIBRAZIONE |
| SOL | 2g | Classic technical | CALIBRABILE | 28 | 57,14% | +1,31% | +1,27% | +0,42% | +2,40% | FEEDBACK RAPIDO |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 39 | 58,97% | +2,49% | +2,26% | -1,15% | +4,66% | PRIMA CALIBRAZIONE |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 41 | 48,78% | +1,83% | +1,11% | -1,55% | +4,00% | PRIMA CALIBRAZIONE |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 44 | 47,73% | +1,73% | +1,02% | -1,52% | +3,96% | PRIMA CALIBRAZIONE |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +1,43% | +1,38% | -1,48% | +3,53% | PRIMA CALIBRAZIONE |
| SOL | 3g | Tecnico | CALIBRABILE | 43 | 48,84% | +1,55% | +0,02% | -1,61% | +3,63% | PRIMA CALIBRAZIONE |
| SOL | 3g | Classic technical | CALIBRABILE | 27 | 55,56% | +1,57% | +1,37% | -1,52% | +3,62% | FEEDBACK RAPIDO |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 50,00% | +1,27% | +1,27% | -2,62% | +5,77% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 37 | 62,16% | +4,08% | +3,94% | -1,63% | +7,09% | PRIMA CALIBRAZIONE |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 39 | 53,85% | +3,16% | +1,77% | -2,05% | +6,18% | PRIMA CALIBRAZIONE |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 42 | 52,38% | +2,99% | +1,59% | -2,05% | +6,02% | PRIMA CALIBRAZIONE |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +2,66% | +2,88% | -2,09% | +5,82% | PRIMA CALIBRAZIONE |
| SOL | 5g | Tecnico | CALIBRABILE | 41 | 46,34% | +2,99% | -0,89% | -2,24% | +5,88% | PRIMA CALIBRAZIONE |
| SOL | 5g | Classic technical | CALIBRABILE | 25 | 60,00% | +2,17% | +1,94% | -2,03% | +4,70% | FEEDBACK RAPIDO |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 33,33% | +1,18% | +1,18% | -1,95% | +5,20% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 35 | 65,71% | +5,39% | +5,54% | -2,03% | +8,81% | PRIMA CALIBRAZIONE |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 37 | 64,86% | +4,30% | +3,90% | -2,48% | +7,81% | PRIMA CALIBRAZIONE |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 40 | 65,00% | +3,97% | +3,61% | -2,50% | +7,52% | PRIMA CALIBRAZIONE |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 34 | 61,76% | +4,35% | +4,41% | -2,45% | +7,76% | PRIMA CALIBRAZIONE |
| SOL | 7g | Tecnico | CALIBRABILE | 39 | 35,90% | +3,92% | -2,51% | -2,71% | +7,43% | PRIMA CALIBRAZIONE |
| SOL | 7g | Classic technical | CALIBRABILE | 23 | 47,83% | +1,60% | +1,68% | -2,66% | +4,77% | FEEDBACK RAPIDO |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 33,33% | +3,96% | +3,96% | -2,17% | +8,29% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 32 | 65,62% | +6,02% | +6,26% | -3,00% | +9,59% | PRIMA CALIBRAZIONE |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 35 | 68,57% | +5,41% | +6,03% | -3,34% | +8,82% | PRIMA CALIBRAZIONE |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 38 | 65,79% | +4,96% | +5,57% | -3,34% | +8,43% | PRIMA CALIBRAZIONE |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 33 | 63,64% | +6,05% | +5,88% | -3,17% | +9,27% | PRIMA CALIBRAZIONE |
| SOL | 10g | Tecnico | CALIBRABILE | 37 | 40,54% | +4,48% | -4,61% | -3,45% | +8,21% | PRIMA CALIBRAZIONE |
| SOL | 10g | Classic technical | CALIBRABILE | 21 | 52,38% | -0,08% | +0,08% | -3,74% | +3,68% | FEEDBACK RAPIDO |
| SOL | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 50,00% | -2,05% | -2,05% | -4,86% | +1,05% | FEEDBACK RAPIDO |
| SOL | 10g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 14g | Global confluence | BENCHMARK | 28 | 71,43% | +5,80% | +7,10% | -3,87% | +10,55% | FEEDBACK RAPIDO |
| SOL | 14g | Famiglia statistica | CALIBRABILE | 31 | 83,87% | +5,69% | +6,90% | -4,05% | +9,76% | PRIMA CALIBRAZIONE |
| SOL | 14g | Scanner grezzo | DIAGNOSTICO | 34 | 85,29% | +4,92% | +6,56% | -4,04% | +9,25% | PRIMA CALIBRAZIONE |
| SOL | 14g | Market regime grezzo | DIAGNOSTICO | 29 | 68,97% | +6,31% | +6,43% | -3,75% | +10,35% | FEEDBACK RAPIDO |
| SOL | 14g | Tecnico | CALIBRABILE | 33 | 33,33% | +3,19% | -3,81% | -4,24% | +7,75% | PRIMA CALIBRAZIONE |
| SOL | 14g | Classic technical | CALIBRABILE | 21 | 38,10% | +1,19% | -1,19% | -4,25% | +5,07% | FEEDBACK RAPIDO |
| SOL | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 50,00% | +8,38% | +8,38% | -5,94% | +13,89% | FEEDBACK RAPIDO |
| SOL | 14g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 21g | Global confluence | BENCHMARK | 23 | 65,22% | +8,57% | +7,02% | -5,27% | +13,95% | FEEDBACK RAPIDO |
| SOL | 21g | Famiglia statistica | CALIBRABILE | 26 | 80,77% | +9,37% | +11,52% | -5,12% | +13,98% | FEEDBACK RAPIDO |
| SOL | 21g | Scanner grezzo | DIAGNOSTICO | 29 | 82,76% | +8,12% | +10,61% | -5,22% | +12,94% | FEEDBACK RAPIDO |
| SOL | 21g | Market regime grezzo | DIAGNOSTICO | 24 | 62,50% | +10,37% | +11,08% | -4,81% | +15,04% | FEEDBACK RAPIDO |
| SOL | 21g | Tecnico | CALIBRABILE | 30 | 40,00% | +7,87% | -9,24% | -5,28% | +12,62% | PRIMA CALIBRAZIONE |
| SOL | 21g | Classic technical | CALIBRABILE | 21 | 38,10% | +11,18% | -11,18% | -4,64% | +15,32% | FEEDBACK RAPIDO |
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

Generato: 2026-08-28 08:02 UTC

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
| BTC | 49 | PRIMA CALIBRAZIONE | 48 | 15 | 0 | 0 | Famiglia statistica | 1g | 56,25% | +0,50% | prima calibrazione possibile, solo modifiche leggere |
| SOL | 49 | PRIMA CALIBRAZIONE | 45 | 15 | 0 | 0 | Tecnico | 1g | 53,33% | +0,47% | prima calibrazione possibile, solo modifiche leggere |
| DOGE | 49 | PRIMA CALIBRAZIONE | 47 | 18 | 0 | 0 | Famiglia statistica | 1g | 57,45% | +0,61% | prima calibrazione possibile, solo modifiche leggere |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Classic technical | 16 | 37,50% | +0,55% | +1,21% | +0,46% | +1,86% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Famiglia statistica | 48 | 56,25% | +0,50% | +0,50% | +0,07% | +1,09% | PESO OK | 0,0 | MEDIA |
| BTC | 1g | BREVE | Microstruttura exchange | 3 | 66,67% | +0,27% | +0,27% | -0,26% | +0,74% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 43 | 39,53% | +0,19% | +0,67% | +0,21% | +1,26% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 2g | BREVE | Classic technical | 15 | 40,00% | +0,76% | +1,78% | +1,19% | +2,61% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Famiglia statistica | 47 | 57,45% | +1,03% | +1,03% | +0,45% | +1,76% | PESO OK | 0,0 | MEDIA |
| BTC | 2g | BREVE | Microstruttura exchange | 3 | 66,67% | +2,14% | +2,14% | +1,22% | +2,65% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 42 | 45,24% | +0,29% | +1,28% | +0,69% | +2,01% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 3g | BREVE | Classic technical | 14 | 42,86% | +0,16% | +2,91% | +0,06% | +4,37% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Famiglia statistica | 46 | 60,87% | +1,54% | +1,54% | -0,81% | +3,15% | PESO OK | 0,0 | MEDIA |
| BTC | 3g | BREVE | Microstruttura exchange | 3 | 66,67% | +1,42% | +1,42% | -0,64% | +3,18% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 41 | 39,02% | -0,08% | +1,97% | -0,57% | +3,53% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 5g | SETTIMANALE | Classic technical | 12 | 41,67% | -2,51% | +7,17% | -0,07% | +8,71% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 44 | 52,27% | +2,67% | +2,67% | -1,35% | +4,79% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 5g | SETTIMANALE | Microstruttura exchange | 2 | 50,00% | +2,17% | +2,17% | +0,08% | +5,37% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 39 | 41,03% | -1,19% | +3,15% | -1,08% | +5,31% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 7g | SETTIMANALE | Classic technical | 10 | 20,00% | -7,29% | +11,13% | +0,03% | +13,42% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 42 | 59,52% | +3,59% | +3,59% | -1,61% | +6,02% | PESO OK | 0,0 | MEDIA |
| BTC | 7g | SETTIMANALE | Microstruttura exchange | 1 | 100,00% | +1,77% | +1,77% | -0,79% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 37 | 35,14% | -2,51% | +4,38% | -1,31% | +6,69% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 10g | SETTIMANALE | Classic technical | 8 | 0,00% | -13,19% | +13,19% | -0,77% | +15,42% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 39 | 56,41% | +3,84% | +3,84% | -2,35% | +6,44% | PESO OK | 0,0 | MEDIA |
| BTC | 10g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -0,43% | -0,43% | -2,30% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 34 | 29,41% | -3,24% | +4,58% | -2,08% | +7,20% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 14g | SWING | Classic technical | 5 | 40,00% | -5,63% | +5,63% | -1,27% | +8,59% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Famiglia statistica | 35 | 57,14% | +3,72% | +3,72% | -2,83% | +6,84% | PESO OK | 0,0 | MEDIA |
| BTC | 14g | SWING | Microstruttura exchange | 1 | 0,00% | -2,25% | -2,25% | -3,05% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 30 | 63,33% | +2,70% | +4,55% | -2,56% | +7,70% | PESO OK | 0,0 | MEDIA |
| BTC | 21g | SWING | Classic technical | 4 | 0,00% | -11,68% | +11,68% | -1,55% | +14,27% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Famiglia statistica | 30 | 60,00% | +5,78% | +5,78% | -2,95% | +9,30% | PESO OK | 0,0 | MEDIA |
| BTC | 21g | SWING | Microstruttura exchange | 1 | 100,00% | +1,21% | +1,21% | -3,06% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Tecnico | 25 | 28,00% | -1,13% | +6,63% | -2,65% | +10,19% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Classic technical | 2 | 0,00% | -24,39% | +24,39% | -2,23% | +27,64% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Famiglia statistica | 21 | 76,19% | +8,14% | +8,14% | -3,24% | +11,87% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Microstruttura exchange | 1 | 100,00% | +0,16% | +0,16% | -3,06% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Tecnico | 17 | 35,29% | -4,90% | +7,58% | -2,88% | +11,85% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Famiglia statistica | 6 | 100,00% | +23,99% | +23,99% | -2,29% | +26,87% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Tecnico | 5 | 40,00% | -5,00% | +24,69% | -2,09% | +27,36% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 31 | 41,94% | -0,51% | +0,27% | -0,38% | +0,97% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 1g | BREVE | Famiglia statistica | 47 | 57,45% | +0,61% | +0,42% | -0,18% | +1,46% | PESO OK | 0,0 | MEDIA |
| DOGE | 1g | BREVE | Microstruttura exchange | 7 | 71,43% | +2,41% | +2,86% | +1,15% | +3,54% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 41 | 56,10% | +0,52% | +0,32% | -0,31% | +1,35% | PESO OK | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Classic technical | 31 | 45,16% | -1,20% | +0,67% | -0,10% | +1,65% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Famiglia statistica | 46 | 52,17% | +1,04% | +0,84% | +0,11% | +2,15% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Microstruttura exchange | 7 | 57,14% | +3,88% | +4,25% | +3,39% | +6,58% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 40 | 62,50% | +0,81% | +0,35% | -0,35% | +1,66% | PESO OK | 0,0 | MEDIA |
| DOGE | 3g | BREVE | Classic technical | 31 | 32,26% | -2,13% | +1,30% | -1,89% | +4,20% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| DOGE | 3g | BREVE | Famiglia statistica | 46 | 52,17% | +1,55% | +1,28% | -1,53% | +4,11% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 3g | BREVE | Microstruttura exchange | 7 | 57,14% | +3,29% | +3,59% | -0,23% | +7,51% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 39 | 48,72% | +0,71% | +0,28% | -1,84% | +2,91% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 5g | SETTIMANALE | Classic technical | 29 | 41,38% | -3,72% | +3,19% | -2,28% | +7,24% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 44 | 54,55% | +3,18% | +2,60% | -2,02% | +6,59% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 5g | SETTIMANALE | Microstruttura exchange | 6 | 50,00% | +3,53% | +3,80% | +0,14% | +10,26% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 37 | 62,16% | +1,09% | +1,44% | -2,43% | +5,30% | PESO OK | 0,0 | MEDIA |
| DOGE | 7g | SETTIMANALE | Classic technical | 27 | 44,44% | -4,34% | +4,34% | -2,39% | +9,14% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 42 | 64,29% | +4,73% | +3,71% | -2,20% | +8,76% | PESO OK | 0,0 | MEDIA |
| DOGE | 7g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +3,43% | +3,64% | +1,17% | +11,40% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 35 | 65,71% | +2,31% | +2,27% | -2,67% | +7,03% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 10g | SETTIMANALE | Classic technical | 26 | 50,00% | -3,10% | +3,10% | -3,17% | +9,15% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 39 | 61,54% | +4,71% | +3,09% | -3,18% | +8,48% | PESO OK | 0,0 | MEDIA |
| DOGE | 10g | SETTIMANALE | Microstruttura exchange | 4 | 75,00% | +0,18% | +0,93% | -1,31% | +5,72% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 33 | 66,67% | +2,31% | +1,15% | -3,59% | +6,29% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 14g | SWING | Classic technical | 23 | 60,87% | -1,45% | +1,45% | -4,25% | +6,95% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Famiglia statistica | 35 | 71,43% | +6,03% | +3,35% | -3,96% | +8,99% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 14g | SWING | Microstruttura exchange | 4 | 75,00% | +2,65% | +12,47% | -1,31% | +16,91% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 30 | 66,67% | +0,31% | -0,31% | -4,43% | +4,70% | PESO OK | 0,0 | MEDIA |
| DOGE | 21g | SWING | Classic technical | 21 | 71,43% | -1,31% | +1,31% | -4,94% | +7,86% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Famiglia statistica | 30 | 83,33% | +9,02% | +5,07% | -4,70% | +12,47% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 21g | SWING | Microstruttura exchange | 3 | 66,67% | -8,45% | +9,47% | -1,27% | +19,32% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Tecnico | 29 | 65,52% | -4,45% | +4,45% | -4,81% | +11,42% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Classic technical | 17 | 64,71% | -4,96% | +4,96% | -5,74% | +12,22% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Famiglia statistica | 21 | 80,95% | +4,86% | +7,04% | -5,88% | +15,39% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Microstruttura exchange | 2 | 100,00% | +31,53% | +31,53% | -1,85% | +40,20% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Tecnico | 21 | 57,14% | -7,04% | +7,04% | -5,88% | +15,39% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Classic technical | 6 | 0,00% | -22,35% | +22,35% | -6,84% | +35,71% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Famiglia statistica | 6 | 0,00% | -22,35% | +22,35% | -6,84% | +35,71% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Tecnico | 6 | 0,00% | -22,35% | +22,35% | -6,84% | +35,71% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Classic technical | 29 | 55,17% | +0,79% | +0,85% | +0,08% | +1,93% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Famiglia statistica | 43 | 60,47% | +0,49% | +0,51% | -0,06% | +1,48% | PESO OK | 0,0 | MEDIA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 45 | 53,33% | +0,47% | +0,50% | -0,12% | +1,42% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Classic technical | 28 | 57,14% | +1,27% | +1,31% | +0,42% | +2,40% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Famiglia statistica | 42 | 50,00% | +0,60% | +1,17% | +0,23% | +2,04% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Microstruttura exchange | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 44 | 45,45% | +0,34% | +1,04% | +0,18% | +2,23% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Classic technical | 27 | 55,56% | +1,37% | +1,57% | -1,52% | +3,62% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Famiglia statistica | 41 | 48,78% | +1,11% | +1,83% | -1,55% | +4,00% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Microstruttura exchange | 4 | 50,00% | +1,27% | +1,27% | -2,62% | +5,77% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 43 | 48,84% | +0,02% | +1,55% | -1,61% | +3,63% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Classic technical | 25 | 60,00% | +1,94% | +2,17% | -2,03% | +4,70% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 39 | 53,85% | +1,77% | +3,16% | -2,05% | +6,18% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Microstruttura exchange | 3 | 33,33% | +1,18% | +1,18% | -1,95% | +5,20% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 41 | 46,34% | -0,89% | +2,99% | -2,24% | +5,88% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Classic technical | 23 | 47,83% | +1,68% | +1,60% | -2,66% | +4,77% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 37 | 64,86% | +3,90% | +4,30% | -2,48% | +7,81% | PESO OK | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Microstruttura exchange | 3 | 33,33% | +3,96% | +3,96% | -2,17% | +8,29% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 39 | 35,90% | -2,51% | +3,92% | -2,71% | +7,43% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 10g | SETTIMANALE | Classic technical | 21 | 52,38% | +0,08% | -0,08% | -3,74% | +3,68% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 35 | 68,57% | +6,03% | +5,41% | -3,34% | +8,82% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Microstruttura exchange | 2 | 50,00% | -2,05% | -2,05% | -4,86% | +1,05% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 37 | 40,54% | -4,61% | +4,48% | -3,45% | +8,21% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 14g | SWING | Classic technical | 21 | 38,10% | -1,19% | +1,19% | -4,25% | +5,07% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Famiglia statistica | 31 | 83,87% | +6,90% | +5,69% | -4,05% | +9,76% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 14g | SWING | Frattale SOL | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Microstruttura exchange | 2 | 50,00% | +8,38% | +8,38% | -5,94% | +13,89% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Tecnico | 33 | 33,33% | -3,81% | +3,19% | -4,24% | +7,75% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 21g | SWING | Classic technical | 21 | 38,10% | -11,18% | +11,18% | -4,64% | +15,32% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Famiglia statistica | 26 | 80,77% | +11,52% | +9,37% | -5,12% | +13,98% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Frattale SOL | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Microstruttura exchange | 1 | 0,00% | -3,18% | -3,18% | -9,62% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Tecnico | 30 | 40,00% | -9,24% | +7,87% | -5,28% | +12,62% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 30g | MEDIO | Classic technical | 13 | 15,38% | -17,86% | +17,86% | -6,31% | +22,43% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Famiglia statistica | 17 | 82,35% | +12,76% | +13,38% | -7,13% | +17,87% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Frattale SOL | 1 | 0,00% | -4,50% | -4,50% | -9,39% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Microstruttura exchange | 1 | 100,00% | +8,54% | +8,54% | -9,62% | +9,47% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Tecnico | 21 | 19,05% | -11,81% | +10,92% | -7,08% | +15,20% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Famiglia statistica | 4 | 0,00% | -24,70% | +24,70% | -8,35% | +30,51% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Frattale SOL | 1 | 100,00% | +19,26% | +19,26% | -9,39% | +23,73% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Tecnico | 6 | 66,67% | +4,02% | +28,78% | -8,03% | +33,38% | OSSERVA | 0,0 | BASSA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 46 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 38 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 48 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Classic technical | 45 | 40,00% | +0,50% |
| BTC | BREVE | Famiglia statistica | 141 | 58,16% | +1,02% |
| BTC | BREVE | Microstruttura exchange | 9 | 66,67% | +1,28% |
| BTC | BREVE | Tecnico | 126 | 41,27% | +0,14% |
| BTC | SETTIMANALE | Classic technical | 30 | 23,33% | -6,95% |
| BTC | SETTIMANALE | Famiglia statistica | 125 | 56,00% | +3,35% |
| BTC | SETTIMANALE | Microstruttura exchange | 4 | 50,00% | +1,42% |
| BTC | SETTIMANALE | Tecnico | 110 | 35,45% | -2,27% |
| BTC | SWING | Classic technical | 9 | 22,22% | -8,32% |
| BTC | SWING | Famiglia statistica | 65 | 58,46% | +4,67% |
| BTC | SWING | Microstruttura exchange | 2 | 50,00% | -0,52% |
| BTC | SWING | Tecnico | 55 | 47,27% | +0,96% |
| BTC | MEDIO | Classic technical | 2 | 0,00% | -24,39% |
| BTC | MEDIO | Famiglia statistica | 27 | 81,48% | +11,66% |
| BTC | MEDIO | Microstruttura exchange | 1 | 100,00% | +0,16% |
| BTC | MEDIO | Tecnico | 22 | 36,36% | -4,92% |
| DOGE | BREVE | Classic technical | 93 | 39,78% | -1,28% |
| DOGE | BREVE | Famiglia statistica | 139 | 53,96% | +1,06% |
| DOGE | BREVE | Microstruttura exchange | 21 | 61,90% | +3,19% |
| DOGE | BREVE | Tecnico | 120 | 55,83% | +0,68% |
| DOGE | SETTIMANALE | Classic technical | 82 | 45,12% | -3,73% |
| DOGE | SETTIMANALE | Famiglia statistica | 125 | 60,00% | +4,18% |
| DOGE | SETTIMANALE | Microstruttura exchange | 15 | 60,00% | +2,60% |
| DOGE | SETTIMANALE | Tecnico | 105 | 64,76% | +1,88% |
| DOGE | SWING | Classic technical | 44 | 65,91% | -1,38% |
| DOGE | SWING | Famiglia statistica | 65 | 76,92% | +7,41% |
| DOGE | SWING | Microstruttura exchange | 7 | 71,43% | -2,11% |
| DOGE | SWING | Tecnico | 59 | 66,10% | -2,03% |
| DOGE | MEDIO | Classic technical | 23 | 47,83% | -9,50% |
| DOGE | MEDIO | Famiglia statistica | 27 | 62,96% | -1,18% |
| DOGE | MEDIO | Microstruttura exchange | 2 | 100,00% | +31,53% |
| DOGE | MEDIO | Tecnico | 27 | 44,44% | -10,44% |
| SOL | BREVE | Classic technical | 84 | 55,95% | +1,14% |
| SOL | BREVE | Famiglia statistica | 126 | 53,17% | +0,73% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 14 | 50,00% | +1,35% |
| SOL | BREVE | Tecnico | 132 | 49,24% | +0,28% |
| SOL | SETTIMANALE | Classic technical | 69 | 53,62% | +1,29% |
| SOL | SETTIMANALE | Famiglia statistica | 111 | 62,16% | +3,82% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Microstruttura exchange | 8 | 37,50% | +1,41% |
| SOL | SETTIMANALE | Tecnico | 117 | 41,03% | -2,61% |
| SOL | SWING | Classic technical | 42 | 38,10% | -6,19% |
| SOL | SWING | Famiglia statistica | 57 | 82,46% | +9,01% |
| SOL | SWING | Frattale SOL | 2 | 0,00% | -3,49% |
| SOL | SWING | Microstruttura exchange | 3 | 33,33% | +4,53% |
| SOL | SWING | Tecnico | 63 | 36,51% | -6,40% |
| SOL | MEDIO | Classic technical | 13 | 15,38% | -17,86% |
| SOL | MEDIO | Famiglia statistica | 21 | 66,67% | +5,62% |
| SOL | MEDIO | Frattale SOL | 2 | 50,00% | +7,38% |
| SOL | MEDIO | Microstruttura exchange | 1 | 100,00% | +8,54% |
| SOL | MEDIO | Tecnico | 27 | 29,63% | -8,29% |

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
| BTC     |         49 |              21 |          28 | RACCOLTA DATI | 0,00%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| SOL     |         49 |              21 |          28 | RACCOLTA DATI | 4,76%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| DOGE    |         49 |              21 |          28 | RACCOLTA DATI | 9,52%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |

Regola: sotto 60 controlli osserva soltanto; da 100+ controlli può diventare utile per correggere rischio spot/leva nel Decision Report.

## Ultima lettura rapida

| Asset   | Rischio spot   | Rischio leva   | Nota leva                                                               |
|:--------|:---------------|:---------------|:------------------------------------------------------------------------|
| BTC     | MEDIO          | MOLTO ALTO     | spot preferibile; leva molto pericolosa anche 2x/3x senza margine largo |
| SOL     | ALTO           | MOLTO ALTO     | spot preferibile; leva molto pericolosa anche 2x/3x senza margine largo |
| DOGE    | MEDIO          | MOLTO ALTO     | spot preferibile; leva molto pericolosa anche 2x/3x senza margine largo |
<!-- RISK_CALIBRATION_END -->

</details>
<!-- COMPACT_SECTION_END:risk_calibration -->

<!-- COMPACT_SECTION_START:global_confluence -->
<details open>
<summary><strong>🌐 Global Confluence — quadro finale</strong></summary>

<!-- GLOBAL_CONFLUENCE_START -->
# Sintesi finale di confluenza

Generato: 2026-08-28 08:02 UTC


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
| SOL | +8 | POSITIVA FORTE | Rialzista | MEDIA / ALTA | HOLD / ACCUMULO A TRANCHE, NO LEVA AGGRESSIVA | Doppio minimo target raggiunto finché mantiene 78,73; nuova conferma tecnica sopra 127,97; milestone analogiche 121,18 / 148,37, valide soltanto se rientra anche il gap frattale. | Allarmi sotto 98,53 / 74,20 / 62,19. |
| DOGE | 0 | MISTA / PARZIALE | Neutrale / misto | BASSA / RACCOLTA DATI | STAI ALLA FINESTRA | Sopra 0.09998 migliora; sopra 0.06933 viene invalidato il pattern ribassista dominante. | Sotto 0.06895 il rischio ribassista aumenta. |

## Punteggi per modulo

| Asset | Scanner grezzo | Market grezzo | Famiglia statistica | Scanner path | Tecnico | Classic tech | Frattale SOL | Fractal path | RSI top-cycle | Lifecycle EMA | Exchange flow | Futures | Daily change | Totale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +3 | 0 | +3 | 0 | +3 | +1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | +7 |
| SOL | +3 | 0 | +3 | 0 | +3 | +1 | 0 | 0 | 0 | 0 | 0 | 0 | +1 | +8 |
| DOGE | -1 | 0 | -1 | 0 | +1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

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
- Scanner (diagnostico, già incluso nella Famiglia statistica): **+3** — Casi positivi 70,00%, return centrale 30g +6,41%. Direzione scanner: SALITA. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **0** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 0, positivi 30g n/a, return p50 n/a.
- Scanner path: **0** — Controlli disponibili 47. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **+3** — Score tecnico 7/12, verdetto rialzista tecnico, trend rialzista, struttura compressione / triangolo, divergenza rialzista nascosta rsi, Wyckoff markup / fase rialzista, pattern score 0 (rialzista Doppio minimo / TARGET RAGGIUNTO; ribassista Doppio massimo / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **+1** — Score classico 6/12, verdetto COSTRUTTIVO / CONFERMA PARZIALE, stage STAGE 3 / DISTRIBUZIONE O PAUSA, struttura MASSIMI E MINIMI CRESCENTI, Wyckoff SIGN OF STRENGTH POSSIBILE, volatilità locale MEDIO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Non applicabile a questo asset.
- Fractal path: **0** — Non applicabile a questo asset.
- RSI top-cycle: **0** — Non applicabile a questo asset.
- Lifecycle EMA: **0** — Non applicabile a questo asset.
- Exchange flow: **0** — Flow +1.75, derivati +0.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +0.50; exchange 3/3, copertura 100%, consenso bull 0, bear 1, divergenze 0, campioni 4h 9 su 4.00h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias LEGGERMENTE POSITIVA / NON PESATA; confidenza BASSA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Rischio sotto, forza 2/5.
- Daily change: **0** — BTC: cambiamento medio in misto rispetto a ieri.

Conferme: Prima resistenza sopra 82.792; conferma del doppio minimo sopra 66.910.

Invalidazioni: Sotto 62.488 il quadro tecnico peggiora.

### SOL

- Confluenza: **POSITIVA FORTE**
- Bias: **Rialzista**
- Punteggio finale: **+8**
- Affidabilità: **MEDIA / ALTA**
- Azione coerente: **HOLD / ACCUMULO A TRANCHE, NO LEVA AGGRESSIVA**

SOL ha una confluenza molto interessante, ma resta più rischiosa di BTC. Le conferme tecniche e frattali devono comunque reggere prima di usare leva.

Dettaglio moduli:

- Famiglia statistica: **+3** — Scanner grezzo +3, Market Regime grezzo 0, match regime 0. Regime ignorato: meno di 5 match utili. Punteggio contato nel Global: +3.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **+3** — Casi positivi 70,00%, return centrale 30g +6,90%. Direzione scanner: SALITA. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **0** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 0, positivi 30g n/a, return p50 n/a.
- Scanner path: **0** — Controlli disponibili 47. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **+3** — Score tecnico 8/12, verdetto rialzista tecnico, trend rialzista, struttura compressione / triangolo, divergenza nessuna, Wyckoff markup / fase rialzista, pattern score 0 (rialzista Doppio minimo / TARGET RAGGIUNTO; ribassista Doppio massimo / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **+1** — Score classico 9/12, verdetto CONFERMATO RIALZISTA, stage STAGE 3 / DISTRIBUZIONE O PAUSA, struttura MASSIMI E MINIMI CRESCENTI, Wyckoff SIGN OF STRENGTH POSSIBILE, volatilità locale MEDIO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Verdetto ANALOGIA DEBOLE / SCENARIO SECONDARIO, somiglianza strutturale +63,74%, aderenza live +70,24%, errore live +14,88%, gap corrente +23,90%, peso operativo 0, tracking STRUTTURA STABILE, fase FRATTALE SOLO DI CONTESTO, rischio ALTO.
- Fractal path: **0** — Controlli disponibili 43, ma percorso ancorato non aderente: gap +23,90%, errore live +14,88%. Peso 0.
- RSI top-cycle: **0** — Rischio top-cycle RSI: BASSO.
- Lifecycle EMA: **0** — Contesto non pesato nel Global. Lifecycle score 2, bias CONTESTO DA OSSERVARE, EMA200 111,43 $, upside EMA200 +4,59%, gap EMA50/EMA200 -5,68%, hit EMA200 12w +90,00%, trend STABILE / DA CONFERMARE. Peso Global forzato a 0.
- Exchange flow: **0** — Flow +1.75, derivati +0.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +1.00; exchange 3/3, copertura 100%, consenso bull 1, bear 1, divergenze 0, campioni 4h 9 su 4.00h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias LEGGERMENTE POSITIVA / NON PESATA; confidenza MEDIA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Misto, forza 1/5.
- Daily change: **+1** — SOL: cambiamento forte in miglioramento rispetto a ieri.

Conferme: Doppio minimo target raggiunto finché mantiene 78,73; nuova conferma tecnica sopra 127,97; milestone analogiche 121,18 / 148,37, valide soltanto se rientra anche il gap frattale.

Invalidazioni: Allarmi sotto 98,53 / 74,20 / 62,19.

### DOGE

- Confluenza: **MISTA / PARZIALE**
- Bias: **Neutrale / misto**
- Punteggio finale: **0**
- Affidabilità: **BASSA / RACCOLTA DATI**
- Azione coerente: **STAI ALLA FINESTRA**

DOGE non ha ancora una confluenza pulita. Serve conferma tecnica prima di trattarlo come asset forte.

Dettaglio moduli:

- Famiglia statistica: **-1** — Scanner grezzo -1, Market Regime grezzo 0, match regime 0. Regime ignorato: meno di 5 match utili. Punteggio contato nel Global: -1.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **-1** — Casi positivi 37,50%, return centrale 30g -4,56%. Direzione scanner: DISCESA. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **0** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 0, positivi 30g n/a, return p50 n/a.
- Scanner path: **0** — Controlli disponibili 47. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **+1** — Score tecnico 2/12, verdetto neutrale / misto, trend misto, struttura rialzista con massimi e minimi crescenti, divergenza nessuna, Wyckoff markdown / fase ribassista, pattern score 0 (rialzista Triplo minimo / TARGET RAGGIUNTO; ribassista Doppio massimo / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **0** — Score classico 0/12, verdetto NEUTRALE / MISTO, stage STAGE 4 / MARKDOWN, struttura MASSIMI E MINIMI CRESCENTI, Wyckoff ACCUMULO POSSIBILE / RANGE BASSO, volatilità locale MEDIO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Non applicabile a questo asset.
- Fractal path: **0** — Non applicabile a questo asset.
- RSI top-cycle: **0** — Non applicabile a questo asset.
- Lifecycle EMA: **0** — Non applicabile a questo asset.
- Exchange flow: **0** — Flow +1.75, derivati +0.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +0.50; exchange 3/3, copertura 100%, consenso bull 1, bear 0, divergenze 1, campioni 4h 9 su 4.00h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias LEGGERMENTE POSITIVA / NON PESATA; confidenza BASSA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Misto, forza 1/5.
- Daily change: **0** — DOGE: nessun cambiamento forte in misto rispetto a ieri.

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

Generato: 2026-08-28 08:02 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [btc_macro_cycle_report.md](btc_macro_cycle_report.md)

Questo modulo descrive il contesto macro di Bitcoin. Non genera entrate tattiche, non autorizza leva e pesa **0** nel Global Confluence.

## Sintesi

| Voce | Valore | Lettura |
| --- | --- | --- |
| Prezzo BTC | 79.711 $ | prezzo corrente |
| Power Law centrale | 124.103 $ | deviazione -35,77% |
| Banda p10-p90 | 77.108 $ / 313.625 $ | BASSA NEL CORRIDOIO |
| Percentile residuo | 13,08% | posizione storica nel corridoio |
| Esponente β | 5,8104 | R² log-log 91,93% |
| Stabilità β | BASSA | range 1,3164 cambiando finestra |
| Ultimo halving | 2024-04-19 | 861 giorni fa |
| Fase ciclo | 58,93% | percentuale indicativa del ciclo quadriennale |
| Peso Global | 0 | CONTESTO MACRO / DIAGNOSTICO |

La Power Law viene trattata come regressione empirica, non come legge fisica. Il report mostra quanto cambia l'esponente usando finestre iniziali diverse e la confronta con il benchmark ingenuo 'prezzo invariato'.

## Bitcoin Power Law

- Campione: 2014-09-17 → 2026-08-28 (4364 osservazioni)
- Formula stimata: prezzo ≈ exp(-39.1127) × giorni^5.8104
- Prezzo centrale oggi: **124.103 $**
- Posizione corrente: **BASSA NEL CORRIDOIO**, percentile 13,08%
- Scarto dal centro: **-35,77%**

![Bitcoin Power Law](btc_power_law_chart.png)

![Bitcoin Power Law log-log](btc_power_law_loglog_chart.png)

### Stabilità dell'esponente

| Inizio campione | β | R² log-log |
| --- | --- | --- |
| 2014 | 5,8104 | 91,93% |
| 2015 | 5,8934 | 91,48% |
| 2016 | 5,5782 | 87,73% |
| 2017 | 4,8493 | 82,88% |
| 2018 | 4,5770 | 78,36% |

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
| 2012-11-28 → 2016-07-09 | 2015-01-14 | +32,19% | +23,05% | +63,98% | +141,61% |
| 2016-07-09 → 2020-05-11 | 2018-10-13 | +1,36% | -41,34% | -19,43% | +32,37% |
| 2020-05-11 → 2024-04-19 | 2022-09-06 | +5,93% | -9,89% | +19,10% | +36,71% |

Campione molto piccolo: questi rendimenti sono contesto di ciclo, non probabilità affidabili.

## SOL/BTC e DOGE/BTC dentro il tempo Bitcoin

![Altcoin nel ciclo BTC](alt_btc_cycle_spirals.png)

| Asset | Coppia | Forza vs BTC | Score raw | Candidato | 30g | Peso Global |
| --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | SOVRAPERFORMA BTC | 5 | 1 | 15.859373934185928 | 0 |
| DOGE | DOGE/BTC | SOTTOPERFORMA BTC | -6 | -1 | 0.21541909565405692 | 0 |

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

Generato: 2026-08-28 08:02 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [relative_strength_btc_report.md](relative_strength_btc_report.md)

Questo modulo controlla se SOL e DOGE stanno davvero battendo Bitcoin. Una salita in USD accompagnata da una coppia ALT/BTC ribassista è spesso soltanto trascinamento di BTC.

**Protezione iniziale:** il candidato relativo è limitato a -1/0/+1, ma il peso nel Global resta **0**. La coppia BTC conferma o indebolisce il tecnico USD; non viene sommata come secondo modulo indipendente.

## Sintesi

| Asset | Coppia | Prezzo | Score raw | Candidato | Peso Global | Forza vs BTC | Confidenza | 30g | Tecnico USD | Lettura combinata |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | 0.00133470 | +5 | +1 | 0 | SOVRAPERFORMA BTC | MEDIA | +15,86% | RIALZISTA | CONFERMA FORTE: sale in USD e batte BTC |
| DOGE | DOGE/BTC | 0.00000110 | -6 | -1 | 0 | SOTTOPERFORMA BTC | MEDIA | +0,22% | MISTA | FORZA RELATIVA NEGATIVA, USD ANCORA MISTO |

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
- **Rendimenti relativi:** 7g +11,60%; 30g +15,86%; 90g +19,28%; 180g +5,01%
- **Daily:** RSI 70.03; MA50 0.00119049; MA200 0.00117847
- **Weekly:** MA30 0.00118432; RSI 59.09
- **Livelli:** supporto 0.00122200; resistenza 0.00134900; breakout 60g 0.00134900; breakdown 60g 0.00110800
- **Pattern:** DOPPIO MINIMO / TARGET RAGGIUNTO; neckline 0.00120200; target 0.00125350
- **Fibonacci:** NON ATTIVO — 23.6% a 0.00128404
- **Fonte:** Yahoo Finance SOL-BTC (coppia diretta)
- **Motivi score:** prezzo sopra MA50 daily; prezzo sopra MA200 daily; prezzo sopra MA30 weekly; MA30 weekly in discesa; struttura con massimi/minimi crescenti; RSI relativo forte; MACD relativo positivo

![Grafico SOL/BTC](relative_strength_SOLBTC.png)

## DOGE/BTC

- **Verdetto relativo:** SOTTOPERFORMA BTC (-6)
- **Candidato futuro:** -1; **peso attuale Global: 0**
- **Lettura combinata USD/BTC:** FORZA RELATIVA NEGATIVA, USD ANCORA MISTO
- **Struttura:** VOLATILITÀ IN ESPANSIONE
- **Rendimenti relativi:** 7g -6,06%; 30g +0,22%; 90g -19,27%; 180g -21,42%
- **Daily:** RSI 46.27; MA50 0.00000111; MA200 0.00000128
- **Weekly:** MA30 0.00000128; RSI 36.76
- **Livelli:** supporto 0.00000110; resistenza 0.00000114; breakout 60g 0.00000133; breakdown 60g 0.00000100
- **Pattern:** DOPPIO MINIMO / TARGET RAGGIUNTO; neckline 0.00000115; target 0.00000128
- **Fibonacci:** NON ATTIVO — 23.6% a 0.00000112
- **Fonte:** Rapporto sintetico DOGE-USD / BTC-USD (sintetica)
- **Motivi score:** prezzo sotto MA50 daily; prezzo sotto MA200 daily; MA50 daily in discesa; prezzo sotto MA30 weekly; MA30 weekly in discesa; MACD relativo negativo

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
| SOL | 1g | 24 | 70,83% | +0,62% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 3g | 22 | 59,09% | +0,68% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 7g | 18 | 44,44% | -0,16% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 14g | 16 | 12,50% | -2,46% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 30g | 5 | 0,00% | -10,69% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 1g | 37 | 64,86% | -0,02% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 3g | 35 | 60,00% | +0,21% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 7g | 35 | 62,86% | +0,40% | ELIGIBILE FUTURO ±1 | 0 |
| DOGE | 14g | 33 | 69,70% | +0,16% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 30g | 19 | 73,68% | +0,44% | LOCKED / RACCOLTA LIVE | 0 |

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

Ultima candela SOL usata: **28 agosto 2026**

## SOL PRICE CONTEXT

| Voce | Valore | Provenienza / significato |
| --- | --- | --- |
| Anchor computazionale | 106,34 $ | 2026-08-28T07:59:27Z \| Yahoo Finance daily shared snapshot \| Close 1d |
| Candela anchor completata | NO | Stato esplicito; il valore non viene sostituito dal prezzo pubblico. |
| Riferimento pubblico corrente | 106,54 $ | 2026-08-28T08:01:00Z \| Yahoo Finance \| solo display |
| Età anchor alla generazione | 0h 2m | WITHIN_DAILY_REPORT_CADENCE |
| Gap corrente vs anchor | 0,20000 $ | +0,19% |
| Validità input modello | REPRODUCIBLE_SHARED_SNAPSHOT | Non è una dichiarazione di validità del segnale/trading. |

```text
COMPUTATIONAL_ANCHOR_PRICE=106.33999633789062
COMPUTATIONAL_ANCHOR_FIELD=Close
COMPUTATIONAL_ANCHOR_TIMESTAMP=2026-08-28T07:59:27Z
COMPUTATIONAL_ANCHOR_SYMBOL=SOL-USD
COMPUTATIONAL_ANCHOR_PROVIDER=Yahoo Finance daily shared snapshot
COMPUTATIONAL_ANCHOR_TIMEFRAME=1d
COMPUTATIONAL_ANCHOR_COMPLETED=NO
CURRENT_PUBLIC_REFERENCE_PRICE=106.54000091552734
CURRENT_PUBLIC_REFERENCE_TIMESTAMP=2026-08-28T08:01:00Z
CURRENT_PUBLIC_REFERENCE_ACQUIRED_AT=2026-08-28T08:01:34Z
CURRENT_PUBLIC_REFERENCE_SYMBOL=SOL-USD
CURRENT_PUBLIC_REFERENCE_PROVIDER=Yahoo Finance
CURRENT_PUBLIC_REFERENCE_FIELD=Close
CURRENT_PUBLIC_REFERENCE_TIMEFRAME=1m
CURRENT_PUBLIC_REFERENCE_STATUS=AVAILABLE
ANCHOR_AGE_SECONDS=127.465753
ANCHOR_AGE_HOURS=0.03540715361111111
CURRENT_VS_ANCHOR_GAP_USD=0.20000457763671875
CURRENT_VS_ANCHOR_GAP_PCT=0.18808029389170144
```

## Verdetto: ANALOGIA DEBOLE / SCENARIO SECONDARIO

- **Fase attuale:** FRATTALE SOLO DI CONTESTO
- **Somiglianza totale:** +63,74%
- **Somiglianza strutturale:** +63,74%
- **Aderenza prezzo live:** +70,24%
- **Errore medio live:** +14,88%
- **Gap prezzo corrente:** +23,90%
- **Peso operativo suggerito:** 0
- **Affidabilita:** BASSA
- **Rischio fase:** ALTO
- **Trend tracking:** STRUTTURA STABILE
- **Sintesi:** Esistono alcuni elementi comuni, ma non abbastanza per una conferma.
- **SOL è al giorno:** 83 dal bottom usato.
- **Giorno BTC equivalente:** 2023-02-12
- **Prossimo step:** Proiezione condizionale, non conferma operativa: **Spinta rialzista abbastanza pulita.** Zona bassa **106,34 $** intorno al **28 agosto 2026**; zona alta **121,18 $** intorno al **5 settembre 2026**; fine step circa **114,99 $** entro il **11 settembre 2026**.

### Metadata aderenza prezzo

```text
OPERATIONAL_VERDICT_REASON=ANALOGIA DEBOLE / SCENARIO SECONDARIO
PRICE_ADHERENCE_FAILED=YES
PRICE_ADHERENCE_LIVE_AVG_GAP_FAILED=NO
PRICE_ADHERENCE_LAST_GAP_FAILED=YES
PRICE_ADHERENCE_LIVE_AVG_GAP_THRESHOLD_PCT=15.0
PRICE_ADHERENCE_LAST_GAP_THRESHOLD_PCT=18.0
PRICE_ADHERENCE_OBSERVED_LIVE_AVG_GAP_PCT=14.88113993212513
PRICE_ADHERENCE_OBSERVED_LAST_GAP_PCT=23.897762541874613
```

## Somiglianza prima e dopo inizio programma

Questa sezione separa la somiglianza della forma dall'aderenza reale del prezzo.

- **Inizio programma/scanner:** 3 luglio 2026
- **Prima del programma** = backtest retroattivo.
- **Da inizio programma** = verifica live: è la parte più importante per l'uso operativo.

| Periodo | Date | Giorni | Aderenza prezzo | Errore medio | Gap ultimo | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| Prima del programma | 6 giugno 2026 -> 2 luglio 2026 | 27 | +87,95% | +6,02% | +21,89% | ABBASTANZA ALLINEATO |
| Da inizio programma | 3 luglio 2026 -> 28 agosto 2026 | 57 | +70,24% | +14,88% | +23,90% | DEVIAZIONE MODERATA |
| Totale dal bottom | 6 giugno 2026 -> 28 agosto 2026 | 84 | +75,93% | +12,03% | +23,90% | DEVIAZIONE MODERATA |

Nota: un frattale può avere una forma simile ma un prezzo distante. In quel caso non è operativo finché il gap non rientra.

## Lettura operativa veloce

Il frattale resta non operativo. Motivo effettivo: ANALOGIA DEBOLE / SCENARIO SECONDARIO.

| Voce | Risposta | Perché |
| --- | --- | --- |
| Uso operativo | NO | Peso 0 per il verdetto: ANALOGIA DEBOLE / SCENARIO SECONDARIO. |
| Aderenza live | +70,24% | Errore medio live +14,88%. |
| Gap corrente | +23,90% | Prezzo non aderente: superata almeno una soglia canonica (15% medio / 18% ultimo). |
| Prima conferma prezzo | 121,18 $ | Serve anche miglioramento del gap, non solo una candela sopra il livello. |
| Seconda conferma | 148,37 $ | Rende più credibile il percorso, ma non sostituisce l'aderenza. |
| Invalidazione soft | 98,53 $ | Sotto questa zona il quadro peggiora. |
| Invalidazione forte | 62,19 $ | Sotto il bottom il paragone è quasi rotto. |

## Target ciclo fino al top BTC 2025

| Voce | Valore |
| --- | --- |
| Stato | CONTESTO / NON OPERATIVO |
| Top BTC 2025 | 6 ottobre 2025 - 124.753 $ |
| Data SOL equivalente | 21 aprile 2029 |
| Target ciclo base dall'anchor modello | 608,87 $ |
| Massimo percorso base | 608,87 $ (21 aprile 2029) |

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
| Prima conferma | 121,18 $ | Deve accompagnarsi al rientro del gap. |
| Seconda conferma | 148,37 $ | Scenario più credibile. |
| Invalidazione soft | 98,53 $ | Il frattale si indebolisce. |
| Invalidazione forte | 62,19 $ | Il paragone si rompe. |

## Proiezione veloce con date SOL

| Orizzonte | Data SOL | BTC fece | SOL base | Min percorso | Max percorso |
| --- | --- | --- | --- | --- | --- |
| 7 giorni | 4 settembre 2026 | +11,66% | 118,73 $ | 106,34 $ | 120,26 $ |
| 14 giorni | 11 settembre 2026 | +8,14% | 114,99 $ | 106,34 $ | 121,18 $ |
| 30 giorni | 27 settembre 2026 | +13,58% | 120,78 $ | 98,53 $ | 121,18 $ |
| 60 giorni | 27 ottobre 2026 | +39,52% | 148,37 $ | 98,53 $ | 148,37 $ |
| 90 giorni | 26 novembre 2026 | +22,93% | 130,72 $ | 98,53 $ | 148,79 $ |
| 120 giorni | 26 dicembre 2026 | +18,88% | 126,42 $ | 98,53 $ | 148,79 $ |

## Prossimi step se SOL segue BTC 2022

| Step | Date SOL | BTC fine | SOL zona bassa | SOL zona alta | SOL fine base | Lettura |
| --- | --- | --- | --- | --- | --- | --- |
| Step 1 - prossime 2 settimane | 28 agosto 2026 -> 11 settembre 2026 | +8,14% | 106,34 $ (28 agosto 2026) | 121,18 $ (5 settembre 2026) | 114,99 $ | Spinta rialzista abbastanza pulita. |
| Step 2 - primo mese | 12 settembre 2026 -> 27 settembre 2026 | +13,58% | 98,53 $ (23 settembre 2026) | 120,78 $ (27 settembre 2026) | 120,78 $ | Prima retest / debolezza, poi recupero. |
| Step 3 - secondo mese | 28 settembre 2026 -> 27 ottobre 2026 | +39,52% | 118,97 $ (28 settembre 2026) | 148,37 $ (27 ottobre 2026) | 148,37 $ | Spinta rialzista abbastanza pulita. |
| Step 4 - terzo mese | 28 ottobre 2026 -> 26 novembre 2026 | +22,93% | 130,72 $ (26 novembre 2026) | 148,79 $ (28 ottobre 2026) | 130,72 $ | Spinta rialzista abbastanza pulita. |

Nota: le proiezioni restano condizionali; il prezzo non è aderente secondo le soglie canoniche.

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
| Prezzo SOL | 106,34 $ |  |
| Weekly RSI | 60,04 / linea grezza 52,71 | LINEA NON AFFIDABILE / RISCHIO NON ATTIVO — IRREALISTICA / NON OPERATIVA |
| Monthly RSI | 47,63 / linea grezza 55,81 | RSI TROPPO BASSO PER RISCHIO TOP — VALIDA / USO PRUDENTE |
| Target ciclo base | 608,87 $ | Avanzamento +17,47% |
| Rischio top-cycle RSI | BASSO | Nessun segnale top-cycle macro attivo. Prezzo ancora lontano dal target ciclo; il filtro RSI resta solo di monitoraggio. |

## Lettura semplice

- Weekly: La top-line weekly non supera i controlli di qualità. Non viene usata per generare rischio top-cycle.
- Monthly: RSI monthly è 47,6, sotto la soglia prudente 55. Anche se fosse vicino alla linea, non è una vera zona di esaurimento ciclo.
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
| Prezzo SOL | 106,34 $ |
| TVL Solana | 5,96 mld $ |
| TVL 7g | +11,73% |
| DEX volume 24h | 3,63 mld $ |
| Fees 24h | 16,24 mln $ |
| Stablecoin su Solana | 16,32 mld $ |
| Stake ratio | 69,02% |
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
| Confronto precedente | 2026-08-24 |
| Fonte prezzi | Yahoo Finance SOL-USD weekly |
| Prezzo SOL | 106,34 $ |
| EMA200 weekly target | 111,43 $ |
| Upside verso EMA200 | +4,59% |
| Distanza prezzo da EMA200 | -4,39% |
| Gap EMA50/EMA200 | -5,68% |
| Stato cross | EMA50 SOTTO EMA200 |
| RSI weekly | 60,13 |
| Età SOL | 6,4 anni |
| Analoghi storici usati | 30 |
| Max analoghi per asset | 3 |
| Hit EMA200 12w analoghi | +90,00% |
| Max gain mediano 12w | +24,21% |
| Drawdown mediano 12w | -37,81% |

Lettura semplice:

**SOLO OSSERVAZIONE**

Autocontrollo: **STABILE / DA CONFERMARE**.

Questo modulo confronta SOL con altre crypto in fasi simili di età, distanza da EMA200, EMA50/EMA200 e RSI. Non usa stock market.

Nota importante: **questo modulo ora NON pesa più nel Global Confluence**. Resta solo come contesto di ciclo e come mappa verso EMA200 weekly. Il punteggio Global resta guidato da prezzo, scanner, regime, struttura tecnica, frattale, RSI e conferme reali.

Nota: se EMA50/EMA200 sono dentro ±2%, il modulo parla di medie sovrapposte / incrocio in corso, perché exchange diversi possono mostrare il cross leggermente prima o dopo.

<!-- Generato: 2026-08-28 08:02 UTC -->
<!-- MAJOR_ALT_LIFECYCLE_SQUEEZE_END -->

</details>
<!-- COMPACT_SECTION_END:major_alt_lifecycle -->

# Report giornaliero BTC / SOL / DOGE

Aggiornato il: **2026-08-28 07:59:28 UTC**

Questo report confronta il grafico attuale di Bitcoin, Solana e Dogecoin con tanti grafici storici di altre crypto.

Non è una previsione certa. È uno scanner statistico: guarda situazioni simili già successe e mostra cosa accadde dopo nei 30 giorni successivi.

<!-- COMPACT_SECTION_START:daily_change -->
<details open>
<summary><strong>🗓️ Cambiamenti rispetto a ieri</strong></summary>

<!-- DAILY_CHANGE_START -->

---

# Mini report cambiamenti da ieri

Report separato completo: [daily_change_report.md](daily_change_report.md)

- BTC: cambiamento importante, ma lettura mista.
- SOL: cambiamento importante in miglioramento rispetto a ieri.
- DOGE: nessun cambiamento forte rispetto a ieri.

| Asset | Cambio | Tono | Verdetto oggi | Casi positivi oggi | Δ casi positivi |
| --- | --- | --- | --- | --- | --- |
| BTC | CAMBIAMENTO MEDIO | misto | RIALZISTA | +70.00% | 0.00 punti |
| SOL | CAMBIAMENTO FORTE | miglioramento | RIALZISTA | +70.00% | +7.50 punti |
| DOGE | NESSUN CAMBIAMENTO FORTE | misto | NEUTRALE / INCERTO | +37.50% | -2.50 punti |

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
| BTC | 75.695 $ | 87.647 $ | +61,11% | +15,79% | rimbalzo possibile | 87.647 $ | 75.695 $ | +14,29% | -13,64% | spike storicamente più resistente |
| SOL | 101,02 $ | 116,97 $ | +65,71% | +15,79% | buona zona storica di rimbalzo | 116,97 $ | 101,02 $ | +24,24% | -13,64% | spike storicamente più resistente |
| DOGE | 0,08314 $ | 0,09627 $ | +45,16% | +15,79% | rimbalzo debole | 0,09627 $ | 0,08314 $ | +51,72% | -13,64% | attenzione a prendere profitto |

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

- **BTC: su 40 casi simili, 36 prima sono scesi a -5,00%. Tra quei 36, 22 poi sono rimbalzati fino a +10,00%. Percentuale: +61,11% (22/36). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo possibile.**
- **BTC: su 40 casi simili, 28 prima sono saliti a +10,00%. Tra quei 28, 4 poi sono scaricati a -5,00%. Percentuale: +14,29% (4/28). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.**
- **SOL: su 40 casi simili, 35 prima sono scesi a -5,00%. Tra quei 35, 23 poi sono rimbalzati fino a +10,00%. Percentuale: +65,71% (23/35). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: buona zona storica di rimbalzo.**
- **SOL: su 40 casi simili, 33 prima sono saliti a +10,00%. Tra quei 33, 8 poi sono scaricati a -5,00%. Percentuale: +24,24% (8/33). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.**
- **DOGE: su 40 casi simili, 31 prima sono scesi a -5,00%. Tra quei 31, 14 poi sono rimbalzati fino a +10,00%. Percentuale: +45,16% (14/31). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.**
- **DOGE: su 40 casi simili, 29 prima sono saliti a +10,00%. Tra quei 29, 15 poi sono scaricati a -5,00%. Percentuale: +51,72% (15/29). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: attenzione a prendere profitto.**

<!-- BOUNCE_AFTER_DRAWDOWN_END -->

</details>
<!-- COMPACT_SECTION_END:bounce_after_drawdown -->

<!-- COMPACT_SECTION_START:scanner_forecast -->
<details>
<summary><strong>🔭 Cono probabilistico dello scanner</strong></summary>

<!-- SCANNER_FORECAST_TRACKER_START -->
# Scanner forecast path / cono probabilistico

Generato: 2026-08-28 08:01:22 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [scanner_forecast_tracker_report.md](scanner_forecast_tracker_report.md)

## Snapshot effettivamente usato

| Asset   | Snapshot prezzo   | Generazione snapshot prezzo   | Snapshot match scanner   |
|:--------|:------------------|:------------------------------|:-------------------------|
| BTC | 2026-08-28 | 2026-08-28T07:59:27Z | 2026-08-28 07:59:28 |
| SOL | 2026-08-28 | 2026-08-28T07:59:27Z | 2026-08-28 07:59:28 |
| DOGE | 2026-08-28 | 2026-08-28T07:59:27Z | 2026-08-28 07:59:28 |

La data di generazione del report non sostituisce la data degli input: se gli snapshot locali sono più vecchi, i valori restano riferiti agli snapshot indicati in tabella.

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
| BTC | 2026-08-28 | 79.679 $ | SALITA | 70,00% | 54.419,54 $ | 78.041,04 $ | 84.787,03 $ | 96.704,53 $ | 114.328,93 $ |
| SOL | 2026-08-28 | 106,34 $ | SALITA | 70,00% | 73,72 $ | 103,05 $ | 113,68 $ | 165,22 $ | 206,69 $ |
| DOGE | 2026-08-28 | 0.08752 $ | DISCESA | 37,50% | 0.05584 $ | 0.07535 $ | 0.08353 $ | 0.10546 $ | 0.12452 $ |

## Confronto raw / regime-adjusted

Il cono raw continua a usare i 40 casi dello scanner. Il cono regime-adjusted sceglie una sola coorte nella gerarchia SAME_BTC_AND_ASSET_REGIME → SAME_ASSET_REGIME → SAME_BTC_REGIME. Ogni livello richiede almeno 5 match; le coorti non vengono mai combinate e ogni fallback è dichiarato.

| Asset   | Stato adjusted              | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level        | selection_reason              | Raw p50 30g   | Adjusted p50 30g   | Raw p90 30g   | Adjusted p90 30g   |
|:--------|:----------------------------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:----------------------|:------------------------------|:--------------|:-------------------|:--------------|:-------------------|
| BTC | INSUFFICIENT_REGIME_MATCHES | NONE | 0 | 1 | 0 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES | 84.787,03 $ | n/a | 114.328,93 $ | n/a |
| SOL | INSUFFICIENT_REGIME_MATCHES | NONE | 0 | 2 | 0 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES | 113,68 $ | n/a | 206,69 $ | n/a |
| DOGE | AVAILABLE | SAME_ASSET_REGIME | 0 | 10 | 0 | 10 | 5 | 1_SAME_ASSET_FALLBACK | FALLBACK_TO_SAME_ASSET_REGIME | 0.08353 $ | 0.07921 $ | 0.12452 $ | 0.11622 $ |

## Grafici

### BTC

![Scanner forecast BTC](scanner_forecast_BTC.png)

#### Verifica storica e discrepanza

![Verifica storica cono BTC](scanner_forecast_history_BTC.png)

- Cono congelato il **2026-07-29**; verificato fino al **2026-08-28**; stato **COMPLETO 30/30g**.
- Reale **79.717,66 $**; p50 previsto **72.294,72 $**; scarto **10,27%**.
- Errore medio assoluto **4,78%**; massimo **13,78%**; DENTRO p10-p90; DENTRO p25-p75.

#### Cono regime-adjusted

Gruppo selezionato: **NONE**; fallback: **NONE**; motivo: **INSUFFICIENT_REGIME_MATCHES**.

Non disponibile: INSUFFICIENT_REGIME_MATCHES (campione selezionato 0/5 match).

### SOL

![Scanner forecast SOL](scanner_forecast_SOL.png)

#### Verifica storica e discrepanza

![Verifica storica cono SOL](scanner_forecast_history_SOL.png)

- Cono congelato il **2026-07-29**; verificato fino al **2026-08-28**; stato **COMPLETO 30/30g**.
- Reale **106,54 $**; p50 previsto **80,42 $**; scarto **32,49%**.
- Errore medio assoluto **7,72%**; massimo **36,99%**; DENTRO p10-p90; FUORI p25-p75.

#### Cono regime-adjusted

Gruppo selezionato: **NONE**; fallback: **NONE**; motivo: **INSUFFICIENT_REGIME_MATCHES**.

Non disponibile: INSUFFICIENT_REGIME_MATCHES (campione selezionato 0/5 match).

### DOGE

![Scanner forecast DOGE](scanner_forecast_DOGE.png)

#### Verifica storica e discrepanza

![Verifica storica cono DOGE](scanner_forecast_history_DOGE.png)

- Cono congelato il **2026-07-29**; verificato fino al **2026-08-28**; stato **COMPLETO 30/30g**.
- Reale **0.08759 $**; p50 previsto **0.07382 $**; scarto **18,66%**.
- Errore medio assoluto **9,16%**; massimo **36,28%**; DENTRO p10-p90; FUORI p25-p75.

#### Cono regime-adjusted

Gruppo selezionato: **SAME_ASSET_REGIME**; fallback: **1_SAME_ASSET_FALLBACK**; motivo: **FALLBACK_TO_SAME_ASSET_REGIME**.

**WARNING:** coorte fallback meno stringente rispetto a SAME_BTC_AND_ASSET_REGIME.

![Scanner forecast regime-adjusted DOGE](scanner_forecast_DOGE_regime_adjusted.png)

## Accuratezza percorso scanner

| Asset   | Giorno   |   Controlli | Dentro p10-p90   | Dentro p25-p75   | Errore medio abs vs p50   | Errore medio vs p50   |
|:--------|:---------|------------:|:-----------------|:-----------------|:--------------------------|:----------------------|
| BTC | 1g | 47 | 93,62% | 61,70% | 2,24% | 0,82% |
| BTC | 3g | 45 | 88,89% | 73,33% | 3,39% | 1,17% |
| BTC | 7g | 41 | 90,24% | 70,73% | 5,63% | 3,01% |
| BTC | 14g | 34 | 97,06% | 70,59% | 5,51% | 2,69% |
| BTC | 30g | 20 | 100,00% | 95,00% | 8,06% | 1,46% |
| SOL | 1g | 47 | 72,34% | 55,32% | 3,13% | 1,39% |
| SOL | 3g | 45 | 86,67% | 66,67% | 4,39% | 1,98% |
| SOL | 7g | 41 | 82,93% | 73,17% | 5,82% | 3,99% |
| SOL | 14g | 34 | 88,24% | 70,59% | 6,98% | 5,89% |
| SOL | 30g | 20 | 90,00% | 55,00% | 12,93% | 12,28% |
| DOGE | 1g | 47 | 85,11% | 59,57% | 3,43% | 1,10% |
| DOGE | 3g | 45 | 88,89% | 71,11% | 4,64% | 2,55% |
| DOGE | 7g | 41 | 78,05% | 75,61% | 9,44% | 7,93% |
| DOGE | 14g | 34 | 79,41% | 55,88% | 11,25% | 10,06% |
| DOGE | 30g | 20 | 90,00% | 35,00% | 18,34% | 18,34% |

## Tail / outlier audit

I casi di coda restano nel calcolo. L'audit leave-one-out quantifica la sensibilità dei percentili senza trasformare l'analisi in un filtro discrezionale.

Dettaglio completo: [scanner_forecast_tail_outlier_audit.md](scanner_forecast_tail_outlier_audit.md).

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

Righe salvate nello storico: **135**.

Questa sezione tiene un diario delle previsioni giornaliere a 30 giorni, senza appesantire il report principale.

| Data | Asset | Prezzo | Direzione | Casi positivi | Return p50 | Drawdown p50 | Max gain p50 | Controllo 30g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08-28 | BTC | 79.679 $ | SALITA | 70,00% | 84.787 $ | 71.011 $ | 91.126 $ | 2026-09-27 |
| 2026-08-28 | DOGE | 0,09000 $ | DISCESA | 37,50% | 0,08000 $ | 0,08000 $ | 0,10000 $ | 2026-09-27 |
| 2026-08-28 | SOL | 106,34 $ | SALITA | 70,00% | 113,68 $ | 91,86 $ | 129,61 $ | 2026-09-27 |

<!-- FORECAST_30D_HISTORY_END -->

</details>
<!-- COMPACT_SECTION_END:scanner_forecast -->

<!-- COMPACT_SECTION_START:extreme_cases -->
<details>
<summary><strong>⚠️ Percorso dei casi estremi</strong></summary>

<!-- EXTREME_CASES_PATH_START -->
# Extreme cases path report

Generato: 2026-08-28 08:01 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [extreme_cases_path_report.md](extreme_cases_path_report.md)

Questo report si attiva quando i casi positivi o negativi sono almeno **80%**.

Ora misura anche il **rialzo massimo prima della discesa principale**, quindi distingue uno spike iniziale da una discesa quasi immediata.

## Trigger estremi

| Asset   | Direzione   | Trigger   | Percentuale   | Motivo                           |   Match disponibili |
|:--------|:------------|:----------|:--------------|:---------------------------------|--------------------:|
| BTC     | NESSUNO     | NO        | +70,00%       | Nessun lato sopra soglia estrema |                  40 |
| SOL     | NESSUNO     | NO        | +70,00%       | Nessun lato sopra soglia estrema |                  40 |
| DOGE    | NESSUNO     | NO        | +62,50%       | Nessun lato sopra soglia estrema |                  40 |

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
- Prezzo attuale: **79.679,38 $**
- Return normale fra 30 giorni: **84.787,03 $** (6,41%)
- Drawdown normale durante il mese: **71.010,69 $** (-10,88%)
- Drawdown brutto da rispettare: **67.214,25 $** (-15,64%)
- Max gain normale durante il mese: **91.125,58 $** (14,37%)
- Max gain buono / take profit ottimistico: **105.016,93 $** (31,80%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Solana
- Direzione più probabile a 30 giorni: **SALITA**
- Casi positivi / salita storica: **70,00%**
- Casi negativi / discesa storica: **30,00%**
- Quanto è netto il segnale: **forte**
- Prezzo attuale: **106,34 $**
- Return normale fra 30 giorni: **113,68 $** (6,90%)
- Drawdown normale durante il mese: **91,86 $** (-13,61%)
- Drawdown brutto da rispettare: **85,67 $** (-19,44%)
- Max gain normale durante il mese: **129,61 $** (21,89%)
- Max gain buono / take profit ottimistico: **172,32 $** (62,05%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Dogecoin
- Direzione più probabile a 30 giorni: **DISCESA**
- Casi positivi / salita storica: **37,50%**
- Casi negativi / discesa storica: **62,50%**
- Quanto è netto il segnale: **medio**
- Prezzo attuale: **0,09 $**
- Return normale fra 30 giorni: **0,08 $** (-4,56%)
- Drawdown normale durante il mese: **0,08 $** (-11,97%)
- Drawdown brutto da rispettare: **0,07 $** (-19,60%)
- Max gain normale durante il mese: **0,10 $** (17,69%)
- Max gain buono / take profit ottimistico: **0,11 $** (24,96%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Messaggio del giorno

Il quadro generale oggi è più favorevole. Lo scanner vede più possibilità di salita su più asset.

---

# Mappa semplice asset per asset

# Bitcoin — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟢 VERDE / Favorevole
**Prezzo attuale:** 79.679,38 $

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

- Se va molto male: **54.419,54 $** (-31,70%)
- Se va male: **78.041,04 $** (-2,06%)
- Scenario normale: **84.787,03 $** (6,41%)
- Se va bene: **96.704,53 $** (21,37%)
- Se va molto bene: **114.328,93 $** (43,49%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **71.010,69 $** (-10,88%)
- Discesa brutta: **67.214,25 $** (-15,64%)
- Discesa molto brutta: **52.511,79 $** (-34,10%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **91.125,58 $** (14,37%)
- Rialzo buono: **105.016,93 $** (31,80%)
- Rialzo molto forte: **123.317,37 $** (54,77%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Bitcoin tendeva a muoversi tra una zona bassa intorno a **71.010,69 $** e uno spike normale intorno a **91.125,58 $**.

La chiusura a 30 giorni era più spesso positiva: salita 70,00%, discesa 30,00%. Quindi la lettura principale è favorevole.

Nota leva BTC: se la liquidazione è vicina a 51.000 $, guarda soprattutto la discesa brutta e molto brutta. Il prezzo può recuperare dopo, ma la leva può saltare prima.

---

# Solana — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟢 VERDE / Favorevole
**Prezzo attuale:** 106,34 $

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

- Se va molto male: **73,72 $** (-30,68%)
- Se va male: **103,05 $** (-3,10%)
- Scenario normale: **113,68 $** (6,90%)
- Se va bene: **165,22 $** (55,37%)
- Se va molto bene: **206,69 $** (94,36%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **91,86 $** (-13,61%)
- Discesa brutta: **85,67 $** (-19,44%)
- Discesa molto brutta: **72,73 $** (-31,60%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **129,61 $** (21,89%)
- Rialzo buono: **172,32 $** (62,05%)
- Rialzo molto forte: **247,49 $** (132,74%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Solana tendeva a muoversi tra una zona bassa intorno a **91,86 $** e uno spike normale intorno a **129,61 $**.

La chiusura a 30 giorni era più spesso positiva: salita 70,00%, discesa 30,00%. Quindi la lettura principale è favorevole.

---

# Dogecoin — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟡 GIALLO / Incerto
**Prezzo attuale:** 0,09 $

**Direzione più probabile a 30 giorni:** **DISCESA**
- Probabilità storica di salita: **37,50%**
- Probabilità storica di discesa: **62,50%**
- Quanto è netto il segnale: **medio**

## Come leggere questa parte

- **Probabilità storica di salita** = su 40 casi simili, quanti hanno chiuso sopra dopo 30 giorni.
- **Probabilità storica di discesa** = su 40 casi simili, quanti hanno chiuso sotto dopo 30 giorni.
- **Quanto è netto il segnale** = quanto è grande la differenza tra salita e discesa. Non vuol dire certezza, vuol dire solo che il risultato storico non è vicino al 50/50.

La lettura principale è ribassista, con segnale medio. Nei casi storici simili, il prezzo ha chiuso sotto dopo 30 giorni più spesso di quanto abbia chiuso sopra.

## 1. Return 30d — prezzo fra 30 giorni

**Return** significa rendimento finale. Qui guardiamo dove potrebbe stare il prezzo **alla fine dei 30 giorni**, non durante il percorso.

- Se va molto male: **0,06 $** (-36,20%)
- Se va male: **0,08 $** (-13,90%)
- Scenario normale: **0,08 $** (-4,56%)
- Se va bene: **0,11 $** (20,50%)
- Se va molto bene: **0,12 $** (42,28%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **0,08 $** (-11,97%)
- Discesa brutta: **0,07 $** (-19,60%)
- Discesa molto brutta: **0,06 $** (-36,82%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **0,10 $** (17,69%)
- Rialzo buono: **0,11 $** (24,96%)
- Rialzo molto forte: **0,15 $** (66,06%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Dogecoin tendeva a muoversi tra una zona bassa intorno a **0,08 $** e uno spike normale intorno a **0,10 $**.

La chiusura a 30 giorni era più spesso negativa: salita 37,50%, discesa 62,50%. Quindi la lettura principale è prudente/debole.

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

- Previsioni già controllate: **27**
- Direzione corretta: **85,00%**
- Errore medio dello scenario centrale: **6,28%**
- Zona rischio toccata: **0,00%**
- Zona rialzo media toccata: **3,70%**
- Prezzo finale dentro lo scenario 10%-90%: **100,00%**

### Dogecoin

- Previsioni già controllate: **27**
- Direzione corretta: **91,67%**
- Errore medio dello scenario centrale: **15,32%**
- Zona rischio toccata: **0,00%**
- Zona rialzo media toccata: **25,93%**
- Prezzo finale dentro lo scenario 10%-90%: **92,59%**

### Solana

- Previsioni già controllate: **27**
- Direzione corretta: **100,00%**
- Errore medio dello scenario centrale: **9,76%**
- Zona rischio toccata: **7,41%**
- Zona rialzo media toccata: **29,63%**
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

Dati ancora insufficienti: previsioni controllate **27** su **30** necessarie.

Per ora si usa solo lo scanner storico grezzo. Quando ci saranno abbastanza previsioni controllate, qui apparirà la lettura autocalibrata.

## Solana

Dati ancora insufficienti: previsioni controllate **27** su **30** necessarie.

Per ora si usa solo lo scanner storico grezzo. Quando ci saranno abbastanza previsioni controllate, qui apparirà la lettura autocalibrata.

## Dogecoin

Dati ancora insufficienti: previsioni controllate **27** su **30** necessarie.

Per ora si usa solo lo scanner storico grezzo. Quando ci saranno abbastanza previsioni controllate, qui apparirà la lettura autocalibrata.

---

# Approfondimento tecnico — Bitcoin (BTC-USD)

## Semaforo: 🟢 VERDE / Favorevole

**Prezzo attuale:** 79.679,38 $

Bitcoin ha un segnale favorevole. La statistica dei casi simili indica più possibilità di salita che di discesa, ma resta comunque una probabilità, non una certezza.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **70,00%**
- Casi negativi dopo 30 giorni: **30,00%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **80,98%**
- Rendimento medio dopo 30 giorni: **9,43%**
- Rendimento centrale dopo 30 giorni: **6,41%**
- Discesa media durante i 30 giorni: **-14,88%**
- Massimo rialzo medio durante i 30 giorni: **23,81%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **87.189,71 $**
- Scenario centrale a 30 giorni: **84.787,03 $**
- Zona di rischio media: **67.820,48 $**
- Zona di rialzo media: **98.654,06 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -31,70% → **54.419,54 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -2,06% → **78.041,04 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: 6,41% → **84.787,03 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 21,37% → **96.704,53 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 43,49% → **114.328,93 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -34,10% → **52.511,79 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -15,64% → **67.214,25 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -10,88% → **71.010,69 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -7,04% → **74.072,98 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: -4,97% → **75.716,74 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 1,51% → **80.879,01 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 9,66% → **87.377,05 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 14,37% → **91.125,58 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 31,80% → **105.016,93 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 54,77% → **123.317,37 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| XRP-USD         | 2023-08-04   | 2023-11-11 |        87.78 |        -6.42 |         -12.41 |           1.57 |
| BNB-USD         | 2018-11-08   | 2019-02-15 |        86.31 |        69.95 |          -1.56 |          73.81 |
| THETA-USD       | 2018-11-07   | 2019-02-14 |        85.34 |        40.04 |          -6.28 |          99.12 |
| EOS-USD         | 2023-08-04   | 2023-11-11 |        84.01 |         6.08 |         -10.34 |          18.01 |
| XTZ-USD         | 2023-08-04   | 2023-11-11 |        84.01 |        -4.35 |         -15.64 |           6.79 |
| THETA-USD       | 2023-08-03   | 2023-11-10 |        83.85 |        10.1  |         -16.48 |          12.22 |
| ETC-USD         | 2023-08-04   | 2023-11-11 |        83.61 |         0.53 |          -9.42 |          11.06 |
| XLM-USD         | 2020-08-24   | 2020-12-01 |        82.68 |       -30.39 |         -31.42 |           3.78 |
| FIL-USD         | 2023-08-03   | 2023-11-10 |        82.55 |        12.12 |          -7.98 |          13.89 |
| RUNE-USD        | 2026-01-21   | 2026-04-30 |        82.49 |       -14.37 |         -15.64 |          26.12 |

---

# Approfondimento tecnico — Solana (SOL-USD)

## Semaforo: 🟢 VERDE / Favorevole

**Prezzo attuale:** 106,34 $

Solana ha un segnale favorevole. La statistica dei casi simili indica più possibilità di salita che di discesa, ma resta comunque una probabilità, non una certezza.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **70,00%**
- Casi negativi dopo 30 giorni: **30,00%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **76,40%**
- Rendimento medio dopo 30 giorni: **53,09%**
- Rendimento centrale dopo 30 giorni: **6,90%**
- Discesa media durante i 30 giorni: **-17,18%**
- Massimo rialzo medio durante i 30 giorni: **71,66%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **162,79 $**
- Scenario centrale a 30 giorni: **113,68 $**
- Zona di rischio media: **88,07 $**
- Zona di rialzo media: **182,54 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -30,68% → **73,72 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -3,10% → **103,05 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: 6,90% → **113,68 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 55,37% → **165,22 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 94,36% → **206,69 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -31,60% → **72,73 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -19,44% → **85,67 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -13,61% → **91,86 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -9,79% → **95,93 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: -3,97% → **102,12 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 0,96% → **107,36 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 13,26% → **120,44 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 21,89% → **129,61 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 62,05% → **172,32 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 132,74% → **247,49 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| ZIL-USD         | 2020-08-21   | 2020-11-28 |        82.61 |       235.51 |           0    |         235.51 |
| VET-USD         | 2020-02-28   | 2020-06-06 |        82.45 |        98.37 |          -0.47 |          98.37 |
| NEO-USD         | 2023-08-04   | 2023-11-11 |        80.18 |        -8.87 |         -21.33 |           0.65 |
| BNB-USD         | 2018-11-08   | 2019-02-15 |        79.77 |        69.95 |          -1.56 |          73.81 |
| FTM-USD         | 2020-10-18   | 2021-01-25 |        79.24 |      1143.11 |           0    |        1143.11 |
| ADA-USD         | 2020-08-24   | 2020-12-01 |        79.05 |        16.29 |         -12.56 |          23.2  |
| EOS-USD         | 2018-11-18   | 2019-02-25 |        79    |        20.31 |          -8.74 |          20.31 |
| VET-USD         | 2023-08-01   | 2023-11-08 |        78.76 |        18.75 |         -14.56 |          18.75 |
| 1INCH-USD       | 2023-08-06   | 2023-11-13 |        78.68 |         4.53 |          -9.19 |          14.73 |
| WAVES-USD       | 2023-08-04   | 2023-11-11 |        78.58 |         2.14 |         -12.76 |          13.61 |

---

# Approfondimento tecnico — Dogecoin (DOGE-USD)

## Semaforo: 🟡 GIALLO / Incerto

**Prezzo attuale:** 0,09 $

Dogecoin è in una situazione incerta. Lo scanner non vede un vantaggio chiaro né per la salita né per la discesa. In questi casi è meglio non forzare la previsione.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **37,50%**
- Casi negativi dopo 30 giorni: **62,50%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **83,10%**
- Rendimento medio dopo 30 giorni: **6,19%**
- Rendimento centrale dopo 30 giorni: **-4,56%**
- Discesa media durante i 30 giorni: **-14,65%**
- Massimo rialzo medio durante i 30 giorni: **29,84%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **0,09 $**
- Scenario centrale a 30 giorni: **0,08 $**
- Zona di rischio media: **0,07 $**
- Zona di rialzo media: **0,11 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -36,20% → **0,06 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -13,90% → **0,08 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: -4,56% → **0,08 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 20,50% → **0,11 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 42,28% → **0,12 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -36,82% → **0,06 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -19,60% → **0,07 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -11,97% → **0,08 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -6,35% → **0,08 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: -1,46% → **0,09 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 1,83% → **0,09 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 9,69% → **0,10 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 17,69% → **0,10 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 24,96% → **0,11 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 66,06% → **0,15 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| MANA-USD        | 2025-01-20   | 2025-04-29 |        87.55 |        -5.09 |          -5.62 |          24.61 |
| FIL-USD         | 2022-04-30   | 2022-08-07 |        87.32 |       -36.15 |         -36.15 |           0    |
| IOTA-USD        | 2025-01-21   | 2025-04-30 |        85.48 |       -13.86 |         -13.86 |          24.14 |
| INJ-USD         | 2021-05-08   | 2021-08-15 |        85.33 |        20.12 |          -3    |          65.27 |
| VET-USD         | 2025-01-22   | 2025-05-01 |        85.23 |       -11.12 |         -12.03 |          18.71 |
| QTUM-USD        | 2022-04-26   | 2022-08-03 |        84.83 |       -20.03 |         -23.75 |           9.37 |
| BTC-USD         | 2025-01-22   | 2025-05-01 |        84.73 |         8.44 |          -2.26 |          15.73 |
| AVAX-USD        | 2021-05-07   | 2021-08-14 |        84.46 |       193.95 |           0    |         227.99 |
| MATIC-USD       | 2022-04-16   | 2022-07-24 |        84.34 |        -5.61 |         -12.38 |          16.29 |
| SAND-USD        | 2025-01-19   | 2025-04-28 |        83.97 |         2.06 |          -9.85 |          22.79 |

</details>
<!-- COMPACT_SECTION_END:scanner_full_detail -->

<!-- COMPACT_SECTION_START:market_regime -->
<details>
<summary><strong>🌦️ Market Regime Match</strong></summary>

<!-- MARKET_REGIME_MATCH_START -->
# Market Regime Match Report


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [market_regime_match_report.md](market_regime_match_report.md)

Generated: 2026-08-28 08:01 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | snapshot_date   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | 2026-08-28 | MIXED | 79.679 $ | True | 8.03% | -8.26% | MIXED | 8.03% | -8.26% |
| DOGE-USD | 2026-08-28 | BEAR | 0.08752 $ | False | -12.82% | -14.95% | MIXED | 8.03% | -8.26% |
| SOL-USD | 2026-08-28 | RECOVERY | 106,34 $ | True | 28.82% | -13.98% | MIXED | 8.03% | -8.26% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 70.00% | 6.41% | 21.37% | 43.49% | -10.88% | -34.10% | 14.37% | 31.80% | 54.77% | 67.50% | 13.91% | 27.48% | 81.19% |
| BTC-USD | SAME_BTC_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| BTC-USD | SAME_ASSET_REGIME | 1 | 0.00% | -1.72% | -1.72% | -1.72% | -7.24% | -7.24% | 44.52% | 44.52% | 44.52% | 100.00% | 22.36% | 22.36% | 22.36% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| DOGE-USD | ALL_MATCHES | 40 | 37.50% | -4.56% | 20.50% | 42.28% | -11.97% | -36.82% | 17.69% | 24.96% | 66.06% | 35.00% | -11.10% | 13.36% | 71.11% |
| DOGE-USD | SAME_BTC_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| DOGE-USD | SAME_ASSET_REGIME | 10 | 30.00% | -9.50% | 15.72% | 32.79% | -16.95% | -36.20% | 11.83% | 20.30% | 49.40% | 20.00% | -20.25% | -4.59% | 55.95% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL-USD | ALL_MATCHES | 40 | 70.00% | 6.90% | 55.37% | 94.36% | -13.61% | -31.60% | 21.89% | 62.05% | 132.74% | 62.50% | 27.76% | 66.31% | 136.46% |
| SOL-USD | SAME_BTC_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL-USD | SAME_ASSET_REGIME | 2 | 100.00% | 3.29% | 3.86% | 4.21% | -14.92% | -16.64% | 17.09% | 18.84% | 19.88% | 100.00% | 32.90% | 41.60% | 46.81% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 6 | 33.33% | -28.92% | -29.56% | 30.70% | 33.33% | -28.01% | 80.87% |
| BTC-USD | HISTORICAL_BTC_BULL | 25 | 72.00% | 4.16% | -10.34% | 18.01% | 76.00% | 14.56% | 62.02% |
| BTC-USD | HISTORICAL_BTC_DISTRIBUTION | 7 | 100.00% | 18.89% | -13.32% | 34.87% | 57.14% | 13.26% | 57.26% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 2 | 50.00% | 34.12% | -4.40% | 66.49% | 100.00% | 68.08% | 96.48% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 5 | 20.00% | -5.61% | -14.75% | 16.29% | 20.00% | -15.42% | 16.29% |
| DOGE-USD | HISTORICAL_BTC_BULL | 32 | 40.62% | -2.86% | -9.33% | 24.96% | 40.62% | -5.74% | 48.12% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 3 | 33.33% | -14.50% | -21.51% | 35.23% | 0.00% | -25.07% | 35.23% |
| SOL-USD | HISTORICAL_BTC_BEAR | 9 | 33.33% | -12.67% | -19.42% | 31.22% | 33.33% | -21.82% | 62.62% |
| SOL-USD | HISTORICAL_BTC_BULL | 27 | 77.78% | 9.27% | -12.76% | 70.85% | 70.37% | 29.02% | 131.82% |
| SOL-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 100.00% | 10.10% | -16.48% | 12.22% | 0.00% | -1.95% | 36.95% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 3 | 100.00% | 69.95% | -1.56% | 86.09% | 100.00% | 113.80% | 144.29% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 29 | 72.41% | 6.74% | -11.06% | 31.66% | 58.62% | 3.84% | 65.84% |
| BTC-USD | HISTORICAL_ASSET_BULL | 5 | 60.00% | 14.13% | -5.26% | 23.88% | 80.00% | 76.15% | 174.70% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 100.00% | 23.22% | -19.34% | 32.28% | 100.00% | 22.03% | 35.00% |
| BTC-USD | HISTORICAL_ASSET_MIXED | 1 | 0.00% | -1.72% | -7.24% | 44.52% | 100.00% | 22.36% | 44.52% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 3 | 66.67% | 2.14% | -12.76% | 11.63% | 100.00% | 15.52% | 40.62% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 10 | 30.00% | -9.50% | -16.95% | 20.30% | 20.00% | -20.25% | 46.69% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 26 | 42.31% | -1.63% | -9.33% | 30.14% | 42.31% | -4.91% | 59.55% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 4 | 25.00% | -27.04% | -31.63% | 9.96% | 25.00% | -29.88% | 13.46% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 26 | 65.38% | 3.94% | -14.26% | 31.08% | 53.85% | 8.77% | 66.62% |
| SOL-USD | HISTORICAL_ASSET_BULL | 11 | 72.73% | 83.57% | -12.56% | 156.86% | 72.73% | 63.03% | 163.21% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 100.00% | 98.37% | -0.47% | 98.37% | 100.00% | 158.76% | 174.79% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 2 | 100.00% | 3.29% | -14.92% | 18.84% | 100.00% | 32.90% | 46.92% |

## Top regime-adjusted matches

A single cohort is selected deterministically: SAME_BTC_AND_ASSET_REGIME, otherwise SAME_ASSET_REGIME, otherwise SAME_BTC_REGIME. Each level must have at least 5 matches; cohorts are never combined.

| target   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level        | selection_reason              |
|:---------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:----------------------|:------------------------------|
| BTC-USD | NONE | 0 | 1 | 0 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES |
| DOGE-USD | SAME_ASSET_REGIME | 0 | 10 | 0 | 10 | 5 | 1_SAME_ASSET_FALLBACK | FALLBACK_TO_SAME_ASSET_REGIME |
| SOL-USD | NONE | 0 | 2 | 0 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES |

- WARNING DOGE-USD: SAME_ASSET_REGIME is a less stringent fallback than SAME_BTC_AND_ASSET_REGIME.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| DOGE-USD | FIL-USD | 2022-04-30 | 87.32% | BEAR | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -36.15% | -36.15% | 0.00% | -37.52% | -40.20% | 0.00% |
| DOGE-USD | MATIC-USD | 2022-04-16 | 84.34% | BEAR | BEAR | SAME_ASSET_ONLY | MIXED | -5.61% | -12.38% | 16.29% | -14.57% | -20.09% | 16.29% |
| DOGE-USD | YFI-USD | 2022-04-25 | 83.28% | RECOVERY | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -14.50% | -21.51% | 13.63% | -25.07% | -25.52% | 13.63% |
| DOGE-USD | DOT-USD | 2023-07-30 | 83.15% | BULL | BEAR | SAME_ASSET_ONLY | HIGH_SPIKE_60D | 21.64% | -1.59% | 21.64% | 49.86% | -1.59% | 85.75% |
| DOGE-USD | NEAR-USD | 2022-05-06 | 82.80% | BEAR | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -13.38% | -36.06% | 0.00% | -46.25% | -46.25% | 0.00% |
| DOGE-USD | EGLD-USD | 2023-07-25 | 82.80% | BULL | BEAR | SAME_ASSET_ONLY | EXPLOSIVE_60D | 40.51% | 0.00% | 48.58% | 110.79% | 0.00% | 126.47% |
| DOGE-USD | EOS-USD | 2022-04-26 | 82.48% | RECOVERY | BEAR | SAME_ASSET_ONLY | BULLISH_30D | 31.93% | 0.00% | 56.82% | -1.27% | -2.15% | 56.82% |
| DOGE-USD | EOS-USD | 2021-12-22 | 81.99% | BULL | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -28.56% | -28.56% | 2.40% | -50.86% | -57.12% | 2.40% |
| DOGE-USD | KSM-USD | 2021-12-25 | 81.37% | BULL | BEAR | SAME_ASSET_ONLY | BEARISH_30D | -36.71% | -36.71% | 0.00% | -63.53% | -67.03% | 0.00% |
| DOGE-USD | MANA-USD | 2022-10-13 | 81.27% | BEAR | BEAR | SAME_ASSET_ONLY | MIXED | -2.01% | -12.01% | 10.03% | -15.42% | -29.42% | 10.03% |

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

Generato: 2026-08-28 08:01 UTC


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
| BTC | 79.679 $ | +6 | COSTRUTTIVO / CONFERMA PARZIALE | STAGE 3 / DISTRIBUZIONE O PAUSA | MASSIMI E MINIMI CRESCENTI | SIGN OF STRENGTH POSSIBILE | MEDIO | SPOT OK / LONG SOLO PRUDENTE SU CONFERMA |
| SOL | 106,34 $ | +9 | CONFERMATO RIALZISTA | STAGE 3 / DISTRIBUZIONE O PAUSA | MASSIMI E MINIMI CRESCENTI | SIGN OF STRENGTH POSSIBILE | MEDIO | TRANCHE PICCOLE / NO LEVA FINCHÉ NON ROMPE CONFERME |
| DOGE | 0.08752 $ | 0 | NEUTRALE / MISTO | STAGE 4 / MARKDOWN | MASSIMI E MINIMI CRESCENTI | ACCUMULO POSSIBILE / RANGE BASSO | MEDIO | STAI ALLA FINESTRA |

## Punteggi per area

| Asset | Trend | Struttura | Momentum | Volume | Prezzo | Candela | Wyckoff | Totale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +1 | +2 | -1 | +2 | 0 | 0 | +2 | +6 |
| SOL | +1 | +2 | 0 | +1 | +3 | 0 | +2 | +9 |
| DOGE | -3 | +2 | 0 | +1 | 0 | 0 | 0 | 0 |

## Livelli tecnici

| Asset | Supporto | Resistenza | Breakout 60g | Breakdown 60g | ATR14 | Rendimento 30g | Rendimento 90g |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 79.206 $ | 81.235 $ | 81.235 $ | 57.748 $ | 3,35% | 24,70% | 8,05% |
| SOL | 83,52 $ | 110,04 $ | 102,59 $ | 64,42 $ | 4,99% | 44,76% | 29,07% |
| DOGE | 0.08189 $ | 0.09169 $ | 0.09998 $ | 0.06797 $ | 5,91% | 25,00% | -12,75% |

## Lettura dettagliata

### BTC

- Prezzo: **79.679 $**
- Score classico: **+6 / 12**
- Verdetto: **COSTRUTTIVO / CONFERMA PARZIALE**
- Azione coerente: **SPOT OK / LONG SOLO PRUDENTE SU CONFERMA**
- Volatilità tecnica locale: **MEDIO** — ATR14 3,35%; distanza supporto 0,61%; distanza resistenza 1,94%

Dettaglio:

- Trend: **+1** — prezzo sopra MA200 daily; breve termine sopra MA20/MA50; MA50 daily in salita; MA200 daily in discesa; STAGE 3 / DISTRIBUZIONE O PAUSA
- Stage weekly: **STAGE 3 / DISTRIBUZIONE O PAUSA** — Prezzo sopra MA30 weekly ma pendenza debole o piatta.
- Struttura: **+2** — MASSIMI E MINIMI CRESCENTI
- Momentum: **-1** — RSI alto 79.3; MACD sopra signal; istogramma MACD in peggioramento
- Volume: **+2** — OBV sopra media; CMF positivo 0.17; volume ratio 1.23
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **+2** — SIGN OF STRENGTH POSSIBILE. Prezzo nella parte alta del range con flusso volume positivo.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 79.34 |
| MACD histogram | 1113.34070 |
| CMF20 | 0.171 |
| Volume ratio 20 | 1.23 |
| MA20 | 70.455 $ |
| MA50 | 66.759 $ |
| MA100 | 66.198 $ |
| MA200 | 69.272 $ |
| Pendenza MA50 20g | +5,46% |
| Pendenza MA200 60g | -8,26% |
| Bollinger width | 36,78% |
| Bollinger position | 0.82 |

### SOL

- Prezzo: **106,34 $**
- Score classico: **+9 / 12**
- Verdetto: **CONFERMATO RIALZISTA**
- Azione coerente: **TRANCHE PICCOLE / NO LEVA FINCHÉ NON ROMPE CONFERME**
- Volatilità tecnica locale: **MEDIO** — ATR14 4,99%; distanza supporto 27,57%; distanza resistenza 3,28%

Dettaglio:

- Trend: **+1** — prezzo sopra MA200 daily; breve termine sopra MA20/MA50; MA50 daily in salita; MA200 daily in discesa; STAGE 3 / DISTRIBUZIONE O PAUSA
- Stage weekly: **STAGE 3 / DISTRIBUZIONE O PAUSA** — Prezzo sopra MA30 weekly ma pendenza debole o piatta.
- Struttura: **+2** — MASSIMI E MINIMI CRESCENTI
- Momentum: **0** — RSI alto 80.1; RSI in peggioramento; MACD sopra signal; istogramma MACD in miglioramento
- Volume: **+1** — OBV sopra media; CMF positivo 0.22; discesa con volume sopra media
- Conferma prezzo: **+3** — Breakout sopra resistenza 60g con volume.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **+2** — SIGN OF STRENGTH POSSIBILE. Prezzo nella parte alta del range con flusso volume positivo.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 80.14 |
| MACD histogram | 2.57135 |
| CMF20 | 0.217 |
| Volume ratio 20 | 1.88 |
| MA20 | 86,36 $ |
| MA50 | 79,66 $ |
| MA100 | 77,26 $ |
| MA200 | 81,58 $ |
| Pendenza MA50 20g | +5,87% |
| Pendenza MA200 60g | -13,98% |
| Bollinger width | 45,12% |
| Bollinger position | 0.92 |

### DOGE

- Prezzo: **0.08752 $**
- Score classico: **0 / 12**
- Verdetto: **NEUTRALE / MISTO**
- Azione coerente: **STAI ALLA FINESTRA**
- Volatilità tecnica locale: **MEDIO** — ATR14 5,91%; distanza supporto 6,96%; distanza resistenza 4,69%

Dettaglio:

- Trend: **-3** — prezzo sotto MA200 daily; breve termine sopra MA20/MA50; MA200 daily in discesa; STAGE 4 / MARKDOWN
- Stage weekly: **STAGE 4 / MARKDOWN** — Prezzo sotto MA30 weekly con MA30 in discesa.
- Struttura: **+2** — MASSIMI E MINIMI CRESCENTI
- Momentum: **0** — RSI sano 64.6; RSI in peggioramento; MACD sopra signal; istogramma MACD in peggioramento
- Volume: **+1** — OBV sopra media; CMF neutrale 0.04; volume ratio 1.03
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **0** — ACCUMULO POSSIBILE / RANGE BASSO. Prezzo nella metà bassa del range, ma senza spring confermato.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 64.64 |
| MACD histogram | 0.00113 |
| CMF20 | 0.044 |
| Volume ratio 20 | 1.03 |
| MA20 | 0.07863 $ |
| MA50 | 0.07429 $ |
| MA100 | 0.08005 $ |
| MA200 | 0.08905 $ |
| Pendenza MA50 20g | +1,40% |
| Pendenza MA200 60g | -14,95% |
| Bollinger width | 44,22% |
| Bollinger position | 0.73 |

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

Generato: 2026-08-28 08:02 UTC


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
| BTC | 79.679 $ | Doppio massimo | CANDIDATO | ribassista | n/a | 49.952 $ | n/a | 37,98% | Fib 78,6% TESTATO (0) @ 78.447 $ | NEL RANGE | 74.959 $ |
| SOL | 106,34 $ | Doppio massimo | CANDIDATO | ribassista | n/a | 51,22 $ | n/a | 65,08% | Fib 78,6% RECUPERATO (0) @ 93,12 $ | BREAKOUT 60G | 83,52 $ |
| DOGE | 0.08752 $ | Doppio massimo | CANDIDATO | ribassista | n/a | 0.06214 $ | n/a | 28,76% | Fib 38,2% TESTATO (0) @ 0.08775 $ | NEL RANGE | 0.08744 $ |

## BTC

![Classic visual BTC](classic_visual_BTC.png)

- Pattern principale: **Doppio massimo**
- Stato pattern: **CANDIDATO** (0)
- Famiglia: **ribassista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-06-22 -> 2026-08-09**
- Età formazione: **19 giorni**
- Breakout pattern: **n/a**
- Età breakout: **n/a**
- Neckline: **57.748 $**
- Target teorico: **49.952 $**
- Progresso verso target: **n/a**
- Distanza dalla neckline: **37,98%**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 78,6% TESTATO (0) @ 78.447 $** — Swing DOWN 2026-05-06 82.792 -> 2026-08-14 62.488; livello più vicino 78.6% a 78.447; stato TESTATO; confluenza: nessuna confluenza indipendente.
- Invalidazione: **58.903 $**
- Relazione prezzo/neckline: **sopra neckline**
- Dettaglio: Due massimi simili vicino a 65.544 tra 2026-06-22 e 2026-08-09. Neckline ribassista stimata: 57.748. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 19 giorni. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **NEL RANGE**
- Supporto: **74.959 $**
- Resistenza: **82.792 $**
- Breakout 60g: **81.235 $**
- Breakdown 60g: **57.748 $**
- RSI14: **79.27**
- ATR14: **3,35%**
- Volume ratio 20g: **1.23**
- Rendimento 30g: **+24,68%**
- Rendimento 90g: **+8,03%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Triangolo ascendente possibile | CANDIDATO | 0 | rialzista | n/a | n/a | n/a | n/a | n/a | n/a | n/a | Resistenza quasi piatta e minimi crescenti. Stato: CANDIDATO; il pattern non ha una neckline univoca da usare per il lifecycle. |
| Doppio massimo | CANDIDATO | 0 | ribassista | 62.227 $ | n/a | n/a | 58.946 $ | n/a | 28,05% | 63.471 $ | Due massimi simili a 65.508 $ e 65.402 $. Neckline circa 62.227 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 19 giorni. |
| Doppio minimo | TARGET RAGGIUNTO | 0 | rialzista | 65.402 $ | 2026-08-19 | 9g | 68.577 $ | 449,68% | n/a | 64.094 $ | Due minimi simili a 62.227 $ e 62.488 $. Neckline circa 65.402 $. Breakout neckline: 2026-08-19 (9 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 68.577 $; progresso: 449,68%; prezzo sopra neckline. |

## SOL

![Classic visual SOL](classic_visual_SOL.png)

- Pattern principale: **Doppio massimo**
- Stato pattern: **CANDIDATO** (0)
- Famiglia: **ribassista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-06-22 -> 2026-08-09**
- Età formazione: **19 giorni**
- Breakout pattern: **n/a**
- Età breakout: **n/a**
- Neckline: **64,42 $**
- Target teorico: **51,22 $**
- Progresso verso target: **n/a**
- Distanza dalla neckline: **65,08%**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 78,6% RECUPERATO (0) @ 93,12 $** — Swing DOWN 2026-05-11 98,27 -> 2026-08-16 74,20; livello più vicino 78.6% a 93,12; stato RECUPERATO; confluenza: nessuna confluenza indipendente.
- Invalidazione: **65,71 $**
- Relazione prezzo/neckline: **sopra neckline**
- Dettaglio: Due massimi simili vicino a 77,62 tra 2026-06-22 e 2026-08-09. Neckline ribassista stimata: 64,42. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 19 giorni. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **BREAKOUT 60G**
- Supporto: **83,52 $**
- Resistenza: **127,97 $**
- Breakout 60g: **102,59 $**
- Breakdown 60g: **64,42 $**
- RSI14: **79.68**
- ATR14: **5,00%**
- Volume ratio 20g: **1.88**
- Rendimento 30g: **+44,49%**
- Rendimento 90g: **+28,82%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Triangolo discendente possibile | CANDIDATO | 0 | ribassista | n/a | n/a | n/a | n/a | n/a | n/a | n/a | Massimi decrescenti e supporto quasi piatto. Stato: CANDIDATO; il pattern non ha una neckline univoca da usare per il lifecycle. |
| Doppio massimo | CANDIDATO | 0 | ribassista | 70,69 $ | n/a | n/a | 62,66 $ | n/a | 50,42% | 72,11 $ | Due massimi simili a 78,73 $ e 77,62 $. Neckline circa 70,69 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 19 giorni. |
| Testa e spalle inverso | TARGET RAGGIUNTO | 0 | rialzista | 78,17 $ | 2026-08-19 | 9g | 85,65 $ | 376,72% | n/a | 76,61 $ | Spalla sinistra 73,40 $, testa 70,69 $, spalla destra 74,20 $. Neckline circa 78,17 $. Breakout neckline: 2026-08-19 (9 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 85,65 $; progresso: 376,72%; prezzo sopra neckline. |
| Doppio minimo | TARGET RAGGIUNTO | 0 | rialzista | 78,73 $ | 2026-08-19 | 9g | 84,05 $ | 518,65% | n/a | 77,15 $ | Due minimi simili a 73,40 $ e 74,20 $. Neckline circa 78,73 $. Breakout neckline: 2026-08-19 (9 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 84,05 $; progresso: 518,65%; prezzo sopra neckline. |

## DOGE

![Classic visual DOGE](classic_visual_DOGE.png)

- Pattern principale: **Doppio massimo**
- Stato pattern: **CANDIDATO** (0)
- Famiglia: **ribassista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-07-26 -> 2026-08-11**
- Età formazione: **17 giorni**
- Breakout pattern: **n/a**
- Età breakout: **n/a**
- Neckline: **0.06797 $**
- Target teorico: **0.06214 $**
- Progresso verso target: **n/a**
- Distanza dalla neckline: **28,76%**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 38,2% TESTATO (0) @ 0.08775 $** — Swing UP 2026-08-01 0.06797 -> 2026-08-22 0.09998; livello più vicino 38.2% a 0.08775; stato TESTATO; confluenza: nessuna confluenza indipendente.
- Invalidazione: **0.06933 $**
- Relazione prezzo/neckline: **sopra neckline**
- Dettaglio: Due massimi simili vicino a 0.07380 tra 2026-07-26 e 2026-08-11. Neckline ribassista stimata: 0.06797. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 17 giorni. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **NEL RANGE**
- Supporto: **0.08744 $**
- Resistenza: **0.09169 $**
- Breakout 60g: **0.09998 $**
- Breakdown 60g: **0.06797 $**
- RSI14: **64.48**
- ATR14: **5,92%**
- Volume ratio 20g: **1.03**
- Rendimento 30g: **+24,90%**
- Rendimento 90g: **-12,82%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Doppio massimo | CANDIDATO | 0 | ribassista | 0.06797 $ | n/a | n/a | 0.06214 $ | n/a | 28,76% | 0.06933 $ | Due massimi simili a 0.07380 $ e 0.07286 $. Neckline circa 0.06797 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 17 giorni. |
| Doppio minimo | TARGET RAGGIUNTO | 0 | rialzista | 0.07923 $ | 2026-08-20 | 8g | 0.08952 $ | 80,58% | n/a | 0.07765 $ | Due minimi simili a 0.06961 $ e 0.06895 $. Neckline circa 0.07923 $. Breakout neckline: 2026-08-20 (8 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 0.08952 $; progresso: 80,58%; prezzo sopra neckline. |

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

Generato: 2026-08-28 08:01 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [fractal_path_tracker.md](fractal_path_tracker.md)

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-08-28**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-02-12**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **106,34 $**
- Verdetto principale: **ANALOGIA DEBOLE / SCENARIO SECONDARIO**
- Somiglianza strutturale: **+63,74%**
- Aderenza live principale: **+70,24%**
- Errore medio live principale: **14,88%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE SOLO DI CONTESTO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **83**
- Osservazioni inclusive dal bottom: **84**
- Osservazioni da inizio programma/scanner: **57**
- Errore assoluto medio dal bottom: **12,03%**
- Errore assoluto medio da inizio programma: **14,88%**
- Gap firmato medio ultimi 7 giorni: **+14,40%**
- Errore assoluto medio ultimi 7 giorni: **14,40%**
- Gap ultimo giorno: **+23,90%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **+23,90%**
- Gap firmato medio 7g: **+14,40%**
- Errore assoluto medio 7g: **14,40%**
- Variazione recente gap: **+11,50%**
- Stato gap: **DISALLINEATO SOPRA IL FRATTALE**
- Trend gap: **SOL sta aumentando il distacco sopra il percorso ancorato**

Soglie operative del grafico:

- entro **±5%**: percorso vicino;
- tra **±5% e ±12%**: deviazione gestibile;
- oltre **±12%**: frattale non abbastanza aderente per conferma operativa;
- oltre **±18%**: disallineamento marcato.

## Ultimi giorni del confronto ancorato

|   Giorno | Data SOL   | Data BTC eq.   | SOL reale   | Percorso ancorato   | Gap firmato   | Fase                |
|---------:|:-----------|:---------------|:------------|:--------------------|:--------------|:--------------------|
| 74 | 2026-08-19 | 2023-02-03 | 85,37 $ | 92,37 $ | -7,58% | da inizio programma |
| 75 | 2026-08-20 | 2023-02-04 | 87,64 $ | 91,91 $ | -4,65% | da inizio programma |
| 76 | 2026-08-21 | 2023-02-05 | 93,65 $ | 90,43 $ | +3,57% | da inizio programma |
| 77 | 2026-08-22 | 2023-02-06 | 93,91 $ | 89,66 $ | +4,75% | da inizio programma |
| 78 | 2026-08-23 | 2023-02-07 | 95,44 $ | 91,64 $ | +4,15% | da inizio programma |
| 79 | 2026-08-24 | 2023-02-08 | 98,56 $ | 90,36 $ | +9,07% | da inizio programma |
| 80 | 2026-08-25 | 2023-02-09 | 96,60 $ | 85,95 $ | +12,39% | da inizio programma |
| 81 | 2026-08-26 | 2023-02-10 | 102,17 $ | 85,29 $ | +19,79% | da inizio programma |
| 82 | 2026-08-27 | 2023-02-11 | 109,21 $ | 86,15 $ | +26,76% | da inizio programma |
| 83 | 2026-08-28 | 2023-02-12 | 106,34 $ | 85,83 $ | +23,90% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-09-04 | 95,83 $ | 118,73 $ | 106,34 $ / 120,26 $ | no | n/a | n/a | n/a |
| 14g | 2026-09-11 | 92,81 $ | 114,99 $ | 106,34 $ / 121,18 $ | no | n/a | n/a | n/a |
| 21g | 2026-09-18 | 88,38 $ | 109,50 $ | 106,34 $ / 121,18 $ | no | n/a | n/a | n/a |
| 28g | 2026-09-25 | 87,31 $ | 108,17 $ | 98,53 $ / 121,18 $ | no | n/a | n/a | n/a |
| 35g | 2026-10-02 | 110,45 $ | 136,85 $ | 98,53 $ / 136,85 $ | no | n/a | n/a | n/a |
| 42g | 2026-10-09 | 110,28 $ | 136,63 $ | 98,53 $ / 138,29 $ | no | n/a | n/a | n/a |
| 49g | 2026-10-16 | 111,08 $ | 137,63 $ | 98,53 $ / 138,99 $ | no | n/a | n/a | n/a |
| 56g | 2026-10-23 | 111,61 $ | 138,28 $ | 98,53 $ / 138,99 $ | no | n/a | n/a | n/a |
| 63g | 2026-10-30 | 119,42 $ | 147,96 $ | 98,53 $ / 148,79 $ | no | n/a | n/a | n/a |
| 70g | 2026-11-06 | 108,69 $ | 134,66 $ | 98,53 $ / 148,79 $ | no | n/a | n/a | n/a |
| 77g | 2026-11-13 | 115,30 $ | 142,85 $ | 98,53 $ / 148,79 $ | no | n/a | n/a | n/a |
| 84g | 2026-11-20 | 112,09 $ | 138,88 $ | 98,53 $ / 148,79 $ | no | n/a | n/a | n/a |
| 91g | 2026-11-27 | 106,09 $ | 131,44 $ | 98,53 $ / 148,79 $ | no | n/a | n/a | n/a |
| 98g | 2026-12-04 | 105,39 $ | 130,58 $ | 98,53 $ / 148,79 $ | no | n/a | n/a | n/a |
| 105g | 2026-12-11 | 110,64 $ | 137,08 $ | 98,53 $ / 148,79 $ | no | n/a | n/a | n/a |
| 112g | 2026-12-18 | 106,83 $ | 132,36 $ | 98,53 $ / 148,79 $ | no | n/a | n/a | n/a |
| 119g | 2026-12-25 | 102,18 $ | 126,60 $ | 98,53 $ / 148,79 $ | no | n/a | n/a | n/a |
| 126g | 2027-01-01 | 103,74 $ | 128,54 $ | 98,53 $ / 148,79 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 43 | 37,21% | 11,59% | 13,80% |
| 14g | 36 | 30,56% | 18,13% | 12,38% |
| 21g | 31 | 19,35% | 25,78% | 14,29% |
| 28g | 24 | 45,83% | 24,28% | 14,54% |
| 35g | 17 | 58,82% | 17,93% | 13,74% |
| 42g | 10 | 100,00% | 9,80% | 13,05% |
| 49g | 3 | 100,00% | 7,07% | 23,90% |
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

Ultima lettura salvata: **2026-08-28** — SOL 106,34 $, gap +23,90%, somiglianza +63,74%.

Nel report principale lascio solo il link, così non diventa troppo lungo.

<!-- SOL_BTC_FRACTAL_HISTORY_END -->

</details>
<!-- COMPACT_SECTION_END:fractal_path -->

<!-- COMPACT_SECTION_START:exchange_microstructure -->
<details>
<summary><strong>🏦 Dati exchange, liquidità e leva</strong></summary>

<!-- EXCHANGE_MICROSTRUCTURE_START -->
# Dati exchange, liquidità e leva

Generato: 2026-08-28 08:02 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [exchange_microstructure_report.md](exchange_microstructure_report.md)

Questo modulo legge Kraken Futures, Bitget Futures e KuCoin Futures come nucleo derivati. OKX e Coinbase vengono raccolti come fonti ausiliarie non pesate.
Non modifica la formula matematica di RSI, Fibonacci o Wyckoff: controlla se quei segnali sono sostenuti da acquisti, vendite, OI, funding e liquidità.

**Limite importante:** questo nucleo non assume disponibile un feed pubblico completo delle liquidazioni. La componente liquidazioni resta neutrale; le zone future restano stime di pressione, non dati certi delle singole posizioni.

Diagnostica completa: [exchange_source_diagnostics.md](exchange_source_diagnostics.md)

## Sintesi

| Asset | Prezzo | Exchange | Segnale candidato | Peso Global | Bias exchange | Confidenza | Copertura | Funding 8h eq. | OI 24h | Taker flow (campione/4h) | Book 0,5% | Liq long campione | Liq short campione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 79.668 $ | 3 | 0 | 0 | LEGGERMENTE POSITIVA / NON PESATA | BASSA | 100% | +0,0031% | -1,09% | 1,96 | -0,72% | 0 $ | 0 $ |
| SOL | 106,75 $ | 3 | 0 | 0 | LEGGERMENTE POSITIVA / NON PESATA | MEDIA | 100% | +0,0021% | +0,77% | 3,28 | -2,65% | 0 $ | 0 $ |
| DOGE | 0.08755 $ | 3 | 0 | 0 | LEGGERMENTE POSITIVA / NON PESATA | BASSA | 100% | +0,0071% | -2,29% | 1,71 | -0,31% | 0 $ | 0 $ |

Il segnale candidato è limitato a **±1**, ma il peso nel Global resta **0** finché il tracker a 7 giorni non raggiunge 30 controlli, almeno 55% di accuratezza e return corretto direzione positivo. Un singolo muro o funding non basta.

La colonna taker usa un campione recente nel primo run. Dopo almeno 3 fotografie distribuite su almeno 45 minuti viene sostituita automaticamente dalla media intraday 4h.

## Dati separati per exchange

| Asset | Exchange | Stato | Funding 8h eq. | Open interest | Taker flow | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | Kraken | OK | +0,0057% | 158,79 mln $ | 1,81 | -4,23% |
| BTC | Bitget | OK | +0,0089% | 2,74 mld $ | 0,03 | +1,20% |
| BTC | Kucoin | OK | +0,0074% | 1,61 mld $ | 0,27 | -7,55% |
| SOL | Kraken | OK | -0,0072% | 31,68 mln $ | 18,55 | -5,74% |
| SOL | Bitget | OK | -0,0032% | 444,95 mln $ | 5,34 | +0,24% |
| SOL | Kucoin | OK | -0,0048% | 307,99 mln $ | 1,14 | -12,13% |
| DOGE | Kraken | OK | +0,0022% | 5,01 mln $ | 4,19 | -14,88% |
| DOGE | Bitget | OK | +0,0058% | 111,55 mln $ | 6,59 | +4,61% |
| DOGE | Kucoin | OK | -0,0042% | 129,81 mln $ | 1,19 | +29,65% |

Kraken, Bitget e KuCoin contribuiscono a funding normalizzato, open interest, trade aggressivi e order book. Non viene inventato un long/short ratio pubblico né un feed completo delle liquidazioni.

## Conferme per indicatori tecnici

### BTC

- Score grezzo exchange: **+2,00**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 1, accuratezza +100,00%.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 0, bear 1, divergenze 0.
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
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 3, accuratezza +33,33%.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 1, bear 1, divergenze 0.
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

- Score grezzo exchange: **+2,00**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 5, accuratezza +60,00%.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 1, bear 0, divergenze 1.
- Flusso taker/order book: **+1,75**.
- OI/funding/basis: **+0,00**.
- Affollamento long/short: **+0,00**.
- Liquidazioni: **NON PESATE / FEED COMPLETO NON ASSUNTO DISPONIBILE**.
- **Wyckoff:** Markdown non pienamente confermato: compare assorbimento compratore.
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
| BTC | +70,00% | +6,41% | 1 | +0,00% | RACCOLTA DATI | 0,00 | +70,00% | +6,41% |
| SOL | +70,00% | +6,90% | 1 | +100,00% | RACCOLTA DATI | 0,00 | +70,00% | +6,90% |
| DOGE | +37,50% | -4,56% | 2 | +100,00% | RACCOLTA DATI | 0,00 | +37,50% | -4,56% |

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

Generato: 2026-08-28 08:02 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [exchange_signal_tracker_report.md](exchange_signal_tracker_report.md)

Questo tracker verifica se il segnale candidato exchange ±1 anticipa correttamente la direzione del prezzo a 1/3/7/14/30 giorni.
Il peso Global resta 0 finché l'orizzonte 7g non ha almeno 30 controlli, accuratezza almeno 55% e return corretto direzione positivo. L'overlay a 30g ha un gate separato.

Controlli maturati completati in questa esecuzione: **15**.

## Ultime fotografie giornaliere

| Data | Asset | Prezzo | Versione | Calibrazione | Candidato | Peso Global | Score raw | Confidenza | Taker 4h | OI 24h | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08-28 | BTC | 79.668,10 | V2.1.3 | OK | 0 | 0 | 2,00 | BASSA | 1,96 | -1,09% | -0,72% |
| 2026-08-28 | DOGE | 0.08755 | V2.1.3 | OK | 0 | 0 | 2,00 | BASSA | 1,71 | -2,29% | -0,31% |
| 2026-08-28 | SOL | 106,75 | V2.1.3 | OK | 0 | 0 | 2,25 | MEDIA | 3,28 | +0,77% | -2,65% |
| 2026-08-27 | BTC | 78.647,60 | V2.1.3 | OK | 0 | 0 | 2,00 | BASSA | 2,39 | -0,57% | -0,55% |
| 2026-08-27 | DOGE | 0.08647 | V2.1.3 | OK | 0 | 0 | 0,75 | BASSA | 1,07 | -1,20% | -4,58% |
| 2026-08-27 | SOL | 100,90 | V2.1.3 | OK | 0 | 0 | 2,25 | MEDIA | 0,96 | +1,70% | +10,07% |
| 2026-08-26 | BTC | 78.654,90 | V2.1.3 | OK | 0 | 0 | 2,00 | BASSA | 1,31 | -1,63% | -1,02% |
| 2026-08-26 | DOGE | 0.08606 | V2.1.3 | OK | 0 | 0 | -0,25 | BASSA | 0,79 | -1,68% | -1,23% |
| 2026-08-26 | SOL | 96,32 | V2.1.3 | OK | 1 | 0 | 3,25 | MEDIA | 3,71 | -4,29% | +9,82% |

## Accuratezza direzionale

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 3 | +66,67% | +0,12% | -0,41% | +0,59% | FEEDBACK RAPIDO |
| BTC | 3g | 3 | +66,67% | +1,27% | -1,97% | +3,06% | FEEDBACK RAPIDO |
| BTC | 7g | 1 | +100,00% | +1,35% | -1,18% | +3,82% | FEEDBACK RAPIDO |
| BTC | 14g | 1 | +0,00% | -2,63% | -3,44% | +3,82% | FEEDBACK RAPIDO |
| BTC | 30g | 1 | +0,00% | -0,24% | -3,45% | +3,82% | FEEDBACK RAPIDO |
| SOL | 1g | 5 | +60,00% | +0,93% | +0,43% | +3,39% | FEEDBACK RAPIDO |
| SOL | 3g | 4 | +50,00% | +1,44% | -3,49% | +6,15% | FEEDBACK RAPIDO |
| SOL | 7g | 3 | +33,33% | +4,01% | -3,47% | +8,64% | FEEDBACK RAPIDO |
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

**BTC** — BTC: i futures sembrano più vulnerabili verso una discesa improvvisa. Non significa che deve scendere, ma se rompe sotto può accelerare. Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale.

**SOL** — SOL: i futures non danno una lettura chiara. Non si vede uno sbilanciamento forte né long né short. Qui pesa di più il report frattale.

**DOGE** — DOGE: i futures non danno una lettura chiara. Non si vede uno sbilanciamento forte né long né short. Qui pesa di più il report frattale.

| Asset | Prezzo | Funding | OI 24h | Long/Short | Lettura futures | Forza |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 79.679 $ | +0.0100% | -10.70% | 1.52 | Rischio sotto | 2/5 |
| SOL | 106,34 $ | +0.0032% | -43.87% | 2.65 | Misto | 1/5 |
| DOGE | 0.08752 $ | +0.0043% | -9.26% | 3.61 | Misto | 1/5 |

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

Generato: 2026-08-28 08:02 UTC


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
| BTC     | 1D   | Hidden bullish     | CONFERMATA    | 79.703 $ / 79,39  | 2026-08-03 62.227 $ / RSI 47,40 → 2026-08-14 62.488 $ / RSI 42,71   | n/a                 | n/a              |      0 |
| BTC     | 1W   | Conferma rialzista | CONTESTO      | 79.703 $ / 58,35  | n/a                                                                 | +23,21%             | 18,61            |      0 |
| SOL     | 1D   | Conferma rialzista | CONTESTO      | 106,54 $ / 80,14  | n/a                                                                 | +41,44%             | 29,16            |      0 |
| SOL     | 1W   | Hidden bearish     | CONFERMATA    | 106,54 $ / 60,13  | 2026-05-17 98,27 $ / RSI 38,29 → 2026-07-05 83,81 $ / RSI 42,25     | n/a                 | n/a              |      0 |
| DOGE    | 1D   | Conferma rialzista | CONTESTO      | 0.08759 $ / 64,64 | n/a                                                                 | +25,13%             | 18,64            |      0 |
| DOGE    | 1W   | Hidden bearish     | IN_FORMAZIONE | 0.08759 $ / 46,61 | 2026-05-17 0.11825 $ / RSI 44,25 → 2026-08-23 0.09998 $ / RSI 49,72 | n/a                 | n/a              |      0 |

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

Generato: 2026-08-28 08:02 UTC


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
| BTC | 79.679 $ | 7 | RIALZISTA TECNICO | Trend rialzista | Momentum misto | Compressione / triangolo | 0 | 0 / TESTATO | Doppio minimo / TARGET RAGGIUNTO | Doppio massimo / CANDIDATO | 62.488 | 82.792 |
| SOL | 106,34 $ | 8 | RIALZISTA TECNICO | Trend rialzista | Momentum in miglioramento | Compressione / triangolo | 0 | 0 / RECUPERATO | Doppio minimo / TARGET RAGGIUNTO | Doppio massimo / CANDIDATO | 74,20 | 127,97 |
| DOGE | 0.08752 $ | 2 | NEUTRALE / MISTO | Trend misto | Momentum misto | Struttura rialzista con massimi e minimi crescenti | 0 | 0 / TESTATO | Triplo minimo / TARGET RAGGIUNTO | Doppio massimo / CANDIDATO | 0.06895 | 0.09998 |

## Riepilogo ciclo di vita pattern

| Asset   | Doppio minimo    | Triplo minimo    | Adam/Eve Bottom                        | Doppio massimo   | Triplo massimo   | Adam/Eve Top                 |   Punteggio pattern |
|:--------|:-----------------|:-----------------|:---------------------------------------|:-----------------|:-----------------|:-----------------------------|--------------------:|
| BTC | TARGET RAGGIUNTO | TARGET RAGGIUNTO | Adam and Eve Bottom — TARGET RAGGIUNTO | CANDIDATO | CANDIDATO | Adam and Eve Top — CANDIDATO | 0 |
| SOL | TARGET RAGGIUNTO | TARGET RAGGIUNTO | Adam and Eve Bottom — TARGET RAGGIUNTO | CANDIDATO | CANDIDATO | Adam and Eve Top — CANDIDATO | 0 |
| DOGE | TARGET RAGGIUNTO | TARGET RAGGIUNTO | Adam and Eve Bottom — TARGET RAGGIUNTO | CANDIDATO | CANDIDATO | Adam and Eve Top — CANDIDATO | 0 |

## Indicatori tecnici

| Asset   |   RSI 14 |   Istogramma MACD | MA20    | MA50    | MA200   | Pendenza MA50 20g   | Pendenza MA200 60g   | Rendimento 30g   | Rendimento 90g   |
|:--------|---------:|------------------:|:--------|:--------|:--------|:--------------------|:---------------------|:-----------------|:-----------------|
| BTC | 79.27 | 1112.5 | 70.454 | 66.759 | 69.272 | 5,44% | -8,07% | 23,10% | 8,29% |
| SOL | 79.68 | 2.55859 | 86,35 | 79,66 | 81,58 | 5,78% | -13,71% | 42,80% | 29,21% |
| DOGE | 64.48 | 0.00112 | 0.07862 | 0.07429 | 0.08905 | 1,80% | -14,68% | 24,05% | -12,70% |

## Dettaglio asset

### BTC

- Prezzo: **79.679 $**
- Punteggio tecnico: **7 / 12**
- Verdetto: **RIALZISTA TECNICO**
- Trend: **Trend rialzista** (3)
- Momentum: **Momentum misto** (0)
- Volume: **Volume da accumulazione** (1)
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
  - Due minimi simili vicino a 62.201 tra 2026-06-18 e 2026-08-14. Neckline stimata: 66.910. Breakout neckline: 2026-08-19 (9 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 71.619; progresso corrente: 271,17%. Relazione prezzo/neckline: sopra neckline.
  - neckline 66.910; target 71.619; breakout 2026-08-19 (9g); progresso 271,17%; prezzo sopra neckline.
- Triplo minimo: **TARGET RAGGIUNTO** (0)
  - Tre minimi simili vicino a 62.201 dal 2026-06-18 al 2026-08-14. Neckline stimata: 66.910. Breakout neckline: 2026-08-19 (9 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 71.619; progresso corrente: 271,17%. Relazione prezzo/neckline: sopra neckline.
  - neckline 66.910; target 71.619; breakout 2026-08-19 (9g); progresso 271,17%; prezzo sopra neckline.
- Adam and Eve Bottom: **TARGET RAGGIUNTO** (0)
  - Pattern Adam and Eve Bottom vicino a 59.109 dal 2026-06-05 al 2026-08-14. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 67.248. Breakout neckline: 2026-08-19 (9 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 75.387; progresso corrente: 152,73%. Relazione prezzo/neckline: sopra neckline.
  - neckline 67.248; target 75.387; breakout 2026-08-19 (9g); progresso 152,73%; prezzo sopra neckline.
- Doppio massimo: **CANDIDATO** (0)
  - Due massimi simili vicino a 65.544 tra 2026-06-22 e 2026-08-09. Neckline ribassista stimata: 57.748. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 19 giorni.
  - neckline 57.748; target 49.952; distanza dalla neckline 37,98%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 65.544 dal 2026-06-22 al 2026-08-09. Neckline ribassista stimata: 57.748. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 19 giorni.
  - neckline 57.748; target 49.952; distanza dalla neckline 37,98%; prezzo sopra neckline.
- Adam and Eve Top: **CANDIDATO** (0)
  - Pattern Adam and Eve Top vicino a 67.248 dal 2026-06-15 al 2026-07-21. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 57.748. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 38 giorni.
  - neckline 57.748; target 48.247; distanza dalla neckline 37,98%; prezzo sopra neckline.

### SOL

- Prezzo: **106,34 $**
- Punteggio tecnico: **8 / 12**
- Verdetto: **RIALZISTA TECNICO**
- Trend: **Trend rialzista** (3)
- Momentum: **Momentum in miglioramento** (2)
- Volume: **Volume da accumulazione** (1)
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
  - Due minimi simili vicino a 73,40 tra 2026-07-17 e 2026-08-16. Neckline stimata: 78,73. Breakout neckline: 2026-08-19 (9 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 84,05; progresso corrente: 518,65%. Relazione prezzo/neckline: sopra neckline.
  - neckline 78,73; target 84,05; breakout 2026-08-19 (9g); progresso 518,65%; prezzo sopra neckline.
- Triplo minimo: **TARGET RAGGIUNTO** (0)
  - Tre minimi simili vicino a 70,69 dal 2026-07-17 al 2026-08-16. Neckline stimata: 78,73. Breakout neckline: 2026-08-19 (9 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 86,76; progresso corrente: 343,81%. Relazione prezzo/neckline: sopra neckline.
  - neckline 78,73; target 86,76; breakout 2026-08-19 (9g); progresso 343,81%; prezzo sopra neckline.
- Adam and Eve Bottom: **TARGET RAGGIUNTO** (0)
  - Pattern Adam and Eve Bottom vicino a 67,92 dal 2026-06-19 al 2026-08-01. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 83,81. Breakout neckline: 2026-08-19 (9 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 99,70; progresso corrente: 141,79%. Relazione prezzo/neckline: sopra neckline.
  - neckline 83,81; target 99,70; breakout 2026-08-19 (9g); progresso 141,79%; prezzo sopra neckline.
- Doppio massimo: **CANDIDATO** (0)
  - Due massimi simili vicino a 77,62 tra 2026-06-22 e 2026-08-09. Neckline ribassista stimata: 64,42. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 19 giorni.
  - neckline 64,42; target 51,22; distanza dalla neckline 65,08%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 78,88 dal 2026-07-15 al 2026-08-09. Neckline ribassista stimata: 70,69. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 19 giorni.
  - neckline 70,69; target 62,51; distanza dalla neckline 50,42%; prezzo sopra neckline.
- Adam and Eve Top: **CANDIDATO** (0)
  - Pattern Adam and Eve Top vicino a 77,62 dal 2026-06-15 al 2026-08-09. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 64,42. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 19 giorni.
  - neckline 64,42; target 51,22; distanza dalla neckline 65,08%; prezzo sopra neckline.

### DOGE

- Prezzo: **0.08752 $**
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
  - Due minimi simili vicino a 0.06829 tra 2026-07-24 e 2026-08-12. Neckline stimata: 0.07380. Breakout neckline: 2026-08-19 (9 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 0.07931; progresso corrente: 248,88%. Relazione prezzo/neckline: sopra neckline.
  - neckline 0.07380; target 0.07931; breakout 2026-08-19 (9g); progresso 248,88%; prezzo sopra neckline.
- Triplo minimo: **TARGET RAGGIUNTO** (0)
  - Tre minimi simili vicino a 0.06835 dal 2026-06-30 al 2026-08-12. Neckline stimata: 0.07923. Breakout neckline: 2026-08-20 (8 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 0.09012; progresso corrente: 76,12%. Relazione prezzo/neckline: sopra neckline.
  - neckline 0.07923; target 0.09012; breakout 2026-08-20 (8g); progresso 76,12%; prezzo sopra neckline.
- Adam and Eve Bottom: **TARGET RAGGIUNTO** (0)
  - Pattern Adam and Eve Bottom vicino a 0.06829 dal 2026-07-24 al 2026-08-06. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 0.07380. Breakout neckline: 2026-08-19 (9 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 0.07931; progresso corrente: 248,88%. Relazione prezzo/neckline: sopra neckline.
  - neckline 0.07380; target 0.07931; breakout 2026-08-19 (9g); progresso 248,88%; prezzo sopra neckline.
- Doppio massimo: **CANDIDATO** (0)
  - Due massimi simili vicino a 0.07380 tra 2026-07-26 e 2026-08-11. Neckline ribassista stimata: 0.06797. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 17 giorni.
  - neckline 0.06797; target 0.06214; distanza dalla neckline 28,76%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 0.07923 dal 2026-07-04 al 2026-08-11. Neckline ribassista stimata: 0.06797. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 17 giorni.
  - neckline 0.06797; target 0.05671; distanza dalla neckline 28,76%; prezzo sopra neckline.
- Adam and Eve Top: **CANDIDATO** (0)
  - Pattern Adam and Eve Top vicino a 0.07923 dal 2026-07-04 al 2026-08-11. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 0.06797. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 17 giorni.
  - neckline 0.06797; target 0.05671; distanza dalla neckline 28,76%; prezzo sopra neckline.

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

- **BTC**: 27/30 previsioni controllate su 55 fatte. Stato: **RACCOLTA DATI**.
- **SOL**: 27/30 previsioni controllate su 55 fatte. Stato: **RACCOLTA DATI**.
- **DOGE**: 27/30 previsioni controllate su 55 fatte. Stato: **RACCOLTA DATI**.

| Asset | Previsioni fatte | Controllate | Progresso | In attesa | Stato | Prossimo controllo |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 55 | 27 | 27/30 [█████████░] | 28 | RACCOLTA DATI | 2026-08-29 / tra 1 giorno |
| SOL | 55 | 27 | 27/30 [█████████░] | 28 | RACCOLTA DATI | 2026-08-29 / tra 1 giorno |
| DOGE | 55 | 27 | 27/30 [█████████░] | 28 | RACCOLTA DATI | 2026-08-29 / tra 1 giorno |

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

Generato: 2026-08-28 08:02 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [data_quality_coherence_report.md](data_quality_coherence_report.md)

Questo controllo non modifica punteggi o decisioni. Verifica che tutti i moduli usino lo stesso prezzo corrente e che le nuove regole Technical/Classic Visual siano integre.

## Stato finale: **WARN**

## Avvisi

- 1 campi prezzo superano la tolleranza specifica del modulo.

## Prezzo unico per modulo

| Modulo                  | Asset   | Campo             | Stato   | Prezzo snapshot   | Prezzo modulo   | Differenza   |
|:------------------------|:--------|:------------------|:--------|:------------------|:----------------|:-------------|
| Scanner                 | BTC     | current_price     | OK      | 79.679 $          | 79.679 $        | +0,0000%     |
| Scanner                 | DOGE    | current_price     | OK      | 0.08752 $         | 0.08752 $       | -0,0000%     |
| Scanner                 | SOL     | current_price     | OK      | 106,34 $          | 106,34 $        | +0,0000%     |
| Scanner Forecast        | BTC     | current_price     | OK      | 79.679 $          | 79.679 $        | +0,0000%     |
| Scanner Forecast        | SOL     | current_price     | OK      | 106,34 $          | 106,34 $        | +0,0000%     |
| Scanner Forecast        | DOGE    | current_price     | OK      | 0.08752 $         | 0.08752 $       | -0,0000%     |
| Technical Structure     | BTC     | price             | OK      | 79.679 $          | 79.679 $        | +0,0000%     |
| Technical Structure     | SOL     | price             | OK      | 106,34 $          | 106,34 $        | +0,0000%     |
| Technical Structure     | DOGE    | price             | OK      | 0.08752 $         | 0.08752 $       | -0,0000%     |
| Classic Technical       | BTC     | price             | OK      | 79.679 $          | 79.679 $        | +0,0000%     |
| Classic Technical       | SOL     | price             | OK      | 106,34 $          | 106,34 $        | +0,0000%     |
| Classic Technical       | DOGE    | price             | OK      | 0.08752 $         | 0.08752 $       | -0,0000%     |
| Classic Visual          | BTC     | price             | OK      | 79.679 $          | 79.679 $        | +0,0000%     |
| Classic Visual          | SOL     | price             | OK      | 106,34 $          | 106,34 $        | +0,0000%     |
| Classic Visual          | DOGE    | price             | OK      | 0.08752 $         | 0.08752 $       | -0,0000%     |
| Exchange Microstructure | BTC     | price             | OK      | 79.679 $          | 79.668 $        | -0,0142%     |
| Exchange Microstructure | SOL     | price             | WARN    | 106,34 $          | 106,75 $        | +0,3837%     |
| Exchange Microstructure | DOGE    | price             | OK      | 0.08752 $         | 0.08755 $       | +0,0343%     |
| RSI top-cycle           | SOL     | current_price     | OK      | 106,34 $          | 106,34 $        | +0,0000%     |
| RSI top-cycle           | SOL     | current_price     | OK      | 106,34 $          | 106,34 $        | +0,0000%     |
| Frattale BTC/SOL        | SOL     | sol_current_price | OK      | 106,34 $          | 106,34 $        | +0,0000%     |
| Fractal path            | SOL     | current_price     | OK      | 106,34 $          | 106,34 $        | +0,0000%     |

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

Generato: 2026-08-28T16:30:34+00:00

- Modalità: **SOLO PAPER TRADING**
- Asset: **SOL spot**
- Leva: **nessuna (1x)**
- Capitale iniziale separato: **€40.000,00**
- Fonte mercato: **KUCOIN_PUBLIC_API**; nuove entrate: **CONSENTITE**

| Equity | Cash | SOL | Prezzo | Rendimento | Realizzato | Commissioni | Max DD | Operazioni |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €43.453,09 | €43.453,09 | 0.000000 | 105.2020 | +8.63% | €3.453,09 | €75,44 | 6.48% | 56 |

**Ultima decisione:** SELL_20_PERCENT — SOL sopra la prima banda adattiva.

Bande 4H: L2 93.3661 · L1 96.3246 · media 100.0227 · U1 103.7209 · U2 106.6794.

> Questo portafoglio non condivide capitale, posizioni o statistiche con il paper trading da €10.000.
<!-- SOL_SPOT_ADAPTIVE_END -->
