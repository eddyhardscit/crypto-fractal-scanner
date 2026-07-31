# Report semplice futures / liquidazioni BTC / SOL / DOGE

Generato: **2026-07-31 07:14:54 CEST**  
UTC: **2026-07-31 05:14:54 UTC**

Fonte dati: **OKX Futures pubblici**.  
Questo report non è la vera heatmap CoinGlass. Serve a capire se il mercato futures è carico di long, short o leva.

## Traduzione in parole semplici

| Asset | Lettura | Forza | Cosa significa in pratica |
| --- | --- | --- | --- |
| BTC | Rischio sotto | 5/5 | Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale. |
| SOL | Rischio sotto | 5/5 | Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale. |
| DOGE | Misto | 1/5 | Qui pesa di più il report frattale. |

## Numeri principali

| Asset | Prezzo | Prezzo 24h | Funding | Open Interest | OI 24h | Long/Short |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 64.330 $ | +0.67% | +0.0100% | $1.96B | +3.03% | 2.27 |
| SOL | 74,00 $ | +0.79% | +0.0072% | $206.87M | +13.86% | 1.79 |
| DOGE | 0.07005 $ | +0.55% | +0.0081% | $86.51M | -23.35% | 3.10 |

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
| Prezzo | $64,385 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +0.67% | movimento dell'ultimo giorno |
| Funding | +0.0100% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-31 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $1.96B | leva aperta stimata in dollari |
| Open Interest 24h | +3.03% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 2.27 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $51,508 | $77,262 |
| 10x | $57,946 | $70,824 |
| 20x | $61,166 | $67,604 |
| 50x | $63,097 | $65,673 |

### Note tecniche usate dallo score

- funding positivo: mercato leggermente carico di long
- open interest in aumento: leva in crescita
- prezzo su + leva su + funding positivo: rischio pulizia dei long sotto
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
| Prezzo | $74.06 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +0.79% | movimento dell'ultimo giorno |
| Funding | +0.0072% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-31 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $206.87M | leva aperta stimata in dollari |
| Open Interest 24h | +13.86% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.79 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $59.25 | $88.87 |
| 10x | $66.65 | $81.47 |
| 20x | $70.36 | $77.76 |
| 50x | $72.58 | $75.54 |

### Note tecniche usate dallo score

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
| Prezzo | $0.07006 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +0.55% | movimento dell'ultimo giorno |
| Funding | +0.0081% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-31 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $86.51M | leva aperta stimata in dollari |
| Open Interest 24h | -23.35% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 3.10 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $0.05605 | $0.08407 |
| 10x | $0.06305 | $0.07707 |
| 20x | $0.06656 | $0.07356 |
| 50x | $0.06866 | $0.07146 |

### Note tecniche usate dallo score

- open interest in forte calo: parte della leva è già uscita
- long/short ratio alto: più mercato sbilanciato long

---
