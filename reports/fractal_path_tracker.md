<!-- FRACTAL_PATH_TRACKER_START -->
# Tracking percorso frattale SOL/BTC

Generato: 2026-07-25 05:14 UTC

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-07-25**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-01-09**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **74,20 $**
- Verdetto principale: **ANALOGIA DEBOLE / SCENARIO SECONDARIO**
- Somiglianza strutturale: **+64,53%**
- Aderenza live principale: **+64,96%**
- Errore medio live principale: **17,52%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE SOLO DI CONTESTO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **49**
- Osservazioni inclusive dal bottom: **50**
- Osservazioni da inizio programma/scanner: **23**
- Errore assoluto medio dal bottom: **11,31%**
- Errore assoluto medio da inizio programma: **17,52%**
- Gap firmato medio ultimi 7 giorni: **+14,79%**
- Errore assoluto medio ultimi 7 giorni: **14,79%**
- Gap ultimo giorno: **+9,53%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **+9,53%**
- Gap firmato medio 7g: **+14,79%**
- Errore assoluto medio 7g: **14,79%**
- Variazione recente gap: **-7,13%**
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
| 40 | 2026-07-16 | 2022-12-31 | 75,27 $ | 65,18 $ | +15,48% | da inizio programma |
| 41 | 2026-07-17 | 2023-01-01 | 75,01 $ | 65,49 $ | +14,54% | da inizio programma |
| 42 | 2026-07-18 | 2023-01-02 | 75,46 $ | 65,74 $ | +14,79% | da inizio programma |
| 43 | 2026-07-19 | 2023-01-03 | 76,36 $ | 65,71 $ | +16,21% | da inizio programma |
| 44 | 2026-07-20 | 2023-01-04 | 77,79 $ | 66,43 $ | +17,11% | da inizio programma |
| 45 | 2026-07-21 | 2023-01-05 | 78,11 $ | 66,32 $ | +17,77% | da inizio programma |
| 46 | 2026-07-22 | 2023-01-06 | 77,91 $ | 66,78 $ | +16,66% | da inizio programma |
| 47 | 2026-07-23 | 2023-01-07 | 75,86 $ | 66,79 $ | +13,58% | da inizio programma |
| 48 | 2026-07-24 | 2023-01-08 | 75,86 $ | 67,33 $ | +12,68% | da inizio programma |
| 49 | 2026-07-25 | 2023-01-09 | 74,20 $ | 67,74 $ | +9,53% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-08-01 | 83,39 $ | 91,34 $ | 74,20 $ / 91,34 $ | no | n/a | n/a | n/a |
| 14g | 2026-08-08 | 90,34 $ | 98,96 $ | 74,20 $ / 98,96 $ | no | n/a | n/a | n/a |
| 21g | 2026-08-15 | 89,97 $ | 98,55 $ | 74,20 $ / 102,58 $ | no | n/a | n/a | n/a |
| 28g | 2026-08-22 | 89,66 $ | 98,21 $ | 74,20 $ / 102,58 $ | no | n/a | n/a | n/a |
| 35g | 2026-08-29 | 85,91 $ | 94,10 $ | 74,20 $ / 102,58 $ | no | n/a | n/a | n/a |
| 42g | 2026-09-05 | 97,81 $ | 107,13 $ | 74,20 $ / 107,13 $ | no | n/a | n/a | n/a |
| 49g | 2026-09-12 | 92,66 $ | 101,50 $ | 74,20 $ / 107,13 $ | no | n/a | n/a | n/a |
| 56g | 2026-09-19 | 88,36 $ | 96,78 $ | 74,20 $ / 107,13 $ | no | n/a | n/a | n/a |
| 63g | 2026-09-26 | 95,32 $ | 104,41 $ | 74,20 $ / 107,13 $ | no | n/a | n/a | n/a |
| 70g | 2026-10-03 | 109,38 $ | 119,81 $ | 74,20 $ / 120,98 $ | no | n/a | n/a | n/a |
| 77g | 2026-10-10 | 106,91 $ | 117,10 $ | 74,20 $ / 122,26 $ | no | n/a | n/a | n/a |
| 84g | 2026-10-17 | 109,47 $ | 119,91 $ | 74,20 $ / 122,88 $ | no | n/a | n/a | n/a |
| 91g | 2026-10-24 | 116,81 $ | 127,95 $ | 74,20 $ / 127,95 $ | no | n/a | n/a | n/a |
| 98g | 2026-10-31 | 115,99 $ | 127,05 $ | 74,20 $ / 131,54 $ | no | n/a | n/a | n/a |
| 105g | 2026-11-07 | 108,43 $ | 118,77 $ | 74,20 $ / 131,54 $ | no | n/a | n/a | n/a |
| 112g | 2026-11-14 | 110,66 $ | 121,21 $ | 74,20 $ / 131,54 $ | no | n/a | n/a | n/a |
| 119g | 2026-11-21 | 109,09 $ | 119,50 $ | 74,20 $ / 131,54 $ | no | n/a | n/a | n/a |
| 126g | 2026-11-28 | 107,12 $ | 117,33 $ | 74,20 $ / 131,54 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 11 | 36,36% | 1,78% | 14,76% |
| 14g | 4 | 0,00% | 4,30% | 11,10% |
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
