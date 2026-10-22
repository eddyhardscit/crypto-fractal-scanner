<!-- SCANNER_FORECAST_TRACKER_START -->
# Scanner forecast path / cono probabilistico

Generato: 2026-10-22 05:33:01 UTC

## Snapshot effettivamente usato

| Asset   | Snapshot prezzo   | Generazione snapshot prezzo   | Snapshot match scanner   |
|:--------|:------------------|:------------------------------|:-------------------------|
| BTC | 2026-10-22 | 2026-10-22T05:30:21Z | 2026-10-22 05:30:22 |
| SOL | 2026-10-22 | 2026-10-22T05:30:21Z | 2026-10-22 05:30:22 |
| DOGE | 2026-10-22 | 2026-10-22T05:30:21Z | 2026-10-22 05:30:22 |

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
| BTC | 2026-10-22 | 82.837 $ | SALITA | 62,50% | 65.933,25 $ | 70.518,59 $ | 87.089,03 $ | 101.203,12 $ | 105.859,81 $ |
| SOL | 2026-10-22 | 105,19 $ | SALITA | 72,50% | 81,50 $ | 104,27 $ | 111,50 $ | 122,11 $ | 135,91 $ |
| DOGE | 2026-10-22 | 0.08008 $ | SALITA | 80,00% | 0.07039 $ | 0.08084 $ | 0.08777 $ | 0.09783 $ | 0.11196 $ |

## Confronto raw / regime-adjusted

Il cono raw continua a usare i 40 casi dello scanner. Il cono regime-adjusted sceglie una sola coorte nella gerarchia SAME_BTC_AND_ASSET_REGIME → SAME_ASSET_REGIME → SAME_BTC_REGIME. Ogni livello richiede almeno 5 match; le coorti non vengono mai combinate e ogni fallback è dichiarato.

| Asset   | Stato adjusted              | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level      | selection_reason            | Raw p50 30g   | Adjusted p50 30g   | Raw p90 30g   | Adjusted p90 30g   |
|:--------|:----------------------------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:--------------------|:----------------------------|:--------------|:-------------------|:--------------|:-------------------|
| BTC | AVAILABLE | SAME_BTC_REGIME | 2 | 2 | 11 | 11 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME | 87.089,03 $ | 83.566,29 $ | 105.859,81 $ | 105.522,01 $ |
| SOL | AVAILABLE | SAME_BTC_REGIME | 4 | 4 | 13 | 13 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME | 111,50 $ | 106,12 $ | 135,91 $ | 148,42 $ |
| DOGE | INSUFFICIENT_REGIME_MATCHES | NONE | 0 | 1 | 3 | 0 | 5 | NONE | INSUFFICIENT_REGIME_MATCHES | 0.08777 $ | n/a | 0.11196 $ | n/a |

## Grafici

### BTC

![Scanner forecast BTC](scanner_forecast_BTC.png)

#### Verifica storica e discrepanza

![Verifica storica cono BTC](scanner_forecast_history_BTC.png)

- Cono congelato il **2026-09-22**; verificato fino al **2026-10-22**; stato **COMPLETO 30/30g**.
- Reale **82.749,18 $**; p50 previsto **96.162,99 $**; scarto **-13,95%**.
- Errore medio assoluto **9,90%**; massimo **19,64%**; DENTRO p10-p90; DENTRO p25-p75.

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

**Campione corrente:** 12 episodi qualificati su 40 · 11 asset distinti.

![SOL conditional successor corrente](scanner_forecast_SOL_conditional_successor_current.png)

###### Confronto diretto a 30 giorni

| Modello | Vintage | N | Target | P10 | P25 | P50 | P75 | P90 |
| --- | --- | ---: | --- | ---: | ---: | ---: | ---: | ---: |
| Cono standard | 2026-10-22 | 40 | 2026-11-21 | 81.50 $ | 104.27 $ | 111.50 $ | 122.11 $ | 135.91 $ |
| Conditional corrente | 2026-10-22 | 12 | 2026-11-21 | 76.59 $ | 88.27 $ | 98.37 $ | 116.31 $ | 201.21 $ |

###### Struttura successiva dei casi correnti

| Classe | Episodi | Frequenza empirica |
| --- | ---: | ---: |
| DIRECT_CONTINUATION | 4 | 33.33% |
| SHALLOW_PULLBACK_THEN_CONTINUATION | 0 | 0.00% |
| DEEP_PULLBACK_THEN_RECOVERY | 0 | 0.00% |
| FAILURE | 8 | 66.67% |
| UNRESOLVED | 0 | 0.00% |

###### Episodi qualificati oggi

| Asset | Match window | -5% hit | +10% anchor | Classe 60d |
| --- | --- | --- | --- | --- |
| MKR-USD | 2020-11-28 → 2021-03-07 | 2021-03-14 | 2021-04-02 | FAILURE |
| ZEC-USD | 2024-06-04 → 2024-09-11 | 2024-09-30 | 2024-10-10 | DIRECT_CONTINUATION |
| MKR-USD | 2019-01-13 → 2019-04-22 | 2019-04-24 | 2019-05-15 | FAILURE |
| ENJ-USD | 2022-12-07 → 2023-03-16 | 2023-03-27 | 2023-04-07 | FAILURE |
| DOGE-USD | 2024-01-21 → 2024-04-29 | 2024-04-30 | 2024-05-04 | FAILURE |
| TRX-USD | 2021-06-30 → 2021-10-07 | 2021-10-27 | 2021-11-02 | DIRECT_CONTINUATION |
| HBAR-USD | 2022-12-09 → 2023-03-18 | 2023-03-27 | 2023-03-29 | FAILURE |
| DASH-USD | 2019-12-03 → 2020-03-11 | 2020-03-12 | 2020-04-09 | FAILURE |
| ICP-USD | 2022-12-10 → 2023-03-19 | 2023-03-20 | 2023-04-16 | DIRECT_CONTINUATION |
| RUNE-USD | 2023-07-06 → 2023-10-13 | 2023-10-17 | 2023-10-22 | DIRECT_CONTINUATION |
| 1INCH-USD | 2022-12-09 → 2023-03-18 | 2023-03-27 | 2023-04-16 | FAILURE |
| FIL-USD | 2022-12-11 → 2023-03-20 | 2023-03-25 | 2023-04-15 | FAILURE |

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

