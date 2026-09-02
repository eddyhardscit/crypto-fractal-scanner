# Report semplice futures / liquidazioni BTC / SOL / DOGE

Generato: **2026-09-02 07:32:33 CEST**  
UTC: **2026-09-02 05:32:33 UTC**

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
| BTC | 77.667 $ | -1.70% | +0.0086% | $2.23B | -11.54% | 1.94 |
| SOL | 100,24 $ | -3.75% | -0.0009% | $319.41M | -33.39% | 2.70 |
| DOGE | 0.08188 $ | -1.87% | +0.0100% | $84.37M | -0.55% | 4.78 |

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
| Prezzo | $77,670 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -1.70% | movimento dell'ultimo giorno |
| Funding | +0.0086% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-09-02 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $2.23B | leva aperta stimata in dollari |
| Open Interest 24h | -11.54% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.94 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $62,136 | $93,204 |
| 10x | $69,903 | $85,437 |
| 20x | $73,787 | $81,554 |
| 50x | $76,117 | $79,224 |

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
- open interest in calo: leva in uscita
- long/short ratio alto: mercato più long

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $100.19 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -3.75% | movimento dell'ultimo giorno |
| Funding | -0.0009% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-09-02 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $319.41M | leva aperta stimata in dollari |
| Open Interest 24h | -33.39% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 2.70 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $80.15 | $120.23 |
| 10x | $90.17 | $110.21 |
| 20x | $95.18 | $105.20 |
| 50x | $98.19 | $102.19 |

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
| Prezzo | $0.08188 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -1.87% | movimento dell'ultimo giorno |
| Funding | +0.0100% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-09-02 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $84.37M | leva aperta stimata in dollari |
| Open Interest 24h | -0.55% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 4.78 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $0.06550 | $0.09826 |
| 10x | $0.07369 | $0.09007 |
| 20x | $0.07779 | $0.08597 |
| 50x | $0.08024 | $0.08352 |

### Note tecniche usate dallo score

- funding positivo: mercato leggermente carico di long
- long/short ratio alto: più mercato sbilanciato long

---
