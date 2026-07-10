<!-- SCANNER_FORECAST_TRACKER_START -->
# Scanner forecast path / cono probabilistico

Generato: 2026-07-10 12:51:15 UTC

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
| BTC     | 2026-07-10 | 64.277,24 $       | SALITA              | 77,50%          | 51.957,71 $ | 65.940,01 $ | 70.066,59 $ | 78.776,66 $ | 92.398,48 $ |
| SOL     | 2026-07-10 | 78,92 $           | DISCESA             | 37,50%          | 62,39 $     | 70,06 $     | 77,30 $     | 86,06 $     | 113,45 $    |
| DOGE    | 2026-07-10 | 0.07401 $         | DISCESA             | 15,00%          | 0.04505 $   | 0.05060 $   | 0.05746 $   | 0.06831 $   | 0.07953 $   |

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
| BTC     | 1g       |           0 | n/a              | n/a              | n/a                       | n/a                   |
| BTC     | 3g       |           0 | n/a              | n/a              | n/a                       | n/a                   |
| BTC     | 7g       |           0 | n/a              | n/a              | n/a                       | n/a                   |
| BTC     | 14g      |           0 | n/a              | n/a              | n/a                       | n/a                   |
| BTC     | 30g      |           0 | n/a              | n/a              | n/a                       | n/a                   |
| SOL     | 1g       |           0 | n/a              | n/a              | n/a                       | n/a                   |
| SOL     | 3g       |           0 | n/a              | n/a              | n/a                       | n/a                   |
| SOL     | 7g       |           0 | n/a              | n/a              | n/a                       | n/a                   |
| SOL     | 14g      |           0 | n/a              | n/a              | n/a                       | n/a                   |
| SOL     | 30g      |           0 | n/a              | n/a              | n/a                       | n/a                   |
| DOGE    | 1g       |           0 | n/a              | n/a              | n/a                       | n/a                   |
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

Nota: servono almeno 5 controlli prima di dare un peso minimo al cono. Sotto 5 controlli resta solo osservazione.
<!-- SCANNER_FORECAST_TRACKER_END -->