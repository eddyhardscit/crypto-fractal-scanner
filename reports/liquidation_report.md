# Report semplice futures / liquidazioni BTC / SOL / DOGE

Generato: **2026-07-05 15:27:20 CEST**  
UTC: **2026-07-05 13:27:20 UTC**

Fonte dati: **OKX Futures pubblici**.  
Questo report non è la vera heatmap CoinGlass. Serve a capire se il mercato futures è carico di long, short o leva.

## Traduzione in parole semplici

| Asset | Lettura | Forza | Cosa significa in pratica |
| --- | --- | --- | --- |
| BTC | Rischio sotto | 5/5 | Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale. |
| SOL | Misto | 1/5 | Qui pesa di più il report frattale. |
| DOGE | Leva alta, direzione mista | 3/5 | Meglio non forzare. Aspetta conferma dal frattale o dal prezzo. |

## Numeri principali

| Asset | Prezzo | Prezzo 24h | Funding | Open Interest | OI 24h | Long/Short |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | $62,699 | +0.13% | +0.0031% | $1.95B | +14.02% | 1.95 |
| SOL | $80.77 | -1.03% | +0.0016% | $274.29M | -21.82% | 3.19 |
| DOGE | $0.07645 | -0.88% | +0.0007% | $73.36M | +9.28% | 3.90 |

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

**RISCHIO DISCESA / FLUSH SOTTO**  
**Forza segnale: 5/5**

BTC: i futures sembrano più vulnerabili verso una discesa improvvisa. Non significa che deve scendere, ma se rompe sotto può accelerare.

**Tradotto operativamente:** Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale.

### Perché

- funding positivo: i long pagano gli short
- open interest in aumento: più leva nel sistema
- long/short ratio alto: mercato più long

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $62,699 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +0.13% | movimento dell'ultimo giorno |
| Funding | +0.0031% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-05 18:00 | prossimo aggiornamento funding |
| Open Interest stimato | $1.95B | leva aperta stimata in dollari |
| Open Interest 24h | +14.02% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.95 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $50,159 | $75,238 |
| 10x | $56,429 | $68,968 |
| 20x | $59,564 | $65,834 |
| 50x | $61,445 | $63,953 |

### Note tecniche usate dallo score

- open interest in forte aumento: entra molta leva
- prezzo su + leva su + funding positivo: rischio pulizia dei long sotto
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
| Prezzo | $80.77 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -1.03% | movimento dell'ultimo giorno |
| Funding | +0.0016% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-05 18:00 | prossimo aggiornamento funding |
| Open Interest stimato | $274.29M | leva aperta stimata in dollari |
| Open Interest 24h | -21.82% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 3.19 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $64.62 | $96.92 |
| 10x | $72.69 | $88.85 |
| 20x | $76.73 | $84.81 |
| 50x | $79.15 | $82.39 |

### Note tecniche usate dallo score

- open interest in forte calo: parte della leva è già uscita
- long/short ratio alto: più mercato sbilanciato long

---

## Dogecoin — DOGE

### Lettura semplice

**MOLTA LEVA MA DIREZIONE MISTA**  
**Forza segnale: 3/5**

DOGE: c'è molta leva nel mercato, ma la direzione non è pulita. Può arrivare un movimento violento, ma non è chiaro se sopra o sotto.

**Tradotto operativamente:** Meglio non forzare. Aspetta conferma dal frattale o dal prezzo.

### Perché

- funding positivo: i long pagano gli short
- open interest in aumento: più leva nel sistema
- long/short ratio alto: mercato più long

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $0.07645 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -0.88% | movimento dell'ultimo giorno |
| Funding | +0.0007% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-05 18:00 | prossimo aggiornamento funding |
| Open Interest stimato | $73.36M | leva aperta stimata in dollari |
| Open Interest 24h | +9.28% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 3.90 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $0.06116 | $0.09174 |
| 10x | $0.06881 | $0.08410 |
| 20x | $0.07263 | $0.08027 |
| 50x | $0.07492 | $0.07798 |

### Note tecniche usate dallo score

- open interest in forte aumento: entra molta leva
- long/short ratio alto: più mercato sbilanciato long

---
