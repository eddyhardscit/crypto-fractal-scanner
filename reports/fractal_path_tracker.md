<!-- FRACTAL_PATH_TRACKER_START -->
# Tracking percorso frattale SOL/BTC

Generato: 2026-07-12 07:39 UTC

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-07-12**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2022-12-27**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **76,45 $**
- Verdetto principale: **STRUTTURA ANALOGA, PREZZO NON ADERENTE**
- Somiglianza strutturale: **+65,20%**
- Aderenza live principale: **+59,51%**
- Errore medio live principale: **20,25%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE NON CONFERMATO DAL PREZZO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **36**
- Osservazioni inclusive dal bottom: **37**
- Osservazioni da inizio programma/scanner: **10**
- Errore assoluto medio dal bottom: **9,87%**
- Errore assoluto medio da inizio programma: **20,25%**
- Gap firmato medio ultimi 7 giorni: **+18,50%**
- Errore assoluto medio ultimi 7 giorni: **18,50%**
- Gap ultimo giorno: **+16,09%**
- Stato aderenza: **STACCATO / MOLTO IN ANTICIPO**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **+16,09%**
- Gap firmato medio 7g: **+18,50%**
- Errore assoluto medio 7g: **18,50%**
- Variazione recente gap: **-1,50%**
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
| 27 | 2026-07-03 | 2022-12-18 | 82,28 $ | 66,01 $ | +24,64% | da inizio programma |
| 28 | 2026-07-04 | 2022-12-19 | 81,65 $ | 64,76 $ | +26,08% | da inizio programma |
| 29 | 2026-07-05 | 2022-12-20 | 81,42 $ | 66,60 $ | +22,26% | da inizio programma |
| 30 | 2026-07-06 | 2022-12-21 | 81,92 $ | 66,25 $ | +23,65% | da inizio programma |
| 31 | 2026-07-07 | 2022-12-22 | 80,65 $ | 66,30 $ | +21,64% | da inizio programma |
| 32 | 2026-07-08 | 2022-12-23 | 77,79 $ | 66,17 $ | +17,56% | da inizio programma |
| 33 | 2026-07-09 | 2022-12-24 | 78,05 $ | 66,37 $ | +17,60% | da inizio programma |
| 34 | 2026-07-10 | 2022-12-25 | 78,07 $ | 66,34 $ | +17,67% | da inizio programma |
| 35 | 2026-07-11 | 2022-12-26 | 76,82 $ | 66,65 $ | +15,26% | da inizio programma |
| 36 | 2026-07-12 | 2022-12-27 | 76,45 $ | 65,85 $ | +16,09% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-07-19 | 65,71 $ | 76,28 $ | 75,67 $ / 76,45 $ | no | n/a | n/a | n/a |
| 14g | 2026-07-26 | 68,73 $ | 79,78 $ | 75,67 $ / 79,78 $ | no | n/a | n/a | n/a |
| 21g | 2026-08-02 | 83,36 $ | 96,77 $ | 75,67 $ / 96,81 $ | no | n/a | n/a | n/a |
| 28g | 2026-08-09 | 89,17 $ | 103,52 $ | 75,67 $ / 104,88 $ | no | n/a | n/a | n/a |
| 35g | 2026-08-16 | 91,15 $ | 105,82 $ | 75,67 $ / 108,72 $ | no | n/a | n/a | n/a |
| 42g | 2026-08-23 | 91,64 $ | 106,39 $ | 75,67 $ / 108,72 $ | no | n/a | n/a | n/a |
| 49g | 2026-08-30 | 87,53 $ | 101,62 $ | 75,67 $ / 108,72 $ | no | n/a | n/a | n/a |
| 56g | 2026-09-06 | 96,26 $ | 111,75 $ | 75,67 $ / 113,55 $ | no | n/a | n/a | n/a |
| 63g | 2026-09-13 | 91,18 $ | 105,86 $ | 75,67 $ / 113,55 $ | no | n/a | n/a | n/a |
| 70g | 2026-09-20 | 87,53 $ | 101,61 $ | 75,67 $ / 113,55 $ | no | n/a | n/a | n/a |
| 77g | 2026-09-27 | 97,48 $ | 113,17 $ | 75,67 $ / 113,55 $ | no | n/a | n/a | n/a |
| 84g | 2026-10-04 | 110,99 $ | 128,85 $ | 75,67 $ / 128,85 $ | no | n/a | n/a | n/a |
| 91g | 2026-10-11 | 107,42 $ | 124,70 $ | 75,67 $ / 129,58 $ | no | n/a | n/a | n/a |
| 98g | 2026-10-18 | 110,96 $ | 128,82 $ | 75,67 $ / 130,24 $ | no | n/a | n/a | n/a |
| 105g | 2026-10-25 | 119,10 $ | 138,27 $ | 75,67 $ / 138,27 $ | no | n/a | n/a | n/a |
| 112g | 2026-11-01 | 119,74 $ | 139,01 $ | 75,67 $ / 139,42 $ | no | n/a | n/a | n/a |
| 119g | 2026-11-08 | 111,51 $ | 129,45 $ | 75,67 $ / 139,42 $ | no | n/a | n/a | n/a |
| 126g | 2026-11-15 | 112,98 $ | 131,16 $ | 75,67 $ / 139,42 $ | no | n/a | n/a | n/a |

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
