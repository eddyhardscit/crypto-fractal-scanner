<!-- FRACTAL_PATH_TRACKER_START -->
# Tracking percorso frattale SOL/BTC

Generato: 2026-08-31 05:32 UTC

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-08-31**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-02-15**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **102,67 $**
- Verdetto principale: **ANALOGIA DEBOLE / SCENARIO SECONDARIO**
- Somiglianza strutturale: **+64,60%**
- Aderenza live principale: **+70,23%**
- Errore medio live principale: **14,88%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE SOLO DI CONTESTO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **86**
- Osservazioni inclusive dal bottom: **87**
- Osservazioni da inizio programma/scanner: **60**
- Errore assoluto medio dal bottom: **12,13%**
- Errore assoluto medio da inizio programma: **14,88%**
- Gap firmato medio ultimi 7 giorni: **+18,24%**
- Errore assoluto medio ultimi 7 giorni: **18,24%**
- Gap ultimo giorno: **+7,22%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **+7,22%**
- Gap firmato medio 7g: **+18,24%**
- Errore assoluto medio 7g: **18,24%**
- Variazione recente gap: **-14,10%**
- Stato gap: **SOPRA IL FRATTALE**
- Trend gap: **SOL resta sopra il percorso ancorato, ma sta riducendo il distacco**

Soglie operative del grafico:

- entro **±5%**: percorso vicino;
- tra **±5% e ±12%**: deviazione gestibile;
- oltre **±12%**: frattale non abbastanza aderente per conferma operativa;
- oltre **±18%**: disallineamento marcato.

## Ultimi giorni del confronto ancorato

|   Giorno | Data SOL   | Data BTC eq.   | SOL reale   | Percorso ancorato   | Gap firmato   | Fase                |
|---------:|:-----------|:---------------|:------------|:--------------------|:--------------|:--------------------|
| 77 | 2026-08-22 | 2023-02-06 | 93,91 $ | 89,66 $ | +4,75% | da inizio programma |
| 78 | 2026-08-23 | 2023-02-07 | 95,44 $ | 91,64 $ | +4,15% | da inizio programma |
| 79 | 2026-08-24 | 2023-02-08 | 98,56 $ | 90,36 $ | +9,07% | da inizio programma |
| 80 | 2026-08-25 | 2023-02-09 | 96,60 $ | 85,95 $ | +12,39% | da inizio programma |
| 81 | 2026-08-26 | 2023-02-10 | 102,17 $ | 85,29 $ | +19,79% | da inizio programma |
| 82 | 2026-08-27 | 2023-02-11 | 109,21 $ | 86,15 $ | +26,76% | da inizio programma |
| 83 | 2026-08-28 | 2023-02-12 | 104,13 $ | 85,83 $ | +21,32% | da inizio programma |
| 84 | 2026-08-29 | 2023-02-13 | 104,13 $ | 85,91 $ | +21,21% | da inizio programma |
| 85 | 2026-08-30 | 2023-02-14 | 104,13 $ | 87,53 $ | +18,96% | da inizio programma |
| 86 | 2026-08-31 | 2023-02-15 | 102,67 $ | 95,75 $ | +7,22% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-09-07 | 95,29 $ | 102,17 $ | 99,78 $ / 104,87 $ | no | n/a | n/a | n/a |
| 14g | 2026-09-14 | 93,15 $ | 99,88 $ | 97,77 $ / 104,87 $ | no | n/a | n/a | n/a |
| 21g | 2026-09-21 | 85,55 $ | 91,73 $ | 91,73 $ / 104,87 $ | no | n/a | n/a | n/a |
| 28g | 2026-09-28 | 96,02 $ | 102,96 $ | 85,27 $ / 104,87 $ | no | n/a | n/a | n/a |
| 35g | 2026-10-05 | 107,57 $ | 115,34 $ | 85,27 $ / 119,01 $ | no | n/a | n/a | n/a |
| 42g | 2026-10-12 | 111,67 $ | 119,74 $ | 85,27 $ / 119,74 $ | no | n/a | n/a | n/a |
| 49g | 2026-10-19 | 111,00 $ | 119,02 $ | 85,27 $ / 120,29 $ | no | n/a | n/a | n/a |
| 56g | 2026-10-26 | 118,72 $ | 127,30 $ | 85,27 $ / 127,71 $ | no | n/a | n/a | n/a |
| 63g | 2026-11-02 | 113,54 $ | 121,74 $ | 85,27 $ / 128,76 $ | no | n/a | n/a | n/a |
| 70g | 2026-11-09 | 111,96 $ | 120,05 $ | 85,27 $ / 128,76 $ | no | n/a | n/a | n/a |
| 77g | 2026-11-16 | 114,26 $ | 122,52 $ | 85,27 $ / 128,76 $ | no | n/a | n/a | n/a |
| 84g | 2026-11-23 | 108,81 $ | 116,67 $ | 85,27 $ / 128,76 $ | no | n/a | n/a | n/a |
| 91g | 2026-11-30 | 107,93 $ | 115,73 $ | 85,27 $ / 128,76 $ | no | n/a | n/a | n/a |
| 98g | 2026-12-07 | 103,74 $ | 111,23 $ | 85,27 $ / 128,76 $ | no | n/a | n/a | n/a |
| 105g | 2026-12-14 | 107,22 $ | 114,97 $ | 85,27 $ / 128,76 $ | no | n/a | n/a | n/a |
| 112g | 2026-12-21 | 103,78 $ | 111,28 $ | 85,27 $ / 128,76 $ | no | n/a | n/a | n/a |
| 119g | 2026-12-28 | 98,97 $ | 106,12 $ | 85,27 $ / 128,76 $ | no | n/a | n/a | n/a |
| 126g | 2027-01-04 | 118,28 $ | 126,83 $ | 85,27 $ / 128,76 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 46 | 34,78% | 11,56% | 13,88% |
| 14g | 39 | 28,21% | 19,77% | 12,59% |
| 21g | 34 | 17,65% | 26,76% | 14,35% |
| 28g | 27 | 40,74% | 24,93% | 14,59% |
| 35g | 20 | 60,00% | 16,14% | 13,94% |
| 42g | 13 | 100,00% | 8,55% | 13,56% |
| 49g | 6 | 100,00% | 5,27% | 17,18% |
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
