<!-- COMPACT_REPORT_HEADER_START -->
> **Vista compatta:** Decisione operativa, Global Confluence e cambiamenti giornalieri restano aperti. Tocca il titolo di una sezione per mostrare o nascondere i dettagli.  
> Tutte le tabelle e tutti i dati restano nel file: copiando il Markdown raw viene copiato tutto.
<!-- COMPACT_REPORT_HEADER_END -->

<!-- COMPACT_SECTION_START:decision -->
<details open>
<summary><strong>🧭 Decisione operativa — da leggere per prima</strong></summary>

<!-- DECISION_REPORT_START -->

# Decisione operativa sintetica

Generato: 2026-08-25 05:32 UTC

Report separato completo: [decision_report.md](decision_report.md)

Sintesi automatica dello scanner: l'azione spot viene copiata direttamente dal Global Confluence; long, short e rischio restano filtri separati e più prudenti.

| Asset | Global | Direzione | Spot | Long leva | Short leva | Max long | Max short | Rischio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +6 | BULLISH | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE | LONG PRUDENTE | NO SHORT | max 2x isolated | nessuna | MEDIO |
| SOL | +6 | NEUTRALE / COSTRUTTIVO | HOLD / TRANCHE PICCOLE, NO LEVA | NO LONG A LEVA | NO SHORT | nessuna | nessuna | MOLTO ALTO |
| DOGE | +5 | NEUTRALE / COSTRUTTIVO | SOLO TRANCHE PICCOLE / NO LEVA | NO LONG A LEVA | NO SHORT | nessuna | nessuna | MOLTO ALTO |

## Lettura immediata

- **BTC**: Global = **+6**, spot = **ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE**, long = **LONG PRUDENTE**, short = **NO SHORT**, rischio = **MEDIO**.
- **SOL**: Global = **+6**, spot = **HOLD / TRANCHE PICCOLE, NO LEVA**, long = **NO LONG A LEVA**, short = **NO SHORT**, rischio = **MOLTO ALTO**.
- **DOGE**: Global = **+5**, spot = **SOLO TRANCHE PICCOLE / NO LEVA**, long = **NO LONG A LEVA**, short = **NO SHORT**, rischio = **MOLTO ALTO**.

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
- Conferme: Prima resistenza sopra 82.792; conferma del doppio minimo sopra 66.910.
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
- Conferme: Doppio minimo target raggiunto finché mantiene 78,73; nuova conferma tecnica sopra 127,97; milestone analogiche 116,62 / 139,27, valide soltanto se rientra anche il gap frattale.
- Invalidazioni: Allarmi sotto 94,82 / 74,20 / 62,19.

### DOGE

- Global Confluence: **+5**
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
- **Lifecycle EMA200** = per SOL resta solo contesto, peso Global 0; score interno 2; EMA200 circa 111,39 $; upside verso EMA200 +8,90%. Non autorizza leva e non aggiunge punti automatici.
- **NO LONG** non significa automaticamente **SHORT**. Lo short ha senso solo se il quadro è bearish o se lo spike viene spesso scaricato.
- Per SOL, se il Global è da **+3 in su**, la decisione non deve diventare bearish solo perché lo scanner grezzo a 30 giorni è incerto.

<!-- DECISION_REPORT_END -->

<!-- BTC_SOL_FRACTAL_START -->

---

# Frattale mirato: BTC 2022 vs SOL 2026

Report separato completo: [btc_2022_vs_sol_2026_report.md](btc_2022_vs_sol_2026_report.md)

Ultima candela SOL usata: **25 agosto 2026**

## SOL PRICE CONTEXT

| Voce | Valore | Provenienza / significato |
| --- | --- | --- |
| Anchor computazionale | 102,48 $ | 2026-08-25T05:30:22Z \| Yahoo Finance daily shared snapshot \| Close 1d |
| Candela anchor completata | NO | Stato esplicito; il valore non viene sostituito dal prezzo pubblico. |
| Riferimento pubblico corrente | 101,91 $ | 2026-08-25T06:00:00Z \| Yahoo Finance \| solo display |
| Età anchor alla generazione | 0h 30m | WITHIN_DAILY_REPORT_CADENCE |
| Gap corrente vs anchor | -0,57000 $ | -0,56% |
| Validità input modello | REPRODUCIBLE_SHARED_SNAPSHOT | Non è una dichiarazione di validità del segnale/trading. |

```text
COMPUTATIONAL_ANCHOR_PRICE=102.4800033569336
COMPUTATIONAL_ANCHOR_FIELD=Close
COMPUTATIONAL_ANCHOR_TIMESTAMP=2026-08-25T05:30:22Z
COMPUTATIONAL_ANCHOR_SYMBOL=SOL-USD
COMPUTATIONAL_ANCHOR_PROVIDER=Yahoo Finance daily shared snapshot
COMPUTATIONAL_ANCHOR_TIMEFRAME=1d
COMPUTATIONAL_ANCHOR_COMPLETED=NO
CURRENT_PUBLIC_REFERENCE_PRICE=101.91000366210938
CURRENT_PUBLIC_REFERENCE_TIMESTAMP=2026-08-25T06:00:00Z
CURRENT_PUBLIC_REFERENCE_ACQUIRED_AT=2026-08-25T06:00:28Z
CURRENT_PUBLIC_REFERENCE_SYMBOL=SOL-USD
CURRENT_PUBLIC_REFERENCE_PROVIDER=Yahoo Finance
CURRENT_PUBLIC_REFERENCE_FIELD=Close
CURRENT_PUBLIC_REFERENCE_TIMEFRAME=1m
CURRENT_PUBLIC_REFERENCE_STATUS=AVAILABLE
ANCHOR_AGE_SECONDS=1806.602413
ANCHOR_AGE_HOURS=0.5018340036111111
CURRENT_VS_ANCHOR_GAP_USD=-0.5699996948242188
CURRENT_VS_ANCHOR_GAP_PCT=-0.5562057729827874
```

## Verdetto: ANALOGIA DEBOLE / SCENARIO SECONDARIO

- **Fase attuale:** FRATTALE SOLO DI CONTESTO
- **Somiglianza totale:** +63,53%
- **Somiglianza strutturale:** +63,53%
- **Aderenza prezzo live:** +71,07%
- **Errore medio live:** +14,47%
- **Gap prezzo corrente:** +19,23%
- **Peso operativo suggerito:** 0
- **Affidabilita:** BASSA
- **Rischio fase:** ALTO
- **Trend tracking:** STRUTTURA STABILE
- **Sintesi:** Esistono alcuni elementi comuni, ma non abbastanza per una conferma.
- **SOL è al giorno:** 80 dal bottom usato.
- **Giorno BTC equivalente:** 2023-02-09
- **Prossimo step:** Proiezione condizionale, non conferma operativa: **Spinta rialzista abbastanza pulita.** Zona bassa **101,69 $** intorno al **26 agosto 2026**; zona alta **116,62 $** intorno al **5 settembre 2026**; fine step circa **112,48 $** entro il **8 settembre 2026**.

### Metadata aderenza prezzo

```text
OPERATIONAL_VERDICT_REASON=ANALOGIA DEBOLE / SCENARIO SECONDARIO
PRICE_ADHERENCE_FAILED=YES
PRICE_ADHERENCE_LIVE_AVG_GAP_FAILED=NO
PRICE_ADHERENCE_LAST_GAP_FAILED=YES
PRICE_ADHERENCE_LIVE_AVG_GAP_THRESHOLD_PCT=15.0
PRICE_ADHERENCE_LAST_GAP_THRESHOLD_PCT=18.0
PRICE_ADHERENCE_OBSERVED_LIVE_AVG_GAP_PCT=14.465999213913786
PRICE_ADHERENCE_OBSERVED_LAST_GAP_PCT=19.231703560210377
```

## Somiglianza prima e dopo inizio programma

Questa sezione separa la somiglianza della forma dall'aderenza reale del prezzo.

- **Inizio programma/scanner:** 3 luglio 2026
- **Prima del programma** = backtest retroattivo.
- **Da inizio programma** = verifica live: è la parte più importante per l'uso operativo.

| Periodo | Date | Giorni | Aderenza prezzo | Errore medio | Gap ultimo | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| Prima del programma | 6 giugno 2026 -> 2 luglio 2026 | 27 | +87,95% | +6,02% | +21,89% | ABBASTANZA ALLINEATO |
| Da inizio programma | 3 luglio 2026 -> 25 agosto 2026 | 54 | +71,07% | +14,47% | +19,23% | DEVIAZIONE MODERATA |
| Totale dal bottom | 6 giugno 2026 -> 25 agosto 2026 | 81 | +76,70% | +11,65% | +19,23% | DEVIAZIONE MODERATA |

Nota: un frattale può avere una forma simile ma un prezzo distante. In quel caso non è operativo finché il gap non rientra.

## Lettura operativa veloce

Il frattale resta non operativo. Motivo effettivo: ANALOGIA DEBOLE / SCENARIO SECONDARIO.

| Voce | Risposta | Perché |
| --- | --- | --- |
| Uso operativo | NO | Peso 0 per il verdetto: ANALOGIA DEBOLE / SCENARIO SECONDARIO. |
| Aderenza live | +71,07% | Errore medio live +14,47%. |
| Gap corrente | +19,23% | Prezzo non aderente: superata almeno una soglia canonica (15% medio / 18% ultimo). |
| Prima conferma prezzo | 116,62 $ | Serve anche miglioramento del gap, non solo una candela sopra il livello. |
| Seconda conferma | 139,27 $ | Rende più credibile il percorso, ma non sostituisce l'aderenza. |
| Invalidazione soft | 94,82 $ | Sotto questa zona il quadro peggiora. |
| Invalidazione forte | 62,19 $ | Sotto il bottom il paragone è quasi rotto. |

## Target ciclo fino al top BTC 2025

| Voce | Valore |
| --- | --- |
| Stato | CONTESTO / NON OPERATIVO |
| Top BTC 2025 | 6 ottobre 2025 - 124.753 $ |
| Data SOL equivalente | 21 aprile 2029 |
| Target ciclo base dall'anchor modello | 585,94 $ |
| Massimo percorso base | 585,94 $ (21 aprile 2029) |

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
| Prima conferma | 116,62 $ | Deve accompagnarsi al rientro del gap. |
| Seconda conferma | 139,27 $ | Scenario più credibile. |
| Invalidazione soft | 94,82 $ | Il frattale si indebolisce. |
| Invalidazione forte | 62,19 $ | Il paragone si rompe. |

## Proiezione veloce con date SOL

| Orizzonte | Data SOL | BTC fece | SOL base | Min percorso | Max percorso |
| --- | --- | --- | --- | --- | --- |
| 7 giorni | 1 settembre 2026 | +8,27% | 110,96 $ | 101,69 $ | 114,17 $ |
| 14 giorni | 8 settembre 2026 | +9,76% | 112,48 $ | 101,69 $ | 116,62 $ |
| 30 giorni | 24 settembre 2026 | -5,44% | 96,91 $ | 94,82 $ | 116,62 $ |
| 60 giorni | 24 ottobre 2026 | +35,90% | 139,27 $ | 94,82 $ | 139,27 $ |
| 90 giorni | 23 novembre 2026 | +26,59% | 129,73 $ | 94,82 $ | 143,19 $ |
| 120 giorni | 23 dicembre 2026 | +21,36% | 124,37 $ | 94,82 $ | 143,19 $ |

## Prossimi step se SOL segue BTC 2022

| Step | Date SOL | BTC fine | SOL zona bassa | SOL zona alta | SOL fine base | Lettura |
| --- | --- | --- | --- | --- | --- | --- |
| Step 1 - prossime 2 settimane | 25 agosto 2026 -> 8 settembre 2026 | +9,76% | 101,69 $ (26 agosto 2026) | 116,62 $ (5 settembre 2026) | 112,48 $ | Spinta rialzista abbastanza pulita. |
| Step 2 - primo mese | 9 settembre 2026 -> 24 settembre 2026 | -5,44% | 94,82 $ (23 settembre 2026) | 111,06 $ (14 settembre 2026) | 96,91 $ | Prima spike, poi scarico. |
| Step 3 - secondo mese | 25 settembre 2026 -> 24 ottobre 2026 | +35,90% | 104,10 $ (25 settembre 2026) | 139,27 $ (24 ottobre 2026) | 139,27 $ | Spinta rialzista abbastanza pulita. |
| Step 4 - terzo mese | 25 ottobre 2026 -> 23 novembre 2026 | +26,59% | 128,11 $ (4 novembre 2026) | 143,19 $ (28 ottobre 2026) | 129,73 $ | Spinta rialzista abbastanza pulita. |

Nota: le proiezioni restano condizionali; il prezzo non è aderente secondo le soglie canoniche.

<!-- BTC_SOL_FRACTAL_END -->

<!-- PAPER_TRADING_START -->
# Paper trading automatico KuCoin

Generato: 2026-08-25T05:32:59+00:00


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [paper_trading_report.md](paper_trading_report.md)

## Configurazione attiva

