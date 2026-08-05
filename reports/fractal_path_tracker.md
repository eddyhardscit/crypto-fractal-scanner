<!-- FRACTAL_PATH_TRACKER_START -->
# Tracking percorso frattale SOL/BTC

Generato: 2026-08-05 05:15 UTC

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-08-05**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-01-20**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **73,91 $**
- Verdetto principale: **ANALOGIA DEBOLE / SCENARIO SECONDARIO**
- Somiglianza strutturale: **+56,86%**
- Aderenza live principale: **+70,03%**
- Errore medio live principale: **14,99%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE SOLO DI CONTESTO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **60**
- Osservazioni inclusive dal bottom: **61**
- Osservazioni da inizio programma/scanner: **34**
- Errore assoluto medio dal bottom: **11,02%**
- Errore assoluto medio da inizio programma: **14,99%**
- Gap firmato medio ultimi 7 giorni: **-12,25%**
- Errore assoluto medio ultimi 7 giorni: **12,25%**
- Gap ultimo giorno: **-17,26%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **-17,26%**
- Gap firmato medio 7g: **-12,25%**
- Errore assoluto medio 7g: **12,25%**
- Variazione recente gap: **-5,37%**
- Stato gap: **IN DEVIAZIONE SOTTO IL FRATTALE**
- Trend gap: **SOL si sta allontanando sotto il percorso ancorato**

Soglie operative del grafico:

- entro **±5%**: percorso vicino;
- tra **±5% e ±12%**: deviazione gestibile;
- oltre **±12%**: frattale non abbastanza aderente per conferma operativa;
- oltre **±18%**: disallineamento marcato.

## Ultimi giorni del confronto ancorato

|   Giorno | Data SOL   | Data BTC eq.   | SOL reale   | Percorso ancorato   | Gap firmato   | Fase                |
|---------:|:-----------|:---------------|:------------|:--------------------|:--------------|:--------------------|
| 51 | 2026-07-27 | 2023-01-11 | 74,14 $ | 70,65 $ | +4,94% | da inizio programma |
| 52 | 2026-07-28 | 2023-01-12 | 73,70 $ | 74,33 $ | -0,85% | da inizio programma |
| 53 | 2026-07-29 | 2023-01-13 | 73,60 $ | 78,43 $ | -6,16% | da inizio programma |
| 54 | 2026-07-30 | 2023-01-14 | 74,47 $ | 82,63 $ | -9,88% | da inizio programma |
| 55 | 2026-07-31 | 2023-01-15 | 72,79 $ | 82,25 $ | -11,51% | da inizio programma |
| 56 | 2026-08-01 | 2023-01-16 | 71,87 $ | 83,39 $ | -13,82% | da inizio programma |
| 57 | 2026-08-02 | 2023-01-17 | 73,45 $ | 83,36 $ | -11,89% | da inizio programma |
| 58 | 2026-08-03 | 2023-01-18 | 73,47 $ | 81,50 $ | -9,85% | da inizio programma |
| 59 | 2026-08-04 | 2023-01-19 | 73,47 $ | 83,07 $ | -11,55% | da inizio programma |
| 60 | 2026-08-05 | 2023-01-20 | 73,91 $ | 89,33 $ | -17,26% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-08-12 | 90,91 $ | 75,22 $ | 73,78 $ / 75,35 $ | no | n/a | n/a | n/a |
| 14g | 2026-08-19 | 92,37 $ | 76,43 $ | 73,78 $ / 77,49 $ | no | n/a | n/a | n/a |
| 21g | 2026-08-26 | 85,29 $ | 70,57 $ | 70,57 $ / 77,49 $ | no | n/a | n/a | n/a |
| 28g | 2026-09-02 | 96,77 $ | 80,07 $ | 70,57 $ / 80,07 $ | no | n/a | n/a | n/a |
| 35g | 2026-09-09 | 91,38 $ | 75,61 $ | 70,57 $ / 80,93 $ | no | n/a | n/a | n/a |
| 42g | 2026-09-16 | 88,09 $ | 72,89 $ | 70,57 $ / 80,93 $ | no | n/a | n/a | n/a |
| 49g | 2026-09-23 | 79,52 $ | 65,80 $ | 65,80 $ / 80,93 $ | no | n/a | n/a | n/a |
| 56g | 2026-09-30 | 108,03 $ | 89,38 $ | 65,80 $ / 89,38 $ | no | n/a | n/a | n/a |
| 63g | 2026-10-07 | 108,30 $ | 89,61 $ | 65,80 $ / 92,35 $ | no | n/a | n/a | n/a |
| 70g | 2026-10-14 | 112,18 $ | 92,82 $ | 65,80 $ / 92,82 $ | no | n/a | n/a | n/a |
| 77g | 2026-10-21 | 110,01 $ | 91,02 $ | 65,80 $ / 92,82 $ | no | n/a | n/a | n/a |
| 84g | 2026-10-28 | 120,09 $ | 99,36 $ | 65,80 $ / 99,36 $ | no | n/a | n/a | n/a |
| 91g | 2026-11-04 | 107,45 $ | 88,90 $ | 65,80 $ / 99,36 $ | no | n/a | n/a | n/a |
| 98g | 2026-11-11 | 115,58 $ | 95,63 $ | 65,80 $ / 99,36 $ | no | n/a | n/a | n/a |
| 105g | 2026-11-18 | 116,34 $ | 96,26 $ | 65,80 $ / 99,36 $ | no | n/a | n/a | n/a |
| 112g | 2026-11-25 | 105,59 $ | 87,37 $ | 65,80 $ / 99,36 $ | no | n/a | n/a | n/a |
| 119g | 2026-12-02 | 105,93 $ | 87,64 $ | 65,80 $ / 99,36 $ | no | n/a | n/a | n/a |
| 126g | 2026-12-09 | 105,25 $ | 87,09 $ | 65,80 $ / 99,36 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 22 | 27,27% | 8,70% | 11,97% |
| 14g | 15 | 6,67% | 15,82% | 9,91% |
| 21g | 8 | 0,00% | 24,80% | 12,65% |
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
