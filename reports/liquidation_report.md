# Report semplice futures / liquidazioni BTC / SOL / DOGE

Generato: **2026-08-19 07:32:59 CEST**  
UTC: **2026-08-19 05:32:59 UTC**

Fonte dati: **OKX Futures pubblici**.  
Questo report non è la vera heatmap CoinGlass. Serve a capire se il mercato futures è carico di long, short o leva.

## Traduzione in parole semplici

| Asset | Lettura | Forza | Cosa significa in pratica |
| --- | --- | --- | --- |
| BTC | Rischio sotto | 2/5 | Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale. |
| SOL | Misto | 1/5 | Qui pesa di più il report frattale. |
| DOGE | Misto | 1/5 | Qui pesa di più il report frattale. |

## Numeri principali

| Asset | Prezzo | Prezzo 24h | Funding | Open Interest | OI 24h | Long/Short |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 64.306 $ | +0.22% | +0.0100% | $2.13B | -4.05% | 1.45 |
| SOL | 76,92 $ | +1.61% | -0.0001% | $232.24M | -6.14% | 2.67 |
| DOGE | 0.07000 $ | +0.46% | +0.0025% | $85.35M | -14.17% | 4.89 |

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
**Forza segnale: 2/5**

BTC: i futures sembrano più vulnerabili verso una discesa improvvisa. Non significa che deve scendere, ma se rompe sotto può accelerare.

**Tradotto operativamente:** Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale.

### Perché

- funding positivo: i long pagano gli short
- open interest in calo: leva in uscita
- long/short ratio alto: mercato più long

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $64,320 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +0.22% | movimento dell'ultimo giorno |
| Funding | +0.0100% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-08-19 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $2.13B | leva aperta stimata in dollari |
| Open Interest 24h | -4.05% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.45 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $51,456 | $77,184 |
| 10x | $57,888 | $70,752 |
| 20x | $61,104 | $67,536 |
| 50x | $63,034 | $65,606 |

### Note tecniche usate dallo score

- funding positivo: mercato leggermente carico di long
- long/short ratio alto: più mercato sbilanciato long

---

## Solana — SOL

### Lettura semplice

**NEUTRALE / POCO CHIARO**  
**Forza segnale: 1/5**

SOL: i futures non danno una lettura chiara. Non si vede uno sbilanciamento forte né long né short.

**Tradotto operativamente:** Qui pesa di più il report frattale.

### Perché

- funding negativo: gli short pagano i long
- open interest in calo: leva in uscita
- long/short ratio alto: mercato più long

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $76.87 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +1.61% | movimento dell'ultimo giorno |
| Funding | -0.0001% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-08-19 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $232.24M | leva aperta stimata in dollari |
| Open Interest 24h | -6.14% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 2.67 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $61.50 | $92.24 |
| 10x | $69.18 | $84.56 |
| 20x | $73.03 | $80.71 |
| 50x | $75.33 | $78.41 |

### Note tecniche usate dallo score

- open interest in forte calo: parte della leva è già uscita
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
| Prezzo | $0.06998 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +0.46% | movimento dell'ultimo giorno |
| Funding | +0.0025% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-08-19 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $85.35M | leva aperta stimata in dollari |
| Open Interest 24h | -14.17% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 4.89 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $0.05598 | $0.08398 |
| 10x | $0.06298 | $0.07698 |
| 20x | $0.06648 | $0.07348 |
| 50x | $0.06858 | $0.07138 |

### Note tecniche usate dallo score

- open interest in forte calo: parte della leva è già uscita
- long/short ratio alto: più mercato sbilanciato long

---
