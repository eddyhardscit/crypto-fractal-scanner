# Report semplice futures / liquidazioni BTC / SOL / DOGE

Generato: **2026-07-08 11:39:59 CEST**  
UTC: **2026-07-08 09:39:59 UTC**

Fonte dati: **OKX Futures pubblici**.  
Questo report non è la vera heatmap CoinGlass. Serve a capire se il mercato futures è carico di long, short o leva.

## Traduzione in parole semplici

| Asset | Lettura | Forza | Cosa significa in pratica |
| --- | --- | --- | --- |
| BTC | Misto | 1/5 | Qui pesa di più il report frattale. |
| SOL | Rischio sotto | 2/5 | Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale. |
| DOGE | Misto | 1/5 | Qui pesa di più il report frattale. |

## Numeri principali

| Asset | Prezzo | Prezzo 24h | Funding | Open Interest | OI 24h | Long/Short |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | $62,078 | -1.76% | +0.0021% | $1.91B | -8.00% | 1.66 |
| SOL | $77.26 | -4.82% | +0.0100% | $249.14M | -29.13% | 2.78 |
| DOGE | $0.07140 | -4.56% | +0.0071% | $69.79M | -1.21% | 3.28 |

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
- open interest in calo: leva in uscita
- long/short ratio alto: mercato più long

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $62,078 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -1.76% | movimento dell'ultimo giorno |
| Funding | +0.0021% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-08 18:00 | prossimo aggiornamento funding |
| Open Interest stimato | $1.91B | leva aperta stimata in dollari |
| Open Interest 24h | -8.00% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.66 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $49,662 | $74,493 |
| 10x | $55,870 | $68,285 |
| 20x | $58,974 | $65,182 |
| 50x | $60,836 | $63,319 |

### Note tecniche usate dallo score

- open interest in forte calo: parte della leva è già uscita
- long/short ratio alto: più mercato sbilanciato long

---

## Solana — SOL

### Lettura semplice

**RISCHIO DISCESA / FLUSH SOTTO**  
**Forza segnale: 2/5**

SOL: i futures sembrano più vulnerabili verso una discesa improvvisa. Non significa che deve scendere, ma se rompe sotto può accelerare.

**Tradotto operativamente:** Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale.

### Perché

- funding positivo: i long pagano gli short
- open interest in calo: leva in uscita
- long/short ratio alto: mercato più long

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $77.26 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -4.82% | movimento dell'ultimo giorno |
| Funding | +0.0100% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-08 18:00 | prossimo aggiornamento funding |
| Open Interest stimato | $249.14M | leva aperta stimata in dollari |
| Open Interest 24h | -29.13% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 2.78 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $61.81 | $92.71 |
| 10x | $69.53 | $84.99 |
| 20x | $73.40 | $81.12 |
| 50x | $75.71 | $78.81 |

### Note tecniche usate dallo score

- funding positivo: mercato leggermente carico di long
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
| Prezzo | $0.07140 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -4.56% | movimento dell'ultimo giorno |
| Funding | +0.0071% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-08 18:00 | prossimo aggiornamento funding |
| Open Interest stimato | $69.79M | leva aperta stimata in dollari |
| Open Interest 24h | -1.21% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 3.28 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $0.05712 | $0.08568 |
| 10x | $0.06426 | $0.07854 |
| 20x | $0.06783 | $0.07497 |
| 50x | $0.06997 | $0.07283 |

### Note tecniche usate dallo score

- long/short ratio alto: più mercato sbilanciato long

---
