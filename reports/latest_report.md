<!-- COMPACT_REPORT_HEADER_START -->
> **Vista compatta:** Decisione operativa, Global Confluence e cambiamenti giornalieri restano aperti. Tocca il titolo di una sezione per mostrare o nascondere i dettagli.  
> Tutte le tabelle e tutti i dati restano nel file: copiando il Markdown raw viene copiato tutto.
<!-- COMPACT_REPORT_HEADER_END -->

<!-- COMPACT_SECTION_START:btc_macro_cycle -->
<details>
<summary><strong>🌀 Bitcoin Macro Cycle — Power Law e Spiral</strong></summary>

<!-- BTC_MACRO_CYCLE_START -->
# Bitcoin Macro Cycle — Power Law e Four-Year Spiral

Generato: 2026-09-24 05:32 UTC

Questo modulo descrive il contesto macro di Bitcoin. Non genera entrate tattiche, non autorizza leva e pesa **0** nel Global Confluence.

## Sintesi

| Voce | Valore | Lettura |
| --- | --- | --- |
| Prezzo BTC | 84.116 $ | prezzo corrente |
| Power Law centrale | 125.737 $ | deviazione -33,10% |
| Banda p10-p90 | 78.110 $ / 317.060 $ | BASSA NEL CORRIDOIO |
| Percentile residuo | 17,24% | posizione storica nel corridoio |
| Esponente β | 5,7946 | R² log-log 91,93% |
| Stabilità β | BASSA | range 1,3167 cambiando finestra |
| Ultimo halving | 2024-04-19 | 888 giorni fa |
| Fase ciclo | 60,78% | percentuale indicativa del ciclo quadriennale |
| Peso Global | 0 | CONTESTO MACRO / DIAGNOSTICO |

La Power Law viene trattata come regressione empirica, non come legge fisica. Il report mostra quanto cambia l'esponente usando finestre iniziali diverse e la confronta con il benchmark ingenuo 'prezzo invariato'.

## Bitcoin Power Law

- Campione: 2014-09-17 → 2026-09-24 (4390 osservazioni)
- Formula stimata: prezzo ≈ exp(-38.9845) × giorni^5.7946
- Prezzo centrale oggi: **125.737 $**
- Posizione corrente: **BASSA NEL CORRIDOIO**, percentile 17,24%
- Scarto dal centro: **-33,10%**

![Bitcoin Power Law](btc_power_law_chart.png)

![Bitcoin Power Law log-log](btc_power_law_loglog_chart.png)

### Stabilità dell'esponente

| Inizio campione | β | R² log-log |
| --- | --- | --- |
| 2014 | 5,7946 | 91,93% |
| 2015 | 5,8756 | 91,48% |
| 2016 | 5,5585 | 87,75% |
| 2017 | 4,8325 | 82,98% |
| 2018 | 4,5589 | 78,52% |

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
| 2012-11-28 → 2016-07-09 | 2015-02-08 | +30,59% | +8,24% | +25,14% | +67,16% |
| 2016-07-09 → 2020-05-11 | 2018-11-08 | -46,14% | -47,10% | -9,67% | +36,43% |
| 2020-05-11 → 2024-04-19 | 2022-10-03 | +2,73% | -15,28% | +44,78% | +39,78% |

Campione molto piccolo: questi rendimenti sono contesto di ciclo, non probabilità affidabili.

## SOL/BTC e DOGE/BTC dentro il tempo Bitcoin

![Altcoin nel ciclo BTC](alt_btc_cycle_spirals.png)

| Asset | Coppia | Forza vs BTC | Score raw | Candidato | 30g | Peso Global |
| --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | SOVRAPERFORMA BTC | 6 | 1 | 10.016027629237346 | 0 |
| DOGE | DOGE/BTC | RELATIVA MISTA / NON CONFERMATA | -2 | 0 | -1.5515997604615972 | 0 |

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

Generato: 2026-09-24 05:32 UTC

Questo modulo controlla se SOL e DOGE stanno davvero battendo Bitcoin. Una salita in USD accompagnata da una coppia ALT/BTC ribassista è spesso soltanto trascinamento di BTC.

**Protezione iniziale:** il candidato relativo è limitato a -1/0/+1, ma il peso nel Global resta **0**. La coppia BTC conferma o indebolisce il tecnico USD; non viene sommata come secondo modulo indipendente.

## Sintesi

| Asset | Coppia | Prezzo | Score raw | Candidato | Peso Global | Forza vs BTC | Confidenza | 30g | Tecnico USD | Lettura combinata |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SOL | SOL/BTC | 0.00137300 | +6 | +1 | 0 | SOVRAPERFORMA BTC | MEDIA | +10,02% | RIALZISTA | CONFERMA FORTE: sale in USD e batte BTC |
| DOGE | DOGE/BTC | 0.00000112 | -2 | 0 | 0 | RELATIVA MISTA / NON CONFERMATA | BASSA | -1,55% | RIALZISTA | QUADRO MISTO / NESSUNA CONFERMA RELATIVA |

## Matrice di lettura

| ALT/USD | ALT/BTC | Interpretazione |
| --- | --- | --- |
| Rialzista | Rialzista | Conferma migliore: sale e batte BTC |
| Rialzista | Ribassista | Sale soprattutto perché BTC trascina il mercato |
| Ribassista | Rialzista | Forza relativa nascosta / possibile rotazione futura |
| Ribassista | Ribassista | Debolezza completa |

## SOL/BTC

- **Verdetto relativo:** SOVRAPERFORMA BTC (+6)
- **Candidato futuro:** +1; **peso attuale Global: 0**
- **Lettura combinata USD/BTC:** CONFERMA FORTE: sale in USD e batte BTC
- **Struttura:** MASSIMI E MINIMI CRESCENTI
- **Rendimenti relativi:** 7g +6,02%; 30g +10,02%; 90g +21,29%; 180g +9,75%
- **Daily:** RSI 62.01; MA50 0.00126758; MA200 0.00118878
- **Weekly:** MA30 0.00119607; RSI 61.09
- **Livelli:** supporto 0.00127800; resistenza 0.00140500; breakout 60g 0.00140500; breakdown 60g 0.00112700
- **Pattern:** DOPPIO MINIMO / TARGET RAGGIUNTO; neckline 0.00133900; target 0.00140150
- **Fibonacci:** NON ATTIVO — 23.6% a 0.00131154
- **Fonte:** Yahoo Finance SOL-BTC (coppia diretta)
- **Motivi score:** prezzo sopra MA50 daily; prezzo sopra MA200 daily; MA50 daily in salita; prezzo sopra MA30 weekly; MA30 weekly in discesa; struttura con massimi/minimi crescenti; RSI relativo forte; MACD relativo positivo

![Grafico SOL/BTC](relative_strength_SOLBTC.png)

## DOGE/BTC

- **Verdetto relativo:** RELATIVA MISTA / NON CONFERMATA (-2)
- **Candidato futuro:** 0; **peso attuale Global: 0**
- **Lettura combinata USD/BTC:** QUADRO MISTO / NESSUNA CONFERMA RELATIVA
- **Struttura:** MASSIMI E MINIMI DECRESCENTI
- **Rendimenti relativi:** 7g +5,56%; 30g -1,55%; 90g -10,49%; 180g -17,39%
- **Daily:** RSI 54.15; MA50 0.00000110; MA200 0.00000124
- **Weekly:** MA30 0.00000124; RSI 42.02
- **Livelli:** supporto 0.00000112; resistenza 0.00000114; breakout 60g 0.00000131; breakdown 60g 0.00000099
- **Pattern:** DOPPIO MINIMO / TARGET RAGGIUNTO; neckline 0.00000115; target 0.00000128
- **Fibonacci:** VICINO — 23.6% a 0.00000112
- **Fonte:** Rapporto sintetico DOGE-USD / BTC-USD (sintetica)
- **Motivi score:** prezzo sopra MA50 daily; prezzo sotto MA200 daily; prezzo sotto MA30 weekly; MA30 weekly in discesa; struttura con massimi/minimi decrescenti; MACD relativo positivo

![Grafico DOGE/BTC](relative_strength_DOGEBTC.png)

## Backtest storico diagnostico

Il backtest usa soltanto indicatori disponibili alla data del segnale e campiona una volta a settimana. È utile subito, ma non sostituisce il tracker live: le soglie sono state definite prima di vedere il risultato.

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto direzione | Return futuro mediano |
| --- | --- | --- | --- | --- | --- |
| SOL | 7g | 209 | 52,63% | +1,96% | -1,05% |
| SOL | 30g | 206 | 47,57% | +4,57% | +0,58% |
| SOL | 90g | 200 | 52,50% | +9,74% | +3,06% |
| DOGE | 7g | 295 | 55,59% | +1,83% | -1,68% |
| DOGE | 30g | 294 | 53,06% | +1,97% | -3,49% |
| DOGE | 90g | 288 | 54,17% | +6,90% | -9,24% |

## Tracker live e gate futuro

| Asset | Orizzonte | Controlli | Accuratezza | Return corretto | Stato | Peso Global |
| --- | --- | --- | --- | --- | --- | --- |
| SOL | 1g | 37 | 56,76% | +0,13% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 3g | 35 | 54,29% | +0,48% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 7g | 35 | 42,86% | +0,55% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 14g | 35 | 45,71% | +0,61% | LOCKED / RACCOLTA LIVE | 0 |
| SOL | 30g | 22 | 31,82% | -4,88% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 1g | 54 | 66,67% | -0,02% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 3g | 54 | 57,41% | +0,01% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 7g | 54 | 53,70% | -0,57% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 14g | 47 | 57,45% | +0,08% | LOCKED / RACCOLTA LIVE | 0 |
| DOGE | 30g | 35 | 65,71% | +0,39% | LOCKED / RACCOLTA LIVE | 0 |

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

Ultima candela SOL usata: **24 settembre 2026**

## SOL PRICE CONTEXT

| Voce | Valore | Provenienza / significato |
| --- | --- | --- |
| Anchor computazionale | 115,45 $ | 2026-09-24T05:30:21Z \| Yahoo Finance daily shared snapshot \| Close 1d |
| Candela anchor completata | NO | Stato esplicito; il valore non viene sostituito dal prezzo pubblico. |
| Riferimento pubblico corrente | 115,29 $ | 2026-09-24T05:32:00Z \| Yahoo Finance \| solo display |
| Età anchor alla generazione | 0h 1m | WITHIN_DAILY_REPORT_CADENCE |
| Gap corrente vs anchor | -0,16000 $ | -0,14% |
| Validità input modello | REPRODUCIBLE_SHARED_SNAPSHOT | Non è una dichiarazione di validità del segnale/trading. |

```text
COMPUTATIONAL_ANCHOR_PRICE=115.44999694824219
COMPUTATIONAL_ANCHOR_FIELD=Close
COMPUTATIONAL_ANCHOR_TIMESTAMP=2026-09-24T05:30:21Z
COMPUTATIONAL_ANCHOR_SYMBOL=SOL-USD
COMPUTATIONAL_ANCHOR_PROVIDER=Yahoo Finance daily shared snapshot
COMPUTATIONAL_ANCHOR_TIMEFRAME=1d
COMPUTATIONAL_ANCHOR_COMPLETED=NO
CURRENT_PUBLIC_REFERENCE_PRICE=115.29000091552734
CURRENT_PUBLIC_REFERENCE_TIMESTAMP=2026-09-24T05:32:00Z
CURRENT_PUBLIC_REFERENCE_ACQUIRED_AT=2026-09-24T05:32:08Z
CURRENT_PUBLIC_REFERENCE_SYMBOL=SOL-USD
CURRENT_PUBLIC_REFERENCE_PROVIDER=Yahoo Finance
CURRENT_PUBLIC_REFERENCE_FIELD=Close
CURRENT_PUBLIC_REFERENCE_TIMEFRAME=1m
CURRENT_PUBLIC_REFERENCE_STATUS=AVAILABLE
ANCHOR_AGE_SECONDS=107.263255
ANCHOR_AGE_HOURS=0.029795348611111112
CURRENT_VS_ANCHOR_GAP_USD=-0.15999603271484375
CURRENT_VS_ANCHOR_GAP_PCT=-0.13858470068783824
```

## Verdetto: STRUTTURA ANALOGA, PREZZO NON ADERENTE

- **Fase attuale:** FRATTALE NON CONFERMATO DAL PREZZO
- **Somiglianza totale:** +69,04%
- **Somiglianza strutturale:** +69,04%
- **Aderenza prezzo live:** +69,05%
- **Errore medio live:** +15,48%
- **Gap prezzo corrente:** +42,05%
- **Peso operativo suggerito:** 0
- **Affidabilita:** BASSA / NON OPERATIVO
- **Rischio fase:** ALTO
- **Trend tracking:** STRUTTURA STABILE
- **Sintesi:** La geometria ricorda BTC 2022, ma SOL è troppo distante dal percorso scalato per usarlo come conferma operativa.
- **SOL è al giorno:** 110 dal bottom usato.
- **Giorno BTC equivalente:** 2023-03-11
- **Prossimo step:** Proiezione condizionale, non conferma operativa: **Spinta rialzista abbastanza pulita.** Zona bassa **115,45 $** intorno al **24 settembre 2026**; zona alta **158,54 $** intorno al **6 ottobre 2026**; fine step circa **153,85 $** entro il **8 ottobre 2026**.

### Metadata aderenza prezzo

```text
OPERATIONAL_VERDICT_REASON=STRUTTURA ANALOGA, PREZZO NON ADERENTE
PRICE_ADHERENCE_FAILED=YES
PRICE_ADHERENCE_LIVE_AVG_GAP_FAILED=YES
PRICE_ADHERENCE_LAST_GAP_FAILED=YES
PRICE_ADHERENCE_LIVE_AVG_GAP_THRESHOLD_PCT=15.0
PRICE_ADHERENCE_LAST_GAP_THRESHOLD_PCT=18.0
PRICE_ADHERENCE_OBSERVED_LIVE_AVG_GAP_PCT=15.476038892527484
PRICE_ADHERENCE_OBSERVED_LAST_GAP_PCT=42.04704419640599
```

## Somiglianza prima e dopo inizio programma

Questa sezione separa la somiglianza della forma dall'aderenza reale del prezzo.

- **Inizio programma/scanner:** 3 luglio 2026
- **Prima del programma** = backtest retroattivo.
- **Da inizio programma** = verifica live: è la parte più importante per l'uso operativo.

| Periodo | Date | Giorni | Aderenza prezzo | Errore medio | Gap ultimo | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| Prima del programma | 6 giugno 2026 -> 2 luglio 2026 | 27 | +87,95% | +6,02% | +21,89% | ABBASTANZA ALLINEATO |
| Da inizio programma | 3 luglio 2026 -> 24 settembre 2026 | 84 | +69,05% | +15,48% | +42,05% | STACCATO / NON ADERENTE |
| Totale dal bottom | 6 giugno 2026 -> 24 settembre 2026 | 111 | +73,65% | +13,18% | +42,05% | DEVIAZIONE MODERATA |

Nota: un frattale può avere una forma simile ma un prezzo distante. In quel caso non è operativo finché il gap non rientra.

## Lettura operativa veloce

