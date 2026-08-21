<!-- FRACTAL_PATH_TRACKER_START -->
# Tracking percorso frattale SOL/BTC

Generato: 2026-08-21 05:32 UTC

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-08-21**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-02-05**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **89,55 $**
- Verdetto principale: **ANALOGIA DEBOLE / SCENARIO SECONDARIO**
- Somiglianza strutturale: **+61,09%**
- Aderenza live principale: **+70,11%**
- Errore medio live principale: **14,95%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE SOLO DI CONTESTO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **76**
- Osservazioni inclusive dal bottom: **77**
- Osservazioni da inizio programma/scanner: **50**
- Errore assoluto medio dal bottom: **11,82%**
- Errore assoluto medio da inizio programma: **14,95%**
- Gap firmato medio ultimi 7 giorni: **-12,23%**
- Errore assoluto medio ultimi 7 giorni: **12,23%**
- Gap ultimo giorno: **-0,97%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **-0,97%**
- Gap firmato medio 7g: **-12,23%**
- Errore assoluto medio 7g: **12,23%**
- Variazione recente gap: **+15,72%**
- Stato gap: **VICINO AL FRATTALE**
- Trend gap: **SOL e sotto il percorso ancorato ma sta recuperando**

Soglie operative del grafico:

- entro **±5%**: percorso vicino;
- tra **±5% e ±12%**: deviazione gestibile;
- oltre **±12%**: frattale non abbastanza aderente per conferma operativa;
- oltre **±18%**: disallineamento marcato.

## Ultimi giorni del confronto ancorato

|   Giorno | Data SOL   | Data BTC eq.   | SOL reale   | Percorso ancorato   | Gap firmato   | Fase                |
|---------:|:-----------|:---------------|:------------|:--------------------|:--------------|:--------------------|
| 67 | 2026-08-12 | 2023-01-27 | 75,53 $ | 90,91 $ | -16,93% | da inizio programma |
| 68 | 2026-08-13 | 2023-01-28 | 76,18 $ | 90,72 $ | -16,03% | da inizio programma |
| 69 | 2026-08-14 | 2023-01-29 | 75,33 $ | 93,65 $ | -19,57% | da inizio programma |
| 70 | 2026-08-15 | 2023-01-30 | 75,27 $ | 89,97 $ | -16,34% | da inizio programma |
| 71 | 2026-08-16 | 2023-01-31 | 74,54 $ | 91,15 $ | -18,22% | da inizio programma |
| 72 | 2026-08-17 | 2023-02-01 | 75,94 $ | 93,45 $ | -18,74% | da inizio programma |
| 73 | 2026-08-18 | 2023-02-02 | 77,03 $ | 92,46 $ | -16,69% | da inizio programma |
| 74 | 2026-08-19 | 2023-02-03 | 85,37 $ | 92,37 $ | -7,58% | da inizio programma |
| 75 | 2026-08-20 | 2023-02-04 | 85,37 $ | 91,91 $ | -7,11% | da inizio programma |
| 76 | 2026-08-21 | 2023-02-05 | 89,55 $ | 90,43 $ | -0,97% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-08-28 | 85,83 $ | 85,00 $ | 84,46 $ / 90,75 $ | no | n/a | n/a | n/a |
| 14g | 2026-09-04 | 95,83 $ | 94,90 $ | 84,46 $ / 96,13 $ | no | n/a | n/a | n/a |
| 21g | 2026-09-11 | 92,81 $ | 91,91 $ | 84,46 $ / 96,86 $ | no | n/a | n/a | n/a |
| 28g | 2026-09-18 | 88,38 $ | 87,52 $ | 84,46 $ / 96,86 $ | no | n/a | n/a | n/a |
| 35g | 2026-09-25 | 87,31 $ | 86,46 $ | 78,75 $ / 96,86 $ | no | n/a | n/a | n/a |
| 42g | 2026-10-02 | 110,45 $ | 109,38 $ | 78,75 $ / 109,38 $ | no | n/a | n/a | n/a |
| 49g | 2026-10-09 | 110,28 $ | 109,21 $ | 78,75 $ / 110,53 $ | no | n/a | n/a | n/a |
| 56g | 2026-10-16 | 111,08 $ | 110,01 $ | 78,75 $ / 111,09 $ | no | n/a | n/a | n/a |
| 63g | 2026-10-23 | 111,61 $ | 110,53 $ | 78,75 $ / 111,09 $ | no | n/a | n/a | n/a |
| 70g | 2026-10-30 | 119,42 $ | 118,26 $ | 78,75 $ / 118,92 $ | no | n/a | n/a | n/a |
| 77g | 2026-11-06 | 108,69 $ | 107,63 $ | 78,75 $ / 118,92 $ | no | n/a | n/a | n/a |
| 84g | 2026-11-13 | 115,30 $ | 114,18 $ | 78,75 $ / 118,92 $ | no | n/a | n/a | n/a |
| 91g | 2026-11-20 | 112,09 $ | 111,00 $ | 78,75 $ / 118,92 $ | no | n/a | n/a | n/a |
| 98g | 2026-11-27 | 106,09 $ | 105,06 $ | 78,75 $ / 118,92 $ | no | n/a | n/a | n/a |
| 105g | 2026-12-04 | 105,39 $ | 104,37 $ | 78,75 $ / 118,92 $ | no | n/a | n/a | n/a |
| 112g | 2026-12-11 | 110,64 $ | 109,56 $ | 78,75 $ / 118,92 $ | no | n/a | n/a | n/a |
| 119g | 2026-12-18 | 106,83 $ | 105,79 $ | 78,75 $ / 118,92 $ | no | n/a | n/a | n/a |
| 126g | 2026-12-25 | 102,18 $ | 101,19 $ | 78,75 $ / 118,92 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 36 | 44,44% | 7,31% | 13,60% |
| 14g | 31 | 35,48% | 15,39% | 12,64% |
| 21g | 24 | 25,00% | 23,09% | 14,25% |
| 28g | 17 | 47,06% | 26,87% | 14,60% |
| 35g | 10 | 50,00% | 26,09% | 13,15% |
| 42g | 3 | 100,00% | 19,21% | 0,97% |
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
