<!-- COMPACT_REPORT_HEADER_START -->
> **Vista compatta:** Decisione operativa, Global Confluence e cambiamenti giornalieri restano aperti. Tocca il titolo di una sezione per mostrare o nascondere i dettagli.  
> Tutte le tabelle e tutti i dati restano nel file: copiando il Markdown raw viene copiato tutto.
<!-- COMPACT_REPORT_HEADER_END -->

<!-- COMPACT_SECTION_START:decision -->
<details open>
<summary><strong>🧭 Decisione operativa — da leggere per prima</strong></summary>

<!-- DECISION_REPORT_START -->

# Decisione operativa sintetica

Generato: 2026-07-23 07:38 UTC

Report separato completo: [decision_report.md](decision_report.md)

Sintesi automatica dello scanner: l'azione spot viene copiata direttamente dal Global Confluence; long, short e rischio restano filtri separati e più prudenti.

| Asset | Global | Direzione | Spot | Long leva | Short leva | Max long | Max short | Rischio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +1 | NEUTRALE / COSTRUTTIVO | HOLD / ATTESA CONFERME | NO LONG A LEVA / ATTENDI SOPRA 67.248 $ | NO SHORT | nessuna | nessuna | MEDIO / ALTO |
| SOL | +1 | NEUTRALE / INCERTO | HOLD LEGGERO / ATTESA CONFERME | NO LONG A LEVA | NO SHORT | nessuna | nessuna | MOLTO ALTO |
| DOGE | -3 | LEGGERMENTE BEARISH | EVITA LONG / SOLO RIMBALZI VELOCI | NO LONG A LEVA | SHORT SOLO DOPO SPIKE | nessuna | max 1x-2x isolated | MOLTO ALTO |

## Lettura immediata

- **BTC**: Global = **+1**, spot = **HOLD / ATTESA CONFERME**, long = **NO LONG A LEVA / ATTENDI SOPRA 67.248 $**, short = **NO SHORT**, rischio = **MEDIO / ALTO**.
- **SOL**: Global = **+1**, spot = **HOLD LEGGERO / ATTESA CONFERME**, long = **NO LONG A LEVA**, short = **NO SHORT**, rischio = **MOLTO ALTO**.
- **DOGE**: Global = **-3**, spot = **EVITA LONG / SOLO RIMBALZI VELOCI**, long = **NO LONG A LEVA**, short = **SHORT SOLO DOPO SPIKE**, rischio = **MOLTO ALTO**.

## Dettaglio logica

### BTC

- Global Confluence: **+1**
- Confluenza: **MISTA / PARZIALE**
- Bias Global: **Neutrale / misto**
- Direzione decisionale: **NEUTRALE / COSTRUTTIVO**
- Azione spot dal Global: **HOLD / ATTESA CONFERME**
- Long leva: **NO LONG A LEVA / ATTENDI SOPRA 67.248 $**
- Short leva: **NO SHORT**
- Rischio: **MEDIO / ALTO**
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
- Conferme: Doppio minimo maturo finché mantiene 75,94; nuova conferma tecnica sopra 78,88; milestone analogiche 103,59 / 112,92, valide soltanto se rientra anche il gap frattale.
- Invalidazioni: Allarmi sotto 73,25 / 73,40 / 62,19.

### DOGE

- Global Confluence: **-3**
- Confluenza: **DEBOLE / FRAGILE**
- Bias Global: **Fragile**
- Direzione decisionale: **LEGGERMENTE BEARISH**
- Azione spot dal Global: **EVITA LONG / SOLO RIMBALZI VELOCI**
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
- **Lifecycle EMA200** = per SOL resta solo contesto, peso Global 0; score interno 4; EMA200 circa 112,77 $; upside verso EMA200 +46,23%. Non autorizza leva e non aggiunge punti automatici.
- **NO LONG** non significa automaticamente **SHORT**. Lo short ha senso solo se il quadro è bearish o se lo spike viene spesso scaricato.
- Per SOL, se il Global è da **+3 in su**, la decisione non deve diventare bearish solo perché lo scanner grezzo a 30 giorni è incerto.

<!-- DECISION_REPORT_END -->

<!-- PAPER_TRADING_START -->
# Paper trading automatico KuCoin

Generato: 2026-07-23T07:38:17+00:00


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [paper_trading_report.md](paper_trading_report.md)

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-07-23T07:34:49+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-07-23T07:34:49+00:00 | 2026-07-23T07:34:49+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-07-23T07:15:00+00:00 | 2026-07-23T07:15:00+00:00 | 4,9 min | 25,0 min | OK |
| 60m | 12 | 2026-07-23T06:00:00+00:00 | 2026-07-23T06:00:00+00:00 | 34,9 min | 45,0 min | OK |
| 240m | 12 | 2026-07-23T00:00:00+00:00 | 2026-07-23T00:00:00+00:00 | 3,58 h | 1,00 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | LAB | 240m | SHORT | -8,25 | 6,00 | 0,00 | STALE_CANDLE | 3,58 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 214.9 minuti; tolleranza 60 minuti. |
| Principale 4H | AKE | 240m | LONG | 7,75 | 6,00 | 0,00 | STALE_CANDLE | 3,58 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 214.9 minuti; tolleranza 60 minuti. |
| Principale 4H | BANK | 240m | LONG | 7,75 | 6,00 | 0,00 | STALE_CANDLE | 3,58 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 214.9 minuti; tolleranza 60 minuti. |
| Principale 4H | HYPE | 240m | SHORT | -7,29 | 6,00 | 0,00 | STALE_CANDLE | 3,58 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 214.9 minuti; tolleranza 60 minuti. |
| Principale 4H | ADA | 240m | LONG | 6,29 | 6,00 | 0,00 | STALE_CANDLE | 3,58 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 214.9 minuti; tolleranza 60 minuti. |
| Principale 4H | DOGE | 240m | SHORT | -6,05 | 6,00 | 0,00 | STALE_CANDLE | 3,58 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 214.9 minuti; tolleranza 60 minuti. |
| Principale 4H | ETH | 240m | LONG | 4,75 | 6,00 | 1,25 | STALE_CANDLE | 3,58 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 214.9 minuti; tolleranza 60 minuti. |
| Principale 4H | ZEC | 240m | SHORT | -3,90 | 6,00 | 2,10 | STALE_CANDLE | 3,58 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 214.9 minuti; tolleranza 60 minuti. |
| Principale 4H | XRP | 240m | LONG | 3,03 | 6,00 | 2,97 | STALE_CANDLE | 3,58 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 214.9 minuti; tolleranza 60 minuti. |
| Principale 4H | SOL | 240m | LONG | 1,67 | 6,00 | 4,33 | STALE_CANDLE | 3,58 h | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 214.9 minuti; tolleranza 60 minuti. |
| Principale 4H | PEPE | 240m | LONG | 1,04 | 6,00 | 4,96 | STALE_CANDLE | 3,58 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 214.9 minuti; tolleranza 60 minuti. |
| Principale 4H | BTC | 240m | SHORT | -0,25 | 6,00 | 5,75 | STALE_CANDLE | 3,58 h | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 214.9 minuti; tolleranza 60 minuti. |
| Bilanciata 1H V2 | DOGE | 60m | SHORT | -5,51 | 5,50 | 0,00 | STRATEGY_FILTER | 34,9 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Filtro V2 non superato: regime, EMA, ritorni e RSI; per Rapida V2 servono anche breakout reale, volume e ADX. |
| Rapida 1H V1 | DOGE | 60m | SHORT | -5,51 | 4,50 | 0,00 | STRATEGY_FILTER | 34,9 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Filtro momentum: serve breakout DOWN oppure movimento breve ≥1,5%; breakout=NONE, movimento=-0.49%. |
| 1H Fast Nohigh Cap75 V1 | DOGE | 60m | SHORT | -5,51 | 4,50 | 0,00 | STRATEGY_FILTER | 34,9 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Filtro momentum: serve breakout DOWN oppure movimento breve ≥1,5%; breakout=NONE, movimento=-0.49%. |
| 1H Fast No Pepe V1 | DOGE | 60m | SHORT | -5,51 | 4,50 | 0,00 | STRATEGY_FILTER | 34,9 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Filtro momentum: serve breakout DOWN oppure movimento breve ≥1,5%; breakout=NONE, movimento=-0.49%. |
| 1H Fast Tp2 V1 | DOGE | 60m | SHORT | -5,51 | 4,50 | 0,00 | STRATEGY_FILTER | 34,9 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Filtro momentum: serve breakout DOWN oppure movimento breve ≥1,5%; breakout=NONE, movimento=-0.49%. |
| Rapida 1H V2 | DOGE | 60m | SHORT | -5,51 | 5,00 | 0,00 | STRATEGY_FILTER | 34,9 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Filtro V2 non superato: regime, EMA, ritorni e RSI; per Rapida V2 servono anche breakout reale, volume e ADX. |
| Forza relativa 1H V1 | DOGE | 60m | SHORT | -5,51 | 4,00 | 0,00 | STRATEGY_FILTER | 34,9 min | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Filtro forza relativa: serve almeno ±2,0% contro BTC; valore=-0.06%. |
| Rapida 1H V1 | BANK | 60m | LONG | 5,50 | 4,50 | 0,00 | STRATEGY_FILTER | 34,9 min | D: n/a | W: n/a | peso 0 | Filtro momentum: serve breakout UP oppure movimento breve ≥1,5%; breakout=NONE, movimento=+0.33%. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.922,84 | -0,77% | €-77,16 | €3.000,00 | -2,57% | 4 | 17 | 29,41% | 0,73 | 4,26% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 17 | 365 | CAMPIONE INSUFFICIENTE | 30 (mancano 13) |

