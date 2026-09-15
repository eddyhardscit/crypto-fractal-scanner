<!-- FRACTAL_PATH_TRACKER_START -->
# Tracking percorso frattale SOL/BTC

Generato: 2026-09-15 05:32 UTC

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-09-15**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-03-02**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **100,90 $**
- Verdetto principale: **ANALOGIA DEBOLE / SCENARIO SECONDARIO**
- Somiglianza strutturale: **+70,72%**
- Aderenza live principale: **+72,91%**
- Errore medio live principale: **13,54%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE SOLO DI CONTESTO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **101**
- Osservazioni inclusive dal bottom: **102**
- Osservazioni da inizio programma/scanner: **75**
- Errore assoluto medio dal bottom: **11,55%**
- Errore assoluto medio da inizio programma: **13,54%**
- Gap firmato medio ultimi 7 giorni: **+9,14%**
- Errore assoluto medio ultimi 7 giorni: **9,14%**
- Gap ultimo giorno: **+9,11%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **+9,11%**
- Gap firmato medio 7g: **+9,14%**
- Errore assoluto medio 7g: **9,14%**
- Variazione recente gap: **-0,74%**
- Stato gap: **SOPRA IL FRATTALE**
- Trend gap: **SOL resta sopra il percorso ancorato con distacco quasi stabile**

Soglie operative del grafico:

- entro **±5%**: percorso vicino;
- tra **±5% e ±12%**: deviazione gestibile;
- oltre **±12%**: frattale non abbastanza aderente per conferma operativa;
- oltre **±18%**: disallineamento marcato.

## Ultimi giorni del confronto ancorato

|   Giorno | Data SOL   | Data BTC eq.   | SOL reale   | Percorso ancorato   | Gap firmato   | Fase                |
|---------:|:-----------|:---------------|:------------|:--------------------|:--------------|:--------------------|
| 92 | 2026-09-06 | 2023-02-21 | 106,45 $ | 96,26 $ | +10,58% | da inizio programma |
| 93 | 2026-09-07 | 2023-02-22 | 103,87 $ | 95,29 $ | +9,01% | da inizio programma |
| 94 | 2026-09-08 | 2023-02-23 | 103,33 $ | 94,33 $ | +9,53% | da inizio programma |
| 95 | 2026-09-09 | 2023-02-24 | 101,61 $ | 91,38 $ | +11,19% | da inizio programma |
| 96 | 2026-09-10 | 2023-02-25 | 98,69 $ | 91,29 $ | +8,10% | da inizio programma |
| 97 | 2026-09-11 | 2023-02-26 | 102,40 $ | 92,81 $ | +10,33% | da inizio programma |
| 98 | 2026-09-12 | 2023-02-27 | 101,79 $ | 92,66 $ | +9,85% | da inizio programma |
| 99 | 2026-09-13 | 2023-02-28 | 99,25 $ | 91,18 $ | +8,84% | da inizio programma |
| 100 | 2026-09-14 | 2023-03-01 | 99,25 $ | 93,15 $ | +6,54% | da inizio programma |
| 101 | 2026-09-15 | 2023-03-02 | 100,90 $ | 92,48 $ | +9,11% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-09-22 | 80,21 $ | 87,52 $ | 87,52 $ / 100,90 $ | no | n/a | n/a | n/a |
| 14g | 2026-09-29 | 98,69 $ | 107,68 $ | 86,77 $ / 107,68 $ | no | n/a | n/a | n/a |
| 21g | 2026-10-06 | 111,61 $ | 121,78 $ | 86,77 $ / 121,78 $ | no | n/a | n/a | n/a |
| 28g | 2026-10-13 | 110,43 $ | 120,49 $ | 86,77 $ / 121,84 $ | no | n/a | n/a | n/a |
| 35g | 2026-10-20 | 110,47 $ | 120,54 $ | 86,77 $ / 122,40 $ | no | n/a | n/a | n/a |
| 42g | 2026-10-27 | 119,75 $ | 130,66 $ | 86,77 $ / 130,66 $ | no | n/a | n/a | n/a |
| 49g | 2026-11-03 | 111,27 $ | 121,40 $ | 86,77 $ / 131,03 $ | no | n/a | n/a | n/a |
| 56g | 2026-11-10 | 116,10 $ | 126,68 $ | 86,77 $ / 131,03 $ | no | n/a | n/a | n/a |
| 63g | 2026-11-17 | 113,64 $ | 123,99 $ | 86,77 $ / 131,03 $ | no | n/a | n/a | n/a |
| 70g | 2026-11-24 | 106,36 $ | 116,05 $ | 86,77 $ / 131,03 $ | no | n/a | n/a | n/a |
| 77g | 2026-12-01 | 105,70 $ | 115,33 $ | 86,77 $ / 131,03 $ | no | n/a | n/a | n/a |
| 84g | 2026-12-08 | 104,30 $ | 113,80 $ | 86,77 $ / 131,03 $ | no | n/a | n/a | n/a |
| 91g | 2026-12-15 | 105,65 $ | 115,28 $ | 86,77 $ / 131,03 $ | no | n/a | n/a | n/a |
| 98g | 2026-12-22 | 104,42 $ | 113,94 $ | 86,77 $ / 131,03 $ | no | n/a | n/a | n/a |
| 105g | 2026-12-29 | 100,75 $ | 109,93 $ | 86,77 $ / 131,03 $ | no | n/a | n/a | n/a |
| 112g | 2027-01-05 | 117,83 $ | 128,57 $ | 86,77 $ / 131,03 $ | no | n/a | n/a | n/a |
| 119g | 2027-01-12 | 119,93 $ | 130,86 $ | 86,77 $ / 131,93 $ | no | n/a | n/a | n/a |
| 126g | 2027-01-19 | 117,82 $ | 128,55 $ | 86,77 $ / 133,91 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 61 | 39,34% | 10,19% | 12,43% |
| 14g | 54 | 25,93% | 16,93% | 11,32% |
| 21g | 47 | 19,15% | 25,18% | 12,70% |
| 28g | 40 | 27,50% | 26,58% | 12,32% |
| 35g | 35 | 37,14% | 19,73% | 11,33% |
| 42g | 28 | 71,43% | 11,19% | 10,46% |
| 49g | 21 | 95,24% | 5,53% | 10,08% |
| 56g | 14 | 100,00% | 6,75% | 8,75% |
| 63g | 7 | 100,00% | 7,00% | 8,93% |
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
