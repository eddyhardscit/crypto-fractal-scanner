# Report semplice futures / liquidazioni BTC / SOL / DOGE

Generato: **2026-07-17 09:32:52 CEST**  
UTC: **2026-07-17 07:32:52 UTC**

Fonte dati: **OKX Futures pubblici**.  
Questo report non è la vera heatmap CoinGlass. Serve a capire se il mercato futures è carico di long, short o leva.

## Traduzione in parole semplici

| Asset | Lettura | Forza | Cosa significa in pratica |
| --- | --- | --- | --- |
| BTC | Misto | 2/5 | Qui pesa di più il report frattale. |
| SOL | Misto | 1/5 | Qui pesa di più il report frattale. |
| DOGE | Leva alta, direzione mista | 3/5 | Meglio non forzare. Aspetta conferma dal frattale o dal prezzo. |

## Numeri principali

| Asset | Prezzo | Prezzo 24h | Funding | Open Interest | OI 24h | Long/Short |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 62.871 $ | -2.29% | +0.0040% | $1.97B | +3.47% | 1.40 |
| SOL | 74,46 $ | -2.89% | +0.0065% | $221.06M | -14.85% | 2.23 |
| DOGE | 0.07165 $ | -2.78% | +0.0022% | $70.09M | +7.76% | 4.24 |

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
**Forza segnale: 2/5**

BTC: i futures non danno una lettura chiara. Non si vede uno sbilanciamento forte né long né short.

**Tradotto operativamente:** Qui pesa di più il report frattale.

### Perché

- funding positivo: i long pagano gli short
- open interest in aumento: più leva nel sistema
- long/short ratio alto: mercato più long

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $62,953 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -2.29% | movimento dell'ultimo giorno |
| Funding | +0.0040% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-17 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $1.97B | leva aperta stimata in dollari |
| Open Interest 24h | +3.47% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.40 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $50,362 | $75,543 |
| 10x | $56,658 | $69,248 |
| 20x | $59,805 | $66,100 |
| 50x | $61,694 | $64,212 |

### Note tecniche usate dallo score

- open interest in aumento: leva in crescita
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
| Prezzo | $74.61 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -2.89% | movimento dell'ultimo giorno |
| Funding | +0.0065% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-17 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $221.06M | leva aperta stimata in dollari |
| Open Interest 24h | -14.85% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 2.23 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $59.69 | $89.53 |
| 10x | $67.15 | $82.07 |
| 20x | $70.88 | $78.34 |
| 50x | $73.12 | $76.10 |

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
| Prezzo | $0.07175 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -2.78% | movimento dell'ultimo giorno |
| Funding | +0.0022% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-17 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $70.09M | leva aperta stimata in dollari |
| Open Interest 24h | +7.76% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 4.24 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $0.05740 | $0.08610 |
| 10x | $0.06457 | $0.07892 |
| 20x | $0.06816 | $0.07534 |
| 50x | $0.07031 | $0.07319 |

### Note tecniche usate dallo score

- open interest in forte aumento: entra molta leva
- long/short ratio alto: più mercato sbilanciato long

---
