<!-- FRACTAL_PATH_TRACKER_START -->
# Tracking percorso frattale SOL/BTC

Generato: 2026-07-18 05:14 UTC

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-07-18**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-01-02**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **74,93 $**
- Verdetto principale: **ANALOGIA DEBOLE / SCENARIO SECONDARIO**
- Somiglianza strutturale: **+64,35%**
- Aderenza live principale: **+62,62%**
- Errore medio live principale: **18,69%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE SOLO DI CONTESTO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **42**
- Osservazioni inclusive dal bottom: **43**
- Osservazioni da inizio programma/scanner: **16**
- Errore assoluto medio dal bottom: **10,74%**
- Errore assoluto medio da inizio programma: **18,69%**
- Gap firmato medio ultimi 7 giorni: **+16,10%**
- Errore assoluto medio ultimi 7 giorni: **16,10%**
- Gap ultimo giorno: **+13,98%**
- Stato aderenza: **STACCATO / MOLTO IN ANTICIPO**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **+13,98%**
- Gap firmato medio 7g: **+16,10%**
- Errore assoluto medio 7g: **16,10%**
- Variazione recente gap: **-4,16%**
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
| 33 | 2026-07-09 | 2022-12-24 | 78,05 $ | 66,37 $ | +17,60% | da inizio programma |
| 34 | 2026-07-10 | 2022-12-25 | 78,07 $ | 66,34 $ | +17,67% | da inizio programma |
| 35 | 2026-07-11 | 2022-12-26 | 76,82 $ | 66,65 $ | +15,26% | da inizio programma |
| 36 | 2026-07-12 | 2022-12-27 | 76,87 $ | 65,85 $ | +16,74% | da inizio programma |
| 37 | 2026-07-13 | 2022-12-28 | 74,86 $ | 65,20 $ | +14,81% | da inizio programma |
| 38 | 2026-07-14 | 2022-12-29 | 77,76 $ | 65,56 $ | +18,62% | da inizio programma |
| 39 | 2026-07-15 | 2022-12-30 | 77,26 $ | 65,40 $ | +18,14% | da inizio programma |
| 40 | 2026-07-16 | 2022-12-31 | 75,27 $ | 65,18 $ | +15,48% | da inizio programma |
| 41 | 2026-07-17 | 2023-01-01 | 75,27 $ | 65,49 $ | +14,94% | da inizio programma |
| 42 | 2026-07-18 | 2023-01-02 | 74,93 $ | 65,74 $ | +13,98% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-07-25 | 67,74 $ | 77,21 $ | 74,89 $ / 77,21 $ | no | n/a | n/a | n/a |
| 14g | 2026-08-01 | 83,39 $ | 95,05 $ | 74,89 $ / 95,05 $ | no | n/a | n/a | n/a |
| 21g | 2026-08-08 | 90,34 $ | 102,97 $ | 74,89 $ / 102,97 $ | no | n/a | n/a | n/a |
| 28g | 2026-08-15 | 89,97 $ | 102,55 $ | 74,89 $ / 106,75 $ | no | n/a | n/a | n/a |
| 35g | 2026-08-22 | 89,66 $ | 102,19 $ | 74,89 $ / 106,75 $ | no | n/a | n/a | n/a |
| 42g | 2026-08-29 | 85,91 $ | 97,92 $ | 74,89 $ / 106,75 $ | no | n/a | n/a | n/a |
| 49g | 2026-09-05 | 97,81 $ | 111,48 $ | 74,89 $ / 111,48 $ | no | n/a | n/a | n/a |
| 56g | 2026-09-12 | 92,66 $ | 105,62 $ | 74,89 $ / 111,48 $ | no | n/a | n/a | n/a |
| 63g | 2026-09-19 | 88,36 $ | 100,71 $ | 74,89 $ / 111,48 $ | no | n/a | n/a | n/a |
| 70g | 2026-09-26 | 95,32 $ | 108,65 $ | 74,89 $ / 111,48 $ | no | n/a | n/a | n/a |
| 77g | 2026-10-03 | 109,38 $ | 124,67 $ | 74,89 $ / 125,89 $ | no | n/a | n/a | n/a |
| 84g | 2026-10-10 | 106,91 $ | 121,86 $ | 74,89 $ / 127,22 $ | no | n/a | n/a | n/a |
| 91g | 2026-10-17 | 109,47 $ | 124,78 $ | 74,89 $ / 127,87 $ | no | n/a | n/a | n/a |
| 98g | 2026-10-24 | 116,81 $ | 133,14 $ | 74,89 $ / 133,14 $ | no | n/a | n/a | n/a |
| 105g | 2026-10-31 | 115,99 $ | 132,21 $ | 74,89 $ / 136,88 $ | no | n/a | n/a | n/a |
| 112g | 2026-11-07 | 108,43 $ | 123,59 $ | 74,89 $ / 136,88 $ | no | n/a | n/a | n/a |
| 119g | 2026-11-14 | 110,66 $ | 126,13 $ | 74,89 $ / 136,88 $ | no | n/a | n/a | n/a |
| 126g | 2026-11-21 | 109,09 $ | 124,35 $ | 74,89 $ / 136,88 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 4 | 0,00% | 2,06% | 14,46% |
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
