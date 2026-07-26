<!-- FRACTAL_PATH_TRACKER_START -->
# Tracking percorso frattale SOL/BTC

Generato: 2026-07-26 05:14 UTC

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-07-26**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-01-10**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **75,08 $**
- Verdetto principale: **ANALOGIA DEBOLE / SCENARIO SECONDARIO**
- Somiglianza strutturale: **+64,17%**
- Aderenza live principale: **+65,93%**
- Errore medio live principale: **17,03%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE SOLO DI CONTESTO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **50**
- Osservazioni inclusive dal bottom: **51**
- Osservazioni da inizio programma/scanner: **24**
- Errore assoluto medio dal bottom: **11,21%**
- Errore assoluto medio da inizio programma: **17,03%**
- Gap firmato medio ultimi 7 giorni: **+13,31%**
- Errore assoluto medio ultimi 7 giorni: **13,31%**
- Gap ultimo giorno: **+9,25%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **+9,25%**
- Gap firmato medio 7g: **+13,31%**
- Errore assoluto medio 7g: **13,31%**
- Variazione recente gap: **-4,33%**
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
| 41 | 2026-07-17 | 2023-01-01 | 75,01 $ | 65,49 $ | +14,54% | da inizio programma |
| 42 | 2026-07-18 | 2023-01-02 | 75,46 $ | 65,74 $ | +14,79% | da inizio programma |
| 43 | 2026-07-19 | 2023-01-03 | 76,36 $ | 65,71 $ | +16,21% | da inizio programma |
| 44 | 2026-07-20 | 2023-01-04 | 77,79 $ | 66,43 $ | +17,11% | da inizio programma |
| 45 | 2026-07-21 | 2023-01-05 | 78,11 $ | 66,32 $ | +17,77% | da inizio programma |
| 46 | 2026-07-22 | 2023-01-06 | 77,91 $ | 66,78 $ | +16,66% | da inizio programma |
| 47 | 2026-07-23 | 2023-01-07 | 75,86 $ | 66,79 $ | +13,58% | da inizio programma |
| 48 | 2026-07-24 | 2023-01-08 | 73,88 $ | 67,33 $ | +9,73% | da inizio programma |
| 49 | 2026-07-25 | 2023-01-09 | 73,88 $ | 67,74 $ | +9,06% | da inizio programma |
| 50 | 2026-07-26 | 2023-01-10 | 75,08 $ | 68,73 $ | +9,25% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-08-02 | 83,36 $ | 91,07 $ | 75,08 $ / 91,10 $ | no | n/a | n/a | n/a |
| 14g | 2026-08-09 | 89,17 $ | 97,42 $ | 75,08 $ / 98,70 $ | no | n/a | n/a | n/a |
| 21g | 2026-08-16 | 91,15 $ | 99,58 $ | 75,08 $ / 102,31 $ | no | n/a | n/a | n/a |
| 28g | 2026-08-23 | 91,64 $ | 100,12 $ | 75,08 $ / 102,31 $ | no | n/a | n/a | n/a |
| 35g | 2026-08-30 | 87,53 $ | 95,63 $ | 75,08 $ / 102,31 $ | no | n/a | n/a | n/a |
| 42g | 2026-09-06 | 96,26 $ | 105,16 $ | 75,08 $ / 106,85 $ | no | n/a | n/a | n/a |
| 49g | 2026-09-13 | 91,18 $ | 99,61 $ | 75,08 $ / 106,85 $ | no | n/a | n/a | n/a |
| 56g | 2026-09-20 | 87,53 $ | 95,62 $ | 75,08 $ / 106,85 $ | no | n/a | n/a | n/a |
| 63g | 2026-09-27 | 97,48 $ | 106,49 $ | 75,08 $ / 106,85 $ | no | n/a | n/a | n/a |
| 70g | 2026-10-04 | 110,99 $ | 121,25 $ | 75,08 $ / 121,25 $ | no | n/a | n/a | n/a |
| 77g | 2026-10-11 | 107,42 $ | 117,35 $ | 75,08 $ / 121,94 $ | no | n/a | n/a | n/a |
| 84g | 2026-10-18 | 110,96 $ | 121,22 $ | 75,08 $ / 122,56 $ | no | n/a | n/a | n/a |
| 91g | 2026-10-25 | 119,10 $ | 130,12 $ | 75,08 $ / 130,12 $ | no | n/a | n/a | n/a |
| 98g | 2026-11-01 | 119,74 $ | 130,82 $ | 75,08 $ / 131,19 $ | no | n/a | n/a | n/a |
| 105g | 2026-11-08 | 111,51 $ | 121,82 $ | 75,08 $ / 131,19 $ | no | n/a | n/a | n/a |
| 112g | 2026-11-15 | 112,98 $ | 123,43 $ | 75,08 $ / 131,19 $ | no | n/a | n/a | n/a |
| 119g | 2026-11-22 | 108,95 $ | 119,03 $ | 75,08 $ / 131,19 $ | no | n/a | n/a | n/a |
| 126g | 2026-11-29 | 106,50 $ | 116,35 $ | 75,08 $ / 131,19 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 12 | 25,00% | 2,34% | 13,87% |
| 14g | 5 | 0,00% | 5,20% | 9,35% |
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
