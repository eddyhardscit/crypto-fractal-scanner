# Report semplice futures / liquidazioni BTC / SOL / DOGE

Generato: **2026-07-10 19:49:26 CEST**  
UTC: **2026-07-10 17:49:26 UTC**

Fonte dati: **OKX Futures pubblici**.  
Questo report non è la vera heatmap CoinGlass. Serve a capire se il mercato futures è carico di long, short o leva.

## Traduzione in parole semplici

| Asset | Lettura | Forza | Cosa significa in pratica |
| --- | --- | --- | --- |
| BTC | Rischio sotto | 5/5 | Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale. |
| SOL | Misto | 1/5 | Qui pesa di più il report frattale. |
| DOGE | Misto | 1/5 | Qui pesa di più il report frattale. |

## Numeri principali

| Asset | Prezzo | Prezzo 24h | Funding | Open Interest | OI 24h | Long/Short |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | $63,891 | +1.32% | +0.0100% | $1.97B | +3.02% | 1.84 |
| SOL | $77.76 | -0.32% | +0.0091% | $243.12M | -23.02% | 2.71 |
| DOGE | $0.07395 | +1.40% | +0.0073% | $68.03M | +1.27% | 3.20 |

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
| Prezzo | $63,891 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +1.32% | movimento dell'ultimo giorno |
| Funding | +0.0100% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-11 02:00 | prossimo aggiornamento funding |
| Open Interest stimato | $1.97B | leva aperta stimata in dollari |
| Open Interest 24h | +3.02% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.84 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $51,113 | $76,669 |
| 10x | $57,502 | $70,280 |
| 20x | $60,696 | $67,086 |
| 50x | $62,613 | $65,169 |

### Note tecniche usate dallo score

- funding positivo: mercato leggermente carico di long
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
| Prezzo | $77.76 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -0.32% | movimento dell'ultimo giorno |
| Funding | +0.0091% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-11 02:00 | prossimo aggiornamento funding |
| Open Interest stimato | $243.12M | leva aperta stimata in dollari |
| Open Interest 24h | -23.02% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 2.71 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $62.21 | $93.31 |
| 10x | $69.98 | $85.54 |
| 20x | $73.87 | $81.65 |
| 50x | $76.20 | $79.32 |

### Note tecniche usate dallo score

- open interest in forte calo: parte della leva è già uscita
- long/short ratio alto: più mercato sbilanciato long

---

## Dogecoin — DOGE

### Lettura semplice

**NEUTRALE / POCO CHIARO**  
**Forza segnale: 1/5**

DOGE: i futures non danno una lettura chiara. Non si vede uno sbilanciamento forte né long né short.

**Tradotto operativamente:** Qui pesa di più il report frattale.

### Perché

- funding positivo: i long pagano gli short
- open interest abbastanza stabile
- long/short ratio alto: mercato più long

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $0.07395 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +1.40% | movimento dell'ultimo giorno |
| Funding | +0.0073% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-11 02:00 | prossimo aggiornamento funding |
| Open Interest stimato | $68.03M | leva aperta stimata in dollari |
| Open Interest 24h | +1.27% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 3.20 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $0.05916 | $0.08874 |
| 10x | $0.06656 | $0.08135 |
| 20x | $0.07025 | $0.07765 |
| 50x | $0.07247 | $0.07543 |

### Note tecniche usate dallo score

- long/short ratio alto: più mercato sbilanciato long

---
