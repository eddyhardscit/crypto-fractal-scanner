<!-- FRACTAL_PATH_TRACKER_START -->
# Tracking percorso frattale SOL/BTC

Generato: 2026-10-04 05:32 UTC

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-10-04**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-03-21**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **120,74 $**
- Verdetto principale: **STRUTTURA ANALOGA, PREZZO NON ADERENTE**
- Somiglianza strutturale: **+71,85%**
- Aderenza live principale: **+68,52%**
- Errore medio live principale: **15,74%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE NON CONFERMATO DAL PREZZO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **120**
- Osservazioni inclusive dal bottom: **121**
- Osservazioni da inizio programma/scanner: **94**
- Errore assoluto medio dal bottom: **13,57%**
- Errore assoluto medio da inizio programma: **15,74%**
- Gap firmato medio ultimi 7 giorni: **+12,81%**
- Errore assoluto medio ultimi 7 giorni: **12,81%**
- Gap ultimo giorno: **+8,78%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **+8,78%**
- Gap firmato medio 7g: **+12,81%**
- Errore assoluto medio 7g: **12,81%**
- Variazione recente gap: **-2,68%**
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
| 111 | 2026-09-25 | 2023-03-12 | 122,01 $ | 87,31 $ | +39,74% | da inizio programma |
| 112 | 2026-09-26 | 2023-03-13 | 121,43 $ | 95,32 $ | +27,39% | da inizio programma |
| 113 | 2026-09-27 | 2023-03-14 | 122,06 $ | 97,48 $ | +25,21% | da inizio programma |
| 114 | 2026-09-28 | 2023-03-15 | 118,84 $ | 96,02 $ | +23,76% | da inizio programma |
| 115 | 2026-09-29 | 2023-03-16 | 119,06 $ | 98,69 $ | +20,64% | da inizio programma |
| 116 | 2026-09-30 | 2023-03-17 | 117,99 $ | 108,03 $ | +9,22% | da inizio programma |
| 117 | 2026-10-01 | 2023-03-18 | 118,40 $ | 106,22 $ | +11,46% | da inizio programma |
| 118 | 2026-10-02 | 2023-03-19 | 118,62 $ | 110,45 $ | +7,39% | da inizio programma |
| 119 | 2026-10-03 | 2023-03-20 | 118,62 $ | 109,38 $ | +8,44% | da inizio programma |
| 120 | 2026-10-04 | 2023-03-21 | 120,74 $ | 110,99 $ | +8,78% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-10-11 | 107,42 $ | 116,85 $ | 116,30 $ / 121,42 $ | no | n/a | n/a | n/a |
| 14g | 2026-10-18 | 110,96 $ | 120,71 $ | 116,30 $ / 122,04 $ | no | n/a | n/a | n/a |
| 21g | 2026-10-25 | 119,10 $ | 129,56 $ | 116,30 $ / 129,56 $ | no | n/a | n/a | n/a |
| 28g | 2026-11-01 | 119,74 $ | 130,26 $ | 116,30 $ / 130,64 $ | no | n/a | n/a | n/a |
| 35g | 2026-11-08 | 111,51 $ | 121,30 $ | 116,30 $ / 130,64 $ | no | n/a | n/a | n/a |
| 42g | 2026-11-15 | 112,98 $ | 122,90 $ | 116,30 $ / 130,64 $ | no | n/a | n/a | n/a |
| 49g | 2026-11-22 | 108,95 $ | 118,52 $ | 116,30 $ / 130,64 $ | no | n/a | n/a | n/a |
| 56g | 2026-11-29 | 106,50 $ | 115,86 $ | 114,78 $ / 130,64 $ | no | n/a | n/a | n/a |
| 63g | 2026-12-06 | 107,25 $ | 116,67 $ | 114,65 $ / 130,64 $ | no | n/a | n/a | n/a |
| 70g | 2026-12-13 | 109,13 $ | 118,71 $ | 112,85 $ / 130,64 $ | no | n/a | n/a | n/a |
| 77g | 2026-12-20 | 107,30 $ | 116,72 $ | 110,39 $ / 130,64 $ | no | n/a | n/a | n/a |
| 84g | 2026-12-27 | 102,10 $ | 111,07 $ | 110,39 $ / 130,64 $ | no | n/a | n/a | n/a |
| 91g | 2027-01-03 | 111,59 $ | 121,39 $ | 107,67 $ / 130,64 $ | no | n/a | n/a | n/a |
| 98g | 2027-01-10 | 120,89 $ | 131,51 $ | 107,67 $ / 131,54 $ | no | n/a | n/a | n/a |
| 105g | 2027-01-17 | 121,24 $ | 131,89 $ | 107,67 $ / 133,51 $ | no | n/a | n/a | n/a |
| 112g | 2027-01-24 | 120,62 $ | 131,22 $ | 107,67 $ / 133,51 $ | no | n/a | n/a | n/a |
| 119g | 2027-01-31 | 117,61 $ | 127,94 $ | 107,67 $ / 134,88 $ | no | n/a | n/a | n/a |
| 126g | 2027-02-07 | 115,13 $ | 125,25 $ | 107,67 $ / 134,88 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 76 | 38,16% | 11,97% | 14,61% |
| 14g | 70 | 24,29% | 17,07% | 15,11% |
| 21g | 66 | 25,76% | 21,85% | 16,17% |
| 28g | 59 | 22,03% | 23,18% | 16,35% |
| 35g | 52 | 34,62% | 24,64% | 16,20% |
| 42g | 45 | 44,44% | 23,02% | 15,05% |
| 49g | 38 | 52,63% | 24,22% | 17,62% |
| 56g | 33 | 48,48% | 21,62% | 18,34% |
| 63g | 26 | 42,31% | 14,81% | 21,18% |
| 70g | 19 | 57,89% | 9,95% | 25,71% |
| 77g | 12 | 41,67% | 10,01% | 18,20% |
| 84g | 5 | 100,00% | 6,51% | 8,21% |
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
