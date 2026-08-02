<!-- FRACTAL_PATH_TRACKER_START -->
# Tracking percorso frattale SOL/BTC

Generato: 2026-08-02 05:14 UTC

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-08-02**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-01-17**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **73,42 $**
- Verdetto principale: **ANALOGIA DEBOLE / SCENARIO SECONDARIO**
- Somiglianza strutturale: **+58,00%**
- Aderenza live principale: **+69,69%**
- Errore medio live principale: **15,16%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE SOLO DI CONTESTO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **57**
- Osservazioni inclusive dal bottom: **58**
- Osservazioni da inizio programma/scanner: **31**
- Errore assoluto medio dal bottom: **10,91%**
- Errore assoluto medio da inizio programma: **15,16%**
- Gap firmato medio ultimi 7 giorni: **-6,87%**
- Errore assoluto medio ultimi 7 giorni: **8,28%**
- Gap ultimo giorno: **-11,92%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **-11,92%**
- Gap firmato medio 7g: **-6,87%**
- Errore assoluto medio 7g: **8,28%**
- Variazione recente gap: **-2,05%**
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
| 48 | 2026-07-24 | 2023-01-08 | 73,88 $ | 67,33 $ | +9,73% | da inizio programma |
| 49 | 2026-07-25 | 2023-01-09 | 74,43 $ | 67,74 $ | +9,87% | da inizio programma |
| 50 | 2026-07-26 | 2023-01-10 | 76,60 $ | 68,73 $ | +11,46% | da inizio programma |
| 51 | 2026-07-27 | 2023-01-11 | 74,14 $ | 70,65 $ | +4,94% | da inizio programma |
| 52 | 2026-07-28 | 2023-01-12 | 73,70 $ | 74,33 $ | -0,85% | da inizio programma |
| 53 | 2026-07-29 | 2023-01-13 | 73,60 $ | 78,43 $ | -6,16% | da inizio programma |
| 54 | 2026-07-30 | 2023-01-14 | 74,47 $ | 82,63 $ | -9,88% | da inizio programma |
| 55 | 2026-07-31 | 2023-01-15 | 72,79 $ | 82,25 $ | -11,51% | da inizio programma |
| 56 | 2026-08-01 | 2023-01-16 | 72,79 $ | 83,39 $ | -12,71% | da inizio programma |
| 57 | 2026-08-02 | 2023-01-17 | 73,42 $ | 83,36 $ | -11,92% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-08-09 | 89,17 $ | 78,54 $ | 71,78 $ / 79,57 $ | no | n/a | n/a | n/a |
| 14g | 2026-08-16 | 91,15 $ | 80,28 $ | 71,78 $ / 82,49 $ | no | n/a | n/a | n/a |
| 21g | 2026-08-23 | 91,64 $ | 80,72 $ | 71,78 $ / 82,49 $ | no | n/a | n/a | n/a |
| 28g | 2026-08-30 | 87,53 $ | 77,10 $ | 71,78 $ / 82,49 $ | no | n/a | n/a | n/a |
| 35g | 2026-09-06 | 96,26 $ | 84,78 $ | 71,78 $ / 86,14 $ | no | n/a | n/a | n/a |
| 42g | 2026-09-13 | 91,18 $ | 80,31 $ | 71,78 $ / 86,14 $ | no | n/a | n/a | n/a |
| 49g | 2026-09-20 | 87,53 $ | 77,09 $ | 71,78 $ / 86,14 $ | no | n/a | n/a | n/a |
| 56g | 2026-09-27 | 97,48 $ | 85,86 $ | 70,04 $ / 86,14 $ | no | n/a | n/a | n/a |
| 63g | 2026-10-04 | 110,99 $ | 97,76 $ | 70,04 $ / 97,76 $ | no | n/a | n/a | n/a |
| 70g | 2026-10-11 | 107,42 $ | 94,61 $ | 70,04 $ / 98,30 $ | no | n/a | n/a | n/a |
| 77g | 2026-10-18 | 110,96 $ | 97,73 $ | 70,04 $ / 98,81 $ | no | n/a | n/a | n/a |
| 84g | 2026-10-25 | 119,10 $ | 104,90 $ | 70,04 $ / 104,90 $ | no | n/a | n/a | n/a |
| 91g | 2026-11-01 | 119,74 $ | 105,46 $ | 70,04 $ / 105,77 $ | no | n/a | n/a | n/a |
| 98g | 2026-11-08 | 111,51 $ | 98,21 $ | 70,04 $ / 105,77 $ | no | n/a | n/a | n/a |
| 105g | 2026-11-15 | 112,98 $ | 99,51 $ | 70,04 $ / 105,77 $ | no | n/a | n/a | n/a |
| 112g | 2026-11-22 | 108,95 $ | 95,96 $ | 70,04 $ / 105,77 $ | no | n/a | n/a | n/a |
| 119g | 2026-11-29 | 106,50 $ | 93,80 $ | 70,04 $ / 105,77 $ | no | n/a | n/a | n/a |
| 126g | 2026-12-06 | 107,25 $ | 94,46 $ | 70,04 $ / 105,77 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 19 | 21,05% | 8,00% | 11,75% |
| 14g | 12 | 8,33% | 13,43% | 8,90% |
| 21g | 5 | 0,00% | 24,17% | 12,05% |
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
