# Report semplice futures / liquidazioni BTC / SOL / DOGE

Generato: **2026-07-07 02:54:47 CEST**  
UTC: **2026-07-07 00:54:47 UTC**

Fonte dati: **OKX Futures pubblici**.  
Questo report non è la vera heatmap CoinGlass. Serve a capire se il mercato futures è carico di long, short o leva.

## Traduzione in parole semplici

| Asset | Lettura | Forza | Cosa significa in pratica |
| --- | --- | --- | --- |
| BTC | Rischio sotto | 5/5 | Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale. |
| SOL | Misto | 1/5 | Qui pesa di più il report frattale. |
| DOGE | Rischio sotto | 4/5 | Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale. |

## Numeri principali

| Asset | Prezzo | Prezzo 24h | Funding | Open Interest | OI 24h | Long/Short |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | $64,222 | +0.96% | +0.0100% | $1.93B | +4.49% | 1.75 |
| SOL | $82.33 | +0.39% | +0.0058% | $261.06M | -28.25% | 2.79 |
| DOGE | $0.07684 | -1.17% | +0.0100% | $65.22M | +11.68% | 3.13 |

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
| Prezzo | $64,222 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +0.96% | movimento dell'ultimo giorno |
| Funding | +0.0100% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-07 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $1.93B | leva aperta stimata in dollari |
| Open Interest 24h | +4.49% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.75 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $51,377 | $77,066 |
| 10x | $57,800 | $70,644 |
| 20x | $61,011 | $67,433 |
| 50x | $62,937 | $65,506 |

### Note tecniche usate dallo score

- funding positivo: mercato leggermente carico di long
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
| Prezzo | $82.33 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +0.39% | movimento dell'ultimo giorno |
| Funding | +0.0058% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-07 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $261.06M | leva aperta stimata in dollari |
| Open Interest 24h | -28.25% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 2.79 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $65.86 | $98.80 |
| 10x | $74.10 | $90.56 |
| 20x | $78.21 | $86.45 |
| 50x | $80.68 | $83.98 |

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
| Prezzo | $0.07684 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -1.17% | movimento dell'ultimo giorno |
| Funding | +0.0100% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-07 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $65.22M | leva aperta stimata in dollari |
| Open Interest 24h | +11.68% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 3.13 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $0.06147 | $0.09221 |
| 10x | $0.06916 | $0.08452 |
| 20x | $0.07300 | $0.08068 |
| 50x | $0.07530 | $0.07838 |

### Note tecniche usate dallo score

- funding positivo: mercato leggermente carico di long
- open interest in forte aumento: entra molta leva
- long/short ratio alto: più mercato sbilanciato long

---
