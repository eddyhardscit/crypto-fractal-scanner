<!-- COMPACT_REPORT_HEADER_START -->
> **Vista compatta:** Decisione operativa, Global Confluence e cambiamenti giornalieri restano aperti. Tocca il titolo di una sezione per mostrare o nascondere i dettagli.  
> Tutte le tabelle e tutti i dati restano nel file: copiando il Markdown raw viene copiato tutto.
<!-- COMPACT_REPORT_HEADER_END -->

<!-- COMPACT_SECTION_START:decision -->
<details open>
<summary><strong>🧭 Decisione operativa — da leggere per prima</strong></summary>

<!-- DECISION_REPORT_START -->

# Decisione operativa sintetica

Generato: 2026-07-26 05:14 UTC

Report separato completo: [decision_report.md](decision_report.md)

Sintesi automatica dello scanner: l'azione spot viene copiata direttamente dal Global Confluence; long, short e rischio restano filtri separati e più prudenti.

| Asset | Global | Direzione | Spot | Long leva | Short leva | Max long | Max short | Rischio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +5 | BULLISH | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE | NO LONG A LEVA / ATTENDI SOPRA 67.248 $ | NO SHORT | nessuna | nessuna | MEDIO |
| SOL | 0 | NEUTRALE / INCERTO | HOLD LEGGERO / ATTESA CONFERME | NO LONG A LEVA | NO SHORT | nessuna | nessuna | MOLTO ALTO |
| DOGE | +2 | NEUTRALE / INCERTO | STAI ALLA FINESTRA | NO LONG A LEVA | NO SHORT | nessuna | nessuna | MOLTO ALTO |

## Lettura immediata

- **BTC**: Global = **+5**, spot = **ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE**, long = **NO LONG A LEVA / ATTENDI SOPRA 67.248 $**, short = **NO SHORT**, rischio = **MEDIO**.
- **SOL**: Global = **0**, spot = **HOLD LEGGERO / ATTESA CONFERME**, long = **NO LONG A LEVA**, short = **NO SHORT**, rischio = **MOLTO ALTO**.
- **DOGE**: Global = **+2**, spot = **STAI ALLA FINESTRA**, long = **NO LONG A LEVA**, short = **NO SHORT**, rischio = **MOLTO ALTO**.

## Dettaglio logica

### BTC

- Global Confluence: **+5**
- Confluenza: **MODERATAMENTE POSITIVA**
- Bias Global: **Costruttivo prudente**
- Direzione decisionale: **BULLISH**
- Azione spot dal Global: **ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE**
- Long leva: **NO LONG A LEVA / ATTENDI SOPRA 67.248 $**
- Short leva: **NO SHORT**
- Rischio: **MEDIO**
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
- Conferme: conferma del doppio minimo sopra 75,94; nuova conferma tecnica sopra 78,73; milestone analogiche 98,70 / 106,85, valide soltanto se rientra anche il gap frattale.
- Invalidazioni: Allarmi sotto 71,33 / 73,40 / 62,19.

### DOGE

- Global Confluence: **+2**
- Confluenza: **MISTA / PARZIALE**
- Bias Global: **Neutrale / misto**
- Direzione decisionale: **NEUTRALE / INCERTO**
- Azione spot dal Global: **STAI ALLA FINESTRA**
- Long leva: **NO LONG A LEVA**
- Short leva: **NO SHORT**
- Rischio: **MOLTO ALTO**
- Conferme: Sopra 0.07923 migliora; sopra 0.07966 viene invalidato il pattern ribassista dominante.
- Invalidazioni: Sotto 0.07097 il rischio ribassista aumenta.

## Nota semplice

- **Spot** = usa la stessa azione del Global Confluence, senza una seconda mappatura che possa produrre frasi diverse.
- **Zona alta storica** = zona dove non inseguire troppo; può essere zona da prendere profitto.
- **Zona bassa storica** = zona di rischio; con leva la liquidazione non dovrebbe stare lì vicino.
- **BTC leva** = nessun long a leva finché il prezzo snapshot non supera **67.248 $**; sotto quella soglia resta solo l'azione spot indicata dal Global.
- **Lifecycle EMA200** = per SOL resta solo contesto, peso Global 0; score interno 4; EMA200 circa 112,75 $; upside verso EMA200 +50,16%. Non autorizza leva e non aggiunge punti automatici.
- **NO LONG** non significa automaticamente **SHORT**. Lo short ha senso solo se il quadro è bearish o se lo spike viene spesso scaricato.
- Per SOL, se il Global è da **+3 in su**, la decisione non deve diventare bearish solo perché lo scanner grezzo a 30 giorni è incerto.

<!-- DECISION_REPORT_END -->

<!-- PAPER_TRADING_START -->
# Paper trading automatico KuCoin

Generato: 2026-07-26T05:14:55+00:00


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [paper_trading_report.md](paper_trading_report.md)

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-07-26T05:08:24+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-07-26T05:08:24+00:00 | 2026-07-26T05:08:24+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-07-26T04:45:00+00:00 | 2026-07-26T04:45:00+00:00 | 8,5 min | 25,0 min | OK |
| 60m | 12 | 2026-07-26T04:00:00+00:00 | 2026-07-26T04:00:00+00:00 | 8,5 min | 45,0 min | OK |
| 240m | 12 | 2026-07-26T00:00:00+00:00 | 2026-07-26T00:00:00+00:00 | 1,14 h | 1,00 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | SHIB | 60m | LONG | 6,25 | 4,50 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | SHIB | 60m | LONG | 6,25 | 4,50 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | BANK | 60m | LONG | 7,75 | 4,50 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | SHIB | 60m | LONG | 6,25 | 4,50 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Balanced V3 Long Only V1 | SHIB | 60m | LONG | 6,25 | 6,00 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Nohigh Cap75 Short Only V1 | SHIB | 60m | LONG | 6,25 | 4,50 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | BANK | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Scanner Top5 Btc Guard Mfe V1 | BANK | 60m | LONG | 7,75 | 5,00 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | SHIB | 60m | LONG | 6,25 | 4,50 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 No Esports Mfe Lock V1 | BANK | 60m | LONG | 7,75 | 4,50 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 Long Nohigh Cap75 V1 | SHIB | 60m | LONG | 6,25 | 4,50 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast V3 Cap75 V1 | SHIB | 60m | LONG | 6,25 | 4,50 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Nohigh Cap75 V1 | SHIB | 60m | LONG | 6,25 | 4,50 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Score 6 75 Cost Aware V1 | SHIB | 60m | LONG | 6,25 | 6,00 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Score 6 75 No Trend Up V1 | SHIB | 60m | LONG | 6,25 | 6,00 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Score 6 75 V1 | SHIB | 60m | LONG | 6,25 | 6,00 | 0,00 | OPENED | 8,5 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Principale 4H | AKE | 240m | LONG | 7,75 | 6,00 | 0,00 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | EUL | 240m | LONG | 7,75 | 6,00 | 0,00 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | ALLO | 240m | SHORT | -6,75 | 6,00 | 0,00 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | BANK | 240m | LONG | 6,25 | 6,00 | 0,00 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | SHIB | 240m | LONG | 6,25 | 6,00 | 0,00 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | ZEC | 240m | SHORT | -5,17 | 6,00 | 0,83 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | PEPE | 240m | LONG | 5,13 | 6,00 | 0,87 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | ETH | 240m | LONG | 3,68 | 6,00 | 2,32 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | SOL | 240m | SHORT | -2,63 | 6,00 | 3,37 | STALE_CANDLE | 1,14 h | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | HYPE | 240m | SHORT | -1,50 | 6,00 | 4,50 | STALE_CANDLE | 1,14 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | DOGE | 240m | SHORT | -1,18 | 6,00 | 4,82 | STALE_CANDLE | 1,14 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Principale 4H | BTC | 240m | SHORT | -0,75 | 6,00 | 5,25 | STALE_CANDLE | 1,14 h | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 68.5 minuti; tolleranza 60 minuti. |
| Benchmark trend following EMA 1H | AKE | 60m | LONG | 7,75 | 5,00 | 0,00 | READY | 8,5 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Combo Adaptive | AKE | 60m | LONG | 7,75 | 5,00 | 0,00 | READY | 8,5 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Combo Adaptive Partial 1R V1 | AKE | 60m | LONG | 7,75 | 5,00 | 0,00 | READY | 8,5 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Combo Adaptive Tp3 V1 | AKE | 60m | LONG | 7,75 | 5,00 | 0,00 | READY | 8,5 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Master Adaptive Gb20 V1 | AKE | 60m | LONG | 7,75 | 0,00 | 0,00 | READY | 8,5 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Bilanciata 1H V2 | ALLO | 60m | SHORT | -7,75 | 5,50 | 0,00 | READY | 8,5 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Fast No Pepe V1 | ALLO | 60m | SHORT | -7,75 | 4,50 | 0,00 | READY | 8,5 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Fast Tp2 V1 | ALLO | 60m | SHORT | -7,75 | 4,50 | 0,00 | READY | 8,5 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.892,26 | -1,08% | €-107,74 | €3.000,00 | -3,59% | 5 | 19 | 31,58% | 0,83 | 4,26% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 19 | 650 | CAMPIONE INSUFFICIENTE | 30 (mancano 11) |

