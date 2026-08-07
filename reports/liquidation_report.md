# Report semplice futures / liquidazioni BTC / SOL / DOGE

Generato: **2026-08-07 07:16:44 CEST**  
UTC: **2026-08-07 05:16:44 UTC**

Fonte dati: **OKX Futures pubblici**.  
Questo report non è la vera heatmap CoinGlass. Serve a capire se il mercato futures è carico di long, short o leva.

## Traduzione in parole semplici

| Asset | Lettura | Forza | Cosa significa in pratica |
| --- | --- | --- | --- |
| BTC | Misto | 1/5 | Qui pesa di più il report frattale. |
| SOL | Leva alta, direzione mista | 3/5 | Meglio non forzare. Aspetta conferma dal frattale o dal prezzo. |
| DOGE | Misto | 1/5 | Qui pesa di più il report frattale. |

## Numeri principali

| Asset | Prezzo | Prezzo 24h | Funding | Open Interest | OI 24h | Long/Short |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 64.195 $ | -1.13% | +0.0067% | $2.06B | -3.65% | 1.55 |
| SOL | 72,65 $ | -2.21% | +0.0047% | $210.78M | +20.44% | 1.85 |
| DOGE | 0.06898 $ | -1.47% | +0.0066% | $85.23M | -18.86% | 3.58 |

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
| Prezzo | $64,211 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -1.13% | movimento dell'ultimo giorno |
| Funding | +0.0067% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-08-07 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $2.06B | leva aperta stimata in dollari |
| Open Interest 24h | -3.65% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.55 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $51,369 | $77,053 |
| 10x | $57,790 | $70,632 |
| 20x | $61,001 | $67,422 |
| 50x | $62,927 | $65,495 |

### Note tecniche usate dallo score

- long/short ratio alto: più mercato sbilanciato long

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
| Prezzo | $72.63 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -2.21% | movimento dell'ultimo giorno |
| Funding | +0.0047% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-08-07 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $210.78M | leva aperta stimata in dollari |
| Open Interest 24h | +20.44% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.85 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $58.10 | $87.16 |
| 10x | $65.37 | $79.89 |
| 20x | $69.00 | $76.26 |
| 50x | $71.18 | $74.08 |

### Note tecniche usate dallo score

- open interest in forte aumento: entra molta leva
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
- open interest in calo: leva in uscita
- long/short ratio alto: mercato più long

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $0.06905 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -1.47% | movimento dell'ultimo giorno |
| Funding | +0.0066% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-08-07 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $85.23M | leva aperta stimata in dollari |
| Open Interest 24h | -18.86% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 3.58 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $0.05524 | $0.08286 |
| 10x | $0.06214 | $0.07596 |
| 20x | $0.06560 | $0.07250 |
| 50x | $0.06767 | $0.07043 |

### Note tecniche usate dallo score

- open interest in forte calo: parte della leva è già uscita
- long/short ratio alto: più mercato sbilanciato long

---
