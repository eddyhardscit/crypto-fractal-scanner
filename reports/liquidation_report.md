# Report semplice futures / liquidazioni BTC / SOL / DOGE

Generato: **2026-07-09 17:57:35 CEST**  
UTC: **2026-07-09 15:57:35 UTC**

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
| BTC | $62,866 | +1.98% | +0.0034% | $1.90B | +7.96% | 2.14 |
| SOL | $77.59 | +1.33% | +0.0036% | $254.02M | -23.59% | 2.66 |
| DOGE | $0.07257 | +1.06% | -0.0009% | $70.06M | +1.54% | 3.11 |

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
| Prezzo | $62,866 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +1.98% | movimento dell'ultimo giorno |
| Funding | +0.0034% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-09 18:00 | prossimo aggiornamento funding |
| Open Interest stimato | $1.90B | leva aperta stimata in dollari |
| Open Interest 24h | +7.96% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 2.14 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $50,292 | $75,439 |
| 10x | $56,579 | $69,152 |
| 20x | $59,722 | $66,009 |
| 50x | $61,608 | $64,123 |

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
| Prezzo | $77.59 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +1.33% | movimento dell'ultimo giorno |
| Funding | +0.0036% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-09 18:00 | prossimo aggiornamento funding |
| Open Interest stimato | $254.02M | leva aperta stimata in dollari |
| Open Interest 24h | -23.59% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 2.66 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $62.07 | $93.11 |
| 10x | $69.83 | $85.35 |
| 20x | $73.71 | $81.47 |
| 50x | $76.04 | $79.14 |

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
| Prezzo | $0.07257 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +1.06% | movimento dell'ultimo giorno |
| Funding | -0.0009% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-09 18:00 | prossimo aggiornamento funding |
| Open Interest stimato | $70.06M | leva aperta stimata in dollari |
| Open Interest 24h | +1.54% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 3.11 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $0.05806 | $0.08708 |
| 10x | $0.06531 | $0.07983 |
| 20x | $0.06894 | $0.07620 |
| 50x | $0.07112 | $0.07402 |

### Note tecniche usate dallo score

- long/short ratio alto: più mercato sbilanciato long

---
