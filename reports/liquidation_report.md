# Report semplice futures / liquidazioni BTC / SOL / DOGE

Generato: **2026-08-04 07:17:20 CEST**  
UTC: **2026-08-04 05:17:20 UTC**

Fonte dati: **OKX Futures pubblici**.  
Questo report non è la vera heatmap CoinGlass. Serve a capire se il mercato futures è carico di long, short o leva.

## Traduzione in parole semplici

| Asset | Lettura | Forza | Cosa significa in pratica |
| --- | --- | --- | --- |
| BTC | Misto | 1/5 | Qui pesa di più il report frattale. |
| SOL | Rischio sotto | 5/5 | Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale. |
| DOGE | Misto | 1/5 | Qui pesa di più il report frattale. |

## Numeri principali

| Asset | Prezzo | Prezzo 24h | Funding | Open Interest | OI 24h | Long/Short |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 63.846 $ | +1.71% | +0.0026% | $2.04B | -3.78% | 1.48 |
| SOL | 73,72 $ | +1.18% | +0.0100% | $209.56M | +30.70% | 1.59 |
| DOGE | 0.07019 $ | +0.66% | +0.0062% | $78.75M | -11.27% | 3.08 |

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
| Prezzo | $63,856 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +1.71% | movimento dell'ultimo giorno |
| Funding | +0.0026% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-08-04 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $2.04B | leva aperta stimata in dollari |
| Open Interest 24h | -3.78% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.48 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $51,085 | $76,628 |
| 10x | $57,471 | $70,242 |
| 20x | $60,664 | $67,049 |
| 50x | $62,579 | $65,134 |

### Note tecniche usate dallo score

- long/short ratio alto: più mercato sbilanciato long

---

## Solana — SOL

### Lettura semplice

**RISCHIO DISCESA / FLUSH SOTTO**  
**Forza segnale: 5/5**

SOL: i futures sembrano più vulnerabili verso una discesa improvvisa. Non significa che deve scendere, ma se rompe sotto può accelerare.

**Tradotto operativamente:** Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale.

### Perché

- funding positivo: i long pagano gli short
- open interest in aumento: più leva nel sistema
- long/short ratio alto: mercato più long

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $73.72 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +1.18% | movimento dell'ultimo giorno |
| Funding | +0.0100% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-08-04 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $209.56M | leva aperta stimata in dollari |
| Open Interest 24h | +30.70% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.59 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $58.98 | $88.46 |
| 10x | $66.35 | $81.09 |
| 20x | $70.03 | $77.41 |
| 50x | $72.25 | $75.19 |

### Note tecniche usate dallo score

- funding positivo: mercato leggermente carico di long
- open interest in forte aumento: entra molta leva
- prezzo su + leva su + funding positivo: rischio pulizia dei long sotto
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
| Prezzo | $0.07022 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +0.66% | movimento dell'ultimo giorno |
| Funding | +0.0062% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-08-04 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $78.75M | leva aperta stimata in dollari |
| Open Interest 24h | -11.27% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 3.08 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $0.05618 | $0.08426 |
| 10x | $0.06320 | $0.07724 |
| 20x | $0.06671 | $0.07373 |
| 50x | $0.06882 | $0.07162 |

### Note tecniche usate dallo score

- open interest in forte calo: parte della leva è già uscita
- long/short ratio alto: più mercato sbilanciato long

---
