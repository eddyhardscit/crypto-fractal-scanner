<!-- FRACTAL_PATH_TRACKER_START -->
# Tracking percorso frattale SOL/BTC

Generato: 2026-09-25 23:50 UTC

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-09-25**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-03-12**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **122,13 $**
- Verdetto principale: **STRUTTURA ANALOGA, PREZZO NON ADERENTE**
- Somiglianza strutturale: **+69,17%**
- Aderenza live principale: **+68,53%**
- Errore medio live principale: **15,73%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE NON CONFERMATO DAL PREZZO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **111**
- Osservazioni inclusive dal bottom: **112**
- Osservazioni da inizio programma/scanner: **85**
- Errore assoluto medio dal bottom: **13,39%**
- Errore assoluto medio da inizio programma: **15,73%**
- Gap firmato medio ultimi 7 giorni: **+38,23%**
- Errore assoluto medio ultimi 7 giorni: **38,23%**
- Gap ultimo giorno: **+39,88%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **+39,88%**
- Gap firmato medio 7g: **+38,23%**
- Errore assoluto medio 7g: **38,23%**
- Variazione recente gap: **-7,86%**
- Stato gap: **DISALLINEATO SOPRA IL FRATTALE**
- Trend gap: **SOL resta sopra il percorso ancorato, ma sta riducendo il distacco**

Soglie operative del grafico:

- entro **±5%**: percorso vicino;
- tra **±5% e ±12%**: deviazione gestibile;
- oltre **±12%**: frattale non abbastanza aderente per conferma operativa;
- oltre **±18%**: disallineamento marcato.

## Ultimi giorni del confronto ancorato

|   Giorno | Data SOL   | Data BTC eq.   | SOL reale   | Percorso ancorato   | Gap firmato   | Fase                |
|---------:|:-----------|:---------------|:------------|:--------------------|:--------------|:--------------------|
| 102 | 2026-09-16 | 2023-03-03 | 98,64 $ | 88,09 $ | +11,98% | da inizio programma |
| 103 | 2026-09-17 | 2023-03-04 | 101,60 $ | 88,06 $ | +15,39% | da inizio programma |
| 104 | 2026-09-18 | 2023-03-05 | 112,60 $ | 88,38 $ | +27,41% | da inizio programma |
| 105 | 2026-09-19 | 2023-03-06 | 111,01 $ | 88,36 $ | +25,64% | da inizio programma |
| 106 | 2026-09-20 | 2023-03-07 | 111,13 $ | 87,53 $ | +26,97% | da inizio programma |
| 107 | 2026-09-21 | 2023-03-08 | 118,75 $ | 85,55 $ | +38,80% | da inizio programma |
| 108 | 2026-09-22 | 2023-03-09 | 118,51 $ | 80,21 $ | +47,74% | da inizio programma |
| 109 | 2026-09-23 | 2023-03-10 | 114,98 $ | 79,52 $ | +44,58% | da inizio programma |
| 110 | 2026-09-24 | 2023-03-11 | 117,01 $ | 81,28 $ | +43,97% | da inizio programma |
| 111 | 2026-09-25 | 2023-03-12 | 122,13 $ | 87,31 $ | +39,88% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-10-02 | 110,45 $ | 154,50 $ | 122,13 $ / 154,50 $ | no | n/a | n/a | n/a |
| 14g | 2026-10-09 | 110,28 $ | 154,26 $ | 122,13 $ / 156,13 $ | no | n/a | n/a | n/a |
| 21g | 2026-10-16 | 111,08 $ | 155,39 $ | 122,13 $ / 156,92 $ | no | n/a | n/a | n/a |
| 28g | 2026-10-23 | 111,61 $ | 156,12 $ | 122,13 $ / 156,92 $ | no | n/a | n/a | n/a |
| 35g | 2026-10-30 | 119,42 $ | 167,05 $ | 122,13 $ / 167,99 $ | no | n/a | n/a | n/a |
| 42g | 2026-11-06 | 108,69 $ | 152,04 $ | 122,13 $ / 167,99 $ | no | n/a | n/a | n/a |
| 49g | 2026-11-13 | 115,30 $ | 161,28 $ | 122,13 $ / 167,99 $ | no | n/a | n/a | n/a |
| 56g | 2026-11-20 | 112,09 $ | 156,80 $ | 122,13 $ / 167,99 $ | no | n/a | n/a | n/a |
| 63g | 2026-11-27 | 106,09 $ | 148,40 $ | 122,13 $ / 167,99 $ | no | n/a | n/a | n/a |
| 70g | 2026-12-04 | 105,39 $ | 147,42 $ | 122,13 $ / 167,99 $ | no | n/a | n/a | n/a |
| 77g | 2026-12-11 | 110,64 $ | 154,76 $ | 122,13 $ / 167,99 $ | no | n/a | n/a | n/a |
| 84g | 2026-12-18 | 106,83 $ | 149,43 $ | 122,13 $ / 167,99 $ | no | n/a | n/a | n/a |
| 91g | 2026-12-25 | 102,18 $ | 142,94 $ | 122,13 $ / 167,99 $ | no | n/a | n/a | n/a |
| 98g | 2027-01-01 | 103,74 $ | 145,12 $ | 122,13 $ / 167,99 $ | no | n/a | n/a | n/a |
| 105g | 2027-01-08 | 120,07 $ | 167,96 $ | 122,13 $ / 169,14 $ | no | n/a | n/a | n/a |
| 112g | 2027-01-15 | 120,62 $ | 168,73 $ | 122,13 $ / 169,14 $ | no | n/a | n/a | n/a |
| 119g | 2027-01-22 | 118,85 $ | 166,25 $ | 122,13 $ / 171,68 $ | no | n/a | n/a | n/a |
| 126g | 2027-01-29 | 119,16 $ | 166,68 $ | 122,13 $ / 173,44 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 70 | 35,71% | 11,38% | 14,93% |
| 14g | 64 | 23,44% | 17,80% | 14,68% |
| 21g | 57 | 22,81% | 24,15% | 16,23% |
| 28g | 50 | 22,00% | 26,31% | 16,45% |
| 35g | 43 | 30,23% | 27,31% | 16,29% |
| 42g | 36 | 55,56% | 21,14% | 14,85% |
| 49g | 31 | 64,52% | 20,44% | 17,69% |
| 56g | 24 | 66,67% | 16,40% | 19,38% |
| 63g | 17 | 64,71% | 12,28% | 24,41% |
| 70g | 10 | 60,00% | 14,28% | 36,87% |
| 77g | 3 | 0,00% | 21,37% | 39,88% |
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
