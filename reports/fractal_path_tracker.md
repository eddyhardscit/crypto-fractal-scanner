<!-- FRACTAL_PATH_TRACKER_START -->
# Tracking percorso frattale SOL/BTC

Generato: 2026-09-16 05:32 UTC

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-09-16**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-03-03**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **97,07 $**
- Verdetto principale: **ANALOGIA DEBOLE / SCENARIO SECONDARIO**
- Somiglianza strutturale: **+70,74%**
- Aderenza live principale: **+72,86%**
- Errore medio live principale: **13,57%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE SOLO DI CONTESTO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **102**
- Osservazioni inclusive dal bottom: **103**
- Osservazioni da inizio programma/scanner: **76**
- Errore assoluto medio dal bottom: **11,59%**
- Errore assoluto medio da inizio programma: **13,57%**
- Gap firmato medio ultimi 7 giorni: **+9,74%**
- Errore assoluto medio ultimi 7 giorni: **9,74%**
- Gap ultimo giorno: **+10,19%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **+10,19%**
- Gap firmato medio 7g: **+9,74%**
- Errore assoluto medio 7g: **9,74%**
- Variazione recente gap: **+1,35%**
- Stato gap: **SOPRA IL FRATTALE**
- Trend gap: **SOL sta aumentando il distacco sopra il percorso ancorato**

Soglie operative del grafico:

- entro **±5%**: percorso vicino;
- tra **±5% e ±12%**: deviazione gestibile;
- oltre **±12%**: frattale non abbastanza aderente per conferma operativa;
- oltre **±18%**: disallineamento marcato.

## Ultimi giorni del confronto ancorato

|   Giorno | Data SOL   | Data BTC eq.   | SOL reale   | Percorso ancorato   | Gap firmato   | Fase                |
|---------:|:-----------|:---------------|:------------|:--------------------|:--------------|:--------------------|
| 93 | 2026-09-07 | 2023-02-22 | 103,87 $ | 95,29 $ | +9,01% | da inizio programma |
| 94 | 2026-09-08 | 2023-02-23 | 103,33 $ | 94,33 $ | +9,53% | da inizio programma |
| 95 | 2026-09-09 | 2023-02-24 | 101,61 $ | 91,38 $ | +11,19% | da inizio programma |
| 96 | 2026-09-10 | 2023-02-25 | 98,69 $ | 91,29 $ | +8,10% | da inizio programma |
| 97 | 2026-09-11 | 2023-02-26 | 102,40 $ | 92,81 $ | +10,33% | da inizio programma |
| 98 | 2026-09-12 | 2023-02-27 | 101,79 $ | 92,66 $ | +9,85% | da inizio programma |
| 99 | 2026-09-13 | 2023-02-28 | 99,25 $ | 91,18 $ | +8,84% | da inizio programma |
| 100 | 2026-09-14 | 2023-03-01 | 102,50 $ | 93,15 $ | +10,03% | da inizio programma |
| 101 | 2026-09-15 | 2023-03-02 | 102,50 $ | 92,48 $ | +10,83% | da inizio programma |
| 102 | 2026-09-16 | 2023-03-03 | 97,07 $ | 88,09 $ | +10,19% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-09-23 | 79,52 $ | 87,63 $ | 87,63 $ / 97,39 $ | no | n/a | n/a | n/a |
| 14g | 2026-09-30 | 108,03 $ | 119,04 $ | 87,63 $ / 119,04 $ | no | n/a | n/a | n/a |
| 21g | 2026-10-07 | 108,30 $ | 119,34 $ | 87,63 $ / 122,99 $ | no | n/a | n/a | n/a |
| 28g | 2026-10-14 | 112,18 $ | 123,62 $ | 87,63 $ / 123,62 $ | no | n/a | n/a | n/a |
| 35g | 2026-10-21 | 110,01 $ | 121,22 $ | 87,63 $ / 123,62 $ | no | n/a | n/a | n/a |
| 42g | 2026-10-28 | 120,09 $ | 132,33 $ | 87,63 $ / 132,33 $ | no | n/a | n/a | n/a |
| 49g | 2026-11-04 | 107,45 $ | 118,40 $ | 87,63 $ / 132,33 $ | no | n/a | n/a | n/a |
| 56g | 2026-11-11 | 115,58 $ | 127,36 $ | 87,63 $ / 132,33 $ | no | n/a | n/a | n/a |
| 63g | 2026-11-18 | 116,34 $ | 128,20 $ | 87,63 $ / 132,33 $ | no | n/a | n/a | n/a |
| 70g | 2026-11-25 | 105,59 $ | 116,35 $ | 87,63 $ / 132,33 $ | no | n/a | n/a | n/a |
| 77g | 2026-12-02 | 105,93 $ | 116,72 $ | 87,63 $ / 132,33 $ | no | n/a | n/a | n/a |
| 84g | 2026-12-09 | 105,25 $ | 115,98 $ | 87,63 $ / 132,33 $ | no | n/a | n/a | n/a |
| 91g | 2026-12-16 | 107,34 $ | 118,28 $ | 87,63 $ / 132,33 $ | no | n/a | n/a | n/a |
| 98g | 2026-12-23 | 104,31 $ | 114,94 $ | 87,63 $ / 132,33 $ | no | n/a | n/a | n/a |
| 105g | 2026-12-30 | 103,71 $ | 114,28 $ | 87,63 $ / 132,33 $ | no | n/a | n/a | n/a |
| 112g | 2027-01-06 | 120,92 $ | 133,24 $ | 87,63 $ / 133,24 $ | no | n/a | n/a | n/a |
| 119g | 2027-01-13 | 120,06 $ | 132,29 $ | 87,63 $ / 133,24 $ | no | n/a | n/a | n/a |
| 126g | 2027-01-20 | 119,53 $ | 131,71 $ | 87,63 $ / 135,24 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 62 | 40,32% | 10,05% | 12,48% |
| 14g | 55 | 29,09% | 16,75% | 11,39% |
| 21g | 48 | 20,83% | 24,76% | 12,75% |
| 28g | 41 | 26,83% | 26,87% | 12,40% |
| 35g | 35 | 37,14% | 19,90% | 11,48% |
| 42g | 29 | 68,97% | 12,15% | 10,64% |
| 49g | 22 | 90,91% | 6,18% | 10,35% |
| 56g | 15 | 100,00% | 6,36% | 9,26% |
| 63g | 8 | 100,00% | 6,47% | 10,01% |
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
