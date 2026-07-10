# Report semplice futures / liquidazioni BTC / SOL / DOGE

Generato: **2026-07-10 20:24:20 CEST**  
UTC: **2026-07-10 18:24:20 UTC**

Fonte dati: **OKX Futures pubblici**.  
Questo report non è la vera heatmap CoinGlass. Serve a capire se il mercato futures è carico di long, short o leva.

## Traduzione in parole semplici

| Asset | Lettura | Forza | Cosa significa in pratica |
| --- | --- | --- | --- |
| BTC | Rischio sotto | 2/5 | Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale. |
| SOL | Rischio sotto | 2/5 | Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale. |
| DOGE | Misto | 1/5 | Qui pesa di più il report frattale. |

## Numeri principali

| Asset | Prezzo | Prezzo 24h | Funding | Open Interest | OI 24h | Long/Short |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | $63,918 | +1.08% | +0.0100% | $1.97B | +1.44% | 1.85 |
| SOL | $77.67 | -0.61% | +0.0100% | $242.94M | -23.81% | 2.72 |
| DOGE | $0.07400 | +1.11% | +0.0082% | $69.13M | +0.25% | 3.19 |

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
**Forza segnale: 2/5**

BTC: i futures sembrano più vulnerabili verso una discesa improvvisa. Non significa che deve scendere, ma se rompe sotto può accelerare.

**Tradotto operativamente:** Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale.

### Perché

- funding positivo: i long pagano gli short
- open interest abbastanza stabile
- long/short ratio alto: mercato più long

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $63,918 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +1.08% | movimento dell'ultimo giorno |
| Funding | +0.0100% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-11 02:00 | prossimo aggiornamento funding |
| Open Interest stimato | $1.97B | leva aperta stimata in dollari |
| Open Interest 24h | +1.44% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.85 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $51,134 | $76,701 |
| 10x | $57,526 | $70,309 |
| 20x | $60,722 | $67,113 |
| 50x | $62,639 | $65,196 |

### Note tecniche usate dallo score

- funding positivo: mercato leggermente carico di long
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
| Prezzo | $77.67 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -0.61% | movimento dell'ultimo giorno |
| Funding | +0.0100% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-11 02:00 | prossimo aggiornamento funding |
| Open Interest stimato | $242.94M | leva aperta stimata in dollari |
| Open Interest 24h | -23.81% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 2.72 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $62.14 | $93.20 |
| 10x | $69.90 | $85.44 |
| 20x | $73.79 | $81.55 |
| 50x | $76.12 | $79.22 |

### Note tecniche usate dallo score

- funding positivo: mercato leggermente carico di long
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
| Prezzo | $0.07400 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +1.11% | movimento dell'ultimo giorno |
| Funding | +0.0082% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-11 02:00 | prossimo aggiornamento funding |
| Open Interest stimato | $69.13M | leva aperta stimata in dollari |
| Open Interest 24h | +0.25% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 3.19 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $0.05920 | $0.08880 |
| 10x | $0.06660 | $0.08140 |
| 20x | $0.07030 | $0.07770 |
| 50x | $0.07252 | $0.07548 |

### Note tecniche usate dallo score

- long/short ratio alto: più mercato sbilanciato long

---
