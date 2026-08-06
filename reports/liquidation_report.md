# Report semplice futures / liquidazioni BTC / SOL / DOGE

Generato: **2026-08-06 07:15:41 CEST**  
UTC: **2026-08-06 05:15:41 UTC**

Fonte dati: **OKX Futures pubblici**.  
Questo report non è la vera heatmap CoinGlass. Serve a capire se il mercato futures è carico di long, short o leva.

## Traduzione in parole semplici

| Asset | Lettura | Forza | Cosa significa in pratica |
| --- | --- | --- | --- |
| BTC | Misto | 1/5 | Qui pesa di più il report frattale. |
| SOL | Rischio sotto | 5/5 | Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale. |
| DOGE | Misto | 1/5 | Qui pesa di più il report frattale. |

## Numeri principali

| Asset | Prezzo | Prezzo 24h | Funding | Open Interest | OI 24h | Long/Short |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 64.848 $ | +0.94% | +0.0095% | $2.01B | -2.63% | 1.44 |
| SOL | 74,13 $ | +0.34% | +0.0029% | $209.98M | +19.02% | 1.73 |
| DOGE | 0.06998 $ | +0.07% | +0.0094% | $80.17M | -18.78% | 3.25 |

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
| Prezzo | $64,885 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +0.94% | movimento dell'ultimo giorno |
| Funding | +0.0095% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-08-06 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $2.01B | leva aperta stimata in dollari |
| Open Interest 24h | -2.63% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.44 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $51,908 | $77,862 |
| 10x | $58,397 | $71,374 |
| 20x | $61,641 | $68,129 |
| 50x | $63,587 | $66,183 |

### Note tecniche usate dallo score

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
| Prezzo | $74.15 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +0.34% | movimento dell'ultimo giorno |
| Funding | +0.0029% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-08-06 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $209.98M | leva aperta stimata in dollari |
| Open Interest 24h | +19.02% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.73 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $59.32 | $88.98 |
| 10x | $66.74 | $81.57 |
| 20x | $70.44 | $77.86 |
| 50x | $72.67 | $75.63 |

### Note tecniche usate dallo score

- open interest in forte aumento: entra molta leva
- prezzo su + leva su + funding positivo: rischio pulizia dei long sotto
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
| Prezzo | $0.07000 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +0.07% | movimento dell'ultimo giorno |
| Funding | +0.0094% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-08-06 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $80.17M | leva aperta stimata in dollari |
| Open Interest 24h | -18.78% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 3.25 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $0.05600 | $0.08400 |
| 10x | $0.06300 | $0.07700 |
| 20x | $0.06650 | $0.07350 |
| 50x | $0.06860 | $0.07140 |

### Note tecniche usate dallo score

- open interest in forte calo: parte della leva è già uscita
- long/short ratio alto: più mercato sbilanciato long

---
