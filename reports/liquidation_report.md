# Report semplice futures / liquidazioni BTC / SOL / DOGE

Generato: **2026-09-28 07:32:41 CEST**  
UTC: **2026-09-28 05:32:41 UTC**

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
| BTC | 83.028 $ | -1.66% | +0.0008% | $2.40B | -8.42% | 1.21 |
| SOL | 119,07 $ | -1.69% | +0.0033% | $365.36M | -8.30% | 1.60 |
| DOGE | 0.09336 $ | -3.05% | +0.0100% | $98.98M | -13.62% | 3.88 |

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
| Prezzo | $82,988 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -1.66% | movimento dell'ultimo giorno |
| Funding | +0.0008% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-09-28 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $2.40B | leva aperta stimata in dollari |
| Open Interest 24h | -8.42% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.21 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $66,391 | $99,586 |
| 10x | $74,689 | $91,287 |
| 20x | $78,839 | $87,138 |
| 50x | $81,329 | $84,648 |

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
| Prezzo | $118.60 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -1.69% | movimento dell'ultimo giorno |
| Funding | +0.0033% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-09-28 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $365.36M | leva aperta stimata in dollari |
| Open Interest 24h | -8.30% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.60 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $94.88 | $142.32 |
| 10x | $106.74 | $130.46 |
| 20x | $112.67 | $124.53 |
| 50x | $116.23 | $120.97 |

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
| Prezzo | $0.09300 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -3.05% | movimento dell'ultimo giorno |
| Funding | +0.0100% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-09-28 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $98.98M | leva aperta stimata in dollari |
| Open Interest 24h | -13.62% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 3.88 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $0.07440 | $0.11160 |
| 10x | $0.08370 | $0.10230 |
| 20x | $0.08835 | $0.09765 |
| 50x | $0.09114 | $0.09486 |

### Note tecniche usate dallo score

- funding positivo: mercato leggermente carico di long
- open interest in forte calo: parte della leva è già uscita
- long/short ratio alto: più mercato sbilanciato long

---
