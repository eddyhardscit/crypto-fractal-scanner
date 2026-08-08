# Divergenze RSI multi-timeframe — diagnostica

Generato: 2026-08-08 05:18 UTC

Il modulo confronta prezzo e RSI 14 sui pivot confermati **daily e weekly**. Riconosce divergenze regolari e nascoste, segnali in formazione, invalidazioni e semplice conferma del momentum.

**Peso operativo: 0.** Non modifica il Global Confluence, non cambia le soglie del Paper Trading e non apre né blocca operazioni. I risultati vengono misurati prima di qualsiasi futura decisione sul peso.

## Sintesi corrente

| Asset   | Daily                       | Stato D    | Weekly                     | Stato W    | Lettura weekly                                                                                                                |   Peso |
|:--------|:----------------------------|:-----------|:---------------------------|:-----------|:------------------------------------------------------------------------------------------------------------------------------|-------:|
| BTC     | Bullish regolare invalidata | INVALIDATA | Bullish regolare           | CONFERMATA | Bullish regolare confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto. |      0 |
| SOL     | Misto / nessuna divergenza  | CONTESTO   | Hidden bearish             | CONFERMATA | Hidden bearish confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto.   |      0 |
| DOGE    | Bullish regolare            | CONFERMATA | Misto / nessuna divergenza | CONTESTO   | Misto / nessuna divergenza. Non esiste una divergenza confermata sugli ultimi pivot.                                          |      0 |

## Dettaglio dei pivot

| Asset   | TF   | Tipo                        | Stato      | Prezzo / RSI      | Pivot confrontati                                                   | Δ prezzo contesto   | Δ RSI contesto   |   Peso |
|:--------|:-----|:----------------------------|:-----------|:------------------|:--------------------------------------------------------------------|:--------------------|:-----------------|-------:|
| BTC     | 1D   | Bullish regolare invalidata | INVALIDATA | 64.966 $ / 54,93  | n/a                                                                 | +1,35%              | 5,34             |      0 |
| BTC     | 1W   | Bullish regolare            | CONFERMATA | 64.966 $ / 41,10  | 2026-06-07 59.109 $ / RSI 34,23 → 2026-07-05 57.748 $ / RSI 38,20   | n/a                 | n/a              |      0 |
| SOL     | 1D   | Misto / nessuna divergenza  | CONTESTO   | 74,52 $ / 49,66   | n/a                                                                 | +0,87%              | 6,76             |      0 |
| SOL     | 1W   | Hidden bearish              | CONFERMATA | 74,52 $ / 39,29   | 2026-05-17 98,27 $ / RSI 38,29 → 2026-07-05 83,81 $ / RSI 42,25     | n/a                 | n/a              |      0 |
| DOGE    | 1D   | Bullish regolare            | CONFERMATA | 0.07013 $ / 43,99 | 2026-07-24 0.06829 $ / RSI 33,29 → 2026-08-01 0.06797 $ / RSI 37,78 | n/a                 | n/a              |      0 |
| DOGE    | 1W   | Misto / nessuna divergenza  | CONTESTO   | 0.07013 $ / 32,74 | n/a                                                                 | -4,05%              | 0,61             |      0 |

### BTC

- **1D — Bullish regolare invalidata / INVALIDATA**: La precedente bullish regolare non è più sostenuta dalla relazione corrente tra pivot di prezzo e RSI.
- **1W — Bullish regolare / CONFERMATA**: Bullish regolare confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto.

### SOL

- **1D — Misto / nessuna divergenza / CONTESTO**: Misto / nessuna divergenza. Non esiste una divergenza confermata sugli ultimi pivot.
- **1W — Hidden bearish / CONFERMATA**: Hidden bearish confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto.

### DOGE

- **1D — Bullish regolare / CONFERMATA**: Bullish regolare confermata sui due pivot del prezzo e dell'RSI. Contesto diagnostico: nessun punto operativo viene aggiunto.
- **1W — Misto / nessuna divergenza / CONTESTO**: Misto / nessuna divergenza. Non esiste una divergenza confermata sugli ultimi pivot.

## Tracker live delle divergenze confermate

Viene salvato un solo evento per combinazione di asset, timeframe, tipo e coppia di pivot. Gli esiti vengono controllati dopo 30, 60, 90 e 180 giorni.

- Eventi indipendenti salvati: **7**.
- Soglie di lettura: **30 / 60 / 100 controlli**.
- Anche oltre le soglie il peso resta **0** finché non viene presa una decisione esplicita.

_Nessun controllo maturato: il tracker ha appena iniziato a raccogliere dati._

## Regole di prudenza

- Una divergenza **in formazione** può scomparire prima che il pivot sia confermato.
- Una divergenza weekly può anticipare il prezzo di diverse settimane.
- Prezzo in calo e RSI in calo non è bullish divergence: è conferma ribassista.
- Le divergenze restano dentro la famiglia tecnica e non vengono sommate come prova indipendente.
- Nessuna statistica di questo modulo autorizza automaticamente il trading reale.
