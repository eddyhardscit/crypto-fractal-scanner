# Report semplice futures / liquidazioni BTC / SOL / DOGE

Generato: **2026-07-11 06:13:39 CEST**  
UTC: **2026-07-11 04:13:39 UTC**

Fonte dati: **OKX Futures pubblici**.  
Questo report non è la vera heatmap CoinGlass. Serve a capire se il mercato futures è carico di long, short o leva.

## Traduzione in parole semplici

| Asset | Lettura | Forza | Cosa significa in pratica |
| --- | --- | --- | --- |
| BTC | Rischio sotto | 5/5 | Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale. |
| SOL | Misto | 1/5 | Qui pesa di più il report frattale. |
| DOGE | Rischio sotto | 2/5 | Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale. |

## Numeri principali

| Asset | Prezzo | Prezzo 24h | Funding | Open Interest | OI 24h | Long/Short |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 64.050 $ | +0.21% | +0.0011% | $1.96B | +5.93% | 1.55 |
| SOL | 77,63 $ | -1.65% | +0.0013% | $241.57M | -23.20% | 2.27 |
| DOGE | 0.07427 $ | +0.30% | +0.0100% | $68.86M | +0.54% | 2.40 |

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
| Prezzo | $64,089 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +0.21% | movimento dell'ultimo giorno |
| Funding | +0.0011% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-11 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $1.96B | leva aperta stimata in dollari |
| Open Interest 24h | +5.93% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.55 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $51,271 | $76,907 |
| 10x | $57,680 | $70,498 |
| 20x | $60,885 | $67,294 |
| 50x | $62,807 | $65,371 |

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
| Prezzo | $77.70 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -1.65% | movimento dell'ultimo giorno |
| Funding | +0.0013% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-11 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $241.57M | leva aperta stimata in dollari |
| Open Interest 24h | -23.20% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 2.27 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $62.16 | $93.24 |
| 10x | $69.93 | $85.47 |
| 20x | $73.81 | $81.59 |
| 50x | $76.15 | $79.25 |

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
| Prezzo | $0.07434 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +0.30% | movimento dell'ultimo giorno |
| Funding | +0.0100% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-11 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $68.86M | leva aperta stimata in dollari |
| Open Interest 24h | +0.54% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 2.40 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $0.05947 | $0.08921 |
| 10x | $0.06691 | $0.08177 |
| 20x | $0.07062 | $0.07806 |
| 50x | $0.07285 | $0.07583 |

### Note tecniche usate dallo score

- funding positivo: mercato leggermente carico di long
- long/short ratio alto: più mercato sbilanciato long

---
