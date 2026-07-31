<!-- FRACTAL_PATH_TRACKER_START -->
# Tracking percorso frattale SOL/BTC

Generato: 2026-07-31 05:14 UTC

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-07-31**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-01-15**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **74,00 $**
- Verdetto principale: **ANALOGIA DEBOLE / SCENARIO SECONDARIO**
- Somiglianza strutturale: **+59,58%**
- Aderenza live principale: **+69,33%**
- Errore medio live principale: **15,34%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE SOLO DI CONTESTO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **55**
- Osservazioni inclusive dal bottom: **56**
- Osservazioni da inizio programma/scanner: **29**
- Errore assoluto medio dal bottom: **10,85%**
- Errore assoluto medio da inizio programma: **15,34%**
- Gap firmato medio ultimi 7 giorni: **-0,24%**
- Errore assoluto medio ultimi 7 giorni: **7,75%**
- Gap ultimo giorno: **-10,04%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **-10,04%**
- Gap firmato medio 7g: **-0,24%**
- Errore assoluto medio 7g: **7,75%**
- Variazione recente gap: **-9,18%**
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
| 46 | 2026-07-22 | 2023-01-06 | 77,91 $ | 66,78 $ | +16,66% | da inizio programma |
| 47 | 2026-07-23 | 2023-01-07 | 75,86 $ | 66,79 $ | +13,58% | da inizio programma |
| 48 | 2026-07-24 | 2023-01-08 | 73,88 $ | 67,33 $ | +9,73% | da inizio programma |
| 49 | 2026-07-25 | 2023-01-09 | 74,43 $ | 67,74 $ | +9,87% | da inizio programma |
| 50 | 2026-07-26 | 2023-01-10 | 76,60 $ | 68,73 $ | +11,46% | da inizio programma |
| 51 | 2026-07-27 | 2023-01-11 | 74,14 $ | 70,65 $ | +4,94% | da inizio programma |
| 52 | 2026-07-28 | 2023-01-12 | 73,70 $ | 74,33 $ | -0,85% | da inizio programma |
| 53 | 2026-07-29 | 2023-01-13 | 73,60 $ | 78,43 $ | -6,16% | da inizio programma |
| 54 | 2026-07-30 | 2023-01-14 | 73,60 $ | 82,63 $ | -10,93% | da inizio programma |
| 55 | 2026-07-31 | 2023-01-15 | 74,00 $ | 82,25 $ | -10,04% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-08-07 | 89,50 $ | 80,52 $ | 73,32 $ / 80,72 $ | no | n/a | n/a | n/a |
| 14g | 2026-08-14 | 93,65 $ | 84,26 $ | 73,32 $ / 84,26 $ | no | n/a | n/a | n/a |
| 21g | 2026-08-21 | 90,43 $ | 81,35 $ | 73,32 $ / 84,26 $ | no | n/a | n/a | n/a |
| 28g | 2026-08-28 | 85,83 $ | 77,22 $ | 73,32 $ / 84,26 $ | no | n/a | n/a | n/a |
| 35g | 2026-09-04 | 95,83 $ | 86,22 $ | 73,32 $ / 87,33 $ | no | n/a | n/a | n/a |
| 42g | 2026-09-11 | 92,81 $ | 83,50 $ | 73,32 $ / 87,99 $ | no | n/a | n/a | n/a |
| 49g | 2026-09-18 | 88,38 $ | 79,51 $ | 73,32 $ / 87,99 $ | no | n/a | n/a | n/a |
| 56g | 2026-09-25 | 87,31 $ | 78,55 $ | 71,54 $ / 87,99 $ | no | n/a | n/a | n/a |
| 63g | 2026-10-02 | 110,45 $ | 99,37 $ | 71,54 $ / 99,37 $ | no | n/a | n/a | n/a |
| 70g | 2026-10-09 | 110,28 $ | 99,21 $ | 71,54 $ / 100,41 $ | no | n/a | n/a | n/a |
| 77g | 2026-10-16 | 111,08 $ | 99,94 $ | 71,54 $ / 100,93 $ | no | n/a | n/a | n/a |
| 84g | 2026-10-23 | 111,61 $ | 100,41 $ | 71,54 $ / 100,93 $ | no | n/a | n/a | n/a |
| 91g | 2026-10-30 | 119,42 $ | 107,44 $ | 71,54 $ / 108,04 $ | no | n/a | n/a | n/a |
| 98g | 2026-11-06 | 108,69 $ | 97,78 $ | 71,54 $ / 108,04 $ | no | n/a | n/a | n/a |
| 105g | 2026-11-13 | 115,30 $ | 103,73 $ | 71,54 $ / 108,04 $ | no | n/a | n/a | n/a |
| 112g | 2026-11-20 | 112,09 $ | 100,84 $ | 71,54 $ / 108,04 $ | no | n/a | n/a | n/a |
| 119g | 2026-11-27 | 106,09 $ | 95,44 $ | 71,54 $ / 108,04 $ | no | n/a | n/a | n/a |
| 126g | 2026-12-04 | 105,39 $ | 94,81 $ | 71,54 $ / 108,04 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 17 | 23,53% | 6,58% | 11,64% |
| 14g | 10 | 10,00% | 11,35% | 8,00% |
| 21g | 3 | 0,00% | 23,94% | 10,04% |
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
