# Report semplice futures / liquidazioni BTC / SOL / DOGE

Generato: **2026-07-16 13:22:42 CEST**  
UTC: **2026-07-16 11:22:42 UTC**

Fonte dati: **OKX Futures pubblici**.  
Questo report non è la vera heatmap CoinGlass. Serve a capire se il mercato futures è carico di long, short o leva.

## Traduzione in parole semplici

| Asset | Lettura | Forza | Cosa significa in pratica |
| --- | --- | --- | --- |
| BTC | Leva alta, direzione mista | 3/5 | Meglio non forzare. Aspetta conferma dal frattale o dal prezzo. |
| SOL | Misto | 1/5 | Qui pesa di più il report frattale. |
| DOGE | Rischio sotto | 4/5 | Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale. |

## Numeri principali

| Asset | Prezzo | Prezzo 24h | Funding | Open Interest | OI 24h | Long/Short |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 64.074 $ | -0.78% | +0.0041% | $1.97B | +7.45% | 1.31 |
| SOL | 76,03 $ | -1.67% | +0.0011% | $225.29M | -13.24% | 2.11 |
| DOGE | 0.07302 $ | -0.71% | +0.0100% | $71.62M | +9.45% | 4.25 |

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
| Prezzo | $64,147 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -0.78% | movimento dell'ultimo giorno |
| Funding | +0.0041% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-16 18:00 | prossimo aggiornamento funding |
| Open Interest stimato | $1.97B | leva aperta stimata in dollari |
| Open Interest 24h | +7.45% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.31 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $51,318 | $76,977 |
| 10x | $57,732 | $70,562 |
| 20x | $60,940 | $67,355 |
| 50x | $62,864 | $65,430 |

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

- funding positivo: i long pagano gli short
- open interest in calo: leva in uscita
- long/short ratio alto: mercato più long

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $76.11 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -1.67% | movimento dell'ultimo giorno |
| Funding | +0.0011% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-16 18:00 | prossimo aggiornamento funding |
| Open Interest stimato | $225.29M | leva aperta stimata in dollari |
| Open Interest 24h | -13.24% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 2.11 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $60.89 | $91.33 |
| 10x | $68.50 | $83.72 |
| 20x | $72.30 | $79.92 |
| 50x | $74.59 | $77.63 |

### Note tecniche usate dallo score

- open interest in forte calo: parte della leva è già uscita
- long/short ratio alto: più mercato sbilanciato long

---

## Dogecoin — DOGE

### Lettura semplice

**RISCHIO DISCESA / FLUSH SOTTO**  
**Forza segnale: 4/5**

DOGE: i futures sembrano più vulnerabili verso una discesa improvvisa. Non significa che deve scendere, ma se rompe sotto può accelerare.

**Tradotto operativamente:** Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale.

### Perché

- funding positivo: i long pagano gli short
- open interest in aumento: più leva nel sistema
- long/short ratio alto: mercato più long

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $0.07313 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -0.71% | movimento dell'ultimo giorno |
| Funding | +0.0100% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-16 18:00 | prossimo aggiornamento funding |
| Open Interest stimato | $71.62M | leva aperta stimata in dollari |
| Open Interest 24h | +9.45% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 4.25 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $0.05850 | $0.08776 |
| 10x | $0.06582 | $0.08044 |
| 20x | $0.06947 | $0.07679 |
| 50x | $0.07167 | $0.07459 |

### Note tecniche usate dallo score

- funding positivo: mercato leggermente carico di long
- open interest in forte aumento: entra molta leva
- long/short ratio alto: più mercato sbilanciato long

---
