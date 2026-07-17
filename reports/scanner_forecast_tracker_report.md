<!-- SCANNER_FORECAST_TRACKER_START -->
# Scanner forecast path / cono probabilistico

Generato: 2026-07-17 07:31:42 UTC

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
| BTC | 2026-07-17 | 62.871 $ | INCERTO | 55,00% | 45.618,96 $ | 52.925,84 $ | 64.404,66 $ | 70.148,27 $ | 79.671,19 $ |
| SOL | 2026-07-17 | 74,46 $ | INCERTO | 47,50% | 57,22 $ | 64,98 $ | 73,79 $ | 81,96 $ | 87,73 $ |
| DOGE | 2026-07-17 | 0.07165 $ | DISCESA | 30,00% | 0.05071 $ | 0.05542 $ | 0.06118 $ | 0.07348 $ | 0.08510 $ |

## Grafici

### BTC

![Scanner forecast BTC](scanner_forecast_BTC.png)

#### Verifica storica e discrepanza

![Verifica storica cono BTC](scanner_forecast_history_BTC.png)

- Cono congelato il **2026-07-10**; verificato fino al **2026-07-17**; stato **PARZIALE 7/30g**.
- Reale **62.913,27 $**; p50 previsto **68.016,95 $**; scarto **-7,50%**.
- Errore medio assoluto **3,03%**; massimo **7,50%**; DENTRO p10-p90; FUORI p25-p75.

### SOL

![Scanner forecast SOL](scanner_forecast_SOL.png)

#### Verifica storica e discrepanza

![Verifica storica cono SOL](scanner_forecast_history_SOL.png)

- Cono congelato il **2026-07-10**; verificato fino al **2026-07-17**; stato **PARZIALE 7/30g**.
- Reale **74,57 $**; p50 previsto **79,28 $**; scarto **-5,94%**.
- Errore medio assoluto **2,78%**; massimo **5,94%**; DENTRO p10-p90; DENTRO p25-p75.

### DOGE

![Scanner forecast DOGE](scanner_forecast_DOGE.png)

#### Verifica storica e discrepanza

![Verifica storica cono DOGE](scanner_forecast_history_DOGE.png)

- Cono congelato il **2026-07-10**; verificato fino al **2026-07-17**; stato **PARZIALE 7/30g**.
- Reale **0.07170 $**; p50 previsto **0.07171 $**; scarto **-0,02%**.
- Errore medio assoluto **1,04%**; massimo **2,71%**; DENTRO p10-p90; DENTRO p25-p75.

## Accuratezza percorso scanner

| Asset   | Giorno   |   Controlli | Dentro p10-p90   | Dentro p25-p75   | Errore medio abs vs p50   | Errore medio vs p50   |
|:--------|:---------|------------:|:-----------------|:-----------------|:--------------------------|:----------------------|
| BTC | 1g | 7 | 100,00% | 85,71% | 2,13% | -1,41% |
| BTC | 3g | 5 | 80,00% | 60,00% | 4,02% | -4,02% |
| BTC | 7g | 1 | 100,00% | 0,00% | 7,95% | -7,95% |
| BTC | 14g | 0 | n/a | n/a | n/a | n/a |
| BTC | 30g | 0 | n/a | n/a | n/a | n/a |
| SOL | 1g | 7 | 85,71% | 57,14% | 2,21% | -1,96% |
| SOL | 3g | 5 | 100,00% | 60,00% | 2,57% | -2,27% |
| SOL | 7g | 1 | 100,00% | 100,00% | 6,04% | -6,04% |
| SOL | 14g | 0 | n/a | n/a | n/a | n/a |
| SOL | 30g | 0 | n/a | n/a | n/a | n/a |
| DOGE | 1g | 7 | 100,00% | 57,14% | 1,69% | -0,69% |
| DOGE | 3g | 5 | 100,00% | 100,00% | 1,72% | -1,33% |
| DOGE | 7g | 1 | 100,00% | 100,00% | 0,02% | -0,02% |
| DOGE | 14g | 0 | n/a | n/a | n/a | n/a |
| DOGE | 30g | 0 | n/a | n/a | n/a | n/a |

## Calibratore shadow

Il cono ufficiale resta grezzo e invariato. Il calibratore usa soltanto previsioni passate già mature, campionate una volta a settimana per ridurre la falsa indipendenza. Ogni orizzonte si attiva a 30 controlli indipendenti: parte al 25% della correzione stimata e cresce gradualmente fino al 100% a 100 controlli.

| Asset   | Orizzonte   |   Controlli indipendenti |   Soglia | Stato                  | Forza correzione   | Shift p50   |   Scala p10-p90 |
|:--------|:------------|-------------------------:|---------:|:-----------------------|:-------------------|:------------|----------------:|
| BTC | 1g | 2 | 30 | RACCOLTA (28 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 3g | 2 | 30 | RACCOLTA (28 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 7g | 1 | 30 | RACCOLTA (29 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 14g | 0 | 30 | RACCOLTA (30 mancanti) | 0,0% | 0,00% | 1,000 |
| BTC | 30g | 0 | 30 | RACCOLTA (30 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 1g | 2 | 30 | RACCOLTA (28 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 3g | 2 | 30 | RACCOLTA (28 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 7g | 1 | 30 | RACCOLTA (29 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 14g | 0 | 30 | RACCOLTA (30 mancanti) | 0,0% | 0,00% | 1,000 |
| SOL | 30g | 0 | 30 | RACCOLTA (30 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 1g | 2 | 30 | RACCOLTA (28 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 3g | 2 | 30 | RACCOLTA (28 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 7g | 1 | 30 | RACCOLTA (29 mancanti) | 0,0% | 0,00% | 1,000 |
| DOGE | 14g | 0 | 30 | RACCOLTA (30 mancanti) | 0,0% | 0,00% | 1,000 |
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