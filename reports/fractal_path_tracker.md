<!-- FRACTAL_PATH_TRACKER_START -->
# Tracking percorso frattale SOL/BTC

Generato: 2026-08-08 05:18 UTC

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-08-08**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-01-23**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **74,58 $**
- Verdetto principale: **ANALOGIA DEBOLE / SCENARIO SECONDARIO**
- Somiglianza strutturale: **+55,47%**
- Aderenza live principale: **+69,48%**
- Errore medio live principale: **15,26%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE SOLO DI CONTESTO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **63**
- Osservazioni inclusive dal bottom: **64**
- Osservazioni da inizio programma/scanner: **37**
- Errore assoluto medio dal bottom: **11,36%**
- Errore assoluto medio da inizio programma: **15,26%**
- Gap firmato medio ultimi 7 giorni: **-15,09%**
- Errore assoluto medio ultimi 7 giorni: **15,09%**
- Gap ultimo giorno: **-17,45%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **-17,45%**
- Gap firmato medio 7g: **-15,09%**
- Errore assoluto medio 7g: **15,09%**
- Variazione recente gap: **-0,25%**
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
| 54 | 2026-07-30 | 2023-01-14 | 74,47 $ | 82,63 $ | -9,88% | da inizio programma |
| 55 | 2026-07-31 | 2023-01-15 | 72,79 $ | 82,25 $ | -11,51% | da inizio programma |
| 56 | 2026-08-01 | 2023-01-16 | 71,87 $ | 83,39 $ | -13,82% | da inizio programma |
| 57 | 2026-08-02 | 2023-01-17 | 73,45 $ | 83,36 $ | -11,89% | da inizio programma |
| 58 | 2026-08-03 | 2023-01-18 | 73,47 $ | 81,50 $ | -9,85% | da inizio programma |
| 59 | 2026-08-04 | 2023-01-19 | 73,72 $ | 83,07 $ | -11,25% | da inizio programma |
| 60 | 2026-08-05 | 2023-01-20 | 73,96 $ | 89,33 $ | -17,20% | da inizio programma |
| 61 | 2026-08-06 | 2023-01-21 | 72,58 $ | 89,73 $ | -19,11% | da inizio programma |
| 62 | 2026-08-07 | 2023-01-22 | 72,58 $ | 89,50 $ | -18,91% | da inizio programma |
| 63 | 2026-08-08 | 2023-01-23 | 74,58 $ | 90,34 $ | -17,45% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-08-15 | 89,97 $ | 74,27 $ | 73,61 $ / 77,31 $ | no | n/a | n/a | n/a |
| 14g | 2026-08-22 | 89,66 $ | 74,01 $ | 73,61 $ / 77,31 $ | no | n/a | n/a | n/a |
| 21g | 2026-08-29 | 85,91 $ | 70,92 $ | 70,41 $ / 77,31 $ | no | n/a | n/a | n/a |
| 28g | 2026-09-05 | 97,81 $ | 80,74 $ | 70,41 $ / 80,74 $ | no | n/a | n/a | n/a |
| 35g | 2026-09-12 | 92,66 $ | 76,49 $ | 70,41 $ / 80,74 $ | no | n/a | n/a | n/a |
| 42g | 2026-09-19 | 88,36 $ | 72,94 $ | 70,41 $ / 80,74 $ | no | n/a | n/a | n/a |
| 49g | 2026-09-26 | 95,32 $ | 78,69 $ | 65,65 $ / 80,74 $ | no | n/a | n/a | n/a |
| 56g | 2026-10-03 | 109,38 $ | 90,30 $ | 65,65 $ / 91,18 $ | no | n/a | n/a | n/a |
| 63g | 2026-10-10 | 106,91 $ | 88,26 $ | 65,65 $ / 92,14 $ | no | n/a | n/a | n/a |
| 70g | 2026-10-17 | 109,47 $ | 90,37 $ | 65,65 $ / 92,61 $ | no | n/a | n/a | n/a |
| 77g | 2026-10-24 | 116,81 $ | 96,43 $ | 65,65 $ / 96,43 $ | no | n/a | n/a | n/a |
| 84g | 2026-10-31 | 115,99 $ | 95,75 $ | 65,65 $ / 99,14 $ | no | n/a | n/a | n/a |
| 91g | 2026-11-07 | 108,43 $ | 89,51 $ | 65,65 $ / 99,14 $ | no | n/a | n/a | n/a |
| 98g | 2026-11-14 | 110,66 $ | 91,35 $ | 65,65 $ / 99,14 $ | no | n/a | n/a | n/a |
| 105g | 2026-11-21 | 109,09 $ | 90,06 $ | 65,65 $ / 99,14 $ | no | n/a | n/a | n/a |
| 112g | 2026-11-28 | 107,12 $ | 88,43 $ | 65,65 $ / 99,14 $ | no | n/a | n/a | n/a |
| 119g | 2026-12-05 | 105,77 $ | 87,32 $ | 65,65 $ / 99,14 $ | no | n/a | n/a | n/a |
| 126g | 2026-12-12 | 109,30 $ | 90,23 $ | 65,65 $ / 99,14 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 25 | 32,00% | 8,63% | 12,81% |
| 14g | 18 | 11,11% | 17,75% | 11,49% |
| 21g | 11 | 0,00% | 25,93% | 14,55% |
| 28g | 4 | 0,00% | 30,69% | 18,18% |
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
