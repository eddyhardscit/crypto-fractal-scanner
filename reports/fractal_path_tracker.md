<!-- FRACTAL_PATH_TRACKER_START -->
# Tracking percorso frattale SOL/BTC

Generato: 2026-09-14 05:32 UTC

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-09-14**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-03-01**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **101,00 $**
- Verdetto principale: **ANALOGIA DEBOLE / SCENARIO SECONDARIO**
- Somiglianza strutturale: **+70,41%**
- Aderenza live principale: **+72,66%**
- Errore medio live principale: **13,67%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE SOLO DI CONTESTO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **100**
- Osservazioni inclusive dal bottom: **101**
- Osservazioni da inizio programma/scanner: **74**
- Errore assoluto medio dal bottom: **11,62%**
- Errore assoluto medio da inizio programma: **13,67%**
- Gap firmato medio ultimi 7 giorni: **+9,86%**
- Errore assoluto medio ultimi 7 giorni: **9,86%**
- Gap ultimo giorno: **+8,43%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **+8,43%**
- Gap firmato medio 7g: **+9,86%**
- Errore assoluto medio 7g: **9,86%**
- Variazione recente gap: **-1,90%**
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
| 91 | 2026-09-05 | 2023-02-20 | 103,19 $ | 97,81 $ | +5,50% | da inizio programma |
| 92 | 2026-09-06 | 2023-02-21 | 106,45 $ | 96,26 $ | +10,58% | da inizio programma |
| 93 | 2026-09-07 | 2023-02-22 | 103,87 $ | 95,29 $ | +9,01% | da inizio programma |
| 94 | 2026-09-08 | 2023-02-23 | 103,33 $ | 94,33 $ | +9,53% | da inizio programma |
| 95 | 2026-09-09 | 2023-02-24 | 101,61 $ | 91,38 $ | +11,19% | da inizio programma |
| 96 | 2026-09-10 | 2023-02-25 | 98,69 $ | 91,29 $ | +8,10% | da inizio programma |
| 97 | 2026-09-11 | 2023-02-26 | 102,40 $ | 92,81 $ | +10,33% | da inizio programma |
| 98 | 2026-09-12 | 2023-02-27 | 101,79 $ | 92,66 $ | +9,85% | da inizio programma |
| 99 | 2026-09-13 | 2023-02-28 | 101,79 $ | 91,18 $ | +11,63% | da inizio programma |
| 100 | 2026-09-14 | 2023-03-01 | 101,00 $ | 93,15 $ | +8,43% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-09-21 | 85,55 $ | 92,76 $ | 92,76 $ / 101,00 $ | no | n/a | n/a | n/a |
| 14g | 2026-09-28 | 96,02 $ | 104,12 $ | 86,22 $ / 105,70 $ | no | n/a | n/a | n/a |
| 21g | 2026-10-05 | 107,57 $ | 116,64 $ | 86,22 $ / 120,35 $ | no | n/a | n/a | n/a |
| 28g | 2026-10-12 | 111,67 $ | 121,08 $ | 86,22 $ / 121,08 $ | no | n/a | n/a | n/a |
| 35g | 2026-10-19 | 111,00 $ | 120,35 $ | 86,22 $ / 121,64 $ | no | n/a | n/a | n/a |
| 42g | 2026-10-26 | 118,72 $ | 128,73 $ | 86,22 $ / 129,14 $ | no | n/a | n/a | n/a |
| 49g | 2026-11-02 | 113,54 $ | 123,11 $ | 86,22 $ / 130,21 $ | no | n/a | n/a | n/a |
| 56g | 2026-11-09 | 111,96 $ | 121,40 $ | 86,22 $ / 130,21 $ | no | n/a | n/a | n/a |
| 63g | 2026-11-16 | 114,26 $ | 123,89 $ | 86,22 $ / 130,21 $ | no | n/a | n/a | n/a |
| 70g | 2026-11-23 | 108,81 $ | 117,98 $ | 86,22 $ / 130,21 $ | no | n/a | n/a | n/a |
| 77g | 2026-11-30 | 107,93 $ | 117,03 $ | 86,22 $ / 130,21 $ | no | n/a | n/a | n/a |
| 84g | 2026-12-07 | 103,74 $ | 112,48 $ | 86,22 $ / 130,21 $ | no | n/a | n/a | n/a |
| 91g | 2026-12-14 | 107,22 $ | 116,26 $ | 86,22 $ / 130,21 $ | no | n/a | n/a | n/a |
| 98g | 2026-12-21 | 103,78 $ | 112,53 $ | 86,22 $ / 130,21 $ | no | n/a | n/a | n/a |
| 105g | 2026-12-28 | 98,97 $ | 107,31 $ | 86,22 $ / 130,21 $ | no | n/a | n/a | n/a |
| 112g | 2027-01-04 | 118,28 $ | 128,25 $ | 86,22 $ / 130,21 $ | no | n/a | n/a | n/a |
| 119g | 2027-01-11 | 118,52 $ | 128,51 $ | 86,22 $ / 131,11 $ | no | n/a | n/a | n/a |
| 126g | 2027-01-18 | 120,20 $ | 130,33 $ | 86,22 $ / 133,08 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 60 | 41,67% | 10,33% | 12,57% |
| 14g | 53 | 26,42% | 17,17% | 11,45% |
| 21g | 46 | 17,39% | 25,65% | 12,88% |
| 28g | 39 | 28,21% | 26,55% | 12,53% |
| 35g | 34 | 38,24% | 19,58% | 11,54% |
| 42g | 27 | 74,07% | 10,95% | 10,70% |
| 49g | 20 | 100,00% | 5,31% | 10,39% |
| 56g | 13 | 100,00% | 6,38% | 9,14% |
| 63g | 6 | 100,00% | 6,28% | 10,06% |
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
