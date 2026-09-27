<!-- FRACTAL_PATH_TRACKER_START -->
# Tracking percorso frattale SOL/BTC

Generato: 2026-09-27 05:32 UTC

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-09-27**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-03-14**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **120,68 $**
- Verdetto principale: **STRUTTURA ANALOGA, PREZZO NON ADERENTE**
- Somiglianza strutturale: **+70,86%**
- Aderenza live principale: **+68,07%**
- Errore medio live principale: **15,97%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE NON CONFERMATO DAL PREZZO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **113**
- Osservazioni inclusive dal bottom: **114**
- Osservazioni da inizio programma/scanner: **87**
- Errore assoluto medio dal bottom: **13,61%**
- Errore assoluto medio da inizio programma: **15,97%**
- Gap firmato medio ultimi 7 giorni: **+38,09%**
- Errore assoluto medio ultimi 7 giorni: **38,09%**
- Gap ultimo giorno: **+23,80%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **+23,80%**
- Gap firmato medio 7g: **+38,09%**
- Errore assoluto medio 7g: **38,09%**
- Variazione recente gap: **-20,17%**
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
| 104 | 2026-09-18 | 2023-03-05 | 112,60 $ | 88,38 $ | +27,41% | da inizio programma |
| 105 | 2026-09-19 | 2023-03-06 | 111,01 $ | 88,36 $ | +25,64% | da inizio programma |
| 106 | 2026-09-20 | 2023-03-07 | 111,13 $ | 87,53 $ | +26,97% | da inizio programma |
| 107 | 2026-09-21 | 2023-03-08 | 118,75 $ | 85,55 $ | +38,80% | da inizio programma |
| 108 | 2026-09-22 | 2023-03-09 | 118,51 $ | 80,21 $ | +47,74% | da inizio programma |
| 109 | 2026-09-23 | 2023-03-10 | 114,98 $ | 79,52 $ | +44,58% | da inizio programma |
| 110 | 2026-09-24 | 2023-03-11 | 117,01 $ | 81,28 $ | +43,97% | da inizio programma |
| 111 | 2026-09-25 | 2023-03-12 | 122,01 $ | 87,31 $ | +39,74% | da inizio programma |
| 112 | 2026-09-26 | 2023-03-13 | 122,01 $ | 95,32 $ | +28,00% | da inizio programma |
| 113 | 2026-09-27 | 2023-03-14 | 120,68 $ | 97,48 $ | +23,80% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-10-04 | 110,99 $ | 137,41 $ | 118,88 $ / 137,41 $ | no | n/a | n/a | n/a |
| 14g | 2026-10-11 | 107,42 $ | 132,98 $ | 118,88 $ / 138,18 $ | no | n/a | n/a | n/a |
| 21g | 2026-10-18 | 110,96 $ | 137,37 $ | 118,88 $ / 138,88 $ | no | n/a | n/a | n/a |
| 28g | 2026-10-25 | 119,10 $ | 147,45 $ | 118,88 $ / 147,45 $ | no | n/a | n/a | n/a |
| 35g | 2026-11-01 | 119,74 $ | 148,24 $ | 118,88 $ / 148,67 $ | no | n/a | n/a | n/a |
| 42g | 2026-11-08 | 111,51 $ | 138,05 $ | 118,88 $ / 148,67 $ | no | n/a | n/a | n/a |
| 49g | 2026-11-15 | 112,98 $ | 139,87 $ | 118,88 $ / 148,67 $ | no | n/a | n/a | n/a |
| 56g | 2026-11-22 | 108,95 $ | 134,88 $ | 118,88 $ / 148,67 $ | no | n/a | n/a | n/a |
| 63g | 2026-11-29 | 106,50 $ | 131,85 $ | 118,88 $ / 148,67 $ | no | n/a | n/a | n/a |
| 70g | 2026-12-06 | 107,25 $ | 132,77 $ | 118,88 $ / 148,67 $ | no | n/a | n/a | n/a |
| 77g | 2026-12-13 | 109,13 $ | 135,10 $ | 118,88 $ / 148,67 $ | no | n/a | n/a | n/a |
| 84g | 2026-12-20 | 107,30 $ | 132,84 $ | 118,88 $ / 148,67 $ | no | n/a | n/a | n/a |
| 91g | 2026-12-27 | 102,10 $ | 126,40 $ | 118,88 $ / 148,67 $ | no | n/a | n/a | n/a |
| 98g | 2027-01-03 | 111,59 $ | 138,15 $ | 118,88 $ / 148,67 $ | no | n/a | n/a | n/a |
| 105g | 2027-01-10 | 120,89 $ | 149,66 $ | 118,88 $ / 149,69 $ | no | n/a | n/a | n/a |
| 112g | 2027-01-17 | 121,24 $ | 150,09 $ | 118,88 $ / 151,94 $ | no | n/a | n/a | n/a |
| 119g | 2027-01-24 | 120,62 $ | 149,33 $ | 118,88 $ / 151,94 $ | no | n/a | n/a | n/a |
| 126g | 2027-01-31 | 117,61 $ | 145,60 $ | 118,88 $ / 153,50 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 70 | 35,71% | 11,38% | 14,93% |
| 14g | 66 | 22,73% | 17,68% | 15,03% |
| 21g | 59 | 22,03% | 23,91% | 16,57% |
| 28g | 52 | 21,15% | 25,47% | 16,83% |
| 35g | 45 | 28,89% | 27,08% | 16,73% |
| 42g | 38 | 52,63% | 22,72% | 15,46% |
| 49g | 33 | 60,61% | 22,23% | 18,22% |
| 56g | 26 | 61,54% | 18,46% | 19,92% |
| 63g | 19 | 57,89% | 12,57% | 24,58% |
| 70g | 12 | 50,00% | 13,50% | 34,67% |
| 77g | 5 | 0,00% | 16,00% | 30,51% |
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
