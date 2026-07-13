# Report semplice futures / liquidazioni BTC / SOL / DOGE

Generato: **2026-07-13 08:28:30 CEST**  
UTC: **2026-07-13 06:28:30 UTC**

Fonte dati: **OKX Futures pubblici**.  
Questo report non è la vera heatmap CoinGlass. Serve a capire se il mercato futures è carico di long, short o leva.

## Traduzione in parole semplici

| Asset | Lettura | Forza | Cosa significa in pratica |
| --- | --- | --- | --- |
| BTC | Misto | 1/5 | Qui pesa di più il report frattale. |
| SOL | Misto | 1/5 | Qui pesa di più il report frattale. |
| DOGE | Leva alta, direzione mista | 3/5 | Meglio non forzare. Aspetta conferma dal frattale o dal prezzo. |

## Numeri principali

| Asset | Prezzo | Prezzo 24h | Funding | Open Interest | OI 24h | Long/Short |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 62.682 $ | -1.38% | +0.0029% | $1.97B | +1.10% | 1.53 |
| SOL | 76,29 $ | +0.63% | -0.0016% | $233.69M | -23.85% | 2.64 |
| DOGE | 0.07214 $ | -0.62% | +0.0046% | $67.14M | +17.25% | 4.12 |

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
| Prezzo | $62,775 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -1.38% | movimento dell'ultimo giorno |
| Funding | +0.0029% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-13 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $1.97B | leva aperta stimata in dollari |
| Open Interest 24h | +1.10% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.53 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $50,220 | $75,330 |
| 10x | $56,498 | $69,053 |
| 20x | $59,636 | $65,914 |
| 50x | $61,520 | $64,031 |

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

- funding negativo: gli short pagano i long
- open interest in calo: leva in uscita
- long/short ratio alto: mercato più long

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $76.36 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +0.63% | movimento dell'ultimo giorno |
| Funding | -0.0016% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-13 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $233.69M | leva aperta stimata in dollari |
| Open Interest 24h | -23.85% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 2.64 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $61.09 | $91.63 |
| 10x | $68.72 | $84.00 |
| 20x | $72.54 | $80.18 |
| 50x | $74.83 | $77.89 |

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
| Prezzo | $0.07221 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -0.62% | movimento dell'ultimo giorno |
| Funding | +0.0046% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-13 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $67.14M | leva aperta stimata in dollari |
| Open Interest 24h | +17.25% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 4.12 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $0.05777 | $0.08665 |
| 10x | $0.06499 | $0.07943 |
| 20x | $0.06860 | $0.07582 |
| 50x | $0.07077 | $0.07365 |

### Note tecniche usate dallo score

- open interest in forte aumento: entra molta leva
- long/short ratio alto: più mercato sbilanciato long

---
