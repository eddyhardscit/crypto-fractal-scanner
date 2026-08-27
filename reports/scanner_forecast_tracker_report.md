<!-- SCANNER_FORECAST_TRACKER_START -->
# Scanner forecast path / cono probabilistico

Generato: 2026-08-27 15:31:53 UTC

## Snapshot effettivamente usato

| Asset   | Snapshot prezzo   | Generazione snapshot prezzo   | Snapshot match scanner   |
|:--------|:------------------|:------------------------------|:-------------------------|
| BTC     | 2026-08-27        | 2026-08-27T05:30:23Z          | 2026-08-27 05:30:24      |
| SOL     | 2026-08-27        | 2026-08-27T05:30:23Z          | 2026-08-27 05:30:24      |
| DOGE    | 2026-08-27        | 2026-08-27T05:30:23Z          | 2026-08-27 05:30:24      |

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
| BTC     | 2026-08-27 | 78.653,26 $       | SALITA              | 70,00%          | 69.633,83 $ | 77.036,02 $ | 87.726,91 $ | 94.069,53 $ | 110.479,34 $ |
| SOL     | 2026-08-27 | 100,99 $          | SALITA              | 62,50%          | 89,12 $     | 98,05 $     | 104,95 $    | 120,32 $    | 196,29 $     |
| DOGE    | 2026-08-27 | 0.08650 $         | DISCESA             | 40,00%          | 0.06503 $   | 0.07575 $   | 0.08256 $   | 0.09074 $   | 0.10718 $    |

## Confronto raw / regime-adjusted

Il cono raw continua a usare i 40 casi dello scanner. Il cono regime-adjusted sceglie una sola coorte nella gerarchia SAME_BTC_AND_ASSET_REGIME → SAME_ASSET_REGIME → SAME_BTC_REGIME. Ogni livello richiede almeno 5 match; le coorti non vengono mai combinate e ogni fallback è dichiarato.

| Asset   | Stato adjusted              | selected_regime_group   |   full_regime_matches |   same_asset_regime_matches |   same_btc_regime_matches |   selected_sample_size |   minimum_required | fallback_level        | selection_reason              | Raw p50 30g   | Adjusted p50 30g   | Raw p90 30g   | Adjusted p90 30g   |
|:--------|:----------------------------|:------------------------|----------------------:|----------------------------:|--------------------------:|-----------------------:|-------------------:|:----------------------|:------------------------------|:--------------|:-------------------|:--------------|:-------------------|
| BTC     | INSUFFICIENT_REGIME_MATCHES | NONE                    |                     0 |                           1 |                         0 |                      0 |                  5 | NONE                  | INSUFFICIENT_REGIME_MATCHES   | 87.726,91 $   | n/a                | 110.479,34 $  | n/a                |
| SOL     | AVAILABLE                   | SAME_ASSET_REGIME       |                     0 |                           8 |                         0 |                      8 |                  5 | 1_SAME_ASSET_FALLBACK | FALLBACK_TO_SAME_ASSET_REGIME | 104,95 $      | 97,68 $            | 196,29 $      | 107,86 $           |
| DOGE    | AVAILABLE                   | SAME_ASSET_REGIME       |                     0 |                           8 |                         0 |                      8 |                  5 | 1_SAME_ASSET_FALLBACK | FALLBACK_TO_SAME_ASSET_REGIME | 0.08256 $     | 0.08495 $          | 0.10718 $     | 0.12078 $          |

## Grafici

### BTC

![Scanner forecast BTC](scanner_forecast_BTC.png)

#### Verifica storica e discrepanza

![Verifica storica cono BTC](scanner_forecast_history_BTC.png)

- Cono congelato il **2026-07-28**; verificato fino al **2026-08-27**; stato **COMPLETO 30/30g**.
- Reale **80.474,24 $**; p50 previsto **68.129,01 $**; scarto **18,12%**.
- Errore medio assoluto **5,24%**; massimo **18,12%**; DENTRO p10-p90; DENTRO p25-p75.

#### Cono regime-adjusted

Gruppo selezionato: **NONE**; fallback: **NONE**; motivo: **INSUFFICIENT_REGIME_MATCHES**.

Non disponibile: INSUFFICIENT_REGIME_MATCHES (campione selezionato 0/5 match).

### SOL

![Scanner forecast SOL](scanner_forecast_SOL.png)

#### Verifica storica e discrepanza

![Verifica storica cono SOL](scanner_forecast_history_SOL.png)

- Cono congelato il **2026-07-28**; verificato fino al **2026-08-27**; stato **COMPLETO 30/30g**.
- Reale **107,27 $**; p50 previsto **78,88 $**; scarto **35,99%**.
- Errore medio assoluto **6,78%**; massimo **35,99%**; DENTRO p10-p90; FUORI p25-p75.

