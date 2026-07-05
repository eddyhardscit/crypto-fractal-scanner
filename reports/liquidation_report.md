# Report semplice futures / liquidazioni BTC / SOL / DOGE

Generato: **2026-07-05 14:45:28 CEST**  
UTC: **2026-07-05 12:45:28 UTC**

Fonte dati: **OKX Futures pubblici**.  
Questo report non è la vera heatmap CoinGlass. Serve a capire se il mercato futures è carico di long, short o leva.

## Traduzione in parole semplici

| Asset | Lettura | Forza | Cosa significa in pratica |
| --- | --- | --- | --- |
| BTC | Rischio sotto | 5/5 | Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale. |
| SOL | Misto | 1/5 | Qui pesa di più il report frattale. |
| DOGE | Leva alta, direzione mista | 3/5 | Meglio non forzare. Aspetta conferma dal frattale o dal prezzo. |

## Numeri principali

| Asset | Prezzo | Prezzo 24h | Funding | Open Interest | OI 24h | Long/Short |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | $62,676 | +0.12% | +0.0037% | $1.94B | +15.31% | 1.76 |
| SOL | $80.75 | -0.87% | +0.0030% | $273.93M | -21.36% | 3.20 |
| DOGE | $0.07627 | -0.92% | +0.0034% | $72.65M | +6.32% | 3.84 |

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
| Prezzo | $62,676 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +0.12% | movimento dell'ultimo giorno |
| Funding | +0.0037% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-05 18:00 | prossimo aggiornamento funding |
| Open Interest stimato | $1.94B | leva aperta stimata in dollari |
| Open Interest 24h | +15.31% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.76 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $50,141 | $75,211 |
| 10x | $56,408 | $68,943 |
| 20x | $59,542 | $65,809 |
| 50x | $61,422 | $63,929 |

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
| Prezzo | $80.75 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -0.87% | movimento dell'ultimo giorno |
| Funding | +0.0030% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-05 18:00 | prossimo aggiornamento funding |
| Open Interest stimato | $273.93M | leva aperta stimata in dollari |
| Open Interest 24h | -21.36% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 3.20 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $64.60 | $96.90 |
| 10x | $72.67 | $88.83 |
| 20x | $76.71 | $84.79 |
| 50x | $79.14 | $82.36 |

### Note tecniche usate dallo score

- open interest in forte calo: parte della leva è già uscita
- long/short ratio alto: più mercato sbilanciato long

---

## Dogecoin — DOGE

### Lettura semplice

**MOLTA LEVA MA DIREZIONE MISTA**  
**Forza segnale: 3/5**

DOGE: c'è molta leva nel mercato, ma la direzione non è pulita. Può arrivare un movimento violento, ma non è chiaro se sopra o sotto.

**Tradotto operativamente:** Meglio non forzare. Aspetta conferma dal frattale o dal prezzo.

### Perché

- funding positivo: i long pagano gli short
- open interest in aumento: più leva nel sistema
- long/short ratio alto: mercato più long

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $0.07627 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -0.92% | movimento dell'ultimo giorno |
| Funding | +0.0034% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-05 18:00 | prossimo aggiornamento funding |
| Open Interest stimato | $72.65M | leva aperta stimata in dollari |
| Open Interest 24h | +6.32% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 3.84 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $0.06102 | $0.09152 |
| 10x | $0.06864 | $0.08390 |
| 20x | $0.07246 | $0.08008 |
| 50x | $0.07474 | $0.07780 |

### Note tecniche usate dallo score

- open interest in forte aumento: entra molta leva
- long/short ratio alto: più mercato sbilanciato long

---
