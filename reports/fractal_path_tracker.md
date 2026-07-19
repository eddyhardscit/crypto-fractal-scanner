<!-- FRACTAL_PATH_TRACKER_START -->
# Tracking percorso frattale SOL/BTC

Generato: 2026-07-19 05:14 UTC

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-07-19**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-01-03**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **76,00 $**
- Verdetto principale: **ANALOGIA DEBOLE / SCENARIO SECONDARIO**
- Somiglianza strutturale: **+64,25%**
- Aderenza live principale: **+63,01%**
- Errore medio live principale: **18,50%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE SOLO DI CONTESTO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **43**
- Osservazioni inclusive dal bottom: **44**
- Osservazioni da inizio programma/scanner: **17**
- Errore assoluto medio dal bottom: **10,84%**
- Errore assoluto medio da inizio programma: **18,50%**
- Gap firmato medio ultimi 7 giorni: **+15,91%**
- Errore assoluto medio ultimi 7 giorni: **15,91%**
- Gap ultimo giorno: **+15,67%**
- Stato aderenza: **STACCATO / MOLTO IN ANTICIPO**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **+15,67%**
- Gap firmato medio 7g: **+15,91%**
- Errore assoluto medio 7g: **15,91%**
- Variazione recente gap: **+0,19%**
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
| 34 | 2026-07-10 | 2022-12-25 | 78,07 $ | 66,34 $ | +17,67% | da inizio programma |
| 35 | 2026-07-11 | 2022-12-26 | 76,82 $ | 66,65 $ | +15,26% | da inizio programma |
| 36 | 2026-07-12 | 2022-12-27 | 76,87 $ | 65,85 $ | +16,74% | da inizio programma |
| 37 | 2026-07-13 | 2022-12-28 | 74,86 $ | 65,20 $ | +14,81% | da inizio programma |
| 38 | 2026-07-14 | 2022-12-29 | 77,76 $ | 65,56 $ | +18,62% | da inizio programma |
| 39 | 2026-07-15 | 2022-12-30 | 77,26 $ | 65,40 $ | +18,14% | da inizio programma |
| 40 | 2026-07-16 | 2022-12-31 | 75,27 $ | 65,18 $ | +15,48% | da inizio programma |
| 41 | 2026-07-17 | 2023-01-01 | 75,01 $ | 65,49 $ | +14,54% | da inizio programma |
| 42 | 2026-07-18 | 2023-01-02 | 75,01 $ | 65,74 $ | +14,10% | da inizio programma |
| 43 | 2026-07-19 | 2023-01-03 | 76,00 $ | 65,71 $ | +15,67% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-07-26 | 68,73 $ | 79,49 $ | 76,00 $ / 79,49 $ | no | n/a | n/a | n/a |
| 14g | 2026-08-02 | 83,36 $ | 96,42 $ | 76,00 $ / 96,46 $ | no | n/a | n/a | n/a |
| 21g | 2026-08-09 | 89,17 $ | 103,14 $ | 76,00 $ / 104,50 $ | no | n/a | n/a | n/a |
| 28g | 2026-08-16 | 91,15 $ | 105,43 $ | 76,00 $ / 108,33 $ | no | n/a | n/a | n/a |
| 35g | 2026-08-23 | 91,64 $ | 106,00 $ | 76,00 $ / 108,33 $ | no | n/a | n/a | n/a |
| 42g | 2026-08-30 | 87,53 $ | 101,25 $ | 76,00 $ / 108,33 $ | no | n/a | n/a | n/a |
| 49g | 2026-09-06 | 96,26 $ | 111,34 $ | 76,00 $ / 113,13 $ | no | n/a | n/a | n/a |
| 56g | 2026-09-13 | 91,18 $ | 105,47 $ | 76,00 $ / 113,13 $ | no | n/a | n/a | n/a |
| 63g | 2026-09-20 | 87,53 $ | 101,24 $ | 76,00 $ / 113,13 $ | no | n/a | n/a | n/a |
| 70g | 2026-09-27 | 97,48 $ | 112,75 $ | 76,00 $ / 113,13 $ | no | n/a | n/a | n/a |
| 77g | 2026-10-04 | 110,99 $ | 128,38 $ | 76,00 $ / 128,38 $ | no | n/a | n/a | n/a |
| 84g | 2026-10-11 | 107,42 $ | 124,24 $ | 76,00 $ / 129,10 $ | no | n/a | n/a | n/a |
| 91g | 2026-10-18 | 110,96 $ | 128,34 $ | 76,00 $ / 129,76 $ | no | n/a | n/a | n/a |
| 98g | 2026-10-25 | 119,10 $ | 137,76 $ | 76,00 $ / 137,76 $ | no | n/a | n/a | n/a |
| 105g | 2026-11-01 | 119,74 $ | 138,50 $ | 76,00 $ / 138,90 $ | no | n/a | n/a | n/a |
| 112g | 2026-11-08 | 111,51 $ | 128,98 $ | 76,00 $ / 138,90 $ | no | n/a | n/a | n/a |
| 119g | 2026-11-15 | 112,98 $ | 130,68 $ | 76,00 $ / 138,90 $ | no | n/a | n/a | n/a |
| 126g | 2026-11-22 | 108,95 $ | 126,02 $ | 76,00 $ / 138,90 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 5 | 20,00% | 1,77% | 14,77% |
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