- Trade del Principale 4H chiusi: **17**; win rate **29,41%**; profit factor **0,73**.
- Expectancy: **€-8,97** per trade; P&L netto: **€-152,45**; max drawdown: **4,26%**.
- Valutazione: **Servono altri eventi indipendenti prima di trarre conclusioni.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 4 | €9.922,84 | €1.512,92 | €4.538,75 | €147,66 | €74,39 |
| TEST | Scanner Top 5 Long 1H | 3 | €10.495,82 | €1.266,43 | €2.532,86 | €157,89 | €-16,69 |
| TEST | Scanner Top 5 + forza BTC 1H | 3 | €10.376,32 | €2.729,95 | €5.459,91 | €156,45 | €-37,34 |
| TEST | Bilanciata 1H V3 Filtered | 4 | €10.283,86 | €2.235,58 | €6.706,75 | €154,42 | €7,79 |
| TEST | Combo Adaptive | 3 | €10.218,64 | €2.169,96 | €4.339,92 | €153,94 | €-18,85 |
| TEST | Benchmark Donchian breakout 1H | 3 | €10.167,63 | €3.555,00 | €7.109,99 | €152,79 | €13,39 |
| TEST | Bilanciata 1H V1 | 4 | €10.129,42 | €3.258,29 | €9.774,87 | €203,95 | €-75,43 |
| TEST | Benchmark Bollinger mean reversion 1H | 1 | €10.114,88 | €1.299,75 | €2.599,50 | €50,41 | €0,54 |
| TEST | Btc Bollinger 1H | 0 | €10.099,96 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Mean Reversion | 0 | €10.085,92 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Forza relativa 1H V2 | 4 | €10.062,38 | €1.816,61 | €3.633,23 | €148,54 | €7,12 |
| TEST | Ampia 4H | 4 | €10.053,65 | €2.235,83 | €4.471,66 | €201,27 | €-33,05 |
| TEST | Btc Bollinger 4H | 1 | €10.043,49 | €1.313,84 | €2.627,69 | €50,00 | €46,82 |
| TEST | Sol Bollinger 4H | 1 | €10.032,03 | €968,56 | €1.937,11 | €50,00 | €33,51 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €10.028,40 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Bollinger 1H | 0 | €10.015,45 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €50 · 15x | 0 | €10.014,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H V2 | 4 | €10.009,38 | €1.825,85 | €5.477,55 | €149,54 | €8,13 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 0 | €10.005,68 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 0 | €10.005,24 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €10 · 15x | 0 | €10.002,80 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 4H | 1 | €10.001,68 | €1.105,63 | €2.211,26 | €50,00 | €-0,29 |
| TEST | Btc Donchian 4H | 1 | €10.001,68 | €1.105,63 | €2.211,26 | €50,00 | €-0,29 |
| TEST | Scalp RSI Long 15 · €10 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €10 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €50 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €50 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · prudente · 5x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · prudente · 5x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €10 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €10 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €50 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · €50 · 15x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · prudente · 5x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 80 · prudente · 5x | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Bollinger 1H | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Donchian 1H | 0 | €9.997,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V3 Filtered | 3 | €9.989,20 | €2.120,81 | €6.362,43 | €148,99 | €0,00 |
| TEST | Btc Adaptive 1H | 0 | €9.988,26 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Donchian 1H | 0 | €9.982,54 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Ema 4H | 1 | €9.981,09 | €883,93 | €1.767,86 | €50,00 | €-17,47 |
| TEST | Btc Adaptive 4H | 1 | €9.976,47 | €1.047,40 | €2.094,81 | €50,00 | €-24,37 |
| TEST | Sol Ema 1H | 1 | €9.971,52 | €1.001,44 | €3.004,32 | €49,95 | €-17,91 |
| TEST | Sol Adaptive 4H | 1 | €9.970,74 | €807,13 | €1.614,26 | €50,00 | €-28,56 |
| TEST | Doge Donchian 1H | 0 | €9.968,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 4H | 1 | €9.968,08 | €880,51 | €1.761,01 | €50,00 | €-31,16 |
| TEST | Sol Donchian 4H | 1 | €9.968,08 | €880,51 | €1.761,01 | €50,00 | €-31,16 |
| TEST | Scanner Top5 Btc Runner25 V1 | 3 | €9.965,64 | €1.277,26 | €2.554,51 | €149,85 | €-15,84 |
| TEST | Scanner Top5 Btc Tp3 V1 | 3 | €9.965,64 | €1.277,26 | €2.554,51 | €149,85 | €-15,84 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.964,86 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 1H | 1 | €9.962,24 | €1.000,51 | €3.001,52 | €49,91 | €-17,90 |
| TEST | 1H Fast No Pepe V1 | 4 | €9.960,83 | €2.745,37 | €8.236,12 | €199,36 | €-9,35 |
| TEST | Scanner Top5 Btc Btc Le3 V1 | 3 | €9.959,10 | €2.827,84 | €5.655,68 | €150,04 | €-42,32 |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | 3 | €9.959,10 | €2.827,84 | €5.655,68 | €150,04 | €-42,32 |
| TEST | Doge Ema 1H | 0 | €9.948,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Tp3 V1 | 3 | €9.945,89 | €2.339,93 | €4.679,86 | €149,52 | €-16,14 |
| TEST | Rapida 1H V2 | 0 | €9.944,87 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 1H | 0 | €9.944,21 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 1H | 0 | €9.937,58 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 1H | 0 | €9.934,39 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Mfe V1 | 3 | €9.930,22 | €2.556,00 | €5.111,99 | €149,56 | €18,45 |
| TEST | Benchmark trend following EMA 1H | 3 | €9.929,69 | €2.181,37 | €4.362,74 | €149,06 | €-15,61 |
| TEST | Combo Trend | 3 | €9.927,44 | €1.698,61 | €3.397,22 | €100,04 | €-21,21 |
| TEST | Eth Adaptive 1H | 1 | €9.918,67 | €1.153,05 | €3.459,15 | €49,81 | €-41,66 |
| TEST | Forza relativa 1H V1 | 4 | €9.909,58 | €2.404,07 | €4.808,14 | €148,58 | €-15,15 |
| TEST | Combo Adaptive Regime V1 | 3 | €9.901,53 | €2.075,49 | €4.150,97 | €148,31 | €-12,61 |
| TEST | Combo Adaptive Quality7 V1 | 2 | €9.899,64 | €1.968,07 | €3.936,13 | €99,06 | €3,30 |
| TEST | 1H Fast V3 Cap75 V1 | 1 | €9.898,20 | €712,28 | €2.136,85 | €49,73 | €0,00 |
| TEST | 1H Fast Score 6 75 V1 | 0 | €9.898,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Long Only V1 | 0 | €9.897,06 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Scanner | 3 | €9.891,20 | €2.783,21 | €5.566,43 | €149,21 | €-13,69 |
| TEST | Combo Adaptive Runner25 V1 | 3 | €9.883,55 | €3.243,15 | €6.486,31 | €149,32 | €-24,00 |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | 2 | €9.870,01 | €954,90 | €2.864,70 | €99,67 | €-12,31 |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | 3 | €9.864,02 | €1.282,24 | €2.564,48 | €148,09 | €-15,68 |
| TEST | Combo Adaptive Long Only V1 | 2 | €9.854,44 | €1.099,22 | €2.198,44 | €98,72 | €-11,51 |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | 0 | €9.850,91 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Ema 1H | 1 | €9.850,17 | €1.144,65 | €3.433,94 | €49,45 | €-37,29 |
| TEST | 1H Fast V3 No Esports V1 | 1 | €9.845,03 | €712,28 | €2.136,85 | €49,73 | €0,00 |
| TEST | Combo Adaptive Quality7 Regime V1 | 2 | €9.841,37 | €1.973,66 | €3.947,32 | €99,07 | €3,30 |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | 2 | €9.841,37 | €1.973,66 | €3.947,32 | €99,07 | €3,30 |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | 3 | €9.835,08 | €1.280,52 | €2.561,03 | €147,68 | €14,08 |
| TEST | 1H Fast Tp2 V1 | 2 | €9.830,72 | €849,53 | €2.548,60 | €98,95 | €22,70 |
| TEST | 1H Fast Nohigh Cap75 V1 | 2 | €9.823,11 | €840,90 | €2.522,69 | €98,32 | €22,69 |
| TEST | 1H Fast V3 Nohigh V1 | 1 | €9.818,47 | €707,41 | €2.122,22 | €49,39 | €0,00 |
| TEST | Master Adaptive Expanded V1 | 3 | €9.802,24 | €2.227,72 | €4.455,45 | €147,21 | €-20,25 |
| TEST | Combo Adaptive Partial 1R V1 | 3 | €9.802,01 | €2.141,01 | €4.282,03 | €147,68 | €-7,58 |
| TEST | Global Confluence puro 1H | 1 | €9.776,79 | €1.527,19 | €3.054,37 | €48,87 | €4,03 |
| TEST | Master Adaptive V1 | 3 | €9.756,37 | €2.731,68 | €5.463,37 | €146,91 | €-23,00 |
| TEST | Master Adaptive No Alt V1 | 3 | €9.756,37 | €2.731,68 | €5.463,37 | €146,91 | €-23,00 |
| TEST | Master Adaptive Runner25 V1 | 3 | €9.756,37 | €2.731,68 | €5.463,37 | €146,91 | €-23,00 |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | 0 | €9.749,89 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V1 | 3 | €9.730,21 | €2.121,86 | €6.365,57 | €146,23 | €0,00 |
| TEST | Scanner Top5 Btc Guard Mfe V1 | 3 | €9.723,42 | €1.161,43 | €2.322,87 | €146,28 | €13,92 |
| TEST | Scanner Bottom 5 Short 1H | 3 | €9.721,27 | €2.430,51 | €4.861,03 | €97,11 | €10,24 |
| TEST | Master Adaptive Strict3 V1 | 3 | €9.706,39 | €2.826,24 | €5.652,48 | €147,55 | €-13,03 |
| TEST | Scanner Top5 Btc Guard V1 | 3 | €9.702,66 | €1.161,08 | €2.322,16 | €146,20 | €-15,43 |
| TEST | Master Adaptive Gb20 V1 | 3 | €9.672,31 | €1.258,76 | €2.517,53 | €146,00 | €-19,87 |
| TEST | Combo Adaptive Mfe Trail | 3 | €9.665,67 | €1.149,02 | €2.298,05 | €96,76 | €-15,54 |

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
| PRINCIPALE | Principale 4H | Confluenza trend | €9.922,84 | €-152,45 | 17 | 17 | 29,41% | 0,73 | €-8,97 | 4,26% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.495,82 | €513,90 | 28 | 28 | 50,00% | 1,96 | €18,35 | 2,70% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €10.376,32 | €416,52 | 20 | 20 | 50,00% | 2,23 | €20,83 | 1,74% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €10.283,86 | €279,12 | 29 | 29 | 44,83% | 1,37 | €9,62 | 2,20% |
| TEST | Combo Adaptive | Combo Adaptive | €10.218,64 | €239,35 | 20 | 20 | 45,00% | 1,71 | €11,97 | 1,31% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €10.167,63 | €157,56 | 17 | 17 | 47,06% | 1,40 | €9,27 | 2,05% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €10.129,42 | €209,55 | 31 | 31 | 48,39% | 1,34 | €6,76 | 2,08% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €10.114,88 | €116,68 | 20 | 20 | 45,00% | 1,34 | €5,83 | 2,06% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.099,96 | €99,96 | 2 | 2 | 100,00% | ∞ | €49,98 | 0,31% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €10.085,92 | €85,92 | 9 | 9 | 44,44% | 1,40 | €9,55 | 1,12% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €10.062,38 | €57,01 | 24 | 23 | 33,33% | 1,08 | €2,38 | 3,69% |
| TEST | Ampia 4H | Confluenza trend | €10.053,65 | €88,72 | 12 | 12 | 25,00% | 1,27 | €7,39 | 2,37% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.043,49 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,27% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €10.032,03 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,40% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €10.028,40 | €28,40 | 6 | 6 | 33,33% | 1,98 | €4,73 | 0,25% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €10.015,45 | €15,45 | 1 | 1 | 100,00% | ∞ | €15,45 | 0,51% |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | €10.014,00 | €14,00 | 2 | 2 | 100,00% | ∞ | €7,00 | 0,04% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €10.009,38 | €4,32 | 20 | 18 | 50,00% | 1,01 | €0,22 | 2,75% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €10.005,68 | €5,68 | 6 | 6 | 33,33% | 1,98 | €0,95 | 0,05% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €10.005,24 | €5,24 | 2 | 2 | 50,00% | 10,75 | €2,62 | 0,09% |
| TEST | Scalp RSI Long 25 · €10 · 15x | Inversione RSI estrema 15m | €10.002,80 | €2,80 | 2 | 2 | 100,00% | ∞ | €1,40 | 0,01% |
| TEST | Btc Ema 4H | Trend following EMA | €10.001,68 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,45% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €10.001,68 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,45% |
| TEST | Scalp RSI Long 15 · €10 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 20 · €10 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 20 · €50 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 20 · prudente · 5x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 85 · €10 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 80 · €10 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 85 · €50 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 80 · €50 · 15x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 85 · prudente · 5x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Short 80 · prudente · 5x | Inversione RSI estrema 15m | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €9.997,37 | €-2,63 | 2 | 2 | 50,00% | 0,41 | €-1,31 | 0,55% |
| TEST | Rapida 1H V3 Filtered | Momentum / breakout V3 Filtered | €9.989,20 | €-7,38 | 47 | 47 | 34,04% | 0,99 | €-0,16 | 2,89% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €9.988,26 | €-11,74 | 2 | 2 | 50,00% | 0,78 | €-5,87 | 0,89% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.982,54 | €-17,46 | 3 | 3 | 33,33% | 0,84 | €-5,82 | 1,38% |
| TEST | Eth Ema 4H | Trend following EMA | €9.981,09 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,34% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €9.976,47 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,42% |
| TEST | Sol Ema 1H | Trend following EMA | €9.971,52 | €-9,16 | 2 | 2 | 50,00% | 0,83 | €-4,58 | 1,10% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €9.970,74 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,32% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €9.968,98 | €-31,02 | 2 | 2 | 50,00% | 0,46 | €-15,51 | 0,93% |
| TEST | Sol Ema 4H | Trend following EMA | €9.968,08 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,35% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €9.968,08 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,35% |
| TEST | Scanner Top5 Btc Runner25 V1 | Scanner Top 5 + forza BTC | €9.965,64 | €-16,90 | 6 | 6 | 50,00% | 0,90 | €-2,82 | 2,33% |
| TEST | Scanner Top5 Btc Tp3 V1 | Scanner Top 5 + forza BTC | €9.965,64 | €-16,90 | 6 | 6 | 50,00% | 0,90 | €-2,82 | 2,33% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.964,86 | €-35,14 | 6 | 6 | 16,67% | 0,18 | €-5,86 | 0,36% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €9.962,24 | €-18,45 | 2 | 2 | 50,00% | 0,67 | €-9,23 | 1,12% |
| TEST | 1H Fast No Pepe V1 | Momentum / breakout | €9.960,83 | €-25,94 | 17 | 17 | 29,41% | 0,93 | €-1,53 | 2,10% |
| TEST | Scanner Top5 Btc Btc Le3 V1 | Scanner Top 5 + forza BTC | €9.959,10 | €4,45 | 2 | 2 | 50,00% | 1,08 | €2,23 | 1,99% |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | Scanner Top 5 + forza BTC | €9.959,10 | €4,45 | 2 | 2 | 50,00% | 1,08 | €2,23 | 1,99% |
| TEST | Doge Ema 1H | Trend following EMA | €9.948,28 | €-51,72 | 4 | 4 | 50,00% | 0,54 | €-12,93 | 1,27% |
| TEST | Combo Adaptive Tp3 V1 | Combo Adaptive | €9.945,89 | €-35,63 | 8 | 8 | 50,00% | 0,83 | €-4,45 | 1,41% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €9.944,87 | €-55,13 | 5 | 4 | 20,00% | 0,56 | €-11,03 | 1,30% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.944,21 | €-55,79 | 1 | 1 | 0,00% | 0,00 | €-55,79 | 0,62% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €9.937,58 | €-62,42 | 3 | 3 | 33,33% | 0,43 | €-20,81 | 1,49% |
| TEST | Btc Ema 1H | Trend following EMA | €9.934,39 | €-65,61 | 4 | 4 | 25,00% | 0,60 | €-16,40 | 1,56% |
| TEST | Scanner Top5 Btc Mfe V1 | Scanner Top 5 + forza BTC | €9.930,22 | €-85,47 | 6 | 6 | 16,67% | 0,31 | €-14,25 | 2,06% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.929,69 | €-52,14 | 15 | 15 | 33,33% | 0,88 | €-3,48 | 2,25% |
| TEST | Combo Trend | Combo Trend | €9.927,44 | €-49,58 | 17 | 17 | 29,41% | 0,90 | €-2,92 | 3,02% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.918,67 | €-37,64 | 3 | 3 | 66,67% | 0,31 | €-12,55 | 1,02% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €9.909,58 | €-72,58 | 22 | 22 | 27,27% | 0,83 | €-3,30 | 3,25% |
| TEST | Combo Adaptive Regime V1 | Combo Adaptive | €9.901,53 | €-83,93 | 8 | 8 | 37,50% | 0,70 | €-10,49 | 2,18% |
| TEST | Combo Adaptive Quality7 V1 | Combo Adaptive | €9.899,64 | €-101,74 | 3 | 3 | 33,33% | 0,05 | €-33,91 | 1,51% |
| TEST | 1H Fast V3 Cap75 V1 | Momentum / breakout V3 Filtered | €9.898,20 | €-100,92 | 18 | 18 | 27,78% | 0,77 | €-5,61 | 2,49% |
| TEST | 1H Fast Score 6 75 V1 | Momentum / breakout | €9.898,20 | €-101,80 | 19 | 19 | 26,32% | 0,77 | €-5,36 | 2,49% |
| TEST | 1H Fast V3 Long Only V1 | Momentum / breakout V3 Filtered | €9.897,06 | €-102,94 | 10 | 10 | 20,00% | 0,57 | €-10,29 | 2,11% |
| TEST | Combo Scanner | Combo Scanner | €9.891,20 | €-91,73 | 21 | 21 | 38,10% | 0,85 | €-4,37 | 2,66% |
| TEST | Combo Adaptive Runner25 V1 | Combo Adaptive | €9.883,55 | €-89,34 | 8 | 8 | 37,50% | 0,67 | €-11,17 | 1,65% |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | Momentum / breakout | €9.870,01 | €-115,93 | 4 | 4 | 0,00% | 0,00 | €-28,98 | 1,53% |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | Scanner Top 5 + forza BTC | €9.864,02 | €-118,58 | 2 | 2 | 0,00% | 0,00 | €-59,29 | 1,64% |
| TEST | Combo Adaptive Long Only V1 | Combo Adaptive | €9.854,44 | €-132,59 | 5 | 5 | 20,00% | 0,42 | €-26,52 | 2,34% |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | Momentum / breakout V3 Filtered | €9.850,91 | €-149,09 | 9 | 9 | 22,22% | 0,48 | €-16,57 | 2,00% |
| TEST | Eth Ema 1H | Trend following EMA | €9.850,17 | €-110,26 | 5 | 5 | 40,00% | 0,33 | €-22,05 | 1,59% |
| TEST | 1H Fast V3 No Esports V1 | Momentum / breakout V3 Filtered | €9.845,03 | €-154,08 | 19 | 19 | 26,32% | 0,69 | €-8,11 | 2,49% |
| TEST | Combo Adaptive Quality7 Regime V1 | Combo Adaptive | €9.841,37 | €-160,00 | 3 | 3 | 0,00% | 0,00 | €-53,33 | 1,95% |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | Combo Adaptive | €9.841,37 | €-160,00 | 3 | 3 | 0,00% | 0,00 | €-53,33 | 1,95% |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | Scanner Top 5 + forza BTC | €9.835,08 | €-177,42 | 4 | 4 | 0,00% | 0,00 | €-44,36 | 2,30% |
| TEST | 1H Fast Tp2 V1 | Momentum / breakout | €9.830,72 | €-190,85 | 17 | 17 | 23,53% | 0,60 | €-11,23 | 2,47% |
| TEST | 1H Fast Nohigh Cap75 V1 | Momentum / breakout | €9.823,11 | €-198,46 | 23 | 23 | 30,43% | 0,71 | €-8,63 | 2,83% |
| TEST | 1H Fast V3 Nohigh V1 | Momentum / breakout V3 Filtered | €9.818,47 | €-180,65 | 20 | 20 | 30,00% | 0,70 | €-9,03 | 2,96% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €9.802,24 | €-174,68 | 6 | 6 | 16,67% | 0,34 | €-29,11 | 2,79% |
| TEST | Combo Adaptive Partial 1R V1 | Combo Adaptive | €9.802,01 | €-187,92 | 10 | 10 | 30,00% | 0,51 | €-18,79 | 2,24% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.776,79 | €-226,02 | 7 | 7 | 28,57% | 0,17 | €-32,29 | 2,92% |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | €9.756,37 | €-216,46 | 4 | 4 | 0,00% | 0,00 | €-54,11 | 2,77% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €9.756,37 | €-216,46 | 4 | 4 | 0,00% | 0,00 | €-54,11 | 2,77% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €9.756,37 | €-216,46 | 4 | 4 | 0,00% | 0,00 | €-54,11 | 2,77% |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | Momentum / breakout V3 Filtered | €9.749,89 | €-250,11 | 9 | 9 | 33,33% | 0,25 | €-27,79 | 2,84% |
| TEST | Rapida 1H V1 | Momentum / breakout | €9.730,21 | €-266,37 | 55 | 55 | 30,91% | 0,80 | €-4,84 | 6,66% |
| TEST | Scanner Top5 Btc Guard Mfe V1 | Scanner Top 5 + forza BTC | €9.723,42 | €-289,21 | 7 | 7 | 0,00% | 0,00 | €-41,32 | 3,47% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.721,27 | €-286,05 | 19 | 19 | 26,32% | 0,46 | €-15,06 | 4,93% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €9.706,39 | €-276,43 | 5 | 5 | 0,00% | 0,00 | €-55,29 | 3,29% |
| TEST | Scanner Top5 Btc Guard V1 | Scanner Top 5 + forza BTC | €9.702,66 | €-280,49 | 5 | 5 | 0,00% | 0,00 | €-56,10 | 3,31% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €9.672,31 | €-306,25 | 10 | 10 | 20,00% | 0,10 | €-30,62 | 3,84% |
| TEST | Combo Adaptive Mfe Trail | Combo Adaptive | €9.665,67 | €-317,53 | 27 | 27 | 25,93% | 0,45 | €-11,76 | 4,11% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | DOGE | SHORT | Confluenza trend | 240m | 3,0x | 0,07292 | 0,07228 | 0,07500 | 0,09686 | 0,06875 | €574,44 | €1.723,33 | €49,28 | €15,02 |
| Principale 4H | LAB | SHORT | Confluenza trend | 240m | 3,0x | 0,17841 | 0,15250 | 0,17841 | 0,23699 | 0,13559 | €136,26 | €408,77 | €0,00 | €59,37 |
| Principale 4H | SUI | LONG | Confluenza trend | 240m | 3,0x | 0,76296 | 0,76296 | 0,73998 | 0,51245 | 0,80891 | €547,52 | €1.642,56 | €49,46 | €0,00 |
| Principale 4H | ONDO | LONG | Confluenza trend | 240m | 3,0x | 0,40344 | 0,40344 | 0,37762 | 0,27098 | 0,45509 | €254,70 | €764,09 | €48,91 | €0,00 |
| Bilanciata 1H V1 | ONDO | LONG | Confluenza trend | 60m | 3,0x | 0,39694 | 0,39694 | 0,38539 | 0,26661 | 0,42004 | €581,76 | €1.745,29 | €50,78 | €0,00 |
| Bilanciata 1H V1 | ZEC | SHORT | Confluenza trend | 60m | 3,0x | 514,40710 | 514,72000 | 526,37866 | 683,30410 | 490,46397 | €731,22 | €2.193,66 | €51,05 | €-1,33 |
| Bilanciata 1H V1 | ETH | LONG | Confluenza trend | 60m | 3,0x | 1937,36740 | 1914,53000 | 1909,46931 | 1301,26510 | 1993,16358 | €1.184,41 | €3.553,24 | €51,17 | €-41,89 |
| Bilanciata 1H V1 | ADA | LONG | Confluenza trend | 60m | 3,0x | 0,17542 | 0,17294 | 0,17150 | 0,11782 | 0,18325 | €760,90 | €2.282,69 | €50,95 | €-32,21 |
| Bilanciata 1H V2 | ESPORTS | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,02164 | 0,02164 | 0,02164 | 0,02874 | 0,01644 | €138,69 | €416,06 | €0,00 | €-0,00 |
| Bilanciata 1H V2 | AKE | LONG | Confluenza trend V2 | 60m | 3,0x | 0,00180 | 0,00184 | 0,00159 | 0,00121 | 0,00222 | €143,70 | €431,11 | €50,27 | €9,81 |
| Bilanciata 1H V2 | ZEC | SHORT | Confluenza trend V2 | 60m | 3,0x | 512,43749 | 514,72000 | 523,41700 | 680,68780 | 490,47847 | €780,12 | €2.340,36 | €50,14 | €-10,42 |
| Bilanciata 1H V2 | HYPE | SHORT | Confluenza trend V2 | 60m | 3,0x | 58,72425 | 58,50000 | 59,98403 | 78,00538 | 56,20471 | €763,34 | €2.290,02 | €49,13 | €8,74 |
| Bilanciata 1H V3 Filtered | ESPORTS | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,02126 | 0,02126 | 0,02126 | 0,02823 | 0,01615 | €141,51 | €424,52 | €0,00 | €-0,00 |
| Bilanciata 1H V3 Filtered | ONDO | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,40134 | 0,40134 | 0,38898 | 0,26957 | 0,42605 | €557,59 | €1.672,77 | €51,50 | €0,00 |
| Bilanciata 1H V3 Filtered | ZEC | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 514,40710 | 514,72000 | 526,37866 | 683,30410 | 490,46397 | €738,63 | €2.215,89 | €51,57 | €-1,35 |
| Bilanciata 1H V3 Filtered | HYPE | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 58,72425 | 58,50000 | 59,98403 | 78,00538 | 56,20471 | €797,86 | €2.393,58 | €51,35 | €9,14 |
| Rapida 1H V1 | ESPORTS | SHORT | Momentum / breakout | 60m | 3,0x | 0,01984 | 0,01984 | 0,02222 | 0,02635 | 0,01627 | €129,65 | €388,96 | €46,68 | €-0,00 |
| Rapida 1H V1 | SUI | LONG | Momentum / breakout | 60m | 3,0x | 0,76416 | 0,76416 | 0,75422 | 0,51326 | 0,77907 | €1.284,19 | €3.852,58 | €50,12 | €0,00 |
| Rapida 1H V1 | ONDO | LONG | Momentum / breakout | 60m | 3,0x | 0,39924 | 0,39924 | 0,38995 | 0,26816 | 0,41318 | €708,01 | €2.124,02 | €49,43 | €0,00 |
| 1H Fast Nohigh Cap75 V1 | ONDO | LONG | Momentum / breakout | 60m | 3,0x | 0,39924 | 0,39924 | 0,38995 | 0,26816 | 0,41318 | €704,39 | €2.113,17 | €49,18 | €0,00 |
| 1H Fast Nohigh Cap75 V1 | BANK | LONG | Momentum / breakout | 60m | 3,0x | 0,23652 | 0,24962 | 0,20814 | 0,15886 | 0,27909 | €136,51 | €409,52 | €49,14 | €22,69 |
| 1H Fast Long Btc 1 3 Cap75 V1 | ONDO | LONG | Momentum / breakout | 60m | 3,0x | 0,39694 | 0,39694 | 0,38849 | 0,26661 | 0,40961 | €783,06 | €2.349,19 | €50,00 | €0,00 |
| 1H Fast Long Btc 1 3 Cap75 V1 | LAB | LONG | Momentum / breakout | 60m | 3,0x | 0,15623 | 0,15250 | 0,14118 | 0,10494 | 0,17881 | €171,84 | €515,51 | €49,67 | €-12,31 |
| 1H Fast No Pepe V1 | ONDO | LONG | Momentum / breakout | 60m | 3,0x | 0,39924 | 0,39924 | 0,38995 | 0,26816 | 0,41318 | €713,68 | €2.141,05 | €49,83 | €0,00 |
| 1H Fast No Pepe V1 | ZEC | SHORT | Momentum / breakout | 60m | 3,0x | 515,14695 | 514,72000 | 524,33753 | 684,28687 | 501,36109 | €935,01 | €2.805,03 | €50,04 | €2,32 |
| 1H Fast No Pepe V1 | ADA | LONG | Momentum / breakout | 60m | 3,0x | 0,17481 | 0,17294 | 0,17178 | 0,11742 | 0,17937 | €954,58 | €2.863,74 | €49,72 | €-30,71 |
| 1H Fast No Pepe V1 | BANK | LONG | Momentum / breakout | 60m | 3,0x | 0,23895 | 0,24962 | 0,21105 | 0,16049 | 0,28080 | €142,10 | €426,29 | €49,78 | €19,04 |
| 1H Fast Tp2 V1 | ONDO | LONG | Momentum / breakout | 60m | 3,0x | 0,39924 | 0,39924 | 0,38995 | 0,26816 | 0,41782 | €712,92 | €2.138,77 | €49,77 | €0,00 |
| 1H Fast Tp2 V1 | BANK | LONG | Momentum / breakout | 60m | 3,0x | 0,23652 | 0,24962 | 0,20814 | 0,15886 | 0,29328 | €136,61 | €409,83 | €49,18 | €22,70 |
| Rapida 1H V3 Filtered | ESPORTS | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,01977 | 0,01977 | 0,02214 | 0,02626 | 0,01621 | €137,70 | €413,09 | €49,57 | €-0,00 |
| Rapida 1H V3 Filtered | SUI | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,76416 | 0,76416 | 0,75422 | 0,51326 | 0,77907 | €1.267,97 | €3.803,92 | €49,49 | €0,00 |
| Rapida 1H V3 Filtered | ONDO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,39924 | 0,39924 | 0,38995 | 0,26816 | 0,41318 | €715,14 | €2.145,42 | €49,93 | €0,00 |
| 1H Fast V3 Cap75 V1 | ONDO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,39924 | 0,39924 | 0,38995 | 0,26816 | 0,41318 | €712,28 | €2.136,85 | €49,73 | €0,00 |
| 1H Fast V3 Nohigh V1 | ONDO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,39924 | 0,39924 | 0,38995 | 0,26816 | 0,41318 | €707,41 | €2.122,22 | €49,39 | €0,00 |
| 1H Fast V3 No Esports V1 | ONDO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,39924 | 0,39924 | 0,38995 | 0,26816 | 0,41318 | €712,28 | €2.136,85 | €49,73 | €0,00 |
| Ampia 4H | DOGE | SHORT | Confluenza trend | 240m | 2,0x | 0,07237 | 0,07228 | 0,07515 | 0,10819 | 0,06457 | €649,49 | €1.298,97 | €50,00 | €1,55 |
| Ampia 4H | ZEC | LONG | Confluenza trend | 240m | 2,0x | 522,36445 | 514,72000 | 483,09844 | 263,79405 | 632,30930 | €332,53 | €665,06 | €49,99 | €-9,73 |
| Ampia 4H | PEPE | LONG | Confluenza trend | 240m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €497,18 | €994,35 | €50,70 | €-9,92 |
| Ampia 4H | ETH | LONG | Confluenza trend | 240m | 2,0x | 1933,63665 | 1914,53000 | 1869,00475 | 976,48651 | 2114,60597 | €756,64 | €1.513,28 | €50,58 | €-14,95 |
| Forza relativa 1H V1 | ESPORTS | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,02126 | 0,02126 | 0,02126 | 0,03178 | 0,01564 | €208,05 | €416,10 | €0,00 | €-0,00 |
| Forza relativa 1H V1 | NIGHT | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,02031 | 0,02031 | 0,02210 | 0,03036 | 0,01637 | €285,91 | €571,83 | €50,45 | €-0,00 |
| Forza relativa 1H V1 | ONDO | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,42171 | €891,90 | €1.783,80 | €49,29 | €0,00 |
| Forza relativa 1H V1 | ZEC | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 510,91780 | 514,72000 | 523,17072 | 763,82211 | 483,96137 | €1.018,21 | €2.036,41 | €48,84 | €-15,15 |
| Forza relativa 1H V2 | ESPORTS | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,02126 | 0,02126 | 0,02126 | 0,03178 | 0,01564 | €215,33 | €430,67 | €0,00 | €-0,00 |
| Forza relativa 1H V2 | ZEC | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 512,43749 | 514,72000 | 523,41700 | 766,09405 | 488,28257 | €1.188,35 | €2.376,70 | €50,92 | €-10,59 |
| Forza relativa 1H V2 | AKE | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,00186 | 0,00184 | 0,00164 | 0,00094 | 0,00234 | €214,82 | €429,64 | €50,07 | €-4,25 |
| Forza relativa 1H V2 | BANK | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,23652 | 0,24962 | 0,20814 | 0,11944 | 0,29896 | €198,11 | €396,21 | €47,55 | €21,95 |
| Benchmark Donchian breakout 1H | SUI | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,76606 | 0,76606 | 0,75182 | 0,38686 | 0,80165 | €1.377,00 | €2.754,00 | €51,18 | €0,00 |
| Benchmark Donchian breakout 1H | HYPE | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 58,85923 | 58,50000 | 60,10965 | 87,99454 | 55,73317 | €1.195,13 | €2.390,27 | €50,78 | €14,59 |
| Benchmark Donchian breakout 1H | ZEC | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 514,40710 | 514,72000 | 527,70883 | 769,03861 | 481,15276 | €982,86 | €1.965,73 | €50,83 | €-1,20 |
| Benchmark Bollinger mean reversion 1H | ZEC | LONG | Bollinger mean reversion | 60m | 2,0x | 514,61290 | 514,72000 | 504,63261 | 259,87952 | 529,58334 | €1.299,75 | €2.599,50 | €50,41 | €0,54 |
| Benchmark trend following EMA 1H | LAB | LONG | Trend following EMA | 60m | 2,0x | 0,15689 | 0,15250 | 0,13807 | 0,07923 | 0,19831 | €207,05 | €414,10 | €49,69 | €-11,60 |
| Benchmark trend following EMA 1H | ZEC | SHORT | Trend following EMA | 60m | 2,0x | 511,44769 | 514,72000 | 525,07617 | 764,61430 | 481,46504 | €934,35 | €1.868,69 | €49,79 | €-11,96 |
| Benchmark trend following EMA 1H | HYPE | SHORT | Trend following EMA | 60m | 2,0x | 58,72425 | 58,50000 | 60,12400 | 87,79276 | 55,64481 | €1.039,97 | €2.079,94 | €49,58 | €7,94 |
| Scanner Top 5 Long 1H | ONDO | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,40114 | 0,40114 | 0,38834 | 0,20258 | 0,42673 | €828,91 | €1.657,82 | €52,88 | €0,00 |
| Scanner Top 5 Long 1H | LAB | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,15689 | 0,15250 | 0,13807 | 0,07923 | 0,19455 | €219,03 | €438,05 | €52,57 | €-12,27 |
| Scanner Top 5 Long 1H | AKE | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,00186 | 0,00184 | 0,00164 | 0,00094 | 0,00231 | €218,50 | €437,00 | €52,44 | €-4,42 |
| Scanner Bottom 5 Short 1H | ESPORTS | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,02150 | 0,02150 | 0,02150 | 0,03214 | 0,01634 | €207,40 | €414,80 | €0,00 | €-0,00 |
| Scanner Bottom 5 Short 1H | ZEC | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 515,09696 | 514,72000 | 526,55393 | 770,06996 | 492,18303 | €1.091,80 | €2.183,60 | €48,57 | €1,60 |
| Scanner Bottom 5 Short 1H | HYPE | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 58,72425 | 58,50000 | 59,98403 | 87,79276 | 56,20471 | €1.131,31 | €2.262,62 | €48,54 | €8,64 |
| Scanner Top 5 + forza BTC 1H | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 77,70854 | 77,10200 | 76,45304 | 39,24281 | 80,47063 | €1.614,82 | €3.229,64 | €52,18 | €-25,21 |
| Scanner Top 5 + forza BTC 1H | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39694 | 0,39694 | 0,38539 | 0,20045 | 0,42235 | €898,57 | €1.797,15 | €52,29 | €0,00 |
| Scanner Top 5 + forza BTC 1H | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15250 | 0,13807 | 0,07923 | 0,19831 | €216,56 | €433,12 | €51,97 | €-12,13 |
| Scanner Top5 Btc Mfe V1 | SUI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,76776 | 0,76776 | 0,75508 | 0,38772 | 0,79565 | €1.514,04 | €3.028,08 | €50,00 | €0,00 |
| Scanner Top5 Btc Mfe V1 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39924 | 0,39924 | 0,38729 | 0,20162 | 0,42552 | €835,46 | €1.670,91 | €50,00 | €0,00 |
| Scanner Top5 Btc Mfe V1 | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,23895 | 0,24962 | 0,21027 | 0,12067 | 0,30203 | €206,50 | €413,00 | €49,56 | €18,45 |
| Scanner Top5 Btc Guard V1 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39724 | 0,39724 | 0,38434 | 0,20061 | 0,42561 | €756,62 | €1.513,24 | €49,13 | €0,00 |
| Scanner Top5 Btc Guard V1 | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15250 | 0,13807 | 0,07923 | 0,19831 | €202,47 | €404,95 | €48,59 | €-11,34 |
| Scanner Top5 Btc Guard V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00186 | 0,00184 | 0,00164 | 0,00094 | 0,00235 | €201,99 | €403,97 | €48,48 | €-4,08 |
| Scanner Top5 Btc Btc Le3 V1 | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 77,78955 | 77,10200 | 76,66939 | 39,28373 | 80,25393 | €1.735,32 | €3.470,64 | €49,98 | €-30,68 |
| Scanner Top5 Btc Btc Le3 V1 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39974 | 0,39974 | 0,38840 | 0,20187 | 0,42468 | €884,65 | €1.769,29 | €50,18 | €0,00 |
| Scanner Top5 Btc Btc Le3 V1 | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15250 | 0,13807 | 0,07923 | 0,19831 | €207,87 | €415,74 | €49,89 | €-11,64 |
| Scanner Top5 Btc Btc 2 3 V1 | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 77,78955 | 77,10200 | 76,66939 | 39,28373 | 80,25393 | €1.735,32 | €3.470,64 | €49,98 | €-30,68 |
| Scanner Top5 Btc Btc 2 3 V1 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39974 | 0,39974 | 0,38840 | 0,20187 | 0,42468 | €884,65 | €1.769,29 | €50,18 | €0,00 |
| Scanner Top5 Btc Btc 2 3 V1 | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15250 | 0,13807 | 0,07923 | 0,19831 | €207,87 | €415,74 | €49,89 | €-11,64 |
| Scanner Top5 Btc Guard Mfe V1 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39724 | 0,39724 | 0,38434 | 0,20061 | 0,42561 | €756,62 | €1.513,24 | €49,13 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00186 | 0,00184 | 0,00164 | 0,00094 | 0,00235 | €203,02 | €406,03 | €48,72 | €-4,10 |
| Scanner Top5 Btc Guard Mfe V1 | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,23895 | 0,24962 | 0,21027 | 0,12067 | 0,30203 | €201,80 | €403,60 | €48,43 | €18,03 |
| Scanner Top5 Btc Guard Btc Le3 V1 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39974 | 0,39974 | 0,38840 | 0,20187 | 0,42468 | €871,05 | €1.742,11 | €49,41 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15250 | 0,13807 | 0,07923 | 0,19831 | €205,84 | €411,68 | €49,40 | €-11,53 |
| Scanner Top5 Btc Guard Btc Le3 V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00186 | 0,00184 | 0,00164 | 0,00094 | 0,00235 | €205,35 | €410,69 | €49,28 | €-4,15 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39974 | 0,39974 | 0,38840 | 0,20187 | 0,42468 | €871,05 | €1.742,11 | €49,41 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00186 | 0,00184 | 0,00164 | 0,00094 | 0,00235 | €205,35 | €410,69 | €49,28 | €-4,15 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,23895 | 0,24962 | 0,21027 | 0,12067 | 0,30203 | €204,12 | €408,23 | €48,99 | €18,23 |
| Scanner Top5 Btc Runner25 V1 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39694 | 0,39694 | 0,38539 | 0,20045 | 0,43159 | €861,83 | €1.723,66 | €50,15 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15250 | 0,13807 | 0,07923 | 0,21338 | €207,96 | €415,92 | €49,91 | €-11,65 |
| Scanner Top5 Btc Runner25 V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00186 | 0,00184 | 0,00164 | 0,00094 | 0,00253 | €207,46 | €414,92 | €49,79 | €-4,19 |
| Scanner Top5 Btc Tp3 V1 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39694 | 0,39694 | 0,38539 | 0,20045 | 0,43159 | €861,83 | €1.723,66 | €50,15 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15250 | 0,13807 | 0,07923 | 0,21338 | €207,96 | €415,92 | €49,91 | €-11,65 |
| Scanner Top5 Btc Tp3 V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00186 | 0,00184 | 0,00164 | 0,00094 | 0,00253 | €207,46 | €414,92 | €49,79 | €-4,19 |
| Global Confluence puro 1H | DOGE | SHORT | Global Confluence puro | 60m | 2,0x | 0,07238 | 0,07228 | 0,07353 | 0,10820 | 0,06948 | €1.527,19 | €3.054,37 | €48,87 | €4,03 |
| Combo Trend | ONDO | LONG | Combo Trend | 60m | 2,0x | 0,37282 | 0,37282 | 0,39131 | 0,18828 | 0,41057 | €545,86 | €1.091,71 | €0,00 | €0,00 |
| Combo Trend | ESPORTS | SHORT | Combo Trend | 60m | 2,0x | 0,01883 | 0,01883 | 0,02109 | 0,02815 | 0,01386 | €209,57 | €419,14 | €50,30 | €-0,00 |
| Combo Trend | ZEC | SHORT | Combo Trend | 60m | 2,0x | 508,99818 | 514,72000 | 522,42162 | 760,95228 | 479,46661 | €943,19 | €1.886,37 | €49,75 | €-21,21 |
| Combo Scanner | ONDO | LONG | Combo Scanner | 60m | 2,0x | 0,39694 | 0,39694 | 0,38539 | 0,20045 | 0,42235 | €857,88 | €1.715,77 | €49,92 | €0,00 |
| Combo Scanner | LAB | LONG | Combo Scanner | 60m | 2,0x | 0,15689 | 0,15250 | 0,13807 | 0,07923 | 0,19831 | €207,54 | €415,08 | €49,81 | €-11,62 |
| Combo Scanner | DOGE | SHORT | Combo Scanner | 60m | 2,0x | 0,07224 | 0,07228 | 0,07328 | 0,10799 | 0,06995 | €1.717,79 | €3.435,58 | €49,47 | €-2,06 |
| Combo Adaptive | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,40114 | 0,40114 | 0,38834 | 0,20258 | 0,42673 | €809,25 | €1.618,50 | €51,63 | €0,00 |
| Combo Adaptive | ZEC | SHORT | Combo Adaptive | 60m | 2,0x | 514,17714 | 514,72000 | 525,63928 | 768,69483 | 491,25287 | €1.147,58 | €2.295,16 | €51,16 | €-2,42 |
| Combo Adaptive | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15250 | 0,13958 | 0,08010 | 0,19668 | €213,13 | €426,26 | €51,15 | €-16,43 |
| Combo Adaptive Mfe Trail | ESPORTS | SHORT | Combo Adaptive | 60m | 2,0x | 0,02156 | 0,02156 | 0,02091 | 0,03223 | 0,01638 | €202,62 | €405,24 | €0,00 | €-0,00 |
| Combo Adaptive Mfe Trail | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39784 | 0,39784 | 0,38492 | 0,20091 | 0,42367 | €744,71 | €1.489,41 | €48,35 | €0,00 |
| Combo Adaptive Mfe Trail | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15250 | 0,13958 | 0,08010 | 0,19668 | €201,70 | €403,39 | €48,41 | €-15,54 |
| Combo Adaptive Quality7 V1 | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,40304 | 0,40304 | 0,39140 | 0,20354 | 0,42632 | €859,15 | €1.718,30 | €49,62 | €0,00 |
| Combo Adaptive Quality7 V1 | ZEC | SHORT | Combo Adaptive | 60m | 2,0x | 515,48688 | 514,72000 | 526,97821 | 770,65289 | 492,50422 | €1.108,92 | €2.217,83 | €49,44 | €3,30 |
| Combo Adaptive Regime V1 | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39724 | 0,39724 | 0,38434 | 0,20061 | 0,42303 | €757,94 | €1.515,88 | €49,21 | €0,00 |
| Combo Adaptive Regime V1 | ZEC | SHORT | Combo Adaptive | 60m | 2,0x | 515,48688 | 514,72000 | 526,97821 | 770,65289 | 492,50422 | €1.111,03 | €2.222,05 | €49,53 | €3,31 |
| Combo Adaptive Regime V1 | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15250 | 0,13958 | 0,08010 | 0,19668 | €206,52 | €413,04 | €49,56 | €-15,92 |
| Combo Adaptive Quality7 Regime V1 | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,40554 | 0,40554 | 0,39390 | 0,20480 | 0,42882 | €864,27 | €1.728,54 | €49,61 | €0,00 |
| Combo Adaptive Quality7 Regime V1 | ZEC | SHORT | Combo Adaptive | 60m | 2,0x | 515,48688 | 514,72000 | 526,97821 | 770,65289 | 492,50422 | €1.109,39 | €2.218,78 | €49,46 | €3,30 |
| Combo Adaptive Long Only V1 | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,41951 | €893,67 | €1.787,34 | €49,39 | €0,00 |
| Combo Adaptive Long Only V1 | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15689 | 0,15250 | 0,13807 | 0,07923 | 0,19455 | €205,55 | €411,10 | €49,33 | €-11,51 |
| Combo Adaptive Partial 1R V1 | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,41951 | €893,02 | €1.786,04 | €49,36 | €0,00 |
| Combo Adaptive Partial 1R V1 | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15689 | 0,15250 | 0,13807 | 0,07923 | 0,19455 | €205,22 | €410,44 | €49,25 | €-11,49 |
| Combo Adaptive Partial 1R V1 | ZEC | SHORT | Combo Adaptive | 60m | 2,0x | 515,68684 | 514,72000 | 527,82154 | 770,95183 | 491,41745 | €1.042,77 | €2.085,55 | €49,08 | €3,91 |
| Combo Adaptive Quality7 Regime Partial 1R V1 | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,40554 | 0,40554 | 0,39390 | 0,20480 | 0,42882 | €864,27 | €1.728,54 | €49,61 | €0,00 |
| Combo Adaptive Quality7 Regime Partial 1R V1 | ZEC | SHORT | Combo Adaptive | 60m | 2,0x | 515,48688 | 514,72000 | 526,97821 | 770,65289 | 492,50422 | €1.109,39 | €2.218,78 | €49,46 | €3,30 |
| Combo Adaptive Runner25 V1 | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,43050 | €902,18 | €1.804,37 | €49,86 | €0,00 |
| Combo Adaptive Runner25 V1 | ZEC | SHORT | Combo Adaptive | 60m | 2,0x | 514,68704 | 514,72000 | 525,11837 | 769,45713 | 483,39306 | €1.229,27 | €2.458,54 | €49,83 | €-0,16 |
| Combo Adaptive Runner25 V1 | ADA | LONG | Combo Adaptive | 60m | 2,0x | 0,17481 | 0,17294 | 0,17091 | 0,08828 | 0,18652 | €1.111,70 | €2.223,40 | €49,63 | €-23,85 |
| Combo Adaptive Tp3 V1 | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,43050 | €902,18 | €1.804,37 | €49,86 | €0,00 |
| Combo Adaptive Tp3 V1 | ZEC | SHORT | Combo Adaptive | 60m | 2,0x | 514,68704 | 514,72000 | 525,11837 | 769,45713 | 483,39306 | €1.230,32 | €2.460,64 | €49,87 | €-0,16 |
| Combo Adaptive Tp3 V1 | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15250 | 0,13958 | 0,08010 | 0,21571 | €207,43 | €414,86 | €49,78 | €-15,99 |
| Btc Ema 4H | BTC | LONG | Trend following EMA | 240m | 2,0x | 65410,57950 | 65402,10000 | 63931,54687 | 33032,34265 | 69108,16107 | €1.105,63 | €2.211,26 | €50,00 | €-0,29 |
| Btc Donchian 4H | BTC | LONG | Donchian breakout 20 barre | 240m | 2,0x | 65410,57950 | 65402,10000 | 63931,54687 | 33032,34265 | 69551,87112 | €1.105,63 | €2.211,26 | €50,00 | €-0,29 |
| Btc Bollinger 4H | BTC | SHORT | Bollinger mean reversion | 240m | 2,0x | 66588,49964 | 65402,10000 | 67855,55360 | 99549,80696 | 64307,80290 | €1.313,84 | €2.627,69 | €50,00 | €46,82 |
| Btc Adaptive 4H | BTC | LONG | Combo Adaptive | 240m | 2,0x | 66171,85172 | 65402,10000 | 64592,42491 | 33416,78512 | 70120,41876 | €1.047,40 | €2.094,81 | €50,00 | €-24,37 |
| Sol Ema 1H | SOL | LONG | Trend following EMA | 60m | 3,0x | 77,56451 | 77,10200 | 76,27481 | 52,09750 | 80,14392 | €1.001,44 | €3.004,32 | €49,95 | €-17,91 |
| Sol Ema 4H | SOL | LONG | Trend following EMA | 240m | 2,0x | 78,49069 | 77,10200 | 76,26213 | 39,63780 | 84,06211 | €880,51 | €1.761,01 | €50,00 | €-31,16 |
| Sol Donchian 4H | SOL | LONG | Donchian breakout 20 barre | 240m | 2,0x | 78,49069 | 77,10200 | 76,26213 | 39,63780 | 84,73068 | €880,51 | €1.761,01 | €50,00 | €-31,16 |
| Sol Bollinger 4H | SOL | SHORT | Bollinger mean reversion | 240m | 2,0x | 78,45931 | 77,10200 | 80,48446 | 117,29666 | 74,81402 | €968,56 | €1.937,11 | €50,00 | €33,51 |
| Sol Adaptive 1H | SOL | LONG | Combo Adaptive | 60m | 3,0x | 77,56451 | 77,10200 | 76,27481 | 52,09750 | 80,14392 | €1.000,51 | €3.001,52 | €49,91 | €-17,90 |
| Sol Adaptive 4H | SOL | LONG | Combo Adaptive | 240m | 2,0x | 78,49069 | 77,10200 | 76,05953 | 39,63780 | 84,56860 | €807,13 | €1.614,26 | €50,00 | €-28,56 |
| Eth Ema 1H | ETH | LONG | Trend following EMA | 60m | 3,0x | 1935,54703 | 1914,53000 | 1907,67515 | 1300,04242 | 1991,29079 | €1.144,65 | €3.433,94 | €49,45 | €-37,29 |
| Eth Ema 4H | ETH | LONG | Trend following EMA | 240m | 2,0x | 1933,63665 | 1914,53000 | 1878,94813 | 976,48651 | 2070,35799 | €883,93 | €1.767,86 | €50,00 | €-17,47 |
| Eth Adaptive 1H | ETH | LONG | Combo Adaptive | 60m | 3,0x | 1937,86750 | 1914,53000 | 1909,96220 | 1301,60100 | 1993,67808 | €1.153,05 | €3.459,15 | €49,81 | €-41,66 |
| Master Adaptive V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39854 | 0,39854 | 0,38677 | 0,20126 | 0,42207 | €833,00 | €1.665,99 | €49,19 | €0,00 |
| Master Adaptive V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15689 | 0,15250 | 0,13807 | 0,07923 | 0,19455 | €203,80 | €407,60 | €48,91 | €-11,42 |
| Master Adaptive V1 | XRP | LONG | Master Adaptive Consensus | 60m | 2,0x | 1,13781 | 1,13392 | 1,12142 | 0,57459 | 1,17058 | €1.694,88 | €3.389,77 | €48,81 | €-11,58 |
| Master Adaptive No Alt V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39854 | 0,39854 | 0,38677 | 0,20126 | 0,42207 | €833,00 | €1.665,99 | €49,19 | €0,00 |
| Master Adaptive No Alt V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15689 | 0,15250 | 0,13807 | 0,07923 | 0,19455 | €203,80 | €407,60 | €48,91 | €-11,42 |
| Master Adaptive No Alt V1 | XRP | LONG | Master Adaptive Consensus | 60m | 2,0x | 1,13781 | 1,13392 | 1,12142 | 0,57459 | 1,17058 | €1.694,88 | €3.389,77 | €48,81 | €-11,58 |
| Master Adaptive Strict3 V1 | ETH | LONG | Master Adaptive Consensus | 60m | 2,0x | 1934,24677 | 1914,53000 | 1906,39362 | 976,79462 | 1989,95308 | €1.737,12 | €3.474,23 | €50,03 | €-35,41 |
| Master Adaptive Strict3 V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,41951 | €887,07 | €1.774,14 | €49,03 | €0,00 |
| Master Adaptive Strict3 V1 | BANK | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,23652 | 0,24962 | 0,20814 | 0,11944 | 0,29328 | €202,06 | €404,12 | €48,49 | €22,39 |
| Master Adaptive Expanded V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39854 | 0,39854 | 0,38677 | 0,20126 | 0,42207 | €833,00 | €1.665,99 | €49,19 | €0,00 |
| Master Adaptive Expanded V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15689 | 0,15250 | 0,13807 | 0,07923 | 0,19455 | €203,80 | €407,60 | €48,91 | €-11,42 |
| Master Adaptive Expanded V1 | ADA | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,17358 | 0,17294 | 0,17000 | 0,08766 | 0,18074 | €1.190,93 | €2.381,85 | €49,11 | €-8,84 |
| Master Adaptive Gb20 V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,40304 | 0,40304 | 0,39140 | 0,20354 | 0,42632 | €848,64 | €1.697,27 | €49,02 | €0,00 |
| Master Adaptive Gb20 V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00186 | 0,00184 | 0,00164 | 0,00094 | 0,00229 | €208,66 | €417,31 | €48,63 | €-4,12 |
| Master Adaptive Gb20 V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15870 | 0,15250 | 0,13966 | 0,08014 | 0,19679 | €201,47 | €402,94 | €48,35 | €-15,75 |
| Master Adaptive Runner25 V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39854 | 0,39854 | 0,38677 | 0,20126 | 0,43384 | €833,00 | €1.665,99 | €49,19 | €0,00 |
| Master Adaptive Runner25 V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15689 | 0,15250 | 0,13807 | 0,07923 | 0,21338 | €203,80 | €407,60 | €48,91 | €-11,42 |
| Master Adaptive Runner25 V1 | XRP | LONG | Master Adaptive Consensus | 60m | 2,0x | 1,13781 | 1,13392 | 1,12142 | 0,57459 | 1,18696 | €1.694,88 | €3.389,77 | €48,81 | €-11,58 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1H Fast Tp2 V1 | ADA | LONG | 2026-07-23T07:23:35+00:00 | 0,17227 | €-53,96 | -1,09 | STOP |
| 1H Fast Nohigh Cap75 V1 | ADA | LONG | 2026-07-23T07:23:35+00:00 | 0,17227 | €-54,07 | -1,09 | STOP |
| 1H Fast Long Btc 1 3 Cap75 V1 | ADA | LONG | 2026-07-23T07:23:35+00:00 | 0,17274 | €-54,52 | -1,10 | STOP |
| Rapida 1H V1 | ADA | LONG | 2026-07-23T07:23:35+00:00 | 0,17227 | €-53,53 | -1,09 | STOP |
| Forza relativa 1H V2 | BANK | LONG | 2026-07-23T02:08:35+00:00 | 0,21843 | €-59,36 | -1,21 | STOP_STRESS_SLIPPAGE |
| Master Adaptive Strict3 V1 | BANK | LONG | 2026-07-23T02:08:35+00:00 | 0,21843 | €-59,23 | -1,21 | STOP_STRESS_SLIPPAGE |
| 1H Fast Tp2 V1 | BANK | LONG | 2026-07-23T02:08:35+00:00 | 0,21849 | €-0,17 | -0,00 | STOP_STRESS_SLIPPAGE |
| 1H Fast Nohigh Cap75 V1 | BANK | LONG | 2026-07-23T02:08:35+00:00 | 0,21795 | €-11,35 | -0,23 | STOP_STRESS_SLIPPAGE |
| Scanner Top5 Btc Mfe V1 | LAB | LONG | 2026-07-23T01:23:33+00:00 | 0,14541 | €-50,41 | -1,01 | STOP |
| Scanner Top5 Btc Guard Mfe V1 | LAB | LONG | 2026-07-23T01:23:33+00:00 | 0,14541 | €-49,39 | -1,01 | STOP |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | LAB | LONG | 2026-07-23T01:23:33+00:00 | 0,14541 | €-49,96 | -1,01 | STOP |
| 1H Fast No Pepe V1 | BANK | LONG | 2026-07-23T01:23:33+00:00 | 0,25757 | €72,59 | 1,49 | TARGET |

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

