# Divergenze RSI multi-timeframe — diagnostica

Generato: 2026-10-18 05:33 UTC

Il modulo confronta prezzo e RSI 14 sui pivot confermati **daily e weekly**. Riconosce divergenze regolari e nascoste, segnali in formazione, invalidazioni e semplice conferma del momentum.

**Peso operativo: 0.** Non modifica il Global Confluence, non cambia le soglie del Paper Trading e non apre né blocca operazioni. I risultati vengono misurati prima di qualsiasi futura decisione sul peso.

## Sintesi corrente

| Asset   | Daily                       | Stato D       | Weekly                    | Stato W       | Lettura weekly                                                                                              |   Peso |
|:--------|:----------------------------|:--------------|:--------------------------|:--------------|:------------------------------------------------------------------------------------------------------------|-------:|
| BTC     | Conferma ribassista         | CONTESTO      | Hidden bullish            | IN_FORMAZIONE | Hidden bullish in formazione: il secondo estremo non è ancora un pivot confermato. Peso operativo sempre 0. |      0 |
| SOL     | Hidden bullish              | IN_FORMAZIONE | Hidden bullish            | IN_FORMAZIONE | Hidden bullish in formazione: il secondo estremo non è ancora un pivot confermato. Peso operativo sempre 0. |      0 |
| DOGE    | Bullish regolare invalidata | INVALIDATA    | Hidden bullish invalidata | INVALIDATA    | La precedente hidden bullish non è più sostenuta dalla relazione corrente tra pivot di prezzo e RSI.        |      0 |

## Dettaglio dei pivot

| Asset   | TF   | Tipo                        | Stato         | Prezzo / RSI      | Pivot confrontati                                                 | Δ prezzo contesto   | Δ RSI contesto   |   Peso |
|:--------|:-----|:----------------------------|:--------------|:------------------|:------------------------------------------------------------------|:--------------------|:-----------------|-------:|
| BTC     | 1D   | Conferma ribassista         | CONTESTO      | 81.619 $ / 46,96  | n/a                                                               | -3,71%              | -16,77           |      0 |
| BTC     | 1W   | Hidden bullish              | IN_FORMAZIONE | 81.619 $ / 56,64  | 2026-09-20 74.945 $ / RSI 58,69 → 2026-10-18 79.736 $ / RSI 56,64 | n/a                 | n/a              |      0 |
| SOL     | 1D   | Hidden bullish              | IN_FORMAZIONE | 103,31 $ / 37,29  | 2026-09-16 96,23 $ / RSI 51,17 → 2026-10-15 101,03 $ / RSI 40,01  | n/a                 | n/a              |      0 |
| SOL     | 1W   | Hidden bullish              | IN_FORMAZIONE | 103,31 $ / 53,02  | 2026-09-20 96,23 $ / RSI 61,01 → 2026-10-18 101,03 $ / RSI 53,02  | n/a                 | n/a              |      0 |
| DOGE    | 1D   | Bullish regolare invalidata | INVALIDATA    | 0.07905 $ / 34,91 | n/a                                                               | -14,84%             | -18,70           |      0 |
| DOGE    | 1W   | Hidden bullish invalidata   | INVALIDATA    | 0.07905 $ / 43,43 | n/a                                                               | -12,96%             | -5,45            |      0 |

### BTC

- **1D — Conferma ribassista / CONTESTO**: Prezzo e RSI stanno scendendo insieme: momentum ribassista confermato, nessuna bullish divergence attiva.
- **1W — Hidden bullish / IN_FORMAZIONE**: Hidden bullish in formazione: il secondo estremo non è ancora un pivot confermato. Peso operativo sempre 0.

### SOL

- **1D — Hidden bullish / IN_FORMAZIONE**: Hidden bullish in formazione: il secondo estremo non è ancora un pivot confermato. Peso operativo sempre 0.
- **1W — Hidden bullish / IN_FORMAZIONE**: Hidden bullish in formazione: il secondo estremo non è ancora un pivot confermato. Peso operativo sempre 0.

### DOGE

