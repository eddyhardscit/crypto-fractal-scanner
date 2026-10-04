# Report semplice futures / liquidazioni BTC / SOL / DOGE

Generato: **2026-10-04 07:32:41 CEST**  
UTC: **2026-10-04 05:32:41 UTC**

Fonte dati: **OKX Futures pubblici**.  
Questo report non è la vera heatmap CoinGlass. Serve a capire se il mercato futures è carico di long, short o leva.

## Traduzione in parole semplici

| Asset | Lettura | Forza | Cosa significa in pratica |
| --- | --- | --- | --- |
| BTC | Misto | 1/5 | Qui pesa di più il report frattale. |
| SOL | Rischio sotto | 2/5 | Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale. |
| DOGE | Misto | 1/5 | Qui pesa di più il report frattale. |

## Numeri principali

| Asset | Prezzo | Prezzo 24h | Funding | Open Interest | OI 24h | Long/Short |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 84.844 $ | +0.26% | +0.0037% | $2.41B | n/d | 0.90 |
| SOL | 120,74 $ | +0.96% | +0.0100% | $362.16M | n/d | 1.97 |
| DOGE | 0.09278 $ | -0.50% | +0.0021% | $103.01M | n/d | 3.33 |

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
| Prezzo | $84,823 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +0.26% | movimento dell'ultimo giorno |
| Funding | +0.0037% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-10-04 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $2.41B | leva aperta stimata in dollari |
| Open Interest 24h | n/d | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 0.90 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $67,858 | $101,787 |
| 10x | $76,341 | $93,305 |
| 20x | $80,582 | $89,064 |
| 50x | $83,126 | $86,519 |

---

## Solana — SOL

### Lettura semplice

**RISCHIO DISCESA / FLUSH SOTTO**  
**Forza segnale: 2/5**

SOL: i futures sembrano più vulnerabili verso una discesa improvvisa. Non significa che deve scendere, ma se rompe sotto può accelerare.

**Tradotto operativamente:** Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale.

### Perché

- funding positivo: i long pagano gli short
- long/short ratio alto: mercato più long

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $120.72 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +0.96% | movimento dell'ultimo giorno |
| Funding | +0.0100% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-10-04 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $362.16M | leva aperta stimata in dollari |
| Open Interest 24h | n/d | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.97 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $96.58 | $144.86 |
| 10x | $108.65 | $132.79 |
| 20x | $114.68 | $126.76 |
| 50x | $118.31 | $123.13 |

### Note tecniche usate dallo score

- funding positivo: mercato leggermente carico di long
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
- long/short ratio alto: mercato più long

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $0.09271 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -0.50% | movimento dell'ultimo giorno |
| Funding | +0.0021% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-10-04 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $103.01M | leva aperta stimata in dollari |
| Open Interest 24h | n/d | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 3.33 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $0.07417 | $0.11125 |
| 10x | $0.08344 | $0.10198 |
| 20x | $0.08807 | $0.09735 |
| 50x | $0.09086 | $0.09456 |

### Note tecniche usate dallo score

- long/short ratio alto: più mercato sbilanciato long

---
