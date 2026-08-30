<!-- FRACTAL_PATH_TRACKER_START -->
# Tracking percorso frattale SOL/BTC

Generato: 2026-08-30 05:32 UTC

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-08-30**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-02-14**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **105,06 $**
- Verdetto principale: **ANALOGIA DEBOLE / SCENARIO SECONDARIO**
- Somiglianza strutturale: **+64,27%**
- Aderenza live principale: **+69,54%**
- Errore medio live principale: **15,23%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE SOLO DI CONTESTO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **85**
- Osservazioni inclusive dal bottom: **86**
- Osservazioni da inizio programma/scanner: **59**
- Errore assoluto medio dal bottom: **12,34%**
- Errore assoluto medio da inizio programma: **15,23%**
- Gap firmato medio ultimi 7 giorni: **+20,34%**
- Errore assoluto medio ultimi 7 giorni: **20,34%**
- Gap ultimo giorno: **+20,02%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **+20,02%**
- Gap firmato medio 7g: **+20,34%**
- Errore assoluto medio 7g: **20,34%**
- Variazione recente gap: **-6,74%**
- Stato gap: **DISALLINEATO SOPRA IL FRATTALE**
- Trend gap: **SOL resta sopra il percorso ancorato, ma sta riducendo il distacco**

Soglie operative del grafico:

- entro **±5%**: percorso vicino;
- tra **±5% e ±12%**: deviazione gestibile;
- oltre **±12%**: frattale non abbastanza aderente per conferma operativa;
- oltre **±18%**: disallineamento marcato.

## Ultimi giorni del confronto ancorato

|   Giorno | Data SOL   | Data BTC eq.   | SOL reale   | Percorso ancorato   | Gap firmato   | Fase                |
|---------:|:-----------|:---------------|:------------|:--------------------|:--------------|:--------------------|
| 76 | 2026-08-21 | 2023-02-05 | 93,65 $ | 90,43 $ | +3,57% | da inizio programma |
| 77 | 2026-08-22 | 2023-02-06 | 93,91 $ | 89,66 $ | +4,75% | da inizio programma |
| 78 | 2026-08-23 | 2023-02-07 | 95,44 $ | 91,64 $ | +4,15% | da inizio programma |
| 79 | 2026-08-24 | 2023-02-08 | 98,56 $ | 90,36 $ | +9,07% | da inizio programma |
| 80 | 2026-08-25 | 2023-02-09 | 96,60 $ | 85,95 $ | +12,39% | da inizio programma |
| 81 | 2026-08-26 | 2023-02-10 | 102,17 $ | 85,29 $ | +19,79% | da inizio programma |
| 82 | 2026-08-27 | 2023-02-11 | 109,21 $ | 86,15 $ | +26,76% | da inizio programma |
| 83 | 2026-08-28 | 2023-02-12 | 109,21 $ | 85,83 $ | +27,24% | da inizio programma |
| 84 | 2026-08-29 | 2023-02-13 | 109,21 $ | 85,91 $ | +27,12% | da inizio programma |
| 85 | 2026-08-30 | 2023-02-14 | 105,06 $ | 87,53 $ | +20,02% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-09-06 | 96,26 $ | 115,54 $ | 105,06 $ / 117,39 $ | no | n/a | n/a | n/a |
| 14g | 2026-09-13 | 91,18 $ | 109,44 $ | 105,06 $ / 117,39 $ | no | n/a | n/a | n/a |
| 21g | 2026-09-20 | 87,53 $ | 105,06 $ | 105,06 $ / 117,39 $ | no | n/a | n/a | n/a |
| 28g | 2026-09-27 | 97,48 $ | 117,00 $ | 95,45 $ / 117,39 $ | no | n/a | n/a | n/a |
| 35g | 2026-10-04 | 110,99 $ | 133,22 $ | 95,45 $ / 133,22 $ | no | n/a | n/a | n/a |
| 42g | 2026-10-11 | 107,42 $ | 128,92 $ | 95,45 $ / 133,96 $ | no | n/a | n/a | n/a |
| 49g | 2026-10-18 | 110,96 $ | 133,18 $ | 95,45 $ / 134,65 $ | no | n/a | n/a | n/a |
| 56g | 2026-10-25 | 119,10 $ | 142,95 $ | 95,45 $ / 142,95 $ | no | n/a | n/a | n/a |
| 63g | 2026-11-01 | 119,74 $ | 143,72 $ | 95,45 $ / 144,14 $ | no | n/a | n/a | n/a |
| 70g | 2026-11-08 | 111,51 $ | 133,84 $ | 95,45 $ / 144,14 $ | no | n/a | n/a | n/a |
| 77g | 2026-11-15 | 112,98 $ | 135,60 $ | 95,45 $ / 144,14 $ | no | n/a | n/a | n/a |
| 84g | 2026-11-22 | 108,95 $ | 130,77 $ | 95,45 $ / 144,14 $ | no | n/a | n/a | n/a |
| 91g | 2026-11-29 | 106,50 $ | 127,83 $ | 95,45 $ / 144,14 $ | no | n/a | n/a | n/a |
| 98g | 2026-12-06 | 107,25 $ | 128,72 $ | 95,45 $ / 144,14 $ | no | n/a | n/a | n/a |
| 105g | 2026-12-13 | 109,13 $ | 130,98 $ | 95,45 $ / 144,14 $ | no | n/a | n/a | n/a |
| 112g | 2026-12-20 | 107,30 $ | 128,79 $ | 95,45 $ / 144,14 $ | no | n/a | n/a | n/a |
| 119g | 2026-12-27 | 102,10 $ | 122,54 $ | 95,45 $ / 144,14 $ | no | n/a | n/a | n/a |
| 126g | 2027-01-03 | 111,59 $ | 133,93 $ | 95,45 $ / 144,14 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 45 | 35,56% | 12,03% | 14,33% |
| 14g | 38 | 28,95% | 19,83% | 13,09% |
| 21g | 33 | 18,18% | 27,22% | 15,00% |
| 28g | 26 | 42,31% | 25,68% | 15,43% |
| 35g | 19 | 52,63% | 17,56% | 15,10% |
| 42g | 12 | 83,33% | 9,69% | 15,49% |
| 49g | 5 | 100,00% | 7,21% | 24,80% |
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
