# Report semplice futures / liquidazioni BTC / SOL / DOGE

Generato: **2026-07-11 03:13:10 CEST**  
UTC: **2026-07-11 01:13:10 UTC**

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
| BTC | 64.070 $ | +1.69% | +0.0059% | $1.95B | +3.87% | 1.78 |
| SOL | 77,73 $ | -0.46% | -0.0000% | $242.07M | -22.88% | 2.80 |
| DOGE | 0.07408 $ | +1.67% | +0.0100% | $68.51M | -0.25% | 3.17 |

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
| Prezzo | $64,109 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +1.69% | movimento dell'ultimo giorno |
| Funding | +0.0059% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-11 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $1.95B | leva aperta stimata in dollari |
| Open Interest 24h | +3.87% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.78 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $51,288 | $76,931 |
| 10x | $57,698 | $70,520 |
| 20x | $60,904 | $67,315 |
| 50x | $62,827 | $65,392 |

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

- funding negativo: gli short pagano i long
- open interest in calo: leva in uscita
- long/short ratio alto: mercato più long

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $77.75 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -0.46% | movimento dell'ultimo giorno |
| Funding | -0.0000% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-11 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $242.07M | leva aperta stimata in dollari |
| Open Interest 24h | -22.88% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 2.80 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $62.20 | $93.30 |
| 10x | $69.98 | $85.53 |
| 20x | $73.86 | $81.64 |
| 50x | $76.19 | $79.31 |

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
| Prezzo | $0.07411 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +1.67% | movimento dell'ultimo giorno |
| Funding | +0.0100% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-11 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $68.51M | leva aperta stimata in dollari |
| Open Interest 24h | -0.25% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 3.17 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $0.05929 | $0.08893 |
| 10x | $0.06670 | $0.08152 |
| 20x | $0.07040 | $0.07782 |
| 50x | $0.07263 | $0.07559 |

### Note tecniche usate dallo score

- funding positivo: mercato leggermente carico di long
- long/short ratio alto: più mercato sbilanciato long

---