- Trade del Principale 4H chiusi: **19**; win rate **31,58%**; profit factor **0,83**.
- Expectancy: **€-5,55** per trade; P&L netto: **€-105,47**; max drawdown: **4,26%**.
- Valutazione: **Servono altri eventi indipendenti prima di trarre conclusioni.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 5 | €9.892,26 | €1.094,91 | €3.284,72 | €148,81 | €-1,01 |
| TEST | Scanner Top 5 Long 1H | 6 | €10.849,66 | €1.596,38 | €3.192,76 | €216,11 | €11,31 |
| TEST | Scanner Top 5 + forza BTC 1H | 6 | €10.618,01 | €1.605,80 | €3.211,60 | €212,56 | €10,96 |
| TEST | Bilanciata 1H V1 | 6 | €10.589,50 | €1.871,05 | €5.613,16 | €159,85 | €28,05 |
| TEST | Benchmark Donchian breakout 1H | 4 | €10.568,52 | €3.284,35 | €6.568,70 | €207,82 | €102,09 |
| TEST | Bilanciata 1H V3 Filtered | 5 | €10.562,11 | €1.104,65 | €3.313,96 | €158,80 | €-0,63 |
| TEST | 1H Fast Nohigh Cap75 V1 | 5 | €10.466,68 | €1.635,49 | €4.906,46 | €209,33 | €58,44 |
| TEST | 1H Fast V3 Cap75 V1 | 4 | €10.438,41 | €1.038,18 | €3.114,54 | €207,64 | €48,26 |
| TEST | 1H Fast Score 6 75 V1 | 3 | €10.412,70 | €826,75 | €2.480,26 | €103,61 | €65,47 |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | 2 | €10.389,24 | €633,24 | €1.899,73 | €103,52 | €5,97 |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | 4 | €10.360,00 | €978,99 | €2.936,96 | €102,42 | €101,85 |
| TEST | Scanner Top5 Btc Runner25 V1 | 6 | €10.328,84 | €1.583,04 | €3.166,08 | €206,77 | €10,78 |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 4 | €10.325,86 | €945,18 | €2.835,53 | €101,53 | €132,79 |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | 4 | €10.311,65 | €1.071,49 | €3.214,46 | €154,67 | €59,55 |
| TEST | Scanner Top5 Btc Tp3 V1 | 5 | €10.300,57 | €1.583,01 | €3.166,02 | €205,91 | €9,68 |
| TEST | 1H Fast Score 6 75 Range Only V1 | 3 | €10.283,89 | €607,65 | €1.822,94 | €103,11 | €59,37 |
| TEST | 1H Fast V3 Nohigh Range Only V1 | 4 | €10.283,51 | €972,94 | €2.918,83 | €102,04 | €101,17 |
| TEST | Combo Adaptive Side Regime Guard V1 | 5 | €10.277,69 | €1.247,01 | €2.494,03 | €104,31 | €99,81 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 4 | €10.274,80 | €952,24 | €2.856,72 | €152,68 | €101,47 |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 5 | €10.242,04 | €1.014,50 | €3.043,51 | €54,60 | €133,38 |
| TEST | Combo Adaptive | 5 | €10.230,73 | €2.175,38 | €4.350,76 | €204,61 | €28,19 |
| TEST | Bilanciata 1H V2 | 5 | €10.230,51 | €1.659,53 | €4.978,58 | €204,95 | €-4,25 |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | 5 | €10.226,94 | €1.518,02 | €3.036,03 | €200,64 | €10,70 |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | 6 | €10.226,51 | €2.065,62 | €6.196,86 | €153,77 | €-1,32 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 3 | €10.221,80 | €772,57 | €2.317,70 | €152,15 | €47,48 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 3 | €10.216,50 | €761,89 | €2.285,68 | €152,09 | €42,16 |
| TEST | Scanner Top5 Btc Btc Le3 V1 | 6 | €10.197,83 | €1.582,62 | €3.165,25 | €202,98 | €10,78 |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | 5 | €10.194,26 | €2.187,20 | €6.561,59 | €153,76 | €95,47 |
| TEST | Rapida 1H V3 Filtered | 5 | €10.191,37 | €2.752,37 | €8.257,11 | €205,26 | €-19,97 |
| TEST | Combo Scanner | 7 | €10.187,58 | €1.542,28 | €3.084,55 | €203,55 | €11,08 |
| TEST | Main Dynamic Asset Selector V1 | 3 | €10.186,76 | €996,99 | €2.990,97 | €101,25 | €-10,62 |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | 3 | €10.181,67 | €847,49 | €2.542,48 | €0,00 | €161,01 |
| TEST | Main Side Regime Guard V1 | 4 | €10.179,86 | €1.136,15 | €3.408,46 | €151,65 | €36,88 |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 4 | €10.174,35 | €846,83 | €2.540,48 | €3,44 | €153,69 |
| TEST | Combo Trend Side Regime Guard V1 | 5 | €10.171,29 | €1.721,03 | €3.442,07 | €153,54 | €62,41 |
| TEST | 1H Fast V3 No Esports Long Only V1 | 4 | €10.158,50 | €1.041,10 | €3.123,29 | €99,87 | €87,97 |
| TEST | Forza relativa 1H V2 | 5 | €10.137,59 | €2.141,44 | €4.282,89 | €202,85 | €-4,72 |
| TEST | 1H Fast No Pepe V1 | 5 | €10.133,50 | €2.736,97 | €8.210,91 | €204,09 | €-19,84 |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 5 | €10.129,90 | €1.017,54 | €3.052,63 | €53,21 | €162,29 |
| TEST | 1H Fast Tp2 V1 | 7 | €10.128,03 | €2.282,43 | €6.847,29 | €155,03 | €67,62 |
| TEST | Scanner Top10 Long | 5 | €10.124,29 | €2.026,73 | €4.053,46 | €152,96 | €25,01 |
| TEST | Scanner Top15 Long | 5 | €10.124,29 | €2.026,73 | €4.053,46 | €152,96 | €25,01 |
| TEST | Scanner Top20 Long | 5 | €10.124,29 | €2.026,73 | €4.053,46 | €152,96 | €25,01 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 4 | €10.121,49 | €933,25 | €2.799,74 | €99,99 | €89,72 |
| TEST | Master Adaptive Gb20 Loss Cap V1 | 4 | €10.120,67 | €2.643,20 | €5.286,40 | €200,90 | €78,50 |
| TEST | Btc Bollinger 1H | 1 | €10.118,93 | €1.402,77 | €4.208,32 | €50,50 | €22,57 |
| TEST | Master Adaptive Gb20 Be V1 | 4 | €10.117,78 | €2.116,52 | €4.233,03 | €151,26 | €5,30 |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | 1 | €10.112,33 | €464,84 | €1.394,53 | €0,00 | €82,47 |
| TEST | Combo Mean Reversion | 2 | €10.100,35 | €2.224,11 | €4.448,22 | €50,00 | €35,05 |
| TEST | Combo Adaptive Runner25 V1 | 6 | €10.100,27 | €2.286,55 | €4.573,09 | €201,30 | €28,22 |
| TEST | Combo Adaptive Quality7 V1 | 5 | €10.093,99 | €2.217,86 | €4.435,72 | €200,01 | €29,90 |
| TEST | Sol Donchian 1H | 0 | €10.092,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Ema 1H | 0 | €10.091,86 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V2 | 2 | €10.087,47 | €2.884,57 | €8.653,70 | €100,39 | €0,00 |
| TEST | Sol Bollinger 4H | 0 | €10.086,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 4H | 0 | €10.084,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | 1 | €10.081,39 | €463,42 | €1.390,27 | €0,00 | €82,22 |
| TEST | 1H Balanced Long No Rhv V1 | 5 | €10.065,96 | €1.406,89 | €4.220,66 | €200,36 | €9,43 |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | 4 | €10.065,64 | €998,18 | €2.994,54 | €199,58 | €42,94 |
| TEST | Master Adaptive Gb20 Partial V1 | 4 | €10.062,65 | €2.086,76 | €4.173,51 | €200,90 | €5,27 |
| TEST | Scanner Top5 Btc Guard V1 | 5 | €10.059,50 | €1.390,81 | €2.781,61 | €197,88 | €10,38 |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | 0 | €10.056,58 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | 4 | €10.042,59 | €994,55 | €2.983,65 | €198,80 | €42,82 |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 5 | €10.035,75 | €701,07 | €2.103,21 | €99,97 | €102,97 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 5 | €10.035,75 | €701,07 | €2.103,21 | €99,97 | €102,97 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 1 | €10.016,78 | €50,00 | €750,00 | €11,00 | €-5,80 |
| TEST | Eth Bollinger 1H | 0 | €10.015,45 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 1H | 0 | €10.013,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Benchmark trend following EMA 1H | 6 | €10.004,98 | €1.132,21 | €2.264,42 | €151,36 | €60,68 |
| TEST | Scalp RSI Short 80 · prudente · 5x | 1 | €10.004,22 | €176,37 | €881,84 | €0,00 | €1,97 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 1 | €10.003,36 | €10,00 | €150,00 | €2,20 | €-1,16 |
| TEST | Scalp RSI Short 80 · €50 · 15x | 1 | €10.002,36 | €50,00 | €750,00 | €0,00 | €1,67 |
| TEST | Scalp RSI Long 25 · €50 · 15x | 0 | €10.001,47 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · prudente · 5x | 1 | €10.001,44 | €176,32 | €881,59 | €0,00 | €1,97 |
| TEST | Scalp RSI Short 85 · €50 · 15x | 1 | €10.001,22 | €50,00 | €750,00 | €0,00 | €1,67 |
| TEST | Scalp RSI Short 80 · €10 · 15x | 1 | €10.000,47 | €10,00 | €150,00 | €0,00 | €0,33 |
| TEST | Scalp RSI Long 25 · €10 · 15x | 0 | €10.000,29 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 85 · €10 · 15x | 1 | €10.000,24 | €10,00 | €150,00 | €0,00 | €0,33 |
| TEST | Scanner Bottom5 Short Continuation V1 | 0 | €10.000,00 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €10 · 15x | 0 | €9.998,96 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Donchian 1H | 0 | €9.998,75 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €10 · 15x | 0 | €9.998,50 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Balanced Short Trend Down Strict V1 | 0 | €9.995,87 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · €50 · 15x | 0 | €9.994,81 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · €50 · 15x | 0 | €9.992,50 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 15 · prudente · 5x | 0 | €9.988,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 No Esports V1 | 5 | €9.983,82 | €2.695,87 | €8.087,60 | €201,08 | €-19,59 |
| TEST | Scalp RSI Long 20 · prudente · 5x | 0 | €9.983,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V1 | 2 | €9.983,53 | €1.645,02 | €4.935,06 | €99,89 | €9,36 |
| TEST | Btc Donchian 1H | 0 | €9.980,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Balanced V3 Long Only V1 | 3 | €9.978,39 | €1.399,40 | €4.198,19 | €149,54 | €-1,90 |
| TEST | Sol Ema 1H | 0 | €9.977,09 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · prudente · 5x | 0 | €9.976,99 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Expanded V1 | 5 | €9.975,46 | €1.484,40 | €2.968,80 | €198,70 | €9,35 |
| TEST | Combo Adaptive Regime V1 | 2 | €9.975,22 | €964,46 | €1.928,92 | €98,78 | €0,00 |
| TEST | Combo Adaptive Long Only V1 | 5 | €9.974,92 | €2.708,23 | €5.416,47 | €199,67 | €10,84 |
| TEST | Sol Donchian 4H | 1 | €9.967,08 | €830,21 | €1.660,43 | €49,74 | €19,86 |
| TEST | Sol Adaptive 4H | 1 | €9.965,66 | €761,04 | €1.522,08 | €49,74 | €18,21 |
| TEST | Combo Adaptive Tp3 V1 | 4 | €9.957,02 | €2.226,41 | €4.452,81 | €198,61 | €27,45 |
| TEST | 1H Fast V3 Nohigh V1 | 5 | €9.956,83 | €2.688,58 | €8.065,74 | €200,53 | €-19,53 |
| TEST | Btc Ema 4H | 0 | €9.950,68 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Donchian 4H | 0 | €9.950,68 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Adaptive 4H | 0 | €9.949,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 1 | €9.949,37 | €135,73 | €678,63 | €9,96 | €-5,25 |
| TEST | Sol Ema 4H | 1 | €9.947,15 | €862,58 | €1.725,17 | €49,74 | €0,05 |
| TEST | Eth Ema 4H | 0 | €9.947,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 1H | 1 | €9.945,65 | €1.153,43 | €3.460,30 | €49,83 | €-18,81 |
| TEST | Ampia 4H | 4 | €9.942,56 | €1.734,53 | €3.469,06 | €199,10 | €-2,77 |
| TEST | Master Adaptive Runner25 V1 | 6 | €9.939,99 | €1.485,57 | €2.971,14 | €198,28 | €10,04 |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | 2 | €9.931,24 | €1.092,52 | €2.185,03 | €100,07 | €0,00 |
| TEST | Master Adaptive V1 | 5 | €9.930,41 | €1.470,56 | €2.941,12 | €197,82 | €9,31 |
| TEST | Master Adaptive No Alt V1 | 5 | €9.930,41 | €1.470,56 | €2.941,12 | €197,82 | €9,31 |
| TEST | 1H Fast V3 Long Only V1 | 5 | €9.927,79 | €716,73 | €2.150,19 | €147,47 | €28,46 |
| TEST | Eth Donchian 1H | 0 | €9.927,32 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | 5 | €9.922,29 | €1.507,45 | €3.014,91 | €198,45 | €6,09 |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | 1 | €9.916,34 | €864,27 | €1.728,54 | €49,61 | €0,00 |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | 2 | €9.912,33 | €1.154,19 | €2.308,39 | €50,00 | €43,68 |
| TEST | Scanner Bottom5 Short Profit Lock V1 | 2 | €9.904,64 | €1.186,90 | €2.373,81 | €50,00 | €57,16 |
| TEST | Benchmark Bollinger mean reversion 1H | 3 | €9.902,27 | €3.619,03 | €7.238,05 | €148,10 | €-27,19 |
| TEST | Sol Bollinger 1H | 0 | €9.901,25 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Bollinger 1H | 0 | €9.888,87 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Eth Adaptive 1H | 1 | €9.883,74 | €1.146,74 | €3.440,21 | €49,54 | €-22,43 |
| TEST | Combo Adaptive Quality7 Regime V1 | 1 | €9.855,64 | €864,27 | €1.728,54 | €49,61 | €0,00 |
| TEST | Combo Adaptive Partial 1R V1 | 5 | €9.841,81 | €2.198,16 | €4.396,33 | €196,58 | €13,21 |
| TEST | Sol Adaptive 1H | 0 | €9.835,19 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Trend | 5 | €9.820,14 | €828,63 | €1.657,26 | €148,07 | €30,28 |
| TEST | Forza relativa 1H V1 | 5 | €9.818,10 | €1.591,35 | €3.182,70 | €196,22 | €-0,41 |
| TEST | Scanner Top5 Btc Mfe V1 | 4 | €9.815,04 | €3.909,71 | €7.819,43 | €196,28 | €4,94 |
| TEST | Eth Ema 1H | 1 | €9.811,38 | €1.138,34 | €3.415,02 | €49,18 | €-22,27 |
| TEST | Scanner Top5 Btc Guard Mfe V1 | 5 | €9.809,46 | €1.382,81 | €2.765,62 | €196,20 | €5,85 |
| TEST | Global Confluence puro 1H | 0 | €9.790,66 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Gb20 V1 | 4 | €9.787,75 | €2.601,69 | €5.203,39 | €194,79 | €36,10 |
| TEST | Scanner Bottom10 Short | 2 | €9.778,08 | €1.977,42 | €3.954,85 | €49,86 | €56,50 |
| TEST | Scanner Bottom15 Short | 2 | €9.778,08 | €1.977,42 | €3.954,85 | €49,86 | €56,50 |
| TEST | Scanner Bottom20 Short | 2 | €9.778,08 | €1.977,42 | €3.954,85 | €49,86 | €56,50 |
| TEST | Master Adaptive Strict3 V1 | 4 | €9.761,34 | €2.622,84 | €5.245,67 | €194,80 | €7,96 |
| TEST | Scanner Bottom 5 Short 1H | 2 | €9.733,69 | €1.583,60 | €3.167,19 | €48,61 | €27,12 |
| TEST | Combo Adaptive Mfe Trail | 4 | €9.517,83 | €2.034,13 | €4.068,27 | €190,44 | €-4,05 |

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
| PRINCIPALE | Principale 4H | Confluenza trend | €9.892,26 | €-105,47 | 19 | 19 | 31,58% | 0,83 | €-5,55 | 4,26% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €10.849,66 | €839,79 | 32 | 32 | 56,25% | 2,58 | €26,24 | 2,70% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €10.618,01 | €608,72 | 25 | 25 | 52,00% | 2,54 | €24,35 | 2,01% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €10.589,50 | €567,43 | 42 | 42 | 54,76% | 1,77 | €13,51 | 2,30% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €10.568,52 | €470,50 | 23 | 23 | 52,17% | 1,98 | €20,46 | 2,12% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €10.562,11 | €564,43 | 41 | 41 | 46,34% | 1,61 | €13,77 | 2,20% |
| TEST | 1H Fast Nohigh Cap75 V1 | Momentum / breakout | €10.466,68 | €411,18 | 44 | 44 | 47,73% | 1,46 | €9,35 | 2,83% |
| TEST | 1H Fast V3 Cap75 V1 | Momentum / breakout V3 Filtered | €10.438,41 | €392,02 | 38 | 38 | 47,37% | 1,56 | €10,32 | 2,49% |
| TEST | 1H Fast Score 6 75 V1 | Momentum / breakout | €10.412,70 | €348,72 | 42 | 42 | 45,24% | 1,45 | €8,30 | 2,49% |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | Momentum / breakout | €10.389,24 | €383,78 | 7 | 7 | 85,71% | 7,91 | €54,83 | 1,17% |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | Momentum / breakout V3 Filtered | €10.360,00 | €259,81 | 7 | 7 | 71,43% | 3,37 | €37,12 | 1,39% |
| TEST | Scanner Top5 Btc Runner25 V1 | Scanner Top 5 + forza BTC | €10.328,84 | €319,70 | 11 | 11 | 63,64% | 2,96 | €29,06 | 2,33% |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | Momentum / breakout V3 Filtered | €10.325,86 | €194,64 | 2 | 2 | 100,00% | ∞ | €97,32 | 0,53% |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | Momentum / breakout | €10.311,65 | €253,41 | 9 | 9 | 66,67% | 2,85 | €28,16 | 2,01% |
| TEST | Scanner Top5 Btc Tp3 V1 | Scanner Top 5 + forza BTC | €10.300,57 | €292,54 | 9 | 9 | 66,67% | 2,79 | €32,50 | 2,33% |
| TEST | 1H Fast Score 6 75 Range Only V1 | Momentum / breakout | €10.283,89 | €224,99 | 8 | 8 | 62,50% | 2,65 | €28,12 | 2,28% |
| TEST | 1H Fast V3 Nohigh Range Only V1 | Momentum / breakout V3 Filtered | €10.283,51 | €184,00 | 6 | 6 | 66,67% | 2,68 | €30,67 | 1,78% |
| TEST | Combo Adaptive Side Regime Guard V1 | Combo Adaptive | €10.277,69 | €179,50 | 5 | 5 | 80,00% | 4,22 | €35,90 | 0,82% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | Momentum / breakout V3 Filtered | €10.274,80 | €175,05 | 3 | 3 | 66,67% | 9,31 | €58,35 | 0,70% |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | Momentum / breakout V3 Filtered | €10.242,04 | €110,11 | 5 | 5 | 80,00% | 2,98 | €22,02 | 0,95% |
| TEST | Combo Adaptive | Combo Adaptive | €10.230,73 | €205,57 | 24 | 24 | 45,83% | 1,52 | €8,57 | 1,49% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €10.230,51 | €237,19 | 32 | 30 | 53,12% | 1,39 | €7,41 | 2,75% |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | Scanner Top 5 + forza BTC | €10.226,94 | €217,93 | 6 | 6 | 66,67% | 2,84 | €36,32 | 1,64% |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | Momentum / breakout V3 Filtered | €10.226,51 | €231,10 | 16 | 16 | 56,25% | 1,96 | €14,44 | 2,05% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | Momentum / breakout V3 Filtered | €10.221,80 | €175,37 | 3 | 3 | 66,67% | 9,32 | €58,46 | 0,69% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | Momentum / breakout V3 Filtered | €10.216,50 | €175,30 | 3 | 3 | 66,67% | 9,32 | €58,43 | 0,68% |
| TEST | Scanner Top5 Btc Btc Le3 V1 | Scanner Top 5 + forza BTC | €10.197,83 | €188,80 | 7 | 7 | 57,14% | 2,74 | €26,97 | 2,20% |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | Momentum / breakout | €10.194,26 | €103,39 | 6 | 6 | 66,67% | 2,42 | €17,23 | 1,39% |
| TEST | Rapida 1H V3 Filtered | Momentum / breakout V3 Filtered | €10.191,37 | €215,90 | 71 | 71 | 38,03% | 1,15 | €3,04 | 2,89% |
| TEST | Combo Scanner | Combo Scanner | €10.187,58 | €178,10 | 28 | 28 | 46,43% | 1,27 | €6,36 | 2,66% |
| TEST | Main Dynamic Asset Selector V1 | Confluenza trend | €10.186,76 | €198,64 | 2 | 2 | 100,00% | ∞ | €99,32 | 0,60% |
| TEST | Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | Momentum / breakout V3 Filtered | €10.181,67 | €21,84 | 1 | 1 | 100,00% | ∞ | €21,84 | 0,45% |
| TEST | Main Side Regime Guard V1 | Confluenza trend | €10.179,86 | €144,49 | 3 | 3 | 66,67% | 3,67 | €48,16 | 0,63% |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | Momentum / breakout V3 Filtered | €10.174,35 | €21,84 | 1 | 1 | 100,00% | ∞ | €21,84 | 0,46% |
| TEST | Combo Trend Side Regime Guard V1 | Combo Trend | €10.171,29 | €111,07 | 5 | 5 | 60,00% | 2,01 | €22,21 | 0,95% |
| TEST | 1H Fast V3 No Esports Long Only V1 | Momentum / breakout V3 Filtered | €10.158,50 | €72,32 | 8 | 8 | 50,00% | 1,33 | €9,04 | 1,32% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €10.137,59 | €144,76 | 39 | 38 | 38,46% | 1,12 | €3,71 | 3,69% |
| TEST | 1H Fast No Pepe V1 | Momentum / breakout | €10.133,50 | €157,89 | 39 | 39 | 41,03% | 1,19 | €4,05 | 2,10% |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | Momentum / breakout V3 Filtered | €10.129,90 | €-30,71 | 4 | 4 | 25,00% | 0,75 | €-7,68 | 1,60% |
| TEST | 1H Fast Tp2 V1 | Momentum / breakout | €10.128,03 | €64,13 | 40 | 40 | 35,00% | 1,08 | €1,60 | 2,58% |
| TEST | Scanner Top10 Long | Scanner Top10 Long | €10.124,29 | €101,43 | 3 | 3 | 66,67% | 330,83 | €33,81 | 0,55% |
| TEST | Scanner Top15 Long | Scanner Top15 Long | €10.124,29 | €101,43 | 3 | 3 | 66,67% | 330,83 | €33,81 | 0,55% |
| TEST | Scanner Top20 Long | Scanner Top20 Long | €10.124,29 | €101,43 | 3 | 3 | 66,67% | 330,83 | €33,81 | 0,55% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | Momentum / breakout V3 Filtered | €10.121,49 | €33,74 | 3 | 3 | 33,33% | 1,56 | €11,25 | 1,21% |
| TEST | Master Adaptive Gb20 Loss Cap V1 | Master Adaptive Consensus | €10.120,67 | €44,66 | 5 | 5 | 40,00% | 1,50 | €8,93 | 0,87% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.118,93 | €99,96 | 2 | 2 | 100,00% | ∞ | €49,98 | 0,54% |
| TEST | Master Adaptive Gb20 Be V1 | Master Adaptive Consensus | €10.117,78 | €114,66 | 5 | 5 | 40,00% | 2,37 | €22,93 | 0,46% |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | Momentum / breakout V3 Filtered | €10.112,33 | €30,69 | 4 | 4 | 50,00% | 1,28 | €7,67 | 0,81% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €10.100,35 | €69,11 | 15 | 15 | 40,00% | 1,18 | €4,61 | 2,31% |
| TEST | Combo Adaptive Runner25 V1 | Combo Adaptive | €10.100,27 | €74,96 | 19 | 19 | 42,11% | 1,17 | €3,95 | 2,12% |
| TEST | Combo Adaptive Quality7 V1 | Combo Adaptive | €10.093,99 | €66,92 | 13 | 13 | 46,15% | 1,38 | €5,15 | 1,51% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €10.092,12 | €92,12 | 3 | 3 | 66,67% | 21,53 | €30,71 | 0,79% |
| TEST | Doge Ema 1H | Trend following EMA | €10.091,86 | €91,86 | 8 | 8 | 62,50% | 1,55 | €11,48 | 1,36% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €10.087,47 | €92,66 | 12 | 11 | 50,00% | 1,36 | €7,72 | 1,69% |
| TEST | Sol Bollinger 4H | Bollinger mean reversion | €10.086,98 | €86,98 | 1 | 1 | 100,00% | ∞ | €86,98 | 0,40% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.084,12 | €84,12 | 1 | 1 | 100,00% | ∞ | €84,12 | 0,30% |
| TEST | Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | Momentum / breakout V3 Filtered | €10.081,39 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,10% |
| TEST | 1H Balanced Long No Rhv V1 | Confluenza trend | €10.065,96 | €58,73 | 5 | 5 | 40,00% | 1,42 | €11,75 | 0,88% |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | Momentum / breakout V3 Filtered | €10.065,64 | €23,89 | 27 | 27 | 40,74% | 1,03 | €0,88 | 2,86% |
| TEST | Master Adaptive Gb20 Partial V1 | Master Adaptive Consensus | €10.062,65 | €59,52 | 4 | 4 | 50,00% | 1,75 | €14,88 | 0,51% |
| TEST | Scanner Top5 Btc Guard V1 | Scanner Top 5 + forza BTC | €10.059,50 | €50,52 | 9 | 9 | 44,44% | 1,18 | €5,61 | 3,31% |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | Momentum / breakout | €10.056,58 | €56,58 | 13 | 13 | 30,77% | 1,24 | €4,35 | 1,92% |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | Momentum / breakout V3 Filtered | €10.042,59 | €0,96 | 28 | 28 | 50,00% | 1,00 | €0,03 | 3,21% |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | Momentum / breakout V3 Filtered | €10.035,75 | €-65,67 | 1 | 1 | 0,00% | 0,00 | €-65,67 | 0,96% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | Momentum / breakout V3 Filtered | €10.035,75 | €-65,67 | 1 | 1 | 0,00% | 0,00 | €-65,67 | 0,96% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €10.016,78 | €23,04 | 8 | 8 | 37,50% | 1,65 | €2,88 | 0,25% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €10.015,45 | €15,45 | 1 | 1 | 100,00% | ∞ | €15,45 | 0,51% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €10.013,28 | €13,28 | 3 | 3 | 66,67% | 1,24 | €4,43 | 0,89% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €10.004,98 | €-53,60 | 23 | 23 | 34,78% | 0,91 | €-2,33 | 2,25% |
| TEST | Scalp RSI Short 80 · prudente · 5x | Inversione RSI estrema 15m | €10.004,22 | €2,78 | 1 | 1 | 100,00% | ∞ | €2,78 | 0,07% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €10.003,36 | €4,61 | 8 | 8 | 37,50% | 1,65 | €0,58 | 0,05% |
| TEST | Scalp RSI Short 80 · €50 · 15x | Inversione RSI estrema 15m | €10.002,36 | €1,14 | 1 | 1 | 100,00% | ∞ | €1,14 | 0,06% |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | €10.001,47 | €1,47 | 5 | 5 | 40,00% | 1,12 | €0,29 | 0,13% |
| TEST | Scalp RSI Short 85 · prudente · 5x | Inversione RSI estrema 15m | €10.001,44 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,07% |
| TEST | Scalp RSI Short 85 · €50 · 15x | Inversione RSI estrema 15m | €10.001,22 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,06% |
| TEST | Scalp RSI Short 80 · €10 · 15x | Inversione RSI estrema 15m | €10.000,47 | €0,23 | 1 | 1 | 100,00% | ∞ | €0,23 | 0,01% |
| TEST | Scalp RSI Long 25 · €10 · 15x | Inversione RSI estrema 15m | €10.000,29 | €0,29 | 5 | 5 | 40,00% | 1,12 | €0,06 | 0,03% |
| TEST | Scalp RSI Short 85 · €10 · 15x | Inversione RSI estrema 15m | €10.000,24 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,01% |
| TEST | Scanner Bottom5 Short Continuation V1 | Scanner Bottom5 Short Continuation | €10.000,00 | €0,00 | 0 | 0 | 0,00% | 0,00 | €0,00 | 0,00% |
| TEST | Scalp RSI Long 20 · €10 · 15x | Inversione RSI estrema 15m | €9.998,96 | €-1,04 | 2 | 2 | 0,00% | 0,00 | €-0,52 | 0,02% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €9.998,75 | €-1,25 | 4 | 4 | 75,00% | 0,98 | €-0,31 | 0,96% |
| TEST | Scalp RSI Long 15 · €10 · 15x | Inversione RSI estrema 15m | €9.998,50 | €-1,50 | 1 | 1 | 0,00% | 0,00 | €-1,50 | 0,02% |
| TEST | 1H Balanced Short Trend Down Strict V1 | Confluenza trend | €9.995,87 | €-4,13 | 1 | 1 | 0,00% | 0,00 | €-4,13 | 0,59% |
| TEST | Scalp RSI Long 20 · €50 · 15x | Inversione RSI estrema 15m | €9.994,81 | €-5,19 | 2 | 2 | 0,00% | 0,00 | €-2,59 | 0,08% |
| TEST | Scalp RSI Long 15 · €50 · 15x | Inversione RSI estrema 15m | €9.992,50 | €-7,50 | 1 | 1 | 0,00% | 0,00 | €-7,50 | 0,11% |
| TEST | Scalp RSI Long 15 · prudente · 5x | Inversione RSI estrema 15m | €9.988,38 | €-11,62 | 1 | 1 | 0,00% | 0,00 | €-11,62 | 0,17% |
| TEST | 1H Fast V3 No Esports V1 | Momentum / breakout V3 Filtered | €9.983,82 | €7,88 | 45 | 45 | 37,78% | 1,01 | €0,18 | 2,49% |
| TEST | Scalp RSI Long 20 · prudente · 5x | Inversione RSI estrema 15m | €9.983,60 | €-16,40 | 2 | 2 | 0,00% | 0,00 | €-8,20 | 0,24% |
| TEST | Rapida 1H V1 | Momentum / breakout | €9.983,53 | €-23,25 | 76 | 76 | 34,21% | 0,99 | €-0,31 | 6,76% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €9.980,62 | €-19,38 | 4 | 4 | 50,00% | 0,82 | €-4,84 | 1,49% |
| TEST | 1H Balanced V3 Long Only V1 | Confluenza trend V3 Filtered | €9.978,39 | €-17,68 | 4 | 4 | 25,00% | 0,84 | €-4,42 | 1,46% |
| TEST | Sol Ema 1H | Trend following EMA | €9.977,09 | €-22,91 | 5 | 5 | 40,00% | 0,86 | €-4,58 | 1,67% |
| TEST | Scalp RSI Long 25 · prudente · 5x | Inversione RSI estrema 15m | €9.976,99 | €-23,01 | 5 | 5 | 20,00% | 0,20 | €-4,60 | 0,37% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €9.975,46 | €-32,18 | 10 | 10 | 40,00% | 0,90 | €-3,22 | 2,80% |
| TEST | Combo Adaptive Regime V1 | Combo Adaptive | €9.975,22 | €-23,53 | 10 | 10 | 50,00% | 0,92 | €-2,35 | 2,18% |
| TEST | Combo Adaptive Long Only V1 | Combo Adaptive | €9.974,92 | €-32,81 | 8 | 8 | 37,50% | 0,86 | €-4,10 | 2,34% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €9.967,08 | €-52,00 | 1 | 1 | 0,00% | 0,00 | €-52,00 | 0,60% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €9.965,66 | €-51,83 | 1 | 1 | 0,00% | 0,00 | €-51,83 | 0,59% |
| TEST | Combo Adaptive Tp3 V1 | Combo Adaptive | €9.957,02 | €-67,05 | 12 | 12 | 41,67% | 0,76 | €-5,59 | 1,41% |
| TEST | 1H Fast V3 Nohigh V1 | Momentum / breakout V3 Filtered | €9.956,83 | €-19,17 | 46 | 46 | 39,13% | 0,98 | €-0,42 | 2,96% |
| TEST | Btc Ema 4H | Trend following EMA | €9.950,68 | €-49,32 | 1 | 1 | 0,00% | 0,00 | €-49,32 | 0,96% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €9.950,68 | €-49,32 | 1 | 1 | 0,00% | 0,00 | €-49,32 | 0,96% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €9.949,62 | €-50,38 | 1 | 1 | 0,00% | 0,00 | €-50,38 | 0,74% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.949,37 | €-44,97 | 8 | 8 | 25,00% | 0,19 | €-5,62 | 0,51% |
| TEST | Sol Ema 4H | Trend following EMA | €9.947,15 | €-52,00 | 1 | 1 | 0,00% | 0,00 | €-52,00 | 0,57% |
| TEST | Eth Ema 4H | Trend following EMA | €9.947,12 | €-52,88 | 1 | 1 | 0,00% | 0,00 | €-52,88 | 0,68% |
| TEST | Btc Ema 1H | Trend following EMA | €9.945,65 | €-34,33 | 5 | 5 | 40,00% | 0,79 | €-6,87 | 1,56% |
| TEST | Ampia 4H | Confluenza trend | €9.942,56 | €-53,35 | 17 | 17 | 23,53% | 0,89 | €-3,14 | 3,67% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €9.939,99 | €-68,32 | 8 | 8 | 25,00% | 0,75 | €-8,54 | 3,19% |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | Scanner Top 5 + forza BTC | €9.931,24 | €-67,07 | 4 | 4 | 25,00% | 0,47 | €-16,77 | 2,38% |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | €9.930,41 | €-77,20 | 7 | 7 | 28,57% | 0,72 | €-11,03 | 3,19% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €9.930,41 | €-77,20 | 7 | 7 | 28,57% | 0,72 | €-11,03 | 3,19% |
| TEST | 1H Fast V3 Long Only V1 | Momentum / breakout V3 Filtered | €9.927,79 | €-99,47 | 30 | 30 | 30,00% | 0,87 | €-3,32 | 3,65% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.927,32 | €-72,68 | 4 | 4 | 25,00% | 0,56 | €-18,17 | 1,38% |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | Scanner Top 5 + forza BTC | €9.922,29 | €-82,50 | 20 | 20 | 40,00% | 0,83 | €-4,13 | 2,88% |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | Combo Adaptive | €9.916,34 | €-82,62 | 5 | 5 | 40,00% | 0,48 | €-16,52 | 1,95% |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | Scanner Bottom 5 Short | €9.912,33 | €-129,97 | 4 | 4 | 25,00% | 0,20 | €-32,49 | 1,38% |
| TEST | Scanner Bottom5 Short Profit Lock V1 | Scanner Bottom 5 Short | €9.904,64 | €-151,10 | 4 | 4 | 25,00% | 0,05 | €-37,77 | 1,53% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €9.902,27 | €-65,16 | 33 | 33 | 39,39% | 0,92 | €-1,97 | 3,25% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.901,25 | €-98,75 | 4 | 4 | 25,00% | 0,41 | €-24,69 | 1,89% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €9.888,87 | €-111,13 | 2 | 2 | 0,00% | 0,00 | €-55,56 | 1,26% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.883,74 | €-92,21 | 4 | 4 | 50,00% | 0,16 | €-23,05 | 1,24% |
| TEST | Combo Adaptive Quality7 Regime V1 | Combo Adaptive | €9.855,64 | €-143,33 | 5 | 5 | 20,00% | 0,17 | €-28,67 | 1,95% |
| TEST | Combo Adaptive Partial 1R V1 | Combo Adaptive | €9.841,81 | €-168,17 | 14 | 14 | 42,86% | 0,62 | €-12,01 | 2,24% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €9.835,19 | €-164,81 | 6 | 6 | 33,33% | 0,29 | €-27,47 | 2,34% |
| TEST | Combo Trend | Combo Trend | €9.820,14 | €-209,42 | 33 | 33 | 30,30% | 0,82 | €-6,35 | 4,86% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €9.818,10 | €-179,89 | 26 | 26 | 26,92% | 0,72 | €-6,92 | 4,25% |
| TEST | Scanner Top5 Btc Mfe V1 | Scanner Top 5 + forza BTC | €9.815,04 | €-185,85 | 16 | 16 | 37,50% | 0,52 | €-11,62 | 3,95% |
| TEST | Eth Ema 1H | Trend following EMA | €9.811,38 | €-164,74 | 6 | 6 | 33,33% | 0,25 | €-27,46 | 1,92% |
| TEST | Scanner Top5 Btc Guard Mfe V1 | Scanner Top 5 + forza BTC | €9.809,46 | €-195,36 | 23 | 23 | 34,78% | 0,66 | €-8,49 | 4,05% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.790,66 | €-209,34 | 10 | 10 | 30,00% | 0,37 | €-20,93 | 2,92% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €9.787,75 | €-245,24 | 40 | 40 | 60,00% | 0,65 | €-6,13 | 4,16% |
| TEST | Scanner Bottom10 Short | Scanner Bottom10 Short | €9.778,08 | €-276,05 | 5 | 5 | 0,00% | 0,00 | €-55,21 | 2,72% |
| TEST | Scanner Bottom15 Short | Scanner Bottom15 Short | €9.778,08 | €-276,05 | 5 | 5 | 0,00% | 0,00 | €-55,21 | 2,72% |
| TEST | Scanner Bottom20 Short | Scanner Bottom20 Short | €9.778,08 | €-276,05 | 5 | 5 | 0,00% | 0,00 | €-55,21 | 2,72% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €9.761,34 | €-243,80 | 17 | 17 | 29,41% | 0,66 | €-14,34 | 4,69% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.733,69 | €-288,92 | 29 | 29 | 31,03% | 0,61 | €-9,96 | 5,48% |
| TEST | Combo Adaptive Mfe Trail | Combo Adaptive | €9.517,83 | €-475,61 | 29 | 29 | 27,59% | 0,39 | €-16,40 | 5,33% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | LAB | SHORT | Confluenza trend | 240m | 3,0x | 0,17841 | 0,17841 | 0,17841 | 0,23699 | 0,13559 | €136,26 | €408,77 | €0,00 | €-0,00 |
| Principale 4H | SUI | LONG | Confluenza trend | 240m | 3,0x | 0,76296 | 0,76296 | 0,73998 | 0,51245 | 0,80891 | €547,52 | €1.642,56 | €49,46 | €0,00 |
| Principale 4H | ONDO | LONG | Confluenza trend | 240m | 3,0x | 0,40344 | 0,40344 | 0,37762 | 0,27098 | 0,45509 | €254,70 | €764,09 | €48,91 | €0,00 |
| Principale 4H | SOL | SHORT | Confluenza trend | 240m | 3,0x | 73,82923 | 75,05500 | 75,57185 | 98,06983 | 70,34400 | €20,35 | €61,04 | €1,44 | €-1,01 |
| Principale 4H | ESPORTS | LONG | Confluenza trend | 240m | 3,0x | 0,05372 | 0,05372 | 0,04728 | 0,03608 | 0,06662 | €136,09 | €408,26 | €48,99 | €0,00 |
| Bilanciata 1H V1 | ONDO | LONG | Confluenza trend | 60m | 3,0x | 0,39694 | 0,39694 | 0,38539 | 0,26661 | 0,42004 | €581,76 | €1.745,29 | €50,78 | €0,00 |
| Bilanciata 1H V1 | ADA | SHORT | Confluenza trend | 60m | 3,0x | 0,16703 | 0,16703 | 0,16365 | 0,22187 | 0,16112 | €978,72 | €2.936,17 | €0,00 | €-0,00 |
| Bilanciata 1H V1 | AKE | LONG | Confluenza trend | 60m | 3,0x | 0,00329 | 0,00326 | 0,00290 | 0,00221 | 0,00408 | €12,36 | €37,07 | €4,45 | €-0,36 |
| Bilanciata 1H V1 | ESPORTS | LONG | Confluenza trend | 60m | 3,0x | 0,05372 | 0,05372 | 0,04728 | 0,03608 | 0,06662 | €147,42 | €442,26 | €53,07 | €0,00 |
| Bilanciata 1H V1 | ALLO | SHORT | Confluenza trend | 60m | 3,0x | 0,36179 | 0,33757 | 0,40521 | 0,48058 | 0,27496 | €141,53 | €424,59 | €50,95 | €28,43 |
| Bilanciata 1H V1 | PEPE | LONG | Confluenza trend | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €9,26 | €27,78 | €0,60 | €-0,02 |
| 1H Balanced Long No Rhv V1 | AKE | LONG | Confluenza trend | 60m | 3,0x | 0,00320 | 0,00326 | 0,00282 | 0,00215 | 0,00397 | €138,85 | €416,55 | €49,99 | €8,22 |
| 1H Balanced Long No Rhv V1 | BEAT | LONG | Confluenza trend | 60m | 3,0x | 3,29017 | 3,29017 | 3,00714 | 2,20990 | 3,85623 | €193,69 | €581,07 | €49,98 | €0,00 |
| 1H Balanced Long No Rhv V1 | XMR | LONG | Confluenza trend | 60m | 3,0x | 366,72991 | 366,72991 | 360,04130 | 246,32025 | 380,10712 | €915,26 | €2.745,79 | €50,08 | €0,00 |
| 1H Balanced Long No Rhv V1 | ESPORTS | LONG | Confluenza trend | 60m | 3,0x | 0,05372 | 0,05372 | 0,04728 | 0,03608 | 0,06662 | €139,74 | €419,23 | €50,31 | €0,00 |
| 1H Balanced Long No Rhv V1 | PEPE | LONG | Confluenza trend | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €19,34 | €58,02 | €0,00 | €1,21 |
| Bilanciata 1H V2 | ADA | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,16276 | 0,16276 | 0,16511 | 0,21620 | 0,15807 | €1.185,56 | €3.556,68 | €51,22 | €-0,00 |
| Bilanciata 1H V2 | AKE | LONG | Confluenza trend V2 | 60m | 3,0x | 0,00320 | 0,00326 | 0,00282 | 0,00215 | 0,00397 | €142,81 | €428,43 | €51,41 | €8,26 |
| Bilanciata 1H V2 | WLD | SHORT | Confluenza trend V2 | 60m | 3,0x | 0,34349 | 0,34349 | 0,35287 | 0,45627 | 0,32475 | €26,53 | €79,60 | €2,17 | €-0,00 |
| Bilanciata 1H V2 | ESPORTS | LONG | Confluenza trend V2 | 60m | 3,0x | 0,05372 | 0,05372 | 0,04728 | 0,03608 | 0,06662 | €142,91 | €428,74 | €51,45 | €0,00 |
| Bilanciata 1H V2 | BANK | LONG | Confluenza trend V2 | 60m | 3,0x | 0,36742 | 0,35795 | 0,33054 | 0,24679 | 0,44120 | €161,71 | €485,13 | €48,70 | €-12,51 |
| Bilanciata 1H V3 Filtered | ONDO | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,40134 | 0,40134 | 0,38898 | 0,26957 | 0,42605 | €557,59 | €1.672,77 | €51,50 | €0,00 |
| Bilanciata 1H V3 Filtered | BEAT | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 3,31215 | 3,31215 | 3,02723 | 2,22466 | 3,88198 | €203,36 | €610,09 | €52,48 | €0,00 |
| Bilanciata 1H V3 Filtered | WLD | SHORT | Confluenza trend V3 Filtered | 60m | 3,0x | 0,34349 | 0,34349 | 0,35287 | 0,45627 | 0,32475 | €23,43 | €70,29 | €1,92 | €-0,00 |
| Bilanciata 1H V3 Filtered | BANK | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,35497 | 0,35795 | 0,35497 | 0,23842 | 0,43149 | €162,02 | €486,06 | €0,00 | €4,08 |
| Bilanciata 1H V3 Filtered | AKE | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,00330 | 0,00326 | 0,00293 | 0,00221 | 0,00403 | €158,25 | €474,75 | €52,90 | €-4,71 |
| Rapida 1H V1 | ADA | SHORT | Momentum / breakout | 60m | 3,0x | 0,16185 | 0,16185 | 0,16367 | 0,21499 | 0,15913 | €1.486,90 | €4.460,70 | €49,96 | €-0,00 |
| Rapida 1H V1 | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00320 | 0,00326 | 0,00286 | 0,00215 | 0,00370 | €158,12 | €474,35 | €49,93 | €9,36 |
| 1H Fast Score 6 75 V1 | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00320 | 0,00326 | 0,00287 | 0,00215 | 0,00369 | €167,22 | €501,65 | €51,54 | €9,99 |
| 1H Fast Score 6 75 V1 | ALLO | SHORT | Momentum / breakout | 60m | 3,0x | 0,37360 | 0,33757 | 0,35320 | 0,49626 | 0,32378 | €192,76 | €578,27 | €0,00 | €55,76 |
| 1H Fast Score 6 75 V1 | SHIB | LONG | Momentum / breakout | 60m | 3,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €466,78 | €1.400,34 | €52,07 | €-0,28 |
| 1H Fast Score 6 75 No Trend Up V1 | BEAT | LONG | Momentum / breakout | 60m | 3,0x | 3,29017 | 3,29017 | 3,07004 | 2,20990 | 3,62037 | €256,24 | €768,73 | €51,43 | €0,00 |
| 1H Fast Score 6 75 No Trend Up V1 | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00322 | 0,00326 | 0,00289 | 0,00216 | 0,00372 | €167,84 | €503,53 | €51,67 | €6,27 |
| 1H Fast Score 6 75 No Trend Up V1 | ALLO | SHORT | Momentum / breakout | 60m | 3,0x | 0,37360 | 0,33757 | 0,35320 | 0,49626 | 0,32378 | €185,15 | €555,44 | €0,00 | €53,56 |
| 1H Fast Score 6 75 No Trend Up V1 | SHIB | LONG | Momentum / breakout | 60m | 3,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €462,25 | €1.386,75 | €51,56 | €-0,28 |
| 1H Fast Score 6 75 Range Only V1 | BEAT | LONG | Momentum / breakout | 60m | 3,0x | 3,29017 | 3,29017 | 3,07004 | 2,20990 | 3,62037 | €256,24 | €768,73 | €51,43 | €0,00 |
| 1H Fast Score 6 75 Range Only V1 | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00322 | 0,00326 | 0,00289 | 0,00216 | 0,00372 | €167,84 | €503,53 | €51,67 | €6,27 |
| 1H Fast Score 6 75 Range Only V1 | ALLO | SHORT | Momentum / breakout | 60m | 3,0x | 0,37360 | 0,33757 | 0,35320 | 0,49626 | 0,32378 | €183,56 | €550,68 | €0,00 | €53,10 |
| 1H Fast Score 6 75 Cost Aware V1 | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00322 | 0,00326 | 0,00289 | 0,00216 | 0,00372 | €167,51 | €502,54 | €51,57 | €6,25 |
| 1H Fast Score 6 75 Cost Aware V1 | SHIB | LONG | Momentum / breakout | 60m | 3,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €465,73 | €1.397,19 | €51,95 | €-0,28 |
| 1H Fast Nohigh Cap75 V1 | BEAT | LONG | Momentum / breakout | 60m | 3,0x | 3,29017 | 3,29017 | 3,07004 | 2,20990 | 3,62037 | €257,44 | €772,31 | €51,67 | €0,00 |
| 1H Fast Nohigh Cap75 V1 | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00320 | 0,00326 | 0,00287 | 0,00215 | 0,00369 | €165,85 | €497,54 | €51,12 | €9,90 |
| 1H Fast Nohigh Cap75 V1 | EUL | LONG | Momentum / breakout | 60m | 3,0x | 2,14213 | 2,42460 | 1,88507 | 1,43880 | 2,52771 | €143,58 | €430,73 | €51,69 | €56,80 |
| 1H Fast Nohigh Cap75 V1 | PEPE | LONG | Momentum / breakout | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.045,31 | €3.135,93 | €52,26 | €-8,25 |
| 1H Fast Nohigh Cap75 V1 | SHIB | LONG | Momentum / breakout | 60m | 3,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €23,32 | €69,95 | €2,60 | €-0,01 |
| 1H Fast No Pepe V1 | ADA | SHORT | Momentum / breakout | 60m | 3,0x | 0,16185 | 0,16185 | 0,16367 | 0,21499 | 0,15913 | €1.512,75 | €4.538,24 | €50,83 | €-0,00 |
| 1H Fast No Pepe V1 | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00320 | 0,00326 | 0,00286 | 0,00215 | 0,00370 | €160,87 | €482,60 | €50,80 | €9,52 |
| 1H Fast No Pepe V1 | WLD | SHORT | Momentum / breakout | 60m | 3,0x | 0,34959 | 0,34959 | 0,35668 | 0,46437 | 0,33896 | €838,72 | €2.516,16 | €51,00 | €-0,00 |
| 1H Fast No Pepe V1 | BANK | LONG | Momentum / breakout | 60m | 3,0x | 0,37549 | 0,35795 | 0,34617 | 0,25220 | 0,41946 | €215,37 | €646,12 | €50,45 | €-30,17 |
| 1H Fast No Pepe V1 | SHIB | LONG | Momentum / breakout | 60m | 3,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €9,26 | €27,79 | €1,01 | €0,81 |
| 1H Fast Tp2 V1 | ADA | SHORT | Momentum / breakout | 60m | 3,0x | 0,16185 | 0,16185 | 0,16367 | 0,21499 | 0,15823 | €1.482,83 | €4.448,49 | €49,82 | €-0,00 |
| 1H Fast Tp2 V1 | AKE | LONG | Momentum / breakout | 60m | 3,0x | 0,00320 | 0,00326 | 0,00286 | 0,00215 | 0,00387 | €157,69 | €473,06 | €49,80 | €9,33 |
| 1H Fast Tp2 V1 | WLD | SHORT | Momentum / breakout | 60m | 3,0x | 0,34959 | 0,34959 | 0,35668 | 0,46437 | 0,33542 | €42,01 | €126,02 | €2,55 | €-0,00 |
| 1H Fast Tp2 V1 | ESPORTS | LONG | Momentum / breakout | 60m | 3,0x | 0,05372 | 0,05372 | 0,04728 | 0,03608 | 0,06662 | €139,31 | €417,93 | €50,15 | €0,00 |
| 1H Fast Tp2 V1 | BANK | LONG | Momentum / breakout | 60m | 3,0x | 0,37549 | 0,35795 | 0,34617 | 0,25220 | 0,43412 | €8,41 | €25,23 | €1,97 | €-1,18 |
| 1H Fast Tp2 V1 | SHIB | LONG | Momentum / breakout | 60m | 3,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €437,46 | €1.312,39 | €0,00 | €59,49 |
| 1H Fast Tp2 V1 | PEPE | LONG | Momentum / breakout | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €14,72 | €44,16 | €0,74 | €-0,02 |
| Rapida 1H V2 | TAO | SHORT | Momentum / breakout V2 | 60m | 3,0x | 188,48684 | 188,48684 | 190,75481 | 250,37335 | 185,08488 | €1.390,02 | €4.170,07 | €50,18 | €-0,00 |
| Rapida 1H V2 | ADA | SHORT | Momentum / breakout V2 | 60m | 3,0x | 0,16185 | 0,16185 | 0,16367 | 0,21499 | 0,15913 | €1.494,54 | €4.483,63 | €50,22 | €-0,00 |
| Rapida 1H V3 Filtered | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16185 | 0,16185 | 0,16367 | 0,21499 | 0,15913 | €1.521,20 | €4.563,60 | €51,11 | €-0,00 |
| Rapida 1H V3 Filtered | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00320 | 0,00326 | 0,00286 | 0,00215 | 0,00370 | €161,77 | €485,30 | €51,08 | €9,57 |
| Rapida 1H V3 Filtered | WLD | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,34959 | 0,34959 | 0,35668 | 0,46437 | 0,33896 | €843,41 | €2.530,22 | €51,28 | €-0,00 |
| Rapida 1H V3 Filtered | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,37549 | 0,35795 | 0,34617 | 0,25220 | 0,41946 | €216,68 | €650,05 | €50,76 | €-30,36 |
| Rapida 1H V3 Filtered | SHIB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €9,32 | €27,95 | €1,02 | €0,82 |
| 1H Fast V3 Cap75 V1 | BEAT | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 3,29017 | 3,29017 | 3,07004 | 2,20990 | 3,62037 | €258,77 | €776,32 | €51,94 | €0,00 |
| 1H Fast V3 Cap75 V1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00320 | 0,00326 | 0,00287 | 0,00215 | 0,00369 | €166,71 | €500,13 | €51,38 | €9,96 |
| 1H Fast V3 Cap75 V1 | EUL | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,22675 | 2,42460 | 1,95954 | 1,49563 | 2,62756 | €144,76 | €434,29 | €52,12 | €38,59 |
| 1H Fast V3 Cap75 V1 | SHIB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €467,93 | €1.403,80 | €52,20 | €-0,28 |
| 1H Fast V3 Nohigh V1 | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16185 | 0,16185 | 0,16367 | 0,21499 | 0,15913 | €1.485,86 | €4.457,58 | €49,92 | €-0,00 |
| 1H Fast V3 Nohigh V1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00320 | 0,00326 | 0,00286 | 0,00215 | 0,00370 | €158,01 | €474,02 | €49,90 | €9,35 |
| 1H Fast V3 Nohigh V1 | WLD | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,34959 | 0,34959 | 0,35668 | 0,46437 | 0,33896 | €823,75 | €2.471,25 | €50,08 | €-0,00 |
| 1H Fast V3 Nohigh V1 | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,37549 | 0,35795 | 0,34617 | 0,25220 | 0,41946 | €211,86 | €635,57 | €49,63 | €-29,68 |
| 1H Fast V3 Nohigh V1 | SHIB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €9,10 | €27,31 | €1,00 | €0,80 |
| 1H Fast V3 Long Only V1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00320 | 0,00326 | 0,00286 | 0,00215 | 0,00370 | €155,06 | €465,19 | €48,97 | €9,18 |
| 1H Fast V3 Long Only V1 | BEAT | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 3,29017 | 3,29017 | 3,07004 | 2,20990 | 3,62037 | €243,96 | €731,87 | €48,97 | €0,00 |
| 1H Fast V3 Long Only V1 | ESPORTS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,05372 | 0,05372 | 0,04728 | 0,03608 | 0,06339 | €137,59 | €412,76 | €49,53 | €0,00 |
| 1H Fast V3 Long Only V1 | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,34640 | 0,35795 | 0,35973 | 0,23266 | 0,39884 | €163,78 | €491,35 | €0,00 | €16,38 |
| 1H Fast V3 Long Only V1 | SHIB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €16,34 | €49,01 | €0,00 | €2,90 |
| 1H Fast V3 Long Nohigh Cap75 V1 | BEAT | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 3,29017 | 3,29017 | 3,07004 | 2,20990 | 3,62037 | €246,62 | €739,85 | €49,50 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 V1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00322 | 0,00326 | 0,00289 | 0,00216 | 0,00372 | €160,75 | €482,24 | €49,49 | €6,00 |
| 1H Fast V3 Long Nohigh Cap75 V1 | EUL | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,22675 | 2,42460 | 1,95954 | 1,49563 | 2,62756 | €139,59 | €418,78 | €50,25 | €37,21 |
| 1H Fast V3 Long Nohigh Cap75 V1 | SHIB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €451,22 | €1.353,67 | €50,33 | €-0,27 |
| 1H Fast V3 No Esports V1 | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16185 | 0,16185 | 0,16367 | 0,21499 | 0,15913 | €1.489,89 | €4.469,66 | €50,06 | €-0,00 |
| 1H Fast V3 No Esports V1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00320 | 0,00326 | 0,00286 | 0,00215 | 0,00370 | €158,44 | €475,31 | €50,03 | €9,38 |
| 1H Fast V3 No Esports V1 | WLD | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,34959 | 0,34959 | 0,35668 | 0,46437 | 0,33896 | €825,98 | €2.477,95 | €50,22 | €-0,00 |
| 1H Fast V3 No Esports V1 | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,37549 | 0,35795 | 0,34617 | 0,25220 | 0,41946 | €212,43 | €637,30 | €49,76 | €-29,76 |
| 1H Fast V3 No Esports V1 | SHIB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €9,13 | €27,38 | €1,00 | €0,80 |
| 1H Fast V3 No Esports Long Only V1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00320 | 0,00326 | 0,00286 | 0,00215 | 0,00370 | €158,13 | €474,39 | €49,94 | €9,36 |
| 1H Fast V3 No Esports Long Only V1 | BEAT | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 3,29017 | 3,29017 | 3,07004 | 2,20990 | 3,62037 | €248,78 | €746,34 | €49,93 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,34640 | 0,35795 | 0,35973 | 0,23266 | 0,39884 | €166,16 | €498,47 | €0,00 | €16,62 |
| 1H Fast V3 No Esports Long Only V1 | SHIB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €468,03 | €1.404,10 | €0,00 | €61,99 |
| 1H Fast V3 No Esports Mfe Lock V1 | ADA | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,16185 | 0,16185 | 0,16367 | 0,21499 | 0,15913 | €1.510,84 | €4.532,53 | €50,76 | €-0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | WLD | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,34959 | 0,34959 | 0,35668 | 0,46437 | 0,33896 | €11,86 | €35,57 | €0,72 | €-0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00322 | 0,00326 | 0,00322 | 0,00216 | 0,00368 | €177,09 | €531,27 | €0,00 | €6,68 |
| 1H Fast V3 No Esports Mfe Lock V1 | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,33165 | 0,33757 | 0,36472 | 0,44055 | 0,28205 | €170,96 | €512,89 | €51,14 | €-9,15 |
| 1H Fast V3 No Esports Mfe Lock V1 | SHIB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €14,38 | €43,13 | €1,57 | €1,26 |
| 1H Fast V3 No Esports Mfe Lock V1 | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,35802 | 0,35795 | 0,32525 | 0,24047 | 0,40718 | €180,50 | €541,49 | €49,57 | €-0,11 |
| 1H Fast V3 No Esports Stress Guard V1 | SHIB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €464,84 | €1.394,53 | €0,00 | €82,47 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | BEAT | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 3,29017 | 3,29017 | 3,07004 | 2,20990 | 3,62037 | €245,16 | €735,47 | €49,21 | €0,00 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00322 | 0,00326 | 0,00289 | 0,00216 | 0,00372 | €159,93 | €479,80 | €49,24 | €5,97 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | EUL | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,22675 | 2,42460 | 1,95954 | 1,49563 | 2,62756 | €139,27 | €417,82 | €50,14 | €37,12 |
| 1H Fast V3 Long Nohigh Cap75 Lock V1 | SHIB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €450,19 | €1.350,57 | €50,22 | €-0,27 |
| Ampia 4H | HYPE | SHORT | Confluenza trend | 240m | 2,0x | 58,36732 | 58,44100 | 61,80927 | 87,25915 | 48,72988 | €424,03 | €848,06 | €50,01 | €-1,07 |
| Ampia 4H | TAO | SHORT | Confluenza trend | 240m | 2,0x | 189,05650 | 189,05650 | 197,51338 | 282,63946 | 165,37722 | €558,68 | €1.117,36 | €49,98 | €-0,00 |
| Ampia 4H | AKE | LONG | Confluenza trend | 240m | 2,0x | 0,00328 | 0,00326 | 0,00288 | 0,00165 | 0,00438 | €207,40 | €414,80 | €49,78 | €-1,70 |
| Ampia 4H | XMR | LONG | Confluenza trend | 240m | 2,0x | 364,45854 | 364,45854 | 347,94701 | 184,05156 | 410,69083 | €544,42 | €1.088,84 | €49,33 | €0,00 |
| Forza relativa 1H V1 | NIGHT | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,02031 | 0,02031 | 0,02210 | 0,03036 | 0,01637 | €285,91 | €571,83 | €50,45 | €-0,00 |
| Forza relativa 1H V1 | ONDO | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,42171 | €891,90 | €1.783,80 | €49,29 | €0,00 |
| Forza relativa 1H V1 | WLD | SHORT | Forza relativa vs BTC V1 | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,32287 | €14,97 | €29,93 | €0,82 | €-0,00 |
| Forza relativa 1H V1 | AKE | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,00327 | 0,00326 | 0,00287 | 0,00165 | 0,00413 | €208,36 | €416,72 | €50,01 | €-0,41 |
| Forza relativa 1H V1 | ESPORTS | LONG | Forza relativa vs BTC V1 | 60m | 2,0x | 0,05542 | 0,05542 | 0,04877 | 0,02799 | 0,07005 | €190,21 | €380,42 | €45,65 | €0,00 |
| Forza relativa 1H V2 | AKE | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,00320 | 0,00326 | 0,00282 | 0,00162 | 0,00405 | €216,28 | €432,55 | €51,91 | €7,89 |
| Forza relativa 1H V2 | WLD | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,32287 | €47,70 | €95,39 | €2,60 | €-0,00 |
| Forza relativa 1H V2 | XMR | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 367,08012 | 367,08012 | 360,46822 | 185,37546 | 381,62629 | €1.446,12 | €2.892,24 | €52,10 | €0,00 |
| Forza relativa 1H V2 | ESPORTS | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,05542 | 0,05542 | 0,04877 | 0,02799 | 0,07005 | €212,29 | €424,59 | €50,95 | €0,00 |
| Forza relativa 1H V2 | BANK | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,36855 | 0,35795 | 0,33045 | 0,18612 | 0,45238 | €219,06 | €438,12 | €45,30 | €-12,61 |
| Scalp RSI Short 85 · €10 · 15x | PEPE | SHORT | Inversione RSI estrema 15m | 15m | 15,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €10,00 | €150,00 | €0,00 | €0,33 |
| Scalp RSI Short 80 · €10 · 15x | PEPE | SHORT | Inversione RSI estrema 15m | 15m | 15,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €10,00 | €150,00 | €0,00 | €0,33 |
| Scalp RSI Short 75 · €10 · 15x | PEPE | SHORT | Inversione RSI estrema 15m | 15m | 15,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €10,00 | €150,00 | €2,20 | €-1,16 |
| Scalp RSI Short 85 · €50 · 15x | PEPE | SHORT | Inversione RSI estrema 15m | 15m | 15,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €50,00 | €750,00 | €0,00 | €1,67 |
| Scalp RSI Short 80 · €50 · 15x | PEPE | SHORT | Inversione RSI estrema 15m | 15m | 15,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €50,00 | €750,00 | €0,00 | €1,67 |
| Scalp RSI Short 75 · €50 · 15x | PEPE | SHORT | Inversione RSI estrema 15m | 15m | 15,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €50,00 | €750,00 | €11,00 | €-5,80 |
| Scalp RSI Short 85 · prudente · 5x | PEPE | SHORT | Inversione RSI estrema 15m | 15m | 5,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €176,32 | €881,59 | €0,00 | €1,97 |
| Scalp RSI Short 80 · prudente · 5x | PEPE | SHORT | Inversione RSI estrema 15m | 15m | 5,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €176,37 | €881,84 | €0,00 | €1,97 |
| Scalp RSI Short 75 · prudente · 5x | PEPE | SHORT | Inversione RSI estrema 15m | 15m | 5,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €135,73 | €678,63 | €9,96 | €-5,25 |
| Benchmark Donchian breakout 1H | SUI | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,76606 | 0,76606 | 0,75182 | 0,38686 | 0,80165 | €1.377,00 | €2.754,00 | €51,18 | €0,00 |
| Benchmark Donchian breakout 1H | ALLO | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,35678 | 0,33757 | 0,39959 | 0,53338 | 0,24974 | €215,19 | €430,38 | €51,65 | €23,17 |
| Benchmark Donchian breakout 1H | PEPE | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.186,91 | €2.373,82 | €52,29 | €49,42 |
| Benchmark Donchian breakout 1H | SHIB | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €505,25 | €1.010,51 | €52,70 | €29,50 |
| Benchmark Bollinger mean reversion 1H | BTC | LONG | Bollinger mean reversion | 60m | 2,0x | 64125,06245 | 64469,02000 | 63355,56170 | 32383,15654 | 65279,31357 | €2.018,75 | €4.037,51 | €48,45 | €21,66 |
| Benchmark Bollinger mean reversion 1H | EUL | SHORT | Bollinger mean reversion | 60m | 2,0x | 2,14127 | 2,42460 | 2,39822 | 3,20120 | 1,75584 | €208,06 | €416,12 | €49,93 | €-55,06 |
| Benchmark Bollinger mean reversion 1H | PEPE | SHORT | Bollinger mean reversion | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.392,21 | €2.784,42 | €49,71 | €6,21 |
| Benchmark trend following EMA 1H | LAB | LONG | Trend following EMA | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €207,05 | €414,10 | €49,69 | €0,00 |
| Benchmark trend following EMA 1H | ALLO | SHORT | Trend following EMA | 60m | 2,0x | 0,35372 | 0,33757 | 0,39616 | 0,52881 | 0,26034 | €209,15 | €418,30 | €50,20 | €19,10 |
| Benchmark trend following EMA 1H | XMR | LONG | Trend following EMA | 60m | 2,0x | 367,08012 | 367,08012 | 359,73357 | 185,37546 | 383,24253 | €17,91 | €35,83 | €0,72 | €0,00 |
| Benchmark trend following EMA 1H | BANK | LONG | Trend following EMA | 60m | 2,0x | 0,34640 | 0,35795 | 0,34640 | 0,17493 | 0,43785 | €203,62 | €407,24 | €0,00 | €13,58 |
| Benchmark trend following EMA 1H | SHIB | LONG | Trend following EMA | 60m | 2,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €479,93 | €959,86 | €50,06 | €28,02 |
| Benchmark trend following EMA 1H | PEPE | LONG | Trend following EMA | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €14,55 | €29,10 | €0,69 | €-0,02 |
| Scanner Top 5 Long 1H | ONDO | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,40114 | 0,40114 | 0,38834 | 0,20258 | 0,42673 | €828,91 | €1.657,82 | €52,88 | €0,00 |
| Scanner Top 5 Long 1H | LAB | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €219,03 | €438,05 | €52,57 | €0,00 |
| Scanner Top 5 Long 1H | AKE | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,00319 | 0,00326 | 0,00281 | 0,00161 | 0,00396 | €224,41 | €448,82 | €53,86 | €10,17 |
| Scanner Top 5 Long 1H | XMR | LONG | Scanner Top 5 Long | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10712 | €70,71 | €141,42 | €2,58 | €0,00 |
| Scanner Top 5 Long 1H | ESPORTS | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,05372 | 0,05372 | 0,04728 | 0,02713 | 0,06662 | €225,93 | €451,85 | €54,22 | €0,00 |
| Scanner Top 5 Long 1H | PEPE | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €27,40 | €54,80 | €0,00 | €1,14 |
| Scanner Bottom 5 Short 1H | ADA | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,16703 | 0,16703 | 0,16365 | 0,24971 | 0,16112 | €1.381,07 | €2.762,13 | €0,00 | €-0,00 |
| Scanner Bottom 5 Short 1H | ALLO | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,36179 | 0,33757 | 0,40521 | 0,54088 | 0,27496 | €202,53 | €405,06 | €48,61 | €27,12 |
| Scanner Top10 Long | AKE | LONG | Scanner Top10 Long | 60m | 2,0x | 0,00319 | 0,00326 | 0,00281 | 0,00161 | 0,00396 | €208,33 | €416,67 | €50,00 | €9,44 |
| Scanner Top10 Long | XMR | LONG | Scanner Top10 Long | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10712 | €1.371,36 | €2.742,71 | €50,02 | €0,00 |
| Scanner Top10 Long | ESPORTS | LONG | Scanner Top10 Long | 60m | 2,0x | 0,05372 | 0,05372 | 0,04728 | 0,02713 | 0,06662 | €210,48 | €420,96 | €50,52 | €0,00 |
| Scanner Top10 Long | BANK | LONG | Scanner Top10 Long | 60m | 2,0x | 0,34640 | 0,35795 | 0,34831 | 0,17493 | 0,42954 | €210,73 | €421,45 | €0,00 | €14,05 |
| Scanner Top10 Long | SHIB | LONG | Scanner Top10 Long | 60m | 2,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €25,83 | €51,66 | €2,43 | €1,51 |
| Scanner Bottom10 Short | ADA | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,16193 | 0,16193 | 0,16426 | 0,24209 | 0,15727 | €1.731,26 | €3.462,51 | €49,86 | €-0,00 |
| Scanner Bottom10 Short | ALLO | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,38133 | 0,33757 | 0,35342 | 0,57009 | 0,30594 | €246,17 | €492,34 | €0,00 | €56,50 |
| Scanner Top15 Long | AKE | LONG | Scanner Top15 Long | 60m | 2,0x | 0,00319 | 0,00326 | 0,00281 | 0,00161 | 0,00396 | €208,33 | €416,67 | €50,00 | €9,44 |
| Scanner Top15 Long | XMR | LONG | Scanner Top15 Long | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10712 | €1.371,36 | €2.742,71 | €50,02 | €0,00 |
| Scanner Top15 Long | ESPORTS | LONG | Scanner Top15 Long | 60m | 2,0x | 0,05372 | 0,05372 | 0,04728 | 0,02713 | 0,06662 | €210,48 | €420,96 | €50,52 | €0,00 |
| Scanner Top15 Long | BANK | LONG | Scanner Top15 Long | 60m | 2,0x | 0,34640 | 0,35795 | 0,34831 | 0,17493 | 0,42954 | €210,73 | €421,45 | €0,00 | €14,05 |
| Scanner Top15 Long | SHIB | LONG | Scanner Top15 Long | 60m | 2,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €25,83 | €51,66 | €2,43 | €1,51 |
| Scanner Bottom15 Short | ADA | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,16193 | 0,16193 | 0,16426 | 0,24209 | 0,15727 | €1.731,26 | €3.462,51 | €49,86 | €-0,00 |
| Scanner Bottom15 Short | ALLO | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,38133 | 0,33757 | 0,35342 | 0,57009 | 0,30594 | €246,17 | €492,34 | €0,00 | €56,50 |
| Scanner Top20 Long | AKE | LONG | Scanner Top20 Long | 60m | 2,0x | 0,00319 | 0,00326 | 0,00281 | 0,00161 | 0,00396 | €208,33 | €416,67 | €50,00 | €9,44 |
| Scanner Top20 Long | XMR | LONG | Scanner Top20 Long | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10712 | €1.371,36 | €2.742,71 | €50,02 | €0,00 |
| Scanner Top20 Long | ESPORTS | LONG | Scanner Top20 Long | 60m | 2,0x | 0,05372 | 0,05372 | 0,04728 | 0,02713 | 0,06662 | €210,48 | €420,96 | €50,52 | €0,00 |
| Scanner Top20 Long | BANK | LONG | Scanner Top20 Long | 60m | 2,0x | 0,34640 | 0,35795 | 0,34831 | 0,17493 | 0,42954 | €210,73 | €421,45 | €0,00 | €14,05 |
| Scanner Top20 Long | SHIB | LONG | Scanner Top20 Long | 60m | 2,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €25,83 | €51,66 | €2,43 | €1,51 |
| Scanner Bottom20 Short | ADA | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,16193 | 0,16193 | 0,16426 | 0,24209 | 0,15727 | €1.731,26 | €3.462,51 | €49,86 | €-0,00 |
| Scanner Bottom20 Short | ALLO | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,38133 | 0,33757 | 0,35342 | 0,57009 | 0,30594 | €246,17 | €492,34 | €0,00 | €56,50 |
| Scanner Top 5 + forza BTC 1H | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39694 | 0,39694 | 0,38539 | 0,20045 | 0,42235 | €898,57 | €1.797,15 | €52,29 | €0,00 |
| Scanner Top 5 + forza BTC 1H | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €216,56 | €433,12 | €51,97 | €0,00 |
| Scanner Top 5 + forza BTC 1H | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00319 | 0,00326 | 0,00281 | 0,00161 | 0,00403 | €219,41 | €438,82 | €52,66 | €9,95 |
| Scanner Top 5 + forza BTC 1H | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 381,44484 | €37,16 | €74,32 | €1,36 | €0,00 |
| Scanner Top 5 + forza BTC 1H | ESPORTS | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,05372 | 0,05372 | 0,04728 | 0,02713 | 0,06790 | €221,11 | €442,22 | €53,07 | €0,00 |
| Scanner Top 5 + forza BTC 1H | SHIB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €12,99 | €25,97 | €1,21 | €1,02 |
| Scanner Top5 Btc Mfe V1 | SUI | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,76776 | 0,76776 | 0,75508 | 0,38772 | 0,79565 | €1.514,04 | €3.028,08 | €50,00 | €0,00 |
| Scanner Top5 Btc Mfe V1 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39924 | 0,39924 | 0,38729 | 0,20162 | 0,42552 | €835,46 | €1.670,91 | €50,00 | €0,00 |
| Scanner Top5 Btc Mfe V1 | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 367,08012 | 367,08012 | 360,46822 | 185,37546 | 381,62629 | €1.363,71 | €2.727,43 | €49,13 | €0,00 |
| Scanner Top5 Btc Mfe V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00322 | 0,00326 | 0,00284 | 0,00163 | 0,00407 | €196,51 | €393,01 | €47,16 | €4,94 |
| Scanner Top5 Btc Guard V1 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39724 | 0,39724 | 0,38434 | 0,20061 | 0,42561 | €756,62 | €1.513,24 | €49,13 | €0,00 |
| Scanner Top5 Btc Guard V1 | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €202,47 | €404,95 | €48,59 | €0,00 |
| Scanner Top5 Btc Guard V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00319 | 0,00326 | 0,00281 | 0,00161 | 0,00403 | €207,86 | €415,72 | €49,89 | €9,42 |
| Scanner Top5 Btc Guard V1 | ESPORTS | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,05372 | 0,05372 | 0,04728 | 0,02713 | 0,06790 | €209,47 | €418,95 | €50,27 | €0,00 |
| Scanner Top5 Btc Guard V1 | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,34640 | 0,35795 | 0,34831 | 0,17493 | 0,43785 | €14,38 | €28,76 | €0,00 | €0,96 |
| Scanner Top5 Btc Btc Le3 V1 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39974 | 0,39974 | 0,38840 | 0,20187 | 0,42468 | €884,65 | €1.769,29 | €50,18 | €0,00 |
| Scanner Top5 Btc Btc Le3 V1 | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €207,87 | €415,74 | €49,89 | €0,00 |
| Scanner Top5 Btc Btc Le3 V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00319 | 0,00326 | 0,00281 | 0,00161 | 0,00403 | €210,72 | €421,44 | €50,57 | €9,55 |
| Scanner Top5 Btc Btc Le3 V1 | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 381,44484 | €37,63 | €75,26 | €1,37 | €0,00 |
| Scanner Top5 Btc Btc Le3 V1 | ESPORTS | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,05372 | 0,05372 | 0,04728 | 0,02713 | 0,06790 | €212,36 | €424,71 | €50,97 | €0,00 |
| Scanner Top5 Btc Btc Le3 V1 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €29,40 | €58,80 | €0,00 | €1,22 |
| Scanner Top5 Btc Btc 2 3 V1 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39974 | 0,39974 | 0,38840 | 0,20187 | 0,42468 | €884,65 | €1.769,29 | €50,18 | €0,00 |
| Scanner Top5 Btc Btc 2 3 V1 | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €207,87 | €415,74 | €49,89 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39724 | 0,39724 | 0,38434 | 0,20061 | 0,42561 | €756,62 | €1.513,24 | €49,13 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00322 | 0,00326 | 0,00284 | 0,00163 | 0,00407 | €201,88 | €403,77 | €48,45 | €5,02 |
| Scanner Top5 Btc Guard Mfe V1 | ESPORTS | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,05372 | 0,05372 | 0,04728 | 0,02713 | 0,06790 | €203,57 | €407,14 | €48,86 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | SHIB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €15,53 | €31,06 | €1,46 | €0,91 |
| Scanner Top5 Btc Guard Mfe V1 | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,35802 | 0,35795 | 0,31588 | 0,18080 | 0,45073 | €205,20 | €410,40 | €48,30 | €-0,08 |
| Scanner Top5 Btc Guard Btc Le3 V1 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39974 | 0,39974 | 0,38840 | 0,20187 | 0,42468 | €871,05 | €1.742,11 | €49,41 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €205,84 | €411,68 | €49,40 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00319 | 0,00326 | 0,00281 | 0,00161 | 0,00403 | €211,32 | €422,63 | €50,72 | €9,58 |
| Scanner Top5 Btc Guard Btc Le3 V1 | ESPORTS | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,05372 | 0,05372 | 0,04728 | 0,02713 | 0,06790 | €212,96 | €425,92 | €51,11 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,34640 | 0,35795 | 0,34831 | 0,17493 | 0,43785 | €16,85 | €33,69 | €0,00 | €1,12 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39974 | 0,39974 | 0,38840 | 0,20187 | 0,42468 | €871,05 | €1.742,11 | €49,41 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00322 | 0,00326 | 0,00284 | 0,00163 | 0,00407 | €204,20 | €408,41 | €49,01 | €5,08 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | ESPORTS | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,05372 | 0,05372 | 0,04728 | 0,02713 | 0,06790 | €205,91 | €411,82 | €49,42 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | SHIB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €18,71 | €37,43 | €1,76 | €1,09 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | BANK | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,35802 | 0,35795 | 0,31588 | 0,18080 | 0,45073 | €207,57 | €415,15 | €48,86 | €-0,08 |
| Scanner Top5 Btc Runner25 V1 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39694 | 0,39694 | 0,38539 | 0,20045 | 0,43159 | €861,83 | €1.723,66 | €50,15 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,21338 | €207,96 | €415,92 | €49,91 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00319 | 0,00326 | 0,00281 | 0,00161 | 0,00434 | €213,22 | €426,44 | €51,17 | €9,67 |
| Scanner Top5 Btc Runner25 V1 | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 386,79573 | €70,70 | €141,40 | €2,58 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | ESPORTS | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,05372 | 0,05372 | 0,04728 | 0,02713 | 0,07306 | €215,09 | €430,17 | €51,62 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | SHIB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €14,24 | €28,48 | €1,33 | €1,12 |
| Scanner Top5 Btc Tp3 V1 | ONDO | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,39694 | 0,39694 | 0,38539 | 0,20045 | 0,43159 | €861,83 | €1.723,66 | €50,15 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | LAB | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,21338 | €207,96 | €415,92 | €49,91 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | AKE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00319 | 0,00326 | 0,00281 | 0,00161 | 0,00434 | €213,56 | €427,11 | €51,25 | €9,68 |
| Scanner Top5 Btc Tp3 V1 | XMR | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 386,79573 | €85,15 | €170,29 | €3,11 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | ESPORTS | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,05372 | 0,05372 | 0,04728 | 0,02713 | 0,07306 | €214,51 | €429,03 | €51,48 | €0,00 |
| Combo Trend | AKE | LONG | Combo Trend | 60m | 2,0x | 0,00329 | 0,00326 | 0,00290 | 0,00166 | 0,00416 | €208,78 | €417,57 | €50,11 | €-4,04 |
| Combo Trend | ALLO | SHORT | Combo Trend | 60m | 2,0x | 0,35372 | 0,33757 | 0,39616 | 0,52881 | 0,26034 | €209,35 | €418,70 | €50,24 | €19,11 |
| Combo Trend | ESPORTS | LONG | Combo Trend | 60m | 2,0x | 0,05542 | 0,05542 | 0,04877 | 0,02799 | 0,07005 | €192,99 | €385,98 | €46,32 | €0,00 |
| Combo Trend | BANK | LONG | Combo Trend | 60m | 2,0x | 0,34640 | 0,35795 | 0,34640 | 0,17493 | 0,43785 | €203,87 | €407,73 | €0,00 | €13,60 |
| Combo Trend | SHIB | LONG | Combo Trend | 60m | 2,0x | 0,00001 | 0,00001 | 0,00000 | 0,00000 | 0,00001 | €13,64 | €27,28 | €1,40 | €1,61 |
| Combo Mean Reversion | BTC | LONG | Combo Mean Reversion | 60m | 2,0x | 63775,69259 | 64469,02000 | 64181,91722 | 32206,72476 | 65000,18589 | €1.998,65 | €3.997,31 | €0,00 | €43,46 |
| Combo Mean Reversion | AKE | SHORT | Combo Mean Reversion | 60m | 2,0x | 0,00320 | 0,00326 | 0,00356 | 0,00479 | 0,00263 | €225,46 | €450,91 | €50,00 | €-8,41 |
| Combo Scanner | ONDO | LONG | Combo Scanner | 60m | 2,0x | 0,39694 | 0,39694 | 0,38539 | 0,20045 | 0,42235 | €857,88 | €1.715,77 | €49,92 | €0,00 |
| Combo Scanner | LAB | LONG | Combo Scanner | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19831 | €207,54 | €415,08 | €49,81 | €0,00 |
| Combo Scanner | AKE | LONG | Combo Scanner | 60m | 2,0x | 0,00319 | 0,00326 | 0,00281 | 0,00161 | 0,00403 | €210,36 | €420,73 | €50,49 | €9,54 |
| Combo Scanner | XMR | LONG | Combo Scanner | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 381,44484 | €23,89 | €47,78 | €0,87 | €0,00 |
| Combo Scanner | ESPORTS | LONG | Combo Scanner | 60m | 2,0x | 0,05372 | 0,05372 | 0,04728 | 0,02713 | 0,06790 | €212,08 | €424,16 | €50,90 | €0,00 |
| Combo Scanner | PEPE | LONG | Combo Scanner | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €13,91 | €27,83 | €0,00 | €0,58 |
| Combo Scanner | SHIB | LONG | Combo Scanner | 60m | 2,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €16,61 | €33,22 | €1,56 | €0,97 |
| Combo Adaptive | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,40114 | 0,40114 | 0,38834 | 0,20258 | 0,42673 | €809,25 | €1.618,50 | €51,63 | €0,00 |
| Combo Adaptive | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15861 | 0,13958 | 0,08010 | 0,19668 | €213,13 | €426,26 | €51,15 | €0,00 |
| Combo Adaptive | WLD | SHORT | Combo Adaptive | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,32475 | €929,60 | €1.859,20 | €50,73 | €-0,00 |
| Combo Adaptive | ALLO | SHORT | Combo Adaptive | 60m | 2,0x | 0,36179 | 0,33757 | 0,40521 | 0,54088 | 0,27496 | €210,64 | €421,27 | €50,55 | €28,20 |
| Combo Adaptive | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €12,76 | €25,52 | €0,55 | €-0,01 |
| Combo Adaptive Mfe Trail | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39784 | 0,39784 | 0,38492 | 0,20091 | 0,42367 | €744,71 | €1.489,41 | €48,35 | €0,00 |
| Combo Adaptive Mfe Trail | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15861 | 0,13958 | 0,08010 | 0,19668 | €201,70 | €403,39 | €48,41 | €0,00 |
| Combo Adaptive Mfe Trail | WLD | SHORT | Combo Adaptive | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,32475 | €883,78 | €1.767,56 | €48,23 | €-0,00 |
| Combo Adaptive Mfe Trail | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,00330 | 0,00326 | 0,00293 | 0,00166 | 0,00403 | €203,95 | €407,90 | €45,45 | €-4,05 |
| Combo Adaptive Quality7 V1 | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,40304 | 0,40304 | 0,39140 | 0,20354 | 0,42632 | €859,15 | €1.718,30 | €49,62 | €0,00 |
| Combo Adaptive Quality7 V1 | WLD | SHORT | Combo Adaptive | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,32475 | €919,99 | €1.839,97 | €50,21 | €-0,00 |
| Combo Adaptive Quality7 V1 | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,00327 | 0,00326 | 0,00287 | 0,00165 | 0,00405 | €209,81 | €419,62 | €50,35 | €-0,42 |
| Combo Adaptive Quality7 V1 | ALLO | SHORT | Combo Adaptive | 60m | 2,0x | 0,36179 | 0,33757 | 0,40521 | 0,54088 | 0,27496 | €207,61 | €415,23 | €49,83 | €27,80 |
| Combo Adaptive Quality7 V1 | SHIB | LONG | Combo Adaptive | 60m | 2,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €21,30 | €42,60 | €0,00 | €2,52 |
| Combo Adaptive Regime V1 | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39724 | 0,39724 | 0,38434 | 0,20061 | 0,42303 | €757,94 | €1.515,88 | €49,21 | €0,00 |
| Combo Adaptive Regime V1 | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15861 | 0,13958 | 0,08010 | 0,19668 | €206,52 | €413,04 | €49,56 | €0,00 |
| Combo Adaptive Quality7 Regime V1 | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,40554 | 0,40554 | 0,39390 | 0,20480 | 0,42882 | €864,27 | €1.728,54 | €49,61 | €0,00 |
| Combo Adaptive Long Only V1 | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,41951 | €893,67 | €1.787,34 | €49,39 | €0,00 |
| Combo Adaptive Long Only V1 | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €205,55 | €411,10 | €49,33 | €0,00 |
| Combo Adaptive Long Only V1 | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,00319 | 0,00326 | 0,00281 | 0,00161 | 0,00396 | €205,22 | €410,44 | €49,25 | €9,30 |
| Combo Adaptive Long Only V1 | XMR | LONG | Combo Adaptive | 60m | 2,0x | 367,08012 | 367,08012 | 360,46822 | 185,37546 | 380,30391 | €1.384,19 | €2.768,37 | €49,86 | €0,00 |
| Combo Adaptive Long Only V1 | SHIB | LONG | Combo Adaptive | 60m | 2,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €19,61 | €39,22 | €1,83 | €1,54 |
| Combo Adaptive Partial 1R V1 | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,41951 | €893,02 | €1.786,04 | €49,36 | €0,00 |
| Combo Adaptive Partial 1R V1 | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €205,22 | €410,44 | €49,25 | €0,00 |
| Combo Adaptive Partial 1R V1 | WLD | SHORT | Combo Adaptive | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,32475 | €895,30 | €1.790,60 | €48,86 | €-0,00 |
| Combo Adaptive Partial 1R V1 | ESPORTS | LONG | Combo Adaptive | 60m | 2,0x | 0,05372 | 0,05372 | 0,04728 | 0,02713 | 0,06662 | €105,94 | €211,87 | €25,42 | €0,00 |
| Combo Adaptive Partial 1R V1 | ALLO | SHORT | Combo Adaptive | 60m | 2,0x | 0,36179 | 0,33757 | 0,40521 | 0,54088 | 0,27496 | €98,69 | €197,38 | €23,69 | €13,21 |
| Combo Adaptive Quality7 Regime Partial 1R V1 | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,40554 | 0,40554 | 0,39390 | 0,20480 | 0,42882 | €864,27 | €1.728,54 | €49,61 | €0,00 |
| Combo Adaptive Runner25 V1 | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,43050 | €902,18 | €1.804,37 | €49,86 | €0,00 |
| Combo Adaptive Runner25 V1 | WLD | SHORT | Combo Adaptive | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,31537 | €919,67 | €1.839,35 | €50,19 | €-0,00 |
| Combo Adaptive Runner25 V1 | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,00327 | 0,00326 | 0,00287 | 0,00165 | 0,00444 | €209,99 | €419,98 | €50,40 | €-0,42 |
| Combo Adaptive Runner25 V1 | XMR | LONG | Combo Adaptive | 60m | 2,0x | 367,08012 | 367,08012 | 360,46822 | 185,37546 | 386,91580 | €27,35 | €54,70 | €0,99 | €0,00 |
| Combo Adaptive Runner25 V1 | ALLO | SHORT | Combo Adaptive | 60m | 2,0x | 0,36179 | 0,33757 | 0,40521 | 0,54088 | 0,23155 | €207,78 | €415,57 | €49,87 | €27,82 |
| Combo Adaptive Runner25 V1 | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €19,57 | €39,13 | €0,00 | €0,81 |
| Combo Adaptive Tp3 V1 | ONDO | LONG | Combo Adaptive | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,43050 | €902,18 | €1.804,37 | €49,86 | €0,00 |
| Combo Adaptive Tp3 V1 | LAB | LONG | Combo Adaptive | 60m | 2,0x | 0,15861 | 0,15861 | 0,13958 | 0,08010 | 0,21571 | €207,43 | €414,86 | €49,78 | €0,00 |
| Combo Adaptive Tp3 V1 | WLD | SHORT | Combo Adaptive | 60m | 2,0x | 0,34349 | 0,34349 | 0,35287 | 0,51352 | 0,31537 | €911,80 | €1.823,59 | €49,76 | €-0,00 |
| Combo Adaptive Tp3 V1 | ALLO | SHORT | Combo Adaptive | 60m | 2,0x | 0,36179 | 0,33757 | 0,40521 | 0,54088 | 0,23155 | €205,00 | €410,00 | €49,20 | €27,45 |
| Btc Ema 1H | BTC | SHORT | Trend following EMA | 60m | 3,0x | 64120,47334 | 64469,02000 | 65043,80816 | 85173,36209 | 62273,80371 | €1.153,43 | €3.460,30 | €49,83 | €-18,81 |
| Btc Bollinger 1H | BTC | LONG | Bollinger mean reversion | 60m | 3,0x | 64125,06245 | 64469,02000 | 63355,56170 | 43070,66694 | 65279,31357 | €1.402,77 | €4.208,32 | €50,50 | €22,57 |
| Sol Ema 4H | SOL | SHORT | Trend following EMA | 240m | 2,0x | 75,05699 | 75,05500 | 77,22103 | 112,21019 | 69,64688 | €862,58 | €1.725,17 | €49,74 | €0,05 |
| Sol Donchian 4H | SOL | SHORT | Donchian breakout 20 barre | 240m | 2,0x | 75,96380 | 75,05500 | 78,23939 | 113,56589 | 69,59218 | €830,21 | €1.660,43 | €49,74 | €19,86 |
| Sol Adaptive 4H | SOL | SHORT | Combo Adaptive | 240m | 2,0x | 75,96380 | 75,05500 | 78,44626 | 113,56589 | 69,75767 | €761,04 | €1.522,08 | €49,74 | €18,21 |
| Eth Ema 1H | ETH | SHORT | Trend following EMA | 60m | 3,0x | 1873,22528 | 1885,44000 | 1900,19972 | 2488,26758 | 1819,27639 | €1.138,34 | €3.415,02 | €49,18 | €-22,27 |
| Eth Adaptive 1H | ETH | SHORT | Combo Adaptive | 60m | 3,0x | 1873,22528 | 1885,44000 | 1900,19972 | 2488,26758 | 1819,27639 | €1.146,74 | €3.440,21 | €49,54 | €-22,43 |
| Master Adaptive V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39854 | 0,39854 | 0,38677 | 0,20126 | 0,42207 | €833,00 | €1.665,99 | €49,19 | €0,00 |
| Master Adaptive V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €203,80 | €407,60 | €48,91 | €0,00 |
| Master Adaptive V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00319 | 0,00326 | 0,00281 | 0,00161 | 0,00396 | €205,42 | €410,83 | €49,30 | €9,31 |
| Master Adaptive V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10713 | €21,54 | €43,08 | €0,79 | €0,00 |
| Master Adaptive V1 | ESPORTS | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,05372 | 0,05372 | 0,04728 | 0,02713 | 0,06662 | €206,81 | €413,61 | €49,63 | €0,00 |
| Master Adaptive No Alt V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39854 | 0,39854 | 0,38677 | 0,20126 | 0,42207 | €833,00 | €1.665,99 | €49,19 | €0,00 |
| Master Adaptive No Alt V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €203,80 | €407,60 | €48,91 | €0,00 |
| Master Adaptive No Alt V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00319 | 0,00326 | 0,00281 | 0,00161 | 0,00396 | €205,42 | €410,83 | €49,30 | €9,31 |
| Master Adaptive No Alt V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10713 | €21,54 | €43,08 | €0,79 | €0,00 |
| Master Adaptive No Alt V1 | ESPORTS | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,05372 | 0,05372 | 0,04728 | 0,02713 | 0,06662 | €206,81 | €413,61 | €49,63 | €0,00 |
| Master Adaptive Strict3 V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39754 | 0,39754 | 0,38655 | 0,20076 | 0,41951 | €887,07 | €1.774,14 | €49,03 | €0,00 |
| Master Adaptive Strict3 V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00320 | 0,00326 | 0,00282 | 0,00162 | 0,00397 | €201,87 | €403,75 | €48,45 | €7,96 |
| Master Adaptive Strict3 V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10713 | €1.330,61 | €2.661,21 | €48,54 | €0,00 |
| Master Adaptive Strict3 V1 | ESPORTS | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,05372 | 0,05372 | 0,04728 | 0,02713 | 0,06662 | €203,29 | €406,58 | €48,79 | €0,00 |
| Master Adaptive Expanded V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39854 | 0,39854 | 0,38677 | 0,20126 | 0,42207 | €833,00 | €1.665,99 | €49,19 | €0,00 |
| Master Adaptive Expanded V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,19455 | €203,80 | €407,60 | €48,91 | €0,00 |
| Master Adaptive Expanded V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00319 | 0,00326 | 0,00281 | 0,00161 | 0,00396 | €206,32 | €412,65 | €49,52 | €9,35 |
| Master Adaptive Expanded V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10713 | €33,54 | €67,08 | €1,22 | €0,00 |
| Master Adaptive Expanded V1 | ESPORTS | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,05372 | 0,05372 | 0,04728 | 0,02713 | 0,06662 | €207,74 | €415,48 | €49,86 | €0,00 |
| Master Adaptive Gb20 V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,40304 | 0,40304 | 0,39140 | 0,20354 | 0,42632 | €848,64 | €1.697,27 | €49,02 | €0,00 |
| Master Adaptive Gb20 V1 | RIF | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,10582 | 0,10582 | 0,09312 | 0,05344 | 0,13122 | €201,89 | €403,77 | €48,45 | €0,00 |
| Master Adaptive Gb20 V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 367,08012 | 367,08012 | 360,46822 | 185,37546 | 380,30391 | €1.348,01 | €2.696,02 | €48,56 | €0,00 |
| Master Adaptive Gb20 V1 | EUL | LONG | Master Adaptive Consensus | 60m | 2,0x | 2,22675 | 2,42460 | 1,95954 | 1,12451 | 2,76116 | €203,16 | €406,33 | €48,76 | €36,10 |
| Master Adaptive Runner25 V1 | ONDO | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,39854 | 0,39854 | 0,38677 | 0,20126 | 0,43384 | €833,00 | €1.665,99 | €49,19 | €0,00 |
| Master Adaptive Runner25 V1 | LAB | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,15689 | 0,15689 | 0,13807 | 0,07923 | 0,21338 | €203,80 | €407,60 | €48,91 | €0,00 |
| Master Adaptive Runner25 V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00319 | 0,00326 | 0,00281 | 0,00161 | 0,00434 | €205,36 | €410,73 | €49,29 | €9,31 |
| Master Adaptive Runner25 V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 386,79573 | €20,87 | €41,74 | €0,76 | €0,00 |
| Master Adaptive Runner25 V1 | ESPORTS | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,05372 | 0,05372 | 0,04728 | 0,02713 | 0,07306 | €207,01 | €414,02 | €49,68 | €0,00 |
| Master Adaptive Runner25 V1 | DOGE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,07164 | 0,07332 | 0,07061 | 0,03618 | 0,07474 | €15,53 | €31,06 | €0,45 | €0,73 |
| Combo Adaptive Side Regime Guard V1 | AKE | LONG | Combo Adaptive | 60m | 2,0x | 0,00320 | 0,00326 | 0,00282 | 0,00162 | 0,00397 | €212,78 | €425,56 | €51,07 | €7,76 |
| Combo Adaptive Side Regime Guard V1 | BANK | LONG | Combo Adaptive | 60m | 2,0x | 0,34640 | 0,35795 | 0,35111 | 0,17493 | 0,42954 | €212,51 | €425,01 | €0,00 | €14,17 |
| Combo Adaptive Side Regime Guard V1 | ALLO | SHORT | Combo Adaptive | 60m | 2,0x | 0,37453 | 0,33757 | 0,35402 | 0,55991 | 0,29289 | €232,55 | €465,11 | €0,00 | €45,89 |
| Combo Adaptive Side Regime Guard V1 | SHIB | LONG | Combo Adaptive | 60m | 2,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €548,64 | €1.097,29 | €51,50 | €32,03 |
| Combo Adaptive Side Regime Guard V1 | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €40,53 | €81,06 | €1,74 | €-0,04 |
| Master Adaptive Gb20 Be V1 | BEAT | LONG | Master Adaptive Consensus | 60m | 2,0x | 3,29017 | 3,29017 | 3,00714 | 1,66154 | 3,85623 | €291,32 | €582,63 | €50,12 | €0,00 |
| Master Adaptive Gb20 Be V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00322 | 0,00326 | 0,00322 | 0,00163 | 0,00400 | €210,71 | €421,43 | €0,00 | €5,30 |
| Master Adaptive Gb20 Be V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 367,86058 | 367,86058 | 361,23463 | 185,76959 | 381,11249 | €1.403,77 | €2.807,55 | €50,57 | €0,00 |
| Master Adaptive Gb20 Be V1 | ESPORTS | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,05372 | 0,05372 | 0,04728 | 0,02713 | 0,06662 | €210,71 | €421,42 | €50,57 | €0,00 |
| Master Adaptive Gb20 Partial V1 | BEAT | LONG | Master Adaptive Consensus | 60m | 2,0x | 3,29017 | 3,29017 | 3,00714 | 1,66154 | 3,85623 | €291,05 | €582,09 | €50,07 | €0,00 |
| Master Adaptive Gb20 Partial V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 360,04130 | 185,19860 | 380,10713 | €1.376,47 | €2.752,95 | €50,21 | €0,00 |
| Master Adaptive Gb20 Partial V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00322 | 0,00326 | 0,00284 | 0,00163 | 0,00400 | €209,67 | €419,35 | €50,32 | €5,27 |
| Master Adaptive Gb20 Partial V1 | ESPORTS | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,05372 | 0,05372 | 0,04728 | 0,02713 | 0,06662 | €209,56 | €419,13 | €50,30 | €0,00 |
| Master Adaptive Gb20 Loss Cap V1 | AKE | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,00275 | 0,00326 | 0,00242 | 0,00139 | 0,00362 | €208,32 | €416,65 | €50,00 | €78,50 |
| Master Adaptive Gb20 Loss Cap V1 | BEAT | LONG | Master Adaptive Consensus | 60m | 2,0x | 3,29017 | 3,29017 | 3,07790 | 1,66154 | 3,85623 | €388,25 | €776,50 | €50,10 | €0,00 |
| Master Adaptive Gb20 Loss Cap V1 | XMR | LONG | Master Adaptive Consensus | 60m | 2,0x | 366,72991 | 366,72991 | 361,71345 | 185,19860 | 380,10713 | €1.835,86 | €3.671,71 | €50,22 | €0,00 |
| Master Adaptive Gb20 Loss Cap V1 | ESPORTS | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,05372 | 0,05372 | 0,04728 | 0,02713 | 0,07091 | €210,77 | €421,54 | €50,58 | €0,00 |
| 1H Fast V3 Nohigh Range Only V1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00320 | 0,00326 | 0,00286 | 0,00215 | 0,00370 | €161,22 | €483,65 | €50,91 | €9,54 |
| 1H Fast V3 Nohigh Range Only V1 | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,34640 | 0,35795 | 0,35973 | 0,23266 | 0,39884 | €166,95 | €500,84 | €0,00 | €16,70 |
| 1H Fast V3 Nohigh Range Only V1 | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,33165 | 0,33757 | 0,36472 | 0,44055 | 0,28205 | €170,92 | €512,75 | €51,13 | €-9,15 |
| 1H Fast V3 Nohigh Range Only V1 | SHIB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €473,86 | €1.421,59 | €0,00 | €84,07 |
| 1H Fast V3 Nohigh Regime Guard V1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00320 | 0,00326 | 0,00286 | 0,00215 | 0,00370 | €161,22 | €483,65 | €50,91 | €9,54 |
| 1H Fast V3 Nohigh Regime Guard V1 | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,34640 | 0,35795 | 0,35973 | 0,23266 | 0,39884 | €168,19 | €504,57 | €0,00 | €16,82 |
| 1H Fast V3 Nohigh Regime Guard V1 | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,33165 | 0,33757 | 0,36472 | 0,44055 | 0,28205 | €172,19 | €516,57 | €51,51 | €-9,22 |
| 1H Fast V3 Nohigh Regime Guard V1 | SHIB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €477,39 | €1.432,18 | €0,00 | €84,70 |
| Main Side Regime Guard V1 | AKE | LONG | Confluenza trend | 240m | 3,0x | 0,00322 | 0,00326 | 0,00284 | 0,00216 | 0,00400 | €140,56 | €421,69 | €50,60 | €5,25 |
| Main Side Regime Guard V1 | SOL | SHORT | Confluenza trend | 240m | 3,0x | 73,82923 | 75,05500 | 75,57185 | 98,06983 | 70,34400 | €715,11 | €2.145,34 | €50,64 | €-35,62 |
| Main Side Regime Guard V1 | BANK | LONG | Confluenza trend | 240m | 3,0x | 0,34200 | 0,35795 | 0,34200 | 0,22971 | 0,42408 | €140,45 | €421,36 | €0,00 | €19,65 |
| Main Side Regime Guard V1 | ALLO | SHORT | Confluenza trend | 240m | 3,0x | 0,38070 | 0,33757 | 0,42639 | 0,50570 | 0,28933 | €140,03 | €420,08 | €50,41 | €47,59 |
| Main Dynamic Asset Selector V1 | AKE | LONG | Confluenza trend | 240m | 3,0x | 0,00322 | 0,00326 | 0,00284 | 0,00216 | 0,00400 | €140,56 | €421,69 | €50,60 | €5,25 |
| Main Dynamic Asset Selector V1 | SOL | SHORT | Confluenza trend | 240m | 3,0x | 73,82923 | 75,05500 | 75,57185 | 98,06983 | 70,34400 | €715,22 | €2.145,66 | €50,64 | €-35,62 |
| Main Dynamic Asset Selector V1 | BANK | LONG | Confluenza trend | 240m | 3,0x | 0,34200 | 0,35795 | 0,34200 | 0,22971 | 0,42408 | €141,21 | €423,62 | €0,00 | €19,76 |
| Combo Trend Side Regime Guard V1 | AKE | LONG | Combo Trend | 60m | 2,0x | 0,00320 | 0,00326 | 0,00282 | 0,00162 | 0,00405 | €211,52 | €423,03 | €50,76 | €7,71 |
| Combo Trend Side Regime Guard V1 | BANK | LONG | Combo Trend | 60m | 2,0x | 0,34640 | 0,35795 | 0,34640 | 0,17493 | 0,43785 | €211,00 | €422,00 | €0,00 | €14,07 |
| Combo Trend Side Regime Guard V1 | ALLO | SHORT | Combo Trend | 60m | 2,0x | 0,37453 | 0,33757 | 0,41947 | 0,55991 | 0,27565 | €207,96 | €415,93 | €49,91 | €41,04 |
| Combo Trend Side Regime Guard V1 | PEPE | LONG | Combo Trend | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.073,98 | €2.147,95 | €51,13 | €-1,17 |
| Combo Trend Side Regime Guard V1 | SHIB | LONG | Combo Trend | 60m | 2,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €16,58 | €33,16 | €1,73 | €0,75 |
| 1H Fast Nohigh Cap75 Short Only V1 | WLD | SHORT | Momentum / breakout | 60m | 3,0x | 0,34959 | 0,34959 | 0,35668 | 0,46437 | 0,33896 | €822,35 | €2.467,06 | €50,00 | €-0,00 |
| 1H Fast Nohigh Cap75 Short Only V1 | ALLO | SHORT | Momentum / breakout | 60m | 3,0x | 0,36948 | 0,33757 | 0,35350 | 0,49079 | 0,31961 | €185,68 | €557,05 | €0,00 | €48,11 |
| 1H Fast Nohigh Cap75 Short Only V1 | EUL | LONG | Momentum / breakout | 60m | 3,0x | 2,14213 | 2,42460 | 1,88507 | 1,43880 | 2,52771 | €140,03 | €420,08 | €50,41 | €55,39 |
| 1H Fast Nohigh Cap75 Short Only V1 | PEPE | LONG | Momentum / breakout | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €1.016,35 | €3.049,05 | €50,81 | €-8,02 |
| 1H Fast Nohigh Cap75 Short Only V1 | SHIB | LONG | Momentum / breakout | 60m | 3,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €22,79 | €68,36 | €2,54 | €-0,01 |
| 1H Balanced V3 Long Only V1 | XMR | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 366,72991 | 366,72991 | 360,04130 | 246,32025 | 380,10712 | €913,56 | €2.740,69 | €49,99 | €0,00 |
| 1H Balanced V3 Long Only V1 | AKE | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,00328 | 0,00326 | 0,00288 | 0,00220 | 0,00406 | €137,93 | €413,80 | €49,66 | €-1,69 |
| 1H Balanced V3 Long Only V1 | SHIB | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €347,90 | €1.043,70 | €49,90 | €-0,21 |
| Scanner Bottom5 Short Profit Lock V1 | WLD | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,34449 | 0,34449 | 0,35368 | 0,51502 | 0,32613 | €937,87 | €1.875,74 | €50,00 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | ALLO | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,38133 | 0,33757 | 0,35342 | 0,57009 | 0,30594 | €249,04 | €498,07 | €0,00 | €57,16 |
| Scanner Bottom5 Short Mfe Trail V1 | WLD | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,34449 | 0,34449 | 0,35368 | 0,51502 | 0,32613 | €937,87 | €1.875,74 | €50,00 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | ALLO | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,37547 | 0,33757 | 0,34560 | 0,56133 | 0,28964 | €216,32 | €432,65 | €0,00 | €43,68 |
| Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00323 | 0,00326 | 0,00290 | 0,00217 | 0,00390 | €162,23 | €486,68 | €50,00 | €4,66 |
| Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | EUL | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,22675 | 2,42460 | 1,95954 | 1,49563 | 2,76116 | €141,68 | €425,05 | €51,01 | €37,77 |
| Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | SHIB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €457,99 | €1.373,96 | €51,09 | €-0,27 |
| Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,34640 | 0,35795 | 0,35973 | 0,23266 | 0,41631 | €165,14 | €495,42 | €0,00 | €16,52 |
| Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | ESPORTS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,05591 | 0,05591 | 0,04920 | 0,03756 | 0,06933 | €138,87 | €416,62 | €49,99 | €0,00 |
| Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00320 | 0,00326 | 0,00287 | 0,00215 | 0,00386 | €162,16 | €486,47 | €49,98 | €9,68 |
| Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,38133 | 0,33757 | 0,34982 | 0,50654 | 0,32269 | €210,30 | €630,90 | €0,00 | €72,40 |
| Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | SHIB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €24,60 | €73,80 | €0,00 | €4,36 |
| Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00320 | 0,00326 | 0,00320 | 0,00215 | 0,00382 | €172,56 | €517,68 | €0,00 | €9,96 |
| Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,37922 | 0,33757 | 0,35093 | 0,50374 | 0,31790 | €205,84 | €617,51 | €0,00 | €67,83 |
| Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | SHIB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €469,10 | €1.407,30 | €0,00 | €83,23 |
| Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,34540 | 0,35795 | 0,35973 | 0,23199 | 0,41511 | €165,14 | €495,42 | €0,00 | €18,00 |
| Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00323 | 0,00326 | 0,00290 | 0,00217 | 0,00390 | €162,03 | €486,10 | €49,94 | €4,66 |
| Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,38133 | 0,33757 | 0,34982 | 0,50654 | 0,32269 | €213,90 | €641,71 | €0,00 | €73,65 |
| Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | SHIB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €467,39 | €1.402,16 | €0,00 | €63,56 |
| Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | EUL | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,22675 | 2,42460 | 1,95954 | 1,49563 | 2,76116 | €9,08 | €27,24 | €3,27 | €2,42 |
| Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00319 | 0,00326 | 0,00319 | 0,00215 | 0,00385 | €162,03 | €486,10 | €0,00 | €10,44 |
| Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,37547 | 0,33757 | 0,34560 | 0,49876 | 0,30872 | €185,38 | €556,13 | €0,00 | €56,14 |
| Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | SHIB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €471,54 | €1.414,62 | €0,00 | €64,13 |
| Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | EUL | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,22675 | 2,42460 | 1,95954 | 1,49563 | 2,76116 | €10,43 | €31,30 | €3,76 | €2,78 |
| Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,35802 | 0,35795 | 0,32525 | 0,24047 | 0,42357 | €185,12 | €555,36 | €50,84 | €-0,11 |
| Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,34640 | 0,35795 | 0,35973 | 0,23266 | 0,41631 | €165,15 | €495,45 | €0,00 | €16,52 |
| Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | ESPORTS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,05591 | 0,05591 | 0,04920 | 0,03756 | 0,06933 | €138,88 | €416,65 | €50,00 | €0,00 |
| Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00320 | 0,00326 | 0,00287 | 0,00215 | 0,00386 | €162,21 | €486,64 | €50,00 | €9,69 |
| Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | SHIB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €467,00 | €1.400,99 | €0,00 | €63,51 |
| Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,34432 | 0,35795 | 0,35973 | 0,23127 | 0,41381 | €165,15 | €495,45 | €0,00 | €19,61 |
| Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00319 | 0,00326 | 0,00287 | 0,00215 | 0,00385 | €162,18 | €486,55 | €49,99 | €10,45 |
| Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | SHIB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €474,66 | €1.423,99 | €0,00 | €64,55 |
| Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | EUL | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,22675 | 2,42460 | 1,95954 | 1,49563 | 2,76116 | €143,18 | €429,55 | €51,55 | €38,17 |
| Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | BANK | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,34640 | 0,35795 | 0,35973 | 0,23266 | 0,41631 | €165,14 | €495,42 | €0,00 | €16,52 |
| Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | ESPORTS | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,05591 | 0,05591 | 0,04920 | 0,03756 | 0,06933 | €138,87 | €416,62 | €49,99 | €0,00 |
| Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00320 | 0,00326 | 0,00287 | 0,00215 | 0,00386 | €162,16 | €486,47 | €49,98 | €9,68 |
| Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,38133 | 0,33757 | 0,34982 | 0,50654 | 0,32269 | €210,30 | €630,90 | €0,00 | €72,40 |
| Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | SHIB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €24,60 | €73,80 | €0,00 | €4,36 |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00320 | 0,00326 | 0,00287 | 0,00215 | 0,00386 | €162,23 | €486,68 | €50,00 | €9,69 |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,37360 | 0,33757 | 0,35320 | 0,49626 | 0,30717 | €186,92 | €560,77 | €0,00 | €54,07 |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | EUL | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,22675 | 2,42460 | 1,95954 | 1,49563 | 2,76116 | €142,49 | €427,47 | €51,30 | €37,98 |
| Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | SHIB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €460,60 | €1.381,80 | €51,38 | €-0,28 |
| Evo Cand 1H Fast V3 No Esports Stress G Tp R200 89Ab3F19 | SHIB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €463,42 | €1.390,27 | €0,00 | €82,22 |
| Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00320 | 0,00326 | 0,00289 | 0,00215 | 0,00382 | €172,57 | €517,70 | €50,00 | €9,96 |
| Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | EUL | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,22675 | 2,42460 | 1,95954 | 1,49563 | 2,76116 | €141,78 | €425,33 | €51,04 | €37,79 |
| Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | SHIB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €458,22 | €1.374,67 | €51,11 | €-0,27 |
| Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | AKE | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00320 | 0,00326 | 0,00320 | 0,00215 | 0,00382 | €172,56 | €517,68 | €0,00 | €9,96 |
| Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | ALLO | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,37453 | 0,33757 | 0,35204 | 0,49749 | 0,31103 | €196,07 | €588,21 | €0,00 | €58,04 |
| Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | SHIB | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00001 | 0,00001 | 0,00001 | 0,00000 | 0,00001 | €468,63 | €1.405,89 | €0,00 | €83,15 |
| Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | EUL | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 2,22675 | 2,42460 | 1,95954 | 1,49563 | 2,76116 | €9,57 | €28,71 | €3,44 | €2,55 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | BANK | LONG | 2026-07-26T05:08:37+00:00 | 0,35968 | €21,84 | 0,44 | STOP_STRESS_SLIPPAGE |
| Evo Cand 1H Fast V3 Nohigh Range Only V Tp R200 52488Eb5 | BANK | LONG | 2026-07-26T05:08:37+00:00 | 0,35968 | €21,84 | 0,44 | STOP_STRESS_SLIPPAGE |
| Sol Adaptive 1H | SOL | SHORT | 2026-07-26T04:53:36+00:00 | 75,16907 | €-54,17 | -1,10 | STOP |
| Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | BANK | LONG | 2026-07-26T04:53:36+00:00 | 0,37133 | €7,97 | 0,16 | STOP_STRESS_SLIPPAGE |
| Scanner Top5 Btc Guard Mfe V1 | BANK | LONG | 2026-07-26T04:38:36+00:00 | 0,37579 | €33,84 | 0,69 | STOP_STRESS_SLIPPAGE |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | BANK | LONG | 2026-07-26T04:38:36+00:00 | 0,37579 | €34,23 | 0,69 | STOP_STRESS_SLIPPAGE |
| 1H Fast V3 No Esports Mfe Lock V1 | BANK | LONG | 2026-07-26T04:38:36+00:00 | 0,37579 | €41,41 | 0,82 | STOP_STRESS_SLIPPAGE |
| Sol Bollinger 1H | SOL | LONG | 2026-07-26T04:23:37+00:00 | 75,09277 | €67,86 | 1,38 | TARGET |
| Combo Trend Side Regime Guard V1 | SHIB | LONG | 2026-07-26T04:23:37+00:00 | 0,00001 | €2,85 | 2,17 | TARGET |
| Benchmark Bollinger mean reversion 1H | SOL | LONG | 2026-07-26T04:23:37+00:00 | 75,09277 | €66,62 | 1,38 | TARGET |
| Master Adaptive Gb20 V1 | AKE | LONG | 2026-07-26T04:08:36+00:00 | 0,00339 | €21,15 | 0,43 | STOP_GAP_STRESS |
| Benchmark Bollinger mean reversion 1H | PEPE | SHORT | 2026-07-26T04:08:36+00:00 | 0,00000 | €-54,29 | -1,09 | STOP |

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

