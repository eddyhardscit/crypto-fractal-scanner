# Report semplice futures / liquidazioni BTC / SOL / DOGE

Generato: **2026-07-08 10:39:58 CEST**  
UTC: **2026-07-08 08:39:58 UTC**

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
| BTC | $61,945 | -1.79% | +0.0032% | $1.89B | -7.85% | 1.68 |
| SOL | $76.94 | -5.46% | +0.0100% | $247.65M | -29.29% | 2.78 |
| DOGE | $0.07111 | -4.97% | +0.0065% | $68.87M | -1.59% | 3.29 |

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
| Prezzo | $61,945 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -1.79% | movimento dell'ultimo giorno |
| Funding | +0.0032% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-08 18:00 | prossimo aggiornamento funding |
| Open Interest stimato | $1.89B | leva aperta stimata in dollari |
| Open Interest 24h | -7.85% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.68 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $49,556 | $74,334 |
| 10x | $55,750 | $68,139 |
| 20x | $58,848 | $65,042 |
| 50x | $60,706 | $63,184 |

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
| Prezzo | $76.94 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -5.46% | movimento dell'ultimo giorno |
| Funding | +0.0100% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-08 18:00 | prossimo aggiornamento funding |
| Open Interest stimato | $247.65M | leva aperta stimata in dollari |
| Open Interest 24h | -29.29% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 2.78 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $61.55 | $92.33 |
| 10x | $69.25 | $84.63 |
| 20x | $73.09 | $80.79 |
| 50x | $75.40 | $78.48 |

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
| Prezzo | $0.07111 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -4.97% | movimento dell'ultimo giorno |
| Funding | +0.0065% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-08 18:00 | prossimo aggiornamento funding |
| Open Interest stimato | $68.87M | leva aperta stimata in dollari |
| Open Interest 24h | -1.59% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 3.29 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $0.05689 | $0.08533 |
| 10x | $0.06400 | $0.07822 |
| 20x | $0.06755 | $0.07467 |
| 50x | $0.06969 | $0.07253 |

### Note tecniche usate dallo score

- long/short ratio alto: più mercato sbilanciato long

---
