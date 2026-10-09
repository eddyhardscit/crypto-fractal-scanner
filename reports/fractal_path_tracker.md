<!-- FRACTAL_PATH_TRACKER_START -->
# Tracking percorso frattale SOL/BTC

Generato: 2026-10-09 05:32 UTC

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-10-09**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-03-26**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **110,49 $**
- Verdetto principale: **STRUTTURA ANALOGA, PREZZO NON ADERENTE**
- Somiglianza strutturale: **+73,09%**
- Aderenza live principale: **+69,36%**
- Errore medio live principale: **15,32%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE NON CONFERMATO DAL PREZZO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **125**
- Osservazioni inclusive dal bottom: **126**
- Osservazioni da inizio programma/scanner: **99**
- Errore assoluto medio dal bottom: **13,33%**
- Errore assoluto medio da inizio programma: **15,32%**
- Gap firmato medio ultimi 7 giorni: **+7,74%**
- Errore assoluto medio ultimi 7 giorni: **7,74%**
- Gap ultimo giorno: **+0,19%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **+0,19%**
- Gap firmato medio 7g: **+7,74%**
- Errore assoluto medio 7g: **7,74%**
- Variazione recente gap: **-8,03%**
- Stato gap: **VICINO AL FRATTALE**
- Trend gap: **SOL resta sopra il percorso ancorato, ma sta riducendo il distacco**

Soglie operative del grafico:

- entro **±5%**: percorso vicino;
- tra **±5% e ±12%**: deviazione gestibile;
- oltre **±12%**: frattale non abbastanza aderente per conferma operativa;
- oltre **±18%**: disallineamento marcato.

## Ultimi giorni del confronto ancorato

|   Giorno | Data SOL   | Data BTC eq.   | SOL reale   | Percorso ancorato   | Gap firmato   | Fase                |
|---------:|:-----------|:---------------|:------------|:--------------------|:--------------|:--------------------|
| 116 | 2026-09-30 | 2023-03-17 | 117,99 $ | 108,03 $ | +9,22% | da inizio programma |
| 117 | 2026-10-01 | 2023-03-18 | 118,40 $ | 106,22 $ | +11,46% | da inizio programma |
| 118 | 2026-10-02 | 2023-03-19 | 118,62 $ | 110,45 $ | +7,39% | da inizio programma |
| 119 | 2026-10-03 | 2023-03-20 | 119,65 $ | 109,38 $ | +9,38% | da inizio programma |
| 120 | 2026-10-04 | 2023-03-21 | 121,53 $ | 110,99 $ | +9,49% | da inizio programma |
| 121 | 2026-10-05 | 2023-03-22 | 120,75 $ | 107,57 $ | +12,25% | da inizio programma |
| 122 | 2026-10-06 | 2023-03-23 | 120,79 $ | 111,61 $ | +8,22% | da inizio programma |
| 123 | 2026-10-07 | 2023-03-24 | 116,22 $ | 108,30 $ | +7,31% | da inizio programma |
| 124 | 2026-10-08 | 2023-03-25 | 116,22 $ | 108,31 $ | +7,31% | da inizio programma |
| 125 | 2026-10-09 | 2023-03-26 | 110,49 $ | 110,28 $ | +0,19% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-10-16 | 111,08 $ | 111,30 $ | 107,12 $ / 112,40 $ | no | n/a | n/a | n/a |
| 14g | 2026-10-23 | 111,61 $ | 111,83 $ | 107,12 $ / 112,40 $ | no | n/a | n/a | n/a |
| 21g | 2026-10-30 | 119,42 $ | 119,65 $ | 107,12 $ / 120,32 $ | no | n/a | n/a | n/a |
| 28g | 2026-11-06 | 108,69 $ | 108,90 $ | 107,12 $ / 120,32 $ | no | n/a | n/a | n/a |
| 35g | 2026-11-13 | 115,30 $ | 115,52 $ | 107,12 $ / 120,32 $ | no | n/a | n/a | n/a |
| 42g | 2026-11-20 | 112,09 $ | 112,31 $ | 107,12 $ / 120,32 $ | no | n/a | n/a | n/a |
| 49g | 2026-11-27 | 106,09 $ | 106,29 $ | 105,71 $ / 120,32 $ | no | n/a | n/a | n/a |
| 56g | 2026-12-04 | 105,39 $ | 105,59 $ | 105,59 $ / 120,32 $ | no | n/a | n/a | n/a |
| 63g | 2026-12-11 | 110,64 $ | 110,85 $ | 103,94 $ / 120,32 $ | no | n/a | n/a | n/a |
| 70g | 2026-12-18 | 106,83 $ | 107,04 $ | 103,94 $ / 120,32 $ | no | n/a | n/a | n/a |
| 77g | 2026-12-25 | 102,18 $ | 102,38 $ | 101,67 $ / 120,32 $ | no | n/a | n/a | n/a |
| 84g | 2027-01-01 | 103,74 $ | 103,95 $ | 99,16 $ / 120,32 $ | no | n/a | n/a | n/a |
| 91g | 2027-01-08 | 120,07 $ | 120,30 $ | 99,16 $ / 121,15 $ | no | n/a | n/a | n/a |
| 98g | 2027-01-15 | 120,62 $ | 120,86 $ | 99,16 $ / 121,15 $ | no | n/a | n/a | n/a |
| 105g | 2027-01-22 | 118,85 $ | 119,08 $ | 99,16 $ / 122,97 $ | no | n/a | n/a | n/a |
| 112g | 2027-01-29 | 119,16 $ | 119,39 $ | 99,16 $ / 124,23 $ | no | n/a | n/a | n/a |
| 119g | 2027-02-05 | 118,51 $ | 118,74 $ | 99,16 $ / 124,23 $ | no | n/a | n/a | n/a |
| 126g | 2027-02-12 | 115,32 $ | 115,55 $ | 99,16 $ / 124,23 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 80 | 38,75% | 11,75% | 14,24% |
| 14g | 74 | 25,68% | 17,57% | 14,59% |
| 21g | 70 | 28,57% | 20,75% | 15,76% |
| 28g | 64 | 28,12% | 21,68% | 15,63% |
| 35g | 57 | 35,09% | 22,86% | 15,40% |
| 42g | 50 | 48,00% | 21,76% | 14,25% |
| 49g | 43 | 48,84% | 24,19% | 16,38% |
| 56g | 36 | 44,44% | 22,29% | 17,38% |
| 63g | 31 | 35,48% | 16,69% | 18,80% |
| 70g | 24 | 41,67% | 10,35% | 21,55% |
| 77g | 17 | 58,82% | 9,09% | 14,60% |
| 84g | 10 | 100,00% | 7,13% | 7,69% |
| 91g | 3 | 100,00% | 10,69% | 0,19% |
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
