# Report semplice futures / liquidazioni BTC / SOL / DOGE

Generato: **2026-07-06 15:58:23 CEST**  
UTC: **2026-07-06 13:58:23 UTC**

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
| BTC | $61,866 | -1.45% | +0.0065% | $1.94B | +1.68% | 1.66 |
| SOL | $80.26 | -1.07% | +0.0016% | $262.64M | -27.84% | 2.78 |
| DOGE | $0.07536 | -1.58% | +0.0025% | $67.85M | +6.79% | 2.99 |

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
| Prezzo | $61,866 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -1.45% | movimento dell'ultimo giorno |
| Funding | +0.0065% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-06 18:00 | prossimo aggiornamento funding |
| Open Interest stimato | $1.94B | leva aperta stimata in dollari |
| Open Interest 24h | +1.68% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.66 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $49,493 | $74,239 |
| 10x | $55,679 | $68,053 |
| 20x | $58,773 | $64,959 |
| 50x | $60,629 | $63,103 |

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
| Prezzo | $80.26 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -1.07% | movimento dell'ultimo giorno |
| Funding | +0.0016% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-06 18:00 | prossimo aggiornamento funding |
| Open Interest stimato | $262.64M | leva aperta stimata in dollari |
| Open Interest 24h | -27.84% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 2.78 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $64.21 | $96.31 |
| 10x | $72.23 | $88.29 |
| 20x | $76.25 | $84.27 |
| 50x | $78.65 | $81.87 |

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
| Prezzo | $0.07536 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -1.58% | movimento dell'ultimo giorno |
| Funding | +0.0025% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-06 18:00 | prossimo aggiornamento funding |
| Open Interest stimato | $67.85M | leva aperta stimata in dollari |
| Open Interest 24h | +6.79% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 2.99 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $0.06029 | $0.09043 |
| 10x | $0.06782 | $0.08290 |
| 20x | $0.07159 | $0.07913 |
| 50x | $0.07385 | $0.07687 |

### Note tecniche usate dallo score

- open interest in forte aumento: entra molta leva
- long/short ratio alto: più mercato sbilanciato long

---
