# Report semplice futures / liquidazioni BTC / SOL / DOGE

Generato: **2026-07-09 18:12:28 CEST**  
UTC: **2026-07-09 16:12:28 UTC**

Fonte dati: **OKX Futures pubblici**.  
Questo report non è la vera heatmap CoinGlass. Serve a capire se il mercato futures è carico di long, short o leva.

## Traduzione in parole semplici

| Asset | Lettura | Forza | Cosa significa in pratica |
| --- | --- | --- | --- |
| BTC | Rischio sotto | 5/5 | Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale. |
| SOL | Misto | 1/5 | Qui pesa di più il report frattale. |
| DOGE | Misto | 1/5 | Qui pesa di più il report frattale. |

## Numeri principali

| Asset | Prezzo | Prezzo 24h | Funding | Open Interest | OI 24h | Long/Short |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | $62,828 | +1.61% | +0.0037% | $1.90B | +8.03% | 2.15 |
| SOL | $77.55 | +0.77% | +0.0043% | $255.95M | -23.92% | 2.70 |
| DOGE | $0.07239 | +0.35% | -0.0010% | $69.54M | +0.12% | 3.33 |

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

**RISCHIO DISCESA / FLUSH SOTTO**  
**Forza segnale: 5/5**

BTC: i futures sembrano più vulnerabili verso una discesa improvvisa. Non significa che deve scendere, ma se rompe sotto può accelerare.

**Tradotto operativamente:** Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale.

### Perché

- funding positivo: i long pagano gli short
- open interest in aumento: più leva nel sistema
- long/short ratio alto: mercato più long

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $62,828 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +1.61% | movimento dell'ultimo giorno |
| Funding | +0.0037% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-10 02:00 | prossimo aggiornamento funding |
| Open Interest stimato | $1.90B | leva aperta stimata in dollari |
| Open Interest 24h | +8.03% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 2.15 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $50,262 | $75,393 |
| 10x | $56,545 | $69,110 |
| 20x | $59,686 | $65,969 |
| 50x | $61,571 | $64,084 |

### Note tecniche usate dallo score

- open interest in forte aumento: entra molta leva
- prezzo su + leva su + funding positivo: rischio pulizia dei long sotto
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
| Prezzo | $77.55 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +0.77% | movimento dell'ultimo giorno |
| Funding | +0.0043% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-10 02:00 | prossimo aggiornamento funding |
| Open Interest stimato | $255.95M | leva aperta stimata in dollari |
| Open Interest 24h | -23.92% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 2.70 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $62.04 | $93.06 |
| 10x | $69.80 | $85.31 |
| 20x | $73.67 | $81.43 |
| 50x | $76.00 | $79.10 |

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

- funding negativo: gli short pagano i long
- open interest abbastanza stabile
- long/short ratio alto: mercato più long

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $0.07239 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +0.35% | movimento dell'ultimo giorno |
| Funding | -0.0010% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-10 02:00 | prossimo aggiornamento funding |
| Open Interest stimato | $69.54M | leva aperta stimata in dollari |
| Open Interest 24h | +0.12% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 3.33 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $0.05791 | $0.08687 |
| 10x | $0.06515 | $0.07963 |
| 20x | $0.06877 | $0.07601 |
| 50x | $0.07094 | $0.07384 |

### Note tecniche usate dallo score

- long/short ratio alto: più mercato sbilanciato long

---
