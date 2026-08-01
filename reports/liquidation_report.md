# Report semplice futures / liquidazioni BTC / SOL / DOGE

Generato: **2026-08-01 07:14:51 CEST**  
UTC: **2026-08-01 05:14:51 UTC**

Fonte dati: **OKX Futures pubblici**.  
Questo report non è la vera heatmap CoinGlass. Serve a capire se il mercato futures è carico di long, short o leva.

## Traduzione in parole semplici

| Asset | Lettura | Forza | Cosa significa in pratica |
| --- | --- | --- | --- |
| BTC | Misto | 1/5 | Qui pesa di più il report frattale. |
| SOL | Leva alta, direzione mista | 3/5 | Meglio non forzare. Aspetta conferma dal frattale o dal prezzo. |
| DOGE | Misto | 1/5 | Qui pesa di più il report frattale. |

## Numeri principali

| Asset | Prezzo | Prezzo 24h | Funding | Open Interest | OI 24h | Long/Short |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 63.065 $ | -2.02% | +0.0063% | $2.01B | -4.12% | 1.67 |
| SOL | 73,12 $ | -1.23% | +0.0042% | $213.07M | +18.80% | 1.45 |
| DOGE | 0.07009 $ | +0.06% | +0.0005% | $89.78M | -21.57% | 3.30 |

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
| Prezzo | $63,091 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -2.02% | movimento dell'ultimo giorno |
| Funding | +0.0063% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-08-01 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $2.01B | leva aperta stimata in dollari |
| Open Interest 24h | -4.12% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.67 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $50,473 | $75,709 |
| 10x | $56,782 | $69,400 |
| 20x | $59,937 | $66,246 |
| 50x | $61,829 | $64,353 |

### Note tecniche usate dallo score

- long/short ratio alto: più mercato sbilanciato long

---

## Solana — SOL

### Lettura semplice

**MOLTA LEVA MA DIREZIONE MISTA**  
**Forza segnale: 3/5**

SOL: c'è molta leva nel mercato, ma la direzione non è pulita. Può arrivare un movimento violento, ma non è chiaro se sopra o sotto.

**Tradotto operativamente:** Meglio non forzare. Aspetta conferma dal frattale o dal prezzo.

### Perché

- funding positivo: i long pagano gli short
- open interest in aumento: più leva nel sistema
- long/short ratio alto: mercato più long

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $73.14 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -1.23% | movimento dell'ultimo giorno |
| Funding | +0.0042% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-08-01 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $213.07M | leva aperta stimata in dollari |
| Open Interest 24h | +18.80% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.45 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $58.51 | $87.77 |
| 10x | $65.83 | $80.45 |
| 20x | $69.48 | $76.80 |
| 50x | $71.68 | $74.60 |

### Note tecniche usate dallo score

- open interest in forte aumento: entra molta leva
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
- open interest in calo: leva in uscita
- long/short ratio alto: mercato più long

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $0.07012 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | +0.06% | movimento dell'ultimo giorno |
| Funding | +0.0005% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-08-01 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $89.78M | leva aperta stimata in dollari |
| Open Interest 24h | -21.57% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 3.30 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $0.05610 | $0.08414 |
| 10x | $0.06311 | $0.07713 |
| 20x | $0.06661 | $0.07363 |
| 50x | $0.06872 | $0.07152 |

### Note tecniche usate dallo score

- open interest in forte calo: parte della leva è già uscita
- long/short ratio alto: più mercato sbilanciato long

---
