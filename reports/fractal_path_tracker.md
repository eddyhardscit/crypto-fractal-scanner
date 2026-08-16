<!-- FRACTAL_PATH_TRACKER_START -->
# Tracking percorso frattale SOL/BTC

Generato: 2026-08-16 05:34 UTC

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-08-16**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-01-31**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **75,31 $**
- Verdetto principale: **ANALOGIA DEBOLE / SCENARIO SECONDARIO**
- Somiglianza strutturale: **+57,72%**
- Aderenza live principale: **+69,10%**
- Errore medio live principale: **15,45%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE SOLO DI CONTESTO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **71**
- Osservazioni inclusive dal bottom: **72**
- Osservazioni da inizio programma/scanner: **45**
- Errore assoluto medio dal bottom: **11,92%**
- Errore assoluto medio da inizio programma: **15,45%**
- Gap firmato medio ultimi 7 giorni: **-16,97%**
- Errore assoluto medio ultimi 7 giorni: **16,97%**
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
- Gap firmato medio 7g: **-16,97%**
- Errore assoluto medio 7g: **16,97%**
- Variazione recente gap: **-1,34%**
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
| 62 | 2026-08-07 | 2023-01-22 | 73,64 $ | 89,50 $ | -17,72% | da inizio programma |
| 63 | 2026-08-08 | 2023-01-23 | 75,97 $ | 90,34 $ | -15,91% | da inizio programma |
| 64 | 2026-08-09 | 2023-01-24 | 76,21 $ | 89,17 $ | -14,53% | da inizio programma |
| 65 | 2026-08-10 | 2023-01-25 | 75,95 $ | 91,07 $ | -16,60% | da inizio programma |
| 66 | 2026-08-11 | 2023-01-26 | 76,20 $ | 90,73 $ | -16,02% | da inizio programma |
| 67 | 2026-08-12 | 2023-01-27 | 75,53 $ | 90,91 $ | -16,93% | da inizio programma |
| 68 | 2026-08-13 | 2023-01-28 | 76,18 $ | 90,72 $ | -16,03% | da inizio programma |
| 69 | 2026-08-14 | 2023-01-29 | 75,33 $ | 93,65 $ | -19,57% | da inizio programma |
| 70 | 2026-08-15 | 2023-01-30 | 75,33 $ | 89,97 $ | -16,28% | da inizio programma |
| 71 | 2026-08-16 | 2023-01-31 | 75,31 $ | 91,15 $ | -17,38% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-08-23 | 91,64 $ | 75,72 $ | 74,08 $ / 77,21 $ | no | n/a | n/a | n/a |
| 14g | 2026-08-30 | 87,53 $ | 72,32 $ | 70,47 $ / 77,21 $ | no | n/a | n/a | n/a |
| 21g | 2026-09-06 | 96,26 $ | 79,53 $ | 70,47 $ / 80,81 $ | no | n/a | n/a | n/a |
| 28g | 2026-09-13 | 91,18 $ | 75,34 $ | 70,47 $ / 80,81 $ | no | n/a | n/a | n/a |
| 35g | 2026-09-20 | 87,53 $ | 72,32 $ | 70,47 $ / 80,81 $ | no | n/a | n/a | n/a |
| 42g | 2026-09-27 | 97,48 $ | 80,54 $ | 65,70 $ / 80,81 $ | no | n/a | n/a | n/a |
| 49g | 2026-10-04 | 110,99 $ | 91,70 $ | 65,70 $ / 91,70 $ | no | n/a | n/a | n/a |
| 56g | 2026-10-11 | 107,42 $ | 88,75 $ | 65,70 $ / 92,22 $ | no | n/a | n/a | n/a |
| 63g | 2026-10-18 | 110,96 $ | 91,68 $ | 65,70 $ / 92,69 $ | no | n/a | n/a | n/a |
| 70g | 2026-10-25 | 119,10 $ | 98,40 $ | 65,70 $ / 98,40 $ | no | n/a | n/a | n/a |
| 77g | 2026-11-01 | 119,74 $ | 98,93 $ | 65,70 $ / 99,22 $ | no | n/a | n/a | n/a |
| 84g | 2026-11-08 | 111,51 $ | 92,13 $ | 65,70 $ / 99,22 $ | no | n/a | n/a | n/a |
| 91g | 2026-11-15 | 112,98 $ | 93,34 $ | 65,70 $ / 99,22 $ | no | n/a | n/a | n/a |
| 98g | 2026-11-22 | 108,95 $ | 90,02 $ | 65,70 $ / 99,22 $ | no | n/a | n/a | n/a |
| 105g | 2026-11-29 | 106,50 $ | 87,99 $ | 65,70 $ / 99,22 $ | no | n/a | n/a | n/a |
| 112g | 2026-12-06 | 107,25 $ | 88,61 $ | 65,70 $ / 99,22 $ | no | n/a | n/a | n/a |
| 119g | 2026-12-13 | 109,13 $ | 90,16 $ | 65,70 $ / 99,22 $ | no | n/a | n/a | n/a |
| 126g | 2026-12-20 | 107,30 $ | 88,65 $ | 65,70 $ / 99,22 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 33 | 42,42% | 7,13% | 13,71% |
| 14g | 26 | 34,62% | 15,94% | 13,10% |
| 21g | 19 | 26,32% | 26,17% | 15,39% |
| 28g | 12 | 33,33% | 28,80% | 16,70% |
| 35g | 5 | 0,00% | 29,19% | 17,74% |
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
