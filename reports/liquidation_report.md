# Report semplice futures / liquidazioni BTC / SOL / DOGE

Generato: **2026-07-10 10:37:28 CEST**  
UTC: **2026-07-10 08:37:28 UTC**

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
| BTC | $64,165 | +1.84% | +0.0094% | $1.98B | +2.09% | 1.92 |
| SOL | $79.25 | +1.27% | +0.0024% | $249.10M | -24.67% | 2.64 |
| DOGE | $0.07424 | +1.78% | +0.0100% | $70.50M | +0.48% | 3.11 |

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
| Prezzo | $64,165 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +1.84% | movimento dell'ultimo giorno |
| Funding | +0.0094% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-10 18:00 | prossimo aggiornamento funding |
| Open Interest stimato | $1.98B | leva aperta stimata in dollari |
| Open Interest 24h | +2.09% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.92 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $51,332 | $76,998 |
| 10x | $57,749 | $70,582 |
| 20x | $60,957 | $67,374 |
| 50x | $62,882 | $65,449 |

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
| Prezzo | $79.25 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +1.27% | movimento dell'ultimo giorno |
| Funding | +0.0024% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-10 18:00 | prossimo aggiornamento funding |
| Open Interest stimato | $249.10M | leva aperta stimata in dollari |
| Open Interest 24h | -24.67% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 2.64 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $63.40 | $95.10 |
| 10x | $71.33 | $87.18 |
| 20x | $75.29 | $83.21 |
| 50x | $77.66 | $80.84 |

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
| Prezzo | $0.07424 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +1.78% | movimento dell'ultimo giorno |
| Funding | +0.0100% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-10 18:00 | prossimo aggiornamento funding |
| Open Interest stimato | $70.50M | leva aperta stimata in dollari |
| Open Interest 24h | +0.48% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 3.11 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $0.05939 | $0.08909 |
| 10x | $0.06682 | $0.08166 |
| 20x | $0.07053 | $0.07795 |
| 50x | $0.07276 | $0.07572 |

### Note tecniche usate dallo score

- funding positivo: mercato leggermente carico di long
- long/short ratio alto: più mercato sbilanciato long

---
