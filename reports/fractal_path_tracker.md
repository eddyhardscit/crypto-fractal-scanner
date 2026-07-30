<!-- FRACTAL_PATH_TRACKER_START -->
# Tracking percorso frattale SOL/BTC

Generato: 2026-07-30 05:14 UTC

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-07-30**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-01-14**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **73,43 $**
- Verdetto principale: **ANALOGIA DEBOLE / SCENARIO SECONDARIO**
- Somiglianza strutturale: **+59,87%**
- Aderenza live principale: **+68,94%**
- Errore medio live principale: **15,53%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE SOLO DI CONTESTO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **54**
- Osservazioni inclusive dal bottom: **55**
- Osservazioni da inizio programma/scanner: **28**
- Errore assoluto medio dal bottom: **10,86%**
- Errore assoluto medio da inizio programma: **15,53%**
- Gap firmato medio ultimi 7 giorni: **+2,57%**
- Errore assoluto medio ultimi 7 giorni: **7,72%**
- Gap ultimo giorno: **-11,13%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **-11,13%**
- Gap firmato medio 7g: **+2,57%**
- Errore assoluto medio 7g: **7,72%**
- Variazione recente gap: **-16,08%**
- Stato gap: **SOTTO IL FRATTALE**
- Trend gap: **SOL si sta allontanando sotto il percorso ancorato**

Soglie operative del grafico:

- entro **±5%**: percorso vicino;
- tra **±5% e ±12%**: deviazione gestibile;
- oltre **±12%**: frattale non abbastanza aderente per conferma operativa;
- oltre **±18%**: disallineamento marcato.

## Ultimi giorni del confronto ancorato

|   Giorno | Data SOL   | Data BTC eq.   | SOL reale   | Percorso ancorato   | Gap firmato   | Fase                |
|---------:|:-----------|:---------------|:------------|:--------------------|:--------------|:--------------------|
| 45 | 2026-07-21 | 2023-01-05 | 78,11 $ | 66,32 $ | +17,77% | da inizio programma |
| 46 | 2026-07-22 | 2023-01-06 | 77,91 $ | 66,78 $ | +16,66% | da inizio programma |
| 47 | 2026-07-23 | 2023-01-07 | 75,86 $ | 66,79 $ | +13,58% | da inizio programma |
| 48 | 2026-07-24 | 2023-01-08 | 73,88 $ | 67,33 $ | +9,73% | da inizio programma |
| 49 | 2026-07-25 | 2023-01-09 | 74,43 $ | 67,74 $ | +9,87% | da inizio programma |
| 50 | 2026-07-26 | 2023-01-10 | 76,60 $ | 68,73 $ | +11,46% | da inizio programma |
| 51 | 2026-07-27 | 2023-01-11 | 74,14 $ | 70,65 $ | +4,94% | da inizio programma |
| 52 | 2026-07-28 | 2023-01-12 | 73,70 $ | 74,33 $ | -0,85% | da inizio programma |
| 53 | 2026-07-29 | 2023-01-13 | 73,70 $ | 78,43 $ | -6,03% | da inizio programma |
| 54 | 2026-07-30 | 2023-01-14 | 73,43 $ | 82,63 $ | -11,13% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-08-06 | 89,73 $ | 79,74 $ | 72,42 $ / 79,74 $ | no | n/a | n/a | n/a |
| 14g | 2026-08-13 | 90,72 $ | 80,62 $ | 72,42 $ / 80,93 $ | no | n/a | n/a | n/a |
| 21g | 2026-08-20 | 91,91 $ | 81,68 $ | 72,42 $ / 83,23 $ | no | n/a | n/a | n/a |
| 28g | 2026-08-27 | 86,15 $ | 76,56 $ | 72,42 $ / 83,23 $ | no | n/a | n/a | n/a |
| 35g | 2026-09-03 | 97,07 $ | 86,26 $ | 72,42 $ / 86,26 $ | no | n/a | n/a | n/a |
| 42g | 2026-09-10 | 91,29 $ | 81,13 $ | 72,42 $ / 86,92 $ | no | n/a | n/a | n/a |
| 49g | 2026-09-17 | 88,06 $ | 78,25 $ | 72,42 $ / 86,92 $ | no | n/a | n/a | n/a |
| 56g | 2026-09-24 | 81,28 $ | 72,23 $ | 70,67 $ / 86,92 $ | no | n/a | n/a | n/a |
| 63g | 2026-10-01 | 106,22 $ | 94,40 $ | 70,67 $ / 96,00 $ | no | n/a | n/a | n/a |
| 70g | 2026-10-08 | 108,31 $ | 96,25 $ | 70,67 $ / 99,19 $ | no | n/a | n/a | n/a |
| 77g | 2026-10-15 | 111,92 $ | 99,46 $ | 70,67 $ / 99,69 $ | no | n/a | n/a | n/a |
| 84g | 2026-10-22 | 110,09 $ | 97,83 $ | 70,67 $ / 99,69 $ | no | n/a | n/a | n/a |
| 91g | 2026-10-29 | 119,43 $ | 106,13 $ | 70,67 $ / 106,72 $ | no | n/a | n/a | n/a |
| 98g | 2026-11-05 | 109,58 $ | 97,38 $ | 70,67 $ / 106,72 $ | no | n/a | n/a | n/a |
| 105g | 2026-11-12 | 115,22 $ | 102,39 $ | 70,67 $ / 106,72 $ | no | n/a | n/a | n/a |
| 112g | 2026-11-19 | 113,86 $ | 101,18 $ | 70,67 $ / 106,72 $ | no | n/a | n/a | n/a |
| 119g | 2026-11-26 | 105,51 $ | 93,76 $ | 70,67 $ / 106,72 $ | no | n/a | n/a | n/a |
| 126g | 2026-12-03 | 106,87 $ | 94,97 $ | 70,67 $ / 106,72 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 16 | 25,00% | 5,75% | 11,76% |
| 14g | 9 | 11,11% | 10,30% | 7,72% |
| 21g | 2 | 0,00% | 24,34% | n/a |
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
