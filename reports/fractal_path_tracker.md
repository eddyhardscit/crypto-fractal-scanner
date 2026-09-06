<!-- FRACTAL_PATH_TRACKER_START -->
# Tracking percorso frattale SOL/BTC

Generato: 2026-09-06 05:32 UTC

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-09-06**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-02-21**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **106,09 $**
- Verdetto principale: **ANALOGIA DEBOLE / SCENARIO SECONDARIO**
- Somiglianza strutturale: **+67,81%**
- Aderenza live principale: **+71,77%**
- Errore medio live principale: **14,12%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE SOLO DI CONTESTO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **92**
- Osservazioni inclusive dal bottom: **93**
- Osservazioni da inizio programma/scanner: **66**
- Errore assoluto medio dal bottom: **11,77%**
- Errore assoluto medio da inizio programma: **14,12%**
- Gap firmato medio ultimi 7 giorni: **+6,67%**
- Errore assoluto medio ultimi 7 giorni: **6,67%**
- Gap ultimo giorno: **+10,21%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **+10,21%**
- Gap firmato medio 7g: **+6,67%**
- Errore assoluto medio 7g: **6,67%**
- Variazione recente gap: **+3,09%**
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
| 83 | 2026-08-28 | 2023-02-12 | 104,13 $ | 85,83 $ | +21,32% | da inizio programma |
| 84 | 2026-08-29 | 2023-02-13 | 105,65 $ | 85,91 $ | +22,98% | da inizio programma |
| 85 | 2026-08-30 | 2023-02-14 | 101,88 $ | 87,53 $ | +16,39% | da inizio programma |
| 86 | 2026-08-31 | 2023-02-15 | 103,00 $ | 95,75 $ | +7,56% | da inizio programma |
| 87 | 2026-09-01 | 2023-02-16 | 99,99 $ | 93,06 $ | +7,45% | da inizio programma |
| 88 | 2026-09-02 | 2023-02-17 | 100,39 $ | 96,77 $ | +3,74% | da inizio programma |
| 89 | 2026-09-03 | 2023-02-18 | 103,98 $ | 97,07 $ | +7,12% | da inizio programma |
| 90 | 2026-09-04 | 2023-02-19 | 101,95 $ | 95,83 $ | +6,38% | da inizio programma |
| 91 | 2026-09-05 | 2023-02-20 | 101,95 $ | 97,81 $ | +4,23% | da inizio programma |
| 92 | 2026-09-06 | 2023-02-21 | 106,09 $ | 96,26 $ | +10,21% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-09-13 | 91,18 $ | 100,49 $ | 100,49 $ / 106,09 $ | no | n/a | n/a | n/a |
| 14g | 2026-09-20 | 87,53 $ | 96,47 $ | 96,47 $ / 106,09 $ | no | n/a | n/a | n/a |
| 21g | 2026-09-27 | 97,48 $ | 107,43 $ | 87,64 $ / 107,43 $ | no | n/a | n/a | n/a |
| 28g | 2026-10-04 | 110,99 $ | 122,32 $ | 87,64 $ / 122,32 $ | no | n/a | n/a | n/a |
| 35g | 2026-10-11 | 107,42 $ | 118,38 $ | 87,64 $ / 123,01 $ | no | n/a | n/a | n/a |
| 42g | 2026-10-18 | 110,96 $ | 122,29 $ | 87,64 $ / 123,64 $ | no | n/a | n/a | n/a |
| 49g | 2026-10-25 | 119,10 $ | 131,26 $ | 87,64 $ / 131,26 $ | no | n/a | n/a | n/a |
| 56g | 2026-11-01 | 119,74 $ | 131,97 $ | 87,64 $ / 132,35 $ | no | n/a | n/a | n/a |
| 63g | 2026-11-08 | 111,51 $ | 122,90 $ | 87,64 $ / 132,35 $ | no | n/a | n/a | n/a |
| 70g | 2026-11-15 | 112,98 $ | 124,52 $ | 87,64 $ / 132,35 $ | no | n/a | n/a | n/a |
| 77g | 2026-11-22 | 108,95 $ | 120,08 $ | 87,64 $ / 132,35 $ | no | n/a | n/a | n/a |
| 84g | 2026-11-29 | 106,50 $ | 117,38 $ | 87,64 $ / 132,35 $ | no | n/a | n/a | n/a |
| 91g | 2026-12-06 | 107,25 $ | 118,20 $ | 87,64 $ / 132,35 $ | no | n/a | n/a | n/a |
| 98g | 2026-12-13 | 109,13 $ | 120,27 $ | 87,64 $ / 132,35 $ | no | n/a | n/a | n/a |
| 105g | 2026-12-20 | 107,30 $ | 118,26 $ | 87,64 $ / 132,35 $ | no | n/a | n/a | n/a |
| 112g | 2026-12-27 | 102,10 $ | 112,53 $ | 87,64 $ / 132,35 $ | no | n/a | n/a | n/a |
| 119g | 2027-01-03 | 111,59 $ | 122,98 $ | 87,64 $ / 132,35 $ | no | n/a | n/a | n/a |
| 126g | 2027-01-10 | 120,89 $ | 133,23 $ | 87,64 $ / 133,26 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 52 | 36,54% | 11,43% | 12,99% |
| 14g | 45 | 26,67% | 19,07% | 11,73% |
| 21g | 38 | 15,79% | 27,05% | 13,53% |
| 28g | 33 | 33,33% | 25,31% | 13,01% |
| 35g | 26 | 50,00% | 16,32% | 12,07% |
| 42g | 19 | 100,00% | 7,81% | 11,05% |
| 49g | 12 | 100,00% | 6,68% | 10,74% |
| 56g | 5 | 100,00% | 8,63% | 6,94% |
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
