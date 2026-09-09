# Report semplice futures / liquidazioni BTC / SOL / DOGE

Generato: **2026-09-09 07:32:43 CEST**  
UTC: **2026-09-09 05:32:43 UTC**

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
| BTC | 79.123 $ | +0.27% | +0.0043% | $2.15B | -5.32% | 1.24 |
| SOL | 104,43 $ | +0.93% | -0.0046% | $293.75M | -17.50% | 1.87 |
| DOGE | 0.09043 $ | +0.16% | +0.0100% | $90.28M | -9.55% | 5.38 |

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
| Prezzo | $78,933 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +0.27% | movimento dell'ultimo giorno |
| Funding | +0.0043% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-09-09 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $2.15B | leva aperta stimata in dollari |
| Open Interest 24h | -5.32% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.24 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $63,146 | $94,720 |
| 10x | $71,040 | $86,826 |
| 20x | $74,986 | $82,880 |
| 50x | $77,354 | $80,512 |

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

- funding negativo: gli short pagano i long
- open interest in calo: leva in uscita
- long/short ratio alto: mercato più long

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $104.20 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +0.93% | movimento dell'ultimo giorno |
| Funding | -0.0046% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-09-09 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $293.75M | leva aperta stimata in dollari |
| Open Interest 24h | -17.50% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.87 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $83.36 | $125.04 |
| 10x | $93.78 | $114.62 |
| 20x | $98.99 | $109.41 |
| 50x | $102.12 | $106.28 |

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
| Prezzo | $0.09013 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +0.16% | movimento dell'ultimo giorno |
| Funding | +0.0100% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-09-09 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $90.28M | leva aperta stimata in dollari |
| Open Interest 24h | -9.55% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 5.38 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $0.07210 | $0.10816 |
| 10x | $0.08112 | $0.09914 |
| 20x | $0.08562 | $0.09464 |
| 50x | $0.08833 | $0.09193 |

### Note tecniche usate dallo score

- funding positivo: mercato leggermente carico di long
- open interest in forte calo: parte della leva è già uscita
- long/short ratio alto: più mercato sbilanciato long

---
