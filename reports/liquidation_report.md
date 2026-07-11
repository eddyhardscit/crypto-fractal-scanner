# Report semplice futures / liquidazioni BTC / SOL / DOGE

Generato: **2026-07-11 15:43:36 CEST**  
UTC: **2026-07-11 13:43:36 UTC**

Fonte dati: **OKX Futures pubblici**.  
Questo report non è la vera heatmap CoinGlass. Serve a capire se il mercato futures è carico di long, short o leva.

## Traduzione in parole semplici

| Asset | Lettura | Forza | Cosa significa in pratica |
| --- | --- | --- | --- |
| BTC | Leva alta, direzione mista | 3/5 | Meglio non forzare. Aspetta conferma dal frattale o dal prezzo. |
| SOL | Misto | 1/5 | Qui pesa di più il report frattale. |
| DOGE | Misto | 1/5 | Qui pesa di più il report frattale. |

## Numeri principali

| Asset | Prezzo | Prezzo 24h | Funding | Open Interest | OI 24h | Long/Short |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 64.162 $ | -0.28% | +0.0024% | $1.98B | +5.77% | 1.45 |
| SOL | 78,11 $ | -1.06% | -0.0032% | $241.59M | -23.39% | 2.21 |
| DOGE | 0.07473 $ | +0.71% | +0.0039% | $69.70M | +1.47% | 2.36 |

## Spiegazione rapida dei termini

- **Funding positivo**: i long pagano gli short. Se è troppo positivo, tanti stanno scommettendo al rialzo.
- **Funding negativo**: gli short pagano i long. Se è troppo negativo, tanti stanno scommettendo al ribasso.
- **Open Interest / OI**: quanta leva è aperta sul mercato. Se sale, entra più leva. Se scende, la leva sta uscendo.
- **Long/Short sopra 1**: più mercato orientato long.
- **Long/Short sotto 1**: più mercato orientato short.
- **Flush sotto**: discesa rapida per pulire i long.
- **Short squeeze sopra**: salita rapida per liquidare gli short.

---

## Bitcoin — BTC

### Lettura semplice

**MOLTA LEVA MA DIREZIONE MISTA**  
**Forza segnale: 3/5**

BTC: c'è molta leva nel mercato, ma la direzione non è pulita. Può arrivare un movimento violento, ma non è chiaro se sopra o sotto.

**Tradotto operativamente:** Meglio non forzare. Aspetta conferma dal frattale o dal prezzo.

### Perché

- funding positivo: i long pagano gli short
- open interest in aumento: più leva nel sistema
- long/short ratio alto: mercato più long

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $64,207 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -0.28% | movimento dell'ultimo giorno |
| Funding | +0.0024% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-11 18:00 | prossimo aggiornamento funding |
| Open Interest stimato | $1.98B | leva aperta stimata in dollari |
| Open Interest 24h | +5.77% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.45 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $51,366 | $77,049 |
| 10x | $57,786 | $70,628 |
| 20x | $60,997 | $67,418 |
| 50x | $62,923 | $65,491 |

### Note tecniche usate dallo score

- open interest in forte aumento: entra molta leva
- long/short ratio alto: più mercato sbilanciato long

---

## Solana — SOL

### Lettura semplice

**NEUTRALE / POCO CHIARO**  
**Forza segnale: 1/5**

SOL: i futures non danno una lettura chiara. Non si vede uno sbilanciamento forte né long né short.

**Tradotto operativamente:** Qui pesa di più il report frattale.

### Perché

- funding negativo: gli short pagano i long
- open interest in calo: leva in uscita
- long/short ratio alto: mercato più long

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $78.12 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -1.06% | movimento dell'ultimo giorno |
| Funding | -0.0032% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-11 18:00 | prossimo aggiornamento funding |
| Open Interest stimato | $241.59M | leva aperta stimata in dollari |
| Open Interest 24h | -23.39% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 2.21 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $62.50 | $93.74 |
| 10x | $70.31 | $85.93 |
| 20x | $74.21 | $82.03 |
| 50x | $76.56 | $79.68 |

### Note tecniche usate dallo score

- open interest in forte calo: parte della leva è già uscita
- long/short ratio alto: più mercato sbilanciato long

---

## Dogecoin — DOGE

### Lettura semplice

**NEUTRALE / POCO CHIARO**  
**Forza segnale: 1/5**

DOGE: i futures non danno una lettura chiara. Non si vede uno sbilanciamento forte né long né short.

**Tradotto operativamente:** Qui pesa di più il report frattale.

### Perché

- funding positivo: i long pagano gli short
- open interest abbastanza stabile
- long/short ratio alto: mercato più long

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $0.07471 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +0.71% | movimento dell'ultimo giorno |
| Funding | +0.0039% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-11 18:00 | prossimo aggiornamento funding |
| Open Interest stimato | $69.70M | leva aperta stimata in dollari |
| Open Interest 24h | +1.47% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 2.36 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $0.05977 | $0.08965 |
| 10x | $0.06724 | $0.08218 |
| 20x | $0.07097 | $0.07845 |
| 50x | $0.07322 | $0.07620 |

### Note tecniche usate dallo score

- long/short ratio alto: più mercato sbilanciato long

---
