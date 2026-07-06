# Report semplice futures / liquidazioni BTC / SOL / DOGE

Generato: **2026-07-06 16:10:47 CEST**  
UTC: **2026-07-06 14:10:47 UTC**

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
| BTC | $61,861 | -1.36% | +0.0063% | $1.95B | +1.43% | 1.66 |
| SOL | $80.22 | -1.17% | +0.0011% | $262.33M | -27.51% | 2.77 |
| DOGE | $0.07530 | -1.65% | +0.0024% | $67.75M | +9.15% | 2.97 |

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
| Prezzo | $61,861 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -1.36% | movimento dell'ultimo giorno |
| Funding | +0.0063% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-06 18:00 | prossimo aggiornamento funding |
| Open Interest stimato | $1.95B | leva aperta stimata in dollari |
| Open Interest 24h | +1.43% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.66 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $49,489 | $74,233 |
| 10x | $55,675 | $68,047 |
| 20x | $58,768 | $64,954 |
| 50x | $60,624 | $63,098 |

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
| Prezzo | $80.22 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -1.17% | movimento dell'ultimo giorno |
| Funding | +0.0011% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-06 18:00 | prossimo aggiornamento funding |
| Open Interest stimato | $262.33M | leva aperta stimata in dollari |
| Open Interest 24h | -27.51% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 2.77 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $64.18 | $96.26 |
| 10x | $72.20 | $88.24 |
| 20x | $76.21 | $84.23 |
| 50x | $78.62 | $81.82 |

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
| Prezzo | $0.07530 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -1.65% | movimento dell'ultimo giorno |
| Funding | +0.0024% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-06 18:00 | prossimo aggiornamento funding |
| Open Interest stimato | $67.75M | leva aperta stimata in dollari |
| Open Interest 24h | +9.15% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 2.97 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $0.06024 | $0.09036 |
| 10x | $0.06777 | $0.08283 |
| 20x | $0.07154 | $0.07907 |
| 50x | $0.07379 | $0.07681 |

### Note tecniche usate dallo score

- open interest in forte aumento: entra molta leva
- long/short ratio alto: più mercato sbilanciato long

---
