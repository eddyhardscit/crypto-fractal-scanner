<!-- FRACTAL_PATH_TRACKER_START -->
# Tracking percorso frattale SOL/BTC

Generato: 2026-08-28 08:01 UTC

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-08-28**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-02-12**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **106,34 $**
- Verdetto principale: **ANALOGIA DEBOLE / SCENARIO SECONDARIO**
- Somiglianza strutturale: **+63,74%**
- Aderenza live principale: **+70,24%**
- Errore medio live principale: **14,88%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE SOLO DI CONTESTO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **83**
- Osservazioni inclusive dal bottom: **84**
- Osservazioni da inizio programma/scanner: **57**
- Errore assoluto medio dal bottom: **12,03%**
- Errore assoluto medio da inizio programma: **14,88%**
- Gap firmato medio ultimi 7 giorni: **+14,40%**
- Errore assoluto medio ultimi 7 giorni: **14,40%**
- Gap ultimo giorno: **+23,90%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **+23,90%**
- Gap firmato medio 7g: **+14,40%**
- Errore assoluto medio 7g: **14,40%**
- Variazione recente gap: **+11,50%**
- Stato gap: **DISALLINEATO SOPRA IL FRATTALE**
- Trend gap: **SOL sta aumentando il distacco sopra il percorso ancorato**

Soglie operative del grafico:

- entro **±5%**: percorso vicino;
- tra **±5% e ±12%**: deviazione gestibile;
- oltre **±12%**: frattale non abbastanza aderente per conferma operativa;
- oltre **±18%**: disallineamento marcato.

## Ultimi giorni del confronto ancorato

|   Giorno | Data SOL   | Data BTC eq.   | SOL reale   | Percorso ancorato   | Gap firmato   | Fase                |
|---------:|:-----------|:---------------|:------------|:--------------------|:--------------|:--------------------|
| 74 | 2026-08-19 | 2023-02-03 | 85,37 $ | 92,37 $ | -7,58% | da inizio programma |
| 75 | 2026-08-20 | 2023-02-04 | 87,64 $ | 91,91 $ | -4,65% | da inizio programma |
| 76 | 2026-08-21 | 2023-02-05 | 93,65 $ | 90,43 $ | +3,57% | da inizio programma |
| 77 | 2026-08-22 | 2023-02-06 | 93,91 $ | 89,66 $ | +4,75% | da inizio programma |
| 78 | 2026-08-23 | 2023-02-07 | 95,44 $ | 91,64 $ | +4,15% | da inizio programma |
| 79 | 2026-08-24 | 2023-02-08 | 98,56 $ | 90,36 $ | +9,07% | da inizio programma |
| 80 | 2026-08-25 | 2023-02-09 | 96,60 $ | 85,95 $ | +12,39% | da inizio programma |
| 81 | 2026-08-26 | 2023-02-10 | 102,17 $ | 85,29 $ | +19,79% | da inizio programma |
| 82 | 2026-08-27 | 2023-02-11 | 109,21 $ | 86,15 $ | +26,76% | da inizio programma |
| 83 | 2026-08-28 | 2023-02-12 | 106,34 $ | 85,83 $ | +23,90% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-09-04 | 95,83 $ | 118,73 $ | 106,34 $ / 120,26 $ | no | n/a | n/a | n/a |
| 14g | 2026-09-11 | 92,81 $ | 114,99 $ | 106,34 $ / 121,18 $ | no | n/a | n/a | n/a |
| 21g | 2026-09-18 | 88,38 $ | 109,50 $ | 106,34 $ / 121,18 $ | no | n/a | n/a | n/a |
| 28g | 2026-09-25 | 87,31 $ | 108,17 $ | 98,53 $ / 121,18 $ | no | n/a | n/a | n/a |
| 35g | 2026-10-02 | 110,45 $ | 136,85 $ | 98,53 $ / 136,85 $ | no | n/a | n/a | n/a |
| 42g | 2026-10-09 | 110,28 $ | 136,63 $ | 98,53 $ / 138,29 $ | no | n/a | n/a | n/a |
| 49g | 2026-10-16 | 111,08 $ | 137,63 $ | 98,53 $ / 138,99 $ | no | n/a | n/a | n/a |
| 56g | 2026-10-23 | 111,61 $ | 138,28 $ | 98,53 $ / 138,99 $ | no | n/a | n/a | n/a |
| 63g | 2026-10-30 | 119,42 $ | 147,96 $ | 98,53 $ / 148,79 $ | no | n/a | n/a | n/a |
| 70g | 2026-11-06 | 108,69 $ | 134,66 $ | 98,53 $ / 148,79 $ | no | n/a | n/a | n/a |
| 77g | 2026-11-13 | 115,30 $ | 142,85 $ | 98,53 $ / 148,79 $ | no | n/a | n/a | n/a |
| 84g | 2026-11-20 | 112,09 $ | 138,88 $ | 98,53 $ / 148,79 $ | no | n/a | n/a | n/a |
| 91g | 2026-11-27 | 106,09 $ | 131,44 $ | 98,53 $ / 148,79 $ | no | n/a | n/a | n/a |
| 98g | 2026-12-04 | 105,39 $ | 130,58 $ | 98,53 $ / 148,79 $ | no | n/a | n/a | n/a |
| 105g | 2026-12-11 | 110,64 $ | 137,08 $ | 98,53 $ / 148,79 $ | no | n/a | n/a | n/a |
| 112g | 2026-12-18 | 106,83 $ | 132,36 $ | 98,53 $ / 148,79 $ | no | n/a | n/a | n/a |
| 119g | 2026-12-25 | 102,18 $ | 126,60 $ | 98,53 $ / 148,79 $ | no | n/a | n/a | n/a |
| 126g | 2027-01-01 | 103,74 $ | 128,54 $ | 98,53 $ / 148,79 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 43 | 37,21% | 11,59% | 13,80% |
| 14g | 36 | 30,56% | 18,13% | 12,38% |
| 21g | 31 | 19,35% | 25,78% | 14,29% |
| 28g | 24 | 45,83% | 24,28% | 14,54% |
| 35g | 17 | 58,82% | 17,93% | 13,74% |
| 42g | 10 | 100,00% | 9,80% | 13,05% |
| 49g | 3 | 100,00% | 7,07% | 23,90% |
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
