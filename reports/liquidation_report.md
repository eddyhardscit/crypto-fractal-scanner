# Report semplice futures / liquidazioni BTC / SOL / DOGE

Generato: **2026-10-23 07:33:44 CEST**  
UTC: **2026-10-23 05:33:44 UTC**

Fonte dati: **OKX Futures pubblici**.  
Questo report non è la vera heatmap CoinGlass. Serve a capire se il mercato futures è carico di long, short o leva.

## Traduzione in parole semplici

| Asset | Lettura | Forza | Cosa significa in pratica |
| --- | --- | --- | --- |
| BTC | Misto | 1/5 | Qui pesa di più il report frattale. |
| SOL | Rischio sotto | 4/5 | Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale. |
| DOGE | Leva alta, direzione mista | 3/5 | Meglio non forzare. Aspetta conferma dal frattale o dal prezzo. |

## Numeri principali

| Asset | Prezzo | Prezzo 24h | Funding | Open Interest | OI 24h | Long/Short |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 81.511 $ | -1.31% | +0.0077% | $2.57B | -1.15% | 0.96 |
| SOL | 104,09 $ | -0.64% | +0.0100% | $310.36M | +12.41% | 1.67 |
| DOGE | 0.07959 $ | -0.14% | +0.0088% | $100.71M | +12.50% | 2.83 |

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
- long/short ratio abbastanza equilibrato

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $81,732 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -1.31% | movimento dell'ultimo giorno |
| Funding | +0.0077% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-10-23 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $2.57B | leva aperta stimata in dollari |
| Open Interest 24h | -1.15% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 0.96 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $65,385 | $98,078 |
| 10x | $73,558 | $89,905 |
| 20x | $77,645 | $85,818 |
| 50x | $80,097 | $83,366 |

---

## Solana — SOL

### Lettura semplice

**RISCHIO DISCESA / FLUSH SOTTO**  
**Forza segnale: 4/5**

SOL: i futures sembrano più vulnerabili verso una discesa improvvisa. Non significa che deve scendere, ma se rompe sotto può accelerare.

**Tradotto operativamente:** Per un long a leva: prudenza alta. Guarda bene liquidazione e drawdown del report frattale.

### Perché

- funding positivo: i long pagano gli short
- open interest in aumento: più leva nel sistema
- long/short ratio alto: mercato più long

### Numeri controllati

| Dato | Valore | Traduzione |
| --- | --- | --- |
| Prezzo | $104.46 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -0.64% | movimento dell'ultimo giorno |
| Funding | +0.0100% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-10-23 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $310.36M | leva aperta stimata in dollari |
| Open Interest 24h | +12.41% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 1.67 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $83.57 | $125.35 |
| 10x | $94.01 | $114.91 |
| 20x | $99.24 | $109.68 |
| 50x | $102.37 | $106.55 |

### Note tecniche usate dallo score

- funding positivo: mercato leggermente carico di long
- open interest in forte aumento: entra molta leva
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
| Prezzo | $0.07983 | prezzo futures/mark usato come riferimento |
| Prezzo 24h | -0.14% | movimento dell'ultimo giorno |
| Funding | +0.0088% | positivo = long pagano; negativo = short pagano |
| Prossimo funding | 2026-10-23 10:00 | prossimo aggiornamento funding |
| Open Interest stimato | $100.71M | leva aperta stimata in dollari |
| Open Interest 24h | +12.50% | leva entrata o uscita nelle ultime 24h |
| Long/Short ratio | 2.83 | sopra 1 = più long; sotto 1 = più short |

### Livelli teorici di liquidazione

Questi NON sono la vera heatmap. Sono solo una stima semplice: se una posizione fosse aperta vicino al prezzo attuale, più o meno dove rischierebbe la liquidazione.

| Leva | Long liquidato circa sotto | Short liquidato circa sopra |
| --- | --- | --- |
| 5x | $0.06386 | $0.09580 |
| 10x | $0.07185 | $0.08781 |
| 20x | $0.07584 | $0.08382 |
| 50x | $0.07823 | $0.08143 |

### Note tecniche usate dallo score

- open interest in forte aumento: entra molta leva
- long/short ratio alto: più mercato sbilanciato long

---
