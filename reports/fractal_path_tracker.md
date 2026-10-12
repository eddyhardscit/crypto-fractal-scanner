<!-- FRACTAL_PATH_TRACKER_START -->
# Tracking percorso frattale SOL/BTC

Generato: 2026-10-12 05:32 UTC

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-10-12**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-03-29**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **112,60 $**
- Verdetto principale: **ANALOGIA DEBOLE / SCENARIO SECONDARIO**
- Somiglianza strutturale: **+73,30%**
- Aderenza live principale: **+70,25%**
- Errore medio live principale: **14,87%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE SOLO DI CONTESTO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **128**
- Osservazioni inclusive dal bottom: **129**
- Osservazioni da inizio programma/scanner: **102**
- Errore assoluto medio dal bottom: **13,02%**
- Errore assoluto medio da inizio programma: **14,87%**
- Gap firmato medio ultimi 7 giorni: **+3,11%**
- Errore assoluto medio ultimi 7 giorni: **3,40%**
- Gap ultimo giorno: **+0,83%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **+0,83%**
- Gap firmato medio 7g: **+3,11%**
- Errore assoluto medio 7g: **3,40%**
- Variazione recente gap: **+1,86%**
- Stato gap: **VICINO AL FRATTALE**
- Trend gap: **SOL sta aumentando il distacco sopra il percorso ancorato**

Soglie operative del grafico:

- entro **±5%**: percorso vicino;
- tra **±5% e ±12%**: deviazione gestibile;
- oltre **±12%**: frattale non abbastanza aderente per conferma operativa;
- oltre **±18%**: disallineamento marcato.

## Ultimi giorni del confronto ancorato

|   Giorno | Data SOL   | Data BTC eq.   | SOL reale   | Percorso ancorato   | Gap firmato   | Fase                |
|---------:|:-----------|:---------------|:------------|:--------------------|:--------------|:--------------------|
| 119 | 2026-10-03 | 2023-03-20 | 119,65 $ | 109,38 $ | +9,38% | da inizio programma |
| 120 | 2026-10-04 | 2023-03-21 | 121,53 $ | 110,99 $ | +9,49% | da inizio programma |
| 121 | 2026-10-05 | 2023-03-22 | 120,75 $ | 107,57 $ | +12,25% | da inizio programma |
| 122 | 2026-10-06 | 2023-03-23 | 120,79 $ | 111,61 $ | +8,22% | da inizio programma |
| 123 | 2026-10-07 | 2023-03-24 | 116,22 $ | 108,30 $ | +7,31% | da inizio programma |
| 124 | 2026-10-08 | 2023-03-25 | 109,44 $ | 108,31 $ | +1,05% | da inizio programma |
| 125 | 2026-10-09 | 2023-03-26 | 109,14 $ | 110,28 $ | -1,03% | da inizio programma |
| 126 | 2026-10-10 | 2023-03-27 | 110,03 $ | 106,91 $ | +2,92% | da inizio programma |
| 127 | 2026-10-11 | 2023-03-28 | 110,03 $ | 107,42 $ | +2,44% | da inizio programma |
| 128 | 2026-10-12 | 2023-03-29 | 112,60 $ | 111,67 $ | +0,83% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-10-19 | 111,00 $ | 111,92 $ | 110,38 $ / 113,12 $ | no | n/a | n/a | n/a |
| 14g | 2026-10-26 | 118,72 $ | 119,71 $ | 110,38 $ / 120,09 $ | no | n/a | n/a | n/a |
| 21g | 2026-11-02 | 113,54 $ | 114,48 $ | 110,38 $ / 121,09 $ | no | n/a | n/a | n/a |
| 28g | 2026-11-09 | 111,96 $ | 112,89 $ | 108,34 $ / 121,09 $ | no | n/a | n/a | n/a |
| 35g | 2026-11-16 | 114,26 $ | 115,21 $ | 108,34 $ / 121,09 $ | no | n/a | n/a | n/a |
| 42g | 2026-11-23 | 108,81 $ | 109,71 $ | 108,34 $ / 121,09 $ | no | n/a | n/a | n/a |
| 49g | 2026-11-30 | 107,93 $ | 108,83 $ | 106,39 $ / 121,09 $ | no | n/a | n/a | n/a |
| 56g | 2026-12-07 | 103,74 $ | 104,60 $ | 104,60 $ / 121,09 $ | no | n/a | n/a | n/a |
| 63g | 2026-12-14 | 107,22 $ | 108,12 $ | 104,60 $ / 121,09 $ | no | n/a | n/a | n/a |
| 70g | 2026-12-21 | 103,78 $ | 104,65 $ | 102,32 $ / 121,09 $ | no | n/a | n/a | n/a |
| 77g | 2026-12-28 | 98,97 $ | 99,80 $ | 99,80 $ / 121,09 $ | no | n/a | n/a | n/a |
| 84g | 2027-01-04 | 118,28 $ | 119,27 $ | 99,80 $ / 121,09 $ | no | n/a | n/a | n/a |
| 91g | 2027-01-11 | 118,52 $ | 119,50 $ | 99,80 $ / 121,92 $ | no | n/a | n/a | n/a |
| 98g | 2027-01-18 | 120,20 $ | 121,20 $ | 99,80 $ / 123,75 $ | no | n/a | n/a | n/a |
| 105g | 2027-01-25 | 119,72 $ | 120,72 $ | 99,80 $ / 123,75 $ | no | n/a | n/a | n/a |
| 112g | 2027-02-01 | 117,84 $ | 118,82 $ | 99,80 $ / 125,02 $ | no | n/a | n/a | n/a |
| 119g | 2027-02-08 | 115,64 $ | 116,60 $ | 99,80 $ / 125,02 $ | no | n/a | n/a | n/a |
| 126g | 2027-02-15 | 114,84 $ | 115,79 $ | 99,80 $ / 125,02 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 83 | 37,35% | 11,60% | 13,80% |
| 14g | 77 | 23,38% | 17,66% | 14,02% |
| 21g | 70 | 28,57% | 20,83% | 15,67% |
| 28g | 67 | 31,34% | 21,13% | 14,92% |
| 35g | 60 | 40,00% | 21,99% | 14,62% |
| 42g | 53 | 50,94% | 21,32% | 13,43% |
| 49g | 46 | 52,17% | 22,55% | 15,28% |
| 56g | 39 | 41,03% | 22,38% | 16,16% |
| 63g | 34 | 32,35% | 16,86% | 17,06% |
| 70g | 27 | 37,04% | 10,60% | 18,99% |
| 77g | 20 | 65,00% | 9,00% | 12,21% |
| 84g | 13 | 100,00% | 8,51% | 5,67% |
| 91g | 6 | 100,00% | 13,30% | 1,81% |
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
