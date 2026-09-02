<!-- FRACTAL_PATH_TRACKER_START -->
# Tracking percorso frattale SOL/BTC

Generato: 2026-09-02 05:32 UTC

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-09-02**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-02-17**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **100,24 $**
- Verdetto principale: **ANALOGIA DEBOLE / SCENARIO SECONDARIO**
- Somiglianza strutturale: **+65,97%**
- Aderenza live principale: **+70,75%**
- Errore medio live principale: **14,63%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE SOLO DI CONTESTO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **88**
- Osservazioni inclusive dal bottom: **89**
- Osservazioni da inizio programma/scanner: **62**
- Errore assoluto medio dal bottom: **12,02%**
- Errore assoluto medio da inizio programma: **14,63%**
- Gap firmato medio ultimi 7 giorni: **+15,61%**
- Errore assoluto medio ultimi 7 giorni: **15,61%**
- Gap ultimo giorno: **+3,59%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **+3,59%**
- Gap firmato medio 7g: **+15,61%**
- Errore assoluto medio 7g: **15,61%**
- Variazione recente gap: **-12,80%**
- Stato gap: **VICINO AL FRATTALE**
- Trend gap: **SOL resta sopra il percorso ancorato, ma sta riducendo il distacco**

Soglie operative del grafico:

- entro **±5%**: percorso vicino;
- tra **±5% e ±12%**: deviazione gestibile;
- oltre **±12%**: frattale non abbastanza aderente per conferma operativa;
- oltre **±18%**: disallineamento marcato.

## Ultimi giorni del confronto ancorato

|   Giorno | Data SOL   | Data BTC eq.   | SOL reale   | Percorso ancorato   | Gap firmato   | Fase                |
|---------:|:-----------|:---------------|:------------|:--------------------|:--------------|:--------------------|
| 79 | 2026-08-24 | 2023-02-08 | 98,56 $ | 90,36 $ | +9,07% | da inizio programma |
| 80 | 2026-08-25 | 2023-02-09 | 96,60 $ | 85,95 $ | +12,39% | da inizio programma |
| 81 | 2026-08-26 | 2023-02-10 | 102,17 $ | 85,29 $ | +19,79% | da inizio programma |
| 82 | 2026-08-27 | 2023-02-11 | 109,21 $ | 86,15 $ | +26,76% | da inizio programma |
| 83 | 2026-08-28 | 2023-02-12 | 104,13 $ | 85,83 $ | +21,32% | da inizio programma |
| 84 | 2026-08-29 | 2023-02-13 | 105,65 $ | 85,91 $ | +22,98% | da inizio programma |
| 85 | 2026-08-30 | 2023-02-14 | 101,88 $ | 87,53 $ | +16,39% | da inizio programma |
| 86 | 2026-08-31 | 2023-02-15 | 103,00 $ | 95,75 $ | +7,56% | da inizio programma |
| 87 | 2026-09-01 | 2023-02-16 | 103,00 $ | 93,06 $ | +10,68% | da inizio programma |
| 88 | 2026-09-02 | 2023-02-17 | 100,24 $ | 96,77 $ | +3,59% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-09-09 | 91,38 $ | 94,66 $ | 94,66 $ / 101,32 $ | no | n/a | n/a | n/a |
| 14g | 2026-09-16 | 88,09 $ | 91,25 $ | 91,25 $ / 101,32 $ | no | n/a | n/a | n/a |
| 21g | 2026-09-23 | 79,52 $ | 82,37 $ | 82,37 $ / 101,32 $ | no | n/a | n/a | n/a |
| 28g | 2026-09-30 | 108,03 $ | 111,90 $ | 82,37 $ / 111,90 $ | no | n/a | n/a | n/a |
| 35g | 2026-10-07 | 108,30 $ | 112,19 $ | 82,37 $ / 115,62 $ | no | n/a | n/a | n/a |
| 42g | 2026-10-14 | 112,18 $ | 116,21 $ | 82,37 $ / 116,21 $ | no | n/a | n/a | n/a |
| 49g | 2026-10-21 | 110,01 $ | 113,95 $ | 82,37 $ / 116,21 $ | no | n/a | n/a | n/a |
| 56g | 2026-10-28 | 120,09 $ | 124,40 $ | 82,37 $ / 124,40 $ | no | n/a | n/a | n/a |
| 63g | 2026-11-04 | 107,45 $ | 111,30 $ | 82,37 $ / 124,40 $ | no | n/a | n/a | n/a |
| 70g | 2026-11-11 | 115,58 $ | 119,72 $ | 82,37 $ / 124,40 $ | no | n/a | n/a | n/a |
| 77g | 2026-11-18 | 116,34 $ | 120,52 $ | 82,37 $ / 124,40 $ | no | n/a | n/a | n/a |
| 84g | 2026-11-25 | 105,59 $ | 109,38 $ | 82,37 $ / 124,40 $ | no | n/a | n/a | n/a |
| 91g | 2026-12-02 | 105,93 $ | 109,73 $ | 82,37 $ / 124,40 $ | no | n/a | n/a | n/a |
| 98g | 2026-12-09 | 105,25 $ | 109,03 $ | 82,37 $ / 124,40 $ | no | n/a | n/a | n/a |
| 105g | 2026-12-16 | 107,34 $ | 111,19 $ | 82,37 $ / 124,40 $ | no | n/a | n/a | n/a |
| 112g | 2026-12-23 | 104,31 $ | 108,05 $ | 82,37 $ / 124,40 $ | no | n/a | n/a | n/a |
| 119g | 2026-12-30 | 103,71 $ | 107,43 $ | 82,37 $ / 124,40 $ | no | n/a | n/a | n/a |
| 126g | 2027-01-06 | 120,92 $ | 125,25 $ | 82,37 $ / 125,25 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 48 | 37,50% | 11,40% | 13,58% |
| 14g | 41 | 26,83% | 20,24% | 12,29% |
| 21g | 35 | 17,14% | 26,91% | 14,23% |
| 28g | 29 | 37,93% | 24,91% | 14,02% |
| 35g | 22 | 59,09% | 15,66% | 13,24% |
| 42g | 15 | 100,00% | 8,49% | 12,54% |
| 49g | 8 | 100,00% | 6,18% | 13,75% |
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
