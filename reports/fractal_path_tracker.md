<!-- FRACTAL_PATH_TRACKER_START -->
# Tracking percorso frattale SOL/BTC

Generato: 2026-08-15 05:33 UTC

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-08-15**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-01-30**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **75,39 $**
- Verdetto principale: **ANALOGIA DEBOLE / SCENARIO SECONDARIO**
- Somiglianza strutturale: **+57,75%**
- Aderenza live principale: **+69,23%**
- Errore medio live principale: **15,39%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE SOLO DI CONTESTO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **70**
- Osservazioni inclusive dal bottom: **71**
- Osservazioni da inizio programma/scanner: **44**
- Errore assoluto medio dal bottom: **11,83%**
- Errore assoluto medio da inizio programma: **15,39%**
- Gap firmato medio ultimi 7 giorni: **-16,43%**
- Errore assoluto medio ultimi 7 giorni: **16,43%**
- Gap ultimo giorno: **-16,21%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **-16,21%**
- Gap firmato medio 7g: **-16,43%**
- Errore assoluto medio 7g: **16,43%**
- Variazione recente gap: **+0,72%**
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
| 61 | 2026-08-06 | 2023-01-21 | 72,58 $ | 89,73 $ | -19,11% | da inizio programma |
| 62 | 2026-08-07 | 2023-01-22 | 73,64 $ | 89,50 $ | -17,72% | da inizio programma |
| 63 | 2026-08-08 | 2023-01-23 | 75,97 $ | 90,34 $ | -15,91% | da inizio programma |
| 64 | 2026-08-09 | 2023-01-24 | 76,21 $ | 89,17 $ | -14,53% | da inizio programma |
| 65 | 2026-08-10 | 2023-01-25 | 75,95 $ | 91,07 $ | -16,60% | da inizio programma |
| 66 | 2026-08-11 | 2023-01-26 | 76,20 $ | 90,73 $ | -16,02% | da inizio programma |
| 67 | 2026-08-12 | 2023-01-27 | 75,53 $ | 90,91 $ | -16,93% | da inizio programma |
| 68 | 2026-08-13 | 2023-01-28 | 76,18 $ | 90,72 $ | -16,03% | da inizio programma |
| 69 | 2026-08-14 | 2023-01-29 | 76,18 $ | 93,65 $ | -18,66% | da inizio programma |
| 70 | 2026-08-15 | 2023-01-30 | 75,39 $ | 89,97 $ | -16,21% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-08-22 | 89,66 $ | 75,13 $ | 75,13 $ / 78,31 $ | no | n/a | n/a | n/a |
| 14g | 2026-08-29 | 85,91 $ | 71,98 $ | 71,47 $ / 78,31 $ | no | n/a | n/a | n/a |
| 21g | 2026-09-05 | 97,81 $ | 81,96 $ | 71,47 $ / 81,96 $ | no | n/a | n/a | n/a |
| 28g | 2026-09-12 | 92,66 $ | 77,64 $ | 71,47 $ / 81,96 $ | no | n/a | n/a | n/a |
| 35g | 2026-09-19 | 88,36 $ | 74,04 $ | 71,47 $ / 81,96 $ | no | n/a | n/a | n/a |
| 42g | 2026-09-26 | 95,32 $ | 79,87 $ | 66,63 $ / 81,96 $ | no | n/a | n/a | n/a |
| 49g | 2026-10-03 | 109,38 $ | 91,65 $ | 66,63 $ / 92,55 $ | no | n/a | n/a | n/a |
| 56g | 2026-10-10 | 106,91 $ | 89,58 $ | 66,63 $ / 93,52 $ | no | n/a | n/a | n/a |
| 63g | 2026-10-17 | 109,47 $ | 91,73 $ | 66,63 $ / 94,00 $ | no | n/a | n/a | n/a |
| 70g | 2026-10-24 | 116,81 $ | 97,88 $ | 66,63 $ / 97,88 $ | no | n/a | n/a | n/a |
| 77g | 2026-10-31 | 115,99 $ | 97,19 $ | 66,63 $ / 100,63 $ | no | n/a | n/a | n/a |
| 84g | 2026-11-07 | 108,43 $ | 90,85 $ | 66,63 $ / 100,63 $ | no | n/a | n/a | n/a |
| 91g | 2026-11-14 | 110,66 $ | 92,72 $ | 66,63 $ / 100,63 $ | no | n/a | n/a | n/a |
| 98g | 2026-11-21 | 109,09 $ | 91,41 $ | 66,63 $ / 100,63 $ | no | n/a | n/a | n/a |
| 105g | 2026-11-28 | 107,12 $ | 89,76 $ | 66,63 $ / 100,63 $ | no | n/a | n/a | n/a |
| 112g | 2026-12-05 | 105,77 $ | 88,63 $ | 66,63 $ / 100,63 $ | no | n/a | n/a | n/a |
| 119g | 2026-12-12 | 109,30 $ | 91,58 $ | 66,63 $ / 100,63 $ | no | n/a | n/a | n/a |
| 126g | 2026-12-19 | 101,48 $ | 85,03 $ | 66,63 $ / 100,63 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 32 | 40,62% | 7,24% | 13,56% |
| 14g | 25 | 32,00% | 16,29% | 12,88% |
| 21g | 18 | 27,78% | 26,22% | 15,20% |
| 28g | 11 | 36,36% | 28,74% | 16,51% |
| 35g | 4 | 0,00% | 29,07% | 17,43% |
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
