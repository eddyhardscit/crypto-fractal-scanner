<!-- FRACTAL_PATH_TRACKER_START -->
# Tracking percorso frattale SOL/BTC

Generato: 2026-07-17 00:32 UTC

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-07-17**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-01-01**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **75,28 $**
- Verdetto principale: **ANALOGIA DEBOLE / SCENARIO SECONDARIO**
- Somiglianza strutturale: **+64,09%**
- Aderenza live principale: **+61,58%**
- Errore medio live principale: **19,21%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE SOLO DI CONTESTO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **41**
- Osservazioni inclusive dal bottom: **42**
- Osservazioni da inizio programma/scanner: **15**
- Errore assoluto medio dal bottom: **10,73%**
- Errore assoluto medio da inizio programma: **19,21%**
- Gap firmato medio ultimi 7 giorni: **+16,72%**
- Errore assoluto medio ultimi 7 giorni: **16,72%**
- Gap ultimo giorno: **+14,95%**
- Stato aderenza: **STACCATO / MOLTO IN ANTICIPO**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **+14,95%**
- Gap firmato medio 7g: **+16,72%**
- Errore assoluto medio 7g: **16,72%**
- Variazione recente gap: **-3,67%**
- Stato gap: **IN DEVIAZIONE SOPRA IL FRATTALE**
- Trend gap: **SOL resta sopra il percorso ancorato, ma sta riducendo il distacco**

Soglie operative del grafico:

- entro **±5%**: percorso vicino;
- tra **±5% e ±12%**: deviazione gestibile;
- oltre **±12%**: frattale non abbastanza aderente per conferma operativa;
- oltre **±18%**: disallineamento marcato.

## Ultimi giorni del confronto ancorato

|   Giorno | Data SOL   | Data BTC eq.   | SOL reale   | Percorso ancorato   | Gap firmato   | Fase                |
|---------:|:-----------|:---------------|:------------|:--------------------|:--------------|:--------------------|
| 32 | 2026-07-08 | 2022-12-23 | 77,79 $ | 66,17 $ | +17,56% | da inizio programma |
| 33 | 2026-07-09 | 2022-12-24 | 78,05 $ | 66,37 $ | +17,60% | da inizio programma |
| 34 | 2026-07-10 | 2022-12-25 | 78,07 $ | 66,34 $ | +17,67% | da inizio programma |
| 35 | 2026-07-11 | 2022-12-26 | 76,82 $ | 66,65 $ | +15,26% | da inizio programma |
| 36 | 2026-07-12 | 2022-12-27 | 76,87 $ | 65,85 $ | +16,74% | da inizio programma |
| 37 | 2026-07-13 | 2022-12-28 | 74,86 $ | 65,20 $ | +14,81% | da inizio programma |
| 38 | 2026-07-14 | 2022-12-29 | 77,76 $ | 65,56 $ | +18,62% | da inizio programma |
| 39 | 2026-07-15 | 2022-12-30 | 77,26 $ | 65,40 $ | +18,14% | da inizio programma |
| 40 | 2026-07-16 | 2022-12-31 | 77,26 $ | 65,18 $ | +18,53% | da inizio programma |
| 41 | 2026-07-17 | 2023-01-01 | 75,28 $ | 65,49 $ | +14,95% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-07-24 | 67,33 $ | 77,39 $ | 75,28 $ / 77,39 $ | no | n/a | n/a | n/a |
| 14g | 2026-07-31 | 82,25 $ | 94,55 $ | 75,28 $ / 94,98 $ | no | n/a | n/a | n/a |
| 21g | 2026-08-07 | 89,50 $ | 102,88 $ | 75,28 $ / 103,14 $ | no | n/a | n/a | n/a |
| 28g | 2026-08-14 | 93,65 $ | 107,65 $ | 75,28 $ / 107,65 $ | no | n/a | n/a | n/a |
| 35g | 2026-08-21 | 90,43 $ | 103,95 $ | 75,28 $ / 107,65 $ | no | n/a | n/a | n/a |
| 42g | 2026-08-28 | 85,83 $ | 98,66 $ | 75,28 $ / 107,65 $ | no | n/a | n/a | n/a |
| 49g | 2026-09-04 | 95,83 $ | 110,16 $ | 75,28 $ / 111,58 $ | no | n/a | n/a | n/a |
| 56g | 2026-09-11 | 92,81 $ | 106,69 $ | 75,28 $ / 112,43 $ | no | n/a | n/a | n/a |
| 63g | 2026-09-18 | 88,38 $ | 101,59 $ | 75,28 $ / 112,43 $ | no | n/a | n/a | n/a |
| 70g | 2026-09-25 | 87,31 $ | 100,36 $ | 75,28 $ / 112,43 $ | no | n/a | n/a | n/a |
| 77g | 2026-10-02 | 110,45 $ | 126,96 $ | 75,28 $ / 126,96 $ | no | n/a | n/a | n/a |
| 84g | 2026-10-09 | 110,28 $ | 126,76 $ | 75,28 $ / 128,30 $ | no | n/a | n/a | n/a |
| 91g | 2026-10-16 | 111,08 $ | 127,69 $ | 75,28 $ / 128,95 $ | no | n/a | n/a | n/a |
| 98g | 2026-10-23 | 111,61 $ | 128,29 $ | 75,28 $ / 128,95 $ | no | n/a | n/a | n/a |
| 105g | 2026-10-30 | 119,42 $ | 137,27 $ | 75,28 $ / 138,04 $ | no | n/a | n/a | n/a |
| 112g | 2026-11-06 | 108,69 $ | 124,94 $ | 75,28 $ / 138,04 $ | no | n/a | n/a | n/a |
| 119g | 2026-11-13 | 115,30 $ | 132,53 $ | 75,28 $ / 138,04 $ | no | n/a | n/a | n/a |
| 126g | 2026-11-20 | 112,09 $ | 128,85 $ | 75,28 $ / 138,04 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 3 | 66,67% | 1,35% | 14,95% |
| 14g | 0 | n/a | n/a | n/a |
| 21g | 0 | n/a | n/a | n/a |
| 28g | 0 | n/a | n/a | n/a |
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
