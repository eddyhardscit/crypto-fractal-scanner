<!-- FRACTAL_PATH_TRACKER_START -->
# Tracking percorso frattale SOL/BTC

Generato: 2026-09-08 05:32 UTC

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-09-08**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-02-23**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **103,29 $**
- Verdetto principale: **ANALOGIA DEBOLE / SCENARIO SECONDARIO**
- Somiglianza strutturale: **+68,39%**
- Aderenza live principale: **+71,92%**
- Errore medio live principale: **14,04%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE SOLO DI CONTESTO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **94**
- Osservazioni inclusive dal bottom: **95**
- Osservazioni da inizio programma/scanner: **68**
- Errore assoluto medio dal bottom: **11,76%**
- Errore assoluto medio da inizio programma: **14,04%**
- Gap firmato medio ultimi 7 giorni: **+7,79%**
- Errore assoluto medio ultimi 7 giorni: **7,79%**
- Gap ultimo giorno: **+9,49%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **+9,49%**
- Gap firmato medio 7g: **+7,79%**
- Errore assoluto medio 7g: **7,79%**
- Variazione recente gap: **+3,99%**
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
| 85 | 2026-08-30 | 2023-02-14 | 101,88 $ | 87,53 $ | +16,39% | da inizio programma |
| 86 | 2026-08-31 | 2023-02-15 | 103,00 $ | 95,75 $ | +7,56% | da inizio programma |
| 87 | 2026-09-01 | 2023-02-16 | 99,99 $ | 93,06 $ | +7,45% | da inizio programma |
| 88 | 2026-09-02 | 2023-02-17 | 100,39 $ | 96,77 $ | +3,74% | da inizio programma |
| 89 | 2026-09-03 | 2023-02-18 | 103,98 $ | 97,07 $ | +7,12% | da inizio programma |
| 90 | 2026-09-04 | 2023-02-19 | 101,95 $ | 95,83 $ | +6,38% | da inizio programma |
| 91 | 2026-09-05 | 2023-02-20 | 103,19 $ | 97,81 $ | +5,50% | da inizio programma |
| 92 | 2026-09-06 | 2023-02-21 | 106,45 $ | 96,26 $ | +10,58% | da inizio programma |
| 93 | 2026-09-07 | 2023-02-22 | 106,45 $ | 95,29 $ | +11,71% | da inizio programma |
| 94 | 2026-09-08 | 2023-02-23 | 103,29 $ | 94,33 $ | +9,49% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-09-15 | 92,48 $ | 101,25 $ | 99,84 $ / 103,29 $ | no | n/a | n/a | n/a |
| 14g | 2026-09-22 | 80,21 $ | 87,83 $ | 87,83 $ / 103,29 $ | no | n/a | n/a | n/a |
| 21g | 2026-09-29 | 98,69 $ | 108,06 $ | 87,07 $ / 108,06 $ | no | n/a | n/a | n/a |
| 28g | 2026-10-06 | 111,61 $ | 122,21 $ | 87,07 $ / 122,21 $ | no | n/a | n/a | n/a |
| 35g | 2026-10-13 | 110,43 $ | 120,91 $ | 87,07 $ / 122,27 $ | no | n/a | n/a | n/a |
| 42g | 2026-10-20 | 110,47 $ | 120,96 $ | 87,07 $ / 122,83 $ | no | n/a | n/a | n/a |
| 49g | 2026-10-27 | 119,75 $ | 131,12 $ | 87,07 $ / 131,12 $ | no | n/a | n/a | n/a |
| 56g | 2026-11-03 | 111,27 $ | 121,83 $ | 87,07 $ / 131,49 $ | no | n/a | n/a | n/a |
| 63g | 2026-11-10 | 116,10 $ | 127,13 $ | 87,07 $ / 131,49 $ | no | n/a | n/a | n/a |
| 70g | 2026-11-17 | 113,64 $ | 124,43 $ | 87,07 $ / 131,49 $ | no | n/a | n/a | n/a |
| 77g | 2026-11-24 | 106,36 $ | 116,46 $ | 87,07 $ / 131,49 $ | no | n/a | n/a | n/a |
| 84g | 2026-12-01 | 105,70 $ | 115,73 $ | 87,07 $ / 131,49 $ | no | n/a | n/a | n/a |
| 91g | 2026-12-08 | 104,30 $ | 114,20 $ | 87,07 $ / 131,49 $ | no | n/a | n/a | n/a |
| 98g | 2026-12-15 | 105,65 $ | 115,68 $ | 87,07 $ / 131,49 $ | no | n/a | n/a | n/a |
| 105g | 2026-12-22 | 104,42 $ | 114,33 $ | 87,07 $ / 131,49 $ | no | n/a | n/a | n/a |
| 112g | 2026-12-29 | 100,75 $ | 110,32 $ | 87,07 $ / 131,49 $ | no | n/a | n/a | n/a |
| 119g | 2027-01-05 | 117,83 $ | 129,02 $ | 87,07 $ / 131,49 $ | no | n/a | n/a | n/a |
| 126g | 2027-01-12 | 119,93 $ | 131,32 $ | 87,07 $ / 132,40 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 54 | 35,19% | 11,10% | 12,93% |
| 14g | 47 | 25,53% | 18,61% | 11,72% |
| 21g | 40 | 15,00% | 27,55% | 13,42% |
| 28g | 35 | 31,43% | 25,74% | 12,92% |
| 35g | 28 | 46,43% | 16,94% | 12,02% |
| 42g | 21 | 90,48% | 7,71% | 11,09% |
| 49g | 14 | 100,00% | 6,30% | 10,85% |
| 56g | 7 | 100,00% | 7,35% | 8,73% |
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
