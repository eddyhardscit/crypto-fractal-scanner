<!-- FRACTAL_PATH_TRACKER_START -->
# Tracking percorso frattale SOL/BTC

Generato: 2026-10-13 05:32 UTC

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-10-13**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-03-30**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **108,21 $**
- Verdetto principale: **ANALOGIA DEBOLE / SCENARIO SECONDARIO**
- Somiglianza strutturale: **+73,32%**
- Aderenza live principale: **+70,49%**
- Errore medio live principale: **14,76%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE SOLO DI CONTESTO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **129**
- Osservazioni inclusive dal bottom: **130**
- Osservazioni da inizio programma/scanner: **103**
- Errore assoluto medio dal bottom: **12,94%**
- Errore assoluto medio da inizio programma: **14,76%**
- Gap firmato medio ultimi 7 giorni: **+1,63%**
- Errore assoluto medio ultimi 7 giorni: **2,61%**
- Gap ultimo giorno: **-2,01%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **-2,01%**
- Gap firmato medio 7g: **+1,63%**
- Errore assoluto medio 7g: **2,61%**
- Variazione recente gap: **-4,93%**
- Stato gap: **VICINO AL FRATTALE**
- Trend gap: **SOL si sta allontanando sotto il percorso ancorato**

Soglie operative del grafico:

- entro **±5%**: percorso vicino;
- tra **±5% e ±12%**: deviazione gestibile;
- oltre **±12%**: frattale non abbastanza aderente per conferma operativa;
- oltre **±18%**: disallineamento marcato.

## Ultimi giorni del confronto ancorato

|   Giorno | Data SOL   | Data BTC eq.   | SOL reale   | Percorso ancorato   | Gap firmato   | Fase                |
|---------:|:-----------|:---------------|:------------|:--------------------|:--------------|:--------------------|
| 120 | 2026-10-04 | 2023-03-21 | 121,53 $ | 110,99 $ | +9,49% | da inizio programma |
| 121 | 2026-10-05 | 2023-03-22 | 120,75 $ | 107,57 $ | +12,25% | da inizio programma |
| 122 | 2026-10-06 | 2023-03-23 | 120,79 $ | 111,61 $ | +8,22% | da inizio programma |
| 123 | 2026-10-07 | 2023-03-24 | 116,22 $ | 108,30 $ | +7,31% | da inizio programma |
| 124 | 2026-10-08 | 2023-03-25 | 109,44 $ | 108,31 $ | +1,05% | da inizio programma |
| 125 | 2026-10-09 | 2023-03-26 | 109,14 $ | 110,28 $ | -1,03% | da inizio programma |
| 126 | 2026-10-10 | 2023-03-27 | 110,03 $ | 106,91 $ | +2,92% | da inizio programma |
| 127 | 2026-10-11 | 2023-03-28 | 111,24 $ | 107,42 $ | +3,56% | da inizio programma |
| 128 | 2026-10-12 | 2023-03-29 | 111,24 $ | 111,67 $ | -0,38% | da inizio programma |
| 129 | 2026-10-13 | 2023-03-30 | 108,21 $ | 110,43 $ | -2,01% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-10-20 | 110,47 $ | 108,25 $ | 107,27 $ / 109,93 $ | no | n/a | n/a | n/a |
| 14g | 2026-10-27 | 119,75 $ | 117,34 $ | 107,27 $ / 117,34 $ | no | n/a | n/a | n/a |
| 21g | 2026-11-03 | 111,27 $ | 109,03 $ | 107,27 $ / 117,68 $ | no | n/a | n/a | n/a |
| 28g | 2026-11-10 | 116,10 $ | 113,77 $ | 105,29 $ / 117,68 $ | no | n/a | n/a | n/a |
| 35g | 2026-11-17 | 113,64 $ | 111,35 $ | 105,29 $ / 117,68 $ | no | n/a | n/a | n/a |
| 42g | 2026-11-24 | 106,36 $ | 104,22 $ | 104,22 $ / 117,68 $ | no | n/a | n/a | n/a |
| 49g | 2026-12-01 | 105,70 $ | 103,57 $ | 103,39 $ / 117,68 $ | no | n/a | n/a | n/a |
| 56g | 2026-12-08 | 104,30 $ | 102,20 $ | 101,65 $ / 117,68 $ | no | n/a | n/a | n/a |
| 63g | 2026-12-15 | 105,65 $ | 103,53 $ | 101,65 $ / 117,68 $ | no | n/a | n/a | n/a |
| 70g | 2026-12-22 | 104,42 $ | 102,32 $ | 99,43 $ / 117,68 $ | no | n/a | n/a | n/a |
| 77g | 2026-12-29 | 100,75 $ | 98,73 $ | 96,98 $ / 117,68 $ | no | n/a | n/a | n/a |
| 84g | 2027-01-05 | 117,83 $ | 115,46 $ | 96,98 $ / 117,68 $ | no | n/a | n/a | n/a |
| 91g | 2027-01-12 | 119,93 $ | 117,52 $ | 96,98 $ / 118,48 $ | no | n/a | n/a | n/a |
| 98g | 2027-01-19 | 117,82 $ | 115,45 $ | 96,98 $ / 120,26 $ | no | n/a | n/a | n/a |
| 105g | 2027-01-26 | 123,99 $ | 121,50 $ | 96,98 $ / 121,50 $ | no | n/a | n/a | n/a |
| 112g | 2027-02-02 | 117,36 $ | 115,00 $ | 96,98 $ / 121,50 $ | no | n/a | n/a | n/a |
| 119g | 2027-02-09 | 115,07 $ | 112,75 $ | 96,98 $ / 121,50 $ | no | n/a | n/a | n/a |
| 126g | 2027-02-16 | 114,94 $ | 112,63 $ | 96,98 $ / 121,50 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 84 | 36,90% | 11,57% | 13,66% |
| 14g | 78 | 23,08% | 17,66% | 13,87% |
| 21g | 71 | 28,17% | 20,99% | 15,47% |
| 28g | 68 | 32,35% | 20,97% | 14,73% |
| 35g | 61 | 40,98% | 21,80% | 14,41% |
| 42g | 54 | 51,85% | 21,15% | 13,22% |
| 49g | 47 | 53,19% | 22,50% | 15,00% |
| 56g | 40 | 40,00% | 22,31% | 15,81% |
| 63g | 35 | 31,43% | 16,86% | 16,63% |
| 70g | 28 | 35,71% | 10,59% | 18,37% |
| 77g | 21 | 66,67% | 8,61% | 11,71% |
| 84g | 14 | 100,00% | 9,11% | 5,42% |
| 91g | 7 | 100,00% | 13,80% | 1,98% |
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
