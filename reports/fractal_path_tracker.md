<!-- FRACTAL_PATH_TRACKER_START -->
# Tracking percorso frattale SOL/BTC

Generato: 2026-09-13 05:32 UTC

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-09-13**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-02-28**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **101,86 $**
- Verdetto principale: **ANALOGIA DEBOLE / SCENARIO SECONDARIO**
- Somiglianza strutturale: **+70,17%**
- Aderenza live principale: **+72,50%**
- Errore medio live principale: **13,75%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE SOLO DI CONTESTO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **99**
- Osservazioni inclusive dal bottom: **100**
- Osservazioni da inizio programma/scanner: **73**
- Errore assoluto medio dal bottom: **11,66%**
- Errore assoluto medio da inizio programma: **13,75%**
- Gap firmato medio ultimi 7 giorni: **+10,05%**
- Errore assoluto medio ultimi 7 giorni: **10,05%**
- Gap ultimo giorno: **+11,71%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **+11,71%**
- Gap firmato medio 7g: **+10,05%**
- Errore assoluto medio 7g: **10,05%**
- Variazione recente gap: **+3,61%**
- Stato gap: **SOPRA IL FRATTALE**
- Trend gap: **SOL sta aumentando il distacco sopra il percorso ancorato**

Soglie operative del grafico:

- entro **±5%**: percorso vicino;
- tra **±5% e ±12%**: deviazione gestibile;
- oltre **±12%**: frattale non abbastanza aderente per conferma operativa;
- oltre **±18%**: disallineamento marcato.

## Ultimi giorni del confronto ancorato

|   Giorno | Data SOL   | Data BTC eq.   | SOL reale   | Percorso ancorato   | Gap firmato   | Fase                |
|---------:|:-----------|:---------------|:------------|:--------------------|:--------------|:--------------------|
| 90 | 2026-09-04 | 2023-02-19 | 101,95 $ | 95,83 $ | +6,38% | da inizio programma |
| 91 | 2026-09-05 | 2023-02-20 | 103,19 $ | 97,81 $ | +5,50% | da inizio programma |
| 92 | 2026-09-06 | 2023-02-21 | 106,45 $ | 96,26 $ | +10,58% | da inizio programma |
| 93 | 2026-09-07 | 2023-02-22 | 103,87 $ | 95,29 $ | +9,01% | da inizio programma |
| 94 | 2026-09-08 | 2023-02-23 | 103,33 $ | 94,33 $ | +9,53% | da inizio programma |
| 95 | 2026-09-09 | 2023-02-24 | 101,61 $ | 91,38 $ | +11,19% | da inizio programma |
| 96 | 2026-09-10 | 2023-02-25 | 98,69 $ | 91,29 $ | +8,10% | da inizio programma |
| 97 | 2026-09-11 | 2023-02-26 | 102,40 $ | 92,81 $ | +10,33% | da inizio programma |
| 98 | 2026-09-12 | 2023-02-27 | 102,40 $ | 92,66 $ | +10,51% | da inizio programma |
| 99 | 2026-09-13 | 2023-02-28 | 101,86 $ | 91,18 $ | +11,71% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-09-20 | 87,53 $ | 97,78 $ | 97,78 $ / 104,06 $ | no | n/a | n/a | n/a |
| 14g | 2026-09-27 | 97,48 $ | 108,90 $ | 88,83 $ / 108,90 $ | no | n/a | n/a | n/a |
| 21g | 2026-10-04 | 110,99 $ | 123,99 $ | 88,83 $ / 123,99 $ | no | n/a | n/a | n/a |
| 28g | 2026-10-11 | 107,42 $ | 119,99 $ | 88,83 $ / 124,68 $ | no | n/a | n/a | n/a |
| 35g | 2026-10-18 | 110,96 $ | 123,95 $ | 88,83 $ / 125,32 $ | no | n/a | n/a | n/a |
| 42g | 2026-10-25 | 119,10 $ | 133,05 $ | 88,83 $ / 133,05 $ | no | n/a | n/a | n/a |
| 49g | 2026-11-01 | 119,74 $ | 133,76 $ | 88,83 $ / 134,15 $ | no | n/a | n/a | n/a |
| 56g | 2026-11-08 | 111,51 $ | 124,57 $ | 88,83 $ / 134,15 $ | no | n/a | n/a | n/a |
| 63g | 2026-11-15 | 112,98 $ | 126,21 $ | 88,83 $ / 134,15 $ | no | n/a | n/a | n/a |
| 70g | 2026-11-22 | 108,95 $ | 121,71 $ | 88,83 $ / 134,15 $ | no | n/a | n/a | n/a |
| 77g | 2026-11-29 | 106,50 $ | 118,97 $ | 88,83 $ / 134,15 $ | no | n/a | n/a | n/a |
| 84g | 2026-12-06 | 107,25 $ | 119,81 $ | 88,83 $ / 134,15 $ | no | n/a | n/a | n/a |
| 91g | 2026-12-13 | 109,13 $ | 121,90 $ | 88,83 $ / 134,15 $ | no | n/a | n/a | n/a |
| 98g | 2026-12-20 | 107,30 $ | 119,86 $ | 88,83 $ / 134,15 $ | no | n/a | n/a | n/a |
| 105g | 2026-12-27 | 102,10 $ | 114,06 $ | 88,83 $ / 134,15 $ | no | n/a | n/a | n/a |
| 112g | 2027-01-03 | 111,59 $ | 124,66 $ | 88,83 $ / 134,15 $ | no | n/a | n/a | n/a |
| 119g | 2027-01-10 | 120,89 $ | 135,04 $ | 88,83 $ / 135,08 $ | no | n/a | n/a | n/a |
| 126g | 2027-01-17 | 121,24 $ | 135,44 $ | 88,83 $ / 137,10 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 59 | 38,98% | 10,48% | 12,66% |
| 14g | 52 | 25,00% | 17,47% | 11,53% |
| 21g | 45 | 13,33% | 26,14% | 13,00% |
| 28g | 38 | 28,95% | 26,37% | 12,67% |
| 35g | 33 | 39,39% | 19,32% | 11,67% |
| 42g | 26 | 76,92% | 10,59% | 10,83% |
| 49g | 19 | 100,00% | 5,61% | 10,55% |
| 56g | 12 | 100,00% | 6,43% | 9,28% |
| 63g | 5 | 100,00% | 6,29% | 10,85% |
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
