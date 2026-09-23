# Report semplice futures / liquidazioni BTC / SOL / DOGE

Generato: **2026-09-23 07:32:40 CEST**  
UTC: **2026-09-23 05:32:40 UTC**

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
| BTC | 86.751 $ | +1.87% | +0.0020% | $2.60B | -12.36% | 1.10 |
| SOL | 118,95 $ | +2.86% | +0.0035% | $368.41M | -23.90% | 1.99 |
| DOGE | 0.10210 $ | +3.66% | +0.0100% | $117.48M | -11.50% | 3.13 |

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
| Prezzo | $86,688 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +1.87% | movimento dell'ultimo giorno |
| Funding | +0.0020% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-09-23 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $2.60B | leva aperta stimata in dollari |
| Open Interest 24h | -12.36% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.10 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $69,351 | $104,026 |
| 10x | $78,020 | $95,357 |
| 20x | $82,354 | $91,023 |
| 50x | $84,955 | $88,422 |

### Note tecniche usate dallo score

- open interest in forte calo: parte della leva è già uscita

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
| Prezzo | $118.86 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +2.86% | movimento dell'ultimo giorno |
| Funding | +0.0035% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-09-23 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $368.41M | leva aperta stimata in dollari |
| Open Interest 24h | -23.90% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.99 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $95.09 | $142.63 |
| 10x | $106.97 | $130.75 |
| 20x | $112.92 | $124.80 |
| 50x | $116.48 | $121.24 |

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
- open interest in calo: leva in uscita
- long/short ratio alto: mercato più long

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $0.10218 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +3.66% | movimento dell'ultimo giorno |
| Funding | +0.0100% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-09-23 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $117.48M | leva aperta stimata in dollari |
| Open Interest 24h | -11.50% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 3.13 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $0.08174 | $0.12262 |
| 10x | $0.09196 | $0.11240 |
| 20x | $0.09707 | $0.10729 |
| 50x | $0.10014 | $0.10422 |

### Note tecniche usate dallo score

- funding positivo: mercato leggermente carico di long
- open interest in forte calo: parte della leva è già uscita
- long/short ratio alto: più mercato sbilanciato long

---
