# Report semplice futures / liquidazioni BTC / SOL / DOGE

Generato: **2026-07-05 14:30:12 CEST**  
UTC: **2026-07-05 12:30:12 UTC**

Fonte dati: **OKX Futures pubblici**.  
Questo report non è la vera heatmap CoinGlass. Serve a capire se il mercato futures è carico di long, short o leva.

## Traduzione in parole semplici

| Asset | Lettura | Forza | Cosa significa in pratica |
| --- | --- | --- | --- |
| BTC | Rischio sotto | 5/5 | Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale. |
| SOL | Misto | 1/5 | Qui pesa di più il report frattale. |
| DOGE | Leva alta, direzione mista | 3/5 | Meglio non forzare. Aspetta conferma dal frattale o dal prezzo. |

## Numeri principali

| Asset | Prezzo | Prezzo 24h | Funding | Open Interest | OI 24h | Long/Short |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | $62,724 | +0.25% | +0.0041% | $1.94B | +15.31% | 1.76 |
| SOL | $81.02 | -0.65% | +0.0035% | $276.01M | -21.36% | 3.20 |
| DOGE | $0.07614 | -1.09% | +0.0041% | $72.55M | +6.32% | 3.84 |

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

**RISCHIO DISCESA / FLUSH SOTTO**  
**Forza segnale: 5/5**

BTC: i futures sembrano più vulnerabili verso una discesa improvvisa. Non significa che deve scendere, ma se rompe sotto può accelerare.

**Tradotto operativamente:** Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale.

### Perché

- funding positivo: i long pagano gli short
- open interest in aumento: più leva nel sistema
- long/short ratio alto: mercato più long

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $62,724 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +0.25% | movimento dell'ultimo giorno |
| Funding | +0.0041% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-05 18:00 | prossimo aggiornamento funding |
| Open Interest stimato | $1.94B | leva aperta stimata in dollari |
| Open Interest 24h | +15.31% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.76 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $50,179 | $75,268 |
| 10x | $56,451 | $68,996 |
| 20x | $59,587 | $65,860 |
| 50x | $61,469 | $63,978 |

### Note tecniche usate dallo score

- open interest in forte aumento: entra molta leva
- prezzo su + leva su + funding positivo: rischio pulizia dei long sotto
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
| Prezzo | $81.02 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -0.65% | movimento dell'ultimo giorno |
| Funding | +0.0035% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-05 18:00 | prossimo aggiornamento funding |
| Open Interest stimato | $276.01M | leva aperta stimata in dollari |
| Open Interest 24h | -21.36% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 3.20 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $64.82 | $97.22 |
| 10x | $72.92 | $89.12 |
| 20x | $76.97 | $85.07 |
| 50x | $79.40 | $82.64 |

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
| Prezzo | $0.07614 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -1.09% | movimento dell'ultimo giorno |
| Funding | +0.0041% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-05 18:00 | prossimo aggiornamento funding |
| Open Interest stimato | $72.55M | leva aperta stimata in dollari |
| Open Interest 24h | +6.32% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 3.84 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $0.06091 | $0.09137 |
| 10x | $0.06853 | $0.08375 |
| 20x | $0.07233 | $0.07995 |
| 50x | $0.07462 | $0.07766 |

### Note tecniche usate dallo score

- open interest in forte aumento: entra molta leva
- long/short ratio alto: più mercato sbilanciato long

---