Il frattale resta non operativo. Motivo effettivo: STRUTTURA ANALOGA, PREZZO NON ADERENTE.

| Voce | Risposta | Perché |
| --- | --- | --- |
| Uso operativo | NO | Peso 0 per il verdetto: STRUTTURA ANALOGA, PREZZO NON ADERENTE. |
| Aderenza live | +69,05% | Errore medio live +15,48%. |
| Gap corrente | +42,05% | Prezzo non aderente: superata almeno una soglia canonica (15% medio / 18% ultimo). |
| Prima conferma prezzo | 158,54 $ | Serve anche miglioramento del gap, non solo una candela sopra il livello. |
| Seconda conferma | 170,58 $ | Rende più credibile il percorso, ma non sostituisce l'aderenza. |
| Invalidazione soft | 109,68 $ | Sotto questa zona il quadro peggiora. |
| Invalidazione forte | 62,19 $ | Sotto il bottom il paragone è quasi rotto. |

## Target ciclo fino al top BTC 2025

| Voce | Valore |
| --- | --- |
| Stato | CONTESTO / NON OPERATIVO |
| Top BTC 2025 | 6 ottobre 2025 - 124.753 $ |
| Data SOL equivalente | 21 aprile 2029 |
| Target ciclo base dall'anchor modello | 698,06 $ |
| Massimo percorso base | 698,06 $ (21 aprile 2029) |

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
| Prima conferma | 158,54 $ | Deve accompagnarsi al rientro del gap. |
| Seconda conferma | 170,58 $ | Scenario più credibile. |
| Invalidazione soft | 109,68 $ | Il frattale si indebolisce. |
| Invalidazione forte | 62,19 $ | Il paragone si rompe. |

## Proiezione veloce con date SOL

| Orizzonte | Data SOL | BTC fece | SOL base | Min percorso | Max percorso |
| --- | --- | --- | --- | --- | --- |
| 7 giorni | 1 ottobre 2026 | +30,70% | 150,89 $ | 115,45 $ | 153,45 $ |
| 14 giorni | 8 ottobre 2026 | +33,26% | 153,85 $ | 115,45 $ | 158,54 $ |
| 30 giorni | 24 ottobre 2026 | +43,72% | 165,93 $ | 115,45 $ | 165,93 $ |
| 60 giorni | 23 novembre 2026 | +33,88% | 154,56 $ | 115,45 $ | 170,58 $ |
| 90 giorni | 23 dicembre 2026 | +28,34% | 148,17 $ | 115,45 $ | 170,58 $ |
| 120 giorni | 22 gennaio 2027 | +46,23% | 168,83 $ | 115,45 $ | 174,34 $ |

## Prossimi step se SOL segue BTC 2022

| Step | Date SOL | BTC fine | SOL zona bassa | SOL zona alta | SOL fine base | Lettura |
| --- | --- | --- | --- | --- | --- | --- |
| Step 1 - prossime 2 settimane | 24 settembre 2026 -> 8 ottobre 2026 | +33,26% | 115,45 $ (24 settembre 2026) | 158,54 $ (6 ottobre 2026) | 153,85 $ | Spinta rialzista abbastanza pulita. |
| Step 2 - primo mese | 9 ottobre 2026 -> 24 ottobre 2026 | +43,72% | 151,86 $ (10 ottobre 2026) | 165,93 $ (24 ottobre 2026) | 165,93 $ | Spinta rialzista abbastanza pulita. |
| Step 3 - secondo mese | 25 ottobre 2026 -> 23 novembre 2026 | +33,88% | 152,63 $ (4 novembre 2026) | 170,58 $ (28 ottobre 2026) | 154,56 $ | Spinta rialzista abbastanza pulita. |
| Step 4 - terzo mese | 24 novembre 2026 -> 23 dicembre 2026 | +28,34% | 144,14 $ (19 dicembre 2026) | 157,16 $ (11 dicembre 2026) | 148,17 $ | Spinta rialzista abbastanza pulita. |

Nota: le proiezioni restano condizionali; il prezzo non è aderente secondo le soglie canoniche.

<!-- BTC_SOL_FRACTAL_END -->

</details>
<!-- COMPACT_SECTION_END:btc_sol_fractal -->

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
| Prezzo SOL | 115,45 $ |
| TVL Solana | 6,40 mld $ |
| TVL 7g | +10,70% |
| DEX volume 24h | 2,68 mld $ |
| Fees 24h | 16,53 mln $ |
| Stablecoin su Solana | 16,37 mld $ |
| Stake ratio | 69,33% |
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
| Trend squeeze | MIGLIORAMENTO |
| Trend squeeze score | 1 |
| Confronto precedente | 2026-09-21 |
| Fonte prezzi | Yahoo Finance SOL-USD weekly |
| Prezzo SOL | 115,45 $ |
| EMA200 weekly target | 111,26 $ |
| Upside verso EMA200 | -3,51% |
| Distanza prezzo da EMA200 | +3,64% |
| Gap EMA50/EMA200 | -5,26% |
| Stato cross | EMA50 SOTTO EMA200 |
| RSI weekly | 62,85 |
| Età SOL | 6,5 anni |
| Analoghi storici usati | 30 |
| Max analoghi per asset | 3 |
| Hit EMA200 12w analoghi | +100,00% |
| Max gain mediano 12w | +21,62% |
| Drawdown mediano 12w | -40,20% |

Lettura semplice:

**SOLO OSSERVAZIONE**

Autocontrollo: **MIGLIORAMENTO**.

Questo modulo confronta SOL con altre crypto in fasi simili di età, distanza da EMA200, EMA50/EMA200 e RSI. Non usa stock market.

Nota importante: **questo modulo ora NON pesa più nel Global Confluence**. Resta solo come contesto di ciclo e come mappa verso EMA200 weekly. Il punteggio Global resta guidato da prezzo, scanner, regime, struttura tecnica, frattale, RSI e conferme reali.

Nota: se EMA50/EMA200 sono dentro ±2%, il modulo parla di medie sovrapposte / incrocio in corso, perché exchange diversi possono mostrare il cross leggermente prima o dopo.

<!-- Generato: 2026-09-24 05:32 UTC -->
<!-- MAJOR_ALT_LIFECYCLE_SQUEEZE_END -->

</details>
<!-- COMPACT_SECTION_END:major_alt_lifecycle -->

# Report giornaliero BTC / SOL / DOGE

Aggiornato il: **2026-09-24 05:30:22 UTC**

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
- DOGE: cambiamento importante in peggioramento rispetto a ieri.

| Asset | Cambio | Tono | Verdetto oggi | Casi positivi oggi | Δ casi positivi |
| --- | --- | --- | --- | --- | --- |
| BTC | CAMBIAMENTO MEDIO | peggioramento | RIALZISTA | +67.50% | -2.50 punti |
| SOL | NESSUN CAMBIAMENTO FORTE | peggioramento | NEUTRALE / INCERTO | +50.00% | -2.50 punti |
| DOGE | CAMBIAMENTO MEDIO | peggioramento | RIBASSISTA | +30.00% | -2.50 punti |

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
| BTC | 79.974 $ | 92.602 $ | +40,00% | +15,79% | rimbalzo debole | 92.602 $ | 79.974 $ | +7,14% | -13,64% | spike storicamente più resistente |
| SOL | 109,68 $ | 126,99 $ | +30,77% | +15,79% | rimbalzo poco frequente | 126,99 $ | 109,68 $ | +24,00% | -13,64% | spike storicamente più resistente |
| DOGE | 0,08976 $ | 0,10393 $ | +18,18% | +15,79% | rimbalzo poco frequente | 0,10393 $ | 0,08976 $ | +33,33% | -13,64% | spike storicamente più resistente |

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

- **BTC: su 40 casi simili, 20 prima sono scesi a -5,00%. Tra quei 20, 8 poi sono rimbalzati fino a +10,00%. Percentuale: +40,00% (8/20). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.**
- **BTC: su 40 casi simili, 28 prima sono saliti a +10,00%. Tra quei 28, 2 poi sono scaricati a -5,00%. Percentuale: +7,14% (2/28). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.**
- **SOL: su 40 casi simili, 26 prima sono scesi a -5,00%. Tra quei 26, 8 poi sono rimbalzati fino a +10,00%. Percentuale: +30,77% (8/26). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.**
- **SOL: su 40 casi simili, 25 prima sono saliti a +10,00%. Tra quei 25, 6 poi sono scaricati a -5,00%. Percentuale: +24,00% (6/25). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.**
- **DOGE: su 40 casi simili, 33 prima sono scesi a -5,00%. Tra quei 33, 6 poi sono rimbalzati fino a +10,00%. Percentuale: +18,18% (6/33). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.**
- **DOGE: su 40 casi simili, 18 prima sono saliti a +10,00%. Tra quei 18, 6 poi sono scaricati a -5,00%. Percentuale: +33,33% (6/18). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.**

<!-- BOUNCE_AFTER_DRAWDOWN_END -->

</details>
<!-- COMPACT_SECTION_END:bounce_after_drawdown -->

<!-- COMPACT_SECTION_START:scanner_forecast -->
<details>
<summary><strong>🔭 Cono probabilistico dello scanner</strong></summary>

<!-- SCANNER_FORECAST_TRACKER_START -->
# Scanner forecast path / cono probabilistico

Generato: 2026-09-24 05:31:53 UTC

## Snapshot effettivamente usato

| Asset   | Snapshot prezzo   | Generazione snapshot prezzo   | Snapshot match scanner   |
|:--------|:------------------|:------------------------------|:-------------------------|
| BTC | 2026-09-24 | 2026-09-24T05:30:21Z | 2026-09-24 05:30:22 |
| SOL | 2026-09-24 | 2026-09-24T05:30:21Z | 2026-09-24 05:30:22 |
| DOGE | 2026-09-24 | 2026-09-24T05:30:21Z | 2026-09-24 05:30:22 |

La data di generazione del report non sostituisce la data degli input: se gli snapshot locali sono più vecchi, i valori restano riferiti agli snapshot indicati in tabella.

Questo report trasforma i 40 casi simili dello scanner in un cono previsionale leggibile.

Per ogni asset crea:

- banda larga p10-p90
- banda centrale p25-p75
- scenario centrale p50
- prezzo reale sovrapposto quando sono disponibili dati successivi

Correzione importante: il cono ora viene calcolato dai percorsi reali dei match storici, non solo dai percentili finali a 30 giorni. Quindi il grafico non deve più mostrare solo due puntini.

## Ultimo cono previsionale salvato

| Asset   | Data       | Prezzo iniziale   | Direzione scanner   | Casi positivi   | P10 30g     | P25 30g     | P50 30g     | P75 30g      | P90 30g      |
|:--------|:-----------|:------------------|:--------------------|:----------------|:------------|:------------|:------------|:-------------|:-------------|
| BTC | 2026-09-24 | 84.184 $ | SALITA | 67,50% | 65.845,78 $ | 77.551,30 $ | 91.351,82 $ | 105.232,22 $ | 138.820,39 $ |
| SOL | 2026-09-24 | 115,45 $ | INCERTO | 50,00% | 77,07 $ | 93,26 $ | 115,80 $ | 141,86 $ | 194,70 $ |
| DOGE | 2026-09-24 | 0.09448 $ | DISCESA | 30,00% | 0.03919 $ | 0.07438 $ | 0.08767 $ | 0.09774 $ | 0.14658 $ |

## Confronto raw / regime-adjusted

Il cono raw continua a usare i 40 casi dello scanner. Il cono regime-adjusted sceglie una sola coorte nella gerarchia SAME_BTC_AND_ASSET_REGIME → SAME_ASSET_REGIME → SAME_BTC_REGIME. Ogni livello richiede almeno 5 match; le coorti non vengono mai combinate e ogni fallback è dichiarato.

| Asset   | Stato adjusted              | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level   | selection_reason            | Raw p50 30g   | Adjusted p50 30g   | Raw p90 30g   | Adjusted p90 30g   |
|:--------|:----------------------------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:-----------------|:----------------------------|:--------------|:-------------------|:--------------|:-------------------|
| BTC | INSUFFICIENT_REGIME_MATCHES | NONE | 0 | 2 | 0 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES | 91.351,82 $ | n/a | 138.820,39 $ | n/a |
| SOL | INSUFFICIENT_REGIME_MATCHES | NONE | 0 | 2 | 0 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES | 115,80 $ | n/a | 194,70 $ | n/a |
| DOGE | INSUFFICIENT_REGIME_MATCHES | NONE | 0 | 2 | 0 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES | 0.08767 $ | n/a | 0.14658 $ | n/a |

## Grafici

### BTC

![Scanner forecast BTC](scanner_forecast_BTC.png)

#### Verifica storica e discrepanza

![Verifica storica cono BTC](scanner_forecast_history_BTC.png)

- Cono congelato il **2026-08-25**; verificato fino al **2026-09-24**; stato **COMPLETO 30/30g**.
- Reale **84.121,15 $**; p50 previsto **86.764,34 $**; scarto **-3,05%**.
- Errore medio assoluto **4,24%**; massimo **8,85%**; DENTRO p10-p90; DENTRO p25-p75.

#### Cono regime-adjusted

Gruppo selezionato: **NONE**; fallback: **NONE**; motivo: **INSUFFICIENT_REGIME_MATCHES**.

Non disponibile: INSUFFICIENT_REGIME_MATCHES (campione selezionato 0/5 match).

### SOL

![Scanner forecast SOL](scanner_forecast_SOL.png)

<!-- SOL_CONDITIONAL_ANALYSES_START -->
#### SOL — Analisi condizionata -5% → +10%

Queste analisi sono **separate dal cono SOL originale**. Il cono sopra continua a usare normalmente i **40 analoghi più simili a SOL**.

Il filtro condizionato parte proprio da quei 40 casi e conserva soltanto gli episodi che hanno toccato **prima -5%** dal proprio baseline e **successivamente +10% entro 30 giorni**.

##### A. Conditional Successor corrente — dinamico

Questo campione viene ricostruito ad ogni run dai **40 analoghi SOL correnti**. Di conseguenza il numero di episodi qualificati e gli asset possono cambiare giorno per giorno.

**Campione corrente:** 8 episodi qualificati su 40 · 7 asset distinti.

**SMALL SAMPLE / DIAGNOSTIC ONLY:** le frequenze empiriche non sono probabilità calibrate.

![SOL conditional successor corrente](scanner_forecast_SOL_conditional_successor_current.png)

###### Confronto diretto a 30 giorni

| Modello | Vintage | N | Target | P10 | P25 | P50 | P75 | P90 |
| --- | --- | ---: | --- | ---: | ---: | ---: | ---: | ---: |
| Cono standard | 2026-09-24 | 40 | 2026-10-24 | 77.07 $ | 93.26 $ | 115.80 $ | 141.86 $ | 194.70 $ |
| Conditional corrente | 2026-09-24 | 8 | 2026-10-24 | 92.29 $ | 97.96 $ | 144.44 $ | 185.20 $ | 247.54 $ |

###### Struttura successiva dei casi correnti

