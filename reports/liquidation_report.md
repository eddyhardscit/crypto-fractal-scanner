# Report semplice futures / liquidazioni BTC / SOL / DOGE

Generato: **2026-09-04 07:32:39 CEST**  
UTC: **2026-09-04 05:32:39 UTC**

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
| BTC | 80.956 $ | +4.67% | +0.0053% | $2.39B | -18.66% | 1.30 |
| SOL | 103,67 $ | +3.39% | -0.0031% | $294.92M | -30.64% | 2.62 |
| DOGE | 0.08695 $ | +5.44% | +0.0100% | $89.38M | -13.21% | 5.07 |

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
| Prezzo | $80,904 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +4.67% | movimento dell'ultimo giorno |
| Funding | +0.0053% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-09-04 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $2.39B | leva aperta stimata in dollari |
| Open Interest 24h | -18.66% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.30 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $64,724 | $97,085 |
| 10x | $72,814 | $88,995 |
| 20x | $76,859 | $84,950 |
| 50x | $79,286 | $82,522 |

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

- funding negativo: gli short pagano i long
- open interest in calo: leva in uscita
- long/short ratio alto: mercato più long

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $103.55 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +3.39% | movimento dell'ultimo giorno |
| Funding | -0.0031% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-09-04 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $294.92M | leva aperta stimata in dollari |
| Open Interest 24h | -30.64% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 2.62 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $82.84 | $124.26 |
| 10x | $93.19 | $113.91 |
| 20x | $98.37 | $108.73 |
| 50x | $101.48 | $105.62 |

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
| Prezzo | $0.08687 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +5.44% | movimento dell'ultimo giorno |
| Funding | +0.0100% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-09-04 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $89.38M | leva aperta stimata in dollari |
| Open Interest 24h | -13.21% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 5.07 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $0.06950 | $0.10424 |
| 10x | $0.07818 | $0.09556 |
| 20x | $0.08253 | $0.09121 |
| 50x | $0.08513 | $0.08861 |

### Note tecniche usate dallo score

- funding positivo: mercato leggermente carico di long
- open interest in forte calo: parte della leva è già uscita
- long/short ratio alto: più mercato sbilanciato long

---
