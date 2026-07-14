# Report semplice futures / liquidazioni BTC / SOL / DOGE

Generato: **2026-07-14 09:23:01 CEST**  
UTC: **2026-07-14 07:23:01 UTC**

Fonte dati: **OKX Futures pubblici**.  
Questo report non è la vera heatmap CoinGlass. Serve a capire se il mercato futures è carico di long, short o leva.

## Traduzione in parole semplici

| Asset | Lettura | Forza | Cosa significa in pratica |
| --- | --- | --- | --- |
| BTC | Leva alta, direzione mista | 3/5 | Meglio non forzare. Aspetta conferma dal frattale o dal prezzo. |
| SOL | Misto | 1/5 | Qui pesa di più il report frattale. |
| DOGE | Leva alta, direzione mista | 3/5 | Meglio non forzare. Aspetta conferma dal frattale o dal prezzo. |

## Numeri principali

| Asset | Prezzo | Prezzo 24h | Funding | Open Interest | OI 24h | Long/Short |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 62.239 $ | -0.42% | +0.0021% | $1.98B | +5.97% | 1.35 |
| SOL | 74,86 $ | -1.90% | +0.0042% | $227.92M | -20.93% | 2.31 |
| DOGE | 0.07185 $ | -0.19% | +0.0049% | $68.01M | +16.15% | 3.86 |

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

**MOLTA LEVA MA DIREZIONE MISTA**  
**Forza segnale: 3/5**

BTC: c'è molta leva nel mercato, ma la direzione non è pulita. Può arrivare un movimento violento, ma non è chiaro se sopra o sotto.

**Tradotto operativamente:** Meglio non forzare. Aspetta conferma dal frattale o dal prezzo.

### Perché

- funding positivo: i long pagano gli short
- open interest in aumento: più leva nel sistema
- long/short ratio alto: mercato più long

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $62,559 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -0.42% | movimento dell'ultimo giorno |
| Funding | +0.0021% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-14 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $1.98B | leva aperta stimata in dollari |
| Open Interest 24h | +5.97% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.35 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $50,047 | $75,071 |
| 10x | $56,303 | $68,815 |
| 20x | $59,431 | $65,687 |
| 50x | $61,308 | $63,810 |

### Note tecniche usate dallo score

- open interest in forte aumento: entra molta leva
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
| Prezzo | $75.00 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -1.90% | movimento dell'ultimo giorno |
| Funding | +0.0042% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-14 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $227.92M | leva aperta stimata in dollari |
| Open Interest 24h | -20.93% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 2.31 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $60.00 | $90.00 |
| 10x | $67.50 | $82.50 |
| 20x | $71.25 | $78.75 |
| 50x | $73.50 | $76.50 |

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
| Prezzo | $0.07218 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -0.19% | movimento dell'ultimo giorno |
| Funding | +0.0049% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-14 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $68.01M | leva aperta stimata in dollari |
| Open Interest 24h | +16.15% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 3.86 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $0.05774 | $0.08662 |
| 10x | $0.06496 | $0.07940 |
| 20x | $0.06857 | $0.07579 |
| 50x | $0.07074 | $0.07362 |

### Note tecniche usate dallo score

- open interest in forte aumento: entra molta leva
- long/short ratio alto: più mercato sbilanciato long

---
