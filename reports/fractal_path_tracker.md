<!-- FRACTAL_PATH_TRACKER_START -->
# Tracking percorso frattale SOL/BTC

Generato: 2026-08-10 05:16 UTC

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-08-10**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-01-25**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **76,55 $**
- Verdetto principale: **ANALOGIA DEBOLE / SCENARIO SECONDARIO**
- Somiglianza strutturale: **+56,89%**
- Aderenza live principale: **+69,61%**
- Errore medio live principale: **15,20%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE SOLO DI CONTESTO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **65**
- Osservazioni inclusive dal bottom: **66**
- Osservazioni da inizio programma/scanner: **39**
- Errore assoluto medio dal bottom: **11,44%**
- Errore assoluto medio da inizio programma: **15,20%**
- Gap firmato medio ultimi 7 giorni: **-15,99%**
- Errore assoluto medio ultimi 7 giorni: **15,99%**
- Gap ultimo giorno: **-15,94%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **-15,94%**
- Gap firmato medio 7g: **-15,99%**
- Errore assoluto medio 7g: **15,99%**
- Variazione recente gap: **+1,78%**
- Stato gap: **IN DEVIAZIONE SOTTO IL FRATTALE**
- Trend gap: **SOL e sotto il percorso ancorato ma sta recuperando**

Soglie operative del grafico:

- entro **±5%**: percorso vicino;
- tra **±5% e ±12%**: deviazione gestibile;
- oltre **±12%**: frattale non abbastanza aderente per conferma operativa;
- oltre **±18%**: disallineamento marcato.

## Ultimi giorni del confronto ancorato

|   Giorno | Data SOL   | Data BTC eq.   | SOL reale   | Percorso ancorato   | Gap firmato   | Fase                |
|---------:|:-----------|:---------------|:------------|:--------------------|:--------------|:--------------------|
| 56 | 2026-08-01 | 2023-01-16 | 71,87 $ | 83,39 $ | -13,82% | da inizio programma |
| 57 | 2026-08-02 | 2023-01-17 | 73,45 $ | 83,36 $ | -11,89% | da inizio programma |
| 58 | 2026-08-03 | 2023-01-18 | 73,47 $ | 81,50 $ | -9,85% | da inizio programma |
| 59 | 2026-08-04 | 2023-01-19 | 73,72 $ | 83,07 $ | -11,25% | da inizio programma |
| 60 | 2026-08-05 | 2023-01-20 | 73,96 $ | 89,33 $ | -17,20% | da inizio programma |
| 61 | 2026-08-06 | 2023-01-21 | 72,58 $ | 89,73 $ | -19,11% | da inizio programma |
| 62 | 2026-08-07 | 2023-01-22 | 73,64 $ | 89,50 $ | -17,72% | da inizio programma |
| 63 | 2026-08-08 | 2023-01-23 | 75,97 $ | 90,34 $ | -15,91% | da inizio programma |
| 64 | 2026-08-09 | 2023-01-24 | 75,97 $ | 89,17 $ | -14,80% | da inizio programma |
| 65 | 2026-08-10 | 2023-01-25 | 76,55 $ | 91,07 $ | -15,94% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-08-17 | 93,45 $ | 78,56 $ | 75,63 $ / 78,72 $ | no | n/a | n/a | n/a |
| 14g | 2026-08-24 | 90,36 $ | 75,96 $ | 75,37 $ / 78,72 $ | no | n/a | n/a | n/a |
| 21g | 2026-08-31 | 95,75 $ | 80,49 $ | 71,69 $ / 80,49 $ | no | n/a | n/a | n/a |
| 28g | 2026-09-07 | 95,29 $ | 80,10 $ | 71,69 $ / 82,22 $ | no | n/a | n/a | n/a |
| 35g | 2026-09-14 | 93,15 $ | 78,30 $ | 71,69 $ / 82,22 $ | no | n/a | n/a | n/a |
| 42g | 2026-09-21 | 85,55 $ | 71,91 $ | 71,69 $ / 82,22 $ | no | n/a | n/a | n/a |
| 49g | 2026-09-28 | 96,02 $ | 80,72 $ | 66,85 $ / 82,22 $ | no | n/a | n/a | n/a |
| 56g | 2026-10-05 | 107,57 $ | 90,42 $ | 66,85 $ / 93,30 $ | no | n/a | n/a | n/a |
| 63g | 2026-10-12 | 111,67 $ | 93,87 $ | 66,85 $ / 93,87 $ | no | n/a | n/a | n/a |
| 70g | 2026-10-19 | 111,00 $ | 93,31 $ | 66,85 $ / 94,30 $ | no | n/a | n/a | n/a |
| 77g | 2026-10-26 | 118,72 $ | 99,80 $ | 66,85 $ / 100,12 $ | no | n/a | n/a | n/a |
| 84g | 2026-11-02 | 113,54 $ | 95,44 $ | 66,85 $ / 100,95 $ | no | n/a | n/a | n/a |
| 91g | 2026-11-09 | 111,96 $ | 94,12 $ | 66,85 $ / 100,95 $ | no | n/a | n/a | n/a |
| 98g | 2026-11-16 | 114,26 $ | 96,05 $ | 66,85 $ / 100,95 $ | no | n/a | n/a | n/a |
| 105g | 2026-11-23 | 108,81 $ | 91,46 $ | 66,85 $ / 100,95 $ | no | n/a | n/a | n/a |
| 112g | 2026-11-30 | 107,93 $ | 90,73 $ | 66,85 $ / 100,95 $ | no | n/a | n/a | n/a |
| 119g | 2026-12-07 | 103,74 $ | 87,20 $ | 66,85 $ / 100,95 $ | no | n/a | n/a | n/a |
| 126g | 2026-12-14 | 107,22 $ | 90,13 $ | 66,85 $ / 100,95 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 27 | 40,74% | 8,23% | 12,90% |
| 14g | 20 | 20,00% | 18,06% | 11,77% |
| 21g | 13 | 15,38% | 25,82% | 14,45% |
| 28g | 6 | 33,33% | 28,97% | 16,09% |
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
