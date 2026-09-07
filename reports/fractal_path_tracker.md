<!-- FRACTAL_PATH_TRACKER_START -->
# Tracking percorso frattale SOL/BTC

Generato: 2026-09-07 05:32 UTC

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-09-07**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-02-22**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **105,54 $**
- Verdetto principale: **ANALOGIA DEBOLE / SCENARIO SECONDARIO**
- Somiglianza strutturale: **+68,14%**
- Aderenza live principale: **+71,92%**
- Errore medio live principale: **14,04%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE SOLO DI CONTESTO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **93**
- Osservazioni inclusive dal bottom: **94**
- Osservazioni da inizio programma/scanner: **67**
- Errore assoluto medio dal bottom: **11,74%**
- Errore assoluto medio da inizio programma: **14,04%**
- Gap firmato medio ultimi 7 giorni: **+6,88%**
- Errore assoluto medio ultimi 7 giorni: **6,88%**
- Gap ultimo giorno: **+10,76%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **+10,76%**
- Gap firmato medio 7g: **+6,88%**
- Errore assoluto medio 7g: **6,88%**
- Variazione recente gap: **+4,38%**
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
| 84 | 2026-08-29 | 2023-02-13 | 105,65 $ | 85,91 $ | +22,98% | da inizio programma |
| 85 | 2026-08-30 | 2023-02-14 | 101,88 $ | 87,53 $ | +16,39% | da inizio programma |
| 86 | 2026-08-31 | 2023-02-15 | 103,00 $ | 95,75 $ | +7,56% | da inizio programma |
| 87 | 2026-09-01 | 2023-02-16 | 99,99 $ | 93,06 $ | +7,45% | da inizio programma |
| 88 | 2026-09-02 | 2023-02-17 | 100,39 $ | 96,77 $ | +3,74% | da inizio programma |
| 89 | 2026-09-03 | 2023-02-18 | 103,98 $ | 97,07 $ | +7,12% | da inizio programma |
| 90 | 2026-09-04 | 2023-02-19 | 101,95 $ | 95,83 $ | +6,38% | da inizio programma |
| 91 | 2026-09-05 | 2023-02-20 | 103,19 $ | 97,81 $ | +5,50% | da inizio programma |
| 92 | 2026-09-06 | 2023-02-21 | 103,19 $ | 96,26 $ | +7,20% | da inizio programma |
| 93 | 2026-09-07 | 2023-02-22 | 105,54 $ | 95,29 $ | +10,76% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-09-14 | 93,15 $ | 103,17 $ | 101,00 $ / 105,54 $ | no | n/a | n/a | n/a |
| 14g | 2026-09-21 | 85,55 $ | 94,76 $ | 94,76 $ / 105,54 $ | no | n/a | n/a | n/a |
| 21g | 2026-09-28 | 96,02 $ | 106,36 $ | 88,08 $ / 107,97 $ | no | n/a | n/a | n/a |
| 28g | 2026-10-05 | 107,57 $ | 119,15 $ | 88,08 $ / 122,94 $ | no | n/a | n/a | n/a |
| 35g | 2026-10-12 | 111,67 $ | 123,69 $ | 88,08 $ / 123,69 $ | no | n/a | n/a | n/a |
| 42g | 2026-10-19 | 111,00 $ | 122,95 $ | 88,08 $ / 124,26 $ | no | n/a | n/a | n/a |
| 49g | 2026-10-26 | 118,72 $ | 131,50 $ | 88,08 $ / 131,92 $ | no | n/a | n/a | n/a |
| 56g | 2026-11-02 | 113,54 $ | 125,76 $ | 88,08 $ / 133,01 $ | no | n/a | n/a | n/a |
| 63g | 2026-11-09 | 111,96 $ | 124,01 $ | 88,08 $ / 133,01 $ | no | n/a | n/a | n/a |
| 70g | 2026-11-16 | 114,26 $ | 126,56 $ | 88,08 $ / 133,01 $ | no | n/a | n/a | n/a |
| 77g | 2026-11-23 | 108,81 $ | 120,52 $ | 88,08 $ / 133,01 $ | no | n/a | n/a | n/a |
| 84g | 2026-11-30 | 107,93 $ | 119,55 $ | 88,08 $ / 133,01 $ | no | n/a | n/a | n/a |
| 91g | 2026-12-07 | 103,74 $ | 114,90 $ | 88,08 $ / 133,01 $ | no | n/a | n/a | n/a |
| 98g | 2026-12-14 | 107,22 $ | 118,76 $ | 88,08 $ / 133,01 $ | no | n/a | n/a | n/a |
| 105g | 2026-12-21 | 103,78 $ | 114,95 $ | 88,08 $ / 133,01 $ | no | n/a | n/a | n/a |
| 112g | 2026-12-28 | 98,97 $ | 109,62 $ | 88,08 $ / 133,01 $ | no | n/a | n/a | n/a |
| 119g | 2027-01-04 | 118,28 $ | 131,01 $ | 88,08 $ / 133,01 $ | no | n/a | n/a | n/a |
| 126g | 2027-01-11 | 118,52 $ | 131,27 $ | 88,08 $ / 133,93 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 53 | 33,96% | 11,31% | 12,91% |
| 14g | 46 | 23,91% | 18,75% | 11,67% |
| 21g | 39 | 15,38% | 27,25% | 13,41% |
| 28g | 34 | 32,35% | 25,45% | 12,89% |
| 35g | 27 | 48,15% | 16,52% | 11,95% |
| 42g | 20 | 100,00% | 7,54% | 10,94% |
| 49g | 13 | 100,00% | 6,52% | 10,58% |
| 56g | 6 | 100,00% | 8,03% | 7,46% |
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