Generato: 2026-07-23 07:38 UTC


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

Segnali totali salvati: **45**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-07-23 | BTC | 65.399,99 | +1 | +2 | +2 | +3 | -1 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-07-23 | DOGE | 0.07229 | -3 | -1 | -1 | 0 | -2 | -1 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-07-23 | SOL | 77,14 | +1 | +3 | +2 | +2 | -2 | -1 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-07-22 | BTC | 66.234,10 | +2 | +2 | +2 | 0 | 0 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-07-22 | DOGE | 0.07318 | -5 | -2 | -1 | -1 | -3 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-07-22 | SOL | 77,82 | -3 | -1 | -1 | 0 | -1 | -1 | 0 | TAKE PROFIT SU SPIKE / NON INSEGUIRE |
| 2026-07-21 | BTC | 65.476,52 | +3 | +2 | +2 | 0 | 0 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-07-21 | DOGE | 0.07281 | -6 | -3 | -2 | -2 | -3 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-07-21 | SOL | 78,22 | +1 | +2 | +1 | +2 | -1 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-07-20 | BTC | 64.190,23 | +2 | +2 | +2 | 0 | -1 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-07-20 | DOGE | 0.07180 | -7 | -3 | -2 | -2 | -3 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-07-20 | SOL | 76,01 | -4 | 0 | 0 | 0 | -3 | -1 | 0 | STAI FUORI / VENDI PARZIALE |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 15 | 14 | 13 | 12 | 10 | 8 | 5 | 1 | 0 | 0 | 0 | 0 |
| SOL | 15 | 14 | 13 | 12 | 10 | 8 | 5 | 1 | 0 | 0 | 0 | 0 |
| DOGE | 15 | 14 | 13 | 12 | 10 | 8 | 5 | 1 | 0 | 0 | 0 | 0 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-07-10 | 14g | 2026-07-24 | domani |
| SOL | 2026-07-10 | 14g | 2026-07-24 | domani |
| DOGE | 2026-07-10 | 14g | 2026-07-24 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 13 | 38,46% | +0,06% | +0,10% | FEEDBACK RAPIDO |
| BTC | 2g | 12 | 50,00% | +0,56% | +0,31% | FEEDBACK RAPIDO |
| BTC | 3g | 11 | 54,55% | +0,63% | +0,27% | FEEDBACK RAPIDO |
| BTC | 5g | 9 | 33,33% | +1,20% | -0,21% | FEEDBACK RAPIDO |
| BTC | 7g | 8 | 62,50% | +1,73% | +1,20% | FEEDBACK RAPIDO |
| BTC | 10g | 5 | 100,00% | +2,63% | +2,63% | FEEDBACK RAPIDO |
| BTC | 14g | 1 | 100,00% | +3,42% | +3,42% | FEEDBACK RAPIDO |
| BTC | 21g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 30g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 1g | 13 | 46,15% | -0,06% | -0,61% | FEEDBACK RAPIDO |
| SOL | 2g | 12 | 16,67% | +0,07% | -1,18% | FEEDBACK RAPIDO |
| SOL | 3g | 11 | 9,09% | +0,14% | -1,79% | FEEDBACK RAPIDO |
| SOL | 5g | 9 | 22,22% | -0,11% | -1,73% | FEEDBACK RAPIDO |
| SOL | 7g | 7 | 42,86% | -0,16% | -1,54% | FEEDBACK RAPIDO |
| SOL | 10g | 4 | 25,00% | +0,19% | -1,19% | FEEDBACK RAPIDO |
| SOL | 14g | 1 | 0,00% | -1,13% | -1,13% | FEEDBACK RAPIDO |
| SOL | 21g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 30g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 1g | 14 | 57,14% | -0,16% | +0,16% | FEEDBACK RAPIDO |
| DOGE | 2g | 13 | 53,85% | -0,12% | +0,12% | FEEDBACK RAPIDO |
| DOGE | 3g | 12 | 50,00% | -0,27% | +0,27% | FEEDBACK RAPIDO |
| DOGE | 5g | 10 | 60,00% | -0,44% | +0,44% | FEEDBACK RAPIDO |
| DOGE | 7g | 8 | 75,00% | -0,80% | +0,80% | FEEDBACK RAPIDO |
| DOGE | 10g | 5 | 60,00% | -0,88% | +0,88% | FEEDBACK RAPIDO |
| DOGE | 14g | 1 | 100,00% | -0,77% | +0,77% | FEEDBACK RAPIDO |
| DOGE | 21g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 30g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 13 | 38,46% | +0,06% | +0,10% | -0,11% | +0,82% | FEEDBACK RAPIDO |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 14 | 42,86% | +0,16% | +0,16% | -0,02% | +0,87% | FEEDBACK RAPIDO |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 14 | 42,86% | +0,16% | +0,16% | -0,02% | +0,87% | FEEDBACK RAPIDO |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 10 | 40,00% | +0,11% | +0,11% | -0,05% | +0,77% | FEEDBACK RAPIDO |
| BTC | 1g | Tecnico | CALIBRABILE | 11 | 27,27% | +0,18% | -0,84% | -0,02% | +0,90% | FEEDBACK RAPIDO |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +2,00% | +2,00% | +1,48% | +2,25% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 12 | 50,00% | +0,56% | +0,31% | +0,01% | +1,66% | FEEDBACK RAPIDO |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 13 | 53,85% | +0,55% | +0,55% | +0,04% | +1,66% | FEEDBACK RAPIDO |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 13 | 53,85% | +0,55% | +0,55% | +0,04% | +1,66% | FEEDBACK RAPIDO |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 10 | 50,00% | +0,30% | +0,30% | -0,30% | +1,45% | FEEDBACK RAPIDO |
| BTC | 2g | Tecnico | CALIBRABILE | 11 | 36,36% | +0,67% | -0,57% | +0,09% | +1,71% | FEEDBACK RAPIDO |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +3,18% | +3,18% | +3,05% | +3,89% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 11 | 54,55% | +0,63% | +0,27% | -1,07% | +2,38% | FEEDBACK RAPIDO |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 12 | 75,00% | +0,78% | +0,78% | -0,94% | +2,41% | FEEDBACK RAPIDO |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 12 | 75,00% | +0,78% | +0,78% | -0,94% | +2,41% | FEEDBACK RAPIDO |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 10 | 70,00% | +0,52% | +0,52% | -1,11% | +2,17% | FEEDBACK RAPIDO |
| BTC | 3g | Tecnico | CALIBRABILE | 11 | 36,36% | +1,01% | -0,21% | -0,84% | +2,54% | FEEDBACK RAPIDO |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,88% | +1,88% | +1,44% | +4,24% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 9 | 33,33% | +1,20% | -0,21% | -2,09% | +2,93% | FEEDBACK RAPIDO |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 10 | 60,00% | +1,32% | +1,32% | -1,90% | +3,11% | FEEDBACK RAPIDO |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 10 | 60,00% | +1,32% | +1,32% | -1,90% | +3,11% | FEEDBACK RAPIDO |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 10 | 60,00% | +1,32% | +1,32% | -1,90% | +3,11% | FEEDBACK RAPIDO |
| BTC | 5g | Tecnico | CALIBRABILE | 9 | 33,33% | +1,35% | -1,13% | -1,75% | +3,23% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 8 | 62,50% | +1,73% | +1,20% | -2,36% | +3,53% | FEEDBACK RAPIDO |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 8 | 75,00% | +1,73% | +1,73% | -2,36% | +3,53% | FEEDBACK RAPIDO |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 8 | 75,00% | +1,73% | +1,73% | -2,36% | +3,53% | FEEDBACK RAPIDO |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 8 | 75,00% | +1,73% | +1,73% | -2,36% | +3,53% | FEEDBACK RAPIDO |
| BTC | 7g | Tecnico | CALIBRABILE | 7 | 57,14% | +2,03% | -0,21% | -2,23% | +3,67% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 5 | 100,00% | +2,63% | +2,63% | -2,65% | +3,95% | FEEDBACK RAPIDO |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 5 | 100,00% | +2,63% | +2,63% | -2,65% | +3,95% | FEEDBACK RAPIDO |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 5 | 100,00% | +2,63% | +2,63% | -2,65% | +3,95% | FEEDBACK RAPIDO |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 5 | 100,00% | +2,63% | +2,63% | -2,65% | +3,95% | FEEDBACK RAPIDO |
| BTC | 10g | Tecnico | CALIBRABILE | 4 | 50,00% | +3,16% | +0,84% | -2,49% | +4,30% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 1 | 100,00% | +3,42% | +3,42% | -2,32% | +5,81% | FEEDBACK RAPIDO |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 1 | 100,00% | +3,42% | +3,42% | -2,32% | +5,81% | FEEDBACK RAPIDO |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 1 | 100,00% | +3,42% | +3,42% | -2,32% | +5,81% | FEEDBACK RAPIDO |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 1 | 100,00% | +3,42% | +3,42% | -2,32% | +5,81% | FEEDBACK RAPIDO |
| BTC | 14g | Tecnico | CALIBRABILE | 1 | 0,00% | +3,42% | -3,42% | -2,32% | +5,81% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 14 | 57,14% | -0,16% | +0,16% | -0,44% | +0,63% | FEEDBACK RAPIDO |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 14 | 57,14% | -0,16% | +0,16% | -0,44% | +0,63% | FEEDBACK RAPIDO |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 14 | 57,14% | -0,16% | +0,16% | -0,44% | +0,63% | FEEDBACK RAPIDO |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 14 | 57,14% | -0,16% | +0,16% | -0,44% | +0,63% | FEEDBACK RAPIDO |
| DOGE | 1g | Tecnico | CALIBRABILE | 14 | 57,14% | -0,16% | +0,16% | -0,44% | +0,63% | FEEDBACK RAPIDO |
| DOGE | 1g | Classic technical | CALIBRABILE | 13 | 53,85% | -0,08% | +0,08% | -0,35% | +0,64% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 13 | 53,85% | -0,12% | +0,12% | -0,72% | +1,32% | FEEDBACK RAPIDO |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 13 | 53,85% | -0,12% | +0,12% | -0,72% | +1,32% | FEEDBACK RAPIDO |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 13 | 53,85% | -0,12% | +0,12% | -0,72% | +1,32% | FEEDBACK RAPIDO |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 13 | 53,85% | -0,12% | +0,12% | -0,72% | +1,32% | FEEDBACK RAPIDO |
| DOGE | 2g | Tecnico | CALIBRABILE | 13 | 53,85% | -0,12% | +0,12% | -0,72% | +1,32% | FEEDBACK RAPIDO |
| DOGE | 2g | Classic technical | CALIBRABILE | 12 | 50,00% | +0,07% | -0,07% | -0,59% | +1,60% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 12 | 50,00% | -0,27% | +0,27% | -1,53% | +2,00% | FEEDBACK RAPIDO |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 12 | 50,00% | -0,27% | +0,27% | -1,53% | +2,00% | FEEDBACK RAPIDO |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 12 | 50,00% | -0,27% | +0,27% | -1,53% | +2,00% | FEEDBACK RAPIDO |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 12 | 50,00% | -0,27% | +0,27% | -1,53% | +2,00% | FEEDBACK RAPIDO |
| DOGE | 3g | Tecnico | CALIBRABILE | 12 | 50,00% | -0,27% | +0,27% | -1,53% | +2,00% | FEEDBACK RAPIDO |
| DOGE | 3g | Classic technical | CALIBRABILE | 11 | 45,45% | -0,10% | +0,10% | -1,45% | +2,13% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 10 | 60,00% | -0,44% | +0,44% | -2,49% | +2,36% | FEEDBACK RAPIDO |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 10 | 60,00% | -0,44% | +0,44% | -2,49% | +2,36% | FEEDBACK RAPIDO |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 10 | 60,00% | -0,44% | +0,44% | -2,49% | +2,36% | FEEDBACK RAPIDO |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 10 | 60,00% | -0,44% | +0,44% | -2,49% | +2,36% | FEEDBACK RAPIDO |
| DOGE | 5g | Tecnico | CALIBRABILE | 10 | 60,00% | -0,44% | +0,44% | -2,49% | +2,36% | FEEDBACK RAPIDO |
| DOGE | 5g | Classic technical | CALIBRABILE | 9 | 55,56% | -0,17% | +0,17% | -2,34% | +2,57% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 8 | 75,00% | -0,80% | +0,80% | -2,83% | +2,60% | FEEDBACK RAPIDO |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 8 | 75,00% | -0,80% | +0,80% | -2,83% | +2,60% | FEEDBACK RAPIDO |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 8 | 75,00% | -0,80% | +0,80% | -2,83% | +2,60% | FEEDBACK RAPIDO |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 8 | 75,00% | -0,80% | +0,80% | -2,83% | +2,60% | FEEDBACK RAPIDO |
| DOGE | 7g | Tecnico | CALIBRABILE | 8 | 75,00% | -0,80% | +0,80% | -2,83% | +2,60% | FEEDBACK RAPIDO |
| DOGE | 7g | Classic technical | CALIBRABILE | 7 | 71,43% | -0,77% | +0,77% | -2,68% | +2,89% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 5 | 60,00% | -0,88% | +0,88% | -2,94% | +2,99% | FEEDBACK RAPIDO |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 5 | 60,00% | -0,88% | +0,88% | -2,94% | +2,99% | FEEDBACK RAPIDO |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 5 | 60,00% | -0,88% | +0,88% | -2,94% | +2,99% | FEEDBACK RAPIDO |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 5 | 60,00% | -0,88% | +0,88% | -2,94% | +2,99% | FEEDBACK RAPIDO |
| DOGE | 10g | Tecnico | CALIBRABILE | 5 | 60,00% | -0,88% | +0,88% | -2,94% | +2,99% | FEEDBACK RAPIDO |
| DOGE | 10g | Classic technical | CALIBRABILE | 5 | 60,00% | -0,88% | +0,88% | -2,94% | +2,99% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 1 | 100,00% | -0,77% | +0,77% | -2,58% | +3,59% | FEEDBACK RAPIDO |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 1 | 100,00% | -0,77% | +0,77% | -2,58% | +3,59% | FEEDBACK RAPIDO |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 1 | 100,00% | -0,77% | +0,77% | -2,58% | +3,59% | FEEDBACK RAPIDO |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 1 | 100,00% | -0,77% | +0,77% | -2,58% | +3,59% | FEEDBACK RAPIDO |
| DOGE | 14g | Tecnico | CALIBRABILE | 1 | 100,00% | -0,77% | +0,77% | -2,58% | +3,59% | FEEDBACK RAPIDO |
| DOGE | 14g | Classic technical | CALIBRABILE | 1 | 100,00% | -0,77% | +0,77% | -2,58% | +3,59% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 13 | 46,15% | -0,06% | -0,61% | -0,40% | +0,84% | FEEDBACK RAPIDO |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 10 | 70,00% | -0,68% | +0,18% | -0,84% | +0,27% | FEEDBACK RAPIDO |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 13 | 61,54% | -0,27% | -0,11% | -0,56% | +0,64% | FEEDBACK RAPIDO |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 8 | 50,00% | -0,17% | +0,34% | -0,66% | +0,79% | FEEDBACK RAPIDO |
| SOL | 1g | Tecnico | CALIBRABILE | 14 | 57,14% | -0,05% | -0,21% | -0,37% | +0,81% | FEEDBACK RAPIDO |
| SOL | 1g | Classic technical | CALIBRABILE | 6 | 66,67% | +0,34% | -0,34% | +0,13% | +1,09% | FEEDBACK RAPIDO |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,51% | -0,51% | -0,47% | +0,31% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 12 | 16,67% | +0,07% | -1,18% | -0,56% | +1,49% | FEEDBACK RAPIDO |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 9 | 44,44% | -0,46% | -0,55% | -1,26% | +0,85% | FEEDBACK RAPIDO |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 12 | 41,67% | -0,26% | -0,50% | -0,96% | +1,33% | FEEDBACK RAPIDO |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 8 | 37,50% | -0,53% | -0,42% | -1,31% | +1,35% | FEEDBACK RAPIDO |
| SOL | 2g | Tecnico | CALIBRABILE | 13 | 23,08% | -0,06% | -0,82% | -0,70% | +1,48% | FEEDBACK RAPIDO |
| SOL | 2g | Classic technical | CALIBRABILE | 5 | 20,00% | +1,30% | -1,30% | +1,03% | +1,98% | FEEDBACK RAPIDO |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -1,38% | -1,38% | -1,57% | +0,62% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 11 | 9,09% | +0,14% | -1,79% | -1,69% | +2,51% | FEEDBACK RAPIDO |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 8 | 37,50% | -0,32% | -0,53% | -2,37% | +1,91% | FEEDBACK RAPIDO |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 11 | 36,36% | -0,15% | -0,47% | -2,05% | +2,31% | FEEDBACK RAPIDO |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 7 | 42,86% | -0,50% | -0,76% | -2,15% | +2,54% | FEEDBACK RAPIDO |
| SOL | 3g | Tecnico | CALIBRABILE | 12 | 25,00% | -0,01% | -0,98% | -1,77% | +2,41% | FEEDBACK RAPIDO |
| SOL | 3g | Classic technical | CALIBRABILE | 5 | 0,00% | +1,89% | -1,89% | -0,57% | +2,88% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 9 | 22,22% | -0,11% | -1,73% | -2,88% | +3,06% | FEEDBACK RAPIDO |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 7 | 57,14% | -0,47% | -0,10% | -3,49% | +2,44% | FEEDBACK RAPIDO |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 10 | 50,00% | -0,12% | -0,28% | -3,05% | +2,88% | FEEDBACK RAPIDO |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 7 | 57,14% | -1,07% | -0,02% | -3,11% | +2,85% | FEEDBACK RAPIDO |
| SOL | 5g | Tecnico | CALIBRABILE | 10 | 20,00% | -0,12% | -1,53% | -3,05% | +2,88% | FEEDBACK RAPIDO |
| SOL | 5g | Classic technical | CALIBRABILE | 3 | 0,00% | +3,16% | -3,16% | -1,17% | +4,21% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 7 | 42,86% | -0,16% | -1,54% | -4,05% | +2,83% | FEEDBACK RAPIDO |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 6 | 83,33% | -0,86% | +0,97% | -4,37% | +2,44% | FEEDBACK RAPIDO |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 8 | 75,00% | -0,55% | +0,64% | -4,11% | +2,66% | FEEDBACK RAPIDO |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 6 | 66,67% | -0,43% | -0,08% | -4,16% | +2,70% | FEEDBACK RAPIDO |
| SOL | 7g | Tecnico | CALIBRABILE | 8 | 12,50% | -0,55% | -1,99% | -4,11% | +2,66% | FEEDBACK RAPIDO |
| SOL | 7g | Classic technical | CALIBRABILE | 1 | 0,00% | +1,50% | -1,50% | -3,42% | +3,59% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 4 | 25,00% | +0,19% | -1,19% | -4,87% | +2,44% | FEEDBACK RAPIDO |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 4 | 50,00% | -0,49% | +0,49% | -4,84% | +2,47% | FEEDBACK RAPIDO |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 5 | 40,00% | -0,28% | +0,28% | -5,00% | +2,26% | FEEDBACK RAPIDO |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 4 | 25,00% | +0,19% | -1,19% | -4,87% | +2,44% | FEEDBACK RAPIDO |
| SOL | 10g | Tecnico | CALIBRABILE | 5 | 40,00% | -0,28% | -0,69% | -5,00% | +2,26% | FEEDBACK RAPIDO |
| SOL | 10g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 14g | Global confluence | BENCHMARK | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 14g | Famiglia statistica | CALIBRABILE | 1 | 100,00% | -1,13% | +1,13% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 14g | Scanner grezzo | DIAGNOSTICO | 1 | 100,00% | -1,13% | +1,13% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 14g | Market regime grezzo | DIAGNOSTICO | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 14g | Tecnico | CALIBRABILE | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | FEEDBACK RAPIDO |
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

