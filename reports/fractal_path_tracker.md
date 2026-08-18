<!-- FRACTAL_PATH_TRACKER_START -->
# Tracking percorso frattale SOL/BTC

Generato: 2026-08-18 05:32 UTC

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-08-18**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-02-02**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **75,70 $**
- Verdetto principale: **ANALOGIA DEBOLE / SCENARIO SECONDARIO**
- Somiglianza strutturale: **+57,65%**
- Aderenza live principale: **+68,74%**
- Errore medio live principale: **15,63%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE SOLO DI CONTESTO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **73**
- Osservazioni inclusive dal bottom: **74**
- Osservazioni da inizio programma/scanner: **47**
- Errore assoluto medio dal bottom: **12,12%**
- Errore assoluto medio da inizio programma: **15,63%**
- Gap firmato medio ultimi 7 giorni: **-17,92%**
- Errore assoluto medio ultimi 7 giorni: **17,92%**
- Gap ultimo giorno: **-18,13%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **-18,13%**
- Gap firmato medio 7g: **-17,92%**
- Errore assoluto medio 7g: **17,92%**
- Variazione recente gap: **-1,79%**
- Stato gap: **DISALLINEATO SOTTO IL FRATTALE**
- Trend gap: **SOL si sta allontanando sotto il percorso ancorato**

Soglie operative del grafico:

- entro **±5%**: percorso vicino;
- tra **±5% e ±12%**: deviazione gestibile;
- oltre **±12%**: frattale non abbastanza aderente per conferma operativa;
- oltre **±18%**: disallineamento marcato.

## Ultimi giorni del confronto ancorato

|   Giorno | Data SOL   | Data BTC eq.   | SOL reale   | Percorso ancorato   | Gap firmato   | Fase                |
|---------:|:-----------|:---------------|:------------|:--------------------|:--------------|:--------------------|
| 64 | 2026-08-09 | 2023-01-24 | 76,21 $ | 89,17 $ | -14,53% | da inizio programma |
| 65 | 2026-08-10 | 2023-01-25 | 75,95 $ | 91,07 $ | -16,60% | da inizio programma |
| 66 | 2026-08-11 | 2023-01-26 | 76,20 $ | 90,73 $ | -16,02% | da inizio programma |
| 67 | 2026-08-12 | 2023-01-27 | 75,53 $ | 90,91 $ | -16,93% | da inizio programma |
| 68 | 2026-08-13 | 2023-01-28 | 76,18 $ | 90,72 $ | -16,03% | da inizio programma |
| 69 | 2026-08-14 | 2023-01-29 | 75,33 $ | 93,65 $ | -19,57% | da inizio programma |
| 70 | 2026-08-15 | 2023-01-30 | 75,27 $ | 89,97 $ | -16,34% | da inizio programma |
| 71 | 2026-08-16 | 2023-01-31 | 74,54 $ | 91,15 $ | -18,22% | da inizio programma |
| 72 | 2026-08-17 | 2023-02-01 | 74,54 $ | 93,45 $ | -20,24% | da inizio programma |
| 73 | 2026-08-18 | 2023-02-02 | 75,70 $ | 92,46 $ | -18,13% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-08-25 | 85,95 $ | 70,37 $ | 70,37 $ / 75,70 $ | no | n/a | n/a | n/a |
| 14g | 2026-09-01 | 93,06 $ | 76,19 $ | 69,83 $ / 78,40 $ | no | n/a | n/a | n/a |
| 21g | 2026-09-08 | 94,33 $ | 77,23 $ | 69,83 $ / 80,08 $ | no | n/a | n/a | n/a |
| 28g | 2026-09-15 | 92,48 $ | 75,71 $ | 69,83 $ / 80,08 $ | no | n/a | n/a | n/a |
| 35g | 2026-09-22 | 80,21 $ | 65,67 $ | 65,67 $ / 80,08 $ | no | n/a | n/a | n/a |
| 42g | 2026-09-29 | 98,69 $ | 80,80 $ | 65,11 $ / 80,80 $ | no | n/a | n/a | n/a |
| 49g | 2026-10-06 | 111,61 $ | 91,38 $ | 65,11 $ / 91,38 $ | no | n/a | n/a | n/a |
| 56g | 2026-10-13 | 110,43 $ | 90,41 $ | 65,11 $ / 91,43 $ | no | n/a | n/a | n/a |
| 63g | 2026-10-20 | 110,47 $ | 90,45 $ | 65,11 $ / 91,85 $ | no | n/a | n/a | n/a |
| 70g | 2026-10-27 | 119,75 $ | 98,04 $ | 65,11 $ / 98,04 $ | no | n/a | n/a | n/a |
| 77g | 2026-11-03 | 111,27 $ | 91,10 $ | 65,11 $ / 98,32 $ | no | n/a | n/a | n/a |
| 84g | 2026-11-10 | 116,10 $ | 95,06 $ | 65,11 $ / 98,32 $ | no | n/a | n/a | n/a |
| 91g | 2026-11-17 | 113,64 $ | 93,04 $ | 65,11 $ / 98,32 $ | no | n/a | n/a | n/a |
| 98g | 2026-11-24 | 106,36 $ | 87,08 $ | 65,11 $ / 98,32 $ | no | n/a | n/a | n/a |
| 105g | 2026-12-01 | 105,70 $ | 86,54 $ | 65,11 $ / 98,32 $ | no | n/a | n/a | n/a |
| 112g | 2026-12-08 | 104,30 $ | 85,39 $ | 65,11 $ / 98,32 $ | no | n/a | n/a | n/a |
| 119g | 2026-12-15 | 105,65 $ | 86,50 $ | 65,11 $ / 98,32 $ | no | n/a | n/a | n/a |
| 126g | 2026-12-22 | 104,42 $ | 85,49 $ | 65,11 $ / 98,32 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 35 | 42,86% | 6,96% | 14,07% |
| 14g | 28 | 39,29% | 15,50% | 13,61% |
| 21g | 21 | 23,81% | 25,77% | 15,84% |
| 28g | 14 | 28,57% | 29,08% | 17,19% |
| 35g | 7 | 0,00% | 29,67% | 18,50% |
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
