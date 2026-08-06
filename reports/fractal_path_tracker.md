<!-- FRACTAL_PATH_TRACKER_START -->
# Tracking percorso frattale SOL/BTC

Generato: 2026-08-06 05:15 UTC

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-08-06**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-01-21**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **74,13 $**
- Verdetto principale: **ANALOGIA DEBOLE / SCENARIO SECONDARIO**
- Somiglianza strutturale: **+56,78%**
- Aderenza live principale: **+69,89%**
- Errore medio live principale: **15,05%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE SOLO DI CONTESTO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **61**
- Osservazioni inclusive dal bottom: **62**
- Osservazioni da inizio programma/scanner: **35**
- Errore assoluto medio dal bottom: **11,12%**
- Errore assoluto medio da inizio programma: **15,05%**
- Gap firmato medio ultimi 7 giorni: **-13,31%**
- Errore assoluto medio ultimi 7 giorni: **13,31%**
- Gap ultimo giorno: **-17,38%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **-17,38%**
- Gap firmato medio 7g: **-13,31%**
- Errore assoluto medio 7g: **13,31%**
- Variazione recente gap: **-7,54%**
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
| 52 | 2026-07-28 | 2023-01-12 | 73,70 $ | 74,33 $ | -0,85% | da inizio programma |
| 53 | 2026-07-29 | 2023-01-13 | 73,60 $ | 78,43 $ | -6,16% | da inizio programma |
| 54 | 2026-07-30 | 2023-01-14 | 74,47 $ | 82,63 $ | -9,88% | da inizio programma |
| 55 | 2026-07-31 | 2023-01-15 | 72,79 $ | 82,25 $ | -11,51% | da inizio programma |
| 56 | 2026-08-01 | 2023-01-16 | 71,87 $ | 83,39 $ | -13,82% | da inizio programma |
| 57 | 2026-08-02 | 2023-01-17 | 73,45 $ | 83,36 $ | -11,89% | da inizio programma |
| 58 | 2026-08-03 | 2023-01-18 | 73,47 $ | 81,50 $ | -9,85% | da inizio programma |
| 59 | 2026-08-04 | 2023-01-19 | 73,72 $ | 83,07 $ | -11,25% | da inizio programma |
| 60 | 2026-08-05 | 2023-01-20 | 73,72 $ | 89,33 $ | -17,48% | da inizio programma |
| 61 | 2026-08-06 | 2023-01-21 | 74,13 $ | 89,73 $ | -17,38% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-08-13 | 90,72 $ | 74,95 $ | 73,67 $ / 75,24 $ | no | n/a | n/a | n/a |
| 14g | 2026-08-20 | 91,91 $ | 75,93 $ | 73,67 $ / 77,37 $ | no | n/a | n/a | n/a |
| 21g | 2026-08-27 | 86,15 $ | 71,18 $ | 70,46 $ / 77,37 $ | no | n/a | n/a | n/a |
| 28g | 2026-09-03 | 97,07 $ | 80,20 $ | 70,46 $ / 80,20 $ | no | n/a | n/a | n/a |
| 35g | 2026-09-10 | 91,29 $ | 75,42 $ | 70,46 $ / 80,81 $ | no | n/a | n/a | n/a |
| 42g | 2026-09-17 | 88,06 $ | 72,75 $ | 70,46 $ / 80,81 $ | no | n/a | n/a | n/a |
| 49g | 2026-09-24 | 81,28 $ | 67,15 $ | 65,70 $ / 80,81 $ | no | n/a | n/a | n/a |
| 56g | 2026-10-01 | 106,22 $ | 87,76 $ | 65,70 $ / 89,25 $ | no | n/a | n/a | n/a |
| 63g | 2026-10-08 | 108,31 $ | 89,48 $ | 65,70 $ / 92,21 $ | no | n/a | n/a | n/a |
| 70g | 2026-10-15 | 111,92 $ | 92,46 $ | 65,70 $ / 92,68 $ | no | n/a | n/a | n/a |
| 77g | 2026-10-22 | 110,09 $ | 90,96 $ | 65,70 $ / 92,68 $ | no | n/a | n/a | n/a |
| 84g | 2026-10-29 | 119,43 $ | 98,67 $ | 65,70 $ / 99,22 $ | no | n/a | n/a | n/a |
| 91g | 2026-11-05 | 109,58 $ | 90,53 $ | 65,70 $ / 99,22 $ | no | n/a | n/a | n/a |
| 98g | 2026-11-12 | 115,22 $ | 95,19 $ | 65,70 $ / 99,22 $ | no | n/a | n/a | n/a |
| 105g | 2026-11-19 | 113,86 $ | 94,07 $ | 65,70 $ / 99,22 $ | no | n/a | n/a | n/a |
| 112g | 2026-11-26 | 105,51 $ | 87,17 $ | 65,70 $ / 99,22 $ | no | n/a | n/a | n/a |
| 119g | 2026-12-03 | 106,87 $ | 88,29 $ | 65,70 $ / 99,22 $ | no | n/a | n/a | n/a |
| 126g | 2026-12-10 | 105,84 $ | 87,44 $ | 65,70 $ / 99,22 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 23 | 30,43% | 8,63% | 12,23% |
| 14g | 16 | 6,25% | 16,60% | 10,43% |
| 21g | 9 | 0,00% | 25,31% | 13,31% |
| 28g | 2 | 0,00% | 29,66% | n/a |
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
