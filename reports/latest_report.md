<!-- DECISION_REPORT_START -->

# Decisione operativa sintetica

Report separato completo: [decision_report.md](decision_report.md)

Sintesi automatica dello scanner: spot, long, short e rischio. Ora include anche Global Confluence e Lifecycle EMA200 per SOL.

| Asset | Direzione | Spot | Long leva | Short leva | Max long | Max short | Rischio |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | BULLISH | COMPRA / ACCUMULA | LONG PRUDENTE | NO SHORT | max 2x isolated | nessuna | MEDIO |
| SOL | NEUTRALE / COSTRUTTIVO | HOLD / TRANCHE PICCOLE, NO LEVA | NO LONG A LEVA | NO SHORT | nessuna | nessuna | MOLTO ALTO |
| DOGE | BEARISH | VENDI PARZIALE / STAI FUORI | NO LONG A LEVA | SHORT SOLO DOPO SPIKE | nessuna | max 1x-2x isolated | MOLTO ALTO |

## Lettura immediata

- **BTC**: spot = **COMPRA / ACCUMULA**, long = **LONG PRUDENTE**, short = **NO SHORT**, rischio = **MEDIO**.
- **SOL**: spot = **HOLD / TRANCHE PICCOLE, NO LEVA**, long = **NO LONG A LEVA**, short = **NO SHORT**, rischio = **MOLTO ALTO**. Lifecycle EMA = **+1**, EMA200 = **113,51 $**.
- **DOGE**: spot = **VENDI PARZIALE / STAI FUORI**, long = **NO LONG A LEVA**, short = **SHORT SOLO DOPO SPIKE**, rischio = **MOLTO ALTO**.

## Nota semplice

- **Zona alta storica** = zona dove non inseguire troppo; può essere zona da prendere profitto.
- **Zona bassa storica** = zona di rischio; con leva la liquidazione non dovrebbe stare lì vicino.
- **Lifecycle EMA200** = per SOL aggiunge contesto da squeeze verso EMA200 weekly, ma non autorizza leva da solo.
- **NO LONG** non significa automaticamente **SHORT**. Lo short ha senso solo se il quadro è bearish o se lo spike viene spesso scaricato.

<!-- DECISION_REPORT_END -->

<!-- GLOBAL_CONFLUENCE_START -->
# Sintesi finale di confluenza

Generato: 2026-07-09 15:58 UTC

Questo report mette insieme i moduli principali dello scanner e controlla se si confermano o si contraddicono.

Moduli letti:

- Scanner frattale/statistico a 30 giorni
- Scanner path / cono previsionale
- Market regime match
- Struttura tecnica classica
- Frattale BTC 2022 vs SOL 2026, solo per SOL
- Fractal path tracker, solo per SOL
- RSI top-cycle, soprattutto per SOL
- Major alt lifecycle squeeze / EMA200 weekly, solo per SOL
- Futures / liquidazioni
- Cambiamento giornaliero

## Sintesi operativa

| Asset   |   Punteggio | Confluenza             | Bias                 | Affidabilità   | Azione coerente                                    | Conferme                                                                                       | Invalidazioni                                |
|:--------|------------:|:-----------------------|:---------------------|:---------------|:---------------------------------------------------|:-----------------------------------------------------------------------------------------------|:---------------------------------------------|
| BTC     |          +5 | MODERATAMENTE POSITIVA | Costruttivo prudente | MEDIA          | ACCUMULA SU PULLBACK / NO SHORT                    | Sopra 65.544 migliora; sopra la neckline tecnica successiva il recupero diventa più credibile. | Sotto 57.748 il quadro tecnico peggiora.     |
| SOL     |          +5 | MODERATAMENTE POSITIVA | Costruttivo prudente | MEDIA          | HOLD / TRANCHE PICCOLE, NO LEVA                    | Conferme sopra 83,81 / 105,44 / 114,16.                                                        | Allarmi sotto 73,59 / 64,42 / 62,19.         |
| DOGE    |          -9 | NEGATIVA               | Ribassista           | MEDIA / ALTA   | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE | Sopra 0.07923 migliora, ma resta asset debole finché scanner e struttura non girano.           | Sotto 0.06961 il rischio ribassista aumenta. |

## Punteggi per modulo

| Asset   |   Scanner |   Scanner path |   Market regime |   Tecnico |   Frattale SOL |   Fractal path |   RSI top-cycle |   Lifecycle EMA |   Futures |   Daily change |   Totale |
|:--------|----------:|---------------:|----------------:|----------:|---------------:|---------------:|----------------:|----------------:|----------:|---------------:|---------:|
| BTC     |        +3 |              0 |              +3 |        -2 |              0 |              0 |               0 |               0 |         0 |             +1 |       +5 |
| SOL     |        -1 |              0 |              +2 |         0 |             +2 |              0 |              +1 |              +1 |         0 |              0 |       +5 |
| DOGE    |        -3 |              0 |              -3 |        -3 |              0 |              0 |               0 |               0 |         0 |              0 |       -9 |

## Lettura asset per asset

### BTC

- Confluenza: **MODERATAMENTE POSITIVA**
- Bias: **Costruttivo prudente**
- Punteggio finale: **+5**
- Affidabilità: **MEDIA**
- Azione coerente: **ACCUMULA SU PULLBACK / NO SHORT**

BTC è l'asset messo meglio nel breve. La struttura macro non è ancora pienamente rialzista, ma scanner, regime e segnali tecnici interni sono abbastanza coerenti per un recupero prudente.

Dettaglio moduli:

- Scanner 30g: **+3** — Casi positivi 70,00%, return centrale 30g 6,89%.
- Scanner path / cono: **0** — Raccolta dati. Controlli disponibili 1. Servono almeno 5 controlli prima di pesare il cono previsionale.
- Market regime: **+3** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 16, positivi 30g 93,75%, return p50 23,86%.
- Tecnico: **-2** — Score tecnico -3/12, verdetto debole, trend trend ribassista, struttura struttura ribassista con massimi e minimi decrescenti, divergenza divergenza rialzista RSI, Wyckoff possibile accumulazione.
- Frattale SOL/BTC: **0** — Non applicabile a questo asset.
- Fractal path tracker: **0** — Non applicabile a questo asset.
- RSI top-cycle: **0** — Non applicabile a questo asset.
- Lifecycle EMA200: **0** — Non applicabile a questo asset.
- Futures/liquidazioni: **0** — Lettura futures Rischio sotto, forza 5/5.
- Cambiamento giornaliero: **+1** — BTC: cambiamento importante in miglioramento rispetto a ieri.

Conferme: Sopra 65.544 migliora; sopra la neckline tecnica successiva il recupero diventa più credibile.

Invalidazioni: Sotto 57.748 il quadro tecnico peggiora.

### SOL

- Confluenza: **MODERATAMENTE POSITIVA**
- Bias: **Costruttivo prudente**
- Punteggio finale: **+5**
- Affidabilità: **MEDIA**
- Azione coerente: **HOLD / TRANCHE PICCOLE, NO LEVA**

SOL ha una confluenza costruttiva, ma va ancora trattato come setup anticipato. La conferma vera arriva solo sopra le resistenze tecniche, frattali e verso la zona EMA200 weekly. Il modulo lifecycle/EMA200 aggiunge una lettura positiva da squeeze, ma non sostituisce le conferme di prezzo.

Dettaglio moduli:

- Scanner 30g: **-1** — Casi positivi 42,50%, return centrale 30g -1,54%.
- Scanner path / cono: **0** — Raccolta dati. Controlli disponibili 1. Servono almeno 5 controlli prima di pesare il cono previsionale.
- Market regime: **+2** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 19, positivi 30g 63,16%, return p50 0,92%.
- Tecnico: **0** — Score tecnico -1/12, verdetto neutrale / misto, trend trend misto, struttura volatilità in espansione, divergenza nessuna, Wyckoff range / fase non chiara.
- Frattale SOL/BTC: **+2** — Verdetto PARZIALMENTE SI, somiglianza 73,81%, tracking FRATTALE STABILE, fase FASE ANTICIPATA, rischio MEDIO / ALTO.
- Fractal path tracker: **0** — Raccolta dati. Controlli disponibili 0. Servono almeno 5 controlli prima di pesare il percorso frattale.
- RSI top-cycle: **+1** — Rischio top-cycle RSI: BASSO.
- Lifecycle EMA200: **+1** — Lifecycle score 5, peso Global +1, bias SQUEEZE SETUP FORTE, EMA200 113,51 $, upside EMA200 46,46%, stato EMA50/EMA200 SOVRAPPOSTE / INCROCIO IN CORSO, hit EMA200 12w 36,67%, trend STABILE / DA CONFERMARE.
- Futures/liquidazioni: **0** — Lettura futures Misto, forza 1/5.
- Cambiamento giornaliero: **0** — SOL: nessun cambiamento forte rispetto a ieri.

Conferme: Conferme sopra 83,81 / 105,44 / 114,16.

Invalidazioni: Allarmi sotto 73,59 / 64,42 / 62,19.

### DOGE

- Confluenza: **NEGATIVA**
- Bias: **Ribassista**
- Punteggio finale: **-9**
- Affidabilità: **MEDIA / ALTA**
- Azione coerente: **STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE**

DOGE resta l'asset più debole. Anche se può fare rimbalzi o spike, la confluenza generale resta negativa rispetto a BTC e SOL.

Dettaglio moduli:

- Scanner 30g: **-3** — Casi positivi 12,50%, return centrale 30g -20,25%.
- Scanner path / cono: **0** — Raccolta dati. Controlli disponibili 1. Servono almeno 5 controlli prima di pesare il cono previsionale.
- Market regime: **-3** — Gruppo SAME_BTC_AND_ASSET_REGIME, match 30, positivi 30g 6,67%, return p50 -27,25%.
- Tecnico: **-3** — Score tecnico -10/12, verdetto ribassista tecnico, trend trend ribassista, struttura struttura ribassista con massimi e minimi decrescenti, divergenza divergenza ribassista nascosta RSI, Wyckoff possibile accumulazione.
- Frattale SOL/BTC: **0** — Non applicabile a questo asset.
- Fractal path tracker: **0** — Non applicabile a questo asset.
- RSI top-cycle: **0** — Non applicabile a questo asset.
- Lifecycle EMA200: **0** — Non applicabile a questo asset.
- Futures/liquidazioni: **0** — Lettura futures Misto, forza 1/5.
- Cambiamento giornaliero: **0** — DOGE: nessun cambiamento forte rispetto a ieri.

Conferme: Sopra 0.07923 migliora, ma resta asset debole finché scanner e struttura non girano.

Invalidazioni: Sotto 0.06961 il rischio ribassista aumenta.

## Come leggere il punteggio

- +7 o più: confluenza positiva forte.
- Da +3 a +6: confluenza moderatamente positiva.
- Da 0 a +2: confluenza parziale o mista.
- Da -1 a -3: confluenza debole o fragile.
- -4 o meno: confluenza negativa.

Nota: Scanner path e Fractal path sono già integrati, ma finché hanno pochi controlli restano quasi sempre a punteggio 0.
Servono almeno 5 controlli prima di influire leggermente, e 30+ controlli prima di pesare davvero.

Nota lifecycle EMA200: il modulo Major alt lifecycle squeeze pesa al massimo +1 / -1 nel Global, perché è un filtro di contesto e non una conferma diretta di prezzo.
<!-- GLOBAL_CONFLUENCE_END -->

<!-- BTC_SOL_FRACTAL_START -->

---

# Frattale mirato: BTC 2022 vs SOL 2026

Report separato completo: [btc_2022_vs_sol_2026_report.md](btc_2022_vs_sol_2026_report.md)

Ultima candela SOL usata: **9 luglio 2026**

## Verdetto: PARZIALMENTE SI

- **Fase attuale:** FASE ANTICIPATA
- **Somiglianza totale:** +73,81%
- **Affidabilita:** MEDIA
- **Rischio fase:** MEDIO / ALTO
- **Trend tracking:** FRATTALE STABILE
- **Sintesi:** SOL sta seguendo abbastanza il frattale BTC 2022, ma non in modo perfetto.
- **SOL e al giorno:** 33 dal bottom usato.
- **Giorno BTC equivalente:** 2022-12-24
- **Prossimo step:** Prossimo step previsto dal frattale: **Laterale / movimento non forte.** Zona bassa stimata: **76,08 $** intorno al **16 luglio 2026**. Zona alta stimata: **77,95 $** intorno al **23 luglio 2026**. Fine step: circa **77,95 $** entro il **23 luglio 2026**.

## Somiglianza prima e dopo inizio programma

Questa sezione separa la parte gia successa prima del programma dalla parte che stiamo monitorando davvero.

- **Inizio programma/scanner:** 3 luglio 2026
- **Prima del programma** = backtest retroattivo: utile, ma gia conosciuto.
- **Da inizio programma** = verifica reale: serve a capire se il frattale sta reggendo dopo che lo abbiamo iniziato a seguire.

