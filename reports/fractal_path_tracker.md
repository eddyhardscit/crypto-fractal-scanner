<!-- FRACTAL_PATH_TRACKER_START -->
# Tracking percorso frattale SOL/BTC

Generato: 2026-09-29 05:32 UTC

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-09-29**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-03-16**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **117,81 $**
- Verdetto principale: **STRUTTURA ANALOGA, PREZZO NON ADERENTE**
- Somiglianza strutturale: **+70,73%**
- Aderenza live principale: **+67,72%**
- Errore medio live principale: **16,14%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE NON CONFERMATO DAL PREZZO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **115**
- Osservazioni inclusive dal bottom: **116**
- Osservazioni da inizio programma/scanner: **89**
- Errore assoluto medio dal bottom: **13,78%**
- Errore assoluto medio da inizio programma: **16,14%**
- Gap firmato medio ultimi 7 giorni: **+32,48%**
- Errore assoluto medio ultimi 7 giorni: **32,48%**
- Gap ultimo giorno: **+19,38%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **+19,38%**
- Gap firmato medio 7g: **+32,48%**
- Errore assoluto medio 7g: **32,48%**
- Variazione recente gap: **-8,01%**
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
| 106 | 2026-09-20 | 2023-03-07 | 111,13 $ | 87,53 $ | +26,97% | da inizio programma |
| 107 | 2026-09-21 | 2023-03-08 | 118,75 $ | 85,55 $ | +38,80% | da inizio programma |
| 108 | 2026-09-22 | 2023-03-09 | 118,51 $ | 80,21 $ | +47,74% | da inizio programma |
| 109 | 2026-09-23 | 2023-03-10 | 114,98 $ | 79,52 $ | +44,58% | da inizio programma |
| 110 | 2026-09-24 | 2023-03-11 | 117,01 $ | 81,28 $ | +43,97% | da inizio programma |
| 111 | 2026-09-25 | 2023-03-12 | 122,01 $ | 87,31 $ | +39,74% | da inizio programma |
| 112 | 2026-09-26 | 2023-03-13 | 121,43 $ | 95,32 $ | +27,39% | da inizio programma |
| 113 | 2026-09-27 | 2023-03-14 | 122,06 $ | 97,48 $ | +25,21% | da inizio programma |
| 114 | 2026-09-28 | 2023-03-15 | 122,06 $ | 96,02 $ | +27,11% | da inizio programma |
| 115 | 2026-09-29 | 2023-03-16 | 117,81 $ | 98,69 $ | +19,38% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-10-06 | 111,61 $ | 133,24 $ | 117,81 $ / 133,24 $ | no | n/a | n/a | n/a |
| 14g | 2026-10-13 | 110,43 $ | 131,83 $ | 117,81 $ / 133,31 $ | no | n/a | n/a | n/a |
| 21g | 2026-10-20 | 110,47 $ | 131,88 $ | 117,81 $ / 133,92 $ | no | n/a | n/a | n/a |
| 28g | 2026-10-27 | 119,75 $ | 142,95 $ | 117,81 $ / 142,95 $ | no | n/a | n/a | n/a |
| 35g | 2026-11-03 | 111,27 $ | 132,83 $ | 117,81 $ / 143,36 $ | no | n/a | n/a | n/a |
| 42g | 2026-11-10 | 116,10 $ | 138,60 $ | 117,81 $ / 143,36 $ | no | n/a | n/a | n/a |
| 49g | 2026-11-17 | 113,64 $ | 135,66 $ | 117,81 $ / 143,36 $ | no | n/a | n/a | n/a |
| 56g | 2026-11-24 | 106,36 $ | 126,97 $ | 117,81 $ / 143,36 $ | no | n/a | n/a | n/a |
| 63g | 2026-12-01 | 105,70 $ | 126,18 $ | 117,81 $ / 143,36 $ | no | n/a | n/a | n/a |
| 70g | 2026-12-08 | 104,30 $ | 124,50 $ | 117,81 $ / 143,36 $ | no | n/a | n/a | n/a |
| 77g | 2026-12-15 | 105,65 $ | 126,12 $ | 117,81 $ / 143,36 $ | no | n/a | n/a | n/a |
| 84g | 2026-12-22 | 104,42 $ | 124,65 $ | 117,81 $ / 143,36 $ | no | n/a | n/a | n/a |
| 91g | 2026-12-29 | 100,75 $ | 120,27 $ | 117,81 $ / 143,36 $ | no | n/a | n/a | n/a |
| 98g | 2027-01-05 | 117,83 $ | 140,66 $ | 117,81 $ / 143,36 $ | no | n/a | n/a | n/a |
| 105g | 2027-01-12 | 119,93 $ | 143,17 $ | 117,81 $ / 144,34 $ | no | n/a | n/a | n/a |
| 112g | 2027-01-19 | 117,82 $ | 140,65 $ | 117,81 $ / 146,51 $ | no | n/a | n/a | n/a |
| 119g | 2027-01-26 | 123,99 $ | 148,02 $ | 117,81 $ / 148,02 $ | no | n/a | n/a | n/a |
| 126g | 2027-02-02 | 117,36 $ | 140,10 $ | 117,81 $ / 148,02 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 71 | 36,62% | 11,46% | 14,99% |
| 14g | 68 | 22,06% | 17,56% | 15,29% |
| 21g | 61 | 21,31% | 23,53% | 16,81% |
| 28g | 54 | 20,37% | 25,01% | 17,09% |
| 35g | 47 | 27,66% | 26,42% | 17,04% |
| 42g | 40 | 50,00% | 24,19% | 15,89% |
| 49g | 35 | 57,14% | 23,67% | 18,54% |
| 56g | 28 | 57,14% | 19,91% | 20,21% |
| 63g | 21 | 52,38% | 13,25% | 24,48% |
| 70g | 14 | 42,86% | 12,51% | 32,83% |
| 77g | 7 | 0,00% | 13,26% | 27,77% |
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
