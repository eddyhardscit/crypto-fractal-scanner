<!-- SCANNER_FORECAST_TRACKER_START -->
# Scanner forecast path / cono probabilistico

Generato: 2026-07-29 05:14:01 UTC

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
| BTC | 2026-07-29 | 63.922 $ | SALITA | 72,50% | 44.465,35 $ | 61.788,22 $ | 72.294,72 $ | 86.378,20 $ | 95.477,04 $ |
| SOL | 2026-07-29 | 73,47 $ | SALITA | 72,50% | 65,89 $ | 72,50 $ | 80,42 $ | 92,04 $ | 107,90 $ |
| DOGE | 2026-07-29 | 0.07061 $ | SALITA | 65,00% | 0.06251 $ | 0.06737 $ | 0.07382 $ | 0.07943 $ | 0.09054 $ |

## Grafici

### BTC

![Scanner forecast BTC](scanner_forecast_BTC.png)

#### Verifica storica e discrepanza

![Verifica storica cono BTC](scanner_forecast_history_BTC.png)

- Cono congelato il **2026-07-10**; verificato fino al **2026-07-29**; stato **PARZIALE 19/30g**.
- Reale **63.920,90 $**; p50 previsto **67.794,45 $**; scarto **-5,71%**.
- Errore medio assoluto **3,93%**; massimo **7,75%**; DENTRO p10-p90; DENTRO p25-p75.

### SOL

![Scanner forecast SOL](scanner_forecast_SOL.png)

#### Verifica storica e discrepanza

![Verifica storica cono SOL](scanner_forecast_history_SOL.png)

- Cono congelato il **2026-07-10**; verificato fino al **2026-07-29**; stato **PARZIALE 19/30g**.
- Reale **73,47 $**; p50 previsto **71,78 $**; scarto **2,36%**.
- Errore medio assoluto **2,65%**; massimo **5,38%**; DENTRO p10-p90; DENTRO p25-p75.

### DOGE

![Scanner forecast DOGE](scanner_forecast_DOGE.png)

#### Verifica storica e discrepanza

![Verifica storica cono DOGE](scanner_forecast_history_DOGE.png)

- Cono congelato il **2026-07-10**; verificato fino al **2026-07-29**; stato **PARZIALE 19/30g**.
- Reale **0.07060 $**; p50 previsto **0.05663 $**; scarto **24,67%**.
- Errore medio assoluto **9,87%**; massimo **25,63%**; DENTRO p10-p90; FUORI p25-p75.

## Accuratezza percorso scanner

| Asset   | Giorno   |   Controlli | Dentro p10-p90   | Dentro p25-p75   | Errore medio abs vs p50   | Errore medio vs p50   |
|:--------|:---------|------------:|:-----------------|:-----------------|:--------------------------|:----------------------|
| BTC | 1g | 19 | 100,00% | 57,89% | 1,80% | -0,05% |
| BTC | 3g | 17 | 100,00% | 70,59% | 2,32% | -0,16% |
| BTC | 7g | 13 | 100,00% | 84,62% | 2,88% | 0,73% |
| BTC | 14g | 6 | 100,00% | 83,33% | 1,85% | 0,14% |
| BTC | 30g | 0 | n/a | n/a | n/a | n/a |
| SOL | 1g | 19 | 73,68% | 47,37% | 2,43% | -0,51% |
| SOL | 3g | 17 | 100,00% | 64,71% | 2,67% | -0,82% |
| SOL | 7g | 13 | 100,00% | 92,31% | 2,61% | 0,72% |
| SOL | 14g | 6 | 100,00% | 83,33% | 2,95% | 2,56% |
| SOL | 30g | 0 | n/a | n/a | n/a | n/a |
| DOGE | 1g | 19 | 89,47% | 52,63% | 3,17% | -0,10% |
| DOGE | 3g | 17 | 100,00% | 88,24% | 2,24% | 0,92% |
| DOGE | 7g | 13 | 100,00% | 100,00% | 7,38% | 7,38% |
| DOGE | 14g | 6 | 100,00% | 16,67% | 18,41% | 18,41% |
| DOGE | 30g | 0 | n/a | n/a | n/a | n/a |

## Calibratore shadow

Il cono ufficiale resta grezzo e invariato. Il calibratore usa soltanto previsioni passate già mature, campionate una volta a settimana per ridurre la falsa indipendenza. Ogni orizzonte si attiva a 30 controlli indipendenti: parte al 25% della correzione stimata e cresce gradualmente fino al 100% a 100 controlli.

| Asset   | Orizzonte   |   Controlli indipendenti |   Soglia | Stato                  | Forza correzione   | Shift p50   |   Scala p10-p90 |
|:--------|:------------|-------------------------:|---------:|:-----------------------|:-------------------|:------------|----------------:|
| BTC | 1g | 4 | 30 | RACCOLTA (26 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 3g | 3 | 30 | RACCOLTA (27 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 7g | 3 | 30 | RACCOLTA (27 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 14g | 2 | 30 | RACCOLTA (28 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 30g | 0 | 30 | RACCOLTA (30 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 1g | 4 | 30 | RACCOLTA (26 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 3g | 3 | 30 | RACCOLTA (27 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 7g | 3 | 30 | RACCOLTA (27 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 14g | 2 | 30 | RACCOLTA (28 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 30g | 0 | 30 | RACCOLTA (30 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 1g | 4 | 30 | RACCOLTA (26 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 3g | 3 | 30 | RACCOLTA (27 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 7g | 3 | 30 | RACCOLTA (27 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 14g | 2 | 30 | RACCOLTA (28 mancanti) | 0,0% | 0,00% | 1,000 |
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