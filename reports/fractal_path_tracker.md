<!-- FRACTAL_PATH_TRACKER_START -->
# Tracking percorso frattale SOL/BTC

Generato: 2026-10-11 05:32 UTC

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-10-11**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-03-28**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **109,54 $**
- Verdetto principale: **STRUTTURA ANALOGA, PREZZO NON ADERENTE**
- Somiglianza strutturale: **+73,21%**
- Aderenza live principale: **+70,00%**
- Errore medio live principale: **15,00%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE NON CONFERMATO DAL PREZZO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **127**
- Osservazioni inclusive dal bottom: **128**
- Osservazioni da inizio programma/scanner: **101**
- Errore assoluto medio dal bottom: **13,11%**
- Errore assoluto medio da inizio programma: **15,00%**
- Gap firmato medio ultimi 7 giorni: **+4,55%**
- Errore assoluto medio ultimi 7 giorni: **4,85%**
- Gap ultimo giorno: **+1,98%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **+1,98%**
- Gap firmato medio 7g: **+4,55%**
- Errore assoluto medio 7g: **4,85%**
- Variazione recente gap: **+0,93%**
- Stato gap: **VICINO AL FRATTALE**
- Trend gap: **SOL resta sopra il percorso ancorato con distacco quasi stabile**

Soglie operative del grafico:

- entro **±5%**: percorso vicino;
- tra **±5% e ±12%**: deviazione gestibile;
- oltre **±12%**: frattale non abbastanza aderente per conferma operativa;
- oltre **±18%**: disallineamento marcato.

## Ultimi giorni del confronto ancorato

|   Giorno | Data SOL   | Data BTC eq.   | SOL reale   | Percorso ancorato   | Gap firmato   | Fase                |
|---------:|:-----------|:---------------|:------------|:--------------------|:--------------|:--------------------|
| 118 | 2026-10-02 | 2023-03-19 | 118,62 $ | 110,45 $ | +7,39% | da inizio programma |
| 119 | 2026-10-03 | 2023-03-20 | 119,65 $ | 109,38 $ | +9,38% | da inizio programma |
| 120 | 2026-10-04 | 2023-03-21 | 121,53 $ | 110,99 $ | +9,49% | da inizio programma |
| 121 | 2026-10-05 | 2023-03-22 | 120,75 $ | 107,57 $ | +12,25% | da inizio programma |
| 122 | 2026-10-06 | 2023-03-23 | 120,79 $ | 111,61 $ | +8,22% | da inizio programma |
| 123 | 2026-10-07 | 2023-03-24 | 116,22 $ | 108,30 $ | +7,31% | da inizio programma |
| 124 | 2026-10-08 | 2023-03-25 | 109,44 $ | 108,31 $ | +1,05% | da inizio programma |
| 125 | 2026-10-09 | 2023-03-26 | 109,14 $ | 110,28 $ | -1,03% | da inizio programma |
| 126 | 2026-10-10 | 2023-03-27 | 109,14 $ | 106,91 $ | +2,09% | da inizio programma |
| 127 | 2026-10-11 | 2023-03-28 | 109,54 $ | 107,42 $ | +1,98% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-10-18 | 110,96 $ | 113,16 $ | 109,54 $ / 114,40 $ | no | n/a | n/a | n/a |
| 14g | 2026-10-25 | 119,10 $ | 121,46 $ | 109,54 $ / 121,46 $ | no | n/a | n/a | n/a |
| 21g | 2026-11-01 | 119,74 $ | 122,11 $ | 109,54 $ / 122,47 $ | no | n/a | n/a | n/a |
| 28g | 2026-11-08 | 111,51 $ | 113,72 $ | 109,54 $ / 122,47 $ | no | n/a | n/a | n/a |
| 35g | 2026-11-15 | 112,98 $ | 115,21 $ | 109,54 $ / 122,47 $ | no | n/a | n/a | n/a |
| 42g | 2026-11-22 | 108,95 $ | 111,11 $ | 109,54 $ / 122,47 $ | no | n/a | n/a | n/a |
| 49g | 2026-11-29 | 106,50 $ | 108,61 $ | 107,60 $ / 122,47 $ | no | n/a | n/a | n/a |
| 56g | 2026-12-06 | 107,25 $ | 109,37 $ | 107,47 $ / 122,47 $ | no | n/a | n/a | n/a |
| 63g | 2026-12-13 | 109,13 $ | 111,28 $ | 105,79 $ / 122,47 $ | no | n/a | n/a | n/a |
| 70g | 2026-12-20 | 107,30 $ | 109,42 $ | 103,48 $ / 122,47 $ | no | n/a | n/a | n/a |
| 77g | 2026-12-27 | 102,10 $ | 104,12 $ | 103,48 $ / 122,47 $ | no | n/a | n/a | n/a |
| 84g | 2027-01-03 | 111,59 $ | 113,80 $ | 100,93 $ / 122,47 $ | no | n/a | n/a | n/a |
| 91g | 2027-01-10 | 120,89 $ | 123,28 $ | 100,93 $ / 123,31 $ | no | n/a | n/a | n/a |
| 98g | 2027-01-17 | 121,24 $ | 123,64 $ | 100,93 $ / 125,16 $ | no | n/a | n/a | n/a |
| 105g | 2027-01-24 | 120,62 $ | 123,01 $ | 100,93 $ / 125,16 $ | no | n/a | n/a | n/a |
| 112g | 2027-01-31 | 117,61 $ | 119,94 $ | 100,93 $ / 126,44 $ | no | n/a | n/a | n/a |
| 119g | 2027-02-07 | 115,13 $ | 117,41 $ | 100,93 $ / 126,44 $ | no | n/a | n/a | n/a |
| 126g | 2027-02-14 | 116,90 $ | 119,21 $ | 100,93 $ / 126,44 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 82 | 37,80% | 11,64% | 13,94% |
| 14g | 76 | 23,68% | 17,66% | 14,18% |
| 21g | 70 | 28,57% | 20,83% | 15,67% |
| 28g | 66 | 30,30% | 21,36% | 15,12% |
| 35g | 59 | 38,98% | 22,23% | 14,84% |
| 42g | 52 | 50,00% | 21,63% | 13,65% |
| 49g | 45 | 51,11% | 22,99% | 15,58% |
| 56g | 38 | 42,11% | 22,27% | 16,55% |
| 63g | 33 | 33,33% | 16,72% | 17,55% |
| 70g | 26 | 38,46% | 10,46% | 19,70% |
| 77g | 19 | 63,16% | 9,19% | 12,80% |
| 84g | 12 | 100,00% | 8,33% | 6,02% |
| 91g | 5 | 100,00% | 13,74% | 1,70% |
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
