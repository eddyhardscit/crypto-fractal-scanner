# Report semplice futures / liquidazioni BTC / SOL / DOGE

Generato: **2026-10-06 07:32:53 CEST**  
UTC: **2026-10-06 05:32:53 UTC**

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
| BTC | 85.668 $ | +0.18% | +0.0069% | $2.48B | n/d | 1.12 |
| SOL | 120,12 $ | -0.05% | +0.0072% | $352.76M | n/d | 1.85 |
| DOGE | 0.09490 $ | -0.03% | +0.0100% | $100.77M | n/d | 3.56 |

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
- long/short ratio abbastanza equilibrato

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $85,607 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +0.18% | movimento dell'ultimo giorno |
| Funding | +0.0069% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-10-06 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $2.48B | leva aperta stimata in dollari |
| Open Interest 24h | n/d | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.12 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $68,486 | $102,729 |
| 10x | $77,047 | $94,168 |
| 20x | $81,327 | $89,888 |
| 50x | $83,895 | $87,320 |

---

## Solana — SOL

### Lettura semplice

**NEUTRALE / POCO CHIARO**  
**Forza segnale: 1/5**

SOL: i futures non danno una lettura chiara. Non si vede uno sbilanciamento forte né long né short.

**Tradotto operativamente:** Qui pesa di più il report frattale.

### Perché

- funding positivo: i long pagano gli short
- long/short ratio alto: mercato più long

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $119.99 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -0.05% | movimento dell'ultimo giorno |
| Funding | +0.0072% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-10-06 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $352.76M | leva aperta stimata in dollari |
| Open Interest 24h | n/d | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.85 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $95.99 | $143.99 |
| 10x | $107.99 | $131.99 |
| 20x | $113.99 | $125.99 |
| 50x | $117.59 | $122.39 |

### Note tecniche usate dallo score

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
- long/short ratio alto: mercato più long

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $0.09486 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -0.03% | movimento dell'ultimo giorno |
| Funding | +0.0100% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-10-06 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $100.77M | leva aperta stimata in dollari |
| Open Interest 24h | n/d | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 3.56 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $0.07589 | $0.11383 |
| 10x | $0.08537 | $0.10435 |
| 20x | $0.09012 | $0.09960 |
| 50x | $0.09296 | $0.09676 |

### Note tecniche usate dallo score

- funding positivo: mercato leggermente carico di long
- long/short ratio alto: più mercato sbilanciato long

---