- Capitale iniziale della simulazione: **€10.000,00**
- Capitale indicato nel file di configurazione: **€10.000,00**
- Obiettivo mensile monitorato: **€3.000,00**
- Compounding: **ATTIVO**
- Reinvestimento dei profitti: **100,00%**
- Politica target: **solo monitoraggio; il bot non aumenta il rischio per inseguirlo**
- Snapshot prezzi usato: **2026-08-25T05:05:29+00:00**; stato dati: **FRESH**; età: **0,0 min**; conversione EUR/USDT: **CONFIG_FALLBACK**
- Dashboard intraday: [apri la pagina live](https://github.com/eddyhardscit/crypto-fractal-scanner/blob/paper-trading-live/reports/paper_trading_live.md)

## Freschezza dati di mercato

| Stato | Fonte | Snapshot mercato | Controllato | Età | Limite | Nuove entrate |
| --- | --- | --- | --- | --- | --- | --- |
| FRESH | KUCOIN_PUBLIC_API | 2026-08-25T05:05:29+00:00 | 2026-08-25T05:05:29+00:00 | 0,0 min | 25,0 min | ABILITATE |

| TF | Asset con dati | Candela più recente | Candela più vecchia | Ritardo dopo chiusura | Tolleranza | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| 15m | 12 | 2026-08-25T04:45:00+00:00 | 2026-08-25T04:45:00+00:00 | 5,6 min | 25,0 min | OK |
| 60m | 12 | 2026-08-25T04:00:00+00:00 | 2026-08-25T04:00:00+00:00 | 5,6 min | 45,0 min | OK |
| 240m | 12 | 2026-08-25T00:00:00+00:00 | 2026-08-25T00:00:00+00:00 | 1,09 h | 1,00 h | STALE_CANDLE |

## Segnali quasi entrati / motivi di esclusione

| Portafoglio | Asset | TF | Lato | Score | Soglia | Manca | Stato | Ritardo chiusura | RSI D/W (peso 0) | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1H Fast V3 Long Only V1 | BTC | 60m | LONG | 4,75 | 4,50 | 0,00 | OPENED | 5,6 min | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| 1H Fast Tp2 V1 | ZEC | 60m | LONG | 5,41 | 4,50 | 0,00 | OPENED | 5,6 min | D: n/a | W: n/a | peso 0 | Posizione virtuale aperta in questa esecuzione. |
| Principale 4H | XRP | 240m | LONG | 7,75 | 6,00 | 0,00 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | HYPE | 240m | LONG | 7,38 | 6,00 | 0,00 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | ETH | 240m | LONG | 6,00 | 6,00 | 0,00 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | BTC | 240m | LONG | 5,25 | 6,00 | 0,75 | STALE_CANDLE | 1,09 h | D: Bullish regolare [CONFERMATA] | W: Bullish regolare [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | VELVET | 240m | SHORT | -4,75 | 6,00 | 1,25 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | DOGE | 240m | LONG | 4,62 | 6,00 | 1,38 | STALE_CANDLE | 1,09 h | D: Hidden bearish [CONFERMATA] | W: Hidden bullish [IN_FORMAZIONE] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | SOL | 240m | LONG | 4,50 | 6,00 | 1,50 | STALE_CANDLE | 1,09 h | D: Conferma ribassista [CONTESTO] | W: Hidden bearish [CONFERMATA] | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | SUI | 240m | LONG | 2,47 | 6,00 | 3,53 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Principale 4H | TUT | 240m | SHORT | -1,48 | 6,00 | 4,52 | STALE_CANDLE | 1,09 h | D: n/a | W: n/a | peso 0 | Segnale arrivato troppo tardi: candela chiusa da 65.6 minuti; tolleranza 60 minuti. |
| Bilanciata 1H V3 Filtered | TUT | 60m | SHORT | -6,25 | 6,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Fast Score 6 75 Cost Aware V1 | TUT | 60m | SHORT | -6,25 | 6,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Forza relativa 1H V2 | TUT | 60m | SHORT | -6,25 | 5,50 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Combo Trend | TUT | 60m | SHORT | -6,25 | 5,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Combo Adaptive | TUT | 60m | SHORT | -6,25 | 5,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Combo Adaptive Partial 1R V1 | TUT | 60m | SHORT | -6,25 | 5,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| 1H Balanced V3 Long Only V1 | TUT | 60m | SHORT | -6,25 | 6,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Bilanciata 1H V3 Filtered | VELVET | 60m | SHORT | -6,25 | 6,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Benchmark trend following EMA 1H | VELVET | 60m | SHORT | -6,25 | 5,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Combo Trend | VELVET | 60m | SHORT | -6,25 | 5,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |
| Combo Adaptive | VELVET | 60m | SHORT | -6,25 | 5,00 | 0,00 | READY | 5,6 min | D: n/a | W: n/a | peso 0 | Tutti i filtri del generatore sono stati superati. |

**Manca** indica quanti punti servivano per raggiungere la soglia. `STRATEGY_FILTER` significa che lo score bastava, ma mancava breakout, momentum o forza relativa. `ALREADY_PROCESSED` significa che la stessa candela era già stata esaminata.

## Portafoglio principale — Principale 4H

| Equity | Rendimento | P&L mese | Target | Progresso | Aperte | Chiuse | Win rate | PF | Max DD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €9.520,12 | -4,80% | €-228,23 | €3.000,00 | -7,61% | 6 | 52 | 38,46% | 0,87 | 6,85% |

## Stato del campione statistico

| Principale 4H — eventi indip. | Sistema eventi indip. | Stato | Prossima soglia |
| --- | --- | --- | --- |
| 52 | 2178 | PRIME INDICAZIONI | 100 (mancano 48) |

- Trade del Principale 4H chiusi: **52**; win rate **38,46%**; profit factor **0,87**.
- Expectancy: **€-3,67** per trade; P&L netto: **€-190,76**; max drawdown: **6,85%**.
- Valutazione: **Si può osservare la direzione, ma il risultato resta fragile.**
- Soglie automatiche Telegram: **30, 100, 200 e 300 eventi indipendenti chiusi del portafoglio principale**.
- Una soglia richiede una valutazione; non attiva automaticamente il trading reale.

## Capitale impegnato e rischio

| Tipo | Portafoglio | Posizioni | Equity | Margine impegnato | Esposizione con leva | Rischio agli stop | P&L aperto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRINCIPALE | Principale 4H | 6 | €9.520,12 | €699,00 | €2.096,99 | €196,05 | €-288,04 |
| TEST | Benchmark Donchian breakout 1H | 5 | €11.448,76 | €2.408,61 | €4.817,22 | €172,42 | €63,30 |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | 7 | €11.342,35 | €984,32 | €2.952,95 | €226,58 | €27,64 |
| TEST | Combo Trend Side Regime Guard V1 | 5 | €11.256,90 | €1.200,01 | €2.400,03 | €172,08 | €96,73 |
| TEST | Donchian 1H Gb20 120R V1 | 5 | €11.179,21 | €2.351,90 | €4.703,81 | €168,36 | €61,81 |
| TEST | Scanner Top 5 Long 1H | 5 | €11.049,49 | €1.204,49 | €2.408,99 | €220,63 | €6,11 |
| TEST | Combo Adaptive | 7 | €10.754,46 | €1.410,55 | €2.821,10 | €215,28 | €38,06 |
| TEST | 1H Fast No Pepe V1 | 7 | €10.725,21 | €1.056,63 | €3.169,88 | €214,88 | €19,13 |
| TEST | Combo Adaptive Long Only V1 | 5 | €10.576,42 | €2.941,99 | €5.883,97 | €211,87 | €-9,65 |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | 5 | €10.554,59 | €1.189,19 | €3.567,56 | €211,33 | €2,04 |
| TEST | Combo Adaptive Side Regime Guard V1 | 5 | €10.546,82 | €1.097,00 | €2.194,01 | €157,82 | €123,46 |
| TEST | Main Side Regime Guard V1 | 6 | €10.507,27 | €677,33 | €2.031,99 | €163,22 | €-283,63 |
| TEST | Rapida 1H V3 Filtered | 5 | €10.486,78 | €1.181,55 | €3.544,64 | €209,97 | €2,03 |
| TEST | Scanner Top5 Btc Tp3 V1 | 5 | €10.428,40 | €1.695,19 | €3.390,38 | €208,31 | €13,82 |
| TEST | Scanner Top5 Btc Runner25 V1 | 5 | €10.422,30 | €1.694,20 | €3.388,39 | €208,19 | €13,81 |
| TEST | Scanner Top10 Long | 5 | €10.407,68 | €3.976,59 | €7.953,18 | €156,78 | €47,41 |
| TEST | 1H Fast Tp2 V1 | 7 | €10.355,73 | €737,92 | €2.213,75 | €156,82 | €74,50 |
| TEST | Scanner Top 5 + forza BTC 1H | 5 | €10.316,24 | €1.091,70 | €2.183,40 | €206,31 | €6,03 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | 0 | €10.300,05 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | 0 | €10.271,73 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Nohigh Range Only V1 | 0 | €10.247,95 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | 0 | €10.239,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | 0 | €10.235,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Adaptive 4H | 1 | €10.223,23 | €330,98 | €661,97 | €0,00 | €59,25 |
| TEST | Main Dynamic Asset Selector V1 | 1 | €10.213,05 | €141,85 | €425,56 | €51,07 | €0,00 |
| TEST | Sol Donchian 4H | 0 | €10.196,46 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Donchian 1H | 0 | €10.192,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | 0 | €10.185,37 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V2 | 0 | €10.182,21 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Partial 1R V1 | 7 | €10.160,77 | €1.277,19 | €2.554,37 | €153,58 | €66,88 |
| TEST | Btc Bollinger 1H | 1 | €10.152,40 | €1.262,52 | €3.787,57 | €50,69 | €16,27 |
| TEST | 1H Fast Score 6 75 Range Only V1 | 0 | €10.149,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | 0 | €10.145,12 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | 0 | €10.140,84 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H V3 Filtered | 5 | €10.132,16 | €1.067,57 | €3.202,71 | €201,86 | €51,77 |
| TEST | Sol Ema 1H | 1 | €10.112,01 | €349,20 | €1.047,59 | €0,00 | €73,95 |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | 0 | €10.099,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Ema 4H | 1 | €10.087,55 | €356,10 | €712,19 | €0,00 | €63,75 |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | 3 | €10.084,59 | €687,89 | €2.063,66 | €102,66 | €21,60 |
| TEST | Btc Adaptive 4H | 1 | €10.071,10 | €648,94 | €1.297,88 | €50,35 | €1,69 |
| TEST | Btc Adaptive 1H | 1 | €10.061,74 | €1.045,87 | €3.137,61 | €50,39 | €-14,73 |
| TEST | Btc Donchian 1H | 1 | €10.049,29 | €1.175,39 | €3.526,17 | €50,34 | €-16,55 |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | 0 | €10.048,77 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Bollinger 1H | 0 | €10.046,17 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · €50 · 15x | 0 | €10.045,08 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Rapida 1H V1 | 0 | €10.043,28 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Balanced Short Trend Down Strict V1 | 0 | €10.035,46 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 20 · prudente · 5x | 0 | €10.028,67 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Nohigh Cap75 V1 | 0 | €10.028,66 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Bollinger 4H | 1 | €10.025,87 | €775,58 | €1.551,16 | €50,15 | €-2,64 |
| TEST | Btc Ema 4H | 1 | €10.020,40 | €704,37 | €1.408,74 | €50,10 | €1,83 |
| TEST | Scalp RSI Short 85 · €50 · 15x | 0 | €10.017,98 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Ampia 4H | 7 | €10.016,21 | €998,50 | €1.997,00 | €206,18 | €-315,50 |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | 1 | €10.015,88 | €299,55 | €599,09 | €50,20 | €0,00 |
| TEST | Scalp RSI Short 80 · €50 · 15x | 0 | €10.015,51 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | 0 | €10.013,82 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Doge Ema 1H | 1 | €10.010,45 | €248,90 | €746,70 | €50,09 | €-6,56 |
| TEST | Scalp RSI Short 75 · €10 · 15x | 0 | €10.009,02 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | 0 | €10.008,92 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 No Esports Long Only V1 | 4 | €10.006,39 | €1.737,79 | €5.213,38 | €148,29 | €5,25 |
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
| TEST | Scanner Top15 Long | 7 | €9.973,26 | €1.841,32 | €3.682,65 | €195,72 | €11,20 |
| TEST | Scanner Top20 Long | 7 | €9.973,26 | €1.841,32 | €3.682,65 | €195,72 | €11,20 |
| TEST | Sol Adaptive 1H | 1 | €9.968,20 | €344,23 | €1.032,69 | €0,00 | €72,90 |
| TEST | Btc Donchian 4H | 1 | €9.966,79 | €700,60 | €1.401,20 | €49,83 | €1,82 |
| TEST | Eth Ema 4H | 1 | €9.954,71 | €487,73 | €975,47 | €49,56 | €44,44 |
| TEST | Scalp RSI Short 80 · prudente · 5x | 0 | €9.952,43 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Long 25 · €50 · 15x | 0 | €9.952,25 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scalp RSI Short 75 · prudente · 5x | 0 | €9.939,62 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Btc Ema 1H | 1 | €9.925,57 | €1.031,72 | €3.095,15 | €49,71 | €-14,53 |
| TEST | Combo Adaptive Regime V1 | 2 | €9.919,86 | €720,33 | €1.440,66 | €49,43 | €31,51 |
| TEST | Doge Donchian 1H | 0 | €9.911,95 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Adaptive Quality7 V1 | 4 | €9.898,22 | €1.604,00 | €3.208,01 | €194,94 | €5,16 |
| TEST | Combo Scanner | 5 | €9.897,57 | €1.047,40 | €2.094,79 | €197,94 | €5,79 |
| TEST | Combo Adaptive Quality7 Regime V1 | 1 | €9.889,90 | €295,78 | €591,56 | €49,57 | €0,00 |
| TEST | Eth Ema 1H | 1 | €9.867,74 | €783,24 | €2.349,73 | €49,33 | €2,89 |
| TEST | Forza relativa 1H V2 | 4 | €9.856,05 | €1.806,95 | €3.613,90 | €97,62 | €65,82 |
| TEST | Eth Adaptive 1H | 0 | €9.844,63 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | 0 | €9.837,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Sol Bollinger 1H | 0 | €9.821,20 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | 0 | €9.817,34 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Guard V1 | 5 | €9.809,43 | €1.332,44 | €2.664,88 | €151,38 | €7,10 |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | 0 | €9.779,10 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 No Esports V1 | 5 | €9.778,68 | €713,06 | €2.139,17 | €195,60 | €12,44 |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | 0 | €9.762,18 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | 0 | €9.723,72 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Balanced Long No Rhv V1 | 6 | €9.717,62 | €1.827,42 | €5.482,27 | €193,87 | €3,54 |
| TEST | Eth Bollinger 1H | 0 | €9.703,71 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | 3 | €9.693,56 | €642,23 | €1.284,46 | €97,32 | €37,12 |
| TEST | Eth Donchian 1H | 0 | €9.678,07 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Mfe V1 | 5 | €9.670,97 | €1.023,42 | €2.046,83 | €193,41 | €5,66 |
| TEST | 1H Fast V3 Long Only V1 | 6 | €9.640,32 | €1.651,50 | €4.954,51 | €192,81 | €-9,69 |
| TEST | Global Confluence puro 1H | 0 | €9.628,04 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Balanced V3 Long Only V1 | 5 | €9.584,43 | €1.049,33 | €3.147,98 | €191,35 | €48,63 |
| TEST | Scanner Top5 Btc Guard Mfe V1 | 5 | €9.581,30 | €1.301,45 | €2.602,90 | €147,85 | €6,93 |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | 0 | €9.579,83 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H V2 | 2 | €9.534,71 | €607,25 | €1.821,75 | €94,13 | €5,06 |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | 4 | €9.523,77 | €612,41 | €1.224,82 | €96,57 | €32,09 |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | 0 | €9.517,55 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Trend | 5 | €9.471,55 | €981,95 | €1.963,90 | €143,09 | €30,65 |
| TEST | 1H Fast V3 Nohigh V1 | 0 | €9.435,38 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Score 6 75 V1 | 0 | €9.415,87 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom10 Short | 4 | €9.398,18 | €1.261,36 | €2.522,73 | €140,86 | €77,46 |
| TEST | Scanner Bottom15 Short | 4 | €9.398,18 | €1.261,36 | €2.522,73 | €140,86 | €77,46 |
| TEST | Scanner Bottom20 Short | 4 | €9.398,18 | €1.261,36 | €2.522,73 | €140,86 | €77,46 |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | 0 | €9.389,68 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Runner25 V1 | 1 | €9.377,78 | €34,77 | €69,54 | €8,34 | €-0,39 |
| TEST | Master Adaptive Gb20 Be V1 | 0 | €9.372,49 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Gb20 Partial V1 | 0 | €9.362,52 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | 3 | €9.357,83 | €589,42 | €1.178,84 | €92,35 | €31,54 |
| TEST | Master Adaptive No Alt V1 | 0 | €9.354,60 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Benchmark trend following EMA 1H | 5 | €9.352,96 | €1.813,23 | €3.626,46 | €95,83 | €77,62 |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | 4 | €9.333,05 | €1.252,64 | €2.505,29 | €139,88 | €76,92 |
| TEST | Master Adaptive V1 | 0 | €9.326,30 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Scanner Bottom5 Short Profit Lock V1 | 4 | €9.318,86 | €1.250,74 | €2.501,48 | €139,67 | €76,80 |
| TEST | Master Adaptive Expanded V1 | 1 | €9.317,58 | €197,50 | €395,01 | €47,40 | €-2,24 |
| TEST | Master Adaptive Gb20 Loss Cap V1 | 1 | €9.249,86 | €195,70 | €391,41 | €45,67 | €-2,22 |
| TEST | Scanner Bottom 5 Short 1H | 4 | €9.247,14 | €1.241,11 | €2.482,23 | €138,60 | €76,21 |
| TEST | Scanner Top5 Btc Btc Le3 V1 | 3 | €9.220,07 | €610,86 | €1.221,72 | €92,56 | €35,30 |
| TEST | Combo Adaptive Mfe Trail | 6 | €9.205,93 | €1.214,43 | €2.428,87 | €183,97 | €36,86 |
| TEST | Master Adaptive Gb20 V1 | 0 | €9.202,39 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | 0 | €9.165,52 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Bilanciata 1H V1 | 0 | €9.150,69 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | 1H Fast V3 Cap75 V1 | 0 | €9.106,22 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Master Adaptive Strict3 V1 | 0 | €9.056,84 | €0,00 | €0,00 | €0,00 | €0,00 |
| TEST | Combo Mean Reversion | 1 | €9.029,57 | €1.684,34 | €3.368,67 | €45,09 | €14,47 |
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
| PRINCIPALE | Principale 4H | Confluenza trend | €9.520,12 | €-190,76 | 52 | 52 | 38,46% | 0,87 | €-3,67 | 6,85% |
| TEST | Benchmark Donchian breakout 1H | Donchian breakout 20 barre | €11.448,76 | €1.387,48 | 98 | 98 | 50,00% | 1,63 | €14,16 | 4,99% |
| TEST | 1H Fast Score 6 75 Cost Aware V1 | Momentum / breakout | €11.342,35 | €1.317,19 | 137 | 137 | 54,01% | 1,50 | €9,61 | 4,41% |
| TEST | Combo Trend Side Regime Guard V1 | Combo Trend | €11.256,90 | €1.162,73 | 103 | 103 | 56,31% | 1,64 | €11,29 | 4,94% |
| TEST | Donchian 1H Gb20 120R V1 | Donchian breakout 20 barre | €11.179,21 | €1.119,37 | 66 | 66 | 50,00% | 1,85 | €16,96 | 4,99% |
| TEST | Scanner Top 5 Long 1H | Scanner Top 5 Long | €11.049,49 | €1.045,48 | 131 | 131 | 50,38% | 1,41 | €7,98 | 8,85% |
| TEST | Combo Adaptive | Combo Adaptive | €10.754,46 | €719,14 | 140 | 140 | 46,43% | 1,31 | €5,14 | 7,91% |
| TEST | 1H Fast No Pepe V1 | Momentum / breakout | €10.725,21 | €708,81 | 201 | 201 | 48,76% | 1,19 | €3,53 | 6,80% |
| TEST | Combo Adaptive Long Only V1 | Combo Adaptive | €10.576,42 | €590,19 | 113 | 113 | 49,56% | 1,25 | €5,22 | 6,25% |
| TEST | 1H Fast V3 No Esports Mfe Lock V1 | Momentum / breakout V3 Filtered | €10.554,59 | €554,77 | 187 | 187 | 50,80% | 1,18 | €2,97 | 9,50% |
| TEST | Combo Adaptive Side Regime Guard V1 | Combo Adaptive | €10.546,82 | €425,63 | 112 | 112 | 48,21% | 1,19 | €3,80 | 8,68% |
| TEST | Main Side Regime Guard V1 | Confluenza trend | €10.507,27 | €792,57 | 33 | 33 | 54,55% | 2,27 | €24,02 | 3,82% |
| TEST | Rapida 1H V3 Filtered | Momentum / breakout V3 Filtered | €10.486,78 | €486,95 | 231 | 231 | 45,02% | 1,12 | €2,11 | 9,48% |
| TEST | Scanner Top5 Btc Tp3 V1 | Scanner Top 5 + forza BTC | €10.428,40 | €417,23 | 97 | 97 | 44,33% | 1,19 | €4,30 | 11,78% |
| TEST | Scanner Top5 Btc Runner25 V1 | Scanner Top 5 + forza BTC | €10.422,30 | €411,13 | 101 | 101 | 44,55% | 1,19 | €4,07 | 12,06% |
| TEST | Scanner Top10 Long | Scanner Top10 Long | €10.407,68 | €365,52 | 118 | 118 | 50,85% | 1,18 | €3,10 | 10,31% |
| TEST | 1H Fast Tp2 V1 | Momentum / breakout | €10.355,73 | €282,60 | 217 | 217 | 41,01% | 1,07 | €1,30 | 6,56% |
| TEST | Scanner Top 5 + forza BTC 1H | Scanner Top 5 + forza BTC | €10.316,24 | €312,12 | 118 | 118 | 46,61% | 1,13 | €2,65 | 11,27% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R200 86882Aa9 | Momentum / breakout V3 Filtered | €10.300,05 | €300,05 | 33 | 33 | 48,48% | 2,04 | €9,09 | 2,01% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 L Tp R200 903364Ad | Momentum / breakout V3 Filtered | €10.271,73 | €271,73 | 22 | 22 | 50,00% | 1,74 | €12,35 | 1,72% |
| TEST | 1H Fast V3 Nohigh Range Only V1 | Momentum / breakout V3 Filtered | €10.247,95 | €247,95 | 41 | 41 | 46,34% | 1,25 | €6,05 | 3,97% |
| TEST | Evo Cand 1H Fast V3 Nohigh Regime Guard Tp R200 934590Ed | Momentum / breakout V3 Filtered | €10.239,20 | €239,20 | 17 | 17 | 52,94% | 4,50 | €14,07 | 1,01% |
| TEST | Evo Cand 1H Fast V3 Cap75 V1 Tp R250 3B03Ece1 | Momentum / breakout V3 Filtered | €10.235,18 | €235,18 | 20 | 20 | 50,00% | 1,90 | €11,76 | 2,73% |
| TEST | Sol Adaptive 4H | Combo Adaptive | €10.223,23 | €164,84 | 6 | 6 | 50,00% | 2,46 | €27,47 | 1,01% |
| TEST | Main Dynamic Asset Selector V1 | Confluenza trend | €10.213,05 | €213,35 | 12 | 12 | 41,67% | 1,74 | €17,78 | 1,68% |
| TEST | Sol Donchian 4H | Donchian breakout 20 barre | €10.196,46 | €196,46 | 6 | 6 | 50,00% | 2,73 | €32,74 | 1,05% |
| TEST | Sol Donchian 1H | Donchian breakout 20 barre | €10.192,62 | €192,62 | 13 | 13 | 53,85% | 1,78 | €14,82 | 2,77% |
| TEST | Evo Cand 1H Fast V3 Long Nohigh Cap75 V Tp R200 051501D0 | Momentum / breakout V3 Filtered | €10.185,37 | €185,37 | 22 | 22 | 40,91% | 1,57 | €8,43 | 2,27% |
| TEST | Rapida 1H V2 | Momentum / breakout V2 | €10.182,21 | €182,21 | 45 | 40 | 46,67% | 1,16 | €4,05 | 3,89% |
| TEST | Combo Adaptive Partial 1R V1 | Combo Adaptive | €10.160,77 | €95,87 | 142 | 142 | 45,77% | 1,04 | €0,68 | 8,69% |
| TEST | Btc Bollinger 1H | Bollinger mean reversion | €10.152,40 | €138,40 | 5 | 5 | 80,00% | 3,42 | €27,68 | 0,85% |
| TEST | 1H Fast Score 6 75 Range Only V1 | Momentum / breakout | €10.149,62 | €149,62 | 38 | 38 | 44,74% | 1,14 | €3,94 | 3,35% |
| TEST | Evo Cand 1H Fast V3 No Esports V1 Tp R200 68F866E1 | Momentum / breakout V3 Filtered | €10.145,12 | €145,12 | 44 | 44 | 45,45% | 1,20 | €3,30 | 2,91% |
| TEST | 1H Fast V3 Nohigh Regime Guard V1 | Momentum / breakout V3 Filtered | €10.140,84 | €140,84 | 63 | 63 | 44,44% | 1,10 | €2,24 | 5,24% |
| TEST | Bilanciata 1H V3 Filtered | Confluenza trend V3 Filtered | €10.132,16 | €83,31 | 148 | 148 | 43,24% | 1,03 | €0,56 | 9,12% |
| TEST | Sol Ema 1H | Trend following EMA | €10.112,01 | €39,53 | 13 | 13 | 38,46% | 1,10 | €3,04 | 3,33% |
| TEST | Evo Cand 1H Fast V3 No Esports Mfe Lock Tp R200 6B7C560F | Momentum / breakout V3 Filtered | €10.099,04 | €99,04 | 55 | 55 | 54,55% | 1,12 | €1,80 | 3,59% |
| TEST | Sol Ema 4H | Trend following EMA | €10.087,55 | €24,73 | 7 | 7 | 28,57% | 1,11 | €3,53 | 2,27% |
| TEST | 1H Fast Long Btc 1 3 Cap75 V1 | Momentum / breakout | €10.084,59 | €65,65 | 53 | 53 | 45,28% | 1,06 | €1,24 | 3,73% |
| TEST | Btc Adaptive 4H | Combo Adaptive | €10.071,10 | €70,19 | 2 | 2 | 50,00% | 2,39 | €35,09 | 0,96% |
| TEST | Btc Adaptive 1H | Combo Adaptive | €10.061,74 | €78,35 | 7 | 7 | 57,14% | 1,69 | €11,19 | 1,13% |
| TEST | Btc Donchian 1H | Donchian breakout 20 barre | €10.049,29 | €67,96 | 8 | 8 | 62,50% | 1,41 | €8,50 | 1,49% |
| TEST | Evo Cand 1H Fast V3 Tp R250 6B45Fc13 | Momentum / breakout V3 Filtered | €10.048,77 | €48,77 | 23 | 23 | 43,48% | 1,12 | €2,12 | 3,05% |
| TEST | Doge Bollinger 1H | Bollinger mean reversion | €10.046,17 | €46,17 | 9 | 9 | 55,56% | 1,19 | €5,13 | 1,89% |
| TEST | Scalp RSI Short 75 · €50 · 15x | Inversione RSI estrema 15m | €10.045,08 | €45,08 | 28 | 28 | 46,43% | 1,40 | €1,61 | 0,33% |
| TEST | Rapida 1H V1 | Momentum / breakout | €10.043,28 | €43,28 | 78 | 78 | 34,62% | 1,02 | €0,55 | 6,76% |
| TEST | 1H Balanced Short Trend Down Strict V1 | Confluenza trend | €10.035,46 | €35,46 | 13 | 13 | 38,46% | 1,13 | €2,73 | 1,80% |
| TEST | Scalp RSI Long 20 · prudente · 5x | Inversione RSI estrema 15m | €10.028,67 | €28,67 | 9 | 9 | 55,56% | 1,80 | €3,19 | 0,36% |
| TEST | 1H Fast Nohigh Cap75 V1 | Momentum / breakout | €10.028,66 | €28,66 | 122 | 122 | 43,44% | 1,01 | €0,23 | 7,10% |
| TEST | Btc Bollinger 4H | Bollinger mean reversion | €10.025,87 | €29,45 | 2 | 2 | 50,00% | 1,54 | €14,72 | 0,86% |
| TEST | Btc Ema 4H | Trend following EMA | €10.020,40 | €19,41 | 3 | 3 | 33,33% | 1,19 | €6,47 | 1,76% |
| TEST | Scalp RSI Short 85 · €50 · 15x | Inversione RSI estrema 15m | €10.017,98 | €17,98 | 5 | 5 | 60,00% | 1,69 | €3,60 | 0,31% |
| TEST | Ampia 4H | Confluenza trend | €10.016,21 | €333,13 | 51 | 51 | 35,29% | 1,29 | €6,53 | 4,45% |
| TEST | Combo Adaptive Quality7 Regime Partial 1R V1 | Combo Adaptive | €10.015,88 | €16,33 | 37 | 37 | 48,65% | 1,02 | €0,44 | 4,21% |
| TEST | Scalp RSI Short 80 · €50 · 15x | Inversione RSI estrema 15m | €10.015,51 | €15,51 | 15 | 15 | 40,00% | 1,32 | €1,03 | 0,53% |
| TEST | 1H Fast V3 No Esports Stress Guard V1 | Momentum / breakout V3 Filtered | €10.013,82 | €13,82 | 41 | 41 | 48,78% | 1,01 | €0,34 | 4,50% |
| TEST | Doge Ema 1H | Trend following EMA | €10.010,45 | €18,06 | 15 | 15 | 60,00% | 1,05 | €1,20 | 2,77% |
| TEST | Scalp RSI Short 75 · €10 · 15x | Inversione RSI estrema 15m | €10.009,02 | €9,02 | 28 | 28 | 46,43% | 1,40 | €0,32 | 0,07% |
| TEST | Evo Cand 1H Fast V3 No Esports Long Onl Tp R200 7Bbb9481 | Momentum / breakout V3 Filtered | €10.008,92 | €8,92 | 30 | 30 | 36,67% | 1,02 | €0,30 | 4,84% |
| TEST | 1H Fast V3 No Esports Long Only V1 | Momentum / breakout V3 Filtered | €10.006,39 | €4,34 | 146 | 146 | 44,52% | 1,00 | €0,03 | 10,60% |
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
| TEST | Scanner Top15 Long | Scanner Top15 Long | €9.973,26 | €-35,08 | 115 | 115 | 50,43% | 0,98 | €-0,31 | 10,31% |
| TEST | Scanner Top20 Long | Scanner Top20 Long | €9.973,26 | €-35,08 | 115 | 115 | 50,43% | 0,98 | €-0,31 | 10,31% |
| TEST | Sol Adaptive 1H | Combo Adaptive | €9.968,20 | €-103,26 | 14 | 14 | 35,71% | 0,77 | €-7,38 | 4,59% |
| TEST | Btc Donchian 4H | Donchian breakout 20 barre | €9.966,79 | €-34,19 | 4 | 4 | 25,00% | 0,80 | €-8,55 | 2,43% |
| TEST | Eth Ema 4H | Trend following EMA | €9.954,71 | €-88,72 | 5 | 5 | 20,00% | 0,58 | €-17,74 | 1,83% |
| TEST | Scalp RSI Short 80 · prudente · 5x | Inversione RSI estrema 15m | €9.952,43 | €-47,57 | 15 | 15 | 40,00% | 0,45 | €-3,17 | 0,89% |
| TEST | Scalp RSI Long 25 · €50 · 15x | Inversione RSI estrema 15m | €9.952,25 | €-47,75 | 15 | 15 | 40,00% | 0,36 | €-3,18 | 0,72% |
| TEST | Scalp RSI Short 75 · prudente · 5x | Inversione RSI estrema 15m | €9.939,62 | €-60,38 | 28 | 28 | 46,43% | 0,60 | €-2,16 | 0,84% |
| TEST | Btc Ema 1H | Trend following EMA | €9.925,57 | €-58,05 | 11 | 11 | 36,36% | 0,82 | €-5,28 | 1,94% |
| TEST | Combo Adaptive Regime V1 | Combo Adaptive | €9.919,86 | €-110,19 | 53 | 53 | 47,17% | 0,92 | €-2,08 | 5,38% |
| TEST | Doge Donchian 1H | Donchian breakout 20 barre | €9.911,95 | €-88,05 | 12 | 12 | 50,00% | 0,75 | €-7,34 | 3,08% |
| TEST | Combo Adaptive Quality7 V1 | Combo Adaptive | €9.898,22 | €-104,50 | 76 | 76 | 40,79% | 0,94 | €-1,38 | 8,88% |
| TEST | Combo Scanner | Combo Scanner | €9.897,57 | €-106,39 | 122 | 122 | 45,90% | 0,96 | €-0,87 | 11,38% |
| TEST | Combo Adaptive Quality7 Regime V1 | Combo Adaptive | €9.889,90 | €-109,66 | 37 | 37 | 43,24% | 0,88 | €-2,96 | 5,41% |
| TEST | Eth Ema 1H | Trend following EMA | €9.867,74 | €-133,67 | 17 | 17 | 41,18% | 0,77 | €-7,86 | 4,80% |
| TEST | Forza relativa 1H V2 | Forza relativa vs BTC V2 | €9.856,05 | €-207,15 | 105 | 100 | 41,90% | 0,93 | €-1,97 | 10,88% |
| TEST | Eth Adaptive 1H | Combo Adaptive | €9.844,63 | €-155,37 | 13 | 13 | 38,46% | 0,66 | €-11,95 | 3,14% |
| TEST | Evo Cand 1H Fast V3 Tp R200 3Ee5Afb4 | Momentum / breakout V3 Filtered | €9.837,38 | €-162,62 | 37 | 37 | 40,54% | 0,76 | €-4,40 | 3,08% |
| TEST | Sol Bollinger 1H | Bollinger mean reversion | €9.821,20 | €-178,80 | 11 | 11 | 36,36% | 0,61 | €-16,25 | 2,37% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R200 8346046B | Momentum / breakout V3 Filtered | €9.817,34 | €-182,66 | 24 | 24 | 41,67% | 0,64 | €-7,61 | 3,23% |
| TEST | Scanner Top5 Btc Guard V1 | Scanner Top 5 + forza BTC | €9.809,43 | €-195,93 | 100 | 100 | 41,00% | 0,92 | €-1,96 | 7,34% |
| TEST | 1H Fast Nohigh Cap75 Short Only V1 | Momentum / breakout | €9.779,10 | €-220,90 | 86 | 86 | 41,86% | 0,88 | €-2,57 | 7,10% |
| TEST | 1H Fast V3 No Esports V1 | Momentum / breakout V3 Filtered | €9.778,68 | €-232,40 | 201 | 201 | 43,78% | 0,94 | €-1,16 | 9,00% |
| TEST | Evo Cand 1H Fast V3 Nohigh V1 Tp R250 C467005A | Momentum / breakout V3 Filtered | €9.762,18 | €-237,82 | 7 | 7 | 14,29% | 0,02 | €-33,97 | 2,82% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R200 751E55C4 | Momentum / breakout V3 Filtered | €9.723,72 | €-276,28 | 31 | 31 | 32,26% | 0,62 | €-8,91 | 4,83% |
| TEST | 1H Balanced Long No Rhv V1 | Confluenza trend | €9.717,62 | €-282,52 | 93 | 93 | 46,24% | 0,86 | €-3,04 | 9,26% |
| TEST | Eth Bollinger 1H | Bollinger mean reversion | €9.703,71 | €-296,29 | 7 | 7 | 28,57% | 0,22 | €-42,33 | 4,16% |
| TEST | Scanner Top5 Btc Btc 2 3 V1 | Scanner Top 5 + forza BTC | €9.693,56 | €-341,98 | 18 | 18 | 27,78% | 0,42 | €-19,00 | 5,46% |
| TEST | Eth Donchian 1H | Donchian breakout 20 barre | €9.678,07 | €-321,93 | 13 | 13 | 23,08% | 0,47 | €-24,76 | 3,44% |
| TEST | Scanner Top5 Btc Mfe V1 | Scanner Top 5 + forza BTC | €9.670,97 | €-332,89 | 110 | 110 | 45,45% | 0,85 | €-3,03 | 12,28% |
| TEST | 1H Fast V3 Long Only V1 | Momentum / breakout V3 Filtered | €9.640,32 | €-346,95 | 158 | 158 | 41,77% | 0,90 | €-2,20 | 12,52% |
| TEST | Global Confluence puro 1H | Global Confluence puro | €9.628,04 | €-371,96 | 16 | 16 | 25,00% | 0,32 | €-23,25 | 3,92% |
| TEST | 1H Balanced V3 Long Only V1 | Confluenza trend V3 Filtered | €9.584,43 | €-461,37 | 103 | 103 | 43,69% | 0,77 | €-4,48 | 8,85% |
| TEST | Scanner Top5 Btc Guard Mfe V1 | Scanner Top 5 + forza BTC | €9.581,30 | €-423,94 | 117 | 117 | 41,88% | 0,84 | €-3,62 | 8,78% |
| TEST | Evo Cand 1H Fast V3 Long Only V1 Tp R250 Bfc04Ed6 | Momentum / breakout V3 Filtered | €9.579,83 | €-420,17 | 11 | 11 | 0,00% | 0,00 | €-38,20 | 4,20% |
| TEST | Bilanciata 1H V2 | Confluenza trend V2 | €9.534,71 | €-468,75 | 101 | 93 | 43,56% | 0,78 | €-4,64 | 8,84% |
| TEST | Scanner Top5 Btc Guard Btc Le3 V1 | Scanner Top 5 + forza BTC | €9.523,77 | €-507,05 | 64 | 64 | 39,06% | 0,74 | €-7,92 | 7,99% |
| TEST | 1H Fast V3 Long Nohigh Cap75 V1 | Momentum / breakout V3 Filtered | €9.517,55 | €-482,45 | 78 | 78 | 39,74% | 0,78 | €-6,19 | 6,59% |
| TEST | Combo Trend | Combo Trend | €9.471,55 | €-557,05 | 150 | 150 | 39,33% | 0,84 | €-3,71 | 10,85% |
| TEST | 1H Fast V3 Nohigh V1 | Momentum / breakout V3 Filtered | €9.435,38 | €-564,62 | 112 | 112 | 40,18% | 0,79 | €-5,04 | 6,91% |
| TEST | 1H Fast Score 6 75 V1 | Momentum / breakout | €9.415,87 | €-584,13 | 137 | 137 | 40,15% | 0,84 | €-4,26 | 12,33% |
| TEST | Scanner Bottom10 Short | Scanner Bottom10 Short | €9.398,18 | €-677,79 | 70 | 70 | 31,43% | 0,65 | €-9,68 | 8,91% |
| TEST | Scanner Bottom15 Short | Scanner Bottom15 Short | €9.398,18 | €-677,79 | 70 | 70 | 31,43% | 0,65 | €-9,68 | 8,91% |
| TEST | Scanner Bottom20 Short | Scanner Bottom20 Short | €9.398,18 | €-677,79 | 70 | 70 | 31,43% | 0,65 | €-9,68 | 8,91% |
| TEST | 1H Fast V3 Long Nohigh Cap75 Lock V1 | Momentum / breakout V3 Filtered | €9.389,68 | €-610,32 | 83 | 83 | 44,58% | 0,76 | €-7,35 | 7,69% |
| TEST | Master Adaptive Runner25 V1 | Master Adaptive Consensus | €9.377,78 | €-621,78 | 51 | 51 | 31,37% | 0,66 | €-12,19 | 8,18% |
| TEST | Master Adaptive Gb20 Be V1 | Master Adaptive Consensus | €9.372,49 | €-627,51 | 55 | 55 | 29,09% | 0,62 | €-11,41 | 8,39% |
| TEST | Master Adaptive Gb20 Partial V1 | Master Adaptive Consensus | €9.362,52 | €-637,48 | 50 | 50 | 34,00% | 0,60 | €-12,75 | 7,98% |
| TEST | Scanner Top5 Btc Guard Btc Le3 Mfe V1 | Scanner Top 5 + forza BTC | €9.357,83 | €-672,47 | 80 | 80 | 38,75% | 0,70 | €-8,41 | 7,27% |
| TEST | Master Adaptive No Alt V1 | Master Adaptive Consensus | €9.354,60 | €-645,40 | 58 | 58 | 34,48% | 0,67 | €-11,13 | 7,26% |
| TEST | Benchmark trend following EMA 1H | Trend following EMA | €9.352,96 | €-721,74 | 122 | 122 | 38,52% | 0,71 | €-5,92 | 12,31% |
| TEST | Scanner Bottom5 Short Mfe Trail V1 | Scanner Bottom 5 Short | €9.333,05 | €-742,38 | 61 | 61 | 31,15% | 0,58 | €-12,17 | 8,93% |
| TEST | Master Adaptive V1 | Master Adaptive Consensus | €9.326,30 | €-673,70 | 52 | 52 | 32,69% | 0,62 | €-12,96 | 7,80% |
| TEST | Scanner Bottom5 Short Profit Lock V1 | Scanner Bottom 5 Short | €9.318,86 | €-756,47 | 62 | 62 | 30,65% | 0,56 | €-12,20 | 8,93% |
| TEST | Master Adaptive Expanded V1 | Master Adaptive Consensus | €9.317,58 | €-679,95 | 61 | 61 | 34,43% | 0,66 | €-11,15 | 7,96% |
| TEST | Master Adaptive Gb20 Loss Cap V1 | Master Adaptive Consensus | €9.249,86 | €-747,69 | 42 | 42 | 23,81% | 0,53 | €-17,80 | 11,41% |
| TEST | Scanner Bottom 5 Short 1H | Scanner Bottom 5 Short | €9.247,14 | €-827,60 | 89 | 89 | 31,46% | 0,64 | €-9,30 | 10,02% |
| TEST | Scanner Top5 Btc Btc Le3 V1 | Scanner Top 5 + forza BTC | €9.220,07 | €-813,73 | 64 | 64 | 34,38% | 0,56 | €-12,71 | 11,72% |
| TEST | Combo Adaptive Mfe Trail | Combo Adaptive | €9.205,93 | €-828,61 | 153 | 153 | 41,18% | 0,73 | €-5,42 | 15,45% |
| TEST | Master Adaptive Gb20 V1 | Master Adaptive Consensus | €9.202,39 | €-797,61 | 87 | 87 | 48,28% | 0,60 | €-9,17 | 9,02% |
| TEST | 1H Fast Score 6 75 No Trend Up V1 | Momentum / breakout | €9.165,52 | €-834,48 | 95 | 95 | 41,05% | 0,72 | €-8,78 | 12,64% |
| TEST | Bilanciata 1H V1 | Confluenza trend | €9.150,69 | €-849,31 | 121 | 121 | 36,36% | 0,69 | €-7,02 | 13,99% |
| TEST | 1H Fast V3 Cap75 V1 | Momentum / breakout V3 Filtered | €9.106,22 | €-893,78 | 136 | 136 | 36,03% | 0,75 | €-6,57 | 14,10% |
| TEST | Master Adaptive Strict3 V1 | Master Adaptive Consensus | €9.056,84 | €-943,16 | 53 | 53 | 28,30% | 0,59 | €-17,80 | 11,51% |
| TEST | Combo Mean Reversion | Combo Mean Reversion | €9.029,57 | €-982,88 | 42 | 42 | 35,71% | 0,46 | €-23,40 | 11,62% |
| TEST | Combo Adaptive Runner25 V1 | Combo Adaptive | €8.964,11 | €-1.035,89 | 94 | 94 | 30,85% | 0,53 | €-11,02 | 12,67% |
| TEST | Combo Adaptive Tp3 V1 | Combo Adaptive | €8.796,64 | €-1.203,36 | 75 | 75 | 29,33% | 0,38 | €-16,04 | 12,67% |
| TEST | Benchmark Bollinger mean reversion 1H | Bollinger mean reversion | €8.740,52 | €-1.259,48 | 81 | 81 | 38,27% | 0,55 | €-15,55 | 14,60% |
| TEST | Forza relativa 1H V1 | Forza relativa vs BTC V1 | €8.445,51 | €-1.554,49 | 105 | 105 | 27,62% | 0,47 | €-14,80 | 17,39% |

**Eventi indip.** conta gli eventi di mercato distinti; varianti dello stesso movimento restano collegate allo stesso evento sperimentale.

## Posizioni aperte

| Portafoglio | Asset | Lato | Metodo | TF | Leva | Entry | Mark | Stop | Liquidazione | Target | Margine | Esposizione | Rischio stop | P&L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principale 4H | SPCX | LONG | Confluenza trend | 240m | 3,0x | 136,56189 | 136,56189 | 128,79610 | 91,72407 | 152,09346 | €285,50 | €856,50 | €48,71 | €0,00 |
| Principale 4H | VELVET | LONG | Confluenza trend | 240m | 3,0x | 0,55987 | 0,14726 | 0,49269 | 0,37605 | 0,69424 | €131,08 | €393,24 | €47,19 | €-289,81 |
| Principale 4H | EDEN | LONG | Confluenza trend | 240m | 3,0x | 0,06195 | 0,06195 | 0,05451 | 0,04161 | 0,07681 | €130,34 | €391,02 | €46,92 | €0,00 |
| Principale 4H | TRUMP | LONG | Confluenza trend | 240m | 3,0x | 2,46049 | 2,46049 | 2,16523 | 1,65263 | 3,05101 | €134,98 | €404,95 | €48,59 | €0,00 |
| Principale 4H | XRP | LONG | Confluenza trend | 240m | 3,0x | 1,46057 | 1,51986 | 1,30460 | 0,98102 | 1,77252 | €8,58 | €25,73 | €2,75 | €1,04 |
| Principale 4H | HYPE | LONG | Confluenza trend | 240m | 3,0x | 78,87277 | 81,10800 | 73,04357 | 52,97621 | 90,53117 | €8,52 | €25,56 | €1,89 | €0,72 |
| 1H Balanced Long No Rhv V1 | SKHYNIX | LONG | Confluenza trend | 60m | 3,0x | 1214,11277 | 1214,11277 | 1170,18211 | 815,47908 | 1301,97411 | €413,43 | €1.240,28 | €44,88 | €0,00 |
| 1H Balanced Long No Rhv V1 | BOME | LONG | Confluenza trend | 60m | 3,0x | 0,00129 | 0,00129 | 0,00114 | 0,00087 | 0,00160 | €134,98 | €404,95 | €48,59 | €0,00 |
| 1H Balanced Long No Rhv V1 | TAO | LONG | Confluenza trend | 60m | 3,0x | 247,38947 | 247,38947 | 237,94346 | 166,16326 | 266,28148 | €428,20 | €1.284,61 | €49,05 | €0,00 |
| 1H Balanced Long No Rhv V1 | PEPE | LONG | Confluenza trend | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €21,51 | €64,54 | €5,62 | €0,59 |
| 1H Balanced Long No Rhv V1 | BTC | LONG | Confluenza trend | 60m | 3,0x | 79476,50212 | 80459,88000 | 79941,98781 | 53381,71726 | 82107,82923 | €8,35 | €25,04 | €0,00 | €0,31 |
| 1H Balanced Long No Rhv V1 | ETH | LONG | Confluenza trend | 60m | 3,0x | 2496,21914 | 2498,90000 | 2449,86508 | 1676,62719 | 2588,92725 | €820,95 | €2.462,84 | €45,73 | €2,65 |
| Bilanciata 1H V2 | SKHYNIX | LONG | Confluenza trend V2 | 60m | 3,0x | 1214,11277 | 1214,11277 | 1170,18211 | 815,47908 | 1301,97411 | €422,38 | €1.267,15 | €45,85 | €0,00 |
| Bilanciata 1H V2 | PEPE | LONG | Confluenza trend V2 | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €184,87 | €554,60 | €48,28 | €5,06 |
| Bilanciata 1H V3 Filtered | SKHYNIX | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1220,85412 | 1220,85412 | 1177,63561 | 820,00702 | 1307,29117 | €460,42 | €1.381,27 | €48,90 | €0,00 |
| Bilanciata 1H V3 Filtered | ZEC | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 807,93155 | 851,02000 | 737,89694 | 542,66069 | 948,00078 | €195,29 | €585,88 | €50,79 | €31,25 |
| Bilanciata 1H V3 Filtered | XRP | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1,47399 | 1,51986 | 1,35380 | 0,99003 | 1,71438 | €205,84 | €617,51 | €50,35 | €19,21 |
| Bilanciata 1H V3 Filtered | PEPE | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €8,77 | €26,32 | €2,02 | €1,31 |
| Bilanciata 1H V3 Filtered | PUMP | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,00523 | 0,00523 | 0,00479 | 0,00351 | 0,00611 | €197,24 | €591,72 | €49,81 | €0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | BTW | LONG | Momentum / breakout | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €8,91 | €26,72 | €3,13 | €0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00086 | 0,00146 | €215,92 | €647,76 | €57,03 | €0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | NEAR | LONG | Momentum / breakout | 60m | 3,0x | 2,08142 | 2,08142 | 2,02315 | 1,39802 | 2,16882 | €42,86 | €128,59 | €3,60 | €0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | XRP | LONG | Momentum / breakout | 60m | 3,0x | 1,47399 | 1,51986 | 1,38051 | 0,99003 | 1,61422 | €284,39 | €853,18 | €54,11 | €26,55 |
| 1H Fast Score 6 75 Cost Aware V1 | PUMP | LONG | Momentum / breakout | 60m | 3,0x | 0,00523 | 0,00523 | 0,00489 | 0,00351 | 0,00574 | €260,23 | €780,70 | €51,11 | €0,00 |
| 1H Fast Score 6 75 Cost Aware V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14742 | 0,14726 | 0,16511 | 0,19582 | 0,12088 | €157,13 | €471,39 | €56,57 | €0,51 |
| 1H Fast Score 6 75 Cost Aware V1 | SOL | LONG | Momentum / breakout | 60m | 3,0x | 100,45609 | 101,76000 | 98,13142 | 67,47301 | 103,94309 | €14,87 | €44,62 | €1,03 | €0,58 |
| 1H Fast Long Btc 1 3 Cap75 V1 | XRP | LONG | Momentum / breakout | 60m | 3,0x | 1,49738 | 1,51986 | 1,40463 | 1,00574 | 1,63650 | €272,47 | €817,41 | €50,63 | €12,27 |
| 1H Fast Long Btc 1 3 Cap75 V1 | DOGE | LONG | Momentum / breakout | 60m | 3,0x | 0,09162 | 0,09232 | 0,08782 | 0,06154 | 0,09732 | €406,05 | €1.218,14 | €50,55 | €9,33 |
| 1H Fast Long Btc 1 3 Cap75 V1 | PUMP | LONG | Momentum / breakout | 60m | 3,0x | 0,00516 | 0,00516 | 0,00489 | 0,00347 | 0,00557 | €9,37 | €28,12 | €1,47 | €0,00 |
| 1H Fast No Pepe V1 | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €172,22 | €516,67 | €49,86 | €0,00 |
| 1H Fast No Pepe V1 | TAO | LONG | Momentum / breakout | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €47,93 | €143,78 | €4,27 | €0,00 |
| 1H Fast No Pepe V1 | XRP | LONG | Momentum / breakout | 60m | 3,0x | 1,49835 | 1,51986 | 1,43358 | 1,00639 | 1,59551 | €415,25 | €1.245,74 | €53,85 | €17,88 |
| 1H Fast No Pepe V1 | PUMP | LONG | Momentum / breakout | 60m | 3,0x | 0,00515 | 0,00515 | 0,00480 | 0,00346 | 0,00567 | €266,74 | €800,21 | €53,85 | €0,00 |
| 1H Fast No Pepe V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,14742 | 0,14726 | 0,16511 | 0,19582 | 0,12088 | €136,27 | €408,80 | €49,06 | €0,45 |
| 1H Fast No Pepe V1 | SOL | LONG | Momentum / breakout | 60m | 3,0x | 102,05441 | 101,76000 | 99,81063 | 68,54654 | 105,42008 | €8,75 | €26,26 | €0,58 | €-0,08 |
| 1H Fast No Pepe V1 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04446 | 0,04309 | 0,04980 | 0,05906 | 0,03646 | €9,48 | €28,43 | €3,41 | €0,88 |
| 1H Fast Tp2 V1 | BTW | LONG | Momentum / breakout | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,56752 | €142,85 | €428,56 | €50,25 | €0,00 |
| 1H Fast Tp2 V1 | BOME | LONG | Momentum / breakout | 60m | 3,0x | 0,00132 | 0,00132 | 0,00119 | 0,00088 | 0,00158 | €18,87 | €56,62 | €5,59 | €0,00 |
| 1H Fast Tp2 V1 | DOGE | LONG | Momentum / breakout | 60m | 3,0x | 0,09162 | 0,09232 | 0,08782 | 0,06154 | 0,09922 | €9,51 | €28,53 | €1,18 | €0,22 |
| 1H Fast Tp2 V1 | PUMP | LONG | Momentum / breakout | 60m | 3,0x | 0,00515 | 0,00515 | 0,00484 | 0,00346 | 0,00576 | €261,16 | €783,47 | €46,57 | €0,00 |
| 1H Fast Tp2 V1 | VELVET | SHORT | Momentum / breakout | 60m | 3,0x | 0,17246 | 0,14726 | 0,17246 | 0,22908 | 0,13107 | €139,71 | €419,14 | €0,00 | €61,24 |
| 1H Fast Tp2 V1 | TUT | SHORT | Momentum / breakout | 60m | 3,0x | 0,04446 | 0,04309 | 0,04980 | 0,05906 | 0,03379 | €141,13 | €423,40 | €50,81 | €13,06 |
| 1H Fast Tp2 V1 | ZEC | LONG | Momentum / breakout | 60m | 3,0x | 851,19020 | 851,02000 | 823,36650 | 571,71609 | 906,83762 | €24,68 | €74,03 | €2,42 | €-0,01 |
| Rapida 1H V3 Filtered | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €172,00 | €515,99 | €49,79 | €0,00 |
| Rapida 1H V3 Filtered | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €589,98 | €1.769,95 | €52,56 | €0,00 |
| Rapida 1H V3 Filtered | PUMP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00522 | 0,00522 | 0,00488 | 0,00351 | 0,00573 | €262,56 | €787,69 | €51,10 | €0,00 |
| Rapida 1H V3 Filtered | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14742 | 0,14726 | 0,16511 | 0,19582 | 0,12088 | €140,02 | €420,06 | €50,41 | €0,46 |
| Rapida 1H V3 Filtered | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04446 | 0,04309 | 0,04980 | 0,05906 | 0,03646 | €16,99 | €50,96 | €6,11 | €1,57 |
| 1H Fast V3 Long Only V1 | BTW | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €126,57 | €379,72 | €44,52 | €0,00 |
| 1H Fast V3 Long Only V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00147 | €9,56 | €28,69 | €2,66 | €0,00 |
| 1H Fast V3 Long Only V1 | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €554,42 | €1.663,26 | €49,39 | €0,00 |
| 1H Fast V3 Long Only V1 | PUMP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00522 | 0,00522 | 0,00488 | 0,00351 | 0,00573 | €229,21 | €687,62 | €44,60 | €0,00 |
| 1H Fast V3 Long Only V1 | XRP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 1,52803 | 1,51986 | 1,48824 | 1,02632 | 1,58771 | €599,35 | €1.798,06 | €46,82 | €-9,61 |
| 1H Fast V3 Long Only V1 | BTC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 80475,97198 | 80459,88000 | 79500,84060 | 54053,02784 | 81938,66944 | €132,39 | €397,17 | €4,81 | €-0,08 |
| 1H Fast V3 No Esports V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €169,36 | €508,09 | €49,03 | €0,00 |
| 1H Fast V3 No Esports V1 | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €27,04 | €81,13 | €2,41 | €0,00 |
| 1H Fast V3 No Esports V1 | PUMP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00522 | 0,00522 | 0,00488 | 0,00351 | 0,00573 | €252,96 | €758,88 | €49,23 | €0,00 |
| 1H Fast V3 No Esports V1 | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14742 | 0,14726 | 0,16511 | 0,19582 | 0,12088 | €133,96 | €401,88 | €48,23 | €0,44 |
| 1H Fast V3 No Esports V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04446 | 0,04309 | 0,04980 | 0,05906 | 0,03646 | €129,73 | €389,20 | €46,70 | €12,00 |
| 1H Fast V3 No Esports Long Only V1 | BTW | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,45972 | 0,45972 | 0,40581 | 0,30878 | 0,54057 | €132,94 | €398,81 | €46,76 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00147 | €10,06 | €30,18 | €2,80 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | PUMP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00522 | 0,00522 | 0,00488 | 0,00351 | 0,00573 | €249,75 | €749,26 | €48,60 | €0,00 |
| 1H Fast V3 No Esports Long Only V1 | BTC | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 80355,23783 | 80459,88000 | 79356,94052 | 53971,93475 | 81852,68421 | €1.345,04 | €4.035,12 | €50,13 | €5,25 |
| 1H Fast V3 No Esports Mfe Lock V1 | BOME | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00129 | 0,00129 | 0,00117 | 0,00087 | 0,00148 | €173,11 | €519,32 | €50,11 | €0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | TAO | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 247,38947 | 247,38947 | 240,04257 | 166,16326 | 258,40981 | €593,79 | €1.781,38 | €52,90 | €0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | PUMP | LONG | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,00522 | 0,00522 | 0,00488 | 0,00351 | 0,00573 | €264,26 | €792,79 | €51,43 | €0,00 |
| 1H Fast V3 No Esports Mfe Lock V1 | VELVET | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,14742 | 0,14726 | 0,16511 | 0,19582 | 0,12088 | €140,93 | €422,78 | €50,73 | €0,46 |
| 1H Fast V3 No Esports Mfe Lock V1 | TUT | SHORT | Momentum / breakout V3 Filtered | 60m | 3,0x | 0,04446 | 0,04309 | 0,04980 | 0,05906 | 0,03646 | €17,09 | €51,28 | €6,15 | €1,58 |
| Ampia 4H | SPCX | LONG | Confluenza trend | 240m | 2,0x | 136,56189 | 136,56189 | 126,46637 | 68,96375 | 164,82935 | €323,86 | €647,73 | €47,88 | €0,00 |
| Ampia 4H | VELVET | LONG | Confluenza trend | 240m | 2,0x | 0,55987 | 0,14726 | 0,49269 | 0,28274 | 0,74799 | €201,63 | €403,26 | €48,39 | €-297,19 |
| Ampia 4H | LINK | LONG | Confluenza trend | 240m | 2,0x | 11,96839 | 11,96839 | 11,08055 | 6,04404 | 14,45436 | €14,07 | €28,15 | €2,09 | €0,00 |
| Ampia 4H | SUI | LONG | Confluenza trend | 240m | 2,0x | 0,86357 | 0,82350 | 0,75994 | 0,43610 | 1,15373 | €215,46 | €430,92 | €51,71 | €-20,00 |
| Ampia 4H | ETH | LONG | Confluenza trend | 240m | 2,0x | 2430,03591 | 2498,90000 | 2267,54364 | 1227,16813 | 2885,01426 | €18,82 | €37,65 | €2,52 | €1,07 |
| Ampia 4H | HYPE | LONG | Confluenza trend | 240m | 2,0x | 79,31286 | 81,10800 | 70,73982 | 40,05299 | 103,31737 | €13,82 | €27,64 | €2,99 | €0,63 |
| Ampia 4H | TRUMP | LONG | Confluenza trend | 240m | 2,0x | 2,37347 | 2,37347 | 2,08866 | 1,19860 | 3,17096 | €210,83 | €421,66 | €50,60 | €0,00 |
| Forza relativa 1H V2 | BEAT | SHORT | Forza relativa vs BTC V2 | 60m | 2,0x | 0,25984 | 0,25984 | 0,25657 | 0,38847 | 0,19125 | €200,38 | €400,75 | €0,00 | €-0,00 |
| Forza relativa 1H V2 | PEPE | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €286,19 | €572,37 | €49,83 | €5,22 |
| Forza relativa 1H V2 | PUMP | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 0,00510 | 0,00510 | 0,00476 | 0,00258 | 0,00586 | €356,70 | €713,40 | €47,79 | €0,00 |
| Forza relativa 1H V2 | SOL | LONG | Forza relativa vs BTC V2 | 60m | 2,0x | 98,65773 | 101,76000 | 100,09761 | 49,82215 | 104,16036 | €963,68 | €1.927,37 | €0,00 | €60,61 |
| Benchmark Donchian breakout 1H | SKHYNIX | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1174,33482 | 1174,33482 | 1128,44989 | 593,03908 | 1289,04713 | €641,25 | €1.282,50 | €50,11 | €0,00 |
| Benchmark Donchian breakout 1H | PUMP | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,00522 | 0,00522 | 0,00474 | 0,00264 | 0,00643 | €312,08 | €624,15 | €57,84 | €0,00 |
| Benchmark Donchian breakout 1H | VELVET | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,14787 | 0,14726 | 0,16561 | 0,22107 | 0,10351 | €237,23 | €474,47 | €56,94 | €1,96 |
| Benchmark Donchian breakout 1H | SOL | LONG | Donchian breakout 20 barre | 60m | 2,0x | 98,65773 | 101,76000 | 99,95358 | 49,82215 | 105,60549 | €1.006,88 | €2.013,76 | €0,00 | €63,32 |
| Benchmark Donchian breakout 1H | BTC | LONG | Donchian breakout 20 barre | 60m | 2,0x | 80839,33463 | 80459,88000 | 79396,75347 | 40823,86399 | 84445,78834 | €211,17 | €422,35 | €7,54 | €-1,98 |
| Donchian 1H Gb20 120R V1 | SKHYNIX | LONG | Donchian breakout 20 barre | 60m | 2,0x | 1174,33482 | 1174,33482 | 1128,44989 | 593,03908 | 1289,04713 | €626,15 | €1.252,30 | €48,93 | €0,00 |
| Donchian 1H Gb20 120R V1 | PUMP | LONG | Donchian breakout 20 barre | 60m | 2,0x | 0,00522 | 0,00522 | 0,00474 | 0,00264 | 0,00643 | €304,73 | €609,46 | €56,48 | €0,00 |
| Donchian 1H Gb20 120R V1 | VELVET | SHORT | Donchian breakout 20 barre | 60m | 2,0x | 0,14787 | 0,14726 | 0,16561 | 0,22107 | 0,10351 | €231,65 | €463,30 | €55,60 | €1,91 |
| Donchian 1H Gb20 120R V1 | SOL | LONG | Donchian breakout 20 barre | 60m | 2,0x | 98,65773 | 101,76000 | 99,95358 | 49,82215 | 105,60549 | €983,17 | €1.966,35 | €0,00 | €61,83 |
| Donchian 1H Gb20 120R V1 | BTC | LONG | Donchian breakout 20 barre | 60m | 2,0x | 80839,33463 | 80459,88000 | 79396,75347 | 40823,86399 | 84445,78834 | €206,20 | €412,40 | €7,36 | €-1,94 |
| Benchmark trend following EMA 1H | BEAT | SHORT | Trend following EMA | 60m | 2,0x | 0,28257 | 0,28257 | 0,25706 | 0,42244 | 0,20797 | €186,11 | €372,23 | €0,00 | €-0,00 |
| Benchmark trend following EMA 1H | SOL | LONG | Trend following EMA | 60m | 2,0x | 95,05001 | 101,76000 | 98,17475 | 48,00025 | 106,18327 | €434,46 | €868,92 | €0,00 | €61,34 |
| Benchmark trend following EMA 1H | ZEC | LONG | Trend following EMA | 60m | 2,0x | 807,93155 | 851,02000 | 730,11531 | 408,00543 | 979,12728 | €17,42 | €34,84 | €3,36 | €1,86 |
| Benchmark trend following EMA 1H | ETH | LONG | Trend following EMA | 60m | 2,0x | 2495,82907 | 2498,90000 | 2437,60814 | 1260,39368 | 2623,91511 | €980,54 | €1.961,08 | €45,75 | €2,41 |
| Benchmark trend following EMA 1H | TUT | SHORT | Trend following EMA | 60m | 2,0x | 0,04446 | 0,04309 | 0,04980 | 0,06647 | 0,03272 | €194,70 | €389,39 | €46,73 | €12,01 |
| Scanner Top 5 Long 1H | BOME | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00160 | €218,24 | €436,47 | €52,38 | €0,00 |
| Scanner Top 5 Long 1H | PEPE | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €322,02 | €644,04 | €56,06 | €5,87 |
| Scanner Top 5 Long 1H | PUMP | LONG | Scanner Top 5 Long | 60m | 2,0x | 0,00502 | 0,00502 | 0,00460 | 0,00254 | 0,00587 | €316,31 | €632,61 | €53,01 | €0,00 |
| Scanner Top 5 Long 1H | TRUMP | LONG | Scanner Top 5 Long | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,08367 | €238,89 | €477,78 | €55,13 | €0,00 |
| Scanner Top 5 Long 1H | ETH | LONG | Scanner Top 5 Long | 60m | 2,0x | 2496,21914 | 2498,90000 | 2449,86508 | 1260,59067 | 2588,92725 | €109,04 | €218,08 | €4,05 | €0,23 |
| Scanner Bottom 5 Short 1H | SOXL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €378,86 | €757,72 | €48,07 | €-0,00 |
| Scanner Bottom 5 Short 1H | SNDK | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €492,80 | €985,60 | €47,71 | €-0,00 |
| Scanner Bottom 5 Short 1H | VELVET | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,17246 | 0,14726 | 0,17246 | 0,25782 | 0,13107 | €191,07 | €382,14 | €0,00 | €55,83 |
| Scanner Bottom 5 Short 1H | TUT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,04570 | 0,04309 | 0,05118 | 0,06832 | 0,03473 | €178,38 | €356,76 | €42,81 | €20,38 |
| Scanner Top10 Long | TAO | LONG | Scanner Top10 Long | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €678,43 | €1.356,86 | €51,81 | €0,00 |
| Scanner Top10 Long | PEPE | LONG | Scanner Top10 Long | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €288,77 | €577,53 | €50,27 | €5,26 |
| Scanner Top10 Long | BTC | LONG | Scanner Top10 Long | 60m | 2,0x | 79476,50212 | 80459,88000 | 79941,98781 | 40135,63357 | 82107,82923 | €1.566,56 | €3.133,13 | €0,00 | €38,77 |
| Scanner Top10 Long | ETH | LONG | Scanner Top10 Long | 60m | 2,0x | 2496,21914 | 2498,90000 | 2449,86508 | 1260,59067 | 2588,92725 | €1.395,14 | €2.790,29 | €51,81 | €3,00 |
| Scanner Top10 Long | SOL | LONG | Scanner Top10 Long | 60m | 2,0x | 101,35627 | 101,76000 | 98,29373 | 51,18491 | 107,48134 | €47,69 | €95,37 | €2,88 | €0,38 |
| Scanner Bottom10 Short | SOXL | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom10 Short | SNDK | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Bottom10 Short | VELVET | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,17246 | 0,14726 | 0,17246 | 0,25782 | 0,13107 | €194,19 | €388,38 | €0,00 | €56,74 |
| Scanner Bottom10 Short | TUT | SHORT | Scanner Bottom10 Short | 60m | 2,0x | 0,04570 | 0,04309 | 0,05118 | 0,06832 | 0,03473 | €181,31 | €362,61 | €43,51 | €20,72 |
| Scanner Top15 Long | NEAR | LONG | Scanner Top15 Long | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €16,79 | €33,59 | €1,21 | €0,00 |
| Scanner Top15 Long | TAO | LONG | Scanner Top15 Long | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €88,53 | €177,07 | €6,76 | €0,00 |
| Scanner Top15 Long | PEPE | LONG | Scanner Top15 Long | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €291,03 | €582,05 | €50,67 | €5,31 |
| Scanner Top15 Long | PUMP | LONG | Scanner Top15 Long | 60m | 2,0x | 0,00502 | 0,00502 | 0,00460 | 0,00254 | 0,00587 | €291,59 | €583,18 | €48,87 | €0,00 |
| Scanner Top15 Long | TRUMP | LONG | Scanner Top15 Long | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,08367 | €215,87 | €431,75 | €49,81 | €0,00 |
| Scanner Top15 Long | BTC | LONG | Scanner Top15 Long | 60m | 2,0x | 79476,50212 | 80459,88000 | 79941,98781 | 40135,63357 | 82107,82923 | €100,15 | €200,30 | €0,00 | €2,48 |
| Scanner Top15 Long | ETH | LONG | Scanner Top15 Long | 60m | 2,0x | 2493,81866 | 2498,90000 | 2436,64076 | 1259,37843 | 2608,17446 | €837,36 | €1.674,71 | €38,40 | €3,41 |
| Scanner Bottom15 Short | SOXL | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom15 Short | SNDK | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Bottom15 Short | VELVET | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,17246 | 0,14726 | 0,17246 | 0,25782 | 0,13107 | €194,19 | €388,38 | €0,00 | €56,74 |
| Scanner Bottom15 Short | TUT | SHORT | Scanner Bottom15 Short | 60m | 2,0x | 0,04570 | 0,04309 | 0,05118 | 0,06832 | 0,03473 | €181,31 | €362,61 | €43,51 | €20,72 |
| Scanner Top20 Long | NEAR | LONG | Scanner Top20 Long | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €16,79 | €33,59 | €1,21 | €0,00 |
| Scanner Top20 Long | TAO | LONG | Scanner Top20 Long | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €88,53 | €177,07 | €6,76 | €0,00 |
| Scanner Top20 Long | PEPE | LONG | Scanner Top20 Long | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €291,03 | €582,05 | €50,67 | €5,31 |
| Scanner Top20 Long | PUMP | LONG | Scanner Top20 Long | 60m | 2,0x | 0,00502 | 0,00502 | 0,00460 | 0,00254 | 0,00587 | €291,59 | €583,18 | €48,87 | €0,00 |
| Scanner Top20 Long | TRUMP | LONG | Scanner Top20 Long | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,08367 | €215,87 | €431,75 | €49,81 | €0,00 |
| Scanner Top20 Long | BTC | LONG | Scanner Top20 Long | 60m | 2,0x | 79476,50212 | 80459,88000 | 79941,98781 | 40135,63357 | 82107,82923 | €100,15 | €200,30 | €0,00 | €2,48 |
| Scanner Top20 Long | ETH | LONG | Scanner Top20 Long | 60m | 2,0x | 2493,81866 | 2498,90000 | 2436,64076 | 1259,37843 | 2608,17446 | €837,36 | €1.674,71 | €38,40 | €3,41 |
| Scanner Bottom20 Short | SOXL | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €385,05 | €770,10 | €48,86 | €-0,00 |
| Scanner Bottom20 Short | SNDK | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €500,82 | €1.001,64 | €48,49 | €-0,00 |
| Scanner Bottom20 Short | VELVET | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,17246 | 0,14726 | 0,17246 | 0,25782 | 0,13107 | €194,19 | €388,38 | €0,00 | €56,74 |
| Scanner Bottom20 Short | TUT | SHORT | Scanner Bottom20 Short | 60m | 2,0x | 0,04570 | 0,04309 | 0,05118 | 0,06832 | 0,03473 | €181,31 | €362,61 | €43,51 | €20,72 |
| Scanner Top 5 + forza BTC 1H | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €203,45 | €406,91 | €48,83 | €0,00 |
| Scanner Top 5 + forza BTC 1H | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €300,64 | €601,28 | €52,34 | €5,48 |
| Scanner Top 5 + forza BTC 1H | PUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00502 | 0,00502 | 0,00460 | 0,00254 | 0,00595 | €295,30 | €590,60 | €49,49 | €0,00 |
| Scanner Top 5 + forza BTC 1H | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,14149 | €223,03 | €446,06 | €51,47 | €0,00 |
| Scanner Top 5 + forza BTC 1H | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 101,35627 | 101,76000 | 98,29373 | 51,18491 | 108,09385 | €69,28 | €138,55 | €4,19 | €0,55 |
| Scanner Top5 Btc Mfe V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €190,73 | €381,46 | €45,77 | €0,00 |
| Scanner Top5 Btc Mfe V1 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €281,84 | €563,67 | €49,07 | €5,14 |
| Scanner Top5 Btc Mfe V1 | PUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00502 | 0,00502 | 0,00460 | 0,00254 | 0,00595 | €276,83 | €553,66 | €46,39 | €0,00 |
| Scanner Top5 Btc Mfe V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,14149 | €209,08 | €418,16 | €48,25 | €0,00 |
| Scanner Top5 Btc Mfe V1 | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 101,35627 | 101,76000 | 98,29373 | 51,18491 | 108,09385 | €64,94 | €129,89 | €3,92 | €0,52 |
| Scanner Top5 Btc Guard V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €197,27 | €394,55 | €47,35 | €0,00 |
| Scanner Top5 Btc Guard V1 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €34,88 | €69,75 | €6,07 | €0,64 |
| Scanner Top5 Btc Guard V1 | PUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00502 | 0,00502 | 0,00460 | 0,00254 | 0,00595 | €276,09 | €552,19 | €46,27 | €0,00 |
| Scanner Top5 Btc Guard V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,55551 | 2,55551 | 2,29388 | 1,29053 | 3,13109 | €13,03 | €26,06 | €2,67 | €0,00 |
| Scanner Top5 Btc Guard V1 | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 101,35627 | 101,76000 | 98,29373 | 51,18491 | 108,09385 | €811,17 | €1.622,33 | €49,02 | €6,46 |
| Scanner Top5 Btc Btc Le3 V1 | XRP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,50701 | 1,51986 | 1,39078 | 0,76104 | 1,76273 | €297,64 | €595,28 | €45,91 | €5,08 |
| Scanner Top5 Btc Btc Le3 V1 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €298,93 | €597,86 | €44,42 | €30,23 |
| Scanner Top5 Btc Btc Le3 V1 | PUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00527 | 0,00527 | 0,00486 | 0,00266 | 0,00618 | €14,29 | €28,58 | €2,23 | €0,00 |
| Scanner Top5 Btc Btc 2 3 V1 | XRP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,50701 | 1,51986 | 1,39078 | 0,76104 | 1,76273 | €312,93 | €625,85 | €48,27 | €5,34 |
| Scanner Top5 Btc Btc 2 3 V1 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €314,28 | €628,56 | €46,70 | €31,78 |
| Scanner Top5 Btc Btc 2 3 V1 | PUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00527 | 0,00527 | 0,00486 | 0,00266 | 0,00618 | €15,02 | €30,05 | €2,35 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €192,69 | €385,37 | €46,24 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €34,07 | €68,13 | €5,93 | €0,62 |
| Scanner Top5 Btc Guard Mfe V1 | PUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00502 | 0,00502 | 0,00460 | 0,00254 | 0,00595 | €269,67 | €539,35 | €45,19 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,55551 | 2,55551 | 2,29388 | 1,29053 | 3,13109 | €12,72 | €25,45 | €2,61 | €0,00 |
| Scanner Top5 Btc Guard Mfe V1 | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 101,35627 | 101,76000 | 98,29373 | 51,18491 | 108,09385 | €792,30 | €1.584,60 | €47,88 | €6,31 |
| Scanner Top5 Btc Guard Btc Le3 V1 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €313,56 | €627,12 | €46,59 | €31,71 |
| Scanner Top5 Btc Guard Btc Le3 V1 | XRP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,49793 | 1,51986 | 1,40541 | 0,75645 | 1,70147 | €13,15 | €26,30 | €1,62 | €0,38 |
| Scanner Top5 Btc Guard Btc Le3 V1 | PUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00502 | 0,00502 | 0,00460 | 0,00254 | 0,00595 | €273,00 | €546,00 | €45,75 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 V1 | TRUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 2,55551 | 2,55551 | 2,29388 | 1,29053 | 3,13109 | €12,70 | €25,40 | €2,60 | €0,00 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €308,18 | €616,36 | €45,79 | €31,16 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | XRP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 1,49793 | 1,51986 | 1,40541 | 0,75645 | 1,70147 | €12,92 | €25,84 | €1,60 | €0,38 |
| Scanner Top5 Btc Guard Btc Le3 Mfe V1 | PUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00502 | 0,00502 | 0,00460 | 0,00254 | 0,00595 | €268,32 | €536,63 | €44,97 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00176 | €210,95 | €421,90 | €50,63 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 818,21361 | 851,02000 | 764,43439 | 413,19787 | 979,55127 | €17,50 | €35,00 | €2,30 | €1,40 |
| Scanner Top5 Btc Runner25 V1 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00001 | €303,79 | €607,58 | €52,89 | €5,54 |
| Scanner Top5 Btc Runner25 V1 | PUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00502 | 0,00502 | 0,00460 | 0,00254 | 0,00629 | €300,08 | €600,16 | €50,29 | €0,00 |
| Scanner Top5 Btc Runner25 V1 | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 101,35627 | 101,76000 | 98,29373 | 51,18491 | 110,54388 | €861,88 | €1.723,75 | €52,08 | €6,87 |
| Scanner Top5 Btc Tp3 V1 | BOME | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00176 | €211,07 | €422,14 | €50,66 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | ZEC | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 818,21361 | 851,02000 | 764,43439 | 413,19787 | 979,55127 | €17,51 | €35,02 | €2,30 | €1,40 |
| Scanner Top5 Btc Tp3 V1 | PEPE | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00001 | €303,97 | €607,94 | €52,92 | €5,54 |
| Scanner Top5 Btc Tp3 V1 | PUMP | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 0,00502 | 0,00502 | 0,00460 | 0,00254 | 0,00629 | €300,25 | €600,51 | €50,32 | €0,00 |
| Scanner Top5 Btc Tp3 V1 | SOL | LONG | Scanner Top 5 + forza BTC | 60m | 2,0x | 101,35627 | 101,76000 | 98,29373 | 51,18491 | 110,54388 | €862,38 | €1.724,76 | €52,11 | €6,87 |
| Combo Trend | BEAT | SHORT | Combo Trend | 60m | 2,0x | 0,25984 | 0,25984 | 0,25657 | 0,38847 | 0,19125 | €193,71 | €387,42 | €0,00 | €-0,00 |
| Combo Trend | ZEC | LONG | Combo Trend | 60m | 2,0x | 807,93155 | 851,02000 | 730,11531 | 408,00543 | 979,12728 | €247,61 | €495,23 | €47,70 | €26,41 |
| Combo Trend | PEPE | LONG | Combo Trend | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00001 | €246,56 | €493,12 | €47,70 | €4,50 |
| Combo Trend | PUMP | LONG | Combo Trend | 60m | 2,0x | 0,00498 | 0,00498 | 0,00455 | 0,00252 | 0,00595 | €266,27 | €532,54 | €46,71 | €0,00 |
| Combo Trend | BTC | LONG | Combo Trend | 60m | 2,0x | 80839,33463 | 80459,88000 | 79396,75347 | 40823,86399 | 84013,01416 | €27,80 | €55,60 | €0,99 | €-0,26 |
| Combo Mean Reversion | BTC | SHORT | Combo Mean Reversion | 60m | 2,0x | 80807,00537 | 80459,88000 | 81888,50855 | 120806,47302 | 79076,60011 | €1.684,34 | €3.368,67 | €45,09 | €14,47 |
| Combo Scanner | BOME | LONG | Combo Scanner | 60m | 2,0x | 0,00129 | 0,00129 | 0,00114 | 0,00065 | 0,00163 | €195,20 | €390,40 | €46,85 | €0,00 |
| Combo Scanner | PEPE | LONG | Combo Scanner | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €288,44 | €576,88 | €50,22 | €5,26 |
| Combo Scanner | PUMP | LONG | Combo Scanner | 60m | 2,0x | 0,00502 | 0,00502 | 0,00460 | 0,00254 | 0,00595 | €283,32 | €566,63 | €47,48 | €0,00 |
| Combo Scanner | TRUMP | LONG | Combo Scanner | 60m | 2,0x | 2,50550 | 2,50550 | 2,21642 | 1,26528 | 3,14149 | €213,98 | €427,96 | €49,38 | €0,00 |
| Combo Scanner | SOL | LONG | Combo Scanner | 60m | 2,0x | 101,35627 | 101,76000 | 98,29373 | 51,18491 | 108,09385 | €66,47 | €132,93 | €4,02 | €0,53 |
| Combo Adaptive | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,01735 | 121,01735 | 128,90956 | 180,92093 | 105,23292 | €367,30 | €734,61 | €47,91 | €-0,00 |
| Combo Adaptive | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €40,89 | €81,77 | €3,12 | €0,00 |
| Combo Adaptive | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 807,93155 | 851,02000 | 737,89694 | 408,00543 | 948,00078 | €307,94 | €615,88 | €53,39 | €32,85 |
| Combo Adaptive | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €306,63 | €613,26 | €53,38 | €5,59 |
| Combo Adaptive | PUMP | LONG | Combo Adaptive | 60m | 2,0x | 0,00520 | 0,00520 | 0,00478 | 0,00262 | 0,00604 | €329,34 | €658,69 | €53,47 | €0,00 |
| Combo Adaptive | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,52450 | 2,33981 | 1,27487 | 2,89389 | €18,69 | €37,37 | €2,73 | €0,00 |
| Combo Adaptive | BTC | LONG | Combo Adaptive | 60m | 2,0x | 80839,33463 | 80459,88000 | 79541,01127 | 40823,86399 | 83435,98137 | €39,76 | €79,52 | €1,28 | €-0,37 |
| Combo Adaptive Mfe Trail | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €54,29 | €108,58 | €4,15 | €0,00 |
| Combo Adaptive Mfe Trail | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €269,51 | €539,03 | €46,92 | €4,91 |
| Combo Adaptive Mfe Trail | XRP | LONG | Combo Adaptive | 60m | 2,0x | 1,49835 | 1,51986 | 1,41507 | 0,75667 | 1,66491 | €363,44 | €726,87 | €40,40 | €10,44 |
| Combo Adaptive Mfe Trail | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,52450 | 2,33981 | 1,27487 | 2,89389 | €315,75 | €631,50 | €46,20 | €0,00 |
| Combo Adaptive Mfe Trail | TUT | SHORT | Combo Adaptive | 60m | 2,0x | 0,04570 | 0,04309 | 0,05118 | 0,06832 | 0,03473 | €190,04 | €380,09 | €45,61 | €21,71 |
| Combo Adaptive Mfe Trail | BTC | LONG | Combo Adaptive | 60m | 2,0x | 80839,33463 | 80459,88000 | 79541,01127 | 40823,86399 | 83435,98137 | €21,40 | €42,79 | €0,69 | €-0,20 |
| Combo Adaptive Quality7 V1 | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €371,68 | €743,36 | €47,16 | €-0,00 |
| Combo Adaptive Quality7 V1 | TAO | LONG | Combo Adaptive | 60m | 2,0x | 247,38947 | 247,38947 | 237,94346 | 124,93168 | 266,28148 | €646,78 | €1.293,57 | €49,39 | €0,00 |
| Combo Adaptive Quality7 V1 | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €283,16 | €566,31 | €49,30 | €5,16 |
| Combo Adaptive Quality7 V1 | PUMP | LONG | Combo Adaptive | 60m | 2,0x | 0,00520 | 0,00520 | 0,00478 | 0,00262 | 0,00604 | €302,38 | €604,77 | €49,09 | €0,00 |
| Combo Adaptive Regime V1 | PUMP | LONG | Combo Adaptive | 60m | 2,0x | 0,00502 | 0,00502 | 0,00460 | 0,00254 | 0,00587 | €294,95 | €589,90 | €49,43 | €0,00 |
| Combo Adaptive Regime V1 | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €425,38 | €850,76 | €0,00 | €31,51 |
| Combo Adaptive Quality7 Regime V1 | PUMP | LONG | Combo Adaptive | 60m | 2,0x | 0,00502 | 0,00502 | 0,00460 | 0,00254 | 0,00587 | €295,78 | €591,56 | €49,57 | €0,00 |
| Combo Adaptive Long Only V1 | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €645,48 | €1.290,95 | €46,47 | €0,00 |
| Combo Adaptive Long Only V1 | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €308,39 | €616,77 | €53,69 | €5,62 |
| Combo Adaptive Long Only V1 | PUMP | LONG | Combo Adaptive | 60m | 2,0x | 0,00502 | 0,00502 | 0,00460 | 0,00254 | 0,00587 | €312,68 | €625,36 | €52,40 | €0,00 |
| Combo Adaptive Long Only V1 | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,52450 | 2,33981 | 1,27487 | 2,89389 | €48,12 | €96,24 | €7,04 | €0,00 |
| Combo Adaptive Long Only V1 | BTC | LONG | Combo Adaptive | 60m | 2,0x | 80839,33463 | 80459,88000 | 79541,01127 | 40823,86399 | 83435,98137 | €1.627,32 | €3.254,65 | €52,27 | €-15,28 |
| Combo Adaptive Partial 1R V1 | SOXL | SHORT | Combo Adaptive | 60m | 2,0x | 121,01735 | 121,01735 | 128,90956 | 180,92093 | 105,23292 | €352,70 | €705,40 | €46,00 | €-0,00 |
| Combo Adaptive Partial 1R V1 | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €292,79 | €585,58 | €50,97 | €5,34 |
| Combo Adaptive Partial 1R V1 | PUMP | LONG | Combo Adaptive | 60m | 2,0x | 0,00502 | 0,00502 | 0,00460 | 0,00254 | 0,00587 | €16,58 | €33,16 | €2,78 | €0,00 |
| Combo Adaptive Partial 1R V1 | TRUMP | LONG | Combo Adaptive | 60m | 2,0x | 2,52450 | 2,52450 | 2,33981 | 1,27487 | 2,89389 | €347,19 | €694,38 | €50,80 | €0,00 |
| Combo Adaptive Partial 1R V1 | VELVET | SHORT | Combo Adaptive | 60m | 2,0x | 0,17246 | 0,14726 | 0,17246 | 0,25782 | 0,13107 | €207,76 | €415,52 | €0,00 | €60,71 |
| Combo Adaptive Partial 1R V1 | SOL | LONG | Combo Adaptive | 60m | 2,0x | 100,45609 | 101,76000 | 97,46723 | 50,73032 | 106,43381 | €39,62 | €79,24 | €2,36 | €1,03 |
| Combo Adaptive Partial 1R V1 | BTC | LONG | Combo Adaptive | 60m | 2,0x | 80839,33463 | 80459,88000 | 79541,01127 | 40823,86399 | 83435,98137 | €20,55 | €41,09 | €0,66 | €-0,19 |
| Combo Adaptive Quality7 Regime Partial 1R V1 | PUMP | LONG | Combo Adaptive | 60m | 2,0x | 0,00502 | 0,00502 | 0,00460 | 0,00254 | 0,00587 | €299,55 | €599,09 | €50,20 | €0,00 |
| Btc Ema 1H | BTC | LONG | Trend following EMA | 60m | 3,0x | 80839,33463 | 80459,88000 | 79541,01127 | 54297,08643 | 83435,98137 | €1.031,72 | €3.095,15 | €49,71 | €-14,53 |
| Btc Ema 4H | BTC | LONG | Trend following EMA | 240m | 2,0x | 80355,23783 | 80459,88000 | 77497,66656 | 40579,39511 | 87499,16561 | €704,37 | €1.408,74 | €50,10 | €1,83 |
| Btc Donchian 1H | BTC | LONG | Donchian breakout 20 barre | 60m | 3,0x | 80839,33463 | 80459,88000 | 79685,26906 | 54297,08643 | 83147,46498 | €1.175,39 | €3.526,17 | €50,34 | €-16,55 |
| Btc Donchian 4H | BTC | LONG | Donchian breakout 20 barre | 240m | 2,0x | 80355,23783 | 80459,88000 | 77497,66656 | 40579,39511 | 88356,43707 | €700,60 | €1.401,20 | €49,83 | €1,82 |
| Btc Bollinger 1H | BTC | SHORT | Bollinger mean reversion | 60m | 3,0x | 80807,00537 | 80459,88000 | 81888,50855 | 107338,63879 | 79184,74978 | €1.262,52 | €3.787,57 | €50,69 | €16,27 |
| Btc Bollinger 4H | BTC | SHORT | Bollinger mean reversion | 240m | 2,0x | 80323,10217 | 80459,88000 | 82919,85488 | 120083,03774 | 75648,94663 | €775,58 | €1.551,16 | €50,15 | €-2,64 |
| Btc Adaptive 1H | BTC | LONG | Combo Adaptive | 60m | 3,0x | 80839,33463 | 80459,88000 | 79541,01127 | 54297,08643 | 83435,98137 | €1.045,87 | €3.137,61 | €50,39 | €-14,73 |
| Btc Adaptive 4H | BTC | LONG | Combo Adaptive | 240m | 2,0x | 80355,23783 | 80459,88000 | 77237,88772 | 40579,39511 | 88148,61352 | €648,94 | €1.297,88 | €50,35 | €1,69 |
| Sol Ema 1H | SOL | LONG | Trend following EMA | 60m | 3,0x | 95,05001 | 101,76000 | 98,99140 | 63,84192 | 104,15904 | €349,20 | €1.047,59 | €0,00 | €73,95 |
| Sol Ema 4H | SOL | LONG | Trend following EMA | 240m | 2,0x | 93,39968 | 101,76000 | 97,35104 | 47,16684 | 109,83325 | €356,10 | €712,19 | €0,00 | €63,75 |
| Sol Adaptive 1H | SOL | LONG | Combo Adaptive | 60m | 3,0x | 95,05001 | 101,76000 | 98,99140 | 63,84192 | 104,15904 | €344,23 | €1.032,69 | €0,00 | €72,90 |
| Sol Adaptive 4H | SOL | LONG | Combo Adaptive | 240m | 2,0x | 93,39968 | 101,76000 | 97,18824 | 47,16684 | 111,32722 | €330,98 | €661,97 | €0,00 | €59,25 |
| Eth Ema 1H | ETH | LONG | Trend following EMA | 60m | 3,0x | 2495,82907 | 2498,90000 | 2443,43023 | 1676,36519 | 2600,62673 | €783,24 | €2.349,73 | €49,33 | €2,89 |
| Eth Ema 4H | ETH | LONG | Trend following EMA | 240m | 2,0x | 2390,02791 | 2498,90000 | 2268,60778 | 1206,96409 | 2693,57826 | €487,73 | €975,47 | €49,56 | €44,44 |
| Doge Ema 1H | DOGE | LONG | Trend following EMA | 60m | 3,0x | 0,09314 | 0,09232 | 0,08689 | 0,06256 | 0,10563 | €248,90 | €746,70 | €50,09 | €-6,56 |
| Master Adaptive Expanded V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04309 | 0,03814 | 0,02188 | 0,05374 | €197,50 | €395,01 | €47,40 | €-2,24 |
| Master Adaptive Runner25 V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04309 | 0,03814 | 0,02188 | 0,05894 | €34,77 | €69,54 | €8,34 | €-0,39 |
| Combo Adaptive Side Regime Guard V1 | NEAR | LONG | Combo Adaptive | 60m | 2,0x | 2,08142 | 2,08142 | 2,00650 | 1,05112 | 2,23125 | €77,52 | €155,04 | €5,58 | €0,00 |
| Combo Adaptive Side Regime Guard V1 | ZEC | LONG | Combo Adaptive | 60m | 2,0x | 807,93155 | 851,02000 | 737,89694 | 408,00543 | 948,00078 | €305,89 | €611,78 | €53,03 | €32,63 |
| Combo Adaptive Side Regime Guard V1 | PEPE | LONG | Combo Adaptive | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00000 | €304,59 | €609,17 | €53,03 | €5,55 |
| Combo Adaptive Side Regime Guard V1 | VELVET | SHORT | Combo Adaptive | 60m | 2,0x | 0,17246 | 0,14726 | 0,17246 | 0,25782 | 0,13107 | €216,61 | €433,23 | €0,00 | €63,29 |
| Combo Adaptive Side Regime Guard V1 | TUT | SHORT | Combo Adaptive | 60m | 2,0x | 0,04570 | 0,04309 | 0,05118 | 0,06832 | 0,03473 | €192,40 | €384,79 | €46,18 | €21,98 |
| Master Adaptive Gb20 Loss Cap V1 | TUT | LONG | Master Adaptive Consensus | 60m | 2,0x | 0,04334 | 0,04309 | 0,03828 | 0,02188 | 0,05682 | €195,70 | €391,41 | €45,67 | €-2,22 |
| Main Side Regime Guard V1 | VELVET | LONG | Confluenza trend | 240m | 3,0x | 0,55987 | 0,14726 | 0,49269 | 0,37605 | 0,69424 | €142,25 | €426,74 | €51,21 | €-314,50 |
| Main Side Regime Guard V1 | AKE | LONG | Confluenza trend | 240m | 3,0x | 0,01021 | 0,01021 | 0,00899 | 0,00686 | 0,01266 | €145,97 | €437,90 | €52,55 | €0,00 |
| Main Side Regime Guard V1 | PUMP | LONG | Confluenza trend | 240m | 3,0x | 0,00468 | 0,00468 | 0,00481 | 0,00314 | 0,00580 | €149,89 | €449,66 | €0,00 | €0,00 |
| Main Side Regime Guard V1 | HYPE | LONG | Confluenza trend | 240m | 3,0x | 77,65853 | 81,10800 | 71,20755 | 52,16065 | 90,56048 | €216,52 | €649,56 | €53,96 | €28,85 |
| Main Side Regime Guard V1 | XRP | LONG | Confluenza trend | 240m | 3,0x | 1,47102 | 1,51986 | 1,31178 | 0,98804 | 1,78951 | €12,77 | €38,31 | €4,15 | €1,27 |
| Main Side Regime Guard V1 | ETH | LONG | Confluenza trend | 240m | 3,0x | 2437,91749 | 2498,90000 | 2326,72117 | 1637,46791 | 2660,31012 | €9,94 | €29,83 | €1,36 | €0,75 |
| Main Dynamic Asset Selector V1 | PUMP | LONG | Confluenza trend | 240m | 3,0x | 0,00515 | 0,00515 | 0,00453 | 0,00346 | 0,00638 | €141,85 | €425,56 | €51,07 | €0,00 |
| Combo Trend Side Regime Guard V1 | ZEC | LONG | Combo Trend | 60m | 2,0x | 822,67450 | 851,02000 | 761,05343 | 415,45062 | 958,24084 | €381,00 | €762,00 | €57,08 | €26,26 |
| Combo Trend Side Regime Guard V1 | PEPE | LONG | Combo Trend | 60m | 2,0x | 0,00000 | 0,00000 | 0,00000 | 0,00000 | 0,00001 | €293,50 | €586,99 | €56,78 | €5,35 |
| Combo Trend Side Regime Guard V1 | PUMP | LONG | Combo Trend | 60m | 2,0x | 0,00523 | 0,00523 | 0,00474 | 0,00264 | 0,00631 | €294,84 | €589,68 | €55,15 | €0,00 |
| Combo Trend Side Regime Guard V1 | VELVET | SHORT | Combo Trend | 60m | 2,0x | 0,17246 | 0,14726 | 0,17246 | 0,25782 | 0,12693 | €217,86 | €435,73 | €0,00 | €63,66 |
| Combo Trend Side Regime Guard V1 | TUT | SHORT | Combo Trend | 60m | 2,0x | 0,04570 | 0,04309 | 0,05118 | 0,06832 | 0,03364 | €12,81 | €25,62 | €3,07 | €1,46 |
| 1H Balanced V3 Long Only V1 | SKHYNIX | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1220,85412 | 1220,85412 | 1177,63561 | 820,00702 | 1307,29117 | €435,49 | €1.306,46 | €46,25 | €0,00 |
| 1H Balanced V3 Long Only V1 | ZEC | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 807,93155 | 851,02000 | 737,89694 | 542,66069 | 948,00078 | €184,72 | €554,15 | €48,04 | €29,55 |
| 1H Balanced V3 Long Only V1 | XRP | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 1,47399 | 1,51986 | 1,35380 | 0,99003 | 1,71438 | €194,69 | €584,07 | €47,63 | €18,17 |
| 1H Balanced V3 Long Only V1 | PUMP | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 0,00523 | 0,00523 | 0,00479 | 0,00351 | 0,00611 | €184,35 | €553,04 | €46,55 | €0,00 |
| 1H Balanced V3 Long Only V1 | ETH | LONG | Confluenza trend V3 Filtered | 60m | 3,0x | 2484,05671 | 2498,90000 | 2436,27995 | 1668,45809 | 2579,61023 | €50,09 | €150,27 | €2,89 | €0,90 |
| Scanner Bottom5 Short Profit Lock V1 | SOXL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €381,80 | €763,60 | €48,45 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | SNDK | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €496,62 | €993,25 | €48,08 | €-0,00 |
| Scanner Bottom5 Short Profit Lock V1 | VELVET | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,17246 | 0,14726 | 0,17246 | 0,25782 | 0,13107 | €192,55 | €385,10 | €0,00 | €56,26 |
| Scanner Bottom5 Short Profit Lock V1 | TUT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,04570 | 0,04309 | 0,05118 | 0,06832 | 0,03473 | €179,76 | €359,53 | €43,14 | €20,54 |
| Scanner Bottom5 Short Mfe Trail V1 | SOXL | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 121,15726 | 121,15726 | 128,84415 | 181,13011 | 105,78350 | €382,38 | €764,76 | €48,52 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | SNDK | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 1562,11217 | 1562,11217 | 1637,73071 | 2335,35769 | 1410,87509 | €497,38 | €994,76 | €48,15 | €-0,00 |
| Scanner Bottom5 Short Mfe Trail V1 | VELVET | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,17246 | 0,14726 | 0,17246 | 0,25782 | 0,13107 | €192,85 | €385,69 | €0,00 | €56,35 |
| Scanner Bottom5 Short Mfe Trail V1 | TUT | SHORT | Scanner Bottom 5 Short | 60m | 2,0x | 0,04570 | 0,04309 | 0,05118 | 0,06832 | 0,03473 | €180,04 | €360,08 | €43,21 | €20,57 |

## Ultime operazioni chiuse

| Portafoglio | Asset | Lato | Chiusura UTC | Exit | P&L netto | R | Motivo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1H Fast V3 No Esports Long Only V1 | PEPE | LONG | 2026-08-25T04:45:00+00:00 | 0,00000 | €7,20 | 0,14 | STOP |
| 1H Fast V3 Long Only V1 | PEPE | LONG | 2026-08-25T04:45:00+00:00 | 0,00000 | €0,73 | 0,14 | STOP |
| 1H Fast Tp2 V1 | PEPE | LONG | 2026-08-25T04:45:00+00:00 | 0,00000 | €0,35 | 0,14 | STOP |
| 1H Fast V3 No Esports Long Only V1 | XRP | LONG | 2026-08-25T04:00:00+00:00 | 1,51078 | €-0,12 | -0,05 | STOP |
| Benchmark trend following EMA 1H | BTC | LONG | 2026-08-25T02:45:00+00:00 | 81208,84767 | €94,01 | 2,11 | TARGET |
| 1H Fast V3 No Esports V1 | DOGE | SHORT | 2026-08-25T02:30:00+00:00 | 0,09187 | €-49,66 | -1,05 | STOP |
| 1H Fast V3 No Esports Mfe Lock V1 | BTC | LONG | 2026-08-25T02:30:00+00:00 | 80496,33500 | €6,06 | 1,40 | TARGET |
| 1H Fast V3 No Esports Mfe Lock V1 | DOGE | SHORT | 2026-08-25T02:30:00+00:00 | 0,09187 | €-1,49 | -1,05 | STOP |
| 1H Fast V3 No Esports Long Only V1 | BTC | LONG | 2026-08-25T02:30:00+00:00 | 80496,33500 | €68,63 | 1,40 | TARGET |
| 1H Fast V3 Long Only V1 | BTC | LONG | 2026-08-25T02:30:00+00:00 | 80854,53436 | €64,00 | 1,39 | TARGET |
| 1H Fast V3 Cap75 V1 | DOGE | SHORT | 2026-08-25T02:30:00+00:00 | 0,09187 | €-48,14 | -1,05 | STOP |
| Rapida 1H V3 Filtered | BTC | LONG | 2026-08-25T02:30:00+00:00 | 80496,33500 | €6,02 | 1,40 | TARGET |

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

Generato: 2026-08-25 05:32 UTC


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

Segnali totali salvati: **138**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08-25 | BTC | 80.778,18 | +6 | +2 | +2 | 0 | +3 | +1 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-08-25 | DOGE | 0.09299 | +5 | +1 | +1 | 0 | +3 | +1 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-08-25 | SOL | 102,40 | +6 | +1 | +1 | 0 | +3 | +1 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-08-24 | BTC | 76.958,14 | +6 | +2 | +2 | 0 | +3 | +1 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-08-24 | DOGE | 0.09174 | +4 | +1 | +1 | 0 | +3 | +1 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-08-24 | SOL | 93,82 | +6 | +1 | +1 | 0 | +3 | +1 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-08-23 | BTC | 76.280,85 | +7 | +2 | +2 | 0 | +3 | +1 | 0 | ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA |
| 2026-08-23 | DOGE | 0.09044 | +7 | +2 | +2 | 0 | +3 | +1 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-08-23 | SOL | 93,05 | +3 | -1 | -1 | 0 | +3 | +1 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-08-22 | BTC | 77.109,54 | +5 | +1 | +1 | 0 | +3 | +1 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-08-22 | DOGE | 0.09028 | +6 | +1 | +1 | 0 | +3 | +1 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-08-22 | SOL | 93,36 | +3 | -1 | -1 | 0 | +3 | +1 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 46 | 45 | 44 | 43 | 41 | 39 | 36 | 34 | 27 | 18 | 3 | 0 |
| SOL | 46 | 45 | 44 | 43 | 41 | 39 | 36 | 34 | 27 | 18 | 3 | 0 |
| DOGE | 46 | 45 | 44 | 43 | 41 | 39 | 36 | 34 | 27 | 18 | 3 | 0 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-07-12 | 45g | 2026-08-26 | domani |
| SOL | 2026-07-12 | 45g | 2026-08-26 | domani |
| DOGE | 2026-07-12 | 45g | 2026-08-26 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 42 | 54,76% | +0,61% | +0,58% | PRIMA CALIBRAZIONE |
| BTC | 2g | 41 | 53,66% | +0,97% | +0,86% | PRIMA CALIBRAZIONE |
| BTC | 3g | 40 | 50,00% | +1,17% | +1,00% | PRIMA CALIBRAZIONE |
| BTC | 5g | 38 | 39,47% | +2,28% | +1,94% | PRIMA CALIBRAZIONE |
| BTC | 7g | 36 | 47,22% | +2,33% | +2,03% | PRIMA CALIBRAZIONE |
| BTC | 10g | 34 | 47,06% | +2,38% | +2,11% | PRIMA CALIBRAZIONE |
| BTC | 14g | 32 | 56,25% | +3,32% | +3,21% | PRIMA CALIBRAZIONE |
| BTC | 21g | 25 | 44,00% | +4,29% | +4,02% | FEEDBACK RAPIDO |
| BTC | 30g | 16 | 87,50% | +5,31% | +5,62% | FEEDBACK RAPIDO |
| BTC | 45g | 3 | 100,00% | +22,42% | +22,42% | FEEDBACK RAPIDO |
| BTC | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 1g | 38 | 57,89% | +0,84% | +0,68% | PRIMA CALIBRAZIONE |
| SOL | 2g | 37 | 54,05% | +1,49% | +1,30% | PRIMA CALIBRAZIONE |
| SOL | 3g | 36 | 55,56% | +2,26% | +2,01% | PRIMA CALIBRAZIONE |
| SOL | 5g | 34 | 58,82% | +3,54% | +3,38% | PRIMA CALIBRAZIONE |
| SOL | 7g | 32 | 62,50% | +3,90% | +4,06% | PRIMA CALIBRAZIONE |
| SOL | 10g | 29 | 62,07% | +3,08% | +3,34% | FEEDBACK RAPIDO |
| SOL | 14g | 27 | 70,37% | +4,48% | +5,83% | FEEDBACK RAPIDO |
| SOL | 21g | 20 | 60,00% | +4,15% | +2,37% | FEEDBACK RAPIDO |
| SOL | 30g | 14 | 42,86% | +2,59% | +0,37% | FEEDBACK RAPIDO |
| SOL | 45g | 2 | 100,00% | +25,44% | +25,44% | FEEDBACK RAPIDO |
| SOL | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 1g | 43 | 51,16% | +0,67% | +0,66% | PRIMA CALIBRAZIONE |
| DOGE | 2g | 42 | 52,38% | +1,33% | +1,32% | PRIMA CALIBRAZIONE |
| DOGE | 3g | 41 | 51,22% | +1,92% | +2,20% | PRIMA CALIBRAZIONE |
| DOGE | 5g | 39 | 58,97% | +3,11% | +3,75% | PRIMA CALIBRAZIONE |
| DOGE | 7g | 37 | 64,86% | +3,11% | +4,30% | PRIMA CALIBRAZIONE |
| DOGE | 10g | 34 | 58,82% | +1,50% | +3,33% | PRIMA CALIBRAZIONE |
| DOGE | 14g | 32 | 65,62% | +2,98% | +5,88% | PRIMA CALIBRAZIONE |
| DOGE | 21g | 26 | 69,23% | +3,15% | +1,62% | FEEDBACK RAPIDO |
| DOGE | 30g | 18 | 72,22% | +4,53% | -1,57% | FEEDBACK RAPIDO |
| DOGE | 45g | 3 | 0,00% | +24,66% | -24,66% | FEEDBACK RAPIDO |
| DOGE | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 42 | 54,76% | +0,61% | +0,58% | +0,16% | +1,20% | PRIMA CALIBRAZIONE |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 45 | 57,78% | +0,56% | +0,56% | +0,13% | +1,13% | PRIMA CALIBRAZIONE |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 45 | 57,78% | +0,56% | +0,56% | +0,13% | +1,13% | PRIMA CALIBRAZIONE |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,25% | +0,25% | -0,10% | +0,70% | PRIMA CALIBRAZIONE |
| BTC | 1g | Tecnico | CALIBRABILE | 40 | 40,00% | +0,75% | +0,24% | +0,29% | +1,33% | PRIMA CALIBRAZIONE |
| BTC | 1g | Classic technical | CALIBRABILE | 13 | 38,46% | +1,59% | +0,78% | +0,75% | +2,20% | FEEDBACK RAPIDO |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +1,45% | +1,45% | +1,10% | +2,07% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 41 | 53,66% | +0,97% | +0,86% | +0,40% | +1,71% | PRIMA CALIBRAZIONE |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 44 | 56,82% | +1,08% | +1,08% | +0,51% | +1,80% | PRIMA CALIBRAZIONE |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 44 | 56,82% | +1,08% | +1,08% | +0,51% | +1,80% | PRIMA CALIBRAZIONE |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,52% | +0,52% | -0,02% | +1,18% | PRIMA CALIBRAZIONE |
| BTC | 2g | Tecnico | CALIBRABILE | 39 | 43,59% | +1,35% | +0,29% | +0,78% | +2,08% | PRIMA CALIBRAZIONE |
| BTC | 2g | Classic technical | CALIBRABILE | 12 | 33,33% | +2,14% | +0,88% | +1,61% | +2,98% | FEEDBACK RAPIDO |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +4,54% | +4,54% | +3,15% | +5,05% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 40 | 50,00% | +1,17% | +1,00% | -0,83% | +2,83% | PRIMA CALIBRAZIONE |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 43 | 60,47% | +1,54% | +1,54% | -0,81% | +3,11% | PRIMA CALIBRAZIONE |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 43 | 60,47% | +1,54% | +1,54% | -0,81% | +3,11% | PRIMA CALIBRAZIONE |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 35 | 57,14% | +0,91% | +0,91% | -1,00% | +2,36% | PRIMA CALIBRAZIONE |
| BTC | 3g | Tecnico | CALIBRABILE | 38 | 36,84% | +2,01% | -0,21% | -0,55% | +3,52% | PRIMA CALIBRAZIONE |
| BTC | 3g | Classic technical | CALIBRABILE | 11 | 36,36% | +3,29% | -0,21% | +0,27% | +4,57% | FEEDBACK RAPIDO |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,88% | +1,88% | +1,44% | +4,24% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 38 | 39,47% | +2,28% | +1,94% | -1,47% | +4,30% | PRIMA CALIBRAZIONE |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 41 | 48,78% | +2,58% | +2,58% | -1,43% | +4,69% | PRIMA CALIBRAZIONE |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 41 | 48,78% | +2,58% | +2,58% | -1,43% | +4,69% | PRIMA CALIBRAZIONE |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 35 | 48,57% | +2,08% | +2,08% | -1,57% | +4,07% | PRIMA CALIBRAZIONE |
| BTC | 5g | Tecnico | CALIBRABILE | 36 | 36,11% | +3,09% | -1,62% | -1,16% | +5,24% | PRIMA CALIBRAZIONE |
| BTC | 5g | Classic technical | CALIBRABILE | 9 | 22,22% | +8,25% | -4,66% | -0,01% | +9,57% | FEEDBACK RAPIDO |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,16% | -0,16% | -0,37% | +4,24% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 36 | 47,22% | +2,33% | +2,03% | -2,11% | +4,78% | PRIMA CALIBRAZIONE |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 39 | 56,41% | +2,78% | +2,78% | -2,06% | +5,22% | PRIMA CALIBRAZIONE |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 39 | 56,41% | +2,78% | +2,78% | -2,06% | +5,22% | PRIMA CALIBRAZIONE |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 34 | 58,82% | +2,59% | +2,59% | -2,06% | +4,93% | PRIMA CALIBRAZIONE |
| BTC | 7g | Tecnico | CALIBRABILE | 34 | 29,41% | +3,53% | -3,97% | -1,80% | +5,83% | PRIMA CALIBRAZIONE |
| BTC | 7g | Classic technical | CALIBRABILE | 8 | 0,00% | +11,51% | -11,51% | -0,67% | +13,66% | FEEDBACK RAPIDO |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,77% | +1,77% | -0,79% | +4,24% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 34 | 47,06% | +2,38% | +2,11% | -2,53% | +4,82% | PRIMA CALIBRAZIONE |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 36 | 52,78% | +2,11% | +2,11% | -2,56% | +4,70% | PRIMA CALIBRAZIONE |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 36 | 52,78% | +2,11% | +2,11% | -2,56% | +4,70% | PRIMA CALIBRAZIONE |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 32 | 59,38% | +2,63% | +2,63% | -2,45% | +4,99% | PRIMA CALIBRAZIONE |
| BTC | 10g | Tecnico | CALIBRABILE | 31 | 32,26% | +2,64% | -1,18% | -2,30% | +5,27% | PRIMA CALIBRAZIONE |
| BTC | 10g | Classic technical | CALIBRABILE | 6 | 0,00% | +9,33% | -9,33% | -1,08% | +11,39% | FEEDBACK RAPIDO |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,43% | -0,43% | -2,30% | +4,24% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 32 | 56,25% | +3,32% | +3,21% | -2,89% | +6,39% | PRIMA CALIBRAZIONE |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 34 | 55,88% | +3,03% | +3,03% | -2,91% | +6,17% | PRIMA CALIBRAZIONE |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 34 | 55,88% | +3,03% | +3,03% | -2,91% | +6,17% | PRIMA CALIBRAZIONE |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 30 | 63,33% | +3,77% | +3,77% | -2,71% | +6,68% | PRIMA CALIBRAZIONE |
| BTC | 14g | Tecnico | CALIBRABILE | 29 | 65,52% | +3,77% | +3,72% | -2,64% | +6,95% | FEEDBACK RAPIDO |
| BTC | 14g | Classic technical | CALIBRABILE | 4 | 50,00% | +0,27% | -0,27% | -1,55% | +3,37% | FEEDBACK RAPIDO |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -2,25% | -2,25% | -3,05% | +4,24% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 25 | 44,00% | +4,29% | +4,02% | -2,89% | +7,89% | FEEDBACK RAPIDO |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 27 | 55,56% | +3,89% | +3,89% | -2,95% | +7,50% | FEEDBACK RAPIDO |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 27 | 55,56% | +3,89% | +3,89% | -2,95% | +7,50% | FEEDBACK RAPIDO |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 23 | 60,87% | +4,80% | +4,80% | -2,68% | +8,40% | FEEDBACK RAPIDO |
| BTC | 21g | Tecnico | CALIBRABILE | 22 | 22,73% | +4,41% | -2,30% | -2,60% | +8,11% | FEEDBACK RAPIDO |
| BTC | 21g | Classic technical | CALIBRABILE | 4 | 0,00% | +11,68% | -11,68% | -1,55% | +14,27% | FEEDBACK RAPIDO |
| BTC | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,21% | +1,21% | -3,06% | +4,24% | FEEDBACK RAPIDO |
| BTC | 30g | Global confluence | BENCHMARK | 16 | 87,50% | +5,31% | +5,62% | -3,22% | +9,08% | FEEDBACK RAPIDO |
| BTC | 30g | Famiglia statistica | CALIBRABILE | 18 | 72,22% | +5,61% | +5,61% | -3,27% | +9,53% | FEEDBACK RAPIDO |
| BTC | 30g | Scanner grezzo | DIAGNOSTICO | 18 | 72,22% | +5,61% | +5,61% | -3,27% | +9,53% | FEEDBACK RAPIDO |
| BTC | 30g | Market regime grezzo | DIAGNOSTICO | 14 | 71,43% | +5,87% | +5,87% | -2,92% | +10,24% | FEEDBACK RAPIDO |
| BTC | 30g | Tecnico | CALIBRABILE | 15 | 40,00% | +5,34% | -2,30% | -2,97% | +9,75% | FEEDBACK RAPIDO |
| BTC | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +0,16% | +0,16% | -3,06% | +4,24% | FEEDBACK RAPIDO |
| BTC | 45g | Global confluence | BENCHMARK | 3 | 100,00% | +22,42% | +22,42% | -3,05% | +25,54% | FEEDBACK RAPIDO |
| BTC | 45g | Famiglia statistica | CALIBRABILE | 3 | 100,00% | +22,42% | +22,42% | -3,05% | +25,54% | FEEDBACK RAPIDO |
| BTC | 45g | Scanner grezzo | DIAGNOSTICO | 3 | 100,00% | +22,42% | +22,42% | -3,05% | +25,54% | FEEDBACK RAPIDO |
| BTC | 45g | Market regime grezzo | DIAGNOSTICO | 3 | 100,00% | +22,42% | +22,42% | -3,05% | +25,54% | FEEDBACK RAPIDO |
| BTC | 45g | Tecnico | CALIBRABILE | 2 | 0,00% | +23,38% | -23,38% | -2,93% | +26,09% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 43 | 51,16% | +0,67% | +0,66% | +0,07% | +1,72% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 45 | 60,00% | +0,55% | +0,82% | -0,05% | +1,57% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 45 | 60,00% | +0,55% | +0,82% | -0,05% | +1,57% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,15% | +0,26% | -0,32% | +0,87% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Tecnico | CALIBRABILE | 38 | 57,89% | +0,49% | +0,72% | -0,15% | +1,48% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Classic technical | CALIBRABILE | 30 | 43,33% | +0,50% | -0,30% | -0,13% | +1,22% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 71,43% | +2,86% | +2,41% | +1,15% | +3,54% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 42 | 52,38% | +1,33% | +1,32% | +0,58% | +2,70% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 44 | 54,55% | +1,16% | +1,38% | +0,43% | +2,50% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 44 | 54,55% | +1,16% | +1,38% | +0,43% | +2,50% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 38 | 50,00% | +0,36% | +0,74% | -0,26% | +1,41% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Tecnico | CALIBRABILE | 37 | 64,86% | +0,69% | +1,19% | +0,01% | +1,98% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Classic technical | CALIBRABILE | 29 | 48,28% | +1,15% | -0,85% | +0,37% | +2,14% | FEEDBACK RAPIDO |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 6 | 66,67% | +5,87% | +5,43% | +5,07% | +8,56% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 41 | 51,22% | +1,92% | +2,20% | -1,01% | +4,61% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 43 | 55,81% | +1,73% | +2,03% | -1,13% | +4,36% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 43 | 55,81% | +1,73% | +2,03% | -1,13% | +4,36% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,84% | +1,55% | -1,48% | +3,36% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Tecnico | CALIBRABILE | 36 | 52,78% | +0,74% | +1,21% | -1,38% | +3,11% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Classic technical | CALIBRABILE | 28 | 35,71% | +2,01% | -1,79% | -1,31% | +4,60% | FEEDBACK RAPIDO |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 6 | 66,67% | +5,19% | +4,84% | +0,90% | +8,54% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 39 | 58,97% | +3,11% | +3,75% | -1,86% | +6,70% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 41 | 56,10% | +2,86% | +3,48% | -1,95% | +6,37% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 41 | 56,10% | +2,86% | +3,48% | -1,95% | +6,37% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +2,45% | +3,08% | -2,17% | +5,74% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Tecnico | CALIBRABILE | 34 | 64,71% | +1,65% | +1,27% | -2,38% | +4,91% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Classic technical | CALIBRABILE | 27 | 44,44% | +3,71% | -3,71% | -1,98% | +7,48% | FEEDBACK RAPIDO |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +5,46% | +5,14% | +1,28% | +11,40% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 37 | 64,86% | +3,11% | +4,30% | -2,68% | +7,24% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 39 | 61,54% | +2,83% | +3,93% | -2,78% | +6,92% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 39 | 61,54% | +2,83% | +3,93% | -2,78% | +6,92% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 37 | 62,16% | +3,04% | +4,08% | -2,78% | +7,05% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Tecnico | CALIBRABILE | 33 | 63,64% | +1,75% | +1,79% | -3,12% | +5,79% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Classic technical | CALIBRABILE | 26 | 46,15% | +3,58% | -3,58% | -2,73% | +7,84% | FEEDBACK RAPIDO |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 50,00% | +0,63% | +0,36% | -0,50% | +5,72% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 34 | 58,82% | +1,50% | +3,33% | -3,36% | +5,85% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 36 | 58,33% | +1,31% | +3,07% | -3,42% | +5,58% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 36 | 58,33% | +1,31% | +3,07% | -3,42% | +5,58% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 34 | 58,82% | +1,44% | +3,20% | -3,42% | +5,64% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Tecnico | CALIBRABILE | 31 | 67,74% | -0,31% | +2,41% | -3,79% | +3,92% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Classic technical | CALIBRABILE | 23 | 56,52% | +0,32% | -0,32% | -3,55% | +4,70% | FEEDBACK RAPIDO |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 75,00% | +0,93% | +0,18% | -1,31% | +5,72% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 32 | 65,62% | +2,98% | +5,88% | -4,04% | +8,39% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 34 | 70,59% | +2,68% | +5,43% | -4,07% | +7,96% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 34 | 70,59% | +2,68% | +5,43% | -4,07% | +7,96% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 32 | 71,88% | +2,94% | +5,67% | -4,09% | +8,18% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Tecnico | CALIBRABILE | 30 | 66,67% | -0,31% | +0,31% | -4,43% | +4,70% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Classic technical | CALIBRABILE | 22 | 63,64% | +0,33% | -0,33% | -4,43% | +5,27% | FEEDBACK RAPIDO |
| DOGE | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 75,00% | +12,47% | +2,65% | -1,31% | +16,91% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 26 | 69,23% | +3,15% | +1,62% | -5,01% | +9,37% | FEEDBACK RAPIDO |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 27 | 81,48% | +2,89% | +7,27% | -5,08% | +9,02% | FEEDBACK RAPIDO |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 27 | 81,48% | +2,89% | +7,27% | -5,08% | +9,02% | FEEDBACK RAPIDO |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 25 | 84,00% | +3,22% | +7,75% | -5,18% | +9,38% | FEEDBACK RAPIDO |
| DOGE | 21g | Tecnico | CALIBRABILE | 27 | 70,37% | +2,89% | -2,89% | -5,08% | +9,02% | FEEDBACK RAPIDO |
| DOGE | 21g | Classic technical | CALIBRABILE | 20 | 75,00% | +0,03% | -0,03% | -5,18% | +6,01% | FEEDBACK RAPIDO |
| DOGE | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +0,76% | +0,76% | -1,85% | +6,57% | FEEDBACK RAPIDO |
| DOGE | 30g | Global confluence | BENCHMARK | 18 | 72,22% | +4,53% | -1,57% | -6,13% | +11,19% | FEEDBACK RAPIDO |
| DOGE | 30g | Famiglia statistica | CALIBRABILE | 18 | 77,78% | +4,53% | +1,99% | -6,13% | +11,19% | FEEDBACK RAPIDO |
| DOGE | 30g | Scanner grezzo | DIAGNOSTICO | 18 | 77,78% | +4,53% | +1,99% | -6,13% | +11,19% | FEEDBACK RAPIDO |
| DOGE | 30g | Market regime grezzo | DIAGNOSTICO | 16 | 87,50% | +1,60% | +5,73% | -6,42% | +7,93% | FEEDBACK RAPIDO |
| DOGE | 30g | Tecnico | CALIBRABILE | 18 | 66,67% | +4,53% | -4,53% | -6,13% | +11,19% | FEEDBACK RAPIDO |
| DOGE | 30g | Classic technical | CALIBRABILE | 16 | 68,75% | +3,81% | -3,81% | -5,92% | +10,30% | FEEDBACK RAPIDO |
| DOGE | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +31,53% | +31,53% | -1,85% | +40,20% | FEEDBACK RAPIDO |
| DOGE | 45g | Global confluence | BENCHMARK | 3 | 0,00% | +24,66% | -24,66% | -7,62% | +33,25% | FEEDBACK RAPIDO |
| DOGE | 45g | Famiglia statistica | CALIBRABILE | 3 | 0,00% | +24,66% | -24,66% | -7,62% | +33,25% | FEEDBACK RAPIDO |
| DOGE | 45g | Scanner grezzo | DIAGNOSTICO | 3 | 0,00% | +24,66% | -24,66% | -7,62% | +33,25% | FEEDBACK RAPIDO |
| DOGE | 45g | Market regime grezzo | DIAGNOSTICO | 3 | 0,00% | +24,66% | -24,66% | -7,62% | +33,25% | FEEDBACK RAPIDO |
| DOGE | 45g | Tecnico | CALIBRABILE | 3 | 0,00% | +24,66% | -24,66% | -7,62% | +33,25% | FEEDBACK RAPIDO |
| DOGE | 45g | Classic technical | CALIBRABILE | 3 | 0,00% | +24,66% | -24,66% | -7,62% | +33,25% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 38 | 57,89% | +0,84% | +0,68% | +0,18% | +1,80% | PRIMA CALIBRAZIONE |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 40 | 60,00% | +0,44% | +0,42% | -0,14% | +1,36% | PRIMA CALIBRAZIONE |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 43 | 58,14% | +0,48% | +0,31% | -0,11% | +1,39% | PRIMA CALIBRAZIONE |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +0,27% | +0,39% | -0,30% | +0,87% | PRIMA CALIBRAZIONE |
| SOL | 1g | Tecnico | CALIBRABILE | 42 | 52,38% | +0,43% | +0,40% | -0,20% | +1,30% | PRIMA CALIBRAZIONE |
| SOL | 1g | Classic technical | CALIBRABILE | 26 | 53,85% | +0,78% | +0,71% | -0,02% | +1,79% | FEEDBACK RAPIDO |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +1,51% | +1,51% | +0,99% | +5,02% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 37 | 54,05% | +1,49% | +1,30% | +0,67% | +2,64% | PRIMA CALIBRAZIONE |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 39 | 48,72% | +0,96% | +0,34% | +0,13% | +1,76% | PRIMA CALIBRAZIONE |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 42 | 47,62% | +0,92% | +0,29% | +0,11% | +1,83% | PRIMA CALIBRAZIONE |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +0,76% | +0,78% | -0,00% | +1,60% | PRIMA CALIBRAZIONE |
| SOL | 2g | Tecnico | CALIBRABILE | 41 | 43,90% | +0,83% | +0,08% | +0,08% | +1,97% | PRIMA CALIBRAZIONE |
| SOL | 2g | Classic technical | CALIBRABILE | 25 | 56,00% | +0,99% | +0,95% | +0,29% | +2,01% | FEEDBACK RAPIDO |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 33,33% | +0,74% | +0,74% | +0,30% | +2,88% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 36 | 55,56% | +2,26% | +2,01% | -1,12% | +4,41% | PRIMA CALIBRAZIONE |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 38 | 47,37% | +1,56% | +1,01% | -1,55% | +3,72% | PRIMA CALIBRAZIONE |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 41 | 46,34% | +1,47% | +0,91% | -1,53% | +3,69% | PRIMA CALIBRAZIONE |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +1,43% | +1,38% | -1,48% | +3,53% | PRIMA CALIBRAZIONE |
| SOL | 3g | Tecnico | CALIBRABILE | 40 | 45,00% | +1,27% | -0,37% | -1,63% | +3,33% | PRIMA CALIBRAZIONE |
| SOL | 3g | Classic technical | CALIBRABILE | 24 | 50,00% | +1,11% | +0,89% | -1,53% | +3,13% | FEEDBACK RAPIDO |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 33,33% | +0,33% | +0,33% | -1,17% | +5,20% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 34 | 58,82% | +3,54% | +3,38% | -1,79% | +6,49% | PRIMA CALIBRAZIONE |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 36 | 58,33% | +2,57% | +2,77% | -2,23% | +5,54% | PRIMA CALIBRAZIONE |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 39 | 56,41% | +2,43% | +2,50% | -2,22% | +5,41% | PRIMA CALIBRAZIONE |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +2,66% | +2,88% | -2,09% | +5,82% | PRIMA CALIBRAZIONE |
| SOL | 5g | Tecnico | CALIBRABILE | 38 | 42,11% | +2,42% | -1,77% | -2,43% | +5,25% | PRIMA CALIBRAZIONE |
| SOL | 5g | Classic technical | CALIBRABILE | 22 | 54,55% | +1,07% | +0,81% | -2,33% | +3,44% | FEEDBACK RAPIDO |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 0,00% | -2,33% | -2,33% | -3,87% | +1,03% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 32 | 62,50% | +3,90% | +4,06% | -2,67% | +7,26% | PRIMA CALIBRAZIONE |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 35 | 65,71% | +3,26% | +3,92% | -2,94% | +6,69% | PRIMA CALIBRAZIONE |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 38 | 65,79% | +2,99% | +3,61% | -2,92% | +6,47% | PRIMA CALIBRAZIONE |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 33 | 60,61% | +3,69% | +3,75% | -2,81% | +7,01% | PRIMA CALIBRAZIONE |
| SOL | 7g | Tecnico | CALIBRABILE | 37 | 32,43% | +3,11% | -3,66% | -2,99% | +6,65% | PRIMA CALIBRAZIONE |
| SOL | 7g | Classic technical | CALIBRABILE | 21 | 42,86% | -0,04% | +0,04% | -3,16% | +3,15% | FEEDBACK RAPIDO |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 0,00% | -3,55% | -3,55% | -4,19% | +1,03% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 29 | 62,07% | +3,08% | +3,34% | -3,30% | +6,57% | FEEDBACK RAPIDO |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 32 | 65,62% | +2,69% | +3,36% | -3,64% | +6,00% | PRIMA CALIBRAZIONE |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 35 | 62,86% | +2,44% | +3,09% | -3,62% | +5,82% | PRIMA CALIBRAZIONE |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 30 | 60,00% | +3,21% | +3,03% | -3,48% | +6,32% | PRIMA CALIBRAZIONE |
| SOL | 10g | Tecnico | CALIBRABILE | 34 | 44,12% | +1,83% | -1,98% | -3,74% | +5,50% | PRIMA CALIBRAZIONE |
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
| SOL | 21g | Global confluence | BENCHMARK | 20 | 60,00% | +4,15% | +2,37% | -5,91% | +9,66% | FEEDBACK RAPIDO |
| SOL | 21g | Famiglia statistica | CALIBRABILE | 23 | 78,26% | +5,64% | +8,07% | -5,66% | +10,25% | FEEDBACK RAPIDO |
| SOL | 21g | Scanner grezzo | DIAGNOSTICO | 26 | 80,77% | +4,67% | +7,45% | -5,71% | +9,52% | FEEDBACK RAPIDO |
| SOL | 21g | Market regime grezzo | DIAGNOSTICO | 21 | 57,14% | +6,43% | +7,24% | -5,35% | +11,11% | FEEDBACK RAPIDO |
| SOL | 21g | Tecnico | CALIBRABILE | 27 | 44,44% | +4,52% | -6,05% | -5,75% | +9,30% | FEEDBACK RAPIDO |
| SOL | 21g | Classic technical | CALIBRABILE | 19 | 42,11% | +8,25% | -8,25% | -5,09% | +12,23% | FEEDBACK RAPIDO |
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

Generato: 2026-08-25 05:32 UTC

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
| BTC | 46 | PRIMA CALIBRAZIONE | 45 | 13 | 0 | 0 | Famiglia statistica | 1g | 57,78% | +0,56% | prima calibrazione possibile, solo modifiche leggere |
| SOL | 46 | PRIMA CALIBRAZIONE | 42 | 14 | 0 | 0 | Tecnico | 1g | 52,38% | +0,40% | prima calibrazione possibile, solo modifiche leggere |
| DOGE | 46 | PRIMA CALIBRAZIONE | 45 | 15 | 0 | 0 | Famiglia statistica | 1g | 60,00% | +0,82% | prima calibrazione possibile, solo modifiche leggere |

## Raccomandazioni per moduli calibrabili

| Asset | Orizzonte | Famiglia | Modulo | Controlli | Accuratezza | Return corretto direzione | Return medio | Drawdown medio | Max gain medio | Raccomandazione | Δ peso suggerito | Confidenza |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | BREVE | Classic technical | 13 | 38,46% | +0,78% | +1,59% | +0,75% | +2,20% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Famiglia statistica | 45 | 57,78% | +0,56% | +0,56% | +0,13% | +1,13% | PESO OK | 0,0 | MEDIA |
| BTC | 1g | BREVE | Microstruttura exchange | 2 | 100,00% | +1,45% | +1,45% | +1,10% | +2,07% | OSSERVA | 0,0 | BASSA |
| BTC | 1g | BREVE | Tecnico | 40 | 40,00% | +0,24% | +0,75% | +0,29% | +1,33% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 2g | BREVE | Classic technical | 12 | 33,33% | +0,88% | +2,14% | +1,61% | +2,98% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Famiglia statistica | 44 | 56,82% | +1,08% | +1,08% | +0,51% | +1,80% | PESO OK | 0,0 | MEDIA |
| BTC | 2g | BREVE | Microstruttura exchange | 2 | 100,00% | +4,54% | +4,54% | +3,15% | +5,05% | OSSERVA | 0,0 | BASSA |
| BTC | 2g | BREVE | Tecnico | 39 | 43,59% | +0,29% | +1,35% | +0,78% | +2,08% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 3g | BREVE | Classic technical | 11 | 36,36% | -0,21% | +3,29% | +0,27% | +4,57% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Famiglia statistica | 43 | 60,47% | +1,54% | +1,54% | -0,81% | +3,11% | PESO OK | 0,0 | MEDIA |
| BTC | 3g | BREVE | Microstruttura exchange | 1 | 100,00% | +1,88% | +1,88% | +1,44% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 3g | BREVE | Tecnico | 38 | 36,84% | -0,21% | +2,01% | -0,55% | +3,52% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 5g | SETTIMANALE | Classic technical | 9 | 22,22% | -4,66% | +8,25% | -0,01% | +9,57% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Famiglia statistica | 41 | 48,78% | +2,58% | +2,58% | -1,43% | +4,69% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 5g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -0,16% | -0,16% | -0,37% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 5g | SETTIMANALE | Tecnico | 36 | 36,11% | -1,62% | +3,09% | -1,16% | +5,24% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 7g | SETTIMANALE | Classic technical | 8 | 0,00% | -11,51% | +11,51% | -0,67% | +13,66% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Famiglia statistica | 39 | 56,41% | +2,78% | +2,78% | -2,06% | +5,22% | PESO OK | 0,0 | MEDIA |
| BTC | 7g | SETTIMANALE | Microstruttura exchange | 1 | 100,00% | +1,77% | +1,77% | -0,79% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 7g | SETTIMANALE | Tecnico | 34 | 29,41% | -3,97% | +3,53% | -1,80% | +5,83% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 10g | SETTIMANALE | Classic technical | 6 | 0,00% | -9,33% | +9,33% | -1,08% | +11,39% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Famiglia statistica | 36 | 52,78% | +2,11% | +2,11% | -2,56% | +4,70% | NON AUMENTARE | 0,0 | MEDIA |
| BTC | 10g | SETTIMANALE | Microstruttura exchange | 1 | 0,00% | -0,43% | -0,43% | -2,30% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 10g | SETTIMANALE | Tecnico | 31 | 32,26% | -1,18% | +2,64% | -2,30% | +5,27% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| BTC | 14g | SWING | Classic technical | 4 | 50,00% | -0,27% | +0,27% | -1,55% | +3,37% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Famiglia statistica | 34 | 55,88% | +3,03% | +3,03% | -2,91% | +6,17% | PESO OK | 0,0 | MEDIA |
| BTC | 14g | SWING | Microstruttura exchange | 1 | 0,00% | -2,25% | -2,25% | -3,05% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 14g | SWING | Tecnico | 29 | 65,52% | +3,72% | +3,77% | -2,64% | +6,95% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Classic technical | 4 | 0,00% | -11,68% | +11,68% | -1,55% | +14,27% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Famiglia statistica | 27 | 55,56% | +3,89% | +3,89% | -2,95% | +7,50% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Microstruttura exchange | 1 | 100,00% | +1,21% | +1,21% | -3,06% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 21g | SWING | Tecnico | 22 | 22,73% | -2,30% | +4,41% | -2,60% | +8,11% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Famiglia statistica | 18 | 72,22% | +5,61% | +5,61% | -3,27% | +9,53% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Microstruttura exchange | 1 | 100,00% | +0,16% | +0,16% | -3,06% | +4,24% | OSSERVA | 0,0 | BASSA |
| BTC | 30g | MEDIO | Tecnico | 15 | 40,00% | -2,30% | +5,34% | -2,97% | +9,75% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Famiglia statistica | 3 | 100,00% | +22,42% | +22,42% | -3,05% | +25,54% | OSSERVA | 0,0 | BASSA |
| BTC | 45g | MEDIO | Tecnico | 2 | 0,00% | -23,38% | +23,38% | -2,93% | +26,09% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Classic technical | 30 | 43,33% | -0,30% | +0,50% | -0,13% | +1,22% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 1g | BREVE | Famiglia statistica | 45 | 60,00% | +0,82% | +0,55% | -0,05% | +1,57% | PESO OK | 0,0 | MEDIA |
| DOGE | 1g | BREVE | Microstruttura exchange | 7 | 71,43% | +2,41% | +2,86% | +1,15% | +3,54% | OSSERVA | 0,0 | BASSA |
| DOGE | 1g | BREVE | Tecnico | 38 | 57,89% | +0,72% | +0,49% | -0,15% | +1,48% | PESO OK | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Classic technical | 29 | 48,28% | -0,85% | +1,15% | +0,37% | +2,14% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Famiglia statistica | 44 | 54,55% | +1,38% | +1,16% | +0,43% | +2,50% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 2g | BREVE | Microstruttura exchange | 6 | 66,67% | +5,43% | +5,87% | +5,07% | +8,56% | OSSERVA | 0,0 | BASSA |
| DOGE | 2g | BREVE | Tecnico | 37 | 64,86% | +1,19% | +0,69% | +0,01% | +1,98% | PESO OK | 0,0 | MEDIA |
| DOGE | 3g | BREVE | Classic technical | 28 | 35,71% | -1,79% | +2,01% | -1,31% | +4,60% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Famiglia statistica | 43 | 55,81% | +2,03% | +1,73% | -1,13% | +4,36% | PESO OK | 0,0 | MEDIA |
| DOGE | 3g | BREVE | Microstruttura exchange | 6 | 66,67% | +4,84% | +5,19% | +0,90% | +8,54% | OSSERVA | 0,0 | BASSA |
| DOGE | 3g | BREVE | Tecnico | 36 | 52,78% | +1,21% | +0,74% | -1,38% | +3,11% | NON AUMENTARE | 0,0 | MEDIA |
| DOGE | 5g | SETTIMANALE | Classic technical | 27 | 44,44% | -3,71% | +3,71% | -1,98% | +7,48% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Famiglia statistica | 41 | 56,10% | +3,48% | +2,86% | -1,95% | +6,37% | PESO OK | 0,0 | MEDIA |
| DOGE | 5g | SETTIMANALE | Microstruttura exchange | 5 | 60,00% | +5,14% | +5,46% | +1,28% | +11,40% | OSSERVA | 0,0 | BASSA |
| DOGE | 5g | SETTIMANALE | Tecnico | 34 | 64,71% | +1,27% | +1,65% | -2,38% | +4,91% | PESO OK | 0,0 | MEDIA |
| DOGE | 7g | SETTIMANALE | Classic technical | 26 | 46,15% | -3,58% | +3,58% | -2,73% | +7,84% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Famiglia statistica | 39 | 61,54% | +3,93% | +2,83% | -2,78% | +6,92% | PESO OK | 0,0 | MEDIA |
| DOGE | 7g | SETTIMANALE | Microstruttura exchange | 4 | 50,00% | +0,36% | +0,63% | -0,50% | +5,72% | OSSERVA | 0,0 | BASSA |
| DOGE | 7g | SETTIMANALE | Tecnico | 33 | 63,64% | +1,79% | +1,75% | -3,12% | +5,79% | PESO OK | 0,0 | MEDIA |
| DOGE | 10g | SETTIMANALE | Classic technical | 23 | 56,52% | -0,32% | +0,32% | -3,55% | +4,70% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Famiglia statistica | 36 | 58,33% | +3,07% | +1,31% | -3,42% | +5,58% | PESO OK | 0,0 | MEDIA |
| DOGE | 10g | SETTIMANALE | Microstruttura exchange | 4 | 75,00% | +0,18% | +0,93% | -1,31% | +5,72% | OSSERVA | 0,0 | BASSA |
| DOGE | 10g | SETTIMANALE | Tecnico | 31 | 67,74% | +2,41% | -0,31% | -3,79% | +3,92% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 14g | SWING | Classic technical | 22 | 63,64% | -0,33% | +0,33% | -4,43% | +5,27% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Famiglia statistica | 34 | 70,59% | +5,43% | +2,68% | -4,07% | +7,96% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| DOGE | 14g | SWING | Microstruttura exchange | 4 | 75,00% | +2,65% | +12,47% | -1,31% | +16,91% | OSSERVA | 0,0 | BASSA |
| DOGE | 14g | SWING | Tecnico | 30 | 66,67% | +0,31% | -0,31% | -4,43% | +4,70% | PESO OK | 0,0 | MEDIA |
| DOGE | 21g | SWING | Classic technical | 20 | 75,00% | -0,03% | +0,03% | -5,18% | +6,01% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Famiglia statistica | 27 | 81,48% | +7,27% | +2,89% | -5,08% | +9,02% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Microstruttura exchange | 2 | 100,00% | +0,76% | +0,76% | -1,85% | +6,57% | OSSERVA | 0,0 | BASSA |
| DOGE | 21g | SWING | Tecnico | 27 | 70,37% | -2,89% | +2,89% | -5,08% | +9,02% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Classic technical | 16 | 68,75% | -3,81% | +3,81% | -5,92% | +10,30% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Famiglia statistica | 18 | 77,78% | +1,99% | +4,53% | -6,13% | +11,19% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Microstruttura exchange | 2 | 100,00% | +31,53% | +31,53% | -1,85% | +40,20% | OSSERVA | 0,0 | BASSA |
| DOGE | 30g | MEDIO | Tecnico | 18 | 66,67% | -4,53% | +4,53% | -6,13% | +11,19% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Classic technical | 3 | 0,00% | -24,66% | +24,66% | -7,62% | +33,25% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Famiglia statistica | 3 | 0,00% | -24,66% | +24,66% | -7,62% | +33,25% | OSSERVA | 0,0 | BASSA |
| DOGE | 45g | MEDIO | Tecnico | 3 | 0,00% | -24,66% | +24,66% | -7,62% | +33,25% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Classic technical | 26 | 53,85% | +0,71% | +0,78% | -0,02% | +1,79% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Famiglia statistica | 40 | 60,00% | +0,42% | +0,44% | -0,14% | +1,36% | PESO OK | 0,0 | MEDIA |
| SOL | 1g | BREVE | Frattale SOL | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Microstruttura exchange | 3 | 66,67% | +1,51% | +1,51% | +0,99% | +5,02% | OSSERVA | 0,0 | BASSA |
| SOL | 1g | BREVE | Tecnico | 42 | 52,38% | +0,40% | +0,43% | -0,20% | +1,30% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Classic technical | 25 | 56,00% | +0,95% | +0,99% | +0,29% | +2,01% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Famiglia statistica | 39 | 48,72% | +0,34% | +0,96% | +0,13% | +1,76% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 2g | BREVE | Frattale SOL | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Microstruttura exchange | 3 | 33,33% | +0,74% | +0,74% | +0,30% | +2,88% | OSSERVA | 0,0 | BASSA |
| SOL | 2g | BREVE | Tecnico | 41 | 43,90% | +0,08% | +0,83% | +0,08% | +1,97% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Classic technical | 24 | 50,00% | +0,89% | +1,11% | -1,53% | +3,13% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Famiglia statistica | 38 | 47,37% | +1,01% | +1,56% | -1,55% | +3,72% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 3g | BREVE | Frattale SOL | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Microstruttura exchange | 3 | 33,33% | +0,33% | +0,33% | -1,17% | +5,20% | OSSERVA | 0,0 | BASSA |
| SOL | 3g | BREVE | Tecnico | 40 | 45,00% | -0,37% | +1,27% | -1,63% | +3,33% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Classic technical | 22 | 54,55% | +0,81% | +1,07% | -2,33% | +3,44% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Famiglia statistica | 36 | 58,33% | +2,77% | +2,57% | -2,23% | +5,54% | PESO OK | 0,0 | MEDIA |
| SOL | 5g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Microstruttura exchange | 2 | 0,00% | -2,33% | -2,33% | -3,87% | +1,03% | OSSERVA | 0,0 | BASSA |
| SOL | 5g | SETTIMANALE | Tecnico | 38 | 42,11% | -1,77% | +2,42% | -2,43% | +5,25% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 7g | SETTIMANALE | Classic technical | 21 | 42,86% | +0,04% | -0,04% | -3,16% | +3,15% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Famiglia statistica | 35 | 65,71% | +3,92% | +3,26% | -2,94% | +6,69% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 7g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Microstruttura exchange | 2 | 0,00% | -3,55% | -3,55% | -4,19% | +1,03% | OSSERVA | 0,0 | BASSA |
| SOL | 7g | SETTIMANALE | Tecnico | 37 | 32,43% | -3,66% | +3,11% | -2,99% | +6,65% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 10g | SETTIMANALE | Classic technical | 21 | 52,38% | +0,08% | -0,08% | -3,74% | +3,68% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Famiglia statistica | 32 | 65,62% | +3,36% | +2,69% | -3,64% | +6,00% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 10g | SETTIMANALE | Frattale SOL | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Microstruttura exchange | 2 | 50,00% | -2,05% | -2,05% | -4,86% | +1,05% | OSSERVA | 0,0 | BASSA |
| SOL | 10g | SETTIMANALE | Tecnico | 34 | 44,12% | -1,98% | +1,83% | -3,74% | +5,50% | NON AUMENTARE | 0,0 | MEDIA |
| SOL | 14g | SWING | Classic technical | 21 | 38,10% | -1,19% | +1,19% | -4,25% | +5,07% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Famiglia statistica | 30 | 83,33% | +5,75% | +4,50% | -4,13% | +8,56% | POSSIBILE AUMENTO LEGGERO | +0,25 | MEDIA |
| SOL | 14g | SWING | Frattale SOL | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Microstruttura exchange | 2 | 50,00% | +8,38% | +8,38% | -5,94% | +13,89% | OSSERVA | 0,0 | BASSA |
| SOL | 14g | SWING | Tecnico | 32 | 34,38% | -2,63% | +2,00% | -4,32% | +6,56% | POSSIBILE RIDUZIONE LEGGERA | -0,25 | MEDIA |
| SOL | 21g | SWING | Classic technical | 19 | 42,11% | -8,25% | +8,25% | -5,09% | +12,23% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Famiglia statistica | 23 | 78,26% | +8,07% | +5,64% | -5,66% | +10,25% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Frattale SOL | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Microstruttura exchange | 1 | 0,00% | -3,18% | -3,18% | -9,62% | +0,62% | OSSERVA | 0,0 | BASSA |
| SOL | 21g | SWING | Tecnico | 27 | 44,44% | -6,05% | +4,52% | -5,75% | +9,30% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Classic technical | 10 | 20,00% | -12,27% | +12,27% | -6,72% | +16,87% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Famiglia statistica | 14 | 78,57% | +7,66% | +8,41% | -7,61% | +12,92% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Frattale SOL | 1 | 0,00% | -4,50% | -4,50% | -9,39% | +1,96% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Microstruttura exchange | 1 | 100,00% | +8,54% | +8,54% | -9,62% | +9,47% | OSSERVA | 0,0 | BASSA |
| SOL | 30g | MEDIO | Tecnico | 18 | 22,22% | -7,69% | +6,65% | -7,44% | +10,90% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Famiglia statistica | 2 | 0,00% | -20,01% | +20,01% | -9,20% | +27,34% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Frattale SOL | 1 | 100,00% | +19,26% | +19,26% | -9,39% | +23,73% | OSSERVA | 0,0 | BASSA |
| SOL | 45g | MEDIO | Tecnico | 3 | 100,00% | +23,88% | +23,88% | -9,18% | +28,69% | OSSERVA | 0,0 | BASSA |

## Moduli esclusi dalle proposte di peso

| Modulo | Ruolo | Famiglia madre | Controlli max | Motivo esclusione |
| --- | --- | --- | --- | --- |
| Global confluence | BENCHMARK | nessuna | 43 | Risultato finale del Global: benchmark, non peso interno. |
| Market regime grezzo | DIAGNOSTICO | statistical_family | 38 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |
| Scanner grezzo | DIAGNOSTICO | statistical_family | 45 | Già incluso in statistical_family; nessuna proposta di peso autonoma. |

## Sintesi per famiglia temporale

| Asset | Famiglia | Modulo calibrabile | Controlli totali | Accuratezza media ponderata | Return corretto direzione |
| --- | --- | --- | --- | --- | --- |
| BTC | BREVE | Classic technical | 36 | 36,11% | +0,51% |
| BTC | BREVE | Famiglia statistica | 132 | 58,33% | +1,05% |
| BTC | BREVE | Microstruttura exchange | 5 | 100,00% | +2,77% |
| BTC | BREVE | Tecnico | 117 | 40,17% | +0,11% |
| BTC | SETTIMANALE | Classic technical | 23 | 8,70% | -8,26% |
| BTC | SETTIMANALE | Famiglia statistica | 116 | 52,59% | +2,50% |
| BTC | SETTIMANALE | Microstruttura exchange | 3 | 33,33% | +0,39% |
| BTC | SETTIMANALE | Tecnico | 101 | 32,67% | -2,27% |
| BTC | SWING | Classic technical | 8 | 25,00% | -5,98% |
| BTC | SWING | Famiglia statistica | 61 | 55,74% | +3,41% |
| BTC | SWING | Microstruttura exchange | 2 | 50,00% | -0,52% |
| BTC | SWING | Tecnico | 51 | 47,06% | +1,12% |
| BTC | MEDIO | Famiglia statistica | 21 | 76,19% | +8,01% |
| BTC | MEDIO | Microstruttura exchange | 1 | 100,00% | +0,16% |
| BTC | MEDIO | Tecnico | 17 | 35,29% | -4,78% |
| DOGE | BREVE | Classic technical | 87 | 42,53% | -0,96% |
| DOGE | BREVE | Famiglia statistica | 132 | 56,82% | +1,40% |
| DOGE | BREVE | Microstruttura exchange | 19 | 68,42% | +4,13% |
| DOGE | BREVE | Tecnico | 111 | 58,56% | +1,04% |
| DOGE | SETTIMANALE | Classic technical | 76 | 48,68% | -2,64% |
| DOGE | SETTIMANALE | Famiglia statistica | 116 | 58,62% | +3,50% |
| DOGE | SETTIMANALE | Microstruttura exchange | 13 | 61,54% | +2,14% |
| DOGE | SETTIMANALE | Tecnico | 98 | 65,31% | +1,80% |
| DOGE | SWING | Classic technical | 42 | 69,05% | -0,19% |
| DOGE | SWING | Famiglia statistica | 61 | 75,41% | +6,25% |
| DOGE | SWING | Microstruttura exchange | 6 | 83,33% | +2,02% |
| DOGE | SWING | Tecnico | 57 | 68,42% | -1,20% |
| DOGE | MEDIO | Classic technical | 19 | 57,89% | -7,10% |
| DOGE | MEDIO | Famiglia statistica | 21 | 66,67% | -1,82% |
| DOGE | MEDIO | Microstruttura exchange | 2 | 100,00% | +31,53% |
| DOGE | MEDIO | Tecnico | 21 | 57,14% | -7,40% |
| SOL | BREVE | Classic technical | 75 | 53,33% | +0,85% |
| SOL | BREVE | Famiglia statistica | 117 | 52,14% | +0,58% |
| SOL | BREVE | Frattale SOL | 3 | 0,00% | -0,79% |
| SOL | BREVE | Microstruttura exchange | 9 | 44,44% | +0,86% |
| SOL | BREVE | Tecnico | 123 | 47,15% | +0,04% |
| SOL | SETTIMANALE | Classic technical | 64 | 50,00% | +0,32% |
| SOL | SETTIMANALE | Famiglia statistica | 103 | 63,11% | +3,34% |
| SOL | SETTIMANALE | Frattale SOL | 3 | 0,00% | -3,03% |
| SOL | SETTIMANALE | Microstruttura exchange | 6 | 16,67% | -2,65% |
| SOL | SETTIMANALE | Tecnico | 109 | 39,45% | -2,48% |
| SOL | SWING | Classic technical | 40 | 40,00% | -4,54% |
| SOL | SWING | Famiglia statistica | 53 | 81,13% | +6,76% |
| SOL | SWING | Frattale SOL | 2 | 0,00% | -3,49% |
| SOL | SWING | Microstruttura exchange | 3 | 33,33% | +4,53% |
| SOL | SWING | Tecnico | 59 | 38,98% | -4,20% |
| SOL | MEDIO | Classic technical | 10 | 20,00% | -12,27% |
| SOL | MEDIO | Famiglia statistica | 16 | 68,75% | +4,20% |
| SOL | MEDIO | Frattale SOL | 2 | 50,00% | +7,38% |
| SOL | MEDIO | Microstruttura exchange | 1 | 100,00% | +8,54% |
| SOL | MEDIO | Tecnico | 21 | 33,33% | -3,18% |

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
| BTC     |         46 |              18 |          28 | RACCOLTA DATI | 0,00%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| SOL     |         46 |              18 |          28 | RACCOLTA DATI | 5,56%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |
| DOGE    |         46 |              18 |          28 | RACCOLTA DATI | 5,56%            | 0,00%           | 0,00%                 | RISCHIO FORSE TROPPO SEVERO |

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

Generato: 2026-08-25 05:32 UTC


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
| BTC | +6 | MODERATAMENTE POSITIVA | Costruttivo prudente | MEDIA | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE | Prima resistenza sopra 82.792; conferma del doppio minimo sopra 66.910. | Sotto 62.488 il quadro tecnico peggiora. |
| SOL | +6 | MODERATAMENTE POSITIVA | Costruttivo prudente | MEDIA | HOLD / TRANCHE PICCOLE, NO LEVA | Doppio minimo target raggiunto finché mantiene 78,73; nuova conferma tecnica sopra 127,97; milestone analogiche 116,62 / 139,27, valide soltanto se rientra anche il gap frattale. | Allarmi sotto 94,82 / 74,20 / 62,19. |
| DOGE | +5 | MODERATAMENTE POSITIVA | Costruttivo prudente | MEDIA | SOLO TRANCHE PICCOLE / NO LEVA | Sopra 0.11825 migliora; sopra 0.06933 viene invalidato il pattern ribassista dominante. | Sotto 0.06895 il rischio ribassista aumenta. |

## Punteggi per modulo

| Asset | Scanner grezzo | Market grezzo | Famiglia statistica | Scanner path | Tecnico | Classic tech | Frattale SOL | Fractal path | RSI top-cycle | Lifecycle EMA | Exchange flow | Futures | Daily change | Totale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +2 | 0 | +2 | 0 | +3 | +1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | +6 |
| SOL | +1 | 0 | +1 | 0 | +3 | +1 | 0 | 0 | 0 | 0 | 0 | 0 | +1 | +6 |
| DOGE | +1 | 0 | +1 | 0 | +3 | +1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | +5 |

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
- Scanner (diagnostico, già incluso nella Famiglia statistica): **+2** — Casi positivi 62,50%, return centrale 30g +7,69%. Direzione scanner: SALITA. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **0** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 0, positivi 30g n/a, return p50 n/a.
- Scanner path: **0** — Controlli disponibili 44. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **+3** — Score tecnico 11/12, verdetto rialzista tecnico, trend rialzista, struttura compressione / triangolo, divergenza rialzista nascosta rsi, Wyckoff markup / fase rialzista, pattern score 0 (rialzista Doppio minimo / TARGET RAGGIUNTO; ribassista Doppio massimo / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **+1** — Score classico 12/12, verdetto CONFERMATO RIALZISTA, stage STAGE 3 / DISTRIBUZIONE O PAUSA, struttura MASSIMI E MINIMI CRESCENTI, Wyckoff SIGN OF STRENGTH POSSIBILE, volatilità locale MEDIO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Non applicabile a questo asset.
- Fractal path: **0** — Non applicabile a questo asset.
- RSI top-cycle: **0** — Non applicabile a questo asset.
- Lifecycle EMA: **0** — Non applicabile a questo asset.
- Exchange flow: **0** — Flow +1.75, derivati +1.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +0.50; exchange 3/3, copertura 100%, consenso bull 2, bear 1, divergenze 0, campioni 4h 9 su 4.00h; candidato +1, peso Global +0 (LOCKED / RACCOLTA 7G). Bias POSITIVA / CANDIDATA, ANCORA NON PESATA; confidenza MEDIA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +1 resta misurato separatamente.
- Futures: **0** — Lettura futures Rischio sotto, forza 2/5.
- Daily change: **0** — BTC: nessun cambiamento forte in miglioramento rispetto a ieri.

Conferme: Prima resistenza sopra 82.792; conferma del doppio minimo sopra 66.910.

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
- Scanner (diagnostico, già incluso nella Famiglia statistica): **+1** — Casi positivi 55,00%, return centrale 30g +3,87%. Direzione scanner: INCERTO. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **0** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 0, positivi 30g n/a, return p50 n/a.
- Scanner path: **0** — Controlli disponibili 44. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **+3** — Score tecnico 10/12, verdetto rialzista tecnico, trend rialzista, struttura compressione / triangolo, divergenza nessuna, Wyckoff markup / fase rialzista, pattern score 0 (rialzista Doppio minimo / TARGET RAGGIUNTO; ribassista Doppio massimo / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **+1** — Score classico 12/12, verdetto CONFERMATO RIALZISTA, stage STAGE 3 / DISTRIBUZIONE O PAUSA, struttura MASSIMI E MINIMI CRESCENTI, Wyckoff SIGN OF STRENGTH POSSIBILE, volatilità locale BASSO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Verdetto ANALOGIA DEBOLE / SCENARIO SECONDARIO, somiglianza strutturale +63,53%, aderenza live +71,07%, errore live +14,47%, gap corrente +19,23%, peso operativo 0, tracking STRUTTURA STABILE, fase FRATTALE SOLO DI CONTESTO, rischio ALTO.
- Fractal path: **0** — Controlli disponibili 40, ma percorso ancorato non aderente: gap +19,23%, errore live +14,47%. Peso 0.
- RSI top-cycle: **0** — Rischio top-cycle RSI: BASSO.
- Lifecycle EMA: **0** — Contesto non pesato nel Global. Lifecycle score 2, bias CONTESTO DA OSSERVARE, EMA200 111,39 $, upside EMA200 +8,90%, gap EMA50/EMA200 -5,79%, hit EMA200 12w +70,00%, trend PEGGIORAMENTO FORTE. Peso Global forzato a 0.
- Exchange flow: **0** — Flow +1.75, derivati +1.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +1.00; exchange 3/3, copertura 100%, consenso bull 2, bear 1, divergenze 0, campioni 4h 9 su 4.00h; candidato +1, peso Global +0 (LOCKED / RACCOLTA 7G). Bias POSITIVA / CANDIDATA, ANCORA NON PESATA; confidenza ALTA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +1 resta misurato separatamente.
- Futures: **0** — Lettura futures Rischio sotto, forza 2/5.
- Daily change: **+1** — SOL: cambiamento medio in miglioramento rispetto a ieri.

Conferme: Doppio minimo target raggiunto finché mantiene 78,73; nuova conferma tecnica sopra 127,97; milestone analogiche 116,62 / 139,27, valide soltanto se rientra anche il gap frattale.

Invalidazioni: Allarmi sotto 94,82 / 74,20 / 62,19.

### DOGE

- Confluenza: **MODERATAMENTE POSITIVA**
- Bias: **Costruttivo prudente**
- Punteggio finale: **+5**
- Affidabilità: **MEDIA**
- Azione coerente: **SOLO TRANCHE PICCOLE / NO LEVA**

DOGE non ha ancora una confluenza pulita. Serve conferma tecnica prima di trattarlo come asset forte.

Dettaglio moduli:

- Famiglia statistica: **+1** — Scanner grezzo +1, Market Regime grezzo 0, match regime 0. Regime ignorato: meno di 5 match utili. Punteggio contato nel Global: +1.
- Scanner (diagnostico, già incluso nella Famiglia statistica): **+1** — Casi positivi 55,00%, return centrale 30g +1,55%. Direzione scanner: INCERTO. Fonte: latest_scanner_summary strutturato.
- Market regime (diagnostico, già incluso nella Famiglia statistica): **0** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 0, positivi 30g n/a, return p50 n/a.
- Scanner path: **0** — Controlli disponibili 44. Il cono previsionale inizia a essere valutabile, ma resta secondario.
- Tecnico: **+3** — Score tecnico 7/12, verdetto rialzista tecnico, trend misto, struttura rialzista con massimi e minimi crescenti, divergenza nessuna, Wyckoff range / fase non chiara, pattern score 0 (rialzista Triplo minimo / TARGET RAGGIUNTO; ribassista Doppio massimo / CANDIDATO). Fonte: technical_structure_metrics.csv.
- Classic technical: **+1** — Score classico 6/12, verdetto COSTRUTTIVO / CONFERMA PARZIALE, stage STAGE 3 / DISTRIBUZIONE O PAUSA, struttura MASSIMI E MINIMI CRESCENTI, Wyckoff RANGE / FASE NON CHIARA, volatilità locale MEDIO. Peso Global limitato a ±1 perché è un filtro di conferma.
- Frattale SOL: **0** — Non applicabile a questo asset.
- Fractal path: **0** — Non applicabile a questo asset.
- RSI top-cycle: **0** — Non applicabile a questo asset.
- Lifecycle EMA: **0** — Non applicabile a questo asset.
- Exchange flow: **0** — Flow +1.75, derivati +0.00, affollamento +0.00, liquidazioni +0.00, conferme tecniche +0.50; exchange 3/3, copertura 100%, consenso bull 1, bear 2, divergenze 0, campioni 4h 9 su 4.00h; candidato +0, peso Global +0 (LOCKED / RACCOLTA 7G). Bias LEGGERMENTE POSITIVA / NON PESATA; confidenza BASSA; fonti 3/3; KuCoin OK; copertura 100,00%. Attivazione: LOCKED / RACCOLTA 7G. Il Global usa +0; il candidato +0 resta misurato separatamente.
- Futures: **0** — Lettura futures Rischio sotto, forza 2/5.
- Daily change: **0** — DOGE: nessun cambiamento forte in miglioramento rispetto a ieri.

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

Generato: 2026-08-25 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [btc_macro_cycle_report.md](btc_macro_cycle_report.md)

Questo modulo descrive il contesto macro di Bitcoin. Non genera entrate tattiche, non autorizza leva e pesa **0** nel Global Confluence.

## Sintesi

| Voce | Valore | Lettura |
| --- | --- | --- |
| Prezzo BTC | 80.775 $ | prezzo corrente |
| Power Law centrale | 124.011 $ | deviazione -34,86% |
| Banda p10-p90 | 76.984 $ / 313.281 $ | BASSA NEL CORRIDOIO |
| Percentile residuo | 14,84% | posizione storica nel corridoio |
| Esponente β | 5,8128 | R² log-log 91,93% |
| Stabilità β | BASSA | range 1,3164 cambiando finestra |
| Ultimo halving | 2024-04-19 | 858 giorni fa |
| Fase ciclo | 58,73% | percentuale indicativa del ciclo quadriennale |
| Peso Global | 0 | CONTESTO MACRO / DIAGNOSTICO |

La Power Law viene trattata come regressione empirica, non come legge fisica. Il report mostra quanto cambia l'esponente usando finestre iniziali diverse e la confronta con il benchmark ingenuo 'prezzo invariato'.

## Bitcoin Power Law

- Campione: 2014-09-17 → 2026-08-25 (4360 osservazioni)
- Formula stimata: prezzo ≈ exp(-39.1323) × giorni^5.8128
- Prezzo centrale oggi: **124.011 $**
- Posizione corrente: **BASSA NEL CORRIDOIO**, percentile 14,84%
- Scarto dal centro: **-34,86%**

![Bitcoin Power Law](btc_power_law_chart.png)

![Bitcoin Power Law log-log](btc_power_law_loglog_chart.png)

### Stabilità dell'esponente

| Inizio campione | β | R² log-log |
| --- | --- | --- |
| 2014 | 5,8128 | 91,93% |
| 2015 | 5,8961 | 91,48% |
| 2016 | 5,5812 | 87,72% |
| 2017 | 4,8519 | 82,87% |
| 2018 | 4,5798 | 78,34% |

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
| 2012-11-28 → 2016-07-09 | 2015-01-12 | -18,15% | -11,82% | +9,45% | +62,69% |
| 2016-07-09 → 2020-05-11 | 2018-10-10 | -3,04% | -38,79% | -19,68% | +30,38% |
| 2020-05-11 → 2024-04-19 | 2022-09-03 | -1,05% | -13,83% | +18,37% | +30,95% |

Campione molto piccolo: questi rendimenti sono contesto di ciclo, non probabilità affidabili.

## SOL/BTC e DOGE/BTC dentro il tempo Bitcoin

![Altcoin nel ciclo BTC](alt_btc_cycle_spirals.png)

| Asset | Coppia | Forza vs BTC | Score raw | Candidato | 30g | Peso Global |
| --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | SOVRAPERFORMA BTC | 4 | 1 | 10.025935362427973 | 0 |
| DOGE | DOGE/BTC | RELATIVA MISTA / NON CONFERMATA | -2 | 0 | 3.251275182301039 | 0 |

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

Generato: 2026-08-25 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [relative_strength_btc_report.md](relative_strength_btc_report.md)

Questo modulo controlla se SOL e DOGE stanno davvero battendo Bitcoin. Una salita in USD accompagnata da una coppia ALT/BTC ribassista è spesso soltanto trascinamento di BTC.

**Protezione iniziale:** il candidato relativo è limitato a -1/0/+1, ma il peso nel Global resta **0**. La coppia BTC conferma o indebolisce il tecnico USD; non viene sommata come secondo modulo indipendente.

## Sintesi

| Asset | Coppia | Prezzo | Score raw | Candidato | Peso Global | Forza vs BTC | Confidenza | 30g | Tecnico USD | Lettura combinata |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | 0.00127300 | +4 | +1 | 0 | SOVRAPERFORMA BTC | BASSA | +10,03% | RIALZISTA | CONFERMA FORTE: sale in USD e batte BTC |
| DOGE | DOGE/BTC | 0.00000115 | -2 | 0 | 0 | RELATIVA MISTA / NON CONFERMATA | BASSA | +3,25% | RIALZISTA | QUADRO MISTO / NESSUNA CONFERMA RELATIVA |

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
- **Rendimenti relativi:** 7g +8,06%; 30g +10,03%; 90g +15,52%; 180g -1,55%
- **Daily:** RSI 69.33; MA50 0.00118740; MA200 0.00117740
- **Weekly:** MA30 0.00118227; RSI 54.72
- **Livelli:** supporto 0.00122200; resistenza 0.00134900; breakout 60g 0.00134900; breakdown 60g 0.00109300
- **Pattern:** DOPPIO MINIMO / TARGET RAGGIUNTO; neckline 0.00120200; target 0.00125350
- **Fibonacci:** VICINO — 23.6% a 0.00126876
- **Fonte:** Yahoo Finance SOL-BTC (coppia diretta)
- **Motivi score:** prezzo sopra MA50 daily; prezzo sopra MA200 daily; prezzo sopra MA30 weekly; MA30 weekly in discesa; RSI relativo forte; MACD relativo positivo

![Grafico SOL/BTC](relative_strength_SOLBTC.png)

## DOGE/BTC

- **Verdetto relativo:** RELATIVA MISTA / NON CONFERMATA (-2)
- **Candidato futuro:** 0; **peso attuale Global: 0**
- **Lettura combinata USD/BTC:** QUADRO MISTO / NESSUNA CONFERMA RELATIVA
- **Struttura:** VOLATILITÀ IN ESPANSIONE
- **Rendimenti relativi:** 7g +5,52%; 30g +3,25%; 90g -13,53%; 180g -22,37%
- **Daily:** RSI 55.57; MA50 0.00000112; MA200 0.00000129
- **Weekly:** MA30 0.00000128; RSI 39.64
- **Livelli:** supporto 0.00000112; resistenza 0.00000115; breakout 60g 0.00000135; breakdown 60g 0.00000100
- **Pattern:** DOPPIO MINIMO / TARGET RAGGIUNTO; neckline 0.00000115; target 0.00000128
- **Fibonacci:** NON ATTIVO — 23.6% a 0.00000112
- **Fonte:** Rapporto sintetico DOGE-USD / BTC-USD (sintetica)
- **Motivi score:** prezzo sopra MA50 daily; prezzo sotto MA200 daily; MA50 daily in discesa; prezzo sotto MA30 weekly; MA30 weekly in discesa; MACD relativo positivo

![Grafico DOGE/BTC](relative_strength_DOGEBTC.png)

## Backtest storico diagnostico

Il backtest usa soltanto indicatori disponibili alla data del segnale e campiona una volta a settimana. È utile subito, ma non sostituisce il tracker live: le soglie sono state definite prima di vedere il risultato.

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto direzione | Return futuro mediano |
| --- | --- | --- | --- | --- | --- |
| SOL | 7g | 205 | 52,20% | +1,94% | -1,06% |
| SOL | 30g | 203 | 47,29% | +4,59% | +0,36% |
| SOL | 90g | 198 | 53,03% | +10,08% | +2,72% |
| DOGE | 7g | 294 | 55,78% | +1,84% | -1,68% |
| DOGE | 30g | 292 | 53,08% | +2,00% | -3,71% |
| DOGE | 90g | 286 | 53,85% | +6,84% | -8,85% |

## Tracker live e gate futuro

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto | Stato | Peso Global |
| --- | --- | --- | --- | --- | --- | --- |
| SOL | 1g | 21 | 66,67% | +0,18% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 3g | 19 | 52,63% | -0,18% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 7g | 16 | 37,50% | -1,41% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 14g | 15 | 6,67% | -3,37% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 30g | 3 | 0,00% | -8,42% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 1g | 35 | 68,57% | +0,02% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 3g | 35 | 60,00% | +0,21% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 7g | 34 | 64,71% | +0,52% | ELIGIBILE FUTURO ±1 | 0 |
| DOGE | 14g | 32 | 65,62% | -0,06% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 30g | 16 | 68,75% | +0,10% | LOCKED / RACCOLTA LIVE | 0 |

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
| Prezzo SOL | 102,48 $ |  |
| Weekly RSI | 58,25 / linea grezza 52,71 | LINEA NON AFFIDABILE / RISCHIO NON ATTIVO — IRREALISTICA / NON OPERATIVA |
| Monthly RSI | 46,88 / linea grezza 55,81 | RSI TROPPO BASSO PER RISCHIO TOP — VALIDA / USO PRUDENTE |
| Target ciclo base | 585,94 $ | Avanzamento +17,49% |
| Rischio top-cycle RSI | BASSO | Nessun segnale top-cycle macro attivo. Prezzo ancora lontano dal target ciclo; il filtro RSI resta solo di monitoraggio. |

## Lettura semplice

- Weekly: La top-line weekly non supera i controlli di qualità. Non viene usata per generare rischio top-cycle.
- Monthly: RSI monthly è 46,9, sotto la soglia prudente 55. Anche se fosse vicino alla linea, non è una vera zona di esaurimento ciclo.
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
| Prezzo SOL | 102,48 $ |
| TVL Solana | 5,79 mld $ |
| TVL 7g | +19,32% |
| DEX volume 24h | 2,99 mld $ |
| Fees 24h | 13,70 mln $ |
| Stablecoin su Solana | 16,36 mld $ |
| Stake ratio | 68,75% |
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

| Voce                      | Valore                       |
|:--------------------------|:-----------------------------|
| Lifecycle squeeze score | 2 |
| Bias | CONTESTO DA OSSERVARE |
| Azione coerente | SOLO OSSERVAZIONE |
| Peso suggerito Global | 0 |
| Trend squeeze | PEGGIORAMENTO FORTE |
| Trend squeeze score | -1 |
| Confronto precedente | 2026-08-24 |
| Fonte prezzi | Yahoo Finance SOL-USD weekly |
| Prezzo SOL | 102,48 $ |
| EMA200 weekly target | 111,39 $ |
| Upside verso EMA200 | +8,90% |
| Distanza prezzo da EMA200 | -8,17% |
| Gap EMA50/EMA200 | -5,79% |
| Stato cross | EMA50 SOTTO EMA200 |
| RSI weekly | 58,16 |
| Età SOL | 6,4 anni |
| Analoghi storici usati | 30 |
| Max analoghi per asset | 3 |
| Hit EMA200 12w analoghi | +70,00% |
| Max gain mediano 12w | +20,01% |
| Drawdown mediano 12w | -40,13% |

Lettura semplice:

**SOLO OSSERVAZIONE**

Autocontrollo: **PEGGIORAMENTO FORTE**.

Questo modulo confronta SOL con altre crypto in fasi simili di età, distanza da EMA200, EMA50/EMA200 e RSI. Non usa stock market.

Nota importante: **questo modulo ora NON pesa più nel Global Confluence**. Resta solo come contesto di ciclo e come mappa verso EMA200 weekly. Il punteggio Global resta guidato da prezzo, scanner, regime, struttura tecnica, frattale, RSI e conferme reali.

Nota: se EMA50/EMA200 sono dentro ±2%, il modulo parla di medie sovrapposte / incrocio in corso, perché exchange diversi possono mostrare il cross leggermente prima o dopo.

<!-- Generato: 2026-08-25 05:32 UTC -->
<!-- MAJOR_ALT_LIFECYCLE_SQUEEZE_END -->

</details>
<!-- COMPACT_SECTION_END:major_alt_lifecycle -->

# Report giornaliero BTC / SOL / DOGE

Aggiornato il: **2026-08-25 05:30:23 UTC**

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
- DOGE: nessun cambiamento forte rispetto a ieri.

| Asset | Cambio | Tono | Verdetto oggi | Casi positivi oggi | Δ casi positivi |
| --- | --- | --- | --- | --- | --- |
| BTC | NESSUN CAMBIAMENTO FORTE | miglioramento | RIALZISTA | +62.50% | +2.50 punti |
| SOL | CAMBIAMENTO MEDIO | miglioramento | NEUTRALE / INCERTO | +55.00% | +2.50 punti |
| DOGE | NESSUN CAMBIAMENTO FORTE | miglioramento | NEUTRALE / INCERTO | +55.00% | +2.50 punti |

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
| BTC | 76.539 $ | 88.625 $ | +39,29% | +15,79% | rimbalzo debole | 88.625 $ | 76.539 $ | +37,04% | -13,64% | scarico possibile |
| SOL | 97,36 $ | 112,73 $ | +42,42% | +15,79% | rimbalzo debole | 112,73 $ | 97,36 $ | +28,00% | -13,64% | spike storicamente più resistente |
| DOGE | 0,08825 $ | 0,10218 $ | +55,56% | +15,79% | rimbalzo possibile | 0,10218 $ | 0,08825 $ | +32,35% | -13,64% | spike storicamente più resistente |

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

- **BTC: su 40 casi simili, 28 prima sono scesi a -5,00%. Tra quei 28, 11 poi sono rimbalzati fino a +10,00%. Percentuale: +39,29% (11/28). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.**
- **BTC: su 40 casi simili, 27 prima sono saliti a +10,00%. Tra quei 27, 10 poi sono scaricati a -5,00%. Percentuale: +37,04% (10/27). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: scarico possibile.**
- **SOL: su 40 casi simili, 33 prima sono scesi a -5,00%. Tra quei 33, 14 poi sono rimbalzati fino a +10,00%. Percentuale: +42,42% (14/33). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.**
- **SOL: su 40 casi simili, 25 prima sono saliti a +10,00%. Tra quei 25, 7 poi sono scaricati a -5,00%. Percentuale: +28,00% (7/25). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.**
- **DOGE: su 40 casi simili, 27 prima sono scesi a -5,00%. Tra quei 27, 15 poi sono rimbalzati fino a +10,00%. Percentuale: +55,56% (15/27). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo possibile.**
- **DOGE: su 40 casi simili, 34 prima sono saliti a +10,00%. Tra quei 34, 11 poi sono scaricati a -5,00%. Percentuale: +32,35% (11/34). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.**

<!-- BOUNCE_AFTER_DRAWDOWN_END -->

</details>
<!-- COMPACT_SECTION_END:bounce_after_drawdown -->

<!-- COMPACT_SECTION_START:scanner_forecast -->
<details>
<summary><strong>🔭 Cono probabilistico dello scanner</strong></summary>

<!-- SCANNER_FORECAST_TRACKER_START -->
# Scanner forecast path / cono probabilistico

Generato: 2026-08-25 05:31:42 UTC


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
| BTC | 2026-08-25 | 80.568 $ | SALITA | 62,50% | 70.503,48 $ | 74.292,10 $ | 86.764,34 $ | 93.821,62 $ | 114.970,46 $ |
| SOL | 2026-08-25 | 102,48 $ | INCERTO | 55,00% | 87,61 $ | 93,61 $ | 106,45 $ | 120,27 $ | 162,09 $ |
| DOGE | 2026-08-25 | 0.09289 $ | INCERTO | 55,00% | 0.07321 $ | 0.08393 $ | 0.09433 $ | 0.11046 $ | 0.13219 $ |

## Grafici

### BTC

![Scanner forecast BTC](scanner_forecast_BTC.png)

#### Verifica storica e discrepanza

![Verifica storica cono BTC](scanner_forecast_history_BTC.png)

- Cono congelato il **2026-07-26**; verificato fino al **2026-08-25**; stato **COMPLETO 30/30g**.
- Reale **80.639,17 $**; p50 previsto **70.778,63 $**; scarto **13,93%**.
- Errore medio assoluto **4,77%**; massimo **18,38%**; DENTRO p10-p90; FUORI p25-p75.

### SOL

![Scanner forecast SOL](scanner_forecast_SOL.png)

#### Verifica storica e discrepanza

![Verifica storica cono SOL](scanner_forecast_history_SOL.png)

- Cono congelato il **2026-07-26**; verificato fino al **2026-08-25**; stato **COMPLETO 30/30g**.
- Reale **102,49 $**; p50 previsto **79,00 $**; scarto **29,74%**.
- Errore medio assoluto **6,40%**; massimo **32,11%**; DENTRO p10-p90; FUORI p25-p75.

### DOGE

![Scanner forecast DOGE](scanner_forecast_DOGE.png)

#### Verifica storica e discrepanza

![Verifica storica cono DOGE](scanner_forecast_history_DOGE.png)

- Cono congelato il **2026-07-26**; verificato fino al **2026-08-25**; stato **COMPLETO 30/30g**.
- Reale **0.09290 $**; p50 previsto **0.07652 $**; scarto **21,40%**.
- Errore medio assoluto **9,07%**; massimo **28,57%**; DENTRO p10-p90; FUORI p25-p75.

## Accuratezza percorso scanner

| Asset   | Giorno   |   Controlli | Dentro p10-p90   | Dentro p25-p75   | Errore medio abs vs p50   | Errore medio vs p50   |
|:--------|:---------|------------:|:-----------------|:-----------------|:--------------------------|:----------------------|
| BTC | 1g | 44 | 93,18% | 54,55% | 2,39% | 0,97% |
| BTC | 3g | 42 | 88,10% | 71,43% | 3,56% | 1,38% |
| BTC | 7g | 38 | 89,47% | 73,68% | 5,32% | 2,49% |
| BTC | 14g | 33 | 96,97% | 72,73% | 5,18% | 2,27% |
| BTC | 30g | 17 | 100,00% | 82,35% | 7,39% | -0,38% |
| SOL | 1g | 44 | 72,73% | 56,82% | 3,18% | 1,33% |
| SOL | 3g | 42 | 85,71% | 66,67% | 4,16% | 1,58% |
| SOL | 7g | 38 | 86,84% | 78,95% | 4,84% | 2,88% |
| SOL | 14g | 33 | 90,91% | 72,73% | 6,52% | 5,40% |
| SOL | 30g | 17 | 94,12% | 64,71% | 9,77% | 9,01% |
| DOGE | 1g | 44 | 88,64% | 63,64% | 3,28% | 1,50% |
| DOGE | 3g | 42 | 88,10% | 76,19% | 4,64% | 3,36% |
| DOGE | 7g | 38 | 81,58% | 78,95% | 9,10% | 7,47% |
| DOGE | 14g | 33 | 81,82% | 57,58% | 11,45% | 10,22% |
| DOGE | 30g | 17 | 88,24% | 35,29% | 19,16% | 19,16% |

## Calibratore shadow

Il cono ufficiale resta grezzo e invariato. Il calibratore usa soltanto previsioni passate già mature, campionate una volta a settimana per ridurre la falsa indipendenza. Ogni orizzonte si attiva a 30 controlli indipendenti: parte al 25% della correzione stimata e cresce gradualmente fino al 100% a 100 controlli.

| Asset   | Orizzonte   |   Controlli indipendenti |   Soglia | Stato                  | Forza correzione   | Shift p50   |   Scala p10-p90 |
|:--------|:------------|-------------------------:|---------:|:-----------------------|:-------------------|:------------|----------------:|
| BTC | 1g | 8 | 30 | RACCOLTA (22 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 3g | 7 | 30 | RACCOLTA (23 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 7g | 7 | 30 | RACCOLTA (23 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 14g | 6 | 30 | RACCOLTA (24 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 30g | 3 | 30 | RACCOLTA (27 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 1g | 8 | 30 | RACCOLTA (22 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 3g | 7 | 30 | RACCOLTA (23 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 7g | 7 | 30 | RACCOLTA (23 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 14g | 6 | 30 | RACCOLTA (24 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 30g | 3 | 30 | RACCOLTA (27 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 1g | 8 | 30 | RACCOLTA (22 mancanti) | 0,0% | 0,00% | 1,000 |
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

Righe salvate nello storico: **126**.

Questa sezione tiene un diario delle previsioni giornaliere a 30 giorni, senza appesantire il report principale.

| Data | Asset | Prezzo | Direzione | Casi positivi | Return p50 | Drawdown p50 | Max gain p50 | Controllo 30g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08-25 | BTC | 80.568 $ | SALITA | 62,50% | 86.764 $ | 74.650 $ | 93.931 $ | 2026-09-24 |
| 2026-08-25 | DOGE | 0,09000 $ | INCERTO | 55,00% | 0,09000 $ | 0,08000 $ | 0,11000 $ | 2026-09-24 |
| 2026-08-25 | SOL | 102,48 $ | INCERTO | 55,00% | 106,45 $ | 90,81 $ | 115,98 $ | 2026-09-24 |

<!-- FORECAST_30D_HISTORY_END -->

</details>
<!-- COMPACT_SECTION_END:scanner_forecast -->

<!-- COMPACT_SECTION_START:extreme_cases -->
<details>
<summary><strong>⚠️ Percorso dei casi estremi</strong></summary>

<!-- EXTREME_CASES_PATH_START -->
# Extreme cases path report

Generato: 2026-08-25 05:31 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [extreme_cases_path_report.md](extreme_cases_path_report.md)

Questo report si attiva quando i casi positivi o negativi sono almeno **80%**.

Ora misura anche il **rialzo massimo prima della discesa principale**, quindi distingue uno spike iniziale da una discesa quasi immediata.

## Trigger estremi

| Asset   | Direzione   | Trigger   | Percentuale   | Motivo                           |   Match disponibili |
|:--------|:------------|:----------|:--------------|:---------------------------------|--------------------:|
| BTC     | NESSUNO     | NO        | +62,50%       | Nessun lato sopra soglia estrema |                  40 |
| SOL     | NESSUNO     | NO        | +55,00%       | Nessun lato sopra soglia estrema |                  40 |
| DOGE    | NESSUNO     | NO        | +55,00%       | Nessun lato sopra soglia estrema |                  40 |

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
- Prezzo attuale: **80.567,77 $**
- Return normale fra 30 giorni: **86.764,34 $** (7,69%)
- Drawdown normale durante il mese: **74.650,41 $** (-7,34%)
- Drawdown brutto da rispettare: **69.772,90 $** (-13,40%)
- Max gain normale durante il mese: **93.930,62 $** (16,59%)
- Max gain buono / take profit ottimistico: **102.813,07 $** (27,61%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Solana
- Direzione più probabile a 30 giorni: **INCERTO**
- Casi positivi / salita storica: **55,00%**
- Casi negativi / discesa storica: **45,00%**
- Quanto è netto il segnale: **molto debole / quasi pari**
- Prezzo attuale: **102,48 $**
- Return normale fra 30 giorni: **106,45 $** (3,87%)
- Drawdown normale durante il mese: **90,81 $** (-11,39%)
- Drawdown brutto da rispettare: **86,16 $** (-15,93%)
- Max gain normale durante il mese: **115,98 $** (13,17%)
- Max gain buono / take profit ottimistico: **127,15 $** (24,07%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Dogecoin
- Direzione più probabile a 30 giorni: **INCERTO**
- Casi positivi / salita storica: **55,00%**
- Casi negativi / discesa storica: **45,00%**
- Quanto è netto il segnale: **molto debole / quasi pari**
- Prezzo attuale: **0,09 $**
- Return normale fra 30 giorni: **0,09 $** (1,55%)
- Drawdown normale durante il mese: **0,08 $** (-9,87%)
- Drawdown brutto da rispettare: **0,08 $** (-16,62%)
- Max gain normale durante il mese: **0,11 $** (21,55%)
- Max gain buono / take profit ottimistico: **0,13 $** (42,02%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Messaggio del giorno

Il quadro generale oggi è misto. Alcuni asset possono avere lettura diversa, quindi è meglio valutare asset per asset.

---

# Mappa semplice asset per asset

# Bitcoin — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟢 VERDE / Favorevole
**Prezzo attuale:** 80.567,77 $

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

- Se va molto male: **70.503,48 $** (-12,49%)
- Se va male: **74.292,10 $** (-7,79%)
- Scenario normale: **86.764,34 $** (7,69%)
- Se va bene: **93.821,62 $** (16,45%)
- Se va molto bene: **114.970,46 $** (42,70%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **74.650,41 $** (-7,34%)
- Discesa brutta: **69.772,90 $** (-13,40%)
- Discesa molto brutta: **65.246,73 $** (-19,02%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **93.930,62 $** (16,59%)
- Rialzo buono: **102.813,07 $** (27,61%)
- Rialzo molto forte: **122.966,98 $** (52,63%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Bitcoin tendeva a muoversi tra una zona bassa intorno a **74.650,41 $** e uno spike normale intorno a **93.930,62 $**.

La chiusura a 30 giorni era più spesso positiva: salita 62,50%, discesa 37,50%. Quindi la lettura principale è favorevole.

Nota leva BTC: se la liquidazione è vicina a 51.000 $, guarda soprattutto la discesa brutta e molto brutta. Il prezzo può recuperare dopo, ma la leva può saltare prima.

---

# Solana — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟡 GIALLO / Incerto
**Prezzo attuale:** 102,48 $

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

- Se va molto male: **87,61 $** (-14,51%)
- Se va male: **93,61 $** (-8,66%)
- Scenario normale: **106,45 $** (3,87%)
- Se va bene: **120,27 $** (17,36%)
- Se va molto bene: **162,09 $** (58,17%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **90,81 $** (-11,39%)
- Discesa brutta: **86,16 $** (-15,93%)
- Discesa molto brutta: **80,24 $** (-21,71%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **115,98 $** (13,17%)
- Rialzo buono: **127,15 $** (24,07%)
- Rialzo molto forte: **162,09 $** (58,17%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Solana tendeva a muoversi tra una zona bassa intorno a **90,81 $** e uno spike normale intorno a **115,98 $**.

La chiusura a 30 giorni è incerta: salita 55,00%, discesa 45,00%. Non c'è un vantaggio netto.

---

# Dogecoin — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟡 GIALLO / Incerto
**Prezzo attuale:** 0,09 $

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

- Se va molto male: **0,07 $** (-21,18%)
- Se va male: **0,08 $** (-9,65%)
- Scenario normale: **0,09 $** (1,55%)
- Se va bene: **0,11 $** (18,91%)
- Se va molto bene: **0,13 $** (42,31%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **0,08 $** (-9,87%)
- Discesa brutta: **0,08 $** (-16,62%)
- Discesa molto brutta: **0,06 $** (-31,21%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **0,11 $** (21,55%)
- Rialzo buono: **0,13 $** (42,02%)
- Rialzo molto forte: **0,15 $** (66,32%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Dogecoin tendeva a muoversi tra una zona bassa intorno a **0,08 $** e uno spike normale intorno a **0,11 $**.

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

- Previsioni già controllate: **24**
- Direzione corretta: **82,35%**
- Errore medio dello scenario centrale: **5,45%**
- Zona rischio toccata: **0,00%**
- Zona rialzo media toccata: **4,17%**
- Prezzo finale dentro lo scenario 10%-90%: **100,00%**

### Dogecoin

- Previsioni già controllate: **24**
- Direzione corretta: **90,48%**
- Errore medio dello scenario centrale: **15,16%**
- Zona rischio toccata: **0,00%**
- Zona rialzo media toccata: **16,67%**
- Prezzo finale dentro lo scenario 10%-90%: **91,67%**

### Solana

- Previsioni già controllate: **24**
- Direzione corretta: **100,00%**
- Errore medio dello scenario centrale: **7,35%**
- Zona rischio toccata: **8,33%**
- Zona rialzo media toccata: **20,83%**
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

Dati ancora insufficienti: previsioni controllate **24** su **30** necessarie.

Per ora si usa solo lo scanner storico grezzo. Quando ci saranno abbastanza previsioni controllate, qui apparirà la lettura autocalibrata.

## Solana

Dati ancora insufficienti: previsioni controllate **24** su **30** necessarie.

Per ora si usa solo lo scanner storico grezzo. Quando ci saranno abbastanza previsioni controllate, qui apparirà la lettura autocalibrata.

## Dogecoin

Dati ancora insufficienti: previsioni controllate **24** su **30** necessarie.

Per ora si usa solo lo scanner storico grezzo. Quando ci saranno abbastanza previsioni controllate, qui apparirà la lettura autocalibrata.

---

# Approfondimento tecnico — Bitcoin (BTC-USD)

## Semaforo: 🟢 VERDE / Favorevole

**Prezzo attuale:** 80.567,77 $

Bitcoin ha un segnale favorevole. La statistica dei casi simili indica più possibilità di salita che di discesa, ma resta comunque una probabilità, non una certezza.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **62,50%**
- Casi negativi dopo 30 giorni: **37,50%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **79,06%**
- Rendimento medio dopo 30 giorni: **12,74%**
- Rendimento centrale dopo 30 giorni: **7,69%**
- Discesa media durante i 30 giorni: **-9,14%**
- Massimo rialzo medio durante i 30 giorni: **25,04%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **90.830,50 $**
- Scenario centrale a 30 giorni: **86.764,34 $**
- Zona di rischio media: **73.206,61 $**
- Zona di rialzo media: **100.738,85 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -12,49% → **70.503,48 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -7,79% → **74.292,10 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: 7,69% → **86.764,34 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 16,45% → **93.821,62 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 42,70% → **114.970,46 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -19,02% → **65.246,73 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -13,40% → **69.772,90 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -7,34% → **74.650,41 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -3,76% → **77.534,57 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: -0,35% → **80.285,58 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 0,00% → **80.567,77 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 6,30% → **85.644,05 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 16,59% → **93.930,62 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 27,61% → **102.813,07 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 52,63% → **122.966,98 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| XRP-USD         | 2023-07-30   | 2023-11-06 |        86.96 |       -10.51 |         -18.88 |           0    |
| BNB-USD         | 2018-11-03   | 2019-02-10 |        85.94 |        67.25 |          -4.66 |          67.25 |
| ETC-USD         | 2020-08-19   | 2020-11-26 |        82.97 |        -4.88 |         -17.07 |           9.66 |
| ETC-USD         | 2023-07-30   | 2023-11-06 |        82.93 |         9.48 |          -1.99 |          12.3  |
| THETA-USD       | 2018-11-02   | 2019-02-09 |        82.23 |        93.12 |           0    |         137.2  |
| LTC-USD         | 2018-11-02   | 2019-02-09 |        82.18 |        23.73 |          -7.03 |          29.69 |
| EOS-USD         | 2023-07-30   | 2023-11-06 |        81.89 |         5.82 |          -7    |           6.19 |
| XLM-USD         | 2020-08-19   | 2020-11-26 |        81.61 |       -12.24 |         -24.52 |          23.19 |
| THETA-USD       | 2023-07-29   | 2023-11-05 |        81.53 |        39.97 |           0    |          40.4  |
| XTZ-USD         | 2023-07-30   | 2023-11-06 |        81.18 |         5.91 |          -7.43 |          11.68 |

---

# Approfondimento tecnico — Solana (SOL-USD)

## Semaforo: 🟡 GIALLO / Incerto

**Prezzo attuale:** 102,48 $

Solana è in una situazione incerta. Lo scanner non vede un vantaggio chiaro né per la salita né per la discesa. In questi casi è meglio non forzare la previsione.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **55,00%**
- Casi negativi dopo 30 giorni: **45,00%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **71,48%**
- Rendimento medio dopo 30 giorni: **27,53%**
- Rendimento centrale dopo 30 giorni: **3,87%**
- Discesa media durante i 30 giorni: **-13,05%**
- Massimo rialzo medio durante i 30 giorni: **39,53%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **130,69 $**
- Scenario centrale a 30 giorni: **106,45 $**
- Zona di rischio media: **89,11 $**
- Zona di rialzo media: **142,99 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -14,51% → **87,61 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -8,66% → **93,61 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: 3,87% → **106,45 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 17,36% → **120,27 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 58,17% → **162,09 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -21,71% → **80,24 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -15,93% → **86,16 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -11,39% → **90,81 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -7,79% → **94,49 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: -2,52% → **99,89 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 1,14% → **103,65 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 6,11% → **108,74 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 13,17% → **115,98 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 24,07% → **127,15 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 58,17% → **162,09 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| EOS-USD         | 2018-11-18   | 2019-02-25 |        80.46 |        20.31 |          -8.74 |          20.31 |
| VET-USD         | 2020-02-23   | 2020-06-01 |        79.66 |        41.53 |           0    |          46.55 |
| ZIL-USD         | 2020-08-16   | 2020-11-23 |        77.94 |       135.96 |           0    |         135.96 |
| FTM-USD         | 2020-10-13   | 2021-01-20 |        76.35 |       748.91 |          -8.15 |         748.91 |
| BNB-USD         | 2018-11-03   | 2019-02-10 |        75.79 |        67.25 |          -4.66 |          67.25 |
| VET-USD         | 2023-08-01   | 2023-11-08 |        75.57 |        18.75 |         -14.56 |          18.75 |
| ADA-USD         | 2020-08-19   | 2020-11-26 |        75.1  |        14.13 |          -1.36 |          23.88 |
| 1INCH-USD       | 2023-08-01   | 2023-11-08 |        74.91 |        11.79 |         -11.52 |          11.79 |
| NEO-USD         | 2023-07-30   | 2023-11-06 |        74.32 |       -10.02 |         -22.76 |           4.43 |
| ETC-USD         | 2020-08-19   | 2020-11-26 |        73.81 |        -4.88 |         -17.07 |           9.66 |

---

# Approfondimento tecnico — Dogecoin (DOGE-USD)

## Semaforo: 🟡 GIALLO / Incerto

**Prezzo attuale:** 0,09 $

Dogecoin è in una situazione incerta. Lo scanner non vede un vantaggio chiaro né per la salita né per la discesa. In questi casi è meglio non forzare la previsione.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **55,00%**
- Casi negativi dopo 30 giorni: **45,00%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **82,94%**
- Rendimento medio dopo 30 giorni: **6,67%**
- Rendimento centrale dopo 30 giorni: **1,55%**
- Discesa media durante i 30 giorni: **-11,82%**
- Massimo rialzo medio durante i 30 giorni: **31,87%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **0,10 $**
- Scenario centrale a 30 giorni: **0,09 $**
- Zona di rischio media: **0,08 $**
- Zona di rialzo media: **0,12 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -21,18% → **0,07 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -9,65% → **0,08 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: 1,55% → **0,09 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 18,91% → **0,11 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 42,31% → **0,13 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -31,21% → **0,06 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -16,62% → **0,08 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -9,87% → **0,08 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -3,00% → **0,09 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: 0,00% → **0,09 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 8,32% → **0,10 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 13,16% → **0,11 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 21,55% → **0,11 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 42,02% → **0,13 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 66,32% → **0,15 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| FIL-USD         | 2022-04-25   | 2022-08-02 |        86.69 |       -29.26 |         -31.16 |          16.04 |
| MANA-USD        | 2025-01-15   | 2025-04-24 |        86.5  |        -4.31 |         -10.11 |          18.69 |
| VET-USD         | 2025-01-17   | 2025-04-26 |        85.96 |         1.03 |          -8.45 |          18.77 |
| SAND-USD        | 2025-01-19   | 2025-04-28 |        84.79 |         2.06 |          -9.85 |          22.79 |
| YFI-USD         | 2022-04-25   | 2022-08-02 |        84.48 |       -14.5  |         -21.51 |          13.63 |
| KAVA-USD        | 2023-07-30   | 2023-11-06 |        84.47 |         8.9  |          -6.74 |          11.72 |
| EGLD-USD        | 2023-07-20   | 2023-10-27 |        84.19 |        57.59 |           0    |          66.83 |
| DOT-USD         | 2023-07-30   | 2023-11-06 |        84.15 |        21.64 |          -1.59 |          21.64 |
| QTUM-USD        | 2022-04-21   | 2022-07-29 |        83.98 |       -36.05 |         -36.05 |           0    |
| ALGO-USD        | 2025-01-19   | 2025-04-28 |        83.92 |        -5.72 |         -13.55 |           9.8  |

</details>
<!-- COMPACT_SECTION_END:scanner_full_detail -->

<!-- COMPACT_SECTION_START:market_regime -->
<details>
<summary><strong>🌦️ Market Regime Match</strong></summary>

<!-- MARKET_REGIME_MATCH_START -->
# Market Regime Match Report


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [market_regime_match_report.md](market_regime_match_report.md)

Generated: 2026-08-25 05:31 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | MIXED | 80.568 $ | True | 8.51% | -9.09% | MIXED | 8.51% | -9.09% |
| DOGE-USD | DISTRIBUTION | 0.09289 $ | True | -7.49% | -15.60% | MIXED | 8.51% | -9.09% |
| SOL-USD | RECOVERY | 102,48 $ | True | 24.49% | -15.17% | MIXED | 8.51% | -9.09% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 62.50% | 7.69% | 16.45% | 42.70% | -7.34% | -19.02% | 16.59% | 27.61% | 52.63% | 65.00% | 13.77% | 40.80% | 73.07% |
| BTC-USD | SAME_BTC_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| BTC-USD | SAME_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| DOGE-USD | ALL_MATCHES | 40 | 55.00% | 1.55% | 18.91% | 42.31% | -9.87% | -31.21% | 21.55% | 42.02% | 66.32% | 50.00% | -2.59% | 30.92% | 93.88% |
| DOGE-USD | SAME_BTC_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| DOGE-USD | SAME_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL-USD | ALL_MATCHES | 40 | 55.00% | 3.87% | 17.36% | 58.17% | -11.39% | -21.71% | 13.17% | 24.07% | 58.17% | 75.00% | 23.26% | 42.84% | 110.93% |
| SOL-USD | SAME_BTC_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL-USD | SAME_ASSET_REGIME | 10 | 30.00% | -5.58% | 6.58% | 39.85% | -12.55% | -17.37% | 4.64% | 15.37% | 46.61% | 100.00% | 28.85% | 54.06% | 78.41% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 8 | 37.50% | -3.77% | -8.94% | 39.55% | 62.50% | 26.27% | 108.72% |
| BTC-USD | HISTORICAL_BTC_BULL | 26 | 76.92% | 10.68% | -7.01% | 24.83% | 73.08% | 15.21% | 64.74% |
| BTC-USD | HISTORICAL_BTC_DISTRIBUTION | 3 | 66.67% | 16.22% | -13.32% | 22.40% | 0.00% | -13.86% | 22.40% |
| BTC-USD | HISTORICAL_BTC_RECOVERY | 3 | 0.00% | -15.07% | -15.75% | 35.71% | 66.67% | 23.44% | 55.17% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 5 | 40.00% | -4.70% | -16.21% | 37.84% | 20.00% | -16.66% | 37.84% |
| DOGE-USD | HISTORICAL_BTC_BULL | 30 | 63.33% | 4.19% | -7.21% | 43.25% | 63.33% | 9.93% | 81.38% |
| DOGE-USD | HISTORICAL_BTC_RECOVERY | 5 | 20.00% | -14.50% | -21.51% | 22.44% | 0.00% | -32.36% | 22.44% |
| SOL-USD | HISTORICAL_BTC_BEAR | 6 | 66.67% | 10.35% | -9.55% | 56.97% | 66.67% | 16.28% | 90.71% |
| SOL-USD | HISTORICAL_BTC_BULL | 17 | 58.82% | 6.74% | -11.52% | 23.19% | 70.59% | 14.56% | 68.47% |
| SOL-USD | HISTORICAL_BTC_DISTRIBUTION | 5 | 80.00% | 12.12% | -13.32% | 18.89% | 40.00% | -1.95% | 65.84% |
| SOL-USD | HISTORICAL_BTC_RECOVERY | 12 | 33.33% | -5.25% | -11.40% | 20.47% | 100.00% | 28.85% | 66.20% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 26 | 73.08% | 11.44% | -7.09% | 26.67% | 69.23% | 12.84% | 63.85% |
| BTC-USD | HISTORICAL_ASSET_BULL | 7 | 57.14% | 3.67% | -7.26% | 35.24% | 57.14% | 29.10% | 103.37% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 7 | 28.57% | -4.88% | -15.75% | 35.71% | 57.14% | 22.65% | 50.49% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 6 | 50.00% | -0.57% | -8.33% | 34.47% | 33.33% | -13.53% | 73.77% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 28 | 60.71% | 2.39% | -9.07% | 44.03% | 60.71% | 9.93% | 71.74% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 6 | 33.33% | -24.77% | -31.40% | 14.96% | 16.67% | -33.81% | 23.30% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 19 | 73.68% | 10.10% | -10.70% | 20.70% | 57.89% | 0.43% | 64.23% |
| SOL-USD | HISTORICAL_ASSET_BULL | 8 | 50.00% | 1.53% | -15.07% | 52.47% | 75.00% | 81.61% | 197.95% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 0.00% | -10.88% | -21.55% | 1.18% | 100.00% | 23.88% | 40.23% |
| SOL-USD | HISTORICAL_ASSET_MIXED | 2 | 50.00% | 0.76% | -8.82% | 36.50% | 100.00% | 13.06% | 36.59% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 10 | 30.00% | -5.58% | -12.55% | 15.37% | 100.00% | 28.85% | 59.77% |

## Top regime-adjusted matches

The table below shows the top matches separately for each target, so BTC does not hide SOL and DOGE.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD | XRP-USD | 2023-07-30 | 86.96% | BULL | BULL | DIFFERENT | BEARISH_30D | -10.51% | -18.88% | 0.00% | -19.43% | -19.43% | 0.00% |
| BTC-USD | BNB-USD | 2018-11-03 | 85.94% | BEAR | BEAR | DIFFERENT | EXPLOSIVE_60D | 67.25% | -4.66% | 67.25% | 92.16% | -4.66% | 114.84% |
| BTC-USD | ETC-USD | 2020-08-19 | 82.97% | BULL | RECOVERY | DIFFERENT | MIXED | -4.88% | -17.07% | 9.66% | 22.65% | -17.07% | 45.22% |
| BTC-USD | ETC-USD | 2023-07-30 | 82.93% | BULL | BEAR | DIFFERENT | MIXED | 9.48% | -1.99% | 12.30% | 8.74% | -1.99% | 22.62% |
| BTC-USD | THETA-USD | 2018-11-02 | 82.23% | BEAR | BEAR | DIFFERENT | EXPLOSIVE_60D | 93.12% | 0.00% | 137.20% | 61.21% | 0.00% | 137.20% |
| BTC-USD | LTC-USD | 2018-11-02 | 82.18% | BEAR | BEAR | DIFFERENT | EXPLOSIVE_60D | 23.73% | -7.03% | 29.69% | 97.31% | -7.03% | 106.68% |
| BTC-USD | EOS-USD | 2023-07-30 | 81.89% | BULL | BEAR | DIFFERENT | MIXED | 5.82% | -7.00% | 6.19% | 6.95% | -7.00% | 29.44% |
| BTC-USD | XLM-USD | 2020-08-19 | 81.61% | BULL | BULL | DIFFERENT | EXPLOSIVE_60D | -12.24% | -24.52% | 23.19% | 56.48% | -24.52% | 103.40% |
| BTC-USD | THETA-USD | 2023-07-29 | 81.53% | BULL | BEAR | DIFFERENT | EXPLOSIVE_60D | 39.97% | 0.00% | 40.40% | 52.99% | 0.00% | 78.81% |
| BTC-USD | XTZ-USD | 2023-07-30 | 81.18% | BULL | BEAR | DIFFERENT | MIXED | 5.91% | -7.43% | 11.68% | 12.98% | -7.43% | 33.82% |
| DOGE-USD | FIL-USD | 2022-04-25 | 86.69% | RECOVERY | RECOVERY | DIFFERENT | BEARISH_30D | -29.26% | -31.16% | 16.04% | -32.36% | -35.61% | 16.04% |
| DOGE-USD | MANA-USD | 2025-01-15 | 86.50% | BULL | BULL | DIFFERENT | MIXED | -4.31% | -10.11% | 18.69% | -19.03% | -26.84% | 18.69% |
| DOGE-USD | VET-USD | 2025-01-17 | 85.96% | BULL | BULL | DIFFERENT | MIXED | 1.03% | -8.45% | 18.77% | -22.61% | -29.05% | 18.77% |
| DOGE-USD | SAND-USD | 2025-01-19 | 84.79% | BULL | BULL | DIFFERENT | MIXED | 2.06% | -9.85% | 22.79% | -20.44% | -22.67% | 22.79% |
| DOGE-USD | YFI-USD | 2022-04-25 | 84.48% | RECOVERY | BEAR | DIFFERENT | BEARISH_30D | -14.50% | -21.51% | 13.63% | -25.07% | -25.52% | 13.63% |
| DOGE-USD | KAVA-USD | 2023-07-30 | 84.47% | BULL | RECOVERY | DIFFERENT | MIXED | 8.90% | -6.74% | 11.72% | 7.44% | -6.74% | 25.72% |
| DOGE-USD | EGLD-USD | 2023-07-20 | 84.19% | BULL | BEAR | DIFFERENT | EXPLOSIVE_60D | 57.59% | 0.00% | 66.83% | 148.44% | 0.00% | 154.29% |
| DOGE-USD | DOT-USD | 2023-07-30 | 84.15% | BULL | BEAR | DIFFERENT | HIGH_SPIKE_60D | 21.64% | -1.59% | 21.64% | 49.86% | -1.59% | 85.75% |
| DOGE-USD | QTUM-USD | 2022-04-21 | 83.98% | RECOVERY | RECOVERY | DIFFERENT | BEARISH_30D | -36.05% | -36.05% | 0.00% | -38.23% | -40.91% | 0.00% |
| DOGE-USD | ALGO-USD | 2025-01-19 | 83.92% | BULL | BULL | DIFFERENT | MIXED | -5.72% | -13.55% | 9.80% | -24.18% | -30.69% | 9.80% |
| SOL-USD | VET-USD | 2020-02-23 | 79.66% | RECOVERY | RECOVERY | SAME_ASSET_ONLY | EXPLOSIVE_60D | 41.53% | 0.00% | 46.55% | 159.81% | 0.00% | 201.34% |
| SOL-USD | ETC-USD | 2020-08-19 | 73.81% | BULL | RECOVERY | SAME_ASSET_ONLY | MIXED | -4.88% | -17.07% | 9.66% | 22.65% | -17.07% | 45.22% |
| SOL-USD | WAVES-USD | 2023-07-30 | 72.44% | BULL | RECOVERY | SAME_ASSET_ONLY | BULLISH_30D | 10.19% | -6.81% | 17.27% | 24.55% | -6.81% | 45.32% |
| SOL-USD | ALGO-USD | 2020-02-25 | 71.85% | RECOVERY | RECOVERY | SAME_ASSET_ONLY | BEARISH_30D | -15.75% | -15.75% | 2.83% | 24.41% | -15.75% | 60.35% |
| SOL-USD | QTUM-USD | 2020-02-26 | 71.75% | RECOVERY | RECOVERY | SAME_ASSET_ONLY | MIXED | -8.20% | -13.76% | 0.78% | 42.12% | -13.76% | 43.18% |
| SOL-USD | ZEC-USD | 2020-02-21 | 71.17% | RECOVERY | RECOVERY | SAME_ASSET_ONLY | MIXED | -4.23% | -9.12% | 6.45% | 32.15% | -9.12% | 32.15% |
| SOL-USD | ETH-USD | 2020-02-26 | 69.59% | RECOVERY | RECOVERY | SAME_ASSET_ONLY | EXPLOSIVE_60D | -6.28% | -8.78% | 1.23% | 58.04% | -8.78% | 58.04% |
| SOL-USD | BNB-USD | 2020-02-26 | 68.80% | RECOVERY | RECOVERY | SAME_ASSET_ONLY | BEARISH_30D | -11.46% | -13.55% | 0.70% | 25.56% | -13.55% | 25.56% |
| SOL-USD | LRC-USD | 2020-02-26 | 68.72% | RECOVERY | RECOVERY | SAME_ASSET_ONLY | EXPLOSIVE_60D | 39.66% | -11.55% | 47.16% | 69.37% | -11.55% | 83.74% |
| SOL-USD | NEO-USD | 2020-02-26 | 67.69% | RECOVERY | RECOVERY | SAME_ASSET_ONLY | BEARISH_30D | -18.30% | -20.05% | 0.00% | 1.84% | -20.05% | 9.18% |

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

Generato: 2026-08-25 05:31 UTC


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
| BTC | 80.568 $ | +12 | CONFERMATO RIALZISTA | STAGE 3 / DISTRIBUZIONE O PAUSA | MASSIMI E MINIMI CRESCENTI | SIGN OF STRENGTH POSSIBILE | MEDIO | SPOT OK / LONG SOLO PRUDENTE SU CONFERMA |
| SOL | 102,48 $ | +12 | CONFERMATO RIALZISTA | STAGE 3 / DISTRIBUZIONE O PAUSA | MASSIMI E MINIMI CRESCENTI | SIGN OF STRENGTH POSSIBILE | BASSO | TRANCHE PICCOLE / NO LEVA FINCHÉ NON ROMPE CONFERME |
| DOGE | 0.09289 $ | +6 | COSTRUTTIVO / CONFERMA PARZIALE | STAGE 3 / DISTRIBUZIONE O PAUSA | MASSIMI E MINIMI CRESCENTI | RANGE / FASE NON CHIARA | MEDIO | SOLO TRADING VELOCE / NO LEVA AGGRESSIVA |

## Punteggi per area

| Asset | Trend | Struttura | Momentum | Volume | Prezzo | Candela | Wyckoff | Totale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +1 | +2 | +2 | +3 | +3 | 0 | +2 | +12 |
| SOL | +1 | +2 | +2 | +3 | +3 | 0 | +2 | +12 |
| DOGE | 0 | +2 | +2 | +2 | 0 | 0 | 0 | +6 |

## Livelli tecnici

| Asset | Supporto | Resistenza | Breakout 60g | Breakdown 60g | ATR14 | Rendimento 30g | Rendimento 90g |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 79.206 $ | 82.430 $ | 79.464 $ | 57.748 $ | 2,94% | 25,45% | 6,40% |
| SOL | 85,25 $ | 102,14 $ | 94,74 $ | 64,42 $ | 3,87% | 37,68% | 22,59% |
| DOGE | 0.09274 $ | 0.09435 $ | 0.09423 $ | 0.06797 $ | 4,80% | 29,61% | -7,94% |

## Lettura dettagliata

### BTC

- Prezzo: **80.568 $**
- Score classico: **+12 / 12**
- Verdetto: **CONFERMATO RIALZISTA**
- Azione coerente: **SPOT OK / LONG SOLO PRUDENTE SU CONFERMA**
- Volatilità tecnica locale: **MEDIO** — ATR14 2,94%; distanza supporto 1,86%; distanza resistenza 2,17%

Dettaglio:

- Trend: **+1** — prezzo sopra MA200 daily; breve termine sopra MA20/MA50; MA50 daily in salita; MA200 daily in discesa; STAGE 3 / DISTRIBUZIONE O PAUSA
- Stage weekly: **STAGE 3 / DISTRIBUZIONE O PAUSA** — Prezzo sopra MA30 weekly ma pendenza debole o piatta.
- Struttura: **+2** — MASSIMI E MINIMI CRESCENTI
- Momentum: **+2** — RSI alto 83.8; RSI in miglioramento; MACD sopra signal; istogramma MACD in miglioramento
- Volume: **+3** — OBV sopra media; CMF positivo 0.26; rialzo con volume sopra media
- Conferma prezzo: **+3** — Breakout sopra resistenza 60g con volume.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **+2** — SIGN OF STRENGTH POSSIBILE. Prezzo nella parte alta del range con flusso volume positivo.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 83.80 |
| MACD histogram | 1786.75767 |
| CMF20 | 0.264 |
| Volume ratio 20 | 2.14 |
| MA20 | 67.596 $ |
| MA50 | 65.497 $ |
| MA100 | 66.125 $ |
| MA200 | 69.094 $ |
| Pendenza MA50 20g | +3,53% |
| Pendenza MA200 60g | -9,27% |
| Bollinger width | 30,15% |
| Bollinger position | 1.04 |

### SOL

- Prezzo: **102,48 $**
- Score classico: **+12 / 12**
- Verdetto: **CONFERMATO RIALZISTA**
- Azione coerente: **TRANCHE PICCOLE / NO LEVA FINCHÉ NON ROMPE CONFERME**
- Volatilità tecnica locale: **BASSO** — ATR14 3,87%; distanza supporto 20,20%; distanza resistenza -0,32%

Dettaglio:

- Trend: **+1** — prezzo sopra MA200 daily; breve termine sopra MA20/MA50; MA50 daily in salita; MA200 daily in discesa; STAGE 3 / DISTRIBUZIONE O PAUSA
- Stage weekly: **STAGE 3 / DISTRIBUZIONE O PAUSA** — Prezzo sopra MA30 weekly ma pendenza debole o piatta.
- Struttura: **+2** — MASSIMI E MINIMI CRESCENTI
- Momentum: **+2** — RSI alto 88.1; RSI in miglioramento; MACD sopra signal; istogramma MACD in miglioramento
- Volume: **+3** — OBV sopra media; CMF positivo 0.36; rialzo con volume sopra media
- Conferma prezzo: **+3** — Breakout sopra resistenza 60g con volume.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **+2** — SIGN OF STRENGTH POSSIBILE. Prezzo nella parte alta del range con flusso volume positivo.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 88.10 |
| MACD histogram | 2.69568 |
| CMF20 | 0.361 |
| Volume ratio 20 | 2.69 |
| MA20 | 80,64 $ |
| MA50 | 77,81 $ |
| MA100 | 76,56 $ |
| MA200 | 81,27 $ |
| Pendenza MA50 20g | +3,73% |
| Pendenza MA200 60g | -15,44% |
| Bollinger width | 35,03% |
| Bollinger position | 1.11 |

### DOGE

- Prezzo: **0.09289 $**
- Score classico: **+6 / 12**
- Verdetto: **COSTRUTTIVO / CONFERMA PARZIALE**
- Azione coerente: **SOLO TRADING VELOCE / NO LEVA AGGRESSIVA**
- Volatilità tecnica locale: **MEDIO** — ATR14 4,80%; distanza supporto 0,17%; distanza resistenza 1,56%

Dettaglio:

- Trend: **0** — prezzo sopra MA200 daily; breve termine sopra MA20/MA50; MA200 daily in discesa; STAGE 3 / DISTRIBUZIONE O PAUSA
- Stage weekly: **STAGE 3 / DISTRIBUZIONE O PAUSA** — Prezzo sopra MA30 weekly ma pendenza debole o piatta.
- Struttura: **+2** — MASSIMI E MINIMI CRESCENTI
- Momentum: **+2** — RSI alto 83.0; RSI in miglioramento; MACD sopra signal; istogramma MACD in miglioramento
- Volume: **+2** — OBV sopra media; CMF positivo 0.22; volume ratio 1.79
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **0** — RANGE / FASE NON CHIARA. Nessuna fase Wyckoff pulita.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 83.02 |
| MACD histogram | 0.00284 |
| CMF20 | 0.221 |
| Volume ratio 20 | 1.79 |
| MA20 | 0.07522 $ |
| MA50 | 0.07327 $ |
| MA100 | 0.08078 $ |
| MA200 | 0.08926 $ |
| Pendenza MA50 20g | -1,63% |
| Pendenza MA200 60g | -15,86% |
| Bollinger width | 39,73% |
| Bollinger position | 0.98 |

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

Generato: 2026-08-25 05:32 UTC


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
| BTC | 80.568 $ | Doppio massimo | CANDIDATO | ribassista | n/a | 49.952 $ | n/a | 39,52% | Fib 78,6% TESTATO (0) @ 78.447 $ | BREAKOUT 60G | 74.959 $ |
| SOL | 102,48 $ | Doppio massimo | CANDIDATO | ribassista | n/a | 51,22 $ | n/a | 59,09% | Fib 78,6% RECUPERATO (0) @ 93,12 $ | BREAKOUT 60G | 83,52 $ |
| DOGE | 0.09289 $ | Doppio massimo | CANDIDATO | ribassista | n/a | 0.06214 $ | n/a | 36,66% | Fib 50,0% REJECTION (0) @ 0.09360 $ | NEL RANGE | 0.09274 $ |

## BTC

![Classic visual BTC](classic_visual_BTC.png)

- Pattern principale: **Doppio massimo**
- Stato pattern: **CANDIDATO** (0)
- Famiglia: **ribassista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-06-22 -> 2026-08-09**
- Età formazione: **16 giorni**
- Breakout pattern: **n/a**
- Età breakout: **n/a**
- Neckline: **57.748 $**
- Target teorico: **49.952 $**
- Progresso verso target: **n/a**
- Distanza dalla neckline: **39,52%**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 78,6% TESTATO (0) @ 78.447 $** — Swing DOWN 2026-05-06 82.792 -> 2026-08-14 62.488; livello più vicino 78.6% a 78.447; stato TESTATO; confluenza: nessuna confluenza indipendente.
- Invalidazione: **58.903 $**
- Relazione prezzo/neckline: **sopra neckline**
- Dettaglio: Due massimi simili vicino a 65.544 tra 2026-06-22 e 2026-08-09. Neckline ribassista stimata: 57.748. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 16 giorni. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **BREAKOUT 60G**
- Supporto: **74.959 $**
- Resistenza: **82.792 $**
- Breakout 60g: **79.464 $**
- Breakdown 60g: **57.748 $**
- RSI14: **83.70**
- ATR14: **2,94%**
- Volume ratio 20g: **2.15**
- Rendimento 30g: **+25,28%**
- Rendimento 90g: **+6,25%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Triangolo ascendente possibile | CANDIDATO | 0 | rialzista | n/a | n/a | n/a | n/a | n/a | n/a | n/a | Resistenza quasi piatta e minimi crescenti. Stato: CANDIDATO; il pattern non ha una neckline univoca da usare per il lifecycle. |
| Doppio massimo | CANDIDATO | 0 | ribassista | 62.227 $ | n/a | n/a | 58.946 $ | n/a | 29,47% | 63.471 $ | Due massimi simili a 65.508 $ e 65.402 $. Neckline circa 62.227 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 16 giorni. |
| Doppio minimo | TARGET RAGGIUNTO | 0 | rialzista | 65.402 $ | 2026-08-19 | 6g | 68.577 $ | 477,65% | n/a | 64.094 $ | Due minimi simili a 62.227 $ e 62.488 $. Neckline circa 65.402 $. Breakout neckline: 2026-08-19 (6 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 68.577 $; progresso: 477,65%; prezzo sopra neckline. |

## SOL

![Classic visual SOL](classic_visual_SOL.png)

- Pattern principale: **Doppio massimo**
- Stato pattern: **CANDIDATO** (0)
- Famiglia: **ribassista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-06-22 -> 2026-08-09**
- Età formazione: **16 giorni**
- Breakout pattern: **n/a**
- Età breakout: **n/a**
- Neckline: **64,42 $**
- Target teorico: **51,22 $**
- Progresso verso target: **n/a**
- Distanza dalla neckline: **59,09%**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 78,6% RECUPERATO (0) @ 93,12 $** — Swing DOWN 2026-05-11 98,27 -> 2026-08-16 74,20; livello più vicino 78.6% a 93,12; stato RECUPERATO; confluenza: nessuna confluenza indipendente.
- Invalidazione: **65,71 $**
- Relazione prezzo/neckline: **sopra neckline**
- Dettaglio: Due massimi simili vicino a 77,62 tra 2026-06-22 e 2026-08-09. Neckline ribassista stimata: 64,42. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 16 giorni. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **BREAKOUT 60G**
- Supporto: **83,52 $**
- Resistenza: **127,97 $**
- Breakout 60g: **94,74 $**
- Breakdown 60g: **64,42 $**
- RSI14: **88.11**
- ATR14: **3,90%**
- Volume ratio 20g: **2.70**
- Rendimento 30g: **+37,69%**
- Rendimento 90g: **+22,60%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Triangolo discendente possibile | CANDIDATO | 0 | ribassista | n/a | n/a | n/a | n/a | n/a | n/a | n/a | Massimi decrescenti e supporto quasi piatto. Stato: CANDIDATO; il pattern non ha una neckline univoca da usare per il lifecycle. |
| Doppio massimo | CANDIDATO | 0 | ribassista | 70,69 $ | n/a | n/a | 62,66 $ | n/a | 44,96% | 72,11 $ | Due massimi simili a 78,73 $ e 77,62 $. Neckline circa 70,69 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 16 giorni. |
| Testa e spalle inverso | TARGET RAGGIUNTO | 0 | rialzista | 78,17 $ | 2026-08-19 | 6g | 85,65 $ | 325,10% | n/a | 76,61 $ | Spalla sinistra 73,40 $, testa 70,69 $, spalla destra 74,20 $. Neckline circa 78,17 $. Breakout neckline: 2026-08-19 (6 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 85,65 $; progresso: 325,10%; prezzo sopra neckline. |
| Doppio minimo | TARGET RAGGIUNTO | 0 | rialzista | 78,73 $ | 2026-08-19 | 6g | 84,05 $ | 446,15% | n/a | 77,15 $ | Due minimi simili a 73,40 $ e 74,20 $. Neckline circa 78,73 $. Breakout neckline: 2026-08-19 (6 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 84,05 $; progresso: 446,15%; prezzo sopra neckline. |

## DOGE

![Classic visual DOGE](classic_visual_DOGE.png)

- Pattern principale: **Doppio massimo**
- Stato pattern: **CANDIDATO** (0)
- Famiglia: **ribassista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-07-26 -> 2026-08-11**
- Età formazione: **14 giorni**
- Breakout pattern: **n/a**
- Età breakout: **n/a**
- Neckline: **0.06797 $**
- Target teorico: **0.06214 $**
- Progresso verso target: **n/a**
- Distanza dalla neckline: **36,66%**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 50,0% REJECTION (0) @ 0.09360 $** — Swing DOWN 2026-05-14 0.11825 -> 2026-08-12 0.06895; livello più vicino 50.0% a 0.09360; stato REJECTION; confluenza: nessuna confluenza indipendente.
- Invalidazione: **0.06933 $**
- Relazione prezzo/neckline: **sopra neckline**
- Dettaglio: Due massimi simili vicino a 0.07380 tra 2026-07-26 e 2026-08-11. Neckline ribassista stimata: 0.06797. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 14 giorni. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **NEL RANGE**
- Supporto: **0.09274 $**
- Resistenza: **0.09584 $**
- Breakout 60g: **0.09423 $**
- Breakdown 60g: **0.06797 $**
- RSI14: **82.99**
- ATR14: **4,80%**
- Volume ratio 20g: **1.79**
- Rendimento 30g: **+29,60%**
- Rendimento 90g: **-7,95%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Triangolo ascendente possibile | CANDIDATO | 0 | rialzista | n/a | n/a | n/a | n/a | n/a | n/a | n/a | Resistenza quasi piatta e minimi crescenti. Stato: CANDIDATO; il pattern non ha una neckline univoca da usare per il lifecycle. |
| Doppio massimo | CANDIDATO | 0 | ribassista | 0.06797 $ | n/a | n/a | 0.06214 $ | n/a | 36,66% | 0.06933 $ | Due massimi simili a 0.07380 $ e 0.07286 $. Neckline circa 0.06797 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 14 giorni. |
| Doppio minimo | TARGET RAGGIUNTO | 0 | rialzista | 0.07923 $ | 2026-08-20 | 5g | 0.08952 $ | 132,80% | n/a | 0.07765 $ | Due minimi simili a 0.06961 $ e 0.06895 $. Neckline circa 0.07923 $. Breakout neckline: 2026-08-20 (5 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 0.08952 $; progresso: 132,80%; prezzo sopra neckline. |

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

Generato: 2026-08-25 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [fractal_path_tracker.md](fractal_path_tracker.md)

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-08-25**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-02-09**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **102,48 $**
- Verdetto principale: **ANALOGIA DEBOLE / SCENARIO SECONDARIO**
- Somiglianza strutturale: **+63,53%**
- Aderenza live principale: **+71,07%**
- Errore medio live principale: **14,47%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE SOLO DI CONTESTO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **80**
- Osservazioni inclusive dal bottom: **81**
- Osservazioni da inizio programma/scanner: **54**
- Errore assoluto medio dal bottom: **11,65%**
- Errore assoluto medio da inizio programma: **14,47%**
- Gap firmato medio ultimi 7 giorni: **+3,58%**
- Errore assoluto medio ultimi 7 giorni: **7,08%**
- Gap ultimo giorno: **+19,23%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **+19,23%**
- Gap firmato medio 7g: **+3,58%**
- Errore assoluto medio 7g: **7,08%**
- Variazione recente gap: **+14,49%**
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
| 71 | 2026-08-16 | 2023-01-31 | 74,54 $ | 91,15 $ | -18,22% | da inizio programma |
| 72 | 2026-08-17 | 2023-02-01 | 75,94 $ | 93,45 $ | -18,74% | da inizio programma |
| 73 | 2026-08-18 | 2023-02-02 | 77,03 $ | 92,46 $ | -16,69% | da inizio programma |
| 74 | 2026-08-19 | 2023-02-03 | 85,37 $ | 92,37 $ | -7,58% | da inizio programma |
| 75 | 2026-08-20 | 2023-02-04 | 87,64 $ | 91,91 $ | -4,65% | da inizio programma |
| 76 | 2026-08-21 | 2023-02-05 | 93,65 $ | 90,43 $ | +3,57% | da inizio programma |
| 77 | 2026-08-22 | 2023-02-06 | 93,91 $ | 89,66 $ | +4,75% | da inizio programma |
| 78 | 2026-08-23 | 2023-02-07 | 95,44 $ | 91,64 $ | +4,15% | da inizio programma |
| 79 | 2026-08-24 | 2023-02-08 | 95,44 $ | 90,36 $ | +5,62% | da inizio programma |
| 80 | 2026-08-25 | 2023-02-09 | 102,48 $ | 85,95 $ | +19,23% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-09-01 | 93,06 $ | 110,96 $ | 101,69 $ / 114,17 $ | no | n/a | n/a | n/a |
| 14g | 2026-09-08 | 94,33 $ | 112,48 $ | 101,69 $ / 116,62 $ | no | n/a | n/a | n/a |
| 21g | 2026-09-15 | 92,48 $ | 110,26 $ | 101,69 $ / 116,62 $ | no | n/a | n/a | n/a |
| 28g | 2026-09-22 | 80,21 $ | 95,64 $ | 95,64 $ / 116,62 $ | no | n/a | n/a | n/a |
| 35g | 2026-09-29 | 98,69 $ | 117,67 $ | 94,82 $ / 117,67 $ | no | n/a | n/a | n/a |
| 42g | 2026-10-06 | 111,61 $ | 133,08 $ | 94,82 $ / 133,08 $ | no | n/a | n/a | n/a |
| 49g | 2026-10-13 | 110,43 $ | 131,67 $ | 94,82 $ / 133,15 $ | no | n/a | n/a | n/a |
| 56g | 2026-10-20 | 110,47 $ | 131,72 $ | 94,82 $ / 133,76 $ | no | n/a | n/a | n/a |
| 63g | 2026-10-27 | 119,75 $ | 142,78 $ | 94,82 $ / 142,78 $ | no | n/a | n/a | n/a |
| 70g | 2026-11-03 | 111,27 $ | 132,67 $ | 94,82 $ / 143,19 $ | no | n/a | n/a | n/a |
| 77g | 2026-11-10 | 116,10 $ | 138,43 $ | 94,82 $ / 143,19 $ | no | n/a | n/a | n/a |
| 84g | 2026-11-17 | 113,64 $ | 135,49 $ | 94,82 $ / 143,19 $ | no | n/a | n/a | n/a |
| 91g | 2026-11-24 | 106,36 $ | 126,82 $ | 94,82 $ / 143,19 $ | no | n/a | n/a | n/a |
| 98g | 2026-12-01 | 105,70 $ | 126,03 $ | 94,82 $ / 143,19 $ | no | n/a | n/a | n/a |
| 105g | 2026-12-08 | 104,30 $ | 124,35 $ | 94,82 $ / 143,19 $ | no | n/a | n/a | n/a |
| 112g | 2026-12-15 | 105,65 $ | 125,97 $ | 94,82 $ / 143,19 $ | no | n/a | n/a | n/a |
| 119g | 2026-12-22 | 104,42 $ | 124,50 $ | 94,82 $ / 143,19 $ | no | n/a | n/a | n/a |
| 126g | 2026-12-29 | 100,75 $ | 120,13 $ | 94,82 $ / 143,19 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 40 | 40,00% | 9,91% | 13,13% |
| 14g | 35 | 31,43% | 17,22% | 12,13% |
| 21g | 28 | 21,43% | 23,29% | 13,36% |
| 28g | 21 | 52,38% | 22,99% | 13,31% |
| 35g | 14 | 64,29% | 20,11% | 11,59% |
| 42g | 7 | 100,00% | 11,38% | 7,46% |
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

Ultima lettura salvata: **2026-08-25** — SOL 102,48 $, gap +19,23%, somiglianza +63,53%.

Nel report principale lascio solo il link, così non diventa troppo lungo.

<!-- SOL_BTC_FRACTAL_HISTORY_END -->

</details>
<!-- COMPACT_SECTION_END:fractal_path -->

<!-- COMPACT_SECTION_START:exchange_microstructure -->
<details>
<summary><strong>🏦 Dati exchange, liquidità e leva</strong></summary>

<!-- EXCHANGE_MICROSTRUCTURE_START -->
# Dati exchange, liquidità e leva

Generato: 2026-08-25 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [exchange_microstructure_report.md](exchange_microstructure_report.md)

Questo modulo legge Kraken Futures, Bitget Futures e KuCoin Futures come nucleo derivati. OKX e Coinbase vengono raccolti come fonti ausiliarie non pesate.
Non modifica la formula matematica di RSI, Fibonacci o Wyckoff: controlla se quei segnali sono sostenuti da acquisti, vendite, OI, funding e liquidità.

**Limite importante:** questo nucleo non assume disponibile un feed pubblico completo delle liquidazioni. La componente liquidazioni resta neutrale; le zone future restano stime di pressione, non dati certi delle singole posizioni.

Diagnostica completa: [exchange_source_diagnostics.md](exchange_source_diagnostics.md)

## Sintesi

| Asset | Prezzo | Exchange | Segnale candidato | Peso Global | Bias exchange | Confidenza | Copertura | Funding 8h eq. | OI 24h | Taker flow (campione/4h) | Book 0,5% | Liq long campione | Liq short campione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 80.493 $ | 3 | +1 | 0 | POSITIVA / CANDIDATA, ANCORA NON PESATA | MEDIA | 100% | +0,0034% | +2,28% | 3,56 | -1,39% | 0 $ | 0 $ |
| SOL | 101,92 $ | 3 | +1 | 0 | POSITIVA / CANDIDATA, ANCORA NON PESATA | ALTA | 100% | +0,0085% | +7,13% | 1,32 | +5,91% | 0 $ | 0 $ |
| DOGE | 0.09243 $ | 3 | 0 | 0 | LEGGERMENTE POSITIVA / NON PESATA | BASSA | 100% | +0,0100% | -4,18% | 1,20 | -0,09% | 0 $ | 0 $ |

Il segnale candidato è limitato a **±1**, ma il peso nel Global resta **0** finché il tracker a 7 giorni non raggiunge 30 controlli, almeno 55% di accuratezza e return corretto direzione positivo. Un singolo muro o funding non basta.

La colonna taker usa un campione recente nel primo run. Dopo almeno 3 fotografie distribuite su almeno 45 minuti viene sostituita automaticamente dalla media intraday 4h.

## Dati separati per exchange

| Asset | Exchange | Stato | Funding 8h eq. | Open interest | Taker flow | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | Kraken | OK | +0,0080% | 145,45 mln $ | 2,06 | -11,18% |
| BTC | Bitget | OK | +0,0100% | 2,76 mld $ | 4,02 | +34,86% |
| BTC | Kucoin | OK | +0,0100% | 1,69 mld $ | 15,46 | +6,81% |
| SOL | Kraken | OK | -0,0141% | 36,12 mln $ | 1,05 | -5,07% |
| SOL | Bitget | OK | +0,0100% | 419,48 mln $ | 1,44 | +37,16% |
| SOL | Kucoin | OK | +0,0100% | 248,70 mln $ | 1,47 | +7,79% |
| DOGE | Kraken | OK | +0,0168% | 4,76 mln $ | 1,50 | -5,79% |
| DOGE | Bitget | OK | +0,0100% | 119,26 mln $ | 0,26 | -0,42% |
| DOGE | Kucoin | OK | +0,0100% | 131,98 mln $ | 1,68 | -21,49% |

Kraken, Bitget e KuCoin contribuiscono a funding normalizzato, open interest, trade aggressivi e order book. Non viene inventato un long/short ratio pubblico né un feed completo delle liquidazioni.

## Conferme per indicatori tecnici

### BTC

- Score grezzo exchange: **+3,00**; candidato: **+1**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 1, accuratezza +100,00%.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 2, bear 1, divergenze 0.
- Flusso taker/order book: **+1,75**.
- OI/funding/basis: **+1,00**.
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

- Score grezzo exchange: **+3,25**; candidato: **+1**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 2, accuratezza +0,00%.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 2, bear 1, divergenze 0.
- Flusso taker/order book: **+1,75**.
- OI/funding/basis: **+1,00**.
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
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 4, accuratezza +50,00%.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 1, bear 2, divergenze 0.
- Flusso taker/order book: **+1,75**.
- OI/funding/basis: **+0,00**.
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
| BTC | +62,50% | +7,69% | 1 | +0,00% | RACCOLTA DATI | 0,00 | +62,50% | +7,69% |
| SOL | +55,00% | +3,87% | 1 | +100,00% | RACCOLTA DATI | 0,00 | +55,00% | +3,87% |
| DOGE | +55,00% | +1,55% | 2 | +100,00% | RACCOLTA DATI | 0,00 | +55,00% | +1,55% |

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

Generato: 2026-08-25 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [exchange_signal_tracker_report.md](exchange_signal_tracker_report.md)

Questo tracker verifica se il segnale candidato exchange ±1 anticipa correttamente la direzione del prezzo a 1/3/7/14/30 giorni.
Il peso Global resta 0 finché l'orizzonte 7g non ha almeno 30 controlli, accuratezza almeno 55% e return corretto direzione positivo. L'overlay a 30g ha un gate separato.

Controlli maturati completati in questa esecuzione: **15**.

## Ultime fotografie giornaliere

| Data | Asset | Prezzo | Versione | Calibrazione | Candidato | Peso Global | Score raw | Confidenza | Taker 4h | OI 24h | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08-25 | BTC | 80.493,33 | V2.1.3 | OK | 1 | 0 | 3,00 | MEDIA | 3,56 | +2,28% | -1,39% |
| 2026-08-25 | DOGE | 0.09243 | V2.1.3 | OK | 0 | 0 | 2,00 | BASSA | 1,20 | -4,18% | -0,09% |
| 2026-08-25 | SOL | 101,92 | V2.1.3 | OK | 1 | 0 | 3,25 | ALTA | 1,32 | +7,13% | +5,91% |
| 2026-08-24 | BTC | 76.901,40 | V2.1.3 | OK | 0 | 0 | 2,25 | MEDIA | 3,80 | +2,92% | +1,83% |
| 2026-08-24 | DOGE | 0.09180 | V2.1.3 | OK | 1 | 0 | 3,25 | MEDIA | 1,09 | +2,91% | +15,94% |
| 2026-08-24 | SOL | 93,87 | V2.1.3 | OK | 0 | 0 | 0,75 | BASSA | 0,55 | -4,62% | +13,79% |
| 2026-08-23 | BTC | 76.568,40 | V2.1.3 | OK | 1 | 0 | 2,50 | MEDIA | 2,97 | +1,29% | +6,02% |
| 2026-08-23 | DOGE | 0.08987 | V2.1.3 | OK | 0 | 0 | 3,00 | MEDIA | 0,96 | -8,05% | +28,88% |
| 2026-08-23 | SOL | 92,73 | V2.1.3 | OK | 0 | 0 | 2,25 | BASSA | 1,39 | +0,09% | +8,75% |

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
| DOGE | 1g | 7 | +57,14% | +1,05% | -0,16% | +2,16% | FEEDBACK RAPIDO |
| DOGE | 3g | 6 | +50,00% | +3,24% | -2,45% | +7,87% | FEEDBACK RAPIDO |
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
| BTC | 80.568 $ | +0.0100% | -12.55% | 1.79 | Rischio sotto | 2/5 |
| SOL | 102,48 $ | +0.0100% | -29.53% | 2.91 | Rischio sotto | 2/5 |
| DOGE | 0.09289 $ | +0.0100% | -8.46% | 3.10 | Rischio sotto | 2/5 |

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

Generato: 2026-08-25 05:32 UTC


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
| BTC     | 1D   | Hidden bullish     | CONFERMATA    | 80.735 $ / 83,84  | 2026-08-03 62.227 $ / RSI 47,40 → 2026-08-14 62.488 $ / RSI 42,71   | n/a                 | n/a              |      0 |
| BTC     | 1W   | Conferma rialzista | CONTESTO      | 80.735 $ / 59,20  | n/a                                                                 | +24,80%             | 19,46            |      0 |
| SOL     | 1D   | Conferma rialzista | CONTESTO      | 102,30 $ / 88,03  | n/a                                                                 | +34,70%             | 33,95            |      0 |
| SOL     | 1W   | Hidden bearish     | CONFERMATA    | 102,30 $ / 58,16  | 2026-05-17 98,27 $ / RSI 38,29 → 2026-07-05 83,81 $ / RSI 42,25     | n/a                 | n/a              |      0 |
| DOGE    | 1D   | Conferma rialzista | CONTESTO      | 0.09292 $ / 83,09 | n/a                                                                 | +33,34%             | 39,71            |      0 |
| DOGE    | 1W   | Hidden bearish     | IN_FORMAZIONE | 0.09292 $ / 49,44 | 2026-05-17 0.11825 $ / RSI 44,25 → 2026-08-23 0.09998 $ / RSI 49,72 | n/a                 | n/a              |      0 |

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

Generato: 2026-08-25 05:32 UTC


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
| BTC | 80.568 $ | 11 | RIALZISTA TECNICO | Trend rialzista | Momentum in miglioramento | Compressione / triangolo | 0 | 0 / TESTATO | Doppio minimo / TARGET RAGGIUNTO | Doppio massimo / CANDIDATO | 62.488 | 82.792 |
| SOL | 102,48 $ | 10 | RIALZISTA TECNICO | Trend rialzista | Momentum in miglioramento | Compressione / triangolo | 0 | 0 / RECUPERATO | Doppio minimo / TARGET RAGGIUNTO | Doppio massimo / CANDIDATO | 74,20 | 127,97 |
| DOGE | 0.09289 $ | 7 | RIALZISTA TECNICO | Trend misto | Momentum in miglioramento | Struttura rialzista con massimi e minimi crescenti | 0 | 0 / REJECTION | Triplo minimo / TARGET RAGGIUNTO | Doppio massimo / CANDIDATO | 0.06895 | 0.11825 |

## Riepilogo ciclo di vita pattern

| Asset   | Doppio minimo    | Triplo minimo    | Adam/Eve Bottom                        | Doppio massimo   | Triplo massimo   | Adam/Eve Top                 |   Punteggio pattern |
|:--------|:-----------------|:-----------------|:---------------------------------------|:-----------------|:-----------------|:-----------------------------|--------------------:|
| BTC | TARGET RAGGIUNTO | TARGET RAGGIUNTO | Adam and Eve Bottom — TARGET RAGGIUNTO | CANDIDATO | CANDIDATO | Adam and Eve Top — CANDIDATO | 0 |
| SOL | TARGET RAGGIUNTO | TARGET RAGGIUNTO | Adam and Eve Bottom — TARGET RAGGIUNTO | CANDIDATO | CANDIDATO | Adam and Eve Top — CANDIDATO | 0 |
| DOGE | TARGET RAGGIUNTO | TARGET RAGGIUNTO | Adam and Eve Bottom — TARGET RAGGIUNTO | CANDIDATO | CANDIDATO | Adam and Eve Top — CANDIDATO | 0 |

## Indicatori tecnici

| Asset   |   RSI 14 |   Istogramma MACD | MA20    | MA50    | MA200   | Pendenza MA50 20g   | Pendenza MA200 60g   | Rendimento 30g   | Rendimento 90g   |
|:--------|---------:|------------------:|:--------|:--------|:--------|:--------------------|:---------------------|:-----------------|:-----------------|
| BTC | 83.7 | 1779.47 | 67.590 | 65.495 | 69.094 | 3,56% | -9,09% | 23,30% | 8,37% |
| SOL | 88.11 | 2.69631 | 80,64 | 77,81 | 81,27 | 3,72% | -15,17% | 33,78% | 24,42% |
| DOGE | 82.99 | 0.00284 | 0.07522 | 0.07327 | 0.08926 | -1,18% | -15,60% | 26,73% | -7,49% |

## Dettaglio asset

### BTC

- Prezzo: **80.568 $**
- Punteggio tecnico: **11 / 12**
- Verdetto: **RIALZISTA TECNICO**
- Trend: **Trend rialzista** (3)
- Momentum: **Momentum in miglioramento** (3)
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
  - Due minimi simili vicino a 62.201 tra 2026-06-18 e 2026-08-14. Neckline stimata: 66.910. Breakout neckline: 2026-08-19 (6 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 71.619; progresso corrente: 290,04%. Relazione prezzo/neckline: sopra neckline.
  - neckline 66.910; target 71.619; breakout 2026-08-19 (6g); progresso 290,04%; prezzo sopra neckline.
- Triplo minimo: **TARGET RAGGIUNTO** (0)
  - Tre minimi simili vicino a 62.201 dal 2026-06-18 al 2026-08-14. Neckline stimata: 66.910. Breakout neckline: 2026-08-19 (6 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 71.619; progresso corrente: 290,04%. Relazione prezzo/neckline: sopra neckline.
  - neckline 66.910; target 71.619; breakout 2026-08-19 (6g); progresso 290,04%; prezzo sopra neckline.
- Adam and Eve Bottom: **TARGET RAGGIUNTO** (0)
  - Pattern Adam and Eve Bottom vicino a 59.109 dal 2026-06-05 al 2026-08-14. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 67.248. Breakout neckline: 2026-08-19 (6 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 75.387; progresso corrente: 163,65%. Relazione prezzo/neckline: sopra neckline.
  - neckline 67.248; target 75.387; breakout 2026-08-19 (6g); progresso 163,65%; prezzo sopra neckline.
- Doppio massimo: **CANDIDATO** (0)
  - Due massimi simili vicino a 65.544 tra 2026-06-22 e 2026-08-09. Neckline ribassista stimata: 57.748. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 16 giorni.
  - neckline 57.748; target 49.952; distanza dalla neckline 39,52%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 65.544 dal 2026-06-22 al 2026-08-09. Neckline ribassista stimata: 57.748. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 16 giorni.
  - neckline 57.748; target 49.952; distanza dalla neckline 39,52%; prezzo sopra neckline.
- Adam and Eve Top: **CANDIDATO** (0)
  - Pattern Adam and Eve Top vicino a 67.248 dal 2026-06-15 al 2026-07-21. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 57.748. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 35 giorni.
  - neckline 57.748; target 48.247; distanza dalla neckline 39,52%; prezzo sopra neckline.

### SOL

- Prezzo: **102,48 $**
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
- Fibonacci automatico: **RECUPERATO** (0)
  - Swing DOWN 2026-05-11 98,27 -> 2026-08-16 74,20; livello più vicino 78.6% a 93,12; stato RECUPERATO; confluenza: nessuna confluenza indipendente.
- Punteggio pattern: **0**
  - rialzista dominante: Doppio minimo (TARGET RAGGIUNTO, 0); ribassista dominante: Doppio massimo (CANDIDATO, 0).
- Supporto più vicino: **74,20**
- Resistenza più vicina: **127,97**

Pattern classici e ciclo di vita:

- Doppio minimo: **TARGET RAGGIUNTO** (0)
  - Due minimi simili vicino a 73,40 tra 2026-07-17 e 2026-08-16. Neckline stimata: 78,73. Breakout neckline: 2026-08-19 (6 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 84,05; progresso corrente: 446,15%. Relazione prezzo/neckline: sopra neckline.
  - neckline 78,73; target 84,05; breakout 2026-08-19 (6g); progresso 446,15%; prezzo sopra neckline.
- Triplo minimo: **TARGET RAGGIUNTO** (0)
  - Tre minimi simili vicino a 70,69 dal 2026-07-17 al 2026-08-16. Neckline stimata: 78,73. Breakout neckline: 2026-08-19 (6 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 86,76; progresso corrente: 295,75%. Relazione prezzo/neckline: sopra neckline.
  - neckline 78,73; target 86,76; breakout 2026-08-19 (6g); progresso 295,75%; prezzo sopra neckline.
- Adam and Eve Bottom: **TARGET RAGGIUNTO** (0)
  - Pattern Adam and Eve Bottom vicino a 67,92 dal 2026-06-19 al 2026-08-01. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 83,81. Breakout neckline: 2026-08-19 (6 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 99,70; progresso corrente: 117,50%. Relazione prezzo/neckline: sopra neckline.
  - neckline 83,81; target 99,70; breakout 2026-08-19 (6g); progresso 117,50%; prezzo sopra neckline.
- Doppio massimo: **CANDIDATO** (0)
  - Due massimi simili vicino a 77,62 tra 2026-06-22 e 2026-08-09. Neckline ribassista stimata: 64,42. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 16 giorni.
  - neckline 64,42; target 51,22; distanza dalla neckline 59,09%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 78,88 dal 2026-07-15 al 2026-08-09. Neckline ribassista stimata: 70,69. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 16 giorni.
  - neckline 70,69; target 62,51; distanza dalla neckline 44,96%; prezzo sopra neckline.
- Adam and Eve Top: **CANDIDATO** (0)
  - Pattern Adam and Eve Top vicino a 77,62 dal 2026-06-15 al 2026-08-09. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 64,42. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 16 giorni.
  - neckline 64,42; target 51,22; distanza dalla neckline 59,09%; prezzo sopra neckline.

### DOGE

- Prezzo: **0.09289 $**
- Punteggio tecnico: **7 / 12**
- Verdetto: **RIALZISTA TECNICO**
- Trend: **Trend misto** (1)
- Momentum: **Momentum in miglioramento** (3)
- Volume: **Volume da accumulazione** (1)
- Struttura: **Struttura rialzista con massimi e minimi crescenti** (2)
  - Dettaglio struttura: Ultimi minimi: 0.06835 -> 0.06895. Ultimi massimi: 0.07117 -> 0.07286.
- Divergenza: **Nessuna** (0)
- Fase Wyckoff candidata: **Range / fase non chiara** (0)
  - Dettaglio Wyckoff: Posizione nel range a 120 giorni: 49,55%. Fase non abbastanza chiara.
- Fibonacci automatico: **REJECTION** (0)
  - Swing DOWN 2026-05-14 0.11825 -> 2026-08-12 0.06895; livello più vicino 50.0% a 0.09360; stato REJECTION; confluenza: nessuna confluenza indipendente.
- Punteggio pattern: **0**
  - rialzista dominante: Triplo minimo (TARGET RAGGIUNTO, 0); ribassista dominante: Doppio massimo (CANDIDATO, 0).
- Supporto più vicino: **0.06895**
- Resistenza più vicina: **0.11825**

Pattern classici e ciclo di vita:

- Doppio minimo: **TARGET RAGGIUNTO** (0)
  - Due minimi simili vicino a 0.06829 tra 2026-07-24 e 2026-08-12. Neckline stimata: 0.07380. Breakout neckline: 2026-08-19 (6 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 0.07931; progresso corrente: 346,33%. Relazione prezzo/neckline: sopra neckline.
  - neckline 0.07380; target 0.07931; breakout 2026-08-19 (6g); progresso 346,33%; prezzo sopra neckline.
- Triplo minimo: **TARGET RAGGIUNTO** (0)
  - Tre minimi simili vicino a 0.06835 dal 2026-06-30 al 2026-08-12. Neckline stimata: 0.07923. Breakout neckline: 2026-08-20 (5 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 0.09012; progresso corrente: 125,46%. Relazione prezzo/neckline: sopra neckline.
  - neckline 0.07923; target 0.09012; breakout 2026-08-20 (5g); progresso 125,46%; prezzo sopra neckline.
- Adam and Eve Bottom: **TARGET RAGGIUNTO** (0)
  - Pattern Adam and Eve Bottom vicino a 0.06829 dal 2026-07-24 al 2026-08-06. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 0.07380. Breakout neckline: 2026-08-19 (6 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 0.07931; progresso corrente: 346,33%. Relazione prezzo/neckline: sopra neckline.
  - neckline 0.07380; target 0.07931; breakout 2026-08-19 (6g); progresso 346,33%; prezzo sopra neckline.
- Doppio massimo: **CANDIDATO** (0)
  - Due massimi simili vicino a 0.07380 tra 2026-07-26 e 2026-08-11. Neckline ribassista stimata: 0.06797. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 14 giorni.
  - neckline 0.06797; target 0.06214; distanza dalla neckline 36,66%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 0.07923 dal 2026-07-04 al 2026-08-11. Neckline ribassista stimata: 0.06797. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 14 giorni.
  - neckline 0.06797; target 0.05671; distanza dalla neckline 36,66%; prezzo sopra neckline.
- Adam and Eve Top: **CANDIDATO** (0)
  - Pattern Adam and Eve Top vicino a 0.07923 dal 2026-07-04 al 2026-08-11. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 0.06797. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 14 giorni.
  - neckline 0.06797; target 0.05671; distanza dalla neckline 36,66%; prezzo sopra neckline.

## Fibonacci automatico

Il modulo seleziona uno swing recente tramite pivot confermati. Un semplice tocco vale 0: Fibonacci pesa al massimo ±1 soltanto quando il livello è tenuto, perso, recuperato o respinto e coincide con almeno un livello tecnico indipendente.

| Asset   | Swing                         | 23,6%   | 38,2%   | 50,0%   | 61,8%   | 78,6%   | Livello vicino   | Stato      | Confluenza                      |   Score |
|:--------|:------------------------------|:--------|:--------|:--------|:--------|:--------|:-----------------|:-----------|:--------------------------------|--------:|
| BTC | DOWN 2026-05-06 -> 2026-08-14 | 67.280 | 70.244 | 72.640 | 75.036 | 78.447 | 78.6% / 78.447 | TESTATO | nessuna confluenza indipendente | 0 |
| SOL | DOWN 2026-05-11 -> 2026-08-16 | 79,88 | 83,40 | 86,24 | 89,07 | 93,12 | 78.6% / 93,12 | RECUPERATO | nessuna confluenza indipendente | 0 |
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

- **BTC**: 24/30 previsioni controllate su 52 fatte. Stato: **RACCOLTA DATI**.
- **SOL**: 24/30 previsioni controllate su 52 fatte. Stato: **RACCOLTA DATI**.
- **DOGE**: 24/30 previsioni controllate su 52 fatte. Stato: **RACCOLTA DATI**.

| Asset | Previsioni fatte | Controllate | Progresso | In attesa | Stato | Prossimo controllo |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 52 | 24 | 24/30 [████████░░] | 28 | RACCOLTA DATI | 2026-08-26 / tra 1 giorno |
| SOL | 52 | 24 | 24/30 [████████░░] | 28 | RACCOLTA DATI | 2026-08-26 / tra 1 giorno |
| DOGE | 52 | 24 | 24/30 [████████░░] | 28 | RACCOLTA DATI | 2026-08-26 / tra 1 giorno |

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

Generato: 2026-08-25 05:32 UTC


<!-- DIRECT_REPORT_LINK -->
Report separato completo: [data_quality_coherence_report.md](data_quality_coherence_report.md)

Questo controllo non modifica punteggi o decisioni. Verifica che tutti i moduli usino lo stesso prezzo corrente e che le nuove regole Technical/Classic Visual siano integre.

## Stato finale: **WARN**

## Avvisi

- 2 campi prezzo superano la tolleranza specifica del modulo.

## Prezzo unico per modulo

| Modulo                  | Asset   | Campo             | Stato   | Prezzo snapshot   | Prezzo modulo   | Differenza   |
|:------------------------|:--------|:------------------|:--------|:------------------|:----------------|:-------------|
| Scanner                 | BTC     | current_price     | OK      | 80.568 $          | 80.568 $        | +0,0000%     |
| Scanner                 | DOGE    | current_price     | OK      | 0.09289 $         | 0.09289 $       | -0,0000%     |
| Scanner                 | SOL     | current_price     | OK      | 102,48 $          | 102,48 $        | +0,0000%     |
| Scanner Forecast        | BTC     | current_price     | OK      | 80.568 $          | 80.568 $        | +0,0000%     |
| Scanner Forecast        | SOL     | current_price     | OK      | 102,48 $          | 102,48 $        | +0,0000%     |
| Scanner Forecast        | DOGE    | current_price     | OK      | 0.09289 $         | 0.09289 $       | -0,0000%     |
| Technical Structure     | BTC     | price             | OK      | 80.568 $          | 80.568 $        | +0,0000%     |
| Technical Structure     | SOL     | price             | OK      | 102,48 $          | 102,48 $        | +0,0000%     |
| Technical Structure     | DOGE    | price             | OK      | 0.09289 $         | 0.09289 $       | -0,0000%     |
| Classic Technical       | BTC     | price             | OK      | 80.568 $          | 80.568 $        | +0,0000%     |
| Classic Technical       | SOL     | price             | OK      | 102,48 $          | 102,48 $        | +0,0000%     |
| Classic Technical       | DOGE    | price             | OK      | 0.09289 $         | 0.09289 $       | -0,0000%     |
| Classic Visual          | BTC     | price             | OK      | 80.568 $          | 80.568 $        | +0,0000%     |
| Classic Visual          | SOL     | price             | OK      | 102,48 $          | 102,48 $        | +0,0000%     |
| Classic Visual          | DOGE    | price             | OK      | 0.09289 $         | 0.09289 $       | -0,0000%     |
| Exchange Microstructure | BTC     | price             | OK      | 80.568 $          | 80.493 $        | -0,0924%     |
| Exchange Microstructure | SOL     | price             | WARN    | 102,48 $          | 101,92 $        | -0,5435%     |
| Exchange Microstructure | DOGE    | price             | WARN    | 0.09289 $         | 0.09243 $       | -0,4952%     |
| RSI top-cycle           | SOL     | current_price     | OK      | 102,48 $          | 102,48 $        | +0,0000%     |
| RSI top-cycle           | SOL     | current_price     | OK      | 102,48 $          | 102,48 $        | +0,0000%     |
| Frattale BTC/SOL        | SOL     | sol_current_price | OK      | 102,48 $          | 102,48 $        | +0,0000%     |
| Fractal path            | SOL     | current_price     | OK      | 102,48 $          | 102,48 $        | +0,0000%     |

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

Generato: 2026-08-26T04:30:34+00:00

- Modalità: **SOLO PAPER TRADING**
- Asset: **SOL spot**
- Leva: **nessuna (1x)**
- Capitale iniziale separato: **€40.000,00**
- Fonte mercato: **KUCOIN_PUBLIC_API**; nuove entrate: **CONSENTITE**

| Equity | Cash | SOL | Prezzo | Rendimento | Realizzato | Commissioni | Max DD | Operazioni |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| €43.453,09 | €43.453,09 | 0.000019 | 97.0320 | +8.63% | €3.453,09 | €75,44 | 6.48% | 45 |

**Ultima decisione:** HOLD — Prezzo dentro la fascia neutrale.

Bande 4H: L2 89.1587 · L1 91.8230 · media 95.1534 · U1 98.4837 · U2 101.1480.

> Questo portafoglio non condivide capitale, posizioni o statistiche con il paper trading da €10.000.
<!-- SOL_SPOT_ADAPTIVE_END -->
