<!-- SCANNER_FORECAST_TRACKER_START -->
# Scanner forecast path / cono probabilistico

Generato: 2026-10-03 05:31:54 UTC

## Snapshot effettivamente usato

| Asset   | Snapshot prezzo   | Generazione snapshot prezzo   | Snapshot match scanner   |
|:--------|:------------------|:------------------------------|:-------------------------|
| BTC | 2026-10-03 | 2026-10-03T05:30:21Z | 2026-10-03 05:30:21 |
| SOL | 2026-10-03 | 2026-10-03T05:30:21Z | 2026-10-03 05:30:21 |
| DOGE | 2026-10-03 | 2026-10-03T05:30:21Z | 2026-10-03 05:30:21 |

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
| BTC | 2026-10-03 | 84.612 $ | INCERTO | 47,50% | 71.471,50 $ | 75.473,19 $ | 83.254,18 $ | 102.664,17 $ | 122.576,98 $ |
| SOL | 2026-10-03 | 119,53 $ | DISCESA | 40,00% | 99,88 $ | 104,62 $ | 115,52 $ | 131,51 $ | 166,33 $ |
| DOGE | 2026-10-03 | 0.09315 $ | DISCESA | 35,00% | 0.07368 $ | 0.07895 $ | 0.08849 $ | 0.09788 $ | 0.13388 $ |

## Confronto raw / regime-adjusted

Il cono raw continua a usare i 40 casi dello scanner. Il cono regime-adjusted sceglie una sola coorte nella gerarchia SAME_BTC_AND_ASSET_REGIME → SAME_ASSET_REGIME → SAME_BTC_REGIME. Ogni livello richiede almeno 5 match; le coorti non vengono mai combinate e ogni fallback è dichiarato.

| Asset   | Stato adjusted   | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level        | selection_reason              | Raw p50 30g   | Adjusted p50 30g   | Raw p90 30g   | Adjusted p90 30g   |
|:--------|:-----------------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:----------------------|:------------------------------|:--------------|:-------------------|:--------------|:-------------------|
| BTC | AVAILABLE | SAME_BTC_REGIME | 2 | 2 | 11 | 11 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME | 83.254,18 $ | 80.273,51 $ | 122.576,98 $ | 104.747,57 $ |
| SOL | AVAILABLE | SAME_ASSET_REGIME | 2 | 6 | 13 | 6 | 5 | 1_SAME_ASSET_FALLBACK | FALLBACK_TO_SAME_ASSET_REGIME | 115,52 $ | 122,23 $ | 166,33 $ | 180,22 $ |
| DOGE | AVAILABLE | SAME_BTC_REGIME | 0 | 1 | 10 | 10 | 5 | 2_SAME_BTC_FALLBACK | FALLBACK_TO_SAME_BTC_REGIME | 0.08849 $ | 0.08827 $ | 0.13388 $ | 0.11670 $ |

## Grafici

### BTC

![Scanner forecast BTC](scanner_forecast_BTC.png)

#### Verifica storica e discrepanza

![Verifica storica cono BTC](scanner_forecast_history_BTC.png)

- Cono congelato il **2026-09-03**; verificato fino al **2026-10-03**; stato **COMPLETO 30/30g**.
- Reale **84.622,69 $**; p50 previsto **84.069,39 $**; scarto **0,66%**.
- Errore medio assoluto **3,85%**; massimo **10,19%**; DENTRO p10-p90; DENTRO p25-p75.

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

**Campione corrente:** 10 episodi qualificati su 40 · 10 asset distinti.

![SOL conditional successor corrente](scanner_forecast_SOL_conditional_successor_current.png)

###### Confronto diretto a 30 giorni

| Modello | Vintage | N | Target | P10 | P25 | P50 | P75 | P90 |
| --- | --- | ---: | --- | ---: | ---: | ---: | ---: | ---: |
| Cono standard | 2026-10-03 | 40 | 2026-11-02 | 99.88 $ | 104.62 $ | 115.52 $ | 131.51 $ | 166.33 $ |
| Conditional corrente | 2026-10-03 | 10 | 2026-11-02 | 87.61 $ | 94.43 $ | 114.21 $ | 135.52 $ | 217.52 $ |

