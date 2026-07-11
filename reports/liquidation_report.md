# Report semplice futures / liquidazioni BTC / SOL / DOGE

Generato: **2026-07-11 19:35:43 CEST**  
UTC: **2026-07-11 17:35:43 UTC**

Fonte dati: **OKX Futures pubblici**.  
Questo report non è la vera heatmap CoinGlass. Serve a capire se il mercato futures è carico di long, short o leva.

## Traduzione in parole semplici

| Asset | Lettura | Forza | Cosa significa in pratica |
| --- | --- | --- | --- |
| BTC | Rischio sotto | 4/5 | Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale. |
| SOL | Misto | 1/5 | Qui pesa di più il report frattale. |
| DOGE | Rischio sotto | 4/5 | Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale. |

## Numeri principali

| Asset | Prezzo | Prezzo 24h | Funding | Open Interest | OI 24h | Long/Short |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 64.260 $ | +0.78% | +0.0058% | $2.01B | +3.98% | 1.51 |
| SOL | 77,96 $ | +0.58% | +0.0076% | $243.10M | -23.17% | 2.17 |
| DOGE | 0.07515 $ | +1.79% | +0.0046% | $70.78M | +2.34% | 2.38 |

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
| Prezzo | $64,379 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +0.78% | movimento dell'ultimo giorno |
| Funding | +0.0058% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-12 02:00 | prossimo aggiornamento funding |
| Open Interest stimato | $2.01B | leva aperta stimata in dollari |
| Open Interest 24h | +3.98% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.51 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $51,503 | $77,255 |
| 10x | $57,941 | $70,817 |
| 20x | $61,160 | $67,598 |
| 50x | $63,092 | $65,667 |

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
| Prezzo | $78.12 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +0.58% | movimento dell'ultimo giorno |
| Funding | +0.0076% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-12 02:00 | prossimo aggiornamento funding |
| Open Interest stimato | $243.10M | leva aperta stimata in dollari |
| Open Interest 24h | -23.17% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 2.17 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $62.50 | $93.74 |
| 10x | $70.31 | $85.93 |
| 20x | $74.21 | $82.03 |
| 50x | $76.56 | $79.68 |

### Note tecniche usate dallo score

- open interest in forte calo: parte della leva è già uscita
- long/short ratio alto: più mercato sbilanciato long

---

## Dogecoin — DOGE

### Lettura semplice

**RISCHIO DISCESA / FLUSH SOTTO**  
**Forza segnale: 4/5**

DOGE: i futures sembrano più vulnerabili verso una discesa improvvisa. Non significa che deve scendere, ma se rompe sotto può accelerare.

**Tradotto operativamente:** Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale.

### Perché

- funding positivo: i long pagano gli short
- open interest in aumento: più leva nel sistema
- long/short ratio alto: mercato più long

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $0.07519 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +1.79% | movimento dell'ultimo giorno |
| Funding | +0.0046% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-12 02:00 | prossimo aggiornamento funding |
| Open Interest stimato | $70.78M | leva aperta stimata in dollari |
| Open Interest 24h | +2.34% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 2.38 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $0.06015 | $0.09023 |
| 10x | $0.06767 | $0.08271 |
| 20x | $0.07143 | $0.07895 |
| 50x | $0.07369 | $0.07669 |

### Note tecniche usate dallo score

- open interest in aumento: leva in crescita
- prezzo su + leva su + funding positivo: rischio pulizia dei long sotto
- long/short ratio alto: più mercato sbilanciato long

---
