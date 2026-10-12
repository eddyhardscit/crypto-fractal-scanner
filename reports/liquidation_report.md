# Report semplice futures / liquidazioni BTC / SOL / DOGE

Generato: **2026-10-12 07:33:20 CEST**  
UTC: **2026-10-12 05:33:20 UTC**

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
| BTC | 83.863 $ | +0.96% | -0.0002% | $2.47B | -13.94% | 1.64 |
| SOL | 112,60 $ | +2.66% | +0.0100% | $338.91M | -17.88% | 2.11 |
| DOGE | 0.08754 $ | +2.41% | -0.0013% | $95.62M | -9.13% | 4.34 |

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

- funding negativo: gli short pagano i long
- open interest in calo: leva in uscita
- long/short ratio alto: mercato più long

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $83,849 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +0.96% | movimento dell'ultimo giorno |
| Funding | -0.0002% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-10-12 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $2.47B | leva aperta stimata in dollari |
| Open Interest 24h | -13.94% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.64 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $67,079 | $100,619 |
| 10x | $75,464 | $92,234 |
| 20x | $79,657 | $88,042 |
| 50x | $82,172 | $85,526 |

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
| Prezzo | $112.54 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +2.66% | movimento dell'ultimo giorno |
| Funding | +0.0100% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-10-12 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $338.91M | leva aperta stimata in dollari |
| Open Interest 24h | -17.88% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 2.11 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $90.03 | $135.05 |
| 10x | $101.29 | $123.79 |
| 20x | $106.91 | $118.17 |
| 50x | $110.29 | $114.79 |

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

- funding negativo: gli short pagano i long
- open interest in calo: leva in uscita
- long/short ratio alto: mercato più long

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $0.08748 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +2.41% | movimento dell'ultimo giorno |
| Funding | -0.0013% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-10-12 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $95.62M | leva aperta stimata in dollari |
| Open Interest 24h | -9.13% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 4.34 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $0.06998 | $0.10498 |
| 10x | $0.07873 | $0.09623 |
| 20x | $0.08311 | $0.09185 |
| 50x | $0.08573 | $0.08923 |

### Note tecniche usate dallo score

- open interest in forte calo: parte della leva è già uscita
- long/short ratio alto: più mercato sbilanciato long

---
