# Report semplice futures / liquidazioni BTC / SOL / DOGE

Generato: **2026-08-03 07:15:33 CEST**  
UTC: **2026-08-03 05:15:33 UTC**

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
| BTC | 62.760 $ | -0.96% | +0.0068% | $1.98B | +0.12% | 1.47 |
| SOL | 72,93 $ | -0.60% | +0.0010% | $213.81M | +30.27% | 1.49 |
| DOGE | 0.06985 $ | -0.43% | -0.0006% | $84.25M | -14.86% | 3.22 |

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
- open interest abbastanza stabile
- long/short ratio alto: mercato più long

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $62,816 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -0.96% | movimento dell'ultimo giorno |
| Funding | +0.0068% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-08-03 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $1.98B | leva aperta stimata in dollari |
| Open Interest 24h | +0.12% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.47 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $50,252 | $75,379 |
| 10x | $56,534 | $69,097 |
| 20x | $59,675 | $65,956 |
| 50x | $61,559 | $64,072 |

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
| Prezzo | $72.98 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -0.60% | movimento dell'ultimo giorno |
| Funding | +0.0010% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-08-03 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $213.81M | leva aperta stimata in dollari |
| Open Interest 24h | +30.27% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.49 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $58.38 | $87.58 |
| 10x | $65.68 | $80.28 |
| 20x | $69.33 | $76.63 |
| 50x | $71.52 | $74.44 |

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

- funding negativo: gli short pagano i long
- open interest in calo: leva in uscita
- long/short ratio alto: mercato più long

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $0.06990 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -0.43% | movimento dell'ultimo giorno |
| Funding | -0.0006% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-08-03 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $84.25M | leva aperta stimata in dollari |
| Open Interest 24h | -14.86% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 3.22 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $0.05592 | $0.08388 |
| 10x | $0.06291 | $0.07689 |
| 20x | $0.06641 | $0.07340 |
| 50x | $0.06850 | $0.07130 |

### Note tecniche usate dallo score

- open interest in forte calo: parte della leva è già uscita
- long/short ratio alto: più mercato sbilanciato long

---
