# Report semplice futures / liquidazioni BTC / SOL / DOGE

Generato: **2026-07-16 17:05:39 CEST**  
UTC: **2026-07-16 15:05:39 UTC**

Fonte dati: **OKX Futures pubblici**.  
Questo report non è la vera heatmap CoinGlass. Serve a capire se il mercato futures è carico di long, short o leva.

## Traduzione in parole semplici

| Asset | Lettura | Forza | Cosa significa in pratica |
| --- | --- | --- | --- |
| BTC | Leva alta, direzione mista | 3/5 | Meglio non forzare. Aspetta conferma dal frattale o dal prezzo. |
| SOL | Misto | 1/5 | Qui pesa di più il report frattale. |
| DOGE | Rischio sotto | 4/5 | Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale. |

## Numeri principali

| Asset | Prezzo | Prezzo 24h | Funding | Open Interest | OI 24h | Long/Short |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 64.444 $ | -1.39% | +0.0019% | $1.97B | +6.10% | 1.35 |
| SOL | 76,30 $ | -2.38% | +0.0001% | $222.68M | -13.92% | 2.22 |
| DOGE | 0.07345 $ | -1.95% | +0.0100% | $72.56M | +9.15% | 4.36 |

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
| Prezzo | $64,441 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -1.39% | movimento dell'ultimo giorno |
| Funding | +0.0019% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-16 18:00 | prossimo aggiornamento funding |
| Open Interest stimato | $1.97B | leva aperta stimata in dollari |
| Open Interest 24h | +6.10% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.35 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $51,553 | $77,329 |
| 10x | $57,997 | $70,885 |
| 20x | $61,219 | $67,663 |
| 50x | $63,152 | $65,730 |

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
| Prezzo | $76.17 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -2.38% | movimento dell'ultimo giorno |
| Funding | +0.0001% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-16 18:00 | prossimo aggiornamento funding |
| Open Interest stimato | $222.68M | leva aperta stimata in dollari |
| Open Interest 24h | -13.92% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 2.22 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $60.94 | $91.40 |
| 10x | $68.55 | $83.79 |
| 20x | $72.36 | $79.98 |
| 50x | $74.65 | $77.69 |

### Note tecniche usate dallo score

- open interest in forte calo: parte della leva è già uscita
- long/short ratio alto: più mercato sbilanciato long

---

## Dogecoin — DOGE

### Lettura semplice

**RISCHIO DISCESA / FLUSH SOTTO**  
**Forza segnale: 4/5**

DOGE: i futures sembrano più vulnerabili verso una discesa improvvisa. Non significa che deve scendere, ma se rompe sotto può accelerare.

**Tradotto operativamente:** Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale.

### Perché

- funding positivo: i long pagano gli short
- open interest in aumento: più leva nel sistema
- long/short ratio alto: mercato più long

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $0.07332 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -1.95% | movimento dell'ultimo giorno |
| Funding | +0.0100% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-16 18:00 | prossimo aggiornamento funding |
| Open Interest stimato | $72.56M | leva aperta stimata in dollari |
| Open Interest 24h | +9.15% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 4.36 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $0.05866 | $0.08798 |
| 10x | $0.06599 | $0.08065 |
| 20x | $0.06965 | $0.07699 |
| 50x | $0.07185 | $0.07479 |

### Note tecniche usate dallo score

- funding positivo: mercato leggermente carico di long
- open interest in forte aumento: entra molta leva
- long/short ratio alto: più mercato sbilanciato long

---
