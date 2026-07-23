# Report semplice futures / liquidazioni BTC / SOL / DOGE

Generato: **2026-07-23 09:37:51 CEST**  
UTC: **2026-07-23 07:37:51 UTC**

Fonte dati: **OKX Futures pubblici**.  
Questo report non è la vera heatmap CoinGlass. Serve a capire se il mercato futures è carico di long, short o leva.

## Traduzione in parole semplici

| Asset | Lettura | Forza | Cosa significa in pratica |
| --- | --- | --- | --- |
| BTC | Misto | 2/5 | Qui pesa di più il report frattale. |
| SOL | Misto | 1/5 | Qui pesa di più il report frattale. |
| DOGE | Misto | 1/5 | Qui pesa di più il report frattale. |

## Numeri principali

| Asset | Prezzo | Prezzo 24h | Funding | Open Interest | OI 24h | Long/Short |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 65.400 $ | -0.51% | -0.0031% | $2.01B | +3.34% | 1.75 |
| SOL | 77,11 $ | +0.16% | -0.0026% | $224.35M | -9.12% | 2.43 |
| DOGE | 0.07226 $ | +0.14% | +0.0075% | $80.27M | -4.58% | 4.69 |

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

- funding negativo: gli short pagano i long
- open interest in aumento: più leva nel sistema
- long/short ratio alto: mercato più long

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $65,404 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -0.51% | movimento dell'ultimo giorno |
| Funding | -0.0031% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-23 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $2.01B | leva aperta stimata in dollari |
| Open Interest 24h | +3.34% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.75 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $52,324 | $78,485 |
| 10x | $58,864 | $71,945 |
| 20x | $62,134 | $68,675 |
| 50x | $64,096 | $66,713 |

### Note tecniche usate dallo score

- open interest in aumento: leva in crescita
- prezzo giù + leva su + funding negativo: rischio short squeeze sopra
- long/short ratio alto: più mercato sbilanciato long

---

## Solana — SOL

### Lettura semplice

**NEUTRALE / POCO CHIARO**  
**Forza segnale: 1/5**

SOL: i futures non danno una lettura chiara. Non si vede uno sbilanciamento forte né long né short.

**Tradotto operativamente:** Qui pesa di più il report frattale.

### Perché

- funding negativo: gli short pagano i long
- open interest in calo: leva in uscita
- long/short ratio alto: mercato più long

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $77.11 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +0.16% | movimento dell'ultimo giorno |
| Funding | -0.0026% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-23 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $224.35M | leva aperta stimata in dollari |
| Open Interest 24h | -9.12% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 2.43 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $61.69 | $92.53 |
| 10x | $69.40 | $84.82 |
| 20x | $73.25 | $80.97 |
| 50x | $75.57 | $78.65 |

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
| Prezzo | $0.07226 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +0.14% | movimento dell'ultimo giorno |
| Funding | +0.0075% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-23 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $80.27M | leva aperta stimata in dollari |
| Open Interest 24h | -4.58% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 4.69 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $0.05781 | $0.08671 |
| 10x | $0.06503 | $0.07949 |
| 20x | $0.06865 | $0.07587 |
| 50x | $0.07081 | $0.07371 |

### Note tecniche usate dallo score

- long/short ratio alto: più mercato sbilanciato long

---
