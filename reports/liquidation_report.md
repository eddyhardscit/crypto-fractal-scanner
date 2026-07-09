# Report semplice futures / liquidazioni BTC / SOL / DOGE

Generato: **2026-07-10 01:43:35 CEST**  
UTC: **2026-07-09 23:43:35 UTC**

Fonte dati: **OKX Futures pubblici**.  
Questo report non è la vera heatmap CoinGlass. Serve a capire se il mercato futures è carico di long, short o leva.

## Traduzione in parole semplici

| Asset | Lettura | Forza | Cosa significa in pratica |
| --- | --- | --- | --- |
| BTC | Rischio sotto | 4/5 | Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale. |
| SOL | Misto | 1/5 | Qui pesa di più il report frattale. |
| DOGE | Misto | 1/5 | Qui pesa di più il report frattale. |

## Numeri principali

| Asset | Prezzo | Prezzo 24h | Funding | Open Interest | OI 24h | Long/Short |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | $63,259 | +1.70% | +0.0073% | $1.90B | +3.39% | 1.92 |
| SOL | $78.01 | +0.61% | +0.0037% | $254.60M | -28.65% | 2.62 |
| DOGE | $0.07284 | +0.82% | +0.0048% | $69.76M | -3.79% | 3.07 |

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
**Forza segnale: 4/5**

BTC: i futures sembrano più vulnerabili verso una discesa improvvisa. Non significa che deve scendere, ma se rompe sotto può accelerare.

**Tradotto operativamente:** Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale.

### Perché

- funding positivo: i long pagano gli short
- open interest in aumento: più leva nel sistema
- long/short ratio alto: mercato più long

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $63,259 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +1.70% | movimento dell'ultimo giorno |
| Funding | +0.0073% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-10 02:00 | prossimo aggiornamento funding |
| Open Interest stimato | $1.90B | leva aperta stimata in dollari |
| Open Interest 24h | +3.39% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.92 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $50,607 | $75,910 |
| 10x | $56,933 | $69,585 |
| 20x | $60,096 | $66,422 |
| 50x | $61,994 | $64,524 |

### Note tecniche usate dallo score

- open interest in aumento: leva in crescita
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
| Prezzo | $78.01 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +0.61% | movimento dell'ultimo giorno |
| Funding | +0.0037% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-10 02:00 | prossimo aggiornamento funding |
| Open Interest stimato | $254.60M | leva aperta stimata in dollari |
| Open Interest 24h | -28.65% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 2.62 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $62.41 | $93.61 |
| 10x | $70.21 | $85.81 |
| 20x | $74.11 | $81.91 |
| 50x | $76.45 | $79.57 |

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
- open interest in calo: leva in uscita
- long/short ratio alto: mercato più long

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $0.07284 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +0.82% | movimento dell'ultimo giorno |
| Funding | +0.0048% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-10 02:00 | prossimo aggiornamento funding |
| Open Interest stimato | $69.76M | leva aperta stimata in dollari |
| Open Interest 24h | -3.79% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 3.07 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $0.05827 | $0.08741 |
| 10x | $0.06556 | $0.08012 |
| 20x | $0.06920 | $0.07648 |
| 50x | $0.07138 | $0.07430 |

### Note tecniche usate dallo score

- long/short ratio alto: più mercato sbilanciato long

---
