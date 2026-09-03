<!-- FRACTAL_PATH_TRACKER_START -->
# Tracking percorso frattale SOL/BTC

Generato: 2026-09-03 05:32 UTC

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-09-03**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-02-18**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **99,93 $**
- Verdetto principale: **ANALOGIA DEBOLE / SCENARIO SECONDARIO**
- Somiglianza strutturale: **+66,25%**
- Aderenza live principale: **+71,23%**
- Errore medio live principale: **14,39%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE SOLO DI CONTESTO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **89**
- Osservazioni inclusive dal bottom: **90**
- Osservazioni da inizio programma/scanner: **63**
- Errore assoluto medio dal bottom: **11,88%**
- Errore assoluto medio da inizio programma: **14,39%**
- Gap firmato medio ultimi 7 giorni: **+11,71%**
- Errore assoluto medio ultimi 7 giorni: **11,71%**
- Gap ultimo giorno: **+2,95%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **+2,95%**
- Gap firmato medio 7g: **+11,71%**
- Errore assoluto medio 7g: **11,71%**
- Variazione recente gap: **-4,62%**
- Stato gap: **VICINO AL FRATTALE**
- Trend gap: **SOL resta sopra il percorso ancorato, ma sta riducendo il distacco**

Soglie operative del grafico:

- entro **±5%**: percorso vicino;
- tra **±5% e ±12%**: deviazione gestibile;
- oltre **±12%**: frattale non abbastanza aderente per conferma operativa;
- oltre **±18%**: disallineamento marcato.

## Ultimi giorni del confronto ancorato

|   Giorno | Data SOL   | Data BTC eq.   | SOL reale   | Percorso ancorato   | Gap firmato   | Fase                |
|---------:|:-----------|:---------------|:------------|:--------------------|:--------------|:--------------------|
| 80 | 2026-08-25 | 2023-02-09 | 96,60 $ | 85,95 $ | +12,39% | da inizio programma |
| 81 | 2026-08-26 | 2023-02-10 | 102,17 $ | 85,29 $ | +19,79% | da inizio programma |
| 82 | 2026-08-27 | 2023-02-11 | 109,21 $ | 86,15 $ | +26,76% | da inizio programma |
| 83 | 2026-08-28 | 2023-02-12 | 104,13 $ | 85,83 $ | +21,32% | da inizio programma |
| 84 | 2026-08-29 | 2023-02-13 | 105,65 $ | 85,91 $ | +22,98% | da inizio programma |
| 85 | 2026-08-30 | 2023-02-14 | 101,88 $ | 87,53 $ | +16,39% | da inizio programma |
| 86 | 2026-08-31 | 2023-02-15 | 103,00 $ | 95,75 $ | +7,56% | da inizio programma |
| 87 | 2026-09-01 | 2023-02-16 | 99,99 $ | 93,06 $ | +7,45% | da inizio programma |
| 88 | 2026-09-02 | 2023-02-17 | 99,99 $ | 96,77 $ | +3,32% | da inizio programma |
| 89 | 2026-09-03 | 2023-02-18 | 99,93 $ | 97,07 $ | +2,95% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-09-10 | 91,29 $ | 93,99 $ | 93,99 $ / 100,69 $ | no | n/a | n/a | n/a |
| 14g | 2026-09-17 | 88,06 $ | 90,65 $ | 90,65 $ / 100,69 $ | no | n/a | n/a | n/a |
| 21g | 2026-09-24 | 81,28 $ | 83,67 $ | 81,87 $ / 100,69 $ | no | n/a | n/a | n/a |
| 28g | 2026-10-01 | 106,22 $ | 109,36 $ | 81,87 $ / 111,21 $ | no | n/a | n/a | n/a |
| 35g | 2026-10-08 | 108,31 $ | 111,50 $ | 81,87 $ / 114,91 $ | no | n/a | n/a | n/a |
| 42g | 2026-10-15 | 111,92 $ | 115,22 $ | 81,87 $ / 115,49 $ | no | n/a | n/a | n/a |
| 49g | 2026-10-22 | 110,09 $ | 113,34 $ | 81,87 $ / 115,49 $ | no | n/a | n/a | n/a |
| 56g | 2026-10-29 | 119,43 $ | 122,95 $ | 81,87 $ / 123,63 $ | no | n/a | n/a | n/a |
| 63g | 2026-11-05 | 109,58 $ | 112,81 $ | 81,87 $ / 123,63 $ | no | n/a | n/a | n/a |
| 70g | 2026-11-12 | 115,22 $ | 118,61 $ | 81,87 $ / 123,63 $ | no | n/a | n/a | n/a |
| 77g | 2026-11-19 | 113,86 $ | 117,22 $ | 81,87 $ / 123,63 $ | no | n/a | n/a | n/a |
| 84g | 2026-11-26 | 105,51 $ | 108,62 $ | 81,87 $ / 123,63 $ | no | n/a | n/a | n/a |
| 91g | 2026-12-03 | 106,87 $ | 110,02 $ | 81,87 $ / 123,63 $ | no | n/a | n/a | n/a |
| 98g | 2026-12-10 | 105,84 $ | 108,96 $ | 81,87 $ / 123,63 $ | no | n/a | n/a | n/a |
| 105g | 2026-12-17 | 106,66 $ | 109,80 $ | 81,87 $ / 123,63 $ | no | n/a | n/a | n/a |
| 112g | 2026-12-24 | 101,83 $ | 104,84 $ | 81,87 $ / 123,63 $ | no | n/a | n/a | n/a |
| 119g | 2026-12-31 | 104,43 $ | 107,51 $ | 81,87 $ / 123,63 $ | no | n/a | n/a | n/a |
| 126g | 2027-01-07 | 120,34 $ | 123,89 $ | 81,87 $ / 124,48 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 49 | 34,69% | 11,47% | 13,28% |
| 14g | 42 | 26,19% | 19,93% | 11,97% |
| 21g | 35 | 17,14% | 26,80% | 14,13% |
| 28g | 30 | 36,67% | 24,77% | 13,50% |
| 35g | 23 | 56,52% | 15,52% | 12,58% |
| 42g | 16 | 100,00% | 8,82% | 11,60% |
| 49g | 9 | 100,00% | 7,16% | 11,71% |
| 56g | 2 | 100,00% | 12,35% | n/a |
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
