<!-- FRACTAL_PATH_TRACKER_START -->
# Tracking percorso frattale SOL/BTC

Generato: 2026-08-20 05:32 UTC

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-08-20**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-02-04**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **84,87 $**
- Verdetto principale: **ANALOGIA DEBOLE / SCENARIO SECONDARIO**
- Somiglianza strutturale: **+59,37%**
- Aderenza live principale: **+69,15%**
- Errore medio live principale: **15,43%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE SOLO DI CONTESTO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **75**
- Osservazioni inclusive dal bottom: **76**
- Osservazioni da inizio programma/scanner: **49**
- Errore assoluto medio dal bottom: **12,09%**
- Errore assoluto medio da inizio programma: **15,43%**
- Gap firmato medio ultimi 7 giorni: **-16,26%**
- Errore assoluto medio ultimi 7 giorni: **16,26%**
- Gap ultimo giorno: **-7,66%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **-7,66%**
- Gap firmato medio 7g: **-16,26%**
- Errore assoluto medio 7g: **16,26%**
- Variazione recente gap: **+11,08%**
- Stato gap: **SOTTO IL FRATTALE**
- Trend gap: **SOL e sotto il percorso ancorato ma sta recuperando**

Soglie operative del grafico:

- entro **±5%**: percorso vicino;
- tra **±5% e ±12%**: deviazione gestibile;
- oltre **±12%**: frattale non abbastanza aderente per conferma operativa;
- oltre **±18%**: disallineamento marcato.

## Ultimi giorni del confronto ancorato

|   Giorno | Data SOL   | Data BTC eq.   | SOL reale   | Percorso ancorato   | Gap firmato   | Fase                |
|---------:|:-----------|:---------------|:------------|:--------------------|:--------------|:--------------------|
| 66 | 2026-08-11 | 2023-01-26 | 76,20 $ | 90,73 $ | -16,02% | da inizio programma |
| 67 | 2026-08-12 | 2023-01-27 | 75,53 $ | 90,91 $ | -16,93% | da inizio programma |
| 68 | 2026-08-13 | 2023-01-28 | 76,18 $ | 90,72 $ | -16,03% | da inizio programma |
| 69 | 2026-08-14 | 2023-01-29 | 75,33 $ | 93,65 $ | -19,57% | da inizio programma |
| 70 | 2026-08-15 | 2023-01-30 | 75,27 $ | 89,97 $ | -16,34% | da inizio programma |
| 71 | 2026-08-16 | 2023-01-31 | 74,54 $ | 91,15 $ | -18,22% | da inizio programma |
| 72 | 2026-08-17 | 2023-02-01 | 75,94 $ | 93,45 $ | -18,74% | da inizio programma |
| 73 | 2026-08-18 | 2023-02-02 | 77,03 $ | 92,46 $ | -16,69% | da inizio programma |
| 74 | 2026-08-19 | 2023-02-03 | 77,03 $ | 92,37 $ | -16,61% | da inizio programma |
| 75 | 2026-08-20 | 2023-02-04 | 84,87 $ | 91,91 $ | -7,66% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-08-27 | 86,15 $ | 79,56 $ | 78,76 $ / 84,87 $ | no | n/a | n/a | n/a |
| 14g | 2026-09-03 | 97,07 $ | 89,63 $ | 78,76 $ / 89,63 $ | no | n/a | n/a | n/a |
| 21g | 2026-09-10 | 91,29 $ | 84,30 $ | 78,76 $ / 90,32 $ | no | n/a | n/a | n/a |
| 28g | 2026-09-17 | 88,06 $ | 81,31 $ | 78,76 $ / 90,32 $ | no | n/a | n/a | n/a |
| 35g | 2026-09-24 | 81,28 $ | 75,05 $ | 73,43 $ / 90,32 $ | no | n/a | n/a | n/a |
| 42g | 2026-10-01 | 106,22 $ | 98,09 $ | 73,43 $ / 99,76 $ | no | n/a | n/a | n/a |
| 49g | 2026-10-08 | 108,31 $ | 100,01 $ | 73,43 $ / 103,07 $ | no | n/a | n/a | n/a |
| 56g | 2026-10-15 | 111,92 $ | 103,35 $ | 73,43 $ / 103,59 $ | no | n/a | n/a | n/a |
| 63g | 2026-10-22 | 110,09 $ | 101,66 $ | 73,43 $ / 103,59 $ | no | n/a | n/a | n/a |
| 70g | 2026-10-29 | 119,43 $ | 110,28 $ | 73,43 $ / 110,89 $ | no | n/a | n/a | n/a |
| 77g | 2026-11-05 | 109,58 $ | 101,19 $ | 73,43 $ / 110,89 $ | no | n/a | n/a | n/a |
| 84g | 2026-11-12 | 115,22 $ | 106,39 $ | 73,43 $ / 110,89 $ | no | n/a | n/a | n/a |
| 91g | 2026-11-19 | 113,86 $ | 105,14 $ | 73,43 $ / 110,89 $ | no | n/a | n/a | n/a |
| 98g | 2026-11-26 | 105,51 $ | 97,43 $ | 73,43 $ / 110,89 $ | no | n/a | n/a | n/a |
| 105g | 2026-12-03 | 106,87 $ | 98,68 $ | 73,43 $ / 110,89 $ | no | n/a | n/a | n/a |
| 112g | 2026-12-10 | 105,84 $ | 97,73 $ | 73,43 $ / 110,89 $ | no | n/a | n/a | n/a |
| 119g | 2026-12-17 | 106,66 $ | 98,49 $ | 73,43 $ / 110,89 $ | no | n/a | n/a | n/a |
| 126g | 2026-12-24 | 101,83 $ | 94,03 $ | 73,43 $ / 110,89 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 35 | 45,71% | 6,86% | 13,98% |
| 14g | 30 | 40,00% | 14,78% | 13,40% |
| 21g | 23 | 26,09% | 24,05% | 15,34% |
| 28g | 16 | 37,50% | 28,31% | 16,25% |
| 35g | 9 | 33,33% | 28,45% | 16,26% |
| 42g | 2 | 100,00% | 21,39% | n/a |
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