| Periodo | Date | Giorni | Aderenza prezzo | Errore medio | Errore ultimo giorno | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| Prima del programma | 6 giugno 2026 -> 2 luglio 2026 | 27 | +87,95% | +6,02% | +21,89% | ABBASTANZA ALLINEATO |
| Da inizio programma | 3 luglio 2026 -> 9 luglio 2026 | 7 | +56,41% | +21,79% | +16,71% | STACCATO / MOLTO IN ANTICIPO |
| Totale dal bottom | 6 giugno 2026 -> 9 luglio 2026 | 34 | +81,46% | +9,27% | +16,71% | ABBASTANZA ALLINEATO |

Nota: **Aderenza prezzo** è uno score semplice basato sulla distanza media dalla linea BTC-scalata. Non sostituisce la somiglianza totale ufficiale, ma rende chiaro se SOL è vicino, sopra o sotto il percorso BTC equivalente.

## Lettura operativa veloce

Fase anticipata: ingresso migliore come prezzo, ma certezza ancora bassa. Ha senso ragionare a tranche, non tutto insieme.

| Voce | Risposta | Perche |
| --- | --- | --- |
| Spot anticipato | SI, ma a tranche | La zona e ancora prima della conferma piena. |
| Aggiunta su conferma | SI | Aggiunta sensata se rompe e tiene 105,44 $. |
| Seconda conferma | 114,16 $ | Sopra questa zona il frattale diventa molto piu credibile. |
| Rischio inseguimento | BASSO / MEDIO | Non sei ancora troppo in ritardo, ma serve invalidazione chiara. |
| Invalidazione soft | 73,59 $ | Sotto questa zona il frattale si indebolisce. |
| Invalidazione forte | 62,19 $ | Sotto questa zona il frattale e quasi rotto. |

## Target ciclo fino al top BTC 2025

| Voce | Valore |
| --- | --- |
| Top BTC 2025 | 6 ottobre 2025 - 124.753 $ |
| Data SOL equivalente | 21 aprile 2029 |
| Target ciclo base dal bottom | 491,43 $ |
| Target ciclo base da oggi | 573,57 $ |
| Massimo percorso base | 573,57 $ (21 aprile 2029) |
| Massimo percorso beta | 2.326 $ (21 aprile 2029) |

## Grafici

### Grafico frattale sovrapposto

![Frattale BTC 2022 vs SOL 2026](btc_2022_vs_sol_2026_fractal_chart.png)

### Grafico proiezione SOL

![Proiezione SOL BTC 2022](btc_2022_vs_sol_2026_projection_chart.png)

### Grafico ciclo BASE fino al top BTC 2025

![Ciclo base SOL BTC 2025](btc_2022_vs_sol_2026_cycle_base_chart.png)

Nel report completo trovi anche il grafico beta separato e il grafico in scala logaritmica.

### Grafico tracking giornaliero

![Tracking frattale BTC SOL](btc_2022_vs_sol_2026_tracking_chart.png)

## Livelli chiave

| Livello | Prezzo | Lettura |
| --- | --- | --- |
| Prima conferma | 105,44 $ | Migliora il frattale. |
| Seconda conferma | 114,16 $ | Scenario rialzista piu credibile. |
| Invalidazione soft | 73,59 $ | Il frattale si indebolisce. |
| Invalidazione forte | 62,19 $ | Il paragone BTC 2022 si rompe. |

## Proiezione veloce con date SOL

| Orizzonte | Data SOL prevista | BTC fece | SOL base | Min percorso | Max percorso |
| --- | --- | --- | --- | --- | --- |
| 7 giorni | 16 luglio 2026 | -1,78% | 76,08 $ | 76,08 $ | 77,79 $ |
| 14 giorni | 23 luglio 2026 | +0,64% | 77,95 $ | 76,08 $ | 77,95 $ |
| 30 giorni | 8 agosto 2026 | +36,13% | 105,44 $ | 76,08 $ | 105,44 $ |
| 60 giorni | 7 settembre 2026 | +43,57% | 111,21 $ | 76,08 $ | 114,16 $ |
| 90 giorni | 7 ottobre 2026 | +63,19% | 126,40 $ | 76,08 $ | 130,27 $ |
| 120 giorni | 6 novembre 2026 | +63,77% | 126,86 $ | 76,08 $ | 140,16 $ |

## Prossimi step se SOL segue BTC 2022

| Step | Date SOL | BTC fine | SOL zona bassa | SOL zona alta | SOL fine base | Lettura |
| --- | --- | --- | --- | --- | --- | --- |
| Step 1 - prossime 2 settimane | 9 luglio 2026 -> 23 luglio 2026 | +0,64% | 76,08 $ (16 luglio 2026) | 77,95 $ (23 luglio 2026) | 77,95 $ | Laterale / movimento non forte. |
| Step 2 - primo mese | 24 luglio 2026 -> 8 agosto 2026 | +36,13% | 78,58 $ (24 luglio 2026) | 105,44 $ (8 agosto 2026) | 105,44 $ | Spinta rialzista abbastanza pulita. |
| Step 3 - secondo mese | 9 agosto 2026 -> 7 settembre 2026 | +43,57% | 99,54 $ (26 agosto 2026) | 114,16 $ (5 settembre 2026) | 111,21 $ | Spinta rialzista abbastanza pulita. |
| Step 4 - terzo mese | 8 settembre 2026 -> 7 ottobre 2026 | +63,19% | 92,81 $ (23 settembre 2026) | 130,27 $ (6 ottobre 2026) | 126,40 $ | Spinta rialzista abbastanza pulita. |

Nota: questa e una proiezione analogica. Conta soprattutto se SOL rispetta i livelli di conferma e invalidazione.

<!-- BTC_SOL_FRACTAL_END -->

<!-- RSI_TOP_CYCLE_START -->

---

# RSI top-cycle warning - SOL

Report separato completo: [rsi_top_cycle_report.md](rsi_top_cycle_report.md)

Questo filtro controlla se RSI weekly/monthly si stanno avvicinando alla trendline alta che puo segnalare esaurimento ciclo.

| Voce | Valore | Lettura |
| --- | --- | --- |
| Prezzo SOL | 77,46 $ |  |
| Weekly RSI | 40,36 / top-line 56,32 | LONTANO DALLA TOP-LINE - normale |
| Monthly RSI | 41,28 / top-line 48,69 | IN AVVICINAMENTO - troppo ripida per proiezione 2029 |
| Target ciclo base | 573,57 $ | Avanzamento +13,50% |
| Rischio top-cycle RSI | BASSO | Nessun segnale top-cycle macro attivo. Prezzo ancora lontano dal target ciclo; il filtro RSI serve piu avanti. |

## Lettura semplice

- Weekly: RSI weekly e ancora basso e lontano dalla trendline di esaurimento ciclo.
- Monthly: RSI monthly si sta avvicinando alla trendline, ma non la sta ancora testando.
- Confluenza prezzo + RSI: **BASSO**

Questo non e un segnale di entrata. Serve soprattutto per riconoscere piu avanti una possibile zona top, per esempio se SOL si avvicina ai target 500/600 e RSI weekly/monthly tornano sulla top-line.

## Grafici RSI

![SOL weekly RSI top-line](rsi_top_cycle_SOL_weekly.png)

![SOL monthly RSI top-line](rsi_top_cycle_SOL_monthly.png)

<!-- RSI_TOP_CYCLE_END -->

<!-- SOL_ONCHAIN_METRICS_START -->

---

# SOL on-chain metrics

Report separato completo: **[sol_onchain_metrics_report.md](sol_onchain_metrics_report.md)**

| Voce | Valore |
| --- | --- |
| Score on-chain | 2 |
| Bias | POSITIVA |
| Azione coerente | CONFERMA MODERATA / BUONO SE IL FRATTALE REGGE |
| Prezzo SOL | 77,57 $ |
| TVL Solana | 4,94 mld $ |
| TVL 7g | +0,63% |
| DEX volume 24h | 2,44 mld $ |
| Fees 24h | 8,25 mln $ |
| Stablecoin su Solana | 15,39 mld $ |
| Stake ratio | 68,16% |
| Metriche mancanti | sol_realized_price_usd, sol_mvrv, sol_holder_profit_pct, sol_exchange_netflow_24h_usd |

Lettura semplice:

**CONFERMA MODERATA / BUONO SE IL FRATTALE REGGE**

Questo blocco non sostituisce il frattale SOL/BTC: serve come filtro per capire se il movimento è sostenuto anche da attività on-chain.

<!-- SOL_ONCHAIN_METRICS_END -->

<!-- MAJOR_ALT_LIFECYCLE_SQUEEZE_START -->

---

# Major alt lifecycle squeeze - SOL

Report separato completo: **[major_alt_lifecycle_squeeze_report.md](major_alt_lifecycle_squeeze_report.md)**

| Voce | Valore |
| --- | --- |
| Lifecycle squeeze score | 5 |
| Bias | SQUEEZE SETUP FORTE |
| Azione coerente | CONFLUENZA BUONA VERSO EMA200, MA SOLO CON CONFERME |
| Peso suggerito Global | 1 |
| Trend squeeze | STABILE / DA CONFERMARE |
| Trend squeeze score | 0 |
| Confronto precedente | 2026-07-08 |
| Fonte prezzi | Yahoo Finance SOL-USD weekly |
| Prezzo SOL | 77,50 $ |
| EMA200 weekly target | 113,51 $ |
| Upside verso EMA200 | +46,46% |
| Distanza prezzo da EMA200 | -31,72% |
| Gap EMA50/EMA200 | -1,23% |
| Stato cross | EMA50/EMA200 SOVRAPPOSTE / INCROCIO IN CORSO |
| RSI weekly | 40,38 |
| Età SOL | 6,3 anni |
| Analoghi storici usati | 30 |
| Max analoghi per asset | 3 |
| Hit EMA200 12w analoghi | 36,67% |
| Max gain mediano 12w | +22,68% |
| Drawdown mediano 12w | -22,63% |

Lettura semplice:

**CONFLUENZA BUONA VERSO EMA200, MA SOLO CON CONFERME**

Autocontrollo: **STABILE / DA CONFERMARE**.

Questo modulo confronta SOL con altre crypto in fasi simili di età, distanza da EMA200, EMA50/EMA200 e RSI. Non usa stock market.

Nota: se EMA50/EMA200 sono dentro ±2%, il modulo parla di medie sovrapposte / incrocio in corso, perché exchange diversi possono mostrare il cross leggermente prima o dopo.

<!-- MAJOR_ALT_LIFECYCLE_SQUEEZE_END -->

# Report giornaliero BTC / SOL / DOGE

Aggiornato il: **2026-07-09 15:54:58 UTC**

Questo report confronta il grafico attuale di Bitcoin, Solana e Dogecoin con tanti grafici storici di altre crypto.

Non è una previsione certa. È uno scanner statistico: guarda situazioni simili già successe e mostra cosa accadde dopo nei 30 giorni successivi.

<!-- DAILY_CHANGE_START -->

---

# Mini report cambiamenti da ieri

Report separato completo: [daily_change_report.md](daily_change_report.md)

- BTC: cambiamento importante in miglioramento rispetto a ieri.
- SOL: nessun cambiamento forte rispetto a ieri.
- DOGE: nessun cambiamento forte rispetto a ieri.

| Asset | Cambio | Tono | Verdetto oggi | Casi positivi oggi | Δ casi positivi |
| --- | --- | --- | --- | --- | --- |
| BTC | CAMBIAMENTO MEDIO | miglioramento | RIALZISTA | +70.00% | +5.00 punti |
| SOL | NESSUN CAMBIAMENTO FORTE | miglioramento | NEUTRALE / INCERTO | +42.50% | -2.50 punti |
| DOGE | NESSUN CAMBIAMENTO FORTE | peggioramento | RIBASSISTA | +12.50% | -7.50 punti |

<!-- DAILY_CHANGE_END -->

<!-- BOUNCE_AFTER_DRAWDOWN_START -->

---

# Sequenze pratiche: rimbalzo / dump

Report separato completo: [bounce_after_drawdown_report.md](bounce_after_drawdown_report.md)

Questa sezione risponde subito a due domande:

- **Se scende, è una zona di rimbalzo?**
- **Se sale forte, è una zona da prendere profitto?**

| Asset | Scende a | Target rimbalzo | % casi rimbalzo | Movimento reale | Lettura discesa | Sale a | Target dump | % casi dump | Movimento reale | Lettura spike |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 59.739 $ | 69.172 $ | +17,65% | +15,79% | rimbalzo poco frequente | 69.172 $ | 59.739 $ | +16,00% | -13,64% | spike storicamente più resistente |
| SOL | 73,69 $ | 85,33 $ | +11,11% | +15,79% | rimbalzo poco frequente | 85,33 $ | 73,69 $ | +26,32% | -13,64% | spike storicamente più resistente |
| DOGE | 0,06892 $ | 0,07980 $ | +8,33% | +15,79% | rimbalzo poco frequente | 0,07980 $ | 0,06892 $ | +66,67% | -13,64% | spike spesso scaricato |

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

