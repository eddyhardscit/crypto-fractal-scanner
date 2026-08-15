<!-- SCANNER_FORECAST_TRACKER_START -->
# Scanner forecast path / cono probabilistico

Generato: 2026-08-15 05:32:59 UTC

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
| BTC | 2026-08-15 | 63.051 $ | SALITA | 70,00% | 58.354,75 $ | 60.759,35 $ | 68.492,55 $ | 75.304,40 $ | 93.822,61 $ |
| SOL | 2026-08-15 | 75,39 $ | SALITA | 75,00% | 69,72 $ | 75,74 $ | 79,32 $ | 92,06 $ | 135,24 $ |
| DOGE | 2026-08-15 | 0.07014 $ | SALITA | 65,00% | 0.05324 $ | 0.06598 $ | 0.07859 $ | 0.08806 $ | 0.09917 $ |

## Grafici

### BTC

![Scanner forecast BTC](scanner_forecast_BTC.png)

#### Verifica storica e discrepanza

![Verifica storica cono BTC](scanner_forecast_history_BTC.png)

- Cono congelato il **2026-07-16**; verificato fino al **2026-08-15**; stato **COMPLETO 30/30g**.
- Reale **63.058,63 $**; p50 previsto **66.378,43 $**; scarto **-5,00%**.
- Errore medio assoluto **2,80%**; massimo **5,31%**; DENTRO p10-p90; DENTRO p25-p75.

### SOL

![Scanner forecast SOL](scanner_forecast_SOL.png)

#### Verifica storica e discrepanza

![Verifica storica cono SOL](scanner_forecast_history_SOL.png)

- Cono congelato il **2026-07-16**; verificato fino al **2026-08-15**; stato **COMPLETO 30/30g**.
- Reale **75,40 $**; p50 previsto **73,94 $**; scarto **1,97%**.
- Errore medio assoluto **1,82%**; massimo **5,60%**; DENTRO p10-p90; DENTRO p25-p75.

### DOGE

![Scanner forecast DOGE](scanner_forecast_DOGE.png)

#### Verifica storica e discrepanza

![Verifica storica cono DOGE](scanner_forecast_history_DOGE.png)

- Cono congelato il **2026-07-16**; verificato fino al **2026-08-15**; stato **COMPLETO 30/30g**.
- Reale **0.07012 $**; p50 previsto **0.05994 $**; scarto **16,98%**.
- Errore medio assoluto **12,21%**; massimo **23,44%**; DENTRO p10-p90; DENTRO p25-p75.

## Accuratezza percorso scanner

| Asset   | Giorno   |   Controlli | Dentro p10-p90   | Dentro p25-p75   | Errore medio abs vs p50   | Errore medio vs p50   |
|:--------|:---------|------------:|:-----------------|:-----------------|:--------------------------|:----------------------|
| BTC | 1g | 34 | 100,00% | 61,76% | 1,61% | -0,21% |
| BTC | 3g | 33 | 100,00% | 78,79% | 2,12% | -0,65% |
| BTC | 7g | 30 | 100,00% | 86,67% | 2,54% | -0,09% |
| BTC | 14g | 23 | 100,00% | 86,96% | 2,83% | -0,05% |
| BTC | 30g | 7 | 100,00% | 85,71% | 8,04% | -8,04% |
| SOL | 1g | 34 | 79,41% | 64,71% | 1,94% | -0,40% |
| SOL | 3g | 33 | 100,00% | 78,79% | 2,31% | -0,95% |
| SOL | 7g | 30 | 100,00% | 93,33% | 1,94% | -0,00% |
| SOL | 14g | 23 | 100,00% | 91,30% | 1,88% | 0,80% |
| SOL | 30g | 7 | 100,00% | 100,00% | 1,76% | -0,05% |
| DOGE | 1g | 34 | 97,06% | 64,71% | 2,32% | 0,09% |
| DOGE | 3g | 33 | 100,00% | 87,88% | 2,25% | 0,73% |
| DOGE | 7g | 30 | 93,33% | 90,00% | 5,39% | 3,33% |
| DOGE | 14g | 23 | 100,00% | 69,57% | 6,92% | 5,16% |
| DOGE | 30g | 7 | 100,00% | 28,57% | 14,20% | 14,20% |

## Calibratore shadow

Il cono ufficiale resta grezzo e invariato. Il calibratore usa soltanto previsioni passate già mature, campionate una volta a settimana per ridurre la falsa indipendenza. Ogni orizzonte si attiva a 30 controlli indipendenti: parte al 25% della correzione stimata e cresce gradualmente fino al 100% a 100 controlli.

| Asset   | Orizzonte   |   Controlli indipendenti |   Soglia | Stato                  | Forza correzione   | Shift p50   |   Scala p10-p90 |
|:--------|:------------|-------------------------:|---------:|:-----------------------|:-------------------|:------------|----------------:|
| BTC | 1g | 6 | 30 | RACCOLTA (24 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 3g | 6 | 30 | RACCOLTA (24 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 7g | 5 | 30 | RACCOLTA (25 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 14g | 4 | 30 | RACCOLTA (26 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 30g | 2 | 30 | RACCOLTA (28 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 1g | 6 | 30 | RACCOLTA (24 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 3g | 6 | 30 | RACCOLTA (24 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 7g | 5 | 30 | RACCOLTA (25 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 14g | 4 | 30 | RACCOLTA (26 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 30g | 2 | 30 | RACCOLTA (28 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 1g | 6 | 30 | RACCOLTA (24 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 3g | 6 | 30 | RACCOLTA (24 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 7g | 5 | 30 | RACCOLTA (25 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 14g | 4 | 30 | RACCOLTA (26 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 30g | 2 | 30 | RACCOLTA (28 mancanti) | 0,0% | 0,00% | 1,000 |

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