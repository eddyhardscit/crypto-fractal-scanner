# Report semplice futures / liquidazioni BTC / SOL / DOGE

Generato: **2026-07-10 14:10:20 CEST**  
UTC: **2026-07-10 12:10:20 UTC**

Fonte dati: **OKX Futures pubblici**.  
Questo report non è la vera heatmap CoinGlass. Serve a capire se il mercato futures è carico di long, short o leva.

## Traduzione in parole semplici

| Asset | Lettura | Forza | Cosa significa in pratica |
| --- | --- | --- | --- |
| BTC | Misto | 1/5 | Qui pesa di più il report frattale. |
| SOL | Misto | 1/5 | Qui pesa di più il report frattale. |
| DOGE | Rischio sotto | 2/5 | Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale. |

## Numeri principali

| Asset | Prezzo | Prezzo 24h | Funding | Open Interest | OI 24h | Long/Short |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | $64,380 | +2.50% | +0.0057% | $2.01B | -0.38% | 1.94 |
| SOL | $79.23 | +2.05% | +0.0015% | $244.99M | -21.95% | 2.67 |
| DOGE | $0.07420 | +2.44% | +0.0100% | $70.12M | -1.57% | 3.08 |

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
**Forza segnale: 1/5**

BTC: i futures non danno una lettura chiara. Non si vede uno sbilanciamento forte né long né short.

**Tradotto operativamente:** Qui pesa di più il report frattale.

### Perché

- funding positivo: i long pagano gli short
- open interest abbastanza stabile
- long/short ratio alto: mercato più long

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $64,380 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +2.50% | movimento dell'ultimo giorno |
| Funding | +0.0057% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-10 18:00 | prossimo aggiornamento funding |
| Open Interest stimato | $2.01B | leva aperta stimata in dollari |
| Open Interest 24h | -0.38% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.94 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $51,504 | $77,256 |
| 10x | $57,942 | $70,818 |
| 20x | $61,161 | $67,599 |
| 50x | $63,093 | $65,668 |

### Note tecniche usate dallo score

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
| Prezzo | $79.23 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +2.05% | movimento dell'ultimo giorno |
| Funding | +0.0015% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-10 18:00 | prossimo aggiornamento funding |
| Open Interest stimato | $244.99M | leva aperta stimata in dollari |
| Open Interest 24h | -21.95% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 2.67 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $63.38 | $95.08 |
| 10x | $71.31 | $87.15 |
| 20x | $75.27 | $83.19 |
| 50x | $77.65 | $80.81 |

### Note tecniche usate dallo score

- open interest in forte calo: parte della leva è già uscita
- long/short ratio alto: più mercato sbilanciato long

---

## Dogecoin — DOGE

### Lettura semplice

**RISCHIO DISCESA / FLUSH SOTTO**  
**Forza segnale: 2/5**

DOGE: i futures sembrano più vulnerabili verso una discesa improvvisa. Non significa che deve scendere, ma se rompe sotto può accelerare.

**Tradotto operativamente:** Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale.

### Perché

- funding positivo: i long pagano gli short
- open interest abbastanza stabile
- long/short ratio alto: mercato più long

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $0.07420 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +2.44% | movimento dell'ultimo giorno |
| Funding | +0.0100% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-10 18:00 | prossimo aggiornamento funding |
| Open Interest stimato | $70.12M | leva aperta stimata in dollari |
| Open Interest 24h | -1.57% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 3.08 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $0.05936 | $0.08904 |
| 10x | $0.06678 | $0.08162 |
| 20x | $0.07049 | $0.07791 |
| 50x | $0.07272 | $0.07568 |

### Note tecniche usate dallo score

- funding positivo: mercato leggermente carico di long
- long/short ratio alto: più mercato sbilanciato long

---
