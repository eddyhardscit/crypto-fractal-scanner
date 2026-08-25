<!-- FRACTAL_PATH_TRACKER_START -->
# Tracking percorso frattale SOL/BTC

Generato: 2026-08-25 05:32 UTC

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-08-25**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-02-09**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **102,48 $**
- Verdetto principale: **ANALOGIA DEBOLE / SCENARIO SECONDARIO**
- Somiglianza strutturale: **+63,53%**
- Aderenza live principale: **+71,07%**
- Errore medio live principale: **14,47%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE SOLO DI CONTESTO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **80**
- Osservazioni inclusive dal bottom: **81**
- Osservazioni da inizio programma/scanner: **54**
- Errore assoluto medio dal bottom: **11,65%**
- Errore assoluto medio da inizio programma: **14,47%**
- Gap firmato medio ultimi 7 giorni: **+3,58%**
- Errore assoluto medio ultimi 7 giorni: **7,08%**
- Gap ultimo giorno: **+19,23%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **+19,23%**
- Gap firmato medio 7g: **+3,58%**
- Errore assoluto medio 7g: **7,08%**
- Variazione recente gap: **+14,49%**
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
| 71 | 2026-08-16 | 2023-01-31 | 74,54 $ | 91,15 $ | -18,22% | da inizio programma |
| 72 | 2026-08-17 | 2023-02-01 | 75,94 $ | 93,45 $ | -18,74% | da inizio programma |
| 73 | 2026-08-18 | 2023-02-02 | 77,03 $ | 92,46 $ | -16,69% | da inizio programma |
| 74 | 2026-08-19 | 2023-02-03 | 85,37 $ | 92,37 $ | -7,58% | da inizio programma |
| 75 | 2026-08-20 | 2023-02-04 | 87,64 $ | 91,91 $ | -4,65% | da inizio programma |
| 76 | 2026-08-21 | 2023-02-05 | 93,65 $ | 90,43 $ | +3,57% | da inizio programma |
| 77 | 2026-08-22 | 2023-02-06 | 93,91 $ | 89,66 $ | +4,75% | da inizio programma |
| 78 | 2026-08-23 | 2023-02-07 | 95,44 $ | 91,64 $ | +4,15% | da inizio programma |
| 79 | 2026-08-24 | 2023-02-08 | 95,44 $ | 90,36 $ | +5,62% | da inizio programma |
| 80 | 2026-08-25 | 2023-02-09 | 102,48 $ | 85,95 $ | +19,23% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-09-01 | 93,06 $ | 110,96 $ | 101,69 $ / 114,17 $ | no | n/a | n/a | n/a |
| 14g | 2026-09-08 | 94,33 $ | 112,48 $ | 101,69 $ / 116,62 $ | no | n/a | n/a | n/a |
| 21g | 2026-09-15 | 92,48 $ | 110,26 $ | 101,69 $ / 116,62 $ | no | n/a | n/a | n/a |
| 28g | 2026-09-22 | 80,21 $ | 95,64 $ | 95,64 $ / 116,62 $ | no | n/a | n/a | n/a |
| 35g | 2026-09-29 | 98,69 $ | 117,67 $ | 94,82 $ / 117,67 $ | no | n/a | n/a | n/a |
| 42g | 2026-10-06 | 111,61 $ | 133,08 $ | 94,82 $ / 133,08 $ | no | n/a | n/a | n/a |
| 49g | 2026-10-13 | 110,43 $ | 131,67 $ | 94,82 $ / 133,15 $ | no | n/a | n/a | n/a |
| 56g | 2026-10-20 | 110,47 $ | 131,72 $ | 94,82 $ / 133,76 $ | no | n/a | n/a | n/a |
| 63g | 2026-10-27 | 119,75 $ | 142,78 $ | 94,82 $ / 142,78 $ | no | n/a | n/a | n/a |
| 70g | 2026-11-03 | 111,27 $ | 132,67 $ | 94,82 $ / 143,19 $ | no | n/a | n/a | n/a |
| 77g | 2026-11-10 | 116,10 $ | 138,43 $ | 94,82 $ / 143,19 $ | no | n/a | n/a | n/a |
| 84g | 2026-11-17 | 113,64 $ | 135,49 $ | 94,82 $ / 143,19 $ | no | n/a | n/a | n/a |
| 91g | 2026-11-24 | 106,36 $ | 126,82 $ | 94,82 $ / 143,19 $ | no | n/a | n/a | n/a |
| 98g | 2026-12-01 | 105,70 $ | 126,03 $ | 94,82 $ / 143,19 $ | no | n/a | n/a | n/a |
| 105g | 2026-12-08 | 104,30 $ | 124,35 $ | 94,82 $ / 143,19 $ | no | n/a | n/a | n/a |
| 112g | 2026-12-15 | 105,65 $ | 125,97 $ | 94,82 $ / 143,19 $ | no | n/a | n/a | n/a |
| 119g | 2026-12-22 | 104,42 $ | 124,50 $ | 94,82 $ / 143,19 $ | no | n/a | n/a | n/a |
| 126g | 2026-12-29 | 100,75 $ | 120,13 $ | 94,82 $ / 143,19 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 40 | 40,00% | 9,91% | 13,13% |
| 14g | 35 | 31,43% | 17,22% | 12,13% |
| 21g | 28 | 21,43% | 23,29% | 13,36% |
| 28g | 21 | 52,38% | 22,99% | 13,31% |
| 35g | 14 | 64,29% | 20,11% | 11,59% |
| 42g | 7 | 100,00% | 11,38% | 7,46% |
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
