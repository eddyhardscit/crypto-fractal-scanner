<!-- FRACTAL_PATH_TRACKER_START -->
# Tracking percorso frattale SOL/BTC

Generato: 2026-07-11 00:41 UTC

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-07-11**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2022-12-26**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **77,78 $**
- Verdetto principale: **STRUTTURA ANALOGA, PREZZO NON ADERENTE**
- Somiglianza strutturale: **+65,17%**
- Aderenza live principale: **+57,33%**
- Errore medio live principale: **21,33%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE NON CONFERMATO DAL PREZZO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorni controllati dal bottom: **36**
- Giorni controllati da inizio programma/scanner: **9**
- Errore assoluto medio dal bottom: **9,73%**
- Errore assoluto medio da inizio programma: **20,86%**
- Gap firmato medio ultimi 7 giorni: **+19,58%**
- Errore assoluto medio ultimi 7 giorni: **19,58%**
- Gap ultimo giorno: **+16,70%**
- Stato aderenza: **STACCATO / MOLTO IN ANTICIPO**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **+16,70%**
- Gap firmato medio 7g: **+19,58%**
- Errore assoluto medio 7g: **19,58%**
- Variazione recente gap: **-0,86%**
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
| 26 | 2026-07-02 | 2022-12-17 | 80,64 $ | 66,16 $ | +21,89% | prima programma |
| 27 | 2026-07-03 | 2022-12-18 | 82,28 $ | 66,01 $ | +24,64% | da inizio programma |
| 28 | 2026-07-04 | 2022-12-19 | 81,65 $ | 64,76 $ | +26,08% | da inizio programma |
| 29 | 2026-07-05 | 2022-12-20 | 81,42 $ | 66,60 $ | +22,26% | da inizio programma |
| 30 | 2026-07-06 | 2022-12-21 | 81,92 $ | 66,25 $ | +23,65% | da inizio programma |
| 31 | 2026-07-07 | 2022-12-22 | 80,65 $ | 66,30 $ | +21,64% | da inizio programma |
| 32 | 2026-07-08 | 2022-12-23 | 77,79 $ | 66,17 $ | +17,56% | da inizio programma |
| 33 | 2026-07-09 | 2022-12-24 | 78,05 $ | 66,37 $ | +17,60% | da inizio programma |
| 34 | 2026-07-10 | 2022-12-25 | 78,05 $ | 66,34 $ | +17,64% | da inizio programma |
| 35 | 2026-07-11 | 2022-12-26 | 77,78 $ | 66,65 $ | +16,70% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-07-18 | 65,74 $ | 76,72 $ | 76,07 $ / 77,78 $ | no | n/a | n/a | n/a |
| 14g | 2026-07-25 | 67,74 $ | 79,05 $ | 76,07 $ / 79,05 $ | no | n/a | n/a | n/a |
| 21g | 2026-08-01 | 83,39 $ | 97,32 $ | 76,07 $ / 97,32 $ | no | n/a | n/a | n/a |
| 28g | 2026-08-08 | 90,34 $ | 105,43 $ | 76,07 $ / 105,43 $ | no | n/a | n/a | n/a |
| 35g | 2026-08-15 | 89,97 $ | 105,00 $ | 76,07 $ / 109,29 $ | no | n/a | n/a | n/a |
| 42g | 2026-08-22 | 89,66 $ | 104,63 $ | 76,07 $ / 109,29 $ | no | n/a | n/a | n/a |
| 49g | 2026-08-29 | 85,91 $ | 100,25 $ | 76,07 $ / 109,29 $ | no | n/a | n/a | n/a |
| 56g | 2026-09-05 | 97,81 $ | 114,14 $ | 76,07 $ / 114,14 $ | no | n/a | n/a | n/a |
| 63g | 2026-09-12 | 92,66 $ | 108,13 $ | 76,07 $ / 114,14 $ | no | n/a | n/a | n/a |
| 70g | 2026-09-19 | 88,36 $ | 103,11 $ | 76,07 $ / 114,14 $ | no | n/a | n/a | n/a |
| 77g | 2026-09-26 | 95,32 $ | 111,24 $ | 76,07 $ / 114,14 $ | no | n/a | n/a | n/a |
| 84g | 2026-10-03 | 109,38 $ | 127,65 $ | 76,07 $ / 128,89 $ | no | n/a | n/a | n/a |
| 91g | 2026-10-10 | 106,91 $ | 124,76 $ | 76,07 $ / 130,25 $ | no | n/a | n/a | n/a |
| 98g | 2026-10-17 | 109,47 $ | 127,75 $ | 76,07 $ / 130,92 $ | no | n/a | n/a | n/a |
| 105g | 2026-10-24 | 116,81 $ | 136,31 $ | 76,07 $ / 136,31 $ | no | n/a | n/a | n/a |
| 112g | 2026-10-31 | 115,99 $ | 135,36 $ | 76,07 $ / 140,14 $ | no | n/a | n/a | n/a |
| 119g | 2026-11-07 | 108,43 $ | 126,53 $ | 76,07 $ / 140,14 $ | no | n/a | n/a | n/a |
| 126g | 2026-11-14 | 110,66 $ | 129,14 $ | 76,07 $ / 140,14 $ | no | n/a | n/a | n/a |

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
