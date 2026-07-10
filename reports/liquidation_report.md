# Report semplice futures / liquidazioni BTC / SOL / DOGE

Generato: **2026-07-10 02:30:56 CEST**  
UTC: **2026-07-10 00:30:56 UTC**

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
| BTC | $63,061 | +1.39% | +0.0072% | $1.90B | +3.30% | 1.90 |
| SOL | $77.95 | +0.35% | +0.0022% | $253.97M | -28.14% | 2.61 |
| DOGE | $0.07278 | +0.78% | +0.0031% | $69.61M | -3.75% | 3.04 |

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
| Prezzo | $63,061 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +1.39% | movimento dell'ultimo giorno |
| Funding | +0.0072% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-10 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $1.90B | leva aperta stimata in dollari |
| Open Interest 24h | +3.30% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.90 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $50,449 | $75,673 |
| 10x | $56,755 | $69,367 |
| 20x | $59,908 | $66,214 |
| 50x | $61,800 | $64,322 |

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
| Prezzo | $77.95 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +0.35% | movimento dell'ultimo giorno |
| Funding | +0.0022% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-10 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $253.97M | leva aperta stimata in dollari |
| Open Interest 24h | -28.14% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 2.61 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $62.36 | $93.54 |
| 10x | $70.16 | $85.75 |
| 20x | $74.05 | $81.85 |
| 50x | $76.39 | $79.51 |

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
| Prezzo | $0.07278 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +0.78% | movimento dell'ultimo giorno |
| Funding | +0.0031% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-10 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $69.61M | leva aperta stimata in dollari |
| Open Interest 24h | -3.75% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 3.04 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $0.05822 | $0.08734 |
| 10x | $0.06550 | $0.08006 |
| 20x | $0.06914 | $0.07642 |
| 50x | $0.07132 | $0.07424 |

### Note tecniche usate dallo score

- long/short ratio alto: più mercato sbilanciato long

---
