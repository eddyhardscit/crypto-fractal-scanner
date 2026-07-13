<!-- FRACTAL_PATH_TRACKER_START -->
# Tracking percorso frattale SOL/BTC

Generato: 2026-07-13 06:28 UTC

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-07-13**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2022-12-28**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **76,29 $**
- Verdetto principale: **ANALOGIA DEBOLE / SCENARIO SECONDARIO**
- Somiglianza strutturale: **+64,96%**
- Aderenza live principale: **+59,98%**
- Errore medio live principale: **20,01%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE SOLO DI CONTESTO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **37**
- Osservazioni inclusive dal bottom: **38**
- Osservazioni da inizio programma/scanner: **11**
- Errore assoluto medio dal bottom: **10,07%**
- Errore assoluto medio da inizio programma: **20,01%**
- Gap firmato medio ultimi 7 giorni: **+17,64%**
- Errore assoluto medio ultimi 7 giorni: **17,64%**
- Gap ultimo giorno: **+17,00%**
- Stato aderenza: **STACCATO / MOLTO IN ANTICIPO**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **+17,00%**
- Gap firmato medio 7g: **+17,64%**
- Errore assoluto medio 7g: **17,64%**
- Variazione recente gap: **-0,67%**
- Stato gap: **IN DEVIAZIONE SOPRA IL FRATTALE**
- Trend gap: **SOL resta sopra il percorso ancorato con distacco quasi stabile**

Soglie operative del grafico:

- entro **±5%**: percorso vicino;
- tra **±5% e ±12%**: deviazione gestibile;
- oltre **±12%**: frattale non abbastanza aderente per conferma operativa;
- oltre **±18%**: disallineamento marcato.

## Ultimi giorni del confronto ancorato

|   Giorno | Data SOL   | Data BTC eq.   | SOL reale   | Percorso ancorato   | Gap firmato   | Fase                |
|---------:|:-----------|:---------------|:------------|:--------------------|:--------------|:--------------------|
| 28 | 2026-07-04 | 2022-12-19 | 81,65 $ | 64,76 $ | +26,08% | da inizio programma |
| 29 | 2026-07-05 | 2022-12-20 | 81,42 $ | 66,60 $ | +22,26% | da inizio programma |
| 30 | 2026-07-06 | 2022-12-21 | 81,92 $ | 66,25 $ | +23,65% | da inizio programma |
| 31 | 2026-07-07 | 2022-12-22 | 80,65 $ | 66,30 $ | +21,64% | da inizio programma |
| 32 | 2026-07-08 | 2022-12-23 | 77,79 $ | 66,17 $ | +17,56% | da inizio programma |
| 33 | 2026-07-09 | 2022-12-24 | 78,05 $ | 66,37 $ | +17,60% | da inizio programma |
| 34 | 2026-07-10 | 2022-12-25 | 78,07 $ | 66,34 $ | +17,67% | da inizio programma |
| 35 | 2026-07-11 | 2022-12-26 | 76,82 $ | 66,65 $ | +15,26% | da inizio programma |
| 36 | 2026-07-12 | 2022-12-27 | 76,87 $ | 65,85 $ | +16,74% | da inizio programma |
| 37 | 2026-07-13 | 2022-12-28 | 76,29 $ | 65,20 $ | +17,00% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-07-20 | 66,43 $ | 77,72 $ | 76,27 $ / 77,72 $ | no | n/a | n/a | n/a |
| 14g | 2026-07-27 | 70,65 $ | 82,66 $ | 76,27 $ / 82,66 $ | no | n/a | n/a | n/a |
| 21g | 2026-08-03 | 81,50 $ | 95,35 $ | 76,27 $ / 97,57 $ | no | n/a | n/a | n/a |
| 28g | 2026-08-10 | 91,07 $ | 106,55 $ | 76,27 $ / 106,55 $ | no | n/a | n/a | n/a |
| 35g | 2026-08-17 | 93,45 $ | 109,34 $ | 76,27 $ / 109,58 $ | no | n/a | n/a | n/a |
| 42g | 2026-08-24 | 90,36 $ | 105,73 $ | 76,27 $ / 109,58 $ | no | n/a | n/a | n/a |
| 49g | 2026-08-31 | 95,75 $ | 112,03 $ | 76,27 $ / 112,03 $ | no | n/a | n/a | n/a |
| 56g | 2026-09-07 | 95,29 $ | 111,49 $ | 76,27 $ / 114,44 $ | no | n/a | n/a | n/a |
| 63g | 2026-09-14 | 93,15 $ | 108,99 $ | 76,27 $ / 114,44 $ | no | n/a | n/a | n/a |
| 70g | 2026-09-21 | 85,55 $ | 100,10 $ | 76,27 $ / 114,44 $ | no | n/a | n/a | n/a |
| 77g | 2026-09-28 | 96,02 $ | 112,35 $ | 76,27 $ / 114,44 $ | no | n/a | n/a | n/a |
| 84g | 2026-10-05 | 107,57 $ | 125,86 $ | 76,27 $ / 129,86 $ | no | n/a | n/a | n/a |
| 91g | 2026-10-12 | 111,67 $ | 130,66 $ | 76,27 $ / 130,66 $ | no | n/a | n/a | n/a |
| 98g | 2026-10-19 | 111,00 $ | 129,87 $ | 76,27 $ / 131,26 $ | no | n/a | n/a | n/a |
| 105g | 2026-10-26 | 118,72 $ | 138,91 $ | 76,27 $ / 139,35 $ | no | n/a | n/a | n/a |
| 112g | 2026-11-02 | 113,54 $ | 132,84 $ | 76,27 $ / 140,51 $ | no | n/a | n/a | n/a |
| 119g | 2026-11-09 | 111,96 $ | 131,00 $ | 76,27 $ / 140,51 $ | no | n/a | n/a | n/a |
| 126g | 2026-11-16 | 114,26 $ | 133,69 $ | 76,27 $ / 140,51 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 0 | n/a | n/a | n/a |
| 14g | 0 | n/a | n/a | n/a |
| 21g | 0 | n/a | n/a | n/a |
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
