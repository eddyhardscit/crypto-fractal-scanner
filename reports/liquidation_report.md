# Report semplice futures / liquidazioni BTC / SOL / DOGE

Generato: **2026-07-09 20:20:47 CEST**  
UTC: **2026-07-09 18:20:47 UTC**

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
| BTC | $63,252 | +1.62% | +0.0053% | $1.88B | +3.59% | 2.13 |
| SOL | $78.21 | +1.39% | +0.0094% | $257.43M | -28.94% | 2.70 |
| DOGE | $0.07323 | +0.78% | +0.0015% | $71.20M | -4.15% | 3.34 |

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
| Prezzo | $63,252 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +1.62% | movimento dell'ultimo giorno |
| Funding | +0.0053% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-10 02:00 | prossimo aggiornamento funding |
| Open Interest stimato | $1.88B | leva aperta stimata in dollari |
| Open Interest 24h | +3.59% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 2.13 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $50,601 | $75,902 |
| 10x | $56,926 | $69,577 |
| 20x | $60,089 | $66,414 |
| 50x | $61,986 | $64,517 |

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
| Prezzo | $78.21 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +1.39% | movimento dell'ultimo giorno |
| Funding | +0.0094% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-10 02:00 | prossimo aggiornamento funding |
| Open Interest stimato | $257.43M | leva aperta stimata in dollari |
| Open Interest 24h | -28.94% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 2.70 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $62.57 | $93.85 |
| 10x | $70.39 | $86.03 |
| 20x | $74.30 | $82.12 |
| 50x | $76.65 | $79.77 |

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
| Prezzo | $0.07323 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +0.78% | movimento dell'ultimo giorno |
| Funding | +0.0015% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-10 02:00 | prossimo aggiornamento funding |
| Open Interest stimato | $71.20M | leva aperta stimata in dollari |
| Open Interest 24h | -4.15% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 3.34 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $0.05858 | $0.08788 |
| 10x | $0.06591 | $0.08055 |
| 20x | $0.06957 | $0.07689 |
| 50x | $0.07177 | $0.07469 |

### Note tecniche usate dallo score

- long/short ratio alto: più mercato sbilanciato long

---
