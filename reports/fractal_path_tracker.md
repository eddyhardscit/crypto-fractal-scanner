<!-- FRACTAL_PATH_TRACKER_START -->
# Tracking percorso frattale SOL/BTC

Generato: 2026-07-14 11:44 UTC

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-07-14**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2022-12-29**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **75,34 $**
- Verdetto principale: **STRUTTURA ANALOGA, PREZZO NON ADERENTE**
- Somiglianza strutturale: **+65,29%**
- Aderenza live principale: **+61,19%**
- Errore medio live principale: **19,40%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE NON CONFERMATO DAL PREZZO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **38**
- Osservazioni inclusive dal bottom: **39**
- Osservazioni da inizio programma/scanner: **12**
- Errore assoluto medio dal bottom: **10,14%**
- Errore assoluto medio da inizio programma: **19,40%**
- Gap firmato medio ultimi 7 giorni: **+16,37%**
- Errore assoluto medio ultimi 7 giorni: **16,37%**
- Gap ultimo giorno: **+14,92%**
- Stato aderenza: **STACCATO / MOLTO IN ANTICIPO**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **+14,92%**
- Gap firmato medio 7g: **+16,37%**
- Errore assoluto medio 7g: **16,37%**
- Variazione recente gap: **-0,34%**
- Stato gap: **IN DEVIAZIONE SOPRA IL FRATTALE**
- Trend gap: **SOL resta sopra il percorso ancorato con distacco quasi stabile**

Soglie operative del grafico:

- entro **±5%**: percorso vicino;
- tra **±5% e ±12%**: deviazione gestibile;
- oltre **±12%**: frattale non abbastanza aderente per conferma operativa;
- oltre **±18%**: disallineamento marcato.

## Ultimi giorni del confronto ancorato

|   Giorno | Data SOL   | Data BTC eq.   | SOL reale   | Percorso ancorato   | Gap firmato   | Fase                |
|---------:|:-----------|:---------------|:------------|:--------------------|:--------------|:--------------------|
| 29 | 2026-07-05 | 2022-12-20 | 81,42 $ | 66,60 $ | +22,26% | da inizio programma |
| 30 | 2026-07-06 | 2022-12-21 | 81,92 $ | 66,25 $ | +23,65% | da inizio programma |
| 31 | 2026-07-07 | 2022-12-22 | 80,65 $ | 66,30 $ | +21,64% | da inizio programma |
| 32 | 2026-07-08 | 2022-12-23 | 77,79 $ | 66,17 $ | +17,56% | da inizio programma |
| 33 | 2026-07-09 | 2022-12-24 | 78,05 $ | 66,37 $ | +17,60% | da inizio programma |
| 34 | 2026-07-10 | 2022-12-25 | 78,07 $ | 66,34 $ | +17,67% | da inizio programma |
| 35 | 2026-07-11 | 2022-12-26 | 76,82 $ | 66,65 $ | +15,26% | da inizio programma |
| 36 | 2026-07-12 | 2022-12-27 | 76,87 $ | 65,85 $ | +16,74% | da inizio programma |
| 37 | 2026-07-13 | 2022-12-28 | 74,86 $ | 65,20 $ | +14,81% | da inizio programma |
| 38 | 2026-07-14 | 2022-12-29 | 75,34 $ | 65,56 $ | +14,92% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-07-21 | 66,32 $ | 76,22 $ | 74,91 $ / 76,34 $ | no | n/a | n/a | n/a |
| 14g | 2026-07-28 | 74,33 $ | 85,42 $ | 74,91 $ / 85,42 $ | no | n/a | n/a | n/a |
| 21g | 2026-08-04 | 83,07 $ | 95,46 $ | 74,91 $ / 95,84 $ | no | n/a | n/a | n/a |
| 28g | 2026-08-11 | 90,73 $ | 104,27 $ | 74,91 $ / 104,65 $ | no | n/a | n/a | n/a |
| 35g | 2026-08-18 | 92,46 $ | 106,26 $ | 74,91 $ / 107,63 $ | no | n/a | n/a | n/a |
| 42g | 2026-08-25 | 85,95 $ | 98,77 $ | 74,91 $ / 107,63 $ | no | n/a | n/a | n/a |
| 49g | 2026-09-01 | 93,06 $ | 106,94 $ | 74,91 $ / 110,04 $ | no | n/a | n/a | n/a |
| 56g | 2026-09-08 | 94,33 $ | 108,41 $ | 74,91 $ / 112,40 $ | no | n/a | n/a | n/a |
| 63g | 2026-09-15 | 92,48 $ | 106,27 $ | 74,91 $ / 112,40 $ | no | n/a | n/a | n/a |
| 70g | 2026-09-22 | 80,21 $ | 92,18 $ | 74,91 $ / 112,40 $ | no | n/a | n/a | n/a |
| 77g | 2026-09-29 | 98,69 $ | 113,41 $ | 74,91 $ / 113,41 $ | no | n/a | n/a | n/a |
| 84g | 2026-10-06 | 111,61 $ | 128,27 $ | 74,91 $ / 128,27 $ | no | n/a | n/a | n/a |
| 91g | 2026-10-13 | 110,43 $ | 126,91 $ | 74,91 $ / 128,33 $ | no | n/a | n/a | n/a |
| 98g | 2026-10-20 | 110,47 $ | 126,96 $ | 74,91 $ / 128,92 $ | no | n/a | n/a | n/a |
| 105g | 2026-10-27 | 119,75 $ | 137,62 $ | 74,91 $ / 137,62 $ | no | n/a | n/a | n/a |
| 112g | 2026-11-03 | 111,27 $ | 127,87 $ | 74,91 $ / 138,01 $ | no | n/a | n/a | n/a |
| 119g | 2026-11-10 | 116,10 $ | 133,43 $ | 74,91 $ / 138,01 $ | no | n/a | n/a | n/a |
| 126g | 2026-11-17 | 113,64 $ | 130,59 $ | 74,91 $ / 138,01 $ | no | n/a | n/a | n/a |

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
