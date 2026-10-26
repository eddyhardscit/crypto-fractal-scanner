<!-- SCANNER_FORECAST_TRACKER_START -->
# Scanner forecast path / cono probabilistico

Generato: 2026-10-26 06:32:59 UTC

## Snapshot effettivamente usato

| Asset   | Snapshot prezzo   | Generazione snapshot prezzo   | Snapshot match scanner   |
|:--------|:------------------|:------------------------------|:-------------------------|
| BTC | 2026-10-26 | 2026-10-26T06:30:21Z | 2026-10-26 06:30:22 |
| SOL | 2026-10-26 | 2026-10-26T06:30:21Z | 2026-10-26 06:30:22 |
| DOGE | 2026-10-26 | 2026-10-26T06:30:21Z | 2026-10-26 06:30:22 |

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
| BTC | 2026-10-26 | 79.856 $ | INCERTO | 47,50% | 64.491,49 $ | 71.820,44 $ | 79.608,96 $ | 89.996,40 $ | 105.949,97 $ |
| SOL | 2026-10-26 | 100,60 $ | INCERTO | 50,00% | 90,61 $ | 95,88 $ | 100,91 $ | 115,70 $ | 127,10 $ |
| DOGE | 2026-10-26 | 0.07658 $ | INCERTO | 47,50% | 0.06757 $ | 0.07325 $ | 0.07638 $ | 0.08680 $ | 0.11127 $ |

## Confronto raw / regime-adjusted

Il cono raw continua a usare i 40 casi dello scanner. Il cono regime-adjusted sceglie una sola coorte nella gerarchia SAME_BTC_AND_ASSET_REGIME → SAME_ASSET_REGIME → SAME_BTC_REGIME. Ogni livello richiede almeno 5 match; le coorti non vengono mai combinate e ogni fallback è dichiarato.

| Asset   | Stato adjusted              | selected_regime_group     |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level      | selection_reason            | Raw p50 30g   | Adjusted p50 30g   | Raw p90 30g   | Adjusted p90 30g   |
|:--------|:----------------------------|:--------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:--------------------|:----------------------------|:--------------|:-------------------|:--------------|:-------------------|
| BTC | AVAILABLE | SAME_BTC_REGIME | 2 | 3 | 10 | 10 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME | 79.608,96 $ | 74.046,45 $ | 105.949,97 $ | 116.644,91 $ |
| SOL | AVAILABLE | SAME_BTC_AND_ASSET_REGIME | 5 | 6 | 12 | 5 | 5 | 0_FULL_REGIME | FULL_REGIME_THRESHOLD_MET | 100,91 $ | 99,42 $ | 127,10 $ | 113,44 $ |
| DOGE | INSUFFICIENT_REGIME_MATCHES | NONE | 1 | 1 | 4 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES | 0.07638 $ | n/a | 0.11127 $ | n/a |

## Grafici

### BTC

![Scanner forecast BTC](scanner_forecast_BTC.png)

#### Verifica storica e discrepanza

![Verifica storica cono BTC](scanner_forecast_history_BTC.png)

- Cono congelato il **2026-09-26**; verificato fino al **2026-10-26**; stato **COMPLETO 30/30g**.
- Reale **79.920,05 $**; p50 previsto **82.488,67 $**; scarto **-3,11%**.
- Errore medio assoluto **4,68%**; massimo **12,71%**; DENTRO p10-p90; DENTRO p25-p75.

#### Cono regime-adjusted

Gruppo selezionato: **SAME_BTC_REGIME**; fallback: **2_SAME_BTC_FALLBACK**; motivo: **FALLBACK_TO_SAME_BTC_REGIME**.

**WARNING:** coorte fallback meno stringente rispetto a SAME_BTC_AND_ASSET_REGIME.

![Scanner forecast regime-adjusted BTC](scanner_forecast_BTC_regime_adjusted.png)

### SOL

![Scanner forecast SOL](scanner_forecast_SOL.png)

<!-- SOL_CONDITIONAL_ANALYSES_START -->
#### SOL — Analisi condizionata -5% → +10%

Queste analisi sono **separate dal cono SOL originale**. Il cono sopra continua a usare normalmente i **40 analoghi più simili a SOL**.

Il filtro condizionato parte proprio da quei 40 casi e conserva soltanto gli episodi che hanno toccato **prima -5%** dal proprio baseline e **successivamente +10% entro 30 giorni**.

##### A. Conditional Successor corrente — dinamico

Questo campione viene ricostruito ad ogni run dai **40 analoghi SOL correnti**. Di conseguenza il numero di episodi qualificati e gli asset possono cambiare giorno per giorno.

