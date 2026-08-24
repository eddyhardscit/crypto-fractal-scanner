<!-- FRACTAL_PATH_TRACKER_START -->
# Tracking percorso frattale SOL/BTC

Generato: 2026-08-24 05:32 UTC

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-08-24**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-02-08**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **94,05 $**
- Verdetto principale: **ANALOGIA DEBOLE / SCENARIO SECONDARIO**
- Somiglianza strutturale: **+63,62%**
- Aderenza live principale: **+71,37%**
- Errore medio live principale: **14,32%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE SOLO DI CONTESTO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **79**
- Osservazioni inclusive dal bottom: **80**
- Osservazioni da inizio programma/scanner: **53**
- Errore assoluto medio dal bottom: **11,52%**
- Errore assoluto medio da inizio programma: **14,32%**
- Gap firmato medio ultimi 7 giorni: **-2,01%**
- Errore assoluto medio ultimi 7 giorni: **6,25%**
- Gap ultimo giorno: **+4,08%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **+4,08%**
- Gap firmato medio 7g: **-2,01%**
- Errore assoluto medio 7g: **6,25%**
- Variazione recente gap: **+0,51%**
- Stato gap: **VICINO AL FRATTALE**
- Trend gap: **SOL resta sopra il percorso ancorato con distacco quasi stabile**

Soglie operative del grafico:

- entro **±5%**: percorso vicino;
- tra **±5% e ±12%**: deviazione gestibile;
- oltre **±12%**: frattale non abbastanza aderente per conferma operativa;
- oltre **±18%**: disallineamento marcato.

## Ultimi giorni del confronto ancorato

|   Giorno | Data SOL   | Data BTC eq.   | SOL reale   | Percorso ancorato   | Gap firmato   | Fase                |
|---------:|:-----------|:---------------|:------------|:--------------------|:--------------|:--------------------|
| 70 | 2026-08-15 | 2023-01-30 | 75,27 $ | 89,97 $ | -16,34% | da inizio programma |
| 71 | 2026-08-16 | 2023-01-31 | 74,54 $ | 91,15 $ | -18,22% | da inizio programma |
| 72 | 2026-08-17 | 2023-02-01 | 75,94 $ | 93,45 $ | -18,74% | da inizio programma |
| 73 | 2026-08-18 | 2023-02-02 | 77,03 $ | 92,46 $ | -16,69% | da inizio programma |
| 74 | 2026-08-19 | 2023-02-03 | 85,37 $ | 92,37 $ | -7,58% | da inizio programma |
| 75 | 2026-08-20 | 2023-02-04 | 87,64 $ | 91,91 $ | -4,65% | da inizio programma |
| 76 | 2026-08-21 | 2023-02-05 | 93,65 $ | 90,43 $ | +3,57% | da inizio programma |
| 77 | 2026-08-22 | 2023-02-06 | 93,91 $ | 89,66 $ | +4,75% | da inizio programma |
| 78 | 2026-08-23 | 2023-02-07 | 93,91 $ | 91,64 $ | +2,48% | da inizio programma |
| 79 | 2026-08-24 | 2023-02-08 | 94,05 $ | 90,36 $ | +4,08% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-08-31 | 95,75 $ | 99,66 $ | 88,77 $ / 99,66 $ | no | n/a | n/a | n/a |
| 14g | 2026-09-07 | 95,29 $ | 99,17 $ | 88,77 $ / 101,80 $ | no | n/a | n/a | n/a |
| 21g | 2026-09-14 | 93,15 $ | 96,95 $ | 88,77 $ / 101,80 $ | no | n/a | n/a | n/a |
| 28g | 2026-09-21 | 85,55 $ | 89,04 $ | 88,77 $ / 101,80 $ | no | n/a | n/a | n/a |
| 35g | 2026-09-28 | 96,02 $ | 99,94 $ | 82,77 $ / 101,80 $ | no | n/a | n/a | n/a |
| 42g | 2026-10-05 | 107,57 $ | 111,96 $ | 82,77 $ / 115,52 $ | no | n/a | n/a | n/a |
| 49g | 2026-10-12 | 111,67 $ | 116,23 $ | 82,77 $ / 116,23 $ | no | n/a | n/a | n/a |
| 56g | 2026-10-19 | 111,00 $ | 115,53 $ | 82,77 $ / 116,76 $ | no | n/a | n/a | n/a |
| 63g | 2026-10-26 | 118,72 $ | 123,57 $ | 82,77 $ / 123,96 $ | no | n/a | n/a | n/a |
| 70g | 2026-11-02 | 113,54 $ | 118,17 $ | 82,77 $ / 124,99 $ | no | n/a | n/a | n/a |
| 77g | 2026-11-09 | 111,96 $ | 116,53 $ | 82,77 $ / 124,99 $ | no | n/a | n/a | n/a |
| 84g | 2026-11-16 | 114,26 $ | 118,92 $ | 82,77 $ / 124,99 $ | no | n/a | n/a | n/a |
| 91g | 2026-11-23 | 108,81 $ | 113,25 $ | 82,77 $ / 124,99 $ | no | n/a | n/a | n/a |
| 98g | 2026-11-30 | 107,93 $ | 112,33 $ | 82,77 $ / 124,99 $ | no | n/a | n/a | n/a |
| 105g | 2026-12-07 | 103,74 $ | 107,97 $ | 82,77 $ / 124,99 $ | no | n/a | n/a | n/a |
| 112g | 2026-12-14 | 107,22 $ | 111,60 $ | 82,77 $ / 124,99 $ | no | n/a | n/a | n/a |
| 119g | 2026-12-21 | 103,78 $ | 108,02 $ | 82,77 $ / 124,99 $ | no | n/a | n/a | n/a |
| 126g | 2026-12-28 | 98,97 $ | 103,01 $ | 82,77 $ / 124,99 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 39 | 41,03% | 8,89% | 12,87% |
| 14g | 34 | 32,35% | 16,37% | 11,81% |
| 21g | 27 | 22,22% | 22,75% | 13,00% |
| 28g | 20 | 55,00% | 23,24% | 12,80% |
| 35g | 13 | 61,54% | 21,79% | 10,60% |
| 42g | 6 | 100,00% | 13,52% | 3,72% |
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
