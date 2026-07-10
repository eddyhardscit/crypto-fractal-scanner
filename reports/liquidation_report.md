# Report semplice futures / liquidazioni BTC / SOL / DOGE

Generato: **2026-07-11 01:23:45 CEST**  
UTC: **2026-07-10 23:23:45 UTC**

Fonte dati: **OKX Futures pubblici**.  
Questo report non è la vera heatmap CoinGlass. Serve a capire se il mercato futures è carico di long, short o leva.

## Traduzione in parole semplici

| Asset | Lettura | Forza | Cosa significa in pratica |
| --- | --- | --- | --- |
| BTC | Rischio sotto | 4/5 | Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale. |
| SOL | Misto | 1/5 | Qui pesa di più il report frattale. |
| DOGE | Rischio sotto | 2/5 | Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale. |

## Numeri principali

| Asset | Prezzo | Prezzo 24h | Funding | Open Interest | OI 24h | Long/Short |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 64.082 $ | +1.42% | +0.0094% | $1.95B | +2.83% | 1.83 |
| SOL | 77,97 $ | +0.03% | +0.0041% | $241.06M | -22.34% | 2.90 |
| DOGE | 0.07404 $ | +1.49% | +0.0100% | $68.44M | -0.81% | 3.25 |

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
| Prezzo | $64,096 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +1.42% | movimento dell'ultimo giorno |
| Funding | +0.0094% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-11 02:00 | prossimo aggiornamento funding |
| Open Interest stimato | $1.95B | leva aperta stimata in dollari |
| Open Interest 24h | +2.83% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.83 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $51,277 | $76,915 |
| 10x | $57,686 | $70,505 |
| 20x | $60,891 | $67,300 |
| 50x | $62,814 | $65,378 |

### Note tecniche usate dallo score

- open interest in aumento: leva in crescita
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
| Prezzo | $77.99 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +0.03% | movimento dell'ultimo giorno |
| Funding | +0.0041% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-11 02:00 | prossimo aggiornamento funding |
| Open Interest stimato | $241.06M | leva aperta stimata in dollari |
| Open Interest 24h | -22.34% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 2.90 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $62.39 | $93.59 |
| 10x | $70.19 | $85.79 |
| 20x | $74.09 | $81.89 |
| 50x | $76.43 | $79.55 |

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
| Prezzo | $0.07405 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +1.49% | movimento dell'ultimo giorno |
| Funding | +0.0100% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-11 02:00 | prossimo aggiornamento funding |
| Open Interest stimato | $68.44M | leva aperta stimata in dollari |
| Open Interest 24h | -0.81% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 3.25 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $0.05924 | $0.08886 |
| 10x | $0.06665 | $0.08146 |
| 20x | $0.07035 | $0.07775 |
| 50x | $0.07257 | $0.07553 |

### Note tecniche usate dallo score

- funding positivo: mercato leggermente carico di long
- long/short ratio alto: più mercato sbilanciato long

---
