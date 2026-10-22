# Report semplice futures / liquidazioni BTC / SOL / DOGE

Generato: **2026-10-22 07:33:46 CEST**  
UTC: **2026-10-22 05:33:46 UTC**

Fonte dati: **OKX Futures pubblici**.  
Questo report non è la vera heatmap CoinGlass. Serve a capire se il mercato futures è carico di long, short o leva.

## Traduzione in parole semplici

| Asset | Lettura | Forza | Cosa significa in pratica |
| --- | --- | --- | --- |
| BTC | Misto | 1/5 | Qui pesa di più il report frattale. |
| SOL | Leva alta, direzione mista | 3/5 | Meglio non forzare. Aspetta conferma dal frattale o dal prezzo. |
| DOGE | Leva alta, direzione mista | 3/5 | Meglio non forzare. Aspetta conferma dal frattale o dal prezzo. |

## Numeri principali

| Asset | Prezzo | Prezzo 24h | Funding | Open Interest | OI 24h | Long/Short |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 82.837 $ | -0.06% | +0.0092% | $2.48B | +0.54% | 0.93 |
| SOL | 105,19 $ | -0.82% | +0.0012% | $308.44M | +14.68% | 1.61 |
| DOGE | 0.08008 $ | -2.19% | +0.0076% | $100.07M | +15.82% | 2.54 |

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
- long/short ratio abbastanza equilibrato

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $82,812 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -0.06% | movimento dell'ultimo giorno |
| Funding | +0.0092% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-10-22 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $2.48B | leva aperta stimata in dollari |
| Open Interest 24h | +0.54% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 0.93 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $66,250 | $99,375 |
| 10x | $74,531 | $91,094 |
| 20x | $78,672 | $86,953 |
| 50x | $81,156 | $84,469 |

---

## Solana — SOL

### Lettura semplice

**MOLTA LEVA MA DIREZIONE MISTA**  
**Forza segnale: 3/5**

SOL: c'è molta leva nel mercato, ma la direzione non è pulita. Può arrivare un movimento violento, ma non è chiaro se sopra o sotto.

**Tradotto operativamente:** Meglio non forzare. Aspetta conferma dal frattale o dal prezzo.

### Perché

- funding positivo: i long pagano gli short
- open interest in aumento: più leva nel sistema
- long/short ratio alto: mercato più long

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $105.13 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -0.82% | movimento dell'ultimo giorno |
| Funding | +0.0012% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-10-22 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $308.44M | leva aperta stimata in dollari |
| Open Interest 24h | +14.68% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.61 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $84.10 | $126.16 |
| 10x | $94.62 | $115.64 |
| 20x | $99.87 | $110.39 |
| 50x | $103.03 | $107.23 |

### Note tecniche usate dallo score

- open interest in forte aumento: entra molta leva
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
| Prezzo | $0.07994 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -2.19% | movimento dell'ultimo giorno |
| Funding | +0.0076% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-10-22 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $100.07M | leva aperta stimata in dollari |
| Open Interest 24h | +15.82% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 2.54 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $0.06395 | $0.09593 |
| 10x | $0.07195 | $0.08793 |
| 20x | $0.07594 | $0.08394 |
| 50x | $0.07834 | $0.08154 |

### Note tecniche usate dallo score

- open interest in forte aumento: entra molta leva
- long/short ratio alto: più mercato sbilanciato long

---
