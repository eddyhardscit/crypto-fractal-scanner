# Report semplice futures / liquidazioni BTC / SOL / DOGE

Generato: **2026-07-11 21:00:13 CEST**  
UTC: **2026-07-11 19:00:13 UTC**

Fonte dati: **OKX Futures pubblici**.  
Questo report non è la vera heatmap CoinGlass. Serve a capire se il mercato futures è carico di long, short o leva.

## Traduzione in parole semplici

| Asset | Lettura | Forza | Cosa significa in pratica |
| --- | --- | --- | --- |
| BTC | Rischio sotto | 4/5 | Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale. |
| SOL | Rischio sotto | 2/5 | Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale. |
| DOGE | Rischio sotto | 2/5 | Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale. |

## Numeri principali

| Asset | Prezzo | Prezzo 24h | Funding | Open Interest | OI 24h | Long/Short |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 64.273 $ | +0.82% | +0.0065% | $2.00B | +2.06% | 1.44 |
| SOL | 78,01 $ | +0.79% | +0.0100% | $241.41M | -22.94% | 2.14 |
| DOGE | 0.07510 $ | +2.09% | +0.0100% | $70.72M | -0.01% | 2.34 |

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
**Forza segnale: 4/5**

BTC: i futures sembrano più vulnerabili verso una discesa improvvisa. Non significa che deve scendere, ma se rompe sotto può accelerare.

**Tradotto operativamente:** Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale.

### Perché

- funding positivo: i long pagano gli short
- open interest in aumento: più leva nel sistema
- long/short ratio alto: mercato più long

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $64,303 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +0.82% | movimento dell'ultimo giorno |
| Funding | +0.0065% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-12 02:00 | prossimo aggiornamento funding |
| Open Interest stimato | $2.00B | leva aperta stimata in dollari |
| Open Interest 24h | +2.06% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.44 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $51,442 | $77,163 |
| 10x | $57,872 | $70,733 |
| 20x | $61,087 | $67,518 |
| 50x | $63,017 | $65,589 |

### Note tecniche usate dallo score

- open interest in aumento: leva in crescita
- prezzo su + leva su + funding positivo: rischio pulizia dei long sotto
- long/short ratio alto: più mercato sbilanciato long

---

## Solana — SOL

### Lettura semplice

**RISCHIO DISCESA / FLUSH SOTTO**  
**Forza segnale: 2/5**

SOL: i futures sembrano più vulnerabili verso una discesa improvvisa. Non significa che deve scendere, ma se rompe sotto può accelerare.

**Tradotto operativamente:** Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale.

### Perché

- funding positivo: i long pagano gli short
- open interest in calo: leva in uscita
- long/short ratio alto: mercato più long

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $78.05 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +0.79% | movimento dell'ultimo giorno |
| Funding | +0.0100% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-12 02:00 | prossimo aggiornamento funding |
| Open Interest stimato | $241.41M | leva aperta stimata in dollari |
| Open Interest 24h | -22.94% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 2.14 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $62.44 | $93.66 |
| 10x | $70.25 | $85.86 |
| 20x | $74.15 | $81.95 |
| 50x | $76.49 | $79.61 |

### Note tecniche usate dallo score

- funding positivo: mercato leggermente carico di long
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
| Prezzo | $0.07521 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +2.09% | movimento dell'ultimo giorno |
| Funding | +0.0100% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-12 02:00 | prossimo aggiornamento funding |
| Open Interest stimato | $70.72M | leva aperta stimata in dollari |
| Open Interest 24h | -0.01% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 2.34 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $0.06017 | $0.09025 |
| 10x | $0.06769 | $0.08273 |
| 20x | $0.07145 | $0.07897 |
| 50x | $0.07371 | $0.07671 |

### Note tecniche usate dallo score

- funding positivo: mercato leggermente carico di long
- long/short ratio alto: più mercato sbilanciato long

---
