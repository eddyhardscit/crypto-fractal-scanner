<!-- FRACTAL_PATH_TRACKER_START -->
# Tracking percorso frattale SOL/BTC

Generato: 2026-08-14 10:52 UTC

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-08-14**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-01-29**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **75,37 $**
- Verdetto principale: **ANALOGIA DEBOLE / SCENARIO SECONDARIO**
- Somiglianza strutturale: **+57,44%**
- Aderenza live principale: **+69,23%**
- Errore medio live principale: **15,39%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE SOLO DI CONTESTO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **69**
- Osservazioni inclusive dal bottom: **70**
- Osservazioni da inizio programma/scanner: **43**
- Errore assoluto medio dal bottom: **11,78%**
- Errore assoluto medio da inizio programma: **15,39%**
- Gap firmato medio ultimi 7 giorni: **-16,51%**
- Errore assoluto medio ultimi 7 giorni: **16,51%**
- Gap ultimo giorno: **-19,52%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **-19,52%**
- Gap firmato medio 7g: **-16,51%**
- Errore assoluto medio 7g: **16,51%**
- Variazione recente gap: **-3,50%**
- Stato gap: **DISALLINEATO SOTTO IL FRATTALE**
- Trend gap: **SOL si sta allontanando sotto il percorso ancorato**

Soglie operative del grafico:

- entro **±5%**: percorso vicino;
- tra **±5% e ±12%**: deviazione gestibile;
- oltre **±12%**: frattale non abbastanza aderente per conferma operativa;
- oltre **±18%**: disallineamento marcato.

## Ultimi giorni del confronto ancorato

|   Giorno | Data SOL   | Data BTC eq.   | SOL reale   | Percorso ancorato   | Gap firmato   | Fase                |
|---------:|:-----------|:---------------|:------------|:--------------------|:--------------|:--------------------|
| 60 | 2026-08-05 | 2023-01-20 | 73,96 $ | 89,33 $ | -17,20% | da inizio programma |
| 61 | 2026-08-06 | 2023-01-21 | 72,58 $ | 89,73 $ | -19,11% | da inizio programma |
| 62 | 2026-08-07 | 2023-01-22 | 73,64 $ | 89,50 $ | -17,72% | da inizio programma |
| 63 | 2026-08-08 | 2023-01-23 | 75,97 $ | 90,34 $ | -15,91% | da inizio programma |
| 64 | 2026-08-09 | 2023-01-24 | 76,21 $ | 89,17 $ | -14,53% | da inizio programma |
| 65 | 2026-08-10 | 2023-01-25 | 75,95 $ | 91,07 $ | -16,60% | da inizio programma |
| 66 | 2026-08-11 | 2023-01-26 | 76,20 $ | 90,73 $ | -16,02% | da inizio programma |
| 67 | 2026-08-12 | 2023-01-27 | 75,53 $ | 90,91 $ | -16,93% | da inizio programma |
| 68 | 2026-08-13 | 2023-01-28 | 76,18 $ | 90,72 $ | -16,03% | da inizio programma |
| 69 | 2026-08-14 | 2023-01-29 | 75,37 $ | 93,65 $ | -19,52% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-08-21 | 90,43 $ | 72,77 $ | 72,41 $ / 75,37 $ | no | n/a | n/a | n/a |
| 14g | 2026-08-28 | 85,83 $ | 69,07 $ | 68,64 $ / 75,37 $ | no | n/a | n/a | n/a |
| 21g | 2026-09-04 | 95,83 $ | 77,12 $ | 68,64 $ / 78,12 $ | no | n/a | n/a | n/a |
| 28g | 2026-09-11 | 92,81 $ | 74,69 $ | 68,64 $ / 78,71 $ | no | n/a | n/a | n/a |
| 35g | 2026-09-18 | 88,38 $ | 71,12 $ | 68,64 $ / 78,71 $ | no | n/a | n/a | n/a |
| 42g | 2026-09-25 | 87,31 $ | 70,26 $ | 64,00 $ / 78,71 $ | no | n/a | n/a | n/a |
| 49g | 2026-10-02 | 110,45 $ | 88,89 $ | 64,00 $ / 88,89 $ | no | n/a | n/a | n/a |
| 56g | 2026-10-09 | 110,28 $ | 88,75 $ | 64,00 $ / 89,82 $ | no | n/a | n/a | n/a |
| 63g | 2026-10-16 | 111,08 $ | 89,40 $ | 64,00 $ / 90,28 $ | no | n/a | n/a | n/a |
| 70g | 2026-10-23 | 111,61 $ | 89,82 $ | 64,00 $ / 90,28 $ | no | n/a | n/a | n/a |
| 77g | 2026-10-30 | 119,42 $ | 96,11 $ | 64,00 $ / 96,65 $ | no | n/a | n/a | n/a |
| 84g | 2026-11-06 | 108,69 $ | 87,47 $ | 64,00 $ / 96,65 $ | no | n/a | n/a | n/a |
| 91g | 2026-11-13 | 115,30 $ | 92,79 $ | 64,00 $ / 96,65 $ | no | n/a | n/a | n/a |
| 98g | 2026-11-20 | 112,09 $ | 90,21 $ | 64,00 $ / 96,65 $ | no | n/a | n/a | n/a |
| 105g | 2026-11-27 | 106,09 $ | 85,38 $ | 64,00 $ / 96,65 $ | no | n/a | n/a | n/a |
| 112g | 2026-12-04 | 105,39 $ | 84,81 $ | 64,00 $ / 96,65 $ | no | n/a | n/a | n/a |
| 119g | 2026-12-11 | 110,64 $ | 89,04 $ | 64,00 $ / 96,65 $ | no | n/a | n/a | n/a |
| 126g | 2026-12-18 | 106,83 $ | 85,97 $ | 64,00 $ / 96,65 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 31 | 41,94% | 7,44% | 13,50% |
| 14g | 24 | 29,17% | 16,82% | 12,76% |
| 21g | 17 | 17,65% | 26,43% | 15,19% |
| 28g | 10 | 30,00% | 29,04% | 16,66% |
| 35g | 3 | 0,00% | 29,53% | 19,52% |
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
