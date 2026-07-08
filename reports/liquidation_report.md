# Report semplice futures / liquidazioni BTC / SOL / DOGE

Generato: **2026-07-08 13:23:07 CEST**  
UTC: **2026-07-08 11:23:07 UTC**

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
| BTC | $62,091 | -1.72% | +0.0027% | $1.92B | -7.83% | 1.58 |
| SOL | $77.09 | -4.76% | +0.0100% | $250.74M | -30.65% | 2.70 |
| DOGE | $0.07163 | -3.92% | +0.0076% | $70.48M | -2.97% | 3.18 |

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
| Prezzo | $62,091 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -1.72% | movimento dell'ultimo giorno |
| Funding | +0.0027% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-08 18:00 | prossimo aggiornamento funding |
| Open Interest stimato | $1.92B | leva aperta stimata in dollari |
| Open Interest 24h | -7.83% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.58 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $49,673 | $74,509 |
| 10x | $55,882 | $68,300 |
| 20x | $58,986 | $65,195 |
| 50x | $60,849 | $63,333 |

### Note tecniche usate dallo score

- open interest in forte calo: parte della leva è già uscita
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
| Prezzo | $77.09 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -4.76% | movimento dell'ultimo giorno |
| Funding | +0.0100% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-08 18:00 | prossimo aggiornamento funding |
| Open Interest stimato | $250.74M | leva aperta stimata in dollari |
| Open Interest 24h | -30.65% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 2.70 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $61.67 | $92.51 |
| 10x | $69.38 | $84.80 |
| 20x | $73.24 | $80.94 |
| 50x | $75.55 | $78.63 |

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
| Prezzo | $0.07163 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -3.92% | movimento dell'ultimo giorno |
| Funding | +0.0076% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-08 18:00 | prossimo aggiornamento funding |
| Open Interest stimato | $70.48M | leva aperta stimata in dollari |
| Open Interest 24h | -2.97% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 3.18 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $0.05730 | $0.08596 |
| 10x | $0.06447 | $0.07879 |
| 20x | $0.06805 | $0.07521 |
| 50x | $0.07020 | $0.07306 |

### Note tecniche usate dallo score

- long/short ratio alto: più mercato sbilanciato long

---
