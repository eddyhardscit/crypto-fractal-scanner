# Scanner forecast path / cono probabilistico

Generato: 2026-07-10 00:56 UTC

Questo report costruisce il cono usando direttamente **i 40 match reali** del file `latest_scanner_matches.csv`, senza più leggere il markdown del report principale.

Per ogni asset crea:

- banda larga p10-p90
- banda centrale p25-p75
- scenario centrale p50
- prezzo reale sovrapposto

Serve a vedere se il prezzo reale sta camminando dentro il percorso previsto dallo scanner.

## Ultimo cono previsionale salvato

| Asset | Data | Prezzo iniziale | Direzione scanner | Casi positivi | P10 30g | P25 30g | P50 30g | P75 30g | P90 30g |
|:------|:-----|----------------:|:------------------|--------------:|--------:|--------:|--------:|--------:|--------:|
| BTC | 2026-07-10 | 63.030,66 $ | SALITA | 72,50% | 48.638,47 $ | 61.987,90 $ | 67.373,22 $ | 77.248,88 $ | 90.606,53 $ |
| SOL | 2026-07-10 | 77,93 $ | INCERTO | 42,50% | 62,69 $ | 69,91 $ | 76,73 $ | 87,27 $ | 112,02 $ |
| DOGE | 2026-07-10 | 0,07 $ | DISCESA | 12,50% | 0,05 $ | 0,05 $ | 0,06 $ | 0,07 $ | 0,07 $ |

## Grafici

### BTC

![Scanner forecast BTC](scanner_forecast_BTC.png)

### SOL

![Scanner forecast SOL](scanner_forecast_SOL.png)

### DOGE

![Scanner forecast DOGE](scanner_forecast_DOGE.png)

## Accuratezza percorso scanner

| Asset | Giorno | Controlli | Dentro p10-p90 | Dentro p25-p75 | Errore medio abs vs p50 | Errore medio vs p50 |
|:------|:-------|----------:|:---------------|:---------------|------------------------:|--------------------:|
| BTC | 1g | 0 | n/a | n/a | n/a | n/a |
| BTC | 3g | 0 | n/a | n/a | n/a | n/a |
| BTC | 7g | 0 | n/a | n/a | n/a | n/a |
| BTC | 14g | 0 | n/a | n/a | n/a | n/a |
| BTC | 30g | 0 | n/a | n/a | n/a | n/a |
| SOL | 1g | 0 | n/a | n/a | n/a | n/a |
| SOL | 3g | 0 | n/a | n/a | n/a | n/a |
| SOL | 7g | 0 | n/a | n/a | n/a | n/a |
| SOL | 14g | 0 | n/a | n/a | n/a | n/a |
| SOL | 30g | 0 | n/a | n/a | n/a | n/a |
| DOGE | 1g | 0 | n/a | n/a | n/a | n/a |
| DOGE | 3g | 0 | n/a | n/a | n/a | n/a |
| DOGE | 7g | 0 | n/a | n/a | n/a | n/a |
| DOGE | 14g | 0 | n/a | n/a | n/a | n/a |
| DOGE | 30g | 0 | n/a | n/a | n/a | n/a |

## Come leggerlo

- Se il prezzo resta dentro p10-p90, lo scanner sta ancora descrivendo bene il range largo.
- Se il prezzo resta dentro p25-p75, lo scanner sta descrivendo bene anche il range centrale.
- Se il prezzo segue p50, il percorso reale è vicino allo scenario normale.
- Se il prezzo esce da p10-p90, il modello statistico dei 40 casi sta perdendo aderenza.
- Questo non sostituisce drawdown e max gain: serve soprattutto a vedere il percorso del return previsto.
