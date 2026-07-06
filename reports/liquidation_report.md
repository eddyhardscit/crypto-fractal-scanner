# Report semplice futures / liquidazioni BTC / SOL / DOGE

Generato: **2026-07-06 14:19:55 CEST**  
UTC: **2026-07-06 12:19:55 UTC**

Fonte dati: **OKX Futures pubblici**.  
Questo report non è la vera heatmap CoinGlass. Serve a capire se il mercato futures è carico di long, short o leva.

## Traduzione in parole semplici

| Asset | Lettura | Forza | Cosa significa in pratica |
| --- | --- | --- | --- |
| BTC | Misto | 2/5 | Qui pesa di più il report frattale. |
| SOL | Misto | 1/5 | Qui pesa di più il report frattale. |
| DOGE | Rischio sotto | 5/5 | Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale. |

## Numeri principali

| Asset | Prezzo | Prezzo 24h | Funding | Open Interest | OI 24h | Long/Short |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | $62,053 | -0.90% | +0.0055% | $1.94B | +2.35% | 1.76 |
| SOL | $80.53 | -0.09% | +0.0052% | $269.23M | -27.46% | 2.81 |
| DOGE | $0.07606 | +0.34% | +0.0035% | $66.87M | +5.79% | 3.04 |

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
**Forza segnale: 2/5**

BTC: i futures non danno una lettura chiara. Non si vede uno sbilanciamento forte né long né short.

**Tradotto operativamente:** Qui pesa di più il report frattale.

### Perché

- funding positivo: i long pagano gli short
- open interest in aumento: più leva nel sistema
- long/short ratio alto: mercato più long

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $62,053 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -0.90% | movimento dell'ultimo giorno |
| Funding | +0.0055% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-06 18:00 | prossimo aggiornamento funding |
| Open Interest stimato | $1.94B | leva aperta stimata in dollari |
| Open Interest 24h | +2.35% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.76 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $49,643 | $74,464 |
| 10x | $55,848 | $68,259 |
| 20x | $58,951 | $65,156 |
| 50x | $60,812 | $63,294 |

### Note tecniche usate dallo score

- open interest in aumento: leva in crescita
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
| Prezzo | $80.53 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -0.09% | movimento dell'ultimo giorno |
| Funding | +0.0052% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-06 18:00 | prossimo aggiornamento funding |
| Open Interest stimato | $269.23M | leva aperta stimata in dollari |
| Open Interest 24h | -27.46% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 2.81 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $64.42 | $96.64 |
| 10x | $72.48 | $88.58 |
| 20x | $76.50 | $84.56 |
| 50x | $78.92 | $82.14 |

### Note tecniche usate dallo score

- open interest in forte calo: parte della leva è già uscita
- long/short ratio alto: più mercato sbilanciato long

---

## Dogecoin — DOGE

### Lettura semplice

**RISCHIO DISCESA / FLUSH SOTTO**  
**Forza segnale: 5/5**

DOGE: i futures sembrano più vulnerabili verso una discesa improvvisa. Non significa che deve scendere, ma se rompe sotto può accelerare.

**Tradotto operativamente:** Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale.

### Perché

- funding positivo: i long pagano gli short
- open interest in aumento: più leva nel sistema
- long/short ratio alto: mercato più long

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $0.07606 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +0.34% | movimento dell'ultimo giorno |
| Funding | +0.0035% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-06 18:00 | prossimo aggiornamento funding |
| Open Interest stimato | $66.87M | leva aperta stimata in dollari |
| Open Interest 24h | +5.79% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 3.04 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $0.06085 | $0.09127 |
| 10x | $0.06845 | $0.08367 |
| 20x | $0.07226 | $0.07986 |
| 50x | $0.07454 | $0.07758 |

### Note tecniche usate dallo score

- open interest in forte aumento: entra molta leva
- prezzo su + leva su + funding positivo: rischio pulizia dei long sotto
- long/short ratio alto: più mercato sbilanciato long

---
