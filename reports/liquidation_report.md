# Report semplice futures / liquidazioni BTC / SOL / DOGE

Generato: **2026-07-17 02:32:53 CEST**  
UTC: **2026-07-17 00:32:53 UTC**

Fonte dati: **OKX Futures pubblici**.  
Questo report non è la vera heatmap CoinGlass. Serve a capire se il mercato futures è carico di long, short o leva.

## Traduzione in parole semplici

| Asset | Lettura | Forza | Cosa significa in pratica |
| --- | --- | --- | --- |
| BTC | Misto | 2/5 | Qui pesa di più il report frattale. |
| SOL | Misto | 1/5 | Qui pesa di più il report frattale. |
| DOGE | Rischio sotto | 4/5 | Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale. |

## Numeri principali

| Asset | Prezzo | Prezzo 24h | Funding | Open Interest | OI 24h | Long/Short |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 63.741 $ | -1.32% | +0.0054% | $1.95B | +4.62% | 1.40 |
| SOL | 75,28 $ | -2.30% | +0.0015% | $212.28M | -10.12% | 2.20 |
| DOGE | 0.07229 $ | -2.17% | +0.0100% | $68.96M | +8.66% | 4.29 |

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
**Forza segnale: 2/5**

BTC: i futures non danno una lettura chiara. Non si vede uno sbilanciamento forte né long né short.

**Tradotto operativamente:** Qui pesa di più il report frattale.

### Perché

- funding positivo: i long pagano gli short
- open interest in aumento: più leva nel sistema
- long/short ratio alto: mercato più long

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $63,680 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -1.32% | movimento dell'ultimo giorno |
| Funding | +0.0054% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-17 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $1.95B | leva aperta stimata in dollari |
| Open Interest 24h | +4.62% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.40 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $50,944 | $76,416 |
| 10x | $57,312 | $70,048 |
| 20x | $60,496 | $66,864 |
| 50x | $62,406 | $64,954 |

### Note tecniche usate dallo score

- open interest in aumento: leva in crescita
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
| Prezzo | $75.17 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -2.30% | movimento dell'ultimo giorno |
| Funding | +0.0015% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-17 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $212.28M | leva aperta stimata in dollari |
| Open Interest 24h | -10.12% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 2.20 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $60.14 | $90.20 |
| 10x | $67.65 | $82.69 |
| 20x | $71.41 | $78.93 |
| 50x | $73.67 | $76.67 |

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
| Prezzo | $0.07224 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -2.17% | movimento dell'ultimo giorno |
| Funding | +0.0100% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-17 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $68.96M | leva aperta stimata in dollari |
| Open Interest 24h | +8.66% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 4.29 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $0.05779 | $0.08669 |
| 10x | $0.06502 | $0.07946 |
| 20x | $0.06863 | $0.07585 |
| 50x | $0.07080 | $0.07368 |

### Note tecniche usate dallo score

- funding positivo: mercato leggermente carico di long
- open interest in forte aumento: entra molta leva
- long/short ratio alto: più mercato sbilanciato long

---
