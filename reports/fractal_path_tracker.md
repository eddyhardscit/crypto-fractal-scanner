<!-- FRACTAL_PATH_TRACKER_START -->
# Tracking percorso frattale SOL/BTC

Generato: 2026-10-02 14:07 UTC

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-10-02**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-03-19**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **122,43 $**
- Verdetto principale: **STRUTTURA ANALOGA, PREZZO NON ADERENTE**
- Somiglianza strutturale: **+71,48%**
- Aderenza live principale: **+68,14%**
- Errore medio live principale: **15,93%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE NON CONFERMATO DAL PREZZO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **118**
- Osservazioni inclusive dal bottom: **119**
- Osservazioni da inizio programma/scanner: **92**
- Errore assoluto medio dal bottom: **13,68%**
- Errore assoluto medio da inizio programma: **15,93%**
- Gap firmato medio ultimi 7 giorni: **+18,36%**
- Errore assoluto medio ultimi 7 giorni: **18,36%**
- Gap ultimo giorno: **+10,85%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **+10,85%**
- Gap firmato medio 7g: **+18,36%**
- Errore assoluto medio 7g: **18,36%**
- Variazione recente gap: **-9,79%**
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
| 109 | 2026-09-23 | 2023-03-10 | 114,98 $ | 79,52 $ | +44,58% | da inizio programma |
| 110 | 2026-09-24 | 2023-03-11 | 117,01 $ | 81,28 $ | +43,97% | da inizio programma |
| 111 | 2026-09-25 | 2023-03-12 | 122,01 $ | 87,31 $ | +39,74% | da inizio programma |
| 112 | 2026-09-26 | 2023-03-13 | 121,43 $ | 95,32 $ | +27,39% | da inizio programma |
| 113 | 2026-09-27 | 2023-03-14 | 122,06 $ | 97,48 $ | +25,21% | da inizio programma |
| 114 | 2026-09-28 | 2023-03-15 | 118,84 $ | 96,02 $ | +23,76% | da inizio programma |
| 115 | 2026-09-29 | 2023-03-16 | 119,06 $ | 98,69 $ | +20,64% | da inizio programma |
| 116 | 2026-09-30 | 2023-03-17 | 117,99 $ | 108,03 $ | +9,22% | da inizio programma |
| 117 | 2026-10-01 | 2023-03-18 | 118,40 $ | 106,22 $ | +11,46% | da inizio programma |
| 118 | 2026-10-02 | 2023-03-19 | 122,43 $ | 110,45 $ | +10,85% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-10-09 | 110,28 $ | 122,24 $ | 119,24 $ / 123,72 $ | no | n/a | n/a | n/a |
| 14g | 2026-10-16 | 111,08 $ | 123,13 $ | 118,51 $ / 124,35 $ | no | n/a | n/a | n/a |
| 21g | 2026-10-23 | 111,61 $ | 123,72 $ | 118,51 $ / 124,35 $ | no | n/a | n/a | n/a |
| 28g | 2026-10-30 | 119,42 $ | 132,37 $ | 118,51 $ / 133,11 $ | no | n/a | n/a | n/a |
| 35g | 2026-11-06 | 108,69 $ | 120,48 $ | 118,51 $ / 133,11 $ | no | n/a | n/a | n/a |
| 42g | 2026-11-13 | 115,30 $ | 127,80 $ | 118,51 $ / 133,11 $ | no | n/a | n/a | n/a |
| 49g | 2026-11-20 | 112,09 $ | 124,25 $ | 118,51 $ / 133,11 $ | no | n/a | n/a | n/a |
| 56g | 2026-11-27 | 106,09 $ | 117,59 $ | 116,95 $ / 133,11 $ | no | n/a | n/a | n/a |
| 63g | 2026-12-04 | 105,39 $ | 116,82 $ | 116,82 $ / 133,11 $ | no | n/a | n/a | n/a |
| 70g | 2026-12-11 | 110,64 $ | 122,64 $ | 114,99 $ / 133,11 $ | no | n/a | n/a | n/a |
| 77g | 2026-12-18 | 106,83 $ | 118,41 $ | 114,99 $ / 133,11 $ | no | n/a | n/a | n/a |
| 84g | 2026-12-25 | 102,18 $ | 113,27 $ | 112,48 $ / 133,11 $ | no | n/a | n/a | n/a |
| 91g | 2027-01-01 | 103,74 $ | 115,00 $ | 109,71 $ / 133,11 $ | no | n/a | n/a | n/a |
| 98g | 2027-01-08 | 120,07 $ | 133,09 $ | 109,71 $ / 134,03 $ | no | n/a | n/a | n/a |
| 105g | 2027-01-15 | 120,62 $ | 133,70 $ | 109,71 $ / 134,03 $ | no | n/a | n/a | n/a |
| 112g | 2027-01-22 | 118,85 $ | 131,74 $ | 109,71 $ / 136,04 $ | no | n/a | n/a | n/a |
| 119g | 2027-01-29 | 119,16 $ | 132,08 $ | 109,71 $ / 137,44 $ | no | n/a | n/a | n/a |
| 126g | 2027-02-05 | 118,51 $ | 131,36 $ | 109,71 $ / 137,44 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 74 | 39,19% | 11,91% | 14,82% |
| 14g | 70 | 24,29% | 17,07% | 15,11% |
| 21g | 64 | 23,44% | 22,52% | 16,47% |
| 28g | 57 | 19,30% | 23,94% | 16,69% |
| 35g | 50 | 32,00% | 25,17% | 16,59% |
| 42g | 43 | 46,51% | 23,93% | 15,45% |
| 49g | 36 | 55,56% | 23,99% | 18,26% |
| 56g | 31 | 51,61% | 21,24% | 19,13% |
| 63g | 24 | 45,83% | 14,24% | 22,48% |
| 70g | 17 | 52,94% | 10,85% | 28,23% |
| 77g | 10 | 30,00% | 10,63% | 21,03% |
| 84g | 3 | 100,00% | 5,32% | 10,85% |
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
