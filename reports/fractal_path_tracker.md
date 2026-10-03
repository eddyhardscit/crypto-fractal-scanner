<!-- FRACTAL_PATH_TRACKER_START -->
# Tracking percorso frattale SOL/BTC

Generato: 2026-10-03 05:32 UTC

Questo modulo separa due percorsi che prima potevano essere confusi:

- **percorso ancorato al bottom**: continua la scala originale BTC 2022 -> SOL 2026 e misura l'aderenza reale;
- **scenario riancorato oggi**: parte dal prezzo SOL corrente e replica solo i movimenti futuri di BTC; e uno scenario condizionale, non una conferma del frattale.

## Stato letto dal frattale principale

- Fonte metadati: **structured_csv**
- Data corrente: **2026-10-03**
- Bottom SOL usato: **2026-06-06**
- Bottom BTC equivalente: **2022-11-21**
- Giorno BTC equivalente: **2023-03-20**
- Inizio programma/scanner: **2026-07-03**
- Prezzo SOL corrente: **119,53 $**
- Verdetto principale: **STRUTTURA ANALOGA, PREZZO NON ADERENTE**
- Somiglianza strutturale: **+71,59%**
- Aderenza live principale: **+68,36%**
- Errore medio live principale: **15,82%**
- Peso operativo suggerito: **0**
- Fase: **FRATTALE NON CONFERMATO DAL PREZZO**
- Rischio fase: **ALTO**

## Aderenza del percorso ancorato

- Giorno corrente dal bottom: **119**
- Osservazioni inclusive dal bottom: **120**
- Osservazioni da inizio programma/scanner: **93**
- Errore assoluto medio dal bottom: **13,62%**
- Errore assoluto medio da inizio programma: **15,82%**
- Gap firmato medio ultimi 7 giorni: **+15,25%**
- Errore assoluto medio ultimi 7 giorni: **15,25%**
- Gap ultimo giorno: **+9,28%**
- Stato aderenza: **IN DEVIAZIONE**

## Grafico completo: due percorsi distinti

![Tracking percorso frattale](btc_2022_vs_sol_2026_path_tracking_chart.png)

La linea **ancorata al bottom** serve a verificare il frattale originale. La linea **riancorata oggi** serve soltanto come scenario futuro condizionale.

## Grafico backtest dal bottom

![Backtest dal bottom](btc_2022_vs_sol_2026_bottom_backtest_chart.png)

## Grafico gap SOL vs BTC scalato

![Gap SOL vs BTC scalato ultimi 60 giorni](btc_2022_vs_sol_2026_gap_60d_chart.png)

### Lettura rapida gap

- Ultimo gap firmato: **+9,28%**
- Gap firmato medio 7g: **+15,25%**
- Errore assoluto medio 7g: **15,25%**
- Variazione recente gap: **+0,05%**
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
| 110 | 2026-09-24 | 2023-03-11 | 117,01 $ | 81,28 $ | +43,97% | da inizio programma |
| 111 | 2026-09-25 | 2023-03-12 | 122,01 $ | 87,31 $ | +39,74% | da inizio programma |
| 112 | 2026-09-26 | 2023-03-13 | 121,43 $ | 95,32 $ | +27,39% | da inizio programma |
| 113 | 2026-09-27 | 2023-03-14 | 122,06 $ | 97,48 $ | +25,21% | da inizio programma |
| 114 | 2026-09-28 | 2023-03-15 | 118,84 $ | 96,02 $ | +23,76% | da inizio programma |
| 115 | 2026-09-29 | 2023-03-16 | 119,06 $ | 98,69 $ | +20,64% | da inizio programma |
| 116 | 2026-09-30 | 2023-03-17 | 117,99 $ | 108,03 $ | +9,22% | da inizio programma |
| 117 | 2026-10-01 | 2023-03-18 | 118,40 $ | 106,22 $ | +11,46% | da inizio programma |
| 118 | 2026-10-02 | 2023-03-19 | 118,40 $ | 110,45 $ | +7,19% | da inizio programma |
| 119 | 2026-10-03 | 2023-03-20 | 119,53 $ | 109,38 $ | +9,28% | da inizio programma |

## Proiezione futura salvata