###### Struttura successiva dei casi correnti

| Classe | Episodi | Frequenza empirica |
| --- | ---: | ---: |
| DIRECT_CONTINUATION | 5 | 50.00% |
| SHALLOW_PULLBACK_THEN_CONTINUATION | 0 | 0.00% |
| DEEP_PULLBACK_THEN_RECOVERY | 1 | 10.00% |
| FAILURE | 4 | 40.00% |
| UNRESOLVED | 0 | 0.00% |

###### Episodi qualificati oggi

| Asset | Match window | -5% hit | +10% anchor | Classe 60d |
| --- | --- | --- | --- | --- |
| KSM-USD | 2023-09-06 → 2023-12-14 | 2023-12-15 | 2023-12-21 | DIRECT_CONTINUATION |
| RUNE-USD | 2023-06-16 → 2023-09-23 | 2023-10-09 | 2023-10-23 | DIRECT_CONTINUATION |
| BTC-USD | 2022-11-20 → 2023-02-27 | 2023-03-07 | 2023-03-17 | DIRECT_CONTINUATION |
| EOS-USD | 2023-09-08 → 2023-12-16 | 2023-12-19 | 2023-12-27 | FAILURE |
| ETC-USD | 2023-09-08 → 2023-12-16 | 2023-12-19 | 2024-01-10 | DIRECT_CONTINUATION |
| KAVA-USD | 2023-09-08 → 2023-12-16 | 2023-12-18 | 2023-12-26 | FAILURE |
| XTZ-USD | 2023-09-08 → 2023-12-16 | 2023-12-18 | 2023-12-25 | FAILURE |
| AVAX-USD | 2021-06-21 → 2021-09-28 | 2021-10-10 | 2021-10-25 | DEEP_PULLBACK_THEN_RECOVERY |
| DOT-USD | 2023-09-08 → 2023-12-16 | 2023-12-19 | 2023-12-21 | DIRECT_CONTINUATION |
| VET-USD | 2020-04-08 → 2020-07-16 | 2020-07-20 | 2020-08-08 | FAILURE |

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

- Ultimo close disponibile: **2026-10-03** · SOL **119.59 $**.
- Giorno del vintage: **15/30**.
- P50 condizionato previsto per quel giorno: **115.87 $**.
- SOL reale: **DENTRO p10-p90** · **DENTRO p25-p75**.

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

- Cono congelato il **2026-09-03**; verificato fino al **2026-10-03**; stato **COMPLETO 30/30g**.
- Reale **119,59 $**; p50 previsto **112,17 $**; scarto **6,62%**.
- Errore medio assoluto **6,31%**; massimo **12,83%**; DENTRO p10-p90; DENTRO p25-p75.

#### Cono regime-adjusted

Gruppo selezionato: **SAME_ASSET_REGIME**; fallback: **1_SAME_ASSET_FALLBACK**; motivo: **FALLBACK_TO_SAME_ASSET_REGIME**.

**WARNING:** coorte fallback meno stringente rispetto a SAME_BTC_AND_ASSET_REGIME.

![Scanner forecast regime-adjusted SOL](scanner_forecast_SOL_regime_adjusted.png)

### DOGE

![Scanner forecast DOGE](scanner_forecast_DOGE.png)

#### Verifica storica e discrepanza

![Verifica storica cono DOGE](scanner_forecast_history_DOGE.png)

- Cono congelato il **2026-09-03**; verificato fino al **2026-10-03**; stato **COMPLETO 30/30g**.
- Reale **0.09316 $**; p50 previsto **0.07480 $**; scarto **24,54%**.
- Errore medio assoluto **11,59%**; massimo **27,76%**; DENTRO p10-p90; FUORI p25-p75.

#### Cono regime-adjusted