- **1D — Bullish regolare invalidata / INVALIDATA**: La precedente bullish regolare non è più sostenuta dalla relazione corrente tra pivot di prezzo e RSI.
- **1W — Hidden bullish invalidata / INVALIDATA**: La precedente hidden bullish non è più sostenuta dalla relazione corrente tra pivot di prezzo e RSI.

## Tracker live delle divergenze confermate

Viene salvato un solo evento per combinazione di asset, timeframe, tipo e coppia di pivot. Gli esiti vengono controllati dopo 30, 60, 90 e 180 giorni.

- Eventi indipendenti salvati: **9**.
- Soglie di lettura: **30 / 60 / 100 controlli**.
- Anche oltre le soglie il peso resta **0** finché non viene presa una decisione esplicita.

| Asset   | TF   | Tipo             |   Orizzonte |   Controlli | Accuratezza   | Return corretto   | Stato         |   Peso |
|:--------|:-----|:-----------------|------------:|------------:|:--------------|:------------------|:--------------|-------:|
| BTC     | 1D   | Bullish regolare |          30 |           1 | 0,00%         | -1,52%            | RACCOLTA DATI |      0 |
| BTC     | 1D   | Bullish regolare |          60 |           1 | +100,00%      | +21,03%           | RACCOLTA DATI |      0 |
| BTC     | 1D   | Bullish regolare |          90 |           1 | +100,00%      | +30,34%           | RACCOLTA DATI |      0 |
| BTC     | 1D   | Hidden bearish   |          30 |           1 | 0,00%         | -1,37%            | RACCOLTA DATI |      0 |
| BTC     | 1D   | Hidden bearish   |          60 |           1 | 0,00%         | -23,44%           | RACCOLTA DATI |      0 |
| BTC     | 1D   | Hidden bearish   |          90 |           1 | 0,00%         | -33,97%           | RACCOLTA DATI |      0 |
| BTC     | 1D   | Hidden bullish   |          30 |           1 | +100,00%      | +25,83%           | RACCOLTA DATI |      0 |
| BTC     | 1D   | Hidden bullish   |          60 |           1 | +100,00%      | +26,95%           | RACCOLTA DATI |      0 |
| BTC     | 1W   | Bullish regolare |          30 |           1 | +100,00%      | +1,03%            | RACCOLTA DATI |      0 |
| BTC     | 1W   | Bullish regolare |          60 |           1 | +100,00%      | +22,85%           | RACCOLTA DATI |      0 |
| BTC     | 1W   | Bullish regolare |          90 |           1 | +100,00%      | +32,26%           | RACCOLTA DATI |      0 |
| DOGE    | 1D   | Bullish regolare |          30 |           1 | +100,00%      | +22,35%           | RACCOLTA DATI |      0 |
| DOGE    | 1D   | Bullish regolare |          60 |           1 | +100,00%      | +35,62%           | RACCOLTA DATI |      0 |
| DOGE    | 1D   | Hidden bearish   |          30 |           2 | +50,00%       | -8,18%            | RACCOLTA DATI |      0 |
| DOGE    | 1D   | Hidden bearish   |          60 |           2 | 0,00%         | -25,06%           | RACCOLTA DATI |      0 |
| DOGE    | 1D   | Hidden bearish   |          90 |           1 | 0,00%         | -17,61%           | RACCOLTA DATI |      0 |
| DOGE    | 1W   | Hidden bearish   |          30 |           1 | 0,00%         | -13,35%           | RACCOLTA DATI |      0 |
| SOL     | 1W   | Hidden bearish   |          30 |           1 | +100,00%      | +1,11%            | RACCOLTA DATI |      0 |
| SOL     | 1W   | Hidden bearish   |          60 |           1 | 0,00%         | -30,59%           | RACCOLTA DATI |      0 |
| SOL     | 1W   | Hidden bearish   |          90 |           1 | 0,00%         | -43,43%           | RACCOLTA DATI |      0 |

## Regole di prudenza

- Una divergenza **in formazione** può scomparire prima che il pivot sia confermato.
- Una divergenza weekly può anticipare il prezzo di diverse settimane.
- Prezzo in calo e RSI in calo non è bullish divergence: è conferma ribassista.
- Le divergenze restano dentro la famiglia tecnica e non vengono sommate come prova indipendente.
- Nessuna statistica di questo modulo autorizza automaticamente il trading reale.
