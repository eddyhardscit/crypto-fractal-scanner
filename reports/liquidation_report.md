# Report semplice futures / liquidazioni BTC / SOL / DOGE

Generato: **2026-07-04 22:28:11 CEST**  
UTC: **2026-07-04 20:28:11 UTC**

Fonte dati: **OKX Futures pubblici**.  
Questo report non è la vera heatmap CoinGlass. Serve a capire se il mercato futures è carico di long, short o leva.

## Traduzione in parole semplici

| Asset | Lettura | Forza | Cosa significa in pratica |
| --- | --- | --- | --- |
| BTC | Rischio sotto | 5/5 | Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale. |
| SOL | Misto | 1/5 | Qui pesa di più il report frattale. |
| DOGE | Rischio sotto | 5/5 | Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale. |

## Numeri principali

| Asset | Prezzo | Prezzo 24h | Funding | Open Interest | OI 24h | Long/Short |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | $63,155 | +0.92% | +0.0075% | $1.93B | +18.96% | 1.77 |
| SOL | $81.59 | -1.11% | +0.0029% | $271.91M | -20.45% | 3.28 |
| DOGE | $0.07800 | +0.26% | +0.0064% | $74.96M | +8.22% | 3.92 |

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
| Prezzo | $63,155 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +0.92% | movimento dell'ultimo giorno |
| Funding | +0.0075% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-05 02:00 | prossimo aggiornamento funding |
| Open Interest stimato | $1.93B | leva aperta stimata in dollari |
| Open Interest 24h | +18.96% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.77 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $50,524 | $75,786 |
| 10x | $56,840 | $69,471 |
| 20x | $59,997 | $66,313 |
| 50x | $61,892 | $64,418 |

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
| Prezzo | $81.59 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -1.11% | movimento dell'ultimo giorno |
| Funding | +0.0029% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-05 02:00 | prossimo aggiornamento funding |
| Open Interest stimato | $271.91M | leva aperta stimata in dollari |
| Open Interest 24h | -20.45% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 3.28 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $65.27 | $97.91 |
| 10x | $73.43 | $89.75 |
| 20x | $77.51 | $85.67 |
| 50x | $79.96 | $83.22 |

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
| Prezzo | $0.07800 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +0.26% | movimento dell'ultimo giorno |
| Funding | +0.0064% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-05 02:00 | prossimo aggiornamento funding |
| Open Interest stimato | $74.96M | leva aperta stimata in dollari |
| Open Interest 24h | +8.22% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 3.92 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $0.06240 | $0.09360 |
| 10x | $0.07020 | $0.08580 |
| 20x | $0.07410 | $0.08190 |
| 50x | $0.07644 | $0.07956 |

### Note tecniche usate dallo score

- open interest in forte aumento: entra molta leva
- prezzo su + leva su + funding positivo: rischio pulizia dei long sotto
- long/short ratio alto: più mercato sbilanciato long

---
