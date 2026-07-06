# Report semplice futures / liquidazioni BTC / SOL / DOGE

Generato: **2026-07-06 16:23:15 CEST**  
UTC: **2026-07-06 14:23:15 UTC**

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
| BTC | $61,884 | -1.25% | +0.0059% | $1.95B | +1.94% | 1.66 |
| SOL | $80.12 | -1.15% | +0.0007% | $261.84M | -27.51% | 2.77 |
| DOGE | $0.07533 | -1.59% | +0.0022% | $67.80M | +9.15% | 2.97 |

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
| Prezzo | $61,884 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -1.25% | movimento dell'ultimo giorno |
| Funding | +0.0059% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-06 18:00 | prossimo aggiornamento funding |
| Open Interest stimato | $1.95B | leva aperta stimata in dollari |
| Open Interest 24h | +1.94% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.66 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $49,508 | $74,261 |
| 10x | $55,696 | $68,073 |
| 20x | $58,790 | $64,979 |
| 50x | $60,647 | $63,122 |

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

- funding positivo: i long pagano gli short
- open interest in calo: leva in uscita
- long/short ratio alto: mercato più long

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $80.12 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -1.15% | movimento dell'ultimo giorno |
| Funding | +0.0007% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-06 18:00 | prossimo aggiornamento funding |
| Open Interest stimato | $261.84M | leva aperta stimata in dollari |
| Open Interest 24h | -27.51% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 2.77 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $64.10 | $96.14 |
| 10x | $72.11 | $88.13 |
| 20x | $76.11 | $84.13 |
| 50x | $78.52 | $81.72 |

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
| Prezzo | $0.07533 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -1.59% | movimento dell'ultimo giorno |
| Funding | +0.0022% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-06 18:00 | prossimo aggiornamento funding |
| Open Interest stimato | $67.80M | leva aperta stimata in dollari |
| Open Interest 24h | +9.15% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 2.97 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $0.06026 | $0.09040 |
| 10x | $0.06780 | $0.08286 |
| 20x | $0.07156 | $0.07910 |
| 50x | $0.07382 | $0.07684 |

### Note tecniche usate dallo score

- open interest in forte aumento: entra molta leva
- long/short ratio alto: più mercato sbilanciato long

---
