<!-- FRACTAL_PATH_TRACKER_START -->
# Tracking percorso frattale SOL/BTC

Generato: 2026-07-24 05:14 UTC

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-07-24**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-01-08**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **75,72 $**
- Verdetto principale: **ANALOGIA DEBOLE / SCENARIO SECONDARIO**
- Somiglianza strutturale: **+64,81%**
- Aderenza live principale: **+63,97%**
- Errore medio live principale: **18,01%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE SOLO DI CONTESTO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **48**
- Osservazioni inclusive dal bottom: **49**
- Osservazioni da inizio programma/scanner: **22**
- Errore assoluto medio dal bottom: **11,41%**
- Errore assoluto medio da inizio programma: **18,01%**
- Gap firmato medio ultimi 7 giorni: **+15,95%**
- Errore assoluto medio ultimi 7 giorni: **15,95%**
- Gap ultimo giorno: **+12,47%**
- Stato aderenza: **STACCATO / MOLTO IN ANTICIPO**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **+12,47%**
- Gap firmato medio 7g: **+15,95%**
- Errore assoluto medio 7g: **15,95%**
- Variazione recente gap: **-5,30%**
- Stato gap: **IN DEVIAZIONE SOPRA IL FRATTALE**
- Trend gap: **SOL resta sopra il percorso ancorato, ma sta riducendo il distacco**

Soglie operative del grafico:

- entro **±5%**: percorso vicino;
- tra **±5% e ±12%**: deviazione gestibile;
- oltre **±12%**: frattale non abbastanza aderente per conferma operativa;
- oltre **±18%**: disallineamento marcato.

## Ultimi giorni del confronto ancorato

|   Giorno | Data SOL   | Data BTC eq.   | SOL reale   | Percorso ancorato   | Gap firmato   | Fase                |
|---------:|:-----------|:---------------|:------------|:--------------------|:--------------|:--------------------|
| 39 | 2026-07-15 | 2022-12-30 | 77,26 $ | 65,40 $ | +18,14% | da inizio programma |
| 40 | 2026-07-16 | 2022-12-31 | 75,27 $ | 65,18 $ | +15,48% | da inizio programma |
| 41 | 2026-07-17 | 2023-01-01 | 75,01 $ | 65,49 $ | +14,54% | da inizio programma |
| 42 | 2026-07-18 | 2023-01-02 | 75,46 $ | 65,74 $ | +14,79% | da inizio programma |
| 43 | 2026-07-19 | 2023-01-03 | 76,36 $ | 65,71 $ | +16,21% | da inizio programma |
| 44 | 2026-07-20 | 2023-01-04 | 77,79 $ | 66,43 $ | +17,11% | da inizio programma |
| 45 | 2026-07-21 | 2023-01-05 | 78,11 $ | 66,32 $ | +17,77% | da inizio programma |
| 46 | 2026-07-22 | 2023-01-06 | 77,91 $ | 66,78 $ | +16,66% | da inizio programma |
| 47 | 2026-07-23 | 2023-01-07 | 77,91 $ | 66,79 $ | +16,64% | da inizio programma |
| 48 | 2026-07-24 | 2023-01-08 | 75,72 $ | 67,33 $ | +12,47% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-07-31 | 82,25 $ | 92,51 $ | 75,72 $ / 92,93 $ | no | n/a | n/a | n/a |
| 14g | 2026-08-07 | 89,50 $ | 100,66 $ | 75,72 $ / 100,91 $ | no | n/a | n/a | n/a |
| 21g | 2026-08-14 | 93,65 $ | 105,33 $ | 75,72 $ / 105,33 $ | no | n/a | n/a | n/a |
| 28g | 2026-08-21 | 90,43 $ | 101,70 $ | 75,72 $ / 105,33 $ | no | n/a | n/a | n/a |
| 35g | 2026-08-28 | 85,83 $ | 96,53 $ | 75,72 $ / 105,33 $ | no | n/a | n/a | n/a |
| 42g | 2026-09-04 | 95,83 $ | 107,78 $ | 75,72 $ / 109,17 $ | no | n/a | n/a | n/a |
| 49g | 2026-09-11 | 92,81 $ | 104,38 $ | 75,72 $ / 110,00 $ | no | n/a | n/a | n/a |
| 56g | 2026-09-18 | 88,38 $ | 99,40 $ | 75,72 $ / 110,00 $ | no | n/a | n/a | n/a |
| 63g | 2026-09-25 | 87,31 $ | 98,19 $ | 75,72 $ / 110,00 $ | no | n/a | n/a | n/a |
| 70g | 2026-10-02 | 110,45 $ | 124,22 $ | 75,72 $ / 124,22 $ | no | n/a | n/a | n/a |
| 77g | 2026-10-09 | 110,28 $ | 124,03 $ | 75,72 $ / 125,53 $ | no | n/a | n/a | n/a |
| 84g | 2026-10-16 | 111,08 $ | 124,93 $ | 75,72 $ / 126,17 $ | no | n/a | n/a | n/a |
| 91g | 2026-10-23 | 111,61 $ | 125,53 $ | 75,72 $ / 126,17 $ | no | n/a | n/a | n/a |
| 98g | 2026-10-30 | 119,42 $ | 134,31 $ | 75,72 $ / 135,06 $ | no | n/a | n/a | n/a |
| 105g | 2026-11-06 | 108,69 $ | 122,24 $ | 75,72 $ / 135,06 $ | no | n/a | n/a | n/a |
| 112g | 2026-11-13 | 115,30 $ | 129,67 $ | 75,72 $ / 135,06 $ | no | n/a | n/a | n/a |
| 119g | 2026-11-20 | 112,09 $ | 126,07 $ | 75,72 $ / 135,06 $ | no | n/a | n/a | n/a |
| 126g | 2026-11-27 | 106,09 $ | 119,31 $ | 75,72 $ / 135,06 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 10 | 50,00% | 1,32% | 15,77% |
| 14g | 3 | 66,67% | 1,91% | 12,47% |
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
