# Report semplice futures / liquidazioni BTC / SOL / DOGE

Generato: **2026-09-01 07:32:58 CEST**  
UTC: **2026-09-01 05:32:58 UTC**

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
| BTC | 78.947 $ | +1.30% | +0.0067% | $2.16B | -10.72% | 2.01 |
| SOL | 103,93 $ | +1.48% | -0.0019% | $321.49M | -33.94% | 2.82 |
| DOGE | 0.08338 $ | +0.83% | +0.0021% | $84.50M | +2.19% | 5.07 |

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
| Prezzo | $78,992 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +1.30% | movimento dell'ultimo giorno |
| Funding | +0.0067% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-09-01 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $2.16B | leva aperta stimata in dollari |
| Open Interest 24h | -10.72% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 2.01 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $63,194 | $94,791 |
| 10x | $71,093 | $86,891 |
| 20x | $75,043 | $82,942 |
| 50x | $77,412 | $80,572 |

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
| Prezzo | $104.02 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +1.48% | movimento dell'ultimo giorno |
| Funding | -0.0019% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-09-01 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $321.49M | leva aperta stimata in dollari |
| Open Interest 24h | -33.94% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 2.82 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $83.22 | $124.82 |
| 10x | $93.62 | $114.42 |
| 20x | $98.82 | $109.22 |
| 50x | $101.94 | $106.10 |

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
| Prezzo | $0.08344 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +0.83% | movimento dell'ultimo giorno |
| Funding | +0.0021% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-09-01 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $84.50M | leva aperta stimata in dollari |
| Open Interest 24h | +2.19% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 5.07 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $0.06675 | $0.10013 |
| 10x | $0.07510 | $0.09178 |
| 20x | $0.07927 | $0.08761 |
| 50x | $0.08177 | $0.08511 |

### Note tecniche usate dallo score

- open interest in aumento: leva in crescita
- prezzo su + leva su + funding positivo: rischio pulizia dei long sotto
- long/short ratio alto: più mercato sbilanciato long

---
