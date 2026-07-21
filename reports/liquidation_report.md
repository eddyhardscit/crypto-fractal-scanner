# Report semplice futures / liquidazioni BTC / SOL / DOGE

Generato: **2026-07-21 07:14:32 CEST**  
UTC: **2026-07-21 05:14:32 UTC**

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
| BTC | 65.472 $ | +2.00% | +0.0015% | $2.05B | -0.54% | 1.40 |
| SOL | 78,18 $ | +2.92% | +0.0069% | $228.36M | -16.15% | 2.18 |
| DOGE | 0.07277 $ | +1.39% | +0.0100% | $79.29M | -5.58% | 4.48 |

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
| Prezzo | $65,493 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +2.00% | movimento dell'ultimo giorno |
| Funding | +0.0015% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-21 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $2.05B | leva aperta stimata in dollari |
| Open Interest 24h | -0.54% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.40 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $52,395 | $78,592 |
| 10x | $58,944 | $72,043 |
| 20x | $62,219 | $68,768 |
| 50x | $64,184 | $66,803 |

### Note tecniche usate dallo score

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
| Prezzo | $78.24 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +2.92% | movimento dell'ultimo giorno |
| Funding | +0.0069% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-21 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $228.36M | leva aperta stimata in dollari |
| Open Interest 24h | -16.15% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 2.18 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $62.59 | $93.89 |
| 10x | $70.42 | $86.06 |
| 20x | $74.33 | $82.15 |
| 50x | $76.68 | $79.80 |

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
| Prezzo | $0.07283 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +1.39% | movimento dell'ultimo giorno |
| Funding | +0.0100% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-21 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $79.29M | leva aperta stimata in dollari |
| Open Interest 24h | -5.58% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 4.48 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $0.05826 | $0.08740 |
| 10x | $0.06555 | $0.08011 |
| 20x | $0.06919 | $0.07647 |
| 50x | $0.07137 | $0.07429 |

### Note tecniche usate dallo score

- funding positivo: mercato leggermente carico di long
- open interest in forte calo: parte della leva è già uscita
- long/short ratio alto: più mercato sbilanciato long

---