Gruppo selezionato: **SAME_BTC_REGIME**; fallback: **2_SAME_BTC_FALLBACK**; motivo: **FALLBACK_TO_SAME_BTC_REGIME**.

**WARNING:** coorte fallback meno stringente rispetto a SAME_BTC_AND_ASSET_REGIME.

![Scanner forecast regime-adjusted DOGE](scanner_forecast_DOGE_regime_adjusted.png)

## Accuratezza percorso scanner

| Asset   | Giorno   |   Controlli | Dentro p10-p90   | Dentro p25-p75   | Errore medio abs vs p50   | Errore medio vs p50   |
|:--------|:---------|------------:|:-----------------|:-----------------|:--------------------------|:----------------------|
| BTC | 1g | 77 | 93,51% | 68,83% | 1,98% | 0,41% |
| BTC | 3g | 74 | 93,24% | 75,68% | 3,36% | 0,69% |
| BTC | 7g | 66 | 92,42% | 68,18% | 4,93% | 1,75% |
| BTC | 14g | 54 | 98,15% | 72,22% | 5,57% | 2,13% |
| BTC | 30g | 26 | 100,00% | 92,31% | 8,20% | 3,12% |
| SOL | 1g | 77 | 83,12% | 63,64% | 2,69% | 0,87% |
| SOL | 3g | 74 | 91,89% | 74,32% | 3,92% | 1,76% |
| SOL | 7g | 66 | 90,91% | 72,73% | 5,54% | 3,78% |
| SOL | 14g | 54 | 87,04% | 75,93% | 8,04% | 7,16% |
| SOL | 30g | 26 | 92,31% | 53,85% | 14,88% | 14,39% |
| DOGE | 1g | 77 | 88,31% | 61,04% | 3,07% | 0,52% |
| DOGE | 3g | 74 | 91,89% | 63,51% | 4,68% | 1,45% |
| DOGE | 7g | 66 | 75,76% | 74,24% | 8,58% | 5,92% |
| DOGE | 14g | 54 | 83,33% | 46,30% | 11,35% | 9,79% |
| DOGE | 30g | 26 | 92,31% | 34,62% | 17,87% | 17,87% |

## Tail / outlier audit

I casi di coda restano nel calcolo. L'audit leave-one-out quantifica la sensibilità dei percentili senza trasformare l'analisi in un filtro discrezionale.

Dettaglio completo: [scanner_forecast_tail_outlier_audit.md](scanner_forecast_tail_outlier_audit.md).

## Calibratore shadow

Il cono ufficiale resta grezzo e invariato. Il calibratore usa soltanto previsioni passate già mature, campionate una volta a settimana per ridurre la falsa indipendenza. Ogni orizzonte si attiva a 30 controlli indipendenti: parte al 25% della correzione stimata e cresce gradualmente fino al 100% a 100 controlli.

| Asset   | Orizzonte   |   Controlli indipendenti |   Soglia | Stato                  | Forza correzione   | Shift p50   |   Scala p10-p90 |
|:--------|:------------|-------------------------:|---------:|:-----------------------|:-------------------|:------------|----------------:|
| BTC | 1g | 13 | 30 | RACCOLTA (17 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 3g | 13 | 30 | RACCOLTA (17 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 7g | 12 | 30 | RACCOLTA (18 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 14g | 11 | 30 | RACCOLTA (19 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 30g | 9 | 30 | RACCOLTA (21 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 1g | 13 | 30 | RACCOLTA (17 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 3g | 13 | 30 | RACCOLTA (17 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 7g | 12 | 30 | RACCOLTA (18 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 14g | 11 | 30 | RACCOLTA (19 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 30g | 9 | 30 | RACCOLTA (21 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 1g | 13 | 30 | RACCOLTA (17 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 3g | 13 | 30 | RACCOLTA (17 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 7g | 12 | 30 | RACCOLTA (18 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 14g | 11 | 30 | RACCOLTA (19 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 30g | 9 | 30 | RACCOLTA (21 mancanti) | 0,0% | 0,00% | 1,000 |

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