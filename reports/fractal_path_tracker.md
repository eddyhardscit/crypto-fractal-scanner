<!-- FRACTAL_PATH_TRACKER_START -->
# Tracking percorso frattale SOL/BTC

Generato: 2026-08-01 05:14 UTC

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-08-01**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-01-16**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **73,12 $**
- Verdetto principale: **ANALOGIA DEBOLE / SCENARIO SECONDARIO**
- Somiglianza strutturale: **+59,64%**
- Aderenza live principale: **+69,63%**
- Errore medio live principale: **15,18%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE SOLO DI CONTESTO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **56**
- Osservazioni inclusive dal bottom: **57**
- Osservazioni da inizio programma/scanner: **30**
- Errore assoluto medio dal bottom: **10,84%**
- Errore assoluto medio da inizio programma: **15,18%**
- Gap firmato medio ultimi 7 giorni: **-3,18%**
- Errore assoluto medio ultimi 7 giorni: **7,87%**
- Gap ultimo giorno: **-12,32%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **-12,32%**
- Gap firmato medio 7g: **-3,18%**
- Errore assoluto medio 7g: **7,87%**
- Variazione recente gap: **-6,16%**
- Stato gap: **IN DEVIAZIONE SOTTO IL FRATTALE**
- Trend gap: **SOL si sta allontanando sotto il percorso ancorato**

Soglie operative del grafico:

- entro **±5%**: percorso vicino;
- tra **±5% e ±12%**: deviazione gestibile;
- oltre **±12%**: frattale non abbastanza aderente per conferma operativa;
- oltre **±18%**: disallineamento marcato.

## Ultimi giorni del confronto ancorato

|   Giorno | Data SOL   | Data BTC eq.   | SOL reale   | Percorso ancorato   | Gap firmato   | Fase                |
|---------:|:-----------|:---------------|:------------|:--------------------|:--------------|:--------------------|
| 47 | 2026-07-23 | 2023-01-07 | 75,86 $ | 66,79 $ | +13,58% | da inizio programma |
| 48 | 2026-07-24 | 2023-01-08 | 73,88 $ | 67,33 $ | +9,73% | da inizio programma |
| 49 | 2026-07-25 | 2023-01-09 | 74,43 $ | 67,74 $ | +9,87% | da inizio programma |
| 50 | 2026-07-26 | 2023-01-10 | 76,60 $ | 68,73 $ | +11,46% | da inizio programma |
| 51 | 2026-07-27 | 2023-01-11 | 74,14 $ | 70,65 $ | +4,94% | da inizio programma |
| 52 | 2026-07-28 | 2023-01-12 | 73,70 $ | 74,33 $ | -0,85% | da inizio programma |
| 53 | 2026-07-29 | 2023-01-13 | 73,60 $ | 78,43 $ | -6,16% | da inizio programma |
| 54 | 2026-07-30 | 2023-01-14 | 74,47 $ | 82,63 $ | -9,88% | da inizio programma |
| 55 | 2026-07-31 | 2023-01-15 | 74,47 $ | 82,25 $ | -9,47% | da inizio programma |
| 56 | 2026-08-01 | 2023-01-16 | 73,12 $ | 83,39 $ | -12,32% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-08-08 | 90,34 $ | 79,22 $ | 71,46 $ / 79,22 $ | no | n/a | n/a | n/a |
| 14g | 2026-08-15 | 89,97 $ | 78,89 $ | 71,46 $ / 82,12 $ | no | n/a | n/a | n/a |
| 21g | 2026-08-22 | 89,66 $ | 78,61 $ | 71,46 $ / 82,12 $ | no | n/a | n/a | n/a |
| 28g | 2026-08-29 | 85,91 $ | 75,33 $ | 71,46 $ / 82,12 $ | no | n/a | n/a | n/a |
| 35g | 2026-09-05 | 97,81 $ | 85,76 $ | 71,46 $ / 85,76 $ | no | n/a | n/a | n/a |
| 42g | 2026-09-12 | 92,66 $ | 81,25 $ | 71,46 $ / 85,76 $ | no | n/a | n/a | n/a |
| 49g | 2026-09-19 | 88,36 $ | 77,47 $ | 71,46 $ / 85,76 $ | no | n/a | n/a | n/a |
| 56g | 2026-09-26 | 95,32 $ | 83,58 $ | 69,73 $ / 85,76 $ | no | n/a | n/a | n/a |
| 63g | 2026-10-03 | 109,38 $ | 95,91 $ | 69,73 $ / 96,85 $ | no | n/a | n/a | n/a |
| 70g | 2026-10-10 | 106,91 $ | 93,74 $ | 69,73 $ / 97,87 $ | no | n/a | n/a | n/a |
| 77g | 2026-10-17 | 109,47 $ | 95,99 $ | 69,73 $ / 98,36 $ | no | n/a | n/a | n/a |
| 84g | 2026-10-24 | 116,81 $ | 102,42 $ | 69,73 $ / 102,42 $ | no | n/a | n/a | n/a |
| 91g | 2026-10-31 | 115,99 $ | 101,70 $ | 69,73 $ / 105,30 $ | no | n/a | n/a | n/a |
| 98g | 2026-11-07 | 108,43 $ | 95,07 $ | 69,73 $ / 105,30 $ | no | n/a | n/a | n/a |
| 105g | 2026-11-14 | 110,66 $ | 97,03 $ | 69,73 $ / 105,30 $ | no | n/a | n/a | n/a |
| 112g | 2026-11-21 | 109,09 $ | 95,66 $ | 69,73 $ / 105,30 $ | no | n/a | n/a | n/a |
| 119g | 2026-11-28 | 107,12 $ | 93,92 $ | 69,73 $ / 105,30 $ | no | n/a | n/a | n/a |
| 126g | 2026-12-05 | 105,77 $ | 92,74 $ | 69,73 $ / 105,30 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 18 | 22,22% | 7,25% | 11,58% |
| 14g | 11 | 18,18% | 12,29% | 8,30% |
| 21g | 4 | 0,00% | 23,66% | 10,89% |
| 28g | 0 | n/a | n/a | n/a |
| 35g | 0 | n/a | n/a | n/a |
| 42g | 0 | n/a | n/a | n/a |
| 49g | 0 | n/a | n/a | n/a |
| 56g | 0 | n/a | n/a | n/a |
| 63g | 0 | n/a | n/a | n/a |
| 70g | 0 | n/a | n/a | n/a |
| 77g | 0 | n/a | n/a | n/a |
| 84g | 0 | n/a | n/a | n/a |
| 91g | 0 | n/a | n/a | n/a |
| 98g | 0 | n/a | n/a | n/a |
| 105g | 0 | n/a | n/a | n/a |
| 112g | 0 | n/a | n/a | n/a |
| 119g | 0 | n/a | n/a | n/a |
| 126g | 0 | n/a | n/a | n/a |

## Regola di lettura

- La somiglianza strutturale descrive la forma.
- Il gap ancorato descrive la distanza reale dal percorso.
- Lo scenario riancorato non dimostra che il frattale sia valido.
- Prima di pesare il modulo servono milestone maturate e un errore ancorato accettabile.
<!-- FRACTAL_PATH_TRACKER_END -->
