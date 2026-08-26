<!-- FRACTAL_PATH_TRACKER_START -->
# Tracking percorso frattale SOL/BTC

Generato: 2026-08-26 05:32 UTC

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-08-26**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-02-10**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **96,77 $**
- Verdetto principale: **ANALOGIA DEBOLE / SCENARIO SECONDARIO**
- Somiglianza strutturale: **+63,79%**
- Aderenza live principale: **+71,14%**
- Errore medio live principale: **14,43%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE SOLO DI CONTESTO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **81**
- Osservazioni inclusive dal bottom: **82**
- Osservazioni da inizio programma/scanner: **55**
- Errore assoluto medio dal bottom: **11,66%**
- Errore assoluto medio da inizio programma: **14,43%**
- Gap firmato medio ultimi 7 giorni: **+6,43%**
- Errore assoluto medio ultimi 7 giorni: **7,76%**
- Gap ultimo giorno: **+13,46%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **+13,46%**
- Gap firmato medio 7g: **+6,43%**
- Errore assoluto medio 7g: **7,76%**
- Variazione recente gap: **+9,32%**
- Stato gap: **IN DEVIAZIONE SOPRA IL FRATTALE**
- Trend gap: **SOL sta aumentando il distacco sopra il percorso ancorato**

Soglie operative del grafico:

- entro **±5%**: percorso vicino;
- tra **±5% e ±12%**: deviazione gestibile;
- oltre **±12%**: frattale non abbastanza aderente per conferma operativa;
- oltre **±18%**: disallineamento marcato.

## Ultimi giorni del confronto ancorato

|   Giorno | Data SOL   | Data BTC eq.   | SOL reale   | Percorso ancorato   | Gap firmato   | Fase                |
|---------:|:-----------|:---------------|:------------|:--------------------|:--------------|:--------------------|
| 72 | 2026-08-17 | 2023-02-01 | 75,94 $ | 93,45 $ | -18,74% | da inizio programma |
| 73 | 2026-08-18 | 2023-02-02 | 77,03 $ | 92,46 $ | -16,69% | da inizio programma |
| 74 | 2026-08-19 | 2023-02-03 | 85,37 $ | 92,37 $ | -7,58% | da inizio programma |
| 75 | 2026-08-20 | 2023-02-04 | 87,64 $ | 91,91 $ | -4,65% | da inizio programma |
| 76 | 2026-08-21 | 2023-02-05 | 93,65 $ | 90,43 $ | +3,57% | da inizio programma |
| 77 | 2026-08-22 | 2023-02-06 | 93,91 $ | 89,66 $ | +4,75% | da inizio programma |
| 78 | 2026-08-23 | 2023-02-07 | 95,44 $ | 91,64 $ | +4,15% | da inizio programma |
| 79 | 2026-08-24 | 2023-02-08 | 98,56 $ | 90,36 $ | +9,07% | da inizio programma |
| 80 | 2026-08-25 | 2023-02-09 | 98,56 $ | 85,95 $ | +14,67% | da inizio programma |
| 81 | 2026-08-26 | 2023-02-10 | 96,77 $ | 85,29 $ | +13,46% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-09-02 | 96,77 $ | 109,80 $ | 96,77 $ / 109,80 $ | no | n/a | n/a | n/a |
| 14g | 2026-09-09 | 91,38 $ | 103,68 $ | 96,77 $ / 110,97 $ | no | n/a | n/a | n/a |
| 21g | 2026-09-16 | 88,09 $ | 99,95 $ | 96,77 $ / 110,97 $ | no | n/a | n/a | n/a |
| 28g | 2026-09-23 | 79,52 $ | 90,23 $ | 90,23 $ / 110,97 $ | no | n/a | n/a | n/a |
| 35g | 2026-09-30 | 108,03 $ | 122,57 $ | 90,23 $ / 122,57 $ | no | n/a | n/a | n/a |
| 42g | 2026-10-07 | 108,30 $ | 122,88 $ | 90,23 $ / 126,64 $ | no | n/a | n/a | n/a |
| 49g | 2026-10-14 | 112,18 $ | 127,28 $ | 90,23 $ / 127,28 $ | no | n/a | n/a | n/a |
| 56g | 2026-10-21 | 110,01 $ | 124,81 $ | 90,23 $ / 127,28 $ | no | n/a | n/a | n/a |
| 63g | 2026-10-28 | 120,09 $ | 136,26 $ | 90,23 $ / 136,26 $ | no | n/a | n/a | n/a |
| 70g | 2026-11-04 | 107,45 $ | 121,91 $ | 90,23 $ / 136,26 $ | no | n/a | n/a | n/a |
| 77g | 2026-11-11 | 115,58 $ | 131,14 $ | 90,23 $ / 136,26 $ | no | n/a | n/a | n/a |
| 84g | 2026-11-18 | 116,34 $ | 132,00 $ | 90,23 $ / 136,26 $ | no | n/a | n/a | n/a |
| 91g | 2026-11-25 | 105,59 $ | 119,80 $ | 90,23 $ / 136,26 $ | no | n/a | n/a | n/a |
| 98g | 2026-12-02 | 105,93 $ | 120,19 $ | 90,23 $ / 136,26 $ | no | n/a | n/a | n/a |
| 105g | 2026-12-09 | 105,25 $ | 119,42 $ | 90,23 $ / 136,26 $ | no | n/a | n/a | n/a |
| 112g | 2026-12-16 | 107,34 $ | 121,79 $ | 90,23 $ / 136,26 $ | no | n/a | n/a | n/a |
| 119g | 2026-12-23 | 104,31 $ | 118,35 $ | 90,23 $ / 136,26 $ | no | n/a | n/a | n/a |
| 126g | 2026-12-30 | 103,71 $ | 117,67 $ | 90,23 $ / 136,26 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 41 | 39,02% | 10,52% | 13,11% |
| 14g | 35 | 31,43% | 17,18% | 12,10% |
| 21g | 29 | 20,69% | 23,72% | 13,33% |
| 28g | 22 | 50,00% | 22,64% | 13,26% |
| 35g | 15 | 66,67% | 18,85% | 11,65% |
| 42g | 8 | 100,00% | 10,30% | 8,28% |
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
