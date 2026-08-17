# Report semplice futures / liquidazioni BTC / SOL / DOGE

Generato: **2026-08-17 07:32:30 CEST**  
UTC: **2026-08-17 05:32:30 UTC**

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
| BTC | 63.429 $ | +0.66% | +0.0060% | $2.08B | -5.63% | 1.62 |
| SOL | 75,42 $ | +0.11% | -0.0072% | $220.08M | -1.18% | 2.71 |
| DOGE | 0.07010 $ | +0.65% | +0.0100% | $85.78M | -15.14% | 4.71 |

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
| Prezzo | $63,460 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +0.66% | movimento dell'ultimo giorno |
| Funding | +0.0060% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-08-17 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $2.08B | leva aperta stimata in dollari |
| Open Interest 24h | -5.63% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.62 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $50,768 | $76,152 |
| 10x | $57,114 | $69,806 |
| 20x | $60,287 | $66,633 |
| 50x | $62,191 | $64,729 |

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
- open interest abbastanza stabile
- long/short ratio alto: mercato più long

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $75.41 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +0.11% | movimento dell'ultimo giorno |
| Funding | -0.0072% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-08-17 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $220.08M | leva aperta stimata in dollari |
| Open Interest 24h | -1.18% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 2.71 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $60.33 | $90.49 |
| 10x | $67.87 | $82.95 |
| 20x | $71.64 | $79.18 |
| 50x | $73.90 | $76.92 |

### Note tecniche usate dallo score

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
| Prezzo | $0.07011 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +0.65% | movimento dell'ultimo giorno |
| Funding | +0.0100% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-08-17 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $85.78M | leva aperta stimata in dollari |
| Open Interest 24h | -15.14% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 4.71 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $0.05609 | $0.08413 |
| 10x | $0.06310 | $0.07712 |
| 20x | $0.06660 | $0.07362 |
| 50x | $0.06871 | $0.07151 |

### Note tecniche usate dallo score

- funding positivo: mercato leggermente carico di long
- open interest in forte calo: parte della leva è già uscita
- long/short ratio alto: più mercato sbilanciato long

---
