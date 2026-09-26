<!-- FRACTAL_PATH_TRACKER_START -->
# Tracking percorso frattale SOL/BTC

Generato: 2026-09-26 05:32 UTC

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-09-26**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-03-13**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **120,40 $**
- Verdetto principale: **STRUTTURA ANALOGA, PREZZO NON ADERENTE**
- Somiglianza strutturale: **+69,86%**
- Aderenza live principale: **+68,42%**
- Errore medio live principale: **15,79%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE NON CONFERMATO DAL PREZZO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **112**
- Osservazioni inclusive dal bottom: **113**
- Osservazioni da inizio programma/scanner: **86**
- Errore assoluto medio dal bottom: **13,46%**
- Errore assoluto medio da inizio programma: **15,79%**
- Gap firmato medio ultimi 7 giorni: **+37,48%**
- Errore assoluto medio ultimi 7 giorni: **37,48%**
- Gap ultimo giorno: **+26,31%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **+26,31%**
- Gap firmato medio 7g: **+37,48%**
- Errore assoluto medio 7g: **37,48%**
- Variazione recente gap: **-18,27%**
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
| 103 | 2026-09-17 | 2023-03-04 | 101,60 $ | 88,06 $ | +15,39% | da inizio programma |
| 104 | 2026-09-18 | 2023-03-05 | 112,60 $ | 88,38 $ | +27,41% | da inizio programma |
| 105 | 2026-09-19 | 2023-03-06 | 111,01 $ | 88,36 $ | +25,64% | da inizio programma |
| 106 | 2026-09-20 | 2023-03-07 | 111,13 $ | 87,53 $ | +26,97% | da inizio programma |
| 107 | 2026-09-21 | 2023-03-08 | 118,75 $ | 85,55 $ | +38,80% | da inizio programma |
| 108 | 2026-09-22 | 2023-03-09 | 118,51 $ | 80,21 $ | +47,74% | da inizio programma |
| 109 | 2026-09-23 | 2023-03-10 | 114,98 $ | 79,52 $ | +44,58% | da inizio programma |
| 110 | 2026-09-24 | 2023-03-11 | 117,01 $ | 81,28 $ | +43,97% | da inizio programma |
| 111 | 2026-09-25 | 2023-03-12 | 117,01 $ | 87,31 $ | +34,02% | da inizio programma |
| 112 | 2026-09-26 | 2023-03-13 | 120,40 $ | 95,32 $ | +26,31% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-10-03 | 109,38 $ | 138,16 $ | 120,40 $ / 139,51 $ | no | n/a | n/a | n/a |
| 14g | 2026-10-10 | 106,91 $ | 135,04 $ | 120,40 $ / 140,98 $ | no | n/a | n/a | n/a |
| 21g | 2026-10-17 | 109,47 $ | 138,28 $ | 120,40 $ / 141,70 $ | no | n/a | n/a | n/a |
| 28g | 2026-10-24 | 116,81 $ | 147,54 $ | 120,40 $ / 147,54 $ | no | n/a | n/a | n/a |
| 35g | 2026-10-31 | 115,99 $ | 146,51 $ | 120,40 $ / 151,69 $ | no | n/a | n/a | n/a |
| 42g | 2026-11-07 | 108,43 $ | 136,96 $ | 120,40 $ / 151,69 $ | no | n/a | n/a | n/a |
| 49g | 2026-11-14 | 110,66 $ | 139,78 $ | 120,40 $ / 151,69 $ | no | n/a | n/a | n/a |
| 56g | 2026-11-21 | 109,09 $ | 137,80 $ | 120,40 $ / 151,69 $ | no | n/a | n/a | n/a |
| 63g | 2026-11-28 | 107,12 $ | 135,30 $ | 120,40 $ / 151,69 $ | no | n/a | n/a | n/a |
| 70g | 2026-12-05 | 105,77 $ | 133,60 $ | 120,40 $ / 151,69 $ | no | n/a | n/a | n/a |
| 77g | 2026-12-12 | 109,30 $ | 138,06 $ | 120,40 $ / 151,69 $ | no | n/a | n/a | n/a |
| 84g | 2026-12-19 | 101,48 $ | 128,17 $ | 120,40 $ / 151,69 $ | no | n/a | n/a | n/a |
| 91g | 2026-12-26 | 102,04 $ | 128,88 $ | 120,40 $ / 151,69 $ | no | n/a | n/a | n/a |
| 98g | 2027-01-02 | 105,77 $ | 133,60 $ | 120,40 $ / 151,69 $ | no | n/a | n/a | n/a |
| 105g | 2027-01-09 | 119,25 $ | 150,62 $ | 120,40 $ / 152,73 $ | no | n/a | n/a | n/a |
| 112g | 2027-01-16 | 122,73 $ | 155,03 $ | 120,40 $ / 155,03 $ | no | n/a | n/a | n/a |
| 119g | 2027-01-23 | 119,81 $ | 151,33 $ | 120,40 $ / 155,03 $ | no | n/a | n/a | n/a |
| 126g | 2027-01-30 | 118,75 $ | 150,00 $ | 120,40 $ / 156,62 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 70 | 35,71% | 11,38% | 14,93% |
| 14g | 65 | 23,08% | 17,68% | 14,77% |
| 21g | 58 | 22,41% | 23,99% | 16,31% |
| 28g | 51 | 23,53% | 25,79% | 16,53% |
| 35g | 44 | 29,55% | 27,03% | 16,39% |
| 42g | 37 | 54,05% | 21,74% | 15,01% |
| 49g | 32 | 62,50% | 21,23% | 17,78% |
| 56g | 25 | 64,00% | 17,24% | 19,43% |
| 63g | 18 | 61,11% | 12,16% | 24,16% |
| 70g | 11 | 54,55% | 13,49% | 35,05% |
| 77g | 4 | 0,00% | 16,76% | 30,16% |
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
