<!-- FRACTAL_PATH_TRACKER_START -->
# Tracking percorso frattale SOL/BTC

Generato: 2026-08-11 05:21 UTC

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-08-11**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-01-26**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **75,98 $**
- Verdetto principale: **ANALOGIA DEBOLE / SCENARIO SECONDARIO**
- Somiglianza strutturale: **+57,11%**
- Aderenza live principale: **+69,55%**
- Errore medio live principale: **15,23%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE SOLO DI CONTESTO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **66**
- Osservazioni inclusive dal bottom: **67**
- Osservazioni da inizio programma/scanner: **40**
- Errore assoluto medio dal bottom: **11,52%**
- Errore assoluto medio da inizio programma: **15,23%**
- Gap firmato medio ultimi 7 giorni: **-16,72%**
- Errore assoluto medio ultimi 7 giorni: **16,72%**
- Gap ultimo giorno: **-16,26%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **-16,26%**
- Gap firmato medio 7g: **-16,72%**
- Errore assoluto medio 7g: **16,72%**
- Variazione recente gap: **-0,35%**
- Stato gap: **IN DEVIAZIONE SOTTO IL FRATTALE**
- Trend gap: **SOL e vicino al percorso ancorato**

Soglie operative del grafico:

- entro **±5%**: percorso vicino;
- tra **±5% e ±12%**: deviazione gestibile;
- oltre **±12%**: frattale non abbastanza aderente per conferma operativa;
- oltre **±18%**: disallineamento marcato.

## Ultimi giorni del confronto ancorato

|   Giorno | Data SOL   | Data BTC eq.   | SOL reale   | Percorso ancorato   | Gap firmato   | Fase                |
|---------:|:-----------|:---------------|:------------|:--------------------|:--------------|:--------------------|
| 57 | 2026-08-02 | 2023-01-17 | 73,45 $ | 83,36 $ | -11,89% | da inizio programma |
| 58 | 2026-08-03 | 2023-01-18 | 73,47 $ | 81,50 $ | -9,85% | da inizio programma |
| 59 | 2026-08-04 | 2023-01-19 | 73,72 $ | 83,07 $ | -11,25% | da inizio programma |
| 60 | 2026-08-05 | 2023-01-20 | 73,96 $ | 89,33 $ | -17,20% | da inizio programma |
| 61 | 2026-08-06 | 2023-01-21 | 72,58 $ | 89,73 $ | -19,11% | da inizio programma |
| 62 | 2026-08-07 | 2023-01-22 | 73,64 $ | 89,50 $ | -17,72% | da inizio programma |
| 63 | 2026-08-08 | 2023-01-23 | 75,97 $ | 90,34 $ | -15,91% | da inizio programma |
| 64 | 2026-08-09 | 2023-01-24 | 76,21 $ | 89,17 $ | -14,53% | da inizio programma |
| 65 | 2026-08-10 | 2023-01-25 | 76,21 $ | 91,07 $ | -16,31% | da inizio programma |
| 66 | 2026-08-11 | 2023-01-26 | 75,98 $ | 90,73 $ | -16,26% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-08-18 | 92,46 $ | 77,43 $ | 75,34 $ / 78,43 $ | no | n/a | n/a | n/a |
| 14g | 2026-08-25 | 85,95 $ | 71,98 $ | 71,98 $ / 78,43 $ | no | n/a | n/a | n/a |
| 21g | 2026-09-01 | 93,06 $ | 77,93 $ | 71,42 $ / 80,19 $ | no | n/a | n/a | n/a |
| 28g | 2026-09-08 | 94,33 $ | 79,00 $ | 71,42 $ / 81,91 $ | no | n/a | n/a | n/a |
| 35g | 2026-09-15 | 92,48 $ | 77,44 $ | 71,42 $ / 81,91 $ | no | n/a | n/a | n/a |
| 42g | 2026-09-22 | 80,21 $ | 67,17 $ | 67,17 $ / 81,91 $ | no | n/a | n/a | n/a |
| 49g | 2026-09-29 | 98,69 $ | 82,64 $ | 66,59 $ / 82,64 $ | no | n/a | n/a | n/a |
| 56g | 2026-10-06 | 111,61 $ | 93,47 $ | 66,59 $ / 93,47 $ | no | n/a | n/a | n/a |
| 63g | 2026-10-13 | 110,43 $ | 92,48 $ | 66,59 $ / 93,52 $ | no | n/a | n/a | n/a |
| 70g | 2026-10-20 | 110,47 $ | 92,51 $ | 66,59 $ / 93,94 $ | no | n/a | n/a | n/a |
| 77g | 2026-10-27 | 119,75 $ | 100,28 $ | 66,59 $ / 100,28 $ | no | n/a | n/a | n/a |
| 84g | 2026-11-03 | 111,27 $ | 93,18 $ | 66,59 $ / 100,57 $ | no | n/a | n/a | n/a |
| 91g | 2026-11-10 | 116,10 $ | 97,23 $ | 66,59 $ / 100,57 $ | no | n/a | n/a | n/a |
| 98g | 2026-11-17 | 113,64 $ | 95,16 $ | 66,59 $ / 100,57 $ | no | n/a | n/a | n/a |
| 105g | 2026-11-24 | 106,36 $ | 89,07 $ | 66,59 $ / 100,57 $ | no | n/a | n/a | n/a |
| 112g | 2026-12-01 | 105,70 $ | 88,51 $ | 66,59 $ / 100,57 $ | no | n/a | n/a | n/a |
| 119g | 2026-12-08 | 104,30 $ | 87,34 $ | 66,59 $ / 100,57 $ | no | n/a | n/a | n/a |
| 126g | 2026-12-15 | 105,65 $ | 88,47 $ | 66,59 $ / 100,57 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 28 | 42,86% | 8,14% | 13,04% |
| 14g | 21 | 19,05% | 17,92% | 12,01% |
| 21g | 14 | 21,43% | 26,05% | 14,61% |
| 28g | 7 | 28,57% | 28,97% | 16,15% |
| 35g | 0 | n/a | n/a | n/a |
| 42g | 0 | n/a | n/a | n/a |
| 49g | 0 | n/a | n/a | n/a |
| 56g | 0 | n/a | n/a | n/a |
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
