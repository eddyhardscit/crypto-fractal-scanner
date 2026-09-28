<!-- FRACTAL_PATH_TRACKER_START -->
# Tracking percorso frattale SOL/BTC

Generato: 2026-09-28 05:32 UTC

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-09-28**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-03-15**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **119,07 $**
- Verdetto principale: **STRUTTURA ANALOGA, PREZZO NON ADERENTE**
- Somiglianza strutturale: **+70,37%**
- Aderenza live principale: **+67,88%**
- Errore medio live principale: **16,06%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE NON CONFERMATO DAL PREZZO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **114**
- Osservazioni inclusive dal bottom: **115**
- Osservazioni da inizio programma/scanner: **88**
- Errore assoluto medio dal bottom: **13,70%**
- Errore assoluto medio da inizio programma: **16,06%**
- Gap firmato medio ultimi 7 giorni: **+36,00%**
- Errore assoluto medio ultimi 7 giorni: **36,00%**
- Gap ultimo giorno: **+24,00%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **+24,00%**
- Gap firmato medio 7g: **+36,00%**
- Errore assoluto medio 7g: **36,00%**
- Variazione recente gap: **-15,74%**
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
| 105 | 2026-09-19 | 2023-03-06 | 111,01 $ | 88,36 $ | +25,64% | da inizio programma |
| 106 | 2026-09-20 | 2023-03-07 | 111,13 $ | 87,53 $ | +26,97% | da inizio programma |
| 107 | 2026-09-21 | 2023-03-08 | 118,75 $ | 85,55 $ | +38,80% | da inizio programma |
| 108 | 2026-09-22 | 2023-03-09 | 118,51 $ | 80,21 $ | +47,74% | da inizio programma |
| 109 | 2026-09-23 | 2023-03-10 | 114,98 $ | 79,52 $ | +44,58% | da inizio programma |
| 110 | 2026-09-24 | 2023-03-11 | 117,01 $ | 81,28 $ | +43,97% | da inizio programma |
| 111 | 2026-09-25 | 2023-03-12 | 122,01 $ | 87,31 $ | +39,74% | da inizio programma |
| 112 | 2026-09-26 | 2023-03-13 | 121,43 $ | 95,32 $ | +27,39% | da inizio programma |
| 113 | 2026-09-27 | 2023-03-14 | 121,43 $ | 97,48 $ | +24,56% | da inizio programma |
| 114 | 2026-09-28 | 2023-03-15 | 119,07 $ | 96,02 $ | +24,00% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-10-05 | 107,57 $ | 133,39 $ | 119,07 $ / 137,63 $ | no | n/a | n/a | n/a |
| 14g | 2026-10-12 | 111,67 $ | 138,47 $ | 119,07 $ / 138,47 $ | no | n/a | n/a | n/a |
| 21g | 2026-10-19 | 111,00 $ | 137,64 $ | 119,07 $ / 139,11 $ | no | n/a | n/a | n/a |
| 28g | 2026-10-26 | 118,72 $ | 147,22 $ | 119,07 $ / 147,69 $ | no | n/a | n/a | n/a |
| 35g | 2026-11-02 | 113,54 $ | 140,79 $ | 119,07 $ / 148,91 $ | no | n/a | n/a | n/a |
| 42g | 2026-11-09 | 111,96 $ | 138,84 $ | 119,07 $ / 148,91 $ | no | n/a | n/a | n/a |
| 49g | 2026-11-16 | 114,26 $ | 141,69 $ | 119,07 $ / 148,91 $ | no | n/a | n/a | n/a |
| 56g | 2026-11-23 | 108,81 $ | 134,92 $ | 119,07 $ / 148,91 $ | no | n/a | n/a | n/a |
| 63g | 2026-11-30 | 107,93 $ | 133,84 $ | 119,07 $ / 148,91 $ | no | n/a | n/a | n/a |
| 70g | 2026-12-07 | 103,74 $ | 128,64 $ | 119,07 $ / 148,91 $ | no | n/a | n/a | n/a |
| 77g | 2026-12-14 | 107,22 $ | 132,96 $ | 119,07 $ / 148,91 $ | no | n/a | n/a | n/a |
| 84g | 2026-12-21 | 103,78 $ | 128,69 $ | 119,07 $ / 148,91 $ | no | n/a | n/a | n/a |
| 91g | 2026-12-28 | 98,97 $ | 122,73 $ | 119,07 $ / 148,91 $ | no | n/a | n/a | n/a |
| 98g | 2027-01-04 | 118,28 $ | 146,68 $ | 119,07 $ / 148,91 $ | no | n/a | n/a | n/a |
| 105g | 2027-01-11 | 118,52 $ | 146,96 $ | 119,07 $ / 149,94 $ | no | n/a | n/a | n/a |
| 112g | 2027-01-18 | 120,20 $ | 149,05 $ | 119,07 $ / 152,19 $ | no | n/a | n/a | n/a |
| 119g | 2027-01-25 | 119,72 $ | 148,46 $ | 119,07 $ / 152,19 $ | no | n/a | n/a | n/a |
| 126g | 2027-02-01 | 117,84 $ | 146,12 $ | 119,07 $ / 153,75 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 70 | 35,71% | 11,38% | 14,93% |
| 14g | 67 | 22,39% | 17,63% | 15,17% |
| 21g | 60 | 21,67% | 23,72% | 16,70% |
| 28g | 53 | 20,75% | 25,29% | 16,97% |
| 35g | 46 | 28,26% | 26,91% | 16,90% |
| 42g | 39 | 51,28% | 23,52% | 15,70% |
| 49g | 34 | 58,82% | 22,98% | 18,40% |
| 56g | 27 | 59,26% | 19,21% | 20,09% |
| 63g | 20 | 55,00% | 12,69% | 24,55% |
| 70g | 13 | 46,15% | 13,12% | 33,71% |
| 77g | 6 | 0,00% | 14,69% | 28,92% |
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
