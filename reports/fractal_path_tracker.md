<!-- FRACTAL_PATH_TRACKER_START -->
# Tracking percorso frattale SOL/BTC

Generato: 2026-09-04 05:32 UTC

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-09-04**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-02-19**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **103,67 $**
- Verdetto principale: **ANALOGIA DEBOLE / SCENARIO SECONDARIO**
- Somiglianza strutturale: **+66,88%**
- Aderenza live principale: **+71,40%**
- Errore medio live principale: **14,30%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE SOLO DI CONTESTO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **90**
- Osservazioni inclusive dal bottom: **91**
- Osservazioni da inizio programma/scanner: **64**
- Errore assoluto medio dal bottom: **11,85%**
- Errore assoluto medio da inizio programma: **14,30%**
- Gap firmato medio ultimi 7 giorni: **+9,96%**
- Errore assoluto medio ultimi 7 giorni: **9,96%**
- Gap ultimo giorno: **+8,18%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **+8,18%**
- Gap firmato medio 7g: **+9,96%**
- Errore assoluto medio 7g: **9,96%**
- Variazione recente gap: **+0,73%**
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
| 81 | 2026-08-26 | 2023-02-10 | 102,17 $ | 85,29 $ | +19,79% | da inizio programma |
| 82 | 2026-08-27 | 2023-02-11 | 109,21 $ | 86,15 $ | +26,76% | da inizio programma |
| 83 | 2026-08-28 | 2023-02-12 | 104,13 $ | 85,83 $ | +21,32% | da inizio programma |
| 84 | 2026-08-29 | 2023-02-13 | 105,65 $ | 85,91 $ | +22,98% | da inizio programma |
| 85 | 2026-08-30 | 2023-02-14 | 101,88 $ | 87,53 $ | +16,39% | da inizio programma |
| 86 | 2026-08-31 | 2023-02-15 | 103,00 $ | 95,75 $ | +7,56% | da inizio programma |
| 87 | 2026-09-01 | 2023-02-16 | 99,99 $ | 93,06 $ | +7,45% | da inizio programma |
| 88 | 2026-09-02 | 2023-02-17 | 100,39 $ | 96,77 $ | +3,74% | da inizio programma |
| 89 | 2026-09-03 | 2023-02-18 | 100,39 $ | 97,07 $ | +3,42% | da inizio programma |
| 90 | 2026-09-04 | 2023-02-19 | 103,67 $ | 95,83 $ | +8,18% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-09-11 | 92,81 $ | 100,40 $ | 98,76 $ / 105,81 $ | no | n/a | n/a | n/a |
| 14g | 2026-09-18 | 88,38 $ | 95,61 $ | 95,26 $ / 105,81 $ | no | n/a | n/a | n/a |
| 21g | 2026-09-25 | 87,31 $ | 94,45 $ | 86,03 $ / 105,81 $ | no | n/a | n/a | n/a |
| 28g | 2026-10-02 | 110,45 $ | 119,48 $ | 86,03 $ / 119,48 $ | no | n/a | n/a | n/a |
| 35g | 2026-10-09 | 110,28 $ | 119,30 $ | 86,03 $ / 120,74 $ | no | n/a | n/a | n/a |
| 42g | 2026-10-16 | 111,08 $ | 120,17 $ | 86,03 $ / 121,36 $ | no | n/a | n/a | n/a |
| 49g | 2026-10-23 | 111,61 $ | 120,74 $ | 86,03 $ / 121,36 $ | no | n/a | n/a | n/a |
| 56g | 2026-10-30 | 119,42 $ | 129,19 $ | 86,03 $ / 129,91 $ | no | n/a | n/a | n/a |
| 63g | 2026-11-06 | 108,69 $ | 117,58 $ | 86,03 $ / 129,91 $ | no | n/a | n/a | n/a |
| 70g | 2026-11-13 | 115,30 $ | 124,73 $ | 86,03 $ / 129,91 $ | no | n/a | n/a | n/a |
| 77g | 2026-11-20 | 112,09 $ | 121,26 $ | 86,03 $ / 129,91 $ | no | n/a | n/a | n/a |
| 84g | 2026-11-27 | 106,09 $ | 114,76 $ | 86,03 $ / 129,91 $ | no | n/a | n/a | n/a |
| 91g | 2026-12-04 | 105,39 $ | 114,01 $ | 86,03 $ / 129,91 $ | no | n/a | n/a | n/a |
| 98g | 2026-12-11 | 110,64 $ | 119,68 $ | 86,03 $ / 129,91 $ | no | n/a | n/a | n/a |
| 105g | 2026-12-18 | 106,83 $ | 115,57 $ | 86,03 $ / 129,91 $ | no | n/a | n/a | n/a |
| 112g | 2026-12-25 | 102,18 $ | 110,54 $ | 86,03 $ / 129,91 $ | no | n/a | n/a | n/a |
| 119g | 2027-01-01 | 103,74 $ | 112,23 $ | 86,03 $ / 129,91 $ | no | n/a | n/a | n/a |
| 126g | 2027-01-08 | 120,07 $ | 129,89 $ | 86,03 $ / 130,81 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 50 | 34,00% | 11,48% | 13,19% |
| 14g | 43 | 25,58% | 19,71% | 11,90% |
| 21g | 36 | 16,67% | 27,01% | 13,96% |
| 28g | 31 | 35,48% | 25,08% | 13,35% |
| 35g | 24 | 54,17% | 15,75% | 12,42% |
| 42g | 17 | 100,00% | 8,48% | 11,43% |
| 49g | 10 | 100,00% | 6,85% | 11,38% |
| 56g | 3 | 100,00% | 10,64% | 8,18% |
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
