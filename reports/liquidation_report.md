# Report semplice futures / liquidazioni BTC / SOL / DOGE

Generato: **2026-07-10 13:40:29 CEST**  
UTC: **2026-07-10 11:40:29 UTC**

Fonte dati: **OKX Futures pubblici**.  
Questo report non è la vera heatmap CoinGlass. Serve a capire se il mercato futures è carico di long, short o leva.

## Traduzione in parole semplici

| Asset | Lettura | Forza | Cosa significa in pratica |
| --- | --- | --- | --- |
| BTC | Misto | 1/5 | Qui pesa di più il report frattale. |
| SOL | Misto | 1/5 | Qui pesa di più il report frattale. |
| DOGE | Rischio sotto | 2/5 | Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale. |

## Numeri principali

| Asset | Prezzo | Prezzo 24h | Funding | Open Interest | OI 24h | Long/Short |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | $64,330 | +2.74% | +0.0070% | $2.01B | -0.24% | 1.95 |
| SOL | $79.17 | +2.35% | +0.0013% | $245.30M | -21.94% | 2.64 |
| DOGE | $0.07412 | +2.56% | +0.0100% | $69.97M | -1.88% | 3.01 |

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
| Prezzo | $64,330 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +2.74% | movimento dell'ultimo giorno |
| Funding | +0.0070% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-10 18:00 | prossimo aggiornamento funding |
| Open Interest stimato | $2.01B | leva aperta stimata in dollari |
| Open Interest 24h | -0.24% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.95 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $51,464 | $77,196 |
| 10x | $57,897 | $70,763 |
| 20x | $61,113 | $67,546 |
| 50x | $63,043 | $65,616 |

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
| Prezzo | $79.17 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +2.35% | movimento dell'ultimo giorno |
| Funding | +0.0013% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-10 18:00 | prossimo aggiornamento funding |
| Open Interest stimato | $245.30M | leva aperta stimata in dollari |
| Open Interest 24h | -21.94% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 2.64 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $63.34 | $95.00 |
| 10x | $71.25 | $87.09 |
| 20x | $75.21 | $83.13 |
| 50x | $77.59 | $80.75 |

### Note tecniche usate dallo score

- open interest in forte calo: parte della leva è già uscita
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
- open interest abbastanza stabile
- long/short ratio alto: mercato più long

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $0.07412 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +2.56% | movimento dell'ultimo giorno |
| Funding | +0.0100% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-10 18:00 | prossimo aggiornamento funding |
| Open Interest stimato | $69.97M | leva aperta stimata in dollari |
| Open Interest 24h | -1.88% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 3.01 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $0.05930 | $0.08894 |
| 10x | $0.06671 | $0.08153 |
| 20x | $0.07041 | $0.07783 |
| 50x | $0.07264 | $0.07560 |

### Note tecniche usate dallo score

- funding positivo: mercato leggermente carico di long
- long/short ratio alto: più mercato sbilanciato long

---
