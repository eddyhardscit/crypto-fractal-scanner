# Report semplice futures / liquidazioni BTC / SOL / DOGE

Generato: **2026-09-16 07:32:39 CEST**  
UTC: **2026-09-16 05:32:39 UTC**

Fonte dati: **OKX Futures pubblici**.  
Questo report non è la vera heatmap CoinGlass. Serve a capire se il mercato futures è carico di long, short o leva.

## Traduzione in parole semplici

| Asset | Lettura | Forza | Cosa significa in pratica |
| --- | --- | --- | --- |
| BTC | Misto | 1/5 | Qui pesa di più il report frattale. |
| SOL | Misto | 1/5 | Qui pesa di più il report frattale. |
| DOGE | Leva alta, direzione mista | 3/5 | Meglio non forzare. Aspetta conferma dal frattale o dal prezzo. |

## Numeri principali

| Asset | Prezzo | Prezzo 24h | Funding | Open Interest | OI 24h | Long/Short |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 75.812 $ | -2.08% | +0.0053% | $2.13B | -5.23% | 2.02 |
| SOL | 97,07 $ | -3.73% | -0.0039% | $252.78M | -14.78% | 2.39 |
| DOGE | 0.08018 $ | -3.22% | +0.0068% | $79.37M | +5.31% | 5.19 |

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
| Prezzo | $75,801 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -2.08% | movimento dell'ultimo giorno |
| Funding | +0.0053% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-09-16 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $2.13B | leva aperta stimata in dollari |
| Open Interest 24h | -5.23% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 2.02 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $60,641 | $90,962 |
| 10x | $68,221 | $83,382 |
| 20x | $72,011 | $79,591 |
| 50x | $74,285 | $77,317 |

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
| Prezzo | $97.05 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -3.73% | movimento dell'ultimo giorno |
| Funding | -0.0039% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-09-16 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $252.78M | leva aperta stimata in dollari |
| Open Interest 24h | -14.78% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 2.39 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $77.64 | $116.46 |
| 10x | $87.34 | $106.76 |
| 20x | $92.20 | $101.90 |
| 50x | $95.11 | $98.99 |

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
| Prezzo | $0.08012 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -3.22% | movimento dell'ultimo giorno |
| Funding | +0.0068% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-09-16 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $79.37M | leva aperta stimata in dollari |
| Open Interest 24h | +5.31% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 5.19 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $0.06410 | $0.09614 |
| 10x | $0.07211 | $0.08813 |
| 20x | $0.07611 | $0.08413 |
| 50x | $0.07852 | $0.08172 |

### Note tecniche usate dallo score

- open interest in forte aumento: entra molta leva
- long/short ratio alto: più mercato sbilanciato long

---
