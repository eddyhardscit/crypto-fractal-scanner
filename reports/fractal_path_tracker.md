<!-- FRACTAL_PATH_TRACKER_START -->
# Tracking percorso frattale SOL/BTC

Generato: 2026-09-05 08:21 UTC

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-09-05**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-02-20**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **102,31 $**
- Verdetto principale: **ANALOGIA DEBOLE / SCENARIO SECONDARIO**
- Somiglianza strutturale: **+67,38%**
- Aderenza live principale: **+71,63%**
- Errore medio live principale: **14,18%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE SOLO DI CONTESTO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **91**
- Osservazioni inclusive dal bottom: **92**
- Osservazioni da inizio programma/scanner: **65**
- Errore assoluto medio dal bottom: **11,79%**
- Errore assoluto medio da inizio programma: **14,18%**
- Gap firmato medio ultimi 7 giorni: **+7,61%**
- Errore assoluto medio ultimi 7 giorni: **7,61%**
- Gap ultimo giorno: **+4,60%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **+4,60%**
- Gap firmato medio 7g: **+7,61%**
- Errore assoluto medio 7g: **7,61%**
- Variazione recente gap: **+0,87%**
- Stato gap: **VICINO AL FRATTALE**
- Trend gap: **SOL resta sopra il percorso ancorato con distacco quasi stabile**

Soglie operative del grafico:

- entro **±5%**: percorso vicino;
- tra **±5% e ±12%**: deviazione gestibile;
- oltre **±12%**: frattale non abbastanza aderente per conferma operativa;
- oltre **±18%**: disallineamento marcato.

## Ultimi giorni del confronto ancorato

|   Giorno | Data SOL   | Data BTC eq.   | SOL reale   | Percorso ancorato   | Gap firmato   | Fase                |
|---------:|:-----------|:---------------|:------------|:--------------------|:--------------|:--------------------|
| 82 | 2026-08-27 | 2023-02-11 | 109,21 $ | 86,15 $ | +26,76% | da inizio programma |
| 83 | 2026-08-28 | 2023-02-12 | 104,13 $ | 85,83 $ | +21,32% | da inizio programma |
| 84 | 2026-08-29 | 2023-02-13 | 105,65 $ | 85,91 $ | +22,98% | da inizio programma |
| 85 | 2026-08-30 | 2023-02-14 | 101,88 $ | 87,53 $ | +16,39% | da inizio programma |
| 86 | 2026-08-31 | 2023-02-15 | 103,00 $ | 95,75 $ | +7,56% | da inizio programma |
| 87 | 2026-09-01 | 2023-02-16 | 99,99 $ | 93,06 $ | +7,45% | da inizio programma |
| 88 | 2026-09-02 | 2023-02-17 | 100,39 $ | 96,77 $ | +3,74% | da inizio programma |
| 89 | 2026-09-03 | 2023-02-18 | 103,98 $ | 97,07 $ | +7,12% | da inizio programma |
| 90 | 2026-09-04 | 2023-02-19 | 101,95 $ | 95,83 $ | +6,38% | da inizio programma |
| 91 | 2026-09-05 | 2023-02-20 | 102,31 $ | 97,81 $ | +4,60% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-09-12 | 92,66 $ | 96,93 $ | 95,50 $ / 102,31 $ | no | n/a | n/a | n/a |
| 14g | 2026-09-19 | 88,36 $ | 92,42 $ | 92,11 $ / 102,31 $ | no | n/a | n/a | n/a |
| 21g | 2026-09-26 | 95,32 $ | 99,71 $ | 83,18 $ / 102,31 $ | no | n/a | n/a | n/a |
| 28g | 2026-10-03 | 109,38 $ | 114,42 $ | 83,18 $ / 115,54 $ | no | n/a | n/a | n/a |
| 35g | 2026-10-10 | 106,91 $ | 111,83 $ | 83,18 $ / 116,75 $ | no | n/a | n/a | n/a |
| 42g | 2026-10-17 | 109,47 $ | 114,51 $ | 83,18 $ / 117,35 $ | no | n/a | n/a | n/a |
| 49g | 2026-10-24 | 116,81 $ | 122,19 $ | 83,18 $ / 122,19 $ | no | n/a | n/a | n/a |
| 56g | 2026-10-31 | 115,99 $ | 121,33 $ | 83,18 $ / 125,62 $ | no | n/a | n/a | n/a |
| 63g | 2026-11-07 | 108,43 $ | 113,42 $ | 83,18 $ / 125,62 $ | no | n/a | n/a | n/a |
| 70g | 2026-11-14 | 110,66 $ | 115,75 $ | 83,18 $ / 125,62 $ | no | n/a | n/a | n/a |
| 77g | 2026-11-21 | 109,09 $ | 114,12 $ | 83,18 $ / 125,62 $ | no | n/a | n/a | n/a |
| 84g | 2026-11-28 | 107,12 $ | 112,05 $ | 83,18 $ / 125,62 $ | no | n/a | n/a | n/a |
| 91g | 2026-12-05 | 105,77 $ | 110,64 $ | 83,18 $ / 125,62 $ | no | n/a | n/a | n/a |
| 98g | 2026-12-12 | 109,30 $ | 114,33 $ | 83,18 $ / 125,62 $ | no | n/a | n/a | n/a |
| 105g | 2026-12-19 | 101,48 $ | 106,15 $ | 83,18 $ / 125,62 $ | no | n/a | n/a | n/a |
| 112g | 2026-12-26 | 102,04 $ | 106,73 $ | 83,18 $ / 125,62 $ | no | n/a | n/a | n/a |
| 119g | 2027-01-02 | 105,77 $ | 110,64 $ | 83,18 $ / 125,62 $ | no | n/a | n/a | n/a |
| 126g | 2027-01-09 | 119,25 $ | 124,73 $ | 83,18 $ / 126,48 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 51 | 35,29% | 11,49% | 13,05% |
| 14g | 44 | 25,00% | 19,31% | 11,77% |
| 21g | 37 | 16,22% | 26,89% | 13,64% |
| 28g | 32 | 34,38% | 25,20% | 13,12% |
| 35g | 25 | 52,00% | 15,98% | 12,17% |
| 42g | 18 | 100,00% | 8,17% | 11,13% |
| 49g | 11 | 100,00% | 6,83% | 10,84% |
| 56g | 4 | 100,00% | 9,44% | 5,49% |
| 63g | 0 | n/a | n/a | n/a |
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
