# Report semplice futures / liquidazioni BTC / SOL / DOGE

Generato: **2026-09-07 07:32:40 CEST**  
UTC: **2026-09-07 05:32:40 UTC**

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
| BTC | 79.818 $ | -0.04% | +0.0053% | $2.12B | -5.52% | 1.16 |
| SOL | 105,54 $ | -0.32% | -0.0019% | $309.75M | -31.09% | 2.40 |
| DOGE | 0.09020 $ | -0.66% | +0.0100% | $94.26M | -14.70% | 5.12 |

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
| Prezzo | $79,809 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -0.04% | movimento dell'ultimo giorno |
| Funding | +0.0053% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-09-07 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $2.12B | leva aperta stimata in dollari |
| Open Interest 24h | -5.52% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.16 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $63,847 | $95,771 |
| 10x | $71,828 | $87,790 |
| 20x | $75,819 | $83,800 |
| 50x | $78,213 | $81,405 |

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
| Prezzo | $105.53 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -0.32% | movimento dell'ultimo giorno |
| Funding | -0.0019% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-09-07 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $309.75M | leva aperta stimata in dollari |
| Open Interest 24h | -31.09% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 2.40 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $84.42 | $126.64 |
| 10x | $94.98 | $116.08 |
| 20x | $100.25 | $110.81 |
| 50x | $103.42 | $107.64 |

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
| Prezzo | $0.09025 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -0.66% | movimento dell'ultimo giorno |
| Funding | +0.0100% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-09-07 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $94.26M | leva aperta stimata in dollari |
| Open Interest 24h | -14.70% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 5.12 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $0.07220 | $0.10830 |
| 10x | $0.08123 | $0.09928 |
| 20x | $0.08574 | $0.09476 |
| 50x | $0.08844 | $0.09205 |

### Note tecniche usate dallo score

- funding positivo: mercato leggermente carico di long
- open interest in forte calo: parte della leva è già uscita
- long/short ratio alto: più mercato sbilanciato long

---
