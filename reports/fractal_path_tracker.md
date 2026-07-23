<!-- FRACTAL_PATH_TRACKER_START -->
# Tracking percorso frattale SOL/BTC

Generato: 2026-07-23 07:37 UTC

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-07-23**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-01-07**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **77,11 $**
- Verdetto principale: **ANALOGIA DEBOLE / SCENARIO SECONDARIO**
- Somiglianza strutturale: **+64,77%**
- Aderenza live principale: **+63,56%**
- Errore medio live principale: **18,22%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE SOLO DI CONTESTO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **47**
- Osservazioni inclusive dal bottom: **48**
- Osservazioni da inizio programma/scanner: **21**
- Errore assoluto medio dal bottom: **11,36%**
- Errore assoluto medio da inizio programma: **18,22%**
- Gap firmato medio ultimi 7 giorni: **+16,08%**
- Errore assoluto medio ultimi 7 giorni: **16,08%**
- Gap ultimo giorno: **+15,45%**
- Stato aderenza: **STACCATO / MOLTO IN ANTICIPO**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **+15,45%**
- Gap firmato medio 7g: **+16,08%**
- Errore assoluto medio 7g: **16,08%**
- Variazione recente gap: **-1,66%**
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
| 38 | 2026-07-14 | 2022-12-29 | 77,76 $ | 65,56 $ | +18,62% | da inizio programma |
| 39 | 2026-07-15 | 2022-12-30 | 77,26 $ | 65,40 $ | +18,14% | da inizio programma |
| 40 | 2026-07-16 | 2022-12-31 | 75,27 $ | 65,18 $ | +15,48% | da inizio programma |
| 41 | 2026-07-17 | 2023-01-01 | 75,01 $ | 65,49 $ | +14,54% | da inizio programma |
| 42 | 2026-07-18 | 2023-01-02 | 75,46 $ | 65,74 $ | +14,79% | da inizio programma |
| 43 | 2026-07-19 | 2023-01-03 | 76,36 $ | 65,71 $ | +16,21% | da inizio programma |
| 44 | 2026-07-20 | 2023-01-04 | 77,79 $ | 66,43 $ | +17,11% | da inizio programma |
| 45 | 2026-07-21 | 2023-01-05 | 78,11 $ | 66,32 $ | +17,77% | da inizio programma |
| 46 | 2026-07-22 | 2023-01-06 | 77,91 $ | 66,78 $ | +16,66% | da inizio programma |
| 47 | 2026-07-23 | 2023-01-07 | 77,11 $ | 66,79 $ | +15,45% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-07-30 | 82,63 $ | 95,40 $ | 77,11 $ / 95,40 $ | no | n/a | n/a | n/a |
| 14g | 2026-08-06 | 89,73 $ | 103,59 $ | 77,11 $ / 103,59 $ | no | n/a | n/a | n/a |
| 21g | 2026-08-13 | 90,72 $ | 104,74 $ | 77,11 $ / 105,14 $ | no | n/a | n/a | n/a |
| 28g | 2026-08-20 | 91,91 $ | 106,11 $ | 77,11 $ / 108,12 $ | no | n/a | n/a | n/a |
| 35g | 2026-08-27 | 86,15 $ | 99,47 $ | 77,11 $ / 108,12 $ | no | n/a | n/a | n/a |
| 42g | 2026-09-03 | 97,07 $ | 112,07 $ | 77,11 $ / 112,07 $ | no | n/a | n/a | n/a |
| 49g | 2026-09-10 | 91,29 $ | 105,40 $ | 77,11 $ / 112,92 $ | no | n/a | n/a | n/a |
| 56g | 2026-09-17 | 88,06 $ | 101,66 $ | 77,11 $ / 112,92 $ | no | n/a | n/a | n/a |
| 63g | 2026-09-24 | 81,28 $ | 93,83 $ | 77,11 $ / 112,92 $ | no | n/a | n/a | n/a |
| 70g | 2026-10-01 | 106,22 $ | 122,64 $ | 77,11 $ / 124,72 $ | no | n/a | n/a | n/a |
| 77g | 2026-10-08 | 108,31 $ | 125,04 $ | 77,11 $ / 128,86 $ | no | n/a | n/a | n/a |
| 84g | 2026-10-15 | 111,92 $ | 129,21 $ | 77,11 $ / 129,52 $ | no | n/a | n/a | n/a |
| 91g | 2026-10-22 | 110,09 $ | 127,10 $ | 77,11 $ / 129,52 $ | no | n/a | n/a | n/a |
| 98g | 2026-10-29 | 119,43 $ | 137,89 $ | 77,11 $ / 138,65 $ | no | n/a | n/a | n/a |
| 105g | 2026-11-05 | 109,58 $ | 126,51 $ | 77,11 $ / 138,65 $ | no | n/a | n/a | n/a |
| 112g | 2026-11-12 | 115,22 $ | 133,02 $ | 77,11 $ / 138,65 $ | no | n/a | n/a | n/a |
| 119g | 2026-11-19 | 113,86 $ | 131,46 $ | 77,11 $ / 138,65 $ | no | n/a | n/a | n/a |
| 126g | 2026-11-26 | 105,51 $ | 121,81 $ | 77,11 $ / 138,65 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 9 | 44,44% | 1,47% | 16,08% |
| 14g | 2 | 100,00% | 1,71% | n/a |
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