Generato: 2026-07-23 07:38 UTC

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
| BTC | 15 | FEEDBACK RAPIDO | 14 | 0 | 0 | 0 | Famiglia statistica | 1g | 42,86% | +0,16% | feedback rapido: utile da osservare, non da pesare |
| SOL | 15 | FEEDBACK RAPIDO | 14 | 0 | 0 | 0 | Tecnico | 1g | 57,14% | -0,21% | feedback rapido: utile da osservare, non da pesare |
| DOGE | 15 | FEEDBACK RAPIDO | 14 | 0 | 0 | 0 | Famiglia statistica | 1g | 57,14% | +0,16% | feedback rapido: utile da osservare, non da pesare |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Famiglia statistica | 14 | 42,86% | +0,16% | +0,16% | -0,02% | +0,87% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Microstruttura exchange | 1 | 100,00% | +2,00% | +2,00% | +1,48% | +2,25% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 11 | 27,27% | -0,84% | +0,18% | -0,02% | +0,90% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Famiglia statistica | 13 | 53,85% | +0,55% | +0,55% | +0,04% | +1,66% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Microstruttura exchange | 1 | 100,00% | +3,18% | +3,18% | +3,05% | +3,89% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 11 | 36,36% | -0,57% | +0,67% | +0,09% | +1,71% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Famiglia statistica | 12 | 75,00% | +0,78% | +0,78% | -0,94% | +2,41% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Microstruttura exchange | 1 | 100,00% | +1,88% | +1,88% | +1,44% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 11 | 36,36% | -0,21% | +1,01% | -0,84% | +2,54% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 10 | 60,00% | +1,32% | +1,32% | -1,90% | +3,11% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 9 | 33,33% | -1,13% | +1,35% | -1,75% | +3,23% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 8 | 75,00% | +1,73% | +1,73% | -2,36% | +3,53% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 7 | 57,14% | -0,21% | +2,03% | -2,23% | +3,67% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 5 | 100,00% | +2,63% | +2,63% | -2,65% | +3,95% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 4 | 50,00% | +0,84% | +3,16% | -2,49% | +4,30% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Famiglia statistica | 1 | 100,00% | +3,42% | +3,42% | -2,32% | +5,81% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 1 | 0,00% | -3,42% | +3,42% | -2,32% | +5,81% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 13 | 53,85% | +0,08% | -0,08% | -0,35% | +0,64% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Famiglia statistica | 14 | 57,14% | +0,16% | -0,16% | -0,44% | +0,63% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 14 | 57,14% | +0,16% | -0,16% | -0,44% | +0,63% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Classic technical | 12 | 50,00% | -0,07% | +0,07% | -0,59% | +1,60% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Famiglia statistica | 13 | 53,85% | +0,12% | -0,12% | -0,72% | +1,32% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 13 | 53,85% | +0,12% | -0,12% | -0,72% | +1,32% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Classic technical | 11 | 45,45% | +0,10% | -0,10% | -1,45% | +2,13% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Famiglia statistica | 12 | 50,00% | +0,27% | -0,27% | -1,53% | +2,00% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 12 | 50,00% | +0,27% | -0,27% | -1,53% | +2,00% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Classic technical | 9 | 55,56% | +0,17% | -0,17% | -2,34% | +2,57% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 10 | 60,00% | +0,44% | -0,44% | -2,49% | +2,36% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 10 | 60,00% | +0,44% | -0,44% | -2,49% | +2,36% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Classic technical | 7 | 71,43% | +0,77% | -0,77% | -2,68% | +2,89% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 8 | 75,00% | +0,80% | -0,80% | -2,83% | +2,60% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 8 | 75,00% | +0,80% | -0,80% | -2,83% | +2,60% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Classic technical | 5 | 60,00% | +0,88% | -0,88% | -2,94% | +2,99% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 5 | 60,00% | +0,88% | -0,88% | -2,94% | +2,99% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 5 | 60,00% | +0,88% | -0,88% | -2,94% | +2,99% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Classic technical | 1 | 100,00% | +0,77% | -0,77% | -2,58% | +3,59% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Famiglia statistica | 1 | 100,00% | +0,77% | -0,77% | -2,58% | +3,59% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 1 | 100,00% | +0,77% | -0,77% | -2,58% | +3,59% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Classic technical | 6 | 66,67% | -0,34% | +0,34% | +0,13% | +1,09% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Famiglia statistica | 10 | 70,00% | +0,18% | -0,68% | -0,84% | +0,27% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 1 | 0,00% | -0,51% | -0,51% | -0,47% | +0,31% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 14 | 57,14% | -0,21% | -0,05% | -0,37% | +0,81% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Classic technical | 5 | 20,00% | -1,30% | +1,30% | +1,03% | +1,98% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Famiglia statistica | 9 | 44,44% | -0,55% | -0,46% | -1,26% | +0,85% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Microstruttura exchange | 1 | 0,00% | -1,38% | -1,38% | -1,57% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 13 | 23,08% | -0,82% | -0,06% | -0,70% | +1,48% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Classic technical | 5 | 0,00% | -1,89% | +1,89% | -0,57% | +2,88% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Famiglia statistica | 8 | 37,50% | -0,53% | -0,32% | -2,37% | +1,91% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 12 | 25,00% | -0,98% | -0,01% | -1,77% | +2,41% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Classic technical | 3 | 0,00% | -3,16% | +3,16% | -1,17% | +4,21% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 7 | 57,14% | -0,10% | -0,47% | -3,49% | +2,44% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 10 | 20,00% | -1,53% | -0,12% | -3,05% | +2,88% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Classic technical | 1 | 0,00% | -1,50% | +1,50% | -3,42% | +3,59% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 6 | 83,33% | +0,97% | -0,86% | -4,37% | +2,44% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 8 | 12,50% | -1,99% | -0,55% | -4,11% | +2,66% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 4 | 50,00% | +0,49% | -0,49% | -4,84% | +2,47% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 5 | 40,00% | -0,69% | -0,28% | -5,00% | +2,26% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Famiglia statistica | 1 | 100,00% | +1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Frattale SOL | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Tecnico | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 14 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 14 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 14 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Famiglia statistica | 39 | 56,41% | +0,48% |
| BTC | BREVE | Microstruttura exchange | 3 | 100,00% | +2,36% |
| BTC | BREVE | Tecnico | 33 | 33,33% | -0,54% |
| BTC | SETTIMANALE | Famiglia statistica | 23 | 73,91% | +1,75% |
| BTC | SETTIMANALE | Tecnico | 20 | 45,00% | -0,41% |
| BTC | SWING | Famiglia statistica | 1 | 100,00% | +3,42% |
| BTC | SWING | Tecnico | 1 | 0,00% | -3,42% |
| DOGE | BREVE | Classic technical | 36 | 50,00% | +0,03% |
| DOGE | BREVE | Famiglia statistica | 39 | 53,85% | +0,18% |
| DOGE | BREVE | Tecnico | 39 | 53,85% | +0,18% |
| DOGE | SETTIMANALE | Classic technical | 21 | 61,90% | +0,54% |
| DOGE | SETTIMANALE | Famiglia statistica | 23 | 65,22% | +0,66% |
| DOGE | SETTIMANALE | Tecnico | 23 | 65,22% | +0,66% |
| DOGE | SWING | Classic technical | 1 | 100,00% | +0,77% |
| DOGE | SWING | Famiglia statistica | 1 | 100,00% | +0,77% |
| DOGE | SWING | Tecnico | 1 | 100,00% | +0,77% |
| SOL | BREVE | Classic technical | 16 | 31,25% | -1,13% |
| SOL | BREVE | Famiglia statistica | 27 | 51,85% | -0,27% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 2 | 0,00% | -0,95% |
| SOL | BREVE | Tecnico | 39 | 35,90% | -0,65% |
| SOL | SETTIMANALE | Classic technical | 4 | 0,00% | -2,74% |
| SOL | SETTIMANALE | Famiglia statistica | 17 | 64,71% | +0,41% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Tecnico | 23 | 21,74% | -1,51% |
| SOL | SWING | Famiglia statistica | 1 | 100,00% | +1,13% |
| SOL | SWING | Frattale SOL | 1 | 0,00% | -1,13% |
| SOL | SWING | Tecnico | 1 | 0,00% | -1,13% |

## Aree ancora in attesa

| Asset | Famiglia | Righe senza controlli | Stato |
| --- | --- | --- | --- |
| BTC | BREVE | 6 | in attesa di controlli maturati |
| BTC | SETTIMANALE | 9 | in attesa di controlli maturati |
| BTC | SWING | 8 | in attesa di controlli maturati |
| BTC | MEDIO | 15 | in attesa di controlli maturati |
| SOL | BREVE | 1 | in attesa di controlli maturati |
| SOL | SETTIMANALE | 4 | in attesa di controlli maturati |
| SOL | SWING | 7 | in attesa di controlli maturati |
| SOL | MEDIO | 15 | in attesa di controlli maturati |
| DOGE | BREVE | 6 | in attesa di controlli maturati |
| DOGE | SETTIMANALE | 6 | in attesa di controlli maturati |
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
| BTC     |         15 |               0 |          15 | RACCOLTA DATI | n/a              | n/a             | n/a                   | n/a            |
| SOL     |         15 |               0 |          15 | RACCOLTA DATI | n/a              | n/a             | n/a                   | n/a            |
| DOGE    |         15 |               0 |          15 | RACCOLTA DATI | n/a              | n/a             | n/a                   | n/a            |

Regola: sotto 60 controlli osserva soltanto; da 100+ controlli può diventare utile per correggere rischio spot/leva nel Decision Report.

## Ultima lettura rapida

| Asset   | Rischio spot   | Rischio leva   | Nota leva                                                               |
|:--------|:---------------|:---------------|:------------------------------------------------------------------------|
| BTC     | MEDIO          | MOLTO ALTO     | spot/tranche; se proprio leva, massimo 2x con margine molto largo       |
| SOL     | MEDIO          | MOLTO ALTO     | spot/tranche; se proprio leva, massimo 2x con margine molto largo       |
| DOGE    | ALTO           | MOLTO ALTO     | spot preferibile; leva molto pericolosa anche 2x/3x senza margine largo |
<!-- RISK_CALIBRATION_END -->

</details>
<!-- COMPACT_SECTION_END:risk_calibration -->

<!-- COMPACT_SECTION_START:global_confluence -->
<details open>
<summary><strong>🌐 Global Confluence — quadro finale</strong></summary>

<!-- GLOBAL_CONFLUENCE_START -->
# Sintesi finale di confluenza

Generato: 2026-07-23 07:38 UTC


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
| BTC | +1 | MISTA / PARZIALE | Neutrale / misto | BASSA / RACCOLTA DATI | HOLD / ATTESA CONFERME | Prima resistenza sopra 65.508; conferma del doppio minimo sopra 67.248. | Sotto 57.748 il quadro tecnico peggiora. |
| SOL | +1 | MISTA / PARZIALE | Neutrale / misto | BASSA / RACCOLTA DATI | HOLD LEGGERO / ATTESA CONFERME | Doppio minimo maturo finché mantiene 75,94; nuova conferma tecnica sopra 78,88; milestone analogiche 103,59 / 112,92, valide soltanto se rientra anche il gap frattale. | Allarmi sotto 73,25 / 73,40 / 62,19. |
| DOGE | -3 | DEBOLE / FRAGILE | Fragile | MEDIA | EVITA LONG / SOLO RIMBALZI VELOCI | Sopra 0.07923 migliora; sopra 0.07966 viene invalidato il pattern ribassista dominante. | Sotto 0.07097 il rischio ribassista aumenta. |

## Punteggi per modulo

| Asset | Scanner grezzo | Market grezzo | Famiglia statistica | Scanner path | Tecnico | Classic tech | Frattale SOL | Fractal path | RSI top-cycle | Lifecycle EMA | Exchange flow | Futures | Daily change | Totale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +2 | +3 | +2 | 0 | -1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | +1 |
| SOL | +2 | +2 | +3 | 0 | -2 | -1 | 0 | 0 | 0 | 0 | 0 | 0 | +1 | +1 |
| DOGE | -1 | 0 | -1 | 0 | -2 | -1 | 0 | 0 | 0 | 0 | 0 | 0 | +1 | -3 |

Le colonne **Scanner grezzo** e **Market grezzo** sono diagnostiche: nel totale entra soltanto la colonna **Famiglia statistica**.

## Lettura asset per asset

### BTC

- Confluenza: **MISTA / PARZIALE**
- Bias: **Neutrale / misto**
- Punteggio finale: **+1**
- Affidabilità: **BASSA / RACCOLTA DATI**
- Azione coerente: **HOLD / ATTESA CONFERME**

BTC è in fase mista. Non è abbastanza debole da autorizzare short semplici, ma non ha ancora una conferma piena.

Dettaglio moduli:

