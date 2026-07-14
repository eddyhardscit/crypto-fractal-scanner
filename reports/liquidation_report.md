# Report semplice futures / liquidazioni BTC / SOL / DOGE

Generato: **2026-07-14 10:22:54 CEST**  
UTC: **2026-07-14 08:22:54 UTC**

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
| BTC | 62.239 $ | -0.60% | +0.0016% | $1.96B | +7.03% | 1.35 |
| SOL | 74,86 $ | -1.60% | +0.0041% | $230.15M | -21.11% | 2.32 |
| DOGE | 0.07185 $ | -0.32% | +0.0049% | $68.18M | +17.08% | 3.88 |

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
| Prezzo | $62,563 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -0.60% | movimento dell'ultimo giorno |
| Funding | +0.0016% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-14 18:00 | prossimo aggiornamento funding |
| Open Interest stimato | $1.96B | leva aperta stimata in dollari |
| Open Interest 24h | +7.03% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.35 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $50,050 | $75,076 |
| 10x | $56,307 | $68,819 |
| 20x | $59,435 | $65,691 |
| 50x | $61,312 | $63,814 |

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
| Prezzo | $75.13 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -1.60% | movimento dell'ultimo giorno |
| Funding | +0.0041% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-14 18:00 | prossimo aggiornamento funding |
| Open Interest stimato | $230.15M | leva aperta stimata in dollari |
| Open Interest 24h | -21.11% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 2.32 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $60.10 | $90.16 |
| 10x | $67.62 | $82.64 |
| 20x | $71.37 | $78.89 |
| 50x | $73.63 | $76.63 |

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
| Prezzo | $0.07208 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -0.32% | movimento dell'ultimo giorno |
| Funding | +0.0049% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-14 18:00 | prossimo aggiornamento funding |
| Open Interest stimato | $68.18M | leva aperta stimata in dollari |
| Open Interest 24h | +17.08% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 3.88 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $0.05766 | $0.08650 |
| 10x | $0.06487 | $0.07929 |
| 20x | $0.06848 | $0.07568 |
| 50x | $0.07064 | $0.07352 |

### Note tecniche usate dallo score

- open interest in forte aumento: entra molta leva
- long/short ratio alto: più mercato sbilanciato long

---