**Campione corrente:** 16 episodi qualificati su 40 · 14 asset distinti.

![SOL conditional successor corrente](scanner_forecast_SOL_conditional_successor_current.png)

###### Confronto diretto a 30 giorni

| Modello | Vintage | N | Target | P10 | P25 | P50 | P75 | P90 |
| --- | --- | ---: | --- | ---: | ---: | ---: | ---: | ---: |
| Cono standard | 2026-10-26 | 40 | 2026-11-25 | 90.61 $ | 95.88 $ | 100.91 $ | 115.70 $ | 127.10 $ |
| Conditional corrente | 2026-10-26 | 16 | 2026-11-25 | 75.27 $ | 82.03 $ | 90.05 $ | 126.03 $ | 141.39 $ |

###### Struttura successiva dei casi correnti

| Classe | Episodi | Frequenza empirica |
| --- | ---: | ---: |
| DIRECT_CONTINUATION | 4 | 25.00% |
| SHALLOW_PULLBACK_THEN_CONTINUATION | 2 | 12.50% |
| DEEP_PULLBACK_THEN_RECOVERY | 1 | 6.25% |
| FAILURE | 9 | 56.25% |
| UNRESOLVED | 0 | 0.00% |

###### Episodi qualificati oggi

| Asset | Match window | -5% hit | +10% anchor | Classe 60d |
| --- | --- | --- | --- | --- |
| ZEC-USD | 2024-06-09 → 2024-09-16 | 2024-10-01 | 2024-10-10 | DIRECT_CONTINUATION |
| AVAX-USD | 2021-07-16 → 2021-10-23 | 2021-10-27 | 2021-11-03 | DIRECT_CONTINUATION |
| MKR-USD | 2020-12-03 → 2021-03-12 | 2021-03-15 | 2021-04-02 | FAILURE |
| ENJ-USD | 2022-12-12 → 2023-03-21 | 2023-03-22 | 2023-04-07 | FAILURE |
| LRC-USD | 2020-12-02 → 2021-03-11 | 2021-03-12 | 2021-03-17 | FAILURE |
| CRV-USD | 2022-12-11 → 2023-03-20 | 2023-03-24 | 2023-04-13 | FAILURE |
| VET-USD | 2022-12-14 → 2023-03-23 | 2023-03-27 | 2023-04-16 | FAILURE |
| MKR-USD | 2019-01-13 → 2019-04-22 | 2019-04-24 | 2019-05-15 | FAILURE |
| HBAR-USD | 2022-12-09 → 2023-03-18 | 2023-03-27 | 2023-03-29 | FAILURE |
| AVAX-USD | 2023-10-09 → 2024-01-16 | 2024-01-18 | 2024-02-10 | DEEP_PULLBACK_THEN_RECOVERY |
| BAT-USD | 2022-12-12 → 2023-03-21 | 2023-03-22 | 2023-04-01 | FAILURE |
| ZIL-USD | 2022-12-09 → 2023-03-18 | 2023-03-25 | 2023-04-01 | SHALLOW_PULLBACK_THEN_CONTINUATION |
| ICP-USD | 2022-12-10 → 2023-03-19 | 2023-03-20 | 2023-04-16 | DIRECT_CONTINUATION |
| ETH-USD | 2020-12-02 → 2021-03-11 | 2021-03-22 | 2021-04-02 | SHALLOW_PULLBACK_THEN_CONTINUATION |
| FIL-USD | 2022-12-11 → 2023-03-20 | 2023-03-25 | 2023-04-15 | FAILURE |
| TRX-USD | 2021-07-05 → 2021-10-12 | 2021-10-27 | 2021-11-02 | DIRECT_CONTINUATION |

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

- Ultimo close disponibile: **2026-10-18** · SOL **104.02 $**.
- Giorno del vintage: **30/30**.
- P50 condizionato previsto per quel giorno: **168.54 $**.
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

- Cono congelato il **2026-09-26**; verificato fino al **2026-10-26**; stato **COMPLETO 30/30g**.
- Reale **100,69 $**; p50 previsto **110,91 $**; scarto **-9,21%**.
- Errore medio assoluto **6,92%**; massimo **14,56%**; DENTRO p10-p90; DENTRO p25-p75.

#### Cono regime-adjusted

Gruppo selezionato: **SAME_BTC_AND_ASSET_REGIME**; fallback: **0_FULL_REGIME**; motivo: **FULL_REGIME_THRESHOLD_MET**.

