<!-- FRACTAL_PATH_TRACKER_START -->
# Tracking percorso frattale SOL/BTC

Generato: 2026-09-01 05:32 UTC

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-09-01**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-02-16**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **103,93 $**
- Verdetto principale: **ANALOGIA DEBOLE / SCENARIO SECONDARIO**
- Somiglianza strutturale: **+65,04%**
- Aderenza live principale: **+70,39%**
- Errore medio live principale: **14,80%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE SOLO DI CONTESTO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **87**
- Osservazioni inclusive dal bottom: **88**
- Osservazioni da inizio programma/scanner: **61**
- Errore assoluto medio dal bottom: **12,11%**
- Errore assoluto medio da inizio programma: **14,80%**
- Gap firmato medio ultimi 7 giorni: **+17,90%**
- Errore assoluto medio ultimi 7 giorni: **17,90%**
- Gap ultimo giorno: **+11,68%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **+11,68%**
- Gap firmato medio 7g: **+17,90%**
- Errore assoluto medio 7g: **17,90%**
- Variazione recente gap: **-11,30%**
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
| 78 | 2026-08-23 | 2023-02-07 | 95,44 $ | 91,64 $ | +4,15% | da inizio programma |
| 79 | 2026-08-24 | 2023-02-08 | 98,56 $ | 90,36 $ | +9,07% | da inizio programma |
| 80 | 2026-08-25 | 2023-02-09 | 96,60 $ | 85,95 $ | +12,39% | da inizio programma |
| 81 | 2026-08-26 | 2023-02-10 | 102,17 $ | 85,29 $ | +19,79% | da inizio programma |
| 82 | 2026-08-27 | 2023-02-11 | 109,21 $ | 86,15 $ | +26,76% | da inizio programma |
| 83 | 2026-08-28 | 2023-02-12 | 104,13 $ | 85,83 $ | +21,32% | da inizio programma |
| 84 | 2026-08-29 | 2023-02-13 | 105,65 $ | 85,91 $ | +22,98% | da inizio programma |
| 85 | 2026-08-30 | 2023-02-14 | 101,88 $ | 87,53 $ | +16,39% | da inizio programma |
| 86 | 2026-08-31 | 2023-02-15 | 101,88 $ | 95,75 $ | +6,39% | da inizio programma |
| 87 | 2026-09-01 | 2023-02-16 | 103,93 $ | 93,06 $ | +11,68% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-09-08 | 94,33 $ | 105,36 $ | 103,93 $ / 109,23 $ | no | n/a | n/a | n/a |
| 14g | 2026-09-15 | 92,48 $ | 103,28 $ | 101,84 $ / 109,23 $ | no | n/a | n/a | n/a |
| 21g | 2026-09-22 | 80,21 $ | 89,59 $ | 89,59 $ / 109,23 $ | no | n/a | n/a | n/a |
| 28g | 2026-09-29 | 98,69 $ | 110,22 $ | 88,81 $ / 110,22 $ | no | n/a | n/a | n/a |
| 35g | 2026-10-06 | 111,61 $ | 124,65 $ | 88,81 $ / 124,65 $ | no | n/a | n/a | n/a |
| 42g | 2026-10-13 | 110,43 $ | 123,33 $ | 88,81 $ / 124,72 $ | no | n/a | n/a | n/a |
| 49g | 2026-10-20 | 110,47 $ | 123,38 $ | 88,81 $ / 125,29 $ | no | n/a | n/a | n/a |
| 56g | 2026-10-27 | 119,75 $ | 133,74 $ | 88,81 $ / 133,74 $ | no | n/a | n/a | n/a |
| 63g | 2026-11-03 | 111,27 $ | 124,27 $ | 88,81 $ / 134,12 $ | no | n/a | n/a | n/a |
| 70g | 2026-11-10 | 116,10 $ | 129,67 $ | 88,81 $ / 134,12 $ | no | n/a | n/a | n/a |
| 77g | 2026-11-17 | 113,64 $ | 126,91 $ | 88,81 $ / 134,12 $ | no | n/a | n/a | n/a |
| 84g | 2026-11-24 | 106,36 $ | 118,79 $ | 88,81 $ / 134,12 $ | no | n/a | n/a | n/a |
| 91g | 2026-12-01 | 105,70 $ | 118,05 $ | 88,81 $ / 134,12 $ | no | n/a | n/a | n/a |
| 98g | 2026-12-08 | 104,30 $ | 116,48 $ | 88,81 $ / 134,12 $ | no | n/a | n/a | n/a |
| 105g | 2026-12-15 | 105,65 $ | 117,99 $ | 88,81 $ / 134,12 $ | no | n/a | n/a | n/a |
| 112g | 2026-12-22 | 104,42 $ | 116,62 $ | 88,81 $ / 134,12 $ | no | n/a | n/a | n/a |
| 119g | 2026-12-29 | 100,75 $ | 112,52 $ | 88,81 $ / 134,12 $ | no | n/a | n/a | n/a |
| 126g | 2027-01-05 | 117,83 $ | 131,60 $ | 88,81 $ / 134,12 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 47 | 36,17% | 11,41% | 13,79% |
| 14g | 40 | 27,50% | 20,13% | 12,52% |
| 21g | 35 | 17,14% | 26,90% | 14,22% |
| 28g | 28 | 39,29% | 24,90% | 14,41% |
| 35g | 21 | 61,90% | 16,00% | 13,74% |
| 42g | 14 | 100,00% | 8,32% | 13,27% |
| 49g | 7 | 100,00% | 5,26% | 15,75% |
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
