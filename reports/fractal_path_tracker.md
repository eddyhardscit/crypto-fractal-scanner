<!-- FRACTAL_PATH_TRACKER_START -->
# Tracking percorso frattale SOL/BTC

Generato: 2026-07-28 05:14 UTC

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-07-28**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-01-12**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **73,28 $**
- Verdetto principale: **ANALOGIA DEBOLE / SCENARIO SECONDARIO**
- Somiglianza strutturale: **+64,21%**
- Aderenza live principale: **+67,56%**
- Errore medio live principale: **16,22%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE SOLO DI CONTESTO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **52**
- Osservazioni inclusive dal bottom: **53**
- Osservazioni da inizio programma/scanner: **26**
- Errore assoluto medio dal bottom: **11,03%**
- Errore assoluto medio da inizio programma: **16,22%**
- Gap firmato medio ultimi 7 giorni: **+9,76%**
- Errore assoluto medio ultimi 7 giorni: **10,16%**
- Gap ultimo giorno: **-1,41%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **-1,41%**
- Gap firmato medio 7g: **+9,76%**
- Errore assoluto medio 7g: **10,16%**
- Variazione recente gap: **-11,29%**
- Stato gap: **VICINO AL FRATTALE**
- Trend gap: **SOL si sta allontanando sotto il percorso ancorato**

Soglie operative del grafico:

- entro **±5%**: percorso vicino;
- tra **±5% e ±12%**: deviazione gestibile;
- oltre **±12%**: frattale non abbastanza aderente per conferma operativa;
- oltre **±18%**: disallineamento marcato.

## Ultimi giorni del confronto ancorato

|   Giorno | Data SOL   | Data BTC eq.   | SOL reale   | Percorso ancorato   | Gap firmato   | Fase                |
|---------:|:-----------|:---------------|:------------|:--------------------|:--------------|:--------------------|
| 43 | 2026-07-19 | 2023-01-03 | 76,36 $ | 65,71 $ | +16,21% | da inizio programma |
| 44 | 2026-07-20 | 2023-01-04 | 77,79 $ | 66,43 $ | +17,11% | da inizio programma |
| 45 | 2026-07-21 | 2023-01-05 | 78,11 $ | 66,32 $ | +17,77% | da inizio programma |
| 46 | 2026-07-22 | 2023-01-06 | 77,91 $ | 66,78 $ | +16,66% | da inizio programma |
| 47 | 2026-07-23 | 2023-01-07 | 75,86 $ | 66,79 $ | +13,58% | da inizio programma |
| 48 | 2026-07-24 | 2023-01-08 | 73,88 $ | 67,33 $ | +9,73% | da inizio programma |
| 49 | 2026-07-25 | 2023-01-09 | 74,43 $ | 67,74 $ | +9,87% | da inizio programma |
| 50 | 2026-07-26 | 2023-01-10 | 76,60 $ | 68,73 $ | +11,46% | da inizio programma |
| 51 | 2026-07-27 | 2023-01-11 | 76,60 $ | 70,65 $ | +8,43% | da inizio programma |
| 52 | 2026-07-28 | 2023-01-12 | 73,28 $ | 74,33 $ | -1,41% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-08-04 | 83,07 $ | 81,89 $ | 73,28 $ / 82,21 $ | no | n/a | n/a | n/a |
| 14g | 2026-08-11 | 90,73 $ | 89,45 $ | 73,28 $ / 89,78 $ | no | n/a | n/a | n/a |
| 21g | 2026-08-18 | 92,46 $ | 91,15 $ | 73,28 $ / 92,33 $ | no | n/a | n/a | n/a |
| 28g | 2026-08-25 | 85,95 $ | 84,73 $ | 73,28 $ / 92,33 $ | no | n/a | n/a | n/a |
| 35g | 2026-09-01 | 93,06 $ | 91,74 $ | 73,28 $ / 94,40 $ | no | n/a | n/a | n/a |
| 42g | 2026-09-08 | 94,33 $ | 93,00 $ | 73,28 $ / 96,42 $ | no | n/a | n/a | n/a |
| 49g | 2026-09-15 | 92,48 $ | 91,17 $ | 73,28 $ / 96,42 $ | no | n/a | n/a | n/a |
| 56g | 2026-09-22 | 80,21 $ | 79,08 $ | 73,28 $ / 96,42 $ | no | n/a | n/a | n/a |
| 63g | 2026-09-29 | 98,69 $ | 97,29 $ | 73,28 $ / 97,29 $ | no | n/a | n/a | n/a |
| 70g | 2026-10-06 | 111,61 $ | 110,03 $ | 73,28 $ / 110,03 $ | no | n/a | n/a | n/a |
| 77g | 2026-10-13 | 110,43 $ | 108,87 $ | 73,28 $ / 110,09 $ | no | n/a | n/a | n/a |
| 84g | 2026-10-20 | 110,47 $ | 108,91 $ | 73,28 $ / 110,60 $ | no | n/a | n/a | n/a |
| 91g | 2026-10-27 | 119,75 $ | 118,05 $ | 73,28 $ / 118,05 $ | no | n/a | n/a | n/a |
| 98g | 2026-11-03 | 111,27 $ | 109,69 $ | 73,28 $ / 118,39 $ | no | n/a | n/a | n/a |
| 105g | 2026-11-10 | 116,10 $ | 114,46 $ | 73,28 $ / 118,39 $ | no | n/a | n/a | n/a |
| 112g | 2026-11-17 | 113,64 $ | 112,03 $ | 73,28 $ / 118,39 $ | no | n/a | n/a | n/a |
| 119g | 2026-11-24 | 106,36 $ | 104,86 $ | 73,28 $ / 118,39 $ | no | n/a | n/a | n/a |
| 126g | 2026-12-01 | 105,70 $ | 104,20 $ | 73,28 $ / 118,39 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 14 | 35,71% | 3,36% | 12,63% |
| 14g | 7 | 28,57% | 6,46% | 8,18% |
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
