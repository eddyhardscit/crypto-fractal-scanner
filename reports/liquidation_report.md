# Report semplice futures / liquidazioni BTC / SOL / DOGE

Generato: **2026-07-09 17:39:47 CEST**  
UTC: **2026-07-09 15:39:47 UTC**

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
| BTC | $62,939 | +2.05% | +0.0032% | $1.91B | +7.96% | 2.14 |
| SOL | $77.68 | +1.53% | +0.0031% | $253.80M | -23.59% | 2.66 |
| DOGE | $0.07258 | +1.26% | -0.0006% | $70.00M | +1.54% | 3.11 |

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
| Prezzo | $62,939 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +2.05% | movimento dell'ultimo giorno |
| Funding | +0.0032% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-09 18:00 | prossimo aggiornamento funding |
| Open Interest stimato | $1.91B | leva aperta stimata in dollari |
| Open Interest 24h | +7.96% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 2.14 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $50,351 | $75,526 |
| 10x | $56,645 | $69,232 |
| 20x | $59,792 | $66,086 |
| 50x | $61,680 | $64,197 |

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
| Prezzo | $77.68 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +1.53% | movimento dell'ultimo giorno |
| Funding | +0.0031% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-09 18:00 | prossimo aggiornamento funding |
| Open Interest stimato | $253.80M | leva aperta stimata in dollari |
| Open Interest 24h | -23.59% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 2.66 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $62.14 | $93.22 |
| 10x | $69.91 | $85.45 |
| 20x | $73.80 | $81.56 |
| 50x | $76.13 | $79.23 |

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
| Prezzo | $0.07258 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +1.26% | movimento dell'ultimo giorno |
| Funding | -0.0006% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-09 18:00 | prossimo aggiornamento funding |
| Open Interest stimato | $70.00M | leva aperta stimata in dollari |
| Open Interest 24h | +1.54% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 3.11 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $0.05806 | $0.08710 |
| 10x | $0.06532 | $0.07984 |
| 20x | $0.06895 | $0.07621 |
| 50x | $0.07113 | $0.07403 |

### Note tecniche usate dallo score

- long/short ratio alto: più mercato sbilanciato long

---
