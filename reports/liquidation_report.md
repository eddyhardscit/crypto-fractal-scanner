# Report semplice futures / liquidazioni BTC / SOL / DOGE

Generato: **2026-08-08 07:18:54 CEST**  
UTC: **2026-08-08 05:18:54 UTC**

Fonte dati: **OKX Futures pubblici**.  
Questo report non è la vera heatmap CoinGlass. Serve a capire se il mercato futures è carico di long, short o leva.

## Traduzione in parole semplici

| Asset | Lettura | Forza | Cosa significa in pratica |
| --- | --- | --- | --- |
| BTC | Misto | 1/5 | Qui pesa di più il report frattale. |
| SOL | Rischio sotto | 5/5 | Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale. |
| DOGE | Rischio sotto | 2/5 | Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale. |

## Numeri principali

| Asset | Prezzo | Prezzo 24h | Funding | Open Interest | OI 24h | Long/Short |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 64.960 $ | +1.22% | +0.0006% | $2.04B | -6.21% | 1.52 |
| SOL | 74,58 $ | +2.60% | +0.0100% | $210.64M | +15.67% | 2.05 |
| DOGE | 0.07009 $ | +1.59% | +0.0100% | $79.25M | -8.55% | 3.58 |

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
| Prezzo | $64,975 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +1.22% | movimento dell'ultimo giorno |
| Funding | +0.0006% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-08-08 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $2.04B | leva aperta stimata in dollari |
| Open Interest 24h | -6.21% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.52 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $51,980 | $77,970 |
| 10x | $58,477 | $71,472 |
| 20x | $61,726 | $68,224 |
| 50x | $63,675 | $66,274 |

### Note tecniche usate dallo score

- open interest in forte calo: parte della leva è già uscita
- long/short ratio alto: più mercato sbilanciato long

---

## Solana — SOL

### Lettura semplice

**RISCHIO DISCESA / FLUSH SOTTO**  
**Forza segnale: 5/5**

SOL: i futures sembrano più vulnerabili verso una discesa improvvisa. Non significa che deve scendere, ma se rompe sotto può accelerare.

**Tradotto operativamente:** Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale.

### Perché

- funding positivo: i long pagano gli short
- open interest in aumento: più leva nel sistema
- long/short ratio alto: mercato più long

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $74.51 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +2.60% | movimento dell'ultimo giorno |
| Funding | +0.0100% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-08-08 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $210.64M | leva aperta stimata in dollari |
| Open Interest 24h | +15.67% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 2.05 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $59.61 | $89.41 |
| 10x | $67.06 | $81.96 |
| 20x | $70.78 | $78.24 |
| 50x | $73.02 | $76.00 |

### Note tecniche usate dallo score

- funding positivo: mercato leggermente carico di long
- open interest in forte aumento: entra molta leva
- prezzo su + leva su + funding positivo: rischio pulizia dei long sotto
- long/short ratio alto: più mercato sbilanciato long

---

## Dogecoin — DOGE

### Lettura semplice

**RISCHIO DISCESA / FLUSH SOTTO**  
**Forza segnale: 2/5**

DOGE: i futures sembrano più vulnerabili verso una discesa improvvisa. Non significa che deve scendere, ma se rompe sotto può accelerare.

**Tradotto operativamente:** Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale.

### Perché

- funding positivo: i long pagano gli short
- open interest in calo: leva in uscita
- long/short ratio alto: mercato più long

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $0.07013 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +1.59% | movimento dell'ultimo giorno |
| Funding | +0.0100% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-08-08 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $79.25M | leva aperta stimata in dollari |
| Open Interest 24h | -8.55% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 3.58 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $0.05610 | $0.08416 |
| 10x | $0.06312 | $0.07714 |
| 20x | $0.06662 | $0.07364 |
| 50x | $0.06873 | $0.07153 |

### Note tecniche usate dallo score

- funding positivo: mercato leggermente carico di long
- open interest in forte calo: parte della leva è già uscita
- long/short ratio alto: più mercato sbilanciato long

---
