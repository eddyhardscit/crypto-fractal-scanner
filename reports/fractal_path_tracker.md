<!-- FRACTAL_PATH_TRACKER_START -->
# Tracking percorso frattale SOL/BTC

Generato: 2026-08-23 05:32 UTC

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-08-23**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-02-07**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **93,19 $**
- Verdetto principale: **ANALOGIA DEBOLE / SCENARIO SECONDARIO**
- Somiglianza strutturale: **+62,81%**
- Aderenza live principale: **+71,02%**
- Errore medio live principale: **14,49%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE SOLO DI CONTESTO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **78**
- Osservazioni inclusive dal bottom: **79**
- Osservazioni da inizio programma/scanner: **52**
- Errore assoluto medio dal bottom: **11,60%**
- Errore assoluto medio da inizio programma: **14,49%**
- Gap firmato medio ultimi 7 giorni: **-5,42%**
- Errore assoluto medio ultimi 7 giorni: **8,19%**
- Gap ultimo giorno: **+1,69%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **+1,69%**
- Gap firmato medio 7g: **-5,42%**
- Errore assoluto medio 7g: **8,19%**
- Variazione recente gap: **+6,34%**
- Stato gap: **VICINO AL FRATTALE**
- Trend gap: **SOL sta aumentando il distacco sopra il percorso ancorato**

Soglie operative del grafico:

- entro **±5%**: percorso vicino;
- tra **±5% e ±12%**: deviazione gestibile;
- oltre **±12%**: frattale non abbastanza aderente per conferma operativa;
- oltre **±18%**: disallineamento marcato.

## Ultimi giorni del confronto ancorato

|   Giorno | Data SOL   | Data BTC eq.   | SOL reale   | Percorso ancorato   | Gap firmato   | Fase                |
|---------:|:-----------|:---------------|:------------|:--------------------|:--------------|:--------------------|
| 69 | 2026-08-14 | 2023-01-29 | 75,33 $ | 93,65 $ | -19,57% | da inizio programma |
| 70 | 2026-08-15 | 2023-01-30 | 75,27 $ | 89,97 $ | -16,34% | da inizio programma |
| 71 | 2026-08-16 | 2023-01-31 | 74,54 $ | 91,15 $ | -18,22% | da inizio programma |
| 72 | 2026-08-17 | 2023-02-01 | 75,94 $ | 93,45 $ | -18,74% | da inizio programma |
| 73 | 2026-08-18 | 2023-02-02 | 77,03 $ | 92,46 $ | -16,69% | da inizio programma |
| 74 | 2026-08-19 | 2023-02-03 | 85,37 $ | 92,37 $ | -7,58% | da inizio programma |
| 75 | 2026-08-20 | 2023-02-04 | 87,64 $ | 91,91 $ | -4,65% | da inizio programma |
| 76 | 2026-08-21 | 2023-02-05 | 93,65 $ | 90,43 $ | +3,57% | da inizio programma |
| 77 | 2026-08-22 | 2023-02-06 | 93,65 $ | 89,66 $ | +4,46% | da inizio programma |
| 78 | 2026-08-23 | 2023-02-07 | 93,19 $ | 91,64 $ | +1,69% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-08-30 | 87,53 $ | 89,01 $ | 86,73 $ / 93,19 $ | no | n/a | n/a | n/a |
| 14g | 2026-09-06 | 96,26 $ | 97,88 $ | 86,73 $ / 99,46 $ | no | n/a | n/a | n/a |
| 21g | 2026-09-13 | 91,18 $ | 92,72 $ | 86,73 $ / 99,46 $ | no | n/a | n/a | n/a |
| 28g | 2026-09-20 | 87,53 $ | 89,01 $ | 86,73 $ / 99,46 $ | no | n/a | n/a | n/a |
| 35g | 2026-09-27 | 97,48 $ | 99,13 $ | 80,86 $ / 99,46 $ | no | n/a | n/a | n/a |
| 42g | 2026-10-04 | 110,99 $ | 112,86 $ | 80,86 $ / 112,86 $ | no | n/a | n/a | n/a |
| 49g | 2026-10-11 | 107,42 $ | 109,23 $ | 80,86 $ / 113,50 $ | no | n/a | n/a | n/a |
| 56g | 2026-10-18 | 110,96 $ | 112,83 $ | 80,86 $ / 114,08 $ | no | n/a | n/a | n/a |
| 63g | 2026-10-25 | 119,10 $ | 121,11 $ | 80,86 $ / 121,11 $ | no | n/a | n/a | n/a |
| 70g | 2026-11-01 | 119,74 $ | 121,76 $ | 80,86 $ / 122,12 $ | no | n/a | n/a | n/a |
| 77g | 2026-11-08 | 111,51 $ | 113,39 $ | 80,86 $ / 122,12 $ | no | n/a | n/a | n/a |
| 84g | 2026-11-15 | 112,98 $ | 114,89 $ | 80,86 $ / 122,12 $ | no | n/a | n/a | n/a |
| 91g | 2026-11-22 | 108,95 $ | 110,79 $ | 80,86 $ / 122,12 $ | no | n/a | n/a | n/a |
| 98g | 2026-11-29 | 106,50 $ | 108,30 $ | 80,86 $ / 122,12 $ | no | n/a | n/a | n/a |
| 105g | 2026-12-06 | 107,25 $ | 109,06 $ | 80,86 $ / 122,12 $ | no | n/a | n/a | n/a |
| 112g | 2026-12-13 | 109,13 $ | 110,97 $ | 80,86 $ / 122,12 $ | no | n/a | n/a | n/a |
| 119g | 2026-12-20 | 107,30 $ | 109,11 $ | 80,86 $ / 122,12 $ | no | n/a | n/a | n/a |
| 126g | 2026-12-27 | 102,10 $ | 103,82 $ | 80,86 $ / 122,12 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 38 | 42,11% | 8,33% | 13,09% |
| 14g | 33 | 33,33% | 16,10% | 12,02% |
| 21g | 26 | 23,08% | 22,95% | 13,33% |
| 28g | 19 | 52,63% | 24,32% | 13,25% |
| 35g | 12 | 58,33% | 22,94% | 11,15% |
| 42g | 5 | 100,00% | 14,55% | 3,24% |
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
