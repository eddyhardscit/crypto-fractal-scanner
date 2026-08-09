<!-- FRACTAL_PATH_TRACKER_START -->
# Tracking percorso frattale SOL/BTC

Generato: 2026-08-09 05:16 UTC

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-08-09**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-01-24**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **75,95 $**
- Verdetto principale: **ANALOGIA DEBOLE / SCENARIO SECONDARIO**
- Somiglianza strutturale: **+55,91%**
- Aderenza live principale: **+69,51%**
- Errore medio live principale: **15,25%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE SOLO DI CONTESTO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **64**
- Osservazioni inclusive dal bottom: **65**
- Osservazioni da inizio programma/scanner: **38**
- Errore assoluto medio dal bottom: **11,42%**
- Errore assoluto medio da inizio programma: **15,25%**
- Gap firmato medio ultimi 7 giorni: **-15,49%**
- Errore assoluto medio ultimi 7 giorni: **15,49%**
- Gap ultimo giorno: **-14,83%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **-14,83%**
- Gap firmato medio 7g: **-15,49%**
- Errore assoluto medio 7g: **15,49%**
- Variazione recente gap: **+4,29%**
- Stato gap: **IN DEVIAZIONE SOTTO IL FRATTALE**
- Trend gap: **SOL e sotto il percorso ancorato ma sta recuperando**

Soglie operative del grafico:

- entro **±5%**: percorso vicino;
- tra **±5% e ±12%**: deviazione gestibile;
- oltre **±12%**: frattale non abbastanza aderente per conferma operativa;
- oltre **±18%**: disallineamento marcato.

## Ultimi giorni del confronto ancorato

|   Giorno | Data SOL   | Data BTC eq.   | SOL reale   | Percorso ancorato   | Gap firmato   | Fase                |
|---------:|:-----------|:---------------|:------------|:--------------------|:--------------|:--------------------|
| 55 | 2026-07-31 | 2023-01-15 | 72,79 $ | 82,25 $ | -11,51% | da inizio programma |
| 56 | 2026-08-01 | 2023-01-16 | 71,87 $ | 83,39 $ | -13,82% | da inizio programma |
| 57 | 2026-08-02 | 2023-01-17 | 73,45 $ | 83,36 $ | -11,89% | da inizio programma |
| 58 | 2026-08-03 | 2023-01-18 | 73,47 $ | 81,50 $ | -9,85% | da inizio programma |
| 59 | 2026-08-04 | 2023-01-19 | 73,72 $ | 83,07 $ | -11,25% | da inizio programma |
| 60 | 2026-08-05 | 2023-01-20 | 73,96 $ | 89,33 $ | -17,20% | da inizio programma |
| 61 | 2026-08-06 | 2023-01-21 | 72,58 $ | 89,73 $ | -19,11% | da inizio programma |
| 62 | 2026-08-07 | 2023-01-22 | 73,64 $ | 89,50 $ | -17,72% | da inizio programma |
| 63 | 2026-08-08 | 2023-01-23 | 73,64 $ | 90,34 $ | -18,49% | da inizio programma |
| 64 | 2026-08-09 | 2023-01-24 | 75,95 $ | 89,17 $ | -14,83% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-08-16 | 91,15 $ | 77,64 $ | 75,95 $ / 79,77 $ | no | n/a | n/a | n/a |
| 14g | 2026-08-23 | 91,64 $ | 78,06 $ | 75,95 $ / 79,77 $ | no | n/a | n/a | n/a |
| 21g | 2026-08-30 | 87,53 $ | 74,56 $ | 72,64 $ / 79,77 $ | no | n/a | n/a | n/a |
| 28g | 2026-09-06 | 96,26 $ | 81,99 $ | 72,64 $ / 83,31 $ | no | n/a | n/a | n/a |
| 35g | 2026-09-13 | 91,18 $ | 77,66 $ | 72,64 $ / 83,31 $ | no | n/a | n/a | n/a |
| 42g | 2026-09-20 | 87,53 $ | 74,55 $ | 72,64 $ / 83,31 $ | no | n/a | n/a | n/a |
| 49g | 2026-09-27 | 97,48 $ | 83,03 $ | 67,73 $ / 83,31 $ | no | n/a | n/a | n/a |
| 56g | 2026-10-04 | 110,99 $ | 94,54 $ | 67,73 $ / 94,54 $ | no | n/a | n/a | n/a |
| 63g | 2026-10-11 | 107,42 $ | 91,49 $ | 67,73 $ / 95,07 $ | no | n/a | n/a | n/a |
| 70g | 2026-10-18 | 110,96 $ | 94,51 $ | 67,73 $ / 95,55 $ | no | n/a | n/a | n/a |
| 77g | 2026-10-25 | 119,10 $ | 101,44 $ | 67,73 $ / 101,44 $ | no | n/a | n/a | n/a |
| 84g | 2026-11-01 | 119,74 $ | 101,99 $ | 67,73 $ / 102,29 $ | no | n/a | n/a | n/a |
| 91g | 2026-11-08 | 111,51 $ | 94,98 $ | 67,73 $ / 102,29 $ | no | n/a | n/a | n/a |
| 98g | 2026-11-15 | 112,98 $ | 96,23 $ | 67,73 $ / 102,29 $ | no | n/a | n/a | n/a |
| 105g | 2026-11-22 | 108,95 $ | 92,80 $ | 67,73 $ / 102,29 $ | no | n/a | n/a | n/a |
| 112g | 2026-11-29 | 106,50 $ | 90,71 $ | 67,73 $ / 102,29 $ | no | n/a | n/a | n/a |
| 119g | 2026-12-06 | 107,25 $ | 91,35 $ | 67,73 $ / 102,29 $ | no | n/a | n/a | n/a |
| 126g | 2026-12-13 | 109,13 $ | 92,95 $ | 67,73 $ / 102,29 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 26 | 38,46% | 8,42% | 12,88% |
| 14g | 19 | 10,53% | 17,97% | 11,68% |
| 21g | 12 | 0,00% | 25,96% | 14,57% |
| 28g | 5 | 20,00% | 29,86% | 17,01% |
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