- **BTC: su 40 casi simili, 17 prima sono scesi a -5,00%. Tra quei 17, 3 poi sono rimbalzati fino a +10,00%. Percentuale: +17,65% (3/17). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.**
- **BTC: su 40 casi simili, 25 prima sono saliti a +10,00%. Tra quei 25, 4 poi sono scaricati a -5,00%. Percentuale: +16,00% (4/25). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.**
- **SOL: su 40 casi simili, 27 prima sono scesi a -5,00%. Tra quei 27, 3 poi sono rimbalzati fino a +10,00%. Percentuale: +11,11% (3/27). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.**
- **SOL: su 40 casi simili, 19 prima sono saliti a +10,00%. Tra quei 19, 5 poi sono scaricati a -5,00%. Percentuale: +26,32% (5/19). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.**
- **DOGE: su 40 casi simili, 36 prima sono scesi a -5,00%. Tra quei 36, 3 poi sono rimbalzati fino a +10,00%. Percentuale: +8,33% (3/36). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.**
- **DOGE: su 40 casi simili, 12 prima sono saliti a +10,00%. Tra quei 12, 8 poi sono scaricati a -5,00%. Percentuale: +66,67% (8/12). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike spesso scaricato.**

<!-- BOUNCE_AFTER_DRAWDOWN_END -->

<!-- SCANNER_FORECAST_TRACKER_START -->
# Scanner forecast path / cono probabilistico

Generato: 2026-07-09 15:58 UTC

Questo report trasforma lo scanner dei 40 casi simili in un grafico a percorso.

Per ogni asset crea:

- banda larga p10-p90
- banda centrale p25-p75
- scenario centrale p50
- prezzo reale sovrapposto

Serve a vedere se il prezzo reale sta camminando dentro il percorso previsto dallo scanner.

## Ultimo cono previsionale salvato

| Asset   | Data       | Prezzo iniziale   | Direzione scanner   | Casi positivi   | P10 30g     | P25 30g     | P50 30g     | P75 30g     | P90 30g     |
|:--------|:-----------|:------------------|:--------------------|:----------------|:------------|:------------|:------------|:------------|:------------|
| BTC     | 2026-07-09 | 62.883,19 $       | SALITA              | 70,00%          | 48.524,67 $ | 61.842,87 $ | 67.215,59 $ | 77.068,15 $ | 90.394,54 $ |
| SOL     | 2026-07-09 | 77,57 $           | INCERTO             | 42,50%          | 62,40 $     | 70,40 $     | 76,37 $     | 86,13 $     | 111,51 $    |
| DOGE    | 2026-07-09 | 0.07000 $         | DISCESA             | 12,50%          | 0.05000 $   | 0.05000 $   | 0.06000 $   | 0.07000 $   | 0.07000 $   |

## Grafici

### BTC

![Scanner forecast BTC](scanner_forecast_BTC.png)

### SOL

![Scanner forecast SOL](scanner_forecast_SOL.png)

### DOGE

![Scanner forecast DOGE](scanner_forecast_DOGE.png)

## Accuratezza percorso scanner

| Asset   | Giorno   |   Controlli | Dentro p10-p90   | Dentro p25-p75   | Errore medio abs vs p50   | Errore medio vs p50   |
|:--------|:---------|------------:|:-----------------|:-----------------|:--------------------------|:----------------------|
| BTC     | 1g       |           1 | 100,00%          | 100,00%          | 0,18%                     | -0,18%                |
| BTC     | 3g       |           0 | n/a              | n/a              | n/a                       | n/a                   |
| BTC     | 7g       |           0 | n/a              | n/a              | n/a                       | n/a                   |
| BTC     | 14g      |           0 | n/a              | n/a              | n/a                       | n/a                   |
| BTC     | 30g      |           0 | n/a              | n/a              | n/a                       | n/a                   |
| SOL     | 1g       |           1 | 100,00%          | 100,00%          | 0,21%                     | 0,21%                 |
| SOL     | 3g       |           0 | n/a              | n/a              | n/a                       | n/a                   |
| SOL     | 7g       |           0 | n/a              | n/a              | n/a                       | n/a                   |
| SOL     | 14g      |           0 | n/a              | n/a              | n/a                       | n/a                   |
| SOL     | 30g      |           0 | n/a              | n/a              | n/a                       | n/a                   |
| DOGE    | 1g       |           1 | 0,00%            | 0,00%            | 3,55%                     | 3,55%                 |
| DOGE    | 3g       |           0 | n/a              | n/a              | n/a                       | n/a                   |
| DOGE    | 7g       |           0 | n/a              | n/a              | n/a                       | n/a                   |
| DOGE    | 14g      |           0 | n/a              | n/a              | n/a                       | n/a                   |
| DOGE    | 30g      |           0 | n/a              | n/a              | n/a                       | n/a                   |

## Come leggerlo