Generato: 2026-07-26 05:14 UTC


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

Segnali totali salvati: **54**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-07-26 | BTC | 64.454,23 | +5 | +4 | +3 | +2 | +1 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-07-26 | DOGE | 0.07344 | +2 | +3 | +2 | +2 | -2 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-07-26 | SOL | 75,10 | 0 | +4 | +3 | +2 | -3 | -1 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-07-25 | BTC | 64.087,96 | +2 | +3 | +3 | +2 | -2 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-07-25 | DOGE | 0.06949 | -1 | +2 | +1 | +2 | -3 | -1 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-07-25 | SOL | 74,17 | 0 | +4 | +3 | +2 | -3 | -1 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-07-24 | BTC | 65.302,77 | 0 | +2 | +2 | +3 | -2 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-07-24 | DOGE | 0.06902 | -5 | -1 | -1 | 0 | -3 | -1 | 0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-07-24 | SOL | 75,72 | 0 | +4 | +3 | +2 | -3 | -1 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-07-23 | BTC | 65.399,99 | +1 | +2 | +2 | +3 | -1 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-07-23 | DOGE | 0.07229 | -3 | -1 | -1 | 0 | -2 | -1 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-07-23 | SOL | 77,14 | +1 | +3 | +2 | +2 | -2 | -1 | 0 | HOLD LEGGERO / ATTESA CONFERME |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 18 | 17 | 16 | 15 | 13 | 11 | 8 | 4 | 0 | 0 | 0 | 0 |
| SOL | 18 | 17 | 16 | 15 | 13 | 11 | 8 | 4 | 0 | 0 | 0 | 0 |
| DOGE | 18 | 17 | 16 | 15 | 13 | 11 | 8 | 4 | 0 | 0 | 0 | 0 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-07-13 | 14g | 2026-07-27 | domani |
| SOL | 2026-07-13 | 14g | 2026-07-27 | domani |
| DOGE | 2026-07-13 | 14g | 2026-07-27 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 15 | 40,00% | +0,08% | +0,11% | FEEDBACK RAPIDO |
| BTC | 2g | 14 | 42,86% | +0,24% | +0,02% | FEEDBACK RAPIDO |
| BTC | 3g | 14 | 42,86% | +0,14% | -0,14% | FEEDBACK RAPIDO |
| BTC | 5g | 12 | 33,33% | +0,83% | -0,23% | FEEDBACK RAPIDO |
| BTC | 7g | 10 | 50,00% | +1,60% | +0,65% | FEEDBACK RAPIDO |
| BTC | 10g | 8 | 75,00% | +2,19% | +2,03% | FEEDBACK RAPIDO |
| BTC | 14g | 4 | 100,00% | +1,69% | +1,69% | FEEDBACK RAPIDO |
| BTC | 21g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 30g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 1g | 14 | 42,86% | -0,19% | -0,69% | FEEDBACK RAPIDO |
| SOL | 2g | 14 | 21,43% | -0,41% | -1,09% | FEEDBACK RAPIDO |
| SOL | 3g | 14 | 14,29% | -0,64% | -1,49% | FEEDBACK RAPIDO |
| SOL | 5g | 12 | 33,33% | -0,65% | -1,39% | FEEDBACK RAPIDO |
| SOL | 7g | 10 | 50,00% | -0,25% | -0,93% | FEEDBACK RAPIDO |
| SOL | 10g | 7 | 28,57% | -0,53% | -1,29% | FEEDBACK RAPIDO |
| SOL | 14g | 3 | 33,33% | -2,53% | -1,33% | FEEDBACK RAPIDO |
| SOL | 21g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 30g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 1g | 17 | 52,94% | -0,02% | +0,02% | FEEDBACK RAPIDO |
| DOGE | 2g | 16 | 56,25% | -0,30% | +0,30% | FEEDBACK RAPIDO |
| DOGE | 3g | 15 | 53,33% | -0,79% | +0,79% | FEEDBACK RAPIDO |
| DOGE | 5g | 13 | 61,54% | -0,88% | +0,88% | FEEDBACK RAPIDO |
| DOGE | 7g | 11 | 72,73% | -1,21% | +1,21% | FEEDBACK RAPIDO |
| DOGE | 10g | 8 | 62,50% | -1,76% | +1,76% | FEEDBACK RAPIDO |
| DOGE | 14g | 4 | 75,00% | -3,15% | +3,15% | FEEDBACK RAPIDO |
| DOGE | 21g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 30g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 15 | 40,00% | +0,08% | +0,11% | -0,14% | +0,76% | FEEDBACK RAPIDO |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 17 | 41,18% | +0,04% | +0,04% | -0,18% | +0,65% | FEEDBACK RAPIDO |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 17 | 41,18% | +0,04% | +0,04% | -0,18% | +0,65% | FEEDBACK RAPIDO |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 13 | 38,46% | -0,02% | -0,02% | -0,25% | +0,51% | FEEDBACK RAPIDO |
| BTC | 1g | Tecnico | CALIBRABILE | 14 | 35,71% | +0,04% | -0,56% | -0,21% | +0,63% | FEEDBACK RAPIDO |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +2,00% | +2,00% | +1,48% | +2,25% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 14 | 42,86% | +0,24% | +0,02% | -0,31% | +1,19% | FEEDBACK RAPIDO |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 16 | 43,75% | +0,16% | +0,16% | -0,34% | +1,07% | FEEDBACK RAPIDO |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 16 | 43,75% | +0,16% | +0,16% | -0,34% | +1,07% | FEEDBACK RAPIDO |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 12 | 41,67% | -0,02% | -0,02% | -0,56% | +0,95% | FEEDBACK RAPIDO |
| BTC | 2g | Tecnico | CALIBRABILE | 13 | 46,15% | +0,31% | -0,23% | -0,21% | +1,21% | FEEDBACK RAPIDO |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +3,18% | +3,18% | +3,05% | +3,89% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 14 | 42,86% | +0,14% | -0,14% | -1,36% | +2,05% | FEEDBACK RAPIDO |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 15 | 60,00% | +0,30% | +0,30% | -1,23% | +2,09% | FEEDBACK RAPIDO |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 15 | 60,00% | +0,30% | +0,30% | -1,23% | +2,09% | FEEDBACK RAPIDO |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 11 | 63,64% | +0,34% | +0,34% | -1,25% | +2,02% | FEEDBACK RAPIDO |
| BTC | 3g | Tecnico | CALIBRABILE | 12 | 41,67% | +0,81% | -0,07% | -0,99% | +2,38% | FEEDBACK RAPIDO |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,88% | +1,88% | +1,44% | +4,24% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 12 | 33,33% | +0,83% | -0,23% | -1,96% | +2,98% | FEEDBACK RAPIDO |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 13 | 53,85% | +0,95% | +0,95% | -1,83% | +3,12% | FEEDBACK RAPIDO |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 13 | 53,85% | +0,95% | +0,95% | -1,83% | +3,12% | FEEDBACK RAPIDO |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 10 | 60,00% | +1,32% | +1,32% | -1,90% | +3,11% | FEEDBACK RAPIDO |
| BTC | 5g | Tecnico | CALIBRABILE | 11 | 45,45% | +1,16% | -0,83% | -1,61% | +3,33% | FEEDBACK RAPIDO |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,16% | -0,16% | -0,37% | +4,24% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 10 | 50,00% | +1,60% | +0,65% | -2,04% | +3,67% | FEEDBACK RAPIDO |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 11 | 72,73% | +1,49% | +1,49% | -1,88% | +3,77% | FEEDBACK RAPIDO |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 11 | 72,73% | +1,49% | +1,49% | -1,88% | +3,77% | FEEDBACK RAPIDO |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 10 | 80,00% | +1,68% | +1,68% | -1,90% | +3,81% | FEEDBACK RAPIDO |
| BTC | 7g | Tecnico | CALIBRABILE | 10 | 40,00% | +1,67% | -0,49% | -1,74% | +3,89% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 8 | 75,00% | +2,19% | +2,03% | -2,36% | +4,37% | FEEDBACK RAPIDO |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 8 | 87,50% | +2,19% | +2,19% | -2,36% | +4,37% | FEEDBACK RAPIDO |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 8 | 87,50% | +2,19% | +2,19% | -2,36% | +4,37% | FEEDBACK RAPIDO |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 8 | 87,50% | +2,19% | +2,19% | -2,36% | +4,37% | FEEDBACK RAPIDO |
| BTC | 10g | Tecnico | CALIBRABILE | 7 | 28,57% | +2,43% | -0,34% | -2,23% | +4,62% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 4 | 100,00% | +1,69% | +1,69% | -3,09% | +4,98% | FEEDBACK RAPIDO |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 4 | 100,00% | +1,69% | +1,69% | -3,09% | +4,98% | FEEDBACK RAPIDO |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 4 | 100,00% | +1,69% | +1,69% | -3,09% | +4,98% | FEEDBACK RAPIDO |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 4 | 100,00% | +1,69% | +1,69% | -3,09% | +4,98% | FEEDBACK RAPIDO |
| BTC | 14g | Tecnico | CALIBRABILE | 3 | 33,33% | +1,50% | -0,83% | -3,03% | +5,05% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 17 | 52,94% | -0,02% | +0,02% | -0,43% | +0,66% | FEEDBACK RAPIDO |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 17 | 58,82% | -0,02% | +0,69% | -0,43% | +0,66% | FEEDBACK RAPIDO |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 17 | 58,82% | -0,02% | +0,69% | -0,43% | +0,66% | FEEDBACK RAPIDO |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 15 | 60,00% | +0,23% | +0,53% | -0,21% | +0,95% | FEEDBACK RAPIDO |
| DOGE | 1g | Tecnico | CALIBRABILE | 17 | 52,94% | -0,02% | +0,02% | -0,43% | +0,66% | FEEDBACK RAPIDO |
| DOGE | 1g | Classic technical | CALIBRABILE | 16 | 50,00% | +0,05% | -0,05% | -0,35% | +0,67% | FEEDBACK RAPIDO |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +3,18% | +3,18% | +1,82% | +3,24% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 16 | 56,25% | -0,30% | +0,30% | -0,97% | +0,91% | FEEDBACK RAPIDO |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 16 | 56,25% | -0,30% | +0,30% | -0,97% | +0,91% | FEEDBACK RAPIDO |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 16 | 56,25% | -0,30% | +0,30% | -0,97% | +0,91% | FEEDBACK RAPIDO |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 14 | 57,14% | -0,52% | +0,52% | -1,09% | +0,85% | FEEDBACK RAPIDO |
| DOGE | 2g | Tecnico | CALIBRABILE | 16 | 56,25% | -0,30% | +0,30% | -0,97% | +0,91% | FEEDBACK RAPIDO |
| DOGE | 2g | Classic technical | CALIBRABILE | 15 | 53,33% | -0,16% | +0,16% | -0,88% | +1,11% | FEEDBACK RAPIDO |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +6,40% | +6,40% | +3,75% | +6,18% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 15 | 53,33% | -0,79% | +0,79% | -2,36% | +1,77% | FEEDBACK RAPIDO |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 15 | 53,33% | -0,79% | +0,79% | -2,36% | +1,77% | FEEDBACK RAPIDO |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 15 | 53,33% | -0,79% | +0,79% | -2,36% | +1,77% | FEEDBACK RAPIDO |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 14 | 57,14% | -0,96% | +0,96% | -2,13% | +1,80% | FEEDBACK RAPIDO |
| DOGE | 3g | Tecnico | CALIBRABILE | 15 | 53,33% | -0,79% | +0,79% | -2,36% | +1,77% | FEEDBACK RAPIDO |
| DOGE | 3g | Classic technical | CALIBRABILE | 14 | 50,00% | -0,70% | +0,70% | -2,36% | +1,87% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 13 | 61,54% | -0,88% | +0,88% | -3,10% | +2,27% | FEEDBACK RAPIDO |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 13 | 61,54% | -0,88% | +0,88% | -3,10% | +2,27% | FEEDBACK RAPIDO |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 13 | 61,54% | -0,88% | +0,88% | -3,10% | +2,27% | FEEDBACK RAPIDO |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 13 | 61,54% | -0,88% | +0,88% | -3,10% | +2,27% | FEEDBACK RAPIDO |
| DOGE | 5g | Tecnico | CALIBRABILE | 13 | 61,54% | -0,88% | +0,88% | -3,10% | +2,27% | FEEDBACK RAPIDO |
| DOGE | 5g | Classic technical | CALIBRABILE | 12 | 58,33% | -0,71% | +0,71% | -3,04% | +2,42% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 11 | 72,73% | -1,21% | +1,21% | -3,45% | +2,43% | FEEDBACK RAPIDO |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 11 | 72,73% | -1,21% | +1,21% | -3,45% | +2,43% | FEEDBACK RAPIDO |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 11 | 72,73% | -1,21% | +1,21% | -3,45% | +2,43% | FEEDBACK RAPIDO |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 11 | 72,73% | -1,21% | +1,21% | -3,45% | +2,43% | FEEDBACK RAPIDO |
| DOGE | 7g | Tecnico | CALIBRABILE | 11 | 72,73% | -1,21% | +1,21% | -3,45% | +2,43% | FEEDBACK RAPIDO |
| DOGE | 7g | Classic technical | CALIBRABILE | 10 | 70,00% | -1,23% | +1,23% | -3,40% | +2,63% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 8 | 62,50% | -1,76% | +1,76% | -4,08% | +2,60% | FEEDBACK RAPIDO |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 8 | 62,50% | -1,76% | +1,76% | -4,08% | +2,60% | FEEDBACK RAPIDO |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 8 | 62,50% | -1,76% | +1,76% | -4,08% | +2,60% | FEEDBACK RAPIDO |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 8 | 62,50% | -1,76% | +1,76% | -4,08% | +2,60% | FEEDBACK RAPIDO |
| DOGE | 10g | Tecnico | CALIBRABILE | 8 | 62,50% | -1,76% | +1,76% | -4,08% | +2,60% | FEEDBACK RAPIDO |
| DOGE | 10g | Classic technical | CALIBRABILE | 7 | 57,14% | -1,15% | +1,15% | -3,67% | +2,89% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 4 | 75,00% | -3,15% | +3,15% | -5,68% | +2,68% | FEEDBACK RAPIDO |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 4 | 75,00% | -3,15% | +3,15% | -5,68% | +2,68% | FEEDBACK RAPIDO |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 4 | 75,00% | -3,15% | +3,15% | -5,68% | +2,68% | FEEDBACK RAPIDO |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 4 | 75,00% | -3,15% | +3,15% | -5,68% | +2,68% | FEEDBACK RAPIDO |
| DOGE | 14g | Tecnico | CALIBRABILE | 4 | 75,00% | -3,15% | +3,15% | -5,68% | +2,68% | FEEDBACK RAPIDO |
| DOGE | 14g | Classic technical | CALIBRABILE | 4 | 75,00% | -3,15% | +3,15% | -5,68% | +2,68% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 14 | 42,86% | -0,19% | -0,69% | -0,54% | +0,67% | FEEDBACK RAPIDO |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 13 | 61,54% | -0,73% | -0,06% | -0,99% | +0,04% | FEEDBACK RAPIDO |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 16 | 56,25% | -0,39% | -0,26% | -0,73% | +0,38% | FEEDBACK RAPIDO |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 11 | 45,45% | -0,36% | +0,01% | -0,89% | +0,37% | FEEDBACK RAPIDO |
| SOL | 1g | Tecnico | CALIBRABILE | 17 | 58,82% | -0,19% | -0,02% | -0,56% | +0,54% | FEEDBACK RAPIDO |
| SOL | 1g | Classic technical | CALIBRABILE | 9 | 66,67% | -0,06% | +0,06% | -0,41% | +0,48% | FEEDBACK RAPIDO |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,51% | -0,51% | -0,47% | +0,31% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 14 | 21,43% | -0,41% | -1,09% | -1,02% | +0,84% | FEEDBACK RAPIDO |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 12 | 41,67% | -0,96% | -0,57% | -1,71% | +0,06% | FEEDBACK RAPIDO |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 15 | 40,00% | -0,70% | -0,53% | -1,38% | +0,60% | FEEDBACK RAPIDO |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 10 | 30,00% | -0,89% | -0,80% | -1,64% | +0,63% | FEEDBACK RAPIDO |
| SOL | 2g | Tecnico | CALIBRABILE | 16 | 37,50% | -0,51% | -0,21% | -1,14% | +0,77% | FEEDBACK RAPIDO |
| SOL | 2g | Classic technical | CALIBRABILE | 8 | 50,00% | -0,11% | +0,11% | -0,50% | +0,37% | FEEDBACK RAPIDO |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -1,38% | -1,38% | -1,57% | +0,62% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 14 | 14,29% | -0,64% | -1,49% | -2,30% | +2,00% | FEEDBACK RAPIDO |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 11 | 36,36% | -1,19% | -0,49% | -2,95% | +1,42% | FEEDBACK RAPIDO |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 14 | 35,71% | -0,87% | -0,45% | -2,58% | +1,84% | FEEDBACK RAPIDO |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 9 | 33,33% | -1,04% | -1,24% | -2,62% | +1,92% | FEEDBACK RAPIDO |
| SOL | 3g | Tecnico | CALIBRABILE | 15 | 40,00% | -0,71% | -0,08% | -2,32% | +1,95% | FEEDBACK RAPIDO |
| SOL | 3g | Classic technical | CALIBRABILE | 7 | 28,57% | +0,30% | -0,30% | -1,81% | +2,01% | FEEDBACK RAPIDO |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -3,20% | -3,20% | -3,71% | +0,62% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 12 | 33,33% | -0,65% | -1,39% | -2,98% | +2,94% | FEEDBACK RAPIDO |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 9 | 55,56% | -0,86% | -0,48% | -3,50% | +2,36% | FEEDBACK RAPIDO |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 12 | 50,00% | -0,46% | -0,53% | -3,13% | +2,75% | FEEDBACK RAPIDO |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 8 | 50,00% | -1,44% | -0,52% | -3,48% | +2,57% | FEEDBACK RAPIDO |
| SOL | 5g | Tecnico | CALIBRABILE | 13 | 38,46% | -0,62% | -0,65% | -3,10% | +2,81% | FEEDBACK RAPIDO |
| SOL | 5g | Classic technical | CALIBRABILE | 5 | 40,00% | +1,33% | -1,33% | -1,45% | +3,95% | FEEDBACK RAPIDO |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -3,99% | -3,99% | -6,07% | +0,62% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 10 | 50,00% | -0,25% | -0,93% | -3,39% | +3,32% | FEEDBACK RAPIDO |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 8 | 75,00% | -0,69% | +0,78% | -3,79% | +2,87% | FEEDBACK RAPIDO |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 11 | 72,73% | -0,53% | +0,59% | -3,50% | +3,16% | FEEDBACK RAPIDO |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 7 | 57,14% | -0,52% | -0,22% | -3,76% | +3,04% | FEEDBACK RAPIDO |
| SOL | 7g | Tecnico | CALIBRABILE | 11 | 27,27% | -0,53% | -1,32% | -3,50% | +3,16% | FEEDBACK RAPIDO |
| SOL | 7g | Classic technical | CALIBRABILE | 4 | 50,00% | +0,02% | -0,02% | -2,24% | +4,25% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 7 | 28,57% | -0,53% | -1,29% | -4,33% | +2,87% | FEEDBACK RAPIDO |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 6 | 50,00% | -1,25% | -0,21% | -4,69% | +2,50% | FEEDBACK RAPIDO |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 8 | 37,50% | -0,74% | -0,35% | -4,48% | +2,71% | FEEDBACK RAPIDO |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 6 | 33,33% | -0,43% | -1,35% | -4,48% | +2,76% | FEEDBACK RAPIDO |
| SOL | 10g | Tecnico | CALIBRABILE | 8 | 50,00% | -0,74% | +0,13% | -4,48% | +2,71% | FEEDBACK RAPIDO |
| SOL | 10g | Classic technical | CALIBRABILE | 1 | 100,00% | -1,18% | +1,18% | -3,42% | +3,59% | FEEDBACK RAPIDO |
| SOL | 10g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 14g | Global confluence | BENCHMARK | 3 | 33,33% | -2,53% | -1,33% | -5,20% | +2,16% | FEEDBACK RAPIDO |
| SOL | 14g | Famiglia statistica | CALIBRABILE | 3 | 100,00% | -1,83% | +1,83% | -5,16% | +2,20% | FEEDBACK RAPIDO |
| SOL | 14g | Scanner grezzo | DIAGNOSTICO | 4 | 100,00% | -2,54% | +2,54% | -5,28% | +2,00% | FEEDBACK RAPIDO |
| SOL | 14g | Market regime grezzo | DIAGNOSTICO | 3 | 33,33% | -2,53% | -1,33% | -5,20% | +2,16% | FEEDBACK RAPIDO |
| SOL | 14g | Tecnico | CALIBRABILE | 4 | 0,00% | -2,54% | -2,54% | -5,28% | +2,00% | FEEDBACK RAPIDO |
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

