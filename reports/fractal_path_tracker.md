<!-- FRACTAL_PATH_TRACKER_START -->
# Tracking percorso frattale SOL/BTC

Generato: 2026-09-11 05:32 UTC

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-09-11**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-02-26**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **99,61 $**
- Verdetto principale: **ANALOGIA DEBOLE / SCENARIO SECONDARIO**
- Somiglianza strutturale: **+69,82%**
- Aderenza live principale: **+72,35%**
- Errore medio live principale: **13,83%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE SOLO DI CONTESTO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **97**
- Osservazioni inclusive dal bottom: **98**
- Osservazioni da inizio programma/scanner: **71**
- Errore assoluto medio dal bottom: **11,68%**
- Errore assoluto medio da inizio programma: **13,83%**
- Gap firmato medio ultimi 7 giorni: **+9,20%**
- Errore assoluto medio ultimi 7 giorni: **9,20%**
- Gap ultimo giorno: **+7,32%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **+7,32%**
- Gap firmato medio 7g: **+9,20%**
- Errore assoluto medio 7g: **9,20%**
- Variazione recente gap: **-2,21%**
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
| 88 | 2026-09-02 | 2023-02-17 | 100,39 $ | 96,77 $ | +3,74% | da inizio programma |
| 89 | 2026-09-03 | 2023-02-18 | 103,98 $ | 97,07 $ | +7,12% | da inizio programma |
| 90 | 2026-09-04 | 2023-02-19 | 101,95 $ | 95,83 $ | +6,38% | da inizio programma |
| 91 | 2026-09-05 | 2023-02-20 | 103,19 $ | 97,81 $ | +5,50% | da inizio programma |
| 92 | 2026-09-06 | 2023-02-21 | 106,45 $ | 96,26 $ | +10,58% | da inizio programma |
| 93 | 2026-09-07 | 2023-02-22 | 103,87 $ | 95,29 $ | +9,01% | da inizio programma |
| 94 | 2026-09-08 | 2023-02-23 | 103,33 $ | 94,33 $ | +9,53% | da inizio programma |
| 95 | 2026-09-09 | 2023-02-24 | 101,61 $ | 91,38 $ | +11,19% | da inizio programma |
| 96 | 2026-09-10 | 2023-02-25 | 101,61 $ | 91,29 $ | +11,30% | da inizio programma |
| 97 | 2026-09-11 | 2023-02-26 | 99,61 $ | 92,81 $ | +7,32% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-09-18 | 88,38 $ | 94,85 $ | 94,50 $ / 99,97 $ | no | n/a | n/a | n/a |
| 14g | 2026-09-25 | 87,31 $ | 93,70 $ | 85,35 $ / 99,97 $ | no | n/a | n/a | n/a |
| 21g | 2026-10-02 | 110,45 $ | 118,54 $ | 85,35 $ / 118,54 $ | no | n/a | n/a | n/a |
| 28g | 2026-10-09 | 110,28 $ | 118,35 $ | 85,35 $ / 119,79 $ | no | n/a | n/a | n/a |
| 35g | 2026-10-16 | 111,08 $ | 119,22 $ | 85,35 $ / 120,40 $ | no | n/a | n/a | n/a |
| 42g | 2026-10-23 | 111,61 $ | 119,78 $ | 85,35 $ / 120,40 $ | no | n/a | n/a | n/a |
| 49g | 2026-10-30 | 119,42 $ | 128,16 $ | 85,35 $ / 128,88 $ | no | n/a | n/a | n/a |
| 56g | 2026-11-06 | 108,69 $ | 116,65 $ | 85,35 $ / 128,88 $ | no | n/a | n/a | n/a |
| 63g | 2026-11-13 | 115,30 $ | 123,74 $ | 85,35 $ / 128,88 $ | no | n/a | n/a | n/a |
| 70g | 2026-11-20 | 112,09 $ | 120,30 $ | 85,35 $ / 128,88 $ | no | n/a | n/a | n/a |
| 77g | 2026-11-27 | 106,09 $ | 113,85 $ | 85,35 $ / 128,88 $ | no | n/a | n/a | n/a |
| 84g | 2026-12-04 | 105,39 $ | 113,11 $ | 85,35 $ / 128,88 $ | no | n/a | n/a | n/a |
| 91g | 2026-12-11 | 110,64 $ | 118,74 $ | 85,35 $ / 128,88 $ | no | n/a | n/a | n/a |
| 98g | 2026-12-18 | 106,83 $ | 114,65 $ | 85,35 $ / 128,88 $ | no | n/a | n/a | n/a |
| 105g | 2026-12-25 | 102,18 $ | 109,67 $ | 85,35 $ / 128,88 $ | no | n/a | n/a | n/a |
| 112g | 2027-01-01 | 103,74 $ | 111,34 $ | 85,35 $ / 128,88 $ | no | n/a | n/a | n/a |
| 119g | 2027-01-08 | 120,07 $ | 128,86 $ | 85,35 $ / 129,77 $ | no | n/a | n/a | n/a |
| 126g | 2027-01-15 | 120,62 $ | 129,46 $ | 85,35 $ / 129,77 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 57 | 36,84% | 10,76% | 12,72% |
| 14g | 50 | 28,00% | 17,85% | 11,55% |
| 21g | 43 | 13,95% | 27,00% | 13,10% |
| 28g | 36 | 30,56% | 25,87% | 12,67% |
| 35g | 31 | 41,94% | 18,47% | 11,71% |
| 42g | 24 | 83,33% | 9,28% | 10,81% |
| 49g | 17 | 100,00% | 6,07% | 10,49% |
| 56g | 10 | 100,00% | 7,07% | 8,85% |
| 63g | 3 | 100,00% | 6,41% | 7,32% |
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
