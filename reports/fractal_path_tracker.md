<!-- FRACTAL_PATH_TRACKER_START -->
# Tracking percorso frattale SOL/BTC

Generato: 2026-10-08 05:32 UTC

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-10-08**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-03-25**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **115,51 $**
- Verdetto principale: **STRUTTURA ANALOGA, PREZZO NON ADERENTE**
- Somiglianza strutturale: **+72,79%**
- Aderenza live principale: **+68,98%**
- Errore medio live principale: **15,51%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE NON CONFERMATO DAL PREZZO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **124**
- Osservazioni inclusive dal bottom: **125**
- Osservazioni da inizio programma/scanner: **98**
- Errore assoluto medio dal bottom: **13,46%**
- Errore assoluto medio da inizio programma: **15,51%**
- Gap firmato medio ultimi 7 giorni: **+9,27%**
- Errore assoluto medio ultimi 7 giorni: **9,27%**
- Gap ultimo giorno: **+6,65%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **+6,65%**
- Gap firmato medio 7g: **+9,27%**
- Errore assoluto medio 7g: **9,27%**
- Variazione recente gap: **-5,60%**
- Stato gap: **SOPRA IL FRATTALE**
- Trend gap: **SOL resta sopra il percorso ancorato, ma sta riducendo il distacco**

Soglie operative del grafico:

- entro **±5%**: percorso vicino;
- tra **±5% e ±12%**: deviazione gestibile;
- oltre **±12%**: frattale non abbastanza aderente per conferma operativa;
- oltre **±18%**: disallineamento marcato.

## Ultimi giorni del confronto ancorato

|   Giorno | Data SOL   | Data BTC eq.   | SOL reale   | Percorso ancorato   | Gap firmato   | Fase                |
|---------:|:-----------|:---------------|:------------|:--------------------|:--------------|:--------------------|
| 115 | 2026-09-29 | 2023-03-16 | 119,06 $ | 98,69 $ | +20,64% | da inizio programma |
| 116 | 2026-09-30 | 2023-03-17 | 117,99 $ | 108,03 $ | +9,22% | da inizio programma |
| 117 | 2026-10-01 | 2023-03-18 | 118,40 $ | 106,22 $ | +11,46% | da inizio programma |
| 118 | 2026-10-02 | 2023-03-19 | 118,62 $ | 110,45 $ | +7,39% | da inizio programma |
| 119 | 2026-10-03 | 2023-03-20 | 119,65 $ | 109,38 $ | +9,38% | da inizio programma |
| 120 | 2026-10-04 | 2023-03-21 | 121,53 $ | 110,99 $ | +9,49% | da inizio programma |
| 121 | 2026-10-05 | 2023-03-22 | 120,75 $ | 107,57 $ | +12,25% | da inizio programma |
| 122 | 2026-10-06 | 2023-03-23 | 120,79 $ | 111,61 $ | +8,22% | da inizio programma |
| 123 | 2026-10-07 | 2023-03-24 | 120,79 $ | 108,30 $ | +11,53% | da inizio programma |
| 124 | 2026-10-08 | 2023-03-25 | 115,51 $ | 108,31 $ | +6,65% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-10-15 | 111,92 $ | 119,36 $ | 114,02 $ / 119,64 $ | no | n/a | n/a | n/a |
| 14g | 2026-10-22 | 110,09 $ | 117,41 $ | 114,02 $ / 119,64 $ | no | n/a | n/a | n/a |
| 21g | 2026-10-29 | 119,43 $ | 127,37 $ | 114,02 $ / 128,08 $ | no | n/a | n/a | n/a |
| 28g | 2026-11-05 | 109,58 $ | 116,87 $ | 114,02 $ / 128,08 $ | no | n/a | n/a | n/a |
| 35g | 2026-11-12 | 115,22 $ | 122,88 $ | 114,02 $ / 128,08 $ | no | n/a | n/a | n/a |
| 42g | 2026-11-19 | 113,86 $ | 121,43 $ | 114,02 $ / 128,08 $ | no | n/a | n/a | n/a |
| 49g | 2026-11-26 | 105,51 $ | 112,52 $ | 112,52 $ / 128,08 $ | no | n/a | n/a | n/a |
| 56g | 2026-12-03 | 106,87 $ | 113,98 $ | 112,52 $ / 128,08 $ | no | n/a | n/a | n/a |
| 63g | 2026-12-10 | 105,84 $ | 112,88 $ | 110,64 $ / 128,08 $ | no | n/a | n/a | n/a |
| 70g | 2026-12-17 | 106,66 $ | 113,75 $ | 110,64 $ / 128,08 $ | no | n/a | n/a | n/a |
| 77g | 2026-12-24 | 101,83 $ | 108,61 $ | 108,22 $ / 128,08 $ | no | n/a | n/a | n/a |
| 84g | 2026-12-31 | 104,43 $ | 111,38 $ | 105,55 $ / 128,08 $ | no | n/a | n/a | n/a |
| 91g | 2027-01-07 | 120,34 $ | 128,34 $ | 105,55 $ / 128,96 $ | no | n/a | n/a | n/a |
| 98g | 2027-01-14 | 120,50 $ | 128,51 $ | 105,55 $ / 128,96 $ | no | n/a | n/a | n/a |
| 105g | 2027-01-21 | 119,33 $ | 127,26 $ | 105,55 $ / 130,89 $ | no | n/a | n/a | n/a |
| 112g | 2027-01-28 | 119,34 $ | 127,28 $ | 105,55 $ / 132,24 $ | no | n/a | n/a | n/a |
| 119g | 2027-02-04 | 117,28 $ | 125,08 $ | 105,55 $ / 132,24 $ | no | n/a | n/a | n/a |
| 126g | 2027-02-11 | 115,64 $ | 123,33 $ | 105,55 $ / 132,24 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 79 | 40,51% | 11,76% | 14,48% |
| 14g | 73 | 27,40% | 17,39% | 14,84% |
| 21g | 70 | 28,57% | 20,74% | 15,81% |
| 28g | 63 | 26,98% | 21,87% | 15,94% |
| 35g | 56 | 33,93% | 23,20% | 15,75% |
| 42g | 49 | 46,94% | 21,74% | 14,63% |
| 49g | 42 | 47,62% | 24,84% | 16,87% |
| 56g | 35 | 45,71% | 22,23% | 17,90% |
| 63g | 30 | 36,67% | 16,61% | 19,59% |
| 70g | 23 | 43,48% | 10,46% | 22,74% |
| 77g | 16 | 56,25% | 8,79% | 15,88% |
| 84g | 9 | 100,00% | 6,27% | 9,27% |
| 91g | 2 | 100,00% | 9,20% | n/a |
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
