<!-- FRACTAL_PATH_TRACKER_START -->
# Tracking percorso frattale SOL/BTC

Generato: 2026-09-12 05:32 UTC

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-09-12**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-02-27**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **101,55 $**
- Verdetto principale: **ANALOGIA DEBOLE / SCENARIO SECONDARIO**
- Somiglianza strutturale: **+70,17%**
- Aderenza live principale: **+72,58%**
- Errore medio live principale: **13,71%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE SOLO DI CONTESTO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **98**
- Osservazioni inclusive dal bottom: **99**
- Osservazioni da inizio programma/scanner: **72**
- Errore assoluto medio dal bottom: **11,61%**
- Errore assoluto medio da inizio programma: **13,71%**
- Gap firmato medio ultimi 7 giorni: **+9,19%**
- Errore assoluto medio ultimi 7 giorni: **9,19%**
- Gap ultimo giorno: **+9,59%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **+9,59%**
- Gap firmato medio 7g: **+9,19%**
- Errore assoluto medio 7g: **9,19%**
- Variazione recente gap: **-1,60%**
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
| 89 | 2026-09-03 | 2023-02-18 | 103,98 $ | 97,07 $ | +7,12% | da inizio programma |
| 90 | 2026-09-04 | 2023-02-19 | 101,95 $ | 95,83 $ | +6,38% | da inizio programma |
| 91 | 2026-09-05 | 2023-02-20 | 103,19 $ | 97,81 $ | +5,50% | da inizio programma |
| 92 | 2026-09-06 | 2023-02-21 | 106,45 $ | 96,26 $ | +10,58% | da inizio programma |
| 93 | 2026-09-07 | 2023-02-22 | 103,87 $ | 95,29 $ | +9,01% | da inizio programma |
| 94 | 2026-09-08 | 2023-02-23 | 103,33 $ | 94,33 $ | +9,53% | da inizio programma |
| 95 | 2026-09-09 | 2023-02-24 | 101,61 $ | 91,38 $ | +11,19% | da inizio programma |
| 96 | 2026-09-10 | 2023-02-25 | 98,69 $ | 91,29 $ | +8,10% | da inizio programma |
| 97 | 2026-09-11 | 2023-02-26 | 98,69 $ | 92,81 $ | +6,33% | da inizio programma |
| 98 | 2026-09-12 | 2023-02-27 | 101,55 $ | 92,66 $ | +9,59% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-09-19 | 88,36 $ | 96,83 $ | 96,50 $ / 102,08 $ | no | n/a | n/a | n/a |
| 14g | 2026-09-26 | 95,32 $ | 104,46 $ | 87,15 $ / 104,46 $ | no | n/a | n/a | n/a |
| 21g | 2026-10-03 | 109,38 $ | 119,87 $ | 87,15 $ / 121,05 $ | no | n/a | n/a | n/a |
| 28g | 2026-10-10 | 106,91 $ | 117,16 $ | 87,15 $ / 122,32 $ | no | n/a | n/a | n/a |
| 35g | 2026-10-17 | 109,47 $ | 119,97 $ | 87,15 $ / 122,94 $ | no | n/a | n/a | n/a |
| 42g | 2026-10-24 | 116,81 $ | 128,01 $ | 87,15 $ / 128,01 $ | no | n/a | n/a | n/a |
| 49g | 2026-10-31 | 115,99 $ | 127,12 $ | 87,15 $ / 131,61 $ | no | n/a | n/a | n/a |
| 56g | 2026-11-07 | 108,43 $ | 118,83 $ | 87,15 $ / 131,61 $ | no | n/a | n/a | n/a |
| 63g | 2026-11-14 | 110,66 $ | 121,27 $ | 87,15 $ / 131,61 $ | no | n/a | n/a | n/a |
| 70g | 2026-11-21 | 109,09 $ | 119,56 $ | 87,15 $ / 131,61 $ | no | n/a | n/a | n/a |
| 77g | 2026-11-28 | 107,12 $ | 117,39 $ | 87,15 $ / 131,61 $ | no | n/a | n/a | n/a |
| 84g | 2026-12-05 | 105,77 $ | 115,92 $ | 87,15 $ / 131,61 $ | no | n/a | n/a | n/a |
| 91g | 2026-12-12 | 109,30 $ | 119,78 $ | 87,15 $ / 131,61 $ | no | n/a | n/a | n/a |
| 98g | 2026-12-19 | 101,48 $ | 111,21 $ | 87,15 $ / 131,61 $ | no | n/a | n/a | n/a |
| 105g | 2026-12-26 | 102,04 $ | 111,82 $ | 87,15 $ / 131,61 $ | no | n/a | n/a | n/a |
| 112g | 2027-01-02 | 105,77 $ | 115,92 $ | 87,15 $ / 131,61 $ | no | n/a | n/a | n/a |
| 119g | 2027-01-09 | 119,25 $ | 130,68 $ | 87,15 $ / 132,51 $ | no | n/a | n/a | n/a |
| 126g | 2027-01-16 | 122,73 $ | 134,50 $ | 87,15 $ / 134,50 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 58 | 37,93% | 10,61% | 12,58% |
| 14g | 51 | 25,49% | 17,76% | 11,42% |
| 21g | 44 | 15,91% | 26,40% | 12,92% |
| 28g | 37 | 29,73% | 25,97% | 12,56% |
| 35g | 32 | 40,62% | 18,76% | 11,50% |
| 42g | 25 | 80,00% | 9,72% | 10,58% |
| 49g | 18 | 100,00% | 5,94% | 10,17% |
| 56g | 11 | 100,00% | 7,10% | 8,47% |
| 63g | 4 | 100,00% | 7,97% | 7,96% |
| 70g | 0 | n/a | n/a | n/a |
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
