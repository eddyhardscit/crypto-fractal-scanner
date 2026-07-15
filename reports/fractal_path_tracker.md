<!-- FRACTAL_PATH_TRACKER_START -->
# Tracking percorso frattale SOL/BTC

Generato: 2026-07-15 07:26 UTC

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-07-15**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2022-12-30**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **77,68 $**
- Verdetto principale: **ANALOGIA DEBOLE / SCENARIO SECONDARIO**
- Somiglianza strutturale: **+64,49%**
- Aderenza live principale: **+60,72%**
- Errore medio live principale: **19,64%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE SOLO DI CONTESTO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **39**
- Osservazioni inclusive dal bottom: **40**
- Osservazioni da inizio programma/scanner: **13**
- Errore assoluto medio dal bottom: **10,45%**
- Errore assoluto medio da inizio programma: **19,64%**
- Gap firmato medio ultimi 7 giorni: **+17,07%**
- Errore assoluto medio ultimi 7 giorni: **17,07%**
- Gap ultimo giorno: **+18,77%**
- Stato aderenza: **STACCATO / MOLTO IN ANTICIPO**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **+18,77%**
- Gap firmato medio 7g: **+17,07%**
- Errore assoluto medio 7g: **17,07%**
- Variazione recente gap: **+2,04%**
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
| 30 | 2026-07-06 | 2022-12-21 | 81,92 $ | 66,25 $ | +23,65% | da inizio programma |
| 31 | 2026-07-07 | 2022-12-22 | 80,65 $ | 66,30 $ | +21,64% | da inizio programma |
| 32 | 2026-07-08 | 2022-12-23 | 77,79 $ | 66,17 $ | +17,56% | da inizio programma |
| 33 | 2026-07-09 | 2022-12-24 | 78,05 $ | 66,37 $ | +17,60% | da inizio programma |
| 34 | 2026-07-10 | 2022-12-25 | 78,07 $ | 66,34 $ | +17,67% | da inizio programma |
| 35 | 2026-07-11 | 2022-12-26 | 76,82 $ | 66,65 $ | +15,26% | da inizio programma |
| 36 | 2026-07-12 | 2022-12-27 | 76,87 $ | 65,85 $ | +16,74% | da inizio programma |
| 37 | 2026-07-13 | 2022-12-28 | 74,86 $ | 65,20 $ | +14,81% | da inizio programma |
| 38 | 2026-07-14 | 2022-12-29 | 77,76 $ | 65,56 $ | +18,62% | da inizio programma |
| 39 | 2026-07-15 | 2022-12-30 | 77,68 $ | 65,40 $ | +18,77% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-07-22 | 66,78 $ | 79,31 $ | 77,42 $ / 79,31 $ | no | n/a | n/a | n/a |
| 14g | 2026-07-29 | 78,43 $ | 93,15 $ | 77,42 $ / 93,15 $ | no | n/a | n/a | n/a |
| 21g | 2026-08-05 | 89,33 $ | 106,10 $ | 77,42 $ / 106,10 $ | no | n/a | n/a | n/a |
| 28g | 2026-08-12 | 90,91 $ | 107,98 $ | 77,42 $ / 108,16 $ | no | n/a | n/a | n/a |
| 35g | 2026-08-19 | 92,37 $ | 109,71 $ | 77,42 $ / 111,24 $ | no | n/a | n/a | n/a |
| 42g | 2026-08-26 | 85,29 $ | 101,30 $ | 77,42 $ / 111,24 $ | no | n/a | n/a | n/a |
| 49g | 2026-09-02 | 96,77 $ | 114,94 $ | 77,42 $ / 114,94 $ | no | n/a | n/a | n/a |
| 56g | 2026-09-09 | 91,38 $ | 108,54 $ | 77,42 $ / 116,17 $ | no | n/a | n/a | n/a |
| 63g | 2026-09-16 | 88,09 $ | 104,63 $ | 77,42 $ / 116,17 $ | no | n/a | n/a | n/a |
| 70g | 2026-09-23 | 79,52 $ | 94,45 $ | 77,42 $ / 116,17 $ | no | n/a | n/a | n/a |
| 77g | 2026-09-30 | 108,03 $ | 128,31 $ | 77,42 $ / 128,31 $ | no | n/a | n/a | n/a |
| 84g | 2026-10-07 | 108,30 $ | 128,64 $ | 77,42 $ / 132,57 $ | no | n/a | n/a | n/a |
| 91g | 2026-10-14 | 112,18 $ | 133,24 $ | 77,42 $ / 133,24 $ | no | n/a | n/a | n/a |
| 98g | 2026-10-21 | 110,01 $ | 130,66 $ | 77,42 $ / 133,24 $ | no | n/a | n/a | n/a |
| 105g | 2026-10-28 | 120,09 $ | 142,64 $ | 77,42 $ / 142,64 $ | no | n/a | n/a | n/a |
| 112g | 2026-11-04 | 107,45 $ | 127,62 $ | 77,42 $ / 142,64 $ | no | n/a | n/a | n/a |
| 119g | 2026-11-11 | 115,58 $ | 137,28 $ | 77,42 $ / 142,64 $ | no | n/a | n/a | n/a |
| 126g | 2026-11-18 | 116,34 $ | 138,19 $ | 77,42 $ / 142,64 $ | no | n/a | n/a | n/a |

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
