# Report semplice futures / liquidazioni BTC / SOL / DOGE

Generato: **2026-07-10 13:50:31 CEST**  
UTC: **2026-07-10 11:50:31 UTC**

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
| BTC | $64,418 | +2.82% | +0.0065% | $2.02B | -0.24% | 1.95 |
| SOL | $79.37 | +2.44% | +0.0014% | $245.17M | -21.94% | 2.64 |
| DOGE | $0.07429 | +2.64% | +0.0100% | $69.98M | -1.88% | 3.01 |

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
| Prezzo | $64,418 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +2.82% | movimento dell'ultimo giorno |
| Funding | +0.0065% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-10 18:00 | prossimo aggiornamento funding |
| Open Interest stimato | $2.02B | leva aperta stimata in dollari |
| Open Interest 24h | -0.24% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.95 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $51,535 | $77,302 |
| 10x | $57,976 | $70,860 |
| 20x | $61,197 | $67,639 |
| 50x | $63,130 | $65,707 |

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
| Prezzo | $79.37 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +2.44% | movimento dell'ultimo giorno |
| Funding | +0.0014% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-10 18:00 | prossimo aggiornamento funding |
| Open Interest stimato | $245.17M | leva aperta stimata in dollari |
| Open Interest 24h | -21.94% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 2.64 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $63.50 | $95.24 |
| 10x | $71.43 | $87.31 |
| 20x | $75.40 | $83.34 |
| 50x | $77.78 | $80.96 |

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
- open interest abbastanza stabile
- long/short ratio alto: mercato più long

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $0.07429 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +2.64% | movimento dell'ultimo giorno |
| Funding | +0.0100% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-10 18:00 | prossimo aggiornamento funding |
| Open Interest stimato | $69.98M | leva aperta stimata in dollari |
| Open Interest 24h | -1.88% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 3.01 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $0.05943 | $0.08915 |
| 10x | $0.06686 | $0.08172 |
| 20x | $0.07058 | $0.07800 |
| 50x | $0.07280 | $0.07578 |

### Note tecniche usate dallo score

- funding positivo: mercato leggermente carico di long
- long/short ratio alto: più mercato sbilanciato long

---
