<!-- FRACTAL_PATH_TRACKER_START -->
# Tracking percorso frattale SOL/BTC

Generato: 2026-07-14 07:22 UTC

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-07-13**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2022-12-28**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **74,86 $**
- Verdetto principale: **STRUTTURA ANALOGA, PREZZO NON ADERENTE**
- Somiglianza strutturale: **+65,25%**
- Aderenza live principale: **+60,38%**
- Errore medio live principale: **19,81%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE NON CONFERMATO DAL PREZZO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **37**
- Osservazioni inclusive dal bottom: **38**
- Osservazioni da inizio programma/scanner: **11**
- Errore assoluto medio dal bottom: **10,01%**
- Errore assoluto medio da inizio programma: **19,81%**
- Gap firmato medio ultimi 7 giorni: **+17,33%**
- Errore assoluto medio ultimi 7 giorni: **17,33%**
- Gap ultimo giorno: **+14,81%**
- Stato aderenza: **STACCATO / MOLTO IN ANTICIPO**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **+14,81%**
- Gap firmato medio 7g: **+17,33%**
- Errore assoluto medio 7g: **17,33%**
- Variazione recente gap: **-2,86%**
- Stato gap: **IN DEVIAZIONE SOPRA IL FRATTALE**
- Trend gap: **SOL resta sopra il percorso ancorato, ma sta riducendo il distacco**

Soglie operative del grafico:

- entro **±5%**: percorso vicino;
- tra **±5% e ±12%**: deviazione gestibile;
- oltre **±12%**: frattale non abbastanza aderente per conferma operativa;
- oltre **±18%**: disallineamento marcato.

## Ultimi giorni del confronto ancorato

|   Giorno | Data SOL   | Data BTC eq.   | SOL reale   | Percorso ancorato   | Gap firmato   | Fase                |
|---------:|:-----------|:---------------|:------------|:--------------------|:--------------|:--------------------|
| 28 | 2026-07-04 | 2022-12-19 | 81,65 $ | 64,76 $ | +26,08% | da inizio programma |
| 29 | 2026-07-05 | 2022-12-20 | 81,42 $ | 66,60 $ | +22,26% | da inizio programma |
| 30 | 2026-07-06 | 2022-12-21 | 81,92 $ | 66,25 $ | +23,65% | da inizio programma |
| 31 | 2026-07-07 | 2022-12-22 | 80,65 $ | 66,30 $ | +21,64% | da inizio programma |
| 32 | 2026-07-08 | 2022-12-23 | 77,79 $ | 66,17 $ | +17,56% | da inizio programma |
| 33 | 2026-07-09 | 2022-12-24 | 78,05 $ | 66,37 $ | +17,60% | da inizio programma |
| 34 | 2026-07-10 | 2022-12-25 | 78,07 $ | 66,34 $ | +17,67% | da inizio programma |
| 35 | 2026-07-11 | 2022-12-26 | 76,82 $ | 66,65 $ | +15,26% | da inizio programma |
| 36 | 2026-07-12 | 2022-12-27 | 76,87 $ | 65,85 $ | +16,74% | da inizio programma |
| 37 | 2026-07-13 | 2022-12-28 | 74,86 $ | 65,20 $ | +14,81% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-07-20 | 66,43 $ | 76,27 $ | 74,84 $ / 76,27 $ | no | n/a | n/a | n/a |
| 14g | 2026-07-27 | 70,65 $ | 81,11 $ | 74,84 $ / 81,11 $ | no | n/a | n/a | n/a |
| 21g | 2026-08-03 | 81,50 $ | 93,57 $ | 74,84 $ / 95,74 $ | no | n/a | n/a | n/a |
| 28g | 2026-08-10 | 91,07 $ | 104,55 $ | 74,84 $ / 104,55 $ | no | n/a | n/a | n/a |
| 35g | 2026-08-17 | 93,45 $ | 107,29 $ | 74,84 $ / 107,52 $ | no | n/a | n/a | n/a |
| 42g | 2026-08-24 | 90,36 $ | 103,75 $ | 74,84 $ / 107,52 $ | no | n/a | n/a | n/a |
| 49g | 2026-08-31 | 95,75 $ | 109,94 $ | 74,84 $ / 109,94 $ | no | n/a | n/a | n/a |
| 56g | 2026-09-07 | 95,29 $ | 109,40 $ | 74,84 $ / 112,29 $ | no | n/a | n/a | n/a |
| 63g | 2026-09-14 | 93,15 $ | 106,94 $ | 74,84 $ / 112,29 $ | no | n/a | n/a | n/a |
| 70g | 2026-09-21 | 85,55 $ | 98,22 $ | 74,84 $ / 112,29 $ | no | n/a | n/a | n/a |
| 77g | 2026-09-28 | 96,02 $ | 110,24 $ | 74,84 $ / 112,29 $ | no | n/a | n/a | n/a |
| 84g | 2026-10-05 | 107,57 $ | 123,50 $ | 74,84 $ / 127,43 $ | no | n/a | n/a | n/a |
| 91g | 2026-10-12 | 111,67 $ | 128,21 $ | 74,84 $ / 128,21 $ | no | n/a | n/a | n/a |
| 98g | 2026-10-19 | 111,00 $ | 127,44 $ | 74,84 $ / 128,80 $ | no | n/a | n/a | n/a |
| 105g | 2026-10-26 | 118,72 $ | 136,31 $ | 74,84 $ / 136,74 $ | no | n/a | n/a | n/a |
| 112g | 2026-11-02 | 113,54 $ | 130,35 $ | 74,84 $ / 137,88 $ | no | n/a | n/a | n/a |
| 119g | 2026-11-09 | 111,96 $ | 128,55 $ | 74,84 $ / 137,88 $ | no | n/a | n/a | n/a |
| 126g | 2026-11-16 | 114,26 $ | 131,19 $ | 74,84 $ / 137,88 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 0 | n/a | n/a | n/a |
| 14g | 0 | n/a | n/a | n/a |
| 21g | 0 | n/a | n/a | n/a |
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