| Classe | Episodi | Frequenza empirica |
| --- | ---: | ---: |
| DIRECT_CONTINUATION | 4 | 50.00% |
| SHALLOW_PULLBACK_THEN_CONTINUATION | 1 | 12.50% |
| DEEP_PULLBACK_THEN_RECOVERY | 1 | 12.50% |
| FAILURE | 2 | 25.00% |
| UNRESOLVED | 0 | 0.00% |

###### Episodi qualificati oggi

| Asset | Match window | -5% hit | +10% anchor | Classe 60d |
| --- | --- | --- | --- | --- |
| THETA-USD | 2023-08-28 → 2023-12-05 | 2023-12-06 | 2023-12-24 | DIRECT_CONTINUATION |
| BTC-USD | 2022-11-11 → 2023-02-18 | 2023-02-24 | 2023-03-17 | DIRECT_CONTINUATION |
| RUNE-USD | 2023-06-11 → 2023-09-18 | 2023-09-21 | 2023-10-01 | FAILURE |
| RUNE-USD | 2020-04-02 → 2020-07-10 | 2020-07-13 | 2020-07-20 | DIRECT_CONTINUATION |
| HBAR-USD | 2020-11-09 → 2021-02-16 | 2021-02-23 | 2021-03-04 | DEEP_PULLBACK_THEN_RECOVERY |
| SNX-USD | 2019-02-01 → 2019-05-11 | 2019-05-12 | 2019-05-14 | DIRECT_CONTINUATION |
| 1INCH-USD | 2023-08-31 → 2023-12-08 | 2023-12-11 | 2023-12-26 | SHALLOW_PULLBACK_THEN_CONTINUATION |
| AVAX-USD | 2021-06-11 → 2021-09-18 | 2021-09-20 | 2021-09-23 | FAILURE |

##### B. Vintage originale 18 settembre — congelato

Questo invece **non cambia più**. Conserva gli 8 episodi / 6 asset della nostra analisi originale e serve per verificare fuori campione se quella specifica previsione descrive bene SOL.

Anchor della chat: circa **$112.70** il **2026-09-18**.

**SMALL SAMPLE · SENSITIVITY UNSTABLE · DIAGNOSTIC ONLY.**

![SOL conditional successor vintage](scanner_forecast_SOL_conditional_successor_vintage_20260918.png)

###### Percentili congelati a 30 giorni

| Modello | Vintage | N | Target | P10 | P25 | P50 | P75 | P90 |
| --- | --- | ---: | --- | ---: | ---: | ---: | ---: | ---: |
| Conditional vintage | 2026-09-18 | 8 | 2026-10-18 | 96.70 $ | 109.70 $ | 168.54 $ | 188.19 $ | 214.50 $ |

###### Verifica contro SOL reale

- Ultimo close disponibile: **2026-09-24** · SOL **115.32 $**.
- Giorno del vintage: **6/30**.
- P50 condizionato previsto per quel giorno: **106.79 $**.
- SOL reale: **DENTRO p10-p90** · **FUORI p25-p75**.

###### Parità con l'analisi originale

| Giorno | Mediana return riprodotta |
| ---: | ---: |
| 7 | -11.51% |
| 14 | 8.85% |
| 21 | 36.80% |
| 30 | 49.55% |

###### Gli 8 episodi congelati

| Asset | Match window | -5% hit | +10% anchor |
| --- | --- | --- | --- |
| BNB-USD | 2023-10-13 → 2024-01-20 | 2024-01-23 | 2024-02-15 |
| HBAR-USD | 2020-11-04 → 2021-02-11 | 2021-02-14 | 2021-02-18 |
| RUNE-USD | 2020-03-28 → 2020-07-05 | 2020-07-06 | 2020-07-20 |
| ETH-USD | 2020-05-11 → 2020-08-18 | 2020-08-21 | 2020-09-01 |
| ADA-USD | 2020-09-08 → 2020-12-16 | 2020-12-21 | 2020-12-29 |
| BCH-USD | 2019-01-17 → 2019-04-26 | 2019-04-29 | 2019-05-03 |
| RUNE-USD | 2023-06-01 → 2023-09-08 | 2023-09-11 | 2023-09-15 |
| HBAR-USD | 2024-09-04 → 2024-12-12 | 2024-12-18 | 2024-12-24 |

**Come leggere la differenza:** il cono standard risponde a "cosa hanno fatto i 40 casi più simili?". Il Conditional Successor risponde a una domanda più stretta: "tra quei casi, cosa è successo dopo che avevano già completato -5% → +10%?". Per questo il secondo può risultare più rialzista ma anche molto più fragile statisticamente.

I due modelli **non vengono mediati**, non sostituiscono l'uno l'altro e non modificano Global Confluence, segnali o decisioni.

<!-- SOL_CONDITIONAL_ANALYSES_END -->


#### Verifica storica e discrepanza

![Verifica storica cono SOL](scanner_forecast_history_SOL.png)

- Cono congelato il **2026-08-25**; verificato fino al **2026-09-24**; stato **COMPLETO 30/30g**.
- Reale **115,32 $**; p50 previsto **106,45 $**; scarto **8,34%**.
- Errore medio assoluto **4,04%**; massimo **13,65%**; DENTRO p10-p90; DENTRO p25-p75.

#### Cono regime-adjusted

Gruppo selezionato: **NONE**; fallback: **NONE**; motivo: **INSUFFICIENT_REGIME_MATCHES**.

Non disponibile: INSUFFICIENT_REGIME_MATCHES (campione selezionato 0/5 match).

### DOGE

![Scanner forecast DOGE](scanner_forecast_DOGE.png)

#### Verifica storica e discrepanza

![Verifica storica cono DOGE](scanner_forecast_history_DOGE.png)

- Cono congelato il **2026-08-25**; verificato fino al **2026-09-24**; stato **COMPLETO 30/30g**.
- Reale **0.09431 $**; p50 previsto **0.09433 $**; scarto **-0,02%**.
- Errore medio assoluto **9,77%**; massimo **16,74%**; DENTRO p10-p90; DENTRO p25-p75.

#### Cono regime-adjusted

Gruppo selezionato: **NONE**; fallback: **NONE**; motivo: **INSUFFICIENT_REGIME_MATCHES**.

Non disponibile: INSUFFICIENT_REGIME_MATCHES (campione selezionato 0/5 match).

## Accuratezza percorso scanner

| Asset   | Giorno   |   Controlli | Dentro p10-p90   | Dentro p25-p75   | Errore medio abs vs p50   | Errore medio vs p50   |
|:--------|:---------|------------:|:-----------------|:-----------------|:--------------------------|:----------------------|
| BTC | 1g | 69 | 92,75% | 66,67% | 2,08% | 0,54% |
| BTC | 3g | 65 | 92,31% | 73,85% | 3,29% | 0,97% |
| BTC | 7g | 61 | 91,80% | 68,85% | 4,98% | 2,23% |
| BTC | 14g | 47 | 97,87% | 72,34% | 5,59% | 3,25% |
| BTC | 30g | 23 | 100,00% | 91,30% | 8,90% | 3,16% |
| SOL | 1g | 69 | 81,16% | 59,42% | 2,85% | 1,07% |
| SOL | 3g | 65 | 90,77% | 70,77% | 4,23% | 1,92% |
| SOL | 7g | 61 | 90,16% | 70,49% | 5,92% | 4,02% |
| SOL | 14g | 47 | 85,11% | 72,34% | 8,11% | 7,10% |
| SOL | 30g | 23 | 91,30% | 47,83% | 15,48% | 14,92% |
| DOGE | 1g | 69 | 86,96% | 60,87% | 3,22% | 0,71% |
| DOGE | 3g | 65 | 90,77% | 64,62% | 4,86% | 1,85% |
| DOGE | 7g | 61 | 73,77% | 72,13% | 9,04% | 6,49% |
| DOGE | 14g | 47 | 85,11% | 53,19% | 10,45% | 8,66% |
| DOGE | 30g | 23 | 91,30% | 34,78% | 17,34% | 17,34% |

## Tail / outlier audit

I casi di coda restano nel calcolo. L'audit leave-one-out quantifica la sensibilità dei percentili senza trasformare l'analisi in un filtro discrezionale.

Dettaglio completo: [scanner_forecast_tail_outlier_audit.md](scanner_forecast_tail_outlier_audit.md).

## Calibratore shadow

Il cono ufficiale resta grezzo e invariato. Il calibratore usa soltanto previsioni passate già mature, campionate una volta a settimana per ridurre la falsa indipendenza. Ogni orizzonte si attiva a 30 controlli indipendenti: parte al 25% della correzione stimata e cresce gradualmente fino al 100% a 100 controlli.

