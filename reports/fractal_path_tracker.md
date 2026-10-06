<!-- FRACTAL_PATH_TRACKER_START -->
# Tracking percorso frattale SOL/BTC

Generato: 2026-10-06 05:32 UTC

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-10-06**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-03-23**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **120,12 $**
- Verdetto principale: **STRUTTURA ANALOGA, PREZZO NON ADERENTE**
- Somiglianza strutturale: **+72,32%**
- Aderenza live principale: **+68,71%**
- Errore medio live principale: **15,64%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE NON CONFERMATO DAL PREZZO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **122**
- Osservazioni inclusive dal bottom: **123**
- Osservazioni da inizio programma/scanner: **96**
- Errore assoluto medio dal bottom: **13,53%**
- Errore assoluto medio da inizio programma: **15,64%**
- Gap firmato medio ultimi 7 giorni: **+9,65%**
- Errore assoluto medio ultimi 7 giorni: **9,65%**
- Gap ultimo giorno: **+7,62%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **+7,62%**
- Gap firmato medio 7g: **+9,65%**
- Errore assoluto medio 7g: **9,65%**
- Variazione recente gap: **-1,76%**
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
| 113 | 2026-09-27 | 2023-03-14 | 122,06 $ | 97,48 $ | +25,21% | da inizio programma |
| 114 | 2026-09-28 | 2023-03-15 | 118,84 $ | 96,02 $ | +23,76% | da inizio programma |
| 115 | 2026-09-29 | 2023-03-16 | 119,06 $ | 98,69 $ | +20,64% | da inizio programma |
| 116 | 2026-09-30 | 2023-03-17 | 117,99 $ | 108,03 $ | +9,22% | da inizio programma |
| 117 | 2026-10-01 | 2023-03-18 | 118,40 $ | 106,22 $ | +11,46% | da inizio programma |
| 118 | 2026-10-02 | 2023-03-19 | 118,62 $ | 110,45 $ | +7,39% | da inizio programma |
| 119 | 2026-10-03 | 2023-03-20 | 119,65 $ | 109,38 $ | +9,38% | da inizio programma |
| 120 | 2026-10-04 | 2023-03-21 | 121,53 $ | 110,99 $ | +9,49% | da inizio programma |
| 121 | 2026-10-05 | 2023-03-22 | 121,53 $ | 107,57 $ | +12,98% | da inizio programma |
| 122 | 2026-10-06 | 2023-03-23 | 120,12 $ | 111,61 $ | +7,62% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-10-13 | 110,43 $ | 118,85 $ | 115,06 $ / 120,18 $ | no | n/a | n/a | n/a |
| 14g | 2026-10-20 | 110,47 $ | 118,89 $ | 115,06 $ / 120,73 $ | no | n/a | n/a | n/a |
| 21g | 2026-10-27 | 119,75 $ | 128,87 $ | 115,06 $ / 128,87 $ | no | n/a | n/a | n/a |
| 28g | 2026-11-03 | 111,27 $ | 119,75 $ | 115,06 $ / 129,24 $ | no | n/a | n/a | n/a |
| 35g | 2026-11-10 | 116,10 $ | 124,95 $ | 115,06 $ / 129,24 $ | no | n/a | n/a | n/a |
| 42g | 2026-11-17 | 113,64 $ | 122,30 $ | 115,06 $ / 129,24 $ | no | n/a | n/a | n/a |
| 49g | 2026-11-24 | 106,36 $ | 114,47 $ | 114,47 $ / 129,24 $ | no | n/a | n/a | n/a |
| 56g | 2026-12-01 | 105,70 $ | 113,75 $ | 113,55 $ / 129,24 $ | no | n/a | n/a | n/a |
| 63g | 2026-12-08 | 104,30 $ | 112,24 $ | 111,64 $ / 129,24 $ | no | n/a | n/a | n/a |
| 70g | 2026-12-15 | 105,65 $ | 113,70 $ | 111,64 $ / 129,24 $ | no | n/a | n/a | n/a |
| 77g | 2026-12-22 | 104,42 $ | 112,38 $ | 109,21 $ / 129,24 $ | no | n/a | n/a | n/a |
| 84g | 2026-12-29 | 100,75 $ | 108,43 $ | 106,51 $ / 129,24 $ | no | n/a | n/a | n/a |
| 91g | 2027-01-05 | 117,83 $ | 126,81 $ | 106,51 $ / 129,24 $ | no | n/a | n/a | n/a |
| 98g | 2027-01-12 | 119,93 $ | 129,07 $ | 106,51 $ / 130,13 $ | no | n/a | n/a | n/a |
| 105g | 2027-01-19 | 117,82 $ | 126,80 $ | 106,51 $ / 132,09 $ | no | n/a | n/a | n/a |
| 112g | 2027-01-26 | 123,99 $ | 133,44 $ | 106,51 $ / 133,44 $ | no | n/a | n/a | n/a |
| 119g | 2027-02-02 | 117,36 $ | 126,30 $ | 106,51 $ / 133,44 $ | no | n/a | n/a | n/a |
| 126g | 2027-02-09 | 115,07 $ | 123,84 $ | 106,51 $ / 133,44 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 78 | 39,74% | 11,89% | 14,52% |
| 14g | 71 | 25,35% | 17,19% | 15,00% |
| 21g | 68 | 26,47% | 21,26% | 16,02% |
| 28g | 61 | 24,59% | 22,49% | 16,17% |
| 35g | 54 | 35,19% | 23,87% | 16,01% |
| 42g | 47 | 44,68% | 22,47% | 14,87% |
| 49g | 40 | 50,00% | 24,85% | 17,28% |
| 56g | 35 | 45,71% | 22,23% | 17,91% |
| 63g | 28 | 39,29% | 15,52% | 20,41% |
| 70g | 21 | 47,62% | 9,60% | 24,18% |
| 77g | 14 | 50,00% | 9,18% | 17,02% |
| 84g | 7 | 100,00% | 5,90% | 9,37% |
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
