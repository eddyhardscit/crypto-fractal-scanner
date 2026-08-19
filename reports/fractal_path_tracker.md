<!-- FRACTAL_PATH_TRACKER_START -->
# Tracking percorso frattale SOL/BTC

Generato: 2026-08-19 05:32 UTC

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-08-19**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-02-03**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **76,92 $**
- Verdetto principale: **ANALOGIA DEBOLE / SCENARIO SECONDARIO**
- Somiglianza strutturale: **+58,26%**
- Aderenza live principale: **+68,77%**
- Errore medio live principale: **15,62%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE SOLO DI CONTESTO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **74**
- Osservazioni inclusive dal bottom: **75**
- Osservazioni da inizio programma/scanner: **48**
- Errore assoluto medio dal bottom: **12,16%**
- Errore assoluto medio da inizio programma: **15,62%**
- Gap firmato medio ultimi 7 giorni: **-17,64%**
- Errore assoluto medio ultimi 7 giorni: **17,64%**
- Gap ultimo giorno: **-16,73%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **-16,73%**
- Gap firmato medio 7g: **-17,64%**
- Errore assoluto medio 7g: **17,64%**
- Variazione recente gap: **+1,50%**
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
| 65 | 2026-08-10 | 2023-01-25 | 75,95 $ | 91,07 $ | -16,60% | da inizio programma |
| 66 | 2026-08-11 | 2023-01-26 | 76,20 $ | 90,73 $ | -16,02% | da inizio programma |
| 67 | 2026-08-12 | 2023-01-27 | 75,53 $ | 90,91 $ | -16,93% | da inizio programma |
| 68 | 2026-08-13 | 2023-01-28 | 76,18 $ | 90,72 $ | -16,03% | da inizio programma |
| 69 | 2026-08-14 | 2023-01-29 | 75,33 $ | 93,65 $ | -19,57% | da inizio programma |
| 70 | 2026-08-15 | 2023-01-30 | 75,27 $ | 89,97 $ | -16,34% | da inizio programma |
| 71 | 2026-08-16 | 2023-01-31 | 74,54 $ | 91,15 $ | -18,22% | da inizio programma |
| 72 | 2026-08-17 | 2023-02-01 | 75,94 $ | 93,45 $ | -18,74% | da inizio programma |
| 73 | 2026-08-18 | 2023-02-02 | 75,94 $ | 92,46 $ | -17,86% | da inizio programma |
| 74 | 2026-08-19 | 2023-02-03 | 76,92 $ | 92,37 $ | -16,73% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-08-26 | 85,29 $ | 71,02 $ | 71,02 $ / 76,92 $ | no | n/a | n/a | n/a |
| 14g | 2026-09-02 | 96,77 $ | 80,58 $ | 71,02 $ / 80,58 $ | no | n/a | n/a | n/a |
| 21g | 2026-09-09 | 91,38 $ | 76,10 $ | 71,02 $ / 81,45 $ | no | n/a | n/a | n/a |
| 28g | 2026-09-16 | 88,09 $ | 73,36 $ | 71,02 $ / 81,45 $ | no | n/a | n/a | n/a |
| 35g | 2026-09-23 | 79,52 $ | 66,22 $ | 66,22 $ / 81,45 $ | no | n/a | n/a | n/a |
| 42g | 2026-09-30 | 108,03 $ | 89,96 $ | 66,22 $ / 89,96 $ | no | n/a | n/a | n/a |
| 49g | 2026-10-07 | 108,30 $ | 90,19 $ | 66,22 $ / 92,94 $ | no | n/a | n/a | n/a |
| 56g | 2026-10-14 | 112,18 $ | 93,42 $ | 66,22 $ / 93,42 $ | no | n/a | n/a | n/a |
| 63g | 2026-10-21 | 110,01 $ | 91,60 $ | 66,22 $ / 93,42 $ | no | n/a | n/a | n/a |
| 70g | 2026-10-28 | 120,09 $ | 100,00 $ | 66,22 $ / 100,00 $ | no | n/a | n/a | n/a |
| 77g | 2026-11-04 | 107,45 $ | 89,48 $ | 66,22 $ / 100,00 $ | no | n/a | n/a | n/a |
| 84g | 2026-11-11 | 115,58 $ | 96,24 $ | 66,22 $ / 100,00 $ | no | n/a | n/a | n/a |
| 91g | 2026-11-18 | 116,34 $ | 96,88 $ | 66,22 $ / 100,00 $ | no | n/a | n/a | n/a |
| 98g | 2026-11-25 | 105,59 $ | 87,93 $ | 66,22 $ / 100,00 $ | no | n/a | n/a | n/a |
| 105g | 2026-12-02 | 105,93 $ | 88,21 $ | 66,22 $ / 100,00 $ | no | n/a | n/a | n/a |
| 112g | 2026-12-09 | 105,25 $ | 87,65 $ | 66,22 $ / 100,00 $ | no | n/a | n/a | n/a |
| 119g | 2026-12-16 | 107,34 $ | 89,39 $ | 66,22 $ / 100,00 $ | no | n/a | n/a | n/a |
| 126g | 2026-12-23 | 104,31 $ | 86,86 $ | 66,22 $ / 100,00 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 35 | 45,71% | 6,90% | 14,02% |
| 14g | 29 | 41,38% | 14,92% | 13,66% |
| 21g | 22 | 27,27% | 25,03% | 15,79% |
| 28g | 15 | 33,33% | 28,94% | 17,02% |
| 35g | 8 | 12,50% | 29,51% | 17,91% |
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
