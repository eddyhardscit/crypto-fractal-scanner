<!-- FRACTAL_PATH_TRACKER_START -->
# Tracking percorso frattale SOL/BTC

Generato: 2026-09-22 05:32 UTC

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-09-22**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-03-09**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **115,88 $**
- Verdetto principale: **STRUTTURA ANALOGA, PREZZO NON ADERENTE**
- Somiglianza strutturale: **+70,10%**
- Aderenza live principale: **+70,81%**
- Errore medio live principale: **14,59%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE NON CONFERMATO DAL PREZZO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **108**
- Osservazioni inclusive dal bottom: **109**
- Osservazioni da inizio programma/scanner: **82**
- Errore assoluto medio dal bottom: **12,47%**
- Errore assoluto medio da inizio programma: **14,59%**
- Gap firmato medio ultimi 7 giorni: **+25,96%**
- Errore assoluto medio ultimi 7 giorni: **25,96%**
- Gap ultimo giorno: **+44,46%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **+44,46%**
- Gap firmato medio 7g: **+25,96%**
- Errore assoluto medio 7g: **25,96%**
- Variazione recente gap: **+18,82%**
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
| 99 | 2026-09-13 | 2023-02-28 | 99,25 $ | 91,18 $ | +8,84% | da inizio programma |
| 100 | 2026-09-14 | 2023-03-01 | 102,50 $ | 93,15 $ | +10,03% | da inizio programma |
| 101 | 2026-09-15 | 2023-03-02 | 96,89 $ | 92,48 $ | +4,77% | da inizio programma |
| 102 | 2026-09-16 | 2023-03-03 | 98,64 $ | 88,09 $ | +11,98% | da inizio programma |
| 103 | 2026-09-17 | 2023-03-04 | 101,60 $ | 88,06 $ | +15,39% | da inizio programma |
| 104 | 2026-09-18 | 2023-03-05 | 112,60 $ | 88,38 $ | +27,41% | da inizio programma |
| 105 | 2026-09-19 | 2023-03-06 | 111,01 $ | 88,36 $ | +25,64% | da inizio programma |
| 106 | 2026-09-20 | 2023-03-07 | 111,13 $ | 87,53 $ | +26,97% | da inizio programma |
| 107 | 2026-09-21 | 2023-03-08 | 111,13 $ | 85,55 $ | +29,90% | da inizio programma |
| 108 | 2026-09-22 | 2023-03-09 | 115,88 $ | 80,21 $ | +44,46% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-09-29 | 98,69 $ | 142,57 $ | 114,88 $ / 142,57 $ | no | n/a | n/a | n/a |
| 14g | 2026-10-06 | 111,61 $ | 161,24 $ | 114,88 $ / 161,24 $ | no | n/a | n/a | n/a |
| 21g | 2026-10-13 | 110,43 $ | 159,53 $ | 114,88 $ / 161,32 $ | no | n/a | n/a | n/a |
| 28g | 2026-10-20 | 110,47 $ | 159,59 $ | 114,88 $ / 162,06 $ | no | n/a | n/a | n/a |
| 35g | 2026-10-27 | 119,75 $ | 172,99 $ | 114,88 $ / 172,99 $ | no | n/a | n/a | n/a |
| 42g | 2026-11-03 | 111,27 $ | 160,74 $ | 114,88 $ / 173,49 $ | no | n/a | n/a | n/a |
| 49g | 2026-11-10 | 116,10 $ | 167,73 $ | 114,88 $ / 173,49 $ | no | n/a | n/a | n/a |
| 56g | 2026-11-17 | 113,64 $ | 164,16 $ | 114,88 $ / 173,49 $ | no | n/a | n/a | n/a |
| 63g | 2026-11-24 | 106,36 $ | 153,65 $ | 114,88 $ / 173,49 $ | no | n/a | n/a | n/a |
| 70g | 2026-12-01 | 105,70 $ | 152,69 $ | 114,88 $ / 173,49 $ | no | n/a | n/a | n/a |
| 77g | 2026-12-08 | 104,30 $ | 150,67 $ | 114,88 $ / 173,49 $ | no | n/a | n/a | n/a |
| 84g | 2026-12-15 | 105,65 $ | 152,62 $ | 114,88 $ / 173,49 $ | no | n/a | n/a | n/a |
| 91g | 2026-12-22 | 104,42 $ | 150,85 $ | 114,88 $ / 173,49 $ | no | n/a | n/a | n/a |
| 98g | 2026-12-29 | 100,75 $ | 145,55 $ | 114,88 $ / 173,49 $ | no | n/a | n/a | n/a |
| 105g | 2027-01-05 | 117,83 $ | 170,22 $ | 114,88 $ / 173,49 $ | no | n/a | n/a | n/a |
| 112g | 2027-01-12 | 119,93 $ | 173,26 $ | 114,88 $ / 174,68 $ | no | n/a | n/a | n/a |
| 119g | 2027-01-19 | 117,82 $ | 170,21 $ | 114,88 $ / 177,30 $ | no | n/a | n/a | n/a |
| 126g | 2027-01-26 | 123,99 $ | 179,12 $ | 114,88 $ / 179,12 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 68 | 36,76% | 10,69% | 13,85% |
| 14g | 61 | 24,59% | 17,09% | 13,04% |
| 21g | 54 | 24,07% | 23,27% | 14,47% |
| 28g | 47 | 25,53% | 26,41% | 14,42% |
| 35g | 40 | 32,50% | 24,72% | 13,88% |
| 42g | 35 | 57,14% | 19,22% | 13,72% |
| 49g | 28 | 71,43% | 14,23% | 14,32% |
| 56g | 21 | 76,19% | 10,00% | 15,04% |
| 63g | 14 | 85,71% | 8,93% | 18,80% |
| 70g | 7 | 85,71% | 9,21% | 30,88% |
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