Generato: 2026-07-26 05:14 UTC

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
| BTC | 18 | FEEDBACK RAPIDO | 17 | 0 | 0 | 0 | Famiglia statistica | 1g | 41,18% | +0,04% | feedback rapido: utile da osservare, non da pesare |
| SOL | 18 | FEEDBACK RAPIDO | 17 | 0 | 0 | 0 | Tecnico | 1g | 58,82% | -0,02% | feedback rapido: utile da osservare, non da pesare |
| DOGE | 18 | FEEDBACK RAPIDO | 17 | 0 | 0 | 0 | Famiglia statistica | 1g | 58,82% | +0,69% | feedback rapido: utile da osservare, non da pesare |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Famiglia statistica | 17 | 41,18% | +0,04% | +0,04% | -0,18% | +0,65% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Microstruttura exchange | 1 | 100,00% | +2,00% | +2,00% | +1,48% | +2,25% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 14 | 35,71% | -0,56% | +0,04% | -0,21% | +0,63% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Famiglia statistica | 16 | 43,75% | +0,16% | +0,16% | -0,34% | +1,07% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Microstruttura exchange | 1 | 100,00% | +3,18% | +3,18% | +3,05% | +3,89% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 13 | 46,15% | -0,23% | +0,31% | -0,21% | +1,21% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Famiglia statistica | 15 | 60,00% | +0,30% | +0,30% | -1,23% | +2,09% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Microstruttura exchange | 1 | 100,00% | +1,88% | +1,88% | +1,44% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 12 | 41,67% | -0,07% | +0,81% | -0,99% | +2,38% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 13 | 53,85% | +0,95% | +0,95% | -1,83% | +3,12% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -0,16% | -0,16% | -0,37% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 11 | 45,45% | -0,83% | +1,16% | -1,61% | +3,33% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 11 | 72,73% | +1,49% | +1,49% | -1,88% | +3,77% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 10 | 40,00% | -0,49% | +1,67% | -1,74% | +3,89% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 8 | 87,50% | +2,19% | +2,19% | -2,36% | +4,37% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 7 | 28,57% | -0,34% | +2,43% | -2,23% | +4,62% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Famiglia statistica | 4 | 100,00% | +1,69% | +1,69% | -3,09% | +4,98% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 3 | 33,33% | -0,83% | +1,50% | -3,03% | +5,05% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 16 | 50,00% | -0,05% | +0,05% | -0,35% | +0,67% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Famiglia statistica | 17 | 58,82% | +0,69% | -0,02% | -0,43% | +0,66% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Microstruttura exchange | 2 | 100,00% | +3,18% | +3,18% | +1,82% | +3,24% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 17 | 52,94% | +0,02% | -0,02% | -0,43% | +0,66% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Classic technical | 15 | 53,33% | +0,16% | -0,16% | -0,88% | +1,11% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Famiglia statistica | 16 | 56,25% | +0,30% | -0,30% | -0,97% | +0,91% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Microstruttura exchange | 1 | 100,00% | +6,40% | +6,40% | +3,75% | +6,18% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 16 | 56,25% | +0,30% | -0,30% | -0,97% | +0,91% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Classic technical | 14 | 50,00% | +0,70% | -0,70% | -2,36% | +1,87% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Famiglia statistica | 15 | 53,33% | +0,79% | -0,79% | -2,36% | +1,77% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 15 | 53,33% | +0,79% | -0,79% | -2,36% | +1,77% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Classic technical | 12 | 58,33% | +0,71% | -0,71% | -3,04% | +2,42% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 13 | 61,54% | +0,88% | -0,88% | -3,10% | +2,27% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 13 | 61,54% | +0,88% | -0,88% | -3,10% | +2,27% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Classic technical | 10 | 70,00% | +1,23% | -1,23% | -3,40% | +2,63% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 11 | 72,73% | +1,21% | -1,21% | -3,45% | +2,43% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 11 | 72,73% | +1,21% | -1,21% | -3,45% | +2,43% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Classic technical | 7 | 57,14% | +1,15% | -1,15% | -3,67% | +2,89% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 8 | 62,50% | +1,76% | -1,76% | -4,08% | +2,60% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 8 | 62,50% | +1,76% | -1,76% | -4,08% | +2,60% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Classic technical | 4 | 75,00% | +3,15% | -3,15% | -5,68% | +2,68% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Famiglia statistica | 4 | 75,00% | +3,15% | -3,15% | -5,68% | +2,68% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 4 | 75,00% | +3,15% | -3,15% | -5,68% | +2,68% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Classic technical | 9 | 66,67% | +0,06% | -0,06% | -0,41% | +0,48% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Famiglia statistica | 13 | 61,54% | -0,06% | -0,73% | -0,99% | +0,04% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 1 | 0,00% | -0,51% | -0,51% | -0,47% | +0,31% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 17 | 58,82% | -0,02% | -0,19% | -0,56% | +0,54% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Classic technical | 8 | 50,00% | +0,11% | -0,11% | -0,50% | +0,37% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Famiglia statistica | 12 | 41,67% | -0,57% | -0,96% | -1,71% | +0,06% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Microstruttura exchange | 1 | 0,00% | -1,38% | -1,38% | -1,57% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 16 | 37,50% | -0,21% | -0,51% | -1,14% | +0,77% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Classic technical | 7 | 28,57% | -0,30% | +0,30% | -1,81% | +2,01% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Famiglia statistica | 11 | 36,36% | -0,49% | -1,19% | -2,95% | +1,42% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Microstruttura exchange | 1 | 0,00% | -3,20% | -3,20% | -3,71% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 15 | 40,00% | -0,08% | -0,71% | -2,32% | +1,95% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Classic technical | 5 | 40,00% | -1,33% | +1,33% | -1,45% | +3,95% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 9 | 55,56% | -0,48% | -0,86% | -3,50% | +2,36% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -3,99% | -3,99% | -6,07% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 13 | 38,46% | -0,65% | -0,62% | -3,10% | +2,81% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Classic technical | 4 | 50,00% | -0,02% | +0,02% | -2,24% | +4,25% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 8 | 75,00% | +0,78% | -0,69% | -3,79% | +2,87% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 11 | 27,27% | -1,32% | -0,53% | -3,50% | +3,16% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Classic technical | 1 | 100,00% | +1,18% | -1,18% | -3,42% | +3,59% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 6 | 50,00% | -0,21% | -1,25% | -4,69% | +2,50% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 8 | 50,00% | +0,13% | -0,74% | -4,48% | +2,71% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Famiglia statistica | 3 | 100,00% | +1,83% | -1,83% | -5,16% | +2,20% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Frattale SOL | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Tecnico | 4 | 0,00% | -2,54% | -2,54% | -5,28% | +2,00% | OSSERVA | 0,0 | BASSA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 17 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 15 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 17 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Famiglia statistica | 48 | 47,92% | +0,16% |
| BTC | BREVE | Microstruttura exchange | 3 | 100,00% | +2,36% |
| BTC | BREVE | Tecnico | 39 | 41,03% | -0,30% |
| BTC | SETTIMANALE | Famiglia statistica | 32 | 68,75% | +1,44% |
| BTC | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -0,16% |
| BTC | SETTIMANALE | Tecnico | 28 | 39,29% | -0,59% |
| BTC | SWING | Famiglia statistica | 4 | 100,00% | +1,69% |
| BTC | SWING | Tecnico | 3 | 33,33% | -0,83% |
| DOGE | BREVE | Classic technical | 45 | 51,11% | +0,25% |
| DOGE | BREVE | Famiglia statistica | 48 | 56,25% | +0,59% |
| DOGE | BREVE | Microstruttura exchange | 3 | 100,00% | +4,26% |
| DOGE | BREVE | Tecnico | 48 | 54,17% | +0,35% |
| DOGE | SETTIMANALE | Classic technical | 29 | 62,07% | +1,00% |
| DOGE | SETTIMANALE | Famiglia statistica | 32 | 65,62% | +1,21% |
| DOGE | SETTIMANALE | Tecnico | 32 | 65,62% | +1,21% |
| DOGE | SWING | Classic technical | 4 | 75,00% | +3,15% |
| DOGE | SWING | Famiglia statistica | 4 | 75,00% | +3,15% |
| DOGE | SWING | Tecnico | 4 | 75,00% | +3,15% |
| SOL | BREVE | Classic technical | 24 | 50,00% | -0,03% |
| SOL | BREVE | Famiglia statistica | 36 | 47,22% | -0,36% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 3 | 0,00% | -1,70% |
| SOL | BREVE | Tecnico | 48 | 45,83% | -0,10% |
| SOL | SETTIMANALE | Classic technical | 10 | 50,00% | -0,55% |
| SOL | SETTIMANALE | Famiglia statistica | 23 | 60,87% | +0,03% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -3,99% |
| SOL | SETTIMANALE | Tecnico | 32 | 37,50% | -0,69% |
| SOL | SWING | Famiglia statistica | 3 | 100,00% | +1,83% |
| SOL | SWING | Frattale SOL | 1 | 0,00% | -1,13% |
| SOL | SWING | Tecnico | 4 | 0,00% | -2,54% |