![Scanner forecast regime-adjusted SOL](scanner_forecast_SOL_regime_adjusted.png)

### DOGE

![Scanner forecast DOGE](scanner_forecast_DOGE.png)

#### Verifica storica e discrepanza

![Verifica storica cono DOGE](scanner_forecast_history_DOGE.png)

- Cono congelato il **2026-09-26**; verificato fino al **2026-10-26**; stato **COMPLETO 30/30g**.
- Reale **0.07674 $**; p50 previsto **0.09179 $**; scarto **-16,40%**.
- Errore medio assoluto **5,86%**; massimo **16,40%**; DENTRO p10-p90; FUORI p25-p75.

#### Cono regime-adjusted

Gruppo selezionato: **NONE**; fallback: **NONE**; motivo: **INSUFFICIENT_REGIME_MATCHES**.

Non disponibile: INSUFFICIENT_REGIME_MATCHES (campione selezionato 0/5 match).

## Accuratezza percorso scanner

| Asset   | Giorno   |   Controlli | Dentro p10-p90   | Dentro p25-p75   | Errore medio abs vs p50   | Errore medio vs p50   |
|:--------|:---------|------------:|:-----------------|:-----------------|:--------------------------|:----------------------|
| BTC | 1g | 99 | 94,95% | 73,74% | 1,83% | 0,15% |
| BTC | 3g | 95 | 94,74% | 78,95% | 2,94% | 0,40% |
| BTC | 7g | 87 | 94,25% | 72,41% | 4,65% | 0,69% |
| BTC | 14g | 74 | 98,65% | 79,73% | 5,69% | -0,08% |
| BTC | 30g | 45 | 100,00% | 68,89% | 11,92% | -5,37% |
| SOL | 1g | 99 | 86,87% | 65,66% | 2,56% | 0,35% |
| SOL | 3g | 95 | 92,63% | 72,63% | 3,83% | 0,83% |
| SOL | 7g | 87 | 93,10% | 71,26% | 5,88% | 1,40% |
| SOL | 14g | 74 | 90,54% | 68,92% | 8,51% | 2,64% |
| SOL | 30g | 45 | 95,56% | 73,33% | 14,57% | 2,52% |
| DOGE | 1g | 99 | 89,90% | 62,63% | 2,94% | 0,05% |
| DOGE | 3g | 95 | 92,63% | 61,05% | 4,67% | 0,39% |
| DOGE | 7g | 87 | 78,16% | 67,82% | 8,49% | 2,79% |
| DOGE | 14g | 74 | 83,78% | 48,65% | 10,57% | 5,01% |
| DOGE | 30g | 45 | 95,56% | 42,22% | 16,00% | 13,05% |

## Tail / outlier audit

I casi di coda restano nel calcolo. L'audit leave-one-out quantifica la sensibilità dei percentili senza trasformare l'analisi in un filtro discrezionale.

Dettaglio completo: [scanner_forecast_tail_outlier_audit.md](scanner_forecast_tail_outlier_audit.md).

## Calibratore shadow

Il cono ufficiale resta grezzo e invariato. Il calibratore usa soltanto previsioni passate già mature, campionate una volta a settimana per ridurre la falsa indipendenza. Ogni orizzonte si attiva a 30 controlli indipendenti: parte al 25% della correzione stimata e cresce gradualmente fino al 100% a 100 controlli.

| Asset   | Orizzonte   |   Controlli indipendenti |   Soglia | Stato                  | Forza correzione   | Shift p50   |   Scala p10-p90 |
|:--------|:------------|-------------------------:|---------:|:-----------------------|:-------------------|:------------|----------------:|
| BTC | 1g | 16 | 30 | RACCOLTA (14 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 3g | 16 | 30 | RACCOLTA (14 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 7g | 16 | 30 | RACCOLTA (14 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 14g | 15 | 30 | RACCOLTA (15 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 30g | 12 | 30 | RACCOLTA (18 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 1g | 16 | 30 | RACCOLTA (14 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 3g | 16 | 30 | RACCOLTA (14 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 7g | 16 | 30 | RACCOLTA (14 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 14g | 15 | 30 | RACCOLTA (15 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 30g | 12 | 30 | RACCOLTA (18 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 1g | 16 | 30 | RACCOLTA (14 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 3g | 16 | 30 | RACCOLTA (14 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 7g | 16 | 30 | RACCOLTA (14 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 14g | 15 | 30 | RACCOLTA (15 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 30g | 12 | 30 | RACCOLTA (18 mancanti) | 0,0% | 0,00% | 1,000 |

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