# Report semplice futures / liquidazioni BTC / SOL / DOGE

Generato: **2026-09-17 07:32:41 CEST**  
UTC: **2026-09-17 05:32:41 UTC**

Fonte dati: **OKX Futures pubblici**.  
Questo report non è la vera heatmap CoinGlass. Serve a capire se il mercato futures è carico di long, short o leva.

## Traduzione in parole semplici

| Asset | Lettura | Forza | Cosa significa in pratica |
| --- | --- | --- | --- |
| BTC | Misto | 1/5 | Qui pesa di più il report frattale. |
| SOL | Misto | 1/5 | Qui pesa di più il report frattale. |
| DOGE | Rischio sotto | 4/5 | Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale. |

## Numeri principali

| Asset | Prezzo | Prezzo 24h | Funding | Open Interest | OI 24h | Long/Short |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 76.403 $ | +0.77% | +0.0068% | $2.19B | -6.72% | 1.53 |
| SOL | 99,61 $ | +2.55% | +0.0031% | $262.17M | -17.27% | 2.34 |
| DOGE | 0.08094 $ | +0.91% | +0.0015% | $81.43M | +3.92% | 5.59 |

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
| Prezzo | $76,390 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +0.77% | movimento dell'ultimo giorno |
| Funding | +0.0068% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-09-17 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $2.19B | leva aperta stimata in dollari |
| Open Interest 24h | -6.72% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.53 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $61,112 | $91,668 |
| 10x | $68,751 | $84,029 |
| 20x | $72,571 | $80,210 |
| 50x | $74,862 | $77,918 |

### Note tecniche usate dallo score

- open interest in forte calo: parte della leva è già uscita
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
| Prezzo | $99.55 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +2.55% | movimento dell'ultimo giorno |
| Funding | +0.0031% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-09-17 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $262.17M | leva aperta stimata in dollari |
| Open Interest 24h | -17.27% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 2.34 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $79.64 | $119.46 |
| 10x | $89.59 | $109.51 |
| 20x | $94.57 | $104.53 |
| 50x | $97.56 | $101.54 |

### Note tecniche usate dallo score

- open interest in forte calo: parte della leva è già uscita
- long/short ratio alto: più mercato sbilanciato long

---

## Dogecoin — DOGE

### Lettura semplice

**RISCHIO DISCESA / FLUSH SOTTO**  
**Forza segnale: 4/5**

DOGE: i futures sembrano più vulnerabili verso una discesa improvvisa. Non significa che deve scendere, ma se rompe sotto può accelerare.

**Tradotto operativamente:** Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale.

### Perché

- funding positivo: i long pagano gli short
- open interest in aumento: più leva nel sistema
- long/short ratio alto: mercato più long

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $0.08087 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +0.91% | movimento dell'ultimo giorno |
| Funding | +0.0015% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-09-17 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $81.43M | leva aperta stimata in dollari |
| Open Interest 24h | +3.92% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 5.59 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $0.06470 | $0.09704 |
| 10x | $0.07278 | $0.08896 |
| 20x | $0.07683 | $0.08491 |
| 50x | $0.07925 | $0.08249 |

### Note tecniche usate dallo score

- open interest in aumento: leva in crescita
- prezzo su + leva su + funding positivo: rischio pulizia dei long sotto
- long/short ratio alto: più mercato sbilanciato long

---
