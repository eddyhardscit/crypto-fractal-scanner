# Report semplice futures / liquidazioni BTC / SOL / DOGE

Generato: **2026-07-16 12:02:14 CEST**  
UTC: **2026-07-16 10:02:14 UTC**

Fonte dati: **OKX Futures pubblici**.  
Questo report non è la vera heatmap CoinGlass. Serve a capire se il mercato futures è carico di long, short o leva.

## Traduzione in parole semplici

| Asset | Lettura | Forza | Cosa significa in pratica |
| --- | --- | --- | --- |
| BTC | Leva alta, direzione mista | 3/5 | Meglio non forzare. Aspetta conferma dal frattale o dal prezzo. |
| SOL | Misto | 1/5 | Qui pesa di più il report frattale. |
| DOGE | Rischio sotto | 4/5 | Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale. |

## Numeri principali

| Asset | Prezzo | Prezzo 24h | Funding | Open Interest | OI 24h | Long/Short |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 64.026 $ | -0.98% | +0.0042% | $1.96B | +8.71% | 1.32 |
| SOL | 75,95 $ | -1.95% | +0.0022% | $225.89M | -13.02% | 2.16 |
| DOGE | 0.07304 $ | -0.95% | +0.0100% | $72.20M | +10.65% | 4.31 |

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

**MOLTA LEVA MA DIREZIONE MISTA**  
**Forza segnale: 3/5**

BTC: c'è molta leva nel mercato, ma la direzione non è pulita. Può arrivare un movimento violento, ma non è chiaro se sopra o sotto.

**Tradotto operativamente:** Meglio non forzare. Aspetta conferma dal frattale o dal prezzo.

### Perché

- funding positivo: i long pagano gli short
- open interest in aumento: più leva nel sistema
- long/short ratio alto: mercato più long

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $64,060 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -0.98% | movimento dell'ultimo giorno |
| Funding | +0.0042% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-16 18:00 | prossimo aggiornamento funding |
| Open Interest stimato | $1.96B | leva aperta stimata in dollari |
| Open Interest 24h | +8.71% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.32 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $51,248 | $76,872 |
| 10x | $57,654 | $70,466 |
| 20x | $60,857 | $67,263 |
| 50x | $62,779 | $65,341 |

### Note tecniche usate dallo score

- open interest in forte aumento: entra molta leva
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
| Prezzo | $76.01 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -1.95% | movimento dell'ultimo giorno |
| Funding | +0.0022% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-16 18:00 | prossimo aggiornamento funding |
| Open Interest stimato | $225.89M | leva aperta stimata in dollari |
| Open Interest 24h | -13.02% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 2.16 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $60.81 | $91.21 |
| 10x | $68.41 | $83.61 |
| 20x | $72.21 | $79.81 |
| 50x | $74.49 | $77.53 |

### Note tecniche usate dallo score

- open interest in forte calo: parte della leva è già uscita
- long/short ratio alto: più mercato sbilanciato long

---

## Dogecoin — DOGE

### Lettura semplice

**RISCHIO DISCESA / FLUSH SOTTO**  
**Forza segnale: 4/5**

DOGE: i futures sembrano più vulnerabili verso una discesa improvvisa. Non significa che deve scendere, ma se rompe sotto può accelerare.

**Tradotto operativamente:** Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale.

### Perché

- funding positivo: i long pagano gli short
- open interest in aumento: più leva nel sistema
- long/short ratio alto: mercato più long

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $0.07309 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -0.95% | movimento dell'ultimo giorno |
| Funding | +0.0100% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-07-16 18:00 | prossimo aggiornamento funding |
| Open Interest stimato | $72.20M | leva aperta stimata in dollari |
| Open Interest 24h | +10.65% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 4.31 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $0.05847 | $0.08771 |
| 10x | $0.06578 | $0.08040 |
| 20x | $0.06944 | $0.07674 |
| 50x | $0.07163 | $0.07455 |

### Note tecniche usate dallo score

- funding positivo: mercato leggermente carico di long
- open interest in forte aumento: entra molta leva
- long/short ratio alto: più mercato sbilanciato long

---