- Se il prezzo resta dentro p10-p90, lo scanner sta ancora descrivendo bene il range largo.
- Se il prezzo resta dentro p25-p75, lo scanner sta descrivendo bene anche il range centrale.
- Se il prezzo segue p50, il percorso reale è vicino allo scenario normale.
- Se il prezzo esce da p10-p90, il modello statistico dei 40 casi sta perdendo aderenza.
- Questo non sostituisce drawdown e max gain: serve soprattutto a vedere il percorso del return previsto.
<!-- SCANNER_FORECAST_TRACKER_END -->

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
- Prezzo attuale: **62.883,19 $**
- Return normale fra 30 giorni: **67.215,59 $** (6,89%)
- Drawdown normale durante il mese: **60.385,92 $** (-3,97%)
- Drawdown brutto da rispettare: **56.978,65 $** (-9,39%)
- Max gain normale durante il mese: **73.392,43 $** (16,71%)
- Max gain buono / take profit ottimistico: **83.406,40 $** (32,64%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Solana
- Direzione più probabile a 30 giorni: **INCERTO**
- Casi positivi / salita storica: **42,50%**
- Casi negativi / discesa storica: **57,50%**
- Quanto è netto il segnale: **debole**
- Prezzo attuale: **77,57 $**
- Return normale fra 30 giorni: **76,37 $** (-1,54%)
- Drawdown normale durante il mese: **69,51 $** (-10,39%)
- Drawdown brutto da rispettare: **59,29 $** (-23,56%)
- Max gain normale durante il mese: **83,61 $** (7,79%)
- Max gain buono / take profit ottimistico: **95,07 $** (22,56%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Dogecoin
- Direzione più probabile a 30 giorni: **DISCESA**
- Casi positivi / salita storica: **12,50%**
- Casi negativi / discesa storica: **87,50%**
- Quanto è netto il segnale: **forte**
- Prezzo attuale: **0,07 $**
- Return normale fra 30 giorni: **0,06 $** (-20,25%)
- Drawdown normale durante il mese: **0,05 $** (-28,61%)
- Drawdown brutto da rispettare: **0,05 $** (-37,60%)
- Max gain normale durante il mese: **0,08 $** (4,88%)
- Max gain buono / take profit ottimistico: **0,08 $** (12,34%)

**Come leggerlo:** casi positivi/negativi ti dicono la direzione più probabile. Return ti dice il prezzo finale fra 30 giorni. Drawdown ti dice il rischio di discesa durante il mese. Max gain ti dice il possibile rialzo durante il mese.

## Messaggio del giorno

Il quadro generale oggi è misto. Alcuni asset possono avere lettura diversa, quindi è meglio valutare asset per asset.

---

# Mappa semplice asset per asset

# Bitcoin — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟢 VERDE / Favorevole
**Prezzo attuale:** 62.883,19 $

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

- Se va molto male: **48.524,67 $** (-22,83%)
- Se va male: **61.842,87 $** (-1,65%)
- Scenario normale: **67.215,59 $** (6,89%)
- Se va bene: **77.068,15 $** (22,56%)
- Se va molto bene: **90.394,54 $** (43,75%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **60.385,92 $** (-3,97%)
- Discesa brutta: **56.978,65 $** (-9,39%)
- Discesa molto brutta: **42.500,97 $** (-32,41%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **73.392,43 $** (16,71%)
- Rialzo buono: **83.406,40 $** (32,64%)
- Rialzo molto forte: **102.258,81 $** (62,62%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Bitcoin tendeva a muoversi tra una zona bassa intorno a **60.385,92 $** e uno spike normale intorno a **73.392,43 $**.

La chiusura a 30 giorni era più spesso positiva: salita 70,00%, discesa 30,00%. Quindi la lettura principale è favorevole.

Nota leva BTC: se la liquidazione è vicina a 51.000 $, guarda soprattutto la discesa brutta e molto brutta. Il prezzo può recuperare dopo, ma la leva può saltare prima.

---

# Solana — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🟡 GIALLO / Incerto
**Prezzo attuale:** 77,57 $

**Direzione più probabile a 30 giorni:** **INCERTO**
- Probabilità storica di salita: **42,50%**
- Probabilità storica di discesa: **57,50%**
- Quanto è netto il segnale: **debole**

## Come leggere questa parte

- **Probabilità storica di salita** = su 40 casi simili, quanti hanno chiuso sopra dopo 30 giorni.
- **Probabilità storica di discesa** = su 40 casi simili, quanti hanno chiuso sotto dopo 30 giorni.
- **Quanto è netto il segnale** = quanto è grande la differenza tra salita e discesa. Non vuol dire certezza, vuol dire solo che il risultato storico non è vicino al 50/50.

La lettura principale è incerta, con segnale debole. Nei casi storici simili non c'è stato un vantaggio chiaro né per salita né per discesa.

## 1. Return 30d — prezzo fra 30 giorni

**Return** significa rendimento finale. Qui guardiamo dove potrebbe stare il prezzo **alla fine dei 30 giorni**, non durante il percorso.

- Se va molto male: **62,40 $** (-19,56%)
- Se va male: **70,40 $** (-9,25%)
- Scenario normale: **76,37 $** (-1,54%)
- Se va bene: **86,13 $** (11,03%)
- Se va molto bene: **111,51 $** (43,75%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **69,51 $** (-10,39%)
- Discesa brutta: **59,29 $** (-23,56%)
- Discesa molto brutta: **53,54 $** (-30,98%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **83,61 $** (7,79%)
- Rialzo buono: **95,07 $** (22,56%)
- Rialzo molto forte: **120,83 $** (55,77%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Solana tendeva a muoversi tra una zona bassa intorno a **69,51 $** e uno spike normale intorno a **83,61 $**.

La chiusura a 30 giorni è incerta: salita 42,50%, discesa 57,50%. Non c'è un vantaggio netto.

---

# Dogecoin — mappa semplice dei prossimi 30 giorni

**Semaforo:** 🔴 ROSSO / Prudenza
**Prezzo attuale:** 0,07 $

**Direzione più probabile a 30 giorni:** **DISCESA**
- Probabilità storica di salita: **12,50%**
- Probabilità storica di discesa: **87,50%**
- Quanto è netto il segnale: **forte**

## Come leggere questa parte

- **Probabilità storica di salita** = su 40 casi simili, quanti hanno chiuso sopra dopo 30 giorni.
- **Probabilità storica di discesa** = su 40 casi simili, quanti hanno chiuso sotto dopo 30 giorni.
- **Quanto è netto il segnale** = quanto è grande la differenza tra salita e discesa. Non vuol dire certezza, vuol dire solo che il risultato storico non è vicino al 50/50.

La lettura principale è ribassista, con segnale forte. Nei casi storici simili, il prezzo ha chiuso sotto dopo 30 giorni più spesso di quanto abbia chiuso sopra.

## 1. Return 30d — prezzo fra 30 giorni

**Return** significa rendimento finale. Qui guardiamo dove potrebbe stare il prezzo **alla fine dei 30 giorni**, non durante il percorso.

- Se va molto male: **0,05 $** (-36,38%)
- Se va male: **0,05 $** (-31,62%)
- Scenario normale: **0,06 $** (-20,25%)
- Se va bene: **0,07 $** (-4,52%)
- Se va molto bene: **0,07 $** (2,99%)

**Come leggerlo:** se vuoi sapere dove potrebbe trovarsi il prezzo fra 30 giorni, guarda soprattutto lo **scenario normale**.

## 2. Drawdown 30d — discesa durante i 30 giorni

**Drawdown** significa la discesa massima durante il periodo. Non è il prezzo finale: è il punto più basso che il prezzo può toccare durante il mese.

- Discesa normale: **0,05 $** (-28,61%)
- Discesa brutta: **0,05 $** (-37,60%)
- Discesa molto brutta: **0,04 $** (-43,86%)

**Come leggerlo:** se usi leva, questa è la parte più importante. Anche se dopo 30 giorni il prezzo recupera, durante il mese può prima scendere qui.

## 3. Max gain 30d — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo toccato durante il mese. Non è il prezzo finale: può essere anche solo uno spike temporaneo.

- Rialzo normale: **0,08 $** (4,88%)
- Rialzo buono: **0,08 $** (12,34%)
- Rialzo molto forte: **0,09 $** (23,46%)

**Come leggerlo:** questa parte serve per capire possibili zone di take profit. Il rialzo normale è più realistico; il rialzo molto forte è possibile ma meno comune.

## Lettura pratica finale

Scenario normale: nei casi simili, Dogecoin tendeva a muoversi tra una zona bassa intorno a **0,05 $** e uno spike normale intorno a **0,08 $**.

La chiusura a 30 giorni era più spesso negativa: salita 12,50%, discesa 87,50%. Quindi la lettura principale è prudente/debole.

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

**Prezzo attuale:** 62.883,19 $

Bitcoin ha un segnale favorevole. La statistica dei casi simili indica più possibilità di salita che di discesa, ma resta comunque una probabilità, non una certezza.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **70,00%**
- Casi negativi dopo 30 giorni: **30,00%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **84,87%**
- Rendimento medio dopo 30 giorni: **11,61%**
- Rendimento centrale dopo 30 giorni: **6,89%**
- Discesa media durante i 30 giorni: **-8,09%**
- Massimo rialzo medio durante i 30 giorni: **26,32%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **70.185,30 $**
- Scenario centrale a 30 giorni: **67.215,59 $**
- Zona di rischio media: **57.792,96 $**
- Zona di rialzo media: **79.436,58 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -22,83% → **48.524,67 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -1,65% → **61.842,87 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: 6,89% → **67.215,59 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 22,56% → **77.068,15 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 43,75% → **90.394,54 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -32,41% → **42.500,97 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -9,39% → **56.978,65 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -3,97% → **60.385,92 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: 0,00% → **62.883,19 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: 0,00% → **62.883,19 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 5,69% → **66.463,53 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 7,92% → **67.861,19 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 16,71% → **73.392,43 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 32,64% → **83.406,40 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 62,62% → **102.258,81 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| XRP-USD         | 2019-09-24   | 2020-01-01 |        88.93 |        24.17 |          -2.4  |          26.46 |
| LRC-USD         | 2018-09-19   | 2018-12-27 |        87.74 |        95.69 |           0    |         178.55 |
| FIL-USD         | 2023-06-14   | 2023-09-21 |        87.68 |         3.93 |          -1.43 |           7.62 |
| DOT-USD         | 2023-06-15   | 2023-09-22 |        87.33 |        -1.36 |          -9.22 |           6.01 |
| ETH-USD         | 2023-06-15   | 2023-09-22 |        86.72 |         4.4  |          -3.37 |           8.82 |
| KSM-USD         | 2022-03-10   | 2022-06-17 |        86.22 |        11.02 |          -4.93 |          16.96 |
| YFI-USD         | 2023-06-14   | 2023-09-21 |        86.06 |         2.83 |          -3.99 |           8.79 |
| SAND-USD        | 2023-06-14   | 2023-09-21 |        86.05 |         5.52 |          -3.95 |           9.97 |
| ONE-USD         | 2020-01-07   | 2020-04-15 |        85.72 |        14.92 |           0    |          14.92 |
| AVAX-USD        | 2023-06-16   | 2023-09-23 |        85.7  |        18.71 |          -1.26 |          19.74 |

---

# Approfondimento tecnico — Solana (SOL-USD)

## Semaforo: 🟡 GIALLO / Incerto

**Prezzo attuale:** 77,57 $

Solana è in una situazione incerta. Lo scanner non vede un vantaggio chiaro né per la salita né per la discesa. In questi casi è meglio non forzare la previsione.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **42,50%**
- Casi negativi dopo 30 giorni: **57,50%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **76,38%**
- Rendimento medio dopo 30 giorni: **7,02%**
- Rendimento centrale dopo 30 giorni: **-1,54%**
- Discesa media durante i 30 giorni: **-13,44%**
- Massimo rialzo medio durante i 30 giorni: **22,30%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **83,02 $**
- Scenario centrale a 30 giorni: **76,37 $**
- Zona di rischio media: **67,14 $**
- Zona di rialzo media: **94,87 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -19,56% → **62,40 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -9,25% → **70,40 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: -1,54% → **76,37 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: 11,03% → **86,13 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 43,75% → **111,51 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -30,98% → **53,54 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -23,56% → **59,29 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -10,39% → **69,51 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -1,85% → **76,14 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: 0,00% → **77,57 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 0,00% → **77,57 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 1,40% → **78,66 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 7,79% → **83,61 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 22,56% → **95,07 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 55,77% → **120,83 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| WAVES-USD       | 2019-02-21   | 2019-05-31 |        82.22 |       -30.84 |         -30.84 |           0.49 |
| QTUM-USD        | 2018-09-19   | 2018-12-27 |        79.52 |        -2.21 |          -3.68 |          15.25 |
| TRX-USD         | 2018-09-19   | 2018-12-27 |        79    |        55.01 |           0    |          55.01 |
| LRC-USD         | 2018-09-19   | 2018-12-27 |        78.44 |        95.69 |           0    |         178.55 |
| ALGO-USD        | 2024-04-14   | 2024-07-22 |        78.38 |       -10.79 |         -27.41 |           0    |
| XLM-USD         | 2020-01-07   | 2020-04-15 |        78.16 |        45.24 |           0    |          62.58 |
| DASH-USD        | 2024-04-15   | 2024-07-23 |        77.74 |        -1.21 |         -16.66 |           1.64 |
| APT-USD         | 2024-09-01   | 2024-12-09 |        77.73 |         0.92 |         -11.47 |           6.42 |
| NEAR-USD        | 2025-12-01   | 2026-03-10 |        77.65 |         6.36 |          -9.61 |          16.07 |
| NEO-USD         | 2023-06-15   | 2023-09-22 |        77.64 |        -5.34 |         -13.04 |           0.22 |

---

# Approfondimento tecnico — Dogecoin (DOGE-USD)

## Semaforo: 🔴 ROSSO / Prudenza

**Prezzo attuale:** 0,07 $

Dogecoin richiede prudenza. La statistica dei casi simili indica più possibilità di discesa che di salita. Con leva, il rischio principale è il drawdown durante il percorso.

## Casi positivi e negativi

- Casi positivi dopo 30 giorni: **12,50%**
- Casi negativi dopo 30 giorni: **87,50%**

**Come leggerli:** questi numeri dicono quante volte, nei 40 casi storici simili, il prezzo ha chiuso sopra o sotto dopo 30 giorni. Sono la parte più semplice per capire se storicamente era più probabile salita o discesa.

## Cosa dicono i 40 casi storici più simili

- Somiglianza media dei pattern: **85,30%**
- Rendimento medio dopo 30 giorni: **-16,99%**
- Rendimento centrale dopo 30 giorni: **-20,25%**
- Discesa media durante i 30 giorni: **-26,11%**
- Massimo rialzo medio durante i 30 giorni: **8,12%**

**Come leggerli:** il rendimento dopo 30 giorni guarda il prezzo finale. La discesa media guarda il rischio durante il mese. Il massimo rialzo medio guarda il possibile spike durante il mese.

## Livelli principali

- Scenario medio a 30 giorni: **0,06 $**
- Scenario centrale a 30 giorni: **0,06 $**
- Zona di rischio media: **0,05 $**
- Zona di rialzo media: **0,08 $**

**Come leggerli:** scenario centrale = prezzo finale più normale a 30 giorni. Zona rischio = dove può scendere durante il mese. Zona rialzo = dove può arrivare durante uno spike.

## Percentili return — prezzo fra 30 giorni

**Return** significa prezzo finale dopo 30 giorni rispetto al prezzo di oggi.

- **Percentile 10%**: -36,38% → **0,05 $**
  - Percentile 10: se va molto male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 25%**: -31,62% → **0,05 $**
  - Percentile 25: se va male, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 50%**: -20,25% → **0,06 $**
  - Percentile 50: scenario normale. È il valore principale da guardare per il prezzo fra 30 giorni.
- **Percentile 75%**: -4,52% → **0,07 $**
  - Percentile 75: se va bene, fra 30 giorni il prezzo può stare circa in questa zona.
- **Percentile 90%**: 2,99% → **0,07 $**
  - Percentile 90: se va molto bene, fra 30 giorni il prezzo può arrivare circa in questa zona.

## Percentili drawdown — discesa durante i 30 giorni

**Drawdown** significa quanto può scendere il prezzo durante il mese, anche se poi recupera.

- **Percentile 10%**: -43,86% → **0,04 $**
  - Percentile 10: rischio molto brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona o peggio.
- **Percentile 25%**: -37,60% → **0,05 $**
  - Percentile 25: rischio brutto. Durante i 30 giorni il prezzo può scendere fino a questa zona.
- **Percentile 50%**: -28,61% → **0,05 $**
  - Percentile 50: discesa normale durante il mese. È il drawdown centrale.
- **Percentile 75%**: -13,56% → **0,06 $**
  - Percentile 75: discesa contenuta. Scenario abbastanza tranquillo.
- **Percentile 90%**: -5,34% → **0,07 $**
  - Percentile 90: discesa molto contenuta. Scenario molto tranquillo.

## Percentili max gain — rialzo durante i 30 giorni

**Max gain** significa il massimo rialzo che il prezzo può toccare durante il mese, anche solo temporaneamente.

- **Percentile 10%**: 0,00% → **0,07 $**
  - Percentile 10: rialzo scarso. Durante i 30 giorni il prezzo è salito poco.
- **Percentile 25%**: 0,73% → **0,07 $**
  - Percentile 25: rialzo modesto. Durante i 30 giorni il prezzo ha fatto poca strada verso l'alto.
- **Percentile 50%**: 4,88% → **0,08 $**
  - Percentile 50: rialzo normale. È lo spike centrale più realistico.
- **Percentile 75%**: 12,34% → **0,08 $**
  - Percentile 75: rialzo buono. Zona interessante per possibile take profit.
- **Percentile 90%**: 23,46% → **0,09 $**
  - Percentile 90: rialzo molto forte. Possibile, ma meno comune.

## Dati tecnici per controllo

Questa tabella serve solo per vedere quali vecchi pattern sono stati trovati. Non è obbligatorio leggerla ogni giorno.

| similar_asset   | start_date   | end_date   |   similarity |   return_30d |   drawdown_30d |   max_gain_30d |
|:----------------|:-------------|:-----------|-------------:|-------------:|---------------:|---------------:|
| DASH-USD        | 2022-02-20   | 2022-05-30 |        88.62 |       -29.45 |         -33.95 |           2.32 |
| NEAR-USD        | 2022-03-02   | 2022-06-09 |        88.5  |       -25.05 |         -39.1  |           0    |
| VET-USD         | 2022-02-22   | 2022-06-01 |        87.38 |       -27.52 |         -29    |           4.39 |
| QTUM-USD        | 2022-02-20   | 2022-05-30 |        87.29 |       -31.65 |         -37.87 |           0    |
| ZEC-USD         | 2019-05-17   | 2019-08-24 |        87.29 |       -11.71 |         -11.71 |           5.15 |
| XLM-USD         | 2019-09-29   | 2020-01-06 |        87.22 |        39.92 |          -5.54 |          39.92 |
| XRP-USD         | 2019-09-24   | 2020-01-01 |        86.82 |        24.17 |          -2.4  |          26.46 |
| 1INCH-USD       | 2022-02-22   | 2022-06-01 |        86.5  |       -31.62 |         -42.19 |           0    |
| OMG-USD         | 2022-02-20   | 2022-05-30 |        86.47 |       -32.46 |         -37.5  |           0    |
| CHZ-USD         | 2022-02-24   | 2022-06-03 |        86.12 |       -19.17 |         -28.71 |           5.97 |

<!-- CALIBRATION_READABLE_START -->

---

# Stato leggibile accuratezza / calibrazione

Report dettagliati:
- [accuracy_report.md](accuracy_report.md)
- [calibration_report.md](calibration_report.md)

## Riassunto semplice

- **BTC**: 0/30 previsioni controllate su 7 fatte. Stato: **RACCOLTA DATI**.
- **SOL**: 0/30 previsioni controllate su 7 fatte. Stato: **RACCOLTA DATI**.
- **DOGE**: 0/30 previsioni controllate su 7 fatte. Stato: **RACCOLTA DATI**.

| Asset | Previsioni fatte | Controllate | Progresso | In attesa | Stato | Prossimo controllo |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 7 | 0 | 0/30 [░░░░░░░░░░] | 7 | RACCOLTA DATI | 2026-08-02 / tra 24 giorni |
| SOL | 7 | 0 | 0/30 [░░░░░░░░░░] | 7 | RACCOLTA DATI | 2026-08-02 / tra 24 giorni |
| DOGE | 7 | 0 | 0/30 [░░░░░░░░░░] | 7 | RACCOLTA DATI | 2026-08-02 / tra 24 giorni |

## Traduzione

- **0/30** significa: lo scanner sta ancora raccogliendo dati.
- **30/30** significa: la calibrazione comincia ad attivarsi.
- **60+** significa: la calibrazione diventa più solida.
- L'email non c'entra con la calibrazione: conta solo che il workflow giri e salvi il diario delle previsioni.

<!-- CALIBRATION_READABLE_END -->

<!-- MODULE_ACCURACY_START -->
# Accuratezza moduli / autocalibrazione allargata

Generato: 2026-07-09 15:58 UTC

Questo report salva ogni giorno i segnali dei moduli e controlla, dopo vari orizzonti, quali moduli stanno davvero aiutando.

Moduli controllati:

- Global Confluence
- Scanner grezzo
- Market regime
- Struttura tecnica
- Frattale SOL/BTC, solo per SOL

Orizzonti controllati: 1, 3, 7, 14, 30 e 60 giorni.

Segnali totali salvati: **6**.

## Ultimi segnali salvati

| Data       | Asset   | Prezzo   |   Global |   Scanner |   Market |   Tecnico |   Frattale | Azione                                             |
|:-----------|:--------|:---------|---------:|----------:|---------:|----------:|-----------:|:---------------------------------------------------|
| 2026-07-09 | BTC     | 62818,14 |       +5 |        +3 |       +3 |        -2 |          0 | ACCUMULA SU PULLBACK / NO SHORT                    |
| 2026-07-09 | DOGE    | 0,07257  |       -9 |        -3 |       -3 |        -3 |          0 | STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE |
| 2026-07-09 | SOL     | 77,55    |       +5 |        -1 |       +2 |         0 |         +2 | HOLD / TRANCHE PICCOLE, NO LEVA                    |

## Stato controlli

| Asset   |   Segnali salvati |   1g controllati |   3g controllati |   7g controllati |   14g controllati |   30g controllati |   60g controllati |
|:--------|------------------:|-----------------:|-----------------:|-----------------:|------------------:|------------------:|------------------:|
| BTC     |                 2 |                1 |                0 |                0 |                 0 |                 0 |                 0 |
| SOL     |                 2 |                1 |                0 |                0 |                 0 |                 0 |                 0 |
| DOGE    |                 2 |                1 |                0 |                0 |                 0 |                 0 |                 0 |

## Accuratezza direzionale per modulo

| Asset   | Orizzonte   | Modulo            |   Controlli | Accuratezza direzione   | Return medio   | Drawdown medio   | Max gain medio   | Stato         |
|:--------|:------------|:------------------|------------:|:------------------------|:---------------|:-----------------|:-----------------|:--------------|
| BTC     | 1g          | Global confluence |           1 | 0,00%                   | 0,00%          | -0,02%           | 0,19%            | RACCOLTA DATI |
| BTC     | 1g          | Market regime     |           1 | 0,00%                   | 0,00%          | -0,02%           | 0,19%            | RACCOLTA DATI |
| BTC     | 1g          | Scanner           |           1 | 0,00%                   | 0,00%          | -0,02%           | 0,19%            | RACCOLTA DATI |
| BTC     | 1g          | Tecnico           |           1 | 0,00%                   | 0,00%          | -0,02%           | 0,19%            | RACCOLTA DATI |
| BTC     | 3g          | Global confluence |           0 | n/a                     | n/a            | n/a              | n/a              | RACCOLTA DATI |
| BTC     | 3g          | Market regime     |           0 | n/a                     | n/a            | n/a              | n/a              | RACCOLTA DATI |
| BTC     | 3g          | Scanner           |           0 | n/a                     | n/a            | n/a              | n/a              | RACCOLTA DATI |
| BTC     | 3g          | Tecnico           |           0 | n/a                     | n/a            | n/a              | n/a              | RACCOLTA DATI |
| BTC     | 7g          | Global confluence |           0 | n/a                     | n/a            | n/a              | n/a              | RACCOLTA DATI |
| BTC     | 7g          | Market regime     |           0 | n/a                     | n/a            | n/a              | n/a              | RACCOLTA DATI |
| BTC     | 7g          | Scanner           |           0 | n/a                     | n/a            | n/a              | n/a              | RACCOLTA DATI |
| BTC     | 7g          | Tecnico           |           0 | n/a                     | n/a            | n/a              | n/a              | RACCOLTA DATI |
| BTC     | 14g         | Global confluence |           0 | n/a                     | n/a            | n/a              | n/a              | RACCOLTA DATI |
| BTC     | 14g         | Market regime     |           0 | n/a                     | n/a            | n/a              | n/a              | RACCOLTA DATI |
| BTC     | 14g         | Scanner           |           0 | n/a                     | n/a            | n/a              | n/a              | RACCOLTA DATI |
| BTC     | 14g         | Tecnico           |           0 | n/a                     | n/a            | n/a              | n/a              | RACCOLTA DATI |
| BTC     | 30g         | Global confluence |           0 | n/a                     | n/a            | n/a              | n/a              | RACCOLTA DATI |
| BTC     | 30g         | Market regime     |           0 | n/a                     | n/a            | n/a              | n/a              | RACCOLTA DATI |
| BTC     | 30g         | Scanner           |           0 | n/a                     | n/a            | n/a              | n/a              | RACCOLTA DATI |
| BTC     | 30g         | Tecnico           |           0 | n/a                     | n/a            | n/a              | n/a              | RACCOLTA DATI |
| BTC     | 60g         | Global confluence |           0 | n/a                     | n/a            | n/a              | n/a              | RACCOLTA DATI |
| BTC     | 60g         | Market regime     |           0 | n/a                     | n/a            | n/a              | n/a              | RACCOLTA DATI |
| BTC     | 60g         | Scanner           |           0 | n/a                     | n/a            | n/a              | n/a              | RACCOLTA DATI |
| BTC     | 60g         | Tecnico           |           0 | n/a                     | n/a            | n/a              | n/a              | RACCOLTA DATI |
| DOGE    | 1g          | Global confluence |           1 | 0,00%                   | 0,00%          | 0,04%            | 0,29%            | RACCOLTA DATI |
| DOGE    | 1g          | Market regime     |           1 | 0,00%                   | 0,00%          | 0,04%            | 0,29%            | RACCOLTA DATI |
| DOGE    | 1g          | Scanner           |           1 | 0,00%                   | 0,00%          | 0,04%            | 0,29%            | RACCOLTA DATI |
| DOGE    | 1g          | Tecnico           |           1 | 0,00%                   | 0,00%          | 0,04%            | 0,29%            | RACCOLTA DATI |
| DOGE    | 3g          | Global confluence |           0 | n/a                     | n/a            | n/a              | n/a              | RACCOLTA DATI |
| DOGE    | 3g          | Market regime     |           0 | n/a                     | n/a            | n/a              | n/a              | RACCOLTA DATI |
| DOGE    | 3g          | Scanner           |           0 | n/a                     | n/a            | n/a              | n/a              | RACCOLTA DATI |
| DOGE    | 3g          | Tecnico           |           0 | n/a                     | n/a            | n/a              | n/a              | RACCOLTA DATI |
| DOGE    | 7g          | Global confluence |           0 | n/a                     | n/a            | n/a              | n/a              | RACCOLTA DATI |
| DOGE    | 7g          | Market regime     |           0 | n/a                     | n/a            | n/a              | n/a              | RACCOLTA DATI |
| DOGE    | 7g          | Scanner           |           0 | n/a                     | n/a            | n/a              | n/a              | RACCOLTA DATI |
| DOGE    | 7g          | Tecnico           |           0 | n/a                     | n/a            | n/a              | n/a              | RACCOLTA DATI |
| DOGE    | 14g         | Global confluence |           0 | n/a                     | n/a            | n/a              | n/a              | RACCOLTA DATI |
| DOGE    | 14g         | Market regime     |           0 | n/a                     | n/a            | n/a              | n/a              | RACCOLTA DATI |
| DOGE    | 14g         | Scanner           |           0 | n/a                     | n/a            | n/a              | n/a              | RACCOLTA DATI |
| DOGE    | 14g         | Tecnico           |           0 | n/a                     | n/a            | n/a              | n/a              | RACCOLTA DATI |
| DOGE    | 30g         | Global confluence |           0 | n/a                     | n/a            | n/a              | n/a              | RACCOLTA DATI |
| DOGE    | 30g         | Market regime     |           0 | n/a                     | n/a            | n/a              | n/a              | RACCOLTA DATI |
| DOGE    | 30g         | Scanner           |           0 | n/a                     | n/a            | n/a              | n/a              | RACCOLTA DATI |
| DOGE    | 30g         | Tecnico           |           0 | n/a                     | n/a            | n/a              | n/a              | RACCOLTA DATI |
| DOGE    | 60g         | Global confluence |           0 | n/a                     | n/a            | n/a              | n/a              | RACCOLTA DATI |
| DOGE    | 60g         | Market regime     |           0 | n/a                     | n/a            | n/a              | n/a              | RACCOLTA DATI |
| DOGE    | 60g         | Scanner           |           0 | n/a                     | n/a            | n/a              | n/a              | RACCOLTA DATI |
| DOGE    | 60g         | Tecnico           |           0 | n/a                     | n/a            | n/a              | n/a              | RACCOLTA DATI |
| SOL     | 1g          | Frattale SOL      |           1 | 0,00%                   | 0,00%          | -0,01%           | 0,29%            | RACCOLTA DATI |
| SOL     | 1g          | Global confluence |           1 | 0,00%                   | 0,00%          | -0,01%           | 0,29%            | RACCOLTA DATI |
| SOL     | 1g          | Market regime     |           1 | 0,00%                   | 0,00%          | -0,01%           | 0,29%            | RACCOLTA DATI |
| SOL     | 1g          | Scanner           |           1 | 0,00%                   | 0,00%          | -0,01%           | 0,29%            | RACCOLTA DATI |
| SOL     | 1g          | Tecnico           |           1 | 0,00%                   | 0,00%          | -0,01%           | 0,29%            | RACCOLTA DATI |
| SOL     | 3g          | Frattale SOL      |           0 | n/a                     | n/a            | n/a              | n/a              | RACCOLTA DATI |
| SOL     | 3g          | Global confluence |           0 | n/a                     | n/a            | n/a              | n/a              | RACCOLTA DATI |
| SOL     | 3g          | Market regime     |           0 | n/a                     | n/a            | n/a              | n/a              | RACCOLTA DATI |
| SOL     | 3g          | Scanner           |           0 | n/a                     | n/a            | n/a              | n/a              | RACCOLTA DATI |
| SOL     | 3g          | Tecnico           |           0 | n/a                     | n/a            | n/a              | n/a              | RACCOLTA DATI |
| SOL     | 7g          | Frattale SOL      |           0 | n/a                     | n/a            | n/a              | n/a              | RACCOLTA DATI |
| SOL     | 7g          | Global confluence |           0 | n/a                     | n/a            | n/a              | n/a              | RACCOLTA DATI |
| SOL     | 7g          | Market regime     |           0 | n/a                     | n/a            | n/a              | n/a              | RACCOLTA DATI |
| SOL     | 7g          | Scanner           |           0 | n/a                     | n/a            | n/a              | n/a              | RACCOLTA DATI |
| SOL     | 7g          | Tecnico           |           0 | n/a                     | n/a            | n/a              | n/a              | RACCOLTA DATI |
| SOL     | 14g         | Frattale SOL      |           0 | n/a                     | n/a            | n/a              | n/a              | RACCOLTA DATI |
| SOL     | 14g         | Global confluence |           0 | n/a                     | n/a            | n/a              | n/a              | RACCOLTA DATI |
| SOL     | 14g         | Market regime     |           0 | n/a                     | n/a            | n/a              | n/a              | RACCOLTA DATI |
| SOL     | 14g         | Scanner           |           0 | n/a                     | n/a            | n/a              | n/a              | RACCOLTA DATI |
| SOL     | 14g         | Tecnico           |           0 | n/a                     | n/a            | n/a              | n/a              | RACCOLTA DATI |
| SOL     | 30g         | Frattale SOL      |           0 | n/a                     | n/a            | n/a              | n/a              | RACCOLTA DATI |
| SOL     | 30g         | Global confluence |           0 | n/a                     | n/a            | n/a              | n/a              | RACCOLTA DATI |
| SOL     | 30g         | Market regime     |           0 | n/a                     | n/a            | n/a              | n/a              | RACCOLTA DATI |
| SOL     | 30g         | Scanner           |           0 | n/a                     | n/a            | n/a              | n/a              | RACCOLTA DATI |
| SOL     | 30g         | Tecnico           |           0 | n/a                     | n/a            | n/a              | n/a              | RACCOLTA DATI |
| SOL     | 60g         | Frattale SOL      |           0 | n/a                     | n/a            | n/a              | n/a              | RACCOLTA DATI |
| SOL     | 60g         | Global confluence |           0 | n/a                     | n/a            | n/a              | n/a              | RACCOLTA DATI |
| SOL     | 60g         | Market regime     |           0 | n/a                     | n/a            | n/a              | n/a              | RACCOLTA DATI |
| SOL     | 60g         | Scanner           |           0 | n/a                     | n/a            | n/a              | n/a              | RACCOLTA DATI |
| SOL     | 60g         | Tecnico           |           0 | n/a                     | n/a            | n/a              | n/a              | RACCOLTA DATI |

## Come leggerlo

- Prima di 30 controlli per asset/modulo, è solo raccolta dati.
- Dopo 30 controlli, il modulo può iniziare a dare una calibrazione leggera.
- Dopo 60 controlli, la lettura diventa più utile.
- Dopo 100+ controlli, i pesi dei moduli possono essere regolati con più fiducia.

Questo report non cambia ancora automaticamente i pesi del Global Confluence. Serve prima a capire quali moduli funzionano davvero.
<!-- MODULE_ACCURACY_END -->

<!-- GLOBAL_WEIGHT_CALIBRATION_START -->
# Calibrazione pesi Global Confluence

Report completo: [global_weight_calibration_report.md](global_weight_calibration_report.md)

Questo blocco controlla se, col tempo, i moduli del Global Confluence meritano più peso, meno peso o peso invariato.

| Asset   | Stato         |   Controlli max |   Moduli 60+ |   Moduli 100+ | Lettura                                       |
|:--------|:--------------|----------------:|-------------:|--------------:|:----------------------------------------------|
| BTC     | RACCOLTA DATI |               0 |            0 |             0 | troppi pochi controlli: non modificare i pesi |
| DOGE    | RACCOLTA DATI |               0 |            0 |             0 | troppi pochi controlli: non modificare i pesi |
| SOL     | RACCOLTA DATI |               0 |            0 |             0 | troppi pochi controlli: non modificare i pesi |

Regola: sotto 60 controlli il report osserva soltanto; da 100+ controlli può suggerire modifiche prudenti ai pesi.
<!-- GLOBAL_WEIGHT_CALIBRATION_END -->

<!-- RISK_CALIBRATION_START -->
# Calibrazione rischio spot / leva

Report completo: [risk_calibration_report.md](risk_calibration_report.md)

Questo blocco controlla se le zone di rischio previste dallo scanner vengono davvero toccate nei 30 giorni successivi.

| Asset   |   Snapshot |   Controlli 30g |   In attesa | Stato         | DD normale hit   | DD brutto hit   | DD molto brutto hit   | Bias rischio   |
|:--------|-----------:|----------------:|------------:|:--------------|:-----------------|:----------------|:----------------------|:---------------|
| BTC     |          1 |               0 |           1 | RACCOLTA DATI | n/a              | n/a             | n/a                   | n/a            |
| SOL     |          1 |               0 |           1 | RACCOLTA DATI | n/a              | n/a             | n/a                   | n/a            |
| DOGE    |          1 |               0 |           1 | RACCOLTA DATI | n/a              | n/a             | n/a                   | n/a            |

Regola: sotto 60 controlli osserva soltanto; da 100+ controlli può diventare utile per correggere rischio spot/leva nel Decision Report.

## Ultima lettura rapida

| Asset   | Rischio spot   | Rischio leva   | Nota leva                                                               |
|:--------|:---------------|:---------------|:------------------------------------------------------------------------|
| BTC     | BASSO          | MEDIO          | spot preferibile; leva molto pericolosa anche 2x/3x senza margine largo |
| SOL     | ALTO           | MOLTO ALTO     | spot preferibile; leva molto pericolosa anche 2x/3x senza margine largo |
| DOGE    | MOLTO ALTO     | MOLTO ALTO     | spot preferibile; leva molto pericolosa anche 2x/3x senza margine largo |
<!-- RISK_CALIBRATION_END -->

<!-- LIQUIDATION_SUMMARY_START -->

---

# Sintesi semplice futures / liquidazioni

Report separato completo: [liquidation_report.md](liquidation_report.md)

**BTC** — BTC: i futures sembrano più vulnerabili verso una discesa improvvisa. Non significa che deve scendere, ma se rompe sotto può accelerare. Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale.

**SOL** — SOL: i futures non danno una lettura chiara. Non si vede uno sbilanciamento forte né long né short. Qui pesa di più il report frattale.

**DOGE** — DOGE: i futures non danno una lettura chiara. Non si vede uno sbilanciamento forte né long né short. Qui pesa di più il report frattale.

| Asset | Prezzo | Funding | OI 24h | Long/Short | Lettura futures | Forza |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | $62,866 | +0.0034% | +7.96% | 2.14 | Rischio sotto | 5/5 |
| SOL | $77.59 | +0.0036% | -23.59% | 2.66 | Misto | 1/5 |
| DOGE | $0.07257 | -0.0009% | +1.54% | 3.11 | Misto | 1/5 |

## Come usarla insieme al frattale

- Frattale ribassista + futures con rischio sotto = prudenza alta.
- Frattale rialzista + futures con rischio sopra = segnale più interessante.
- Frattale e futures opposti = situazione sporca, meglio non forzare.
- Per posizioni a leva, il futures report serve soprattutto a capire se può arrivare una pulizia violenta prima dei 30 giorni.

<!-- LIQUIDATION_SUMMARY_END -->

<!-- FRACTAL_PATH_TRACKER_START -->
# Tracking percorso frattale SOL/BTC

Generato: 2026-07-09 15:57 UTC

Questo report controlla se SOL sta seguendo il percorso previsto dal frattale BTC 2022 vs SOL 2026.

Ora il controllo è diviso in quattro parti:

- confronto dal bottom: BTC 2022 scalato contro SOL reale
- tratto da inizio programma/scanner: verifica se il tracking recente sta reggendo
- proiezione futura giornaliera: BTC 2022 viene scalato giorno per giorno su SOL
- grafico gap: differenza leggibile tra SOL reale e BTC scalato

## Stato ultimo frattale salvato

- Data previsione: **2026-07-09**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC 2022 equivalente: **2022-11-21**
- Giorno BTC equivalente oggi: **2022-12-24**
- Inizio programma/scanner rilevato: **2026-07-03**
- Prezzo SOL corrente: **77,46 $**
- Verdetto: **n/a**
- Somiglianza: **n/a**
- Tracking: **n/a**
- Fase: **FASE ANTICIPATA**
- Rischio fase: **MEDIO / ALTO**

## Confronto dal bottom a oggi

- Giorni controllati dal bottom: **34**
- Giorni controllati da inizio programma/scanner: **7**
- Errore medio assoluto dal bottom: **9,27%**
- Errore medio assoluto ultimi 7 giorni: **21,79%**
- Errore medio assoluto da inizio programma/scanner: **21,79%**
- Errore ultimo giorno: **+16,71%**
- Stato: **DEVIAZIONE MODERATA**

## Grafico completo: bottom, inizio programma e proiezione giornaliera

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato - ultimi 60 giorni

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap: **+16,71%**
- Media mobile 7g gap: **+21,79%**
- Stato gap: **SOPRA FRATTALE / MOLTO IN ANTICIPO**
- Trend gap: **SOL si sta rafforzando rispetto al frattale**

Come leggerlo:

- **Sopra 0%** = SOL è sopra il percorso BTC scalato.
- **Sotto 0%** = SOL è sotto il percorso BTC scalato.
- Se il gap sale, SOL si sta rafforzando rispetto al frattale.
- Se il gap scende, SOL si sta indebolendo rispetto al frattale.
- Questo è il grafico più leggibile per capire subito se SOL si sta orientando sopra o sotto il frattale.

## Ultimi giorni del confronto dal bottom

|   Giorno | Data SOL   | Data BTC eq.   | SOL reale   | BTC scalato   | Errore   | Fase                |
|---------:|:-----------|:---------------|:------------|:--------------|:---------|:--------------------|
|       24 | 2026-06-30 | 2022-12-15     | 73,52 $     | 68,40 $       | +7,48%   | prima programma     |
|       25 | 2026-07-01 | 2022-12-16     | 77,38 $     | 65,58 $       | +18,00%  | prima programma     |
|       26 | 2026-07-02 | 2022-12-17     | 80,64 $     | 66,16 $       | +21,89%  | prima programma     |
|       27 | 2026-07-03 | 2022-12-18     | 82,28 $     | 66,01 $       | +24,64%  | da inizio programma |
|       28 | 2026-07-04 | 2022-12-19     | 81,65 $     | 64,76 $       | +26,08%  | da inizio programma |
|       29 | 2026-07-05 | 2022-12-20     | 81,42 $     | 66,60 $       | +22,26%  | da inizio programma |
|       30 | 2026-07-06 | 2022-12-21     | 81,92 $     | 66,25 $       | +23,65%  | da inizio programma |
|       31 | 2026-07-07 | 2022-12-22     | 80,65 $     | 66,30 $       | +21,64%  | da inizio programma |
|       32 | 2026-07-08 | 2022-12-23     | 77,79 $     | 66,17 $       | +17,56%  | da inizio programma |
|       33 | 2026-07-09 | 2022-12-24     | 77,46 $     | 66,37 $       | +16,71%  | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Base frattale   | Min percorso   | Max percorso   | Controllato   | Prezzo reale   | Errore   | Dentro banda   |
|:------------|:--------------|:----------------|:---------------|:---------------|:--------------|:---------------|:---------|:---------------|
| 7g          | 2026-07-16    | 76,08 $         | 76,08 $        | 77,79 $        | no            | n/a            | n/a      | n/a            |
| 14g         | 2026-07-23    | 77,95 $         | 76,08 $        | 77,95 $        | no            | n/a            | n/a      | n/a            |
| 30g         | 2026-08-08    | 105,44 $        | 76,08 $        | 105,44 $       | no            | n/a            | n/a      | n/a            |
| 60g         | 2026-09-07    | 111,21 $        | 76,08 $        | 114,16 $       | no            | n/a            | n/a      | n/a            |
| 90g         | 2026-10-07    | 126,40 $        | 76,08 $        | 130,27 $       | no            | n/a            | n/a      | n/a            |
| 120g        | 2026-11-06    | 126,86 $        | 76,08 $        | 140,16 $       | no            | n/a            | n/a      | n/a            |

Nota: la tabella sopra mostra solo le milestone principali. Il grafico invece usa la proiezione giornaliera del frattale BTC scalato su SOL.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda   | Errore medio assoluto   | Errore medio   |
|:------------|------------:|:---------------|:------------------------|:---------------|
| 7g          |           0 | n/a            | n/a                     | n/a            |
| 14g         |           0 | n/a            | n/a                     | n/a            |
| 30g         |           0 | n/a            | n/a                     | n/a            |
| 60g         |           0 | n/a            | n/a                     | n/a            |
| 90g         |           0 | n/a            | n/a                     | n/a            |
| 120g        |           0 | n/a            | n/a                     | n/a            |

## Come leggerlo

- BTC 2022 scalato su SOL è il percorso che SOL dovrebbe seguire se il frattale resta valido.
- SOL reale mostra cosa ha fatto davvero dal bottom.
- La linea di inizio programma/scanner separa il backtest retroattivo dalla parte che stiamo monitorando davvero giorno per giorno.
- Se SOL resta vicino a BTC scalato, il frattale è in linea.
- Se SOL sta sopra BTC scalato, il frattale è in anticipo o più forte.
- Se SOL sta sotto BTC scalato, il frattale è in ritardo o più debole.
- Il grafico gap ultimi 60 giorni serve proprio per vedere meglio questa differenza.
- La proiezione futura va letta insieme alle conferme e invalidazioni del report frattale principale.
<!-- FRACTAL_PATH_TRACKER_END -->

<!-- SOL_BTC_FRACTAL_HISTORY_START -->

---

# Storico frattale SOL/BTC

Per vedere la tabella giorno per giorno devi aprire/cliccare questo file:

**[sol_btc_fractal_history.md](sol_btc_fractal_history.md)**

Ultima lettura salvata: **2026-07-09** — SOL 77,46 $, gap +16,71%, somiglianza +73,81%.

Nel report principale lascio solo il link, così non diventa troppo lungo.

<!-- SOL_BTC_FRACTAL_HISTORY_END -->

<!-- MARKET_REGIME_MATCH_START -->
# Market Regime Match Report

Generated: 2026-07-09 15:58 UTC

This report adds market regime context to the raw fractal matches.

Main idea:

- A chart match during a bull market is not the same as a chart match during a bear market.
- This report separates matches by BTC regime and by similar-asset regime.
- The most useful group is SAME_BTC_AND_ASSET_REGIME, but only if it has enough matches.

## Current regime snapshot

| target   | target_regime_today   |   target_price | target_above_ma200   | target_return_90d   | target_ma200_slope_60d   | btc_regime_today   | btc_return_90d   | btc_ma200_slope_60d   |
|:---------|:----------------------|---------------:|:---------------------|:--------------------|:-------------------------|:-------------------|:-----------------|:----------------------|
| BTC-USD  | BEAR                  |       62779.9  | False                | -13.98%             | -10.28%                  | BEAR               | -13.98%          | -10.28%               |
| DOGE-USD | BEAR                  |           0.07 | False                | -22.64%             | -16.73%                  | BEAR               | -13.98%          | -10.28%               |
| SOL-USD  | BEAR                  |          77.51 | False                | -8.63%              | -18.86%                  | BEAR               | -13.98%          | -10.28%               |

## Summary by regime filter

| target   | group                     |   matches | positive_30d_rate   | return_30d_p50   | return_30d_p75   | return_30d_p90   | drawdown_30d_p50   | drawdown_30d_p10   | max_gain_30d_p50   | max_gain_30d_p75   | max_gain_30d_p90   | positive_60d_rate   | return_60d_p50   | return_60d_p75   | return_60d_p90   |
|:---------|:--------------------------|----------:|:--------------------|:-----------------|:-----------------|:-----------------|:-------------------|:-------------------|:-------------------|:-------------------|:-------------------|:--------------------|:-----------------|:-----------------|:-----------------|
| BTC-USD  | ALL_MATCHES               |        40 | 70.00%              | 6.89%            | 22.56%           | 43.75%           | -3.97%             | -32.41%            | 16.71%             | 32.64%             | 62.62%             | 72.50%              | 21.61%           | 45.40%           | 63.22%           |
| BTC-USD  | SAME_BTC_REGIME           |        18 | 94.44%              | 23.86%           | 40.45%           | 64.86%           | 0.00%              | -7.28%             | 34.09%             | 58.92%             | 68.90%             | 94.44%              | 41.68%           | 53.55%           | 93.67%           |
| BTC-USD  | SAME_ASSET_REGIME         |        30 | 76.67%              | 12.97%           | 25.32%           | 46.56%           | -2.89%             | -9.92%             | 18.35%             | 34.16%             | 62.73%             | 86.67%              | 30.82%           | 45.61%           | 69.24%           |
| BTC-USD  | SAME_BTC_AND_ASSET_REGIME |        16 | 93.75%              | 23.86%           | 34.59%           | 69.18%           | 0.00%              | -5.83%             | 34.09%             | 51.61%             | 72.07%             | 93.75%              | 36.92%           | 47.97%           | 97.66%           |
| DOGE-USD | ALL_MATCHES               |        40 | 12.50%              | -20.25%          | -4.52%           | 2.99%            | -28.61%            | -43.86%            | 4.88%              | 12.34%             | 23.46%             | 42.50%              | -8.19%           | 10.58%           | 21.93%           |
| DOGE-USD | SAME_BTC_REGIME           |        31 | 6.45%               | -26.97%          | -13.48%          | -2.33%           | -30.96%            | -44.75%            | 4.26%              | 9.33%              | 23.35%             | 41.94%              | -8.19%           | 9.13%            | 15.56%           |
| DOGE-USD | SAME_ASSET_REGIME         |        34 | 11.76%              | -24.71%          | -5.32%           | 0.71%            | -29.12%            | -44.46%            | 4.57%              | 11.79%             | 24.08%             | 44.12%              | -5.94%           | 12.10%           | 23.67%           |
| DOGE-USD | SAME_BTC_AND_ASSET_REGIME |        30 | 6.67%               | -27.25%          | -11.95%          | -2.27%           | -30.31%            | -44.76%            | 4.32%              | 9.83%              | 23.46%             | 40.00%              | -8.19%           | 9.20%            | 16.46%           |
| SOL-USD  | ALL_MATCHES               |        40 | 42.50%              | -1.54%           | 11.03%           | 43.75%           | -10.39%            | -30.98%            | 7.79%              | 22.56%             | 55.77%             | 52.50%              | 0.81%            | 24.48%           | 52.68%           |
| SOL-USD  | SAME_BTC_REGIME           |        24 | 62.50%              | 3.64%            | 19.32%           | 44.75%           | -5.08%             | -18.60%            | 15.09%             | 32.20%             | 60.31%             | 66.67%              | 10.13%           | 34.93%           | 53.48%           |
| SOL-USD  | SAME_ASSET_REGIME         |        28 | 50.00%              | 0.14%            | 15.66%           | 48.17%           | -7.71%             | -20.49%            | 11.22%             | 22.56%             | 57.28%             | 60.71%              | 6.46%            | 32.61%           | 51.71%           |
| SOL-USD  | SAME_BTC_AND_ASSET_REGIME |        19 | 63.16%              | 0.92%            | 21.98%           | 47.20%           | -6.43%             | -17.32%            | 14.92%             | 32.57%             | 56.53%             | 63.16%              | 6.95%            | 27.07%           | 47.02%           |

## Breakdown by historical BTC regime

| target   | group                       |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:----------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD  | HISTORICAL_BTC_BEAR         |        18 | 94.44%              | 23.86%           | 0.00%              | 58.92%             | 94.44%              | 41.68%           | 77.34%             |
| BTC-USD  | HISTORICAL_BTC_BULL         |         8 | 37.50%              | -11.59%          | -12.33%            | 9.57%              | 37.50%              | -14.20%          | 53.66%             |
| BTC-USD  | HISTORICAL_BTC_DISTRIBUTION |         9 | 66.67%              | 3.65%            | -5.75%             | 16.92%             | 100.00%             | 21.58%           | 73.78%             |
| BTC-USD  | HISTORICAL_BTC_RECOVERY     |         5 | 40.00%              | -3.60%           | -11.70%            | 16.38%             | 0.00%               | -24.31%          | 16.38%             |
| DOGE-USD | HISTORICAL_BTC_BEAR         |        31 | 6.45%               | -26.97%          | -30.96%            | 9.33%              | 41.94%              | -8.19%           | 18.89%             |
| DOGE-USD | HISTORICAL_BTC_BULL         |         3 | 33.33%              | -8.75%           | -14.04%            | 14.60%             | 33.33%              | -9.16%           | 15.40%             |
| DOGE-USD | HISTORICAL_BTC_DISTRIBUTION |         3 | 66.67%              | 18.71%           | -2.40%             | 23.10%             | 100.00%             | 21.64%           | 115.31%            |
| DOGE-USD | HISTORICAL_BTC_RECOVERY     |         3 | 0.00%               | -11.71%          | -11.71%            | 6.53%              | 0.00%               | -34.20%          | 6.53%              |
| SOL-USD  | HISTORICAL_BTC_BEAR         |        24 | 62.50%              | 3.64%            | -5.08%             | 32.20%             | 66.67%              | 10.13%           | 60.27%             |
| SOL-USD  | HISTORICAL_BTC_BULL         |         9 | 0.00%               | -10.79%          | -28.90%            | 1.50%              | 0.00%               | -7.77%           | 1.50%              |
| SOL-USD  | HISTORICAL_BTC_DISTRIBUTION |         5 | 40.00%              | -2.54%           | -7.18%             | 21.60%             | 100.00%             | 33.69%           | 80.74%             |
| SOL-USD  | HISTORICAL_BTC_RECOVERY     |         2 | 0.00%               | -16.77%          | -29.03%            | 11.14%             | 0.00%               | -35.08%          | 11.14%             |

## Breakdown by historical asset regime

| target   | group                         |   matches | positive_30d_rate   | return_30d_p50   | drawdown_30d_p50   | max_gain_30d_p75   | positive_60d_rate   | return_60d_p50   | max_gain_60d_p75   |
|:---------|:------------------------------|----------:|:--------------------|:-----------------|:-------------------|:-------------------|:--------------------|:-----------------|:-------------------|
| BTC-USD  | HISTORICAL_ASSET_BEAR         |        30 | 76.67%              | 12.97%           | -2.89%             | 34.16%             | 86.67%              | 30.82%           | 71.82%             |
| BTC-USD  | HISTORICAL_ASSET_BULL         |         3 | 0.00%               | -11.76%          | -12.91%            | 8.72%              | 0.00%               | -23.03%          | 8.72%              |
| BTC-USD  | HISTORICAL_ASSET_DISTRIBUTION |         1 | 100.00%             | 4.40%            | -3.37%             | 8.82%              | 100.00%             | 21.58%           | 33.10%             |
| BTC-USD  | HISTORICAL_ASSET_RECOVERY     |         6 | 66.67%              | 4.46%            | -10.12%            | 30.00%             | 33.33%              | -22.26%          | 65.67%             |
| DOGE-USD | HISTORICAL_ASSET_BEAR         |        34 | 11.76%              | -24.71%          | -29.12%            | 11.79%             | 44.12%              | -5.94%           | 24.30%             |
| DOGE-USD | HISTORICAL_ASSET_BULL         |         3 | 33.33%              | -12.18%          | -17.30%            | 8.26%              | 66.67%              | 5.41%            | 15.40%             |
| DOGE-USD | HISTORICAL_ASSET_MIXED        |         1 | 0.00%               | -8.75%           | -14.04%            | 12.94%             | 0.00%               | -9.16%           | 12.94%             |
| DOGE-USD | HISTORICAL_ASSET_RECOVERY     |         2 | 0.00%               | -6.05%           | -7.15%             | 7.22%              | 0.00%               | -24.95%          | 7.22%              |
| SOL-USD  | HISTORICAL_ASSET_BEAR         |        28 | 50.00%              | 0.14%            | -7.71%             | 22.56%             | 60.71%              | 6.46%            | 60.00%             |
| SOL-USD  | HISTORICAL_ASSET_BULL         |         4 | 0.00%               | -19.12%          | -29.62%            | 0.21%              | 25.00%              | -6.73%           | 0.21%              |
| SOL-USD  | HISTORICAL_ASSET_DISTRIBUTION |         2 | 0.00%               | -8.70%           | -29.28%            | 0.83%              | 0.00%               | -7.90%           | 0.83%              |
| SOL-USD  | HISTORICAL_ASSET_RECOVERY     |         6 | 50.00%              | 3.47%            | -17.29%            | 28.80%             | 50.00%              | 10.69%           | 67.73%             |

## Top regime-adjusted matches

The table below shows the top matches separately for each target, so BTC does not hide SOL and DOGE.

| target   | similar_asset   | start_date   | similarity   | btc_regime_at_match   | similar_asset_regime_at_match   | regime_alignment   | outcome_family   | return_30d   | drawdown_30d   | max_gain_30d   | return_60d   | drawdown_60d   | max_gain_60d   |
|:---------|:----------------|:-------------|:-------------|:----------------------|:--------------------------------|:-------------------|:-----------------|:-------------|:---------------|:---------------|:-------------|:---------------|:---------------|
| BTC-USD  | LRC-USD         | 2018-09-19   | 87.74%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | HIGH_SPIKE_60D   | 95.69%       | 0.00%          | 178.55%        | 42.97%       | 0.00%          | 178.55%        |
| BTC-USD  | KSM-USD         | 2022-03-10   | 86.22%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BULLISH_30D      | 11.02%       | -4.93%         | 16.96%         | 14.38%       | -4.93%         | 37.01%         |
| BTC-USD  | ONE-USD         | 2020-01-07   | 85.72%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BULLISH_30D      | 14.92%       | 0.00%          | 14.92%         | -3.06%       | -3.06%         | 19.26%         |
| BTC-USD  | XLM-USD         | 2020-01-07   | 84.84%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | EXPLOSIVE_60D    | 45.24%       | 0.00%          | 62.58%         | 53.88%       | 0.00%          | 78.05%         |
| BTC-USD  | MKR-USD         | 2021-07-21   | 84.83%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BULLISH_30D      | 29.66%       | -0.21%         | 38.63%         | 12.58%       | -6.23%         | 38.63%         |
| BTC-USD  | TRX-USD         | 2020-01-07   | 84.53%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BULLISH_30D      | 22.02%       | 0.00%          | 33.95%         | 32.98%       | 0.00%          | 48.70%         |
| BTC-USD  | OMG-USD         | 2020-01-07   | 84.50%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | EXPLOSIVE_60D    | 79.99%       | 0.00%          | 79.99%         | 195.80%      | 0.00%          | 253.59%        |
| BTC-USD  | ADA-USD         | 2020-01-07   | 84.27%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | EXPLOSIVE_60D    | 58.37%       | 0.00%          | 64.15%         | 140.87%      | 0.00%          | 179.32%        |
| BTC-USD  | QTUM-USD        | 2020-01-07   | 84.21%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BULLISH_30D      | 16.10%       | 0.00%          | 28.06%         | 33.45%       | 0.00%          | 45.51%         |
| BTC-USD  | SOL-USD         | 2022-03-10   | 84.14%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BULLISH_30D      | 25.70%       | 0.00%          | 37.70%         | 40.39%       | 0.00%          | 51.21%         |
| DOGE-USD | DASH-USD        | 2022-02-20   | 88.62%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BEARISH_30D      | -29.45%      | -33.95%        | 2.32%          | -19.38%      | -36.58%        | 2.32%          |
| DOGE-USD | VET-USD         | 2022-02-22   | 87.38%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BEARISH_30D      | -27.52%      | -29.00%        | 4.39%          | -11.12%      | -29.73%        | 4.39%          |
| DOGE-USD | QTUM-USD        | 2022-02-20   | 87.29%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BEARISH_30D      | -31.65%      | -37.87%        | 0.00%          | 12.26%       | -37.87%        | 12.26%         |
| DOGE-USD | XLM-USD         | 2019-09-29   | 87.22%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BULLISH_30D      | 39.92%       | -5.54%         | 39.92%         | 24.54%       | -5.54%         | 74.65%         |
| DOGE-USD | 1INCH-USD       | 2022-02-22   | 86.50%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BEARISH_30D      | -31.62%      | -42.19%        | 0.00%          | -20.09%      | -42.19%        | 0.00%          |
| DOGE-USD | OMG-USD         | 2022-02-20   | 86.47%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BEARISH_30D      | -32.46%      | -37.50%        | 0.00%          | -16.83%      | -40.22%        | 0.00%          |
| DOGE-USD | CHZ-USD         | 2022-02-24   | 86.12%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BEARISH_30D      | -19.17%      | -28.71%        | 5.97%          | 11.61%       | -28.71%        | 22.22%         |
| DOGE-USD | THETA-USD       | 2022-02-24   | 86.08%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | MIXED            | 1.59%        | -8.56%         | 23.35%         | 14.81%       | -8.85%         | 24.03%         |
| DOGE-USD | XTZ-USD         | 2025-12-06   | 85.91%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BEARISH_30D      | -10.41%      | -12.14%        | 4.26%          | -2.16%       | -12.14%        | 4.26%          |
| DOGE-USD | ENJ-USD         | 2022-02-25   | 85.77%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BEARISH_30D      | -16.55%      | -33.46%        | 5.00%          | 1.45%        | -33.46%        | 5.00%          |
| SOL-USD  | QTUM-USD        | 2018-09-19   | 79.52%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | MIXED            | -2.21%       | -3.68%         | 15.25%         | -0.51%       | -17.60%        | 15.25%         |
| SOL-USD  | TRX-USD         | 2018-09-19   | 79.00%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | BULLISH_30D      | 55.01%       | 0.00%          | 55.01%         | 32.25%       | 0.00%          | 58.38%         |
| SOL-USD  | LRC-USD         | 2018-09-19   | 78.44%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | HIGH_SPIKE_60D   | 95.69%       | 0.00%          | 178.55%        | 42.97%       | 0.00%          | 178.55%        |
| SOL-USD  | XLM-USD         | 2020-01-07   | 78.16%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | EXPLOSIVE_60D    | 45.24%       | 0.00%          | 62.58%         | 53.88%       | 0.00%          | 78.05%         |
| SOL-USD  | APT-USD         | 2024-09-01   | 77.73%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | MIXED            | 0.92%        | -11.47%        | 6.42%          | -34.40%      | -34.40%        | 6.42%          |
| SOL-USD  | NEAR-USD        | 2025-12-01   | 77.65%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | MIXED            | 6.36%        | -9.61%         | 16.07%         | 21.89%       | -9.61%         | 24.08%         |
| SOL-USD  | ENJ-USD         | 2018-09-19   | 77.19%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | EXPLOSIVE_60D    | -16.11%      | -19.37%        | 5.11%          | 93.16%       | -38.09%        | 93.16%         |
| SOL-USD  | SOL-USD         | 2025-12-04   | 76.85%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | MIXED            | -7.51%       | -10.44%        | 9.16%          | 6.95%        | -10.44%        | 10.43%         |
| SOL-USD  | XRP-USD         | 2020-01-07   | 76.31%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | MIXED            | 9.73%        | 0.00%          | 25.47%         | 5.71%        | 0.00%          | 25.47%         |
| SOL-USD  | OMG-USD         | 2025-12-01   | 75.77%       | BEAR                  | BEAR                            | SAME_BTC_AND_ASSET | MIXED            | -5.35%       | -7.41%         | 2.96%          | 13.31%       | -7.41%         | 15.03%         |

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

<!-- TECHNICAL_STRUCTURE_START -->
# Report struttura tecnica

Generato: 2026-07-09 15:58 UTC

Questo report aggiunge al tuo scanner una lettura classica di analisi tecnica.

Moduli inclusi:

- Struttura trend con MA20 / MA50 / MA200
- Massimi e minimi crescenti oppure decrescenti
- Doppio minimo, triplo minimo, doppio massimo, triplo massimo
- Pattern Adam and Eve Bottom / Top
- Divergenze RSI e divergenze RSI nascoste
- Momentum MACD
- Conferma volume con OBV / CMF
- Candidato fase Wyckoff
- Punteggio tecnico di confluenza

## Sintesi

| Asset   | Prezzo   |   Punteggio | Verdetto           | Trend            | Momentum        | Struttura                                             | Divergenza                         | Wyckoff                 | Supporto   | Resistenza   |
|:--------|:---------|------------:|:-------------------|:-----------------|:----------------|:------------------------------------------------------|:-----------------------------------|:------------------------|:-----------|:-------------|
| BTC     | 62.790   |          -3 | DEBOLE             | Trend ribassista | Momentum misto  | Struttura ribassista con massimi e minimi decrescenti | Divergenza rialzista RSI           | Possibile accumulazione | 57.748     | 65.544       |
| SOL     | 77,49    |          -1 | NEUTRALE / MISTO   | Trend misto      | Momentum misto  | Volatilità in espansione                              | Nessuna                            | Range / fase non chiara | 64,42      | 83,81        |
| DOGE    | 0.07251  |         -10 | RIBASSISTA TECNICO | Trend ribassista | Momentum debole | Struttura ribassista con massimi e minimi decrescenti | Divergenza ribassista nascosta RSI | Possibile accumulazione | 0.06961    | 0.07923      |

## Riepilogo pattern

| Asset   | Doppio minimo   | Triplo minimo   | Adam/Eve Bottom     | Doppio massimo   | Triplo massimo   | Adam/Eve Top     |   Punteggio pattern |
|:--------|:----------------|:----------------|:--------------------|:-----------------|:-----------------|:-----------------|--------------------:|
| BTC     | Possibile       | Possibile       | Adam and Eve Bottom | Confermato       | Confermato       | Eve and Adam Top |                  -4 |
| SOL     | Confermato      | Possibile       | Adam and Eve Bottom | Possibile        | Confermato       | Eve and Adam Top |                   1 |
| DOGE    | Assente         | Possibile       | Adam and Eve Bottom | Assente          | Confermato       | Eve and Adam Top |                  -4 |

## Indicatori tecnici

| Asset   |   RSI 14 |   Istogramma MACD | MA20    | MA50    | MA200   | Pendenza MA50 20g   | Pendenza MA200 60g   | Rendimento 30g   | Rendimento 90g   |
|:--------|---------:|------------------:|:--------|:--------|:--------|:--------------------|:---------------------|:-----------------|:-----------------|
| BTC     |    48.56 |         565.523   | 61.800  | 65.628  | 74.223  | -9,36%              | -10,12%              | 2,18%            | -14,05%          |
| SOL     |    53.31 |           0.50882 | 75,30   | 74,86   | 92,44   | -6,41%              | -18,53%              | 22,69%           | -8,78%           |
| DOGE    |    32.14 |           0.00043 | 0.07605 | 0.08580 | 0.10185 | -13,11%             | -16,44%              | -12,59%          | -22,13%          |

## Dettaglio asset

### BTC

- Prezzo: **62.790**
- Punteggio tecnico: **-3 / 12**
- Verdetto: **DEBOLE**
- Trend: **Trend ribassista** (-3)
- Momentum: **Momentum misto** (1)
- Volume: **Volume da accumulazione** (2)
- Struttura: **Struttura ribassista con massimi e minimi decrescenti** (-2)
  - Dettaglio struttura: Ultimi minimi: 5.808e+04 -> 5.775e+04. Ultimi massimi: 6.725e+04 -> 6.554e+04.
- Divergenza: **Divergenza rialzista RSI** (2)
- Fase Wyckoff candidata: **Possibile accumulazione** (1)
  - Dettaglio Wyckoff: Prezzo sotto MA200, vicino alla parte bassa del range a 120 giorni, RSI 48.6.
- Supporto più vicino: **57.748**
- Resistenza più vicina: **65.544**

Pattern classici:

- Doppio minimo: **Possibile**
  - Due minimi simili vicino a 57.748 tra 2026-06-05 e 2026-07-01. Neckline stimata: 67.248.
- Triplo minimo: **Possibile**
  - Tre minimi simili vicino a 57.748 dal 2026-06-05 al 2026-07-01. Neckline stimata: 67.248.
- Adam/Eve Bottom: **Adam and Eve Bottom**
  - Possibile pattern Adam and Eve Bottom vicino a 62.201 dal 2026-03-29 al 2026-06-18. Nel modello Adam/Eve un minimo è più appuntito e violento, l'altro è più arrotondato. Neckline stimata: 82.792.
- Doppio massimo: **Confermato**
  - Due massimi simili vicino a 79.488 tra 2026-04-27 e 2026-05-26. Neckline ribassista stimata: 74.959.
- Triplo massimo: **Confermato**
  - Tre massimi simili vicino a 79.468 dal 2026-04-17 al 2026-05-26. Neckline ribassista stimata: 74.959.
- Adam/Eve Top: **Eve and Adam Top**
  - Possibile pattern Eve and Adam Top vicino a 82.792 dal 2026-04-22 al 2026-05-06. Nel modello Adam/Eve un massimo è più appuntito e violento, l'altro è più arrotondato. Neckline ribassista stimata: 74.959.

### SOL

- Prezzo: **77,49**
- Punteggio tecnico: **-1 / 12**
- Verdetto: **NEUTRALE / MISTO**
- Trend: **Trend misto** (-1)
- Momentum: **Momentum misto** (-1)
- Volume: **Volume neutrale** (0)
- Struttura: **Volatilità in espansione** (0)
  - Dettaglio struttura: Ultimi minimi: 67.92 -> 64.42. Ultimi massimi: 74.89 -> 83.81.
- Divergenza: **Nessuna** (0)
- Fase Wyckoff candidata: **Range / fase non chiara** (0)
  - Dettaglio Wyckoff: Posizione nel range a 120 giorni: 45,11%. Fase non abbastanza chiara.
- Supporto più vicino: **64,42**
- Resistenza più vicina: **83,81**

Pattern classici:

- Doppio minimo: **Confermato**
  - Due minimi simili vicino a 60,41 tra 2026-06-06 e 2026-06-25. Neckline stimata: 75,94.
- Triplo minimo: **Possibile**
  - Tre minimi simili vicino a 81,41 dal 2026-04-12 al 2026-05-23. Neckline stimata: 98,27.
- Adam/Eve Bottom: **Adam and Eve Bottom**
  - Possibile pattern Adam and Eve Bottom vicino a 60,41 dal 2026-06-06 al 2026-06-25. Nel modello Adam/Eve un minimo è più appuntito e violento, l'altro è più arrotondato. Neckline stimata: 75,94.
- Doppio massimo: **Possibile**
  - Due massimi simili vicino a 87,79 tra 2026-05-21 e 2026-07-04. Neckline ribassista stimata: 60,41.
- Triplo massimo: **Confermato**
  - Tre massimi simili vicino a 89,26 dal 2026-04-22 al 2026-05-21. Neckline ribassista stimata: 81,63.
- Adam/Eve Top: **Eve and Adam Top**
  - Possibile pattern Eve and Adam Top vicino a 88,05 dal 2026-04-27 al 2026-07-04. Nel modello Adam/Eve un massimo è più appuntito e violento, l'altro è più arrotondato. Neckline ribassista stimata: 60,41.

### DOGE

- Prezzo: **0.07251**
- Punteggio tecnico: **-10 / 12**
- Verdetto: **RIBASSISTA TECNICO**
- Trend: **Trend ribassista** (-3)
- Momentum: **Momentum debole** (-2)
- Volume: **Volume da accumulazione** (1)
- Struttura: **Struttura ribassista con massimi e minimi decrescenti** (-2)
  - Dettaglio struttura: Ultimi minimi: 0.07809 -> 0.06961. Ultimi massimi: 0.09169 -> 0.07923.
- Divergenza: **Divergenza ribassista nascosta RSI** (-1)
- Fase Wyckoff candidata: **Possibile accumulazione** (1)
  - Dettaglio Wyckoff: Prezzo sotto MA200, vicino alla parte bassa del range a 120 giorni, RSI 32.1.
- Supporto più vicino: **0.06961**
- Resistenza più vicina: **0.07923**

Pattern classici:

- Doppio minimo: **Assente**
- Triplo minimo: **Possibile**
  - Tre minimi simili vicino a 0.09274 dal 2026-04-19 al 2026-05-28. Neckline stimata: 0.11825.
- Adam/Eve Bottom: **Adam and Eve Bottom**
  - Possibile pattern Adam and Eve Bottom vicino a 0.09274 dal 2026-04-19 al 2026-05-23. Nel modello Adam/Eve un minimo è più appuntito e violento, l'altro è più arrotondato. Neckline stimata: 0.11825.
- Doppio massimo: **Assente**
- Triplo massimo: **Confermato**
  - Tre massimi simili vicino a 0.10200 dal 2026-03-25 al 2026-04-17. Neckline ribassista stimata: 0.08862.
- Adam/Eve Top: **Eve and Adam Top**
  - Possibile pattern Eve and Adam Top vicino a 0.09584 dal 2026-04-07 al 2026-06-12. Nel modello Adam/Eve un massimo è più appuntito e violento, l'altro è più arrotondato. Neckline ribassista stimata: 0.07809.

## Come leggere il punteggio

- Da +7 a +12: forte confluenza tecnica rialzista.
- Da +3 a +6: struttura costruttiva, ma serve ancora conferma.
- Da -2 a +2: situazione mista / neutrale.
- Da -6 a -3: struttura tecnica debole.
- Da -12 a -7: forte confluenza tecnica ribassista.

Nota importante: questo report non è una previsione da solo. È un filtro tecnico da leggere insieme a scanner frattale, market regime, futures e RSI.
<!-- TECHNICAL_STRUCTURE_END -->
