<!-- FRACTAL_PATH_TRACKER_START -->
# Tracking percorso frattale SOL/BTC

Generato: 2026-08-22 05:32 UTC

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-08-22**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-02-06**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **93,70 $**
- Verdetto principale: **ANALOGIA DEBOLE / SCENARIO SECONDARIO**
- Somiglianza strutturale: **+61,86%**
- Aderenza live principale: **+70,53%**
- Errore medio live principale: **14,73%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE SOLO DI CONTESTO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **77**
- Osservazioni inclusive dal bottom: **78**
- Osservazioni da inizio programma/scanner: **51**
- Errore assoluto medio dal bottom: **11,72%**
- Errore assoluto medio da inizio programma: **14,73%**
- Gap firmato medio ultimi 7 giorni: **-9,21%**
- Errore assoluto medio ultimi 7 giorni: **10,50%**
- Gap ultimo giorno: **+4,51%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **+4,51%**
- Gap firmato medio 7g: **-9,21%**
- Errore assoluto medio 7g: **10,50%**
- Variazione recente gap: **+12,08%**
- Stato gap: **VICINO AL FRATTALE**
- Trend gap: **SOL sta aumentando il distacco sopra il percorso ancorato**

Soglie operative del grafico:

- entro **±5%**: percorso vicino;
- tra **±5% e ±12%**: deviazione gestibile;
- oltre **±12%**: frattale non abbastanza aderente per conferma operativa;
- oltre **±18%**: disallineamento marcato.

## Ultimi giorni del confronto ancorato

|   Giorno | Data SOL   | Data BTC eq.   | SOL reale   | Percorso ancorato   | Gap firmato   | Fase                |
|---------:|:-----------|:---------------|:------------|:--------------------|:--------------|:--------------------|
| 68 | 2026-08-13 | 2023-01-28 | 76,18 $ | 90,72 $ | -16,03% | da inizio programma |
| 69 | 2026-08-14 | 2023-01-29 | 75,33 $ | 93,65 $ | -19,57% | da inizio programma |
| 70 | 2026-08-15 | 2023-01-30 | 75,27 $ | 89,97 $ | -16,34% | da inizio programma |
| 71 | 2026-08-16 | 2023-01-31 | 74,54 $ | 91,15 $ | -18,22% | da inizio programma |
| 72 | 2026-08-17 | 2023-02-01 | 75,94 $ | 93,45 $ | -18,74% | da inizio programma |
| 73 | 2026-08-18 | 2023-02-02 | 77,03 $ | 92,46 $ | -16,69% | da inizio programma |
| 74 | 2026-08-19 | 2023-02-03 | 85,37 $ | 92,37 $ | -7,58% | da inizio programma |
| 75 | 2026-08-20 | 2023-02-04 | 87,64 $ | 91,91 $ | -4,65% | da inizio programma |
| 76 | 2026-08-21 | 2023-02-05 | 87,64 $ | 90,43 $ | -3,09% | da inizio programma |
| 77 | 2026-08-22 | 2023-02-06 | 93,70 $ | 89,66 $ | +4,51% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-08-29 | 85,91 $ | 89,78 $ | 89,13 $ / 95,78 $ | no | n/a | n/a | n/a |
| 14g | 2026-09-05 | 97,81 $ | 102,22 $ | 89,13 $ / 102,22 $ | no | n/a | n/a | n/a |
| 21g | 2026-09-12 | 92,66 $ | 96,84 $ | 89,13 $ / 102,22 $ | no | n/a | n/a | n/a |
| 28g | 2026-09-19 | 88,36 $ | 92,34 $ | 89,13 $ / 102,22 $ | no | n/a | n/a | n/a |
| 35g | 2026-09-26 | 95,32 $ | 99,62 $ | 83,11 $ / 102,22 $ | no | n/a | n/a | n/a |
| 42g | 2026-10-03 | 109,38 $ | 114,31 $ | 83,11 $ / 115,43 $ | no | n/a | n/a | n/a |
| 49g | 2026-10-10 | 106,91 $ | 111,73 $ | 83,11 $ / 116,65 $ | no | n/a | n/a | n/a |
| 56g | 2026-10-17 | 109,47 $ | 114,41 $ | 83,11 $ / 117,24 $ | no | n/a | n/a | n/a |
| 63g | 2026-10-24 | 116,81 $ | 122,08 $ | 83,11 $ / 122,08 $ | no | n/a | n/a | n/a |
| 70g | 2026-10-31 | 115,99 $ | 121,22 $ | 83,11 $ / 125,51 $ | no | n/a | n/a | n/a |
| 77g | 2026-11-07 | 108,43 $ | 113,32 $ | 83,11 $ / 125,51 $ | no | n/a | n/a | n/a |
| 84g | 2026-11-14 | 110,66 $ | 115,65 $ | 83,11 $ / 125,51 $ | no | n/a | n/a | n/a |
| 91g | 2026-11-21 | 109,09 $ | 114,01 $ | 83,11 $ / 125,51 $ | no | n/a | n/a | n/a |
| 98g | 2026-11-28 | 107,12 $ | 111,95 $ | 83,11 $ / 125,51 $ | no | n/a | n/a | n/a |
| 105g | 2026-12-05 | 105,77 $ | 110,54 $ | 83,11 $ / 125,51 $ | no | n/a | n/a | n/a |
| 112g | 2026-12-12 | 109,30 $ | 114,23 $ | 83,11 $ / 125,51 $ | no | n/a | n/a | n/a |
| 119g | 2026-12-19 | 101,48 $ | 106,05 $ | 83,11 $ / 125,51 $ | no | n/a | n/a | n/a |
| 126g | 2026-12-26 | 102,04 $ | 106,64 $ | 83,11 $ / 125,51 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 37 | 43,24% | 7,71% | 13,40% |
| 14g | 32 | 34,38% | 15,75% | 12,36% |
| 21g | 25 | 24,00% | 22,95% | 13,82% |
| 28g | 18 | 50,00% | 25,62% | 13,94% |
| 35g | 11 | 54,55% | 24,45% | 12,15% |
| 42g | 4 | 100,00% | 16,48% | 3,80% |
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