| Orizzonte   | Data target   | Percorso ancorato   | Scenario riancorato oggi   | Min/max riancorato   | Controllato   | Prezzo reale   | Errore riancorato   | Errore ancorato   |
|:------------|:--------------|:--------------------|:---------------------------|:---------------------|:--------------|:---------------|:--------------------|:------------------|
| 7g | 2026-10-10 | 106,91 $ | 116,83 $ | 116,83 $ / 121,97 $ | no | n/a | n/a | n/a |
| 14g | 2026-10-17 | 109,47 $ | 119,63 $ | 116,83 $ / 122,59 $ | no | n/a | n/a | n/a |
| 21g | 2026-10-24 | 116,81 $ | 127,65 $ | 116,83 $ / 127,65 $ | no | n/a | n/a | n/a |
| 28g | 2026-10-31 | 115,99 $ | 126,75 $ | 116,83 $ / 131,23 $ | no | n/a | n/a | n/a |
| 35g | 2026-11-07 | 108,43 $ | 118,49 $ | 116,83 $ / 131,23 $ | no | n/a | n/a | n/a |
| 42g | 2026-11-14 | 110,66 $ | 120,93 $ | 116,83 $ / 131,23 $ | no | n/a | n/a | n/a |
| 49g | 2026-11-21 | 109,09 $ | 119,22 $ | 116,83 $ / 131,23 $ | no | n/a | n/a | n/a |
| 56g | 2026-11-28 | 107,12 $ | 117,06 $ | 115,30 $ / 131,23 $ | no | n/a | n/a | n/a |
| 63g | 2026-12-05 | 105,77 $ | 115,59 $ | 115,17 $ / 131,23 $ | no | n/a | n/a | n/a |
| 70g | 2026-12-12 | 109,30 $ | 119,44 $ | 113,36 $ / 131,23 $ | no | n/a | n/a | n/a |
| 77g | 2026-12-19 | 101,48 $ | 110,89 $ | 110,89 $ / 131,23 $ | no | n/a | n/a | n/a |
| 84g | 2026-12-26 | 102,04 $ | 111,50 $ | 110,89 $ / 131,23 $ | no | n/a | n/a | n/a |
| 91g | 2027-01-02 | 105,77 $ | 115,59 $ | 108,15 $ / 131,23 $ | no | n/a | n/a | n/a |
| 98g | 2027-01-09 | 119,25 $ | 130,31 $ | 108,15 $ / 132,14 $ | no | n/a | n/a | n/a |
| 105g | 2027-01-16 | 122,73 $ | 134,12 $ | 108,15 $ / 134,12 $ | no | n/a | n/a | n/a |
| 112g | 2027-01-23 | 119,81 $ | 130,93 $ | 108,15 $ / 134,12 $ | no | n/a | n/a | n/a |
| 119g | 2027-01-30 | 118,75 $ | 129,77 $ | 108,15 $ / 135,50 $ | no | n/a | n/a | n/a |
| 126g | 2027-02-06 | 114,93 $ | 125,60 $ | 108,15 $ / 135,50 $ | no | n/a | n/a | n/a |

La colonna **Percorso ancorato** continua la scala dal bottom. La colonna **Scenario riancorato oggi** riparte dal prezzo corrente e non cancella, nei controlli, il gap gia accumulato.

## Accuratezza storica della proiezione futura

| Orizzonte   |   Controlli | Dentro banda riancorata   | Errore ass. riancorato   | Errore ass. ancorato   |
|:------------|------------:|:--------------------------|:-------------------------|:-----------------------|
| 7g | 75 | 37,33% | 11,97% | 14,70% |
| 14g | 70 | 24,29% | 17,07% | 15,11% |
| 21g | 65 | 26,15% | 22,13% | 16,30% |
| 28g | 58 | 20,69% | 23,58% | 16,50% |
| 35g | 51 | 33,33% | 24,93% | 16,37% |
| 42g | 44 | 45,45% | 23,40% | 15,21% |
| 49g | 37 | 54,05% | 24,04% | 17,90% |
| 56g | 32 | 50,00% | 21,45% | 18,68% |
| 63g | 25 | 44,00% | 14,49% | 21,75% |
| 70g | 18 | 55,56% | 10,44% | 26,81% |
| 77g | 11 | 36,36% | 10,33% | 19,32% |
| 84g | 4 | 100,00% | 6,42% | 8,24% |
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
