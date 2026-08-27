# Report semplice futures / liquidazioni BTC / SOL / DOGE

Generato: **2026-08-27 07:32:52 CEST**  
UTC: **2026-08-27 05:32:52 UTC**

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
| BTC | 78.653 $ | -0.60% | +0.0060% | $2.27B | -10.17% | 1.81 |
| SOL | 100,99 $ | +4.09% | +0.0100% | $317.20M | -34.34% | 2.79 |
| DOGE | 0.08650 $ | -0.61% | +0.0028% | $92.48M | -12.64% | 3.48 |

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
| Prezzo | $78,620 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -0.60% | movimento dell'ultimo giorno |
| Funding | +0.0060% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-08-27 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $2.27B | leva aperta stimata in dollari |
| Open Interest 24h | -10.17% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.81 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $62,896 | $94,344 |
| 10x | $70,758 | $86,482 |
| 20x | $74,689 | $82,551 |
| 50x | $77,048 | $80,192 |

### Note tecniche usate dallo score

- open interest in forte calo: parte della leva è già uscita
- long/short ratio alto: più mercato sbilanciato long

---

## Solana — SOL

### Lettura semplice

**RISCHIO DISCESA / FLUSH SOTTO**  
**Forza segnale: 2/5**

SOL: i futures sembrano più vulnerabili verso una discesa improvvisa. Non significa che deve scendere, ma se rompe sotto può accelerare.

**Tradotto operativamente:** Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale.

### Perché

- funding positivo: i long pagano gli short
- open interest in calo: leva in uscita
- long/short ratio alto: mercato più long

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $100.86 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +4.09% | movimento dell'ultimo giorno |
| Funding | +0.0100% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-08-27 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $317.20M | leva aperta stimata in dollari |
| Open Interest 24h | -34.34% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 2.79 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $80.69 | $121.03 |
| 10x | $90.77 | $110.95 |
| 20x | $95.82 | $105.90 |
| 50x | $98.84 | $102.88 |

### Note tecniche usate dallo score

- funding positivo: mercato leggermente carico di long
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
| Prezzo | $0.08627 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -0.61% | movimento dell'ultimo giorno |
| Funding | +0.0028% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-08-27 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $92.48M | leva aperta stimata in dollari |
| Open Interest 24h | -12.64% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 3.48 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $0.06902 | $0.10352 |
| 10x | $0.07764 | $0.09490 |
| 20x | $0.08196 | $0.09058 |
| 50x | $0.08454 | $0.08800 |

### Note tecniche usate dallo score

- open interest in forte calo: parte della leva è già uscita
- long/short ratio alto: più mercato sbilanciato long

---
