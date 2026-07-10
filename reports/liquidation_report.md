# Report semplice futures / liquidazioni BTC / SOL / DOGE

Generato: **2026-07-10 14:52:13 CEST**  
UTC: **2026-07-10 12:52:13 UTC**

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
| BTC | $64,316 | +2.73% | +0.0042% | $2.00B | -0.38% | 1.94 |
| SOL | $78.96 | +1.70% | +0.0012% | $242.89M | -21.95% | 2.67 |
| DOGE | $0.07404 | +2.44% | +0.0100% | $70.25M | -1.57% | 3.08 |

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
| Prezzo | $64,316 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +2.73% | movimento dell'ultimo giorno |
| Funding | +0.0042% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-10 18:00 | prossimo aggiornamento funding |
| Open Interest stimato | $2.00B | leva aperta stimata in dollari |
| Open Interest 24h | -0.38% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.94 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $51,453 | $77,180 |
| 10x | $57,885 | $70,748 |
| 20x | $61,101 | $67,532 |
| 50x | $63,030 | $65,603 |

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
| Prezzo | $78.96 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +1.70% | movimento dell'ultimo giorno |
| Funding | +0.0012% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-10 18:00 | prossimo aggiornamento funding |
| Open Interest stimato | $242.89M | leva aperta stimata in dollari |
| Open Interest 24h | -21.95% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 2.67 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $63.17 | $94.75 |
| 10x | $71.06 | $86.86 |
| 20x | $75.01 | $82.91 |
| 50x | $77.38 | $80.54 |

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
| Prezzo | $0.07404 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +2.44% | movimento dell'ultimo giorno |
| Funding | +0.0100% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-10 18:00 | prossimo aggiornamento funding |
| Open Interest stimato | $70.25M | leva aperta stimata in dollari |
| Open Interest 24h | -1.57% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 3.08 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $0.05923 | $0.08885 |
| 10x | $0.06664 | $0.08144 |
| 20x | $0.07034 | $0.07774 |
| 50x | $0.07256 | $0.07552 |

### Note tecniche usate dallo score

- funding positivo: mercato leggermente carico di long
- long/short ratio alto: più mercato sbilanciato long

---
