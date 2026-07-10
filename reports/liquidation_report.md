# Report semplice futures / liquidazioni BTC / SOL / DOGE

Generato: **2026-07-10 03:35:30 CEST**  
UTC: **2026-07-10 01:35:30 UTC**

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
| BTC | $63,307 | +1.67% | +0.0064% | $1.91B | +3.51% | 1.90 |
| SOL | $78.26 | +0.44% | +0.0006% | $253.09M | -27.71% | 2.60 |
| DOGE | $0.07314 | +0.87% | +0.0023% | $70.08M | -1.91% | 3.05 |

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
| Prezzo | $63,307 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +1.67% | movimento dell'ultimo giorno |
| Funding | +0.0064% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-10 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $1.91B | leva aperta stimata in dollari |
| Open Interest 24h | +3.51% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.90 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $50,646 | $75,969 |
| 10x | $56,977 | $69,638 |
| 20x | $60,142 | $66,473 |
| 50x | $62,041 | $64,574 |

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
| Prezzo | $78.26 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +0.44% | movimento dell'ultimo giorno |
| Funding | +0.0006% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-10 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $253.09M | leva aperta stimata in dollari |
| Open Interest 24h | -27.71% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 2.60 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $62.61 | $93.91 |
| 10x | $70.43 | $86.09 |
| 20x | $74.35 | $82.17 |
| 50x | $76.69 | $79.83 |

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
| Prezzo | $0.07314 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +0.87% | movimento dell'ultimo giorno |
| Funding | +0.0023% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-10 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $70.08M | leva aperta stimata in dollari |
| Open Interest 24h | -1.91% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 3.05 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $0.05851 | $0.08777 |
| 10x | $0.06583 | $0.08045 |
| 20x | $0.06948 | $0.07680 |
| 50x | $0.07168 | $0.07460 |

### Note tecniche usate dallo score

- long/short ratio alto: più mercato sbilanciato long

---
