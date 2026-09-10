<!-- FRACTAL_PATH_TRACKER_START -->
# Tracking percorso frattale SOL/BTC

Generato: 2026-09-10 05:32 UTC

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-09-10**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-02-25**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **102,02 $**
- Verdetto principale: **ANALOGIA DEBOLE / SCENARIO SECONDARIO**
- Somiglianza strutturale: **+69,32%**
- Aderenza live principale: **+72,09%**
- Errore medio live principale: **13,95%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE SOLO DI CONTESTO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **96**
- Osservazioni inclusive dal bottom: **97**
- Osservazioni da inizio programma/scanner: **70**
- Errore assoluto medio dal bottom: **11,75%**
- Errore assoluto medio da inizio programma: **13,95%**
- Gap firmato medio ultimi 7 giorni: **+9,40%**
- Errore assoluto medio ultimi 7 giorni: **9,40%**
- Gap ultimo giorno: **+11,75%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **+11,75%**
- Gap firmato medio 7g: **+9,40%**
- Errore assoluto medio 7g: **9,40%**
- Variazione recente gap: **+2,74%**
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
| 87 | 2026-09-01 | 2023-02-16 | 99,99 $ | 93,06 $ | +7,45% | da inizio programma |
| 88 | 2026-09-02 | 2023-02-17 | 100,39 $ | 96,77 $ | +3,74% | da inizio programma |
| 89 | 2026-09-03 | 2023-02-18 | 103,98 $ | 97,07 $ | +7,12% | da inizio programma |
| 90 | 2026-09-04 | 2023-02-19 | 101,95 $ | 95,83 $ | +6,38% | da inizio programma |
| 91 | 2026-09-05 | 2023-02-20 | 103,19 $ | 97,81 $ | +5,50% | da inizio programma |
| 92 | 2026-09-06 | 2023-02-21 | 106,45 $ | 96,26 $ | +10,58% | da inizio programma |
| 93 | 2026-09-07 | 2023-02-22 | 103,87 $ | 95,29 $ | +9,01% | da inizio programma |
| 94 | 2026-09-08 | 2023-02-23 | 103,33 $ | 94,33 $ | +9,53% | da inizio programma |
| 95 | 2026-09-09 | 2023-02-24 | 103,33 $ | 91,38 $ | +13,07% | da inizio programma |
| 96 | 2026-09-10 | 2023-02-25 | 102,02 $ | 91,29 $ | +11,75% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-09-17 | 88,06 $ | 98,40 $ | 98,40 $ / 104,09 $ | no | n/a | n/a | n/a |
| 14g | 2026-09-24 | 81,28 $ | 90,83 $ | 88,87 $ / 104,09 $ | no | n/a | n/a | n/a |
| 21g | 2026-10-01 | 106,22 $ | 118,71 $ | 88,87 $ / 120,72 $ | no | n/a | n/a | n/a |
| 28g | 2026-10-08 | 108,31 $ | 121,03 $ | 88,87 $ / 124,73 $ | no | n/a | n/a | n/a |
| 35g | 2026-10-15 | 111,92 $ | 125,07 $ | 88,87 $ / 125,36 $ | no | n/a | n/a | n/a |
| 42g | 2026-10-22 | 110,09 $ | 123,03 $ | 88,87 $ / 125,36 $ | no | n/a | n/a | n/a |
| 49g | 2026-10-29 | 119,43 $ | 133,46 $ | 88,87 $ / 134,20 $ | no | n/a | n/a | n/a |
| 56g | 2026-11-05 | 109,58 $ | 122,46 $ | 88,87 $ / 134,20 $ | no | n/a | n/a | n/a |
| 63g | 2026-11-12 | 115,22 $ | 128,75 $ | 88,87 $ / 134,20 $ | no | n/a | n/a | n/a |
| 70g | 2026-11-19 | 113,86 $ | 127,24 $ | 88,87 $ / 134,20 $ | no | n/a | n/a | n/a |
| 77g | 2026-11-26 | 105,51 $ | 117,91 $ | 88,87 $ / 134,20 $ | no | n/a | n/a | n/a |
| 84g | 2026-12-03 | 106,87 $ | 119,43 $ | 88,87 $ / 134,20 $ | no | n/a | n/a | n/a |
| 91g | 2026-12-10 | 105,84 $ | 118,28 $ | 88,87 $ / 134,20 $ | no | n/a | n/a | n/a |
| 98g | 2026-12-17 | 106,66 $ | 119,19 $ | 88,87 $ / 134,20 $ | no | n/a | n/a | n/a |
| 105g | 2026-12-24 | 101,83 $ | 113,80 $ | 88,87 $ / 134,20 $ | no | n/a | n/a | n/a |
| 112g | 2026-12-31 | 104,43 $ | 116,70 $ | 88,87 $ / 134,20 $ | no | n/a | n/a | n/a |
| 119g | 2027-01-07 | 120,34 $ | 134,48 $ | 88,87 $ / 135,12 $ | no | n/a | n/a | n/a |
| 126g | 2027-01-14 | 120,50 $ | 134,66 $ | 88,87 $ / 135,12 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 56 | 35,71% | 10,97% | 12,86% |
| 14g | 49 | 28,57% | 17,90% | 11,69% |
| 21g | 42 | 14,29% | 27,51% | 13,30% |
| 28g | 35 | 31,43% | 25,65% | 12,84% |
| 35g | 30 | 43,33% | 18,11% | 11,95% |
| 42g | 23 | 86,96% | 8,96% | 11,09% |
| 49g | 16 | 100,00% | 6,04% | 10,88% |
| 56g | 9 | 100,00% | 7,01% | 9,40% |
| 63g | 2 | 100,00% | 4,86% | n/a |
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
