<!-- FRACTAL_PATH_TRACKER_START -->
# Tracking percorso frattale SOL/BTC

Generato: 2026-10-07 05:32 UTC

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-10-07**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-03-24**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **118,59 $**
- Verdetto principale: **STRUTTURA ANALOGA, PREZZO NON ADERENTE**
- Somiglianza strutturale: **+72,63%**
- Aderenza live principale: **+68,84%**
- Errore medio live principale: **15,58%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE NON CONFERMATO DAL PREZZO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **123**
- Osservazioni inclusive dal bottom: **124**
- Osservazioni da inizio programma/scanner: **97**
- Errore assoluto medio dal bottom: **13,50%**
- Errore assoluto medio da inizio programma: **15,58%**
- Gap firmato medio ultimi 7 giorni: **+9,67%**
- Errore assoluto medio ultimi 7 giorni: **9,67%**
- Gap ultimo giorno: **+9,50%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **+9,50%**
- Gap firmato medio 7g: **+9,67%**
- Errore assoluto medio 7g: **9,67%**
- Variazione recente gap: **+0,00%**
- Stato gap: **SOPRA IL FRATTALE**
- Trend gap: **SOL resta sopra il percorso ancorato con distacco quasi stabile**

Soglie operative del grafico:

- entro **±5%**: percorso vicino;
- tra **±5% e ±12%**: deviazione gestibile;
- oltre **±12%**: frattale non abbastanza aderente per conferma operativa;
- oltre **±18%**: disallineamento marcato.

## Ultimi giorni del confronto ancorato

|   Giorno | Data SOL   | Data BTC eq.   | SOL reale   | Percorso ancorato   | Gap firmato   | Fase                |
|---------:|:-----------|:---------------|:------------|:--------------------|:--------------|:--------------------|
| 114 | 2026-09-28 | 2023-03-15 | 118,84 $ | 96,02 $ | +23,76% | da inizio programma |
| 115 | 2026-09-29 | 2023-03-16 | 119,06 $ | 98,69 $ | +20,64% | da inizio programma |
| 116 | 2026-09-30 | 2023-03-17 | 117,99 $ | 108,03 $ | +9,22% | da inizio programma |
| 117 | 2026-10-01 | 2023-03-18 | 118,40 $ | 106,22 $ | +11,46% | da inizio programma |
| 118 | 2026-10-02 | 2023-03-19 | 118,62 $ | 110,45 $ | +7,39% | da inizio programma |
| 119 | 2026-10-03 | 2023-03-20 | 119,65 $ | 109,38 $ | +9,38% | da inizio programma |
| 120 | 2026-10-04 | 2023-03-21 | 121,53 $ | 110,99 $ | +9,49% | da inizio programma |
| 121 | 2026-10-05 | 2023-03-22 | 120,75 $ | 107,57 $ | +12,25% | da inizio programma |
| 122 | 2026-10-06 | 2023-03-23 | 120,75 $ | 111,61 $ | +8,19% | da inizio programma |
| 123 | 2026-10-07 | 2023-03-24 | 118,59 $ | 108,30 $ | +9,50% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-10-14 | 112,18 $ | 122,84 $ | 117,07 $ / 122,84 $ | no | n/a | n/a | n/a |
| 14g | 2026-10-21 | 110,01 $ | 120,46 $ | 117,07 $ / 122,84 $ | no | n/a | n/a | n/a |
| 21g | 2026-10-28 | 120,09 $ | 131,50 $ | 117,07 $ / 131,50 $ | no | n/a | n/a | n/a |
| 28g | 2026-11-04 | 107,45 $ | 117,66 $ | 117,07 $ / 131,50 $ | no | n/a | n/a | n/a |
| 35g | 2026-11-11 | 115,58 $ | 126,56 $ | 117,07 $ / 131,50 $ | no | n/a | n/a | n/a |
| 42g | 2026-11-18 | 116,34 $ | 127,39 $ | 117,07 $ / 131,50 $ | no | n/a | n/a | n/a |
| 49g | 2026-11-25 | 105,59 $ | 115,62 $ | 115,62 $ / 131,50 $ | no | n/a | n/a | n/a |
| 56g | 2026-12-02 | 105,93 $ | 115,99 $ | 115,53 $ / 131,50 $ | no | n/a | n/a | n/a |
| 63g | 2026-12-09 | 105,25 $ | 115,25 $ | 113,59 $ / 131,50 $ | no | n/a | n/a | n/a |
| 70g | 2026-12-16 | 107,34 $ | 117,54 $ | 113,59 $ / 131,50 $ | no | n/a | n/a | n/a |
| 77g | 2026-12-23 | 104,31 $ | 114,22 $ | 111,11 $ / 131,50 $ | no | n/a | n/a | n/a |
| 84g | 2026-12-30 | 103,71 $ | 113,56 $ | 108,37 $ / 131,50 $ | no | n/a | n/a | n/a |
| 91g | 2027-01-06 | 120,92 $ | 132,40 $ | 108,37 $ / 132,40 $ | no | n/a | n/a | n/a |
| 98g | 2027-01-13 | 120,06 $ | 131,46 $ | 108,37 $ / 132,40 $ | no | n/a | n/a | n/a |
| 105g | 2027-01-20 | 119,53 $ | 130,88 $ | 108,37 $ / 134,39 $ | no | n/a | n/a | n/a |
| 112g | 2027-01-27 | 119,49 $ | 130,84 $ | 108,37 $ / 135,77 $ | no | n/a | n/a | n/a |
| 119g | 2027-02-03 | 117,82 $ | 129,01 $ | 108,37 $ / 135,77 $ | no | n/a | n/a | n/a |
| 126g | 2027-02-10 | 115,50 $ | 126,47 $ | 108,37 $ / 135,77 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 79 | 40,51% | 11,75% | 14,45% |
| 14g | 72 | 26,39% | 17,30% | 14,93% |
| 21g | 69 | 27,54% | 20,95% | 15,92% |
| 28g | 62 | 25,81% | 22,17% | 16,06% |
| 35g | 55 | 34,55% | 23,52% | 15,88% |
| 42g | 48 | 45,83% | 22,05% | 14,75% |
| 49g | 41 | 48,78% | 25,00% | 17,08% |
| 56g | 35 | 45,71% | 22,23% | 17,90% |
| 63g | 29 | 37,93% | 16,09% | 20,00% |
| 70g | 22 | 45,45% | 9,93% | 23,44% |
| 77g | 15 | 53,33% | 8,98% | 16,43% |
| 84g | 8 | 100,00% | 6,16% | 9,37% |
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
