<!-- FRACTAL_PATH_TRACKER_START -->
# Tracking percorso frattale SOL/BTC

Generato: 2026-08-29 05:32 UTC

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-08-29**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-02-13**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **104,04 $**
- Verdetto principale: **ANALOGIA DEBOLE / SCENARIO SECONDARIO**
- Somiglianza strutturale: **+63,94%**
- Aderenza live principale: **+69,91%**
- Errore medio live principale: **15,05%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE SOLO DI CONTESTO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **84**
- Osservazioni inclusive dal bottom: **85**
- Osservazioni da inizio programma/scanner: **58**
- Errore assoluto medio dal bottom: **12,18%**
- Errore assoluto medio da inizio programma: **15,05%**
- Gap firmato medio ultimi 7 giorni: **+17,22%**
- Errore assoluto medio ultimi 7 giorni: **17,22%**
- Gap ultimo giorno: **+21,11%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **+21,11%**
- Gap firmato medio 7g: **+17,22%**
- Errore assoluto medio 7g: **17,22%**
- Variazione recente gap: **+1,32%**
- Stato gap: **DISALLINEATO SOPRA IL FRATTALE**
- Trend gap: **SOL sta aumentando il distacco sopra il percorso ancorato**

Soglie operative del grafico:

- entro **±5%**: percorso vicino;
- tra **±5% e ±12%**: deviazione gestibile;
- oltre **±12%**: frattale non abbastanza aderente per conferma operativa;
- oltre **±18%**: disallineamento marcato.

## Ultimi giorni del confronto ancorato

|   Giorno | Data SOL   | Data BTC eq.   | SOL reale   | Percorso ancorato   | Gap firmato   | Fase                |
|---------:|:-----------|:---------------|:------------|:--------------------|:--------------|:--------------------|
| 75 | 2026-08-20 | 2023-02-04 | 87,64 $ | 91,91 $ | -4,65% | da inizio programma |
| 76 | 2026-08-21 | 2023-02-05 | 93,65 $ | 90,43 $ | +3,57% | da inizio programma |
| 77 | 2026-08-22 | 2023-02-06 | 93,91 $ | 89,66 $ | +4,75% | da inizio programma |
| 78 | 2026-08-23 | 2023-02-07 | 95,44 $ | 91,64 $ | +4,15% | da inizio programma |
| 79 | 2026-08-24 | 2023-02-08 | 98,56 $ | 90,36 $ | +9,07% | da inizio programma |
| 80 | 2026-08-25 | 2023-02-09 | 96,60 $ | 85,95 $ | +12,39% | da inizio programma |
| 81 | 2026-08-26 | 2023-02-10 | 102,17 $ | 85,29 $ | +19,79% | da inizio programma |
| 82 | 2026-08-27 | 2023-02-11 | 109,21 $ | 86,15 $ | +26,76% | da inizio programma |
| 83 | 2026-08-28 | 2023-02-12 | 109,21 $ | 85,83 $ | +27,24% | da inizio programma |
| 84 | 2026-08-29 | 2023-02-13 | 104,04 $ | 85,91 $ | +21,11% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-09-05 | 97,81 $ | 118,45 $ | 104,04 $ / 118,45 $ | no | n/a | n/a | n/a |
| 14g | 2026-09-12 | 92,66 $ | 112,22 $ | 104,04 $ / 118,45 $ | no | n/a | n/a | n/a |
| 21g | 2026-09-19 | 88,36 $ | 107,01 $ | 104,04 $ / 118,45 $ | no | n/a | n/a | n/a |
| 28g | 2026-09-26 | 95,32 $ | 115,44 $ | 96,31 $ / 118,45 $ | no | n/a | n/a | n/a |
| 35g | 2026-10-03 | 109,38 $ | 132,47 $ | 96,31 $ / 133,76 $ | no | n/a | n/a | n/a |
| 42g | 2026-10-10 | 106,91 $ | 129,48 $ | 96,31 $ / 135,17 $ | no | n/a | n/a | n/a |
| 49g | 2026-10-17 | 109,47 $ | 132,58 $ | 96,31 $ / 135,86 $ | no | n/a | n/a | n/a |
| 56g | 2026-10-24 | 116,81 $ | 141,47 $ | 96,31 $ / 141,47 $ | no | n/a | n/a | n/a |
| 63g | 2026-10-31 | 115,99 $ | 140,47 $ | 96,31 $ / 145,44 $ | no | n/a | n/a | n/a |
| 70g | 2026-11-07 | 108,43 $ | 131,32 $ | 96,31 $ / 145,44 $ | no | n/a | n/a | n/a |
| 77g | 2026-11-14 | 110,66 $ | 134,02 $ | 96,31 $ / 145,44 $ | no | n/a | n/a | n/a |
| 84g | 2026-11-21 | 109,09 $ | 132,12 $ | 96,31 $ / 145,44 $ | no | n/a | n/a | n/a |
| 91g | 2026-11-28 | 107,12 $ | 129,73 $ | 96,31 $ / 145,44 $ | no | n/a | n/a | n/a |
| 98g | 2026-12-05 | 105,77 $ | 128,10 $ | 96,31 $ / 145,44 $ | no | n/a | n/a | n/a |
| 105g | 2026-12-12 | 109,30 $ | 132,37 $ | 96,31 $ / 145,44 $ | no | n/a | n/a | n/a |
| 112g | 2026-12-19 | 101,48 $ | 122,89 $ | 96,31 $ / 145,44 $ | no | n/a | n/a | n/a |
| 119g | 2026-12-26 | 102,04 $ | 123,57 $ | 96,31 $ / 145,44 $ | no | n/a | n/a | n/a |
| 126g | 2027-01-02 | 105,77 $ | 128,10 $ | 96,31 $ / 145,44 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 44 | 36,36% | 11,76% | 14,05% |
| 14g | 37 | 29,73% | 18,95% | 12,72% |
| 21g | 32 | 18,75% | 26,56% | 14,63% |
| 28g | 25 | 44,00% | 24,99% | 14,97% |
| 35g | 18 | 55,56% | 17,68% | 14,41% |
| 42g | 11 | 90,91% | 9,74% | 14,31% |
| 49g | 4 | 100,00% | 6,88% | 24,17% |
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
