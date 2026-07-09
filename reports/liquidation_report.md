# Report semplice futures / liquidazioni BTC / SOL / DOGE

Generato: **2026-07-09 17:02:51 CEST**  
UTC: **2026-07-09 15:02:51 UTC**

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
| BTC | $62,926 | +1.74% | +0.0037% | $1.90B | +7.71% | 2.14 |
| SOL | $77.67 | +0.94% | +0.0022% | $252.47M | -23.55% | 2.66 |
| DOGE | $0.07254 | +1.03% | +0.0008% | $70.05M | +1.52% | 3.08 |

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
| Prezzo | $62,926 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +1.74% | movimento dell'ultimo giorno |
| Funding | +0.0037% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-09 18:00 | prossimo aggiornamento funding |
| Open Interest stimato | $1.90B | leva aperta stimata in dollari |
| Open Interest 24h | +7.71% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 2.14 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $50,341 | $75,511 |
| 10x | $56,633 | $69,218 |
| 20x | $59,780 | $66,072 |
| 50x | $61,667 | $64,184 |

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
| Prezzo | $77.67 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +0.94% | movimento dell'ultimo giorno |
| Funding | +0.0022% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-09 18:00 | prossimo aggiornamento funding |
| Open Interest stimato | $252.47M | leva aperta stimata in dollari |
| Open Interest 24h | -23.55% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 2.66 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $62.14 | $93.20 |
| 10x | $69.90 | $85.44 |
| 20x | $73.79 | $81.55 |
| 50x | $76.12 | $79.22 |

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
| Prezzo | $0.07254 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +1.03% | movimento dell'ultimo giorno |
| Funding | +0.0008% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-09 18:00 | prossimo aggiornamento funding |
| Open Interest stimato | $70.05M | leva aperta stimata in dollari |
| Open Interest 24h | +1.52% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 3.08 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $0.05803 | $0.08705 |
| 10x | $0.06529 | $0.07979 |
| 20x | $0.06891 | $0.07617 |
| 50x | $0.07109 | $0.07399 |

### Note tecniche usate dallo score

- long/short ratio alto: più mercato sbilanciato long

---
