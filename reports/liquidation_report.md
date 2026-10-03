# Report semplice futures / liquidazioni BTC / SOL / DOGE

Generato: **2026-10-03 07:32:46 CEST**  
UTC: **2026-10-03 05:32:46 UTC**

Fonte dati: **OKX Futures pubblici**.  
Questo report non è la vera heatmap CoinGlass. Serve a capire se il mercato futures è carico di long, short o leva.

## Traduzione in parole semplici

| Asset | Lettura | Forza | Cosa significa in pratica |
| --- | --- | --- | --- |
| BTC | Misto | 1/5 | Qui pesa di più il report frattale. |
| SOL | Misto | 1/5 | Qui pesa di più il report frattale. |
| DOGE | Rischio sotto | 2/5 | Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale. |

## Numeri principali

| Asset | Prezzo | Prezzo 24h | Funding | Open Interest | OI 24h | Long/Short |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 84.612 $ | -2.01% | +0.0031% | $2.43B | n/d | 1.24 |
| SOL | 119,53 $ | -2.69% | +0.0023% | $353.50M | n/d | 1.92 |
| DOGE | 0.09315 $ | -3.33% | +0.0100% | $100.06M | n/d | 4.00 |

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
- long/short ratio abbastanza equilibrato

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $84,606 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -2.01% | movimento dell'ultimo giorno |
| Funding | +0.0031% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-10-03 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $2.43B | leva aperta stimata in dollari |
| Open Interest 24h | n/d | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.24 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $67,685 | $101,527 |
| 10x | $76,145 | $93,067 |
| 20x | $80,376 | $88,836 |
| 50x | $82,914 | $86,298 |

---

## Solana — SOL

### Lettura semplice

**NEUTRALE / POCO CHIARO**  
**Forza segnale: 1/5**

SOL: i futures non danno una lettura chiara. Non si vede uno sbilanciamento forte né long né short.

**Tradotto operativamente:** Qui pesa di più il report frattale.

### Perché

- funding positivo: i long pagano gli short
- long/short ratio alto: mercato più long

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $119.57 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -2.69% | movimento dell'ultimo giorno |
| Funding | +0.0023% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-10-03 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $353.50M | leva aperta stimata in dollari |
| Open Interest 24h | n/d | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.92 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $95.66 | $143.48 |
| 10x | $107.61 | $131.53 |
| 20x | $113.59 | $125.55 |
| 50x | $117.18 | $121.96 |

### Note tecniche usate dallo score

- long/short ratio alto: più mercato sbilanciato long

---

## Dogecoin — DOGE

### Lettura semplice

**RISCHIO DISCESA / FLUSH SOTTO**  
**Forza segnale: 2/5**

DOGE: i futures sembrano più vulnerabili verso una discesa improvvisa. Non significa che deve scendere, ma se rompe sotto può accelerare.

**Tradotto operativamente:** Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale.

### Perché

- funding positivo: i long pagano gli short
- long/short ratio alto: mercato più long

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $0.09316 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -3.33% | movimento dell'ultimo giorno |
| Funding | +0.0100% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-10-03 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $100.06M | leva aperta stimata in dollari |
| Open Interest 24h | n/d | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 4.00 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $0.07453 | $0.11179 |
| 10x | $0.08384 | $0.10248 |
| 20x | $0.08850 | $0.09782 |
| 50x | $0.09130 | $0.09502 |

### Note tecniche usate dallo score

- funding positivo: mercato leggermente carico di long
- long/short ratio alto: più mercato sbilanciato long

---
