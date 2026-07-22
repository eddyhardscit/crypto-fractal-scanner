<!-- FRACTAL_PATH_TRACKER_START -->
# Tracking percorso frattale SOL/BTC

Generato: 2026-07-22 05:14 UTC

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-07-22**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-01-06**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **77,84 $**
- Verdetto principale: **ANALOGIA DEBOLE / SCENARIO SECONDARIO**
- Somiglianza strutturale: **+64,69%**
- Aderenza live principale: **+63,34%**
- Errore medio live principale: **18,33%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE SOLO DI CONTESTO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **46**
- Osservazioni inclusive dal bottom: **47**
- Osservazioni da inizio programma/scanner: **20**
- Errore assoluto medio dal bottom: **11,26%**
- Errore assoluto medio da inizio programma: **18,33%**
- Gap firmato medio ultimi 7 giorni: **+16,00%**
- Errore assoluto medio ultimi 7 giorni: **16,00%**
- Gap ultimo giorno: **+16,57%**
- Stato aderenza: **STACCATO / MOLTO IN ANTICIPO**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **+16,57%**
- Gap firmato medio 7g: **+16,00%**
- Errore assoluto medio 7g: **16,00%**
- Variazione recente gap: **+0,36%**
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
| 37 | 2026-07-13 | 2022-12-28 | 74,86 $ | 65,20 $ | +14,81% | da inizio programma |
| 38 | 2026-07-14 | 2022-12-29 | 77,76 $ | 65,56 $ | +18,62% | da inizio programma |
| 39 | 2026-07-15 | 2022-12-30 | 77,26 $ | 65,40 $ | +18,14% | da inizio programma |
| 40 | 2026-07-16 | 2022-12-31 | 75,27 $ | 65,18 $ | +15,48% | da inizio programma |
| 41 | 2026-07-17 | 2023-01-01 | 75,01 $ | 65,49 $ | +14,54% | da inizio programma |
| 42 | 2026-07-18 | 2023-01-02 | 75,46 $ | 65,74 $ | +14,79% | da inizio programma |
| 43 | 2026-07-19 | 2023-01-03 | 76,36 $ | 65,71 $ | +16,21% | da inizio programma |
| 44 | 2026-07-20 | 2023-01-04 | 77,79 $ | 66,43 $ | +17,11% | da inizio programma |
| 45 | 2026-07-21 | 2023-01-05 | 77,79 $ | 66,32 $ | +17,29% | da inizio programma |
| 46 | 2026-07-22 | 2023-01-06 | 77,84 $ | 66,78 $ | +16,57% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-07-29 | 78,43 $ | 91,42 $ | 77,84 $ / 91,42 $ | no | n/a | n/a | n/a |
| 14g | 2026-08-05 | 89,33 $ | 104,13 $ | 77,84 $ / 104,13 $ | no | n/a | n/a | n/a |
| 21g | 2026-08-12 | 90,91 $ | 105,97 $ | 77,84 $ / 106,15 $ | no | n/a | n/a | n/a |
| 28g | 2026-08-19 | 92,37 $ | 107,67 $ | 77,84 $ / 109,17 $ | no | n/a | n/a | n/a |
| 35g | 2026-08-26 | 85,29 $ | 99,42 $ | 77,84 $ / 109,17 $ | no | n/a | n/a | n/a |
| 42g | 2026-09-02 | 96,77 $ | 112,80 $ | 77,84 $ / 112,80 $ | no | n/a | n/a | n/a |
| 49g | 2026-09-09 | 91,38 $ | 106,52 $ | 77,84 $ / 114,01 $ | no | n/a | n/a | n/a |
| 56g | 2026-09-16 | 88,09 $ | 102,68 $ | 77,84 $ / 114,01 $ | no | n/a | n/a | n/a |
| 63g | 2026-09-23 | 79,52 $ | 92,70 $ | 77,84 $ / 114,01 $ | no | n/a | n/a | n/a |
| 70g | 2026-09-30 | 108,03 $ | 125,93 $ | 77,84 $ / 125,93 $ | no | n/a | n/a | n/a |
| 77g | 2026-10-07 | 108,30 $ | 126,24 $ | 77,84 $ / 130,10 $ | no | n/a | n/a | n/a |
| 84g | 2026-10-14 | 112,18 $ | 130,77 $ | 77,84 $ / 130,77 $ | no | n/a | n/a | n/a |
| 91g | 2026-10-21 | 110,01 $ | 128,23 $ | 77,84 $ / 130,77 $ | no | n/a | n/a | n/a |
| 98g | 2026-10-28 | 120,09 $ | 139,98 $ | 77,84 $ / 139,98 $ | no | n/a | n/a | n/a |
| 105g | 2026-11-04 | 107,45 $ | 125,25 $ | 77,84 $ / 139,98 $ | no | n/a | n/a | n/a |
| 112g | 2026-11-11 | 115,58 $ | 134,72 $ | 77,84 $ / 139,98 $ | no | n/a | n/a | n/a |
| 119g | 2026-11-18 | 116,34 $ | 135,62 $ | 77,84 $ / 139,98 $ | no | n/a | n/a | n/a |
| 126g | 2026-11-25 | 105,59 $ | 123,08 $ | 77,84 $ / 139,98 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 8 | 37,50% | 1,53% | 16,08% |
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
