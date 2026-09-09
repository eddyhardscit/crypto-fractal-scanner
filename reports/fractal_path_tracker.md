<!-- FRACTAL_PATH_TRACKER_START -->
# Tracking percorso frattale SOL/BTC

Generato: 2026-09-09 05:32 UTC

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-09-09**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-02-24**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **104,43 $**
- Verdetto principale: **ANALOGIA DEBOLE / SCENARIO SECONDARIO**
- Somiglianza strutturale: **+69,05%**
- Aderenza live principale: **+71,98%**
- Errore medio live principale: **14,01%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE SOLO DI CONTESTO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **95**
- Osservazioni inclusive dal bottom: **96**
- Osservazioni da inizio programma/scanner: **69**
- Errore assoluto medio dal bottom: **11,76%**
- Errore assoluto medio da inizio programma: **14,01%**
- Gap firmato medio ultimi 7 giorni: **+9,00%**
- Errore assoluto medio ultimi 7 giorni: **9,00%**
- Gap ultimo giorno: **+14,28%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **+14,28%**
- Gap firmato medio 7g: **+9,00%**
- Errore assoluto medio 7g: **9,00%**
- Variazione recente gap: **+3,69%**
- Stato gap: **IN DEVIAZIONE SOPRA IL FRATTALE**
- Trend gap: **SOL sta aumentando il distacco sopra il percorso ancorato**

Soglie operative del grafico:

- entro **±5%**: percorso vicino;
- tra **±5% e ±12%**: deviazione gestibile;
- oltre **±12%**: frattale non abbastanza aderente per conferma operativa;
- oltre **±18%**: disallineamento marcato.

## Ultimi giorni del confronto ancorato

|   Giorno | Data SOL   | Data BTC eq.   | SOL reale   | Percorso ancorato   | Gap firmato   | Fase                |
|---------:|:-----------|:---------------|:------------|:--------------------|:--------------|:--------------------|
| 86 | 2026-08-31 | 2023-02-15 | 103,00 $ | 95,75 $ | +7,56% | da inizio programma |
| 87 | 2026-09-01 | 2023-02-16 | 99,99 $ | 93,06 $ | +7,45% | da inizio programma |
| 88 | 2026-09-02 | 2023-02-17 | 100,39 $ | 96,77 $ | +3,74% | da inizio programma |
| 89 | 2026-09-03 | 2023-02-18 | 103,98 $ | 97,07 $ | +7,12% | da inizio programma |
| 90 | 2026-09-04 | 2023-02-19 | 101,95 $ | 95,83 $ | +6,38% | da inizio programma |
| 91 | 2026-09-05 | 2023-02-20 | 103,19 $ | 97,81 $ | +5,50% | da inizio programma |
| 92 | 2026-09-06 | 2023-02-21 | 106,45 $ | 96,26 $ | +10,58% | da inizio programma |
| 93 | 2026-09-07 | 2023-02-22 | 103,87 $ | 95,29 $ | +9,01% | da inizio programma |
| 94 | 2026-09-08 | 2023-02-23 | 103,87 $ | 94,33 $ | +10,10% | da inizio programma |
| 95 | 2026-09-09 | 2023-02-24 | 104,43 $ | 91,38 $ | +14,28% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-09-16 | 88,09 $ | 100,67 $ | 100,67 $ / 106,45 $ | no | n/a | n/a | n/a |
| 14g | 2026-09-23 | 79,52 $ | 90,88 $ | 90,88 $ / 106,45 $ | no | n/a | n/a | n/a |
| 21g | 2026-09-30 | 108,03 $ | 123,45 $ | 90,88 $ / 123,45 $ | no | n/a | n/a | n/a |
| 28g | 2026-10-07 | 108,30 $ | 123,77 $ | 90,88 $ / 127,55 $ | no | n/a | n/a | n/a |
| 35g | 2026-10-14 | 112,18 $ | 128,20 $ | 90,88 $ / 128,20 $ | no | n/a | n/a | n/a |
| 42g | 2026-10-21 | 110,01 $ | 125,71 $ | 90,88 $ / 128,20 $ | no | n/a | n/a | n/a |
| 49g | 2026-10-28 | 120,09 $ | 137,24 $ | 90,88 $ / 137,24 $ | no | n/a | n/a | n/a |
| 56g | 2026-11-04 | 107,45 $ | 122,79 $ | 90,88 $ / 137,24 $ | no | n/a | n/a | n/a |
| 63g | 2026-11-11 | 115,58 $ | 132,08 $ | 90,88 $ / 137,24 $ | no | n/a | n/a | n/a |
| 70g | 2026-11-18 | 116,34 $ | 132,95 $ | 90,88 $ / 137,24 $ | no | n/a | n/a | n/a |
| 77g | 2026-11-25 | 105,59 $ | 120,67 $ | 90,88 $ / 137,24 $ | no | n/a | n/a | n/a |
| 84g | 2026-12-02 | 105,93 $ | 121,05 $ | 90,88 $ / 137,24 $ | no | n/a | n/a | n/a |
| 91g | 2026-12-09 | 105,25 $ | 120,28 $ | 90,88 $ / 137,24 $ | no | n/a | n/a | n/a |
| 98g | 2026-12-16 | 107,34 $ | 122,67 $ | 90,88 $ / 137,24 $ | no | n/a | n/a | n/a |
| 105g | 2026-12-23 | 104,31 $ | 119,21 $ | 90,88 $ / 137,24 $ | no | n/a | n/a | n/a |
| 112g | 2026-12-30 | 103,71 $ | 118,52 $ | 90,88 $ / 137,24 $ | no | n/a | n/a | n/a |
| 119g | 2027-01-06 | 120,92 $ | 138,18 $ | 90,88 $ / 138,18 $ | no | n/a | n/a | n/a |
| 126g | 2027-01-13 | 120,06 $ | 137,20 $ | 90,88 $ / 138,18 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 55 | 36,36% | 11,03% | 12,91% |
| 14g | 48 | 27,08% | 18,17% | 11,73% |
| 21g | 41 | 14,63% | 27,72% | 13,39% |
| 28g | 35 | 31,43% | 25,67% | 12,85% |
| 35g | 29 | 44,83% | 17,59% | 12,02% |
| 42g | 22 | 90,91% | 8,28% | 11,14% |
| 49g | 15 | 100,00% | 6,13% | 10,95% |
| 56g | 8 | 100,00% | 7,13% | 9,31% |
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
