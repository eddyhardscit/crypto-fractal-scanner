<!-- FRACTAL_PATH_TRACKER_START -->
# Tracking percorso frattale SOL/BTC

Generato: 2026-09-17 05:32 UTC

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-09-17**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-03-04**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **99,61 $**
- Verdetto principale: **ANALOGIA DEBOLE / SCENARIO SECONDARIO**
- Somiglianza strutturale: **+71,56%**
- Aderenza live principale: **+73,04%**
- Errore medio live principale: **13,48%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE SOLO DI CONTESTO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **103**
- Osservazioni inclusive dal bottom: **104**
- Osservazioni da inizio programma/scanner: **77**
- Errore assoluto medio dal bottom: **11,55%**
- Errore assoluto medio da inizio programma: **13,48%**
- Gap firmato medio ultimi 7 giorni: **+9,56%**
- Errore assoluto medio ultimi 7 giorni: **9,56%**
- Gap ultimo giorno: **+13,12%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **+13,12%**
- Gap firmato medio 7g: **+9,56%**
- Errore assoluto medio 7g: **9,56%**
- Variazione recente gap: **+3,09%**
- Stato gap: **IN DEVIAZIONE SOPRA IL FRATTALE**
- Trend gap: **SOL sta aumentando il distacco sopra il percorso ancorato**

Soglie operative del grafico:

- entro **±5%**: percorso vicino;
- tra **±5% e ±12%**: deviazione gestibile;
- oltre **±12%**: frattale non abbastanza aderente per conferma operativa;
- oltre **±18%**: disallineamento marcato.

## Ultimi giorni del confronto ancorato

|   Giorno | Data SOL   | Data BTC eq.   | SOL reale   | Percorso ancorato   | Gap firmato   | Fase                |
|---------:|:-----------|:---------------|:------------|:--------------------|:--------------|:--------------------|
| 94 | 2026-09-08 | 2023-02-23 | 103,33 $ | 94,33 $ | +9,53% | da inizio programma |
| 95 | 2026-09-09 | 2023-02-24 | 101,61 $ | 91,38 $ | +11,19% | da inizio programma |
| 96 | 2026-09-10 | 2023-02-25 | 98,69 $ | 91,29 $ | +8,10% | da inizio programma |
| 97 | 2026-09-11 | 2023-02-26 | 102,40 $ | 92,81 $ | +10,33% | da inizio programma |
| 98 | 2026-09-12 | 2023-02-27 | 101,79 $ | 92,66 $ | +9,85% | da inizio programma |
| 99 | 2026-09-13 | 2023-02-28 | 99,25 $ | 91,18 $ | +8,84% | da inizio programma |
| 100 | 2026-09-14 | 2023-03-01 | 102,50 $ | 93,15 $ | +10,03% | da inizio programma |
| 101 | 2026-09-15 | 2023-03-02 | 96,89 $ | 92,48 $ | +4,77% | da inizio programma |
| 102 | 2026-09-16 | 2023-03-03 | 96,89 $ | 88,09 $ | +9,99% | da inizio programma |
| 103 | 2026-09-17 | 2023-03-04 | 99,61 $ | 88,06 $ | +13,12% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-09-24 | 81,28 $ | 91,94 $ | 89,96 $ / 99,98 $ | no | n/a | n/a | n/a |
| 14g | 2026-10-01 | 106,22 $ | 120,16 $ | 89,96 $ / 122,21 $ | no | n/a | n/a | n/a |
| 21g | 2026-10-08 | 108,31 $ | 122,52 $ | 89,96 $ / 126,26 $ | no | n/a | n/a | n/a |
| 28g | 2026-10-15 | 111,92 $ | 126,60 $ | 89,96 $ / 126,90 $ | no | n/a | n/a | n/a |
| 35g | 2026-10-22 | 110,09 $ | 124,54 $ | 89,96 $ / 126,90 $ | no | n/a | n/a | n/a |
| 42g | 2026-10-29 | 119,43 $ | 135,10 $ | 89,96 $ / 135,85 $ | no | n/a | n/a | n/a |
| 49g | 2026-11-05 | 109,58 $ | 123,96 $ | 89,96 $ / 135,85 $ | no | n/a | n/a | n/a |
| 56g | 2026-11-12 | 115,22 $ | 130,34 $ | 89,96 $ / 135,85 $ | no | n/a | n/a | n/a |
| 63g | 2026-11-19 | 113,86 $ | 128,80 $ | 89,96 $ / 135,85 $ | no | n/a | n/a | n/a |
| 70g | 2026-11-26 | 105,51 $ | 119,35 $ | 89,96 $ / 135,85 $ | no | n/a | n/a | n/a |
| 77g | 2026-12-03 | 106,87 $ | 120,89 $ | 89,96 $ / 135,85 $ | no | n/a | n/a | n/a |
| 84g | 2026-12-10 | 105,84 $ | 119,73 $ | 89,96 $ / 135,85 $ | no | n/a | n/a | n/a |
| 91g | 2026-12-17 | 106,66 $ | 120,65 $ | 89,96 $ / 135,85 $ | no | n/a | n/a | n/a |
| 98g | 2026-12-24 | 101,83 $ | 115,20 $ | 89,96 $ / 135,85 $ | no | n/a | n/a | n/a |
| 105g | 2026-12-31 | 104,43 $ | 118,14 $ | 89,96 $ / 135,85 $ | no | n/a | n/a | n/a |
| 112g | 2027-01-07 | 120,34 $ | 136,13 $ | 89,96 $ / 136,78 $ | no | n/a | n/a | n/a |
| 119g | 2027-01-14 | 120,50 $ | 136,31 $ | 89,96 $ / 136,78 $ | no | n/a | n/a | n/a |
| 126g | 2027-01-21 | 119,33 $ | 134,99 $ | 89,96 $ / 138,84 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 63 | 39,68% | 9,96% | 12,39% |
| 14g | 56 | 28,57% | 16,72% | 11,31% |
| 21g | 49 | 18,37% | 24,43% | 12,63% |
| 28g | 42 | 26,19% | 26,59% | 12,26% |
| 35g | 35 | 37,14% | 19,70% | 11,30% |
| 42g | 30 | 66,67% | 12,74% | 10,51% |
| 49g | 23 | 86,96% | 6,82% | 10,18% |
| 56g | 16 | 100,00% | 6,42% | 9,09% |
| 63g | 9 | 100,00% | 6,71% | 9,56% |
| 70g | 2 | 100,00% | 3,69% | n/a |
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
