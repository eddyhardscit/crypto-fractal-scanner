<!-- FRACTAL_PATH_TRACKER_START -->
# Tracking percorso frattale SOL/BTC

Generato: 2026-10-05 05:32 UTC

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-10-05**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-03-22**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **120,09 $**
- Verdetto principale: **STRUTTURA ANALOGA, PREZZO NON ADERENTE**
- Somiglianza strutturale: **+72,09%**
- Aderenza live principale: **+68,61%**
- Errore medio live principale: **15,70%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE NON CONFERMATO DAL PREZZO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **121**
- Osservazioni inclusive dal bottom: **122**
- Osservazioni da inizio programma/scanner: **95**
- Errore assoluto medio dal bottom: **13,56%**
- Errore assoluto medio da inizio programma: **15,70%**
- Gap firmato medio ultimi 7 giorni: **+11,08%**
- Errore assoluto medio ultimi 7 giorni: **11,08%**
- Gap ultimo giorno: **+11,64%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **+11,64%**
- Gap firmato medio 7g: **+11,08%**
- Errore assoluto medio 7g: **11,08%**
- Variazione recente gap: **+4,25%**
- Stato gap: **SOPRA IL FRATTALE**
- Trend gap: **SOL sta aumentando il distacco sopra il percorso ancorato**

Soglie operative del grafico:

- entro **±5%**: percorso vicino;
- tra **±5% e ±12%**: deviazione gestibile;
- oltre **±12%**: frattale non abbastanza aderente per conferma operativa;
- oltre **±18%**: disallineamento marcato.

## Ultimi giorni del confronto ancorato

|   Giorno | Data SOL   | Data BTC eq.   | SOL reale   | Percorso ancorato   | Gap firmato   | Fase                |
|---------:|:-----------|:---------------|:------------|:--------------------|:--------------|:--------------------|
| 112 | 2026-09-26 | 2023-03-13 | 121,43 $ | 95,32 $ | +27,39% | da inizio programma |
| 113 | 2026-09-27 | 2023-03-14 | 122,06 $ | 97,48 $ | +25,21% | da inizio programma |
| 114 | 2026-09-28 | 2023-03-15 | 118,84 $ | 96,02 $ | +23,76% | da inizio programma |
| 115 | 2026-09-29 | 2023-03-16 | 119,06 $ | 98,69 $ | +20,64% | da inizio programma |
| 116 | 2026-09-30 | 2023-03-17 | 117,99 $ | 108,03 $ | +9,22% | da inizio programma |
| 117 | 2026-10-01 | 2023-03-18 | 118,40 $ | 106,22 $ | +11,46% | da inizio programma |
| 118 | 2026-10-02 | 2023-03-19 | 118,62 $ | 110,45 $ | +7,39% | da inizio programma |
| 119 | 2026-10-03 | 2023-03-20 | 119,65 $ | 109,38 $ | +9,38% | da inizio programma |
| 120 | 2026-10-04 | 2023-03-21 | 119,65 $ | 110,99 $ | +7,80% | da inizio programma |
| 121 | 2026-10-05 | 2023-03-22 | 120,09 $ | 107,57 $ | +11,64% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-10-12 | 111,67 $ | 124,67 $ | 119,35 $ / 124,67 $ | no | n/a | n/a | n/a |
| 14g | 2026-10-19 | 111,00 $ | 123,92 $ | 119,35 $ / 125,24 $ | no | n/a | n/a | n/a |
| 21g | 2026-10-26 | 118,72 $ | 132,54 $ | 119,35 $ / 132,96 $ | no | n/a | n/a | n/a |
| 28g | 2026-11-02 | 113,54 $ | 126,75 $ | 119,35 $ / 134,07 $ | no | n/a | n/a | n/a |
| 35g | 2026-11-09 | 111,96 $ | 124,99 $ | 119,35 $ / 134,07 $ | no | n/a | n/a | n/a |
| 42g | 2026-11-16 | 114,26 $ | 127,56 $ | 119,35 $ / 134,07 $ | no | n/a | n/a | n/a |
| 49g | 2026-11-23 | 108,81 $ | 121,47 $ | 119,35 $ / 134,07 $ | no | n/a | n/a | n/a |
| 56g | 2026-11-30 | 107,93 $ | 120,49 $ | 117,79 $ / 134,07 $ | no | n/a | n/a | n/a |
| 63g | 2026-12-07 | 103,74 $ | 115,81 $ | 115,81 $ / 134,07 $ | no | n/a | n/a | n/a |
| 70g | 2026-12-14 | 107,22 $ | 119,70 $ | 115,81 $ / 134,07 $ | no | n/a | n/a | n/a |
| 77g | 2026-12-21 | 103,78 $ | 115,86 $ | 113,29 $ / 134,07 $ | no | n/a | n/a | n/a |
| 84g | 2026-12-28 | 98,97 $ | 110,49 $ | 110,49 $ / 134,07 $ | no | n/a | n/a | n/a |
| 91g | 2027-01-04 | 118,28 $ | 132,05 $ | 110,49 $ / 134,07 $ | no | n/a | n/a | n/a |
| 98g | 2027-01-11 | 118,52 $ | 132,31 $ | 110,49 $ / 134,99 $ | no | n/a | n/a | n/a |
| 105g | 2027-01-18 | 120,20 $ | 134,19 $ | 110,49 $ / 137,02 $ | no | n/a | n/a | n/a |
| 112g | 2027-01-25 | 119,72 $ | 133,65 $ | 110,49 $ / 137,02 $ | no | n/a | n/a | n/a |
| 119g | 2027-02-01 | 117,84 $ | 131,55 $ | 110,49 $ / 138,42 $ | no | n/a | n/a | n/a |
| 126g | 2027-02-08 | 115,64 $ | 129,09 $ | 110,49 $ / 138,42 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 77 | 38,96% | 11,95% | 14,57% |
| 14g | 70 | 24,29% | 17,07% | 15,11% |
| 21g | 67 | 26,87% | 21,57% | 16,10% |
| 28g | 60 | 23,33% | 22,84% | 16,27% |
| 35g | 53 | 33,96% | 24,25% | 16,11% |
| 42g | 46 | 43,48% | 22,68% | 14,97% |
| 49g | 39 | 51,28% | 24,58% | 17,46% |
| 56g | 34 | 47,06% | 21,94% | 18,13% |
| 63g | 27 | 40,74% | 15,18% | 20,80% |
| 70g | 20 | 55,00% | 9,62% | 24,93% |
| 77g | 13 | 46,15% | 9,42% | 17,60% |
| 84g | 6 | 100,00% | 5,89% | 9,05% |
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
