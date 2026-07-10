# Report semplice futures / liquidazioni BTC / SOL / DOGE

Generato: **2026-07-10 05:11:57 CEST**  
UTC: **2026-07-10 03:11:57 UTC**

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
| BTC | $63,890 | +3.44% | +0.0052% | $1.93B | +3.01% | 1.98 |
| SOL | $78.80 | +2.54% | +0.0008% | $249.81M | -26.21% | 2.56 |
| DOGE | $0.07391 | +2.44% | +0.0043% | $69.27M | -0.08% | 3.04 |

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
| Prezzo | $63,890 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +3.44% | movimento dell'ultimo giorno |
| Funding | +0.0052% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-10 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $1.93B | leva aperta stimata in dollari |
| Open Interest 24h | +3.01% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.98 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $51,112 | $76,668 |
| 10x | $57,501 | $70,279 |
| 20x | $60,696 | $67,085 |
| 50x | $62,613 | $65,168 |

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
| Prezzo | $78.80 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +2.54% | movimento dell'ultimo giorno |
| Funding | +0.0008% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-10 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $249.81M | leva aperta stimata in dollari |
| Open Interest 24h | -26.21% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 2.56 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $63.04 | $94.56 |
| 10x | $70.92 | $86.68 |
| 20x | $74.86 | $82.74 |
| 50x | $77.22 | $80.38 |

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
- open interest abbastanza stabile
- long/short ratio alto: mercato più long

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $0.07391 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +2.44% | movimento dell'ultimo giorno |
| Funding | +0.0043% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-10 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $69.27M | leva aperta stimata in dollari |
| Open Interest 24h | -0.08% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 3.04 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $0.05913 | $0.08869 |
| 10x | $0.06652 | $0.08130 |
| 20x | $0.07021 | $0.07761 |
| 50x | $0.07243 | $0.07539 |

### Note tecniche usate dallo score

- long/short ratio alto: più mercato sbilanciato long

---
