<!-- FRACTAL_PATH_TRACKER_START -->
# Tracking percorso frattale SOL/BTC

Generato: 2026-08-03 05:15 UTC

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-08-03**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-01-18**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **72,93 $**
- Verdetto principale: **ANALOGIA DEBOLE / SCENARIO SECONDARIO**
- Somiglianza strutturale: **+56,90%**
- Aderenza live principale: **+69,79%**
- Errore medio live principale: **15,10%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE SOLO DI CONTESTO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **58**
- Osservazioni inclusive dal bottom: **59**
- Osservazioni da inizio programma/scanner: **32**
- Errore assoluto medio dal bottom: **10,95%**
- Errore assoluto medio da inizio programma: **15,10%**
- Gap firmato medio ultimi 7 giorni: **-9,50%**
- Errore assoluto medio ultimi 7 giorni: **9,50%**
- Gap ultimo giorno: **-10,51%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **-10,51%**
- Gap firmato medio 7g: **-9,50%**
- Errore assoluto medio 7g: **9,50%**
- Variazione recente gap: **+0,99%**
- Stato gap: **SOTTO IL FRATTALE**
- Trend gap: **SOL e vicino al percorso ancorato**

Soglie operative del grafico:

- entro **±5%**: percorso vicino;
- tra **±5% e ±12%**: deviazione gestibile;
- oltre **±12%**: frattale non abbastanza aderente per conferma operativa;
- oltre **±18%**: disallineamento marcato.

## Ultimi giorni del confronto ancorato

|   Giorno | Data SOL   | Data BTC eq.   | SOL reale   | Percorso ancorato   | Gap firmato   | Fase                |
|---------:|:-----------|:---------------|:------------|:--------------------|:--------------|:--------------------|
| 49 | 2026-07-25 | 2023-01-09 | 74,43 $ | 67,74 $ | +9,87% | da inizio programma |
| 50 | 2026-07-26 | 2023-01-10 | 76,60 $ | 68,73 $ | +11,46% | da inizio programma |
| 51 | 2026-07-27 | 2023-01-11 | 74,14 $ | 70,65 $ | +4,94% | da inizio programma |
| 52 | 2026-07-28 | 2023-01-12 | 73,70 $ | 74,33 $ | -0,85% | da inizio programma |
| 53 | 2026-07-29 | 2023-01-13 | 73,60 $ | 78,43 $ | -6,16% | da inizio programma |
| 54 | 2026-07-30 | 2023-01-14 | 74,47 $ | 82,63 $ | -9,88% | da inizio programma |
| 55 | 2026-07-31 | 2023-01-15 | 72,79 $ | 82,25 $ | -11,51% | da inizio programma |
| 56 | 2026-08-01 | 2023-01-16 | 71,87 $ | 83,39 $ | -13,82% | da inizio programma |
| 57 | 2026-08-02 | 2023-01-17 | 71,87 $ | 83,36 $ | -13,79% | da inizio programma |
| 58 | 2026-08-03 | 2023-01-18 | 72,93 $ | 81,50 $ | -10,51% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-08-10 | 91,07 $ | 81,49 $ | 72,93 $ / 81,49 $ | no | n/a | n/a | n/a |
| 14g | 2026-08-17 | 93,45 $ | 83,63 $ | 72,93 $ / 83,81 $ | no | n/a | n/a | n/a |
| 21g | 2026-08-24 | 90,36 $ | 80,86 $ | 72,93 $ / 83,81 $ | no | n/a | n/a | n/a |
| 28g | 2026-08-31 | 95,75 $ | 85,69 $ | 72,93 $ / 85,69 $ | no | n/a | n/a | n/a |
| 35g | 2026-09-07 | 95,29 $ | 85,27 $ | 72,93 $ / 87,53 $ | no | n/a | n/a | n/a |
| 42g | 2026-09-14 | 93,15 $ | 83,36 $ | 72,93 $ / 87,53 $ | no | n/a | n/a | n/a |
| 49g | 2026-09-21 | 85,55 $ | 76,56 $ | 72,93 $ / 87,53 $ | no | n/a | n/a | n/a |
| 56g | 2026-09-28 | 96,02 $ | 85,93 $ | 71,16 $ / 87,53 $ | no | n/a | n/a | n/a |
| 63g | 2026-10-05 | 107,57 $ | 96,26 $ | 71,16 $ / 99,32 $ | no | n/a | n/a | n/a |
| 70g | 2026-10-12 | 111,67 $ | 99,93 $ | 71,16 $ / 99,93 $ | no | n/a | n/a | n/a |
| 77g | 2026-10-19 | 111,00 $ | 99,33 $ | 71,16 $ / 100,39 $ | no | n/a | n/a | n/a |
| 84g | 2026-10-26 | 118,72 $ | 106,24 $ | 71,16 $ / 106,58 $ | no | n/a | n/a | n/a |
| 91g | 2026-11-02 | 113,54 $ | 101,60 $ | 71,16 $ / 107,47 $ | no | n/a | n/a | n/a |
| 98g | 2026-11-09 | 111,96 $ | 100,19 $ | 71,16 $ / 107,47 $ | no | n/a | n/a | n/a |
| 105g | 2026-11-16 | 114,26 $ | 102,25 $ | 71,16 $ / 107,47 $ | no | n/a | n/a | n/a |
| 112g | 2026-11-23 | 108,81 $ | 97,37 $ | 71,16 $ / 107,47 $ | no | n/a | n/a | n/a |
| 119g | 2026-11-30 | 107,93 $ | 96,58 $ | 71,16 $ / 107,47 $ | no | n/a | n/a | n/a |
| 126g | 2026-12-07 | 103,74 $ | 92,83 $ | 71,16 $ / 107,47 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 20 | 20,00% | 8,59% | 11,84% |
| 14g | 13 | 7,69% | 14,27% | 9,32% |
| 21g | 6 | 0,00% | 24,24% | 12,41% |
| 28g | 0 | n/a | n/a | n/a |
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
