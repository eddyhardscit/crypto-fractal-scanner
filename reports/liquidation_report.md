# Report semplice futures / liquidazioni BTC / SOL / DOGE

Generato: **2026-10-04 16:40:30 CEST**  
UTC: **2026-10-04 14:40:30 UTC**

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
| BTC | 85.128 $ | +0.45% | +0.0038% | $2.42B | n/d | 1.03 |
| SOL | 121,45 $ | +1.72% | +0.0100% | $373.65M | n/d | 1.94 |
| DOGE | 0.09358 $ | +0.65% | +0.0020% | $101.12M | n/d | 4.12 |

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
| Prezzo | $85,098 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +0.45% | movimento dell'ultimo giorno |
| Funding | +0.0038% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-10-04 18:00 | prossimo aggiornamento funding |
| Open Interest stimato | $2.42B | leva aperta stimata in dollari |
| Open Interest 24h | n/d | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.03 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $68,078 | $102,118 |
| 10x | $76,588 | $93,608 |
| 20x | $80,843 | $89,353 |
| 50x | $83,396 | $86,800 |

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
| Prezzo | $121.42 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +1.72% | movimento dell'ultimo giorno |
| Funding | +0.0100% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-10-04 18:00 | prossimo aggiornamento funding |
| Open Interest stimato | $373.65M | leva aperta stimata in dollari |
| Open Interest 24h | n/d | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.94 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $97.14 | $145.70 |
| 10x | $109.28 | $133.56 |
| 20x | $115.35 | $127.49 |
| 50x | $118.99 | $123.85 |

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
| Prezzo | $0.09360 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +0.65% | movimento dell'ultimo giorno |
| Funding | +0.0020% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-10-04 18:00 | prossimo aggiornamento funding |
| Open Interest stimato | $101.12M | leva aperta stimata in dollari |
| Open Interest 24h | n/d | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 4.12 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $0.07488 | $0.11232 |
| 10x | $0.08424 | $0.10296 |
| 20x | $0.08892 | $0.09828 |
| 50x | $0.09173 | $0.09547 |

### Note tecniche usate dallo score

- long/short ratio alto: più mercato sbilanciato long

---
