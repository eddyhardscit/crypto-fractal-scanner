# Report semplice futures / liquidazioni BTC / SOL / DOGE

Generato: **2026-07-08 14:15:53 CEST**  
UTC: **2026-07-08 12:15:53 UTC**

Fonte dati: **OKX Futures pubblici**.  
Questo report non è la vera heatmap CoinGlass. Serve a capire se il mercato futures è carico di long, short o leva.

## Traduzione in parole semplici

| Asset | Lettura | Forza | Cosa significa in pratica |
| --- | --- | --- | --- |
| BTC | Misto | 1/5 | Qui pesa di più il report frattale. |
| SOL | Rischio sotto | 2/5 | Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale. |
| DOGE | Misto | 1/5 | Qui pesa di più il report frattale. |

## Numeri principali

| Asset | Prezzo | Prezzo 24h | Funding | Open Interest | OI 24h | Long/Short |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | $62,290 | -2.28% | +0.0037% | $1.92B | -2.58% | 1.62 |
| SOL | $77.45 | -5.23% | +0.0100% | $254.62M | -26.10% | 2.71 |
| DOGE | $0.07205 | -4.19% | +0.0072% | $70.94M | -2.27% | 3.16 |

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

**NEUTRALE / POCO CHIARO**  
**Forza segnale: 1/5**

BTC: i futures non danno una lettura chiara. Non si vede uno sbilanciamento forte né long né short.

**Tradotto operativamente:** Qui pesa di più il report frattale.

### Perché

- funding positivo: i long pagano gli short
- open interest in calo: leva in uscita
- long/short ratio alto: mercato più long

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $62,290 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -2.28% | movimento dell'ultimo giorno |
| Funding | +0.0037% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-08 18:00 | prossimo aggiornamento funding |
| Open Interest stimato | $1.92B | leva aperta stimata in dollari |
| Open Interest 24h | -2.58% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.62 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $49,832 | $74,748 |
| 10x | $56,061 | $68,519 |
| 20x | $59,176 | $65,405 |
| 50x | $61,044 | $63,536 |

### Note tecniche usate dallo score

- long/short ratio alto: più mercato sbilanciato long

---

## Solana — SOL

### Lettura semplice

**RISCHIO DISCESA / FLUSH SOTTO**  
**Forza segnale: 2/5**

SOL: i futures sembrano più vulnerabili verso una discesa improvvisa. Non significa che deve scendere, ma se rompe sotto può accelerare.

**Tradotto operativamente:** Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale.

### Perché

- funding positivo: i long pagano gli short
- open interest in calo: leva in uscita
- long/short ratio alto: mercato più long

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $77.45 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -5.23% | movimento dell'ultimo giorno |
| Funding | +0.0100% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-08 18:00 | prossimo aggiornamento funding |
| Open Interest stimato | $254.62M | leva aperta stimata in dollari |
| Open Interest 24h | -26.10% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 2.71 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $61.96 | $92.94 |
| 10x | $69.70 | $85.20 |
| 20x | $73.58 | $81.32 |
| 50x | $75.90 | $79.00 |

### Note tecniche usate dallo score

- funding positivo: mercato leggermente carico di long
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
| Prezzo | $0.07205 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -4.19% | movimento dell'ultimo giorno |
| Funding | +0.0072% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-08 18:00 | prossimo aggiornamento funding |
| Open Interest stimato | $70.94M | leva aperta stimata in dollari |
| Open Interest 24h | -2.27% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 3.16 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $0.05764 | $0.08646 |
| 10x | $0.06484 | $0.07926 |
| 20x | $0.06845 | $0.07565 |
| 50x | $0.07061 | $0.07349 |

### Note tecniche usate dallo score

- long/short ratio alto: più mercato sbilanciato long

---
