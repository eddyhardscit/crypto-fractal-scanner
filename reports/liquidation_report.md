# Report semplice futures / liquidazioni BTC / SOL / DOGE

Generato: **2026-10-24 07:33:39 CEST**  
UTC: **2026-10-24 05:33:39 UTC**

Fonte dati: **OKX Futures pubblici**.  
Questo report non è la vera heatmap CoinGlass. Serve a capire se il mercato futures è carico di long, short o leva.

## Traduzione in parole semplici

| Asset | Lettura | Forza | Cosa significa in pratica |
| --- | --- | --- | --- |
| BTC | Misto | 1/5 | Qui pesa di più il report frattale. |
| SOL | Rischio sotto | 4/5 | Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale. |
| DOGE | Misto | 2/5 | Qui pesa di più il report frattale. |

## Numeri principali

| Asset | Prezzo | Prezzo 24h | Funding | Open Interest | OI 24h | Long/Short |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 80.661 $ | -1.27% | +0.0028% | $2.46B | -3.09% | 1.21 |
| SOL | 102,17 $ | -2.12% | +0.0100% | $303.76M | +8.25% | 1.69 |
| DOGE | 0.07829 $ | -1.94% | +0.0040% | $94.85M | +2.67% | 3.70 |

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
- long/short ratio abbastanza equilibrato

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $80,705 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -1.27% | movimento dell'ultimo giorno |
| Funding | +0.0028% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-10-24 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $2.46B | leva aperta stimata in dollari |
| Open Interest 24h | -3.09% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.21 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $64,564 | $96,846 |
| 10x | $72,635 | $88,776 |
| 20x | $76,670 | $84,741 |
| 50x | $79,091 | $82,319 |

---

## Solana — SOL

### Lettura semplice

**RISCHIO DISCESA / FLUSH SOTTO**  
**Forza segnale: 4/5**

SOL: i futures sembrano più vulnerabili verso una discesa improvvisa. Non significa che deve scendere, ma se rompe sotto può accelerare.

**Tradotto operativamente:** Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale.

### Perché

- funding positivo: i long pagano gli short
- open interest in aumento: più leva nel sistema
- long/short ratio alto: mercato più long

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $102.26 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -2.12% | movimento dell'ultimo giorno |
| Funding | +0.0100% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-10-24 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $303.76M | leva aperta stimata in dollari |
| Open Interest 24h | +8.25% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.69 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $81.81 | $122.71 |
| 10x | $92.03 | $112.49 |
| 20x | $97.15 | $107.37 |
| 50x | $100.21 | $104.31 |

### Note tecniche usate dallo score

- funding positivo: mercato leggermente carico di long
- open interest in forte aumento: entra molta leva
- long/short ratio alto: più mercato sbilanciato long

---

## Dogecoin — DOGE

### Lettura semplice

**NEUTRALE / POCO CHIARO**  
**Forza segnale: 2/5**

DOGE: i futures non danno una lettura chiara. Non si vede uno sbilanciamento forte né long né short.

**Tradotto operativamente:** Qui pesa di più il report frattale.

### Perché

- funding positivo: i long pagano gli short
- open interest in aumento: più leva nel sistema
- long/short ratio alto: mercato più long

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $0.07830 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -1.94% | movimento dell'ultimo giorno |
| Funding | +0.0040% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-10-24 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $94.85M | leva aperta stimata in dollari |
| Open Interest 24h | +2.67% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 3.70 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $0.06264 | $0.09396 |
| 10x | $0.07047 | $0.08613 |
| 20x | $0.07438 | $0.08221 |
| 50x | $0.07673 | $0.07987 |

### Note tecniche usate dallo score

- open interest in aumento: leva in crescita
- long/short ratio alto: più mercato sbilanciato long

---
