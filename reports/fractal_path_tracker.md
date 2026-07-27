<!-- FRACTAL_PATH_TRACKER_START -->
# Tracking percorso frattale SOL/BTC

Generato: 2026-07-27 05:14 UTC

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-07-27**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-01-11**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **76,32 $**
- Verdetto principale: **ANALOGIA DEBOLE / SCENARIO SECONDARIO**
- Somiglianza strutturale: **+64,77%**
- Aderenza live principale: **+66,66%**
- Errore medio live principale: **16,67%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE SOLO DI CONTESTO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **51**
- Osservazioni inclusive dal bottom: **52**
- Osservazioni da inizio programma/scanner: **25**
- Errore assoluto medio dal bottom: **11,14%**
- Errore assoluto medio da inizio programma: **16,67%**
- Gap firmato medio ultimi 7 giorni: **+11,99%**
- Errore assoluto medio ultimi 7 giorni: **11,99%**
- Gap ultimo giorno: **+8,03%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **+8,03%**
- Gap firmato medio 7g: **+11,99%**
- Errore assoluto medio 7g: **11,99%**
- Variazione recente gap: **-1,71%**
- Stato gap: **SOPRA IL FRATTALE**
- Trend gap: **SOL resta sopra il percorso ancorato, ma sta riducendo il distacco**

Soglie operative del grafico:

- entro **±5%**: percorso vicino;
- tra **±5% e ±12%**: deviazione gestibile;
- oltre **±12%**: frattale non abbastanza aderente per conferma operativa;
- oltre **±18%**: disallineamento marcato.

## Ultimi giorni del confronto ancorato

|   Giorno | Data SOL   | Data BTC eq.   | SOL reale   | Percorso ancorato   | Gap firmato   | Fase                |
|---------:|:-----------|:---------------|:------------|:--------------------|:--------------|:--------------------|
| 42 | 2026-07-18 | 2023-01-02 | 75,46 $ | 65,74 $ | +14,79% | da inizio programma |
| 43 | 2026-07-19 | 2023-01-03 | 76,36 $ | 65,71 $ | +16,21% | da inizio programma |
| 44 | 2026-07-20 | 2023-01-04 | 77,79 $ | 66,43 $ | +17,11% | da inizio programma |
| 45 | 2026-07-21 | 2023-01-05 | 78,11 $ | 66,32 $ | +17,77% | da inizio programma |
| 46 | 2026-07-22 | 2023-01-06 | 77,91 $ | 66,78 $ | +16,66% | da inizio programma |
| 47 | 2026-07-23 | 2023-01-07 | 75,86 $ | 66,79 $ | +13,58% | da inizio programma |
| 48 | 2026-07-24 | 2023-01-08 | 73,88 $ | 67,33 $ | +9,73% | da inizio programma |
| 49 | 2026-07-25 | 2023-01-09 | 74,43 $ | 67,74 $ | +9,87% | da inizio programma |
| 50 | 2026-07-26 | 2023-01-10 | 74,43 $ | 68,73 $ | +8,30% | da inizio programma |
| 51 | 2026-07-27 | 2023-01-11 | 76,32 $ | 70,65 $ | +8,03% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-08-03 | 81,50 $ | 88,04 $ | 76,32 $ / 90,09 $ | no | n/a | n/a | n/a |
| 14g | 2026-08-10 | 91,07 $ | 98,38 $ | 76,32 $ / 98,38 $ | no | n/a | n/a | n/a |
| 21g | 2026-08-17 | 93,45 $ | 100,95 $ | 76,32 $ / 101,17 $ | no | n/a | n/a | n/a |
| 28g | 2026-08-24 | 90,36 $ | 97,62 $ | 76,32 $ / 101,17 $ | no | n/a | n/a | n/a |
| 35g | 2026-08-31 | 95,75 $ | 103,44 $ | 76,32 $ / 103,44 $ | no | n/a | n/a | n/a |
| 42g | 2026-09-07 | 95,29 $ | 102,93 $ | 76,32 $ / 105,66 $ | no | n/a | n/a | n/a |
| 49g | 2026-09-14 | 93,15 $ | 100,63 $ | 76,32 $ / 105,66 $ | no | n/a | n/a | n/a |
| 56g | 2026-09-21 | 85,55 $ | 92,42 $ | 76,32 $ / 105,66 $ | no | n/a | n/a | n/a |
| 63g | 2026-09-28 | 96,02 $ | 103,73 $ | 76,32 $ / 105,66 $ | no | n/a | n/a | n/a |
| 70g | 2026-10-05 | 107,57 $ | 116,20 $ | 76,32 $ / 119,90 $ | no | n/a | n/a | n/a |
| 77g | 2026-10-12 | 111,67 $ | 120,63 $ | 76,32 $ / 120,63 $ | no | n/a | n/a | n/a |
| 84g | 2026-10-19 | 111,00 $ | 119,91 $ | 76,32 $ / 121,19 $ | no | n/a | n/a | n/a |
| 91g | 2026-10-26 | 118,72 $ | 128,25 $ | 76,32 $ / 128,66 $ | no | n/a | n/a | n/a |
| 98g | 2026-11-02 | 113,54 $ | 122,65 $ | 76,32 $ / 129,73 $ | no | n/a | n/a | n/a |
| 105g | 2026-11-09 | 111,96 $ | 120,95 $ | 76,32 $ / 129,73 $ | no | n/a | n/a | n/a |
| 112g | 2026-11-16 | 114,26 $ | 123,43 $ | 76,32 $ / 129,73 $ | no | n/a | n/a | n/a |
| 119g | 2026-11-23 | 108,81 $ | 117,54 $ | 76,32 $ / 129,73 $ | no | n/a | n/a | n/a |
| 126g | 2026-11-30 | 107,93 $ | 116,59 $ | 76,32 $ / 129,73 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 13 | 30,77% | 2,59% | 13,33% |
| 14g | 6 | 16,67% | 5,34% | 8,98% |
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
