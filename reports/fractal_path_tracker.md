<!-- FRACTAL_PATH_TRACKER_START -->
# Tracking percorso frattale SOL/BTC

Generato: 2026-07-29 05:14 UTC

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-07-29**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-01-13**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **73,47 $**
- Verdetto principale: **ANALOGIA DEBOLE / SCENARIO SECONDARIO**
- Somiglianza strutturale: **+60,46%**
- Aderenza live principale: **+68,64%**
- Errore medio live principale: **15,68%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE SOLO DI CONTESTO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **53**
- Osservazioni inclusive dal bottom: **54**
- Osservazioni da inizio programma/scanner: **27**
- Errore assoluto medio dal bottom: **10,85%**
- Errore assoluto medio da inizio programma: **15,68%**
- Gap firmato medio ultimi 7 giorni: **+6,14%**
- Errore assoluto medio ultimi 7 giorni: **8,02%**
- Gap ultimo giorno: **-6,32%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **-6,32%**
- Gap firmato medio 7g: **+6,14%**
- Errore assoluto medio 7g: **8,02%**
- Variazione recente gap: **-17,78%**
- Stato gap: **SOTTO IL FRATTALE**
- Trend gap: **SOL si sta allontanando sotto il percorso ancorato**

Soglie operative del grafico:

- entro **±5%**: percorso vicino;
- tra **±5% e ±12%**: deviazione gestibile;
- oltre **±12%**: frattale non abbastanza aderente per conferma operativa;
- oltre **±18%**: disallineamento marcato.

## Ultimi giorni del confronto ancorato

|   Giorno | Data SOL   | Data BTC eq.   | SOL reale   | Percorso ancorato   | Gap firmato   | Fase                |
|---------:|:-----------|:---------------|:------------|:--------------------|:--------------|:--------------------|
| 44 | 2026-07-20 | 2023-01-04 | 77,79 $ | 66,43 $ | +17,11% | da inizio programma |
| 45 | 2026-07-21 | 2023-01-05 | 78,11 $ | 66,32 $ | +17,77% | da inizio programma |
| 46 | 2026-07-22 | 2023-01-06 | 77,91 $ | 66,78 $ | +16,66% | da inizio programma |
| 47 | 2026-07-23 | 2023-01-07 | 75,86 $ | 66,79 $ | +13,58% | da inizio programma |
| 48 | 2026-07-24 | 2023-01-08 | 73,88 $ | 67,33 $ | +9,73% | da inizio programma |
| 49 | 2026-07-25 | 2023-01-09 | 74,43 $ | 67,74 $ | +9,87% | da inizio programma |
| 50 | 2026-07-26 | 2023-01-10 | 76,60 $ | 68,73 $ | +11,46% | da inizio programma |
| 51 | 2026-07-27 | 2023-01-11 | 74,14 $ | 70,65 $ | +4,94% | da inizio programma |
| 52 | 2026-07-28 | 2023-01-12 | 74,14 $ | 74,33 $ | -0,26% | da inizio programma |
| 53 | 2026-07-29 | 2023-01-13 | 73,47 $ | 78,43 $ | -6,32% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-08-05 | 89,33 $ | 83,68 $ | 73,47 $ / 83,68 $ | no | n/a | n/a | n/a |
| 14g | 2026-08-12 | 90,91 $ | 85,16 $ | 73,47 $ / 85,31 $ | no | n/a | n/a | n/a |
| 21g | 2026-08-19 | 92,37 $ | 86,53 $ | 73,47 $ / 87,73 $ | no | n/a | n/a | n/a |
| 28g | 2026-08-26 | 85,29 $ | 79,90 $ | 73,47 $ / 87,73 $ | no | n/a | n/a | n/a |
| 35g | 2026-09-02 | 96,77 $ | 90,65 $ | 73,47 $ / 90,65 $ | no | n/a | n/a | n/a |
| 42g | 2026-09-09 | 91,38 $ | 85,61 $ | 73,47 $ / 91,62 $ | no | n/a | n/a | n/a |
| 49g | 2026-09-16 | 88,09 $ | 82,52 $ | 73,47 $ / 91,62 $ | no | n/a | n/a | n/a |
| 56g | 2026-09-23 | 79,52 $ | 74,49 $ | 73,47 $ / 91,62 $ | no | n/a | n/a | n/a |
| 63g | 2026-09-30 | 108,03 $ | 101,20 $ | 73,47 $ / 101,20 $ | no | n/a | n/a | n/a |
| 70g | 2026-10-07 | 108,30 $ | 101,46 $ | 73,47 $ / 104,56 $ | no | n/a | n/a | n/a |
| 77g | 2026-10-14 | 112,18 $ | 105,09 $ | 73,47 $ / 105,09 $ | no | n/a | n/a | n/a |
| 84g | 2026-10-21 | 110,01 $ | 103,05 $ | 73,47 $ / 105,09 $ | no | n/a | n/a | n/a |
| 91g | 2026-10-28 | 120,09 $ | 112,50 $ | 73,47 $ / 112,50 $ | no | n/a | n/a | n/a |
| 98g | 2026-11-04 | 107,45 $ | 100,66 $ | 73,47 $ / 112,50 $ | no | n/a | n/a | n/a |
| 105g | 2026-11-11 | 115,58 $ | 108,27 $ | 73,47 $ / 112,50 $ | no | n/a | n/a | n/a |
| 112g | 2026-11-18 | 116,34 $ | 108,99 $ | 73,47 $ / 112,50 $ | no | n/a | n/a | n/a |
| 119g | 2026-11-25 | 105,59 $ | 98,92 $ | 73,47 $ / 112,50 $ | no | n/a | n/a | n/a |
| 126g | 2026-12-02 | 105,93 $ | 99,23 $ | 73,47 $ / 112,50 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 15 | 26,67% | 4,58% | 11,79% |
| 14g | 8 | 12,50% | 8,55% | 7,10% |
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
