# Report semplice futures / liquidazioni BTC / SOL / DOGE

Generato: **2026-07-10 06:35:30 CEST**  
UTC: **2026-07-10 04:35:30 UTC**

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
| BTC | $64,059 | +2.94% | +0.0051% | $1.93B | +2.53% | 1.88 |
| SOL | $78.98 | +1.77% | +0.0030% | $248.80M | -25.49% | 2.55 |
| DOGE | $0.07399 | +2.11% | +0.0074% | $69.80M | +0.27% | 3.05 |

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
| Prezzo | $64,059 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +2.94% | movimento dell'ultimo giorno |
| Funding | +0.0051% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-10 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $1.93B | leva aperta stimata in dollari |
| Open Interest 24h | +2.53% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.88 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $51,247 | $76,871 |
| 10x | $57,653 | $70,465 |
| 20x | $60,856 | $67,262 |
| 50x | $62,778 | $65,340 |

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
| Prezzo | $78.98 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +1.77% | movimento dell'ultimo giorno |
| Funding | +0.0030% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-10 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $248.80M | leva aperta stimata in dollari |
| Open Interest 24h | -25.49% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 2.55 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $63.18 | $94.78 |
| 10x | $71.08 | $86.88 |
| 20x | $75.03 | $82.93 |
| 50x | $77.40 | $80.56 |

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
| Prezzo | $0.07399 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +2.11% | movimento dell'ultimo giorno |
| Funding | +0.0074% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-10 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $69.80M | leva aperta stimata in dollari |
| Open Interest 24h | +0.27% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 3.05 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $0.05919 | $0.08879 |
| 10x | $0.06659 | $0.08139 |
| 20x | $0.07029 | $0.07769 |
| 50x | $0.07251 | $0.07547 |

### Note tecniche usate dallo score

- long/short ratio alto: più mercato sbilanciato long

---
