<!-- FRACTAL_PATH_TRACKER_START -->
# Tracking percorso frattale SOL/BTC

Generato: 2026-09-23 10:18 UTC

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-09-23**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-03-10**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **117,38 $**
- Verdetto principale: **STRUTTURA ANALOGA, PREZZO NON ADERENTE**
- Somiglianza strutturale: **+69,22%**
- Aderenza live principale: **+69,72%**
- Errore medio live principale: **15,14%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE NON CONFERMATO DAL PREZZO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **109**
- Osservazioni inclusive dal bottom: **110**
- Osservazioni da inizio programma/scanner: **83**
- Errore assoluto medio dal bottom: **12,90%**
- Errore assoluto medio da inizio programma: **15,14%**
- Gap firmato medio ultimi 7 giorni: **+32,79%**
- Errore assoluto medio ultimi 7 giorni: **32,79%**
- Gap ultimo giorno: **+47,61%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **+47,61%**
- Gap firmato medio 7g: **+32,79%**
- Errore assoluto medio 7g: **32,79%**
- Variazione recente gap: **+20,64%**
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
| 100 | 2026-09-14 | 2023-03-01 | 102,50 $ | 93,15 $ | +10,03% | da inizio programma |
| 101 | 2026-09-15 | 2023-03-02 | 96,89 $ | 92,48 $ | +4,77% | da inizio programma |
| 102 | 2026-09-16 | 2023-03-03 | 98,64 $ | 88,09 $ | +11,98% | da inizio programma |
| 103 | 2026-09-17 | 2023-03-04 | 101,60 $ | 88,06 $ | +15,39% | da inizio programma |
| 104 | 2026-09-18 | 2023-03-05 | 112,60 $ | 88,38 $ | +27,41% | da inizio programma |
| 105 | 2026-09-19 | 2023-03-06 | 111,01 $ | 88,36 $ | +25,64% | da inizio programma |
| 106 | 2026-09-20 | 2023-03-07 | 111,13 $ | 87,53 $ | +26,97% | da inizio programma |
| 107 | 2026-09-21 | 2023-03-08 | 118,75 $ | 85,55 $ | +38,80% | da inizio programma |
| 108 | 2026-09-22 | 2023-03-09 | 118,51 $ | 80,21 $ | +47,74% | da inizio programma |
| 109 | 2026-09-23 | 2023-03-10 | 117,38 $ | 79,52 $ | +47,61% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-09-30 | 108,03 $ | 159,46 $ | 117,38 $ / 159,46 $ | no | n/a | n/a | n/a |
| 14g | 2026-10-07 | 108,30 $ | 159,86 $ | 117,38 $ / 164,75 $ | no | n/a | n/a | n/a |
| 21g | 2026-10-14 | 112,18 $ | 165,59 $ | 117,38 $ / 165,59 $ | no | n/a | n/a | n/a |
| 28g | 2026-10-21 | 110,01 $ | 162,38 $ | 117,38 $ / 165,59 $ | no | n/a | n/a | n/a |
| 35g | 2026-10-28 | 120,09 $ | 177,26 $ | 117,38 $ / 177,26 $ | no | n/a | n/a | n/a |
| 42g | 2026-11-04 | 107,45 $ | 158,60 $ | 117,38 $ / 177,26 $ | no | n/a | n/a | n/a |
| 49g | 2026-11-11 | 115,58 $ | 170,60 $ | 117,38 $ / 177,26 $ | no | n/a | n/a | n/a |
| 56g | 2026-11-18 | 116,34 $ | 171,73 $ | 117,38 $ / 177,26 $ | no | n/a | n/a | n/a |
| 63g | 2026-11-25 | 105,59 $ | 155,86 $ | 117,38 $ / 177,26 $ | no | n/a | n/a | n/a |
| 70g | 2026-12-02 | 105,93 $ | 156,35 $ | 117,38 $ / 177,26 $ | no | n/a | n/a | n/a |
| 77g | 2026-12-09 | 105,25 $ | 155,36 $ | 117,38 $ / 177,26 $ | no | n/a | n/a | n/a |
| 84g | 2026-12-16 | 107,34 $ | 158,44 $ | 117,38 $ / 177,26 $ | no | n/a | n/a | n/a |
| 91g | 2026-12-23 | 104,31 $ | 153,97 $ | 117,38 $ / 177,26 $ | no | n/a | n/a | n/a |
| 98g | 2026-12-30 | 103,71 $ | 153,08 $ | 117,38 $ / 177,26 $ | no | n/a | n/a | n/a |
| 105g | 2027-01-06 | 120,92 $ | 178,48 $ | 117,38 $ / 178,48 $ | no | n/a | n/a | n/a |
| 112g | 2027-01-13 | 120,06 $ | 177,21 $ | 117,38 $ / 178,48 $ | no | n/a | n/a | n/a |
| 119g | 2027-01-20 | 119,53 $ | 176,43 $ | 117,38 $ / 181,16 $ | no | n/a | n/a | n/a |
| 126g | 2027-01-27 | 119,49 $ | 176,38 $ | 117,38 $ / 183,02 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 69 | 36,23% | 11,19% | 14,54% |
| 14g | 62 | 24,19% | 17,47% | 13,82% |
| 21g | 55 | 23,64% | 23,82% | 15,32% |
| 28g | 48 | 22,92% | 26,72% | 15,41% |
| 35g | 41 | 31,71% | 26,36% | 15,05% |
| 42g | 35 | 57,14% | 19,63% | 14,09% |
| 49g | 29 | 68,97% | 16,92% | 16,01% |
| 56g | 22 | 72,73% | 12,69% | 17,28% |
| 63g | 15 | 73,33% | 10,82% | 21,95% |
| 70g | 8 | 62,50% | 12,41% | 35,69% |
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
