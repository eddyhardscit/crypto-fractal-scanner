# Report semplice futures / liquidazioni BTC / SOL / DOGE

Generato: **2026-07-04 22:39:44 CEST**  
UTC: **2026-07-04 20:39:44 UTC**

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
| BTC | $63,225 | +0.91% | +0.0077% | $1.93B | +18.96% | 1.77 |
| SOL | $81.90 | -0.81% | +0.0028% | $272.95M | -20.45% | 3.28 |
| DOGE | $0.07805 | +0.41% | +0.0068% | $75.00M | +8.22% | 3.92 |

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
| Prezzo | $63,225 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +0.91% | movimento dell'ultimo giorno |
| Funding | +0.0077% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-05 02:00 | prossimo aggiornamento funding |
| Open Interest stimato | $1.93B | leva aperta stimata in dollari |
| Open Interest 24h | +18.96% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.77 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $50,580 | $75,870 |
| 10x | $56,903 | $69,548 |
| 20x | $60,064 | $66,386 |
| 50x | $61,961 | $64,490 |

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
| Prezzo | $81.90 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -0.81% | movimento dell'ultimo giorno |
| Funding | +0.0028% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-05 02:00 | prossimo aggiornamento funding |
| Open Interest stimato | $272.95M | leva aperta stimata in dollari |
| Open Interest 24h | -20.45% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 3.28 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $65.52 | $98.28 |
| 10x | $73.71 | $90.09 |
| 20x | $77.81 | $86.00 |
| 50x | $80.26 | $83.54 |

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
| Prezzo | $0.07805 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +0.41% | movimento dell'ultimo giorno |
| Funding | +0.0068% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-05 02:00 | prossimo aggiornamento funding |
| Open Interest stimato | $75.00M | leva aperta stimata in dollari |
| Open Interest 24h | +8.22% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 3.92 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $0.06244 | $0.09366 |
| 10x | $0.07025 | $0.08586 |
| 20x | $0.07415 | $0.08195 |
| 50x | $0.07649 | $0.07961 |

### Note tecniche usate dallo score

- open interest in forte aumento: entra molta leva
- prezzo su + leva su + funding positivo: rischio pulizia dei long sotto
- long/short ratio alto: più mercato sbilanciato long

---