#### Cono regime-adjusted

Gruppo selezionato: **SAME_ASSET_REGIME**; fallback: **1_SAME_ASSET_FALLBACK**; motivo: **FALLBACK_TO_SAME_ASSET_REGIME**.

**WARNING:** coorte fallback meno stringente rispetto a SAME_BTC_AND_ASSET_REGIME.

![Scanner forecast regime-adjusted SOL](scanner_forecast_SOL_regime_adjusted.png)

### DOGE

![Scanner forecast DOGE](scanner_forecast_DOGE.png)

#### Verifica storica e discrepanza

![Verifica storica cono DOGE](scanner_forecast_history_DOGE.png)

- Cono congelato il **2026-07-28**; verificato fino al **2026-08-27**; stato **COMPLETO 30/30g**.
- Reale **0.08899 $**; p50 previsto **0.07461 $**; scarto **19,27%**.
- Errore medio assoluto **7,64%**; massimo **33,18%**; DENTRO p10-p90; FUORI p25-p75.

#### Cono regime-adjusted

Gruppo selezionato: **SAME_ASSET_REGIME**; fallback: **1_SAME_ASSET_FALLBACK**; motivo: **FALLBACK_TO_SAME_ASSET_REGIME**.

**WARNING:** coorte fallback meno stringente rispetto a SAME_BTC_AND_ASSET_REGIME.

![Scanner forecast regime-adjusted DOGE](scanner_forecast_DOGE_regime_adjusted.png)

## Accuratezza percorso scanner

| Asset   | Giorno   |   Controlli | Dentro p10-p90   | Dentro p25-p75   | Errore medio abs vs p50   | Errore medio vs p50   |
|:--------|:---------|------------:|:-----------------|:-----------------|:--------------------------|:----------------------|
| BTC     | 1g       |          46 | 93,48%           | 60,87%           | 2,27%                     | 0,82%                 |
| BTC     | 3g       |          44 | 88,64%           | 72,73%           | 3,38%                     | 1,29%                 |
| BTC     | 7g       |          40 | 90,00%           | 70,00%           | 5,67%                     | 2,98%                 |
| BTC     | 14g      |          33 | 96,97%           | 72,73%           | 5,01%                     | 2,10%                 |
| BTC     | 30g      |          19 | 100,00%          | 94,74%           | 7,89%                     | 0,94%                 |
| SOL     | 1g       |          46 | 73,91%           | 56,52%           | 3,04%                     | 1,26%                 |
| SOL     | 3g       |          44 | 86,36%           | 65,91%           | 4,33%                     | 1,87%                 |
| SOL     | 7g       |          40 | 85,00%           | 75,00%           | 5,46%                     | 3,59%                 |
| SOL     | 14g      |          33 | 90,91%           | 72,73%           | 6,13%                     | 5,01%                 |
| SOL     | 30g      |          19 | 94,74%           | 57,89%           | 11,60%                    | 10,92%                |
| DOGE    | 1g       |          46 | 84,78%           | 58,70%           | 3,49%                     | 1,11%                 |
| DOGE    | 3g       |          44 | 88,64%           | 72,73%           | 4,59%                     | 2,76%                 |
| DOGE    | 7g       |          40 | 77,50%           | 75,00%           | 9,48%                     | 7,93%                 |
| DOGE    | 14g      |          33 | 81,82%           | 57,58%           | 11,01%                    | 9,78%                 |
| DOGE    | 30g      |          19 | 89,47%           | 36,84%           | 18,27%                    | 18,27%                |

## Tail / outlier audit

I casi di coda restano nel calcolo. L'audit leave-one-out quantifica la sensibilità dei percentili senza trasformare l'analisi in un filtro discrezionale.

Dettaglio completo: [scanner_forecast_tail_outlier_audit.md](scanner_forecast_tail_outlier_audit.md).

## Calibratore shadow

Il cono ufficiale resta grezzo e invariato. Il calibratore usa soltanto previsioni passate già mature, campionate una volta a settimana per ridurre la falsa indipendenza. Ogni orizzonte si attiva a 30 controlli indipendenti: parte al 25% della correzione stimata e cresce gradualmente fino al 100% a 100 controlli.

