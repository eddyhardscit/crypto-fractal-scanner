<!-- FRACTAL_PATH_TRACKER_START -->
# Tracking percorso frattale SOL/BTC

Generato: 2026-08-17 05:32 UTC

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-08-17**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-02-01**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **75,42 $**
- Verdetto principale: **ANALOGIA DEBOLE / SCENARIO SECONDARIO**
- Somiglianza strutturale: **+57,75%**
- Aderenza live principale: **+68,93%**
- Errore medio live principale: **15,54%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE SOLO DI CONTESTO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **72**
- Osservazioni inclusive dal bottom: **73**
- Osservazioni da inizio programma/scanner: **46**
- Errore assoluto medio dal bottom: **12,02%**
- Errore assoluto medio da inizio programma: **15,54%**
- Gap firmato medio ultimi 7 giorni: **-17,37%**
- Errore assoluto medio ultimi 7 giorni: **17,37%**
- Gap ultimo giorno: **-19,30%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **-19,30%**
- Gap firmato medio 7g: **-17,37%**
- Errore assoluto medio 7g: **17,37%**
- Variazione recente gap: **+0,27%**
- Stato gap: **DISALLINEATO SOTTO IL FRATTALE**
- Trend gap: **SOL e vicino al percorso ancorato**

Soglie operative del grafico:

- entro **±5%**: percorso vicino;
- tra **±5% e ±12%**: deviazione gestibile;
- oltre **±12%**: frattale non abbastanza aderente per conferma operativa;
- oltre **±18%**: disallineamento marcato.

## Ultimi giorni del confronto ancorato

|   Giorno | Data SOL   | Data BTC eq.   | SOL reale   | Percorso ancorato   | Gap firmato   | Fase                |
|---------:|:-----------|:---------------|:------------|:--------------------|:--------------|:--------------------|
| 63 | 2026-08-08 | 2023-01-23 | 75,97 $ | 90,34 $ | -15,91% | da inizio programma |
| 64 | 2026-08-09 | 2023-01-24 | 76,21 $ | 89,17 $ | -14,53% | da inizio programma |
| 65 | 2026-08-10 | 2023-01-25 | 75,95 $ | 91,07 $ | -16,60% | da inizio programma |
| 66 | 2026-08-11 | 2023-01-26 | 76,20 $ | 90,73 $ | -16,02% | da inizio programma |
| 67 | 2026-08-12 | 2023-01-27 | 75,53 $ | 90,91 $ | -16,93% | da inizio programma |
| 68 | 2026-08-13 | 2023-01-28 | 76,18 $ | 90,72 $ | -16,03% | da inizio programma |
| 69 | 2026-08-14 | 2023-01-29 | 75,33 $ | 93,65 $ | -19,57% | da inizio programma |
| 70 | 2026-08-15 | 2023-01-30 | 75,27 $ | 89,97 $ | -16,34% | da inizio programma |
| 71 | 2026-08-16 | 2023-01-31 | 75,27 $ | 91,15 $ | -17,42% | da inizio programma |
| 72 | 2026-08-17 | 2023-02-01 | 75,42 $ | 93,45 $ | -19,30% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-08-24 | 90,36 $ | 72,93 $ | 72,36 $ / 75,42 $ | no | n/a | n/a | n/a |
| 14g | 2026-08-31 | 95,75 $ | 77,28 $ | 68,83 $ / 77,28 $ | no | n/a | n/a | n/a |
| 21g | 2026-09-07 | 95,29 $ | 76,90 $ | 68,83 $ / 78,93 $ | no | n/a | n/a | n/a |
| 28g | 2026-09-14 | 93,15 $ | 75,17 $ | 68,83 $ / 78,93 $ | no | n/a | n/a | n/a |
| 35g | 2026-09-21 | 85,55 $ | 69,04 $ | 68,83 $ / 78,93 $ | no | n/a | n/a | n/a |
| 42g | 2026-09-28 | 96,02 $ | 77,49 $ | 64,18 $ / 78,93 $ | no | n/a | n/a | n/a |
| 49g | 2026-10-05 | 107,57 $ | 86,81 $ | 64,18 $ / 89,57 $ | no | n/a | n/a | n/a |
| 56g | 2026-10-12 | 111,67 $ | 90,12 $ | 64,18 $ / 90,12 $ | no | n/a | n/a | n/a |
| 63g | 2026-10-19 | 111,00 $ | 89,58 $ | 64,18 $ / 90,54 $ | no | n/a | n/a | n/a |
| 70g | 2026-10-26 | 118,72 $ | 95,81 $ | 64,18 $ / 96,12 $ | no | n/a | n/a | n/a |
| 77g | 2026-11-02 | 113,54 $ | 91,63 $ | 64,18 $ / 96,92 $ | no | n/a | n/a | n/a |
| 84g | 2026-11-09 | 111,96 $ | 90,36 $ | 64,18 $ / 96,92 $ | no | n/a | n/a | n/a |
| 91g | 2026-11-16 | 114,26 $ | 92,21 $ | 64,18 $ / 96,92 $ | no | n/a | n/a | n/a |
| 98g | 2026-11-23 | 108,81 $ | 87,81 $ | 64,18 $ / 96,92 $ | no | n/a | n/a | n/a |
| 105g | 2026-11-30 | 107,93 $ | 87,10 $ | 64,18 $ / 96,92 $ | no | n/a | n/a | n/a |
| 112g | 2026-12-07 | 103,74 $ | 83,72 $ | 64,18 $ / 96,92 $ | no | n/a | n/a | n/a |
| 119g | 2026-12-14 | 107,22 $ | 86,53 $ | 64,18 $ / 96,92 $ | no | n/a | n/a | n/a |
| 126g | 2026-12-21 | 103,78 $ | 83,76 $ | 64,18 $ / 96,92 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 34 | 41,18% | 7,04% | 13,89% |
| 14g | 27 | 37,04% | 15,72% | 13,36% |
| 21g | 20 | 25,00% | 26,13% | 15,61% |
| 28g | 13 | 30,77% | 28,85% | 16,94% |
| 35g | 6 | 16,67% | 29,29% | 18,16% |
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
