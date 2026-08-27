<!-- FRACTAL_PATH_TRACKER_START -->
# Tracking percorso frattale SOL/BTC

Generato: 2026-08-27 05:32 UTC

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-08-27**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-02-11**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **100,99 $**
- Verdetto principale: **ANALOGIA DEBOLE / SCENARIO SECONDARIO**
- Somiglianza strutturale: **+64,58%**
- Aderenza live principale: **+71,13%**
- Errore medio live principale: **14,43%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE SOLO DI CONTESTO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **82**
- Osservazioni inclusive dal bottom: **83**
- Osservazioni da inizio programma/scanner: **56**
- Errore assoluto medio dal bottom: **11,70%**
- Errore assoluto medio da inizio programma: **14,43%**
- Gap firmato medio ultimi 7 giorni: **+9,20%**
- Errore assoluto medio ultimi 7 giorni: **9,20%**
- Gap ultimo giorno: **+17,22%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **+17,22%**
- Gap firmato medio 7g: **+9,20%**
- Errore assoluto medio 7g: **9,20%**
- Variazione recente gap: **+8,15%**
- Stato gap: **IN DEVIAZIONE SOPRA IL FRATTALE**
- Trend gap: **SOL sta aumentando il distacco sopra il percorso ancorato**

Soglie operative del grafico:

- entro **±5%**: percorso vicino;
- tra **±5% e ±12%**: deviazione gestibile;
- oltre **±12%**: frattale non abbastanza aderente per conferma operativa;
- oltre **±18%**: disallineamento marcato.

## Ultimi giorni del confronto ancorato

|   Giorno | Data SOL   | Data BTC eq.   | SOL reale   | Percorso ancorato   | Gap firmato   | Fase                |
|---------:|:-----------|:---------------|:------------|:--------------------|:--------------|:--------------------|
| 73 | 2026-08-18 | 2023-02-02 | 77,03 $ | 92,46 $ | -16,69% | da inizio programma |
| 74 | 2026-08-19 | 2023-02-03 | 85,37 $ | 92,37 $ | -7,58% | da inizio programma |
| 75 | 2026-08-20 | 2023-02-04 | 87,64 $ | 91,91 $ | -4,65% | da inizio programma |
| 76 | 2026-08-21 | 2023-02-05 | 93,65 $ | 90,43 $ | +3,57% | da inizio programma |
| 77 | 2026-08-22 | 2023-02-06 | 93,91 $ | 89,66 $ | +4,75% | da inizio programma |
| 78 | 2026-08-23 | 2023-02-07 | 95,44 $ | 91,64 $ | +4,15% | da inizio programma |
| 79 | 2026-08-24 | 2023-02-08 | 98,56 $ | 90,36 $ | +9,07% | da inizio programma |
| 80 | 2026-08-25 | 2023-02-09 | 96,60 $ | 85,95 $ | +12,39% | da inizio programma |
| 81 | 2026-08-26 | 2023-02-10 | 96,60 $ | 85,29 $ | +13,27% | da inizio programma |
| 82 | 2026-08-27 | 2023-02-11 | 100,99 $ | 86,15 $ | +17,22% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-09-03 | 97,07 $ | 113,78 $ | 100,61 $ / 113,78 $ | no | n/a | n/a | n/a |
| 14g | 2026-09-10 | 91,29 $ | 107,01 $ | 100,61 $ / 114,65 $ | no | n/a | n/a | n/a |
| 21g | 2026-09-17 | 88,06 $ | 103,22 $ | 100,61 $ / 114,65 $ | no | n/a | n/a | n/a |
| 28g | 2026-09-24 | 81,28 $ | 95,27 $ | 93,22 $ / 114,65 $ | no | n/a | n/a | n/a |
| 35g | 2026-10-01 | 106,22 $ | 124,52 $ | 93,22 $ / 126,63 $ | no | n/a | n/a | n/a |
| 42g | 2026-10-08 | 108,31 $ | 126,96 $ | 93,22 $ / 130,83 $ | no | n/a | n/a | n/a |
| 49g | 2026-10-15 | 111,92 $ | 131,19 $ | 93,22 $ / 131,50 $ | no | n/a | n/a | n/a |
| 56g | 2026-10-22 | 110,09 $ | 129,05 $ | 93,22 $ / 131,50 $ | no | n/a | n/a | n/a |
| 63g | 2026-10-29 | 119,43 $ | 140,00 $ | 93,22 $ / 140,77 $ | no | n/a | n/a | n/a |
| 70g | 2026-11-05 | 109,58 $ | 128,45 $ | 93,22 $ / 140,77 $ | no | n/a | n/a | n/a |
| 77g | 2026-11-12 | 115,22 $ | 135,06 $ | 93,22 $ / 140,77 $ | no | n/a | n/a | n/a |
| 84g | 2026-11-19 | 113,86 $ | 133,47 $ | 93,22 $ / 140,77 $ | no | n/a | n/a | n/a |
| 91g | 2026-11-26 | 105,51 $ | 123,68 $ | 93,22 $ / 140,77 $ | no | n/a | n/a | n/a |
| 98g | 2026-12-03 | 106,87 $ | 125,27 $ | 93,22 $ / 140,77 $ | no | n/a | n/a | n/a |
| 105g | 2026-12-10 | 105,84 $ | 124,07 $ | 93,22 $ / 140,77 $ | no | n/a | n/a | n/a |
| 112g | 2026-12-17 | 106,66 $ | 125,02 $ | 93,22 $ / 140,77 $ | no | n/a | n/a | n/a |
| 119g | 2026-12-24 | 101,83 $ | 119,37 $ | 93,22 $ / 140,77 $ | no | n/a | n/a | n/a |
| 126g | 2026-12-31 | 104,43 $ | 122,41 $ | 93,22 $ / 140,77 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 42 | 38,10% | 10,84% | 13,15% |
| 14g | 35 | 31,43% | 17,10% | 12,03% |
| 21g | 30 | 20,00% | 24,24% | 13,38% |
| 28g | 23 | 47,83% | 22,93% | 13,33% |
| 35g | 16 | 68,75% | 17,90% | 11,87% |
| 42g | 9 | 100,00% | 9,41% | 9,20% |
| 49g | 2 | 100,00% | 0,20% | n/a |
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
