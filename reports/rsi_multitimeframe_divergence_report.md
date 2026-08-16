# Divergenze RSI multi-timeframe — diagnostica

Generato: 2026-08-16 05:34 UTC

Il modulo confronta prezzo e RSI 14 sui pivot confermati **daily e weekly**. Riconosce divergenze regolari e nascoste, segnali in formazione, invalidazioni e semplice conferma del momentum.

**Peso operativo: 0.** Non modifica il Global Confluence, non cambia le soglie del Paper Trading e non apre né blocca operazioni. I risultati vengono misurati prima di qualsiasi futura decisione sul peso.

## Sintesi corrente

| Asset   | Daily                      | Stato D       | Weekly              | Stato W    | Lettura weekly                                                                                                                |   Peso |
|:--------|:---------------------------|:--------------|:--------------------|:-----------|:------------------------------------------------------------------------------------------------------------------------------|-------:|
| BTC     | Hidden bullish             | IN_FORMAZIONE | Bullish regolare    | CONFERMATA | Bullish regolare confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto. |      0 |
| SOL     | Conferma rialzista         | CONTESTO      | Hidden bearish      | CONFERMATA | Hidden bearish confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto.   |      0 |
| DOGE    | Misto / nessuna divergenza | CONTESTO      | Conferma ribassista | CONTESTO   | Prezzo e RSI stanno scendendo insieme: momentum ribassista confermato, nessuna bullish divergence attiva.                     |      0 |

## Dettaglio dei pivot

| Asset   | TF   | Tipo                       | Stato         | Prezzo / RSI      | Pivot confrontati                                                 | Δ prezzo contesto   | Δ RSI contesto   |   Peso |
|:--------|:-----|:---------------------------|:--------------|:------------------|:------------------------------------------------------------------|:--------------------|:-----------------|-------:|
| BTC     | 1D   | Hidden bullish             | IN_FORMAZIONE | 63.006 $ / 42,97  | 2026-08-03 62.227 $ / RSI 47,40 → 2026-08-14 62.488 $ / RSI 42,71 | n/a                 | n/a              |      0 |
| BTC     | 1W   | Bullish regolare           | CONFERMATA    | 63.006 $ / 38,99  | 2026-06-07 59.109 $ / RSI 34,23 → 2026-07-05 57.748 $ / RSI 38,20 | n/a                 | n/a              |      0 |
| SOL     | 1D   | Conferma rialzista         | CONTESTO      | 75,31 $ / 50,90   | n/a                                                               | +4,79%              | 11,26            |      0 |
| SOL     | 1W   | Hidden bearish             | CONFERMATA    | 75,31 $ / 40,17   | 2026-05-17 98,27 $ / RSI 38,29 → 2026-07-05 83,81 $ / RSI 42,25   | n/a                 | n/a              |      0 |
| DOGE    | 1D   | Misto / nessuna divergenza | CONTESTO      | 0.06965 $ / 44,75 | n/a                                                               | +0,84%              | 6,97             |      0 |
| DOGE    | 1W   | Conferma ribassista        | CONTESTO      | 0.06965 $ / 32,74 | n/a                                                               | -10,40%             | -2,39            |      0 |

### BTC

- **1D — Hidden bullish / IN_FORMAZIONE**: Hidden bullish in formazione: il secondo estremo non è ancora un pivot confermato. Peso operativo sempre 0.
- **1W — Bullish regolare / CONFERMATA**: Bullish regolare confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto.

### SOL

- **1D — Conferma rialzista / CONTESTO**: Prezzo e RSI stanno salendo insieme: momentum rialzista confermato.
- **1W — Hidden bearish / CONFERMATA**: Hidden bearish confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto.

### DOGE

- **1D — Misto / nessuna divergenza / CONTESTO**: Misto / nessuna divergenza. Non esiste una divergenza confermata sugli ultimi pivot.
- **1W — Conferma ribassista / CONTESTO**: Prezzo e RSI stanno scendendo insieme: momentum ribassista confermato, nessuna bullish divergence attiva.

## Tracker live delle divergenze confermate

Viene salvato un solo evento per combinazione di asset, timeframe, tipo e coppia di pivot. Gli esiti vengono controllati dopo 30, 60, 90 e 180 giorni.

- Eventi indipendenti salvati: **7**.
- Soglie di lettura: **30 / 60 / 100 controlli**.
- Anche oltre le soglie il peso resta **0** finché non viene presa una decisione esplicita.

| Asset   | TF   | Tipo             |   Orizzonte |   Controlli | Accuratezza   | Return corretto   | Stato         |   Peso |
|:--------|:-----|:-----------------|------------:|------------:|:--------------|:------------------|:--------------|-------:|
| BTC     | 1D   | Bullish regolare |          30 |           1 | 0,00%         | -1,52%            | RACCOLTA DATI |      0 |
| BTC     | 1D   | Hidden bearish   |          30 |           1 | 0,00%         | -1,37%            | RACCOLTA DATI |      0 |
| BTC     | 1W   | Bullish regolare |          30 |           1 | +100,00%      | +1,03%            | RACCOLTA DATI |      0 |
| DOGE    | 1D   | Hidden bearish   |          30 |           1 | +100,00%      | +4,98%            | RACCOLTA DATI |      0 |
| SOL     | 1W   | Hidden bearish   |          30 |           1 | +100,00%      | +1,11%            | RACCOLTA DATI |      0 |

## Regole di prudenza

- Una divergenza **in formazione** può scomparire prima che il pivot sia confermato.
- Una divergenza weekly può anticipare il prezzo di diverse settimane.
- Prezzo in calo e RSI in calo non è bullish divergence: è conferma ribassista.
- Le divergenze restano dentro la famiglia tecnica e non vengono sommate come prova indipendente.
- Nessuna statistica di questo modulo autorizza automaticamente il trading reale.