| Asset   | Orizzonte   |   Controlli indipendenti |   Soglia | Stato                  | Forza correzione   | Shift p50   |   Scala p10-p90 |
|:--------|:------------|-------------------------:|---------:|:-----------------------|:-------------------|:------------|----------------:|
| BTC | 1g | 12 | 30 | RACCOLTA (18 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 3g | 11 | 30 | RACCOLTA (19 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 7g | 11 | 30 | RACCOLTA (19 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 14g | 10 | 30 | RACCOLTA (20 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 30g | 8 | 30 | RACCOLTA (22 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 1g | 12 | 30 | RACCOLTA (18 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 3g | 11 | 30 | RACCOLTA (19 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 7g | 11 | 30 | RACCOLTA (19 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 14g | 10 | 30 | RACCOLTA (20 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 30g | 8 | 30 | RACCOLTA (22 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 1g | 12 | 30 | RACCOLTA (18 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 3g | 11 | 30 | RACCOLTA (19 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 7g | 11 | 30 | RACCOLTA (19 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 14g | 10 | 30 | RACCOLTA (20 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 30g | 8 | 30 | RACCOLTA (22 mancanti) | 0,0% | 0,00% | 1,000 |

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

Generato: 2026-09-24 05:32 UTC

Questo report si attiva quando i casi positivi o negativi sono almeno **80%**.

Ora misura anche il **rialzo massimo prima della discesa principale**, quindi distingue uno spike iniziale da una discesa quasi immediata.

## Trigger estremi

| Asset   | Direzione   | Trigger   | Percentuale   | Motivo                           |   Match disponibili |
|:--------|:------------|:----------|:--------------|:---------------------------------|--------------------:|
| BTC     | NESSUNO     | NO        | +67,50%       | Nessun lato sopra soglia estrema |                  40 |
| SOL     | NESSUNO     | NO        | +50,00%       | Nessun lato sopra soglia estrema |                  40 |
| DOGE    | NESSUNO     | NO        | +70,00%       | Nessun lato sopra soglia estrema |                  40 |

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
- Casi positivi / salita storica: **67,50%**
- Casi negativi / discesa storica: **32,50%**
- Quanto è netto il segnale: **medio**
- Prezzo attuale: **84.183,64 $**
- Return normale fra 30 giorni: **91.351,82 $** (8,51%)
- Drawdown normale durante il mese: **80.448,24 $** (-4,44%)
- Drawdown brutto da rispettare: **69.854,72 $** (-17,02%)
- Max gain normale durante il mese: **103.936,38 $** (23,46%)
- Max gain buono / take profit ottimistico: **127.040,23 $** (50,91%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Solana
- Direzione più probabile a 30 giorni: **INCERTO**
- Casi positivi / salita storica: **50,00%**
- Casi negativi / discesa storica: **50,00%**
- Quanto è netto il segnale: **molto debole / quasi pari**
- Prezzo attuale: **115,45 $**
- Return normale fra 30 giorni: **115,80 $** (0,30%)
- Drawdown normale durante il mese: **98,63 $** (-14,57%)
- Drawdown brutto da rispettare: **84,41 $** (-26,89%)
- Max gain normale durante il mese: **131,84 $** (14,20%)
- Max gain buono / take profit ottimistico: **174,37 $** (51,03%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Dogecoin
- Direzione più probabile a 30 giorni: **DISCESA**
- Casi positivi / salita storica: **30,00%**
- Casi negativi / discesa storica: **70,00%**
- Quanto è netto il segnale: **forte**
- Prezzo attuale: **0,09 $**
- Return normale fra 30 giorni: **0,09 $** (-7,20%)
- Drawdown normale durante il mese: **0,07 $** (-22,77%)
- Drawdown brutto da rispettare: **0,07 $** (-30,42%)
- Max gain normale durante il mese: **0,10 $** (9,04%)
- Max gain buono / take profit ottimistico: **0,11 $** (20,78%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Messaggio del giorno

Il quadro generale oggi è misto. Alcuni asset possono avere lettura diversa, quindi è meglio valutare asset per asset.

---

# Mappa semplice asset per asset

# Bitcoin — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟢 VERDE / Favorevole
**Prezzo attuale:** 84.183,64 $

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

- Se va molto male: **65.845,78 $** (-21,78%)
- Se va male: **77.551,30 $** (-7,88%)
- Scenario normale: **91.351,82 $** (8,51%)
- Se va bene: **105.232,22 $** (25,00%)
- Se va molto bene: **138.820,39 $** (64,90%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **80.448,24 $** (-4,44%)
- Discesa brutta: **69.854,72 $** (-17,02%)
- Discesa molto brutta: **56.583,06 $** (-32,79%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **103.936,38 $** (23,46%)
- Rialzo buono: **127.040,23 $** (50,91%)
- Rialzo molto forte: **164.429,57 $** (95,32%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Bitcoin tendeva a muoversi tra una zona bassa intorno a **80.448,24 $** e uno spike normale intorno a **103.936,38 $**.

La chiusura a 30 giorni era più spesso positiva: salita 67,50%, discesa 32,50%. Quindi la lettura principale è favorevole.

Nota leva BTC: se la liquidazione è vicina a 51.000 $, guarda soprattutto la discesa brutta e molto brutta. Il prezzo può recuperare dopo, ma la leva può saltare prima.

---

# Solana — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟡 GIALLO / Incerto
**Prezzo attuale:** 115,45 $

**Direzione più probabile a 30 giorni:** **INCERTO**
- Probabilità storica di salita: **50,00%**
- Probabilità storica di discesa: **50,00%**
- Quanto è netto il segnale: **molto debole / quasi pari**

## Come leggere questa parte

- **Probabilità storica di salita** = su 40 casi simili, quanti hanno chiuso sopra dopo 30 giorni.
- **Probabilità storica di discesa** = su 40 casi simili, quanti hanno chiuso sotto dopo 30 giorni.
- **Quanto è netto il segnale** = quanto è grande la differenza tra salita e discesa. Non vuol dire certezza, vuol dire solo che il risultato storico non è vicino al 50/50.

La lettura principale è incerta, con segnale molto debole / quasi pari. Nei casi storici simili non c'è stato un vantaggio chiaro né per salita né per discesa.

## 1. Return 30d — prezzo fra 30 giorni

**Return** significa rendimento finale. Qui guardiamo dove potrebbe stare il prezzo **alla fine dei 30 giorni**, non durante il percorso.

- Se va molto male: **77,07 $** (-33,25%)
- Se va male: **93,26 $** (-19,22%)
- Scenario normale: **115,80 $** (0,30%)
- Se va bene: **141,86 $** (22,87%)
- Se va molto bene: **194,70 $** (68,64%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **98,63 $** (-14,57%)
- Discesa brutta: **84,41 $** (-26,89%)
- Discesa molto brutta: **74,85 $** (-35,17%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **131,84 $** (14,20%)
- Rialzo buono: **174,37 $** (51,03%)
- Rialzo molto forte: **208,69 $** (80,76%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Solana tendeva a muoversi tra una zona bassa intorno a **98,63 $** e uno spike normale intorno a **131,84 $**.

La chiusura a 30 giorni è incerta: salita 50,00%, discesa 50,00%. Non c'è un vantaggio netto.

---

# Dogecoin — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🔴 ROSSO / Prudenza
**Prezzo attuale:** 0,09 $

**Direzione più probabile a 30 giorni:** **DISCESA**
- Probabilità storica di salita: **30,00%**
- Probabilità storica di discesa: **70,00%**
- Quanto è netto il segnale: **forte**

## Come leggere questa parte

- **Probabilità storica di salita** = su 40 casi simili, quanti hanno chiuso sopra dopo 30 giorni.
- **Probabilità storica di discesa** = su 40 casi simili, quanti hanno chiuso sotto dopo 30 giorni.
- **Quanto è netto il segnale** = quanto è grande la differenza tra salita e discesa. Non vuol dire certezza, vuol dire solo che il risultato storico non è vicino al 50/50.

La lettura principale è ribassista, con segnale forte. Nei casi storici simili, il prezzo ha chiuso sotto dopo 30 giorni più spesso di quanto abbia chiuso sopra.

## 1. Return 30d — prezzo fra 30 giorni

**Return** significa rendimento finale. Qui guardiamo dove potrebbe stare il prezzo **alla fine dei 30 giorni**, non durante il percorso.

- Se va molto male: **0,04 $** (-58,52%)
- Se va male: **0,07 $** (-21,27%)
- Scenario normale: **0,09 $** (-7,20%)
- Se va bene: **0,10 $** (3,45%)
- Se va molto bene: **0,15 $** (55,15%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **0,07 $** (-22,77%)
- Discesa brutta: **0,07 $** (-30,42%)
- Discesa molto brutta: **0,04 $** (-61,13%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **0,10 $** (9,04%)
- Rialzo buono: **0,11 $** (20,78%)
- Rialzo molto forte: **0,15 $** (61,16%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Dogecoin tendeva a muoversi tra una zona bassa intorno a **0,07 $** e uno spike normale intorno a **0,10 $**.

La chiusura a 30 giorni era più spesso negativa: salita 30,00%, discesa 70,00%. Quindi la lettura principale è prudente/debole.

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

- Grezzo: **8,51%** → **91.351,82 $**
- Correzione imparata dagli errori: **2,01%**
- Calibrato: **10,52%** → **93.042,16 $**
- Lettura: Lo scanner è stato troppo pessimista sul prezzo finale.

### Drawdown 30d — rischio di discesa durante il mese

- Grezzo: **-4,44%** → **80.448,24 $**
- Correzione imparata dagli errori: **4,72%**
- Calibrato: **0,29%** → **84.424,50 $**
- Lettura: Lo scanner è stato troppo prudente: nella realtà il prezzo è sceso meno del previsto.

### Max gain 30d — rialzo/spike durante il mese

- Grezzo: **23,46%** → **103.936,38 $**
- Correzione imparata dagli errori: **-2,82%**
- Calibrato: **20,64%** → **101.558,26 $**
- Lettura: Lo scanner ha sovrastimato gli spike: nella realtà il prezzo è salito meno del previsto.

### Come leggerlo

La parte grezza ti dice cosa mostrano i vecchi pattern storici. La parte calibrata ti dice come cambia quella lettura dopo aver visto se lo scanner, nel mercato reale, è stato troppo ottimista o troppo pessimista.

## Solana

- Previsioni controllate: **30**
- Previsioni usate per la calibrazione recente: **30**
- Affidabilità direzionale storica: **alta**
- Direzione indovinata in passato: **100,00%**

### Confronto: grezzo vs autocalibrato

- Direzione grezza oggi: **INCERTO**
- Direzione calibrata oggi: **SALITA**

### Return 30d — prezzo finale fra 30 giorni

- Grezzo: **0,30%** → **115,80 $**
- Correzione imparata dagli errori: **8,80%**
- Calibrato: **9,10%** → **125,95 $**
- Lettura: Lo scanner è stato troppo pessimista sul prezzo finale.

### Drawdown 30d — rischio di discesa durante il mese

- Grezzo: **-14,57%** → **98,63 $**
- Correzione imparata dagli errori: **2,99%**
- Calibrato: **-11,58%** → **102,08 $**
- Lettura: Lo scanner è stato troppo prudente: nella realtà il prezzo è sceso meno del previsto.

### Max gain 30d — rialzo/spike durante il mese

- Grezzo: **14,20%** → **131,84 $**
- Correzione imparata dagli errori: **4,02%**
- Calibrato: **18,21%** → **136,48 $**
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

- Grezzo: **-7,20%** → **0,09 $**
- Correzione imparata dagli errori: **15,19%**
- Calibrato: **7,98%** → **0,10 $**
- Lettura: Lo scanner è stato troppo pessimista sul prezzo finale.

### Drawdown 30d — rischio di discesa durante il mese

- Grezzo: **-22,77%** → **0,07 $**
- Correzione imparata dagli errori: **15,34%**
- Calibrato: **-7,44%** → **0,09 $**
- Lettura: Lo scanner è stato troppo prudente: nella realtà il prezzo è sceso meno del previsto.

### Max gain 30d — rialzo/spike durante il mese

- Grezzo: **9,04%** → **0,10 $**
- Correzione imparata dagli errori: **2,52%**
- Calibrato: **11,56%** → **0,11 $**
- Lettura: Lo scanner ha sottostimato gli spike: nella realtà il prezzo è salito più del previsto.

### Come leggerlo

La parte grezza ti dice cosa mostrano i vecchi pattern storici. La parte calibrata ti dice come cambia quella lettura dopo aver visto se lo scanner, nel mercato reale, è stato troppo ottimista o troppo pessimista.

---

# Approfondimento tecnico — Bitcoin (BTC-USD)

## Semaforo: 🟢 VERDE / Favorevole

**Prezzo attuale:** 84.183,64 $

Bitcoin ha un segnale favorevole. La statistica dei casi simili indica più possibilità di salita che di discesa, ma resta comunque una probabilità, non una certezza.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **67,50%**
- Casi negativi dopo 30 giorni: **32,50%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **86,65%**
- Rendimento medio dopo 30 giorni: **15,37%**
- Rendimento centrale dopo 30 giorni: **8,51%**
- Discesa media durante i 30 giorni: **-10,90%**
- Massimo rialzo medio durante i 30 giorni: **37,36%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **97.124,66 $**
- Scenario centrale a 30 giorni: **91.351,82 $**
- Zona di rischio media: **75.010,58 $**
- Zona di rialzo media: **115.634,46 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -21,78% → **65.845,78 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -7,88% → **77.551,30 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: 8,51% → **91.351,82 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 25,00% → **105.232,22 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 64,90% → **138.820,39 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -32,79% → **56.583,06 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -17,02% → **69.854,72 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -4,44% → **80.448,24 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: 0,00% → **84.183,64 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: 0,00% → **84.183,64 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 0,53% → **84.628,38 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 8,05% → **90.963,16 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 23,46% → **103.936,38 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 50,91% → **127.040,23 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 95,32% → **164.429,57 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| BTC-USD         | 2022-11-11   | 2023-02-18 |        90.45 |        12.69 |         -18.08 |          13.79 |
| RUNE-USD        | 2023-06-06   | 2023-09-13 |        89.97 |         3.73 |           0    |          31.23 |
| INJ-USD         | 2023-08-21   | 2023-11-28 |        89.17 |       114.93 |           0    |         161.2  |
| DASH-USD        | 2020-09-13   | 2020-12-21 |        89.13 |        16.13 |         -16.67 |          42.17 |
| ALGO-USD        | 2023-08-28   | 2023-12-05 |        88.66 |        35.21 |          -0.54 |          56.22 |
| THETA-USD       | 2023-08-28   | 2023-12-05 |        88.42 |         9.3  |          -8.21 |          27.74 |
| XLM-USD         | 2020-09-18   | 2020-12-26 |        88.06 |        78.3  |         -13.08 |         131.76 |
| EGLD-USD        | 2023-08-29   | 2023-12-06 |        87.56 |        17.81 |           0    |          50.57 |
| ADA-USD         | 2023-08-29   | 2023-12-06 |        87.56 |        22.34 |           0    |          50.37 |
| ATOM-USD        | 2023-08-29   | 2023-12-06 |        87.46 |         5.85 |           0    |          23.72 |

---

# Approfondimento tecnico — Solana (SOL-USD)

## Semaforo: 🟡 GIALLO / Incerto

**Prezzo attuale:** 115,45 $

Solana è in una situazione incerta. Lo scanner non vede un vantaggio chiaro né per la salita né per la discesa. In questi casi è meglio non forzare la previsione.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **50,00%**
- Casi negativi dopo 30 giorni: **50,00%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **85,39%**
- Rendimento medio dopo 30 giorni: **13,87%**
- Rendimento centrale dopo 30 giorni: **0,30%**
- Discesa media durante i 30 giorni: **-16,53%**
- Massimo rialzo medio durante i 30 giorni: **39,23%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **131,46 $**
- Scenario centrale a 30 giorni: **115,80 $**
- Zona di rischio media: **96,36 $**
- Zona di rialzo media: **160,74 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -33,25% → **77,07 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -19,22% → **93,26 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: 0,30% → **115,80 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 22,87% → **141,86 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 68,64% → **194,70 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -35,17% → **74,85 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -26,89% → **84,41 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -14,57% → **98,63 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: 0,00% → **115,45 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: 0,00% → **115,45 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 0,00% → **115,45 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 0,83% → **116,41 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 14,20% → **131,84 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 51,03% → **174,37 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 80,76% → **208,69 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| CRV-USD         | 2022-11-11   | 2023-02-18 |        89.19 |       -23.26 |         -33.1  |           0.85 |
| AAVE-USD        | 2022-11-10   | 2023-02-17 |        87.97 |        -7.99 |         -22.1  |           6.22 |
| ATOM-USD        | 2023-08-29   | 2023-12-06 |        87.3  |         5.85 |           0    |          23.72 |
| THETA-USD       | 2023-08-28   | 2023-12-05 |        87.12 |         9.3  |          -8.21 |          27.74 |
| MKR-USD         | 2018-12-14   | 2019-03-23 |        86.97 |       -17.63 |         -18.11 |           6.91 |
| HBAR-USD        | 2022-11-09   | 2023-02-16 |        86.9  |       -25.52 |         -31.4  |           4.31 |
| BTC-USD         | 2022-11-11   | 2023-02-18 |        86.63 |        12.69 |         -18.08 |          13.79 |
| RUNE-USD        | 2023-06-11   | 2023-09-18 |        86.49 |       -15.88 |         -17.79 |          12.36 |
| EGLD-USD        | 2023-08-29   | 2023-12-06 |        86.45 |        17.81 |           0    |          50.57 |
| WAVES-USD       | 2023-08-29   | 2023-12-06 |        86.25 |        13.04 |          -2.25 |          31.88 |

---

# Approfondimento tecnico — Dogecoin (DOGE-USD)

## Semaforo: 🔴 ROSSO / Prudenza

**Prezzo attuale:** 0,09 $

Dogecoin richiede prudenza. La statistica dei casi simili indica più possibilità di discesa che di salita. Con leva, il rischio principale è il drawdown durante il percorso.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **30,00%**
- Casi negativi dopo 30 giorni: **70,00%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **80,75%**
- Rendimento medio dopo 30 giorni: **-1,57%**
- Rendimento centrale dopo 30 giorni: **-7,20%**
- Discesa media durante i 30 giorni: **-25,60%**
- Massimo rialzo medio durante i 30 giorni: **26,09%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **0,09 $**
- Scenario centrale a 30 giorni: **0,09 $**
- Zona di rischio media: **0,07 $**
- Zona di rialzo media: **0,12 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -58,52% → **0,04 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -21,27% → **0,07 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: -7,20% → **0,09 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 3,45% → **0,10 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 55,15% → **0,15 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -61,13% → **0,04 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -30,42% → **0,07 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -22,77% → **0,07 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -11,53% → **0,08 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: 0,00% → **0,09 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 0,00% → **0,09 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 3,43% → **0,10 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 9,04% → **0,10 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 20,78% → **0,11 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 61,16% → **0,15 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| DASH-USD        | 2019-11-08   | 2020-02-15 |        85.31 |       -64.76 |         -64.76 |           0    |
| RUNE-USD        | 2020-09-09   | 2020-12-17 |        84.84 |        97.38 |         -12.58 |          97.38 |
| MANA-USD        | 2022-11-07   | 2023-02-14 |        83.17 |       -14.97 |         -23.45 |           9.86 |
| FIL-USD         | 2020-12-06   | 2021-03-15 |        83.12 |       213.76 |           0    |         256.97 |
| SAND-USD        | 2021-05-05   | 2021-08-12 |        83.03 |        26.27 |          -8.4  |          58.13 |
| MKR-USD         | 2018-08-01   | 2018-11-08 |        82.7  |       -48.45 |         -51.77 |           5.23 |
| NEAR-USD        | 2022-11-07   | 2023-02-14 |        82.25 |       -12.29 |         -20.34 |          20.09 |
| BCH-USD         | 2019-11-08   | 2020-02-15 |        82.01 |       -60.99 |         -65.22 |           0    |
| ETH-USD         | 2025-03-06   | 2025-06-13 |        81.87 |        15.27 |         -13.62 |          15.27 |
| ENJ-USD         | 2022-11-12   | 2023-02-19 |        81.86 |       -15.2  |         -26.87 |          12.71 |

</details>
<!-- COMPACT_SECTION_END:scanner_full_detail -->

<!-- COMPACT_SECTION_START:market_regime -->
<details>
<summary><strong>🌦️ Market Regime Match</strong></summary>

<!-- MARKET_REGIME_MATCH_START -->
# Market Regime Match Report

Generated: 2026-09-24 05:31 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | snapshot_date   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD | 2026-09-24 | RECOVERY | 84.184 $ | True | 40.27% | -1.90% | RECOVERY | 40.27% | -1.90% |
| DOGE-USD | 2026-09-24 | RECOVERY | 0.09448 $ | True | 24.87% | -9.23% | RECOVERY | 40.27% | -1.90% |
| SOL-USD | 2026-09-24 | RECOVERY | 115,45 $ | True | 60.71% | -4.32% | RECOVERY | 40.27% | -1.90% |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD | ALL_MATCHES | 40 | 67.50% | 8.51% | 25.00% | 64.90% | -4.44% | -32.79% | 23.46% | 50.91% | 95.32% | 60.00% | 8.32% | 35.61% | 118.00% |
| BTC-USD | SAME_BTC_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| BTC-USD | SAME_ASSET_REGIME | 2 | 100.00% | 24.99% | 29.42% | 32.08% | -13.94% | -16.12% | 48.48% | 51.63% | 53.52% | 100.00% | 154.75% | 183.20% | 200.26% |
| BTC-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| DOGE-USD | ALL_MATCHES | 40 | 30.00% | -7.20% | 3.45% | 55.15% | -22.77% | -61.13% | 9.04% | 20.78% | 61.16% | 57.50% | 3.52% | 20.34% | 58.38% |
| DOGE-USD | SAME_BTC_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| DOGE-USD | SAME_ASSET_REGIME | 2 | 50.00% | 25.78% | 40.75% | 49.73% | -9.13% | -16.43% | 31.59% | 43.65% | 50.89% | 50.00% | 2.59% | 7.67% | 10.72% |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL-USD | ALL_MATCHES | 40 | 50.00% | 0.30% | 22.87% | 68.64% | -14.57% | -35.17% | 14.20% | 51.03% | 80.76% | 45.00% | -0.81% | 23.93% | 141.43% |
| SOL-USD | SAME_BTC_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| SOL-USD | SAME_ASSET_REGIME | 2 | 0.00% | -36.54% | -34.86% | -33.85% | -44.39% | -49.38% | 0.00% | 0.00% | 0.00% | 0.00% | -36.06% | -25.62% | -19.35% |
| SOL-USD | SAME_BTC_AND_ASSET_REGIME | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_BTC_BEAR | 24 | 66.67% | 10.99% | -3.65% | 42.51% | 54.17% | 3.64% | 56.21% |
| BTC-USD | HISTORICAL_BTC_BULL | 15 | 66.67% | 5.85% | -9.97% | 50.47% | 66.67% | 10.15% | 159.15% |
| BTC-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 100.00% | 14.06% | 0.00% | 92.34% | 100.00% | 10.26% | 92.34% |
| DOGE-USD | HISTORICAL_BTC_BEAR | 28 | 17.86% | -13.96% | -25.26% | 12.78% | 50.00% | -1.98% | 31.64% |
| DOGE-USD | HISTORICAL_BTC_BULL | 9 | 66.67% | 23.20% | -6.32% | 88.39% | 77.78% | 16.91% | 88.39% |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION | 3 | 33.33% | -2.17% | -25.24% | 8.41% | 66.67% | 0.79% | 42.74% |
| SOL-USD | HISTORICAL_BTC_BEAR | 22 | 45.45% | -4.23% | -18.09% | 36.44% | 36.36% | -5.11% | 54.97% |
| SOL-USD | HISTORICAL_BTC_BULL | 17 | 58.82% | 5.85% | -3.00% | 52.43% | 58.82% | 9.69% | 103.78% |
| SOL-USD | HISTORICAL_BTC_DISTRIBUTION | 1 | 0.00% | -11.89% | -21.59% | 0.76% | 0.00% | -28.06% | 0.76% |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD | HISTORICAL_ASSET_BEAR | 31 | 70.97% | 7.73% | -1.10% | 44.87% | 58.06% | 7.58% | 53.39% |
| BTC-USD | HISTORICAL_ASSET_BULL | 5 | 60.00% | 78.30% | -10.65% | 148.83% | 80.00% | 111.45% | 280.80% |
| BTC-USD | HISTORICAL_ASSET_DISTRIBUTION | 2 | 0.00% | -19.23% | -25.62% | 3.81% | 0.00% | -10.12% | 3.81% |
| BTC-USD | HISTORICAL_ASSET_RECOVERY | 2 | 100.00% | 24.99% | -13.94% | 51.63% | 100.00% | 154.75% | 185.40% |
| DOGE-USD | HISTORICAL_ASSET_BEAR | 27 | 18.52% | -14.25% | -25.24% | 17.77% | 48.15% | -5.35% | 26.51% |
| DOGE-USD | HISTORICAL_ASSET_BULL | 9 | 66.67% | 4.72% | -12.58% | 58.13% | 100.00% | 29.97% | 59.24% |
| DOGE-USD | HISTORICAL_ASSET_DISTRIBUTION | 1 | 0.00% | -47.71% | -51.80% | 0.00% | 0.00% | -33.65% | 0.00% |
| DOGE-USD | HISTORICAL_ASSET_MIXED | 1 | 0.00% | -49.55% | -68.95% | 4.40% | 0.00% | -65.63% | 4.40% |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY | 2 | 50.00% | 25.78% | -9.13% | 43.65% | 50.00% | 2.59% | 43.65% |
| SOL-USD | HISTORICAL_ASSET_BEAR | 32 | 50.00% | 0.30% | -14.57% | 41.49% | 40.62% | -2.87% | 52.50% |
| SOL-USD | HISTORICAL_ASSET_BULL | 3 | 66.67% | 7.79% | -5.54% | 64.30% | 100.00% | 9.69% | 78.10% |
| SOL-USD | HISTORICAL_ASSET_DISTRIBUTION | 3 | 66.67% | 17.79% | -12.33% | 65.42% | 66.67% | 56.67% | 151.04% |
| SOL-USD | HISTORICAL_ASSET_RECOVERY | 2 | 0.00% | -36.54% | -44.39% | 0.00% | 0.00% | -36.06% | 0.00% |

## Top regime-adjusted matches

A single cohort is selected deterministically: SAME_BTC_AND_ASSET_REGIME, otherwise SAME_ASSET_REGIME, otherwise SAME_BTC_REGIME. Each level must have at least 5 matches; cohorts are never combined.

| target   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level   | selection_reason            |
|:---------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:-----------------|:----------------------------|
| BTC-USD | NONE | 0 | 2 | 0 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES |
| DOGE-USD | NONE | 0 | 2 | 0 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES |
| SOL-USD | NONE | 0 | 2 | 0 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES |

_No data._

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

Generato: 2026-09-24 05:32 UTC

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
| BTC | 84.184 $ | +7 | COSTRUTTIVO / CONFERMA PARZIALE | STAGE 3 / DISTRIBUZIONE O PAUSA | MASSIMI E MINIMI DECRESCENTI | SIGN OF STRENGTH POSSIBILE | MEDIO | SPOT OK / LONG SOLO PRUDENTE SU CONFERMA |
| SOL | 115,45 $ | +9 | CONFERMATO RIALZISTA | STAGE 3 / DISTRIBUZIONE O PAUSA | MASSIMI E MINIMI DECRESCENTI | SIGN OF STRENGTH POSSIBILE | BASSO | TRANCHE PICCOLE / NO LEVA FINCHÉ NON ROMPE CONFERME |
| DOGE | 0.09448 $ | +5 | COSTRUTTIVO / CONFERMA PARZIALE | STAGE 3 / DISTRIBUZIONE O PAUSA | MASSIMI E MINIMI DECRESCENTI | SIGN OF STRENGTH POSSIBILE | MEDIO | SOLO TRADING VELOCE / NO LEVA AGGRESSIVA |

## Punteggi per area

| Asset | Trend | Struttura | Momentum | Volume | Prezzo | Candela | Wyckoff | Totale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +1 | -2 | +3 | 0 | +3 | 0 | +2 | +7 |
| SOL | +2 | -2 | +3 | +1 | +3 | 0 | +2 | +9 |
| DOGE | +1 | -2 | +3 | +1 | 0 | 0 | +2 | +5 |

## Livelli tecnici

| Asset | Supporto | Resistenza | Breakout 60g | Breakdown 60g | ATR14 | Rendimento 30g | Rendimento 90g |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 79.206 $ | 87.364 $ | 82.262 $ | 62.227 $ | 2,91% | 6,53% | 40,85% |
| SOL | 98,63 $ | 119,81 $ | 114,06 $ | 70,69 $ | 4,31% | 16,97% | 70,61% |
| DOGE | 0.08189 $ | 0.09998 $ | 0.09998 $ | 0.06797 $ | 5,35% | 4,89% | 26,10% |

## Lettura dettagliata

### BTC

- Prezzo: **84.184 $**
- Score classico: **+7 / 12**
- Verdetto: **COSTRUTTIVO / CONFERMA PARZIALE**
- Azione coerente: **SPOT OK / LONG SOLO PRUDENTE SU CONFERMA**
- Volatilità tecnica locale: **MEDIO** — ATR14 2,91%; distanza supporto 6,20%; distanza resistenza 3,86%

Dettaglio:

- Trend: **+1** — prezzo sopra MA200 daily; breve termine sopra MA20/MA50; MA50 daily in salita; MA200 daily in discesa; STAGE 3 / DISTRIBUZIONE O PAUSA
- Stage weekly: **STAGE 3 / DISTRIBUZIONE O PAUSA** — Prezzo sopra MA30 weekly ma pendenza debole o piatta.
- Struttura: **-2** — MASSIMI E MINIMI DECRESCENTI
- Momentum: **+3** — RSI sano 64.6; MACD sopra signal; istogramma MACD in miglioramento
- Volume: **0** — OBV sopra media; CMF neutrale 0.03; discesa con volume sopra media
- Conferma prezzo: **+3** — Breakout sopra resistenza 60g con volume.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **+2** — SIGN OF STRENGTH POSSIBILE. Prezzo nella parte alta del range con flusso volume positivo.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 64.60 |
| MACD histogram | 549.55782 |
| CMF20 | 0.030 |
| Volume ratio 20 | 1.49 |
| MA20 | 79.501 $ |
| MA50 | 74.527 $ |
| MA100 | 68.894 $ |
| MA200 | 70.758 $ |
| Pendenza MA50 20g | +8,86% |
| Pendenza MA200 60g | -2,08% |
| Bollinger width | 15,09% |
| Bollinger position | 0.86 |

### SOL

- Prezzo: **115,45 $**
- Score classico: **+9 / 12**
- Verdetto: **CONFERMATO RIALZISTA**
- Azione coerente: **TRANCHE PICCOLE / NO LEVA FINCHÉ NON ROMPE CONFERME**
- Volatilità tecnica locale: **BASSO** — ATR14 4,31%; distanza supporto 16,90%; distanza resistenza 3,92%

Dettaglio:

- Trend: **+2** — prezzo sopra MA200 daily; medie daily allineate rialziste; MA50 daily in salita; MA200 daily in discesa; STAGE 3 / DISTRIBUZIONE O PAUSA
- Stage weekly: **STAGE 3 / DISTRIBUZIONE O PAUSA** — Prezzo sopra MA30 weekly ma pendenza debole o piatta.
- Struttura: **-2** — MASSIMI E MINIMI DECRESCENTI
- Momentum: **+3** — RSI sano 64.3; MACD sopra signal; istogramma MACD in miglioramento
- Volume: **+1** — OBV sopra media; CMF positivo 0.18; discesa con volume sopra media
- Conferma prezzo: **+3** — Breakout sopra resistenza 60g con volume.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **+2** — SIGN OF STRENGTH POSSIBILE. Prezzo nella parte alta del range con flusso volume positivo.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 64.34 |
| MACD histogram | 1.06877 |
| CMF20 | 0.183 |
| Volume ratio 20 | 1.44 |
| MA20 | 105,47 $ |
| MA50 | 94,91 $ |
| MA100 | 84,96 $ |
| MA200 | 84,24 $ |
| Pendenza MA50 20g | +14,79% |
| Pendenza MA200 60g | -4,64% |
| Bollinger width | 23,19% |
| Bollinger position | 0.87 |

### DOGE

- Prezzo: **0.09448 $**
- Score classico: **+5 / 12**
- Verdetto: **COSTRUTTIVO / CONFERMA PARZIALE**
- Azione coerente: **SOLO TRADING VELOCE / NO LEVA AGGRESSIVA**
- Volatilità tecnica locale: **MEDIO** — ATR14 5,35%; distanza supporto 15,17%; distanza resistenza 6,01%

Dettaglio:

- Trend: **+1** — prezzo sopra MA200 daily; breve termine sopra MA20/MA50; MA50 daily in salita; MA200 daily in discesa; STAGE 3 / DISTRIBUZIONE O PAUSA
- Stage weekly: **STAGE 3 / DISTRIBUZIONE O PAUSA** — Prezzo sopra MA30 weekly ma pendenza debole o piatta.
- Struttura: **-2** — MASSIMI E MINIMI DECRESCENTI
- Momentum: **+3** — RSI sano 60.2; RSI in miglioramento; MACD sopra signal; istogramma MACD in miglioramento
- Volume: **+1** — OBV sopra media; CMF positivo 0.08; discesa con volume sopra media
- Conferma prezzo: **0** — Nessuna rottura confermata di prezzo.
- Candela: **0** — Nessuna candela forte
- Wyckoff: **+2** — SIGN OF STRENGTH POSSIBILE. Prezzo nella parte alta del range con flusso volume positivo.

Indicatori principali:

| Indicatore | Valore |
| --- | --- |
| RSI14 | 60.23 |
| MACD histogram | 0.00122 |
| CMF20 | 0.083 |
| Volume ratio 20 | 1.83 |
| MA20 | 0.08748 $ |
| MA50 | 0.08200 $ |
| MA100 | 0.07824 $ |
| MA200 | 0.08780 $ |
| Pendenza MA50 20g | +8,66% |
| Pendenza MA200 60g | -9,58% |
| Bollinger width | 24,06% |
| Bollinger position | 0.80 |

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

Generato: 2026-09-24 05:32 UTC

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
| BTC | 84.184 $ | Doppio minimo | ATTIVO | rialzista | 2026-09-21 | 89.580 $ | 26,26% | n/a | Fib 78,6% RECUPERATO (+1) @ 80.696 $ | BREAKOUT 60G | 76.248 $ |
| SOL | 115,45 $ | Triplo massimo | CANDIDATO | ribassista | n/a | 62,51 $ | n/a | 63,31% | Fib 78,6% RECUPERATO (+1) @ 107,08 $ | BREAKOUT 60G | 97,45 $ |
| DOGE | 0.09448 $ | Doppio minimo | ATTIVO | rialzista | 2026-09-21 | 0.11001 $ | 1,71% | n/a | Fib 78,6% TESTATO (0) @ 0.09536 $ | NEL RANGE | 0.09274 $ |

## BTC

![Classic visual BTC](classic_visual_BTC.png)

- Pattern principale: **Doppio minimo**
- Stato pattern: **ATTIVO** (+1)
- Famiglia: **rialzista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-09-02 -> 2026-09-15**
- Età formazione: **9 giorni**
- Breakout pattern: **2026-09-21**
- Età breakout: **3 giorni**
- Neckline: **82.262 $**
- Target teorico: **89.580 $**
- Progresso verso target: **26,26%**
- Distanza dalla neckline: **n/a**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 78,6% RECUPERATO (+1) @ 80.696 $** — Swing DOWN 2026-09-03 82.262 -> 2026-09-15 74.945; livello più vicino 78.6% a 80.696; stato RECUPERATO; confluenza: resistenza tecnica, neckline rialzista, invalidazione rialzista.
- Invalidazione: **80.617 $**
- Relazione prezzo/neckline: **sopra neckline**
- Dettaglio: Due minimi simili vicino a 74.945 tra 2026-09-02 e 2026-09-15. Neckline stimata: 82.262. Breakout neckline: 2026-09-21 (3 giorni fa). Stato: ATTIVO. Target teorico: 89.580; progresso corrente: 26,26%. Relazione prezzo/neckline: sopra neckline. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **BREAKOUT 60G**
- Supporto: **76.248 $**
- Resistenza: **87.364 $**
- Breakout 60g: **82.262 $**
- Breakdown 60g: **62.227 $**
- RSI14: **64.81**
- ATR14: **2,90%**
- Volume ratio 20g: **1.49**
- Rendimento 30g: **+6,61%**
- Rendimento 90g: **+40,96%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Doppio minimo | ATTIVO | +1 | rialzista | 82.262 $ | 2026-09-21 | 3g | 89.580 $ | 26,26% | n/a | 80.617 $ | Due minimi simili a 76.248 $ e 74.945 $. Neckline circa 82.262 $. Breakout neckline: 2026-09-21 (3 giorni fa). Stato: ATTIVO. Target teorico: 89.580 $; progresso: 26,26%; prezzo sopra neckline. |
| Doppio massimo | CANDIDATO | 0 | ribassista | 62.227 $ | n/a | n/a | 58.946 $ | n/a | 35,29% | 63.471 $ | Due massimi simili a 65.508 $ e 65.402 $. Neckline circa 62.227 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 46 giorni. |

## SOL

![Classic visual SOL](classic_visual_SOL.png)

- Pattern principale: **Triplo massimo**
- Stato pattern: **CANDIDATO** (0)
- Famiglia: **ribassista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-07-15 -> 2026-08-09**
- Età formazione: **46 giorni**
- Breakout pattern: **n/a**
- Età breakout: **n/a**
- Neckline: **70,69 $**
- Target teorico: **62,51 $**
- Progresso verso target: **n/a**
- Distanza dalla neckline: **63,31%**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 78,6% RECUPERATO (+1) @ 107,08 $** — Swing DOWN 2026-08-27 110,04 -> 2026-09-16 96,23; livello più vicino 78.6% a 107,08; stato RECUPERATO; confluenza: resistenza tecnica, neckline rialzista, invalidazione rialzista.
- Invalidazione: **72,11 $**
- Relazione prezzo/neckline: **sopra neckline**
- Dettaglio: Tre massimi simili vicino a 78,88 dal 2026-07-15 al 2026-08-09. Neckline ribassista stimata: 70,69. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 46 giorni. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **BREAKOUT 60G**
- Supporto: **97,45 $**
- Resistenza: **119,81 $**
- Breakout 60g: **114,06 $**
- Breakdown 60g: **70,69 $**
- RSI14: **64.58**
- ATR14: **4,31%**
- Volume ratio 20g: **1.44**
- Rendimento 30g: **+17,13%**
- Rendimento 90g: **+70,85%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Triplo massimo | CANDIDATO | 0 | ribassista | 70,69 $ | n/a | n/a | 62,51 $ | n/a | 63,31% | 72,11 $ | Tre massimi simili vicino a 78,88 dal 2026-07-15 al 2026-08-09. Neckline ribassista stimata: 70,69. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 46 giorni. Fonte lifecycle: technical_structure_metrics.csv. |
| Doppio massimo | CANDIDATO | 0 | ribassista | 70,69 $ | n/a | n/a | 62,66 $ | n/a | 63,31% | 72,11 $ | Due massimi simili a 78,73 $ e 77,62 $. Neckline circa 70,69 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 46 giorni. |
| Doppio minimo | TARGET RAGGIUNTO | 0 | rialzista | 107,12 $ | 2026-09-18 | 6g | 118,01 $ | 76,52% | n/a | 104,97 $ | Due minimi simili a 97,45 $ e 96,23 $. Neckline circa 107,12 $. Breakout neckline: 2026-09-18 (6 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 118,01 $; progresso: 76,52%; prezzo sopra neckline. |
| Testa e spalle inverso | TARGET RAGGIUNTO | 0 | rialzista | 78,17 $ | 2026-08-19 | 36g | 85,65 $ | 498,56% | n/a | 76,61 $ | Spalla sinistra 73,40 $, testa 70,69 $, spalla destra 74,20 $. Neckline circa 78,17 $. Breakout neckline: 2026-08-19 (36 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 85,65 $; progresso: 498,56%; prezzo sopra neckline. |

## DOGE

![Classic visual DOGE](classic_visual_DOGE.png)

- Pattern principale: **Doppio minimo**
- Stato pattern: **ATTIVO** (+1)
- Famiglia: **rialzista**
- Confidenza lifecycle: **TECHNICAL STRUCTURE**
- Formazione: **2026-09-02 -> 2026-09-16**
- Età formazione: **8 giorni**
- Breakout pattern: **2026-09-21**
- Età breakout: **3 giorni**
- Neckline: **0.09421 $**
- Target teorico: **0.11001 $**
- Progresso verso target: **1,71%**
- Distanza dalla neckline: **n/a**
- Fonte lifecycle: **technical_structure_metrics.csv**
- Fibonacci: **Fib 78,6% TESTATO (0) @ 0.09536 $** — Swing DOWN 2026-08-22 0.09998 -> 2026-09-16 0.07841; livello più vicino 78.6% a 0.09536; stato TESTATO; confluenza: neckline rialzista, invalidazione rialzista.
- Invalidazione: **0.09232 $**
- Relazione prezzo/neckline: **vicino alla neckline**
- Dettaglio: Due minimi simili vicino a 0.07841 tra 2026-09-02 e 2026-09-16. Neckline stimata: 0.09421. Breakout neckline: 2026-09-21 (3 giorni fa). Stato: ATTIVO. Target teorico: 0.11001; progresso corrente: 1,71%. Relazione prezzo/neckline: vicino alla neckline. Fonte lifecycle: technical_structure_metrics.csv.
- Candela più recente: **Nessuna candela forte**
- Stato prezzo: **NEL RANGE**
- Supporto: **0.09274 $**
- Resistenza: **0.09584 $**
- Breakout 60g: **0.09998 $**
- Breakdown 60g: **0.06797 $**
- RSI14: **60.49**
- ATR14: **5,34%**
- Volume ratio 20g: **1.83**
- Rendimento 30g: **+5,08%**
- Rendimento 90g: **+26,33%**

### Pattern trovati

| Pattern | Stato | Score | Famiglia | Neckline | Breakout | Età | Target | Progresso | Distanza neckline | Invalidazione | Dettaglio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Doppio minimo | ATTIVO | +1 | rialzista | 0.09421 $ | 2026-09-21 | 3g | 0.11001 $ | 1,71% | n/a | 0.09232 $ | Due minimi simili a 0.08028 $ e 0.07841 $. Neckline circa 0.09421 $. Breakout neckline: 2026-09-21 (3 giorni fa). Stato: ATTIVO. Target teorico: 0.11001 $; progresso: 1,71%; prezzo vicino alla neckline. |
| Doppio massimo | CANDIDATO | 0 | ribassista | 0.06797 $ | n/a | n/a | 0.04174 $ | n/a | 39,00% | 0.06933 $ | Due massimi simili a 0.09169 $ e 0.09421 $. Neckline circa 0.06797 $. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età formazione: 19 giorni. |

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

Generato: 2026-09-24 05:32 UTC

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-09-24**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-03-11**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **115,45 $**
- Verdetto principale: **STRUTTURA ANALOGA, PREZZO NON ADERENTE**
- Somiglianza strutturale: **+69,04%**
- Aderenza live principale: **+69,05%**
- Errore medio live principale: **15,48%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE NON CONFERMATO DAL PREZZO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **110**
- Osservazioni inclusive dal bottom: **111**
- Osservazioni da inizio programma/scanner: **84**
- Errore assoluto medio dal bottom: **13,18%**
- Errore assoluto medio da inizio programma: **15,48%**
- Gap firmato medio ultimi 7 giorni: **+36,80%**
- Errore assoluto medio ultimi 7 giorni: **36,80%**
- Gap ultimo giorno: **+42,05%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **+42,05%**
- Gap firmato medio 7g: **+36,80%**
- Errore assoluto medio 7g: **36,80%**
- Variazione recente gap: **+3,24%**
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
| 101 | 2026-09-15 | 2023-03-02 | 96,89 $ | 92,48 $ | +4,77% | da inizio programma |
| 102 | 2026-09-16 | 2023-03-03 | 98,64 $ | 88,09 $ | +11,98% | da inizio programma |
| 103 | 2026-09-17 | 2023-03-04 | 101,60 $ | 88,06 $ | +15,39% | da inizio programma |
| 104 | 2026-09-18 | 2023-03-05 | 112,60 $ | 88,38 $ | +27,41% | da inizio programma |
| 105 | 2026-09-19 | 2023-03-06 | 111,01 $ | 88,36 $ | +25,64% | da inizio programma |
| 106 | 2026-09-20 | 2023-03-07 | 111,13 $ | 87,53 $ | +26,97% | da inizio programma |
| 107 | 2026-09-21 | 2023-03-08 | 118,75 $ | 85,55 $ | +38,80% | da inizio programma |
| 108 | 2026-09-22 | 2023-03-09 | 118,51 $ | 80,21 $ | +47,74% | da inizio programma |
| 109 | 2026-09-23 | 2023-03-10 | 118,51 $ | 79,52 $ | +49,02% | da inizio programma |
| 110 | 2026-09-24 | 2023-03-11 | 115,45 $ | 81,28 $ | +42,05% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-10-01 | 106,22 $ | 150,89 $ | 115,45 $ / 153,45 $ | no | n/a | n/a | n/a |
| 14g | 2026-10-08 | 108,31 $ | 153,85 $ | 115,45 $ / 158,54 $ | no | n/a | n/a | n/a |
| 21g | 2026-10-15 | 111,92 $ | 158,98 $ | 115,45 $ / 159,35 $ | no | n/a | n/a | n/a |
| 28g | 2026-10-22 | 110,09 $ | 156,38 $ | 115,45 $ / 159,35 $ | no | n/a | n/a | n/a |
| 35g | 2026-10-29 | 119,43 $ | 169,65 $ | 115,45 $ / 170,58 $ | no | n/a | n/a | n/a |
| 42g | 2026-11-05 | 109,58 $ | 155,65 $ | 115,45 $ / 170,58 $ | no | n/a | n/a | n/a |
| 49g | 2026-11-12 | 115,22 $ | 163,66 $ | 115,45 $ / 170,58 $ | no | n/a | n/a | n/a |
| 56g | 2026-11-19 | 113,86 $ | 161,74 $ | 115,45 $ / 170,58 $ | no | n/a | n/a | n/a |
| 63g | 2026-11-26 | 105,51 $ | 149,87 $ | 115,45 $ / 170,58 $ | no | n/a | n/a | n/a |
| 70g | 2026-12-03 | 106,87 $ | 151,81 $ | 115,45 $ / 170,58 $ | no | n/a | n/a | n/a |
| 77g | 2026-12-10 | 105,84 $ | 150,34 $ | 115,45 $ / 170,58 $ | no | n/a | n/a | n/a |
| 84g | 2026-12-17 | 106,66 $ | 151,50 $ | 115,45 $ / 170,58 $ | no | n/a | n/a | n/a |
| 91g | 2026-12-24 | 101,83 $ | 144,65 $ | 115,45 $ / 170,58 $ | no | n/a | n/a | n/a |
| 98g | 2026-12-31 | 104,43 $ | 148,34 $ | 115,45 $ / 170,58 $ | no | n/a | n/a | n/a |
| 105g | 2027-01-07 | 120,34 $ | 170,94 $ | 115,45 $ / 171,76 $ | no | n/a | n/a | n/a |
| 112g | 2027-01-14 | 120,50 $ | 171,17 $ | 115,45 $ / 171,76 $ | no | n/a | n/a | n/a |
| 119g | 2027-01-21 | 119,33 $ | 169,50 $ | 115,45 $ / 174,34 $ | no | n/a | n/a | n/a |
| 126g | 2027-01-28 | 119,34 $ | 169,52 $ | 115,45 $ / 176,13 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 70 | 35,71% | 11,41% | 14,97% |
| 14g | 63 | 23,81% | 17,64% | 14,31% |
| 21g | 56 | 23,21% | 24,10% | 15,84% |
| 28g | 49 | 22,45% | 26,63% | 16,01% |
| 35g | 42 | 30,95% | 27,06% | 15,76% |
| 42g | 35 | 57,14% | 19,63% | 14,09% |
| 49g | 30 | 66,67% | 18,81% | 16,99% |
| 56g | 23 | 69,57% | 14,81% | 18,53% |
| 63g | 16 | 68,75% | 11,66% | 23,49% |
| 70g | 9 | 55,56% | 13,54% | 36,80% |
| 77g | 2 | 0,00% | 20,93% | n/a |
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

<!-- RSI_MULTI_TIMEFRAME_DIVERGENCE_START -->
# Divergenze RSI multi-timeframe — diagnostica

Generato: 2026-09-24 05:32 UTC

Il modulo confronta prezzo e RSI 14 sui pivot confermati **daily e weekly**. Riconosce divergenze regolari e nascoste, segnali in formazione, invalidazioni e semplice conferma del momentum.

**Peso operativo: 0.** Non modifica il Global Confluence, non cambia le soglie del Paper Trading e non apre né blocca operazioni. I risultati vengono misurati prima di qualsiasi futura decisione sul peso.

## Sintesi corrente

| Asset   | Daily              | Stato D   | Weekly             | Stato W    | Lettura weekly                                                                                                              |   Peso |
|:--------|:-------------------|:----------|:-------------------|:-----------|:----------------------------------------------------------------------------------------------------------------------------|-------:|
| BTC     | Conferma rialzista | CONTESTO  | Conferma rialzista | CONTESTO   | Prezzo e RSI stanno salendo insieme: momentum rialzista confermato.                                                         |      0 |
| SOL     | Conferma rialzista | CONTESTO  | Conferma rialzista | CONTESTO   | Prezzo e RSI stanno salendo insieme: momentum rialzista confermato.                                                         |      0 |
| DOGE    | Conferma rialzista | CONTESTO  | Hidden bearish     | CONFERMATA | Hidden bearish confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto. |      0 |

## Dettaglio dei pivot

| Asset   | TF   | Tipo               | Stato      | Prezzo / RSI      | Pivot confrontati                                                   | Δ prezzo contesto   | Δ RSI contesto   |   Peso |
|:--------|:-----|:-------------------|:-----------|:------------------|:--------------------------------------------------------------------|:--------------------|:-----------------|-------:|
| BTC     | 1D   | Conferma rialzista | CONTESTO   | 84.131 $ / 64,64  | n/a                                                                 | +7,50%              | 5,27             |      0 |
| BTC     | 1W   | Conferma rialzista | CONTESTO   | 84.131 $ / 61,28  | n/a                                                                 | +33,93%             | 22,48            |      0 |
| SOL     | 1D   | Conferma rialzista | CONTESTO   | 115,34 $ / 64,41  | n/a                                                                 | +13,51%             | 5,72             |      0 |
| SOL     | 1W   | Conferma rialzista | CONTESTO   | 115,34 $ / 62,86  | n/a                                                                 | +54,74%             | 23,15            |      0 |
| DOGE    | 1D   | Conferma rialzista | CONTESTO   | 0.09429 $ / 60,20 | n/a                                                                 | +9,43%              | 5,93             |      0 |
| DOGE    | 1W   | Hidden bearish     | CONFERMATA | 0.09429 $ / 51,25 | 2026-05-17 0.11825 $ / RSI 44,25 → 2026-08-23 0.09998 $ / RSI 49,72 | n/a                 | n/a              |      0 |

### BTC

- **1D — Conferma rialzista / CONTESTO**: Prezzo e RSI stanno salendo insieme: momentum rialzista confermato.
- **1W — Conferma rialzista / CONTESTO**: Prezzo e RSI stanno salendo insieme: momentum rialzista confermato.

### SOL

- **1D — Conferma rialzista / CONTESTO**: Prezzo e RSI stanno salendo insieme: momentum rialzista confermato.
- **1W — Conferma rialzista / CONTESTO**: Prezzo e RSI stanno salendo insieme: momentum rialzista confermato.

### DOGE

- **1D — Conferma rialzista / CONTESTO**: Prezzo e RSI stanno salendo insieme: momentum rialzista confermato.
- **1W — Hidden bearish / CONFERMATA**: Hidden bearish confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto.

## Tracker live delle divergenze confermate

Viene salvato un solo evento per combinazione di asset, timeframe, tipo e coppia di pivot. Gli esiti vengono controllati dopo 30, 60, 90 e 180 giorni.

- Eventi indipendenti salvati: **9**.
- Soglie di lettura: **30 / 60 / 100 controlli**.
- Anche oltre le soglie il peso resta **0** finché non viene presa una decisione esplicita.

| Asset   | TF   | Tipo             |   Orizzonte |   Controlli | Accuratezza   | Return corretto   | Stato         |   Peso |
|:--------|:-----|:-----------------|------------:|------------:|:--------------|:------------------|:--------------|-------:|
| BTC     | 1D   | Bullish regolare |          30 |           1 | 0,00%         | -1,52%            | RACCOLTA DATI |      0 |
| BTC     | 1D   | Bullish regolare |          60 |           1 | +100,00%      | +21,03%           | RACCOLTA DATI |      0 |
| BTC     | 1D   | Hidden bearish   |          30 |           1 | 0,00%         | -1,37%            | RACCOLTA DATI |      0 |
| BTC     | 1D   | Hidden bearish   |          60 |           1 | 0,00%         | -23,44%           | RACCOLTA DATI |      0 |
| BTC     | 1D   | Hidden bullish   |          30 |           1 | +100,00%      | +25,83%           | RACCOLTA DATI |      0 |
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

<!-- COMPACT_SECTION_START:exchange_microstructure -->
<details>
<summary><strong>🏦 Dati exchange, liquidità e leva</strong></summary>

<!-- EXCHANGE_MICROSTRUCTURE_START -->
# Dati exchange, liquidità e leva

Generato: 2026-09-24 05:32 UTC

Questo modulo legge Kraken Futures, Bitget Futures e KuCoin Futures come nucleo derivati. OKX e Coinbase vengono raccolti come fonti ausiliarie non pesate.
Non modifica la formula matematica di RSI, Fibonacci o Wyckoff: controlla se quei segnali sono sostenuti da acquisti, vendite, OI, funding e liquidità.

**Limite importante:** questo nucleo non assume disponibile un feed pubblico completo delle liquidazioni. La componente liquidazioni resta neutrale; le zone future restano stime di pressione, non dati certi delle singole posizioni.

Diagnostica completa: [exchange_source_diagnostics.md](exchange_source_diagnostics.md)

## Sintesi

| Asset | Prezzo | Exchange | Segnale candidato | Peso Global | Bias exchange | Confidenza | Copertura | Funding 8h eq. | OI 24h | Taker flow (campione/4h) | Book 0,5% | Liq long campione | Liq short campione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 84.264 $ | 3 | +1 | 0 | POSITIVA / CANDIDATA, ANCORA NON PESATA | MEDIA | 100% | +0,0061% | -8,96% | 1,59 | +0,80% | 0 $ | 0 $ |
| SOL | 115,86 $ | 3 | 0 | 0 | LEGGERMENTE POSITIVA / NON PESATA | BASSA | 100% | -0,0019% | -4,25% | 0,99 | -0,25% | 0 $ | 0 $ |
| DOGE | 0.09480 $ | 3 | 0 | 0 | LEGGERMENTE POSITIVA / NON PESATA | BASSA | 100% | +0,0078% | -4,76% | 2,24 | -3,20% | 0 $ | 0 $ |

Il segnale candidato è limitato a **±1**, ma il peso nel Global resta **0** finché il tracker a 7 giorni non raggiunge 30 controlli, almeno 55% di accuratezza e return corretto direzione positivo. Un singolo muro o funding non basta.

La colonna taker usa un campione recente nel primo run. Dopo almeno 3 fotografie distribuite su almeno 45 minuti viene sostituita automaticamente dalla media intraday 4h.

## Dati separati per exchange

| Asset | Exchange | Stato | Funding 8h eq. | Open interest | Taker flow | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | Kraken | OK | +0,0035% | 188,29 mln $ | 2,03 | -2,12% |
| BTC | Bitget | OK | +0,0072% | 2,77 mld $ | 5,63 | +44,04% |
| BTC | Kucoin | OK | +0,0011% | 894,21 mln $ | 0,15 | -2,28% |
| SOL | Kraken | OK | +0,0119% | 31,39 mln $ | 315,42 | -7,19% |
| SOL | Bitget | OK | +0,0020% | 459,04 mln $ | 0,44 | -1,04% |
| SOL | Kucoin | OK | +0,0033% | 133,25 mln $ | 0,59 | -13,04% |
| DOGE | Kraken | OK | +0,0143% | 5,66 mln $ | 0,55 | -2,79% |
| DOGE | Bitget | OK | +0,0082% | 121,88 mln $ | 3,29 | -5,69% |
| DOGE | Kucoin | OK | +0,0100% | 68,22 mln $ | 2,88 | +9,62% |

Kraken, Bitget e KuCoin contribuiscono a funding normalizzato, open interest, trade aggressivi e order book. Non viene inventato un long/short ratio pubblico né un feed completo delle liquidazioni.

## Conferme per indicatori tecnici

### BTC

- Score grezzo exchange: **+2,75**; candidato: **+1**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 5, accuratezza +40,00%.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 1, bear 0, divergenze 0.
- Flusso taker/order book: **+1,75**.
- OI/funding/basis: **+0,50**.
- Affollamento long/short: **+0,00**.
- Liquidazioni: **NON PESATE / FEED COMPLETO NON ASSUNTO DISPONIBILE**.
- **Wyckoff:** Fase Wyckoff non abbastanza chiara per una conferma exchange.
- **Fibonacci:** Fibonacci recuperato con acquisti/assorbimento coerenti: conferma positiva. Confluenza tecnica dichiarata: resistenza tecnica, neckline rialzista, invalidazione rialzista.
- **RSI:** RSI in zona non estrema o flusso exchange non abbastanza netto.
- **Pattern:** Doppio minimo attivo sostenuto dal flusso exchange.
- **Breakout/breakdown:** Prezzo non abbastanza vicino a un livello chiave o flusso non netto.
- **Mappa liquidità attuale:** muro bid: n/a; muro ask: n/a

![Microstruttura exchange BTC](exchange_microstructure_BTC.png)

### SOL

- Score grezzo exchange: **+1,50**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 5, accuratezza +60,00%.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 0, bear 2, divergenze 0.
- Flusso taker/order book: **+0,75**.
- OI/funding/basis: **+0,50**.
- Affollamento long/short: **+0,00**.
- Liquidazioni: **NON PESATE / FEED COMPLETO NON ASSUNTO DISPONIBILE**.
- **Wyckoff:** Fase Wyckoff non abbastanza chiara per una conferma exchange.
- **Fibonacci:** Fibonacci recuperato con acquisti/assorbimento coerenti: conferma positiva. Confluenza tecnica dichiarata: resistenza tecnica, neckline rialzista, invalidazione rialzista.
- **RSI:** RSI in zona non estrema o flusso exchange non abbastanza netto.
- **Pattern:** I pattern candidati restano non operativi: i dati exchange possono solo preparare la conferma.
- **Breakout/breakdown:** Prezzo non abbastanza vicino a un livello chiave o flusso non netto.
- **Mappa liquidità attuale:** muro bid: n/a; muro ask: n/a

![Microstruttura exchange SOL](exchange_microstructure_SOL.png)

### DOGE

- Score grezzo exchange: **+2,50**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 9, accuratezza +44,44%.
- Fonti disponibili: Kraken **SI**, Bitget **SI**, KuCoin **SI**.
- Consenso multi-exchange: bull 1, bear 1, divergenze 1.
- Flusso taker/order book: **+1,75**.
- OI/funding/basis: **+0,50**.
- Affollamento long/short: **+0,00**.
- Liquidazioni: **NON PESATE / FEED COMPLETO NON ASSUNTO DISPONIBILE**.
- **Wyckoff:** Fase Wyckoff non abbastanza chiara per una conferma exchange.
- **Fibonacci:** Livello Fibonacci soltanto testato: order book e taker flow non bastano ancora per dichiararlo tenuto o perso. Confluenza tecnica dichiarata: neckline rialzista, invalidazione rialzista.
- **RSI:** RSI in zona non estrema o flusso exchange non abbastanza netto.
- **Pattern:** Doppio minimo attivo sostenuto dal flusso exchange.
- **Breakout/breakdown:** Prezzo non abbastanza vicino a un livello chiave o flusso non netto.
- **Mappa liquidità attuale:** muro bid: n/a; muro ask: n/a

![Microstruttura exchange DOGE](exchange_microstructure_DOGE.png)

## Overlay sulle previsioni a 30 giorni

La previsione storica grezza dello scanner resta intatta. L'overlay exchange può correggerla solo dopo almeno 30 controlli maturati a 30 giorni e solo se il modulo dimostra accuratezza direzionale almeno del 55%.

| Asset | Prob. grezza salita | Return p50 grezzo | Controlli 30g | Accuratezza exchange | Stato overlay | Peso | Prob. corretta | Return corretto |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +67,50% | +8,51% | 2 | +50,00% | RACCOLTA DATI | 0,00 | +67,50% | +8,51% |
| SOL | +50,00% | +0,30% | 3 | +100,00% | RACCOLTA DATI | 0,00 | +50,00% | +0,30% |
| DOGE | +30,00% | -7,20% | 7 | +71,43% | RACCOLTA DATI | 0,00 | +30,00% | -7,20% |

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

<!-- COMPACT_SECTION_START:technical_structure -->
<details>
<summary><strong>🧱 Struttura tecnica completa e Fibonacci</strong></summary>

<!-- TECHNICAL_STRUCTURE_START -->
# Report struttura tecnica

Generato: 2026-09-24 05:32 UTC

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

| Asset   | Prezzo   |   Punteggio | Verdetto          | Trend           | Momentum                  | Struttura                                             |   Pattern score | Fibonacci       | Pattern rialzista                | Pattern ribassista         | Supporto   | Resistenza   |
|:--------|:---------|------------:|:------------------|:----------------|:--------------------------|:------------------------------------------------------|----------------:|:----------------|:---------------------------------|:---------------------------|:-----------|:-------------|
| BTC | 84.184 $ | 10 | RIALZISTA TECNICO | Trend rialzista | Momentum in miglioramento | Volatilità in espansione | +1 | +1 / RECUPERATO | Doppio minimo / ATTIVO | Doppio massimo / CANDIDATO | 74.945 | 82.262 |
| SOL | 115,45 $ | 7 | RIALZISTA TECNICO | Trend rialzista | Momentum in miglioramento | Struttura ribassista con massimi e minimi decrescenti | 0 | +1 / RECUPERATO | Doppio minimo / TARGET RAGGIUNTO | Triplo massimo / CANDIDATO | 96,23 | 107,12 |
| DOGE | 0.09448 $ | 8 | RIALZISTA TECNICO | Trend rialzista | Momentum in miglioramento | Struttura ribassista con massimi e minimi decrescenti | +1 | 0 / TESTATO | Doppio minimo / ATTIVO | Doppio massimo / CANDIDATO | 0.07841 | 0.09998 |

## Riepilogo ciclo di vita pattern

| Asset   | Doppio minimo    | Triplo minimo    | Adam/Eve Bottom                        | Doppio massimo   | Triplo massimo   | Adam/Eve Top                 |   Punteggio pattern |
|:--------|:-----------------|:-----------------|:---------------------------------------|:-----------------|:-----------------|:-----------------------------|--------------------:|
| BTC | ATTIVO | TARGET RAGGIUNTO | Eve and Adam Bottom — ATTIVO | CANDIDATO | CANDIDATO | ASSENTE | 1 |
| SOL | TARGET RAGGIUNTO | TARGET RAGGIUNTO | Adam and Eve Bottom — TARGET RAGGIUNTO | INVALIDATO | CANDIDATO | Adam and Eve Top — CANDIDATO | 0 |
| DOGE | ATTIVO | TARGET RAGGIUNTO | Adam and Eve Bottom — ATTIVO | CANDIDATO | CANDIDATO | Adam and Eve Top — CANDIDATO | 1 |

## Indicatori tecnici

| Asset   |   RSI 14 |   Istogramma MACD | MA20    | MA50    | MA200   | Pendenza MA50 20g   | Pendenza MA200 60g   | Rendimento 30g   | Rendimento 90g   |
|:--------|---------:|------------------:|:--------|:--------|:--------|:--------------------|:---------------------|:-----------------|:-----------------|
| BTC | 64.81 | 553.662 | 79.504 | 74.528 | 70.758 | 8,36% | -1,90% | 7,15% | 40,27% |
| SOL | 64.58 | 1.07898 | 105,48 | 94,91 | 84,24 | 14,06% | -4,32% | 19,51% | 60,71% |
| DOGE | 60.49 | 0.00123 | 0.08749 | 0.08200 | 0.08780 | 8,31% | -9,23% | 10,22% | 24,87% |

## Dettaglio asset

### BTC

- Prezzo: **84.184 $**
- Punteggio tecnico: **10 / 12**
- Verdetto: **RIALZISTA TECNICO**
- Trend: **Trend rialzista** (3)
- Momentum: **Momentum in miglioramento** (3)
- Volume: **Volume neutrale** (0)
- Struttura: **Volatilità in espansione** (0)
  - Dettaglio struttura: Ultimi minimi: 7.625e+04 -> 7.494e+04. Ultimi massimi: 8.135e+04 -> 8.226e+04.
- Divergenza: **Nessuna** (0)
- Fase Wyckoff candidata: **Markup / fase rialzista** (2)
  - Dettaglio Wyckoff: Prezzo sopra MA200, MA50 in salita e trend a 30 giorni positivo.
- Fibonacci automatico: **RECUPERATO** (+1)
  - Swing DOWN 2026-09-03 82.262 -> 2026-09-15 74.945; livello più vicino 78.6% a 80.696; stato RECUPERATO; confluenza: resistenza tecnica, neckline rialzista, invalidazione rialzista.
- Punteggio pattern: **+1**
  - rialzista dominante: Doppio minimo (ATTIVO, +1); ribassista dominante: Doppio massimo (CANDIDATO, 0).
- Supporto più vicino: **74.945**
- Resistenza più vicina: **82.262**

Pattern classici e ciclo di vita:

- Doppio minimo: **ATTIVO** (+1)
  - Due minimi simili vicino a 74.945 tra 2026-09-02 e 2026-09-15. Neckline stimata: 82.262. Breakout neckline: 2026-09-21 (3 giorni fa). Stato: ATTIVO. Target teorico: 89.580; progresso corrente: 26,26%. Relazione prezzo/neckline: sopra neckline.
  - neckline 82.262; target 89.580; breakout 2026-09-21 (3g); progresso 26,26%; prezzo sopra neckline.
- Triplo minimo: **TARGET RAGGIUNTO** (0)
  - Tre minimi simili vicino a 62.201 dal 2026-06-18 al 2026-08-14. Neckline stimata: 66.910. Breakout neckline: 2026-08-19 (36 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 71.619; progresso corrente: 366,83%. Relazione prezzo/neckline: sopra neckline.
  - neckline 66.910; target 71.619; breakout 2026-08-19 (36g); progresso 366,83%; prezzo sopra neckline.
- Eve and Adam Bottom: **ATTIVO** (+1)
  - Pattern Eve and Adam Bottom vicino a 74.945 dal 2026-09-02 al 2026-09-15. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 82.262. Breakout neckline: 2026-09-21 (3 giorni fa). Stato: ATTIVO. Target teorico: 89.580; progresso corrente: 26,26%. Relazione prezzo/neckline: sopra neckline.
  - neckline 82.262; target 89.580; breakout 2026-09-21 (3g); progresso 26,26%; prezzo sopra neckline.
- Doppio massimo: **CANDIDATO** (0)
  - Due massimi simili vicino a 65.508 tra 2026-07-15 e 2026-08-09. Neckline ribassista stimata: 62.227. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 46 giorni.
  - neckline 62.227; target 58.946; distanza dalla neckline 35,29%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 65.544 dal 2026-06-22 al 2026-08-09. Neckline ribassista stimata: 57.748. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 46 giorni.
  - neckline 57.748; target 49.952; distanza dalla neckline 45,78%; prezzo sopra neckline.
- Adam/Eve Top: **ASSENTE** (0)

### SOL

- Prezzo: **115,45 $**
- Punteggio tecnico: **7 / 12**
- Verdetto: **RIALZISTA TECNICO**
- Trend: **Trend rialzista** (3)
- Momentum: **Momentum in miglioramento** (2)
- Volume: **Volume da accumulazione** (1)
- Struttura: **Struttura ribassista con massimi e minimi decrescenti** (-2)
  - Dettaglio struttura: Ultimi minimi: 97.45 -> 96.23. Ultimi massimi: 110 -> 107.1.
- Divergenza: **Nessuna** (0)
- Fase Wyckoff candidata: **Markup / fase rialzista** (2)
  - Dettaglio Wyckoff: Prezzo sopra MA200, MA50 in salita e trend a 30 giorni positivo.
- Fibonacci automatico: **RECUPERATO** (+1)
  - Swing DOWN 2026-08-27 110,04 -> 2026-09-16 96,23; livello più vicino 78.6% a 107,08; stato RECUPERATO; confluenza: resistenza tecnica, neckline rialzista, invalidazione rialzista.
- Punteggio pattern: **0**
  - rialzista dominante: Doppio minimo (TARGET RAGGIUNTO, 0); ribassista dominante: Triplo massimo (CANDIDATO, 0).
- Supporto più vicino: **96,23**
- Resistenza più vicina: **107,12**

Pattern classici e ciclo di vita:

- Doppio minimo: **TARGET RAGGIUNTO** (0)
  - Due minimi simili vicino a 96,23 tra 2026-09-02 e 2026-09-16. Neckline stimata: 107,12. Breakout neckline: 2026-09-18 (6 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 118,01; progresso corrente: 76,52%. Relazione prezzo/neckline: sopra neckline.
  - neckline 107,12; target 118,01; breakout 2026-09-18 (6g); progresso 76,52%; prezzo sopra neckline.
- Triplo minimo: **TARGET RAGGIUNTO** (0)
  - Tre minimi simili vicino a 70,69 dal 2026-07-17 al 2026-08-16. Neckline stimata: 78,73. Breakout neckline: 2026-08-19 (36 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 86,76; progresso corrente: 457,24%. Relazione prezzo/neckline: sopra neckline.
  - neckline 78,73; target 86,76; breakout 2026-08-19 (36g); progresso 457,24%; prezzo sopra neckline.
- Adam and Eve Bottom: **TARGET RAGGIUNTO** (0)
  - Pattern Adam and Eve Bottom vicino a 96,23 dal 2026-09-02 al 2026-09-16. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 107,12. Breakout neckline: 2026-09-18 (6 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 118,01; progresso corrente: 76,52%. Relazione prezzo/neckline: sopra neckline.
  - neckline 107,12; target 118,01; breakout 2026-09-18 (6g); progresso 76,52%; prezzo sopra neckline.
- Doppio massimo: **INVALIDATO** (0)
  - Due massimi simili vicino a 110,04 tra 2026-08-27 e 2026-09-06. Neckline ribassista stimata: 97,45. Breakout neckline: 2026-09-15 (9 giorni fa). Stato: INVALIDATO. Target teorico: 84,86; progresso corrente: -142,98%. Relazione prezzo/neckline: sopra neckline.
  - neckline 97,45; target 84,86; breakout 2026-09-15 (9g); progresso -142,98%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 78,88 dal 2026-07-15 al 2026-08-09. Neckline ribassista stimata: 70,69. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 46 giorni.
  - neckline 70,69; target 62,51; distanza dalla neckline 63,31%; prezzo sopra neckline.
- Adam and Eve Top: **CANDIDATO** (0)
  - Pattern Adam and Eve Top vicino a 83,81 dal 2026-07-04 al 2026-08-09. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 70,69. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 46 giorni.
  - neckline 70,69; target 57,58; distanza dalla neckline 63,31%; prezzo sopra neckline.

### DOGE

- Prezzo: **0.09448 $**
- Punteggio tecnico: **8 / 12**
- Verdetto: **RIALZISTA TECNICO**
- Trend: **Trend rialzista** (3)
- Momentum: **Momentum in miglioramento** (3)
- Volume: **Volume da accumulazione** (1)
- Struttura: **Struttura ribassista con massimi e minimi decrescenti** (-2)
  - Dettaglio struttura: Ultimi minimi: 0.08028 -> 0.07841. Ultimi massimi: 0.09998 -> 0.09421.
- Divergenza: **Nessuna** (0)
- Fase Wyckoff candidata: **Markup / fase rialzista** (2)
  - Dettaglio Wyckoff: Prezzo sopra MA200, MA50 in salita e trend a 30 giorni positivo.
- Fibonacci automatico: **TESTATO** (0)
  - Swing DOWN 2026-08-22 0.09998 -> 2026-09-16 0.07841; livello più vicino 78.6% a 0.09536; stato TESTATO; confluenza: neckline rialzista, invalidazione rialzista.
- Punteggio pattern: **+1**
  - rialzista dominante: Doppio minimo (ATTIVO, +1); ribassista dominante: Doppio massimo (CANDIDATO, 0).
- Supporto più vicino: **0.07841**
- Resistenza più vicina: **0.09998**

Pattern classici e ciclo di vita:

- Doppio minimo: **ATTIVO** (+1)
  - Due minimi simili vicino a 0.07841 tra 2026-09-02 e 2026-09-16. Neckline stimata: 0.09421. Breakout neckline: 2026-09-21 (3 giorni fa). Stato: ATTIVO. Target teorico: 0.11001; progresso corrente: 1,71%. Relazione prezzo/neckline: vicino alla neckline.
  - neckline 0.09421; target 0.11001; breakout 2026-09-21 (3g); progresso 1,71%; prezzo vicino alla neckline.
- Triplo minimo: **TARGET RAGGIUNTO** (0)
  - Tre minimi simili vicino a 0.06835 dal 2026-07-13 al 2026-08-12. Neckline stimata: 0.07380. Breakout neckline: 2026-08-19 (36 giorni fa). Stato: TARGET RAGGIUNTO. Target teorico: 0.07926; progresso corrente: 379,03%. Relazione prezzo/neckline: sopra neckline.
  - neckline 0.07380; target 0.07926; breakout 2026-08-19 (36g); progresso 379,03%; prezzo sopra neckline.
- Adam and Eve Bottom: **ATTIVO** (+1)
  - Pattern Adam and Eve Bottom vicino a 0.07841 dal 2026-09-02 al 2026-09-16. Un minimo è più appuntito e l'altro più arrotondato. Neckline stimata: 0.09421. Breakout neckline: 2026-09-21 (3 giorni fa). Stato: ATTIVO. Target teorico: 0.11001; progresso corrente: 1,71%. Relazione prezzo/neckline: vicino alla neckline.
  - neckline 0.09421; target 0.11001; breakout 2026-09-21 (3g); progresso 1,71%; prezzo vicino alla neckline.
- Doppio massimo: **CANDIDATO** (0)
  - Due massimi simili vicino a 0.07380 tra 2026-07-26 e 2026-08-11. Neckline ribassista stimata: 0.06797. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 44 giorni.
  - neckline 0.06797; target 0.06214; distanza dalla neckline 39,00%; prezzo sopra neckline.
- Triplo massimo: **CANDIDATO** (0)
  - Tre massimi simili vicino a 0.07923 dal 2026-07-04 al 2026-08-11. Neckline ribassista stimata: 0.06797. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 44 giorni.
  - neckline 0.06797; target 0.05671; distanza dalla neckline 39,00%; prezzo sopra neckline.
- Adam and Eve Top: **CANDIDATO** (0)
  - Pattern Adam and Eve Top vicino a 0.07923 dal 2026-07-04 al 2026-08-11. Un massimo è più appuntito e l'altro più arrotondato. Neckline ribassista stimata: 0.06797. Stato: CANDIDATO; la neckline non è ancora stata rotta con un margine di almeno 0.50%. Età della formazione: 44 giorni.
  - neckline 0.06797; target 0.05671; distanza dalla neckline 39,00%; prezzo sopra neckline.

## Fibonacci automatico

Il modulo seleziona uno swing recente tramite pivot confermati. Un semplice tocco vale 0: Fibonacci pesa al massimo ±1 soltanto quando il livello è tenuto, perso, recuperato o respinto e coincide con almeno un livello tecnico indipendente.

| Asset   | Swing                         | 23,6%   | 38,2%   | 50,0%   | 61,8%   | 78,6%   | Livello vicino   | Stato      | Confluenza                                                      |   Score |
|:--------|:------------------------------|:--------|:--------|:--------|:--------|:--------|:-----------------|:-----------|:----------------------------------------------------------------|--------:|
| BTC | DOWN 2026-09-03 -> 2026-09-15 | 76.672 | 77.740 | 78.603 | 79.467 | 80.696 | 78.6% / 80.696 | RECUPERATO | resistenza tecnica, neckline rialzista, invalidazione rialzista | +1 |
| SOL | DOWN 2026-08-27 -> 2026-09-16 | 99,49 | 101,50 | 103,13 | 104,76 | 107,08 | 78.6% / 107,08 | RECUPERATO | resistenza tecnica, neckline rialzista, invalidazione rialzista | +1 |
| DOGE | DOWN 2026-08-22 -> 2026-09-16 | 0.08350 | 0.08665 | 0.08919 | 0.09174 | 0.09536 | 78.6% / 0.09536 | TESTATO | neckline rialzista, invalidazione rialzista | 0 |

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

<!-- COMPACT_SECTION_START:data_quality -->
<details>
<summary><strong>✅ Controllo qualità e coerenza dati</strong></summary>

<!-- DATA_QUALITY_COHERENCE_START -->
# Data quality / coherence check

Generato: 2026-09-24 05:32 UTC

Questo controllo non modifica punteggi o decisioni. Verifica che tutti i moduli usino lo stesso prezzo corrente e che le nuove regole Technical/Classic Visual siano integre.

## Stato finale: **WARN**

## Avvisi

- Blocco Global Confluence non trovato nel report principale.
- 2 campi prezzo superano la tolleranza specifica del modulo.

## Prezzo unico per modulo

| Modulo                  | Asset   | Campo             | Stato   | Prezzo snapshot   | Prezzo modulo   | Differenza   |
|:------------------------|:--------|:------------------|:--------|:------------------|:----------------|:-------------|
| Scanner                 | BTC     | current_price     | OK      | 84.184 $          | 84.184 $        | +0,0000%     |
| Scanner                 | DOGE    | current_price     | OK      | 0.09448 $         | 0.09448 $       | +0,0000%     |
| Scanner                 | SOL     | current_price     | OK      | 115,45 $          | 115,45 $        | +0,0000%     |
| Scanner Forecast        | BTC     | current_price     | OK      | 84.184 $          | 84.184 $        | +0,0000%     |
| Scanner Forecast        | SOL     | current_price     | OK      | 115,45 $          | 115,45 $        | +0,0000%     |
| Scanner Forecast        | DOGE    | current_price     | OK      | 0.09448 $         | 0.09448 $       | +0,0000%     |
| Technical Structure     | BTC     | price             | OK      | 84.184 $          | 84.184 $        | +0,0000%     |
| Technical Structure     | SOL     | price             | OK      | 115,45 $          | 115,45 $        | +0,0000%     |
| Technical Structure     | DOGE    | price             | OK      | 0.09448 $         | 0.09448 $       | +0,0000%     |
| Classic Technical       | BTC     | price             | OK      | 84.184 $          | 84.184 $        | +0,0000%     |
| Classic Technical       | SOL     | price             | OK      | 115,45 $          | 115,45 $        | +0,0000%     |
| Classic Technical       | DOGE    | price             | OK      | 0.09448 $         | 0.09448 $       | +0,0000%     |
| Classic Visual          | BTC     | price             | OK      | 84.184 $          | 84.184 $        | +0,0000%     |
| Classic Visual          | SOL     | price             | OK      | 115,45 $          | 115,45 $        | +0,0000%     |
| Classic Visual          | DOGE    | price             | OK      | 0.09448 $         | 0.09448 $       | +0,0000%     |
| Exchange Microstructure | BTC     | price             | OK      | 84.184 $          | 84.264 $        | +0,0958%     |
| Exchange Microstructure | SOL     | price             | WARN    | 115,45 $          | 115,86 $        | +0,3560%     |
| Exchange Microstructure | DOGE    | price             | WARN    | 0.09448 $         | 0.09480 $       | +0,3387%     |
| RSI top-cycle           | SOL     | current_price     | OK      | 115,45 $          | 115,45 $        | +0,0000%     |
| RSI top-cycle           | SOL     | current_price     | OK      | 115,45 $          | 115,45 $        | +0,0000%     |
| Frattale BTC/SOL        | SOL     | sol_current_price | OK      | 115,45 $          | 115,45 $        | +0,0000%     |
| Fractal path            | SOL     | current_price     | OK      | 115,45 $          | 115,45 $        | +0,0000%     |

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


<!-- SOL_LONG_TERM_CONE_HISTORY_START -->
## SOL Long-Term Cone History

[SOL Long-Term Cone History](sol_long_term_history/README.md)
<!-- SOL_LONG_TERM_CONE_HISTORY_END -->
