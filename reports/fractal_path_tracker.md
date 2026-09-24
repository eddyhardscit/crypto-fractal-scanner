<!-- FRACTAL_PATH_TRACKER_START -->
# Tracking percorso frattale SOL/BTC

Generato: 2026-09-24 05:32 UTC

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-09-24**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-03-11**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **115,45 $**
- Verdetto principale: **STRUTTURA ANALOGA, PREZZO NON ADERENTE**
- Somiglianza strutturale: **+69,04%**
- Aderenza live principale: **+69,05%**
- Errore medio live principale: **15,48%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE NON CONFERMATO DAL PREZZO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **110**
- Osservazioni inclusive dal bottom: **111**
- Osservazioni da inizio programma/scanner: **84**
- Errore assoluto medio dal bottom: **13,18%**
- Errore assoluto medio da inizio programma: **15,48%**
- Gap firmato medio ultimi 7 giorni: **+36,80%**
- Errore assoluto medio ultimi 7 giorni: **36,80%**
- Gap ultimo giorno: **+42,05%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **+42,05%**
- Gap firmato medio 7g: **+36,80%**
- Errore assoluto medio 7g: **36,80%**
- Variazione recente gap: **+3,24%**
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
| 101 | 2026-09-15 | 2023-03-02 | 96,89 $ | 92,48 $ | +4,77% | da inizio programma |
| 102 | 2026-09-16 | 2023-03-03 | 98,64 $ | 88,09 $ | +11,98% | da inizio programma |
| 103 | 2026-09-17 | 2023-03-04 | 101,60 $ | 88,06 $ | +15,39% | da inizio programma |
| 104 | 2026-09-18 | 2023-03-05 | 112,60 $ | 88,38 $ | +27,41% | da inizio programma |
| 105 | 2026-09-19 | 2023-03-06 | 111,01 $ | 88,36 $ | +25,64% | da inizio programma |
| 106 | 2026-09-20 | 2023-03-07 | 111,13 $ | 87,53 $ | +26,97% | da inizio programma |
| 107 | 2026-09-21 | 2023-03-08 | 118,75 $ | 85,55 $ | +38,80% | da inizio programma |
| 108 | 2026-09-22 | 2023-03-09 | 118,51 $ | 80,21 $ | +47,74% | da inizio programma |
| 109 | 2026-09-23 | 2023-03-10 | 118,51 $ | 79,52 $ | +49,02% | da inizio programma |
| 110 | 2026-09-24 | 2023-03-11 | 115,45 $ | 81,28 $ | +42,05% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-10-01 | 106,22 $ | 150,89 $ | 115,45 $ / 153,45 $ | no | n/a | n/a | n/a |
| 14g | 2026-10-08 | 108,31 $ | 153,85 $ | 115,45 $ / 158,54 $ | no | n/a | n/a | n/a |
| 21g | 2026-10-15 | 111,92 $ | 158,98 $ | 115,45 $ / 159,35 $ | no | n/a | n/a | n/a |
| 28g | 2026-10-22 | 110,09 $ | 156,38 $ | 115,45 $ / 159,35 $ | no | n/a | n/a | n/a |
| 35g | 2026-10-29 | 119,43 $ | 169,65 $ | 115,45 $ / 170,58 $ | no | n/a | n/a | n/a |
| 42g | 2026-11-05 | 109,58 $ | 155,65 $ | 115,45 $ / 170,58 $ | no | n/a | n/a | n/a |
| 49g | 2026-11-12 | 115,22 $ | 163,66 $ | 115,45 $ / 170,58 $ | no | n/a | n/a | n/a |
| 56g | 2026-11-19 | 113,86 $ | 161,74 $ | 115,45 $ / 170,58 $ | no | n/a | n/a | n/a |
| 63g | 2026-11-26 | 105,51 $ | 149,87 $ | 115,45 $ / 170,58 $ | no | n/a | n/a | n/a |
| 70g | 2026-12-03 | 106,87 $ | 151,81 $ | 115,45 $ / 170,58 $ | no | n/a | n/a | n/a |
| 77g | 2026-12-10 | 105,84 $ | 150,34 $ | 115,45 $ / 170,58 $ | no | n/a | n/a | n/a |
| 84g | 2026-12-17 | 106,66 $ | 151,50 $ | 115,45 $ / 170,58 $ | no | n/a | n/a | n/a |
| 91g | 2026-12-24 | 101,83 $ | 144,65 $ | 115,45 $ / 170,58 $ | no | n/a | n/a | n/a |
| 98g | 2026-12-31 | 104,43 $ | 148,34 $ | 115,45 $ / 170,58 $ | no | n/a | n/a | n/a |
| 105g | 2027-01-07 | 120,34 $ | 170,94 $ | 115,45 $ / 171,76 $ | no | n/a | n/a | n/a |
| 112g | 2027-01-14 | 120,50 $ | 171,17 $ | 115,45 $ / 171,76 $ | no | n/a | n/a | n/a |
| 119g | 2027-01-21 | 119,33 $ | 169,50 $ | 115,45 $ / 174,34 $ | no | n/a | n/a | n/a |
| 126g | 2027-01-28 | 119,34 $ | 169,52 $ | 115,45 $ / 176,13 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 70 | 35,71% | 11,41% | 14,97% |
| 14g | 63 | 23,81% | 17,64% | 14,31% |
| 21g | 56 | 23,21% | 24,10% | 15,84% |
| 28g | 49 | 22,45% | 26,63% | 16,01% |
| 35g | 42 | 30,95% | 27,06% | 15,76% |
| 42g | 35 | 57,14% | 19,63% | 14,09% |
| 49g | 30 | 66,67% | 18,81% | 16,99% |
| 56g | 23 | 69,57% | 14,81% | 18,53% |
| 63g | 16 | 68,75% | 11,66% | 23,49% |
| 70g | 9 | 55,56% | 13,54% | 36,80% |
| 77g | 2 | 0,00% | 20,93% | n/a |
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
