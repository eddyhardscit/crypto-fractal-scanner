# Report semplice futures / liquidazioni BTC / SOL / DOGE

Generato: **2026-08-05 07:15:39 CEST**  
UTC: **2026-08-05 05:15:39 UTC**

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
| BTC | 64.258 $ | +0.66% | +0.0049% | $1.98B | -1.39% | 1.54 |
| SOL | 73,91 $ | +0.30% | +0.0043% | $208.23M | +26.08% | 1.71 |
| DOGE | 0.06992 $ | -0.36% | +0.0072% | $78.93M | -15.37% | 3.04 |

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
| Prezzo | $64,276 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +0.66% | movimento dell'ultimo giorno |
| Funding | +0.0049% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-08-05 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $1.98B | leva aperta stimata in dollari |
| Open Interest 24h | -1.39% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.54 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $51,421 | $77,131 |
| 10x | $57,848 | $70,704 |
| 20x | $61,062 | $67,490 |
| 50x | $62,991 | $65,562 |

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
| Prezzo | $73.91 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +0.30% | movimento dell'ultimo giorno |
| Funding | +0.0043% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-08-05 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $208.23M | leva aperta stimata in dollari |
| Open Interest 24h | +26.08% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.71 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $59.13 | $88.69 |
| 10x | $66.52 | $81.30 |
| 20x | $70.21 | $77.61 |
| 50x | $72.43 | $75.39 |

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
| Prezzo | $0.06995 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -0.36% | movimento dell'ultimo giorno |
| Funding | +0.0072% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-08-05 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $78.93M | leva aperta stimata in dollari |
| Open Interest 24h | -15.37% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 3.04 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $0.05596 | $0.08394 |
| 10x | $0.06295 | $0.07694 |
| 20x | $0.06645 | $0.07345 |
| 50x | $0.06855 | $0.07135 |

### Note tecniche usate dallo score

- open interest in forte calo: parte della leva è già uscita
- long/short ratio alto: più mercato sbilanciato long

---
