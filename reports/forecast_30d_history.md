# Storico previsioni scanner a 30 giorni

Generato: **2026-07-13 21:25:22 CEST**  
UTC: **2026-07-13 19:25:22 UTC**

Questo file salva, giorno per giorno, la previsione a 30 giorni dello scanner.

Serve per vedere come cambia nel tempo la lettura:

- direzione prevista
- casi positivi / negativi
- scenario centrale a 30 giorni
- drawdown atteso durante i 30 giorni
- massimo rialzo atteso durante i 30 giorni

Il file CSV completo è: `forecast_30d_history.csv`.

## Stato archivio

| Voce | Valore |
| --- | --- |
| Prima previsione salvata | 2026-07-13 |
| Ultima previsione salvata | 2026-07-13 |
| Righe totali salvate | 3 |
| Asset seguiti | BTC, SOL, DOGE |

## Ultima previsione salvata

| Data | Asset | Prezzo | Direzione | Casi positivi | Return p50 | Return % | Drawdown p50 | Drawdown % | Max gain p50 | Max gain % | Controllo 30g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-07-13 | BTC | 62.682 $ | SALITA | 70,00% | 67.852 $ | +8,25% | 59.777 $ | -4,63% | 72.306 $ | +15,35% | 2026-08-12 |
| 2026-07-13 | DOGE | 0,07000 $ | DISCESA | 17,50% | 0,06000 $ | -19,69% | 0,05000 $ | -26,99% | 0,08000 $ | +4,92% | 2026-08-12 |
| 2026-07-13 | SOL | 76,29 $ | DISCESA | 35,00% | 74,30 $ | -2,61% | 67,07 $ | -12,08% | 82,25 $ | +7,81% | 2026-08-12 |

## Storico compatto per asset

### Bitcoin (BTC)

| Data | Prezzo | Direzione | Casi positivi | Return p50 | Return % | Drawdown p50 | Drawdown % | Max gain p50 | Max gain % | Max gain p75 | Max gain p75 % | Controllo 30g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-07-13 | 62.682 $ | SALITA | 70,00% | 67.852 $ | +8,25% | 59.777 $ | -4,63% | 72.306 $ | +15,35% | 79.172 $ | +26,31% | 2026-08-12 |

### Solana (SOL)

| Data | Prezzo | Direzione | Casi positivi | Return p50 | Return % | Drawdown p50 | Drawdown % | Max gain p50 | Max gain % | Max gain p75 | Max gain p75 % | Controllo 30g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-07-13 | 76,29 $ | DISCESA | 35,00% | 74,30 $ | -2,61% | 67,07 $ | -12,08% | 82,25 $ | +7,81% | 88,12 $ | +15,50% | 2026-08-12 |

### Dogecoin (DOGE)

| Data | Prezzo | Direzione | Casi positivi | Return p50 | Return % | Drawdown p50 | Drawdown % | Max gain p50 | Max gain % | Max gain p75 | Max gain p75 % | Controllo 30g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-07-13 | 0,07000 $ | DISCESA | 17,50% | 0,06000 $ | -19,69% | 0,05000 $ | -26,99% | 0,08000 $ | +4,92% | 0,08000 $ | +15,20% | 2026-08-12 |

## Storico completo percentili

Questa parte è più larga, ma è utile se vuoi vedere tutta l'evoluzione delle bande.

### Bitcoin (BTC) — percentili completi

| Data | Return p10 | Return p25 | Return p50 | Return p75 | Return p90 | Drawdown p10 | Drawdown p25 | Drawdown p50 | Max gain p50 | Max gain p75 | Max gain p90 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-07-13 | 50.625 $ | 60.170 $ | 67.852 $ | 75.079 $ | 87.726 $ | 47.284 $ | 55.304 $ | 59.777 $ | 72.306 $ | 79.172 $ | 96.237 $ |

### Solana (SOL) — percentili completi

| Data | Return p10 | Return p25 | Return p50 | Return p75 | Return p90 | Drawdown p10 | Drawdown p25 | Drawdown p50 | Max gain p50 | Max gain p75 | Max gain p90 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-07-13 | 58,88 $ | 66,61 $ | 74,30 $ | 79,02 $ | 98,31 $ | 56,98 $ | 59,84 $ | 67,07 $ | 82,25 $ | 88,12 $ | 110,60 $ |

### Dogecoin (DOGE) — percentili completi

| Data | Return p10 | Return p25 | Return p50 | Return p75 | Return p90 | Drawdown p10 | Drawdown p25 | Drawdown p50 | Max gain p50 | Max gain p75 | Max gain p90 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-07-13 | 0,05000 $ | 0,05000 $ | 0,06000 $ | 0,07000 $ | 0,08000 $ | 0,04000 $ | 0,05000 $ | 0,05000 $ | 0,08000 $ | 0,08000 $ | 0,09000 $ |

## Come leggerlo

- **Return p50**: scenario centrale del prezzo fra 30 giorni.
- **Drawdown p50**: discesa normale possibile durante quei 30 giorni.
- **Drawdown p10/p25**: scenari brutti da guardare se usi leva.
- **Max gain p50**: rialzo normale possibile durante il mese.
- **Max gain p75/p90**: zone più ottimistiche, utili per take profit.
- **Controllo 30g**: giorno in cui quella previsione potrà essere verificata.

Nota: se lanci il workflow più volte nello stesso giorno, viene tenuta solo l'ultima previsione di quel giorno per ogni asset.
