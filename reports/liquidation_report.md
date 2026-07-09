# Report semplice futures / liquidazioni BTC / SOL / DOGE

Generato: **2026-07-09 20:30:26 CEST**  
UTC: **2026-07-09 18:30:26 UTC**

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
| BTC | $63,328 | +1.95% | +0.0051% | $1.89B | +3.59% | 2.13 |
| SOL | $78.18 | +1.51% | +0.0096% | $256.96M | -28.94% | 2.70 |
| DOGE | $0.07325 | +1.06% | +0.0022% | $71.19M | -4.15% | 3.34 |

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
| Prezzo | $63,328 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +1.95% | movimento dell'ultimo giorno |
| Funding | +0.0051% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-10 02:00 | prossimo aggiornamento funding |
| Open Interest stimato | $1.89B | leva aperta stimata in dollari |
| Open Interest 24h | +3.59% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 2.13 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $50,662 | $75,994 |
| 10x | $56,995 | $69,661 |
| 20x | $60,162 | $66,495 |
| 50x | $62,062 | $64,595 |

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
| Prezzo | $78.18 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +1.51% | movimento dell'ultimo giorno |
| Funding | +0.0096% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-10 02:00 | prossimo aggiornamento funding |
| Open Interest stimato | $256.96M | leva aperta stimata in dollari |
| Open Interest 24h | -28.94% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 2.70 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $62.54 | $93.82 |
| 10x | $70.36 | $86.00 |
| 20x | $74.27 | $82.09 |
| 50x | $76.62 | $79.74 |

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
- open interest in calo: leva in uscita
- long/short ratio alto: mercato più long

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $0.07325 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +1.06% | movimento dell'ultimo giorno |
| Funding | +0.0022% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-10 02:00 | prossimo aggiornamento funding |
| Open Interest stimato | $71.19M | leva aperta stimata in dollari |
| Open Interest 24h | -4.15% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 3.34 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $0.05860 | $0.08790 |
| 10x | $0.06592 | $0.08058 |
| 20x | $0.06959 | $0.07691 |
| 50x | $0.07178 | $0.07472 |

### Note tecniche usate dallo score

- long/short ratio alto: più mercato sbilanciato long

---
