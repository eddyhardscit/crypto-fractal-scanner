# Report semplice futures / liquidazioni BTC / SOL / DOGE

Generato: **2026-07-09 19:19:06 CEST**  
UTC: **2026-07-09 17:19:06 UTC**

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
| BTC | $62,774 | +1.18% | +0.0056% | $1.88B | +5.29% | 2.13 |
| SOL | $77.88 | +0.92% | +0.0073% | $258.10M | -28.01% | 2.73 |
| DOGE | $0.07281 | +0.55% | -0.0003% | $70.21M | -2.71% | 3.34 |

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
| Prezzo | $62,774 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +1.18% | movimento dell'ultimo giorno |
| Funding | +0.0056% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-10 02:00 | prossimo aggiornamento funding |
| Open Interest stimato | $1.88B | leva aperta stimata in dollari |
| Open Interest 24h | +5.29% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 2.13 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $50,219 | $75,329 |
| 10x | $56,497 | $69,051 |
| 20x | $59,635 | $65,913 |
| 50x | $61,519 | $64,029 |

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
| Prezzo | $77.88 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +0.92% | movimento dell'ultimo giorno |
| Funding | +0.0073% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-10 02:00 | prossimo aggiornamento funding |
| Open Interest stimato | $258.10M | leva aperta stimata in dollari |
| Open Interest 24h | -28.01% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 2.73 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $62.30 | $93.46 |
| 10x | $70.09 | $85.67 |
| 20x | $73.99 | $81.77 |
| 50x | $76.32 | $79.44 |

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
- open interest in calo: leva in uscita
- long/short ratio alto: mercato più long

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $0.07281 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +0.55% | movimento dell'ultimo giorno |
| Funding | -0.0003% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-10 02:00 | prossimo aggiornamento funding |
| Open Interest stimato | $70.21M | leva aperta stimata in dollari |
| Open Interest 24h | -2.71% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 3.34 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $0.05825 | $0.08737 |
| 10x | $0.06553 | $0.08009 |
| 20x | $0.06917 | $0.07645 |
| 50x | $0.07135 | $0.07427 |

### Note tecniche usate dallo score

- long/short ratio alto: più mercato sbilanciato long

---