- Famiglia statistica: **+2** — Scanner grezzo +2, Market Regime grezzo +3, match regime 7. Scanner e regime concordi, ma i match sono meno di 10: nessun bonus. Punteggio contato nel Global: +2.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **+2** — Casi positivi 62,50%, return centrale 30g +10,04%. Direzione scanner: SALITA. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **+3** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 7, positivi 30g 85,71%, return p50 +6,86%.
- Scanner path: **0** — Controlli disponibili 13. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **-1** — Score tecnico -2/12, verdetto neutrale / misto, trend misto, struttura ribassista con massimi e minimi decrescenti, divergenza rialzista rsi, ribassista nascosta rsi, Wyckoff markdown / fase ribassista, pattern score 0 (rialzista Doppio minimo / CANDIDATO; ribassista Doppio massimo / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **0** — Score classico -1/12, verdetto NEUTRALE / MISTO, stage STAGE 4 / MARKDOWN, struttura MASSIMI E MINIMI CRESCENTI, Wyckoff ACCUMULO POSSIBILE / RANGE BASSO, volatilità locale BASSO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Non applicabile a questo asset.
- Fractal path: **0** — Non applicabile a questo asset.
- RSI top-cycle: **0** — Non applicabile a questo asset.
- Lifecycle EMA: **0** — Non applicabile a questo asset.
- Exchange flow: **0** — Flow +1.75, derivati +0.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +1.00; exchange 3/3, copertura 100%, consenso bull 0, bear 1, divergenze 1, campioni 4h 8 su 4.00h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias LEGGERMENTE POSITIVA / NON PESATA; confidenza MEDIA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Misto, forza 2/5.
- Daily change: **0** — BTC: nessun cambiamento forte in miglioramento rispetto a ieri.

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

- Famiglia statistica: **+3** — Scanner grezzo +2, Market Regime grezzo +2, match regime 22. Scanner e regime concordi con almeno 10 match: bonus massimo di 1 punto. Punteggio contato nel Global: +3.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **+2** — Casi positivi 62,50%, return centrale 30g +3,79%. Direzione scanner: SALITA. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **+2** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 22, positivi 30g 68,18%, return p50 +4,57%.
- Scanner path: **0** — Controlli disponibili 13. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **-2** — Score tecnico -6/12, verdetto debole, trend ribassista, struttura compressione / triangolo, divergenza nessuna, Wyckoff markdown / fase ribassista, pattern score +1 (rialzista Doppio minimo / MATURO; ribassista Doppio massimo / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **-1** — Score classico -6/12, verdetto RIBASSISTA / FRAGILE, stage STAGE 4 / MARKDOWN, struttura MASSIMI E MINIMI DECRESCENTI, Wyckoff ACCUMULO POSSIBILE / RANGE BASSO, volatilità locale BASSO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Verdetto ANALOGIA DEBOLE / SCENARIO SECONDARIO, somiglianza strutturale +64,77%, aderenza live +63,56%, errore live +18,22%, gap corrente +15,45%, peso operativo 0, tracking STRUTTURA STABILE, fase FRATTALE SOLO DI CONTESTO, rischio ALTO.
- Fractal path: **0** — Controlli disponibili 9, ma percorso ancorato non aderente: gap +15,45%, errore live +18,22%. Peso 0.
- RSI top-cycle: **0** — Rischio top-cycle RSI: BASSO.
- Lifecycle EMA: **0** — Contesto non pesato nel Global. Lifecycle score 4, bias SQUEEZE SETUP MODERATO, EMA200 112,77 $, upside EMA200 +46,23%, gap EMA50/EMA200 -3,02%, hit EMA200 12w +30,00%, trend STABILE / DA CONFERMARE. Peso Global forzato a 0.
- Exchange flow: **0** — Flow +1.75, derivati +0.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +1.00; exchange 3/3, copertura 100%, consenso bull 1, bear 0, divergenze 0, campioni 4h 8 su 4.00h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias LEGGERMENTE POSITIVA / NON PESATA; confidenza MEDIA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Misto, forza 1/5.
- Daily change: **+1** — SOL: cambiamento forte in miglioramento rispetto a ieri.

Conferme: Doppio minimo maturo finché mantiene 75,94; nuova conferma tecnica sopra 78,88; milestone analogiche 103,59 / 112,92, valide soltanto se rientra anche il gap frattale.

Invalidazioni: Allarmi sotto 73,25 / 73,40 / 62,19.

### DOGE

- Confluenza: **DEBOLE / FRAGILE**
- Bias: **Fragile**
- Punteggio finale: **-3**
- Affidabilità: **MEDIA**
- Azione coerente: **EVITA LONG / SOLO RIMBALZI VELOCI**

DOGE non ha ancora una confluenza pulita. Serve conferma tecnica prima di trattarlo come asset forte.

Dettaglio moduli:

- Famiglia statistica: **-1** — Scanner grezzo -1, Market Regime grezzo 0, match regime 27. Regime neutro: resta il punteggio Scanner. Punteggio contato nel Global: -1.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **-1** — Casi positivi 47,50%, return centrale 30g -0,99%. Direzione scanner: INCERTO. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **0** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 27, positivi 30g 48,15%, return p50 -0,80%.
- Scanner path: **0** — Controlli disponibili 13. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **-2** — Score tecnico -6/12, verdetto debole, trend ribassista, struttura ribassista con massimi e minimi decrescenti, divergenza ribassista nascosta rsi, Wyckoff possibile accumulazione, pattern score -1 (rialzista Doppio minimo / CANDIDATO; ribassista Triplo massimo / MATURO). Fonte: technical_structure_metrics.csv.
- Classic technical: **-1** — Score classico -6/12, verdetto RIBASSISTA / FRAGILE, stage STAGE 4 / MARKDOWN, struttura COMPRESSIONE / TRIANGOLO POSSIBILE, Wyckoff MARKDOWN / DEBOLEZZA, volatilità locale BASSO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Non applicabile a questo asset.
- Fractal path: **0** — Non applicabile a questo asset.
- RSI top-cycle: **0** — Non applicabile a questo asset.
- Lifecycle EMA: **0** — Non applicabile a questo asset.
- Exchange flow: **0** — Flow +1.75, derivati +0.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +1.25; exchange 3/3, copertura 100%, consenso bull 0, bear 1, divergenze 0, campioni 4h 8 su 4.00h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias LEGGERMENTE POSITIVA / NON PESATA; confidenza MEDIA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Misto, forza 1/5.
- Daily change: **+1** — DOGE: cambiamento forte in miglioramento rispetto a ieri.

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

Generato: 2026-07-23 07:38 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [btc_macro_cycle_report.md](btc_macro_cycle_report.md)

Questo modulo descrive il contesto macro di Bitcoin. Non genera entrate tattiche, non autorizza leva e pesa **0** nel Global Confluence.

## Sintesi

| Voce | Valore | Lettura |
| --- | --- | --- |
| Prezzo BTC | 65.400 $ | prezzo corrente |
| Power Law centrale | 122.623 $ | deviazione -46,67% |
| Banda p10-p90 | 76.332 $ / 307.787 $ | SOTTO LA BANDA P10 |
| Percentile residuo | 2,54% | posizione storica nel corridoio |
| Esponente β | 5,8382 | R² log-log 91,98% |
| Stabilità β | BASSA | range 1,3080 cambiando finestra |
| Ultimo halving | 2024-04-19 | 825 giorni fa |
| Fase ciclo | 56,47% | percentuale indicativa del ciclo quadriennale |
| Peso Global | 0 | CONTESTO MACRO / DIAGNOSTICO |

La Power Law viene trattata come regressione empirica, non come legge fisica. Il report mostra quanto cambia l'esponente usando finestre iniziali diverse e la confronta con il benchmark ingenuo 'prezzo invariato'.

## Bitcoin Power Law

- Campione: 2014-09-17 → 2026-07-23 (4328 osservazioni)
- Formula stimata: prezzo ≈ exp(-39.3381) × giorni^5.8382
- Prezzo centrale oggi: **122.623 $**
- Posizione corrente: **SOTTO LA BANDA P10**, percentile 2,54%
- Scarto dal centro: **-46,67%**

![Bitcoin Power Law](btc_power_law_chart.png)

![Bitcoin Power Law log-log](btc_power_law_loglog_chart.png)

### Stabilità dell'esponente

| Inizio campione | β | R² log-log |
| --- | --- | --- |
| 2014 | 5,8382 | 91,98% |
| 2015 | 5,9245 | 91,55% |
| 2016 | 5,6138 | 87,79% |
| 2017 | 4,8834 | 82,88% |
| 2018 | 4,6165 | 78,35% |

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
| 2012-11-28 → 2016-07-09 | 2014-12-13 | -22,91% | -17,86% | -33,87% | +24,87% |
| 2016-07-09 → 2020-05-11 | 2018-09-09 | +5,42% | -44,83% | -38,09% | +64,02% |
| 2020-05-11 → 2024-04-19 | 2022-08-02 | -12,41% | -10,80% | +3,47% | +26,87% |

Campione molto piccolo: questi rendimenti sono contesto di ciclo, non probabilità affidabili.

## SOL/BTC e DOGE/BTC dentro il tempo Bitcoin

![Altcoin nel ciclo BTC](alt_btc_cycle_spirals.png)

| Asset | Coppia | Forza vs BTC | Score raw | Candidato | 30g | Peso Global |
| --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | RELATIVA MISTA / NON CONFERMATA | -1 | 0 | 6.1116159966603245 | 0 |
| DOGE | DOGE/BTC | SOTTOPERFORMA BTC | -6 | -1 | -12.151510600062021 | 0 |

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

Generato: 2026-07-23 07:38 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [relative_strength_btc_report.md](relative_strength_btc_report.md)

Questo modulo controlla se SOL e DOGE stanno davvero battendo Bitcoin. Una salita in USD accompagnata da una coppia ALT/BTC ribassista è spesso soltanto trascinamento di BTC.

**Protezione iniziale:** il candidato relativo è limitato a -1/0/+1, ma il peso nel Global resta **0**. La coppia BTC conferma o indebolisce il tecnico USD; non viene sommata come secondo modulo indipendente.

## Sintesi

| Asset | Coppia | Prezzo | Score raw | Candidato | Peso Global | Forza vs BTC | Confidenza | 30g | Tecnico USD | Lettura combinata |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | 0.00117890 | -1 | 0 | 0 | RELATIVA MISTA / NON CONFERMATA | BASSA | +6,11% | RIBASSISTA | QUADRO MISTO / NESSUNA CONFERMA RELATIVA |
| DOGE | DOGE/BTC | 0.00000111 | -6 | -1 | 0 | SOTTOPERFORMA BTC | MEDIA | -12,15% | RIBASSISTA | DEBOLEZZA COMPLETA: scende in USD e contro BTC |

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
- **Rendimenti relativi:** 7g -0,09%; 30g +6,11%; 90g +5,92%; 180g -17,33%
- **Daily:** RSI 45.42; MA50 0.00116300; MA200 0.00121819
- **Weekly:** MA30 0.00122036; RSI 45.88
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
- **Rendimenti relativi:** 7g -2,55%; 30g -12,15%; 90g -13,05%; 180g -20,64%
- **Daily:** RSI 23.49; MA50 0.00000124; MA200 0.00000134
- **Weekly:** MA30 0.00000134; RSI 30.50
- **Livelli:** supporto 0.00000110; resistenza 0.00000121; breakout 60g 0.00000153; breakdown 60g 0.00000108
- **Pattern:** DOPPIO MASSIMO / CONFERMATO; neckline 0.00000112; target 0.00000099
- **Fibonacci:** NON ATTIVO — 23.6% a 0.00000118
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
| DOGE | 7g | 291 | 56,01% | +1,86% | -1,77% |
| DOGE | 30g | 287 | 52,61% | +1,98% | -3,49% |
| DOGE | 90g | 285 | 54,04% | +6,94% | -8,47% |

## Tracker live e gate futuro

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto | Stato | Peso Global |
| --- | --- | --- | --- | --- | --- | --- |
| SOL | 1g | 0 | n/a | n/a | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 3g | 0 | n/a | n/a | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 7g | 0 | n/a | n/a | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 14g | 0 | n/a | n/a | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 30g | 0 | n/a | n/a | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 1g | 12 | 83,33% | +0,85% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 3g | 10 | 90,00% | +1,70% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 7g | 6 | 100,00% | +3,59% | LOCKED / RACCOLTA LIVE | 0 |
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

Ultima candela SOL usata: **23 luglio 2026**

## Verdetto: ANALOGIA DEBOLE / SCENARIO SECONDARIO

- **Fase attuale:** FRATTALE SOLO DI CONTESTO
- **Somiglianza totale:** +64,77%
- **Somiglianza strutturale:** +64,77%
- **Aderenza prezzo live:** +63,56%
- **Errore medio live:** +18,22%
- **Gap prezzo corrente:** +15,45%
- **Peso operativo suggerito:** 0
- **Affidabilita:** BASSA
- **Rischio fase:** ALTO
- **Trend tracking:** STRUTTURA STABILE
- **Sintesi:** Esistono alcuni elementi comuni, ma non abbastanza per una conferma.
- **SOL è al giorno:** 47 dal bottom usato.
- **Giorno BTC equivalente:** 2023-01-07
- **Prossimo step:** Proiezione condizionale, non conferma operativa: **Spinta rialzista abbastanza pulita.** Zona bassa **77,11 $** intorno al **23 luglio 2026**; zona alta **103,59 $** intorno al **6 agosto 2026**; fine step circa **103,59 $** entro il **6 agosto 2026**.

## Somiglianza prima e dopo inizio programma

Questa sezione separa la somiglianza della forma dall'aderenza reale del prezzo.

- **Inizio programma/scanner:** 3 luglio 2026
- **Prima del programma** = backtest retroattivo.
- **Da inizio programma** = verifica live: è la parte più importante per l'uso operativo.

| Periodo | Date | Giorni | Aderenza prezzo | Errore medio | Gap ultimo | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| Prima del programma | 6 giugno 2026 -> 2 luglio 2026 | 27 | +87,95% | +6,02% | +21,89% | ABBASTANZA ALLINEATO |
| Da inizio programma | 3 luglio 2026 -> 23 luglio 2026 | 21 | +63,56% | +18,22% | +15,45% | STACCATO / NON ADERENTE |
| Totale dal bottom | 6 giugno 2026 -> 23 luglio 2026 | 48 | +77,28% | +11,36% | +15,45% | DEVIAZIONE MODERATA |

Nota: un frattale può avere una forma simile ma un prezzo distante. In quel caso non è operativo finché il gap non rientra.

## Lettura operativa veloce

Il frattale non deve generare acquisti o leva adesso. La forma è un contesto, ma l'aderenza live del prezzo è insufficiente.

| Voce | Risposta | Perché |
| --- | --- | --- |
| Uso operativo | NO | Il frattale vale 0 punti operativi finché il prezzo resta non aderente. |
| Aderenza live | +63,56% | Errore medio live +18,22%. |
| Gap corrente | +15,45% | Deve rientrare circa entro ±12%. |
| Prima conferma prezzo | 103,59 $ | Serve anche miglioramento del gap, non solo una candela sopra il livello. |
| Seconda conferma | 112,92 $ | Rende più credibile il percorso, ma non sostituisce l'aderenza. |
| Invalidazione soft | 73,25 $ | Sotto questa zona il quadro peggiora. |
| Invalidazione forte | 62,19 $ | Sotto il bottom il paragone è quasi rotto. |

## Target ciclo fino al top BTC 2025

| Voce | Valore |
| --- | --- |
| Stato | CONTESTO / NON OPERATIVO |
| Top BTC 2025 | 6 ottobre 2025 - 124.753 $ |
| Data SOL equivalente | 21 aprile 2029 |
| Target ciclo base da oggi | 567,36 $ |
| Massimo percorso base | 567,36 $ (21 aprile 2029) |

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
| Prima conferma | 103,59 $ | Deve accompagnarsi al rientro del gap. |
| Seconda conferma | 112,92 $ | Scenario più credibile. |
| Invalidazione soft | 73,25 $ | Il frattale si indebolisce. |
| Invalidazione forte | 62,19 $ | Il paragone si rompe. |

## Proiezione veloce con date SOL

| Orizzonte | Data SOL | BTC fece | SOL base | Min percorso | Max percorso |
| --- | --- | --- | --- | --- | --- |
| 7 giorni | 30 luglio 2026 | +23,72% | 95,40 $ | 77,11 $ | 95,40 $ |
| 14 giorni | 6 agosto 2026 | +34,34% | 103,59 $ | 77,11 $ | 103,59 $ |
| 30 giorni | 22 agosto 2026 | +34,24% | 103,51 $ | 77,11 $ | 108,12 $ |
| 60 giorni | 21 settembre 2026 | +28,09% | 98,77 $ | 77,11 $ | 112,92 $ |
| 90 giorni | 21 ottobre 2026 | +64,70% | 127,00 $ | 77,11 $ | 129,52 $ |
| 120 giorni | 20 novembre 2026 | +67,83% | 129,41 $ | 77,11 $ | 138,65 $ |

## Prossimi step se SOL segue BTC 2022

| Step | Date SOL | BTC fine | SOL zona bassa | SOL zona alta | SOL fine base | Lettura |
| --- | --- | --- | --- | --- | --- | --- |
| Step 1 - prossime 2 settimane | 23 luglio 2026 -> 6 agosto 2026 | +34,34% | 77,11 $ (23 luglio 2026) | 103,59 $ (6 agosto 2026) | 103,59 $ | Spinta rialzista abbastanza pulita. |
| Step 2 - primo mese | 7 agosto 2026 -> 22 agosto 2026 | +34,24% | 102,95 $ (9 agosto 2026) | 108,12 $ (14 agosto 2026) | 103,51 $ | Spinta rialzista abbastanza pulita. |
| Step 3 - secondo mese | 23 agosto 2026 -> 21 settembre 2026 | +28,09% | 98,47 $ (26 agosto 2026) | 112,92 $ (5 settembre 2026) | 98,77 $ | Spinta rialzista abbastanza pulita. |
| Step 4 - terzo mese | 22 settembre 2026 -> 21 ottobre 2026 | +64,70% | 91,81 $ (23 settembre 2026) | 129,52 $ (14 ottobre 2026) | 127,00 $ | Spinta rialzista abbastanza pulita. |

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
| Prezzo SOL | 77,11 $ |  |
| Weekly RSI | 40,42 / linea grezza 53,89 | LINEA NON AFFIDABILE / RISCHIO NON ATTIVO — IRREALISTICA / NON OPERATIVA |
| Monthly RSI | 41,20 / linea grezza 56,16 | RSI TROPPO BASSO PER RISCHIO TOP — VALIDA / USO PRUDENTE |
| Target ciclo base | 567,36 $ | Avanzamento +13,59% |
| Rischio top-cycle RSI | BASSO | Nessun segnale top-cycle macro attivo. Prezzo ancora lontano dal target ciclo; il filtro RSI resta solo di monitoraggio. |

## Lettura semplice

- Weekly: La top-line weekly non supera i controlli di qualità. Non viene usata per generare rischio top-cycle.
- Monthly: RSI monthly è 41,2, sotto la soglia prudente 55. Anche se fosse vicino alla linea, non è una vera zona di esaurimento ciclo.
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
| Prezzo SOL | 77,11 $ |
| TVL Solana | 4,99 mld $ |
| TVL 7g | +1,47% |
| DEX volume 24h | 1,72 mld $ |
| Fees 24h | 8,67 mln $ |
| Stablecoin su Solana | 16,97 mld $ |
| Stake ratio | 67,81% |
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
| Prezzo SOL | 77,11 $ |
| EMA200 weekly target | 112,77 $ |
| Upside verso EMA200 | +46,23% |
| Distanza prezzo da EMA200 | -31,61% |
| Gap EMA50/EMA200 | -3,02% |
| Stato cross | EMA50 SOTTO EMA200 |
| RSI weekly | 40,43 |
| Età SOL | 6,3 anni |
| Analoghi storici usati | 30 |
| Max analoghi per asset | 3 |
| Hit EMA200 12w analoghi | +30,00% |
| Max gain mediano 12w | +22,38% |
| Drawdown mediano 12w | -20,34% |

Lettura semplice:

**CONTESTO INTERESSANTE, SERVONO CONFERME DI PREZZO**

Autocontrollo: **STABILE / DA CONFERMARE**.

Questo modulo confronta SOL con altre crypto in fasi simili di età, distanza da EMA200, EMA50/EMA200 e RSI. Non usa stock market.

Nota importante: **questo modulo ora NON pesa più nel Global Confluence**. Resta solo come contesto di ciclo e come mappa verso EMA200 weekly. Il punteggio Global resta guidato da prezzo, scanner, regime, struttura tecnica, frattale, RSI e conferme reali.

Nota: se EMA50/EMA200 sono dentro ±2%, il modulo parla di medie sovrapposte / incrocio in corso, perché exchange diversi possono mostrare il cross leggermente prima o dopo.

<!-- Generato: 2026-07-23 07:37 UTC -->
<!-- MAJOR_ALT_LIFECYCLE_SQUEEZE_END -->

</details>
<!-- COMPACT_SECTION_END:major_alt_lifecycle -->

# Report giornaliero BTC / SOL / DOGE

Aggiornato il: **2026-07-23 07:35:30 UTC**

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
- DOGE: cambiamento importante in miglioramento rispetto a ieri.

| Asset | Cambio | Tono | Verdetto oggi | Casi positivi oggi | Δ casi positivi |
| --- | --- | --- | --- | --- | --- |
| BTC | NESSUN CAMBIAMENTO FORTE | miglioramento | RIALZISTA | +62.50% | +2.50 punti |
| SOL | CAMBIAMENTO FORTE | miglioramento | RIALZISTA | +62.50% | +15.00 punti |
| DOGE | CAMBIAMENTO FORTE | miglioramento | NEUTRALE / INCERTO | +47.50% | +10.00 punti |

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
| BTC | 62.130 $ | 71.940 $ | +51,43% | +15,79% | rimbalzo possibile | 71.940 $ | 62.130 $ | +8,70% | -13,64% | spike storicamente più resistente |
| SOL | 73,25 $ | 84,82 $ | +36,67% | +15,79% | rimbalzo debole | 84,82 $ | 73,25 $ | +15,00% | -13,64% | spike storicamente più resistente |
| DOGE | 0,06865 $ | 0,07949 $ | +27,27% | +15,79% | rimbalzo poco frequente | 0,07949 $ | 0,06865 $ | +52,00% | -13,64% | attenzione a prendere profitto |

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

- **BTC: su 40 casi simili, 35 prima sono scesi a -5,00%. Tra quei 35, 18 poi sono rimbalzati fino a +10,00%. Percentuale: +51,43% (18/35). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo possibile.**
- **BTC: su 40 casi simili, 23 prima sono saliti a +10,00%. Tra quei 23, 2 poi sono scaricati a -5,00%. Percentuale: +8,70% (2/23). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.**
- **SOL: su 40 casi simili, 30 prima sono scesi a -5,00%. Tra quei 30, 11 poi sono rimbalzati fino a +10,00%. Percentuale: +36,67% (11/30). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.**
- **SOL: su 40 casi simili, 20 prima sono saliti a +10,00%. Tra quei 20, 3 poi sono scaricati a -5,00%. Percentuale: +15,00% (3/20). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.**
- **DOGE: su 40 casi simili, 33 prima sono scesi a -5,00%. Tra quei 33, 9 poi sono rimbalzati fino a +10,00%. Percentuale: +27,27% (9/33). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.**
- **DOGE: su 40 casi simili, 25 prima sono saliti a +10,00%. Tra quei 25, 13 poi sono scaricati a -5,00%. Percentuale: +52,00% (13/25). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: attenzione a prendere profitto.**

<!-- BOUNCE_AFTER_DRAWDOWN_END -->

</details>
<!-- COMPACT_SECTION_END:bounce_after_drawdown -->

<!-- COMPACT_SECTION_START:scanner_forecast -->
<details>
<summary><strong>🔭 Cono probabilistico dello scanner</strong></summary>

<!-- SCANNER_FORECAST_TRACKER_START -->
# Scanner forecast path / cono probabilistico

Generato: 2026-07-23 07:37:02 UTC


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
| BTC | 2026-07-23 | 65.400 $ | SALITA | 62,50% | 47.772,28 $ | 55.295,48 $ | 71.966,75 $ | 80.646,57 $ | 84.705,10 $ |
| SOL | 2026-07-23 | 77,11 $ | SALITA | 62,50% | 64,58 $ | 71,73 $ | 80,03 $ | 89,31 $ | 100,25 $ |
| DOGE | 2026-07-23 | 0.07226 $ | INCERTO | 47,50% | 0.05167 $ | 0.06211 $ | 0.07155 $ | 0.08108 $ | 0.09241 $ |

## Grafici

### BTC

![Scanner forecast BTC](scanner_forecast_BTC.png)

#### Verifica storica e discrepanza

![Verifica storica cono BTC](scanner_forecast_history_BTC.png)

- Cono congelato il **2026-07-10**; verificato fino al **2026-07-23**; stato **PARZIALE 13/30g**.
- Reale **65.394,85 $**; p50 previsto **66.948,28 $**; scarto **-2,32%**.
- Errore medio assoluto **3,70%**; massimo **7,75%**; DENTRO p10-p90; DENTRO p25-p75.

### SOL

![Scanner forecast SOL](scanner_forecast_SOL.png)

#### Verifica storica e discrepanza

![Verifica storica cono SOL](scanner_forecast_history_SOL.png)

- Cono congelato il **2026-07-10**; verificato fino al **2026-07-23**; stato **PARZIALE 13/30g**.
- Reale **77,13 $**; p50 previsto **74,86 $**; scarto **3,04%**.
- Errore medio assoluto **2,91%**; massimo **5,38%**; DENTRO p10-p90; DENTRO p25-p75.

### DOGE

![Scanner forecast DOGE](scanner_forecast_DOGE.png)

#### Verifica storica e discrepanza

![Verifica storica cono DOGE](scanner_forecast_history_DOGE.png)

- Cono congelato il **2026-07-10**; verificato fino al **2026-07-23**; stato **PARZIALE 13/30g**.
- Reale **0.07228 $**; p50 previsto **0.05969 $**; scarto **21,09%**.
- Errore medio assoluto **4,45%**; massimo **21,09%**; DENTRO p10-p90; FUORI p25-p75.

## Accuratezza percorso scanner

| Asset   | Giorno   |   Controlli | Dentro p10-p90   | Dentro p25-p75   | Errore medio abs vs p50   | Errore medio vs p50   |
|:--------|:---------|------------:|:-----------------|:-----------------|:--------------------------|:----------------------|
| BTC | 1g | 13 | 100,00% | 69,23% | 1,93% | 0,19% |
| BTC | 3g | 11 | 100,00% | 54,55% | 3,09% | -0,46% |
| BTC | 7g | 7 | 100,00% | 71,43% | 3,00% | -0,99% |
| BTC | 14g | 0 | n/a | n/a | n/a | n/a |
| BTC | 30g | 0 | n/a | n/a | n/a | n/a |
| SOL | 1g | 13 | 76,92% | 53,85% | 2,32% | 0,16% |
| SOL | 3g | 11 | 100,00% | 36,36% | 2,91% | 0,14% |
| SOL | 7g | 7 | 100,00% | 100,00% | 2,54% | 0,50% |
| SOL | 14g | 0 | n/a | n/a | n/a | n/a |
| SOL | 30g | 0 | n/a | n/a | n/a | n/a |
| DOGE | 1g | 13 | 100,00% | 61,54% | 2,44% | 1,16% |
| DOGE | 3g | 11 | 100,00% | 90,91% | 2,47% | 1,17% |
| DOGE | 7g | 7 | 100,00% | 85,71% | 6,39% | 6,39% |
| DOGE | 14g | 0 | n/a | n/a | n/a | n/a |
| DOGE | 30g | 0 | n/a | n/a | n/a | n/a |

## Calibratore shadow

Il cono ufficiale resta grezzo e invariato. Il calibratore usa soltanto previsioni passate già mature, campionate una volta a settimana per ridurre la falsa indipendenza. Ogni orizzonte si attiva a 30 controlli indipendenti: parte al 25% della correzione stimata e cresce gradualmente fino al 100% a 100 controlli.

| Asset   | Orizzonte   |   Controlli indipendenti |   Soglia | Stato                  | Forza correzione   | Shift p50   |   Scala p10-p90 |
|:--------|:------------|-------------------------:|---------:|:-----------------------|:-------------------|:------------|----------------:|
| BTC | 1g | 3 | 30 | RACCOLTA (27 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 3g | 3 | 30 | RACCOLTA (27 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 7g | 2 | 30 | RACCOLTA (28 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 14g | 0 | 30 | RACCOLTA (30 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 30g | 0 | 30 | RACCOLTA (30 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 1g | 3 | 30 | RACCOLTA (27 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 3g | 3 | 30 | RACCOLTA (27 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 7g | 2 | 30 | RACCOLTA (28 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 14g | 0 | 30 | RACCOLTA (30 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 30g | 0 | 30 | RACCOLTA (30 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 1g | 3 | 30 | RACCOLTA (27 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 3g | 3 | 30 | RACCOLTA (27 mancanti) | 0,0% | 0,00% | 1,000 |
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

Righe salvate nello storico: **33**.

Questa sezione tiene un diario delle previsioni giornaliere a 30 giorni, senza appesantire il report principale.

| Data | Asset | Prezzo | Direzione | Casi positivi | Return p50 | Drawdown p50 | Max gain p50 | Controllo 30g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-07-23 | BTC | 65.400 $ | SALITA | 62,50% | 71.967 $ | 57.984 $ | 74.464 $ | 2026-08-22 |
| 2026-07-23 | DOGE | 0,07000 $ | INCERTO | 47,50% | 0,07000 $ | 0,06000 $ | 0,08000 $ | 2026-08-22 |
| 2026-07-23 | SOL | 77,11 $ | SALITA | 62,50% | 80,03 $ | 70,43 $ | 85,06 $ | 2026-08-22 |

<!-- FORECAST_30D_HISTORY_END -->

</details>
<!-- COMPACT_SECTION_END:scanner_forecast -->

<!-- COMPACT_SECTION_START:extreme_cases -->
<details>
<summary><strong>⚠️ Percorso dei casi estremi</strong></summary>

<!-- EXTREME_CASES_PATH_START -->
# Extreme cases path report

Generato: 2026-07-23 07:37 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [extreme_cases_path_report.md](extreme_cases_path_report.md)

Questo report si attiva quando i casi positivi o negativi sono almeno **80%**.

Ora misura anche il **rialzo massimo prima della discesa principale**, quindi distingue uno spike iniziale da una discesa quasi immediata.

## Trigger estremi

| Asset   | Direzione   | Trigger   | Percentuale   | Motivo                           |   Match disponibili |
|:--------|:------------|:----------|:--------------|:---------------------------------|--------------------:|
| BTC     | NESSUNO     | NO        | +62,50%       | Nessun lato sopra soglia estrema |                  40 |
| SOL     | NESSUNO     | NO        | +62,50%       | Nessun lato sopra soglia estrema |                  40 |
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
- Casi positivi / salita storica: **62,50%**
- Casi negativi / discesa storica: **37,50%**
- Quanto è netto il segnale: **medio**
- Prezzo attuale: **65.399,99 $**
- Return normale fra 30 giorni: **71.966,75 $** (10,04%)
- Drawdown normale durante il mese: **57.984,06 $** (-11,34%)
- Drawdown brutto da rispettare: **52.125,30 $** (-20,30%)
- Max gain normale durante il mese: **74.464,18 $** (13,86%)
- Max gain buono / take profit ottimistico: **83.140,88 $** (27,13%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Solana
- Direzione più probabile a 30 giorni: **SALITA**
- Casi positivi / salita storica: **62,50%**
- Casi negativi / discesa storica: **37,50%**
- Quanto è netto il segnale: **medio**
- Prezzo attuale: **77,11 $**
- Return normale fra 30 giorni: **80,03 $** (3,79%)
- Drawdown normale durante il mese: **70,43 $** (-8,66%)
- Drawdown brutto da rispettare: **68,03 $** (-11,77%)
- Max gain normale durante il mese: **85,06 $** (10,31%)
- Max gain buono / take profit ottimistico: **94,61 $** (22,70%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Dogecoin
- Direzione più probabile a 30 giorni: **INCERTO**
- Casi positivi / salita storica: **47,50%**
- Casi negativi / discesa storica: **52,50%**
- Quanto è netto il segnale: **molto debole / quasi pari**
- Prezzo attuale: **0,07 $**
- Return normale fra 30 giorni: **0,07 $** (-0,99%)
- Drawdown normale durante il mese: **0,06 $** (-14,61%)
- Drawdown brutto da rispettare: **0,06 $** (-23,17%)
- Max gain normale durante il mese: **0,08 $** (13,74%)
- Max gain buono / take profit ottimistico: **0,09 $** (21,46%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Messaggio del giorno

Il quadro generale oggi è più favorevole. Lo scanner vede più possibilità di salita su più asset.

---

# Mappa semplice asset per asset

# Bitcoin — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟢 VERDE / Favorevole
**Prezzo attuale:** 65.399,99 $

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

- Se va molto male: **47.772,28 $** (-26,95%)
- Se va male: **55.295,48 $** (-15,45%)
- Scenario normale: **71.966,75 $** (10,04%)
- Se va bene: **80.646,57 $** (23,31%)
- Se va molto bene: **84.705,10 $** (29,52%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **57.984,06 $** (-11,34%)
- Discesa brutta: **52.125,30 $** (-20,30%)
- Discesa molto brutta: **46.576,08 $** (-28,78%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **74.464,18 $** (13,86%)
- Rialzo buono: **83.140,88 $** (27,13%)
- Rialzo molto forte: **87.018,18 $** (33,06%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Bitcoin tendeva a muoversi tra una zona bassa intorno a **57.984,06 $** e uno spike normale intorno a **74.464,18 $**.

La chiusura a 30 giorni era più spesso positiva: salita 62,50%, discesa 37,50%. Quindi la lettura principale è favorevole.

Nota leva BTC: se la liquidazione è vicina a 51.000 $, guarda soprattutto la discesa brutta e molto brutta. Il prezzo può recuperare dopo, ma la leva può saltare prima.

---

# Solana — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟢 VERDE / Favorevole
**Prezzo attuale:** 77,11 $

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

- Se va molto male: **64,58 $** (-16,25%)
- Se va male: **71,73 $** (-6,97%)
- Scenario normale: **80,03 $** (3,79%)
- Se va bene: **89,31 $** (15,82%)
- Se va molto bene: **100,25 $** (30,00%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **70,43 $** (-8,66%)
- Discesa brutta: **68,03 $** (-11,77%)
- Discesa molto brutta: **59,83 $** (-22,41%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **85,06 $** (10,31%)
- Rialzo buono: **94,61 $** (22,70%)
- Rialzo molto forte: **111,41 $** (44,49%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Solana tendeva a muoversi tra una zona bassa intorno a **70,43 $** e uno spike normale intorno a **85,06 $**.

La chiusura a 30 giorni era più spesso positiva: salita 62,50%, discesa 37,50%. Quindi la lettura principale è favorevole.

---

# Dogecoin — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟡 GIALLO / Incerto
**Prezzo attuale:** 0,07 $

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

- Se va molto male: **0,05 $** (-28,49%)
- Se va male: **0,06 $** (-14,05%)
- Scenario normale: **0,07 $** (-0,99%)
- Se va bene: **0,08 $** (12,21%)
- Se va molto bene: **0,09 $** (27,88%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **0,06 $** (-14,61%)
- Discesa brutta: **0,06 $** (-23,17%)
- Discesa molto brutta: **0,05 $** (-35,19%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **0,08 $** (13,74%)
- Rialzo buono: **0,09 $** (21,46%)
- Rialzo molto forte: **0,10 $** (33,95%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Dogecoin tendeva a muoversi tra una zona bassa intorno a **0,06 $** e uno spike normale intorno a **0,08 $**.

La chiusura a 30 giorni è incerta: salita 47,50%, discesa 52,50%. Non c'è un vantaggio netto.

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

**Prezzo attuale:** 65.399,99 $

Bitcoin ha un segnale favorevole. La statistica dei casi simili indica più possibilità di salita che di discesa, ma resta comunque una probabilità, non una certezza.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **62,50%**
- Casi negativi dopo 30 giorni: **37,50%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **86,37%**
- Rendimento medio dopo 30 giorni: **5,81%**
- Rendimento centrale dopo 30 giorni: **10,04%**
- Discesa media durante i 30 giorni: **-13,92%**
- Massimo rialzo medio durante i 30 giorni: **19,49%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **69.197,05 $**
- Scenario centrale a 30 giorni: **71.966,75 $**
- Zona di rischio media: **56.298,67 $**
- Zona di rialzo media: **78.149,60 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -26,95% → **47.772,28 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -15,45% → **55.295,48 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: 10,04% → **71.966,75 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 23,31% → **80.646,57 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 29,52% → **84.705,10 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -28,78% → **46.576,08 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -20,30% → **52.125,30 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -11,34% → **57.984,06 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -6,81% → **60.945,27 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: -4,79% → **62.265,33 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 1,86% → **66.618,58 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 6,97% → **69.961,52 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 13,86% → **74.464,18 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 27,13% → **83.140,88 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 33,06% → **87.018,18 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| SAND-USD        | 2023-06-29   | 2023-10-06 |        89.94 |        24.82 |          -6.32 |          24.82 |
| LRC-USD         | 2018-09-29   | 2019-01-06 |        89.93 |        21.04 |         -13.46 |         133.38 |
| XRP-USD         | 2019-10-09   | 2020-01-16 |        89.3  |        33.98 |          -3.56 |          46.48 |
| FIL-USD         | 2023-06-29   | 2023-10-06 |        89.06 |        23.33 |          -4.87 |          23.33 |
| ONE-USD         | 2020-01-22   | 2020-04-30 |        88.94 |         8.85 |          -5.79 |           9.61 |
| XLM-USD         | 2020-07-15   | 2020-10-22 |        88.89 |        27.12 |         -12.53 |          27.12 |
| ETH-USD         | 2023-06-30   | 2023-10-07 |        87.32 |        16.23 |          -5.81 |          16.23 |
| EOS-USD         | 2023-06-30   | 2023-10-07 |        87.17 |        22.59 |          -6.25 |          22.59 |
| BTC-USD         | 2018-09-30   | 2019-01-07 |        86.99 |       -15.19 |         -15.19 |           0.25 |
| MATIC-USD       | 2023-06-30   | 2023-10-07 |        86.84 |        30.44 |          -9.96 |          30.44 |

---

# Approfondimento tecnico — Solana (SOL-USD)

## Semaforo: 🟢 VERDE / Favorevole

**Prezzo attuale:** 77,11 $

Solana ha un segnale favorevole. La statistica dei casi simili indica più possibilità di salita che di discesa, ma resta comunque una probabilità, non una certezza.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **62,50%**
- Casi negativi dopo 30 giorni: **37,50%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **76,39%**
- Rendimento medio dopo 30 giorni: **7,24%**
- Rendimento centrale dopo 30 giorni: **3,79%**
- Discesa media durante i 30 giorni: **-10,93%**
- Massimo rialzo medio durante i 30 giorni: **19,61%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **82,70 $**
- Scenario centrale a 30 giorni: **80,03 $**
- Zona di rischio media: **68,68 $**
- Zona di rialzo media: **92,23 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -16,25% → **64,58 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -6,97% → **71,73 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: 3,79% → **80,03 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 15,82% → **89,31 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 30,00% → **100,25 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -22,41% → **59,83 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -11,77% → **68,03 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -8,66% → **70,43 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -5,41% → **72,94 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: -3,70% → **74,25 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 2,50% → **79,04 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 5,04% → **80,99 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 10,31% → **85,06 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 22,70% → **94,61 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 44,49% → **111,41 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| WAVES-USD       | 2019-03-08   | 2019-06-15 |        83.03 |       -37.82 |         -38.96 |           1    |
| QTUM-USD        | 2018-10-04   | 2019-01-11 |        80.29 |        -9.14 |         -19.1  |           3.33 |
| ENJ-USD         | 2018-10-04   | 2019-01-11 |        79.04 |       -12.02 |         -26.93 |           5.36 |
| NEAR-USD        | 2025-12-16   | 2026-03-25 |        78.79 |        10.14 |          -9.23 |          12.11 |
| BNB-USD         | 2025-12-21   | 2026-03-30 |        78.42 |         1.44 |          -4.18 |           5.73 |
| LINK-USD        | 2025-12-16   | 2026-03-25 |        78.32 |         0.03 |         -10.34 |           2.67 |
| RUNE-USD        | 2025-12-17   | 2026-03-26 |        78.04 |        18.5  |          -7.03 |          20.04 |
| SOL-USD         | 2025-12-19   | 2026-03-28 |        77.68 |         3.42 |          -3.74 |           8.51 |
| LRC-USD         | 2018-10-04   | 2019-01-11 |        77.62 |        35.3  |          -5.72 |         154.28 |
| APT-USD         | 2024-09-16   | 2024-12-24 |        77.43 |       -29.47 |         -29.47 |           7.73 |

---

# Approfondimento tecnico — Dogecoin (DOGE-USD)

## Semaforo: 🟡 GIALLO / Incerto

**Prezzo attuale:** 0,07 $

Dogecoin è in una situazione incerta. Lo scanner non vede un vantaggio chiaro né per la salita né per la discesa. In questi casi è meglio non forzare la previsione.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **47,50%**
- Casi negativi dopo 30 giorni: **52,50%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **87,56%**
- Rendimento medio dopo 30 giorni: **-1,15%**
- Rendimento centrale dopo 30 giorni: **-0,99%**
- Discesa media durante i 30 giorni: **-16,04%**
- Massimo rialzo medio durante i 30 giorni: **16,22%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **0,07 $**
- Scenario centrale a 30 giorni: **0,07 $**
- Zona di rischio media: **0,06 $**
- Zona di rialzo media: **0,08 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -28,49% → **0,05 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -14,05% → **0,06 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: -0,99% → **0,07 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 12,21% → **0,08 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 27,88% → **0,09 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -35,19% → **0,05 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -23,17% → **0,06 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -14,61% → **0,06 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -6,27% → **0,07 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: -0,47% → **0,07 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 0,00% → **0,07 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 6,00% → **0,08 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 13,74% → **0,08 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 21,46% → **0,09 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 33,95% → **0,10 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| ZEC-USD         | 2019-06-01   | 2019-09-08 |        92.28 |       -23.97 |         -27.41 |           8.97 |
| OP-USD          | 2025-12-17   | 2026-03-26 |        89.53 |        15.02 |          -6.29 |          23.81 |
| VET-USD         | 2022-03-09   | 2022-06-16 |        89.35 |         4.43 |          -5.37 |          15.47 |
| AVAX-USD        | 2025-08-29   | 2025-12-06 |        88.84 |         7.79 |         -14.74 |           8.89 |
| MKR-USD         | 2022-09-24   | 2023-01-01 |        88.71 |        27.72 |          -1.56 |          39.59 |
| THETA-USD       | 2022-03-11   | 2022-06-18 |        88.67 |        11.61 |          -6.22 |          26.91 |
| NEAR-USD        | 2022-03-17   | 2022-06-24 |        88.63 |         8.87 |         -20.28 |          13.53 |
| INJ-USD         | 2022-03-04   | 2022-06-11 |        88.44 |       -32.36 |         -35.14 |           0    |
| DASH-USD        | 2022-03-07   | 2022-06-14 |        88.38 |         0.01 |          -8.31 |          19.82 |
| XRP-USD         | 2019-10-04   | 2020-01-11 |        87.87 |        29.37 |           0    |          33.33 |

</details>
<!-- COMPACT_SECTION_END:scanner_full_detail -->

<!-- COMPACT_SECTION_START:market_regime -->
<details>
<summary><strong>🌦️ Market Regime Match</strong></summary>

<!-- MARKET_REGIME_MATCH_START -->
# Market Regime Match Report


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [market_regime_match_report.md](market_regime_match_report.md)

Generated: 2026-07-23 07:37 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | BEAR | 65.400 $ | False | -15.58% | -9.90% | BEAR | -15.58% | -9.90% |
| DOGE-USD | BEAR | 0.07226 $ | False | -26.59% | -16.11% | BEAR | -15.58% | -9.90% |
| SOL-USD | BEAR | 77,11 $ | False | -10.57% | -16.91% | BEAR | -15.58% | -9.90% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 62.50% | 10.04% | 23.31% | 29.52% | -11.34% | -28.78% | 13.86% | 27.13% | 33.06% | 57.50% | 11.71% | 43.89% | 78.22% |
| BTC-USD | SAME_BTC_REGIME | 7 | 85.71% | 6.86% | 21.12% | 31.24% | -8.55% | -16.91% | 11.67% | 28.73% | 44.81% | 42.86% | -3.23% | 11.71% | 18.58% |
| BTC-USD | SAME_ASSET_REGIME | 22 | 86.36% | 22.37% | 26.46% | 30.33% | -9.07% | -13.72% | 22.53% | 28.96% | 43.50% | 72.73% | 29.73% | 48.04% | 76.00% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 7 | 85.71% | 6.86% | 21.12% | 31.24% | -8.55% | -16.91% | 11.67% | 28.73% | 44.81% | 42.86% | -3.23% | 11.71% | 18.58% |
| DOGE-USD | ALL_MATCHES | 40 | 47.50% | -0.99% | 12.21% | 27.88% | -14.61% | -35.19% | 13.74% | 21.46% | 33.95% | 75.00% | 19.64% | 38.94% | 57.40% |
| DOGE-USD | SAME_BTC_REGIME | 28 | 50.00% | -0.40% | 12.46% | 28.21% | -14.10% | -35.27% | 13.83% | 20.82% | 35.21% | 82.14% | 21.48% | 42.37% | 57.99% |
| DOGE-USD | SAME_ASSET_REGIME | 29 | 48.28% | -0.80% | 15.02% | 28.05% | -10.05% | -35.23% | 15.47% | 22.48% | 34.58% | 82.76% | 24.58% | 48.98% | 57.70% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 27 | 48.15% | -0.80% | 13.31% | 28.38% | -13.72% | -35.32% | 14.12% | 21.81% | 35.83% | 81.48% | 23.23% | 44.60% | 58.29% |
| SOL-USD | ALL_MATCHES | 40 | 62.50% | 3.79% | 15.82% | 30.00% | -8.66% | -22.41% | 10.31% | 22.70% | 44.49% | 70.00% | 5.43% | 28.39% | 66.47% |
| SOL-USD | SAME_BTC_REGIME | 22 | 68.18% | 4.57% | 17.08% | 34.71% | -8.86% | -22.24% | 10.89% | 24.80% | 50.83% | 81.82% | 6.65% | 25.23% | 84.12% |
| SOL-USD | SAME_ASSET_REGIME | 27 | 66.67% | 5.72% | 20.55% | 41.83% | -8.49% | -21.91% | 12.11% | 24.49% | 57.62% | 77.78% | 7.75% | 32.38% | 73.36% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 22 | 68.18% | 4.57% | 17.08% | 34.71% | -8.86% | -22.24% | 10.89% | 24.80% | 50.83% | 81.82% | 6.65% | 25.23% | 84.12% |

## Breakdown by historical BTC regime

| target   | group                   |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 7 | 85.71% | 6.86% | -8.55% | 28.73% | 42.86% | -3.23% | 39.20% |
| BTC-USD | HISTORICAL_BTC_BULL | 24 | 58.33% | 13.19% | -10.87% | 27.13% | 66.67% | 31.23% | 58.92% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 9 | 55.56% | 8.85% | -13.46% | 22.26% | 44.44% | -3.08% | 39.13% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 28 | 50.00% | -0.40% | -14.10% | 20.82% | 82.14% | 21.48% | 59.69% |
| DOGE-USD | HISTORICAL_BTC_BULL | 5 | 80.00% | 14.01% | -6.83% | 32.09% | 60.00% | 27.74% | 50.85% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 7 | 14.29% | -17.99% | -24.85% | 13.61% | 57.14% | 0.59% | 23.33% |
| SOL-USD | HISTORICAL_BTC_BEAR | 22 | 68.18% | 4.57% | -8.86% | 24.80% | 81.82% | 6.65% | 74.63% |
| SOL-USD | HISTORICAL_BTC_BULL | 9 | 44.44% | -3.92% | -8.33% | 22.59% | 77.78% | 7.46% | 36.59% |
| SOL-USD | HISTORICAL_BTC_MIXED | 1 | 0.00% | -16.48% | -17.11% | 2.98% | 0.00% | -21.33% | 2.98% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 8 | 75.00% | 6.51% | -7.31% | 18.19% | 37.50% | -6.51% | 41.35% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 22 | 86.36% | 22.37% | -9.07% | 28.96% | 72.73% | 29.73% | 62.17% |
| BTC-USD | HISTORICAL_ASSET_BULL | 11 | 27.27% | -16.23% | -22.79% | 21.67% | 45.45% | -5.18% | 50.90% |
| BTC-USD | HISTORICAL_ASSET_MIXED | 1 | 0.00% | -37.22% | -39.28% | 4.09% | 0.00% | -36.70% | 4.09% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 6 | 50.00% | -3.17% | -11.85% | 16.06% | 33.33% | -6.00% | 20.40% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 29 | 48.28% | -0.80% | -10.05% | 22.48% | 82.76% | 24.58% | 59.53% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 4 | 75.00% | 11.44% | -12.74% | 36.78% | 75.00% | 15.77% | 58.21% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 7 | 28.57% | -17.98% | -19.91% | 13.61% | 42.86% | -8.92% | 16.67% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 27 | 66.67% | 5.72% | -8.49% | 24.49% | 77.78% | 7.75% | 67.90% |
| SOL-USD | HISTORICAL_ASSET_BULL | 6 | 16.67% | -9.66% | -15.15% | 14.58% | 66.67% | 3.31% | 20.55% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 100.00% | 19.99% | -1.20% | 24.50% | 100.00% | 42.40% | 47.99% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 6 | 83.33% | 6.51% | -7.56% | 14.78% | 33.33% | -5.66% | 32.90% |

## Top regime-adjusted matches

The table below shows the top matches separately for each target, so BTC does not hide SOL and DOGE.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | XRP-USD | 2019-10-09 | 89.30% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 33.98% | -3.56% | 46.48% | -38.29% | -38.91% | 46.48% |
| BTC-USD | ETH-USD | 2025-12-16 | 86.50% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 6.81% | -8.55% | 11.67% | -3.23% | -8.55% | 11.67% |
| BTC-USD | XRP-USD | 2025-12-16 | 86.21% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 1.37% | -6.98% | 4.44% | -4.54% | -6.98% | 4.94% |
| BTC-USD | MKR-USD | 2020-01-23 | 86.02% | BEAR | BEAR | SAME_BTC_AND_ASSET | HIGH_SPIKE_60D | 29.42% | -10.98% | 43.69% | 27.94% | -10.98% | 94.10% |
| BTC-USD | BTC-USD | 2025-12-17 | 85.28% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 12.82% | -4.12% | 13.78% | 12.34% | -4.12% | 19.40% |
| BTC-USD | OMG-USD | 2018-10-04 | 85.04% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -8.64% | -21.63% | 0.39% | 11.07% | -21.63% | 11.07% |
| BTC-USD | THETA-USD | 2022-03-21 | 85.00% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 6.86% | -13.75% | 6.86% | -10.80% | -13.75% | 31.92% |
| BTC-USD | SAND-USD | 2023-06-29 | 89.94% | BULL | BEAR | SAME_ASSET_ONLY | BULLISH_30D | 24.82% | -6.32% | 24.82% | 49.53% | -6.32% | 49.53% |
| BTC-USD | LRC-USD | 2018-09-29 | 89.93% | RECOVERY | BEAR | SAME_ASSET_ONLY | HIGH_SPIKE_60D | 21.04% | -13.46% | 133.38% | 29.74% | -13.46% | 133.38% |
| BTC-USD | FIL-USD | 2023-06-29 | 89.06% | BULL | BEAR | SAME_ASSET_ONLY | BULLISH_30D | 23.33% | -4.87% | 23.33% | 43.44% | -4.87% | 56.53% |
| DOGE-USD | OP-USD | 2025-12-17 | 89.53% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 15.02% | -6.29% | 23.81% | 19.12% | -6.29% | 58.54% |
| DOGE-USD | VET-USD | 2022-03-09 | 89.35% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 4.43% | -5.37% | 15.47% | 38.55% | -5.37% | 47.28% |
| DOGE-USD | MKR-USD | 2022-09-24 | 88.71% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 27.72% | -1.56% | 39.59% | 72.17% | -1.56% | 80.88% |
| DOGE-USD | THETA-USD | 2022-03-11 | 88.67% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 11.61% | -6.22% | 26.91% | 19.72% | -6.22% | 43.44% |
| DOGE-USD | INJ-USD | 2022-03-04 | 88.44% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -32.36% | -35.14% | 0.00% | 0.31% | -36.02% | 0.31% |
| DOGE-USD | DASH-USD | 2022-03-07 | 88.38% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 0.01% | -8.31% | 19.82% | 30.52% | -8.31% | 30.52% |
| DOGE-USD | XRP-USD | 2019-10-04 | 87.87% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 29.37% | 0.00% | 33.33% | -1.77% | -2.34% | 58.05% |
| DOGE-USD | HBAR-USD | 2022-03-09 | 87.82% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 2.03% | -8.48% | 14.12% | 19.55% | -8.48% | 27.29% |
| DOGE-USD | OMG-USD | 2022-03-07 | 87.75% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -8.54% | -14.76% | 5.54% | 24.58% | -14.76% | 24.58% |
| DOGE-USD | LTC-USD | 2018-04-08 | 87.70% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -35.58% | -35.58% | 6.16% | -33.12% | -38.94% | 6.16% |
| SOL-USD | QTUM-USD | 2018-10-04 | 80.29% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -9.14% | -19.10% | 3.33% | -0.16% | -19.10% | 10.72% |
| SOL-USD | ENJ-USD | 2018-10-04 | 79.04% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | -12.02% | -26.93% | 5.36% | 445.37% | -26.93% | 526.80% |
| SOL-USD | NEAR-USD | 2025-12-16 | 78.79% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 10.14% | -9.23% | 12.11% | 87.14% | -9.23% | 91.97% |
| SOL-USD | BNB-USD | 2025-12-21 | 78.42% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 1.44% | -4.18% | 5.73% | 5.54% | -4.18% | 11.40% |
| SOL-USD | LINK-USD | 2025-12-16 | 78.32% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 0.03% | -10.34% | 2.67% | 0.58% | -10.34% | 14.27% |
| SOL-USD | RUNE-USD | 2025-12-17 | 78.04% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 18.50% | -7.03% | 20.04% | 9.91% | -7.03% | 54.43% |
| SOL-USD | SOL-USD | 2025-12-19 | 77.68% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 3.42% | -3.74% | 8.51% | 0.43% | -3.74% | 18.70% |
| SOL-USD | LRC-USD | 2018-10-04 | 77.62% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 35.30% | -5.72% | 154.28% | 57.00% | -5.72% | 154.28% |
| SOL-USD | APT-USD | 2024-09-16 | 77.43% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -29.47% | -29.47% | 7.73% | -30.92% | -30.92% | 7.73% |
| SOL-USD | EOS-USD | 2018-10-14 | 77.20% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 66.62% | -4.37% | 66.62% | 55.08% | -4.37% | 81.36% |

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

Generato: 2026-07-23 07:37 UTC


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
| BTC | 65.400 $ | -1 | NEUTRALE / MISTO | STAGE 4 / MARKDOWN | MASSIMI E MINIMI CRESCENTI | ACCUMULO POSSIBILE / RANGE BASSO | BASSO | RIDUCI RISCHIO / NO LONG A LEVA |
| SOL | 77,11 $ | -6 | RIBASSISTA / FRAGILE | STAGE 4 / MARKDOWN | MASSIMI E MINIMI DECRESCENTI | ACCUMULO POSSIBILE / RANGE BASSO | BASSO | NON INSEGUIRE / TAKE PROFIT SU SPIKE |
| DOGE | 0.07226 $ | -6 | RIBASSISTA / FRAGILE | STAGE 4 / MARKDOWN | COMPRESSIONE / TRIANGOLO POSSIBILE | MARKDOWN / DEBOLEZZA | BASSO | NO LONG / SHORT SOLO DOPO SPIKE E REJECTION |

## Punteggi per area

| Asset | Trend | Struttura | Momentum | Volume | Prezzo | Candela | Wyckoff | Totale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | -4 | +2 | +1 | 0 | 0 | 0 | 0 | -1 |
| SOL | -4 | -2 | +2 | -2 | 0 | 0 | 0 | -6 |
| DOGE | -4 | 0 | +2 | -2 | 0 | 0 | -2 | -6 |

## Livelli tecnici

| Asset | Supporto | Resistenza | Breakout 60g | Breakdown 60g | ATR14 | Rendimento 30g | Rendimento 90g |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 64.972 $ | 65.508 $ | 78.101 $ | 57.748 $ | 2,19% | 4,34% | -15,58% |
| SOL | 76,82 $ | 78,88 $ | 87,79 $ | 60,41 $ | 2,65% | 10,74% | -10,57% |
| DOGE | 0.07206 $ | 0.07546 $ | 0.10653 $ | 0.06961 $ | 2,59% | -8,32% | -26,59% |

## Lettura dettagliata

### BTC

- Prezzo: **65.400 $**
- Score classico: **-1 / 12**
- Verdetto: **NEUTRALE / MISTO**
- Azione coerente: **RIDUCI RISCHIO / NO LONG A LEVA**
- Volatilità tecnica locale: **BASSO** — ATR14 2,19%; distanza supporto 0,64%; distanza resistenza 0,18%

Dettaglio:

- Trend: **-4** — prezzo sotto MA200 daily; breve termine sopra MA20/MA50; MA50 daily in discesa; MA200 daily in discesa; STAGE 4 / MARKDOWN
- Stage weekly: **STAGE 4 / MARKDOWN** — Prezzo sotto MA30 weekly con MA30 in discesa.
- Struttura: **+2** — MASSIMI E MINIMI CRESCENTI
- Momentum: **+1** — RSI sano 55.6; MACD sopra signal; istogramma MACD in peggioramento
- Volume: **0** — OBV sotto media; CMF positivo 0.08; volume ratio 1.01
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **0** — ACCUMULO POSSIBILE / RANGE BASSO. Prezzo nella metà bassa del range, ma senza spring confermato.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 55.62 |
| MACD histogram | 322.16714 |
| CMF20 | 0.079 |
| Volume ratio 20 | 1.01 |
| MA20 | 64.169 $ |
| MA50 | 63.108 $ |
| MA100 | 69.996 $ |
| MA200 | 72.557 $ |
| Pendenza MA50 20g | -6,32% |
| Pendenza MA200 60g | -9,90% |
| Bollinger width | 6,96% |
| Bollinger position | 0.77 |

### SOL

- Prezzo: **77,11 $**
- Score classico: **-6 / 12**
- Verdetto: **RIBASSISTA / FRAGILE**
- Azione coerente: **NON INSEGUIRE / TAKE PROFIT SU SPIKE**
- Volatilità tecnica locale: **BASSO** — ATR14 2,65%; distanza supporto 0,39%; distanza resistenza 2,28%

Dettaglio:

- Trend: **-4** — prezzo sotto MA200 daily; MA200 daily in discesa; STAGE 4 / MARKDOWN
- Stage weekly: **STAGE 4 / MARKDOWN** — Prezzo sotto MA30 weekly con MA30 in discesa.
- Struttura: **-2** — MASSIMI E MINIMI DECRESCENTI
- Momentum: **+2** — RSI sano 51.8; RSI in miglioramento; MACD sotto signal; istogramma MACD in miglioramento
- Volume: **-2** — OBV sotto media; CMF negativo -0.10; volume ratio 0.88
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **0** — ACCUMULO POSSIBILE / RANGE BASSO. Prezzo nella metà bassa del range, ma senza spring confermato.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 51.82 |
| MACD histogram | -0.10340 |
| CMF20 | -0.102 |
| Volume ratio 20 | 0.88 |
| MA20 | 77,81 $ |
| MA50 | 73,38 $ |
| MA100 | 79,62 $ |
| MA200 | 89,00 $ |
| Pendenza MA50 20g | -2,89% |
| Pendenza MA200 60g | -16,91% |
| Bollinger width | 11,04% |
| Bollinger position | 0.42 |

### DOGE

- Prezzo: **0.07226 $**
- Score classico: **-6 / 12**
- Verdetto: **RIBASSISTA / FRAGILE**
- Azione coerente: **NO LONG / SHORT SOLO DOPO SPIKE E REJECTION**
- Volatilità tecnica locale: **BASSO** — ATR14 2,59%; distanza supporto 0,31%; distanza resistenza 4,41%

Dettaglio:

- Trend: **-4** — prezzo sotto MA200 daily; medie daily allineate ribassiste; MA50 daily in discesa; MA200 daily in discesa; STAGE 4 / MARKDOWN
- Stage weekly: **STAGE 4 / MARKDOWN** — Prezzo sotto MA30 weekly con MA30 in discesa.
- Struttura: **0** — COMPRESSIONE / TRIANGOLO POSSIBILE
- Momentum: **+2** — RSI neutrale 39.1; MACD sopra signal; istogramma MACD in miglioramento
- Volume: **-2** — OBV sotto media; CMF negativo -0.09; volume ratio 0.96
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **-2** — MARKDOWN / DEBOLEZZA. Prezzo basso nel range e sotto medie principali.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 39.15 |
| MACD histogram | 0.00043 |
| CMF20 | -0.094 |
| Volume ratio 20 | 0.96 |
| MA20 | 0.07359 $ |
| MA50 | 0.07820 $ |
| MA100 | 0.09074 $ |
| MA200 | 0.09792 $ |
| Pendenza MA50 20g | -12,75% |
| Pendenza MA200 60g | -16,11% |
| Bollinger width | 9,81% |
| Bollinger position | 0.31 |

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

Generato: 2026-07-23 07:37 UTC


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
| BTC | 65.400 $ | Doppio massimo | CANDIDATO | ribassista | n/a | 49.952 $ | n/a | 13,25% | Fib 23,6% NON ATTIVO (0) @ 63.676 $ | NEL RANGE | 65.092 $ |
| SOL | 77,11 $ | Doppio minimo | MATURO | rialzista | 2026-07-01 | 91,46 $ | 7,54% | n/a | Fib 23,6% REJECTION (-1) @ 79,27 $ | NEL RANGE | 76,82 $ |
| DOGE | 0.07226 $ | Triplo massimo | MATURO | ribassista | 2026-06-24 | 0.05847 $ | 29,73% | n/a | Fib 23,6% NON ATTIVO (0) @ 0.08213 $ | NEL RANGE | 0.07107 $ |

## BTC

![Classic visual BTC](classic_visual_BTC.png)

- Pattern principale: **Doppio massimo**
- Stato pattern: **CANDIDATO** (0)
- Famiglia: **ribassista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-06-22 -> 2026-07-15**
- Età formazione: **8 giorni**
- Breakout pattern: **n/a**
- Età breakout: **n/a**
- Neckline: **57.748 $**
- Target teorico: **49.952 $**
- Progresso verso target: **n/a**
- Distanza dalla neckline: **13,25%**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 23,6% NON ATTIVO (0) @ 63.676 $** — Swing UP 2026-07-01 57.748 -> 2026-07-15 65.508; livello più vicino 23.6% a 63.676; stato NON ATTIVO; confluenza: nessuna confluenza indipendente.
- Invalidazione: **58.903 $**
- Relazione prezzo/neckline: **sopra neckline**
- Dettaglio: Due massimi simili vicino a 65.544 tra 2026-06-22 e 2026-07-15. Neckline ribassista stimata: 57.748. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 8 giorni. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **NEL RANGE**
- Supporto: **65.092 $**
- Resistenza: **65.508 $**
- Breakout 60g: **78.101 $**
- Breakdown 60g: **57.748 $**
- RSI14: **55.66**
- ATR14: **2,19%**
- Volume ratio 20g: **1.01**
- Rendimento 30g: **+4,36%**
- Rendimento 90g: **-15,56%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Doppio massimo | CANDIDATO | 0 | ribassista | 57.748 $ | n/a | n/a | 49.952 $ | n/a | 13,25% | 58.903 $ | Due massimi simili a 65.544 $ e 65.508 $. Neckline circa 57.748 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 8 giorni. |
| Triangolo discendente possibile | CANDIDATO | 0 | ribassista | n/a | n/a | n/a | n/a | n/a | n/a | n/a | Massimi decrescenti e supporto quasi piatto. Stato: CANDIDATO; il pattern non ha una neckline univoca da usare per il lifecycle. |
| Doppio minimo | CANDIDATO | 0 | rialzista | 67.248 $ | n/a | n/a | 76.748 $ | n/a | 2,83% | 65.903 $ | Due minimi simili a 59.109 $ e 57.748 $. Neckline circa 67.248 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 22 giorni. |

## SOL

![Classic visual SOL](classic_visual_SOL.png)

- Pattern principale: **Doppio minimo**
- Stato pattern: **MATURO** (+1)
- Famiglia: **rialzista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-06-06 -> 2026-06-25**
- Età formazione: **28 giorni**
- Breakout pattern: **2026-07-01**
- Età breakout: **22 giorni**
- Neckline: **75,94 $**
- Target teorico: **91,46 $**
- Progresso verso target: **7,54%**
- Distanza dalla neckline: **n/a**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 23,6% REJECTION (-1) @ 79,27 $** — Swing DOWN 2026-05-11 98,27 -> 2026-07-17 73,40; livello più vicino 23.6% a 79,27; stato REJECTION; confluenza: resistenza tecnica.
- Invalidazione: **74,42 $**
- Relazione prezzo/neckline: **sopra neckline**
- Dettaglio: Due minimi simili vicino a 60,41 tra 2026-06-06 e 2026-06-25. Neckline stimata: 75,94. Breakout neckline: 2026-07-01 (22 giorni fa). Stato: MATURO. Target teorico: 91,46; progresso corrente: 7,54%. Relazione prezzo/neckline: sopra neckline. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **NEL RANGE**
- Supporto: **76,82 $**
- Resistenza: **78,88 $**
- Breakout 60g: **87,79 $**
- Breakdown 60g: **60,41 $**
- RSI14: **51.79**
- ATR14: **2,65%**
- Volume ratio 20g: **0.88**
- Rendimento 30g: **+10,72%**
- Rendimento 90g: **-10,58%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Doppio minimo | MATURO | +1 | rialzista | 75,94 $ | 2026-07-01 | 22g | 91,46 $ | 7,54% | n/a | 74,42 $ | Due minimi simili vicino a 60,41 tra 2026-06-06 e 2026-06-25. Neckline stimata: 75,94. Breakout neckline: 2026-07-01 (22 giorni fa). Stato: MATURO. Target teorico: 91,46; progresso corrente: 7,54%. Relazione prezzo/neckline: sopra neckline. Fonte lifecycle: technical_structure_metrics.csv. |
| Testa e spalle inverso | CANDIDATO | 0 | rialzista | 79,35 $ | n/a | n/a | 94,28 $ | n/a | 2,91% | 77,76 $ | Spalla sinistra 67,92 $, testa 64,42 $, spalla destra 73,40 $. Neckline circa 79,35 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 6 giorni. |
| Doppio massimo | CANDIDATO | 0 | ribassista | 64,42 $ | n/a | n/a | 49,96 $ | n/a | 19,70% | 65,71 $ | Due massimi simili a 75,94 $ e 78,88 $. Neckline circa 64,42 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 8 giorni. |
| Doppio minimo | CANDIDATO | 0 | rialzista | 98,27 $ | n/a | n/a | 114,91 $ | n/a | 27,44% | 96,30 $ | Due minimi simili a 81,63 $ e 81,69 $. Neckline circa 98,27 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 61 giorni. |
| Testa e spalle | TARGET RAGGIUNTO | 0 | ribassista | 82,57 $ | 2026-05-28 | 56g | 66,88 $ | 34,80% | n/a | 84,22 $ | Spalla sinistra 88,05 $, testa 98,27 $, spalla destra 87,79 $. Neckline circa 82,57 $. Breakout neckline: 2026-05-28 (56 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 66,88 $; progresso: 34,80%; prezzo sotto neckline. |

## DOGE

![Classic visual DOGE](classic_visual_DOGE.png)

- Pattern principale: **Triplo massimo**
- Stato pattern: **MATURO** (-1)
- Famiglia: **ribassista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-03-25 -> 2026-06-12**
- Età formazione: **41 giorni**
- Breakout pattern: **2026-06-24**
- Età breakout: **29 giorni**
- Neckline: **0.07809 $**
- Target teorico: **0.05847 $**
- Progresso verso target: **29,73%**
- Distanza dalla neckline: **n/a**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 23,6% NON ATTIVO (0) @ 0.08213 $** — Swing DOWN 2026-05-14 0.11825 -> 2026-07-13 0.07097; livello più vicino 23.6% a 0.08213; stato NON ATTIVO; confluenza: nessuna confluenza indipendente.
- Invalidazione: **0.07966 $**
- Relazione prezzo/neckline: **sotto neckline**
- Dettaglio: Tre massimi simili vicino a 0.09772 dal 2026-03-25 al 2026-06-12. Neckline ribassista stimata: 0.07809. Breakout neckline: 2026-06-24 (29 giorni fa). Stato: MATURO. Target teorico: 0.05847; progresso corrente: 29,73%. Relazione prezzo/neckline: sotto neckline. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **NEL RANGE**
- Supporto: **0.07107 $**
- Resistenza: **0.07923 $**
- Breakout 60g: **0.10653 $**
- Breakdown 60g: **0.06961 $**
- RSI14: **39.09**
- ATR14: **2,59%**
- Volume ratio 20g: **0.96**
- Rendimento 30g: **-8,35%**
- Rendimento 90g: **-26,61%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Triplo massimo | MATURO | -1 | ribassista | 0.07809 $ | 2026-06-24 | 29g | 0.05847 $ | 29,73% | n/a | 0.07966 $ | Tre massimi simili vicino a 0.09772 dal 2026-03-25 al 2026-06-12. Neckline ribassista stimata: 0.07809. Breakout neckline: 2026-06-24 (29 giorni fa). Stato: MATURO. Target teorico: 0.05847; progresso corrente: 29,73%. Relazione prezzo/neckline: sotto neckline. Fonte lifecycle: technical_structure_metrics.csv. |
| Doppio massimo | MATURO | -1 | ribassista | 0.07809 $ | 2026-06-24 | 29g | 0.06035 $ | 32,89% | n/a | 0.07966 $ | Due massimi simili a 0.09584 $ e 0.09169 $. Neckline circa 0.07809 $. Breakout neckline: 2026-06-24 (29 giorni fa). Stato: MATURO. Target teorico: 0.06035 $; progresso: 32,89%; prezzo sotto neckline. |
| Doppio minimo | CANDIDATO | 0 | rialzista | 0.07923 $ | n/a | n/a | 0.08886 $ | n/a | 9,65% | 0.07765 $ | Due minimi simili a 0.06961 $ e 0.07097 $. Neckline circa 0.07923 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 10 giorni. |
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

Generato: 2026-07-23 07:37 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [fractal_path_tracker.md](fractal_path_tracker.md)

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-07-23**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-01-07**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **77,11 $**
- Verdetto principale: **ANALOGIA DEBOLE / SCENARIO SECONDARIO**
- Somiglianza strutturale: **+64,77%**
- Aderenza live principale: **+63,56%**
- Errore medio live principale: **18,22%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE SOLO DI CONTESTO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **47**
- Osservazioni inclusive dal bottom: **48**
- Osservazioni da inizio programma/scanner: **21**
- Errore assoluto medio dal bottom: **11,36%**
- Errore assoluto medio da inizio programma: **18,22%**
- Gap firmato medio ultimi 7 giorni: **+16,08%**
- Errore assoluto medio ultimi 7 giorni: **16,08%**
- Gap ultimo giorno: **+15,45%**
- Stato aderenza: **STACCATO / MOLTO IN ANTICIPO**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **+15,45%**
- Gap firmato medio 7g: **+16,08%**
- Errore assoluto medio 7g: **16,08%**
- Variazione recente gap: **-1,66%**
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
| 38 | 2026-07-14 | 2022-12-29 | 77,76 $ | 65,56 $ | +18,62% | da inizio programma |
| 39 | 2026-07-15 | 2022-12-30 | 77,26 $ | 65,40 $ | +18,14% | da inizio programma |
| 40 | 2026-07-16 | 2022-12-31 | 75,27 $ | 65,18 $ | +15,48% | da inizio programma |
| 41 | 2026-07-17 | 2023-01-01 | 75,01 $ | 65,49 $ | +14,54% | da inizio programma |
| 42 | 2026-07-18 | 2023-01-02 | 75,46 $ | 65,74 $ | +14,79% | da inizio programma |
| 43 | 2026-07-19 | 2023-01-03 | 76,36 $ | 65,71 $ | +16,21% | da inizio programma |
| 44 | 2026-07-20 | 2023-01-04 | 77,79 $ | 66,43 $ | +17,11% | da inizio programma |
| 45 | 2026-07-21 | 2023-01-05 | 78,11 $ | 66,32 $ | +17,77% | da inizio programma |
| 46 | 2026-07-22 | 2023-01-06 | 77,91 $ | 66,78 $ | +16,66% | da inizio programma |
| 47 | 2026-07-23 | 2023-01-07 | 77,11 $ | 66,79 $ | +15,45% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-07-30 | 82,63 $ | 95,40 $ | 77,11 $ / 95,40 $ | no | n/a | n/a | n/a |
| 14g | 2026-08-06 | 89,73 $ | 103,59 $ | 77,11 $ / 103,59 $ | no | n/a | n/a | n/a |
| 21g | 2026-08-13 | 90,72 $ | 104,74 $ | 77,11 $ / 105,14 $ | no | n/a | n/a | n/a |
| 28g | 2026-08-20 | 91,91 $ | 106,11 $ | 77,11 $ / 108,12 $ | no | n/a | n/a | n/a |
| 35g | 2026-08-27 | 86,15 $ | 99,47 $ | 77,11 $ / 108,12 $ | no | n/a | n/a | n/a |
| 42g | 2026-09-03 | 97,07 $ | 112,07 $ | 77,11 $ / 112,07 $ | no | n/a | n/a | n/a |
| 49g | 2026-09-10 | 91,29 $ | 105,40 $ | 77,11 $ / 112,92 $ | no | n/a | n/a | n/a |
| 56g | 2026-09-17 | 88,06 $ | 101,66 $ | 77,11 $ / 112,92 $ | no | n/a | n/a | n/a |
| 63g | 2026-09-24 | 81,28 $ | 93,83 $ | 77,11 $ / 112,92 $ | no | n/a | n/a | n/a |
| 70g | 2026-10-01 | 106,22 $ | 122,64 $ | 77,11 $ / 124,72 $ | no | n/a | n/a | n/a |
| 77g | 2026-10-08 | 108,31 $ | 125,04 $ | 77,11 $ / 128,86 $ | no | n/a | n/a | n/a |
| 84g | 2026-10-15 | 111,92 $ | 129,21 $ | 77,11 $ / 129,52 $ | no | n/a | n/a | n/a |
| 91g | 2026-10-22 | 110,09 $ | 127,10 $ | 77,11 $ / 129,52 $ | no | n/a | n/a | n/a |
| 98g | 2026-10-29 | 119,43 $ | 137,89 $ | 77,11 $ / 138,65 $ | no | n/a | n/a | n/a |
| 105g | 2026-11-05 | 109,58 $ | 126,51 $ | 77,11 $ / 138,65 $ | no | n/a | n/a | n/a |
| 112g | 2026-11-12 | 115,22 $ | 133,02 $ | 77,11 $ / 138,65 $ | no | n/a | n/a | n/a |
| 119g | 2026-11-19 | 113,86 $ | 131,46 $ | 77,11 $ / 138,65 $ | no | n/a | n/a | n/a |
| 126g | 2026-11-26 | 105,51 $ | 121,81 $ | 77,11 $ / 138,65 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 9 | 44,44% | 1,47% | 16,08% |
| 14g | 2 | 100,00% | 1,71% | n/a |
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

Ultima lettura salvata: **2026-07-23** — SOL 77,11 $, gap +15,45%, somiglianza +64,77%.

Nel report principale lascio solo il link, così non diventa troppo lungo.

<!-- SOL_BTC_FRACTAL_HISTORY_END -->

</details>
<!-- COMPACT_SECTION_END:fractal_path -->

<!-- COMPACT_SECTION_START:exchange_microstructure -->
<details>
<summary><strong>🏦 Dati exchange, liquidità e leva</strong></summary>

<!-- EXCHANGE_MICROSTRUCTURE_START -->
# Dati exchange, liquidità e leva

Generato: 2026-07-23 07:38 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [exchange_microstructure_report.md](exchange_microstructure_report.md)

Questo modulo legge Kraken Futures, Bitget Futures e KuCoin Futures come nucleo derivati. OKX e Coinbase vengono raccolti come fonti ausiliarie non pesate.
Non modifica la formula matematica di RSI, Fibonacci o Wyckoff: controlla se quei segnali sono sostenuti da acquisti, vendite, OI, funding e liquidità.

**Limite importante:** questo nucleo non assume disponibile un feed pubblico completo delle liquidazioni. La componente liquidazioni resta neutrale; le zone future restano stime di pressione, non dati certi delle singole posizioni.

Diagnostica completa: [exchange_source_diagnostics.md](exchange_source_diagnostics.md)

## Sintesi

| Asset | Prezzo | Exchange | Segnale candidato | Peso Global | Bias exchange | Confidenza | Copertura | Funding 8h eq. | OI 24h | Taker flow (campione/4h) | Book 0,5% | Liq long campione | Liq short campione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 65.401 $ | 3 | 0 | 0 | LEGGERMENTE POSITIVA / NON PESATA | MEDIA | 100% | -0,0054% | -2,58% | 1,28 | +2,03% | 0 $ | 0 $ |
| SOL | 77,12 $ | 3 | 0 | 0 | LEGGERMENTE POSITIVA / NON PESATA | MEDIA | 100% | +0,0008% | -5,54% | 2,89 | -2,81% | 0 $ | 0 $ |
| DOGE | 0.07229 $ | 3 | 0 | 0 | LEGGERMENTE POSITIVA / NON PESATA | MEDIA | 100% | +0,0080% | +5,83% | 1,72 | +4,06% | 0 $ | 0 $ |

Il segnale candidato è limitato a **±1**, ma il peso nel Global resta **0** finché il tracker a 7 giorni non raggiunge 30 controlli, almeno 55% di accuratezza e return corretto direzione positivo. Un singolo muro o funding non basta.

La colonna taker usa un campione recente nel primo run. Dopo almeno 3 fotografie distribuite su almeno 45 minuti viene sostituita automaticamente dalla media intraday 4h.

## Dati separati per exchange

| Asset | Exchange | Stato | Funding 8h eq. | Open interest | Taker flow | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | Kraken | OK | +0,0032% | 134,10 mln $ | 0,12 | +8,38% |
| BTC | Bitget | OK | +0,0021% | 2,32 mld $ | 0,64 | -14,26% |
| BTC | Kucoin | OK | -0,0129% | 1,71 mld $ | 0,79 | -1,13% |
| SOL | Kraken | OK | -0,0461% | 17,93 mln $ | 0,95 | -15,78% |
| SOL | Bitget | OK | -0,0023% | 346,44 mln $ | 40,38 | -1,12% |
| SOL | Kucoin | OK | -0,0082% | 251,09 mln $ | 2,27 | -4,30% |
| DOGE | Kraken | OK | -0,0020% | 3,36 mln $ | 1,20 | +0,53% |
| DOGE | Bitget | OK | +0,0005% | 84,95 mln $ | 0,53 | -3,30% |
| DOGE | Kucoin | OK | +0,0100% | 127,68 mln $ | 0,42 | +12,23% |

Kraken, Bitget e KuCoin contribuiscono a funding normalizzato, open interest, trade aggressivi e order book. Non viene inventato un long/short ratio pubblico né un feed completo delle liquidazioni.

## Conferme per indicatori tecnici

### BTC

- Score grezzo exchange: **+2,25**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 0, accuratezza n/a.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 0, bear 1, divergenze 1.
- Flusso taker/order book: **+1,75**.
- OI/funding/basis: **+0,00**.
- Affollamento long/short: **+0,00**.
- Liquidazioni: **NON PESATE / FEED COMPLETO NON ASSUNTO DISPONIBILE**.
- **Wyckoff:** Markdown non pienamente confermato: compare assorbimento compratore.
- **Fibonacci:** Fibonacci non_attivo; nessuna conferma exchange netta.
- **RSI:** RSI in zona non estrema o flusso exchange non abbastanza netto.
- **Pattern:** I pattern candidati restano non operativi: i dati exchange possono solo preparare la conferma.
- **Breakout/breakdown:** Resistenza vicina con acquisti aggressivi: breakout più credibile, ma serve chiusura sopra il livello.
- **Mappa liquidità attuale:** muro bid: n/a; muro ask: n/a

![Microstruttura exchange BTC](exchange_microstructure_BTC.png)

### SOL

- Score grezzo exchange: **+2,25**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 0, accuratezza n/a.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 1, bear 0, divergenze 0.
- Flusso taker/order book: **+1,75**.
- OI/funding/basis: **+0,00**.
- Affollamento long/short: **+0,00**.
- Liquidazioni: **NON PESATE / FEED COMPLETO NON ASSUNTO DISPONIBILE**.
- **Wyckoff:** Markdown non pienamente confermato: compare assorbimento compratore.
- **Fibonacci:** Fibonacci rejection; nessuna conferma exchange netta. Confluenza tecnica dichiarata: resistenza tecnica.
- **RSI:** RSI in zona non estrema o flusso exchange non abbastanza netto.
- **Pattern:** Doppio minimo maturo sostenuto dal flusso exchange.
- **Breakout/breakdown:** Prezzo non abbastanza vicino a un livello chiave o flusso non netto.
- **Mappa liquidità attuale:** muro bid: n/a; muro ask: n/a

![Microstruttura exchange SOL](exchange_microstructure_SOL.png)

### DOGE

- Score grezzo exchange: **+2,38**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 0, accuratezza n/a.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 0, bear 1, divergenze 0.
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
| BTC | +62,50% | +10,04% | 0 | n/a | RACCOLTA DATI | 0,00 | +62,50% | +10,04% |
| SOL | +62,50% | +3,79% | 0 | n/a | RACCOLTA DATI | 0,00 | +62,50% | +3,79% |
| DOGE | +47,50% | -0,99% | 0 | n/a | RACCOLTA DATI | 0,00 | +47,50% | -0,99% |

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

Generato: 2026-07-23 07:38 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [exchange_signal_tracker_report.md](exchange_signal_tracker_report.md)

Questo tracker verifica se il segnale candidato exchange ±1 anticipa correttamente la direzione del prezzo a 1/3/7/14/30 giorni.
Il peso Global resta 0 finché l'orizzonte 7g non ha almeno 30 controlli, accuratezza almeno 55% e return corretto direzione positivo. L'overlay a 30g ha un gate separato.

Controlli maturati completati in questa esecuzione: **9**.

## Ultime fotografie giornaliere

| Data | Asset | Prezzo | Versione | Calibrazione | Candidato | Peso Global | Score raw | Confidenza | Taker 4h | OI 24h | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-07-23 | BTC | 65.401,40 | V2.1.3 | OK | 0 | 0 | 2,25 | MEDIA | 1,28 | -2,58% | +2,03% |
| 2026-07-23 | DOGE | 0.07229 | V2.1.3 | OK | 0 | 0 | 2,38 | MEDIA | 1,72 | +5,83% | +4,06% |
| 2026-07-23 | SOL | 77,12 | V2.1.3 | OK | 0 | 0 | 2,25 | MEDIA | 2,89 | -5,54% | -2,81% |
| 2026-07-22 | BTC | 66.242,06 | V2.1.3 | OK | 0 | 0 | 3,50 | ALTA | 1,21 | +3,44% | +1,49% |
| 2026-07-22 | DOGE | 0.07326 | V2.1.3 | OK | 0 | 0 | 0,75 | BASSA | 0,95 | +2,24% | +0,22% |
| 2026-07-22 | SOL | 77,84 | V2.1.3 | OK | 0 | 0 | 2,25 | MEDIA | 1,93 | +6,24% | +6,76% |
| 2026-07-21 | BTC | 65.482,28 | V2.1.3 | OK | 0 | 0 | 3,50 | ALTA | 1,98 | +2,64% | +0,77% |
| 2026-07-21 | DOGE | 0.07279 | V2.1.3 | OK | 0 | 0 | 2,12 | MEDIA | 1,70 | -1,89% | -0,20% |
| 2026-07-21 | SOL | 78,16 | V2.1.3 | OK | 1 | 0 | 2,50 | MEDIA | 3,05 | +1,19% | +3,26% |

## Accuratezza direzionale

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 1 | +100,00% | +1,59% | +1,07% | +1,84% | FEEDBACK RAPIDO |
| BTC | 3g | 1 | +100,00% | +1,47% | -1,13% | +3,82% | FEEDBACK RAPIDO |
| BTC | 7g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 14g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 30g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 1g | 1 | +0,00% | -0,43% | -0,39% | +0,39% | FEEDBACK RAPIDO |
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

**DOGE** — DOGE: i futures non danno una lettura chiara. Non si vede uno sbilanciamento forte né long né short. Qui pesa di più il report frattale.

| Asset | Prezzo | Funding | OI 24h | Long/Short | Lettura futures | Forza |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 65.400 $ | -0.0031% | +3.34% | 1.75 | Misto | 2/5 |
| SOL | 77,11 $ | -0.0026% | -9.12% | 2.43 | Misto | 1/5 |
| DOGE | 0.07226 $ | +0.0075% | -4.58% | 4.69 | Misto | 1/5 |

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

Generato: 2026-07-23 07:37 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [rsi_multitimeframe_divergence_report.md](rsi_multitimeframe_divergence_report.md)

Il modulo confronta prezzo e RSI 14 sui pivot confermati **daily e weekly**. Riconosce divergenze regolari e nascoste, segnali in formazione, invalidazioni e semplice conferma del momentum.

**Peso operativo: 0.** Non modifica il Global Confluence, non cambia le soglie del Paper Trading e non apre né blocca operazioni. I risultati vengono misurati prima di qualsiasi futura decisione sul peso.

## Sintesi corrente

| Asset   | Daily                     | Stato D    | Weekly              | Stato W    | Lettura weekly                                                                                                                |   Peso |
|:--------|:--------------------------|:-----------|:--------------------|:-----------|:------------------------------------------------------------------------------------------------------------------------------|-------:|
| BTC     | Bullish regolare          | CONFERMATA | Bullish regolare    | CONFERMATA | Bullish regolare confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto. |      0 |
| SOL     | Hidden bearish invalidata | INVALIDATA | Hidden bearish      | CONFERMATA | Hidden bearish confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto.   |      0 |
| DOGE    | Hidden bearish            | CONFERMATA | Conferma ribassista | CONTESTO   | Prezzo e RSI stanno scendendo insieme: momentum ribassista confermato, nessuna bullish divergence attiva.                     |      0 |

## Dettaglio dei pivot

| Asset   | TF   | Tipo                      | Stato      | Prezzo / RSI      | Pivot confrontati                                                   | Δ prezzo contesto   | Δ RSI contesto   |   Peso |
|:--------|:-----|:--------------------------|:-----------|:------------------|:--------------------------------------------------------------------|:--------------------|:-----------------|-------:|
| BTC     | 1D   | Bullish regolare          | CONFERMATA | 65.395 $ / 55,64  | 2026-06-25 58.076 $ / RSI 30,46 → 2026-07-01 57.748 $ / RSI 37,26   | n/a                 | n/a              |      0 |
| BTC     | 1W   | Bullish regolare          | CONFERMATA | 65.395 $ / 40,73  | 2026-06-07 59.109 $ / RSI 34,23 → 2026-07-05 57.748 $ / RSI 38,20   | n/a                 | n/a              |      0 |
| SOL     | 1D   | Hidden bearish invalidata | INVALIDATA | 77,14 $ / 51,88   | n/a                                                                 | -1,16%              | -2,61            |      0 |
| SOL     | 1W   | Hidden bearish            | CONFERMATA | 77,14 $ / 40,45   | 2026-05-17 98,27 $ / RSI 38,29 → 2026-07-05 83,81 $ / RSI 42,25     | n/a                 | n/a              |      0 |
| DOGE    | 1D   | Hidden bearish            | CONFERMATA | 0.07228 $ / 39,15 | 2026-06-12 0.09169 $ / RSI 35,18 → 2026-07-04 0.07923 $ / RSI 41,65 | n/a                 | n/a              |      0 |
| DOGE    | 1W   | Conferma ribassista       | CONTESTO   | 0.07228 $ / 33,26 | n/a                                                                 | -18,57%             | -4,13            |      0 |

### BTC

- **1D — Bullish regolare / CONFERMATA**: Bullish regolare confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto.
- **1W — Bullish regolare / CONFERMATA**: Bullish regolare confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto.

### SOL

- **1D — Hidden bearish invalidata / INVALIDATA**: La precedente hidden bearish non è più sostenuta dalla relazione corrente tra pivot di prezzo e RSI.
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

Generato: 2026-07-23 07:37 UTC


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

| Asset   | Prezzo   |   Punteggio | Verdetto         | Trend            | Momentum                  | Struttura                                             |   Pattern score | Fibonacci      | Pattern rialzista         | Pattern ribassista         | Supporto   | Resistenza   |
|:--------|:---------|------------:|:-----------------|:-----------------|:--------------------------|:------------------------------------------------------|----------------:|:---------------|:--------------------------|:---------------------------|:-----------|:-------------|
| BTC | 65.400 $ | -2 | NEUTRALE / MISTO | Trend misto | Momentum in miglioramento | Struttura ribassista con massimi e minimi decrescenti | 0 | 0 / NON ATTIVO | Doppio minimo / CANDIDATO | Doppio massimo / CANDIDATO | 57.748 | 65.508 |
| SOL | 77,11 $ | -6 | DEBOLE | Trend ribassista | Momentum misto | Compressione / triangolo | +1 | -1 / REJECTION | Doppio minimo / MATURO | Doppio massimo / CANDIDATO | 73,40 | 78,88 |
| DOGE | 0.07226 $ | -6 | DEBOLE | Trend ribassista | Momentum in miglioramento | Struttura ribassista con massimi e minimi decrescenti | -1 | 0 / NON ATTIVO | Doppio minimo / CANDIDATO | Triplo massimo / MATURO | 0.07097 | 0.07923 |

## Riepilogo ciclo di vita pattern

| Asset   | Doppio minimo   | Triplo minimo   | Adam/Eve Bottom                 | Doppio massimo   | Triplo massimo   | Adam/Eve Top                 |   Punteggio pattern |
|:--------|:----------------|:----------------|:--------------------------------|:-----------------|:-----------------|:-----------------------------|--------------------:|
| BTC | CANDIDATO | CANDIDATO | Adam and Eve Bottom — CANDIDATO | CANDIDATO | CANDIDATO | Adam and Eve Top — CANDIDATO | 0 |
| SOL | MATURO | CANDIDATO | Adam and Eve Bottom — CANDIDATO | CANDIDATO | CANDIDATO | Adam and Eve Top — CANDIDATO | 1 |
| DOGE | CANDIDATO | ASSENTE | Adam and Eve Bottom — CANDIDATO | ASSENTE | MATURO | Eve and Adam Top — MATURO | -1 |

## Indicatori tecnici

| Asset   |   RSI 14 |   Istogramma MACD | MA20    | MA50    | MA200   | Pendenza MA50 20g   | Pendenza MA200 60g   | Rendimento 30g   | Rendimento 90g   |
|:--------|---------:|------------------:|:--------|:--------|:--------|:--------------------|:---------------------|:-----------------|:-----------------|
| BTC | 55.66 | 322.755 | 64.169 | 63.108 | 72.557 | -5,87% | -9,76% | 7,22% | -15,73% |
| SOL | 51.79 | -0.10404 | 77,81 | 73,38 | 89,00 | -2,70% | -16,64% | 13,43% | -10,49% |
| DOGE | 39.09 | 0.00043 | 0.07359 | 0.07820 | 0.09792 | -12,05% | -15,90% | -4,93% | -26,30% |

## Dettaglio asset

### BTC

- Prezzo: **65.400 $**
- Punteggio tecnico: **-2 / 12**
- Verdetto: **NEUTRALE / MISTO**
- Trend: **Trend misto** (-1)
- Momentum: **Momentum in miglioramento** (2)
- Volume: **Volume neutrale** (0)
- Struttura: **Struttura ribassista con massimi e minimi decrescenti** (-2)
  - Dettaglio struttura: Ultimi minimi: 5.808e+04 -> 5.775e+04. Ultimi massimi: 6.554e+04 -> 6.551e+04.
- Divergenza: **Divergenza rialzista RSI, Divergenza ribassista nascosta RSI** (1)
- Fase Wyckoff candidata: **Markdown / fase ribassista** (-2)
  - Dettaglio Wyckoff: Prezzo sotto MA200 con trend a 90 giorni ancora debole.
- Fibonacci automatico: **NON ATTIVO** (0)
  - Swing UP 2026-07-01 57.748 -> 2026-07-15 65.508; livello più vicino 23.6% a 63.676; stato NON ATTIVO; confluenza: nessuna confluenza indipendente.
- Punteggio pattern: **0**
  - rialzista dominante: Doppio minimo (CANDIDATO, 0); ribassista dominante: Doppio massimo (CANDIDATO, 0).
- Supporto più vicino: **57.748**
- Resistenza più vicina: **65.508**

Pattern classici e ciclo di vita:

- Doppio minimo: **CANDIDATO** (0)
  - Due minimi simili vicino a 57.748 tra 2026-06-05 e 2026-07-01. Neckline stimata: 67.248. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 22 giorni.
  - neckline 67.248; target 76.748; distanza dalla neckline 2,83%; prezzo sotto neckline.
- Triplo minimo: **CANDIDATO** (0)
  - Tre minimi simili vicino a 57.748 dal 2026-06-05 al 2026-07-01. Neckline stimata: 67.248. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 22 giorni.
  - neckline 67.248; target 76.748; distanza dalla neckline 2,83%; prezzo sotto neckline.
- Adam and Eve Bottom: **CANDIDATO** (0)
  - Pattern Adam and Eve Bottom vicino a 57.748 dal 2026-06-05 al 2026-07-01. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 67.248. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 22 giorni.
  - neckline 67.248; target 76.748; distanza dalla neckline 2,83%; prezzo sotto neckline.
- Doppio massimo: **CANDIDATO** (0)
  - Due massimi simili vicino a 65.544 tra 2026-06-22 e 2026-07-15. Neckline ribassista stimata: 57.748. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 8 giorni.
  - neckline 57.748; target 49.952; distanza dalla neckline 13,25%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 67.248 dal 2026-06-15 al 2026-07-15. Neckline ribassista stimata: 57.748. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 8 giorni.
  - neckline 57.748; target 48.247; distanza dalla neckline 13,25%; prezzo sopra neckline.
- Adam and Eve Top: **CANDIDATO** (0)
  - Pattern Adam and Eve Top vicino a 67.248 dal 2026-06-15 al 2026-07-15. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 57.748. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 8 giorni.
  - neckline 57.748; target 48.247; distanza dalla neckline 13,25%; prezzo sopra neckline.

### SOL

- Prezzo: **77,11 $**
- Punteggio tecnico: **-6 / 12**
- Verdetto: **DEBOLE**
- Trend: **Trend ribassista** (-3)
- Momentum: **Momentum misto** (1)
- Volume: **Volume da distribuzione** (-2)
- Struttura: **Compressione / triangolo** (0)
  - Dettaglio struttura: Ultimi minimi: 64.42 -> 73.4. Ultimi massimi: 83.81 -> 78.88.
- Divergenza: **Nessuna** (0)
- Fase Wyckoff candidata: **Markdown / fase ribassista** (-2)
  - Dettaglio Wyckoff: Prezzo sotto MA200 con trend a 90 giorni ancora debole.
- Fibonacci automatico: **REJECTION** (-1)
  - Swing DOWN 2026-05-11 98,27 -> 2026-07-17 73,40; livello più vicino 23.6% a 79,27; stato REJECTION; confluenza: resistenza tecnica.
- Punteggio pattern: **+1**
  - rialzista dominante: Doppio minimo (MATURO, +1); ribassista dominante: Doppio massimo (CANDIDATO, 0).
- Supporto più vicino: **73,40**
- Resistenza più vicina: **78,88**

Pattern classici e ciclo di vita:

- Doppio minimo: **MATURO** (+1)
  - Due minimi simili vicino a 60,41 tra 2026-06-06 e 2026-06-25. Neckline stimata: 75,94. Breakout neckline: 2026-07-01 (22 giorni fa). Stato: MATURO. Target teorico: 91,46; progresso corrente: 7,54%. Relazione prezzo/neckline: sopra neckline.
  - neckline 75,94; target 91,46; breakout 2026-07-01 (22g); progresso 7,54%; prezzo sopra neckline.
- Triplo minimo: **CANDIDATO** (0)
  - Tre minimi simili vicino a 81,63 dal 2026-04-29 al 2026-05-23. Neckline stimata: 98,27. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 61 giorni.
  - neckline 98,27; target 114,91; distanza dalla neckline 27,44%; prezzo sotto neckline.
- Adam and Eve Bottom: **CANDIDATO** (0)
  - Pattern Adam and Eve Bottom vicino a 67,92 dal 2026-06-19 al 2026-07-17. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 83,81. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 6 giorni.
  - neckline 83,81; target 99,70; distanza dalla neckline 8,69%; prezzo sotto neckline.
- Doppio massimo: **CANDIDATO** (0)
  - Due massimi simili vicino a 78,88 tra 2026-06-15 e 2026-07-15. Neckline ribassista stimata: 64,42. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 8 giorni.
  - neckline 64,42; target 49,96; distanza dalla neckline 19,70%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 78,88 dal 2026-06-15 al 2026-07-15. Neckline ribassista stimata: 64,42. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 8 giorni.
  - neckline 64,42; target 49,96; distanza dalla neckline 19,70%; prezzo sopra neckline.
- Adam and Eve Top: **CANDIDATO** (0)
  - Pattern Adam and Eve Top vicino a 78,88 dal 2026-06-15 al 2026-07-15. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 64,42. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 8 giorni.
  - neckline 64,42; target 49,96; distanza dalla neckline 19,70%; prezzo sopra neckline.

### DOGE

- Prezzo: **0.07226 $**
- Punteggio tecnico: **-6 / 12**
- Verdetto: **DEBOLE**
- Trend: **Trend ribassista** (-3)
- Momentum: **Momentum in miglioramento** (2)
- Volume: **Volume da distribuzione** (-2)
- Struttura: **Struttura ribassista con massimi e minimi decrescenti** (-2)
  - Dettaglio struttura: Ultimi minimi: 0.07107 -> 0.07097. Ultimi massimi: 0.09169 -> 0.07923.
- Divergenza: **Divergenza ribassista nascosta RSI** (-1)
- Fase Wyckoff candidata: **Possibile accumulazione** (1)
  - Dettaglio Wyckoff: Prezzo sotto MA200, vicino alla parte bassa del range a 120 giorni, RSI 39.1.
- Fibonacci automatico: **NON ATTIVO** (0)
  - Swing DOWN 2026-05-14 0.11825 -> 2026-07-13 0.07097; livello più vicino 23.6% a 0.08213; stato NON ATTIVO; confluenza: nessuna confluenza indipendente.
- Punteggio pattern: **-1**
  - rialzista dominante: Doppio minimo (CANDIDATO, 0); ribassista dominante: Triplo massimo (MATURO, -1).
- Supporto più vicino: **0.07097**
- Resistenza più vicina: **0.07923**

Pattern classici e ciclo di vita:

- Doppio minimo: **CANDIDATO** (0)
  - Due minimi simili vicino a 0.06961 tra 2026-06-30 e 2026-07-13. Neckline stimata: 0.07923. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 10 giorni.
  - neckline 0.07923; target 0.08886; distanza dalla neckline 9,65%; prezzo sotto neckline.
- Triplo minimo: **ASSENTE** (0)
- Adam and Eve Bottom: **CANDIDATO** (0)
  - Pattern Adam and Eve Bottom vicino a 0.06961 dal 2026-06-30 al 2026-07-13. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 0.07923. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 10 giorni.
  - neckline 0.07923; target 0.08886; distanza dalla neckline 9,65%; prezzo sotto neckline.
- Doppio massimo: **ASSENTE** (0)
- Triplo massimo: **MATURO** (-1)
  - Tre massimi simili vicino a 0.09772 dal 2026-03-25 al 2026-06-12. Neckline ribassista stimata: 0.07809. Breakout neckline: 2026-06-24 (29 giorni fa). Stato: MATURO. Target teorico: 0.05847; progresso corrente: 29,73%. Relazione prezzo/neckline: sotto neckline.
  - neckline 0.07809; target 0.05847; breakout 2026-06-24 (29g); progresso 29,73%; prezzo sotto neckline.
- Eve and Adam Top: **MATURO** (-1)
  - Pattern Eve and Adam Top vicino a 0.09584 dal 2026-04-07 al 2026-06-12. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 0.07809. Breakout neckline: 2026-06-24 (29 giorni fa). Stato: MATURO. Target teorico: 0.06035; progresso corrente: 32,89%. Relazione prezzo/neckline: sotto neckline.
  - neckline 0.07809; target 0.06035; breakout 2026-06-24 (29g); progresso 32,89%; prezzo sotto neckline.

## Fibonacci automatico

Il modulo seleziona uno swing recente tramite pivot confermati. Un semplice tocco vale 0: Fibonacci pesa al massimo ±1 soltanto quando il livello è tenuto, perso, recuperato o respinto e coincide con almeno un livello tecnico indipendente.

| Asset   | Swing                         | 23,6%   | 38,2%   | 50,0%   | 61,8%   | 78,6%   | Livello vicino   | Stato      | Confluenza                      |   Score |
|:--------|:------------------------------|:--------|:--------|:--------|:--------|:--------|:-----------------|:-----------|:--------------------------------|--------:|
| BTC | UP 2026-07-01 -> 2026-07-15 | 63.676 | 62.543 | 61.628 | 60.712 | 59.408 | 23.6% / 63.676 | NON ATTIVO | nessuna confluenza indipendente | 0 |
| SOL | DOWN 2026-05-11 -> 2026-07-17 | 79,27 | 82,90 | 85,83 | 88,77 | 92,95 | 23.6% / 79,27 | REJECTION | resistenza tecnica | -1 |
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

- **BTC**: 0/30 previsioni controllate su 21 fatte. Stato: **RACCOLTA DATI**.
- **SOL**: 0/30 previsioni controllate su 21 fatte. Stato: **RACCOLTA DATI**.
- **DOGE**: 0/30 previsioni controllate su 21 fatte. Stato: **RACCOLTA DATI**.

| Asset | Previsioni fatte | Controllate | Progresso | In attesa | Stato | Prossimo controllo |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 21 | 0 | 0/30 [░░░░░░░░░░] | 21 | RACCOLTA DATI | 2026-08-02 / tra 10 giorni |
| SOL | 21 | 0 | 0/30 [░░░░░░░░░░] | 21 | RACCOLTA DATI | 2026-08-02 / tra 10 giorni |
| DOGE | 21 | 0 | 0/30 [░░░░░░░░░░] | 21 | RACCOLTA DATI | 2026-08-02 / tra 10 giorni |

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

Generato: 2026-07-23 07:38 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [data_quality_coherence_report.md](data_quality_coherence_report.md)

Questo controllo non modifica punteggi o decisioni. Verifica che tutti i moduli usino lo stesso prezzo corrente e che le nuove regole Technical/Classic Visual siano integre.

## Stato finale: **OK**

## Prezzo unico per modulo

| Modulo                  | Asset   | Campo             | Stato   | Prezzo snapshot   | Prezzo modulo   | Differenza   |
|:------------------------|:--------|:------------------|:--------|:------------------|:----------------|:-------------|
| Scanner                 | BTC     | current_price     | OK      | 65.400 $          | 65.400 $        | +0,0000%     |
| Scanner                 | DOGE    | current_price     | OK      | 0.07226 $         | 0.07226 $       | -0,0000%     |
| Scanner                 | SOL     | current_price     | OK      | 77,11 $           | 77,11 $         | +0,0000%     |
| Scanner Forecast        | BTC     | current_price     | OK      | 65.400 $          | 65.400 $        | +0,0000%     |
| Scanner Forecast        | SOL     | current_price     | OK      | 77,11 $           | 77,11 $         | +0,0000%     |
| Scanner Forecast        | DOGE    | current_price     | OK      | 0.07226 $         | 0.07226 $       | -0,0000%     |
| Technical Structure     | BTC     | price             | OK      | 65.400 $          | 65.400 $        | +0,0000%     |
| Technical Structure     | SOL     | price             | OK      | 77,11 $           | 77,11 $         | +0,0000%     |
| Technical Structure     | DOGE    | price             | OK      | 0.07226 $         | 0.07226 $       | -0,0000%     |
| Classic Technical       | BTC     | price             | OK      | 65.400 $          | 65.400 $        | +0,0000%     |
| Classic Technical       | SOL     | price             | OK      | 77,11 $           | 77,11 $         | +0,0000%     |
| Classic Technical       | DOGE    | price             | OK      | 0.07226 $         | 0.07226 $       | -0,0000%     |
| Classic Visual          | BTC     | price             | OK      | 65.400 $          | 65.400 $        | +0,0000%     |
| Classic Visual          | SOL     | price             | OK      | 77,11 $           | 77,11 $         | +0,0000%     |
| Classic Visual          | DOGE    | price             | OK      | 0.07226 $         | 0.07226 $       | -0,0000%     |
| Exchange Microstructure | BTC     | price             | OK      | 65.400 $          | 65.401 $        | +0,0022%     |
| Exchange Microstructure | SOL     | price             | OK      | 77,11 $           | 77,12 $         | +0,0182%     |
| Exchange Microstructure | DOGE    | price             | OK      | 0.07226 $         | 0.07229 $       | +0,0347%     |
| RSI top-cycle           | SOL     | current_price     | OK      | 77,11 $           | 77,11 $         | +0,0000%     |
| RSI top-cycle           | SOL     | current_price     | OK      | 77,11 $           | 77,11 $         | +0,0000%     |
| Frattale BTC/SOL        | SOL     | sol_current_price | OK      | 77,11 $           | 77,11 $         | +0,0000%     |
| Fractal path            | SOL     | current_price     | OK      | 77,11 $           | 77,11 $         | +0,0000%     |

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

Generato: 2026-07-23T20:17:35+00:00

- Modalità: **SOLO PAPER TRADING**
- Asset: **SOL spot**
- Leva: **nessuna (1x)**
- Capitale iniziale separato: **€40.000,00**
- Fonte mercato: **KUCOIN_PUBLIC_API**; nuove entrate: **CONSENTITE**

| Equity | Cash | SOL | Prezzo | Rendimento | Realizzato | Commissioni | Max DD | Operazioni |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €40.000,00 | €40.000,00 | 0.000000 | 75.7080 | +0.00% | €0,00 | €0,00 | 0.00% | 0 |

**Ultima decisione:** HOLD — Prezzo dentro la fascia neutrale.

Bande 4H: L2 72.2976 · L1 74.4580 · media 77.1586 · U1 79.8592 · U2 82.0196.

> Questo portafoglio non condivide capitale, posizioni o statistiche con il paper trading da €10.000.
<!-- SOL_SPOT_ADAPTIVE_END -->
