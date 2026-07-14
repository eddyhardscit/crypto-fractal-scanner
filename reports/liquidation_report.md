# Report semplice futures / liquidazioni BTC / SOL / DOGE

Generato: **2026-07-14 13:44:45 CEST**  
UTC: **2026-07-14 11:44:45 UTC**

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
| BTC | 62.768 $ | -0.16% | +0.0024% | $1.97B | +7.28% | 1.33 |
| SOL | 75,34 $ | -1.30% | +0.0032% | $229.55M | -20.05% | 2.34 |
| DOGE | 0.07220 $ | -0.01% | +0.0069% | $68.75M | +18.67% | 3.89 |

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
| Prezzo | $62,826 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -0.16% | movimento dell'ultimo giorno |
| Funding | +0.0024% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-14 18:00 | prossimo aggiornamento funding |
| Open Interest stimato | $1.97B | leva aperta stimata in dollari |
| Open Interest 24h | +7.28% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.33 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $50,261 | $75,392 |
| 10x | $56,544 | $69,109 |
| 20x | $59,685 | $65,968 |
| 50x | $61,570 | $64,083 |

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
| Prezzo | $75.36 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -1.30% | movimento dell'ultimo giorno |
| Funding | +0.0032% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-14 18:00 | prossimo aggiornamento funding |
| Open Interest stimato | $229.55M | leva aperta stimata in dollari |
| Open Interest 24h | -20.05% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 2.34 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $60.29 | $90.43 |
| 10x | $67.82 | $82.90 |
| 20x | $71.59 | $79.13 |
| 50x | $73.85 | $76.87 |

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
| Prezzo | $0.07225 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -0.01% | movimento dell'ultimo giorno |
| Funding | +0.0069% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-14 18:00 | prossimo aggiornamento funding |
| Open Interest stimato | $68.75M | leva aperta stimata in dollari |
| Open Interest 24h | +18.67% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 3.89 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $0.05780 | $0.08670 |
| 10x | $0.06502 | $0.07948 |
| 20x | $0.06864 | $0.07586 |
| 50x | $0.07080 | $0.07369 |

### Note tecniche usate dallo score

- open interest in forte aumento: entra molta leva
- long/short ratio alto: più mercato sbilanciato long

---
