<!-- FRACTAL_PATH_TRACKER_START -->
# Tracking percorso frattale SOL/BTC

Generato: 2026-09-30 05:32 UTC

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-09-30**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-03-17**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **119,12 $**
- Verdetto principale: **STRUTTURA ANALOGA, PREZZO NON ADERENTE**
- Somiglianza strutturale: **+70,80%**
- Aderenza live principale: **+67,91%**
- Errore medio live principale: **16,05%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE NON CONFERMATO DAL PREZZO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **116**
- Osservazioni inclusive dal bottom: **117**
- Osservazioni da inizio programma/scanner: **90**
- Errore assoluto medio dal bottom: **13,73%**
- Errore assoluto medio da inizio programma: **16,05%**
- Gap firmato medio ultimi 7 giorni: **+27,25%**
- Errore assoluto medio ultimi 7 giorni: **27,25%**
- Gap ultimo giorno: **+10,27%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **+10,27%**
- Gap firmato medio 7g: **+27,25%**
- Errore assoluto medio 7g: **27,25%**
- Variazione recente gap: **-14,95%**
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
| 107 | 2026-09-21 | 2023-03-08 | 118,75 $ | 85,55 $ | +38,80% | da inizio programma |
| 108 | 2026-09-22 | 2023-03-09 | 118,51 $ | 80,21 $ | +47,74% | da inizio programma |
| 109 | 2026-09-23 | 2023-03-10 | 114,98 $ | 79,52 $ | +44,58% | da inizio programma |
| 110 | 2026-09-24 | 2023-03-11 | 117,01 $ | 81,28 $ | +43,97% | da inizio programma |
| 111 | 2026-09-25 | 2023-03-12 | 122,01 $ | 87,31 $ | +39,74% | da inizio programma |
| 112 | 2026-09-26 | 2023-03-13 | 121,43 $ | 95,32 $ | +27,39% | da inizio programma |
| 113 | 2026-09-27 | 2023-03-14 | 122,06 $ | 97,48 $ | +25,21% | da inizio programma |
| 114 | 2026-09-28 | 2023-03-15 | 118,84 $ | 96,02 $ | +23,76% | da inizio programma |
| 115 | 2026-09-29 | 2023-03-16 | 118,84 $ | 98,69 $ | +20,42% | da inizio programma |
| 116 | 2026-09-30 | 2023-03-17 | 119,12 $ | 108,03 $ | +10,27% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-10-07 | 108,30 $ | 119,42 $ | 117,13 $ / 123,07 $ | no | n/a | n/a | n/a |
| 14g | 2026-10-14 | 112,18 $ | 123,70 $ | 117,13 $ / 123,70 $ | no | n/a | n/a | n/a |
| 21g | 2026-10-21 | 110,01 $ | 121,30 $ | 117,13 $ / 123,70 $ | no | n/a | n/a | n/a |
| 28g | 2026-10-28 | 120,09 $ | 132,42 $ | 117,13 $ / 132,42 $ | no | n/a | n/a | n/a |
| 35g | 2026-11-04 | 107,45 $ | 118,48 $ | 117,13 $ / 132,42 $ | no | n/a | n/a | n/a |
| 42g | 2026-11-11 | 115,58 $ | 127,44 $ | 117,13 $ / 132,42 $ | no | n/a | n/a | n/a |
| 49g | 2026-11-18 | 116,34 $ | 128,29 $ | 117,13 $ / 132,42 $ | no | n/a | n/a | n/a |
| 56g | 2026-11-25 | 105,59 $ | 116,43 $ | 116,43 $ / 132,42 $ | no | n/a | n/a | n/a |
| 63g | 2026-12-02 | 105,93 $ | 116,80 $ | 116,34 $ / 132,42 $ | no | n/a | n/a | n/a |
| 70g | 2026-12-09 | 105,25 $ | 116,06 $ | 114,39 $ / 132,42 $ | no | n/a | n/a | n/a |
| 77g | 2026-12-16 | 107,34 $ | 118,36 $ | 114,39 $ / 132,42 $ | no | n/a | n/a | n/a |
| 84g | 2026-12-23 | 104,31 $ | 115,02 $ | 111,89 $ / 132,42 $ | no | n/a | n/a | n/a |
| 91g | 2026-12-30 | 103,71 $ | 114,36 $ | 109,13 $ / 132,42 $ | no | n/a | n/a | n/a |
| 98g | 2027-01-06 | 120,92 $ | 133,33 $ | 109,13 $ / 133,33 $ | no | n/a | n/a | n/a |
| 105g | 2027-01-13 | 120,06 $ | 132,38 $ | 109,13 $ / 133,33 $ | no | n/a | n/a | n/a |
| 112g | 2027-01-20 | 119,53 $ | 131,80 $ | 109,13 $ / 135,33 $ | no | n/a | n/a | n/a |
| 119g | 2027-01-27 | 119,49 $ | 131,76 $ | 109,13 $ / 136,72 $ | no | n/a | n/a | n/a |
| 126g | 2027-02-03 | 117,82 $ | 129,91 $ | 109,13 $ / 136,72 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 72 | 37,50% | 11,65% | 14,94% |
| 14g | 69 | 21,74% | 17,28% | 15,18% |
| 21g | 62 | 22,58% | 23,17% | 16,66% |
| 28g | 55 | 20,00% | 24,63% | 16,92% |
| 35g | 48 | 29,17% | 25,88% | 16,84% |
| 42g | 41 | 48,78% | 24,32% | 15,69% |
| 49g | 35 | 57,14% | 23,59% | 18,47% |
| 56g | 29 | 55,17% | 20,28% | 19,75% |
| 63g | 22 | 50,00% | 13,36% | 23,65% |
| 70g | 15 | 46,67% | 11,90% | 30,91% |
| 77g | 8 | 12,50% | 12,24% | 24,46% |
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