- Cono congelato il **2026-09-22**; verificato fino al **2026-10-22**; stato **COMPLETO 30/30g**.
- Reale **105,06 $**; p50 previsto **121,93 $**; scarto **-13,84%**.
- Errore medio assoluto **5,39%**; massimo **15,74%**; DENTRO p10-p90; DENTRO p25-p75.

#### Cono regime-adjusted

Gruppo selezionato: **SAME_BTC_REGIME**; fallback: **2_SAME_BTC_FALLBACK**; motivo: **FALLBACK_TO_SAME_BTC_REGIME**.

**WARNING:** coorte fallback meno stringente rispetto a SAME_BTC_AND_ASSET_REGIME.

![Scanner forecast regime-adjusted SOL](scanner_forecast_SOL_regime_adjusted.png)

### DOGE

![Scanner forecast DOGE](scanner_forecast_DOGE.png)

#### Verifica storica e discrepanza

![Verifica storica cono DOGE](scanner_forecast_history_DOGE.png)

- Cono congelato il **2026-09-22**; verificato fino al **2026-10-22**; stato **COMPLETO 30/30g**.
- Reale **0.07986 $**; p50 previsto **0.09029 $**; scarto **-11,55%**.
- Errore medio assoluto **6,57%**; massimo **14,02%**; DENTRO p10-p90; FUORI p25-p75.

#### Cono regime-adjusted

Gruppo selezionato: **NONE**; fallback: **NONE**; motivo: **INSUFFICIENT_REGIME_MATCHES**.

Non disponibile: INSUFFICIENT_REGIME_MATCHES (campione selezionato 0/5 match).

## Accuratezza percorso scanner

| Asset   | Giorno   |   Controlli | Dentro p10-p90   | Dentro p25-p75   | Errore medio abs vs p50   | Errore medio vs p50   |
|:--------|:---------|------------:|:-----------------|:-----------------|:--------------------------|:----------------------|
| BTC | 1g | 95 | 94,74% | 72,63% | 1,81% | 0,25% |
| BTC | 3g | 91 | 94,51% | 80,22% | 2,95% | 0,53% |
| BTC | 7g | 84 | 94,05% | 73,81% | 4,66% | 0,88% |
| BTC | 14g | 70 | 98,57% | 78,57% | 5,81% | 0,13% |
| BTC | 30g | 41 | 100,00% | 68,29% | 12,09% | -4,91% |
| SOL | 1g | 95 | 86,32% | 64,21% | 2,60% | 0,45% |
| SOL | 3g | 91 | 92,31% | 73,63% | 3,76% | 1,11% |
| SOL | 7g | 84 | 92,86% | 72,62% | 5,85% | 1,70% |
| SOL | 14g | 70 | 90,00% | 72,86% | 8,38% | 3,41% |
| SOL | 30g | 41 | 95,12% | 70,73% | 14,88% | 3,87% |
| DOGE | 1g | 95 | 89,47% | 61,05% | 2,97% | 0,11% |
| DOGE | 3g | 91 | 92,31% | 62,64% | 4,60% | 0,69% |
| DOGE | 7g | 84 | 77,38% | 70,24% | 8,45% | 3,24% |
| DOGE | 14g | 70 | 87,14% | 51,43% | 10,43% | 6,04% |
| DOGE | 30g | 41 | 95,12% | 41,46% | 16,20% | 15,68% |

## Tail / outlier audit

I casi di coda restano nel calcolo. L'audit leave-one-out quantifica la sensibilità dei percentili senza trasformare l'analisi in un filtro discrezionale.

Dettaglio completo: [scanner_forecast_tail_outlier_audit.md](scanner_forecast_tail_outlier_audit.md).

## Calibratore shadow

Il cono ufficiale resta grezzo e invariato. Il calibratore usa soltanto previsioni passate già mature, campionate una volta a settimana per ridurre la falsa indipendenza. Ogni orizzonte si attiva a 30 controlli indipendenti: parte al 25% della correzione stimata e cresce gradualmente fino al 100% a 100 controlli.

| Asset   | Orizzonte   |   Controlli indipendenti |   Soglia | Stato                  | Forza correzione   | Shift p50   |   Scala p10-p90 |
|:--------|:------------|-------------------------:|---------:|:-----------------------|:-------------------|:------------|----------------:|
| BTC | 1g | 16 | 30 | RACCOLTA (14 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 3g | 16 | 30 | RACCOLTA (14 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 7g | 15 | 30 | RACCOLTA (15 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 14g | 14 | 30 | RACCOLTA (16 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 30g | 12 | 30 | RACCOLTA (18 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 1g | 16 | 30 | RACCOLTA (14 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 3g | 16 | 30 | RACCOLTA (14 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 7g | 15 | 30 | RACCOLTA (15 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 14g | 14 | 30 | RACCOLTA (16 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 30g | 12 | 30 | RACCOLTA (18 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 1g | 16 | 30 | RACCOLTA (14 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 3g | 16 | 30 | RACCOLTA (14 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 7g | 15 | 30 | RACCOLTA (15 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 14g | 14 | 30 | RACCOLTA (16 mancanti) | 0,0% | 0,00% | 1,000 |
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