| Asset   | Orizzonte   |   Controlli indipendenti |   Soglia | Stato                  | Forza correzione   | Shift p50   |   Scala p10-p90 |
|:--------|:------------|-------------------------:|---------:|:-----------------------|:-------------------|:------------|----------------:|
| BTC     | 1g          |                        8 |       30 | RACCOLTA (22 mancanti) | 0,0%               | 0,00%       |           1,000 |
| BTC     | 3g          |                        8 |       30 | RACCOLTA (22 mancanti) | 0,0%               | 0,00%       |           1,000 |
| BTC     | 7g          |                        7 |       30 | RACCOLTA (23 mancanti) | 0,0%               | 0,00%       |           1,000 |
| BTC     | 14g         |                        6 |       30 | RACCOLTA (24 mancanti) | 0,0%               | 0,00%       |           1,000 |
| BTC     | 30g         |                        4 |       30 | RACCOLTA (26 mancanti) | 0,0%               | 0,00%       |           1,000 |
| SOL     | 1g          |                        8 |       30 | RACCOLTA (22 mancanti) | 0,0%               | 0,00%       |           1,000 |
| SOL     | 3g          |                        8 |       30 | RACCOLTA (22 mancanti) | 0,0%               | 0,00%       |           1,000 |
| SOL     | 7g          |                        7 |       30 | RACCOLTA (23 mancanti) | 0,0%               | 0,00%       |           1,000 |
| SOL     | 14g         |                        6 |       30 | RACCOLTA (24 mancanti) | 0,0%               | 0,00%       |           1,000 |
| SOL     | 30g         |                        4 |       30 | RACCOLTA (26 mancanti) | 0,0%               | 0,00%       |           1,000 |
| DOGE    | 1g          |                        8 |       30 | RACCOLTA (22 mancanti) | 0,0%               | 0,00%       |           1,000 |
| DOGE    | 3g          |                        8 |       30 | RACCOLTA (22 mancanti) | 0,0%               | 0,00%       |           1,000 |
| DOGE    | 7g          |                        7 |       30 | RACCOLTA (23 mancanti) | 0,0%               | 0,00%       |           1,000 |
| DOGE    | 14g         |                        6 |       30 | RACCOLTA (24 mancanti) | 0,0%               | 0,00%       |           1,000 |
| DOGE    | 30g         |                        4 |       30 | RACCOLTA (26 mancanti) | 0,0%               | 0,00%       |           1,000 |

### Confronto fuori campione: grezzo vs shadow

| Asset   | Orizzonte   |   Controlli OOS | MAE grezzo   | MAE shadow   | Miglioramento   | Shadow vince   | Copertura larga grezza   | Copertura larga shadow   |
|:--------|:------------|----------------:|:-------------|:-------------|:----------------|:---------------|:-------------------------|:-------------------------|
| BTC     | 1g          |               0 | n/a          | n/a          | n/a             | n/a            | n/a                      | n/a                      |
| BTC     | 3g          |               0 | n/a          | n/a          | n/a             | n/a            | n/a                      | n/a                      |
| BTC     | 7g          |               0 | n/a          | n/a          | n/a             | n/a            | n/a                      | n/a                      |
| BTC     | 14g         |               0 | n/a          | n/a          | n/a             | n/a            | n/a                      | n/a                      |
| BTC     | 30g         |               0 | n/a          | n/a          | n/a             | n/a            | n/a                      | n/a                      |
| DOGE    | 1g          |               0 | n/a          | n/a          | n/a             | n/a            | n/a                      | n/a                      |
| DOGE    | 3g          |               0 | n/a          | n/a          | n/a             | n/a            | n/a                      | n/a                      |
| DOGE    | 7g          |               0 | n/a          | n/a          | n/a             | n/a            | n/a                      | n/a                      |
| DOGE    | 14g         |               0 | n/a          | n/a          | n/a             | n/a            | n/a                      | n/a                      |
| DOGE    | 30g         |               0 | n/a          | n/a          | n/a             | n/a            | n/a                      | n/a                      |
| SOL     | 1g          |               0 | n/a          | n/a          | n/a             | n/a            | n/a                      | n/a                      |
| SOL     | 3g          |               0 | n/a          | n/a          | n/a             | n/a            | n/a                      | n/a                      |
| SOL     | 7g          |               0 | n/a          | n/a          | n/a             | n/a            | n/a                      | n/a                      |
| SOL     | 14g         |               0 | n/a          | n/a          | n/a             | n/a            | n/a                      | n/a                      |
| SOL     | 30g         |               0 | n/a          | n/a          | n/a             | n/a            | n/a                      | n/a                      |

## Come leggerlo

- Se il prezzo resta dentro p10-p90, lo scanner sta ancora descrivendo bene il range largo.
- Se il prezzo resta dentro p25-p75, lo scanner sta descrivendo bene anche il range centrale.
- Se il prezzo segue p50, il percorso reale è vicino allo scenario normale.
- Se il prezzo esce da p10-p90, il modello statistico dei 40 casi sta perdendo aderenza.
- Questo non sostituisce drawdown e max gain: serve soprattutto a vedere il percorso del return previsto.

Nota: servono almeno 5 controlli prima di dare un peso minimo al cono. Sotto 5 controlli resta solo osservazione.
<!-- SCANNER_FORECAST_TRACKER_END -->