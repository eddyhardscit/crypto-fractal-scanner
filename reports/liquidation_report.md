# Report semplice futures / liquidazioni BTC / SOL / DOGE

Generato: **2026-08-15 07:34:11 CEST**  
UTC: **2026-08-15 05:34:11 UTC**

Fonte dati: **OKX Futures pubblici**.  
Questo report non è la vera heatmap CoinGlass. Serve a capire se il mercato futures è carico di long, short o leva.

## Traduzione in parole semplici

| Asset | Lettura | Forza | Cosa significa in pratica |
| --- | --- | --- | --- |
| BTC | Rischio sotto | 2/5 | Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale. |
| SOL | Misto | 1/5 | Qui pesa di più il report frattale. |
| DOGE | Misto | 1/5 | Qui pesa di più il report frattale. |

## Numeri principali

| Asset | Prezzo | Prezzo 24h | Funding | Open Interest | OI 24h | Long/Short |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 63.051 $ | -0.37% | +0.0100% | $2.15B | -5.12% | 1.31 |
| SOL | 75,39 $ | -0.58% | +0.0029% | $223.04M | +0.33% | 2.43 |
| DOGE | 0.07014 $ | +0.30% | +0.0099% | $83.52M | -13.10% | 4.31 |

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
**Forza segnale: 2/5**

BTC: i futures sembrano più vulnerabili verso una discesa improvvisa. Non significa che deve scendere, ma se rompe sotto può accelerare.

**Tradotto operativamente:** Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale.

### Perché

- funding positivo: i long pagano gli short
- open interest in calo: leva in uscita
- long/short ratio alto: mercato più long

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $63,096 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -0.37% | movimento dell'ultimo giorno |
| Funding | +0.0100% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-08-15 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $2.15B | leva aperta stimata in dollari |
| Open Interest 24h | -5.12% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.31 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $50,477 | $75,715 |
| 10x | $56,786 | $69,405 |
| 20x | $59,941 | $66,250 |
| 50x | $61,834 | $64,358 |

### Note tecniche usate dallo score

- funding positivo: mercato leggermente carico di long
- open interest in forte calo: parte della leva è già uscita
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
- open interest abbastanza stabile
- long/short ratio alto: mercato più long

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $75.41 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -0.58% | movimento dell'ultimo giorno |
| Funding | +0.0029% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-08-15 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $223.04M | leva aperta stimata in dollari |
| Open Interest 24h | +0.33% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 2.43 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $60.33 | $90.49 |
| 10x | $67.87 | $82.95 |
| 20x | $71.64 | $79.18 |
| 50x | $73.90 | $76.92 |

### Note tecniche usate dallo score

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
| Prezzo | $0.07019 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +0.30% | movimento dell'ultimo giorno |
| Funding | +0.0099% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-08-15 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $83.52M | leva aperta stimata in dollari |
| Open Interest 24h | -13.10% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 4.31 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $0.05615 | $0.08423 |
| 10x | $0.06317 | $0.07721 |
| 20x | $0.06668 | $0.07370 |
| 50x | $0.06879 | $0.07159 |

### Note tecniche usate dallo score

- open interest in forte calo: parte della leva è già uscita
- long/short ratio alto: più mercato sbilanciato long

---
