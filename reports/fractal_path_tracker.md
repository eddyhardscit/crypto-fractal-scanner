<!-- FRACTAL_PATH_TRACKER_START -->
# Tracking percorso frattale SOL/BTC

Generato: 2026-07-20 05:14 UTC

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-07-20**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-01-04**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **75,92 $**
- Verdetto principale: **ANALOGIA DEBOLE / SCENARIO SECONDARIO**
- Somiglianza strutturale: **+64,38%**
- Aderenza live principale: **+63,49%**
- Errore medio live principale: **18,26%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE SOLO DI CONTESTO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **44**
- Osservazioni inclusive dal bottom: **45**
- Osservazioni da inizio programma/scanner: **18**
- Errore assoluto medio dal bottom: **10,92%**
- Errore assoluto medio da inizio programma: **18,26%**
- Gap firmato medio ultimi 7 giorni: **+15,81%**
- Errore assoluto medio ultimi 7 giorni: **15,81%**
- Gap ultimo giorno: **+14,29%**
- Stato aderenza: **STACCATO / MOLTO IN ANTICIPO**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **+14,29%**
- Gap firmato medio 7g: **+15,81%**
- Errore assoluto medio 7g: **15,81%**
- Variazione recente gap: **-0,25%**
- Stato gap: **IN DEVIAZIONE SOPRA IL FRATTALE**
- Trend gap: **SOL resta sopra il percorso ancorato con distacco quasi stabile**

Soglie operative del grafico:

- entro **±5%**: percorso vicino;
- tra **±5% e ±12%**: deviazione gestibile;
- oltre **±12%**: frattale non abbastanza aderente per conferma operativa;
- oltre **±18%**: disallineamento marcato.

## Ultimi giorni del confronto ancorato

|   Giorno | Data SOL   | Data BTC eq.   | SOL reale   | Percorso ancorato   | Gap firmato   | Fase                |
|---------:|:-----------|:---------------|:------------|:--------------------|:--------------|:--------------------|
| 35 | 2026-07-11 | 2022-12-26 | 76,82 $ | 66,65 $ | +15,26% | da inizio programma |
| 36 | 2026-07-12 | 2022-12-27 | 76,87 $ | 65,85 $ | +16,74% | da inizio programma |
| 37 | 2026-07-13 | 2022-12-28 | 74,86 $ | 65,20 $ | +14,81% | da inizio programma |
| 38 | 2026-07-14 | 2022-12-29 | 77,76 $ | 65,56 $ | +18,62% | da inizio programma |
| 39 | 2026-07-15 | 2022-12-30 | 77,26 $ | 65,40 $ | +18,14% | da inizio programma |
| 40 | 2026-07-16 | 2022-12-31 | 75,27 $ | 65,18 $ | +15,48% | da inizio programma |
| 41 | 2026-07-17 | 2023-01-01 | 75,01 $ | 65,49 $ | +14,54% | da inizio programma |
| 42 | 2026-07-18 | 2023-01-02 | 75,46 $ | 65,74 $ | +14,79% | da inizio programma |
| 43 | 2026-07-19 | 2023-01-03 | 75,46 $ | 65,71 $ | +14,85% | da inizio programma |
| 44 | 2026-07-20 | 2023-01-04 | 75,92 $ | 66,43 $ | +14,29% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-07-27 | 70,65 $ | 80,74 $ | 75,80 $ / 80,74 $ | no | n/a | n/a | n/a |
| 14g | 2026-08-03 | 81,50 $ | 93,14 $ | 75,80 $ / 95,31 $ | no | n/a | n/a | n/a |
| 21g | 2026-08-10 | 91,07 $ | 104,08 $ | 75,80 $ / 104,08 $ | no | n/a | n/a | n/a |
| 28g | 2026-08-17 | 93,45 $ | 106,81 $ | 75,80 $ / 107,04 $ | no | n/a | n/a | n/a |
| 35g | 2026-08-24 | 90,36 $ | 103,28 $ | 75,80 $ / 107,04 $ | no | n/a | n/a | n/a |
| 42g | 2026-08-31 | 95,75 $ | 109,44 $ | 75,80 $ / 109,44 $ | no | n/a | n/a | n/a |
| 49g | 2026-09-07 | 95,29 $ | 108,90 $ | 75,80 $ / 111,78 $ | no | n/a | n/a | n/a |
| 56g | 2026-09-14 | 93,15 $ | 106,46 $ | 75,80 $ / 111,78 $ | no | n/a | n/a | n/a |
| 63g | 2026-09-21 | 85,55 $ | 97,78 $ | 75,80 $ / 111,78 $ | no | n/a | n/a | n/a |
| 70g | 2026-09-28 | 96,02 $ | 109,74 $ | 75,80 $ / 111,78 $ | no | n/a | n/a | n/a |
| 77g | 2026-10-05 | 107,57 $ | 122,94 $ | 75,80 $ / 126,85 $ | no | n/a | n/a | n/a |
| 84g | 2026-10-12 | 111,67 $ | 127,63 $ | 75,80 $ / 127,63 $ | no | n/a | n/a | n/a |
| 91g | 2026-10-19 | 111,00 $ | 126,86 $ | 75,80 $ / 128,21 $ | no | n/a | n/a | n/a |
| 98g | 2026-10-26 | 118,72 $ | 135,69 $ | 75,80 $ / 136,12 $ | no | n/a | n/a | n/a |
| 105g | 2026-11-02 | 113,54 $ | 129,76 $ | 75,80 $ / 137,25 $ | no | n/a | n/a | n/a |
| 112g | 2026-11-09 | 111,96 $ | 127,96 $ | 75,80 $ / 137,25 $ | no | n/a | n/a | n/a |
| 119g | 2026-11-16 | 114,26 $ | 130,59 $ | 75,80 $ / 137,25 $ | no | n/a | n/a | n/a |
| 126g | 2026-11-23 | 108,81 $ | 124,36 $ | 75,80 $ / 137,25 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 6 | 16,67% | 1,57% | 14,62% |
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
