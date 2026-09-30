# Report semplice futures / liquidazioni BTC / SOL / DOGE

Generato: **2026-09-30 07:32:44 CEST**  
UTC: **2026-09-30 05:32:44 UTC**

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
| BTC | 83.353 $ | +0.31% | +0.0034% | $2.36B | -9.09% | 1.15 |
| SOL | 119,12 $ | +1.47% | -0.0053% | $354.48M | -7.18% | 1.83 |
| DOGE | 0.09370 $ | +0.83% | +0.0100% | $94.64M | -10.65% | 4.15 |

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
| Prezzo | $83,410 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +0.31% | movimento dell'ultimo giorno |
| Funding | +0.0034% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-09-30 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $2.36B | leva aperta stimata in dollari |
| Open Interest 24h | -9.09% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.15 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $66,728 | $100,092 |
| 10x | $75,069 | $91,751 |
| 20x | $79,240 | $87,580 |
| 50x | $81,742 | $85,078 |

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
| Prezzo | $119.31 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +1.47% | movimento dell'ultimo giorno |
| Funding | -0.0053% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-09-30 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $354.48M | leva aperta stimata in dollari |
| Open Interest 24h | -7.18% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.83 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $95.45 | $143.17 |
| 10x | $107.38 | $131.24 |
| 20x | $113.34 | $125.28 |
| 50x | $116.92 | $121.70 |

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
| Prezzo | $0.09395 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +0.83% | movimento dell'ultimo giorno |
| Funding | +0.0100% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-09-30 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $94.64M | leva aperta stimata in dollari |
| Open Interest 24h | -10.65% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 4.15 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $0.07516 | $0.11274 |
| 10x | $0.08456 | $0.10335 |
| 20x | $0.08925 | $0.09865 |
| 50x | $0.09207 | $0.09583 |

### Note tecniche usate dallo score

- funding positivo: mercato leggermente carico di long
- open interest in forte calo: parte della leva è già uscita
- long/short ratio alto: più mercato sbilanciato long

---
