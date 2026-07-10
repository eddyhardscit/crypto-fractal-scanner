<!-- FRACTAL_PATH_TRACKER_START -->
# Tracking percorso frattale SOL/BTC

Generato: 2026-07-10 23:41 UTC

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-07-10**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2022-12-25**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **78,01 $**
- Verdetto principale: **STRUTTURA ANALOGA, PREZZO NON ADERENTE**
- Somiglianza strutturale: **+65,14%**
- Aderenza live principale: **+57,25%**
- Errore medio live principale: **21,38%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE NON CONFERMATO DAL PREZZO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorni controllati dal bottom: **35**
- Giorni controllati da inizio programma/scanner: **8**
- Errore assoluto medio dal bottom: **9,53%**
- Errore assoluto medio da inizio programma: **21,38%**
- Gap firmato medio ultimi 7 giorni: **+20,91%**
- Errore assoluto medio ultimi 7 giorni: **20,91%**
- Gap ultimo giorno: **+17,58%**
- Stato aderenza: **STACCATO / MOLTO IN ANTICIPO**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **+17,58%**
- Gap firmato medio 7g: **+20,91%**
- Errore assoluto medio 7g: **20,91%**
- Variazione recente gap: **-4,06%**
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
| 25 | 2026-07-01 | 2022-12-16 | 77,38 $ | 65,58 $ | +18,00% | prima programma |
| 26 | 2026-07-02 | 2022-12-17 | 80,64 $ | 66,16 $ | +21,89% | prima programma |
| 27 | 2026-07-03 | 2022-12-18 | 82,28 $ | 66,01 $ | +24,64% | da inizio programma |
| 28 | 2026-07-04 | 2022-12-19 | 81,65 $ | 64,76 $ | +26,08% | da inizio programma |
| 29 | 2026-07-05 | 2022-12-20 | 81,42 $ | 66,60 $ | +22,26% | da inizio programma |
| 30 | 2026-07-06 | 2022-12-21 | 81,92 $ | 66,25 $ | +23,65% | da inizio programma |
| 31 | 2026-07-07 | 2022-12-22 | 80,65 $ | 66,30 $ | +21,64% | da inizio programma |
| 32 | 2026-07-08 | 2022-12-23 | 77,79 $ | 66,17 $ | +17,56% | da inizio programma |
| 33 | 2026-07-09 | 2022-12-24 | 78,05 $ | 66,37 $ | +17,60% | da inizio programma |
| 34 | 2026-07-10 | 2022-12-25 | 78,01 $ | 66,34 $ | +17,58% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-07-17 | 65,49 $ | 77,01 $ | 76,65 $ / 78,37 $ | no | n/a | n/a | n/a |
| 14g | 2026-07-24 | 67,33 $ | 79,16 $ | 76,65 $ / 79,16 $ | no | n/a | n/a | n/a |
| 21g | 2026-07-31 | 82,25 $ | 96,72 $ | 76,65 $ / 97,16 $ | no | n/a | n/a | n/a |
| 28g | 2026-08-07 | 89,50 $ | 105,24 $ | 76,65 $ / 105,50 $ | no | n/a | n/a | n/a |
| 35g | 2026-08-14 | 93,65 $ | 110,12 $ | 76,65 $ / 110,12 $ | no | n/a | n/a | n/a |
| 42g | 2026-08-21 | 90,43 $ | 106,33 $ | 76,65 $ / 110,12 $ | no | n/a | n/a | n/a |
| 49g | 2026-08-28 | 85,83 $ | 100,92 $ | 76,65 $ / 110,12 $ | no | n/a | n/a | n/a |
| 56g | 2026-09-04 | 95,83 $ | 112,68 $ | 76,65 $ / 114,14 $ | no | n/a | n/a | n/a |
| 63g | 2026-09-11 | 92,81 $ | 109,13 $ | 76,65 $ / 115,01 $ | no | n/a | n/a | n/a |
| 70g | 2026-09-18 | 88,38 $ | 103,92 $ | 76,65 $ / 115,01 $ | no | n/a | n/a | n/a |
| 77g | 2026-09-25 | 87,31 $ | 102,66 $ | 76,65 $ / 115,01 $ | no | n/a | n/a | n/a |
| 84g | 2026-10-02 | 110,45 $ | 129,87 $ | 76,65 $ / 129,87 $ | no | n/a | n/a | n/a |
| 91g | 2026-10-09 | 110,28 $ | 129,67 $ | 76,65 $ / 131,24 $ | no | n/a | n/a | n/a |
| 98g | 2026-10-16 | 111,08 $ | 130,62 $ | 76,65 $ / 131,91 $ | no | n/a | n/a | n/a |
| 105g | 2026-10-23 | 111,61 $ | 131,24 $ | 76,65 $ / 131,91 $ | no | n/a | n/a | n/a |
| 112g | 2026-10-30 | 119,42 $ | 140,42 $ | 76,65 $ / 141,21 $ | no | n/a | n/a | n/a |
| 119g | 2026-11-06 | 108,69 $ | 127,80 $ | 76,65 $ / 141,21 $ | no | n/a | n/a | n/a |
| 126g | 2026-11-13 | 115,30 $ | 135,57 $ | 76,65 $ / 141,21 $ | no | n/a | n/a | n/a |

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