## Aree ancora in attesa

| Asset | Famiglia | Righe senza controlli | Stato |
| --- | --- | --- | --- |
| BTC | BREVE | 6 | in attesa di controlli maturati |
| BTC | SETTIMANALE | 8 | in attesa di controlli maturati |
| BTC | SWING | 8 | in attesa di controlli maturati |
| BTC | MEDIO | 15 | in attesa di controlli maturati |
| SOL | SETTIMANALE | 2 | in attesa di controlli maturati |
| SOL | SWING | 7 | in attesa di controlli maturati |
| SOL | MEDIO | 15 | in attesa di controlli maturati |
| DOGE | BREVE | 4 | in attesa di controlli maturati |
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
| BTC     |         18 |               0 |          18 | RACCOLTA DATI | n/a              | n/a             | n/a                   | n/a            |
| SOL     |         18 |               0 |          18 | RACCOLTA DATI | n/a              | n/a             | n/a                   | n/a            |
| DOGE    |         18 |               0 |          18 | RACCOLTA DATI | n/a              | n/a             | n/a                   | n/a            |

Regola: sotto 60 controlli osserva soltanto; da 100+ controlli può diventare utile per correggere rischio spot/leva nel Decision Report.

## Ultima lettura rapida

| Asset   | Rischio spot   | Rischio leva   | Nota leva                                                         |
|:--------|:---------------|:---------------|:------------------------------------------------------------------|
| BTC     | MEDIO          | MOLTO ALTO     | spot/tranche; se proprio leva, massimo 2x con margine molto largo |
| SOL     | MEDIO          | MOLTO ALTO     | leva da limitare; 2x/3x solo con invalidazione chiara             |
| DOGE    | MEDIO          | MOLTO ALTO     | spot/tranche; se proprio leva, massimo 2x con margine molto largo |
<!-- RISK_CALIBRATION_END -->

</details>
<!-- COMPACT_SECTION_END:risk_calibration -->

<!-- COMPACT_SECTION_START:global_confluence -->
<details open>
<summary><strong>🌐 Global Confluence — quadro finale</strong></summary>

<!-- GLOBAL_CONFLUENCE_START -->
# Sintesi finale di confluenza

Generato: 2026-07-26 05:14 UTC


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
| BTC | +5 | MODERATAMENTE POSITIVA | Costruttivo prudente | MEDIA | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE | Prima resistenza sopra 66.910; conferma del doppio minimo sopra 67.248. | Sotto 57.748 il quadro tecnico peggiora. |
| SOL | 0 | MISTA / PARZIALE | Neutrale / misto | BASSA / RACCOLTA DATI | HOLD LEGGERO / ATTESA CONFERME | conferma del doppio minimo sopra 75,94; nuova conferma tecnica sopra 78,73; milestone analogiche 98,70 / 106,85, valide soltanto se rientra anche il gap frattale. | Allarmi sotto 71,33 / 73,40 / 62,19. |
| DOGE | +2 | MISTA / PARZIALE | Neutrale / misto | BASSA / RACCOLTA DATI | STAI ALLA FINESTRA | Sopra 0.07923 migliora; sopra 0.07966 viene invalidato il pattern ribassista dominante. | Sotto 0.07097 il rischio ribassista aumenta. |

## Punteggi per modulo

| Asset | Scanner grezzo | Market grezzo | Famiglia statistica | Scanner path | Tecnico | Classic tech | Frattale SOL | Fractal path | RSI top-cycle | Lifecycle EMA | Exchange flow | Futures | Daily change | Totale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +3 | +2 | +4 | 0 | +1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | +5 |
| SOL | +3 | +2 | +4 | 0 | -3 | -1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| DOGE | +2 | +2 | +3 | 0 | -2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | +1 | +2 |

Le colonne **Scanner grezzo** e **Market grezzo** sono diagnostiche: nel totale entra soltanto la colonna **Famiglia statistica**.

## Lettura asset per asset

### BTC

- Confluenza: **MODERATAMENTE POSITIVA**
- Bias: **Costruttivo prudente**
- Punteggio finale: **+5**
- Affidabilità: **MEDIA**
- Azione coerente: **ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE**

BTC è l'asset messo meglio nel breve, ma lo score statistico ora conta Scanner e Market Regime una sola volta. La struttura macro resta debole: ha più senso accumulare a tranche sui pullback che inseguire il prezzo vicino alle resistenze.

Dettaglio moduli:

- Famiglia statistica: **+4** — Scanner grezzo +3, Market Regime grezzo +2, match regime 10. Scanner e regime concordi con almeno 10 match: bonus massimo di 1 punto. Punteggio contato nel Global: +4.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **+3** — Casi positivi 65,00%, return centrale 30g +9,80%. Direzione scanner: SALITA. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **+2** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 10, positivi 30g 70,00%, return p50 +4,13%.
- Scanner path: **0** — Controlli disponibili 16. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **+1** — Score tecnico 1/12, verdetto neutrale / misto, trend misto, struttura volatilità in espansione, divergenza rialzista rsi, Wyckoff possibile accumulazione, pattern score 0 (rialzista Doppio minimo / CANDIDATO; ribassista Doppio massimo / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **0** — Score classico -2/12, verdetto DEBOLE / NON CONFERMATO, stage STAGE 4 / MARKDOWN, struttura MASSIMI E MINIMI CRESCENTI, Wyckoff ACCUMULO POSSIBILE / RANGE BASSO, volatilità locale BASSO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Non applicabile a questo asset.
- Fractal path: **0** — Non applicabile a questo asset.
- RSI top-cycle: **0** — Non applicabile a questo asset.
- Lifecycle EMA: **0** — Non applicabile a questo asset.
- Exchange flow: **0** — Flow -0.25, derivati +0.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +0.00; exchange 3/3, copertura 100%, consenso bull 1, bear 1, divergenze 0, campioni 4h 9 su 4.00h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias MISTA / NEUTRALE; confidenza BASSA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Misto, forza 1/5.
- Daily change: **0** — BTC: cambiamento medio in misto rispetto a ieri.

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

- Famiglia statistica: **+4** — Scanner grezzo +3, Market Regime grezzo +2, match regime 19. Scanner e regime concordi con almeno 10 match: bonus massimo di 1 punto. Punteggio contato nel Global: +4.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **+3** — Casi positivi 70,00%, return centrale 30g +5,22%. Direzione scanner: SALITA. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **+2** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 19, positivi 30g 73,68%, return p50 +5,72%.
- Scanner path: **0** — Controlli disponibili 16. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **-3** — Score tecnico -10/12, verdetto ribassista tecnico, trend ribassista, struttura compressione / triangolo, divergenza ribassista nascosta rsi, Wyckoff markdown / fase ribassista, pattern score +1 (rialzista Doppio minimo / MATURO; ribassista Doppio massimo / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **-1** — Score classico -11/12, verdetto RIBASSISTA / FRAGILE, stage STAGE 4 / MARKDOWN, struttura MASSIMI E MINIMI DECRESCENTI, Wyckoff ACCUMULO POSSIBILE / RANGE BASSO, volatilità locale BASSO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Verdetto ANALOGIA DEBOLE / SCENARIO SECONDARIO, somiglianza strutturale +64,17%, aderenza live +65,93%, errore live +17,03%, gap corrente +9,25%, peso operativo 0, tracking STRUTTURA STABILE, fase FRATTALE SOLO DI CONTESTO, rischio ALTO.
- Fractal path: **0** — Controlli disponibili 12, ma percorso ancorato non aderente: gap +9,25%, errore live +17,03%. Peso 0.
- RSI top-cycle: **0** — Rischio top-cycle RSI: BASSO.
- Lifecycle EMA: **0** — Contesto non pesato nel Global. Lifecycle score 4, bias SQUEEZE SETUP MODERATO, EMA200 112,75 $, upside EMA200 +50,16%, gap EMA50/EMA200 -3,07%, hit EMA200 12w +16,67%, trend STABILE / DA CONFERMARE. Peso Global forzato a 0.
- Exchange flow: **0** — Flow +1.75, derivati +0.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +1.00; exchange 3/3, copertura 100%, consenso bull 1, bear 1, divergenze 0, campioni 4h 9 su 4.00h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias LEGGERMENTE POSITIVA / NON PESATA; confidenza MEDIA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Misto, forza 1/5.
- Daily change: **0** — SOL: nessun cambiamento forte in misto rispetto a ieri.

Conferme: conferma del doppio minimo sopra 75,94; nuova conferma tecnica sopra 78,73; milestone analogiche 98,70 / 106,85, valide soltanto se rientra anche il gap frattale.

Invalidazioni: Allarmi sotto 71,33 / 73,40 / 62,19.

### DOGE

- Confluenza: **MISTA / PARZIALE**
- Bias: **Neutrale / misto**
- Punteggio finale: **+2**
- Affidabilità: **BASSA / RACCOLTA DATI**
- Azione coerente: **STAI ALLA FINESTRA**

DOGE non ha ancora una confluenza pulita. Serve conferma tecnica prima di trattarlo come asset forte.

Dettaglio moduli:

- Famiglia statistica: **+3** — Scanner grezzo +2, Market Regime grezzo +2, match regime 28. Scanner e regime concordi con almeno 10 match: bonus massimo di 1 punto. Punteggio contato nel Global: +3.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **+2** — Casi positivi 62,50%, return centrale 30g +4,13%. Direzione scanner: SALITA. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **+2** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 28, positivi 30g 67,86%, return p50 +5,62%.
- Scanner path: **0** — Controlli disponibili 16. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **-2** — Score tecnico -5/12, verdetto debole, trend ribassista, struttura ribassista con massimi e minimi decrescenti, divergenza ribassista nascosta rsi, Wyckoff possibile accumulazione, pattern score -1 (rialzista Doppio minimo / CANDIDATO; ribassista Triplo massimo / MATURO). Fonte: technical_structure_metrics.csv.
- Classic technical: **0** — Score classico -2/12, verdetto DEBOLE / NON CONFERMATO, stage STAGE 4 / MARKDOWN, struttura COMPRESSIONE / TRIANGOLO POSSIBILE, Wyckoff SPRING / TEST POSSIBILE, volatilità locale BASSO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Non applicabile a questo asset.
- Fractal path: **0** — Non applicabile a questo asset.
- RSI top-cycle: **0** — Non applicabile a questo asset.
- Lifecycle EMA: **0** — Non applicabile a questo asset.
- Exchange flow: **0** — Flow +1.75, derivati -0.50, affollamento +0.00, liquidazioni +0.00, conferme tecniche +0.75; exchange 3/3, copertura 100%, consenso bull 0, bear 3, divergenze 0, campioni 4h 9 su 4.00h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias LEGGERMENTE POSITIVA / NON PESATA; confidenza MEDIA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
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

Generato: 2026-07-26 05:14 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [btc_macro_cycle_report.md](btc_macro_cycle_report.md)

Questo modulo descrive il contesto macro di Bitcoin. Non genera entrate tattiche, non autorizza leva e pesa **0** nel Global Confluence.

## Sintesi

| Voce | Valore | Lettura |
| --- | --- | --- |
| Prezzo BTC | 64.454 $ | prezzo corrente |
| Power Law centrale | 122.834 $ | deviazione -47,53% |
| Banda p10-p90 | 76.424 $ / 308.286 $ | SOTTO LA BANDA P10 |
| Percentile residuo | 1,99% | posizione storica nel corridoio |
| Esponente β | 5,8366 | R² log-log 91,98% |
| Stabilità β | BASSA | range 1,3086 cambiando finestra |
| Ultimo halving | 2024-04-19 | 828 giorni fa |
| Fase ciclo | 56,67% | percentuale indicativa del ciclo quadriennale |
| Peso Global | 0 | CONTESTO MACRO / DIAGNOSTICO |

La Power Law viene trattata come regressione empirica, non come legge fisica. Il report mostra quanto cambia l'esponente usando finestre iniziali diverse e la confronta con il benchmark ingenuo 'prezzo invariato'.

## Bitcoin Power Law

- Campione: 2014-09-17 → 2026-07-26 (4330 osservazioni)
- Formula stimata: prezzo ≈ exp(-39.3247) × giorni^5.8366
- Prezzo centrale oggi: **122.834 $**
- Posizione corrente: **SOTTO LA BANDA P10**, percentile 1,99%
- Scarto dal centro: **-47,53%**

![Bitcoin Power Law](btc_power_law_chart.png)

![Bitcoin Power Law log-log](btc_power_law_loglog_chart.png)

### Stabilità dell'esponente

| Inizio campione | β | R² log-log |
| --- | --- | --- |
| 2014 | 5,8366 | 91,98% |
| 2015 | 5,9226 | 91,54% |
| 2016 | 5,6116 | 87,78% |
| 2017 | 4,8814 | 82,88% |
| 2018 | 4,6140 | 78,35% |

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
| 2012-11-28 → 2016-07-09 | 2014-12-16 | -35,84% | -11,15% | -28,59% | +39,10% |
| 2016-07-09 → 2020-05-11 | 2018-09-12 | -1,22% | -46,08% | -38,52% | +63,89% |
| 2020-05-11 → 2024-04-19 | 2022-08-05 | -14,18% | -13,22% | +1,87% | +24,70% |

Campione molto piccolo: questi rendimenti sono contesto di ciclo, non probabilità affidabili.

## SOL/BTC e DOGE/BTC dentro il tempo Bitcoin

![Altcoin nel ciclo BTC](alt_btc_cycle_spirals.png)

| Asset | Coppia | Forza vs BTC | Score raw | Candidato | 30g | Peso Global |
| --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | SOTTOPERFORMA BTC | -4 | -1 | 2.9151959633912927 | 0 |
| DOGE | DOGE/BTC | SOTTOPERFORMA BTC | -5 | -1 | -8.974206382920535 | 0 |

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

Generato: 2026-07-26 05:14 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [relative_strength_btc_report.md](relative_strength_btc_report.md)

Questo modulo controlla se SOL e DOGE stanno davvero battendo Bitcoin. Una salita in USD accompagnata da una coppia ALT/BTC ribassista è spesso soltanto trascinamento di BTC.

**Protezione iniziale:** il candidato relativo è limitato a -1/0/+1, ma il peso nel Global resta **0**. La coppia BTC conferma o indebolisce il tecnico USD; non viene sommata come secondo modulo indipendente.

## Sintesi

| Asset | Coppia | Prezzo | Score raw | Candidato | Peso Global | Forza vs BTC | Confidenza | 30g | Tecnico USD | Lettura combinata |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | 0.00116500 | -4 | -1 | 0 | SOTTOPERFORMA BTC | BASSA | +2,92% | RIBASSISTA | DEBOLEZZA COMPLETA: scende in USD e contro BTC |
| DOGE | DOGE/BTC | 0.00000114 | -5 | -1 | 0 | SOTTOPERFORMA BTC | MEDIA | -8,97% | RIBASSISTA | DEBOLEZZA COMPLETA: scende in USD e contro BTC |

## Matrice di lettura

| ALT/USD | ALT/BTC | Interpretazione |
| --- | --- | --- |
| Rialzista | Rialzista | Conferma migliore: sale e batte BTC |
| Rialzista | Ribassista | Sale soprattutto perché BTC trascina il mercato |
| Ribassista | Rialzista | Forza relativa nascosta / possibile rotazione futura |
| Ribassista | Ribassista | Debolezza completa |

## SOL/BTC

- **Verdetto relativo:** SOTTOPERFORMA BTC (-4)
- **Candidato futuro:** -1; **peso attuale Global: 0**
- **Lettura combinata USD/BTC:** DEBOLEZZA COMPLETA: scende in USD e contro BTC
- **Struttura:** COMPRESSIONE / TRIANGOLO POSSIBILE
- **Rendimenti relativi:** 7g +0,00%; 30g +2,92%; 90g +5,43%; 180g -17,20%
- **Daily:** RSI 43.19; MA50 0.00116676; MA200 0.00121484
- **Weekly:** MA30 0.00121990; RSI 44.93
- **Livelli:** supporto 0.00116400; resistenza 0.00119500; breakout 60g 0.00134900; breakdown 60g 0.00100900
- **Pattern:** DOPPIO MINIMO / TARGET RAGGIUNTO; neckline 0.00113200; target 0.00117200
- **Fibonacci:** VICINO — 50.0% a 0.00117900
- **Fonte:** Yahoo Finance SOL-BTC (coppia diretta)
- **Motivi score:** prezzo sotto MA50 daily; prezzo sotto MA200 daily; MA50 daily in salita; prezzo sotto MA30 weekly; MA30 weekly in discesa; MACD relativo negativo

![Grafico SOL/BTC](relative_strength_SOLBTC.png)

## DOGE/BTC

- **Verdetto relativo:** SOTTOPERFORMA BTC (-5)
- **Candidato futuro:** -1; **peso attuale Global: 0**
- **Lettura combinata USD/BTC:** DEBOLEZZA COMPLETA: scende in USD e contro BTC
- **Struttura:** MASSIMI E MINIMI DECRESCENTI
- **Rendimenti relativi:** 7g +1,92%; 30g -8,97%; 90g -9,70%; 180g -17,73%
- **Daily:** RSI 45.76; MA50 0.00000123; MA200 0.00000134
- **Weekly:** MA30 0.00000134; RSI 33.38
- **Livelli:** supporto 0.00000112; resistenza 0.00000121; breakout 60g 0.00000153; breakdown 60g 0.00000107
- **Pattern:** DOPPIO MASSIMO / CONFERMATO; neckline 0.00000112; target 0.00000099
- **Fibonacci:** VICINO — 23.6% a 0.00000115
- **Fonte:** Rapporto sintetico DOGE-USD / BTC-USD (sintetica)
- **Motivi score:** prezzo sotto MA50 daily; prezzo sotto MA200 daily; MA50 daily in discesa; prezzo sotto MA30 weekly; MA30 weekly in discesa; struttura con massimi/minimi decrescenti; MACD relativo positivo

![Grafico DOGE/BTC](relative_strength_DOGEBTC.png)

## Backtest storico diagnostico

Il backtest usa soltanto indicatori disponibili alla data del segnale e campiona una volta a settimana. È utile subito, ma non sostituisce il tracker live: le soglie sono state definite prima di vedere il risultato.

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto direzione | Return futuro mediano |
| --- | --- | --- | --- | --- | --- |
| SOL | 7g | 202 | 51,98% | +1,96% | -1,34% |
| SOL | 30g | 200 | 48,00% | +4,76% | +0,44% |
| SOL | 90g | 195 | 53,85% | +10,36% | +1,62% |
| DOGE | 7g | 291 | 56,01% | +1,87% | -1,77% |
| DOGE | 30g | 288 | 52,78% | +2,00% | -3,71% |
| DOGE | 90g | 285 | 54,04% | +6,94% | -8,47% |

## Tracker live e gate futuro

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto | Stato | Peso Global |
| --- | --- | --- | --- | --- | --- | --- |
| SOL | 1g | 2 | 0,00% | -0,61% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 3g | 0 | n/a | n/a | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 7g | 0 | n/a | n/a | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 14g | 0 | n/a | n/a | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 30g | 0 | n/a | n/a | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 1g | 15 | 80,00% | +0,20% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 3g | 13 | 76,92% | +1,30% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 7g | 9 | 77,78% | +3,02% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 14g | 2 | 100,00% | +1,26% | LOCKED / RACCOLTA LIVE | 0 |
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

Ultima candela SOL usata: **26 luglio 2026**

## Verdetto: ANALOGIA DEBOLE / SCENARIO SECONDARIO

- **Fase attuale:** FRATTALE SOLO DI CONTESTO
- **Somiglianza totale:** +64,17%
- **Somiglianza strutturale:** +64,17%
- **Aderenza prezzo live:** +65,93%
- **Errore medio live:** +17,03%
- **Gap prezzo corrente:** +9,25%
- **Peso operativo suggerito:** 0
- **Affidabilita:** BASSA
- **Rischio fase:** ALTO
- **Trend tracking:** STRUTTURA STABILE
- **Sintesi:** Esistono alcuni elementi comuni, ma non abbastanza per una conferma.
- **SOL è al giorno:** 50 dal bottom usato.
- **Giorno BTC equivalente:** 2023-01-10
- **Prossimo step:** Proiezione condizionale, non conferma operativa: **Spinta rialzista abbastanza pulita.** Zona bassa **75,08 $** intorno al **26 luglio 2026**; zona alta **98,70 $** intorno al **8 agosto 2026**; fine step circa **97,42 $** entro il **9 agosto 2026**.

## Somiglianza prima e dopo inizio programma

Questa sezione separa la somiglianza della forma dall'aderenza reale del prezzo.

- **Inizio programma/scanner:** 3 luglio 2026
- **Prima del programma** = backtest retroattivo.
- **Da inizio programma** = verifica live: è la parte più importante per l'uso operativo.

| Periodo | Date | Giorni | Aderenza prezzo | Errore medio | Gap ultimo | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| Prima del programma | 6 giugno 2026 -> 2 luglio 2026 | 27 | +87,95% | +6,02% | +21,89% | ABBASTANZA ALLINEATO |
| Da inizio programma | 3 luglio 2026 -> 26 luglio 2026 | 24 | +65,93% | +17,03% | +9,25% | STACCATO / NON ADERENTE |
| Totale dal bottom | 6 giugno 2026 -> 26 luglio 2026 | 51 | +77,59% | +11,21% | +9,25% | DEVIAZIONE MODERATA |

Nota: un frattale può avere una forma simile ma un prezzo distante. In quel caso non è operativo finché il gap non rientra.

## Lettura operativa veloce

Il frattale non deve generare acquisti o leva adesso. La forma è un contesto, ma l'aderenza live del prezzo è insufficiente.

| Voce | Risposta | Perché |
| --- | --- | --- |
| Uso operativo | NO | Il frattale vale 0 punti operativi finché il prezzo resta non aderente. |
| Aderenza live | +65,93% | Errore medio live +17,03%. |
| Gap corrente | +9,25% | Deve rientrare circa entro ±12%. |
| Prima conferma prezzo | 98,70 $ | Serve anche miglioramento del gap, non solo una candela sopra il livello. |
| Seconda conferma | 106,85 $ | Rende più credibile il percorso, ma non sostituisce l'aderenza. |
| Invalidazione soft | 71,33 $ | Sotto questa zona il quadro peggiora. |
| Invalidazione forte | 62,19 $ | Sotto il bottom il paragone è quasi rotto. |

## Target ciclo fino al top BTC 2025

| Voce | Valore |
| --- | --- |
| Stato | CONTESTO / NON OPERATIVO |
| Top BTC 2025 | 6 ottobre 2025 - 124.753 $ |
| Data SOL equivalente | 21 aprile 2029 |
| Target ciclo base da oggi | 536,87 $ |
| Massimo percorso base | 536,87 $ (21 aprile 2029) |

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
| Prima conferma | 98,70 $ | Deve accompagnarsi al rientro del gap. |
| Seconda conferma | 106,85 $ | Scenario più credibile. |
| Invalidazione soft | 71,33 $ | Il frattale si indebolisce. |
| Invalidazione forte | 62,19 $ | Il paragone si rompe. |

## Proiezione veloce con date SOL

| Orizzonte | Data SOL | BTC fece | SOL base | Min percorso | Max percorso |
| --- | --- | --- | --- | --- | --- |
| 7 giorni | 2 agosto 2026 | +21,30% | 91,07 $ | 75,08 $ | 91,10 $ |
| 14 giorni | 9 agosto 2026 | +29,75% | 97,42 $ | 75,08 $ | 98,70 $ |
| 30 giorni | 25 agosto 2026 | +25,06% | 93,90 $ | 75,08 $ | 102,31 $ |
| 60 giorni | 24 settembre 2026 | +18,26% | 88,79 $ | 75,08 $ | 106,85 $ |
| 90 giorni | 24 ottobre 2026 | +69,97% | 127,61 $ | 75,08 $ | 127,61 $ |
| 120 giorni | 23 novembre 2026 | +58,32% | 118,87 $ | 75,08 $ | 131,19 $ |

## Prossimi step se SOL segue BTC 2022

| Step | Date SOL | BTC fine | SOL zona bassa | SOL zona alta | SOL fine base | Lettura |
| --- | --- | --- | --- | --- | --- | --- |
| Step 1 - prossime 2 settimane | 26 luglio 2026 -> 9 agosto 2026 | +29,75% | 75,08 $ (26 luglio 2026) | 98,70 $ (8 agosto 2026) | 97,42 $ | Spinta rialzista abbastanza pulita. |
| Step 2 - primo mese | 10 agosto 2026 -> 25 agosto 2026 | +25,06% | 93,90 $ (25 agosto 2026) | 102,31 $ (14 agosto 2026) | 93,90 $ | Spinta rialzista abbastanza pulita. |
| Step 3 - secondo mese | 26 agosto 2026 -> 24 settembre 2026 | +18,26% | 86,88 $ (23 settembre 2026) | 106,85 $ (5 settembre 2026) | 88,79 $ | Spinta rialzista abbastanza pulita. |
| Step 4 - terzo mese | 25 settembre 2026 -> 24 ottobre 2026 | +69,97% | 95,38 $ (25 settembre 2026) | 127,61 $ (24 ottobre 2026) | 127,61 $ | Spinta rialzista abbastanza pulita. |

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
| Prezzo SOL | 75,08 $ |  |
| Weekly RSI | 39,20 / linea grezza 53,89 | LINEA NON AFFIDABILE / RISCHIO NON ATTIVO — IRREALISTICA / NON OPERATIVA |
| Monthly RSI | 40,74 / linea grezza 56,16 | RSI TROPPO BASSO PER RISCHIO TOP — VALIDA / USO PRUDENTE |
| Target ciclo base | 536,87 $ | Avanzamento +13,98% |
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
| Score on-chain | 2 |
| Bias | POSITIVA |
| Azione coerente | CONFERMA MODERATA / BUONO SE IL FRATTALE REGGE |
| Prezzo SOL | 75,08 $ |
| TVL Solana | 4,83 mld $ |
| TVL 7g | -0,55% |
| DEX volume 24h | 1,14 mld $ |
| Fees 24h | 7,20 mln $ |
| Stablecoin su Solana | 16,96 mld $ |
| Stake ratio | 67,96% |
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
| Prezzo SOL | 75,08 $ |
| EMA200 weekly target | 112,75 $ |
| Upside verso EMA200 | +50,16% |
| Distanza prezzo da EMA200 | -33,40% |
| Gap EMA50/EMA200 | -3,07% |
| Stato cross | EMA50 SOTTO EMA200 |
| RSI weekly | 39,20 |
| Età SOL | 6,3 anni |
| Analoghi storici usati | 30 |
| Max analoghi per asset | 3 |
| Hit EMA200 12w analoghi | +16,67% |
| Max gain mediano 12w | +22,38% |
| Drawdown mediano 12w | -22,62% |

Lettura semplice:

**CONTESTO INTERESSANTE, SERVONO CONFERME DI PREZZO**

Autocontrollo: **STABILE / DA CONFERMARE**.

Questo modulo confronta SOL con altre crypto in fasi simili di età, distanza da EMA200, EMA50/EMA200 e RSI. Non usa stock market.

Nota importante: **questo modulo ora NON pesa più nel Global Confluence**. Resta solo come contesto di ciclo e come mappa verso EMA200 weekly. Il punteggio Global resta guidato da prezzo, scanner, regime, struttura tecnica, frattale, RSI e conferme reali.

Nota: se EMA50/EMA200 sono dentro ±2%, il modulo parla di medie sovrapposte / incrocio in corso, perché exchange diversi possono mostrare il cross leggermente prima o dopo.

<!-- Generato: 2026-07-26 05:14 UTC -->
<!-- MAJOR_ALT_LIFECYCLE_SQUEEZE_END -->

</details>
<!-- COMPACT_SECTION_END:major_alt_lifecycle -->

# Report giornaliero BTC / SOL / DOGE

Aggiornato il: **2026-07-26 05:12:22 UTC**

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
- SOL: nessun cambiamento forte rispetto a ieri.
- DOGE: cambiamento importante in miglioramento rispetto a ieri.

| Asset | Cambio | Tono | Verdetto oggi | Casi positivi oggi | Δ casi positivi |
| --- | --- | --- | --- | --- | --- |
| BTC | CAMBIAMENTO MEDIO | misto | RIALZISTA | +65.00% | 0.00 punti |
| SOL | NESSUN CAMBIAMENTO FORTE | misto | RIALZISTA | +70.00% | +2.50 punti |
| DOGE | CAMBIAMENTO FORTE | miglioramento | RIALZISTA | +62.50% | +7.50 punti |

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
| BTC | 61.237 $ | 70.906 $ | +46,67% | +15,79% | rimbalzo debole | 70.906 $ | 61.237 $ | +8,70% | -13,64% | spike storicamente più resistente |
| SOL | 71,33 $ | 82,59 $ | +26,92% | +15,79% | rimbalzo poco frequente | 82,59 $ | 71,33 $ | +9,52% | -13,64% | spike storicamente più resistente |
| DOGE | 0,06982 $ | 0,08084 $ | +39,29% | +15,79% | rimbalzo debole | 0,08084 $ | 0,06982 $ | +46,67% | -13,64% | scarico possibile |

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

- **BTC: su 40 casi simili, 30 prima sono scesi a -5,00%. Tra quei 30, 14 poi sono rimbalzati fino a +10,00%. Percentuale: +46,67% (14/30). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.**
- **BTC: su 40 casi simili, 23 prima sono saliti a +10,00%. Tra quei 23, 2 poi sono scaricati a -5,00%. Percentuale: +8,70% (2/23). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.**
- **SOL: su 40 casi simili, 26 prima sono scesi a -5,00%. Tra quei 26, 7 poi sono rimbalzati fino a +10,00%. Percentuale: +26,92% (7/26). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.**
- **SOL: su 40 casi simili, 21 prima sono saliti a +10,00%. Tra quei 21, 2 poi sono scaricati a -5,00%. Percentuale: +9,52% (2/21). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.**
- **DOGE: su 40 casi simili, 28 prima sono scesi a -5,00%. Tra quei 28, 11 poi sono rimbalzati fino a +10,00%. Percentuale: +39,29% (11/28). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.**
- **DOGE: su 40 casi simili, 30 prima sono saliti a +10,00%. Tra quei 30, 14 poi sono scaricati a -5,00%. Percentuale: +46,67% (14/30). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: scarico possibile.**

<!-- BOUNCE_AFTER_DRAWDOWN_END -->

</details>
<!-- COMPACT_SECTION_END:bounce_after_drawdown -->

<!-- COMPACT_SECTION_START:scanner_forecast -->
<details>
<summary><strong>🔭 Cono probabilistico dello scanner</strong></summary>

<!-- SCANNER_FORECAST_TRACKER_START -->
# Scanner forecast path / cono probabilistico

Generato: 2026-07-26 05:13:49 UTC


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
| BTC | 2026-07-26 | 64.460 $ | SALITA | 65,00% | 48.268,54 $ | 58.798,28 $ | 70.778,63 $ | 80.557,98 $ | 92.919,73 $ |
| SOL | 2026-07-26 | 75,08 $ | SALITA | 70,00% | 67,32 $ | 72,97 $ | 79,00 $ | 89,50 $ | 103,41 $ |
| DOGE | 2026-07-26 | 0.07349 $ | SALITA | 62,50% | 0.05983 $ | 0.06792 $ | 0.07652 $ | 0.08648 $ | 0.09707 $ |

## Grafici

### BTC

![Scanner forecast BTC](scanner_forecast_BTC.png)

#### Verifica storica e discrepanza

![Verifica storica cono BTC](scanner_forecast_history_BTC.png)

- Cono congelato il **2026-07-10**; verificato fino al **2026-07-26**; stato **PARZIALE 16/30g**.
- Reale **64.457,40 $**; p50 previsto **66.789,34 $**; scarto **-3,49%**.
- Errore medio assoluto **3,77%**; massimo **7,75%**; DENTRO p10-p90; DENTRO p25-p75.

### SOL

![Scanner forecast SOL](scanner_forecast_SOL.png)

#### Verifica storica e discrepanza

![Verifica storica cono SOL](scanner_forecast_history_SOL.png)

- Cono congelato il **2026-07-10**; verificato fino al **2026-07-26**; stato **PARZIALE 16/30g**.
- Reale **75,10 $**; p50 previsto **73,63 $**; scarto **1,99%**.
- Errore medio assoluto **2,58%**; massimo **5,38%**; DENTRO p10-p90; DENTRO p25-p75.

### DOGE

![Scanner forecast DOGE](scanner_forecast_DOGE.png)

#### Verifica storica e discrepanza

![Verifica storica cono DOGE](scanner_forecast_history_DOGE.png)

- Cono congelato il **2026-07-10**; verificato fino al **2026-07-26**; stato **PARZIALE 16/30g**.
- Reale **0.07344 $**; p50 previsto **0.06087 $**; scarto **20,65%**.
- Errore medio assoluto **7,57%**; massimo **28,04%**; DENTRO p10-p90; FUORI p25-p75.

## Accuratezza percorso scanner

| Asset   | Giorno   |   Controlli | Dentro p10-p90   | Dentro p25-p75   | Errore medio abs vs p50   | Errore medio vs p50   |
|:--------|:---------|------------:|:-----------------|:-----------------|:--------------------------|:----------------------|
| BTC | 1g | 16 | 100,00% | 68,75% | 1,83% | 0,01% |
| BTC | 3g | 14 | 100,00% | 64,29% | 2,53% | -0,30% |
| BTC | 7g | 10 | 100,00% | 80,00% | 2,94% | 0,15% |
| BTC | 14g | 3 | 100,00% | 66,67% | 1,89% | -1,40% |
| BTC | 30g | 0 | n/a | n/a | n/a | n/a |
| SOL | 1g | 16 | 75,00% | 56,25% | 2,26% | -0,24% |
| SOL | 3g | 14 | 100,00% | 57,14% | 2,88% | -0,72% |
| SOL | 7g | 10 | 100,00% | 100,00% | 2,51% | 1,09% |
| SOL | 14g | 3 | 100,00% | 100,00% | 2,90% | 2,90% |
| SOL | 30g | 0 | n/a | n/a | n/a | n/a |
| DOGE | 1g | 16 | 100,00% | 50,00% | 3,09% | 0,90% |
| DOGE | 3g | 14 | 100,00% | 92,86% | 2,26% | 1,19% |
| DOGE | 7g | 10 | 100,00% | 100,00% | 8,11% | 8,11% |
| DOGE | 14g | 3 | 100,00% | 33,33% | 21,15% | 21,15% |
| DOGE | 30g | 0 | n/a | n/a | n/a | n/a |

## Calibratore shadow

Il cono ufficiale resta grezzo e invariato. Il calibratore usa soltanto previsioni passate già mature, campionate una volta a settimana per ridurre la falsa indipendenza. Ogni orizzonte si attiva a 30 controlli indipendenti: parte al 25% della correzione stimata e cresce gradualmente fino al 100% a 100 controlli.

| Asset   | Orizzonte   |   Controlli indipendenti |   Soglia | Stato                  | Forza correzione   | Shift p50   |   Scala p10-p90 |
|:--------|:------------|-------------------------:|---------:|:-----------------------|:-------------------|:------------|----------------:|
| BTC | 1g | 3 | 30 | RACCOLTA (27 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 3g | 3 | 30 | RACCOLTA (27 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 7g | 2 | 30 | RACCOLTA (28 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 14g | 1 | 30 | RACCOLTA (29 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 30g | 0 | 30 | RACCOLTA (30 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 1g | 3 | 30 | RACCOLTA (27 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 3g | 3 | 30 | RACCOLTA (27 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 7g | 2 | 30 | RACCOLTA (28 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 14g | 1 | 30 | RACCOLTA (29 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 30g | 0 | 30 | RACCOLTA (30 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 1g | 3 | 30 | RACCOLTA (27 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 3g | 3 | 30 | RACCOLTA (27 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 7g | 2 | 30 | RACCOLTA (28 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 14g | 1 | 30 | RACCOLTA (29 mancanti) | 0,0% | 0,00% | 1,000 |
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

Righe salvate nello storico: **42**.

Questa sezione tiene un diario delle previsioni giornaliere a 30 giorni, senza appesantire il report principale.

| Data | Asset | Prezzo | Direzione | Casi positivi | Return p50 | Drawdown p50 | Max gain p50 | Controllo 30g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-07-26 | BTC | 64.460 $ | SALITA | 65,00% | 70.779 $ | 59.324 $ | 74.185 $ | 2026-08-25 |
| 2026-07-26 | DOGE | 0,07000 $ | SALITA | 62,50% | 0,08000 $ | 0,07000 $ | 0,08000 $ | 2026-08-25 |
| 2026-07-26 | SOL | 75,08 $ | SALITA | 70,00% | 79,00 $ | 68,87 $ | 83,93 $ | 2026-08-25 |

<!-- FORECAST_30D_HISTORY_END -->

</details>
<!-- COMPACT_SECTION_END:scanner_forecast -->

<!-- COMPACT_SECTION_START:extreme_cases -->
<details>
<summary><strong>⚠️ Percorso dei casi estremi</strong></summary>

<!-- EXTREME_CASES_PATH_START -->
# Extreme cases path report

Generato: 2026-07-26 05:13 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [extreme_cases_path_report.md](extreme_cases_path_report.md)

Questo report si attiva quando i casi positivi o negativi sono almeno **80%**.

Ora misura anche il **rialzo massimo prima della discesa principale**, quindi distingue uno spike iniziale da una discesa quasi immediata.

## Trigger estremi

| Asset   | Direzione   | Trigger   | Percentuale   | Motivo                           |   Match disponibili |
|:--------|:------------|:----------|:--------------|:---------------------------------|--------------------:|
| BTC     | NESSUNO     | NO        | +65,00%       | Nessun lato sopra soglia estrema |                  40 |
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
- Casi positivi / salita storica: **65,00%**
- Casi negativi / discesa storica: **35,00%**
- Quanto è netto il segnale: **medio**
- Prezzo attuale: **64.459,57 $**
- Return normale fra 30 giorni: **70.778,63 $** (9,80%)
- Drawdown normale durante il mese: **59.323,94 $** (-7,97%)
- Drawdown brutto da rispettare: **53.216,74 $** (-17,44%)
- Max gain normale durante il mese: **74.184,96 $** (15,09%)
- Max gain buono / take profit ottimistico: **83.223,71 $** (29,11%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Solana
- Direzione più probabile a 30 giorni: **SALITA**
- Casi positivi / salita storica: **70,00%**
- Casi negativi / discesa storica: **30,00%**
- Quanto è netto il segnale: **forte**
- Prezzo attuale: **75,08 $**
- Return normale fra 30 giorni: **79,00 $** (5,22%)
- Drawdown normale durante il mese: **68,87 $** (-8,27%)
- Drawdown brutto da rispettare: **65,45 $** (-12,83%)
- Max gain normale durante il mese: **83,93 $** (11,78%)
- Max gain buono / take profit ottimistico: **93,51 $** (24,54%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Dogecoin
- Direzione più probabile a 30 giorni: **SALITA**
- Casi positivi / salita storica: **62,50%**
- Casi negativi / discesa storica: **37,50%**
- Quanto è netto il segnale: **medio**
- Prezzo attuale: **0,07 $**
- Return normale fra 30 giorni: **0,08 $** (4,13%)
- Drawdown normale durante il mese: **0,07 $** (-7,57%)
- Drawdown brutto da rispettare: **0,06 $** (-17,02%)
- Max gain normale durante il mese: **0,08 $** (15,51%)
- Max gain buono / take profit ottimistico: **0,10 $** (32,21%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Messaggio del giorno

Il quadro generale oggi è più favorevole. Lo scanner vede più possibilità di salita su più asset.

---

# Mappa semplice asset per asset

# Bitcoin — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟢 VERDE / Favorevole
**Prezzo attuale:** 64.459,57 $

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

- Se va molto male: **48.268,54 $** (-25,12%)
- Se va male: **58.798,28 $** (-8,78%)
- Scenario normale: **70.778,63 $** (9,80%)
- Se va bene: **80.557,98 $** (24,97%)
- Se va molto bene: **92.919,73 $** (44,15%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **59.323,94 $** (-7,97%)
- Discesa brutta: **53.216,74 $** (-17,44%)
- Discesa molto brutta: **46.982,08 $** (-27,11%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **74.184,96 $** (15,09%)
- Rialzo buono: **83.223,71 $** (29,11%)
- Rialzo molto forte: **99.573,66 $** (54,47%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Bitcoin tendeva a muoversi tra una zona bassa intorno a **59.323,94 $** e uno spike normale intorno a **74.184,96 $**.

La chiusura a 30 giorni era più spesso positiva: salita 65,00%, discesa 35,00%. Quindi la lettura principale è favorevole.

Nota leva BTC: se la liquidazione è vicina a 51.000 $, guarda soprattutto la discesa brutta e molto brutta. Il prezzo può recuperare dopo, ma la leva può saltare prima.

---

# Solana — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟢 VERDE / Favorevole
**Prezzo attuale:** 75,08 $

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

- Se va molto male: **67,32 $** (-10,33%)
- Se va male: **72,97 $** (-2,81%)
- Scenario normale: **79,00 $** (5,22%)
- Se va bene: **89,50 $** (19,20%)
- Se va molto bene: **103,41 $** (37,74%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **68,87 $** (-8,27%)
- Discesa brutta: **65,45 $** (-12,83%)
- Discesa molto brutta: **61,67 $** (-17,86%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **83,93 $** (11,78%)
- Rialzo buono: **93,51 $** (24,54%)
- Rialzo molto forte: **108,64 $** (44,69%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Solana tendeva a muoversi tra una zona bassa intorno a **68,87 $** e uno spike normale intorno a **83,93 $**.

La chiusura a 30 giorni era più spesso positiva: salita 70,00%, discesa 30,00%. Quindi la lettura principale è favorevole.

---

# Dogecoin — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟢 VERDE / Favorevole
**Prezzo attuale:** 0,07 $

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

- Se va molto male: **0,06 $** (-18,59%)
- Se va male: **0,07 $** (-7,58%)
- Scenario normale: **0,08 $** (4,13%)
- Se va bene: **0,09 $** (17,67%)
- Se va molto bene: **0,10 $** (32,09%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **0,07 $** (-7,57%)
- Discesa brutta: **0,06 $** (-17,02%)
- Discesa molto brutta: **0,06 $** (-23,42%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **0,08 $** (15,51%)
- Rialzo buono: **0,10 $** (32,21%)
- Rialzo molto forte: **0,10 $** (41,11%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Dogecoin tendeva a muoversi tra una zona bassa intorno a **0,07 $** e uno spike normale intorno a **0,08 $**.

La chiusura a 30 giorni era più spesso positiva: salita 62,50%, discesa 37,50%. Quindi la lettura principale è favorevole.

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

**Prezzo attuale:** 64.459,57 $

Bitcoin ha un segnale favorevole. La statistica dei casi simili indica più possibilità di salita che di discesa, ma resta comunque una probabilità, non una certezza.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **65,00%**
- Casi negativi dopo 30 giorni: **35,00%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **86,37%**
- Rendimento medio dopo 30 giorni: **10,73%**
- Rendimento centrale dopo 30 giorni: **9,80%**
- Discesa media durante i 30 giorni: **-11,76%**
- Massimo rialzo medio durante i 30 giorni: **25,59%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **71.378,75 $**
- Scenario centrale a 30 giorni: **70.778,63 $**
- Zona di rischio media: **56.877,24 $**
- Zona di rialzo media: **80.954,77 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -25,12% → **48.268,54 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -8,78% → **58.798,28 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: 9,80% → **70.778,63 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 24,97% → **80.557,98 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 44,15% → **92.919,73 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -27,11% → **46.982,08 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -17,44% → **53.216,74 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -7,97% → **59.323,94 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -5,33% → **61.023,16 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: -1,89% → **63.241,94 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 1,64% → **65.519,78 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 4,34% → **67.259,17 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 15,09% → **74.184,96 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 29,11% → **83.223,71 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 54,47% → **99.573,66 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| LRC-USD         | 2018-10-04   | 2019-01-11 |        91.74 |        35.3  |          -5.72 |         154.28 |
| XRP-USD         | 2019-10-09   | 2020-01-16 |        90.32 |        33.98 |          -3.56 |          46.48 |
| XLM-USD         | 2020-07-20   | 2020-10-27 |        89.48 |       104.8  |          -8.82 |         138.95 |
| FIL-USD         | 2023-07-04   | 2023-10-11 |        88.96 |        44.46 |          -0.01 |          44.46 |
| SAND-USD        | 2023-06-29   | 2023-10-06 |        88.68 |        24.82 |          -6.32 |          24.82 |
| ONE-USD         | 2020-01-22   | 2020-04-30 |        88.1  |         8.85 |          -5.79 |           9.61 |
| BTC-USD         | 2018-10-03   | 2019-01-10 |        87.65 |        -0.21 |          -7.6  |           1.35 |
| DOGE-USD        | 2020-07-20   | 2020-10-27 |        87.56 |        21.4  |          -5.98 |          57.04 |
| ETC-USD         | 2019-05-27   | 2019-09-03 |        87.4  |       -32.21 |         -32.86 |           3.5  |
| KSM-USD         | 2024-02-23   | 2024-06-01 |        87.22 |       -21.84 |         -23.92 |           7.69 |

---

# Approfondimento tecnico — Solana (SOL-USD)

## Semaforo: 🟢 VERDE / Favorevole

**Prezzo attuale:** 75,08 $

Solana ha un segnale favorevole. La statistica dei casi simili indica più possibilità di salita che di discesa, ma resta comunque una probabilità, non una certezza.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **70,00%**
- Casi negativi dopo 30 giorni: **30,00%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **76,84%**
- Rendimento medio dopo 30 giorni: **9,64%**
- Rendimento centrale dopo 30 giorni: **5,22%**
- Discesa media durante i 30 giorni: **-9,20%**
- Massimo rialzo medio durante i 30 giorni: **20,63%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **82,32 $**
- Scenario centrale a 30 giorni: **79,00 $**
- Zona di rischio media: **68,17 $**
- Zona di rialzo media: **90,57 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -10,33% → **67,32 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -2,81% → **72,97 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: 5,22% → **79,00 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 19,20% → **89,50 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 37,74% → **103,41 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -17,86% → **61,67 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -12,83% → **65,45 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -8,27% → **68,87 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -3,57% → **72,40 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: 0,00% → **75,08 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 2,65% → **77,07 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 5,04% → **78,86 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 11,78% → **83,93 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 24,54% → **93,51 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 44,69% → **108,64 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| WAVES-USD       | 2019-03-08   | 2019-06-15 |        81.79 |       -37.82 |         -38.96 |           1    |
| ENJ-USD         | 2018-10-04   | 2019-01-11 |        81.15 |       -12.02 |         -26.93 |           5.36 |
| QTUM-USD        | 2018-10-04   | 2019-01-11 |        80.27 |        -9.14 |         -19.1  |           3.33 |
| RUNE-USD        | 2025-12-22   | 2026-03-31 |        79.71 |        20.64 |          -8.4  |          23.46 |
| BNB-USD         | 2025-12-21   | 2026-03-30 |        79.55 |         1.44 |          -4.18 |           5.73 |
| SOL-USD         | 2025-12-19   | 2026-03-28 |        79.17 |         3.42 |          -3.74 |           8.51 |
| NEAR-USD        | 2025-12-16   | 2026-03-25 |        78.95 |        10.14 |          -9.23 |          12.11 |
| DASH-USD        | 2024-04-30   | 2024-08-07 |        78.76 |         4.72 |           0    |          21.92 |
| KAVA-USD        | 2025-12-21   | 2026-03-30 |        78.33 |         5.72 |          -7.96 |          14.26 |
| XRP-USD         | 2020-01-22   | 2020-04-30 |        78.2  |        -3.07 |          -8.83 |           5.24 |

---

# Approfondimento tecnico — Dogecoin (DOGE-USD)

## Semaforo: 🟢 VERDE / Favorevole

**Prezzo attuale:** 0,07 $

Dogecoin ha un segnale favorevole. La statistica dei casi simili indica più possibilità di salita che di discesa, ma resta comunque una probabilità, non una certezza.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **62,50%**
- Casi negativi dopo 30 giorni: **37,50%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **87,78%**
- Rendimento medio dopo 30 giorni: **4,98%**
- Rendimento centrale dopo 30 giorni: **4,13%**
- Discesa media durante i 30 giorni: **-11,33%**
- Massimo rialzo medio durante i 30 giorni: **20,83%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **0,08 $**
- Scenario centrale a 30 giorni: **0,08 $**
- Zona di rischio media: **0,07 $**
- Zona di rialzo media: **0,09 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -18,59% → **0,06 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -7,58% → **0,07 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: 4,13% → **0,08 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 17,67% → **0,09 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 32,09% → **0,10 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -23,42% → **0,06 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -17,02% → **0,06 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -7,57% → **0,07 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -4,27% → **0,07 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: 0,00% → **0,07 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 5,29% → **0,08 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 9,81% → **0,08 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 15,51% → **0,08 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 32,21% → **0,10 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 41,11% → **0,10 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| ZEC-USD         | 2019-06-01   | 2019-09-08 |        91.09 |       -23.97 |         -27.41 |           8.97 |
| DASH-USD        | 2022-03-07   | 2022-06-14 |        90.13 |         0.01 |          -8.31 |          19.82 |
| AVAX-USD        | 2025-08-29   | 2025-12-06 |        89.3  |         7.79 |         -14.74 |           8.89 |
| MKR-USD         | 2022-09-24   | 2023-01-01 |        89.13 |        27.72 |          -1.56 |          39.59 |
| NEAR-USD        | 2022-03-17   | 2022-06-24 |        88.8  |         8.87 |         -20.28 |          13.53 |
| THETA-USD       | 2022-03-11   | 2022-06-18 |        88.7  |        11.61 |          -6.22 |          26.91 |
| OMG-USD         | 2022-03-07   | 2022-06-14 |        88.7  |        -8.54 |         -14.76 |           5.54 |
| VET-USD         | 2022-03-09   | 2022-06-16 |        88.69 |         4.43 |          -5.37 |          15.47 |
| INJ-USD         | 2022-03-09   | 2022-06-16 |        88.47 |        -2.67 |         -13.24 |           7.61 |
| OP-USD          | 2025-12-22   | 2026-03-31 |        88.46 |         8.81 |          -3.72 |          21.82 |

</details>
<!-- COMPACT_SECTION_END:scanner_full_detail -->

<!-- COMPACT_SECTION_START:market_regime -->
<details>
<summary><strong>🌦️ Market Regime Match</strong></summary>

<!-- MARKET_REGIME_MATCH_START -->
# Market Regime Match Report


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [market_regime_match_report.md](market_regime_match_report.md)

Generated: 2026-07-26 05:14 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | BEAR | 64.460 $ | False | -16.69% | -9.82% | BEAR | -16.69% | -9.82% |
| DOGE-USD | BEAR | 0.07349 $ | False | -25.80% | -16.04% | BEAR | -16.69% | -9.82% |
| SOL-USD | BEAR | 75,08 $ | False | -11.47% | -16.65% | BEAR | -16.69% | -9.82% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 65.00% | 9.80% | 24.97% | 44.15% | -7.97% | -27.11% | 15.09% | 29.11% | 54.47% | 57.50% | 11.28% | 41.82% | 62.36% |
| BTC-USD | SAME_BTC_REGIME | 10 | 70.00% | 4.13% | 29.42% | 36.93% | -7.97% | -22.42% | 9.70% | 39.68% | 61.89% | 70.00% | 8.61% | 11.85% | 66.66% |
| BTC-USD | SAME_ASSET_REGIME | 19 | 78.95% | 22.59% | 34.64% | 45.89% | -6.41% | -19.08% | 22.59% | 43.10% | 55.04% | 78.95% | 29.73% | 53.27% | 62.75% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 10 | 70.00% | 4.13% | 29.42% | 36.93% | -7.97% | -22.42% | 9.70% | 39.68% | 61.89% | 70.00% | 8.61% | 11.85% | 66.66% |
| DOGE-USD | ALL_MATCHES | 40 | 62.50% | 4.13% | 17.67% | 32.09% | -7.57% | -23.42% | 15.51% | 32.21% | 41.11% | 82.50% | 26.27% | 40.81% | 60.86% |
| DOGE-USD | SAME_BTC_REGIME | 30 | 70.00% | 5.62% | 18.58% | 32.68% | -6.25% | -18.80% | 17.65% | 32.58% | 41.11% | 90.00% | 30.87% | 44.72% | 61.29% |
| DOGE-USD | SAME_ASSET_REGIME | 29 | 65.52% | 4.43% | 19.04% | 32.69% | -6.22% | -17.20% | 19.77% | 32.02% | 39.94% | 89.66% | 31.22% | 45.34% | 62.49% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 28 | 67.86% | 5.62% | 21.21% | 32.70% | -6.21% | -17.38% | 17.65% | 32.21% | 40.11% | 89.29% | 31.80% | 46.27% | 63.70% |
| SOL-USD | ALL_MATCHES | 40 | 70.00% | 5.22% | 19.20% | 37.74% | -8.27% | -17.86% | 11.78% | 24.54% | 44.69% | 62.50% | 2.91% | 25.71% | 62.83% |
| SOL-USD | SAME_BTC_REGIME | 20 | 75.00% | 7.59% | 19.37% | 36.45% | -8.16% | -19.88% | 16.76% | 24.19% | 48.78% | 75.00% | 2.91% | 32.98% | 89.20% |
| SOL-USD | SAME_ASSET_REGIME | 26 | 69.23% | 6.36% | 20.22% | 40.73% | -8.15% | -18.41% | 13.19% | 25.65% | 55.54% | 69.23% | 2.91% | 47.82% | 63.43% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 19 | 73.68% | 5.72% | 17.35% | 29.18% | -7.96% | -20.66% | 14.26% | 21.55% | 35.45% | 73.68% | 2.51% | 21.35% | 63.03% |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 10 | 70.00% | 4.13% | -7.97% | 39.68% | 70.00% | 8.61% | 41.90% |
| BTC-USD | HISTORICAL_BTC_BULL | 22 | 68.18% | 17.23% | -6.36% | 31.48% | 63.64% | 29.58% | 54.07% |
| BTC-USD | HISTORICAL_BTC_MIXED | 1 | 100.00% | 44.12% | -4.48% | 54.19% | 100.00% | 41.64% | 108.28% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 7 | 42.86% | -2.53% | -15.01% | 11.78% | 14.29% | -15.27% | 14.08% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 30 | 70.00% | 5.62% | -6.25% | 32.58% | 90.00% | 30.87% | 60.29% |
| DOGE-USD | HISTORICAL_BTC_BULL | 4 | 75.00% | 14.60% | -6.40% | 39.98% | 75.00% | 24.76% | 51.22% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 6 | 16.67% | -20.98% | -23.66% | 13.78% | 50.00% | 7.58% | 33.57% |
| SOL-USD | HISTORICAL_BTC_BEAR | 20 | 75.00% | 7.59% | -8.16% | 24.19% | 75.00% | 2.91% | 59.46% |
| SOL-USD | HISTORICAL_BTC_BULL | 6 | 83.33% | 20.86% | -1.03% | 42.59% | 83.33% | 35.62% | 64.07% |
| SOL-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 0.00% | -5.89% | -15.62% | 6.07% | 100.00% | 26.02% | 83.19% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 13 | 61.54% | 4.16% | -8.83% | 11.45% | 30.77% | -8.97% | 18.99% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 19 | 78.95% | 22.59% | -6.41% | 43.10% | 78.95% | 29.73% | 56.83% |
| BTC-USD | HISTORICAL_ASSET_BULL | 11 | 54.55% | 10.75% | -8.82% | 25.63% | 45.45% | -1.00% | 37.28% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 100.00% | 18.22% | -5.61% | 18.22% | 100.00% | 29.43% | 32.77% |
| BTC-USD | HISTORICAL_ASSET_MIXED | 2 | 50.00% | 3.45% | -21.88% | 41.66% | 50.00% | 2.47% | 82.23% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 7 | 42.86% | -2.53% | -15.01% | 11.78% | 14.29% | -15.27% | 14.08% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 29 | 65.52% | 4.43% | -6.22% | 32.02% | 89.66% | 31.22% | 60.33% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 5 | 80.00% | 8.87% | -17.54% | 34.30% | 100.00% | 24.07% | 49.59% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 6 | 33.33% | -17.99% | -19.88% | 13.78% | 33.33% | -14.29% | 30.13% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 26 | 69.23% | 6.36% | -8.15% | 25.65% | 69.23% | 2.91% | 64.07% |
| SOL-USD | HISTORICAL_ASSET_BULL | 1 | 0.00% | -37.82% | -38.96% | 1.00% | 0.00% | -50.22% | 1.00% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 100.00% | 19.99% | -1.20% | 24.50% | 100.00% | 42.40% | 47.99% |
| SOL-USD | HISTORICAL_ASSET_MIXED | 1 | 0.00% | -12.42% | -12.78% | 2.93% | 0.00% | -11.30% | 2.93% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 11 | 81.82% | 4.72% | -8.22% | 23.29% | 54.55% | 3.89% | 23.29% |

## Top regime-adjusted matches

The table below shows the top matches separately for each target, so BTC does not hide SOL and DOGE.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | LRC-USD | 2018-10-04 | 91.74% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 35.30% | -5.72% | 154.28% | 57.00% | -5.72% | 154.28% |
| BTC-USD | XRP-USD | 2019-10-09 | 90.32% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 33.98% | -3.56% | 46.48% | -38.29% | -38.91% | 46.48% |
| BTC-USD | BTC-USD | 2018-10-03 | 87.65% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -0.21% | -7.60% | 1.35% | 6.15% | -7.60% | 12.60% |
| BTC-USD | OMG-USD | 2018-10-04 | 86.68% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -8.64% | -21.63% | 0.39% | 11.07% | -21.63% | 11.07% |
| BTC-USD | ETH-USD | 2025-12-16 | 86.24% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 6.81% | -8.55% | 11.67% | -3.23% | -8.55% | 11.67% |
| BTC-USD | BNB-USD | 2018-10-04 | 86.03% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 51.62% | -8.34% | 51.62% | 153.58% | -8.34% | 153.58% |
| BTC-USD | BNB-USD | 2025-12-21 | 85.99% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 1.44% | -4.18% | 5.73% | 5.54% | -4.18% | 11.40% |
| BTC-USD | BTC-USD | 2025-12-20 | 85.65% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 15.76% | 0.00% | 19.26% | 11.50% | 0.00% | 24.54% |
| BTC-USD | APT-USD | 2024-09-16 | 85.54% | BEAR | BEAR | SAME_BTC_AND_ASSET | BEARISH_30D | -29.47% | -29.47% | 7.73% | -30.92% | -30.92% | 7.73% |
| BTC-USD | NEO-USD | 2018-10-04 | 85.27% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 0.18% | -13.66% | 1.68% | 11.97% | -13.66% | 28.15% |
| DOGE-USD | DASH-USD | 2022-03-07 | 90.13% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 0.01% | -8.31% | 19.82% | 30.52% | -8.31% | 30.52% |
| DOGE-USD | MKR-USD | 2022-09-24 | 89.13% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 27.72% | -1.56% | 39.59% | 72.17% | -1.56% | 80.88% |
| DOGE-USD | THETA-USD | 2022-03-11 | 88.70% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 11.61% | -6.22% | 26.91% | 19.72% | -6.22% | 43.44% |
| DOGE-USD | OMG-USD | 2022-03-07 | 88.70% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -8.54% | -14.76% | 5.54% | 24.58% | -14.76% | 24.58% |
| DOGE-USD | VET-USD | 2022-03-09 | 88.69% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 4.43% | -5.37% | 15.47% | 38.55% | -5.37% | 47.28% |
| DOGE-USD | INJ-USD | 2022-03-09 | 88.47% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -2.67% | -13.24% | 7.61% | 32.39% | -13.24% | 54.99% |
| DOGE-USD | OP-USD | 2025-12-22 | 88.46% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 8.81% | -3.72% | 21.82% | 8.70% | -3.72% | 56.00% |
| DOGE-USD | ENJ-USD | 2022-03-12 | 88.37% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 41.33% | 0.00% | 41.33% | 40.13% | 0.00% | 60.33% |
| DOGE-USD | QTUM-USD | 2022-03-07 | 88.36% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | -0.80% | -6.74% | 13.36% | 54.57% | -6.74% | 68.52% |
| DOGE-USD | RUNE-USD | 2022-03-08 | 88.17% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 6.81% | -22.98% | 22.31% | 37.54% | -22.98% | 46.15% |
| SOL-USD | ENJ-USD | 2018-10-04 | 81.15% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | -12.02% | -26.93% | 5.36% | 445.37% | -26.93% | 526.80% |
| SOL-USD | QTUM-USD | 2018-10-04 | 80.27% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -9.14% | -19.10% | 3.33% | -0.16% | -19.10% | 10.72% |
| SOL-USD | RUNE-USD | 2025-12-22 | 79.71% | BEAR | BEAR | SAME_BTC_AND_ASSET | BULLISH_30D | 20.64% | -8.40% | 23.46% | 3.30% | -8.40% | 52.16% |
| SOL-USD | BNB-USD | 2025-12-21 | 79.55% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 1.44% | -4.18% | 5.73% | 5.54% | -4.18% | 11.40% |
| SOL-USD | SOL-USD | 2025-12-19 | 79.17% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 3.42% | -3.74% | 8.51% | 0.43% | -3.74% | 18.70% |
| SOL-USD | NEAR-USD | 2025-12-16 | 78.95% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 10.14% | -9.23% | 12.11% | 87.14% | -9.23% | 91.97% |
| SOL-USD | KAVA-USD | 2025-12-21 | 78.33% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 5.72% | -7.96% | 14.26% | 2.51% | -7.96% | 24.10% |
| SOL-USD | ZIL-USD | 2018-10-06 | 77.95% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | -7.19% | -10.59% | 26.39% | -0.95% | -11.40% | 26.39% |
| SOL-USD | LRC-USD | 2018-10-04 | 77.51% | BEAR | BEAR | SAME_BTC_AND_ASSET | EXPLOSIVE_60D | 35.30% | -5.72% | 154.28% | 57.00% | -5.72% | 154.28% |
| SOL-USD | LINK-USD | 2025-12-16 | 77.04% | BEAR | BEAR | SAME_BTC_AND_ASSET | MIXED | 0.03% | -10.34% | 2.67% | 0.58% | -10.34% | 14.27% |

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

Generato: 2026-07-26 05:14 UTC


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
| BTC | 64.460 $ | -2 | DEBOLE / NON CONFERMATO | STAGE 4 / MARKDOWN | MASSIMI E MINIMI CRESCENTI | ACCUMULO POSSIBILE / RANGE BASSO | BASSO | RIDUCI RISCHIO / NO LONG A LEVA |
| SOL | 75,08 $ | -11 | RIBASSISTA / FRAGILE | STAGE 4 / MARKDOWN | MASSIMI E MINIMI DECRESCENTI | ACCUMULO POSSIBILE / RANGE BASSO | BASSO | NON INSEGUIRE / TAKE PROFIT SU SPIKE |
| DOGE | 0.07349 $ | -2 | DEBOLE / NON CONFERMATO | STAGE 4 / MARKDOWN | COMPRESSIONE / TRIANGOLO POSSIBILE | SPRING / TEST POSSIBILE | BASSO | NO LONG / SHORT SOLO DOPO SPIKE E REJECTION |

## Punteggi per area

| Asset | Trend | Struttura | Momentum | Volume | Prezzo | Candela | Wyckoff | Totale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | -4 | +2 | 0 | 0 | 0 | 0 | 0 | -2 |
| SOL | -4 | -2 | -3 | -2 | 0 | 0 | 0 | -11 |
| DOGE | -4 | 0 | +1 | 0 | 0 | 0 | +1 | -2 |

## Livelli tecnici

| Asset | Supporto | Resistenza | Breakout 60g | Breakdown 60g | ATR14 | Rendimento 30g | Rendimento 90g |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 63.062 $ | 64.598 $ | 77.991 $ | 57.748 $ | 2,32% | 7,92% | -18,06% |
| SOL | 74,16 $ | 75,94 $ | 87,66 $ | 60,41 $ | 2,87% | 11,12% | -13,66% |
| DOGE | 0.07206 $ | 0.07377 $ | 0.10653 $ | 0.06961 $ | 3,02% | -1,89% | -26,10% |

## Lettura dettagliata

### BTC

- Prezzo: **64.460 $**
- Score classico: **-2 / 12**
- Verdetto: **DEBOLE / NON CONFERMATO**
- Azione coerente: **RIDUCI RISCHIO / NO LONG A LEVA**
- Volatilità tecnica locale: **BASSO** — ATR14 2,32%; distanza supporto 2,21%; distanza resistenza 0,22%

Dettaglio:

- Trend: **-4** — prezzo sotto MA200 daily; breve termine sopra MA20/MA50; MA50 daily in discesa; MA200 daily in discesa; STAGE 4 / MARKDOWN
- Stage weekly: **STAGE 4 / MARKDOWN** — Prezzo sotto MA30 weekly con MA30 in discesa.
- Struttura: **+2** — MASSIMI E MINIMI CRESCENTI
- Momentum: **0** — RSI sano 51.2; RSI in peggioramento; MACD sopra signal; istogramma MACD in peggioramento
- Volume: **0** — OBV sotto media; CMF positivo 0.05; volume ratio 0.53
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **0** — ACCUMULO POSSIBILE / RANGE BASSO. Prezzo nella metà bassa del range, ma senza spring confermato.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 51.19 |
| MACD histogram | 88.17915 |
| CMF20 | 0.051 |
| Volume ratio 20 | 0.53 |
| MA20 | 64.247 $ |
| MA50 | 63.178 $ |
| MA100 | 69.778 $ |
| MA200 | 72.260 $ |
| Pendenza MA50 20g | -5,36% |
| Pendenza MA200 60g | -9,98% |
| Bollinger width | 6,72% |
| Bollinger position | 0.55 |

### SOL

- Prezzo: **75,08 $**
- Score classico: **-11 / 12**
- Verdetto: **RIBASSISTA / FRAGILE**
- Azione coerente: **NON INSEGUIRE / TAKE PROFIT SU SPIKE**
- Volatilità tecnica locale: **BASSO** — ATR14 2,87%; distanza supporto 1,25%; distanza resistenza 1,13%

Dettaglio:

- Trend: **-4** — prezzo sotto MA200 daily; MA200 daily in discesa; STAGE 4 / MARKDOWN
- Stage weekly: **STAGE 4 / MARKDOWN** — Prezzo sotto MA30 weekly con MA30 in discesa.
- Struttura: **-2** — MASSIMI E MINIMI DECRESCENTI
- Momentum: **-3** — RSI neutrale 46.7; RSI in peggioramento; MACD sotto signal; istogramma MACD in peggioramento
- Volume: **-2** — OBV sotto media; CMF negativo -0.08; volume ratio 0.48
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **0** — ACCUMULO POSSIBILE / RANGE BASSO. Prezzo nella metà bassa del range, ma senza spring confermato.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 46.70 |
| MACD histogram | -0.37973 |
| CMF20 | -0.076 |
| Volume ratio 20 | 0.48 |
| MA20 | 77,04 $ |
| MA50 | 73,69 $ |
| MA100 | 79,36 $ |
| MA200 | 88,35 $ |
| Pendenza MA50 20g | -2,15% |
| Pendenza MA200 60g | -16,95% |
| Bollinger width | 10,42% |
| Bollinger position | 0.25 |

### DOGE

- Prezzo: **0.07349 $**
- Score classico: **-2 / 12**
- Verdetto: **DEBOLE / NON CONFERMATO**
- Azione coerente: **NO LONG / SHORT SOLO DOPO SPIKE E REJECTION**
- Volatilità tecnica locale: **BASSO** — ATR14 3,02%; distanza supporto 1,82%; distanza resistenza 0,54%

Dettaglio:

- Trend: **-4** — prezzo sotto MA200 daily; MA50 daily in discesa; MA200 daily in discesa; STAGE 4 / MARKDOWN
- Stage weekly: **STAGE 4 / MARKDOWN** — Prezzo sotto MA30 weekly con MA30 in discesa.
- Struttura: **0** — COMPRESSIONE / TRIANGOLO POSSIBILE
- Momentum: **+1** — RSI neutrale 47.4; RSI in miglioramento; MACD sopra signal; istogramma MACD in peggioramento
- Volume: **0** — OBV sotto media; CMF neutrale -0.03; rialzo con volume sopra media
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **+1** — SPRING / TEST POSSIBILE. Ha bucato un minimo importante e ha recuperato: possibile spring, da confermare.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 47.36 |
| MACD histogram | 0.00031 |
| CMF20 | -0.028 |
| Volume ratio 20 | 1.36 |
| MA20 | 0.07282 $ |
| MA50 | 0.07760 $ |
| MA100 | 0.09019 $ |
| MA200 | 0.09711 $ |
| Pendenza MA50 20g | -12,10% |
| Pendenza MA200 60g | -16,32% |
| Bollinger width | 8,78% |
| Bollinger position | 0.59 |

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

Generato: 2026-07-26 05:14 UTC


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
| BTC | 64.460 $ | Doppio massimo | CANDIDATO | ribassista | n/a | 48.247 $ | n/a | 11,62% | Fib 23,6% TESTATO (0) @ 64.748 $ | NEL RANGE | 62.553 $ |
| SOL | 75,08 $ | Doppio minimo | MATURO | rialzista | 2026-07-01 | 91,46 $ | -5,53% | n/a | Fib 23,6% TESTATO (0) @ 74,40 $ | NEL RANGE | 73,40 $ |
| DOGE | 0.07349 $ | Triplo massimo | MATURO | ribassista | 2026-06-24 | 0.05847 $ | 23,46% | n/a | Fib 23,6% NON ATTIVO (0) @ 0.08213 $ | NEL RANGE | 0.07107 $ |

## BTC

![Classic visual BTC](classic_visual_BTC.png)

- Pattern principale: **Doppio massimo**
- Stato pattern: **CANDIDATO** (0)
- Famiglia: **ribassista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-06-15 -> 2026-07-21**
- Età formazione: **5 giorni**
- Breakout pattern: **n/a**
- Età breakout: **n/a**
- Neckline: **57.748 $**
- Target teorico: **48.247 $**
- Progresso verso target: **n/a**
- Distanza dalla neckline: **11,62%**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 23,6% TESTATO (0) @ 64.748 $** — Swing UP 2026-07-01 57.748 -> 2026-07-21 66.910; livello più vicino 23.6% a 64.748; stato TESTATO; confluenza: nessuna confluenza indipendente.
- Invalidazione: **58.903 $**
- Relazione prezzo/neckline: **sopra neckline**
- Dettaglio: Due massimi simili vicino a 67.248 tra 2026-06-15 e 2026-07-21. Neckline ribassista stimata: 57.748. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 5 giorni. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **NEL RANGE**
- Supporto: **62.553 $**
- Resistenza: **65.508 $**
- Breakout 60g: **77.991 $**
- Breakdown 60g: **57.748 $**
- RSI14: **51.21**
- ATR14: **2,32%**
- Volume ratio 20g: **0.53**
- Rendimento 30g: **+7,93%**
- Rendimento 90g: **-18,05%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Doppio massimo | CANDIDATO | 0 | ribassista | 57.748 $ | n/a | n/a | 48.247 $ | n/a | 11,62% | 58.903 $ | Due massimi simili a 67.248 $ e 66.910 $. Neckline circa 57.748 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 5 giorni. |
| Doppio minimo | CANDIDATO | 0 | rialzista | 67.248 $ | n/a | n/a | 76.748 $ | n/a | 4,33% | 65.903 $ | Due minimi simili a 59.109 $ e 57.748 $. Neckline circa 67.248 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 25 giorni. |

## SOL

![Classic visual SOL](classic_visual_SOL.png)

- Pattern principale: **Doppio minimo**
- Stato pattern: **MATURO** (+1)
- Famiglia: **rialzista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-06-06 -> 2026-06-25**
- Età formazione: **31 giorni**
- Breakout pattern: **2026-07-01**
- Età breakout: **25 giorni**
- Neckline: **75,94 $**
- Target teorico: **91,46 $**
- Progresso verso target: **-5,53%**
- Distanza dalla neckline: **n/a**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 23,6% TESTATO (0) @ 74,40 $** — Swing UP 2026-06-06 60,41 -> 2026-07-21 78,73; livello più vicino 23.6% a 74,40; stato TESTATO; confluenza: supporto tecnico, neckline rialzista, invalidazione rialzista.
- Invalidazione: **74,42 $**
- Relazione prezzo/neckline: **sotto neckline**
- Dettaglio: Due minimi simili vicino a 60,41 tra 2026-06-06 e 2026-06-25. Neckline stimata: 75,94. Breakout neckline: 2026-07-01 (25 giorni fa). Stato: MATURO. Target teorico: 91,46; progresso corrente: -5,53%. Relazione prezzo/neckline: sotto neckline. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **NEL RANGE**
- Supporto: **73,40 $**
- Resistenza: **75,94 $**
- Breakout 60g: **87,66 $**
- Breakdown 60g: **60,41 $**
- RSI14: **46.67**
- ATR14: **2,87%**
- Volume ratio 20g: **0.48**
- Rendimento 30g: **+11,11%**
- Rendimento 90g: **-13,67%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Doppio minimo | MATURO | +1 | rialzista | 75,94 $ | 2026-07-01 | 25g | 91,46 $ | -5,53% | n/a | 74,42 $ | Due minimi simili vicino a 60,41 tra 2026-06-06 e 2026-06-25. Neckline stimata: 75,94. Breakout neckline: 2026-07-01 (25 giorni fa). Stato: MATURO. Target teorico: 91,46; progresso corrente: -5,53%. Relazione prezzo/neckline: sotto neckline. Fonte lifecycle: technical_structure_metrics.csv. |
| Doppio massimo | CANDIDATO | 0 | ribassista | 64,42 $ | n/a | n/a | 50,11 $ | n/a | 16,55% | 65,71 $ | Due massimi simili a 75,94 $ e 78,73 $. Neckline circa 64,42 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 5 giorni. |
| Testa e spalle inverso | CANDIDATO | 0 | rialzista | 79,35 $ | n/a | n/a | 94,28 $ | n/a | 5,69% | 77,76 $ | Spalla sinistra 67,92 $, testa 64,42 $, spalla destra 73,40 $. Neckline circa 79,35 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 9 giorni. |
| Doppio minimo | CANDIDATO | 0 | rialzista | 98,27 $ | n/a | n/a | 114,91 $ | n/a | 30,88% | 96,30 $ | Due minimi simili a 81,63 $ e 81,69 $. Neckline circa 98,27 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 64 giorni. |
| Testa e spalle | TARGET RAGGIUNTO | 0 | ribassista | 82,57 $ | 2026-05-28 | 59g | 66,88 $ | 47,74% | n/a | 84,22 $ | Spalla sinistra 88,05 $, testa 98,27 $, spalla destra 87,79 $. Neckline circa 82,57 $. Breakout neckline: 2026-05-28 (59 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 66,88 $; progresso: 47,74%; prezzo sotto neckline. |

## DOGE

![Classic visual DOGE](classic_visual_DOGE.png)

- Pattern principale: **Triplo massimo**
- Stato pattern: **MATURO** (-1)
- Famiglia: **ribassista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-03-25 -> 2026-06-12**
- Età formazione: **44 giorni**
- Breakout pattern: **2026-06-24**
- Età breakout: **32 giorni**
- Neckline: **0.07809 $**
- Target teorico: **0.05847 $**
- Progresso verso target: **23,46%**
- Distanza dalla neckline: **n/a**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 23,6% NON ATTIVO (0) @ 0.08213 $** — Swing DOWN 2026-05-14 0.11825 -> 2026-07-13 0.07097; livello più vicino 23.6% a 0.08213; stato NON ATTIVO; confluenza: nessuna confluenza indipendente.
- Invalidazione: **0.07966 $**
- Relazione prezzo/neckline: **sotto neckline**
- Dettaglio: Tre massimi simili vicino a 0.09772 dal 2026-03-25 al 2026-06-12. Neckline ribassista stimata: 0.07809. Breakout neckline: 2026-06-24 (32 giorni fa). Stato: MATURO. Target teorico: 0.05847; progresso corrente: 23,46%. Relazione prezzo/neckline: sotto neckline. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **NEL RANGE**
- Supporto: **0.07107 $**
- Resistenza: **0.07923 $**
- Breakout 60g: **0.10653 $**
- Breakdown 60g: **0.06961 $**
- RSI14: **47.70**
- ATR14: **3,04%**
- Volume ratio 20g: **1.36**
- Rendimento 30g: **-1,73%**
- Rendimento 90g: **-25,98%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Triplo massimo | MATURO | -1 | ribassista | 0.07809 $ | 2026-06-24 | 32g | 0.05847 $ | 23,46% | n/a | 0.07966 $ | Tre massimi simili vicino a 0.09772 dal 2026-03-25 al 2026-06-12. Neckline ribassista stimata: 0.07809. Breakout neckline: 2026-06-24 (32 giorni fa). Stato: MATURO. Target teorico: 0.05847; progresso corrente: 23,46%. Relazione prezzo/neckline: sotto neckline. Fonte lifecycle: technical_structure_metrics.csv. |
| Doppio massimo | MATURO | -1 | ribassista | 0.07809 $ | 2026-06-24 | 32g | 0.06035 $ | 25,96% | n/a | 0.07966 $ | Due massimi simili a 0.09584 $ e 0.09169 $. Neckline circa 0.07809 $. Breakout neckline: 2026-06-24 (32 giorni fa). Stato: MATURO. Target teorico: 0.06035 $; progresso: 25,96%; prezzo sotto neckline. |
| Doppio minimo | CANDIDATO | 0 | rialzista | 0.07923 $ | n/a | n/a | 0.08886 $ | n/a | 7,82% | 0.07765 $ | Due minimi simili a 0.06961 $ e 0.07097 $. Neckline circa 0.07923 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 13 giorni. |
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

Generato: 2026-07-26 05:14 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [fractal_path_tracker.md](fractal_path_tracker.md)

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-07-26**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-01-10**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **75,08 $**
- Verdetto principale: **ANALOGIA DEBOLE / SCENARIO SECONDARIO**
- Somiglianza strutturale: **+64,17%**
- Aderenza live principale: **+65,93%**
- Errore medio live principale: **17,03%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE SOLO DI CONTESTO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **50**
- Osservazioni inclusive dal bottom: **51**
- Osservazioni da inizio programma/scanner: **24**
- Errore assoluto medio dal bottom: **11,21%**
- Errore assoluto medio da inizio programma: **17,03%**
- Gap firmato medio ultimi 7 giorni: **+13,31%**
- Errore assoluto medio ultimi 7 giorni: **13,31%**
- Gap ultimo giorno: **+9,25%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **+9,25%**
- Gap firmato medio 7g: **+13,31%**
- Errore assoluto medio 7g: **13,31%**
- Variazione recente gap: **-4,33%**
- Stato gap: **SOPRA IL FRATTALE**
- Trend gap: **SOL resta sopra il percorso ancorato, ma sta riducendo il distacco**

Soglie operative del grafico:

- entro **±5%**: percorso vicino;
- tra **±5% e ±12%**: deviazione gestibile;
- oltre **±12%**: frattale non abbastanza aderente per conferma operativa;
- oltre **±18%**: disallineamento marcato.

## Ultimi giorni del confronto ancorato

|   Giorno | Data SOL   | Data BTC eq.   | SOL reale   | Percorso ancorato   | Gap firmato   | Fase                |
|---------:|:-----------|:---------------|:------------|:--------------------|:--------------|:--------------------|
| 41 | 2026-07-17 | 2023-01-01 | 75,01 $ | 65,49 $ | +14,54% | da inizio programma |
| 42 | 2026-07-18 | 2023-01-02 | 75,46 $ | 65,74 $ | +14,79% | da inizio programma |
| 43 | 2026-07-19 | 2023-01-03 | 76,36 $ | 65,71 $ | +16,21% | da inizio programma |
| 44 | 2026-07-20 | 2023-01-04 | 77,79 $ | 66,43 $ | +17,11% | da inizio programma |
| 45 | 2026-07-21 | 2023-01-05 | 78,11 $ | 66,32 $ | +17,77% | da inizio programma |
| 46 | 2026-07-22 | 2023-01-06 | 77,91 $ | 66,78 $ | +16,66% | da inizio programma |
| 47 | 2026-07-23 | 2023-01-07 | 75,86 $ | 66,79 $ | +13,58% | da inizio programma |
| 48 | 2026-07-24 | 2023-01-08 | 73,88 $ | 67,33 $ | +9,73% | da inizio programma |
| 49 | 2026-07-25 | 2023-01-09 | 73,88 $ | 67,74 $ | +9,06% | da inizio programma |
| 50 | 2026-07-26 | 2023-01-10 | 75,08 $ | 68,73 $ | +9,25% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-08-02 | 83,36 $ | 91,07 $ | 75,08 $ / 91,10 $ | no | n/a | n/a | n/a |
| 14g | 2026-08-09 | 89,17 $ | 97,42 $ | 75,08 $ / 98,70 $ | no | n/a | n/a | n/a |
| 21g | 2026-08-16 | 91,15 $ | 99,58 $ | 75,08 $ / 102,31 $ | no | n/a | n/a | n/a |
| 28g | 2026-08-23 | 91,64 $ | 100,12 $ | 75,08 $ / 102,31 $ | no | n/a | n/a | n/a |
| 35g | 2026-08-30 | 87,53 $ | 95,63 $ | 75,08 $ / 102,31 $ | no | n/a | n/a | n/a |
| 42g | 2026-09-06 | 96,26 $ | 105,16 $ | 75,08 $ / 106,85 $ | no | n/a | n/a | n/a |
| 49g | 2026-09-13 | 91,18 $ | 99,61 $ | 75,08 $ / 106,85 $ | no | n/a | n/a | n/a |
| 56g | 2026-09-20 | 87,53 $ | 95,62 $ | 75,08 $ / 106,85 $ | no | n/a | n/a | n/a |
| 63g | 2026-09-27 | 97,48 $ | 106,49 $ | 75,08 $ / 106,85 $ | no | n/a | n/a | n/a |
| 70g | 2026-10-04 | 110,99 $ | 121,25 $ | 75,08 $ / 121,25 $ | no | n/a | n/a | n/a |
| 77g | 2026-10-11 | 107,42 $ | 117,35 $ | 75,08 $ / 121,94 $ | no | n/a | n/a | n/a |
| 84g | 2026-10-18 | 110,96 $ | 121,22 $ | 75,08 $ / 122,56 $ | no | n/a | n/a | n/a |
| 91g | 2026-10-25 | 119,10 $ | 130,12 $ | 75,08 $ / 130,12 $ | no | n/a | n/a | n/a |
| 98g | 2026-11-01 | 119,74 $ | 130,82 $ | 75,08 $ / 131,19 $ | no | n/a | n/a | n/a |
| 105g | 2026-11-08 | 111,51 $ | 121,82 $ | 75,08 $ / 131,19 $ | no | n/a | n/a | n/a |
| 112g | 2026-11-15 | 112,98 $ | 123,43 $ | 75,08 $ / 131,19 $ | no | n/a | n/a | n/a |
| 119g | 2026-11-22 | 108,95 $ | 119,03 $ | 75,08 $ / 131,19 $ | no | n/a | n/a | n/a |
| 126g | 2026-11-29 | 106,50 $ | 116,35 $ | 75,08 $ / 131,19 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 12 | 25,00% | 2,34% | 13,87% |
| 14g | 5 | 0,00% | 5,20% | 9,35% |
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

Ultima lettura salvata: **2026-07-26** — SOL 75,08 $, gap +9,25%, somiglianza +64,17%.

Nel report principale lascio solo il link, così non diventa troppo lungo.

<!-- SOL_BTC_FRACTAL_HISTORY_END -->

</details>
<!-- COMPACT_SECTION_END:fractal_path -->

<!-- COMPACT_SECTION_START:exchange_microstructure -->
<details>
<summary><strong>🏦 Dati exchange, liquidità e leva</strong></summary>

<!-- EXCHANGE_MICROSTRUCTURE_START -->
# Dati exchange, liquidità e leva

Generato: 2026-07-26 05:14 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [exchange_microstructure_report.md](exchange_microstructure_report.md)

Questo modulo legge Kraken Futures, Bitget Futures e KuCoin Futures come nucleo derivati. OKX e Coinbase vengono raccolti come fonti ausiliarie non pesate.
Non modifica la formula matematica di RSI, Fibonacci o Wyckoff: controlla se quei segnali sono sostenuti da acquisti, vendite, OI, funding e liquidità.

**Limite importante:** questo nucleo non assume disponibile un feed pubblico completo delle liquidazioni. La componente liquidazioni resta neutrale; le zone future restano stime di pressione, non dati certi delle singole posizioni.

Diagnostica completa: [exchange_source_diagnostics.md](exchange_source_diagnostics.md)

## Sintesi

| Asset | Prezzo | Exchange | Segnale candidato | Peso Global | Bias exchange | Confidenza | Copertura | Funding 8h eq. | OI 24h | Taker flow (campione/4h) | Book 0,5% | Liq long campione | Liq short campione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 64.469 $ | 3 | 0 | 0 | MISTA / NEUTRALE | BASSA | 100% | +0,0041% | -0,46% | 0,80 | +7,17% | 0 $ | 0 $ |
| SOL | 75,00 $ | 3 | 0 | 0 | LEGGERMENTE POSITIVA / NON PESATA | MEDIA | 100% | +0,0018% | +0,37% | 2,52 | +5,87% | 0 $ | 0 $ |
| DOGE | 0.07319 $ | 3 | 0 | 0 | LEGGERMENTE POSITIVA / NON PESATA | MEDIA | 100% | +0,0050% | -5,19% | 1,35 | -2,50% | 0 $ | 0 $ |

Il segnale candidato è limitato a **±1**, ma il peso nel Global resta **0** finché il tracker a 7 giorni non raggiunge 30 controlli, almeno 55% di accuratezza e return corretto direzione positivo. Un singolo muro o funding non basta.

La colonna taker usa un campione recente nel primo run. Dopo almeno 3 fotografie distribuite su almeno 45 minuti viene sostituita automaticamente dalla media intraday 4h.

## Dati separati per exchange

| Asset | Exchange | Stato | Funding 8h eq. | Open interest | Taker flow | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | Kraken | OK | +0,0109% | 136,45 mln $ | 0,34 | -1,68% |
| BTC | Bitget | OK | -0,0018% | 2,32 mld $ | 0,30 | +50,28% |
| BTC | Kucoin | OK | +0,0044% | 1,62 mld $ | 0,10 | +19,73% |
| SOL | Kraken | OK | +0,0251% | 15,31 mln $ | 0,65 | +5,62% |
| SOL | Bitget | OK | +0,0042% | 361,19 mln $ | 0,22 | +5,41% |
| SOL | Kucoin | OK | +0,0088% | 316,53 mln $ | 1,51 | +5,86% |
| DOGE | Kraken | OK | +0,0119% | 4,33 mln $ | 0,88 | -29,97% |
| DOGE | Bitget | OK | +0,0100% | 100,45 mln $ | 0,67 | -2,25% |
| DOGE | Kucoin | OK | -0,0068% | 92,70 mln $ | 0,45 | -34,90% |

Kraken, Bitget e KuCoin contribuiscono a funding normalizzato, open interest, trade aggressivi e order book. Non viene inventato un long/short ratio pubblico né un feed completo delle liquidazioni.

## Conferme per indicatori tecnici

### BTC

- Score grezzo exchange: **-0,25**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 0, accuratezza n/a.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 1, bear 1, divergenze 0.
- Flusso taker/order book: **-0,25**.
- OI/funding/basis: **+0,00**.
- Affollamento long/short: **+0,00**.
- Liquidazioni: **NON PESATE / FEED COMPLETO NON ASSUNTO DISPONIBILE**.
- **Wyckoff:** Possibile accumulazione ancora neutrale nei dati exchange.
- **Fibonacci:** Livello Fibonacci soltanto testato: order book e taker flow non bastano ancora per dichiararlo tenuto o perso.
- **RSI:** RSI in zona non estrema o flusso exchange non abbastanza netto.
- **Pattern:** I pattern candidati restano non operativi: i dati exchange possono solo preparare la conferma.
- **Breakout/breakdown:** Prezzo non abbastanza vicino a un livello chiave o flusso non netto.
- **Mappa liquidità attuale:** muro bid: n/a; muro ask: n/a

![Microstruttura exchange BTC](exchange_microstructure_BTC.png)

### SOL

- Score grezzo exchange: **+2,25**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 0, accuratezza n/a.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 1, bear 1, divergenze 0.
- Flusso taker/order book: **+1,75**.
- OI/funding/basis: **+0,00**.
- Affollamento long/short: **+0,00**.
- Liquidazioni: **NON PESATE / FEED COMPLETO NON ASSUNTO DISPONIBILE**.
- **Wyckoff:** Markdown non pienamente confermato: compare assorbimento compratore.
- **Fibonacci:** Livello Fibonacci soltanto testato: order book e taker flow non bastano ancora per dichiararlo tenuto o perso. Confluenza tecnica dichiarata: supporto tecnico, neckline rialzista, invalidazione rialzista.
- **RSI:** RSI in zona non estrema o flusso exchange non abbastanza netto.
- **Pattern:** Doppio minimo maturo sostenuto dal flusso exchange.
- **Breakout/breakdown:** Prezzo non abbastanza vicino a un livello chiave o flusso non netto.
- **Mappa liquidità attuale:** muro bid: n/a; muro ask: n/a

![Microstruttura exchange SOL](exchange_microstructure_SOL.png)

### DOGE

- Score grezzo exchange: **+1,62**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 0, accuratezza n/a.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 0, bear 3, divergenze 0.
- Flusso taker/order book: **+1,75**.
- OI/funding/basis: **-0,50**.
- Affollamento long/short: **+0,00**.
- Liquidazioni: **NON PESATE / FEED COMPLETO NON ASSUNTO DISPONIBILE**.
- **Wyckoff:** Possibile accumulazione/spring sostenuto da pressione compratrice o assorbimento.
- **Fibonacci:** Fibonacci non_attivo; nessuna conferma exchange netta.
- **RSI:** RSI in zona non estrema o flusso exchange non abbastanza netto.
- **Pattern:** I pattern candidati restano non operativi: i dati exchange possono solo preparare la conferma.
- **Breakout/breakdown:** Prezzo non abbastanza vicino a un livello chiave o flusso non netto.
- **Mappa liquidità attuale:** muro bid: n/a; muro ask: n/a

![Microstruttura exchange DOGE](exchange_microstructure_DOGE.png)

## Overlay sulle previsioni a 30 giorni

La previsione storica grezza dello scanner resta intatta. L'overlay exchange può correggerla solo dopo almeno 30 controlli maturati a 30 giorni e solo se il modulo dimostra accuratezza direzionale almeno del 55%.

| Asset | Prob. grezza salita | Return p50 grezzo | Controlli 30g | Accuratezza exchange | Stato overlay | Peso | Prob. corretta | Return corretto |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +65,00% | +9,80% | 0 | n/a | RACCOLTA DATI | 0,00 | +65,00% | +9,80% |
| SOL | +70,00% | +5,22% | 0 | n/a | RACCOLTA DATI | 0,00 | +70,00% | +5,22% |
| DOGE | +62,50% | +4,13% | 0 | n/a | RACCOLTA DATI | 0,00 | +62,50% | +4,13% |

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

Generato: 2026-07-26 05:14 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [exchange_signal_tracker_report.md](exchange_signal_tracker_report.md)

Questo tracker verifica se il segnale candidato exchange ±1 anticipa correttamente la direzione del prezzo a 1/3/7/14/30 giorni.
Il peso Global resta 0 finché l'orizzonte 7g non ha almeno 30 controlli, accuratezza almeno 55% e return corretto direzione positivo. L'overlay a 30g ha un gate separato.

Controlli maturati completati in questa esecuzione: **12**.

## Ultime fotografie giornaliere

| Data | Asset | Prezzo | Versione | Calibrazione | Candidato | Peso Global | Score raw | Confidenza | Taker 4h | OI 24h | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-07-26 | BTC | 64.469,20 | V2.1.3 | OK | 0 | 0 | -0,25 | BASSA | 0,80 | -0,46% | +7,17% |
| 2026-07-26 | DOGE | 0.07319 | V2.1.3 | OK | 0 | 0 | 1,62 | MEDIA | 1,35 | -5,19% | -2,50% |
| 2026-07-26 | SOL | 75,00 | V2.1.3 | OK | 0 | 0 | 2,25 | MEDIA | 2,52 | +0,37% | +5,87% |
| 2026-07-25 | BTC | 64.136,30 | V2.1.3 | OK | 0 | 0 | 2,38 | MEDIA | 5,64 | -0,67% | +4,43% |
| 2026-07-25 | DOGE | 0.06962 | V2.1.3 | OK | 1 | 0 | 2,50 | MEDIA | 1,43 | +8,66% | -4,98% |
| 2026-07-25 | SOL | 74,25 | V2.1.3 | OK | 0 | 0 | 0,75 | BASSA | 0,96 | -3,26% | +0,17% |
| 2026-07-24 | BTC | 65.326,60 | V2.1.3 | OK | 0 | 0 | 2,25 | MEDIA | 3,29 | -1,87% | +3,07% |
| 2026-07-24 | DOGE | 0.06905 | V2.1.3 | OK | 1 | 0 | 2,88 | MEDIA | 1,88 | -10,42% | -7,48% |
| 2026-07-24 | SOL | 75,75 | V2.1.3 | OK | 0 | 0 | 0,38 | MEDIA | 7,39 | +14,43% | +2,17% |

## Accuratezza direzionale

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 1 | +100,00% | +1,59% | +1,07% | +1,84% | FEEDBACK RAPIDO |
| BTC | 3g | 1 | +100,00% | +1,47% | -1,13% | +3,82% | FEEDBACK RAPIDO |
| BTC | 7g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 14g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 30g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 1g | 1 | +0,00% | -0,43% | -0,39% | +0,39% | FEEDBACK RAPIDO |
| SOL | 3g | 1 | +0,00% | -3,12% | -3,63% | +0,73% | FEEDBACK RAPIDO |
| SOL | 7g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 14g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 30g | 0 | n/a | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 1g | 2 | +100,00% | +3,08% | +1,70% | +3,12% | FEEDBACK RAPIDO |
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
| BTC | 64.460 $ | -0.0013% | +1.36% | 1.82 | Misto | 1/5 |
| SOL | 75,08 $ | +0.0042% | -14.97% | 2.33 | Misto | 1/5 |
| DOGE | 0.07349 $ | +0.0076% | -29.39% | 3.81 | Misto | 1/5 |

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

Generato: 2026-07-26 05:14 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [rsi_multitimeframe_divergence_report.md](rsi_multitimeframe_divergence_report.md)

Il modulo confronta prezzo e RSI 14 sui pivot confermati **daily e weekly**. Riconosce divergenze regolari e nascoste, segnali in formazione, invalidazioni e semplice conferma del momentum.

**Peso operativo: 0.** Non modifica il Global Confluence, non cambia le soglie del Paper Trading e non apre né blocca operazioni. I risultati vengono misurati prima di qualsiasi futura decisione sul peso.

## Sintesi corrente

| Asset   | Daily                     | Stato D    | Weekly              | Stato W    | Lettura weekly                                                                                                                |   Peso |
|:--------|:--------------------------|:-----------|:--------------------|:-----------|:------------------------------------------------------------------------------------------------------------------------------|-------:|
| BTC     | Bullish regolare          | CONFERMATA | Bullish regolare    | CONFERMATA | Bullish regolare confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto. |      0 |
| SOL     | Hidden bullish invalidata | INVALIDATA | Hidden bearish      | CONFERMATA | Hidden bearish confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto.   |      0 |
| DOGE    | Hidden bearish            | CONFERMATA | Conferma ribassista | CONTESTO   | Prezzo e RSI stanno scendendo insieme: momentum ribassista confermato, nessuna bullish divergence attiva.                     |      0 |

## Dettaglio dei pivot

| Asset   | TF   | Tipo                      | Stato      | Prezzo / RSI      | Pivot confrontati                                                   | Δ prezzo contesto   | Δ RSI contesto   |   Peso |
|:--------|:-----|:--------------------------|:-----------|:------------------|:--------------------------------------------------------------------|:--------------------|:-----------------|-------:|
| BTC     | 1D   | Bullish regolare          | CONFERMATA | 64.454 $ / 51,19  | 2026-06-25 58.076 $ / RSI 30,46 → 2026-07-01 57.748 $ / RSI 37,26   | n/a                 | n/a              |      0 |
| BTC     | 1W   | Bullish regolare          | CONFERMATA | 64.454 $ / 39,52  | 2026-06-07 59.109 $ / RSI 34,23 → 2026-07-05 57.748 $ / RSI 38,20   | n/a                 | n/a              |      0 |
| SOL     | 1D   | Hidden bullish invalidata | INVALIDATA | 75,09 $ / 46,70   | n/a                                                                 | -2,26%              | -4,70            |      0 |
| SOL     | 1W   | Hidden bearish            | CONFERMATA | 75,09 $ / 39,20   | 2026-05-17 98,27 $ / RSI 38,29 → 2026-07-05 83,81 $ / RSI 42,25     | n/a                 | n/a              |      0 |
| DOGE    | 1D   | Hidden bearish            | CONFERMATA | 0.07336 $ / 47,33 | 2026-06-12 0.09169 $ / RSI 35,18 → 2026-07-04 0.07923 $ / RSI 41,65 | n/a                 | n/a              |      0 |
| DOGE    | 1W   | Conferma ribassista       | CONTESTO   | 0.07336 $ / 34,05 | n/a                                                                 | -17,36%             | -3,34            |      0 |

### BTC

- **1D — Bullish regolare / CONFERMATA**: Bullish regolare confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto.
- **1W — Bullish regolare / CONFERMATA**: Bullish regolare confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto.

### SOL

- **1D — Hidden bullish invalidata / INVALIDATA**: La precedente hidden bullish non è più sostenuta dalla relazione corrente tra pivot di prezzo e RSI.
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

Generato: 2026-07-26 05:14 UTC


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

| Asset   | Prezzo   |   Punteggio | Verdetto           | Trend            | Momentum        | Struttura                                             |   Pattern score | Fibonacci      | Pattern rialzista         | Pattern ribassista         | Supporto   | Resistenza   |
|:--------|:---------|------------:|:-------------------|:-----------------|:----------------|:------------------------------------------------------|----------------:|:---------------|:--------------------------|:---------------------------|:-----------|:-------------|
| BTC | 64.460 $ | 1 | NEUTRALE / MISTO | Trend misto | Momentum misto | Volatilità in espansione | 0 | 0 / TESTATO | Doppio minimo / CANDIDATO | Doppio massimo / CANDIDATO | 57.748 | 66.910 |
| SOL | 75,08 $ | -10 | RIBASSISTA TECNICO | Trend ribassista | Momentum debole | Compressione / triangolo | +1 | 0 / TESTATO | Doppio minimo / MATURO | Doppio massimo / CANDIDATO | 73,40 | 78,73 |
| DOGE | 0.07349 $ | -5 | DEBOLE | Trend ribassista | Momentum misto | Struttura ribassista con massimi e minimi decrescenti | -1 | 0 / NON ATTIVO | Doppio minimo / CANDIDATO | Triplo massimo / MATURO | 0.07097 | 0.07923 |

## Riepilogo ciclo di vita pattern

| Asset   | Doppio minimo   | Triplo minimo   | Adam/Eve Bottom                 | Doppio massimo   | Triplo massimo   | Adam/Eve Top                 |   Punteggio pattern |
|:--------|:----------------|:----------------|:--------------------------------|:-----------------|:-----------------|:-----------------------------|--------------------:|
| BTC | CANDIDATO | CANDIDATO | Adam and Eve Bottom — CANDIDATO | CANDIDATO | CANDIDATO | Adam and Eve Top — CANDIDATO | 0 |
| SOL | MATURO | CANDIDATO | Adam and Eve Bottom — CANDIDATO | CANDIDATO | CANDIDATO | Adam and Eve Top — CANDIDATO | 1 |
| DOGE | CANDIDATO | ASSENTE | Adam and Eve Bottom — CANDIDATO | ASSENTE | MATURO | Eve and Adam Top — MATURO | -1 |

## Indicatori tecnici

| Asset   |   RSI 14 |   Istogramma MACD | MA20    | MA50    | MA200   | Pendenza MA50 20g   | Pendenza MA200 60g   | Rendimento 30g   | Rendimento 90g   |
|:--------|---------:|------------------:|:--------|:--------|:--------|:--------------------|:---------------------|:-----------------|:-----------------|
| BTC | 51.21 | 88.5309 | 64.248 | 63.178 | 72.260 | -4,97% | -9,82% | 7,40% | -16,68% |
| SOL | 46.67 | -0.38037 | 77,04 | 73,69 | 88,35 | -2,07% | -16,65% | 4,52% | -11,48% |
| DOGE | 47.7 | 0.00031 | 0.07282 | 0.07761 | 0.09711 | -11,45% | -16,04% | -2,87% | -25,75% |

## Dettaglio asset

### BTC

- Prezzo: **64.460 $**
- Punteggio tecnico: **1 / 12**
- Verdetto: **NEUTRALE / MISTO**
- Trend: **Trend misto** (-1)
- Momentum: **Momentum misto** (-1)
- Volume: **Volume neutrale** (0)
- Struttura: **Volatilità in espansione** (0)
  - Dettaglio struttura: Ultimi minimi: 5.808e+04 -> 5.775e+04. Ultimi massimi: 6.551e+04 -> 6.691e+04.
- Divergenza: **Divergenza rialzista RSI** (2)
- Fase Wyckoff candidata: **Possibile accumulazione** (1)
  - Dettaglio Wyckoff: Prezzo sotto MA200, vicino alla parte bassa del range a 120 giorni, RSI 51.2.
- Fibonacci automatico: **TESTATO** (0)
  - Swing UP 2026-07-01 57.748 -> 2026-07-21 66.910; livello più vicino 23.6% a 64.748; stato TESTATO; confluenza: nessuna confluenza indipendente.
- Punteggio pattern: **0**
  - rialzista dominante: Doppio minimo (CANDIDATO, 0); ribassista dominante: Doppio massimo (CANDIDATO, 0).
- Supporto più vicino: **57.748**
- Resistenza più vicina: **66.910**

Pattern classici e ciclo di vita:

- Doppio minimo: **CANDIDATO** (0)
  - Due minimi simili vicino a 57.748 tra 2026-06-05 e 2026-07-01. Neckline stimata: 67.248. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 25 giorni.
  - neckline 67.248; target 76.748; distanza dalla neckline 4,33%; prezzo sotto neckline.
- Triplo minimo: **CANDIDATO** (0)
  - Tre minimi simili vicino a 57.748 dal 2026-06-05 al 2026-07-01. Neckline stimata: 67.248. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 25 giorni.
  - neckline 67.248; target 76.748; distanza dalla neckline 4,33%; prezzo sotto neckline.
- Adam and Eve Bottom: **CANDIDATO** (0)
  - Pattern Adam and Eve Bottom vicino a 57.748 dal 2026-06-05 al 2026-07-01. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 67.248. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 25 giorni.
  - neckline 67.248; target 76.748; distanza dalla neckline 4,33%; prezzo sotto neckline.
- Doppio massimo: **CANDIDATO** (0)
  - Due massimi simili vicino a 67.248 tra 2026-06-15 e 2026-07-21. Neckline ribassista stimata: 57.748. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 5 giorni.
  - neckline 57.748; target 48.247; distanza dalla neckline 11,62%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 66.910 dal 2026-06-22 al 2026-07-21. Neckline ribassista stimata: 57.748. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 5 giorni.
  - neckline 57.748; target 48.585; distanza dalla neckline 11,62%; prezzo sopra neckline.
- Adam and Eve Top: **CANDIDATO** (0)
  - Pattern Adam and Eve Top vicino a 67.248 dal 2026-06-15 al 2026-07-21. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 57.748. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 5 giorni.
  - neckline 57.748; target 48.247; distanza dalla neckline 11,62%; prezzo sopra neckline.

### SOL

- Prezzo: **75,08 $**
- Punteggio tecnico: **-10 / 12**
- Verdetto: **RIBASSISTA TECNICO**
- Trend: **Trend ribassista** (-3)
- Momentum: **Momentum debole** (-3)
- Volume: **Volume da distribuzione** (-2)
- Struttura: **Compressione / triangolo** (0)
  - Dettaglio struttura: Ultimi minimi: 64.42 -> 73.4. Ultimi massimi: 78.88 -> 78.73.
- Divergenza: **Divergenza ribassista nascosta RSI** (-1)
- Fase Wyckoff candidata: **Markdown / fase ribassista** (-2)
  - Dettaglio Wyckoff: Prezzo sotto MA200 con trend a 90 giorni ancora debole.
- Fibonacci automatico: **TESTATO** (0)
  - Swing UP 2026-06-06 60,41 -> 2026-07-21 78,73; livello più vicino 23.6% a 74,40; stato TESTATO; confluenza: supporto tecnico, neckline rialzista, invalidazione rialzista.
- Punteggio pattern: **+1**
  - rialzista dominante: Doppio minimo (MATURO, +1); ribassista dominante: Doppio massimo (CANDIDATO, 0).
- Supporto più vicino: **73,40**
- Resistenza più vicina: **78,73**

Pattern classici e ciclo di vita:

- Doppio minimo: **MATURO** (+1)
  - Due minimi simili vicino a 60,41 tra 2026-06-06 e 2026-06-25. Neckline stimata: 75,94. Breakout neckline: 2026-07-01 (25 giorni fa). Stato: MATURO. Target teorico: 91,46; progresso corrente: -5,53%. Relazione prezzo/neckline: sotto neckline.
  - neckline 75,94; target 91,46; breakout 2026-07-01 (25g); progresso -5,53%; prezzo sotto neckline.
- Triplo minimo: **CANDIDATO** (0)
  - Tre minimi simili vicino a 81,63 dal 2026-04-29 al 2026-05-23. Neckline stimata: 98,27. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 64 giorni.
  - neckline 98,27; target 114,91; distanza dalla neckline 30,88%; prezzo sotto neckline.
- Adam and Eve Bottom: **CANDIDATO** (0)
  - Pattern Adam and Eve Bottom vicino a 67,92 dal 2026-06-19 al 2026-07-17. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 83,81. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 9 giorni.
  - neckline 83,81; target 99,70; distanza dalla neckline 11,63%; prezzo sotto neckline.
- Doppio massimo: **CANDIDATO** (0)
  - Due massimi simili vicino a 78,73 tra 2026-06-15 e 2026-07-21. Neckline ribassista stimata: 64,42. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 5 giorni.
  - neckline 64,42; target 50,11; distanza dalla neckline 16,55%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 78,88 dal 2026-06-15 al 2026-07-21. Neckline ribassista stimata: 64,42. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 5 giorni.
  - neckline 64,42; target 49,96; distanza dalla neckline 16,55%; prezzo sopra neckline.
- Adam and Eve Top: **CANDIDATO** (0)
  - Pattern Adam and Eve Top vicino a 78,73 dal 2026-06-15 al 2026-07-21. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 64,42. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 5 giorni.
  - neckline 64,42; target 50,11; distanza dalla neckline 16,55%; prezzo sopra neckline.

### DOGE

- Prezzo: **0.07349 $**
- Punteggio tecnico: **-5 / 12**
- Verdetto: **DEBOLE**
- Trend: **Trend ribassista** (-3)
- Momentum: **Momentum misto** (1)
- Volume: **Volume neutrale** (0)
- Struttura: **Struttura ribassista con massimi e minimi decrescenti** (-2)
  - Dettaglio struttura: Ultimi minimi: 0.07107 -> 0.07097. Ultimi massimi: 0.09169 -> 0.07923.
- Divergenza: **Divergenza ribassista nascosta RSI** (-1)
- Fase Wyckoff candidata: **Possibile accumulazione** (1)
  - Dettaglio Wyckoff: Prezzo sotto MA200, vicino alla parte bassa del range a 120 giorni, RSI 47.7.
- Fibonacci automatico: **NON ATTIVO** (0)
  - Swing DOWN 2026-05-14 0.11825 -> 2026-07-13 0.07097; livello più vicino 23.6% a 0.08213; stato NON ATTIVO; confluenza: nessuna confluenza indipendente.
- Punteggio pattern: **-1**
  - rialzista dominante: Doppio minimo (CANDIDATO, 0); ribassista dominante: Triplo massimo (MATURO, -1).
- Supporto più vicino: **0.07097**
- Resistenza più vicina: **0.07923**

Pattern classici e ciclo di vita:

- Doppio minimo: **CANDIDATO** (0)
  - Due minimi simili vicino a 0.06961 tra 2026-06-30 e 2026-07-13. Neckline stimata: 0.07923. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 13 giorni.
  - neckline 0.07923; target 0.08886; distanza dalla neckline 7,82%; prezzo sotto neckline.
- Triplo minimo: **ASSENTE** (0)
- Adam and Eve Bottom: **CANDIDATO** (0)
  - Pattern Adam and Eve Bottom vicino a 0.06961 dal 2026-06-30 al 2026-07-13. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 0.07923. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 13 giorni.
  - neckline 0.07923; target 0.08886; distanza dalla neckline 7,82%; prezzo sotto neckline.
- Doppio massimo: **ASSENTE** (0)
- Triplo massimo: **MATURO** (-1)
  - Tre massimi simili vicino a 0.09772 dal 2026-03-25 al 2026-06-12. Neckline ribassista stimata: 0.07809. Breakout neckline: 2026-06-24 (32 giorni fa). Stato: MATURO. Target teorico: 0.05847; progresso corrente: 23,46%. Relazione prezzo/neckline: sotto neckline.
  - neckline 0.07809; target 0.05847; breakout 2026-06-24 (32g); progresso 23,46%; prezzo sotto neckline.
- Eve and Adam Top: **MATURO** (-1)
  - Pattern Eve and Adam Top vicino a 0.09584 dal 2026-04-07 al 2026-06-12. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 0.07809. Breakout neckline: 2026-06-24 (32 giorni fa). Stato: MATURO. Target teorico: 0.06035; progresso corrente: 25,96%. Relazione prezzo/neckline: sotto neckline.
  - neckline 0.07809; target 0.06035; breakout 2026-06-24 (32g); progresso 25,96%; prezzo sotto neckline.

## Fibonacci automatico

Il modulo seleziona uno swing recente tramite pivot confermati. Un semplice tocco vale 0: Fibonacci pesa al massimo ±1 soltanto quando il livello è tenuto, perso, recuperato o respinto e coincide con almeno un livello tecnico indipendente.

| Asset   | Swing                         | 23,6%   | 38,2%   | 50,0%   | 61,8%   | 78,6%   | Livello vicino   | Stato      | Confluenza                                                    |   Score |
|:--------|:------------------------------|:--------|:--------|:--------|:--------|:--------|:-----------------|:-----------|:--------------------------------------------------------------|--------:|
| BTC | UP 2026-07-01 -> 2026-07-21 | 64.748 | 63.410 | 62.329 | 61.248 | 59.708 | 23.6% / 64.748 | TESTATO | nessuna confluenza indipendente | 0 |
| SOL | UP 2026-06-06 -> 2026-07-21 | 74,40 | 71,73 | 69,57 | 67,41 | 64,33 | 23.6% / 74,40 | TESTATO | supporto tecnico, neckline rialzista, invalidazione rialzista | 0 |
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

- **BTC**: 0/30 previsioni controllate su 24 fatte. Stato: **RACCOLTA DATI**.
- **SOL**: 0/30 previsioni controllate su 24 fatte. Stato: **RACCOLTA DATI**.
- **DOGE**: 0/30 previsioni controllate su 24 fatte. Stato: **RACCOLTA DATI**.

| Asset | Previsioni fatte | Controllate | Progresso | In attesa | Stato | Prossimo controllo |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 24 | 0 | 0/30 [░░░░░░░░░░] | 24 | RACCOLTA DATI | 2026-08-02 / tra 7 giorni |
| SOL | 24 | 0 | 0/30 [░░░░░░░░░░] | 24 | RACCOLTA DATI | 2026-08-02 / tra 7 giorni |
| DOGE | 24 | 0 | 0/30 [░░░░░░░░░░] | 24 | RACCOLTA DATI | 2026-08-02 / tra 7 giorni |

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

Generato: 2026-07-26 05:14 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [data_quality_coherence_report.md](data_quality_coherence_report.md)

Questo controllo non modifica punteggi o decisioni. Verifica che tutti i moduli usino lo stesso prezzo corrente e che le nuove regole Technical/Classic Visual siano integre.

## Stato finale: **WARN**

## Avvisi

- 1 campi prezzo superano la tolleranza specifica del modulo.

## Prezzo unico per modulo

| Modulo                  | Asset   | Campo             | Stato   | Prezzo snapshot   | Prezzo modulo   | Differenza   |
|:------------------------|:--------|:------------------|:--------|:------------------|:----------------|:-------------|
| Scanner                 | BTC     | current_price     | OK      | 64.460 $          | 64.460 $        | +0,0000%     |
| Scanner                 | DOGE    | current_price     | OK      | 0.07349 $         | 0.07349 $       | -0,0000%     |
| Scanner                 | SOL     | current_price     | OK      | 75,08 $           | 75,08 $         | +0,0000%     |
| Scanner Forecast        | BTC     | current_price     | OK      | 64.460 $          | 64.460 $        | +0,0000%     |
| Scanner Forecast        | SOL     | current_price     | OK      | 75,08 $           | 75,08 $         | +0,0000%     |
| Scanner Forecast        | DOGE    | current_price     | OK      | 0.07349 $         | 0.07349 $       | -0,0000%     |
| Technical Structure     | BTC     | price             | OK      | 64.460 $          | 64.460 $        | +0,0000%     |
| Technical Structure     | SOL     | price             | OK      | 75,08 $           | 75,08 $         | +0,0000%     |
| Technical Structure     | DOGE    | price             | OK      | 0.07349 $         | 0.07349 $       | -0,0000%     |
| Classic Technical       | BTC     | price             | OK      | 64.460 $          | 64.460 $        | +0,0000%     |
| Classic Technical       | SOL     | price             | OK      | 75,08 $           | 75,08 $         | +0,0000%     |
| Classic Technical       | DOGE    | price             | OK      | 0.07349 $         | 0.07349 $       | -0,0000%     |
| Classic Visual          | BTC     | price             | OK      | 64.460 $          | 64.460 $        | +0,0000%     |
| Classic Visual          | SOL     | price             | OK      | 75,08 $           | 75,08 $         | +0,0000%     |
| Classic Visual          | DOGE    | price             | OK      | 0.07349 $         | 0.07349 $       | -0,0000%     |
| Exchange Microstructure | BTC     | price             | OK      | 64.460 $          | 64.469 $        | +0,0149%     |
| Exchange Microstructure | SOL     | price             | OK      | 75,08 $           | 75,00 $         | -0,0999%     |
| Exchange Microstructure | DOGE    | price             | WARN    | 0.07349 $         | 0.07319 $       | -0,4082%     |
| RSI top-cycle           | SOL     | current_price     | OK      | 75,08 $           | 75,08 $         | +0,0000%     |
| RSI top-cycle           | SOL     | current_price     | OK      | 75,08 $           | 75,08 $         | +0,0000%     |
| Frattale BTC/SOL        | SOL     | sol_current_price | OK      | 75,08 $           | 75,08 $         | +0,0000%     |
| Fractal path            | SOL     | current_price     | OK      | 75,08 $           | 75,08 $         | +0,0000%     |

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

Generato: 2026-07-26T20:17:34+00:00

- Modalità: **SOLO PAPER TRADING**
- Asset: **SOL spot**
- Leva: **nessuna (1x)**
- Capitale iniziale separato: **€40.000,00**
- Fonte mercato: **KUCOIN_PUBLIC_API**; nuove entrate: **CONSENTITE**

| Equity | Cash | SOL | Prezzo | Rendimento | Realizzato | Commissioni | Max DD | Operazioni |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €40.627,56 | €4.024,85 | 486.149894 | 75.2910 | +1.57% | €0,00 | €35,98 | 0.28% | 6 |

**Ultima decisione:** HOLD — Prezzo dentro la fascia neutrale.

Bande 4H: L2 71.0197 · L1 73.1419 · media 75.7948 · U1 78.4476 · U2 80.5698.

> Questo portafoglio non condivide capitale, posizioni o statistiche con il paper trading da €10.000.
<!-- SOL_SPOT_ADAPTIVE_END -->
