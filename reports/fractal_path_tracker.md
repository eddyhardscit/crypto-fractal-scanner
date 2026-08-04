<!-- FRACTAL_PATH_TRACKER_START -->
# Tracking percorso frattale SOL/BTC

Generato: 2026-08-04 05:16 UTC

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-08-04**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-01-19**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **73,72 $**
- Verdetto principale: **ANALOGIA DEBOLE / SCENARIO SECONDARIO**
- Somiglianza strutturale: **+57,08%**
- Aderenza live principale: **+70,18%**
- Errore medio live principale: **14,91%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE SOLO DI CONTESTO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **59**
- Osservazioni inclusive dal bottom: **60**
- Osservazioni da inizio programma/scanner: **33**
- Errore assoluto medio dal bottom: **10,91%**
- Errore assoluto medio da inizio programma: **14,91%**
- Gap firmato medio ultimi 7 giorni: **-10,63%**
- Errore assoluto medio ultimi 7 giorni: **10,63%**
- Gap ultimo giorno: **-11,25%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **-11,25%**
- Gap firmato medio 7g: **-10,63%**
- Errore assoluto medio 7g: **10,63%**
- Variazione recente gap: **+2,57%**
- Stato gap: **SOTTO IL FRATTALE**
- Trend gap: **SOL e sotto il percorso ancorato ma sta recuperando**

Soglie operative del grafico:

- entro **±5%**: percorso vicino;
- tra **±5% e ±12%**: deviazione gestibile;
- oltre **±12%**: frattale non abbastanza aderente per conferma operativa;
- oltre **±18%**: disallineamento marcato.

## Ultimi giorni del confronto ancorato

|   Giorno | Data SOL   | Data BTC eq.   | SOL reale   | Percorso ancorato   | Gap firmato   | Fase                |
|---------:|:-----------|:---------------|:------------|:--------------------|:--------------|:--------------------|
| 50 | 2026-07-26 | 2023-01-10 | 76,60 $ | 68,73 $ | +11,46% | da inizio programma |
| 51 | 2026-07-27 | 2023-01-11 | 74,14 $ | 70,65 $ | +4,94% | da inizio programma |
| 52 | 2026-07-28 | 2023-01-12 | 73,70 $ | 74,33 $ | -0,85% | da inizio programma |
| 53 | 2026-07-29 | 2023-01-13 | 73,60 $ | 78,43 $ | -6,16% | da inizio programma |
| 54 | 2026-07-30 | 2023-01-14 | 74,47 $ | 82,63 $ | -9,88% | da inizio programma |
| 55 | 2026-07-31 | 2023-01-15 | 72,79 $ | 82,25 $ | -11,51% | da inizio programma |
| 56 | 2026-08-01 | 2023-01-16 | 71,87 $ | 83,39 $ | -13,82% | da inizio programma |
| 57 | 2026-08-02 | 2023-01-17 | 73,45 $ | 83,36 $ | -11,89% | da inizio programma |
| 58 | 2026-08-03 | 2023-01-18 | 73,45 $ | 81,50 $ | -9,88% | da inizio programma |
| 59 | 2026-08-04 | 2023-01-19 | 73,72 $ | 83,07 $ | -11,25% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-08-11 | 90,73 $ | 80,52 $ | 73,72 $ / 80,82 $ | no | n/a | n/a | n/a |
| 14g | 2026-08-18 | 92,46 $ | 82,06 $ | 73,72 $ / 83,12 $ | no | n/a | n/a | n/a |
| 21g | 2026-08-25 | 85,95 $ | 76,28 $ | 73,72 $ / 83,12 $ | no | n/a | n/a | n/a |
| 28g | 2026-09-01 | 93,06 $ | 82,59 $ | 73,72 $ / 84,98 $ | no | n/a | n/a | n/a |
| 35g | 2026-09-08 | 94,33 $ | 83,72 $ | 73,72 $ / 86,80 $ | no | n/a | n/a | n/a |
| 42g | 2026-09-15 | 92,48 $ | 82,07 $ | 73,72 $ / 86,80 $ | no | n/a | n/a | n/a |
| 49g | 2026-09-22 | 80,21 $ | 71,19 $ | 71,19 $ / 86,80 $ | no | n/a | n/a | n/a |
| 56g | 2026-09-29 | 98,69 $ | 87,59 $ | 70,58 $ / 87,59 $ | no | n/a | n/a | n/a |
| 63g | 2026-10-06 | 111,61 $ | 99,06 $ | 70,58 $ / 99,06 $ | no | n/a | n/a | n/a |
| 70g | 2026-10-13 | 110,43 $ | 98,01 $ | 70,58 $ / 99,11 $ | no | n/a | n/a | n/a |
| 77g | 2026-10-20 | 110,47 $ | 98,04 $ | 70,58 $ / 99,56 $ | no | n/a | n/a | n/a |
| 84g | 2026-10-27 | 119,75 $ | 106,28 $ | 70,58 $ / 106,28 $ | no | n/a | n/a | n/a |
| 91g | 2026-11-03 | 111,27 $ | 98,75 $ | 70,58 $ / 106,58 $ | no | n/a | n/a | n/a |
| 98g | 2026-11-10 | 116,10 $ | 103,04 $ | 70,58 $ / 106,58 $ | no | n/a | n/a | n/a |
| 105g | 2026-11-17 | 113,64 $ | 100,85 $ | 70,58 $ / 106,58 $ | no | n/a | n/a | n/a |
| 112g | 2026-11-24 | 106,36 $ | 94,40 $ | 70,58 $ / 106,58 $ | no | n/a | n/a | n/a |
| 119g | 2026-12-01 | 105,70 $ | 93,81 $ | 70,58 $ / 106,58 $ | no | n/a | n/a | n/a |
| 126g | 2026-12-08 | 104,30 $ | 92,56 $ | 70,58 $ / 106,58 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 21 | 23,81% | 8,55% | 11,68% |
| 14g | 14 | 7,14% | 14,86% | 9,27% |
| 21g | 7 | 0,00% | 23,98% | 11,67% |
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
